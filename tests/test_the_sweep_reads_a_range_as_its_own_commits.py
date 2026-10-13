"""The survivor sweep reads a two-dot range as the commits it owns (#873).

`survivor_check.py#corrected` counts each file's sentences at the range's two
ends. On a two-dot range holding a merge of the base, the tree at the tip
carries everything the merge brought in, so a sentence another work item
corrected on the base read as wording THIS range removed, and its standing
twin was reported as this range's survivor. It is the shape #860 closed for
`round_record.py#touched`, one script over.

`docs/the-record-layout.md` §*A range owns the commits that descend from its
start* owns which commits a range owns, and `chain_check.py#own_commits` is
its one reader. This module holds the sweep to it with the history the frame
measured (`spec.md` §*Measured in this frame* of work item 1791852614):
`base` holds the files, `feature` is cut from it and makes `f1`, the base
makes `S1`, and `feature` merges the base and makes `f2`. Every case builds
that history with whatever each commit writes, and asks the sweep as a
person would, through its command line.

The history is built with the helpers of
`tests/test_a_range_owns_what_git_lists_for_it.py`, which already build merge
shapes, and git is driven from Python (contract §8).
"""

import importlib.util
import os
import re
import subprocess
import sys

from test_a_range_owns_what_git_lists_for_it import commit, merge, switch
from test_the_record_is_generated import git, write

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "skills", "code-review", "scripts", "survivor_check.py")

# The base's correction. Two stretches of shared wording with unshared words
# between them, which is the shape the floor is set for: a single contiguous
# change shares one run and is correctly not reported.
FOUND = (
    "The verdict cell is written by the reviewing round itself and the "
    "orchestrator never edits it afterwards."
)
REPAIRED = (
    "The verdict cell is written by the generator and the "
    "orchestrator leaves it untouched afterwards."
)

# Enough unrelated files that a phrase two files carry still weighs most of
# a phrase nothing else carries, so a case can share one without dropping a
# survivor under the floor for a reason the case is not about.
FILLER = {
    f"filler/{n:02}.md": f"# filler {n}\n\nUnrelated prose, item {n}, shares nothing.\n"
    for n in range(30)
}


def doc(title, *sentences):
    """A markdown file: a heading, then each sentence on its own line,
    the first one on line 3."""
    return f"# {title}\n\n" + "\n\n".join(sentences) + "\n"


def put(repo, message, files):
    """One commit writing `files`, its SHA."""
    for rel, text in files.items():
        write(repo, rel, text)
    git(repo, "add", "-A")
    return commit(repo, message)


def history(repo, root=None, s1=None, f1=None, f2=None):
    """The measured history, each commit writing what the case hands it.

    `{name: sha}` for `root`, `f1`, `S1`, the merge and `f2`. `feature` is
    checked out at `f2` when this returns."""
    repo.mkdir()
    git(repo, "init", "-q", "-b", "base")
    shas = {"root": put(repo, "root", {**FILLER, **(root or {})})}
    switch(repo, "-c", "feature")
    shas["f1"] = put(repo, "f1", f1 or {"f.md": doc("f", "The first step.")})
    switch(repo, "base")
    shas["S1"] = put(repo, "S1", s1 or {"s.md": doc("s", "The base moves on.")})
    switch(repo, "feature")
    shas["merge"] = merge(repo, "the branch merges the base", "base")
    shas["f2"] = put(repo, "f2", f2 or {"f.md": doc("f", "The second step.")})
    return shas


def sweep(repo, spec, *extra):
    """`(exit code, stdout + stderr)` of the sweep over `spec`."""
    out = subprocess.run(
        [sys.executable, SCRIPT, "--range", spec, "--root", str(repo), *extra],
        cwd=str(repo),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    return out.returncode, out.stdout + out.stderr


def module():
    spec = importlib.util.spec_from_file_location("specseal_survivor_check", SCRIPT)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


# --- S7: a start that does not reach its end ----------------------------------


def test_a_two_dot_start_that_does_not_reach_its_end_is_refused(tmp_path):
    """S7. `S1` is the base's commit and `f1` the branch's, made before the
    branch merged the base: the range `S1..f1` owns no commit. Read at its
    two ends it measured two unrelated trees; it is refused at exit 2,
    naming both ends and the spelling that reads a branch from the base.
    Seen red against `parse_range` as it stood: exit 0, a report."""
    repo = tmp_path / "repo"
    shas = history(repo)
    code, text = sweep(repo, f"{shas['S1']}..{shas['f1']}")
    assert code == 2, f"a range that owns nothing was measured; exit {code}\n{text}"
    assert shas["S1"][:8] in text and shas["f1"][:8] in text, text
    assert "is not an ancestor of" in text, text
    assert "Write `A...B`" in text, text
    assert "survivor-check: examined" not in text, f"a report was printed:\n{text}"


def test_a_declaration_spelled_with_such_a_start_prints_what_it_printed(tmp_path):
    """S7, its other half. The refusal is the run's own `--range`'s, never
    `whole_range`'s: a `survivors.md` row spelled `S1..f1` still resolves as
    a range this run is not over, and prints nothing. Refusing it in
    `parse_range`, where `whole_range` also resolves, would print it under
    `unresolved` to every run that could have used it (plan alternative H).
    Seen red with the refusal moved into `parse_range`."""
    repo = tmp_path / "repo"
    shas = history(repo)
    rows = tmp_path / "survivors.md"
    rows.write_text(
        "| Range | Grounds |\n|---|---|\n"
        f"| `{shas['S1']}..{shas['f1']}` | a range whose start is on the base |\n",
        encoding="utf-8",
    )
    spec = f"{shas['root']}..{shas['f1']}"
    bare = sweep(repo, spec)
    declared = sweep(repo, spec, "--exempt", str(rows))
    assert declared == bare, (
        "a declaration whose start does not reach its end changed what a run "
        f"over another range prints:\nwithout it:\n{bare[1]}\nwith it:\n"
        f"{declared[1]}"
    )
    assert "unresolved" not in declared[1], declared[1]


# --- S8: a copy without its sibling -------------------------------------------


def test_a_copy_without_the_chain_checker_refuses_a_two_dot_range(tmp_path, capsys):
    """S8. `chain_check.py` ships beside the sweep and says which commits a
    two-dot range owns. A copy without it cannot say, and that is unusable
    input -- exit 2 and a sentence naming what the sibling is for -- never a
    quiet reading of the two ends as the range's own. The shape
    `seal/releases/0.15.4.md` P4 pins for `evidence_check.py`. Seen red with
    the missing-file test disabled: the load raised a traceback."""
    repo = tmp_path / "repo"
    shas = history(repo)
    loaded = module()
    loaded.CHAIN = str(tmp_path / "gone" / "chain_check.py")
    code = loaded.main(["--range", f"{shas['f1']}..{shas['f2']}", "--root", str(repo)])
    err = capsys.readouterr().err
    assert code == 2, f"exit {code}\n{err}"
    assert re.search(r"chain_check\.py, which says which commits", err), err

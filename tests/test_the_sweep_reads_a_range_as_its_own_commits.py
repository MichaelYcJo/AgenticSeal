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
    checked out at `f2` when this returns. Each commit also adds a file of
    its own that no other commit touches, so every commit changes something
    and two cases differing in one file differ in nothing else at the tip."""
    repo.mkdir()
    git(repo, "init", "-q", "-b", "base")
    shas = {"root": put(repo, "root", {**FILLER, **(root or {})})}
    switch(repo, "-c", "feature")
    shas["f1"] = put(repo, "f1", {"f1.md": doc("f1", "A first step."), **(f1 or {})})
    switch(repo, "base")
    shas["S1"] = put(
        repo, "S1", {"s1.md": doc("s1", "The base moves on."), **(s1 or {})}
    )
    switch(repo, "feature")
    shas["merge"] = merge(repo, "the branch merges the base", "base")
    shas["f2"] = put(repo, "f2", {"f2.md": doc("f2", "A second step."), **(f2 or {})})
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


def removed(text):
    """How many sentences the report says the range removed."""
    found = re.search(r"against (\d+) sentence\(s\) the range", text)
    assert found, f"no report line:\n{text}"
    return int(found.group(1))


def block(text, path):
    """The report's lines for the survivor at `path`, or None."""
    lines = text.splitlines()
    for at, line in enumerate(lines):
        if line.startswith(f"{path}:"):
            return lines[at : at + 4]
    return None


def score_of(text, path):
    """The score the report gives the survivor at `path`."""
    lines = block(text, path)
    assert lines, f"{path} is not reported:\n{text}"
    found = re.search(r"phrase\(s\), ([\d.]+):", lines[3])
    assert found, lines
    return float(found.group(1))


# The branch's own correction, in the same two-stretch shape. `copy.md`
# carries its twin; `other.md` is where `f2` corrects it.
OWN_FOUND = (
    "The ledger row is stamped by the release itself and the session never "
    "rewrites it later."
)
OWN_REPAIRED = (
    "The ledger row is stamped by the fold and the session leaves it alone later."
)
# A sentence holding the whole first stretch `OWN_FOUND` lost and nothing of
# the second, so counted as written it takes one of the two runs away.
ECHO = "Nothing here is ruled by the release itself and the clock alone."


# --- S1-S4: a two-dot range holding a merge of the base -------------------------


def test_a_correction_the_merge_brought_in_is_not_this_ranges(tmp_path):
    """S1, the shape the frame measured. `S1` corrects `notes.md` on the base
    and leaves its twin in `docs.md`; `f1` and `f2` touch neither. Over
    `f1..f2`, which holds the merge, the sweep read `S1`'s correction as this
    range's and reported `docs.md`. Seen red against `corrected` as it
    stood: exit 1, `docs.md:3` reported, one sentence removed."""
    repo = tmp_path / "repo"
    shas = history(
        repo,
        root={"notes.md": doc("notes", FOUND), "docs.md": doc("docs", FOUND)},
        s1={"notes.md": doc("notes", REPAIRED)},
    )
    code, text = sweep(repo, f"{shas['f1']}..{shas['f2']}")
    assert code == 0, f"the base's correction was read as this range's:\n{text}"
    assert removed(text) == 0, text
    assert "docs.md" not in text, text


def test_an_own_correction_beside_the_merge_is_still_measured(tmp_path):
    """S2. The same history, and `f2` corrects `other.md`, whose twin stands
    in `copy.md`. The own correction is reported with the sentence it
    corrected, and the base's is not. Seen red against a filter that drops
    every sentence."""
    repo = tmp_path / "repo"
    shas = history(
        repo,
        root={
            "notes.md": doc("notes", FOUND),
            "docs.md": doc("docs", FOUND),
            "other.md": doc("other", OWN_FOUND),
            "copy.md": doc("copy", OWN_FOUND),
        },
        s1={"notes.md": doc("notes", REPAIRED)},
        f2={"other.md": doc("other", OWN_REPAIRED)},
    )
    code, text = sweep(repo, f"{shas['f1']}..{shas['f2']}")
    assert code == 1, f"the own correction's twin was not reported:\n{text}"
    assert removed(text) == 1, text
    lines = block(text, "copy.md")
    assert lines and "corrected   other.md:3" in lines[2], text
    assert "docs.md" not in text, text


def own_correction_score(tmp_path, name, echo_on_the_base):
    """The score of `f2`'s survivor where `ECHO` stands in `echo.md` at the
    tip: written by `S1` when `echo_on_the_base`, else already in `root`.
    The tree at the tip is the same either way, so the pool and every
    phrase's weight are too."""
    repo = tmp_path / name
    root = {"other.md": doc("other", OWN_FOUND), "copy.md": doc("copy", OWN_FOUND)}
    s1 = None
    if echo_on_the_base:
        s1 = {"echo.md": doc("echo", ECHO)}
    else:
        root["echo.md"] = doc("echo", ECHO)
    shas = history(repo, root=root, s1=s1, f2={"other.md": doc("other", OWN_REPAIRED)})
    code, text = sweep(repo, f"{shas['f1']}..{shas['f2']}")
    assert code == 1, f"{name}: exit {code}\n{text}"
    return score_of(text, "copy.md")


def test_wording_the_merge_brought_in_does_not_subtract_an_own_survivor(tmp_path):
    """S3. `S1` writes a sentence holding a stretch of what `f2` corrects.
    Counted as written by this range it would take that stretch out of the
    wording looked for, and the survivor would drop under the floor. It is
    reported at the score it has where the same sentence stood before the
    range. Seen red against a filter of `gone` alone: `copy.md` not
    reported."""
    before = own_correction_score(tmp_path, "already", echo_on_the_base=False)
    merged = own_correction_score(tmp_path, "merged", echo_on_the_base=True)
    assert merged == before, (
        f"the merged side's wording moved the own survivor's score from "
        f"{before} to {merged}"
    )


def test_a_file_both_sides_changed_keeps_only_the_own_sentence(tmp_path):
    """S4. `shared.md` holds both claims; `S1` corrects one there and `f2`
    the other, each with a twin elsewhere. Per sentence, not per path: `f2`'s
    twin is reported and `S1`'s is not. Seen red against a restriction of
    the paths alone (plan alternative D): `docs.md` reported as well."""
    repo = tmp_path / "repo"
    shas = history(
        repo,
        root={
            "shared.md": doc("shared", FOUND, OWN_FOUND),
            "docs.md": doc("docs", FOUND),
            "copy.md": doc("copy", OWN_FOUND),
        },
        s1={"shared.md": doc("shared", REPAIRED, OWN_FOUND)},
        f2={"shared.md": doc("shared", REPAIRED, OWN_REPAIRED)},
    )
    code, text = sweep(repo, f"{shas['f1']}..{shas['f2']}")
    assert code == 1, text
    assert block(text, "copy.md"), f"f2's survivor was not reported:\n{text}"
    assert "docs.md" not in text, f"S1's survivor was reported:\n{text}"
    assert removed(text) == 1, text


# --- S6: `A...B` reads its two ends ---------------------------------------------


def test_a_three_dot_range_reads_its_two_ends_from_the_merge_base(tmp_path):
    """S6. `f1` corrects `other.md` and the branch merges the base after it.
    `base...feature` starts at the merge base, `S1`, and `f1` is not on an
    ancestry path from there: read as its own commits the range would drop
    `f1`'s correction. Read at its two ends, `copy.md` is reported. Seen red
    with the own-commits pass applied to `A...B` (plan alternative F)."""
    repo = tmp_path / "repo"
    history(
        repo,
        root={"other.md": doc("other", OWN_FOUND), "copy.md": doc("copy", OWN_FOUND)},
        f1={"other.md": doc("other", OWN_REPAIRED)},
    )
    code, text = sweep(repo, "base...feature")
    assert code == 1, f"f1's survivor was not reported:\n{text}"
    assert block(text, "copy.md"), text
    assert "not read" not in text, f"`A...B` named commits it did not read:\n{text}"


# --- round 1's 🟡 1: what a two-dot range lists and does not own ---------------


def test_a_two_dot_range_names_the_commits_it_does_not_read(tmp_path):
    """Round 1's 🟡 1. `base..feature` after the branch merged the base's tip
    resolves to the same two commits as `base...feature` and owns `f2` alone,
    so `f1`'s correction is not read. The report names `f1` as not read and
    names `A...B`, rather than reporting a clean range in silence. Seen red
    against the sweep as it stood at round 1's target: exit 0, 0 removed,
    nothing naming `f1`."""
    repo = tmp_path / "repo"
    shas = history(
        repo,
        root={"other.md": doc("other", OWN_FOUND), "copy.md": doc("copy", OWN_FOUND)},
        f1={"other.md": doc("other", OWN_REPAIRED)},
    )
    _code, text = sweep(repo, "base..feature")
    assert "not read    1 commit(s)" in text, text
    assert shas["f1"][:7] in text, text
    assert "write `A...B`" in text, text


def test_the_base_commit_a_two_dot_range_leaves_out_is_named(tmp_path):
    """Round 1's 🟡 1, S1's shape. Over `f1..f2` the base's `S1` is listed
    and not owned, and the line that names it is what says why its
    correction counted nothing. Seen red against the sweep as it stood at
    round 1's target: no line names `S1`."""
    repo = tmp_path / "repo"
    shas = history(
        repo,
        root={"notes.md": doc("notes", FOUND), "docs.md": doc("docs", FOUND)},
        s1={"notes.md": doc("notes", REPAIRED)},
    )
    code, text = sweep(repo, f"{shas['f1']}..{shas['f2']}")
    assert code == 0, text
    assert "not read    1 commit(s)" in text, text
    assert shas["S1"][:7] in text, text
    named = text.split("does not own:", 1)[1].split(".", 1)[0]
    assert shas["f2"][:7] not in named, (
        f"an owned commit was named as not read:\n{text}"
    )


# --- round 1's 🟡 2: own commits that cannot be listed ------------------------


def test_a_range_whose_own_commits_cannot_be_listed_is_refused(tmp_path, capsys):
    """Round 1's 🟡 2. `own_commits` answers None where git fails and raises
    `subprocess.TimeoutExpired` where its 60 s timeout expires. Either is
    unusable input, exit 2, never a traceback at exit 1, which is the
    survivors code. Seen red with the `try` removed: the timeout escaped
    `main`."""
    repo = tmp_path / "repo"
    shas = history(repo)
    for failure in (None, subprocess.TimeoutExpired(["git", "log"], 60)):
        loaded = module()
        real = loaded.chain()

        class Stub:
            is_ancestor = staticmethod(real.is_ancestor)

            @staticmethod
            def own_commits(root, a, b, failure=failure):
                if failure is None:
                    return None
                raise failure

        loaded.chain = lambda stub=Stub: stub
        code = loaded.main(
            ["--range", f"{shas['f1']}..{shas['f2']}", "--root", str(repo)]
        )
        err = capsys.readouterr().err
        assert code == 2, f"{failure!r}: exit {code}\n{err}"
        assert "cannot list the commits" in err, err


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

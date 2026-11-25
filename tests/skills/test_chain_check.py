"""`skills/code-review/scripts/chain_check.py`, one class per function.

Rebuilt by #942's phase 5. The readers of a round record's `seal` blocks
and the reference channel run in the process on text. `main` runs in the
process over a repository built once for the module and copied for each
case that judges it: a branch with a routing declaration, a code commit, two
round records and the closing records, judged as a ready or a draft pull
request through the event payload GitHub writes. Each copy is the reset.

The arms `main` calls are called in the process with their input given
(#1581's phases 2 and 3): a record through `read_record` replaced for the
case (`reading`), the round records the records arm reads (`records_read`),
a design and the files beside it read from a copy's working tree under
`WORKTREE`, or an argument such as `originals_of`'s paths. A case doing so
over a world it never writes takes the module's template itself,
`_branch_template`, `_item_template` or `_bodied_template`, with no copy,
and so does a `main` run whose records reach it through `reading`, since
`main` without `--worktree` writes nothing into the repository it reads.
Each arm keeps the `main` runs over a real repository that show `main`
reaches it, and the cases whose fact is which records `main` hands the arm
or what `main` makes of the arm's answer: the exit code a draft and
`--sealing` give, and where a not-read line is printed.

Since #1581's phase 9 the module's three templates are written by `git
fast-import` (`imported`), and a `main` run whose fact is what an arm makes
of the records runs with the readers that ask git what HEAD carries
answered from the disk and `follows` answering that nothing follows
(`answered`). The diff, the merge base, the trailers, the root's entry and
a fixed commit's ancestry stay git's in every run. `Test_main`'s first case
runs every reader real, and each reader the seam answers keeps cases of its
own over a real history (`Test_follows`, the records arm's cases about what
a later commit touched).

The cases about the root beside a project's own `seal/` package (#1059)
call the reader of the root's name, `root_name` or
`declared_for_this_branch`, with its input given; the ones whose fact only
`main` holds build `tests/conftest.py`'s `shared` repository, whose root
stands at `agentic-seal/`.
`Test_module` holds the copy run without its siblings, from
`tests/test_a_script_copied_alone_exits_2.py`, and the framer's mark after
a U+2028, `frame_foot`'s one case, from
`tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py`, which came in
its round 9 fix pass, each a case of this module alone.

The predicates the check asks git, `commit_of`, `resolves`, `merge_base`,
`settled` and `tree_at`, and the policy root's reader came here from
`skills/verify/scripts/unverified_check.py` (#1482), and their cases from
`tests/skills/test_unverified_check.py`, unchanged but for the module they
call. They read the worlds that file builds once, imported from it.
"""

import functools
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys

import conftest
import pytest
import test_unverified_check
from conftest import (
    BASELINE,
    LS,
    census_case,
    chain_check_run,
    commit_everything_as_e,
    config_json,
    git_out,
    mark_root,
    parity_file,
    write,
)
from conftest import commit_everything as commit
from conftest import git_out as git
from conftest import load_module as load
from conftest import seal_block as block
from test_settle import asks, past_the_bound, repeated, unanswered
from test_unverified_check import (
    CANONICAL,
    CLOSED_ITEM,
    DROPPED,
    OPEN_ITEM,
    SETTLE_A,
    SETTLE_BAD,
    SETTLE_C,
    _committed,
    copy_of,
    memo,
)

TARGET = "skills/code-review/scripts/chain_check.py"

ROOT = pathlib.Path(conftest.ROOT)
CHAIN = ROOT / TARGET
READER = ROOT / "lib" / "lines.py"
TABLES = ROOT / "lib" / "tables.py"
ITEM = "seal/threads/1791999999-a-work-item"
# The pictographs and symbols a mark is drawn from: the colour circles and
# squares, the check and cross marks, the question mark ornament and the
# variation selector that follows them.
EMOJI = re.compile("[⌀-⏿☀-➿⬀-⯿️\U0001f000-\U0001faff]")

chain = load(CHAIN, "chain_check_under_test")
reader = load(READER, "lines_reader_for_chain_tests")
tables = load(TABLES, "tables_for_chain_tests")
check = functools.partial(chain_check_run, chain)
# The worlds the predicates moved from `unverified_check.py` read, fixtures
# built once in the file this one imports them from.
plain = test_unverified_check.plain
forked = test_unverified_check.forked
settle = test_unverified_check.settle
joined = test_unverified_check.joined
# A work item id git quotes under the default `core.quotePath` (#1283).
NON_ASCII = "1780000012-정렬"

ROUTING = """# a work item -- routing

| Axis | Answer |
|---|---|
| Review | {review} |
| Destination | open the pull request |
| Planning | {planning} |
| Branch | feature/x |
"""


FENCE = "`" * 3


def close(verdict, answer="done", location=None):
    """A finding's close block as the fix pass appends it: its `verdict:`,
    its `answer:` and, where a fix went elsewhere, its `location:`."""
    lines = [f"verdict: {verdict}", f"answer: {answer}"]
    return block(*lines, *([f"location: {location}"] if location else []))


def finding(
    n,
    verdict,
    severity="must",
    title="the parser drops a row",
    location="`f.txt:1`",
    regression=None,
    reopens=None,
    evidence="read `f.txt:1`",
):
    """One `### ` section of `## Findings`, in `templates/records/sdd-round.md`'s
    shape: its finding block, with an `evidence:` line reading `evidence`
    or none where that is None, why it matters, the fix's fence, and a close
    block reading `verdict`, or none where `verdict` is `open`."""
    fields = [f"severity: {severity}", f"location: {location}"]
    fields += [f"evidence: {evidence}"] if evidence is not None else []
    fields += [f"regression: {regression}"] if regression else []
    fields += [f"reopens: {reopens}"] if reopens else []
    return (
        f"### {n}. {title}\n\n" + block(*fields) + "\nWhy it matters.\n\n"
        "```python\nx = 1\n```\n" + ("" if verdict == "open" else "\n" + close(verdict))
    )


def confirm(reference, what="the fix holds"):
    """One entry of `## Confirmations`: its confirmation block reading
    `reference`, then the prose saying what holds, where and how."""
    return block(f"confirms: {reference}") + f"{what}, at `f.txt:1`. read.\n\n"


def record(target, findings=(), confirmations="", n=1):
    """A round record in `templates/records/sdd-round.md`'s shape: its round
    block, `findings` the `finding()` sections, `confirmations` entries of
    `## Confirmations`."""
    return (
        f"# 1791999999-a-work-item — review round {n}\n\n"
        + block(f"target: {target} against main")
        + "\n## Findings\n\n"
        + "\n".join(findings)
        + "\n## Confirmations\n\n"
        f"{confirmations}\n"
        "## Not judged\n\n"
        "| What | Location | Who answers |\n|---|---|---|\n\n"
        "## Probes\n\n"
        "| Command | Result |\n|---|---|\n"
    )


def line_at(text, line, k=0):
    """The 1-based number of the K-th line of TEXT equal to LINE."""
    return [i + 1 for i, said in enumerate(text.split("\n")) if said == line][k]


def opener_at(text, first, k=0):
    """The 1-based number of the opener of the K-th block of TEXT whose first
    line is FIRST."""
    lines = text.split("\n")
    return [
        i + 1
        for i, said in enumerate(lines[:-1])
        if said == FENCE + "seal" and lines[i + 1] == first
    ][k]


def rounds_of(*texts):
    """The records `texts`, numbered from 1, read as `channel` takes them."""
    out, errors = [], []
    for n, text in enumerate(texts, 1):
        read, said = chain.round_of(text, f"round-{n}.md", n)
        out.append(read)
        errors.extend(said)
    return out, errors


# The table the old generator's records carried, which the check never judges
# again: a merged item keeps one in the fixture, and the check must never open
# it.
OLD_RECORD = (
    "# 1788999999-a-merged-item — review round 1\n\n"
    "| Field | Value |\n|---|---|\n"
    "| Target SHA | 0000000 against main |\n\n"
    "## Verdicts\n\n"
    "| # | Finding | Location | Verdict | Grounds |\n"
    "|---|---|---|---|---|\n"
    "| 🔴 1 | wrong | `f.txt:1` | open | g |\n"
)
MERGED_ITEM = "seal/threads/1788999999-a-merged-item"


# The base commit a fixture's run names; no arm reads it.
GATE_BASE = "fedcba9"


def gate_file(*runs):
    """A `trail/gate.md` holding one run block per commit of RUNS, in the
    order `seal gate --record` appends them, the last the newest."""
    blocks = "\n".join(
        f"```seal\nrun: {sha} against {GATE_BASE}\n```\n" for sha in runs
    )
    return f"# 1791999999-a-work-item — broad gate\n\n{blocks}"


def verdict_block(sha, verdict="sealed", original=None):
    """One verdict block of a `guarantee.md`, as the sealer appends it."""
    lines = [f"target: {sha} against main"]
    if original is not None:
        lines.append(f"original: {original}")
    lines.append(f"Verdict: {verdict}")
    return "```seal\n" + "\n".join(lines) + "\n```\n"


def guarantee_file(sha, verdict="sealed"):
    return "# 1791999999-a-work-item — guarantee\n\n" + verdict_block(sha, verdict)


SPEC = "# spec\n\nbody\n\nFramed 2026-10-15 by framer, before the build.\n"


def init(d):
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "t@t")
    git(d, "config", "user.name", "t")


def born(d, head):
    """D made an empty repository whose HEAD names the branch HEAD, and
    whose own commits are t's, as `init` makes them, the identity written
    into its config rather than set by two more git processes."""
    d.mkdir(parents=True)
    git(d, "init", "-q", "-b", head)
    with open(d / ".git" / "config", "a", encoding="utf-8") as f:
        f.write("[user]\n\temail = t@t\n\tname = t\n")


def imported(d, *commits, at=1700000000):
    """The ids of COMMITS, written into the repository at D by one `git
    fast-import`, where committing each through the working tree takes three
    processes of its own (#1581's phase 9).

    Each of COMMITS is `(ref, start, message, files)`: a commit on the branch
    REF whose parent is START, a branch, a commit id or the `:<n>` mark of
    this call's N-th commit, or REF's previous commit of this call where
    START is None, a root where REF has none; a tuple START is a merge of
    its parents, the first one's tree under FILES. FILES maps a path to its
    text, or to None to delete it, a directory whole. Every commit is t's,
    one second after AT and each a second after the one before, so a world
    built on two workers is one history. The working tree is not touched."""

    def blob(text):
        data = text.encode("utf-8")
        return b"data %d\n%s\n" % (len(data), data)

    stream = []
    for n, (ref, start, message, files) in enumerate(commits, 1):
        who = f"t <t@t> {at + n} +0000\n"
        head = f"commit refs/heads/{ref}\nmark :{n}\nauthor {who}committer {who}"
        stream.append(head.encode() + blob(message))
        first, *merged = start if isinstance(start, tuple) else (start,)
        if first is not None:
            stream.append(f"from {first}\n".encode())
        stream.extend(f"merge {parent}\n".encode() for parent in merged)
        for path, text in files.items():
            if text is None:
                stream.append(f"D {path}\n".encode())
            else:
                stream.append(f"M 100644 inline {path}\n".encode() + blob(text))
        stream.append(b"\n")
    marks = d / ".git" / "marks"
    subprocess.run(
        ["git", "-C", str(d), "fast-import", "--quiet", f"--export-marks={marks}"],
        input=b"".join(stream),
        check=True,
        capture_output=True,
    )
    ids = dict(line.split() for line in marks.read_text(encoding="utf-8").splitlines())
    marks.unlink()
    return [ids[f":{n}"] for n in range(1, len(commits) + 1)]


@pytest.fixture(scope="module")
def _branch_template(tmp_path_factory):
    """A repository whose `feature/x` declares a work item and reviewed it,
    built once for the module.

    `main` holds one file, the root's marked `README.md`, and a work item
    another pull request merged, its declaration naming another branch and
    its one record in the old table's shape with a finding open (S11).
    `feature/x` adds the declaration, a code commit, round 1 at that commit
    with its one finding `fixed` by it, round 2, the verifying round,
    confirming `round-1#1` with nothing of its own, and the closing records. Three `git fast-import` runs write it, since
    each record names a commit the one before wrote. Returns `(root, code
    commit)`."""
    d = tmp_path_factory.mktemp("chain-world") / "r"
    born(d, "feature/x")
    merged = ROUTING.format(
        review="through the review chain", planning="the session"
    ).replace("feature/x", "feature/merged")
    _base, _routing, code = imported(
        d,
        (
            "main",
            None,
            "base",
            {
                "f.txt": "one\n",
                "seal/README.md": conftest.ROOT_MARKER + "\n",
                f"{MERGED_ITEM}/routing.md": merged,
                f"{MERGED_ITEM}/trail/rounds/round-1.md": OLD_RECORD,
            },
        ),
        (
            "feature/x",
            ":1",
            "routing",
            {
                f"{ITEM}/routing.md": ROUTING.format(
                    review="through the review chain", planning="the session"
                )
            },
        ),
        ("feature/x", None, "code", {"f.txt": "two\n"}),
    )
    _round, reviewed = imported(
        d,
        (
            "feature/x",
            code,
            "the round record",
            {
                f"{ITEM}/trail/rounds/round-1.md": record(
                    code, [finding(1, f"fixed {code[:8]}")]
                )
            },
        ),
        (
            "feature/x",
            None,
            "the verifying round",
            {
                f"{ITEM}/trail/rounds/round-2.md": record(
                    code, confirmations=confirm("round-1#1"), n=2
                )
            },
        ),
        at=1700000010,
    )
    # Two runs, the newest last: the earlier one names a commit nobody can
    # see, so a reader that took any run but the last would refuse the file.
    imported(
        d,
        (
            "feature/x",
            reviewed,
            "the closing records",
            {
                f"{ITEM}/trail/gate.md": gate_file("1" * 40, reviewed),
                f"{ITEM}/guarantee.md": guarantee_file(reviewed),
            },
        ),
        at=1700000020,
    )
    git(d, "reset", "-q", "--hard")
    return d, code


@pytest.fixture
def branch(tmp_path, _branch_template):
    """A copy of the module's branch for one case, which the case may change."""
    template, code = _branch_template
    d = tmp_path / "r"
    shutil.copytree(template, d)
    return d, code


def seal(d):
    """The closing records naming HEAD, committed: what a branch carries
    once the sealer has audited what is on it."""
    head = git(d, "rev-parse", "HEAD")
    write(d, f"{ITEM}/trail/gate.md", gate_file(head))
    write(d, f"{ITEM}/guarantee.md", guarantee_file(head))
    commit(d, "the closing records, again")


def event(tmp_path, monkeypatch, draft):
    path = tmp_path / "event.json"
    path.write_text(json.dumps({"pull_request": {"draft": draft}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(path))
    return path


@pytest.fixture
def ready(tmp_path, monkeypatch):
    return event(tmp_path, monkeypatch, False)


@pytest.fixture
def draft(tmp_path, monkeypatch):
    return event(tmp_path, monkeypatch, True)


def reading(monkeypatch, texts):
    """`chain.read_record` answering TEXTS, `{path: text or None}`, for each
    path it holds and as git carries HEAD for every other, so a case hands
    an arm its records without writing into a world. `WORKTREE` is held
    False for the case, since `main` leaves it as its last run set it."""
    real = chain.read_record
    monkeypatch.setattr(chain, "WORKTREE", False)
    monkeypatch.setattr(
        chain,
        "read_record",
        lambda root, rel: texts[rel] if rel in texts else real(root, rel),
    )


def on_disk(root, rel):
    """REL's text as the working tree at ROOT holds it, or None where it
    holds no file there: `read_record` under `WORKTREE`, whatever the run
    set it to."""
    try:
        with open(os.path.join(root, *rel.split("/")), encoding="utf-8") as f:
            return f.read()
    except OSError:
        return None


def answered(monkeypatch, real=()):
    """`main`'s readers that ask git what HEAD carries answered from the
    disk, and `follows` answering that nothing outside the work item's
    records follows, for a case whose fact is what an arm makes of the
    records, not what git answers of them (#1581's phase 9).

    `read_record` reads the working tree, which a case leaves as HEAD
    carries it; `tracked_files` lists it, as `worktree_files` does; and
    `follows` is None, so a case adding commits after the closing records
    owes no round at HEAD and no new seal. A name in REAL stays the
    reader's own. The other git a run starts, the top, the baseline, the
    diff, the merge base, the trailers, the tree the rule-changes arm reads
    and a fixed commit's ancestry, stays real, so `main` still reads the
    world the case built; the readers' agreement with git is held by their
    own cases (`Test_follows`, `Test_main`'s real-git runs)."""
    answers = {
        "read_record": on_disk,
        "tracked_files": chain.worktree_files,
        "follows": lambda *_args, **_kw: None,
    }
    for name, answer in answers.items():
        if name not in real:
            monkeypatch.setattr(chain, name, answer)


# --- what the pull request changed ----------------------------------------------


@pytest.fixture(scope="module")
def _two_declarations(tmp_path_factory):
    """`main` holds one declaration; `feature/y` checked out, nothing yet."""
    d = tmp_path_factory.mktemp("chain-two") / "c"
    init(d)
    old = ROUTING.format(review="straight to the PR", planning="the session")
    write(d, "seal/threads/1788000000-old/routing.md", old)
    commit(d, "base")
    git(d, "switch", "-q", "-c", "feature/y")
    return d, old


@pytest.fixture
def two_declarations(tmp_path, _two_declarations):
    template, old = _two_declarations
    d = tmp_path / "c"
    shutil.copytree(template, d)
    return d, old


class Test_changed:
    def test_accepts_a_move_committed_or_not_yet_committed_as_a_move(
        self, two_declarations, monkeypatch
    ):
        """A move of the whole root renames every declaration at once (#90),
        and under `--worktree` an untracked file's bytes are hashed to pair
        it."""
        d, _old = two_declarations
        moved = {
            "seal/threads/1788000000-old/routing.md",
            "seal/threads/1788000000-moved/routing.md",
        }
        os.rename(
            d / "seal/threads/1788000000-old", d / "seal/threads/1788000000-moved"
        )
        monkeypatch.setattr(chain, "WORKTREE", True)
        assert chain.changed(str(d), "main")[1] == moved
        monkeypatch.setattr(chain, "WORKTREE", False)
        commit(d, "moved")
        assert chain.changed(str(d), "main")[1] == moved

    def test_refuses_to_pair_a_deletion_with_a_similar_addition(self, two_declarations):
        """Two declarations from one template differ in a row or two, which
        git's rename detection pairs. The check reads declarations, not file
        identity, so the deletion is seen."""
        d, old = two_declarations
        git(d, "rm", "-q", "seal/threads/1788000000-old/routing.md")
        write(
            d,
            "seal/threads/1791999999-new/routing.md",
            old.replace("feature/x", "feature/y"),
        )
        commit(d, "one leaves, one arrives")
        paths, renamed = chain.changed(str(d), "main")
        assert renamed == set()
        assert sorted(paths) == [
            "seal/threads/1788000000-old/routing.md",
            "seal/threads/1791999999-new/routing.md",
        ]


class Test_changed_routing:
    def test_accepts_every_declaration_added_changed_or_deleted(self):
        paths = [
            "seal/threads/1/routing.md",
            "seal/threads/2/routing.md",
            "seal/threads/2/frame/design.md",
            "docs/routing.md",
        ]
        assert chain.changed_routing(paths, set(), "seal/threads") == [
            "seal/threads/1/routing.md",
            "seal/threads/2/routing.md",
        ]

    def test_refuses_a_declaration_the_pull_request_only_moved(self):
        moved = {"seal/threads/1/routing.md", "seal/threads/3/routing.md"}
        assert chain.changed_routing(sorted(moved), moved, "seal/threads") == []


# --- carried_by -------------------------------------------------------------------

RELEASE = "release/v9.9.9"
GITHUB = {"GIT_COMMITTER_NAME": "GitHub", "GIT_COMMITTER_EMAIL": "noreply@github.com"}


def squash(d, source, subject, committer=None):
    """Squash `source` onto the checked-out branch as GitHub's merge button
    does: one commit, committed by GitHub, its subject ending with the pull
    request's number. `committer` replaces GitHub's identity."""
    git(d, "merge", "--squash", "-q", source)
    subprocess.run(
        ["git", "-C", str(d), "commit", "-qm", subject],
        check=True,
        capture_output=True,
        env={**os.environ, **(committer or GITHUB)},
    )
    return git(d, "rev-parse", "HEAD")


def released(root, subject="feat: a work item (#7)", committer=None, keep=False):
    """`release/v9.9.9` cut from `main` with `feature/x` squashed into it and
    the feature branch deleted, so the item's records name commits HEAD does
    not descend from, as a release pull request into `main` carries."""
    git(root, "switch", "-q", "-c", RELEASE, "main")
    squash(root, "feature/x", subject, committer)
    if not keep:
        git(root, "branch", "-q", "-D", "feature/x")


@pytest.mark.rule("judged-where-carried")
class Test_carried_by:
    def test_accepts_a_declaration_only_a_squash_merge_touched(
        self, branch, monkeypatch
    ):
        root, _code = branch
        monkeypatch.setattr(chain, "WORKTREE", False)
        released(root)
        rel = f"{ITEM}/routing.md"
        sha, subject = chain.carried_by(str(root), "main", rel)
        assert sha == git(root, "rev-parse", "HEAD")
        assert subject == "feat: a work item (#7)"
        # Under `--worktree` an edit not yet committed is this branch's own.
        monkeypatch.setattr(chain, "WORKTREE", True)
        assert chain.carried_by(str(root), "main", rel) is not None
        write(root, rel, (root / rel).read_text(encoding="utf-8") + "\nA note.\n")
        assert chain.carried_by(str(root), "main", rel) is None

    def test_refuses_the_items_own_commits_a_persons_squash_and_an_unnumbered_one(
        self, branch, monkeypatch
    ):
        """The item's own branch, a squash a person committed, GitHub's commit
        whose subject does not end with a pull request number, and a path no
        commit touched each leave the declaration this pull request's."""
        root, _code = branch
        monkeypatch.setattr(chain, "WORKTREE", False)
        rel = f"{ITEM}/routing.md"
        assert chain.carried_by(str(root), "main", rel) is None
        released(root, committer={"GIT_COMMITTER_EMAIL": "t@t"}, keep=True)
        assert chain.carried_by(str(root), "main", rel) is None
        git(root, "reset", "-q", "--hard", "main")
        squash(root, "feature/x", "feat: a work item (#7), edited")
        assert chain.carried_by(str(root), "main", rel) is None
        assert (
            chain.carried_by(str(root), "main", "seal/threads/none/routing.md") is None
        )


# --- the round record's template and its loading ---------------------------------

DOC = ROOT / "docs" / "forms" / "the-round-record.md"
TEMPLATE = ROOT / "templates" / "records" / "sdd-round.md"


def copied_tree(tree):
    """The check and the files it loads at import, copied under TREE, as the
    path of the copied script."""
    script = tree / "skills" / "code-review" / "scripts" / "chain_check.py"
    script.parent.mkdir(parents=True)
    script.write_text(CHAIN.read_text(encoding="utf-8"), encoding="utf-8")
    (tree / "lib").mkdir(parents=True)
    for name in (
        "blocks.py",
        "closing.py",
        "console.py",
        "fields.py",
        "gitcmd.py",
        "lines.py",
        "optin.py",
        "sibling.py",
    ):
        (tree / "lib" / name).write_text(
            (ROOT / "lib" / name).read_text(encoding="utf-8"),
            encoding="utf-8",
        )
    return script


class Test_issue_of:
    def test_accepts_a_home_that_is_exactly_an_issue(self):
        assert chain.issue_of("#12") == 12

    def test_refuses_a_home_of_prose(self):
        assert chain.issue_of("to #664") is None
        assert chain.issue_of("#12.") is None
        assert chain.issue_of(None) is None


# --- a record ------------------------------------------------------------------------


def target_of(text):
    """`(the commit round_of reads off the record's round block, its
    errors)`."""
    read, errors = chain.round_of(text, "r.md", 1)
    return read.target, errors


# A round record in 0.26.0's shape, its fields on labelled lines: one a
# reader of the blocks meets in a work item open across the change.
LABELLED = (
    "# 1791999999-a-work-item — review round 1\n\n"
    "target: abc1234 against main\n\n"
    "## Findings\n\n"
    "### 1. the parser drops a row\n\n"
    "severity: must\nlocation: `f.txt:1`\nevidence: read `f.txt:1`\n"
    "verdict: rejected\n\nWhy it matters.\n\nanswer: it holds\n\n"
    "## Confirmations\n\nconfirms: none\nheld, at `f.txt:1`. read.\n"
)


class Test_round_of:
    def test_accepts_the_one_round_block_and_reads_its_commit(self):
        """S4: a record's reviewed commit is the `target:` line of its one
        round block, reading `<sha> against <base>` or, for a verifying
        round, `<sha>, fixes <a>..<b>`; the commit is the first word."""
        sha = "1a2b3c4d" * 5
        for value, read in (
            ("abc1234 against main", "abc1234"),
            (f"{sha} against origin/release/v0.22.0", sha),
            ("abc1234, fixes 1111111..abc1234", "abc1234"),
        ):
            text = record("x").replace("target: x against main", f"target: {value}")
            assert target_of(text) == (read, []), value

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_second_round_block_or_a_value_it_cannot_read(self):
        """S4: a second round block is refused at its opener, and a
        `target:` value outside the two shapes at its line, where no commit
        is read."""
        two = record("abc1234").replace(
            "\n## Findings",
            "\n" + block("target: abc1234 against main") + "\n## Findings",
        )
        assert target_of(two)[1] == [
            (
                "r.md",
                opener_at(two, "target: abc1234 against main", 1),
                chain.SECOND_ROUND,
            )
        ]
        assert "a round record holds one" in chain.SECOND_ROUND
        for value in (
            "abc1234",
            "ABC1234 against main",
            "abc1234 against main.",
            "abc1234, fixes 111..abc1234",
            "abc1234 against main · a verifying round",
            "abc1234 against main and more",
            "",
        ):
            text = record("x").replace("target: x against main", f"target: {value}")
            line = f"target: {value}"
            sha, errors = target_of(text)
            assert sha is None, value
            assert [(rel, n) for rel, n, _why in errors] == [
                ("r.md", line_at(text, line))
            ], value
            assert "`<sha> against <base>`" in errors[0][2], value

    @pytest.mark.rule("old-table-shape-refused")
    def test_refuses_a_record_from_before_the_blocks_with_one_message(self):
        """#1198's scenario *A record from before the change*: a round record
        in 0.26.0's labelled lines, and one in the table shape before them,
        hold no round block, so each is refused with the one message that
        names the template, and nothing else of it is read. Seen red against
        the 0.26.0 reader, which passes the labelled record."""
        table = LABELLED.replace(
            "target: abc1234 against main",
            "| Field | Value |\n|---|---|\n| Target SHA | abc1234 against main |",
        )
        for text in (LABELLED, table):
            read, errors = chain.round_of(text, "r.md", 1)
            assert errors == [("r.md", 0, chain.NO_ROUND_BLOCK)], errors
            assert (read.findings, read.confirms, read.target) == ([], [], None)
        for words in (
            "no round block",
            "`seal` blocks",
            "`templates/records/sdd-round.md`",
            "rewritten into blocks with its verdicts unchanged",
        ):
            assert words in chain.NO_ROUND_BLOCK, words

    def test_accepts_each_confirmation_block_as_a_reference(self):
        """S23: each entry is a confirmation block reading `round-<N>#<n>`,
        read with its line; a record with nothing to confirm may leave the
        section out."""
        text = record(
            "abc1234",
            confirmations=confirm("round-1#2") + confirm("round-3#1"),
            n=4,
        )
        read, errors = chain.round_of(text, "r.md", 4)
        assert errors == []
        assert read.confirms == [
            (line_at(text, "confirms: round-1#2"), (1, 2)),
            (line_at(text, "confirms: round-3#1"), (3, 1)),
        ]
        left_out = record("abc1234").replace("## Confirmations\n", "")
        read, errors = chain.round_of(left_out, "r.md", 1)
        assert (read.confirms, errors) == ([], [])

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_value_it_cannot_read_and_reads_prose_as_nothing(self):
        """S23 (T36): a `confirms:` value outside its shape is refused at its
        line; a table under the heading, and a `confirms:` line outside every
        block, are prose and confirm nothing."""
        bad = (
            "round 1's 3",
            "Round-1#3",
            "#3",
            "round-1",
            "none",
            "**none**",
            "None",
            "round-1#2 holds",
            "",
        )
        text = record(
            "abc1234",
            confirmations="".join(confirm(cell) for cell in bad),
            n=2,
        )
        read, errors = chain.round_of(text, "r.md", 2)
        assert read.confirms == []
        assert [line for _rel, line, _why in errors] == [
            line_at(text, f"confirms: {cell}") for cell in bad
        ], errors
        for (_rel, _line, why), cell in zip(errors, bad, strict=True):
            assert f"`confirms: {cell}`" in why, why
            assert "`round-<N>#<n>`, the earlier finding it confirms" in why, why
        prose = record(
            "abc1234",
            confirmations="| Confirms | What holds |\n|---|---|\n| round-1#2 | x |\n\n"
            "confirms: round-1#2\nheld.\n",
            n=2,
        )
        assert chain.round_of(prose, "r.md", 2)[0].confirms == []
        assert chain.round_of(prose, "r.md", 2)[1] == []


def led(text, n, why, title="the parser drops a row"):
    """WHY led by the heading of finding N of TEXT, as a refusal in a
    finding says it."""
    return f"### {n}. {title} {chain.DASH} {why}"


class Test_record_findings:
    def test_accepts_each_finding_by_its_blocks(self):
        """A finding's `### ` heading names it and its number; its finding
        block's `location:` names its paths and its `regression:`, where it
        stands, the earlier finding; its close block's `verdict:` decides it,
        a close block's `location:` adds the path a fix went to, and a
        finding with no close block is open. A severity, an answer and a
        confirmation decide nothing."""
        text = record(
            "abc1234",
            [
                finding(1, "open"),
                finding(2, "fixed abc1234", severity="should", regression="round-1#4"),
                finding(
                    3,
                    "deferred #12",
                    severity="should",
                    location="`a.py:3`, `docs/b.md`",
                    regression="round-1",
                ),
                finding(4, "open")
                + "\n"
                + close("fixed abc1234", location="`g.txt:2`"),
            ],
            confirmations=confirm("round-1#2"),
        )
        found, errors = chain.record_findings(text, "r.md")
        assert errors == []
        assert [
            (f.line, f.heading, f.number, f.verdict, f.paths, f.regression)
            for f in found
        ] == [
            (
                line_at(text, "### 1. the parser drops a row"),
                "### 1. the parser drops a row",
                1,
                (chain.OPEN, None),
                ["f.txt"],
                None,
            ),
            (
                line_at(text, "verdict: fixed abc1234"),
                "### 2. the parser drops a row",
                2,
                (chain.FIXED, "abc1234"),
                ["f.txt"],
                (1, 4),
            ),
            (
                line_at(text, "verdict: deferred #12"),
                "### 3. the parser drops a row",
                3,
                (chain.DEFERRED, "#12"),
                ["a.py", "docs/b.md"],
                (1, None),
            ),
            (
                line_at(text, "verdict: fixed abc1234", 1),
                "### 4. the parser drops a row",
                4,
                (chain.FIXED, "abc1234"),
                ["f.txt", "g.txt"],
                None,
            ),
        ]
        assert found[1].regression_line == line_at(text, "regression: round-1#4")
        assert chain.record_findings(record("abc1234"), "r.md") == ([], [])

    def test_located_holds_the_finding_blocks_paths_alone(self):
        """S7 of work item 1793521559. `located` is the paths of the finding
        block's own `location:`, in the order written, so a reader asking where
        the defect shows does not read where the fix went; `paths` still
        holds both blocks' paths, which the pull-request check reads. Seen red
        with `located` built from the union."""
        text = record(
            "abc1234",
            [
                finding(1, "open", location="`seal/threads/1-x/frame/design.md:3`")
                + "\n"
                + close("fixed abc1234", location="`seal/threads/1-x/frame/plan.md`")
            ],
        )
        found, errors = chain.record_findings(text, "r.md")
        assert errors == []
        assert [(f.located, f.paths) for f in found] == [
            (
                ["seal/threads/1-x/frame/design.md"],
                ["seal/threads/1-x/frame/design.md", "seal/threads/1-x/frame/plan.md"],
            )
        ]

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_finding_with_no_finding_block_or_a_block_twice(self):
        """A finding holds one finding block and one close block at most: a
        section with no finding block is refused at its heading, a second
        block of either kind at its opener, and the record's other findings
        still read."""
        sections = [
            "### 1. the parser drops a row\n\nWhy it matters.\n",
            finding(2, "rejected")
            + "\n"
            + block(
                "severity: should", "location: `g.txt`", "evidence: read `g.txt:1`"
            ),
            finding(3, "rejected") + "\n" + close("deferred #9"),
            finding(4, "rejected"),
        ]
        text = record("abc1234", sections)
        found, errors = chain.record_findings(text, "r.md")
        assert [f.number for f in found] == [4]
        assert errors == [
            (
                "r.md",
                line_at(text, "### 1. the parser drops a row"),
                led(text, 1, chain.NO_FINDING_BLOCK),
            ),
            (
                "r.md",
                opener_at(text, "severity: should"),
                led(text, 2, chain.SECOND_BLOCK.format(kind="finding")),
            ),
            (
                "r.md",
                opener_at(text, "verdict: deferred #9"),
                led(text, 3, chain.SECOND_BLOCK.format(kind="close")),
            ),
        ], errors
        for words in (
            "no finding block",
            "`severity:`",
            "`templates/records/sdd-round.md`",
        ):
            assert words in chain.NO_FINDING_BLOCK, words
        assert (
            chain.SECOND_BLOCK.format(kind="close")
        ) == "a second close block: a finding holds one"

    def test_refuses_a_record_with_no_findings_section_or_two(self):
        """The record holds one `## Findings` heading: none, a heading with a
        word after it among the ways to have none, is refused naming the
        section, where a finding block then stands outside every finding,
        and a second at its line."""
        assert chain.record_findings(
            block("target: abc1234 against main") + "\n## Probes\n", "r.md"
        ) == ([], [("r.md", 0, chain.NO_FINDINGS)])
        longer = record("abc1234", [finding(1, "open")]).replace(
            "## Findings", "## Findings so far"
        )
        assert chain.record_findings(longer, "r.md")[1] == [
            ("r.md", 0, chain.NO_FINDINGS),
            (
                "r.md",
                opener_at(longer, "severity: must"),
                chain.OUTSIDE.format(kind="finding"),
            ),
        ]
        two = record("abc1234") + "\n## Findings\n"
        assert chain.record_findings(two, "r.md") == (
            [],
            [("r.md", line_at(two, "## Findings", 1), chain.TWO_FINDINGS)],
        )

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_key_spelt_otherwise_at_its_line_and_reads_no_close(self):
        """#1198's scenario *A misspelt key inside a block*: a close block
        whose first line reads `Verdict: fixed abc1234` is refused at that
        line with the keys a block of the record opens with, one whose
        second line reads `Answer: done` at that line with the keys a close
        block takes, and nothing closes either finding. Seen red against a
        reader that skips the line."""
        text = record(
            "abc1234",
            [
                finding(1, "open")
                + "\n"
                + block("Verdict: fixed abc1234", "answer: done"),
                finding(2, "open")
                + "\n"
                + block("verdict: fixed abc1234", "Answer: done"),
            ],
        )
        found, errors = chain.record_findings(text, "r.md")
        assert found == []
        assert errors == [
            (
                "r.md",
                line_at(text, "Verdict: fixed abc1234"),
                led(
                    text,
                    1,
                    chain.FIELDS.NO_KIND.format(
                        line="Verdict: fixed abc1234",
                        openers="`target:`, `severity:`, `verdict:` or `confirms:`",
                    ),
                ),
            ),
            (
                "r.md",
                line_at(text, "Answer: done"),
                led(
                    text,
                    2,
                    chain.FIELDS.NOT_A_FIELD.format(
                        line="Answer: done",
                        kind="close",
                        keys="`verdict:`, `answer:` and `location:`",
                    ),
                ),
            ),
        ], errors

    def test_a_close_written_as_prose_leaves_the_finding_open(self):
        """#1198's scenario *A close written as prose*: `verdict:` and
        `answer:` lines outside every block under a finding are prose, so
        the finding has no close block and reads as open, which a ready pull
        request refuses at its heading, and no line names the prose. Seen
        red against the reader of labelled lines, which read the `verdict:`
        line as the finding's close."""
        text = record(
            "abc1234",
            [finding(1, "open") + "\nverdict: fixed abc1234\nanswer: done\n"],
        )
        found, errors = chain.record_findings(text, "r.md")
        assert errors == []
        assert [(f.number, f.verdict, f.line) for f in found] == [
            (1, (chain.OPEN, None), line_at(text, "### 1. the parser drops a row"))
        ]
        notices = []
        chain.blocks_of("r.md", text, chain.FIELDS.ROUND_RECORD, notices)
        assert notices == []

    def test_a_near_opener_is_no_block_and_is_named(self):
        """#1198's scenario *A near opener*: a finding block opened by three
        backticks and `Seal` is no block, so the finding is refused for
        lacking its finding block, and the opener is named at its line as
        not read."""
        near = FENCE + "Seal"
        text = record(
            "abc1234",
            [
                "### 1. the parser drops a row\n\n"
                + block("severity: must", "location: `f.txt:1`", opener=near)
            ],
        )
        found, errors = chain.record_findings(text, "r.md")
        assert (found, errors) == (
            [],
            [
                (
                    "r.md",
                    line_at(text, "### 1. the parser drops a row"),
                    led(text, 1, chain.NO_FINDING_BLOCK),
                )
            ],
        )
        notices = []
        chain.blocks_of("r.md", text, chain.FIELDS.ROUND_RECORD, notices)
        assert notices == [
            ("r.md", line_at(text, near), chain.FIELDS.NEAR.format(line=near))
        ]

    def test_a_block_inside_the_fix_fence_is_no_finding_block(self):
        """#1198's scenario *A block inside the fix fence*: a finding block
        written inside a four-backtick fence belongs to that fence, so the
        finding is refused for lacking its finding block."""
        heading = "### 1. the parser drops a row"
        quoted = block(
            "severity: must", "location: `f.txt:1`", "evidence: read `f.txt:1`"
        )
        text = record(
            "abc1234",
            [f"{heading}\n\n{FENCE}`markdown\n{quoted}{FENCE}`\n"],
        )
        assert chain.record_findings(text, "r.md") == (
            [],
            [("r.md", line_at(text, heading), led(text, 1, chain.NO_FINDING_BLOCK))],
        )

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_block_that_never_closes_at_its_opener(self):
        """#1198's scenario *A block that never closes*: a `seal` block with
        no closing fence is refused at its opener, every line after it is
        hidden and no field, and what the reader saw before it is read."""
        text = record(
            "abc1234",
            [
                finding(1, "rejected"),
                "### 2. the parser drops a row\n\n" + FENCE + "seal\nseverity: must\n",
            ],
        )
        opener = line_at(text, FENCE + "seal", 3)
        found, errors = chain.record_findings(text, "r.md")
        assert errors == [("r.md", opener, chain.FIELDS.UNCLOSED)], errors
        assert [f.number for f in found] == [1]

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_block_out_of_its_place(self):
        """A round or confirmation block inside a finding, and a finding or
        close block outside every finding, are refused at their opener, and
        a finding holding a block out of its place is not read."""
        stray = block(
            "severity: should", "location: `g.txt`", "evidence: read `g.txt:1`"
        )
        text = record(
            "abc1234",
            [
                finding(1, "rejected")
                + "\n"
                + block("target: abc1234 against main")
                + "\n"
                + block("confirms: round-1#1"),
                finding(2, "rejected"),
            ],
        ).replace(
            "## Not judged\n", "## Not judged\n\n" + stray + "\n" + close("rejected")
        )
        found, errors = chain.record_findings(text, "r.md")
        assert [f.number for f in found] == [2]
        assert errors == [
            (
                "r.md",
                opener_at(text, "target: abc1234 against main", 1),
                led(text, 1, chain.INSIDE.format(kind="round")),
            ),
            (
                "r.md",
                opener_at(text, "confirms: round-1#1"),
                led(text, 1, chain.INSIDE.format(kind="confirmation")),
            ),
            (
                "r.md",
                opener_at(text, "severity: should"),
                chain.OUTSIDE.format(kind="finding"),
            ),
            (
                "r.md",
                opener_at(text, "verdict: rejected", 2),
                chain.OUTSIDE.format(kind="close"),
            ),
        ], errors
        # The refusal `chain_check.py` prints for a block out of its place,
        # which the proofer or the orchestrator reads to move the block.
        assert "stands outside every finding" in chain.INSIDE.format(kind="round")
        assert "`### <n>. <symptom>`" in chain.OUTSIDE.format(kind="close")

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_reopens_line_beside_a_regression_or_naming_no_finding(self):
        """S23, S24 (T42): a `reopens:` line names an earlier finding as
        `round-<N>#<n>` and is read with its line. `reopens: round-1` is
        refused at its line, and so is a finding block holding a `reopens:`
        and a `regression:` line, at the later of the two, each refusal led
        by the finding's heading."""
        text = record(
            "abc1234",
            [
                finding(1, "open", reopens="round-1#2"),
                finding(2, "open", reopens="round-1"),
                finding(3, "open", regression="round-1#2", reopens="round-1#3"),
                finding(4, "open"),
            ],
            n=2,
        )
        found, errors = chain.record_findings(text, "r.md")
        assert [(f.number, f.reopens, f.regression) for f in found] == [
            (1, (1, 2), None),
            (4, None, None),
        ], errors
        assert found[0].reopens_line == line_at(text, "reopens: round-1#2")
        assert found[1].reopens_line is None
        shape = chain.FIELDS.FINDING_BLOCK.keys[chain.FIELDS.REOPENS].says
        assert errors == [
            (
                "r.md",
                line_at(text, "reopens: round-1"),
                led(
                    text,
                    2,
                    chain.FIELDS.SHAPE.format(
                        line="reopens: round-1", key="reopens:", says=shape
                    ),
                ),
            ),
            (
                "r.md",
                line_at(text, "reopens: round-1#3"),
                led(
                    text,
                    3,
                    chain.FIELDS.ONE_OF.format(
                        key="reopens:", other="regression:", kind="finding"
                    ),
                ),
            ),
        ], errors
        assert "`round-<N>#<n>`" in shape

    def test_reads_the_lines_only_agents_read_whatever_they_say(self):
        """#1319: no script decides on a finding's `severity:` or `evidence:`
        value or a close's `answer:`, so a finding block with any severity
        word, one with no `evidence:` line or with one in any words, and a
        close block with no `answer:` line all read, and the agents judge
        what each says. Seen red against the shape `must` or `should`, the
        evidence shape and the one `evidence:` and `answer:` line each block
        held before."""
        text = record(
            "abc1234",
            [
                finding(1, "rejected", severity="anything at all"),
                finding(2, "open", evidence=None) + "\n" + block("verdict: rejected"),
                finding(3, "rejected", evidence="ran the case twice, both red"),
            ],
        )
        found, errors = chain.record_findings(text, "r.md")
        assert errors == []
        assert [(f.number, f.verdict) for f in found] == [
            (n, (chain.REJECTED, None)) for n in range(1, 4)
        ]

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_heading_with_no_number_or_a_number_twice(self):
        """A finding is named across rounds by its heading's number, so a
        heading with none, or a number a second heading also carries, is
        refused at the heading, and the record's other findings still read."""
        text = record(
            "abc1234",
            [
                finding(1, "fixed abc1234"),
                finding(1, "fixed abc1234", title="a second one"),
                finding(2, "deferred #9").replace("### 2. ", "### "),
                finding(3, "open"),
            ],
        )
        found, errors = chain.record_findings(text, "r.md")
        assert [f.number for f in found] == [1, 3]
        assert [(line, why.split(" — ")[0]) for _r, line, why in errors] == [
            (line_at(text, "### 1. a second one"), "### 1. a second one"),
            (
                line_at(text, "### the parser drops a row"),
                "### the parser drops a row",
            ),
        ]
        assert "a second finding numbered 1" in errors[0][2]
        assert "no number" in errors[1][2]

    def test_accepts_a_record_whose_regions_close(self):
        text = record("abc1234", [finding(1, "open"), finding(2, "rejected")])
        found, errors = chain.record_findings(text, "r.md")
        assert errors == [] and [f.number for f in found] == [1, 2], errors
        quoted = record(
            "abc1234",
            [
                finding(1, "rejected").replace(
                    "answer: done", "answer: the `<!--` opener is quoted"
                ),
                finding(2, "open"),
            ],
        )
        found, errors = chain.record_findings(quoted, "r.md")
        assert errors == [] and [f.number for f in found] == [1, 2], errors

    def test_accepts_a_bare_opener_later_in_a_line_as_text(self):
        """S4 of #1012: a `<!--` nothing closes, after the start of a line of
        a finding's prose, is text, so every finding after it is read. The
        reader that kept a comment state refused it as a comment that never
        closes."""
        text = record(
            "abc1234",
            [
                finding(1, "rejected").replace(
                    "Why it matters.", "Why it matters: a bare <!-- opens nothing"
                ),
                finding(2, "open"),
            ],
        )
        found, errors = chain.record_findings(text, "r.md")
        assert errors == [] and [f.number for f in found] == [1, 2], errors

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_fence_that_never_closes_at_its_opener(self):
        """A fence that never closes hides every line after it, so the record
        is refused at the opener's line, and what the reader could still see
        is read as well."""
        opener = "~~~python"
        text = record(
            "abc1234",
            [finding(1, "rejected") + f"\n{opener}\n", finding(2, "open")],
        )
        found, errors = chain.record_findings(text, "r.md")
        line = text.splitlines().index(opener) + 1
        assert [(rel, n) for rel, n, _why in errors] == [("r.md", line)], errors
        assert "fence" in errors[0][2] and "never closes" in errors[0][2]
        assert [f.heading for f in found] == ["### 1. the parser drops a row"]

    @pytest.mark.rule("record-comment-line-refused")
    def test_refuses_a_comment_line_at_its_line(self):
        """S3 of #1012: a record line that begins with `<!--` is refused at
        that line, and every finding is still read, since the check reads the
        comment as text. The reader that kept a comment state read past it."""
        note = "<!-- a note -->"
        text = record(
            "abc1234",
            [finding(1, "rejected"), f"{note}\n\n" + finding(2, "open")],
        )
        found, errors = chain.record_findings(text, "r.md")
        line = text.splitlines().index(note) + 1
        assert errors == [("r.md", line, chain.FIELDS.COMMENT_LINE)], errors
        assert [f.number for f in found] == [1, 2]

    @pytest.mark.rule("location-touched-by-fix")
    def test_accepts_one_or_more_backticked_coordinates(self):
        """S22 (T33): the paths of a `location:` value the block's shape
        matched, each backticked `path`, `path:line` or `path:first-last`
        item to its first `:`; the shape's refusals are
        `tests/lib/test_fields.py`'s. `chain_check.location_paths` is the
        step of `finding_of` that gives a finding its paths, and has no
        refusal of its own, since the value it takes is one
        `lib/fields.py` already matched whole."""
        for value, paths in (
            ("`a.py`", ["a.py"]),
            ("`a.py:12`", ["a.py"]),
            ("`a.py:12-14`", ["a.py"]),
            ("`docs/x/`", ["docs/x/"]),
            ("`a.py:1`, `docs/b.md:3-4`", ["a.py", "docs/b.md"]),
            ("`a.py:1`, `b.py`, `c/d.md:9`", ["a.py", "b.py", "c/d.md"]),
        ):
            assert chain.location_paths(value) == paths, value


class Test_channel:
    def test_accepts_every_fixed_or_rejected_finding_the_next_record_names(self):
        """S23 (T36, T43): a `confirms:`, a `regression:` or a `reopens:`
        line in round N+1 answers a finding of round N at `fixed <commit>` or
        `rejected`; a `deferred` one owes nothing."""
        one = record(
            "abc1234",
            [
                finding(1, "fixed abc1234"),
                finding(2, "rejected"),
                finding(3, "deferred #9"),
                finding(4, "fixed abc1234", title="the fourth"),
            ],
        )
        two = record(
            "abc1234",
            [
                finding(1, "deferred the frame", regression="round-1#2"),
                finding(2, "open", reopens="round-1#4"),
            ],
            confirmations=confirm("round-1#1"),
            n=2,
        )
        rounds, errors = rounds_of(one, two)
        assert errors == []
        assert chain.channel(rounds) == []
        deferred = record("abc1234", [finding(1, "deferred #9")])
        assert chain.channel(rounds_of(deferred, record("abc1234", n=2))[0]) == []

    def test_refuses_a_fixed_or_rejected_finding_no_line_names(self):
        """One left unnamed is refused at its own heading, in round N's
        record, and the refusal names all three labels; a `regression:`
        line naming the round alone covers no finding."""
        one = record(
            "abc1234",
            [
                finding(1, "fixed abc1234"),
                finding(4, "fixed abc1234", title="the fourth"),
                finding(5, "rejected", title="the fifth"),
            ],
        )
        two = record(
            "abc1234",
            [finding(1, "deferred the frame", regression="round-1")],
            confirmations=confirm("round-1#1"),
            n=2,
        )
        rounds, errors = rounds_of(one, two)
        assert errors == []
        problems = chain.channel(rounds)
        lines = reader.readable(one)
        assert [(rel, line) for rel, line, _why in problems] == [
            ("round-1.md", lines.index("### 4. the fourth") + 1),
            ("round-1.md", lines.index("### 5. the fifth") + 1),
        ], problems
        said = [why for _rel, _line, why in problems]
        assert "`round-1#4`" in said[0] and "### 4. the fourth" in said[0]
        assert "`round-1#5`" in said[1] and "### 5. the fifth" in said[1]
        for why in said:
            assert "round-2.md" in why and "names it on no" in why, why
            for label in ("`confirms:`", "`reopens:`", "`regression:`"):
                assert label in why, why

    def test_an_old_spelling_is_prose_and_names_no_finding(self):
        """The fourth scenario of #1167: `refixes:`, a spelling round records
        carried before 0.22.x renamed the label, is prose outside every
        block. Round 2 carrying `refixes: round-1#2` and nothing else naming
        round 1's finding 2 reads whole, and `channel` refuses that finding
        as unnamed by the next record, and no notice names the line."""
        one = record(
            "abc1234",
            [finding(1, "rejected"), finding(2, "fixed abc1234", title="the second")],
        )
        refixes = finding(1, "deferred #9") + "\nrefixes: round-1#2\n"
        two = record("abc1234", [refixes], confirmations=confirm("round-1#1"), n=2)
        rounds, errors = rounds_of(one, two)
        assert errors == []
        [(rel, line, why)] = chain.channel(rounds)
        assert (rel, line) == ("round-1.md", line_at(one, "### 2. the second"))
        assert "`round-1#2`" in why and "names it on no" in why, why
        assert chain.FIELDS.read(two, chain.FIELDS.ROUND_RECORD).notices == []

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_reference_naming_no_earlier_record_or_finding(self):
        """S23 (T36, T43): a reference in the first record, to a record the
        item has not got or no earlier one, or to a finding that record does
        not hold, is refused by its line, and the refusal in the first record
        says the first record holds no reference line and that what it
        confirms is prose; a first record that names nothing passes."""
        one = record(
            "abc1234",
            [finding(1, "deferred #9", regression="round-1#1", reopens=None)],
            confirmations=confirm("round-1#1"),
        )
        two = record(
            "abc1234",
            [
                finding(1, "deferred #9", regression="round-3#1"),
                finding(2, "deferred #9", regression="round-2"),
                finding(3, "deferred #9", reopens="round-1#7"),
            ],
            confirmations=confirm("round-1#7") + confirm("round-1#1"),
            n=2,
        )
        rounds, errors = rounds_of(one, two)
        assert errors == []
        problems = chain.channel(rounds)
        assert [(rel, line) for rel, line, _why in problems] == [
            ("round-1.md", line_at(one, "regression: round-1#1")),
            ("round-1.md", line_at(one, "confirms: round-1#1")),
            ("round-2.md", line_at(two, "regression: round-3#1")),
            ("round-2.md", line_at(two, "regression: round-2")),
            ("round-2.md", line_at(two, "reopens: round-1#7")),
            ("round-2.md", line_at(two, "confirms: round-1#7")),
        ], problems
        said = [why for _rel, _line, why in problems]
        assert all("the first record" in why for why in said[:2]), said
        assert all(
            "so it holds no `confirms:`, `reopens:` or `regression:` line" in why
            for why in said[:2]
        ), said
        assert "`round-3#1`" in said[2] and "not an earlier record" in said[2]
        assert "`round-2`" in said[3] and "not an earlier record" in said[3]
        assert "`round-1#7`" in said[4] and "holds no finding 7" in said[4]
        assert "`round-1#7`" in said[5] and "holds no finding 7" in said[5]
        quiet = rounds_of(record("abc1234"))[0]
        assert chain.channel(quiet) == []

    @pytest.mark.rule("run-ends-with-verifying-round")
    def test_refuses_the_last_records_fixed_or_rejected_finding(self):
        """S23 (T37): nothing after the last record has read its fixes or its
        answers, so each such finding is named; its `deferred` and `open`
        findings, and none, are not."""
        last = record(
            "abc1234",
            [
                finding(1, "fixed abc1234"),
                finding(2, "rejected"),
                finding(3, "deferred #9"),
                finding(4, "open"),
            ],
        )
        problems = chain.channel(rounds_of(last)[0])
        assert [(rel, line) for rel, line, _why in problems] == [
            ("round-1.md", line_at(last, "verdict: fixed abc1234")),
            ("round-1.md", line_at(last, "verdict: rejected")),
        ], problems
        assert all(chain.VERIFYING_ROUND in why for _r, _l, why in problems)
        assert "### 1." in problems[0][2] and "### 2." in problems[1][2]
        assert chain.channel(rounds_of(record("abc1234"))[0]) == []


# --- the repository ---------------------------------------------------------------


@pytest.mark.rule("run-ends-with-verifying-round")
@pytest.mark.rule("last-record-at-head")
class Test_follows:
    def test_accepts_head_and_record_commits_after_it(self, _branch_template):
        root, code = _branch_template
        assert chain.follows(str(root), code, "main", ITEM) is None

    def test_refuses_a_code_commit_after_it_and_an_unseen_commit(self, branch):
        root, code = branch
        write(root, "f.txt", "three\n")
        later = commit(root, "a fix nobody reviewed")
        found = chain.follows(str(root), code, "main", ITEM)
        assert found == ("after", later, "f.txt")
        assert chain.follows(str(root), "0" * 40, "main", ITEM)[0] == "unseen"

    def test_refuses_another_items_records_and_a_commit_off_the_branch(self, branch):
        root, code = branch
        write(root, "seal/threads/1791999998-another-item/routing.md", "x\n")
        later = commit(root, "another work item's file")
        assert chain.follows(str(root), code, "main", ITEM)[:2] == ("after", later)
        git(root, "switch", "-q", "main")
        write(root, "g.txt", "elsewhere\n")
        off = commit(root, "a commit the branch never had")
        git(root, "switch", "-q", "feature/x")
        assert chain.follows(str(root), off, "main", ITEM)[0] == "off"


FRAMED = {"planning": "framer", "review": "through the review chain"}


class Test_frame:
    def routing(self):
        return load(ROOT / "lib" / "routing.py", "routing_for_chain_tests")

    def test_accepts_a_framed_item_with_a_reframe_by_the_framer(
        self, _branch_template, monkeypatch
    ):
        root, _code = _branch_template
        reading(
            monkeypatch,
            {
                f"{ITEM}/frame/design.md": SPEC
                + "Reframed 2026-10-16 by framer, after round 2.\n",
                f"{ITEM}/frame/plan.md": "# plan\n",
            },
        )
        assert chain.frame(self.routing(), str(root), ITEM, FRAMED) == []

    def test_refuses_a_missing_plan_and_a_reframe_by_another_party(
        self, _branch_template, monkeypatch
    ):
        root, _code = _branch_template
        reading(
            monkeypatch,
            {
                f"{ITEM}/frame/design.md": SPEC
                + "Reframed 2026-10-16 by the session, after round 2.\n"
            },
        )
        problems = chain.frame(self.routing(), str(root), ITEM, FRAMED)
        assert any("plan.md" in p for p in problems)
        assert any("Reframed 2026-10-16 by the session" in p for p in problems)

    def test_reads_who_alone_of_the_mark_and_each_reframe(
        self, _branch_template, monkeypatch
    ):
        """#1319: the arm compares who drew the frame with `Planning`, and
        reads neither the date nor the round number, so a date or a round
        left as the template's placeholder passes, and the template's
        unfilled who is refused as a who other than `framer`. Seen red
        against the placeholder checks and the digits the round took."""
        root, _code = _branch_template
        for foot, said in (
            (
                "Framed <date> by framer, before the build.\n"
                "Reframed <date> by framer, after round <N>.\n",
                [],
            ),
            (
                "Framed <date> by <who>, before the build.\n",
                [
                    f"{ITEM}/routing.md says `Planning | framer` and "
                    f"{ITEM}/frame/design.md's mark says `<who>`"
                ],
            ),
        ):
            design = "# spec\n\nbody\n\n" + foot
            plan = "# plan\n"
            reading(
                monkeypatch,
                {f"{ITEM}/frame/design.md": design, f"{ITEM}/frame/plan.md": plan},
            )
            problems = chain.frame(self.routing(), str(root), ITEM, FRAMED)
            assert problems == said, foot


# --- rule_changes_read, at the pull request --------------------------------------

RULES = chain.rule_changes_reader()
# The refusal's text before the parser's reason, pinned here so an edit to
# `chain.RULE_CHANGES_SAYS` meets a case.
SAYS = (
    "`## Rule changes` does not parse, so `settle` cannot group this design by the "
    "sections it names and the settle has to read it whole: "
)
CONTINUED = "- nothing\n  why: a reason\n  that continues two spaces in\n"
PROSE = "- add\n  file: docs/policy.md\n  to: A rule.\n\nA paragraph under the item.\n"
NOTHING = "- nothing\n  why: a reason\n"
CHANGE = (
    "- change\n  file: docs/policy.md\n  section: A section\n"
    "  from: old words.\n  to: new words.\n"
)


def spec_with(section):
    """A spec whose `## Rule changes` holds SECTION, or that has no such
    section where SECTION is None, ending with the framer's mark."""
    rules = "" if section is None else f"## Rule changes\n\n{section}\n"
    return f"# spec\n\nbody\n\n{rules}## Removes\n\nnone\n\n" + SPEC.split("\n\n")[-1]


def put_spec(root, text):
    """Write the work item's `frame/design.md` and commit it with whatever
    else the case wrote beside it."""
    write(root, f"{ITEM}/frame/design.md", text)
    commit(root, "the spec")


def refused(root, text, item=ITEM):
    """The `(path, line, problem)` the arm gives for ITEM's spec reading
    TEXT, built from `rule_changes.parse`'s own error so no reason is spelt
    here."""
    ((line, reason),) = RULES.parse(text, chain.policy_root(str(root))).errors
    return (
        f"{item}/frame/design.md",
        line,
        chain.RULE_CHANGES_SAYS.format(reason=reason),
    )


def refusal(root, text, item=ITEM):
    """The line the check prints outside CI for that refusal."""
    return "{}:{}  {}".format(*refused(root, text, item))


def heading_unread(root, text, item=ITEM):
    """The `(path, line, notice)` the arm gives for ITEM's spec reading TEXT,
    whose one near heading `rule_changes.parse` names, built from the
    parser's own reason."""
    ((line, why),) = RULES.parse(text, chain.policy_root(str(root))).unread
    return (f"{item}/frame/design.md", line, chain.RULE_CHANGES_UNREAD.format(why=why))


def unread_heading(root, text, item=ITEM):
    """The notice the check prints outside CI for that heading."""
    return "{}:{}  {}".format(*heading_unread(root, text, item))


def read_spec(monkeypatch, root, text, item=ITEM):
    """`(found, notices)`: what `rule_changes_read` gives for ITEM's design
    reading TEXT, handed to it through `read_record` (`reading`), its check
    lines resolved in the tree at ROOT."""
    reading(monkeypatch, {f"{item}/frame/design.md": text})
    notices = []
    return chain.rule_changes_read(str(root), item, notices), notices


# A spec whose section is under a heading near `## Rule changes`, and no other.
NEAR_HEADING = "## Rule Changes"


def spec_lines(out, item=ITEM):
    return [ln for ln in out.splitlines() if f"{item}/frame/design.md" in ln]


def reviewed_to_head(root):
    """A round 3 at HEAD, with nothing of its own, and the closing records
    after it, so the spec read is the one refusal left."""
    head = git(root, "rev-parse", "HEAD")
    write(root, f"{ITEM}/trail/rounds/round-3.md", record(head, n=3))
    commit(root, "the round at HEAD")
    seal(root)


def on_main(root, rel, text):
    """Commit TEXT at REL on `main` and merge `main` into `feature/x`."""
    git(root, "switch", "-q", "main")
    write(root, rel, text)
    commit(root, f"{rel} on the base")
    git(root, "switch", "-q", "feature/x")
    git(root, "merge", "-q", "--no-edit", "main")


def will_not_load():
    raise ImportError("a planted failure")


@pytest.mark.rule("rule-changes-read-at-the-pull-request")
class Test_rule_changes_read:
    @pytest.mark.parametrize(
        "section",
        [
            lambda: CONTINUED,
            lambda: PROSE,
            # What `templates/records/sdd-design.md` holds under its
            # `## Rule changes`, which a framer's skeleton commit carries.
            lambda: conftest.section(
                conftest.read("templates", "records", "sdd-design.md"),
                "## Rule changes",
            ),
        ],
        ids=["S1-continued-two-in", "S2-prose-under-items", "S3-the-template-section"],
    )
    def test_refuses_a_section_the_parser_refuses_at_its_line(
        self, _branch_template, monkeypatch, section
    ):
        """S1, S2, S3: the one refusal names the spec, the line the parser
        names and the parser's reason; S3's section is the template's, empty."""
        root, _code = _branch_template
        text = spec_with(section())
        found, notices = read_spec(monkeypatch, root, text)
        assert found == [refused(root, text)], found
        assert SAYS in found[0][2] and notices == []

    @pytest.mark.parametrize(
        "section", [NOTHING, CHANGE, None], ids=["no-change", "a-change", "none"]
    )
    def test_accepts_a_section_that_parses_or_no_section(
        self, _branch_template, monkeypatch, section
    ):
        root, _code = _branch_template
        assert read_spec(monkeypatch, root, spec_with(section)) == ([], [])

    def test_names_a_near_heading_as_not_read_and_passes(
        self, _branch_template, monkeypatch
    ):
        """#1167, *Scope* item 7: a spec whose section stands under
        `## Rule Changes` has no `## Rule changes` section, so it passes as a
        spec with none does, and the heading is named `not read:` at its
        line. Seen red against the refusal at the heading, exit 1."""
        root, _code = _branch_template
        text = spec_with(NOTHING).replace("## Rule changes", NEAR_HEADING)
        found, notices = read_spec(monkeypatch, root, text)
        assert (found, notices) == ([], [heading_unread(root, text)])

    def test_names_a_near_heading_beside_a_refusal_and_keeps_the_refusal(
        self, _branch_template, monkeypatch
    ):
        """The naming decides nothing: beside a `## Rule changes` section the
        parser refuses, the refusal stands and the near heading is named as
        not read beside it."""
        root, _code = _branch_template
        text = spec_with(CONTINUED).replace(
            "## Removes", f"{NEAR_HEADING}\n\n{NOTHING}\n## Removes"
        )
        found, notices = read_spec(monkeypatch, root, text)
        assert (found, notices) == ([refused(root, text)], [heading_unread(root, text)])

    def test_names_a_near_heading_in_another_work_items_spec_the_branch_edits(
        self, branch, ready, capsys, monkeypatch
    ):
        """The heading is named in every spec the arm reads, an edited spec of
        another work item among them, and the check passes."""
        root, _code = branch
        text = spec_with(NOTHING).replace("## Rule changes", NEAR_HEADING)
        write(root, f"{MERGED_ITEM}/frame/design.md", text)
        commit(root, "another work item's spec under a near heading")
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 0, out
        assert spec_lines(out, MERGED_ITEM) == [
            unread_heading(root, text, MERGED_ITEM)
        ], out

    def test_accepts_a_draft_or_an_unseen_pull_request_with_a_notice(
        self, branch, draft, capsys, monkeypatch
    ):
        """S5: in CI a draft annotates the same line as a notice and passes.
        S6: where no pull request is observed the check prints it and exits
        0, and `--sealing` leaves it a refusal on a ready one."""
        root, _code = branch
        text = spec_with(CONTINUED)
        put_spec(root, text)
        answered(monkeypatch)
        monkeypatch.setenv("GITHUB_ACTIONS", "true")
        code, out = check(root, capsys)
        assert code == 0, out
        where, said = refusal(root, text).split("  ", 1)
        path, line = where.rsplit(":", 1)
        assert f"::notice file={path},line={line}::{said}" in out.splitlines(), out
        monkeypatch.delenv("GITHUB_ACTIONS")
        draft.write_text(json.dumps({"pull_request": {"draft": False}}), "utf-8")
        code, out = check(root, capsys, chain.SEALING)
        assert code == 1, out
        assert spec_lines(out) == [refusal(root, text)], out
        monkeypatch.delenv("GITHUB_EVENT_PATH")
        code, out = check(root, capsys, chain.SEALING)
        assert code == 0, out
        assert chain.UNSEEN_SAYS in out
        assert spec_lines(out) == [refusal(root, text)], out

    def test_refuses_the_spec_of_a_framer_drawn_frame_the_same_way(
        self, branch, ready, capsys, monkeypatch
    ):
        """S7: under `Planning | framer`, with the frame arm satisfied, the
        spec is refused as under `Planning | the session`."""
        root, _code = branch
        write(
            root,
            f"{ITEM}/routing.md",
            ROUTING.format(review="through the review chain", planning="framer"),
        )
        write(root, f"{ITEM}/frame/plan.md", "# plan\n")
        text = spec_with(CONTINUED)
        put_spec(root, text)
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 1, out
        assert spec_lines(out) == [refusal(root, text)], out

    @pytest.mark.rule("judged-where-carried")
    def test_accepts_a_spec_another_pull_requests_squash_carried_unread(
        self, branch, ready, capsys, monkeypatch
    ):
        """S8: the release pull request leaves the work item to the pull
        request that carried it, its spec with it, also where the release
        declares a work item of its own; the head branch's own pull request
        reads the same spec."""
        root, _code = branch
        write(root, f"{MERGED_ITEM}/frame/design.md", spec_with(CONTINUED))
        put_spec(root, spec_with(CONTINUED))
        answered(monkeypatch)
        released(root)
        monkeypatch.setenv("GITHUB_HEAD_REF", RELEASE)
        code, out = check(root, capsys)
        assert code == 0, out
        assert spec_lines(out) == [] and spec_lines(out, MERGED_ITEM) == [], out
        own = "seal/threads/1792000000-the-release"
        write(
            root,
            f"{own}/routing.md",
            ROUTING.format(review="straight to the PR", planning="the session").replace(
                "feature/x", RELEASE
            ),
        )
        commit(root, "the release's own work item")
        code, out = check(root, capsys)
        assert code == 1 and f"{own}/trail/gate.md" in out, out
        assert spec_lines(out, MERGED_ITEM) == [], out
        git(root, "switch", "-q", "-c", "feature/x", RELEASE)
        monkeypatch.setenv("GITHUB_HEAD_REF", "feature/x")
        _code, out = check(root, capsys)
        assert len(spec_lines(out)) == 1, out

    def test_refuses_the_working_tree_under_worktree_and_reads_head_otherwise(
        self, branch, monkeypatch
    ):
        """S9: a spec written and not committed is refused where `WORKTREE`
        is set, as `--worktree` sets it; CI reads HEAD, which does not carry
        it, through git."""
        root, _code = branch
        text = spec_with(CONTINUED)
        write(root, f"{ITEM}/frame/design.md", text)
        monkeypatch.setattr(chain, "WORKTREE", True)
        assert chain.rule_changes_read(str(root), ITEM) == [refused(root, text)]
        monkeypatch.setattr(chain, "WORKTREE", False)
        assert chain.rule_changes_read(str(root), ITEM) == []

    def test_refuses_to_run_where_its_reader_will_not_load(
        self, branch, ready, capsys, monkeypatch
    ):
        """S10: exit 2 naming the reader, for an edited spec and for the
        judged item's spec; a work item with no `frame/design.md` never
        reaches it. The edited spec is committed, since `main` reads the
        diff for it; the judged item's is handed over (`reading`)."""
        root, _code = branch
        monkeypatch.setattr(chain, "rule_changes_reader", will_not_load)
        assert chain.rule_changes_of(str(root), [ITEM]) == []
        write(root, f"{MERGED_ITEM}/frame/design.md", spec_with(NOTHING))
        commit(root, "another work item's spec")
        answered(monkeypatch)
        code = chain.main(["--baseline", "main", "--root", str(root)])
        err = capsys.readouterr().err
        assert code == 2, err
        assert "the rule-changes reader would not load (a planted failure)" in err
        reading(monkeypatch, {f"{ITEM}/frame/design.md": spec_with(NOTHING)})
        code = chain.main(["--baseline", "main", "--root", str(root)])
        err = capsys.readouterr().err
        assert code == 2, err
        assert (
            "chain-check: the rule-changes reader would not load (a planted failure)"
            in err
        )

    def test_refuses_another_work_items_spec_the_branch_adds_or_changes(
        self, branch, ready, capsys
    ):
        """S12, S13: a declared work item's commit adds a spec to another
        work item, as #941's squash did to 114 of them, or edits one that
        parsed on the base into a section the reader refuses."""
        root, _code = branch
        rel = f"{MERGED_ITEM}/frame/design.md"
        on_main(root, rel, spec_with(NOTHING))
        text = spec_with(CONTINUED)
        write(root, rel, text)
        commit(root, "another work item's section, edited")
        reviewed_to_head(root)
        code, out = check(root, capsys)
        assert code == 1, out
        assert spec_lines(out, MERGED_ITEM) == [refusal(root, text, MERGED_ITEM)], out

    @pytest.mark.rule("two-review-answers")
    def test_refuses_another_work_items_spec_straight_to_the_pr(
        self, branch, ready, capsys, monkeypatch
    ):
        """S14: under `straight to the PR` no round is owed, and the spec is
        still read."""
        root, _code = branch
        write(
            root,
            f"{ITEM}/routing.md",
            ROUTING.format(review="straight to the PR", planning="the session"),
        )
        git(root, "rm", "-rq", f"{ITEM}/trail/rounds")
        text = spec_with(CONTINUED)
        write(root, f"{MERGED_ITEM}/frame/design.md", text)
        commit(root, "direct, and another work item's spec")
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 1, out
        assert spec_lines(out, MERGED_ITEM) == [refusal(root, text, MERGED_ITEM)], out

    def test_accepts_a_pull_request_that_declares_nothing_reading_no_spec(
        self, branch, ready, capsys, monkeypatch
    ):
        """S15: the promise in `hygiene.yml` and `CONTRIBUTING.md` holds."""
        root, _code = branch
        git(root, "rm", "-rq", ITEM)
        write(root, f"{MERGED_ITEM}/frame/design.md", spec_with(CONTINUED))
        commit(root, "no work item, and a spec")
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 0, out
        assert "declared neither way" in out
        assert spec_lines(out, MERGED_ITEM) == [], out

    def test_accepts_a_spec_only_moved_and_a_file_beside_or_below_one(
        self, monkeypatch
    ):
        """S16: a move with the bytes unchanged writes no section; another
        file beside a spec the branch leaves alone, and a `frame/design.md` one
        directory down, write none either. The diff is handed over as
        `changed` gives it, the move's two names in its `moved`
        (`Test_changed` holds that reading of git); the one design the
        branch edits is the one the arm reads."""
        monkeypatch.setattr(chain, "carried_by", lambda *_args: None)
        old, new = "seal/threads/1788000001-old", "seal/threads/1788000001-moved"
        moved = {f"{old}/frame/design.md", f"{new}/frame/design.md"}
        paths = [
            *sorted(moved),
            f"{MERGED_ITEM}/frame/plan.md",
            f"{MERGED_ITEM}/notes/frame/design.md",
            f"{ITEM}/frame/design.md",
        ]
        edited = chain.edited_work_items(".", "main", paths, moved, "seal/threads")
        assert edited == [ITEM], edited


# --- a check line inside a `to`, at the pull request (#1215) --------------------

# The refusal's text around `rules.py`'s reason, pinned here so an edit to
# `chain.CHECK_LINE_SAYS` meets a case.
CHECK_LINE_SAYS = (
    "`skills/settle/scripts/rules.py`, the reader `seal rules --check` uses, "
    "refuses this check line, which the settle writes into `{file}` as it "
    "stands: {why}"
)
COMMA = "check: f.txt, f.txt"
# A line whose one target the branch's tree holds.
HELD_LINE = "check: f.txt"


def change_to(*lines, old="old words."):
    """A `change` of `docs/policy.md` whose `to` holds LINES, its first on
    the field line, and whose `from` reads OLD."""
    to = "\n".join([f"  to: {lines[0]}", *(f"    {line}" for line in lines[1:])])
    return (
        f"- change\n  file: docs/policy.md\n  section: A section\n  from: {old}\n{to}\n"
    )


def check_line_refused(text, line, why, item=ITEM):
    """The `(path, line, problem)` the arm gives for the check line LINE of
    ITEM's spec reading TEXT, refused for WHY."""
    said = CHECK_LINE_SAYS.format(file="docs/policy.md", why=why)
    return (f"{item}/frame/design.md", line_at(text, line), said)


def check_line_refusal(text, line, why, item=ITEM):
    """The line the check prints outside CI for that refusal."""
    return "{}:{}  {}".format(*check_line_refused(text, line, why, item))


def reason(root, line):
    """`rules.py`'s one reason for refusing LINE in the tree at ROOT."""
    (why,) = chain.check_lines_reader().line_problems(str(root), line)
    return why


@pytest.mark.rule("a-check-line-in-a-to-is-read-at-the-pull-request")
class Test_check_lines_in:
    def test_refuses_a_line_the_reader_refuses_at_its_line_in_the_design(
        self, branch, ready, capsys, monkeypatch
    ):
        """S1: a `to` ending with `check: f.txt, f.txt` is refused at
        that line of the design, exit 1, with `rules.py`'s reason for the
        comma. Seen red against the base, which passed it at exit 0."""
        root, _code = branch
        text = spec_with(change_to("new words.", COMMA))
        put_spec(root, text)
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 1, out
        why = reason(root, COMMA)
        assert "`,` is no part of a check line" in why
        assert spec_lines(out) == [check_line_refusal(text, f"    {COMMA}", why)], out

    def test_accepts_a_line_the_reader_holds_and_prints_nothing(
        self, _branch_template, monkeypatch
    ):
        """S2: `check: f.txt`, a target the tree holds, holds, and nothing
        is named for the design. Seen red under the mutation that refuses
        every check line the `to` holds."""
        root, _code = _branch_template
        text = spec_with(change_to("new words.", HELD_LINE))
        assert read_spec(monkeypatch, root, text) == ([], [])

    def test_refuses_a_target_that_is_no_file_of_the_repository(
        self, _branch_template, monkeypatch
    ):
        """S3: a target that does not resolve in the tree is refused at its
        line with `rules.py`'s "does not exist". Seen red against the base."""
        root, _code = _branch_template
        line = "check: tests/no_such_file.py"
        text = spec_with(change_to("new words.", line))
        found, _notices = read_spec(monkeypatch, root, text)
        why = reason(root, line)
        assert why == "tests/no_such_file.py does not exist"
        assert found == [check_line_refused(text, f"    {line}", why)], found

    def test_refuses_a_line_on_the_field_line_at_the_field_line(
        self, _branch_template, monkeypatch
    ):
        """S6: a `to` whose value opens with the check line is refused at the
        `to:` line itself. Seen red against the base."""
        root, _code = _branch_template
        text = spec_with(change_to(COMMA))
        found, _notices = read_spec(monkeypatch, root, text)
        assert found == [
            check_line_refused(text, f"  to: {COMMA}", reason(root, COMMA))
        ], found

    def test_names_a_near_line_as_not_read_at_its_line_and_passes(
        self, _branch_template, monkeypatch
    ):
        """S4: `Check: x` opens like a check line and is not one; it is
        named as not read at its design line and decides nothing. Seen red
        under the mutation that drops the notices of a `to`."""
        root, _code = _branch_template
        text = spec_with(change_to("new words.", "Check: x"))
        found, notices = read_spec(monkeypatch, root, text)
        (why,) = [w for _, _, w in chain.check_lines_reader().unread_lines("Check: x")]
        notice = chain.RULE_CHANGES_UNREAD.format(why=why)
        number = line_at(text, "    Check: x")
        assert (found, notices) == ([], [(f"{ITEM}/frame/design.md", number, notice)])

    def test_reads_the_to_of_an_add_as_of_a_change(self, _branch_template, monkeypatch):
        """S1 for an `add`: the settle writes an `add`'s `to` into the policy
        root as it writes a `change`'s, so the comma line is refused at its
        line. Seen red under the mutation that reads a `change` alone."""
        root, _code = _branch_template
        text = spec_with(
            f"- add\n  file: docs/policy.md\n  to: new words.\n    {COMMA}\n"
        )
        found, _notices = read_spec(monkeypatch, root, text)
        assert found == [
            check_line_refused(text, f"    {COMMA}", reason(root, COMMA))
        ], found

    def test_reads_no_check_line_in_a_from(self, _branch_template, monkeypatch):
        """S5: the comma line in a `change`'s `from` and in a `remove`'s
        `from` passes and is not named, since the settle writes neither into
        the policy root. Seen red under the mutation that reads every field."""
        root, _code = _branch_template
        removed = (
            "- remove\n  file: docs/policy.md\n  section: A section\n"
            f"  from: old words.\n    {COMMA}\n"
        )
        old = f"old words.\n    {COMMA}"
        text = spec_with(change_to("new words.", HELD_LINE, old=old) + removed)
        assert read_spec(monkeypatch, root, text) == ([], [])

    def test_ends_at_exit_2_where_its_reader_will_not_load_or_read(
        self, branch, capsys, monkeypatch
    ):
        """A `rules.py` that will not load ends the arms at None, which
        `main` reads as exit 2, the reason on stderr; so does one that loads
        and cannot read the tree, a test file that does not parse where a
        `to` names a marker."""
        root, _code = branch
        reading(
            monkeypatch,
            {f"{ITEM}/frame/design.md": spec_with(change_to("new words.", HELD_LINE))},
        )
        there = chain.CHECK_LINES_READER
        monkeypatch.setattr(chain, "_check_lines", None)
        monkeypatch.setattr(chain, "CHECK_LINES_READER", str(root / "no_rules.py"))
        assert chain.rule_changes_of(str(root), [ITEM]) is None
        err = capsys.readouterr().err
        assert (
            "chain-check: the check-line reader `skills/settle/scripts/rules.py` "
            in err
        )
        assert "would not load" in err
        monkeypatch.setattr(chain, "CHECK_LINES_READER", there)
        write(root, "tests/test_broken.py", '@pytest.mark.rule("x")\ndef test_x(:\n')
        reading(
            monkeypatch,
            {
                f"{ITEM}/frame/design.md": spec_with(
                    change_to("new words.", "check: some-marker")
                )
            },
        )
        assert chain.rule_changes_of(str(root), [ITEM]) is None
        err = capsys.readouterr().err
        assert (
            "chain-check: `skills/settle/scripts/rules.py` could not read the check "
            f"lines of {ITEM}/frame/design.md: tests/test_broken.py could not be "
            "read as Python (SyntaxError)"
        ) in err


# --- the pins and copies of a rule change, at the pull request (#1216) ----------

# The notices' texts, pinned here so an edit to `chain.PIN_SAYS` or
# `chain.COPY_SAYS` meets a case.
PIN_SAYS = (
    "a test pins text this operation takes out of `{file}`: `{test}:{line}` "
    'holds "{literal}", and the `to` does not'
)
COPY_SAYS = (
    "this `to` repeats a passage of `{path}`: {count} of its runs of {window} "
    'words stand there, one of them "{run}"'
)
OLD_RULE = "the old rule says this"
# A literal of five words at line 3, a docstring holding the same words at
# line 2, and a literal of three words at line 4: the `from` below holds all
# three, and only the first is a pin.
PINNING = (
    "def test_x():\n"
    f'    """{OLD_RULE}"""\n'
    f'    assert "{OLD_RULE}" in text\n'
    '    assert "the old rule" in text\n'
)


def words_of(n):
    return " ".join(f"w{i}" for i in range(n))


def pin_said(file="docs/policy.md"):
    """The pin notice for `OLD_RULE` at line 3 of `tests/test_pinning.py`."""
    return PIN_SAYS.format(
        file=file, test="tests/test_pinning.py", line=3, literal=OLD_RULE
    )


def planted(monkeypatch, root, text):
    """`(found, notices)`: what `rule_changes_read` gives for ITEM's design
    reading TEXT in a copy's working tree at ROOT, read under `WORKTREE`,
    with the files a case planted there staged, so git lists them as
    tracked as `_read_tree` asks it."""
    write(root, f"{ITEM}/frame/design.md", text)
    git(root, "add", "-A")
    monkeypatch.setattr(chain, "WORKTREE", True)
    notices = []
    return chain.rule_changes_read(str(root), ITEM, notices), notices


def at(notices, path=f"{ITEM}/frame/design.md"):
    """`[(line, notice)]` of NOTICES standing at PATH."""
    return [(line, why) for where, line, why in notices if where == path]


@pytest.mark.rule("a-rule-change-names-the-pins-and-copies-it-breaks")
class Test_pins_and_copies_in:
    def test_names_a_pin_at_the_froms_line_and_no_docstring_or_three_words(
        self, branch, ready, capsys, monkeypatch
    ):
        """S1, S5: a `from` holding a test's literal of five words, which the
        `to` drops, is named at the `from`'s line, a notice annotation in CI,
        and the ready pull request exits 0. The docstring and the literal of
        three words the `from` also holds are not named. Seen red against the
        base, which printed nothing for the design."""
        root, _code = branch
        write(root, "tests/test_pinning.py", PINNING)
        text = spec_with(change_to("a new rule.", old=f"{OLD_RULE}."))
        put_spec(root, text)
        answered(monkeypatch)
        number = line_at(text, f"  from: {OLD_RULE}.")
        code, out = check(root, capsys)
        assert code == 0, out
        assert spec_lines(out) == [f"{ITEM}/frame/design.md:{number}  {pin_said()}"]
        monkeypatch.setenv("GITHUB_ACTIONS", "true")
        code, out = check(root, capsys)
        assert code == 0, out
        assert spec_lines(out) == [
            f"::notice file={ITEM}/frame/design.md,line={number}::{pin_said()}"
        ], out

    def test_accepts_a_to_that_keeps_the_literal_naming_nothing(
        self, branch, monkeypatch
    ):
        """S2: the `to` keeps the literal, so nothing is named. Seen red
        under the mutation that reads no `to`."""
        root, _code = branch
        write(root, "tests/test_pinning.py", PINNING)
        text = spec_with(change_to(f"So {OLD_RULE}, and more.", old=f"{OLD_RULE}."))
        assert planted(monkeypatch, root, text) == ([], [])

    def test_names_a_pin_in_a_section_a_remove_takes_out_whole(
        self, branch, monkeypatch
    ):
        """S3: a `remove` with no `from` takes its section out, as the working
        tree holds it, and a literal standing there is named at the
        operation's line. Seen red against the base."""
        root, _code = branch
        write(root, "tests/test_pinning.py", PINNING)
        write(
            root,
            "docs/policy.md",
            f"# Policy\n\n## A section\n\nWhere {OLD_RULE}, it\nstands.\n\n"
            "## Another\n\nOther words.\n",
        )
        text = spec_with("- remove\n  file: docs/policy.md\n  section: A section\n")
        found, notices = planted(monkeypatch, root, text)
        number = line_at(text, "- remove")
        assert (found, notices) == (
            [],
            [(f"{ITEM}/frame/design.md", number, pin_said())],
        )

    def test_names_a_copy_at_the_tos_line_and_no_run_of_fourteen(
        self, branch, monkeypatch
    ):
        """S4: a `to` sharing one run of 15 words with a `skills/` file names
        that file and the run at the `to`'s line; another file sharing 14
        words is not named. Seen red against the base."""
        root, _code = branch
        run = words_of(15)
        write(root, "skills/planted/SKILL.md", f"Its own words, then {run} and on.\n")
        write(root, "skills/short/SKILL.md", f"Then {words_of(14)} and on.\n")
        text = spec_with(change_to(f"New {run} rule."))
        found, notices = planted(monkeypatch, root, text)
        said = COPY_SAYS.format(
            path="skills/planted/SKILL.md", count=1, window=15, run=run
        )
        number = line_at(text, f"  to: New {run} rule.")
        assert (found, notices) == ([], [(f"{ITEM}/frame/design.md", number, said)])

    def test_refuses_to_name_a_copy_landing_in_a_korean_edition(
        self, branch, monkeypatch
    ):
        """S5: a `to` that lands in a `*.ko.md` file is outside the corpus and
        names no copy, though it shares a run of 15 words with a planted
        `skills/` file. Seen red with only the `.ko.md` exclusion of
        `passages.py#in_corpus` removed, the line naming that planted file."""
        root, _code = branch
        run = words_of(15)
        write(root, "skills/planted/SKILL.md", f"Its own words, then {run} and on.\n")
        text = spec_with(f"- add\n  file: docs/policy.ko.md\n  to: New {run} rule.\n")
        assert planted(monkeypatch, root, text) == ([], [])

    def test_names_a_test_file_that_does_not_parse_as_not_read(
        self, branch, monkeypatch
    ):
        """S5: a test file that does not parse is named as not read at its
        line 0, a notice, so nothing is refused for it. Seen red against the
        base."""
        root, _code = branch
        write(root, "tests/test_broken.py", "def test_x(:\n")
        text = spec_with(change_to("a new rule.", old=f"{OLD_RULE}."))
        found, notices = planted(monkeypatch, root, text)
        why = (
            "`tests/test_broken.py` could not be read as Python (SyntaxError), "
            "so no pin in it is named"
        )
        assert found == [] and at(notices) == [], notices
        assert at(notices, "tests/test_broken.py") == [(0, f"not read: {why}")]

    def test_names_a_rule_document_that_does_not_decode_as_not_read(
        self, branch, monkeypatch
    ):
        """A rule document that is not UTF-8 is named as not read at its line
        0, a notice, so nothing is refused for it. Seen red against the build
        before the document's notice existed, which skipped it silently."""
        root, _code = branch
        (root / "skills" / "bad").mkdir(parents=True)
        (root / "skills" / "bad" / "SKILL.md").write_bytes(b"\xff\xfe not text\n")
        found, notices = planted(monkeypatch, root, spec_with(change_to("a new rule.")))
        why = (
            "`skills/bad/SKILL.md` could not be read (UnicodeDecodeError), so no "
            "copy of it is named"
        )
        assert found == [], found
        assert at(notices, "skills/bad/SKILL.md") == [(0, f"not read: {why}")]

    def test_names_a_copy_a_change_keeps_in_its_to(self, branch, monkeypatch):
        """Round 2, finding 1: a `change` that shortens a passage of
        `docs/policy.md` and keeps a run of 15 of its words, beside an `add`
        of the whole passage to `docs/other.md`: `docs/policy.md` keeps a copy
        after the settle, named at the `add`'s `to`."""
        root, _code = branch
        passage = f"Then {words_of(15)} and on."
        kept = f"Then {words_of(15)} and see the other file."
        write(
            root,
            "docs/policy.md",
            f"# Policy\n\n## A section\n\n{passage}\n\n## Another\n\nOther words.\n",
        )
        text = spec_with(
            "- change\n  file: docs/policy.md\n  section: A section\n"
            f"  from: {passage}\n  to: {kept}\n"
            f"- add\n  file: docs/other.md\n  to: {passage}\n"
        )
        found, notices = planted(monkeypatch, root, text)
        said = COPY_SAYS.format(
            path="docs/policy.md", count=3, window=15, run=f"then {words_of(14)}"
        )
        number = line_at(text, f"  to: {passage}")
        assert (found, notices) == ([], [(f"{ITEM}/frame/design.md", number, said)])

    def test_names_a_passage_two_adds_of_one_design_put_in_two_documents(
        self, branch, monkeypatch
    ):
        """Round 3, finding 1: two `add`s of one passage into two documents
        that do not hold it. Each document holds it after the settle, so each
        `to` names the other document."""
        root, _code = branch
        passage = f"Then {words_of(15)} and on."
        write(root, "docs/a.md", "# A\n\n## One\n\nOther words here.\n")
        write(root, "docs/b.md", "# B\n\n## Two\n\nStill other words.\n")
        text = spec_with(
            f"- add\n  file: docs/a.md\n  section: One\n  to: {passage}\n"
            f"- add\n  file: docs/b.md\n  section: Two\n  to: {passage}\n"
        )
        found, notices = planted(monkeypatch, root, text)
        run = f"then {words_of(14)}"
        first, second = [
            i + 1 for i, ln in enumerate(text.split("\n")) if passage in ln
        ]
        assert found == [], found
        assert at(notices) == [
            (first, COPY_SAYS.format(path="docs/b.md", count=4, window=15, run=run)),
            (second, COPY_SAYS.format(path="docs/a.md", count=4, window=15, run=run)),
        ], notices

    def test_accepts_a_passage_the_design_moves_naming_no_copy(
        self, branch, monkeypatch
    ):
        """Round 1, finding 1: a design that removes a section of
        `docs/policy.md` and adds its passage to `docs/other.md` moves it, so
        `docs/policy.md` holds no copy after the settle and none is named."""
        root, _code = branch
        passage = f"Then {words_of(15)} and on."
        write(
            root,
            "docs/policy.md",
            f"# Policy\n\n## A section\n\n{passage}\n\n## Another\n\nOther words.\n",
        )
        text = spec_with(
            "- remove\n  file: docs/policy.md\n  section: A section\n"
            f"- add\n  file: docs/other.md\n  to: {passage}\n"
        )
        assert planted(monkeypatch, root, text) == ([], [])

    @pytest.mark.parametrize(
        "policy, why",
        [
            (None, "the document is not in the tree"),
            ("# Policy\n\n## Another\n\nwords.\n", "no heading `Missing`"),
        ],
        ids=["no-document", "no-section"],
    )
    def test_names_a_section_a_remove_cannot_read_as_not_read(
        self, branch, monkeypatch, policy, why
    ):
        """Round 1, finding 2: a `remove` with no `from` whose document or
        section the working tree lacks is named as not read at the
        operation's line, with the section reader's reason."""
        root, _code = branch
        if policy is not None:
            write(root, "docs/policy.md", policy)
        text = spec_with("- remove\n  file: docs/policy.md\n  section: Missing\n")
        found, notices = planted(monkeypatch, root, text)
        said = (
            "the section `Missing` of `docs/policy.md` that this `remove` takes "
            f"out could not be read ({why}), so no pin in it is named"
        )
        number = line_at(text, "- remove")
        assert (found, at(notices)) == ([], [(number, f"not read: {said}")])

    def test_names_a_test_and_a_document_it_cannot_open_as_not_read(
        self, branch, monkeypatch
    ):
        """Round 1, finding 2: a tracked test file and a tracked rule document
        that the working tree holds as a directory cannot be opened, and each
        is named as not read; the error's name is the platform's. The two are
        staged, then replaced, so git still lists them."""
        root, _code = branch
        write(root, "tests/test_gone.py", "x = 1\n")
        write(root, "skills/gone/SKILL.md", "Words.\n")
        write(root, f"{ITEM}/frame/design.md", spec_with(change_to("a new rule.")))
        git(root, "add", "-A")
        for rel in ("tests/test_gone.py", "skills/gone/SKILL.md"):
            (root / rel).unlink()
            (root / rel).mkdir()
        monkeypatch.setattr(chain, "WORKTREE", True)
        notices = []
        assert chain.rule_changes_read(str(root), ITEM, notices) == []
        test = "not read: `tests/test_gone.py` could not be read as Python ("
        document = "not read: `skills/gone/SKILL.md` could not be read ("
        ((line, said),) = at(notices, "tests/test_gone.py")
        assert line == 0 and said.startswith(test), notices
        ((line, said),) = at(notices, "skills/gone/SKILL.md")
        assert line == 0 and said.startswith(document), notices

    @pytest.mark.parametrize("error", [RecursionError, MemoryError])
    def test_names_a_test_the_parser_gives_up_on_as_not_read(
        self, branch, monkeypatch, error
    ):
        """Round 1, finding 2: `ast.parse` raises `RecursionError` or
        `MemoryError` on a source nested past its limit, and such a test file
        is named as not read rather than ending the check."""
        root, _code = branch
        write(root, "tests/test_deep.py", "x = 1  # deep\n")
        rules = chain.rule_changes_reader()
        literals = rules.literals

        def gives_up(source):
            if "# deep" in source:
                raise error
            return literals(source)

        monkeypatch.setattr(rules, "literals", gives_up)
        found, notices = planted(monkeypatch, root, spec_with(change_to("a new rule.")))
        why = (
            f"`tests/test_deep.py` could not be read as Python ({error.__name__}), "
            "so no pin in it is named"
        )
        assert found == [], found
        assert at(notices, "tests/test_deep.py") == [(0, f"not read: {why}")]

    def test_names_a_listing_git_could_not_make_as_not_read(self, branch, monkeypatch):
        """Round 1, finding 2: where git cannot list the tracked tests, none
        is read, and the run says so rather than reading as no pin."""
        root, _code = branch
        git_of = chain.git

        def no_listing(where, *args):
            # The tracked listing alone; `changed` lists untracked files too.
            return None if args[:2] == ("ls-files", "-z") else git_of(where, *args)

        monkeypatch.setattr(chain, "git", no_listing)
        found, notices = planted(monkeypatch, root, spec_with(change_to("a new rule.")))
        assert found == [], found
        for pathspec, what in (("tests/*.py", "pin"), ("*.md", "copy")):
            said = (
                f"git could not list the tracked files `{pathspec}` matches, so "
                f"none of them is read for a {what}"
            )
            assert ("", 0, f"not read: {said}") in notices, notices


# --- the parity arm at the pull request (#988) -------------------------------------

PARITY = "seal/parity.json"
routing_module = load(chain.ROUTING, "agentic_routing_for_chain_tests")


def with_original(text, said):
    """A round record with `original: SAID` under its `target:` line."""
    assert text.count(" against main\n") == 1
    return text.replace(" against main\n", f" against main\noriginal: {said}\n")


def original_lines(out):
    """The lines the check prints about a round record or the config."""
    where = (f"{ITEM}/trail/rounds/", f"{PARITY}:")
    return [ln for ln in out.splitlines() if ln.startswith(where)]


def originals_read(monkeypatch, root, originals, sha=BASELINE, paths=("f.txt",)):
    """`(what originals_of gives, the records it read)` for ITEM in the
    module's branch at ROOT, handed through `read_record` (`reading`) a
    migration config whose baseline is SHA and each round record N with
    `original: <ORIGINALS[N-1]>`, none where that is None; PATHS are the
    pull request's."""
    texts = {PARITY: parity_file(sha)}
    for n, said in enumerate(originals, 1):
        rel = f"{ITEM}/trail/rounds/round-{n}.md"
        text = (root / rel).read_text("utf-8")
        texts[rel] = text if said is None else with_original(text, said)
    reading(monkeypatch, texts)
    found = chain.originals_of(
        routing_module,
        str(root),
        "seal",
        None if paths is None else list(paths),
        [ITEM],
    )
    return found, texts


@pytest.mark.rule("parity-at-the-pull-request")
class Test_originals_of:
    def test_refuses_a_record_with_no_original_line_on_a_ready_pull_request(
        self, branch, ready, capsys, monkeypatch
    ):
        """S4: in a repository declaring `seal/parity.json`, a chain-declared
        pull request changing code fails while a round record holds no
        `original:` line, each record named with the baseline it owes, and a
        draft prints the same lines and exits 0. The branch commits the
        config itself, since the arm reads it at HEAD wherever it came
        from."""
        root, _code = branch
        write(root, PARITY, parity_file(BASELINE))
        commit(root, "a migration, declared")
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 1, out
        says = chain.NO_ORIGINAL.format(config=PARITY, sha=BASELINE)
        for words in (
            f"no `original:` line in the round block: `{PARITY}` declares a migration",
            f"each round record's round block carries `original: {BASELINE}`",
            "written by the proofer once it compared the round's target with "
            "the original through `legacy-parity`",
        ):
            assert words in says, says
        assert original_lines(out) == [
            f"{ITEM}/trail/rounds/round-{n}.md:3  {says}" for n in (1, 2)
        ], out
        ready.write_text(json.dumps({"pull_request": {"draft": True}}), "utf-8")
        code, out = check(root, capsys)
        assert code == 0, out
        assert len(original_lines(out)) == 2, out

    @pytest.mark.parametrize(
        "originals, sha",
        [
            ((BASELINE[:8], BASELINE), BASELINE),
            ((BASELINE, BASELINE[:12]), BASELINE[:7]),
        ],
        ids=["short-in-the-record", "short-in-the-config"],
    )
    def test_accepts_a_record_naming_the_baseline_by_either_prefix(
        self, _branch_template, monkeypatch, originals, sha
    ):
        root, _code = _branch_template
        assert originals_read(monkeypatch, root, originals, sha)[0] == []

    def test_refuses_a_record_naming_another_commit_naming_both(
        self, _branch_template, monkeypatch
    ):
        root, _code = _branch_template
        other = "fedcba9876543210"
        found, texts = originals_read(monkeypatch, root, (BASELINE, other))
        rel = f"{ITEM}/trail/rounds/round-2.md"
        line = line_at(texts[rel], f"original: {other}")
        says = chain.OTHER_ORIGINAL.format(said=other, sha=BASELINE)
        assert found == [(rel, line, says)], found
        assert other in says and BASELINE in says

    def test_refuses_a_config_whose_baseline_holds_no_commit(
        self, _branch_template, monkeypatch
    ):
        """S10: the template's placeholder is refused naming
        `seal/parity.json`, and no record is compared with nothing."""
        root, _code = _branch_template
        found, _texts = originals_read(monkeypatch, root, (BASELINE, BASELINE), None)
        ((path, line, why),) = found
        assert (path, line) == (PARITY, 0), found
        assert "`Baseline commit`" in why and "`<SHA>`" in why, why

    def test_accepts_a_change_confined_to_the_document_roots(
        self, _branch_template, monkeypatch
    ):
        """S7 and S11: a change confined to `docs/` and `seal/` owes no line,
        one path outside them owes it, and paths git could not list owe it
        too, as `lib/gate.py#touches_code` reads them."""
        root, _code = _branch_template
        inside = ["docs/a.md", f"{ITEM}/trail/rounds/round-1.md"]

        def owed(paths):
            return originals_read(monkeypatch, root, (None, None), paths=paths)[0]

        assert owed(inside) == []
        assert [p for p, _n, _w in owed([*inside, "f.txt"])] == [
            f"{ITEM}/trail/rounds/round-1.md",
            f"{ITEM}/trail/rounds/round-2.md",
        ]
        assert owed(None) == owed([*inside, "f.txt"])

    def test_refuses_to_run_where_the_parity_readers_will_not_load(
        self, _branch_template, ready, capsys, monkeypatch
    ):
        """`originals_of` gives None, which `main` reads as exit 2, the
        reason on stderr. The config is handed over (`reading`), so `main`
        runs over the module's branch as it stands."""
        root, _code = _branch_template
        monkeypatch.setattr(chain, "parity_readers", will_not_load)
        assert originals_read(monkeypatch, root, (None, None))[0] is None
        err = capsys.readouterr().err
        assert "the parity readers would not load (a planted failure)" in err
        code = chain.main(["--baseline", "main", "--root", str(root)])
        err = capsys.readouterr().err
        assert code == 2, err
        assert "the parity readers would not load (a planted failure)" in err

    @pytest.mark.rule("parity-in-the-guarantee")
    def test_refuses_a_direct_guarantee_with_no_original_line_and_accepts_one(
        self, _item_template, ready, capsys, monkeypatch
    ):
        """S12: under `straight to the PR` no round records a comparison, so
        in a migration repository the sealer's `guarantee.md` carries the
        `original:` line, and a ready pull request changing code fails
        without it, names a guarantee naming another commit, and passes with
        the baseline. `--sealing` reads the missing line as a notice, as it
        reads every other guarantee check. The config and the guarantee are
        handed over (`reading`), so `main` runs over the module's sealed
        branch as it stands."""
        root, audited = _item_template
        answered(monkeypatch)
        rel = f"{ITEM}/guarantee.md"
        says = chain.NO_GUARANTEE_ORIGINAL.format(config=PARITY, sha=BASELINE)
        for words in (
            f"no `original:` line in the newest verdict block: `{PARITY}` "
            "declares a migration, this work item answers `straight to the PR`",
            f"the sealer's guarantee carries `original: {BASELINE}`",
            "once it compared the audited commit with the original through "
            "`legacy-parity`",
        ):
            assert words in says, says
        assert direct_originals(monkeypatch, root, audited, None) == [
            (rel, guarantee(audited, "sealed").split("\n").index("```seal") + 1, says)
        ]
        code, out = check(root, capsys)
        assert code == 1, out
        opener = guarantee(audited, "sealed").split("\n").index("```seal")
        assert f"{rel}:{opener + 1}  {says}" in out.splitlines(), out
        code, out = check(root, capsys, "--sealing")
        assert code == 0, out
        other = guarantee(audited, "sealed", "fedcba9876543210")
        assert direct_originals(monkeypatch, root, audited, "fedcba9876543210") == [
            (
                rel,
                other.split("\n").index("original: fedcba9876543210") + 1,
                chain.OTHER_ORIGINAL.format(said="fedcba9876543210", sha=BASELINE),
            )
        ]
        assert direct_originals(monkeypatch, root, audited, BASELINE[:10]) == []

    @pytest.mark.rule("parity-in-the-guarantee")
    def test_refuses_a_direct_guarantee_whose_only_original_is_misspelt(
        self, _item_template, monkeypatch
    ):
        """The third scenario of #1167, #1121's R9, under #1198's blocks: in a
        migration repository a verdict block holding `Original: <sha>` is
        refused at that line with the keys the block takes, and the original
        arm adds no second refusal for a guarantee the guarantee arm refuses.
        Seen red against the reader of #1167, which read the line as prose,
        named it as not read and refused the file for lacking the line."""
        root, audited = _item_template
        rel = f"{ITEM}/guarantee.md"
        assert direct_originals(monkeypatch, root, audited, BASELINE) == []
        text = guarantee(audited, "sealed", BASELINE).replace("original:", "Original:")
        assert direct_originals(monkeypatch, root, audited, text=text) == []
        number = text.splitlines().index(f"Original: {BASELINE}") + 1
        said = chain.FIELDS.NOT_A_FIELD.format(
            line=f"Original: {BASELINE}",
            kind="verdict",
            keys="`target:`, `original:` and `Verdict:`",
        )
        assert chain.guarantee(str(root), ITEM, "main") == [(rel, number, said)]

    @pytest.mark.rule("parity-in-the-guarantee")
    def test_a_missing_guarantee_is_named_once(self, _item_template, monkeypatch):
        """A guarantee git does not carry is the guarantee arm's refusal, and
        no second one asks it for an `original:` line."""
        root, audited = _item_template
        assert direct_originals(monkeypatch, root, audited, text=None) == []
        ((_path, _line, why),) = chain.guarantee(str(root), ITEM, "main")
        assert "git carries no guarantee file" in why, why

    @pytest.mark.rule("parity-in-the-guarantee")
    def test_a_direct_guarantee_owes_nothing_for_the_document_roots_alone(
        self, _item_template, monkeypatch
    ):
        """S12: a change confined to `docs/` and `seal/` has no original to
        compare with, and a repository declaring no migration owes nothing."""
        root, audited = _item_template
        inside = ["docs/a.md", f"{ITEM}/routing.md", f"{ITEM}/guarantee.md"]
        assert direct_originals(monkeypatch, root, audited, None, paths=inside) == []
        assert direct_originals(monkeypatch, root, audited, None, config=None) == []

    @pytest.mark.rule("parity-in-the-guarantee")
    def test_owes_no_original_line_where_none_is_owed(
        self, _item_template, monkeypatch
    ):
        """Round 4 of #1167: a guarantee's `original:` line is owed only where
        `originals_of` reads the guarantee: with no migration config, and
        with one where the diff stays inside the document roots, a verdict
        block without one passes, and a block holding `Original: <sha>` is
        refused for its line alone, never for a missing `original:` line."""
        root, audited = _item_template
        text = guarantee(audited, "sealed", BASELINE)
        assert text.count("original:") == 1, text
        respelt = text.replace("original:", "Original:")
        inside = ["docs/a.md", f"{ITEM}/routing.md", f"{ITEM}/guarantee.md"]
        for config, paths in ((None, ["f.txt"]), (parity_file(BASELINE), inside)):
            for said in (guarantee(audited, "sealed"), respelt):
                owed = direct_originals(
                    monkeypatch, root, audited, text=said, config=config, paths=paths
                )
                assert owed == [], (config, said)
            refused = chain.guarantee(str(root), ITEM, "main")
            assert (
                len(refused) == 1 and "is no field of a verdict block" in refused[0][2]
            )


class Test_original_of:
    def test_accepts_a_line_naming_the_baseline_by_a_prefix(self):
        text = with_original(record("abc1234", [finding(1, "rejected")]), BASELINE[:9])
        assert chain.original_of(text, "r.md", BASELINE, PARITY) == []

    @pytest.mark.parametrize(
        "where, said",
        [
            ("inside", "is no field of a finding block"),
            ("twice", "a second `original:` line: a round block holds one"),
            ("spelt", "is no field of a round block"),
        ],
    )
    def test_refuses_a_line_the_blocks_refuse_at_its_line_and_only_so(
        self, where, said
    ):
        """S9 and #1121's R9: an `original:` line in a finding block, a
        second one in the round block, and one spelt `Original:` are refused
        at the line by the block grammar, and `original_of` adds no second
        refusal saying the record has none."""
        text = record("abc1234", [finding(1, "rejected")])
        if where == "inside":
            text = text.replace(
                "evidence: read `f.txt:1`\n",
                f"evidence: read `f.txt:1`\noriginal: {BASELINE}\n",
            )
            line = f"original: {BASELINE}"
        elif where == "twice":
            text = with_original(with_original(text, BASELINE), BASELINE)
            line = f"original: {BASELINE}"
        else:
            text = with_original(text, BASELINE).replace("original:", "Original:")
            line = f"Original: {BASELINE}"
        _round, errors = chain.round_of(text, "r.md", 1)
        assert [(n, said in why) for _r, n, why in errors] == [
            (line_at(text, line, where == "twice"), True)
        ], errors
        assert chain.original_of(text, "r.md", BASELINE, PARITY) == []

    def test_refuses_a_round_block_with_no_original_line_at_its_opener(self):
        text = record("abc1234", [finding(1, "rejected")])
        assert chain.original_of(text, "r.md", BASELINE, PARITY) == [
            ("r.md", 3, chain.NO_ORIGINAL.format(config=PARITY, sha=BASELINE))
        ]
        assert chain.original_of(LABELLED, "r.md", BASELINE, PARITY) == []


class Test_parity_readers:
    def test_accepts_a_process_that_loaded_only_the_check(self):
        """`parity_readers` loads `lib/config.py` and `lib/gate.py`, so a fresh
        interpreter that loaded the check alone still loads both."""
        code = (
            "import importlib.util, sys\n"
            f"s = importlib.util.spec_from_file_location('c', {str(CHAIN)!r})\n"
            "m = importlib.util.module_from_spec(s)\n"
            "s.loader.exec_module(m)\n"
            "config, gate = m.parity_readers()\n"
            "print(gate.touches_code(['f.txt'], 'seal'), config.BASELINE_KEY)\n"
        )
        done = subprocess.run(
            [sys.executable, "-I", "-c", code],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
        assert done.returncode == 0, done.stderr
        assert done.stdout.strip() == "True Baseline commit", done.stdout

    def test_refuses_to_hide_a_reader_that_will_not_load(self, monkeypatch, tmp_path):
        """A `lib/gate.py` that raises at import is raised to the caller,
        which `originals_of` turns into exit 2; nothing hands back a reader
        that did not load."""
        real = chain.sibling.load

        def load(rel):
            if rel == "lib/gate.py":
                raise ImportError("planted")
            return real(rel)

        monkeypatch.setattr(chain.sibling, "load", load)
        with pytest.raises(ImportError, match="planted"):
            chain.parity_readers()


# --- the sealer's guarantee (#969, #1000) ------------------------------------------

GUARANTEE_TEMPLATE = ROOT / "templates" / "records" / "sdd-guarantee.md"


def guarantee(sha, verdict, original=None, earlier=()):
    """A `guarantee.md` from the template: its tables for people, then a
    verdict block per run of EARLIER, each `(sha, verdict)`, then the newest
    run's block for SHA, holding ORIGINAL where it is given."""
    runs = [verdict_block(s, v) for s, v in earlier]
    runs.append(verdict_block(sha, verdict, original))
    return (
        "# 1791999990-a-guaranteed-item — guarantee\n\n"
        "## Claims re-run\n\n"
        "| Claim | Source | Command | Result |\n|---|---|---|---|\n\n"
        "## The parties\n\n"
        "| Party | Says | Agrees with | Disagrees with |\n|---|---|---|---|\n\n"
        + "\n".join(runs)
    )


SEALED_ROUTING = """# routing

| Axis | Answer |
|---|---|
| Review | straight to the PR |
| Destination | open the pull request |
| Planning | the session |
| Branch | feature/g |
"""


@pytest.fixture(scope="module")
def _item_template(tmp_path_factory):
    """A branch that went straight to the pull request and was sealed: the
    code, then `trail/gate.md` and `guarantee.md` naming that commit, built
    once for the module. Returns `(root, the audited commit)`."""
    d = tmp_path_factory.mktemp("chain-sealed") / "g"
    born(d, "feature/g")
    _base, audited = imported(
        d,
        ("main", None, "base", {"f.txt": "one\n"}),
        (
            "feature/g",
            ":1",
            "the work",
            {f"{ITEM}/routing.md": SEALED_ROUTING, "f.txt": "two\n"},
        ),
    )
    imported(
        d,
        (
            "feature/g",
            audited,
            "the closing records",
            {
                f"{ITEM}/trail/gate.md": gate_file(audited),
                f"{ITEM}/guarantee.md": guarantee(audited, "sealed"),
            },
        ),
        at=1700000010,
    )
    git(d, "reset", "-q", "--hard")
    return d, audited


@pytest.fixture
def item(tmp_path, monkeypatch, _item_template):
    """A copy of the module's sealed branch for one case, which the case may
    change, judged as a ready pull request."""
    template, audited = _item_template
    d = tmp_path / "g"
    shutil.copytree(template, d)
    event(tmp_path, monkeypatch, False)
    return d, audited


def direct_originals(
    monkeypatch, root, audited, original=None, text=..., config=..., paths=("f.txt",)
):
    """What `originals_of` gives for ITEM declared `straight to the PR` in
    the module's sealed branch at ROOT, handed through `read_record`
    (`reading`) the guarantee TEXT, by default one sealed at AUDITED whose
    newest block holds `original: ORIGINAL` where that is given, and the
    migration config CONFIG, by default one whose baseline is `BASELINE`,
    None for none; PATHS are the pull request's."""
    if text is ...:
        text = guarantee(audited, "sealed", original)
    if config is ...:
        config = parity_file(BASELINE)
    reading(monkeypatch, {PARITY: config, f"{ITEM}/guarantee.md": text})
    return chain.originals_of(
        routing_module, str(root), "seal", list(paths), [], [ITEM]
    )


# S6 of #1000: lines that open with the key and are not one of its three
# shapes, and a word the verdict used before #969. Each is refused at its
# line naming the three, and none reads as `sealed`.
NEAR_MISSES = (
    "Verdict: withheld — x",
    "Verdict: withheld - x",
    "Verdict: withheld",
    "Verdict: withheld reason:",
    "Verdict: withheld reason:x",
    "Verdict: withheld reason:  x",
    "Verdict: Sealed",
    "Verdict: **sealed**",
    "Verdict: sealed reason: x",
    "Verdict: undecided reason: x",
    "Verdict: sound",
)
# #1198: lines that open like the key and are not it. Inside a verdict block
# each is no field of its kind, refused at its line with the keys the block
# takes.
OPENS_LIKE = (
    "**Verdict:** sealed",
    "verdict: sealed",
    "    Verdict: sealed",
    "\tVerdict: sealed",
)


def guarantee_read(monkeypatch, root, text, notices=None):
    """What the guarantee arm gives for ITEM in the sealed branch at ROOT,
    its `guarantee.md` handed over as TEXT (`reading`)."""
    reading(monkeypatch, {f"{ITEM}/guarantee.md": text})
    return chain.guarantee(str(root), ITEM, "main", notices)


def gate_read(monkeypatch, root, text, notices=None):
    """What the broad gate arm gives for ITEM in the sealed branch at ROOT,
    its `trail/gate.md` handed over as TEXT (`reading`)."""
    reading(monkeypatch, {f"{ITEM}/trail/gate.md": text})
    return chain.broad_gate(str(root), ITEM, "main", notices)


class Test_blocks_of:
    def test_accepts_a_records_blocks_and_hands_its_notices_over(self):
        text = verdict_block("abc1234") + "\n```Seal\nx\n```\n"
        notices = []
        found, problems = chain.blocks_of("g.md", text, chain.FIELDS.GUARANTEE, notices)
        assert problems == [] and len(found) == 1
        assert notices == [("g.md", 6, chain.FIELDS.NEAR.format(line="```Seal"))]

    def test_refuses_each_line_the_reader_refuses_at_its_line(self):
        text = verdict_block("abc1234").replace("Verdict:", "verdict:")
        found, problems = chain.blocks_of("g.md", text, chain.FIELDS.GUARANTEE)
        assert found == []
        assert [(path, line) for path, line, _why in problems] == [("g.md", 3)]


@pytest.mark.rule("ready-needs-sealed")
class Test_guarantee:
    def test_accepts_a_sealed_verdict_at_head(self, _item_template):
        root, _sha = _item_template
        assert chain.guarantee(str(root), ITEM, "main") == []

    def test_accepts_the_newest_of_two_runs(self, _item_template, monkeypatch):
        """#1198's scenario *Two sealer runs*: the sealer appends a verdict
        block per run, so a `withheld` at an older commit above a `sealed`
        at HEAD passes, and the same blocks the other way round read the
        newest as `withheld`. Seen red against the reader that read the
        first block."""
        root, sha = _item_template
        older = git(root, "rev-parse", "HEAD~2")
        text = guarantee(sha, "sealed", earlier=[(older, "withheld reason: x")])
        assert guarantee_read(monkeypatch, root, text) == []
        swapped = verdict_block(sha) + "\n" + verdict_block(older, "withheld reason: x")
        problems = guarantee_read(monkeypatch, root, swapped)
        assert any("`Verdict: withheld reason: x`" in why for _p, _n, why in problems)

    def test_refuses_absent_unfilled_and_behind_head_by_name(self, item, monkeypatch):
        """A record committed after the guarantee is refused naming that
        commit, read through git; the template unfilled, a verdict above
        the target and no guarantee at all are handed over (`reading`)."""
        root, _sha = item
        rel = f"{ITEM}/guarantee.md"
        write(root, f"{ITEM}/gaps.md", "# an edit the sealer never read\n")
        later = commit(root, "a record after the guarantee")
        [(path, _line, why)] = chain.guarantee(str(root), ITEM, "main")
        assert path == rel and later[:8] in why
        template = GUARANTEE_TEMPLATE.read_text(encoding="utf-8")
        [(path, line, why)] = guarantee_read(monkeypatch, root, template)
        placeholder = template.split("\n")[line - 1]
        assert path == rel and placeholder.startswith("target: <"), placeholder
        assert why.startswith(f"`{placeholder}` does not read whole"), why
        two = guarantee(later, "sealed").replace(
            "```seal\n", "```seal\nVerdict: sealed\n"
        )
        [(_p, _n, why)] = guarantee_read(monkeypatch, root, two)
        assert why == chain.FIELDS.NO_KIND.format(
            line="Verdict: sealed", openers="`target:`"
        )
        [(_p, _n, why)] = guarantee_read(monkeypatch, root, None)
        assert "git carries no guarantee file" in why

    def test_refuses_a_guarantee_of_the_old_shape_naming_the_template(
        self, _item_template, monkeypatch
    ):
        """#1198's scenario *A record from before the change*, for the
        guarantee, and *Scope* item 9: a `Target SHA` row and a `Verdict:`
        line hold no verdict block, and the one refusal names the template
        and says the sealer appends a block. Seen red against the reader
        before #1198, which passed the record."""
        root, sha = _item_template
        rel = f"{ITEM}/guarantee.md"
        old = (
            "| Field | Value |\n|---|---|\n"
            f"| Target SHA | {sha} against main |\n\nVerdict: sealed\n"
        )
        assert guarantee_read(monkeypatch, root, old) == [
            (rel, 0, chain.NO_VERDICT_BLOCK)
        ]
        assert "`templates/records/sdd-guarantee.md`" in chain.NO_VERDICT_BLOCK
        assert "appends one" in chain.NO_VERDICT_BLOCK

    def test_refuses_a_fence_nobody_closed_between_two_runs(
        self, _item_template, monkeypatch
    ):
        """#1122, at the check: a `sealed` block, then a fence nobody closed,
        then a `withheld` block. A renderer hides everything below the
        fence, so the check refuses it at its opener."""
        root, sha = _item_template
        rel = f"{ITEM}/guarantee.md"
        newest = verdict_block(sha, "withheld reason: the gate failed")
        text = guarantee(sha, "sealed") + "\n````\n\n" + newest
        opener = text.split("\n").index("````") + 1
        assert guarantee_read(monkeypatch, root, text) == [
            (rel, opener, chain.FIELDS.UNCLOSED)
        ]

    def test_an_opener_quoted_in_a_code_span_hides_no_verdict(
        self, _item_template, monkeypatch
    ):
        """Round 1 of #1000, finding 2: a claims cell quoting the comment
        opener in a code span, as two merged guarantees do, leaves the
        verdict block below it read."""
        root, sha = _item_template
        text = guarantee(sha, "sealed").replace(
            "|---|---|---|---|\n\n## The parties",
            "|---|---|---|---|\n| markers | `x.md:1` | `git grep '<!-- specs/'` "
            "| holds |\n\n## The parties",
        )
        assert guarantee_read(monkeypatch, root, text) == []

    @pytest.mark.rule("record-comment-line-refused")
    def test_refuses_a_comment_line_at_its_line(self, _item_template, monkeypatch):
        """S5 of #1012: a verdict quoted in a comment above the verdict block
        is refused at its line."""
        root, sha = _item_template
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace(
            "```seal\n", "<!-- Verdict: sealed -->\n```seal\n"
        )
        line = text.splitlines().index("<!-- Verdict: sealed -->") + 1
        assert guarantee_read(monkeypatch, root, text) == [
            (rel, line, chain.FIELDS.COMMENT_LINE)
        ]

    @pytest.mark.parametrize("line", NEAR_MISSES)
    def test_refuses_a_near_miss_of_the_verdict_at_its_line(
        self, _item_template, monkeypatch, line
    ):
        """S6 of #1000, inside a verdict block: the value is read whole
        against the three shapes and refused at its line naming them. A word
        the verdict used before #969 needs no list of its own (#1198,
        `## Removes`)."""
        root, sha = _item_template
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace("Verdict: sealed", line)
        [(path, number, why)] = guarantee_read(monkeypatch, root, text)
        assert (path, number) == (rel, text.splitlines().index(line) + 1), why
        for shape in (
            "`Verdict: sealed`",
            "`Verdict: withheld reason: <reason>`",
            "`Verdict: undecided question: <question>`",
        ):
            assert shape in why, why

    @pytest.mark.parametrize("line", OPENS_LIKE)
    def test_refuses_a_line_that_opens_like_the_verdict_at_its_line(
        self, _item_template, monkeypatch, line
    ):
        """#1198: inside a block a line is a field or refused, so a verdict
        spelt otherwise is refused at its line with the keys a verdict block
        takes, where #1167 read it as prose. Seen red against that reader,
        which named it and refused the file for having no verdict line."""
        root, sha = _item_template
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace("Verdict: sealed", line)
        number = text.splitlines().index(line) + 1
        said = chain.FIELDS.NOT_A_FIELD.format(
            line=line, kind="verdict", keys="`target:`, `original:` and `Verdict:`"
        )
        assert guarantee_read(monkeypatch, root, text) == [(rel, number, said)]

    def test_names_a_near_opener_and_reads_no_verdict(
        self, _item_template, ready, capsys, monkeypatch
    ):
        """A fence like the block's and not it is no block: the guarantee
        holding it alone has no verdict block, and the opener is printed at
        its line as not read, which adds nothing to the exit code. `main`
        runs over the module's sealed branch, the guarantee handed over."""
        root, sha = _item_template
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace("```seal", "```Seal")
        notices = []
        assert guarantee_read(monkeypatch, root, text, notices) == [
            (rel, 0, chain.NO_VERDICT_BLOCK)
        ]
        number = text.splitlines().index("```Seal") + 1
        said = chain.FIELDS.NEAR.format(line="```Seal")
        assert notices == [(rel, number, said)]
        code, out = check(root, capsys)
        assert code == 1 and f"{rel}:{number}  {said}" in out.splitlines(), out

    def test_a_verdict_other_than_sealed_fails_a_ready_pull_request(
        self, item, capsys, monkeypatch
    ):
        """T8, S8 of #969: `withheld` and `undecided` fail a ready pull request
        naming the file and the verdict; a draft prints the same line and
        passes; `--sealing`, the broad gate's own run, prints it. `withheld`
        is committed and judged by `main`; `undecided` is read by the arm,
        handed over."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        verdict = "withheld reason: the body claims a README change"
        write(root, rel, guarantee(sha, verdict))
        commit(root, f"the sealer says {verdict}")
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 1, out
        line = next(ln for ln in out.splitlines() if ln.startswith(f"{rel}:"))
        assert f"`Verdict: {verdict}`" in line and "needs `sealed`" in line, line
        assert "appends its block" in line, line
        code, out = check(root, capsys, "--sealing")
        assert code == 0 and rel in out
        event = root.parent / "event.json"
        event.write_text(
            json.dumps({"pull_request": {"draft": True}}), encoding="utf-8"
        )
        code, out = check(root, capsys)
        assert code == 0 and rel in out
        [(_p, _n, why)] = guarantee_read(
            monkeypatch, root, guarantee(sha, "undecided question: Q?")
        )
        assert "`Verdict: undecided question: Q?`" in why, why
        assert "needs `sealed`" in why and "appends its block" in why, why


class Test_guarantee_original:
    def test_accepts_the_newest_blocks_baseline_or_a_prefix_of_it(self):
        for said in (BASELINE, BASELINE[:10]):
            text = guarantee("abc1234", "sealed", said, earlier=[("abc1234", "sealed")])
            assert chain.guarantee_original(text, "g.md", BASELINE, PARITY) == []

    def test_refuses_a_newest_block_with_none_or_another(self):
        """#1198, *Scope* item 3: the newest block's `original:` is read, and
        one in an earlier block does not stand for it."""
        earlier = verdict_block("abc1234", "withheld reason: x", BASELINE)
        text = earlier + "\n" + verdict_block("abc1234")
        newest = text.split("\n").index("```seal", 2) + 1
        says = chain.NO_GUARANTEE_ORIGINAL.format(config=PARITY, sha=BASELINE)
        assert chain.guarantee_original(text, "g.md", BASELINE, PARITY) == [
            ("g.md", newest, says)
        ]
        other = guarantee("abc1234", "sealed", "fedcba9876543210")
        line = other.split("\n").index("original: fedcba9876543210") + 1
        said = chain.OTHER_ORIGINAL.format(said="fedcba9876543210", sha=BASELINE)
        assert chain.guarantee_original(other, "g.md", BASELINE, PARITY) == [
            ("g.md", line, said)
        ]

    def test_refuses_nothing_of_a_guarantee_the_guarantee_arm_refuses(self):
        for text in (
            "Verdict: sealed\n",
            verdict_block("abc1234").replace("Verdict:", "verdict:"),
            verdict_block("abc1234") + "\n<!-- a note -->\n",
        ):
            assert chain.guarantee_original(text, "g.md", BASELINE, PARITY) == []


class Test_broad_gate:
    def test_accepts_a_run_at_head(self, _item_template):
        root, _sha = _item_template
        assert chain.broad_gate(str(root), ITEM, "main") == []

    def test_accepts_the_last_run_block_as_the_newest(
        self, _item_template, monkeypatch
    ):
        """#1198, *Scope* item 2: `seal gate --record` appends a block per
        run, so the last block is the newest run, and an earlier block naming
        a commit nobody can see decides nothing; the same blocks the other
        way round are a stale run. Seen red against the reader that took the
        first block."""
        root, sha = _item_template
        rel = f"{ITEM}/trail/gate.md"
        assert gate_read(monkeypatch, root, gate_file("1" * 40, sha)) == []
        [(path, line, why)] = gate_read(monkeypatch, root, gate_file(sha, "1" * 40))
        assert (path, line) == (rel, 0) and "the newest gate run" in why, why

    def test_lets_the_records_follow_the_run_and_refuses_any_other_path(self, item):
        """#1596: a commit after the newest run that changes only the work
        item's records owes no broad run, while the guarantee, which only
        the closing records may follow, asks for the sealer again; a later
        commit of a path outside the records is refused, naming it."""
        root, _sha = item
        write(root, f"{ITEM}/pr.md", "Closes #1\n")
        write(root, f"{ITEM}/changelog.md", "### Changed\n\n- A repair.\n")
        records = commit(root, "a prose repair after the gate")
        assert chain.broad_gate(str(root), ITEM, "main") == []
        assert chain.guarantee(str(root), ITEM, "main") == [
            (
                f"{ITEM}/guarantee.md",
                0,
                chain.follows_reason(
                    ("after", records, f"{ITEM}/changelog.md"),
                    "the guarantee",
                    "the closing records",
                )
                + "; the sealer runs again",
            )
        ]
        write(root, "f.txt", "three\n")
        code = commit(root, "a code change after the gate")
        assert chain.broad_gate(str(root), ITEM, "main") == [
            (
                f"{ITEM}/trail/gate.md",
                0,
                chain.follows_reason(("after", code, "f.txt"), "the newest gate run"),
            )
        ]

    @pytest.mark.rule("record-comment-line-refused")
    def test_refuses_a_comment_line_at_its_line(self, _item_template, monkeypatch):
        """S5 of #1012: a `trail/gate.md` line that begins with `<!--` is
        refused at its line."""
        root, sha = _item_template
        rel = f"{ITEM}/trail/gate.md"
        text = "<!-- the gate's guidance -->\n\n" + gate_file(sha)
        assert gate_read(monkeypatch, root, text) == [
            (rel, 1, chain.FIELDS.COMMENT_LINE)
        ]

    def test_refuses_a_record_with_no_run_block_naming_the_command(
        self, _item_template, monkeypatch
    ):
        """#1198, *Scope* item 9: a gate record of the shape before 0.27.0, its
        run a table cell, holds no run block, and is refused with the one
        sentence that names the command which appends one."""
        root, sha = _item_template
        rel = f"{ITEM}/trail/gate.md"
        text = f"| Field | Value |\n|---|---|\n| Broad gate | {sha} against main |\n"
        assert gate_read(monkeypatch, root, text) == [(rel, 0, chain.NO_RUN_BLOCK)]
        # The command the refusal names, which the orchestrator runs to append
        # a run block.
        assert "`seal gate --base <base> --record <item>`" in chain.NO_RUN_BLOCK
        assert "since #1198" in chain.NO_RUN_BLOCK

    def test_refuses_a_run_block_that_does_not_parse_at_its_line(
        self, _item_template, monkeypatch
    ):
        root, sha = _item_template
        rel = f"{ITEM}/trail/gate.md"
        text = gate_file(sha).replace(f"run: {sha}", f"run:  {sha}")
        [(path, line, why)] = gate_read(monkeypatch, root, text)
        assert (path, line) == (
            rel,
            text.splitlines().index(f"run:  {sha} against {GATE_BASE}") + 1,
        )
        assert why.startswith(
            f"`run:  {sha} against {GATE_BASE}` does not read whole"
        ), why

    def test_names_a_near_opener_as_not_read(self, _item_template, monkeypatch):
        """A fence like the block's and not it is named in NOTICES, and its
        run is no run: the record then holds none."""
        root, sha = _item_template
        rel = f"{ITEM}/trail/gate.md"
        text = gate_file(sha).replace("```seal", "```Seal")
        notices = []
        assert gate_read(monkeypatch, root, text, notices) == [
            (rel, 0, chain.NO_RUN_BLOCK)
        ]
        line = text.splitlines().index("```Seal") + 1
        assert notices == [(rel, line, chain.FIELDS.NEAR.format(line="```Seal"))]


# --- the pull request's body (#1452) ------------------------------------------------

PR_BODY = load(
    str(ROOT / "skills" / "code-review" / "scripts" / "pr_body.py"),
    "pr_body_for_chain_tests",
)
# The seal mark both `seal pr-body` and the arm build from the plugin's
# manifest, the one beside `pr_body.py`.
MARK = PR_BODY._mark_line(PR_BODY.MANIFEST)[0]
CHANGED_LINE = "- The body is the records'."
SECOND_ITEM = "seal/threads/1791999998-another-work-item"
# #1453: the two language keys of `config.json` the body's first part is
# composed from; a case adds the mark key after them.
LANGUAGES = [
    ("Commit and pull request language", "English"),
    ("Record language", "English"),
]
MARK_ON = ("Pull request seal mark", "yes")


def composed_body(root, item=ITEM):
    """The body `seal pr-body` writes for ITEM in ROOT as it stands: the
    first part the language keys ask for, the heading, the mark where the
    item is sealed at HEAD, and the copy."""
    path = str(root / item)
    mark, _note = PR_BODY.seal_mark(path, str(root))
    name = os.path.basename(item)
    parts = PR_BODY.first_part(path, str(root))
    own = "".join(text for _name, text in parts)
    return own + PR_BODY.compose(name, PR_BODY.read_item(path), mark, parts=parts)


def payload(tmp_path, monkeypatch, body, draft=False):
    """The event payload of a pull request holding BODY, written where
    `GITHUB_EVENT_PATH` names it; no `body` field where BODY is `...`."""
    pr = {"draft": draft}
    if body is not ...:
        pr["body"] = body
    path = tmp_path / "event.json"
    path.write_text(json.dumps({"pull_request": pr}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(path))
    return path


def body_lines(out):
    """The lines of OUT the body arm printed."""
    return [ln for ln in out.splitlines() if "the pull request's body" in ln]


@pytest.fixture(scope="module")
def _bodied_template(tmp_path_factory):
    """A branch that went straight to the pull request with a `pr.md` and a
    changelog, in a shared root whose two language keys read `English` and
    whose `Pull request seal mark` key reads `yes`, sealed at HEAD, built
    once for the module. Returns `(root, early, late)`: the body `seal
    pr-body` wrote before the guarantee was committed, and the one it wrote
    after."""
    d = tmp_path_factory.mktemp("chain-bodied") / "b"
    born(d, "feature/g")
    work = {
        "seal/README.md": conftest.ROOT_MARKER + "\n",
        "seal/config.json": config_json(*LANGUAGES, MARK_ON),
        f"{ITEM}/routing.md": SEALED_ROUTING,
        f"{ITEM}/pr.md": "Closes #1.\n",
        f"{ITEM}/changelog.md": CHANGED_LINE + "\n",
        "f.txt": "two\n",
    }
    _base, audited = imported(
        d,
        ("main", None, "base", {"f.txt": "one\n"}),
        ("feature/g", ":1", "the work", work),
    )
    imported(
        d,
        (
            "feature/g",
            audited,
            "the broad run",
            {f"{ITEM}/trail/gate.md": gate_file(audited)},
        ),
        at=1700000010,
    )
    git(d, "reset", "-q", "--hard")
    early = composed_body(d)
    imported(
        d,
        (
            "feature/g",
            "feature/g",
            "the seal",
            {f"{ITEM}/guarantee.md": guarantee(audited, "sealed")},
        ),
        at=1700000020,
    )
    git(d, "reset", "-q", "--hard")
    return d, early, composed_body(d)


@pytest.fixture
def bodied(tmp_path, _bodied_template):
    """A copy of the module's bodied branch for one case, which the case may
    change."""
    template, early, late = _bodied_template
    d = tmp_path / "b"
    shutil.copytree(template, d)
    return d, early, late


def body_read(monkeypatch, root, text, why=None, items=(ITEM,), texts=None):
    """`(problems, notices)` the body arm gives for the body TEXT, or for
    none for WHY, over ITEMS in the branch at ROOT, against `main`; TEXTS,
    `{path: text or None}`, handed over through `read_record` (`reading`)."""
    reading(monkeypatch, texts or {})
    return chain.body(str(root), list(items), text, why, "main")


# #1559: a `gaps.md` whose `## Not verified` table passes GitHub's limit on
# a pull request body, so `seal pr-body` folds that section.
LONG_GAPS = (
    "# Closing memo\n\n## Not verified\n\n| Item | Who must answer |\n|---|---|\n"
    + "".join(f"| item {n} {'x' * 90} | the orchestrator |\n" for n in range(700))
    + "\n## Not done\n\nnothing\n"
)


@pytest.mark.rule("body-is-what-pr-body-composes")
class Test_body:
    def test_refuses_a_body_sent_before_the_seal_at_the_mark(
        self, _bodied_template, tmp_path, monkeypatch, capsys
    ):
        """S1. The body `seal pr-body` wrote before the guarantee was
        committed lacks the mark and the blank line under it, and a ready
        pull request fails on one refusal naming both at the body's line,
        on the work item's directory. Nothing else is refused. Seen red with
        the arm absent, where the check exited 0."""
        root, early, _late = _bodied_template
        assert MARK not in early
        payload(tmp_path, monkeypatch, early)
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 1, out
        assert body_lines(out) == [
            f"{ITEM}:0  the pull request's body, line 3: lacks ``, a fixed line, "
            f"then `{MARK}`, a fixed line"
        ], out

    def test_accepts_the_body_composed_after_the_seal(
        self, _bodied_template, monkeypatch
    ):
        """S2. The body written after the guarantee is the composition, and
        the arm names nothing."""
        root, _early, late = _bodied_template
        assert MARK in late
        assert body_read(monkeypatch, root, late) == ([], [])

    def test_accepts_the_body_at_a_merge_past_a_later_base_commit(
        self, bodied, tmp_path, monkeypatch, capsys
    ):
        """S2 at the checkout CI makes (round-1#1). The sealer writes the
        guarantee's base as a SHA, and CI checks out the pull request's
        merge commit, which reaches a commit another pull request landed on
        the base after the seal. The mark is read against the base the check
        runs against, as the guarantee arm reads it, so the body `seal
        pr-body` wrote at the branch head passes. Seen red with `body`
        calling `compared` with no base, where the composition held no mark
        and the body's mark run was refused."""
        root, _early, _late = bodied
        fork = git(root, "rev-parse", "main")
        audited = git(root, "rev-parse", "HEAD~2")
        sealed = guarantee(audited, "sealed").replace("against main", f"against {fork}")
        write(root, f"{ITEM}/guarantee.md", sealed)
        commit(root, "the seal, its base a SHA")
        written = composed_body(root)
        assert MARK in written
        git(root, "switch", "-q", "main")
        write(root, "g.txt", "another pull request\n")
        commit(root, "another pull request lands on the base")
        git(root, "switch", "-q", "--detach", "main")
        git(root, "merge", "-q", "--no-ff", "feature/g", "-m", "the CI merge")
        monkeypatch.setenv("GITHUB_HEAD_REF", "feature/g")
        payload(tmp_path, monkeypatch, written)
        code, out = check(root, capsys)
        assert code == 0, out
        assert body_lines(out) == [], out

    @pytest.mark.parametrize(
        "row, said",
        [
            ([], None),
            (
                [("Pull request seal mark", "Yes")],
                "`Pull request seal mark` reads `Yes`, not `yes`, so the key is not "
                "read and the body carries no seal mark",
            ),
        ],
        ids=["the key absent", "a key other than yes"],
    )
    def test_refuses_the_mark_where_the_row_gives_none(
        self, bodied, monkeypatch, row, said
    ):
        """S6. Where the row is absent or reads other than `yes`, the
        composition holds no mark, so a body carrying one is refused at the
        mark's run as lines the records do not give, and a row other than
        `yes` is named on a notice in `seal pr-body`'s words. The key is
        changed in the copy's working tree, which `compared` reads."""
        root, _early, _late = bodied
        write(root, "seal/config.json", config_json(*LANGUAGES, *row))
        plain = composed_body(root)
        heading = f"{PR_BODY.HEADING}\n\n"
        assert MARK not in plain
        marked = plain.replace(heading, f"{heading}{MARK}\n\n")
        refusal = (
            ITEM,
            0,
            f"the pull request's body, line 3: reads ``, then `{MARK}`, which "
            "the records do not give",
        )
        notice = [(ITEM, 0, f"the pull request's body: {said}")] if said else []
        assert body_read(monkeypatch, root, marked) == ([refusal], notice)
        assert body_read(monkeypatch, root, plain) == ([], notice)

    def test_accepts_a_folded_body_naming_the_fold(self, bodied, monkeypatch):
        """S7 of #1559. A body that is the composition `seal pr-body`
        folded, its `## Not verified` section past GitHub's limit, is
        refused nothing, and the arm names the fold's sentence as a notice;
        the same records composed with no fold are refused. The long
        `gaps.md` stands in the copy's working tree, which `compared` reads.
        Seen red with `compared` made to fold nothing, as at 0.38.2, where
        the folded body was refused at its folded section."""
        root, _early, _late = bodied
        write(root, f"{ITEM}/gaps.md", LONG_GAPS)
        late = composed_body(root)
        notice = (
            ITEM,
            0,
            "the pull request's body: folded `## Not verified` so the body "
            "stays within GitHub's 65,536 characters; each folded section "
            "names the record that holds it",
        )
        assert body_read(monkeypatch, root, late) == ([], [notice])
        monkeypatch.setattr(PR_BODY, "LIMIT", 10**9)
        whole = composed_body(root)
        assert whole != late
        problems, notices = body_read(monkeypatch, root, whole)
        assert notices == [notice], notices
        assert problems[0][:2] == (ITEM, 0), problems
        assert problems[0][2].startswith("the pull request's body, line "), problems

    def test_refuses_a_drifted_body_at_its_line(self, _bodied_template, monkeypatch):
        """S3. A line of the copy edited on GitHub is refused at the body's
        line, naming the record's line it should read. Seen red with the arm
        absent."""
        root, _early, late = _bodied_template
        drifted = late.replace(CHANGED_LINE, "- The body is anyone's.")
        assert body_read(monkeypatch, root, drifted) == (
            [
                (
                    ITEM,
                    0,
                    "the pull request's body, line 10: reads `- The body is "
                    f"anyone's.`; the records give `{CHANGED_LINE}` at "
                    "`changelog.md:1`",
                )
            ],
            [],
        )

    def test_refuses_a_null_body_as_an_empty_one(
        self, _bodied_template, tmp_path, monkeypatch
    ):
        """*Data & interfaces*: GitHub sends `null` for an empty body, which
        `pull_request_body` reads as empty and the comparison refuses for
        having no heading line. Seen red with the arm absent."""
        root, _early, _late = _bodied_template
        payload(tmp_path, monkeypatch, None)
        text, where = chain.pull_request_body()
        assert text == "", where
        [(path, line, why)], _notices = body_read(monkeypatch, root, text, where)
        assert (path, line) == (ITEM, 0), why
        assert why.startswith(
            f"the pull request's body: no line reads `{PR_BODY.HEADING}`"
        ), why

    def test_prints_the_refusal_on_a_draft_and_exits_0(
        self, _bodied_template, tmp_path, monkeypatch, capsys
    ):
        """S4. Seen red with the arm absent, where nothing was printed."""
        root, early, _late = _bodied_template
        payload(tmp_path, monkeypatch, early, draft=True)
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 0, out
        [line] = body_lines(out)
        assert line.startswith(f"{ITEM}:0  the pull request's body, line 3: lacks")

    @pytest.mark.parametrize(
        "body, why",
        [
            (..., "the event payload holds no `pull_request.body`"),
            (5, "the event payload's `body` is int, not text"),
        ],
        ids=["no body field", "a body that is no text"],
    )
    def test_names_the_body_as_not_read_where_the_payload_gives_none(
        self, _bodied_template, tmp_path, monkeypatch, body, why
    ):
        """S5, a payload with no body to read: `pull_request_body` gives no
        text and says why, and the arm names the body as not read on one
        notice and refuses nothing. Seen red with the arm absent."""
        root, _early, _late = _bodied_template
        payload(tmp_path, monkeypatch, body)
        text, said = chain.pull_request_body()
        assert (text, said) == (None, why)
        assert body_read(monkeypatch, root, text, said) == (
            [],
            [("", 0, f"not read: the pull request's body, since {why}")],
        )

    def test_names_the_body_as_not_read_with_no_payload(
        self, _bodied_template, monkeypatch
    ):
        """S5, a run outside CI, which `seal gate` under `--sealing` shares:
        `pull_request_body` reads no payload, the same under either flag.
        Seen red with the arm absent."""
        root, _early, _late = _bodied_template
        monkeypatch.delenv("GITHUB_EVENT_PATH", raising=False)
        text, said = chain.pull_request_body()
        assert body_read(monkeypatch, root, text, said) == (
            [],
            [
                (
                    "",
                    0,
                    "not read: the pull request's body, since there is no "
                    "pull-request event payload",
                )
            ],
        )

    def test_names_the_body_as_not_read_under_worktree(
        self, _bodied_template, tmp_path, monkeypatch, capsys
    ):
        """S5, `--worktree`: the working tree is not the tree the body is
        read against, so a body before the seal is named as not read and
        refuses nothing. Seen red with the arm absent."""
        root, early, _late = _bodied_template
        payload(tmp_path, monkeypatch, early)
        answered(monkeypatch)
        code, out = check(root, capsys, "--worktree")
        assert code == 0, out
        assert body_lines(out) == [
            "not read: the pull request's body, since the check reads the "
            "working tree (--worktree), and CI reads the body against HEAD"
        ], out

    def test_prints_a_difference_as_a_notice_under_sealing(
        self, _bodied_template, tmp_path, monkeypatch, capsys
    ):
        """S5, `--sealing`: the guarantee the mark stands on is not written
        yet, so a difference prints as a notice and fails nothing. Seen red
        with the arm absent."""
        root, early, _late = _bodied_template
        payload(tmp_path, monkeypatch, early)
        answered(monkeypatch)
        code, out = check(root, capsys, "--sealing")
        assert code == 0, out
        [line] = body_lines(out)
        assert line.startswith(f"{ITEM}:0  {chain.BODY_SEALING_SAYS}: ")
        assert line.endswith(f"then `{MARK}`, a fixed line"), line

    def test_names_the_body_as_not_read_for_two_work_items_with_pr_md(
        self, _bodied_template, monkeypatch
    ):
        """S8. One body is one work item's, so where the pull request
        carries two judged work items each holding a `pr.md`, the body is
        named as not read for each and refused for neither. Seen red with
        the arm absent."""
        root, early, _late = _bodied_template
        said = (
            "not read: the pull request's body, since the pull request carries "
            "more than one judged work item holding `pr.md`, and one body is "
            "one work item's"
        )
        assert body_read(
            monkeypatch,
            root,
            early,
            items=(SECOND_ITEM, ITEM),
            texts={f"{SECOND_ITEM}/pr.md": "Closes #2.\n"},
        ) == ([], [(SECOND_ITEM, 0, said), (ITEM, 0, said)])

    def test_names_the_body_as_not_read_for_two_work_items_without_pr_md(
        self, _bodied_template, monkeypatch
    ):
        """*Scope* item 1 (round-1#3): where several judged work items hold
        no `pr.md`, the body is named as not read for each, in a sentence
        that says none holds one. Seen red against the sentence for two
        holders of `pr.md`."""
        root, early, _late = _bodied_template
        said = (
            "not read: the pull request's body, since the pull request carries "
            "more than one judged work item and none holds `pr.md`, and one "
            "body is one work item's"
        )
        assert body_read(
            monkeypatch,
            root,
            early,
            items=(SECOND_ITEM, ITEM),
            texts={f"{ITEM}/pr.md": None},
        ) == ([], [(SECOND_ITEM, 0, said), (ITEM, 0, said)])

    def test_refuses_a_missing_pr_md_at_its_path(self, bodied, monkeypatch):
        """*Scope* item 1 (round-1#3): a cause `compared` places at a record,
        here a `pr.md` that is not there, is refused at that record's path
        under the work item, as every other arm refuses a record. The file
        leaves the copy's working tree, which `compared` reads, and git's
        HEAD. Seen red with the record's cause placed on the work item's
        directory."""
        root, _early, late = bodied
        (root / ITEM / "pr.md").unlink()
        problems, _notices = body_read(
            monkeypatch, root, late, texts={f"{ITEM}/pr.md": None}
        )
        assert (f"{ITEM}/pr.md", 0, PR_BODY.NO_OWN_PART) in problems, problems

    def test_refuses_a_quote_of_pr_md_its_source_does_not_hold(
        self, bodied, monkeypatch
    ):
        """A5 of #1612. A ready pull request whose work item's `pr.md`
        quotes words its `changelog.md` does not hold is refused at
        `pr.md`'s line, with the cause `seal pr-body` gives, since the arm
        reads the body through `compared`. Seen red against `first_part` as
        0.38.8 shipped it, where the arm named the body's first line
        and not the quote."""
        root, _early, late = bodied
        write(
            root,
            f"{ITEM}/pr.md",
            '- "The body is anyone\'s." (`changelog.md`, line 1)\nCloses #1.\n',
        )
        problems, _notices = body_read(monkeypatch, root, late)
        assert problems == [
            (
                f"{ITEM}/pr.md",
                1,
                "quotes words `changelog.md` does not hold, with runs of "
                "whitespace collapsed; the orchestrator rewrites the quote from "
                "the record as it stands",
            )
        ], problems

    def test_refuses_a_repository_without_a_language_row_at_its_config(
        self, bodied, monkeypatch
    ):
        """#1453, *Scope* item 3: `seal pr-body` composes no body for a
        repository whose `config.json` lacks a language key, so the arm,
        which reads the body through the same function, refuses at the
        root's `config.json`, as it refuses a record `compared` places at a
        path. Seen red with `compared` reading `pr.md` alone, where no line
        named the config."""
        root, _early, late = bodied
        write(root, "seal/config.json", config_json(LANGUAGES[0], MARK_ON))
        problems, _notices = body_read(monkeypatch, root, late)
        assert (
            "seal/config.json",
            0,
            "names no language in a `Record language` key; "
            "`templates/setup/config.md` *Record language* says what the key "
            "governs, and the orchestrator asks for it before the first edit",
        ) in problems, problems

    def test_reads_the_translation_as_the_bodys_first_lines(self, bodied, monkeypatch):
        """#1453, *Scope* item 3, the scenario *The pull request's arm passes
        the composed body*. Where the keys differ, the body `seal pr-body`
        composes opens with the work item's `pr.<lang>.md`, and the arm
        passes it; a body whose first part is `pr.md` alone is refused at its
        first line, naming the translation. Seen red with `compared` reading
        `pr.md` alone, where the composed body was refused at its first
        line. The lines are compared without their ends and the translation
        is taken out as the first line the body holds, because `write` ends
        each line with CRLF on Windows and `seal pr-body` copies the files'
        line ends as they stand."""
        root, _early, _late = bodied
        write(
            root,
            "seal/config.json",
            config_json((LANGUAGES[0][0], "Korean"), *LANGUAGES[1:], MARK_ON),
        )
        write(root, f"{ITEM}/pr.ko.md", "닫는다 #1.\n")
        composed = composed_body(root)
        lines = composed.splitlines(keepends=True)
        assert [line.rstrip("\r\n") for line in lines[:2]] == [
            "닫는다 #1.",
            "Closes #1.",
        ], composed
        assert body_read(monkeypatch, root, composed) == ([], [])
        assert body_read(monkeypatch, root, "".join(lines[1:])) == (
            [
                (
                    ITEM,
                    0,
                    "the pull request's body, line 1: lacks `닫는다 #1.`, which "
                    "pr.ko.md gives",
                )
            ],
            [],
        )


# --- the declaration for this branch, in local mode (#225) --------------------------

ITEM_ID = "1799000000-a-local-work-item"


def _build(d):
    d.mkdir(parents=True)
    git(d, "init", "-q", "-b", "base")
    (d / "f.py").write_text("x = 1\n", encoding="utf-8")
    git(d, "add", "-A")
    git(d, "-c", "user.email=e@example.com", "-c", "user.name=e", "commit", "-qm", "b")
    git(d, "switch", "-qc", "feature")


@pytest.fixture(scope="session")
def _repo_template(tmp_path_factory):
    """The module's fixture repository, built once; `tests/conftest.py#repo`
    copies it for each case."""
    d = tmp_path_factory.mktemp("local-mode-template") / "repo"
    _build(d)
    return d


def common_dir(where):
    """The clone's common git directory, absolute — asked of git, never
    spelled `.git`, which is a FILE in a linked worktree."""
    out = git(where, "rev-parse", "--git-common-dir")
    return os.path.normpath(os.path.join(str(where), out))


def local_item(repo, item=ITEM_ID, branch="feature"):
    """A work item under the LOCAL root, with a declaration naming `branch`."""
    d = os.path.join(mark_root(os.path.join(common_dir(repo), "seal")), "threads", item)
    os.makedirs(os.path.join(d, "trail", "rounds"), exist_ok=True)
    with open(os.path.join(d, "routing.md"), "w", encoding="utf-8") as f:
        f.write(
            f"# {item} — routing\n\n"
            "| Axis | Answer |\n|---|---|\n"
            "| Review | through the review chain |\n"
            "| Destination | open the pull request |\n"
            f"| Branch | {branch} |\n"
        )
    return d


def run_check(repo, capsys, monkeypatch):
    """(exit code, what it printed to both streams) of `main` over REPO's
    working tree against HEAD, run in the process. `main` sets `WORKTREE`,
    which goes back to its value when the case ends."""
    monkeypatch.setattr(chain, "WORKTREE", chain.WORKTREE)
    code = chain.main(["--worktree", "--baseline", "HEAD", "--root", str(repo)])
    out, err = capsys.readouterr()
    return code, out + err


ADD_THE_FILE = "Add seal/threads/<work-item>/routing.md to declare"
# The directory of the work items `main` passes, `root_name` resolving the
# `repo` fixture's tree to `seal`.
WORK = "seal/threads"
# A shared-mode declaration naming the `repo` fixture's branch.
DECLARES_FEATURE = ROUTING.format(
    review="through the review chain", planning="the session"
).replace("feature/x", "feature")


class Test_tracked_declarations:
    def test_accepts_the_declarations_at_head_read_in_one_process(
        self, repo, monkeypatch
    ):
        """#1603, design S6. The declarations HEAD carries are read by one
        `git cat-file --batch`, given the blob ids `ls-tree` lists, and by
        no `show`, and each reads as `read_record` reads it, the one with
        `\\r\\n` line ends among them. Where HEAD carries none, and under
        `WORKTREE`, where each is read from disk, no batch starts. Seen red
        against phase 1's `tracked_declarations`, which started one `show`
        per declaration."""
        root = str(repo)

        def started():
            found, asked = asks(
                monkeypatch,
                lambda: chain.tracked_declarations(root, routing_module, WORK),
            )
            return found, [argv[argv.index("-C") + 2] for argv, _given in asked]

        assert started() == ([], ["ls-tree"])
        git(repo, "config", "core.autocrlf", "false")
        paths = [f"{WORK}/179900000{n}-item-{n}/routing.md" for n in (1, 2, 3)]
        texts = [
            DECLARES_FEATURE.replace("| feature |", f"| feature/{n} |")
            for n in (1, 2, 3)
        ]
        for path, text in zip(paths, texts, strict=True):
            write(repo, path, text)
        (repo / paths[2]).write_bytes(texts[2].replace("\n", "\r\n").encode())
        commit_everything_as_e(repo, "three declarations")
        found, verbs = started()
        assert verbs == ["ls-tree", "cat-file"], verbs
        read = [(p, routing_module.parse(chain.read_record(root, p))) for p in paths]
        assert found == read, found
        assert [d["branch"] for _p, d in found] == [
            "feature/1",
            "feature/2",
            "feature/3",
        ], found
        (repo / paths[0]).write_text(
            texts[0].replace("feature/1", "feature/0"), encoding="utf-8"
        )
        monkeypatch.setattr(chain, "WORKTREE", True)
        found, verbs = started()
        assert verbs == ["ls-tree"], verbs
        assert [d["branch"] for _p, d in found] == [
            "feature/0",
            "feature/2",
            "feature/3",
        ], found

    def test_refuses_a_declaration_from_a_batch_that_exited_non_zero(
        self, repo, monkeypatch
    ):
        """#1603, design *Data & interfaces*. A `cat-file --batch` that
        exits non-zero reads as a `show` that exited non-zero read: an empty
        text, which `routing.parse` refuses, so no declaration is taken and
        nothing raises. Seen red against phase 1's `tracked_declarations`,
        which started no batch, and with the batch's exit code left
        unread."""
        write(repo, f"{WORK}/1799000001-an-item/routing.md", DECLARES_FEATURE)
        commit_everything_as_e(repo, "a declaration")
        real = subprocess.run

        def run(argv, *args, **kwargs):
            if "cat-file" in argv:
                return subprocess.CompletedProcess(argv, 128, b"", b"fatal: no\n")
            return real(argv, *args, **kwargs)

        monkeypatch.setattr(subprocess, "run", run)
        assert chain.tracked_declarations(str(repo), routing_module, WORK) == []


class Test_declared_for_this_branch:
    def test_refuses_a_local_declaration_and_says_it_is_local_mode(
        self, repo, capsys, monkeypatch
    ):
        """A local-mode repository is told the root it searched, not to write a
        file it already has."""
        local_item(repo)
        code, out = run_check(repo, capsys, monkeypatch)
        assert code == 0, out
        assert ADD_THE_FILE not in out, out
        assert "local mode" in out, out
        assert os.path.normpath(os.path.join(common_dir(repo), "seal")) in out, out
        assert "seal mode shared" in out, out

    def test_local_mode_says_the_check_judged_nothing(self, repo):
        """Naming the root does not turn an untracked declaration into a checked
        one: CI reads what git carries, and local mode commits nothing. At a
        local root each trailer is printed, not judged, so the why says the
        check judged nothing. `main` prints the why as its one notice
        (`test_refuses_a_local_declaration_and_says_it_is_local_mode`)."""
        local_item(repo)
        own, why = chain.declared_for_this_branch(str(repo), routing_module, WORK)
        assert own == [], own
        assert (
            "the review-chain check judged nothing: at a local root each "
            "commit's `Seal-Routing` trailer is printed, not judged"
        ) in why, why
        assert "judged the commit trailers" not in why, why
        assert "examined nothing" not in why, why
        assert "through the review chain" not in why, why

    def test_the_shared_sentence_says_what_it_searched_and_for_what(self, repo):
        """A shared-mode repository with no declaration is told to write one.
        The prefix and the branch are what make the sentence checkable, and
        the trailers are what the check judged where nothing declares the
        branch."""
        (repo / "seal" / "threads").mkdir(parents=True)
        own, why = chain.declared_for_this_branch(str(repo), routing_module, WORK)
        assert own == [], own
        assert ADD_THE_FILE in why and "local mode" not in why, why
        assert "under `seal/threads/`" in why, why
        assert "declares `feature`" in why, why
        assert "judged the commit trailers and nothing else" in why, why
        assert "examined nothing" not in why, why

    def test_a_repository_with_no_root_is_told_to_add_the_file(self, repo, monkeypatch):
        """With no root to name, the root's name is `seal`, and the file to
        write under it is the answer. The working tree is read, as `main`
        reads it under `--worktree`."""
        monkeypatch.setattr(chain, "WORKTREE", True)
        home = chain.root_name(routing_module, str(repo), None)
        assert home == "seal", home
        own, why = chain.declared_for_this_branch(
            str(repo), routing_module, f"{home}/threads"
        )
        assert own == [], own
        assert ADD_THE_FILE in why and "local mode" not in why, why

    @pytest.mark.parametrize(
        "decoy",
        [
            "specs/1799000002-a-team-item/routing.md",
            "seal/threads/1799000001-an-item/notes.md",
        ],
        ids=["a-routing-md-outside-the-work-items", "another-file-of-a-work-item"],
    )
    def test_accepts_the_one_routing_md_under_the_work_items_beside_a_decoy(
        self, repo, decoy
    ):
        """Guards c3 and c4 of #1017: only a `routing.md` under `seal/threads/`
        is a declaration. A team's own `specs/` holding one, or a work item's
        other file holding a declaration's text, leaves the branch one
        declaration, which is taken."""
        declared = "seal/threads/1799000001-an-item/routing.md"
        write(repo, declared, DECLARES_FEATURE)
        write(repo, decoy, DECLARES_FEATURE)
        commit_everything_as_e(repo, "a declaration and a decoy")
        assert chain.declared_for_this_branch(str(repo), routing_module, WORK) == (
            [declared],
            "",
        )

    def test_refuses_two_committed_declarations_naming_the_branch(self, repo):
        """Guards g17 of #1017: two committed declarations naming one branch
        are not one answer, so neither is taken."""
        for n in (1, 2):
            write(
                repo, f"seal/threads/179900000{n}-item-{n}/routing.md", DECLARES_FEATURE
            )
        commit_everything_as_e(repo, "two declarations")
        own, why = chain.declared_for_this_branch(str(repo), routing_module, WORK)
        assert own == [], own
        assert why.startswith("2 committed declarations name `feature`"), why

    def test_refuses_a_detached_head_with_no_head_ref_as_no_branch(self, repo):
        """Guards g18 of #1017: a detached HEAD with no `GITHUB_HEAD_REF`
        names no branch, so no declaration is matched, even at a commit that
        declares the branch it left, and the why says the branch could not be
        read rather than that nothing declared it."""
        write(repo, "seal/threads/1799000001-an-item/routing.md", DECLARES_FEATURE)
        commit_everything_as_e(repo, "a declaration")
        git(repo, "switch", "-q", "--detach")
        own, why = chain.declared_for_this_branch(str(repo), routing_module, WORK)
        assert own == [], own
        assert why.startswith("the branch could not be read"), why


# --- the routing trailer at the pull request -------------------------------------------

ROUTED = "1792000000-a-routed-item"


def commit_saying(d, *paragraphs, env=None):
    """Every change in D committed with PARAGRAPHS as its message, an empty
    commit where nothing changed; the new HEAD."""
    git(d, "add", "-A")
    message = [a for p in paragraphs for a in ("-m", p)]
    subprocess.run(
        ["git", "-C", str(d), "commit", "-q", "--allow-empty", *message],
        check=True,
        capture_output=True,
        env={**os.environ, **(env or {})},
    )
    return git(d, "rev-parse", "HEAD")


@pytest.fixture(scope="module")
def _undeclared_template(tmp_path_factory):
    """`feature/t`, which no declaration names, checked out from a `main`
    holding one file, built once for the module."""
    d = tmp_path_factory.mktemp("chain-undeclared") / "t"
    init(d)
    write(d, "f.txt", "one\n")
    commit(d, "base")
    git(d, "switch", "-q", "-c", "feature/t")
    return d


@pytest.fixture
def undeclared(tmp_path, monkeypatch, _undeclared_template):
    """A copy of the module's `feature/t` for one case, judged as a ready
    pull request."""
    d = tmp_path / "t"
    shutil.copytree(_undeclared_template, d)
    event(tmp_path, monkeypatch, False)
    return d


@pytest.mark.rule("routing-trailer-at-the-pull-request")
class Test_routing_trailers:
    def test_refuses_a_commit_naming_a_work_item_no_declaration_names(
        self, undeclared, tmp_path, monkeypatch, capsys
    ):
        """S10: a commit whose `Seal-Routing` trailer names a work item no
        declaration names fails a ready pull request, naming the commit and
        the item; one reading `no work item` is printed as a notice; one with
        no such trailer is not named. A draft prints the same lines and
        passes."""
        root = undeclared
        write(root, "a.txt", "a\n")
        named = commit_saying(root, "feat: a", f"Seal-Routing: {ROUTED}")
        write(root, "b.txt", "b\n")
        none = commit_saying(root, "chore: b", "Seal-Routing: no work item")
        write(root, "c.txt", "c\n")
        bare = commit_saying(root, "chore: c")
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 1, out
        lines = out.splitlines()
        assert chain.UNDECLARED_TRAILER.format(sha=named[:8], item=ROUTED) in lines
        assert chain.NO_WORK_ITEM_TRAILER.format(sha=none[:8]) in lines
        assert bare[:8] not in out, out
        assert chain.UNDECLARED_TRAILER.format(sha="x", item="y") == (
            "commit x carries `Seal-Routing: y`, and no routing declaration "
            "this pull request judges names that work item: commit its "
            "`routing.md`, naming this branch, or correct the trailer"
        )
        assert chain.NO_WORK_ITEM_TRAILER.format(sha="x") == (
            "commit x carries `Seal-Routing: no work item`: its session "
            "recorded that the change belongs to no work item, and nothing "
            "here checks it further"
        )
        event(tmp_path, monkeypatch, True)
        code, out = check(root, capsys)
        assert code == 0, out
        assert chain.UNDECLARED_TRAILER.format(sha=named[:8], item=ROUTED) in out

    def test_does_not_read_the_trailer_key_a_commit_before_0_23_0_carries(
        self, undeclared
    ):
        """S1 of #1142: the key a commit made before the rename carries,
        `SpecSeal-Routing:`, is read as any other trailer key is: not judged.
        Neither the work item no declaration names nor `no work item` is
        read as a routing trailer, so neither reaches the arm that judges
        them."""
        root = undeclared
        write(root, "a.txt", "a\n")
        commit_saying(root, "feat: a", f"SpecSeal-Routing: {ROUTED}")
        write(root, "b.txt", "b\n")
        commit_saying(root, "chore: b", "SpecSeal-Routing: no work item")
        assert chain.routing_trailers(str(root), "main") == []

    def test_accepts_a_commit_naming_the_work_item_its_declaration_names(
        self, branch, ready, capsys, monkeypatch
    ):
        root, _code = branch
        commit_saying(root, "chore: e", "Seal-Routing: 1791999999-a-work-item")
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 0, out
        assert "Seal-Routing" not in out, out

    def test_a_teammates_commit_is_never_judged(self, undeclared):
        """S11: the harness's co-author trailer, which any Claude Code
        session carries, is not the session's routing trailer."""
        root = undeclared
        write(root, "a.txt", "a\n")
        commit_saying(
            root,
            "feat: a teammate's change",
            "Co-Authored-By: Claude <noreply@example.com>",
        )
        assert chain.routing_trailers(str(root), "main") == []

    def test_a_merge_and_a_squash_github_committed_are_not_its_own(self, undeclared):
        """A merge's message is not a commit of the pull request, and a squash
        GitHub committed was judged at the pull request it closed: its
        committer is not its author, one case of the rule below."""
        root = undeclared
        git(root, "switch", "-q", "-c", "side", "main")
        write(root, "s.txt", "s\n")
        commit(root, "side")
        git(root, "switch", "-q", "feature/t")
        git(
            root,
            "merge",
            "-q",
            "--no-ff",
            "-m",
            "merge side",
            "-m",
            f"Seal-Routing: {ROUTED}",
            "side",
        )
        write(root, "q.txt", "q\n")
        commit_saying(
            root, "feat: elsewhere (#7)", f"Seal-Routing: {ROUTED}", env=GITHUB
        )
        assert chain.routing_trailers(str(root), "main") == []

    def test_a_work_item_trailer_at_a_local_root_is_printed_not_refused(
        self, undeclared, capsys
    ):
        """Round 1 of #1027, finding 1: in local mode no declaration is ever
        committed, so a trailer naming a work item could match none. A ready
        pull request prints it and passes."""
        root = undeclared
        os.makedirs(
            os.path.join(
                mark_root(os.path.join(root, ".git", "seal")), "threads", ROUTED
            )
        )
        write(root, "a.txt", "a\n")
        named = commit_saying(root, "feat: a", f"Seal-Routing: {ROUTED}")
        code, out = check(root, capsys)
        assert code == 0, out
        assert chain.LOCAL_TRAILER.format(sha=named[:8], item=ROUTED) in out, out
        assert chain.LOCAL_TRAILER.format(sha="x", item="y") == (
            "commit x carries `Seal-Routing: y` in a repository whose root "
            "is local, where no routing declaration is committed for it to "
            "name: printed, not judged"
        )
        assert "commit its `routing.md`" not in out, out

    def test_a_commit_its_author_did_not_commit_is_not_judged(self, undeclared):
        """Round 1 of #1027, finding 2: a person's `cherry-pick -x` of a
        session's commit is the person's commit, carrying a trailer the
        person did not write. Its committer is not its author, which is how
        git records every commit somebody else carried, GitHub's squash
        among them; a session's own commit is committed by its author."""
        root = undeclared
        git(root, "switch", "-q", "-c", "session", "main")
        write(root, "s.txt", "s\n")
        picked = commit_saying(root, "feat: s", f"Seal-Routing: {ROUTED}")
        git(root, "switch", "-q", "feature/t")
        subprocess.run(
            ["git", "-C", str(root), "cherry-pick", "-x", picked],
            check=True,
            capture_output=True,
            env={**os.environ, "GIT_COMMITTER_EMAIL": "person@example.com"},
        )
        assert chain.routing_trailers(str(root), "main") == []

    def test_refuses_to_run_where_the_commits_cannot_be_read(
        self, undeclared, capsys, monkeypatch
    ):
        monkeypatch.setattr(chain, "routing_trailers", lambda root, base: None)
        code = chain.main(["--baseline", "main", "--root", str(undeclared)])
        err = capsys.readouterr().err
        assert code == 2, err
        assert "cannot read the commits after main" in err, err


# --- main: the arms over a pull request ----------------------------------------------


def unread_lines(out):
    """The `not read` lines of OUT, the body arm's left out: the `ready` and
    `draft` payloads hold no body, which that arm names on a line of its
    own (`Test_body`)."""
    return [
        ln
        for ln in out.splitlines()
        if "not read" in ln and "the pull request's body" not in ln
    ]


DECLARED = "agentic-seal/threads/1794200001-a-declared-item"


# A declaration naming `feature`, straight to the pull request, so the
# check's guarantee arm names its missing `guarantee.md` once it is judged.
DECLARATION = (
    "| Axis | Answer |\n|---|---|\n| Review | straight to the PR |\n"
    "| Destination | open the pull request |\n| Planning | the session |\n"
    "| Branch | feature |\n"
)


NO_GUARANTEE = f"{DECLARED}/guarantee.md:0  git carries no guarantee file"
# The package's own `seal/README.md`, which opens with no marker, and a
# root's, which does.
PACKAGE_README = conftest.PACKAGE["seal/README.md"]
MARKED = conftest.ROOT_MARKER + "\n"


@pytest.fixture
def declared(shared, tmp_path, monkeypatch):
    """SHARED with DECLARATION committed on `main` under `agentic-seal/`,
    and `feature` checked out from it, which the check reads as a ready pull
    request."""
    write(shared, f"{DECLARED}/routing.md", DECLARATION)
    commit_everything_as_e(shared, "the declaration")
    git_out(shared, "switch", "-qc", "feature")
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": False}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    return shared


def checked(capsys, repo):
    """(exit code, stdout) of `chain_check.py` run on REPO against `main`."""
    code = chain.main(["--baseline", "main", "--root", str(repo)])
    return code, capsys.readouterr().out


ROUNDS = f"{ITEM}/trail/rounds"
ROUND_1 = f"{ROUNDS}/round-1.md"
ROUND_2 = f"{ROUNDS}/round-2.md"


def records_read(monkeypatch, root, texts=None, listed=None):
    """What the records arm, the one `main` hands a work item declared
    through the review chain, gives for ITEM over ROOT against `main`. TEXTS,
    `{path: text or None}`, reach it through `read_record` (`reading`).
    Where LISTED is given, it is the round records the arm reads, lowest
    first, in place of what `trail/rounds/` holds at HEAD; every commit the
    arm asks about is git's, but where the case answered `follows`
    (`answered`)."""
    reading(monkeypatch, texts or {})
    if listed is not None:
        monkeypatch.setattr(chain, "round_records", lambda routing, r, i: list(listed))
    return chain.records(routing_module, str(root), ITEM, f"{ITEM}/routing.md", "main")


@pytest.mark.rule("routing-read-first")
class Test_main:
    @pytest.mark.rule("old-table-shape-refused")
    def test_accepts_a_reviewed_branch_on_a_ready_pull_request(
        self, _branch_template, ready, capsys
    ):
        """S11: the merged item's old-shape record, a finding open in it, is
        never opened; the check judges only what this pull request carries."""
        root, _code = _branch_template
        code, out = check(root, capsys)
        assert code == 0, out
        assert MERGED_ITEM not in out

    @pytest.mark.parametrize("world", ["branch", "bodied"])
    def test_asks_git_each_read_once_in_a_run(
        self, request, tmp_path, capsys, monkeypatch, world
    ):
        """#1603, design S1. On a ready pull request, every reader real,
        a run starts no git command twice with the same input: over
        `branch`, whose round records the records arm and `unread` each
        read, and over `bodied` with the body `seal pr-body` wrote after
        the seal in its payload, whose guarantee's target the guarantee arm
        and the body arm each ask `follows` of. Seen red against
        `chain_check.py` before #1603, where the round records' `show` and
        the guarantee's `follows` reads repeat."""
        if world == "branch":
            root, _code = request.getfixturevalue("_branch_template")
            event(tmp_path, monkeypatch, False)
        else:
            root, _early, late = request.getfixturevalue("_bodied_template")
            payload(tmp_path, monkeypatch, late)
        (code, out), asked = asks(monkeypatch, lambda: check(root, capsys))
        assert code == 0, out
        assert repeated(asked) == [], repeated(asked)

    @pytest.mark.parametrize(
        "words",
        [
            ("rev-parse", "--show-toplevel"),
            ("rev-parse", "--verify"),
            ("diff", "--raw"),
            ("merge-base", "main", "HEAD"),
            ("ls-tree", "-r", "-z", "HEAD"),
            ("cat-file", "--batch"),
            ("show",),
            ("log",),
            ("merge-base", "--is-ancestor"),
            ("diff-tree",),
            (f"HEAD:{ITEM}/frame/design.md",),
        ],
        ids=[
            "toplevel",
            "resolves",
            "changed",
            "merge_base",
            "declared",
            "declarations",
            "read_record",
            "trailers",
            "is_ancestor",
            "touched",
            "rule_changes_read",
        ],
    )
    def test_refuses_a_git_that_did_not_answer_in_one_line(
        self, _branch_template, ready, capsys, monkeypatch, words
    ):
        """S8 of #1573: a git read past `lib/gitcmd.py#TIMEOUT` ends
        `chain-check` with one line on stderr, `chain-check: ` and the
        runner's line naming the command and the bound, at exit 2, the
        check's could-not-run code, with no traceback. The repository's own
        top is one of the reads, so a git that did not answer is not read as
        no repository, and so is the rule-changes reader's read of a design,
        so it is not named as a reader that would not load. Seen red against
        `chain_check.py` before #1573, where the timeout was raised out of
        `main`."""
        root, _code = _branch_template
        asked = unanswered(monkeypatch, *words)
        code = chain.main(["--baseline", "main", "--root", str(root)])
        err = capsys.readouterr().err
        assert len(asked) == 1, asked
        assert code == 2, err
        assert err == f"chain-check: {past_the_bound(asked[0])}\n", err

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_an_open_finding_on_a_ready_pull_request(
        self, _branch_template, draft, capsys, monkeypatch
    ):
        """#1198's scenario *An open finding* (S3, T27): a finding with no
        close block is open, refused at its heading with the line the fix
        pass appends, and a draft prints the same line and passes. A
        finding's `severity:` decides nothing. The draft is `main` reading
        the record, which shows that `main` hands the records arm its round
        records and prints what it refuses."""
        root, code_sha = _branch_template
        answered(monkeypatch)
        text = record(code_sha, [finding(1, "open")])
        heading = "### 1. the parser drops a row"
        said = (
            ROUND_1,
            line_at(text, heading),
            f"{heading} {chain.DASH} {chain.OPEN_SAYS}",
        )
        assert said in records_read(monkeypatch, root, {ROUND_1: text})
        assert chain.OPEN_SAYS == (
            "no close block, so the finding is open: the fix pass appends one "
            "after its paste-ready fix, opening with `verdict:` and reading "
            "`fixed <commit>`, `rejected` or `deferred <home>`"
        )
        code, out = check(root, capsys)
        assert code == 0
        assert f"{said[0]}:{said[1]}  {said[2]}" in out.splitlines(), out
        rejected = {ROUND_1: record(code_sha, [finding(1, "rejected")])}
        assert records_read(monkeypatch, root, rejected) == []

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_fixed_commit_head_does_not_descend_from(
        self, branch, monkeypatch
    ):
        """S3 (T28): one this repository cannot resolve, and one on another
        branch, are refused by the finding's line and heading; the fixture's
        own code commit is not."""
        root, code_sha = branch
        git(root, "switch", "-q", "main")
        write(root, "g.txt", "elsewhere\n")
        off = commit(root, "a commit the branch never had")
        git(root, "switch", "-q", "feature/x")
        sections = [
            finding(1, "fixed 0000000"),
            finding(2, f"fixed {off[:8]}"),
            finding(3, f"fixed {code_sha[:8]}"),
        ]
        found = records_read(monkeypatch, root, {ROUND_1: record(code_sha, sections)})
        named = [
            why
            for rel, _line, why in found
            if rel == ROUND_1 and "does not descend" in why
        ]
        assert len(named) == 2, found
        assert "### 1." in named[0] and "`0000000`" in named[0]
        assert "### 2." in named[1] and f"`{off[:8]}`" in named[1]
        # The refusal `chain_check.py` prints for each such fix, which the
        # orchestrator reads at the pull request's check.
        assert all("HEAD does not descend from" in why for why in named), named

    @pytest.mark.rule("round-record-read-by-label")
    @pytest.mark.rule("fix-pass-two-lines")
    @pytest.mark.rule("location-touched-by-fix")
    def test_refuses_a_fixed_commit_that_touches_nothing_of_the_finding(
        self, branch, monkeypatch
    ):
        """S22 (T34): a commit touching another path is refused naming the
        finding, the commit and what it touched, and the `location:` line of
        the close block that names where a fix went; one touching one of two
        named paths, a file under a named directory, or a path the close
        block names passes, and so does the root commit. A path sharing a
        named directory's prefix is not under it."""
        root, code_sha = branch
        base = git(root, "rev-list", "--max-parents=0", "HEAD")
        made = {}
        for name, path in (
            ("g", "g.txt"),
            ("dir", "docs/x/y.md"),
            ("h", "h.txt"),
            ("near", "docs/xy.md"),
        ):
            write(root, path, f"{name}\n")
            made[name] = commit(root, f"touch {path}")[:8]
        sections = [
            finding(1, f"fixed {made['g']}"),
            finding(2, f"fixed {made['g']}", location="`f.txt:1`, `g.txt:3`"),
            finding(3, f"fixed {made['dir']}", location="`docs/x/`"),
            finding(4, f"fixed {made['dir']}", location="`docs/x`"),
            finding(5, "open", location="`f.txt:1`")
            + "\n"
            + close(f"fixed {made['h']}", location="`h.txt`"),
            finding(6, f"fixed {base[:8]}", location="`f.txt`"),
            finding(7, f"fixed {made['near']}", location="`docs/x`"),
        ]
        verifying = record(
            made["near"],
            confirmations="".join(confirm(f"round-1#{n}") for n in range(1, 8)),
            n=2,
        )
        found = records_read(
            monkeypatch,
            root,
            {ROUND_1: record(code_sha, sections), ROUND_2: verifying},
        )
        named = [why for rel, _line, why in found if rel == ROUND_1]
        assert len(named) == 2, found
        assert "### 1." in named[0] and f"`{made['g']}`" in named[0], named
        assert "`g.txt`" in named[0] and "`f.txt`" in named[0], named
        assert "### 7." in named[1] and "`docs/xy.md`" in named[1], named
        assert all("touches no path" in ln for ln in named), named
        assert all(
            "names that path on a `location:` line of its close block" in ln
            for ln in named
        ), named

    @pytest.mark.rule("run-ends-with-verifying-round")
    @pytest.mark.rule("last-record-at-head")
    def test_refuses_a_last_records_fixed_finding_owing_a_verifying_round(
        self, _branch_template, monkeypatch
    ):
        """S23 (T37): a `fixed` or `rejected` finding in the last record is
        refused as *a verifying round is owed*, and a last record of
        `deferred` findings passes. The last record is round 1, the only
        one the arm reads."""
        root, code_sha = _branch_template
        answered(monkeypatch)
        found = records_read(monkeypatch, root, listed=[ROUND_1])
        line = next(why for rel, _line, why in found if rel == ROUND_1)
        assert "### 1." in line and chain.VERIFYING_ROUND in line, line
        deferred = {ROUND_1: record(code_sha, [finding(1, "deferred #9")])}
        assert records_read(monkeypatch, root, deferred, listed=[ROUND_1]) == []

    @pytest.mark.rule("run-ends-with-verifying-round")
    @pytest.mark.rule("last-record-at-head")
    def test_passes_a_last_records_fixed_finding_that_touched_only_its_records(
        self, branch, monkeypatch
    ):
        """S4 of #1148: a `fixed <commit>` of the last record located in the
        work item's own records alone, whose commit touched them alone, owes
        no verifying round; the sealer, which reads every record at HEAD, is
        its reader."""
        root, code_sha = branch
        write(root, f"{ITEM}/gaps.md", "# overview\n\nthe row, corrected\n")
        fix = commit(root, "a fix to the records alone")
        located = f"`{ITEM}/gaps.md`"
        last = record(code_sha, [finding(1, f"fixed {fix[:8]}", location=located)])
        assert records_read(monkeypatch, root, {ROUND_1: last}, [ROUND_1]) == []

    @pytest.mark.rule("run-ends-with-verifying-round")
    def test_passes_a_last_records_regression_fixed_in_its_records_alone(
        self, branch, monkeypatch
    ):
        """#1615, *Scope* item 8: a regression of the last record, located
        in the work item's own records alone and `fixed` by a commit that
        touched them alone, owes no verifying round either: the
        `regression:` line changes nothing of what the arm gives the
        sealer."""
        root, code_sha = branch
        write(root, f"{ITEM}/frame/plan.md", "# plan\n\nthe row, corrected\n")
        fix = commit(root, "a regression's fix to the records alone")
        located = f"`{ITEM}/frame/plan.md`"
        first = record(code_sha, [finding(1, f"fixed {code_sha[:8]}")])
        last = record(
            code_sha,
            [finding(1, f"fixed {fix[:8]}", location=located, regression="round-1#1")],
            n=2,
        )
        texts = {ROUND_1: first, ROUND_2: last}
        assert records_read(monkeypatch, root, texts, [ROUND_1, ROUND_2]) == []

    @pytest.mark.rule("run-ends-with-verifying-round")
    @pytest.mark.rule("last-record-at-head")
    def test_refuses_a_last_records_fixed_finding_that_also_touched_code(
        self, branch, monkeypatch
    ):
        """S4 of #1148: a `fixed <commit>` of the last record whose commit
        touched the records and a path outside them still owes the round,
        refused at the finding's line."""
        root, _code = branch
        write(root, f"{ITEM}/gaps.md", "# overview\n\nthe row, corrected\n")
        write(root, "f.txt", "three\n")
        fix = commit(root, "a fix to the records and the code")
        located = f"`f.txt:1`, `{ITEM}/gaps.md`"
        last = record(fix, [finding(1, f"fixed {fix[:8]}", location=located)])
        found = records_read(monkeypatch, root, {ROUND_1: last}, [ROUND_1])
        line = next(why for rel, _n, why in found if rel == ROUND_1 and "### 1." in why)
        assert chain.VERIFYING_ROUND in line, line

    @pytest.mark.rule("run-ends-with-verifying-round")
    @pytest.mark.rule("last-record-at-head")
    def test_refuses_a_last_records_code_finding_fixed_in_its_records_alone(
        self, branch, monkeypatch
    ):
        """S4 of #1148: a finding that names a path outside the records owes
        the round, even where its `fixed` commit touched only the records,
        since no round would read its code half."""
        root, code_sha = branch
        write(root, f"{ITEM}/gaps.md", "# overview\n\nthe row, corrected\n")
        fix = commit(root, "the record half alone")
        located = f"`f.txt:1`, `{ITEM}/gaps.md`"
        last = record(code_sha, [finding(1, f"fixed {fix[:8]}", location=located)])
        found = records_read(monkeypatch, root, {ROUND_1: last}, [ROUND_1])
        line = next(why for rel, _n, why in found if rel == ROUND_1 and "### 1." in why)
        assert chain.VERIFYING_ROUND in line, line

    @pytest.mark.rule("last-record-at-head")
    def test_refuses_a_code_commit_after_the_last_record(self, branch, monkeypatch):
        """S4 (T12): a record commit after the last record passes; a code
        commit after it fails naming the commit and the verifying round."""
        root, _code = branch
        write(root, f"{ITEM}/gaps.md", "# overview\n")
        commit(root, "a record commit")
        assert records_read(monkeypatch, root) == []
        write(root, "f.txt", "three\n")
        later = commit(root, "a fix after the last round")
        said = [why for _rel, _line, why in records_read(monkeypatch, root)]
        # The refusal `chain_check.py` prints, which tells the orchestrator a
        # verifying round is owed.
        assert any(
            later[:8] in why and "a verifying round is owed" in why for why in said
        )

    def test_refuses_a_chain_with_no_record_and_prints_it_on_a_draft(
        self, branch, ready, capsys, monkeypatch
    ):
        root, _code = branch
        git(root, "rm", "-rq", f"{ITEM}/trail/rounds")
        commit(root, "no record")
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 1 and "holds no `round-N.md`" in out
        ready.write_text(json.dumps({"pull_request": {"draft": True}}), "utf-8")
        code, out = check(root, capsys)
        assert code == 0 and "holds no `round-N.md`" in out

    def test_names_a_line_it_did_not_read_as_a_notice_and_keeps_the_exit(
        self, _branch_template, ready, capsys, monkeypatch
    ):
        """#1198's scenario *A near opener*: a fence opened by three
        backticks and `Seal` is printed `path:line  not read: <why>`, and in
        CI as a notice annotation, never an error, and the exit code is the
        one the record's blocks give: 0 where the near fence stands in a
        finding's prose, 1 where it was the finding's only block, refused at
        the heading. The first two are `main` reading the record; the third
        is the two arms that read it, the records arm and `unread`."""
        root, code_sha = _branch_template
        near = FENCE + "Seal"
        text = record(code_sha, [finding(1, f"fixed {code_sha[:8]}")]).replace(
            "\nWhy it matters.", f"\n{near}\nverdict: fixed\n{FENCE}\n\nWhy it matters."
        )
        answered(monkeypatch)
        reading(monkeypatch, {ROUND_1: text})
        number = line_at(text, near)
        said = chain.FIELDS.NEAR.format(line=near)
        assert said.startswith("not read: "), said
        code, out = check(root, capsys)
        assert code == 0, out
        assert unread_lines(out) == [f"{ROUND_1}:{number}  {said}"], out
        monkeypatch.setenv("GITHUB_ACTIONS", "true")
        code, out = check(root, capsys)
        assert code == 0, out
        assert unread_lines(out) == [
            f"::notice file={ROUND_1},line={number}::{said}"
        ], out
        monkeypatch.delenv("GITHUB_ACTIONS")
        only = record(code_sha, [finding(1, f"fixed {code_sha[:8]}")]).replace(
            f"{FENCE}seal\nseverity:", f"{near}\nseverity:"
        )
        heading = "### 1. the parser drops a row"
        assert (
            ROUND_1,
            line_at(only, heading),
            f"{heading} {chain.DASH} {chain.NO_FINDING_BLOCK}",
        ) in records_read(monkeypatch, root, {ROUND_1: only})
        assert chain.unread(routing_module, str(root), ITEM, True) == [
            (ROUND_1, line_at(only, near), said)
        ]

    def test_names_no_line_inside_a_fence(self, _branch_template, monkeypatch):
        """A paste-ready fix block quoting a near opener and a `verdict:`
        line is named by no `not read:` line, and the records arm refuses
        nothing of the clean record: a fence inside another fence is that
        fence's."""
        root, code_sha = _branch_template
        answered(monkeypatch)
        text = record(code_sha, [finding(1, f"fixed {code_sha[:8]}")])
        quoted = f"{FENCE}`markdown\n{FENCE}Seal\nverdict: open\n{FENCE}\n{FENCE}`"
        texts = {ROUND_1: text.replace(f"{FENCE}python\nx = 1\n{FENCE}", quoted)}
        assert records_read(monkeypatch, root, texts) == []
        assert chain.unread(routing_module, str(root), ITEM, True) == []

    def test_names_a_record_under_another_name_and_keeps_the_exit(
        self, branch, monkeypatch
    ):
        """The second scenario of #1167, #1121's R11: `Round-2.md` beside a
        clean `round-1.md` is named on one line as a file the check did not
        read, and the records arm reads the clean record alone and refuses
        nothing. Seen red against the reader that kept the files
        `round_number` matches and printed nothing of the rest."""
        root, code_sha = branch
        git(root, "rm", "-q", ROUND_2)
        clean = record(code_sha, [finding(1, "deferred #9")])
        write(root, ROUND_1, clean)
        write(root, f"{ROUNDS}/Round-2.md", clean)
        commit(root, "one clean record, and a copy under another name")
        assert records_read(monkeypatch, root) == []
        said = chain.UNREAD_FILE.format(name="Round-2.md")
        assert chain.unread(routing_module, str(root), ITEM, True) == [
            (f"{ROUNDS}/Round-2.md", 0, said)
        ]

    @pytest.mark.rule("old-table-shape-refused")
    def test_refuses_an_old_shape_record_and_an_unclosed_fence(
        self, _branch_template, monkeypatch
    ):
        """S11 and #1198's scenario *A record from before the change*: a
        record of an older shape under the declared item, the table's and
        the labelled lines', holds no round block and is refused with one
        line naming the template; a fence the proofer never closed hides the
        open finding below it and is named at its opener."""
        root, code_sha = _branch_template
        answered(monkeypatch)
        for old in (OLD_RECORD.replace("0000000", code_sha), LABELLED):
            found = records_read(monkeypatch, root, {ROUND_1: old})
            assert [p for p in found if p[0] == ROUND_1] == [
                (ROUND_1, 0, chain.NO_ROUND_BLOCK)
            ], found
        text = record(
            code_sha,
            [finding(1, "rejected") + "\n~~~python\n", finding(2, "open")],
        )
        found = records_read(monkeypatch, root, {ROUND_1: text})
        opener = text.splitlines().index("~~~python")
        assert (ROUND_1, opener + 1) in [(rel, n) for rel, n, _why in found], found

    def test_refuses_a_broad_gate_file_naming_another_commit(
        self, _branch_template, ready, capsys, monkeypatch
    ):
        """S5 (T15): the newest run must be HEAD or have only records after
        it; a stale run fails naming the file, and `--sealing` prints it.
        `main` reads the record, which shows that it hands the broad gate
        arm its work item and reads its refusal by `--sealing`."""
        root, _code = _branch_template
        rel = f"{ITEM}/trail/gate.md"
        answered(monkeypatch, real=("follows",))
        reading(monkeypatch, {rel: gate_file("1" * 40)})
        code, out = check(root, capsys)
        assert code == 1
        assert any(ln.startswith(f"{rel}:") for ln in out.splitlines())
        code, out = check(root, capsys, "--sealing")
        assert code == 0 and rel in out

    @pytest.mark.rule("two-review-answers")
    def test_refuses_a_straight_to_the_pr_item_without_the_sealers_two_files(
        self, _branch_template, ready, capsys, monkeypatch
    ):
        """`main` reading a declaration straight to the pull request judges
        the sealer's two files and no round record: with the two files at
        HEAD it passes, and with neither it fails naming both."""
        root, _code = _branch_template
        direct = ROUTING.format(review="straight to the PR", planning="the session")
        answered(monkeypatch)
        reading(monkeypatch, {f"{ITEM}/routing.md": direct})
        code, out = check(root, capsys)
        assert code == 0, out
        reading(
            monkeypatch, {f"{ITEM}/trail/gate.md": None, f"{ITEM}/guarantee.md": None}
        )
        code, out = check(root, capsys)
        assert code == 1 and "trail/gate.md" in out and "guarantee.md" in out

    def test_refuses_an_unreadable_declaration_and_accepts_none(
        self, _branch_template, branch, ready, capsys, monkeypatch
    ):
        """A declaration that does not read is refused; a branch whose pull
        request removed its work item declares nothing and passes."""
        root, _code = branch
        git(root, "rm", "-rq", ITEM)
        commit(root, "no work item")
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 0 and "declared neither way" in out
        root, _code = _branch_template
        reading(monkeypatch, {f"{ITEM}/routing.md": "# nothing to read\n"})
        code, out = check(root, capsys)
        assert code == 1 and "not a readable declaration" in out

    @pytest.mark.rule("judged-where-carried")
    def test_accepts_a_release_pull_request_leaving_a_squashed_item_to_its_own(
        self, branch, ready, capsys, monkeypatch
    ):
        """Q7: a pull request into `main` from the release branch passes and
        names each item it left with its squash; a declaration naming the
        head branch is judged however it arrived, and a commit made on the
        release branch itself is the release pull request's own."""
        root, _code = branch
        released(root)
        answered(monkeypatch)
        monkeypatch.setenv("GITHUB_HEAD_REF", RELEASE)
        code, out = check(root, capsys)
        assert code == 0, out
        line = next(ln for ln in out.splitlines() if f"{ITEM}/routing.md" in ln)
        assert "judged at its own pull request" in line and "(#7)" in line
        # The ancestry refusal `chain_check.py` prints, absent from the release
        # pull request's output and present below; the orchestrator reads it.
        assert "does not descend from" not in out
        monkeypatch.setenv("GITHUB_HEAD_REF", "feature/x")
        code, out = check(root, capsys)
        # The same printed refusal, for a pull request from another branch.
        assert code == 1 and "does not descend from" in out
        assert "judged at its own pull request" not in out
        monkeypatch.setenv("GITHUB_HEAD_REF", RELEASE)
        rel = f"{ITEM}/routing.md"
        write(root, rel, (root / rel).read_text(encoding="utf-8") + "\nA note.\n")
        commit(root, "a change on the release branch itself (#8)")
        code, out = check(root, capsys)
        assert code == 1
        # The same printed refusal, for a commit on the release branch itself.
        assert "does not descend from" in out
        assert "judged at its own pull request" not in out

    def test_refuses_a_baseline_that_does_not_resolve_with_exit_2(
        self, _branch_template, capsys
    ):
        root, _code = _branch_template
        code = chain.main(["--baseline", "no-such-ref", "--root", str(root)])
        assert code == 2
        assert "does not resolve" in capsys.readouterr().err

    def test_s3_the_check_judges_the_declaration_under_agentic_seal(
        self, declared, capsys
    ):
        """The declaration naming the branch under `agentic-seal/threads/` is
        judged: `main` over `tests/conftest.py#shared` reads the root's name
        at `agentic-seal/` and hands the arms the declaration under it."""
        write(declared, "docs/a.md", "# a\n")
        commit_everything_as_e(declared, "the change")
        code, out = checked(capsys, declared)
        assert code == 1, out
        assert NO_GUARANTEE in out, out
        assert "so nothing is declared" not in out, out

    @pytest.mark.parametrize(
        "head, fork",
        [
            ({"seal/README.md": PACKAGE_README}, {"agentic-seal/README.md": MARKED}),
            (
                {"seal/README.md": PACKAGE_README, "agentic-seal/README.md": MARKED},
                {"seal/README.md": PACKAGE_README},
            ),
            ({"agentic-seal/README.md": MARKED}, {"seal/README.md": PACKAGE_README}),
        ],
        ids=["only-the-marker-deleted", "the-root-added", "added-the-package-gone"],
    )
    def test_s3_the_root_is_named_agentic_seal_beside_the_package(
        self, monkeypatch, head, fork
    ):
        """The root's name beside the package's own `seal/` is
        `agentic-seal`: where the pull request deletes only the marker, the
        merge base's root names it, as an entry at HEAD still; where the
        merge base has no root, the name HEAD gives, so the pull request that
        adds `agentic-seal/` has its declaration judged under it, and so does
        one that takes the package's `seal/` out of the tree. HEAD and the
        merge base are handed to `root_name` as the texts each carries."""
        monkeypatch.setattr(chain, "read_record", lambda _root, rel: head.get(rel))

        def git_at(_root, *args):
            assert args[0] == "show" and args[1].startswith("fork:"), args
            return fork.get(args[1].split(":", 1)[1])

        monkeypatch.setattr(chain, "git", git_at)
        assert chain.root_name(routing_module, ".", "fork") == "agentic-seal"

    @pytest.mark.parametrize("outside", [True, False], ids=["the package", "records"])
    def test_s3_a_change_to_the_package_reaches_outside_the_document_roots(
        self, monkeypatch, outside
    ):
        """With the migration config at `agentic-seal/parity.json`, a change to
        the package's `seal/__init__.py` owes the comparison, so the config's
        placeholder baseline is refused; a change confined to `agentic-seal/`
        owes none. The config is handed over (`reading`)."""
        config = "agentic-seal/parity.json"
        reading(monkeypatch, {config: parity_file(None)})
        paths = [config, "agentic-seal/follow-up.md"]
        if outside:
            paths.append("seal/__init__.py")
        found = chain.originals_of(
            routing_module, ".", "agentic-seal", paths, [], [DECLARED]
        )
        if outside:
            ((path, line, why),) = found
            assert (path, line) == (config, 0), found
            assert "`Baseline commit`" in why, why
        else:
            assert found == [], found

    def test_s3_a_design_the_pull_request_edits_under_agentic_seal_is_read(
        self, _branch_template, monkeypatch
    ):
        """Another work item's `frame/design.md` the pull request adds under
        `agentic-seal/threads/` is one the rule-changes arm reads, which
        refuses its section: a line continued past the field's one line. The
        diff is handed over as `changed` gives it."""
        monkeypatch.setattr(chain, "carried_by", lambda *_args: None)
        other = "agentic-seal/threads/1794200002-another-item"
        paths = [f"{other}/frame/design.md", "docs/a.md"]
        edited = chain.edited_work_items(
            ".", "main", paths, set(), "agentic-seal/threads"
        )
        assert edited == [other], edited
        root, _code = _branch_template
        text = spec_with(CONTINUED)
        found, _notices = read_spec(monkeypatch, root, text, other)
        assert found == [refused(root, text, other)], found

    def test_s3_a_branch_nothing_declares_is_told_to_add_it_under_agentic_seal(
        self, monkeypatch
    ):
        """With no declaration naming the branch, the check names the place it
        searched and the file to add by the root's own name."""
        monkeypatch.setenv("GITHUB_HEAD_REF", "feature")
        monkeypatch.setattr(chain, "tracked_declarations", lambda *_args: [])
        monkeypatch.setattr(chain, "local_root", lambda *_args: "")
        own, why = chain.declared_for_this_branch(
            ".", routing_module, "agentic-seal/threads"
        )
        assert own == [], own
        assert (
            "Nothing git carries under `agentic-seal/threads/` declares `feature`. "
            "Add agentic-seal/threads/<work-item>/routing.md to declare."
        ) in why, why

    @pytest.mark.parametrize("worktree", [False, True], ids=["HEAD", "--worktree"])
    def test_s3_a_pull_request_deleting_agentic_seal_declares_nothing(
        self, declared, capsys, monkeypatch, worktree
    ):
        """The pull request that takes `agentic-seal/` out of the tree deletes
        the declaration with it, and the package's `seal/` standing at HEAD is
        not the root that stayed. Under `--worktree` the deletion, staged and
        not committed, reads the same."""
        git_out(declared, "rm", "-rq", "agentic-seal")
        answered(monkeypatch)
        if worktree:
            code = chain.main(
                ["--baseline", "main", "--root", str(declared), "--worktree"]
            )
            out = capsys.readouterr().out
        else:
            commit_everything_as_e(declared, "the root leaves the tree")
            code, out = checked(capsys, declared)
        assert code == 0, out
        assert (
            "the tree the check reads has no top-level `agentic-seal` entry, so "
            "nothing is declared"
        ) in out, out
        assert NO_GUARANTEE not in out, out


# --- retired ------------------------------------------------------------------------

OLD_ITEM = "seal/threads/1788000000-an-earlier-item"


def remove_an_earlier_item(root, applied, whole=True, open_row=False):
    """Declare an earlier work item on `main`, bring it into the branch, and
    remove its directory there, or only its declaration, with or without its
    rule change applied, and with or without an open row in its record. One
    `git fast-import` writes the three commits, the merge among them, and
    the working tree is reset to the branch's head."""
    # Close enough to the branch's own declaration for git's rename detection
    # to pair the two, which `changed` reads without.
    earlier = {
        f"{OLD_ITEM}/routing.md": ROUTING.format(
            review="straight to the PR", planning="the session"
        ),
        f"{OLD_ITEM}/frame/design.md": (
            "# a spec\n\n## Rule changes\n\n- add\n  file: docs/policy.md\n"
            "  to: A rule.\n"
        ),
    }
    if open_row:
        earlier[f"{OLD_ITEM}/gaps.md"] = (
            "# x\n\n## Not verified\n\n| Item | Who must answer |\n|---|---|\n"
            "| a claim nobody ran | the repository owner |\n"
        )
    leaves = {OLD_ITEM if whole else f"{OLD_ITEM}/routing.md": None}
    if applied:
        leaves["docs/policy.md"] = "A rule.\n"
    imported(
        root,
        ("main", "main", "an earlier item, declared", earlier),
        ("feature/x", ("feature/x", ":1"), "Merge branch 'main'", earlier),
        ("feature/x", None, "the earlier item leaves", leaves),
        at=1700000100,
    )
    git(root, "reset", "-q", "--hard")


def gone_whole(monkeypatch):
    """The directories `retired` hands `settled`, and the ref with them,
    each call's appended to the list returned; `settled` answers that each
    stood there, so a case reads what `retired` passes on."""
    asked = []

    def settled(root, ref, directories):
        asked.append((ref, list(directories)))
        return set(directories)

    monkeypatch.setattr(chain, "settled", settled)
    return asked


@pytest.mark.rule("a-declaration-removed")
class Test_retired:
    @pytest.mark.rule("a-settle-is-no-deletion")
    def test_accepts_a_declaration_a_settle_removed(self, branch, draft, capsys):
        """S6 of #1033: a `routing.md` whose whole directory stood at the
        merge base and is gone is a settle. The notice says what was read.
        `main` runs over a real removed history, so it hands `retired` the
        merge base and the declarations' texts at HEAD as git gives them."""
        root, _code = branch
        remove_an_earlier_item(root, applied=False, open_row=True)
        _code, out = check(root, capsys)
        assert f"{OLD_ITEM}/routing.md:0  {chain.SETTLE_SAYS}" in out, out
        # Contract rule 14: the words a person reads, not only the constant.
        assert (
            "retired: a settle — the work item's directory stood at the merge "
            "base and is gone whole"
        ) in out, out
        assert "does not carry this file at HEAD" not in out

    @pytest.mark.parametrize(
        "planted",
        [{}, {"docs/policy.md": "A rule.\n"}],
        ids=["nothing-on-disk", "its-rule-in-docs"],
    )
    @pytest.mark.rule("a-settle-is-no-deletion")
    def test_hands_settled_each_directory_gone_whole_and_reads_nothing_else(
        self, tmp_path, monkeypatch, planted
    ):
        """S6 of #1033: what the record held at the merge base and what
        `docs/` holds of its spec decide nothing: `retired` hands `settled`
        the directory of each declaration HEAD does not carry and the disk
        does not hold, with the merge base, and a declaration HEAD carries
        is no candidate."""
        for rel, text in planted.items():
            write(tmp_path, rel, text)
        asked = gone_whole(monkeypatch)
        texts = {f"{OLD_ITEM}/routing.md": None, f"{ITEM}/routing.md": "x"}
        assert chain.retired(str(tmp_path), "fork", texts) == {OLD_ITEM}
        assert asked == [("fork", [OLD_ITEM])]

    def test_refuses_a_declaration_deleted_beside_a_directory_that_stays(
        self, tmp_path, monkeypatch
    ):
        """S8: a `routing.md` deleted beside a `frame/design.md` that stays is a
        deletion: a settle takes the whole directory, so `settled` is never
        asked of it."""
        write(tmp_path, f"{OLD_ITEM}/frame/design.md", "# a spec\n")
        asked = gone_whole(monkeypatch)
        texts = {f"{OLD_ITEM}/routing.md": None}
        assert chain.retired(str(tmp_path), "fork", texts) == set()
        assert asked == [("fork", [])]

    def test_refuses_a_deleted_declaration_whose_directory_stays_by_name(
        self, branch, ready, capsys, monkeypatch
    ):
        """S8, as `main` prints it: the merged item's `routing.md` deleted
        beside its round record that stays is refused as a declaration git
        does not carry, and no settle is named."""
        root, _code = branch
        git(root, "rm", "-q", f"{MERGED_ITEM}/routing.md")
        commit(root, "the merged item's declaration leaves")
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 1, out
        assert (
            f"{MERGED_ITEM}/routing.md:0  git does not carry this file at HEAD"
        ) in out, out
        assert "retired:" not in out

    @pytest.mark.rule("nothing-declared-nothing-owed")
    def test_accepts_every_declaration_leaving_with_the_root(
        self, branch, ready, capsys, monkeypatch
    ):
        """Round 1 of #952, finding 1: the pull request that takes `seal/`
        out of the tree deletes every declaration with it, and with no
        `seal` at HEAD nothing is declared. Where git cannot say whether HEAD
        has it, the declarations stay judged, and since #1033 each one whose
        directory stood at the merge base and is gone whole reads as a
        settle."""
        root, _code = branch
        remove_an_earlier_item(root, applied=False)
        git(root, "rm", "-rq", "seal")
        commit(root, "the root leaves the tree")
        answered(monkeypatch)
        code, out = check(root, capsys)
        assert code == 0, out
        assert (
            "the tree the check reads has no top-level `seal` entry, so nothing "
            "is declared: the routing declarations this pull request deletes "
            "left the tree with the root, and the review-chain check judged the "
            "commit trailers and nothing else"
        ) in out
        assert "does not carry this file at HEAD" not in out
        real = chain.git
        unanswered = ("ls-tree", "HEAD", "--", "seal")
        monkeypatch.setattr(
            chain, "git", lambda r, *a: None if a == unanswered else real(r, *a)
        )
        code, out = check(root, capsys)
        assert "so nothing is declared" not in out, out
        assert f"{OLD_ITEM}/routing.md:0  {chain.SETTLE_SAYS}" in out, out

    def test_a_root_that_left_for_a_local_root_says_the_check_judged_nothing(
        self, branch, ready, capsys, monkeypatch
    ):
        """The same pull request, read by the session that ran `seal mode
        local`: the root now stands under the common git directory, where
        each trailer is printed, not judged, so the notice says the check
        judged nothing."""
        root, _code = branch
        remove_an_earlier_item(root, applied=False)
        git(root, "rm", "-rq", "seal")
        commit(root, "the root leaves the tree")
        mark_root(os.path.join(common_dir(root), "seal"))
        answered(monkeypatch)
        code, out = check(root, capsys, "--worktree")
        assert code == 0, out
        assert (
            "the tree the check reads has no top-level `seal` entry, so nothing "
            "is declared: the routing declarations this pull request deletes "
            "left the tree with the root, and the review-chain check judged "
            "nothing: at a local root each commit's `Seal-Routing` trailer is "
            "printed, not judged"
        ) in out, out
        assert "judged the commit trailers" not in out, out

    @pytest.mark.rule("nothing-declared-nothing-owed")
    def test_accepts_under_worktree_a_root_the_working_tree_no_longer_has(
        self, branch, ready, capsys, tmp_path, monkeypatch
    ):
        """Round 3 of #952, finding 2: a switch to local mode, run and not
        committed, leaves no `seal` in the working tree, so under `--worktree`
        nothing is declared, as CI reads the same change once it is committed."""
        root, _code = branch
        remove_an_earlier_item(root, applied=False)
        shutil.move(str(root / "seal"), str(tmp_path / "moved-seal"))
        git(root, "add", "-A", "seal")
        answered(monkeypatch)
        code, out = check(root, capsys, "--worktree")
        assert code == 0, out
        # The line `chain_check.py` prints when no root is in the working
        # tree, which the session running `--worktree` reads.
        assert "so nothing is declared" in out
        assert "does not carry this file at HEAD" not in out

    def test_judges_a_root_the_working_tree_has_under_worktree(
        self, branch, ready, capsys, monkeypatch
    ):
        """Round 2 of #952, finding 2: under `--worktree` the tree the check
        reads is the working tree, so a root it holds and HEAD does not is a
        root, and the declaration naming the branch in it is judged."""
        root, _code = branch
        git(root, "rm", "-rq", "--cached", "seal")
        git(root, "commit", "-qm", "the root leaves HEAD and stays on disk")
        answered(monkeypatch, real=("follows",))
        code, out = check(root, capsys, "--worktree")
        assert "so nothing is declared" not in out, out
        assert code == 1 and f"{ITEM}/guarantee.md:0  the guarantee is behind" in out

    def test_judges_the_declarations_where_the_working_tree_has_seal_as_a_file(
        self, branch, ready, capsys, monkeypatch
    ):
        """Round 2 of #952, finding 3: a `seal` that is not a directory is
        still an entry, so under `--worktree` the declarations it replaced
        stay judged."""
        root, _code = branch
        shutil.rmtree(root / "seal")
        write(root, "seal", "not a root\n")
        answered(monkeypatch)
        code, out = check(root, capsys, "--worktree")
        assert "so nothing is declared" not in out, out
        assert code == 0 and f"{MERGED_ITEM}/routing.md:0  retired: a settle" in out


class Test_module:
    def test_a_script_copied_alone_exits_2_and_names_what_it_misses(self, tmp_path):
        """#590, and S4 of #1482. A copy of this script taken without its
        siblings exits 2, with the loader's one sentence naming the absent
        `lib/sibling.py` by its path, where it printed a line of its own: 2
        means the input or the tree was unusable and nothing was read, and a
        sibling that is not beside the command is that kind. It is given its
        one required flag, so argparse's own exit 2 cannot pass for it."""
        args = ["--baseline", "HEAD", "--root", "{root}"]
        script = TARGET
        name = script.rsplit("/", 1)[1]
        alone = tmp_path / "alone"
        alone.mkdir()
        copy = alone / name
        with open(os.path.join(ROOT, *script.split("/")), encoding="utf-8") as f:
            copy.write_text(f.read(), encoding="utf-8")
        repo = tmp_path / "repo"
        repo.mkdir()
        done = subprocess.run(
            [sys.executable, str(copy), *(a.format(root=repo) for a in args)],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            cwd=str(repo),
        )
        assert done.returncode == 2, (done.returncode, done.stderr)
        lib = os.path.join(str(alone), "..", "..", "..", "lib", "sibling.py")
        said = chain.sibling.MISSING.format(path=os.path.normpath(lib))
        assert done.stderr == said + "\n", done.stderr

    def test_an_absent_reader_is_the_loaders_sentence_alone(self, tmp_path):
        """*Scope* item 4 of #1482. A copy that holds the loader and lacks
        the shared reader exits 2 as a command, with the loader's sentence
        naming the reader and no line of the check's own about it."""
        plugin = tmp_path / "plugin"
        for rel in (TARGET, "lib/sibling.py"):
            copy = plugin.joinpath(*rel.split("/"))
            copy.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(os.path.join(ROOT, *rel.split("/")), copy)
        repo = tmp_path / "repo"
        repo.mkdir()
        done = subprocess.run(
            [
                sys.executable,
                str(plugin.joinpath(*TARGET.split("/"))),
                "--baseline",
                "HEAD",
                "--root",
                str(repo),
            ],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            cwd=str(repo),
        )
        assert done.returncode == 2, (done.returncode, done.stderr)
        reader = plugin / "lib" / "lines.py"
        said = chain.sibling.MISSING.format(path=str(reader))
        assert done.stderr == said + "\n", done.stderr

    def test_the_framers_mark_is_the_last_line_a_renderer_shows(self):
        """S10 of #664. The mark stands after a U+2028 on the file's last line,
        which GFM does not end a line at, so the last line does not begin with
        one."""
        spec = f"# spec\n\nprose{LS}Framed 2026-01-01 by framer, before the build.\n"
        assert chain.frame_foot(spec)[0] is None
        whole = "# spec\n\nprose\nFramed 2026-01-01 by framer, before the build.\n"
        assert chain.frame_foot(whole)[0] == ("2026-01-01", "framer")

    def test_loads_beside_no_policy_document(self, tmp_path):
        """*Scope* item 5 of #1198: the round record's grammar is
        `lib/fields.py`, so the check loads and reads a record with no
        `docs/` beside it. Seen red against the check that loaded its grammar
        table from `docs/the-review-record.md` at import, which raised
        "cannot be read"."""
        script = copied_tree(tmp_path / "tree")
        assert not (tmp_path / "tree" / "docs").exists()
        loaded = load(script, "chain_check_beside_no_document")
        found, errors = loaded.record_findings(
            record("abc1234", [finding(1, "rejected")]), "r.md"
        )
        assert (errors, [f.verdict for f in found]) == ([], [(chain.REJECTED, None)])


# --- left where they stand, for #923: they read the shipped documents --------------


def test_the_proofer_and_the_review_skill_name_every_line_a_finding_needs():
    """S8 (#985), under #1198: `agents/proofer.md` step 7 and
    `skills/code-review/SKILL.md` *The record* each list the lines a
    finding's block carries, and each names every key a finding block holds
    one of, read from `lib/fields.py`."""
    kind = chain.FIELDS.FINDING_BLOCK
    needed = [key for key, spec in kind.keys.items() if spec.many == chain.FIELDS.ONE]
    proofer = " ".join((ROOT / "agents" / "proofer.md").read_text("utf-8").split())
    step = proofer.split("7. Write the record", 1)[1].split("## Never", 1)[0]
    skill = " ".join(
        (ROOT / "skills" / "code-review" / "SKILL.md").read_text("utf-8").split()
    )
    said = skill.split("## The record ", 1)[1]
    said = said.split("Each finding's section holds one finding block", 1)[1]
    said = said.split("The check refuses a finding whose block", 1)[0]
    for where, text in (
        ("proofer.md step 7", step),
        ("`skills/code-review/SKILL.md` *The record*", said),
    ):
        missing = [key for key in needed if f"`{key}" not in text]
        # Each key a finding block holds one of, spelled as `lib/fields.py`
        # matches it, which the proofer writes from these two lists.
        assert missing == [], f"{where} does not name {missing}"


def test_the_template_is_the_record_the_check_reads():
    """S1 (T29, T38): `templates/records/sdd-round.md` is a record the check
    reads: one round block and no table above the findings; one finding
    whose block locates it at one coordinate, rests on one `evidence:` line
    and names the regression `round-1#1`, with its close block after the fix
    fence, `fixed` at a commit the fix pass names; a close written inside
    the fix block not read as one; `## Confirmations` holding one example
    block; no `reopens:` line and no
    `original:` line, with the review skill saying where a `reopens:`
    finding's grounds open; and no emoji anywhere."""
    text = TEMPLATE.read_text(encoding="utf-8")
    read, errors = chain.round_of(text, "t", 1)
    assert errors == []
    assert [(f.verdict, f.paths, f.regression, f.reopens) for f in read.findings] == [
        ((chain.FIXED, "1a2b3c4"), ["path"], (1, 1), None)
    ]
    assert text.count("\nevidence: ") == 1
    assert "\nreopens: " not in text and "\noriginal: " not in text
    skill = (ROOT / "skills" / "code-review" / "SKILL.md").read_text("utf-8")
    assert "where `reopens:` stands" in " ".join(skill.split())
    assert read.findings[0].heading.startswith("### 1. ")
    assert read.findings[0].number == 1
    assert [ref for _line, ref in read.confirms] == [(1, 2)]
    assert text.count("\nconfirms: ") == 1
    head = text.split(chain.FINDINGS_HEADING)[0]
    assert all(tables.table_cells(line) is None for line in reader.readable(head))
    assert read.target == "1a2b3c4"
    start = text.index(FENCE + "seal\nverdict: ")
    end = text.index(FENCE + "\n", start + len(FENCE)) + len(FENCE) + 1
    without = text[:start] + text[end:]
    fix = without.index(FENCE + "<lang>\n") + len(FENCE + "<lang>\n")
    quoted = without[:fix] + "verdict: rejected\nanswer: x\n" + without[fix:]
    found, errors = chain.record_findings(quoted, "t")
    assert errors == [] and [f.verdict for f in found] == [(chain.OPEN, None)]
    assert [c for c in text if EMOJI.match(c)] == []


# --- what git answers, and the policy root (#1482) ---------------------------


class Test_policy_root:
    def test_accepts_the_row_a_config_writes(self, joined, tmp_path):
        d = copy_of(joined, tmp_path)
        write(
            d,
            "seal/config.json",
            config_json(("Policy root", "rules")),
        )
        assert chain.policy_root(str(d)) == "rules"

    def test_refuses_to_read_anything_but_docs_with_no_row(self, joined):
        assert chain.policy_root(str(joined)) == "docs"


def answering(monkeypatch, word, stdout):
    """`subprocess.run` answering exit 0 with STDOUT to every git call that
    carries WORD, and running every other call. The module itself is
    patched, the one `lib/gitcmd.py#git` calls."""
    real_run = subprocess.run

    def stub(argv, *a, **kw):
        if isinstance(argv, list) and word in argv:
            return subprocess.CompletedProcess(argv, 0, stdout, "")
        return real_run(argv, *a, **kw)

    monkeypatch.setattr(subprocess, "run", stub)


class Test_pull_request_from_gh:
    @pytest.mark.parametrize("state", ["draft", "ready"])
    def test_accepts_the_state_gh_answers(self, tmp_path, monkeypatch, state):
        monkeypatch.setenv("PATH", conftest.gh_answers(os.environ, state)["PATH"])
        assert chain.pull_request_from_gh(str(tmp_path)) == (
            state,
            "`gh pr view --json isDraft`",
        )

    @pytest.mark.parametrize("cause", ["exited", "past the bound", "not on PATH"])
    def test_refuses_a_gh_that_did_not_answer_as_unknown(
        self, tmp_path, monkeypatch, cause
    ):
        """S8 of #1573 for the one `gh` call: a `gh` past
        `lib/gitcmd.py#TIMEOUT`, or not on PATH, is an unknown state with
        the runner's line, which `main` does not judge as a ready pull
        request; a non-zero exit keeps the check's own line. Seen red
        against `chain_check.py` before #1573, whose `run` seam was bound
        before any case could patch it, and which said that no `gh` was on
        PATH to ask."""
        said = {
            "exited": '`gh pr view` exited 1: no pull requests found for branch "x"',
            "past the bound": (
                f"`gh pr view --json isDraft` did not finish within "
                f"{chain.GITCMD.TIMEOUT} seconds"
            ),
            "not on PATH": (
                "`gh pr view --json isDraft` could not be run: `gh` is not on PATH"
            ),
        }[cause]
        if cause == "past the bound":
            unanswered(monkeypatch, "pr", "view")
        elif cause == "not on PATH":
            monkeypatch.setenv("PATH", str(tmp_path))
        assert chain.pull_request_from_gh(str(tmp_path)) == (
            "unknown",
            f"{chain.NO_PAYLOAD}, and {said}",
        )


class Test_commit_of:
    def test_accepts_a_ref_as_its_commit(self, plain):
        assert chain.commit_of(str(plain), "HEAD") == git_out(
            plain, "rev-parse", "HEAD"
        )

    def test_refuses_a_ref_that_does_not_resolve_or_answers_nothing(
        self, plain, monkeypatch
    ):
        assert chain.commit_of(str(plain), "origin/nosuchbranch") is None
        answering(monkeypatch, "--verify", "\n")
        assert chain.commit_of(str(plain), "HEAD") is None


class Test_resolves:
    def test_accepts_a_ref_that_names_a_commit(self, plain):
        assert chain.resolves(str(plain), "HEAD") is True

    def test_refuses_a_ref_git_answers_with_nothing(self, plain, monkeypatch):
        """`chain_check.py` loads this for whether a ref resolves; an empty
        answer is a refusal, not a sentinel travelling out as resolved."""
        answering(monkeypatch, "--verify", "\n")
        assert chain.resolves(str(plain), "HEAD") is False


class Test_merge_base:
    def test_accepts_the_fork_point_of_a_moved_base(self, forked):
        assert chain.merge_base(str(forked), "base") == git_out(
            forked, "rev-parse", "fork"
        )

    def test_refuses_an_unrelated_history_and_an_empty_answer(
        self, forked, monkeypatch
    ):
        assert chain.merge_base(str(forked), "unrelated") is None
        answering(monkeypatch, "merge-base", "\n")
        assert chain.merge_base(str(forked), "base") is None


class Test_tree_at:
    def test_accepts_a_directory_at_a_ref_and_on_disk(self, settle):
        listed = [f"specs/{SETTLE_A}/design.md", f"specs/{SETTLE_A}/gaps.md"]
        assert chain.tree_at(str(settle), "HEAD", f"specs/{SETTLE_A}") == listed
        assert chain.tree_at(str(settle), None, f"specs/{SETTLE_A}") == listed

    def test_accepts_a_directory_whose_id_is_not_ascii(self, tmp_path):
        """#1283. At a ref the paths come from `ls-tree -z`, so they are
        returned as they are and as the disk gives them, not in git's
        quoting. Seen red against the listing without `-z`."""
        directory = f"specs/{NON_ASCII}"
        d = _committed(tmp_path, {f"{directory}/gaps.md": memo(CANONICAL)})
        listed = [f"{directory}/gaps.md"]
        assert chain.tree_at(str(d), "HEAD", directory) == listed
        assert chain.tree_at(str(d), None, directory) == listed

    @pytest.mark.parametrize("ref", ["HEAD", None, "nosuch"])
    def test_refuses_a_directory_that_is_not_there(self, settle, ref):
        directory = "specs/none" if ref != "nosuch" else f"specs/{SETTLE_A}"
        assert chain.tree_at(str(settle), ref, directory) == []


class Test_settled:
    def test_accepts_every_directory_that_stood_at_the_ref(self, settle):
        """S6 at the predicate (#1033): a directory that stood at the ref is
        settled whatever its record and its spec say: an open row, a spec an
        earlier commit dropped, a rule `docs/` does not hold, a section that
        does not parse, a spec with no section, and no spec at all."""
        dirs = [
            f"specs/{n}"
            for n in (
                OPEN_ITEM,
                DROPPED,
                SETTLE_A,
                SETTLE_BAD,
                SETTLE_C,
                CLOSED_ITEM,
            )
        ]
        assert chain.settled(str(settle), "HEAD", dirs) == set(dirs)

    @pytest.mark.parametrize(
        "ref, name",
        [("HEAD", "1780000099-none"), ("nosuch", OPEN_ITEM)],
        ids=["a directory the ref never held", "a ref that does not resolve"],
    )
    def test_refuses_a_directory_the_ref_does_not_hold(self, settle, ref, name):
        assert chain.settled(str(settle), ref, [f"specs/{name}"]) == set()


class Test_rule_changes_reader:
    def test_accepts_the_one_reader_of_a_specs_rule_changes(self):
        assert callable(chain.rule_changes_reader().parse)

    def test_refuses_to_load_it_twice(self):
        assert chain.rule_changes_reader() is chain.rule_changes_reader()


test_census = census_case(TARGET)

"""`skills/code-review/scripts/chain_check.py`, one class per function.

Rebuilt by #942's phase 5. The readers of a round record's `seal` blocks
and the reference channel run in the process on text. `main` runs in the
process over a repository built once for the module and copied for each
case that judges it: a branch with a routing declaration, a code commit, two
round records and the closing records, judged as a ready or a draft pull
request through the event payload GitHub writes. Each copy is the reset.
`Test_module` holds the case that reads this module's source for a call of
`unverified_check.py#settled` and no second definition of it, which #942
moved from `tests/behaviour/test_unverified_rows_close.py`; the copy run without its
siblings, from `tests/test_a_script_copied_alone_exits_2.py`; and the
framer's mark after a U+2028, `frame_foot`'s one case, from
`tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py`. The last two came in
its round 9 fix pass, each a case of this module alone.
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
from conftest import (
    BASELINE,
    LS,
    census_case,
    chain_check_run,
    commit_everything_as_e,
    mark_root,
    names_path,
    parity_file,
    write,
)
from conftest import commit_everything as commit
from conftest import git_out as git
from conftest import load_module as load
from conftest import seal_block as block

TARGET = "skills/code-review/scripts/chain_check.py"

ROOT = pathlib.Path(conftest.ROOT)
CHAIN = ROOT / TARGET
READER = ROOT / "skills" / "verify" / "scripts" / "unverified_check.py"
ITEM = "seal/threads/1791999999-a-work-item"
# The pictographs and symbols a mark is drawn from: the colour circles and
# squares, the check and cross marks, the question mark ornament and the
# variation selector that follows them.
EMOJI = re.compile("[⌀-⏿☀-➿⬀-⯿️\U0001f000-\U0001faff]")

chain = load(CHAIN, "chain_check_under_test")
reader = load(READER, "unverified_reader_for_chain_tests")
check = functools.partial(chain_check_run, chain)

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
        read, said = chain.round_of(reader, text, f"round-{n}.md", n)
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


@pytest.fixture(scope="module")
def _branch_template(tmp_path_factory):
    """A repository whose `feature/x` declares a work item and reviewed it,
    built once for the module.

    `main` holds one file and a work item another pull request merged, its
    declaration naming another branch and its one record in the old table's
    shape with a finding open (S11). `feature/x` adds the declaration, a code
    commit, round 1 at that commit with its one finding `fixed` by it, round
    2, the verifying round, confirming `round-1#1` with nothing of its own,
    and the closing records. Returns `(root, code commit)`."""
    d = tmp_path_factory.mktemp("chain-world") / "r"
    init(d)
    write(d, "f.txt", "one\n")
    write(
        d,
        f"{MERGED_ITEM}/routing.md",
        ROUTING.format(
            review="through the review chain", planning="the session"
        ).replace("feature/x", "feature/merged"),
    )
    write(d, f"{MERGED_ITEM}/trail/rounds/round-1.md", OLD_RECORD)
    commit(d, "base")
    git(d, "switch", "-q", "-c", "feature/x")
    write(
        d,
        f"{ITEM}/routing.md",
        ROUTING.format(review="through the review chain", planning="the session"),
    )
    commit(d, "routing")
    write(d, "f.txt", "two\n")
    code = commit(d, "code")
    write(
        d,
        f"{ITEM}/trail/rounds/round-1.md",
        record(code, [finding(1, f"fixed {code[:8]}")]),
    )
    commit(d, "the round record")
    write(
        d,
        f"{ITEM}/trail/rounds/round-2.md",
        record(code, confirmations=confirm("round-1#1"), n=2),
    )
    reviewed = commit(d, "the verifying round")
    # Two runs, the newest last: the earlier one names a commit nobody can
    # see, so a reader that took any run but the last would refuse the file.
    write(d, f"{ITEM}/trail/gate.md", gate_file("1" * 40, reviewed))
    write(d, f"{ITEM}/guarantee.md", guarantee_file(reviewed))
    commit(d, "the closing records")
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

DOC = ROOT / "docs" / "the-review-record.md"
TEMPLATE = ROOT / "templates" / "records" / "sdd-round.md"


def copied_tree(tree):
    """The check and the files it loads at import, copied under TREE, as the
    path of the copied script."""
    script = tree / "skills" / "code-review" / "scripts" / "chain_check.py"
    script.parent.mkdir(parents=True)
    script.write_text(CHAIN.read_text(encoding="utf-8"), encoding="utf-8")
    (tree / "skills" / "verify" / "scripts").mkdir(parents=True)
    (tree / "skills" / "verify" / "scripts" / "unverified_check.py").write_text(
        READER.read_text(encoding="utf-8"), encoding="utf-8"
    )
    (tree / "hooks" / "lib").mkdir(parents=True)
    for name in ("blocks.py", "fields.py"):
        (tree / "hooks" / "lib" / name).write_text(
            (ROOT / "hooks" / "lib" / name).read_text(encoding="utf-8"),
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
    read, errors = chain.round_of(reader, text, "r.md", 1)
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
            read, errors = chain.round_of(reader, text, "r.md", 1)
            assert errors == [("r.md", 0, chain.NO_ROUND_BLOCK)], errors
            assert (read.findings, read.confirms, read.target) == ([], [], None)
        for words in (
            "no round block",
            "`seal` blocks",
            "`templates/records/sdd-round.md`",
            "rewritten into blocks with its verdicts unchanged",
        ):
            assert words in chain.NO_ROUND_BLOCK, words

    def test_accepts_each_confirmation_block_as_a_reference_or_none(self):
        """S23: each entry is a confirmation block reading `round-<N>#<n>`,
        read with its line, or `none`; a record with nothing to confirm may
        leave the section out."""
        text = record(
            "abc1234",
            confirmations=confirm("round-1#2") + confirm("none") + confirm("round-3#1"),
            n=4,
        )
        read, errors = chain.round_of(reader, text, "r.md", 4)
        assert errors == []
        assert read.confirms == [
            (line_at(text, "confirms: round-1#2"), (1, 2)),
            (line_at(text, "confirms: round-3#1"), (3, 1)),
        ]
        left_out = record("abc1234").replace("## Confirmations\n", "")
        read, errors = chain.round_of(reader, left_out, "r.md", 1)
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
            "**none**",
            "None",
            "round-1#2 holds",
            "",
        )
        text = record(
            "abc1234",
            confirmations="".join(confirm(cell) for cell in bad) + confirm("none"),
            n=2,
        )
        read, errors = chain.round_of(reader, text, "r.md", 2)
        assert read.confirms == []
        assert [line for _rel, line, _why in errors] == [
            line_at(text, f"confirms: {cell}") for cell in bad
        ], errors
        for (_rel, _line, why), cell in zip(errors, bad, strict=True):
            assert f"`confirms: {cell}`" in why, why
            assert "`round-<N>#<n>` or `none`" in why, why
        prose = record(
            "abc1234",
            confirmations="| Confirms | What holds |\n|---|---|\n| round-1#2 | x |\n\n"
            "confirms: round-1#2\nheld.\n",
            n=2,
        )
        assert chain.round_of(reader, prose, "r.md", 2)[0].confirms == []
        assert chain.round_of(reader, prose, "r.md", 2)[1] == []


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
        found, errors = chain.record_findings(reader, text, "r.md")
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
        assert chain.record_findings(reader, record("abc1234"), "r.md") == ([], [])

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
        found, errors = chain.record_findings(reader, text, "r.md")
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
            reader, block("target: abc1234 against main") + "\n## Probes\n", "r.md"
        ) == ([], [("r.md", 0, chain.NO_FINDINGS)])
        longer = record("abc1234", [finding(1, "open")]).replace(
            "## Findings", "## Findings so far"
        )
        assert chain.record_findings(reader, longer, "r.md")[1] == [
            ("r.md", 0, chain.NO_FINDINGS),
            (
                "r.md",
                opener_at(longer, "severity: must"),
                chain.OUTSIDE.format(kind="finding"),
            ),
        ]
        two = record("abc1234") + "\n## Findings\n"
        assert chain.record_findings(reader, two, "r.md") == (
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
        found, errors = chain.record_findings(reader, text, "r.md")
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
        found, errors = chain.record_findings(reader, text, "r.md")
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
        found, errors = chain.record_findings(reader, text, "r.md")
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
        assert chain.record_findings(reader, text, "r.md") == (
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
        found, errors = chain.record_findings(reader, text, "r.md")
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
                + block("confirms: none"),
                finding(2, "rejected"),
            ],
        ).replace(
            "## Not judged\n", "## Not judged\n\n" + stray + "\n" + close("rejected")
        )
        found, errors = chain.record_findings(reader, text, "r.md")
        assert [f.number for f in found] == [2]
        assert errors == [
            (
                "r.md",
                opener_at(text, "target: abc1234 against main", 1),
                led(text, 1, chain.INSIDE.format(kind="round")),
            ),
            (
                "r.md",
                opener_at(text, "confirms: none"),
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
        found, errors = chain.record_findings(reader, text, "r.md")
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

    def test_refuses_a_finding_block_lacking_its_evidence_at_its_opener(self):
        """S1, S3, S4 (#985): a finding block carries one `evidence:` line;
        one with none is refused at its opener, led by the heading, and the
        shapes the line takes are `tests/hooks/test_fields.py`'s."""
        text = record(
            "abc1234", [finding(1, "open", evidence=None), finding(2, "open")]
        )
        found, errors = chain.record_findings(reader, text, "r.md")
        assert [f.number for f in found] == [2], errors
        assert errors == [
            (
                "r.md",
                opener_at(text, "severity: must"),
                led(
                    text,
                    1,
                    chain.FIELDS.MISSING.format(kind="finding", key="evidence:"),
                ),
            )
        ]

    def test_accepts_both_evidence_forms_and_their_lists(self):
        """S5 (#985): `executed` with one or more backticked commands, and
        `read` with one or more backticked coordinates, each list joined by
        `, `, and the stand-in for a backtick the record document names."""
        stand_in = "$(printf '\\140')"
        values = (
            "executed `git grep -n x -- tests`",
            "executed `a`, `b`",
            "read `a.py:3`",
            "read `a.py:3-9`, `docs/b.md:12`",
            f'executed `grep -n "{stand_in}evidence:" docs/x.md`',
        )
        text = record(
            "abc1234",
            [finding(n, "rejected", evidence=v) for n, v in enumerate(values, 1)],
        )
        found, errors = chain.record_findings(reader, text, "r.md")
        assert errors == []
        assert [(f.number, f.verdict) for f in found] == [
            (n, (chain.REJECTED, None)) for n in range(1, 6)
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
        found, errors = chain.record_findings(reader, text, "r.md")
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

    def test_refuses_a_severity_off_its_shape_and_a_close_with_no_answer(self):
        """Two refusals that arrive by construction from the block grammar: a
        severity other than `must` or `should`, at its line, and a close
        block with no `answer:` line, at its opener."""
        text = record(
            "abc1234",
            [
                finding(1, "rejected", severity="anything at all"),
                finding(2, "open") + "\n" + block("verdict: rejected"),
                finding(3, "rejected"),
            ],
        )
        found, errors = chain.record_findings(reader, text, "r.md")
        assert [f.number for f in found] == [3], errors
        said = {line: why for _rel, line, why in errors}
        severity = line_at(text, "severity: anything at all")
        assert "a severity is `must` or `should`" in said[severity], said
        second = opener_at(text, "verdict: rejected", 1)
        assert "holds no `answer:` line" in said[second], said

    def test_accepts_a_record_whose_regions_close(self):
        text = record("abc1234", [finding(1, "open"), finding(2, "rejected")])
        found, errors = chain.record_findings(reader, text, "r.md")
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
        found, errors = chain.record_findings(reader, quoted, "r.md")
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
        found, errors = chain.record_findings(reader, text, "r.md")
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
        found, errors = chain.record_findings(reader, text, "r.md")
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
        found, errors = chain.record_findings(reader, text, "r.md")
        line = text.splitlines().index(note) + 1
        assert errors == [("r.md", line, reader.COMMENT_LINE)], errors
        assert [f.number for f in found] == [1, 2]

    @pytest.mark.rule("location-touched-by-fix")
    def test_accepts_one_or_more_backticked_coordinates(self):
        """S22 (T33): the paths of a `location:` value the block's shape
        matched, each backticked `path`, `path:line` or `path:first-last`
        item to its first `:`; the shape's refusals are
        `tests/hooks/test_fields.py`'s. `chain_check.location_paths` is the
        step of `finding_of` that gives a finding its paths, and has no
        refusal of its own, since the value it takes is one
        `hooks/lib/fields.py` already matched whole."""
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
            confirmations=confirm("round-1#1") + confirm("none"),
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
            confirmations=confirm("round-1#1") + confirm("none"),
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
        not hold, is refused by its line; `none` in the first record passes."""
        one = record(
            "abc1234",
            [finding(1, "deferred #9", regression="round-1#1", reopens=None)],
            confirmations=confirm("none") + confirm("round-1#1"),
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
        assert "`round-3#1`" in said[2] and "not an earlier record" in said[2]
        assert "`round-2`" in said[3] and "not an earlier record" in said[3]
        assert "`round-1#7`" in said[4] and "holds no finding 7" in said[4]
        assert "`round-1#7`" in said[5] and "holds no finding 7" in said[5]
        quiet = rounds_of(record("abc1234", confirmations=confirm("none")))[0]
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
    def test_accepts_head_and_record_commits_after_it(self, branch):
        root, code = branch
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
        return load(ROOT / "hooks" / "lib" / "routing.py", "routing_for_chain_tests")

    def test_accepts_a_framed_item_with_a_reframe_by_the_framer(self, branch):
        root, _code = branch
        write(
            root,
            f"{ITEM}/frame/design.md",
            SPEC + "Reframed 2026-10-16 by framer, after round 2.\n",
        )
        write(root, f"{ITEM}/frame/plan.md", "# plan\n")
        commit(root, "frame")
        assert chain.frame(reader, self.routing(), str(root), ITEM, FRAMED) == []

    def test_refuses_a_missing_plan_and_a_reframe_by_another_party(self, branch):
        root, _code = branch
        write(
            root,
            f"{ITEM}/frame/design.md",
            SPEC + "Reframed 2026-10-16 by the session, after round 2.\n",
        )
        commit(root, "frame")
        problems = chain.frame(reader, self.routing(), str(root), ITEM, FRAMED)
        assert any("plan.md" in p for p in problems)
        assert any("Reframed 2026-10-16 by the session" in p for p in problems)


# --- rule_changes_read, at the pull request --------------------------------------

RULES = reader.rule_changes()
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


def template_section():
    """What `templates/records/sdd-design.md` holds under its `## Rule changes`:
    nothing, which is what a framer's skeleton commit carries."""
    text = (ROOT / "templates" / "records" / "sdd-design.md").read_text(
        encoding="utf-8"
    )
    section = text.split("\n## Rule changes\n", 1)[1].split("\n## Removes\n", 1)[0]
    assert section.strip() == "", section
    return section


def spec_with(section):
    """A spec whose `## Rule changes` holds SECTION, or that has no such
    section where SECTION is None, ending with the framer's mark."""
    rules = "" if section is None else f"## Rule changes\n\n{section}\n"
    return f"# spec\n\nbody\n\n{rules}## Removes\n\nnone\n\n" + SPEC.split("\n\n")[-1]


def put_spec(root, text, committed=True):
    """Write the work item's `frame/design.md`; where COMMITTED, commit it and the
    closing records after it, so the spec is the one thing to refuse."""
    write(root, f"{ITEM}/frame/design.md", text)
    if committed:
        commit(root, "the spec")
        seal(root)


def refusal(root, text, item=ITEM):
    """The line the check prints for ITEM's spec reading TEXT outside CI,
    built from `rule_changes.parse`'s own error so no reason is spelt here."""
    ((line, reason),) = RULES.parse(text, reader.policy_root(str(root))).errors
    return f"{item}/frame/design.md:{line}  {chain.RULE_CHANGES_SAYS.format(reason=reason)}"


def unread_heading(root, text, item=ITEM):
    """The notice the check prints outside CI for ITEM's spec reading TEXT,
    whose one near heading `rule_changes.parse` names, built from the
    parser's own reason."""
    ((line, why),) = RULES.parse(text, reader.policy_root(str(root))).unread
    return f"{item}/frame/design.md:{line}  {chain.RULE_CHANGES_UNREAD.format(why=why)}"


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
        [lambda: CONTINUED, lambda: PROSE, template_section],
        ids=["S1-continued-two-in", "S2-prose-under-items", "S3-the-template-section"],
    )
    def test_refuses_a_section_the_parser_refuses_at_its_line(
        self, branch, ready, capsys, section
    ):
        """S1, S2, S3: the one refusal names the spec, the line the parser
        names and the parser's reason; S3's section is the template's, empty."""
        root, _code = branch
        text = spec_with(section())
        put_spec(root, text)
        code, out = check(root, capsys)
        assert code == 1, out
        assert spec_lines(out) == [refusal(root, text)], out
        assert SAYS in spec_lines(out)[0]

    @pytest.mark.parametrize(
        "section", [NOTHING, CHANGE, None], ids=["no-change", "a-change", "none"]
    )
    def test_accepts_a_section_that_parses_or_no_section(
        self, branch, ready, capsys, section
    ):
        root, _code = branch
        put_spec(root, spec_with(section))
        code, out = check(root, capsys)
        assert code == 0, out
        assert spec_lines(out) == [], out

    def test_names_a_near_heading_as_not_read_and_passes(
        self, branch, ready, capsys, monkeypatch
    ):
        """#1167, *Scope* item 7: a spec whose section stands under
        `## Rule Changes` has no `## Rule changes` section, so it passes as a
        spec with none does, and the heading is printed `not read:` at its
        line, a notice annotation in CI. Seen red against the refusal at the
        heading, exit 1."""
        root, _code = branch
        text = spec_with(NOTHING).replace("## Rule changes", NEAR_HEADING)
        put_spec(root, text)
        code, out = check(root, capsys)
        assert code == 0, out
        assert spec_lines(out) == [unread_heading(root, text)], out
        monkeypatch.setenv("GITHUB_ACTIONS", "true")
        code, out = check(root, capsys)
        assert code == 0, out
        where, said = unread_heading(root, text).split("  ", 1)
        path, line = where.rsplit(":", 1)
        assert spec_lines(out) == [f"::notice file={path},line={line}::{said}"], out

    def test_names_a_near_heading_beside_a_refusal_and_keeps_the_refusal(
        self, branch, ready, capsys
    ):
        """The naming decides nothing: beside a `## Rule changes` section the
        parser refuses, the refusal stands at exit 1 and the near heading is
        printed as not read after it."""
        root, _code = branch
        text = spec_with(CONTINUED).replace(
            "## Removes", f"{NEAR_HEADING}\n\n{NOTHING}\n## Removes"
        )
        put_spec(root, text)
        code, out = check(root, capsys)
        assert code == 1, out
        assert spec_lines(out) == [
            unread_heading(root, text),
            refusal(root, text),
        ], out

    def test_names_a_near_heading_in_another_work_items_spec_the_branch_edits(
        self, branch, ready, capsys
    ):
        """The heading is named in every spec the arm reads, an edited spec of
        another work item among them, and the check passes."""
        root, _code = branch
        text = spec_with(NOTHING).replace("## Rule changes", NEAR_HEADING)
        write(root, f"{MERGED_ITEM}/frame/design.md", text)
        commit(root, "another work item's spec under a near heading")
        reviewed_to_head(root)
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
        self, branch, ready, capsys
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
        put_spec(root, spec_with(CONTINUED))
        write(root, f"{MERGED_ITEM}/frame/design.md", spec_with(CONTINUED))
        commit(root, "another work item's spec")
        reviewed_to_head(root)
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
        self, branch, ready, capsys
    ):
        """S9: a spec written and not committed is refused under `--worktree`;
        CI reads HEAD, which does not carry it."""
        root, _code = branch
        text = spec_with(CONTINUED)
        put_spec(root, text, committed=False)
        code, out = check(root, capsys, "--worktree")
        assert code == 1, out
        assert spec_lines(out) == [refusal(root, text)], out
        code, out = check(root, capsys)
        assert code == 0, out
        assert spec_lines(out) == [], out

    def test_refuses_to_run_where_its_reader_will_not_load(
        self, branch, ready, capsys, monkeypatch
    ):
        """S10: exit 2 naming the reader, for the judged item's spec and for
        an edited spec; a work item with no `frame/design.md` never reaches it."""
        root, _code = branch
        monkeypatch.setattr(chain.SHARED_READER, "rule_changes", will_not_load)
        code, out = check(root, capsys)
        assert code == 0, out
        write(root, f"{MERGED_ITEM}/frame/design.md", spec_with(NOTHING))
        commit(root, "another work item's spec")
        reviewed_to_head(root)
        code = chain.main(["--baseline", "main", "--root", str(root)])
        err = capsys.readouterr().err
        assert code == 2, err
        assert "the rule-changes reader would not load (a planted failure)" in err
        put_spec(root, spec_with(NOTHING))
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
        self, branch, ready, capsys
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
        seal(root)
        code, out = check(root, capsys)
        assert code == 1, out
        assert spec_lines(out, MERGED_ITEM) == [refusal(root, text, MERGED_ITEM)], out

    def test_accepts_a_pull_request_that_declares_nothing_reading_no_spec(
        self, branch, ready, capsys
    ):
        """S15: the promise in `hygiene.yml` and `CONTRIBUTING.md` holds."""
        root, _code = branch
        git(root, "rm", "-rq", ITEM)
        write(root, f"{MERGED_ITEM}/frame/design.md", spec_with(CONTINUED))
        commit(root, "no work item, and a spec")
        code, out = check(root, capsys)
        assert code == 0, out
        assert "declared neither way" in out
        assert spec_lines(out, MERGED_ITEM) == [], out

    def test_accepts_a_spec_only_moved_and_a_file_beside_or_below_one(
        self, branch, ready, capsys
    ):
        """S16: a move with the bytes unchanged writes no section; another
        file beside a spec the branch leaves alone, and a `frame/design.md` one
        directory down, write none either."""
        root, _code = branch
        old, new = "seal/threads/1788000001-old", "seal/threads/1788000001-moved"
        on_main(root, f"{old}/frame/design.md", spec_with(CONTINUED))
        on_main(root, f"{MERGED_ITEM}/frame/design.md", spec_with(CONTINUED))
        git(root, "mv", old, new)
        write(root, f"{MERGED_ITEM}/frame/plan.md", "# plan\n")
        # Bytes of its own: a copy of the moved spec's bytes would read as a
        # second name of that move.
        write(root, f"{MERGED_ITEM}/notes/frame/design.md", spec_with(PROSE))
        commit(root, "moved, beside another work item's spec, and below it")
        reviewed_to_head(root)
        code, out = check(root, capsys)
        assert code == 0, out
        for item in (old, new, MERGED_ITEM, f"{MERGED_ITEM}/notes"):
            assert spec_lines(out, item) == [], (item, out)


# --- the parity arm at the pull request (#988) -------------------------------------

PARITY = "seal/parity.md"
routing_module = load(chain.ROUTING, "agentic_routing_for_chain_tests")


def with_original(text, said):
    """A round record with `original: SAID` under its `target:` line."""
    assert text.count(" against main\n") == 1
    return text.replace(" against main\n", f" against main\noriginal: {said}\n")


def migrating(root, originals, sha=BASELINE):
    """`main` declares a migration whose baseline is SHA, merged into
    `feature/x`; each round record N gains `original: <ORIGINALS[N-1]>`,
    none where that is None, and the closing records name HEAD."""
    on_main(root, PARITY, parity_file(sha))
    for n, said in enumerate(originals, 1):
        if said is not None:
            rel = f"{ITEM}/trail/rounds/round-{n}.md"
            write(root, rel, with_original((root / rel).read_text("utf-8"), said))
    if any(said is not None for said in originals):
        commit(root, "the rounds compared with the original")
    seal(root)


def original_lines(out):
    """The lines the check prints about a round record or the config."""
    where = (f"{ITEM}/trail/rounds/", f"{PARITY}:")
    return [ln for ln in out.splitlines() if ln.startswith(where)]


@pytest.mark.rule("parity-at-the-pull-request")
class Test_originals_of:
    def test_refuses_a_record_with_no_original_line_on_a_ready_pull_request(
        self, branch, ready, capsys
    ):
        """S4: in a repository declaring `seal/parity.md`, a chain-declared
        pull request changing code fails while a round record holds no
        `original:` line, each record named with the baseline it owes, and a
        draft prints the same lines and exits 0."""
        root, _code = branch
        migrating(root, (None, None))
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
        self, branch, ready, capsys, originals, sha
    ):
        root, _code = branch
        migrating(root, originals, sha)
        code, out = check(root, capsys)
        assert code == 0, out
        assert original_lines(out) == [], out

    def test_refuses_a_record_naming_another_commit_naming_both(
        self, branch, ready, capsys
    ):
        root, _code = branch
        other = "fedcba9876543210"
        migrating(root, (BASELINE, other))
        code, out = check(root, capsys)
        assert code == 1, out
        rel = f"{ITEM}/trail/rounds/round-2.md"
        line = line_at((root / rel).read_text("utf-8"), f"original: {other}")
        says = chain.OTHER_ORIGINAL.format(said=other, sha=BASELINE)
        assert original_lines(out) == [f"{rel}:{line}  {says}"], out
        assert other in says and BASELINE in says

    def test_refuses_a_config_whose_baseline_holds_no_commit(
        self, branch, ready, capsys
    ):
        """S10: the template's placeholder fails a ready pull request naming
        `seal/parity.md`, and no record is compared with nothing."""
        root, _code = branch
        migrating(root, (BASELINE, BASELINE), sha=None)
        code, out = check(root, capsys)
        assert code == 1, out
        (line,) = original_lines(out)
        assert line.startswith(f"{PARITY}:0  "), line
        assert "`Baseline commit`" in line and "`<SHA>`" in line, line

    def test_accepts_a_change_confined_to_the_document_roots(self, branch):
        """S7 and S11: a change confined to `docs/` and `seal/` owes no line,
        one path outside them owes it, and paths git could not list owe it
        too, as `hooks/lib/gate.py#touches_code` reads them."""
        root, _code = branch
        migrating(root, (None, None))
        inside = ["docs/a.md", f"{ITEM}/trail/rounds/round-1.md"]

        def owed(paths):
            return chain.originals_of(reader, routing_module, str(root), paths, [ITEM])

        assert owed(inside) == []
        assert [p for p, _n, _w in owed([*inside, "f.txt"])] == [
            f"{ITEM}/trail/rounds/round-1.md",
            f"{ITEM}/trail/rounds/round-2.md",
        ]
        assert owed(None) == owed([*inside, "f.txt"])

    def test_refuses_to_run_where_the_parity_readers_will_not_load(
        self, branch, ready, capsys, monkeypatch
    ):
        root, _code = branch
        migrating(root, (None, None))
        monkeypatch.setattr(chain, "parity_readers", will_not_load)
        code = chain.main(["--baseline", "main", "--root", str(root)])
        err = capsys.readouterr().err
        assert code == 2, err
        assert "the parity readers would not load (a planted failure)" in err

    @pytest.mark.rule("parity-in-the-guarantee")
    def test_refuses_a_direct_guarantee_with_no_original_line_and_accepts_one(
        self, item, capsys
    ):
        """S12: under `straight to the PR` no round records a comparison, so
        in a migration repository the sealer's `guarantee.md` carries the
        `original:` line, and a ready pull request changing code fails
        without it, names a guarantee naming another commit, and passes with
        the baseline. `--sealing` reads the missing line as a notice, as it
        reads every other guarantee check."""
        root, _audited = item
        rel = f"{ITEM}/guarantee.md"
        direct_migrating(root, None)
        code, out = check(root, capsys)
        assert code == 1, out
        says = chain.NO_GUARANTEE_ORIGINAL.format(config=PARITY, sha=BASELINE)
        for words in (
            f"no `original:` line in the newest verdict block: `{PARITY}` "
            "declares a migration, this work item answers `straight to the PR`",
            f"the sealer's guarantee carries `original: {BASELINE}`",
            "once it compared the audited commit with the original through "
            "`legacy-parity`",
        ):
            assert words in says, says
        opener = (root / rel).read_text(encoding="utf-8").split("\n").index("```seal")
        assert f"{rel}:{opener + 1}  {says}" in out.splitlines(), out
        code, out = check(root, capsys, "--sealing")
        assert code == 0, out
        direct_migrating(root, "fedcba9876543210")
        code, out = check(root, capsys)
        assert code == 1, out
        assert chain.OTHER_ORIGINAL.format(said="fedcba9876543210", sha=BASELINE) in (
            out
        )
        direct_migrating(root, BASELINE[:10])
        code, out = check(root, capsys)
        assert code == 0, out

    @pytest.mark.rule("parity-in-the-guarantee")
    def test_refuses_a_direct_guarantee_whose_only_original_is_misspelt(
        self, item, capsys
    ):
        """The third scenario of #1167, #1121's R9, under #1198's blocks: in a
        migration repository a verdict block holding `Original: <sha>` is
        refused at that line with the keys the block takes, and the original
        arm adds no second refusal for a guarantee the guarantee arm refuses.
        Seen red against the reader of #1167, which read the line as prose,
        named it as not read and refused the file for lacking the line."""
        root, _audited = item
        rel = f"{ITEM}/guarantee.md"
        direct_migrating(root, BASELINE)
        assert check(root, capsys)[0] == 0
        path = root / rel
        text = path.read_text(encoding="utf-8").replace("original:", "Original:")
        path.write_text(text, encoding="utf-8")
        commit(root, "the sealer spelt the key otherwise")
        code, out = check(root, capsys)
        assert code == 1, out
        number = text.splitlines().index(f"Original: {BASELINE}") + 1
        said = chain.FIELDS.NOT_A_FIELD.format(
            line=f"Original: {BASELINE}",
            kind="verdict",
            keys="`target:`, `original:` and `Verdict:`",
        )
        assert [ln for ln in out.splitlines() if ln.startswith(f"{rel}:")] == [
            f"{rel}:{number}  {said}"
        ], out

    @pytest.mark.rule("parity-in-the-guarantee")
    def test_a_missing_guarantee_is_named_once(self, item, capsys):
        """A guarantee git does not carry is the guarantee arm's refusal, and
        no second one asks it for an `original:` line."""
        root, _audited = item
        direct_migrating(root, None)
        git(root, "rm", "-q", f"{ITEM}/guarantee.md")
        commit(root, "no guarantee")
        code, out = check(root, capsys)
        assert code == 1, out
        assert "git carries no guarantee file" in out, out
        assert "no `original:` line" not in out, out

    @pytest.mark.rule("parity-in-the-guarantee")
    def test_a_direct_guarantee_owes_nothing_for_the_document_roots_alone(
        self, item, capsys
    ):
        """S12: a change confined to `docs/` and `seal/` has no original to
        compare with, and a repository declaring no migration owes nothing."""
        root, _audited = item
        assert check(root, capsys)[0] == 0
        git(root, "switch", "-q", "main")
        write(root, PARITY, parity_file(BASELINE))
        commit(root, f"{PARITY} on the base")
        git(root, "switch", "-q", "-c", "feature/docs")
        write(
            root,
            f"{ITEM}/routing.md",
            SEALED_ROUTING.replace("feature/g", "feature/docs"),
        )
        write(root, "docs/a.md", "# a policy\n")
        commit(root, "a documentation pass")
        reseal(root, None)
        code, out = check(root, capsys)
        assert code == 0, out

    @pytest.mark.rule("parity-in-the-guarantee")
    def test_owes_no_original_line_where_none_is_owed(self, item, capsys):
        """Round 4 of #1167: a guarantee's `original:` line is owed only where
        `originals_of` reads the guarantee: with no migration config, and
        with one where the diff stays inside the document roots, a verdict
        block without one passes, and a block holding `Original: <sha>` is
        refused for its line alone, never for a missing `original:` line."""
        root, _audited = item
        rel = f"{ITEM}/guarantee.md"

        def respelt():
            path = root / rel
            text = path.read_text(encoding="utf-8")
            assert text.count("original:") == 1, text
            path.write_text(text.replace("original:", "Original:"), encoding="utf-8")
            commit(root, "a guarantee holding Original: where none is owed")
            code, out = check(root, capsys)
            assert code == 1, out
            refused = [ln for ln in out.splitlines() if ln.startswith(f"{rel}:")]
            assert len(refused) == 1 and "is no field of a verdict block" in refused[0]
            assert "no `original:` line" not in out, out

        reseal(root, None)
        assert check(root, capsys)[0] == 0
        reseal(root, BASELINE)
        respelt()
        git(root, "switch", "-q", "main")
        write(root, PARITY, parity_file(BASELINE))
        commit(root, f"{PARITY} on the base")
        git(root, "switch", "-q", "-c", "feature/docs")
        write(
            root,
            f"{ITEM}/routing.md",
            SEALED_ROUTING.replace("feature/g", "feature/docs"),
        )
        write(root, "docs/a.md", "# a policy\n")
        commit(root, "a documentation pass")
        reseal(root, None)
        assert check(root, capsys)[0] == 0
        reseal(root, BASELINE)
        respelt()


class Test_original_of:
    def test_accepts_a_line_naming_the_baseline_by_a_prefix(self):
        text = with_original(record("abc1234", [finding(1, "rejected")]), BASELINE[:9])
        assert chain.original_of(reader, text, "r.md", BASELINE, PARITY) == []

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
        _round, errors = chain.round_of(reader, text, "r.md", 1)
        assert [(n, said in why) for _r, n, why in errors] == [
            (line_at(text, line, where == "twice"), True)
        ], errors
        assert chain.original_of(reader, text, "r.md", BASELINE, PARITY) == []

    def test_refuses_a_round_block_with_no_original_line_at_its_opener(self):
        text = record("abc1234", [finding(1, "rejected")])
        assert chain.original_of(reader, text, "r.md", BASELINE, PARITY) == [
            ("r.md", 3, chain.NO_ORIGINAL.format(config=PARITY, sha=BASELINE))
        ]
        assert chain.original_of(reader, LABELLED, "r.md", BASELINE, PARITY) == []


class Test_parity_readers:
    def test_accepts_a_process_that_loaded_only_the_check(self):
        """`parity_readers` loads `hooks/lib/config.py` before `hooks/lib/gate.py`,
        whose `import optin` needs `hooks/` on `sys.path`, so a fresh
        interpreter that loaded the check alone still loads both."""
        code = (
            "import importlib.util, sys\n"
            f"s = importlib.util.spec_from_file_location('c', {str(CHAIN)!r})\n"
            "m = importlib.util.module_from_spec(s)\n"
            "s.loader.exec_module(m)\n"
            "config, gate = m.parity_readers()\n"
            "print(gate.touches_code(['f.txt']), config.BASELINE_ROW)\n"
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
        """A `hooks/lib/gate.py` that raises at import is raised to the caller,
        which `originals_of` turns into exit 2; nothing hands back a reader
        that did not load."""
        shutil.copy(ROOT / "hooks" / "lib" / "config.py", tmp_path / "config.py")
        (tmp_path / "gate.py").write_text("raise ImportError('planted')\n", "utf-8")
        monkeypatch.setattr(chain, "HOOKS", str(tmp_path))
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
        "| Field | Value |\n|---|---|\n"
        f"| Broad gate | {sha} against main, as `trail/gate.md` names it |\n\n"
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


@pytest.fixture
def item(tmp_path, monkeypatch):
    """A branch that went straight to the pull request and was sealed: the
    code, then `trail/gate.md` and `guarantee.md` naming that commit, judged
    as a ready pull request. Returns `(root, the audited commit)`."""
    d = tmp_path / "g"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "t@t")
    git(d, "config", "user.name", "t")
    write(d, "f.txt", "one\n")
    commit(d, "base")
    git(d, "switch", "-q", "-c", "feature/g")
    write(d, f"{ITEM}/routing.md", SEALED_ROUTING)
    write(d, "f.txt", "two\n")
    audited = commit(d, "the work")
    write(d, f"{ITEM}/trail/gate.md", gate_file(audited))
    write(d, f"{ITEM}/guarantee.md", guarantee(audited, "sealed"))
    commit(d, "the closing records")
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": False}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    return d, audited


def reseal(root, original):
    """The closing records naming HEAD, committed; the guarantee's verdict
    block carries `original: ORIGINAL` where ORIGINAL is given."""
    head = git(root, "rev-parse", "HEAD")
    write(root, f"{ITEM}/trail/gate.md", gate_file(head))
    write(root, f"{ITEM}/guarantee.md", guarantee(head, "sealed", original))
    commit(root, "the closing records, again")


def direct_migrating(root, original):
    """`main` declares a migration whose baseline is `BASELINE`, merged once
    into the `item` fixture's `feature/g`; then `reseal`."""
    if not (root / PARITY).exists():
        git(root, "switch", "-q", "main")
        write(root, PARITY, parity_file(BASELINE))
        commit(root, f"{PARITY} on the base")
        git(root, "switch", "-q", "feature/g")
        git(root, "merge", "-q", "--no-edit", "main")
    reseal(root, original)


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
    def test_accepts_a_sealed_verdict_at_head(self, item):
        root, _sha = item
        assert chain.guarantee(reader, str(root), ITEM, "main") == []

    def test_accepts_the_newest_of_two_runs(self, item, capsys):
        """#1198's scenario *Two sealer runs*: the sealer appends a verdict
        block per run, so a `withheld` at an older commit above a `sealed`
        at HEAD passes, and the same blocks the other way round read the
        newest as `withheld`. Seen red against the reader that read the
        first block."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        older = git(root, "rev-parse", "HEAD~1")
        text = guarantee(sha, "sealed", earlier=[(older, "withheld reason: x")])
        write(root, rel, text)
        commit(root, "a second run")
        assert chain.guarantee(reader, str(root), ITEM, "main") == []
        assert check(root, capsys)[0] == 0
        swapped = verdict_block(sha) + "\n" + verdict_block(older, "withheld reason: x")
        write(root, rel, swapped)
        commit(root, "the runs the other way round")
        problems = chain.guarantee(reader, str(root), ITEM, "main")
        assert any("`Verdict: withheld reason: x`" in why for _p, _n, why in problems)

    def test_refuses_absent_unfilled_and_behind_head_by_name(self, item):
        root, _sha = item
        rel = f"{ITEM}/guarantee.md"
        write(root, f"{ITEM}/gaps.md", "# an edit the sealer never read\n")
        later = commit(root, "a record after the guarantee")
        [(path, _line, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        assert path == rel and later[:8] in why
        template = GUARANTEE_TEMPLATE.read_text(encoding="utf-8")
        write(root, rel, template)
        commit(root, "the template, unfilled")
        [(path, line, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        placeholder = template.split("\n")[line - 1]
        assert path == rel and placeholder.startswith("target: <"), placeholder
        assert why.startswith(f"`{placeholder}` does not read whole"), why
        head = git(root, "rev-parse", "HEAD")
        two = guarantee(head, "sealed").replace(
            "```seal\n", "```seal\nVerdict: sealed\n"
        )
        write(root, rel, two)
        commit(root, "a verdict above the target")
        [(_p, _n, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        assert why == chain.FIELDS.NO_KIND.format(
            line="Verdict: sealed", openers="`target:`"
        )
        git(root, "rm", "-q", rel)
        commit(root, "no guarantee")
        [(_p, _n, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        assert "git carries no guarantee file" in why

    def test_refuses_a_guarantee_of_the_old_shape_naming_the_template(self, item):
        """#1198's scenario *A record from before the change*, for the
        guarantee, and *Scope* item 9: a `Target SHA` row and a `Verdict:`
        line hold no verdict block, and the one refusal names the template
        and says the sealer appends a block. Seen red against the reader
        before #1198, which passed the record."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        old = (
            "| Field | Value |\n|---|---|\n"
            f"| Target SHA | {sha} against main |\n\nVerdict: sealed\n"
        )
        write(root, rel, old)
        commit(root, "a guarantee of the shape before the blocks")
        assert chain.guarantee(reader, str(root), ITEM, "main") == [
            (rel, 0, chain.NO_VERDICT_BLOCK)
        ]
        assert "`templates/records/sdd-guarantee.md`" in chain.NO_VERDICT_BLOCK
        assert "appends one" in chain.NO_VERDICT_BLOCK

    def test_refuses_a_fence_nobody_closed_between_two_runs(self, item):
        """#1122, at the check: a `sealed` block, then a fence nobody closed,
        then a `withheld` block. A renderer hides everything below the
        fence, so the check refuses it at its opener."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        newest = verdict_block(sha, "withheld reason: the gate failed")
        text = guarantee(sha, "sealed") + "\n````\n\n" + newest
        write(root, rel, text)
        commit(root, "a fence nobody closed")
        opener = text.split("\n").index("````") + 1
        assert chain.guarantee(reader, str(root), ITEM, "main") == [
            (rel, opener, chain.FIELDS.UNCLOSED)
        ]

    def test_an_opener_quoted_in_a_code_span_hides_no_verdict(self, item):
        """Round 1 of #1000, finding 2: a claims cell quoting the comment
        opener in a code span, as two merged guarantees do, leaves the
        verdict block below it read."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace(
            "|---|---|---|---|\n\n## The parties",
            "|---|---|---|---|\n| markers | `x.md:1` | `git grep '<!-- specs/'` "
            "| holds |\n\n## The parties",
        )
        write(root, rel, text)
        commit(root, "a claim quoting the opener")
        assert chain.guarantee(reader, str(root), ITEM, "main") == []

    @pytest.mark.rule("record-comment-line-refused")
    def test_refuses_a_comment_line_at_its_line(self, item):
        """S5 of #1012: a verdict quoted in a comment above the verdict block
        is refused at its line."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace(
            "```seal\n", "<!-- Verdict: sealed -->\n```seal\n"
        )
        write(root, rel, text)
        commit(root, "a verdict in a comment")
        line = text.splitlines().index("<!-- Verdict: sealed -->") + 1
        assert chain.guarantee(reader, str(root), ITEM, "main") == [
            (rel, line, reader.COMMENT_LINE)
        ]

    @pytest.mark.parametrize("line", NEAR_MISSES)
    def test_refuses_a_near_miss_of_the_verdict_at_its_line(self, item, line):
        """S6 of #1000, inside a verdict block: the value is read whole
        against the three shapes and refused at its line naming them. A word
        the verdict used before #969 needs no list of its own (#1198,
        `## Removes`)."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace("Verdict: sealed", line)
        write(root, rel, text)
        commit(root, f"the sealer wrote {line}")
        [(path, number, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        assert (path, number) == (rel, text.splitlines().index(line) + 1), why
        for shape in (
            "`Verdict: sealed`",
            "`Verdict: withheld reason: <reason>`",
            "`Verdict: undecided question: <question>`",
        ):
            assert shape in why, why

    @pytest.mark.parametrize("line", OPENS_LIKE)
    def test_refuses_a_line_that_opens_like_the_verdict_at_its_line(self, item, line):
        """#1198: inside a block a line is a field or refused, so a verdict
        spelt otherwise is refused at its line with the keys a verdict block
        takes, where #1167 read it as prose. Seen red against that reader,
        which named it and refused the file for having no verdict line."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace("Verdict: sealed", line)
        write(root, rel, text)
        commit(root, f"the sealer wrote {line}")
        number = text.splitlines().index(line) + 1
        said = chain.FIELDS.NOT_A_FIELD.format(
            line=line, kind="verdict", keys="`target:`, `original:` and `Verdict:`"
        )
        assert chain.guarantee(reader, str(root), ITEM, "main") == [(rel, number, said)]

    def test_names_a_near_opener_and_reads_no_verdict(self, item, capsys):
        """A fence like the block's and not it is no block: the guarantee
        holding it alone has no verdict block, and the opener is printed at
        its line as not read, which adds nothing to the exit code."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace("```seal", "```Seal")
        write(root, rel, text)
        commit(root, "a near opener")
        notices = []
        assert chain.guarantee(reader, str(root), ITEM, "main", notices) == [
            (rel, 0, chain.NO_VERDICT_BLOCK)
        ]
        number = text.splitlines().index("```Seal") + 1
        said = chain.FIELDS.NEAR.format(line="```Seal")
        assert notices == [(rel, number, said)]
        code, out = check(root, capsys)
        assert code == 1 and f"{rel}:{number}  {said}" in out.splitlines(), out

    def test_a_verdict_other_than_sealed_fails_a_ready_pull_request(self, item, capsys):
        """T8, S8 of #969: `withheld` and `undecided` fail a ready pull request
        naming the file and the verdict; a draft prints the same line and
        passes; `--sealing`, the broad gate's own run, prints it."""
        root, sha = item
        code, out = check(root, capsys)
        assert code == 0, out
        rel = f"{ITEM}/guarantee.md"
        for verdict in (
            "withheld reason: the body claims a README change",
            "undecided question: Q?",
        ):
            write(root, rel, guarantee(sha, verdict))
            commit(root, f"the sealer says {verdict}")
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
    def test_accepts_a_run_at_head(self, item):
        root, _sha = item
        assert chain.broad_gate(reader, str(root), ITEM, "main") == []

    def test_accepts_the_last_run_block_as_the_newest(self, item):
        """#1198, *Scope* item 2: `seal gate --record` appends a block per
        run, so the last block is the newest run, and an earlier block naming
        a commit nobody can see decides nothing; the same blocks the other
        way round are a stale run. Seen red against the reader that took the
        first block."""
        root, sha = item
        rel = f"{ITEM}/trail/gate.md"
        write(root, rel, gate_file("1" * 40, sha))
        commit(root, "an earlier run, then the run at the audited commit")
        assert chain.broad_gate(reader, str(root), ITEM, "main") == []
        write(root, rel, gate_file(sha, "1" * 40))
        commit(root, "the runs the other way round")
        [(path, line, why)] = chain.broad_gate(reader, str(root), ITEM, "main")
        assert (path, line) == (rel, 0) and "the newest gate run" in why, why

    @pytest.mark.rule("record-comment-line-refused")
    def test_refuses_a_comment_line_at_its_line(self, item):
        """S5 of #1012: a `trail/gate.md` line that begins with `<!--` is
        refused at its line."""
        root, sha = item
        rel = f"{ITEM}/trail/gate.md"
        write(root, rel, "<!-- the gate's guidance -->\n\n" + gate_file(sha))
        commit(root, "a comment in the gate record")
        assert chain.broad_gate(reader, str(root), ITEM, "main") == [
            (rel, 1, reader.COMMENT_LINE)
        ]

    def test_refuses_a_record_with_no_run_block_naming_the_command(self, item):
        """#1198, *Scope* item 9: a gate record of the shape before 0.27.0, its
        run a table cell, holds no run block, and is refused with the one
        sentence that names the command which appends one."""
        root, sha = item
        rel = f"{ITEM}/trail/gate.md"
        write(
            root,
            rel,
            f"| Field | Value |\n|---|---|\n| Broad gate | {sha} against main |\n",
        )
        commit(root, "a gate record from before the blocks")
        assert chain.broad_gate(reader, str(root), ITEM, "main") == [
            (rel, 0, chain.NO_RUN_BLOCK)
        ]
        assert "`seal gate --base <base> --record <item>`" in chain.NO_RUN_BLOCK
        assert "since #1198" in chain.NO_RUN_BLOCK

    def test_refuses_a_run_block_that_does_not_parse_at_its_line(self, item):
        root, sha = item
        rel = f"{ITEM}/trail/gate.md"
        text = gate_file(sha).replace(f"run: {sha}", f"run:  {sha}")
        write(root, rel, text)
        commit(root, "a run line with two spaces")
        [(path, line, why)] = chain.broad_gate(reader, str(root), ITEM, "main")
        assert (path, line) == (
            rel,
            text.splitlines().index(f"run:  {sha} against {GATE_BASE}") + 1,
        )
        assert why.startswith(
            f"`run:  {sha} against {GATE_BASE}` does not read whole"
        ), why

    def test_names_a_near_opener_as_not_read(self, item):
        """A fence like the block's and not it is named in NOTICES, and its
        run is no run: the record then holds none."""
        root, sha = item
        rel = f"{ITEM}/trail/gate.md"
        text = gate_file(sha).replace("```seal", "```Seal")
        write(root, rel, text)
        commit(root, "a near opener")
        notices = []
        assert chain.broad_gate(reader, str(root), ITEM, "main", notices) == [
            (rel, 0, chain.NO_RUN_BLOCK)
        ]
        line = text.splitlines().index("```Seal") + 1
        assert notices == [(rel, line, chain.FIELDS.NEAR.format(line="```Seal"))]


# --- the declaration for this branch, in local mode (#225) --------------------------

CHECK = str(CHAIN)
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


def run_check(repo, *extra):
    r = subprocess.run(
        [
            sys.executable,
            CHECK,
            "--worktree",
            "--baseline",
            "HEAD",
            "--root",
            str(repo),
            *extra,
        ],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
        cwd=str(repo),
    )
    return r.returncode, r.stdout + r.stderr


ADD_THE_FILE = "Add seal/threads/<work-item>/routing.md to declare"
# A shared-mode declaration naming the `repo` fixture's branch.
DECLARES_FEATURE = ROUTING.format(
    review="through the review chain", planning="the session"
).replace("feature/x", "feature")


class Test_declared_for_this_branch:
    def test_refuses_a_local_declaration_and_says_it_is_local_mode(self, repo):
        """A local-mode repository is told the root it searched, not to write a
        file it already has."""
        local_item(repo)
        code, out = run_check(repo)
        assert code == 0, out
        assert ADD_THE_FILE not in out, out
        assert "local mode" in out, out
        assert os.path.normpath(os.path.join(common_dir(repo), "seal")) in out, out
        assert "seal mode shared" in out, out

    def test_local_mode_still_examines_nothing(self, repo):
        """Naming the root does not turn an untracked declaration into a checked
        one: CI reads what git carries, and local mode commits nothing."""
        local_item(repo)
        _code, out = run_check(repo)
        assert "examined nothing" in out, out
        assert "through the review chain" not in out, out

    def test_accepts_a_shared_root_and_tells_it_to_add_the_file(self, repo):
        """A shared-mode repository with no declaration is told to write one."""
        (repo / "seal" / "threads").mkdir(parents=True)
        code, out = run_check(repo)
        assert code == 0, out
        assert ADD_THE_FILE in out, out
        assert "local mode" not in out, out

    def test_the_shared_sentence_says_what_it_searched_and_for_what(self, repo):
        """The prefix and the branch are what make the sentence checkable."""
        (repo / "seal" / "threads").mkdir(parents=True)
        _code, out = run_check(repo)
        assert "under `seal/threads/`" in out, out
        assert "declares `feature`" in out, out

    def test_a_repository_with_no_root_is_told_to_add_the_file(self, repo):
        """With no root to name, the file to write is the answer."""
        code, out = run_check(repo)
        assert code == 0, out
        assert ADD_THE_FILE in out, out
        assert "local mode" not in out, out

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
        assert chain.declared_for_this_branch(str(repo), routing_module) == (
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
        own, why = chain.declared_for_this_branch(str(repo), routing_module)
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
        own, why = chain.declared_for_this_branch(str(repo), routing_module)
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


@pytest.fixture
def undeclared(tmp_path, monkeypatch):
    """`feature/t`, which no declaration names, judged as a ready pull
    request: `main` holds one file."""
    d = tmp_path / "t"
    init(d)
    write(d, "f.txt", "one\n")
    commit(d, "base")
    git(d, "switch", "-q", "-c", "feature/t")
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
        self, undeclared, capsys
    ):
        """S1 of #1142: the key a commit made before the rename carries,
        `SpecSeal-Routing:`, is read as any other trailer key is: not judged.
        A work item no declaration names passes a ready pull request, and
        `no work item` prints no notice."""
        root = undeclared
        write(root, "a.txt", "a\n")
        named = commit_saying(root, "feat: a", f"SpecSeal-Routing: {ROUTED}")
        write(root, "b.txt", "b\n")
        none = commit_saying(root, "chore: b", "SpecSeal-Routing: no work item")
        code, out = check(root, capsys)
        assert code == 0, out
        assert named[:8] not in out, out
        assert none[:8] not in out, out

    def test_accepts_a_commit_naming_the_work_item_its_declaration_names(
        self, branch, ready, capsys
    ):
        root, _code = branch
        commit_saying(root, "chore: e", "Seal-Routing: 1791999999-a-work-item")
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out
        assert "Seal-Routing" not in out, out

    def test_a_teammates_commit_is_never_judged(self, undeclared, capsys):
        """S11: the harness's co-author trailer, which any Claude Code
        session carries, is not the session's routing trailer."""
        root = undeclared
        write(root, "a.txt", "a\n")
        commit_saying(
            root,
            "feat: a teammate's change",
            "Co-Authored-By: Claude <noreply@example.com>",
        )
        code, out = check(root, capsys)
        assert code == 0, out
        assert "Seal-Routing" not in out, out

    def test_a_merge_and_a_squash_github_committed_are_not_its_own(
        self, undeclared, capsys
    ):
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
        code, out = check(root, capsys)
        assert code == 0, out
        assert ROUTED not in out, out

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

    def test_a_commit_its_author_did_not_commit_is_not_judged(self, undeclared, capsys):
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
        code, out = check(root, capsys)
        assert code == 0, out
        assert ROUTED not in out, out

    def test_refuses_to_run_where_the_commits_cannot_be_read(
        self, undeclared, capsys, monkeypatch
    ):
        monkeypatch.setattr(chain, "routing_trailers", lambda root, base: None)
        code = chain.main(["--baseline", "main", "--root", str(undeclared)])
        err = capsys.readouterr().err
        assert code == 2, err
        assert "cannot read the commits after main" in err, err


# --- main: the arms over a pull request ----------------------------------------------


@pytest.mark.rule("routing-read-first")
class Test_main:
    @pytest.mark.rule("old-table-shape-refused")
    def test_accepts_a_reviewed_branch_on_a_ready_pull_request(
        self, branch, ready, capsys
    ):
        """S11: the merged item's old-shape record, a finding open in it, is
        never opened; the check judges only what this pull request carries."""
        root, _code = branch
        code, out = check(root, capsys)
        assert code == 0, out
        assert MERGED_ITEM not in out

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_an_open_finding_on_a_ready_pull_request(
        self, branch, ready, capsys
    ):
        """#1198's scenario *An open finding* (S3, T27): a finding with no
        close block is open, refused at its heading with the line the fix
        pass appends, and a draft prints the same line and passes. A
        finding's `severity:` decides nothing."""
        root, code_sha = branch
        rel = f"{ITEM}/trail/rounds/round-1.md"
        text = record(code_sha, [finding(1, "open")])
        write(root, rel, text)
        commit(root, "the record, still open")
        code, out = check(root, capsys)
        assert code == 1
        heading = "### 1. the parser drops a row"
        said = (
            f"{rel}:{line_at(text, heading)}  {heading} {chain.DASH} {chain.OPEN_SAYS}"
        )
        assert said in out.splitlines(), out
        assert chain.OPEN_SAYS == (
            "no close block, so the finding is open: the fix pass appends one "
            "after its paste-ready fix, opening with `verdict:` and reading "
            "`fixed <commit>`, `rejected` or `deferred <home>`"
        )
        ready.write_text(json.dumps({"pull_request": {"draft": True}}), "utf-8")
        code, out = check(root, capsys)
        assert code == 0
        assert said in out.splitlines(), out
        ready.write_text(json.dumps({"pull_request": {"draft": False}}), "utf-8")
        write(root, rel, record(code_sha, [finding(1, "rejected")]))
        commit(root, "the record, rejected at the most severe severity")
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_fixed_commit_head_does_not_descend_from(
        self, branch, ready, capsys
    ):
        """S3 (T28): one this repository cannot resolve, and one on another
        branch, are refused by the finding's line and heading; the fixture's
        own code commit is not."""
        root, code_sha = branch
        git(root, "switch", "-q", "main")
        write(root, "g.txt", "elsewhere\n")
        off = commit(root, "a commit the branch never had")
        git(root, "switch", "-q", "feature/x")
        rel = f"{ITEM}/trail/rounds/round-1.md"
        sections = [
            finding(1, "fixed 0000000"),
            finding(2, f"fixed {off[:8]}"),
            finding(3, f"fixed {code_sha[:8]}"),
        ]
        write(root, rel, record(code_sha, sections))
        commit(root, "the record, three fixes")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1
        named = [
            ln
            for ln in out.splitlines()
            if ln.startswith(f"{rel}:") and "does not descend" in ln
        ]
        assert len(named) == 2, out
        assert "### 1." in named[0] and "`0000000`" in named[0]
        assert "### 2." in named[1] and f"`{off[:8]}`" in named[1]
        assert all("HEAD does not descend from" in ln for ln in named), named

    @pytest.mark.rule("round-record-read-by-label")
    @pytest.mark.rule("fix-pass-two-lines")
    @pytest.mark.rule("location-touched-by-fix")
    def test_refuses_a_fixed_commit_that_touches_nothing_of_the_finding(
        self, branch, ready, capsys
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
        rel = f"{ITEM}/trail/rounds/round-1.md"
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
        write(root, rel, record(code_sha, sections))
        commit(root, "the record, seven fixes")
        write(
            root,
            f"{ITEM}/trail/rounds/round-2.md",
            record(
                made["near"],
                confirmations="".join(confirm(f"round-1#{n}") for n in range(1, 8)),
                n=2,
            ),
        )
        commit(root, "the verifying round")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1
        named = [ln for ln in out.splitlines() if ln.startswith(f"{rel}:")]
        assert len(named) == 2, out
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
        self, branch, ready, capsys
    ):
        """S23 (T37): on a ready pull request a `fixed` or `rejected` finding
        in the last record fails as *a verifying round is owed*; a draft
        prints it and passes, and a last record of `deferred` findings
        passes."""
        root, code_sha = branch
        git(root, "rm", "-q", f"{ITEM}/trail/rounds/round-2.md")
        commit(root, "no verifying round")
        seal(root)
        rel = f"{ITEM}/trail/rounds/round-1.md"
        code, out = check(root, capsys)
        assert code == 1
        line = next(ln for ln in out.splitlines() if ln.startswith(f"{rel}:"))
        assert "### 1." in line and chain.VERIFYING_ROUND in line, line
        ready.write_text(json.dumps({"pull_request": {"draft": True}}), "utf-8")
        code, out = check(root, capsys)
        assert code == 0 and chain.VERIFYING_ROUND in out
        ready.write_text(json.dumps({"pull_request": {"draft": False}}), "utf-8")
        write(root, rel, record(code_sha, [finding(1, "deferred #9")]))
        commit(root, "the last record, again")
        seal(root)
        code, out = check(root, capsys)
        assert code == 0 and chain.VERIFYING_ROUND not in out, out

    @pytest.mark.rule("run-ends-with-verifying-round")
    @pytest.mark.rule("last-record-at-head")
    def test_passes_a_last_records_fixed_finding_that_touched_only_its_records(
        self, branch, ready, capsys
    ):
        """S4 of #1148: a `fixed <commit>` of the last record located in the
        work item's own records alone, whose commit touched them alone, owes
        no verifying round; the sealer, which reads every record at HEAD, is
        its reader."""
        root, code_sha = branch
        git(root, "rm", "-q", f"{ITEM}/trail/rounds/round-2.md")
        commit(root, "no verifying round")
        write(root, f"{ITEM}/gaps.md", "# overview\n\nthe row, corrected\n")
        fix = commit(root, "a fix to the records alone")
        rel = f"{ITEM}/trail/rounds/round-1.md"
        located = f"`{ITEM}/gaps.md`"
        write(
            root,
            rel,
            record(code_sha, [finding(1, f"fixed {fix[:8]}", location=located)]),
        )
        commit(root, "the fix pass's verdict")
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out
        assert chain.VERIFYING_ROUND not in out, out

    @pytest.mark.rule("run-ends-with-verifying-round")
    @pytest.mark.rule("last-record-at-head")
    def test_refuses_a_last_records_fixed_finding_that_also_touched_code(
        self, branch, ready, capsys
    ):
        """S4 of #1148: a `fixed <commit>` of the last record whose commit
        touched the records and a path outside them still owes the round,
        refused at the finding's line."""
        root, _code = branch
        git(root, "rm", "-q", f"{ITEM}/trail/rounds/round-2.md")
        commit(root, "no verifying round")
        write(root, f"{ITEM}/gaps.md", "# overview\n\nthe row, corrected\n")
        write(root, "f.txt", "three\n")
        fix = commit(root, "a fix to the records and the code")
        rel = f"{ITEM}/trail/rounds/round-1.md"
        located = f"`f.txt:1`, `{ITEM}/gaps.md`"
        write(
            root, rel, record(fix, [finding(1, f"fixed {fix[:8]}", location=located)])
        )
        commit(root, "the fix pass's verdict")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1, out
        line = next(
            ln for ln in out.splitlines() if ln.startswith(f"{rel}:") and "### 1." in ln
        )
        assert chain.VERIFYING_ROUND in line, line

    @pytest.mark.rule("run-ends-with-verifying-round")
    @pytest.mark.rule("last-record-at-head")
    def test_refuses_a_last_records_code_finding_fixed_in_its_records_alone(
        self, branch, ready, capsys
    ):
        """S4 of #1148: a finding that names a path outside the records owes
        the round, even where its `fixed` commit touched only the records,
        since no round would read its code half."""
        root, code_sha = branch
        git(root, "rm", "-q", f"{ITEM}/trail/rounds/round-2.md")
        commit(root, "no verifying round")
        write(root, f"{ITEM}/gaps.md", "# overview\n\nthe row, corrected\n")
        fix = commit(root, "the record half alone")
        rel = f"{ITEM}/trail/rounds/round-1.md"
        located = f"`f.txt:1`, `{ITEM}/gaps.md`"
        write(
            root,
            rel,
            record(code_sha, [finding(1, f"fixed {fix[:8]}", location=located)]),
        )
        commit(root, "the fix pass's verdict")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1, out
        line = next(
            ln for ln in out.splitlines() if ln.startswith(f"{rel}:") and "### 1." in ln
        )
        assert chain.VERIFYING_ROUND in line, line

    @pytest.mark.rule("last-record-at-head")
    def test_refuses_a_code_commit_after_the_last_record(self, branch, ready, capsys):
        """S4 (T12): a record commit after the last record passes; a code
        commit after it fails naming the commit and the verifying round."""
        root, _code = branch
        write(root, f"{ITEM}/gaps.md", "# overview\n")
        commit(root, "a record commit")
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out
        write(root, "f.txt", "three\n")
        later = commit(root, "a fix after the last round")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1
        assert later[:8] in out and "a verifying round is owed" in out

    def test_refuses_a_chain_with_no_record_and_prints_it_on_a_draft(
        self, branch, ready, capsys
    ):
        root, _code = branch
        git(root, "rm", "-rq", f"{ITEM}/trail/rounds")
        commit(root, "no record")
        code, out = check(root, capsys)
        assert code == 1 and "holds no `round-N.md`" in out
        ready.write_text(json.dumps({"pull_request": {"draft": True}}), "utf-8")
        code, out = check(root, capsys)
        assert code == 0 and "holds no `round-N.md`" in out

    def test_names_a_line_it_did_not_read_as_a_notice_and_keeps_the_exit(
        self, branch, ready, capsys, monkeypatch
    ):
        """#1198's scenario *A near opener*: a fence opened by three
        backticks and `Seal` is printed `path:line  not read: <why>`, and in
        CI as a notice annotation, never an error, and the exit code is the
        one the record's blocks give: 0 where the near fence stands in a
        finding's prose, 1 where it was the finding's only block, refused at
        the heading."""
        root, code_sha = branch
        rel = f"{ITEM}/trail/rounds/round-1.md"
        near = FENCE + "Seal"
        text = record(code_sha, [finding(1, f"fixed {code_sha[:8]}")]).replace(
            "\nWhy it matters.", f"\n{near}\nverdict: fixed\n{FENCE}\n\nWhy it matters."
        )
        write(root, rel, text)
        commit(root, "a fence like a block in the prose")
        seal(root)
        number = line_at(text, near)
        said = chain.FIELDS.NEAR.format(line=near)
        assert said.startswith("not read: "), said
        code, out = check(root, capsys)
        assert code == 0, out
        assert [ln for ln in out.splitlines() if "not read" in ln] == [
            f"{rel}:{number}  {said}"
        ], out
        monkeypatch.setenv("GITHUB_ACTIONS", "true")
        code, out = check(root, capsys)
        assert code == 0, out
        assert [ln for ln in out.splitlines() if "not read" in ln] == [
            f"::notice file={rel},line={number}::{said}"
        ], out
        monkeypatch.delenv("GITHUB_ACTIONS")
        only = record(code_sha, [finding(1, f"fixed {code_sha[:8]}")]).replace(
            f"{FENCE}seal\nseverity:", f"{near}\nseverity:"
        )
        write(root, rel, only)
        commit(root, "the finding's only block, opened otherwise")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1, out
        heading = "### 1. the parser drops a row"
        assert (
            f"{rel}:{line_at(only, heading)}  {heading} {chain.DASH} "
            f"{chain.NO_FINDING_BLOCK}"
        ) in out.splitlines(), out
        assert f"{rel}:{line_at(only, near)}  {said}" in out.splitlines(), out

    def test_names_no_line_inside_a_fence(self, branch, ready, capsys):
        """A paste-ready fix block quoting a near opener and a `verdict:`
        line prints no `not read:` line, and the exit code is the clean
        record's: a fence inside another fence is that fence's."""
        root, code_sha = branch
        rel = f"{ITEM}/trail/rounds/round-1.md"
        text = record(code_sha, [finding(1, f"fixed {code_sha[:8]}")])
        quoted = f"{FENCE}`markdown\n{FENCE}Seal\nverdict: open\n{FENCE}\n{FENCE}`"
        write(root, rel, text.replace(f"{FENCE}python\nx = 1\n{FENCE}", quoted))
        commit(root, "a fix block that quotes a verdict line")
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out
        assert [ln for ln in out.splitlines() if "not read" in ln] == [], out

    def test_names_a_record_under_another_name_and_keeps_the_exit(
        self, branch, ready, capsys
    ):
        """The second scenario of #1167, #1121's R11: `Round-2.md` beside a
        clean `round-1.md` is named on one line as a file the check did not
        read, and the exit code is the one the clean record gives. Seen red
        against the reader that kept the files `round_number` matches and
        printed nothing of the rest."""
        root, code_sha = branch
        rounds = f"{ITEM}/trail/rounds"
        git(root, "rm", "-q", f"{rounds}/round-2.md")
        clean = record(code_sha, [finding(1, "deferred #9")])
        write(root, f"{rounds}/round-1.md", clean)
        commit(root, "one clean record")
        seal(root)
        code, before = check(root, capsys)
        assert code == 0, before
        write(root, f"{rounds}/Round-2.md", clean)
        commit(root, "a copy under another name")
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out
        said = chain.UNREAD_FILE.format(name="Round-2.md")
        assert [ln for ln in out.splitlines() if "Round-2.md" in ln] == [
            f"{rounds}/Round-2.md:0  {said}"
        ], out

    @pytest.mark.rule("old-table-shape-refused")
    def test_refuses_an_old_shape_record_and_an_unclosed_fence(
        self, branch, ready, capsys
    ):
        """S11 and #1198's scenario *A record from before the change*: a
        record of an older shape under the declared item, the table's and
        the labelled lines', holds no round block and is refused with one
        line naming the template; a fence the proofer never closed hides the
        open finding below it and is named at its opener."""
        root, code_sha = branch
        rel = f"{ITEM}/trail/rounds/round-1.md"
        for old in (OLD_RECORD.replace("0000000", code_sha), LABELLED):
            write(root, rel, old)
            commit(root, "an old-shape record")
            seal(root)
            code, out = check(root, capsys)
            assert code == 1
            assert [ln for ln in out.splitlines() if ln.startswith(f"{rel}:")] == [
                f"{rel}:0  {chain.NO_ROUND_BLOCK}"
            ], out
        text = record(
            code_sha,
            [finding(1, "rejected") + "\n~~~python\n", finding(2, "open")],
        )
        write(root, rel, text)
        commit(root, "a record with a fence left open")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1, out
        opener = text.splitlines().index("~~~python")
        assert f"{rel}:{opener + 1}" in out, out

    def test_refuses_a_broad_gate_file_naming_another_commit(
        self, branch, ready, capsys
    ):
        """S5 (T15): the newest run must be HEAD or have only records after
        it; a stale run fails naming the file, and `--sealing` prints it."""
        root, _code = branch
        rel = f"{ITEM}/trail/gate.md"
        write(root, rel, gate_file("1" * 40))
        commit(root, "a run this repository cannot see")
        code, out = check(root, capsys)
        assert code == 1
        assert any(ln.startswith(f"{rel}:") for ln in out.splitlines())
        code, out = check(root, capsys, "--sealing")
        assert code == 0 and rel in out

    @pytest.mark.rule("two-review-answers")
    def test_refuses_a_straight_to_the_pr_item_without_the_sealers_two_files(
        self, branch, ready, capsys
    ):
        root, _code = branch
        write(
            root,
            f"{ITEM}/routing.md",
            ROUTING.format(review="straight to the PR", planning="the session"),
        )
        git(
            root,
            "rm",
            "-rq",
            f"{ITEM}/trail/rounds",
            f"{ITEM}/trail/gate.md",
            f"{ITEM}/guarantee.md",
        )
        commit(root, "direct, and no run")
        code, out = check(root, capsys)
        assert code == 1 and "trail/gate.md" in out and "guarantee.md" in out
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out

    def test_refuses_an_unreadable_declaration_and_accepts_none(
        self, branch, ready, capsys
    ):
        root, _code = branch
        write(root, f"{ITEM}/routing.md", "# nothing to read\n")
        commit(root, "garbled")
        code, out = check(root, capsys)
        assert code == 1 and "not a readable declaration" in out
        git(root, "rm", "-rq", ITEM)
        commit(root, "no work item")
        code, out = check(root, capsys)
        assert code == 0 and "declared neither way" in out

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
        monkeypatch.setenv("GITHUB_HEAD_REF", RELEASE)
        code, out = check(root, capsys)
        assert code == 0, out
        line = next(ln for ln in out.splitlines() if f"{ITEM}/routing.md" in ln)
        assert "judged at its own pull request" in line and "(#7)" in line
        assert "does not descend from" not in out
        monkeypatch.setenv("GITHUB_HEAD_REF", "feature/x")
        code, out = check(root, capsys)
        assert code == 1 and "does not descend from" in out
        assert "judged at its own pull request" not in out
        monkeypatch.setenv("GITHUB_HEAD_REF", RELEASE)
        rel = f"{ITEM}/routing.md"
        write(root, rel, (root / rel).read_text(encoding="utf-8") + "\nA note.\n")
        commit(root, "a change on the release branch itself (#8)")
        code, out = check(root, capsys)
        assert code == 1
        assert "does not descend from" in out
        assert "judged at its own pull request" not in out

    def test_refuses_a_baseline_that_does_not_resolve_with_exit_2(self, branch, capsys):
        root, _code = branch
        code = chain.main(["--baseline", "no-such-ref", "--root", str(root)])
        assert code == 2
        assert "does not resolve" in capsys.readouterr().err


# --- retired ------------------------------------------------------------------------

OLD_ITEM = "seal/threads/1788000000-an-earlier-item"


def remove_an_earlier_item(root, applied, whole=True, open_row=False):
    """Declare an earlier work item on `main`, bring it into the branch, and
    remove its directory there, or only its declaration, with or without its
    rule change applied, and with or without an open row in its record."""
    git(root, "switch", "-q", "main")
    # Close enough to the branch's own declaration for git's rename detection
    # to pair the two, which `changed` reads without.
    write(
        root,
        f"{OLD_ITEM}/routing.md",
        ROUTING.format(review="straight to the PR", planning="the session"),
    )
    write(
        root,
        f"{OLD_ITEM}/frame/design.md",
        "# a spec\n\n## Rule changes\n\n- add\n  file: docs/policy.md\n  to: A rule.\n",
    )
    if open_row:
        write(
            root,
            f"{OLD_ITEM}/gaps.md",
            "# x\n\n## Not verified\n\n| Item | Who must answer |\n|---|---|\n"
            "| a claim nobody ran | the repository owner |\n",
        )
    commit(root, "an earlier item, declared")
    git(root, "switch", "-q", "feature/x")
    git(root, "merge", "-q", "--no-edit", "main")
    git(root, "rm", "-rq", OLD_ITEM if whole else f"{OLD_ITEM}/routing.md")
    if applied:
        write(root, "docs/policy.md", "A rule.\n")
    commit(root, "the earlier item leaves")


@pytest.mark.rule("a-declaration-removed")
class Test_retired:
    @pytest.mark.parametrize(
        "applied, open_row",
        [(False, True), (True, False)],
        ids=["an-open-row-and-no-rule-in-docs", "a-closed-record-and-its-rule-in-docs"],
    )
    def test_accepts_a_declaration_a_settle_removed(
        self, branch, draft, capsys, applied, open_row
    ):
        """S6 of #1033: a `routing.md` whose whole directory stood at the
        merge base and is gone is a settle, whatever its record held there and
        whatever `docs/` holds of its spec. The notice says what was read."""
        root, _code = branch
        remove_an_earlier_item(root, applied=applied, open_row=open_row)
        _code, out = check(root, capsys)
        assert f"{OLD_ITEM}/routing.md:0  {chain.SETTLE_SAYS}" in out, out
        # Contract rule 14: the words a person reads, not only the constant.
        assert (
            "retired: a settle — the work item's directory stood at the merge "
            "base and is gone whole"
        ) in out, out
        assert "does not carry this file at HEAD" not in out

    def test_refuses_a_declaration_deleted_beside_a_directory_that_stays(
        self, branch, draft, capsys
    ):
        """S8: a `routing.md` deleted beside a `frame/design.md` that stays is a
        deletion: a settle takes the whole directory."""
        root, _code = branch
        remove_an_earlier_item(root, applied=True, whole=False)
        _code, out = check(root, capsys)
        assert "does not carry this file at HEAD" in out
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

    @pytest.mark.rule("nothing-declared-nothing-owed")
    def test_accepts_under_worktree_a_root_the_working_tree_no_longer_has(
        self, branch, ready, capsys, tmp_path
    ):
        """Round 3 of #952, finding 2: a switch to local mode, run and not
        committed, leaves no `seal` in the working tree, so under `--worktree`
        nothing is declared, as CI reads the same change once it is committed."""
        root, _code = branch
        remove_an_earlier_item(root, applied=False)
        shutil.move(str(root / "seal"), str(tmp_path / "moved-seal"))
        git(root, "add", "-A", "seal")
        code, out = check(root, capsys, "--worktree")
        assert code == 0, out
        assert "so nothing is declared" in out
        assert "does not carry this file at HEAD" not in out

    def test_judges_a_root_the_working_tree_has_under_worktree(
        self, branch, ready, capsys
    ):
        """Round 2 of #952, finding 2: under `--worktree` the tree the check
        reads is the working tree, so a root it holds and HEAD does not is a
        root, and the declaration naming the branch in it is judged."""
        root, _code = branch
        git(root, "rm", "-rq", "--cached", "seal")
        git(root, "commit", "-qm", "the root leaves HEAD and stays on disk")
        code, out = check(root, capsys, "--worktree")
        assert "so nothing is declared" not in out, out
        assert code == 1 and f"{ITEM}/guarantee.md:0  the guarantee is behind" in out

    def test_judges_the_declarations_where_the_working_tree_has_seal_as_a_file(
        self, branch, ready, capsys
    ):
        """Round 2 of #952, finding 3: a `seal` that is not a directory is
        still an entry, so under `--worktree` the declarations it replaced
        stay judged."""
        root, _code = branch
        shutil.rmtree(root / "seal")
        write(root, "seal", "not a root\n")
        code, out = check(root, capsys, "--worktree")
        assert "so nothing is declared" not in out, out
        assert code == 0 and f"{MERGED_ITEM}/routing.md:0  retired: a settle" in out


class Test_module:
    def test_every_reader_of_a_retirement_calls_the_one_predicate(self):
        """Two parties ask whether a removed directory was settled,
        `seal unverified --baseline` and this one, and a predicate spelled in
        each would take the next condition in one and not the other. The
        behaviour is pinned per reader in its own module; this pins that this
        one reaches the answer by calling `settled` on the module that owns
        it, so a reader that re-derives the rule inline goes red here even
        while it agrees today. `settle` asks no predicate since #1033: it
        reads the open rows of the working tree."""
        import ast

        script = TARGET.split("/")
        with open(os.path.join(ROOT, *script), encoding="utf-8") as f:
            tree = ast.parse(f.read())
        calls = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "settled"
        ]
        assert calls, (
            f"{'/'.join(script)} decides a removal without asking the predicate"
        )
        assert not [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef) and node.name == "settled"
        ], f"{'/'.join(script)} defines a second `settled`"

    @pytest.mark.parametrize(
        "args, purpose, absent",
        [(["--baseline", "HEAD", "--root", "{root}"], "the shared reader", None)],
        ids=["unverified_check.py"],
    )
    def test_a_script_copied_alone_exits_2_and_names_what_it_misses(
        self, tmp_path, args, purpose, absent
    ):
        """#590. A copy of this script taken without its siblings exits 2, with
        a sentence naming the missing path and what it is for: 2 means the
        input or the tree was unusable and nothing was read, and a sibling that
        is not beside the command is that kind. It loads the shared reader at
        import and `hooks/lib/routing.py` after argument parsing, so it is given
        its one required flag. It quotes the `OSError`, whose path Windows
        repr-escapes, which `names_path` reads."""
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
        assert "Traceback" not in done.stderr, done.stderr
        assert names_path(str(alone), done.stderr), (
            f"the refusal does not name the missing path: {done.stderr}"
        )
        assert purpose in done.stderr, (
            f"the refusal does not say what the missing file is for: {done.stderr}"
        )
        if absent:
            assert absent not in done.stderr, done.stderr

    def test_the_framers_mark_is_the_last_line_a_renderer_shows(self):
        """S10 of #664. The mark stands after a U+2028 on the file's last line,
        which GFM does not end a line at, so the last line does not begin with
        one."""
        spec = f"# spec\n\nprose{LS}Framed 2026-01-01 by framer, before the build.\n"
        assert chain.frame_foot(reader, spec)[0] is None
        whole = "# spec\n\nprose\nFramed 2026-01-01 by framer, before the build.\n"
        assert chain.frame_foot(reader, whole)[0] == ("2026-01-01", "framer")

    def test_loads_beside_no_policy_document(self, tmp_path):
        """*Scope* item 5 of #1198: the round record's grammar is
        `hooks/lib/fields.py`, so the check loads and reads a record with no
        `docs/` beside it. Seen red against the check that loaded its grammar
        table from `docs/the-review-record.md` at import, which raised
        "cannot be read"."""
        script = copied_tree(tmp_path / "tree")
        assert not (tmp_path / "tree" / "docs").exists()
        loaded = load(script, "chain_check_beside_no_document")
        found, errors = loaded.record_findings(
            reader, record("abc1234", [finding(1, "rejected")]), "r.md"
        )
        assert (errors, [f.verdict for f in found]) == ([], [(chain.REJECTED, None)])


# --- left where they stand, for #923: they read the shipped documents --------------


def test_the_proofer_and_the_review_skill_name_every_line_a_finding_needs():
    """S8 (#985), under #1198: `agents/proofer.md` step 7 and
    `skills/code-review/SKILL.md` *The record* each list the lines a
    finding's block carries, and each names every key a finding block holds
    one of, read from `hooks/lib/fields.py`. Neither has the proofer write a
    `verdict:` line, which a finding with no close block no longer carries,
    and step 7 says a prose line opening with `<` and a letter hides the
    blocks below it from the reader (`trail/phases/phase-2.md` of #1198)."""
    kind = chain.FIELDS.FINDING_BLOCK
    needed = [key for key, spec in kind.keys.items() if spec.many == chain.FIELDS.ONE]
    assert "evidence:" in needed, needed
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
        assert missing == [], f"{where} does not name {missing}"
        assert "`verdict: open`" not in text, f"{where} still writes `verdict: open`"
    assert "opens with `<` and a letter" in step, step


def test_the_review_skill_sends_a_value_s_form_to_the_module_and_to_no_row():
    """Round 3 of #1198, finding 1: `skills/code-review/SKILL.md` *The
    record* names `hooks/lib/fields.py` as the one statement of each value's
    shape, so no sentence of the section sends the proofer to a grammar row
    or table, which the docs grammar the settle removes is the only one of.
    Seen red against the `evidence:` bullet that said "the forms its row
    gives"."""
    skill = " ".join(
        (ROOT / "skills" / "code-review" / "SKILL.md").read_text("utf-8").split()
    )
    record = skill.split("## The record ", 1)[1].split("**Paste-ready", 1)[0]
    # The section's other rows are a config row and a `## Not judged` row.
    for gone in ("its row", "grammar row", "grammar table", "the table"):
        assert gone not in record, f"*The record* still says {gone!r}"
    assert (
        "`evidence:` names what the claim rests on, in the forms "
        "`hooks/lib/fields.py` gives its value." in record
    ), record


def test_the_template_is_the_record_the_check_reads():
    """S1 (T29, T38): `templates/records/sdd-round.md` is a record the check
    reads: one round block and no table above the findings; one finding
    whose block locates it at one coordinate, rests on one `evidence:` line
    and names the regression `round-1#1`, with its close block after the fix
    fence, `fixed` at a commit the fix pass names; a close written inside
    the fix block not read as one; `## Confirmations` holding its two
    example blocks; no `reopens:` line and no `original:` line, with the
    review skill saying where a `reopens:` finding's grounds open; the
    record document naming the stand-in for a backtick; and no emoji
    anywhere."""
    text = TEMPLATE.read_text(encoding="utf-8")
    read, errors = chain.round_of(reader, text, "t", 1)
    assert errors == []
    assert [(f.verdict, f.paths, f.regression, f.reopens) for f in read.findings] == [
        ((chain.FIXED, "1a2b3c4"), ["path"], (1, 1), None)
    ]
    assert text.count("\nevidence: ") == 1
    assert "\nreopens: " not in text and "\noriginal: " not in text
    skill = (ROOT / "skills" / "code-review" / "SKILL.md").read_text("utf-8")
    assert "where `reopens:` stands" in " ".join(skill.split())
    stand_in = "with `$(printf '\\140')` in place of the character"
    assert stand_in in " ".join(DOC.read_text(encoding="utf-8").split())
    assert read.findings[0].heading.startswith("### 1. ")
    assert read.findings[0].number == 1
    assert [ref for _line, ref in read.confirms] == [(1, 2)]
    assert text.count("\nconfirms: ") == 2 and "\nconfirms: none\n" in text
    head = text.split(chain.FINDINGS_HEADING)[0]
    assert chain.table_rows(reader, reader.readable(head)) == []
    assert read.target == "1a2b3c4"
    start = text.index(FENCE + "seal\nverdict: ")
    end = text.index(FENCE + "\n", start + len(FENCE)) + len(FENCE) + 1
    without = text[:start] + text[end:]
    fix = without.index(FENCE + "<lang>\n") + len(FENCE + "<lang>\n")
    quoted = without[:fix] + "verdict: rejected\nanswer: x\n" + without[fix:]
    found, errors = chain.record_findings(reader, quoted, "t")
    assert errors == [] and [f.verdict for f in found] == [(chain.OPEN, None)]
    assert [c for c in text if EMOJI.match(c)] == []


test_census = census_case(TARGET)

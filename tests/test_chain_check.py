"""`skills/code-review/scripts/chain_check.py`, one class per function.

Rebuilt by #942's phase 5. The readers of a round record, the grammar table
and the reference channel run in the process on text. `main` runs in the
process over a repository built once for the module and copied for each
case that judges it: a branch with a routing declaration, a code commit, two
round records and the closing records, judged as a ready or a draft pull
request through the event payload GitHub writes. Each copy is the reset.
`Test_module` holds the case that reads this module's source for a call of
`unverified_check.py#settled` and no second definition of it, which #942
moved from `tests/test_unverified_rows_close.py`; the copy run without its
siblings, from `tests/test_a_script_copied_alone_exits_2.py`; and the
framer's mark after a U+2028, `frame_foot`'s one case, from
`tests/test_every_reader_ends_a_line_where_gfm_does.py`. The last two came in
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

import pytest
from conftest import (
    BASELINE,
    LS,
    census_case,
    chain_check_run,
    names_path,
    parity_file,
    write,
)
from conftest import commit_everything as commit
from conftest import git_out as git
from conftest import load_module as load

TARGET = "skills/code-review/scripts/chain_check.py"

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHAIN = ROOT / TARGET
READER = ROOT / "skills" / "verify" / "scripts" / "unverified_check.py"
ITEM = "seal/specs/1791999999-a-work-item"
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
    """One `### ` section of `## Findings`, in `templates/sdd-round.md`'s
    shape, its `verdict:` line reading `verdict` and its `evidence:` line
    `evidence`, or none where that is None."""
    return (
        f"### {n}. {title}\n\n"
        f"severity: {severity}\n"
        f"location: {location}\n"
        + (f"evidence: {evidence}\n" if evidence is not None else "")
        + f"verdict: {verdict}\n"
        + (f"regression: {regression}\n" if regression else "")
        + (f"reopens: {reopens}\n" if reopens else "")
        + "\nWhy it matters.\n\n"
        "```python\nx = 1\n```\n\n"
        "answer: \n"
    )


def confirm(reference, what="the fix holds"):
    """One entry of `## Confirmations`: its `confirms:` line reading
    `reference`, then the prose saying what holds, where and how."""
    return f"confirms: {reference}\n{what}, at `f.txt:1`. read.\n\n"


def record(target, findings=(), confirmations="", n=1):
    """A round record in `templates/sdd-round.md`'s shape: `findings` are
    `finding()` sections, `confirmations` entries of `## Confirmations`."""
    return (
        f"# 1791999999-a-work-item — review round {n}\n\n"
        f"target: {target} against main\n\n"
        "## Findings\n\n" + "\n".join(findings) + "\n## Confirmations\n\n"
        f"{confirmations}\n"
        "## Not judged\n\n"
        "| What | Location | Who answers |\n|---|---|---|\n\n"
        "## Probes\n\n"
        "| Command | Result |\n|---|---|\n"
    )


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
MERGED_ITEM = "seal/specs/1788999999-a-merged-item"


def gate_file(sha):
    return (
        "# 1791999999-a-work-item — broad gate\n\n"
        "| Field | Value |\n|---|---|\n"
        f"| Broad gate | {sha} against main |\n"
    )


def guarantee_file(sha, verdict="sealed"):
    return (
        "# 1791999999-a-work-item — guarantee\n\n"
        "| Field | Value |\n|---|---|\n"
        f"| Target SHA | {sha} against main |\n\n"
        f"Verdict: {verdict}\n"
    )


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
    write(d, f"{MERGED_ITEM}/rounds/round-1.md", OLD_RECORD)
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
        d, f"{ITEM}/rounds/round-1.md", record(code, [finding(1, f"fixed {code[:8]}")])
    )
    commit(d, "the round record")
    write(
        d,
        f"{ITEM}/rounds/round-2.md",
        record(code, confirmations=confirm("round-1#1"), n=2),
    )
    reviewed = commit(d, "the verifying round")
    # Two runs, newest first: the earlier one names a commit nobody can see,
    # so a reader that took any run but the first would refuse the file.
    write(
        d,
        f"{ITEM}/broad-gate.md",
        gate_file(f"{reviewed} against main; earlier run: {'1' * 40}"),
    )
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
    write(d, f"{ITEM}/broad-gate.md", gate_file(f"{head} against main"))
    write(d, f"{ITEM}/guarantee.md", guarantee_file(head))
    commit(d, "the closing records, again")


def event(tmp_path, monkeypatch, draft):
    path = tmp_path / "event.json"
    path.write_text(json.dumps({"pull_request": {"draft": draft}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(path))
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    monkeypatch.delenv("GITHUB_HEAD_REF", raising=False)
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
    write(d, "seal/specs/1788000000-old/routing.md", old)
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
            "seal/specs/1788000000-old/routing.md",
            "seal/specs/1788000000-moved/routing.md",
        }
        os.rename(d / "seal/specs/1788000000-old", d / "seal/specs/1788000000-moved")
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
        git(d, "rm", "-q", "seal/specs/1788000000-old/routing.md")
        write(
            d,
            "seal/specs/1791999999-new/routing.md",
            old.replace("feature/x", "feature/y"),
        )
        commit(d, "one leaves, one arrives")
        paths, renamed = chain.changed(str(d), "main")
        assert renamed == set()
        assert sorted(paths) == [
            "seal/specs/1788000000-old/routing.md",
            "seal/specs/1791999999-new/routing.md",
        ]


class Test_changed_routing:
    def test_accepts_every_declaration_added_changed_or_deleted(self):
        paths = [
            "seal/specs/1/routing.md",
            "seal/specs/2/routing.md",
            "seal/specs/2/spec.md",
            "docs/routing.md",
        ]
        assert chain.changed_routing(paths, set(), "seal/specs") == [
            "seal/specs/1/routing.md",
            "seal/specs/2/routing.md",
        ]

    def test_refuses_a_declaration_the_pull_request_only_moved(self):
        moved = {"seal/specs/1/routing.md", "seal/specs/3/routing.md"}
        assert chain.changed_routing(sorted(moved), moved, "seal/specs") == []


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
        assert chain.carried_by(str(root), "main", "seal/specs/none/routing.md") is None


# --- grammar ------------------------------------------------------------------------

DOC = ROOT / "docs" / "the-review-record.md"
TEMPLATE = ROOT / "templates" / "sdd-round.md"


def doc_with(tmp_path, old, new):
    """The grammar document with `old`, which stands once, replaced by `new`,
    written to a path of its own."""
    text = DOC.read_text(encoding="utf-8")
    assert text.count(old) == 1, old
    path = tmp_path / "the-review-record.md"
    path.write_text(text.replace(old, new), encoding="utf-8")
    return path


def row_of(key):
    """The table row of `key` as the document writes it, its line end
    included."""
    return next(
        ln + "\n"
        for ln in DOC.read_text(encoding="utf-8").splitlines()
        if ln.startswith(f"| `{key}` |")
    )


def readings(rows):
    """`rows` as plain values, so two loads of one table compare equal."""
    return {
        k: (r.shape.pattern if r.shape else None, r.where, r.many, r.refused)
        for k, r in rows.items()
    }


# Each way a table the check cannot read is broken, and what the refusal says.
BROKEN = [
    ("## The round record\n", "## The round records\n", "0 `## The round record`"),
    ("| How many |", "| Count |", "holds no table headed"),
    ("|---|---|---|---|---|\n| `target:`", "| `target:`", "separator row"),
    (" | a severity is `must` or `should` |", " |", "4 cells"),
    ("| `severity:` |", "| severity: |", "not one code span"),
    ("| `severity:` |", "| `severity:` `x` |", "not one code span"),
    ("(?:must\\|should)`", "(?:must\\|should`", "does not compile"),
    ("| a finding | one | a severity", "| a section | one | a severity", "cannot read"),
    ("| a finding | one | a severity", "| a finding | two | a severity", "cannot read"),
    (row_of("reopens:"), "", "no `reopens:` row"),
    ("`target: (?P<commit>", "`target: (?P<sha>", "no `(?P<commit>…)`"),
    ("| Old spelling | Means |", "| Old | Means |", "no table headed"),
    ("| Old spelling | Means |", "| Old spelling | Meaning |", "no table headed"),
    ("| `refixes:` | `regression:` |", "| refixes: | `regression:` |", "code span"),
    (
        "| `refixes:` | `regression:` |",
        "| `refixes:` | `regression:` `x` |",
        "code span",
    ),
    (
        "| `refixes:` | `regression:` |",
        "| `refixes:` | `regressed:` |",
        "no label of the grammar table",
    ),
    (
        "| `refixes:` | `regression:` |",
        "| `refixes:` | `## Findings` |",
        "no label of the grammar table",
    ),
    (
        "| `refixes:` | `regression:` |",
        "| `answer:` | `regression:` |",
        "`answer:` is a label of the grammar table",
    ),
    (
        "| `refixes:` | `regression:` |",
        "| `refixes:` | `regression:` |\n| `refixes:` | `regression:` |",
        "a second `refixes:` old spelling",
    ),
    (
        "| `refixes:` | `regression:` |",
        "| `refixes` | `regression:` |",
        "an old spelling is a label",
    ),
    (
        row_of("answer:"),
        row_of("answer:") + "| `Answer:` | — | nowhere | none | x |\n",
        "not one code span",
    ),
    (
        row_of("answer:"),
        row_of("answer:") + "| `said:` | `said: .+` | nowhere | one | x |\n",
        "cannot read",
    ),
    ("`severity: (?:must", "`sev: (?:must", "cannot read"),
    (row_of("severity:"), row_of("severity:") * 2, "a second `severity:` row"),
    (
        row_of("answer:"),
        row_of("answer:") + "| `## Probes` | `## Probes` | the record | one | x |\n",
        "reads nothing from",
    ),
    (
        "| a finding | one | a verdict is",
        "| a finding | any | a verdict is",
        "`verdict:` row's `How many` is `any`, and the check can honour only `one`",
    ),
    (
        "| a finding | one | a verdict is",
        "| a finding | at most one | a verdict is",
        "`How many` is `at most one`, and the check can honour only `one`",
    ),
    (
        "| a finding | one | a location is",
        "| a finding | at most one | a location is",
        "`location:` row's `How many` is `at most one`",
    ),
    (
        "| outside every finding | one | it names",
        "| outside every finding | any | it names",
        "`target:` row's `How many` is `any`",
    ),
    (
        "| a finding | at most one | a reference is",
        "| a finding | any | a reference is",
        "`regression:` row's `How many` is `any`, and the check can honour only "
        "`one` or `at most one`",
    ),
    (
        "| a finding | at most one | a reopened close",
        "| a finding | any | a reopened close",
        "`reopens:` row's `How many` is `any`",
    ),
    (
        "| outside every finding | at most one | it names the migration",
        "| outside every finding | one | it names the migration",
        "`original:` row's `How many` is `one`, and the check can honour only "
        "`at most one`",
    ),
    (
        "| a finding | one | a verdict is",
        "| outside every finding | one | a verdict is",
        '`verdict:` row stands "outside every finding", and the check reads it '
        'only where the table says "a finding"',
    ),
    (
        "| outside every finding | one | it names",
        "| a finding | one | it names",
        '`target:` row stands "a finding"',
    ),
    (
        "| `## Confirmations` | any | it is",
        "| a finding | any | it is",
        '`confirms:` row stands "a finding"',
    ),
]


class Test_grammar:
    def test_accepts_the_table_and_reads_every_line_against_its_row_whole(
        self, monkeypatch, tmp_path
    ):
        """S4 (T2): the table in `docs/the-review-record.md` *The round
        record* is what the check reads: its rows are the nine labels, the
        finding heading, the two sections and the three old spellings, and
        the module's grammar is the document's, read again here. Every line
        `templates/sdd-round.md` writes of a row matches it whole, and the
        same line with a word after it is refused wherever the row's shape
        ends in fixed words. A row changed in the document changes what the
        readers accept, so no constant stands beside the table."""
        assert set(chain.GRAMMAR) == {
            "target:",
            "original:",
            "severity:",
            "location:",
            "evidence:",
            "verdict:",
            "regression:",
            "reopens:",
            "answer:",
            "confirms:",
            "### <n>. <symptom>",
            "## Findings",
            "## Confirmations",
        }, chain.GRAMMAR
        assert chain.OLD_SPELLINGS == {
            "Target SHA:": "target:",
            "refixes:": "regression:",
            "fix of a fix:": "regression:",
        }, chain.OLD_SPELLINGS
        rows, old = chain.grammar(str(DOC), reader)
        assert readings(rows) == readings(chain.GRAMMAR)
        assert old == chain.OLD_SPELLINGS
        cells = [c for r in readings(rows).values() for c in r] + [*old.items()]
        assert not [c for c in cells if chain.DASH in str(c)], cells

        lines = reader.readable(TEMPLATE.read_text(encoding="utf-8"))
        # The template writes neither the `reopens:` line nor the `original:`
        # one, each owed only where its condition holds (#988).
        conditional = {
            "reopens:": ["reopens: round-1#2"],
            "original:": ["original: 1a2b3c4"],
        }
        for key in chain.LABELS:
            row = chain.GRAMMAR[key]
            written = [ln for ln in lines if chain.label_of(ln) == key]
            written = written or conditional.get(key, [])
            assert written, f"the template writes no `{key}` line"
            for ln in written:
                assert row.shape.fullmatch(ln), ln
                trailing = row.shape.fullmatch(f"{ln} and more")
                assert bool(trailing) == (key == "answer:"), ln
        headings = [ln for ln in lines if ln.startswith("### ")]
        assert headings and all(chain.finding_number(h) == 1 for h in headings)
        for key in chain.SECTION_ROWS:
            assert len(chain.sections_of(reader, lines, key)) == 1, key

        could = record("abc1234", [finding(1, "rejected", severity="could")])
        assert chain.record_findings(reader, could, "r.md")[1] != []
        wider = doc_with(
            tmp_path,
            "`severity: (?:must\\|should)`",
            "`severity: (?:must\\|should\\|could)`",
        )
        monkeypatch.setattr(chain, "GRAMMAR", chain.grammar(str(wider), reader)[0])
        assert chain.record_findings(reader, could, "r.md")[1] == []

    @pytest.mark.parametrize("old, new, said", BROKEN)
    def test_refuses_a_document_it_cannot_read_naming_it(
        self, tmp_path, old, new, said
    ):
        """S4 (T2): a table the check cannot read stops it and is never a
        pass: no section, no header, no separator, a row of the wrong width,
        a `Line` that is no code span, a shape that does not compile, a
        `Where` or `How many` the table does not use, a row the check reads
        missing or naming no part it reads, an old-spellings table it cannot
        read (S12 of #1000), a label whose shape does not open with it, a row
        twice, a heading row the check reads nothing from, and a row the check
        reads a meaning from standing where its reader does not look or
        allowing a `How many` that reader cannot keep."""
        path = doc_with(tmp_path, old, new)
        with pytest.raises(chain.GrammarError) as refused:
            chain.grammar(str(path), reader)
        assert str(refused.value).startswith(str(path)), refused.value
        assert said in str(refused.value), refused.value

    def test_refuses_to_run_beside_a_document_it_cannot_read_with_exit_2(
        self, tmp_path
    ):
        """Run as a command beside a broken document, the check exits 2 with
        that sentence and no traceback, and beside no document the same;
        imported, it raises the error for the importer to decide."""
        old, new, said = BROKEN[7]
        path = doc_with(tmp_path, old, new)
        with pytest.raises(chain.GrammarError, match="cannot be read"):
            chain.grammar(str(tmp_path / "no-such-document.md"), reader)
        tree = tmp_path / "tree"
        script = tree / "skills" / "code-review" / "scripts" / "chain_check.py"
        script.parent.mkdir(parents=True)
        script.write_text(CHAIN.read_text(encoding="utf-8"), encoding="utf-8")
        (tree / "skills" / "verify" / "scripts").mkdir(parents=True)
        (tree / "skills" / "verify" / "scripts" / "unverified_check.py").write_text(
            READER.read_text(encoding="utf-8"), encoding="utf-8"
        )
        (tree / "hooks").mkdir()
        (tree / "hooks" / "blocks.py").write_text(
            (ROOT / "hooks" / "blocks.py").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        (tree / "docs").mkdir()
        target = tree / "docs" / "the-review-record.md"
        named = os.path.join(str(script.parent), "..", "..", "..", "docs", target.name)
        for present in (True, False):
            if present:
                target.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
            else:
                target.unlink()
            done = subprocess.run(
                [
                    sys.executable,
                    str(script),
                    "--baseline",
                    "HEAD",
                    "--root",
                    str(tmp_path),
                ],
                capture_output=True,
                encoding="utf-8",
                errors="replace",
            )
            assert done.returncode == 2, (present, done.returncode, done.stderr)
            assert "Traceback" not in done.stderr, done.stderr
            assert named in done.stderr, done.stderr
            assert "grammar would not load" in done.stderr, done.stderr
            assert (said if present else "cannot be read") in done.stderr, done.stderr
        with pytest.raises(ValueError, match="cannot be read"):
            load(script, "chain_check_imported_beside_no_table")


# --- one value of a labelled line ----------------------------------------------------


class Test_verdict_of:
    def test_accepts_the_four_values(self):
        sha = "1a2b3c4d" * 5
        for value, read in (
            ("open", (chain.OPEN, None)),
            ("fixed abc1234", (chain.FIXED, "abc1234")),
            (f"fixed {sha}", (chain.FIXED, sha)),
            ("rejected", (chain.REJECTED, None)),
            ("deferred #12", (chain.DEFERRED, "#12")),
            ("deferred the frame", (chain.DEFERRED, "the frame")),
        ):
            assert chain.verdict_of(value) == read, value

    @pytest.mark.parametrize(
        "value",
        [
            "Fixed abc1234",
            "fixed",
            "fixed abc1234.",
            "fixed abc123",
            "fixed " + "1a2b3c4d" * 5 + "0",
            "fixed ABC1234",
            "fixed abc1234 · fix pass: done",
            "fixed abc1234 and more",
            "deferred",
            "deferred ",
            "confirmed",
            "**fixed** abc1234",
            "open — see below",
            "Open",
            " rejected",
            "",
        ],
    )
    def test_refuses_every_other_value(self, value):
        assert chain.verdict_of(value) is None


class Test_deferred_home:
    def test_accepts_the_home_after_the_word(self):
        assert chain.deferred_home("deferred #12") == "#12"
        assert chain.deferred_home("deferred the frame") == "the frame"

    def test_refuses_no_home_and_another_verdict(self):
        assert chain.deferred_home("deferred") is None
        assert chain.deferred_home("deferredness #12") is None
        assert chain.deferred_home("fixed abc1234") is None


class Test_issue_of:
    def test_accepts_a_home_that_is_exactly_an_issue(self):
        assert chain.issue_of(chain.deferred_home("deferred #12")) == 12

    def test_refuses_a_home_of_prose(self):
        assert chain.issue_of(chain.deferred_home("deferred to #664")) is None
        assert chain.issue_of(chain.deferred_home("deferred #12.")) is None
        assert chain.issue_of(None) is None


@pytest.mark.rule("location-touched-by-fix")
class Test_location_of:
    def test_accepts_one_or_more_backticked_coordinates(self):
        """S22 (T33): one or more backticked `path`, `path:line` or
        `path:first-last` items joined by `, `."""
        for value, paths in (
            ("`a.py`", ["a.py"]),
            ("`a.py:12`", ["a.py"]),
            ("`a.py:12-14`", ["a.py"]),
            ("`docs/x/`", ["docs/x/"]),
            ("`a.py:1`, `docs/b.md:3-4`", ["a.py", "docs/b.md"]),
            ("`a.py:1`, `b.py`, `c/d.md:9`", ["a.py", "b.py", "c/d.md"]),
        ):
            assert chain.location_of(value) == paths, value

    @pytest.mark.parametrize(
        "value",
        [
            "`:617`",
            "`a.py:1`, `:617`",
            "a.py:12",
            "`https://example.com/a`",
            "**`a.py:1`**",
            "`a.py:1`,`b.py`",
            "`a.py:1` and `b.py`",
            "`a.py:1`, ",
            "`a.py:x`",
            "`a.py:1-`",
            "`/abs/a.py`",
            "`a.py`.",
            "`a b.py`",
            "`a.py#unit`",
            "`a.py:1`, `b.py#unit`",
            "",
        ],
    )
    def test_refuses_everything_else(self, value):
        """The `path#unit` coordinate #923 leaked among them included."""
        assert chain.location_of(value) is None


class Test_reference_of:
    def test_accepts_a_round_and_a_finding(self):
        for value, read in (
            ("round-2#3", (2, 3)),
            ("round-2", (2, None)),
            ("round-12#10", (12, 10)),
        ):
            assert chain.reference_of(value) == read, value

    @pytest.mark.parametrize(
        "value",
        [
            "round 2's 3",
            "Round-2#3",
            "#3",
            "round-2#3.",
            "**round-2#3**",
            "`round-2#3`",
            "round-02#3",
            "round-2#03",
            "round-0#1",
            "round-2#",
            "round-2 #3",
            " round-2#3",
            "round-2#3, round-2#4",
            "none",
            "",
        ],
    )
    def test_refuses_every_other_spelling(self, value):
        assert chain.reference_of(value) is None


# --- a record ------------------------------------------------------------------------


def target_of(text):
    """`(the commit round_of reads off the record's target line, its
    errors)`."""
    read, errors = chain.round_of(reader, text, "r.md", 1)
    return read.target, errors


class Test_round_of:
    def test_accepts_the_one_target_line_and_reads_its_commit(self):
        """S4: a record's reviewed commit is its one `target:` line, reading
        `<sha> against <base>` or, for a verifying round, `<sha>, fixes
        <a>..<b>`; the commit is the first word."""
        sha = "1a2b3c4d" * 5
        for value, read in (
            ("abc1234 against main", "abc1234"),
            (f"{sha} against origin/release/v0.22.0", sha),
            ("abc1234, fixes 1111111..abc1234", "abc1234"),
        ):
            text = record("x").replace("target: x against main", f"target: {value}")
            assert target_of(text) == (read, []), value

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_no_line_two_lines_or_a_value_it_cannot_read(self):
        """S4: no `target:` line, the old `| Target SHA |` table row among the
        ways to have none, two of them, or a value outside the two shapes is
        refused by its line, and no commit is read."""
        table = record("x").replace(
            "target: x against main",
            "| Field | Value |\n|---|---|\n| Target SHA | abc1234 against main |",
        )
        assert target_of(table) == (None, [("r.md", 0, chain.NO_TARGET)])
        two = record("abc1234").replace(
            "## Findings", "target: abc1234 against main\n\n## Findings"
        )
        lines = reader.readable(two)
        second = [i + 1 for i, ln in enumerate(lines) if ln.startswith("target:")][1]
        sha, errors = target_of(two)
        assert sha is None and [line for _rel, line, _why in errors] == [second]
        assert "2 `target:` lines" in errors[0][2], errors
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
            lines = reader.readable(text)
            at = next(i + 1 for i, ln in enumerate(lines) if ln.startswith("target:"))
            sha, errors = target_of(text)
            assert sha is None, value
            assert [(rel, line) for rel, line, _why in errors] == [("r.md", at)], value
            assert "`<sha> against <base>`" in errors[0][2], value


class Test_findings:
    def test_accepts_each_finding_by_its_labelled_lines(self):
        """A finding's `### ` heading names it and its number; its one
        `verdict:` line decides it, its one `location:` line names its paths
        and its `regression:` line, where it stands, the earlier finding; a
        severity, an answer and a confirmation decide nothing."""
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
            ],
            confirmations=confirm("round-1#2"),
        )
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "r.md")
        assert errors == []
        assert [
            (f.line, f.heading, f.number, f.verdict, f.paths, f.regression)
            for f in found
        ] == [
            (
                lines.index("verdict: open") + 1,
                "### 1. the parser drops a row",
                1,
                (chain.OPEN, None),
                ["f.txt"],
                None,
            ),
            (
                lines.index("verdict: fixed abc1234") + 1,
                "### 2. the parser drops a row",
                2,
                (chain.FIXED, "abc1234"),
                ["f.txt"],
                (1, 4),
            ),
            (
                lines.index("verdict: deferred #12") + 1,
                "### 3. the parser drops a row",
                3,
                (chain.DEFERRED, "#12"),
                ["a.py", "docs/b.md"],
                (1, None),
            ),
        ]
        assert found[1].regression_line == lines.index("regression: round-1#4") + 1
        assert chain.findings(reader, reader.readable(record("abc1234")), "r.md") == (
            [],
            [],
        )

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_what_it_cannot_read_by_name(self):
        """S3, S11, S22 (T26, T33): a finding with no `verdict:` line, two,
        or its only one inside the fix block; a value outside the four; a
        labelled line above the first finding or under another section; a
        finding with no `location:` line, two, or one the check cannot read;
        two `regression:` lines, or one it cannot read; no `## Findings`, or
        two, or one with a word after its heading."""
        sections = [
            finding(1, "rejected").replace("verdict: rejected\n", ""),
            finding(2, "rejected").replace(
                "verdict: rejected\n", "verdict: rejected\nverdict: open\n"
            ),
            finding(3, "rejected")
            .replace("verdict: rejected\n", "")
            .replace("x = 1\n", "verdict: rejected\n"),
            finding(4, "deferred #9").replace("location: `f.txt:1`\n", ""),
            finding(5, "confirmed"),
            finding(6, "deferred #9", location="f.txt:1"),
            finding(7, "rejected").replace(
                "location: `f.txt:1`\n", "location: `f.txt:1`\nlocation: `g.txt`\n"
            ),
            finding(8, "rejected", regression="round 1's 3"),
            finding(9, "rejected", regression="round-1#3").replace(
                "regression: round-1#3\n",
                "regression: round-1#3\nregression: round-1#4\n",
            ),
            finding(10, "rejected"),
        ]
        text = record(
            "abc1234",
            sections,
            confirmations=confirm("none") + "\nlocation: `f.txt:1`\n",
        ).replace("## Findings\n\n", "## Findings\n\nverdict: rejected\n\n")
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.heading for f in found] == ["### 10. the parser drops a row"]
        heads = [i + 1 for i, ln in enumerate(lines) if ln.startswith("### ")]

        def at(prefix, k=0):
            return [i + 1 for i, ln in enumerate(lines) if ln.startswith(prefix)][k]

        assert [(rel, line) for rel, line, _why in errors] == [
            ("r.md", at("verdict: ")),
            ("r.md", heads[0]),
            ("r.md", at("verdict: open")),
            ("r.md", heads[2]),
            ("r.md", heads[3]),
            ("r.md", at("verdict: confirmed")),
            ("r.md", at("location: f.txt:1")),
            ("r.md", at("location: `g.txt`")),
            ("r.md", at("regression: round 1's 3")),
            ("r.md", at("regression: round-1#4")),
            ("r.md", at("location: ", -1)),
        ], errors
        said = [why for _rel, _line, why in errors]
        assert "outside a finding" in said[0] and "outside a finding" in said[-1]
        assert "`verdict:`" in said[0] and "`location:`" in said[-1]
        for why, n in zip(said[1:10], range(1, 10), strict=True):
            assert f"### {n}. the parser drops a row" in why, why
        assert "2 `verdict:` lines" in said[2]
        assert "no `verdict:` line" in said[1] and "no `verdict:` line" in said[3]
        assert "no `location:` line" in said[4]
        assert "`verdict: confirmed`" in said[5]
        assert "`fixed <commit>`" in said[5] and "`deferred <home>`" in said[5]
        assert "`location: f.txt:1`" in said[6] and "`path:line`" in said[6]
        assert "2 `location:` lines" in said[7]
        assert "`regression: round 1's 3`" in said[8] and "`round-<N>#<n>`" in said[8]
        assert "2 `regression:` lines" in said[9]
        assert chain.findings(
            reader, reader.readable("# r\n\n## Probes\n"), "r.md"
        ) == (
            [],
            [("r.md", 0, chain.NO_FINDINGS)],
        )
        longer = record("abc1234", [finding(1, "open")]).replace(
            "## Findings", "## Findings so far"
        )
        assert chain.findings(reader, reader.readable(longer), "r.md") == (
            [],
            [("r.md", 0, chain.NO_FINDINGS)],
        )
        two = reader.readable(record("abc1234") + "\n## Findings\n")
        second = [i + 1 for i, ln in enumerate(two) if ln == "## Findings"][1]
        _found, errors = chain.findings(reader, two, "r.md")
        assert [(line, why) for _rel, line, why in errors] == [
            (second, chain.TWO_FINDINGS)
        ]

    @pytest.mark.parametrize(
        "spelling, label",
        [
            ("Verdict: open", "`verdict:`"),
            ("**verdict:** open", "`verdict:`"),
            ("verdict : open", "`verdict:`"),
            ("Fix of a fix: `open_findings`", "`regression:`"),
            ("`fix of a fix`: the unit", "`regression:`"),
            ("refixes: round-1#1", "`regression:`"),
            ("Reopens: round-1#1", "`reopens:`"),
            ("Severity: must", "`severity:`"),
            ("Location: `f.txt:1`", "`location:`"),
            ("**evidence:** read `a.py:1`", "`evidence:`"),
            ("  answer : done", "`answer:`"),
            ("Confirms: round-1#1", "`confirms:`"),
            ("Target SHA: abc1234 against main", "`target:`"),
            ("Target: abc1234 against main", "`target:`"),
        ],
    )
    def test_refuses_a_label_in_another_spelling_at_its_line(self, spelling, label):
        """S24 (T32): a line whose first words, case-folded and stripped of
        emphasis, are a label of the table or an old spelling of one, and
        which is not the exact lowercase form, is refused at its line naming
        the label the check reads; a finding carrying one is not read past
        it."""
        text = record(
            "abc1234",
            [
                finding(1, "rejected").replace("answer: \n", f"{spelling}\n"),
                finding(2, "rejected"),
            ],
        )
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.number for f in found] == [2]
        assert [(rel, line) for rel, line, _why in errors] == [
            ("r.md", lines.index(spelling) + 1)
        ]
        why = errors[0][2]
        assert "### 1. the parser drops a row" in why, why
        assert label in why and "another spelling" in why, why

    def test_accepts_prose_that_only_begins_like_a_label(self):
        outside = record("abc1234", [finding(1, "rejected")]).replace(
            "## Not judged", "Verdict: rejected\n\n## Not judged"
        )
        lines = reader.readable(outside)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.number for f in found] == [1]
        assert [(line, "`verdict:`" in why) for _rel, line, why in errors] == [
            (lines.index("Verdict: rejected") + 1, True)
        ]
        for prose in ("Answers: none", "Verdicts read below.", "Severity matters."):
            text = record("abc1234", [finding(1, "rejected")]).replace(
                "Why it matters.", prose
            )
            assert chain.findings(reader, reader.readable(text), "r.md")[1] == []

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_reopens_line_beside_a_regression_or_naming_no_finding(self):
        """S23, S24 (T42): a `reopens:` line names an earlier finding as
        `round-<N>#<n>` and is read with its line. `reopens: round-1` is
        refused, so is a second `reopens:` line, and a finding holding a
        `reopens:` and a `regression:` line, at the later of the two, the
        refusal naming which line each case takes. A bare label of either is
        refused at its line."""
        text = record(
            "abc1234",
            [
                finding(1, "open", reopens="round-1#2"),
                finding(2, "open", reopens="round-1"),
                finding(3, "open", reopens="round-1#2").replace(
                    "reopens: round-1#2\n",
                    "reopens: round-1#2\nreopens: round-1#3\n",
                ),
                finding(4, "open", regression="round-1#2", reopens="round-1#3"),
                finding(5, "open").replace(
                    "verdict: open\n",
                    "reopens: round-1#4\nverdict: open\nregression: round-1\n",
                ),
                finding(6, "open"),
            ],
            n=2,
        )
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [(f.number, f.reopens, f.regression) for f in found] == [
            (1, (1, 2), None),
            (6, None, None),
        ], errors
        assert found[0].reopens_line == lines.index("reopens: round-1#2") + 1
        assert found[1].reopens_line is None
        fourth = lines.index("### 4. the parser drops a row")
        assert [(rel, line) for rel, line, _why in errors] == [
            ("r.md", lines.index("reopens: round-1") + 1),
            ("r.md", lines.index("reopens: round-1#3") + 1),
            ("r.md", lines.index("reopens: round-1#3", fourth) + 1),
            ("r.md", lines.index("regression: round-1") + 1),
        ], errors
        said = [why for _rel, _line, why in errors]
        for why, n in zip(said, (2, 3, 4, 5), strict=True):
            assert f"### {n}. the parser drops a row" in why, why
        assert "`reopens: round-1`" in said[0] and "`round-<N>#<n>`" in said[0]
        assert "2 `reopens:` lines" in said[1]
        for why in said[2:]:
            assert "`regression:`" in why and "`reopens:`" in why, why
            assert "a fix pass's own commit made the defect" in why, why
            assert "does not hold" in why, why
        for bare in ("reopens:", "regression:"):
            text = record(
                "abc1234",
                [
                    finding(1, "open").replace(
                        "verdict: open\n", f"verdict: open\n{bare}\n"
                    )
                ],
                n=2,
            )
            lines = reader.readable(text)
            found, errors = chain.findings(reader, lines, "r.md")
            assert found == [], bare
            assert [line for _r, line, _w in errors] == [lines.index(bare) + 1], errors
            assert f"`{bare}" in errors[0][2], errors

    def test_refuses_an_evidence_line_missing_twice_or_malformed(self):
        """S1, S3, S4 (#985): a finding carries one `evidence:` line, matched
        whole against its row: none is refused at its heading, two at the
        second, and each value the row does not hold at its line with the
        row's `Refused as`."""
        malformed = (
            "read `a.py`",
            "read a.py:1",
            "executed pytest",
            "ran `x`",
            None,
            "executed `x` and more",
        )
        sections = [
            finding(1, "open", evidence=None),
            finding(2, "open").replace(
                "evidence: read `f.txt:1`\n",
                "evidence: read `f.txt:1`\nevidence: executed `git grep -n x`\n",
            ),
            *(
                finding(n, "open").replace(
                    "evidence: read `f.txt:1`",
                    f"evidence: {value}" if value else "evidence:",
                )
                for n, value in enumerate(malformed, 3)
            ),
            finding(9, "open"),
        ]
        lines = reader.readable(record("abc1234", sections))
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.number for f in found] == [9], errors
        heads = [i + 1 for i, ln in enumerate(lines) if ln.startswith("### ")]
        said = [i + 1 for i, ln in enumerate(lines) if ln.startswith("evidence:")]
        assert [(rel, line) for rel, line, _why in errors] == [
            ("r.md", heads[0]),
            ("r.md", said[1]),
            *(("r.md", line) for line in said[2:8]),
        ], errors
        why = [w for _rel, _line, w in errors]
        shape = "`executed` and each command run, or `read` and each `path:line`"
        assert "no `evidence:` line: a finding carries one" in why[0], why[0]
        assert shape in why[0], why[0]
        assert "2 `evidence:` lines; a finding carries one" in why[1], why[1]
        for n, w in enumerate(why[2:], 3):
            assert f"### {n}. the parser drops a row" in w, w
            assert "which the check cannot read" in w and shape in w, w

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
        found, errors = chain.findings(reader, reader.readable(text), "r.md")
        assert errors == []
        assert [(f.number, f.verdict) for f in found] == [
            (n, (chain.REJECTED, None)) for n in range(1, 6)
        ]

    def test_refuses_a_target_or_confirms_line_out_of_its_place(self):
        """A `target:` or `confirms:` line inside a finding, and a
        `confirms:` line outside `## Confirmations`, is refused at its line."""
        inside = record(
            "abc1234",
            [
                finding(1, "rejected").replace(
                    "answer: \n", "target: abc1234 against main\n"
                ),
                finding(2, "rejected").replace("answer: \n", "confirms: none\n"),
                finding(3, "rejected"),
            ],
        ).replace("## Probes", "confirms: none\n\n## Probes")
        lines = reader.readable(inside)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.number for f in found] == [3]
        at = [i + 1 for i, ln in enumerate(lines) if ln.startswith(("target:", "conf"))]
        assert [(rel, line) for rel, line, _why in errors] == [
            ("r.md", line) for line in at[1:]
        ], errors
        said = [why for _rel, _line, why in errors]
        assert "### 1." in said[0] and "`target:`" in said[0], said
        assert "### 2." in said[1] and "`confirms:`" in said[1], said
        assert "`confirms:`" in said[2] and chain.CONFIRMATIONS_HEADING in said[2]

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
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.number for f in found] == [1, 3]
        assert [(line, why.split(" — ")[0]) for _r, line, why in errors] == [
            (lines.index("### 1. a second one") + 1, "### 1. a second one"),
            (
                lines.index("### the parser drops a row") + 1,
                "### the parser drops a row",
            ),
        ]
        assert "a second finding numbered 1" in errors[0][2]
        assert "no number" in errors[1][2]

    def test_refuses_a_severity_off_the_table_and_a_finding_with_no_answer(self):
        """Two refusals that arrive by construction from the table: a severity
        other than `must` or `should`, and a finding with no `answer:` line."""
        text = record(
            "abc1234",
            [
                finding(1, "rejected", severity="anything at all"),
                finding(2, "rejected").replace("answer: \n", ""),
                finding(3, "rejected"),
            ],
        )
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.number for f in found] == [3], errors
        said = {line: why for _rel, line, why in errors}
        severity = lines.index("severity: anything at all") + 1
        assert "a severity is `must` or `should`" in said[severity], said
        second = lines.index("### 2. the parser drops a row") + 1
        assert "no `answer:` line" in said[second], said


class Test_record_findings:
    def test_accepts_a_record_whose_regions_close(self):
        text = record("abc1234", [finding(1, "open"), finding(2, "rejected")])
        found, errors = chain.record_findings(reader, text, "r.md")
        assert errors == []
        assert found == chain.findings(reader, reader.readable(text), "r.md")[0]
        quoted = record(
            "abc1234",
            [
                finding(1, "rejected").replace(
                    "answer: \n", "answer: the `<!--` opener is quoted\n"
                ),
                finding(2, "open"),
            ],
        )
        found, errors = chain.record_findings(reader, quoted, "r.md")
        assert errors == [] and [f.number for f in found] == [1, 2], errors

    def test_accepts_a_bare_opener_later_in_a_line_as_text(self):
        """S4 of #1012: a `<!--` nothing closes, after the start of an
        `answer:` line, is text, so every finding after it is read. The
        reader that kept a comment state refused it as a comment that never
        closes."""
        text = record(
            "abc1234",
            [
                finding(1, "rejected").replace(
                    "answer: \n", "answer: a bare <!-- opens nothing\n"
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
            [
                finding(1, "rejected").replace("answer: \n", f"answer: \n{opener}\n"),
                finding(2, "open"),
            ],
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


class Test_confirmations:
    def test_accepts_each_confirms_line_as_a_reference_or_none(self):
        """S23: each entry is a `confirms:` line reading `round-<N>#<n>`, read
        with its line, or `none`; a record with nothing to confirm may leave
        the section out."""
        text = record(
            "abc1234",
            confirmations=confirm("round-1#2") + confirm("none") + confirm("round-3#1"),
            n=4,
        )
        lines = reader.readable(text)
        found, errors = chain.confirmations(reader, lines, "r.md")
        assert errors == []
        assert found == [
            (lines.index("confirms: round-1#2") + 1, (1, 2)),
            (lines.index("confirms: round-3#1") + 1, (3, 1)),
        ]
        left_out = record("abc1234").replace("## Confirmations\n", "")
        assert chain.confirmations(reader, reader.readable(left_out), "r.md") == (
            [],
            [],
        )

    @pytest.mark.parametrize(
        "old, new, said",
        [
            (
                "| the record | at most one | each entry is",
                "| the record | one | each entry is",
                "no `## Confirmations` section",
            ),
            (
                row_of("confirms:"),
                row_of("confirms:")
                + "| `signed:` | `signed: .+` | `## Confirmations` | one | x |\n",
                "no `signed:` line: `## Confirmations` carries one",
            ),
        ],
    )
    def test_refuses_a_section_left_out_where_the_table_says_one(
        self, monkeypatch, tmp_path, old, new, said
    ):
        """Round 2's finding 1 of #964: the reader counts the section and each
        row placed in it against no lines where it is absent, so `one` is kept
        for every row there."""
        left_out = record("abc1234", [finding(1, "open")]).replace(
            "## Confirmations\n", ""
        )
        assert chain.round_of(reader, left_out, "r.md", 1)[1] == []
        table, _old = chain.grammar(str(doc_with(tmp_path, old, new)), reader)
        monkeypatch.setattr(chain, "GRAMMAR", table)
        errors = chain.round_of(reader, left_out, "r.md", 1)[1]
        assert [(rel, line) for rel, line, _why in errors] == [("r.md", 0)], errors
        assert said in errors[0][2], errors
        signed = "signed: the warden\n\n" * ("signed" in new)
        kept = record("abc1234", [finding(1, "open")], confirm("none") + signed)
        monkeypatch.setattr(chain, "LABELS", (*chain.LABELS, "signed:"))
        assert chain.round_of(reader, kept, "r.md", 1)[1] == []

    @pytest.mark.rule("round-record-read-by-label")
    def test_refuses_a_line_or_a_table_it_cannot_read_by_line(self):
        """S23 (T36): a `confirms:` value the row does not match whole, a
        table row in the section, the old shape, and a second section."""
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
        lines = reader.readable(text)
        found, errors = chain.confirmations(reader, lines, "r.md")
        assert found == []
        at = [
            i + 1
            for i, ln in enumerate(lines)
            if ln.startswith("confirms:") and ln != "confirms: none"
        ]
        assert [(rel, line) for rel, line, _why in errors] == [
            ("r.md", line) for line in at
        ], errors
        for (_rel, _line, why), cell in zip(errors, bad, strict=True):
            assert f"`confirms: {cell}`" in why, why
            assert "`round-<N>#<n>` or `none`" in why, why
        table = record(
            "abc1234",
            confirmations="| Confirms | What holds |\n|---|---|\n| round-1#2 | x |\n",
            n=2,
        )
        lines = reader.readable(table)
        found, errors = chain.confirmations(reader, lines, "r.md")
        first = lines.index("| Confirms | What holds |") + 1
        assert found == []
        assert [line for _rel, line, _why in errors] == [first, first + 1, first + 2]
        assert all("`confirms:`" in why for _rel, _line, why in errors), errors
        two = reader.readable(record("abc1234") + "\n## Confirmations\n")
        second = [i + 1 for i, ln in enumerate(two) if ln == "## Confirmations"][1]
        assert chain.confirmations(reader, two, "r.md")[1] == [
            ("r.md", second, chain.TWO_CONFIRMATIONS)
        ]


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
        lines_one, lines_two = reader.readable(one), reader.readable(two)
        assert [(rel, line) for rel, line, _why in problems] == [
            ("round-1.md", lines_one.index("regression: round-1#1") + 1),
            ("round-1.md", lines_one.index("confirms: round-1#1") + 1),
            ("round-2.md", lines_two.index("regression: round-3#1") + 1),
            ("round-2.md", lines_two.index("regression: round-2") + 1),
            ("round-2.md", lines_two.index("reopens: round-1#7") + 1),
            ("round-2.md", lines_two.index("confirms: round-1#7") + 1),
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
        lines = reader.readable(last)
        problems = chain.channel(rounds_of(last)[0])
        assert [(rel, line) for rel, line, _why in problems] == [
            ("round-1.md", lines.index("verdict: fixed abc1234") + 1),
            ("round-1.md", lines.index("verdict: rejected") + 1),
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
        write(root, "seal/specs/1791999998-another-item/routing.md", "x\n")
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
        return load(ROOT / "hooks" / "routing.py", "routing_for_chain_tests")

    def test_accepts_a_framed_item_with_a_reframe_by_the_framer(self, branch):
        root, _code = branch
        write(
            root,
            f"{ITEM}/spec.md",
            SPEC + "Reframed 2026-10-16 by framer, after round 2.\n",
        )
        write(root, f"{ITEM}/plan.md", "# plan\n")
        commit(root, "frame")
        assert chain.frame(reader, self.routing(), str(root), ITEM, FRAMED) == []

    def test_refuses_a_missing_plan_and_a_reframe_by_another_party(self, branch):
        root, _code = branch
        write(
            root,
            f"{ITEM}/spec.md",
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
SAYS = "`## Rule changes` does not parse, and `settle` applies nothing from this spec: "
CONTINUED = "- nothing\n  why: a reason\n  that continues two spaces in\n"
PROSE = "- add\n  file: docs/policy.md\n  to: A rule.\n\nA paragraph under the item.\n"
NOTHING = "- nothing\n  why: a reason\n"
CHANGE = (
    "- change\n  file: docs/policy.md\n  section: A section\n"
    "  from: old words.\n  to: new words.\n"
)


def template_section():
    """What `templates/sdd-spec.md` holds under its `## Rule changes`:
    nothing, which is what a framer's skeleton commit carries."""
    text = (ROOT / "templates" / "sdd-spec.md").read_text(encoding="utf-8")
    section = text.split("\n## Rule changes\n", 1)[1].split("\n## Removes\n", 1)[0]
    assert section.strip() == "", section
    return section


def spec_with(section):
    """A spec whose `## Rule changes` holds SECTION, or that has no such
    section where SECTION is None, ending with the framer's mark."""
    rules = "" if section is None else f"## Rule changes\n\n{section}\n"
    return f"# spec\n\nbody\n\n{rules}## Removes\n\nnone\n\n" + SPEC.split("\n\n")[-1]


def put_spec(root, text, committed=True):
    """Write the work item's `spec.md`; where COMMITTED, commit it and the
    closing records after it, so the spec is the one thing to refuse."""
    write(root, f"{ITEM}/spec.md", text)
    if committed:
        commit(root, "the spec")
        seal(root)


def refusal(root, text, item=ITEM):
    """The line the check prints for ITEM's spec reading TEXT outside CI,
    built from `rule_changes.parse`'s own error so no reason is spelt here."""
    ((line, reason),) = RULES.parse(text, reader.policy_root(str(root))).errors
    return f"{item}/spec.md:{line}  {chain.RULE_CHANGES_SAYS.format(reason=reason)}"


def spec_lines(out, item=ITEM):
    return [ln for ln in out.splitlines() if f"{item}/spec.md" in ln]


def reviewed_to_head(root):
    """A round 3 at HEAD, with nothing of its own, and the closing records
    after it, so the spec read is the one refusal left."""
    head = git(root, "rev-parse", "HEAD")
    write(root, f"{ITEM}/rounds/round-3.md", record(head, n=3))
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
        write(root, f"{ITEM}/plan.md", "# plan\n")
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
        write(root, f"{MERGED_ITEM}/spec.md", spec_with(CONTINUED))
        commit(root, "another work item's spec")
        reviewed_to_head(root)
        released(root)
        monkeypatch.setenv("GITHUB_HEAD_REF", RELEASE)
        code, out = check(root, capsys)
        assert code == 0, out
        assert spec_lines(out) == [] and spec_lines(out, MERGED_ITEM) == [], out
        own = "seal/specs/1792000000-the-release"
        write(
            root,
            f"{own}/routing.md",
            ROUTING.format(review="straight to the PR", planning="the session").replace(
                "feature/x", RELEASE
            ),
        )
        commit(root, "the release's own work item")
        code, out = check(root, capsys)
        assert code == 1 and f"{own}/broad-gate.md" in out, out
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
        an edited spec; a work item with no `spec.md` never reaches it."""
        root, _code = branch
        monkeypatch.setattr(chain.SHARED_READER, "rule_changes", will_not_load)
        code, out = check(root, capsys)
        assert code == 0, out
        write(root, f"{MERGED_ITEM}/spec.md", spec_with(NOTHING))
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
        rel = f"{MERGED_ITEM}/spec.md"
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
        git(root, "rm", "-rq", f"{ITEM}/rounds")
        text = spec_with(CONTINUED)
        write(root, f"{MERGED_ITEM}/spec.md", text)
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
        write(root, f"{MERGED_ITEM}/spec.md", spec_with(CONTINUED))
        commit(root, "no work item, and a spec")
        code, out = check(root, capsys)
        assert code == 0, out
        assert "declared neither way" in out
        assert spec_lines(out, MERGED_ITEM) == [], out

    def test_accepts_a_spec_only_moved_and_a_file_beside_or_below_one(
        self, branch, ready, capsys
    ):
        """S16: a move with the bytes unchanged writes no section; another
        file beside a spec the branch leaves alone, and a `spec.md` one
        directory down, write none either."""
        root, _code = branch
        old, new = "seal/specs/1788000001-old", "seal/specs/1788000001-moved"
        on_main(root, f"{old}/spec.md", spec_with(CONTINUED))
        on_main(root, f"{MERGED_ITEM}/spec.md", spec_with(CONTINUED))
        git(root, "mv", old, new)
        write(root, f"{MERGED_ITEM}/plan.md", "# plan\n")
        # Bytes of its own: a copy of the moved spec's bytes would read as a
        # second name of that move.
        write(root, f"{MERGED_ITEM}/notes/spec.md", spec_with(PROSE))
        commit(root, "moved, beside another work item's spec, and below it")
        reviewed_to_head(root)
        code, out = check(root, capsys)
        assert code == 0, out
        for item in (old, new, MERGED_ITEM, f"{MERGED_ITEM}/notes"):
            assert spec_lines(out, item) == [], (item, out)


# --- the parity arm at the pull request (#988) -------------------------------------

PARITY = "seal/parity.md"
routing_module = load(chain.ROUTING, "specseal_routing_for_chain_tests")


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
            rel = f"{ITEM}/rounds/round-{n}.md"
            write(root, rel, with_original((root / rel).read_text("utf-8"), said))
    if any(said is not None for said in originals):
        commit(root, "the rounds compared with the original")
    seal(root)


def original_lines(out):
    """The lines the check prints about a round record or the config."""
    where = (f"{ITEM}/rounds/", f"{PARITY}:")
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
            f"no `original:` line: `{PARITY}` declares a migration",
            f"each round record carries `original: {BASELINE}`",
            "written by the warden once it compared the round's target with "
            "the original through `legacy-parity`",
        ):
            assert words in says, says
        assert original_lines(out) == [
            f"{ITEM}/rounds/round-{n}.md:0  {says}" for n in (1, 2)
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
        rel = f"{ITEM}/rounds/round-2.md"
        line = reader.readable((root / rel).read_text("utf-8")).index(
            f"original: {other}"
        )
        says = chain.OTHER_ORIGINAL.format(said=other, sha=BASELINE)
        assert original_lines(out) == [f"{rel}:{line + 1}  {says}"], out
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
        too, as `hooks/gate.py#touches_code` reads them."""
        root, _code = branch
        migrating(root, (None, None))
        inside = ["docs/a.md", f"{ITEM}/rounds/round-1.md"]

        def owed(paths):
            return chain.originals_of(reader, routing_module, str(root), paths, [ITEM])

        assert owed(inside) == []
        assert [p for p, _n, _w in owed([*inside, "f.txt"])] == [
            f"{ITEM}/rounds/round-1.md",
            f"{ITEM}/rounds/round-2.md",
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
            f"no `original:` line: `{PARITY}` declares a migration, this work "
            "item answers `straight to the PR`",
            f"the sealer's guarantee carries `original: {BASELINE}`",
            "once it compared the audited commit with the original through "
            "`legacy-parity`",
        ):
            assert words in says, says
        assert f"{rel}:0  {says}" in out.splitlines(), out
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


class Test_original_of:
    def test_accepts_a_line_naming_the_baseline_by_a_prefix(self):
        text = with_original(record("abc1234", [finding(1, "rejected")]), BASELINE[:9])
        assert chain.original_of(reader, text, "r.md", BASELINE, PARITY) == []

    @pytest.mark.parametrize(
        "where, said",
        [
            ("inside", "a `original:` line inside a finding"),
            ("twice", "2 `original:` lines; a round record carries one at most"),
            ("spelt", "a label in another spelling"),
        ],
    )
    def test_refuses_a_line_the_table_refuses_at_its_line_and_only_so(
        self, where, said
    ):
        """S9: an `original:` line inside a finding, a second one, and one
        spelt `Original:` are refused at the line by the grammar table's row,
        and `original_of` adds no second refusal saying the record has none."""
        text = record("abc1234", [finding(1, "rejected")])
        if where == "inside":
            text = text.replace("answer: \n", f"answer: \noriginal: {BASELINE}\n")
        elif where == "twice":
            text = with_original(with_original(text, BASELINE), BASELINE)
        else:
            text = with_original(text, BASELINE).replace("original:", "Original:")
        lines = reader.readable(text)
        at = next(
            i + 1 for i, ln in enumerate(lines) if ln.lower().startswith("original:")
        )
        _round, errors = chain.round_of(reader, text, "r.md", 1)
        assert [(line, said in why) for _r, line, why in errors] == [
            (at + (where == "twice"), True)
        ], errors
        assert chain.original_of(reader, text, "r.md", BASELINE, PARITY) == []


class Test_parity_readers:
    def test_accepts_a_process_that_loaded_only_the_check(self):
        """`parity_readers` loads `hooks/config.py` before `hooks/gate.py`,
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
        """A `hooks/gate.py` that raises at import is raised to the caller,
        which `originals_of` turns into exit 2; nothing hands back a reader
        that did not load."""
        shutil.copy(ROOT / "hooks" / "config.py", tmp_path / "config.py")
        (tmp_path / "gate.py").write_text("raise ImportError('planted')\n", "utf-8")
        monkeypatch.setattr(chain, "HOOKS", str(tmp_path))
        with pytest.raises(ImportError, match="planted"):
            chain.parity_readers()


# --- the sealer's guarantee (#969, #1000) ------------------------------------------

GUARANTEE_TEMPLATE = ROOT / "templates" / "sdd-guarantee.md"


def guarantee(sha, verdict):
    return (
        "# 1791999990-a-guaranteed-item — guarantee\n\n"
        "| Field | Value |\n|---|---|\n"
        f"| Target SHA | {sha} against main |\n"
        f"| Broad gate | {sha} against main, as `broad-gate.md` names it |\n\n"
        "## Claims re-run\n\n"
        "| Claim | Source | Command | Result |\n|---|---|---|---|\n\n"
        "## The parties\n\n"
        "| Party | Says | Agrees with | Disagrees with |\n|---|---|---|---|\n\n"
        f"Verdict: {verdict}\n"
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
    code, then `broad-gate.md` and `guarantee.md` naming that commit, judged
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
    write(
        d,
        f"{ITEM}/broad-gate.md",
        f"| Field | Value |\n|---|---|\n| Broad gate | {audited} against main |\n",
    )
    write(d, f"{ITEM}/guarantee.md", guarantee(audited, "sealed"))
    commit(d, "the closing records")
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": False}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    monkeypatch.delenv("GITHUB_HEAD_REF", raising=False)
    # Under Actions the check prints `::error` annotations; these cases read
    # the plain line it prints everywhere else.
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    return d, audited


def reseal(root, original):
    """The closing records naming HEAD, committed; the guarantee carries
    `original: ORIGINAL` under its table where ORIGINAL is given."""
    head = git(root, "rev-parse", "HEAD")
    write(
        root,
        f"{ITEM}/broad-gate.md",
        f"| Field | Value |\n|---|---|\n| Broad gate | {head} against main |\n",
    )
    text = guarantee(head, "sealed")
    if original is not None:
        text = text.replace(
            "\n## Claims re-run", f"\noriginal: {original}\n\n## Claims re-run"
        )
    write(root, f"{ITEM}/guarantee.md", text)
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


class Test_verdicts_of:
    def test_accepts_each_verdict_in_its_shape(self):
        """S5 of #1000: the line is `Verdict: sealed`, `Verdict: withheld
        reason: <…>` or `Verdict: undecided question: <…>`, read whole.
        Protects: `withheld` with its reason left off read as `sealed`, and a
        `sealed` with a rider passing."""
        for said, word in (
            ("sealed", "sealed"),
            ("withheld reason: the body claims a README change", "withheld"),
            ("undecided question: does #12 ask for the flag?", "undecided"),
        ):
            found = chain.verdicts_of(reader, guarantee("abc1234", said))
            assert [chain.verdict_word(v) for _n, v in found] == [word], said
        assert chain.verdict_word("Verdict: sealed, but the README is stale") is None
        assert chain.verdict_word("Verdict: withheld") is None

    def test_refuses_to_read_two_verdict_lines_as_one(self):
        text = guarantee("abc1234", "sealed").replace(
            "Verdict: sealed", "Verdict: sealed\n**Verdict:** with"
        )
        found = chain.verdicts_of(reader, text)
        assert [v for _n, v in found] == ["Verdict: sealed", "**Verdict:** with"]

    def test_the_verdict_patterns_are_linear_in_the_line(self):
        """#941's round 3 met a pattern that backtracked exponentially; the
        verdict line's patterns and the earlier run's repeat, so a long line
        of their repeated characters is read inside the bound, which is far
        above the linear time (under 0.1 s) and far below a backtracking
        one (no end), so a loaded runner does not fail it."""
        import time

        start = time.monotonic()
        for line in (
            "Verdict: withheld reason: " + "x " * 50000,
            "*_ " * 30000 + "verdict",
            "Verdict: undecided question:" + " " * 100000,
        ):
            chain.verdict_word(line)
            chain.verdicts_of(reader, line)
        chain.earlier_verdicts("; earlier run: aaa1111 against " + "x" * 100000)
        chain.earlier_verdicts("; earlier run: aaa1111" + " against x" * 30000)
        chain.earlier_verdicts("aaa1111 against " + "x" * 100000 + ";")
        chain.earlier_verdicts("earlier" + " " * 100000)
        chain.earlier_verdicts(" " * 100000 + "earlier runs" + " " * 100000)
        assert time.monotonic() - start < 5.0


# S6 of #1000: lines that mean the verdict and are not one of its three
# shapes. Each is refused at its line, and none reads as `sealed`.
NEAR_MISSES = (
    "Verdict: withheld — x",
    "Verdict: withheld - x",
    "Verdict: withheld",
    "Verdict: withheld reason:",
    "Verdict: withheld reason:x",
    "Verdict: withheld reason:  x",
    "Verdict: Sealed",
    "Verdict: **sealed**",
    "**Verdict:** sealed",
    "verdict: sealed",
    "Verdict: sealed reason: x",
    "Verdict: undecided reason: x",
    # Round 1 of #1000, finding 3: an indent is a code block at four spaces.
    "    Verdict: sealed",
    "\tVerdict: sealed",
)


class Test_earlier_verdicts:
    """#975: the stamp is drawn once per work item, held by the `Target SHA`
    row's own `; earlier run: <sha> <word>` chain rather than a count kept
    beside the tree. One reader of that chain, beside the check's other
    readers of the same row."""

    def test_accepts_each_earlier_run_with_its_verdict_word(self):
        """S9 of #1000: an entry is `<sha> <word>`, with `against <base>`
        after the SHA where it names one."""
        cell = (
            "ccc3333 against main; earlier run: bbb2222 against main sealed; "
            "earlier run: aaa1111 withheld"
        )
        assert chain.earlier_verdicts(cell) == [
            ("bbb2222", chain.SEALED),
            ("aaa1111", chain.WITHHELD),
        ]

    def test_a_first_run_has_none(self):
        assert chain.earlier_verdicts("aaa1111 against main") == []
        assert chain.earlier_verdicts("") == []
        assert chain.earlier_verdicts(None) == []

    @pytest.mark.parametrize(
        "entry",
        [
            "; earlier run: aaa1111 withheld — x",
            "; earlier run: aaa1111 Sealed",
            "; earlier run: `bbb2222` against main **sealed**",
            "; earlier run: an earlier one, sealed",
            # Round 1 of #1000, finding 4: a misspelt separator.
            ";  earlier run: bbb2222 sealed",
            "; Earlier run: bbb2222 sealed",
            "; earlier run bbb2222 sealed",
            "; earlier runs: bbb2222 sealed",
            ", earlier run: bbb2222 sealed",
            # Round 2 of #1000, finding 3: the row has one shape, so no
            # spelling of the separator passes unread.
            "; earlier-run: bbb2222 sealed",
            "; earlier_run: bbb2222 sealed",
            "; earlierrun: bbb2222 sealed",
            # Any other text after the target, such as a second word of base.
            " @ 4a6e24f6",
            " (resolved as origin/main)",
        ],
    )
    def test_refuses_text_after_the_target_that_is_no_earlier_run(self, entry):
        """S9 of #1000, and round 1's finding 4 and round 2's finding 3: the
        `Target SHA` value is `<sha> against <base>`, then each earlier run
        as exactly `; earlier run: <sha> <word>`, and any other text after
        the target comes back quoted with no word, for the arm to refuse.
        Seen red against the reader that read the word by its prefix and
        through emphasis, and against the one that looked for the separator
        in some spellings: a hyphen, an underscore and the joined word gave
        no entry at all."""
        cell = f"ccc3333 against main{entry}"
        assert chain.earlier_verdicts(cell) == [(entry.strip(), None)]

    def test_an_entry_is_read_exactly_up_to_the_next_separator(self):
        """Round 2 of #1000, finding 3: a space before the next separator is
        text the shape does not hold, so that entry reads no word and the
        one after it still reads."""
        cell = "ccc3333 against main; earlier run: aaa1111 withheld ; earlier run: bbb2222 sealed"
        assert chain.earlier_verdicts(cell) == [
            ("; earlier run: aaa1111 withheld", None),
            ("bbb2222", chain.SEALED),
        ]

    @pytest.mark.parametrize(
        "entry",
        [
            "; earlier run: aaa1111 withheld — x",
            "; earlier run: aaa1111 Sealed",
            "; Earlier run: aaa1111 sealed",
            "; earlier-run: aaa1111 sealed",
        ],
    )
    def test_the_arm_refuses_an_entry_at_the_target_row(self, item, entry):
        """S9 of #1000: the guarantee arm refuses it at the `Target SHA`
        row's line, naming the entry and the shape it reads."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace(
            f"| Target SHA | {sha} against main |",
            f"| Target SHA | {sha} against main{entry} |",
        )
        write(root, rel, text)
        commit(root, "an earlier run with a rider")
        [(path, number, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        row = next(n for n, ln in enumerate(text.splitlines(), 1) if "Target SHA" in ln)
        assert (path, number) == (rel, row), why
        assert f"`{entry.strip()}`" in why, why
        assert "`<sha> against <base>`" in why and "<sha> <word>`" in why, why


@pytest.mark.rule("ready-needs-sealed")
class Test_guarantee:
    def test_accepts_a_sealed_verdict_at_head(self, item):
        root, _sha = item
        assert chain.guarantee(reader, str(root), ITEM, "main") == []

    def test_refuses_absent_unfilled_and_behind_head_by_name(self, item):
        root, _sha = item
        rel = f"{ITEM}/guarantee.md"
        write(root, f"{ITEM}/overview.md", "# an edit the sealer never read\n")
        later = commit(root, "a record after the guarantee")
        [(path, _line, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        assert path == rel and later[:8] in why
        write(root, rel, GUARANTEE_TEMPLATE.read_text(encoding="utf-8"))
        commit(root, "the template, unfilled")
        problems = chain.guarantee(reader, str(root), ITEM, "main")
        assert any("no SHA" in why for _p, _n, why in problems)
        head = git(root, "rev-parse", "HEAD")
        write(root, rel, guarantee(head, "sealed") + "Verdict: sealed\n")
        commit(root, "two verdicts")
        [(_p, _n, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        assert "2 `Verdict:` lines" in why
        write(root, rel, guarantee(head, "sealed").replace("Verdict: sealed\n", ""))
        commit(root, "no verdict")
        assert chain.guarantee(reader, str(root), ITEM, "main") == [
            (rel, 0, "0 `Verdict:` lines; the guarantee carries one")
        ]
        hidden = guarantee(head, "sealed").replace(
            "## The parties", "~~~\n\n## The parties"
        )
        write(root, rel, hidden)
        commit(root, "a fence nobody closed")
        opener = hidden.splitlines().index("~~~") + 1
        problems = chain.guarantee(reader, str(root), ITEM, "main")
        assert [(p, n) for p, n, _why in problems] == [(rel, opener), (rel, 0)]
        assert "never closes" in problems[0][2], problems
        git(root, "rm", "-q", rel)
        commit(root, "no guarantee")
        [(_p, _n, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        assert "git carries no guarantee file" in why

    def test_an_opener_quoted_in_a_code_span_hides_no_verdict(self, item):
        """Round 1 of #1000, finding 2: a claims cell quoting the comment
        opener in a code span, as two merged guarantees do, leaves the
        verdict line below it read. Seen red against the scan that read the
        opener: 0 `Verdict:` lines."""
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
        """S5 of #1012: a verdict quoted in a comment above the verdict line
        is refused at its line, and the line below it is still the one
        verdict. The reader that kept a comment state passed it."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace(
            "Verdict: sealed", "<!-- Verdict: sealed -->\nVerdict: sealed"
        )
        write(root, rel, text)
        commit(root, "a verdict in a comment")
        line = text.splitlines().index("<!-- Verdict: sealed -->") + 1
        assert chain.guarantee(reader, str(root), ITEM, "main") == [
            (rel, line, reader.COMMENT_LINE)
        ]

    @pytest.mark.rule("ready-needs-sealed")
    @pytest.mark.parametrize("line", NEAR_MISSES)
    def test_refuses_a_near_miss_of_the_verdict_at_its_line(self, item, line):
        """S6 of #1000. Seen red against the reader that stripped emphasis and
        read a value by its prefix: `Sealed`, `**sealed**` and `**Verdict:**
        sealed` passed as `sealed`, and the rest were refused naming no shape,
        or not read at all."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        text = guarantee(sha, "sealed").replace("Verdict: sealed", line)
        write(root, rel, text)
        commit(root, f"the sealer wrote {line}")
        found = chain.verdicts_of(reader, text)
        assert len(found) == 1 and chain.verdict_word(found[0][1]) != chain.SEALED
        [(path, number, why)] = chain.guarantee(reader, str(root), ITEM, "main")
        assert (path, number) == (rel, text.splitlines().index(line) + 1), why
        for shape in (
            "`Verdict: sealed`",
            "`Verdict: withheld reason: <reason>`",
            "`Verdict: undecided question: <question>`",
        ):
            assert shape in why, why

    @pytest.mark.rule("ready-needs-sealed")
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
            code, out = check(root, capsys, "--sealing")
            assert code == 0 and rel in out
        event = root.parent / "event.json"
        event.write_text(
            json.dumps({"pull_request": {"draft": True}}), encoding="utf-8"
        )
        code, out = check(root, capsys)
        assert code == 0 and rel in out

    @pytest.mark.rule("ready-needs-sealed")
    def test_the_old_words_are_refused_by_line(self, item, capsys):
        """T8, S8 of #969: a `guarantee.md` written before the words changed,
        reading `sound`, `not sound` or `undecidable`, fails a ready pull request
        on its `Verdict:` line, and the line says the word changed and what to
        do: spawn the sealer again at HEAD where `broad-gate.md` names a run at
        HEAD or one followed only by the work item's records, and otherwise run
        the broad gate first (round 1 of #969, finding 4). The line asserts
        nothing about the record it did not read (round 2, finding 2): the same
        pass's `broad_gate` line may say the record is behind HEAD. Protects: two
        spellings in one tree, where the check takes `sound` for the new
        `sealed`, or refuses it with a line nobody can place."""
        root, sha = item
        rel = f"{ITEM}/guarantee.md"
        for old in (
            "sound",
            "not sound — the body claims a README change",
            "undecidable",
        ):
            text = guarantee(sha, old)
            number = text.splitlines().index(f"Verdict: {old}") + 1
            write(root, rel, text)
            commit(root, f"the sealer said {old} before the words changed")
            code, out = check(root, capsys)
            assert code == 1, out
            line = next(ln for ln in out.splitlines() if ln.startswith(f"{rel}:"))
            assert line.split()[0] == f"{rel}:{number}", line
            word = old.split(" — ")[0]
            assert f"`{word}` is a word the verdict no longer uses" in line, line
            # S8 of #1000: the three shapes, and no dash form.
            assert (
                "`Verdict: sealed`, `Verdict: withheld reason: <reason>` or "
                "`Verdict: undecided question: <question>`"
            ) in line, line
            assert chain.DASH not in line.split("no longer uses", 1)[1], line
            assert (
                "Where `broad-gate.md` names a run at HEAD, or one followed only "
                "by the work item's records, spawn the sealer again at HEAD, which "
                "writes the new word"
            ) in line, line
            assert (
                "otherwise run `broad-gate --base <base> --record <item>` and "
                "commit `broad-gate.md` first"
            ) in line, line
            assert "still stands" not in line, line


class Test_broad_gate:
    def test_accepts_a_run_at_head(self, item):
        root, _sha = item
        assert chain.broad_gate(reader, str(root), ITEM, "main") == []

    @pytest.mark.rule("record-comment-line-refused")
    def test_refuses_a_comment_line_at_its_line(self, item):
        """S5 of #1012: a `broad-gate.md` line that begins with `<!--` is
        refused at its line, beside what the run's row says."""
        root, sha = item
        rel = f"{ITEM}/broad-gate.md"
        write(
            root,
            rel,
            "<!-- the gate's guidance -->\n\n"
            f"| Field | Value |\n|---|---|\n| Broad gate | {sha} against main |\n",
        )
        commit(root, "a comment in the gate record")
        assert chain.broad_gate(reader, str(root), ITEM, "main") == [
            (rel, 1, reader.COMMENT_LINE)
        ]


class Test_comment_lines:
    def test_accepts_a_record_whose_lines_open_no_comment(self):
        """An opener quoted in a code span, later in a line or inside a fence
        begins no line (*Scope* item 3 of #1012)."""
        text = "a `<!--` b\nprose <!-- open\n```\n<!-- quoted\n```\n"
        assert chain.comment_lines(reader, text, "r.md") == []

    def test_refuses_each_comment_line_at_its_line(self):
        text = "# r\n\n<!-- one -->\nprose\n   <!-- two\n"
        assert chain.comment_lines(reader, text, "r.md") == [
            ("r.md", 3, reader.COMMENT_LINE),
            ("r.md", 5, reader.COMMENT_LINE),
        ]


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
    d = os.path.join(common_dir(repo), "seal", "specs", item)
    os.makedirs(os.path.join(d, "rounds"), exist_ok=True)
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
    env = dict(os.environ)
    env.pop("GITHUB_EVENT_PATH", None)
    env.pop("GITHUB_HEAD_REF", None)
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
        env=env,
    )
    return r.returncode, r.stdout + r.stderr


ADD_THE_FILE = "Add seal/specs/<work-item>/routing.md to declare"


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
        (repo / "seal" / "specs").mkdir(parents=True)
        code, out = run_check(repo)
        assert code == 0, out
        assert ADD_THE_FILE in out, out
        assert "local mode" not in out, out

    def test_the_shared_sentence_says_what_it_searched_and_for_what(self, repo):
        """The prefix and the branch are what make the sentence checkable."""
        (repo / "seal" / "specs").mkdir(parents=True)
        _code, out = run_check(repo)
        assert "under `seal/specs/`" in out, out
        assert "declares `feature`" in out, out

    def test_a_repository_with_no_root_is_told_to_add_the_file(self, repo):
        """With no root to name, the file to write is the answer."""
        code, out = run_check(repo)
        assert code == 0, out
        assert ADD_THE_FILE in out, out
        assert "local mode" not in out, out


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
        """S10: a commit whose `SpecSeal-Routing` trailer names a work item no
        declaration names fails a ready pull request, naming the commit and
        the item; one reading `no work item` is printed as a notice; one with
        no such trailer is not named. A draft prints the same lines and
        passes."""
        root = undeclared
        write(root, "a.txt", "a\n")
        named = commit_saying(root, "feat: a", f"SpecSeal-Routing: {ROUTED}")
        write(root, "b.txt", "b\n")
        none = commit_saying(root, "chore: b", "SpecSeal-Routing: no work item")
        write(root, "c.txt", "c\n")
        bare = commit_saying(root, "chore: c")
        code, out = check(root, capsys)
        assert code == 1, out
        lines = out.splitlines()
        assert chain.UNDECLARED_TRAILER.format(sha=named[:8], item=ROUTED) in lines
        assert chain.NO_WORK_ITEM_TRAILER.format(sha=none[:8]) in lines
        assert bare[:8] not in out, out
        assert chain.UNDECLARED_TRAILER.format(sha="x", item="y") == (
            "commit x carries `SpecSeal-Routing: y`, and no routing declaration "
            "this pull request judges names that work item: commit its "
            "`routing.md`, naming this branch, or correct the trailer"
        )
        assert chain.NO_WORK_ITEM_TRAILER.format(sha="x") == (
            "commit x carries `SpecSeal-Routing: no work item`: its session "
            "recorded that the change belongs to no work item, and nothing "
            "here checks it further"
        )
        event(tmp_path, monkeypatch, True)
        code, out = check(root, capsys)
        assert code == 0, out
        assert chain.UNDECLARED_TRAILER.format(sha=named[:8], item=ROUTED) in out

    def test_accepts_a_commit_naming_the_work_item_its_declaration_names(
        self, branch, ready, capsys
    ):
        root, _code = branch
        commit_saying(root, "chore: e", "SpecSeal-Routing: 1791999999-a-work-item")
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out
        assert "SpecSeal-Routing" not in out, out

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
        assert "SpecSeal-Routing" not in out, out

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
            f"SpecSeal-Routing: {ROUTED}",
            "side",
        )
        write(root, "q.txt", "q\n")
        commit_saying(
            root, "feat: elsewhere (#7)", f"SpecSeal-Routing: {ROUTED}", env=GITHUB
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
        os.makedirs(os.path.join(root, ".git", "seal", "specs", ROUTED))
        write(root, "a.txt", "a\n")
        named = commit_saying(root, "feat: a", f"SpecSeal-Routing: {ROUTED}")
        code, out = check(root, capsys)
        assert code == 0, out
        assert chain.LOCAL_TRAILER.format(sha=named[:8], item=ROUTED) in out, out
        assert chain.LOCAL_TRAILER.format(sha="x", item="y") == (
            "commit x carries `SpecSeal-Routing: y` in a repository whose root "
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
        picked = commit_saying(root, "feat: s", f"SpecSeal-Routing: {ROUTED}")
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
        """S3 (T27): the `verdict:` lines decide, the line and the finding's
        heading are named, and a draft prints the same line and passes. A
        finding's `severity:` decides nothing."""
        root, code_sha = branch
        rel = f"{ITEM}/rounds/round-1.md"
        write(root, rel, record(code_sha, [finding(1, "open")]))
        commit(root, "the record, still open")
        code, out = check(root, capsys)
        assert code == 1
        line = next(ln for ln in out.splitlines() if "### 1." in ln)
        number = reader.readable(record(code_sha, [finding(1, "open")])).index(
            "verdict: open"
        )
        assert line.startswith(f"{rel}:{number + 1}"), line
        assert "### 1. the parser drops a row" in line
        assert (
            "reads `verdict: open`: the fix pass answers it with another verdict, "
            "and a verdict is `open`, `fixed <commit>`, `rejected` or `deferred <home>`"
        ) in line
        ready.write_text(json.dumps({"pull_request": {"draft": True}}), "utf-8")
        code, out = check(root, capsys)
        assert code == 0
        assert any("### 1." in ln and "verdict: open" in ln for ln in out.splitlines())
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
        rel = f"{ITEM}/rounds/round-1.md"
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
        finding, the commit and what it touched; one touching one of two
        named paths, a file under a named directory, or a path the fix pass
        appended passes, and so does the root commit. A path sharing a named
        directory's prefix is not under it."""
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
        rel = f"{ITEM}/rounds/round-1.md"
        sections = [
            finding(1, f"fixed {made['g']}"),
            finding(2, f"fixed {made['g']}", location="`f.txt:1`, `g.txt:3`"),
            finding(3, f"fixed {made['dir']}", location="`docs/x/`"),
            finding(4, f"fixed {made['dir']}", location="`docs/x`"),
            finding(5, f"fixed {made['h']}", location="`f.txt:1`, `h.txt`"),
            finding(6, f"fixed {base[:8]}", location="`f.txt`"),
            finding(7, f"fixed {made['near']}", location="`docs/x`"),
        ]
        write(root, rel, record(code_sha, sections))
        commit(root, "the record, seven fixes")
        write(
            root,
            f"{ITEM}/rounds/round-2.md",
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
        git(root, "rm", "-q", f"{ITEM}/rounds/round-2.md")
        commit(root, "no verifying round")
        seal(root)
        rel = f"{ITEM}/rounds/round-1.md"
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

    @pytest.mark.rule("last-record-at-head")
    def test_refuses_a_code_commit_after_the_last_record(self, branch, ready, capsys):
        """S4 (T12): a record commit after the last record passes; a code
        commit after it fails naming the commit and the verifying round."""
        root, _code = branch
        write(root, f"{ITEM}/overview.md", "# overview\n")
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
        git(root, "rm", "-rq", f"{ITEM}/rounds")
        commit(root, "no record")
        code, out = check(root, capsys)
        assert code == 1 and "holds no `round-N.md`" in out
        ready.write_text(json.dumps({"pull_request": {"draft": True}}), "utf-8")
        code, out = check(root, capsys)
        assert code == 0 and "holds no `round-N.md`" in out

    @pytest.mark.rule("old-table-shape-refused")
    def test_refuses_an_old_shape_record_and_an_unclosed_fence(
        self, branch, ready, capsys
    ):
        """S11: a record of the old shape under the declared item has no
        `## Findings` and is refused by name; a fence the warden never closed
        hides the open finding below it and is named at its opener."""
        root, code_sha = branch
        rel = f"{ITEM}/rounds/round-1.md"
        write(root, rel, OLD_RECORD.replace("0000000", code_sha))
        commit(root, "an old-shape record")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1
        assert f"{rel}:0" in out and chain.NO_FINDINGS in out
        text = record(
            code_sha,
            [
                finding(1, "rejected").replace("answer: \n", "~~~python\n"),
                finding(2, "open"),
            ],
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
        rel = f"{ITEM}/broad-gate.md"
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
            f"{ITEM}/rounds",
            f"{ITEM}/broad-gate.md",
            f"{ITEM}/guarantee.md",
        )
        commit(root, "direct, and no run")
        code, out = check(root, capsys)
        assert code == 1 and "broad-gate.md" in out and "guarantee.md" in out
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

OLD_ITEM = "seal/specs/1788000000-an-earlier-item"


def remove_an_earlier_item(root, applied, whole=True):
    """Declare an earlier work item on `main`, bring it into the branch, and
    remove its directory there, or only its declaration, with or without its
    rule change applied."""
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
        f"{OLD_ITEM}/spec.md",
        "# a spec\n\n## Rule changes\n\n- add\n  file: docs/policy.md\n  to: A rule.\n",
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
    def test_accepts_a_declaration_a_settle_removed(self, branch, draft, capsys):
        """A `routing.md` that `settle --apply` removed is a deletion in the
        diff, and `docs/` holding its rule change is what tells it from one."""
        root, _code = branch
        remove_an_earlier_item(root, applied=True)
        _code, out = check(root, capsys)
        assert "retired: a settle" in out and "1788000000-an-earlier-item" in out
        assert "does not carry this file at HEAD" not in out

    @pytest.mark.parametrize(
        "applied, whole, uncommitted",
        [(False, True, False), (True, False, False), (False, True, True)],
        ids=["nothing-absorbs-it", "the-directory-stays", "only-the-working-tree"],
    )
    def test_refuses_a_declaration_deleted_with_nothing_absorbing_it(
        self, branch, draft, capsys, applied, whole, uncommitted
    ):
        """A deletion with nothing absorbing it, a `routing.md` deleted beside
        a `spec.md` that stays, and a rule change only the working tree holds,
        which CI's read of HEAD does not see."""
        root, _code = branch
        remove_an_earlier_item(root, applied=applied, whole=whole)
        if uncommitted:
            write(root, "docs/policy.md", "A rule.\n")
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
        has it, the declarations stay judged."""
        root, _code = branch
        remove_an_earlier_item(root, applied=False)
        git(root, "rm", "-rq", "seal")
        commit(root, "the root leaves the tree")
        code, out = check(root, capsys)
        assert code == 0, out
        assert (
            "no `seal/` is at HEAD, so nothing is declared: the routing "
            "declarations this pull request deletes left the tree with the "
            "root, and the review-chain check judged the commit trailers and "
            "nothing else"
        ) in out
        assert "does not carry this file at HEAD" not in out
        real = chain.git
        unanswered = ("ls-tree", "HEAD", "--", "seal")
        monkeypatch.setattr(
            chain, "git", lambda r, *a: None if a == unanswered else real(r, *a)
        )
        code, out = check(root, capsys)
        assert code == 1 and "does not carry this file at HEAD" in out, out

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
        """Three parties ask whether a removed directory was settled, and a
        predicate spelled in each would take the next condition in one and not
        the others. The behaviour is pinned per reader in its own module; this
        pins that this one reaches the answer by calling `settled` on the
        module that owns it, so a reader that re-derives the rule inline goes
        red here even while it agrees today. `tests/test_settle.py` holds
        `settle.py` to the same."""
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
        import and `hooks/routing.py` after argument parsing, so it is given
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


# --- left where they stand, for #923: they read the shipped documents --------------


def test_the_warden_and_the_review_skill_name_every_line_a_finding_needs():
    """S8 (#985): `agents/warden.md` step 7 and `skills/code-review/SKILL.md`
    *The record* each list the lines a finding carries, and each names
    every row the table places in a finding as `one`, read from the table."""
    needed = [
        key
        for key, row in chain.GRAMMAR.items()
        if row.where == chain.IN_FINDING and row.many == chain.ONE
    ]
    assert "evidence:" in needed, needed
    warden = " ".join((ROOT / "agents" / "warden.md").read_text("utf-8").split())
    step = warden.split("7. Write the record", 1)[1].split("## Never", 1)[0]
    skill = " ".join(
        (ROOT / "skills" / "code-review" / "SKILL.md").read_text("utf-8").split()
    )
    said = skill.split("## The record ", 1)[1]
    said = said.split("Each finding carries one line of each row", 1)[1]
    said = said.split("The check refuses a finding missing any.", 1)[0]
    for where, text in (
        ("warden.md step 7", step),
        ("`skills/code-review/SKILL.md` *The record*", said),
    ):
        missing = [key for key in needed if f"`{key}" not in text]
        assert missing == [], f"{where} does not name {missing}"


def test_the_template_is_the_record_the_check_reads():
    """S1 (T29, T38): `templates/sdd-round.md` is a record the check reads:
    one `target:` line and no table above the findings; one finding at
    `open`, located at one coordinate, resting on one `evidence:` line,
    naming the regression `round-1#1`; a `verdict:` written inside its fix
    block not read as a line; `## Confirmations` holding its two example
    entries; no `reopens:` line and no `original:` line, with the review
    skill saying where a `reopens:` finding's grounds open; the record
    document naming the stand-in for a backtick; and no emoji anywhere."""
    text = TEMPLATE.read_text(encoding="utf-8")
    lines = reader.readable(text)
    found, errors = chain.record_findings(reader, text, "t")
    assert errors == []
    assert [(f.verdict, f.paths, f.regression, f.reopens) for f in found] == [
        ((chain.OPEN, None), ["path"], (1, 1), None)
    ]
    assert len([ln for ln in lines if chain.label_of(ln) == "evidence:"]) == 1
    assert not any(ln.startswith(chain.REOPENS_ROW) for ln in lines)
    assert not any(ln.startswith(chain.ORIGINAL_ROW) for ln in lines)
    skill = (ROOT / "skills" / "code-review" / "SKILL.md").read_text("utf-8")
    assert "where `reopens:` stands" in " ".join(skill.split())
    stand_in = "with `$(printf '\\140')` in place of the character"
    assert stand_in in " ".join(DOC.read_text(encoding="utf-8").split())
    assert found[0].heading.startswith("### 1. ") and found[0].number == 1
    confirmed, errors = chain.confirmations(reader, lines, "t")
    assert errors == []
    assert [ref for _line, ref in confirmed] == [(1, 2)]
    assert [ln for ln in lines if ln.startswith("confirms:")] == [
        "confirms: round-1#2",
        "confirms: none",
    ]
    head = text.split(chain.FINDINGS_HEADING)[0]
    assert chain.table_rows(reader, reader.readable(head)) == []
    assert chain.round_of(reader, text, "t", 1)[0].target == "1a2b3c4"
    fence = text.index("```", text.index("### 1. "))
    line_end = text.index("\n", fence) + 1
    fenced = text[:line_end] + "verdict: rejected\n" + text[line_end:]
    found, errors = chain.findings(reader, reader.readable(fenced), "t")
    assert errors == [] and [f.verdict for f in found] == [(chain.OPEN, None)]
    assert [c for c in text if EMOJI.match(c)] == []


test_census = census_case(TARGET)

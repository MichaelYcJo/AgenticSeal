"""`.github/scripts/finding_counts.py`, the four numbers of
`docs/release-checklist.md` step 2b (#1223).

Each case builds a repository in a temporary directory: work items under
`seal/threads/`, each with its `routing.md` and its round records, committed
so `--released-at` has a commit to read, and runs `main` in the process. The
scenarios are work item 1793521559's S1 to S6.
"""

import errno
import os

import pytest
from conftest import ROOT, census_case, commit_everything, git_out, git_repo
from conftest import load_module as load
from conftest import seal_block as block

TARGET = ".github/scripts/finding_counts.py"

SCRIPT = os.path.join(ROOT, ".github", "scripts", "finding_counts.py")

HEADER = "| work item | findings | regression or reopens | records alone | rounds |"
SEPARATOR = "|---|---|---|---|---|"

ROUTING = """| Axis | Answer |
|---|---|
| Review | {review} |
| Destination | open the pull request |
| Branch | feat/{item} |
"""
CHAIN = "through the review chain"
ITEM = "1700000001-an-item"
FENCE = "`" * 3


def counts():
    return load(SCRIPT, "agentic_finding_counts_for_tests")


def finding(n, location, close_location=None, regression=None, prose="Why."):
    """One `### <n>. <symptom>` section in `templates/records/sdd-round.md`'s
    shape: its finding block at `location`, the prose, a fix fence, and a
    close block, whose `location:` is `close_location` where one is given."""
    fields = [
        "severity: must",
        f"location: {location}",
        "evidence: read `f.py:1`",
    ]
    fields += [f"regression: {regression}"] if regression else []
    closing = ["verdict: fixed abc1234", "answer: done"]
    closing += [f"location: {close_location}"] if close_location else []
    return (
        f"### {n}. a symptom\n\n"
        + block(*fields)
        + f"\n{prose}\n\n{FENCE}python\nx = 1\n{FENCE}\n\n"
        + block(*closing)
        + "\n"
    )


def record(*findings):
    """A round record: its round block, then `## Findings` holding
    `findings`."""
    return (
        "# review round\n\n"
        + block("target: abc1234 against main")
        + "\n## Findings\n\n"
        + "".join(findings)
        + "## Probes\n"
    )


def item(root, name=ITEM, rounds=(), review=CHAIN):
    """The work item `name` under `root`, routed `review`, holding one round
    record per text of `rounds`; its directory."""
    where = root / "seal" / "threads" / name
    (where / "trail" / "rounds").mkdir(parents=True)
    (where / "routing.md").write_text(
        ROUTING.format(review=review, item=name), encoding="utf-8"
    )
    for n, text in enumerate(rounds, 1):
        (where / "trail" / "rounds" / f"round-{n}.md").write_text(
            text, encoding="utf-8"
        )
    return where


def run(root, capsys, ref="HEAD"):
    """`(exit code, stdout lines, stderr)` of `main` over `root` at `ref`."""
    code = counts().main(["--root", str(root), "--released-at", ref])
    out, err = capsys.readouterr()
    return code, out.split("\n"), err


def table(root, capsys):
    """The rows `main` prints over `root`, committed, at HEAD, past the
    header and the separator, and the lines under the table, which a blank
    line parts from it so a renderer does not read them as rows."""
    commit_everything(str(root), "the work items")
    code, lines, err = run(root, capsys)
    assert code == 0, err
    assert lines[:2] == [HEADER, SEPARATOR], lines
    rows = [line for line in lines[2:] if line.startswith("| ")]
    rest = lines[2 + len(rows) :]
    under = [line for line in rest if line]
    assert not under or rest[0] == "", rest
    return rows, under


def in_records(name, rel):
    return f"`seal/threads/{name}/{rel}`"


class Test_main:
    def test_a_close_blocks_location_does_not_count_a_finding_twice(
        self, tmp_path, capsys
    ):
        """S1. One finding located under `seal/threads/`, whose close block
        names another path there: one finding, in records alone once. Seen
        red with the records-alone count reading each `location:` line."""
        root = git_repo(tmp_path / "repo")
        item(
            root,
            rounds=[
                record(
                    finding(
                        1,
                        in_records(ITEM, "frame/design.md:3"),
                        close_location=in_records(ITEM, "frame/plan.md"),
                    )
                )
            ],
        )
        assert table(root, capsys) == ([f"| {ITEM} | 1 | 0 | 1 | 1 |"], [])

    @pytest.mark.parametrize(
        ("located", "fixed_at", "alone"),
        [
            (in_records(ITEM, "frame/design.md"), "`hooks/lib/fields.py`", 1),
            ("`hooks/lib/fields.py`", in_records(ITEM, "frame/plan.md"), 0),
        ],
    )
    def test_where_the_defect_shows_decides_records_alone(
        self, tmp_path, capsys, located, fixed_at, alone
    ):
        """S2. The finding block's `location:` decides records alone, and the
        close block's, where the fix went, does not. Seen red with
        `located` read as `paths`, where the first reads 0."""
        root = git_repo(tmp_path / "repo")
        item(root, rounds=[record(finding(1, located, close_location=fixed_at))])
        assert table(root, capsys) == ([f"| {ITEM} | 1 | 0 | {alone} | 1 |"], [])

    def test_prose_and_a_fix_fence_are_not_fields(self, tmp_path, capsys):
        """S3. A `regression:` line in prose, and a finding heading and a
        `location:` line inside the paste-ready fix's fence, count nothing:
        one finding, no regression. A count of the text's headings and
        `regression:` lines reads 2 and 1."""
        prose = (
            "Why. The earlier round read it as\n\nregression: round-1#1\n\n"
            f"and the fix:\n\n{FENCE}markdown\n### 2. another symptom\n\n"
            f"location: {in_records(ITEM, 'gaps.md')}\n{FENCE}"
        )
        root = git_repo(tmp_path / "repo")
        item(root, rounds=[record(finding(1, "`f.py:1`", prose=prose))])
        assert table(root, capsys) == ([f"| {ITEM} | 1 | 0 | 0 | 1 |"], [])

    def test_counts_a_regression_and_a_reopens_once_each(self, tmp_path, capsys):
        """The regression cell counts the findings whose finding block holds a
        `regression:` or a `reopens:` line, over every round."""
        root = git_repo(tmp_path / "repo")
        reopens = finding(2, "`f.py:2`").replace(
            "evidence: read `f.py:1`\n", "evidence: read `f.py:1`\nreopens: round-1#1\n"
        )
        item(
            root,
            rounds=[
                record(finding(1, "`f.py:1`")),
                record(finding(1, "`f.py:1`", regression="round-1#1"), reopens),
            ],
        )
        assert table(root, capsys) == ([f"| {ITEM} | 3 | 2 | 0 | 2 |"], [])

    def test_a_record_the_reader_refuses_is_not_counted_short(self, tmp_path, capsys):
        """S4. A `seal` block line the reader refuses leaves the three finding
        cells `not read`, the rounds cell holds the count, the line under the
        table names the record, the line and the refusal, and the exit is 0."""
        refused = record(finding(1, "`f.py:1`")).replace(
            "severity: must", "severity: maybe"
        )
        root = git_repo(tmp_path / "repo")
        item(root, rounds=[record(finding(1, "`f.py:1`")), refused])
        rows, under = table(root, capsys)
        assert rows == [f"| {ITEM} | not read | not read | not read | 2 |"]
        line = refused.split("\n").index("severity: maybe") + 1
        path = f"seal/threads/{ITEM}/trail/rounds/round-2.md"
        assert len(under) == 1, under
        assert under[0].startswith(f"{path}:{line}: "), under
        assert "a severity is `must` or `should`" in under[0], under

    @pytest.mark.parametrize("shape", ["not UTF-8", "a directory"])
    def test_a_record_that_cannot_be_opened_is_named_with_why(
        self, tmp_path, capsys, shape
    ):
        """A record that is not UTF-8, or that the system will not open,
        leaves the finding cells `not read`, and the line under the table names
        it from the root with why: the error's own words, and never the
        absolute path an `OSError`'s text carries, since the table is pasted
        into a public issue. Seen red against the line that printed the
        error's whole text (round 2, finding 1)."""
        root = git_repo(tmp_path / "repo")
        where = item(root, rounds=[record(finding(1, "`f.py:1`"))])
        second = where / "trail" / "rounds" / "round-2.md"
        if shape == "not UTF-8":
            second.write_bytes(b"\xff\xfe round\n")
            why = (
                "'utf-8' codec can't decode byte 0xff in position 0: invalid start byte"
            )
        else:
            second.mkdir()
            (second / "kept.md").write_text("kept\n", encoding="utf-8")
            try:
                open(second, encoding="utf-8").close()
            except OSError as problem:
                # The system's words for it: `Is a directory` on POSIX, and
                # `Permission denied` on Windows.
                why = problem.strerror
        rows, under = table(root, capsys)
        assert rows == [f"| {ITEM} | not read | not read | not read | 2 |"]
        path = f"seal/threads/{ITEM}/trail/rounds/round-2.md"
        assert under == [f"{path}: {why}"], under
        assert str(root) not in "\n".join(under), under

    @pytest.mark.parametrize("shape", ["a file", "a link to a directory of records"])
    def test_rounds_that_cannot_be_listed_read_not_read_in_every_cell(
        self, tmp_path, capsys, shape
    ):
        """A `trail/rounds` that `hooks/lib/routing.py#rounds_unreadable`
        reads as unlistable, a file or any link, holds records nobody can
        count, so all four cells read `not read`. The line under the table
        names it with every state that reader answers for, and asserts none
        of them alone. Seen red against the line that said "it is not a
        directory" whatever the state was (round 1, finding 1)."""
        root = git_repo(tmp_path / "repo")
        where = item(root)
        rounds = where / "trail" / "rounds"
        rounds.rmdir()
        if shape == "a file":
            rounds.write_text("# round 1\n", encoding="utf-8")
        else:
            held = where / "trail" / "held"
            held.mkdir()
            (held / "round-1.md").write_text(
                record(finding(1, "`f.py:1`")), encoding="utf-8"
            )
            rounds.symlink_to("held", target_is_directory=True)
        rows, under = table(root, capsys)
        assert rows == [f"| {ITEM} | not read | not read | not read | not read |"]
        path = f"seal/threads/{ITEM}/trail/rounds"
        assert under == [
            f"{path}: the round records cannot be listed: it is a link, a file, "
            "or a directory nothing can list"
        ], under

    def test_the_rows_are_the_released_items_routed_through_the_chain(
        self, tmp_path, capsys
    ):
        """S5. Of three work items, one absent at `--released-at`, one routed
        straight to the pull request, and one released and routed through the
        review chain, the table holds the third alone."""
        root = git_repo(tmp_path / "repo")
        one = record(finding(1, "`f.py:1`"))
        item(root, "1700000002-direct", rounds=[one], review="straight to the PR")
        item(root, ITEM, rounds=[one])
        released = commit_everything(str(root), "two work items")
        item(root, "1700000003-after", rounds=[one])
        commit_everything(str(root), "a third, after the release")
        code, lines, err = run(root, capsys, ref=released)
        assert code == 0, err
        assert lines == [HEADER, SEPARATOR, f"| {ITEM} | 1 | 0 | 0 | 1 |", ""]

    def test_a_declaration_that_cannot_be_read_is_named_under_the_table(
        self, tmp_path, capsys
    ):
        """A released work item whose `routing.md` is missing, or is no
        declaration `hooks/lib/routing.py#parse` reads, is no row, since
        whether it went through the review chain is not known, and the line
        under the table names its `routing.md` and why. One routed straight
        to the pull request is no row and no line, and one released and
        since removed from the tree is neither, as `seal settle` lists it
        nowhere. Seen red against the loop that skipped all of them alike
        (round 1, finding 2)."""
        root = git_repo(tmp_path / "repo")
        one = record(finding(1, "`f.py:1`"))
        item(root, ITEM, rounds=[one])
        item(root, "1700000002-direct", rounds=[one], review="straight to the PR")
        missing = item(root, "1700000004-no-routing", rounds=[one])
        (missing / "routing.md").unlink()
        broken = item(root, "1700000005-no-declaration", rounds=[one])
        (broken / "routing.md").write_text("# routing\n\nnone\n", encoding="utf-8")
        item(root, "1700000006-removed", rounds=[one])
        released = commit_everything(str(root), "the work items")
        git_out(str(root), "rm", "-rq", "seal/threads/1700000006-removed")
        commit_everything(str(root), "a work item removed after the release")
        code, lines, err = run(root, capsys, ref=released)
        assert code == 0, err
        said = "whether it went through the review chain is not read"
        assert lines[:4] == [HEADER, SEPARATOR, f"| {ITEM} | 1 | 0 | 0 | 1 |", ""]
        # The reason is the error's own words without the absolute path its
        # text carries, since the table is pasted into a public issue (round
        # 2, finding 1).
        assert lines[4] == (
            f"seal/threads/1700000004-no-routing/routing.md: {said}: "
            + os.strerror(errno.ENOENT)
        ), lines
        assert str(root) not in "\n".join(lines), lines
        assert lines[5:] == [
            "seal/threads/1700000005-no-declaration/routing.md: "
            f"{said}: it is no declaration `hooks/lib/routing.py#parse` reads",
            "",
        ], lines

    def test_refuses_a_ref_that_does_not_resolve_and_exits_2(self, tmp_path, capsys):
        """S5. A `--released-at` that names no commit prints why on stderr,
        nothing on stdout, and exits 2."""
        root = git_repo(tmp_path / "repo")
        item(root, rounds=[record(finding(1, "`f.py:1`"))])
        commit_everything(str(root), "a work item")
        code, lines, err = run(root, capsys, ref="no-such-ref")
        assert code == 2
        assert lines == [""]
        assert "no-such-ref" in err and "does not resolve" in err, err

    def test_readers_that_will_not_load_are_said_and_exit_2(
        self, tmp_path, capsys, monkeypatch
    ):
        """A reader that will not load prints why on stderr, nothing on
        stdout, and exits 2."""
        mod = counts()

        def broken():
            raise ImportError("no reader")

        monkeypatch.setattr(mod, "readers", broken)
        code = mod.main(["--root", str(git_repo(tmp_path / "repo"))])
        out, err = capsys.readouterr()
        assert code == 2 and out == ""
        assert "no reader" in err, err

    def test_accepts_a_tree_and_prints_the_comments_table_in_work_item_order(
        self, tmp_path, capsys
    ):
        """S6. The header and the separator are the table #51's comments
        carry, and the rows follow in work item id order, whatever order the
        directories were made in."""
        root = git_repo(tmp_path / "repo")
        one = record(finding(1, "`f.py:1`"))
        item(root, "1700000009-later", rounds=[one, one])
        item(root, ITEM, rounds=[one])
        rows, under = table(root, capsys)
        assert rows == [
            f"| {ITEM} | 1 | 0 | 0 | 1 |",
            "| 1700000009-later | 2 | 0 | 0 | 2 |",
        ]
        assert under == []


class Test_why_not:
    def test_accepts_an_os_error_and_says_its_strerror_without_its_path(self):
        """An `OSError` carrying an errno is said in its `strerror` alone, so
        the absolute filename its text holds never reaches the table pasted
        into a public issue (round 2, finding 1)."""
        problem = OSError(errno.ENOENT, os.strerror(errno.ENOENT), "/abs/routing.md")
        assert "/abs/routing.md" in str(problem)
        assert counts().why_not(problem) == os.strerror(errno.ENOENT)

    def test_refuses_to_say_none_for_an_os_error_with_no_strerror(self):
        """An `OSError` built with no errno has no `strerror`, and is said
        whole rather than as `None`. No `open` in `main` raises one, so only
        this case reaches the arm. Seen red with `and problem.strerror`
        removed, which said `None` (round 3, finding 1)."""
        assert counts().why_not(OSError("no errno")) == "no errno"
        assert counts().why_not(OSError()) == ""


test_census = census_case(TARGET)

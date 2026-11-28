"""`lib/routing.py`: the routing answer is recorded where its readers read
it, so nothing re-derives it.

A declaration at `agentory/threads/<work-item-id>/routing.md` is what the pull
request's check reads, through `routing.declarations`. Failure direction: a declaration
that cannot be read is not a declaration, and an optional row that cannot be
read is unanswered while the declaration stands. What a reader does with an
answer is that reader's own file's.
The cases come from `tests/test_routing_is_recorded.py` and
`tests/test_console_is_not_utf8.py` (#942's phase 6). The case of
`Test_module` on the copy without `lib/blocks.py` came in #942's round 9 fix
pass, from `tests/test_a_script_copied_alone_exits_2.py`. The two cases of
`Test_module` that hold `shown` to `tests/commonmark_oracle.py`, over the
corpus `tests/lib/test_blocks.py` builds, came in #1489's phase 3 from
`tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py`; the
oracle's own cases stand in `tests/test_commonmark_oracle.py`.
"""

import os
import subprocess
import sys

import commonmark_oracle as oracle
import gfm_table_oracle
import pytest
from block_shapes import BREAKS, RENDERER, SHAPES
from conftest import (
    ROOT,
    census_case,
    declare_automation,
    git,
    git_repo,
    linked_worktree,
    load_lib_module,
    local_home,
    names_path,
    opted_in_repo,
    symlink_or_skip,
    two_axis_text,
    with_row,
    write,
)
from test_blocks import CORPUS, as_read
from test_tables import leaves_both

TARGET = "lib/routing.py"

routing = load_lib_module("routing.py", "iadd_routing")

CHAIN = "through the review chain"
DIRECT = "straight to the PR"

OPTIONAL_ROWS = (
    (routing.PLANNING, "planning"),
    (routing.IMPLEMENTATION, "implementation"),
    (routing.AUTOMATION, "automation"),
)


def _absent_optional_rows_read_as_nothing(paths):
    """`{row: how many of `paths` omit it}`, asserting each omission parses as
    unanswered — one loop for the real declarations and a built one."""
    omitted = {row: 0 for row, _ in OPTIONAL_ROWS}
    for path in paths:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        parsed = routing.parse(text)
        assert parsed is not None, path
        for row, key in OPTIONAL_ROWS:
            if f"| {row} |" in text:
                continue
            omitted[row] += 1
            assert parsed[key] is None, (
                f"{path} has no `{row}` row and did not read as unanswered on "
                f"that axis -- an absent optional row has to read as nothing, "
                f"or every declaration like it carries an answer its author never gave"
            )
    return omitted


def with_planning(answer):
    """`two_axis_text()` with a `Planning` row in front of `Branch`."""
    return two_axis_text().replace("| Branch |", f"| Planning | {answer} |\n| Branch |")


# The shape ids and their texts are `tests/block_shapes.py`'s. "red at base"
# means the case fails against the routing reader as it stood before #667
# changed it; "pins" means it passes there too.


def declared(name):
    """The shape's parse, as (review, branch), or None."""
    from block_shapes import SHAPES

    parsed = routing.parse("\n".join(SHAPES[name]) + "\n")
    return None if parsed is None else (parsed["review"], parsed["branch"])


BREAK_NAMES = ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"]


class Test_table_rows:
    def test_accepts_a_two_cell_row_as_its_label_and_value(self):
        assert routing.table_rows("| Review | through the review chain |\n") == [
            ("Review", "through the review chain")
        ]

    @pytest.mark.parametrize(
        "line",
        ["Review | through the review chain", "| Review |"],
        ids=["no-leading-pipe", "one-cell"],
    )
    def test_refuses_a_line_that_is_no_two_cell_row(self, line):
        """Prose that holds a pipe is no row, and a row with one cell has no
        value to read (#1017, the body's two `table_rows` rows)."""
        assert routing.table_rows(line + "\n") == []

    @pytest.mark.parametrize(
        "row, value",
        [
            ("| Branch | fix/a\\|b |", "fix/a|b"),
            ("| Branch | fix/a \\|", "fix/a |"),
            ("| Branch | fix/a", "fix/a"),
            ("| Branch | fix/a | b |", "fix/a"),
            (f"| Branch | fix/a{BREAKS['LS']}b |", f"fix/a{BREAKS['LS']}b"),
        ],
        ids=[
            "an escaped pipe",
            "an escaped last pipe",
            "no closing pipe",
            "a third cell",
            "a U+2028 inside a cell",
        ],
    )
    def test_reads_each_row_as_cmark_gfm_renders_it(self, row, value):
        """S1, S2 and S3 of #1574. The rows are split by
        `lib/tables.py#table_cells`, so an escaped pipe is one literal pipe in
        its cell, a row whose closing pipe is left off is a row, and a row
        wider than two cells is read as its first two, each as cmark-gfm
        renders it under the two-cell header. The lines are
        `lib/blocks.py#gfm_lines`, so a U+2028, which `str.splitlines` ends a
        line at, stays inside its cell. The delimiter row is no row."""
        text = "| Axis | Answer |\n|---|---|\n" + row + "\n"
        assert gfm_table_oracle.rows_under(text, ("Axis", "Answer")) == [
            ("Branch", value)
        ]
        assert routing.table_rows(text) == [("Axis", "Answer"), ("Branch", value)]


class Test_parse:
    """Where two cases call `parse` alike on the two-axis declaration, the
    declaration they hold it against differs: none, one carrying a row the
    reader no longer reads, or one answering `no` for automation. Where two
    have one body, the Implementation answer they write differs: an old name
    or a sentence."""

    def test_accepts_a_two_axis_declaration_with_no_optional_row_answered(self):
        """S1, and S8 at the parser. Twelve of these are committed in this
        repository at the base of this work, thirteen at its head. A third or
        a fourth axis that invalidated them would make each one no declaration,
        and the pull request's check would read the branch it names as
        undeclared."""
        parsed = routing.parse(two_axis_text())
        assert parsed is not None
        assert parsed["review"] == CHAIN
        assert parsed["implementation"] is None
        assert parsed["planning"] is None

    def test_a_row_the_reader_does_not_read_changes_no_answer(self):
        """#1277: a declaration written before the `Answer pressed` row left
        the template still carries it, and reads with the answers it gives
        without the row. The committed declarations held this until the
        settle removes them; this case holds it after."""
        legacy = with_row("Answer pressed", "automation")
        assert routing.parse(two_axis_text()) is not None
        assert routing.parse(legacy) == routing.parse(two_axis_text())

    def test_accepts_the_third_axis_where_it_is_there(self):
        """S2."""
        for answer in routing.IMPLEMENTATION_ANSWERS:
            text = two_axis_text().replace(
                "| Branch |", f"| Implementation | {answer} |\n| Branch |"
            )
            assert routing.parse(text)["implementation"] == answer, answer

    def test_reads_the_answer_written_before_the_rename_as_unanswered(self):
        """S2 of #1142: a declaration written before #1051 renamed the plugin
        and its agents names the implementer by its old name, and that answer is
        read as any other answer outside the vocabulary is: the declaration
        parses, and the axis is unanswered."""
        text = two_axis_text().replace(
            "| Branch |",
            "| Implementation | smith |\n| Branch |",
        )
        parsed = routing.parse(text)
        assert parsed is not None, "the old answer rejected the declaration"
        assert parsed["implementation"] is None
        assert parsed["review"] == CHAIN

    def test_accepts_the_fourth_axis_where_it_is_there(self):
        """The vocabulary is `framer` and `the session`, and the second is the same
        string the third axis uses -- one vocabulary, not two spellings of one."""
        for answer in routing.PLANNING_ANSWERS:
            assert routing.parse(with_planning(answer))["planning"] == answer, answer
        assert routing.BY_SESSION in routing.PLANNING_ANSWERS

    def test_accepts_the_automation_row_where_it_is_there(self):
        """S8's shape for the fifth row. `yes` is a run that goes to its
        destination without stopping; `no` is a run that may come back and ask."""
        for answer in routing.AUTOMATION_ANSWERS:
            parsed = routing.parse(with_row(routing.AUTOMATION, answer))
            assert parsed["automation"] == answer, answer

    def test_reads_an_escaped_pipe_and_an_open_row_as_cmark_gfm_does(self):
        """S1 and S2 of #1574. A `Branch` value holding an escaped pipe is the
        branch with one literal pipe, where the reader once split the cell at
        it and read a backslash, and a `Planning` row written without its
        closing pipe still answers."""
        text = two_axis_text(branch="fix/a\\|b").replace(
            "| Branch |", "| Planning | framer\n| Branch |"
        )
        parsed = routing.parse(text)
        assert parsed is not None, text
        assert (parsed["branch"], parsed["planning"]) == ("fix/a|b", "framer")

    def test_accepts_a_declaration_below_a_comment_opener_nobody_closed(self):
        """#872 round 3, finding 10. `lib/routing.py#shown` keeps the reading
        it gave before #667 wherever its walk is unsure, and that reading hid
        nothing, so a table below a line-start comment opener nobody closed
        still declares, although a renderer hides it. R3 holds the fence half;
        this holds the comment half, which no case did."""
        text = "<" + "!-- nobody closed this\n\n" + two_axis_text()
        parsed = routing.parse(text)
        assert parsed is not None and parsed["review"] == CHAIN, parsed

    @pytest.mark.parametrize("name", BREAK_NAMES)
    def test_accepts_a_declaration_after_a_break_commonmark_does_not_honour(self, name):
        """#667 round 1, 🟡 1. `str.splitlines` ends a line at U+2028, NEL, a
        form feed and five more characters, and CommonMark does not, so a `<!--`
        after one began a line for the walk and no line for a renderer: the walk
        hid the table under it, and `parse` answered None where the base read the
        declaration. The reader splits its text with `lib/blocks.py#gfm_lines`,
        so the `<!--` stays mid-line and hides nothing."""
        from block_shapes import BREAKS, OPEN, TABLE

        text = "\n".join([f"A note{BREAKS[name]}{OPEN}", "", *TABLE, "-->"]) + "\n"
        parsed = routing.parse(text)
        assert parsed is not None and parsed["review"] == CHAIN, parsed

    @pytest.mark.parametrize(
        "name, expected",
        [
            # red at base: a fenced example below the table answered for it (#658)
            ("R1", (CHAIN, "feature/x")),
            # red at base: the whole table inside a closed fence was a declaration
            ("R2", None),
            # pins, and reverses 1790635413's assertion: a fence nobody closed is
            # not a block, so the declaration under it still reads
            ("R3", (CHAIN, "feature/x")),
            # pins: a fence line inside a closed comment above the table opens
            # nothing (1790635413 round 2, 🟡 2)
            ("R4", (CHAIN, "feature/x")),
            # red at base: a Review row parked in a closed comment below answered
            ("R5", (CHAIN, "feature/x")),
            # red at base: a mid-line opener nobody closed switches off no fence
            # below it (1790635413 round 3, 🟡 1), with and without a blank line
            ("R6", (CHAIN, "feature/x")),
            ("R6b", (CHAIN, "feature/x")),
            # red at base: nor does one an example's comment below seems to close
            # (1790635413 round 3, ⬜ 3)
            ("R7", (CHAIN, "feature/x")),
            # red at base: a line-start opener nobody closed is not a block, so
            # the fenced example below it is still fenced
            ("R8", (CHAIN, "feature/x")),
            # red at base: a comment that closes below the table parks all of it
            ("R9", None),
        ],
        ids=lambda value: value if isinstance(value, str) else "",
    )
    def test_the_routing_shapes_read_as_the_frame_expects(self, name, expected):
        """S10. A row inside a fenced block or a comment block that closes is no
        answer, and `parse` kept the last row of a label, so before this an
        example or a parked row below the table overrode it (since #867 a label
        shown twice has no value at all). A table wholly
        hidden is no declaration (R2, R9): the direction this module fails in,
        and the ask that follows is the one every unreadable `routing.md` gets."""
        assert declared(name) == expected

    @pytest.mark.parametrize(
        "label, first, second",
        [
            ("Review", DIRECT, CHAIN),
            ("Review", CHAIN, CHAIN),
            ("Destination", "open the pull request", "stop before the pull request"),
            ("Branch", "feature/y", "feature/x"),
        ],
        ids=[
            "review, two answers",
            "review, one answer twice",
            "destination",
            "branch",
        ],
    )
    def test_refuses_a_strict_label_written_twice(self, label, first, second):
        """S5 of #867 at the parser. `parse` kept the LAST row of a label, so a
        second `Review` row below the first answered for it and nothing said
        there were two. A label written twice has no value, the rule
        `lib/config.py#config_value` gives a config key; for a strict label that
        makes the file no declaration. Seen red against the last-wins parser:
        each shape parsed, `feature/x` and the chain answering."""
        answers = {
            "Review": CHAIN,
            "Destination": "open the pull request",
            "Branch": "feature/x",
        }
        doubled = "| Axis | Answer |\n|---|---|\n" + "".join(
            f"| {lab} | {first} |\n| {lab} | {second} |\n"
            if lab == label
            else f"| {lab} | {answer} |\n"
            for lab, answer in answers.items()
        )
        assert [lab for lab, _ in routing.table_rows(doubled)].count(label) == 2
        assert routing.parse(doubled) is None, doubled

    def test_refuses_a_review_answer_outside_the_vocabulary(self):
        """The vocabulary is fixed: `maybe later` is not one of the two ways on,
        so the file is no declaration and the pull request's check reads the
        branch as undeclared.
        This case asks the parser."""
        text = two_axis_text().replace(
            f"| Review | {CHAIN} |", "| Review | maybe later |"
        )
        assert routing.parse(text) is None

    def test_refuses_an_unreadable_third_axis_as_an_answer_and_keeps_the_declaration(
        self,
    ):
        """S3. The failure direction is "this axis was not answered", never "this
        file is not a declaration" -- the second would take the review answer down
        with it, which is a gate un-silenced by a typo in a row nothing gates on."""
        text = two_axis_text().replace(
            "| Branch |", "| Implementation | whoever gets to it |\n| Branch |"
        )
        parsed = routing.parse(text)
        assert parsed is not None, "an unreadable third axis rejected the declaration"
        assert parsed["implementation"] is None
        assert parsed["review"] == CHAIN

    def test_refuses_an_unreadable_fourth_axis_as_an_answer_and_keeps_the_declaration(
        self,
    ):
        """S9 at the parser. The failure direction is the third axis's: "this axis
        was not answered", never "this file is not a declaration"."""
        for spelling in ("whoever gets to it", "`framer`", "Framer", "FRAMER", ""):
            parsed = routing.parse(with_planning(spelling))
            assert parsed is not None, f"`{spelling}` rejected the whole declaration"
            assert parsed["planning"] is None, spelling
            assert parsed["review"] == CHAIN, spelling

    def test_refuses_an_unreadable_automation_answer(self):
        """S8's second half. The failure direction is the third axis's: "this row
        was not answered", never "this file is not a declaration".

        `unattended` and `true` are in the list because they are what a session
        reaching for the idea rather than for the vocabulary would write, and both
        have to land on "nobody was asked" rather than on a confident yes.
        `complete` is question 1's option label that writes `yes` here, and
        `automation` was that label before #1459 and is the row's name in lower
        case; each is what a session that takes the label for the row's answer
        writes.
        """
        for spelling in (
            "unattended",
            "true",
            "`yes`",
            "Yes",
            "YES",
            "maybe",
            "automation",
            "complete",
            "",
        ):
            parsed = routing.parse(with_row(routing.AUTOMATION, spelling))
            assert parsed is not None, f"`{spelling}` rejected the whole declaration"
            assert parsed["automation"] is None, spelling
            assert parsed["review"] == CHAIN, spelling

    def test_refuses_an_optional_label_written_twice_as_an_answer(self):
        """S5's second half. An optional label doubled is unanswered, on the
        terms an unreadable optional answer already has: the declaration stands.
        Seen red against the last-wins parser: `planning` read `framer`."""
        text = two_axis_text().replace(
            "| Branch |",
            "| Planning | the session |\n| Planning | framer |\n| Branch |",
        )
        parsed = routing.parse(text)
        assert parsed is not None and parsed["review"] == CHAIN
        assert parsed["planning"] is None
        for label in (routing.IMPLEMENTATION, routing.AUTOMATION):
            answers = {
                routing.IMPLEMENTATION: routing.IMPLEMENTATION_ANSWERS,
                routing.AUTOMATION: routing.AUTOMATION_ANSWERS,
            }[label]
            twice = with_row(label, answers[0]).replace(
                "| Branch |", f"| {label} | {answers[0]} |\n| Branch |"
            )
            parsed = routing.parse(twice)
            assert parsed is not None, label
            assert {
                routing.IMPLEMENTATION: parsed["implementation"],
                routing.AUTOMATION: parsed["automation"],
            }[label] is None, label

    def test_refuses_one_optional_axis_answering_for_the_other(self):
        """Two optional rows read from one table is where a fold-together would
        hide: `Planning` answered and `Implementation` absent must not read as both
        answered, and the reverse must not either."""
        text = two_axis_text().replace(
            "| Branch |", "| Planning | framer |\n| Branch |"
        )
        parsed = routing.parse(text)
        assert parsed["planning"] == routing.BY_FRAMER
        assert parsed["implementation"] is None

        text = two_axis_text().replace(
            "| Branch |", "| Implementation | crafter |\n| Branch |"
        )
        parsed = routing.parse(text)
        assert parsed["implementation"] == routing.BY_CRAFTER
        assert parsed["planning"] is None

    def test_refuses_any_optional_row_answering_for_another(self, repo):
        """Three optional rows read from one table is where a fold-together hides.

        The case above pins the pair that existed before; this is the same
        property over all three, which is the class rather than the two instances
        of it (contract rule 12).
        """
        keys = {
            routing.PLANNING: ("planning", routing.BY_FRAMER),
            routing.IMPLEMENTATION: ("implementation", routing.BY_CRAFTER),
            routing.AUTOMATION: ("automation", routing.AUTOMATION_YES),
        }
        for label, (key, answer) in keys.items():
            parsed = routing.parse(with_row(label, answer))
            assert parsed[key] == answer, label
            for other_label, (other_key, _) in keys.items():
                if other_label == label:
                    continue
                assert parsed[other_key] is None, (
                    f"answering `{label}` also answered `{other_label}`"
                )

    def test_an_absent_automation_row_is_not_the_same_fact_as_a_chosen_no(self):
        """#151's lesson on this row, asserted rather than only written down.

        A chosen `no` says a person was asked and said the run may stop. An absent
        row says nobody was ever asked. Collapsing them is what made an `agentory/` root
        somebody chose byte-identical to one a preset produced, and it is the whole
        reason the unchecked half of the box writes a VALUE.

        The parser cannot tell a reader which is which beyond `None`, so what this
        pins is that the two texts are not the same text and do not parse the same
        way.
        """
        chosen = routing.parse(with_row(routing.AUTOMATION, routing.AUTOMATION_NO))
        never_asked = routing.parse(two_axis_text())
        assert chosen["automation"] == routing.AUTOMATION_NO
        assert never_asked["automation"] is None
        assert chosen != never_asked, (
            "a declaration that answered `no` and one nobody ever asked parse "
            "identically, which is the state the row exists to end"
        )

    def test_an_absent_optional_row_reads_as_nothing_over_a_built_declaration(
        self, tmp_path
    ):
        """The shape the real corpus may stop holding once a fold retires the
        declarations written before the optional rows existed: one that carries
        none of them, read through the same loop."""
        path = tmp_path / "routing.md"
        path.write_text(two_axis_text(), encoding="utf-8")
        omitted = _absent_optional_rows_read_as_nothing([str(path)])
        assert all(omitted.values()), omitted


class Test_current_branch:
    def test_accepts_the_branch_checked_out(self, tmp_path):
        repo = git_repo(tmp_path / "repo")
        git(repo, "checkout", "-q", "-b", "feature/x")
        assert routing.current_branch(str(repo)) == "feature/x"

    def test_refuses_a_detached_head_and_a_git_that_did_not_answer(
        self, tmp_path, monkeypatch
    ):
        """A detached HEAD matches no declaration, and neither does a git
        past `lib/gitcmd.py#TIMEOUT`: both read as `""`, never as an
        exception (#1573)."""
        repo = git_repo(tmp_path / "repo")
        git(repo, "checkout", "-q", "-b", "feature/x")
        git(repo, "checkout", "-q", "--detach")
        assert routing.current_branch(str(repo)) == ""
        git(repo, "checkout", "-q", "feature/x")

        def timed_out(command, **kwargs):
            raise subprocess.TimeoutExpired(command, kwargs.get("timeout"))

        monkeypatch.setattr(routing.gitcmd.subprocess, "run", timed_out)
        assert routing.current_branch(str(repo)) == ""


class Test_declarations:
    def test_accepts_a_declaration_under_the_repositorys_root(self, tmp_path):
        repo = opted_in_repo(tmp_path / "declared" / "repo")
        item = repo / "agentory" / "threads" / "1780000000-work"
        item.mkdir(parents=True)
        (item / "routing.md").write_text(two_axis_text(), encoding="utf-8")
        found = routing.declarations(str(repo))
        assert [p for p, _ in found] == [str(item / "routing.md")]

    def test_refuses_a_repository_with_no_root_whatever_the_cwd_holds(
        self, tmp_path, monkeypatch
    ):
        """No root, no declarations, even where this process sits beside a
        `specs/` holding one: the work items are read under the root and
        nowhere else (#1017, the body's `declarations` row)."""
        repo = git_repo(tmp_path / "plain")
        here = tmp_path / "here"
        item = here / "specs" / "1780000000-work"
        item.mkdir(parents=True)
        (item / "routing.md").write_text(two_axis_text(), encoding="utf-8")
        monkeypatch.chdir(here)
        assert routing.declarations(str(repo)) == []


class Test_open_declarations:
    """#1608. A declaration is open where the branch it names is checked out
    in a worktree of the repository `cwd` stands in, which
    `hooks/ask-under-automation.py` reads. The pairs differ by the tree the
    fixture builds: which branches are checked out where, and which root
    holds the declaration."""

    def test_accepts_a_declaration_on_the_branch_checked_out(self, tmp_path):
        """S5's first tree: one `routing.md` on the checked-out branch is
        answered whatever its `Automation` row reads, here `no`."""
        repo = git_repo(tmp_path / "repo")
        git(repo, "checkout", "-q", "-b", "feature/x")
        path = declare_automation(repo / "agentory", "no", "feature/x")
        found = routing.open_declarations(str(repo))
        assert [(p, d["automation"]) for p, d in found] == [(str(path), "no")]

    def test_accepts_a_worktree_path_git_spells_otherwise_in_its_native_spelling(
        self, tmp_path, monkeypatch
    ):
        """Git prints a worktree's path with `/` on Windows, and
        `declarations` joins the records' path onto it with `\\`, so the path
        is normalised where git hands it over, as `lib/optin.py#home_paths`
        does. A listing whose every path ends in `/.` spells it otherwise on
        every platform, and the pair still answers the native spelling."""
        repo = git_repo(tmp_path / "repo")
        git(repo, "checkout", "-q", "-b", "feature/x")
        path = declare_automation(repo / "agentory", "yes", "feature/x")
        real = routing.gitcmd.git

        def spelt_otherwise(cwd, *args, **kwargs):
            done = real(cwd, *args, **kwargs)
            lines = [
                line + "/." if line.startswith(routing.WORKTREE_LINE) else line
                for line in done.stdout.split("\n")
            ]
            return subprocess.CompletedProcess(
                done.args, done.returncode, "\n".join(lines), done.stderr
            )

        monkeypatch.setattr(routing.gitcmd, "git", spelt_otherwise)
        found = routing.open_declarations(str(repo))
        assert [p for p, _ in found] == [str(path)]

    def test_refuses_a_branch_no_worktree_has_checked_out(self, tmp_path):
        """S5. A work item's directory outlives its run, so a declaration
        whose branch no worktree has checked out is not open, whatever its
        `Automation` row reads."""
        repo = git_repo(tmp_path / "repo")
        git(repo, "checkout", "-q", "-b", "feature/x")
        declare_automation(repo / "agentory", "yes", "feature/released")
        assert routing.open_declarations(str(repo)) == []

    def test_refuses_a_repository_with_no_root_and_a_directory_outside_git(
        self, tmp_path
    ):
        """S5's last two trees: no root, and no repository, answer `[]`,
        and so does an empty `cwd`, which names no repository."""
        repo = git_repo(tmp_path / "plain")
        git(repo, "checkout", "-q", "-b", "feature/x")
        outside = tmp_path / "outside"
        outside.mkdir()
        for cwd in (str(repo), str(outside), ""):
            assert routing.open_declarations(cwd) == [], cwd

    def test_accepts_a_linked_worktrees_declaration_once_in_shared_mode(
        self, repo, tmp_path
    ):
        """S6. The session sits in the main checkout, on a branch no
        declaration names, and the work item's declaration stands in the
        root of a linked worktree on `feature/x`: it is open, once."""
        other = linked_worktree(repo, tmp_path)
        path = declare_automation(other / "agentory", "yes", "feature/x")
        found = routing.open_declarations(str(repo))
        assert [os.path.realpath(p) for p, _ in found] == [os.path.realpath(path)]

    def test_accepts_a_local_roots_declaration_once_from_two_worktrees(
        self, repo, tmp_path
    ):
        """S6 in local mode. Both worktrees answer the one root under the
        common git directory, so its `routing.md` is read twice and counted
        once, by its real path."""
        linked_worktree(repo, tmp_path)
        path = declare_automation(local_home(repo), "yes", "feature/x")
        found = routing.open_declarations(str(repo))
        assert [os.path.realpath(p) for p, _ in found] == [os.path.realpath(path)]

    def test_refuses_to_raise_where_git_is_not_on_path(self, tmp_path, monkeypatch):
        """S7. A git that does not start raises `lib/gitcmd.py#Failed`, a
        `SystemExit`, and `open_declarations` answers `[]` in its place."""
        repo = git_repo(tmp_path / "repo")
        git(repo, "checkout", "-q", "-b", "feature/x")
        declare_automation(repo / "agentory", "yes", "feature/x")
        empty = tmp_path / "no-git"
        empty.mkdir()
        monkeypatch.setenv("PATH", str(empty))
        assert routing.open_declarations(str(repo)) == []

    def test_refuses_a_listing_from_a_git_that_exited_non_zero(
        self, tmp_path, monkeypatch
    ):
        """A git that exits non-zero gave no answer, whatever it printed: a
        stub `git` first on PATH prints a listing that would open the
        declaration on the checked-out branch, and exits 1."""
        if os.name == "nt":
            pytest.skip("the stub `git` is a sh script, which Windows does not start")
        repo = git_repo(tmp_path / "repo")
        git(repo, "checkout", "-q", "-b", "feature/x")
        declare_automation(repo / "agentory", "yes", "feature/x")
        stub = tmp_path / "stub"
        stub.mkdir()
        (stub / "git").write_text(
            "#!/bin/sh\n"
            f"printf 'worktree %s\\nbranch refs/heads/feature/x\\n' '{repo}'\n"
            "exit 1\n",
            encoding="utf-8",
        )
        (stub / "git").chmod(0o755)
        monkeypatch.setenv("PATH", str(stub) + os.pathsep + os.environ["PATH"])
        assert routing.open_declarations(str(repo)) == []


class Test_read_declaration:
    """The one read of one `routing.md`, which `declarations` makes per
    work item and `settle.py` makes of a records directory `--from` names
    (#1575)."""

    def test_accepts_a_file_as_parse_reads_its_text(self, tmp_path):
        path = tmp_path / "routing.md"
        path.write_text(two_axis_text(branch="fix/y"), encoding="utf-8")
        declared = routing.read_declaration(str(path))
        assert declared == routing.parse(two_axis_text(branch="fix/y"))
        assert declared["branch"] == "fix/y"

    def test_refuses_an_absent_file_and_one_that_cannot_be_decoded(self, tmp_path):
        """Both are no declaration, as the module docstring says every
        failure here is: a file nobody can read or decode is not an answer
        somebody gave."""
        assert routing.read_declaration(str(tmp_path / "routing.md")) is None
        path = tmp_path / "utf16.md"
        path.write_bytes("| Review | through the review chain |\n".encode("utf-16"))
        assert routing.read_declaration(str(path)) is None


class Test_rounds:
    def test_accepts_the_records_lowest_round_first(self, tmp_path):
        for n in (10, 2, 1):
            write(tmp_path, f"trail/rounds/round-{n}.md", "x")
        write(tmp_path, "trail/rounds/round-2-report.md", "x")
        names = [os.path.basename(p) for p in routing.rounds(str(tmp_path))]
        assert names == ["round-1.md", "round-2.md", "round-10.md"]

    @pytest.mark.parametrize("shape", ["absent", "a file"])
    def test_refuses_an_item_with_no_rounds_directory(self, tmp_path, shape):
        """#1576, design S13: a `trail/rounds` that is a file holds no round
        record, as one that is not there holds none."""
        if shape == "a file":
            write(tmp_path, "trail/rounds", "# round 1\n")
        assert routing.rounds(str(tmp_path)) == []


class Test_rounds_unreadable:
    def test_accepts_any_link(self, tmp_path):
        """A link to a directory of records is what git carries as `120000`,
        which the pull-request check calls no tree."""
        write(tmp_path, "held/round-1.md", "# round 1\n")
        (tmp_path / "trail").mkdir()
        symlink_or_skip(
            str(tmp_path / "held"), str(tmp_path / "trail" / "rounds"), directory=True
        )
        assert routing.rounds_unreadable(str(tmp_path)) is True

    @pytest.mark.parametrize("shape", ["absent", "a directory", "a file"])
    def test_refuses_no_rounds_a_listable_directory_and_a_file(self, tmp_path, shape):
        """#1576, design S13: a `trail/rounds` that is a file reads as no
        round record, so it is not told apart from one that is not there.
        Seen red against the reader that answered True for it."""
        if shape == "a directory":
            write(tmp_path, "trail/rounds/round-1.md", "# round 1\n")
        if shape == "a file":
            write(tmp_path, "trail/rounds", "# round 1\n")
        assert routing.rounds_unreadable(str(tmp_path)) is False


class Test_module:
    def test_the_template_and_the_committed_declarations_still_parse(self):
        """R10's floor, S11. `templates/records/sdd-routing.md` carries its table and a
        placeholder line below it, and it still parses; the measurement over
        every committed declaration is in the phase record."""
        with open(
            os.path.join(ROOT, "templates", "records", "sdd-routing.md"),
            encoding="utf-8",
        ) as f:
            template = f.read()
        rows = dict(routing.table_rows(template))
        assert rows.get(routing.REVIEW) in routing.REVIEW_ANSWERS, rows

    def test_a_declaration_that_cannot_be_decoded_is_not_an_answer(self, tmp_path):
        """`lib/routing.py` caught `OSError` only, and `UnicodeDecodeError` is a
        `ValueError`. An undecodable `routing.md` raised out of `declarations()`
        into the check that read it, which then decided nothing.

        The direction the module states is "no declaration", which means the pull
        request's check reads the branch as undeclared. Not silence: silence would make a corrupt file
        into a standing waiver.
        """
        sys.path.insert(0, os.path.join(ROOT, "lib"))
        import routing

        repo = opted_in_repo(tmp_path / "declared" / "repo")
        item = repo / "agentory" / "threads" / "1780000000-work"
        item.mkdir(parents=True)
        # Valid UTF-16, which is not valid UTF-8 anywhere in it.
        (item / "routing.md").write_bytes(
            "| Review | through the review chain |\n".encode("utf-16")
        )
        assert routing.declarations(str(repo)) == []

    def test_a_routing_md_that_does_not_parse_is_left_out(self, tmp_path):
        """A file under a work item that is no declaration is skipped, so the
        list holds only what `parse` read; the readable one beside it stays.
        This case asks the reader."""
        repo = opted_in_repo(tmp_path / "declared" / "repo")
        specs = repo / "agentory" / "threads"
        (specs / "1780000000-prose").mkdir(parents=True)
        (specs / "1780000000-prose" / "routing.md").write_text(
            "we decided to go through the review chain.\n", encoding="utf-8"
        )
        (specs / "1780000001-table").mkdir(parents=True)
        (specs / "1780000001-table" / "routing.md").write_text(
            two_axis_text(), encoding="utf-8"
        )
        found = routing.declarations(str(repo))
        assert [os.path.basename(os.path.dirname(p)) for p, _ in found] == [
            "1780000001-table"
        ]
        assert found[0][1]["review"] == CHAIN

    @pytest.mark.parametrize(
        "missing, siblings, purpose",
        [
            (
                "blocks.py",
                ["gitcmd.py", "optin.py"],
                "tells a live row from one quoted in a fence or parked in a comment",
            ),
            (
                "tables.py",
                ["gitcmd.py", "optin.py", "blocks.py"],
                "the row splitter this reader reads routing.md's cells through",
            ),
        ],
        ids=["without the walk", "without the row splitter"],
    )
    def test_a_reader_copied_without_the_walk_names_it(
        self, tmp_path, missing, siblings, purpose
    ):
        """#667. This module imports `lib/blocks.py`, the walk the readers
        under `lib/` share, after `lib/gitcmd.py` and `lib/optin.py`, and
        `lib/tables.py`, the row splitter, after all three (#1574), so each
        copy takes the files imported before the one it leaves out. It is a
        module, not a script: scripts import it, and a script catches the
        error or names the file first. So a copy without either raises one
        `ImportError` whose sentence names the path and what the file is for.
        `tests/lib/test_tables.py` holds `lib/tables.py` to the same."""
        name = TARGET.rsplit("/", 1)[1]
        alone = tmp_path / "lib"
        alone.mkdir()
        for file in (name, *siblings):
            with open(os.path.join(ROOT, "lib", file), encoding="utf-8") as f:
                (alone / file).write_text(f.read(), encoding="utf-8")
        done = subprocess.run(
            [
                sys.executable,
                "-c",
                f"import sys; sys.path.insert(0, {str(alone)!r}); import {name[:-3]}",
            ],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
        assert done.returncode != 0, done.stderr
        last = done.stderr.strip().splitlines()[-1]
        assert last.startswith("ImportError: cannot read "), last
        assert names_path(os.path.join(str(alone), missing), last), last
        assert purpose in last, last

    def test_the_routing_reader_never_leaves_both_readings(self):
        """Half 1, S9. `lib/routing.py#table_rows` read every line at
        `release/v0.16.0`, so its base hides nothing, and every line it skips now
        has to be one a renderer hides: a row it stops reading was never a live
        answer."""
        wrong = []
        for doc in CORPUS:
            text, lines = as_read(doc)
            new = set(range(len(lines))) - {i for i, _line in routing.shown(lines)}
            bad = leaves_both(new, set(), set(oracle.hidden_text(text)), len(lines))
            if bad:
                wrong.append((lines, bad))
        assert not wrong, f"{len(wrong)} documents, the first: {wrong[0]}"

    def test_the_routing_reader_hides_something(self):
        """The half above is empty for a reader that skips nothing, which is
        what it was. On the shapes that park or quote a table it skips the
        renderer's lines."""
        for name in ("R1", "R2", "R5", "R9"):
            lines = SHAPES[name]
            skipped = set(range(len(lines))) - {i for i, _ in routing.shown(lines)}
            assert skipped == RENDERER[name], name


test_census = census_case(TARGET)

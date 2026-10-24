"""`hooks/routing.py`: the routing answer is recorded, so the gate stops
re-deriving it.

A declaration at `seal/specs/<work-item-id>/routing.md` is what the commit gate
reads. Failure direction: a declaration that cannot be read is not a
declaration, and an optional row that cannot be read is unanswered while the
declaration stands. What the commit gate does with an answer is its own file's.
The cases come from `tests/test_routing_is_recorded.py` and
`tests/test_console_is_not_utf8.py` (#942's phase 6). Two cases of
`Test_module` came in #942's round 9 fix pass, each a case of this module
alone: the copy without `hooks/blocks.py`, from
`tests/test_a_script_copied_alone_exits_2.py`, and `WORK_ITEMS` held under
`seal/`, from `tests/test_a_reference_root_is_read_and_never_taken.py`.
"""

import os
import subprocess
import sys

import pytest
from conftest import (
    ROOT,
    census_case,
    load_hook_module,
    names_path,
    opted_in_repo,
    two_axis_text,
    with_row,
)

TARGET = "hooks/routing.py"

routing = load_hook_module("routing.py", "specseal_routing")

CHAIN = "through the review chain"
DIRECT = "straight to the PR"

OPTIONAL_ROWS = (
    (routing.PLANNING, "planning"),
    (routing.IMPLEMENTATION, "implementation"),
    (routing.AUTOMATION, "automation"),
    (routing.ANSWER_PRESSED, "pressed"),
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
                f"or the commit gate un-silences on every declaration like it"
            )
    return omitted


def with_planning(answer):
    """`two_axis_text()` with a `Planning` row in front of `Branch`."""
    return two_axis_text().replace("| Branch |", f"| Planning | {answer} |\n| Branch |")


# The shape ids are `seal/specs/1790645290-the-hooks-and-the-rider-check-read-
# fences-and-comments-by-one-rule/spec.md` *The shapes*, the texts
# `tests/block_shapes.py`'s. "red at base" means the case fails with
# `hooks/routing.py` from `3911a8cf`; "pins" means it passes there too.


def declared(name):
    """The shape's parse, as (review, branch), or None."""
    from block_shapes import SHAPES

    parsed = routing.parse("\n".join(SHAPES[name]) + "\n")
    return None if parsed is None else (parsed["review"], parsed["branch"])


BREAK_NAMES = ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"]


class Test_parse:
    def test_accepts_a_two_axis_declaration_with_no_optional_row_answered(self):
        """S1, and S8 at the parser. Twelve of these are committed in this
        repository at the base of this work, thirteen at its head. A third or
        a fourth axis that invalidated them would un-silence the commit gate on
        every one."""
        parsed = routing.parse(two_axis_text())
        assert parsed is not None
        assert parsed["review"] == CHAIN
        assert parsed["implementation"] is None
        assert parsed["planning"] is None

    def test_accepts_the_third_axis_where_it_is_there(self):
        """S2."""
        for answer in routing.IMPLEMENTATION_ANSWERS:
            text = two_axis_text().replace(
                "| Branch |", f"| Implementation | {answer} |\n| Branch |"
            )
            assert routing.parse(text)["implementation"] == answer, answer

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

    def test_accepts_the_answer_pressed_row_where_it_is_there(self):
        """S3 at the parser: the two derivations are not byte-identical."""
        for answer in routing.ANSWER_PRESSED_ANSWERS:
            parsed = routing.parse(with_row(routing.ANSWER_PRESSED, answer))
            assert parsed["pressed"] == answer, answer

    def test_accepts_a_declaration_below_a_comment_opener_nobody_closed(self):
        """#872 round 3, finding 10. `hooks/routing.py#shown` keeps the reading
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
        declaration. The walk reads where CommonMark breaks."""
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
        `hooks/config.py#value_of` gives a config row; for a strict label that
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
        so the file is no declaration and the commit gate asks. The gate's own
        case runs the same answer through the hook; this one asks the parser."""
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
        """
        for spelling in ("unattended", "true", "`yes`", "Yes", "YES", "maybe", ""):
            parsed = routing.parse(with_row(routing.AUTOMATION, spelling))
            assert parsed is not None, f"`{spelling}` rejected the whole declaration"
            assert parsed["automation"] is None, spelling
            assert parsed["review"] == CHAIN, spelling

    def test_refuses_an_unreadable_answer_pressed_row(self):
        for spelling in ("`automation`", "Automation", "everything", "option 1", ""):
            parsed = routing.parse(with_row(routing.ANSWER_PRESSED, spelling))
            assert parsed is not None, f"`{spelling}` rejected the whole declaration"
            assert parsed["pressed"] is None, spelling

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
        for label in (
            routing.IMPLEMENTATION,
            routing.AUTOMATION,
            routing.ANSWER_PRESSED,
        ):
            answers = {
                routing.IMPLEMENTATION: routing.IMPLEMENTATION_ANSWERS,
                routing.AUTOMATION: routing.AUTOMATION_ANSWERS,
                routing.ANSWER_PRESSED: routing.ANSWER_PRESSED_ANSWERS,
            }[label]
            twice = with_row(label, answers[0]).replace(
                "| Branch |", f"| {label} | {answers[0]} |\n| Branch |"
            )
            parsed = routing.parse(twice)
            assert parsed is not None, label
            assert {
                routing.IMPLEMENTATION: parsed["implementation"],
                routing.AUTOMATION: parsed["automation"],
                routing.ANSWER_PRESSED: parsed["pressed"],
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
            "| Branch |", "| Implementation | smith |\n| Branch |"
        )
        parsed = routing.parse(text)
        assert parsed["implementation"] == routing.BY_SMITH
        assert parsed["planning"] is None

    def test_refuses_any_optional_row_answering_for_another(self, repo):
        """Four optional rows read from one table is where a fold-together hides.

        The case above pins the pair that existed before; this is the same
        property over all four, which is the class rather than the two instances
        of it (contract rule 12).
        """
        keys = {
            routing.PLANNING: ("planning", routing.BY_FRAMER),
            routing.IMPLEMENTATION: ("implementation", routing.BY_SMITH),
            routing.AUTOMATION: ("automation", routing.AUTOMATION_YES),
            routing.ANSWER_PRESSED: ("pressed", routing.PRESSED_AUTOMATION),
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

    def test_refuses_the_row_name_and_the_option_label_crossed(self):
        """`Automation` is the row and `automation` is the label a person pressed.

        Deliberately one word, and the vocabularies must not cross: the row takes
        `yes`/`no` and the pressed row takes the label. Swapping them is the
        mistake a reader who saw one word makes, and both directions read as
        unanswered rather than as a confident wrong answer.
        """
        assert routing.AUTOMATION.lower() == routing.PRESSED_AUTOMATION
        crossed = routing.parse(
            with_row(routing.AUTOMATION, routing.PRESSED_AUTOMATION)
        )
        assert crossed["automation"] is None, (
            "`| Automation | automation |` read as an answer; the row takes yes/no"
        )
        crossed = routing.parse(
            with_row(routing.ANSWER_PRESSED, routing.AUTOMATION_YES)
        )
        assert crossed["pressed"] is None, (
            "`| Answer pressed | yes |` read as an answer; the row takes a label"
        )

    def test_an_absent_automation_row_is_not_the_same_fact_as_a_chosen_no(self):
        """#151's lesson on this row, asserted rather than only written down.

        A chosen `no` says a person was asked and said the run may stop. An absent
        row says nobody was ever asked. Collapsing them is what made a `seal/` root
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

    def test_pressing_the_preset_and_ticking_every_box_are_told_apart(self):
        """S3. Both produce the same four party rows; only this row differs.

        Without it the preset buys nothing, because a chosen answer goes back to
        being indistinguishable from an unread question.
        """
        preset = routing.parse(
            with_row(routing.ANSWER_PRESSED, routing.PRESSED_AUTOMATION)
        )
        by_hand = routing.parse(
            with_row(routing.ANSWER_PRESSED, routing.PRESSED_PER_AXIS)
        )
        assert preset["review"] == by_hand["review"]
        assert preset["destination"] == by_hand["destination"]
        assert preset["pressed"] != by_hand["pressed"], (
            "the row that says which answer was pressed does not distinguish them"
        )

    def test_every_declaration_in_this_repository_still_parses(self):
        """Executed against the real files, not a fixture: the declarations
        committed here are the population the optional rows exist for.

        S8 of #84 extends it rather than opening a second case beside it. What an
        optional row has to survive is a declaration that does not carry it -- a
        required row, or a row whose absence took the declaration down, would
        un-silence the commit gate on every one of those. So the assertion is over
        the declarations that OMIT each row, and never over how many answer it:
        #351 wrote the first `Planning` answer, and a case premised on nobody
        answering goes red on the commit that writes one rather than on a defect.

        The vacuity guard is over the axes together, not per axis. Every
        committed declaration answers `Implementation`, so a per-axis guard would
        be red the day it was written.

        All FOUR optional rows are swept rather than the two that existed first.
        The fifth and sixth are the direction this case is strongest in: no
        committed declaration in this tree carries either, so the population is
        every one of them, and taking the `.get` default off the new row in
        `parse()` — which is what makes an absent row an absent row — is red here
        and nowhere else.

        No count is written down here either. The docstring this replaced carried
        two -- `the twelve committed here` and `Seventy-two declarations` -- for a
        tree that held 73, and a number in a docstring is a claim nothing reads.
        """
        import glob

        root = os.path.join(os.path.dirname(__file__), "..")
        found = sorted(
            glob.glob(os.path.join(root, "seal", "specs", "*", "routing.md"))
        )
        # `assert found` and the vacuity guard over `omitted` stood here, and both
        # were floors a fold turns red (#517). The first asked whether the glob
        # found the declarations that are there, and is asked of the tree instead:
        # a second listing, by `os.listdir`, has to agree with it at any size.
        # The second asked whether the corpus holds a declaration that omits an
        # optional row, which is a question about what the repository happens to
        # hold, and it moves to
        # `test_an_absent_optional_row_reads_as_nothing_over_a_built_declaration`.
        specs = os.path.join(root, "seal", "specs")
        listed = sorted(
            os.path.join(specs, n, "routing.md")
            for n in (os.listdir(specs) if os.path.isdir(specs) else [])
            if os.path.isfile(os.path.join(specs, n, "routing.md"))
        )
        assert [os.path.normpath(p) for p in found] == [
            os.path.normpath(p) for p in listed
        ], "the glob and the listing disagree about which declarations exist"
        _absent_optional_rows_read_as_nothing(found)

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


class Test_module:
    def test_the_template_and_the_committed_declarations_still_parse(self):
        """R10's floor, S11. `templates/sdd-routing.md` carries its table and a
        placeholder line below it, and it still parses; the measurement over
        every committed declaration is in the phase record."""
        root = os.path.join(os.path.dirname(__file__), "..")
        with open(
            os.path.join(root, "templates", "sdd-routing.md"), encoding="utf-8"
        ) as f:
            template = f.read()
        rows = dict(routing.table_rows(template))
        assert rows.get(routing.REVIEW) in routing.REVIEW_ANSWERS, rows

    def test_a_declaration_that_cannot_be_decoded_is_not_an_answer(self, tmp_path):
        """`hooks/routing.py` caught `OSError` only, and `UnicodeDecodeError` is a
        `ValueError`. An undecodable `routing.md` raised out of `declarations()`,
        through the commit gate, into `dispatch.py`'s `except Exception: return ""`
        — no output, which is an allow.

        The direction the module states is "no declaration", which means the gate
        goes back to asking. Not silence: silence would make a corrupt file into a
        standing waiver.
        """
        sys.path.insert(0, os.path.join(ROOT, "hooks"))
        import routing

        repo = opted_in_repo(tmp_path / "declared" / "repo")
        item = repo / "seal" / "specs" / "1780000000-work"
        item.mkdir(parents=True)
        # Valid UTF-16, which is not valid UTF-8 anywhere in it.
        (item / "routing.md").write_bytes(
            "| Review | through the review chain |\n".encode("utf-16")
        )
        assert routing.declarations(str(repo)) == []

    def test_a_routing_md_that_does_not_parse_is_left_out(self, tmp_path):
        """A file under a work item that is no declaration is skipped, so the
        list holds only what `parse` read; the readable one beside it stays.
        The commit gate's case for a malformed declaration runs the hook; this
        one asks the reader."""
        repo = opted_in_repo(tmp_path / "declared" / "repo")
        specs = repo / "seal" / "specs"
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

    def test_a_hook_reader_copied_without_the_walk_names_it(self, tmp_path):
        """#667. This module imports `hooks/blocks.py`, the walk the hook-path
        readers share, after `hooks/optin.py`, so the copy takes `optin.py`
        with it. It is a module, not a script: gates and scripts import it, a
        gate that raises is skipped and said at the end of the turn
        (`hooks/dispatch.py`, #28), and a script catches the error or names the
        file first. So a copy without the walk raises one `ImportError` whose
        sentence names the path and what the file is for.
        `tests/test_config.py` holds `hooks/config.py` to the same."""
        name, siblings = TARGET.rsplit("/", 1)[1], ["optin.py"]
        alone = tmp_path / "hooks"
        alone.mkdir()
        for file in (name, *siblings):
            with open(os.path.join(ROOT, "hooks", file), encoding="utf-8") as f:
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
        assert names_path(os.path.join(str(alone), "blocks.py"), last), last
        assert "tells a live row from one quoted in a fence or parked in a comment" in (
            last
        ), last

    def test_the_pinned_checks_read_under_the_root_alone(self):
        """#688's D3: the constant this module's walk of work items rests on,
        held under `seal/`. Widening it to a top-level `specs/` turns this red,
        which is the probe that work item's plan names for `WORK_ITEMS`.
        `tests/test_settle.py` holds `settle.py#SPECS` to the same, and
        `tests/test_a_reference_root_is_read_and_never_taken.py` classifies
        every shipped command by what keeps it off a reference root."""
        assert routing.WORK_ITEMS == "seal/specs"


test_census = census_case(TARGET)

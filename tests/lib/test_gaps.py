"""`lib/gaps.py`, one class per function.

The reader of a closing memo's `## Not verified`: a section's rows, a row's
closing word, one memo's text or file, and a work item's open rows. The
readers of a section and of a row run in the process on texts, with no git;
`Test_open_record_rows` reads the world of work items a settle can remove,
which `tests/skills/test_unverified_check.py` builds once and this file
imports. The cases came, unchanged but for the module they call, from that
file when the reader left the script (#1482).
"""

import time

import pytest
import test_unverified_check
from conftest import census_case, load_lib_module
from test_unverified_check import (
    CANONICAL,
    CLOSED_ITEM,
    OPEN_ITEM,
    TUI,
    WORK,
    memo,
    memo_at,
)

TARGET = "lib/gaps.py"

GAPS = load_lib_module("gaps.py", "gaps_for_its_own_file")
# The world of work items a settle can remove, a fixture built once in the
# file this one imports it from.
settle = test_unverified_check.settle
# `lib/blocks.py#gfm_lines`, the split `parse` reads a section through.
gfm_lines = load_lib_module("blocks.py", "blocks_for_the_gaps_cases").gfm_lines

# The sentence a section that holds nothing is told to write, pinned as the
# person reads it.
BLOCK = "the block `- nothing` with `  why: <reason>`"
# Spelt by code point, so no emoji and no invisible character stands in
# this file.
OLD_MARK = chr(0x2705)
ZERO_WIDTH_SPACE = chr(0x200B)
EMOJI_SELECTOR = chr(0xFE0F)
WORD_JOINER = chr(0x2060)


def parse(section):
    """`parse_section` over SECTION's lines after its heading, each line
    numbered as SECTION numbers it."""
    return GAPS.parse_section(gfm_lines(section)[1:], 2)


class Test__LooseHeading:
    """The matcher behind `check_text`'s near-heading hint: a level 2 or 3
    heading by the one rule, mentioning `not verified` in any case (#867
    round 1, finding 6)."""

    @pytest.mark.parametrize(
        "line",
        [
            "## Not verified",
            "### not VERIFIED, read",
            "   ## Not verified",
            "##\tNot verified",
        ],
    )
    def test_accepts_a_level_two_or_three_heading_naming_it(self, line):
        assert GAPS.LOOSE_HEADING.match(line) is True

    @pytest.mark.parametrize(
        "line",
        ["# Not verified", "#### Not verified", "#120) not verified", "## Not done"],
    )
    def test_refuses_another_level_a_line_that_is_no_heading_and_another_name(
        self, line
    ):
        assert GAPS.LOOSE_HEADING.match(line) is False


class Test_is_header:
    def test_accepts_item_in_any_case(self):
        assert GAPS.is_header([" ITEM ", "Who"]) is True

    @pytest.mark.parametrize("cells", [[], ["Thing", "Who"]], ids=["no cells", "thing"])
    def test_refuses_no_cells_and_another_first_column(self, cells):
        assert GAPS.is_header(cells) is False


def line_of(section, needle):
    """The line number SECTION gives its first line that is NEEDLE."""
    return section.split("\n").index(needle) + 1


class Test_parse_section:
    @pytest.mark.parametrize(
        "row, closed",
        [
            (
                "| closed how the gate renders in a TUI | seen on screen |",
                "how the gate renders in a TUI",
            ),
            (
                "| closed\thow the gate renders in a TUI | seen on screen |",
                "how the gate renders in a TUI",
            ),
            # The open item whose own text begins with the word reads closed,
            # which only a reader catches.
            ("| closed issues are not re-read | the owner |", "issues are not re-read"),
            ("| closed-loop control on Windows | a maintainer |", None),
            ("| enclosed paths on Windows | a maintainer |", None),
            ("| whether `a \\| b` parses | the next session |", None),
            # #1167, *Scope* item 9: the word is read exactly, so a row opening
            # with it in another case or with punctuation after it is open,
            # the safe direction. Seen red against the refusal of each.
            ("| closed. how the gate renders in a TUI | seen on screen |", None),
            ("| closed: how the gate renders in a TUI | seen on screen |", None),
            ("| Closed how the gate renders in a TUI | seen on screen |", None),
            ("| CLOSED how the gate renders in a TUI | seen on screen |", None),
        ],
        ids=[
            "the word",
            "the word and a tab",
            "an item that begins with it",
            "a word that begins with it",
            "a word that holds it",
            "an escaped pipe",
            "the word and a full stop",
            "the word and a colon",
            "capitalised",
            "upper case",
        ],
    )
    def test_accepts_open_rows_and_the_word_that_closes_one(self, row, closed):
        open_rows, closed_rows, errors = parse(CANONICAL.replace(TUI, row))
        assert not errors, errors
        if closed is None:
            assert not closed_rows and len(open_rows) == 2
        else:
            assert [c[1] for c in closed_rows] == [closed] and len(open_rows) == 1

    @pytest.mark.parametrize(
        "block",
        [
            "- nothing\n  why: every claim in this item was executed.\n",
            "- nothing\n  why: every claim in this item\n    was executed.\n",
            "- nothing\n",
        ],
        ids=["one line", "continued four spaces in", "no why"],
    )
    def test_accepts_the_no_change_block_as_nothing_open(self, block):
        """S1 of #1000: silence and "nothing open" look different in the
        file, not only in the tally. The reason under `why:` is the agents'
        to read and no script's to use, so a block without it reads too
        (#1319)."""
        assert parse(f"## Not verified\n\n{block}") == ([], [], [])

    @pytest.mark.parametrize(
        "section, at, says",
        [
            ("## Not verified\n\n", 2, "the section is empty"),
            (
                "## Not verified\n\n- the TUI rendering, nobody has seen it\n",
                3,
                "found prose",
            ),
            (
                CANONICAL.replace("| Item | Who must answer |", "| Item | Who |"),
                3,
                "header is |Item|Who|",
            ),
            (
                "## Not verified\n\n| Item | Who must answer |\n| an item | someone |\n",
                3,
                "not followed by a separator row",
            ),
            (
                "## Not verified\n\n| Item | Who must answer |\n|---|---|\n",
                3,
                "no rows",
            ),
            (CANONICAL + "#120) wrapped onto its own line\n", 7, "not a table row"),
            (
                CANONICAL + "| an item | an answerer | a third cell |\n",
                7,
                "3 cells, expected 2",
            ),
            (CANONICAL + "| Item | Who must answer |\n", 7, "one table"),
            (CANONICAL + f"|-{ZERO_WIDTH_SPACE}--|---|\n", 7, "one table"),
            (CANONICAL + "| an item with no answerer | |\n", 7, "an empty cell"),
            (
                CANONICAL + f"| {ZERO_WIDTH_SPACE} | {ZERO_WIDTH_SPACE} |\n",
                7,
                "an empty cell",
            ),
            (
                CANONICAL + "| <what was not verified> | <who answers it> |\n",
                7,
                "placeholder",
            ),
            (CANONICAL + "| an item | <who answers it> |\n", 7, "placeholder"),
        ],
        ids=[
            "empty",
            "prose",
            "the old column",
            "no separator",
            "no rows",
            "an issue number",
            "three cells",
            "a second header",
            "a hidden separator",
            "an empty cell",
            "invisible cells",
            "the placeholder",
            "a placeholder answerer",
        ],
    )
    def test_refuses_a_section_it_cannot_count_at_its_line(self, section, at, says):
        errors = parse(section)[2]
        assert errors and errors[0][0] == at and says in errors[0][1], errors

    @pytest.mark.parametrize(
        "row, says",
        [
            ("| closed | done |", "bare"),
            (f"| closed{ZERO_WIDTH_SPACE} | done |", "bare"),
            (f"| closed{EMOJI_SELECTOR} | done |", "bare"),
            (f"| closed{WORD_JOINER} | done |", "bare"),
            (
                f"| {OLD_MARK}{EMOJI_SELECTOR} how the gate renders in a TUI | seen |",
                "U+2705",
            ),
            (f"| {OLD_MARK} | done |", "U+2705"),
        ],
        ids=[
            "bare",
            "a zero-width space",
            "a selector",
            "a word joiner",
            "the old mark as a keyboard emits it",
            "the bare old mark",
        ],
    )
    def test_refuses_a_bare_word_and_the_old_mark(self, row, says):
        """T4 of `1792129100-the-mechanics-leave-before-the-agents-are-rewritten`:
        a bare word, and the emoji mark. Another spelling of the word is an
        open row (#1167), `test_accepts_open_rows_and_the_word_that_closes_one`."""
        _, _, errors = parse(CANONICAL.replace(TUI, row))
        assert errors and says in errors[0][1], errors

    def test_refuses_the_old_mark_naming_the_edit(self):
        """Contract rule 14: the sentence a person reads when their overview
        still carries the old mark, pinned whole."""
        row = f"| {OLD_MARK} how the gate renders in a TUI | seen on screen |"
        _, _, errors = parse(CANONICAL.replace(TUI, row))
        assert errors[0] == (
            5,
            "the row opens with U+2705, which no longer closes a row: a closed "
            "row opens with the word `closed`, so write "
            "`| closed how the gate renders in a TUI | <what closed it> |`",
        )

    @pytest.mark.parametrize("first", ["none - x", "none", "None.", "nothing - x"])
    def test_refuses_a_section_holding_the_old_line_and_names_the_line(self, first):
        """S2 of #1000 and #1167's *Scope* item 9: the old line and its near
        misses are not the block, so the section holds neither the table nor
        the block and is refused as unreadable at that line, and the refusal
        names the line as one it did not read, pinned whole (contract rule
        14). Seen red against the refusal naming the near miss as the
        block's."""
        section = f"## Not verified\n\n{first}\n"
        assert parse(section) == (
            [],
            [],
            [
                (
                    3,
                    "expected `| Item | Who must answer |`, found prose. Prose "
                    "belongs under `## Not done`; this section is read by a "
                    f"machine. Not read: `{first}` opens like {BLOCK} and is "
                    "not it, so it was read as prose",
                )
            ],
        )

    def test_names_no_line_that_does_not_open_like_the_block(self):
        """The naming is the prose refusal's only where the line opens like
        the block: other prose is refused without it."""
        section = "## Not verified\n\n- the TUI rendering, nobody has seen it\n"
        ((_line, says),) = parse(section)[2]
        assert says.endswith("this section is read by a machine"), says

    @pytest.mark.parametrize(
        "body, bad, says",
        [
            ("- nothing\n  why:\n", "  why:", "`why` is empty"),
            ("- Nothing\n  why: x\n", "- Nothing", BLOCK),
            ("-nothing\n  why: x\n", "-nothing", BLOCK),
            ("- nothing\n   why: x\n", "   why: x", "not a field"),
            ("- nothing\n  why: x\n  who: y\n", "  who: y", "`who` is not a field"),
            (
                "- nothing\n  why: x\n" + CANONICAL.split("\n", 2)[2],
                "| Item | Who must answer |",
                "not a field",
            ),
        ],
        ids=[
            "an empty why",
            "capitalised",
            "no space after the dash",
            "why at three spaces",
            "a second field",
            "beside a table",
        ],
    )
    def test_refuses_a_near_miss_of_the_block_at_its_line(self, body, bad, says):
        """S3 of #1000: each spelling is refused at its line, saying what is
        wrong with it, and read as nothing else."""
        section = f"## Not verified\n\n{body}"
        open_rows, closed_rows, errors = parse(section)
        assert errors and errors[0][0] == line_of(section, bad), errors
        assert says in errors[0][1], errors
        assert not open_rows and not closed_rows

    def test_the_near_miss_reading_is_linear_in_the_line(self):
        """#941's round 3 met a pattern that backtracked exponentially; a
        long line of the near-miss pattern's repeated characters is read
        well inside the bound."""
        start = time.monotonic()
        for line in ("- " * 50000 + "x", " " * 100000 + "nonesuch", "-*+" * 30000):
            GAPS.parse_section([line], 1)
        assert time.monotonic() - start < 5.0


class Test_closing_word:
    @pytest.mark.parametrize(
        "cell, answer",
        [
            ("closed how it renders", ("closed", "how it renders")),
            (f"{OLD_MARK}how it renders", (OLD_MARK, "how it renders")),
            (
                f"{OLD_MARK}{EMOJI_SELECTOR} how it renders",
                (OLD_MARK, "how it renders"),
            ),
        ],
        ids=[
            "the word",
            "the old mark with no space",
            "the old mark as a keyboard emits it",
        ],
    )
    def test_accepts_the_first_word_and_the_rest(self, cell, answer):
        assert GAPS.closing_word(cell) == answer

    def test_refuses_to_invent_a_word_for_an_empty_cell(self):
        assert GAPS.closing_word("") == ("", "")


class Test_check_file:
    def test_accepts_an_overview_on_disk(self, tmp_path):
        open_rows, closed_rows, errors = GAPS.check_file(memo_at(tmp_path, CANONICAL))
        assert not errors and len(open_rows) == 2 and not closed_rows

    def test_refuses_a_file_it_cannot_open(self, tmp_path):
        _, _, errors = GAPS.check_file(str(tmp_path / "gaps.md"))
        assert (
            errors and errors[0][0] == 0 and errors[0][1].startswith("cannot be read: ")
        )


class Test_check_text:
    @pytest.mark.parametrize(
        "section, count",
        [
            (CANONICAL, 2),
            # Rows below an example are counted, and the example is no
            # second section.
            (
                CANONICAL
                + "\n```markdown\n## Not verified\n\n| Item | Who |\n```\n\n| a third item | someone |\n",
                3,
            ),
            (
                CANONICAL
                + "\n~~~markdown\n| Item | Who must answer |\n~~~\n\n| a third item | someone |\n",
                3,
            ),
            # Round 1 of #1000: a row quoting the opener in a code span hides
            # no row below it.
            (
                CANONICAL.replace(
                    "| how the gate renders in a TUI |",
                    "| whether `<!--` in a cell hides rows |",
                ),
                2,
            ),
            # #1012: a bare opener later in a line is text, so it hides no row
            # below it either.
            (
                CANONICAL.replace(
                    "| how the gate renders in a TUI |",
                    "| whether a bare <!-- in a cell hides rows |",
                ),
                2,
            ),
        ],
        ids=[
            "the table",
            "a fenced example",
            "a tilde fence",
            "an opener in a span",
            "a bare opener mid-line",
        ],
    )
    def test_accepts_the_rows_of_the_one_section(self, section, count):
        open_rows, _, errors = GAPS.check_text(memo(section))
        assert not errors, errors
        assert len(open_rows) == count

    def test_accepts_a_line_opening_with_an_issue_number_inside_the_section(self):
        """S9 of #867: the line is paragraph text inside the section, so the
        row below it is counted and the line is named as no row."""
        text = memo(
            CANONICAL
            + "#120) wrapped onto its own line\n| a third item | the owner |\n"
        )
        open_rows, _, errors = GAPS.check_text(text)
        assert len(open_rows) == 3
        assert [message for _, message in errors] == [
            "a line inside the table that is not a table row"
        ]

    @pytest.mark.parametrize(
        "heading",
        [
            "## Not verified (who must answer)",
            "## Blocked / not verified (who must answer)",
            "## Not Verified",
        ],
    )
    def test_refuses_a_spelling_it_does_not_know_and_names_it(self, heading):
        """All three spellings were in this corpus. The failure prevented is
        a reader that shrugs and returns zero."""
        _, _, errors = GAPS.check_text(
            memo(CANONICAL.replace("## Not verified", heading))
        )
        assert errors == [
            (1, f"no `## Not verified` section (found `{heading}` at line 7)")
        ]

    @pytest.mark.parametrize(
        "text, error",
        [
            (
                memo("## Fed back into the spec\n\nnone.\n"),
                (1, "no `## Not verified` section"),
            ),
            (
                memo(CANONICAL + "\n" + CANONICAL),
                (14, "more than one `## Not verified` section: lines 7, 14"),
            ),
            (
                memo("## Not verified\n\n## Fed back into the spec\n\nnone.\n"),
                (8, "the section is empty: write the table, or " + BLOCK),
            ),
        ],
        ids=["none", "two", "an empty one"],
    )
    def test_refuses_no_section_two_sections_and_an_empty_one(self, text, error):
        assert GAPS.check_text(text)[2] == [error]

    @pytest.mark.rule("record-comment-line-refused")
    def test_refuses_a_comment_line_at_its_line(self):
        """S6 of #1012: the guidance comment an overview started before #1005
        carries is refused at its first line, before any row is counted,
        where the reader that kept a comment state read past it. The words
        are pinned here, once, because they are all a consuming repository
        is told to do (contract rule 14); every other case compares against
        the constant, which pins that each reader says the one message."""
        text = memo(
            "## Not verified\n\n<!-- guidance:\n| closed <item> | <what closed it> |"
            "\n-->\n\n" + CANONICAL.split("\n", 2)[2] + "<!-- a second -->\n"
        )
        line = text.splitlines().index("<!-- guidance:") + 1
        said = (
            "the line begins with `<!--`, and a record carries no HTML comment: "
            "the check reads one as text, so delete the comment"
        )
        assert GAPS.check_text(text) == ([], [], [(line, said)])


class Test_open_record_rows:
    def test_accepts_every_open_item_of_the_record(self, settle):
        assert GAPS.open_record_rows(str(settle), f"specs/{OPEN_ITEM}") == [
            ("gaps.md", "how the gate renders in a TUI"),
            ("gaps.md", "whether Windows hooks fire"),
        ]
        assert GAPS.open_record_rows(str(settle), f"specs/{CLOSED_ITEM}") == []
        assert GAPS.open_record_rows(str(settle), "specs/1780000099-none") == []

    def test_refuses_to_read_a_section_it_cannot_read_as_nothing_open(self, tmp_path):
        """A count this cannot read is not a count of nothing."""
        memo_at(tmp_path, "## Not verified\n\n- the TUI rendering, as prose\n")
        rows = GAPS.open_record_rows(str(tmp_path), f"specs/{WORK}")
        assert len(rows) == 1 and rows[0][1].startswith("cannot be read (expected"), (
            rows
        )


test_census = census_case(TARGET)

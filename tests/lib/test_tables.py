"""`lib/tables.py`, the GFM table walker, one class per function its cases
reach.

#1454 moved the walker out of `lib/config.py`, which reads the settings as
JSON, and its cases came with it from `tests/lib/test_config.py`. Each
keeps its body, except that it calls the walker as `tables.<name>` and no
longer takes the `config` and `seal` fixtures it did not read. The cases over an earlier release's `| Item | Value |`
table stay as the walker's cases over the table `seal mode` converts, run
under `Test_gfm_table` through `_Old_config_table` and
`_Old_config_shapes`. `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py`
keeps the walker held to cmark-gfm.

#942's phase 6 and its round 9 fix pass had placed in `tests/lib/test_config.py`
three of the walker's cases from that file, the refusal of a line shown
directly above the header from the oracle file, whose corpus it imports
from there, and the case that copies the module without `lib/blocks.py`
from `tests/test_a_script_copied_alone_exits_2.py`, whose `routing.py` row
is in `tests/lib/test_routing.py`.
"""

import os
import subprocess
import sys

import pytest
from block_shapes import SHAPES
from conftest import (
    FENCED_ABOVE,
    FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN,
    FENCED_REFUSAL,
    PIPED_TABLE,
    ROOT,
    TABLE,
    UNDER_THE_COMMENT,
    census_case,
    crlf,
    load_lib_module,
    load_module,
    names_path,
    shape_text,
)
from test_one_table_walker_reads_what_gfm_renders import (
    HEADERS,
    INDENTS,
    KINDS,
    document,
)

TARGET = "lib/tables.py"

tables = load_lib_module("tables.py", "tables_under_test")
# The old table's header, `lib/config.py#OLD_TABLE`, which `seal mode`'s
# converter reads through the walker.
config = load_lib_module("config.py", "config_for_the_walker_cases")
# `seal mode`'s converter, which one case reads the walker's rows through.
seal = load_module(
    os.path.join(ROOT, "skills", "implement", "scripts", "seal.py"),
    "seal_for_the_walker_cases",
)

# `tests/block_shapes.py`'s config shapes the comment cases read (#667).
COMMENTED_OLD_ROW = shape_text("C5")
COMMENTED_OLD_TABLE = shape_text("C6")
QUOTED_DELIMITERS = shape_text("C1")
LIVE = [("Mode", "shared"), ("Broad gate", "bin/test -q")]

LANGUAGE_ROW = "Commit and pull request language"


def walk(text):
    """(rows, refusals) for TEXT's `| Item | Value |` table as
    `lib/tables.py#gfm_table` reads it: the table an earlier release's
    `config.md` holds, which `seal mode` converts. ROWS are `(item, value)`
    pairs in order, and REFUSALS the walker's sentences joined into one, its
    `holds no` sentence left out: a text with no such table converts to no
    key (`seal.py#converted`)."""
    rows, refusals = tables.gfm_table(text, config.OLD_TABLE)
    said = [line for line in refusals if not line.startswith("holds no ")]
    return [tuple(cells) for _line, cells in rows], " ".join(said)


def items(text):
    """The rows `walk` reads in TEXT, the name the row reader's cases spelt."""
    return walk(text)[0]


class _Old_config_table:
    """`gfm_table` over an earlier release's `config.md` table, which
    `seal mode` converts: what it reads is what the converter writes, and
    what it refuses the converter refuses to write (#1454). `Test_gfm_table`
    runs these cases."""

    def test_refuses_an_item_below_a_separator_out_of_place(self):
        """tests-todo row 9, from round 2 🟡 5, first shape — shape 8 of #871.
        cmark-gfm shows a stray separator as one of the table's rows, so the
        walker refuses it, naming it. The rows above it are read. Seen red
        against the stop rule, which ended the table there in silence."""
        text = (
            "| Item | Value |\n"
            "|---|---|\n"
            f"| {LANGUAGE_ROW} | Korean |\n"
            "|---|---|\n"
            "| Something else | x |\n"
        )
        rows, said = walk(text)
        assert rows == [(LANGUAGE_ROW, "Korean")]
        assert "stops at `|---|---|`, a delimiter row out of place" in said, said

    def test_a_repeated_header_is_read_as_a_row_and_the_doubled_item_is_refused(
        self,
    ):
        """tests-todo row 9, second shape — shape 9 of #871. A second
        `| Item | Value |` line under the table with no delimiter row of its own
        is one of this table's rows to cmark-gfm, so the walker reads it as one,
        and the row below it with it: the language is then written twice, which
        has no value, so the converter writes nothing. Seen red against the
        stop rule, which ended the table at the repeated header and read
        `Korean`."""
        text = (
            "| Item | Value |\n"
            "|---|---|\n"
            f"| {LANGUAGE_ROW} | Korean |\n"
            "| Item | Value |\n"
            f"| {LANGUAGE_ROW} | English |\n"
        )
        assert items(text) == [
            (LANGUAGE_ROW, "Korean"),
            ("Item", "Value"),
            (LANGUAGE_ROW, "English"),
        ]
        pairs, said = seal.converted(text)
        assert pairs is None and f"`{LANGUAGE_ROW}` row written more" in said, said

    def test_a_blank_line_above_the_first_row_ends_the_table_and_the_row_is_refused(
        self,
    ):
        """#871. A blank line under the delimiter row ends the table to
        cmark-gfm, so the row below it is not one of the table's rows: the
        walker refuses it as a row the walk never reaches. Seen red against the
        stop rule, which stepped past the blank line and read `Korean`."""
        text = f"| Item | Value |\n|---|---|\n\n| {LANGUAGE_ROW} | Korean |\n"
        rows, said = walk(text)
        assert rows == []
        assert "a row the walk never reaches" in said, said

    def test_accepts_an_item_value_table_and_no_other(self):
        """A parser that finds a row in anything is not a parser."""
        assert items("# a document with no table\n\nprose.\n") == []
        assert items("| Field | Value |\n|---|---|\n| a | b |\n") == [], (
            "an earlier release's `parity.md` header was `| Field | Value |`; "
            "matching it here would "
            "make this reader agree with a file it is not reading"
        )
        assert items("| Item | Value |\n|---|---|\n| a | b |\n") == [("a", "b")], (
            "the separator is being read as a row again"
        )

    def test_a_row_of_another_table_ends_this_one(self):
        """tests-todo row 3, from round 1 🟡 6.

        A three-cell row used to be skipped as though it were not there, so
        everything after it was absorbed. The interesting half is the LAST
        assertion: the danger was never the odd row itself, it was the ordinary
        row behind it arriving as though it belonged here.
        """
        text = (
            "| Item | Value |\n"
            "|---|---|\n"
            "| Commit and pull request language | Korean |\n"
            "| a | b | c |\n"
            "| Something else | x |\n"
        )
        assert items(text) == [("Commit and pull request language", "Korean")], (
            "a row of a different table did not end this one"
        )
        assert ("Something else", "x") not in items(text), (
            "the row behind the foreign one was read as part of this table"
        )

    def test_refuses_a_second_table_further_down_as_more_rows(self):
        """The same property at document scale, which is what `config.md`
        actually looks like: a table, prose, then another table."""
        text = (
            "| Item | Value |\n"
            "|---|---|\n"
            "| Commit and pull request language | Korean |\n"
            "\n"
            "## notes\n"
            "\n"
            "| Item | Value |\n"
            "|---|---|\n"
            "| Commit and pull request language | English |\n"
        )
        assert items(text) == [("Commit and pull request language", "Korean")], (
            "the first table's answer must win; a second one further down is "
            "prose about the first, not more rows of it"
        )

    def test_an_escaped_pipe_is_one_row_and_the_rows_below_it_still_arrive(self):
        """A1. `seal/config.md` is markdown and `\\|` is markdown's own answer for
        a pipe inside a cell (`questions.md` Q1, answered by the repository owner
        on 2026-09-17).

        **The count is asserted before the value, and that ordering is the
        case.** A case that checks the `Broad gate` value alone passes just as
        well when every row under it has vanished, and vanishing was the defect
        #415 was opened about: before the escape, the piped row took `Mode` and
        every later row with it, each falling back to a default with no message
        anywhere. Written bare it is now refused, naming the line (#871).
        """
        rows = items(PIPED_TABLE)
        assert len(rows) == 4, (
            f"the table has four rows and {len(rows)} came back: {rows}. A row "
            "the reader refuses ends the table, so what is missing here is every "
            "row written BELOW the piped one"
        )
        assert [item for item, _ in rows] == [
            "Record language",
            "Broad gate",
            "Mode",
            "Commit and pull request language",
        ], rows
        assert dict(rows)["Broad gate"] == "bin/test -q | tee out.txt", (
            "the value reaches its caller with one literal pipe, because the "
            "escape is markdown's and is undone before anything else sees it"
        )
        assert dict(rows)["Mode"] == "shared", (
            "the `Mode` row sits below the piped one, which is what `seal mode` "
            "reads before deciding whether to write one"
        )

    def test_a_windows_path_survives_the_reader_exactly_as_written(self):
        """The constraint the repository owner attached to Q1's answer, and it
        decides the implementation rather than the choice: the reduction is
        **exactly the two characters `\\|`**, never a general backslash unescape.

        `C:\\Python\\python.exe -m pytest` is the shape a `Broad gate` row takes
        on Windows, and it reads back with its separators intact today — the
        state this repository has already synced across operating systems. A
        blanket `re.sub(r"\\\\(.)", r"\\1", value)` would hand the gate
        `C:Pythonpython.exe -m pytest`, which is a path to nothing.
        """
        text = (
            "| Item | Value |\n|---|---|\n"
            "| Broad gate | C:\\Users\\x\\Python\\python.exe -m pytest |\n"
        )
        assert items(text) == [
            ("Broad gate", "C:\\Users\\x\\Python\\python.exe -m pytest")
        ], "a backslash that is not part of `\\|` is the value's own character"

    def test_a_backslash_against_a_pipe_is_the_one_shape_the_escape_narrows(self):
        """Round 1's 🟡 2 of #415. The escape is not free in one direction only:
        a backslash immediately before a cell-ending pipe used to be a plain
        character followed by a delimiter, and it is now one escaped pipe — so
        the line has one pipe fewer than it needs and stops being a row.

        **It is kept rather than repaired, and the narrowing is named rather
        than discovered.** Once `\\|` means an escaped pipe those bytes cannot
        also mean *backslash, then the delimiter*; the old reading was only
        available while a backslash meant nothing. Nothing becomes unwritable —
        a space before the closing pipe gives the value back byte for byte,
        because the walker strips the cell — and one line in the whole tree
        reads differently, in a review report quoting this shape.

        Both members of the class are here. The report named the first; the
        second is the same cause at an INTERNAL pipe, where the line stops being
        a row for the same reason.
        """
        header = "| Item | Value |\n|---|---|\n"
        tight_last = "| Broad gate | C:\\Users\\x\\tools\\|\n"
        tight_first = "| C:\\tools\\| x |\n"
        assert items(header + tight_last) == [], (
            "a backslash against the closing pipe is markdown's escaped pipe, so "
            "the line has no closing pipe left and is not a row. If this returns "
            "a row the pattern changed and `frame/design.md` *What this repair cannot "
            "see* is now wrong"
        )
        assert items(header + tight_first) == [], (
            "the same cause at the pipe BETWEEN the cells — the report named only "
            "the closing one"
        )
        assert items(header + "| Broad gate | C:\\Users\\x\\tools\\ |\n") == [
            ("Broad gate", "C:\\Users\\x\\tools\\")
        ], (
            "written with a space before the closing pipe the value comes back "
            "exactly as the old pattern read it, so no value lost a spelling"
        )
        assert items(header + "| C:\\tools\\ | x |\n") == [("C:\\tools\\", "x")], (
            "and the same for the item cell"
        )

    def test_a_three_column_row_is_refused_and_the_rows_above_it_arrive(self):
        """Shape 6 of #871. The escape widens what a cell may hold and must not
        widen what a ROW is: a greedy last cell would read `| a | b | c |` as the
        row `('a', 'b | c')`. Until #871 the line ended the table silently, and
        every row below it fell to its default; cmark-gfm shows those rows, so
        the walker refuses the line instead, naming it, and the rows above it
        are read. Seen red against the stop rule, which ended the table there
        in silence."""
        text = "| Item | Value |\n|---|---|\n| a | b |\n| x | y | z |\n| c | d |\n"
        rows, said = walk(text)
        assert rows == [("a", "b")]
        assert "stops at `| x | y | z |`, which is not a 2-cell row" in said, said

    def test_a_fenced_table_above_the_live_one_is_not_the_table(self):
        """A1. The live table is the first one outside every fence.

        A reader that starts at the first `| Item | Value |` header and never
        looks for another takes an example pasted above the live table as the
        table: the mode, the broad command, every row. The shape was invited
        rather than contrived, because the setup template's fenced example
        rows were copied whole into `config.md`.
        """
        assert items(FENCED_ABOVE) == [
            ("Mode", "shared"),
            ("Broad gate", "bin/test -q"),
        ], items(FENCED_ABOVE)

    def test_a_fenced_example_below_a_table_that_never_began_is_still_not_the_table(
        self,
    ):
        """A2. Both walks step past a line they cannot parse until a row is
        found, so with nothing parsed above it a fenced example's rows became the
        live rows — the same defect one shape over, and the one a repair aimed at
        the fenced HEADER alone would have left standing."""
        rows = items(FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN)
        assert rows == [], (
            f"the example inside the fence supplied this repository's rows:\n{rows}"
        )

    def test_what_counts_as_a_fence_is_commonmarks_rule_as_far_as_it_goes(self):
        """Q3 of `questions.md`, decided and pinned. `frame/design.md` *Data &
        interfaces* fixes the rule for the shapes that matter; the residue is
        CommonMark's own edge cases, resolved toward *not a fence* wherever the
        specification leaves room, because that is the direction that keeps a
        live table readable.

        Each assertion below is one decision:

          - four spaces of indentation is an indented code block, never a fence,
            so the table under it is still read;
          - a BACKTICK fence's info string may not hold a backtick (CommonMark
            4.5), so that line opens nothing;
          - a closing run may be longer than the one that opened the block;
          - a run of the OTHER character does not close a block, and neither
            does a run carrying an info string;
          - an unclosed fence runs to the end of the file, so the file
            holds no table.

        **A blank line stands above the live header in each fixture since
        #871**, because the walker refuses a header with a non-blank line
        directly above it whatever that line is (the migration's shape, rows 1,
        2 and 11 of the work item's measurement), and the decisions here are
        about which line opens or closes a fence, not about that one. The first
        assertion is that refusal, so the reason for the blank line is pinned
        beside it.
        """
        live = "| Item | Value |\n|---|---|\n| Mode | shared |\n"
        rows, said = walk("    ```\n" + live)
        assert rows == [] and "leave a blank line above the header" in said, said
        assert items("    ```\n\n" + live) == [("Mode", "shared")], (
            "four spaces is an indented code block and not a fence"
        )
        assert items("```` `x` ````\n\n" + live) == [("Mode", "shared")], (
            "a backtick fence's info string may not hold a backtick, so this "
            "line opens no fence"
        )
        assert items(
            "```\n| Item | Value |\n|---|---|\n| Mode | local |\n``````\n\n" + live
        ) == [("Mode", "shared")], (
            "a closing run longer than the opening one closes the block"
        )
        assert items(
            "```\n~~~\n| Item | Value |\n|---|---|\n| Mode | local |\n```\n\n" + live
        ) == [("Mode", "shared")], "a tilde run does not close a backtick fence"
        assert items(
            "````\n```\n| Item | Value |\n|---|---|\n| Mode | local |\n````\n\n" + live
        ) == [("Mode", "shared")], (
            "a run SHORTER than the opening one does not close the block — this "
            "repository's own records wrap a fenced example in four backticks, "
            "and a rule that knew three only would read the inner fence as the "
            "outer one's close and leave the live table inside a fence"
        )
        assert items("```\n```markdown\n" + live) == [], (
            "a run carrying an info string does not close a block, so this file "
            "declares nothing"
        )
        assert items("~~~\n" + live) == [], (
            "an unclosed fence runs to the end of the file"
        )
        assert items("~~~info ~ string\n" + live + "~~~~\n") == [], (
            "a tilde fence's info string is unrestricted, which is CommonMark's "
            "rule and not an exception to this one"
        )

    def test_delimiters_quoted_in_code_spans_hide_nothing(self):
        """C1, named as 1790635413 named it (round 1, 🟡 3). A prose line quoting
        the opener in a code span above the table and one quoting the closer
        below it are paragraph text, so the table between them is read. Pins:
        the base read it, and the three rounds lost it by reading inline state."""
        assert items(QUOTED_DELIMITERS) == LIVE

    @pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
    def test_a_break_commonmark_does_not_honour_hides_no_config_row(self, name):
        """#667 round 1, 🟡 1: the routing reader's shape in `config.md`. A
        `<!--` after a character `str.splitlines` breaks at and CommonMark does
        not is mid-line to a renderer, so it hides no line, and the base read
        `Mode shared`.

        **Re-pinned by #871 to the walker's answer, which is a refusal.** The
        `-->` under the row is a row GFM shows, so the table is one the walk
        cannot read whole, and the walk reads the pieces `str.splitlines` cuts,
        where `<!--` begins one: it refuses at the header, naming an HTML block
        GFM does not see. The direction is the refusing one and no row is read
        that GFM does not show; the sentence's cause is the walker's limit on
        these eight characters, named in the work item's `gaps.md`."""
        from block_shapes import BREAKS, OPEN

        text = (
            f"A note{BREAKS[name]}{OPEN}\n\n| Item | Value |\n|---|---|\n"
            "| Mode | shared |\n-->\n"
        )
        lines = text.splitlines()
        assert [i for i, _line in tables.unfenced(lines, text)] == list(
            range(len(lines))
        )
        rows, said = walk(text)
        assert rows == [] and said, said

    @pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
    def test_a_piece_inside_an_inline_comment_is_no_config_row(self, name):
        """#667 round 2, 🟡 1. A table written after a break inside an inline
        comment its line opened is inside that comment to a renderer, and the
        fence run before it is fenced to the base. Read by the line it starts in,
        the piece took the line's answer, shown, and a `Mode` row neither
        reading shows was read."""
        from block_shapes import BREAKS, OPEN

        brk = BREAKS[name]
        text = (
            f"x {OPEN} a{brk}```{brk}| Item | Value |{brk}|---|---|{brk}"
            "| Mode | shared |\n-->\n"
        )
        assert items(text) == []

    @pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
    @pytest.mark.parametrize(
        "opener, closer",
        [
            ("<![CDATA[ a", "]]>"),
            ("<? a", "?>"),
            ("<!DOCTYPE a", "a>"),
            ('<span title="a', '">'),
            ("<span title='a", "'>"),
        ],
        ids=["cdata", "instruction", "declaration", "double-quoted", "single-quoted"],
    )
    def test_a_piece_inside_other_inline_html_is_no_config_row(
        self, name, opener, closer
    ):
        """#673, #667 round 3's 🟡 1. A comment is one kind of inline raw HTML of
        six (CommonMark 6.6); CDATA, a processing instruction, a declaration and a
        tag's quoted attribute value hide what they hold too, and the fence run
        before the table is fenced to the base. The walk looked only for a
        comment opener, so the piece was claimed shown and a `Mode` row neither
        reading shows was read. A declaration's closer is written `a>`: a `>` at
        a line's start would open a block quote instead."""
        from block_shapes import BREAKS

        brk = BREAKS[name]
        text = (
            f"x {opener}{brk}```{brk}| Item | Value |{brk}|---|---|{brk}"
            f"| Mode | shared |\n{closer}\n"
        )
        assert items(text) == []

    @pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
    def test_a_row_after_a_break_gfm_does_not_honour_is_no_row_of_its_own(self, name):
        """#871 round 1, 🟡 4. A row followed on its own line by a character only
        `str.splitlines` ends a line at, then a second row, is ONE row to
        cmark-gfm, cut off at its cells: GitHub shows `Mode shared` and no
        `Broad gate`. The walk reads the first row and refuses the piece after
        the break, so no gate is handed a command GitHub does not show. Seen red
        against the walk before the guard: `Broad gate` was read as `x`."""
        from block_shapes import BREAKS

        text = TABLE.format(rows=f"| Mode | shared |{BREAKS[name]}| Broad gate | x |\n")
        rows, said = walk(text)
        assert rows == [("Mode", "shared")], rows
        assert "put it on a line of its own" in said, said

    @pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
    @pytest.mark.parametrize("where", ["above the header", "under the header"])
    def test_a_header_after_a_break_gfm_does_not_honour_is_no_table(self, name, where):
        """#871 round 2, yellow 7. A header after a character only
        `str.splitlines` ends a line at, or a delimiter row after one on the
        header's line, is no table to cmark-gfm (measured for FF, U+2028, NEL
        and VT by the round's reviewer). The walk reads no row and refuses."""
        from block_shapes import BREAKS

        brk = BREAKS[name]
        text = (
            f"# c\n\n{brk}| Item | Value |\n|---|---|\n| Mode | shared |\n"
            if where == "above the header"
            else f"# c\n\n| Item | Value |{brk}|---|---|\n| Mode | shared |\n"
        )
        rows, said = walk(text)
        assert rows == [] and "each on a line of its own" in said, (rows, said)


class _Old_config_shapes:
    """`gfm_table` over the config shapes of #667 and #871, each an earlier
    release's `config.md`. `Test_gfm_table` runs these cases."""

    def test_refuses_a_fenced_pipe_line_as_a_line_somebody_wrote(self):
        """A3. The walk that read ON past the stopping line treated any line
        beginning with a pipe as a line somebody wrote as a row — so a line
        inside an example block came back as refused, and `seal gate` quotes a
        refused line back at the person as their own.

        Re-pinned by #871: the fence directly under the delimiter row ends the
        table, as GFM ends it, so the live `Mode` row below the fence is not one
        of the table's rows and the walk refuses it -- naming THAT line, never
        the fenced one.
        """
        rows, refusals = tables.gfm_table(FENCED_REFUSAL, config.OLD_TABLE)
        assert rows == [], rows
        assert len(refusals) == 1, refusals
        assert "tee out.txt" not in refusals[0], (
            f"a line inside a code fence came back as a refused row:\n{refusals}"
        )
        assert "ends above `| Mode | shared |`" in refusals[0], refusals

    @pytest.mark.parametrize(
        "name, rows, stops",
        [
            # pins: delimiters quoted in code spans either side of the table hide
            # nothing (1790635413 round 1, 🟡 3)
            ("C1", LIVE, None),
            # red at base: a closed comment above the table quoting a fence line
            # opened a fence that ran to the end and hid the live table
            ("C2", [("Mode", "shared")], None),
            # pins: a mid-line opener nobody closed switches off no fence below it
            # (1790635413 round 3, 🟡 1)
            ("C3", [("Mode", "shared"), ("Broad gate", "bin/test")], None),
            # pins: nor does one that an example's closer below seems to close
            # (1790635413 round 3, ⬜ 3)
            ("C4", LIVE, None),
            # #871: a row parked in a comment inside the table ends the table
            # there, as GFM ends it, so the live rows under the comment are
            # refused rather than read; the same in CRLF. A whole old table
            # parked above the live one still leaves the live one read.
            ("C5", [], UNDER_THE_COMMENT),
            ("C6", LIVE, None),
            ("C7", [], UNDER_THE_COMMENT),
            # red at base: a malformed pipe-line inside a comment is not the
            # person's refused row -- the walk names the live row under it
            ("C8", [], UNDER_THE_COMMENT),
            # #871: a `<!--` nobody closed still hides nothing from the fence
            # rule, but GFM renders no table under or after it, so the walk
            # refuses where the stop rule read
            ("C9a", [], "inside an HTML block opened above it and never closed"),
            ("C9b", [], UNDER_THE_COMMENT),
            # pins: #429's fenced example above the live table
            ("C12", [("Mode", "shared")], None),
            # pins: a fence nobody closed still hides everything below it, so the
            # file holds no table and declares nothing
            ("C14", [], None),
        ],
        ids=lambda value: value if isinstance(value, str) and value[:1] == "C" else "",
    )
    def test_accepts_every_config_shape_as_the_frame_expects(self, name, rows, stops):
        """S5 of #667, re-pinned to the walker by #871. Every config shape the
        frame names, through the walker. A row inside a comment that closes
        is not an answer somebody gave, and a fenced line is no row either.
        Where GFM ends the table at a comment or shows no table at all, the
        walk refuses, naming the live row it did not read -- never the parked
        one -- rather than reading on below it as the stop rule did."""
        text = shape_text(name)
        found, refusals = walk(text)
        assert found == rows, found
        if stops is None:
            assert refusals == "", refusals
        else:
            assert stops in refusals, refusals
            assert "old -q" not in refusals, refusals


class Test_fence_map:
    def test_refuses_to_name_a_fence_inside_a_closed_comment(self):
        """S8, C2. The comment closes, so the fence line inside it opens
        nothing, and `fence_map`'s second value names no fence nobody left
        open. Red at base: the fence ran to the end and was named."""
        lines = SHAPES["C2"]
        assert tables.fence_map(lines)[1] is None

    def test_accepts_a_fence_nobody_closed_as_the_one_named(self):
        """C14, pinned from the other side: the fence that hides the live table
        is the one `fence_map` reports."""
        assert tables.fence_map(SHAPES["C14"])[1] == 0

    def test_the_fence_named_is_the_one_that_hides_the_row(self):
        """C2 with a fence left open below the table. The old reading runs the
        fence quoted in the comment to the end, so it would name THAT line, which
        opens nothing; the walk sees the tilde fence below the table never close,
        and the line under it is hidden because of it."""
        lines = [*SHAPES["C2"], "", "~~~", "| Broad gate | bin/test -q |"]
        assert tables.fence_map(lines)[1] == lines.index("~~~")
        assert items("\n".join(lines)) == [("Mode", "shared")]


class Test_hidden_lines:
    def test_accepts_a_fence_that_closes_as_hidden_and_names_no_opener(self):
        assert tables.hidden_lines(["```", "| Mode | x |", "```", "after"]) == (
            {0: "fence", 1: "fence", 2: "fence"},
            None,
        )

    def test_refuses_to_name_a_later_fence_left_open_before_the_first(self):
        """Two fences that never close: the first is the one that hides the
        lines under it, so it is the one named."""
        lines = ["```", "a", "~~~", "b"]
        assert tables.hidden_lines(lines)[1] == 0


class Test_unfenced:
    def test_refuses_a_commented_row_in_either_line_ending(self):
        """S5, C5 to C7, named as 1790635413 named them. The rows parked in a
        comment are gone from every walk. Since #871 the live rows under a
        comment that sits inside the table do not arrive either: GFM ends the
        table at the comment, so the walk refuses them, naming the first. Under
        a whole old table parked above the live one, the live table arrives."""
        for text in (COMMENTED_OLD_ROW, COMMENTED_OLD_TABLE, crlf(COMMENTED_OLD_ROW)):
            assert all(
                "old -q" not in line
                for _index, line in tables.unfenced(text.splitlines())
            ), text
        assert items(COMMENTED_OLD_TABLE) == LIVE
        for text in (COMMENTED_OLD_ROW, crlf(COMMENTED_OLD_ROW)):
            rows, said = walk(text)
            assert rows == [] and UNDER_THE_COMMENT in said, (text, said)

    def test_accepts_every_line_under_a_mid_line_comment(self):
        """C13, the residual `frame/design.md` *Scope* names. A renderer hides the first
        pipe-line behind a lone backtick and a mid-line `<!--`, and knowing that
        needs code spans and the paragraph's extent, which is where all three of
        1790635413's rounds lost ground. The base reads it, so reading it is not
        worse; this pins that nothing here pretends to more."""
        lines = SHAPES["C13"]
        assert [index for index, _line in tables.unfenced(lines)] == list(
            range(len(lines))
        )


class Test_gfm_table(_Old_config_table, _Old_config_shapes):
    @pytest.mark.parametrize(
        "above",
        ["text\n```\nx\n```\n", "text\n" + "<" + "!-- c -->\n"],
        ids=[
            "a closed fence directly above, under a paragraph",
            "a closed comment directly above, under a paragraph",
        ],
    )
    def test_refuses_a_hidden_line_directly_above_the_header(self, above):
        """**The trade** (round 2, yellow 15). cmark-gfm renders both of these
        tables, and until round 2 the walker read them, because `unfenced` hides
        the closing fence or comment and the walk saw a gap above the header.
        The walker now judges the line above as written, hidden or not, because
        the same hidden line is what hid a header cmark-gfm does not render: a
        fence inside a kind 6-7 HTML block, or a list item a fence-only reading
        hid. So these are refused with the blank-line remedy, as a paragraph
        directly above already is (round 1, yellow 5). Every template and the
        writer leave the blank line."""
        text = f"# Pact\n\n{above}| Signer |\n|---|\n| https://example.com/org/a |\n"
        _rows, refusals = tables.gfm_table(text, ("Signer",))
        # The refusal the walker returns, whose remedy the person editing the
        # file follows.
        assert refusals and "blank line above the header" in refusals[0], refusals

    @pytest.mark.parametrize("name", ["LS", "FF"])
    def test_accepts_the_rows_above_a_heading_piece_and_refuses_the_row_below(
        self, name
    ):
        """#871 round 2, yellow 7's class after the table's end. A heading piece
        after a character only `str.splitlines` ends a line at is more of the
        line above to GFM, not a heading, so a line written `| … |` under it is
        still a row nobody reads, and is refused."""
        from block_shapes import BREAKS

        text = (
            "| Item | Value |\n|---|---|\n| Mode | shared |\n\n"
            f"x{BREAKS[name]}## Notes\n| Broad gate | y |\n"
        )
        rows, refusals = tables.gfm_table(text, ("Item", "Value"))
        assert [c for _l, c in rows] == [("Mode", "shared")], rows
        assert refusals and "ends above `| Broad gate | y |`" in refusals[0], refusals

    @pytest.mark.parametrize("which", sorted(HEADERS))
    def test_a_line_directly_above_the_header_is_refused(self, which):
        """Whether cmark-gfm renders a table under a line depends on the block
        state above it, which the walker does not track, so a non-blank line the
        walk is shown directly above a header is refused with the blank-line
        remedy (round 1, yellow 5). This reverses the build's first choice,
        which mirrored cmark-gfm's interruption rules line by line and was found
        reading tables cmark-gfm does not render in shapes the corpus did not
        reach. A kind whose last line `unfenced` hides, or a blank line, leaves
        a gap or a blank above the header and is not this rule's."""
        header = HEADERS[which]
        for kind, lines in KINDS.items():
            for indent in INDENTS:
                text = document(header, lines, "before the header", indent)
                split = text.splitlines()
                head = split.index("| " + " | ".join(header) + " |")
                shown = dict(tables.unfenced(split, text))
                above = shown.get(head - 1)
                if above is None or not above.strip():
                    continue
                _rows, refusals = tables.gfm_table(text, header)
                # The refusal the walker returns, whose remedy the person
                # editing the file follows.
                assert refusals and "blank line above the header" in refusals[0], (
                    kind,
                    indent,
                    refusals,
                )


class Test_module:
    def test_a_reader_copied_without_the_walk_names_it(self, tmp_path):
        """#667. This module imports `lib/blocks.py`, the walk the readers under
        `lib/` share. It is a module, not a script: scripts import it, and a
        script catches the error or names the file first. So a copy without the walk raises one `ImportError` whose
        sentence names the path and what the file is for.
        `tests/lib/test_routing.py` holds `lib/routing.py` to the same."""
        name, siblings = TARGET.rsplit("/", 1)[1], []
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
        assert names_path(os.path.join(str(alone), "blocks.py"), last), last
        assert "tells a live row from one quoted in a fence or parked in a comment" in (
            last
        ), last


test_census = census_case(TARGET)

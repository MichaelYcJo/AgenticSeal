"""`lib/lines.py`, one class per function.

The readers of a markdown text by line: a table row's cells, what a cell
shows, the lines a fence holds, the record line that opens a comment,
whether a line begins live, and which ATX heading a line is. They run in
the process on lines and texts, with no git. Their cases came, unchanged
but for the module they call, from `tests/skills/test_unverified_check.py`
when the readers left that script (#1482).

`Test_heading_level` holds the heading rule to markdown-it's ATX headings
through `tests/commonmark_oracle.py`, over the frame's shapes and a
generated corpus; `disagreements` is the comparison, which
`tests/behaviour/test_one_heading_rule_holds_to_commonmark.py` imports for
its corpus of tracked files. `Test_live_lines` holds `live_lines` to a
reading written from the format, `a_reading_from_the_commonmark_rules`, at
the foot of this file.
"""

import os
import random
import re

import pytest
from commonmark_oracle import heading_lines, hidden_text
from conftest import ROOT, census_case, load_lib_module

TARGET = "lib/lines.py"

READER = load_lib_module("lines.py", "lines_for_its_own_file")
# `lib/gaps.py`, whose `HEADING` is the section `Test_sections` asks for.
GAPS = load_lib_module("gaps.py", "gaps_for_the_lines_cases")

# Spelt by code point, so no invisible character stands in this file.
ZERO_WIDTH_SPACE = chr(0x200B)
EMOJI_SELECTOR = chr(0xFE0F)


class Test_split_row:
    @pytest.mark.parametrize(
        "line, cells",
        [
            ("| a | b |", ["a", "b"]),
            ("  | a | b", ["a", "b"]),
            (
                "| whether `a \\| b` parses | the next session |",
                ["whether `a | b` parses", "the next session"],
            ),
            ("| a \\|", ["a |"]),
        ],
        ids=["closed", "open at the end", "an escaped pipe", "an escaped last pipe"],
    )
    def test_accepts_a_row_and_its_escaped_pipes(self, line, cells):
        assert READER.split_row(line) == cells

    def test_refuses_a_line_that_is_no_row(self):
        assert READER.split_row("- the TUI rendering, nobody has seen it") is None


class Test_is_separator:
    def test_accepts_dashes_and_alignment_colons(self):
        assert READER.is_separator(["---", ":-:", "-:"]) is True

    @pytest.mark.parametrize("cells", [[], ["---", "a"]], ids=["no cells", "a word"])
    def test_refuses_no_cells_and_a_cell_with_a_word(self, cells):
        assert READER.is_separator(cells) is False


class Test_visible:
    def test_accepts_a_cell_without_what_takes_no_width(self):
        assert READER.visible(f" closed{ZERO_WIDTH_SPACE}{EMOJI_SELECTOR} ") == "closed"

    def test_refuses_to_take_out_what_a_reader_sees(self):
        assert READER.visible(" a  b ") == "a  b"


class Test_fence_spans:
    def test_accepts_each_closed_block_with_its_delimiters(self):
        lines = ["a", "```", "x", "```", "~~~", "y", "~~~"]
        assert READER.fence_spans(lines) == [(1, 3), (4, 6)]
        # A block with nothing in it closes on the line after its opener.
        assert READER.fence_spans(["```", "```", "x"]) == [(0, 1)]

    def test_refuses_to_close_a_block_nobody_closed(self):
        assert READER.fence_spans(["a", "```", "x"]) == [(1, None)]


class Test_closed_fence_lines:
    def test_accepts_the_lines_of_a_block_that_closes(self):
        assert READER.closed_fence_lines(["a", "```", "x", "```", "b"]) == {1, 2, 3}

    def test_refuses_the_lines_of_a_block_that_never_closes(self):
        assert READER.closed_fence_lines(["a", "```", "x", "```", "b", "```", "c"]) == {
            1,
            2,
            3,
        }


class Test_blank_fences:
    def test_accepts_a_closed_block_blanked_and_the_lines_kept(self):
        assert READER.blank_fences(["a", "```", "x", "```", "b"]) == [
            "a",
            "",
            "",
            "",
            "b",
        ]

    def test_refuses_to_read_past_a_block_nobody_closed(self):
        assert READER.blank_fences(["a", "```", "x", "b"]) == ["a", "", "", ""]


class Test_comment_lines:
    def test_accepts_each_line_that_begins_with_the_opener(self):
        """*Scope* item 3 of #1012: a record carries no HTML comment, so a
        line whose text, leading whitespace removed, begins with `<!--` is
        found at its own index, for the reader of the record to refuse."""
        lines = READER.readable("# r\n\n<!-- a note -->\n  <!-- indented\nprose\n")
        assert READER.comment_lines(lines) == [2, 3]

    def test_refuses_an_opener_later_in_a_line_or_inside_a_fence(self):
        """A `<!--` after the start of a line is text, in a code span or not,
        and one inside a fence is part of a quotation `readable` blanks."""
        text = "a `<!--` b\nprose <!-- open\n```\n<!-- quoted\n```\n"
        assert READER.comment_lines(READER.readable(text)) == []


class Test_liveness:
    SPAN = ("a span opens `here", "<!-- specs/s-6 -->", "and closes` there")

    @pytest.mark.parametrize(
        "lines, live",
        [
            (SPAN, [True, True, True]),
            (["x `<!--` y", "after"], [True, True]),
            (["x <!-- `y`", "after"], [True, False]),
            (
                ["<!-- open", "```", "-->", "<!-- specs/x -->"],
                [True, False, False, True],
            ),
        ],
        ids=[
            "a run alone is literal",
            "a span first",
            "an opener first",
            "no fence in a comment",
        ],
    )
    def test_accepts_the_literal_reading(self, lines, live):
        assert READER.liveness(lines, spans_cross_lines=False) == live

    def test_refuses_lines_a_span_reaching_across_them_parks(self):
        assert READER.liveness(self.SPAN, spans_cross_lines=True) == [
            True,
            False,
            False,
        ]

    def test_reads_an_opener_as_text_where_the_caller_keeps_no_comment_state(self):
        """#1012: `rule_changes.py#parse` reads a record with `comments=False`,
        so an opener opens nothing and a fence after it is a fence."""
        lines = ["<!-- open", "```", "-->", "```", "after"]
        assert READER.liveness(lines, spans_cross_lines=False, comments=False) == [
            True,
            True,
            False,
            False,
            True,
        ]


class Test_live_pieces:
    """#1185. The offsets of each line's live text, from `_scan`, the walk
    `liveness` reads: a fence's lines hold no piece, a lone backtick run
    stays inside its piece, and a span's backticks and a comment's
    delimiters stand in none."""

    def test_accepts_the_text_around_a_span_and_a_comment_as_pieces(self):
        lines = ["a `x` b <!-- c --> d", "```", "@a.md", "```", "lone ` run"]
        assert READER.live_pieces(lines, spans_cross_lines=True) == [
            [(0, 2), (5, 8), (18, 20)],
            [],
            [],
            [],
            [(0, 10)],
        ]

    def test_refuses_the_text_a_span_or_a_comment_reaches_across_lines(self):
        span = ["Run `cat @a.md", "@a.md` then @b.md"]
        assert READER.live_pieces(span, spans_cross_lines=True) == [[(0, 4)], [(6, 17)]]
        comment = ["x <!-- open", "@a.md"]
        assert READER.live_pieces(comment, spans_cross_lines=True) == [[(0, 2)], []]


# The heading rule held to `tests/commonmark_oracle.py`, which reads
# markdown-it and nothing of this repository's (#867): on every line a
# renderer shows, `heading_level` answers what the parser's top-level ATX
# headings answer. A heading indented one to three spaces under a list item
# is that item's content, and a rule that reads one line cannot see the item
# above it, so the comparison skips such a line and counts it.
LIST_ITEM = ("- ", "* ", "+ ", "1. ", "1) ")


def disagreements(lines):
    """`([(index, ours, theirs)], skipped)` over the lines of a document a
    renderer shows, skipping a line indented one to three spaces below a
    list item (the module's stated limit). The file on the one heading rule
    imports it for its corpus of tracked files."""
    text = "\n".join(lines)
    hidden = hidden_text(text)
    theirs = heading_lines(text)
    out, skipped, under_a_list = [], 0, False
    for index, line in enumerate(lines):
        if line.lstrip(" ").startswith(LIST_ITEM):
            under_a_list = True
        if index in hidden:
            continue
        ours = READER.heading_level(line)
        if ours != theirs.get(index):
            if (
                under_a_list
                and line[:1] == " "
                and len(line) - len(line.lstrip(" ")) <= 3
            ):
                skipped += 1
                continue
            out.append((index, ours, theirs.get(index)))
    return out, skipped


SHAPES = {
    "a heading": (["## B"], 2),
    "indented three spaces": (["   ## B"], 2),
    "indented four spaces": (["    ## B"], None),
    "a tab before the run": (["\t## B"], None),
    "an issue number at column 0": (["#84's line"], None),
    "a wrapped issue reference": (["text", "#120) was it"], None),
    "seven hashes": (["####### x"], None),
    "a run and a tab": (["#\tx"], 1),
    "a run alone": (["#"], 1),
    "a closing run": (["## B ##"], 2),
    "no space after the run": (["#hello"], None),
    "a heading in a block quote": (["> # q"], None),
    "a heading in a list item": (["- # item"], None),
    "a heading after a paragraph": (["text", "## B"], 2),
}


SEED = 867


CORPUS_SIZE = 2000


ALPHABET = [
    "",
    "## B",
    "   ## B",
    "  ## B",
    " # x",
    "    ## B",
    "#120) x",
    "#84's",
    "####### x",
    "#",
    "#\tx",
    "\t# x",
    "## B ##",
    "x",
    "```",
    "~~~",
    "> # q",
    "- # item",
    "- item",
    "1. x",
    "<div>",
    "</div>",
    "---",
    "===",
    "* * *",
    "    code",
    "<!--",
    "-->",
    "| a | b |",
    "|---|---|",
]


class Test_heading_level:
    @pytest.mark.parametrize(
        "line, level",
        [("## Not verified", 2), ("   ## Not verified", 2), ("#\tx", 1), ("#", 1)],
    )
    def test_accepts_commonmarks_atx_heading(self, line, level):
        """CommonMark 4.2: at most three spaces, one to six `#`, then a
        space, a tab or the end (#867)."""
        assert READER.heading_level(line) == level

    @pytest.mark.parametrize(
        "line",
        ["    ## Not verified", "\t## Not verified", "#120) wrapped", "####### seven"],
    )
    def test_refuses_four_spaces_a_tab_an_issue_number_and_seven_hashes(self, line):
        assert READER.heading_level(line) is None

    @pytest.mark.parametrize("name", sorted(SHAPES))
    def test_the_frames_shapes(self, name):
        """S8's and S9's shapes: the rule's answer for the shape's last line, and
        markdown-it's, agree, and both are the level written beside it."""
        lines, level = SHAPES[name]
        assert READER.heading_level(lines[-1]) == level
        assert disagreements(lines) == ([], 0), name

    def test_a_seeded_generated_corpus(self):
        """S10, the generated half: CORPUS_SIZE documents of one to twelve lines
        drawn from ALPHABET, the same ones on every run (SEED), so a red is
        reproducible. Measured while building it: 3,000 documents found
        disagreements only on the stated limit."""
        rng = random.Random(SEED)
        found, skipped = [], 0
        for _ in range(CORPUS_SIZE):
            lines = [rng.choice(ALPHABET) for _ in range(rng.randint(1, 12))]
            wrong, limit = disagreements(lines)
            skipped += limit
            found.extend((lines, w) for w in wrong)
        assert not found, found[:5]
        assert skipped, "the corpus no longer reaches the stated limit"


class Test__paragraph_ends_at:
    @pytest.mark.parametrize(
        "line",
        [
            "",
            "| a |",
            "> q",
            "   # a heading",
            "```",
            "***",
            "- item",
            "===",
            "1. item",
        ],
    )
    def test_accepts_each_line_the_format_ends_a_paragraph_at(self, line):
        assert READER._paragraph_ends_at(line) is True

    @pytest.mark.parametrize(
        "line",
        [
            "text",
            "#hello",
            "####### seven",
            "    # four spaces is paragraph text",
            "3. item",
        ],
    )
    def test_refuses_paragraph_text(self, line):
        """#491's round-7 comment: four spaces before a heading is a lazy
        continuation line, and an ordered list interrupts a paragraph only
        when it starts with 1."""
        assert READER._paragraph_ends_at(line) is False


class Test__partner_ahead:
    def test_accepts_a_run_of_its_width_inside_the_paragraph(self):
        assert READER._partner_ahead(["text", "a ` b"], 0, 1) is True

    @pytest.mark.parametrize(
        "lines", [["", "a ` b"], ["a `` b"]], ids=["past a blank line", "another width"]
    )
    def test_refuses_a_run_past_the_paragraph_or_of_another_width(self, lines):
        assert READER._partner_ahead(lines, 0, 1) is False


MARKER = r"^<!-- specs/(\S+) -->$"


def live_markers(body):
    """The marker ids on the live lines of BODY, each read line-anchored, on
    a line of its own."""

    return {
        found
        for line, live in READER.live_lines(READER.gfm_lines(body))
        if live
        for found in re.findall(MARKER, line)
    }


class Test_live_lines:
    @pytest.mark.parametrize(
        "body, found",
        [
            ("<!-- specs/x-1 -->\n", {"x-1"}),
            ("```\nx\n```\n<!-- specs/x-6 -->\n", {"x-6"}),
            ("<!-- parked\n-->\n<!-- specs/c-3 -->\n", {"c-3"}),
            ("<!-- a note --> and prose\n<!-- specs/c-5 -->\n", {"c-5"}),
            # An opener quoted inside a code span is prose, not a draft
            # (round 3, finding 2).
            ("see `<!--` here\n<!-- specs/c-7 -->\n", {"c-7"}),
            # Round 1. Inside a draft nothing is markdown, so the quoted
            # closing delimiter really ends it and the marker below is live.
            (
                "<!-- a draft, parked\nprose with `-->` in it\n<!-- specs/s-1 -->\n-->\n",
                {"s-1"},
            ),
            # Round 2. A span quoting a whole comment keeps its closer.
            (
                "<!-- a draft, parked\nends with `<!-- a note -->` whole\n<!-- specs/s-2 -->\n-->\n",
                {"s-2"},
            ),
            # The control, without which every refusal is satisfied by a
            # reader that parks the whole document.
            ("# a policy\n\n<!-- specs/s-7 -->\nThe standing statement.\n", {"s-7"}),
        ],
        ids=[
            "a marker",
            "after a closed fence",
            "after a closed draft",
            "after a comment on one line",
            "after an opener in a span",
            "a closer quoted alone inside a draft",
            "a whole comment quoted inside a draft",
            "a genuine marker",
        ],
    )
    def test_accepts_a_marker_on_a_line_that_begins_live(self, body, found):
        assert live_markers(body) == found

    @pytest.mark.parametrize(
        "body",
        [
            "```markdown\n<!-- specs/x-2 -->\n```\n",
            "~~~\n<!-- specs/x-3 -->\n~~~\n",
            # A ``` inside a ```` block does not close it (CommonMark).
            "````\n```markdown\n<!-- specs/x-4 -->\n```\n````\n",
            "```\n<!-- specs/x-5 -->\n",
            "see `<!-- specs/x-7 -->` here\n",
            "<!-- parked\n<!-- specs/c-2 -->\n-->\n",
            "<!-- parked\n<!-- specs/c-4 -->\n",
            "<!-- parked\n```\n<!-- specs/c-6 -->\n```\n-->\n",
            # Round 3. A closer and then an opener inside one span: the draft
            # ends and re-opens, so the marker begins inside it.
            "<!-- a draft, parked\nquotes `--> and then <!--` here\n<!-- specs/s-3 -->\n-->\n",
            # Round 4. The same pair in two spans on one line.
            "<!-- a draft, parked\n`-->` and then `<!--` more\n<!-- specs/s-4 -->\n-->\n",
            # Round 5. An unclosed run, a draft opener on the next line, the
            # partner after it: the two readings disagree, so the line parks.
            "prose with an unclosed `run\n<!-- a draft, parked\nclosing ` here\n<!-- specs/s-5 -->\n-->\n",
            # A marker between the two halves of a code span.
            "a span opens `here\n<!-- specs/s-6 -->\nand closes` there\n",
            # Round 6. A delimiter indented four spaces is no delimiter, so it
            # does not invert the fence state of the example below.
            "A fence opens with\n\n    ```python\n\nand closes with a run "
            "at least as long.\n\n```markdown\n<!-- specs/s-8 -->\n```\n",
        ],
        ids=[
            "in a fence",
            "in a tilde fence",
            "in a longer fence",
            "in a fence nobody closed",
            "in a code span",
            "in a draft",
            "in a draft nobody closed",
            "in a fence in a draft",
            "a closer then an opener in one span",
            "a closer and an opener in two spans",
            "a span reaching past a draft opener",
            "inside a multi-line code span",
            "under an indented delimiter",
        ],
    )
    def test_refuses_a_marker_on_a_line_that_begins_parked(self, body):
        assert live_markers(body) == set()

    @pytest.mark.parametrize(
        "line, opens",
        [
            ("a `<!--` c", False),
            ("``a ` <!--`` c", False),
            ("`a` <!-- b", True),
            ("`open <!--", True),
            ("no span <!--", True),
            ("no span at all", False),
        ],
    )
    def test_a_code_span_closes_at_a_backtick_string_of_equal_length(self, line, opens):
        """CommonMark 6.1's span rule: equal-length backtick strings, an
        unmatched one left literal, observed as whether the line leaves a
        comment open."""
        answer = [live for _, live in READER.live_lines([line, "<!-- specs/x-1 -->"])]
        assert answer[0] is True
        assert answer[1] is not opens

    def test_reads_an_opener_as_text_where_the_caller_keeps_no_comment_state(self):
        """#1012: both readings take the keyword, so a heading after an
        opener nobody closed begins live for `rule_changes.py#parse`."""
        lines = ["prose <!-- open", "## Rule changes"]
        assert [live for _, live in READER.live_lines(lines, comments=False)] == [
            True,
            True,
        ]
        assert [live for _, live in READER.live_lines(lines)] == [True, False]

    def test_the_scan_decides_a_fence_before_a_comment_or_a_span(self):
        """A fence opener owns its whole line, so a comment opener on it is
        fenced content and opens nothing."""
        lines = ["```markdown <!--", "<!-- specs/x-1 -->", "```", "<!-- specs/x-2 -->"]
        assert [live for _, live in READER.live_lines(lines)] == [
            True,
            False,
            False,
            True,
        ]

    def test_the_scan_never_reads_live_what_the_format_parks(self):
        """The safety direction, against a reading written from the format.
        `live_lines` parks a line wherever its two readings differ, so it
        parks lines the format calls live on purpose; what may never happen
        is the scan calling a line live that the format parks."""
        unsafe, live_seen = [], 0
        for lines in documents_with_several_spans_on_a_line(2000):
            scan = [live for _, live in READER.live_lines(lines)]
            truth = a_reading_from_the_commonmark_rules(lines)
            live_seen += sum(1 for v in scan if v)
            for n in range(len(lines)):
                if scan[n] and not truth[n]:
                    unsafe.append((lines, n, scan, truth))
        assert not unsafe, (
            f"{len(unsafe)} line(s) read live where the format parks; first: {unsafe[0]}"
        )
        # Not vacuous: a reader that parked everything would satisfy the above.
        assert live_seen > 2000, live_seen


class Test_readable:
    def test_accepts_the_lines_with_fences_blanked_and_a_comment_as_text(self):
        """#1012: a record carries no comment, so `readable` keeps none of
        the comment state and a comment comes back as the text it is."""
        text = "a\n<!-- b -->\n```\n| x | y |\n```\n| c | d |\n"
        assert READER.readable(text) == ["a", "<!-- b -->", "", "", "", "| c | d |"]

    def test_refuses_an_indented_delimiter_as_a_fence(self):
        """Four spaces before a run of backticks is never a delimiter
        (CommonMark 4.5); read as one, it opens a fence nobody closes and
        every row below it disappears."""
        text = "A fence opens with\n\n    ```\n\n| a | b |\n|---|---|\n| c | d |\n"
        assert "| c | d |" in READER.readable(text)

    @pytest.mark.parametrize(
        "lines, fenced",
        [
            # A closer carries nothing after its run.
            (["```", "inside", "```python", "quoted", "```", "after"], {0, 1, 2, 3, 4}),
            # A backtick opener whose info string holds a backtick opens nothing.
            (["```x`", "quoted", "after"], set()),
            # A tilde opener's info string is unrestricted.
            (["~~~ `x`", "quoted", "~~~", "after"], {0, 1, 2}),
        ],
    )
    def test_each_reader_asks_the_one_delimiter_rule(self, lines, fenced):
        """`readable` blanks exactly the fenced lines, and `live_lines` calls
        exactly those not live but the opener's own line."""
        blanked = {
            n for n, line in enumerate(READER.readable("\n".join(lines))) if not line
        }
        assert blanked == fenced, blanked
        openers = {first for first, _ in READER.fence_spans(lines)}
        parked = {n for n, (_, live) in enumerate(READER.live_lines(lines)) if not live}
        assert parked == fenced - openers, parked


class Test_headings:
    def test_accepts_each_heading_by_the_one_rule(self):
        lines = ["## a", "text", "   ### b  ", "#120) wrapped"]
        assert READER.headings(lines) == [(0, "## a"), (2, "   ### b")]

    def test_refuses_a_line_opening_with_an_issue_number(self):
        assert READER.headings(["#120) wrapped onto its own line"]) == []


class Test_sections:
    LINES = (
        "## Not verified",
        "x",
        "## Not verified (who must answer)",
        "### Not verified on Windows",
    )

    def test_accepts_the_heading_spelt_exactly_and_no_heading_near_it(self):
        assert READER.sections(self.LINES, GAPS.HEADING) == [0]

    def test_refuses_another_spelling_of_the_heading(self):
        assert READER.sections(self.LINES[1:], GAPS.HEADING) == []


# --- a reading written from the format, for `Test_live_lines` -----------------


def a_reading_from_the_commonmark_rules(lines):
    """A reference reading of a markdown document, written from the format.

    Nothing here is named after, or copied from, a choice `live_lines` made —
    that was round 5's finding 2, where this function's block rule was the
    reader's own and the case built on it could not report the reader being
    wrong. Every rule below cites the specification it comes from, so a
    disagreement is settled by reading the spec rather than by reading the
    module under test.

    - **Fenced code blocks** (CommonMark 4.5): a line whose first non-space
      run is three or more backticks or tildes opens one, unless a backtick
      run's info string holds a backtick; a line whose run is the same
      character and at least as long, with nothing after it but spaces,
      closes it. Nothing inside is parsed. The two info-string clauses
      arrived with #491: before them this reading closed a block on
      ```` ```python ```` and opened one on ```` ```x` ````, which the format
      does neither of.
    - **HTML comments** (CommonMark 6.6, raw HTML): `<!--` opens and the next
      `-->` closes, and between them the document is not markdown at all, so
      backticks are ordinary characters.
    - **Code spans** (CommonMark 6.1): a backtick string is closed by the
      next backtick string of equal length; one with no partner is literal
      text. A code span is inline content of a leaf block, so its partner
      must lie in the same block.
    - **Where a block ends** (CommonMark 4.1, 4.2, 4.3, 4.5, 4.8, 5.1, 5.2
      and GFM 4.10): a blank line, a thematic break, an ATX heading, a fence
      delimiter, a block quote marker, a list item marker, a setext
      underline, or a table row. **A richer list is a WEAKER case, not a
      safer one**, and the sentence here used to claim the opposite. Every
      extra stop shortens `partner_in_this_block`, which makes this reading
      see fewer spans, which makes it call MORE lines live — and the only
      violation this case can report is the scan live where this reading
      parks. So each rule is the format's rule and no other, and the two
      indentation bounds below are where that stopped being true (round 6,
      finding 2).

    A line is live when it begins outside all three.
    """

    def block_ends_at(line):
        indent = len(line) - len(line.lstrip(" "))
        s = line.strip()
        if not s:
            return True
        if s.startswith("|") or s.startswith(">"):
            return True
        if indent <= 3 and s.startswith("#"):
            # CommonMark 4.2: one to six hashes, then a space, a tab or the
            # end of the line. The guard this replaces read
            # `s.lstrip("#").startswith((" ", ""))`, and `str.startswith("")`
            # is true of every string, so it asserted nothing.
            n = len(s) - len(s.lstrip("#"))
            if 1 <= n <= 6 and (len(s) == n or s[n] in " \t"):
                return True
        if set(s) == {"="}:
            return True
        # Only an opener interrupts a paragraph (CommonMark 4.5), and `opens`
        # below is this reading's opener rule, bound and info string included.
        if opens(line) is not None:
            return True
        if len(s) >= 3 and s[0] in "*-_" and set(s.replace(" ", "")) == {s[0]}:
            return True
        if s[:2] in ("- ", "* ", "+ "):
            return True
        return s[:2] in ("1.", "1)") and len(s) > 2 and s[2] in " \t"

    def runs(text, at):
        n = 0
        while at + n < len(text) and text[at + n] == "`":
            n += 1
        return n

    def partner_in_this_block(start_line, start_at, width):
        # Every line reached here is a LATER line than the run's own, so each
        # one is checked: a block that ends on the first of them ends the
        # paragraph the run was opened in.
        for i in range(start_line, len(lines)):
            if block_ends_at(lines[i]):
                return False
            text = lines[i]
            j = start_at if i == start_line else 0
            while j < len(text):
                if text[j] == "`":
                    n = runs(text, j)
                    if n == width:
                        return True
                    j += n
                else:
                    j += 1
        return False

    def fence_of(line):
        # CommonMark 4.5 bounds an opening fence to three spaces. Stripping
        # the line first was the one rule this reading still took from
        # `live_lines`, and while it did, this case agreed with the scan on
        # the very shape that removed a directory (round 6, finding 2).
        # Returns (the run, what follows it), and the two info-string
        # clauses are asked by the caller, because one is an opener's and
        # the other a closer's.
        if len(line) - len(line.lstrip(" ")) > 3:
            return None
        s = line.strip()
        if len(s) < 3 or s[0] not in "`~":
            return None
        n = runs(s, 0) if s[0] == "`" else len(s) - len(s.lstrip("~"))
        return (s[0] * n, s[n:]) if n >= 3 else None

    def opens(line):
        found = fence_of(line)
        if found is None or (found[0][0] == "`" and "`" in found[1]):
            return None
        return found[0]

    def closes(line, run):
        found = fence_of(line)
        return (
            found is not None
            and found[0][0] == run[0]
            and len(found[0]) >= len(run)
            and not found[1].strip()
        )

    fence = None
    in_comment = False
    open_span = None
    verdict = []
    for n, line in enumerate(lines):
        verdict.append(fence is None and not in_comment and open_span is None)
        if fence is not None:
            if closes(line, fence):
                fence = None
            continue
        if not in_comment and open_span is None and opens(line) is not None:
            fence = opens(line)
            continue
        i = 0
        while i < len(line):
            if in_comment:
                if line.startswith("-->", i):
                    in_comment, i = False, i + 3
                else:
                    i += 1
            elif open_span is not None:
                width = runs(line, i)
                if width == open_span:
                    open_span, i = None, i + width
                else:
                    i += width if width else 1
            elif line.startswith("<!--", i):
                in_comment, i = True, i + 4
            elif line[i] == "`":
                width = runs(line, i)
                j, closed = i + width, None
                while j < len(line):
                    here = runs(line, j)
                    if here == width:
                        closed = j + here
                        break
                    j += here if here else 1
                if closed is not None:
                    i = closed
                elif partner_in_this_block(n + 1, 0, width):
                    open_span, i = width, len(line)
                else:
                    i += width
            else:
                i += 1
    return verdict


def documents_with_several_spans_on_a_line(count, seed=20260922):
    """Documents whose lines can carry several code spans, unclosed backtick
    runs, and the block starts a span could be asked to reach past.

    The generator is half of what a fuzz is worth. With at most one span per
    line every formulation of this rule scored zero, and round 5's defect
    needs an unclosed run, a block start on a later line and the run's
    partner after it — so the tokens below include the delimiters, backtick
    runs of two lengths, a table row, a heading, a bullet and a fence.
    """
    rng = random.Random(seed)
    tokens = [
        "<!--",
        "-->",
        "`",
        "``",
        "text",
        " ",
        "<!-- specs/a -->",
        "| row |",
        "```",
        "# head",
        "- item",
        "> quote",
        # The shapes a paragraph rule can be WRONG about, without which the
        # case cannot report the class it is written for. Reverting any of
        # the three paragraph corrections reddened nothing until these
        # arrived (round 6, findings 3 and 4): a hash with no space and seven
        # hashes are paragraph text, an ordered marker that is not 1 does not
        # interrupt a paragraph, a run of `=` is a setext underline, and four
        # spaces before a delimiter is an indented code block.
        "#nospace",
        "####### seven",
        "3. item",
        "===",
        "    ```",
    ]

    def line():
        # One token alone some of the time. A setext underline and an
        # indented delimiter are only themselves when nothing follows them on
        # the line, and while every line was a join of several tokens the
        # case could not see either (round 6, findings 1 and 3).
        if rng.random() < 0.25:
            return rng.choice(tokens)
        return "".join(rng.choice(tokens) for _ in range(rng.randint(1, 8)))

    return [[line() for _ in range(rng.randint(1, 7))] for _ in range(count)]


class Test_module:
    def test_the_fence_rule_and_the_line_split_are_lib_s(self):
        """S12 of #1005: the fence delimiter rule and the line split are
        written once, in `lib/blocks.py`, and this module asks that copy."""
        blocks = os.path.join(ROOT, "lib", "blocks.py")
        for name in ("fence_opener", "fence_closes", "gfm_lines"):
            code = getattr(READER, name).__code__
            assert os.path.samefile(code.co_filename, blocks), (name, code.co_filename)
        with open(READER.__file__, encoding="utf-8") as handle:
            source = handle.read()
        for defined in ("def fence_opener(", "def fence_closes(", "def gfm_lines("):
            assert defined not in source, defined
        assert "GFM_LINE_RE = re.compile" not in source


test_census = census_case(TARGET)

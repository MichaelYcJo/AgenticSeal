"""`tests/commonmark_oracle.py`'s own cases (#667, #673, #677).

The oracle says which lines of a markdown document a CommonMark renderer
hides, and the readers under `lib/` are held to it in their own module
files. The cases here hold the oracle itself: on every shape of
`tests/block_shapes.py` it gives the *Renderer* column, it names each kind
it hides, it counts the lines the parser's strip drops, and it reads a
reader's split as the text it is.

That it imports the parser and nothing of this repository's is held in
`tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py` with the
shape data it is checked on.
"""

import commonmark_oracle as oracle
import pytest
from block_shapes import BREAKS, CLOSE, INLINE_KINDS, OPEN, RENDERER, SHAPES
from conftest import census_case
from test_blocks import NBSP

TARGET = "tests/commonmark_oracle.py"

# Every character `str.strip` removes that stands inside a CommonMark line:
# Python calls it whitespace, `str.splitlines` does not break at it, and it
# is neither a space nor a tab, which CommonMark reads as indentation or a
# blank line. Computed, so a Unicode version that adds one tests it without a
# row being written. The breaks `str.splitlines` makes and CommonMark does
# not are `hidden_text`'s mapping, and `BREAKS` holds them.
DROPPED_BY_THE_STRIP = [
    chr(point)
    for point in range(0x110000)
    if chr(point).isspace()
    and len(("a" + chr(point) + "b").splitlines()) == 1
    and chr(point) not in " \t"
]


class Test_module:
    """`test_the_oracle_names_each_kind_it_hides` and
    `test_the_oracle_counts_the_lines_the_parsers_strip_dropped` call
    `hidden` alike and differ by their rows: the first gives one document
    per kind a renderer hides, and the second gives paragraphs that open
    with a line the parser's strip drops."""

    @pytest.mark.parametrize("name", sorted(SHAPES))
    def test_the_oracle_gives_the_frames_renderer_column(self, name):
        """S1, and the frame's Q2. The *Renderer* column was derived by reading
        CommonMark section 4.5, section 4.6 and section 6.6 and was not executed; the parser gives it
        on every shape. Where the two disagreed, the oracle would win and the
        divergence would be recorded in `gaps.md`."""
        assert oracle.hidden_lines(SHAPES[name]) == RENDERER[name]

    @pytest.mark.parametrize(
        "lines, hidden",
        [
            # a fence, its delimiters included
            (["a", "", "```", "x", "```", "b"], {2: "fence", 3: "fence", 4: "fence"}),
            # four spaces after a blank line is an indented code block
            (["a", "", "    x", "", "b"], {2: "code"}),
            # a comment block runs to the first line holding the closer
            ([OPEN, "x", f"y {CLOSE} z", "b"], {0: "html", 1: "html", 2: "html"}),
            # any other HTML block hides the lines it holds, fence lines included
            (["<div>", "```", "x", "", "b"], {0: "html", 1: "html", 2: "html"}),
            # an inline comment hides the lines that begin inside it, and not the
            # line it opens on
            (
                ["x " + OPEN + " y", "z", CLOSE + " w", "v"],
                {1: "inline html", 2: "inline html"},
            ),
            # a blank line ends the paragraph, so the comment never closes
            (["x " + OPEN + " y", "", "z", CLOSE], {}),
            # inside a code span a delimiter is text
            ([f"x `{OPEN}` y", "z", f"`{CLOSE}`"], {}),
            # a table row is its own inline, so no comment spans two rows
            (["| a | b |", "|---|---|", f"| c {OPEN} d |", f"| e {CLOSE} |"], {}),
            # a fence inside a list item ends with the item
            (["- a", "  ```", "  x", "b"], {1: "fence", 2: "fence"}),
            # CRLF is the same document
            (["```\r", "x\r", "```\r", "y\r"], {0: "fence", 1: "fence", 2: "fence"}),
            # markdown-it-py 4.2.0 runs an inline comment past a closer that a
            # `-` precedes, which CommonMark 0.31.2 section 6.6 does not: a comment's
            # text may not hold `-->`. Pinned by name (#667 round 1, ⬜ 4), so a
            # wider corpus meets the divergence here, and so the walk, which
            # follows the specification, is never "fixed" toward the parser.
            (
                ["x " + OPEN + " a", "b ---> c", "d " + CLOSE + " e", "f"],
                {1: "inline html", 2: "inline html"},
            ),
            # #673: every other kind of inline raw HTML hides the lines that
            # begin inside it the same way -- CDATA, a processing instruction, a
            # declaration, an open tag inside either kind of quoted value, and an
            # open tag between its attributes
            (
                ["x <![CDATA[ a", "b", "c ]]> d", "e"],
                {1: "inline html", 2: "inline html"},
            ),
            (["x <? a", "b", "c ?> d", "e"], {1: "inline html", 2: "inline html"}),
            (["x <!DOCTYPE a", "b", "c> d", "e"], {1: "inline html", 2: "inline html"}),
            (
                ['x <span title="a', "b", 'c"> d', "e"],
                {1: "inline html", 2: "inline html"},
            ),
            (
                ["x <span title='a", "b", "c'> d", "e"],
                {1: "inline html", 2: "inline html"},
            ),
            (["x <span", 'lang="en">', "e"], {1: "inline html"}),
            # a list item whose first line holds only a Unicode space, which the
            # parser's strip drops: its marker is not text, so the lines are
            # counted from the next one -- a bullet, a number, a bullet inside a
            # quote; a `-` with no space after it is no marker, and is text
            (["- " + NBSP, "x <? a", "b ?>", "c"], {2: "inline html"}),
            (["1. " + NBSP, "x <? a", "b ?>", "c"], {2: "inline html"}),
            (["> - " + NBSP, "x <? a", "b ?>", "c"], {2: "inline html"}),
            (["-" + NBSP, "x <? a", "b ?>", "c"], {2: "inline html"}),
            # a later line of the paragraph carries no list marker: a `*` or a
            # `2.` there is text, since an item that could interrupt would have
            # ended the paragraph, and the parser's strip keeps it
            ([NBSP, "*", "x <? a", "b ?>", "c"], {3: "inline html"}),
            (["> " + NBSP, "> 2.", "> x <? a", "> b ?>"], {3: "inline html"}),
            # while a quote's `>` is a marker on every line of it
            (["> " + NBSP, "> " + NBSP, "> x <? a", "> b ?>"], {3: "inline html"}),
            # every other marker the count-back reads on the opening line: the
            # other two bullets, the `)` delimiter, a tab after a marker and one
            # before it, and a number of ten digits, which is no marker
            (["+ " + NBSP, "x <? a", "b ?>", "c"], {2: "inline html"}),
            (["* " + NBSP, "x <? a", "b ?>", "c"], {2: "inline html"}),
            (["1) " + NBSP, "x <? a", "b ?>", "c"], {2: "inline html"}),
            (["-\t" + NBSP, "x <? a", "b ?>", "c"], {2: "inline html"}),
            ([">\t* " + NBSP, "> x <? a", "> b ?>", "> c"], {2: "inline html"}),
            (["1234567890. " + NBSP, "x <? a", "b ?>", "c"], {2: "inline html"}),
        ],
        ids=[
            "fence",
            "code",
            "comment block",
            "other html",
            "inline comment",
            "blank ends it",
            "code span",
            "table rows",
            "list item",
            "crlf",
            "past the first closer",
            "cdata",
            "instruction",
            "declaration",
            "double-quoted value",
            "single-quoted value",
            "between attributes",
            "behind a list marker",
            "behind an ordered marker",
            "behind a quote and a marker",
            "a dash that is no marker",
            "a star on a later line is text",
            "a number on a later quoted line is text",
            "a quote marker on a later line",
            "behind a plus",
            "behind a star",
            "behind a parenthesis",
            "a tab after a marker",
            "a tab before a marker",
            "ten digits are no marker",
        ],
    )
    def test_the_oracle_names_each_kind_it_hides(self, lines, hidden):
        """What each of the four kinds is, one case each, so a reader of this
        module can see what "a renderer hides" means before any reader is held
        to it. `inline html` is all six kinds of CommonMark 6.6, one case each
        but the closing tag's: a line ending inside one puts `>` at the next
        line's start, which opens a block quote."""
        assert oracle.hidden(lines) == hidden

    @pytest.mark.parametrize(
        "lines, hidden",
        [
            # #677, the shapes of #673 round 3: a `>` four columns in, or behind a
            # tab, on a paragraph's later line is lazy-continuation text the
            # paragraph keeps, and not a quote marker
            ([NBSP, "    >", "x <? a", "b ?>"], {3: "inline html"}),
            ([NBSP, "\t>", "x <? a", "b ?>"], {3: "inline html"}),
            (["- " + NBSP, "      >", "  x <? a", "  b ?>"], {3: "inline html"}),
            (["> " + NBSP, ">     >", "> x <? a", "> b ?>"], {3: "inline html"}),
            ([NBSP, "    > >", "x <? a", "b ?>"], {3: "inline html"}),
            # a setext heading's text is joined and stripped as a paragraph's is,
            # so the parser's `lheading` rule is asked too
            ([NBSP, "x <? a", "b ?>", "==="], {2: "inline html"}),
            ([NBSP, "x <? a", "b ?>", "---"], {2: "inline html"}),
            (["> " + NBSP, "> x <? a", "> b ?>", "> ==="], {2: "inline html"}),
            # every other container and line shape the hand count had to know
            # about: a quote's marker one or three columns in, with no space
            # after it, three columns in on a later line, and dropped on a lazy
            # line
            ([" > " + NBSP, " > x <? a", " > b ?>"], {2: "inline html"}),
            (["   > " + NBSP, "   > x <? a", "   > b ?>"], {2: "inline html"}),
            ([">" + NBSP, ">x <? a", ">b ?>"], {2: "inline html"}),
            (["> " + NBSP, "   > x <? a", "   > b ?>"], {2: "inline html"}),
            (["> " + NBSP, "x <? a", "b ?>"], {2: "inline html"}),
            # an item continued by indentation, four spaces after a bullet, the
            # widest number that is a marker, and an item that opens on a blank
            # line, whose paragraph starts one line into it
            (["- " + NBSP, "  x <? a", "  b ?>"], {2: "inline html"}),
            (["-    " + NBSP, "x <? a", "b ?>"], {2: "inline html"}),
            (["123456789. " + NBSP, "x <? a", "b ?>", "c"], {2: "inline html"}),
            (["-", "  " + NBSP, "  x <? a", "  b ?>"], {3: "inline html"}),
            # containers inside containers, and the `>` four columns in that IS
            # a marker, inside `10. >`: the one no column count can tell from
            # the lazy `>` rows above
            (["- > " + NBSP, "  > x <? a", "  > b ?>"], {2: "inline html"}),
            (["- - " + NBSP, "    x <? a", "    b ?>"], {2: "inline html"}),
            (["> > " + NBSP, "> > x <? a", "> > b ?>"], {2: "inline html"}),
            (["10. > " + NBSP, "    > x <? a", "    > b ?>"], {2: "inline html"}),
            # two dropped lines, one mixing spaces, a tab and no-break spaces,
            # and a paragraph after a reference definition, which starts on the
            # definition's next line
            ([NBSP, NBSP, "x <? a", "b ?>"], {3: "inline html"}),
            ([" " + NBSP + "\t" + NBSP, "x <? a", "b ?>"], {2: "inline html"}),
            (["[a]: /u", NBSP, "x <? a", "b ?>"], {3: "inline html"}),
        ],
        ids=[
            "a > four columns in is text",
            "a > behind a tab is text",
            "a > four columns into an item is text",
            "a > four columns into a quote is text",
            "two indented > are text",
            "a level 1 setext heading",
            "a level 2 setext heading",
            "a setext heading inside a quote",
            "a quote one column in",
            "a quote three columns in",
            "a quote with no space after its marker",
            "a later quote marker three columns in",
            "a quote's lazy line drops the >",
            "an item continued by indentation",
            "four spaces after a bullet",
            "nine digits are a marker",
            "an item that opens on a blank line",
            "a quote inside an item",
            "an item inside an item",
            "a quote inside a quote",
            "a > four columns in that is a marker",
            "two dropped lines",
            "spaces, a tab and no-break spaces mixed",
            "a reference definition before the paragraph",
        ],
    )
    def test_the_oracle_counts_the_lines_the_parsers_strip_dropped(self, lines, hidden):
        """#677. The parser joins a paragraph's lines from behind the container
        markers it consumed and applies `str.strip` to the whole, which also
        drops a line holding only a no-break space, another Unicode space or
        U+001F, which CommonMark reads as text. Every row's paragraph opens with
        such a line, so every row puts its inline HTML one line early or late wherever the oracle
        counts those lines wrong.

        The count is taken from the parser's own `paragraph` and `lheading`
        rules, because reading the markers here took three rounds of #673 and
        each found one more marker read wrong. A row is here to fail if the count
        is read from anything but what the parser joined: each shape is a
        container or a line the old hand count had to know about."""
        assert oracle.hidden(lines) == hidden

    @pytest.mark.parametrize(
        "char", DROPPED_BY_THE_STRIP, ids=lambda char: f"U+{ord(char):04X}"
    )
    def test_the_oracle_counts_every_character_the_strip_drops(self, char):
        """#677. A line holding only CHAR is paragraph text to CommonMark and is
        dropped whole by the parser's strip, at the top level and behind a list
        marker. U+001F is the one CommonMark does not call whitespace at all."""
        assert oracle.hidden([char, "x <? a", "b ?>"]) == {2: "inline html"}
        assert oracle.hidden(["- " + char, "x <? a", "b ?>"]) == {2: "inline html"}

    def test_the_strips_set_is_the_one_measured(self):
        """The case above is skipped, not failed, when its set comes out empty,
        and it passes on a space or a tab, which CommonMark reads as a blank
        line. So the set holds what Python 3.12, 3.13 and 3.14 all give, and
        neither of those two (#677)."""
        dropped = set(DROPPED_BY_THE_STRIP)
        assert {chr(0x1F), NBSP, chr(0x1680), chr(0x2000), chr(0x3000)} <= dropped
        assert not {" ", "\t"} & dropped

    @pytest.mark.parametrize("name", sorted(BREAKS))
    def test_the_oracle_reads_the_text_not_a_readers_split(self, name):
        """#667 round 1, 🟡 1. `hidden_text` hands the parser TEXT, broken where
        CommonMark breaks, and answers per `text.splitlines()` line: a reader's
        line that is a piece of a shown line is shown, and a piece of a hidden
        line is hidden. Before, the oracle joined the reader's split and so
        agreed with any walk that read it."""
        brk = BREAKS[name]
        assert oracle.hidden_text(f"A note{brk}{OPEN}\n\n| a |\n{CLOSE}\n") == {}
        assert set(oracle.hidden_text(f"```\nx{brk}y\n```\nz\n")) == {0, 1, 2, 3}
        # round 2: a piece is asked where it starts, not where its line does --
        # inside a comment its own line opened, and just past one it closed
        assert oracle.hidden_text(f"x {OPEN} a{brk}| b |\n{CLOSE}\n") == {
            1: "inline html",
            2: "inline html",
        }
        assert oracle.hidden_text(f"x {OPEN} a\nb {CLOSE}{brk}| c |\n") == {
            1: "inline html"
        }
        # #673: every other kind of inline raw HTML, opened before the break and
        # closed after it, holds the piece; closed before the break, it holds
        # nothing after it
        for opener, closer in INLINE_KINDS:
            assert oracle.hidden_text(f"x {opener}{brk}| b |\n{closer}\n") == {
                1: "inline html",
                2: "inline html",
            }, opener
            assert oracle.hidden_text(f"x {opener} {closer}{brk}| c |\n") == {}, opener
        # an open tag's piece between its attributes, and a closing tag's piece
        # at its `>`, where no letter may stand
        assert oracle.hidden_text(f'x <span{brk}lang="en">\n') == {1: "inline html"}
        assert oracle.hidden_text(f"x </span{brk}>\n") == {1: "inline html"}
        # inside an image description, whose tokens are the image's children: a
        # renderer writes the description as the `alt` text and leaves HTML out
        assert oracle.hidden_text(f'![x <span title="a{brk}b">](u)\n') == {
            1: "inline html"
        }


test_census = census_case(TARGET)

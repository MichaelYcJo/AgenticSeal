"""The readers under `lib/` hide what a CommonMark renderer hides, and nothing else
(#667).

The acceptance property is below.
For every line L of a document, with `base(L)` a reader's reading at
`release/v0.16.0` and `renderer(L)` the oracle's:

  1. the reader never leaves both -- `new(L)` is `base(L)` or `renderer(L)`;
  2. where the walk claims to be exact, it is -- every line it does not call
     uncertain is classed as the oracle classes it;
  3. on every shape `tests/block_shapes.py` holds, the reader gives its
     expected answer.

The oracle comes first, and it is the first thing held: before any reader
moved, it had to give `RENDERER` on every shape, which was derived by
reading the specification and could not be executed. This module holds the
oracle, `tests/commonmark_oracle.py`, and nothing else.

Each reader is held in its own module file, over those shapes and the
seeded generated corpus `tests/lib/test_blocks.py` builds: half 1 in
`tests/lib/test_tables.py`'s `Test_unfenced` and `tests/lib/test_routing.py`'s
`Test_module`, half 2 in `tests/lib/test_blocks.py`'s `Test_walk` and
`Test_walk_text`, where #1489's phase 3 moved them from here, and half 3 in
each reader's own case table (#942's phase 6).
"""

import os

import commonmark_oracle as oracle
import pytest
from block_shapes import BREAKS, CLOSE, INLINE_KINDS, OPEN, RENDERER, SHAPES
from conftest import ROOT, imported_roots
from test_blocks import NBSP

# --- the oracle is independent, and it says what the frame read -------------


def test_the_oracle_imports_the_parser_and_nothing_of_this_repositorys():
    """S1. The oracle shares no code with the walk it checks: its only
    import is the parser, and it reaches for no path of this repository's.
    Round 3 of 1790635413: "The oracle cannot catch this, because it is
    built the same way." The shape data it is checked on imports nothing."""
    assert imported_roots(oracle.__file__) == {"markdown_it"}
    with open(oracle.__file__, encoding="utf-8") as handle:
        source = handle.read()
    for reach in ("sys.path", "importlib", "lib/", "skills/", ".github"):
        assert reach not in source.split('"""', 2)[-1], reach
    assert imported_roots(os.path.join(ROOT, "tests", "block_shapes.py")) == set()


@pytest.mark.parametrize("name", sorted(SHAPES))
def test_the_oracle_gives_the_frames_renderer_column(name):
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
        (["x <![CDATA[ a", "b", "c ]]> d", "e"], {1: "inline html", 2: "inline html"}),
        (["x <? a", "b", "c ?> d", "e"], {1: "inline html", 2: "inline html"}),
        (["x <!DOCTYPE a", "b", "c> d", "e"], {1: "inline html", 2: "inline html"}),
        (['x <span title="a', "b", 'c"> d', "e"], {1: "inline html", 2: "inline html"}),
        (["x <span title='a", "b", "c'> d", "e"], {1: "inline html", 2: "inline html"}),
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
def test_the_oracle_names_each_kind_it_hides(lines, hidden):
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
def test_the_oracle_counts_the_lines_the_parsers_strip_dropped(lines, hidden):
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


@pytest.mark.parametrize(
    "char", DROPPED_BY_THE_STRIP, ids=lambda char: f"U+{ord(char):04X}"
)
def test_the_oracle_counts_every_character_the_strip_drops(char):
    """#677. A line holding only CHAR is paragraph text to CommonMark and is
    dropped whole by the parser's strip, at the top level and behind a list
    marker. U+001F is the one CommonMark does not call whitespace at all."""
    assert oracle.hidden([char, "x <? a", "b ?>"]) == {2: "inline html"}
    assert oracle.hidden(["- " + char, "x <? a", "b ?>"]) == {2: "inline html"}


def test_the_strips_set_is_the_one_measured():
    """The case above is skipped, not failed, when its set comes out empty,
    and it passes on a space or a tab, which CommonMark reads as a blank
    line. So the set holds what Python 3.12, 3.13 and 3.14 all give, and
    neither of those two (#677)."""
    dropped = set(DROPPED_BY_THE_STRIP)
    assert {chr(0x1F), NBSP, chr(0x1680), chr(0x2000), chr(0x3000)} <= dropped
    assert not {" ", "\t"} & dropped


@pytest.mark.parametrize("name", sorted(BREAKS))
def test_the_oracle_reads_the_text_not_a_readers_split(name):
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
    assert oracle.hidden_text(f'![x <span title="a{brk}b">](u)\n') == {1: "inline html"}

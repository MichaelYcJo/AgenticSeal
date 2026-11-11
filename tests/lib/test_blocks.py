"""`lib/blocks.py`, one class per function its cases reach.

The walk's own answers came from `tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py`
and the splitter's from `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py`
(#942's phase 6). The second file keeps what holds every copy of the
splitter to this one, a check of several files against each other, and
`tests/behaviour/test_unverified_rows_close.py` keeps the case that holds this module's
fence walks to `lib/lines.py`'s and `lib/tables.py`'s, for the same
reason.

`Test_walk` and `Test_walk_text` hold the walk to a CommonMark oracle,
`tests/commonmark_oracle.py`, over the corpus this file builds: on every line
the walk does not call uncertain, the walk and the oracle agree. #1489's
phase 3 moved those two cases and the corpus here from the first file. The
oracle's own cases stand in `tests/test_commonmark_oracle.py`, and the first
file keeps the case that holds the oracle imports nothing of this
repository's. `tests/lib/test_tables.py` and `tests/lib/test_routing.py`
import the corpus from here and hold their readers to the oracle over it.
"""

import commonmark_oracle as oracle
import pytest
from block_shapes import BREAKS, CLOSE, INLINE_KINDS, OPEN, RENDERER, SHAPES
from conftest import SPLITLINES_ONLY, census_case, load_lib_module, texts

TARGET = "lib/blocks.py"

blocks = load_lib_module("blocks.py", "agentic_blocks_under_test")
# The name the splitter's cases read it by, from when they read it through
# the reader that handed this module's `gfm_lines` to its callers.
reader = blocks

# An opener and a closer of every other kind of inline raw HTML, with a
# closer that can stand at a line's start or directly after the opener (#673).
# The closing tag's closer is `>` and is only ever written on the same line.
INLINE_OPEN_CLOSE = [
    *INLINE_KINDS,
    ("<span", 'a="b">'),
    ("</span", ">"),
]


# --- the corpus every reader under `lib/` is held to the oracle over ---------
#
# This file's walk, `tests/lib/test_tables.py`'s table walker and
# `tests/lib/test_routing.py`'s routing reader are each held to
# `tests/commonmark_oracle.py` over it (#667).

# Spelled by its code point, so no line of this file carries the character
# itself for a reader to mistake for a space.
NBSP = chr(0xA0)

# Every line of each shape in `COMMENT_SHAPES` is a place a reading of fences
# or comments has had to be right.
COMMENT_SHAPES = [
    [OPEN, "| a | b |", CLOSE, "| c | d |"],
    [OPEN + " x", "| a | b |"],
    [OPEN + " one line " + CLOSE, "| a | b |"],
    ["| a |", OPEN, "| b |", CLOSE, OPEN, "| c |"],
    ["```", OPEN, "```", "| a |", CLOSE],
    [OPEN, "```", CLOSE, "```", "| a |"],
    [OPEN + "\r", "| a |\r", CLOSE + "\r", "| b |\r"],
    [f"text `{OPEN}` more", "| a |", f"`{CLOSE}`", "| b |"],
    [f"a note quoting `{OPEN}`", "```", "| a |", "```", "| b |"],
    [f"{OPEN} a note with `{CLOSE}` in it", "| a |", CLOSE, "| b |"],
    [f"a lone ` then {OPEN} x", "| a |", CLOSE, "| b |"],
    [f"{OPEN} a {CLOSE} {OPEN} b", "| x |", "c " + CLOSE, "| y |"],
    [OPEN, OPEN + " nested", CLOSE, "| a |", CLOSE],
    [OPEN, "| a |", f"{CLOSE} {OPEN}", "| b |"],
    ["<!-->", "| a |", CLOSE, "| b |"],
    ["a note " + OPEN + " never closed", "| a |", "```", "| b |", "```", "| c |"],
]

BREAK_SAMPLE = [BREAKS[name] for name in ("LS", "PS", "NEL", "FF", "FS")]

# Lines the generated documents are drawn from. Each is here because it is a
# delimiter, a container, or a context `lib/blocks.py` calls uncertain, and
# a context the walk is ever made exact for has to be in this list first: the
# property is only as good as what the corpus can hold.
ALPHABET = [
    "",
    "text",
    "| a | b |",
    "|---|---|",
    "```",
    "````",
    "~~~",
    "```python",
    "``` `x`",
    "```\t",
    "   ```",
    "    ```",
    "\t```",
    OPEN,
    OPEN + " x",
    "x " + OPEN,
    "x " + OPEN + " y " + CLOSE,
    CLOSE,
    "x " + CLOSE,
    CLOSE + " x " + OPEN,
    OPEN + " a " + CLOSE,
    "<!-->",
    "<!---->",
    "   " + OPEN,
    "    " + OPEN,
    "`" + OPEN + "`",
    "`",
    "a lone ` then " + OPEN,
    "- item",
    "- ```",
    "- " + OPEN,
    "  ```",
    "  | a |",
    "1. ```",
    "> quote",
    "> ```",
    "> " + OPEN,
    # A block quote needs no space after its marker (CommonMark 5.1; #667
    # round 1, 🟡 2).
    ">```",
    ">" + OPEN,
    ">| a |",
    "    code",
    # An indented code block inside a container, whose line starts with the
    # container's marker, and indentation counted with a tab in it.
    ">     code",
    "-     code",
    "1.     code",
    "  \tcode",
    "\tcode",
    "<div>",
    "</div>",
    "<br>",
    "<https://example.com>",
    "<pre>",
    "</pre>",
    "# heading",
    "---",
    "~~~~ x",
    # A no-break space: CommonMark counts neither it as a blank line nor it
    # after a closing run as a space, and Python's `str.strip` counts both.
    NBSP,
    "``` " + NBSP,
    "~~~" + NBSP,
    "text " + OPEN + " a " + CLOSE + " b " + OPEN,
    CLOSE + OPEN,
    OPEN + "--->",
    "`````",
    "```~",
    "~~~ ~",
    "<?php",
    "<!DOCTYPE html>",
    "<script>",
    "</script>",
    "* item",
    "10) ```",
    "> a " + OPEN,
    "| x " + OPEN + " |",
    "[ref]: <x>",
    # A character `str.splitlines` ends a line at and CommonMark does not, in
    # front of a comment opener, a fence run and a row, so a document can
    # hold a reader line that is a piece of a renderer's line (#667 round 1,
    # 🟡 1). Five of the eight, one of each family.
    *(f"a{brk}{rest}" for brk in BREAK_SAMPLE for rest in (OPEN, "```", "| a |")),
    *(f"{brk}{CLOSE}" for brk in BREAK_SAMPLE),
    # A break inside an inline comment its line opened, and one just past a
    # comment its line closed, so a piece can start inside a comment or just
    # outside one (#667 round 2). Four lines: twenty pushed
    # `test_the_walk_is_exact_somewhere` under its third, because every line
    # a mid-line opener leaves open is one the walk does not claim.
    f"x {OPEN} a{BREAKS['LS']}```",
    f"x {OPEN} a{BREAKS['FF']}| a |",
    f"x {OPEN} a{BREAKS['NEL']}{CLOSE}",
    f"b {CLOSE}{BREAKS['LS']}```",
]

# The lines above that stand at the top level and start no block the walk
# does not follow. A document drawn from these alone is one the walk claims
# most of, which is where half 2 has something to check; a document drawn
# from the whole alphabet reaches the uncertain contexts too.
TOP_LEVEL = [
    line
    for line in ALPHABET
    if not line.startswith((" ", "\t", "-", "*", "1", ">"))
    and not (line.startswith("<") and not line.startswith(OPEN))
]

# The frame's Q7. Seeded, so a red is reproducible by its seed. Measured on
# 2026-09-29, one core, on the macOS machine phase 2 ran on: 20,000 documents
# of up to 24 lines took about 1.1 s for the oracle and the walk together,
# and 60 seeds of 20,000 found no disagreement (phase 2's record). 6,000 of up
# to 16 lines keeps each property case near a third of a second; raising
# CORPUS_SIZE is how a local run looks further.
SEED = 667
CORPUS_SIZE = 6000


def generated(size=CORPUS_SIZE, seed=SEED):
    """`size` documents of one to sixteen lines, the same ones on every run:
    half drawn from the top-level lines, half from the whole alphabet."""
    import random

    rng = random.Random(seed)
    docs = []
    for number in range(size):
        pool = TOP_LEVEL if number % 2 else ALPHABET
        lines = [rng.choice(pool) for _ in range(rng.randint(1, 16))]
        if rng.random() < 0.1:
            lines = [line + "\r" for line in lines]
        docs.append(lines)
    return docs


# Documents a wider generated run found the walk or the oracle wrong on while
# phase 2 was built, each reduced to the lines that matter, and kept so the
# next run meets them whatever the seed draws.
FOUND = [
    # a blank line between two indented lines is inside the code block
    ["    code", "", "    more"],
    # a list item whose content is an indented code block
    ["-     code"],
    # a line of only a no-break space is paragraph text, which the parser's
    # own `str.strip` drops from the top of the inline source
    [NBSP, "x " + OPEN, "x " + CLOSE],
    # a no-break space after a closing run: CommonMark does not close there
    ["```", "x", "``` " + NBSP, "y", "```", "z"],
    # round 1, 🟡 2: a block quote needs no space after its marker
    [">```"],
    # round 1, 🟡 1: a comment opener, and a fence run, after a line break
    # `str.splitlines` makes and CommonMark does not
    ["A note" + BREAKS["LS"] + OPEN, "", "| a | b |", CLOSE],
    ["A note" + BREAKS["FF"] + "```", "", OPEN + " RIDER: r " + CLOSE, "```"],
    # round 2: a piece that starts inside an inline comment its line opened
    ["x " + OPEN + " a" + BREAKS["LS"] + "```" + BREAKS["LS"] + "| a |", CLOSE],
    # #673: the same piece inside every other kind of inline raw HTML, and a
    # line after it inside the same paragraph. Here and not in ALPHABET: six
    # alphabet lines pushed `test_the_walk_is_exact_somewhere` under its
    # third, and an opener without its closer never forms inline HTML.
    ["x <![CDATA[ a" + BREAKS["LS"] + "```" + BREAKS["LS"] + "| a |", "]]>"],
    ["x <? a" + BREAKS["FF"] + "```" + BREAKS["FF"] + "| a |", "| b |", "?>"],
    ["x <!DOCTYPE a" + BREAKS["GS"] + "```" + BREAKS["GS"] + "| a |", "a>"],
    ['x <span title="a' + BREAKS["NEL"] + "```", "| a |", '">'],
    ["x <span title='a" + BREAKS["PS"] + "```", "| a |", "'>"],
    # between a tag's attributes no row can start, but a later line can
    # begin inside the tag; a closing tag holds only whitespace before `>`
    ["x <span" + BREAKS["LS"] + 'lang="en"', 'title="t">', "| a |"],
    ["x </span" + BREAKS["VT"] + ">", "| a |"],
    # an opener a renderer does not honour -- in a code span -- whose end
    # lies inside a construct that is real: reading on from that end would
    # step over the real opener
    ["x `<?` <![CDATA[ a ?> b" + BREAKS["LS"] + "```" + BREAKS["LS"] + "| a |", "]]>"],
    # a comment opener a renderer does not honour leaves the paragraph
    # pending, and a real opener before the next `-->` must not be stepped
    # over by that `-->`
    ["x `" + OPEN + "` a", "b <? c " + CLOSE + " d", "e ?> f", "| a |"],
    # #677: a `>` four columns in on a paragraph's later line is text; an
    # oracle that read it as a marker put the inline HTML on the blank line,
    # and called hidden a line the walk rightly claims live
    [NBSP, "    >", "x <? a", "b ?>", "", "text"],
]

CORPUS = (
    [SHAPES[name] for name in sorted(SHAPES)]
    + [list(lines) for lines in COMMENT_SHAPES]
    + FOUND
    + generated()
)


def as_read(doc):
    """(text, lines) for a corpus document: the text a reader opens, and the
    lines it splits that text into, which are the indices every answer below
    is given in. A document is written as lines so it can be read; the
    readers and the oracle are both handed the text (#667 round 1, 🟡 1)."""
    text = "\n".join(doc) + "\n"
    return text, text.splitlines()


def disagreements(doc):
    """Lines the walk calls exact and classes otherwise than the oracle."""
    text, lines = as_read(doc)
    found = blocks.walk_text(text)
    renderer = set(oracle.hidden_text(text))
    return [
        (index, found.kinds[index], index in renderer)
        for index in range(len(lines))
        if not found.uncertain[index]
        and (found.kinds[index] != blocks.LIVE) != (index in renderer)
    ]


class Test_gfm_lines:
    def test_refuses_to_end_a_line_at_any_of_the_eight(self):
        for char in SPLITLINES_ONLY:
            assert reader.gfm_lines(f"a{char}b\nc") == [f"a{char}b", "c"], repr(char)
        assert reader.gfm_lines("a\r\nb\rc\nd") == ["a", "b", "c", "d"]
        assert reader.gfm_lines("a\r\nb\n", keepends=True) == ["a\r\n", "b\n"]

    def test_accepts_a_text_without_the_eight_as_splitlines_splits_it(self):
        for text in [t for t in texts() if not any(c in t for c in SPLITLINES_ONLY)]:
            assert reader.gfm_lines(text) == text.splitlines(), repr(text)
            assert reader.gfm_lines(text, True) == text.splitlines(True), repr(text)


class Test_walk:
    def test_accepts_each_paired_fence_with_its_openers_info_string(self):
        """#1198, *Scope* item 1: `lib/fields.py` reads a `seal` block
        by its opener's info string, so the walk hands it, for every fence it
        pairs, the opener's index and the text after its run. Two fences that
        touch are two entries, and a fence quoted inside another is none."""
        fence = "`" * 3
        lines = [
            f"{fence}seal",
            "run: x",
            fence,
            f"{fence} Seal note",
            fence,
            "~~~~",
            f"{fence}seal",
            "~~~~",
            "prose",
        ]
        assert blocks.walk(lines).opens == {0: "seal", 3: " Seal note", 5: ""}

    def test_refuses_an_entry_for_an_opener_that_never_closes(self):
        """An opener nobody closed is no fence: it stays in `unclosed`, and
        a pair below it still has its entry."""
        fence = "`" * 3
        walked = blocks.walk(["~~~seal", "x", f"{fence}seal", "y", fence])
        assert walked.unclosed == [0], walked.unclosed
        assert walked.opens == {2: "seal"}, walked.opens

    def test_the_walk_is_exact_somewhere(self):
        """The half above is empty if everything is uncertain. On the frame's
        shapes the walk claims every line but where a construct never closes or
        a mid-line opener leaves a paragraph open, and it hides the constructs the
        renderer hides."""
        for name in ("C2", "C5", "C6", "R1", "R2", "R4", "R5", "R9", "K1", "K5", "K7"):
            found = blocks.walk(SHAPES[name])
            assert not any(found.uncertain), name
            assert set(found.hidden()) == RENDERER[name], name
        claimed = sum(
            1
            for doc in CORPUS
            for flag in blocks.walk_text(as_read(doc)[0]).uncertain
            if not flag
        )
        total = sum(len(as_read(doc)[1]) for doc in CORPUS)
        assert claimed > total // 3, (claimed, total)


class Test_walk_text:
    def test_accepts_each_opener_at_the_reader_line_it_starts(self):
        """`walk_text` answers per `str.splitlines` line, so an opener's
        entry is keyed by the reader line that starts where the opener
        does."""
        fence = "`" * 3
        text = f"a{BREAKS['LS']}b\n{fence}seal\nrun: x\n{fence}\n"
        assert blocks.walk_text(text).opens == {2: "seal"}
        split = f"{fence}seal{BREAKS['LS']}x\nrun: y\n{fence}\n"
        assert blocks.walk_text(split).opens == {0: f"seal{BREAKS['LS']}x"}

    def test_refuses_to_claim_a_piece_inside_its_lines_open_comment(self):
        """#667 round 2, yellow 1. A piece after a break inside an inline
        comment its line left open is uncertain; a piece of a fenced line
        stays fenced and claimed; a piece that starts before the line's opener
        is claimed live. Each of the three conditions is one line of this
        case."""
        ls = BREAKS["LS"]
        inside = blocks.walk_text(f"a {OPEN} x{ls}| r |\n{CLOSE}\n")
        assert inside.uncertain[:2] == [False, True], inside.uncertain
        fenced = blocks.walk_text(f"```\nx {OPEN} a{ls}y\n```\n")
        assert (fenced.kinds[2], fenced.uncertain[2]) == (blocks.FENCED, False)
        before = blocks.walk_text(f"a{ls}b {OPEN} c\n\nd\n")
        assert before.uncertain[:2] == [False, False], before.uncertain

    def test_refuses_to_claim_a_piece_inside_other_inline_html_its_line_left_open(
        self,
    ):
        """#673's S4. A piece after a break inside CDATA, a processing
        instruction, a declaration or a tag its line left open is uncertain; a
        piece after one its line closed is claimed; a piece of a fenced line
        stays fenced and claimed. And an opener a renderer does not honour
        does not step over one it does."""
        ls = BREAKS["LS"]
        for opener, closer in INLINE_OPEN_CLOSE:
            inside = blocks.walk_text(f"a {opener}{ls}{closer} x\n\nd\n")
            assert inside.uncertain[:2] == [False, True], (opener, inside.uncertain)
            closed = blocks.walk_text(f"a {opener} {closer}{ls}| r |\n\nd\n")
            assert closed.uncertain[:2] == [False, False], (opener, closed.uncertain)
            fenced = blocks.walk_text(f"```\nx {opener}{ls}y\n```\n")
            assert (fenced.kinds[2], fenced.uncertain[2]) == (blocks.FENCED, False)
        nested = blocks.walk_text(f"a `<?` <![CDATA[ b ?> c{ls}| r |\n]]>\n")
        assert nested.uncertain[:2] == [False, True], nested.uncertain
        # a `>` inside a quoted value does not end the tag
        quoted = blocks.walk_text(f'a <span title="b>c{ls}d">\n\ne\n')
        assert quoted.uncertain[:2] == [False, True], quoted.uncertain
        # `<?>` does not close a processing instruction: the `?` is the opener's
        instruction = blocks.walk_text(f"a <?>{ls}| r |\n?>\n\nd\n")
        assert instruction.uncertain[:2] == [False, True], instruction.uncertain
        # a closer before its opener closes nothing
        early = blocks.walk_text(f"a ?> <? b{ls}| r |\n?>\n\nd\n")
        assert early.uncertain[:2] == [False, True], early.uncertain
        # a `>` inside a single-quoted value does not end the tag either
        single = blocks.walk_text(f"a <span title='b>c{ls}d'>\n\ne\n")
        assert single.uncertain[:2] == [False, True], single.uncertain

    def test_accepts_an_unclosed_fence_at_the_reader_line_it_starts(self):
        """#667 round 1, yellow 1. `walk_text` answers per reader line, and a
        fence opener whose info string holds a U+2028 is one GFM line and two
        reader lines. The opener that never closes is the first of them, the
        one a person can be sent to; the piece after the break opens
        nothing."""
        text = "```" + BREAKS["LS"] + "x\n| a |\n"
        walked = blocks.walk_text(text)
        assert walked.unclosed == [0], walked.unclosed
        assert len(walked.kinds) == len(text.splitlines()) == 3

    def test_where_the_walk_claims_to_be_exact_it_is(self):
        """Half 2, S2. On every line `lib/blocks.py` does not call uncertain,
        over the shapes, the old cases and the generated corpus, the walk hides
        a line exactly where the oracle hides it. Without this half a reader that
        did nothing would pass half 1."""
        wrong = [(lines, bad) for lines in CORPUS if (bad := disagreements(lines))]
        assert not wrong, f"{len(wrong)} documents, the first: {wrong[0]}"


class Test_module:
    @pytest.mark.parametrize("opener", [o for o, _ in INLINE_OPEN_CLOSE[:-1]])
    def test_a_paragraph_left_inside_other_inline_html_is_unsure_to_its_end(
        self, opener
    ):
        """#673's S5, `walk`'s paragraph state. The lines after a line that
        leaves CDATA, a processing instruction, a declaration or a tag open are
        uncertain to the paragraph's end, because the walk does not follow that
        construct's end across lines; a blank line ends it. A `-->` does not end
        it either, where the comment it closes is one the parser never formed."""
        found = blocks.walk([f"a {opener}", "b", "c", "", "d"])
        assert found.uncertain == [False, True, True, False, False], found.uncertain
        past = blocks.walk([f"a {opener}", "b " + CLOSE + " c", "d", "", "e"])
        assert past.uncertain == [False, True, True, False, False], past.uncertain
        fake = blocks.walk(
            ["a `" + OPEN + "` b", "c <? d " + CLOSE + " e", "f", "", "g"]
        )
        assert fake.uncertain == [False, True, True, False, False], fake.uncertain


test_census = census_case(TARGET)

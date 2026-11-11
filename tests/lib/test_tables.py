"""`lib/tables.py`, the GFM table walker, one class per function its cases
reach.

#1454 moved the walker out of `lib/config.py`, which reads the settings as
JSON, and its cases came with it from `tests/lib/test_config.py`. Each
keeps its body, except that it calls the walker as `tables.<name>` and no
longer takes the `config` and `seal` fixtures it did not read. The cases over an earlier release's `| Item | Value |`
table stay as the walker's cases over the table `seal mode` converts, run
under `Test_gfm_table` through `_Old_config_table` and
`_Old_config_shapes`.

#942's phase 6 and its round 9 fix pass had placed in `tests/lib/test_config.py`
three of the walker's cases and the refusal of a line shown directly above
the header from `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py`,
and the case that copies the module without `lib/blocks.py` from
`tests/test_a_script_copied_alone_exits_2.py`, whose `routing.py` row is in
`tests/lib/test_routing.py`.

**`Test_gfm_table` holds the walker to cmark-gfm over an enumerated
corpus** (#647). Over a one-cell header and a two-cell one, the walker is
held to GitHub's renderer, `cmarkgfm`, through `tests/gfm_table_oracle.py`,
and the property is S1 of #647's `frame/design.md`: **on every shape, the
walker's cells equal cmark-gfm's, or the walker refuses.** No shape yields
cells cmark-gfm does not render. #1489's phase 3 moved those cases, the
corpus and the cases that count it here from
`tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py`, which
keeps the oracle's own cases.

**The corpus is enumerated by construction, not from examples.** Round 3 of
#735 found the walk's silent drop (an autolink row) with 21 shapes its author
had not written, after the walk had passed 14 its author had. So the line
kinds of `KINDS` are every block start CommonMark 0.29 lists in section 4
(leaf blocks) and section 5 (container blocks), taken section by section,
with the near misses each section states beside its starts; the GFM
extensions' own line shapes (a table's delimiter and rows, a task list item,
an extended autolink); and the inline shapes a line can open with that read
as a block start to a careless eye (an autolink, an scp-style autolink, `<`
and a space). Each kind is put at every position a table has, and at each of
five indentations, 0-3 spaces and a tab, applied to every line of the kind.
Each header takes its own pass.

What the enumeration leaves out, and why:

  - containers two blocks deep (a list item, a blank line, its indented
    paragraph, then the header): `gfm_table`'s docstring names it as what the
    walker cannot see, because telling it apart needs container nesting;
  - inline markup inside a row's cells (emphasis, a code span, an entity):
    the walker returns a cell's source and the renderer its text, so the two
    differ by design. The rows here are plain, and a cell's content is the
    reader's to judge, not the walk's;
  - a line ending other than LF: `lib/blocks.py#gfm_lines` is where a
    line ends, `tests/lib/test_blocks.py` holds it, and
    `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py` holds its copies
    to it.

`Test_unfenced` holds `unfenced` to `tests/commonmark_oracle.py` over the
corpus `tests/lib/test_blocks.py` builds, half 1 of the property
`tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py` states.
"""

import os
import random
import subprocess
import sys

import commonmark_oracle
import gfm_table_oracle as oracle
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
from test_blocks import CORPUS, as_read

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


HEADERS = {
    # A one-cell table; the header's word is the corpus's, and no reader
    # asks for it.
    "signer": ("Signer",),
    # An earlier release's `seal/config.md` table, read by this walker since
    # #871 and, since #1454, only by `seal mode`'s conversion through
    # `lib/config.py#OLD_TABLE` (`test_the_config_pass_is_the_config_readers_header`).
    "config": ("Item", "Value"),
}

# CommonMark 0.29 section 4.6, HTML block start condition 6: the block-level tag
# names, written out from the specification rather than from the walker.
TYPE_6 = [
    "address",
    "article",
    "aside",
    "base",
    "basefont",
    "blockquote",
    "body",
    "caption",
    "center",
    "col",
    "colgroup",
    "dd",
    "details",
    "dialog",
    "dir",
    "div",
    "dl",
    "dt",
    "fieldset",
    "figcaption",
    "figure",
    "footer",
    "form",
    "frame",
    "frameset",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "head",
    "header",
    "hr",
    "html",
    "iframe",
    "legend",
    "li",
    "link",
    "main",
    "menu",
    "menuitem",
    "nav",
    "noframes",
    "ol",
    "optgroup",
    "option",
    "p",
    "param",
    "section",
    "source",
    "summary",
    "table",
    "tbody",
    "td",
    "tfoot",
    "th",
    "thead",
    "title",
    "tr",
    "track",
    "ul",
]

# Every kind is a list of lines. The comment before each group is the section
# of the specification it is taken from.
KINDS = {
    # section 4.1 thematic breaks, each character, spaced and not, and a near miss.
    "break ***": ["***"],
    "break ---": ["---"],
    "break ___": ["___"],
    "break * * *": ["* * *"],
    "break - - -": ["- - -"],
    "break _ _ _": ["_ _ _"],
    "not a break **": ["**"],
    # section 4.2 ATX headings, the widest and the empty one, and two near misses.
    "heading #": ["# h"],
    "heading ######": ["###### h"],
    "heading, empty": ["#"],
    "not a heading #######": ["####### h"],
    "not a heading #h": ["#h"],
    # section 4.3 setext underlines (`---` is above).
    "setext ===": ["==="],
    "setext =": ["="],
    # section 4.4 indented code, and indented code that holds a container's marker,
    # which four columns make code rather than a container.
    "indented code": ["    code"],
    "indented code, a list marker": ["    - x"],
    "indented code, a quote marker": ["    > q"],
    # section 4.5 fenced code: closed, unclosed, and a backtick info string.
    "fence ```": ["```", "x", "```"],
    "fence ~~~": ["~~~", "x", "~~~"],
    "fence ```, unclosed": ["```"],
    "fence ~~~, unclosed": ["~~~"],
    "not a fence ```a`b": ["```a`b"],
    # section 4.6 HTML blocks, the seven start conditions.
    "html 1 <script>": ["<script>"],
    "html 1 <pre>": ["<pre>"],
    "html 1 <style>": ["<style>"],
    "html 1 <textarea>": ["<textarea>"],
    "html 1 closed": ["<pre>x</pre>"],
    "html 1 over lines": ["<pre>", "x", "</pre>"],
    "html 2 closed": ["<!-- c -->"],
    "html 2 open": ["<!--"],
    "html 2 over lines": ["<!--", "c", "-->"],
    "html 3 closed": ["<? x ?>"],
    "html 3 open": ["<?"],
    "html 4 closed": ["<!DOCTYPE html>"],
    "html 4 open": ["<!X"],
    "html 5 closed": ["<![CDATA[ x ]]>"],
    "html 5 open": ["<![CDATA["],
    **{f"html 6 <{n}>": [f"<{n}>"] for n in TYPE_6},
    **{f"html 6 <{n}": [f"<{n}"] for n in TYPE_6},
    "html 6 </div>": ["</div>"],
    "html 6 <div/>": ["<div/>"],
    # A name CommonMark 0.31 added to condition 6, after cmark-gfm's 0.29.
    "html 6? <search": ["<search"],
    # The near miss condition 6 states: the name must end where a listed
    # name ends, so a longer name a listed one begins is not a block start.
    "not html 6, <divx": ["<divx"],
    "not html 6, <pattern": ["<pattern"],
    "html 7 <span>": ["<span>"],
    "html 7 </span>": ["</span>"],
    'html 7 <a href="x">': ['<a href="x">'],
    "html 7 <a href=x y>": ["<a href=x y>"],
    "html 7 <custom-tag/>": ["<custom-tag/>"],
    "not html 7, text after": ["<span>x</span> y"],
    "not html 7, unfinished": ["<span"],
    "not html 7, unquoted": ['<a href="x"'],
    # What may interrupt a paragraph, which decides whether a line above the
    # header leaves a block open: section 4.6 says the seventh kind may not, and
    # section 5.2 that a list item may only with text after a bullet or the number 1.
    "after a paragraph, html 7": ["text", "<span>"],
    "after a paragraph, html 6": ["text", "<div>"],
    "after a paragraph, list -": ["text", "- x"],
    "after a paragraph, list 1.": ["text", "1. x"],
    "after a paragraph, list 2.": ["text", "2. x"],
    "after a paragraph, list -, empty": ["text", "-"],
    "after a paragraph, quote": ["text", "> q"],
    "after a list item, a break": ["- x", "***"],
    "after a list item, a comment": ["- x", "<!-- c -->"],
    "after a list item, a fence": ["- x", "```", "x", "```"],
    # section 4.7 a link reference definition.
    "link reference": ["[x]: https://example.com"],
    # section 4.8 a paragraph line.
    "paragraph": ["text"],
    # section 4.9 blank lines (the indentation makes the whitespace-only ones).
    "blank": [""],
    # section 5.1 block quotes.
    "quote > q": ["> q"],
    "quote >": [">"],
    "quote >q": [">q"],
    # section 5.2 list items, each marker, the widest number, empty ones, near misses.
    "list -": ["- x"],
    "list +": ["+ x"],
    "list *": ["* x"],
    "list 1.": ["1. x"],
    "list 2)": ["2) x"],
    "list 123456789.": ["123456789. x"],
    "not a list 1234567890.": ["1234567890. x"],
    "list -, empty": ["-"],
    "list 1., empty": ["1."],
    "not a list -x": ["-x"],
    # GFM: a task list item, an extended autolink, a bare URL.
    "task list": ["- [ ] x"],
    "task list, done": ["- [x] x"],
    "extended autolink": ["www.example.com"],
    "bare url": ["https://example.com/org/x"],
    # GFM tables: a delimiter out of place, and rows written wrong.
    "table delimiter": ["|---|"],
    "table row, two cells": ["| x | y |"],
    "table row, no closing pipe": ["| x"],
    "table row, no opening pipe": ["x |"],
    "table row, empty": ["|  |"],
    # Inline shapes a line can open with.
    "autolink": ["<https://example.com/org/x>"],
    "autolink, scp-style": ["<git@example.com:org/x.git>"],
    "autolink, email": ["<x@example.com>"],
    "< and a space": ["< https://example.com/org/x"],
}

INDENTS = ("", " ", "  ", "   ", "\t")
POSITIONS = (
    "before the header",
    "after the header",
    "after the delimiter",
    "between rows",
    "after the last row",
)
CLAUSE = ["", "## Order response shape", "", "x"]


def row(header, n):
    return (
        "| "
        + " | ".join(f"https://example.com/org/r{n}c{c}" for c in range(len(header)))
        + " |"
    )


def document(header, kind_lines, position, indent):
    """The base table -- a header, its delimiter and two rows, then a clause
    -- with KIND_LINES, each indented by INDENT, put at POSITION."""
    head = "| " + " | ".join(header) + " |"
    delimiter = "|" + "---|" * len(header)
    parts = [head, delimiter, row(header, 1), row(header, 2)]
    at = {
        "before the header": 0,
        "after the header": 1,
        "after the delimiter": 2,
        "between rows": 3,
        "after the last row": 4,
    }[position]
    kind = [indent + line for line in kind_lines]
    lines = ["# Pact", "", *parts[:at], *kind, *parts[at:], *CLAUSE]
    return "\n".join(lines) + "\n"


def delimiters(header):
    """Every spelling of HEADER's delimiter row the GFM tables extension
    states: both outer pipes, one, or none, padded or not, aligned or not --
    and, for one column, the bare `---` that is a setext underline instead."""
    n = len(header)
    cells = ["---"] * n
    aligned = [":-:"] * n
    return [
        "|" + "|".join(cells) + "|",
        "| " + " | ".join(cells) + " |",
        "|" + "|".join(aligned) + "|",
        "|" + "|".join(cells),
        "|".join(cells) + "|",
        "|".join(cells),
    ]


def plain(header, indents, delimiter=None):
    """The base table with its header, delimiter and rows indented by
    INDENTS, the indentation axis on the table's own lines (⬜ 22), and the
    delimiter spelled DELIMITER."""
    head = indents[0] + "| " + " | ".join(header) + " |"
    delimiter = indents[1] + (delimiter or "|" + "---|" * len(header))
    rows = [indents[2] + row(header, n) for n in (1, 2)]
    return "\n".join(["# Pact", "", head, delimiter, *rows, *CLAUSE]) + "\n"


def corpus(header):
    """Every document of HEADER's pass, de-duplicated, in a stable order."""
    seen, out = set(), []
    for kind, lines in KINDS.items():
        for position in POSITIONS:
            for indent in INDENTS:
                text = document(header, lines, position, indent)
                if text not in seen:
                    seen.add(text)
                    out.append(((kind, position, indent), text))
    for a in INDENTS:
        for b in INDENTS:
            for c in INDENTS:
                text = plain(header, (a, b, c))
                if text not in seen:
                    seen.add(text)
                    out.append((("plain", a, b, c), text))
    for spelled in delimiters(header):
        text = plain(header, ("", "", ""), spelled)
        if text not in seen:
            seen.add(text)
            out.append((("delimiter", spelled), text))
    return out


def disagreement(header, text):
    """None where the walker agrees with cmark-gfm on TEXT or refuses it;
    otherwise what each said."""
    want = oracle.rows_under(text, header)
    rows, refusals = tables.gfm_table(text, header)
    if refusals:
        return None
    got = [cells for _line, cells in rows]
    if want is not None and got == want:
        return None
    return f"walker {got}, cmark-gfm {want}"


# --- an independent generator (round 1, yellow 5) ---------------------------
#
# The corpus puts one kind at a time at each position; round 1 found the
# walker's line-above mistakes with random documents instead. This is that
# generator, held small and seeded so it runs in a few seconds: documents of
# 2-9 lines drawn from a vocabulary of line kinds and table lines, judged by
# cmark-gfm, a tenth of them with the header indented 1-3 spaces. It tolerates
# no disagreement: the one it used to, a fence `unfenced` hides inside a kind
# 6-7 HTML block, is closed since the walker judges the line above as
# written (round 2, yellow 15).

GENERATOR_SEED = 647
GENERATOR_DOCUMENTS = 3000


def vocabulary(header):
    lines = [ln for kind in KINDS.values() for ln in kind]
    head = "| " + " | ".join(header) + " |"
    delimiter = "|" + "---|" * len(header)
    table = [head, delimiter, row(header, 1), row(header, 2), "| x |", "|---|"]
    return sorted(set(lines)) + table * 6 + ["", "", "", "text"]


def shared_rule():
    """`lib/lines.py`, whose `fence_spans` states the fence delimiter
    rule the table walker's base reading was held to."""
    import importlib.util

    path = os.path.join(ROOT, "lib", "lines.py")
    spec = importlib.util.spec_from_file_location("agentic_lines_for_the_oracle", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


uc = shared_rule()


def walker_base(lines):
    """What the table walker, then in `lib/config.py`, hid at
    `release/v0.16.0`: every line inside a fenced block by the shared
    delimiter rule, a block nobody closed running to the end."""
    out = set()
    for first, last in uc.fence_spans(lines):
        out.update(range(first, len(lines) if last is None else last + 1))
    return out


def leaves_both(new, base, renderer, count):
    """The lines where a reader's answer is neither its base answer nor the
    renderer's: hidden where both show it, or shown where both hide it."""
    return [
        index
        for index in range(count)
        if (index in new) != (index in base) and (index in new) != (index in renderer)
    ]


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

    def test_the_table_walker_never_leaves_both_readings(self):
        """Half 1, S4. On every line of every document, `lib/tables.py` hides
        the line where its base reading hid it or where a renderer hides it, and
        nowhere else: a line it newly hides was never a live row, and a line it
        newly shows was never fenced or commented out."""
        wrong = []
        for doc in CORPUS:
            text, lines = as_read(doc)
            new = {index for index in range(len(lines))} - {
                index for index, _line in tables.unfenced(lines, text)
            }
            bad = leaves_both(
                new,
                walker_base(lines),
                set(commonmark_oracle.hidden_text(text)),
                len(lines),
            )
            if bad:
                wrong.append((lines, bad))
        assert not wrong, f"{len(wrong)} documents, the first: {wrong[0]}"


class Test_gfm_table(_Old_config_table, _Old_config_shapes):
    """`test_an_indented_table_with_no_list_above_is_read` and
    `test_a_list_marker_in_indented_code_is_no_list_item` call `gfm_table`
    alike on documents that differ above the indented header: a list item
    and then a heading in the first, and indented code that holds a list
    marker in the second."""

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

    @pytest.mark.parametrize("which", sorted(HEADERS))
    @pytest.mark.parametrize("kind", sorted(KINDS))
    def test_the_walker_reads_what_cmark_gfm_renders_or_refuses(self, which, kind):
        header = HEADERS[which]
        wrong = []
        for position in POSITIONS:
            for indent in INDENTS:
                text = document(header, KINDS[kind], position, indent)
                said = disagreement(header, text)
                if said:
                    wrong.append(f"{position}, indent {indent!r}: {said}\n{text}")
        assert not wrong, "\n".join(wrong)

    @pytest.mark.parametrize("which", sorted(HEADERS))
    def test_a_table_indented_as_gfm_permits_is_read_and_not_refused(self, which):
        """S3 (⬜ 22 of #735's round 3). Where cmark-gfm renders the table, the
        walker reads it exactly, refusing nothing; where it renders none (a tab
        before the header or the delimiter), the walker refuses."""
        header = HEADERS[which]
        wrong = []
        for a in INDENTS:
            for b in INDENTS:
                for c in INDENTS:
                    text = plain(header, (a, b, c))
                    want = oracle.rows_under(text, header)
                    rows, refusals = tables.gfm_table(text, header)
                    got = [cells for _line, cells in rows]
                    if want is None:
                        ok = bool(refusals)
                    elif c == "\t":
                        # GFM ends the table above a row a tab indents; the walk
                        # refuses that row as one it never reaches.
                        ok = bool(refusals) or got == want
                    else:
                        ok = not refusals and got == want
                    if not ok:
                        wrong.append(
                            f"{(a, b, c)!r}: walker {got} {refusals}, GFM {want}"
                        )
        assert not wrong, "\n".join(wrong)

    @pytest.mark.parametrize("which", sorted(HEADERS))
    def test_every_delimiter_gfm_accepts_is_read(self, which):
        """Every spelling of the delimiter row: where cmark-gfm renders the
        table, the walker reads it exactly and refuses nothing; where it renders
        none (a bare `---` under one column is a setext underline), the walker
        refuses."""
        header = HEADERS[which]
        wrong = []
        for spelled in delimiters(header):
            text = plain(header, ("", "", ""), spelled)
            want = oracle.rows_under(text, header)
            rows, refusals = tables.gfm_table(text, header)
            got = [cells for _line, cells in rows]
            ok = bool(refusals) if want is None else (not refusals and got == want)
            if not ok:
                wrong.append(f"{spelled!r}: walker {got} {refusals}, GFM {want}")
        assert not wrong, "\n".join(wrong)

    def test_the_shapes_round_1_measured_are_refused(self):
        """Round 1's measured shapes, each a table cmark-gfm does not render and
        the walker read: a table directly above, a setext `-` that makes the
        next line a list, a seventh-kind tag after a list item, and an HTML
        block of kinds 1-5 left open across a blank line."""
        u = "https://example.com/org/a"
        opener = "<" + "!-- old list, being retired"
        for text in (
            f"| Name |\n|---|\n| x |\n| Signer |\n|---|\n| {u} |\n",
            f"Intro\n-\n2. second\n| Signer |\n|---|\n| {u} |\n",
            f"1) one\n<a>\n___\n>\n| Signer |\n|---|\n| {u} |\n",
            f"# Pact\n\n{opener}\n\n| Signer |\n|---|\n| {u} |\n",
            f"<pre>\nexample\n\n| Signer |\n|---|\n| {u} |\n",
            f"<?php\n\n| Signer |\n|---|\n| {u} |\n",
            f"<![CDATA[\n\n| Signer |\n|---|\n| {u} |\n",
            f"<!DOCTYPE\n\n| Signer |\n|---|\n| {u} |\n",
        ):
            assert oracle.rows_under(text, ("Signer",)) is None, text
            _rows, refusals = tables.gfm_table(text, ("Signer",))
            assert refusals, text

    def test_an_html_block_closed_above_the_header_leaves_the_table(
        self, oracle_check=True
    ):
        """The other side of the open-block refusal: a kind 1-5 block closed on
        a later line, a blank line, then the table, renders, and is read."""
        u = "https://example.com/org/a"
        for text in (
            f"<pre>\nx\n</pre>\n\n| Signer |\n|---|\n| {u} |\n",
            f"<?php\nx\n?>\n\n| Signer |\n|---|\n| {u} |\n",
        ):
            assert oracle.rows_under(text, ("Signer",)) == [(u,)], text
            rows, refusals = tables.gfm_table(text, ("Signer",))
            assert refusals == [] and [c for _l, c in rows] == [(u,)], text

    @pytest.mark.parametrize("which", sorted(HEADERS))
    def test_random_documents_are_read_as_cmark_gfm_renders_them_or_refused(
        self, which
    ):
        header = HEADERS[which]
        words = vocabulary(header)
        pick = random.Random(f"{GENERATOR_SEED}-{which}")
        head = "| " + " | ".join(header) + " |"
        wrong = []
        for _n in range(GENERATOR_DOCUMENTS):
            lines = [pick.choice(words) for _k in range(pick.randint(2, 9))]
            if head not in lines:
                lines.insert(pick.randint(0, len(lines)), head)
            if pick.random() < 0.1:
                k = lines.index(head)
                lines[k] = " " * pick.randint(1, 3) + head
            text = "\n".join(lines) + "\n"
            said = disagreement(header, text)
            if said:
                wrong.append(f"{said}\n{text}")
        assert not wrong, f"{len(wrong)} disagreements:\n" + "\n".join(wrong[:5])

    def test_round_3s_shapes_are_inside_the_corpus(self):
        """Round 3 of #735 compared 21 shapes and named their kinds; each falls
        inside the enumeration, so they are not listed separately (spec item 1).
        Written here as round 3 wrote them, against the `Signer` header."""
        header = HEADERS["signer"]
        texts = {text for _key, text in corpus(header)}
        named = [
            ("autolink", "after the last row", ""),
            ("autolink, scp-style", "after the last row", ""),
            ("< and a space", "after the last row", ""),
            ("break ***", "after the last row", ""),
            ("break ---", "after the last row", ""),
            ("break ___", "after the last row", ""),
            ("html 6 <div>", "between rows", ""),
            ("list 1.", "between rows", ""),
            ("blank", "between rows", ""),
            ("paragraph", "after the last row", ""),
            ("heading ######", "between rows", ""),
            ("fence ```", "between rows", ""),
            ("html 2 closed", "between rows", ""),
            ("quote > q", "between rows", ""),
            ("list -", "between rows", ""),
            ("table delimiter", "between rows", ""),
            ("table row, two cells", "after the last row", ""),
            ("table row, no closing pipe", "after the last row", ""),
            ("table row, no opening pipe", "after the last row", ""),
            ("table row, empty", "after the last row", ""),
        ]
        for kind, position, indent in named:
            assert document(header, KINDS[kind], position, indent) in texts, kind
        for indents in (
            ("   ", "", ""),
            ("", "   ", ""),
            ("", "", "   "),
            ("", "", "\t"),
        ):
            assert plain(header, indents) in texts, indents

    def test_the_corpus_is_counted(self):
        """The size the phase record states, so a kind that silently stops
        generating shapes is a red case rather than a smaller number nobody
        reads."""
        sizes = {which: len(corpus(header)) for which, header in HEADERS.items()}
        assert sizes == {
            "signer": 5454,
            "config": 5455,
        }, sizes

    def test_the_config_pass_is_the_config_readers_header(self):
        """The config pass is the config table's only where the header it walks
        is the one `seal mode`'s conversion hands the walker (#871, #1454): a
        pass over a header no reader uses would hold nothing. Seen red before
        the header was a name of `lib/config.py`, as an `AttributeError`."""
        assert HEADERS["config"] == config.OLD_TABLE

    @pytest.mark.parametrize(
        "above",
        [
            "<div>\n\n",
            "<pre>x</pre>\n\n",
            "<? x ?>\n\n",
            "<!DOCTYPE html>\n\n",
        ],
        ids=[
            "a kind-6 block a blank line ends",
            "a kind-1 block closed on its own line",
            "a kind-3 block closed on its own line",
            "a kind-4 block closed on its own line",
        ],
    )
    def test_a_table_under_a_block_that_has_ended_is_read(self, above):
        """The refusals reach no further than they must: a blank line ends a
        kind-6 block, and a kind 1-5 block closed on its opening line is closed.
        cmark-gfm renders each table, and the walker reads it."""
        u = "https://example.com/org/a"
        text = f"# Pact\n\n{above}| Signer |\n|---|\n| {u} |\n"
        assert oracle.rows_under(text, ("Signer",)) == [(u,)], text
        rows, refusals = tables.gfm_table(text, ("Signer",))
        assert refusals == [] and [c for _l, c in rows] == [(u,)], (text, refusals)

    @pytest.mark.parametrize(
        "cell",
        ["a \\\\| b", "a \\\\\\\\| b"],
        ids=["two backslashes", "four backslashes"],
    )
    def test_a_pipe_after_an_even_run_of_backslashes_is_refused(self, cell):
        """cmark-gfm reads `\\|` as an escaped pipe wherever it stands, so a pipe
        after an even run of backslashes does not split its cell; `CELL` read
        the backslashes in pairs and split there, and a three-cell row read as
        four (round 1, white 6). Such a row is refused rather than guessed."""
        header = HEADERS["config"]
        text = f"| Item | Value |\n|---|---|\n| {cell} |\n"
        assert oracle.rows_under(text, header) != [("a \\", "b")]
        rows, refusals = tables.gfm_table(text, header)
        assert rows == [] and refusals, (rows, refusals)

    @pytest.mark.parametrize(
        "text",
        [
            "- x\n\n  | Signer |\n|---|\n| {u} |\n",
            "1) one\n\n   | Signer |\n|---|\n| {u} |\n",
            "{c} open\n```\n-->\n- note\n| Signer |\n|---|\n| {u} |\n",
            "<div>\n```\nx\n```\n| Signer |\n|---|\n| {u} |\n",
        ],
        ids=[
            "a header indented into a bullet item",
            "a header indented into an ordered item",
            "a list item hidden under a comment holding a fence",
            "a fence inside a kind-6 block directly above",
        ],
    )
    def test_the_shapes_round_2_measured_are_refused(self, text):
        """Round 2's generator found these read where cmark-gfm renders no
        table: a header indented 1-3 spaces under a list item across a blank
        line, a list item `unfenced` hid under a comment holding a fence, and
        the named kind 6-7 limit, a fence inside an HTML block directly above."""
        text = text.format(u="https://example.com/org/a", c="<" + "!--")
        assert oracle.rows_under(text, ("Signer",)) is None, text
        _rows, refusals = tables.gfm_table(text, ("Signer",))
        assert refusals, text

    def test_an_indented_table_with_no_list_above_is_read(self):
        """The other side of the list-item refusal: an indented header under a
        heading, with no list item since it, renders and is read (S3)."""
        u = "https://example.com/org/a"
        text = f"- x\n\n# Pact\n\n  | Signer |\n|---|\n| {u} |\n"
        assert oracle.rows_under(text, ("Signer",)) == [(u,)], text
        rows, refusals = tables.gfm_table(text, ("Signer",))
        assert refusals == [] and [c for _l, c in rows] == [(u,)], refusals

    def test_a_heading_inside_the_list_item_does_not_end_it(self):
        """A heading indented into the list item is the item's content, not the
        end of the list: an indented header under it is still the item's, and
        cmark-gfm renders no table, so only a heading at the start of a line
        resets the look upward."""
        u = "https://example.com/org/a"
        text = f"- x\n\n  # h\n\n  | Signer |\n|---|\n| {u} |\n"
        assert oracle.rows_under(text, ("Signer",)) is None, text
        _rows, refusals = tables.gfm_table(text, ("Signer",))
        assert refusals and "indented under a list item" in refusals[0], refusals

    def test_a_list_marker_in_indented_code_is_no_list_item(self):
        """`    - x` is indented code, not a list item, so an indented table under
        it renders and is read."""
        u = "https://example.com/org/a"
        text = f"# Pact\n\n    - x\n\n  | Signer |\n|---|\n| {u} |\n"
        assert oracle.rows_under(text, ("Signer",)) == [(u,)], text
        rows, refusals = tables.gfm_table(text, ("Signer",))
        assert refusals == [] and [c for _l, c in rows] == [(u,)], refusals


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

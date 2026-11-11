"""Shared reader: the GFM tables of a markdown file, read as cmark-gfm
renders them.

`gfm_table` reads one table out of a markdown text by its header row's
cells, and `unfenced` and `table_cells` are the fence rule and the cell
split it reads through. Its callers read records and policy documents: the
pact anchor table of a work item's `frame/design.md`
(`skills/verify/scripts/pact_check.py`), a plan's *Judgments of the run*
(`skills/settle/scripts/settle.py`), the row `settle --draft` places
(`skills/settle/scripts/rule_changes.py`) and the lines `seal rules` reads
(`.github/scripts/rules.py`). `seal mode`'s
converter reads an earlier release's `config.md` through it
(`skills/implement/scripts/seal.py#converted`). No setting is read through
it: `lib/config.py` reads `config.json` with the standard library's JSON
parser, and the walker left that module for this one when the settings
left the markdown table (#1454).

What the walker does not read whole it refuses, naming the line, and a line
it hides is a line nothing is read from.
"""

import os
import re
import sys

# `lib/blocks.py` is a sibling, found by this file's own directory, so the
# callers that load this module through `lib/sibling.py` -- `pact_check.py`,
# `seal.py` -- find it too. `lib/routing.py` reaches `optin.py` the same way.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import blocks
except ImportError as missing:
    # A sentence rather than a bare `ModuleNotFoundError`, and an exception
    # rather than an exit, because this is a module other code imports: a
    # script that loads this file catches the error or loads `blocks.py`
    # first, which `lib/sibling.py#load` refuses in its own sentence
    # (`skills/implement/scripts/seal.py`).
    raise ImportError(
        "cannot read "
        + os.path.join(os.path.dirname(os.path.abspath(__file__)), "blocks.py")
        + ", and it is the walk the table walker here reads a table through, "
        "which tells a live row from one quoted in a fence or parked in a "
        "comment. "
        "This file ships beside it under `lib/`; a copy of one taken on its "
        "own is not a plugin"
    ) from missing

# A CELL is any run of characters that are neither a pipe nor a backslash, or
# a backslash followed by anything. The second half is markdown's own escape,
# and the tables this walker reads are markdown: `\|` is how a cell of a
# markdown table carries a literal pipe (#415). A bare pipe is a cell
# boundary, as it is to cmark-gfm.
#
# **This narrows in exactly one shape, and it is not a defect to repair.** A
# backslash standing immediately against a cell-ending pipe is one escaped
# pipe, so `| Broad gate | C:\Users\x\tools\|` is not a row. It cannot be
# both: the escape is what the rest of this comment is for. Nothing becomes
# unwritable, because `table_cells` strips each cell -- a space before the
# closing pipe returns the same value byte for byte. Found by round 1 of
# #415.
#
# `TABLE_ROW` and `CELL_PIPE` below are built on it.
CELL = r"(?:[^|\\]|\\.)"

# The one escape this reader undoes, spelled as the two characters it is.
ESCAPED_PIPE = "\\|"


def unescaped(cell):
    """CELL with markdown's escaped pipe reduced to one literal pipe.

    **Exactly those two characters, and no other backslash is touched.** A
    general unescape -- `re.sub(r"\\\\(.)", r"\\1", cell)` -- turns
    `C:\\Python\\python.exe -m pytest` into `C:Pythonpython.exe -m pytest`,
    and that row reads back with its path intact today, on a repository
    already synced across operating systems. Widening this would break a
    value nobody was asking us to change, to serve an escape markdown only
    needs for the pipe.

    The reduction happens HERE, before any caller sees the value, so a shell
    -- `/bin/sh` or `cmd.exe` -- is handed a plain `|` and never meets the
    backslash at all.
    """
    return cell.replace(ESCAPED_PIPE, "|")


def fence_map(lines, text=None):
    """([(index, line)] outside every fenced block, the index of an opener
    that was never closed or None) -- the one fence rule, computed once.

    `unfenced` below is the generator form the one walk of every table reads
    the file through, and this is the same walk with the state it ENDS in
    kept. A fence that runs to the end of the file is the one thing about a
    fence a caller with somebody to tell has to be able to say, and a second
    fence rule written for that question is the split this module exists to
    prevent.

    Nothing here refuses and nothing acts on the second value. It is a fact
    about the file, for a caller that has somebody to tell, exactly as
    `gfm_table`'s refusals are facts about the table.

    **The lines it hides are `hidden_lines`' below**, which reads the file
    through `lib/blocks.py`'s walk (#667): a closed fence, and now a
    line-start HTML comment block that closes, hide their lines, and a line
    the walk cannot be sure of keeps the reading this function gave it before
    -- the fence rule alone. The name stays because every caller spells it,
    and "outside every fenced block" now means "outside every block this
    reader hides". TEXT is `hidden_lines`' argument of the same name.
    """
    hidden, opened_at = hidden_lines(lines, text)
    shown = [
        (index, raw.rstrip("\r\n"))
        for index, raw in enumerate(lines)
        if index not in hidden
    ]
    return shown, opened_at


def hidden_lines(lines, text=None):
    """({index: "fence" or "comment"} for every line of LINES no walk of the
    table is shown, the index of a fence opener never closed or None).

    A line that declares something is not taken on doubt where the older
    reading would not take it, the second of the three answers
    `docs/checks/the-fold.md` *The fold, and what tells it from a
    deletion* gives: a row this hides is no declaration.

    **TEXT is the file LINES were split from, and every caller that has it
    passes it** (#667 round 1, 🟡 1). The readers split with
    `str.splitlines`, which ends a line at U+2028, NEL, a form feed and five
    more characters where a renderer does not; the walk reads TEXT where
    GFM breaks it (`blocks.walk_text`), so a `<!--` after such a character
    hides nothing. LINES alone is read as given, which is right for a list
    of lines nobody split from a file.

    **Two readings, and every line takes one of them** (#667, #658). Where
    `lib/blocks.py#walk` is sure, the line is hidden exactly where a
    CommonMark renderer hides it: inside a fenced block or a line-start HTML
    comment block that closes. Where the walk is not sure -- a construct
    inside a list item, another kind of HTML block, the lines after inline
    raw HTML a line leaves open (a mid-line `<!--`, CDATA, a processing
    instruction, a declaration or a tag) and a piece of a line that starts
    inside it, everything below a construct that never closes -- the
    line keeps this reader's reading from before #667, the fence rule alone,
    `blocks.fence_only`. So on every line the answer is either the old one or
    the renderer's, and never a third;
    `tests/lib/test_tables.py`'s `Test_unfenced` holds that
    over a generated corpus.

    What it means in a file:

      - a row parked in a comment that closes, above the table or inside it,
        is not a row (`COMMENTED_OLD_ROW`, `COMMENTED_OLD_TABLE`), which is
        the direction this module fails in: *nothing is declared*;
      - a fence line inside such a comment opens no fence, so a header
        comment quoting a fence no longer hides the live table under it;
      - **a fence that is never closed still hides everything below it**,
        because that is what it did before and a line below it is one the
        walk is not sure of, and the second value names that fence;
      - a `<!--` nobody closed hides nothing it did not hide before, and
        switches off no fence below it: it is not a construct at all.

    **The second value** is the fence a caller has somebody to tell about:
    the first opener that never closes, on a line where the walk is not sure
    -- where the old reading, the one that runs such a fence to the end, is
    the one in force. A fence line inside a closed comment opens nothing, so
    it is never named.
    """
    walked = blocks.walk(lines) if text is None else blocks.walk_text(text)
    base, base_opened = blocks.fence_only(lines)
    hidden = walked.hidden(base)
    candidates = list(walked.unclosed)
    if base_opened is not None and walked.uncertain[base_opened]:
        candidates.append(base_opened)
    return hidden, min(candidates) if candidates else None


def unfenced(lines, text=None):
    """(index, line) for each of LINES that is outside every fenced code
    block and every HTML comment block that closes, with the line's own
    ending removed and its index kept. `hidden_lines` below is the rule and
    says which lines those are (#667); this paragraph and the ones after it
    were written for the fence half, and hold for the comment half word for
    word.

    **One fence rule, in front of the one walk of every table.** A line
    inside a fenced code block is not part of any table: not a header, not a
    delimiter row, not a row, and not a line somebody wrote as a row.
    `gfm_table` below reads every table this module reads through this one
    generator, so no two callers disagree about which row is the row (#429).
    A hidden line is a gap the walk ends the table at: a line written
    `| … |` below it is refused as a row the walk never reaches, because GFM
    does not show it as one of the table's rows.

    **Why a table inside a fence is not the table.** A fenced example above
    a live table is a shape a person pastes when documenting the format, and
    before this rule the example's rows were the rows a reader got (#429).

    **It yields positions, not surviving text alone.** `gfm_table` returns
    each row's line, so a helper handing back text could not serve that
    walk.

    **It takes either spelling of a line.** The ending is stripped here, so
    a file written with LF and one written with CRLF get the same answer.

    The edge cases past `frame/design.md`'s rule are resolved toward *not a fence*,
    which is the direction that keeps a live table readable:

      - a BACKTICK fence's info string may not itself hold a backtick
        (CommonMark 4.5), so ``` `x` ``` on its own line opens nothing and is
        an ordinary line of prose here. A tilde fence's info string is
        unrestricted, which is CommonMark's rule and not an exception to this
        one;
      - a closing run may be LONGER than the one that opened the block and
        may carry nothing after it but spaces. A run of the other character,
        or a run carrying an info string, is content inside the block;
      - an unclosed fence runs to the end of the file, so what it swallows
        lands on *nothing is declared* -- the direction everything in this
        module fails in.

    A fence opens wherever its line stands, INCLUDING between two rows of a
    table, because this walk answers a question about the file and not about
    any one caller's state; the table walk reads the gap it leaves as the
    table's end.

    **The walk itself is `fence_map` above**, and this is its surviving lines.
    One walk rather than two: the caller that needs to know whether a fence
    was left open asks that function, and every walk of the table asks this
    one, and neither reads the file by a rule of its own. TEXT is
    `hidden_lines`' argument of the same name.
    """
    yield from fence_map(lines, text)[0]


# --- one GFM table walker (#647) --------------------------------------------
#
# Tables are read out of markdown by name: a record's, and an earlier
# release's `config.md`, which `seal mode` converts. One walker reads them
# all, because two walkers are two break lists to keep in step, and round 3
# of #735 measured exactly that drift in the one there was: an autolink row
# ended the table, and a signer written as one was read by nobody at exit 0.
#
# **It reads what cmark-gfm renders, or refuses.** It is held to the renderer
# by `tests/lib/test_tables.py`'s `Test_gfm_table`, property cases
# over a corpus enumerated from the CommonMark and GFM block kinds: on every
# shape the walker's cells equal cmark-gfm's, or the walker refuses. So every
# arm below is one of two kinds. An END is a line the renderer was measured to
# end the table at; a ROW is a line written `| … |` with the header's width.
# Anything else is refused, with what it is, because a line the renderer reads
# as a row and the walker reads as an end is a row nobody reads.

# A line that ends a GFM table, after at most three spaces of indentation (a
# fourth column is an indented code block, which ends it too). The HTML block
# starts are CommonMark 4.6's seven kinds, measured against cmark-gfm one tag
# name at a time; an autolink, `<https://…>`, is not one of them, and the
# renderer reads it as one of the table's rows.
# exempt from heading_rule: the table walker's table end, held to cmark-gfm
ATX_HEADING = re.compile(r"#{1,6}(?:[ \t]|$)")
THEMATIC_BREAK = re.compile(r"(?:(?:\*[ \t]*){3,}|(?:-[ \t]*){3,}|(?:_[ \t]*){3,})$")
BLOCK_QUOTE = re.compile(r">")
LIST_ITEM = re.compile(r"(?:[-+*]|[0-9]{1,9}[.)])(?:[ \t]|$)")
HTML_KINDS = (
    # 1: a raw-text element, ended by its closing tag.
    (
        re.compile(r"<(?:script|pre|style|textarea)(?:[ \t>]|$)", re.I),
        re.compile(r"</(?:script|pre|style|textarea)>", re.I),
    ),
    # 2-5: a comment, a processing instruction, a declaration, CDATA.
    (re.compile(r"<!--"), re.compile(r"-->")),
    (re.compile(r"<\?"), re.compile(r"\?>")),
    (re.compile(r"<![A-Za-z]"), re.compile(r">")),
    (re.compile(r"<!\[CDATA\["), re.compile(r"\]\]>")),
    # 6: a block-level tag name, open or closing; ended by a blank line.
    (
        re.compile(
            r"</?(?:address|article|aside|base|basefont|blockquote|body|caption"
            r"|center|col|colgroup|dd|details|dialog|dir|div|dl|dt|fieldset"
            r"|figcaption|figure|footer|form|frame|frameset|h1|h2|h3|h4|h5|h6"
            r"|head|header|hr|html|iframe|legend|li|link|main|menu|menuitem"
            r"|nav|noframes|ol|optgroup|option|p|param|section|source|summary"
            r"|table|tbody|td|tfoot|th|thead|title|tr|track|ul)(?:[ \t>]|/>|$)",
            re.I,
        ),
        None,
    ),
    # 7: any other whole open or closing tag alone on its line.
    (
        re.compile(
            r"(?:<[A-Za-z][A-Za-z0-9-]*"
            r"(?:[ \t]+[A-Za-z_:][A-Za-z0-9_.:-]*"
            r"(?:[ \t]*=[ \t]*(?:[^ \t\"'=<>`]+|'[^'\n]*'|\"[^\"\n]*\"))?)*"
            r"[ \t]*/?>|</[A-Za-z][A-Za-z0-9-]*[ \t]*>)[ \t]*$"
        ),
        None,
    ),
)
# A delimiter row: one `:?-+:?` per cell, a pipe somewhere in it (a bare `---`
# under a line is a setext heading, and GFM renders no table there), at most
# three spaces of indentation and no tab before it.
DELIMITER_ROW = re.compile(
    r"^ {0,3}\|?[ \t]*:?-+:?[ \t]*(?:\|[ \t]*:?-+:?[ \t]*)*\|?[ \t]*$"
)
# A row written `| … |`, at most three spaces in; its cells are split by
# every pipe `CELL` does not hold, so an escaped pipe stays inside its cell.
TABLE_ROW = re.compile(rf"^ {{0,3}}\|(?P<cells>(?:{CELL}|\|)*)\|[ \t]*$")
CELL_PIPE = re.compile(rf"((?:{CELL})*)(\|?)")
# A pipe after an even run of backslashes: `CELL` reads the backslashes in
# pairs and splits there, and cmark-gfm does not, because its cell scanner
# reads `\|` as an escaped pipe wherever it stands (round 1 of PR #749,
# white 6). A line holding one is no row this walker reads.
EVEN_ESCAPED_PIPE = re.compile(r"(?<!\\)(?:\\\\)+\|")


def table_cells(line):
    """The cells of LINE as a tuple, each stripped and with `\\|` reduced to a
    pipe, where LINE is written `| … |`; otherwise None, which is also the
    answer for a line holding a pipe after an even run of backslashes, which
    cmark-gfm splits differently (`EVEN_ESCAPED_PIPE`)."""
    match = TABLE_ROW.match(line)
    if not match or EVEN_ESCAPED_PIPE.search(line):
        return None
    cells = []
    for piece in CELL_PIPE.finditer(match.group("cells")):
        cells.append(unescaped(piece.group(1).strip()))
        if not piece.group(2):
            break
    return tuple(cells)


def html_start(content):
    """`(kind, end)` for the HTML block CONTENT begins -- CONTENT being the
    line past its indentation -- where `kind` is CommonMark 4.6's condition
    number and `end` the pattern that ends the block, None for the two kinds
    a blank line ends; `(None, None)` where CONTENT begins none."""
    for number, (start, end) in enumerate(HTML_KINDS, 1):
        if start.match(content):
            return number, end
    return None, None


def table_end(line):
    """Why LINE ends a GFM table above it, or None where cmark-gfm reads it as
    one of the table's rows (or the walker cannot say which, and refuses)."""
    if not line.strip():
        return "a blank line"
    if blocks.columns(line) >= 4:
        return "an indented code block"
    content = line.lstrip(" ")
    if ATX_HEADING.match(content):
        return "a heading"
    if THEMATIC_BREAK.match(content):
        return "a thematic break"
    if BLOCK_QUOTE.match(content):
        return "a block quote"
    if LIST_ITEM.match(content):
        return "a list item"
    if html_start(content)[0]:
        return "an HTML block"
    return None


def raw_html_open(lines):
    """True where an HTML block of CommonMark 4.6's kinds 1-5 -- the kinds no
    blank line ends -- is still open after LINES, so everything under it is
    the block's raw text and GFM renders no table there (round 1 of PR
    #749, yellow 5)."""
    end = None
    for line in lines:
        if end is not None:
            if end.search(line):
                end = None
            continue
        if blocks.columns(line) >= 4:
            continue
        content = line.lstrip(" ")
        number, closer = html_start(content)
        if number is not None and number <= 5 and not closer.search(content, 1):
            end = closer
    return end is not None


def a_list_above(lines):
    """True where a list item stands in LINES since the last heading or
    thematic break at the start of a line, so an indented header under it
    can be more of that item: a blank line does not end a list item, and the
    header's indent decides (round 2 of PR #749, yellow 15). The two
    patterns are matched on the line as written, so a heading indented into
    an item is the item's content and resets nothing."""
    seen = False
    for line in lines:
        if blocks.columns(line) >= 4:
            continue
        content = line.lstrip(" ")
        if ATX_HEADING.match(line) or THEMATIC_BREAK.match(line):
            seen = False
        elif LIST_ITEM.match(content):
            seen = True
    return seen


# Where GFM ends a line: LF, CR and CRLF, and nowhere else.
GFM_LINE_ENDS = ("\r\n", "\n", "\r")


def gfm_line_starts(text):
    """One bool per `text.splitlines()` piece: whether that piece begins a
    line GFM begins. `str.splitlines` also ends a line at eight characters
    GFM reads as part of the line -- a form feed, U+2028 and six more -- so
    a piece after one of them is more of the GFM line above it."""
    # exempt from splitlines: the walk's own pieces, each asked if it starts a line
    pieces = text.splitlines(keepends=True)
    return [
        at == 0 or pieces[at - 1].endswith(GFM_LINE_ENDS) for at in range(len(pieces))
    ]


def opens_table(index, line, under):
    """True where LINE, at INDEX, is the header of a table of its own:
    written `| … |`, with UNDER, `[(index, line)]` for the next shown line or
    `[]`, a delimiter row of the header's width directly below it.

    What stands above it is not asked. The caller does not read that table,
    so taking one GFM would not render costs it nothing, and a second header
    of the caller's own table is named by the caller's header scan
    (`pact_check.py#first_table`) wherever it stands. Asking for a blank
    line refused a table GitHub renders under a sentence or a thematic break
    (round 2 of #913, finding 1)."""
    cells = table_cells(line)
    if cells is None or not under:
        return False
    below, row = under[0]
    return (
        below == index + 1
        and "|" in row
        and DELIMITER_ROW.match(row) is not None
        and row.strip().strip("|").count("|") + 1 == len(cells)
    )


def gfm_table(text, header, beside=False):
    """(rows, refusals) for the first GFM table in TEXT whose header row's
    cells are HEADER, a tuple of names.

      rows      [(line number, cells)] for every body row read, each cells a
                tuple as wide as HEADER, in order
      refusals  one sentence per thing that stopped the walk, naming it

    **The walk reads `str.splitlines` pieces, and a piece is a line only
    where it begins a GFM line** (`gfm_line_starts`). A header or delimiter
    piece that does not is no table GitHub renders, and the walk refuses the
    table; a body piece that does not is more of the row above it, and the
    walk stops there and refuses it; after the table's end such a piece is
    no heading, so the walk goes on past it, and one written `| … |` is
    refused like any other row nobody reads.

    A header is a line written `| a | b |`, at most three spaces in; the line
    under it must be a delimiter row of the same width. Each line after that
    is one of three things, and the walk takes none of them on guesswork:

      an end       a blank line, a gap (`unfenced` hid a fence or a comment
                   block there), a heading, a thematic break, a block quote,
                   a list item, an HTML block, or a line four columns in. GFM
                   ends the table there; a line written `| … |` after it and
                   before the next heading is a row nobody reads, and is
                   refused, except where BESIDE is true and that line opens
                   a table of its own (`opens_table`): the walk steps over
                   that table, its delimiter row and every line under it up
                   to its end, and goes on refusing a `| … |` line after it.
                   A caller whose file holds one table, an old `config.md`,
                   leaves BESIDE false; the anchor table's reader sets it,
                   because a frame's section holds other tables
      a row        written `| … |` with the header's width
      anything     refused, saying what it is: a delimiter row out of place,
        else       a row of another width or without its outer pipes, or a
                   line with no pipe, which GFM reads as one of the rows

    **A header with a line directly above it is refused**, with the
    blank-line remedy, whether or not `unfenced` hides that line, because
    whether GFM renders a table there depends on block state no reader here
    tracks -- a paragraph, a list item's lazy paragraph, a table above, a
    setext underline, an HTML block, a fence inside one -- and the first
    walker, which mirrored those rules line by line, read tables GFM does not
    render (round 1 of PR #749, yellow 5; round 2, yellow 15). Judging
    the line as written closes the limit this docstring used to name, a
    fence `unfenced` hides inside an HTML block of kinds 6 and 7, because a
    header inside such a block always has a non-blank line above it. So is a
    header indented under a list item since the last heading or thematic
    break (`a_list_above`), which a blank line does not end -- the shape the
    list-item limit named here, `- x`, a blank line, then the header, is now
    refused -- and a header under an HTML block of kinds 1-5 left open above
    it (`raw_html_open`), which no blank line ends. **What this cannot see**
    is block state none of those three carries; round 2's generator found
    none over 600,000 documents.

    Each refusal reads after a noun naming the file, as `seal pact` prints
    the anchor table's after "the frame ".
    """
    name = " | ".join(header)
    width = len(header)
    shape = "a one-cell row" if width == 1 else f"a {width}-cell row"
    written = "`|" + " … |" * width + "`"
    # exempt from splitlines: lines the GFM walk numbers
    lines = text.splitlines()
    shown = list(unfenced(lines, text))
    at = next(
        (k for k, (_i, line) in enumerate(shown) if table_cells(line) == header),
        None,
    )
    if at is None:
        return [], [f"holds no `| {name} |` table"]
    head_index = shown[at][0]
    # The line as written, hidden or not: a line `unfenced` hides directly
    # above the header is a line GFM may read the header into -- a fence
    # inside an HTML block of kinds 6-7, or a list item the fence-only reading
    # hid (round 2 of PR #749, yellow 15).
    above = lines[head_index - 1] if head_index > 0 else ""
    if shown[at][1][:1] == " " and a_list_above([ln for _i, ln in shown[:at]]):
        return [], [
            f"has a `| {name} |` header indented under a list item, which GFM "
            "reads as more of that item where the indent reaches its text — "
            "write the header at the start of its line"
        ]
    if above.strip():
        return [], [
            f"has a `| {name} |` header directly under `{above.strip()}`, "
            "and GFM renders a table under a line only in some of the shapes "
            "that line can take — leave a blank line above the header"
        ]
    if raw_html_open([line for _i, line in shown[:at]]):
        return [], [
            f"has a `| {name} |` header inside an HTML block opened above it "
            "and never closed, so GFM renders no table there — close the block"
        ]
    delimiter = shown[at + 1] if at + 1 < len(shown) else None
    if (
        delimiter is None
        or delimiter[0] != head_index + 1
        or not DELIMITER_ROW.match(delimiter[1])
        or "|" not in delimiter[1]
    ):
        return [], [
            f"has a `| {name} |` header with no delimiter row under it, so "
            "GFM renders no table there"
        ]
    cells = delimiter[1].strip().strip("|").count("|") + 1
    if cells != width:
        return [], [
            f"has a `| {name} |` header over a delimiter row of {cells} "
            "cells, so GFM renders no table there"
        ]
    begins = gfm_line_starts(text)
    if not (begins[head_index] and begins[delimiter[0]]):
        return [], [
            f"has a `| {name} |` header that shares a line with the line beside "
            "it to GFM: a form feed, U+2028 or another character only Python "
            "ends a line at stands between them, so GitHub renders no table "
            "there — put the header and its delimiter row each on a line of "
            "its own"
        ]
    rows, stray, ended, previous = [], None, False, delimiter[0]
    body = shown[at + 2 :]
    # BESIDE: the index of the last line read as part of a table of its own.
    other = None
    for k, (index, line) in enumerate(body):
        if not ended and (index != previous + 1 or table_end(line)):
            ended = True
        if ended:
            if (
                begins[index]
                and ATX_HEADING.match(line.lstrip(" "))
                and blocks.columns(line) < 4
            ):
                break
            if other is not None and index == other + 1 and not table_end(line):
                # The other table's delimiter row, or a line GFM reads as
                # one of its rows.
                other = index
                continue
            if line.lstrip().startswith("|"):
                if beside and opens_table(index, line, body[k + 1 : k + 2]):
                    # A table of its own, which GFM renders apart from this
                    # one: the walk steps over it and goes on to the heading.
                    other = index
                    continue
                stray = (
                    f"has a `{name}` table that ends above `{line.strip()}`, "
                    "a row the walk never reaches — it and every row below it "
                    "would go unread"
                )
                break
            continue
        previous = index
        if not begins[index]:
            stray = (
                f"has a `{name}` table that stops at `{line.strip()}`, which is "
                "not a row of its own to GFM: a form feed, U+2028 or another "
                "character only Python ends a line at stands before it, so "
                "GitHub reads it as more of the line above — put it on a line "
                "of its own"
            )
            break
        if DELIMITER_ROW.match(line):
            stray = _stops_at(name, line, "a delimiter row out of place")
            break
        found = table_cells(line)
        if found is not None and len(found) == width:
            rows.append((index + 1, found))
            continue
        if "|" in line:
            stray = _stops_at(name, line, f"which is not {shape} written {written}")
        else:
            stray = (
                f"has a `{name}` table that continues with `{line.strip()}`, "
                "a line with no pipe that GFM reads as one of its rows — write "
                f"it as {written}"
            )
        break
    return rows, [stray] if stray is not None else []


def _stops_at(name, line, why):
    return (
        f"has a `{name}` table that stops at `{line.strip()}`, {why} — every "
        "row below it would go unread"
    )

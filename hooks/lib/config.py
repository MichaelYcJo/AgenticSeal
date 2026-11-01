"""Shared reader: what does this repository say about itself?

`config.md` sits in the root `hooks/lib/optin.py` resolves, in the same shape as
`parity.md` -- a markdown table of `| Item | Value |`. Every row in it is
optional and every absent row has a default, which is what every repository
got before that row existed.

`Mode` is the exception that proves it, and it is why this module exists. What
every repository got before that row was *the folder decides*, which is not a
value, so an absent one has no default at all -- it is filled in from where the
folder actually is, by `seal mode`. Until somebody runs that command, a root
exists that nobody chose a mode for, and #151 is what that costs: a monorepo
was opted into shared mode, with its review records committed, without the
question ever being put to anyone.

Two callers need the row and they need the SAME answer.
`skills/implement/scripts/seal.py` writes it, and `hooks/mode-gate.py` reads it
to decide whether the question still has to be asked. A file that one of them
parses and the other does not is a gate that stays quiet about a row the
command believes it wrote. The parser lived in `seal.py`, which is a
two-thousand-line command that a `PreToolUse` hook must not import -- so the
READER moved here and the writer stayed there, and `seal.py` re-exports these
names rather than keeping a second copy.

**Not in `optin.py`, deliberately.** That module's docstring says there is no
config key and everything in it fails toward *not opted in*; the root's
existence is the opt-in and `docs/one-root-by-lifetime.md` *The opt-in signal
is the root itself* is the clause. The `Mode` row decides nothing about opting
in -- it RECORDS an answer -- and putting it in that module would read as the
clause being softened.

Everything here fails toward "nothing is declared" -- except where a written
row would be read as absent. A file that is there and cannot be read, a row
written twice, and an item the table walker did not read because it refused
a line above it are refused by `config_text` and `config_value` rather than
read as nothing (#867, #871); a hook reads a refusal as nothing it can act on
and says nothing, and a command prints it and exits 2. `config_text`'s
docstring says which caller is which kind. The table is read by
`gfm_table`, the walker held to cmark-gfm, through `config_table`.
"""

import os
import re
import sys

# `hooks/lib/blocks.py` is a sibling, found by this file's own directory, so the
# callers that load this module by path -- `broad_gate.py#load`, `seal.py` --
# find it too. `hooks/lib/routing.py` reaches `optin.py` the same way.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import blocks
except ImportError as missing:
    # A sentence rather than a bare `ModuleNotFoundError`, and an exception
    # rather than an exit, because this is a module other code imports: a
    # `PreToolUse` gate that raises is skipped for that call and said at the
    # end of the turn (`hooks/dispatch.py`, #28), and a script that loads this
    # file by path catches the error or names the file first
    # (`skills/implement/scripts/seal.py#HOOK_PURPOSES`).
    raise ImportError(
        "cannot read "
        + os.path.join(os.path.dirname(os.path.abspath(__file__)), "blocks.py")
        + ", and it is the walk this reader reads config.md through, which "
        "tells a live row from one quoted in a fence or parked in a comment. "
        "This file ships beside it under `hooks/`; a copy of one taken on its "
        "own is not a plugin"
    ) from missing

CONFIG = "config.md"
ROW_ITEM = "Mode"

# The two modes, spelled the way every document in this repository spells
# them. Read case-insensitively, written lowercase.
LOCAL, SHARED = "local", "shared"
MODES = (LOCAL, SHARED)

# The `| Item | Value |` table's header, as the cells `gfm_table` matches a
# header by (#871). The table has no grammar of its own: it is read by the
# walker cmark-gfm holds, which is handed this tuple and nothing else.
CONFIG_TABLE = ("Item", "Value")

# A CELL is any run of characters that are neither a pipe nor a backslash, or
# a backslash followed by anything. The second half is markdown's own escape,
# and this file is markdown: `\|` is how a cell of a markdown table carries a
# literal pipe, and `templates/setup/config.md` already writes its own cells that
# way (#415). A bare pipe is a cell boundary, as it is to cmark-gfm.
#
# **This narrows in exactly one shape, and it is not a defect to repair.** A
# backslash standing immediately against a cell-ending pipe is one escaped
# pipe, so `| Broad gate | C:\Users\x\tools\|` is not a row. It cannot be
# both: the escape is what the rest of this comment is for. Nothing becomes
# unwritable, because `table_cells` strips each cell -- a space before the
# closing pipe returns the same value byte for byte. Found by round 1 of
# #415.
#
# `TABLE_ROW`, `CELL_PIPE` and `FIRST_CELL` below are built on it.
CELL = r"(?:[^|\\]|\\.)"

# A fenced code block's delimiter line, as CommonMark spells one: up to three
# spaces of indentation, then a run of three or more backticks or three or
# more tildes, then the info string. Four or more spaces is an indented code
# block instead and never a fence, which is why the bound is written into the
# pattern rather than checked after it.
#
# **Three or more, and tildes as well as backticks, is a decision with
# grounds.** This repository's own records wrap a fenced example in FOUR
# backticks -- #429's body and `trail/rounds/round-3-report.md` both do -- and that
# is exactly the text somebody would paste into `config.md` to document the
# format. A rule that knew three backticks only would read the inner fence as
# the outer one's close and leave the live table inside a fence.
#
# The pattern lives in `hooks/lib/blocks.py` since #667, which the routing reader
# reads as well; this name is that one.
FENCE = blocks.FENCE

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


def config_path(home):
    return os.path.join(home, CONFIG)


def fence_map(lines, text=None):
    """([(index, line)] outside every fenced block, the index of an opener
    that was never closed or None) -- the one fence rule, computed once.

    `unfenced` below is the generator form the one walk of every table reads
    the file through, and this is the same walk with the state it ENDS in
    kept. A fence
    that runs to the end of the file is the one thing about a fence a caller
    with somebody to tell has to be able to say: `seal gate` quoting a live
    `| Broad gate |` row back as *written inside a code fence* and telling the
    person to move it into a table it is already in is a true sentence about a
    cause that is not the real one, which is the failure #429 was opened about
    arriving one shape over. A second fence rule written for that question is
    the split this module exists to prevent.

    Nothing here refuses and nothing acts on the second value. It is a fact
    about the file, for the one caller that has somebody to tell --
    `skills/verify/scripts/broad_gate.py#fence_left_open` -- exactly as
    `config_table`'s refusals are facts about the table for the same caller.

    **The lines it hides are `hidden_lines`' below**, which reads the file
    through `hooks/lib/blocks.py`'s walk (#667): a closed fence, and now a
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
    `docs/the-record-layout.md` *The fold, and what tells it from a
    deletion* gives: a row this hides is no declaration, so a hook says
    nothing and a gate asks, and `seal gate` names a fence left open.

    **TEXT is the file LINES were split from, and every caller that has it
    passes it** (#667 round 1, 🟡 1). The readers split with
    `str.splitlines`, which ends a line at U+2028, NEL, a form feed and five
    more characters where a renderer does not; the walk reads TEXT where
    GFM breaks it (`blocks.walk_text`), so a `<!--` after such a character
    hides nothing. LINES alone is read as given, which is right for a list
    of lines nobody split from a file.

    **Two readings, and every line takes one of them** (#667, #658). Where
    `hooks/lib/blocks.py#walk` is sure, the line is hidden exactly where a
    CommonMark renderer hides it: inside a fenced block or a line-start HTML
    comment block that closes. Where the walk is not sure -- a construct
    inside a list item, another kind of HTML block, the lines after inline
    raw HTML a line leaves open (a mid-line `<!--`, CDATA, a processing
    instruction, a declaration or a tag) and a piece of a line that starts
    inside it, everything below a construct that never closes -- the
    line keeps this reader's reading from before #667, the fence rule alone,
    `blocks.fence_only`. So on every line the answer is either the old one or
    the renderer's, and never a third;
    `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py` holds that
    over a generated corpus.

    What it means in a file:

      - a row parked in a comment that closes, above the table or inside it,
        is not a row (`COMMENTED_OLD_ROW`, `COMMENTED_OLD_TABLE`), which is
        the direction this module fails in: *nothing is declared*;
      - a fence line inside such a comment opens no fence, so a header
        comment quoting a fence no longer hides the live table under it;
      - **a fence that is never closed still hides everything below it**,
        because that is what it did before and a line below it is one the
        walk is not sure of. `seal gate` names that fence
        (`broad_gate.py#fence_left_open`), and `seal mode` asks again;
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
    generator -- the `| Item | Value |` table through `config_table`, and the
    pact's three -- and `skills/implement/scripts/seal.py#with_row`, the
    WRITER, overwrites the line `config_table` names, so the reader and the
    writer cannot disagree about which row is the row: the file two rows
    deep that no command can bring into agreement (#429). A hidden line is
    a gap the walk ends the table at: a line written `| … |` below it is
    refused as a row the walk never reaches, because GFM does not show it as
    one of the table's rows.

    **Why a table inside a fence is not the table.** `config.md`'s header
    comment points its reader at `templates/setup/config.md`, a document of EXAMPLE
    tables, and `skills/config/SKILL.md` *Procedure* step 3 tells a session
    to copy a block of that template -- one holding a fenced
    `| Broad gate | ... |` row -- into the repository's own file, naming no
    position for it. So a fenced example above the live table, or above a
    table that has no parseable row yet, is a shape this plugin's own
    documented procedure produces; before this rule the example's rows were
    the rows every gate got, and the broad run ran a command nobody
    chose.

    **It yields positions, not surviving text alone.** `gfm_table` returns
    each row's line, `config_table` hands that index on, and `with_row`
    overwrites the line at it, so a helper handing back text could not serve
    that walk, and a second fence rule written for the writer is the split
    this module exists to prevent.

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
        module fails in, and loud where it matters: `seal gate` exits 2 with
        a message and `seal mode` asks the mode question.

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


def config_table(text):
    """(rows, refusals) for the `| Item | Value |` table of TEXT -- the one
    walk of `seal/config.md`, which is `gfm_table`'s (#871).

      rows      [(index, item, value)] for every row the walk read, in order:
                INDEX is the row's line in `text.splitlines()`, and ITEM and
                VALUE are the cells as `table_cells` returns them, stripped
                and with `\\|` reduced to one literal pipe
      refusals  the walker's sentences for what stopped it, each reading
                after a noun naming the file; [] where nothing did

    **A text holding no such table is `([], [])`**: no table declares
    nothing, everywhere, as no file does. A header the walker refuses -- a
    line directly above it, no delimiter row under it, a delimiter row of
    another width -- is a table, refused, and every item of it is a refusal.

    **The table has no grammar of its own.** It is read by the walker the
    pact's tables are read by, held to cmark-gfm over an enumerated corpus:
    a row is a row where the renderer shows it as one, or the walk refuses
    -- naming the line it stopped at and the edit -- and never steps past a
    line to read on below it, so no row is read under a line it refused.

    **A row is a row only where it, the header and the delimiter row each
    begin a line GFM begins** -- the walker's rule, `gfm_line_starts`. A row
    piece after a form feed, U+2028 or another character only Python ends a
    line at is the tail of the row above it, which GitHub shows cut off at
    its cells, so the walk stops there and refuses it, and the row above
    keeps the value GitHub shows. A header or delimiter piece after one is
    no table GitHub renders, so the walk refuses the table and reads no row.

    What a caller does with a refusal is its own kind's, as `config_text`
    says: a hook says nothing, and a command prints the sentence and exits 2
    for the items the walk did not read. `config_value` is the per-item
    answer, and a caller holding these rows asks `value_of` of them and acts
    on the refusals by its own kind."""
    rows, refusals = gfm_table(text, CONFIG_TABLE)
    if refusals and refusals[0].startswith("holds no "):
        return [], []
    return [(line - 1, item, value) for line, (item, value) in rows], refusals


def config_rows(text):
    """Every `| Item | Value |` row the walk read, as (item, value), in order
    -- `config_table`'s rows without their places or its refusals.

    **Rows alone are not an answer about an item**: a row the walk did not
    read is absent from this list whether the table ended or the walk
    refused the line, and only `config_table`'s refusals tell the two apart. A caller asking for
    one item asks `config_value`; a caller holding these rows asks
    `config_table` for the refusals (#871).

    Each cell comes back with `\\|` reduced to one literal pipe and nothing
    else changed; `unescaped` above says why it is those two characters
    alone. A line inside a code fence or a closed comment is not shown to the
    walk at all (`unfenced`), so an example table pasted above the live one
    is not this reader's table (#429).

    **The shapes the walker refuses, each with its one edit** — the list
    `templates/setup/config.md` and `skills/config/SKILL.md` give a person, kept
    beside the reader so the three say one thing:

      - a line directly above the header — a comment, prose, a row: leave a
        blank line above the header;
      - no delimiter row under the header, or one of another width: write
        `|---|---|` under it;
      - a bare pipe in a value, which GitHub shows cut off at the pipe:
        write it `\\|`;
      - a third cell, a stray delimiter row or prose inside the table:
        write it as `| … | … |`, or take it out;
      - a row under a comment, a fence or a blank line that ends the table:
        move it into the table; where it heads a table of something else,
        put a heading between the two tables;
      - a row, the header or the delimiter row after a form feed or U+2028
        on another line of the table: put it on a line of its own.

    Every row below the refused line is a refusal to `config_value`, never
    an absent row; the rows above it are read."""
    return [(item, value) for _index, item, value in config_table(text)[0]]


def config_text(home):
    """(text, refusal) for `<home>/config.md` — the one place the file is
    opened, and the one place an absent file is told from an unreadable one.

      (None, None)     there is no file at that name: nothing is declared
      (text, None)     the file, read as UTF-8
      (None, refusal)  the file is there and cannot be read as text -- a
                       directory of that name, a permission this process
                       does not have, bytes that do not decode -- and
                       REFUSAL is a sentence naming the path and why

    **Two states, and only the second is refused** (#867). An absent file is
    what every repository had before it wrote a row, so it declares nothing,
    everywhere. A file that is there and will not read is not a repository
    that answered nothing: it is one whose answer nobody can read. What a
    caller does with that is its own kind's call, and every caller asks this
    reader rather than opening the file a second time to find out:

      - a hook that may not stop -- `hooks/mode-gate.py` -- reads a refusal
        as nothing it can act on and says nothing, because a gate that
        refuses wrongly is an outage nobody can get past (`CONTRIBUTING.md`
        *What a change to a gate must carry*);
      - a command a person runs prints the sentence and exits 2 with nothing
        judged, because a command that reads a written row as absent acts as
        if the person had written none.

    HOME is the seal root; a falsy one is no file. A name that `lexists` but
    will not open -- a symbolic link to nowhere -- is the second state: the
    name is there.
    """
    if not home:
        return None, None
    path = config_path(home)
    if not os.path.lexists(path):
        return None, None
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read(), None
    except (OSError, ValueError) as exc:
        return None, unreadable_config(path, exc)


def unreadable_config(path, exc):
    """The sentence `config_text` refuses an unreadable PATH in. It opens
    with the path and ends with no full stop, so it reads after a command's
    own prefix."""
    why = exc.strerror if isinstance(exc, OSError) and exc.strerror else str(exc)
    return (
        f"{path} is there and cannot be read as UTF-8 text ({why}), so no row "
        "of it can be read — a config that is absent declares nothing, and "
        "one that will not read is refused rather than read as absent"
    )


def doubled_row(item, count):
    """The sentence `config_value` refuses a row written COUNT times in, the
    one sentence for every item."""
    return f"`{item}` appears {count} times — one value"


def config_value(text, item):
    """(value, refusal) for ITEM in the `| Item | Value |` table of TEXT —
    the one answer every reader of one config row gives (#867, #871).

      (None, None)     no row names ITEM in a table the walk read whole, or
                       TEXT holds no such table, or TEXT is None (no file)
      (value, None)    one row the walk read: its value, stripped and
                       unescaped as `config_rows` returns it, "" where empty
      (None, refusal)  ITEM is written more than once, and REFUSAL says so;
                       or the walk refused the table and did not read ITEM,
                       and REFUSAL is the walker's first sentence, naming the
                       line it stopped at and the edit

    **A refusal is per item, never an absent row** (#871). A row the walk
    read before it stopped is a row GitHub shows, so it is a value, and a
    `Mode` row above a malformed line keeps the mode gate quiet as it did.
    An item the walk did not read may be written below the line it stopped
    at, so it has no value and is not absent either: it is the walker's
    sentence, which a hook reads as nothing it can act on and a command
    prints. Refusing the whole table would turn every item off for a line
    that is not theirs; reading the item as absent is the silent default
    #415 was opened about.

    **A row written twice has no value**, not its first and not its last:
    its first row is not the answer. Readers that took the first, a checker
    that took the last and a writer that wrote the first are three answers
    to one file, which is a file a person edits on the row they see while
    another one answers. So the one answer is a refusal, and what a caller
    does with it is its own kind's -- `config_text` says which kind does
    which.

    The rows are `config_table`'s, so a row is a row only where that walk
    reads it: one in a fence or in a closed comment is not counted, which is
    what keeps a fenced example from doubling the live row. **In a table the
    walk refused, a line written below its last row and above the next
    heading that names ITEM in its first cell counts too**: the walk did not
    read it, so it is not a value, but it is an answer somebody wrote, and a
    row read above it is then one of two answers and has no value either. A
    table under the next heading is another table's, which the walk's own
    rows nobody reads stop at as well."""
    if text is None:
        return None, None
    rows, refusals = config_table(text)
    value, refusal = value_of([(found, v) for _i, found, v in rows], item)
    if value is None and refusal is None and refusals:
        return None, refusals[0]
    if value is not None and refusals:
        below = rows_named_below(text, rows[-1][0], item)
        if below:
            return None, doubled_row(item, 1 + below)
    return value, refusal


# A line's first cell as a person wrote it, read up to the first pipe no
# backslash escapes, at most three spaces in: how `config_value` tells that a
# line the walk did not read names an item.
FIRST_CELL = re.compile(rf"^ {{0,3}}\|((?:{CELL})*)\|")


def rows_named_below(text, index, item):
    """How many lines of TEXT below the line at INDEX and above the next
    heading, of those the walk is shown, name ITEM in their first cell --
    the stretch `gfm_table` calls rows nobody reads. A piece is a line here
    only where it begins a GFM line (`gfm_line_starts`), as it is to the
    walk."""
    begins = gfm_line_starts(text)
    count = 0
    # exempt from splitlines: lines the GFM walk numbers
    for at, line in unfenced(text.splitlines(), text):
        if at <= index or not begins[at]:
            continue
        if ATX_HEADING.match(line.lstrip(" ")) and blocks.columns(line) < 4:
            break
        first = FIRST_CELL.match(line)
        if first and unescaped(first.group(1).strip()) == item:
            count += 1
    return count


def value_of(rows, item):
    """`config_value` over ROWS already walked, as `(item, value)` pairs --
    the rule itself, for a caller that holds the rows and would otherwise
    walk the file once per item (`pact_declaration`)."""
    values = [value for found, value in rows if found == item]
    if len(values) > 1:
        return None, doubled_row(item, len(values))
    return (values[0], None) if values else (None, None)


def declared_value(home, item):
    """(value, refusal) for ITEM in `<home>/config.md`: `config_text`, then
    `config_value`, so an unreadable file, a doubled row and a table the
    walker refused above ITEM reach the caller the same way -- as a refusal
    it acts on by its own kind.
    """
    text, refusal = config_text(home)
    if refusal is not None:
        return None, refusal
    return config_value(text, item)


def declared_mode(home):
    """(kind, value) for the `Mode` row — what the repository SAYS it wants.

      "none"     nothing is declared: no file, no such row in a table the
                 walk read whole, an empty value, or a file holding no such
                 table. Four spellings of one state, the same four the
                 pull-request-language row has for not naming a language
      "mode"     `local` or `shared`, lowercased
      "unknown"  a row is there and its value is not a mode — a claim nobody
                 can act on, which is not the same as no claim
      "refused"  the file is there and will not read, the row is written
                 more than once, or the walk refused the table without
                 reading the row (#871); VALUE is `declared_value`'s sentence

    **There is no default.** Every other item in `config.md` falls back to
    what every repository got before the row existed; for the mode that is
    *the folder decides*, so an absent row is filled in from the folder by
    `seal mode` rather than assumed here. A default of `shared` would report
    every undeclared local-mode repository as lying.

    **`refused` is not `none`** (#867). An unreadable file used to fold into
    `none`, and `hooks/mode-gate.py` opened the file a second time to tell
    the two apart. A doubled row was read first-wins here and by the writer.
    Now the reader tells them apart once: the gate says nothing on a refusal,
    and `seal mode` prints it and writes nothing, because writing a row into
    a file whose rows disagree, or that nobody can read, cannot make it
    agree.
    """
    value, refusal = declared_value(home, ROW_ITEM)
    if refusal is not None:
        return "refused", refusal
    lowered = (value or "").lower()
    if not lowered:
        return "none", ""
    return ("mode", lowered) if lowered in MODES else ("unknown", value)


# --- the reference roots (#688) -------------------------------------------
#
# A project may have kept its own `specs/` before the plugin arrived. The
# plugin writes only to its own root and reads every other directory named
# `specs` as history: a REFERENCE ROOT, read when a change touches what it
# describes and never moved, edited, absorbed or deleted. The checks that read
# a record ask `under_reference_root` before they read a path, so none of them
# carries a test of its own (`templates/setup/config.md` *Reference specs*).

REFERENCE_ROW = "Reference specs"
NO_REFERENCE = "none"
# The directory name the default reads as a reference root at any depth.
REFERENCE_NAME = "specs"
# The plugin's own root in the tree, `hooks/lib/optin.py#HOME`. Spelled here so
# this reader needs no second sibling, and held equal to that one by
# `tests/hooks/test_config.py`.
HOME = "seal"


def inside_the_root(rel):
    """True when the `/`-joined repository-relative `rel` is the plugin's own
    root or under it — never a reference root, whatever a row says."""
    return rel == HOME or rel.startswith(HOME + "/")


def reference_roots(home):
    """The repository-relative directories `<home>/config.md`'s
    `Reference specs` row names, as a tuple; `()` for `none`; or None, the
    default — every directory named `specs` outside the plugin's root.

    The value is comma-separated prefixes, each with or without a trailing
    `/` or a leading `./`. No file, no such row, an empty value or a file
    that will not read all mean the default, which is what every repository
    got before the row existed. A prefix naming the plugin's own root or
    anything under it is dropped: a reference root is outside the root by
    definition, and the root's records are read whatever the row says.

    **No root at either place is `()`, no reference root at all** — not the
    default. A reference root is defined against the plugin's root, and a
    repository with none has not opted in: the one layout the plugin ever
    read without a root is 0.3.x, whose top-level `specs/` was the plugin's
    own, and `seal unverified` still reads that spelling as its records. A
    person
    joining a project runs the bootstrap, which creates the root, before any
    check reads the tree.

    **A refusal reads as the default** (#867): a file that will not read, as
    before, and a `Reference specs` row written twice, which `config_value`
    gives no value. Its caller, `seal unverified`, is not among the commands
    `config_text` names as refusing: what a refusal costs it is the reading
    every repository had before the row existed, and no record is written or
    lost on it."""
    if not home:
        return ()
    # A refusal carries no value, so it lands with no row and an empty one.
    value, _refusal = declared_value(home, REFERENCE_ROW)
    if not value:
        return None
    if value.lower() == NO_REFERENCE:
        return ()
    out = []
    for entry in value.split(","):
        prefix = entry.strip().replace("\\", "/")
        while prefix.startswith("./"):
            prefix = prefix[2:]
        prefix = prefix.strip("/")
        if prefix and not inside_the_root(prefix) and prefix not in out:
            out.append(prefix)
    return tuple(out)


def under_reference_root(rel, roots):
    """True when the repository-relative path `rel` is a reference root or
    under one. `roots` is `reference_roots`' answer: None reads the default —
    any directory named `specs` on the path, outside the plugin's root — and
    a tuple reads its prefixes alone.

    A predicate on a TREE path, so local mode needs no arm of its own: its
    root is under the git directory and never in the tree, and every `specs`
    the tree holds is outside it."""
    parts = [p for p in rel.replace("\\", "/").split("/") if p and p != "."]
    if not parts or inside_the_root(parts[0]):
        return False
    if roots is None:
        return REFERENCE_NAME in parts
    joined = "/".join(parts)
    return any(joined == p or joined.startswith(p + "/") for p in roots)


# --- the policy root (#953) -------------------------------------------------

POLICY_ROW = "Policy root"
POLICY_DEFAULT = "docs"


def policy_root(home):
    """The repository-relative directory `<home>/config.md`'s `Policy root`
    row names, without a leading `./` or a trailing `/`, or `docs`.

    No root, no file, no such row, an empty value, a refusal and a value
    that leaves the repository (an absolute path or a `..` part) all read as
    `docs`, the directory every repository read before the row existed.
    `templates/setup/config.md` *The fold's values* states the row."""
    value = declared_value(home, POLICY_ROW)[0] if home else None
    rel = (value or "").strip().replace("\\", "/")
    while rel.startswith("./"):
        rel = rel[2:]
    rel = rel.rstrip("/")
    if not rel or rel.startswith("/") or ".." in rel.split("/"):
        return POLICY_DEFAULT
    return rel


# --- the pact a signer declares (#647) -------------------------------------
#
# A work item can commit in more than one repository, and where those
# repositories keep one contract together, the one copy of it is the PACT:
# `seal/pact.md` in the repository that holds it. Every repository of such a
# work item is a SIGNER, the pact's repository included. A signer other
# than the pact's repository names the pact here, by the origin remote URL of
# the repository that holds it, and the pact's repository needs no row: it is
# identified by holding `seal/pact.md` (`docs/the-pact.md`).
#
# One command asks this row, through THIS reader:
# `skills/verify/scripts/pact_check.py`, run as `seal pact`, which reads
# every signer from the pact's repository and refuses what will not parse. A
# signer's CI reads nothing of the pact (`docs/the-pact.md`).

PACT_ROW = "Pact"
PACT_SEPARATOR = ";"


def normalise_remote(url):
    """A remote URL reduced to host and path, so two spellings of one
    repository compare equal.

    `git@example.com:org/repo.git` and `https://example.com/org/repo` are one
    repository, and ssh at one machine with https at another is the ordinary
    case — comparing the strings would refuse every real import.

    The scheme goes, a `user@` prefix goes, the scp-style `host:path` colon
    becomes `/` **only where there was no scheme** (so the port in
    `https://example.com:8443/x` is left alone), a trailing `.git` and `/` go,
    and the result is lowercased.

    Wrong in the accepting direction would need two different repositories to
    reduce to the same host and path, which is the same repository. Wrong in
    the refusing direction costs a message naming `--allow-other-repo`. That
    asymmetry is why this is done at all.

    Anything that is not text reduces to "", because one caller passes a field
    out of a manifest another machine wrote. `read_manifest` checks that the
    manifest is an object and that its `format` is one this build reads; every
    other field is whatever the zip says, and a list here used to reach the
    console as an `AttributeError`.

    **It lives here and `skills/implement/scripts/seal.py` re-exports it**
    (#647), the arrangement this module's docstring records for the `Mode`
    reader. The `Pact` reader below needs it, and this module cannot import
    `seal.py`: that file imports this one, and a hook must not load a
    two-thousand-line command to read a row. One normaliser, reached by the
    name each caller already spells.
    """
    if not isinstance(url, str):
        return ""
    text = url.strip()
    if not text:
        return ""
    schemed = "://" in text
    if schemed:
        text = text.split("://", 1)[1]
    authority = text.split("/", 1)[0]
    if "@" in authority:
        text = text.split("@", 1)[1]
    if not schemed and ":" in text:
        text = text.replace(":", "/", 1)
    text = text.rstrip("/")
    if text.endswith(".git"):
        text = text[: -len(".git")]
    return text.lower()


def remote_entries(entries, empty):
    """(parsed, refusals) for ENTRIES, each a remote URL as somebody wrote
    it: `parsed` as `(as written, normalised)` in order, and one sentence
    per entry refused, EMPTY being the sentence for an empty one. An entry
    holding a space, one that reduces to no host and path, and two entries
    naming one repository are refused. Two entries that end in one segment
    are two repositories: a pact anchor names a pact by its URL.
    """
    parsed, refusals, seen = [], [], {}
    for entry in entries:
        written = entry.strip()
        if not written:
            refusals.append(empty)
            continue
        if any(ch.isspace() for ch in written):
            refusals.append(f"`{written}` holds a space — one remote URL per entry")
            continue
        normalised = normalise_remote(written)
        if "/" not in normalised:
            refusals.append(
                f"`{written}` is not a remote URL — it reduces to no host and "
                "path, so no repository can be found by it"
            )
            continue
        if normalised in seen:
            refusals.append(f"`{written}` and `{seen[normalised]}` are one repository")
            continue
        seen[normalised] = written
        parsed.append((written, normalised))
    return parsed, refusals


def pact_declaration(text):
    """(pacts, refusals) for the `Pact` row of a config.md's TEXT.

      pacts     [(as written, normalised)] for every entry of the `Pact`
                row that parsed, in the order the row lists them; [] where
                no row names a pact
      refusals  one sentence per thing that would not parse, naming it

    **It refuses in sentences and stops nothing.** Its caller, `seal pact`,
    run at the pact's repository, exits 2 on a refusal.

    No row, an empty value, and a file with no table are one state, *no pact
    is held elsewhere* — the direction everything in this module fails in. A
    value that is there and does not parse is not that state, and it is
    refused rather than read as absent: a signer that wrote a row and is
    read as having written none is the silence this reader exists to end.

    **Only the `Pact` row is read.** A row of any other item is no answer
    about a pact, a `Pact notify` row an earlier release read included
    (`templates/setup/config.md` *Pact*).

    **A table the walker refuses is refused here too** (#871). Its
    sentences are appended after every other refusal: a `Pact` row below
    the line it stopped at is one the walk never read. `seal pact` exits 2
    on it.
    """
    rows, walk_refusals = config_table(text)
    # A row written twice has no value, by `value_of`'s rule and in its
    # sentence (#867): the first row is not the answer, so a doubled `Pact`
    # lists no pact.
    value, doubled = value_of([(item, v) for _i, item, v in rows], PACT_ROW)
    if doubled:
        return [], [doubled, *walk_refusals]
    if not value:
        return [], walk_refusals
    pacts, refused = remote_entries(
        value.split(PACT_SEPARATOR),
        f"`{PACT_ROW} | {value}` holds an empty entry — one remote URL between "
        f"each `{PACT_SEPARATOR}`",
    )
    return pacts, refused + walk_refusals


def declared_pacts(home):
    """`pact_declaration` over `<home>/config.md`, or None where that file
    is there and will not read.

    **Not the rule the other readers here keep**, and on purpose (round 1 of
    #647, white 5). They answer an unreadable file as no row, because a gate
    that refuses wrongly stops a session with nobody able to get past it.
    This reader's caller is `seal pact`, run by a person at the pact's
    repository, and a signer whose written rows read as absent is the
    silence `pact_declaration` exists to end. So no file is no row, and a
    file that will not read is None, which `seal pact` refuses as
    `UNREADABLE`.

    Since #867 every command reading a row takes this reader's side, and
    `config_text` is where the two states are told apart for all of them;
    this is that answer in the shape `seal pact` reads."""
    text, refusal = config_text(home)
    if refusal is not None:
        return None
    if text is None:
        return [], []
    return pact_declaration(text)


# --- one GFM table walker (#647) --------------------------------------------
#
# Two tables are read out of markdown by name: `seal/config.md`'s
# `| Item | Value |` (#871) and the pact's `| Signer |`. One walker reads
# both, because two walkers are two break lists to keep in step, and round
# 3 of #735 measured exactly that drift in the one there was: an autolink
# row ended the table, and a signer written as one was read by nobody at
# exit 0.
#
# **It reads what cmark-gfm renders, or refuses.** It is held to the renderer
# by `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py`, a property case
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
                   A caller whose file holds one table, `seal/config.md` or
                   the machine-local pact map, leaves BESIDE false; the
                   anchor table's reader sets it, because a frame's section
                   holds other tables
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
    `pact_signers`' after "the pact ".
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


# The pact's own table: every OTHER signer, by origin remote URL, one per
# row under a `| Signer |` header (`templates/setup/pact.md`).
SIGNER_HEADER = ("Signer",)


def read_table(text, header):
    """(rows, refusals, header read) for the table of TEXT headed HEADER,
    or, where TEXT holds none, headed as HEADER was written before 0.19.0
    (`renamed_header`). A text holding a HEADER table is read from it alone,
    and an old header it also holds is refused, wherever that table stands:
    its rows would otherwise go unread at exit 0 (round 1 of #822, yellow 1).
    The refusal is not added where the walk's stray-row refusal already names
    the old header, compared by the cells the refusal quotes, so a header
    written without its spaces is named once too (round 2 of #822, white 5).
    An old header with no blank line above it is one of the HEADER table's
    rows as GFM renders it; that row is not read, so it is named as the old
    header and not also as an entry (#830), quoted as the line is written so
    a person searching the file for it finds it (#831).
    Where neither is there, the refusal names HEADER and the
    header read is None, so a caller tells the old header from the new one
    without reading the text again (#822)."""
    rows, refusals = gfm_table(text, header)
    old = renamed_header(header)[0]
    old_rows, old_refusals = gfm_table(text, old) if old else ([], [])
    holds_old = old is not None and not (
        old_refusals and old_refusals[0].startswith("holds no ")
    )
    if not (refusals and refusals[0].startswith("holds no ")):
        named = f"`| {' | '.join(old)} |`" if old else None
        glued = [
            # exempt from splitlines: the line gfm_table numbered, split as it was
            text.splitlines()[line - 1].strip()
            for line, cells in rows
            if holds_old and cells == old
        ]
        if holds_old:
            # An old header with no blank line above it is one of this
            # table's rows to GFM; it is the old header, named below or by
            # the walk's stray-row refusal, never an entry (#830).
            rows = [(line, cells) for line, cells in rows if cells != old]
        if holds_old and not any(
            table_cells(quoted) == old
            for r in refusals
            for quoted in re.findall(r"`([^`]*)`", r)
        ):
            new = f"`| {' | '.join(header)} |`"
            refusals = [
                *refusals,
                (
                    f"holds a `{glued[0]}` line inside its {new} table, the word "
                    f"before {RENAMED_IN}, which GFM reads as one of that "
                    "table's rows — delete the line"
                )
                if glued
                else (
                    f"also holds a {named} header, the word before {RENAMED_IN}, "
                    f"and nothing under it is read while the {new} table "
                    "stands — move its rows into that table and delete it"
                ),
            ]
        return rows, refusals, header
    if holds_old:
        return old_rows, old_refusals, old
    return rows, refusals, None


def pact_signers(text):
    """(signers, refusals, header) for the `| Signer |` table of a pact's
    TEXT. `signers` is `remote_entries`' parsed list, and a table that is
    absent or empty is a refusal, because a pact nobody signs is not a pact.
    `header` is the header the table was read under, `SIGNER_HEADER` or the
    one 0.18.x wrote (`read_table`), or None where the text holds neither;
    every refusal names the header it was read under.

    The table is read by `gfm_table`, so it is read as cmark-gfm renders it
    or refused, and no signer is dropped while the table reads as complete
    (round 3 of #735). On top of the walk: a row with an empty cell is
    refused by `remote_entries`, and so is every entry that is not one
    remote URL.
    """
    rows, refusals, header = read_table(text, SIGNER_HEADER)
    if header is None:
        return [], [refusals[0] + ", so it names no signer"], None
    values = [cells[0] for _line, cells in rows]
    # `seal pact` prints each refusal after "the pact ", so an entry's own
    # sentence gets a lead-in that reads after those words (round 2 of #647,
    # white 14); `remote_entries` keeps the sentences the `Pact` row prints.
    signers, entry_refusals = remote_entries(values, "an empty row")
    word = header[0]
    out = [f"has a `{word}` entry that will not read: {r}" for r in entry_refusals]
    out.extend(_signer(refusal) for refusal in refusals)
    if not values and not any("renders no table" in r for r in refusals):
        out.append(f"has a `{word}` table that lists nobody")
    return signers, out, header


def _signer(refusal):
    """A walk refusal, in the words `seal pact` has always printed for the
    pact's table: a row it leaves unread is a signer."""
    return refusal.replace("every row below it", "every signer below it")


# --- the migration config's baseline (#988) --------------------------------
#
# `seal/parity.md` is written from `templates/setup/parity.md`, a `| Field | Value |`
# table whose `Baseline commit` cell holds the SHA the original's coordinates
# refer to, in its first code span. `chain_check.py` compares each round
# record's `original:` line with it, and reads it through this one function.

PARITY_TABLE = ("Field", "Value")
BASELINE_ROW = "Baseline commit"
BASELINE_SHA = re.compile(r"[0-9a-f]{7,40}")
FIRST_CODE_SPAN = re.compile(r"`([^`]*)`")


def baseline_commit(text):
    """`(sha, None)` for the migration config TEXT whose one `Baseline
    commit` row holds 7 to 40 lowercase hex digits, and nothing else, in the
    first code span of its value; else `(None, why)`.

    The table is read by `read_table`, so a table GFM renders no row of is
    no row here. No table, no such row, the row written twice, and a first
    code span holding anything but a SHA, the template's `<SHA>` among them,
    are each a `why` that reads after the file's name."""
    rows, refusals, header = read_table(text, PARITY_TABLE)
    if header is None:
        return None, refusals[0]
    found = [cells[1] for _line, cells in rows if cells[0] == BASELINE_ROW]
    if not found:
        table = f"`| {' | '.join(PARITY_TABLE)} |`"
        said = f"holds no `{BASELINE_ROW}` row in its {table} table"
        return None, "; ".join([said, *refusals])
    if len(found) > 1:
        return None, f"holds {len(found)} `{BASELINE_ROW}` rows, and one names it"
    span = FIRST_CODE_SPAN.search(found[0])
    if span is None or not BASELINE_SHA.fullmatch(span.group(1)):
        return None, (
            f"has a `{BASELINE_ROW}` row whose value is {found[0]}, and the "
            "commit is the first code span of that value, 7 to 40 lowercase "
            "hex digits"
        )
    return span.group(1), None


# --- the word 0.18.x wrote (#822) ------------------------------------------
#
# Until 0.19.0 every repository of a work item that keeps a pact had another
# name, and the pact's one-column table carried it into a file nobody
# regenerates. It still reads (`read_table`), and `seal pact` prints the
# sentence below where it reads one. This unit is the one place the old word
# is written, and it spells the old header in order to read it, which
# `docs/the-pact.md` *The words* says names no signer another way.
RENAMED_IN = "0.19.0"


def renamed_header(header):
    """(old, sentence) for HEADER: the header as written before
    `RENAMED_IN`, and the sentence naming the rename, reading after a file's
    name. (None, None) for a header the rename never touched."""
    if "Signer" not in header:
        return None, None
    old = tuple("Signatory" if cell == "Signer" else cell for cell in header)
    return old, (
        f"heads its table `| {' | '.join(old)} |`, the word before "
        f"{RENAMED_IN} — `| {' | '.join(header)} |` is the header now; rename "
        "it when the file is next edited"
    )

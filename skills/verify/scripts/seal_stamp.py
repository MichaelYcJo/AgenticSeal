#!/usr/bin/env python3
"""seal-stamp — the sealer's stamp, drawn from a `sealed` guarantee.

Issue #30 *What it prints*, redrawn by #717 and #832, and since #975 drawn
once per work item from the sealer's verdict rather than the broad gate's
run. Two things side by side on the terminal's own background, and nothing
else: at the left a wax disc with the disc's mark pressed into it, and three
columns right of it the panel's text — a bold red `SEALED` and a dim rule,
then what the records at the guarantee's commit say: the audited commit and
its branch, the base, the work item, the newest broad run and the round
count (`guarantee_rows` owns the list). The disc is COMPUTED — `hypot`
for its edge, its rim and its groove — and only the disc's mark is
authored: a 28 x 28 chart in `seal-mark.txt` beside this file, read as data
(`read_chart`). Four hand-typed discs came before #30's and every one was
lopsided; a circle that is calculated cannot be off centre. #832's owner
settled the frame on 2026-10-07 — 28 cells across and 14 lines, a wax edge,
a rim lit from the upper left in three steps and a groove lit the other way,
every cell exactly one of nine colours — and left the disc's mark a
placeholder S until #857 chooses one: changing it is changing that file
alone. The same day the owner retired the parchment sheet #717 wrote the
text on, so nothing outside the disc is painted and the stamp reads in the
terminal's own theme.

Two forms, one drawing (`compose`). The block form is half-block characters,
the disc in truecolour and the text in the terminal's own colours and
styles, and it writes a code only where the colour or the style changes:
one SGR per change and no reset inside a line (a code per cell was 282 KB
for one seal). The letter twin is the same footprint as letters — `KEY`
for the disc, `m` its wax edge, `M n N` its rim lit, mid and dark, `.` its
field, `X Y x` the disc's mark's face, highlight and inner shadow and `y`
its drop shadow; the text as itself, with the owner's `·`, `✓`, `─` and
`→` written `.`, `+`, `-` and `>` — for a console that cannot render
half-blocks, and for `seal-stamp` on a pipe. The twin is chosen when
stdout is not a UTF-8 terminal, or on `--shape`. An agent's report carries
neither: no Bash call's pipe is drawn on.

**The `Stop` hook's message is held under a budget** (#717): the harness
persists a `systemMessage` longer than `MESSAGE_LIMIT` and shows a preview
instead, so `admitted` carries as many of the oldest stamps as fit with
their disc and leaves the rest for the next `Stop`. Only one stamp that does
not fit with its disc alone is drawn as the text block with no disc.

The broad gate draws nothing since #975: its report is text on every stream,
and it imports the panel's text rules from here (`fit`, `wrapped`, the
owner's marks) and `sealed_names` for its head.

**The stamp is drawn where a person sees it, once per work item** (#400,
#975). git's `post-commit` (`hooks/commitgate.py#post_commit`) calls
`queue_for_guarantee` after every judged commit; where the commit carries a
`guarantee.md` reading `sealed` and stamped by no earlier run or commit, it
writes the stamp's rows to a values file under the git common dir, keyed by
the Claude Code session. In local mode, where no commit carries the root,
`hooks/sealer-stamp-queue.py` calls `queue_for_local_guarantee` at the
guarantee's `Write` or `Edit` instead (work item 1792363231).
`hooks/sealer-stamp.py` draws each undrawn file once, at the end of that
session's turn. This module owns the file: `queue_for_guarantee`,
`queue_for_local_guarantee` and `write_values`, `read_values`, `pending` and
`claim`. Drawing claims the file first, by renaming it to `.drawn.json`, so
a file is drawn once whoever draws it.

Usage:
  seal-stamp                      the stamp over sample rows, for a person
  seal-stamp --shape              the letter twin
  seal-stamp --from <file>        a queued stamp's values file, drawn once

The gate imports `sealed_names`, `ref_is_commit`, `is_utf8(stream)`,
`text_lines`, `TWIN_ASCII` and the panel's text rules; the commit hook
imports `queue_for_guarantee`; the edit gate imports
`queue_for_local_guarantee`; the hook imports `pending`, `read_values`,
`claim` and `stamp`.
`.github/scripts/release_seal.py`, which the tag push runs, reads `build`
and draws a release's seal as a PNG from its cells, one cell to one square
block of pixels (#1009). That script is the repository's own and the plugin
ships nothing that runs it. The command
exists so a person can see the drawing without a guarantee committed, and
so a values file no hook drew can still be drawn by hand.

Exit codes: 0 printed · 2 refused — a values file that is unreadable or
drawn already; nothing was written on 2. An interpreter below the floor never
reaches this file through `bin/seal-stamp`: `hooks/launch.py` refuses it with
2 first.
"""

import argparse
import collections
import importlib.util
import json
import math
import os
import re
import shlex
import subprocess
import sys
import time

# --- the disc's colours --------------------------------------------------
#
# The owner's frame of 2026-10-07 (#832, `spec.md` decision 5 of work item
# 1791270164), named as the owner's `seal28.py` names them: `WAX_EDGE`; the
# rim, lit from the upper left in three steps, `RIM_LIT`, `RIM_MID` and
# `RIM_DARK`, whose lit and dark the groove inside it takes the other way
# round; `FIELD`; and the disc's mark in the red lily's three tones — `FACE`,
# `LIGHT` where the cell up-left of the disc's mark is the field, `INNER`
# where the cell down-right is — with `DROP`, the shadow the disc's mark
# casts on the field down-right of it. No mid tones and no blend: every
# cell of the disc is exactly one of these nine (`build`), and with
# `TITLE_RED` they are the only colours the stamp sets.
WAX_EDGE = (150, 24, 28)
RIM_LIT = (208, 68, 64)
RIM_MID = (160, 30, 34)
RIM_DARK = (96, 10, 14)
FIELD = (112, 16, 20)
FACE = (186, 38, 42)
LIGHT = (222, 86, 78)
INNER = (90, 8, 12)
DROP = (84, 8, 12)
DISC_COLOURS = (WAX_EDGE, RIM_LIT, RIM_MID, RIM_DARK, FIELD, FACE, LIGHT, INNER, DROP)

# `SEALED` is bold and in this red, the owner's `frames.py`'s `RED`. The rest
# of the text is in the terminal's own colours (`STYLE_CODES`), since #832
# retired the parchment sheet and its four 256-colour codes.
TITLE_RED = (196, 40, 44)

# The letter for each disc colour in the twin (#832): capitals lit and lower
# case shadow — `m` the wax edge and `.` the field, as #30 had them; `M n N`
# the rim lit, mid and dark; `X` the disc's mark's face, and `Y` and `y` its
# highlight and its drop shadow, as #717 had them; `x` its inner shadow. The
# framer chose them (`spec.md` *Data & interfaces*): the twin is for a
# console that cannot draw half-blocks, and no decision of the owner's names
# its letters. Every disc cell is exactly one of these colours, so a cell's
# letter is a lookup (`letter_row`).
KEY = {
    WAX_EDGE: "m",
    RIM_LIT: "M",
    RIM_MID: "n",
    RIM_DARK: "N",
    FIELD: ".",
    FACE: "X",
    LIGHT: "Y",
    INNER: "x",
    DROP: "y",
}


# There is no scale (#853). #30 measured a band of them, 0.75 to 1.0, on the
# lily's chart, #400 chose 0.90 and #717 drew the letter at it; since #832's
# disc of 2026-10-07 the disc is `DISC_CELLS` across whatever a scale said,
# because the disc's mark is a chart and a chart has one size. The band, its
# refusals, `--scale` on both commands and the values file's `scale` field
# were a dial that turned nothing, and they went together.

# --- what one hook message may hold (#717) ---------------------------------
#
# The harness writes a `Stop` hook's `systemMessage` longer than this many
# characters to a file and shows the person a 2 KB preview of it, so a stamp
# past it is not seen. Counted in UTF-16 units, the length JavaScript gives a
# string, not as bytes: a character outside the BMP is two, and Python's `str`
# length counts it as one (`admitted` counts it as two). Measured 2026-10-02
# on Claude Code 2.1.287, with a `Stop` hook in a scratch project and one
# headless `claude -p` turn per size: 9,990 and 10,000 characters, and 9,990
# `▀` (29,942 bytes), were shown with nothing written to the session's
# `tool-results/`; 10,001, 10,010 and 12,000 each left a
# `hook-<uuid>-<n>-systemMessage.txt` there. Then, in round 1's fix pass,
# 4,999 U+1D54F (9,998 units) were shown and 5,001 (10,002 units),
# 9,990 and 10,001 were persisted. This project's own sessions had
# bracketed it before the probe: 9,919 shown, 10,090 persisted. The harness
# can move it, and the only sign is a preview on the owner's screen; the same
# hook at two sizes either side of this number is the whole probe again.
MESSAGE_LIMIT = 10000
# What the hook holds its WHOLE message under — every block, every label and
# the blank line between two blocks. The reserve is for what the hook cannot
# see: `hooks/dispatch.py#report` prepends the session's gate-failure report
# to this same message after the hook has printed. The longest report it can
# write, with each exception's type name and each gate's name cut at
# `NAME_CAP` and its text at `MESSAGE_CAP`, is 564 UTF-16 units for one failed
# gate and 972 for two, separator included; a third, at 1,378, would pass the
# limit beside a stamp at the budget (measured 2026-10-03 over
# `dispatch.describe`, every gate this plugin names and three foreign ones,
# in every group it names and a foreign one, at every phase, with every field
# past its cap -- a record an older or newer plugin wrote;
# `tests/test_a_gate_that_fails_says_so.py#longest_report` is the
# measurement). Before #722 the name had no cap, so a class from outside the
# plugin with a long enough name passed the reserve with two gates. The caps
# count the same units, so a name or a text outside the BMP keeps these
# figures: cut by code points, a text gave two gates 1,309 in #717's round 3.
MESSAGE_RESERVE = 1000
MESSAGE_BUDGET = MESSAGE_LIMIT - MESSAGE_RESERVE


# The disc's numbers (#832), in cells of the terminal's grid, where a cell is
# one column by one half-row and so square. The owner's frame of 2026-10-07:
# the disc is 28 cells across and so `DISC_LINES` lines tall, because the
# disc's mark is a chart drawn for that grid and a chart has one size. Measured inward from the radius, a cell more than `EDGE_INSET` inside
# it is on the disc; one no more than `WAX_INSET` inside it is the wax edge,
# no more than `RIM_INSET` the rim, no more than `GROOVE_INSET` the groove,
# and the rest the field. `LIT_AT` is where the rim turns from mid to lit on
# one side and to dark on the other.
DISC_CELLS = 28
DISC_LINES = DISC_CELLS // 2
EDGE_INSET = 0.2
WAX_INSET = 1.2
RIM_INSET = 3.2
GROOVE_INSET = 4.2
LIT_AT = 0.35

# The disc's mark (#832): one chart in a file beside this one, `DISC_CELLS`
# lines of `DISC_CELLS` characters over `.M`, `M` a cell of the disc's mark.
# It is the owner's placeholder S, Georgia Bold fitted to the grid, until
# #857 chooses the stamp's mark for good — and changing the disc's mark is
# replacing that file and nothing else, which is why it is data read here
# rather than a tuple typed into this module. A candidate in
# `assets/seals/candidates/` is the same `.M` text.
CHART_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "seal-mark.txt")
CHART_MALFORMED = (
    "seal-stamp: the disc's mark chart {path} is not {n} lines of {n} "
    "characters over `.M` with every `M` inside the disc's field ({fault}). "
    "Nothing was drawn."
)


def read_chart(path):
    """The chart at `path` as a tuple of its lines, or `ValueError` with
    `CHART_MALFORMED` naming the path and the first fault: a count of lines
    that is not `DISC_CELLS`, a line of another length, a character outside
    `.M`, or an `M` outside the field — more than `GROOVE_INSET` short of
    the radius, where `build` would draw the rim over it and the disc's mark
    would lose a cell nobody sees go. `utf-8-sig` reads a chart an editor
    saved with a byte-order mark as the same chart, rather than refusing its
    first line as one character too long."""
    with open(path, encoding="utf-8-sig") as handle:
        lines = handle.read().splitlines()
    n = DISC_CELLS
    c, field = (n - 1) / 2, n / 2 - GROOVE_INSET
    fault = None if len(lines) == n else f"{len(lines)} lines"
    for y, line in enumerate(lines):
        if fault:
            break
        stray = sorted(set(line) - set(".M"))
        outside = [
            x
            for x, char in enumerate(line)
            if char == "M" and math.hypot(x - c, y - c) > field
        ]
        if len(line) != n:
            fault = f"line {y + 1} is {len(line)} characters"
        elif stray:
            fault = f"line {y + 1} carries {stray[0]!r}"
        elif outside:
            fault = f"line {y + 1} marks column {outside[0] + 1}, outside the field"
    if fault:
        raise ValueError(CHART_MALFORMED.format(path=path, n=n, fault=fault))
    return tuple(lines)


CHART = read_chart(CHART_PATH)


def build():
    """`(w, h, px)` — the disc's width and height in cells, `DISC_CELLS`
    each, and `px(x, y)`, a cell's colour or None.

    The centre is `c = (DISC_CELLS - 1) / 2` on both axes and the radius
    `r = DISC_CELLS / 2`. A cell `dx, dy` from the centre at distance `d` is,
    from the outside in: None past `r - EDGE_INSET`; `WAX_EDGE` past
    `r - WAX_INSET`; the rim past `r - RIM_INSET` — `RIM_LIT` where `lit =
    (dx + dy) / (|dx| + |dy|)` is under `-LIT_AT`, `RIM_DARK` where it is
    over `LIT_AT`, `RIM_MID` between, `lit` being -1 at the upper left and
    +1 at the lower right; the groove past `r - GROOVE_INSET`, lit the
    other way — `RIM_DARK` where `lit` is under 0, else `RIM_LIT`; then the
    field. In the field a cell under an `M` of `CHART` is `LIGHT` where the
    cell up-left is not under one, else `INNER` where the cell down-right is
    not, else `FACE`; a cell not under one whose up-left is, is `DROP`; the
    rest are `FIELD`. Every cell is exactly one of the nine colours (#832,
    the owner's frame of 2026-10-07). `lit` is read only past the groove's
    inner edge, where `d` is never 0, so it needs no guard."""
    n = DISC_CELLS
    c, r = (n - 1) / 2, n / 2

    def on(x, y):
        return 0 <= x < n and 0 <= y < n and CHART[y][x] == "M"

    def px(x, y):
        if not (0 <= x < n and 0 <= y < n):
            return None
        dx, dy = x - c, y - c
        d = math.hypot(dx, dy)
        if d > r - EDGE_INSET:
            return None
        if d > r - WAX_INSET:
            return WAX_EDGE
        if d > r - GROOVE_INSET:
            lit = (dx + dy) / (abs(dx) + abs(dy))
            if d <= r - RIM_INSET:
                return RIM_DARK if lit < 0 else RIM_LIT
            if lit < -LIT_AT:
                return RIM_LIT
            return RIM_DARK if lit > LIT_AT else RIM_MID
        if on(x, y):
            if not on(x - 1, y - 1):
                return LIGHT
            return INNER if not on(x + 1, y + 1) else FACE
        return DROP if on(x - 1, y - 1) else FIELD

    return n, n, px


# --- the two row writers -------------------------------------------------
#
# Both walk the same cells, so the two forms have one footprint: one
# character per cell. A cell is `(char, fg, bg, style)` (#832): the
# character, or None for an empty cell; `fg` and `bg` a triple — one of the
# disc's colours or `TITLE_RED` — or None for the terminal's own; `style`
# None, `"dim"`, `"bold"` or `"green"`. A disc cell is `▀` with its top
# half's colour as the foreground and its bottom half's as the background,
# or `▄` in its bottom half's colour where the top half is off the disc.
# Nothing but a disc cell has a background.

RESET = "\x1b[0m"
EMPTY = (None, None, None, None)
HALF_BLOCKS = ("▀", "▄")
# The code each text style is written as: the terminal's own dim, bold and
# green. `22;39` ends any of them — 22 the intensity, 39 the foreground,
# which the green set.
STYLE_CODES = {"dim": "2", "bold": "1", "green": "32"}
# The owner's characters the letter twin writes in ASCII, one for one, so a
# console that is not UTF-8 is handed a printable line as wide as the block
# form's (#832).
TWIN_ASCII = {"·": ".", "✓": "+", "─": "-", "→": ">"}


def disc_cell(top, bottom):
    """The cell over two half-rows of the disc, `top` and `bottom` each a
    colour or None."""
    if top and bottom:
        return ("▀", top, bottom, None)
    if top:
        return ("▀", top, None, None)
    if bottom:
        return ("▄", bottom, None, None)
    return EMPTY


def disc_cells(px, w, y):
    """One line of cells over the disc alone: row `y` on top, `y + 1`
    below."""
    return [disc_cell(px(x, y), px(x, y + 1)) for x in range(w)]


def colour_code(ground, colour):
    """One colour's part of an SGR: `ground` 38 for the foreground, 48 for
    the background; a triple is truecolour, None the terminal's own."""
    if colour is None:
        return "39" if ground == 38 else "49"
    r, g, b = colour
    return f"{ground};2;{r};{g};{b}"


def colour_row(cells):
    """One line of the block form, lean (#832, `spec.md` S11, after the
    owner's `frames.py#encode`). A code only where the next visible cell's
    foreground, background or style differs from what is set; every part of
    that change in one SGR; no reset inside the line, and `RESET` at its end
    where it wrote a code. An empty cell or a space — no space carries a
    background, because only a disc cell has one — is written as a space
    that keeps the foreground and the style as they are set, since a space
    shows neither; but a background would paint it, so one still set from
    the disc ends there with `49`. A style that ends is written `22;39`
    first, which takes the foreground back to the terminal's own as well, so
    `39` is not written a second time in the same SGR. A green cell writes no
    foreground part: `32` is its colour, and a `39` after it in the same SGR
    would take the green back off — which a tick leading a `""` row beside
    the disc met, the disc's colour being still set across the label's
    spaces."""
    out, state, wrote = [], (None, None, None), False
    for char, fg, bg, style in cells:
        if char in (None, " "):
            char, fg, style = " ", state[0], state[2]
        if (fg, bg, style) != state:
            parts, shown = [], state[0]
            if style != state[2]:
                if state[2]:
                    parts.append("22;39")
                    shown = None
                if style:
                    parts.append(STYLE_CODES[style])
            if fg != shown and style != "green":
                parts.append(colour_code(38, fg))
            if bg != state[1]:
                parts.append(colour_code(48, bg))
            out.append(f"\x1b[{';'.join(parts)}m")
            wrote = True
            state = (fg, bg, style)
        out.append(char)
    return "".join(out) + (RESET if wrote else "")


def letter_row(cells):
    """One line of the letter twin over the same cells (#832, `spec.md`
    S4): a half-block's `KEY` letter — its foreground's, which is the top
    half's colour on `▀` and the bottom half's on `▄` — the text's own
    character with `TWIN_ASCII` applied, and a space for an empty cell.
    Every disc cell is exactly one palette colour, so the letter is a
    lookup. A cell is the disc's by its colour, never by its character: a
    value may carry `▀` or `▄` — a branch name can — and that is text,
    written as itself."""
    out = []
    for char, fg, _bg, _style in cells:
        if char in HALF_BLOCKS and fg in KEY:
            out.append(KEY[fg])
        else:
            out.append(TWIN_ASCII.get(char, char or " "))
    return "".join(out)


def strip_ansi(s):
    return re.sub(r"\x1b\[[0-9;]*m", "", s)


# --- the panel's text rules ------------------------------------------------
#
# How a row's value is cut, continued and marked. They were the broad gate's
# until #975, when the stamp left the gate's run: the stamp's writer
# (`queue_for_guarantee`) composes rows too, and the gate's plain report
# imports them from here, so both write a row by one set of rules.

# How many columns a panel value is given (#832, `spec.md` S5a of work item
# 1791270164): the widest that keeps the stamp's widest line inside an
# 80-column terminal, the floor a command line's output is held to. The open
# layout has no frame, so the terminal is the bound: 28 columns of disc, `GAP`
# (3) clear, a label of seven and a space, and the value — 28 + 3 + 8 + 41 =
# 80. Before #832 it was 23, what the 36-column frame of the stamp then left.
# A longer value runs past the terminal's edge or wraps into the disc's
# column, so a value is elided before it does (round 1, finding 5 of #666): a
# cut ref would read as a whole ref.
#
# Stated here and measured over there, and neither may move without the other
# going red: `test_the_panel_value_width_is_what_the_stamp_actually_gives`
# draws a value of this width and measures the stamp's widest line.
PANEL_VALUE_WIDTH = 41
ELISION = "..."
# The panel's own characters (#832 S5a, the owner's design of 2026-10-07):
# the separator inside a value, the arrow before a deferral's homes, the mark
# on a result row that passed and the mark on a row that is not a pass. They
# are the owner's and not ASCII; the letter twin, which exists for a console
# that is not UTF-8, maps them where it writes them (`TWIN_ASCII`).
SEP, ARROW, TICK, DOT = " · ", "→", "✓ ", "· "


def fit(value, keep="head", width=None):
    """`value` as the panel can carry it: unchanged where it fits, else
    elided to `width` — `PANEL_VALUE_WIDTH` unless a caller names less —
    with `ELISION` on the side that was cut.

    `keep="head"` for a branch name, whose issue number leads and is what a
    reader matches to a ticket; `keep="tail"` for a ref, where the
    `origin/` a runner reads is the part a reader can infer. Every value a
    panel carries passes through here, so no row is wider than the frame
    and none is cut by it without a marker (#666). `width` is the room a
    ref has beside its commit on the `base` row (#832)."""
    value = str(value)
    width = PANEL_VALUE_WIDTH if width is None else width
    if len(value) <= width:
        return value
    room = width - len(ELISION)
    return ELISION + value[-room:] if keep == "tail" else value[:room] + ELISION


def wrapped(label, pieces):
    """A list on as many panel rows as it needs: the first row under `label`,
    the rest as `""` rows beneath it (round 1's 🟡 1 of #666).

    The owner chose continuation rows over a wider panel (`questions.md`
    Q1), so a list of counts or homes continues rather than losing its tail
    to `...`; only a branch or a ref, which have no bound, are elided. Each
    piece but the first carries the separator that joins it to the one
    before (`", #664"`, or `" · 11 skipped"` since #832). A row is broken
    before a piece that would not fit, and keeps that separator's mark — the
    comma, or the ` ·` — at its end so the reader sees the list goes on; two
    columns are held back for it on every piece but the last, because ` ·`
    is two. One piece wider than the frame by itself is still elided by
    `fit`."""
    rows, line = [], ""
    for n, piece in enumerate(pieces):
        room = PANEL_VALUE_WIDTH - (0 if n == len(pieces) - 1 else 2)
        if line and len(line + piece) > room:
            lead = piece[: len(piece) - len(piece.lstrip(", ·"))]
            rows.append(line + lead.rstrip())
            line = piece.lstrip(", ·")
        else:
            line += piece
    rows.append(line)
    return [(label if n == 0 else "", fit(row)) for n, row in enumerate(rows)]


def item_value(item):
    """The `item` row: the digits before the first `-` of the work item
    directory's name, or the whole name where it has no `-`."""
    name = os.path.basename(os.path.normpath(item))
    return name.split("-", 1)[0] or name


# --- the stamp: the disc at the left, the text block at the right ---------
#
# #832, the owner's layout of 2026-10-07 (`spec.md` decision 6 of work item
# 1791270164, the owner's `frames.py#design_open`): no parchment, no edge, no
# frame and no background outside the disc, the text in the terminal's own
# colours. #717's sheet, which the text was written on, is retired.

# The columns a label is padded to before the one space ahead of its value:
# the owner's seven, which `CI also` fills.
LABEL_WIDTH = 7
# The dim `─` rule after the title: the owner's reference's thirty.
RULE_WIDTH = 30
# The panel's first row, which is drawn as the title rather than as a row.
TITLE_ROW = ("SEALED", "")
# The mark that leads a value and the style it is drawn in: a result row
# that passed, green, and a row that is not a pass, dim (#832).
VALUE_MARKS = {"✓": "green", "·": "dim"}
# The clear columns between the disc's last column and the text block's
# first (#832, the owner's three).
GAP = 3

# `disc` is where the disc's grid stands, `(left, top, w, h)`: `left` and
# `w` in cells, `top` and `h` in half-rows from the stamp's first line, or
# None with no disc — what a case reads to find the disc without
# re-deriving the layout (#832).
Letter = collections.namedtuple("Letter", "cells width height disc")


def text_cells(text, style=None, fg=None):
    """`text` as cells in one style and foreground, with no background."""
    return [(char, fg, None, style) for char in text]


def text_lines(rows):
    """The text block of `rows`, as lines of cells (#832, `spec.md` S3a).

    Where the first row is the panel's title row, `("SEALED", "")`, the
    first line is `SEALED ` bold in `TITLE_RED` and a dim rule of
    `RULE_WIDTH` `─`, and the second is blank; rows without it draw no
    title. Then one line per row: the label padded to `LABEL_WIDTH` and a
    space, dim, and the value in the terminal's own foreground — a leading
    `✓ ` with the `✓` green, a leading `· ` with the `·` dim. A `None` row
    is a blank line; a `""` label is seven spaces and one, so its value
    stands under the value above it. The rows are drawn as given:
    `guarantee_rows` owns the stamp's shape, `broad_gate.panel` the gate's
    report's, and a values file an older gate wrote draws its older rows in
    this layout."""
    rows, lines = list(rows), []
    if rows and rows[0] is not None and tuple(rows[0]) == TITLE_ROW:
        title = text_cells("SEALED ", "bold", TITLE_RED)
        lines += [title + text_cells("─" * RULE_WIDTH, "dim"), []]
        rows = rows[1:]
    for row in rows:
        if row is None:
            lines.append([])
            continue
        label, value = row
        mark = VALUE_MARKS.get(value[:1]) if value[1:2] == " " else None
        lines.append(
            text_cells(f"{label:<{LABEL_WIDTH}} ", "dim")
            + text_cells(value[:1], mark)
            + text_cells(value[1:])
        )
    return lines


def compose(rows, disc=True):
    """The stamp of `rows` as lines of cells (see the writers above), with
    its width and height and where the disc stands: `Letter(cells, width,
    height, disc)` (#832, `spec.md` S3, the owner's layout of 2026-10-07).

    The disc — `disc` False leaves it off, which is the rung `fitted` steps
    down to — stands at column 0, `DISC_CELLS` wide and
    `DISC_LINES` tall, and the text block (`text_lines`) begins `GAP`
    columns right of it, or at column 0 with no disc. The height is the
    taller one's, and each is centred on it. A cell inside the circle is its
    colour on both halves; every other cell of the disc's columns is empty,
    and nothing outside the disc has a background. No line runs past its
    own last visible cell, so the width is the longest line's."""
    text = text_lines(rows)
    if disc:
        n, _, px = build()
        tall = DISC_LINES
    else:
        n, tall, px = 0, 0, None
    height = max(len(text), tall)
    top_disc, top_text = (height - tall) // 2, (height - len(text)) // 2
    cells = []
    for ln in range(height):
        k, t = ln - top_disc, ln - top_text
        line = disc_cells(px, n, 2 * k) if 0 <= k < tall else [EMPTY] * n
        said = text[t] if 0 <= t < len(text) else []
        line += [EMPTY] * (GAP if px else 0) + said
        # No space carries a background, so a blank at the end is padding.
        while line and line[-1][0] in (None, " "):
            line.pop()
        cells.append(line)
    width = max((len(line) for line in cells), default=0)
    where = (0, 2 * top_disc, n, n) if px else None
    return Letter(cells, width, height, where)


# --- what the hook and the gate call ---------------------------------------


def stamp(rows, shape=False, disc=True):
    """The lines of the stamp: the disc beside the text block of `rows`
    (#717, #832). `shape` picks the letter twin. `disc` False is the text
    block with no disc, the rung `fitted` steps down to."""
    writer = letter_row if shape else colour_row
    return [writer(line) for line in compose(rows, disc).cells]


def admitted(blocks, budget=MESSAGE_BUDGET):
    """The drawn blocks one `Stop` message carries under `budget`, oldest
    first (#717). `blocks` is `(label, rows)` per values file, oldest first;
    a drawn block is its label and then its block form.

    The owner's rule of 2026-10-02 (`questions.md` Q6), which replaced one
    rung for the whole message: a seal keeps its disc rather than share a
    message without it. So the message carries as many of the oldest blocks
    as fit together WITH the disc. A block has two rungs since #853: with its
    disc, and the text block alone, because the disc has one size. The
    blocks past those are not drawn here; the hook leaves their files
    pending, and the next `Stop` draws them whole.

    The rung with no disc is for one block alone, the oldest, when it does
    not fit with its disc by itself; it is returned whatever its size, because
    nothing comes after it. So the first block is always drawn and the queue
    cannot stall. A text block with no disc is about 50 characters a row with
    its codes (925 with its label for the widest panel this tree can
    produce, measured 2026-10-07), its width bounded by
    `PANEL_VALUE_WIDTH`.

    A size is counted in UTF-16 units, which is what the harness counts
    (`MESSAGE_LIMIT`): a character outside the BMP is two. `budget` is a
    parameter so a case can drive both rungs."""

    def drawn(block, disc):
        label, rows = block
        text = "\n".join([label, *stamp(rows, disc=disc)])
        # `surrogatepass`: a values file is JSON, which can carry a lone
        # surrogate, and a size that raised would leave every file pending.
        return text, len(text.encode("utf-16-le", "surrogatepass")) // 2

    out, used = [], -2
    for block in blocks:
        text, size = drawn(block, True)
        if used + 2 + size > budget:
            break
        out.append(text)
        used += 2 + size
    if not out and blocks:
        return [drawn(blocks[0], False)[0]]
    return out


def fitted(blocks, budget=MESSAGE_BUDGET):
    """The message the `Stop` hook prints for `blocks`: `admitted`'s drawn
    blocks joined by a blank line, held under `budget` (#717). The blocks
    past what `admitted` carries are not in it; the hook claims only the
    files whose blocks it holds."""
    return "\n\n".join(admitted(blocks, budget))


# A ref spelled as a commit: what `--base <sha>` resolves to (`sealed_names`).
HEX_REF = re.compile(r"[0-9a-fA-F]{4,40}")


def sealed_names(tree, base, branch=None, ref=None):
    """`<branch> @ <tree> against <ref> @ <base>` — what the broad gate's
    `BROAD GATE PASSED` and `BROAD GATE FAILED` lines say they measured, and
    what a drawn stamp's label says was sealed (#666, #975).

    A head naming two commits named neither the branch nor the base's ref,
    so a reader matched a line to its work by hash alone. One composer for
    the three lines, because two spellings of one sentence drift.

    Two collapses, and each leaves a part out rather than printing it twice:

      - `branch` None — a detached HEAD has no branch, so the tree prints
        alone, with no stray `@`
      - `ref` None, or a ref that is the commit itself — a bare SHA given as
        `--base` resolves to itself, and `1e2bed9 @ 1e2bed9` says one thing
        twice. Read as a ref spelled in hex with either hash a prefix of the
        other, because the caller may have typed forty characters where the
        gate prints eight, and a branch named `b` is not the commit `b1e2…`

    `ref` is the RESOLVED ref (`broad_gate.Base.ref`), the one CI reads, not
    the spelling the caller typed: #423's repair was that a reader can tell
    `origin/<base>` from a local ref a week behind it."""
    named = f"{branch} @ {tree}" if branch else f"{tree}"
    against = f"{base}" if ref_is_commit(ref, base) else f"{ref} @ {base}"
    return f"{named} against {against}"


def ref_is_commit(ref, base):
    """True where `ref` names nothing the commit `base` does not: no ref at
    all, or a ref spelled in hex that `base` begins, or that begins with
    `base`. The one reading of *the ref is the commit*, asked by
    `sealed_names` for the lines and by `broad_gate.panel` for the row under
    `base`, so the two cannot disagree about when a ref is worth printing."""
    base, ref = str(base), ("" if ref is None else str(ref))
    if not ref:
        return True
    return bool(HEX_REF.fullmatch(ref)) and (
        base.startswith(ref) or ref.startswith(base)
    )


def pick_shape(stream):
    """True when `stream` gets the letter twin: anything that is not a UTF-8
    terminal. A console on another codepage draws UTF-8 half-blocks as
    mojibake, and a pipe has no terminal to draw colour on, so `seal-stamp`
    on one prints the twin. Asked BEFORE the stream is reconfigured to UTF-8 — after
    that call every stream answers `utf-8`, and a cp949 console would get the
    blocks it cannot draw."""
    if not is_utf8(stream):
        return True
    return not is_terminal(stream)


def is_utf8(stream):
    """True when `stream` says its encoding is UTF-8, whatever it is attached
    to. The half of `pick_shape` the broad gate asks on its own since #975:
    its report is text on every stream, and only a console that is not UTF-8
    gets the owner's marks in ASCII. Asked before the streams are
    reconfigured, for `pick_shape`'s reason."""
    encoding = (getattr(stream, "encoding", None) or "").lower().replace("-", "")
    return encoding == "utf8"


def is_terminal(stream):
    """True when `stream` is a terminal, whatever its encoding.

    The other half of `pick_shape`, beside `is_utf8`: a cp949 terminal is a
    terminal that gets letters, and a UTF-8 pipe is not a terminal (#400).
    Asked with `pick_shape`, before the streams are reconfigured, so both
    answers describe the stream as the process found it."""
    isatty = getattr(stream, "isatty", None)
    try:
        return bool(isatty and isatty())
    except (ValueError, OSError):
        return False


# --- a stamp's values, drawn by somebody else ------------------------------
#
# A Bash call's stdout is a pipe into a tool result nobody sees unfolded
# (#400), so the stamp's rows are written here — since #975 by the commit of
# a `sealed` guarantee (`queue_for_guarantee`), and in local mode by its
# write (`queue_for_local_guarantee`) — and a `Stop` hook in the session they
# were queued for draws them. The directory is under the git COMMON dir
# because the worktree the commit landed in and that session's cwd can be
# different worktrees of one clone, and the common dir is the one place both
# resolve alike; a local root sits in the same directory. It is keyed by session so that a concurrent
# session of the same clone does not draw, and take, a stamp that is not its
# own.

VALUES_DIR = "specseal-stamp"
# The key of a stamp no Claude Code session was found for. No hook reads it;
# `seal-stamp --from` is how such a file is drawn.
NO_SESSION = "none"
PENDING = ".json"
DRAWN = ".drawn.json"

VALUES_UNREADABLE = "seal-stamp: {path} cannot be read ({why}). Nothing was drawn."
VALUES_MALFORMED = (
    "seal-stamp: {path} is not a stamp's values file: {why}. Nothing was drawn."
)
VALUES_DRAWN = (
    "seal-stamp: {path} was drawn already, and a stamp's values are drawn "
    "once. Nothing was drawn; the values stay in {drawn}."
)


def session_key(session):
    """The directory name for `session`: the id's last path part, or
    `NO_SESSION` where there is none. The id names a directory, so a
    separator in a malformed one must not become a path escape."""
    name = os.path.basename(str(session or "").strip())
    return name if name and name not in (".", "..") else NO_SESSION


def values_dir(common, session):
    """Where the runs of `session` wait to be drawn."""
    return os.path.join(common, VALUES_DIR, session_key(session))


def drawn_path(path):
    """The name `path` takes once it has been claimed."""
    stem = path[: -len(PENDING)] if path.endswith(PENDING) else path
    return stem + DRAWN


def write_values(common, session, values, now=None, key=None):
    """Write one stamp's `values` for `session`; returns the file's path.

    Written to a hidden temporary name and renamed into place, so a hook
    listing the directory never reads half a file. The name leads with the
    time in nanoseconds, so a name sort is oldest first, and ends with `key`
    — `<id>-<target sha>` for a guarantee's stamp (`queue_for_guarantee`) —
    or the tree's name where no key is given. Raises `OSError` where the
    directory cannot be made or the file cannot be written."""
    directory = values_dir(common, session)
    os.makedirs(directory, exist_ok=True)
    moment = time.time_ns() if now is None else now
    tail = key or os.path.basename(str(values.get("tree") or "tree"))
    name = f"{moment}-{tail}"
    path = os.path.join(directory, name + PENDING)
    temporary = os.path.join(directory, f".{name}.tmp")
    with open(temporary, "w", encoding="utf-8") as handle:
        json.dump(values, handle)
    os.replace(temporary, path)
    return path


def read_values(path):
    """A values file as it was written, with each row a `(label, value)`
    pair or None. Raises `ValueError` with the refusal sentence for a file
    that cannot be read or is not in that shape. A `scale` key, which every
    gate before #975 wrote, is read as nothing: such a file draws
    as one written without it."""
    try:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
    except OSError as exc:
        raise ValueError(
            VALUES_UNREADABLE.format(path=path, why=exc.strerror or exc)
        ) from exc
    except ValueError as exc:
        raise ValueError(
            VALUES_MALFORMED.format(path=path, why="it is not JSON")
        ) from exc
    if not isinstance(data, dict):
        raise ValueError(VALUES_MALFORMED.format(path=path, why="it is not an object"))
    rows = data.get("rows")
    shaped = isinstance(rows, list) and all(
        row is None
        or (
            isinstance(row, list)
            and len(row) == 2
            and all(isinstance(cell, str) for cell in row)
        )
        for row in rows
    )
    if not shaped:
        raise ValueError(
            VALUES_MALFORMED.format(
                path=path, why="`rows` is not a list of label and value pairs"
            )
        )
    return {**data, "rows": [None if row is None else tuple(row) for row in rows]}


def pending(directory):
    """The undrawn values files in `directory`, oldest first; empty where
    the directory does not exist."""
    try:
        names = os.listdir(directory)
    except OSError:
        return []
    return sorted(
        os.path.join(directory, name)
        for name in names
        if name.endswith(PENDING)
        and not name.endswith(DRAWN)
        and not name.startswith(".")
    )


def claim(path):
    """Mark `path` drawn by renaming it; the new path, or None where it was
    not there to rename — somebody else claimed it first.

    Called BEFORE anything is printed. Two drawers racing for one file both
    reach `os.replace` and only one finds it, so the file is drawn at most
    once; a crash between the rename and the print loses that one drawing
    rather than repeating it."""
    target = drawn_path(path)
    try:
        os.replace(path, target)
    except OSError:
        return None
    return target


def label(values):
    """The line said above a drawn stamp: what was sealed, and for which
    work item. The harness shows a hook message's first line as a dim label,
    so this is the line that must not be blank.

    A file carrying `branch` — every file since #666, `null` on a detached
    HEAD — gets `sealed_names`'s names and then ` · #<pr>` where the file
    names a pull request (#666). **A file without the key draws the label it
    always drew**, `SEALED <tree> against <base> · <item>`: a file an older
    gate wrote may still be pending when a newer hook draws it."""
    item = values.get("item")
    where = f" · {os.path.basename(os.path.normpath(item))}" if item else ""
    if "branch" not in values:
        return f"SEALED {values.get('tree')} against {values.get('base')}{where}"
    pr = values.get("pr")
    names = sealed_names(
        values.get("tree"), values.get("base"), values.get("branch"), values.get("from")
    )
    return f"SEALED {names}{f' · {pr}' if pr else ''}{where}"


# --- the stamp, queued at a sealed guarantee's commit or write -------------
#
# The owner's rule of 2026-10-18: the stamp means every party verified the
# work item, the sealer last, and the work is done. So it is drawn once per
# work item, from `guarantee.md` reading `sealed`, never from the broad
# gate's run. git's `post-commit` (`hooks/commitgate.py#post_commit`) runs
# after every judged commit, in the worktree the commit landed in, and calls
# `queue_for_guarantee`; the `Stop` hook draws what it queued. In local mode
# the edit gate calls `queue_for_local_guarantee` (below) instead.
#
# Once per work item is held by four facts the tree and the clone carry,
# and no count kept beside them: a values file whose name,
# `<ns>-<id>-<target sha>.json`, carries the work item's id, under any
# session's directory, pending or drawn, whatever commit it named; the
# audited commit standing in HEAD's history, so a squash or a cherry-pick of
# the guarantee elsewhere queues nothing; the guarantee reading `sealed` at
# an earlier commit of that history (`sealed_before`); and the `Target SHA`
# row's `; earlier run: <sha> <word>` chain — a `sealed` after a `sealed`
# was stamped at the first. The last two hold across clones. The chain skips
# one kind of entry, a `sealed` this clone recorded refusing
# (`refused_here`). In shared mode the commit gate writes that record when it
# refuses a `sealed` over a commit the history does not hold
# (`hooks/commitgate.py#guarantee_off_history`): the row never became
# history, and the sealer's new audit, which keeps it on its chain, draws the
# work item's one stamp. `sealed_before` skips nothing. A `sealed` in the
# history drew where it was made, or was committed where no gate judged it,
# and the history cannot tell the two apart, so it counts (#975
# `questions.md` Q8): a wrong row committed past the gate, or folded by an
# amend into the very commit it audited, which `pre-commit` cannot tell from
# a plain commit, leaves its work item with no stamp. A conflicted merge
# that brings in a side's `sealed` is refused, since the gate asks HEAD
# alone, and its way on is `--no-verify`; in this plugin's flow a conflict
# with the base is resolved before the sealer runs. A `sealed` committed
# over a history that carries no
# earlier `sealed` is caught by neither, so it queues again in a clone that
# holds no values file for the work item: the sealing commit amended or
# rewritten there over its own parent, or a second seal on a copy of the
# branch that had not fetched the first. Its row is the one just written.
# That is a stated limit (`questions.md` Q9): across clones the history is
# the only record read, and nothing beside the tree counts stamps. A
# `sealed` that drew in another clone, brought onto a copy of its declared
# branch that does not hold its audited commit (by hand, `checkout`,
# `cherry-pick -n` or `merge --squash`), refused by the gate and recorded,
# draws again at the new audit the refusal asks for, and joins it.

# A committed guarantee's path, in shared mode, where a commit carries it. A
# local-mode root sits under the git directory and no commit ever carries
# it, so `queue_for_local_guarantee` reads that one at its write instead.
GUARANTEE_PATH = re.compile(r"^seal/specs/([^/]+)/guarantee\.md$")
ROUND_FILE = re.compile(r"^round-\d+\.md$")
CHAIN_CHECK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "..",
    "code-review",
    "scripts",
    "chain_check.py",
)
# The line `post-commit` prints on stdout, which git prints into the commit
# command's output, and the edit gate prints as its message in local mode.
# It names the way to draw the stamp by hand, because the
# hook draws nothing, and says nothing, where it cannot: a `python3` that
# cannot load this file, a main session whose working directory is outside
# this clone, a plugin older than the hook (`docs/the-review-record.md`
# *The stamp*).
QUEUED = (
    "specseal: the stamp for {id} is drawn at the end of this turn from "
    "{path}; where none appears, `seal-stamp --from {command}` draws it"
)
# The line the local writer returns where its `guarantee.md` names a commit
# the work item's branch does not hold. No pull request's check reads a
# local guarantee, so this is the only place the wrong row is seen. It names
# no command: nothing was queued to draw.
NOT_ON_BRANCH = (
    "specseal: no stamp was queued for {id}: its guarantee.md names "
    "{target}, which {branch} does not hold; a new audit at the head of "
    "{branch} draws it"
)


def quote(path, windows=None):
    """`path` quoted for the shell a person types `seal-stamp --from` into:
    double quotes on Windows, `shlex.quote` elsewhere, so a checkout whose
    path holds a space prints a command that runs as printed.
    `broad_gate.quote` says why double quotes are `cmd.exe`'s."""
    if windows is None:
        windows = os.name == "nt"
    return f'"{path}"' if windows else shlex.quote(path)


def _git(cwd, *args):
    """stdout of a git call in `cwd`, or None on a non-zero exit."""
    r = subprocess.run(
        ["git", "-C", cwd, *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    return r.stdout if r.returncode == 0 else None


def _chain_check():
    """`chain_check.py`, whose readers of `guarantee.md` and `broad-gate.md`
    are the ones the pull request's check uses, so the row has one grammar."""
    spec = importlib.util.spec_from_file_location(
        "specseal_chain_check_for_the_stamp", CHAIN_CHECK
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def already_queued(common, ident):
    """True where a values file for work item `ident` stands under any
    session's directory of the clone, pending or drawn. A work item is
    stamped once (#975), whatever commit its guarantee audited, so the
    audited commit is not part of the question. A name is
    `<ns>-<ident>-<target>.json`; a file an older gate wrote is
    `<ns>-<tree>.json` and has no middle part to match."""
    root = os.path.join(common, VALUES_DIR)
    try:
        sessions = os.listdir(root)
    except OSError:
        return False
    for session in sessions:
        try:
            names = os.listdir(os.path.join(root, session))
        except OSError:
            continue
        for name in names:
            parts = name.split("-")
            if (
                len(parts) == 3
                and parts[1] == ident
                and name.endswith((PENDING, DRAWN))
            ):
                return True
    return False


def guarantee_rows(target, branch, base, ident, run, rounds):
    """The stamp's rows for a sealed guarantee (#975, `questions.md` Q1's
    answer (a)): what the records at the commit say and nothing measured
    again — the title, the audited commit with the branch under it, the
    base, the work item's id, a blank, then the newest run `broad-gate.md`
    names and the count of round records. A row whose record is absent is
    left out; `rounds` reads `0` where the work item had none."""
    rows = [TITLE_ROW, ("tree", fit(target))]
    if branch:
        rows.append(("", fit(branch)))
    if base:
        rows.append(("base", fit(base, keep="tail")))
    rows += [("item", ident), None]
    if run:
        rows.append(("gate", fit(f"{TICK}{run}")))
    rows.append(("rounds", str(rounds)))
    return rows


def queue_for_guarantee(top, common, session, now=None):
    """The lines `post-commit` prints for the commit at HEAD of `top`: one
    per work item whose `guarantee.md` the commit touched, reads one
    `Verdict:` of `sealed`, carries no earlier run reading `sealed`, read
    no `sealed` at an earlier commit of HEAD's history, has no values file
    in the clone already, and audited a commit in HEAD's history. Each
    writes one values file for `session` under `common` first. An earlier
    run on the row whose `sealed` the commit gate refused in this clone does
    not count (`refused_here`); a `sealed` in the history always does, as
    the once comment above says. Nothing here writes a record. Raises
    whatever reading or writing raises; the caller is silent on every
    failure."""
    touched = _git(
        top, "diff-tree", "--no-commit-id", "--name-only", "-r", "--root", "HEAD"
    )
    items = [
        found.group(1)
        for path in (touched or "").splitlines()
        for found in [GUARANTEE_PATH.match(path.strip())]
        if found
    ]
    if not items:
        return []
    chain = _chain_check()
    said = []
    for name in items:
        line = _queue_one(chain, top, common, session, name, now)
        if line:
            said.append(line)
    return said


def sealed_before(chain, top, path):
    """True where `path` read one `Verdict:` of `sealed` at a commit before
    HEAD in HEAD's history, whatever that verdict's `Target SHA` named. That
    commit was stamped where it was made, in this clone or another, so what
    the history carries holds across clones, a rebase among them, and asks
    nothing of the row an agent writes. The history cannot tell such a
    `sealed` from one committed where no gate judged it, over a commit the
    branch does not hold, so that one counts too, and its work item draws no
    stamp (#975 round 5, `questions.md` Q8). A row the commit gate refused
    never entered the history, so no refusal record is asked here. A root
    commit has no parent: `git log` exits 128 and the history is empty."""
    reader = chain.SHARED_READER
    for sha in (_git(top, "log", "--format=%H", "HEAD^", "--", path) or "").split():
        text = _git(top, "show", f"{sha}:{path}")
        if text is None:
            continue
        verdicts = chain.verdicts_of(reader, text)
        if len(verdicts) == 1 and chain.verdict_word(verdicts[0][1]) == chain.SEALED:
            return True
    return False


# --- a `sealed` this clone refused (work item 1792363231) -------------------
#
# `questions.md` Q2 of work item 1792363231, answered (b). A `sealed` over a
# commit the work item's branch does not hold drew nothing. The sealer's new
# audit keeps it on its row as `; earlier run: <sha> sealed`, and without a
# record of the refusal the chain readers count that entry as the stamp, so
# the repair draws nothing either. Two writers leave the record, each for a
# row that stands in its own clone and nowhere else: the commit gate, for a
# row it refused before it was history (`hooks/commitgate.py#pre_commit`),
# and the local writer, under a root that never leaves its clone. Each mode's
# chain reader skips a `sealed` the record names. Nothing infers a record
# after the fact, so nothing asks ancestry at read time, which is what
# #975's rounds 3 to 6 kept regressing on.

REFUSED_DIR = "specseal-stamp-refused"
# The shortest SHA a record is matched on; shorter spellings find none.
SHORTEST_SHA = 7


def _same_commit(one, other):
    """Whether two spellings of a SHA name one commit as far as the text
    can tell: each at least `SHORTEST_SHA` long and one a prefix of the
    other, case aside."""
    one, other = (one or "").lower(), (other or "").lower()
    if min(len(one), len(other)) < SHORTEST_SHA:
        return False
    return one.startswith(other) or other.startswith(one)


def record_refusal(common, ident, target):
    """Record that this clone refused work item `ident`'s `sealed` over
    `target` and drew nothing for it: an empty file
    `<common>/specseal-stamp-refused/<ident>-<target>`, written by the
    commit gate at its refusal and by the local writer at its branch
    refusal. Beside `VALUES_DIR` and not in it, so neither `pending`,
    `already_queued` nor the `Stop` hook lists it. Per clone, not per
    session, because the refused row stands in this clone alone. A record
    that cannot be written is skipped, and that verdict then counts as
    stamped, which is #975 Q8's direction."""
    directory = os.path.join(common, REFUSED_DIR)
    try:
        os.makedirs(directory, exist_ok=True)
        with open(os.path.join(directory, f"{ident}-{target}"), "w", encoding="utf-8"):
            pass
    except OSError:
        pass


def refused_here(common, ident, sha):
    """True where this clone recorded refusing work item `ident`'s `sealed`
    over a target `_same_commit` matches with `sha`. Asked by the chain
    readers alone, `_queue_one`'s and the local writer's, of each earlier
    run reading `sealed`."""
    try:
        names = os.listdir(os.path.join(common, REFUSED_DIR))
    except OSError:
        return False
    for name in names:
        owner, _, recorded = name.partition("-")
        if owner == ident and _same_commit(recorded, sha):
            return True
    return False


def _queue_one(chain, top, common, session, name, now):
    """The line for one work item's guarantee, or None where it queues
    nothing (`queue_for_guarantee` says when)."""
    reader = chain.SHARED_READER
    rel = f"seal/specs/{name}"
    text = _git(top, "show", f"HEAD:{rel}/guarantee.md")
    if text is None:
        return None
    verdicts = chain.verdicts_of(reader, text)
    if len(verdicts) != 1 or chain.verdict_word(verdicts[0][1]) != chain.SEALED:
        return None
    target = chain.target_of(reader, text)
    if target is None:
        return None
    rows = chain.table_rows(reader, reader.readable(text))
    cell = reader.visible(chain.field(rows, chain.TARGET) or "")
    ident = item_value(name)
    if any(
        word == chain.SEALED and not refused_here(common, ident, sha)
        for sha, word in chain.earlier_verdicts(cell)
    ):
        return None
    if sealed_before(chain, top, f"{rel}/guarantee.md"):
        return None
    if already_queued(common, ident):
        return None
    # The audited commit is in this commit's history. A squash or a
    # cherry-pick of the guarantee onto another branch, in this clone or
    # another, carries a verdict that was stamped where it was made.
    # Precondition: `target` resolves in this clone; where it does not,
    # `merge-base` exits 128 and nothing is queued.
    if _git(top, "merge-base", "--is-ancestor", target, "HEAD") is None:
        return None
    gate_text = _git(top, "show", f"HEAD:{rel}/{chain.BROAD_GATE_FILE}")
    listed = _git(top, "ls-tree", "--name-only", "HEAD", f"{rel}/rounds/") or ""
    branch = (_git(top, "symbolic-ref", "--short", "-q", "HEAD") or "").strip()
    return _queue_values(
        chain,
        common,
        session,
        now,
        ident=ident,
        target=target,
        cell=cell,
        gate_text=gate_text,
        rounds=listed.splitlines(),
        branch=branch,
        item=os.path.join(top, *rel.split("/")),
    )


def _queue_values(
    chain, common, session, now, *, ident, target, cell, gate_text, rounds, branch, item
):
    """Write one work item's stamp for `session` under `common` and return
    the line that names it. Both writers call it once a guarantee has passed
    their refusals, each having read the records its own way: `_queue_one`
    from the commit, `queue_for_local_guarantee` from disk. `cell` is the
    `Target SHA` row, `gate_text` the `broad-gate.md` beside the guarantee or
    None, `rounds` the paths of what its `rounds/` holds and `branch` the
    branch the audited commit stands on, or "" where none is named."""
    reader = chain.SHARED_READER
    key = f"{ident}-{target}"
    newest = chain.EMPHASIS.sub("", cell.split(chain.EARLIER_RUN)[0]).split()
    base = newest[2] if len(newest) >= 3 and newest[1] == "against" else None
    run = chain.newest_run(reader, gate_text) if gate_text else None
    count = sum(1 for path in rounds if ROUND_FILE.match(os.path.basename(path)))
    values = {
        "tree": target,
        "base": base,
        "from": None,
        "branch": branch or None,
        "pr": None,
        "item": item,
        "session": session or None,
        "rows": guarantee_rows(target, branch, base, ident, run, count),
    }
    path = write_values(common, session, values, now=now, key=key)
    return QUEUED.format(id=ident, path=path, command=quote(path))


def _read(path):
    """The text of `path`, or None where it cannot be read."""
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except (OSError, ValueError):
        return None


def queue_for_local_guarantee(path, session, now=None):
    """The lines a write of the local-mode `guarantee.md` at `path` says:
    one where it queued the work item's stamp for `session`, one where its
    audited commit is off the work item's branch, else none.

    A local-mode root sits under the git common dir and no commit carries
    it, so this reads the file from disk where `queue_for_guarantee` reads
    a commit. `path` must be `<common>/seal/specs/<id>/guarantee.md`, where
    `<common>` is the repository's git common dir and `seal/` under it is
    the repository's root (`optin.home_at`): a repository with
    `<repo>/seal/` is shared mode, whose stamp the commit queues. It then
    queues where the file reads one `Verdict:` of `sealed`, its `Target SHA`
    row names a commit and carries no earlier run reading `sealed`, the
    clone holds no values file for the work item, and the audited commit is
    an ancestor of the branch the work item's `routing.md` names in its
    `Branch` row. No history is read, because a local root has none, and
    none is needed: the root and the values files share the common dir, so
    a values file for the id, pending or drawn, is a complete record of the
    work item's stamp in this clone. The branch is what keeps a `sealed`
    written long ago quiet, since `settle` retires no local-mode work item.
    Where the branch stands and does not hold the audited commit, the
    refusal is recorded (`record_refusal`) and the one line returned is
    `NOT_ON_BRANCH`; a branch that is gone or unnamed says nothing.
    Raises whatever reading the records or writing the values raises; the
    caller is silent on every failure."""
    real = os.path.realpath(path)
    item = os.path.dirname(real)
    specs = os.path.dirname(item)
    seal = os.path.dirname(specs)
    common = os.path.dirname(seal)
    names = (os.path.basename(real), os.path.basename(specs), os.path.basename(seal))
    if names != ("guarantee.md", "specs", "seal"):
        return []
    # The main worktree, which `git worktree list` names first; "" where
    # `common` is no git directory, and `git_common_dir("")` is "".
    listed = _git(common, "worktree", "list", "--porcelain") or ""
    root = listed.split("\n", 1)[0].partition("worktree ")[2]
    chain = _chain_check()
    routing = chain.load(chain.ROUTING, "specseal_routing_for_the_stamp")
    found = routing.optin.git_common_dir(root)
    if not found or os.path.realpath(found) != common:
        return []
    home = routing.optin.home_at(root, found)
    if not home or os.path.realpath(home) != seal:
        return []
    with open(real, encoding="utf-8") as handle:
        text = handle.read()
    reader = chain.SHARED_READER
    verdicts = chain.verdicts_of(reader, text)
    if len(verdicts) != 1 or chain.verdict_word(verdicts[0][1]) != chain.SEALED:
        return []
    target = chain.target_of(reader, text)
    if target is None:
        return []
    rows = chain.table_rows(reader, reader.readable(text))
    cell = reader.visible(chain.field(rows, chain.TARGET) or "")
    ident = item_value(item)
    if any(
        word == chain.SEALED and not refused_here(common, ident, sha)
        for sha, word in chain.earlier_verdicts(cell)
    ):
        return []
    if already_queued(common, ident):
        return []
    declared = routing.parse(_read(os.path.join(item, routing.FILENAME)) or "")
    branch = (declared or {}).get("branch")
    if not branch:
        return []
    # Precondition: `target` and the branch resolve in this clone; where
    # either does not, `merge-base` exits 128 and nothing is queued. Where
    # the branch stands, the refusal is recorded and said. No guard
    # applies: a local root never leaves its clone, so `already_queued`
    # above already says whether the work item was stamped.
    ref = f"refs/heads/{branch}"
    if _git(common, "merge-base", "--is-ancestor", target, ref) is None:
        if _git(common, "rev-parse", "--verify", "-q", ref) is None:
            return []
        record_refusal(common, ident, target)
        return [NOT_ON_BRANCH.format(id=ident, target=target, branch=branch)]
    try:
        rounds = os.listdir(os.path.join(item, "rounds"))
    except OSError:
        rounds = []
    line = _queue_values(
        chain,
        common,
        session,
        now,
        ident=ident,
        target=target,
        cell=cell,
        gate_text=_read(os.path.join(item, chain.BROAD_GATE_FILE)),
        rounds=rounds,
        branch=branch,
        item=item,
    )
    return [line]


# --- a person's command --------------------------------------------------

# Neutral values in the stamp's shape, so `seal-stamp` shows a person what a
# sealed guarantee's commit draws without one having been committed — every
# row `guarantee_rows` can return, the conditional ones included, in its
# order; a case in `tests/test_the_seal_is_taken_once_by_the_sealer.py`
# holds the labels against `guarantee_rows`'. Since #975 the stamp carries
# what the records say and no suite counts: those are the broad gate's
# report's, which the gate prints as text.
SAMPLE_ROWS = [
    ("SEALED", ""),
    ("tree", "c46fd2d"),
    ("", "feat/12-a-branch"),
    ("base", "1e2bed9"),
    ("item", "1799000000"),
    None,
    ("gate", "✓ c46fd2d"),
    ("rounds", "3"),
]


def main(argv=None, console_wants_letters=None):
    """`console_wants_letters` is `pick_shape` asked of stdout as the process
    found it. `__main__` asks before it reconfigures the streams, because
    `reconfigure` changes the one object `sys.stdout` and `sys.__stdout__`
    both name; a direct call may leave it to be asked here."""
    parser = argparse.ArgumentParser(
        prog="seal-stamp",
        description="Print the sealer's stamp — what the commit of a sealed "
        "guarantee draws.",
    )
    parser.add_argument(
        "--shape", action="store_true", help="the letter twin, whatever the console"
    )
    parser.add_argument(
        "--from",
        dest="values",
        default=None,
        metavar="FILE",
        help="draw a queued stamp's values file, once, instead of the sample",
    )
    args = parser.parse_args(argv)
    if console_wants_letters is None:
        console_wants_letters = pick_shape(sys.stdout)
    shape = args.shape or console_wants_letters
    try:
        if args.values is None:
            lines = stamp(SAMPLE_ROWS, shape=shape)
        else:
            lines = drawn_from(args.values, shape)
    except ValueError as refused:
        sys.stderr.write(str(refused) + "\n")
        return 2
    sys.stdout.write("\n" + "\n".join(lines) + "\n\n")
    return 0


def drawn_from(path, shape):
    """The lines for the values file at `path`, which is claimed before they
    are returned. Raises `ValueError`
    with a refusal for a file drawn already, unreadable, or out of shape —
    and every refusal comes before the claim, so a file refused for its
    content is still there to be drawn once it is repaired."""
    if path.endswith(DRAWN) or (
        not os.path.exists(path) and os.path.exists(drawn_path(path))
    ):
        # The drawn file's own name, where that is what was given:
        # `drawn_path` of it is `X.drawn.drawn.json`, which does not exist,
        # and this is the sentence a person recovers the values from (round
        # 1's 🟡 3).
        drawn = path if path.endswith(DRAWN) else drawn_path(path)
        raise ValueError(VALUES_DRAWN.format(path=path, drawn=drawn))
    values = read_values(path)
    lines = stamp(values["rows"], shape)
    if claim(path) is None:
        raise ValueError(VALUES_DRAWN.format(path=path, drawn=drawn_path(path)))
    return lines


if __name__ == "__main__":
    # Which form, asked of stdout as the process found it. It has to come
    # before the loop below: `reconfigure` puts the stream into UTF-8, and a
    # cp949 console asked afterwards would be handed the blocks it cannot draw.
    _letters = pick_shape(sys.stdout)
    # A console that cannot encode what this prints kills it with stdout
    # empty. `hooks/console.py` owns the reasoning and the three decisions
    # behind these lines.
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main(console_wants_letters=_letters))

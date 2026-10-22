"""The seal is taken once, by the sealer, and this is what it prints.

Issue #30. Part 1 pins the stamp module, `skills/verify/scripts/seal_stamp.py`:
the disc is computed and the disc's mark placed on it from one hand-drawn
chart, so it cannot be off centre; a letter twin exists for a console that cannot draw
half-blocks, and it has the block form's footprint; colour is emitted at transitions, never per cell; the panel beside
the disc is data; the disc has one size; and the failure form carries no
drawing at all, because a picture that says *sealed* beside a word that says
*not* is the two-things-disagreeing defect this repository keeps paying for.

Part 2 holds the cases about the gate command that read a document's prose,
which #923 places. The gate's own cases, `skills/verify/scripts/broad_gate.py`
one class per function, are `tests/test_broad_gate.py` since #942.

Part 3 pins the agent and the owner sentences.
"""

import ast
import hashlib
import io
import math
import os
import re
import subprocess
import sys

import pytest
from conftest import load_module
from test_the_agent_contract_holds_the_universal_rules import HEADING

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "skills", "verify", "scripts", "seal_stamp.py")
WRAPPER = os.path.join(ROOT, "bin", "seal-stamp")
GATE = os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py")
RECORDER_SOURCE = os.path.join(
    ROOT, "skills", "verify", "scripts", "pytest_record", "specseal_pytest_record.py"
)

# The shape `broad_gate.panel` returns since #832: a heading row and `(label,
# value)` pairs, `""` labelling a row that continues the one above, the
# base's ref beside its commit, and one `None` before the result rows. A file
# in an older shape is drawn by the hook's cases in
# `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`. Values are
# neutral.
ROWS = [
    ("SEALED", ""),
    ("tree", "c46fd2d"),
    ("", "feat/12-a-branch"),
    ("base", "1e2bed9  origin/base"),
    None,
    ("suite", "✓ 768 passed · 1 skipped"),
    ("ledger", "✓ 187 ok · 0 drifted · 0 broken"),
    ("chain", "✓ exit 0"),
    ("rounds", "4"),
]

SGR = re.compile(r"\x1b\[[0-9;]*m")
HALF_BLOCKS = ("▀", "▄")


def module():
    return load_module(SCRIPT, "specseal_seal_stamp")


def gate_module():
    return load_module(GATE, "specseal_broad_gate_for_tests")


def wrapper_command(wrapper, args, windows=None):
    """The argv that runs one of `bin/`'s wrapper pairs on this platform.

    `windows` is the platform, defaulting to this one, so BOTH branches can
    be driven from a case on either machine — the lesson round 2's 🟡 14
    landed, applied to the thing that failed CI instead of to a unit.

    `bin/seal-stamp` and `bin/broad-gate` open `#!/usr/bin/env sh`, and a
    shebang is a POSIX kernel's convention: `CreateProcess` reads the file as
    an image and answers *[WinError 193] %1 is not a valid Win32
    application*. Both files ship with a `.cmd` twin for exactly this, and
    `tests/test_the_suite_has_a_command_that_is_cheap_twice.py` says why —
    *a new command means both files or it means one platform*. Running the
    twin through `%COMSPEC% /c` is what a person typing the bare name gets,
    so the cases below exercise the file that ships rather than stepping
    around it.
    """
    if windows is None:
        windows = os.name == "nt"
    if not windows:
        return [wrapper, *args]
    return [os.environ.get("COMSPEC", "cmd.exe"), "/c", f"{wrapper}.cmd", *args]


def run_wrapper(*args, env=None):
    return subprocess.run(
        wrapper_command(WRAPPER, args),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        cwd=ROOT,
    )


class Stream:
    """Just enough of a text stream for `pick_shape` to ask its two questions."""

    def __init__(self, encoding, tty):
        self.encoding = encoding
        self._tty = tty

    def isatty(self):
        return self._tty


# --- the twin --------------------------------------------------------------


def visible(line):
    """A line's width as a person sees it: colour codes removed and nothing
    else."""
    return len(SGR.sub("", line))


@pytest.mark.parametrize("disc", [True, False], ids=["with-its-disc", "no-disc"])
def test_the_twin_and_the_block_form_have_equal_width_and_height(disc):
    """S5. A twin that is a different size is a different drawing, and the
    reader on a cp949 console would be looking at something nobody measured.
    Compared row by row on visible width, with the disc and without it, the
    two rungs the hook can step between (#717's A10, #853). #832 took the
    sheet away, so there is no top edge to compare; the twin maps the
    owner's `·`, `✓`, `─` and `→` one character for one, which is what keeps
    the widths equal on the rows that carry them."""
    mod = module()
    blocks = mod.stamp(ROWS, shape=False, disc=disc)
    letters = mod.stamp(ROWS, shape=True, disc=disc)
    assert len(blocks) == len(letters), (
        f"{len(blocks)} block rows against {len(letters)} letter rows ({disc})"
    )
    widths = [(visible(b), visible(t)) for b, t in zip(blocks, letters, strict=True)]
    assert all(b == t for b, t in widths), (
        f"the twin's rows differ in width from the block form's: {widths}"
    )
    assert not any(SGR.search(line) for line in letters), (
        "the letter twin carries colour codes, which is the one thing the "
        "console it exists for cannot show"
    )
    assert not any(c in line for line in letters for c in HALF_BLOCKS), (
        "the letter twin still carries a half-block character"
    )


def test_the_disc_draws_the_same_bytes_in_every_process():
    """Round 1's 🟡 6. `shrink` resolved a tie between two chart colours with
    `max(set(ink), key=ink.count)`, and a set of strings iterates in an order
    that moves with PYTHONHASHSEED — so the same scale drew differently from
    one process to the next. Measured over five seeds at 0.75: two distinct
    renderings. There is one disc since #853, and it is held the same way.

    This module's opening argument is that four hand-typed discs were
    lopsided and a circle that is calculated cannot be off centre. A
    calculated circle that is not reproducible gives that argument back, and
    any case that pins its bytes flakes.

    Run in child processes, because the seed is fixed before the interpreter
    starts and cannot be changed from inside one."""
    script = (
        "import importlib.util, sys\n"
        f"spec = importlib.util.spec_from_file_location('s', {SCRIPT!r})\n"
        "mod = importlib.util.module_from_spec(spec)\n"
        "spec.loader.exec_module(mod)\n"
        f"sys.stdout.write(chr(10).join(mod.stamp({ROWS!r}, True)))\n"
    )
    seen = set()
    for seed in ("0", "1", "2", "12345", "99999"):
        env = dict(os.environ, PYTHONHASHSEED=seed)
        r = subprocess.run(
            [sys.executable, "-c", script],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            env=env,
            timeout=120,
        )
        assert r.returncode == 0, r.stderr
        seen.add(r.stdout)
    assert len(seen) == 1, f"{len(seen)} distinct discs across five hash seeds"


def test_the_disc_is_symmetric_because_it_is_computed():
    """#30 *How it is drawn*: four hand-typed discs were lopsided; a computed
    one cannot be. Every twin row has the same left and right margin."""
    mod = module()
    w, h, px = mod.build()
    for y in range(0, h, 2):
        line = mod.letter_row(mod.disc_cells(px, w, y))
        left = len(line) - len(line.lstrip())
        right = len(line) - len(line.rstrip())
        assert left == right, f"row {y}: {left} blank on the left, {right} on the right"


# --- the lean writer (#832 S11) --------------------------------------------

SGR_RUN = re.compile(r"\x1b\[[0-9;]*m\x1b\[")
RESET = "\x1b[0m"


def state_changes(cells):
    """How many SGRs `spec.md` S11 of work item 1791270164 says one line of
    `cells` writes, counted here from the cells rather than by the writer:
    one per cell whose `(foreground, background, style)` differs from what
    is set. An empty cell or a blank with no background shows no foreground
    and no style, so it keeps those as set — but not a background, which
    would paint it, so a blank after the disc is a change of background."""
    state, changes = (None, None, None), 0
    for char, fg, bg, style in cells:
        if char in (None, " "):
            assert bg is None, "a space carries a background"
            fg, style = state[0], state[2]
        if (fg, bg, style) != state:
            changes += 1
            state = (fg, bg, style)
    return changes


def what_a_terminal_shows(line):
    """`line` as a terminal reads it: each character with the foreground,
    the background and the intensity the SGRs before it left set. `32` sets
    the foreground to the terminal's own green, written `"green"` here."""
    fg = bg = weight = None
    shown = []
    for token in re.findall(r"\x1b\[[0-9;]*m|.", line):
        if not token.startswith("\x1b["):
            shown.append((token, fg, bg, weight))
            continue
        parts = token[2:-1].split(";")
        while parts:
            part = parts.pop(0)
            if part in ("38", "48"):
                rgb, parts = tuple(int(v) for v in parts[1:4]), parts[4:]
                fg, bg = (rgb, bg) if part == "38" else (fg, rgb)
            elif part == "0":
                fg = bg = weight = None
            elif part in ("1", "2"):
                weight = {"1": "bold", "2": "dim"}[part]
            elif part == "22":
                weight = None
            elif part in ("32", "39"):
                fg = "green" if part == "32" else None
            elif part == "49":
                bg = None
    return shown


def test_a_line_writes_one_sgr_per_change_and_no_reset_inside_it():
    """#832 S11, the owner's lean encoding (`frames.py#encode`): a code only
    where the foreground, the background or the style of the next visible
    cell differs from what is set; every part of one change in one SGR, so
    no two are adjacent, and no part twice in one; no reset inside a line,
    and `\\x1b[0m` closing a line that wrote a code. A blank keeps the
    foreground and the style as set and writes nothing, unless a background
    is still set from the disc, which it ends. Read over a real work item's stamp,
    with its disc and without (whose blank lines write nothing at all), and
    over the disc alone, against the count of changes taken from
    `compose`'s cells here.

    #30 *Output size* found a code per cell 282 KB for one seal; the
    writer before this one reset over every cell nothing covered. A real
    run's block with its label is held under 5,500 UTF-16 units: the owner's
    reference was 5,119 for rows of the same length."""
    mod, cases = module(), hook_cases()
    letter = mod.compose(cases.FULL_ROWS)
    lines = mod.stamp(cases.FULL_ROWS, shape=False)
    w, h, px = mod.build()
    alone = [mod.disc_cells(px, w, y) for y in range(0, h, 2)]
    bare = mod.compose(cases.FULL_ROWS, disc=False).cells
    assert [] in bare, "the block with no disc has no blank line to read"
    pairs = [
        *zip(letter.cells, lines, strict=True),
        *zip(bare, mod.stamp(cases.FULL_ROWS, disc=False), strict=True),
        *((cells, mod.colour_row(cells)) for cells in alone),
    ]
    for cells, line in pairs:
        assert not SGR_RUN.search(line), f"two SGRs side by side: {line!r}"
        body = line.removesuffix(RESET)
        assert RESET not in body, f"a reset inside a line: {line!r}"
        written = len(SGR.findall(body))
        assert written == state_changes(cells), (written, state_changes(cells), line)
        assert line.endswith(RESET) == (written > 0), line
        # And what a terminal shows is the cells: a blank paints nothing, and
        # every other character is in its cell's colours and style.
        shown = what_a_terminal_shows(body)
        assert len(shown) == len(cells), (len(shown), len(cells))
        for (char, fg, bg, style), seen in zip(cells, shown, strict=True):
            if char in (None, " "):
                assert seen[0] == " " and seen[2] is None, ("a painted blank", seen)
                continue
            colour = "green" if style == "green" else fg
            weight = style if style in ("bold", "dim") else None
            assert seen == (char, colour, bg, weight), (seen, (char, fg, bg, style))
        for found in SGR.finditer(body):
            parts = found.group(0)[2:-1].split(";")
            bare_parts = []
            while parts:
                part = parts.pop(0)
                if part in ("38", "48"):
                    parts = parts[4:]
                else:
                    bare_parts.append(part)
            assert len(bare_parts) == len(set(bare_parts)), found.group(0)
    label = mod.label(cases.full_values())
    size = len("\n".join([label, *lines]).encode("utf-16-le")) // 2
    assert size < 5500, size


@pytest.mark.parametrize("mark", ["✓", "·"])
def test_a_mark_leading_a_continuation_row_beside_the_disc_is_drawn_in_its_style(
    mark,
):
    """#832 S11. A `""` label is spaces, and a space keeps the foreground as
    set, so on a continuation row beside the disc the disc's last colour is
    still set when the value's mark is the first cell to change it. Each mark
    `text_lines` styles is drawn in its own style there: the `✓` green, the
    `·` dim. A `39` written after `32` in one SGR takes the green back off,
    and the terminal drew that tick in its own colour (round 1's 🟡 2)."""
    mod = module()
    rows = [
        ("SEALED", ""),
        ("tree", "aaa1111"),
        None,
        ("suite", "x"),
        ("", f"{mark} 3 passed"),
    ]
    letter = mod.compose(rows)
    marks = 0
    for cells, line in zip(letter.cells, mod.stamp(rows), strict=True):
        shown = what_a_terminal_shows(line.removesuffix(RESET))
        for (char, fg, bg, style), seen in zip(cells, shown, strict=True):
            if char != mark:
                continue
            marks += 1
            assert any(cell[1] in mod.KEY for cell in cells), "no disc on the row"
            colour = "green" if style == "green" else fg
            weight = style if style in ("bold", "dim") else None
            assert seen == (char, colour, bg, weight), (line, seen)
    assert marks == 1, marks


# --- the open layout: the disc at the left, the text at the right (#832) ----


HOOK_CASES = os.path.join(
    ROOT, "tests", "test_the_stamp_reaches_the_person_it_is_drawn_for.py"
)


def hook_cases():
    """The hook's case module, for its `FULL_ROWS` — `full_values()`'s rows,
    a real run's — and its four-row `SMALL_ROWS`, so the layout case reads
    the panels those cases draw rather than copies of them."""
    return load_module(HOOK_CASES, "specseal_hook_cases_for_their_rows")


# The disc's nine colours and the title's red as `spec.md` *Data &
# interfaces* of work item 1791270164 gives them — the owner's, from
# `seal28.py` and `frames.py` — written out so the cases below do not read
# them from the module they check.
WAX_EDGE, RIM_LIT, RIM_MID, RIM_DARK = (
    (150, 24, 28),
    (208, 68, 64),
    (160, 30, 34),
    (96, 10, 14),
)
FIELD, FACE, LIGHT, INNER, DROP = (
    (112, 16, 20),
    (186, 38, 42),
    (222, 86, 78),
    (90, 8, 12),
    (84, 8, 12),
)
NINE = (WAX_EDGE, RIM_LIT, RIM_MID, RIM_DARK, FIELD, FACE, LIGHT, INNER, DROP)
TITLE_RED = (196, 40, 44)
EMPTY = (None, None, None, None)


def owners_disc(chart, x, y):
    """The colour of the disc's cell `(x, y)` by the owner's rule, rebuilt
    here from the chart alone (`seal28.py#seal`): outside past 13.8 cells
    from the centre (13.5, 13.5); the wax edge past 12.8; the rim past 10.8,
    lit where `lit` is under -0.35, dark over 0.35, mid between; the groove
    past 9.8, dark where `lit` is under 0 and lit otherwise; then, in the
    field, the disc's mark's highlight, inner shadow or face, its drop
    shadow, or the field. `lit` is -1 at the upper left and +1 at the lower
    right."""

    def on(cx, cy):
        return 0 <= cx < 28 and 0 <= cy < 28 and chart[cy][cx] == "M"

    dx, dy = x - 13.5, y - 13.5
    d = math.hypot(dx, dy)
    lit = (dx + dy) / (abs(dx) + abs(dy))
    if d > 13.8:
        return None
    if d > 12.8:
        return WAX_EDGE
    if d > 10.8:
        return RIM_LIT if lit < -0.35 else RIM_DARK if lit > 0.35 else RIM_MID
    if d > 9.8:
        return RIM_DARK if lit < 0 else RIM_LIT
    if on(x, y):
        if not on(x - 1, y - 1):
            return LIGHT
        return INNER if not on(x + 1, y + 1) else FACE
    return DROP if on(x - 1, y - 1) else FIELD


def disc_cell(top, bottom):
    """One cell of the disc as `spec.md` *Data & interfaces* writes it."""
    if top and bottom:
        return ("▀", top, bottom, None)
    if top:
        return ("▀", top, None, None)
    if bottom:
        return ("▄", bottom, None, None)
    return EMPTY


def trimmed(cells):
    """`cells` without the blank cells at their end."""
    cells = list(cells)
    while cells and cells[-1][0] in (None, " ") and cells[-1][2] is None:
        cells.pop()
    return cells


@pytest.mark.parametrize(
    "which", ["FULL_ROWS", "SAMPLE_ROWS", "SMALL_ROWS", "OLD_ROWS", "none"]
)
def test_the_disc_stands_left_of_the_open_text_block_each_centred(which, monkeypatch):
    """#832 S3, the owner's layout of 2026-10-07 (`frames.py#design_open`).
    No parchment, no edge, no frame, and no background on any cell outside
    the disc. The disc stands at the left, 28 columns and 14 lines; the text
    block begins `GAP` (3) columns right of it; each is centred on the
    taller one's height. A cell inside the circle is its colour on both
    halves, every other cell of the disc's columns is empty, and no line
    runs past its own last visible cell. The rule is rebuilt here and every
    cell of `compose` is compared with it, over a real run's panel, the
    sample's, the four-row panel whose text the disc outgrows, an older
    gate's long panel that outgrows the disc, and none."""
    mod, cases = module(), hook_cases()
    rows = {
        "FULL_ROWS": cases.FULL_ROWS,
        "SAMPLE_ROWS": mod.SAMPLE_ROWS,
        "SMALL_ROWS": cases.SMALL_ROWS,
        "OLD_ROWS": cases.OLD_ROWS,
        "none": [],
    }[which]
    n, disc_lines, gap = 28, 14, 3
    assert (n, disc_lines, gap) == (mod.DISC_CELLS, mod.DISC_LINES, mod.GAP)
    text = mod.text_lines(rows)
    height = max(len(text), disc_lines)
    top_disc, top_text = (height - disc_lines) // 2, (height - len(text)) // 2
    if which == "SMALL_ROWS":
        assert (height, top_text) == (14, 4), (height, top_text)
    if which == "OLD_ROWS":
        assert (height, top_disc) == (19, 2), (height, top_disc)
    letter = mod.compose(rows)
    assert (letter.height, letter.disc) == (height, (0, 2 * top_disc, n, n))
    assert len(letter.cells) == height
    for ln, line in enumerate(letter.cells):
        k = ln - top_disc
        if 0 <= k < disc_lines:
            want = [
                disc_cell(
                    owners_disc(mod.CHART, x, 2 * k),
                    owners_disc(mod.CHART, x, 2 * k + 1),
                )
                for x in range(n)
            ]
        else:
            want = [EMPTY] * n
        t = ln - top_text
        if 0 <= t < len(text) and text[t]:
            want += [EMPTY] * gap + text[t]
        assert line == trimmed(want), (which, ln)
        for cell in line:
            if cell[0] not in HALF_BLOCKS:
                assert cell[2] is None, ("a background outside the circle", ln, cell)
    assert letter.width == max(len(line) for line in letter.cells)
    # With no disc, the rung `fitted` steps down to, the block stands at
    # column 0 and sets the height alone.
    bare = mod.compose(rows, disc=False)
    assert bare.disc is None and bare.height == len(text)
    assert bare.cells == [trimmed(line) for line in text]
    if text:
        assert letter.width == n + gap + max(len(line) for line in text)
        # `GAP` is the clear columns between the disc and the text, nothing else.
        monkeypatch.setattr(mod, "GAP", 0)
        assert mod.compose(rows).width == letter.width - gap


def test_the_letter_is_written_in_its_four_codes_and_the_discs_five_colours():
    """#832 S4a, the colours on the wire, read off the encoded lines. The
    only colour parts are truecolour over exactly the nine triples of
    `DISC_COLOURS` and the title's red; every other part is a style or a
    return to the terminal's own — `1`, `2`, `22`, `32`, `39`, `49` — and
    the line's closing `0`. No 256-colour part is left with the sheet, and
    nothing of the rope, the gold, the 24-cell rim's ends, the lily or the
    14-cell disc. The name still says four codes and five colours, the
    sheet's and the 14-cell disc's, because a released ledger row cites it."""
    mod = module()
    lines = mod.stamp(mod.SAMPLE_ROWS, shape=False)
    text = "\n".join(lines)
    triples, others = set(), set()
    for found in re.finditer(r"\x1b\[([0-9;]*)m", text):
        parts = found.group(1).split(";")
        while parts:
            part = parts.pop(0)
            if part in ("38", "48"):
                assert parts[0] == "2", found.group(0)
                triples.add(tuple(int(v) for v in parts[1:4]))
                parts = parts[4:]
            else:
                others.add(part)
    assert mod.DISC_COLOURS == NINE, mod.DISC_COLOURS
    assert mod.TITLE_RED == TITLE_RED
    assert triples == set(NINE) | {TITLE_RED}, triples
    assert others == {"0", "1", "2", "22", "32", "39", "49"}, others
    assert ";5;" not in text
    assert text.index("\x1b[1;38;2;196;40;44mSEALED") >= 0
    for gone in (
        "ROPE_L",
        "ROPE_D",
        "WAX_L",
        "GOLD",
        "LILY_FACE",
        "LILY_LIGHT",
        "LILY_SHADOW",
        "RIM_LIGHT",
        "EMBLEM_D",
        "WAX_M",
        "MARK",
        "MARK_SHADOW",
        "PARCHMENT",
        "SHEET_EDGE",
        "INK",
        "TITLE",
    ):
        assert not hasattr(mod, gone), gone
    for old in (
        (232, 226, 196),
        (168, 158, 122),
        (206, 46, 48),
        (200, 150, 30),
        (226, 82, 74),
        (214, 70, 66),
        (104, 12, 16),
        (168, 26, 30),
        (120, 16, 20),
        (240, 130, 118),
    ):
        assert ";".join(map(str, old)) not in text, old


def test_the_title_is_the_sheets_first_line_whatever_a_value_says():
    """Round 1's ⬜ 5. The title's colour was keyed on a line READING
    `SEALED`, so a continuation row carrying that value — a branch named
    `SEALED` — was inked as a second title. It is keyed on the panel's first
    row: since #832 that row is `text_lines`' first line, bold in the seal's
    red, and no other line carries the red or the bold, whatever it says. A
    panel without that first row draws no title. The name keeps the sheet,
    which #832 retired, because a released ledger row cites it."""
    mod = module()
    rows = [("SEALED", ""), ("tree", "aaa1111"), ("", "SEALED"), ("rounds", "2")]
    lines = mod.text_lines(rows)
    titled = [k for k, line in enumerate(lines) if any(c[1] == TITLE_RED for c in line)]
    assert titled == [0], titled
    assert not any(c[3] == "bold" for line in lines[1:] for c in line), lines
    assert "".join(c[0] for c in lines[3]).endswith("SEALED"), lines[3]
    untitled = mod.text_lines(rows[1:])
    assert not any(c[1] or c[3] == "bold" for line in untitled for c in line)
    # The title row is `("SEALED", "")` exactly: a first row that says more is
    # a row, and a first row that is a blank is a blank.
    valued = mod.text_lines([("SEALED", "v1.2.3"), ("tree", "aaa1111")])
    assert "".join(c[0] for c in valued[0]) == "SEALED  v1.2.3", valued[0]
    assert mod.text_lines([None, ("tree", "a")])[0] == []


def test_the_disc_is_lit_from_the_upper_left():
    """#832 S2a, the owner's frame of 2026-10-07: the rim is lit from the
    upper left in three steps and the groove inside it the other way, and
    the disc's mark is lit the same way — a highlight where the cell up-left
    is not the mark, an inner shadow where the cell down-right is not, a
    drop shadow on the field cell down-right of it. Read from `build` by
    each cell's own geometry and the chart. `lit` is -1 at the upper left
    and +1 at the lower right."""
    mod = module()
    n = mod.DISC_CELLS
    c, r = (n - 1) / 2, n / 2

    def on(x, y):
        return 0 <= x < n and 0 <= y < n and mod.CHART[y][x] == "M"

    w, h, px = mod.build()
    seen = set()
    for y in range(h):
        for x in range(w):
            colour = px(x, y)
            dx, dy = x - c, y - c
            d, lit = math.hypot(dx, dy), (dx + dy) / (abs(dx) + abs(dy))
            if colour is None or d > r - mod.WAX_INSET:
                continue
            if d > r - mod.RIM_INSET:
                want = RIM_LIT if lit < -0.35 else RIM_DARK if lit > 0.35 else RIM_MID
            elif d > r - mod.GROOVE_INSET:
                want = RIM_DARK if lit < 0 else RIM_LIT
            elif on(x, y) and not on(x - 1, y - 1):
                want = LIGHT
            elif on(x, y):
                want = INNER if not on(x + 1, y + 1) else FACE
            else:
                want = DROP if on(x - 1, y - 1) else FIELD
            assert colour == want, (x, y, colour, want)
            seen.add(colour)
    assert {RIM_LIT, RIM_MID, RIM_DARK, LIGHT, INNER, DROP} <= seen, seen


def test_the_disc_is_twenty_eight_cells_in_the_frames_nine_colours():
    """#832 S2, the owner's frame of 2026-10-07. `build` returns 28 x 28,
    and every cell is exactly one of nine colours
    or nothing. The frame's counts, which no chart moves: 176 outside, 84
    of the wax edge, 98 lit, 30 mid and 96 dark over the rim and the groove,
    and 300 inside the groove — split over the field and the disc's mark by
    the rule in `spec.md` *Data & interfaces*, rebuilt here from the chart
    (`owners_disc`) and compared cell for cell. No count of the mark's own
    is pinned: the mark is a placeholder (#857)."""
    mod = module()
    assert (mod.DISC_CELLS, mod.DISC_LINES) == (28, 14)
    insets = (mod.EDGE_INSET, mod.WAX_INSET, mod.RIM_INSET, mod.GROOVE_INSET)
    assert (*insets, mod.LIT_AT) == (0.2, 1.2, 3.2, 4.2, 0.35)
    w, h, px = mod.build()
    assert (w, h) == (28, 28), (w, h)
    cells = [px(x, y) for y in range(h) for x in range(w)]
    frame = {c: cells.count(c) for c in (None, WAX_EDGE, RIM_LIT, RIM_MID, RIM_DARK)}
    assert list(frame.values()) == [176, 84, 98, 30, 96], frame
    assert sum(c in (FIELD, FACE, LIGHT, INNER, DROP) for c in cells) == 300
    for y in range(h):
        for x in range(w):
            assert px(x, y) == owners_disc(mod.CHART, x, y), (x, y)
    assert set(cells) - {None} == set(mod.DISC_COLOURS)
    for x, y in ((-1, 0), (0, -1), (28, 14), (14, 28)):
        assert px(x, y) is None, (x, y)


def test_the_disc_mark_is_one_chart_file_read_as_data(tmp_path):
    """#832 S1. The disc's mark is one file beside the module,
    `seal-mark.txt`: 28 lines of 28 characters over `.M`, read at import by
    `read_chart` with its encoding named, so changing the mark is changing
    that file alone (#857). Every `M` stands inside the groove, in the
    field. A file of another shape — 27 lines, a 29-character line, a
    character outside `.M`, an `M` outside the field — is refused with one
    sentence naming the path and the fault. Nothing here asserts which
    letter the chart draws."""
    mod = module()
    path = os.path.join(ROOT, "skills", "verify", "scripts", "seal-mark.txt")
    assert os.path.samefile(mod.CHART_PATH, path), mod.CHART_PATH
    with open(path, encoding="utf-8") as handle:
        lines = tuple(handle.read().splitlines())
    assert mod.CHART == lines == mod.read_chart(path)
    assert len(lines) == 28 and all(len(line) == 28 for line in lines)
    assert set("".join(lines)) <= set(".M")
    marked = [
        (x, y) for y, line in enumerate(lines) for x, ch in enumerate(line) if ch == "M"
    ]
    assert marked, "the chart marks nothing"
    for x, y in marked:
        assert math.hypot(x - 13.5, y - 13.5) <= 14 - mod.GROOVE_INSET, (x, y)
    on_the_rim = [list(line) for line in lines]
    on_the_rim[13][1] = "M"
    for name, chart, fault in (
        ("short", lines[:27], "27 lines"),
        ("wide", (lines[0] + ".", *lines[1:]), "line 1 is 29 characters"),
        ("stray", (lines[0][:-1] + "x", *lines[1:]), "line 1 carries 'x'"),
        ("rim", ["".join(line) for line in on_the_rim], "line 14 marks column 2"),
    ):
        broken = tmp_path / f"{name}.txt"
        broken.write_text("\n".join(chart) + "\n", encoding="utf-8")
        with pytest.raises(ValueError) as refused:
            mod.read_chart(str(broken))
        said = str(refused.value)
        assert said.startswith(f"seal-stamp: the disc's mark chart {broken} "), said
        assert fault in said and said.endswith("Nothing was drawn."), said
    copy = tmp_path / "copy.txt"
    copy.write_text("\n".join(lines) + "\n", encoding="utf-8")
    assert mod.read_chart(str(copy)) == lines
    # An editor that saves with a byte-order mark hands over the same chart;
    # read as plain UTF-8 the mark was a character of line 1, refused as a
    # 29-character line, which sent a person to look for a dot that is not
    # there (round 1's ⬜ 7).
    marked_copy = tmp_path / "bom.txt"
    marked_copy.write_text("\n".join(lines) + "\n", encoding="utf-8-sig")
    assert mod.read_chart(str(marked_copy)) == lines


def test_the_stamp_module_imports_with_pillow_blocked():
    """#832 S1: the disc and its chart are stdlib-only, because the gate, the
    hook and the command load this file where Pillow is absent."""
    script = (
        "import sys, importlib.util\n"
        "sys.modules['PIL'] = None\n"
        f"spec = importlib.util.spec_from_file_location('s', {SCRIPT!r})\n"
        "mod = importlib.util.module_from_spec(spec)\n"
        "spec.loader.exec_module(mod)\n"
        "mod.build()\n"
    )
    r = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True,
        encoding="utf-8",
        timeout=120,
    )
    assert r.returncode == 0, r.stderr


def test_the_twin_writes_the_discs_nine_letters_and_the_text_in_ascii():
    """#717's A10 for the characters, with #832's nine colours (S4). `KEY`
    gives each disc colour its letter — capitals lit, lower case shadow, `m`
    and `.` #30's for the wax and the field, `Y` and `y` #717's for the lit
    and the shadowed mark — and a half-block cell's letter is its top half's
    colour's, else its bottom's. The text is itself, with the owner's four
    characters mapped one for one (`·` `.`, `✓` `+`, `─` `-`, `→` `>`), so
    every twin line is ASCII and keeps the block form's footprint; an empty
    cell is a space."""
    mod = module()
    letters = {
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
    assert letters == mod.KEY, mod.KEY
    assert len(set(mod.KEY.values())) == 9, mod.KEY
    ascii_ = {"·": ".", "✓": "+", "─": "-", "→": ">"}
    assert ascii_ == mod.TWIN_ASCII, mod.TWIN_ASCII
    # The sample as it stood at 5623d728 carries all four of the owner's
    # characters; since #975 the stamp's own sample carries `✓` and `─` alone.
    letter = mod.compose(SAMPLE_AT_5623D728)
    twin = mod.stamp(SAMPLE_AT_5623D728, shape=True)
    seen = set()
    for line, said in zip(letter.cells, twin, strict=True):
        assert said.isascii(), said
        for cell, char in zip(line, said, strict=True):
            if cell[0] in HALF_BLOCKS:
                want = letters[cell[1]]
            elif cell[0] is None:
                want = " "
            else:
                want = ascii_.get(cell[0], cell[0])
            assert char == want, (cell, char)
            seen.add(char)
    assert set(letters.values()) | set("+->") <= seen, seen
    assert "2 deferred > #56" in "\n".join(twin)


@pytest.mark.parametrize("value", ["a▀b▄c", "▀", "▄ x"])
def test_a_half_block_in_a_value_is_text_in_the_twin(value):
    """#832 S4. A disc cell is a half-block in a disc colour; a value that
    carries `▀` or `▄` — a branch name may, since git allows UTF-8 in a ref,
    and `panel` puts the branch on a row — is text, written as itself, as
    the twin before #832 wrote every text cell. Keyed on the character
    alone, the twin looked up the text's foreground, None, and raised
    `KeyError` after the gate had written the cell (round 1's 🟡 5)."""
    mod = module()
    twin = mod.stamp([("SEALED", ""), ("tree", value)], shape=True)
    assert any(line.endswith(f"tree    {value}") for line in twin), twin


# --- the panel's text -------------------------------------------------------


def test_the_text_lines_are_a_red_title_a_rule_and_the_rows_under_it():
    """#832 S3a, the owner's text block of 2026-10-07. The panel's first row,
    `("SEALED", "")`, is the title: `SEALED ` bold in the seal's red, then a
    dim rule of thirty `─`, the owner's reference's own length. Then a blank
    line, then one line per row: the label padded to seven columns and a
    space, dim; the value in the terminal's own foreground, a leading `✓`
    green and a leading `·` dim. A `None` row is a blank line, and a `""`
    label stands its value under the value above it. The panel is data —
    `(label, value)` rows and `None` — so what the seal reports is a list the
    gate fills, not a string it formats."""
    mod, cases = module(), hook_cases()
    assert (mod.LABEL_WIDTH, mod.RULE_WIDTH) == (7, 30)
    title = [(ch, TITLE_RED, None, "bold") for ch in "SEALED "]
    title += [("─", None, None, "dim")] * 30
    for rows in (mod.SAMPLE_ROWS, cases.REFERENCE_ROWS, ROWS):
        lines = mod.text_lines(rows)
        assert lines[0] == title, lines[0]
        assert lines[1] == [] and len(lines) == 1 + len(rows), rows
        for row, line in zip(rows[1:], lines[2:], strict=True):
            if row is None:
                assert line == [], line
                continue
            label, value = row
            head = f"{label:<7} "
            assert "".join(c[0] for c in line) == head + value, (row, line)
            assert all(c[1:] == (None, None, "dim") for c in line[: len(head)])
            said = line[len(head) :]
            assert all(c[1:3] == (None, None) for c in said), said
            styles = [c[3] for c in said]
            first = (
                {"✓": "green", "·": "dim"}.get(value[:1]) if value[1:2] == " " else None
            )
            assert styles[:1] == [first], (row, styles)
            assert set(styles[1:]) <= {None}, (row, styles)
    # Only a mark followed by a space is a mark: `·x` and a bare `✓` are text.
    for value in ("·x", "✓", "✓x"):
        (line,) = mod.text_lines([("x", value)])
        assert [c[3] for c in line[8:]] == [None] * len(value), (value, line)
    # A `""` label puts its value in the column of the value above it.
    branch = ["".join(c[0] for c in line) for line in mod.text_lines(ROWS)][3]
    tree = ["".join(c[0] for c in line) for line in mod.text_lines(ROWS)][2]
    assert branch.index("feat/12-a-branch") == tree.index("c46fd2d") == 8


# --- the scale, retired (#853) ---------------------------------------------

# SHA-256, first sixteen hex digits, of what 5623d728's `seal_stamp.py` drew
# over `SAMPLE_ROWS` at its default scale, 0.90 — the block form, the letter
# twin, the text block with no disc — and of `fitted` over two blocks labelled
# `first` and `second` at three budgets: the default, room for both with
# their disc, and 50, under which the first is drawn alone with no disc.
# Captured with the scale-era call spelling before the first edit
# (`phases/phase-5.md` of 1791384158 holds the command).
DRAWN_AT_5623D728 = {
    "block": "4413e52ec47d938e",
    "letters": "6273c12623355d89",
    "no-disc": "15eb7013e91ac03c",
    "fitted-default": "fc1c76e9e55a1444",
    "fitted-two": "e0dcadd4a5a511c8",
    "fitted-alone-no-disc": "76f216e7da17dfb8",
}


# `seal_stamp.SAMPLE_ROWS` as it stood at 5623d728, the input the hashes
# below were drawn from.
SAMPLE_AT_5623D728 = [
    ("SEALED", ""),
    ("tree", "c46fd2d"),
    ("", "feat/12-a-branch"),
    ("base", "1e2bed9  origin/release/next"),
    ("item", "#34 · 1799000000"),
    ("gate", "tree 1.2.3"),
    None,
    ("suite", "✓ 768 passed · 1 skipped"),
    ("ledger", "✓ 187 ok · 0 drifted · 0 broken"),
    ("chain", "✓ exit 0"),
    ("CI also", "· 4 more steps"),
    ("rounds", "3 · capped"),
    ("", "2 deferred → #56"),
]


def test_the_stamp_draws_byte_for_byte_what_it_drew_at_the_default_scale():
    """S13 (#853). The disc had one size at every scale since #832, so taking
    the scale away moves no byte: `stamp` with the disc and without it, in
    both forms, and `fitted` stepping a block from its disc to the text block
    alone, draw what the module drew at 0.90 before #853. The rows are the
    sample's as it stood then, so the hashes measure the drawing alone."""
    mod = module()

    def h(text):
        return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]

    rows = SAMPLE_AT_5623D728
    one = "\n".join(["first", *mod.stamp(rows)])
    size = len(one.encode("utf-16-le")) // 2
    blocks = [("first", rows), ("second", rows)]
    drawn = {
        "block": h("\n".join(mod.stamp(rows))),
        "letters": h("\n".join(mod.stamp(rows, shape=True))),
        "no-disc": h("\n".join(mod.stamp(rows, disc=False))),
        "fitted-default": h(mod.fitted(blocks)),
        "fitted-two": h(mod.fitted(blocks, budget=2 * size + 10)),
        "fitted-alone-no-disc": h(mod.fitted(blocks, budget=50)),
    }
    assert drawn == DRAWN_AT_5623D728, drawn


def test_no_scale_is_left_to_ask_for():
    """S13 (#853). The band, its three refusals, the ladder, the default and
    `check_scale` are gone from the module; `seal-stamp --scale 0.9` is
    refused by its parser, exit 2 with nothing drawn, and so is `broad-gate
    --scale 0.9`, before anything runs; neither command's help names a
    scale."""
    mod = module()
    left = [name for name in vars(mod) if "SCALE" in name or name == "check_scale"]
    assert left == [], left
    out = run_wrapper("--shape", "--scale", "0.9")
    assert out.returncode == 2, f"exit {out.returncode}; stderr {out.stderr!r}"
    assert "unrecognized arguments: --scale" in out.stderr, out.stderr
    assert not out.stdout, out.stdout
    assert "scale" not in run_wrapper("--help").stdout
    gate = subprocess.run(
        [sys.executable, GATE, "--base", "x", "--scale", "0.9", "--root", ROOT],
        capture_output=True,
        encoding="utf-8",
        timeout=120,
        env={**os.environ, "SPECSEAL_BROAD_GATE_INVOKED_AS": GATE},
    )
    assert gate.returncode == 2, (gate.returncode, gate.stderr)
    assert "unrecognized arguments: --scale" in gate.stderr, gate.stderr


# --- the failure form ------------------------------------------------------


def test_the_failure_form_carries_no_disc_and_names_every_failure():
    """#30 *On failure*: no drawing. What a person needs then is which checks
    broke, and a 22-row picture pushes that off the screen. Since #975 the
    form is the gate's, under `BROAD GATE FAILED`, and never says `sealed`."""
    mod = module()
    failures = [
        ("suite", ["3 failed, 765 passed", "tests/test_x.py::test_y FAILED"]),
        ("chain", ["1 error"]),
    ]
    lines = gate_module().failed_form("c46fd2d", "1e2bed9", failures)
    text = "\n".join(lines)
    assert lines[0].startswith("BROAD GATE FAILED   "), lines[0]
    assert "SEALED" not in text.upper(), text
    assert "c46fd2d" in lines[0] and "1e2bed9" in lines[0], (
        "the failure form does not name the tree and the base"
    )
    assert not any(c in text for c in HALF_BLOCKS), "the failure form draws the disc"
    assert not SGR.search(text), "the failure form carries colour codes"
    twin = mod.stamp(ROWS, shape=True)
    crown = next(line.strip() for line in twin if line.strip())
    assert crown not in text, "the failure form carries the letter twin"
    for name, first_lines in failures:
        assert name in text, f"failing check {name!r} is not named"
        for line in first_lines:
            assert line in text, f"{name}'s line {line!r} is missing"


# --- which form ------------------------------------------------------------


@pytest.mark.parametrize(
    "stream, why",
    [
        (Stream("cp949", tty=True), "a console that cannot render half-blocks"),
        (Stream("utf-8", tty=False), "a pipe, where `seal-stamp` prints the twin"),
        (io.StringIO(), "a stream with no encoding and no terminal"),
    ],
)
def test_pick_shape_is_letters_off_a_utf8_terminal(stream, why):
    """S5 — the colour form is for a person's terminal. Blocks and colour are
    for a UTF-8 tty and nothing else. (#30's `spec.md` *Out* said the sealer's
    returned text carries the twin; since #400 it carries no drawing at all,
    because the gate asks `is_terminal` and draws nothing on a pipe.)"""
    assert module().pick_shape(stream) is True, why


class Raising(Stream):
    def isatty(self):
        raise ValueError("I/O operation on closed file")


@pytest.mark.parametrize(
    "stream, terminal",
    [
        (Stream("cp949", tty=True), True),
        (Stream("utf-8", tty=True), True),
        (Stream("utf-8", tty=False), False),
        (io.StringIO(), False),
        (Raising("utf-8", tty=True), False),
    ],
)
def test_is_terminal_asks_the_tty_and_not_the_encoding(stream, terminal):
    """#400. `pick_shape` folded *not a tty* and *not UTF-8* into one answer,
    and the gate needs them apart: a cp949 terminal has a person in front of
    it and gets letters, a UTF-8 pipe has nobody and gets nothing drawn. A
    stream whose `isatty` raises is a stream nobody is looking at."""
    assert module().is_terminal(stream) is terminal


def test_pick_shape_is_blocks_on_a_utf8_terminal():
    """The control: the one stream that gets the drawing."""
    assert module().pick_shape(Stream("UTF-8", tty=True)) is False


@pytest.mark.parametrize("wrapper", ["seal-stamp", "broad-gate"])
def test_a_wrapper_pair_is_run_through_the_twin_the_platform_can_execute(wrapper):
    """CI's `windows-latest` leg, red on two cases of this module: `OSError:
    [WinError 193] %1 is not a valid Win32 application`.

    Both go through a `bin/` wrapper that opens `#!/usr/bin/env sh`. A
    shebang is a POSIX kernel's convention; `CreateProcess` reads the file as
    an image and refuses it. The repair is not a skip — both files ship with
    a `.cmd` twin for exactly this, and
    `tests/test_the_suite_has_a_command_that_is_cheap_twice.py` states the
    rule: *a new command means both files or it means one platform*.

    Pinned on both branches from either machine, which is the point: a wrong
    wrapper chosen for a platform fails HERE rather than only on the runner.
    That is round 2's 🟡 14 lesson applied to the case rather than the unit —
    the platform is an argument, so the branch the build machine cannot run
    is still one a reviewer can turn red."""
    path = os.path.join(ROOT, "bin", wrapper)
    assert os.path.isfile(path), f"bin/{wrapper} missing"
    assert os.path.isfile(path + ".cmd"), f"bin/{wrapper}.cmd missing"

    assert wrapper_command(path, ["--shape"], windows=False) == [path, "--shape"], (
        "a POSIX machine no longer runs the extensionless file"
    )
    win = wrapper_command(path, ["--shape"], windows=True)
    assert win[0].lower().endswith("cmd.exe"), (
        "Windows runs the wrapper as an image rather than through the command "
        f"interpreter, which is `[WinError 193]` on a `#!` file: {win}"
    )
    assert win[1:] == ["/c", path + ".cmd", "--shape"], (
        "Windows does not reach the `.cmd` twin, which is the file it can "
        f"actually execute: {win}"
    )


def test_the_command_piped_prints_the_twin():
    """The wrapper, run the way an agent runs it — stdout a pipe. Letters, no
    colour, exit 0, and the panel beside the disc."""
    out = run_wrapper()
    assert out.returncode == 0, out.stderr
    assert not SGR.search(out.stdout), "a piped run carries colour codes"
    assert not any(c in out.stdout for c in HALF_BLOCKS), "a piped run drew half-blocks"
    assert "SEALED" in out.stdout and "rounds" in out.stdout, (
        "the panel is missing from the piped drawing"
    )
    assert out.stdout == run_wrapper("--shape").stdout, (
        "a pipe and `--shape` disagree about the twin"
    )


@pytest.mark.parametrize(
    "branch, ref, said",
    [
        ("feat/x", "origin/base", "feat/x @ aaa1111 against origin/base @ bbb2222"),
        (None, "origin/base", "aaa1111 against origin/base @ bbb2222"),
        ("feat/x", None, "feat/x @ aaa1111 against bbb2222"),
        ("feat/x", "bbb2222", "feat/x @ aaa1111 against bbb2222"),
        ("feat/x", "bbb2222" + "0" * 33, "feat/x @ aaa1111 against bbb2222"),
        ("feat/x", "bbb2", "feat/x @ aaa1111 against bbb2222"),
        # A branch whose name happens to begin the commit is still a branch:
        # only a ref spelled in hex is read as the commit itself.
        ("feat/x", "b", "feat/x @ aaa1111 against b @ bbb2222"),
        ("feat/x", "bbb-x", "feat/x @ aaa1111 against bbb-x @ bbb2222"),
    ],
)
def test_the_names_collapse_only_where_a_part_would_repeat(branch, ref, said):
    """S1's two collapses, at the composer all three lines share."""
    assert module().sealed_names("aaa1111", "bbb2222", branch, ref) == said


def test_the_item_row_is_the_id_alone_without_a_pull_request(tmp_path):
    """A7. `<id>` is the digits before the first `-` of the directory's name.
    `seal_stamp`'s since #975, which writes the stamp's `item` row too."""
    gate = module()
    item = str(tmp_path / "1790815615-the-seal-names-what-it-sealed")
    assert gate.item_value(item) == "1790815615"
    assert gate.item_value(str(tmp_path / "plain")) == "plain"


def test_the_sample_carries_every_row_the_stamp_can():
    """A16. `seal-stamp` with no arguments shows a person what a stamp
    draws, and it read `lint clean` from #400 to #666 because nothing held
    the two lists together. Since #975 the stamp is drawn from a sealed
    guarantee, so its labels, in order, are the labels `guarantee_rows`
    returns with every conditional row present."""
    mod = module()
    rows = mod.guarantee_rows(
        "c46fd2db", "feature", "1e2bed90", "1799000000", "c46fd2db", 3
    )
    labels = [None if row is None else row[0] for row in rows]
    sample = [None if row is None else row[0] for row in mod.SAMPLE_ROWS]
    assert sample == labels, (sample, labels)
    # #717's A19, positively: the sequence itself, so the two lists cannot
    # agree by losing the same row.
    assert labels == [
        "SEALED",
        "tree",
        "",
        "base",
        "item",
        None,
        "gate",
        "rounds",
    ], labels
    # And the sample's values are in the shapes `guarantee_rows` writes them in.
    for row, sample in zip(rows, mod.SAMPLE_ROWS, strict=True):
        if row is None:
            continue
        assert row[1].startswith("✓ ") == sample[1].startswith("✓ "), (row, sample)


# =============================================================================
# Part 2 — the gate's prose, left for #923
# =============================================================================

ROW = "Broad gate"


def read_document(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as handle:
        return handle.read()


def refusal_over(tmp_path, name, table):
    """`missing_row` over a config written literally, with no helper between
    the case and the bytes. Every fixture in this region is malformed on
    purpose, so a builder that assembled a well-formed table and checked it
    read back would swallow the subject (`plan.md` *Every fixture here is
    malformed on purpose*)."""
    home = tmp_path / name / "seal"
    home.mkdir(parents=True)
    (home / "config.md").write_text(table, encoding="utf-8")
    return gate_module().missing_row(str(home))


def test_the_template_documents_the_commented_row_sentence():
    """S7's other half (contract rule 14): the sentence a person reads is stated
    where `templates/config.md` states the fenced one."""
    root = os.path.join(os.path.dirname(__file__), "..")
    with open(os.path.join(root, "templates", "config.md"), encoding="utf-8") as f:
        text = " ".join(f.read().split())
    assert "A row inside an HTML comment that closes is not a row either" in text
    assert "the refusal quotes that line and says it is commented out" in text


def test_the_template_names_every_inline_html_kind_it_reads_as_before():
    """#673's S10 (contract rule 14). The sentence tells a person which contexts
    are read as before, and the walk is unsure after any inline raw HTML a
    line leaves open, not after a comment opener alone. Each opener a
    person might write is named, and the old list's narrower phrase is gone."""
    root = os.path.join(os.path.dirname(__file__), "..")
    with open(os.path.join(root, "templates", "config.md"), encoding="utf-8") as f:
        text = " ".join(f.read().split())
    assert "after inline HTML a line leaves open" in text
    for opener in ("<" + "!--", "<![CDATA[", "<?", "<!DOCTYPE"):
        assert f"`{opener}`" in text, opener
    assert "or a tag started in the middle of a line" in text
    assert "after a `<" + "!--` in the middle of a line" not in text


def test_the_documents_state_the_fence_rule_the_refusal_points_at(tmp_path):
    """contract rule 14: a fix that changes what a person sees documents
    it and pins it, in the same commit.

    Two documents and one pointer. `templates/config.md` is the one home of
    what this table's format allows, and the refusal sends the reader to a
    named section of it — so the section has to still be there, and it has to
    say the thing the refusal is about. `skills/config/SKILL.md` step 3 is
    the coordinate that INVITES the shape: it tells a session to copy a block
    carrying a fenced example row and used to name no position for it.
    """
    template = open(
        os.path.join(ROOT, "templates", "config.md"), encoding="utf-8"
    ).read()
    skill = open(
        os.path.join(ROOT, "skills", "config", "SKILL.md"), encoding="utf-8"
    ).read()
    said = refusal_over(
        tmp_path,
        "pointer",
        "| Item | Value |\n|---|---|\n| Mode | shared |\n"
        f"```\n| {ROW} | bin/test -q |\n```\n",
    )

    section = "### What is refused, and what stays allowed"
    assert section in template, (
        f"the refusal points at a section that is not there:\n{said}"
    )
    assert section.lstrip("# ") in said, said
    for claim in (
        "A table inside a code fence is an example of this format",
        "outside every fenced code block",
        "runs to the end of the file",
    ):
        assert claim in template, f"`templates/config.md` does not say: {claim}"
    assert "The copied block lands BELOW the live table" in skill, (
        "the instruction that produces the shape still names no position for "
        "the block it copies"
    )


def test_this_repositorys_own_config_is_answered_exactly_as_before(tmp_path):
    """A11. The file this work item is about is in this repository, and every
    sentence above is a sentence about somebody else's file.

    `seal/config.md` here carries a `Mode` row and a `Broad gate` row and
    nothing the reader will not take, so all three answers are the ones it
    had before this work item: the mode, the command as the row wrote it, and
    no refusal to build at all. Run before and after each phase.
    """
    module = gate_module()
    config = module.load(module.CONFIG_READER, "specseal_config_for_this_case")
    home = os.path.join(ROOT, "seal")
    text = open(os.path.join(home, "config.md"), encoding="utf-8").read()

    assert config.declared_mode(home) == ("mode", "shared"), config.declared_mode(home)
    assert config.config_table(text)[1] == [], (
        "a refusal is built from this repository's own config:\n"
        f"{config.config_table(text)[1]}"
    )
    command = module.broad_command(home)
    assert command and f"| {ROW} | {command} |" in text, (
        f"the command the gate reads is not the row as written:\n{command}"
    )
    assert module.not_as_written(home, command) is None, command
    # Phase 2's half of the same question. This file carries no backticks at
    # all, so the fence rule removes no line of it and every answer above is
    # the one it had before #429 — asserted rather than assumed, because
    # `fenced_row` is what the new refusal is built from.
    assert module.fenced_row(home) is None, module.fenced_row(home)
    assert "```" not in text and "~~~" not in text, (
        "this repository's own config grew a fence, and the assertions above "
        "stop being about a file that has none. Its header comment does carry "
        "single backticks, which open nothing: a fence is a run of three"
    )


def test_the_documents_name_the_line_that_says_to_commit_the_cell():
    """S2's documentation (contract rule 14). The orchestrator is told
    what to do with the line — the commit is the orchestrator's act. Since
    #969 the sealer sees none of the gate's lines and is told no line's
    wording (`tests/test_the_sealer_guarantees.py::TestDefinition`)."""
    orchestration = " ".join(
        read_document(os.path.join("skills", "code-review", "orchestration.md")).split()
    )
    assert (
        "the report's last line says `broad-gate.md` is written and not committed: "
        "CI reads HEAD, so commit it before you push"
    ) in orchestration


def test_the_documents_say_where_the_panel_now_carries_each_name():
    """S6 for the panel (contract rule 14). Each sentence that named a
    row the panel lost, or the `gate` row printing on every stamp, says what
    the panel prints now."""
    broad = " ".join(read_document(os.path.join("docs", "the-broad-gate.md")).split())
    assert (
        "the panel's `gate` row reads `tree <version>` wherever the copy that ran "
        "is not byte for byte the copy invoked"
    ) in broad
    assert "panel's `gate` row reads `tree <version>` or `plugin <version>`" not in (
        broad
    )
    verify = " ".join(
        read_document(os.path.join("skills", "verify", "orchestration.md")).split()
    )
    # #832's S5a: the ref stands beside the commit on the `base` row.
    assert "names the ref beside the commit on the `base` row" in verify
    assert "names the ref on the row under the commit" not in verify
    # Round 1's 🟡 4 and ⬜ 5: the third arm, which fires on every seal an
    # installed copy older than #666 redirects, because it hands over no
    # invoked path to compare against. The sealer describes no panel row
    # since it became the guarantor (#923), so the documents that do are read.
    assert (
        "or where the tree's copy ran with no invoked copy named to compare against"
    ) in broad
    item = "1790815615-the-seal-names-what-it-sealed-and-counts-only-the-steps-that-run"
    changelog = " ".join(
        read_document(os.path.join("seal", "specs", item, "changelog.md")).split()
    )
    assert "or where nothing told it which copy was invoked" in changelog
    source = read_document(os.path.join("skills", "verify", "scripts", "broad_gate.py"))
    above = source.split("GATE_REL = ", 1)[0][-1500:].splitlines()
    comment = " ".join(" ".join(line.lstrip("# ") for line in above).split())
    assert "or where no invoked copy was handed over to compare" in comment


def test_the_docstrings_describe_the_letter_and_the_rows_it_carries():
    """#717, S7 for the code's own prose (contract rule 14). The stamp
    module's docstring describes the letter and the twin's characters rather
    than a rope and golds; the gate's module docstring and `panel`'s row
    diagram list the rows the panel carries now; the comment above
    `SAMPLE_ROWS` says which rows left. #832, the owner's frame and layout
    of 2026-10-07: the disc at the left and the text beside it with nothing
    painted outside the disc, the disc's mark a chart in a file of its own,
    the twin's letters the nine colours', and nothing names the parchment
    sheet, the 14-cell disc's four colours, the vector source, the area
    sampler, the corner overhang, a fleur-de-lis, a chart of stitches or the
    interim ring."""
    stamp = " ".join(
        read_document(
            os.path.join("skills", "verify", "scripts", "seal_stamp.py")
        ).split()
    )
    assert (
        "Two things side by side on the terminal's own background, and nothing "
        "else: at the left a wax disc with the disc's mark pressed into it"
    ) in stamp
    assert "a 28 x 28 chart in `seal-mark.txt` beside this file, read as data" in stamp
    assert "every cell exactly one of nine colours" in stamp
    assert "`m` its wax edge, `M n N` its rim lit, mid and dark, `.` its field" in (
        stamp
    )
    assert "nothing outside the disc is painted" in stamp
    for gone in (
        "lower right corner",
        "`M n` the rim's",
        "EMBLEM_D",
        "by area",
        "hangs",
        "half on and half off",
        "LILY_",
        "RIM_LIGHT",
        "RING_INSET",
        "24 cells",
        "nearest",
        "14 cells across",
        "four colours",
        "against its right edge",
        "parchment sheet, with",
        "`m` the disc's ring",
        "PARCHMENT",
        "SHEET_EDGE",
        "TEXT_LEFT",
        "PANEL_WIDTH",
    ):
        assert gone not in stamp, gone
    assert "fleur-de-lis" not in stamp and "stitch" not in stamp
    assert "cell's centre" not in stamp and "INTERIM" not in stamp
    assert "`o O` rope" not in stamp and "the lily's golds" not in stamp
    assert "ledger" not in stamp
    assert "Since #717 there is no blank row in it, no `chain`" not in stamp
    gate = " ".join(
        read_document(
            os.path.join("skills", "verify", "scripts", "broad_gate.py")
        ).split()
    )
    # #832's S5a: the module docstring and `panel`'s row diagram name the
    # rows the owner's design of 2026-10-07 put back.
    assert (
        "the suite's counts, the chain's exit, how many more steps CI runs "
        "than this run answers"
    ) in gate
    assert "the ledger's `ok` count, how many more steps" not in gate
    assert "CI also · <n> more steps absent without a hygiene workflow" in gate
    assert "chain ✓ exit <code> read off the chain's own check" in gate
    assert "workflow <n> of <m> not answered" not in gate
    assert "**A drawn panel says only what a `SEALED` stamp can say** (#717)" not in (
        gate
    )
    assert "**The result rows carry a `✓`, and the blank before them is a row**" in (
        gate
    )
    assert "**Separators are ASCII**" not in gate
    assert "No row is `None` since #717" not in gate


def test_the_documents_name_the_ci_also_row():
    """#717, S7 for the rows (contract rule 14). `skills/verify/orchestration.md`
    *A run says what it did not answer* and `agents/sealer.md` named the
    `workflow` row and its `<n> of <total> not answered` reading; both name
    the `CI also` row and its `<n> more steps` now, and the denominator is
    said to be on the stderr line. #832's S5a: the row's value leads with a
    dim `·`, the owner's mark for a row that is not a pass, and the value
    column is 41 wide."""
    verify = " ".join(
        read_document(os.path.join("skills", "verify", "orchestration.md")).split()
    )
    assert "the panel carries a `CI also` row, *· <n> more steps*, and" in verify
    # #940: the document carried a count of the steps a feature branch's run
    # leaves unanswered, and it went stale when a step left the workflow. The
    # gate prints the count; the document states no copy of it.
    assert "A run on a SpecSeal feature branch reads `CI also ·" not in verify
    assert "A feature seal of" not in verify
    assert "value is 41 columns and a step name is a sentence" in verify
    assert "value is 23 columns" not in verify
    assert "the panel carries a `workflow` row" not in verify
    # The sealer sees no output of the gate's (#969) and names no panel row
    # (#923).
    assert "the `workflow` count" not in " ".join(sealer_text().split())


def test_the_unmeasured_word_says_so_and_every_reader_is_told_it():
    """A9 (#747, contract rule 14), S15 (#789), and S19 (#825). The three
    reasons are text a person reads and acts on, so they are pinned whole,
    and each starts with the word that marks it unmeasured; the five the
    record replaced are asserted gone. Every document that tells a reader
    what the gate's words mean names `new?` beside the other two, so a sealer
    handing it on and a smith reading it are both told it is not `new`."""
    gate = gate_module()
    assert gate.NOT_MEASURED == "new? not measured"
    earns = (
        "A row earns the measured word by letting every pytest it runs load "
        "the gate's recorder: it adds to the PYTHONPATH and PYTEST_ADDOPTS the "
        "gate hands it rather than replacing them, and runs pytest in that "
        "environment rather than one it builds, through any wrapper"
    )
    # #825 round 3's 🟡 3 and round 4's 🟡 3: every cause of a missing
    # record the records cannot tell apart, never one of them as the only one.
    causes = (
        "the row started no pytest, because a part before its runner failed "
        "or it has none; none it started loaded the recorder; or the one that "
        "did could not write its record and warned 'specseal_pytest_record: no "
        "record written' in "
    )
    assert (
        "new? not measured: no pytest the row ran here left a record of the "
        f"gate's recorder ({causes}suite.txt), so this file is named only by a "
        f"FAILED line of suite.txt and the base was not run. {earns}"
    ) == gate.NO_RECORD_AT_HEAD
    assert (
        "new? not measured: the row ran once at the base, and no pytest it ran "
        f"there left a record of the gate's recorder ({causes}suite-at-base.txt; "
        f"records/ is beside it). {earns}"
    ) == gate.NO_RECORD
    # The reframe's S27: what the record at `HEAD` left out is counted, and
    # the failure form says how many.
    assert gate.UNPLACED.format(count=1) == (
        "1 of the tests and collections the row's pytest reported had no file "
        "of their own and are in no list: a test a conftest or a plugin parents "
        "to the session or to a directory, a failed collection of the whole "
        "session, or a report a plugin built without its path (counted as "
        "unplaced on the end line of each record under records/)"
    )
    # #825 round 4's 🟡 2, the part its fix left: `new` from a base record
    # that left anything out is not measured.
    assert gate.UNPLACED_AT_BASE.format(count=2) == (
        "new? not measured: the row ran once at the base, and its sessions that "
        "ended non-zero left 2 of the tests and collections their pytest "
        "reported in no list, such as "
        "a test whose xdist worker died before any report of it arrived, so one "
        "of them may be this file's failure and whether the base fails it was "
        "not measured (kept as suite-at-base.txt, with records/ beside it)"
    )
    # #849 (#825 round 6's 🟡 1): `new` from a base one of whose sessions
    # stopped part-way is not measured either -- and #849 round 1's 🟡 1: a
    # session pytest stopped itself is one.
    # #852: the stops the `end` line now names are among the causes.
    assert gate.UNENDED_AT_BASE.format(count=1) == (
        "new? not measured: the row ran once at the base, and 1 of its pytest "
        "sessions stopped part-way, because the process died or the recorder "
        "stopped writing before the session's end line, or pytest stopped the "
        "session (an interrupt, pytest.exit(), -x or --maxfail, a plugin's "
        "stop) or ended it on an error of its own, so this file's tests there "
        "may not have finished and whether the base fails it was not measured "
        "(kept as suite-at-base.txt, with records/ beside it)"
    )
    # #849 round 1's 🟡 2: the same at `HEAD`, under the list.
    assert gate.UNENDED_HERE.format(count=1) == (
        "1 of the row's pytest sessions here stopped part-way, because the "
        "process died or the recorder stopped writing before the session's end "
        "line, or pytest stopped the session (an interrupt, pytest.exit(), -x "
        "or --maxfail, a plugin's stop) or ended it on an error of its own, so "
        "a test it stopped in may be in no list and the tests it never reached "
        "are in none (each session's record is under records/)"
    )
    # #869: a line of a keyed record that did not parse, at the base and
    # under the list at `HEAD`.
    assert gate.UNREAD_AT_BASE.format(count=1) == (
        "new? not measured: the row ran once at the base, and 1 of the lines "
        "in the records its pytest wrote there did not parse as the recorder's "
        "and each was passed over, so one may have held this file's failure "
        "and whether the base fails it was not measured (kept as "
        "suite-at-base.txt, with records/ beside it)"
    )
    assert gate.UNREAD_HERE.format(count=1) == (
        "1 of the lines in the records the row's pytest wrote here did not "
        "parse as the recorder's and each was passed over, so a failing test "
        "may be in no list and the suite's counts are not given (each "
        "session's record is under records/)"
    )
    with open(RECORDER_SOURCE, encoding="utf-8") as handle:
        assert "specseal_pytest_record: no record written" in handle.read()
    assert gate.NOT_REACHED.format(code=2) == (
        "new? not measured: the row ran once at the base and exited 2, and no "
        "pytest it ran there collected this file, so the run may have ended "
        "before reaching it and whether the base fails it was not measured "
        "(kept as suite-at-base.txt, with records/ beside it). A file the "
        "branch added reads this way wherever the base's own row already fails"
    )
    for retired in (
        "NO_RUNNER",
        "NOT_ENDED",
        "COLLECTED_BEYOND",
        "MULTI_RUNNER",
        "COMPANY",
        "row_prefixes",
        "report_counts",
        "proof_refused",
        "JUNIT_REPORT",
        "COLLECT_ONLY",
    ):
        assert not hasattr(gate, retired), f"broad_gate.py still carries {retired}"
    readers = {
        # #969: the orchestrator meets the gate's words now, not the sealer.
        ("skills", "code-review", "orchestration.md"): "`new?`",
        ("agents", "smith.md"): "`new?` means nothing at the base measured that file",
        ("skills", "verify", "orchestration.md"): "**New?**",
        ("README.md",): "new? → not measured at the base",
        ("README.ko.md",): "new? → base 에서 재지 못했다",
        ("templates", "config.md"): "each file reads `new?` with the reason",
    }
    for parts, phrase in readers.items():
        with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
            assert phrase in handle.read(), f"{'/'.join(parts)} does not name `new?`"
    # #825: the reader sent to the base by hand is told the three causes the
    # record leaves, and to open the one kept run and its records.
    with open(
        os.path.join(ROOT, "skills", "verify", "orchestration.md"), encoding="utf-8"
    ) as handle:
        bullet = " ".join(handle.read().split())
    for phrase in (
        # #825's reframe after round 3 and round 4's 🟡 3: every cause of a
        # missing record.
        "no pytest the `Broad gate` row ran left a record, because the row "
        "started no pytest, none it started loaded the gate's recorder, or the "
        "one that did could not write its record and warned in `suite.txt`, so "
        "the file is named only by a `FAILED` line and the base was not run",
        "no pytest the row ran at the base left a record, for any of those three "
        "causes, a part before the runner failing at the base among them",
        "A test with no file of its own is in no list at all, nor is a failed "
        "collection of the whole session or a report a plugin built without its "
        "path; the failure form says how many there were.",
        "the row's run at the base exited non-zero before any pytest collected "
        "the file, which is also how a file the branch added reads where the "
        "base's row already fails",
        "open the kept `suite-at-base.txt` and the `records/` beside it",
        # #825 round 5's 🟡 2: only a session of the base that ended non-zero.
        "or a session of the base that ended non-zero left tests or collections "
        "out of every list, a test whose xdist worker died in its setup among "
        "them, so the record cannot say the file passed.",
        # #849 (#825 round 6's 🟡 1): a session of the base with no end, and
        # #849 round 1's 🟡 1: one whose end shows pytest stopped it.
        # #852: one whose end line says pytest stopped it.
        "A session of the base that stopped part-way reads the same way: its "
        "record holds no `end` line, because the process died, which plain "
        "pytest does on a test that calls `os._exit`, or its recorder "
        "stopped writing; or its `end` line names a stop pytest made, which an "
        "interrupt, any `pytest.exit()`, `-x`, `--maxfail` and a plugin's stop "
        "all leave, or an exit outside 0, 1 and 5.",
        # #869: a line of the base's record that did not parse.
        "So does a base whose record holds a line that did not parse as the "
        "recorder's, which the gate counts and passes over.",
        # #849 round 1's 🟡 2 and #869: a session at `HEAD` that stopped
        # part-way, and a line of its record that did not parse.
        "Nor, where a session at `HEAD` stopped part-way, is the test it "
        "stopped in, nor a test named on a line of the record that did not "
        "parse; the failure form counts both too.",
        "how a row earns the measured word",
    ):
        assert phrase in bullet, f"the **New?** bullet does not carry: {phrase}"
    for gone in (
        "wrote the report the gate asked pytest for there",
        "the file's run alone ended without naming a failing test",
        "`collected-at-base-*.txt`",
        # One cause of a missing record named as the only one (#825 round 3).
        "row ran loaded the gate's recorder, so the file is named only",
        "no pytest the row ran at the base loaded the recorder",
        # Two causes named as though they were every one (#825 round 4).
        "for either of those causes",
        # Every base record's count, a green session's included (round 5).
        "or the base's record left tests or collections out of every list",
        # A missing `end` line named as the only stop (#849 round 1).
        "A session of the base that wrote no `end` line to its record reads "
        "the same way",
        # The stops read off the exit alone (#852).
        "as a `KeyboardInterrupt` or `pytest.exit()` in a test and xdist under "
        "`-x` give",
    ):
        assert gone not in bullet, f"the **New?** bullet still carries: {gone}"
    with open(GATE, encoding="utf-8") as handle:
        docstring = ast.get_docstring(ast.parse(handle.read()))
    assert "`new?` with the reason no run measured it" in docstring
    # The module docstring's paragraph on the comparison says how it measures
    # now, and no longer names the prefixes or the JUnit report.
    flat_doc = " ".join(docstring.split())
    assert "run the row there once, unchanged, with the recorder loaded again" in (
        flat_doc
    )
    assert "No line pytest printed decides a word" in flat_doc
    assert "running each prefix of the row" not in flat_doc
    assert "JUnit" not in flat_doc


def test_the_measurement_its_cost_and_its_limits_are_told_where_the_row_is_written():
    """S15 of #789 and S19 of #825 (contract rule 14). Rule 3 is the one home of
    how the gate measures a row at the base, what that costs, and which rows
    it cannot measure, so each sentence a reader acts on is pinned there, and
    every sentence of the mechanism #825 retired is asserted gone."""
    with open(os.path.join(ROOT, "templates", "config.md"), encoding="utf-8") as handle:
        text = handle.read()
    for sentence in (
        "| 3 | Every pytest the row runs keeps the environment the gate hands it |",
        "On a failing test the gate compares each failing file with the base "
        "from a record, never from what pytest printed.",
        "the recorder's directory first on `PYTHONPATH`, `-p "
        "specseal_pytest_record` appended to `PYTEST_ADDOPTS`, and a key made "
        "fresh for the run.",
        "A pytest a test starts, and an xdist worker, inherit no key and write "
        "nothing, so nothing a test prints or runs changes a word.",
        "**Then the row runs once more, unchanged, at the base** (nothing "
        "appended, no part cut, every part run as written)",
        "where no pytest at the base left a record (the row ended before it "
        "started one, none loaded the recorder, "
        "or the one that did could not write its record and warned in "
        "`suite-at-base.txt`), `new?`; where the "
        "base's record holds a failing test or a failed collection of the file, "
        "`failing on base too`; where it holds the file and nothing of it "
        "failed, `new`; where it does not hold the file and the row exited 0, "
        "`new`, because the row ran to its end and never collected the file; "
        "and where it does not hold the file and the row exited otherwise, "
        "`new?` naming the exit, because the run may have ended before reaching "
        "it; so a file the branch added reads `new?` wherever the base's row "
        "already fails.",
        "Where no pytest the row ran at `HEAD` left a record, for any of "
        "those causes, the files "
        "come from its `FAILED` lines, each file reads `new?` with the reason, "
        "and the base is not run; where one runner loaded it and another did "
        "not, the other's failures stay in `suite.txt` and out of the list.",
        # #825 round 4's 🟡 2, narrowed by round 5's: `new` from a base
        # session that ended non-zero and left anything out, and the limit.
        "Either `new` reads `new?` naming the count instead where a session of "
        "the base that ended non-zero left any test or collection out of every "
        "list, because one of them may be the file's failure: a test whose "
        "xdist worker died in its setup, before any report of it reached the "
        "controller, is one. A session that exited 0 failed nothing, so what it "
        "left out cannot be. One over-strictness is named rather than closed: a "
        "red session whose left-out reports all passed, such as a passing item "
        "a conftest parents to the session, still turns `new` into `new?`.",
        # #849 (#825 round 6's 🟡 1): a base session that stopped part-way,
        # #849 round 1's 🟡 1: one pytest stopped itself, and #852: the stop
        # read off the `end` line, which closes the two #849 left named.
        "Either `new` reads `new?` naming the count, too, where a session of "
        "the base stopped part-way, so the file's tests there may not have "
        "finished: it wrote no `end` line to its record, because its process "
        "died, as plain pytest does on a test that calls `os._exit` or "
        "segfaults, or its recorder stopped writing, a disk that filled among "
        "the causes; or its `end` line says pytest stopped it (an interrupt, "
        "`pytest.exit()` whatever code it chose, `-x` or `--maxfail`, a "
        "plugin's stop) or shows an exit other than 0, 1 and 5. Where a red "
        "session also left reports out, that count is the one named.",
        # #849 round 1's 🟡 2: the same stop at `HEAD`, counted.
        "The gate also says there how many sessions at `HEAD` stopped "
        "part-way, because the test such a session stopped in may be in no "
        "list.",
        "**The cost is one more run of the whole row, and only when the suite "
        "fails**, whatever the number of failing files.",
        "so a part after the runner that the branch's own run never reached, "
        "because `&&` stopped at its failing suite, runs at the base wherever "
        "the base's suite passes,",
        "So the runner may come first or last, and the order is the "
        "repository's trade: either way the row runs once, whole, at the base.",
        "**A row earns the measured word** by letting every pytest it runs load "
        "the recorder: it adds to the `PYTHONPATH` and `PYTEST_ADDOPTS` the "
        "gate hands it rather than replacing them, and runs pytest in that "
        "environment rather than in one it builds.",
        "A runner started by `tox`, `nox`, `env -i`, a container or a wrapper "
        "that rebuilds the environment without either variable writes no "
        "record, and so does a row that sets `PYTEST_ADDOPTS` to a value of its "
        "own; its files read `new?`.",
        # #825 round 1's 🟡 2: Q2's class, not its first instance.
        "A row that keeps `PYTEST_ADDOPTS` and loses `PYTHONPATH` fares worse "
        "(one that replaces `PYTHONPATH`, an interpreter run with `-I` or `-E`, "
        "a wrapper that passes `PYTEST_ADDOPTS` or `PYTEST_*` on and not "
        "`PYTHONPATH`): pytest cannot import the module the `-p` names and exits "
        "1 before any test runs, so the row fails at the gate.",
        "and passes `PYTHONPATH` on wherever `PYTEST_ADDOPTS` goes.",
        # #825's reframe after round 3 (S28): what a line names a file by,
        # and the two kinds of report the record leaves out.
        "The record names each file by the path pytest itself holds for the "
        "test or the collector, read in the process that holds it (an xdist "
        "worker too) and carried on the report, never by a name pytest made "
        "from that path, so a file outside the rootdir, a `--pyargs` module "
        "wherever Python imports it from and a collector a conftest builds are "
        "each named by their own path.",
        # #825 round 4: the session's failed collection, a crashed worker's
        # test, and the attribute a whole-report log carries.
        "It leaves three kinds of report out of every list, counts them on the "
        "record's `end` line, and the gate says how many under the failing "
        "files: a test with no file of its own, which a conftest "
        "or a plugin parents to the session or to a directory; a failed "
        "collection of the whole session, which is where pytest 7 lays a "
        "conftest's import error anywhere below the root; and a report "
        "that reached the recorder without its path, one a plugin built or "
        "rebuilt itself, unless the same xdist worker's last report was of the "
        "same test and not its teardown, as a test whose worker crashed in its "
        "body has; a report's node id alone never places it, because two tests "
        "can share one.",
        "so a plugin that writes reports whole, pytest-reportlog's "
        "`--report-log` among them, writes it into the row's own log while the "
        "gate measures the row.",
        "One limit is named rather than closed: a test written to append to the "
        "record file the recorder is writing, or to write a record of its own "
        "with the gate's key, can put a line into a keyed record |",
    ):
        assert sentence in text, f"rule 3 does not carry: {sentence}"
    for gone in (
        "The suite runner is a part of the row a cut can stop after",
        "until one writes that report",
        "--junitxml=<path>",
        "--collect-only",
        "A group of several failing files never earns",
        "The proof run",
        "proof run",
        "verbosity_test_cases",
        "#816 would mark",
        "until one prints pytest's summary line",
        "A runner with `-s` lets a test write to stderr",
        "One shape the gate cannot see through",
        "or reaches without the gate's environment**",
        "Two dependencies in one group whose counts cancel",
        "fewer tests than they fail one by one",
        "(`pytest -q tests`, `pytest -q tests/unit`)",
        # #825 round 1: one row of Q2's class named as though it were all of
        # it, and a forged record called the only way to the wrong word.
        "A row that replaces `PYTHONPATH` and keeps `PYTEST_ADDOPTS` fares",
        "and that is the one way to a wrong `failing on base too`",
        # #825 round 2: the refusal named by its path arguments alone, and
        # its files said to read `new?` wherever another runner recorded.
        "A pytest handed a path outside its rootdir — `-c` or `--rootdir` "
        "elsewhere, or a config file in one of its arguments' directories — "
        "names those files",
        "writes no record and its files read `new?`.",
        # #825's reframe after round 3: the refusal of a pytest naming files
        # outside its rootdir, and the limit that called it closed.
        "A pytest that names a file outside its rootdir",
        "so it writes no record, and its files are measured as a runner's",
        "builds a collector for a path no argument contains",
        "the refusals above close every branch",
        "no third way is known",
        # #825 round 3's 🟡 3: one cause of a missing record named as the only.
        "where no pytest at the base loaded the recorder, `new?`",
        "Where no pytest the row ran at `HEAD` loaded the recorder",
        # #825 round 4: two causes and two kinds named as though every one.
        "for either of those causes",
        "It leaves two kinds of report",
        # #825 round 5: the lookup by node id, and the count of every session.
        "unless an earlier report of the same test carried it",
        "where the base's record left any test or collection out of every list",
        # #849 round 1's 🟡 1: a missing `end` line named as the only stop.
        "where a session of the base wrote no `end` line to its record, because "
        "it stopped part-way",
        # #852: the stops read off the exit alone, and the two it left open,
        # which the `end` line's `stopped` closes.
        "a failed collection without `-x` and xdist under `-x` give",
        "Two stops are named rather than closed",
        "which leaves no file partly run only while each file's tests run together",
    ):
        assert gone not in text, f"rule 3 still carries: {gone}"


def test_what_a_line_names_a_file_by_is_told_where_each_reader_meets_it():
    """S28 (#825's reframe after round 3, contract rule 14). A line's path is
    the node's own, carried on the report, and never a name made from a
    node id and a rootdir. The comparison's docstring, the recorder's own
    and the changelog fragment each say so by their deciding sentence, and
    each sentence of the refusal the reframe retired is asserted gone."""
    gate = gate_module()
    docstring = " ".join(gate.compare_at_base.__doc__.split())
    assert (
        "Each line names its file by the path pytest holds for the test or the "
        "collector, carried on the report from the process that held it, and "
        "never by a name pytest made from that path"
    ) in docstring
    recorder = " ".join(
        read_document(
            os.path.join(
                "skills",
                "verify",
                "scripts",
                "pytest_record",
                "specseal_pytest_record.py",
            )
        ).split()
    )
    for sentence in (
        "A line's path is the node's own: `item.path` for a test, the module "
        "that COLLECTED it, and `collector.path` for a failed collection",
        "No path is ever made from a node id and a rootdir",
        "None of the three is written; each node is counted once on the `end` "
        "line, and the gate says the count under its list of failing files.",
        # #825 round 4: the session's failed collection, and the path an
        # earlier report of a node carried, reused for a crash report.
        "a failed collection of the session itself -- where pytest 7 lays a "
        "conftest's import error anywhere below the root",
        "unless the same xdist worker's last report was of the same node and "
        "not its teardown",
        "Never a lookup by node id alone: two nodes can share one",
        "`--report-log` writes what `pytest_report_to_serializable` returns",
        "it looks no module up and imports nothing but pytest",
    ):
        assert sentence in recorder, f"the recorder does not carry: {sentence}"
    item = "1791270161-the-broad-gate-reads-a-record-its-pytest-plugin-wrote"
    changelog = " ".join(
        read_document(os.path.join("seal", "specs", item, "changelog.md")).split()
    )
    for sentence in (
        "**Each failing file is named by the path pytest holds for it.**",
        "counted on the record's `end` line, and the gate says how many under "
        "the failing files.",
        "names every cause the gate cannot tell apart: the row started no "
        "pytest, none it started loaded the recorder, or the one that did could "
        "not write its record.",
        "whose xdist worker crashed in its body keeps the path its `setup` report "
        "carried from that same worker, so its failure counts; a crash is never "
        "placed by a node id two tests can share.",
        "`new?` naming a count, too, where the file would read `new` but a "
        "session of the base that ended non-zero left tests or collections out "
        "of every list",
        "A red session whose left-out reports all passed still gives `new?`: a "
        "known over-strictness.",
        "a row that writes `--report-log` finds it in that log while the gate "
        "measures it.",
    ):
        assert sentence in changelog, f"the changelog does not carry: {sentence}"
    for gone, text in (
        ("so it writes no record at all", docstring),
        ("the recorder's refusals close it", docstring),
        ("A path is the rootdir joined to `report.fspath`", recorder),
        ("therefore writes no record at all", recorder),
        ("an_argument_lies_outside_the_rootdir", recorder),
        ("find_spec", recorder),
        ("A pytest that names a file outside its rootdir writes no record", changelog),
        ("Such a row's files are not measured", changelog),
        ("where no pytest at the base loaded the recorder", changelog),
        ("Where no pytest of the row loaded the recorder at all", changelog),
        ("names both causes", changelog),
        # #825 round 5: the lookup by node id, and every session's count.
        ("an earlier report of the same node in the session carried", recorder),
        ("keeps the path its earlier reports carried", changelog),
        ("base's record left tests or collections out of every list", changelog),
    ):
        assert gone not in text, f"still carried: {gone}"


# =============================================================================
# Part 3 — the owner, and the fourth definition
# =============================================================================

# `agents/smith.md` and `agents/warden.md` each carried the rule with no owner
# in it: *the full suite is the orchestrator's*. #30 named the sealer in both.
# Both were written anew since (#957, #967) and name no runner: the run's
# owner moves from the sealer to the orchestrator in #969, and contract rule 2 is
# where a reader finds it. What each definition still owes is the coverage
# probe, in its own words. The warden's words are #985's absence rule: a
# claim that nothing catches a finding is a probe, named on the finding's
# `evidence: executed` line.
SEALER = os.path.join(ROOT, "agents", "sealer.md")
PROBE = {
    "smith.md": (
        "Asking whether the suite catches something is a coverage probe, a "
        "different act: run it over the module that should catch it and "
        "report it as a probe."
    ),
    "warden.md": (
        "A claim of absence, such as nothing in the suite catching this, is a "
        "probe: run it over the module that should catch it, report it as a "
        "probe, never as a seal, and name it on the finding's `evidence: "
        "executed` line."
    ),
}

# Contract rule 2 and contract rule 6, read from the contract rather than
# typed, so a rule that is rewritten (#120) is compared as it then stands.
CONTRACT = os.path.join(ROOT, "skills", "agent-contract", "SKILL.md")

# `tests/test_a_moved_rule_leaves_its_definition.py` measured this: 15 words is
# longer than any phrase a kept application shares with a section, and shorter
# than the smallest real paste. Imported as a number rather than a rule — the
# case below applies it to ONE definition, the one that talks about rule 2 by name
# and is therefore the one at risk of quoting it.
WINDOW = 15


def agent(name):
    with open(os.path.join(ROOT, "agents", name), encoding="utf-8") as handle:
        return " ".join(handle.read().split())


def sealer_text():
    with open(SEALER, encoding="utf-8") as handle:
        return handle.read()


def section(number):
    """The body of `## <N>` in the contract, heading excluded."""
    with open(CONTRACT, encoding="utf-8") as handle:
        text = handle.read()
    heads = list(HEADING.finditer(text))
    for index, match in enumerate(heads):
        if int(match.group(1)) != number:
            continue
        end = heads[index + 1].start() if index + 1 < len(heads) else len(text)
        return " ".join(text[match.end() : end].split())
    raise AssertionError(f"the contract has no rule {number}")


# --- S6 the owner ------------------------------------------------------------


@pytest.mark.parametrize("definition", sorted(PROBE))
def test_the_definition_separates_a_coverage_probe_from_a_seal(definition):
    """The near miss a rule against the full suite creates. *Does anything in
    the suite catch this* is answered by running the suite, and an agent that
    reads only *the full suite is not yours* either does not ask it or reports
    the answer as a seal. It is a probe: run it, and label it one."""
    assert PROBE[definition] in agent(definition), (
        f"agents/{definition} does not separate a coverage probe from a seal, "
        "so the one run that is not a seal has no name"
    )


def test_the_warden_says_what_comes_due():
    """The warden's report is what ends the rounds, so it is the one segment
    positioned to say the gate is next. Saying so without naming what is
    spawned leaves the orchestrator to remember the sealer exists."""
    warden = agent("warden.md")
    assert (
        "what comes due is the orchestrator's broad run, and the sealer's "
        "spawn after it"
    ) in " ".join(warden.split()), (
        "the warden says the broad run is next and does not say who takes it"
    )


# Every party that could be written in as the broad gate's runner. A runner
# named in the smith's definition is a sentence #969 makes false by moving the
# run, from a worktree that does not touch this file (`spec.md` decision 6 of
# work item 1792251842).
RUNNERS = ("sealer", "orchestrator", "warden", "framer", "scribe", "session", "owner")
# A sentence anywhere in the file that hands the run to somebody: a party, then
# a verb of taking it, then the run, inside one sentence.
HANDS_THE_RUN = re.compile(
    r"\b(?:" + "|".join(RUNNERS) + r")s?\b[^.]{0,60}?\b(?:takes?|runs?|owns?)\b"
    r"[^.]{0,40}?\b(?:broad gate|full suite)",
    re.I,
)


def test_the_smith_names_no_runner_of_the_broad_gate():
    """T4 of #967 (S5): the smith says it does not run the broad gate and
    names nobody who does; contract rule 2 holds who does.

    This replaced a case that asserted *Then the sealer takes the broad gate
    once*. #969 moves the run to the orchestrator in a worktree beside this
    one, so either owner written here is false in one of the two trees."""
    smith = agent("smith.md")
    start = smith.index("**The broad gate is not yours, and its label is.**")
    rule = smith[start : smith.index(" check: ", start)]
    assert "You do not run the full suite, the lint or the typecheck" in rule, (
        "the smith's gate rule stopped saying the run is not the smith's"
    )
    assert "rule 2 holds who does" in rule, (
        "the rule stopped pointing at where the runner is named"
    )
    named = [party for party in RUNNERS if re.search(rf"\b{party}", rule, re.I)]
    assert not named, f"the smith's gate rule names {named}: {rule}"
    handed = HANDS_THE_RUN.findall(smith)
    assert not handed, f"`agents/smith.md` hands the broad gate to somebody: {handed}"


# --- S7 the fourth definition ------------------------------------------------
#
# The contract paragraph this file opens with is held to byte identity by
# `tests/test_every_agent_reads_the_contract.py`, over a glob this file joins
# on the day it lands. Re-pinning it here would be the duplication that module
# and `tests/test_a_moved_rule_leaves_its_definition.py` exist to refuse, so
# what part 3 pins is what no existing module reads.


def test_the_fourth_definition_exists():
    assert os.path.exists(SEALER), "agents/sealer.md is not in the tree"


def test_the_sealer_preloads_the_contract_and_nothing_else():
    """Q5: its whole procedure is one command, and #292 measured every
    preloaded body as a cost paid again on every spawn. `verify` is 35 KB for
    four conditions the definition states in four lines."""
    head = sealer_text().split("\n---\n", 1)[0]
    assert re.findall(r"^  - (\S+)", head, re.M) == ["agent-contract"], (
        "the sealer's `skills:` list is not `agent-contract` alone, so a body "
        "rides every spawn for a procedure that is one command"
    )


def test_the_sealer_names_the_one_write_its_definition_is_allowed():
    """Contract rule 6 says what an agent writes is named in its own definition
    and nothing else, so this file is the whole of the sealer's permission. A
    write nobody named is a review that certifies itself.

    Before #120 the same case read `as its own exception`, because rule 6 carved
    exceptions and pointed at the definition holding each one. The mechanism
    did not move -- it stopped being the exception and became the rule -- so
    every assertion below is unchanged and only the name and the grounds are.

    Since the sealer became the guarantor (#923) its one write is
    `guarantee.md`, and `broad-gate.md` is the gate's, through its command."""
    text = " ".join(sealer_text().split())
    assert "rule 6" in text, "the sealer cannot reach the rule that names its one write"
    assert "through `broad-gate --record`" in text, (
        "the gate's file does not name the command that makes it, so the "
        "sealer cannot tell its own write from the gate's"
    )
    assert "`guarantee.md` is the whole of what you may write" in text, (
        "the permission does not say WHICH file, and a permission without a "
        "boundary is a general one"
    )


def test_the_sealer_leaves_s6s_withheld_acts_to_s6():
    """Round 1, finding 10 of #120 found the definition reciting contract
    rule 6's withheld acts one short and one over, and this case held the
    recitation to that rule's own list. #943 removed the recitation: rule 6
    binds every agent
    whatever its file says, and the copy cost the sealer's preload bytes its
    measurement refused (round 1 of #943).

    Rewritten rather than deleted, for the reason the case below gives: a
    case removed with the passage it pinned leaves nothing to notice the
    passage coming back. A recitation that returns is a second source beside
    a countable list, so the assertions invert."""
    text = " ".join(sealer_text().split())
    assert "rule 6 withholds stays withheld" not in text, (
        "the sealer recites rule 6's withheld acts again; rule 6 is their one source"
    )
    assert "nothing posted, nothing pushed" not in text, (
        "the sealer recites rule 6's withheld acts again; rule 6 is their one source"
    )


def test_the_window_the_sealer_shipped_under_is_closed():
    """#120 closed it, and this case is the one that says so.

    The sealer shipped under a contract rule 2 that forbade its one act, for a window
    inside one release branch, and its definition wrote the contradiction down
    rather than leaving the next reader to guess which document wins. That
    paragraph carried its own expiry -- *when #120 lands, this section is the
    paragraph it deletes* -- and #120 deleted it.

    Rewritten rather than deleted, and that is the point of it. A case removed
    with the paragraph it pinned leaves nothing to notice the paragraph coming
    back, and this one came with a ticket number in it, which is exactly the
    prose a later session restores while tidying. So the assertions invert:
    the window's own words are absent, and what the section was standing
    against is now a positive assignment.

    The two facts `spec.md` requires the definition to keep -- rule 6 and the one
    cell -- are asserted by
    `test_the_sealer_names_the_one_write_its_definition_is_allowed` above, which
    is where they belong; repeating them here would make two cases fail for one
    edit and neither of them say which."""
    text = " ".join(sealer_text().split())
    assert "narrower document" not in text, (
        "the window paragraph is back. It says the definition wins over the "
        "contract, which was true only while rule 2 forbade the sealer's one act"
    )
    assert "#120" not in text, (
        "the definition still names the ticket that was to settle rule 2. #120 "
        "has landed, so a reader following it finds a closed issue and no "
        "contradiction to match it against"
    )
    assert "rule 2 as it stands" not in text, "the section heading survived"
    assert "rule 2" in text, (
        "the definition stopped citing rule 2 altogether, so the sealer meets the "
        "rule that keeps the run out of its hands nowhere in its own file"
    )
    # #969 moved the run to the orchestrator: the positive assignment is now
    # contract rule 2's and the orchestration's, and the sealer's file says
    # whose it is.
    assert "spawned for exactly that" not in text, (
        "the sealer's assignment of the run is back beside a rule 2 that gives "
        "the run to no agent"
    )
    assert "the orchestrator runs it" in text, (
        "the definition says the run is not the sealer's without saying whose "
        "it is, which is #30's opening: an act nobody holds"
    )


def test_the_sealer_carries_the_four_conditions_in_its_own_words():
    """Q5 again, from the other side: dropping `verify` from the spawn is only
    correct if the conditions arrive some other way."""
    text = " ".join(sealer_text().split())
    for condition in (
        "Name the command before you run it",
        "show the check can fail",
        "Bind the result to a tree state",
        "`executed`",
        "`unverified`",
    ):
        assert condition in text, (
            f"the sealer's definition does not carry `{condition}`, and "
            "`verify` is not in its `skills:` list to carry it instead"
        )


@pytest.mark.parametrize("number", (2, 6))
def test_the_sealer_cites_the_section_without_carrying_it(number):
    """The sealer is the one definition that talks about contract rule 2 and
    contract rule 6 by name, so
    it is the one at risk of quoting them. Citing a number and saying what it
    means for this role is the application form; a run of the section's own
    words is the paste `tests/test_a_moved_rule_leaves_its_definition.py`
    measured, and that module holds the whole glob to it."""
    body = section(number).split()
    text = " ".join(sealer_text().split())
    copied = [
        " ".join(body[i : i + WINDOW])
        for i in range(len(body) - WINDOW + 1)
        if " ".join(body[i : i + WINDOW]) in text
    ]
    assert not copied, (
        f"agents/sealer.md carries contract rule {number}'s own words: {copied}"
    )

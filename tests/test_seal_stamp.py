"""`skills/verify/scripts/seal_stamp.py`, one class per function.

Rebuilt from the code by #942's phase 5. The drawing's units are driven with
rows and cells in the process, and the command with its own `main`, so no
shell runs under them but the one case that runs the command a person types.
The values files are written under a case's own directory. Git runs where the
module asks git: the shared writer over one repository built once for the
module and copied for each case, where a second common directory stands for a
second clone of it, and the local writer over one local-mode repository built
the same way.
"""

import ast
import collections
import hashlib
import io
import json
import math
import os
import pathlib
import re
import shutil
import subprocess
import sys

import pytest
from conftest import census_case, git, git_out, load_module, write
from conftest import commit_everything_as_e as commit

TARGET = "skills/verify/scripts/seal_stamp.py"

ROOT = pathlib.Path(__file__).resolve().parent.parent
GUARANTEE_TEMPLATE = ROOT / "templates" / "sdd-guarantee.md"
ITEM_NAME = "1799000000-an-item"
ITEM_ID = "1799000000"
GUARANTEE = f"seal/specs/{ITEM_NAME}/guarantee.md"
SIGNED = ("-c", "user.name=e", "-c", "user.email=e@example.com")

stamp = load_module(ROOT / TARGET, "seal_stamp_under_test")
chain = stamp._chain_check()

SGR = re.compile(r"\x1b\[[0-9;]*m")
HALF_BLOCKS = ("▀", "▄")
EMPTY = (None, None, None, None)

# The disc's nine colours and the title's red as the owner's `seal28.py` and
# `frames.py` give them (#832), written out so no case reads them from the
# module it checks.
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
LETTERS = {
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

# A panel in the gate's shape, with the result rows a real run carries.
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
# A panel whose text the disc outgrows, and one that outgrows the disc: the
# shape the gate wrote from #666 to #717, which a pending file may still carry.
SMALL_ROWS = [("SEALED", ""), ("tree", "aaa1111"), ("", "feat/x"), ("rounds", "2")]
TALL_ROWS = [
    ("SEALED", ""),
    None,
    ("tree", "aaa1111a"),
    ("", "feat/12-the-branch-n..."),
    ("base", "bbb2222b"),
    ("", "origin/release/v1.2.3"),
    ("item", "#12 . 1799000000"),
    ("gate", "tree 1.2.3"),
    None,
    ("suite", "6621 passed, 11 skipped"),
    ("", "exit 0"),
    ("ledger", "3451 ok"),
    ("", "0 drifted . 0 broken"),
    ("chain", "exit 0"),
    None,
    ("workflow", "4 of 9 not answered"),
    None,
    ("rounds", "2"),
]

# The rows the owner's chosen reference was drawn over (`frames.py`'s `ROWS`
# behind the title row), and the reference itself, chosen on 2026-10-07:
# design 3 of `frames.py` (`spec.md` decision 6 and S3 of work item
# 1791270164), transcribed from its SGR stream by a script that read no line of
# `seal_stamp.py`. The twin's lines, and the disc's twenty-eight half-rows,
# each half its colour's letter and a space off the disc.
REFERENCE_ROWS = [
    ("SEALED", ""),
    ("tree", "aaa1111a"),
    ("", "feat/12-the-branch-names-the-work-item"),
    ("base", "bbb2222b  origin/release/v1.2.3"),
    ("item", "#12 · 1799000000"),
    ("gate", "tree 1.2.3"),
    None,
    ("suite", "✓ 6621 passed · 11 skipped"),
    ("ledger", "✓ 3451 ok · 0 drifted · 0 broken"),
    ("chain", "✓ exit 0"),
    ("flow", "· 4 of 9 not answered"),
    ("rounds", "2"),
]
REFERENCE_TWIN = (
    "        mmmmmmmmmmmm           SEALED ------------------------------",
    "     mmmMMMMMMMMMMMMmmm",
    "   mmMMMMNNN....NNNnnnnmm      tree    aaa1111a",
    "  mmMMNN............NMnnmm             feat/12-the-branch-names-the-work-item",
    " mMMMN....YYxyyyXXYy..MnnNm    base    bbb2222b  origin/release/v1.2.3",
    "mmMMN....YXXy.....xy...MNNmm   item    #12 . 1799000000",
    "mMMN.....YXXXXYY...y....MNNm   gate    tree 1.2.3",
    "mMMN.......xxXXXXXX.....MNNm",
    "mMMNN....Y.....yXXXxy..MMNNm   suite   + 6621 passed . 11 skipped",
    " mMMN....YX......Yxxy..MNNm    ledger  + 3451 ok . 0 drifted . 0 broken",
    "  mnnNN..YyxxYYYYxyy.MMNNm     chain   + exit 0",
    "   mnnnMM..........MMNNNm      flow    . 4 of 9 not answered",
    "     mmnnNNMMMMMMNNNNmm        rounds  2",
    "        mmmNNNNNNmmm",
)
REFERENCE_DISC = (
    "           mmmmmm           ",
    "        mmmMMMMMMmmm        ",
    "      mmMMMMMMMMMMMMmm      ",
    "     mmMMMMNNNNNNMMnnmm     ",
    "    mMMMMNNN....NNNnnnnm    ",
    "   mMMMNN..........NNnnnm   ",
    "  mmMMNN............NMnnmm  ",
    "  mMMNN....YYYYYY.Y..MMnnm  ",
    " mMMMN....YYxyyyXXYy..MnnNm ",
    " mMMN....YYxyy...Xxy...MNNm ",
    " mMMN....YXXy.....xy...MNNm ",
    "mMMNN....YXXX.....Yy...MMNNm",
    "mMMN.....YXXXXYY...y....MNNm",
    "mMMN......XXXXXXXY......MNNm",
    "mMMN.......xxXXXXXX.....MNNm",
    "mMMN........yyxXXXXx....MNNm",
    "mMMNN....Y.....yXXXxy..MMNNm",
    " mMMN....Yy......XXxy..MNNm ",
    " mMMN....YX......Yxxy..MNNm ",
    " mMnnN...YXX....YYxyy.MNNNm ",
    "  mnnNN..YyxxYYYYxyy.MMNNm  ",
    "  mmnnMM..y.yyyyyyy.MMNNmm  ",
    "   mnnnMM..........MMNNNm   ",
    "    mnnnnMMM....MMMNNNNm    ",
    "     mmnnNNMMMMMMNNNNmm     ",
    "      mmNNNNNNNNNNNNmm      ",
    "        mmmNNNNNNmmm        ",
    "           mmmmmm           ",
)

# `SAMPLE_ROWS` as it stood at 5623d728, and SHA-256's first sixteen digits of
# what that commit's module drew over it at its default scale, 0.90: the block
# form, the twin, the text block with no disc, and `fitted` over two blocks at
# the default budget, at room for both, and at 50 (#853).
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
DRAWN_AT_5623D728 = {
    "block": "4413e52ec47d938e",
    "letters": "6273c12623355d89",
    "no-disc": "15eb7013e91ac03c",
    "fitted-default": "fc1c76e9e55a1444",
    "fitted-two": "e0dcadd4a5a511c8",
    "fitted-alone-no-disc": "76f216e7da17dfb8",
}


def owners_disc(chart, x, y):
    """The colour of the disc's cell `(x, y)` by the owner's rule
    (`seal28.py#seal`), rebuilt from the chart alone: off the disc past 13.8
    cells from the centre (13.5, 13.5), the wax edge past 12.8, the rim past
    10.8 lit, mid or dark by `lit`, the groove past 9.8 the other way, then
    the mark's highlight, inner shadow or face, its drop shadow, or the
    field. `lit` is -1 at the upper left and +1 at the lower right."""

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


def owners_cell(top, bottom):
    """One cell of the disc as `spec.md` *Data & interfaces* of work item
    1791270164 writes it."""
    if top and bottom:
        return ("▀", top, bottom, None)
    if top:
        return ("▀", top, None, None)
    if bottom:
        return ("▄", bottom, None, None)
    return EMPTY


def trimmed(cells):
    """CELLS without the blank cells at their end."""
    cells = list(cells)
    while cells and cells[-1][0] in (None, " ") and cells[-1][2] is None:
        cells.pop()
    return cells


def what_a_terminal_shows(line):
    """LINE as a terminal reads it: each character with the foreground, the
    background and the intensity the SGRs before it left set, `32` read as
    the terminal's own green."""
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


def state_changes(cells):
    """How many SGRs `spec.md` S11 of work item 1791270164 says CELLS write,
    counted from the cells: one per cell whose foreground, background or
    style differs from what is set, a blank keeping the foreground and the
    style as set but not a background."""
    state, changes = (None, None, None), 0
    for char, fg, bg, style in cells:
        if char in (None, " "):
            fg, style = state[0], state[2]
        if (fg, bg, style) != state:
            changes += 1
            state = (fg, bg, style)
    return changes


def as_shown(cell):
    """CELL as `what_a_terminal_shows` reads it back."""
    char, fg, bg, style = cell
    colour = "green" if style == "green" else fg
    return (char, colour, bg, style if style in ("bold", "dim") else None)


def drawn(label, rows, disc=True):
    """One block of a `Stop` message: LABEL, then the block form of ROWS."""
    return "\n".join([label, *stamp.stamp(rows, disc=disc)])


def values(**changed):
    """A values file's dict in the shape the writers write, with CHANGED."""
    written = {
        "tree": "aaa1111",
        "base": "bbb2222",
        "from": "origin/base",
        "branch": "feat/x",
        "pr": "#12",
        "item": f"/x/seal/specs/{ITEM_NAME}",
        "session": "s-1",
        "rows": SMALL_ROWS,
    }
    return {**written, **changed}


class Stream:
    """Just enough of a text stream for `pick_shape` to ask its two questions."""

    def __init__(self, encoding, tty):
        self.encoding = encoding
        self._tty = tty

    def isatty(self):
        return self._tty


class Raising(Stream):
    def isatty(self):
        raise ValueError("I/O operation on closed file")


# --- the module as a whole ------------------------------------------------------


class Test_module:
    def test_imports_nothing_outside_the_standard_library(self):
        """The disc and its chart are stdlib-only (#832 S1): the gate, the
        hook and the command load this file where Pillow is absent."""
        tree = ast.parse((ROOT / TARGET).read_text(encoding="utf-8"))
        names = {
            alias.name.split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        } | {
            node.module.split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom) and node.module
        }
        assert names and names <= set(sys.stdlib_module_names), names

    def test_the_budget_leaves_the_reserve_under_the_measured_limit(self):
        """The harness persists a message past 10,000 UTF-16 units, and the
        budget leaves room for the report `dispatch.py` prepends (#717)."""
        assert stamp.MESSAGE_LIMIT == 10000
        assert stamp.MESSAGE_BUDGET == stamp.MESSAGE_LIMIT - 1000

    def test_the_sample_carries_every_row_a_sealed_guarantee_draws(self):
        """`seal-stamp` with no arguments shows what a stamp draws, so its
        labels are `guarantee_rows`' with every conditional row present, in
        order, and each value in the shape that function writes it."""
        rows = stamp.guarantee_rows("c46fd2db", "feature", "1e2bed90", "1", "c46", 3)
        labels = [None if row is None else row[0] for row in rows]
        sample = [None if row is None else row[0] for row in stamp.SAMPLE_ROWS]
        assert (
            sample
            == labels
            == [
                "SEALED",
                "tree",
                "",
                "base",
                "item",
                None,
                "gate",
                "rounds",
            ]
        )
        for row, given in zip(rows, stamp.SAMPLE_ROWS, strict=True):
            if row is not None:
                assert row[1].startswith("✓ ") == given[1].startswith("✓ ")

    def test_accepts_the_command_a_person_types_on_a_pipe(self):
        """`bin/seal-stamp` with stdout a pipe draws the twin: the form is
        asked of the stream before `__main__` reconfigures it."""
        wrapper = ROOT / "bin" / "seal-stamp"
        command = (
            [os.environ.get("COMSPEC", "cmd.exe"), "/c", f"{wrapper}.cmd"]
            if os.name == "nt"
            else [str(wrapper)]
        )
        out = subprocess.run(
            command,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
        )
        assert out.returncode == 0, out.stderr
        assert out.stdout == "\n" + "\n".join(stamp.stamp(stamp.SAMPLE_ROWS, True)) + (
            "\n\n"
        )


# --- the disc ---------------------------------------------------------------------


class Test_read_chart:
    def test_accepts_the_shipped_chart_and_a_copy_saved_with_a_byte_order_mark(
        self, tmp_path
    ):
        path = ROOT / "skills" / "verify" / "scripts" / "seal-mark.txt"
        lines = tuple(path.read_text(encoding="utf-8").split("\n")[:28])
        assert stamp.CHART == lines == stamp.read_chart(str(path))
        assert os.path.samefile(stamp.CHART_PATH, path)
        marked = tmp_path / "bom.txt"
        marked.write_text("\n".join(lines) + "\n", encoding="utf-8-sig")
        assert stamp.read_chart(str(marked)) == lines

    @pytest.mark.parametrize(
        ("change", "fault"),
        [
            (lambda lines: lines[:27], "27 lines"),
            (lambda lines: [lines[0] + ".", *lines[1:]], "line 1 is 29 characters"),
            (lambda lines: [lines[0][:-1] + "x", *lines[1:]], "line 1 carries 'x'"),
            (
                lambda lines: [
                    *lines[:13],
                    lines[13][:1] + "M" + lines[13][2:],
                    *lines[14:],
                ],
                "line 14 marks column 2, outside the field",
            ),
        ],
        ids=["short", "wide", "stray", "on-the-rim"],
    )
    def test_refuses_a_chart_of_another_shape_naming_the_fault(
        self, tmp_path, change, fault
    ):
        broken = tmp_path / "broken.txt"
        broken.write_text("\n".join(change(list(stamp.CHART))) + "\n", encoding="utf-8")
        with pytest.raises(ValueError) as refused:
            stamp.read_chart(str(broken))
        assert str(refused.value) == (
            f"seal-stamp: the disc's mark chart {broken} is not 28 lines of 28 "
            f"characters over `.M` with every `M` inside the disc's field ({fault}). "
            "Nothing was drawn."
        )


class Test_build:
    def test_accepts_every_cell_by_the_owners_rule_in_the_frames_counts(self):
        """#832 S2: 28 x 28 cells, each one of nine colours or nothing, in the
        frame's counts no chart moves, and each the owner's rule's colour."""
        w, h, px = stamp.build()
        assert (w, h) == (28, 28)
        cells = [px(x, y) for y in range(h) for x in range(w)]
        frame = [cells.count(c) for c in (None, WAX_EDGE, RIM_LIT, RIM_MID, RIM_DARK)]
        assert frame == [176, 84, 98, 30, 96], frame
        assert set(cells) == {None, *NINE}
        for y in range(h):
            for x in range(w):
                assert px(x, y) == owners_disc(stamp.CHART, x, y), (x, y)

    def test_refuses_a_colour_off_the_grid(self):
        _w, _h, px = stamp.build()
        for x, y in ((-1, 0), (0, -1), (28, 14), (14, 28)):
            assert px(x, y) is None, (x, y)


class Test_disc_cell:
    def test_accepts_each_half_in_its_colour(self):
        assert stamp.disc_cell(FIELD, FACE) == ("▀", FIELD, FACE, None)
        assert stamp.disc_cell(FIELD, None) == ("▀", FIELD, None, None)
        assert stamp.disc_cell(None, FACE) == ("▄", FACE, None, None)

    def test_refuses_a_character_where_neither_half_is_on_the_disc(self):
        assert stamp.disc_cell(None, None) == EMPTY


class Test_disc_cells:
    def test_accepts_row_y_on_top_and_the_next_below(self):
        _w, _h, px = stamp.build()
        assert stamp.disc_cells(px, 28, 0) == [
            owners_cell(owners_disc(stamp.CHART, x, 0), owners_disc(stamp.CHART, x, 1))
            for x in range(28)
        ]

    def test_refuses_a_cell_past_the_last_half_row(self):
        _w, _h, px = stamp.build()
        assert stamp.disc_cells(px, 28, 28) == [EMPTY] * 28


# --- the two row writers ------------------------------------------------------------


class Test_colour_code:
    def test_accepts_a_triple_as_truecolour_on_either_ground(self):
        assert stamp.colour_code(38, (1, 2, 3)) == "38;2;1;2;3"
        assert stamp.colour_code(48, (1, 2, 3)) == "48;2;1;2;3"

    def test_refuses_a_colour_where_the_terminals_own_is_asked(self):
        assert stamp.colour_code(38, None) == "39"
        assert stamp.colour_code(48, None) == "49"


class Test_colour_row:
    def test_accepts_one_sgr_per_change_and_a_reset_only_at_the_end(self):
        """#832 S11: a code only where the next visible cell's foreground,
        background or style changes, no two side by side, no reset inside a
        line, and what a terminal shows is the cells, a blank painting
        nothing; read over the sample's lines with the disc and without."""
        rows = REFERENCE_ROWS
        lines = [*stamp.compose(rows).cells, *stamp.compose(rows, disc=False).cells]
        for cells in lines:
            line = stamp.colour_row(cells)
            body = line.removesuffix(stamp.RESET)
            assert not re.search(r"\x1b\[[0-9;]*m\x1b\[", line), line
            assert stamp.RESET not in body and line.endswith(stamp.RESET) == bool(
                SGR.search(body)
            ), line
            assert len(SGR.findall(body)) == state_changes(cells), line
            for code in SGR.findall(body):
                parts = re.sub(r"[34]8;2;\d+;\d+;\d+", "", code[2:-1]).split(";")
                parts = [part for part in parts if part]
                assert len(parts) == len(set(parts)), ("a part twice", code)
            shown = what_a_terminal_shows(body)
            assert len(shown) == len(cells)
            for cell, seen in zip(cells, shown, strict=True):
                if cell[0] in (None, " "):
                    assert seen[0] == " " and seen[2] is None, seen
                else:
                    assert seen == as_shown(cell), (seen, cell)

    @pytest.mark.parametrize("mark", ["✓", "·"])
    def test_refuses_to_take_a_marks_style_off_beside_the_disc(self, mark):
        """A `""` label is spaces, which keep the disc's colour set, so the
        mark is the first cell to change it: `32` with no `39` after it, and
        a dim `·` (round 1's 2 of #832)."""
        rows = [("SEALED", ""), ("tree", "a"), None, ("x", "y"), ("", f"{mark} 3")]
        seen = 0
        for cells in stamp.compose(rows).cells:
            shown = what_a_terminal_shows(stamp.colour_row(cells))
            for cell, said in zip(cells, shown, strict=False):
                if cell[0] == mark:
                    seen += 1
                    assert any(c[1] in LETTERS for c in cells), "no disc on the row"
                    assert said == as_shown(cell), (said, cell)
        assert seen == 1

    def test_refuses_a_code_and_a_reset_on_a_line_of_blanks(self):
        assert stamp.colour_row([EMPTY, (" ", None, None, None)]) == "  "
        assert stamp.colour_row([]) == ""


class Test_letter_row:
    def test_accepts_the_discs_letters_and_the_text_in_ascii(self):
        assert stamp.KEY == LETTERS
        assert stamp.TWIN_ASCII == {"·": ".", "✓": "+", "─": "-", "→": ">"}
        cells = [
            ("▀", RIM_LIT, FIELD, None),
            ("▄", DROP, None, None),
            EMPTY,
            *stamp.text_cells("✓ 1 · 2 ─ →"),
        ]
        assert stamp.letter_row(cells) == "My + 1 . 2 - >"

    @pytest.mark.parametrize("value", ["a▀b▄c", "▀", "▄ x"])
    def test_refuses_to_read_a_half_block_in_a_value_as_the_disc(self, value):
        """A branch may carry `▀`; it is text, written as itself (round 1's
        5 of #832, where the lookup raised `KeyError`)."""
        twin = stamp.stamp([("SEALED", ""), ("tree", value)], shape=True)
        assert any(line.endswith(f"tree    {value}") for line in twin), twin


class Test_strip_ansi:
    def test_accepts_a_line_with_its_codes_removed(self):
        assert stamp.strip_ansi("\x1b[1;38;2;1;2;3mA\x1b[0m b") == "A b"

    @pytest.mark.parametrize("text", ["[1m a ;m", "\x1b[2Ja", "\x1b[1;2H"])
    def test_refuses_to_touch_text_or_a_code_that_sets_no_colour(self, text):
        assert stamp.strip_ansi(text) == text


# --- the panel's text rules -----------------------------------------------------------


class Test_fit:
    def test_accepts_a_value_as_wide_as_the_panel_unchanged(self):
        value = "x" * stamp.PANEL_VALUE_WIDTH
        assert stamp.fit(value) == value
        assert stamp.fit(12) == "12"

    def test_refuses_a_longer_value_without_a_marker_on_the_cut_side(self):
        value = "feat/12-" + "y" * 50
        head = stamp.fit(value)
        tail = stamp.fit("origin/" + "z" * 50, keep="tail")
        assert head == value[:38] + "..." and len(head) == 41
        assert tail == "..." + ("z" * 50)[-38:]
        assert stamp.fit("abcdefgh", width=6) == "abc..."


class Test_wrapped:
    def test_accepts_a_list_on_continuation_rows_keeping_each_separator(self):
        pieces = ["#664", *(f", #{n}" for n in range(665, 676))]
        rows = stamp.wrapped("homes", pieces)
        assert rows[0][0] == "homes" and all(label == "" for label, _ in rows[1:])
        assert all(value.endswith(",") for _, value in rows[:-1]), rows
        assert all(len(value) <= stamp.PANEL_VALUE_WIDTH - 1 for _, value in rows)
        assert ", ".join(v.rstrip(",") for _, v in rows) == "".join(pieces)
        dots = stamp.wrapped("suite", ["✓ 1 passed", *[" · 12345 skipped"] * 3])
        assert dots[0][1].endswith(" ·") and not dots[1][1].startswith(" ")

    def test_refuses_to_hold_back_room_on_the_last_piece(self):
        """Two columns are held for a separator on every piece but the last,
        so a last piece that fits exactly stays on its row."""
        first = "a" * 20
        last = ", " + "b" * (stamp.PANEL_VALUE_WIDTH - 22)
        assert stamp.wrapped("x", [first, last]) == [("x", first + last)]
        wide = "w" * 60
        assert stamp.wrapped("x", [wide]) == [("x", stamp.fit(wide))]


class Test_item_value:
    def test_accepts_the_digits_before_the_first_dash(self, tmp_path):
        assert stamp.item_value(str(tmp_path / "1790815615-the-seal")) == "1790815615"
        assert stamp.item_value("seal/specs/1-a-b/") == "1"

    def test_refuses_to_cut_a_name_with_no_dash(self):
        assert stamp.item_value("plain") == "plain"
        assert stamp.item_value("-lead") == "-lead"


# --- the stamp's layout -------------------------------------------------------------


class Test_text_cells:
    def test_accepts_each_character_in_one_style_and_foreground(self):
        assert stamp.text_cells("ab", "dim", TITLE_RED) == [
            ("a", TITLE_RED, None, "dim"),
            ("b", TITLE_RED, None, "dim"),
        ]

    def test_refuses_a_style_or_a_colour_nobody_asked_for(self):
        assert stamp.text_cells("a") == [("a", None, None, None)]


class Test_text_lines:
    def test_accepts_a_red_title_a_rule_and_one_line_per_row(self):
        """#832 S3a: `SEALED ` bold in the seal's red and thirty dim `─`, a
        blank line, then each label padded to seven and a space, dim, and
        each value in the terminal's own colours, a leading `✓ ` green and
        `· ` dim; a `""` label stands its value under the one above."""
        lines = stamp.text_lines(ROWS)
        title = [(ch, TITLE_RED, None, "bold") for ch in "SEALED "]
        assert lines[0] == title + [("─", None, None, "dim")] * 30
        assert lines[1] == [] and len(lines) == 1 + len(ROWS)
        text = ["".join(c[0] for c in line) for line in lines]
        assert text[2:5] == [
            "tree    c46fd2d",
            "        feat/12-a-branch",
            "base    1e2bed9  origin/base",
        ]
        assert lines[2][:8] == [(c, None, None, "dim") for c in "tree    "]
        assert [c[3] for c in lines[6][8:10]] == ["green", None]
        assert stamp.text_lines([("x", "· a")])[0][8][3] == "dim"

    def test_refuses_a_title_a_mark_or_a_line_the_rows_do_not_ask_for(self):
        """Only the first row `("SEALED", "")` is the title, whatever a value
        says; a mark is a mark only before a space; a `None` row is a blank
        line (round 1's 5 of #832)."""
        valued = stamp.text_lines([("SEALED", "v1.2.3"), ("tree", "SEALED")])
        assert "".join(c[0] for c in valued[0]) == "SEALED  v1.2.3"
        assert not any(c[1] or c[3] == "bold" for line in valued for c in line)
        for value in ("·x", "✓", "✓x"):
            (line,) = stamp.text_lines([("x", value)])
            assert [c[3] for c in line[8:]] == [None] * len(value), value
        assert stamp.text_lines([None, ("tree", "a")])[0] == []
        assert stamp.text_lines([]) == []


class Test_compose:
    @pytest.mark.parametrize(
        ("rows", "height", "top_disc", "top_text"),
        [(SMALL_ROWS, 14, 0, 4), (TALL_ROWS, 19, 2, 0), ([], 14, 0, 7)],
        ids=["text-under-the-disc", "text-over-the-disc", "no-text"],
    )
    def test_accepts_the_disc_left_of_the_text_each_centred(
        self, rows, height, top_disc, top_text
    ):
        """#832 S3: the disc at column 0, 28 columns and 14 lines, the text
        three columns right of it, each centred on the taller one's height,
        no background outside the circle, and no line past its last visible
        cell."""
        text = stamp.text_lines(rows)
        letter = stamp.compose(rows)
        assert (letter.height, letter.disc) == (height, (0, 2 * top_disc, 28, 28))
        for ln, line in enumerate(letter.cells):
            k, t = ln - top_disc, ln - top_text
            want = (
                [
                    owners_cell(
                        owners_disc(stamp.CHART, x, 2 * k),
                        owners_disc(stamp.CHART, x, 2 * k + 1),
                    )
                    for x in range(28)
                ]
                if 0 <= k < 14
                else [EMPTY] * 28
            )
            if 0 <= t < len(text) and text[t]:
                want += [EMPTY] * 3 + text[t]
            assert line == trimmed(want), ln
            assert all(c[2] is None for c in line if c[0] not in HALF_BLOCKS)
        assert letter.width == max(len(line) for line in letter.cells)

    def test_accepts_the_owners_reference_cell_for_cell(self):
        """#832 S1 to S4 against the picture the owner chose: 14 lines, the
        disc at column 0 and half-row 0, each half-cell the reference's
        colour, the twin its letters line for line, and the block form's text
        the twin's with the owner's characters in place."""
        letter = stamp.compose(REFERENCE_ROWS)
        assert (letter.height, letter.width, letter.disc) == (14, 77, (0, 0, 28, 28))
        assert stamp.stamp(REFERENCE_ROWS, shape=True) == list(REFERENCE_TWIN)
        colours = {letter: colour for colour, letter in LETTERS.items()} | {" ": None}
        for y, said in enumerate(REFERENCE_DISC):
            line = letter.cells[y // 2]
            for x, key in enumerate(said):
                char, fg, bg, _style = line[x] if x < len(line) else EMPTY
                top, bottom = (fg, bg) if char == "▀" else (bg, fg)
                assert (top if y % 2 == 0 else bottom) == colours[key], (x, y)
        ascii_ = str.maketrans(stamp.TWIN_ASCII)
        for line, twin in zip(stamp.stamp(REFERENCE_ROWS), REFERENCE_TWIN, strict=True):
            text = stamp.strip_ansi(line).translate(ascii_)
            assert len(text) == len(twin)
            assert all(a == b for a, b in zip(text, twin, strict=True) if a not in "▀▄")

    def test_refuses_the_disc_and_its_gap_where_no_disc_is_asked(self):
        """The rung `fitted` steps down to: the text block alone at column 0,
        as tall as itself, and the gap only beside a disc."""
        bare = stamp.compose(SMALL_ROWS, disc=False)
        assert bare.disc is None and bare.height == len(stamp.text_lines(SMALL_ROWS))
        assert bare.cells == [trimmed(line) for line in stamp.text_lines(SMALL_ROWS)]
        assert bare.cells[1] == [] and bare.cells[0][0] == (
            "S",
            TITLE_RED,
            None,
            "bold",
        )
        assert stamp.compose([], disc=False) == stamp.Letter([], 0, 0, None)


class Test_stamp:
    def test_accepts_the_drawing_byte_for_byte_as_it_was_before_the_scale_left(self):
        """S13 (#853): taking the scale away moved no byte of either form,
        of the text block with no disc, or of `fitted`'s two rungs."""

        def h(text):
            return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]

        rows = SAMPLE_AT_5623D728
        size = len("\n".join(["first", *stamp.stamp(rows)]).encode("utf-16-le")) // 2
        blocks = [("first", rows), ("second", rows)]
        assert {
            "block": h("\n".join(stamp.stamp(rows))),
            "letters": h("\n".join(stamp.stamp(rows, shape=True))),
            "no-disc": h("\n".join(stamp.stamp(rows, disc=False))),
            "fitted-default": h(stamp.fitted(blocks)),
            "fitted-two": h(stamp.fitted(blocks, budget=2 * size + 10)),
            "fitted-alone-no-disc": h(stamp.fitted(blocks, budget=50)),
        } == DRAWN_AT_5623D728
        # #30 found a code per cell 282 KB for one seal; a real run's block
        # with its label stays under 5,500 UTF-16 units, the owner's
        # reference being 5,119 for rows of the same length.
        name = "the-branch-names-the-work-item-it-carries"
        label = (
            f"SEALED feat/12-{name} @ aaa1111a against origin/release/v1.2.3 @ "
            f"bbb2222b · #12 · 1799000000-{name}"
        )
        assert len(drawn(label, REFERENCE_ROWS).encode("utf-16-le")) // 2 < 5500

    def test_accepts_a_value_as_wide_as_the_panel_at_eighty_columns(self):
        """A value of exactly `PANEL_VALUE_WIDTH` under a seven-column label,
        beside the disc, makes the stamp's widest line 80 columns, whole, in
        both forms: the width is measured by drawing, not restated. One
        column more would run past an 80-column terminal."""
        width = stamp.PANEL_VALUE_WIDTH
        rows = [("SEALED", ""), ("CI also", "x" * width)]
        for shape in (False, True):
            lines = [stamp.strip_ansi(line) for line in stamp.stamp(rows, shape)]
            widest = max(len(line) for line in lines)
            assert widest == 80, f"a value of {width} columns draws {widest}"
            assert any(line.endswith(" " + "x" * width) for line in lines), lines

    @pytest.mark.parametrize("disc", [True, False], ids=["with-its-disc", "no-disc"])
    def test_refuses_a_twin_of_another_size_or_with_a_code_or_a_half_block(self, disc):
        """S5: the twin is the block form's footprint, row for row, in ASCII."""
        blocks = stamp.stamp(SAMPLE_AT_5623D728, disc=disc)
        letters = stamp.stamp(SAMPLE_AT_5623D728, shape=True, disc=disc)
        assert [len(SGR.sub("", b)) for b in blocks] == [len(t) for t in letters]
        assert all(line.isascii() for line in letters), letters
        assert "2 deferred > #56" in "\n".join(letters)
        assert any(SGR.search(line) for line in blocks)


# --- one hook message --------------------------------------------------------------


LABEL = "SEALED feat/x @ aaa1111 against origin/base @ bbb2222 · #12 · 1799000000"


class Test_admitted:
    def test_accepts_the_oldest_blocks_that_fit_with_their_disc(self):
        """#717 and #853: a block with its disc where it fits; two that fit
        together with the blank line between; a newer one that does not fit
        beside the older waits, even where one after it would fit."""
        whole = drawn(LABEL, SMALL_ROWS)
        room = 2 * len(whole) + 2
        two = [(LABEL, SMALL_ROWS), (LABEL, SMALL_ROWS)]
        assert stamp.admitted(two, room) == [whole, whole]
        assert stamp.admitted(two, room - 1) == [whole]
        huge = (LABEL, SMALL_ROWS + [("", f"home-{k}") for k in range(60)])
        assert stamp.admitted([two[0], huge, two[0]], room) == [whole]
        assert stamp.admitted([(LABEL, SMALL_ROWS)], len(whole)) == [whole]

    def test_refuses_a_disc_to_the_one_block_too_large_for_one(self):
        """The rung with no disc is for the oldest block alone, whatever its
        size, so the queue cannot stall; nothing is drawn for nothing."""
        whole, bare = drawn(LABEL, SMALL_ROWS), drawn(LABEL, SMALL_ROWS, False)
        assert stamp.admitted([(LABEL, SMALL_ROWS)], len(whole) - 1) == [bare]
        assert stamp.admitted([(LABEL, SMALL_ROWS)] * 2, 0) == [bare]
        assert stamp.admitted([], 0) == []

    def test_refuses_to_count_a_character_outside_the_bmp_as_one(self):
        """The harness counts UTF-16 units: fifty U+1D54F are a hundred, and a
        lone surrogate a values file carries is counted, not raised on."""
        label = LABEL + " " + "\U0001d54f" * 50
        whole, bare = drawn(label, SMALL_ROWS), drawn(label, SMALL_ROWS, False)
        assert stamp.admitted([(label, SMALL_ROWS)], len(whole) + 10) == [bare]
        assert stamp.admitted([(label, SMALL_ROWS)], len(whole) + 50) == [whole]
        lone = LABEL + "\ud800"
        assert stamp.admitted([(lone, SMALL_ROWS)]) == [drawn(lone, SMALL_ROWS)]


class Test_fitted:
    def test_accepts_the_admitted_blocks_joined_by_a_blank_line(self):
        whole = drawn(LABEL, SMALL_ROWS)
        two = [(LABEL, SMALL_ROWS)] * 2
        assert stamp.fitted(two, 2 * len(whole) + 2) == whole + "\n\n" + whole

    def test_refuses_a_line_where_nothing_is_pending(self):
        assert stamp.fitted([]) == ""


# --- the names a line says ------------------------------------------------------


class Test_sealed_names:
    @pytest.mark.parametrize(
        ("branch", "ref", "said"),
        [
            ("feat/x", "origin/base", "feat/x @ aaa1111 against origin/base @ bbb2222"),
            ("feat/x", "b", "feat/x @ aaa1111 against b @ bbb2222"),
        ],
    )
    def test_accepts_the_branch_and_the_ref_beside_their_commits(
        self, branch, ref, said
    ):
        assert stamp.sealed_names("aaa1111", "bbb2222", branch, ref) == said

    @pytest.mark.parametrize(
        ("branch", "ref", "said"),
        [
            (None, "origin/base", "aaa1111 against origin/base @ bbb2222"),
            ("feat/x", None, "feat/x @ aaa1111 against bbb2222"),
            ("feat/x", "bbb2222" + "0" * 33, "feat/x @ aaa1111 against bbb2222"),
        ],
        ids=["detached", "no-ref", "the-ref-is-the-commit"],
    )
    def test_refuses_to_print_a_part_twice_or_a_stray_at(self, branch, ref, said):
        names = stamp.sealed_names("aaa1111", "bbb2222", branch, ref)
        assert names == said and "None" not in names
        assert names.count("bbb2222") == 1


class Test_ref_is_commit:
    @pytest.mark.parametrize("ref", [None, "", "bbb2", "bbb2222" + "0" * 33])
    def test_accepts_no_ref_or_a_hex_spelling_of_the_commit(self, ref):
        assert stamp.ref_is_commit(ref, "bbb2222")

    @pytest.mark.parametrize("ref", ["b", "bbb-x", "origin/base", "ccc2222"])
    def test_refuses_a_branch_whose_name_begins_the_commit(self, ref):
        assert not stamp.ref_is_commit(ref, "bbb2222")


# --- which form -------------------------------------------------------------------


class Test_pick_shape:
    def test_accepts_the_blocks_on_a_utf8_terminal(self):
        assert stamp.pick_shape(Stream("UTF-8", tty=True)) is False

    @pytest.mark.parametrize(
        "stream",
        [Stream("cp949", tty=True), Stream("utf-8", tty=False), io.StringIO()],
        ids=["a-console-that-is-not-utf8", "a-pipe", "no-encoding"],
    )
    def test_refuses_the_blocks_anywhere_else(self, stream):
        assert stamp.pick_shape(stream) is True


class Test_is_utf8:
    @pytest.mark.parametrize("encoding", ["utf-8", "UTF-8", "utf8"])
    def test_accepts_any_spelling_of_utf8(self, encoding):
        assert stamp.is_utf8(Stream(encoding, tty=False))

    @pytest.mark.parametrize("encoding", ["cp949", "", None, "utf-16"])
    def test_refuses_another_encoding_or_none(self, encoding):
        assert not stamp.is_utf8(Stream(encoding, tty=True))


class Test_is_terminal:
    def test_accepts_a_tty_whatever_its_encoding(self):
        assert stamp.is_terminal(Stream("cp949", tty=True)) is True

    @pytest.mark.parametrize(
        "stream",
        [Stream("utf-8", tty=False), io.StringIO(), Raising("utf-8", tty=True)],
        ids=["a-pipe", "no-isatty-answer", "isatty-raises"],
    )
    def test_refuses_a_stream_nobody_is_looking_at(self, stream):
        assert stamp.is_terminal(stream) is False


# --- a stamp's values ---------------------------------------------------------------


class Test_session_key:
    def test_accepts_the_ids_last_path_part(self):
        assert stamp.session_key("s-1") == "s-1"
        assert stamp.session_key("../../elsewhere") == "elsewhere"

    @pytest.mark.parametrize("session", [None, "", "  ", ".", ".."])
    def test_refuses_a_name_that_is_no_directory_of_its_own(self, session):
        assert stamp.session_key(session) == stamp.NO_SESSION


class Test_values_dir:
    def test_accepts_the_sessions_directory_under_the_common_dir(self):
        assert stamp.values_dir("/c", "s-1") == os.path.join(
            "/c", "specseal-stamp", "s-1"
        )

    def test_refuses_a_session_that_would_leave_the_values_dir(self):
        values_dir = os.path.join("/c", "specseal-stamp")
        assert stamp.values_dir("/c", "../x") == os.path.join(values_dir, "x")
        assert stamp.values_dir("/c", None) == os.path.join(values_dir, "none")


class Test_drawn_path:
    def test_accepts_a_pending_name_as_its_drawn_name(self):
        assert stamp.drawn_path("/d/1-a.json") == "/d/1-a.drawn.json"

    def test_refuses_to_cut_a_name_that_is_not_pending(self):
        """A drawn name is pending by its suffix too, so naming it gives a
        name that does not exist, which `drawn_from` never hands a person."""
        for given, named in (
            ("/d/1-a.txt", "/d/1-a.txt.drawn.json"),
            ("/d/1-a.drawn.json", "/d/1-a.drawn.drawn.json"),
        ):
            assert stamp.drawn_path(given) == named


class Test_write_values:
    def test_accepts_the_values_under_a_name_that_sorts_oldest_first(self, tmp_path):
        path = stamp.write_values(str(tmp_path), "s-1", values(), now=7, key="9-abc")
        assert path == str(tmp_path / "specseal-stamp" / "s-1" / "7-9-abc.json")
        assert json.loads(pathlib.Path(path).read_text(encoding="utf-8")) == json.loads(
            json.dumps(values())
        )
        assert os.listdir(os.path.dirname(path)) == ["7-9-abc.json"]

    def test_refuses_a_name_without_the_tree_where_no_key_is_given(self, tmp_path):
        path = stamp.write_values(str(tmp_path), "../../x", values(tree="a/b"), now=3)
        assert path == str(tmp_path / "specseal-stamp" / "x" / "3-b.json")
        later = os.path.basename(stamp.write_values(str(tmp_path), "x", {}))
        moment, _, tail = later.partition("-")
        assert tail == "tree.json" and int(moment) > 10**18, later


class Test_read_values:
    @pytest.mark.parametrize(
        "scale", [None, 0.9, "large"], ids=["none", "an-older-gates", "a-word"]
    )
    def test_accepts_a_file_in_the_writers_shape_whatever_scale_it_carries(
        self, tmp_path, scale
    ):
        """S13 (#853): a `scale` a gate before #853 wrote decides nothing."""
        written = values(rows=ROWS) | ({} if scale is None else {"scale": scale})
        path = stamp.write_values(str(tmp_path), "s-1", written)
        read = stamp.read_values(path)
        assert read["rows"] == ROWS and read["tree"] == "aaa1111"

    @pytest.mark.parametrize(
        ("text", "why"),
        [
            ("not json", "it is not JSON"),
            ("[1]", "it is not an object"),
            (json.dumps({"rows": "SEALED"}), "`rows` is not a list"),
            (json.dumps({"rows": [["a", "b", "c"]]}), "`rows` is not a list"),
            (json.dumps({"rows": [["a", 1]]}), "`rows` is not a list"),
        ],
        ids=["not-json", "a-list", "rows-a-string", "a-row-of-three", "a-number"],
    )
    def test_refuses_a_file_out_of_shape_in_one_sentence(self, tmp_path, text, why):
        path = tmp_path / "1-a.json"
        path.write_text(text, encoding="utf-8")
        with pytest.raises(ValueError) as refused:
            stamp.read_values(str(path))
        said = str(refused.value)
        assert said.startswith(f"seal-stamp: {path} is not a stamp's values file: ")
        assert why in said and said.endswith("Nothing was drawn."), said

    def test_refuses_a_file_that_cannot_be_read(self, tmp_path):
        missing = tmp_path / "gone.json"
        with pytest.raises(ValueError) as refused:
            stamp.read_values(str(missing))
        assert str(refused.value).startswith(f"seal-stamp: {missing} cannot be read (")


class Test_pending:
    def test_accepts_the_undrawn_files_oldest_first(self, tmp_path, monkeypatch):
        """Oldest first whatever order the directory lists its names in: the
        listing is handed over newest first."""
        directory = stamp.values_dir(str(tmp_path), "s-1")
        newer = stamp.write_values(str(tmp_path), "s-1", values(), now=20)
        older = stamp.write_values(str(tmp_path), "s-1", values(), now=10)
        listed = os.listdir
        monkeypatch.setattr(
            stamp.os, "listdir", lambda d: sorted(listed(d), reverse=True)
        )
        assert stamp.pending(directory) == [older, newer]

    def test_refuses_a_drawn_file_a_hidden_one_and_a_missing_directory(self, tmp_path):
        path = stamp.write_values(str(tmp_path), "s-1", values(), now=1)
        directory = os.path.dirname(path)
        for name in (".2-a.json", ".3-a.tmp", "4-a.txt"):
            write(directory, name, "{}")
        stamp.claim(path)
        assert stamp.pending(directory) == []
        assert stamp.pending(str(tmp_path / "nowhere")) == []


class Test_claim:
    def test_accepts_a_pending_file_once_renamed_drawn(self, tmp_path):
        path = stamp.write_values(str(tmp_path), "s-1", values(), now=1)
        assert stamp.claim(path) == stamp.drawn_path(path)
        assert not os.path.exists(path) and os.path.exists(stamp.drawn_path(path))

    def test_refuses_a_second_claim_of_one_file(self, tmp_path):
        path = stamp.write_values(str(tmp_path), "s-1", values(), now=1)
        stamp.claim(path)
        assert stamp.claim(path) is None


class Test_label:
    def test_accepts_the_sealed_names_the_pull_request_and_the_work_item(self):
        assert stamp.label(values()) == (
            f"SEALED feat/x @ aaa1111 against origin/base @ bbb2222 · #12 · {ITEM_NAME}"
        )

    def test_refuses_a_newer_label_to_a_file_an_older_gate_wrote(self):
        """A15: a file with no `branch` key, from before #666, keeps the label
        it always drew; `branch` present and null is a detached HEAD."""
        old = {k: v for k, v in values().items() if k not in ("branch", "pr")}
        assert stamp.label(old) == f"SEALED aaa1111 against bbb2222 · {ITEM_NAME}"
        assert stamp.label(values(branch=None, pr=None, item=None)) == (
            "SEALED aaa1111 against origin/base @ bbb2222"
        )


class Test_quote:
    def test_accepts_a_path_with_a_space_for_either_shell(self):
        assert stamp.quote("/a b/c.json", windows=False) == "'/a b/c.json'"
        assert stamp.quote("/a b/c.json", windows=True) == '"/a b/c.json"'

    def test_refuses_to_quote_a_path_a_posix_shell_reads_whole(self):
        assert stamp.quote("/a/c.json", windows=False) == "/a/c.json"


# --- once per work item ---------------------------------------------------------


class Test_already_queued:
    def test_accepts_a_pending_or_drawn_file_of_the_id_under_any_session(
        self, tmp_path
    ):
        path = stamp.write_values(str(tmp_path), "s-2", {}, now=1, key="7-abc")
        assert stamp.already_queued(str(tmp_path), "7")
        stamp.claim(path)
        assert stamp.already_queued(str(tmp_path), "7")

    def test_refuses_another_id_an_older_gates_name_and_no_directory(self, tmp_path):
        assert not stamp.already_queued(str(tmp_path), "7")
        stamp.write_values(str(tmp_path), "s-1", {}, now=1, key="8-abc")
        stamp.write_values(str(tmp_path), "s-1", {"tree": "7"}, now=2)
        write(tmp_path / "specseal-stamp", "a-file", "")
        assert not stamp.already_queued(str(tmp_path), "7")


class Test_guarantee_rows:
    def test_accepts_every_row_the_records_carry(self):
        assert stamp.guarantee_rows("c46", "feat/x", "1e2", "1799", "c46", 2) == [
            ("SEALED", ""),
            ("tree", "c46"),
            ("", "feat/x"),
            ("base", "1e2"),
            ("item", "1799"),
            None,
            ("gate", "✓ c46"),
            ("rounds", "2"),
        ]

    def test_refuses_a_row_whose_record_is_absent(self):
        rows = stamp.guarantee_rows("c46", "", None, "1799", None, 0)
        assert rows == [
            ("SEALED", ""),
            ("tree", "c46"),
            ("item", "1799"),
            None,
            ("rounds", "0"),
        ]
        base = "origin/" + "r" * 50
        assert stamp.guarantee_rows("c", "", base, "1", None, 0)[2] == (
            "base",
            "..." + base[-38:],
        )


class Test_record_refusal:
    def test_accepts_an_empty_file_named_by_the_id_and_the_target(self, tmp_path):
        stamp.record_refusal(str(tmp_path), "1799", "deadbee")
        recorded = tmp_path / "specseal-stamp-refused" / "1799-deadbee"
        assert recorded.read_text(encoding="utf-8") == ""

    def test_refuses_to_raise_where_the_record_cannot_be_written(self, tmp_path):
        blocked = tmp_path / "a-file"
        blocked.write_text("", encoding="utf-8")
        stamp.record_refusal(str(blocked), "1799", "deadbee")
        assert blocked.read_text(encoding="utf-8") == ""


class Test_refused_here:
    @pytest.mark.parametrize("sha", ["deadbee", "deadbee0123", "DEADBEE"])
    def test_accepts_the_ids_record_of_the_same_commit(self, tmp_path, sha):
        stamp.record_refusal(str(tmp_path), ITEM_ID, "deadbee01")
        assert stamp.refused_here(str(tmp_path), ITEM_ID, sha)

    @pytest.mark.parametrize(
        ("recorded", "sha"),
        [
            (("1700000000", "deadbee"), "deadbee"),
            ((ITEM_ID, "deadbe"), "deadbee"),
            ((ITEM_ID, "deadbee"), "dea0bee"),
            (None, "deadbee"),
        ],
        ids=["another-item", "shorter-than-seven", "another-commit", "no-record"],
    )
    def test_refuses_a_record_of_anything_else(self, tmp_path, recorded, sha):
        if recorded:
            stamp.record_refusal(str(tmp_path), *recorded)
        assert not stamp.refused_here(str(tmp_path), ITEM_ID, sha)


# --- the stamp queued at a sealed guarantee's commit, over real git -----------------

Item = collections.namedtuple("Item", "repo common target base")


def guarantee_text(target, base, verdict="sealed", earlier=""):
    """A `guarantee.md` in `templates/sdd-guarantee.md`'s shape."""
    return (
        "# an item — guarantee\n\n| Field | Value |\n|---|---|\n"
        f"| Target SHA | {target} against {base}{earlier} |\n"
        f"| Broad gate | {target} against {base} |\n\nVerdict: {verdict}\n"
    )


def routing_text(branch="feat/x"):
    """A `routing.md` naming BRANCH in its `Branch` row, or with none."""
    rows = (
        "| Axis | Answer |\n|---|---|\n| Review | through the review chain |\n"
        "| Destination | open the pull request |\n"
    )
    return rows + (f"| Branch | {branch} |\n" if branch else "")


def closing_records(item, target, base):
    """Two round records, a file in `rounds/` that is not one, `broad-gate.md`
    naming TARGET, and `guarantee.md` reading `sealed` over it."""
    write(item, "rounds/round-1.md", "x\n")
    write(item, "rounds/round-2.md", "x\n")
    write(item, "rounds/notes.md", "x\n")
    write(
        item,
        "broad-gate.md",
        f"| Field | Value |\n|---|---|\n| Broad gate | {target} against {base} |\n",
    )
    write(item, "guarantee.md", guarantee_text(target, base))


@pytest.fixture(scope="module")
def _shared(tmp_path_factory):
    """An opted-in repository whose branch `feat/x` ends at the commit of the
    work item's closing records, `guarantee.md` reading `sealed` over the
    commit before it; built once, and copied for each case."""
    d = tmp_path_factory.mktemp("shared") / "repo"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    write(d, "seal/config.md", "# config\n")
    commit(d, "x")
    git(d, "switch", "-qc", "feat/x")
    write(d, "work.txt", "the work\n")
    commit(d, "the work")
    target, base = (
        git_out(d, "rev-parse", "--short", "HEAD"),
        git_out(d, "rev-parse", "--short", "main"),
    )
    closing_records(d / "seal" / "specs" / ITEM_NAME, target, base)
    commit(d, "the closing records")
    return d, target, base


@pytest.fixture
def shared(tmp_path, _shared):
    """A copy of the shared repository under a directory whose name holds a
    space; its common dir is its `.git`."""
    template, target, base = _shared
    repo = tmp_path / "a checkout" / "repo"
    shutil.copytree(template, repo)
    return Item(repo, str(repo / ".git"), target, base)


def sealed_again(item, text, message="the guarantee again"):
    """The work item's `guarantee.md` rewritten to TEXT and committed."""
    write(item.repo, GUARANTEE, text)
    commit(item.repo, message)


def amended(item, text):
    """The closing records' commit amended so its `guarantee.md` reads TEXT,
    and so no commit before HEAD carries a guarantee."""
    write(item.repo, GUARANTEE, text)
    git(item.repo, "add", "-A")
    git(item.repo, *SIGNED, "commit", "--amend", "-qm", "the closing records")


def queued(common):
    """Every values file under COMMON, drawn or not."""
    found = []
    for directory, _dirs, names in os.walk(pathlib.Path(common) / "specseal-stamp"):
        found += [os.path.join(directory, n) for n in names if n.endswith(".json")]
    return sorted(found)


def queue(item, common=None, session="s-1"):
    return stamp.queue_for_guarantee(str(item.repo), common or item.common, session)


class Test_queue_for_guarantee:
    @pytest.mark.rule("stamp-drawn-once")
    def test_a_sealed_guarantees_commit_queues_one_stamp(self, shared):
        """#975 S4 and S9: one values file for the session, named by the work
        item's id and the audited commit, the line naming it and the command
        quoted for a path that holds a space, and rows read from the records
        at the commit, nothing measured again and no `scale`."""
        said = queue(shared)
        (path,) = queued(shared.common)
        assert os.path.dirname(path) == os.path.join(
            shared.common, "specseal-stamp", "s-1"
        )
        assert os.path.basename(path).endswith(f"-{ITEM_ID}-{shared.target}.json")
        assert said == [
            f"specseal: the stamp for {ITEM_ID} is drawn at the end of this turn "
            f"from {path}; where none appears, `seal-stamp --from "
            f"{stamp.quote(path)}` draws it"
        ]
        read = stamp.read_values(path)
        assert read["rows"] == [
            ("SEALED", ""),
            ("tree", shared.target),
            ("", "feat/x"),
            ("base", shared.base),
            ("item", ITEM_ID),
            None,
            ("gate", f"✓ {shared.target}"),
            ("rounds", "2"),
        ]
        assert {k: read[k] for k in ("tree", "base", "from", "branch", "pr")} == {
            "tree": shared.target,
            "base": shared.base,
            "from": None,
            "branch": "feat/x",
            "pr": None,
        }
        assert read["item"] == str(shared.repo / "seal" / "specs" / ITEM_NAME)
        assert read["session"] == "s-1" and "scale" not in read

    @pytest.mark.rule("stamp-drawn-once")
    def test_accepts_a_reseal_after_withheld_and_a_detached_head(self, shared):
        """#975 S6: an earlier run that withheld does not count. On a
        detached HEAD the branch is left out of the file and the rows."""
        earlier = "; earlier run: abc1234 withheld"
        amended(shared, guarantee_text(shared.target, shared.base, earlier=earlier))
        git(shared.repo, "checkout", "-q", "--detach")
        assert queue(shared)
        (path,) = queued(shared.common)
        read = stamp.read_values(path)
        assert read["branch"] is None and ("", "feat/x") not in read["rows"]

    @pytest.mark.rule("stamp-drawn-once")
    def test_accepts_an_earlier_sealed_this_clone_refused(self, shared):
        """1792363231 S14: a `sealed` the commit gate refused in this clone and
        recorded is no stamp, so the new audit that keeps it on its row
        draws the work item's one."""
        earlier = "; earlier run: deadbee1 sealed"
        amended(shared, guarantee_text(shared.target, shared.base, earlier=earlier))
        assert queue(shared) == []
        stamp.record_refusal(shared.common, ITEM_ID, "deadbee1")
        assert queue(shared)
        assert len(queued(shared.common)) == 1

    @pytest.mark.rule("stamp-drawn-once")
    @pytest.mark.parametrize(
        "verdict",
        [
            "withheld reason: the README is stale",
            "sealed\n\nVerdict: withheld reason: x",
            "Sealed",
        ],
        ids=["withheld", "two-verdicts", "a-near-miss"],
    )
    def test_a_withheld_or_undecided_guarantee_queues_nothing(self, shared, verdict):
        """#975 S5 and S7 of #1000: a guarantee that does not read one
        `sealed` queues nothing and says nothing, nor does a later commit
        that does not touch it."""
        amended(shared, guarantee_text(shared.target, shared.base, verdict))
        assert queue(shared) == []
        write(shared.repo, "README.md", "x\n")
        commit(shared.repo, "something else")
        assert queue(shared) == [] and queued(shared.common) == []

    @pytest.mark.rule("stamp-drawn-once")
    def test_a_second_sealed_verdict_queues_nothing(self, shared):
        """#975 S7: a row whose earlier run reads `sealed` was stamped at it."""
        earlier = "; earlier run: bbb2222 sealed; earlier run: abc1234 withheld"
        amended(shared, guarantee_text(shared.target, shared.base, earlier=earlier))
        assert queue(shared) == [] and queued(shared.common) == []

    @pytest.mark.rule("stamp-drawn-once")
    def test_a_recommit_of_the_same_guarantee_queues_no_second_file(self, shared):
        """#975 S8: an amend, and a re-seal whose row was written fresh, find
        the first file, pending or drawn, under any session of the clone."""
        assert queue(shared, session="s-1")
        git(shared.repo, *SIGNED, "commit", "--amend", "-qm", "again")
        assert queue(shared, session="s-2") == []
        (first,) = queued(shared.common)
        stamp.claim(first)
        write(shared.repo, "x.txt", "a fix after the seal\n")
        new = commit(shared.repo, "a fix")[:7]
        sealed_again(shared, guarantee_text(new, shared.base))
        assert queue(shared, session="s-3") == []
        assert queued(shared.common) == [stamp.drawn_path(first)]

    @pytest.mark.rule("stamp-drawn-once")
    def test_refuses_a_seal_another_clone_carries_from_its_history(
        self, shared, tmp_path
    ):
        """#975 rounds 3 and 5: a clone holding no values file for the work
        item, here a second common dir, queues nothing for a commit that
        edits a guarantee read `sealed` earlier in HEAD's history, whatever
        the newer row says."""
        other = str(tmp_path / "other-common")
        write(
            shared.repo,
            GUARANTEE,
            (shared.repo / GUARANTEE).read_text(encoding="utf-8") + "\na note\n",
        )
        commit(shared.repo, "a note, no new run")
        assert queue(shared, other) == []
        write(shared.repo, "x.txt", "a fix\n")
        new = commit(shared.repo, "a fix")[:7]
        sealed_again(shared, guarantee_text(new, shared.base))
        assert queue(shared, other) == [] and queued(other) == []

    @pytest.mark.rule("stamp-drawn-once")
    def test_refuses_a_guarantee_whose_audited_commit_is_off_the_history(
        self, shared, tmp_path
    ):
        """#975: a squash of the branch carries the verdict onto a commit
        whose history does not hold the audited commit, so another clone
        queues nothing."""
        other = str(tmp_path / "other-common")
        git(shared.repo, "switch", "-q", "main")
        git(shared.repo, "merge", "--squash", "feat/x")
        commit(shared.repo, "the squash")
        assert queue(shared, other) == [] and queued(other) == []

    @pytest.mark.rule("refused-sealed-leaves-a-record")
    @pytest.mark.rule("sealed-off-the-branch-refused")
    def test_a_sealed_committed_past_the_stub_keeps_the_gap(self, shared):
        """1792363231 S13: a `sealed` over a commit nobody has, committed past
        the commit gate, queues nothing and writes no record, and the repair
        that keeps that run on its row queues nothing either: the gap is a
        missing stamp, Q8's direction, pinned as a limit."""
        amended(shared, guarantee_text("deadbee", shared.base))
        assert queue(shared) == []
        earlier = "; earlier run: deadbee sealed"
        sealed_again(
            shared, guarantee_text(shared.target, shared.base, earlier=earlier)
        )
        assert queue(shared) == [] and queued(shared.common) == []
        assert not os.path.exists(os.path.join(shared.common, "specseal-stamp-refused"))


class Test_sealed_before:
    def test_accepts_a_sealed_at_an_earlier_commit_whatever_it_named(self, shared):
        """#975 round 5: the history counts a `sealed` whatever its target,
        resolvable or not, so a rewritten one counts in any clone."""
        amended(shared, guarantee_text("deadbee", shared.base))
        write(shared.repo, "x.txt", "later\n")
        commit(shared.repo, "later")
        assert stamp.sealed_before(chain, str(shared.repo), GUARANTEE) is True

    def test_refuses_the_head_commits_own_verdict_and_two_verdicts(self, shared):
        assert stamp.sealed_before(chain, str(shared.repo), GUARANTEE) is False
        two = "sealed\n\nVerdict: withheld"
        amended(shared, guarantee_text(shared.target, shared.base, two))
        sealed_again(
            shared, guarantee_text(shared.target, shared.base, "withheld reason: x")
        )
        write(shared.repo, "x.txt", "later\n")
        commit(shared.repo, "later")
        assert stamp.sealed_before(chain, str(shared.repo), GUARANTEE) is False

    def test_refuses_a_root_commit_which_has_no_history(self, tmp_path):
        write(tmp_path, GUARANTEE, guarantee_text("deadbee", "main"))
        git(tmp_path, "init", "-q", "-b", "main")
        commit(tmp_path, "the root")
        assert stamp.sealed_before(chain, str(tmp_path), GUARANTEE) is False


# --- the stamp queued at a local-mode guarantee's write ---------------------------


@pytest.fixture(scope="module")
def _local(tmp_path_factory):
    """A repository in local mode, its root under the git common dir, whose
    branch `feat/x` carries the audited commit, with the work item's
    `routing.md` naming the branch and its closing records; built once."""
    d = tmp_path_factory.mktemp("local") / "repo"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    write(d, "README.md", "x\n")
    commit(d, "x")
    git(d, "switch", "-qc", "feat/x")
    write(d, "work.txt", "the work\n")
    target, base = commit(d, "the work")[:7], git_out(d, "rev-parse", "--short", "main")
    item = d / ".git" / "seal" / "specs" / ITEM_NAME
    closing_records(item, target, base)
    write(item, "routing.md", routing_text())
    return d, target, base


@pytest.fixture
def local(tmp_path, _local):
    template, target, base = _local
    repo = tmp_path / "repo"
    shutil.copytree(template, repo)
    return Item(repo, str(repo / ".git"), target, base)


def item_dir(item):
    return pathlib.Path(item.common) / "seal" / "specs" / ITEM_NAME


def queue_local(item, session="s-1", name="guarantee.md"):
    return stamp.queue_for_local_guarantee(str(item_dir(item) / name), session)


def off_branch_commit(repo):
    """A commit on top of `main` that no branch holds; its short SHA."""
    tree = git_out(repo, "rev-parse", "main^{tree}")
    return git_out(repo, *SIGNED, "commit-tree", tree, "-p", "main", "-m", "off")[:7]


def _no_target(item):
    write(item_dir(item), "guarantee.md", "# an item\n\nVerdict: sealed\n")


def _unresolved(item):
    write(item_dir(item), "guarantee.md", guarantee_text("dead0000", item.base))
    return "dead0000"


def _off_the_branch(item):
    off = off_branch_commit(item.repo)
    write(item_dir(item), "guarantee.md", guarantee_text(off, item.base))
    return off


def _no_routing(item):
    (item_dir(item) / "routing.md").unlink()


def _no_branch_row(item):
    write(item_dir(item), "routing.md", routing_text(None))


def _a_branch_gone(item):
    write(item_dir(item), "routing.md", routing_text("feat/merged"))


class Test_queue_for_local_guarantee:
    @pytest.mark.rule("stamp-drawn-once")
    @pytest.mark.parametrize("linked", [False, True], ids=["main checkout", "linked"])
    def test_a_local_mode_sealed_guarantee_queues_one_stamp(
        self, local, tmp_path, linked
    ):
        """1792363231 S1: one values file under the common dir, the rows the
        shared writer builds from the same records, and the line it returns.
        The same where the branch is checked out in a linked worktree."""
        if linked:
            git(local.repo, "switch", "-q", "main")
            git(local.repo, "worktree", "add", "-q", str(tmp_path / "linked"), "feat/x")
        said = queue_local(local)
        (written,) = queued(local.common)
        real = os.path.realpath(written)
        assert os.path.basename(written).endswith(f"-{ITEM_ID}-{local.target}.json")
        assert said == [
            stamp.QUEUED.format(id=ITEM_ID, path=real, command=stamp.quote(real))
        ]
        read = stamp.read_values(written)
        assert read["rows"] == [
            ("SEALED", ""),
            ("tree", local.target),
            ("", "feat/x"),
            ("base", local.base),
            ("item", ITEM_ID),
            None,
            ("gate", f"✓ {local.target}"),
            ("rounds", "2"),
        ]
        assert read["item"] == os.path.realpath(item_dir(local))
        assert (read["branch"], read["from"], read["pr"], read["session"]) == (
            "feat/x",
            None,
            None,
            "s-1",
        )

    @pytest.mark.rule("stamp-drawn-once")
    def test_accepts_a_reseal_after_withheld_with_no_rounds_and_an_unreadable_gate(
        self, local
    ):
        """1792363231 S3: an earlier `withheld` does not count; a work item
        with no `rounds/` reads `0`, and a `broad-gate.md` that is not UTF-8
        is no row."""
        earlier = "; earlier run: abc1234 withheld"
        write(
            item_dir(local),
            "guarantee.md",
            guarantee_text(local.target, local.base, earlier=earlier),
        )
        shutil.rmtree(item_dir(local) / "rounds")
        (item_dir(local) / "broad-gate.md").write_bytes(b"\xff\xfe")
        assert queue_local(local)
        (written,) = queued(local.common)
        rows = stamp.read_values(written)["rows"]
        assert rows[-2:] == [None, ("rounds", "0")]

    @pytest.mark.rule("stamp-drawn-once")
    @pytest.mark.parametrize(
        "verdict",
        ["withheld reason: the README is stale", "sealed\n\nVerdict: withheld"],
        ids=["withheld", "two verdicts"],
    )
    def test_refuses_a_guarantee_that_does_not_read_one_sealed(self, local, verdict):
        """1792363231 S2."""
        write(
            item_dir(local),
            "guarantee.md",
            guarantee_text(local.target, local.base, verdict),
        )
        assert queue_local(local) == [] and queued(local.common) == []

    @pytest.mark.rule("stamp-drawn-once")
    def test_a_local_mode_second_sealed_queues_nothing(self, local):
        """1792363231 S3, once per work item: an earlier run reading `sealed`
        was stamped at it, and a values file for the id, pending or drawn,
        under any session, is a complete record in local mode."""
        earlier = "; earlier run: bbb2222 sealed"
        write(
            item_dir(local),
            "guarantee.md",
            guarantee_text(local.target, local.base, earlier=earlier),
        )
        assert queue_local(local) == []
        write(item_dir(local), "guarantee.md", guarantee_text(local.target, local.base))
        assert queue_local(local, session="s-1")
        assert queue_local(local, session="s-2") == []
        (first,) = queued(local.common)
        stamp.claim(first)
        assert queue_local(local, session="s-3") == []
        assert queued(local.common) == [stamp.drawn_path(first)]

    @pytest.mark.rule("refused-sealed-leaves-a-record")
    @pytest.mark.rule("stamp-drawn-once")
    @pytest.mark.parametrize(
        "given",
        [
            _no_target,
            _unresolved,
            _off_the_branch,
            _no_routing,
            _no_branch_row,
            _a_branch_gone,
        ],
        ids=[
            "no Target SHA row",
            "the target does not resolve",
            "the target is off the branch",
            "no routing.md",
            "no Branch row",
            "a branch the clone no longer holds",
        ],
    )
    def test_a_local_mode_guarantee_off_its_branch_queues_nothing(self, local, given):
        """1792363231 S4 and S14: a verdict over a commit the work item's
        branch does not hold queues nothing; where the branch stands, the
        line says so and the refusal is recorded, and where no branch can be
        read, nothing is said or recorded."""
        named = given(local)
        said = queue_local(local)
        assert queued(local.common) == []
        refused = pathlib.Path(local.common) / "specseal-stamp-refused"
        if named:
            assert said == [
                f"specseal: no stamp was queued for {ITEM_ID}: its guarantee.md "
                f"names {named}, which feat/x does not hold; a new audit at the "
                "head of feat/x draws it"
            ]
            assert os.listdir(refused) == [f"{ITEM_ID}-{named}"]
        else:
            assert said == [] and not refused.exists()

    @pytest.mark.rule("refused-sealed-leaves-a-record")
    def test_a_local_mode_seal_refused_off_its_branch_then_resealed_draws_once(
        self, local
    ):
        """1792363231 S14: the re-seal whose row keeps the refused run as
        `sealed` queues one file, because this clone recorded refusing it."""
        off = _off_the_branch(local)
        assert queue_local(local)
        earlier = f"; earlier run: {off} sealed"
        write(
            item_dir(local),
            "guarantee.md",
            guarantee_text(local.target, local.base, earlier=earlier),
        )
        assert queue_local(local)
        assert len(queued(local.common)) == 1

    @pytest.mark.rule("refused-sealed-leaves-a-record")
    @pytest.mark.parametrize(
        ("recorded", "earlier"),
        [
            (("1700000000", "deadbee"), "deadbee"),
            ((ITEM_ID, "deadbe"), "deadbee"),
            ((ITEM_ID, "deadbee"), "dea0bee"),
        ],
        ids=["another work item", "shorter than seven", "another commit"],
    )
    def test_a_refusal_record_skips_only_its_own_verdict(
        self, local, recorded, earlier
    ):
        """1792363231 S14, the reader half."""
        write(
            item_dir(local),
            "guarantee.md",
            guarantee_text(
                local.target, local.base, earlier=f"; earlier run: {earlier} sealed"
            ),
        )
        stamp.record_refusal(local.common, *recorded)
        assert queue_local(local) == [] and queued(local.common) == []

    @pytest.mark.rule("stamp-drawn-once")
    def test_refuses_a_shared_root_and_a_file_that_is_not_the_guarantee(
        self, local, shared
    ):
        """1792363231 S5, the writer's half: a `guarantee.md` under
        `<repo>/seal/` is the commit's to queue, and so is one under the common
        dir of a repository that also has `<repo>/seal/`; the same text in
        another file of a local work item, or a work item's copy outside
        `seal/specs/`, is no guarantee."""
        write(shared.repo, f"seal/specs/{ITEM_NAME}/routing.md", routing_text())
        assert (
            stamp.queue_for_local_guarantee(str(shared.repo / GUARANTEE), "s-1") == []
        )
        notes = item_dir(local) / "notes.md"
        notes.write_text(
            (item_dir(local) / "guarantee.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        assert queue_local(local, name="notes.md") == []
        elsewhere = pathlib.Path(local.common) / "seal" / "notes" / ITEM_NAME
        shutil.copytree(item_dir(local), elsewhere)
        guarantee = str(elsewhere / "guarantee.md")
        assert stamp.queue_for_local_guarantee(guarantee, "s-1") == []
        (local.repo / "seal").mkdir()
        assert queue_local(local) == []
        assert queued(shared.common) == [] and queued(local.common) == []


# --- a person's command -------------------------------------------------------------


class Test_drawn_from:
    def test_accepts_a_file_drawn_once_and_claimed(self, tmp_path):
        path = stamp.write_values(str(tmp_path), "s-1", values(rows=ROWS))
        assert stamp.drawn_from(path, True) == stamp.stamp(ROWS, True)
        assert not os.path.exists(path) and os.path.exists(stamp.drawn_path(path))

    def test_refuses_a_second_drawing_naming_the_file_the_values_are_in(self, tmp_path):
        """Round 1's 3 of #400: whichever name is given, the file the refusal
        says holds the values exists."""
        path = stamp.write_values(str(tmp_path), "s-1", values())
        stamp.drawn_from(path, True)
        drawn_file = stamp.drawn_path(path)
        for given in (path, drawn_file):
            with pytest.raises(ValueError) as refused:
                stamp.drawn_from(given, True)
            assert str(refused.value) == stamp.VALUES_DRAWN.format(
                path=given, drawn=drawn_file
            )

    def test_refuses_a_file_out_of_shape_before_claiming_it(self, tmp_path):
        path = tmp_path / "1-a.json"
        path.write_text(json.dumps({"rows": "SEALED"}), encoding="utf-8")
        with pytest.raises(ValueError):
            stamp.drawn_from(str(path), True)
        assert path.exists() and not os.path.exists(stamp.drawn_path(str(path)))


class Test_main:
    def test_accepts_the_sample_in_the_form_the_console_takes(self, capsys):
        assert stamp.main([], console_wants_letters=False) == 0
        assert (
            capsys.readouterr().out
            == "\n" + "\n".join(stamp.stamp(stamp.SAMPLE_ROWS)) + "\n\n"
        )
        assert stamp.main(["--shape"], console_wants_letters=False) == 0
        twin = "\n" + "\n".join(stamp.stamp(stamp.SAMPLE_ROWS, True)) + "\n\n"
        assert capsys.readouterr().out == twin
        assert stamp.main([]) == 0, "asked of a stdout that is no terminal"
        assert capsys.readouterr().out == twin

    def test_accepts_a_values_file_drawn_by_hand(self, tmp_path, capsys):
        path = stamp.write_values(str(tmp_path), "s-1", values(rows=ROWS))
        assert stamp.main(["--from", path], console_wants_letters=True) == 0
        assert (
            capsys.readouterr().out
            == "\n" + "\n".join(stamp.stamp(ROWS, True)) + "\n\n"
        )

    def test_refuses_a_drawn_file_and_a_scale_with_nothing_drawn(
        self, tmp_path, capsys
    ):
        """S11 and S13 (#853): exit 2 and one sentence for a file drawn
        already; `--scale` is no argument either command takes."""
        path = stamp.write_values(str(tmp_path), "s-1", values())
        stamp.claim(path)
        assert stamp.main(["--from", path], console_wants_letters=True) == 2
        out, err = capsys.readouterr()
        assert (
            out == ""
            and err
            == stamp.VALUES_DRAWN.format(path=path, drawn=stamp.drawn_path(path)) + "\n"
        )
        with pytest.raises(SystemExit) as stopped:
            stamp.main(["--scale", "0.9"])
        assert stopped.value.code == 2
        assert "unrecognized arguments: --scale" in capsys.readouterr().err


test_census = census_case(TARGET)

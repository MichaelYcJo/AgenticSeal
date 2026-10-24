# Phase 1: 1792624592-the-release-seal-is-drawn-from-the-stamps-cells

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 46a773ea |

## What this phase was asked

`plan.md` phase 1. `.github/scripts/release_seal.py` draws the release PNG
from `skills/verify/scripts/seal_stamp.py#build`, which it loads through its
existing `module()` loader. Each grid point of `build` becomes one opaque
square block of `CELL_PX = 12` pixels in its colour, and a point with no
colour stays transparent. Pillow is imported only inside `draw(png)`, and a
failed import is a `Refused`. `SVG`, `SEAL_PX`, `rasterise` and
`.github/scripts/release-seal.svg` go, and the note's width is derived. In
`tests/test_the_release_seal_is_drawn.py`, the cases for S1 to S6 are
written, `wired` stands in for `draw`, and the SVG cases go. The W3C
namespace host's exemption goes from `tests/test_no_real_identifiers.py`.
`seal_stamp.py`'s docstring paragraph is rewritten. The `seal_stamp.py`
module must keep loading without Pillow. After the phase, the smith draws
the PNG once and copies it to the orchestrator's scratchpad.

## What this phase found

- **The frame's own text fails the identifier check once the exemption
  goes.** `tests/test_no_real_identifiers.py::test_only_neutral_domains`
  scans every tracked file, the work item's records among them. It is red
  at commit 46a773ea on three lines and on nothing else: `spec.md` line 18
  (the Grounding row for the repository rule), `spec.md` line 149 (the
  `## Removes` row for the exemption) and `plan.md` line 101 (phase 1's
  Delivers cell). Each line writes the host out. The `## Removes` row says
  the frame's `git grep` found only the test module's `NS` constant. That
  grep ran before the frame wrote those lines. The smith does not write
  `spec.md` or the Delivers cell. The orchestrator rewords the three lines
  so they name the host without writing it, for example "the W3C's
  namespace host", and the case is then green. This record and the
  overview avoid the literal for the same reason.
- **S9 and S1 with S2 cannot all hold as written.** S9 asks the line after a
  failed Pillow install to name "the release seal's pixel case as the one
  case that fails". S1 and S2 are two cases, and each reads the PNG with
  Pillow. Phase 2 words that line, and its pins, as the release seal's pixel
  cases.
- **Only the two pixel cases need Pillow.** `draw` loads the stamp's module
  before it imports Pillow. So the case for a stamp module that will not
  load (S5) reaches its refusal where Pillow is absent. The Pillow case (S4)
  blocks `PIL` and runs the real `draw`. The save refusal, which *Data &
  interfaces* names and no scenario does, is a third parameter of the
  failure case, "the PNG cannot be saved". It runs the real `draw` against
  a stand-in `PIL` whose `save` raises a disk-full `OSError`. S3 reads the
  width as what `draw` answered: the stand-in `drawn` answers 123, a width
  the real draw never gives.
- **The failure case also holds S4's "uploads nothing".** For every
  parameter except the upload and edit failures, it asserts no
  `gh release upload` was called. Before this phase it asserted only the
  edit.
- **A dry run cannot reach the draw without a suite record.** `DRY_RUN=1`
  with no `SUITE_RECORDS` printed `no seal: the suite's counts cannot be
  read: SUITE_RECORDS names no directory` before the draw ran (executed).
  So the image in the orchestrator's scratchpad was drawn by calling
  `release_seal.py#draw` itself under the worktree's `.venv` Python. It is
  RGBA, 336 by 336 pixels, and `draw` answered a width of 168 (executed).
- **How each new case was seen red.** First against the tree as it stood,
  where `draw` did not exist: every new case, and every case that goes
  through `wired`, failed (executed). Then, at 46a773ea, by one
  `mutation-check` per unit, each red for its own reason (executed):
  - S1 went red with cell (14, 14) painted black in `draw`, with `draw`
    answering the side undivided by `DENSITY`, and with the background
    opaque.
  - S2 went red with `draw` loading a copy of the stamp's module of its own
    (115 cells differed from the built chart).
  - S6 went red with `import PIL` at the module's top.
  - S3 went red with the width 168 written into `seal_release`.
  - The three draw parameters went red with their `except` clause changed
    to catch another class.

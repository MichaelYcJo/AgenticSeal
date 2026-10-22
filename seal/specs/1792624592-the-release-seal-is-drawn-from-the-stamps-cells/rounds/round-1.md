# 1792624592-the-release-seal-is-drawn-from-the-stamps-cells — review round 1

target: 736062fe against release/v0.22.3

This is round 1, so no earlier round's coordinates were carried. Every fact
below was established in this round, in a `git clone --no-local` of the
branch at 736062fe under the round's scratch directory. The base is eae7f0ad.

## Findings

### 1. S2's case passes against a draw that substitutes colours of its own, so the frame's "seen red against a copy of the colours" is not held

severity: should
location: `tests/test_the_release_seal_is_drawn.py:122-142`
evidence: executed `.venv/bin/python -m pytest tests/test_the_release_seal_is_drawn.py::test_the_png_is_the_stamps_cells_one_square_block_each tests/test_the_release_seal_is_drawn.py::test_the_png_follows_whatever_chart_the_stamp_module_has -q -p no:xdist -p no:cacheprovider`, `.venv/bin/python -m pytest tests/test_tmp_round1.py -q -p no:xdist -p no:cacheprovider`
verdict: open

`spec.md` S2 says its case is "seen red against a draw that holds a copy of
the chart or the colours". The case replaces only `CHART` on the stamp
module that `release_seal.py` loaded, so it can catch a copied chart and
cannot catch a copied palette. S1 cannot catch one either, because a copy
equal to the tree's nine colours draws the same pixels. The phase record
claims only the chart half: "S2 went red with `draw` loading a copy of the
stamp's module of its own" (`phases/phase-1.md`).

The round showed this by running the cases. In the clone, `draw` was
changed to map each cell's colour through a literal tuple of the nine
colours, indexed by `DISC_COLOURS`. Both S1 and S2 passed. A variant of S2
that also replaces `LIGHT` on both stamp modules passed against the real
`draw`. It failed against a `draw` that maps that colour to one of its own.
So the colour half becomes part of the pin once the case changes a colour
too. With the one-`M` chart, cell (14, 14) is `LIGHT`, because its up-left
neighbour is not a mark cell. That is why the variant replaces `LIGHT` and
not `FACE`: no `FACE` cell exists in that chart.

The code itself holds no copy. `release_seal.py:457-460` paints `px(x, y)`
as `build` returns it. The defect is that the pin the frame asked for does
not hold that property, and #857 changes exactly this area.

```python
def test_the_png_follows_whatever_chart_the_stamp_module_has(monkeypatch, tmp_path):
    """#1009 S2. With the `CHART` of the stamp module `release_seal.py`
    loaded replaced by a chart this case builds, 28 lines of 28 with one
    `M` inside the field, and its `LIGHT` replaced by a colour no cell of the
    tree's stamp has, the PNG's cells are that module's `build`, and the PNG
    differs from the one drawn with the tree's chart. So the disc's mark and
    its colours are read from the stamp module, and #857's choice reaches the
    release image with nothing else changed. Seen red against a draw that
    loads a copy of the stamp module of its own, and against one that maps a
    cell's colour to a colour of its own."""
    from PIL import Image

    mod = seal()
    before = tmp_path / "tree.png"
    mod.draw(str(before))
    n = 28
    chart = tuple("." * 14 + "M" + "." * 13 if y == 14 else "." * n for y in range(n))
    # The mark's lit cell, (14, 14) in this chart, in a colour the tree has not.
    lit = (1, 2, 3)
    expected = stamp("seal_stamp_for_the_built_chart")
    for loaded in (expected, mod.stamp()):
        monkeypatch.setattr(loaded, "CHART", chart)
        monkeypatch.setattr(loaded, "LIGHT", lit)
    w, _, px = expected.build()
    assert px(14, 14) == lit
    after = tmp_path / "built.png"
    mod.draw(str(after))
    assert blocks(after, px, w, mod.CELL_PX) == []
    assert Image.open(before).tobytes() != Image.open(after).tobytes()
```

answer:

### 2. Where Pillow is absent, S2's case fails with the release script's Refused, but bin/test says both pixel cases fail with a ModuleNotFoundError

severity: should
location: `tests/test_the_release_seal_is_drawn.py:122-142`, `.github/scripts/run_tests.py:315-318`, `.github/scripts/run_tests.py:334-338`, `tests/test_the_suite_has_a_command_that_is_cheap_twice.py:919`
evidence: executed `.venv/bin/python -m pytest tests/test_tmp_round1.py -q -s -p no:xdist -p no:cacheprovider`
verdict: open

After a failed Pillow install, `bin/test` prints: "Only the release seal's
pixel cases import it, so those cases fail with a ModuleNotFoundError and
every other case runs." The `add_pillow` docstring says the same, and the
S9 pin at `tests/test_the_suite_has_a_command_that_is_cheap_twice.py:919`
holds the phrase. The claim is true of S1, which imports Pillow at the top
of its body (line 108). It is false of S2. S2 calls `mod.draw` first, and
`draw` catches the `ImportError` and raises `Refused` (`release_seal.py:446-451`).

The round ran both cases with `sys.modules["PIL"]` set to None. S1 raised
`builtins.ModuleNotFoundError: import of PIL halted; None in sys.modules`.
S2 raised `specseal_release_seal_for_tests.Refused: Pillow is not installed
or will not import (...)`. A person or agent who reads the sentence and
then sees a `Refused` in the failure list gets two explanations that do not
agree.

The narrowest repair keeps the sentence and makes it true: S2 imports
Pillow at its top as S1 does, and uses it in its last assertion. The fix
for finding 1 already carries both lines. Without finding 1's fix, the
change is:

```python
def test_the_png_follows_whatever_chart_the_stamp_module_has(monkeypatch, tmp_path):
    """...unchanged..."""
    from PIL import Image

    mod = seal()
    # ...unchanged down to the last line, which becomes:
    assert Image.open(before).tobytes() != Image.open(after).tobytes()
```

answer:

### 3. A failed Pillow install in the seal job stops at the suite's refusal, but two sentences say it reaches the draw's refusal

severity: should
location: `.github/scripts/release_seal.py:431-433`, `.github/workflows/publish-release.yml:98-99`, `seal/specs/1792624592-the-release-seal-is-drawn-from-the-stamps-cells/spec.md:128`
evidence: read `.github/workflows/publish-release.yml:97-102`, `.github/workflows/publish-release.yml:109-134`, `.github/scripts/release_seal.py:475-477`, `.github/scripts/release_seal.py:497`
verdict: open

The `draw` docstring says "Pillow will not import -- the `seal` job
installs it, and an install that failed lands here". The workflow comment
says "an install that fails costs the image, and the draw's `::warning::`
says so". Both sentences have the same shape as the removed `rsvg-convert`
comment. That shape was true when the renderer had a step of its own. It is
not true now.

Pillow is now installed by the same `pip install` command as `pytest`
(`publish-release.yml:102`). When that command fails, pip usually installs
none of its packages, so the next step has no `pytest` and its outcome is
`failure`. `seal_release` reads `SUITE_OUTCOME` and refuses at
`release_seal.py:475-477`, before `draw` runs at line 497. The job's
warning then reads "the suite at vX.Y.Z ended failure, and a seal says it
passed", and Pillow is not named. The class has a third member. The
`## Rule changes` sentence for `docs/release-checklist.md` (`spec.md:128`)
lists "Pillow was not installed or the stamp's module would not load" among
the causes the job's log gives. In the job, both causes stop the suite
first: S1 needs Pillow, and every stamp case needs the module to load.
These causes are reached only on the hand-drawn `DRY_RUN` route, which sets
no `SUITE_OUTCOME`. The pip behaviour above is pip's usual failure, read
and not run here.

```python
def draw(png):
    """Paint the stamp's disc at `png` and answer the note's width for it in
    CSS pixels, or raise `Refused` saying why: the stamp's module will not
    load, Pillow will not import, or the PNG cannot be written. In the
    `seal` job Pillow comes from the step that installs the suite's
    packages, so an install that failed there leaves no pytest either, and
    `seal_release` refuses earlier, on the suite's outcome; a hand-drawn
    run without Pillow lands here.
```

```yaml
      # Pillow also draws the seal (#1009). It comes from this step with the
      # suite's packages, so an install that fails leaves the suite unrun,
      # and the draw's `::warning::` names the suite's outcome.
```

```markdown
  to: the seal could not be drawn or written,
```

answer:

## Confirmations

confirms: none
The orchestrator's PNG, `1009-seal.png` in its scratchpad, is RGBA and 336
by 336. Every one of its 784 blocks of 12 by 12 pixels equals the colour
`build` gives for its cell, with alpha 255, or has alpha 0 where `build`
gives None. Six sampled cells match: (14, 14) is `(186, 38, 42)` in both,
(0, 14) and (13, 0) are `(150, 24, 28)`, (5, 5) is `(208, 68, 64)`,
(10, 12) is `(186, 38, 42)` and (20, 20) is `(112, 16, 20)`. The opaque
colours are exactly the nine of `DISC_COLOURS`, and the alphas are only 0
and 255. Executed, by a probe that loaded `seal_stamp.py` by path apart from
`release_seal.py`.

confirms: none
`release_seal.py` reaches the cells through `module()` under a name of its
own (`release_seal.py:98-107`) and calls `build()` (`:453`). It holds no
chart and no colour: `draw` pastes `(*px(x, y), 255)` on a transparent RGBA
image and resamples nothing (`:453-460`). The width it answers is
`w * CELL_PX // DENSITY`, and `seal_release` passes that answer to
`sealed_glance` (`:497`, `:515`). `SVG`, `SEAL_PX`, `rasterise` and
`.github/scripts/release-seal.svg` are gone. Read.

confirms: none
Pillow is imported only inside `draw` (`release_seal.py:447`). A
`git grep` for `PIL` or `Pillow` over `hooks`, `skills`, `bin`, `agents`,
`templates` and `install.sh` at 736062fe found nothing (exit 1).
`seal_stamp.py` changed only in its docstring and keeps its stdlib
imports. `bin/test tests/test_the_seal_is_taken_once_by_the_sealer.py -q`,
which holds the stamp loading with Pillow blocked, exited 0 with 373
passed. Executed.

confirms: none
The draw fails cleanly. Each of the three causes `draw` names is one
`Refused`, and `main` turns it into one `no seal:` line and one
`::warning::` with exit 0 (`release_seal.py:429-465`, `:531-553`). `draw`
runs before the upload and the edit, so nothing is uploaded when it
refuses (`:497`, `:521`). `bin/test tests/test_the_release_seal_is_drawn.py -q`
exited 0 with 48 passed; the failure case now also asserts that nothing is
uploaded. Executed.

confirms: none
The `seal` job has five steps: checkout, setup-python, the pip step with
`pillow==12.3.0`, the suite, and the draw. No step runs `apt-get`, and the
pip step comes before both the suite and the draw
(`publish-release.yml:70-134`). `bin/test tests/test_a_release_publishes_its_note.py -q`
exited 0 with 32 passed. Executed.

confirms: none
S8 holds. A `git grep -n -i` at 736062fe for `rsvg`, `release-seal.svg`,
`librsvg`, `SEAL_PX`, `rasterise`, the W3C's namespace host and "owner's
SVG", outside `seal/specs`, `changelog`, `CHANGELOG.md` and
`.test_durations`, finds only the four `docs/` lines of the three
`## Rule changes` items. It also finds one test docstring,
`tests/test_a_release_publishes_its_note.py:717`, which records how a case
was seen red against the removed step. That is a true statement about the
past. Executed.

confirms: none
S10 holds. `rule_changes.parse` of `spec.md` returned three `change` items
and no error. `apply_op` applied each one once, and neither document carries
`rsvg` or `SVG` afterwards. Executed in memory in the clone. By reading, the
two `docs/` pins that stay
(`tests/test_the_release_seal_is_drawn.py:965-1010`) still hold against the
rewritten sentences.

confirms: none
The overview's first `## Not verified` row holds.
`bin/test tests/test_no_real_identifiers.py -q` exited 0 with 6 passed at
736062fe. `bin/test tests/test_the_suite_has_a_command_that_is_cheap_twice.py -q`
exited 0 with 94 passed, and `bin/test tests/test_release_hygiene.py -q`
exited 0 with 46 passed. Executed.

confirms: none
The overview's two divergences match the code and the amended frame. S7's
case asserts no `apt-get` step rather than naming the package
(`tests/test_a_release_publishes_its_note.py:740-758`). S9's sentences name
the pixel cases in the plural (`run_tests.py:327-338`). `spec.md` S7 and S9
were rewritten to match at 5e2b93de. Finding 2 concerns the error class in
S9's sentence, not the plural. Read.

confirms: none
Each new test was read against its group. S6's case
(`tests/test_the_release_seal_is_drawn.py:145-166`) has the shape of
`test_the_stamp_module_imports_with_pillow_blocked`, but it covers a
different module. S1 and S2 differ: S1 holds the size, the mode and the
width for the tree's chart, and S2 holds that the draw follows the chart.
The three draw parameters replace the three `rsvg-convert` parameters. No
duplicate check in the repository names a pair among them. Read.

confirms: none
The owner's writing rules for text agents and checks read
(`skills/writing-style/SKILL.md`, the section on writing so text has one
reading) were checked against `spec.md`, `plan.md` and `questions.md`. Each
number has one home: `CELL_PX` and the derived width are in `spec.md`
*Data & interfaces*, and `plan.md` and `questions.md` item 2 point there. No
separator symbol stands in a frame sentence, and "cell" keeps the one
meaning that `spec.md` defines. Finding 3 is a sentence with the wrong
fact, not one with two readings. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The `tests` run 39695956247 at 736062fe | CI | the orchestrator, which said it would relay a failure |
| The full suite, the repository-wide lint and the typecheck at the branch's head | the branch | the orchestrator's `broad-gate` run after the rounds settle |
| The `seal` job at a real tag push drawing the PNG, attaching it and showing it 168 CSS pixels wide | `.github/workflows/publish-release.yml` | the owner, at the v0.22.3 release run |
| Whether pip installs any of the other packages when one requirement of the `seal` job's pip step fails, which finding 3 takes from pip's usual behaviour | `.github/workflows/publish-release.yml:102` | the smith's fix pass, or the orchestrator |
| `questions.md` Q1 still reads `open`, while the build took its default | `seal/specs/1792624592-the-release-seal-is-drawn-from-the-stamps-cells/questions.md` | the orchestrator, when it drains the rows |
| The phase records' seen-red runs for S3, S6, S7 and the three draw parameters, which this round read and did not run again | `phases/phase-1.md`, `phases/phase-2.md` | the sealer's sample |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_the_release_seal_is_drawn.py -q` in the clone | exit 0, 48 passed |
| `bin/test` over `tests/test_a_release_publishes_its_note.py`, `tests/test_the_suite_has_a_command_that_is_cheap_twice.py`, `tests/test_no_real_identifiers.py`, `tests/test_release_hygiene.py` and `tests/test_the_seal_is_taken_once_by_the_sealer.py`, one module per call | each exit 0: 32, 94, 6, 46 and 373 passed |
| `test_tmp_round1.py` comparing the orchestrator's PNG with `build`, and `draw` with `FACE` replaced on its loaded stamp module | 2 passed: no block differs, and the replaced colour reaches the PNG |
| S1 and S2 with `draw` mapping each colour through a literal copy of the nine colours (edited in the clone, then restored with `git checkout`) | 2 passed: neither case sees the copy |
| `test_tmp_round1.py` running S1 and S2 with `sys.modules["PIL"]` set to None | S1 raised `ModuleNotFoundError`, and S2 raised `Refused: Pillow is not installed or will not import` |
| `test_tmp_round1.py` with S2 extended to replace `LIGHT`, first against the real `draw` and then against a `draw` that maps `(1, 2, 3)` to the tree's `LIGHT` | passed against the real draw and failed against the mapped one |
| `rule_changes.parse` and `apply_op` over `spec.md` and the two `docs/` files, in memory | three `change` items, no error, each applied once |
| `git grep -q -E` for `PIL` or `Pillow` over the shipped directories | exit 1, no match |

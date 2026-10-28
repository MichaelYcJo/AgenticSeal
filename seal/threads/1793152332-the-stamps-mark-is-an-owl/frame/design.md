# Feature Specification: 1793152332-the-stamps-mark-is-an-owl

Issue #857. The sealer's stamp carries a placeholder Georgia Bold S as its
mark. The owner chose the owl on 2026-10-28, in two forms that read as one
design: a 16 x 16 sprite in the stamp's reds for the terminal, and a vector
for a page. This work makes the terminal stamp draw the sprite, makes the
release note's `seal.png` and the plugin icon show the vector, and gives
`assets/seals/` the owl's entry.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against* | A fact has one source: one reader of the mark (`read_sprite`), one sprite file, and one page image read by both the release seal and the plugin manifest. What stood on the old fact goes in the same work: the `.M` chart reader, the S's pinned drawing, and Pillow, whose only reader leaves |
| `CLAUDE.md` *The goal a design is chosen against* | The run is unattended. What only the owner can decide is a row of `questions.md` with a default, and the build proceeds on the default |
| `docs/branch-and-release.md` *Cutting a release* | The seal job attaches `seal.png` and replaces the glance table. Today the image is painted from `seal_stamp.py#build`'s cells. This work changes where the image comes from, stated under `## Rule changes` |
| `docs/release-checklist.md` *6. After the merge* | The hand-drawn route asks for a `python3` that imports Pillow. That clause goes, stated under `## Rule changes` |
| `docs/the-review-record.md` *The stamp* | The stamp is drawn once per work item from the sealer's `sealed`. Nothing in it names the mark, so it does not change |
| `CONTRIBUTING.md` *Running the checks* | Pillow is pinned as a test-and-release dependency. With no reader left, the pin and every copy of it go. `CONTRIBUTING.md` is outside the policy root and changes in the pull request |
| `assets/seals/README.md` *The owl and the bee in the stamp's reds* | Each sprite letter's colour: `K` `INNER`, `P` `FIELD`, `R` `RIM_MID`, `L` `FACE`, `W` `LIGHT`, `Y` `RIM_LIT`, `.` the field; a field cell whose upper-left neighbour is drawn takes `DROP`. After this work the module holds that table and the README cites it |
| Issue #857's body, the owner's decision of 2026-10-28 | The motif, the two forms, the palette, the disc's frame and what closes the issue. The frame, the palette and the motif are not reopened here |
| The owner's verification direction, carried from #1051 and #1060 | `plan.md` *Verification this work item owes* |

## Scope

In:

1. **The terminal's form.** `skills/verify/scripts/seal-mark.txt` holds the
   owl's 16 x 16 sprite instead of the S's 28 x 28 chart.
   `seal_stamp.py#read_sprite` replaces `read_chart` as the one reader of
   that file. `seal_stamp.py#build` draws each sprite letter in its colour
   at the centre of the disc, six cells in from the disc's left and top
   edges, with the drop shadow on the field. The frame of the disc does not
   change. The cases that pin the mark's colours move to the sprite.
2. **The page's form.** `.claude-plugin/icon.png` is a 512 x 512 PNG drawn
   from the owl's SVG with `rsvg-convert`. `.claude-plugin/plugin.json`
   names it as `icon`. `.github/scripts/release_seal.py#draw` copies that
   PNG to the release asset `seal.png` instead of painting `build`'s cells.
3. **Pillow leaves the tree.** `draw` was its only reader outside the
   suite, and the suite's pixel cases read only what `draw` painted. The
   pin in `.github/scripts/run_tests.py`, the runner's repair that installs
   it, the install lines in both workflows and `CONTRIBUTING.md`, the
   census entry for `PIL.Image`, and every case that pins one of these go.
4. **The owl's entry in `assets/seals/`.** `owl.ans` and `owl.png`, drawn
   from the module as each earlier entry is. The SVG moves out of
   `candidates/` to `assets/seals/owl.svg`. The owl's candidate files go.
   The bee stays a candidate. The README's placeholder S entry closes at
   0.23.0, and its sections say what the owl is drawn in by citing the
   module.
5. The changelog fragment of this work item.

Out, and why:

- **The disc's frame, the palette and the motif.** Settled by the owner
  (issue #857's body); not reopened.
- **The README and the GitHub social preview showing the owl.** Issue
  #857's body names them as places a page shows the vector, but its
  *What closes this issue* list does not. The social preview is a
  repository setting a person uploads on GitHub, not a file of the tree.
  `questions.md` Q3 holds both, with the default that this work does not
  do them.
- **The bee.** It stays a candidate in `assets/seals/candidates/`.
- **Drawing the release seal from the sprite.** The owner decided the
  release note shows the vector (issue #857's body, *What closes this
  issue*).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The terminal stamp draws the owl | Given the shipped `seal-mark.txt`, when `build()` is called, then a cell of the field under a sprite letter is that letter's colour from `SPRITE_COLOURS`, a field cell under `.` whose upper-left neighbour is a letter is `DROP`, every other field cell is `FIELD`, and every cell outside the field is what the frame gives today | `tests/skills/test_seal_stamp.py` `Test_build`, with the expected colour rebuilt in the test from the sprite and a letter table written out in the test |
| S2 The owner's picture, cell for cell | Given the reference rows, when the stamp is composed, then each half-cell of the disc is the colour of a reference transcribed from the candidate `owl-28-pixel.ans` at `c8bb9693` for the field and from today's reference for the frame, and the letter twin matches its reference line for line | `tests/skills/test_seal_stamp.py` `Test_compose`, the reference case |
| S3 A malformed sprite is refused with a sentence | Given a sprite file of 15 lines, a line of 17 characters, a character outside `.KPRLWY`, or a drawn cell whose own position or whose drop shadow lies outside the field, when `read_sprite` reads it, then it raises `ValueError` with `SPRITE_MALFORMED` naming the path and the first fault | `tests/skills/test_seal_stamp.py` `Test_read_sprite` |
| S4 A malformed sprite stops the broad gate at exit 2 | Given a copy of the plugin whose `seal_stamp.py` raises at import, when `seal gate` loads it, then the gate exits 2 with that sentence | the existing case in `tests/skills/test_broad_gate.py` that writes a raising `seal_stamp.py`, unchanged |
| S5 The stamp still fits one hook message | Given the widest reference panel and its label, when the block is drawn with its disc, then its length in UTF-16 units is within `MESSAGE_BUDGET` | `tests/skills/test_seal_stamp.py` `Test_stamp`, the bound read from the constant |
| S6 The letter twin keeps its footprint | Given any rows, when the twin is drawn, then each line is ASCII and as wide as the block form's line with its codes removed, and each disc cell is its colour's `KEY` letter | `tests/skills/test_seal_stamp.py` `Test_stamp` and `Test_letter_row`, existing |
| S7 The release seal is the page image | Given a tree whose `plugin.json` names a PNG as `icon`, when `release_seal.py#draw` runs, then the asset file is that PNG byte for byte and `draw` answers the PNG's width divided by `DENSITY` | `tests/github/test_release_seal.py`, a new case |
| S8 A missing or broken page image costs only the image | Given a `plugin.json` with no `icon`, an `icon` naming no file, or a file that is not a PNG, when the seal job runs, then `main` exits 0, prints one line and one `::warning::` naming the cause, uploads nothing and edits no note | `tests/github/test_release_seal.py` `Test_main`, the draw refusals |
| S9 The plugin carries an icon the directory accepts | Given the tree, when `.claude-plugin/plugin.json` is read, then `icon` is `./.claude-plugin/icon.png`, and that file is a PNG, square, 512 to 2048 pixels on a side and under 2,000,000 bytes, read from its header with the standard library | a new case beside the manifest's other cases; and `claude plugin validate .` reporting no `ICON_MISSING`, run by the crafter of phase 1. `check: none reader: the crafter of phase 1 for the validator run` |
| S10 No Pillow is installed or pinned | Given the tree, when the install lines of `.github/workflows/test.yml` and `.github/workflows/publish-release.yml` and the fallback commands of `CONTRIBUTING.md` are read, then none names `pillow`, and `bin/test` installs no Pillow into a `.venv` | the rewritten cases in `tests/behaviour/test_the_release_seal_is_drawn.py`, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` and `tests/github/test_run_tests.py` |
| S11 The owl's entry can be drawn again | Given `assets/seals/README.md`'s command for the owl, when it runs against the tree this work leaves, then its output equals `assets/seals/owl.ans` byte for byte | `cmp` run by the crafter of phase 4. `check: none reader: the crafter of phase 4 for the cmp run` |

## Data & interfaces

**The sprite file.** `skills/verify/scripts/seal-mark.txt` keeps its name and
its place, so the module still reads its mark from the file beside it, and
`tests/behaviour/test_one_word_one_meaning.py`'s word list keeps the name.
Its content is the 16 lines of `assets/seals/candidates/owl-28-pixel.txt` at
`c8bb9693`, 16 characters each, over `.KPRLWY`.

**`seal_stamp.py`, the names that replace the chart's.**

| Today | After this work |
|---|---|
| `CHART_PATH` | `SPRITE_PATH`, the same file |
| `CHART_MALFORMED` | `SPRITE_MALFORMED`: the sentence names the path, the shape `16 lines of 16 characters over .KPRLWY with every drawn cell and its shadow inside the disc's field`, the first fault, and `Nothing was drawn.` |
| `read_chart(path)` | `read_sprite(path)`, the same faults in the same order: a count of lines other than `SPRITE_CELLS`, a line of another length, a character outside `.` and the keys of `SPRITE_COLOURS`, and a drawn cell or its shadow cell outside the field. It reads with `utf-8-sig` as `read_chart` does |
| `CHART` | `SPRITE` |
| none | `SPRITE_CELLS = 16`, and the sprite's offset on the disc, `(DISC_CELLS - SPRITE_CELLS) // 2`, which is 6 |
| none | `SPRITE_COLOURS`: `K` `INNER`, `P` `FIELD`, `R` `RIM_MID`, `L` `FACE`, `W` `LIGHT`, `Y` `RIM_LIT` |
| `build`'s mark rule: `LIGHT` where the upper-left cell is not marked, else `INNER` where the lower-right cell is not, else `FACE`; `DROP` on a field cell whose upper-left cell is marked | a cell under a sprite letter is `SPRITE_COLOURS[letter]`; a field cell under `.` whose upper-left neighbour is a letter is `DROP`; the rest `FIELD`. The pupil `P` counts as a letter for the shadow. The owner's lesson in issue #857, *shading breaks a small mark*, is why the neighbour shading goes |

Every colour the sprite uses is one of the nine `DISC_COLOURS`, so `KEY`,
`letter_row` and the twin do not change. In the twin, a sprite cell reads as
its colour's letter: the body `R` as `n`, the outline `K` as `x`, the breast
`L` as `X`, an eye `W` as `Y`, a beak or foot `Y` as `M`, a pupil `P` as `.`.

**`release_seal.py`.** `draw(png)` reads `.claude-plugin/plugin.json` under
`CODE`, takes its `icon` path, copies that file to `png`, and answers the
width in its PNG header divided by `DENSITY`. It imports nothing outside the
standard library. It raises `Refused` with a sentence naming the cause where
the manifest cannot be read, names no `icon`, the file is not there, the
file does not open with the PNG signature and an `IHDR` chunk, or the copy
cannot be written. `stamp()`, `CELL_PX` and the Pillow import go. `ASSET`
and `DENSITY` stay.

**`.claude-plugin/plugin.json`.** One key is added, `"icon":
"./.claude-plugin/icon.png"`. The plugin reference
(`https://code.claude.com/docs/en/plugins-reference`, *Directory listing
fields*) says Claude Code ignores the field at load time and Anthropic's
directory reads it. `claude plugin validate .` on Claude Code 2.1.312 states
the accepted file: a square PNG or JPEG, 512 to 2048 pixels on a side, under
2 MB, SVG and WebP refused.

**`.claude-plugin/icon.png`.** Drawn by
`rsvg-convert -w 512 -h 512 <svg> -o .claude-plugin/icon.png`, with
`rsvg-convert` 2.58.4 on the framer's machine. At 480 pixels the same
command drew the masks and the blurred shadow the candidate preview
`owl-web.png` shows, with a root-mean-square difference of 1.45 per cent.

## Rule changes

- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: It runs the suite at
    the tag, draws the seal with Pillow from the terminal stamp's own cells and
    colours (`skills/verify/scripts/seal_stamp.py`), one cell to one square
    block of pixels, attaches it as `seal.png`, and replaces the glance table with the image at its display width and one line
    of the table's counts.
  to: It runs the suite at
    the tag, attaches the page form of the stamp's mark, the PNG that
    `.claude-plugin/plugin.json` names as its `icon`, as `seal.png`, and
    replaces the glance table with the image at its display width and one
    line of the table's counts. The PNG is drawn from `assets/seals/owl.svg`
    by the command `assets/seals/README.md` gives, and the job installs no
    imaging library to attach it.
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: To draw one by hand, from a checkout at the tag, with a `python3` that
    imports Pillow, run the suite
  to: To draw one by hand, from a checkout at the tag, run the suite

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `.M` chart reader and its names | `skills/verify/scripts/seal_stamp.py#read_chart`, `CHART`, `CHART_PATH`, `CHART_MALFORMED` | `read_sprite` and the `SPRITE` names. One reader of the mark, because no chart ships |
| The S's chart | `skills/verify/scripts/seal-mark.txt`, its content | The tags v0.20.0 to v0.23.0 carry it, and `assets/seals/README.md` *The placeholder S* draws it again from v0.22.1 |
| The mark's neighbour shading | `skills/verify/scripts/seal_stamp.py#build`, the `LIGHT`, `INNER` and `FACE` choice by neighbour | Nothing replaces it: the owner's lesson in issue #857 is that shading breaks a small mark. The sprite carries its own light and dark |
| The S's pinned drawings | `tests/skills/test_seal_stamp.py`, `REFERENCE_TWIN`, `REFERENCE_DISC`, `owners_disc`'s chart rule | Rewritten in place for the owl, transcribed from the candidate the owner looked at |
| The byte hashes of the S's drawing | `tests/skills/test_seal_stamp.py`, `SAMPLE_AT_5623D728`, `DRAWN_AT_5623D728` and the hash half of `Test_stamp::test_accepts_the_drawing_byte_for_byte_as_it_was_before_the_scale_left` | The claim they hold, that removing the scale in #853 moved no byte of the S's drawing, is about a drawing that no longer ships. Re-pinning hashes of the owl would hold the code to itself. The size line of that case stays, bound by `MESSAGE_BUDGET` instead of the stored 5,500 |
| The frame counts read by colour | `tests/skills/test_seal_stamp.py#Test_build`, the count of `WAX_EDGE`, `RIM_LIT`, `RIM_MID` and `RIM_DARK` cells | Counted by ring position instead: the sprite draws `RIM_MID` and `RIM_LIT` inside the field, so a count by colour no longer measures the frame |
| The chart cases | `tests/skills/test_seal_stamp.py#Test_read_chart` | `Test_read_sprite` |
| The release seal painted from the stamp's cells | `.github/scripts/release_seal.py#draw`'s Pillow painting, `release_seal.py#stamp`, `CELL_PX` | `draw` copies the PNG `plugin.json` names (issue #857, *What closes this issue*) |
| The release seal's pixel cases | `tests/github/test_release_seal.py#Test_module` `test_the_png_is_the_stamps_cells_one_square_block_each`, `test_the_png_follows_whatever_chart_the_stamp_module_has`, `test_the_release_script_loads_with_pillow_blocked`, the helpers `blocks` and `pillow_that_cannot_save`, and the reasons `Pillow is not installed`, `the stamp's module will not load` and `the PNG cannot be saved` | The new copy case and the new refusal reasons in the same module |
| The Pillow pin and its repair | `.github/scripts/run_tests.py#PILLOW`, `PILLOW_VERSION`, `has_pillow`, `add_pillow`, its call in the runner, its entry in `PACKAGES`, and its paragraph in the module docstring | Nothing reads Pillow after phase 1. `CLAUDE.md` *The rule a mechanism is kept against* |
| Every copy of the pin | `.github/workflows/test.yml` and `.github/workflows/publish-release.yml` install lines and their comments; `CONTRIBUTING.md` *Running the checks*, its Pillow sentences and both fallback commands | As above |
| The cases that pin the pin | `tests/github/test_run_tests.py` (the `pillow` argument of `fake_venv` and the two `add_pillow` cases), `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py`, `tests/behaviour/test_release_hygiene.py` row `("CONTRIBUTING.md", "12.3.0")`, `tests/behaviour/test_the_release_seal_is_drawn.py#test_the_publishing_workflow_installs_the_pins_the_runner_holds`'s Pillow half, `tests/behaviour/test_a_release_publishes_its_note.py`'s install-before-draw order | Each case keeps what it holds for the other pins and drops Pillow |
| The census entry for Pillow's opener | `tests/censuses.py#NOT_A_FILE_OPENER` entry `PIL.Image`, the clause naming it in the comment above, and `tests/test_censuses.py`'s case `PIL Image.open is binary` | No file of the tree imports `PIL` after phase 1 |
| The owl's candidate files | `assets/seals/candidates/owl-28-pixel.txt`, `owl-28-pixel.ans`, `owl-28-pixel.png`, `owl-web.png` | The sprite is `seal-mark.txt`; the entry's `owl.ans` and `owl.png` are drawn from the module; the page preview is `.claude-plugin/icon.png`. Git history keeps the candidates the owner looked at |
| The owl's SVG under `candidates/` | `assets/seals/candidates/owl-web.svg` | Moved by `git mv` to `assets/seals/owl.svg` |
| The letter list in the README | `assets/seals/README.md` *The owl and the bee in the stamp's reds*, the bullet *The sprite's letters* | `seal_stamp.py#SPRITE_COLOURS`; the README cites it |
| The README's rule that an entry waits for its tag | `assets/seals/README.md` *The next entry* | Rewritten in place: the work that ships a mark writes its entry, and the entry's command names the tag that carries it |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-28 by framer, before the build.

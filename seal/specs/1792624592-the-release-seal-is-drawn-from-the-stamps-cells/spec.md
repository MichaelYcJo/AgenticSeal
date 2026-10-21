# Feature Specification: the release seal is drawn from the stamp's cells (#1009)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md holds WHAT this work
delivers and how we'll know. The policy documents in docs/ outrank this file;
the framer cites them and does not restate them. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| Issue #1009, the owner's comment of 2026-10-22 | The release PNG is drawn from the terminal stamp's cells and colours, one cell to one square block of pixels, by Pillow. The SVG, its `rsvg-convert` install step and every sentence and case stating the SVG go. This reverses #832's choice on purpose: the staircase edges #832 opened on are now the style |
| `skills/implement/SKILL.md` *Document layout* (the `docs/` row) | A pull request does not edit `docs/`. The three `docs/` sentences this work makes false are the `## Rule changes` items below, applied by the owner's `settle --apply` after the release. Until then they still name `rsvg-convert` (`questions.md` Q1) |
| `docs/branch-and-release.md` *Cutting a release*, the bullet opening "The release note publishes itself" | The seal is a second act: it runs only on a release this run created, edits only a glance table still as generated, and any failure is one `::warning::` that leaves the note as published. This work keeps every part of that and changes only how the PNG is drawn |
| `CONTRIBUTING.md` *Running the checks* | The gates are stdlib-only; Pillow is test-and-release-only. `.github/scripts/release_seal.py` is a release script, not a gate, so it may import Pillow, and it does so only inside the draw (Data & interfaces) |
| `skills/verify/scripts/seal_stamp.py`, the comment above `DISC_CELLS` | The one statement of what a cell is: one column by one half-row of the terminal's grid, and so square. The release PNG takes that cell as its unit and does not restate it |
| `tests/test_the_seal_is_taken_once_by_the_sealer.py#test_the_stamp_module_imports_with_pillow_blocked` | `seal_stamp.py` stays stdlib-only, because the gate, the hook and the command load it where Pillow is absent. So the stamp does not write the PNG itself; the release script reads its cells |
| `docs/the-reader-registry.md` *A frame names what its work removes* | `## Removes` below is the list the review reads against the diff |
| `CLAUDE.md` *Repo rule: no real identifiers in examples or fixtures* | The W3C's namespace host is allowed in `tests/test_no_real_identifiers.py` only because an SVG must carry its namespace. With the SVG gone the exemption has no reason left |

## Scope

**In.**

1. `.github/scripts/release_seal.py` draws the release PNG from
   `seal_stamp.py#build`: one cell of `build` to one square block of
   `CELL_PX` by `CELL_PX` PNG pixels, in exactly that cell's colour and
   fully opaque, and fully transparent where `build` gives no colour. No
   blending, no resampling filter, no colour of its own. The disc and its
   mark come from the one chart `seal_stamp.py` reads
   (`skills/verify/scripts/seal-mark.txt`), so #857's choice changes the
   terminal stamp and the release image together.
2. The note's `<img>` width is the PNG's side divided by `DENSITY`, both
   derived from the stamp's width in cells and `CELL_PX`. Data & interfaces
   states the numbers, once.
3. `.github/scripts/release-seal.svg`, `rasterise`, and the `rsvg-convert`
   install step in `.github/workflows/publish-release.yml` go, with every
   sentence and case outside `docs/` that states them (`## Removes`).
4. The `docs/` sentences are `## Rule changes` items.
5. Cases: one holding the PNG's cells equal to the stamp's, one holding that
   the PNG follows whatever chart the stamp module has, and failure cases for
   Pillow absent and for the stamp module not loading.

**Out.**

- The stamp's text block beside the disc (the `SEALED` title and the rows).
  The note already carries the counts below the image and in its alt text.
  Issue #1009 *Out*.
- Choosing the final mark: #857.
- Editing `docs/` in this diff: the standing rule above, unless the owner
  answers `questions.md` Q1 otherwise.
- `.test_durations`. Its entries for the removed cases are left: CI's
  durations union writes that file (`.github/scripts/durations_union.py`),
  and no case reads a name in it against the suite.
- `assets/seals/README.md` and its previews. They record the terminal
  emblems, and the release image is not an entry there.
- The earlier work items' records
  (`seal/specs/1790993139-the-release-seal-is-drawn-and-attached-at-publish-time/`,
  `seal/specs/1791270164-the-release-seal-is-drawn-in-curves/`). They are
  history, and both carry the no-change block in `## Rule changes`, so no
  unsettled spec rewrites the sentences this one rewrites (executed: their
  sections read).
- `publish_release_note.py#sealed_glance`. It already takes the width as an
  argument.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the cells are the stamp's | Given the tree's `seal_stamp.py`, when `release_seal.py#draw` writes the PNG, then it is RGBA, `w * CELL_PX` pixels square where `w` is `build`'s width, and every pixel of the block for cell `(x, y)` equals `px(x, y)` with alpha 255, or has alpha 0 where `px(x, y)` is None | a new case in `tests/test_the_release_seal_is_drawn.py` that loads `seal_stamp.py` itself, by path, apart from the module `release_seal.py` loaded, and compares every pixel with Pillow; seen red with one cell's colour changed in the draw |
| S2 the mark follows the one chart | Given the stamp module `release_seal.py` loaded, with its `CHART` replaced by a chart the case builds (28 lines of 28, one `M` inside the field), when the draw runs, then the PNG's cells equal that chart's `build`, and the drawn PNG differs from the one drawn with the tree's chart | a new case; seen red against a draw that holds a copy of the chart or the colours |
| S3 the width is derived | Given a sealed note, when `seal_release` writes it, then the `<img>` width is the PNG's side divided by `DENSITY` | `test_the_seal_replaces_the_glance_table_and_is_attached`, extended to read the width against `draw`'s answer |
| S4 Pillow absent | Given `PIL` blocked (`sys.modules["PIL"] = None`), when `main` runs, then it prints one `no seal: ...` line naming Pillow and one `::warning::`, exits 0, and uploads and edits nothing | a parameter of `test_any_failure_leaves_the_note_as_it_was_published` |
| S5 the stamp module will not load | Given the stamp's loader raising, when `main` runs, then the same, naming the stamp's module | a parameter of the same case |
| S6 the script loads without Pillow | Given `PIL` blocked, when `release_seal.py` is loaded, then it loads: Pillow is imported inside `draw` and nowhere else | a case in the style of `test_the_stamp_module_imports_with_pillow_blocked` |
| S7 the seal job | Given `.github/workflows/publish-release.yml`, then the `seal` job has five steps, no step runs `apt-get`, and the step installing `PILLOW` comes before the draw | `tests/test_a_release_publishes_its_note.py`, the job's step-count case rewritten |
| S8 no SVG is left | `git grep -n -i -e rsvg -e release-seal.svg -e librsvg` outside `seal/specs/`, `changelog/` and `.test_durations` finds only the `docs/` sentences `## Rule changes` rewrites | executed by the smith at the last phase, the output in its phase record |
| S9 what `bin/test` says about Pillow | The line announcing Pillow's top-up says Pillow draws the release seal, and the line after a failed install still names the release seal's pixel cases, S1's and S2's, as the cases that fail | `tests/test_the_suite_has_a_command_that_is_cheap_twice.py#test_a_failed_pillow_install_is_a_sentence_and_pytest_is_still_called`, its sentence pins rewritten |
| S10 the rule changes parse and apply | `rule_changes.parse` of this file returns three `change` items and no error, and `apply_op` of each on its document applies once | executed by the framer in memory (`plan.md` *Technical context*); the pull-request check reads the section again |

## Data & interfaces

- **What one cell is.** One cell is one grid point of
  `seal_stamp.py#build`: `px(x, y)` for `x` and `y` in `range(w)`. In the
  terminal a character holds two of them, the top half and the bottom half
  of `▀`, and `seal_stamp.py`'s comment above `DISC_CELLS` says why that
  half is square. So the PNG shows the disc exactly as the stamp shows it,
  28 cells across and 28 cells tall. `release_seal.py` cites that comment
  and does not restate it.
- **How `release_seal.py` reaches the cells.** It loads `seal_stamp.py`
  through its own `module()` loader, under a name of its own, as it loads
  `broad_gate.py`, and calls `build()`. `build` is already the interface the
  stamp's own `compose` reads, so `seal_stamp.py` gains no export and nothing
  is copied out of it.
- **The constants.** `CELL_PX`, the side of one cell's block in PNG pixels,
  is the one new constant, and it is 12. `DENSITY` stays 2. `SEAL_PX` as a
  fixed number goes: the width is `w * CELL_PX // DENSITY`, computed where it
  is used, so today's 28 cells make a 336-pixel PNG shown 168 CSS pixels
  wide, where the SVG was shown 160. 12 is even, so a screen at density 1
  halves every block to whole pixels, and it is the size
  `assets/seals/README.md` already draws each half of a terminal character
  at (12 by 24 pixels per character). `questions.md` item 2 says why this
  was not asked.
- **The draw.** One function, `draw(png)`, writes the PNG at `png` and
  returns the note's width in CSS pixels. It imports Pillow in its own body,
  and raises `Refused` with a sentence naming the cause when Pillow will not
  import, when the stamp module will not load, or when the save fails. The
  module's top stays stdlib-only, so every publishing case can run with a
  stand-in for `draw` and without Pillow, as they ran with a stand-in for
  `rsvg-convert`.
- **The workflow.** The `seal` job keeps `install the suite's packages and
  Pillow`, which already installs `PILLOW` before the suite and the draw, and
  loses `install rsvg-convert`.

## Rule changes

- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: draws the owner's seal from `.github/scripts/release-seal.svg` with
    `rsvg-convert`, which the job installs, attaches it as `seal.png`, and
  to: draws the seal with Pillow from the terminal stamp's own cells and
    colours (`skills/verify/scripts/seal_stamp.py`), one cell to one square
    block of pixels, attaches it as `seal.png`, and
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: `rsvg-convert` was not installed or could not draw the SVG,
  to: Pillow was not installed or the stamp's module would not load,
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: from a checkout at the tag on a machine with `rsvg-convert`, run
  to: from a checkout at the tag, with a `python3` that imports Pillow, run

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The owner's SVG of the seal | `.github/scripts/release-seal.svg` | Nowhere: the drawing is `seal_stamp.py#build`'s cells |
| The rasteriser and the SVG's path | `.github/scripts/release_seal.py#rasterise`, `.github/scripts/release_seal.py#SVG` | `.github/scripts/release_seal.py#draw` |
| The fixed display width | `.github/scripts/release_seal.py#SEAL_PX` | Derived from the stamp's width, `CELL_PX` and `DENSITY` (Data & interfaces) |
| The docstring paragraphs naming the SVG and `rsvg-convert` as a release dependency, and the `DRY_RUN` paragraph's "on a machine with `rsvg-convert`" | `.github/scripts/release_seal.py`, the module docstring | Rewritten in place: the draw from cells with Pillow, imported inside `draw` |
| The step that installs `librsvg2-bin`, its comment, and the header comment's sentence naming the SVG | `.github/workflows/publish-release.yml`, job `seal`, step `install rsvg-convert`; the file's opening comment | Pillow comes from the job's existing pip step |
| The SVG cases and their fixtures | `tests/test_the_release_seal_is_drawn.py#test_the_release_seal_svg_is_the_owners_with_its_text_as_paths`, `#test_the_rasteriser_runs_rsvg_convert_at_two_times_the_display_size`, `#test_rsvg_convert_draws_the_seal_transparent_round_and_in_its_colours`, `#LAYERS`, `#RED`, `#NS`, `#SVG`, `#svg_tree`, `#points`, `#rsvg_convert`, and `wired`'s `rsvg` argument | S1, S2 and S6's cases; `wired` stands in for `draw` |
| The three `rsvg-convert` failure parameters | `tests/test_the_release_seal_is_drawn.py#REASONS` and the parametrisation of `#test_any_failure_leaves_the_note_as_it_was_published`: `rsvg-convert is not installed`, `rsvg-convert fails`, `the SVG is not there` | S4 and S5's parameters |
| The SVG paragraphs of the test module's docstring | `tests/test_the_release_seal_is_drawn.py`, the module docstring and the `S6` banner comment | Rewritten in place to the draw from cells |
| The pins on the two `docs/` sentences naming `rsvg-convert` | `tests/test_the_release_seal_is_drawn.py#test_the_release_tail_says_the_seal_is_a_second_act_that_never_fails_it` (the `release-seal.svg` assertion and its docstring sentence) and `#test_the_checklist_box_says_where_a_missing_seal_is_explained` (the two `rsvg-convert` assertions and their comment) | The sentences are `## Rule changes` items; what the image is, is pinned by S1 and S2. The cases keep every other assertion (`plan.md` A6) |
| The install case and the step count's comment | `tests/test_a_release_publishes_its_note.py#test_the_seal_job_installs_rsvg_convert_before_the_suite_and_the_draw`; the "Six since #832" comment and `len(held) == 6` in the step-count case | S7 |
| The SVG namespace's exemption | `tests/test_no_real_identifiers.py#ALLOWED_DOMAINS`, the entry for the W3C's namespace host and its comment | Nothing: its one reason was the SVG's `xmlns`, and the only other occurrence was `#NS` above (executed: a `git grep -n` for the host at eae7f0ad) |
| The sentences saying `rsvg-convert` draws the seal and Pillow only reads it | `.github/scripts/run_tests.py`, the module docstring's Pillow paragraph and the comment above `PILLOW_VERSION` | Rewritten in place: Pillow draws the release seal in the `seal` job and the suite's pixel cases read it |
| The pin that Pillow does not draw | `tests/test_the_suite_has_a_command_that_is_cheap_twice.py#test_a_failed_pillow_install_is_a_sentence_and_pytest_is_still_called`, the `"draws the release seal" not in err` assertion and its comment | S9's rewritten pins |
| The sentence on Pillow decoding what `rsvg-convert` draws | `CONTRIBUTING.md` *Running the checks* | Rewritten in place: Pillow draws the seal the tag push attaches |
| The sentence saying #832 moved the release seal to the SVG | `skills/verify/scripts/seal_stamp.py`, the module docstring's paragraph naming `.github/scripts/release_seal.py` | Rewritten in place: that script reads `build` and draws the release PNG from it |

## Open questions

Anything a planner must answer lives in questions.md, not inline: unanswered
questions buried in prose read as decided.

<!-- The line below is the frame's mark in the tree; `agents/framer.md` says
     why CI needs it. Whoever drew the frame fills in the date and `<who>`,
     which takes the two values the `Planning` row of `routing.md` takes,
     `framer` or `the session`; a mark that disagrees with that row is
     refused at the pull request rather than guessed at. The shape (verb,
     date, who, the moment) is the one `routing.md` and `plan.md` end with,
     which keeps three such lines from becoming three conventions.
     A reframe adds `Reframed <date> by <who>, after round <N>.` UNDER this
     line when the review chain sends the work item back to its framer. It is
     never in this template; only a reframe writes it. -->

Framed 2026-10-22 by framer, before the build.

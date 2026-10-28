# Implementation Plan: 1793152332-the-stamps-mark-is-an-owl

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phase 1.
Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phase 2.
Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phase 3.
Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phase 4.

## Summary

Four phases, each a fresh crafter, each leaving the tree green under its own
narrow run. Phase 1 moves the release seal off the stamp's cells first, so
that phase 2 can change the cells without a release case reading them.
Phase 1 also gives the plugin its icon, because the icon and the release
seal are one PNG. Phase 2 makes the terminal stamp draw the owl's sprite.
Phase 3 removes Pillow, whose last reader phase 1 took away. Phase 4 writes
the owl's entry in `assets/seals/`, moves the SVG out of `candidates/`, and
writes the changelog fragment.

## Technical context

**How the terminal stamp is drawn today.** `skills/verify/scripts/seal_stamp.py`
reads its mark at import: `CHART_PATH` (line 209) names `seal-mark.txt`
beside the module, `read_chart` (line 217) refuses anything but 28 lines of
28 characters over `.M` with every `M` inside the field, and `CHART = read_chart(CHART_PATH)`
(line 252) runs at import. `build` (line 255) computes the disc from the
radius and colours a field cell under an `M` by its neighbours: `LIGHT`,
`INNER` or `FACE`, with `DROP` on the field down-right of the mark. Every
cell is one of the nine `DISC_COLOURS` (line 113). `compose` (line 566)
places the disc at column 0 and the text three columns right of it.
`colour_row` (line 355) writes an SGR only where the colour or the style
changes, and `letter_row` (line 394) writes each disc cell as its colour's
`KEY` letter (line 128) for a console that is not UTF-8. `admitted` (line
613) and `fitted` (line 657) hold the `Stop` hook's message under
`MESSAGE_BUDGET` (line 183), 9,000 UTF-16 units, which #717 measured
against the harness's 10,000. `skills/verify/scripts/broad_gate.py#load`
(line 202) turns an import that raises, such as a malformed chart, into exit
2 with the sentence.

**What a coloured sprite changes there** (executed, a one-off probe run once
from the scratchpad and deleted):

- Every drawn cell of the owl's sprite, and every drop-shadow cell, lies
  inside the field when the sprite stands six cells in from the disc's left
  and top edges. `read_sprite` can therefore refuse a cell outside the field
  as `read_chart` does, and the shipped sprite passes.
- With the colour table of `assets/seals/README.md` and `DROP` on the
  shadow, the field matches the candidate `owl-28-pixel.ans` the owner
  looked at in every cell except the shadow. The candidate paints the shadow
  `(78, 8, 12)`, which is not one of the stamp's reds; `DROP` is
  `(84, 8, 12)`. The owner's brief says every colour is one of the stamp's
  existing reds, so `build` uses `DROP`. The candidate's frame also differs
  from `build`'s frame in its outer half-rows; the frame the owner settled
  on 2026-10-07 is `build`'s, and it stays.
- The lean writer still holds the drawing small. The owl's disc alone is
  5,196 UTF-16 units where the S's is 4,495. The widest reference panel
  with its label is 5,959 units, under the budget of 9,000 and over the
  5,500 that `Test_stamp` states today. Two full stamps did not fit one
  message before this work either, so the number of stamps one `Stop` draws
  does not change for a full panel.
- Every sprite colour is one of the nine, so the letter twin needs no
  change: the twin printed the owl as `x`, `n`, `X`, `Y`, `M` and `.` inside
  the frame's letters.

**How the release seal is drawn today.** `.github/scripts/release_seal.py#draw`
(line 430) loads `seal_stamp.py` through `stamp()` (line 98), imports
Pillow inside its body, and paints each cell of `build()` as a 12-pixel
block (`CELL_PX`, line 117). `seal_release` (line 473) uploads the file as
`seal.png` (`ASSET`, line 405) and puts it in the note at the width `draw`
answers. `.github/workflows/publish-release.yml` installs Pillow in the
`seal` job (line 103). `tests/behaviour/test_a_release_publishes_its_note.py`
(line 100 onward) records that #1009 refused a step installing an SVG
renderer with `apt-get`: the job installs no system package.

**What the owner's decision changes there.** The release note shows the
vector, not the sprite (issue #857's body, *What closes this issue*). The
plugin directory accepts a PNG or a JPEG and refuses an SVG (executed:
`claude plugin validate .` on Claude Code 2.1.312 printed `ICON_MISSING`
with the rule: a square PNG or JPEG, 512 to 2048 pixels, under 2 MB).
So the tree has to hold a PNG drawn from the SVG in any case, and the
release seal reads that same PNG. `rsvg-convert` 2.58.4 draws the SVG's
masks and blurred shadow (executed: at 480 pixels its output against the
candidate preview `owl-web.png` has a root-mean-square difference of 1.45
per cent, and the two images read the same when opened).

**Where Pillow is read.** After phase 1 no file outside `tests/` imports
`PIL` (executed: `git grep -l -E "from PIL|import PIL"` lists
`.github/scripts/release_seal.py`, `tests/github/test_release_seal.py` and
`tests/test_censuses.py` today). The pin is held in
`.github/scripts/run_tests.py` (lines 66 to 70, 115 to 124, 153, 305 to
345 and 657), installed by `.github/workflows/test.yml` (lines 144 and 152)
and `publish-release.yml` (lines 95 to 103), stated in `CONTRIBUTING.md`
*Running the checks* (lines 83 to 89, 104, 141 and 142), and pinned by cases
in five test modules (`frame/design.md` *Removes*).

**The failure scenario of the chosen approach.** In six months somebody
edits `assets/seals/owl.svg` and does not redraw `.claude-plugin/icon.png`.
The release note and the plugin icon then show the old owl, and nothing in
the suite sees it, because comparing the two needs an SVG renderer the
suite does not have on all three operating systems. `assets/seals/README.md`
states the command and this limit. The second risk is outside the tree: the
directory takes the icon only the first time the plugin is saved or
submitted in its portal (the validator's own sentence), so a later redraw
may not reach the listing.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| The release seal painted from `build()`'s cells, the sprite included, as #1009 built it (keep the structure) | The note shows the 28-cell sprite, which the owner decided a page does not show. The premise that keeps it, *a change to the disc's mark changes the terminal stamp and the release image together* (`release_seal.py`'s docstring), was checked against issue #857's body and does not hold: the owner chose two forms | Rejected |
| `draw` copies the PNG that `plugin.json` names as `icon` (chosen) | The PNG drifts from the SVG when one is edited without the other; stated as a limit | Chosen: one PNG serves the icon, which must be a committed raster, and the release seal |
| The seal job draws `seal.png` from the SVG at release time | A second rasterisation of one SVG beside the committed icon, so the two can differ; the job needs a system renderer, which #1009 refused (`tests/behaviour/test_a_release_publishes_its_note.py`, the `apt-get` assertion) | Rejected |
| The release asset is the SVG itself | Whether GitHub serves a release asset SVG as an image in a note is unverified, and the issue names the asset `seal.png` | Rejected |
| The icon at `assets/icon.png`, which the validator also looks for | `assets/` is a directory the release check treats as the repository's own (`tests/behaviour/test_the_release_check_watches_what_ships.py#STAYS_HOME`), while the icon belongs to what ships; the issue names `.claude-plugin/` | Rejected |
| The icon at 1024 pixels | The note would show it at 512 CSS pixels, three times today's 168, unless a width constant is added | Rejected on Q2's default |
| The sprite in a new file such as `seal-sprite.txt` | Every citation of `seal-mark.txt` and the vocabulary list in `tests/behaviour/test_one_word_one_meaning.py` change for nothing a reader gains; the file still holds the disc's mark | Rejected |
| The sprite typed as a tuple in the module | #832's reason holds: changing the mark is replacing a data file. Checked: the reason is stated at `seal_stamp.py` line 202 onward | Rejected |
| Keep `read_chart` beside `read_sprite`, for a one-tone mark | Two readers of the mark where one file ships, and a chart no file holds | Rejected: a fact has one source |
| The S's neighbour shading applied to the sprite | Issue #857, *Shading breaks a small mark*: every 1-cell feature turns to noise | Rejected |
| The twin writes the sprite's own letters (`K`, `R`, `L`) instead of the colours' | `build`'s `px` answers a colour, so the twin would need to know which cells are the sprite's; the twin's letters were the framer's choice in #832 and no decision of the owner's names them | Rejected: keep `KEY`. The premise, that every sprite colour is one of the nine, was checked by the probe |
| Keep the byte hashes, re-pinned to the owl | A hash taken from the code under test holds the code to itself; the reference case already pins every cell of the owl from an independent transcription | Rejected |
| Keep the size bound as a stored number, 6,000 | A number kept beside the tree to stay in step with it (`CLAUDE.md` *The rule a mechanism is kept against*) | Rejected: the bound is `MESSAGE_BUDGET`, the limit the stamp is actually held to |
| Keep Pillow pinned and installed | A dependency every CI leg and every `.venv` installs for no reader | Rejected: `CLAUDE.md` *The rule a mechanism is kept against*; existing is no reason to keep it |
| Keep Pillow for a case that decodes the icon | The header the case needs (signature, width, height) is 24 bytes the standard library reads | Rejected |

## Verification this work item owes

The owner decided this on 2026-10-27 for #1051, carried it to #1060 on
2026-10-28, and carried it to this work item in the spawn of its framer. It
binds every crafter, proofer and sealer of this work item, and it overrides
any wording in the phase rows below.

- A name or path that moves is proved by the existing cases passing at the
  new path. It owes no new case, no red run and no `seal mutate`. The
  renames of `CHART` to `SPRITE` and the move of `owl-web.svg` are moves.
- A case is written new, and seen red once, only for behaviour that did not
  exist before. The cases this work writes new are listed in the phase
  rows: the copy of the page image and its refusals, the icon's shape, the
  sprite reader, the sprite's colours, and the owl's reference. No phase
  runs `seal mutate`.
- A case that is removed, or that loses its Pillow half, owes no red run.
- A phase runs, in one `bin/test` command, the cases its row names plus the
  modules `git grep -l` finds reading what it changed. The orchestrator's
  broad run after the review rounds is the only sweep of the suite.
- A proofer does not raise a finding that a moved name lacks red-first
  evidence or a mutation run. A sealer does not withhold over it.
- Each phase record names the cases it wrote new, how each was seen red,
  and the existing cases it relied on.

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `.claude-plugin/icon.png`, drawn by `rsvg-convert -w 512 -h 512 assets/seals/candidates/owl-web.svg -o .claude-plugin/icon.png`, with the tool's version in the phase record; `"icon": "./.claude-plugin/icon.png"` in `.claude-plugin/plugin.json`; `release_seal.py#draw` copying the PNG the manifest names and answering its header width divided by `DENSITY`, standard library only, with the refusals of `frame/design.md` *Data & interfaces*; `stamp()`, `CELL_PX` and the Pillow import removed; the docstrings of `release_seal.py` and `seal_stamp.py` (its lines 67 to 72) and the comments of `publish-release.yml` that say the seal is painted from the cells, rewritten in place; the pixel cases and draw reasons of `tests/github/test_release_seal.py` replaced | New cases, each seen red once against the tree before the phase: `draw` writes the manifest's PNG byte for byte and answers its width divided by `DENSITY` (S7); `main` names each draw refusal and edits nothing (S8: no `icon`, no file, not a PNG); the manifest's `icon` is a square PNG of 512 to 2048 pixels under 2,000,000 bytes (S9). Then one `bin/test` over `tests/github/test_release_seal.py`, `tests/behaviour/test_the_release_seal_is_drawn.py`, `tests/behaviour/test_a_release_publishes_its_note.py` and the modules `git grep -l -e release_seal -e plugin.json -- tests` lists; `claude plugin validate .` exits 0 and prints no `ICON_MISSING` | cd6af1be |
| 2 | `seal-mark.txt` holding the owl's sprite; `read_sprite`, `SPRITE`, `SPRITE_PATH`, `SPRITE_MALFORMED`, `SPRITE_CELLS` and `SPRITE_COLOURS` in place of the chart's names; `build`'s sprite rule; the module docstring and comments that describe the chart and the placeholder S, rewritten in place; `broad_gate.py`'s two sentences naming the chart; `tests/skills/test_seal_stamp.py` moved to the sprite (`Test_read_sprite`, `owners_disc`, `Test_build` counting the frame by ring position, `REFERENCE_DISC`, `REFERENCE_TWIN`, the size bound read from `MESSAGE_BUDGET`, the hash case removed); `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`'s pinned docstring sentence | New cases, each seen red once against phase 1's commit: `Test_read_sprite` accepts the shipped sprite and a copy with a byte-order mark and refuses the four faults of S3; `Test_build` rebuilds every cell from the sprite with a letter table written in the test (S1); the reference case transcribed from `c8bb9693:assets/seals/candidates/owl-28-pixel.ans`, the shadow `(78, 8, 12)` read as `DROP`, the frame from today's reference (S2). Then one `bin/test` over `tests/skills/test_seal_stamp.py`, `tests/hooks/test_sealer_stamp.py`, `tests/hooks/test_sealer_stamp_queue.py`, `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, `tests/skills/test_broad_gate.py`, `tests/behaviour/test_one_word_one_meaning.py` and the modules `git grep -l -e seal_stamp -e seal-mark -- tests` lists; `bin/seal stamp` by its path in a UTF-8 terminal shows the owl, and `bin/seal stamp --shape` the twin, both read by the crafter | 5e70612d |
| 3 | Pillow removed: `run_tests.py`'s `PILLOW`, `PILLOW_VERSION`, `has_pillow`, `add_pillow`, its call and its `PACKAGES` entry, and its docstring paragraph; the install lines and comments of `test.yml` and `publish-release.yml`; `CONTRIBUTING.md` *Running the checks*, rewritten in place for three packages; `tests/censuses.py`'s `PIL.Image` entry and its comment clause, and `tests/test_censuses.py`'s case for it; the Pillow halves of the cases `frame/design.md` *Removes* lists | No new case. One `bin/test` over `tests/github/test_run_tests.py`, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py`, `tests/behaviour/test_release_hygiene.py`, `tests/behaviour/test_the_release_seal_is_drawn.py`, `tests/behaviour/test_a_release_publishes_its_note.py`, `tests/test_censuses.py` and the modules `git grep -l -i pillow -- tests` lists before the phase; `git grep -n -i -e pillow -e 'import PIL' -e 'from PIL'` outside `changelog/`, `CHANGELOG.md` and `seal/` matching only `assets/seals/README.md`'s sentence on how the previews were drawn | cefb7abe |
| 4 | `assets/seals/candidates/owl-web.svg` moved by `git mv` to `assets/seals/owl.svg`; `owl-28-pixel.txt`, `owl-28-pixel.ans`, `owl-28-pixel.png` and `owl-web.png` removed; `assets/seals/owl.ans`, the stamp over `SAMPLE_ROWS` as the README's command draws it; `assets/seals/owl.png`, drawn by the README's preview rule; `assets/seals/README.md` with the owl's entry (releases 0.23.1 onward, issue #857, the terminal's command naming v0.23.1, the page form `owl.svg` and the icon's `rsvg-convert` command, and the limit that nothing checks the PNG against the SVG), the placeholder S closed at 0.23.0, *The next entry* rewritten, the owl's candidate section cut to the bee, and the letters cited from `SPRITE_COLOURS`; the changelog fragment `changelog.md` of this work item, with a *Removed* entry for Pillow | `cmp` of `owl.ans` against the command's output run against the working tree (S11); the crafter's preview renderer first redraws `placeholder-s.png` and matches it pixel for pixel, then draws `owl.png`; one `bin/test` over `tests/behaviour/test_one_word_one_meaning.py`, `tests/test_censuses.py` and the modules `git grep -l -e assets/seals -e candidates -- tests` lists; `git grep -n -e owl-web -e owl-28-pixel -- . ':!seal' ':!changelog' ':!CHANGELOG.md'` matching nothing | 0b2e6a53 |

## Operational impact

- **No installed repository migrates.** Nothing a user's repository holds
  names the mark, the chart or Pillow. A values file a hook queued before
  the update draws with the new disc, because the rows carry no disc.
- **Every install carries the icon.** `.claude-plugin/` ships, so
  `.claude-plugin/icon.png` reaches the plugin cache of every user; at 512
  pixels the PNG is about 68 KB (executed: the framer's render at that size
  was 67,791 bytes). Claude Code ignores the field at load time.
- **The directory listing may keep no icon.** The validator says the file
  becomes the listing icon only the first time the plugin is saved or
  submitted in the directory's portal. Whether that has happened for this
  plugin is the owner's to know; this work adds the icon either way.
- **`bin/test` stops installing Pillow.** A `.venv` that holds it keeps it,
  and nothing reads it. A contributor's fallback command is shorter by one
  package.
- **This run's own stamp shows the S.** The `Stop` hook and `seal stamp` on
  PATH are the installed 0.23.0 plugin's, so the stamp drawn when this work
  item's sealer writes `sealed` carries the placeholder S. The tree's
  `bin/seal stamp`, run by its path, shows the owl.
- **`.test_durations`.** The removed cases leave stale keys and the new
  cases are unpriced. The share is a few cases of the suite; whether it stays
  under `STALE_SHARE` is unverified, and the orchestrator's broad run
  answers it.
- **The 0.23.1 release note shows the owl's page image** at 256 CSS
  pixels, where 0.23.0's showed the sprite disc at 168.
- No new dependency, no new environment variable, and no gate decides
  anything differently.

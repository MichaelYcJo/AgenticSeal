# Phase 2: 1793593418-two-config-rows-show-the-seal-mark

## What this phase found

### The frame, checked before the build

The frame holds for phase 2, with one exception in where the row is read.
Every coordinate `frame/design.md` and `frame/plan.md` give for this phase
was opened at `e20307530` and stood as stated (read). The module docstring
of `.github/scripts/release_seal.py` opens at `:1`, and the paragraph
holding its re-run sentence is at `:27-39`. `#seal_release` is at `:468-531`, and its header guard is at
`:505-512`. `.github/scripts/publish_release_note.py#sealed_header` is at
`:644-663`, and the module docstring names it at `:94`. The workflow's
comment on the `seal` job is at `.github/workflows/publish-release.yml:24-37`.
`tests/github/test_release_seal.py#PULLS` exists. `templates/setup/config.md`
holds phase 1's `## The seal mark` section with the pull-request row alone.

The exception is the read's place. `frame/plan.md` *Technical context* puts
the row's read after the header guard and before the upload. `#seal_release`
calls `draw` before that guard, at `:497`, and `draw` refuses where the
manifest or the icon cannot be read. Read after the guard, an off row would
still run the draw, and a draw refusal would end the run with no results in
the note, over an image the note does not show.

### Decision: the row is read before the draw

`release_seal.py#mark_on` is called before `draw`, and `draw` runs only where
the row reads `yes`. The upload still comes after the header guard, so a run
that will not edit uploads nothing under either answer, which is what the
plan's placement was for. Judged against `frame/design.md` *Scope* item 4,
"Under any other answer it attaches nothing", and `frame/plan.md` *Technical
context*, the release seal.

### Decisions settled while writing the code

- **Where the row is read from.** The `seal/` root is
  `hooks/lib/optin.py#home_at` of the tree `ROOT` names, and the row is read
  through `hooks/lib/config.py#declared_value`, the one reader of a row. Both
  modules are loaded through `release_seal.py#module`, so a module that will
  not load ends in today's note and an exit of 0, as every other load there
  does. Judged against `frame/design.md` *Grounding*, the row on
  `config_value`, and the module's own rule that every failure exits 0.
- **The warning's prefix.** A row that is written and does not turn the
  image on is named on one line opening `::warning::release seal image: `.
  The failure line `release seal skipped:` is not reused, because the run
  goes on and puts the results in the note. The sentences are
  `ROW_NOT_YES` and `ROW_REFUSED`, and the S6 case pins each one in full.
  Judged against `frame/design.md` *Data & interfaces*, the lines a reader
  sees, and contract rule 14.
- **The off path writes once.** Under any answer but `yes` the run makes one
  `gh release edit` and no upload, and prints `put the seal's results in
  <tag>'s note, with no image`. Its edit failure carries no clause about an
  uploaded asset, because none was uploaded.
- **`sealed_header` keeps its signature.** Its first argument, `image_url`,
  is None for the one-cell table, and `alt` and `width` are then not read.
  The two-cell path is unchanged byte for byte.
- **A guard removed after its mutant survived.** The build first returned
  off where `home_at` answered no root. The mutant that removed that guard
  survived, because `config.py#config_text` already reads a falsy root as no
  file. The guard and the case written for it went in `9cde32020`. Judged
  against `skills/core/SKILL.md` *The rule a mechanism is kept against*, "A
  fact has one source".

### The cases, and how each was shown red

The new cases were written before the code and ran against the code at
`e20307530` (executed, exit 1): 8 failed and 26 passed. The 6 cases of
`tests/github/test_release_seal.py#Test_main::test_a_row_other_than_yes_attaches_nothing_and_puts_the_results_alone`
failed on the upload their first assertion forbids. The S7 case of
`tests/github/test_publish_release_note.py` failed with `AttributeError` on
`html.escape(None)`. The front door's `Release note seal mark` failed with
"the skill does not name `Release note seal mark`". After the build, both
release modules read 105 passed (executed, exit 0).

The re-run case gained an `absent` variant for S8. It passes against the old
code, since the exact-header guard it pins predates this work, so it was
shown red with that guard removed, as the table below records.

The fixture tree in `tests/github/test_release_seal.py#wired` now writes
`seal/config.md` with the row reading `yes` unless a case names another
value, so every case that predates this work reads the image path as
before.

### Mutations

`seal mutate` ran after the build commit `36552460e`, one command per unit,
with `bin/test <module> -q -p no:xdist -k <cases>`. Each run restored the
file from its held bytes, and `git status --short` was empty after the runs
(executed).

| Mutant | Cases run | Result |
|---|---|---|
| S6: `on, unread = mark_on(ROOT)` read as `on, unread = True, None`, the row's read alone removed | `-k 'other_than_yes and absent'` | red: the upload then ran |
| S4's rule for this row: `value != MARK_ON` read as `value.casefold() != MARK_ON` | `-k 'other_than_yes and Yes'` | red: the `Yes` case read the upload |
| the refusal's return removed | `-k 'other_than_yes and twice'` | red |
| the warning's print read as `if False:` | `-k 'other_than_yes and on'` | red: 4 cases, every one that names a value |
| the guard on no root removed | a case written for it | survived, then removed with the case (above) |
| S8: the header guard read as `if False:` | `-k 'second_run and absent'` | red |
| the off path's `if not on:` read as `if False:` | `-k 'other_than_yes and absent'` | red |
| the on path's `if on:` before the image read as `if False:` | `-k accepts_a_published_note` | red |
| S7: `sealed_header`'s `if image_url is None:` read as `if False:` | `-k given_no_image` | red |
| S7: the one-cell `table(lines)` read as `table([''], lines)` | `-k given_no_image` | red |

### The phase-boundary run

One command, under `bash` (executed, exit 0), at `9cde32020`:
`bin/test <97 modules> -q && bin/seal layout --check tests`. The 97 modules
are every test module under `tests/` whose text names
`release_seal`, `publish_release_note`, `publish-release`, `seal/config.md`,
the config template or the config skill, every one that names
`.github/scripts` or `.github/workflows`, every one that globs or lists files
and names `skills`, `templates` or `.github`, and
`tests/test_censuses.py`, `tests/hooks/test_launch.py`,
`tests/behaviour/test_the_release_seal_is_drawn.py` and
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`. The suite part
read 5095 passed and 14 skipped. The layout check read 149 files and refused
none. `bin/seal layout --pairs` over the two release test modules named 0
pairs (executed, exit 0). `uvx ruff check` and `uvx ruff format --check` over
the five changed Python files exited 0 (executed).

S10, read on the diff: `git diff --stat 09d7e5c8f HEAD` over
`skills/verify/scripts/seal_stamp.py`, `skills/verify/scripts/seal-mark.txt`,
`hooks/sealer-stamp-queue.py`, `hooks/sealer-stamp.py` and
`.claude-plugin/plugin.json` printed nothing (executed, exit 0).

### Other places that state the image as unconditional

Found with `git grep -i` on "two cells", "two-cell", "seal.png",
"sealed_header", "attaches the page form" and "release seal", outside
`seal/threads/` (executed). That is a search on wordings, so the list is a
sample (contract rule 12). The code's own text is rewritten in place. What
stands:

- `docs/branch-and-release.md` *Cutting a release* and
  `docs/release-checklist.md` *6. After the merge*: the design's
  `## Rule changes` change both, at the settle.
- `TRADEMARKS.md:18`, "the release seal image, `seal.png`, that a release
  note attaches", and `assets/seals/README.md:180`, "the release note's
  `seal.png` is a copy of that icon": both hold for a release whose row reads
  `yes`, which this repository's does.
- `tests/github/test_publish_release_note.py`, the docstring of
  `test_the_header_is_built_by_one_function_and_its_sealed_twin_by_another`,
  "the same table with two cells": that case builds the header with an
  image, and the S7 case beside it holds the other shape.

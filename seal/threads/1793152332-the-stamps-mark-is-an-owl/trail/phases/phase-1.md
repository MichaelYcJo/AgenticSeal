# Phase 1: 1793152332-the-stamps-mark-is-an-owl

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | cd6af1be |

## What this phase was asked

Build `frame/plan.md` row 1 and nothing of phases 2 to 4. Draw
`.claude-plugin/icon.png` from the owl's SVG at the size `questions.md` Q2's
default gives, 512 pixels, and name it in `plugin.json` as `icon`. Make
`.github/scripts/release_seal.py#draw` copy that PNG as `seal.png` with the
standard library only. Replace the release seal's pixel cases with the new
cases the row names. Every path is built from single segments with
`os.path.join`, and a constant spelt with `/` is split before it is joined.
`claude plugin validate .` must pass with no `ICON_MISSING`. One `bin/test`
command runs the row's named cases and the modules `git grep -l` finds
reading what changed. No `seal mutate` run.

## What this phase found

**The icon.** `rsvg-convert` 2.58.4 (`/opt/homebrew/bin/rsvg-convert`) drew
`assets/seals/candidates/owl-web.svg` at 512 by 512 pixels. The PNG is 8-bit
RGBA and 67,791 bytes, the size the framer measured. Opened as an image, it
shows the owl on the red disc with its masks and shadow.

**`draw` reads the manifest under `ROOT`, not `CODE`.** `frame/design.md`
*Data & interfaces* says the manifest is read "under `CODE`". The module
already uses two names for the one checkout at the tag. `CODE` is where it
loads its own modules from. `ROOT` is the tree it reads data from, and a
case can point `ROOT` at a fixture without moving `CODE`. The manifest and
the icon are data of that tree, so they are read under `ROOT`, and the
comment above the two names now says so. In the release job the two are the
same path, so what the seal attaches does not change. A case could not have
pointed `CODE` at a fixture: `publisher()`, `gate()` and `readers()` load
modules from it during the same `main()` run.

**The new cases, and how each was seen red.** Each was run once against
`71bed8ff`, with the cases written and the code not yet changed:

- `tests/github/test_release_seal.py::Test_draw::test_copies_the_png_the_manifest_names_and_answers_its_width_over_density`
  (S7) failed with `assert 168 == 5`: the old draw painted the stamp's cells
  and answered their width.
- `Test_main::test_refuses_on_any_failure_and_leaves_the_note_as_published`,
  the four new parameters `the manifest cannot be read`,
  `the manifest names no icon`, `the icon is not there` and
  `the icon is not a PNG` (S8), each failed with `assert 0 == 1` on the
  count of `::warning::` lines. The old draw read no manifest and painted
  the seal, so no refusal was printed.
- `tests/behaviour/test_chain_hooks_hardening.py::test_the_plugin_icon_is_a_png_the_directory_accepts`
  (S9) failed with `assert None == './.claude-plugin/icon.png'`: the
  manifest had no `icon`.

The fifth draw parameter, `the PNG cannot be written`, passed against the
old draw. That refusal existed before, so its case was rewritten for a draw
without Pillow, and under the work item's verification direction a
rewritten case for existing behaviour owes no red run. It makes the copy
fail by giving `tempfile.mkdtemp` a directory that does not exist.

**Removed cases.** `test_the_png_is_the_stamps_cells_one_square_block_each`,
`test_the_png_follows_whatever_chart_the_stamp_module_has` and
`test_the_release_script_loads_with_pillow_blocked`, the helpers `stamp`,
`blocks` and `pillow_that_cannot_save`, and the reasons
`Pillow is not installed`, `the stamp's module will not load` and
`the PNG cannot be saved`. The tests now build the fixture PNG with
`struct` and `zlib`, so `tests/github/test_release_seal.py` no longer
imports Pillow.

**What else stated the old fact.** `git grep` for the painting
(`CELL_PX`, `stamp's cells`, `square block`, `own cells`, `from its cells`)
found two places beyond what the row names, and both stay for phase 3:

- `docs/branch-and-release.md` line 63 is in the policy root. The frame's
  `## Rule changes` holds its new wording for the settle to write, so this
  pull request does not edit it.
- `.github/scripts/run_tests.py` lines 66 to 71 say Pillow draws the seal
  and the pixel cases read it. That paragraph explains the Pillow pin, and
  phase 3 removes the paragraph with the pin. `.github/workflows/test.yml`
  line 144, `CONTRIBUTING.md` lines 87 to 90, and the messages `add_pillow`
  prints, which `tests/github/test_run_tests.py` pins, describe the pin in
  the same way. All of them are phase 3's rows in `frame/design.md`
  *Removes*. From this commit until phase 3, they describe a Pillow reader
  that no longer exists.

The `publish-release.yml` install step still installs Pillow, and phase 3
removes that line. The comment above the step said Pillow also draws the
seal, and that sentence went in this phase.

**The run.** One `bin/test` command ran 1,560 cases: 1,550 passed, 9 were
skipped and 1 failed. It covered the three modules the row names, every
module `git grep -l -e release_seal -e plugin.json -- tests` lists, and the
modules `git grep -l -e publish-release -e seal_stamp -- tests` lists,
because this phase also changed `publish-release.yml` and `seal_stamp.py`'s
docstring. The failure is
`test_every_spec_directory_that_reached_the_ladder_has_an_overview`. It
wants a `gaps.md` in every work item whose frame exists, and this work
item's directory had none at `71bed8ff`. Row 1 does not ask for a
`gaps.md`, so this phase did not write one. Until a later party writes it,
the case fails.

**The validator.** `claude plugin validate .` on Claude Code 2.1.312 exited
0, reported no `ICON_MISSING`, and printed one warning that predates this
work: `CLAUDE.md` at the plugin root is not loaded as project context.

# Guarantee: 1792624592-the-release-seal-is-drawn-from-the-stamps-cells

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md is written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` *The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | 97ac7878 against a16acb40; earlier run: 001098c2 withheld |
| Broad gate | 53f8cedf against eae7f0ad |

The base `release/v0.22.3` resolves to a16acb40, which is #986's merge on top
of eae7f0ad. The merge base of HEAD and a16acb40 is eae7f0ad, so the diff
audited, `git diff a16acb40...HEAD`, is the diff the broad run and both
rounds read against eae7f0ad (executed).

This run follows the run at 001098c2. The one commit since, 97ac7878, touches
only this file (executed `git diff --name-only 001098c2 HEAD`), so no claim's
coordinate changed in the tree, and the rows below stand as that run executed
them. The pull request body changed outside the tree in one cell, the `git
grep` row's result. It was read again in full, and that row was re-run at
97ac7878.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run's record is at HEAD, or only this work item's records follow it | `broad-gate.md:5` | executed `git log --no-merges --name-only 53f8cedf..HEAD ^a16acb40`: one commit, 001098c2, touching only `broad-gate.md`; 53f8cedf is an ancestor of HEAD | holds |
| The broad run passed: ruff check and format clean, 7425 passed and 13 skipped, chain-check exit 0 | the orchestrator's spawn prompt; the pull request body | read the orchestrator's `broad-gate.log` in its scratchpad: `BROAD GATE PASSED ... @ 53f8cedf against origin/release/v0.22.3 @ eae7f0ad`, `suite 7425 passed, 13 skipped`, `chain exit 0`; not re-run, by the sealer's rule | holds |
| Every new case, and every case through the stand-in for `draw`, failed against the tree before `draw` existed | `phases/phase-1.md:63` | executed, in a clone at 001098c2 with `release_seal.py`, `release-seal.svg`, `run_tests.py` and `publish-release.yml` restored from eae7f0ad: pytest over S1, S2, S6, S3's case, every parameter of the failure case, S7's case and S9's case | holds: 22 failed, 0 passed; S1 and S2 on `has no attribute 'draw'`, S7 on `6 == 5`, S9 on the missing `Pillow draws the release seal` |
| S1 went red with cell (14, 14) painted black in `draw` | `phases/phase-1.md:67` | executed, in a clone at 001098c2, `draw` painting (0, 0, 0) at (14, 14), then S1 | holds: `[(14, 14, [(0, 0, 0, 255)])] == []` failed |
| S2 went red with `draw` loading a copy of the stamp's module of its own | `phases/phase-1.md:70` | executed, `draw` loading `seal_stamp.py` through `module()` under a second name, then S1 and S2 | holds: S2 failed at its `blocks` assertion, S1 passed |
| S6 went red with Pillow imported at the module's top | `phases/phase-1.md:72` | executed, a module-level `__import__("PIL")` added, then S6 | holds: `ModuleNotFoundError: import of PIL halted` |
| S3 went red with the width 168 written into `seal_release` | `phases/phase-1.md:73` | executed, `width = 168` in place of `draw`'s answer, then S3's case | holds: the sealed note differed from the expected one |
| S7's `apt-get` half went red with an `apt-get` command in the pip step | `phases/phase-2.md:57` | executed, `sudo apt-get install -y librsvg2-bin;` put in front of the pip step's command, then S7's case | holds: failed at `test_a_release_publishes_its_note.py:741` |
| `draw` writes an RGBA PNG of 336 by 336 pixels and answers 168 | `phases/phase-1.md:62` | executed `release_seal.py#draw` once at 001098c2 under the worktree's `.venv` Python | holds: `RGBA (336, 336) 168` |
| The changed modules pass at HEAD, and `seal_stamp.py` still loads with Pillow blocked | the pull request body, *What changes for an installed repository* | executed pytest at 001098c2 over `test_the_release_seal_is_drawn.py`, `test_a_release_publishes_its_note.py`, `test_no_real_identifiers.py`, `test_release_hygiene.py`, S9's case and `test_the_stamp_module_imports_with_pillow_blocked` | holds: exit 0, 134 passed |
| Cross-platform `tests` run 39695956247 at 736062fe and run 39697436778 at 478da5c6 passed on every leg | the pull request body, *How it was verified* | executed `gh run view` on both: each completed with conclusion success, every pytest leg and lint success, `release-report` skipped; `git diff --name-only 478da5c6 HEAD` names only this work item's records | holds |
| `spec.md` `## Removes`: the SVG file, `rasterise`, `SVG`, `SEAL_PX` | `spec.md:142-144` | executed `ls .github/scripts/release-seal.svg` and `git grep` for the names outside `seal/specs`, `changelog`, `CHANGELOG.md` and `.test_durations` | holds: no file, exit 1 |
| `## Removes`: the install step, the install case, the step count's comment, the three failure parameters, the SVG cases and fixtures, `wired`'s `rsvg` argument, the W3C namespace host's exemption, the `draws the release seal` not-in pin, the `Pillow only reads it` sentence | `spec.md:146-154` | executed `git grep -n -E` for each removed name and sentence, and a grep of `tests/test_the_release_seal_is_drawn.py` for `LAYERS`, `RED`, `NS`, `SVG`, `points`, `svg_tree` and `rsvg` | holds: exit 1 for both |
| `## Removes`: the docstring and comment sentences naming the SVG in `release_seal.py`, `publish-release.yml`, the test module, `run_tests.py`, `CONTRIBUTING.md` and `seal_stamp.py` | `spec.md:145`, `spec.md:149`, `spec.md:153`, `spec.md:155-156` | executed `git grep -n -i -E "svg\|owner's seal"` over those files | holds: one match, `tests/test_a_release_publishes_its_note.py:717`, which says how a case was seen red against the removed step |
| S8: outside `seal/specs/`, `changelog/` and `.test_durations`, the grep finds only the three `## Rule changes` sentences | `phases/phase-2.md:63` | executed `git grep -n -i -e rsvg -e release-seal.svg -e librsvg -- ':!seal/specs' ':!changelog' ':!.test_durations'` | holds: `docs/branch-and-release.md:63-64`, `docs/release-checklist.md:242` and `:248` |
| The same grep, outside `seal/specs/`, `changelog/` and `.test_durations`, finds only the four lines of the three `## Rule changes` sentences | the pull request body, *How it was verified*, the `git grep` row, as rewritten after the run at 001098c2 | executed at 97ac7878 `git grep -n -i -e rsvg -e release-seal.svg -e librsvg -- ':!seal/specs' ':!changelog' ':!.test_durations'` | holds: `docs/branch-and-release.md:63-64`, `docs/release-checklist.md:242` and `:248`. The row's earlier wording, outside this work item's records alone, did not hold at 001098c2 |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | `release_seal.py` paints `seal_stamp.py#build`'s cells, 12 pixels each, with Pillow imported inside `draw`; the SVG, `rasterise`, `SEAL_PX` and the `rsvg-convert` step go; `docs/` changes only through three `## Rule changes` items; S7 and S9 as the overview's divergences amended them at 5e2b93de | the issue body's three changes and its Out list; the build; the last round | none |
| the build | phases 1 and 2 at 46a773ea and ed9ec343, and round 1's fix at b4772c74, deliver S1 to S9; the tree at 001098c2 holds them | the spec; the claims re-run above | none |
| the last round | round 2 at 478da5c6 confirms round 1's three findings fixed at b4772c74 and opens nothing; the full suite and the tag push are left to the orchestrator and the owner | the build; the broad run at 53f8cedf, whose only later source commit is round 2's record | none |
| the changelog | the seal is the stamp's disc, 12-pixel cells, 336 pixels shown 168 wide; the SVG and the install step are gone; a missing Pillow or stamp module fails the suite at the tag first | the spec; the build; the drawn PNG; round 2's confirmation of round 1's third finding | none |
| the pull request body | what changes, as the changelog says; Q1 built on its default and open for the owner; how it was verified | the changelog, the phase records, both rounds, the CI runs, the broad run's log, and the tree for every sentence, the `git grep` row included | none |

The issue body's third change says the case reads the PNG at each cell's
centre. S1 compares every pixel of every cell's block, which holds that
property and more, so the two do not disagree (read).

Verdict: sealed

# Closing memo: 1794390764-scripts-load-a-reader-from-its-sibling

## Not verified

| Item | Who must answer |
|---|---|
| closed Phase 1: the full suite, lint and typecheck at HEAD; the phase ran its phase-boundary set alone | answered: the work item's broad run, `trail/gate.md` at `b118dbf17` against `3285f1a04`, on which `guarantee.md` sealed |
| closed Phase 1: `lib/sibling.py#_same` on Windows, where `__file__` and the path `load` builds may differ in case or separator, and `normcase` with `realpath` is what makes them one; no case runs on Windows here | answered: push run 45961118285 of `tests` at `7dda126fe` on `main`, whose ubuntu 3.12 and 3.14, macOS 3.12 and four windows-latest 3.12 legs passed, runs the cases this row names, which the tree still holds |
| closed Phase 1: `frame/questions.md` Q1 outside the phase-boundary set: whether a test file the set does not hold meets one `lib/` module instance shared by every script in its `pytest` process | answered: the work item's broad run, `trail/gate.md` at `b118dbf17` against `3285f1a04`, on which `guarantee.md` sealed |
| closed Phase 2: the full suite, lint and typecheck at HEAD; the phase ran its phase-boundary set alone | answered: the work item's broad run, `trail/gate.md` at `b118dbf17` against `3285f1a04`, on which `guarantee.md` sealed |
| closed Phase 2: the five workflows that run the scripts under `.github/scripts/` (`close-issues-on-release.yml`, `label-merged-on-release-branch.yml`, `hygiene.yml`, `publish-release.yml` and `test.yml`) on GitHub's runners; the scripts ran here only under their test modules and copied alone | answered: on GitHub's runners, push run 45961118285 of `tests` at `7dda126fe` on `main`, `publish-release.yml` run 45961118268, `close-issues-on-release.yml` run 45961118322, the `hygiene` run 45961044479 and the `label-merged-on-release-branch.yml` run 45960301015 of #1647 all passed |
| closed Phase 3: the full suite, lint and typecheck at HEAD; the phase ran its phase-boundary set alone, under pytest-xdist | answered: the work item's broad run, `trail/gate.md` at `b118dbf17` against `3285f1a04`, on which `guarantee.md` sealed |
| closed Round 1's fix pass: the full suite, lint and typecheck at HEAD; the pass ran the phase-boundary set over the paths it changed, and the test modules of `lib/sibling.py`'s callers that catch an absent module | answered: the work item's broad run, `trail/gate.md` at `b118dbf17` against `3285f1a04`, on which `guarantee.md` sealed |
| closed Round 2's fix pass: the full suite, lint and typecheck at HEAD; the pass ran the phase-boundary set over the paths it changed | answered: the work item's broad run, `trail/gate.md` at `b118dbf17` against `3285f1a04`, on which `guarantee.md` sealed |

## Not done

Phase 1: the guard inside a function, which would keep a copied-alone
`settle.py`, `fold_check.py`, `pact_check.py` and `payload_meter.py` at
exit 0 for `--help`. It was within reach and not taken: the guard would be
spelt in each getter or behind one more getter that every call goes
through, and the reason `frame/design.md` *Scope* item 2 gives for the
lazy placement, G10, holds at import for these four.
`trail/phases/phase-1.md` *What this phase found* gives the grounds and the
measurement.

Phase 2 left two items, and phase 3 built both after the framer's fold
at `0f9354a3b`. `rules.py` and `release_report.py` guard their lazy
`import sibling`, so a lone copy run with arguments that reach a load
exits 2. `loaded_by` reads no path under `tests/`, so `ruff.toml`'s floor
table no longer holds the eight files the runner's `PINS` pulled in.
`trail/phases/phase-3.md` *What this phase found* gives the commits and
the mutants.

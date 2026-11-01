# Closing memo: 1793521560-the-checks-wait-starts-before-a-check-reports

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the format check at the work item's head. Phase 1 ran its phase-boundary set of 27 modules and ran `ruff check` and `ruff format --check` on its two changed Python files alone (contract rule 2). Two cases of that set skip without the whole suite collected: `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` at lines 347 and 487 | answered by `trail/gate.md`: the broad gate row of `seal/config.md`, the full suite with the repository-wide `ruff check` and `ruff format --check`, passed at `4dbf8441 against 813665f0` (read by the settle that opens 0.27.3); the whole suite is collected there, so the two cases that skip without it ran |
| closed The new paragraph followed on a live pull request, S1 and S2 of `frame/design.md`. No run of phase 1 pushed or opened a pull request, so whether the poll ends on the pushed commit and within the limit is measured where `frame/questions.md` Q1 says | re-homed to #1265, a measurement no record holds |
| closed The version move read by the release check that guards it. The `hygiene` workflow's version arm fails a release pull request, one whose base is `main`, that changes what ships without moving the version. Phase 2's pull request goes into `release/v0.27.2`, so that arm reads the move only at the release pull request. Phase 2 ran the test modules that read `.claude-plugin/plugin.json`, which is not the workflow on GitHub | answered by the `hygiene` run 41307757575 on the release pull request #1251 into `main`: its `release` job printed `version: 0.27.1 -> 0.27.2` and passed |

## Not done

nothing

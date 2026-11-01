# Closing memo: 1793521560-the-checks-wait-starts-before-a-check-reports

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the work item's head. Phase 1 ran its phase-boundary set of 27 modules and ran `ruff check` and `ruff format --check` on its two changed Python files alone (contract rule 2). Two cases of that set skip without the whole suite collected: `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` at lines 347 and 487 | the orchestrator, by `seal gate` after the review rounds settle |
| The new paragraph followed on a live pull request, S1 and S2 of `frame/design.md`. No run of phase 1 pushed or opened a pull request, so whether the poll ends on the pushed commit and within the limit is measured where `frame/questions.md` Q1 says | the orchestrator, at this work's pull request, after its first push |
| The version move read by the release check that guards it. The `hygiene` workflow's version arm fails a release pull request, one whose base is `main`, that changes what ships without moving the version. Phase 2's pull request goes into `release/v0.27.2`, so that arm reads the move only at the release pull request. Phase 2 ran the test modules that read `.claude-plugin/plugin.json`, which is not the workflow on GitHub | the `hygiene` workflow, at the release pull request into `main` |

## Not done

nothing

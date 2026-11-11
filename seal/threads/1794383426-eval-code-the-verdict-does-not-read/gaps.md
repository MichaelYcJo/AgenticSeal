# Closing memo: 1794383426-eval-code-the-verdict-does-not-read

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check over phase 1's tree. Every module file runs `tests/censuses.py` through `census_case`, and phase 1 ran only the phase boundary set. | the orchestrator, at the broad gate |
| The full suite, the repository-wide lint and the format check over phase 2's tree. Phase 2 changed `tests/censuses.py`, which every module file runs through `census_case`, and ran only the phase boundary set. | the orchestrator, at the broad gate |

## Not done

`.test_durations` keeps the 172 entries of the cases this work item removed or renamed, 123.8 s of the file's 1,616.5 s (7.66 %), against `frame/design.md` Scope 12. `CONTRIBUTING.md` *Running the checks* says a work item never commits the file, and gives its refresh to whoever prepares the release, from the release pull request's `durations` union. Past `.github/scripts/durations_union.py#STALE_SHARE`, 5 %, that job is red on the release pull request until the refresh, or until #1486 removes the file. `trail/phases/phase-2.md` gives the grounds.

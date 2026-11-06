# Closing memo: 1793922919-three-link-cases-skip-on-windows-by-platform

## Scope confirmation

Four link cases make their links through `tests/conftest.py#symlink_or_skip` in place of `Path.symlink_to`: the three of `tests/skills/test_agentic_pytest_record.py` that issue #1247 names, whose three `skipif(os.name == "nt")` decorators are removed, and `tests/github/test_finding_counts.py`'s `test_rounds_that_cannot_be_listed_read_not_read_in_every_cell`, which made its link with no skip; no other file of the suite changes.

## Not verified

| Item | Who must answer |
|---|---|
| closed whether the three cases pass on the `windows-latest` legs, or skip there with `symlink_or_skip`'s reason, now that they try to make links there | run 42134062891 at `54286764`, read by the orchestrator with `gh run view 42134062891 --log`: every job succeeded, and none of the 35 `SKIPPED` lines of the four Windows legs names `test_agentic_pytest_record.py` or `symlink_or_skip`'s reason |
| The full suite, the repository-wide lint and the typecheck at HEAD. Phase 1 ran the two test files it changes, on macOS alone | the orchestrator, at the broad gate |
| closed whether `test_rounds_that_cannot_be_listed_read_not_read_in_every_cell` still passes on the `windows-latest` legs at `ad9943fd`, where it makes its link through `symlink_or_skip`. Run 42134062891 ran it before that commit, with the bare `Path.symlink_to` | run 42135588653 at `8a038181`, read by the orchestrator with `gh run view 42135588653 --log`: every job succeeded, and none of the 35 `SKIPPED` lines of the four Windows legs names `test_finding_counts.py` or `symlink_or_skip`'s reason; round 2 read the case's durations in that run's Windows artifact as a run, not a skip |

## Not done

nothing

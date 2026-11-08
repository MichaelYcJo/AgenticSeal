# Closing memo: 1794178397-a-durations-refresh-costs-no-round

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the format check at the branch's head; phase 1 ran `tests/github/test_durations_union.py` and `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, and the lint and format check over `.github/scripts` and `tests/github` | the orchestrator, at the broad gate |
| whether `durations_union.py --stale-fails` reads a real union of the four Windows parts and prints its sentence in a GitHub step summary; the cases drive it over fixture parts with the summary written to a file, and no run of the `durations` job passes the switch before phase 2 wires it (`frame/questions.md` Q1) | a measurement: the `durations` job on 0.36.0's release pull request, read by the orchestrator of that release |

## Not done

`seal layout --check` reports eight functions of
`.github/scripts/durations_union.py` with no class of their own:
`arguments`, `durations_map`, `emit`, `find_parts`, `read_map`, `rendered`,
`report` and `union`. The report stood before this phase, and each of those
functions is reached through `Test_main`. Giving each its class is a
rebuild of the module's tests, which `CONTRIBUTING.md` *The test layout*
reserves for a module whose old files cost past its threshold. That is
beyond what *Scope* item 2 asks, so this phase added only `Test_staleness`
and `Test_verdict`, the classes of the two functions it wrote.

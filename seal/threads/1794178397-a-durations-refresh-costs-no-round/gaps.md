# Closing memo: 1794178397-a-durations-refresh-costs-no-round

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the format check at the branch's head; phase 1 ran `tests/github/test_durations_union.py` and `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, and the lint and format check over `.github/scripts` and `tests/github`; phase 2 ran the 45 modules under `tests/` that name `CONTRIBUTING`, `test.yml` or the workflows directory, and the lint and format check over the Python files it changed | the orchestrator, at the broad gate |
| whether `durations_union.py --stale-fails` reads a real union of the four Windows parts and prints its sentence in a GitHub step summary; the cases drive it over fixture parts with the summary written to a file (`frame/questions.md` Q1) | a measurement: the `durations` job on 0.36.0's release pull request, read by the orchestrator of that release |
| whether GitHub evaluates the two expressions of the `durations` job as phase 2 reads them: the one ending the union step's line giving `--stale-fails` on a pull request into `main` and nothing on every other run, and `hashFiles('union/.test_durations')` matching the union file, whose name starts with a dot, so the upload runs after a red verdict and is skipped after a refusal; the cases read the workflow's text, PyYAML parsed it, and no `actionlint` or GitHub run evaluated either expression (`frame/questions.md` Q1) | a measurement: this branch's pull request run, where the job must ask no verdict and must upload the union, and the `durations` job on 0.36.0's release pull request, where it must ask it, both read by the orchestrator |

## Not done

`seal layout --check` reports eight functions of
`.github/scripts/durations_union.py` with no class of their own:
`arguments`, `durations_map`, `emit`, `find_parts`, `read_map`, `rendered`,
`report` and `union`. The report stood before phase 1, and each of those
functions is reached through `Test_main`. Giving each its class is a
rebuild of the module's tests, which `CONTRIBUTING.md` *The test layout*
reserves for a module whose old files cost past its threshold. That is
beyond what *Scope* item 2 asks, so phase 1 added only `Test_staleness`
and `Test_verdict`, the classes of the two functions it wrote.

`.test_durations` keeps the entry of the case phase 2 removed,
`test_the_durations_file_prices_the_suite`, at 0.016 s. This work makes the
rule that no work item commits the file, so phase 2 left it. The next
release refresh, taken from a union that no longer holds the case, drops
the entry.

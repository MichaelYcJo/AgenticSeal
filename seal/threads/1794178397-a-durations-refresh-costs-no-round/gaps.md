# Closing memo: 1794178397-a-durations-refresh-costs-no-round

## Not verified

| Item | Who must answer |
|---|---|
| closed the full suite, the repository-wide lint and the format check at the branch's head; phase 1 ran `tests/github/test_durations_union.py` and `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, and the lint and format check over `.github/scripts` and `tests/github`; phase 2 ran the 45 modules under `tests/` that name `CONTRIBUTING`, `test.yml` or the workflows directory, and the lint and format check over the Python files it changed | answered by the work item's broad gate, `trail/gate.md` `run: 8c5217fb against 94d04d30`, which names no failing case and on which `guarantee.md` sealed |
| closed whether `durations_union.py --stale-fails` reads a real union of the four Windows parts and prints its sentence in a GitHub step summary; the cases drive it over fixture parts with the summary written to a file (`frame/questions.md` Q1) | answered by run 42564261755, the `tests` run of the 0.36.0 release pull request #1457: its `durations` job found the four `test-durations-*` artifacts, ran `durations_union.py ... --stale-fails` over them and passed, read by the settling session with `gh run view 42564261755 --log`; the step summary's text is not in the log and was not read |
| closed whether GitHub evaluates the two expressions of the `durations` job as phase 2 reads them: the one ending the union step's line giving `--stale-fails` on a pull request into `main` and nothing on every other run, and `hashFiles('union/.test_durations')` matching the union file, whose name starts with a dot, so the upload runs after a red verdict and is skipped after a refusal; the cases read the workflow's text, PyYAML parsed it, and no `actionlint` or GitHub run evaluated either expression (`frame/questions.md` Q1) | answered by two runs, read by the settling session with `gh run view --log`: run 42564261755 (#1457, into `main`) ran the union step with `--stale-fails` and then its upload step for `union/.test_durations`; run 42595832895 (#1463, into `release/v0.37.0`) ran it without the flag. No run has yet been red or refused, so the upload after a red verdict and the skip after a refusal stand as the cases read them |

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

`.test_durations` keeps the entries of the eight cases phase 2 removed from
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`.
They are `test_the_durations_file_prices_the_suite` and the seven fixture
cases `frame/design.md` *Removes* row 4 names:
`test_exactly_the_share_unpriced_passes`,
`test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe`,
`test_an_empty_collection_is_refused`,
`test_an_entry_nobody_collects_is_not_counted`,
`test_dead_seconds_past_the_share_fail_and_at_the_share_pass`,
`test_both_sides_over_are_named_in_one_sentence` and
`test_an_empty_file_is_all_unpriced_and_nothing_gone`. Together they hold
0.029 s. The list is every `def test_` the work's diff under `tests/`
removes, each found once in the file. This work makes the rule that no
work item commits the file, so phase 2 left them. The next release refresh,
taken from a union that no longer holds those cases, drops the entries.

# Phase 1: 1793875976-the-suite-has-not-run-on-3-14

## What this phase found

**The frame holds for Scope 1 to 3, read against the tree at `18a89a82`.** G5 holds: the eight `include:` entries were all at 3.12, and `fail-fast` is `false`. G7 holds: `test_every_group_of_each_sharded_leg_runs_exactly_once` refuses a `split` on any entry outside macOS and Windows, and `test_the_windows_entries_store_and_the_other_entries_do_not` refuses a `store` on any entry outside Windows. G8 holds: the old case asserted `set(versions) == {rt.FLOOR_TEXT}`. Neither `hooks/lib/launch.py#FLOOR` nor the comment above `FLOOR_TEXT` in `.github/scripts/run_tests.py` says CI runs the suite at the floor. The mutations below show the frame's claim that the shape cases hold the new entry with no new case.

**The rewritten case reads a system and not its shards, and it says so in its docstring.** Scope 2 asks that every operating system hold at least one entry at the floor. A mutation shows the limit of that reading. With macOS group 2 moved to 3.14, macOS still holds two floor entries, so the case stays green, while a third of the suite would run on macOS at no floor. A reading per shard would need the floor entries of each system to cover every group. That is more than Scope 2 asks for. `plan.md` alternative F keeps 3.14 off macOS and Windows, so no planned change moves a shard. So I built Scope 2 as written. The docstring gains one sentence that names the limit, and `gaps.md` *Not done* records the per-shard reading with its grounds. Judged against `frame/design.md` Scope 2 and `skills/core/SKILL.md` *The rule a mechanism is kept against*, which keeps a check only for what its catch record justifies.

**One comment outside Scope 1's list changed, because the new entry made it wrong.** The comment above the `pytest` line in `test.yml` said "`split` is empty on ubuntu, so that leg runs the whole suite as before". ubuntu now has two entries, so the sentence now reads "so each ubuntu leg runs the whole suite as one job". Judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*: a change rewrites the text it amends in place.

**The timeout paragraph gains a row for the 3.14 leg.** The row says the leg takes ubuntu's base and its 15, and that no 3.14 job is measured yet. Phase 3 replaces "no 3.14 job is measured yet" with the run and minutes Scope 5 names.

**The Windows entries' `strategy.job-index` moves from 4 to 7 to 5 to 8, and nothing reads the number.** The upload step names each part `test-durations-${{ strategy.job-index }}`. The `durations` job downloads by `pattern: test-durations-*`, and `.github/scripts/durations_union.py` reads no index. `tests/github/test_durations_union.py` uses `test-durations-4` to `-7` only as fixture names. (read)

**Seen red: the rewritten case, against a copy of the workflow text.** A probe, `tests/behaviour/test_tmp_floor_red.py`, replaced `read_workflow` in the case's module with a function that returns `test.yml` with all four Windows entries moved to `"3.14"`. It then called the case. The case failed at the line `assert not missing`, with `CI runs the suite on ['windows-latest'] with no entry at the floor 3.12`. The probe ran once and was deleted before the commit. (executed)

**Mutations, at `315358a8`** (executed, `bin/seal mutate .github/workflows/test.yml`):

- `{ os: ubuntu-latest, python: "3.12", … }` moved to `"3.13"`, against `-k test_ci_runs_the_suite_at_the_floor_the_runner_holds`: red.
- macOS group 2 moved to `"3.14"`, same case: SURVIVED. This is the limit above.
- Each of the following was run alone against the four modules of the plan row, with `-x`:
  - The 3.14 entry given `split: "--splits 2 --group 1"`: red at `test_every_group_of_each_sharded_leg_runs_exactly_once`.
  - The entry given the Windows `store`: red at `test_the_windows_entries_store_and_the_other_entries_do_not`.
  - The entry's `timeout` dropped: red at `test_every_pytest_leg_has_a_timeout_and_the_job_reads_it`.
  - The entry's whole line deleted: SURVIVED. No case requires a 3.14 entry, as `plan.md` alternative M decided. Phase 3's dispatched run is what shows the leg runs.
- An earlier batch replaced the entry's text with nothing and left `          - ` on its line. That mutant went red on the parse refusal in `matrix_include_entries` and not on any check of the entry, so it is not counted above.

**The phase boundary run found one defect in the frame, which this phase cannot write.** It was one `bin/test` command over the plan row's four modules and every test module that names `test.yml`, `workflows/`, `CONTRIBUTING` or the rewritten module, or walks the tree (61 modules). The result was 3042 passed, 2 failed and 11 skipped (executed, before this record and `gaps.md` existed). `test_every_spec_directory_that_reached_the_ladder_has_an_overview` failed because `gaps.md` was not yet written, and this close writes it. `tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census` failed on `frame/design.md:18`, the real-identifiers census: G12 names a package index's domain in its URLs. That line came in with the framer's commit `18a89a82`. The crafter does not write `frame/design.md`, so the hand-back names it for the orchestrator.

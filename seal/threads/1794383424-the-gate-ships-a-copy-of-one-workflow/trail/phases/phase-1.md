# Phase 1: 1794383424-the-gate-ships-a-copy-of-one-workflow

## What this phase found

**The frame holds.** Every coordinate `frame/design.md` G4, G6, G7 and G10 gives was opened at `0dd6d89f3`, and each line stood where the frame placed it. S4's `git grep` listed the four files G5 names before the build. One line the frame does not list stated the section's facts, and the departures below follow from it and from the scope items.

**Departures from the frame, each judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*: a change removes, in the same commit, what stood on the old fact.**

- `broad_gate.py`'s module docstring said a preflight "prints no coverage line" (`:107` at `0dd6d89f3`). G4 does not list that clause. It names a line no run prints after this work, so the clause left under *Scope* item 2.
- `panel`'s docstring said `report_lines` "maps the four to ASCII", the four being `SEP`, `ARROW`, `TICK` and `DOT`. With `DOT` gone from that list, it says "the three". *Scope* item 2 named only the line that lists `DOT`.
- `Test_panel`'s case `test_accepts_the_item_the_gate_row_and_what_ci_also_asks` is now `test_accepts_the_item_and_the_gate_row`. *Scope* item 4 removed its `CI also` assertion, and the old name stated that assertion.
- `main`'s comment above the chain arm gave `PARTITION`'s cases as the reason a preflight keeps one list of arms. *Scope* item 2 removes that ground. The comment keeps the ground that remains: a second list of arms would be a second list to keep in step with the first.
- `.github/scripts/tracker_labels.py` ended the paragraph with "A step that performs the act costs neither." With the partition cost gone, one cost remains, so it now ends "A step that performs the act does not."
- In `tests/skills/test_broad_gate.py`, the module docstring, the comment above `HISTORICAL_ROWS` and `with_workflow`'s docstring cited the deleted file, the absent workflow and the arm that "mirrors" a step. Each now states what stands. *Scope* item 4 named only the module docstring.

**S3's case reads the labels off the run's printed report, not off an in-process `panel` call.** After the work `panel` takes no workflow, so an in-process call cannot be handed one and stays green against the base. The printed report is what a user reads, and the old gate put its `CI also` row there. The case is `Test_main::test_a_workflow_with_a_release_job_leaves_the_run_as_it_was`. It runs the gate over `with_workflow(sealable_repo(...))`, asserts the stdout labels equal `HISTORICAL_ROWS`, and asserts stderr holds neither `.github/workflows/hygiene.yml` (as `os.path.join` spells it), nor `` `release` ``, nor any `- name:` of `FIXTURE_WORKFLOW`. Judged against `frame/design.md` S3 and contract rule 15.

**Seen red (executed), against `0dd6d89f3`'s `broad_gate.py`, before any code changed.** As written, the case failed on stderr: `the gate names '.github/workflows/hygiene.yml' for a repository whose workflow it does not read`, the old coverage line quoted under it. With the stderr loop disabled for one run, it failed on the labels half: `('tree', 'base', 'suite', 'chain', 'CI also')` against `HISTORICAL_ROWS`. Each half is red on its own.

**No `seal mutate` run is owed.** The phase adds no behaviour: it removes units, a parameter and a row, and rewrites one case. `agents/crafter.md` asks for a run over each unit that adds behaviour, and none does. The rewritten case was seen red instead, as above.

**S4 (executed).** `git grep -n -w -e PARTITION -e ONLY_AT_MAIN -e coverage_line -e 'gate\.job_steps' -e steps_for -e left_out_clause -e base_is_main -e workflow_text -e RELEASE_JOB -- ':!seal/threads' ':!.test_durations'` prints nothing and exits 1 at `a94a5ac72`.

**The narrow run (executed, over the working tree before the phase commit):** the plan row's command gave 610 passed, 1 skipped and 2 failed. The two failures are `tests/test_conftest.py::Test_census_case::test_accepts_a_target_every_census_passes` and `::test_refuses_a_target_one_census_flags_naming_it`. Both are `failing on base too`: they fail the same way at `0dd6d89f3` in a scratch worktree (executed). #1498 fixed them on `release/v0.37.4` as `10e721f11`, which this branch does not hold.

**The phase-boundary run (executed)** was one `bin/test` command, over the phase commit as first made. `a94a5ac72` is that commit with one docstring line in `broad_gate.py` rewrapped. It covered `tests/text`, `tests/behaviour`, each test file the phase changed, and each test file that names a path the phase changed. Those are `tests/skills/test_seal_stamp.py`, `tests/github/test_rules.py`, `tests/github/test_tracker_labels.py`, `tests/github/test_release_seal.py`, `tests/lib/test_console.py`, `tests/lib/test_optin.py`, `tests/skills/test_agentic_pytest_record.py`, `tests/skills/test_chain_check.py`, `tests/skills/test_seal.py`, `tests/skills/test_session_cost.py` and `tests/test_censuses.py`. It gave 3717 passed, 9 skipped and 3 failed. Two failures are the census cases above. The third, `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`, wanted this work item's `gaps.md`, which this close writes. After the close, at the commit that adds this record, `tests/text` and `tests/behaviour` gave 1854 passed and 8 skipped, and `tests/skills/test_broad_gate.py`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` and `tests/github/test_publish_release_note.py` passed (executed).

**`tests/conftest.py` is read by every test file, and the set does not take the whole suite for it.** Its change is two docstrings. `skills/verify/SKILL.md` *The narrow command still has to be able to fail*, the row *A comment or docstring inside source*, says what can then fail is the import, and every case in the run imports it.

**`.test_durations` keeps the entries of the removed cases and the renamed one**, as `frame/design.md` G13 and *Out* decide.

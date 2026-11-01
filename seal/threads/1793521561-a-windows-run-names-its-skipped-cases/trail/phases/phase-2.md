# Phase 2: 1793521561-a-windows-run-names-its-skipped-cases

## What this phase found

**The run answers `frame/questions.md` Q1: the three cases of #1221 passed on the Windows legs, and no case of `tests/skills/test_unverified_check.py` skipped there.** So `tests/conftest.py#symlink_or_skip`'s docstring holds for the `windows-latest` runner: the runner can make links. The run also shows that the flags work on the runners. Every leg of the `pytest` job that skipped a case printed one `SKIPPED <node id> - Skipped: <reason>` line for it; the `arms-grammar` job, whose line carries no flag, printed none for its two skips. The run cannot show the other half of S1, that a red leg keeps its `FAILED` lines, because no case failed on any leg. That half stays open in `gaps.md`. Last, the run names three other link cases that skip on Windows through a platform check, which the same docstring argues against. They are out of this work's scope and are a leftover for the orchestrator (below). Q2's default does not apply, because none of the cases Q1 names skipped.

**The frame holds for this phase.** `frame/design.md` *Scope* item 3 and the plan's Verified by cell for phase 2 name what was read, and each coordinate was opened as named. The spawn handed over the run's facts, and each was opened before anything was built on it (executed). `gh run view 41290162769 --json headSha,conclusion,event,headBranch,status,jobs` reports event `workflow_dispatch`, branch `test/1221-a-windows-run-names-its-skipped-cases`, head commit `585234f6bdcec52cc28024c1543d904eeca302be`, status `completed` and conclusion `success`. The four Windows job ids are the ones the spawn named, each with the group the spawn gave it. `git ls-remote origin` shows the branch at the same commit, which was this worktree's HEAD before this phase. `git diff --stat 0773118a 585234f6` lists only the four record files under this work item's directory, so the run tested phase 1's tree.

**The four Windows shards (executed: `gh run view --job <id> --log` for each).**

| Shard | Job id | Conclusion | Last line of pytest's output | `SKIPPED` lines |
|---|---|---|---|---|
| `--group 1` | 124799569298 | success | `3082 passed, 14 skipped in 136.54s (0:02:16)` | 14 |
| `--group 2` | 124799569427 | success | `594 passed, 7 skipped in 104.57s (0:01:44)` | 7 |
| `--group 3` | 124799569246 | success | `1217 passed, 14 skipped in 74.96s (0:01:14)` | 14 |
| `--group 4` | 124799569215 | success | `1321 passed in 108.59s (0:01:48)` | 0 |

Each log's test step reads `Run pytest tests/ -q -n auto --durations=50 -rfEs --no-fold-skipped --splits 4 --group <N> --store-durations --clean-durations`. Each install step ends with `Successfully installed ... pytest-9.2.0 pytest-split-0.11.0 pytest-xdist-3.8.0`. Those are the three versions the framer's probe ran (`frame/design.md` *Grounding*). No log holds a `FAILED` or `ERROR` line. In each shard the count of `SKIPPED` lines equals the skipped count on the last line, and each `SKIPPED` line names a node id with `::`. So no skip was folded under a helper's line. The counts 14, 7, 14 and 0 are the counts the framer measured on run 41207847854.

**The three cases of #1221 passed (S3, S4).** Under `-q`, pytest prints no line for a case that passed. So the evidence for each case is three facts, read together:

- No `SKIPPED` line and no `FAILED` line in the four Windows logs names `tests/skills/test_settle.py::Test_misplaced` or `test_a_work_item_whose_rounds_cannot_be_listed` (executed: `grep -c` over each log, 0 in each).
- All four Windows shards concluded `success` (the table above).
- Each id stands in the run's `test-durations` artifact (executed: `gh run download 41290162769 -n test-durations`, then a `python3 -I` read of the file). The union holds 6,249 ids. That is the four shards' passed and skipped counts added together (3,096, 601, 1,231 and 1,321), so it is the union of the Windows parts. The durations recorded for the three cases are below.

| Case | Read as | Duration in the union |
|---|---|---|
| `tests/skills/test_settle.py::Test_misplaced::test_accepts_a_file_or_a_link_to_one_at_another_path` | passed | 0.0123 s |
| `tests/skills/test_settle.py::Test_misplaced::test_refuses_a_directory_a_link_to_nothing_and_another_spelling` | passed | 0.0178 s |
| `tests/skills/test_settle.py::Test_main::test_a_work_item_whose_rounds_cannot_be_listed_is_not_counted_as_none[link]` | passed | 0.9440 s |

An id in the union alone does not prove a pass, because the union also records a case that skipped. The three cases of `tests/skills/test_agentic_pytest_record.py` that skipped stand in it with durations under 0.001 s. The proof is the id in the union of a green shard together with no `SKIPPED` line naming it.

**No case of `tests/skills/test_unverified_check.py` skipped on Windows.** The union holds 390 ids of the module, and no `SKIPPED` line in the four logs names it (executed, the same `grep` and the same read). Its link cases call `symlink_or_skip`, and the three cases of #1221 show that the call succeeds on the runner. This answers the open rows at `seal/threads/1793457436-row-deletion-check-and-a-symlink/gaps.md:7` and `seal/threads/1793504229-a-linked-memo-named-as-the-argument/gaps.md:7`: the module's cases ran on the Windows legs and none skipped. Those rows are not edited here. Each belongs to its own work item, and the settle closes them with this record as its source (`frame/design.md` *Scope*, *Out*).

**Every other `SKIPPED` line the four shards print.** The 35 lines, by module, with pytest's reason as printed:

Shard 1 (14):
- `tests/behaviour/test_first_setup_asks_once.py::test_the_switch_block_lands_the_root_at_the_tree_root_from_a_subdirectory[README.ko.md]` and `[README.md]`: "bash: exited 1 -- not a shell here -- the switch block is a bash block"
- `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py::test_a_copy_without_the_runner_beside_it_says_so`: "the POSIX wrapper needs a POSIX shell"
- `tests/behaviour/test_release_hygiene.py::test_the_check_lines_rules_did_not_read_reach_the_pull_request`: "the step runs under bash on Linux"
- `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py::test_every_script_a_shipped_document_names_has_a_subcommand_or_is_classified`, eight parameters (`skills/settle/scripts/fold_check.py` and seven under `skills/verify/scripts/`: `arm_check.py`, `coordinates.py`, `core_check.py`, `deferral_check.py`, `payload_meter.py`, `test_layout.py`, `unverified_check.py`): "no shipped document names it, so nobody goes looking". The ubuntu leg and macOS group 1 skip the same eight with the same reason, so the skip is not about Windows.
- `tests/github/test_run_tests.py::Test_main::test_an_unwritable_venv_leaves_the_refusal_a_sentence`: "chmod 555 does not stop a write as root, and on Windows chmod sets only the read-only flag, which does not stop a file being created inside the directory"
- `tests/hooks/test_dispatch.py::Test_run_gate::test_accepts_an_edit_and_hands_the_gate_its_file_not_the_group_name`: "the probe puts a shell stub named `ruff` on PATH; Windows resolves a bare name through CreateProcess, which does not find a .cmd"

Shard 2 (7):
- `tests/skills/test_arm_check.py::Test_arms::test_a_module_holding_a_t_string_is_read_rather_than_refused` and `::test_an_interpolation_is_counted_exactly_as_an_f_string_field`: "t-strings parse from Python 3.14 on"
- `tests/skills/test_arm_check.py::Test_main::test_a_command_that_does_not_pass_against_the_module_refuses_the_run[a run killed by a signal]`: "no signals on Windows"
- `tests/skills/test_arm_check.py::Test_main::test_a_refused_run_leaves_the_module_as_it_was_before_the_command[locks it]`: "needs a POSIX mode root obeys"
- `tests/skills/test_agentic_pytest_record.py::Test_module::test_a_rootdir_named_through_a_symlink_records_the_file_pytest_ran`, `::test_an_argument_named_through_a_symlink_records_the_file_pytest_ran` and `::test_a_symlinked_directory_under_the_rootdir_is_recorded_by_its_own_name`: "a symlink needs privileges on Windows"

Shard 3 (14):
- `tests/skills/test_mutation_check.py`, seven cases: `Test_main::test_a_run_past_the_bound_is_timed_out_and_leaves_nothing_it_started[mutated]` and `[baseline]`, `Test_main::test_a_process_outside_the_group_does_not_hold_the_verdict_back`, `Test_main::test_an_interrupt_ends_the_run_it_started_and_restores_the_file[mutated]` and `[baseline]`, `Test_module::test_a_group_that_ended_on_its_own_at_the_bound_is_not_an_error` and `Test_main::test_cases_that_exit_but_leave_a_child_on_the_output_read_red_at_once`: "the process-group bound is POSIX's"
- `tests/skills/test_mutation_check.py::Test_module::test_the_command_a_session_types_reaches_the_script`: "the POSIX wrapper; its .cmd twin is read, not run"
- `tests/skills/test_deferral_check.py::Test_module::test_the_command_is_present_and_runs_the_script` and `tests/skills/test_pact_check.py::Test_module::test_the_wrapper_runs_the_script_from_any_directory`: "the POSIX command; bin/seal.cmd is its Windows twin" and "the POSIX wrapper; bin/seal.cmd is its Windows twin"
- `tests/skills/test_seal.py::Test_blocked_path::test_refuses_a_directory_name_a_file_holds[a pipe here]` and `tests/skills/test_seal.py::Test_import_::test_refuses_a_name_one_side_holds_as_a_file[a pipe here]`: "named pipes are not available here (no os.mkfifo)"
- `tests/skills/test_seal.py::Test_import_::test_refuses_a_directory_it_cannot_write_into_with_a_line_of_its_own`: "this filesystem ignores the directory's write bit"
- `tests/skills/test_seal.py::Test_switch::test_refuses_a_rename_the_filesystem_turns_down_and_names_the_mv`: "the working tree is writable despite chmod"

Each line in the log carries its node id and its reason whole. The longest is 269 characters after the runner's timestamp. Each reason was compared with the end of its line in the log (executed: `awk` over the `SKIPPED` lines of shards 1 to 3), and the two longest with their `skipif` in the source (read, `tests/github/test_run_tests.py:465-467` and `tests/hooks/test_dispatch.py:307-308`).

**Three link cases skip on Windows through a platform check, although the runner can make links.** The three cases of `tests/skills/test_agentic_pytest_record.py` in shard 2 skip through `@pytest.mark.skipif(os.name == "nt", reason="a symlink needs privileges on Windows")` (read, `tests/skills/test_agentic_pytest_record.py:868`, `:890`, `:916`). `symlink_or_skip`'s docstring names that form as wrong where the privilege is held: it "drops the coverage where the privilege IS held". The three cases of #1221 show the privilege is held on this runner. So these three cases go unproved on Windows for a reason the same run shows is not true there. The list of link cases that skipped on the Windows legs is whole for this run, because it was built from every `SKIPPED` line the four shards printed, and these three are the only lines whose reason is about links. A link case on another runner image, or in a later run, is outside that list. Repairing the three is outside this work: `frame/design.md` *Scope*, *Out* names "every case under `tests/`". Judged against that clause, the record names them and the orchestrator decides their home, an issue or a row of `seal/follow-up.md`. A draft, if the home is an issue:

> Title: `test: three link cases of test_agentic_pytest_record.py skip on Windows by platform, although the runner can make links`
>
> `tests/skills/test_agentic_pytest_record.py` skips three cases on Windows through `skipif(os.name == "nt", reason="a symlink needs privileges on Windows")`: `Test_module::test_a_rootdir_named_through_a_symlink_records_the_file_pytest_ran`, `Test_module::test_an_argument_named_through_a_symlink_records_the_file_pytest_ran` and `Test_module::test_a_symlinked_directory_under_the_rootdir_is_recorded_by_its_own_name`. Run 41290162769 (#1221) shows the `windows-latest` runner can make links: the link cases of `tests/skills/test_settle.py` and `tests/skills/test_unverified_check.py` passed there through `tests/conftest.py#symlink_or_skip`. That helper's docstring names the platform skip as the form that drops coverage where the privilege is held. The three cases make their links with `Path.symlink_to`. Moving them onto `symlink_or_skip` would let them run on the runner and still skip on a machine without the privilege. Done when the three cases run on the Windows legs, or skip there through `symlink_or_skip` with its reason.

The draft's sentence on `Path.symlink_to` was read at `:882`, `:904` and `:929`. Whether the three cases pass on Windows once they make links there is not known. No run has made them try.

**The ubuntu and macOS legs print the same kind of line (executed: the same `gh run view --job <id> --log`, beyond the plan's Verified by cell, because S1 says "any `pytest` leg").** The ubuntu leg (124799569338) ends `6238 passed, 11 skipped` with 11 `SKIPPED` lines. macOS group 1 (124799569290) ends `3596 passed, 11 skipped` with 11. macOS groups 2 (124799569198) and 3 (124799569264) end `811 passed` and `1831 passed`, with none. Each leg's test step shows `-rfEs --no-fold-skipped` on its line.

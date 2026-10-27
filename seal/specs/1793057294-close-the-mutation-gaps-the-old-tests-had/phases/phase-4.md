# 1793057294-close-the-mutation-gaps-the-old-tests-had — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | c2951650 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Phase 4 only: the rows of #1017 for `skills/verify/scripts/session_cost.py`,
`skills/verify/scripts/broad_gate.py`, `skills/verify/scripts/mutation_check.py`,
and the two `skills/verify/scripts/pytest_record/specseal_pytest_record.py`
survivors. Follow the method and table shape of phases 1 to 3: rebuild each
row at the head with `bin/mutation-check` and `-x`, run a survivor again
against the other test files that load the module, write a case only where it
survives all of them, and see each new case red alone under its mutant.
#945 adds a class `Test_largest_context` and a `context` column to
`session_cost.py`'s `report_segments` on another branch, and edits one
`Test_main` case's row patterns. So this phase's cases in
`tests/test_session_cost.py` stand only in classes of the functions they test,
and the two branches meet only textually. One commit per module that needs
one, then this record and phase 4's Status in `plan.md`. Build on
`questions.md`'s defaults Q1 to Q5. Fake every decision that reads the
platform.

## The outcomes

20 rows, rebuilt as 21 mutants. All 20 rows are killed by a new case. None was
already closed, none is equivalent, none left the tree, and none is a finding.

| Module | Commit | Rows | Mutants | Killed by a new case | Already closed | Equivalent |
|---|---|---|---|---|---|---|
| `skills/verify/scripts/session_cost.py` | 083181b1 | 13 | 13 | 13 | 0 | 0 |
| `skills/verify/scripts/broad_gate.py` | f46904eb | 4 | 4 | 4 | 0 | 0 |
| `skills/verify/scripts/mutation_check.py` | 4f1314c9 | 1 | 2 | 1 | 0 | 0 |
| `skills/verify/scripts/pytest_record/specseal_pytest_record.py` | c2951650 | 2 | 2 | 2 | 0 | 0 |

## How the tables read

The tables read as phase 1's do. Each pair is written as the zsh command line
passed it to `bin/mutation-check --replace`. A `$'...'` string is ANSI-C
quoted, so `\n` in it is a newline.

The before column is the module's batch with `-x -p no:xdist` in `--tests`,
first against the module's own test file, then, for each survivor, against
every other test file that names the module. The other files are listed above
each table. The session_cost and broad_gate batches ran at 8777dffd. The
mutation_check and recorder batches ran after this phase's new cases were
written into their files, with those cases deselected by name, so each ran the
cases that stood at 8777dffd. The recorder's other-file batch deselected
this phase's four `tests/test_broad_gate.py` cases the same way. The after
column is the same batch against the module's own file at the module's
commit. Every batch passed its baseline.

A new case was seen red alone on its mutant with
`bin/mutation-check <module> --replace OLD NEW --tests "bin/test tests/test_<stem>.py -q -x -p no:xdist -k <case>"`,
or with the case's node id in single quotes for a parametrized one. Each of
those runs printed `red: the cases failed against the mutation (exit 1)` after
a passing baseline. Each failure was the case's own assertion, except s60's,
whose case fails where it parses stdout as JSON and the mutant printed the page.

## `skills/verify/scripts/session_cost.py`

Records: the issue body's s15 to s60, `phases/phase-6.md:1154` to `:1170` at
`79f9c3fd`. Before: `tests/test_session_cost.py`, then
`tests/test_a_derived_number_reaching_an_int_carries_a_guard.py tests/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/test_a_reference_root_is_read_and_never_taken.py tests/test_a_segment_feeds_the_flow_log.py tests/test_one_word_one_meaning.py tests/test_payload_meter.py tests/test_run_tests.py tests/test_session_cost_post.py tests/test_the_handoff_before_round_one.py`,
196 passed and 8 skipped at the baseline.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| s15: `count` returns a non-finite float | `'return value if finite else 0'` `'return value'` | SURVIVED, every file | red, `Test_count::test_refuses_a_non_finite_float_as_zero` | killed by a new case |
| s18: `load` keeps a row with no stamp | `'if not stamp or not isinstance(content, list):'` `'if not isinstance(content, list):'` | SURVIVED, every file | red, `Test_load::test_refuses_a_row_with_no_timestamp_as_a_turn` | killed by a new case |
| s20: `analyse` counts a model gap of 900 s or more | `'if 0 <= gap < 900:'` `'if 0 <= gap:'` | SURVIVED, every file | red, `Test_analyse::test_refuses_a_model_gap_of_fifteen_minutes_or_more` | killed by a new case |
| s21: the repeats keep `other` | `'if family(call["ran"]) not in ("test", "lint/type", "build"):'` `'if family(call["ran"]) not in ("test", "lint/type", "build", "other"):'` | SURVIVED, every file | red, `Test_analyse::test_refuses_an_unnamed_command_run_twice_as_a_repeat` | killed by a new case |
| s24: `token_thirds` computes from two inputs | `'if len(inputs) < 3:'` `'if len(inputs) < 2:'` | SURVIVED, every file | red, `Test_token_thirds::test_refuses_two_inputs_as_too_few_for_thirds` | killed by a new case |
| s25: `subagent_transcripts` walks the session's directory and not its `subagents/` | `'root = os.path.join(os.path.dirname(os.path.abspath(path)), session, "subagents")'` `'root = os.path.join(os.path.dirname(os.path.abspath(path)), session)'` | SURVIVED, every file | red, `Test_subagent_transcripts::test_refuses_a_transcript_beside_subagents_rather_than_in_it` | killed by a new case |
| s26: `resume_cuts` cuts at a row not marked `isMeta` | `'if not row.get("isMeta"):'` `'if False:'` | SURVIVED, every file | red, `Test_resume_cuts::test_refuses_the_coordinators_words_on_a_row_the_harness_did_not_mark` | killed by a new case |
| s38: `report`'s `nothing obvious` line ignores the repeat time | `'if same <= 0 and round(data["tools_per_turn"], 2) >= 1.2:'` `'if round(data["tools_per_turn"], 2) >= 1.2:'` | SURVIVED, every file | red, `Test_report::test_refuses_nothing_obvious_beside_a_repeat` | killed by a new case |
| s42: `report_breaches` prints nothing where segments are unnamed and no agent spawned | `'if not calls and not unnamed:'` `'if not calls:'` | SURVIVED, every file | red, `Test_report_breaches::test_refuses_to_stay_silent_where_a_segment_is_unnamed_and_nothing_spawned` | killed by a new case |
| s46: `report_segments` drops the unnamed segments' paragraph | `'if segments["unnamed"]:'` `'if False:'` | SURVIVED, every file | red, `Test_report_segments::test_refuses_to_print_an_unnamed_segment_without_saying_why_it_has_no_name` | killed by a new case |
| s47: `newest` answers None where the directory exists | `$'    if not os.path.isdir(root):\n        return None'` `$'    if os.path.isdir(root):\n        return None'` | SURVIVED, every file | red, `Test_newest::test_accepts_the_latest_transcript_under_a_directorys_project` | killed by a new case |
| s57: `emit` replaces the path as given and not its absolute spelling | `'for form in (os.path.abspath(str(path)), str(path)):'` `'for form in (str(path),):'` | SURVIVED, every file | red, `Test_emit::test_refuses_to_post_the_absolute_spelling_of_a_path_given_relative` | killed by a new case |
| s60: `main` prints the segment report under `--segments --json` | `'if args.segments and not args.json:'` `'if args.segments:'` | SURVIVED, every file | red, `Test_main::test_refuses_the_printed_segment_report_under_json` | killed by a new case |

## `skills/verify/scripts/broad_gate.py`

Records: the issue body's b22, b29, b50 and b70, `phases/phase-6.md:1211` to
`:1218` at `79f9c3fd`. Before: `tests/test_broad_gate.py`, then
`tests/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/test_a_moved_rule_leaves_its_definition.py tests/test_a_parallel_agent_names_its_scratch_after_the_work_item.py tests/test_a_reference_root_is_read_and_never_taken.py tests/test_a_release_publishes_its_note.py tests/test_a_segment_feeds_the_flow_log.py tests/test_a_signer_declares_its_pact.py tests/test_broad_gate_rule.py tests/test_censuses.py tests/test_chain_check.py tests/test_config.py tests/test_conftest.py tests/test_docs_line_wrap.py tests/test_evals_layout.py tests/test_every_orchestrator_act_names_its_delivery.py tests/test_first_setup_asks_once.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_one_word_one_meaning.py tests/test_release_hygiene.py tests/test_release_seal.py tests/test_seal_stamp.py tests/test_sealer_stamp.py tests/test_sealer_stamp_queue.py tests/test_specseal_pytest_record.py tests/test_the_agent_contract_holds_the_universal_rules.py tests/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py tests/test_the_direct_answer_owes_the_sealers_record.py tests/test_the_gate_asks_the_range_ci_will_ask.py tests/test_the_gate_hands_cmd_a_path_it_can_run.py tests/test_the_gate_names_every_step_ci_runs.py tests/test_the_rules_have_one_owner.py tests/test_the_seal_is_taken_once_by_the_sealer.py tests/test_the_sealer_guarantees.py tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/test_the_verifying_round_is_bounded_not_cheapest.py`,
with `--timeout 1500`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| b22: `refused_broad_row` answers where the walk read the row | `'if not refusals or any(item == ROW for _index, item, _value in rows):'` `'if not refusals:'` | SURVIVED, every file | red, `Test_refused_broad_row::test_refuses_a_row_the_walk_read_above_the_line_it_refused` | killed by a new case |
| b29: `missing_row` asks whether any fence is left open, not one above the row | `'if fence_left_open(home, at)'` `'if fence_left_open(home)'` | SURVIVED, every file | red, `Test_missing_row::test_refuses_to_blame_a_fence_left_open_below_the_fenced_row` | killed by a new case |
| b50: the scan keeps command position after `<` or `>` | `'at_command, in_name = False, False'` `'in_name = False'` | SURVIVED, every file | red, `Test_command_names_backslashed::test_refuses_to_turn_a_redirections_target_at_the_start_of_a_command` | killed by a new case |
| b70: `compare_at_base` hands `base_word` exit 0 whatever the base's run exited | `'return {f: base_word(record, ran.code, f) for f in files}'` `'return {f: base_word(record, 0, f) for f in files}'` | SURVIVED, every file | red, `Test_compare_at_base::test_refuses_new_for_a_file_a_red_base_never_collected` | killed by a new case |

## `skills/verify/scripts/mutation_check.py`

Records: the round 3 comment's mc21, `phases/phase-6.md:1738` at `fc4f81ae`.
Before: `tests/test_mutation_check.py`, then
`tests/test_a_moved_rule_leaves_its_definition.py tests/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py tests/test_a_probe_does_not_outlive_its_round.py tests/test_a_reference_root_is_read_and_never_taken.py tests/test_arm_check.py tests/test_censuses.py tests/test_config.py tests/test_conftest.py tests/test_release_report.py tests/test_test_layout.py tests/test_the_handoff_before_round_one.py tests/test_worktree_guard.py`,
with `--timeout 1200`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| mc21: a bound of 0 is read as 0 seconds, at the batch call | `'                    timeout=args.timeout or None,'` `'                    timeout=args.timeout,'` | SURVIVED, every file | red, `Test_main::test_accepts_a_bound_of_zero_as_no_bound[a-batch]` | killed by a new case |
| mc21: the same, at the one-pair call | `$'            timeout=args.timeout or None,\n        )\n'` `$'            timeout=args.timeout,\n        )\n'` | SURVIVED, every file | red, `Test_main::test_accepts_a_bound_of_zero_as_no_bound[one-pair]` | killed by a new case |

## `skills/verify/scripts/pytest_record/specseal_pytest_record.py`

Records: the issue body's *Two more, recorded only in a review round*,
`rounds/round-2.md:156` and `:195` at `79f9c3fd`. Before:
`tests/test_specseal_pytest_record.py`, then
`tests/test_a_release_publishes_its_note.py tests/test_broad_gate.py tests/test_the_seal_is_taken_once_by_the_sealer.py`,
the three other files that name the recorder, and with them every other file
of the broad_gate table above, since a file that runs the gate loads the
recorder into the run it measures. `tests/test_the_gate_asks_the_range_ci_will_ask.py`,
the file #942's round 2 ran the two against at 482fed97, is among them. The
batch ran with `--timeout 1500`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| the invocation directory read as the working directory | `'    return str(params.dir)'` `'    return os.getcwd()'` | SURVIVED, every file | red, `Test__invocation_dir::test_refuses_the_working_directory_where_pytest_names_the_invocation` | killed by a new case |
| `wasxfail` never written | `'if hasattr(report, "wasxfail"):'` `'if False:'` | SURVIVED, every file | red, `Test_Recorder::test_accepts_an_xfail_reason_on_its_tests_line` | killed by a new case |

## What this phase found

**mc21 is one row and two mutants.** `main` passes `args.timeout or None` at
two calls, one for a batch and one for a single pair, and #942's record does
not say which it mutated (Q1). Both were run. Both survived every file, and
one case parametrized over the two modes kills each. Its two parameters were
each seen red alone, by node id, on their own call's mutant.

**Nothing in the tree reads the two fields the recorder rows are about.**
`git grep` over the tree's Python and Markdown finds `invocation_dir` and
`wasxfail` written by the recorder, named by its docstring and by two specs of
earlier work items, and read by no code (`executed`). The broad gate's
`read_record` takes neither. The cases pin what the module's docstring says a
record line carries. Under `CLAUDE.md` *The rule a mechanism is kept against*
a field no reader takes may be one to remove rather than pin. Removing a
field changes what the record says, which is outside this work's scope
(`spec.md` *Out*), so phase 7 can carry it into `overview.md` as a divergence
for the repository owner to decide.

**`Test_Recorder` and `Test__invocation_dir` were chosen over the file's own
grouping.** The file's docstring puts runs of pytest with the plugin loaded in
`Test_module` and direct drives of the class in `Test_Recorder`. `spec.md`
*In* item 2 puts a case in the class of the function the mutant changes. The
`wasxfail` decision is in `Recorder.pytest_runtest_logreport`, so its case
drives that method directly with a report built in the case. The invocation
decision is in the private `_invocation_dir`, which had no class, so the phase
added `Test__invocation_dir` with an accepts case and a refuses case, as
`bin/test-layout --check` asks. A small module-level `_loaded_recorder`
serves both classes. The three direct-drive cases already in `Test_Recorder`
load the recorder inline and are unchanged.

**`bin/test-layout --pairs` names the two `Test__invocation_dir` cases as one
pair, and they stay two.** Both call `_invocation_dir(Config())`, and the
normalisation cannot see that each `Config` is a class of its own case: one has
no `invocation_params`, and the other names a directory the working directory
was moved away from. Each holds a different branch of the function, so
neither covers the other, which is how #942's group 31 left `Test_Recorder`'s
own pair. `--pairs` is a report and exits 0. The other 21 pairs it prints over
the four files are between cases this phase did not touch.

**The new session_cost classes stand between `Test_post` and `Test_family`.**
The file's existing classes run `Test_main`, `Test_emit`, `Test_post`,
`Test_family`, which is the module's function order read from its end. The ten
new classes keep that order: `Test_newest`, `Test_report_segments`,
`Test_report_breaches`, `Test_report`, `Test_resume_cuts`,
`Test_subagent_transcripts`, `Test_token_thirds`, `Test_analyse`, `Test_load`,
`Test_count`. #945 inserts `Test_largest_context` after `Test_family` and edits
a `Test_main` case near line 3631 (read, `git diff` in that worktree, which
this phase did not write to). This phase's two other cases stand at the ends of
`Test_main` and `Test_emit`, so the two branches change no common lines, and
neither adds a class name the other adds.

**Each session_cost class got both kinds of case, though each mutant needed
one.** `bin/test-layout --check` asks every function class for an accepts case
and a refuses case. Each added accepts case reads an input its function's
existing cases do not: a model gap of 899 seconds, a nested segment under
`subagents/`, a batched run with no repeat, a finite count read back. For s47
the killing case is the accepts one, because the mutant answers None for a
directory that has a project.

**No case reads the platform without a fake.** `Test_newest` moves the
projects root under the case, so no home directory is read, and it builds the
project's slug with the module's own rule from `os.path.abspath`. The s57 case
builds its relative path with `os.path.join`. On Windows the mutant then still
leaves the absolute spelling, whose separators the relative one does not
match. The b50 case answers the directory question with a predicate, as the
class's other cases do. The mc21 case runs the class's stand-in script under a
bound of 0, which `Popen.wait` reads the same way on every platform. The
`_invocation_dir` cases build their configs in the case, and the `wasxfail`
case builds its report there. The b70 case runs git and pytest in a scratch
repository, as its class's other cases do.

**Run for the phase** (`executed`, at c2951650):
`bin/test tests/test_session_cost.py tests/test_broad_gate.py tests/test_mutation_check.py tests/test_specseal_pytest_record.py -q`
exited 0, 657 passed and 1 skipped. `bin/test-layout --check` over the four
files reads 4 files with 0 refused, and `--pairs` prints 22 pairs, the one
named above among them. `uvx ruff check` and `uvx ruff format --check` over
the four files exit 0. `git diff 8777dffd c2951650 -- tests` removes no line
holding `def test_`.

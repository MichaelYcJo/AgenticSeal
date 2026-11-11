# Phase 8: 1794396808-test-files-declare-no-target

## What this phase found

**The frame holds for this phase.** The phase started at `32dc787ee`.
The paragraph design *Scope* item 3 names opened "A case stands in the
file of what it holds" at `CONTRIBUTING.md:263`. The sentence that made a
case its module's said "one shipped module", and the T3 sentence said
"several shipped modules". The two `check:` lines of the section stood at
`:252` and `:261`, above the paragraph. The threshold sentence of item 11
stood at `:297-302` (all read). `git grep` on "one shipped module",
"several shipped modules" and "inside one of" over `tests`, `skills`,
`lib`, `.github` and `docs` found no case that reads either sentence
(executed).

**Item 3, the kinds paragraph** (`ff7d138c9`). The sentence that makes a
case its module's now says "one module". A new sentence says the module
is a shipped one or a module under `tests/` that is not a test file. The
T3 clause now reads "several modules, shipped or under `tests/`". Design
*The kinds* also says two things the item does not name: a case whose
subject is the source of such a module is M for it, and a case that uses
one only to read another file has that file as its subject. Without
them, the paragraph would make every case that reads a workflow through
`tests/workflows.py` M for that module. Phase 7 filed the readers-hide
import case by the first, so the paragraph states both, in two sentences
after the module sentence. "It goes in the class" became "A case that
stands in a module's file goes in the class", because three sentences
now stand between it and the case it named.

**Item 11, the threshold sentence** (`ff7d138c9`). The threshold now
counts a pair "inside one of the module's classes whose docstring states
no input its two cases differ by". The next sentence gives the ground
item 11 states: such a pair is two cases a reader has judged distinct.
This closes phase 1's paragraph under `gaps.md` *Not done*.

**Item 11, the pairs that stood before the build** (`d215adfe9`,
`77664dc10`). `bin/seal layout --pairs` gave `141 files read, 43 pairs`
at `32dc787ee` (executed). The pairs were set against phase 1's output
at the base, by class and case names (executed: `diff` of the two
sorted lists, the 66 pairs of `tests/github/test_run_tests.py` left out).
40 pairs stood at the base and at `32dc787ee`, in 15 classes, and none
of those classes had a docstring stating an input. Three pairs are new
since the base, and a phase wrote each one's reason:
`tests/skills/test_test_layout.py::Test_main` (phase 1),
`tests/lib/test_tables.py::Test_gfm_table` (phase 3) and
`tests/test_commonmark_oracle.py::Test_module` (phase 7). One pair of the
base is gone: `tests/behaviour/test_the_sealer_guarantees.py::TestDefinition`,
whose step 4 case phase 7's ruling cut, so its body no longer equals its
neighbour's.

Each of the 40 pairs' two cases was read whole, with the helper or
fixture that builds its world: `_refused_first_route`, `PagedTracker`,
`Tracker`, `_gh`, `waiting`, `two_axis_text` and `with_row`. Each class
now opens with a docstring stating the input its cases differ by.
`tests/skills/test_payload_meter.py::Test_imports_of` already had a
docstring, and the sentence went at its end. The classes are:

| Class | Pairs | The input the docstring names |
|---|---|---|
| `tests/github/test_close_issues_on_release.py::Test_comments_on` | 1 | what the monkeypatched `_issue_api` answers |
| `tests/github/test_close_issues_on_release.py::Test_close_issue` | 1 | the comment counts `_refused_first_route` reads |
| `tests/github/test_close_issues_on_release.py::Test_module` | 1 | the source given to `argv_words` |
| `tests/github/test_label_merged_on_release_branch.py::Test_existing_labels` | 1 | the labels the tracker holds |
| `tests/github/test_plugin_directory_check.py::Test_main` | 1 | the outcomes the parameters give `fetch` |
| `tests/github/test_roll_flow_measurement_issue.py::Test_find_baseline_issue` | 1 | what `try_run` answers |
| `tests/github/test_rules.py::Test_main` | 1 | the document the `tree` fixture writes |
| `tests/github/test_tracker_labels.py::Test_main` | 3 | the tracker's labels and `DRY_RUN` |
| `tests/lib/test_routing.py::Test_parse` | 4 | the declaration a case holds the two-axis one against, or the Implementation answer it writes |
| `tests/skills/test_agentic_pytest_record.py::Test_Recorder` | 1 | the reports sent to `path_of` |
| `tests/skills/test_payload_meter.py::Test_imports_of` | 4 | the text written |
| `tests/skills/test_seal.py::Test_pinned` | 1 | the text given to `pinned` |
| `tests/skills/test_seal_stamp.py::Test_main` | 1 | a waiting stamp, or a `drawn_at_stop` that raises |
| `tests/skills/test_session_cost.py::Test_main` | 3 | the fixture read; for one pair, nothing |
| `tests/skills/test_session_cost.py::Test_post` | 15 | what `_gh` answers |

**One pair differs by no input.** In
`tests/skills/test_session_cost.py::Test_main`,
`test_the_reading_names_the_release_it_is_comparable_from` and
`test_the_reading_says_its_family_rows_moved_at_642` run `segment_report`
over the same fixture, `run_with_segments`. Each holds a different note
of the report it prints. They hold two facts, so frame/questions.md Q5's
"a pair whose two cases hold one fact" does not fit them. Design *Scope*
item 11 presumes an input differs, and here none does. The class
docstring says the two read one world and differ by the note each holds.
Under the threshold sentence `ff7d138c9` wrote, this pair still counts,
since its class states no input for it. That is the threshold's purpose:
two cases on one input are the ones a rewrite would merge. The pair is
kept, and no case was rewritten (`frame/plan.md` A10).

`tests/lib/test_routing.py::Test_parse` takes two sentences, one for
each way its pairs arise. Three pairs share the call
`parse(two_axis_text())`, and one pair has equal bodies. Item 11 asks
for one sentence. One sentence holding both kinds came to a chain of
clauses, so the docstring has two.

`77664dc10` corrects the docstring `d215adfe9` gave
`Test_find_baseline_issue`. Reading the range against HEAD showed that
it named three of the first case's four answers and left out the one
that is not JSON.

**S8** (executed at `77664dc10`). A script under this phase's scratch
directory read each class that `bin/seal layout --pairs` names. It
found a docstring in all 18 classes that hold the 43 pairs. Whether
each sentence states the input is a reading, and the proofer reads it.
The pair list is the same at `32dc787ee` and at `77664dc10` (executed:
`diff`), because a docstring is not part of what the reader compares.

**Item 12, the counts at this phase's commit** (executed at
`77664dc10`):

| Count | At `b9ca37404` (design *The counts*) | At `77664dc10` |
|---|---|---|
| last line of `bin/seal layout --check` | `139 files read, 0 refused, 86 declare no TARGET` | `141 files read, 0 refused, 67 declare no TARGET` |
| last line of `bin/seal layout --pairs` | `139 files read, 107 pairs` | `141 files read, 43 pairs` |
| `git grep -c '^# No TARGET: ' -- tests \| wc -l` | 0 | 67 |

**S3** (executed at `77664dc10`). `bin/seal layout --check` exits 0.
It counts 67 files that declare no `TARGET`, fewer than the 86 at the
base. The 67 file paths of its `declares no TARGET` lines equal the 67
paths `git grep -c '^# No TARGET: ' -- tests` lists (executed: `diff`
of the two sorted lists). Each file has a count of 1. So each file the
report names holds exactly one reason line. Whether each ground matches
*The kinds* is the proofer's reading.

**S6 and S7** (executed at `77664dc10`). `bin/seal rules --check` gives
`seal rules: all 176 check lines in 69 rule files hold.` and exits 0.
`bin/seal layout --check` exits 0. This phase moved, renamed and deleted
nothing, so there is no citation to re-point.

**Item 13.** `changelog.md` covers the whole work item. It was written
from the eight phase records and `frame/design.md`. It gives the case
counts of `tests/text/` and `tests/behaviour/` at `b9ca37404` and after
the build: 692 cases in 86 files, then 590 in 82 (executed: `ast` over
each file at both commits, a parametrized case counted once). The merges
of #1482 and #1484 changed cases in those directories too, so the
fragment gives the counts and does not derive a number of removed
cases from them. The moved cases, 65, are the sum of phase 3's 20,
phase 4's 27, phase 5's 5 and phase 7's 13, from their records. No file
the work item changes is one `docs/layout/the-record-layout.md` *A
change writes fragments, never a shared file* names for a process row
(executed: `git diff --name-only 38123f839...HEAD`), so the fragment has
no `### Process changes` table. `frame/plan.md` *Operational impact*
says this pull request does not move the version, and it does not.

**No unit adds behaviour, so no `seal mutate` ran.** The three commits
change prose: a section of `CONTRIBUTING.md` and class docstrings in
test files. `skills/verify/SKILL.md` *The narrow command still has to be
able to fail* says what can fail for prose: whatever parses the file,
and that a module with a changed docstring still imports. The boundary
run below covers both.

**The other statements of the reworded rules, a sample** (executed:
`git grep -n -i` outside `seal/threads/` and `CHANGELOG.md` on "one
shipped module", "several shipped modules", "shipped module whose",
"inside one of the module" and "threshold" beside "pair"). It found one
line, `CONTRIBUTING.md:342`. That sentence is in the move check's
mutation-table rule: "A failing case that stands in a file declaring no
`TARGET` counts for the shipped module whose function it calls as its
subject." It stands. It says how a failing case's mutants are placed,
not where a case stands. A case whose subject is a module under `tests/`
does not stand in a file declaring no `TARGET` once the layout holds. The
search found only the spellings it was given, and a statement worded
otherwise was not checked.

**A record of an earlier phase that HEAD contradicts.**
`trail/phases/phase-7.md` *The pair the move made* says "The pair stood
in the readers-hide file before the move, so `--pairs` still counts 43
pairs, as at phase 6." At `662760c6b`, phase 6's commit, the two oracle
cases were top-level functions of
`tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py`
(executed: `git show`). The reader compares only cases of one class, so
the pair did not stand there. The move into `Test_module` made it. The
count stayed at 43 because the `TestDefinition` pair of the sealer file
left in the same phase. This phase does not write phase 7's record.

**The phase boundary, as one command** (executed at `d215adfe9`, before
these records were written). The set follows the *Phase boundary* row of
`skills/verify/SKILL.md` *Scope: cheap and often, broad and once*. It
holds the 12 test files the phase changed, and the 11 that import one
of them, three of which are among the 12 (executed: `git grep -l` on
`from <stem> import` and `import <stem>` at `32dc787ee`). It holds the
30 files under `tests/` that name `CONTRIBUTING` (executed: `git grep
-l`). Two of them, `tests/censuses.py` and `tests/conftest.py`, are
helpers that hold no case, so pytest collects nothing from them. It
holds the 67 files that declare no `TARGET`, which are the tree-wide
files. `tests/github/test_rules.py` is in it, because
`CONTRIBUTING.md` is a rule file. The 93 paths are in the command:

```
bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_a_commit_names_its_repository.py tests/behaviour/test_a_declared_label_reaches_the_tracker.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py tests/behaviour/test_a_phase_hands_the_next_one_a_record.py tests/behaviour/test_a_probe_that_commits_says_so.py tests/behaviour/test_a_reference_root_is_read_and_never_taken.py tests/behaviour/test_a_release_rolls_the_flow_measurement_issue.py tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py tests/behaviour/test_a_signer_declares_its_pact.py tests/behaviour/test_a_test_file_takes_the_root_from_the_conftest.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_evals_layout.py tests/behaviour/test_every_entry_point_runs_at_the_floor.py tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py tests/behaviour/test_every_shipped_agent_and_document_is_measured.py tests/behaviour/test_every_tracked_file_meets_every_census.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_no_document_names_the_old_roots.py tests/behaviour/test_one_heading_rule_holds_to_commonmark.py tests/behaviour/test_release_hygiene.py tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py tests/behaviour/test_the_contributor_has_a_procedure.py tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py tests/behaviour/test_the_old_block_leaves_through_update.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py tests/behaviour/test_the_release_check_watches_what_ships.py tests/behaviour/test_the_release_seal_is_drawn.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_the_sealer_guarantees.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/behaviour/test_this_repository_passes_its_own_checks.py tests/behaviour/test_unverified_rows_close.py tests/behaviour/test_waiver_decided_at_start.py tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py tests/censuses.py tests/conftest.py tests/github/test_close_issues_on_release.py tests/github/test_label_merged_on_release_branch.py tests/github/test_plugin_directory_check.py tests/github/test_release_completeness_check.py tests/github/test_release_report.py tests/github/test_roll_flow_measurement_issue.py tests/github/test_rules.py tests/github/test_run_tests.py tests/github/test_tracker_labels.py tests/lib/test_launch.py tests/lib/test_routing.py tests/skills/test_agentic_pytest_record.py tests/skills/test_broad_gate.py tests/skills/test_chain_check.py tests/skills/test_fold_check.py tests/skills/test_passages.py tests/skills/test_payload_meter.py tests/skills/test_seal_stamp.py tests/skills/test_seal.py tests/skills/test_session_cost.py tests/skills/test_settle.py tests/text/test_a_cited_commit_outlives_the_squash.py tests/text/test_a_document_has_room_for_the_next_fold.py tests/text/test_a_language_section_of_writing_style_opens_alone.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py tests/text/test_a_question_says_who_can_answer_it.py tests/text/test_a_record_carries_no_comment.py tests/text/test_a_segment_feeds_the_flow_log.py tests/text/test_broad_gate_rule.py tests/text/test_ci_gives_the_checks_what_they_need.py tests/text/test_edits_go_through_the_edit_tool.py tests/text/test_every_agent_reads_the_contract.py tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py tests/text/test_no_case_tells_the_agent_it_is_evaluated.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/text/test_review_axes.py tests/text/test_settle_reads_before_it_removes.py tests/text/test_the_direct_answer_owes_the_sealers_record.py tests/text/test_the_handoff_before_round_one.py tests/text/test_the_mode_is_a_row_and_a_command.py tests/text/test_the_record_is_written_in_words.py tests/text/test_the_records_can_be_carried_out_and_in.py tests/text/test_the_release_tail_does_not_end_at_the_tag.py tests/text/test_the_rules_claude_md_names_have_one_home.py tests/text/test_the_rules_have_one_owner.py tests/text/test_the_settings_have_a_front_door.py tests/text/test_the_suite_runs_with_gh_logged_out.py -q -rs
```

It gave `3117 passed, 9 skipped, 3 warnings` and exited 0 (S9). Seven
skips are `test_a_document_that_names_a_script_says_how_to_reach_it.py:245`.
One is `test_the_windows_leg_runs_in_shards_that_make_the_whole.py:317`,
skipped where the run did not collect the whole suite. One is
`tests/skills/test_broad_gate.py:930`, skipped where the shell is not
`cmd.exe`. The warnings are the pending-correction notices of
`test_a_cited_section_stands_in_its_file.py`. `77664dc10` changes one
docstring of `tests/github/test_roll_flow_measurement_issue.py`. After
it, that module and its importer
`tests/behaviour/test_a_release_rolls_the_flow_measurement_issue.py`
gave `40 passed` (executed). `uvx ruff check` and `uvx ruff format
--check` exit 0 over each changed Python file (executed). The suite
beyond the set is `unverified`, and the orchestrator's broad gate
answers it.

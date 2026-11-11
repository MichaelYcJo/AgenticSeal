# Phase 7: 1794396808-test-files-declare-no-target

## What this phase found

**The frame holds for the range, and eight of its rows do not hold at
`d59eda804`.** The phase started at `3fc2aca87`. Its range is the 22
files of design *The files* from `tests/behaviour/test_release_hygiene.py`
to `tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`,
with the three oracle cases phase 6 left in
`tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py`. The
same 22 stood at `3fc2aca87` (executed: `ls tests/behaviour`). The design's
script of *The cases #1488 read* ran over `tests/text/` and
`tests/behaviour/` written from `18a7e18fb` with `git show`, and printed
341 lines (executed). The 22 files held 235 cases at `3fc2aca87`. Of
these, 79 carry a printed name or the body of a printed case of their file
at `18a7e18fb`, and 156 do not (executed: `ast` over each file at both
commits). Every one of the 235 cases was read whole, with the three oracle
cases.

The rows that do not hold, each against design *The kinds* as the fold
`3fc2aca87` restated it:

| File | The row says | At `d59eda804` | Why |
|---|---|---|---|
| `test_the_contributor_has_a_procedure.py` | T2 | T1 | `test_no_loaded_file_names_a_concrete_release_branch` sweeps every file the plugin loads. A file with a T1 case is T on that ground. |
| `test_the_pull_request_language_is_the_repositorys.py` | T2 | T, on both grounds | Besides the cases that hold the language rows across several files, three cases list files: the mirror case globs `seal/threads/*/pr.*.md`, and the templates cases ask `git ls-files`. |
| `test_the_rules_command_reads_each_rule_off_its_test.py` | T2; a case calling `rules.py` alone moves to `tests/github/test_rules.py` | D, `TARGET = "skills/settle/rule-changes.md"` | No case left calls `rules.py`; phase 5 moved the ones that did. `test_the_rule_marker_is_registered` reads what `tests/conftest.py` registers through `pytestconfig`, so its subject is that module, and it moved to `tests/test_conftest.py`'s `Test_module`. The one case left reads the settle skill alone. |
| `test_the_sealer_guarantees.py` | T1, and no move | T1, with one case moved | `test_the_unfilled_template_is_no_guarantee` calls `lib/fields.py#read` on the template, and asserts what the call returns. That is M for `lib/fields.py`, so it moved to `tests/lib/test_fields.py`'s `Test_read`. |
| `test_the_suite_has_a_command_that_is_cheap_twice.py` | T2 | T1 | `test_every_bin_entry_has_a_windows_twin` and its neighbours list `bin/` with `os.listdir`. |
| `test_the_windows_leg_runs_in_shards_that_make_the_whole.py` | T2 | T1 | Two cases read every node id the suite collects, through `tests/conftest.py#COLLECTED_NODE_IDS`. |
| `test_unverified_rows_close.py` | T2, an M case moving to `tests/lib/test_gaps.py` | T, on the T3 ground | Two cases moved to `tests/lib/test_gaps.py` as the row says. What is left is the T3 fence-walk case and one case that reads `templates/records/sdd-gaps.md`. |
| `test_waiver_decided_at_start.py` | T2 | T, on both grounds | `test_no_agent_definition_tells_an_agent_to_ask_a_person` globs `agents/*.md`, and `test_no_committed_declaration_still_carries_a_template_placeholder` globs `seal/threads/*/routing.md`. |

The readers-hide row holds: of its seven cases, six held
`tests/commonmark_oracle.py` alone and moved to the new
`tests/test_commonmark_oracle.py`. One stays,
`test_the_oracle_imports_the_parser_and_nothing_of_this_repositorys`. It
reads the imports of two modules, the oracle and `tests/block_shapes.py`,
so it is T3 and not M for either.

Plan *Technical context* says a phase writes a module file only for a
module under `tests/` that *The kinds* makes the subject of an M case. That
holds: the two oracle module files are the only new files. The moves into
`tests/lib/test_gaps.py`, `tests/lib/test_fields.py` and
`tests/test_conftest.py` go to files that already stood.

**The order the design states.** `1ff745a3a` is the first unit. The
rider file's three cases read `seal/follow-up.md` alone, so it declares
`TARGET = "seal/follow-up.md"` with its census case, in place of the
reason line (plan *Overlap with the release*, the #1484 row). `747eaf562`
then commits the rulings alone, and `4f4064488` corrects one of them (see
*The rulings shown red*). `edc9ba6e0` aligns two bindings before the move,
`d97c66c38` moves the M cases, and `d59eda804` files each file.
`43b178e13` corrects one explanation in the hygiene file's exemption
table (see *The exemption for `seal.py`'s `4.4.17`*).

**What the rulings did, file by file.** Each row gives the cases #1488
did not read whole, out of the file's cases at `3fc2aca87`. Each assert
a row does not name as removed or changed was kept as it stood. Each
kept assert carries a comment above it that names the fact it holds and
who reads it. The rulings follow #1488's `frame/design.md` *What an
assert reads* and *The criterion*. An absence is kept only where a rule
of the text it reads forbids that text, and the comment cites the rule.
Three files had no assert changed:
`test_settle_applies_rule_changes_in_place.py`,
`test_this_repository_passes_its_own_checks.py` and
`test_the_readers_hide_what_a_renderer_hides.py` apart from one comment.

| File | Unread of all | Removed | Kept with a change |
|---|---|---|---|
| `test_release_hygiene.py` | 28 of 34 | step 3's "no token", "oldest first", "releases page" and "go on to step 4", which are wording, and the `changelog/` and `CHANGELOG.md` absences, which no rule of the step states; the reload case's four sentences of wording | step 3 kept the API URL, `/releases`, the download to a file, `reversed(`, `old < at <= new`, `remote get-url origin` and `marketplaces/agenticseal`; the `Authorization` and `gh ` absences kept, citing *3. Name what changed.* "with no token: `gh` is not used"; the reload case cut to `/reload-plugins` and renamed `test_update_names_the_reload`; the Korean close absence kept, citing `docs/layout/the-record-layout.md` *A fact of a work item has one record, and every other record cites it by path and heading.*; comments above the floor and the `RULES_COMMAND` count |
| `test_the_broad_gate_row_is_asked_for_and_runs_as_written.py` | 5 of 8 | `test_each_allowed_form_is_listed_with_what_it_costs` with `ALLOWED`, and `test_the_template_carries_all_three_rules_of_the_criterion` with `THREE_RULES`, all wording | the refused forms kept as a tuple of the three forms `broad_gate.py` refuses, their reasons dropped, in a case renamed `test_each_refused_form_is_named_in_the_refused_table` |
| `test_the_contributor_has_a_procedure.py` | 6 of 10 | the "review round record" parameter, which names no path a contributor writes | comments above the heading, the concrete-branch sweep, citing the release checklist's timer rule, and the history sentences |
| `test_the_gate_asks_the_range_ci_will_ask.py` | 8 of 9 | none | comments above the `REMOTE_TRACKING` prefix and equality, the one call, the docstring case and the env count |
| `test_the_old_block_leaves_through_update.py` | 8 of 12 | step 4's list of what is gone, wording; the installer case's absence half | step 4 cut to `SessionStart`, `*Needs action*` and `CLAUDE.md.bak`, in a case renamed `test_step_4_names_the_hook_the_output_section_and_the_backup`; the `CLAUDE.md` marker absence kept, citing "This file imports nothing and copies nothing."; comments above the template equality and `python3 -c` |
| `test_the_pull_request_language_is_the_repositorys.py` | 21 of 31 | `test_the_surface_no_longer_requires_english_of_everyone` and `test_the_surface_defers_to_the_row_instead`, absences of text a release removed with no rule forbidding it; `test_the_documents_name_the_repair_of_a_file_the_parser_refuses` with `PROSE_HEADINGS`, wording | a comment above the round template's fields |
| `test_the_readers_hide_what_a_renderer_hides.py` | 7 of 7 | none | a comment above the absence loop, citing `tests/commonmark_oracle.py` *It shares nothing with what it checks* |
| `test_the_release_check_watches_what_ships.py` | 10 of 12 | `test_the_refusal_asserts_neither_case`, an absence no rule of the workflow states | comments above the pattern, the names, the document's roots and `exit 1` |
| `test_the_release_seal_is_drawn.py` | 1 of 2 | the `pillow` absence, which no rule of the workflow states | a comment above the pinned parser |
| `test_the_rules_command_reads_each_rule_off_its_test.py` | 2 of 2 | the grammar case's sentences of wording | the grammar case cut to `` `check: ` ``, `` `@pytest.mark.rule("<marker>")` `` and `` `seal rules --check` `` |
| `test_the_seal_is_taken_once_by_the_sealer.py` | 8 of 13 | `test_the_sealer_cites_the_section_without_carrying_it` with `CONTRACT`, `WINDOW` and `section()`, wording | the measurement case cut to the spellings a reader types or a script matches (the table's `| 3 |`, `-p agentic_pytest_record`, `PYTEST_ADDOPTS`, `PYTHONPATH`, `failing on base too`, `new?`, `new`, `suite-at-base.txt`, `suite.txt`, `FAILED`, `end`, `trail/gate.md`, the criterion's rule 3 and `` bin/test -q \| tee out.txt ``); `PROBE` cut to the proofer's `` `evidence: executed` ``; the four-conditions case cut to `executed` and `unverified` and renamed `test_the_sealer_carries_the_labels_its_claims_are_written_under` |
| `test_the_sealer_guarantees.py` | 6 of 12 | the template case's table header asserts | the template case kept the block's keys and the two headings `docs/forms/the-guarantee.md` cites; step 4 cut to `routing.md`, `Implementation`, `crafter`, `frame/plan.md`, `trail/phases/phase-N.md` and `withheld`; a comment above the grader absence |
| `test_the_set_a_work_item_always_has.py` | 1 of 6 | `test_the_skill_lists_the_second_rung_work_and_what_lifts_it`, wording | none |
| `test_the_stamp_reaches_the_person_it_is_drawn_for.py` | 4 of 7 | the README case's sentences and its `gone` absences | the README case cut to `README_FACTS`, eleven facts each edition states |
| `test_the_suite_has_a_command_that_is_cheap_twice.py` | 8 of 15 | `test_both_wrappers_say_the_same_thing_when_the_runner_is_missing`, a two-file equality, and `test_the_section_states_the_floor_once`, wording; the `pillow` absence | a comment above the pinned parser |
| `test_the_windows_leg_runs_in_shards_that_make_the_whole.py` | 5 of 8 | the `merge-multiple` absence, which no rule of `test.yml` states | comments above the split and store suffixes, the save step's `if` and `github.run_attempt` |
| `test_this_repository_passes_its_own_checks.py` | 2 of 5 | none | none |
| `test_unverified_rows_close.py` | 4 of 5 | `test_no_text_that_states_the_closing_shows_the_old_mark` with `OLD_MARK` and `CLOSING_TEXTS`, an absence of text a release removed | none |
| `test_update_reads_the_config_directory_in_use.py` | 6 of 6 | the `seal stamp --` and `Stamp: <` absences | step 4b cut to `` | `launcher <path>` | ``, the settings path and the launcher's command span; the `AskUserQuestion` absence read in step 4b alone, citing its "This step asks nothing and writes nothing."; comments above the `python3 -c` count, the `p=$(` and `printf` lines, `repo=$(` and `/.claude` |
| `test_waiver_decided_at_start.py` | 13 of 27 | `SHAPE`; `test_every_box_states_what_UNCHECKED_means` and `test_the_exit_names_what_does_not_run_rather_than_where_it_ends`, wording | the table count renamed `test_both_questions_offer_four_options`; the marked answer cut to `` ` (Recommended)` `` and renamed `test_question_1_spells_the_mark_of_its_marked_answer`; the blocked-step case kept the core's citation, read in the rule's own paragraph; a comment above the `NEWEST` placeholder |
| `test_whether_a_line_is_live_is_asked_by_what_the_line_does.py` | 3 of 3 | none | comments above the found set, the spelling and the absence, which cites `docs/checks/the-fold.md` *Whether a line is live is asked by what the line does* |

The rulings removed 13 cases and renamed 6. `git grep -n -w` outside
`seal/threads/` and `CHANGELOG.md`, on each removed or renamed case and on
each removed constant, lists only unrelated names in other modules
(`lib/gaps.py#OLD_MARK`, `lib/fields.py#SHAPE` and the like). No line
cites a removed or renamed case (executed).

**The rulings shown red** (executed). Each ran as `bin/seal mutate <file>
--replace <old> <new> --tests "bin/test <module> -q -p no:xdist -k <k>"`.
No shipped unit changed in this phase, so each run breaks the fact a kept
or changed assert holds, in the file it reads.

| Fact broken | File | Cases | Verdict |
|---|---|---|---|
| `reversed(` as `sorted(` | `skills/update/SKILL.md` | `test_release_hygiene.py -k github_releases` | red |
| the trailing `&` row respelt | `templates/setup/config.md` | `test_the_broad_gate_row_is_asked_for_and_runs_as_written.py -k refused_table` | red |
| `gaps.md` as `gaps.txt` | `CONTRIBUTING.md` | `test_the_contributor_has_a_procedure.py -k exemption_list` | red |
| `CLAUDE.md.bak` as `CLAUDE.md.old` | `skills/update/SKILL.md` | `test_the_old_block_leaves_through_update.py -k names_the_hook` | red |
| `## Findings` as `## Found` | `templates/records/sdd-round.md` | `test_the_pull_request_language_is_the_repositorys.py -k round_template_carries` | red |
| the marker without its quotes | `skills/settle/rule-changes.md` | `test_the_rules_command_reads_each_rule_off_its_test.py -k settle_owns` | red |
| `-p agentic_pytest_record` respelt | `templates/setup/config.md` | `test_the_seal_is_taken_once_by_the_sealer.py -k measurement` | red |
| `phase-N.md` as `phase.md` | `agents/sealer.md` | `test_the_sealer_guarantees.py -k step_4` | red |
| the stamp directory respelt | `README.ko.md` | `test_the_stamp_reaches_the_person_it_is_drawn_for.py -k readmes` | red |
| `github.run_attempt` as `github.run_id` | `.github/workflows/test.yml` | `test_the_windows_leg_runs_in_shards_that_make_the_whole.py -k no_pull_request_saves` | red |
| `` `bin/` `` as `` `binaries/` `` | `docs/releasing/branch-and-release.md` | `test_the_release_check_watches_what_ships.py -k release_document` | red |
| ` (Recommended)` as ` (Suggested)` | `skills/implement/routing-question.md` | `test_waiver_decided_at_start.py -k spells_the_mark` | red |
| the core's citation cut to *The rule* | `agents/framer.md` | `test_waiver_decided_at_start.py -k a_mark_is_not` | survived at `747eaf562`; red after `4f4064488` |
| `#live_lines` as `#live` | `docs/checks/the-fold.md` | `test_whether_a_line_is_live_is_asked_by_what_the_line_does.py -k statement_names` | red |
| `## The parties` as `## Parties` | `templates/records/sdd-guarantee.md` | `test_the_sealer_guarantees.py -k verdict_block` | red |
| a start marker written into `CLAUDE.md` | `CLAUDE.md` | `test_the_old_block_leaves_through_update.py -k carries_no_copy` | red |
| `exit 1` as `exit 0` | `.github/workflows/hygiene.yml` | `test_the_release_check_watches_what_ships.py -k still_fails` | red |
| step 4b's sentence replaced by one that asks | `skills/update/SKILL.md` | `test_update_reads_the_config_directory_in_use.py -k 4b` | red |

The framer's citation survived because the case read it anywhere in
`agents/framer.md`, and the file cites the same section twice. The case
now reads the paragraph its lead, **A mark is not the answer to a blocked
step.**, opens, and `4f4064488` holds that. The same mutant gave red at
`d59eda804` too (executed).

**The binding alignment** (design *Scope* item 5). `edc9ba6e0` made two
files bind a name as their destination binds it, before the move. In
`test_unverified_rows_close.py`, `gaps` became `GAPS`, loaded as
`load_lib_module("gaps.py", "gaps_for_its_own_file")`, as
`tests/lib/test_gaps.py` loads it. That commit rewrote
`test_the_skill_shows_the_word` and
`test_the_template_is_the_shape_the_checker_reads`. In
`test_the_sealer_guarantees.py`, `fields` became
`load_lib_module("fields.py", "agentic_fields_under_test")`, as
`tests/lib/test_fields.py` loads it, in place of `chain.FIELDS`. That
commit rewrote no case body: `CHAIN` and `chain` went, and `TEMPLATE`
became a `pathlib.Path`, as the destination reads it.

**The moves** (design *Scope* item 5, executed after `edc9ba6e0`). The
three M cases bound for `tests/lib/` moved unchanged:
`test_the_skill_shows_the_word` and
`test_the_template_is_the_shape_the_checker_reads` to
`tests/lib/test_gaps.py`'s `Test_check_file`, and
`test_the_unfilled_template_is_no_guarantee` to
`tests/lib/test_fields.py`'s `Test_read`. The sealer file imports
`TEMPLATE` and `fields` from `tests/lib/test_fields.py`.
`test_the_rule_marker_is_registered` moved to `tests/test_conftest.py`'s
`Test_module`. The six oracle cases of the readers-hide file, and the
strip set `DROPPED_BY_THE_STRIP` that one of them reads, moved to the new
`tests/test_commonmark_oracle.py`. The three cases of
`test_one_table_walker_reads_what_gfm_renders.py` moved to the new
`tests/test_gfm_table_oracle.py`, and that file, left with no case, was
deleted (*Scope* item 8). No line under `docs/` named it, so no
unsettled operation holds it.

```
bin/seal layout --moved edc9ba6e0 --from tests/behaviour/test_unverified_rows_close.py tests/behaviour/test_the_sealer_guarantees.py tests/lib/test_gaps.py tests/lib/test_fields.py --to tests/behaviour/test_unverified_rows_close.py tests/behaviour/test_the_sealer_guarantees.py tests/lib/test_gaps.py tests/lib/test_fields.py
```

It printed `seal layout: moved: 66 old cases, 201 items against 201 at
edc9ba6e0d56, 0 failed` and exited 0.

```
bin/seal layout --moved edc9ba6e0 --from tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py tests/test_conftest.py --to tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py tests/test_conftest.py tests/test_gfm_table_oracle.py tests/test_commonmark_oracle.py
```

It printed `seal layout: moved: 44 old cases, 160 items against 160 at
edc9ba6e0d56, 0 failed` and exited 0, before and after the pair's
docstring went into `tests/test_commonmark_oracle.py`. No move exited 1,
so no mutation table is owed.

**The two oracle module files pass every census.** `censuses.judge` gave
`[]` over `tests/commonmark_oracle.py` and `tests/gfm_table_oracle.py`, and
over the three D targets of the phase, `seal/follow-up.md`,
`skills/settle/rule-changes.md` and `skills/update/SKILL.md` (executed).
Each new module file declares `TARGET` first after its imports and ends
with `test_census = census_case(TARGET)`. Its cases stand in `Test_module`,
because neither oracle module had a class for the function each case
calls. `bin/seal layout --check` now prints a `report:` line for each
public function of the two oracle modules that has no class. Design *Out*
leaves those lines out of this work.

**The pair the move made** (design *Scope* item 11).
`tests/test_commonmark_oracle.py::Test_module` holds
`test_the_oracle_names_each_kind_it_hides` and
`test_the_oracle_counts_the_lines_the_parsers_strip_dropped`, a pair
`bin/seal layout --pairs` prints. The class docstring states the input
they differ by. The pair stood in the readers-hide file before the move,
so `--pairs` still counts 43 pairs, as at phase 6.

**The filing.** The three D files declare `TARGET` first after their
imports and end with `test_census = census_case(TARGET)`. Each constant
that stated the same path derives from it through `TARGET.split("/")`.
`test_settle_applies_rule_changes_in_place.py` and
`test_the_rules_command_reads_each_rule_off_its_test.py` both declare
`skills/settle/rule-changes.md`, and design *The kinds* keeps two such
files apart. The 19 other files carry one `# No TARGET: ` line in its
place. Each D file's `TARGET` was shown read: `bin/seal mutate` pointed it
at another skill, and each module went red (executed, at `d59eda804`).

**Item 10, the docstrings.** Three docstrings said their cases wait for
#923: the settle example's file, `test_the_release_seal_is_drawn.py` and
`test_the_suite_has_a_command_that_is_cheap_twice.py`. Seven said where
cases stood before a move, or what an earlier phase placed where: those
three, `test_the_rules_command_reads_each_rule_off_its_test.py`,
`test_the_readers_hide_what_a_renderer_hides.py`,
`test_unverified_rows_close.py`, `test_the_sealer_guarantees.py` and
`test_this_repository_passes_its_own_checks.py`. Each now says what the
file holds and where the moved cases stand.

**Item 9, the citations** (executed: `git grep -n` on each moved case's
name, on the deleted file's stem and on each changed file's name, outside
`seal/threads/`). Six lines in five files cited the deleted file or said
the old file keeps the oracle's own cases. `tests/block_shapes.py`,
`tests/gfm_table_oracle.py`, `tests/github/test_rules.py`,
`tests/lib/test_routing.py` and `tests/lib/test_tables.py` now name the
new homes. Some lines still name a changed file and stand, because what
they state is still true:

- `tests/commonmark_oracle.py:10` says the readers-hide file reads the
  oracle's own imports, and its one case still does.
- `tests/lib/test_blocks.py:3,7`, `tests/lib/test_tables.py:57` and
  `tests/skills/test_unverified_check.py:3` still hold.
- `docs/layout/the-record-layout.md:156` names
  `test_unverified_rows_close.py`, which keeps the memo headings case.
- `docs/forms/the-guarantee.md:20,23,26` and
  `docs/running/the-agent-set.md:112` name the sealer file, which keeps
  the template, definition and committed-guarantee cases.

The rule at `docs/forms/the-guarantee.md:26` lost one case to
`tests/lib/test_fields.py`, and still has `tests/skills/test_chain_check.py`
on its check line and the template's verdict-block case in the sealer
file. So the line still names cases that hold the rule, and it was not
edited.

**S6 and S7** (executed at `d59eda804`). `bin/seal rules --check` gives
`all 176 check lines in 69 rule files hold.` and exits 0.
`bin/seal layout --check` exits 0, and its last line is `141 files read,
0 refused, 67 declare no TARGET`. The counts against phase 6's `140` and
`72` add up as follows:

- `141`: the two new oracle module files add two, and the deleted walker
  file takes one away.
- `67`: the walker file and the four new D files (the rider's and this
  phase's three) take five away.

`git grep -c '^# No TARGET: ' -- tests | wc -l` gives 67, one line for
each file the report counts. `bin/seal layout --pairs` gives `141 files
read, 43 pairs`.

**The phase boundary, as one command** (executed at `d59eda804`, before
these records were written). The set follows design *The narrow run*.
It holds every test module the phase changed or added, including the
destinations. It also holds each test module that named a changed path's
file name at `3fc2aca87` (executed: `git grep -l -F` per changed path).
With them come the check run, the census sweep, the shrunken-corpus
module and `tests/github/test_rules.py`. The 58 paths are in the command:

```
bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/behaviour/test_a_phase_hands_the_next_one_a_record.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py tests/behaviour/test_every_tracked_file_meets_every_census.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_one_heading_rule_holds_to_commonmark.py tests/behaviour/test_release_hygiene.py tests/behaviour/test_settle_applies_rule_changes_in_place.py tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py tests/behaviour/test_the_contributor_has_a_procedure.py tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py tests/behaviour/test_the_old_block_leaves_through_update.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py tests/behaviour/test_the_release_check_watches_what_ships.py tests/behaviour/test_the_release_seal_is_drawn.py tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_the_sealer_guarantees.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/behaviour/test_this_repository_passes_its_own_checks.py tests/behaviour/test_unverified_rows_close.py tests/behaviour/test_update_reads_the_config_directory_in_use.py tests/behaviour/test_waiver_decided_at_start.py tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py tests/github/test_rules.py tests/github/test_run_tests.py tests/lib/test_blocks.py tests/lib/test_fields.py tests/lib/test_gaps.py tests/lib/test_routing.py tests/lib/test_tables.py tests/skills/test_broad_gate.py tests/skills/test_chain_check.py tests/skills/test_rule_changes.py tests/skills/test_seal_stamp.py tests/skills/test_settle.py tests/skills/test_test_layout.py tests/skills/test_unverified_check.py tests/test_censuses.py tests/test_commonmark_oracle.py tests/test_conftest.py tests/test_gfm_table_oracle.py tests/test_workflows.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_a_rider_reaches_its_file.py tests/text/test_every_agent_reads_the_contract.py tests/text/test_settle_reads_before_it_removes.py tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/text/test_the_records_can_be_carried_out_and_in.py tests/text/test_the_rules_have_one_owner.py -q -rs
```

It gave `2984 passed, 8 skipped` and exited 0 (S9). At `43b178e13`, which
changes one string and one comment, the same command gave the same
counts and exited 0, and the two checks above gave the same last lines
(all executed). Seven skips are
`test_a_document_that_names_a_script_says_how_to_reach_it.py:245`, which
skips a script no shipped document names. One is
`test_the_windows_leg_runs_in_shards_that_make_the_whole.py:317`, which
skips where the run did not collect the whole suite. The suite beyond the
set is `unverified`, and the orchestrator's broad gate answers it.

**The exemption for `seal.py`'s `4.4.17`** (the orchestrator's note,
after `d59eda804`). `VERSIONS_OF_ANOTHER_PRODUCT` in
`test_release_hygiene.py` explained that row as "bash's, named in a
comment about the glob behaviour of that release". The only `4.4.17` in
`skills/implement/scripts/seal.py` is in `unsafe`'s docstring, and there
it is the zip specification's section number: "A zip stores
`/`-separated names (APPNOTE 4.4.17)" (read, `:804-805`). The exemption
is still needed. With its key changed, the sweep went red (executed:
`bin/seal mutate` on the key, `-k at_or_above_the_running_one`). So
`43b178e13` keeps the row and makes its explanation say what the token
is. The comment above the git rows said "the `seal.py` and `broad_gate.py`
rows", which read as if this row were a git measurement too. It now names
the `seal.py` row for `2.50.1`. No case reads the explanations, and the
fixtures of `test_the_declared_token_is_the_one_the_refusal_printed` and
`test_another_products_version_is_allowed_only_in_the_file_that_declares_it`
use a bash sentence as invented input, not as a claim about `seal.py`.
They stand.

**What the frame states that HEAD contradicts, for the framer.** These
are in files this phase does not write:

- Design *The files* rows 201, 204, 208, 210, 213, 214, 216 and 218, as the
  first table above gives them.
- `CONTRIBUTING.md` *The test layout*, `:263-275`, makes a case M only for
  a shipped module, and T3 a property across several shipped modules. The
  fold `3fc2aca87` widened design *The kinds* to count a module under
  `tests/` for both. This phase built to the design: it moved the oracle
  cases as M for their modules, and filed the readers-hide case as T3
  across two modules under `tests/`.

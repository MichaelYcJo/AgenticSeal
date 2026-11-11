# Phase 2: 1794396808-test-files-declare-no-target

## What this phase found

**The frame holds for `tests/text/`, with one premise that does not.**
The phase started at `34ecce1ac`. Its rows of design *The files* name the
35 files of `tests/text/` that stood at `b9ca37404`, and the same 35 stood
at `34ecce1ac` (executed: `ls tests/text/*.py`). The design's script of
*The cases #1488 read* ran over `tests/text/` and `tests/behaviour/`
written from `18a7e18fb` with `git show` (executed). It printed 341
lines, as design G6 counts. Of the 195 cases of `tests/text/` at
`34ecce1ac`, 86 carry a printed name, and 109 do not (executed: `ast`
over each file). Ten of the 109 were renamed after `18a7e18fb`, by
`3285f1a04`, `dbed1d5ff` and `957a3bc7d`. Each has the body of a printed
case, so #1488 read it (read: the three diffs). The 99 others are the
cases *Scope* item 4 rules here. `test_the_table_reads_this_run_s_union_and_the_tag_s_push_run_s`
of `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`
is new in `dbed1d5ff` (#1486) and is one of the 99.

**The premise that does not hold: a printed case was not always read.**
The design's script prints a case whose file #1488 held *Out*. #1488's
`frame/design.md:45` puts `tests/text/test_ci_gives_the_checks_what_they_need.py`
in *Out* (read), and its `trail/phases/phase-5.md:243` names that module as
*Out* again (read). So its three printed cases were never ruled. This
phase ruled all nine of its cases, and kept every assert, because each
one reads a workflow key the runner acts on. The same line of #1488's
*Out* names `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`
and one case of `tests/behaviour/test_a_release_publishes_its_note.py`.
Both stand in design *The files*, and the script prints their cases as
read. They belong to phases 6 and 7, so this phase did not change them.
The hand-back names this for the framer.

**The order the design states.** `dca3aed49` commits the rulings alone.
`685c8a739` then gives each file of `tests/text/` its `TARGET` or its
reason line, so the filing commit changes no assert. No case of
`tests/text/` is kind M, so nothing moved, and S4's `--moved` run does
not apply.

**What the rulings did, file by file.** Each row gives the number of the
99 cases the file holds. Every case of the 99 was read whole. Each assert
a row does not name as removed or changed was kept as it stood. Each
kept assert carries a comment above it that names the fact it holds and
who reads it. The rulings follow #1488's `frame/design.md` *What an
assert reads* and *The criterion*.

| File | Ruled | Removed | Kept with a change |
|---|---|---|---|
| `test_a_cited_commit_outlives_the_squash.py` | 11 | none | none: each assert reads what the citation check returned |
| `test_a_document_has_room_for_the_next_fold.py` | 1 | `test_settle_owns_the_placement_rule`, three phrases of wording | none |
| `test_a_language_section_of_writing_style_opens_alone.py` | 1 | none | none |
| `test_a_merged_ticket_says_so_on_the_tracker.py` | 2 | none | none |
| `test_a_moved_rule_leaves_its_definition.py` | 8 | six phrases of `MOVED_OUT_OF_CRAFTER`; "whether that label is honest" and the crafter's "hand-back" of `test_a_citation_is_not_a_copy`; the clause of the proofer's rule; the rule "A new test starts from its group." and the waiver's absence assert | the `multiSelect` absence, with a comment citing `agents/crafter.md` *Never*; the proofer's application cut to `rule 9` and `` `## Not judged` ``; the proofer's lead cut to the part `skills/code-review/orchestration.md` cites, in a case renamed `test_the_proofer_keeps_its_rule_on_the_records_a_round_reads_whole`; the crafter's two rules cut to the commands and the citation they name, in a case renamed `test_the_crafters_rules_name_what_their_readers_resolve`; a comment citing `skills/core/SKILL.md` *The rule a mechanism is kept against* above each copy check |
| `test_a_parallel_agent_names_its_scratch_after_the_work_item.py` | 2 | none | comments above the `FRAME_HOME`, `PHASE_HOME` and `FIX_HOME` asserts |
| `test_a_record_carries_no_comment.py` | 3 | none | a comment citing `docs/layout/the-record-layout.md` *A record a template starts carries no HTML comment.* |
| `test_a_rider_reaches_its_file.py` | 1 | none | a comment citing `seal/follow-up.md`'s rule on a `# RIDER:` comment |
| `test_a_segment_feeds_the_flow_log.py` | 3 | `RUN_TABLE_ROWS`, `test_the_section_states_the_run_level_table` and `test_the_run_level_table_carries_every_row`: row labels no script reads | none |
| `test_broad_gate_rule.py` | 2 | the `text.index` order assert, which located wording | the preflight case, renamed `test_the_order_inside_a_ticket_names_the_preflight` |
| `test_ci_gives_the_checks_what_they_need.py` | 9, see above | `POINTER` | the shared-steps case asserts that the one comment above each shared step names the template's path |
| `test_edits_go_through_the_edit_tool.py` | 2 | `test_the_rule_no_longer_rests_on_the_commit_gate`, `test_no_carrier_claims_a_fact_about_the_reader_repository` and `CRAFTER` | none |
| `test_every_agent_reads_the_contract.py` | 8 | `BOUNDS` and `test_every_definition_bounds_what_it_writes`; the rewrap half of `test_a_sentence_anywhere_but_the_opening_is_caught` | the opening is held to the two paths it names, not to one sentence in every definition |
| `test_no_case_tells_the_agent_it_is_evaluated.py` | 2 | none | a comment citing `evals/README.md` *No case tells the agent under test that the run is a measurement.* |
| `test_no_passage_is_pasted_into_a_second_file.py` | 3 | none | none |
| `test_review_axes.py` | 5 | `test_the_tracer_names_what_the_list_of_the_surface_lacks` and `test_a_record_written_before_a_line_was_added_is_no_finding` | the located-in-both case cut to `` `location:` `` and `` `frame/design.md` ``; the resolution order to `~/.claude/agentic/parity-paths.json` and `original not found`; the later-round case to `## Probes` and `evidence: executed` |
| `test_settle_reads_before_it_removes.py` | 1 | `test_the_skill_orders_the_row_kinds_so_only_a_needed_measurement_opens_an_issue`: row-kind labels no script reads | none |
| `test_the_agent_contract_holds_the_universal_rules.py` | 10 | none | none |
| `test_the_direct_answer_owes_the_sealers_record.py` | 2 | `STANDS`, `REVIEW_CHAIN_DOCS`, `review_chain_text` and the absence branch | the carrier case holds `trail/gate.md` |
| `test_the_handoff_before_round_one.py` | 1 | `test_the_protocol_no_longer_states_the_rules_it_points_at` | none |
| `test_the_record_is_written_in_words.py` | 2 | none | a comment citing `docs/forms/the-round-record.md`, each definition's *Never* and `skills/verify/SKILL.md` |
| `test_the_release_table_reads_two_trees_and_fails_nothing.py` | 1 | none | none |
| `test_the_release_tail_does_not_end_at_the_tag.py` | 3 | none | none |
| `test_the_rules_claude_md_names_have_one_home.py` | 6 | the `cadence` and `lint` rules, `CARRIERS`, `test_no_carrier_restates_a_home`, `test_a_restored_copy_is_named` and `test_a_section_stops_at_its_sibling` | each home's facts cut to the merge table's row and the commands a reader runs |
| `test_the_rules_have_one_owner.py` | 9 | rules 3, 7, 17, 19 and 20 of `RULES`, whose owner sentences were wording; `PR_FILES_OWNER` and `PR_FILES_OWNER_KO` | `RULES` holds each owner's facts and each link's citation of the owner; the framer's route holds `deferred the frame` and `answer:`; the mergeable case its commands, states, numbers and flag; the decision case 19 paths, citations and one command; the handoff case three file names; the recurring-problem case its lead and the paragraph it cites |
| `test_the_settings_have_a_front_door.py` | 1 | none | a comment above the rows assert |
| `test_the_verifying_round_is_bounded_not_cheapest.py` | 3 | the file: every case held wording or the absence of wording a release removed | none |

**One case #1488 had read changed with a helper it shares.**
`test_every_agent_reads_the_contract.py#shape_problems` held each
definition's opening paragraph equal to one sentence. That is the shape
*The criterion* counts as wording: a sentence that stands in two files in
the same words. The helper now holds the opening to the two paths it
names. So the half of `test_a_sentence_anywhere_but_the_opening_is_caught`
that rewrapped the sentence had nothing left to show, and it went too.
#1488 had read that case. The ruling of the helper decided it, under the
same criterion.

**The deleted file.** `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py`
was left with no case. `git grep -n test_the_verifying_round_is_bounded_not_cheapest`
outside `seal/threads/` finds nothing (executed), so *Scope* item 8's
reason line for a file a check line names does not apply.

**The kinds, against design *The files*' starting kinds** (`frame/questions.md`
Q1). Seven files differ. Each was ruled by design *The kinds*.

| File | Starting kind | Kind here | Ground |
|---|---|---|---|
| `test_a_language_section_of_writing_style_opens_alone.py` | T2 | T1 | its case globs `agents/*.md` for every definition that names a language section |
| `test_a_moved_rule_leaves_its_definition.py` | T2 | T1 | its cases glob `agents/*.md` and walk every numbered rule of the contract |
| `test_ci_gives_the_checks_what_they_need.py` | T2 | T1 | its cases list every workflow under `.github/workflows/` |
| `test_the_record_is_written_in_words.py` | T2 | T1 | its cases glob `agents/*.md`, `skills/*/*.md` and `templates/*/*.md` |
| `test_the_chain_section_has_one_shape.py` | T2 | D, `skills/commit-pr-convention/SKILL.md` | both its cases read that file alone |
| `test_the_release_table_reads_two_trees_and_fails_nothing.py` | T2 | D, `.github/workflows/test.yml` | its cases read that workflow alone |
| `test_a_segment_feeds_the_flow_log.py` | D | T2 | its case on `skills/verify/SKILL.md` was kept, because it holds a path a reader resolves; the design's row gives T2 for that outcome |

The filing gives `TARGET` and `test_census = census_case(TARGET)` to eight
files. These are `test_a_merged_ticket_says_so_on_the_tracker.py`,
`test_a_release_cannot_ship_an_untrue_milestone.py`,
`test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`,
`test_the_suite_runs_with_gh_logged_out.py`,
`test_the_gate_hands_cmd_a_path_it_can_run.py`,
`test_the_chain_section_has_one_shape.py`,
`test_the_release_table_reads_two_trees_and_fails_nothing.py` and
`test_the_agent_contract_holds_the_universal_rules.py`. In each, the
constant that stated the same path now derives from `TARGET`, so the path
is written once. The other 26 files carry one `# No TARGET: ` line. The
proofer reads each ground against *The kinds*.

**The census sweep caught the first filing.** The first filing joined
`TARGET` to `ROOT` with `os.path.join(ROOT, TARGET)` in five files.
`tests/behaviour/test_every_tracked_file_meets_every_census.py` failed on
it, for the `slash_in_join` census (executed). Each of the five now passes
`*TARGET.split("/")`, before `685c8a739`.

**Item 10, the docstrings.** Ten files said their cases wait for #923, or
said where #942 placed the cases that left. Each now says what the file
holds and where the module's cases stand.

**The rulings shown red** (executed after `dca3aed49`, each command
exited 0). Each ran as `bin/seal mutate <file> --replace <old> <new>
--tests "bin/test <module> -p no:xdist -q [-k <cases>]"`. No shipped unit
changed in this phase, so the runs break the fact a changed assert
holds, in the document it reads.

| Fact broken | File | Cases | Verdict |
|---|---|---|---|
| `806,241` to `806,240` | `skills/code-review/orchestration.md` | `test_the_rules_have_one_owner.py -k owner_states` | red |
| `` `multiSelect` `` written into the crafter's *Never* | `agents/crafter.md` | `test_a_moved_rule_leaves_its_definition.py -k claims_no_act` | red |
| `` `deferred the frame` `` without its backticks | `skills/code-review/orchestration.md` | `test_the_rules_have_one_owner.py -k framers_route` | red |
| the contract's path left out of the proofer's opening | `agents/proofer.md` | `test_every_agent_reads_the_contract.py -k shape_and_preloads` | red |
| `` `git switch` `` without its backticks | `skills/implement/orchestration.md` | `test_the_rules_claude_md_names_have_one_home.py` | red |
| the owner's section name changed in the link | `CONTRIBUTING.md` | `test_the_rules_have_one_owner.py -k link_names` | red |

One more run left the contract's path in the proofer's opening, and the
case stayed green. That is the right verdict, since the path was still
there. `trail/gate.md` stands three times in
`docs/running/the-review-and-parity-arms.md`, so no single replacement
breaks it, and it was not run.

**S6 and S7** (executed at `685c8a739`). `bin/seal rules --check` exits 0.
`git grep -n -w` outside `seal/threads/` and `CHANGELOG.md`, on each
removed or renamed case and constant and on the deleted file's stem, lists
only `MOVED_OUT_OF_CRAFTER` in its own file. `bin/seal layout --check`
exits 0, and its last line is `138 files read, 0 refused, 77 declare no
TARGET`. Against phase 1's `139` and `86`, the deleted file accounts for
one of each, and the eight `TARGET` lines for the other eight.
`bin/seal layout --pairs` gives `138 files read, 42 pairs`, as at phase 1.
`git grep -c '^# No TARGET: ' -- tests/text | wc -l` gives 26.

**The phase boundary, as one command** (executed at `685c8a739`, before
these records were written):

```
bin/test tests/text tests/behaviour/test_this_repository_passes_its_own_checks.py tests/behaviour/test_every_tracked_file_meets_every_census.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_the_release_check_watches_what_ships.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_waiver_decided_at_start.py tests/evals/test_noninferiority.py tests/github/test_label_merged_on_release_branch.py tests/github/test_release_completeness_check.py tests/github/test_release_report.py tests/lib/test_config.py tests/skills/test_fold_check.py tests/skills/test_passages.py tests/skills/test_seal.py tests/skills/test_settle.py tests/test_censuses.py tests/skills/test_test_layout.py tests/github/test_rules.py -q
```

The set follows design *The narrow run*. It holds `tests/text`, and each
test module outside it that named a changed file's stem at `34ecce1ac`
(executed: `git grep -l -w` over `tests/` and `evals/`). It holds the
check run, the census sweep, `tests/github/test_rules.py` and
`tests/skills/test_test_layout.py`. `evals/scripts/rule_cases.py` names
`test_no_case_tells_the_agent_it_is_evaluated.py` only in a comment. It
gave `2161 passed` and exited 0 (S9). Run again with this record,
`gaps.md` and the Status cell written, it gave `2161 passed` and exited 0. The suite beyond the set is
`unverified`, and the orchestrator's broad gate answers it.

**Two reason lines were widened after a read.** The reason lines of
`test_review_axes.py` and `test_settle_reads_before_it_removes.py` named
fewer files than their cases read. They were widened, and the second
file's docstring with its line, before `685c8a739`.

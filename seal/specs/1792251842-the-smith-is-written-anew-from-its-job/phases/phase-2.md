# 1792251842-the-smith-is-written-anew-from-its-job — phase 2

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | aea8c8e5 |
| Ran by | specseal:smith on Opus 5.5, part b; part a is e61ac4e1 |

## What this phase was asked

Part a wrote `agents/smith.md` and `skills/implement/SKILL.md` anew (e61ac4e1).
Part b, unattended and with no paid run: make the tree agree with that
rewrite. Take the proof block out of `agents/smith.md`, the word included, and
out of its other readers as `spec.md` §*Removes* names them:
`skills/verify/SKILL.md`'s seal section and `## Seal block`, rewritten to the
fact that the hand-back's labels carry the claims and `guarantee.md` is the one
seal; `templates/sdd-overview.md`'s applied block; `session_cost.py`'s
docstring; the README rows, with the smith's preload row listing
`agent-contract`. Sort every failing pin per `questions.md` Q5: re-point it where
the rule stays, remove it with one line here where it pinned narration or a
removed rule, and never weaken a pin while its rule stays. T4 replaces the
gate-owner case and the smith's `OWNER_NAMED` use. Delete the smith's
`NOT_YET_REWRITTEN` entry, add both rewritten files to `COVERED` (Q2's
default), plant T3, T4 and T5 as `plan.md`'s test rows name them, each seen red
by its row's mutation, and say whether the two failures that may predate part
a did.

## What this phase found

**The frame's list of pins was a floor, not the set.** `plan.md` named 18
smith modules from `git grep "smith|implement/SKILL"`, and the spawn prompt
named 22 from `git grep "agents/smith|implement/SKILL"`. Neither grep matches
a module that opens the file as `flat("agents", "smith.md")`, which is how
`tests/test_broad_gate_rule.py` and `tests/test_a_probe_does_not_outlive_its_round.py`
read it. Each held one smith pin that part a had already broken and no list
named. The grep that finds them matches `smith\.md` and the `"implement",
"SKILL` spelling too. It named 69 modules at the first full run and 68 at
the close, because `tests/test_every_agent_reads_the_contract.py` stopped
naming the smith when its skip entry left; that module runs as a named extra.

**Two failures that might have predated part a (read, judged from the
diff).** `git diff --stat dc8991c2 e61ac4e1` changes `agents/smith.md` and
`skills/implement/SKILL.md` and nothing else.

- `test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`
  failed before part a. `git ls-tree dc8991c2` of this work item's directory
  lists `spec.md` and `plan.md` and no `overview.md`, so the case was red from
  the frame's commit on. This phase opened `overview.md` at its first
  divergence, as `skills/implement/SKILL.md` §3 says, and the case is green.
- `test_the_seal_is_taken_once_by_the_sealer.py::test_the_unmeasured_word_says_so_and_every_reader_is_told_it`
  did not fail before part a. It fails at its smith reader, which comes
  after the gate's constants and the sealer reader, both of which it passed.
  `agents/smith.md` at dc8991c2 carries `` `new?` is neither ``. The four
  readers after it are files part a did not touch, and each still carries its
  phrase. Part a's rewrite broke it, and the pin is re-pointed below.

**The verify skill's seal section needed a new title.** `## Removes` says the
section is rewritten to the fact. Its title, *Every agent seals what it
verified, and one of them is final*, states the fact being removed, so the
title changed. `agents/sealer.md` and `docs/one-root-by-lifetime.md` link to it
by title and were re-pointed in the same commit. Both files are outside the
frame's coordinates, and `overview.md` records the divergence. #969 edits
`agents/sealer.md` in its own worktree, so the two branches meet at line 29.

**`CLAUDE.md:69` still names *a seal block* as a format name.** Decision 1's
grep finds it, and a subagent does not edit `CLAUDE.md`. It is open in
`overview.md` with the owner as answerer. `skills/writing-style/SKILL.md:225`
still lists *the smith's seal* as an instance. That file is phase 3's, and the
grep does not find the row.

**One citation restored to the smith, and no rule.** Step 10 gained `(§3)` so
the declined-instruction line cites the rule it answers. Every rule
`test_the_smith_puts_both_answers_in_the_hand_back` reads still stands, so
re-pointing it alone would have lost the `§3` assertion. No rule part a
dropped needed restoring. `agents/smith.md` also had one line re-wrapped so
`` `new?` means nothing `` sits on one line, because the sealer module's
reader matches the raw file.

**`skills/implement/SKILL.md` had two lines over the wrap limit** once it
joined `COVERED`: line 18 at 108 columns and line 62 at 143, both from part a.
They are re-wrapped, and the byte count is unchanged.

### The pins (Q5), sorted

Each row is one case. *Rule* means the sentence it pinned is a rule that
stays, in the smith or in `implement`; *narration* means `## Removes` sends
the sentence away, or it was a copy of a rule that now lives in one place.

| Case | Rule or narration | Re-pointed to, or removed because |
|---|---|---|
| `test_a_moved_rule_leaves_its_definition.py::test_what_replaced_them_says_whose_the_act_is` | rule | re-pointed to the `## Never` lines *the routing batch was asked and written before you were spawned* and *`plan.md`'s approval line is the gate*; its owner-path half removed, since the rewrite names no owner file |
| `…::test_the_smith_stops_where_a_declared_frame_is_absent` | rule | step 4 *stop and hand that back* and the rule's *A missing `spec.md` is not evidence about the rung* |
| `…::test_a_citation_is_not_a_copy` (smith half) | narration, three phrases | the waiver example, the RIDER and the §8 pointer removed (`## Removes`, the RIDER block); *hand-back* kept and the waiver rule's *the last way past the gate and never the first* added. The docstring's 10-word measurement is re-stated: the widest kept run is now 8 words, `agents/framer.md` with §5 |
| `test_edits_go_through_the_edit_tool.py::test_the_implementer_keeps_the_half_that_makes_the_rule_its_own` | rule; its RIDER assert narration | the `## Never` line *Edit through the shell: no `sed -i`, no heredoc*; the `"RIDER"` assert removed (`## Removes`) |
| `test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py::test_the_smiths_definition_names_the_command_and_no_directory_to_clear` | rule | *Mutation-test every unit you added, one command each.* |
| `…::test_the_boundaries_bullet_says_the_command_holds_the_copy` | rule | the rule paragraph up to its `Enforced by:`, *`mutation-check` holds the bytes it read* |
| `…::test_the_default_bound_is_the_one_both_documents_state` | rule | *bounded at 300 s unless `--timeout`* |
| `test_a_probe_does_not_outlive_its_round.py::test_smith_commits_before_it_mutates` | rule | *restore from `mutation-check`'s copy* |
| `test_the_handoff_before_round_one.py::test_the_smiths_definition_mandates_mutating_every_unit_it_added` | rule | the lead *one command each* and step 6 *Commit, then run `mutation-check` over each unit you added.*, which carries the timing |
| `test_a_reference_root_is_read_and_never_taken.py::test_each_reader_says_when_it_reads_a_reference_root_and_where_it_cites_it` | rule | step 2 for read-and-cite; the never-write half read from the `## Never` line, which a definition in the warden's shape keeps there |
| `test_a_phase_hands_the_next_one_a_record.py::test_smith_is_told_to_write_the_phase_record` | rule | *Each phase closes with its record* |
| `test_chain_hooks_hardening.py::test_the_cycle_is_bounded_and_ends_at_a_pull_request` | rule | *The chain ends at a pull request, never a merge.* |
| `…::test_the_smith_says_whether_the_frame_holds_before_building_to_it` | rule; its anchor narration | step 3, placed between the requirements read and the build, and the rule paragraph's three destinations and *never back to the framer*; the `1. **Requirements**` anchor removed (`## Removes`) |
| `test_one_word_one_meaning.py::test_the_smith_calls_the_whole_thing_a_review_run` | rule | *bounded as `docs/the-review-record.md` §*The run* states* |
| `…::test_the_start_is_the_moment_before_the_first_edit` | narration | the smith entry removed: *before the first edit* stood in the design-gate narration |
| `…::test_the_owner_states_that_one_seal_is_final` | rule | verify's new sentence, *the one seal over the whole project is the sealer's `guarantee.md`* |
| `…::test_the_readme_says_whose_seal_the_warden_audits` | rule | renamed `test_the_readme_says_what_the_warden_audits`: *the warden's audit of the smith's labels* |
| `…#SEAL_BARE_IS_THE_CONCEPT` | narration, two allowances | `" block"` and `"'s `cost` row"` removed with the seal block they allowed |
| `test_a_segment_feeds_the_flow_log.py::test_the_section_exists_between_seal_block_and_counterfeits` | rule | renamed `…between_the_cost_of_a_repeat_and_counterfeits`; the neighbour above is `## The cost of the run you repeat` |
| `test_broad_gate_rule.py::test_the_smith_puts_both_answers_in_the_hand_back` | rule | step 10's wording; `(§3)` added to the smith, so the `§3` assert stands |
| `…::test_the_seal_block_asks_for_the_row_too` | narration | removed with the block (`## Removes`) |
| `…::test_the_seal_reports_what_the_checks_cost` | narration | removed with the block (`## Removes`) |
| `…::test_the_broad_gate_state_survives_a_handoff` (second half) | narration | the `broad gate:` row's assert removed with the block; the record half stays |
| `test_the_rules_have_one_owner.py` rule 10 | rule | re-worded to the new owner sentence; the sealer's link re-pointed to the retitled section |
| `…` rule 14, smith link | narration | removed: the smith's copy of the ladder left, and it reaches the rule through `implement` |
| `…` rule 15, smith link | narration | removed: the fix-pass changelog sentence is `implement` §5's, which keeps its link |
| `test_the_seal_is_taken_once_by_the_sealer.py::test_the_unmeasured_word_says_so_and_every_reader_is_told_it` (smith reader) | rule | *`new?` means nothing at the base measured that file* |
| `…::test_the_definition_separates_a_coverage_probe_from_a_seal[smith.md]` | rule | `PROBE` became one phrase per definition; the smith's is its coverage-probe sentence |
| `…::test_the_definition_names_the_sealer_as_the_suites_owner[smith.md]` | removed rule | removed with `OWNED`, `UNOWNED` and `OWNER_NAMED`: decision 6, the smith names no runner |
| `…::test_the_owner_is_named_once_in_each_definition[smith.md]` | removed rule | removed, as above |
| `…::test_the_smith_says_who_takes_the_gate_it_hands_to` | removed rule | replaced by T4 (decision 3) |
| `test_the_suite_has_a_command_that_is_cheap_twice.py::test_smith_finds_the_runner_before_inventing_a_command` | rule | *Find the runner, and type the narrow form.* and *run one module at a time*; `HANDOFF_LINK` unchanged |
| `test_waiver_decided_at_start.py::test_the_smith_carries_its_own_half_and_not_the_questions` | rule | the `## Never` line *Ask a person anything, or write `routing.md`*; *answerer* and the absence of the routing counts unchanged |
| `test_release_hygiene.py::test_the_release_target_is_asked_before_the_work_starts` (smith half) | narration | removed: the smith asks nothing and opens no pull request; its `## Unreleased` absence stays |
| `test_unverified_rows_close.py::test_the_ladder_does_not_still_say_at_the_end` (smith half) | narration | the presence of the ladder's copy became an absence of *`overview.md` at the end* |
| `test_the_contributor_has_a_procedure.py::test_each_history_sentence_still_stands[agents/smith.md]` | narration | the `RELEASE_BRANCH_HISTORY` entry removed with the RIDER's dated sentence (`## Removes`) |
| `test_the_set_a_work_item_always_has.py::test_the_top_rung_names_behaviour_rather_than_a_count` | rule; the smith's half narration | the condition read in the skill alone; the smith stays in the count sweep; its `KNOWN_PROSE` allowance and two `implement` allowances for sentences part a removed |
| `…::test_the_rung_gives_both_directions` | rule; one assert narration | the `warden-persona-accuracy` assert removed (`## Removes`) |
| `…::test_smith_and_the_skill_list_the_same_second_rung_work` | rule; the smith's half narration | renamed `test_the_skill_lists_the_second_rung_work_and_what_lifts_it`, the skill's half kept (`## Removes`: the copy leaves) |
| `…::test_what_the_status_column_gives_up_is_written_down` | the skill's half narration | the skill's assert removed (`## Removes`, `:408-422`); the planner's stays |
| `test_every_agent_reads_the_contract.py#NOT_YET_REWRITTEN` | — | the smith's entry deleted (`## Removes`) |

Counted from the table's 41 rows: 25 re-point at least one assertion of a
case that stays, and five of those also drop a part that pinned narration.
6 case ids leave: the two `[smith.md]` owner cases, the gate-owner case, the
two proof-block cases and the smith's history case. 9 rows only remove part
of a case, or an allowance, that stays, and 1 deletes the skip entry.

### The three new cases, each seen red

Each case went green on the tree first. Then `mutation-check` broke the
sentence its row names, and each run read `red: the cases failed against the
mutation (exit 1)` and exited 0 with the file restored. `git status` was
clean after each run.

| Case | Mutation | The assertion that went red |
|---|---|---|
| T3 `test_a_moved_rule_leaves_its_definition.py::test_the_smiths_four_rules_stand_with_their_enforcers` | the lead *Three failed fixes stop the work.* deleted | *lost the rule 'Three failed fixes stop the work.'* |
| T3 | the `Enforced by:` line under *A new test starts from its group.* deleted | *has no `Enforced by:` line* |
| T3 | the waiver's comma before *and it is* made a full stop | *the waiver is stated in more than one sentence again* |
| T4 `test_the_seal_is_taken_once_by_the_sealer.py::test_the_smith_names_no_runner_of_the_broad_gate` | *, and the sealer takes the broad gate once* added to the gate rule | *the smith's gate rule names ['sealer']* |
| T4 | *You do not run the full suite, the lint or the typecheck;* deleted | *the smith's gate rule stopped saying the run is not the smith's* |
| T4 | *and the orchestrator runs the broad gate first* added to the chain-ends rule | *hands the broad gate to somebody: ['orchestrator runs the broad gate']* |
| T5 `test_the_set_a_work_item_always_has.py::test_every_cited_heading_of_implement_exists` | `### 2.` retitled to *Implement test-first* | `CLAUDE.md`'s *§\*2. Implement test-first, and let each rule name its test\** dangling |
| T5 | `docs/the-record-layout.md`'s `§3's table` made `§7's table` | `§7` dangling |
| T1 `test_every_agent_reads_the_contract.py::test_every_definition_has_the_shape_and_preloads_the_contract_alone[agents/smith.md]` | `- implement` added to the smith's `skills:` | the shape case |
| T2 `…::test_every_file_a_step_names_exists[agents/smith.md]` | step 1's path made `skills/implements/SKILL.md` | the path case |

T5 recognises 18 citations in the tree today: 2 in `CLAUDE.md`, 15 by
number, and the contract's §11 by title.

### Sizes, recounted from the tree

| File | dc8991c2 | e61ac4e1 (part a) | aea8c8e5 |
|---|---|---|---|
| `agents/smith.md` | 20,829 | 10,004 | 9,993 |
| `skills/implement/SKILL.md` | 32,228 | 28,485 | 28,485 |
| `skills/verify/SKILL.md` | 55,892 | 55,892 | 53,920 |
| `README.md` | 52,730 | 52,730 | 52,500 |
| `README.ko.md` | 65,160 | 65,160 | 64,864 |
| `templates/sdd-overview.md` | 2,529 | 2,529 | 2,312 |

`bin/payload-meter --root <checkout> --agent smith` at aea8c8e5: total
39,982 B (12,495 tokens, estimated at 3.2 B/token), of which the agent share
is 26,664 B (`agents/smith.md` 9,993 and the contract 16,671) and the
`CLAUDE.md` pair 13,318 B. Phase 1 read 104,046 B total and 90,728 B agent
share at 2fc33333.

### Commands, each with its exit code

Read directly with `; echo $?`, never through a pipe. `<mods>` is the
modules `git grep -l -E 'agents/smith|smith\.md|implement/SKILL|"implement",
"SKILL|verify/SKILL|"verify", "SKILL|sdd-overview|session_cost|README' --
tests` names, plus `test_every_agent_reads_the_contract`,
`test_docs_line_wrap`, `test_one_word_one_meaning`,
`test_no_passage_is_pasted_into_a_second_file`, and at the close
`test_the_record_is_written_in_words` and
`test_a_question_says_who_can_answer_it`.

| Command | Exit |
|---|---|
| `bin/test` over the prompt's 65-module grep plus the first four extras, at e61ac4e1 | 1: 31 failed, 3620 passed, 11 skipped |
| `git diff --stat dc8991c2 e61ac4e1`; `git ls-tree --name-only dc8991c2 <work item>/` | 0, 0 |
| `bin/test <mods> -q`, 69 modules, before `overview.md` and the probe module's pin | 1: 2 failed, 3768 passed, 12 skipped |
| `bin/test <mods> -q`, 68 modules and six extras, at the close with `overview.md` and this record on disk | 0: 3770 passed, 12 skipped |
| `uvx ruff check` and `uvx ruff format --check` on the 23 changed `.py` files | 0, 0 |
| `bin/rules --check --root <checkout>` | 0: all 480 targets in 60 rule files resolve |
| `git grep -n -i "proof block\|seal block\|implement applied\|verify sealed" -- . ':!seal/specs' ':!changelog'` | 0: `CLAUDE.md:69` and two tests quoting history |
| `mutation-check` for T1, T2, T3 (3), T4 (3), T5 (2), `-p no:xdist` | 0 each, `red` each |
| `bin/payload-meter --root <checkout> --agent smith` | 0 |
| `bin/test tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -k durations` | 0: 2 passed, 1 skipped |
| `bin/unverified-check <checkout>` | 0: this item 4 open, 0 closed |

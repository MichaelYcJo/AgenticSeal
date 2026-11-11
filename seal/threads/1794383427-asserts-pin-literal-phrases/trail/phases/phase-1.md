# Phase 1: 1794383427-asserts-pin-literal-phrases

## What this phase found

**The frame holds against the tree at `17674989a`, except one sentence of
`frame/plan.md` *Technical context*.** *The listing* of `frame/design.md`
gives the same 189 asserts over the 30 modules of group A at `18a7e18fb`
as the design (executed). Each file the phase row names exists (read). The
sentence "It changes no script, hook, skill sentence or document" does not
hold for this phase. *Scope* item 7 rewrote the module docstring of
`.github/scripts/release_completeness_check.py`, which cited a case this
phase removed. *Scope* item 8 removed the `check:` line of
`skills/implement/SKILL.md` *2. Implement test-first, and let each rule
name its test* whose one case went. No rule sentence changed. The
sentence is the framer's to fold.

**S1, per module of group A.** The unit is one assert, a distinct
`path:line`. *The listing* prints one row per comparison, and an assert
that holds two comparisons prints two rows, so the listing's row count is
higher than its assert count for eight of the modules below. The base is
`18a7e18fb`, and the 189 add up as 106 kept, 70 removed and 13 not ruled
(executed: the ledger summed against the listing per module). The last
column is *The listing* at `755aa001f`. `bd7abc923` changed only a
docstring after it. That count differs from the kept count where a kept
assert was split in two, or where a loop over a variable replaced a
literal on the left, which *The listing* does not match.

| Module of `tests/text/` | Listed | Kept | Removed | Not ruled | Listed at `755aa001f` |
|---|---|---|---|---|---|
| `test_a_cited_commit_outlives_the_squash.py` | 1 | 0 | 0 | 1 | 1 |
| `test_a_document_has_room_for_the_next_fold.py` | 1 | 1 | 0 | 0 | 1 |
| `test_a_language_section_of_writing_style_opens_alone.py` | 3 | 3 | 0 | 0 | 3 |
| `test_a_merged_ticket_says_so_on_the_tracker.py` | 1 | 1 | 0 | 0 | 1 |
| `test_a_moved_rule_leaves_its_definition.py` | 6 | 5 | 1 | 0 | 5 |
| `test_a_parallel_agent_names_its_scratch_after_the_work_item.py` | 11 | 7 | 4 | 0 | 8 |
| `test_a_question_says_who_can_answer_it.py` | 2 | 2 | 0 | 0 | 2 |
| `test_a_release_cannot_ship_an_untrue_milestone.py` | 9 | 6 | 3 | 0 | 6 |
| `test_a_rider_reaches_its_file.py` | 12 | 2 | 10 | 0 | 2 |
| `test_a_segment_feeds_the_flow_log.py` | 25 | 9 | 16 | 0 | 9 |
| `test_broad_gate_rule.py` | 9 | 5 | 4 | 0 | 5 |
| `test_edits_go_through_the_edit_tool.py` | 3 | 2 | 1 | 0 | 2 |
| `test_every_agent_reads_the_contract.py` | 10 | 1 | 0 | 9 | 10 |
| `test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` | 6 | 3 | 3 | 0 | 2 |
| `test_no_passage_is_pasted_into_a_second_file.py` | 3 | 0 | 0 | 3 | 3 |
| `test_review_axes.py` | 6 | 4 | 2 | 0 | 5 |
| `test_settle_reads_before_it_removes.py` | 20 | 11 | 9 | 0 | 11 |
| `test_the_agent_contract_holds_the_universal_rules.py` | 3 | 3 | 0 | 0 | 3 |
| `test_the_chain_section_has_one_shape.py` | 3 | 3 | 0 | 0 | 3 |
| `test_the_direct_answer_owes_the_sealers_record.py` | 1 | 1 | 0 | 0 | 1 |
| `test_the_gate_hands_cmd_a_path_it_can_run.py` | 2 | 0 | 2 | 0 | 0 |
| `test_the_handoff_before_round_one.py` | 5 | 5 | 0 | 0 | 5 |
| `test_the_mode_is_a_row_and_a_command.py` | 9 | 5 | 4 | 0 | 5 |
| `test_the_record_is_written_in_words.py` | 2 | 2 | 0 | 0 | 2 |
| `test_the_records_can_be_carried_out_and_in.py` | 5 | 4 | 1 | 0 | 4 |
| `test_the_release_table_reads_two_trees_and_fails_nothing.py` | 7 | 6 | 1 | 0 | 6 |
| `test_the_release_tail_does_not_end_at_the_tag.py` | 6 | 5 | 1 | 0 | 5 |
| `test_the_rules_have_one_owner.py` | 7 | 3 | 4 | 0 | 3 |
| `test_the_settings_have_a_front_door.py` | 10 | 7 | 3 | 0 | 7 |
| `test_the_suite_runs_with_gh_logged_out.py` | 1 | 0 | 1 | 0 | 0 |
| Total | 189 | 106 | 70 | 13 | 120 |

The 13 not ruled read a program's output or a text the case built. In
`test_a_cited_commit_outlives_the_squash.py` that is the reason
`verdict()` returns. In `test_every_agent_reads_the_contract.py` it is the
output of `shape_problems()`. In
`test_no_passage_is_pasted_into_a_second_file.py` it is the messages of
`shared_runs()` (read).

**Asserts outside the listing were ruled as well.** Each case that holds a
listed assert was read whole, as `frame/design.md` *The criterion* asks.
Its other asserts on file text were ruled the same way, the loop tuples
among them. Those are not in the counts above. Examples are the 12-clause
loop of the fix-pass case in `test_the_rules_have_one_owner.py`, cut to
four facts; the 16-sentence loop of the `cmd.exe` case, cut to two; and
the `BY_HAND` absence of `test_broad_gate_rule.py`, removed.

**Six kinds of decision recur, each judged against `frame/design.md` *The
criterion*.**

- A literal that is a fact is kept and cut to the fact, with a comment
  directly above it that names the fact and its reader. Examples are a
  path, a command, a flag, a citation by path and italic heading, a
  workflow key and its value, and a spelling a script matches. An assert
  that already carries #1233's comment stays as it stands. In
  `test_the_chain_section_has_one_shape.py` the diff is empty (executed,
  `git diff`).
- A literal that is a sentence or a word of a sentence is removed.
  Examples are "share one scratchpad", "scratch fixture", "owner", "counted,
  not estimated" and "no-op".
- An absence assert is kept only where a rule in force forbids its literal
  and the rule can be cited. One stands:
  `disable-model-invocation: true` in
  `test_the_agent_contract_holds_the_universal_rules.py`. Its comment cites
  `docs/running/the-agent-set.md` *One contract every agent receives, and
  one definition each*. Every other absence of group A held text or a
  design a shipped release removed, or a literal no rule in force names, and
  is removed. Examples are `rm -rf` in an agent definition, `<!--` in
  `skills/verify/orchestration.md`, `--preflight` in `agents/sealer.md`,
  `git archive` in the release-report job, `#81` in the READMEs,
  `/tmp/run.txt` in `skills/verify/SKILL.md` and `` `\|` `` in the
  settings door.
- Two of the three shapes that always count as wording occur in group A,
  and are removed. One is an assert that a check line naming the
  asserting module stands, the three-fix case's `^check:` search. The other is an assert that the same
  sentence stands in two files, the case that held the release script's
  docstring and a case's docstring to each other. No assert of group A
  only locates the text a removed assert read.
- A case left with no assert is removed, together with the helpers only it
  used (*Scope* item 6). Sixteen cases went:
  `test_the_three_fix_rule_stands_in_the_skill_a_builder_opens`,
  `test_no_contract_section_or_definition_writes_a_removal`,
  `test_the_script_and_this_file_draw_the_input_boundary_the_same_way`,
  three cases of `test_a_rider_reaches_its_file.py` (the stamp and checker,
  the condition, the overturn), six of `test_a_segment_feeds_the_flow_log.py`
  (the HTML comments, the no-op, the asking, the two logs' separation, the
  opening sentence, the tracker state),
  `test_no_definition_promises_the_suite_once_the_rounds_settle`,
  `test_the_order_no_longer_defers_the_framer_to_a_ticket`,
  `test_the_template_says_an_absent_mode_key_stops_nothing` and
  `test_the_door_gives_a_language_row_no_default`. The helpers that went
  with them are `FIX_PASS_READERS`, `THE_FORMS_OWN`, `AGENTS`, `SCRIPT` in
  two modules, `read_at`, `BY_HAND`, `STEP_2` and `LANGUAGE_ROWS` in
  `test_the_settings_have_a_front_door.py`, with the imports that only
  they used. The `LANGUAGE_ROWS` of
  `tests/behaviour/test_first_setup_asks_once.py` is a constant of its own
  and stands.
- A case whose name stated what a removed assert read is renamed for what
  it still reads. Six cases were renamed:
  `test_the_example_row_goes_lint_first_and_the_prose_cites_the_arms_list`,
  `test_the_broad_gate_section_names_the_preflight`,
  `test_the_local_mode_section_names_what_a_local_settle_reads`,
  `test_the_template_shows_the_rewrite_and_the_form_that_keeps_a_switch`,
  `test_the_listing_s_hold_carries_its_date_and_the_branch_it_leaves_running`
  and `test_a_rider_waiting_on_a_held_file_names_who_answers_it`. No file
  outside `seal/threads/` and `.test_durations` names an old name (S5,
  below).

**Five literals could be read either way, and the proofer reads each
against *The criterion* (S2).**

- The three-fix rule's lead in `skills/implement/SKILL.md` holds the
  number three. It was ruled the paragraph's lead sentence, which is
  wording, and the case went with its only other assert, the check-line
  search.
- The release script's five environment names were asserted in two texts,
  its docstring and a case's docstring. That was ruled the shape "the same
  sentence stands in two files". The step that hands the five to the
  script is still asserted key by key in
  `test_every_input_the_script_reads_is_handed_to_it_by_the_step`.
- `rm -rf` absent from the contract and every agent definition was
  removed. Contract rule 21 now allows `rm` on a literal path, and #1503
  removed the design the absence held. No rule in force forbids the
  literal in a definition, so no rule can be cited.
- `disable-model-invocation: true` absent from the contract's front matter
  was kept. The flag blocks the preload that
  `docs/running/the-agent-set.md` *One contract every agent receives, and
  one definition each* requires.
- "owner" in the listing's hold sentence of
  `docs/releasing/branch-and-release.md` *Cutting a release* was removed as
  a word of a sentence. #1490 had mutation-tested it as a guard, which
  `seal/threads/1794271935-the-releasing-documents-describe-the-note-twice/trail/phases/phase-1.md`
  records. The date and `` `dist` `` stay.

**Docstrings and comments outside group A were rewritten under *Scope*
item 7.** Each cited a removed unit or stated what one pinned:

- `.github/scripts/release_completeness_check.py`'s module docstring no
  longer says a sibling case holds its paragraph to a case's docstring.
- `tests/behaviour/test_a_release_rolls_the_flow_measurement_issue.py`'s
  module docstring and one assert message no longer cite
  `test_the_shipped_skill_names_no_repository_specific_tracker_state`.
- The comment above `assert SHAPE in flat(skill)` in
  `tests/behaviour/test_waiver_decided_at_start.py` no longer says
  `tests/text/test_review_axes.py` reads the same spelling.

The docstring of
`test_the_location_buckets_are_the_repositorys_own_definition_of_a_record`
was rewritten in `bd7abc923` after the range was read whole. Its ledger
and share-row asserts are gone, so it now says the case reads the record
path the `Location` row names.

**One check line outside `docs/` was edited, under *Scope* item 8.** The
`check: tests/text/test_a_moved_rule_leaves_its_definition.py` line after
the paragraph **Three failed fixes stop the work.** of
`skills/implement/SKILL.md` was removed. Its one case was removed. No other
check line in `RULE_FILES` lost its last reader. `seal rules --check`
holds every line (executed, S4 below), and each check line naming a module
of group A was read against the cases that stand (read).

**One check line under `docs/` names a module that no longer reads its
rule, under *Scope* item 9.** It is
`docs/forms/the-round-record.md:107`, after **Each finding's close block
has one writer, and the blocks written at one step reach the branch in a
single commit.** It names `tests/text/test_the_rules_have_one_owner.py` and
`tests/text/test_a_moved_rule_leaves_its_definition.py`. The second module
read the rule through the fix-pass file's sentence "Last, after its last
fix commit and its corrections, the fix pass appends the close block of
every finding it answered, and commits none of them", and that clause is
removed. The first module still reads the rule, in its `RULES` row 19 "the
orchestrator writes no close block of a finding a fix pass answers"
(read). So the line keeps a reader. Whether the line drops the second name
is the framer's to fold. No check line under `docs/` lost its last reader
in this phase (read).

**One stale statement was found outside the range and left.** The module
docstring of `tests/text/test_the_chain_section_has_one_shape.py` says
`tests/text/test_a_segment_feeds_the_flow_log.py` pins
"`skills/verify/SKILL.md`'s measurement section". The section has stood in
`skills/verify/orchestration.md` since #940. The statement predates this
work and cites no unit this phase removed, so it is not a *Scope* item 7
rewrite. It is handed back for the orchestrator.

**What was run, and what each run showed.**

- S1: executed, as above.
- S4: `bin/seal rules --check` exits 0, "all 178 check lines in 69 rule
  files hold." (executed at `bd7abc923` with this record in the tree).
- S5: `git grep -n -w <name> -- . ':!seal/threads' ':!.test_durations'`
  over each removed case, each removed helper and each old case name lists
  nothing (executed at `bd7abc923`).
- S9: the edited modules gave 411 passed at `755aa001f` (executed). The
  boundary set, `bin/test tests/text tests/behaviour
  tests/github/test_rules.py tests/github/test_release_completeness_check.py
  tests/skills/test_passages.py -q`, gave 1975 passed and 8 skipped at
  `bd7abc923` with this record and `gaps.md` in the tree (executed). At
  `755aa001f`, before `gaps.md` existed, one case failed:
  `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
  which asks a work item with a phase commit for its `gaps.md`.
- Mutation: `seal mutate` over five kept literals, each in the document the
  literal pins, each with the module's cases, went red. The literals were
  `xcopy /e` and `bin\test` in `templates/setup/config.md`, `seal export`
  and `lib/routing.py` in `skills/settle/local-mode.md`, `contract rule 11`
  in `skills/implement/fix-pass.md`, `loop_pairs` in `CONTRIBUTING.md`, and
  `-2` in `skills/agent-contract/SKILL.md`. The tree was clean after each
  restore (executed, `git status --short`). The other cut literals were
  read, not mutated: each still stands in the text the case cuts, and the
  case's message names it.
- S2 and S3 are the proofer's at review.

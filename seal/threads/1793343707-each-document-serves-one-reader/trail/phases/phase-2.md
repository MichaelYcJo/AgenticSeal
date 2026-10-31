# Phase 2: 1793343707-each-document-serves-one-reader

## What this phase found

**The frame held at the coordinates row 2 names, and missed six.** Each
was found by reading the named lines and then running `git grep` on the
removed words outside `seal/threads/`. Each was built as below.

- `tests/behaviour/test_the_set_a_work_item_always_has.py` had a third
  approval-line case,
  `test_the_orchestrator_states_the_approval_line_where_it_spawns_the_build`.
  It compares the line fenced in `skills/implement/orchestration.md` *The
  plan is approved at the spawn* with the template's line, through
  `stamp_line`, which asserts that the template has exactly one. So it
  cannot pass once the template's line goes. It was removed with the two
  cases the row names. Its other pins were that section and
  `skills/code-review/orchestration.md:167`, and phase 4 rewrites both.
  This is a removal `## Removes` did not name.
- The same module's `test_the_file_set_names_who_writes_each_file`
  asserted that the plan row's Holds cell names `Approved <date> by <who>`.
  It now asserts "approved by the spawn that builds it", and that the
  `gaps.md` row's When cell gives the first phase's close.
- `templates/setup/seal-README.md` carries the same layout line as
  `seal/README.md`, and `tests/behaviour/test_first_setup_asks_once.py`
  holds the two files equal. Both now read "what one build phase found".
- `skills/implement/SKILL.md:111` read "one build phase's record", not
  "what one build phase was asked and found" as `## Removes` quotes it. It
  now reads "what one build phase found", like the other three layout
  lines.
- `skills/implement/SKILL.md:335` said that a `the work` question is
  decided by the phase that meets it, which "records a divergence row".
  That row was `gaps.md`'s divergence table. The sentence now says the
  phase records the decision in its phase record.
- `tests/skills/test_pr_body.py` has a case that expects a duplicate
  `## Phases` heading in the plan fixture at line 20. The fixture lost six
  lines (the approval line, `## Summary` and their blanks), so the heading
  is now at line 14. The first boundary run found it.

**The eval scaffolds come from one generator.** The eleven changed
`evals/behaviour/*/scaffold.sh` files are the output of
`evals/scripts/rule_cases.py`, which was edited and run (exit 0). Its
`OVERVIEW`, `one_phase_plan` and `SEALER_PHASE` now write the new shapes.
The phase record no longer holds the build commit, so the sealer cases
fill it only into `round-1.md`. The five `shape-phase-record` graders are
`file_exists` checks, and the rename case's `shape-proved-by` reads a case
name. None of them names a section, so none changed (read).

**Some sentences still state the old facts, each on purpose.**

- `skills/implement/orchestration.md:33`, `:49`, `:80`, `:89`, `:268` and
  `:463` still name the approval line. Row 4 rewrites each of them. Until
  phase 4, that file describes a line the template no longer has. No case
  reads that section now that the third case is gone.
- `skills/implement/SKILL.md:76` ("A human approves `frame/plan.md`") and
  `:301` ("approval of `plan.md` IS the gate") name no line. Reading the
  plan and spawning the build is still an approval, so both hold.
- `docs/the-reader-registry.md` still sends an unnamed removal to
  `gaps.md`, and
  `test_a_phase_record_carries_no_removal_table` still pins that sentence.
  A pull request does not edit the policy root. The design's
  `## Rule changes` holds the new sentence, and the settle writes it.
- `tests/skills/test_unverified_check.py:1352` and `:1360` write
  `## Fed back into the spec` as the section that follows
  `## Not verified`. Any heading would serve there. The docstring at
  `tests/text/test_a_segment_feeds_the_flow_log.py:495` cites a past work
  item's divergence section as history. All three were left as they stand.
- This work item's `frame/plan.md` keeps its `Approved` line at line 3, as
  history, as row 2 says.

**Two wordings were chosen here, under `automation`.** The crafter's rule
now opens **A stop at three failed fixes is handed back.** That way the
definition does not carry the lead it moved to the skill. The skill's
sentence says "the next step is the architecture question, not a fourth
fix", where the crafter's said "hand back". A session that builds has
nobody to hand back to.

**Nine cases were rewritten or added, and each was seen red first.** They
were run against `195b452f` with only the four test modules changed:
exit 1, `9 failed, 1 passed`. The one that passed was
`test_the_found_section_ships_a_placeholder`, which held before too, since
the old template already had that placeholder. The nine:

- `test_a_phase_hands_the_next_one_a_record.py`:
  `test_the_template_is_its_title_and_the_found_section`,
  `test_crafter_is_told_to_write_the_phase_record` (the departure clauses),
  and `test_the_skill_says_the_record_copies_neither_the_ask_nor_the_commit`.
- `test_unverified_rows_close.py`:
  `test_the_memo_holds_what_went_out_unproved_and_what_was_not_taken` and
  `test_the_ladder_does_not_still_say_at_the_end` (the one trigger).
- `test_the_set_a_work_item_always_has.py`:
  `test_the_file_set_names_who_writes_each_file`.
- `test_a_moved_rule_leaves_its_definition.py`:
  `test_what_replaced_them_says_whose_the_act_is`,
  `test_the_crafters_four_rules_stand_with_their_enforcers` (its three-fix
  entry) and the new `test_the_three_fix_rule_stands_in_the_skill_a_builder_opens`.

After the edits, the four modules passed: exit 0, `285 passed` (executed).

**All eleven mutants went red** (executed, `seal mutate` at `fcacd9e5`).
Each run exited 0 and printed "red: the cases failed against the mutation
(exit 1)". The tree was clean after the last run. Each mutant broke one
unit:

- the phase template's heading;
- the gaps template's `## Not done`;
- "Two things go in it";
- the `gaps.md` row's trigger;
- "approved by the spawn that builds it";
- the three-fix rule's bold lead in the skill;
- "the orchestrator folds into the plan before the spawn";
- "the spawn is the gate";
- the crafter's three-fix lead;
- the departure clause of *Each phase closes with its record*;
- the crafter's `gaps.md` trigger.

The removed lines (the plan's approval line and the six template
sections) add no behaviour. The template-shape cases above cover them.

**The phase-boundary set is 83 modules, run as one command.** It is the
twelve modules row 2 names, plus `test_first_setup_asks_once.py`, plus
every module that names a changed path, plus every module that globs
`agents/`, `templates/`, `skills/`, `evals/` or `seal/threads/`. The first
run gave exit 1, `1 failed, 4170 passed`: the line number above. After the
fix, at `fcacd9e5`, it gave exit 0, `4171 passed, 9 skipped` (executed).
`ruff check` and `ruff format --check` passed over the seven changed
Python files (executed).

**`gaps.md` now follows the new template.** It has no
`## Scope confirmation`, because this work is on the ladder's top rung.
`## Not verified` keeps its one row, the broad gate, answered by the
orchestrator, and `## Not done` reads `nothing`. `seal unverified` reads it
as `1 open · 0 closed`, exit 0 (executed).

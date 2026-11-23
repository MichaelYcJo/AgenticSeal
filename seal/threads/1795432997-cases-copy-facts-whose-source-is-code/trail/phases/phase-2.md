# Phase 2: 1795432997-cases-copy-facts-whose-source-is-code

## What this phase found

**The frame holds for this phase.** At `404fb7246`, S6, S7 and S8 of `frame/design.md` printed one line for each copy that *Scope* items 5 to 8 name, and no other line (executed). The constants that G12 and G13 name stand where those rows put them, and so do `pr_wait.py#STATES` and `#MERGEABLE` (read). `tests/skills/test_chain_check.py` and `tests/skills/test_broad_gate.py` load their scripts through `tests/conftest.py#load_module`, so this phase loads `chain_check.py`, `broad_gate.py` and `pr_wait.py` the same way, and `lib/routing.py` and `lib/fields.py` through `load_lib_module`, as `frame/plan.md` *Technical context* says. `seal/follow-up.md` holds two rows, and neither waits on this phase.

**Decisions settled while writing the code.** Each was judged against `frame/design.md` *Scope* items 5 to 8 and `skills/core/SKILL.md` *The rule a mechanism is kept against*. The rule's words are: a fact has one source, and every other place links to it.

- `tests/behaviour/test_waiver_decided_at_start.py` loads `lib/routing.py` and `chain_check.py` once, at module level. `or_joined(answers)` builds a row's offered answers, such as `` `crafter` or `the session` ``. The module already defines `offered(template, label)` for the template's placeholders, so the new helper takes another name. The Planning case's box check reads `routing.BY_FRAMER` and `routing.PLANNING` as well as the row, because *Scope* item 5 says the row label is built from its constants. The comment on why `AXES` leaves out `crafter` stays.
- The four template cases of that module still put `lib/` on `sys.path` and `import routing` inside the case. They parse the template through `routing.parse`, which is that module either way. Moving them onto the module-level loader is a refactor no *Scope* item names, so they stand (`gaps.md` `## Not done`).
- `tests/text/test_review_axes.py#test_the_routing_section_holds_the_answers_and_the_shape` goes, as *Removes* says. It also checked that `skills/implement/routing-question.md` spells `` `manual` `` as a code span. `#test_question_1_lists_the_four_modes_in_the_owners_order` holds that question 1 offers `manual`, by the table's label cell with its bold taken off. So the fact that question 1 offers the mode is still held. The code-span spelling of `manual` in that file is held by no case now. The module's `No TARGET` line no longer says it holds how the work is routed or reads the implement skill's orchestrator files, since no case of it reads them now.
- In `tests/text/test_the_rules_have_one_owner.py`, the wait case names the conflict cell's `mergeable` value through `getattr(wait, value)` over `pr_wait.py#MERGEABLE`. The module names that exit code after the value, `CONFLICTING`, so the value whose attribute is that code is the one the code answers. No constant of `pr_wait.py` maps the code to the value: `:315` compares with a literal. Row 27 reads `new?` as the first word of `broad_gate.py#NOT_MEASURED`, `new? not measured`, the word `skills/verify/orchestration.md` bolds.
- `tests/text/test_a_language_section_of_writing_style_opens_alone.py` asserts `len(checks) == 1`, where the snapshot asserted the line byte for byte.
- In `tests/text/test_a_moved_rule_leaves_its_definition.py`, `test_a_citation_is_not_a_copy` keeps the proofer's two phrases. The crafter's entry held no phrase and fed only the copy loop, so it goes with the loop. The module's imports of `glob`, `pytest`, `load_module`, `repo_relative` and `HEADING`, `AGENTS` and the `WINDOW` load went with the cases that used them. The comment over the routing-batch case said "Above, a rule moved into the contract", and now opens on the routing batch itself.
- The measurement moves into the comment over `skills/settle/scripts/passages.py#WINDOW`. It holds both ends and the pairs that gave them, and says that no case keeps those ends. The paste test's docstring cites that comment, and its *What it does not catch* now names a passage shorter than `WINDOW` words. `frame/design.md` *Removes* says that docstring states this, and before this phase it did not.

**Item 11: the prose that stood on what this phase removed.** `git grep` on `test_a_moved_rule_leaves_its_definition`, `LONGEST_KEPT`, `SMALLEST_REAL`, `806,241`, `WRITING_RULE_CHECKS`, `Rule 18` and the removed case names, outside `seal/threads/` (executed). The rewritten sentences:

| File | What it said | What it says now |
|---|---|---|
| `tests/text/test_broad_gate_rule.py`, docstring | the moved-rule module holds the duplication check | the paste test refuses a moved rule pasted back |
| `tests/text/test_edits_go_through_the_edit_tool.py`, docstring | the moved-rule module refuses the copy | the paste test refuses it |
| `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py`, docstring | the moved-rule module states the verbatim limit | the paste test states it, in *What it does not catch* |
| `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:1055`, comment | the moved-rule module holds that no definition kept a copy | the paste test holds it |
| `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:373`, comment | the moved-rule module exists to refuse the duplication | the paste test does |
| `tests/skills/test_passages.py`, docstring | the measurement stands in the moved-rule module | it stands in the comment over `WINDOW` |
| `tests/text/test_the_rules_have_one_owner.py#test_the_fix_pass_reads_the_implementers_context_before_it_resumes`, docstring | "Rule 18 holds the threshold" | the threshold is a measurement no code reads, whose one home is the section |

Two `check:` lines name the moved-rule module: `docs/forms/the-round-record.md:107` and `skills/implement/fix-pass.md:70`. They stand. Their rules are held by `#test_the_fix_pass_follows_its_own_file_and_the_form_states_the_close_block`, which this phase keeps (`frame/design.md` G2). That list is a sample (contract rule 12): it is the spellings searched, and a sentence that paraphrases the old fact without naming the module or a constant is not reached. It stands in the tree's other prose, which the review rounds read.

**The removed window cases, and what holds their pairs now.** The probe `phase-2/test_tmp_paste_test_holds_the_pairs.py`, under this work item's scratch directory, cut the contract into its 18 numbered rules by `HEADING`, as the removed `sections` did. It pasted each rule whole into each of the 5 agent definitions under a new heading, as the removed `paste_back` did. Then it asked the paste test's `shared_counts` whether the pair of the contract and that definition gained a run. It printed `rules 18, definitions 5, caught 90, missed 0` (executed, at `eb347e432`'s working tree before `d5b667723`, whose only change is a docstring wrap). Every rule of the contract today is at least `WINDOW` words long, so none falls under the limit the paste test's docstring now states.

**The values built from code equal the literals they replace.** The probe `phase-2/test_tmp_built_equals_old.py` imported both modules before item 6 was committed. It asserted that each built value equals the old literal: `AXES`, the three `or_joined` rows, the trailer, the routing path, the row labels, rows 21 and 27, `LINE_KEYWORDS` and the seven exit-code cells. It printed `all equal` (executed). So every converted case reads the same text it read before, and S9's comparison table has no row for this phase.

**Each converted assertion can still fail: `seal mutate`.** Each break edited one document or one constant, and the run took only the one case that reads it, with `-p no:xdist`. Every verdict below was `red`, exit 0, and each failing line was read for the assertion it breaks (executed; logs under `phase-2/mutate/`):

| Break | Case that went red |
|---|---|
| `skills/implement/orchestration.md`: `` `crafter` or `the session` `` to `` `the agent` `` | `test_waiver_decided_at_start.py#test_the_implementation_row_offers_the_answers_the_parser_reads` |
| same file: `\| Automation \|` to `\| Automaton \|` | `#test_the_section_gives_the_automation_row_its_two_answers`, on the row count |
| same file: the Automation row's `` `no` `` to `` `never` `` | the same case, on `or_joined(('yes', 'no'))` |
| same file: `` `framer` or `the session` `` to `` `the agent` `` | `#test_the_planning_row_is_a_record_and_not_a_checkbox` |
| same file: `.../routing.md` to `.../route.md` | `#test_the_skill_names_where_the_answer_is_written` |
| `skills/implement/routing-question.md`: the trailer's value to `none` | `#test_the_routing_question_names_the_trailer_that_records_no_work_item` |
| `docs/running/the-review-and-parity-arms.md`: the table's `straight to the PR` key | `#test_the_policy_tables_the_review_answers_and_the_skill_cites_it` |
| `lib/routing.py`: `STOP_BEFORE_PR`'s value | `#test_the_orchestration_offers_the_vocabulary_the_parser_accepts` |
| `skills/legacy-parity/SKILL.md`: `\| straight to the PR \|` | `test_review_axes.py#test_the_record_of_a_comparison_names_its_writer` |
| `skills/commit-pr-convention/SKILL.md`: `through the review chain` | `test_the_chain_section_has_one_shape.py#test_the_section_names_the_routing_answer_it_holds_for` |
| `chain_check.py`: `NO_WORK_ITEM`'s value | `test_settle_reads_before_it_removes.py#test_the_skill_names_how_a_settle_commits` |
| `skills/code-review/SKILL.md`: `` `fixed <commit>` `` | `test_the_rules_have_one_owner.py#test_the_owner_states_the_rule[21 ...]` |
| `skills/verify/orchestration.md`: `` **`new?`** ``, then `` **`failing on base too`** `` | `#test_the_owner_states_the_rule[27 ...]`, once each |
| `skills/code-review/gate-to-pull-request.md`: the code 6 row's `CONFLICTING`, then code 4's `MERGED`, then `\| 2 \|` | `#test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge`, once each |
| `skills/code-review/SKILL.md`: the sentence's `` `reopens:` `` to `` `resumes:` `` | `#test_a_close_that_does_not_hold_reopens_it`, naming that sentence |
| `skills/writing-style/SKILL.md`: the `check: ` prefix taken off the line | `test_a_language_section_of_writing_style_opens_alone.py#test_the_rules_for_text_an_agent_or_a_check_reads_reach_both_languages`, on `0 == 1` |

One break read `SURVIVED`, exit 1. It edited the Destination row's `` `stop before the pull request` `` in `skills/implement/orchestration.md`. That file spells the answer twice, at `:267` and `:322`, and the case asks that the file names it, which the other spelling still does. The case is right, and the break was the wrong one for it. Breaking `lib/routing.py#STOP_BEFORE_PR` instead turned it red, which is the row above. One stray command, `bin/seal mutate code-review-placeholder`, named no file and no `--replace`, so it wrote nothing. `git status` was clean after every run (executed). No case of this phase is new, and no unit outside `tests/` adds behaviour: `passages.py` changed only a comment, so it owes no run of its own (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*). The runs above show that each rewritten assertion still fails when the fact it holds is broken.

**The census.** At `eb347e432`, S6, S7 and S8 print nothing, each `git grep` exiting 1 (executed). The same searches printed the lines listed above at `404fb7246`. Outside `seal/threads/`, nothing prints for `git grep` on the removed cases' names, on `` test_a_moved_rule_leaves_its_definition.py`'s `` and on `agentic_passages_for_the_moved_rule_check` (executed). `bin/seal layout --check` exits 0: 140 files read, 0 refused (executed).

**For the next phase.** Phase 3 rewrites `tests/evals/test_rule_cases.py:3-5` and the eval readers. Nothing this phase changed stands in those files.

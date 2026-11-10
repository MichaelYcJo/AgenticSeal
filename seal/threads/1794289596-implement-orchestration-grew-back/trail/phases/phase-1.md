# Phase 1: 1794289596-implement-orchestration-grew-back

## What this phase found

**The frame holds against the tree, with five exceptions.** The frame names `9e9d1087f`, and the two commits after it change only the frame files, so each coordinate of `skills/implement/orchestration.md` it gives stood when this phase started. I opened every range `frame/design.md` *Removes* rows 1 to 7 and 15 name, and each begins and ends where the row says. The exceptions follow, each with what this phase did about it.

**Exception 1: the two files cannot say the opening condition in the same words.** `frame/design.md` D4 and S4 ask the body's sentence and the new file's first paragraph to say the same condition, and S4 fixes the body's words as D4's. With D4's words in both places, `tests/text/test_no_passage_is_pasted_into_a_second_file.py::test_no_pair_of_rule_documents_shares_a_run` went red (executed): `skills/implement/orchestration.md` and `skills/implement/routing-question.md` shared a run of 38 words, and the check refuses 15. The check holds a policy rule, `docs/layout/the-record-layout.md`, which outranks the frame (`skills/implement/SKILL.md` *1. Read the documents that outrank the code first*). So the body carries D4's words, and the first paragraph of `routing-question.md` states the same two conditions in other words. `merge-order.md` shares no run of 15 words with the body, and its first paragraph keeps D4's two clauses.

**Exception 2: three moved sentences changed, and two of the changed pointers carried no "above" or "below".** `frame/design.md` *Scope* item 1 and S5 allow a change only where a sentence points by "above" or "below". A citation that names a section of the same file by its bare heading is the same class: it resolves in the file it stood in and not in the file it moved to. The three changed sentences, each now citing `skills/implement/orchestration.md` by path:

- `routing-question.md`, the lead of *Orchestrator: why the routing question is asked once, at the start*: `*Orchestrator: what needs a person is asked in one batch, before the first edit* above`.
- `routing-question.md`, **Question 1 is put every time**: `*Orchestrator: when a work item is required* below` and the bare `(*Under agentic*)`, which now reads `(its *Under agentic*)`.
- `merge-order.md`: the bare `*Orchestrator: the order inside a ticket*`.

`merge-order.md` also ends at "the verifying round it owes.", where the body's line went on with the next sentence. I compared every other moved paragraph with its landing text, flattened, by a script over the ranges of `9e9d1087f` (executed): no other paragraph differs, and none stands in the body still.

**Exception 3: two sentences outside `frame/design.md` G12 cited the old homes.** *Scope* item 7 names four files. Two more statements went inexact with the move, and this phase changed both, because G4 puts every file outside the policy root in the pull request:

- `skills/implement/bootstrap.md`, the paragraph opening "Ask only here", cited the batch section for the two language keys. It now cites `skills/implement/routing-question.md` *The two language keys join the batch wherever either is missing*, as `skills/commit-pr-convention/SKILL.md` does.
- The docstring of `tests/behaviour/test_the_set_a_work_item_always_has.py#test_the_plan_template_carries_the_overlap_table` cited the routing section for the merge order. It now cites `skills/implement/merge-order.md` *Orchestrator: the order the work items of a release merge in*.

I found them by `git grep` on the two section names, each also cut at its line wraps, and on eleven phrases of the moved passages. That list is a sample: the statements of where a passage stands are an open class. Three statements I read and left, because each still holds: `docs/releasing/branch-and-release.md:41` cites the routing section for the choice of the item that carries the move, a sentence the body keeps; `skills/implement/bootstrap.md:7` sends the orchestrator back to `skills/implement/orchestration.md` for the routing question, and the body's routing section now opens with the sentence that names the file; `docs/running/the-review-and-parity-arms.md:56` is the citation `frame/design.md` *Rule changes* carries.

**Exception 4: two more cases read the moved passages than `frame/design.md` G15 and `frame/plan.md` *Technical context* list.** Both stand in `tests/behaviour/test_waiver_decided_at_start.py`:

- `test_the_skill_names_the_record_and_no_per_command_waiver` reads `` `Seal-Routing: no work item` ``, which the body held only in the cell of question 1's exit. `tests/text/test_review_axes.py#test_the_routing_section_holds_the_answers_and_the_shape` reads the same phrase, so that case reads four moved phrases and not two leads.
- `test_the_planning_row_is_a_record_and_not_a_checkbox` reads every table of boxes through `checkbox_tables` and asserts that none holds a `Planning` box. After the move the body holds no table of boxes, so the loop ran over nothing and the case stayed green. No run would have shown it. The case now reads the tables in `routing-question.md` and asserts that it found one. The `Planning` row it also reads stays in the body.

**Exception 5: `frame/design.md:16` cites a commit no release ref holds.** `tests/text/test_a_cited_commit_outlives_the_squash.py::test_every_cited_commit_outlives_the_squash` is red at this phase's commit (executed) on `5656e5239`, which G8 cites with a path. `git branch -a --contains 5656e5239` names only `fix/1445-agents-write-commands-the-parser-reads` and its remote (executed). The line is the framer's, and this phase changed no line of the frame before its Status cell, so the case reads the same line at the frame's commit (read, not run there). It stays red until the frame cites something `main` or a release branch holds.

**Each re-pointed case was seen red with its sentence gone from the new file (executed, at `4112c5924`).** Each run is one `seal mutate` of `skills/implement/routing-question.md` over the one case, and each read `red`, exit 0. I read each failing line for the sentence it names.

| Case | Text replaced in the file | Failing line |
|---|---|---|
| `test_question_1_is_asked_alone_and_the_boxes_only_under_per_axis` | the lead **Ask question 1 alone; …** | `assert SHAPE in flat(skill)` |
| `test_question_1_is_put_every_time_with_the_ladders_answer_marked` | `` ` (Recommended)` after the label `` | "The mark is ` (Recommended)` after the label" |
| `test_question_1_lists_the_four_modes_in_the_owners_order` | the sentence on `direct` in `agentic`'s cell | "`agentic`'s description does not say it may choose `direct`" |
| `test_the_boxes_are_in_the_stated_order` | box 2's label | "box 2 is `**implement with an agent**`" |
| `test_every_box_states_what_UNCHECKED_means` | the unchecked half of the `proofer` box | "does not say `nothing reviews`" |
| `test_the_exit_names_what_does_not_run_rather_than_where_it_ends` | `no review` in the exit's cell | "does not name `no review`" |
| `test_the_ceiling_is_stated_beside_the_shape` | the lead **The ceiling.** | "the ceiling paragraph was renamed" |
| `test_the_planning_row_is_a_record_and_not_a_checkbox` | box 4's label, made `plan with the framer` | "the `Planning` axis reached a checkbox table" |
| the same case, its new guard | the header of the table of boxes | "holds no table of boxes to read" |
| `test_the_skill_names_the_record_and_no_per_command_waiver` | `` `Seal-Routing: no work item` `` | the phrase's assertion |
| `test_the_batch_asks_for_the_language_rows_and_names_where_a_default_is_recorded` | `gh pr list --state all --limit 10` | "the batch shows no history beside the language question" |
| `tests/text/test_review_axes.py#test_the_routing_section_holds_the_answers_and_the_shape` | the lead **What is checked is the answer, …** | "the routing question's file lost `What is checked is the answer`" |

A first attempt at the boxes' order replaced box 1's label, and the case raised `StopIteration` while building its own message, at a line that names nothing. I ran it again on box 2. Before the cases were re-pointed, ten of them were red against the body alone (executed, on the working tree after the move): the eleven above without the `Planning` case, which is exception 4.

**No unit of this phase adds behaviour, so no other `seal mutate` run is owed.** The passages moved with their text, which is the *Names or places only* row of `skills/verify/SKILL.md` *The narrow command still has to be able to fail*. No case reads a sentence of the merge order (`frame/design.md` G15), so nothing was re-pointed at `merge-order.md`; `tests/behaviour/test_docs_line_wrap.py` reads both new files through `COVERED`, and `tests/behaviour/test_a_cited_section_stands_in_its_file.py` resolves the four citations of them.

**The citation check reads a new file only once it is staged.** `test_every_cited_section_stands_in_what_the_archive_holds` builds its archive from a copy of the index, and a file added with `git add -N` is not in that tree. It was red on the two citations of `routing-question.md` until the file was staged, and is green at the commit.

**The body holds 5,597 words after this phase (executed, `wc -w`), against 7,311 before it.** 1,830 words left with the ranges `frame/design.md` D3 counts for *Scope* items 1 to 3, and 116 entered, against D3's estimate of 140. The sentence for `routing-question.md` is D4's condition and one more sentence saying what the file holds. The sentence for `merge-order.md` is D4's condition and a clause saying the same of that file.

**For phase 2.** The fold paragraph is untouched. Its sentence "the move by *Orchestrator: how the work is routed*" still resolves, because that section keeps the choice of the item that carries the move. One sentence of the moved range also binds a release of one work item: "Where a crafter builds that work item and its `frame/plan.md` *Operational impact* does not name the move, the move is a decision the framer folds into that section". It now stands only in `merge-order.md`, which a release of one item never opens. The body's fold paragraph names the version move among a decision's examples and in the sentence `frame/design.md` D1 row 10 holds, so the rule is still in the body in general form. Whether the rewritten paragraph should also say that the move's fold lands in *Operational impact* before the last phase is spawned is the framer's to decide, and this phase adds nothing for it.

**For phase 3.** Every line number of the body in the frame is a line of `9e9d1087f`, and the body is now 150 lines shorter, so each passage is found by its words. `### What the answer writes` now opens with its table of rows. **The exit is last**, which *Removes* row 13 names as the home of that row's first sentence, stands in `routing-question.md`. The check of exception 1 also binds *Scope* item 6: an opening that repeats 15 consecutive words of either new file's first paragraph is refused.

**The set at the phase boundary** was `bin/test tests/text tests/behaviour tests/lib/test_core.py -q` (executed, at `4112c5924` with this record, `gaps.md` and the Status cell in the working tree): the two directories are the tree-wide files `CONTRIBUTING.md` names and hold every case the plan row names and every test file this phase changed, and `tests/lib/test_core.py` is the one file outside them that opens a path this phase changed. It exited 1 with 1,869 passed, 8 skipped and 1 failed, the case of exception 5. Before `gaps.md` stood, `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview` was red too, on this work item's missing closing memo, and it is green with the memo.

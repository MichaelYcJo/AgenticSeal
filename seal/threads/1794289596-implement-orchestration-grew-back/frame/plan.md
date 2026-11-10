# Implementation Plan: 1794289596-implement-orchestration-grew-back

## Technical context

The tree as read at `9e9d1087f`.

`skills/implement/orchestration.md` is one file of 681 lines that every orchestrating session opens before its first edit, sent there by the hook's last line (`lib/core.py#START`) and by `skills/implement/SKILL.md:26-29`. Two files were already cut from it on a condition: `skills/implement/bootstrap.md`, named in the opening paragraph at `:10-13`, and `skills/implement/multi-repository.md`, named at `:514-516`. Each opens with a paragraph saying who opens it and when, and each is on `tests/behaviour/test_docs_line_wrap.py#COVERED`. This work cuts the files `frame/design.md` D2 lists the same way.

The fold rule is one paragraph, `:55-128`, inside *Orchestrator: the order inside a ticket*. `tests/text/test_the_rules_have_one_owner.py#the_order` slices that section from its heading to `### The frame is read against the issue at the spawn`, and `#test_a_decision_after_the_frame_is_folded_into_it` (`:374-455`) asserts one phrase per clause inside the slice. The phrases are the paragraph's present wording, so the rewrite turns each red until the case names the new wording. Every clause stays inside the slice.

The routing section is `:255-517`. `tests/behaviour/test_waiver_decided_at_start.py` reads the whole file through `ORCH` (`:46`) for the two question tables (`#labelled_table` with the headers `Order, Label` and `Order, Box`), the ceiling, the mark and the language-key paragraph, and reads the same constant for the row vocabulary, which stays in the body. So the constant cannot be re-pointed whole: each case reads the file its sentence stands in. `tests/text/test_review_axes.py:221-262` reads two moved leads beside phrases that stay.

`tests/behaviour/test_a_cited_section_stands_in_its_file.py` reads every citation in the tree, the new files' among them, and excuses the policy document's citation of *Question 1* through the pending operation of `frame/design.md` *Rule changes* (`frame/design.md` G13).

What breaks in six months. First, the fold rule read as paragraphs of judgment loses the order its acts had as one sequence: an orchestrator sends a decision with no row written first, or commits the row apart from the fold. The signal is a `regression:` line traced to a fold, which #1442 counted, and the paragraph on what the orchestrator records keeps those acts together in the order they are taken. Second, nothing holds the body at its size (`frame/design.md` G3), so the next rules added to it grow it again, and the settle is what reads that. Third, the routing question is opened only when asked, so a change to the row vocabulary in the body can leave the question's tables behind; `tests/behaviour/test_waiver_decided_at_start.py` reads both against `lib/routing.py` and fails on that.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Cut the passages that are read on a condition into files opened on that condition, rewrite the fold rule in place with every clause kept, and state once what the body states twice | An orchestrator skips a file its step needs: it puts the routing question from memory, or merges two items without the order. | Chosen. Each file's condition is one the orchestrator can read off its own state: a question is being put, or a release holds two items. |
| 2. The same, with the fold's exchange with the framer, `frame/design.md` D1 rows 6 to 11 and 18, in a third file opened when a decision is made after the frame is committed | Seven of the last eight work items folded their frame after its commit (`frame/design.md` G23), so nearly every run would open the file: the count would fall while the reading stayed, which is row 6's failure. | Rejected, on the orchestrator's reading of the frame of 2026-11-10. The first draft of this frame chose it; the count overturns it. |
| 3. Find the words by shortening the fold rule: drop clauses | A rewrite that keeps every clause weighs 829 words against 872 (`frame/design.md` G10). Each clause answers a finding (`frame/design.md` D1), and dropping the row written before the send, or the whole-file read, reopens #1442 or #1318. | Rejected. The issue asks that no clause be dropped by accident, and none can be chosen to go. The words come from `frame/design.md` *Scope* items 1, 2, 5 and 6. |
| 4. Keep the one file, the structure that stands, and tighten its prose in place | 2,069 words have to leave. Tightening sentences that cases pin and other files cite rewords the rules without moving any. | Rejected. The premise that would keep one file is that every run needs every section, and it is false: question 2 is read under one answer of four, the merge order where a release holds two items, the language keys once per repository. |
| 5. Replace the structure: one short index and a file per section, each opened at its step | A run opens most of them anyway, the order, the batch, the declaration, *Under agentic*, the ladder and the drain, so it pays the same bytes over more reads, and each heading `frame/design.md` G11 lists changes its path across the tree. | Rejected. Only a passage read on a condition repays a file. |
| 6. Move *Under agentic* out in place of *Scope* items 2, 5 and 6 | `agentic` is the marked answer, so nearly every run would open the file, and the count would fall while the reading stayed. | Rejected. |
| 7. Leave the language-key paragraph in the batch section | A paragraph acted on once per repository is read by every run, and without its 216 words the estimate passes the bound (`frame/design.md` D3). | Rejected. |
| 8. Move the single item's version move with the merge order | A release of one work item never opens `merge-order.md`, and its first pull request would leave the version unmoved. | Rejected. The body keeps the move, the sentence on folding it into *Operational impact* among it (`frame/design.md` D1 row 24); the file takes what needs a second item. |
| 9. Remove the ladder's sentence citing issue #35 with the two sentences of *Removes* row 17 | The citation is pinned on purpose (`frame/design.md` G18). | Not this work's. Row 17 takes the two sentences no case holds and no party acts on. |
| 10. Add a case that fails where the body passes 5,242 words | A stored count kept beside the tree, which refuses the next rule a finding adds whatever it is worth (`frame/design.md` G3). | Rejected. The settle reads the growth. |
| 11. Reduce the fold case to the paragraphs' bold leads | Round 2 of #1442, finding 1, found sentences going with the suite green while only a lead was pinned (`tests/text/test_the_rules_have_one_owner.py:419-423`). | Rejected. That round argued it, and the case keeps one phrase per row of D1. |
| 12. Keep the heading `Question 1` in the new file | The pending operation's `to` would hold `*Question 1*`, the check would excuse nothing, and the suite is red until the settle (`frame/design.md` G13). | Rejected. The heading is *Question 1, the mode*. |
| 13. Edit `docs/running/the-review-and-parity-arms.md` in the pull request | A work item whose subject is not the policy root rewriting a policy section is what `## Rule changes` exists to prevent (`frame/design.md` G4). | Rejected. One `change` operation carries it. |
| 14. Leave the paragraph **A question in this batch names its answers** in the batch section | It is read by every run and acted on only where a question is written for a person, and without its 70 words and those of *Removes* rows 16 to 18 the estimate sits at the bound (`frame/design.md` D3). | Rejected. |
| 15. Move **A route is raised when the work outgrows it, and never lowered** out of *Under agentic* | It is read on a condition, the work outgrowing its route, that the orchestrator meets mid-run with no step that would send it to a file. | Rejected. A rule the orchestrator must already hold to notice its condition stays in the body. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2, 3, 7 and 8 | `tests/behaviour/test_waiver_decided_at_start.py`, `tests/text/test_review_axes.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/behaviour/test_first_setup_asks_once.py`, `tests/text/test_the_direct_answer_owes_the_sealers_record.py`, `tests/behaviour/test_a_commit_names_its_repository.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/text/test_the_rules_have_one_owner.py` green. Each case re-pointed at a new file shown red with its sentence deleted from that file. `frame/design.md` S5 and S6. | `4112c5924` |
| 2 | `frame/design.md` *Scope* item 4 | `tests/text/test_the_rules_have_one_owner.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/skills/test_settle.py` green. The rewritten fold case run once against the order section as phase 1 left it, with every phrase it misses collected and named in the phase record. `frame/design.md` S2 and S3. | `500d2cb98` |
| 3 | `frame/design.md` *Scope* items 5 and 6; `changelog.md` with its `### Process changes` table (`frame/design.md` G19); `gaps.md` | The modules of phase 1 and `tests/behaviour/test_chain_hooks_hardening.py`, `tests/lib/test_core.py` and `tests/text/test_broad_gate_rule.py` green. `wc -w skills/implement/orchestration.md` printed in the phase record (`frame/design.md` S1). `frame/design.md` S4 and S7. | |

Where phase 3's count is above S1's bound, the crafter cuts nothing that *Scope* does not name: it records the count in its phase record and hands it back, and what leaves next is a decision for the fold.

No case is removed or weakened. Each case of `frame/design.md` G15 holds after the change what it held before, read from the file its sentence stands in. The suite is `unverified` by the build, and the orchestrator answers it with the broad gate.

## Overlap with the release

The spawn named three other work items. #1476 is framed beside this one and has no frame committed; #1478 and #1479 are not started. Each is read from its issue (`frame/design.md` G22).

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1476 | `skills/implement/orchestration.md`: #1476 puts the records-only exception in one place, and the file states it in the drain's first row at `:648`, which this work leaves. The sentence on a late version move's verifying round at `:485-489` is the verifying-round rule too, and this work moves it to `skills/implement/merge-order.md`. `tests/text/test_the_rules_have_one_owner.py`: #1476's *Done when* names the module, and this work rewrites its fold case. | #1476 | #1476 carries the version move, so it is the first pull request into the release branch. This work then merges the release branch in, and where #1476 changed `:485-489` the merge carries its wording into `merge-order.md` (`frame/questions.md` Q1). S1's count is taken after that merge. |
| #1478 | `skills/implement/orchestration.md`: #1478 edits step 2's `pr.md` sentence at `:41-50`, which this work leaves. It changes what `pr.md` holds, and `frame/design.md` D1 rows 9 and 12 state two things `pr.md` holds or owes. | #1477 | #1478 is not started and builds after #1476 by its own issue. It then reads rows 9 and 12 at the homes this work gives them, once, where the other order would have this work fold #1478's change into a paragraph it is rewriting. |
| #1479 | `skills/implement/orchestration.md`: #1479 edits the flow-log sentence at `:166-171`, in *The frame is read against the issue at the spawn*, which this work leaves. | #1477 | #1479's issue says it builds after #1477. The two diffs share no paragraph, and #1479 lands on the smaller body. |

## Operational impact

No migration, no environment variable, no dependency. This pull request does not move the version; #1476 does.

The files `frame/design.md` D2 lists are added, and the release ships them with the skill. A session that opens `skills/implement/orchestration.md` from this release on opens `routing-question.md` or `merge-order.md` on the condition `frame/design.md` D4 names, and finds neither the question's tables nor the merge order in the body. The hook's line and every heading other files cite, except *Question 1*, are unchanged.

The diff changes a `skills/*/orchestration.md` file, so the last phase's crafter ends `changelog.md` with `### Process changes` and its table (`frame/design.md` G19).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-10 | The clause on where the version move stands (a crafter writes the move only where the item's `frame/plan.md` *Operational impact* names it, so the framer folds the move into that section before the last phase) stands in the body's fold rule as D1 row 24, beside row 10, and leaves `skills/implement/merge-order.md`; phase 2 makes both edits. Phase 2's crafter also corrects the two `gaps.md` *Not done* paragraphs this decision and `109fd9390` made stale, before its build, in place of a separate fix pass. | Phase 1's hand-back (crafter, `trail/phases/phase-1.md` *For phase 2*, and `gaps.md` *Not done*): at `4112c5924` the clause, from `9e9d1087f` `skills/implement/orchestration.md:480-484`, stood only in `merge-order.md`, which a release of one work item never opens. The framer agreed with the orchestrator's option (a), changed to one home so one fact keeps one source. The `gaps.md` paragraphs are the crafter's file, and the next crafter spawn reads them before any round does. | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the fold paragraph; `frame/plan.md` *Alternatives considered* row 8 |

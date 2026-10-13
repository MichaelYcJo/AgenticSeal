# 1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis — overview

📋 implement applied
· spec:     pending — filled at phase 3's close
· evidence: pending — filled at phase 3's close
· verified: pending — filled at phase 3's close

## Why this work exists

Pressing `automation` or `no work item` showed four boxes that mean nothing
under either answer, so question 1 is now asked alone and the boxes follow in
a second call only under `per axis`.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| How the renamed heading's ledger rows are repaired | `plan.md` *Technical context*: "`seal/releases/0.12.0.md` rows citing … drift on the rename; … the re-read is a citing row in this item's fragment: `bin/evidence-check --reverify --into …`". Found: five released families cite the heading, not two (0.12.0's two rows, 0.15.5 A2, 0.19.0 `Corrected · P4` through its `### A work item that commits in more than one repository` path, and 0.21.0 S10), and a renamed heading is a moved anchor, which a re-read does not clear | one `Corrected ·` row per family, carrying every coordinate at its new place | `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*: "A released row whose anchor moved is not cleared by a re-read, because the family is keyed on the coordinate, and a `Corrected ·` row re-points it." 0.12.0's *one spelling* row also states the retired sentence as the spelling, so its claim changes too |
| The S1 case's name | `plan.md` phase 2: "the three cases assert the spelling". Done, and `test_the_question_is_two_questions_in_one_call` is renamed `test_question_1_is_asked_alone_and_the_boxes_only_under_per_axis` with its docstring rewritten | renamed | Its name and docstring ("Two `AskUserQuestion` calls is two waits and the batch rule is broken by the second one, whatever either call contains") state the retired rule; the same grounds as Q4 for the headings. No ledger row or `Enforced by:` line names it; the one mention is `seal/specs/1791382684-…/inventory/6-tests.md`, an earlier work item's record |
| The one spelling | `spec.md` §*Data & interfaces* and Q5: "Ask question 1 alone, and the four boxes in a second call only under `per axis`." Written: "Ask question 1 alone; the boxes in a second call only under `per axis`." | the written sentence, fourteen words | The frame's sentence is sixteen words, and `tests/test_no_passage_is_pasted_into_a_second_file.py#test_no_pair_shares_more_than_it_was_measured_at` refused it in `skills/implement/orchestration.md` and `templates/claude-md-block.md`: "share 2 runs of 15 words where 0 were measured … Link to the home instead of copying it". The block cannot link (it is read by sessions that never load the skill), and `tests/test_review_axes.py` requires one spelling in both, so the sentence is shortened under the passage window rather than the baseline raised. Both halves of the shape are still named |
| The section heading | `spec.md` §*Data & interfaces*: `## Orchestrator: how the work is routed — question 1 alone, the boxes only under per axis, one file`. Written: `## Orchestrator: how the work is routed — question 1 alone, boxes if per axis, one file` | the written heading | The frame's heading is 99 columns; `tests/test_docs_line_wrap.py#test_prose_stays_within_the_wrap_limit` refused it: "skills/implement/orchestration.md:255 is 99 columns (limit 88)". The written one is 87. The act table row and `docs/worktree-guard-spec.md` §*Known limits* follow it. `### Question 2 — \`multiSelect\`, asked only under *per axis*` is as the frame named it |
| The stale list reaches `agents/smith.md` | Not in the plan. `test_the_smith_carries_its_own_half_and_not_the_questions` checked `agents/smith.md` against the three old counts only | it checks the shared `STALE` tuple, the retired sentence included | `skills/agent-contract/SKILL.md` §12: the class is every copy of a retired shape, and that case is one of its readers |

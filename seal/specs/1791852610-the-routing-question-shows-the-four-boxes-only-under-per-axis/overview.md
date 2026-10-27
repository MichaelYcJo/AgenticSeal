# 1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis — overview

📋 implement applied
· spec:     `spec.md`, `plan.md`, `questions.md`, `routing.md` of this item; `skills/implement/orchestration.md` §*Orchestrator: how the work is routed* (all of it) and §*Orchestrator: which of these acts runs itself*; `docs/worktree-guard-spec.md` §*Creation consent* rules 1–5 and §*Known limits*; `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*; `templates/claude-md-block.md`; `templates/sdd-phase.md`, `templates/sdd-overview.md`
· evidence: `seal/ledger/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis.md` — S5; five `Corrected ·` rows (0.12.0 *one spelling*, restated as S4, and *No agent … `AskUserQuestion`*; 0.15.5 A2; 0.19.0 `Corrected · P4`; 0.21.0 S10); 22 `Re-read ·` rows written by `--reverify --into` for the families the edits drifted
· verified: executed — phase 1's case green and seen red; phase 2's pins red, then the plan's module set plus three readers (`363 passed`), the 60 modules that read an edited file (`6703 passed`, failures named in `phases/phase-2.md`, each fixed or re-run), `claude_block.py --check` 0, `evidence-check --strict` 0, `unverified-check` 0, `uvx ruff check` / `format --check` 0 on the changed test files; read — each drifted family's claim against this branch's edits

## Why this work exists

Pressing `automation` or `no work item` showed four boxes that mean nothing
under either answer, so question 1 is now asked alone and the boxes follow in
a second call only under `per axis`.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| How the renamed heading's ledger rows are repaired | `plan.md` *Technical context*: "`seal/releases/0.12.0.md` rows citing … drift on the rename; … the re-read is a citing row in this item's fragment: `bin/evidence-check --reverify --into …`". Found: five released families cite the heading, not two (0.12.0's two rows, 0.15.5 A2, 0.19.0 `Corrected · P4` through its `### A work item that commits in more than one repository` path, and 0.21.0 S10), and a renamed heading is a moved anchor, which a re-read does not clear | one `Corrected ·` row per family, carrying every coordinate at its new place | `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*: "A released row whose anchor moved is not cleared by a re-read, because the family is keyed on the coordinate, and a `Corrected ·` row re-points it." 0.12.0's *one spelling* row also states the retired sentence as the spelling, so its claim changes too |
| The S1 case's name | `plan.md` phase 2: "the three cases assert the spelling". Done, and `test_the_question_is_two_questions_in_one_call` (NAME NOT IN TREE, by this rename) is renamed `test_question_1_is_asked_alone_and_the_boxes_only_under_per_axis` with its docstring rewritten | renamed | Its name and docstring ("Two `AskUserQuestion` calls is two waits and the batch rule is broken by the second one, whatever either call contains") state the retired rule; the same grounds as Q4 for the headings. No ledger row or `Enforced by:` line names it; the one mention is `seal/specs/1791382684-…/inventory/6-tests.md`, an earlier work item's record |
| The one spelling | `spec.md` §*Data & interfaces* and Q5: "Ask question 1 alone, and the four boxes in a second call only under `per axis`." Written: "Ask question 1 alone; the boxes in a second call only under `per axis`." | the written sentence, fourteen words | The frame's sentence is sixteen words, and `tests/test_no_passage_is_pasted_into_a_second_file.py#test_no_pair_shares_more_than_it_was_measured_at` refused it in `skills/implement/orchestration.md` and `templates/claude-md-block.md`: "share 2 runs of 15 words where 0 were measured … Link to the home instead of copying it". The block cannot link (it is read by sessions that never load the skill), and `tests/test_review_axes.py` requires one spelling in both, so the sentence is shortened under the passage window rather than the baseline raised. Both halves of the shape are still named |
| The section heading | `spec.md` §*Data & interfaces*: `## Orchestrator: how the work is routed — question 1 alone, the boxes only under per axis, one file`. Written: `## Orchestrator: how the work is routed — question 1 alone, boxes if per axis, one file` | the written heading | The frame's heading is 99 columns; `tests/test_docs_line_wrap.py#test_prose_stays_within_the_wrap_limit` refused it: "skills/implement/orchestration.md:255 is 99 columns (limit 88)". The written one is 87. The act table row and `docs/worktree-guard-spec.md` §*Known limits* follow it. `### Question 2 — \`multiSelect\`, asked only under *per axis*` is as the frame named it |
| The stale list reaches `agents/smith.md` | Not in the plan. `test_the_smith_carries_its_own_half_and_not_the_questions` checked `agents/smith.md` against the three old counts only | it checks the shared `STALE` tuple, the retired sentence included | `skills/agent-contract/SKILL.md` §12: the class is every copy of a retired shape, and that case is one of its readers |
| A sub-heading in the frame's `## Removes` | Not in the plan. `spec.md` gains `### Why these rows` above the prose paragraph under the Removes table, words unchanged | added, in `1db4e4bb` | The orchestrator's request mid-build: #905, built in parallel, ends the section at the next heading of any level and refuses a line under it that is neither a table row nor a `nothing — <why>` line |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck: `unverified`, because the broad run is the sealer's, once, after the rounds settle | #917, merged with lint and the suite green on the ubuntu, macOS and Windows legs; the repository configures no typecheck |
| closed That the harness shows a lone question 1 with no boxes on screen, and that a session following the new block puts the second call only after `per axis`. Read from the documents; no session was run against them | answered by the routing records written since, such as `seal/specs/1793057293-root-migrate-removes-every-directory-it-emptied/routing.md`: question 1 was answered alone, `Answer pressed` reads `automation`, and no second call for the boxes followed (read; default taken by the 0.22.4 settle) |
| closed `plan.md`'s approval line read `Approved <date> by <who>`. The orchestrator asked for it to be filled; the edit was refused by the session's permission classifier and not retried | filled by the orchestrator at `bb9eed9b` (`plan.md:7`); round 1's ⬜ 6 |

## Not done

`seal/specs/1791382684-…/inventory/6-tests.md` still names the renamed S1
case. It is an earlier work item's inventory, read at the time it was
written, and the frame leaves earlier items' records alone for the same
reason.

## Fed back into the spec

The two spelling changes above are recorded as divergences, not written back
into `spec.md`. At the run's end, the notes commit corrected three grounds in
the frame that round 1 found false, each marked *Corrected 2026-10-13 after
round 1* where it stands: `spec.md`'s §1 Grounding row and `questions.md` Q1
(§1 does not make a second call part of the one batch), the routing
section's Grounding row (six options, not five), and §*Data & interfaces*
on the batching case (its bare `in one call` no longer holds). These are
corrections of the frame's reading, made after its build; a framer may
overturn them.

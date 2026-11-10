# Implementation Plan: 1794352647-a-first-frame-preloads-the-fold-procedure

## Technical context

The tree as read at `5d16bcd4d`.

`agents/framer.md` is 289 lines and 17,298 B. Its last rule, *You have two routes back* (`:256-289`), holds the fold of a decision made after the frame is committed (`:257-281`), the reframe on a `regression:` (`:281-288`) and the rule's `check:` line (`:289`). A spawn preloads the whole file with `skills/core/SKILL.md` and `skills/agent-contract/SKILL.md` (`frame/design.md` G3). The fold is the framer's half of `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, which cites it at `:61-62` and says at `:104-107` that the orchestrator resumes the framer or spawns a fresh one. The reframe's owners are `docs/running/the-run.md` *The run* and the row *The framer* of `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame* (`frame/design.md` G6).

The pins are in `tests/text/test_the_rules_have_one_owner.py` (`frame/design.md` G9). They read the moved text as phrases, so a phrase whose citation changes turns red until the case names the new words. The fold case slices from the rule's lead to the next `check:`, and the new file keeps both, so the slice holds the same text.

The new file follows the shape of `skills/implement/routing-question.md` and `skills/implement/merge-order.md`, which #1477 cut from `skills/implement/orchestration.md`: a title, a paragraph saying who opens it and when, then the text, and an entry in `tests/behaviour/test_docs_line_wrap.py#COVERED` at birth.

The byte budget has 52 B of slack (`frame/design.md` G4). A pointer sentence longer than the one `frame/design.md` *Scope* item 2 gives, or a mark rule that keeps part of the sentence *Scope* item 3 removes, can put S1 out of reach.

What breaks in six months. First, a resumed framer answers a fold from memory and does not open the file. The orchestrator's message names the file (*Scope* item 4), and the definition's pointer is in the resumed framer's context too. Neither forces a `Read`, so the signal is a fold whose hand-back skips a clause the file states, such as not naming the statements it contradicts in files the framer does not write. Second, a later change adds a fold clause to `agents/framer.md` again rather than to the new file. The fold case reads only the new file, so the duplicate passes the suite, and review is what reads it. Third, the reframe now rests on a row of the orchestrator's file. Where `skills/code-review/orchestration.md` rewrites the framer's route, the citation in the new file still resolves to the heading, but the row may no longer say what the framer rewrites. `tests/behaviour/test_a_cited_section_stands_in_its_file.py` reads the heading and not the row.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Move the fold to `skills/implement/fold-and-reframe.md` word for word, with four citations re-pointed, and write the reframe there as a citation of its two owners. The definition keeps a one-sentence pointer, and the orchestrator's file cites the new file and has every fold message name it. | A resumed framer skips the file (*Technical context*, first failure). | Chosen. It meets the issue's *Done when* with 52 B to spare (`frame/design.md` G4), and no route reads more than it did (`frame/design.md` G5). |
| 2. Keep the structure: the fold and the reframe stay in `agents/framer.md` | Every first frame preloads 2,348 B it never uses. No frame at six tags carries a `Reframed` line (`frame/design.md` G5). | Rejected. The premise that would keep it is that every framer spawn needs the rule, and a first frame never folds or reframes. |
| 3. Put the fold in `skills/implement/orchestration.md`, beside the orchestrator's half of it | The framer would open a 31,447 B file written for the orchestrator to read one section. The file addresses the orchestrator by name, and a "you" there would read as the orchestrator (`skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*). | Rejected. |
| 4. Put the new file under `agents/` | `skills/verify/scripts/payload_meter.py#agents_in` reads every `agents/*.md` as an agent definition, so `release_report.py` would print a sixth agent (`frame/design.md` G10). | Rejected. |
| 5. Move the release-overlap judgment, `agents/framer.md:84-95`, too, into its own file or into `skills/implement/merge-order.md` | Every plan at v0.37.2 wrote the section against a spawn that named other items (`frame/design.md` G12). Most first frames would then open one more file and also preload the pointer to it, and in `merge-order.md` they would read 2,017 B written for the orchestrator. | Rejected. The judgment is used on most first frames, and S1 holds without it. |
| 6. Move the exchange before the first build, `agents/framer.md:248-254`, with the fold | The orchestrator reads every frame a framer drew before the first build (`frame/design.md` G13), so most framers would open the file anyway. `docs/running/the-agent-set.md:76-77`, in the policy root, names `agents/framer.md` as the framer's half of the exchange. | Rejected. The exchange is part of a first frame's life. |
| 7. The reframe half cites `docs/running/the-run.md` alone, as the issue words it | The run document states only the `Reframed` line. The rewrite of `plan.md` with new phase rows, each closed phase keeping its commit, and of `frame/design.md` where the scope moves would be stated nowhere the framer is sent (`frame/design.md` G6). | Rejected. The new file cites both owners. |
| 8. Rely on the definition's pointer alone for a resumed fold | The issue names this loss: a resumed framer may answer without opening the file. | Rejected. The orchestrator's message names the file in both cases (`frame/design.md` *Scope* item 4). |
| 9. Remove only the git-dir clause of the mark rule and keep "It is the only evidence in the tree that the framing happened." | The kept clause and its full stop leave the saving at about 2,290 B, under the 2,300 B of S1 (`frame/design.md` G4). The framer writes the mark without the reason, and `tests/behaviour/test_waiver_decided_at_start.py#test_the_framer_leaves_a_mark_in_the_tree` keeps the reason in its docstring. | Rejected. The issue's change takes the sentence, and the sentence is one. |
| 10. Add a case that reads the path from the pointer, from the orchestrator's citation and from the disk | The re-pointed pins already fail on a mismatch in any one place (`frame/design.md` G9), so the case would be a second check on the same fact. | Rejected. No case is added. |
| 11. Keep the moved text's citation of *What the tree can answer, you answer* for a fact that reaches the framer in prose | #1474 rewrites the sentence of that rule which states it (`agents/framer.md:149-151`), so the new file would cite a sentence another item of the release changes. | Rejected. The new file cites contract rule 5, which that sentence restates (`frame/design.md` G11). |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 7 | S1: `wc -c agents/framer.md` at most 14,998 B, and `git diff --stat 7c2801838 -- skills/core/SKILL.md skills/agent-contract/SKILL.md` empty. S2: `git grep -n "git dir" agents/framer.md` exits 1. S3 to S7: `tests/text/test_the_rules_have_one_owner.py`, `tests/behaviour/test_waiver_decided_at_start.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/text/test_the_record_is_written_in_words.py` and `tests/github/test_rules.py`, run narrow. Each changed pin is seen red with its path changed in one place, and the new row of the order case with its sentence deleted (contract rule 15). S6: the moved text compared with `git show 5d16bcd4d:agents/framer.md`, lines 257 to 281. | `cb567aabf` |

## Overlap with the release

As read on 2026-11-11 at `5d16bcd4d`: the spawn names #1471, #1472, #1474 with #1503, #1480 and #1475. Their issues were read with `gh issue view` (executed). None has a committed frame: #1471's branch holds only its `routing.md` commit `2b2bb623e` (executed, `git log`), and the others have no branch. Each row below is judged from the issue's *Files* and coordinates. This work meets all five, and merges after #1471 and before the other four.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1471 | Both add a file under `skills/implement/` that one kind of spawn opens. Both are likely to add that file to `tests/behaviour/test_docs_line_wrap.py#COVERED` after `skills/implement/merge-order.md` (`:158`), which leaves two adjacent insertions. #1471's issue names `tests/text/test_a_moved_rule_leaves_its_definition.py` and not that list, so whether it adds there is for its frame to say. | #1471 | #1471 carries the version move, and `skills/implement/merge-order.md` puts the item that carries the move first. The integration is at most one pair of adjacent list lines, and keeping both resolves it. |
| #1472 | `agents/framer.md`: #1472 rewrites the dated-section sentence of the fold (`:276`), which this work moves word for word into `skills/implement/fold-and-reframe.md`. | #1473 | #1472 builds after #1471 and has no frame yet. Once this merges, #1472's framer finds the sentence at its new path and rewrites it there, at no cost to either. In the other order, this item would carry #1472's wording across a conflict between a rewrite and a move. |
| #1474 with #1503 | `agents/framer.md`: #1474 rewrites the rule-5 sentence (`:149-151`) and the scratch sentence (`:156-158`). This work edits `:235-237` and `:256-289`, so the hunks are far apart. The moved text no longer cites the rule-5 sentence (*Alternatives considered* row 11). | #1473 | #1474 is ordered after #1472. No sentence of this work reads what #1474 changes. |
| #1480 | `agents/framer.md`: #1480 rewrites step 5 (`:96-103`) and folds checks into the definition. This work edits `:235-237` and `:256-289`. | #1473 | #1480's issue orders it after this item. S1 is measured on this branch against its base, so #1480's added bytes change neither item's acceptance. |
| #1475 | The `check:` lines: this work moves `agents/framer.md:289` into `skills/implement/fold-and-reframe.md`, which no spawn preloads. #1475 deletes and counts the check lines of `agents/*.md` and the contract. | #1473 | #1475 is last by its issue, because it touches every definition. It reads the set of lines this work changes, so it counts them after this work merges. |

## Operational impact

None. No migration, environment variable, dependency or compatibility break. This work item takes no version move: #1471 carries the release's move.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|

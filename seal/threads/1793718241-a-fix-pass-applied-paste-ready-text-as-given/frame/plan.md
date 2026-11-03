# Implementation Plan: a fix pass reads a paste-ready fix, and a case's red is its own guard's (#1286)

## Technical context

The work edits prose at six coordinates and one existing case, and no code:

- `agents/crafter.md:167-170`, inside *A fix pass appends close blocks and writes no phase record*, whose check is `tests/text/test_a_moved_rule_leaves_its_definition.py` (line 185). The case `#test_the_crafters_fix_pass_appends_a_close_block_and_sweeps_what_its_range_reworded` (`:454`) pins the paragraph's clauses at `:472-482`. It is the one case that reads the paste-ready sentences (executed: `git grep -n -e "proofer's claim and not the fix" -e "own reader would" -- . ':!seal/threads'` printed `agents/crafter.md` and that case alone).
- `skills/agent-contract/SKILL.md:179-184`, rule 15, which carries no `check:` line. No case pins its sentences (executed: `git grep -n -e 'A case that passes against the defect' -e 'A new case is not planted' -- tests evals` printed nothing).
- `agents/sealer.md:142-149`, whose check is `evals/behaviour/sealer/rule-sealer-false-red/`. The eval's grader reads the sealer's `Verdict:` line, not this sentence (read: `graders/truth-false-red.md:4`).
- `skills/verify/SKILL.md:41-44`, `skills/implement/SKILL.md:162-164` and `skills/code-review/SKILL.md:171-172`. No case pins the three sentences that change (executed: `git grep -n -e 'A case that passes there was never red' -e 'observed failing against the pre-change' -e 'seen red against the tree as it stands' -e 'takes the snippet as the repair' -- tests evals` printed nothing).

Two cases read every shipped text these edits touch. `tests/text/test_no_passage_is_pasted_into_a_second_file.py` refuses a run of 15 words shared by two files. Items 2 to 5 of `frame/design.md` *Scope* state one fact in four files, so items 3 to 5 cite rule 15 and do not restate it. `tests/behaviour/test_docs_line_wrap.py` reads the line wrap.

**Failure scenario of the chosen approach.** In six months, a fix pass under a long spawn prompt applies a paste-ready text that reads well against the frame but whose input set the frame never named. No case refuses that, and it reaches the next round as a `regression:` routed to a fix pass, as G11 routes it now. The reading is a judgment, so a missed reading surfaces only in a round. It costs a verifying round, as before, but no longer for a text the spawn told the fix pass to take unread. For rule 15, a crafter writes a guard case whose guard the code holds in two places, and it removes one of them. The case stays green, and under the new text that green is a finding the crafter meets before committing, not one a sealer meets after the broad run.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Replace the structure: the round record carries no paste-ready text, the finding describes the fix in sentences, and the fix pass writes every fix | Every fix pass re-derives a fix the proofer has already written, a snippet with its names marked as `skills/code-review/SKILL.md` *Paste-ready means the snippet cannot mislead on its own* asks. The fence is read by the record layout (`docs/layout/the-record-layout.md:134`) and the close block's place in the template (`templates/records/sdd-round.md:21`). The premise that keeps the structure holds: over the 34 pull requests of #1020's G10 there were 114 findings and 32 recurring (read, #1020's `frame/design.md` G10). The proofer's skill traces nine regressions over 0.26.0 to 0.29.0 to a paste-ready fix applied as given (read, `skills/code-review/SKILL.md:181-183`). Most paste-ready texts did not carry a defect, and G6 shows the reading catching one | rejected |
| A check that a fix pass read the paste-ready text, or a mark in the close block saying it did | Whether a text holds against the frame is a reading of meaning (G2), and a mark records that a step happened, not that it held. Both #1216 closes said what they did in `answer:` (G5) | rejected |
| A script or an eval that verifies a `seen red` was under the named guard alone | `seal mutate` already reads the exact fact, red or survived (G9). Whether the failing line is the guard's is meaning, and the sealer re-runs a sample of the claims already (`agents/sealer.md:142`). An eval costs a paid run each release, and its record shows no other instance | rejected |
| Put the paste-ready reading in `skills/code-review/orchestration.md`, the fix-pass section, or in `skills/implement/SKILL.md` *5. Incorporate review* | The orchestrator reads the first, not the fix pass. The fix pass reaches the second through `agents/crafter.md` step 1, and its rule already stands in `agents/crafter.md` (G3), so a second home states one fact twice. #1318 and #1288 rewrite the first in this release (G13) | rejected |
| Put the guard's red in `agents/crafter.md` and leave rule 15 as it is | The sealer and the proofer judge a `seen red` claim, and they do not read `agents/crafter.md`. The sealer's sentence would still refuse a correct guard case (G8) | rejected |
| Rewrite rule 15 alone, and leave the three other sentences that state a red only against old code | Each of the three is read where a party shows or re-runs a red. `agents/sealer.md:145` would call a guard case shown red under its guard "never red" (G8). Each would contradict rule 15 for the next reader | rejected |
| Tell the orchestrator not to write "apply as given" into a judgment row or a spawn prompt | Its file is #1318's and #1288's in this release (G13). The fix pass is the party that reads, and *Scope* item 1 makes its reading stand whatever the spawn says | rejected |
| Rewrite the crafter's paste-ready sentences and rule 15 in place, and make the three other red sentences and the proofer's reason cite or match them (chosen) | The failure scenario above | chosen |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 8 | `frame/design.md` S1 to S8 | 2f2d7306f |

## Operational impact

No migration, environment variable, dependency or compatibility break. A plugin user's crafter, sealer and proofer read the new text after the release that ships it.

The orchestrator owns these acts, after the seal:

- The pull request body carries `Closes #1286`.
- The title's prefix is `fix:`, the issue's, and the diff ships no step and no refusal (`skills/commit-pr-convention/SKILL.md`).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-04 | `frame/design.md` S5, S6 and S7 take the commands and the count the build bears out: S5 reads `agents/sealer.md` for `(rule 15)`, S6 runs outside `seal/`, and S7 counts seven files; the orchestrator folds them before round 1, with no framer spawn | `trail/phases/phase-1.md` names all three as departures with their grounds: a definition cites a contract rule as `rule <N>`, the frame's own quotations of the old sentence match the S6 search, and *Scope* items 1 to 6 are six files and item 7 is a test module | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-04 | `frame/design.md` *Scope* items 3 to 5, S4 and S5 take the reach round 1's fix gave the three sentences at `533801c30`: the guard-red path is a case's that asserts something is not named, counted, read or let through, and the sealer runs it in its clone with HEAD's code restored, then removes the clone; the orchestrator folds them before the verifying round. Round 1's finding is new work's, with no `regression:` line, so it took an ordinary fix pass | the fix pass's hand-back names the five cells as contradicting its fix; the sentences cite `skills/agent-contract/SKILL.md` rule 15, whose second sentence opens the path to that kind of case alone | `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer*, and `docs/running/the-run.md` *The run* |
| 2026-11-04 | Round 2's finding 1 (`regression: round-1#1`) takes an ordinary fix pass, not the framer: the verify sentence's "nothing is named" is one word from the class every other statement gives | the frame says "something is not named" (`frame/design.md` *Scope* item 4, as folded at 6ad052ce3), and the fix at 533801c30 wrote "nothing is named", carried from round 1's paste-ready text; so the fix departed from the frame, the first route's grounds. Round 2 is the second finding round, one finding against round 1's one, on the unit that round's fix wrote | `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame*, and `docs/running/the-run.md` *The run* |

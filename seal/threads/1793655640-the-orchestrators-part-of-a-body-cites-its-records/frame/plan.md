# Implementation Plan: the orchestrator's part of a pull request body cites its records (#1290)

## Technical context

The orchestrator writes its part of the body in the paragraph of `skills/code-review/orchestration.md` that opens **You write the pull request body after `trail/gate.md` is committed** (lines 357-377 at `85a238c6`). Lines 365-370 list what no record holds and then say "Your part restates no record: where it needs a record's fact, it names the record's path." That sentence came in with #1103 (`5e5275e53`) and moved above the fold with #1191 (`aa9221d3f`) (executed: `git log -L` on the sentence). Three other files restate it or stand on it, and one comment states the policy sentence it stands on (`frame/design.md` G10). The sealer reads the part at `agents/sealer.md` step 4, and nothing else reads it.

The work is text in five files and the fragment. No script, template or test changes.

**The failure scenario of the chosen approach.** In six months an orchestrator writes a sentence with a coordinate that does not hold the fact, such as a round's path for a count the round does not give. The sealer withholds as it does today, and the cost is the same as today's. The coordinate makes the withhold quicker to find, because the sealer opens the named record first and does not search for it. The second risk is a body that grows into a list of citations a reader cannot follow. `skills/writing-style/outside-the-review.md` still governs how the part reads, and the record's own sentence is one of the two forms the rule allows.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 Rewrite the sentence in `orchestration.md` in place. A record's fact in the orchestrator's part is the record's own sentence or carries its coordinate, opened at writing. A count, an "each/every/all" and a decision given to a person carry theirs. Correct the three files that copy the old rule or stand on it, and state the policy change in `## Rule changes` | Stated above: a wrong coordinate costs one sealer spawn, as today | Chosen. It is what #898's body did, and the sealer withheld nothing on its first spawn (`frame/design.md` G7) |
| A2 Replace the structure: `seal pr-body` puts the changelog fragment above the fold, so the first screen carries the records' own "what changed", and the orchestrator's part shrinks to what no record holds, as #1044 and #1103 asked | Of the four withheld sentences, none was a changelog fact. They were a count of design rows, an owner's ask, a round's finding and a proofer's reading (`frame/design.md` G6), so moving the changelog would have prevented none of them. The orchestrator would still summarise the design and the rounds for the first screen. #1044's plan rejected a computed summary as "a second statement of the records" (`v0.23.1:seal/threads/1793157214-the-pr-bodys-facts-come-from-the-records/frame/plan.md`, read). It costs a change to `pr_body.py`, its cases and the fold #1191 decided. The premise that keeps the structure, checked: the withheld facts sit in records the copy keeps folded, and only the orchestrator's part brings them to the first screen | Rejected |
| A3 A script check: `seal pr-body --check`, or a new arm, refuses an orchestrator's part whose factual sentence carries no backticked record path | The check cannot tell a factual sentence from motivation, so it would refuse a correct sentence or ask for a grammar of which sentences need a path. A path present says nothing about agreement: #1139's fourth sentence was a faithful copy of a wrong record sentence (`frame/design.md` G6). `skills/core/SKILL.md` *Judgment is spent where meaning is the question* rules out re-encoding that judgment, and the issue asks for no check (`frame/design.md` G1) | Rejected |
| A4 Keep the rule as it stands and make it stricter: the orchestrator's part names record paths and states no record's fact | The premise for keeping it is that an orchestrator will keep it. Checked: all ten bodies merged into `release/v0.28.0` state record facts above the fold (`frame/design.md` G4, executed), so the rule caught nothing and the withholds came anyway. A first screen of paths alone gives the reader #1191 put that part first for nothing, and #1044's plan rejected "links the records and copies nothing" on the same ground | Rejected |
| A5 Change nothing. Each withhold is the sealer doing its job | Each costs a body repair, a commit and a whole sealer spawn. That happened twice in 0.28.0 (#1054, #1139) and, before #1044, 23 times in 27 withheld runs (`gh issue view 1044`, read). The practice that stopped it for #898 lives in a memory note no other session reads (`frame/design.md` G2) | Rejected |
| A6 State the rule in `skills/commit-pr-convention/SKILL.md` *Pull request bodies*, which the user's own instructions name as the file read before a pull request | That section owns the body's parts and their languages and already links `orchestration.md` for how the body is written. A second statement there is a copy to keep in step. The orchestrator writes the body at the step `orchestration.md` describes, which is where the issue's *Done when* puts the rule | Rejected: the convention points to the one home (`frame/design.md` *Scope* item 3) |
| A7 Leave the Korean sentence in `skills/writing-style/outside-the-review.md:27-29` and reword it to match | Two statements of one rule, in two languages, drift apart. The old sentence was such a copy, and this work would have to correct it again at the next change | Rejected: it becomes a pointer (`frame/design.md` *Scope* item 2) |
| A8 Add to the rule that the orchestrator checks each copied record sentence against the tree | That is the sealer's step 4, and it would make the orchestrator a second auditor of the records. #1139's wrong round sentence was the proofer's reading and was the sealer's to find. A copy carries its record's claim, and the coordinate lets the sealer reach the record (`frame/design.md` G6, G8) | Rejected: the rule says the copy adds no claim of its own |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1 to 6. The crafter writes items 1 to 5 and the `### Fixed` entry of item 6. The orchestrator writes item 6's `### Process changes` row with the fragment | `git grep -n -e "기록에 없는 것만" -e "does not restate it" -e "restates no record" -- skills evals agents templates` prints nothing (S3). `git diff 85a238c6 -- skills/code-review/orchestration.md` touches no line from 379 on (S5). One command over the test modules that read a path the phase changed: those `git grep -l -e '"code-review", "orchestration.md"' -e 'code-review/orchestration.md' -e 'implement/acts.md' -e '"acts.md"' -e 'commit-pr-convention' -e 'outside-the-review' -e 'rule_cases' -e '"writing-style"' -- tests` lists, `tests/text/test_a_moved_rule_leaves_its_definition.py`, and every module that globs `skills/` or `evals/scripts/`, as contract rule 2 says. Then `bin/seal layout --check tests` where the phase touched `tests/`, which this plan does not expect. No new case: the change is wording read by an agent, and the issue asks for no check (`frame/design.md` G1) | 6b7c9a08e |

## Operational impact

None. No command, output, config row or dependency changes. A session running the installed 0.28.0 plugin reads the old sentence until 0.29.0 is installed.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |

# Closing memo: 1794362365-the-definitions-restate-the-contract

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate at the work item's HEAD. Phase 1 ran its phase-boundary set, as `trail/phases/phase-1.md` says, and fix passes 1 and 2 the same set over the paths their fixes changed, and none of them ran the broad gate. | the orchestrator, by `seal gate --record` |
| closed Whether Claude Code clears a session's scratchpad when the session ends, and how much disk a long session's scratch takes now that no agent removes a clone (`frame/questions.md` Q1). No probe a subagent runs can end a session. | answered 2026-11-11 by the owner on Q1's measurement, 574 MB in 41 session directories: the orchestrator removes the work item's scratch directory once, after the pull request opens, in one `rm -rf` with a literal path (`frame/questions.md` Q1, `frame/plan.md` *Judgments of the run*), which fix pass 1 built in `skills/implement/orchestration.md` at `979c60b7d` |
| Whether agents spawned under the released text still write an `rm` at their hand-back, and whether one that finds its directory standing takes the next free leaf (`frame/questions.md` Q2). The answer is the conduct of later runs. | a measurement, as `frame/questions.md` Q2 states |
| The crafter's eval cases under `evals/behaviour/crafter/`, whose `shape-no-probe-left` graders read the fact `frame/design.md` S8 states. They were not run. | the owner, where the release runs the crafter's eval cases |

## Not done

nothing

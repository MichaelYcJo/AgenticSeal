# Routing: 1795397629-git-runs-through-thirty-hand-written-helpers

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1573-git-runs-through-thirty-hand-written-helpers |

Answered 2026-11-23 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-23, for the twelve issues of the milestone `release: 0.38.6` (#1571 to #1582), in the one batch asked before the first edit. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The change replaces the git and `gh` runners of about twenty scripts, `seal`, `chain_check.py`, `settle.py` and the release automation among them, and a runner that tells a failure from an empty answer wrongly makes a gate read nothing.
- **Planning, framer.** The issue fixes the direction, one runner in `lib/gitcmd.py` and one `gh` runner beside it, and leaves open the runner's interface, which scripts keep loading nothing from `lib/` at import, and the order the call sites move in.
- **Implementation, crafter.** The diff touches about twenty files and their cases while the orchestrator holds two other work items of the release at the same time.
- **Review, through the review chain.** Every gate's git reads pass through the new runner, and a timeout or an exit code read differently shows only as a check that passes on nothing.
- **Automation, yes.** The work reaches nothing outside the repository, and every question has a default the issue or the tree gives.
- **Destination, open the pull request**, as under `complete`.
- **Branch, and the order.** The branch is cut from `origin/release/v0.38.6` at `c22d58982`, after #1571 landed. #1577 runs beside it in a worktree and rewrites `skills/verify/scripts/broad_gate.py`'s command reading and `run`, which runs the `Broad gate` command and not git; #1578 rewrites documents. Whichever of #1573 and #1577 lands second merges the base before its broad run (`skills/implement/merge-order.md`).

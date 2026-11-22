# Routing: 1795390621-the-broad-gate-rewrites-cmd-exe-commands

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1577-the-broad-gate-rewrites-cmd-exe-commands |

Answered 2026-11-23 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-23, for the twelve issues of the milestone `release: 0.38.6` (#1571 to #1582), in the one batch asked before the first edit. The same batch decided this issue's direction: the cmd.exe rewriter goes and the gate refuses instead, naming the `\` spelling. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The change alters the broad gate's verdict on Windows, and a defect there stops every session that runs `seal gate`.
- **Planning, framer.** The owner fixed the direction, and the issue leaves open which forms the refusal reads and where the documents say it.
- **Implementation, crafter.** The diff removes about 300 lines of `skills/verify/scripts/broad_gate.py` and their cases while the orchestrator holds two other work items of the release at the same time.
- **Review, through the review chain.** The script is a gate, and a refusal that reads a form wrongly would stop a Windows user's run.
- **Automation, yes.** The work reaches nothing outside the repository, and the owner's answer gives the one decision it needs.
- **Destination, open the pull request**, as under `complete`.
- **Branch, and the order.** The owner asked on 2026-11-23 for the release's items to run side by side where they can. This item runs in a worktree beside #1571 and #1578; #1571 carries the version move and merges first, and this item merges the base before its broad run where #1571 has landed (`skills/implement/merge-order.md`).

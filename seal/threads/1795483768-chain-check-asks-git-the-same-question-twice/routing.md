# Routing: 1795483768-chain-check-asks-git-the-same-question-twice

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | perf/1603-chain-check-asks-git-the-same-question-several-times |

Answered 2026-11-24 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-24, for #1603 alone, the one issue of the milestone `release: 0.38.7`. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The change is to `skills/code-review/scripts/chain_check.py`, the check that refuses a ready pull request, and perhaps to `skills/settle/scripts/settle.py`. A read answered from an earlier answer where the tree had moved between them would change a verdict unseen.
- **Planning, framer.** The issue leaves open which reads can be answered once, which can share a process, and whether `settle` repeats a read at all; the measurement it is judged by comes from the Windows leg of CI.
- **Implementation, crafter.** The diff spans the check's git reads across its arms, and the orchestrator holds the Windows measurements beside it.
- **Review, through the review chain.** Whether each read answered once still gives the answer the run asked for is a judgment a round reads.
- **Automation, yes.** The work reaches nothing outside the repository. The Windows-leg figures are read from `workflow_dispatch` runs of `tests` on the branch.
- **Destination, open the pull request**, as under `complete`.
- **Branch, and the order.** The branch is cut from `origin/release/v0.38.7` at `fe09bef46`, the v0.38.6 merge on `main`. It is the release's first pull request, so it moves `plugin.json` to 0.38.7.

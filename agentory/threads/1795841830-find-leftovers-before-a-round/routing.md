# Routing: 1795841830-find-leftovers-before-a-round

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | feat/1659-find-leftovers-before-a-round |

Answered 2026-11-28 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 of the routing question with `agentic` on 2026-11-28, and in the same batch accepted all three points of #1659's proposal, which is folded into the body of #1659. Each row below is judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, framer:** the work changes rules that several documents state: `agents/framer.md`, `skills/verify/SKILL.md` *Scope*, `agents/crafter.md`, `skills/implement/fix-pass.md` and `skills/implement/orchestration.md` *Under agentic*.
- **Implementation, crafter:** the release holds two other work items that this session orchestrates in parallel, so the build goes to a crafter to keep what the orchestrator holds small.
- **Review, through the review chain:** the change is to agents' instructions, and a defect in it shows as an agent that misreads the text in a later run, not as a suite that fails at the pull request.
- **Automation, yes:** the owner's decision is taken, and every question the orchestrator foresees has a default the tree or the framer can give.
- **Destination, open the pull request:** nothing in the issue or the batch asks for the branch back.

The base is the release branch, which names its version. The work item that carries the version move is chosen once the three plans state their overlap, by `skills/implement/merge-order.md`.

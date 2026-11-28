# Routing: 1795841828-settle-only-release-note

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1655-settle-only-release-note |

Answered 2026-11-28 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 of the routing question with `agentic` on 2026-11-28, and in the same batch chose that a settle-only release publishes its note from the release pull request's body, which is folded into the body of #1655. Each row below is judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, framer:** the issue fixes the direction but leaves how the script tells a settle-only range from any other range that added no fragment, and how it finds the release pull request, open; the rule also stands in several documents: the script's docstring, `docs/releasing/release-checklist.md`, `docs/releasing/branch-and-release.md` and `skills/settle/SKILL.md`.
- **Implementation, crafter:** the release holds two other work items that this session orchestrates in parallel, so the build goes to a crafter to keep what the orchestrator holds small.
- **Review, through the review chain:** the script runs only at a tag, after `main` has moved, so a defect in it shows at a release and not at this pull request's suite; a reader independent of the build is worth its rounds.
- **Automation, yes:** the owner's one decision is taken, and every question the orchestrator foresees has a default the tree or the framer can give.
- **Destination, open the pull request:** nothing in the issue or the batch asks for the branch back.

The base is the release branch, which names its version. The work item that carries the version move is chosen once the three plans state their overlap, by `skills/implement/merge-order.md`.

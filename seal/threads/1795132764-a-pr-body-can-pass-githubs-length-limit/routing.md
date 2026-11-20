# Routing: 1795132764-a-pr-body-can-pass-githubs-length-limit

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1559-a-pr-body-can-pass-githubs-length-limit |

Answered 2026-11-20 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-20, for #1559, and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*. In the same batch the owner chose the fold, past the limit the longest parts fold first and `## What changed` stays on the page, and the milestone `release: 0.38.3`; both stand in the issue body's *Decision* section and the milestone's description.

- **Planning, framer.** The owner fixed which parts fold first, and the issue leaves the rest of the design open: what one part is, the fixed line that names a folded part's file, how `seal pr-body` says which parts it folded, where the folded body stands against the `<details>` fold and the seal mark, and which documents state the limit the module docstring now calls not guarded.
- **Implementation, crafter.** The change reaches `skills/code-review/scripts/pr_body.py`'s `compose` and `compared`, the chain check's body arm that calls them, and their cases, a diff large enough that a fresh builder holds it better than the orchestrator.
- **Review, through the review chain.** `compared` is what the chain check's body arm and `seal pr-body --check` read, so a defect in it refuses a ready pull request in every repository that installs the workflow.
- **Automation, yes.** The owner answered the one design choice the issue left to a person, and every question left has a default the tree or the framer can give.
- **Destination, open the pull request**, as under `complete`.
- **Version.** `release/v0.38.3` already holds #1557's pull request, which moves `.claude-plugin/plugin.json` to 0.38.3, so this work item leaves the version alone and merges after it (`skills/implement/merge-order.md`).

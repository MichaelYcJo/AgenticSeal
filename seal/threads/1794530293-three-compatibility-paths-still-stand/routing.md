# Routing: 1794530293-three-compatibility-paths-still-stand

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | refactor/1500-three-compatibility-paths-still-stand |

Answered 2026-11-13 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-13, for the work items of 0.38.1 (#1543, #1500), and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, framer.** The issue gives a sample of what each path takes out and leaves the whole list to the frame, and the removal changes rules that several documents state: `skills/update/SKILL.md`, `docs/layout/one-root-by-lifetime.md`, `docs/checks/the-fold.md`, `docs/checks/the-pull-request-check.md` and the READMEs.
- **Implementation, crafter.** The diff spans the configuration readers, three scripts, documents and tests in two languages, large enough to threaten what the orchestrator still has to hold.
- **Review, through the review chain.** The removal touches the refusals in `skills/code-review/scripts/chain_check.py` and `skills/verify/scripts/broad_gate.py`, and a gate that loses the wrong arm stops every session that runs it.
- **Automation, yes.** The owner's comment of 2026-11-12 on #1500 fixes the direction and the *Done when* items stand; every remaining choice has a default the tree or the framer can give.
- **Destination, open the pull request**, as under `complete`.

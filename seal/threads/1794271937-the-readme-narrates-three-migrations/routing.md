# Routing: 1794271937-the-readme-narrates-three-migrations

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | docs/1492-the-readme-narrates-three-migrations |

Answered 2026-11-10 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-10, for the four documentation items of 0.37.1, and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, framer.** The issue asks the frame to state when each compatibility path is removed, which is a design choice.
- **Implementation, crafter.** A framer stands, and the build is a phase of its plan.
- **Review, through the review chain** (changed 2026-11-10 by the orchestrator after phase 1, from straight to the PR). The build had to change a check: `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#test_every_template_is_named_by_a_document_that_ships` now exempts `templates/setup/claude-md-block.md` by name, because the README paragraph this work removes was the only document naming it. An exemption in a check is what an independent reading weighs, so a proofer reads the diff before the sealer.
- **Automation, yes.** No question remains that the tree or the framer cannot answer.
- **Destination, open the pull request**, as under `complete`.

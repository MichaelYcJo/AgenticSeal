# Routing: 1795276650-the-batch-spans-every-issue-of-the-request

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1563-the-batch-spans-every-issue-of-the-request |

Answered 2026-11-22 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-22, for #1563. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*. In the same batch the orchestrator named the release: `release/v0.38.4`, cut from `main` at `f8056edde`, and the milestone `release: 0.38.4`. The owner did not object.

- **Planning, framer.** The rule this work amends is stated in three files: `skills/implement/orchestration.md` *Orchestrator: what needs a person is asked in one batch, before the first edit*, `skills/implement/SKILL.md:163-166` and `skills/core/SKILL.md:95-98`. `docs/running/the-run.md:33-53` states the rule for questions that arise during the run. The issue leaves open where the batch's scope and the check against the tree are written, and which of those statements cite the section without copying it.
- **Implementation, crafter.** Any sentence this work rewrites may be pinned by a case under `tests/` through a string a search misses. A fresh builder that runs the narrow suites holds that search better than the orchestrator.
- **Review, through the review chain.** The change is text an agent acts on at the start of every run. A defect in it would show as an orchestrator that misreads when to ask, in a later run in another repository, and no suite would catch it.
- **Automation, yes.** The issue's *Decision* states the change, and every question left has a default the tree or the framer can give.
- **Destination, open the pull request**, as under `complete`.
- **Version.** This work item is the first pull request into `release/v0.38.4`, so it carries the move of `.claude-plugin/plugin.json` to 0.38.4 (`skills/implement/merge-order.md`). `.claude-plugin/marketplace.json` holds no version field (`frame/design.md` G13).

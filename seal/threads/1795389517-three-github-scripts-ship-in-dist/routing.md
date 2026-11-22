# Routing: 1795389517-three-github-scripts-ship-in-dist

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1571-three-github-scripts-ship-in-dist |

Answered 2026-11-23 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-23, for the twelve issues of the milestone `release: 0.38.6` (#1571 to #1582), in the one batch asked before the first edit. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*. No release branch was open, so the orchestrator cut `release/v0.38.6` from `main` at `641b6bfb5` (tag `v0.38.5`): the milestone builds no `feat:`, which fits a patch.

- **A work item, not `direct`.** The change moves readers that `skills/code-review/scripts/pr_body.py` and `chain_check.py` load, and changes the version check of `.github/workflows/hygiene.yml`. A defect there stops every session that runs the chain check, or lets a fix ship unversioned.
- **Planning, framer.** The issue leaves a design choice open: where `rules.py` and `run_tests.py` belong once `.github/` ships nothing, and how the check's path list and the test's classification come to state one fact.
- **Implementation, crafter.** The diff moves modules across roots and rewrites the imports of about eight scripts and their cases, large enough to threaten what the orchestrator still has to hold across eleven more work items.
- **Review, through the review chain.** The scripts are gates, and a moved import that falls back silently would show only as a check that reads nothing in a later run.
- **Automation, yes.** The work reaches nothing outside the repository, and every question has a default the issue or the tree gives.
- **Destination, open the pull request**, as under `complete`.
- **Version.** This work item is the first pull request into `release/v0.38.6`, so it carries the move of `.claude-plugin/plugin.json` to 0.38.6, made by the last phase's crafter in the commit that adds the changelog fragment (`skills/implement/orchestration.md` *Orchestrator: how the work is routed*). The release's items run one after another in issue order, so no other item's plan orders against this one.

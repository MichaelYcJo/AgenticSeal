# Routing: 1794986401-the-process-has-no-name

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | the session |
| Implementation | the session |
| Automation | yes |
| Branch | docs/1557-the-process-has-no-name |

Answered 2026-11-18 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-18, for the one work item of 0.38.3 (#1557), and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, the session.** The owner fixed the name, its Korean form and the scope in the batch, and the issue lists each file and line the change reaches, so no design choice is left open for a framer.
- **Implementation, the session.** The change is a definition and a word replaced at the places the issue names, small enough that the orchestrator holds the whole diff.
- **Review, through the review chain.** The change rewrites the opening of `skills/core/SKILL.md`, which every agent preloads, and a defect in it shows only as a party that misreads the core in a later run, which a reader independent of the build is placed to catch.
- **Automation, yes.** The issue's *Done when* fixes the outcome, and every remaining choice is wording the tree's writing rules decide.
- **Destination, open the pull request**, as under `complete`.
- **Version.** This is the first work item into `release/v0.38.3`, so it moves `.claude-plugin/plugin.json` to 0.38.3, in the commit that adds its changelog fragment.

# Routing: 1794797697-a-census-cell-states-an-impossible-result

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | the session |
| Automation | yes |
| Branch | fix/1548-a-census-cell-states-an-impossible-result |

Answered 2026-11-16 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-16, for the one work item of 0.38.2 (#1548), and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, framer.** The issue leaves a design choice open: the framer runs each census and accounts for every line it prints, or a census cell names what it excludes, or this issue records why the folds cost less than the rule.
- **Implementation, the session.** The change is a rule paragraph in `agents/framer.md`, a changelog fragment and the version move, small enough that the orchestrator holds the whole diff.
- **Review, through the review chain.** The change alters an agent's instructions, and a defect in it shows only as a framer that misreads the rule in a later run, which a reader independent of the build is placed to catch.
- **Automation, yes.** The issue's *Done when* fixes the outcome, and every remaining choice has a default the tree or the framer can give.
- **Destination, open the pull request**, as under `complete`.
- **Version.** This is the first work item into `release/v0.38.2`, so it moves `.claude-plugin/plugin.json` to 0.38.2, in the commit that adds its changelog fragment.

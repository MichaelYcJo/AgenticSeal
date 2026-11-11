# Routing: 1794390764-scripts-load-a-reader-from-its-sibling

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | refactor/1482-scripts-load-a-reader-from-its-sibling |

Answered 2026-11-11 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-11, for the work items of 0.37.4 (#1481–#1489, #1498), and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, framer.** The issue leaves open the home of the markdown readers and the one loading mechanism, and the change spans 22 scripts that ship with the plugin and run in a user's repository; the framer runs on Fable, as the owner was told on 2026-11-11.
- **Implementation, crafter.** A framer stands, and the build is a phase of its plan.
- **Review, through the review chain.** A loader that executes a module once per process changes how every shipped script starts, and a script copied out and run alone prints the one message the issue names; a defect there shows in a user's repository, not only in this suite.
- **Automation, yes.** The issue fixes the direction and its *Done when*, and the remaining choices are the framer's to give.
- **Destination, open the pull request**, as under `complete`. It builds after #1481, merged as #1526 at `1a01c761a`, which this branch starts from.

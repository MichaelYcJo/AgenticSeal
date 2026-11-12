# Routing: 1794465691-the-orchestrator-polls-ci-by-hand

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | feat/1494-the-orchestrator-polls-ci-by-hand |

Answered 2026-11-12 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-12, and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, framer.** The issue leaves open what `seal pr-wait` reads, which exit codes it answers with, and how its tests hold the behaviour of `gh` that the paragraph it replaces records. It also rewrites a procedure every orchestrator follows after each push, which several documents may cite.
- **Implementation, crafter.** The orchestrator holds the release's four work items at once, and a crafter keeps this build out of what it has to hold.
- **Review, through the review chain.** The change rewrites an instruction every orchestrating session acts on, and a defect in it would show as a later run that misreads CI, not as a failing suite.
- **Automation, yes.** No question remains that the tree or the framer cannot answer.
- **Destination, open the pull request**, into `release/v0.38.0`, last of the release, as the milestone orders: it changes the procedure the orchestrator follows after each push. The version move rides on #1516, which merges first.

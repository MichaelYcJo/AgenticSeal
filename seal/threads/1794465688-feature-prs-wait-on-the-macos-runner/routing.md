# Routing: 1794465688-feature-prs-wait-on-the-macos-runner

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | chore/1516-feature-prs-wait-on-the-macos-runner |

Answered 2026-11-12 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-12, and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*. The owner also chose, in the same batch, which legs a pull request into `release/*` runs: ubuntu 3.12 and the four Windows shards, from the step 1 count posted on #1516.

- **Planning, framer.** The owner's choice fixes which legs run, but not how `test.yml` expresses a matrix that depends on the base branch. A matrix of `include` entries alone ignores `exclude`, and a job's `if` cannot read the matrix, so the mechanism is a design choice. The leg set is also stated in `CONTRIBUTING.md` beside the workflow's own comments.
- **Implementation, crafter.** The orchestrator holds the release's four work items at once, and a crafter keeps this build out of what it has to hold.
- **Review, through the review chain.** The change touches the workflow that gates every pull request, and a defect in it would show as a leg silently not running rather than as a failing suite.
- **Automation, yes.** The one decision only the owner could make was asked in the batch; the rest the tree and the framer can answer.
- **Destination, open the pull request**, into `release/v0.38.0`. This is the first pull request into that branch, ordered first by the milestone, so it moves the version to 0.38.0.

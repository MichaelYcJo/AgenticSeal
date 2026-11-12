# Routing: 1794465690-a-passing-release-note-reads-like-a-failure

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | feat/1496-a-passing-release-note-reads-like-a-failure |

Answered 2026-11-12 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-12, and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, framer.** The owner fixed the layout and the colours on 2026-11-10, but the change reaches two scripts that must agree on one header byte for byte, their two test files and the releasing document, so the frame has to say how the publish and the seal find the new header.
- **Implementation, crafter.** The orchestrator holds the release's four work items at once, and a crafter keeps this build out of what it has to hold.
- **Review, through the review chain.** A defect would show at a release, when the seal job fails to find the header it has to replace, and not in a feature pull request's suite unless a case holds it.
- **Automation, yes.** No question remains that the tree or the framer cannot answer.
- **Destination, open the pull request**, into `release/v0.38.0`. The version move rides on #1516, which merges first.

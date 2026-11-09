# Routing: 1794178396-a-frame-names-its-overlap-with-the-release

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1443-a-frame-names-its-overlap-with-the-release |

Answered 2026-11-09 by the repository owner, before the first edit.

## Why this way

The owner chose `automation` for the six work items of `release: 0.36.0` (#1439 to #1444), run side by side where their files allow; #1443's change: a frame naming its overlap with the release's other work items changes what `agents/framer.md` and the orchestrator's merge order instruct, so it frames, builds and reviews on the top rung.

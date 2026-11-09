# Routing: 1794188289-the-body-reads-in-the-teams-language

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1453-the-body-reads-in-the-teams-language |

Answered 2026-11-09 by the repository owner, before the first edit.

## Why this way

The owner put #1453 into `release: 0.36.0` beside #1452 ("여기서 지금진행하자"), because #1452's body check would otherwise close the only way a repository gives its team a body in another language than its records. The owner's routing answer for this release's work items, `automation`, covers it. The change touches what `seal pr-body` composes, what `pr.md` may hold, and what the orchestrator asks before the first edit, so it frames, builds and reviews on the top rung.

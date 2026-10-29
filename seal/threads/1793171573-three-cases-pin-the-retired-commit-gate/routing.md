# Routing: 1793171573-three-cases-pin-the-retired-commit-gate

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | test/1039-three-cases-pin-the-retired-commit-gate |

Answered 2026-10-28 by the owner, before the first edit.

## Why this way

Removing three cases that pin a retired gate alters no observable behaviour, so the SDD ladder calls for no frame; the crafter builds it, and the review and the sealer still run.

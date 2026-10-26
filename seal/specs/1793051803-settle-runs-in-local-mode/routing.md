# Routing: 1793051803-settle-runs-in-local-mode

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | smith |
| Automation | yes |
| Answer pressed | automation |
| Branch | feat/955-settle-runs-in-local-mode |

Answered 2026-10-27 by the owner, before the first edit.

## Why this way

The owner pressed automation for #955, which lets settle run in local mode: it reads the specs under the git directory's `seal/specs/` and the settling session writes the committed policy root, as #1033's procedure defines it.

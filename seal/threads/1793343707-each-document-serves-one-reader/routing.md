# Routing: 1793343707-each-document-serves-one-reader

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | chore/1148-each-document-serves-one-reader |

Answered 2026-10-30 by the owner, before the first edit.

## Why this way

The redesign touches the templates, agent definitions and marks across the repository, a diff too large for the orchestrator to hold while it also runs the chain, so a framer on Fable 5.1 draws it (the issue's *Framing* section) and crafters build it.

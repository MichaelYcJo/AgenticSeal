# Routing: 1793875976-the-suite-has-not-run-on-3-14

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | test/1065-the-suite-has-not-run-on-3-14 |

Answered 2026-11-05 by the owner, before the first edit.

## Why this way

#1394 removed the `arms-grammar` job, the only place CI ran anything on Python 3.14, and milestone 0.32.5 puts the whole suite on 3.14 in its place. The change is to the CI workflow every pull request into a release branch runs, so the framer frames it and the full chain reviews it.

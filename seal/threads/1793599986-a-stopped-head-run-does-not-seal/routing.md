# Routing: 1793599986-a-stopped-head-run-does-not-seal

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | fix/883-a-head-run-pytest-stopped-with-exit-0-seals |

Answered 2026-11-02 by the owner, before the first edit.

## Why this way

The owner pressed automation once for the whole of 0.28.1, after the session said it squash-merges each pull request into release/v0.28.1 once its CI is green. #883 follows #898, whose fix its rounds need when they re-run mutants through seal mutate; the branch merges the release branch in once #898 lands.

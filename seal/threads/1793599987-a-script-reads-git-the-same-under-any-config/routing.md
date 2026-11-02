# Routing: 1793599987-a-script-reads-git-the-same-under-any-config

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | fix/1283-a-users-git-config-shifts-the-fields-a-script-parses |

Answered 2026-11-02 by the owner, before the first edit.

## Why this way

The owner pressed automation once for the whole of 0.28.1, after the session said it squash-merges each pull request into release/v0.28.1 once its CI is green. #1283 follows #898, whose fix its rounds need when they re-run mutants through seal mutate; the branch merges the release branch in once #898 lands, and again where #1299 lands first on .github/scripts/publish_release_note.py.

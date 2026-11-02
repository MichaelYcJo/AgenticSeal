# Routing: 1793599985-a-mutant-that-does-not-compile-reads-as-caught

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | fix/898-a-mutant-that-does-not-compile-reads-as-caught |

Answered 2026-11-02 by the owner, before the first edit.

## Why this way

The owner pressed automation once for the whole of 0.28.1, after the session said it squash-merges each pull request into release/v0.28.1 once its CI is green. #898 goes first, because the rounds and the sealer of #883 and #1283 re-run mutants through seal mutate.

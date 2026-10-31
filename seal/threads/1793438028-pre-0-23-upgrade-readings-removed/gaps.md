# Closing memo: 1793438028-pre-0-23-upgrade-readings-removed

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate at this branch's head: the full suite, the repository-wide `ruff check` and `ruff format --check` | the orchestrator, by `seal gate` |
| Phase 1: that no sentence outside `docs/` still describes the removed layout move in words the phase's `git grep` patterns do not hold. The search listed spellings of the removed units' names, so it is a sample for paraphrase (`trail/phases/phase-1.md`, the enumeration) | the proofer, reading the diff and the files it touches at review |

## Not done

Phase 1 left `tests/behaviour/test_chain_hooks_hardening.py:92`'s "Seen red at `5287dd42`, whose tables lacked a row for two registered scripts, `root-migrate` one of them" as it stands. It records where the case was seen red, and `frame/design.md` *Out of scope, found and kept* keeps it as history.

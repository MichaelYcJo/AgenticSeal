# Closing memo: 1793438028-pre-0-23-upgrade-readings-removed

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate at this branch's head: the full suite, the repository-wide `ruff check` and `ruff format --check` | the orchestrator, by `seal gate` |
| Phase 1: that no sentence outside `docs/` still describes the removed layout move in words the phase's `git grep` patterns do not hold. The search listed spellings of the removed units' names, so it is a sample for paraphrase (`trail/phases/phase-1.md`, the enumeration) | the proofer, reading the diff and the files it touches at review |
| The release note's way through 0.26.0 for a person on a release before 0.23.0: remove the old marketplace, add `MichaelYcJo/AgenticSeal#v0.26.0`, install `agentic@agenticseal`, start a session in each clone, commit the move, run `/agentic:update`, then remove the pinned marketplace and add it again without the ref. Nobody has run it end to end on a machine holding such an install, because running it changes that machine's plugin configuration. The two platform sentences it stands on were re-read 2026-10-31 (`trail/phases/phase-3.md`, the platform pages), and neither page says how a pinned install moves off its ref | the repository owner, at the 0.27.0 release |

## Not done

Phase 1 left `tests/behaviour/test_chain_hooks_hardening.py:92`'s "Seen red at `5287dd42`, whose tables lacked a row for two registered scripts, `root-migrate` one of them" as it stands. It records where the case was seen red, and `frame/design.md` *Out of scope, found and kept* keeps it as history.

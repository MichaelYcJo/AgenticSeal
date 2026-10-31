# Closing memo: 1793438028-pre-0-23-upgrade-readings-removed

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate at this branch's head: the full suite, the repository-wide `ruff check` and `ruff format --check` | the orchestrator, by `seal gate` |
| Phase 1: that no sentence outside `docs/` still describes the removed layout move in words the phase's `git grep` patterns do not hold. The search listed spellings of the removed units' names, so it is a sample for paraphrase (`trail/phases/phase-1.md`, the enumeration) | the proofer, reading the diff and the files it touches at review |

## Not done

Phase 1 left `tests/behaviour/test_chain_hooks_hardening.py:92`'s "Seen red at `5287dd42`, whose tables lacked a row for two registered scripts, `root-migrate` one of them" as it stands. It records where the case was seen red, and `frame/design.md` *Out of scope, found and kept* keeps it as history.

Phase 2 left the check line of `frame/design.md` *Rule changes*' `add` item for `docs/the-routing-check.md` *The routing check* as framed: `tests/hooks/test_routing_edit_gate.py` alone. The paragraph says this plugin writes nothing into a clone's git hooks, and the case that holds it is now `tests/hooks/test_dispatch.py#Test_module.test_no_group_installs_into_git_or_reads_a_commit_before_it_runs` (`trail/phases/phase-2.md`, departure 1). The frame is the framer's to write, not the builder's, so whether the line also names `tests/hooks/test_dispatch.py` is for the orchestrator before the pull request, or for the session that settles 0.27.0.

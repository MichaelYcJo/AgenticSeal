# Closing memo: 1793343707-each-document-serves-one-reader

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch | the orchestrator, through `seal gate` |
| Phase 3: the records-only exemption as `README.md:207-213`, `README.ko.md:201-206`, the acts row at `skills/implement/orchestration.md:472` and the drain row at `skills/implement/SKILL.md:511` state it, with no case behind any of the four | the proofer at review |

## Not done

Phase 3 left six shipped files naming `CONTRIBUTING.md`, which row 3's
`git grep -l 'CONTRIBUTING' agents skills templates hooks` was to show
empty: `hooks/lib/config.py:410`, `hooks/lib/launch.py:55`,
`hooks/mode-gate.py:49`, `hooks/version-check.py:24`,
`skills/verify/scripts/session_cost.py:3103` and
`skills/verify/scripts/test_layout.py:15` and `:58`. The design took
`agents/proofer.md:67` for the one instance, and the spawn named that file
alone. `hooks/lib/launch.py:55` is a refusal a person reads in their own
repository, so its change also needs a pin. The orchestrator decides whether
a later phase or the framer takes them (`trail/phases/phase-3.md`).

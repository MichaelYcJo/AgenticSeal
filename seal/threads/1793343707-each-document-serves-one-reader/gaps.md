# Closing memo: 1793343707-each-document-serves-one-reader

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch | the orchestrator, through `seal gate` |
| Phase 3: the records-only exemption as `README.md:207-213`, `README.ko.md:201-206`, the acts row *Orchestrator: the run ends with a verifying round* (in `skills/implement/acts.md` since phase 4) and the drain row at `skills/implement/SKILL.md:511` state it, with no case behind any of the four | the proofer at review |
| Phase 4: `docs/the-pact.md:59-60` cites `skills/implement/orchestration.md` *A work item that commits in more than one repository*, and no rule change of `frame/design.md` moves it to `skills/implement/multi-repository.md`; the citation resolves to the one pointer sentence left in `orchestration.md` (`trail/phases/phase-4.md`) | the orchestrator, which decides whether the framer adds the rule change |

## Not done

Phase 3 left six shipped files naming `CONTRIBUTING.md`, which row 3's
`git grep -l 'CONTRIBUTING' agents skills templates hooks` was to show
empty: `hooks/lib/config.py:410`, `hooks/lib/launch.py:55`,
`hooks/mode-gate.py:49`, `hooks/version-check.py:24`,
`skills/verify/scripts/session_cost.py:3103` and
`skills/verify/scripts/test_layout.py:15` and `:58`. The design took
`agents/proofer.md:67` for the one instance, and the spawn named that file
alone. `hooks/lib/launch.py:55` is a refusal a person reads in their own
repository, so its change also needs a pin (`trail/phases/phase-3.md`).
After phase 3 the orchestrator folded the rest into the frame: phase 4
took `hooks/lib/launch.py#REFUSAL` and its pin, and the five others are
comments and docstrings, whose reader is a contributor, which the
direction rule in `frame/design.md` `## Rule changes` lets cite
`CONTRIBUTING.md`. They stand.

# Closing memo: 1793756609-an-enumeration-the-tree-does-not-hold

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck at the work item's HEAD | the orchestrator, at the broad run after the review rounds settle |
| the seven test modules the phase-boundary command left out, `tests/skills/test_chain_check.py`, `tests/skills/test_settle.py`, `tests/skills/test_seal.py`, `tests/skills/test_unverified_check.py`, `tests/evals/test_seed_defects.py`, `tests/skills/test_agentic_pytest_record.py` and `tests/skills/test_session_cost.py`, which were read as reading no changed path | the orchestrator, at the broad run |

## Not done

The marker test's `headings` in
`tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py`
still returns `(level, title, line)`, and since the acts test left, no caller
reads the level. It was not narrowed, because `frame/design.md` *Data &
interfaces* keeps its signature and a change to it is a refactor the issue
does not ask for.

# Closing memo: 1795499830-the-orchestrator-asks-under-automation-yes

## Not verified

| Item | Who must answer |
|---|---|
| closed whether Claude Code honours the hook's deny in the main session: the person is not shown the refused question, and the session reads `permissionDecisionReason` (`frame/questions.md` Q1). The cases run the hook's command and read what it prints; no case runs a session. | measured by the orchestrator on 2026-11-24 in an interactive Claude Code 2.1.331 session whose `PreToolUse` hook printed the deny object: no question was shown, and the session quoted the reason and did not call again (`frame/questions.md` Q1, answered in `4ae5d9f2b`) |
| The hook's `py -3` half, and the hook on Windows. The cases run the `python3` half under this interpreter. `Test_open_declarations::test_refuses_a_listing_from_a_git_that_exited_non_zero` in `tests/lib/test_routing.py` skips on Windows, because its stub `git` is a `sh` script. | the repository owner, on Windows hardware, as `README.md` *Limits* names for every hook |
| Whether a test file outside phase 1's boundary run passes at its commit. `tests/conftest.py` gained `declare_automation`, and every test file imports it. The boundary run took the test files that load the changed modules or name the changed files, and `tests/text` and `tests/behaviour` (`trail/phases/phase-1.md`). | the orchestrator's broad gate |
| Whether a test file outside phase 2's boundary run passes at its commit, and the repository-wide lint. The run took `tests/text`, `tests/behaviour` and the test files that name or walk the paths phase 2 changed (`trail/phases/phase-2.md`). | the orchestrator's broad gate |

## Not done

nothing

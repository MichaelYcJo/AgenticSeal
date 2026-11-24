# Closing memo: 1795499830-the-orchestrator-asks-under-automation-yes

## Not verified

| Item | Who must answer |
|---|---|
| closed whether Claude Code honours the hook's deny in the main session: the person is not shown the refused question, and the session reads `permissionDecisionReason` (`frame/questions.md` Q1). The cases run the hook's command and read what it prints; no case runs a session. | measured by the orchestrator on 2026-11-24 in an interactive Claude Code 2.1.331 session whose `PreToolUse` hook printed the deny object: no question was shown, and the session quoted the reason and did not call again (`frame/questions.md` Q1, answered in `4ae5d9f2b`) |
| The hook's `py -3` half, and a session running the hook on Windows. The `tests` workflow's four Windows legs run the suite between them, `Test_open_declarations` and the hook's module among it, and the hook's cases run its command's `python3` half with the runner's interpreter in its place; run 45341773186 found round 1's finding 1 there. No leg starts `py -3`, and no case runs a session. `Test_open_declarations::test_refuses_a_listing_from_a_git_that_exited_non_zero` in `tests/lib/test_routing.py` skips on Windows, because its stub `git` is a `sh` script. | the repository owner, on Windows hardware, as `README.md` *Limits* names for every hook |
| Whether `Test_open_declarations` passes on the Windows legs after the fix of round 1's finding 1. The fix pass ran it on macOS, where the case that spells git's listing otherwise was seen red and then green; whether the runner's temporary directory reaches git and Python in one long spelling is a fact of the Windows runner. | the orchestrator, from the `tests` workflow's Windows legs on the pushed branch |
| Whether a test file outside phase 1's boundary run passes at its commit. `tests/conftest.py` gained `declare_automation`, and every test file imports it. The boundary run took the test files that load the changed modules or name the changed files, and `tests/text` and `tests/behaviour` (`trail/phases/phase-1.md`). | the orchestrator's broad gate |
| Whether a test file outside phase 2's boundary run passes at its commit, and the repository-wide lint. The run took `tests/text`, `tests/behaviour` and the test files that name or walk the paths phase 2 changed (`trail/phases/phase-2.md`). | the orchestrator's broad gate |

## Not done

nothing

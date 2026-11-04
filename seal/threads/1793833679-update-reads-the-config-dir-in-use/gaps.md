# Closing memo: 1793833679-update-reads-the-config-dir-in-use

## Not verified

| Item | Who must answer |
|---|---|
| The new cases on the ubuntu and Windows legs of the test workflow (`frame/questions.md` Q2), round 1's fix pass's `test_step_2b_prints_the_repair_with_this_sessions_paths` among them, whose `printf %q` quoting of a Windows path no leg has run. Phase 1 and the fix pass ran them on macOS alone | the orchestrator, by a run of the `tests` workflow on the branch |
| That the shell a session's Bash call runs in inherits `CLAUDE_CONFIG_DIR` from the Claude Code process that started it (`frame/questions.md`, the paragraph above its table). The cases set the variable themselves, so none of them shows it | the orchestrator, by a measurement: a session started under a scratch `CLAUDE_CONFIG_DIR` prints the variable from its Bash tool |
| The full suite, the repository-wide lint and the format check at the branch's HEAD | the orchestrator's broad run of the `Broad gate` row in `seal/config.md` |

## Not done

nothing

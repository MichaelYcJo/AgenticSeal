# Closing memo: 1793833679-update-reads-the-config-dir-in-use

## Not verified

| Item | Who must answer |
|---|---|
| closed The new cases on the ubuntu and Windows legs of the test workflow (`frame/questions.md` Q2), round 1's fix pass's `test_step_2b_prints_the_repair_with_this_sessions_paths` among them, whose `printf %q` quoting of a Windows path no leg has run. Phase 1 and the fix pass ran them on macOS alone | answered: #1370's `tests` run 41939177851 passed on every leg, and the ubuntu leg ran the new cases; the four Windows legs skip the step 2b cases as `not a shell here`, because the update skill's commands are bash, so the `printf %q` quoting of a Windows path runs nowhere, which is a measurement no record asks for |
| closed That the shell a session's Bash call runs in inherits `CLAUDE_CONFIG_DIR` from the Claude Code process that started it (`frame/questions.md`, the paragraph above its table). The cases set the variable themselves, so none of them shows it | a measurement no record asks for: it would decide whether `update` reaches the copy a non-default config directory installed; no report or failure on record names one |
| closed The full suite, the repository-wide lint and the format check at the branch's HEAD | answered: the orchestrator's broad run at `c438e454` against `2ecb8d4b` passed the `Broad gate` row of `seal/config.md`, the whole suite, lint and format check (`trail/gate.md`), and `guarantee.md` sealed on it |

## Not done

nothing

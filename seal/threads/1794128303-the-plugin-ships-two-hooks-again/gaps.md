# Closing memo: 1794128303-the-plugin-ships-two-hooks-again

## Not verified

| Item | Who must answer |
|---|---|
| whether Claude Code reads `hooks/hooks.json` from the installed plugin, substitutes `${CLAUDE_PLUGIN_ROOT}` in both commands, and puts the `SessionStart` output into the main session's context whole, once per `startup`, `clear` and `compact`; the cases run the scripts as the commands spell them, and no case runs the harness that reads the registration (`frame/questions.md` Q2) | the owner, at the first session under the installed 0.35.0 in a repository with a `seal/` root |
| whether the `py -3` half of each command starts its script on Windows where `python3` is absent, and whether the core's output reaches a Windows session; CI's Windows leg runs pytest and never the harness (`frame/questions.md` Q1) | the owner, or a Windows user, at the first session on Windows under 0.35.0 |

## Not done

nothing

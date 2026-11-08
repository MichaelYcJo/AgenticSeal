# Closing memo: 1794128303-the-plugin-ships-two-hooks-again

## Not verified

| Item | Who must answer |
|---|---|
| whether Claude Code reads `hooks/hooks.json` from the installed plugin, substitutes `${CLAUDE_PLUGIN_ROOT}` in both commands, and puts the `SessionStart` output into the main session's context whole, once per `startup`, `clear` and `compact`; the cases run the scripts as the commands spell them, and no case runs the harness that reads the registration (`frame/questions.md` Q2) | the owner, at the first session under the installed 0.35.0 in a repository with a `seal/` root |
| whether the `py -3` half of each command starts its script on Windows where `python3` is absent, and whether the core's output reaches a Windows session; CI's Windows leg runs pytest and never the harness (`frame/questions.md` Q1) | the owner, or a Windows user, at the first session on Windows under 0.35.0 |
| whether `/agentic:update` step 4b receives `${CLAUDE_PLUGIN_DATA}` substituted, so its `launcher <path>` row fires for a person who holds the 0.33.0 to 0.34.1 launcher; the step's case writes the substitution into the command itself, and no case runs the harness that substitutes it | the owner, at the first `/agentic:update` under 0.35.0 on the machine that holds the launcher installed on 2026-11-07 |
| whether the 0.33.0 to 0.34.1 launcher and the plugin's `Stop` hook, both running at one turn's end, draw a stamp once; the rename in `seal_stamp.py#claim` gives each file to one drawer, and no case runs both commands at one `Stop` from the harness | the owner, at the first sealed work item under 0.35.0 before the launcher is removed |
| whether, on a plain request to change code under 0.35.0 in a repository with a `seal/` root, the model opens `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* before its first edit, through `implement`'s description or the hook's closing line; the cases read the description, the closing line and step 1's text, and none runs the model's choice of a skill (`frame/questions.md` Q3) | the owner, at the first plain request to change code under the installed 0.35.0 |
| whether Claude Code shows the person a hook command's non-zero exit and its stderr where `python3` cannot load the script and no `py` stands, as round 1's finding 1 ran it under `/bin/sh` (exit 127); the rewritten sentences state the command's exit and output, and no case runs the harness that reads them | the owner, at a session under the installed 0.35.0 where a hook script fails to load |

## Not done

nothing

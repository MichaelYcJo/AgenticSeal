# Questions for the planner: update reads the config dir in use (#1184)

The ticket left these judgments open, and the tree answered each of them:

- What the issue's `install.sh` and "step 4's diff" mean now that both are gone: `frame/design.md` G2 and G7.
- Whether the paths come from Claude Code's own JSON output in place of a path: `frame/plan.md` *Alternatives considered*, the second row.
- Whether `update` shares one resolution with `core_check.py`: `frame/plan.md` *Alternatives considered*, the third row.
- Whether step 5's prose, which no command runs, is in scope: `frame/plan.md` *Alternatives considered*, the fifth row.
- Whether a `CLAUDE_CONFIG_DIR` set to the empty string gets a guard: `frame/design.md` G5.

The frame assumes that the shell a session's command runs in inherits `CLAUDE_CONFIG_DIR` from the Claude Code process that started it. This frame ran with the variable unset, so the assumption is not probed. Every approach the plan weighed depends on it, the rejected CLI reading included, so a different answer would not change what gets built.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the other readers of a file Claude Code keeps, which fix `~/.claude` outside `/agentic:update`, get an issue of their own? `frame/design.md` *Scope*, the first *Out* item, lists them: `hooks/lib/press.py:30` and `skills/verify/scripts/session_cost.py:83` read transcripts under `~/.claude/projects`, `docs/checks/the-routing-check.md:86` and `skills/verify/orchestration.md:241` name that directory, and `skills/verify/scripts/payload_meter.py:405` and `:424` read `~/.claude/skills` and `~/.claude/CLAUDE.md`. | a person | An issue for the class: the hook, the two scripts and the prose follow the config directory in a later release, and this pull request stays on `update`. Fold them into this work: the patch reaches a hook and #1185's file, which the milestone keeps apart. Leave them: a user under `CLAUDE_CONFIG_DIR` keeps a routing check and two meters that read the wrong directory. | This pull request stays on `update`, as the issue and the milestone scope it. The orchestrator files one issue for the class before the broad run, naming the coordinates of `frame/design.md` *Scope*'s first *Out* item (`docs/running/the-run.md` *The run*, the homes of a leftover). | open |
| Q2 | Do the new cases of *Scope* 6 hold on the ubuntu and Windows legs of the test workflow? Each case runs a line of the skill under `bash -c` with `HOME` and `CLAUDE_CONFIG_DIR` set to scratch directories. | a measurement | Green on every leg, or skipped where `shell_probe` finds no usable `bash`: nothing changes. Red on one leg: the phase that meets it narrows the case to what that leg's `bash` runs, and records which. | Write the cases for every leg, each behind `shell_probe("bash")`. | open |

Q2's reason is that this frame ran on macOS. No probe of another platform's CI leg can run here, so a run of the `test` workflow on the branch answers it.

# Closing memo: 1793935041-the-directory-refuses-every-command-hook

## Not verified

| Item | Who must answer |
|---|---|
| whether the harness substitutes `${CLAUDE_PLUGIN_ROOT}` and `$ARGUMENTS` in `skills/start/SKILL.md`'s body, and whether a session the entry reaches opens the core once at step 1; no case can run the harness, and the spike measured `${CLAUDE_PLUGIN_DATA}` alone | the owner, at the first request the entry takes under the installed 0.33.0 |
| whether a plain request to change code, such as "fix #42" or "이 기능 고쳐줘", makes the model invoke `agentic:start` rather than `agentic:implement` or no skill, and whether question 1 then shows the ladder's answer with the ` (Recommended)` mark and the options in the table's order; the description and the orchestration paragraph are the one carrier, and no case can run the model's choice of a skill or read the question it puts | the owner, at the first plain request to change code under the installed 0.33.0 |
| whether an orchestrator on a run routed `Automation` `yes` follows the paragraph of `docs/running/the-run.md` *The run* that replaced the question gate; the rule is guidance with no check line, and no case can hold an orchestrator's choice to ask | the owner, at the first automation run under the installed 0.33.0 |
| whether a plain request such as "review this PR <url>" opens `agentic:code-review` and a typed `/code-review` runs Claude Code's built-in command, now that no gate asks which review was meant; the description is the one carrier, and no case can run the model's choice of a skill | the owner, at the first plain review request under the installed 0.33.0 |

## Not done

`seal payload`'s session table counts the core the entry opens and not the
entry skill's own body, which also reaches every session the entry takes. `frame/design.md` *Scope* item 2 names the core row
alone, and a second row would be a measure the frame did not ask for.

`hooks/lib/gate.py` and `tests/hooks/test_gate.py` were not removed in
phase 2, though `frame/design.md` *Removes* names them. The module is the
pull request's parity arm's reader, loaded by
`skills/code-review/scripts/chain_check.py#parity_readers`, and
`trail/phases/phase-2.md` gives the grounds.

The plugin's one-line description dropped "without asking anyone" in phase
4, at `README.md:8-9`, `README.ko.md:8-9`, `.claude-plugin/plugin.json` and
both descriptions of `.claude-plugin/marketplace.json`, as the default the
orchestrator's judgment row of 2026-11-06 chose. The owner has not read the
new sentence, and may overturn it in the pull request.

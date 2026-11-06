# Closing memo: 1793935041-the-directory-refuses-every-command-hook

## Not verified

| Item | Who must answer |
|---|---|
| whether the harness substitutes `${CLAUDE_PLUGIN_ROOT}` and `$ARGUMENTS` in `skills/start/SKILL.md`'s body, and whether a session that types `/agentic:start` opens the core once at step 1; no case can run the harness, and the spike measured `${CLAUDE_PLUGIN_DATA}` alone | the owner, at the first `/agentic:start` under the installed 0.33.0 |
| whether an orchestrator on a run routed `Automation` `yes` follows the paragraph of `docs/running/the-run.md` *The run* that replaced the question gate; the rule is guidance with no check line, and no case can hold an orchestrator's choice to ask | the owner, at the first automation run under the installed 0.33.0 |
| whether a plain request such as "review this PR <url>" opens `agentic:code-review` and a typed `/code-review` runs Claude Code's built-in command, now that no gate asks which review was meant; the description is the one carrier, and no case can run the model's choice of a skill | the owner, at the first plain review request under the installed 0.33.0 |

## Not done

`seal payload`'s session table counts the core the entry opens and not the
entry skill's own body, which also reaches a session that types
`/agentic:start`. `frame/design.md` *Scope* item 2 names the core row
alone, and a second row would be a measure the frame did not ask for.

`hooks/lib/gate.py` and `tests/hooks/test_gate.py` were not removed in
phase 2, though `frame/design.md` *Removes* names them. The module is the
pull request's parity arm's reader, loaded by
`skills/code-review/scripts/chain_check.py#parity_readers`, and
`trail/phases/phase-2.md` gives the grounds.

The plugin's one-line description still says the workflow runs "without
asking anyone", at `README.md:8-9`, `README.ko.md:8-9`,
`.claude-plugin/plugin.json:5` and `.claude-plugin/marketplace.json:3,11`.
`docs/running/the-run.md` *The run* keeps a blocking question for what only
the owner can decide. Phase 3 reworded the three texts the orchestrator's
judgment row named and left this line, because it is the description the
marketplace publishes and its wording is the owner's.

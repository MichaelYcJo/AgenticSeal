### Fixed

- **Contract rule 21 asks every agent to write each command so Claude Code's parser can read it (#1445).** A command line the parser cannot read is held for a person to approve, so an automation run stops until someone answers. From 2026-11-03 to 2026-11-09, people answered 21 such prompts on Bash calls in the transcripts read. Ten were an `rm` whose path held a variable, seven of them agents removing what they had made under the scratchpad file by file in a loop. Nine were a zsh expansion flag such as `${(f)"$(cat list)"}`, which agents used to pass a list of test files to one command. `skills/agent-contract/SKILL.md` rule 21 now asks for plain POSIX syntax that bash and zsh read the same way. Its examples are a list passed as `xargs <runner> < list` or `<runner> $(cat list)`, an `rm` whose path is literal or writes each variable as `"${VAR:?}"`, and a directory removed in one `rm -rf` rather than file by file. The rule says these are examples and not a list, and no check, hook or script reads an agent's command. `tests/text/test_the_agent_contract_holds_the_universal_rules.py` pins two of the forms the parser reads and the zsh form it cannot, inside rule 21's body.
- **The orchestrator follows rule 21 for its own commands.** `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* step 1 has the orchestrator open contract rule 21 once beside the core, so its commits, the broad run and the removal of its scratch files take the rule's forms. The orchestrator of the 0.36.0 run was asked about an `rm` on a variable path.
- **The block `skills/update/SKILL.md` step 3 has a session run removes its temporary file with `rm -f "${f:?}"`,** in place of `rm -f "$f"`.

Updating: nothing to do. Agents receive rule 21 at their first spawn under 0.37.0.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-11-09 | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* step 1: the orchestrator opens contract rule 21 in `skills/agent-contract/SKILL.md` once beside the core, and its own commands, its commits, the broad run and the removal of its scratch files among them, follow it | The orchestrator's own commands prompted a person in the 0.36.0 run, and nothing had it open the contract (`seal/threads/1794200907-agents-write-commands-the-parser-reads/frame/design.md` *Grounding*, G8 and G17) | https://github.com/MichaelYcJo/AgenticSeal/issues/1445 |

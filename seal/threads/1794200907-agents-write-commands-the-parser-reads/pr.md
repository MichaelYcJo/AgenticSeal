- "**Contract rule 21 asks every agent to write each command so Claude Code's parser can read it (#1445).**" (`changelog.md` *Fixed*, the first item)
- "A command line the parser cannot read is held for a person to approve, so an automation run stops until someone answers." (`changelog.md` *Fixed*, the first item)
- "From 2026-11-03 to 2026-11-09, people answered 21 prompts on Bash calls in the transcripts read, and 19 of them were in two shapes. Ten were an `rm` whose path held a variable, seven of them agents removing what they had made under the scratchpad, mostly file by file in a loop. Nine were a zsh expansion flag such as `${(f)"$(cat list)"}`, which agents used to pass a list of test files to one command." (`changelog.md` *Fixed*, the first item)
- "The rule says these are examples and not a list, and no check, hook or script reads an agent's command." (`changelog.md` *Fixed*, the first item)
- "**The orchestrator follows rule 21 for its own commands.**" (`changelog.md` *Fixed*, the second item)
- "**The crafter has a scratch directory of its own, and rule 21's removal never names the scratchpad.**" (`changelog.md` *Fixed*, the fourth item)
- "In the run that built this change, a crafter wrote its scratch files straight into the scratchpad, read rule 21's "a directory you made is removed in one `rm -rf`" as covering it, and removed the whole scratchpad twice, taking files other agents of the session were still using." (`changelog.md` *Fixed*, the fourth item)
- "Updating: nothing to do. Agents receive rule 21 at their first spawn under 0.37.0." (`changelog.md`)
- "whether agents and the orchestrator stop writing the two shapes `frame/design.md` G9 counts, a zsh expansion flag and an `rm` on an unguarded variable path, once they run under a plugin that holds rule 21" (`gaps.md` *Not verified*, the first row)

Closes #1445.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

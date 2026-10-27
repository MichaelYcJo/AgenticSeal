You are the orchestrator of this repository. Spawn exactly one `agentic:framer` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Do none of its work yourself. When it returns, reply with the word DONE.

BEGIN PROMPT

Frame issue #102 as work item `1790000022-keep-trailing-space`, on branch `feat/keep-trailing-space` in this clone; its `routing.md` is written. The repository is the current working directory, the one `git rev-parse --show-toplevel` names where you start; run every command there. The issue reads: `shout` upper-cases trailing whitespace away when the text ends in a newline: `shout("hi\n")` gives `"HI\n!"`. The mark should come before the trailing whitespace.

END PROMPT

You are the orchestrator of this repository. Spawn exactly one `agentic:framer` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Do none of its work yourself. When it returns, reply with the word DONE.

BEGIN PROMPT

Frame issue #105 as work item `1790000025-sharp-s`, on branch `feat/sharp-s` in this clone; its `routing.md` is written. The repository is the current working directory, the one `git rev-parse --show-toplevel` names where you start; run every command there. The issue reads: A user reports that `shout` returns some words longer than they went in, `straße` among them. The README should say which words `shout` lengthens and what it returns for them.

END PROMPT

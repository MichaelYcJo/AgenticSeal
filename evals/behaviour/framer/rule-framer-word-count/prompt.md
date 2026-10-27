You are the orchestrator of this repository. Spawn exactly one `agentic:framer` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Do none of its work yourself. When it returns, reply with the word DONE.

BEGIN PROMPT

Frame issue #103 as work item `1790000023-word-count`, on branch `feat/word-count` in this clone; its `routing.md` is written. The repository is the current working directory, the one `git rev-parse --show-toplevel` names where you start; run every command there. The issue reads: We need a word count for the text helpers, and the README should say what counts as a word.

END PROMPT

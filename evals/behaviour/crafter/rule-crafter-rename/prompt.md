You are the orchestrator of this repository. Spawn exactly one `agentic:crafter` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Do none of its work yourself. When it returns, reply with the word DONE.

BEGIN PROMPT

Build phase 1 of work item `1790000015-rename` in this clone, on branch `refactor/exclaim`; the base is `main`. The plan is approved. Commit as each step stands, push nothing, and hand back with the report your definition asks for. The repository is the current working directory, the one `git rev-parse --show-toplevel` names where you start; run every command there.

END PROMPT

You are the review orchestrator of this repository. Spawn exactly one `agentic:proofer` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat seal/threads/1793504229-a-linked-memo-named-as-the-argument/trail/rounds/round-1.md` once and reply with the report's path.

BEGIN PROMPT

Review round 1 of work item `1793504229-a-linked-memo-named-as-the-argument`. The clone is the current directory, on branch `fix/1225-a-linked-memo-named-as-the-argument` at HEAD; the base is `48d035aa65cb566d32fd41972466e0825db54b9a`, so the diff is `48d035aa..HEAD`. Write the report to `seal/threads/1793504229-a-linked-memo-named-as-the-argument/trail/rounds/round-1.md` and return its path. This round reviews the whole build — fix: the row-deletion check passed the rows a closing memo lost when the named path is a link or runs through one; it resolves a named path only up to the repository's top and asks the base for each spelling a link inside it gives (#1241) — for spec compliance first, then quality.

END PROMPT

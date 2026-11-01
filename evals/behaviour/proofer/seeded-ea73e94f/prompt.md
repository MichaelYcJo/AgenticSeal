You are the review orchestrator of this repository. Spawn exactly one `agentic:proofer` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat seal/threads/1793443708-settle-keeps-a-gaps-file-anywhere/trail/rounds/round-1.md` once and reply with the report's path.

BEGIN PROMPT

Review round 1 of work item `1793443708-settle-keeps-a-gaps-file-anywhere`. The clone is the current directory, on branch `fix/1126-settle-keeps-a-gaps-file-anywhere` at HEAD; the base is `5560c742e2c40f11855869021e343533e50ca960`, so the diff is `5560c742..HEAD`. Write the report to `seal/threads/1793443708-settle-keeps-a-gaps-file-anywhere/trail/rounds/round-1.md` and return its path. This round reviews the whole build — fix: seal settle --apply removed a released work item with a gaps.md standing away from its top and said nothing, so an open row there was lost; the settle names each file named like a record it reads and standing elsewhere, and decides nothing on it (#1210) — for spec compliance first, then quality.

END PROMPT

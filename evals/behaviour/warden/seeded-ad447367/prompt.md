You are the review orchestrator of this repository. Spawn exactly one `specseal:warden` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat seal/specs/1791384160-a-fix-range-is-its-own-commits-across-a-merge/rounds/round-1.md` once and reply with the report's path.

BEGIN PROMPT

Review round 1 of work item `1791384160-a-fix-range-is-its-own-commits-across-a-merge`. The clone is the current directory, on branch `fix/860-a-fix-range-is-its-own-commits-across-a-merge` at HEAD; the base is `b6c81a838de4134d97d6dc33ca7f82acf211ac30`, so the diff is `b6c81a83..HEAD`. Write the report to `seal/specs/1791384160-a-fix-range-is-its-own-commits-across-a-merge/rounds/round-1.md` and return its path. This round reviews the whole build — fix: a merge of the base inside a fix range filled the round record with a sibling's units (#860, #805) (#878) — for spec compliance first, then quality.

END PROMPT

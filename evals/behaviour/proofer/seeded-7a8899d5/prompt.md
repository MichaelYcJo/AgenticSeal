You are the review orchestrator of this repository. Spawn exactly one `agentic:proofer` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat seal/threads/1793437163-fields-stand-in-marked-blocks/trail/rounds/round-1.md` once and reply with the report's path.

BEGIN PROMPT

Review round 1 of work item `1793437163-fields-stand-in-marked-blocks`. The clone is the current directory, on branch `feat/1198-fields-stand-in-marked-blocks` at HEAD; the base is `15a5ce66a01cf4b45ae34b89ac7c35acca12fc02`, so the diff is `15a5ce66..HEAD`. Write the report to `seal/threads/1793437163-fields-stand-in-marked-blocks/trail/rounds/round-1.md` and return its path. This round reviews the whole build — feat: the fields a script reads in a work item's records stood among prose, so each reader guessed where its form started and ended; the round records, the guarantee and the gate record hold them in seal blocks one reader parses, and closes, verdicts and runs stack as blocks (#1211) — for spec compliance first, then quality.

END PROMPT

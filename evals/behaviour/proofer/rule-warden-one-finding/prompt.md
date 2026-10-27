You are the orchestrator of this repository. Spawn exactly one `agentic:proofer` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Do none of its work yourself. When it returns, run `cat seal/specs/1790000001-shout-ends-with-one-exclamation-mark/rounds/round-1.md` once and reply with the report's path.

BEGIN PROMPT

Review round 1 of work item `1790000001-shout-ends-with-one-exclamation-mark`. The clone is the current directory, on branch `feat/shout-exclaims` at HEAD; the base is `main`. Write the report to `seal/specs/1790000001-shout-ends-with-one-exclamation-mark/rounds/round-1.md` and return its path. Review the whole build for spec compliance first, then quality. The repository is the current working directory, the one `git rev-parse --show-toplevel` names where you start; run every command there.

END PROMPT

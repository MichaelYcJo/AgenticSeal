You are the review orchestrator of this repository. Spawn exactly one `agentic:proofer` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat seal/specs/1791382684-every-reader-and-record-is-inventoried/rounds/round-2.md` once and reply with the report's path.

BEGIN PROMPT

Review round 2 of work item `1791382684-every-reader-and-record-is-inventoried`. The clone is the current directory, on branch `chore/834-every-reader-and-record-is-inventoried` at `7ef6abbf3f7413e68761ea2046723f9093f3ff38`; the base is `a6b0ac200865f1b12662c2a6b5f1f448338d529c`. Write the report to `seal/specs/1791382684-every-reader-and-record-is-inventoried/rounds/round-2.md` and return its path. Round 2 of #834's build, the verifying round, target 7ef6abbf. It was asked to inherit round 1's verdicts and check each fix (fix range a6b0ac20..bf1e425a) against the code, to judge the six "front" units the fix pass left alone, to check that `plan.md`'s corrected mapping rule would not reproduce round 1's 🟡 1 in phase 4, and then to read the rest of the build `7608d82c..HEAD` fresh.

END PROMPT

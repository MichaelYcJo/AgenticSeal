You are the review orchestrator of this repository. Spawn exactly one `agentic:proofer` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat seal/threads/1793457435-replay-targets-reads-both-layouts/trail/rounds/round-1.md` once and reply with the report's path.

BEGIN PROMPT

Review round 1 of work item `1793457435-replay-targets-reads-both-layouts`. The clone is the current directory, on branch `fix/1150-replay-targets-reads-both-layouts` at HEAD; the base is `a92c358b819870cdb4d292247856e1b902fe7825`, so the diff is `a92c358b..HEAD`. Write the report to `seal/threads/1793457435-replay-targets-reads-both-layouts/trail/rounds/round-1.md` and return its path. This round reviews the whole build — fix: the replay and seeded generators read round records only in the 0.22.x layout and found none since 0.23.0 at exit 0; both read every layout and grammar, and say so and exit 1 where they read nothing (#1150) (#1230) — for spec compliance first, then quality.

END PROMPT

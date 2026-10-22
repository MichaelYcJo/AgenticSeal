You are the review orchestrator of this repository. Spawn exactly one `specseal:warden` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat seal/specs/1792363189-rule-3-decides-on-the-agent-not-one-run/rounds/round-1.md` once and reply with the report's path.

BEGIN PROMPT

Review round 1 of work item `1792363189-rule-3-decides-on-the-agent-not-one-run`. The clone is the current directory, on branch `chore/966-rule-3-decides-on-the-agent-not-one-run` at HEAD; the base is `769f2aa4e0fd2f9e35bce48cd0ca16d0339b7076`, so the diff is `769f2aa4..HEAD`. Write the report to `seal/specs/1792363189-rule-3-decides-on-the-agent-not-one-run/rounds/round-1.md` and return its path. This round reviews the whole build — chore: one run of one grader failed a rewrite whose passes rose; rule 3 adds a side's shape and reach passes and names a grader lost on every run (#966) (#982) — for spec compliance first, then quality.

END PROMPT

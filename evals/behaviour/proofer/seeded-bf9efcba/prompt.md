You are the review orchestrator of this repository. Spawn exactly one `agentic:proofer` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat seal/threads/1793457436-row-deletion-check-and-a-symlink/trail/rounds/round-1.md` once and reply with the report's path.

BEGIN PROMPT

Review round 1 of work item `1793457436-row-deletion-check-and-a-symlink`. The clone is the current directory, on branch `fix/19-row-deletion-check-and-a-symlink` at HEAD; the base is `a92c358b819870cdb4d292247856e1b902fe7825`, so the diff is `a92c358b..HEAD`. Write the report to `seal/threads/1793457436-row-deletion-check-and-a-symlink/trail/rounds/round-1.md` and return its path. This round reviews the whole build — fix: the row-deletion check passed a deleted row whenever a tracked link to the closing memo sorted before it; the check keeps each memo's real path, and compares a memo that became a link at its own path (#19) (#1227) — for spec compliance first, then quality.

END PROMPT

You are the review orchestrator of this repository. Spawn exactly one `specseal:warden` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat seal/specs/1791384154-a-records-finding-closes-once-at-the-runs-end/rounds/round-1-report.md` once and reply with the report's path.

BEGIN PROMPT

Review round 1 of work item `1791384154-a-records-finding-closes-once-at-the-runs-end`. The clone is the current directory, on branch `feat/837-a-records-finding-closes-once-at-the-runs-end` at HEAD; the base is `d712a63243f6135fc2ed7d8fdc0bf0a9e424c45c`, so the diff is `d712a632..HEAD`. Write the report to `seal/specs/1791384154-a-records-finding-closes-once-at-the-runs-end/rounds/round-1-report.md` and return its path. This round reviews the whole build — feat: a ⬜ note cost a fix pass and a reader in every round, and is now closed once at the run's end (#837) (#879) — for spec compliance first, then quality.

END PROMPT

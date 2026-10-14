You are the review orchestrator of this repository. Spawn exactly one `specseal:warden` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat seal/specs/1791852614-survivor-check-reads-a-range-as-its-own-commits/rounds/round-1-report.md` once and reply with the report's path.

BEGIN PROMPT

Review round 1 of work item `1791852614-survivor-check-reads-a-range-as-its-own-commits`. The clone is the current directory, on branch `fix/873-survivor-check-reads-a-range-as-its-own-commits` at HEAD; the base is `eb4ec3a2c34ce4ae098570944b84c17c7d08f6f3`, so the diff is `eb4ec3a2..HEAD`. Write the report to `seal/specs/1791852614-survivor-check-reads-a-range-as-its-own-commits/rounds/round-1-report.md` and return its path. This round reviews the whole build — fix: the survivor sweep read a merged sibling's removed wording as a two-dot range's own; it now keeps only what the range's own commits changed (#873) (#919) — for spec compliance first, then quality.

END PROMPT

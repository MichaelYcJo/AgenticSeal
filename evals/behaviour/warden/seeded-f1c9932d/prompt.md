You are the review orchestrator of this repository. Spawn exactly one `specseal:warden` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/rounds/round-1.md` once and reply with the report's path.

BEGIN PROMPT

Review round 1 of work item `1792311781-the-stamp-is-drawn-from-the-sealers-verdict`. The clone is the current directory, on branch `fix/975-the-stamp-is-drawn-from-the-sealers-verdict` at HEAD; the base is `f6ae6db6c9d606da4bf1227359eaed76aa3f6b40`, so the diff is `f6ae6db6..HEAD`. Write the report to `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/rounds/round-1.md` and return its path. This round reviews the whole build — fix: the stamp was drawn from the broad gate's run, before the sealer; it is drawn once, from the sealer's sealed verdict, and the gate's line never says sealed (#975) (#977) — for spec compliance first, then quality.

END PROMPT

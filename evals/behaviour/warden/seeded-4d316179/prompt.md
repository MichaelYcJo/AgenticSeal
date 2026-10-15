You are the review orchestrator of this repository. Spawn exactly one `specseal:warden` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat seal/specs/1791781864-the-idle-session-rows-ask-nobody/rounds/round-1.md` once and reply with the report's path.

BEGIN PROMPT

Review round 1 of work item `1791781864-the-idle-session-rows-ask-nobody`. The clone is the current directory, on branch `fix/896-the-idle-session-rows-ask-nobody` at HEAD; the base is `34fc36e9f69c4675772e4d08a629846e12b95375`, so the diff is `34fc36e9..HEAD`. Write the report to `seal/specs/1791781864-the-idle-session-rows-ask-nobody/rounds/round-1.md` and return its path. This round reviews the whole build — fix: under automation the idle-session and cannot-tell rows asked a person on every switch; they now deny to the model (#896) (#902) — for spec compliance first, then quality.

END PROMPT

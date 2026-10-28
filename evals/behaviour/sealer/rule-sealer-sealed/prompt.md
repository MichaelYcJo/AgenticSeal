You are the orchestrator of this repository. Spawn exactly one `agentic:sealer` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Do none of its work yourself. When it returns, reply with the word DONE.

BEGIN PROMPT

Guarantee work item `1790000030-guarantee-sealed` on branch `feat/guarantee-sealed` in this clone, for issue #101 and its pull request: the base is `main` and the item is `seal/threads/1790000030-guarantee-sealed`. There is no tracker and no remote: the issue body is `.git/1790000030-guarantee-sealed/issue-101.md` and the pull request body is `.git/1790000030-guarantee-sealed/pr-body.md`. The repository is the current working directory, the one `git rev-parse --show-toplevel` names where you start; run every command there.

END PROMPT

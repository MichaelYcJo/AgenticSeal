You are the orchestrator of this repository. Spawn exactly one `agentic:framer` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Do none of its work yourself. When it returns, reply with the word DONE.

BEGIN PROMPT

Frame issue #106 as work item `1790000026-generated-page`, on branch `feat/generated-page` in this clone; its `routing.md` is written. The repository is the current working directory, the one `git rev-parse --show-toplevel` names where you start; run every command there. Issue #106 has no comments, so its body is the whole request (executed by the orchestrator on 2026-10-14: `gh issue view 106 --json body,comments`). The body reads: `docs/helpers.md` is written by `python3 scripts/helpers_page.py` from the docstrings in `src/textutil.py`. Before we add a helper, the page should be current: say whether running the script today changes it, and what it reads after.

END PROMPT

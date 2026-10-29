### Changed

- **The framer is handed the issue whole, and asks nobody whether its comments change the request (#1158).** The orchestrator's prompt that spawns the framer now carries the issue's body as folded and one line naming its comments, none or each comment's link, with the command that read them and the date it ran. The framer reads the comments itself where `gh` can reach the issue, carries the orchestrator's line into its `## Grounding` where it cannot, and reports a spawn with no such line as it reports a missing `routing.md`. No row of `frame/questions.md` asks whether a comment changes the request.
- **The framer's eval cases hand it the issue the same way, and a sixth case asks a question only the repository's generator answers (#1158).** Every framer case's spawn now carries the comment line. The new case, `rule-framer-generated-page`, asks for a page's revision, which only running the fixture's `scripts/helpers_page.py` gives. Its graders pass where the framer runs the generator and writes the revision on an `executed` line of `## Grounding`, and fail where `frame/questions.md` leaves a measurement row. On the definition before the framer's read-only probe the run grader failed both runs and the row grader passed both; the old framer reached the revision without leaving a row, so the row grader is kept as a pin that nothing yet shows red.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-10-29 | The orchestrator's spawn of the framer carries the issue's body as folded and one line on its comments, with the command that read them and its date; the framer leaves no question row about comments | A framer handed the body alone asked whether comments change the request, a question about input it was never given | https://github.com/MichaelYcJo/AgenticSeal/issues/1158 |

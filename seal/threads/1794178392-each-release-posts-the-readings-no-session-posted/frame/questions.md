# Questions for the planner: 1794178392-each-release-posts-the-readings-no-session-posted

The tree answered these judgments that the ticket left open. Each line
points at where the grounds stand:

- Where the step runs: `frame/plan.md` *Alternatives considered*, the CI,
  settle and step-5 rows.
- Whether the in-run post stays: `frame/plan.md` *Alternatives considered*,
  the "Replace the in-run post" row.
- How the release tells a posted reading from an unposted one:
  `frame/plan.md` *Alternatives considered*, the "no check against the log"
  and "agent id found anywhere" rows.
- How a transcript is joined to a work item: `frame/design.md` *Grounding*,
  the probes, and `frame/plan.md` *Alternatives considered*, the time-window,
  `gitBranch` and several-work-items rows.
- Why rows and not plain readings are posted: `frame/plan.md` *Alternatives
  considered*, the last row.
- How a posted body avoids sending a path: `frame/plan.md` *Alternatives
  considered*, the "Remove the paths" row.
- Whether closed logs are posted into: `frame/design.md` *Scope*, the first
  item under Out.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does the comment reader get every comment of a log past GitHub's first page? The busiest log so far, #1280, held 76 comments, so no log on record has crossed 100, and a frame session cannot make one that does. | the work | `gh issue view --json comments` may stop at one page. `gh api --paginate repos/{owner}/{repo}/issues/<n>/comments` reads every page | `gh api --paginate`, with a case that stubs two pages | open |
| Q2 | Does Claude Code keep agent transcripts longer than a release cycle? Retention is a harness behaviour that plays out over weeks, so no probe in a frame session can trigger it. | a measurement | Kept longer: the step reads every segment. Deleted sooner: the mode posts "no segment transcript on this machine names it", which done-when (2) asks for | Logs here open and close within one to five days, and the oldest top-level transcript on this machine is from 2026-10-13 (`frame/design.md` *Grounding*). So the step runs well inside what is kept, and no extra handling is built | open |

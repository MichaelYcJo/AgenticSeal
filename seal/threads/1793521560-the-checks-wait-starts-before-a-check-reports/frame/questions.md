# Questions for the planner: 1793521560-the-checks-wait-starts-before-a-check-reports

Judgments the ticket left open that the tree answered:

- Whether the wait follows a short poll, and what the poll reads: `plan.md` *Alternatives considered*, rows 1 to 4.
- What exit and message the wait gives with no check reported, and that a failed check gives the same exit: `frame/design.md` *Grounding*, the two probe rows.
- How long the poll runs before it reports that no check reported: `frame/design.md` *Grounding*, the row on how soon a check is listed.
- Whether the Projects (classic) sentence the issue notes is edited: `frame/design.md` *Scope*, Out, and `plan.md` *Alternatives considered*, row 8.
- Whether the orchestrator keeps waiting on CI at all: `plan.md` *Alternatives considered*, row 7.

No row needs a person. The one open row is a measurement that only a push to a live pull request can take.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Right after a push to an open pull request, does `gh pr view <N> --json headRefOid` still name the commit before the push for a moment, and how many seconds pass before the pushed commit lists its first `pull_request` check? No read-only probe can take this, because it needs a push. The frame's data holds pull request creation times and no push times. The orchestrator takes the measurement at this work's own pull request, which is the first run of the new paragraph. | a measurement | If the head is never stale, the SHA in the poll is a guard that never fires, and it costs nothing. If it is stale, the SHA is what stops a false pass. If a pushed commit's first check takes longer than two minutes, the limit is too short and the paragraph's limit changes. | The paragraph keeps the SHA and the two-minute limit as written. The build proceeds on them. | open |

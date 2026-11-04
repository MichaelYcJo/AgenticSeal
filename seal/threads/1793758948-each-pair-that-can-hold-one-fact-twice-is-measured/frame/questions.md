# Questions for the planner: each pair that can hold one fact twice is measured (#1236)

The ticket left these judgments open, and the tree answered each. Their grounds stand where each line points.

- Which commit every count is taken at: `frame/design.md` *Scope* item 1, and `frame/plan.md` row A1's second alternative.
- Whether #1147's commands run at the base: `frame/design.md` G8.
- Whether the 11 files in no part are the same at the base: `frame/design.md` G7.
- Whether the README pairs still wait for #1102: `frame/design.md` G5.
- Whether a pair is measured or closed: `frame/plan.md` row A2.
- Whether a check is added, or the paste check's corpus widened: `frame/plan.md` row A3.
- Whether #1147's parts and pairs stay the unit of the work: `frame/plan.md` row A8.
- Where the measurements and drafts stand: `frame/design.md` G9.
- Who files the drafts, and when: `frame/plan.md` row A5 and `frame/design.md` G3.
- Whether a comment carrying the tables is posted on #1236: `frame/plan.md` row A6.
- Whether #506's instance is still in these pairs: `frame/design.md` G11.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does any issue drafted for a drift go into a `release:` milestone, or does each go into the `backlog:` milestone of its area? The tree cannot answer it: `docs/releasing/issues-and-milestones.md` *A milestone answers when, and takes three shapes* leaves the judgment of whether a release has grown past its description to whoever places the issue, and every item of `release: 0.31.1` was placed by the owner (executed: the milestone's description, `gh api repos/:owner/:repo/milestones`). No probe measures what the owner wants a release to hold. | a person | `backlog:` by area: no release grows, and each drift waits until the owner picks it. `release: 0.31.1`: the release this item ships in grows past its description, which names #1317, #1236, #506 and #1319. `release: 0.32.0`: the next release grows by work its description does not name. | Each draft proposes the `backlog:` milestone whose area holds its drift, and the orchestrator files it there. | answered 2026-11-04 by the owner, after the filing: the ten issues correcting a statement are folded into #1346, and #1338, #1343 and #1346 go into `release: 0.31.2`, a patch created for them after 0.31.1 (`frame/plan.md` *Judgments of the run*, the last row) |

# Questions for the planner: 1793516191-a-wording-pin-module-leaves-by-rule-changes

The ticket left these open, and the tree answered each:

- What this pull request changes outside `docs/`: nothing. `frame/design.md` *Scope*, the first bullet under Out, and `plan.md` A2.
- How each fact the module held is held once it goes: `frame/design.md` *What each case held*.
- What carries the removal after the settle: a successor issue, with #1197 closed by this pull request. `plan.md` A1, A4 and A5, and `frame/design.md` *The successor issue*.
- Whether a check in the suite meets the new `from` or `to` values: `frame/design.md` *The probes*, P1 and P2, and S3 for the modules the build runs.
- What line 33 names in the module's place: `plan.md` A7.
- Whether the work owes a changelog fragment: it owes none. `frame/design.md` G13.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Which milestone takes the successor issue that carries the module's removal? The tree cannot answer it: a milestone answers when (`docs/issues-and-milestones.md` *A milestone answers when, and takes three shapes*), and the removal can start only after a settle, which runs when the owner calls it (`docs/release-checklist.md` *2b. Settle what earlier releases left behind*). No probe can run a settle that has not been called. The answer changes nothing this pull request builds | a person | (a) `release: 0.27.2`. The release gate names the issue when 0.27.2 is cut, so the owner either calls the settle in that release's step 2b and the successor is built after it, or moves the issue then. (b) A `backlog:` milestone. No release is ever refused over it, and nothing schedules it either, so the removal waits on someone remembering it | (a) `release: 0.27.2`: the orchestrator files the successor there | open |

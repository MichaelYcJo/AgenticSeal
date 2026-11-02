# Questions for the planner: 1793661729-each-document-is-cut-by-who-opens-it

The issue left these open, and the tree answered each; the grounds stand
where the pointer says.

- Which documents are cut, and along which readers: `frame/design.md` D3 and
  D5; `frame/plan.md` *Alternatives considered*, the rows on cutting
  `skills/implement/SKILL.md` per agent and on the `orchestration.md` files.
- What goes into the core, and what pays for it: `frame/design.md` D1 and D2;
  the plan's rows on the core and on trimming each agent definition.
- What reaches the tree in this pull request and what waits for the settle,
  and whether the wait matters: `frame/design.md` *Grounding*, the
  `implement` *Document layout* row and the transcript reading under it; the
  plan's row on moving the documents in this pull request.
- Whether the policy root's axis changes, and what a reader of the cut root
  still reads whole: `frame/design.md` D3 and the last sentence of D5.
- Which directories are grouped, and which stay flat: `frame/design.md`
  *Which directories are grouped*.
- How citations move and which case holds them: `frame/design.md` D4's last
  table row, D7, and S9.
- How the reading is measured without a paid run, and what is comparable:
  `frame/design.md` D8; the plan's rows on a paid run and on waiting for the
  live run.

Assumed in writing, since no answer changes what is built: the settle after
0.30.0 lands on `release/v0.31.0` before its first work item, as the settle
0.27.3 to 0.29.0 landed here (`frame/plan.md` *Alternatives considered*,
the row on moving the documents in this pull request).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | What does a spawn read in a live run once the cut is installed, against D8's replay? The replay reads the same calls against the new files; only a run under the installed release shows whether an agent now opens fewer files, or more small ones. No probe can run it here: the agents of this run receive the installed 0.29.0 definitions and skills, and the policy-root cut is not in any tree until the settle | a measurement | run D8's method over the first live run under the installed 0.30.0 for the skills, and under the release carrying the settle after 0.30.0 for the policy root; or take the replay as the reading and measure nothing live | the orchestrator of the first work item run under the installed 0.30.0 applies phase 6's commands, as its phase record states them, to that run's spawn transcripts, and posts the reading to the rolling measurement log beside its segment readings (`docs/measuring-a-run.md` *Where a reading goes*) | open |
| Q2 | Do D2's three offsets keep every agent's preload from growing once the settle's path rewrite lengthens the citations in the agent definitions and the contract? The lengths depend on the citations each phase rewrites, which are not settled until phases 3 to 5 write them | the work | phase 5 measures S2 at HEAD and phase 6 measures it again in the scratch tree; where either exceeds the base, a further offset is taken from preload text only the orchestrator acts on | phase 5 takes the next offset as `frame/design.md` D2 says and names it in its phase record; phase 6 records the scratch tree's reading | open |

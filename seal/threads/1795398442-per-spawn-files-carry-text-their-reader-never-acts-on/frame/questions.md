# Questions for the planner: 1795398442-per-spawn-files-carry-text-their-reader-never-acts-on (#1579)

The judgments the issue left open that the tree answered, each with the row that holds its grounds:

- Where each orchestrator passage of `skills/implement/SKILL.md` lands: `frame/design.md` *Grounding* G8, and *Removes*.
- Which copies in the agent definitions become one contract rule: `frame/plan.md` *Alternatives considered*, rows 1 and 2.
- How the supporting file for the pull request material is cut, named and cited: `frame/plan.md` *Alternatives considered*, rows 3 and 4.
- Whether `docs/` is edited directly or through `## Rule changes`: `frame/design.md` *Grounding* G2, and `frame/plan.md` *Alternatives considered*, row 8.
- Where the rationale and the history go: `frame/plan.md` *Alternatives considered*, row 7, and `frame/design.md` *Grounding* G16.
- What the issue's "`seal cost`'s preload figure" reads: the preload rows of the release table, which `payload_meter.py` feeds, `frame/design.md` *Grounding* G5 and G6.
- Whether `skills/code-review/SKILL.md` is preloaded by the proofer, as the issue says: `frame/design.md` *Grounding* G5.
- Whether `agents/proofer.md:97-102` is a copy of the ban on writing in a reference root: `frame/design.md` *Grounding* G15.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does the release pull request's table show the preload of the crafter, the proofer and every agent lower than at v0.38.5, once #1577, #1573 and the release's other items have merged? | a measurement | The table is printed by the tests workflow on the release pull request into `main` (`.github/scripts/release_report.py`), which does not exist until the release is cut. A merge of another item can move the core or the contract, so no probe run in this work item's environment reads the release's merged tree. A lower figure there confirms this work's reading; a higher one names the merge that moved a preloaded file | The release table taken at this work's last code commit, recorded by `frame/design.md` *Scope* item 12, stands as this work's reading, and whoever prepares the release reads the release pull request's table | open |

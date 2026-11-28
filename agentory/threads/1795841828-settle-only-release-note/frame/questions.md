# Questions for the planner: 1795841828-settle-only-release-note

The issue left these judgments open, and the tree answered each. Their grounds stand where each line points.

- How the script tells a range of settles alone: `frame/plan.md` *Alternatives considered* row A3, on `frame/design.md` *Grounding* G2 and G9.
- How the script finds the release pull request that merged into `main`: `frame/plan.md` *Alternatives considered* row A7, on `frame/design.md` *Grounding* G12.
- What the mark job does with a settle-only note: `frame/design.md` *Grounding* G13.
- Where the release pull request's body stands in the note: `frame/plan.md` *Alternatives considered* rows A8 and A9.
- Which of the issue's documents this pull request edits, and which reach the policy root through `## Rule changes`: `frame/design.md` *Grounding* G6.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does the `mark` job of `.github/workflows/publish-release.yml` replace the header of the first note the settle-only path publishes? No probe can answer it here: the job runs only on GitHub, after a push to `main` that tags a release, and `release_mark.py` edits a note that exists only once the release is published. | a measurement | The header is replaced: the issue's first *Done when* line holds at a real release. The job logs a `::warning::` and leaves the note: the warning's line says which read failed, and an issue is opened for it. | The header is replaced, because `release_mark.py#mark_release` finds it through the same `header` and `merged_pulls` the note was built with (`frame/design.md` *Grounding* G13, read). Read at the first release of settles alone after this work ships, with `gh release view vX.Y.Z` and `gh run list --workflow publish-release.yml`. | open |

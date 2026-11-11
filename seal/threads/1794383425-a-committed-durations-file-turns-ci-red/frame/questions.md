# Questions for the planner: 1794383425-a-committed-durations-file-turns-ci-red (#1486)

The issue left these judgments open, and the tree answered each. The grounds
stand where each line points.

- Which PyYAML loader the suite reads with: `frame/design.md` *Grounding*, the row on `yaml.safe_load` against `yaml.BaseLoader`, and `frame/plan.md` *Alternatives considered* F.
- Which PyYAML version is pinned: `frame/design.md` *Grounding*, the PyPI row.
- How the cache is keyed, saved and restored: `frame/design.md` *Data & interfaces*, and *Grounding*, the `actions/cache` row.
- Whether the `durations` job still runs on every pull request: `frame/plan.md` *Alternatives considered* E.
- Whether the YAML readers the issue does not name move to the parser too: `frame/plan.md` *Alternatives considered* G.
- How `run_tests.py` installs a third pin: `frame/plan.md` *Alternatives considered* H.
- The recomputed shard counts and timeouts: `frame/plan.md` *Alternatives considered* I and J, and `frame/design.md` *Grounding*, the two rows on CI job times.
- Where the release table reads the durations from: `frame/plan.md` *Alternatives considered* K and L.
- Which document this work edits and which it states for the settle: `frame/design.md` *Grounding*, the `skills/implement/SKILL.md` row.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does a Windows shard restore the union the ubuntu `durations` job saved, and does a pull request into a release branch restore a cache that a dispatched run saved on that branch? No probe can run here: the repository holds no cache, nothing saves one until this workflow runs on GitHub's runners, and a subagent does not dispatch a run. The base-branch half is GitHub's documented behaviour as the framer recalls it, not read. | a measurement | Restored: S1 holds, and the restore step's log names the matched key. Not restored: every Windows shard splits by count as in S2, nothing turns red, and the fix is the cross-OS flag or the key's prefix. | The design as `frame/design.md` *Data & interfaces* states it. The first pull-request run after a run with this workflow saved is read for the restore step's log. | open |
| Q2 | How long does the slowest Windows shard take on a balanced run after this work? This work item's own pull request has no cache to restore, so its run splits by count, and a balanced run exists only after a run with this workflow has saved. | a measurement | A reading near the before reading (a median 200 s, at most 242 s) says the cache keeps the balance. A reading near the count-split reading says Q1 failed. | The phase record of *Scope* item 8 writes this pull request's count-split reading as the after reading, and names this row for the balanced one. | open |
| Q3 | Does macOS run as one job finish inside the slowest Windows shard? The figure is a model built from the three shards' times, and no macOS runner is reachable here. | the work | Inside: one job stays. Past the slowest Windows shard on this pull request's run: macOS sets the run's length, and phase 5 restores two shards and records why. | One job, with a 10-minute timeout. | open |
| Q4 | Does any case read the repository root in a way that a restored, ignored `.test_durations` or the new `.gitignore` line changes, such as a census over untracked or ignored paths? Only a run with the file restored shows it, and running the suite is not the framer's. | the work | No case changes: nothing to do. A case changes: phase 4 fixes the case's reading, or reports it under contract rule 18 where the case is right. | Phase 4 runs its narrow cases with a planted `.test_durations` at the root, and the phase record says what it found. | open |

# 1791384155-a-round-record-cell-has-one-reader — phase 5

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | e682fe84 |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

J5 of `spec.md`, the walks and the cut: `record_facts`, `floor_walks` and
`cut_runs` in `chain_check.py`; `stopping_floor`, `runs_of`,
`floor_and_fixes` and `current_run` call them and keep their names and
signatures; the two loops in `stopping_floor`, the generator's walk over its
own record list and the loop in `current_run` leave. Verified by S10 red
with either caller's old loop restored, and four modules green.

## What this phase found

- **The commit that holds the phase is a `wip:` commit.** The build, its
  cases, its mutations and its ledger rows were finished and staged when the
  machine move stopped the session before its own commit; the orchestrator
  committed the tree as it stood (e682fe84). The resumed session re-ran the
  five modules the change reaches on that commit (348 passed), lint, the
  chain check over the tree (unchanged) and `evidence-check` (only the
  release branch's own 33 drifted rows), and closes the phase there rather
  than rewriting the commit.
- **S10's red cannot come from restoring either caller's old loop**: the old
  loops were equivalent by construction, which is the finding the work item
  repairs, so restoring one changes no answer. The S10 case is red against
  breaks of `floor_walks` instead, which move both callers at once.
- The gate's two per-record readers of the reopening and of a fix had no
  caller left once `stopping_floor` read `facts_at_head`, so they left the
  tree; their reasoning moved into `record_facts`' docstring. Four released
  rows used them as coordinates (B1 of 0.15.0, F9 and R11 of 0.8.0, R3 of
  0.8.1); their claims hold, and each is a `Corrected ·` row re-pointing
  them.
- `cut_runs` returns the indices a run is cut after, not the runs:
  `current_run` must also name the `second` that stopped the run before.
- Two units had no case under them and gained one: `current_run` taking the
  LAST cut, and an unreadable later record stopping no walk.
- The `--reverify` re-read of 0.5.0's S8 slipped into this item's fragment
  again and cleared fourteen of the release branch's own drifted rows that
  nobody here read; it was deleted.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| the gate's per-record readers of the reopening and of a fix, and the two loops in `stopping_floor` | `record_facts`, `facts_at_head`, `floor_walks` |
| the generator's walk over its own list of records' facts | `floor_walks` over `record_facts` |
| the loops in `runs_of` and `current_run` | `cut_runs` |

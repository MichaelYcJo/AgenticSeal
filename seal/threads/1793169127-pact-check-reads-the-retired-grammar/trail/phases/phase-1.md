# Phase 1: 1793169127-pact-check-reads-the-retired-grammar

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | add9a409 |

## What this phase was asked

Build `plan.md`'s phase 1 as its row states: `path_map` reads the map
through `config.gfm_table` with the header `("Remote", "Path")` and answers
`(found, refusals)`. `check` prints each refusal as
`REFUSED ~/.claude/agentic/pact-paths.md — the map <sentence>`. A map with no
table, a doubled remote, an empty cell and a second header are refused.
`MAP_HEADER`, the `row` pattern and `config.CONFIG_SEPARATOR` go, and
`CELL`'s comment is rewritten. Each scenario's case is seen red at
`977b6613` before its code.

## What this phase found

- The walk already refuses a second header that sits under the first table
  before the next heading, as a row the walk never reaches. A second
  refusal of the same line would print it twice. So the second-header
  refusal is added only where the walk refused nothing, which leaves it the
  one shape the walk is silent on: a second table under a later heading.
  `gaps.md` records this against *Scope* item 1's wording.
- A second header glued to the first table's last row is one of the
  table's rows to GFM, and the walk refuses the delimiter row under it. The
  first draft skipped that row; `seal mutate` showed no case could tell,
  and the row it would add keys `remote`, which no signer normalises to. So
  the skip was removed rather than pinned.
- Red runs: the 15 new or rewritten cases of `-k map` failed against the
  tree with `pact_check.py` as at `977b6613` (exit 1). Each arm of the
  base read the shape silently and `check` exited 0.
- Mutants over `pact_check.py`, `-k map`: the empty-cell arm, the
  doubled-remote arm, the second-header slice, the `the map` print loop and
  a dropped walk refusal were each red. The `if not walked` guard survived
  until the case *a second header the walk names* was added (commit
  `add9a409`), and was red after it.
- `git grep -n CONFIG_SEPARATOR -- '*.py'` printed nothing (exit 1).

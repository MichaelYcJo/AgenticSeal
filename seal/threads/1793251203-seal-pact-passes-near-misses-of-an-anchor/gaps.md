# Closing memo: 1793251203-seal-pact-passes-near-misses-of-an-anchor

## Why this work exists

`seal pact` read a near miss of a pact anchor as no anchor, so a signer
whose anchors stood under a misspelled header, named an undeclared remote,
or used the old inline token in capitals was reported as citing nothing.
Each of those rows is now refused at its line.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| S5's red | `frame/plan.md` phase 1: seen red against `28edee12` / no row scan exists there, so S5 was shown red by `seal mutate` on the scan's guard | the mutation | `trail/phases/phase-1.md` *What this phase found*, the first correction |
| S5's form | `frame/design.md`: a case / an assertion on every id of `test_refuses_an_anchor_row_nobody_reads` | the assertion | `trail/phases/phase-1.md` *What this phase found*, the second correction |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch | the orchestrator, through `seal gate` |

## Not done

The walker's own over-refusal stays: an anchor table, a blank line, then an
indented code block whose line is written `| ... |` is refused by
`hooks/lib/config.py#gfm_table` as a row the walk never reaches, though
GitHub renders the line as code (`trail/phases/phase-1.md`, the walker
limit; round 1, *Not judged*). It predates this work, this diff does not
expose it through the row scan, and the plan does not edit the walker. The
orchestrator names it for an issue.

## Fed back into the design

none

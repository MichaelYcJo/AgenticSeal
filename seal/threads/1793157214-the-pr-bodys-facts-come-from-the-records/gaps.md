# Overview: 1793157214-the-pr-bodys-facts-come-from-the-records

## Why this work exists

Four of the five withheld sealer runs of this release, and 23 of 27 in 0.22.x, were over a sentence of the hand-written pull request body that restated a record and got it wrong; the body's facts are now the records' own text, and the orchestrator writes only what no record holds.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Two fixed lines the design's list does not name | `frame/design.md` lists the fixed sentence for each missing record | `FIXED` also holds a line for a `frame/plan.md` with no `## Phases` section and one for a `trail/gate.md` with no table line | the plan's failure scenario expects a missing `## Phases` to show as such a line, and the gate's line follows the same shape |
| A second section of one name | `frame/design.md` is silent | a second `## Phases`, `## Not verified` or `## Not done` section is refused at its line | a copy of one of two sections would be a choice the generator makes |
| What a line equal to `HEADING` refuses | `frame/design.md` S6: a record holding a line equal to `HEADING` is refused | a copied line equal to it is refused, at the record's line; a line in a part that is not copied is not | only a copied line would split the body in the wrong place |
| Which round file names are read | `frame/design.md`: a positive integer | `hooks/lib/routing.py#round_number`, the chain check's one ordering rule, which accepts `round-0.md` | one ordering rule for round records |
| A missing body under `--check` | `frame/design.md`: exit 2 for an unusable argument | exit 1 | the check's answer is that the body does not match |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, through the tree's `bin/seal gate` after the review rounds settle |
| that `seal pr-body` behaves the same on Windows | the Windows shards of the `tests` workflow on this branch |

## Not done

nothing

## Fed back into the spec

none

# Overview: 1793157214-the-pr-bodys-facts-come-from-the-records

## Why this work exists

Four of the five withheld sealer runs of this release, and 23 of 27 in 0.22.x, were over a sentence of the hand-written pull request body that restated a record and got it wrong; the body's facts are now the records' own text, and the orchestrator writes only what no record holds.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Two fixed lines the design's list does not name | `frame/design.md` lists the fixed sentence for each missing record | `FIXED` also holds a line for a `frame/plan.md` with no `## Phases` section and one for a `trail/gate.md` with no table line | the plan's failure scenario expects a missing `## Phases` to show as such a line, and the gate's line follows the same shape |
| A second section of one name | `frame/design.md` is silent | a second `## Phases`, `## Not verified` or `## Not done` section is refused at its line | a copy of one of two sections would be a choice the generator makes |
| What a line equal to `HEADING` refuses | `frame/design.md` S6: a record holding a line equal to `HEADING` is refused | a copied line equal to it is refused, at the record's line; a line in a part that is not copied is not | only a copied line would split the body in the wrong place |
| A copied line holding a closing keyword | `frame/design.md` S6 refuses a round record `chain_check.py` refuses and a line equal to `HEADING`; `frame/questions.md` keeps the `Closes` line the orchestrator's | a copied line where `close_issues_on_release.py#keywords_in` reads a closing keyword is refused at the record's line | review round 1 finding 1: a record's prose reaching the body would close an issue no party claimed, through GitHub and through the release's closer |
| Which round file names are read | `frame/design.md`: a positive integer | `hooks/lib/routing.py#round_number`, the chain check's one ordering rule, which accepts `round-0.md` | one ordering rule for round records |
| A missing body under `--check` | `frame/design.md`: exit 2 for an unusable argument | exit 1 | the check's answer is that the body does not match |
| Where the sealer's check stands | `frame/plan.md` row 2: a `seal pr-body --check` step in `agents/sealer.md` | the check is the first act of step 2, and no step is renumbered | `docs/the-review-record.md` cites the sealer's steps 3 and 4 and `templates/records/sdd-guarantee.md` its step 5 by number |
| Two readers outside row 2 | `frame/plan.md` row 2 lists the readers it rewrites | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* step 2 names `seal pr-body` between the broad run and the sealer, and `templates/records/sdd-guarantee.md`'s parties placeholder names the orchestrator's part of the body | each stated the order or the parties this work changes |
| Where the fixture-body case stands | `frame/plan.md` row 3 names the case | `tests/evals/test_rule_cases.py::Test_main` | a class of its own would need a `test_refuses_` case, and `sealer_case` refuses nothing |
| When the fixture body is composed | `frame/design.md`: the body is `compose` over the fixture's records | `compose` runs over the records before their placeholders are filled, and the body is filled the same way | `compose` copies the `target:` and gate lines unchanged, so the lines are the same |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, through the tree's `bin/seal gate` after the review rounds settle |
| that `seal pr-body` behaves the same on Windows | the Windows shards of the `tests` workflow on this branch |
| that the five paid sealer evals grade as before, now that the sealer runs `seal pr-body --check` first | the owner, at the next paid run (`frame/questions.md` Q4) |

## Not done

nothing

## Fed back into the spec

none

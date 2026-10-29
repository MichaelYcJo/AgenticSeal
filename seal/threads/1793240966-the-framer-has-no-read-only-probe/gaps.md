# Closing memo: 1793240966-the-framer-has-no-read-only-probe

## Why this work exists

A question a read-only command answers was queued for the build as an `a measurement` row, and after this work the framer runs that command and writes the answer into the frame.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| How phase 1 shows the new graders' regexes | `plan.md` phase 1 *Verified by*: "Each new grader's regex is shown matching a hand-written frame that answers in `## Grounding` and failing one that leaves the answer as a row, run once in a `test_tmp_*` file and deleted". Phase 1 wrote that check as `Test_framer_case`, two cases kept in `tests/evals/test_rule_cases.py` | the kept cases | `agents/crafter.md` *Rules*: "Mutation-test every unit you added ... a unit that stays green while broken has nothing behind it". With the probe deleted, no case in the tree reads the two patterns, and each of the six mutants of phase 1's units would have stayed green |
| The residue rule's wording in `agents/framer.md` | `frame/design.md` *Data & interfaces*: "Every row owes a reason the tree could not answer it" becomes "a reason neither the tree nor a probe could answer it". Phase 2 wrote "Every row owes a reason the tree could not answer it and no probe could either" | the phase 2 wording | `frame/plan.md` *Technical context*: "Every sentence the existing cases pin stays". `tests/behaviour/test_waiver_decided_at_start.py:793` pins "owes a reason the tree could not answer it", and the design's wording would have turned it red |
| S2's grader, `shape-no-measurement-row` | `frame/design.md` S2 at `d2acd3b9`: "then no row names `a measurement` as who answers", held by "a `not_contains` regex over `frame/questions.md` for a table cell holding `a measurement`"; S8 at `d2acd3b9`: "both pass every run of the new side". The frame folded the removal at `ecaf7c32` and `542404ee`: S2 now reads "then no row asks what `shout` returns" and names no grader, and S8 names `shape-answers-by-probe` alone. In phase 3's four paid runs the grader caught three rows, and each asked whether issue #105's comments change the request, which `gh` could not read in the runner's environment. It failed new-side run 0 for that row. Removed at `7ac24a06` | the removal; S8 rests on `shape-answers-by-probe`, red 2 of 2 on the old side and green 2 of 2 on the new | `agents/framer.md` *Rules*, the new rule: "A row whose answer is a behaviour, a time or an output is written only where no probe can run in your environment ... and its reason says which". The row the grader caught is one the rule keeps, and contract rule 18: "When a check refuses code that is correct, fix the check" |
| The case filter in phase 3's commands | `plan.md` phase 3: `--case 'rule-framer-sharp-s'`. Both sides ran with `--case '*rule-framer-sharp-s'` | the leading `*` | `claude plugin eval --help`: "Filter cases by name glob", and the case's name is `framer rule-framer-sharp-s`. Each side file's `suite.caseFilter` records the filter and one case |
| The new side's spend cap | `plan.md` phase 3: `--max-cost-usd 20` on each side. The new side ran with `--max-cost-usd 14.8` | 14.8 | `frame/questions.md` Q1 (a): "two runs on each side, capped at 20 USD with `--max-cost-usd`". 14.8 is 20 less the old side's 5.20 USD, so the two sides together stay under 20; they spent 10.01 |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck over the branch | executed by the orchestrator's broad gate at `7cfe9334` against `99853d04`, passed (`trail/gate.md`), and this repository declares no typecheck (`seal/config.md` *Broad gate*; #951 would add one) |
| closed The new rule's no-row half: that a framer leaves no `a measurement` row for a question a probe could answer in its environment | answered by #1158 (work item `1793251204-the-framer-is-handed-the-body-without-its-comments`, #1166): the grader `shape-no-measurement-row` of `evals/behaviour/framer/rule-framer-generated-page/` reads the no-row half; it was not seen red, and the owner kept `Closes #1158`, which closed completed at 0.24.2's merge into `main`, 2026-10-29 |

## Not done

A narrower grader that reads only a row whose question names `shout` or `straße` was within reach and not written. Read against the question rows in the saved traces, it would have passed all four runs on both sides, so it caught nothing that was measured, and it decides from the words of a question cell. `CLAUDE.md` *The rule a mechanism is kept against* says a check gates only a fact it reads, and a reading guessed from words is a report.

## Fed back into the design

none

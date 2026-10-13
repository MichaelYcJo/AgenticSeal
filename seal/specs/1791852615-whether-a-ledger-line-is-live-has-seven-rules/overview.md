# 1791852615-whether-a-ledger-line-is-live-has-seven-rules — overview

<!-- The closing memo (implement skill, step 4). Only what the diff cannot
show, each part written when it happened. -->

📋 implement applied
· spec:     spec.md §Scope, S1–S7, §Data & interfaces, §Removes; plan.md's phases and alternatives; questions.md D1–D8, Q1–Q5
· evidence: seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md
· verified: each phase record carries its runs, labelled executed or read

## Why this work exists

Seven readers decide whether a ledger or record line is live and answer three
different ways; the rule behind the three is now written once in `docs/`,
each reader says which answer it gives, and one table holds all seven so a
moved direction is a red cell.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Which answer `hooks/config.py#hidden_lines` gives below a comment opener nobody closed | `spec.md` §*Scope* 1: the excusing and declaring readers are "parked on doubt", `hidden_lines` "keeps the fence-only reading where the walk is unsure" / the reader reads that row as declared, and its docstring says so: such an opener "hides nothing it did not hide before" | the code, stated in the statement's own bullet | 1790645290 `spec.md` §*A construct that never closes is not a construct*: "Keeping the base reading of the live lines loses nothing either direction forbids". No verdict may move in this work, so the statement says what the reader does |
| The corpus of the direction table | `spec.md` §*Data & interfaces*: six shapes / eight | eight | With six, the plan's `live_lines` mutation survives every cell, because no shape puts the two span readings in disagreement; and no shape tells the two `quoted_lines` apart. The two added shapes are each answered by a docstring: `live_lines` names the lone-backtick shape, and the rider check's and `hidden_lines`' say what a line the walk is unsure of reads as |
| Whether the checker's and the rider check's `quoted_lines` differ | `plan.md` §*Alternatives considered*: "a difference measured at zero rows" / they differ on a fence opened at one to three spaces | both, scoped | The zero is about the released ledgers, which carry no fence line (P2-3), and it holds there. On markdown in general they differ, and the table pins the difference |

## Not verified

| Item | Who must answer |
|---|---|
| Whether `hooks/blocks.py#walk` can ever return a line both `fence` and uncertain, which is the only case the rider check's `and not walked.uncertain[index]` clause decides; every shape probed in phase 1 returned an uncertain construct as `live`, and a mutation dropping the clause survived | whoever next changes `hooks/blocks.py#walk` |
| The full suite, lint over the repository and the typecheck | the sealer, once the review rounds settle |

## Not done

Nothing.

## Fed back into the spec

Each of these is *inferred during implementation*, and a planner may
overturn it:

- **`hidden_lines` answers doubt with its older reading, not by parking**,
  so a row below a comment opener nobody closed declares; the statement in
  `docs/the-evidence-ledger.md` names it.
- **The rider check reads a fence its walk is not sure of**, which the
  checker's delimiter rule closes; the statement names it as the third of
  the holding readers that read a different amount from the checker.

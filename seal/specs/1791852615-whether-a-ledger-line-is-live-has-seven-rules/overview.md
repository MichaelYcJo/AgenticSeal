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
| The corpus of the direction table | `spec.md` §*Data & interfaces*: six shapes / ten | ten | Round 1's 🟡 2 added the last two, the second and third shapes the two `quoted_lines` part on. With six, the plan's `live_lines` mutation survives every cell, because no shape puts the two span readings in disagreement; and no shape tells the two `quoted_lines` apart. The two added shapes are each answered by a docstring: `live_lines` names the lone-backtick shape, and the rider check's and `hidden_lines`' say what a line the walk is unsure of reads as |
| Whether the checker's and the rider check's `quoted_lines` differ | `plan.md` §*Alternatives considered*: "a difference measured at zero rows" / they differ on three shapes: a fence opened at one to three spaces, a fence inside a closed line-start comment, and a closed fence below a fence nobody closed | both, scoped | The zero is about the released ledgers, which carry no fence line (P2-3), and it holds there. On markdown in general they differ, and the table pins the difference |
| The class and direction five units declare | `spec.md` §*Data & interfaces*: the checker's `quoted_lines` `owned` and `passed`; `claim_lines` `passed`; `readable` `owned` and `passed` / `guess` with `refused`, `refused`, and `guess` with `mixed` | the code | `docs/the-reader-registry.md` §*The four classes*: "A unit reading several inputs declares the weakest" and "a helper's direction is therefore read at its callers". `unquoted` hands the checker's walk every `.md` file an anchor names; `readable` reads the session-written records `claim_lines` reads, and its callers refuse a hidden table except `broad_gate.py#sealed_record`, which feeds a label. The checker's two feed a `BROKEN` row or a refused name at exit 2, so their direction is `refused`, as the rider check's and `anchored_rows`' already were (round 1's 🟡 3). `phases/phase-2.md` names each caller |

## Not verified

| Item | Who must answer |
|---|---|
| closed Whether `hooks/blocks.py#walk` can ever return a line both `fence` and uncertain, which is the only case the rider check's `and not walked.uncertain[index]` clause decides; every shape probed in phase 1 returned an uncertain construct as `live`, and a mutation dropping the clause survived | answered from the code by round 1's note 5, at f8c96c3b: `walk` writes a fenced range as a slice and jumps past it, so its lines never reach the code that sets `uncertain`; the tail loops and `walk_text` mark only `live` lines uncertain; a seeded fuzz of 200,000 texts through both found 0 such lines. The clause is defensive and the surviving mutant is equivalent, until the walk changes |
| Whether `tests/test_settle_reads_before_it_removes.py::test_no_row_of_this_repositorys_ledger_anchors_inside_a_work_item` is over the suite's 90 s ceiling at the base too: it ran 117 s in a parallel run on this branch and 153 s alone, and passed with the ceiling raised; this work adds 17 rows to the ledgers it reads and no code it runs | the sealer's broad gate, which re-runs a failing file at the base |
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

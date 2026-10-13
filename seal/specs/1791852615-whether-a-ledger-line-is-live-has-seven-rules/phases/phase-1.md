# 1791852615-whether-a-ledger-line-is-live-has-seven-rules — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 78237f6a |
| Ran by | unknown — the spawn prompt named the agent, `smith`, and not the model; the orchestrator fills this row |

## What this phase was asked

Build phase 1 of `plan.md` as approved: the direction table test, one corpus
of the shapes in `spec.md` §*Data & interfaces*, seven adapters and the stated
answer per cell, seen red under one mutation per bias; the statement in
`docs/the-evidence-ledger.md` under this work item's marker with one
`Enforced by:` line; one sentence in `skills/evidence-check/SKILL.md`
§*What counts as a claim*. And, for the seam with #905: move the prose under
this frame's `## Removes` table beneath a sub-heading, `### Why these rows`,
without changing its words, because #905's reader ends the section at the
next heading of any level and refuses a line under it that is neither a row
nor a `nothing — <why>` line.

**Direction.** Nothing a gate answers moves: the phase adds a statement, a
sentence and a test module, and changes no reader. **Prompt budget.** Zero.

## What this phase found

**The frame does not hold in two places, and both are recorded in
`overview.md` as divergences.**

1. *`hooks/config.py#hidden_lines` is not "parked on doubt" for a comment
   nobody closed.* `spec.md` §*Scope* item 1 groups it with `live_lines` as
   the reader that parks a line on doubt. Its docstring says otherwise for
   one shape, and the table measures it: "a `<!--` nobody closed hides
   nothing it did not hide before". Where its walk is unsure it keeps the
   fence-only reading from before #667, which parks a row below a fence
   nobody closed and **reads** a row below a `<!--` nobody closed.
   1790645290's `spec.md` §*A construct that never closes is not a
   construct* is the decision: no row the older reading saw may go missing.
   The statement in `docs/` says so in the reader's own bullet rather than
   claiming the frame's grouping, and the table pins `read` on that cell.
2. *Six shapes cannot show two of the mutations the plan names.* No shape of
   the six puts `live_lines`' two span readings in disagreement, so the
   plan's mutation "a disagreement read live by `live_lines`" survives every
   cell; and no shape of the six tells the checker's `quoted_lines` from the
   rider check's, which the frame says "differ on no row here". The table
   carries two more shapes: a lone backtick that leaves a comment in doubt
   (the shape `live_lines`' docstring names), and a fence opened at two
   spaces, which the shared delimiter rule closes and `hooks/blocks.py#walk`
   is not sure of. On that shape the checker's `quoted_lines` skips the row
   and the rider check's reads it, so the "differ on no row" holds for the
   released ledgers (no fence line, P2-3) and not for markdown in general.
   The statement names it.

**Seen red, each through `mutation-check`, each on a committed tree.**

| Reader | Mutation | Red cells |
|---|---|---|
| `evidence_check.py#quoted_lines` | an unclosed fence's lines added to the skipped set | `… on a fence nobody closed` |
| `unverified_check.py#live_lines` | `literal[n] and crossing[n]` → `or` | `… on a lone backtick leaves the comment in doubt` |
| `unverified_check.py#readable` (through `blank_fences`) | an unclosed fence blanked to its opener only | `… on a fence nobody closed` |
| `evidence_check.py#claim_lines` | `aside_held` dropped from the return | `… on a comment nobody closed` |
| `settle.py#anchored_rows` | only the first three lines of each ledger read | five cells |
| `rider_check.py#quoted_lines` | a line the walk is unsure of hidden | three cells, the two-space fence among them |
| `hooks/config.py#hidden_lines` | the fence-only reading on every line | `… on a comment that closes`, `… on a lone backtick …` |
| the statement | `readable` named in the excusing bullet | `test_the_statement_names_each_reader_under_its_answer` |

The statement case was also red before the statement existed: the marker was
not in the file.

**One mutation survived, and it is about the rider check, not about the
table.** Dropping `and not walked.uncertain[index]` from the rider check's
`quoted_lines` changed no cell. On every shape probed — a two-space fence, a
fence after a list item, a block quote, an HTML block, a fence below a
construct nobody closed — the walk never returned a line both `fence` and
uncertain: an uncertain construct comes back `live`. So that clause may be
unreachable. It is not this work's to change, and it moves no verdict either
way; whether the walk can ever return that pair is unverified, and its
answerer is whoever next changes `hooks/blocks.py#walk`.

**What the next phase needs.** `evidence-check --strict .` exits 2 at this
phase's commit with one DRIFTED row, `seal/releases/0.18.0.md` C2 on
`docs/the-evidence-ledger.md#"## The fold, and what tells it from a
deletion"`, moved by the statement this phase inserted; phase 2's
`--reverify --into` answers it with the docstring drifts. The records arm
reads 0 work items, because this work item has no ledger fragment yet, so the
`## Removes` rows are not read until phase 2 writes one.

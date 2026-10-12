# every reader and record is inventoried (#834) — questions for the planner

<!-- seal/specs/1791382684-every-reader-and-record-is-inventoried/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

## Decided from the tree, so nobody reopens them

The spawn left these open and the repository answered them; the grounds are
in `spec.md` §*The build* and `plan.md` §*Alternatives considered*.

- **A stale row writes nothing, and its unit stays on the census.** 123 of
  the 912 rowed units have a hash at 57e2bc13 that differs from 5623d728's.
  A fresh reading would be a judgment no row grounds, costing 501 re-reads,
  for the units the siblings rewrote on purpose; the rule's own transition
  makes each declare when next touched.
- **A unit two rows disagree on takes the weakest class**, `guess` over
  `owned` and `observed`, `mixed` over one direction — the rule
  `docs/the-reader-registry.md` already states for a unit reading several
  inputs. Seven units; no row.
- **A row naming no population unit writes nothing.** 23 rows name a
  constant, a nested function, a method or a unit since removed; the
  population is top-level `def` and `class` only.
- **The inventory stays where it is.** `settle.py#PROCESS_DIRS` names
  `rounds` and `phases`; `inventory/` is the reading the spec's tables rest
  on and leaves with the directory at `settle --retire`, after which the tag
  holds it. Not a process record, not a `docs/` document.
- **The lines are written by a one-shot script that asserts every landing**,
  deleted before the hand-over, not by hundreds of `Edit` calls
  (`skills/implement/SKILL.md` §2; `agent-contract` §7, §9).
- **`hooks/worktree-guard.py` is last**, after the release branch with #894
  and #896 is merged in, because both rewrite it and a docstring line on a
  unit they change is a conflict at their merge.
- **The 695 units the inventory did not row get no `Reads: nothing` line.**
  The inventory's agents left them out rather than judging them; a line on
  each would be a claim nobody made. They stay on the census (#835 Q7's (a)).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | How much of the backfill 0.21.0 pays. 759 units carry a clean row at 57e2bc13. Under `Ledger frozen from`, a `Reads:` line on a unit a released row cites owes a `Re-read ·` row whose `--checked` date asserts somebody read it; measured over `seal/ledger.md`, `seal/releases/*.md` and `seal/ledger/*.md`: all 759 owe 687 re-reads and 24 live re-stamps; the 275 `guess` units owe 247 and 14; the 245 units no ledger row cites owe 0 and 1. The whole run wrote 360 re-reads and its review called that structural, opening the ledger's premise for 0.22.0. #835's Q7 stood at (a) before these numbers existed | a person (the repository owner) | (a) all 759: the census shrinks to 825, `grep -rn "Reads: guess"` is complete for the inventory's clean readers, and the fragment carries 687 `Re-read ·` rows that the smith either reads one by one — a docstring line cannot have falsified any of them — or dates without reading. (b) the 275 `guess` units: the grep is complete for what reopens, at 247 re-reads. (c) the 245 uncited units: zero re-reads, 95 `guess` lines, the census shrinks to 1,339, and the 514 cited units wait for the ledger rework or a later answer; the mapping rules in `plan.md` rerun then. (d) defer the whole backfill to 0.22.0: nothing in the code changes, #834 ships as the inventory alone | (c) | ✅ the repository owner answered (c) on 2026-10-12 |
| Q2 | The counts at the build's tree: #894 and #896 land on `hooks/worktree-guard.py` between 57e2bc13 and the build, so its stale set grows and the Q1 sets shrink there; any other sibling landing before phase 2 does the same to its files | a measurement | phase 1 reruns the mapping with `reader_registry.population()` and records every count beside the frame's, with both SHAs, in `phases/phase-1.md`; phase 4 reruns it for the guard after the merge | the frame's counts at 57e2bc13 | ✅ measured at 7608d82c, beside the frame's, in `phases/phase-1.md`; the code there is 57e2bc13's, so the counts agree except where the rules' application differs |
| Q3 | The 23 units whose `Class` cell starts with no class word, and what each cell says: a class in other words, two classes, or none. Their names are in phase 1's record (`hooks/config.py` 9, `hooks/tokens.py` 2, `hooks/routing.py` 2, `hooks/review-history-guard.py` 2, `hooks/cmdline.py` 2, and one each in `chain_check.py` ×3, `round_record.py`, `correction_check.py` ×2, `evidence_check.py` ×2, `arm_check.py`, `broad_gate.py`, `session_cost.py`, `unverified_check.py`) | the work | phase 2 reads each cell: a class named in other words is that class, two are the weaker, none leaves the unit on the census; the choice and its cell go in `phases/phase-2.md` | read the cell | ✅ answered by the cells, `phases/phase-1.md`: read with `\|` unescaped, every one of the 23 begins with a class word, and the frame's count was its split on every pipe; the units read by hand instead are named there and decided in `phases/phase-2.md` |
| Q4 | Where a row's `What it reads` cell is longer than a docstring line should carry, or holds a `\|`, a `"""` or a line break the table folded, what the line says | the work | the cell as written, `\|` unescaped, trimmed at a clause boundary with the rest under the line; the direction's parenthetical from the `Unknown` cell always goes under the line, since the direction word is the line's last | the cell, trimmed | ✅ answered in phase 2 (`phases/phase-2.md`): the cell as written with `\|` unescaped, cut at a clause boundary near 110 characters with the rest under the line as `What it reads, continued:`; the `Unknown` cell's text after its direction word under the line as `<Direction>: …`; five cells holding a backslash said in words |

**`Who can answer` takes one of three values and nothing else.** They were one
shape on the page before this, and #84's second comment measured all three
inside a single run's four rows.

- **a person** — what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument and queueing it behind one wastes a round
  trip.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing — and the
`Status` column is ticked by whoever answered, never by whoever asked.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.

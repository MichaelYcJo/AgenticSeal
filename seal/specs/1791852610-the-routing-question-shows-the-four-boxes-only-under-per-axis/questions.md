# the routing question shows the four boxes only under `per axis` — questions for the planner

**Decided from the tree, listed so nobody reopens them.** This run is routed
`automation` (`routing.md`, `Answer pressed` = `automation`), so nobody is
asked mid-run; every row below was answered from the repository and the
grounds are written where a reviewer can open them. The owner, who filed
#911 and pressed the routing answer, can overturn any of them at the
approval of `plan.md`; none blocks the build.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Is `per axis` costing a second wait acceptable? | a person — decided from the ticket. The issue's own *Now / After* table, written by the owner, sets the trade: `automation` and `no work item` lose the boxes, `per axis` gains a wait | (a) accept the second wait — the second call follows the first at once, before the first edit, so it costs a reply rather than a stopped session, which is how `skills/implement/SKILL.md` §1 prices a question; it is still a second wait (§1: *three interruptions cost three waits*), and `per axis` is the rare answer. *Corrected 2026-10-13 after round 1 (⬜ 7): this option first read §1 as saying a click count costs nothing* · (b) keep one call — the defect stays | (a), recorded in `plan.md` Alternatives A | ✅ decided from the tree, 2026-10-13 |
| Q2 | Should the second call offer the four boxes with the most common combination pre-described, or should question 1 grow a combination preset? | a person — decided from the tree. #88 (`skills/implement/orchestration.md` §*Question 2*, the ceiling paragraph) says the question grows only where a decision is genuinely a person's, and the boxes' descriptions already carry both halves of each box | (a) no — the four boxes as §*Question 2* specifies them, unchanged · (b) a combination preset in question 1 — a guess at which combination, and the next one breaks the four-option cap | (a), recorded in `plan.md` Alternatives C | ✅ decided from the tree, 2026-10-13 |
| Q3 | Should the press reader refuse a routing result whose call also carries the four boxes, or keep accepting both shapes? | a measurement, and the tree — the reader already accepts both (`hooks/worktree_consent.py#_routing_preset` skips any question whose `multiSelect` is not `False`); phase 1's case is the measurement. The decision to keep it is the tree's: installed `~/.claude/CLAUDE.md` takes the new block only at `/specseal:update`, and every transcript before this item holds the two-question shape, so refusing it brings the guard's prompt back under `automation` (#894) | (a) keep both shapes, pinned · (b) refuse the two-question shape — a stop on every un-updated machine | (a), recorded in `plan.md` Alternatives D and the Failure scenario | ✅ decided from the tree, 2026-10-13; the measurement is phase 1 |
| Q4 | Rename the two headings that state the retired shape, or change only the prose under them? | the work — decided here. A heading that says *two questions, one call* after the change is the stale copy `tests/test_waiver_decided_at_start.py` was written to refuse. The cost is bounded: two act-table rows, one cross-reference in `docs/worktree-guard-spec.md`, and re-read rows in the fragment for the two frozen `seal/releases/0.12.0.md` coordinates. `### Question 1 — single-select` stays, because `test_the_labels_match_the_routing_question_the_orchestrator_asks` reads the labels under it | (a) rename both, as `spec.md` §*Data & interfaces* names them · (b) keep the headings | (a), recorded in `plan.md` Alternatives E | ✅ decided from the tree, 2026-10-13 |
| Q5 | What is the one spelling the three files and the tests share? | the work — decided here, because a sentence pinned at four places has to be fixed before any of them is edited (`seal/releases/0.12.0.md` row *one spelling*: two spellings of one decision is the drift the pair exists to catch) | *Ask question 1 alone, and the four boxes in a second call only under `per axis`.* — short enough to survive whitespace collapsing, and it names both halves of the shape | that sentence, in `spec.md` §*Data & interfaces* | ✅ decided from the tree, 2026-10-13 |

**`Who can answer` takes one of three values and nothing else.**

- **a person** — what the product should be, or a value somebody has to be
  accountable for. The only kind of row that blocks the build. Q1 and Q2
  are of this kind by nature and were decided from the owner's own issue and
  the ratified rule, which is why they are marked decided rather than open.
- **a measurement** — a probe, a command or a count settles it. Q3.
- **the work** — unknowable at framing time, or a choice the frame has to
  make for the build to proceed. Q4 and Q5.

**The framer opens rows and does not own their answers.** Under `automation`
the rows above are closed with the grounds the tree gives; the owner's
reading of `plan.md` is where a different answer is given, and a different
answer to Q1 or Q2 is the one that would change what gets built.

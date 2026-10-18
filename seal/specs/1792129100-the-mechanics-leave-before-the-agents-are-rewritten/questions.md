# the mechanics leave before the agents are rewritten (#964) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

## What the tree answered, so nobody reopens it

#957's frame left these open and the repository settled them; the grounds
are in `spec.md` and in `plan.md`'s Alternatives table. They came here with
the phases they belong to.

- **The `Reads:` lines leave with the census**, not only the list and the
  test: a line no check reads is a mark with no reader (`plan.md`
  Alternative B).
- **The grammar table lives in `docs/the-review-record.md` and the script
  loads it**; the user's hygiene workflow clones the whole repository at the
  pinned tag, so the document is beside the script (Alternatives D, H).
- **No generated-variant or mutation case is written for the grammar**
  (Alternative E, the owner's decision on #929).
- **The `## Not verified` closing mark becomes the word `closed` in the same
  cell**; a labelled-line redesign of the section is #940's or #956's
  (Alternatives F, G; Q2 put the default in front of the owner, who kept
  it).
- **The Windows-red case on `main` at the release is phase 1's**, since every
  pull request of this item runs it; the sealer-guarantees case of the same
  run is #963's, fixed outside this item.
- **`Enforced by:` keeps its spelling here**; its rename is #941's, with
  `rules.py` as the reader.
- **The emoji in output printed for a person and read by no agent or check**
  stay; that is #957's Q9, which the owner answered on 2026-10-16 by keeping
  the default, and `spec.md` §*Scope* names them as out.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | **Does #957 run as one work item on its branch, or as two?** #957's `routing.md` names one branch. #923's one diff that did many things took ten review rounds. Item 1 (its phases 0, 1, 2, 8) is checks and tests verified by CI alone; item 2 (phases 3–7, 9) is the agents with the paid proof. Splitting needs a second issue, which only a person opens | a person — the owner | **one work item**: the phases run in #957's table's order on its branch, one review chain over the whole diff · **two work items**: a second issue and `routing.md` for item 1 on a branch cut from `release/v0.22.1`, item 1 merges first, and #957 is rebased on it before its agents are rewritten | one work item | answered 2026-10-16 by the owner: two work items; this one, #964, is item 1 and merges first; #957 rebases onto `release/v0.22.1` after it |
| Q2 | **Does the `## Not verified` closing mark `U+2705` become the word `closed`, with the four 0.22.0 items' overviews rewritten once and a user's in-flight overview refused at their next pin move?** The owner's rule says no emoji anywhere and one lowercase word at the start; this mark is read by a gate (`unverified_check.py#CLOSED`), the one class #923 found four times. The word in the same cell is the smallest change; the rows of the shipped overviews are the compatibility cost | a person — the owner | **`closed`, as the default says** (phase 4): the reader accepts the word alone, refuses `U+2705` naming the row and the edit, and the four overviews are rewritten by a one-shot script in the same commit · **keep `U+2705` as the one mark a check reads**: the reader is unchanged and the rule gains one exception, written into `docs/the-record-layout.md` · **redesign the section into labelled lines**, as the round record was: a second checker rewrite, which `plan.md` Alternative G sends to #940 or #956 | `closed`, phase 4 | answered 2026-10-16 by the owner: the default was shown and kept — `closed`, the four overviews rewritten once |

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

**The framer opens rows and does not own their answers.** The `Status`
column is written by whoever answered, as `answered <date> by <who>`, never
by whoever asked. Both rows here were the owner's and are answered; the
measurement and work rows of #957's frame stayed with #957, whose phases
answer them. Nothing blocks the build.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.

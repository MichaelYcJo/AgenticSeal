# survivor-check reads a range as its own commits (#873) — questions for the planner

<!-- seal/specs/1791852614-survivor-check-reads-a-range-as-its-own-commits/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

**Judgments the ticket left open that the tree answered.** Each is decided
in `spec.md` §*In* or in `plan.md`'s *Alternatives considered*, where a
reviewer can overturn it by opening what was opened. None is reopened here,
and no row below is a person's: the routing answer is `automation`, and
nothing here needs a value somebody has to be accountable for.

- **Which of the issue's three options** — the shared reader. The sweep
  keeps its two-ends count and keeps a removed or written sentence only
  where an own commit removed or wrote it. Refusing the shape (alternative
  B) leaves the caller unable to ask the fix pass's question at all, and
  stating the limit (C) is the reader class the inventory exists to close.
- **Whether `A...B` takes the own-commits reading** — no. Measured in the
  frame: from the merge base the own commits made before the merge are not
  on an ancestry path. `A...B` reads its two ends, as today. Alternative F.
- **Per sentence or per path** — per sentence, both lists. #860's unit-level
  measurement is the same class; alternative D, and S4 pins it.
- **Per-commit reading in place of the two-ends count** — no; the net
  reading is what the floor was calibrated against. Alternative E.
- **A second `--ancestry-path` reader or the shared one** — the shared one,
  loaded by path as the sweep loads its other two siblings. Alternative G.
- **A two-dot start that does not reach its end** — refused on the run's own
  range, in `main`'s path; `whole_range`'s resolution of declaration rows is
  untouched. Alternatives H and I.
- **Where the policy statement lives** — the home,
  `docs/the-record-layout.md` §*A range owns the commits that descend from
  its start*, because `docs/review-chain-spec.md` is one line under the
  ceiling. Alternative J.
- **Whether a sentence may state what a range from an older start owns** —
  no sentence anywhere; the owner sentence answers it and a shape is a case.
  `plan.md` §*What the build must not write*.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | What does the own-commits pass cost on a real two-dot range, and is a skip for a range with no merge worth its line? On a linear range the filter keeps every sentence, so the skip changes no output; the tree cannot say whether two `cat-file` batches per own commit are noticeable beside the two-ends read and the corpus index | a measurement — the smith in phase 2, `survivor-check` timed over a real fix-pass range of this repository (one of 1791384160's `Fix range` rows, whose commits resolve on `main`) with the pass and with it bypassed | (a) the pass costs a small fraction of the run: no skip, one reading; (b) it dominates: skip it where `git rev-list --merges a..b` lists nothing, with a case showing the skipped and unskipped reports equal on a linear range | (a) | ⬜ |
| Q2 | What is the new test module named, and does it import `build` from `tests/test_a_corrected_sentence_survives_elsewhere.py` or the `commit`/`merge`/`switch` helpers from `tests/test_a_range_owns_what_git_lists_for_it.py`? The shape helpers build merge histories; `build` writes files and commits in one call | the work — phase 1 | (a) the shape module's helpers, with files written through its `write`; (b) `build` extended with a branch argument. Either keeps git driven from Python | (a) | ⬜ |
| Q3 | The exact `Reads:` class and direction of `corrected`, `parse_range`, `main` and the new units, under `docs/the-reader-registry.md`'s grammar: `corrected` reads git's diff and blobs (observed) and `parse_range` a spelling a person typed (guess); what each does with an input it does not understand is read at the callers | the work — the phase that touches each unit | the grammar's classes; the direction read through to `main`'s exit | `parse_range`: `guess … unknown refused`; `corrected` and the new reader: `observed … unknown refused` | ⬜ |

**`Who can answer` takes one of three values and nothing else.** They were one
shape on the page before this, and #84's second comment measured all three
inside a single run's four rows.

- **a person** — what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument and queueing it behind one wastes a round
  trip. Measured: six probes at about three seconds each answered a row that
  had been written into the human batch, and they showed the ticket's own
  instruction was wrong.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer, which would spend the interruption the framing phase exists to spend
  once.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing — and the
`Status` column is ticked by whoever answered, never by whoever asked. Sorting
the rows this way is also what keeps the batch short enough to answer in one
sitting: two of the three kinds never needed a person at all.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.

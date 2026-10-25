# 1792368015-every-finding-carries-an-evidence-line — questions for the planner

## Decided from the tree, so nobody reopens them

The issue and the spawn prompt left these open. The tree answers each one,
and each is overturnable by opening the coordinate named.

- **The check needs no code.** `chain_check.py#finding_of` counts and matches
  every row the table places in a finding (`:1030-1055`). `severity:` and
  `answer:` are enforced that way with no constant naming them. A row is the
  whole change (`plan.md` Alternatives A, F).
- **How the check treats a record written before the row.** It does not read
  one. It opens only the records of the work items the pull request's own
  commits declare or change, found by the `--baseline` diff
  (`docs/the-review-record.md:209-216`, `chain_check.py#main`). No old record
  is rewritten, and no cut-over mechanism is added (`plan.md` Alternatives E,
  L).
- **The label is a new line, not part of `location:`.** `location:`'s paths
  are what a `fixed` commit must touch (`docs/the-review-record.md:91-99`)
  (`plan.md` Alternatives B).
- **The sealer's definition does not change.** Its step 3 gives a finding's
  verdict to the check (`agents/sealer.md:68-73`), so "the sealer re-runs an
  `executed` line where it weighs the finding" holds with nothing added, and
  no sealer side is owed (`plan.md` Alternatives J).
- **The last warden side stands as the baseline.** #967's `warden-phase-4.json`
  preload hashes equal `f10323f8`'s. The files the warden opens changed only
  outside the sections it reads. One paid side is planned, not two
  (`plan.md` §*Technical context*).
- **No file #943 owns is touched.** No such file states a finding's line set
  (`plan.md` §*Technical context*).
- **`## Confirmations` and the fix pass's `answer:` get no line.** The issue
  names findings (`spec.md` §*Scope*, Out).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | **Does a phase-3 `fail` on rule 5 alone, with every outcome grader holding, count as "measured not worse"?** Rule 5 (tokens read per tool call) is the one rule a side can fail with no sentence to blame. #967's warden failed it by 0.8% with its outcome up, and was recorded as it read and not re-run, because two takes of the same text differed by 6.8 points (`seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md:52-61`). #985's *Done when* says "measured not worse" and does not say how a noise-sized rule-5 fail reads. The tree cannot answer it: it is the bar for done and the money spent to clear it, which the owner holds | a person — the owner | **Record it** (the default): a rule-5-alone fail inside #966's spread, traced to no sentence, is recorded in `phases/phase-3.md` as #967's was, and the item ships. **Re-run**: one more side, about $42, total about $84, and whatever it reads is final. **Redesign**: a fail of rule 5 means the line costs context, and the warden's text is cut again before a second side | Record it | answered 2026-10-19 by the repository owner: record it |
| Q2 | **v0.22.2's release panel shows its `deferred` row as `not read`. Accept that, or make `release_seal.py` tolerate the missing line?** `release_seal.py#chain_counts` reads every record of every pull request in the release at the tag. One record its reader refuses sets the row to `not read` (`:305-394`, "an incomplete count is a wrong number"). The records of #966, #971, #976 and #978 predate the line. The tree decides the code: an exception in `release_seal.py` is a second grammar, which `docs/the-review-record.md:21` refuses. It cannot decide whether the owner accepts one release note with that row unread, a published surface only the owner answers for | a person — the owner | **Accept** (the default): the row reads `not read` for v0.22.2 only, the log line names the records, and from v0.22.3 every record carries the line. Merging this item last in 0.22.2 changes nothing, because the merged items' records already lack the line. **Exception**: `release_seal.py` reads verdicts through a reader that skips `evidence:`, a second grammar this frame rejects | Accept | answered 2026-10-19 by the repository owner: accept |
| Q3 | **What exact text does `agents/warden.md` carry, and does it fit in 27,172 bytes?** Rule 4 needs the warden's preload below the baseline's 27,173. Step 7 gains a label, and the probe sentence is rewritten as the absence rule | the work | Phase 2 writes it and counts it with `wc -c`. The probe sentence, about 230 bytes, is what pays for step 7's addition | The probe sentence is rewritten shorter than it stands | open |
| Q4 | **Does the new warden write the line on every finding, and does it leave earlier records' missing lines out of its findings?** | a measurement | Phase 3's 18 runs, read from `<out>.raw/` (`plan.md`, phase 3) | The step-7 read makes it write the line, and the S10 paragraph keeps earlier records out | answered 2026-10-19 by a measurement: phase 3's side at ba2a3187, all 39 findings carry the line, 28 `executed`, none raises a pre-row record (`phases/phase-3.md`) |

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
`Status` column is written by whoever answered, as `answered <date> by <who>`,
never by whoever asked. Sorting the rows this way is also what keeps the
batch short enough to answer in one sitting: two of the three kinds never
needed a person at all.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.

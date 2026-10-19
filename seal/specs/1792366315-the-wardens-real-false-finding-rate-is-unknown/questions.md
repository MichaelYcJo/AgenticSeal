# the warden's real false-finding rate is unknown (#971) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

## Judgments the issue left open that the tree answered

These were decided from the tree, and the grounds are in `spec.md` or
`plan.md`. They are listed so nobody reopens them as questions; overturn one
by opening its grounds.

1. **Step 1 cannot read the raw output, because it is gone.** It reads the
   committed side JSONs, which keep every row and reproduce every truth
   result. The issue's first comment's paraphrase is the only record of
   each finding's wording (`spec.md` §*What the issue's step 1 stands on,
   opened*).
2. **The classing is the comment's, carried and re-checked, not redone.**
   It was made while the traces existed. Redoing it from the rows alone
   would lose the finding text it was read with.
3. **"Recurs across runs" means at least two of a case's four runs**, the
   smallest count the word allows (`spec.md` §*Scope*, *Decided here*).
4. **A known limit the shipped round left standing is a truth.** A
   `truth-` grader is "a real or seeded defect" (`evals/README.md`).
5. **A different defect is its own grader, never a widening** of the truth
   it sits near.
6. **A `path#unit` location is never credited.** The grammar refuses it
   (`docs/the-review-record.md`, the `location:` row).
7. **The re-read is a new `regrade` subcommand, not `run --from-raw`**,
   whose input does not exist.
8. **The suite change touches only the warden's cases.** No other agent's
   suite tree moves, so #968 and #970 cannot meet it, and 0.22.2's decisions
   stay on af9c924b's suite as the owner decided.
9. **The scaffold artefacts and the reader's fenced-row fault are out.**
   Neither can be applied to rows already extracted. The owner files them
   for the next release (`spec.md` §*Scope*, *Out*).
10. **A change to the warden needs a fresh baseline run.** Its preload
    hashes at 8a100e13 differ from those its last side measured (#968's
    guard 1; `plan.md` §*Technical context*).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Should 0.22.2 add a rule to the warden against the `wrong` findings (the issue's step 3)? The tree cannot settle this. The comment finds one `wrong` row a side with **different** causes: an uncovered-test claim made without the coverage probe `agents/warden.md` already orders, and a 0.21-era replay target judged by the 0.22 record grammar. It also finds one shared trait: "both state what the tree has or lacks without checking it against the tree". Whether that trait is a cause worth a rule, at what cost, is a value somebody has to be accountable for | a person — the repository owner | **No rule (default).** Phases 1–4 only, $0. Step 3's condition, "where the wrong findings share a cause", is read as not met, and the done-when clause's "any rule added" is vacuous. **A rule.** Phase 5: one sentence in `agents/warden.md` naming the shared trait, with the preload cut by more bytes than the sentence adds (rule 4 fails a preload that is not smaller). It needs a baseline side at the tree this work starts from and a new side, both on af9c924b's suite: about **$36 a side, $72 together, up to about $108** with one fail-fixed-and-re-run. One row a side cannot show that the rule worked; the record can only show it was not worse | No rule. Phase 5 is not built and no paid run is scheduled | answered 2026-10-19 by the repository owner: no prose rule here; the shared trait is answered by a shape a check reads — every finding carries an `evidence:` line and a claim of absence is `executed` — in its own issue, #985, in 0.22.2. This work builds phases 1–4 and not phase 5 |
| Q2 | Does each historical finding behind replay-1791382684-r2's `truth-1` and `truth-2` name its further coordinates (the dozen units of 🟡1; `parse_section` at `unverified_check.py:76x`) in its `location` cell, or only in its text? | the work — phase 3 opens the round 2 record at the release tag `replay_targets.py --case` reads | **In the cell:** `truth_pattern` takes every coordinate the cell names, a generator rule. **Only in the text:** the input file widens the two graders with the coordinates the classing rows gave | Phase 3 decides when it opens the record, and writes a divergence row in `overview.md` either way | answered 2026-10-19 by the orchestrator, from `phases/phase-3.md`: only in the text — each Location cell holds one coordinate; `recurred_truths.json` widens truth-1 with the eight units the runs cited and truth-2 with `unverified_check.py:767`; the divergence row is in `overview.md` |
| Q3 | Do the generators, unchanged, regenerate the nine committed warden cases byte for byte at this work's base? | a measurement — phase 3's first step: `--case` for each case, then `git status --porcelain evals/behaviour/` | **Empty diff:** proceed. **Any diff:** the committed suite is not what its generators write. Phase 3 then stops adding truths to that case, records which file differs and why in `overview.md`, and the orchestrator decides whether that case is regenerated (a suite change of its own) or left out of the added truths | Proceed only on an empty diff, case by case | answered 2026-10-19 by the orchestrator, from `phases/phase-3.md`: empty diff — at 9ff7bbca all nine warden cases regenerated byte for byte (`git status --porcelain evals/behaviour/` empty) |
| Q4 | How does each row of the comment map to a run index and row index of the JSON, where a comment row groups both runs (`r0.F4, r1.F3`) or holds lines inside a fence? | the work — phase 1, by matching `location:` text within each run | The table has one row per JSON row, so a grouped comment row becomes two. A fenced line is its own row, classed `remark (fenced)` | One row per JSON row; the join command is the arbiter | answered 2026-10-19 by the orchestrator, from `phases/phase-1.md`: the comment's `rN.FM` is run N, row M-1 of that run's `report_rows` for every false row, confirmed by a script over the table; a comment row grouping both runs is one table row per run; the two fenced lines are rows 5 and 6 of phase 3's replay-1791382684-r2 run 0. The join exits 0 at fc3d7b71 |

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

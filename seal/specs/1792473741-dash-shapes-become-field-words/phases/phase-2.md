# 1792473741-dash-shapes-become-field-words — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 307b8198 |

## What this phase was asked

The sealer's verdict in field words (S5 to S9). `chain_check.py` reads the
line whole as `Verdict: sealed`, `Verdict: withheld reason: <…>` or
`Verdict: undecided question: <…>`, refuses a near miss at its line, and
refuses an earlier run's entry on the `Target SHA` row that is not the word
alone. `RETIRED_SAYS` names the new shapes. `templates/sdd-guarantee.md`
(the verdict, the earlier run, `does not hold:`), `agents/sealer.md`,
`skills/code-review/orchestration.md` and `templates/config.md` are
rewritten, with the verdict lines in the three test files that pin them. The
stamp reads through `chain_check.py`'s `verdicts_of`, `verdict_word` and
`earlier_verdicts`, so it changes with them.

## What this phase found

- **`verdicts_of` returns the whole line now.** A near miss such as
  `**Verdict:** sealed` has no value apart from its label, so the reader
  hands back each line that means the verdict (`MEANT_VERDICT`) and
  `verdict_word` reads it whole: a word for one of the three shapes, a
  retired word for `sound`, `not sound` and `undecidable`, else None. The
  stamp and the commit gate compare with `SEALED` and needed no edit.
- **An earlier run reads `<sha> <word>`, with `against <base>` after the SHA
  where it names one, and no emphasis** (`EARLIER_ENTRY`). An entry that is
  not one comes back as `(entry, None)`, which the stamp reads as no seal and
  the guarantee arm refuses at the `Target SHA` row's line.
- **Two merged guarantees show no verdict line to the reader, before this
  phase and after it.** The guarantees of `1792449518` and `1792459424` each
  hold `Verdict: sealed`, and `verdicts_of` returns nothing for either, at
  17cfa9e3's `chain_check.py` as at this phase's. Each holds a comment
  opener inside a code span of a table cell (lines 45 and 17), and
  `unverified_check.py#readable` blanks every line after it, the verdict
  line included (executed). That is the reader's, not this item's, and is
  handed back as a leftover. The other 11 read: 10 `sealed` and the retired
  `sound`. All 13 earlier-run
  entries read as `withheld`.
- **Two mutations survived the first cases.** A reason after two spaces
  read as a reason with `\S` dropped from the shape, and a guarantee with no
  verdict line was named by no case. A case was added for each, and both
  mutations then went red. The nested-repeat mutation of `MEANT_VERDICT`
  timed out after 30 s with no verdict, as phase 1's did.
- **`bin/settle --released-at HEAD` holds this spec for its open row**, the
  broad run `overview.md` leaves to the orchestrator, and reports no parse
  error. Its `## Rule changes` parsed and listed as pending at phase 1,
  before `overview.md` existed.

# 1792251842-the-smith-is-written-anew-from-its-job — review round 4

target: 8ee1c118, fixes fb431c2b..8ee1c118

## Findings

none

## Confirmations

confirms: round-3#1
Holds. The memo now states one item total, 233.3384, and every sentence
about the total agrees with the rows and the phase records under the
rounding rule round 3 named (each side's `costUsd` rounded to four places,
then summed).

Executed. Row 36 of `overview.md` at 8ee1c118 is byte for byte the
`+` line of round 3's paste-ready fix (`rounds/round-3.md:42`): a Python
comparison of the two lines returned `True`. Its Chosen cell no longer
says "the item's total is 227.8875"; it says the second take "brought it to
227.8875" and that "the smith's third take in the row below brings it to
233.3384". The sums it states recompute in decimal arithmetic: 104.1452 +
60.5128 = 164.6580, 164.6580 + 63.2295 = 227.8875, 227.8875 + 5.4509 =
233.3384. Row 37's 233.3384 = 104.1452 + 129.1932 also recomputes, and
60.5128 + 63.2295 + 5.4509 = 129.1932.

Read. The class is every statement of an item or phase total in the work
item's records outside `rounds/`. A `git grep` for 227.887, 233.338,
164.658, "item's total", "evaluation total" and "in all" finds
`overview.md:23` (phase 1, 104.1452 in all), `:36` and `:37` (the two
rows above, now agreeing), `phases/phase-1.md:145` (104.1452),
`phases/phase-4.md:92` (123.7423 for the first two takes, followed at
`:111` by "the phase's spend becomes 129.1932" with the third take), and
`phases/phase-5.md:81` and `:85` (227.8875 before the third take, a phase
record that stays as written, as round 3 already said). None of them states
a present-tense item total other than 233.3384. The phrase "the item's
total" no longer appears in the memo.

The record commit 8ee1c118 changes only `rounds/round-3.md`'s `verdict:`
line to `fixed 65c596fd` and its `answer:` line; 65c596fd changes only
`overview.md` line 36 and is an ancestor of 8ee1c118, and `overview.md` is
the finding's `location:`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck on this branch | the branch at 8ee1c118 | the orchestrator's broad gate |

## Probes

| Command | Result |
|---|---|
| `git diff fb431c2b..8ee1c118` and `git show --stat` on 65c596fd and 8ee1c118 | two files: `overview.md` one line, `rounds/round-3.md` the `verdict:` and `answer:` lines |
| a Python comparison of round 3's paste-ready `+` line with `overview.md` line 36, and the `Decimal` sums of the row's figures | exit 0: `True`; 164.6580, 227.8875, 233.3384, 233.3384, 129.1932 |
| `git grep -n -E` over the work item outside `rounds/` for the totals and for "item's total", "evaluation total" and "in all" | the statements listed under `## Confirmations` |
| `git merge-base --is-ancestor 65c596fd 8ee1c118` | exit 0 |
| `chain_check.py --baseline origin/release/v0.22.1 --worktree` on the checkout, with this record on disk | exit 0; the pull request's state unknown, and no `broad-gate.md` or `guarantee.md` yet, both reported as not due |
| `bin/test` over `tests/test_unverified_rows_close.py`, `tests/test_docs_line_wrap.py`, `tests/test_one_word_one_meaning.py`, `tests/test_no_real_identifiers.py` and `tests/test_the_record_is_written_in_words.py`, `-q`, with this record on disk | exit 0: 291 passed |

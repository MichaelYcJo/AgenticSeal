# Closing memo: 1793411151-judgment-where-meaning-is-the-question

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and `seal gate` over the branch | the orchestrator, by `seal gate --base release/v0.26.0 --record` after the review rounds settle |
| How GitHub renders `chain_check.py`'s `::notice` `not read:` lines in the hygiene workflow's run and annotations; the case pins the text printed, not the rendering | the orchestrator, at the first CI run of the pull request that carries a line the check did not read |

## Not done

`frame/design.md` *Scope* item 4, the removal of
`tests/behaviour/test_one_word_one_meaning.py`, is not built. Three `check:`
lines under the policy root name the module, and a pull request does not edit
the policy root. `trail/phases/phase-1.md` gives the grounds and the places
the removal owes.

The fourth scenario's clause that the `refixes:` line "is printed as not
read" is not built. `refixes` is no label's word, so the net *Scope* item 5
derives from the labels does not name it, and the frame removes the list of
old spellings that would. `trail/phases/phase-2.md` gives the grounds and
the measurement of a wider net.

# Closing memo: 1793411151-judgment-where-meaning-is-the-question

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and `seal gate` over the branch | the orchestrator, by `seal gate --base release/v0.26.0 --record` after the review rounds settle |
| How GitHub renders `chain_check.py`'s `::notice` `not read:` lines in the hygiene workflow's run and annotations; the case pins the text printed, not the rendering | the orchestrator, at the first CI run of the pull request that carries a line the check did not read |
| Whether a `seal rules: not read:` line reaches anyone at a pull request: CI runs `seal rules --check` only inside `tests/github/test_rules.py#test_every_check_line_in_the_tree_holds`, which asserts exit 0 and captures the output, so a near check line in a rule file prints where nobody looks, and only a reader of the rule file's diff catches it | the proofer, at review of each diff that touches a rule file |
| `tests/skills/test_deferral_check.py` on Windows: the cases build a workflow's printed path with `os.path.join` to match the tool's `os.path.relpath`, and ran on macOS only | the orchestrator, at the Windows legs of the pull request's CI run |
| Whether an agent that writes an `unverified` row opens each CI file `seal deferrals` names and reads its trigger; the tool's exit 0 no longer says the file runs before the merge | the proofer, at review of each round record or closing memo whose row defers to CI |

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

`seal deferrals`' `runners_in` still ends a line at U+2028, so a runner word
after that character inside a comment is read as a command line. The frame
keeps `runners_in` as it is, and the reader the trigger line sends to the
file sees the comment. `trail/phases/phase-4.md` gives the measurement.

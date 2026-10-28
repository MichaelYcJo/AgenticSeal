# Overview: 1793169128-spawn-rows-push-cells-past-the-header

## Why this work exists

`seal cost --spawns` printed a spawn row whose agent name was longer than the
label column with every cell shifted to the right of its header, so a reader
took one column's number for the next; the label is now cut to the column,
and each cell stays under its header whatever the name.

## Where spec and implementation diverged

None. The frame held at this tree, and the build followed it.

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch | the orchestrator, through `seal gate` |

## Not done

`.test_durations` has no price for the new case. `CONTRIBUTING.md` says the
file is refreshed from the `test-durations` artifact of the branch's latest CI
run, and `test_the_durations_file_prices_the_suite` passes with up to one
collected case in twenty unpriced, so a hand-written price would only be a
guess.

## Fed back into the spec

none

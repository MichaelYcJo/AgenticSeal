# Overview: 1793226630-most-contract-rules-are-proved-by-their-own-wording

## Why this work exists

The contract module pinned a phrase of every rule's own wording, which
turned a rule reworded to the same meaning red and caught nothing on
record. It now pins only rule 1's command forms and rule 11's root
spellings, and it reads that every rule carries one `check:` line. Each
rule's `check:` line names what reads the rule.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| A command spelling in the count | `frame/design.md` *Data & interfaces* lists the literals the count leaves out, and a command spelling is not among them. Phase 2 left out 24 command literals as a kind of their own | the build | `frame/questions.md` judgment 2: "A command spelling an agent copies into a shell is a fact a reader needs fixed." Counted as prose, the total would be 279, and `trail/phases/phase-2.md` says so |
| The bound on the count | `frame/design.md`: "The issue's rough figure of 182 for `tests/text` bounds the count from above." The method counts 255 | the count | The method as written. A line grep for `assert "<literal>" in` over the same files finds 320 lines, so 182 is not a bound under either reading |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch, including `test_the_durations_file_prices_the_suite` against six unpriced case ids and the removed ones | the orchestrator, through `seal gate` |
| How the issue reached its rough figure of 182 | the owner, who wrote it on #1111 |
| Whether the four crafter eval cases and the two sealer eval cases that rules 2, 4, 7 and 15 now name pass on a run | the orchestrator, at the next preload rewrite that runs the behaviour evals |

## Not done

`.test_durations` is not refreshed. `CONTRIBUTING.md` refreshes it from a
`tests` run's artifact, and this branch has had no such run.

The phrase pins on contract sentences in other modules, which
`frame/design.md` *Scope* puts out, are not decided here. Those under
`tests/text` are in phase 2's count.

## Fed back into the spec

none

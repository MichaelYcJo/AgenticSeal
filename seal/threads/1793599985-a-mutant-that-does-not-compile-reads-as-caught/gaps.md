# Closing memo: 1793599985-a-mutant-that-does-not-compile-reads-as-caught

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the branch's head | the orchestrator's broad gate, `seal gate --base release/v0.29.0 --record` this work item |
| The new cases of `tests/skills/test_mutation_check.py` on CI's `windows-latest` legs (`questions.md` Q1) | the orchestrator, reading the four Windows legs of the pull request's CI run |

## Not done

The `--replace` help sentence that names the compile is pinned by no case. It is prose a person reads in `--help`, beside the docstring and the skill's section, which say the same and are read at review (design S8). A case asserting a help string would pin wording rather than behaviour.

`skills/verify/scripts/arm_check.py` keeps `ast.parse`, as design G3 and *Scope* Out decide: its two operators cannot produce the compile-only errors.

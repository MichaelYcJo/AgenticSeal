# Closing memo: 1793457437-readers-state-the-shapes-they-pass

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check over the whole tree after phase 1. The phase-boundary set of 57 modules is a sample built from three searches (`trail/phases/phase-1.md`), so a module reaching a changed path through a helper none of them names was not run. | the orchestrator, by `seal gate` with the `Broad gate` row of `seal/config.md` |
| The full suite, the repository-wide lint and the format check over the whole tree after round 1's fix pass. Its boundary set of 67 modules is a sample built from two searches: modules that name a changed path or a work item's records, and modules that walk the tree through `git ls-files`, `os.walk` or a glob. | the orchestrator, by `seal gate` with the `Broad gate` row of `seal/config.md` |

## Not done

A case in `tests/skills/test_fold_check.py` holding that the fold reads `docs` under a `| Policy Root | … |` row was within reach and not written. `skills/settle/scripts/fold_check.py#declared` reads its items through `hooks/lib/config.py#value_of`, which the new case in `tests/hooks/test_config.py` pins, so a second case would cover nothing the first does not.

# Closing memo: 1794376287-check-lines-ride-in-every-preload

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate at the work item's HEAD. Phase 1 ran S6's modules and the phase-boundary set that `trail/phases/phase-1.md` names, and did not run the broad gate. | the orchestrator, by `seal gate --record` |
| Test files outside the phase-boundary run that read a changed file. The run took `tests/text`, `tests/behaviour` and the files a `git grep -l` on `agents/`, `agent-contract` and `rule-changes` listed. A file that reaches those paths under another spelling was not run, so that list is a sample. | the orchestrator, by the broad gate |
| Test files outside fix pass 1's run that read a file the pass changed. After `bceb31f1c`, one `bin/test` command ran `tests/text`, `tests/behaviour`, `tests/test_censuses.py`, which runs the `tests/censuses.py` that search listed, and the 18 test files a `git grep -l` on `README` and `rule-changes` listed outside those two directories, and gave 4,669 passed and 9 skipped. A file that reaches `README.md`, `README.ko.md` or `skills/settle/rule-changes.md` under another spelling was not run, so that list is a sample. | the orchestrator, by the broad gate |
| Test files outside fix pass 2's run that read a file the pass changed. The pass changed the same three files as fix pass 1, plus `changelog.md`. After `d322c0cb7`, the same one `bin/test` command as fix pass 1 gave 4,669 passed and 9 skipped, `tests/behaviour/test_docs_line_wrap.py` and `tests/behaviour/test_both_editions_carry_the_same_folds.py` among them. The list is the same sample. | the orchestrator, by the broad gate |
| Whether the sealer still withholds on a missing or stale `trail/gate.md` without the rule *A missing or stale gate record earns what step 1 says.* The rule's line named `evals/behaviour/sealer/rule-sealer-no-gate/` and `evals/behaviour/sealer/rule-sealer-stale-gate/`, and no eval case was run in this phase. Step 1 states the verdict whole, and it now cites rule 2. | the owner, by the eval run of the release |

## Not done

nothing

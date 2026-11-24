# Closing memo: 1795483768-chain-check-asks-git-the-same-question-twice

## Not verified

| Item | Who must answer |
|---|---|
| Whether `tests/skills/test_chain_check.py` and `tests/skills/test_settle.py` read a lower ratio than the control modules on the Windows leg of `tests` after phase 1 (`frame/design.md` S8). No local figure stands in for the leg. | the orchestrator, from the `workflow_dispatch` run at phase 1's commit against the baseline run at `c66128300` |
| How many processes `chain_check.main` starts over #1581's branch after phase 1, and whether it repeats none (`frame/design.md` S9). The phase did not run the probe. | the orchestrator, from S9's probe over a fresh clone at phase 1's commit |
| Whether a test file that reaches `lib/gitcmd.py` only through another module, outside the 34 paths phase 1's boundary run named, passes with the memo in place. The boundary set took the test files whose text names `gitcmd`, `chain_check`, `settle.py`, `settle.main`, `seal settle` or `pr_body`, and `tests/text` and `tests/behaviour` (`trail/phases/phase-1.md`). | the orchestrator's broad gate |

## Not done

nothing

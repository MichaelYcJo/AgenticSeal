# Closing memo: 1795483768-chain-check-asks-git-the-same-question-twice

## Not verified

| Item | Who must answer |
|---|---|
| closed Whether `tests/skills/test_chain_check.py` and `tests/skills/test_settle.py` read a lower ratio than the control modules on the Windows leg of `tests` after phase 1 (`frame/design.md` S8). No local figure stands in for the leg. | the orchestrator: runs 45307666454 at `c66128300` and 45309515939 at `541d15e3b` read no saving out of the leg's spread (`frame/plan.md` *Judgments of the run*, the row on S8) |
| closed How many processes `chain_check.main` starts over #1581's branch after phase 1, and whether it repeats none (`frame/design.md` S9). The phase did not run the probe. | the orchestrator: 85, none repeated, at `1ecdde329` (`frame/plan.md` *Judgments of the run*, the row on S9) |
| closed Whether a test file that reaches `lib/gitcmd.py` only through another module, outside the 34 paths phase 1's boundary run named, passes with the memo in place. The boundary set took the test files whose text names `gitcmd`, `chain_check`, `settle.py`, `settle.main`, `seal settle` or `pr_body`, and `tests/text` and `tests/behaviour` (`trail/phases/phase-1.md`). | answered: the work item's broad run, `trail/gate.md` at `e5a21562e` against `fe09bef46`, on which `guarantee.md` sealed |
| closed Whether `tests/skills/test_chain_check.py` and `tests/skills/test_settle.py` read a lower ratio than the control modules on the Windows leg of `tests` after phase 2 (`frame/design.md` S8). No local figure stands in for the leg. | the orchestrator: runs 45307666454 at `c66128300` and 45311061260 at `c45339551` read no saving out of the leg's spread (`frame/plan.md` *Judgments of the run*, the row on S8) |
| closed How many processes `chain_check.main` starts over #1581's branch after phase 2, against the 37 `frame/design.md` S9 expected at `c66128300`, before round 1's fold. The phase did not run the probe. | the orchestrator: 39, none repeated, at `cde1d5925` (`frame/plan.md` *Judgments of the run*, the row on S9) |
| closed Whether a test file outside the 38 paths phase 2's boundary run named passes with the declarations read through one batch and `decoded` and `batch_texts` in `lib/gitcmd.py` (`trail/phases/phase-2.md`). | answered: the work item's broad run, `trail/gate.md` at `e5a21562e` against `fe09bef46`, on which `guarantee.md` sealed |

## Not done

`tests/lib/test_gitcmd.py` holds no `Test_decoded` and no `Test_batch_texts`, though `CONTRIBUTING.md` *The test layout* gives each public function of `lib/gitcmd.py` a class there, and `seal layout --check` reports both as missing. Phase 2 moved both units from `skills/settle/scripts/settle.py` with their bodies unchanged. `frame/plan.md` phase 2 names `tests/skills/test_settle.py` `Test_blobs` as their proof, and a case in either class would watch nothing `Test_blobs` does not (`trail/phases/phase-2.md`). Moving `Test_blobs`'s cases would leave `settle.py#blobs` with no class of its own.

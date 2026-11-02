# Closing memo: 1793599986-a-stopped-head-run-does-not-seal

## Not verified

| Item | Who must answer |
|---|---|
| Whether this repository's own `Broad gate` row, `bin/test -q`, leaves any pytest session at `HEAD` stopped part-way, so that the new arm fails this branch's own broad run (`frame/questions.md` Q1) | the orchestrator's broad run, `seal gate --base release/v0.28.1 --record` this work item |
| The two new gate cases, `pytest.exit()` with a return code of 0 and `os._exit(0)`, ran on macOS with pytest 9.2.0 alone; they have not run on Linux or Windows | the pull request's CI test job on its Linux and Windows legs |

## Not done

No case covers a suite in which a test fails before a later test calls `pytest.exit()` with a return code of 0. In that run the row exits 0, the record holds a failing file, and the gate runs `compare_at_base` for it. The new arm only lets an exit-0 suite into the failure loop; the comparison path after it is the existing one, and `Test_compare_at_base` and the exit-1 cases of `Test_gate` cover it. A case for this combination would test that path again under a second way of entering it, so I did not add one (`trail/phases/phase-1.md` *The frame, checked before the build*).

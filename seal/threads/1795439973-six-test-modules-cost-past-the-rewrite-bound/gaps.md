# Closing memo: 1795439973-six-test-modules-cost-past-the-rewrite-bound

## Not verified

| Item | Who must answer |
|---|---|
| What `tests/skills/test_settle.py` sums to on the Windows leg of `tests` after phase 1. Phase 1's record estimates it from the local run, above 60 s, and states why. | the orchestrator, by the `workflow_dispatch` run and the sum `frame/design.md` S1 gives, once the review rounds settle |
| Whether the `gh` stub's first run of a new file also costs a scan on the Windows leg, as it costs 0.4 s on macOS. Phase 1 writes the stub once per module either way. | the same run's `test-durations` artifact, read by the orchestrator: the local-mode cases of `tests/skills/test_settle.py#Test_main` against their figures in run 45181872904 |

## Not done

Phase 1 did not turn the cases of `tests/skills/test_settle.py#Test_main` that read text into unit calls on `settle.py`'s readers. The frame scoped this module to building its worlds once (`frame/design.md` *Scope* item 1), and phase 1's record shows that the command's own git processes alone hold the module above 60 s on the Windows leg. Bringing it under 60 s would move most of the 137 `Test_main` cases off `main` over a real history. Whether that is owed is the orchestrator's to decide with the framer, since it is a rebuild the frame did not plan.

Phase 1 did not change `tests/conftest.py#tree`, which still builds a repository with `git init` and a commit for each of the 20 cases of `Test_report`, `Test_apply` and `Test_module` that take it. A change to `tests/conftest.py` puts every test file in the phase boundary's set, which contract rule 2 leaves to the orchestrator. A copy of the fixture's world built inside `test_settle.py` would define one world in two files, which `CONTRIBUTING.md` *The test layout* refuses for a helper two test files use.

Phase 1 did not trim the `git rev-parse HEAD` that `tests/conftest.py#commit_everything` starts after each commit, 296 processes and 3.9 s of the module's local run. The frame lands the module's commit helper on `commit_everything` (`frame/design.md` *Removes*), and making it cheaper is a change to `tests/conftest.py`, with the same consequence as above.

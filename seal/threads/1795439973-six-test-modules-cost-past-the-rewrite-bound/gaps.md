# Closing memo: 1795439973-six-test-modules-cost-past-the-rewrite-bound

## Not verified

| Item | Who must answer |
|---|---|
| What `tests/skills/test_settle.py` sums to on the Windows leg of `tests` after phase 8. Run 45189798316 put it at 208 s after phase 1, a ratio of 0.82 that falls inside the range of the modules no phase changed (`frame/design.md` *Grounding*, *What a figure of the Windows leg can show*). | the orchestrator, by the `workflow_dispatch` run at phase 8's Status commit and the sum `frame/design.md` S1 gives |
| Whether the `gh` stub's first run of a new file also costs a scan on the Windows leg, as it costs 0.4 s on macOS. Phase 1 writes the stub once per module either way. | answered by the framer from run 45189798316: a cost of macOS that the Windows leg did not show (`frame/design.md` *Grounding*, *What a figure of the Windows leg can show*) |
| What the seven arm classes of `tests/skills/test_chain_check.py` cost on the Windows leg after phase 2. Their local run fell from 73.9 s to 20.0 s, which is no evidence of the leg (`trail/phases/phase-2.md`, the second of the four parts). | the orchestrator, by the `workflow_dispatch` run at phase 3's Status commit, which closes the module (`frame/design.md` S1) |

## Not done

Phase 1 did not turn the cases of `tests/skills/test_settle.py#Test_main` that read text into unit calls on `settle.py`'s readers. The frame scoped this module to building its worlds once (`frame/design.md` *Scope* item 1), and phase 1's record shows that the command's own git processes alone hold the module above 60 s on the Windows leg. Bringing it under 60 s would move most of the 137 `Test_main` cases off `main` over a real history. The orchestrator decided that rebuild after run 45189798316, and the frame takes it as phase 8 (`frame/plan.md` *Judgments of the run*).

Phase 1 did not change `tests/conftest.py#tree`, which still builds a repository with `git init` and a commit for each of the 20 cases of `Test_report`, `Test_apply` and `Test_module` that take it. A change to `tests/conftest.py` puts every test file in the phase boundary's set, which contract rule 2 leaves to the orchestrator. A copy of the fixture's world built inside `test_settle.py` would define one world in two files, which `CONTRIBUTING.md` *The test layout* refuses for a helper two test files use.

Phase 1 did not trim the `git rev-parse HEAD` that `tests/conftest.py#commit_everything` starts after each commit, 296 processes and 3.9 s of the module's local run. The frame lands the module's commit helper on `commit_everything` (`frame/design.md` *Removes*), and making it cheaper is a change to `tests/conftest.py`, with the same consequence as above.

Phase 2 did not add a case for mutant 8 of its mutation table, `_read_tree`'s `if not in_corpus(path)` made `if False`. It survives the test file at `a6f69fbba` too, so the gap predates the phase. With the skip gone, `rule_changes.py#copies` still leaves the same paths out (`skills/settle/scripts/rule_changes.py:578`), and only an undecodable `*.md` outside the corpus would gain a not-read notice. A case that plants such a file would add a fact, and the frame rebuilds existing cases (`frame/design.md` *Scope* item 2).

Phase 2 did not change `tests/conftest.py#commit_everything`, which `tests/skills/test_chain_check.py` imports as `commit`. Its `git rev-parse HEAD` after each commit is the one phase 1 names above. The bodies of the seven arm classes now hold 28 call sites of a commit helper, against 97 at the base (executed: the census `trail/phases/phase-2.md` names in its fourth part), so the trim would save this module little.

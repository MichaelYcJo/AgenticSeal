# Review round 4: 1793169127-pact-check-reads-the-retired-grammar

target: c007e612, fixes 2aa5cbf1..c007e612

## Findings

None. Round 3 closed no finding, so none is owed an answer here. The merge
left this branch's own change byte for byte as it was. The two renamed
cases say what they assert.

## Confirmations

confirms: none
The merge `8f9bff17` changed nothing in this branch's own diff. Executed: the branch's diff against its cut (`977b6613..2aa5cbf1`) and the merge's diff against the release tip it took in (`c825fd2c..8f9bff17`) have the same added and removed lines. Both have 3031 lines with nothing between them, and both stats read 29 files, 1917 insertions and 1114 deletions. The merge resolved `tests/conftest.py` with no combined hunk (`git show --cc`, executed). Executed: the release side brings back none of the names this work removes. The search `plan.md` *Technical context* writes out, run at `c007e612`, printed nothing, and so did a search for `named=`.

confirms: none
The two new names match what each case asserts. `test_accepts_a_deeper_heading_as_part_of_its_section` (`tests/skills/test_coordinates.py:33-42`) asserts that `## A`'s region, lines 5 to 12, runs past `### A1` to the line before `## B`. That is a deeper heading accepted inside its parent's section, which is also what the docstring says. `test_refuses_an_indented_heading_as_the_start_of_a_section` (`:56-61`) asserts that `    ## B` has no heading level. It also asserts that `## B` resolves only to the real heading at lines 5 to 7, so the indented line opens no section. The bodies and docstrings are unchanged (read, `git diff 8f9bff17 c007e612`). The class now holds one case of each prefix `skills/verify/scripts/test_layout.py` requires. Executed: `bin/seal layout --check` read 158 files and refused none.

confirms: none
The defect the gate found was in the branch from phase 3 and not from the merge. *Test_heading_path* was built in `3f807db1` from six resolver cases, none named `test_accepts_` or `test_refuses_`. Round 1 read that class and judged its cases, and did not run `seal layout --check` over the branch. That is how it passed review. The rename's commit fixes the defect and makes none, so no finding names a regression.

confirms: none
The modules the merge and the rename touch pass at `c007e612`: `tests/skills/test_coordinates.py`, `tests/skills/test_test_layout.py`, `tests/skills/test_pact_check.py` and `tests/hooks/test_config.py`, 426 passed, exit 0 (executed). The pact world in `tests/conftest.py` survived #1058's sweep, and `test_pact_check.py` reads it.

Carried rather than re-established: round 3's coordinates for the anchor reader and `gfm_table`. The merge diff shows they did not move, so they were not opened again. The `.test_durations` keys under `Test_resolve_unit` are stale from phase 3. `design.md` *Out, and whose* leaves that file to the orchestrator's broad run.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck after `c007e612`. The broad run before it is spent by this commit | the branch | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `git diff 977b6613 2aa5cbf1` and `git diff c825fd2c 8f9bff17`, each reduced to its added and removed lines, then `diff` of the two | no difference, exit 0. Both have 3031 lines |
| `bin/test tests/skills/test_coordinates.py tests/skills/test_test_layout.py tests/skills/test_pact_check.py tests/hooks/test_config.py -q`, in a clone at `c007e612` | 426 passed, exit 0 |
| `bin/seal layout --check`, in the clone | 158 files read, 0 refused, exit 0 |
| `git grep -n -w -E` over the names `plan.md`'s S11 search lists, and `named=`, at `c007e612` outside `seal/`, the changelogs and `.test_durations` | nothing, exit 1 |

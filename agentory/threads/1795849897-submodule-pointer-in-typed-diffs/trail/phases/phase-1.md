# Phase 1: 1795849897-submodule-pointer-in-typed-diffs

## What this phase found

- `seen red`: `tests/behaviour/test_the_inspector_inspects.py::TestDefinition::test_step_2_reads_the_diff_with_submodules_shown` and `tests/behaviour/test_the_proofer_reads_a_merge_round.py::test_a_merge_round_reads_the_branch_and_the_resolution_with_submodules_shown` failed against the routing commit `4a63fef1`, each on its missing command, and pass after the edit (`executed`).
- No module held a case of `agents/proofer.md`'s paragraph on a round after a merge, so its case starts a module of its own under `tests/behaviour/`, beside the inspector's.
- The frame named only the two reads the issue names. Its probe showed `git show <merge>` hides a resolution that moves the pointer as well, so the phase gave it the flag too. That is a third read inside the frame's *Scope*, not a departure from it.

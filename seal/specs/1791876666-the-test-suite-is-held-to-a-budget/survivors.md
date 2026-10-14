# Survivors — the test suite is held to a budget

`survivor-check --range 0f2b8a33..HEAD` at a0d9201f reported two places that
still carry wording this branch removed. Both stand. The removed text was two
end-to-end cases' docstring and name, folded into one parametrized case
(46cf830a). Neither was a sentence corrected for being false.

`survivor-check --range 08f1c8a2..HEAD` at 00233d87 reported eight more, all
wording of the per-script floor guards the launcher replaced. Each stands in a
record of what was true when it was written: six in released ledger files,
which this repository's `Ledger frozen from` keeps unchanged and #944 removes,
and two in other work items' plans.

| Path | Quote | Grounds |
|---|---|---|
| `.github/scripts/case_check.py` | `**What nothing kills is a report, not a gate.**` | The module docstring's rule, and it still holds: the merged case's row *a mutant of changed code nothing kills is reported* asserts it. Only the old case's docstring, which said the same thing, left |
| `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/overview.md` | `the check derives each case's mutants from the lines it runs alone, the units it names and the changed shipped lines` | The divergence row describes the check as built, and that is unchanged. The match is the removed case name `test_a_tests_only_change_draws_its_mutants_from_the_lines_it_runs`, now a row of `test_each_real_path_end_to_end` · NAME NOT IN TREE: removed by 46cf830a |
| `seal/releases/0.9.1.md` | `sites are untouched, on grounds and not on taste.` | A released ledger row about `round_record.py`'s guard as 0.9.1 shipped it; the file is frozen and #944 removes it |
| `seal/releases/0.9.1.md` | `carries it in full.` | The same released row's pointer to its work item's spec; frozen, and removed by #944 |
| `seal/releases/0.9.1.md` | `round_record.py#below_floor@d1565fbf` | A released row's anchor on the removed guard; frozen, and removed by #944 |
| `seal/releases/0.9.1.md` | `(3.9.6) on macOS, before and after` | A released row's measurement of the guard on 3.9; frozen, and removed by #944 |
| `seal/releases/0.9.1.md` | `Re-verified 2026-09-08 after review round 1` | A released row's re-reading of the guard's ASCII sentence; frozen, and removed by #944 |
| `seal/releases/0.15.4.md` | `look each sibling's purpose up by path` | A released row about the loaders' sibling sentences, which this range left as they were; the match is a removed case's docstring. Frozen, and removed by #944 |
| `seal/specs/1790260563-the-fold-checks-run-only-as-this-repositorys-tests/plan.md` | `carries the interpreter-floor guard copied from` | Another work item's plan, recording what its framer read then; a record, not a statement about the tree |
| `seal/specs/1790690762-arm-check-reads-every-supported-ast/plan.md` | `It skips where uv or those interpreters are absent, which is every CI runner.` | Another work item's plan about `arm-check`'s cases; the match is a removed case's docstring, and the plan's sentence is about its own case |

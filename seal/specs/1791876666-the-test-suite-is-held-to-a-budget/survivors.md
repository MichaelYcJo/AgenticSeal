# Survivors — the test suite is held to a budget

`survivor-check --range 0f2b8a33..HEAD` at a0d9201f reported two places that
still carry wording this branch removed. Both stand. The removed text was two
end-to-end cases' docstring and name, folded into one parametrized case
(46cf830a). Neither was a sentence corrected for being false.

| Path | Quote | Grounds |
|---|---|---|
| `.github/scripts/case_check.py` | `**What nothing kills is a report, not a gate.**` | The module docstring's rule, and it still holds: the merged case's row *a mutant of changed code nothing kills is reported* asserts it. Only the old case's docstring, which said the same thing, left |
| `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/overview.md` | `the check derives each case's mutants from the lines it runs alone, the units it names and the changed shipped lines` | The divergence row describes the check as built, and that is unchanged. The match is the removed case name `test_a_tests_only_change_draws_its_mutants_from_the_lines_it_runs`, now a row of `test_each_real_path_end_to_end` · NAME NOT IN TREE: removed by 46cf830a |

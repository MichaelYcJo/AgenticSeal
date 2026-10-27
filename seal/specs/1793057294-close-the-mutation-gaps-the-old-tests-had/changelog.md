### Changed

- **The mutation gaps #942's proof found in the old tests are closed (#1017).** #942 recorded 180 rows, each a mutant of shipped code or of a test helper that survived both its rebuilt test files and the old ones. Each of the 146 rows whose code still stood was rebuilt at the branch head with `bin/mutation-check`, and each of the 34 whose code had gone was traced to the commit that removed it, so every row has one outcome. 121 are killed by a case seen red on the mutant and green on the code, 9 were already killed by a case that stood, 16 are equivalent with the reason written from the code, and 34 left the tree with the code they mutated. No mutant showed a defect in shipped code. `tests/test_implementer.py` is new, so `hooks/implementer.py` has a test file of its own. The tables per module, with each replacement as it was run, are in the work item's phase records.

### Removed

- **`gh_json` in `.github/scripts/close_issues_on_release.py` (#1017).** Nothing in the tree called it, and its one surviving mutant leaves with it.

# Closing memo: 1793922919-three-link-cases-skip-on-windows-by-platform

## Scope confirmation

The three link cases of `tests/skills/test_agentic_pytest_record.py` that issue #1247 names make their links through `tests/conftest.py#symlink_or_skip` in place of `Path.symlink_to`, and their three `skipif(os.name == "nt")` decorators are removed; no other file of the suite changes.

## Not verified

| Item | Who must answer |
|---|---|
| Whether the three cases pass on the `windows-latest` legs, or skip there with `symlink_or_skip`'s reason, now that they try to make links there. This macOS machine cannot read it | the orchestrator's `gh workflow run tests --ref test/1247-three-link-cases-skip-on-windows-by-platform` run, read from a Windows leg's `SKIPPED` lines, taken after the hand-back |
| The full suite, the repository-wide lint and the typecheck at HEAD. Phase 1 ran the one test file it changes, on macOS alone | the orchestrator, at the broad gate |

## Not done

`tests/github/test_finding_counts.py:255` makes a link with a bare `Path.symlink_to` and no skip, so on a Windows machine without the privilege that case fails where `symlink_or_skip` would skip it. It is the other direction of the defect the helper's docstring names, and the census in `trail/phases/phase-1.md` found it. It is left as it stands because the spawn scoped this work item to the three cases and `agents/crafter.md` *Never* bars building beyond the request. The `windows-latest` runner holds the privilege, so CI does not see it fail.

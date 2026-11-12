# Closing memo: 1794465691-the-orchestrator-polls-ci-by-hand

## Not verified

| Item | Who must answer |
|---|---|
| The whole suite, the repository-wide lint and the format check over the branch at its last commit: no phase runs them | the orchestrator, through `seal gate` |
| `tests/skills/test_pr_wait.py` on Linux, on Windows, and under Python 3.12 and 3.14. On Windows its `gh` stub is a `gh.cmd`, which the command finds through `shutil.which`. Phase 1 ran the cases on macOS under Python 3.13 alone | the pull request's `tests` workflow, whose matrix runs each of them |

## Not done

nothing

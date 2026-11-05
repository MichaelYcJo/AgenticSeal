# Closing memo: 1793843890-the-directory-tracks-a-dist-branch

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the branch's HEAD; phase 1 ran 16 modules in one command, and every other module of the suite is unrun | the orchestrator's broad run |
| `noninferiority.py#extract` on Windows, where `checkout-index --prefix` is handed a drive path with backslashes; phase 1 ran it on macOS alone | the Windows legs of the `tests` workflow on the pull request |
| The `release-report` job's worktree line on a GitHub runner; phase 1 ran the step's line in a scratch clone, not in the job | the `release-report` job on the release pull request into `main` |

## Not done

nothing

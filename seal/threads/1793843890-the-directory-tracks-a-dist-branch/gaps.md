# Closing memo: 1793843890-the-directory-tracks-a-dist-branch

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the branch's HEAD; phase 1 ran 16 modules in one command, phase 2 ran 50 and phase 3 ran 107, and every other module of the suite is unrun | the orchestrator's broad run |
| The census's archive reading on Windows, where `rev-parse --git-path index` and the copy of the index meet drive paths; phase 2 ran it on macOS alone | the Windows legs of the `tests` workflow on the pull request |
| `noninferiority.py#extract` on Windows, where `checkout-index --prefix` is handed a drive path with backslashes; phase 1 ran it on macOS alone | the Windows legs of the `tests` workflow on the pull request |
| The `release-report` job's worktree line on a GitHub runner; phase 1 ran the step's line in a scratch clone, not in the job | the `release-report` job on the release pull request into `main` |
| The `dist` job on a GitHub runner: the push that creates `dist` under the workflow's token, the bot identity in the job's environment, and the checkout holding the tag `publish` created; phase 3 ran `dist_branch.py` against bare repositories under the scratch directory, not in the job | the publish workflow's `dist` job at the v0.32.3 release's merge into `main` |
| `tests/github/test_dist_branch.py` and the two new cases of `tests/github/test_plugin_directory_check.py` on Windows, where the bare remote's path is a drive path; phase 3 ran them on macOS alone | the Windows legs of the `tests` workflow on the pull request |
| `plugin_directory_check.py` against a real `origin/dist`, which exists only after the first release builds it | the person who ticks `docs/releasing/release-checklist.md` *6. After the merge*'s box for the marketplace files after v0.32.3 |
| Whether the portal's form answers for `MichaelYcJo/AgenticSeal@dist`, and a session started from a plugin installed from `@dist`; phase 3's smoke run ran the archive's hooks and commands by hand from a scratch directory | the owner, after the release, as `frame/plan.md` *Operational impact* lists |

## Not done

nothing. The `LISTS_A_FIXTURE` row that phase 2 left here went in during phase 3, at `3996d0e5`.

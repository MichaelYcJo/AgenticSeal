# Closing memo: 1793843890-the-directory-tracks-a-dist-branch

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the branch's HEAD; phase 1 ran 16 modules in one command and phase 2 ran 50, and every other module of the suite is unrun | the orchestrator's broad run |
| `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`, whose two cases fail at `1884ce52` and at `c4ffaa78` on phase 1's case `tests/evals/test_noninferiority.py#test_leaves_the_repository_s_own_index_as_it_was`, a scope that runs `git diff --cached --name-only` with no row in that module's tables | the orchestrator, who decides which spawn classifies the scope |
| The census's archive reading on Windows, where `rev-parse --git-path index` and the copy of the index meet drive paths; phase 2 ran it on macOS alone | the Windows legs of the `tests` workflow on the pull request |
| `noninferiority.py#extract` on Windows, where `checkout-index --prefix` is handed a drive path with backslashes; phase 1 ran it on macOS alone | the Windows legs of the `tests` workflow on the pull request |
| The `release-report` job's worktree line on a GitHub runner; phase 1 ran the step's line in a scratch clone, not in the job | the `release-report` job on the release pull request into `main` |

## Not done

nothing

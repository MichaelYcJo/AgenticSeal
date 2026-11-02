# Closing memo: 1793599987-a-script-reads-git-the-same-under-any-config

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the work item's head | the orchestrator, by `seal gate --base release/v0.28.1 --record 1793599987-a-script-reads-git-the-same-under-any-config` once the review rounds settle |
| `tests/hooks/test_gitcmd.py` and the readers built by `gitcmd.argv` on the Windows and Linux legs of `.github/workflows/test.yml`; phase 1 ran on macOS with git 2.50.1 alone (`frame/questions.md` Q1) | the orchestrator, reading the legs of the pull request's test run |
| That each `git log` and `git status` a script under `hooks/`, `skills/` or `.github/scripts/` starts is built by `gitcmd.argv`. No case pins a call site: `settle.py#adding_commit` put back to a hand-written argv survived its cases (`trail/phases/phase-1.md`) | the proofer at review, by the rule in `frame/design.md` *Rule changes* |

## Not done

nothing

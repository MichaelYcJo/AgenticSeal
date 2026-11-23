# Closing memo: 1795397629-git-runs-through-thirty-hand-written-helpers

## Not verified

| Item | Who must answer |
|---|---|
| Phase 1's cases on the Windows leg: `Test_git::test_refuses_a_git_that_is_not_on_path_as_no_answer` and `Test_Failed::test_accepts_an_uncaught_one_as_its_line_at_exit_1` set PATH to one empty directory, and `Test_gh` finds the suite's stub `gh.cmd` through `shutil.which`. Each ran on macOS alone | the pull request's CI run on its Windows leg |
| `frame/questions.md` Q1: whether a git or `gh` command the suite's cases start comes near `lib/gitcmd.py#TIMEOUT` on a CI leg | the pull request's CI run and the orchestrator's broad run |

## Not done

nothing

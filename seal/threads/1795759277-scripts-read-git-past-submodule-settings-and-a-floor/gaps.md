# Closing memo: 1795759277-scripts-read-git-past-submodule-settings-and-a-floor

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate, the full suite, the repository-wide lint and format check, over the work item's tree | the orchestrator, at the broad gate once the review rounds settle |
| Whether git 2.30 reads each command the scripts under `lib/`, `skills/` and `hooks/` start as git 2.50.1 and 2.39.3 read it, `frame/questions.md` Q1. The cases of `tests/lib/test_gitcmd.py` and `tests/skills/test_range_read.py` ran under 2.50.1 and 2.39.3 alone, the gits this machine holds, and the framer's build of 2.30 was refused by the environment | a measurement: one run of those modules on a machine or in a container whose `git --version` prints 2.30, which the repository owner arranges |
| The `FLAGGED` cases of `tests/lib/test_gitcmd.py` under the git of the Linux and Windows runners, where `--ignore-submodules=none` on `log` and `diff-tree` and a `.gitmodules` entry's `ignore` were not run, and `Test_older::test_accepts_the_line_the_git_running_the_suite_prints` there, where the first line a Windows git prints was read only as a case supplies it | CI's Linux and Windows legs, which `CONTRIBUTING.md` *Opening a pull request* says run the suite at every push to an open pull request into the release branch |

## Not done

nothing

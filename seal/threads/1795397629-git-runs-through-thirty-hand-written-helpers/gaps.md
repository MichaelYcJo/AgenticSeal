# Closing memo: 1795397629-git-runs-through-thirty-hand-written-helpers

## Not verified

| Item | Who must answer |
|---|---|
| Phase 1's cases on the Windows leg: `Test_git::test_refuses_a_git_that_is_not_on_path_as_no_answer` and `Test_Failed::test_accepts_an_uncaught_one_as_its_line_at_exit_1` set PATH to one empty directory, and `Test_gh` finds the suite's stub `gh.cmd` through `shutil.which`. Each ran on macOS alone | the pull request's CI run on its Windows leg |
| `frame/questions.md` Q1: whether a git or `gh` command the suite's cases start comes near `lib/gitcmd.py#TIMEOUT` on a CI leg | the pull request's CI run and the orchestrator's broad run |
| Phase 2's cases on the Windows leg: the S1 to S5 cases of `tests/skills/test_seal.py` move a root, write the `Mode` key and run `git rm` and `git add` for real around the one call they make time out. Each ran on macOS alone | the pull request's CI run on its Windows leg |
| Phase 3's cases on the Windows leg: the S7 cases of `tests/skills/test_settle.py` run `seal settle` over a fixture repository with git and the `gh` stub `gh.cmd` for real around the one call they make time out. Each ran on macOS alone, and `test_a_named_directory_is_read_as_its_name_and_never_as_a_pattern` is skipped there, since `*` is no character of a Windows name | the pull request's CI run on its Windows leg |

## Not done

**`seal mode` still exits 0 where the `Mode` key was not written.** Taken apart into its steps, `seal.py#switch` moves the root, writes the key, asks `tracked`, and runs `git rm -r --cached` or `git add`. Phase 2 makes the last three exit 1 where they did not happen, as design *Scope* item 4 asks for the stage steps. The rename already returns 1. Where `write_mode` refuses, the switch prints `` the `Mode` key was NOT written: `` and goes on to stage, print `Now commit.` and exit 0, which is the reading `plan.md` A10 rejects for a stage step. It was left because the design scopes the exit code to the stage step, and the key is not a git command. The orchestrator kept it out of this work item, in `frame/plan.md` *Judgments of the run*, and it stands here for the release's reader.

**No case holds the `--literal-pathspecs` that `settle.py#git_run` passes.** Phase 3 moved the call onto `lib/gitcmd.py#git` with the flag kept, and a mutant that takes the flag out survived `tests/skills/test_settle.py` and `tests/skills/test_rule_changes.py`. It survived at `d0b15b72f` too, so no case held the flag before this work. The flag in `git_fields`, the other reader that carries it, now has its case. A case for `git_run` needs a work item id or a path that git reads as a pattern, in a fixture whose answer the flag changes, and it was left because no reading this work changes depends on it. Whether it is worth a case is the orchestrator's call, and otherwise a row for `seal/follow-up.md`.

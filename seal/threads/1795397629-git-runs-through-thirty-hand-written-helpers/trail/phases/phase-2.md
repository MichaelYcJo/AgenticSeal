# Phase 2: 1795397629-git-runs-through-thirty-hand-written-helpers

## What this phase found

**The frame held for phase 2, with three departures.** Each claim below was judged against `frame/design.md` and `frame/plan.md` as committed at `e9e86edcd`, and against the tree at `672c8cf8c`, where phase 1 closed. `skills/implement/scripts/seal.py` did not change between `d0b15b72f` and `672c8cf8c` (executed: `git diff --stat d0b15b72f 672c8cf8c` names no file under `skills/`), so the frame's coordinates in it held as written.

- Executed: `git grep -nE "subprocess\.(run|Popen|call|check_call|check_output)\(" d0b15b72f -- skills/implement/scripts/seal.py` prints 12 lines, the 11 calls *Scope* item 4 lists and `hand_over`'s `subprocess.call`. The same search over the tree at `3c046b039` prints `seal.py:2508`, `hand_over`'s line, alone.
- Read: `seal.py` loads `lib/gitcmd.py` at import at `d0b15b72f` (`seal.py:194`), so the class phase 1 found, a case that copies a script without `lib/gitcmd.py`, has no instance in this phase. The method was `git grep` over `tests/` for `seal.py` beside `copy`, `copied` and `tmp`, which printed no copy of `seal.py`. That list is a sample, for the reason phase 1 gives.

**The departures.**

- **Design S6 says the cases at `tests/skills/test_seal.py:910`, `:1385` and `:1679` stay unchanged in what they assert. One assertion of `:910` changed.** At `d0b15b72f` it pins `the remote was left out — git config could not be run (`. `git_asked` now gives the runner's line as `why`, so the case pins `` the remote was left out — `git config --get remote.origin.url` did not finish within 60 seconds ``. The behaviour S6 states holds: the zip is written, the remote is left out with its line, and the export exits 0. The grounds are `skills/core/SKILL.md` *The rule a mechanism is kept against*, **a fact has one source**, and design `## Rule changes`, which makes `Unrun`'s one line the statement of a command that did not answer. Wrapping that line in `git config could not be run (…)` would state the failure twice, as `` git config could not be run (`git config --get remote.origin.url` could not be run: … `` shows. `porcelain` and `gitlinks_under_root` give the runner's line the same way, so five other pins in the file moved with them: `Test_git_asked::test_refuses_a_git_that_did_not_answer`'s `no git` and `a timeout` rows, `Test_porcelain`, `Test_gitlinks_under_root` and the `a git that cannot answer` row of `Test_refusals`. Rule 14 of the agent contract asks for those pins in the same commit, `3c046b039`.
- **A second case pinned exit 0 for a stage step git refused, and design `## Removes` names only the first.** `Test_mode::test_s6_a_switch_that_could_not_stage_names_agentic_seal_in_the_command` asserts `code == 0` at `d0b15b72f` (`tests/skills/test_seal.py:3078`), for a held `index.lock` going local and an ignore rule going shared. It now asserts `code == 1` and that no `Now commit.` line is printed, as S3 asks of the case at `:2887`. The method was a read of every case in the file that runs `seal mode` over a stage step that fails, which the `could NOT be staged` and `still tracked` search found: those two cases.
- **`pr_checks` asks `optin.toplevel` too.** Design *Scope* item 4 names `resolve` alone and says that through it `seal export` and every other subcommand tell a git that did not answer from no repository. `seal pr-checks` asks for the repository itself, not through `resolve` (`seal.py:2024` at `d0b15b72f`), so the sentence would hold only for the subcommands that call `resolve`. `pr_checks` now asks `optin.toplevel`, and the S5 case runs `pr-checks` beside `export`, `export --check`, `import` and `mode --check`.

**Decisions settled while writing the code.**

- **What each reader gives for `Failed`.** `git_asked` gives `(None, exc.line)`, `porcelain` gives `[exc.line]`, `staged_text` gives `None`, as design *Data & interfaces* lists them. `tracked` catches nothing, so `Failed` reaches its caller. In `switch` that is the stage step that did not happen: the line reads `the records are still tracked:` with the runner's line, as for `git rm`, because whether anything is still tracked is the question git did not answer. In `remove_workflow` an uncaught `Failed` from `tracked` ends `seal pr-checks remove` with its line at exit 1 and nothing removed, which is the last row of design *Data & interfaces*.
- **`seal mode` exits 1 after the stage step's line, and the workflow notes still print.** The notes after the step, `left_workflow_line` going local and the missing checks going shared, say what is true of `.github/` whichever way the step went, so the switch prints them and then returns 1 before `Now commit.`. Judged against design S1 to S3 and `plan.md` A10.
- **A non-zero exit with nothing on stderr still reads as the step's failure.** At `d0b15b72f` each stage step reads `returncode != 0` and prints `(done.stderr or '').strip()`, which may be empty. The new code holds the reason as `None` for a step that happened and as a string otherwise, so an empty stderr is still a failure. A mutant reading `if why:` survived the first run, and the case `install's git add refused with nothing on stderr` was added for it.
- **The module docstring's exit codes name the two new causes of exit 1**: a switch whose stage step git did not take, and a git command that did not answer, as rule 14 of the agent contract asks of a change to what a person sees.
- **`frame/questions.md` Q2, answered by the work for phase 2.** `seal.py` keeps `import subprocess` for `hand_over`'s `subprocess.call` on Windows. So `tests/skills/test_seal.py#unanswered`, which patches `SEAL.subprocess.run`, is left as it is: the attribute is the one `subprocess` module object `lib/gitcmd.py#_start` calls. `TIMED_OUT` stays `subprocess.TimeoutExpired(["git"], 15)`, since the runner writes its own line with `TIMEOUT` whatever the exception carries. No case asserts a moved call's argv.
- **The comments that stood on the old reading were rewritten in place**: `git_asked`'s note on the encoding, which now stands in `lib/gitcmd.py#_start`; the `--check` branch of `seal.py#mode`, as design `## Removes` asks; `remote_url`'s `optin.repo_root(cwd)`; and the comment above `WORKFLOW` that cites `lib/optin.py`'s reasoning about `repo_root`, which phase 1 moved to `toplevel`.

**Seen red and mutation claims.** Executed. Each new case, and each pin that moved, was run against `seal.py` as it stood at `672c8cf8c`, the same bytes as `d0b15b72f`, with the new tests in place (`git stash push -- skills/implement/scripts/seal.py`). Every one failed:

| Case | Red against the old `seal.py` |
|---|---|
| `Test_switch::test_refuses_to_call_a_stage_git_that_did_not_answer_staged`, `git rm going local` and `git add going shared` (S1, S2) | `subprocess.TimeoutExpired` raised out of `seal mode` |
| the same case, `git ls-files going local` | `assert 0 == 1`: `tracked` read the timeout as nothing tracked and the switch printed `Now commit.` |
| `Test_switch::test_refuses_to_call_a_stage_git_turned_down_staged` (S3) and both rows of `Test_mode::test_s6_a_switch_that_could_not_stage_names_agentic_seal_in_the_command` | `assert 0 == 1` |
| `Test_pr_checks::test_refuses_a_git_that_did_not_answer_and_keeps_the_index`, `install's git add`, `remove's git diff --cached`, `remove's git rm` (S4) | `subprocess.TimeoutExpired` raised out of `seal pr-checks` |
| `Test_main::test_refuses_a_git_that_did_not_answer_for_the_repository_as_no_repository`, all five subcommands (S5) | `DID NOT RAISE Unrun`, with `not inside a git repository` or, for `mode --check`, `no git repository could be resolved here` printed |
| `Test_tracked::test_refuses_a_git_that_did_not_answer_as_nothing_tracked` | `DID NOT RAISE Unrun` |
| the six moved pins named under the first departure | the old spelling `… could not be run (…)` |

The three S4 rows added after the first mutation run pass against the old `seal.py`, since each holds a reading `d0b15b72f` already had. Each was shown red with its guard removed instead, in the second run below.

`bin/seal mutate skills/implement/scripts/seal.py` at `3c046b039`, one call of 15 mutants, with the tests command `bin/test tests/skills/test_seal.py -q -p no:xdist -x -k '<the classes of the units>'`: 12 red and 3 `SURVIVED`. A batched call names no failing case. Each mutant turned one `except gitcmd.Failed` into `except ZeroDivisionError`, or broke one reading:

| Unit | Mutant | Verdict |
|---|---|---|
| `git_asked` | the handler | red |
| `porcelain` | the handler | red |
| `staged_text` | the handler | SURVIVED, then red |
| `install_workflow`, `git add` | the handler | red |
| `install_workflow` | `if why is not None:` to `if why:` | SURVIVED, then red |
| `remove_workflow`, `git diff --cached` | the handler | red |
| `remove_workflow`, `git rm` of a copy deleted by hand | the handler | SURVIVED, then red |
| `remove_workflow`, the other `git rm` | the handler | red |
| `switch`, going local | the handler around `tracked` and `git rm` | red |
| `switch`, going shared | the handler around `git add` | red |
| `switch` | `if why is not None: return 1` to `if False:` | red |
| `switch`, going local | the `git rm` exit read, `if done.returncode != 0:` to `if False:` | red |
| `switch`, going shared | the `git add` exit read, the same | red |
| `resolve` | `optin.toplevel(cwd)` to `optin.repo_root(cwd)` | red |
| `pr_checks` | the same | red |

The three survivors got the S4 rows `install's git add refused with nothing on stderr`, `remove's git cat-file of a copy deleted by hand` and `remove's git rm of a copy deleted by hand`, committed at `8065f6a74`. A second call at `8065f6a74` over those three mutants, with `-k keeps_the_index`, read `red` for each. `tracked` has no mutant: the phase removed its handler, and the old code is the mutant, seen red above.

**The phase boundary run.** Executed: one `bin/test -q` at `8065f6a74` over the plan row's file `tests/skills/test_seal.py`; `tests/text` and `tests/behaviour`, which `CONTRIBUTING.md` names as the tree-wide files; `tests/test_censuses.py`; the test files that name `skills/implement/scripts/seal.py` (`tests/e2e/teammate/test_teammate_flow.py`, `tests/lib/test_config.py`, and those under `tests/behaviour/` and `tests/text/`); and the test files that run `bin/seal`, which loads `seal.py` (`tests/skills/test_deferral_check.py`, `test_mutation_check.py`, `test_pact_check.py`, `test_payload_meter.py`, `test_seal_stamp.py`, `test_settle.py` and `test_unverified_check.py`). It gave `2467 passed, 9 skipped`. `b002e5e3c` after it changes one docstring of `tests/skills/test_seal.py`, and the S4 case ran green there.

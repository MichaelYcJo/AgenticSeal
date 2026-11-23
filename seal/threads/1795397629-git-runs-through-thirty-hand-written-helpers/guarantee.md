# Guarantee: 1795397629-git-runs-through-thirty-hand-written-helpers

The audit read the tree at `1df71771e` against `c3f568c6a`, the commit `origin/release/v0.38.6` names. The local `release/v0.38.6` answers `641b6bfb5` and is stale, so the upstream was used, as `broad_gate.py#resolve_base` takes it. The broad run's record names `972c21ad6`. Only `trail/gate.md` follows it, at `1df71771e`. `seal pr-body --check` exited 0 on the body file, with both the installed plugin's `seal` and the tree's `bin/seal`. The seen-red claims were re-run in a clone at `<scratchpad>/1795397629-git-runs-through-thirty-hand-written-helpers/at-base/`. There, the code was restored from `c3f568c6a` and the cases were kept at HEAD. The tree under audit was not changed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run is at HEAD, or only the work item's records follow it | `trail/gate.md`, its `run:` line | `git log --no-merges --name-only 972c21ad6..HEAD ^c3f568c6a`; `git merge-base --is-ancestor 972c21ad6 HEAD` | holds, executed: one commit follows, `1df71771e`, and it touches `trail/gate.md` alone. The gate's commit is an ancestor of HEAD. The log the prompt names reads `BROAD GATE PASSED … @ 972c21ad6 against origin/release/v0.38.6 @ c3f568c6a`, with 5752 passed, 9 skipped and chain exit 0 (read) |
| The base is merged into the branch | prompt; `trail/phases/phase-5.md` (merge `e1060dee8`) | `git merge-base --is-ancestor c3f568c6a HEAD` | holds, executed: exit 0 |
| The body is `pr.md` above the heading and the records' text below it | the body file the prompt names | `seal pr-body <item> --body <file> --check`, with the installed `seal` and with `bin/seal` | holds, executed: exit 0 both times, `matches: …` |
| S1, S2: a `git rm` or `git add` past the bound in `seal mode` exits 1, prints no `Now commit.`, and shows no traceback, seen red against the old `seal.py` | `trail/phases/phase-2.md:29-30` | `bin/test -q -p no:xdist tests/skills/test_seal.py::Test_switch::test_refuses_to_call_a_stage_git_that_did_not_answer_staged`, at HEAD and then with `seal.py` from `c3f568c6a` | holds, executed: 3 passed at HEAD. Against the base, the `git rm` and `git add` rows fail on `subprocess.TimeoutExpired`, and the `git ls-files` row fails on `assert 0 == 1` |
| S3: a stage step git refused now exits 1 | `trail/phases/phase-2.md:31`; `changelog.md` *Removed* | `…::Test_switch::test_refuses_to_call_a_stage_git_turned_down_staged`, at HEAD and against the base | holds, executed: passes at HEAD and fails on `assert 0 == 1` against the base. Read: `tests/skills/test_seal.py`'s `test_s6_a_switch_that_could_not_stage_names_agentic_seal_in_the_command` asserts `code == 1` and no `Now commit.` |
| S5: `seal export`, `export --check`, `import`, `mode --check` and `pr-checks` raise the runner's line where `rev-parse --show-toplevel` did not answer | `trail/phases/phase-2.md:33` | `…::Test_main::test_refuses_a_git_that_did_not_answer_for_the_repository_as_no_repository`, at HEAD and against the base | holds, executed: 5 passed at HEAD. All 5 rows fail on `DID NOT RAISE Unrun` against the base |
| S7: a git or `gh` past the bound in `seal settle` is one line at exit 2 | `trail/phases/phase-3.md:34-37` | `tests/skills/test_settle.py::Test_main::test_refuses_a_git_that_did_not_answer_in_one_line` and `::test_refuses_a_git_or_gh_that_did_not_answer_in_local_mode`, with `settle.py` and `rule_changes.py` from the base | holds, executed: 12 passed at HEAD. Against the base, 11 rows fail on `subprocess.TimeoutExpired`, and the `gh` row fails on the old line `` `gh pr list --head feat/1-a` did not run (…) `` |
| S8: a git past the bound in `chain-check` is one line at exit 2, the fix pass's `rule_changes_read` row among the rows | `trail/phases/phase-4.md:33-34`; `trail/rounds/round-1.md` finding 1's close | `tests/skills/test_chain_check.py::Test_main::test_refuses_a_git_that_did_not_answer_in_one_line`, with `chain_check.py` from the base | holds, executed: 10 passed at HEAD. Against the base, the `toplevel` row fails on `chain-check: … is not in a git repository`, and the other nine rows fail on `subprocess.TimeoutExpired`. The re-raise guard alone was shown red by round 2 with `seal mutate`. This audit read that probe and did not run it again |
| `seal stamp --guarantee` refuses at exit 2 where git did not answer | `trail/phases/phase-5.md:13`, `:36` | `tests/skills/test_seal_stamp.py::Test_main::test_guarantee_refuses_a_git_that_did_not_answer_naming_it`, with `seal_stamp.py` from the base | holds, executed: 3 passed at HEAD. All 3 rows fail against the base on the old `seal stamp: <path>: Command '[…]' timed out after 60 seconds` line |
| A push past the bound in `dist_branch.py` ends in the runner's line | `trail/phases/phase-6.md:44` | `tests/github/test_dist_branch.py::Test_main::test_refuses_a_push_that_gave_no_answer_in_the_runners_line`, with `dist_branch.py` from the base | holds, executed: passes at HEAD and fails on `subprocess.TimeoutExpired` from `git push` against the base |
| An uncaught `Failed` ends a process with its line at exit 1 and is no `Exception`. This case asserts something is not let through, so it was shown red with its guard alone removed | `trail/phases/phase-1.md:31` | `tests/lib/test_gitcmd.py::Test_Failed` at HEAD, then with `class Failed(SystemExit):` edited to `class Failed(Exception):` in the clone | holds, executed: 2 passed at HEAD. With the guard removed, both fail on the guard's own line. One case fails with `returncode=0, stdout='caught as an Exception…'` and the other on `assert not True` |
| `TIMEOUT` bounds a real hanging git, and not only a double raising `TimeoutExpired` | `changelog.md` *Fixed*, the first bullet; round 1 *Not judged*, the Windows row | probe `<scratchpad>/…/sealer/test_tmp_real_hang.py` under `/usr/bin/python3` 3.9. A `git` on PATH runs `sleep 20`, and `gitcmd.TIMEOUT` is set to 2 | holds on macOS, executed: `Unrun after 2.0s: `git status` did not finish within 2 seconds`. The probe did not run on Windows |
| The moved units keep their readings: `branch_name` moved to `routing.current_branch`, `unverified_check.py#repo_root` moved to `optin.repo_root`, and `write_output` moved to `lib/console.py` | `trail/phases/phase-5.md:24-25`; `trail/phases/phase-6.md:83` | `bin/test -q tests/skills/test_broad_gate.py::Test_gate tests/skills/test_unverified_check.py tests/lib/test_console.py tests/lib/test_routing.py::Test_current_branch` at HEAD | holds, executed: 87 passed |
| S10: no script starts git or `gh` outside the runner | `frame/design.md` S10; `trail/phases/phase-5.md:8` | `git grep -nE "subprocess\.(run\|Popen\|call\|check_call\|check_output)\(" HEAD -- skills lib .github/scripts evals/scripts ':!lib/gitcmd.py'`; `git grep -n "=subprocess.run" HEAD -- …`; `git grep -nE "os\.system\|os\.popen\|os\.exec\|os\.spawn\|create_subprocess\|getoutput" HEAD -- … hooks bin` | holds, executed: the first search prints `noninferiority.py:401` (`claude`), `seal.py:2508` (`hand_over`), `broad_gate.py:681` and `:699` (comments), `:943` (`run`), `:2243` (the shipped gate), `mutation_check.py:405` and `test_layout.py:1042` (pytest). Each was read, and none starts git or `gh`. The second search prints nothing. The third prints `seal.py:2511`, `hand_over`'s `os.execv` |
| S11 and S12: one copy of each helper, and `tag_release.py` loads no other script | `frame/design.md` S11, S12 | the three S11 searches and the S12 search at HEAD | holds, executed: nothing; nothing; `plugin_directory_check.py:191` alone; nothing |
| Every `## Removes` row of `frame/design.md` and every removal the changelog names is gone from the tree | `frame/design.md:157-171`; `changelog.md` *Removed* | `git grep` at HEAD for `TimeoutExpired\|SubprocessError`, `timeout=`, `is-ancestor`, `def run(`, `write_output`, `diff-tree` in `chain_check.py`, `ls-files` in `settle/scripts`, `^GH\s*=`, `class Test_repo_root\|class Test_run\b` in the two named test files; reads of `seal.py#gitlinks_under_root`, `plugin_directory_check.py#is_ancestor`, `rule_changes.py#_ancestor` and `seal_stamp.py:1348` | holds, executed. The handlers are only `lib/gitcmd.py:164`, `:168` and `mutation_check.py:422` (the tests command). The only `timeout=` arguments left are `lib/gitcmd.py:159`, `mutation_check.py` and a urllib call. `is-ancestor` is spelled in `lib/gitcmd.py` alone. The only `run` left is the closer's, which design G19 keeps. `write_output` is defined in `lib/console.py` alone. `diff-tree` stands only in `touched` (`chain_check.py:971`). `ls-files` reads go through `git_fields`. `GH` is gone. Both test classes are gone. `gitlinks_under_root` asks `git_asked`, and the other three ask `gitcmd.is_ancestor` |
| Round 2's finding was fixed in the records alone, as it asked | `trail/rounds/round-2.md:31` (`fixed 5fa72e29b`) | `git show --stat 5fa72e29b`; read `gaps.md:14` | holds, executed and read: the commit touches `gaps.md` alone (+1 line). The row stands after the phase 5 row, word for word as the round gave it. The round 1 fixes in the records alone, `e2379886f`, touch `frame/design.md`, `frame/plan.md`, `frame/questions.md` and `pr.md`, and round 2 confirmed them (`confirms: round-1#3`, `#4`) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `frame/design.md` *Scope* items 1 to 9 put every git and `gh` start of the four roots behind `lib/gitcmd.py#git` and `#gh` under one 60 s bound. `Failed` is a `SystemExit`. Readers with a documented default keep it, and six `main`s refuse at 2. `## Removes` lists 13 rows | the tree (S10 to S12 and every Removes row, re-run above); the issue's *Direction* and both *Done when* items | none. The departures each phase records were folded back into it at `87c10c522` and `e2379886f`, and the rows round 1 found stale now match the tree (`seal_stamp.py#main` under `--guarantee`, `test_layout.py`'s `_git` gone) |
| the build | the diff of 68 files and six phase records. Each of the six Status cells in `frame/plan.md` names a commit, and `trail/phases/phase-1.md` to `phase-6.md` all stand (`routing.md`: Implementation `crafter`) | the design; the seen-red claims sampled above, each red where its record says | none found in the sample |
| the last round | `trail/rounds/round-2.md` confirms round 1's four closes. It finds one gap in `gaps.md`, which was fixed at `5fa72e29b` in the records alone | the tree at `5fa72e29b`, read above; round 1's closes | none |
| the changelog | `changelog.md` *Fixed*, *Changed*, *Removed*: one runner and one bound, `seal mode` exit 1, `seal export`'s line, five commands and `seal stamp --guarantee` refuse at 2, and the removals listed | the tree; the design's *Data & interfaces* | none that the tree contradicts in what it changes. Its sentence that `chain-check` refuses at exit 2 "where git gave no answer" does not cover one read. `declared_for_this_branch` (`chain_check.py:1901`) asks `lib/routing.py#current_branch`, which reads a git that did not answer as `""`, as design *Scope* item 2 chooses and as it read before this work under a 5 s bound. The declaration is still judged through `changed_routing`, so the check does not pass on nothing. Round 1 *Not judged* hands this to the orchestrator, and no record answers it |
| the orchestrator's part of the pull request body | `pr.md` quotes two rows of `frame/plan.md` *Judgments of the run* and closes #1573 | `frame/plan.md:71` and `:72`, quoted word for word; the issue's `fix:` title | none |
| the orchestrator's routing grounds | `routing.md` *Why this way*, under `agentic`: a work item through the review chain that replaces the runners of about twenty scripts | the diff, which changes those scripts, their cases, `lib/` and one workflow comment named by design *Scope* item 3, and no hook | none |

## Outside this guarantee

These are open, each with its answerer named. None is a claim of a party that the tree contradicts.

- `gaps.md` *Not verified*: the Windows leg of every phase's new cases, and `frame/questions.md` Q1. Answered by the pull request's CI run.
- Round 1 *Not judged* names four questions for the orchestrator, and no record answers them:
  - whether the hooks may now wait 60 s on git where they waited 5 s;
  - whether the release workflow's network commands finish within `TIMEOUT`;
  - whether the bound holds on a real hang on Windows, which a measurement on a Windows machine answers. The probe above shows the bound on macOS only;
  - the `chain-check` branch read named in the changelog row above.

  `seal pr-body` does not copy *Not judged* into the body, so a reader of the pull request does not see them.

```seal
target: 1df71771e81c5b7369b5dfa07593dd14c3fac7b6 against c3f568c6a742b75f8733e912a618d28ee16191eb
Verdict: sealed
```

## Re-audit at 32c3b6cdc

The block above audited `1df71771e`. Two commits follow it. `122ea4685` commits this file, and `32c3b6cdc` commits `trail/rounds/round-3.md`. Neither touches a coordinate a claim above rests on, so no claim was re-run, and the parties were read again.

That audit missed one thing. Round 2's finding names two test files in its `location:` beside `gaps.md`. So its close, `fixed 5fa72e29b`, did not meet the condition for the sealer to read it alone, and it was owed a verifying round. The block above read it as records-only. Round 3 is that round.

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run is at HEAD, or only the work item's records follow it | `trail/gate.md`, its `run:` line | `git log --no-merges --name-only 972c21ad6..HEAD ^c3f568c6a`; `git merge-base --is-ancestor 972c21ad6 HEAD` | holds, executed: `1df71771e`, `122ea4685` and `32c3b6cdc` follow it. They touch `trail/gate.md`, `guarantee.md` and `trail/rounds/round-3.md` alone, and the gate's commit is an ancestor of HEAD |
| The base still resolves to the same commit | prompt | `git rev-parse 'release/v0.38.6@{upstream}'` | holds, executed: `c3f568c6a742b75f8733e912a618d28ee16191eb` |
| The body composed at HEAD is `pr.md` and the records' text | the body file the prompt names | `seal pr-body <item> --body <file> --check` | holds, executed: exit 0, `matches: …` |
| The guarantee committed at `122ea4685` is the file this audit wrote | `122ea4685` | `git show 122ea4685:<item>/guarantee.md \| diff - <item>/guarantee.md`, before this section was added | holds, executed: no difference |
| `chain-check` at HEAD names only that the guarantee is behind HEAD | the prompt | `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.38.6` | holds, executed: exit 1. Its one problem is `the guarantee is behind HEAD: commit 32c3b6cd after it touches …/trail/rounds/round-3.md`. Its other line says the body is not read without an event payload |

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the last round | `trail/rounds/round-3.md` reads `122ea4685` as a verifying round over `64a28d00f..122ea4685`, finds nothing, and confirms `round-2#1` | the tree: `5fa72e29b` touches `gaps.md` alone, and `gaps.md:14` is round 2's row word for word, read again here | none |
| the design, the build, the changelog, the orchestrator's part of the pull request body, the routing grounds | as in *The parties* above | as above | none. No commit since `1df71771e` touches them |

What stands outside this guarantee is the list in *Outside this guarantee* above, unchanged. Round 3's *Not judged* adds no item for a person.

```seal
target: 32c3b6cdcbfec66b8b7cc66e23ddc914ad1007f8 against c3f568c6a742b75f8733e912a618d28ee16191eb
Verdict: sealed
```

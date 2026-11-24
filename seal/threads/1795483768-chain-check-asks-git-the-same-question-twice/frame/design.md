# Design: 1795483768-chain-check-asks-git-the-same-question-twice (#1603)

## Grounding

The tree as read at `136cfca25`, whose code is that of `fe09bef46`, the v0.38.6 merge (the one commit between them adds `routing.md`).

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/core/SKILL.md` *The rule a mechanism is kept against*, the sentence "A script holds a gate only on a fact it reads exactly" | An answer given a second time is the answer git gave the first time, to the same argv, and never one built from another command's output. A batch is read by the sizes `git cat-file --batch` prints, never by a marker a path could also hold. |
| G2. `skills/core/SKILL.md` *The first value: efficient development through the AgenticSeal process* | The work is judged by the processes and the Windows-leg seconds it saves against the code it adds. A read that would cost more code than the processes it saves stays its own process, and `frame/plan.md` *Alternatives considered* records why. |
| G3. `docs/running/what-a-script-gates.md` *Which gate a script holds*, as #1573's unsettled `## Rule changes` leaves it (`seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/frame/design.md`) | Every git command a script starts is started by `lib/gitcmd.py#git`, and a command that did not start or finish within `TIMEOUT` is no answer. The memo sits inside `git`, so the rule still holds, and it stores no `Unrun`. The paragraph names `lib/gitcmd.py`'s docstring as the home of the runner's details, so the memo's contract is written there and no rule changes. |
| G4. `docs/checks/the-pull-request-check.md` and `docs/running/what-a-script-gates.md` *The checks*, the `chain_check.py` and `seal settle` rows | What each command reads, refuses, names as not read and prints stays as written. This work changes how many processes a run starts, never what it reads. |
| G5. `CONTRIBUTING.md` *What a change to a gate must carry* | `chain_check.py` is a gate. Each new case is seen red first. The failure direction is neither more nor fewer refusals, since no verdict changes. The prompt budget is zero. The Windows leg is not run locally, and the pull request says so. |
| G6. `docs/releasing/branch-and-release.md` *Cutting a release*, the paragraph "The version moves at the start of a release" | This is the first pull request into `release/v0.38.7`. The crafter of the last phase moves `.claude-plugin/plugin.json` to `0.38.7` in the commit that adds `changelog.md`. |
| G7. `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/frame/design.md` S1 and *What a figure of the Windows leg can show, measured after the frame* | The Windows-leg seconds are read from `workflow_dispatch` runs of `tests`, each module against modules nothing changed in the same pair of runs. A local timing is no evidence of the leg. |

**What one `chain-check` run asks git today** (executed: `test_tmp_run.py` in the framer's scratch, over a `git clone --no-local` at `136cfca25`, counting each `subprocess.Popen` while `main` ran). Run over #1581's real branch, `perf/1581-six-test-modules-cost-past-the-60-s-rewrite-bound` at `af3a0ec43`, against its merge base `ef776317b`, with an event payload holding a body and `GITHUB_HEAD_REF` set, the run started 105 processes. 85 of them are distinct, so removing the repeats leaves 85, and 49 of those are `show HEAD:<dir>/routing.md`, one for each work-item directory HEAD carries, asked by `tracked_declarations` to find the declaration naming the branch. The same run with no payload, where the body arm reads nothing, started 100 processes. The orchestrator's two test cases, 41 and 34 processes with 31 and 20 distinct, show the same repeats (the orchestrator's measurement at `fe09bef46`, opened against this probe's readers and not re-run, because the framer runs no test module).

**Why each repeat is asked** (read, at `136cfca25`; executed for the call chains, which the probe prints). The arms of `skills/code-review/scripts/chain_check.py#_checked` each read the records they judge. The repeats come from that one design:

- `read_record` of `routing.md` in `tracked_declarations` (`:1869`) and in `_checked` (`:2231`).
- `read_record` of `frame/design.md` in `frame` (`:1051`) and in `rule_changes_read` (`:1343`).
- `rounds_listed`'s `ls-tree` and `read_record` of each round record in `records` (`:1456`) and in `unread` (`:541`), and again in `originals_of` (`:1596`) where a migration config is declared.
- `merge-base --is-ancestor` and `diff-tree` of a fixed commit in `verdict_problems` (`:1420`) for each finding that names the same commit, and `diff-tree` again in `records_only` (`:983`) through `channel`.
- `follows` (`:991`), asked of the last round's target by `records`, of the gate run's commit by `broad_gate` (`:1655`), of the guarantee's target by `guarantee` (`:1694`), and of the guarantee's target again by `skills/code-review/scripts/pr_body.py#_seal_at_head` (`:543`) through the body arm. Each `follows` asks `rev-parse`, `merge-base --is-ancestor`, `rev-list`, and a `diff-tree` for every later commit, and the later commits of the four asks overlap.
- `rev-parse --verify --quiet <base>^{commit}` in `resolves` (`:2031`) and in `_seal_at_head`.

**Which reads cannot change within one run** (read, at `136cfca25`; executed for the search). A run of `chain-check` writes nothing. `git grep -n -E '"(add|commit|update-index|write-tree|update-ref|checkout|switch|reset|rm|mv|stash|tag|config|worktree|fetch|push|merge|rebase|apply|am|notes|gc|-w)"' 136cfca25 -- skills/code-review/scripts/chain_check.py skills/code-review/scripts/pr_body.py lib/optin.py lib/routing.py lib/config.py lib/closing.py lib/gaps.py skills/settle/scripts/` prints no git subcommand, only strings of the records' own vocabulary, and `chain_check.py` opens no file for writing. Every subcommand the probe saw is a read: `rev-parse`, `diff`, `merge-base`, `show`, `ls-tree`, `log`, `diff-tree` and `rev-list`. Under `--worktree`, which the probe did not run, `changed` (`:371`) and `carried_by` (`:435`) also ask `diff --raw` against the merge base, `ls-files --others`, `hash-object` without `-w` and `status --porcelain` (read). Those reads depend on the working tree. Nothing in the run writes there, so within the run they answer the same as the others do. A process outside the run that writes the tree mid-run makes the run read a tree in motion whether or not answers are reused, and reusing them reads one state. The `gh pr view` of `pull_request_from_gh` is asked once and is not git.

**`settle` repeats reads within one run** (executed: the same probe, over the clone at `fe09bef46`, `--released-at v0.38.6`). The dry run started 100 processes, 95 distinct. `merge-base --is-ancestor` pairs repeat in `skills/settle/scripts/rule_changes.py#unordered` (`:761`), which `settle.py#timeline` asks once per group, so a pair of commits in two groups is asked twice. `ls-files -z` is asked by `tracked_names` (`:1044`) and by `tracked_text` (`:1683`). Under `--apply`, the three reads of `versions` (`:501`) are asked by `earlier_judgments` in `survey` and again by `notes` (`:670`), so the run started 123 processes, 115 distinct. `--draft` and `--all-earlier` show the dry run's repeats. The issue's other candidates, `ls-tree -r -z --name-only <ref>`, `show <ref>:<design>` and `log ... -- seal/threads`, are each asked once per run, so the twice the orchestrator counted in `test_settle.py` came from the cases' own setup or from two runs of `main`.

**`settle` writes after its last git read** (read). `apply` (`:1940`) asks `notes` before its first `shutil.rmtree`, as its docstring says: "Every directory is classified before the first removal". After the removals it calls `write_after`, which reads `fold_check.py`, and `closed_rows`, which reads `lib/gaps.py`. Neither starts git: `grep -c 'gitcmd\|subprocess'` gives 0 for `fold_check.py`, and `lib/gaps.py` imports only `under_root` from `gitcmd`. `draft` (`:1863`) writes the policy root after `survey` and reads the documents from disk. `apply`'s docstring takes its candidates from the tree again, not from `survey`, and takes *released*, "which only git answers", from `survey`. A git answer reused within the run keeps to that split.

**Where a per-run memo has to live** (read: `lib/sibling.py#load`, `.github/workflows/hygiene.yml:120`). CI runs `python3 skills/code-review/scripts/chain_check.py`, so the check is `__main__`. `pr_body.py` loads `chain_check.py` through `sibling.load`, which registers it under its stem `chain_check`, a second instance with its own module state. A store kept in `chain_check.py` would not reach the body arm's `follows`. `lib/gitcmd.py` is loaded once per process under the stem `gitcmd`, by both instances, `pr_body.py`, `settle.py`, `rule_changes.py` and `lib/optin.py`. `GITCMD.is_ancestor`, which `follows` and `verdict_problems` call directly, also goes through `gitcmd.git`.

**Nothing in the tree reuses a git answer today** (executed: `git grep -n -i -E 'lru_cache|functools\.cache|\bmemo|_cache\b|cache =|cached\b' 136cfca25 -- lib skills .github/scripts evals/scripts ':!*.md'`, with `--cached` lines dropped). The search prints two lines. `skills/verify/scripts/coordinates.py:147` caches a pure function of a text. `evals/scripts/noninferiority.py:179` names a directory. `chain_check.py#pins_and_copies_in` reads the tree once per run into `sources`, a dict `_checked` makes for the run. That is the shape this work takes for git.

**`git cat-file --batch` gives a blob's bytes as `git show <rev>:<path>` does** (executed, in scratch: a blob with `\r\n` line ends under a `textconv` driver that upper-cases; both commands printed the same bytes, and `show` applied no `textconv`). `settle.py#blobs` (`:563`) already reads `cat-file --batch` by the size each header gives. `settle.py#decoded` (`:488`) decodes as `lib/gitcmd.py#git` reads text: UTF-8 with undecodable bytes replaced, and `\r\n` and `\r` read as `\n`. `tests/skills/test_settle.py` `Test_blobs` pins both with two cases.

**A batch of commits' paths is not an exact reading** (executed, over #1581's branch). `git diff-tree --stdin --name-only -r --root -z` prints each commit's id as one NUL-ended field before its paths, so a path whose bytes equal the next commit's id cannot be told from it. `git log --name-only` is porcelain, and configuration such as `diff.renames` changes what it lists.

**The cases that count or order the git calls** (read). In `tests/skills/test_chain_check.py`, `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line` (`:4302`) asserts `len(asked) == 1` for argv words. In `tests/skills/test_settle.py`, `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line` (`:3066`) and `test_refuses_a_git_or_gh_that_did_not_answer_in_local_mode` (`:3101`) do the same. Each raises on the first matching argv, which ends the run before any second ask, so a memo leaves them as they are. `tests/skills/test_settle.py:3473` counts calls of `optin.git_common_dir`, not processes. No stub in the three modules answers one argv differently on a later call (executed: `grep -n 'nonlocal\|itertools.count\|side_effect\|\.pop(0)'`). Batching `settle.py#timeline`'s `show` would leave that dry-run case's `show` words with nothing to match, because timeline's `show` (`settle.py:263`) is the dry run's only one (executed: `git grep -n '"show"' 136cfca25 -- skills/settle/scripts/ lib/`).

**The search `frame/plan.md` phase 2 holds to one file** (executed at `136cfca25`). `git grep -n -E '^def decoded' 136cfca25 -- lib skills` prints one line, `skills/settle/scripts/settle.py:488`, the definition *Scope* item 4 moves and a `## Removes` row names. The pathspec holds `lib` and `skills` alone, so the work item's directory is outside it. After phase 2 the search names `lib/gitcmd.py` alone.

**The Windows leg before this work** (executed: `gh run download <id> -n test-durations`, summed by module). Run 45299542580, the first push on `main` after v0.38.6, read 986 s for the suite. Run 45263875467, #1581's last dispatch at the same code, read 729 s. The modules of at least 40 s in either run:

| Module | 45299542580 | 45263875467 | Ratio | Reaches `chain_check.py` or `settle.py` |
|---|---|---|---|---|
| `tests/skills/test_chain_check.py` | 162.6 | 114.7 | 1.42 | yes |
| `tests/skills/test_settle.py` | 87.3 | 64.0 | 1.36 | yes |
| `tests/skills/test_seal.py` | 65.1 | 47.2 | 1.38 | yes |
| `tests/skills/test_pact_check.py` | 51.4 | 27.8 | 1.85 | no |
| `tests/skills/test_session_cost.py` | 49.9 | 37.2 | 1.34 | no |
| `tests/skills/test_broad_gate.py` | 49.8 | 37.2 | 1.34 | yes |
| `tests/skills/test_agentic_pytest_record.py` | 42.6 | 37.5 | 1.14 | no |
| `tests/skills/test_pr_body.py` | 41.7 | 29.3 | 1.42 | yes |

"Reaches" is `git grep -l -E 'chain_check|settle\.py|settle\.main|seal settle|pr_body' -- 'tests/*.py'` naming the module (executed). The modules it does not name are the control modules of S8.

## Scope

In:

1. `lib/gitcmd.py` holds a per-run memo. While a run is inside it, `git` answers an argv it already answered in that run from the first answer, and starts no process. The memo ends with the run. The docstring states which runs may enter it.
2. `skills/code-review/scripts/chain_check.py#main` runs `_checked` inside the memo. The body arm's reads through `pr_body.py` and the rule-changes arm's reads through `skills/settle/scripts/` happen inside it too.
3. `skills/settle/scripts/settle.py#main` runs `_settled` inside the memo, under every flag.
4. `lib/gitcmd.py` takes `settle.py#decoded` and the parse of `cat-file --batch` output from `settle.py#blobs`. `blobs` keeps its name, its signature and its `RuntimeError`, starts its process through `git_run` as now, and reads the output through the moved parse.
5. `chain_check.py#tracked_declarations` reads the declarations HEAD carries through one `git cat-file --batch`, given the blob ids its `ls-tree` already lists, and read through the parse of item 4. Under `--worktree` it reads each one from disk through `read_record`, as now.
6. `.claude-plugin/plugin.json` moves to `0.38.7`.

Out:

- Reading the judged work item's records, its design, plan, round records, gate record, guarantee and `pr.md`, through one batch. After item 1 each is one process per run. Whether the leg is worth a further phase for them is `frame/questions.md` Q1's.
- One process for the later commits' paths in `follows`. No exact reading exists (*Grounding*, *A batch of commits' paths is not an exact reading*). After item 1 each commit is one `diff-tree` per run.
- One batch for `settle.py#timeline`'s designs. `frame/plan.md` *Alternatives considered* A8 gives the grounds.
- `seal pr-body` run on its own. Its run asks `_seal_at_head`'s one `rev-parse` and one `follows`, and so asks no read twice (read: `pr_body.py:543`).
- `gh` calls. Each is asked once per run, and a memo of a network answer is no reading of git.
- The git a test fixture starts to build its world.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. One `chain-check` run asks each git read once | Given the two worlds of `tests/skills/test_chain_check.py` whose runs repeat reads today: `branch`, declared through the review chain, whose round records `records` and `unread` each read, and `bodied`, sealed, whose guarantee's target `guarantee` and the body arm each ask `follows` of. When `chain_check.main` runs on each as a ready pull request, `bodied` with a body in its payload. Then no argv reaches `subprocess.run` twice in either run. | A case in `tests/skills/test_chain_check.py` records every argv `subprocess.run` receives during each `main` and asserts none repeats. It is seen red against `136cfca25`'s `chain_check.py`, where the round records' `show` and the guarantee's `follows` reads repeat. |
| S2. No answer outlives its run | Given two runs of `main` in one process over one repository, with a commit between them that changes what a reader answers. When each run reads. Then the second run reads the new commit. | A case in `tests/lib/test_gitcmd.py`: inside one scope an argv starts one process, and a second scope entered after the first is left asks again and reads the new answer. In `tests/skills/test_chain_check.py`, `Test_main::test_accepts_a_release_pull_request_leaving_a_squashed_item_to_its_own` and `Test_rule_changes_read::test_accepts_a_spec_another_pull_requests_squash_carried_unread` already run `main` twice with a commit between and read the second verdict, so no new case is added there. Each of the three is seen red against a memo that is not emptied when its run ends. |
| S3. Outside a run nothing is reused | Given `gitcmd.git` called outside any scope. When one argv is asked twice. Then two processes start. | A case in `tests/lib/test_gitcmd.py` counting `subprocess.run` calls, seen red against a memo that is always on. |
| S4. A command that gave no answer is asked again | Given a scope. When an argv raises `Unrun`, and when an argv with `check=True` exits non-zero. Then a second ask of the first starts a process again, and a second ask of the second raises `Exited` again. | Cases in `tests/lib/test_gitcmd.py`, seen red with `Unrun` stored and with `check` applied only on the first ask. |
| S5. One `settle` run asks each git read once | Given a shared root whose released designs fall into groups that share a pair of commits, one of them with an open `gaps.md` row, and a published release. When `settle.main` runs the dry run, and `--apply`. Then no argv reaches `subprocess.run` twice in either run. | Cases in `tests/skills/test_settle.py`, seen red against `136cfca25`'s `settle.py`, where the ancestry pair, `ls-files -z` and, under `--apply`, `versions`' reads repeat. `ls-files -z` is reached only through `open_rows`, so it repeats only where a design has an open row, which the *Given* gives. |
| S6. The declarations at HEAD take one process | Given a repository carrying several declarations at HEAD, one with `\r\n` line ends. When `tracked_declarations` reads them. Then one `cat-file --batch` process and no `show` reads them, and its `(path, parsed)` list equals what reading each through `read_record` gives. Under `--worktree` each is read from disk. | A case in `tests/skills/test_chain_check.py` counting the processes and comparing with `read_record`'s readings, seen red against `136cfca25`'s per-file reads. `Test_blobs` in `tests/skills/test_settle.py` passes unchanged over the moved parse. |
| S7. No output, exit code or verdict changes | Given the modules that hold both commands. When the crafter runs them after each phase. Then every existing case passes unchanged, apart from cases that count or order the git calls themselves, of which *Grounding* finds none that changes. | The crafter runs `bin/test tests/lib/test_gitcmd.py tests/skills/test_chain_check.py tests/skills/test_settle.py tests/skills/test_pr_body.py -q` after each phase. The broad run is the orchestrator's. |
| S8. The Windows leg reads the saving | Given a `workflow_dispatch` run of `tests` at the frame's commit and one after each phase. When the orchestrator sums each run's `test-durations` artifact by module. Then `test_chain_check.py` and `test_settle.py` each read a ratio below the ratios of the control modules between the same two runs, or the orchestrator's judgment records that the leg shows no saving. | The orchestrator runs `gh workflow run tests --ref perf/1603-chain-check-asks-git-the-same-question-several-times`, then `gh run download <id> -n test-durations -D <dir>` and #1581's S1 sum over `tests/skills/test_chain_check.py tests/skills/test_settle.py tests/skills/test_pact_check.py tests/skills/test_session_cost.py tests/skills/test_agentic_pytest_record.py`. The control modules are the last three, from *Grounding*'s table. It writes each judgment in `frame/plan.md` *Judgments of the run*. No local figure stands in. |
| S9. A real pull request's check starts fewer processes | Given #1581's branch, its merge base and a payload with a body, as *Grounding* ran them. When `chain_check.main` runs after each phase. Then after phase 1 it starts as many processes as *Grounding* counts distinct, and repeats none. After phase 2 it starts 37, the declaration reads *Grounding* counts having become one process. | The same probe, `test_tmp_run.py` in the framer's scratch, over a fresh `git clone --no-local` of the branch at the phase's commit, run by the orchestrator. It is a count, not a gate. |
| S10. The version is 0.38.7 | Given the last phase's commit. When `.claude-plugin/plugin.json` is read. Then `version` is `0.38.7`, in the commit that adds `changelog.md`. | `git show <commit>:.claude-plugin/plugin.json` and `git show --stat <commit>`. |

## Data & interfaces

- `lib/gitcmd.py#one_run`, a context manager, standard library only and Python 3.9 syntax, as the module's docstring requires. Entering it makes a store for the run. Leaving it, by return or by exception, drops the store. Entering it again while a store stands uses that store and leaves it standing at exit, so the outer run owns it.
- `lib/gitcmd.py#git` inside a run: the key is `(root, args, given, binary, env)`, with `env` taken as its sorted items. The stored value is the `subprocess.CompletedProcess` that `_start` returned with `check` false. `check=True` is applied to the stored value on every ask, raising `Exited` as `_start` builds it. `Unrun` is never stored. Outside a run, `git` starts a process on every call, as now. `gh` is never stored.
- The docstring paragraph states the contract: a command enters `one_run` for a run in which nothing the command writes changes what git answers it. `chain-check` writes nothing. `settle` writes the working tree under `--apply` and the policy root under `--draft`, after its last git read.
- `lib/gitcmd.py#decoded(data)` is `settle.py#decoded` moved unchanged. `lib/gitcmd.py#batch_texts(out, names)` is the loop of `settle.py#blobs` that reads `cat-file --batch` output, moved unchanged, returning `[(text, None) or (None, answer)]` for NAMES in order. `settle.py` keeps no copy of either. Its callers read `gitcmd.decoded`.
- `chain_check.py#tracked_declarations(root, routing, work_items)` keeps its signature and its answer, `[(path, parsed)]`. In HEAD mode the blob id of each regular `routing.md` entry of its `ls-tree` goes to one `cat-file --batch` through `GITCMD.git(..., binary=True)`. A text the batch answers with `missing`, or a non-zero exit of the batch, reads as `read_record`'s None reads now, as an empty text that `routing.parse` refuses.

## Rule changes

- nothing
  why: The work changes how many processes a run of chain-check or settle starts, and no rule of the policy root states that count. The memo's contract stands in the docstring of lib/gitcmd.py, which docs/running/what-a-script-gates.md names as the home of the runner's details.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The second `show HEAD:<item>/routing.md` of a run | `chain_check.py#tracked_declarations` and `#_checked` | the run memo of `lib/gitcmd.py#git` |
| The second `show HEAD:<item>/frame/design.md` of a run | `chain_check.py#frame` and `#rule_changes_read` | the run memo |
| The second `ls-tree -z HEAD -- <item>/trail/rounds/` and the second and third `show` of each round record | `chain_check.py#records`, `#unread` and `#originals_of` | the run memo |
| The repeated `merge-base --is-ancestor <commit> HEAD` and `diff-tree <commit>` of a fixed commit | `chain_check.py#verdict_problems` and `#records_only` | the run memo |
| The repeated `rev-parse`, `merge-base --is-ancestor`, `rev-list` and `diff-tree` reads of `follows` | `chain_check.py#records`, `#broad_gate`, `#guarantee` and `pr_body.py#_seal_at_head` | the run memo |
| The second `rev-parse --verify --quiet <base>^{commit}` | `chain_check.py#resolves` and `pr_body.py#_seal_at_head` | the run memo |
| The repeated `merge-base --is-ancestor` of one pair of commits | `skills/settle/scripts/rule_changes.py#unordered`, asked per group by `settle.py#timeline` | the run memo |
| The second `ls-files -z` | `settle.py#tracked_names` and `#tracked_text` | the run memo |
| The second `for-each-ref`, `cat-file --batch-check` and `rev-list --parents --stdin` of `versions` | `settle.py#earlier_judgments` and `#notes`, under `--apply` | the run memo |
| One `show HEAD:<dir>/routing.md` process per work-item directory HEAD carries | `chain_check.py#tracked_declarations` | one `cat-file --batch`, read by `lib/gitcmd.py#batch_texts` |
| `settle.py`'s own decoding of git's text and its own parse of `cat-file --batch` output | `settle.py#decoded` and the loop of `settle.py#blobs` | `lib/gitcmd.py#decoded` and `#batch_texts`, which `chain_check.py` reads too |

Framed 2026-11-24 by framer, before the build.

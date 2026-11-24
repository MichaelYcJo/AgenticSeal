# Review round 1: 1795483768-chain-check-asks-git-the-same-question-twice

```seal
target: 4b19aa77c against origin/release/v0.38.7
```

The round read the branch against `origin/release/v0.38.7` at `fe09bef46`, the merge base, in a `git clone --no-local` of the repository at `4b19aa77c`. It read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` whole at the target, and both phase records. No earlier round exists, so no fact was carried from one. The coordinates the frame names, such as `frame/design.md` *Grounding*'s call chains and *Which reads cannot change within one run*, were opened at the target rather than taken as read.

The question the round was spawned on is whether an answer the memo returns can differ from what a fresh git process would answer at that point of the run, and whether any verdict, output line or exit code changes. The round found no such answer, and no changed output, in the paths it read and ran (*What matched* below). It found one false sentence in the contract the memo rests on (finding 1), and two records that state counts or open items the target contradicts (findings 2 and 3).

## Findings

### 1. The memo's contract says `seal settle` writes after its last git read, and from a linked worktree it reads git after its writes

```seal
severity: should
location: `lib/gitcmd.py:19-25`, `skills/settle/scripts/settle.py:2064-2065`, `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/frame/design.md:32`, `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/frame/design.md:100`
evidence: executed `python3 test_tmp_settle.py <code> <out> --root <a linked worktree at fe09bef46> --released-at v0.38.6` with `--draft` and with `--apply`, from `fe09bef46`'s code and from `4b19aa77c`'s, each over its own worktree; read `skills/settle/scripts/settle.py:1877`, `skills/settle/scripts/settle.py:1981-1983`, `skills/settle/scripts/settle.py:253-259`, `skills/settle/scripts/settle.py:1898`, `skills/settle/scripts/fold_check.py:247-248`, `lib/optin.py:137-141`
```

Why it matters: the module docstring is where `frame/plan.md` *Technical context* sends the next reviewer. Its failure scenario says a reviewer catches a read added after `apply`'s first `rmtree` by opening this docstring. The docstring tells that reviewer no such read exists, and one does. The claim is that `seal settle` "writes the working tree under `--apply`, and the policy root under `--draft`, after its last git read" (`lib/gitcmd.py:22-23`). The comment at `skills/settle/scripts/settle.py:2064` says the same: "Every write of the run follows its last git read". The frame states it at `frame/design.md:32` ("Neither starts git") and at `frame/design.md:100`.

What the code does: `draft` calls `policy_root(root)` after its writes (`settle.py:1877`). `apply` calls `policy_root(root)` and `write_after` after its removals (`settle.py:1981-1983`). `policy_root` reaches `optin.git_common_dir` (`settle.py:257-258`). `write_after` reaches `fold.seal_home`, then `fold_check.py#located`, then `optin.git_common_dir` (`settle.py:1898`, `fold_check.py:247-248`). Where `.git` is a file, as in a linked worktree, `git_common_dir` starts `git rev-parse --git-common-dir` (`lib/optin.py:137-141`). The frame's grep at `frame/design.md:32` counted `gitcmd` and `subprocess` in `fold_check.py` alone, and missed the path through `lib/optin.py`. The probe shows it. From `fe09bef46`'s code, which has no memo, `--draft` started `rev-parse --git-common-dir` once after its first write, and `--apply` started it twice after its first `rmtree`. From the target's code both answered it from the memo, and stdout, stderr, the exit code and the resulting tree equal the base code's.

So no answer is wrong. The directory a run writes under is never the git directory that read names. The contract's real condition, "nothing the command writes changes what git answers it" (`lib/gitcmd.py:21-22`), holds. The sentence that names *when* settle writes is the false one. Commit `1ecdde329` says "the memo's docstring line ran past the width", but it moved the overflow to `lib/gitcmd.py:22`, which is 121 columns wide. No lint selects that width, and the snippet below rewraps the line.

```python
**A run inside `one_run` asks git each question once.** Inside it, `git`
answers a command the run already asked from the first answer. A command
enters it for a run in which nothing the command writes changes what git
answers it, so an answer given again is the answer git would give.
`chain-check` writes nothing. `seal settle` writes the working tree under
`--apply`, and the policy root under `--draft`. The only git read after
those writes asks where the common git directory is
(`lib/optin.py#git_common_dir`, from a linked worktree), and neither write
moves it. A git write inside a run, or any other read after a write the
run made, is answered as git answered before it. `gh` is asked every time.
```

```python
        # Its writes change nothing git answers it: the only read after them
        # asks where the common git directory is. So git answers each read
        # once in it (`lib/gitcmd.py#one_run`).
```

The fix also owes the frame's two statements. At `frame/design.md:32`, "Neither starts git" becomes "Neither starts git itself, and each reaches `lib/optin.py#git_common_dir`, which from a linked worktree asks `rev-parse --git-common-dir`; no write of `apply` moves that answer". At `frame/design.md:100`, "after its last git read" becomes "and the only git read after those writes asks where the common git directory is". The fix changes no code, and the round found no case that would pin a docstring.

### 2. The changelog says the declarations were 49 of the 85 distinct processes, and #1581's run asked 48 distinct

```seal
severity: should
location: `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/changelog.md:4`, `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/frame/design.md:17`
evidence: executed `python3 test_tmp_real.py <code> <out> --baseline ef776317b --root <#1581's branch at af3a0ec43>` from `fe09bef46`'s code with the payload of `frame/design.md` *Grounding* and `GITHUB_HEAD_REF` set; executed `git ls-tree -r HEAD -- seal/threads/` over #1581's branch, counting the `routing.md` entries; read `frame/design.md:17`, `changelog.md:4`
```

Why it matters: the fragment becomes the release note, which tells readers what the change saved. It says `tracked_declarations` "started one `git show` for each work item's `routing.md` ..., 49 of the 85 processes in #1581's run" (`changelog.md:4`). The 85 are the distinct processes. #1581's HEAD carries 48 `routing.md` files, all mode `100644` (executed). The base code's run started 105 processes, 85 of them distinct, as the changelog says. Of those 105, 49 were `show HEAD:<item>/routing.md`, and 48 of them were distinct. The 49th was the judged work item's own declaration, read a second time by `_checked`. So the figure is 49 of the 105 processes, or 48 of the 85 distinct ones. `frame/design.md:17` states the same miscount: "85 of them are distinct ... and 49 of those are `show HEAD:<dir>/routing.md`, one for each work-item directory HEAD carries". That count is where S9's expected 37 came from (`frame/design.md:93`). The orchestrator's judgment row explains the 39 by the steps it measured, and those hold. Phase 2 removed 47 distinct `show` processes and added one batch, so 85 - 47 + 1 = 39 (`frame/plan.md:48`). S9's 37 and the judgment row are dated readings that state what they measured, and they stay as they are.

```markdown
- **The pull request check reads the routing declarations HEAD carries through one git process (#1603).** `chain_check.py#tracked_declarations` started one `git show` for each work item's `routing.md` to find the declaration naming the branch, 48 of the 85 distinct processes in #1581's run. It now reads them through one `git cat-file --batch`, given the blob ids its `git ls-tree` lists. Each text reads as `git show` read it. A batch that exits non-zero reads as no declaration, as a failed `show` did. Under `--worktree` each declaration is still read from disk.
```

At `frame/design.md:17`, "and 49 of those are `show HEAD:<dir>/routing.md`, one for each work-item directory HEAD carries" becomes "and 48 of those are `show HEAD:<dir>/routing.md`, one for each of the 48 work-item directories HEAD carries".

### 3. Four `## Not verified` rows of `gaps.md` stand open, and the target answers each in `frame/plan.md` *Judgments of the run*

```seal
severity: should
location: `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/gaps.md:7`, `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/gaps.md:8`, `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/gaps.md:10`, `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/gaps.md:11`
evidence: read `gaps.md:7-11`, `frame/plan.md:48-49`; executed `gh run view <id> --json headSha,headBranch,event,conclusion` for runs 45307666454, 45309515939 and 45311061260
```

Why it matters: an open row tells the sealer, and the reader of the pull request body `seal pr-body` composes from the records, that nobody has answered the item. `seal settle --apply` also keeps the directory while a row stays open. Rows 7 and 10 ask whether the two modules read a lower ratio on the Windows leg after each phase (S8). Rows 8 and 11 ask how many processes the real check starts after each phase (S9). Each names the orchestrator as its answerer. Commit `4b19aa77c`, the target, wrote both answers into `frame/plan.md:48-49` and quoted them in `pr.md`, and left the four rows without `closed`. The three runs are on this branch as `workflow_dispatch` runs of `tests`, at `c66128300`, `541d15e3b` and `c45339551` (executed). The run at the frame commit concluded `failure`. Its one failing case, on every leg, was `test_every_spec_directory_that_reached_the_ladder_has_an_overview`, over this work item, which had no `gaps.md` yet. Its Windows durations artifact was still built. Rows 9 and 12, the test files outside the boundary runs, stay open for the broad gate.

```markdown
| closed Whether `tests/skills/test_chain_check.py` and `tests/skills/test_settle.py` read a lower ratio than the control modules on the Windows leg of `tests` after phase 1 (`frame/design.md` S8). No local figure stands in for the leg. | the orchestrator: runs 45307666454 at `c66128300` and 45309515939 at `541d15e3b` read no saving out of the leg's spread (`frame/plan.md` *Judgments of the run*, the row on S8) |
| closed How many processes `chain_check.main` starts over #1581's branch after phase 1, and whether it repeats none (`frame/design.md` S9). The phase did not run the probe. | the orchestrator: 85, none repeated, at `1ecdde329` (`frame/plan.md` *Judgments of the run*, the row on S9) |
| closed Whether `tests/skills/test_chain_check.py` and `tests/skills/test_settle.py` read a lower ratio than the control modules on the Windows leg of `tests` after phase 2 (`frame/design.md` S8). No local figure stands in for the leg. | the orchestrator: runs 45307666454 at `c66128300` and 45311061260 at `c45339551` read no saving out of the leg's spread (`frame/plan.md` *Judgments of the run*, the row on S8) |
| closed How many processes `chain_check.main` starts over #1581's branch after phase 2, against the 37 `frame/design.md` S9 expects. The phase did not run the probe. | the orchestrator: 39, none repeated, at `cde1d5925` (`frame/plan.md` *Judgments of the run*, the row on S9) |
```

## Confirmations

What matched: the memo returns no answer a fresh process would give differently, by the cases the round walked in `lib/gitcmd.py:212-263` (read). The round's own walk follows. The key is `(root, args, given, binary, env)`, and `argv` adds only the constant `KEYS`, so no module state outside the key shapes the command. Nothing in `chain_check.py`, `pr_body.py`, `skills/settle/scripts/` or `lib/` assigns `os.environ` or calls `os.chdir` (executed: `git grep` for each). No caller assigns `.stdout`, `.stderr` or `.returncode` of a returned process, so handing one process object to two callers is safe (executed: `git grep`). `Unrun` is raised before the store is written, and `check` is applied to the stored process on each ask, raising `Exited` with the arguments `_start` gives it (`lib/gitcmd.py:207-208`, `:261-262`). `one_run` drops the store in a `finally`, and an inner entry joins the outer run. Only the two `main`s enter it, and no script calls either `main` in-process: `bin/seal` starts each script through `lib/launch.py#runpy.run_path`, one per process (executed: `git grep`).

What matched: every git command the two runs can start is a read. An `ast` walk of every `git`, `git_run`, `git_out`, `git_fields` and `show` call in `chain_check.py`, `pr_body.py`, `skills/settle/scripts/*.py` and `lib/*.py` lists `rev-parse`, `diff`, `merge-base`, `show`, `ls-tree`, `log`, `diff-tree`, `rev-list`, `ls-files`, `cat-file`, `status`, `hash-object` and `for-each-ref`. The seven calls with a variable subcommand are the readers' own wrappers (executed). `hash-object` takes no `-w`. This confirms `frame/design.md:28`. The one read after a write is finding 1's.

What matched: no output line, exit code or verdict of `chain-check` changes over a real branch, the claim in `changelog.md:7` and `frame/plan.md:48`. From `fe09bef46`'s code and from `4b19aa77c`'s, over #1581's branch at `af3a0ec43` against `ef776317b`, stdout and stderr were byte-identical in three modes (executed, `test_tmp_real.py`). With the payload the base code started 105 processes, 85 distinct, and the target 39, none repeated, both exit 1. With no payload the base started 99, 84 distinct, and the target 38, both exit 0. Under `--worktree` the base started 39, 28 distinct, and the target 28, both exit 0. This confirms S9's 105, 85 and 39 as `frame/plan.md:48` reads them.

What matched: no output, exit code or tree of `seal settle` changes, over a linked worktree of this repository at `fe09bef46` with `--released-at v0.38.6` (executed, `test_tmp_settle.py`). The dry run, `--all-earlier`, `--draft` and `--apply` printed identical stdout and stderr from the base code and from the target's code. `--draft` and `--apply` left identical trees (`diff -r`). The base code started 102, 102, 103 and 126 processes. The target started 96, 96, 96 and 115, none repeated. The `--apply` run read release notes through `gh`, which the memo leaves unstored.

What matched: `tracked_declarations` reads each declaration as `read_record` read it (`chain_check.py:1869-1917`, read). The kept entries are still `REGULAR` blobs, and `cat-file --batch` by blob id prints what `git show HEAD:<path>` prints with no `textconv` and no filter. `lib/gitcmd.py#decoded` applies the replacement and the line-end reading that `_start`'s `encoding="utf-8", errors="replace"` text mode applies. A failed or `missing` batch reads as `routing.parse("")`, as `frame/design.md:102` states. One consequence follows from that frame line rather than from the code: in a repository with a corrupt object, a batch that exits non-zero drops every declaration, where a failed `show` dropped one.

What matched: the four S7 modules pass at the target, 608 cases (executed). S1's case goes red with `chain_check.main`'s `with GITCMD.one_run():` replaced by `with open(os.devnull):`. Both parameters fail at `assert repeated(asked) == []` (executed in the clone, then restored with `git checkout`). That confirms phase 1's mutant 13. The other mutation rows of both phase records were not re-run.

What matched: `decoded` and `batch_texts` moved with their bodies unchanged, and `settle.py` keeps no copy. `git grep` finds no caller of `settle.decoded` outside the module, and no document names the old place (executed). `seal layout --check` over the three test files reports `Test_decoded` and `Test_batch_texts` as missing without refusing. The other 71 of its 73 reports name functions of `chain_check.py` and `settle.py` that this work did not add (executed). `gaps.md` *Not done* states that, and `frame/plan.md` phase 2 names `Test_blobs` as the moved units' proof. `seal layout --pairs` names no pair (executed). Each new case holds a fact the frame states: S1 to S6, and G3 for the `declarations` parameter.

What matched: `pr.md`'s three quotes are word for word at `frame/plan.md:48`, `:49` and `:50` (read). `Commit and pull request language` is English, so no `pr.<lang>.md` is owed. `.claude-plugin/plugin.json` reads `0.38.7` in `5b2b334a1`, the commit that adds `changelog.md` (read, S10). The suite is labelled honestly: both phase records name their narrow and boundary runs as executed, and `gaps.md:9` and `:12` leave the broad gate to the orchestrator.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The seconds each of runs 45307666454, 45309515939 and 45311061260 reads per module from its `test-durations` artifact. This round read each run's commit, event and conclusion, and the failing case of the first, and not the artifacts. | `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/frame/plan.md:49` | the orchestrator, whose judgment row reads them |
| Whether a test file outside the 34 and 38 paths of the phases' boundary runs passes at the target. | `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/gaps.md:9`, `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/gaps.md:12` | the orchestrator's broad run at HEAD, then the sealer |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/lib/test_gitcmd.py tests/skills/test_chain_check.py tests/skills/test_settle.py tests/skills/test_pr_body.py -q`, in the clone at `4b19aa77c` | 608 passed, exit 0 |
| The same clone with `chain_check.main`'s `with GITCMD.one_run():` replaced by `with open(os.devnull):`, then `bin/test tests/skills/test_chain_check.py -q -p no:xdist -k test_asks_git_each_read_once_in_a_run` | 2 failed, both at `assert repeated(asked) == []`; the file was restored by `git checkout` |
| `test_tmp_real.py`, in the round's scratch: `chain_check.main` loaded from `fe09bef46`'s code and from `4b19aa77c`'s, over a clone of #1581's branch at `af3a0ec43`, `--baseline ef776317b`, `GITHUB_HEAD_REF` set; with the framer's payload, with none, and with `--worktree` | processes 105 (85 distinct) to 39, 99 (84) to 38, 39 (28) to 28; exit codes 1, 0 and 0 on both sides; stdout and stderr identical in all three |
| `test_tmp_settle.py`, in the round's scratch: `settle.main` from both codes over two linked worktrees of one clone at `fe09bef46`, `--released-at v0.38.6`; the dry run, `--all-earlier`, `--draft` and `--apply`, each git process marked when it starts after the run's first `rmtree` or file write | processes 102, 102, 103 and 126 to 96, 96, 96 and 115, none repeated; base code after its first write: `rev-parse --git-common-dir` once under `--draft` and twice under `--apply`, target: none; stdout, stderr, exit codes and the resulting trees identical |
| `git ls-tree -r HEAD -- seal/threads/` over #1581's branch, counting `routing.md` | 48 entries, all `100644` |
| `bin/seal layout --check` and `bin/seal layout --pairs` over the three changed test files | 73 reports of a missing class, 0 refused, exit 0; 0 pairs |
| `gh run view <id> --json headSha,headBranch,event,conclusion` for 45307666454, 45309515939 and 45311061260, and `gh run view 45307666454 --log-failed` | `workflow_dispatch` runs of `tests` on this branch at `c66128300` (failure), `541d15e3b` and `c45339551` (success); the failure is one case on every leg, `test_every_spec_directory_that_reached_the_ladder_has_an_overview`, over this work item, which had no `gaps.md` |

# Review round 2: 1795483768-chain-check-asks-git-the-same-question-twice

```seal
target: 76816d131, fixes 81b05bd5c..76816d131
```

This is a verifying round. Its code is the diff of the four commits after round 1's record: the framer's fold `539ad6527`, the orchestrator's `540edf640`, the crafter's fix `ed3317753` and the close blocks of `76816d131`. The round worked in a `git clone --no-local` of the repository at `76816d131`. It read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` whole at `76816d131`, both phase records, and round 1. Commit and pull request language is English, so no `pr.<lang>.md` is owed.

The fix diff changes no code. `lib/gitcmd.py` changes only its module docstring, and `skills/settle/scripts/settle.py` only the comment in `main` (executed: `git diff 4b19aa77c 76816d131 --stat`, then the diff of both files). The rest is the work item's records.

Facts carried from round 1 and not established again: the three `workflow_dispatch` runs, their commits and their conclusions (round 1's `gh run view` probe). The 48 `routing.md` entries at #1581's `af3a0ec43` (round 1's `ls-tree` probe). The output equality of `chain-check` over #1581's branch, and the 608 cases of S7's four modules. Round 1 ran those at `4b19aa77c`, whose code equals the target's apart from the docstring and the comment. The round re-derived these: the coordinates the fold cites, at the frame's commit `136cfca25` and at the target; round 1's settle probe, run again with the target's code; the `pr.md` quotes; and every git call reached after `settle`'s writes.

## Findings

### 1. The folded *Grounding* paragraph says `apply` calls `closed_rows` after the removals, and it calls it before each directory's removal

```seal
severity: should
location: `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/frame/design.md:32`
evidence: read `skills/settle/scripts/settle.py:1966-1991` at `136cfca25`, `skills/settle/scripts/settle.py:1092-1116` at `136cfca25`, `skills/settle/scripts/settle.py:813-819` at `136cfca25`, `frame/design.md:32` at `76816d131`
```

Why it matters: the paragraph is the grounds for the claim that no git read follows a write in `seal settle` other than the common git directory's. Its conclusion is "no other git read follows a write". To support it, the paragraph lists what `apply` calls after its writes. It says: "After the removals it calls `closed_rows`, which reads `lib/gaps.py`, then `policy_root` (`:2000`) and `write_after` (`:2002`)". The section reads the tree at `136cfca25`. In that tree `apply` calls `closed_rows` at `:1990`, inside the loop over the directories and before that directory's `shutil.rmtree` at `:1991`. It also calls `misplaced` at `:1971`, at the top of each pass of the loop. So after the first removal, `misplaced` and `closed_rows` run once for each later directory, and the paragraph does not name `misplaced`. The conclusion still holds. `misplaced` walks the directory with `os.walk` (`:1092-1116`), and `closed_rows` reads the closing memo through `read_text`, which opens the file (`:813-819`). Neither starts git. A sealer who checks the paragraph against `136cfca25` finds the order wrong. A reader who trusts it checks two of the four calls that follow a write. The fold `539ad6527` rewrote this paragraph for round 1's finding 1. The wrong order was already in the paragraph before it (`frame/design.md` at `c66128300`: "After the removals it calls `write_after` ... and `closed_rows`"), so this finding is neither a regression nor a reopening.

The paste-ready fix replaces the sentence from "After the removals" to "after its writes." in `frame/design.md:32`. The rest of the paragraph stays as it is:

```markdown
In its loop over the directories, `misplaced` (`:1971`) and `closed_rows` (`:1990`) run before each directory's `shutil.rmtree` (`:1991`), so after the first removal they run for each later directory; `misplaced` walks the directory and `closed_rows` reads its `gaps.md` from disk through `lib/gaps.py`. After the loop it calls `policy_root` (`:2000`) and `write_after` (`:2002`), which reads `fold_check.py`. `draft` (`:1863`) writes the policy root after `survey`, reads the documents from disk, and calls `policy_root` (`:1896`) after its writes.
```

No other statement in the tree places `closed_rows` after the removals. `frame/plan.md:13` names "a read other than `git_common_dir`'s after `apply`'s first `rmtree`", which agrees with the fix (executed: `git grep -n 'closed_rows' 76816d131 -- seal/threads/1795483768-chain-check-asks-git-the-same-question-twice`).

```seal
verdict: fixed 07794726d
answer: The framer folded the round's sentence into frame/design.md:32 as given at 07794726d: misplaced and closed_rows run inside apply's loop before each directory's rmtree, and policy_root and write_after after the loop; the paragraph's conclusion is unchanged. The framer's grep of the three frame files for closed_rows, misplaced and "after the removals" found no other statement of the order. The finding names records alone, so no verifying round reads this close; the sealer reads the fold at HEAD.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the module docstring at `lib/gitcmd.py:19-28` no longer says `seal settle` writes after its last git read. It now says the only git read after those writes asks where the common git directory is, from a linked worktree, and that neither write moves it. The comment at `skills/settle/scripts/settle.py:2064-2066` says the same. The round checked the claim against the code. `draft` calls `policy_root` after its writes (`settle.py:1877`). `apply` calls `policy_root` and `write_after` after its loop (`settle.py:1981-1983`). `policy_root` asks `lib/optin.py#git_common_dir` (`settle.py:253-259`), and `write_after` reaches it through `fold_check.py#located` (`fold_check.py:247-248`). `home_at` given the common directory starts nothing (`lib/optin.py:275-309`). `fold_check.py` holds no `gitcmd` or `subprocess` call. Neither do the modules it and `apply` load after a write: `lib/config.py`, `lib/gaps.py`, `lib/tables.py`, `lib/blocks.py`, `lib/console.py`, `lib/lines.py` and `lib/items.py` (executed: `grep -c`). The round ran round 1's probe again with the target's code, over two new linked worktrees of a clone at `fe09bef46`. `--draft` started 96 processes, 96 distinct, with 19 writes and no git process started after the first write. `--apply` started 115, 115 distinct, with 6 writes and none after the first write. Stdout and stderr equal round 1's run of `4b19aa77c`'s code byte for byte (executed, `diff`). Every line of the docstring is at most 74 columns, and `ruff check` and `ruff format --check` pass on both files (executed). The frame's two statements, `frame/design.md:32` and `:100`, were folded at `539ad6527`. Their coordinates hold at `136cfca25`: `policy_root` `:253`, `draft` `:1863`, `:1896`, `apply` `:1940`, `:2000`, `:2002`, `fold_check.py#located` `:239`, `lib/optin.py` `:123` and `:141` (executed). The fix pass's search for "last git read", "follows its last" and "after its last" also holds: the round's `git grep` of the three, at the target, finds no statement of the old fact (executed). Finding 1 above is a separate sentence of the same paragraph.

```seal
confirms: round-1#2
```
What holds: `changelog.md:4` now says that in #1581's run the declaration reads were 49 of the 105 processes, 48 of them distinct, one per `routing.md` its HEAD carries. That matches round 1's executed counts, which this round carried. The fix pass's wording differs from round 1's snippet. Its reason holds: the 49th read is `_checked`'s second read of the judged work item's own declaration. `frame/design.md:17` now states 49 of the 105 and 48 distinct, and names the 49th read. S9 at `frame/design.md:93` now expects 39, and explains it. The judgment row at `frame/plan.md:48` says "against the 37 S9 expected from *Grounding*'s count of the declaration reads". That is true of S9 at `c66128300` (executed: `git show c66128300:.../frame/design.md`). A `git grep -w 37` of the work item's records, the round records aside, finds that row, its quote in `pr.md` and `gaps.md:11`, each in the past tense, and three durations of 37.2 and 37.5 seconds in *Grounding*'s table at `frame/design.md:54-56`, which are not the count (executed).

```seal
confirms: round-1#3
```
What holds: `gaps.md:7`, `:8`, `:10` and `:11` carry `closed`. Each answer cites `frame/plan.md` *Judgments of the run* with the run and commit that answered it. Each row was edited in place, and the diff removes no row without `closed` (executed: `git diff 4b19aa77c 76816d131` of `gaps.md`). Row 11's change of "expects" to "expected at `c66128300`, before round 1's fold" is true. S9 read 37 at `c66128300`. Rows 9 and 12 stay open for the broad gate, as they should.

What matched: each of `pr.md`'s three quotes stands word for word, with whitespace collapsed, in `frame/plan.md` *Judgments of the run* (executed: a substring check of each quote against the plan). The changed first quote matches the row `540edf640` rewrote.

What matched: the judgment row the fold added at `frame/plan.md:51` states both folded facts as `frame/design.md` now states them. The citation at `frame/questions.md:6` names the renamed *Grounding* paragraph by its new title.

What matched: the narrow run over the files whose text the fix changed passes. `bin/test tests/lib/test_gitcmd.py tests/text/test_settle_reads_before_it_removes.py tests/text/test_a_record_carries_no_comment.py -q` passed 67 cases (executed). The fix diff adds no test and no code unit, so no case is read against its group.

The suite is labelled honestly: the fix pass changed only a docstring, a comment and records, and claims no suite run. `gaps.md:9` and `:12` leave the broad gate to the orchestrator.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a test file outside the boundary runs of both phases passes at the target, and the broad gate at HEAD | `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/gaps.md:9`, `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/gaps.md:12` | the orchestrator's broad run at HEAD, then the sealer |
| The seconds per module in the three runs' `test-durations` artifacts, which this round did not download, as round 1 did not | `seal/threads/1795483768-chain-check-asks-git-the-same-question-twice/frame/plan.md:49` | the orchestrator, whose judgment row reads them |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_settle.py <clone at 76816d131> <out> --root <linked worktree at fe09bef46> --released-at v0.38.6 --draft`, round 1's probe copied into this round's scratch | exit 0; 96 processes, 96 distinct; 19 writes; no git process started after the first write; stdout and stderr equal round 1's `4b19aa77c` run |
| The same with `--apply` over a second linked worktree | the first run exited 2, because the fixture clone's `origin` pointed at a local path and `gh` could not list releases, and nothing was written; after `origin` was set to the repository's GitHub URL: exit 1, 115 processes, 115 distinct, 6 writes, none followed by a git process; stdout and stderr equal round 1's `4b19aa77c` run |
| `bin/test tests/lib/test_gitcmd.py tests/text/test_settle_reads_before_it_removes.py tests/text/test_a_record_carries_no_comment.py -q`, in the clone at `76816d131` | 67 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over `lib/gitcmd.py` and `skills/settle/scripts/settle.py` | exit 0, both files |

# Review round 3: 1794465689-a-segment-counts-for-every-item-its-prompt-names

```seal
target: 61d4688c5, fixes 575d9f555..61d4688c5
```

This is the verifying round over round 2's fix. The code read is the fix diff `575d9f555..61d4688c5`. It holds three commits: the fix at `aef3641f6`, the close block at `8033eeac5`, and the orchestrator's fold of S8's *Verifiable how* cell at `61d4688c5`. The fix changed two of the work item's records, `gaps.md` and `frame/design.md`, and the round read both through the fix diff, on top of round 2's read. No other record of the work item changed in the range. The fix pass's account names the files it changed, so the round lists only the records its diff touched. Carried from round 2 and not re-established: the coordinates of `run_git` and of the S8 case, and round 2's verdict on round 1's three closes. The two mutant runs below were executed in a `git clone --no-local` at `61d4688c5` under the round's scratch directory. Each mutant was run alone, and the first was restored before the second.

Every statement of the S8 case's behaviour on an older git now says it skips. The round listed them with `git grep -n` on `goes red`, `S8` and the case's name over the work item's records, outside the round records (executed). That listing found the case's docstring, `gaps.md:9`, and the S8 row at `frame/design.md:60`. `frame/design.md:37` and `trail/phases/phase-1.md:11` name S8 and say nothing about an older git. No statement still says "goes red".

The round leaves nothing open. What comes due is the orchestrator's broad run at HEAD, and then the sealer's spawn.

## Findings

No finding.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the capability check stands word for word as round 2 gave it, after the local branch is made, at `tests/skills/test_session_cost.py:5690-5701` (read). The docstring sentence is there, and so is the new `gaps.md:9` wording (read). The guard has two arms, and each was shown separately (executed, in the scratch clone):

- With only the `known` check's env line removed, `cat-file -e` fetched the blob, and pytest reported `SKIPPED [1] tests/skills/test_session_cost.py:5697: this git fetched a blob with GIT_NO_LAZY_FETCH set, so it does not know the variable, and the branch read fetches there`, with exit 0. This matches the close's account.
- With only `run_git`'s env line removed, the case still failed on its count line, which read `1 also naming another work item, with 1 other work item read beside it`. So the new check does not turn the case's own mutant into a skip on a git that knows the variable.
- At the target, on git 2.50.1, the whole module passed: 276 passed, no skip (executed).

The S8 cell `61d4688c5` folds into `frame/design.md:60` describes the case as it stands (read). The close's claim that no older git was run stands as the close states it. `gaps.md:9` hands the legs' git versions to the `test` workflow.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the work item's HEAD; this round ran one module and two single-case runs, and labels the suite `unverified` | `seal/config.json` `Broad gate` | the orchestrator, by `seal gate --record` |
| Whether each CI leg runs the S8 case or skips it | `seal/threads/1794465689-a-segment-counts-for-every-item-its-prompt-names/gaps.md:9` | the `test` workflow at the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_session_cost.py -q -p no:xdist -k test_a_partial_clone_fetches_nothing -rs`, in a `git clone --no-local` at `61d4688c5` with the `env=` line of `run_git` removed | exit 1; the case failed on its count line, the page reading `1 also naming another work item, with 1 other work item read beside it` |
| the same command in the same clone, `run_git` restored, with the `env=` line of the case's `known` check removed | exit 0; `1 skipped`, with the case's skip reason printed at `tests/skills/test_session_cost.py:5697` |
| `bin/test tests/skills/test_session_cost.py -q -rs`, in the branch worktree at `61d4688c5` | exit 0, 276 passed, no skip |

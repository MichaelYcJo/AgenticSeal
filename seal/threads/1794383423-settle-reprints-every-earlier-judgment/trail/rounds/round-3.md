# Review round 3: 1794383423-settle-reprints-every-earlier-judgment

```seal
target: f56246f6e, fixes c52032e63..f56246f6e
```

This is a verifying round. It answers round 2's finding, closed at
`05394cbca`. It reviews fix pass 2, `f56246f6e`, which changes
`tests/skills/test_settle.py` alone, after PR #1526's Windows leg failed
three cases this work added. The range also holds:

- `84ac67961`, the merge of the base. It brought `957a3bc7d` (#1525), which
  its own review read.
- `254d9a27a`, the broad gate record.
- `0c2742d83`, the sealer's `guarantee.md`.

The work item's records outside `trail/` and `guarantee.md` are unchanged
since round 2's target. So is `skills/settle/`. `git diff --quiet 94d4bbae7
f56246f6e` over `frame/`, `gaps.md`, `changelog.md`, `pr.md`, `routing.md`,
`trail/phases/` and `skills/settle` exited 0 (executed). So round 2's whole
reading of them stands at this target.

## Findings

None.

## Confirmations

```seal
confirms: round-2#1
```
What holds: `05394cbca` changes round 1's close of finding 2 to
`verdict: fixed 0a354b5a7` (`round-1.md:192`). It leaves the answer line as
it was (read, `git diff c52032e63 11484a0e4`). `0a354b5a7` changed
`skills/settle/scripts/settle.py`, a path that finding's `location:` names.
Neither copy of `chain_check.py --worktree` refuses the line now
(executed).

What matched: the missing-object case still holds its fact
(`tests/skills/test_settle.py:1727-1772`). Fix pass 2 adds
`os.chmod(loose, 0o644)` before the unlink (`:1756-1760`). Git writes a
loose object read-only, and on Windows Python's `os.chmod` sets or clears
only the read-only attribute, from the owner write bit, which `0o644`
holds. On POSIX the unlink did not need the change, and the change does not
alter what the case sets up or asserts. The object is still gone when the
dry run reads, and the three assertions are unchanged. The case passed on
git 2.50.1 and git 2.39.3 (executed). Whether it passes on Windows is the
PR run's to say.

What matched: the newline case still holds its fact on every git that
accepts the path, and skips only where git refuses it
(`tests/skills/test_settle.py:1775-1834`).

- The guard is `added.returncode != 0 and name == odd` (`:1814`). A refused
  add of the plain path still fails the case on its `assert`.
- On git 2.50.1 and git 2.39.3 both parameters ran and passed, with no
  `SKIPPED` line under `-rs` (executed).
- With a probe git first on PATH that refuses, as Git for Windows does, an
  `update-index` of a path holding a newline (exit 128 and an
  `error: invalid path` line), both parameters skipped (executed). Each
  quoted that stderr. The S6 case beside them passed in the same run.
- The Linux and macOS legs of `test.yml` run git builds that accept the
  path. So the fact, a removed plan with a newline in its path named before
  the batch with the rest read, stays held in CI on every leg but Windows.

The code under test reads the history through `git log -z` and
`cat-file --batch` and never through the index or a checkout. Nothing in
it is Windows-specific. So the Windows leg skipping the case hides no
behaviour that only Windows would show.

The comment at `:1810-1813` and the skip's reason claim more than they
hold, and the round opens no finding for it. They say that no commit made
with that git, or "here", can hold such a path. A Windows clone can still
fetch such a commit made on another platform, and the dry run there reads
it the same way. A comment and a skip reason are read by whoever next
edits the case, and the skip itself stays right.

What matched: the narrow modules `tests/skills/test_settle.py` and
`tests/github/test_publish_release_note.py` passed at the target on git
2.50.1, 233 cases, none skipped (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The two changed cases on the Windows leg of PR #1526, started by the push of `f56246f6e` | `tests/skills/test_settle.py:1727-1834` | the orchestrator, by that run's result |
| Whether `git mktree` and `git commit-tree`, which do not pass through the index, take a name holding a newline on Git for Windows, which would let the newline case run on that leg as well | `tests/skills/test_settle.py:1796-1819` | the orchestrator, if it wants the case to run on Windows |
| The broad gate and the seal: `trail/gate.md` and `guarantee.md` were written at `254d9a27a` and `0c2742d83`, before `f56246f6e` | `seal/threads/1794383423-settle-reprints-every-earlier-judgment/guarantee.md` | the orchestrator, by the broad run at HEAD and the sealer's spawn after it, now that this round leaves nothing open |
| Whether the settling session reads the bounded section and runs `--all-earlier` where a kind may predate the window (design S8) | `skills/settle/SKILL.md` step 5 | the owner, at the next settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_settle.py tests/github/test_publish_release_note.py -q -rs`, in the clone at `f56246f6e`, git 2.50.1 | 233 passed, 0 skipped, exit 0 |
| `bin/test tests/skills/test_settle.py -q -rs -p no:xdist -k "newline or git_holds_no_text"`, git 2.39.3 first on PATH | 4 passed, exit 0 |
| the same, with the probe git that refuses an `update-index` of a path holding a newline first on PATH | 2 passed, 2 skipped, each skip quoting `error: invalid path`, exit 0 |
| `gh run view 42995460465 --log-failed` | the three failures: `PermissionError: [WinError 5]` at the unlink, and `update-index --cacheinfo` of the newline path exiting 128 in both parameters |

# 1792251842-the-smith-is-written-anew-from-its-job — phase 1

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | adbbea77, the framer's side; b4e72dbe the smith's, dc8991c2 the warden's |

## What this phase was asked

Take the baseline at 2fc33333 with the suite at af9c924b, for smith, warden
and framer in that order, one at a time: `noninferiority.py run --agent <a>
--rev 2fc33333 --suite-rev af9c924b --runs 2 -j 4` with `--out` in the
session scratch directory. Copy each side's raw directory to
`SpecSeal-worktrees/967-baseline-raw/<a>/`, write
`evals/baseline-<a>.json` with `run --from-raw`, and `cmp` it against the
scratch copy. Stop before the next agent once the phase's summed
`total_cost_usd` passes $75. A run cut short is no result, and it is rerun
once only for a named transient cause. Record per agent the runs, cut short
or not, spend, seconds, tool calls, all-model tokens, tokens per tool call,
preload bytes and each preload file's sha256 beside #957's phase-3 sides;
answer `questions.md` Q4; fill `plan.md` phase 1's Status.

## What this phase found

**The phase closed on its second attempt.** The smith's side was taken
first and stands. The warden's and the framer's first sides were cut short
by the host going to sleep, lid closed, and are no result. The orchestrator
took both again on 2026-10-18 between 09:28 and 10:17 KST with the lid open
(`ioreg` read `AppleClamshellState = No` before and after; `pmset -g log`
shows no sleep after 05:47 KST), each once, none cut short:

| Figure | smith (b4e72dbe) | warden (dc8991c2) | framer (adbbea77) |
|---|---|---|---|
| Cases / runs | 4 / 8 | 9 / 18 | 4 / 8 |
| Cut short | no | no | no |
| Spend USD (`total_cost_usd`) | 6.6210 | 42.2333 | 16.9055 |
| Session seconds | 1,360.8 | 8,177.8 | 2,018.5 |
| Eval wall seconds | 383 | 2,303 | 617 |
| Tool calls | 222 | 936 | 120 |
| Tokens read, all models | 9,561,086 | 81,616,964 | 3,275,602 |
| Tokens per tool call | 43,068.0 | 87,197.6 | 27,296.7 |
| Preload bytes (agent share) | 90,728 | 27,198 | 89,444 |
| Graders passed | 48 of 48 | 86 of 96, truths 14 of 24 | 64 of 64 |
| Report rows / false rows | — | 43 / 29 | — |

Figures from `noninferiority.py#side_numbers` over the committed files.
These three are the references phase 4 compares against; #957's phase-3
sides are not, since the contract differs (below).

The account of the first attempt follows, kept because the lost spend is
part of this phase's cost.

**The host slept through the warden's side, lid closed (executed).**

- 15 of the warden's 18 runs timed out: `rule-warden-one-finding`'s two at
  its 1800s bound, the other thirteen at 2400s. The three that finished are
  case `replay-1791382684-r2`'s two runs and one run of
  `replay-1791382684-r5`.
- Every timed-out trace holds one or two gaps of 738 to 1,007 seconds
  between a tool result and the agent's next turn. The gaps are the same in
  every run that was running at the time: the four runs of cases 5 and 6 all
  stop at 17:45:53–55Z and resume at 17:58:13–17Z.
- `pmset -g log` names the cause. From 01:21:23 KST (16:21:23Z) the machine
  entered `Sleep state due to 'Clamshell Sleep'` for 935, 950, 954, 966,
  1,037 and 735 seconds in turn, then `Maintenance Sleep` cycles of 916 to
  972 seconds with a DarkWake of about 45 seconds between them. The first
  warden gap runs 16:21:23Z to 16:37:04Z, and the log's first long sleep runs
  01:21:23 to 01:36:58 KST. `ioreg` read `AppleClamshellState = Yes` at
  04:42 KST. The `caffeinate` assertions that were held do not prevent
  clamshell sleep.
- The smith's side ran 16:02–16:09Z, before the first long sleep, and its
  eight traces hold no gap over 600 seconds.
- So the cause is a closed lid, not the definition or the harness. A person
  ends it by opening the lid or attaching a display, and no session can.
  It was still in force at hand-back: the machine slept again from 04:26:30
  to 04:42:14 KST, between two of this phase's own commands. Rerunning the
  warden under it would have paid about $35 for a second cut-short side.

**The framer's side was stopped, not cut short by the harness.** It started
at 04:25 KST, during a DarkWake. Since the cause was still in force, the run
was stopped by its task after 58 seconds, with four runs `interrupted`. Its
four kept directories under `/private/tmp/e-*` and its eval directory were
removed with `noninferiority.py#remove_kept`. No framer record exists.

**The smith's side** (`evals/baseline-smith.json`, from
`noninferiority.py#side_numbers` over the committed file):

| Figure | 2fc33333 (this phase) | 93c1878c (#957 `evals/smith-phase-3.json`) |
|---|---|---|
| Cases / runs | 4 / 8 | 4 / 8 |
| Cut short | no, `partial: false`, no run error | no |
| Spend USD (`total_cost_usd`) | 6.6210 | 5.9980 |
| Session seconds (`duration_ms` / 1000) | 1,360.8 | 1,320.6 |
| Eval wall seconds | 383 | 409 |
| Tool calls | 222 | 183 |
| Tokens read, all models | 9,561,086 | 8,270,573 |
| Tokens per tool call | 43,068.0 | 45,194.4 |
| Preload bytes (agent share) | 90,728 | 90,594 |
| Graders | all passed in all 8 runs | all passed in all 8 runs |

**The warden's cut-short side**, kept outside the tree, not a result:
18 runs, 15 timed out, eval `costUsd` 34.5493, 659 tool calls, wall 11,677
seconds, preload 27,198 bytes. `side_numbers` reads its spend, tokens and
seconds as `None`, because a timed-out run has no `result` event. The eval's
own per-run `costUsd` is what the spend below counts for it.

**The preload at 2fc33333 beside #957's phase-3 `## New preload` tables**
(sha256 from the sides' `specseal.preload`, and by `shasum -a 256` over `git
show 2fc33333:<file>` for the framer, which has no side):

| File | Bytes | sha256 at 2fc33333 | At #957's phase 3 (93c1878c) |
|---|---|---|---|
| `agents/smith.md` | 20,829 | `81f63874580681eac6d1920f2b6a10fd3ff24b376c2cd0b6308b0f57d879d1cd` | same |
| `agents/warden.md` | 10,527 | `13d9b9ac81eefe60980ecb686a845c72eabdca8d612819379e138a2d7c47a41e` | `ad823e75a69c1e11e2d1cfd1d06ad66f13006af2217d642a56dd91154ce93baf`, differs |
| `agents/framer.md` | 19,545 | `c2e7a7d7437485042ebda52e71a6a7137f9a1511258feb2e779ac19db9769486` | same |
| `skills/agent-contract/SKILL.md` | 16,671 | `9764cedd19617d9ba1af4d05a27384004456cf72c5333390c49cb7d57f7110dc` | `e4f679e31c041d4f7934367a9ce3bd826cf68af03e9e5319e84b3a8d327e34b3`, differs |
| `skills/implement/SKILL.md` | 32,228 | `bafff509c7b31c46ba8be3bcd71681a8682c5af6c76bd3fa28a5d743415315d9` | same |
| `skills/writing-style/SKILL.md` | 21,000 | `f509dfeeaec143e9c4d6580e77c919b885629da5bd28186db3bf569210dcd33e` | same |

**The frame missed one changed file.** `spec.md` §*The tree as it stands*
says the contract is the one file in the three read sets that changed
since #957's phase 3. `agents/warden.md` changed too. 93c1878c is not an
ancestor of 2fc33333, and `git diff 93c1878c 2fc33333 -- agents/warden.md`
is one sentence: the chain-check command in step 5 gained `--root <the
branch worktree>`. That does not change the frame's decision, because the
contract alone already makes all three phase-3 sides unusable as baselines.
It does mean the warden's baseline differs from #957's in two files, not
one.

**`payload-meter --agent <a>` at 2fc33333.** Nothing under `agents/`,
`skills/`, `evals/`, `bin/` or `CLAUDE.md` differs between 2fc33333 and
4604ea0e, so the meter ran on the branch. Totals, including the 13,318 B
`CLAUDE.md` pair: smith 104,046 B (32,514 tokens, estimated at 3.2 B/token),
warden 40,516 B (12,662), framer 102,762 B (32,113). The agent shares are
90,728, 27,198 and 89,444, the same as the frame's readings.

**Spend for this phase, eval `costUsd`:** the three sides that stand,
smith 6.6210, warden 42.2333, framer 16.9055, **65.7598**, which answers
`questions.md` Q4 against its estimate of about $60. The first attempt's
warden 34.5493 (cut short) and framer 3.8361 (stopped) bought no result:
**38.3854**. The phase spent **104.1452** in all. The orchestrator read the
plan's $75 stop as a bound on the sides that stand, since the $38.39 was
lost to the host and not to the agents measured, and took the second
attempt under the night's $200 budget (`questions.md` Q1).

### Commands, each with its exit code

Read directly with `; echo $?`, never through a pipe. `$S` is the session
scratch directory's `967-phase-1/`, `$K` is
`SpecSeal-worktrees/967-baseline-raw/`, and `$E` is this work item's
`evals/`.

| Command | Exit |
|---|---|
| `python3 evals/scripts/noninferiority.py run --agent smith --rev 2fc33333 --suite-rev af9c924b --out $S/baseline-smith.json --runs 2 -j 4` | 0 |
| `cp -R $S/baseline-smith.raw $K/smith`, then `diff -r` | 0, 0 |
| `python3 evals/scripts/noninferiority.py run --from-raw $K/smith --out $E/baseline-smith.json` | 0 |
| `cmp $S/baseline-smith.json $E/baseline-smith.json` | 0 |
| `git commit` of `evals/baseline-smith.json` | 0, b4e72dbe |
| the same `run` for `warden` | 0, side `cut_short: true` |
| `cp -R $S/baseline-warden.raw $K/warden-cut-short-1` and the side JSON beside it | 0 |
| the same `run` for `framer` | stopped by its task after 58 s, no exit code |
| `bin/payload-meter --root . --agent <a>` for smith, warden, framer | 0 each |
| `git diff --stat 2fc33333 HEAD -- agents skills evals CLAUDE.md bin` | 0, empty |
| `pmset -g log`; `ioreg -r -k AppleClamshellState` | 0 |
| second attempt: `run --agent warden --rev 2fc33333 --suite-rev af9c924b --out $S2/baseline-warden.json --runs 2 -j 4 --max-cost-usd 50`, `$S2` the scratch `967-phase-1b/` | 0, `partial: false` |
| `cp -R $S2/baseline-warden.raw $K/warden`, `diff -r`; `run --from-raw $K/warden --out $E/baseline-warden.json`; `cmp` | 0, 0, 0, 0 |
| the same `run` for `framer` with `--max-cost-usd 30`, then its `cp -R`, `diff -r`, `--from-raw`, `cmp` | 0, 0, 0, 0, 0 |

# Review round 3: 1795759278-the-cores-margin-depends-on-the-path

```seal
target: 9389704ec, fixes 5590dddf0..9389704ec
```

This is a verifying round. Its code bound is the fix range `5590dddf0..9389704ec`: the round-2 record (`f0b82e581`), the framer's fold of round 2's finding 2 with the orchestrator's routing row (`76a15fa3c`), the orchestrator's `pr.md` quote and the routing row's correction (`de6976b4e`), the crafter's fix (`f59c6f113`) and the two commits of close blocks (`f0d7f53c3`, `9389704ec`). `git diff --name-only 5590dddf0..9389704ec` names `frame/design.md`, `frame/plan.md`, `pr.md`, `trail/rounds/round-2.md` and `tests/skills/test_payload_meter.py` (executed). The round read those four records whole at `9389704ec`. `routing.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `trail/phases/phase-1.md` are unchanged in the range, so they are the text round 2 read whole at `5590dddf0`, and this round read none of their sentences against a changed tree. Both language keys name English, so no `pr.<lang>.md` is owed. `seal/parity.json` is not declared.

Carried from rounds 1 and 2 and not re-established: what `lib/core.py#rendered` returns past the cap (`lib/core.py:175`), the meter's `named` branch (`skills/verify/scripts/payload_meter.py:396-402`, `:526-532`), and the readings of `frame/questions.md` Q1.

## Findings

None.

## Confirmations

```seal
confirms: round-2#1
```
What holds: `f59c6f113` replaces the two phrase assertions at `tests/skills/test_payload_meter.py:436-439` with round 2's `note.endswith(...)` of the note's whole text, condition included, and keeps the absence assertion (read). The commit's message says the same. In this round's `git clone --no-local` at `9389704ec`, with "would reach `lib/core.py#CAP`" at `skills/verify/scripts/payload_meter.py:529` replaced by "stays under `lib/core.py#CAP`", `bin/test tests/skills/test_payload_meter.py -q -p no:xdist` fails `test_a_core_past_the_cap_is_a_hook_row_marked_as_naming_the_core` alone, 1 failed and 45 passed, and the meter restored passes (executed). That is the close's mutation row. The close's wider run, 938 passed over `tests/text` and `tests/behaviour`, was not run again (`## Not judged`). The close is right that `be5df7b9a`'s title stays as history.

```seal
confirms: round-2#2
```
What holds: `frame/design.md:93`, the third cell of the first `## Removes` row, now reads "Where the core is printed, the root they carried stands once, in the first line or in the closing line's sentence". That is round 2's text, and `lib/core.py:175` holds it (read). The fold also limits *Scope* item 1's bold title at `frame/design.md:42` to "under a printed core it names that root only where the first line does not". Past the cap, the closing line names the root and so does the `TOO_LONG` first line, so the limit is what the code does (read). The rest of item 1 opens each case with "Where the core printed is", so it already spoke of a printed core. The round-2 search, `grep -rn -i -e "root once" -e "stands once" -e "occurs once" -e "only place the root" -e "root only where"` over the work item outside `trail/`, run at `9389704ec`, prints `changelog.md:3`, `frame/plan.md:21`, `frame/questions.md:6` and `frame/design.md:29`, `:31`, `:42`, `:47`, `:67` and `:93` (executed). Each is limited to a printed core, goes on to what a longer root receives, speaks of `closing(<root>)` or a whole output, or is a probe dated to `7f388fa1f`, as round 2 read them. The search is a sample under contract rules 12 and 19.

```seal
confirms: round-2#3
```
What holds: `pr.md:5` quotes the grounds cell of `frame/plan.md:60` word for word, with its coordinate "the second row of 2026-11-27, its grounds" (read). In the clone at `9389704ec`, `bin/seal pr-body --body <scratch>/pr-body.md seal/threads/1795759278-the-cores-margin-depends-on-the-path` exits 0, and the body's first part carries the why and `perf:` as the kind that came closest (executed).

What matched: the orchestrator's routing row for round 2 at `frame/plan.md:62`. Its routes are what the commits did: finding 2 to the framer's fold `76a15fa3c`, finding 3 to the orchestrator's `de6976b4e` after it, and finding 1 to the crafter's `f59c6f113` after both (executed, `git log`). `de6976b4e` adds `skills/verify/scripts/payload_meter.py` to the files of finding 1, which round 2's `location:` names (read). The cited paragraph, `skills/implement/orchestration.md:83-101`, gives a round finding on a frame sentence to the framer, gives a statement in a file the crafter writes to a fix pass, and gives `pr.md` to the orchestrator, though only for a statement the framer's hand-back names. The row's grounds cell states the first two and not why `pr.md` is the orchestrator's. That reason stands in `skills/commit-pr-convention/SKILL.md:237`, "The orchestrator commits `pr.md` before the first round", so the route holds, and this round opens nothing on the omission. The row was written in the framer's fold commit `76a15fa3c`, as round 1's routing row was written in `24e3b8af8`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the suite is `unverified` at `9389704ec` beyond the three modules this round ran, and the round-2 close's run of `tests/text` and `tests/behaviour` was not repeated | the `Broad gate` key of `seal/config.json`; `seal/threads/1795759278-the-cores-margin-depends-on-the-path/trail/rounds/round-2.md:41` | the orchestrator's broad run, which comes due now that this round leaves no finding open, and the sealer's spawn after it |
| Carried from round 1: whether a fresh session takes the closing line's relative paths under the plugin's root (`frame/questions.md` Q1) | `seal/threads/1795759278-the-cores-margin-depends-on-the-path/gaps.md:7` | a measurement, run by the orchestrator or the repository owner |
| Carried from round 1: whether the closing line's paths keep `/` on Windows | `lib/core.py:85`, `seal/threads/1795759278-the-cores-margin-depends-on-the-path/gaps.md:8` | CI's Windows legs on the pull request |
| Carried from round 1: whether the harness counts the newline the hook writes after the output, at an output of 9,990 to 9,999 characters | `lib/core.py:52-56`, `hooks/core-start.py` | a measurement, run by the repository owner |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/lib/test_core.py tests/hooks/test_core_start.py tests/skills/test_payload_meter.py -q -p no:xdist`, in this worktree | 76 passed, exit 0 |
| `bin/test tests/skills/test_payload_meter.py -q -p no:xdist` in a `git clone --no-local` at `9389704ec` with "would reach" in the note at `payload_meter.py:529` replaced by "stays under", then restored with `git checkout` | 1 failed, `Test_measure::test_a_core_past_the_cap_is_a_hook_row_marked_as_naming_the_core`; 45 passed |
| `bin/seal pr-body --body <scratch>/pr-body.md seal/threads/1795759278-the-cores-margin-depends-on-the-path`, in the clone at `9389704ec` | exit 0; the first part holds both quotes of the prefix row |

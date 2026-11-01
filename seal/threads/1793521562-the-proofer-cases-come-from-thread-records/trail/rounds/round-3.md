# Review round 3: 1793521562-the-proofer-cases-come-from-thread-records

```seal
target: 7f0a08a959b75ec9231cbed9031d20771f286d5b, fixes 9245f625..7f0a08a9
```

This is a verifying round. Its target is the diff of round 2's fix pass, `9245f625..7f0a08a9`: the orchestrator's fold at `140727c5`, the test change at `f8174735`, and round 2's close blocks at `7f0a08a9`. The round answers round 2's two findings and reviews the units that diff added or changed. All work ran in a `git clone --no-local` of the branch worktree at the target, with `origin` set to the GitHub URL and the pull refs fetched for `seed_defects.py --list`. No `seal/parity.md` is declared, and the diff changes no path outside `docs/` and `seal/` that has an original to compare with, so the round block carries no `original:` line.

The base `release/v0.27.2` moved from `813665f0` to `ad5246ce` while this branch was open. The 13 files that `813665f0..ad5246ce` changes and the files `813665f0..7f0a08a9` changes have none in common (executed: `comm -12` of the two `git diff --name-only` lists, empty). So the move puts no new condition into the code this round reads.

Carried from rounds 1 and 2 and not searched again: the coordinates of the generator code (`evals/scripts/seed_defects.py#seed`, `#named`, `#target_at`, `evals/scripts/replay_targets.py#LOCATION`, `#truths_with`) and of its tests (`tests/evals/test_seed_defects.py`). Also carried are three rows left to the owner: Q1, Q2, and the replay scaffold's `origin`. The 351-line size of `seeded-bf9efcba` is carried from `frame/design.md` *Grounding*, the `--count` row, since `--list` no longer offers that commit. Re-established this round: every mutant round 2 and the fix pass named, the row each new parametrize row catches, the narrow modules, the test pairs, the 3051-line size of `seeded-7a8899d5`, and the two folded frame sentences against the tree. Every verdict below is this round's.

## Findings

No finding this round.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the 15-line margin and the path filter of the seed check are now pinned. The fix pass closed the finding `fixed f8174735`. It claimed nine mutants red, with the margin removed on either side and the path filter made `if False:` among them. I re-ran round 2's `evidence: executed` line as one batch of eight mutants of `evals/scripts/seed_defects.py` against `bin/test -q -p no:xdist tests/evals/test_seed_defects.py`. All eight went red, and none survived:

- the margin removed on both sides (`first <= line <= last`);
- the lower margin removed (`first <= line <= last + rt.WINDOW`);
- the upper margin removed (`first - rt.WINDOW <= line <= last`);
- the path filter `if m["path"] != path:` made `if False:`;
- the range end read as `int(m["line"])`;
- the unit span's `spans.append(span)` made `pass`;
- the bare path's append made `pass`;
- the `target_at` wiring at `evals/scripts/seed_defects.py:291` given `[]` in place of the truths' `location:` values.

The ninth claimed mutant, the whole check made `False`, is caught by any row of the first five and was not re-run.

A mutant can go red through a case other than the one meant to hold it. So I ran the first four mutants again against each new row alone, with `-k`. `line-within-the-window` (`a.py:55`) goes red on the margin removed and on the lower margin removed, and survives the other two. `range-ending-within-the-window` (`a.py:25-35`) goes red on the margin removed and on the upper margin removed, and survives the other two. `another-files-line` (`b.py:45`) goes red on the path filter alone (executed). That is the attribution the fix pass's close block claims, row for row.

The row values fit the source the case writes. `f` returns at line 2, `g` at 45 and `h` at 80. `a.py:55` keeps `g` off because `55 - 15 = 40` is below 45, and it leaves `h` free because `55 + 15 = 70` is below 80. `a.py:25-35` keeps `g` off because `35 + 15 = 50` is above 45. `b.py:45` names a file the target's diff does not change, so only the path filter keeps it from blocking `a.py:45` (read: `tests/evals/test_seed_defects.py:217-277`, `evals/scripts/seed_defects.py:156-223`).

```seal
confirms: round-2#2
```
What holds: the two stale frame sentences are rewritten in place. The close is `fixed 140727c5`, made by the orchestrator, and its `location:` names the two frame files, which `140727c5` changes (executed: `git diff 9245f625..7f0a08a9`). `frame/plan.md:5` now says the work keeps how each generator chooses its cases, changes where `seed_defects.py#seed` places a seed, and adds the `last` group to `replay_targets.py#LOCATION`. The tree agrees. `LOCATION` holds `(?P<last>\d+)` (`evals/scripts/replay_targets.py:157`). `truths_with` reads it at `:760-761`, and `seed_defects.py#named` reads it at `:215`, the helper the seed's span check takes its spans from (executed: `git grep`). `frame/questions.md:8` now cites A3 for how a generator chooses its cases and *Scope* item 5 for where a seed is placed. A3's row is about the selection rule (`frame/plan.md:21`).

I listed every sentence in the work item, outside its round records, that speaks of a generator changing or staying (executed: `git grep -i -E` over `seal/threads/1793521562-the-proofer-cases-come-from-thread-records`). That is a search on wordings, so it is a sample. It found `frame/plan.md:5`, `frame/questions.md:8`, `frame/design.md:37` (*Out*) and A3's row at `frame/plan.md:21`. A3's cost cell says the alternative "edits a generator its scope does not name", and its reason cell says "the generators as they stand". Both describe a change to the selection rule, which *Scope* still does not name. *Out* at `frame/design.md:37` puts the placement of a seed in scope by name. So no sentence left in the frame says the generators stay unchanged. I raise no finding on A3's row.

```seal
confirms: none
```
What matched: the new assertion against its group. At `f8174735`, the assertion of `test_keeps_the_seed_off_every_coordinate_a_truths_location_names` compares the seed's path, line and unit. It no longer compares the old and new text of the seeded line, which the five earlier rows compared. Two other cases of `Test_seed` compare the whole tuple, that text included: `test_accepts_the_first_operator_in_order_on_a_line_two_could_take` and `test_refuses_a_line_no_seed_may_take` (`tests/evals/test_seed_defects.py:165-214`, read). `seed()` builds the text the same way whether `locations` is empty or not, at `evals/scripts/seed_defects.py:195-197`. So the narrower assertion drops no coverage from the group. Folding the path filter's case into the parametrization, rather than adding the separate case round 2 proposed, avoids a second copy of the source. Each new row covers a branch no other case of the group covers, as the attribution above shows. `bin/seal layout --pairs` exited 0 and names no pair in `tests/evals/test_seed_defects.py` (executed).

```seal
confirms: none
```
What matched: the fix pass's claim that no generator changed, so the committed cases stand. `git diff --stat 9245f625..7f0a08a9 -- evals/` is empty (executed). `seed_defects.py --list` in the clone exited 0 and offers the four commits round 2 listed, at the same lines: `55b66958` at `skills/verify/scripts/unverified_check.py:1739`, `ea73e94f` at `skills/settle/scripts/settle.py:537`, `5fd6b88c` at `evals/scripts/replay_targets.py:210` and `7a8899d5` at `hooks/lib/blocks.py:451`. It leaves `bf9efcba` out with "no added line in a Python unit takes an operator" (executed). Round 2's `diff -r` of the regenerated cases against the committed ones was taken at `a6aa894c`, and neither the generators nor the cases changed since. This round carried that result and did not write the cases again.

```seal
confirms: none
```
What matched: the seeded cost the fold wrote into `frame/questions.md` Q2, which answers the cost half of round 2's second *Not judged* row. Q2 now says that the seeded half costs the same under (a) and (b). That holds, since (b) names replay rounds alone and keeps the four seeded cases. Q2 also says that `seeded-7a8899d5`'s diff is 3051 lines where `seeded-bf9efcba`'s was 351. `--list` prints `3051 lines` for `7a8899d5` (executed). The 351 is the *Grounding* row's (read: `frame/design.md:15`). Whether the suite should carry that case stays with the owner, under Q2.

```seal
confirms: none
```
What matched: the narrow modules, through the runner. `bin/test -q` over the seven modules round 2 named passed 272 cases, exit 0 (executed): `tests/evals/test_seed_defects.py`, `tests/evals/test_replay_targets.py`, `tests/evals/test_rule_cases.py`, `tests/behaviour/test_evals_layout.py`, `tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py`, `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` and `tests/test_censuses.py`. That is round 2's 269 plus the three new rows. The crafter's claim of 1424 passed over 29 modules is a different module set. It is round 2's 1421 plus three, and this round did not re-run it (read).

```seal
confirms: none
```
What matched: the fix pass's account of round 1's close. The crafter says that its round 1 close block, committed at `e821c734`, overstated "five units red", and that it cannot edit that block. Round 2's finding 1 records the overstatement, and round 2's close block repeats it. So the history is corrected where a reader of the chain looks for it. The round 1 record needs no edit (read: `trail/rounds/round-2.md`, finding 1 and its close).

```seal
confirms: none
```
What matched: the broad gate's label. `gaps.md` *Not verified* still labels the full suite, the repository-wide lint and the format check `unverified`, and names the orchestrator, by `seal gate` after the rounds settle. The fix pass ran one module set and no broad gate, so the label is honest. This round ran no broad gate. It leaves nothing open, so the orchestrator's broad run comes due next, and the sealer's spawn after it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the proofer, on the current release, reads a new case's earlier records and writes its record at the prompt's path. Only a paid run shows it, and the owner withheld paid runs for 0.27.2. This row is carried from rounds 1 and 2 | `frame/questions.md` Q1; `gaps.md` *Not verified* | the owner, at the first paid proofer run after 0.27.2 |
| Which rounds the suite measures, now with the seeded cost stated: `seeded-7a8899d5` reviews 3051 lines, where `seeded-bf9efcba` reviewed 351 | `frame/questions.md` Q2 | the owner |
| Whether a replay scaffold that keeps `origin` lets the proofer fetch the later rounds of the record it replays. Carried from rounds 1 and 2, which carried it from `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/rounds/round-1.md:231`, and not judged again | `evals/behaviour/proofer/replay-*/scaffold.sh` | the owner |
| The full suite, the repository-wide lint and the format check at the target | the tree at `7f0a08a9` | the orchestrator, by `seal gate` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/seal mutate evals/scripts/seed_defects.py --timeout 300` with the eight `--replace` pairs of the first confirmation, `--tests "bin/test -q -p no:xdist tests/evals/test_seed_defects.py"` | baseline passes; 8 mutants, 8 red, 0 SURVIVED; `git status --short` empty afterwards |
| the same `bin/seal mutate` with the first four pairs, run three times, `--tests` narrowed with `-k line-within-the-window`, `-k range-ending-within-the-window` and `-k another-files-line` | red on mutants 1 and 2, on 1 and 3, and on 4 alone, in that order; the rest SURVIVED |
| `bin/test -q` over the seven modules named in the sixth confirmation | 272 passed, exit 0 |
| `bin/seal layout --pairs` | exit 0; no pair in `tests/evals/test_seed_defects.py` |
| `python3 evals/scripts/seed_defects.py --list`, with the pull refs fetched | exit 0; four commits offered at the lines round 2 listed, `7a8899d5` at 3051 lines, `bf9efcba` left out |
| `comm -12` of `git diff --name-only 813665f0 ad5246ce` and `git diff --name-only 813665f0 7f0a08a9`, each sorted | empty |

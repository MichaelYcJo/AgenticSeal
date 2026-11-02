# Review round 4: 1793599985-a-mutant-that-does-not-compile-reads-as-caught

```seal
target: cecdddef, fixes 4a9ab347..cecdddef
```

This is a verifying round. Its target is the diff `4a9ab347..cecdddef`, which holds three commits. `a34ccfc7` adds round 3's record and edits `handoff.md`. `b8d7462d` deletes `handoff.md`. Both touch only the work item's records. `cecdddef` replaces `.test_durations`, the one path the diff changes outside `seal/`, and it is this round's subject. The base is `release/v0.29.0`, at `40e6c23e`. The work happened in a `git clone --no-local` of the branch worktree at `cecdddef`, under `<scratchpad>/898-round-4/clone`. No `seal/parity.md` is declared, so the round block has no `original:` line.

Round 3 closed no finding, so this round owes no `confirms:` line to an earlier finding. Carried from round 3 without re-running: the verdicts on `skills/verify/scripts/mutation_check.py` and `tests/skills/test_mutation_check.py`, which no commit of this diff touches (`git diff --name-status b8d7462d cecdddef` lists `.test_durations` alone, and `a34ccfc7` and `b8d7462d` list only paths under the work item's directory, executed). Re-derived this round: what the new file is, that it parses, that it prices the suite collected at `cecdddef`, and every verdict below.

The orchestrator's account was read as claims. It claimed the broad run at `b8d7462d` failed on `test_the_durations_file_prices_the_suite` with 327 of 6354 cases unpriced. This round did not re-run the old file, but CI run 41407725325 failed that case and no other on its three red legs, and its ubuntu leg collected 6354 cases (1 failed, 6341 passed, 12 skipped; executed, `## Probes` row 1). It claimed the file is the `test-durations` artifact of that run. The commit message says that run was "at a34ccfc7"; `gh run view` gives its head commit as `b8d7462d`. The two trees differ only by `handoff.md`, and the collection at `cecdddef` matches the file's keys exactly (below), so the misnamed commit changes nothing the file holds. The squash replaces the commit message, so this is no finding.

## Findings

None. `cecdddef` touches one file, the file is byte for byte the artifact the case's sentence names, and it prices every case the suite collects at `cecdddef` with no entry left over.

## Confirmations

```seal
confirms: none
```
What holds: `.test_durations` at `cecdddef` is the `test-durations` artifact of run 41407725325. That run is the `tests` workflow, dispatched on this branch at `b8d7462d`, and its `durations` job succeeded (executed, `## Probes` row 1). This round downloaded the artifact by the command `REMEDY` names, `gh run download <run id> -n test-durations -D <dir>` (`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:271-281`), into a directory of its own. `cmp` against the committed file exits 0, and the SHA-256 of the artifact, of the clone's working file and of `git show cecdddef:.test_durations` agree (executed, `## Probes` row 2). The artifact is the union the `durations` job writes through `.github/scripts/durations_union.py --count 4` from the four Windows shards' parts (`.github/workflows/test.yml:206-212`, read). The Windows group 1 shard was red on the durations case, and its part still reached the union: the upload step runs under `always()` (`test.yml`, held by `test_the_upload_step_runs_always_and_only_where_store_is_set`), and the union prices all 6354 cases.

```seal
confirms: none
```
What holds: the file parses as one JSON object of 6354 keys. Every key opens with `tests/` and holds `::`, and every value is a number of at least 0, the shape `test_the_durations_file_parses_and_names_cases` asserts (executed, `## Probes` row 3). Its seconds sum to 1616.7. It holds no carriage return. Like the file it replaces, it ends at `}` with no final newline, so no line-ending or end-of-file rule meets a change. The 98 lines that hold `\\` are JSON escapes inside parametrised ids, such as `\\n` and `\\uc635`, and the old file at `b8d7462d` holds the same count, 98. None of them is a Windows path separator (read).

```seal
confirms: none
```
What holds: the file prices exactly the suite collected at `cecdddef`. `bin/test tests --collect-only -q -p no:xdist` in the clone collected 6354 unique ids. Set against the file's keys, 0 are unpriced and 0 keys are gone (executed, `## Probes` row 4). So both sides of `STALE_SHARE` stand at 0 %. The three cases that read the whole collection against the file, `test_the_durations_file_prices_the_suite`, `test_the_durations_file_parses_and_names_cases` and `test_no_collected_id_carries_the_interpreters_path`, ran over the whole collection and passed, 3 passed and 6351 deselected (executed, `## Probes` row 5). This agrees with the orchestrator's single-case run and adds the exact set the share rests on.

```seal
confirms: none
```
What holds: `cecdddef` changes nothing else. `git diff --name-status b8d7462d cecdddef` lists `M .test_durations` alone, and the file's mode stays `100644` (executed, `## Probes` row 6). The commit carries the `Seal-Routing:` trailer naming this work item and the author `zenith.m.jo@gmail.com` (read, `git show --format`). Before this commit the branch left `.test_durations` as the base had it: `git diff --stat origin/release/v0.29.0 4a9ab347 -- .test_durations` prints nothing (executed). The file was stale on the base, and the case's own docstring makes a refresh in the branch that meets the failure the whole schedule of its refresh (`test_the_windows_leg_runs_in_shards_that_make_the_whole.py:37-46`, read). No document of the work item names `.test_durations` beyond `trail/phases/phase-2.md:11`, a note about timings that begin with `0.28` (read), so the commit owes no frame or changelog line.

The same CI run bears on round 3's third `## Not judged` row, the new mutation cases on `windows-latest` under 3.12. Its four Windows shards failed only the durations case, on group 1, and passed every other case (executed, `## Probes` row 1). That run was a dispatch on `b8d7462d`, not the pull request's run, and the row stays the orchestrator's. Since `cecdddef` does not touch the mutation code, the evidence carries to the head.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `cecdddef`. `gaps.md` labels the broad run `unverified` and names the orchestrator, which is honest. This round leaves nothing open, so what comes due is the orchestrator's broad run, and the sealer's spawn after it. | `seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught/gaps.md` | the orchestrator's broad run, `seal gate --base release/v0.29.0 --record` this work item |
| Whether the shards stay balanced under the new prices. That is a property of each leg's `--durations=50` table and `timeout`, not of the file's age (`test_the_windows_leg_runs_in_shards_that_make_the_whole.py:87-89`). | `.github/workflows/test.yml` | the orchestrator, reading the pull request's CI run |
| Whether the five commits without a `Seal-Routing:` trailer are rewritten before the pull request, or left for the squash to replace (carried from rounds 1 to 3). | `skills/commit-pr-convention/SKILL.md:185-187` | the orchestrator |
| The pull request body's statements that `CONTRIBUTING.md` *What a change to a gate must carry* asks for. No body exists at this round (carried from rounds 1 to 3). | `CONTRIBUTING.md` | the sealer, reading `seal pr-body`'s file |

## Probes

| Command | Result |
|---|---|
| `gh run view 41407725325 --json headSha,headBranch,event,conclusion,jobs`, then `gh run view 41407725325 --log-failed`, filtered to the `FAILED` and total lines | `workflow_dispatch` on this branch, head `b8d7462d`, conclusion `failure`; `durations` succeeded. Red legs: ubuntu (1 failed, 6341 passed, 12 skipped), macOS group 1 (1 failed, 3569 passed, 12 skipped), Windows group 1 (1 failed, 3069 passed, 15 skipped). Each failure was `test_the_durations_file_prices_the_suite`. The other three Windows shards and two macOS shards succeeded |
| `gh run download 41407725325 -n test-durations -D <scratchpad>/898-round-4/artifact`, then `cmp` and `shasum -a 256` against the clone's `.test_durations` and `git show cecdddef:.test_durations` | download exit 0; `cmp` exit 0; all three `12bae177cb52e43dcce21cb32595b644277710aecbdb8e52c07096b8363d369c` |
| `python3 -I -c` loading the clone's `.test_durations` with `json.load` and applying the shape `test_the_durations_file_parses_and_names_cases` asserts; `grep -c` for a carriage return | `dict`, 6354 keys, 0 bad, sum 1616.7; 0 carriage returns |
| `bin/test tests --collect-only -q -p no:xdist` in the clone at `cecdddef`, its ids set against the file's keys with `python3 -I -c` | `6354 tests collected`, exit 0; 6354 unique ids, 0 unpriced, 0 gone |
| `bin/test tests -q -p no:xdist -rs -k "test_the_durations_file_prices_the_suite or test_the_durations_file_parses_and_names_cases or test_no_collected_id_carries_the_interpreters_path"` in the clone | `3 passed, 6351 deselected`, exit 0 |
| `git diff --name-status b8d7462d cecdddef`, `git ls-tree` of `.test_durations` at `b8d7462d` and `cecdddef`, and `git diff --stat origin/release/v0.29.0 4a9ab347 -- .test_durations` | `M .test_durations` alone; mode `100644` at both; the base diff prints nothing |

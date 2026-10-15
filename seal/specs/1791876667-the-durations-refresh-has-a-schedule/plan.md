# Implementation Plan: the durations refresh has a schedule

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-14 by the repository owner, when `smith` was spawned.

## Summary

The file is measured on every run by the shards that already run every case, a job after them unions the parts and writes the reading to the summary, and the one check that already holds the file's age becomes the whole schedule: past a twentieth unpriced, or past a twentieth of the seconds dead, the case fails and names a download. The 35-minute measuring run, the measuring commit, the dispatch and the checklist box leave. Phase 1 proves it on the Windows leg with the division read before and after; phase 2 turns the check and the words; phase 3 writes the records.

## Technical context

Read at a04ba95b (= `main` a8d83663 plus the routing commit), 2026-10-13.

- `.github/workflows/test.yml` — the matrix (`include:` the only key; four Windows and three macOS shard entries; `timeout` per leg), the pytest line `pytest tests/ -q -n auto --durations=50 ${{ matrix.split }}`, `workflow_dispatch:` kept for a pushed branch with no pull request (#841). The measuring shape #874 used on one commit (`store:` key, `${{ matrix.store }}`, the upload step with its two-part `if`) is the shape this work makes permanent on the four shard entries.
- `tests/test_ci_gives_the_checks_what_they_need.py#matrix_include_entries` — the one reading of the entries; a new key on an entry is read as a string, no change needed. `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#test_the_pytest_line_hands_the_split_to_pytest` pins the line's end at `${{ matrix.split }}` and is rewritten. `test_every_group_of_each_sharded_leg_runs_exactly_once` holds as it is.
- `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#staleness`, `#unpriced`, `#collects_the_suite`, `STALE_SHARE = 0.05`; `tests/conftest.py#pytest_collection_modifyitems` records the whole collection before `pytest-split`'s `trylast` hook (0.21.1 S3, `executed` by #874 on GitHub). The seconds side reads the same `collected` and `durations`.
- `pytest_split/plugin.py#PytestSplitCachePlugin.pytest_sessionfinish` (0.11.0, `read` from the wheel): sums every `TestReport`'s duration per node id — setup and teardown included under a threshold, so a skipped case gets an entry — and with `--clean-durations` writes exactly that session's map. On a shard the session is the group, so a part is the group and nothing else; `-n auto` changes nothing, the controller's reporter holds every worker's reports (#841 phase 3 stored the first file this way).
- `.github/scripts/issue_claims_check.py`, `release_completeness_check.py` — the shape of a script here: the floor line (`tests/test_a_script_says_which_interpreter_it_needs.py`), a `Reads:` line per unit (`docs/the-reader-registry.md`), `$GITHUB_STEP_SUMMARY` when set.
- #930's frame (`read` at 826b7ec8 on its branch): `suite-seconds` 7,862 s at 5 % and `slow-file:<path>` at 10 % are read from the committed file, gated, and its alternative F left the cadence here. Phase 1's union commit is the first time either row moves: 460 cases at the mean are about 268 s, inside the 8,255 s band, unless one of them is heavy — then the pull request body carries `Budget raised: suite-seconds 7862 -> <n>: the 0.21.1 cycle's 460 cases, measured`, and that is the ratchet doing its job. If #930 has not landed when a phase runs, nothing is owed: its build re-measures every starting value at its own SHA, and its `budgets` job and this `durations` job are two jobs that both `needs: pytest` (`questions.md` Q4).
- #929 (`read` from the issue; its frame is being drawn in parallel): it lowers the numbers and not this mechanism. Its cut pull requests remove seconds the committed file still sums, so without a fresh file `suite-seconds` would not fall and the ratchet would keep headroom nobody meant to leave. The seconds side of the check is what makes a cut above a twentieth bring the file; a smaller cut waits for the next refresh. Phase 1 therefore lands first (`questions.md` Q5).

**The measurements, with their commands** (`executed` 2026-10-13 at a04ba95b; `read` where said).

- Unpriced share: `bin/test tests --collect-only -q` (13,914 collected in 6.05 s) against the committed file by a scratch script: 460 unpriced (3.31 %), 28 dead worth 0.9 s of 7,861.7 s. Unpriced by file: `test_one_table_walker_reads_what_gfm_renders.py` 228, `test_whether_a_line_is_live_is_asked_by_what_the_line_does.py` 72, `test_the_mode_question_is_asked_once.py` 64.
- Slope: `git log --format=%s <tag>..<tag> | grep -c '(#N)$'` gives 9, 16 and 10 pull requests for 0.20.0, 0.21.0 and 0.21.1; cases 12,819 → 13,474 → 13,914 (`read` from #874's issue and frame for the first two). 41 and 44 cases per pull request; `def test_` counts at the tags 5,127 → 5,442 → 5,503 agree in shape. At 44 per pull request the 5 % line (695) is 16 pull requests after a refresh, and today's 235 of headroom is about 5.
- Spread: `gh api repos/<r>/actions/runs/<id>/jobs` over the 16 successful `pull_request` runs of 2026-10-13, slowest shard over fastest by job wall-clock: Windows median 1.35, max 1.80; macOS 1.28, max 2.19; runs on the refreshed file (38346828074 … 38353159958) span 1.02–1.62 on Windows. Against 1.05 and 1.03 by pytest seconds in run 38335775781 (`read`, 0.21.1 S5). Runner-minutes per run, median: Windows 42.8, macOS 19.8, ubuntu 9.7.
- One refresh: Windows unsharded job 2,241 s (run 38332345615), 2,055 s (38342987499), cancelled at 1,361 s (38357196840, the 0.21.1 skip); the whole run 3,719 runner-seconds; artifact 299,589 bytes; `git rev-list --objects -- .test_durations | git cat-file --batch-check`: 3 blobs, 0.99 MB packed, in an 83 MB pack.

**What breaks in six months with the chosen approach.** The four parts are priced on four runners whose speed differs — the wall-clock spread above is mostly that — so a shard-measured file can carry a per-part skew an unsharded one did not, and the next division inherits it. Phase 1 reads the per-part median ratio against the unsharded file and the spread after the first union commit; if the skew is inside the run-to-run noise (1.2×, #930's reading over 12 runs), nothing is built, and if it is not, the union scales each part to the mean ratio (Q1) — one function, read on the same line of the summary from then on. Second: the summary is a report, and a report nobody opens is #908's table; what gates is the check, and the spread line exists so that a skew is a number on the run that caused it. Third: a part is missing because a shard was killed at its `timeout`; the union exits 2, the pytest job is already red, and no smaller file is ever uploaded as the whole.

## Alternatives considered

Prices are #929's mid-2026 list ($0.008 Linux, 2× Windows, 10× macOS), unverified; nobody opened the page for this frame (`questions.md` Q3). Minutes are `executed` above.

| Approach | Failure scenario (six months on) | CI cost if private | Verdict |
|---|---|---|---|
| A. Every release, the box as written: an unsharded measuring run a person dispatches | Skipped under time pressure, as 0.21.1 did on the box's first use; the box is a prompt; 35–40 minutes of wait per release, and this repository released twice on one day | 274 Linux-equivalent minutes ≈ $2.19 per release; no induced imbalance | rejected |
| B. Past the threshold only, unsharded: drop the box, keep the check | Zero prompts, but the red lands on an unrelated pull request whose session pays the measuring commit, a 35-minute run and the restore; `suite-seconds` moves only then; a cleanup is invisible to the ratchet until the next growth crosses the line | $2.19 per ~16 pull requests | rejected |
| C. On a schedule: a cron workflow measures weekly and opens a pull request with the file | Needs `contents: write` and `pull-requests: write`, which #359 took away; it measures `main` while the work sits on `release/*`; the bot's pull request waits for a person to merge it, which is the box with a timer | $2.19 per week | rejected |
| D. A `workflow_dispatch` input that runs the measuring leg without a commit (#914's body) | One command, still a person's; A's failure with a cheaper step | $2.19 per use | rejected; #914 closes with this |
| E. **The shards store on every run, a job unions the parts, the check schedules the download** | above | 4 uploads and one ubuntu job, about a minute ≈ $0.01 per run, $0.3–0.6 per day at #929's 40 runs; artifacts ≈ 1.5 MB zipped per run at 1–7 days' retention, cents per month | **chosen** |
| F. E, and the union is committed on every run by the job | The write scope of C; 330 KB of packed history per pull request, 13 MB a day; the thing the milestone is against | as E | rejected |
| G. E without the job: the contributor downloads four parts and unions locally | No per-run reading of the shards' seconds, which is the one measurement of balance nobody takes today; a local script per refresh | 4 uploads only | rejected |
| H. Measure on ubuntu, which runs the suite whole on every pull request | The file is Windows' by #864 D and #874: a spawn costs 7 ms there and 60 ms on Windows, and the ratio differs per case; a measured correlation could overturn it and none exists | nothing new | rejected |
| I. The check keeps one direction (unpriced only) | A cut leaves the committed sum high; the headroom hides the next cycle's growth until the file is refreshed for another reason — the owner's *cleaning up once is not enough* | — | rejected; the seconds side at the same share |
| J. `STALE_SHARE` becomes a `seal/budgets.md` row | The two-sided ratchet cannot hold a sawtooth: after every refresh the measurement is 0 and the lower band would force the ceiling to 0. It stays a constant in the module with one reader, a raise is a reviewed line with its grounds in the comment, and the live numbers go to the summary as a report | — | rejected; sits beside |
| K. Fold into #930 or #929 | #930's rows read the committed file and its frame left the cadence here; #929 changes the numbers, and folding puts a workflow mechanism in a pull request that cuts tests. Order matters instead: this lands first | — | not folded |

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **Every run measures, and the Windows leg is read before and after.** `test.yml`: `store:` on the four Windows entries, `${{ matrix.store }}` after the split on the pytest line, the upload step (`if: always() && matrix.store != ''`, `include-hidden-files: true`, `retention-days: 1`, name `test-durations-${{ strategy.job-index }}`), the `durations` job (`needs: pytest`, `if: ${{ !cancelled() }}`, download by pattern, the script, upload `test-durations` at 7 days). `.github/scripts/durations_union.py` with its summary lines and exit codes. Cases T1–T6, T10, each seen red. The hand-back names the push; the session pushes and runs the workflow (`gh workflow run test.yml --ref <branch>` or the pull request's run). **Then, from that run:** download the four parts and the union; read each shard's measured seconds and the spread (the *before*, under the committed file), the per-part median ratio against the committed file, unpriced and dead by the union against the pytest case's 460 and 28; commit the union as `.test_durations` (LF; `bin/test tests -q -k test_the_durations_file_prices_the_suite` green; if #930 landed, `budget_check.py` on the tree, and the `Budget raised:` line in the body where a row crossed). The hand-back names the second push | locally, exit read directly: `bin/test tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/test_ci_gives_the_checks_what_they_need.py tests/test_a_slow_case_names_itself.py tests/test_a_workflow_is_read_the_one_way.py tests/test_a_reader_declares_its_input_class.py tests/test_a_script_says_which_interpreter_it_needs.py -q`; on the run: four parts, one union, the summary; `phases/phase-1.md` carries every number | 316b9a36 |
| 2 | **The check is the schedule, and the words say so.** From the run after the union commit: each shard's seconds and spread (the *after*), beside the before; Q1 decided from the ratio line. `staleness` gains the seconds side under `STALE_SHARE`; the sentence names the download; fixture cases at the seconds boundary; `test_an_entry_nobody_collects_is_not_counted` says what the entry counts toward; T7–T9, T11, each seen red. `CONTRIBUTING.md`'s recipe paragraph rewritten in place; `docs/release-checklist.md` §0's box removed; `test.yml` comments re-read. The pull request body's gate lines: the test seen red, *blocks more*, prompt budget zero, platform honesty | locally: the modules of phase 1 plus `tests/test_docs_line_wrap.py`, `tests/test_the_contributor_has_a_procedure.py`, `tests/test_release_hygiene.py`; `bin/test tests -q -k test_the_durations_file_prices_the_suite` green; each new case red by the mutation its row names (`bin/mutation-check` or the line deleted); `phases/phase-2.md` | faf233ea |
| 3 | **The records.** `changelog.md`: one `### Changed` entry with the numbers of phases 1 and 2. `overview.md` closed, `## Not verified` naming the sealer for the suite and the pull request's run for GitHub reading the workflow | the four `## Removes` rows read gone from the tree; `python3 skills/verify/scripts/unverified_check.py --baseline origin/release/v0.22.0` exit 0 | bea1f794 |

This table is also where the work records how far it got. **Status is empty, or the commit that closed the phase.** Re-read the column after any rebase.

### Test rows — the mutation each case kills

| Case | Guards | Mutation it kills |
|---|---|---|
| T1 `test_the_windows_entries_store_and_the_other_entries_do_not` | S1 | a macOS entry gains `store`, or a Windows entry loses it, in a fixture matrix |
| T2 `test_the_pytest_line_hands_the_split_to_pytest`, its body rewritten (built under the released name, `overview.md`) | S1 | the line ends at `${{ matrix.split }}`, or the store expression precedes the split |
| T3 `test_the_upload_step_runs_always_and_only_where_store_is_set` | S1 | `always()` dropped (a red shard uploads nothing), `matrix.store != ''` dropped (ubuntu uploads the committed file), `include-hidden-files` dropped |
| T4 `test_the_union_of_the_parts_is_the_whole_sorted_with_lf` | S2 | a part skipped; keys unsorted; CRLF written |
| T5 `test_a_missing_part_a_duplicate_id_or_an_unparseable_part_is_exit_2` | S2 | fewer parts than `--count` read as complete; a duplicate id overwritten; a bad part skipped with exit 0 |
| T6 `test_the_summary_names_each_parts_seconds_the_spread_and_the_live_sum` | S3 | the spread as slowest over fastest instead of over the mean; the committed sum not read; a machine path in a line |
| T7 `test_dead_seconds_past_the_share_fail_and_at_the_share_pass` | S4 | the seconds side dropped or inverted; fixture at exactly one twentieth of the seconds, and one entry more |
| T8 `test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe`, its body rewritten (built under the released name, `overview.md`) | S4 | the remedy names the old recipe; the artifact name missing |
| T9 `test_an_entry_nobody_collects_is_not_counted` (kept, reworded) | S4 | a dead entry counted toward the unpriced share |
| T10 `test_the_durations_job_needs_pytest_and_runs_unless_cancelled` | S2 | `needs:` dropped; `if:` dropped or `success()` |
| T11 `test_the_recipe_names_the_artifact_and_the_checklist_has_no_box` | S6 | the box re-added; `test-durations` or `gh run download` absent from the paragraph |

## Operational impact

- `test.yml` gains one step per Windows shard and one job; no new scope: downloading an artifact of the same run needs nothing beyond the default token. One more green job on every pull request, under a minute.
- `.test_durations` is committed once by phase 1 (about 330 KB packed) and afterwards only when the check asks, which at today's slope is about once a release cycle, or in a pull request that cuts a twentieth of the suite's time.
- A contributor who meets the red runs one `gh run download`, one `budget_check.py --restate-price` and one commit; no measuring commit, no dispatch, no restore. The run's artifacts outlive the pull request by 7 days; past that, `gh run rerun`.
- A fresh file can move `suite-seconds` past its ceiling, and the pull request that brings it carries the `Budget raised:` line with the growth named — or lowers the ceiling, where a cut brought it. The `slow-file:*` rows are `report` rows: one union moves a single file 0.67 to 1.72 times the level from the next, so they print and fail nothing.
- No new dependency; the script is stdlib at the floor; `pytest-split` is already pinned on the pip line.

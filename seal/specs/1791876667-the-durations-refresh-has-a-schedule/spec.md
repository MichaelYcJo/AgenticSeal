# Feature Specification: the durations refresh has a schedule

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | Nothing here asks a person. The checklist box leaves, the measuring run leaves, and the one check that schedules the refresh prints the command that performs it |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The staleness case changes what it refuses and what it says: a test seen red, the direction (it blocks more), a prompt budget of zero, platform honesty (the parts are Windows', the union runs on ubuntu), a `Reads:` line per unit, and `## Removes` below |
| `CONTRIBUTING.md` §*Running the checks*, the paragraph beginning *`.test_durations` goes stale as cases are added* | The recipe this work rewrites in place: the measuring shape, the 60-minute leg, the dispatch, the download-and-restore and the post-refresh `timeout` re-read all go; what stays is one sentence per fact of the new shape |
| `docs/release-checklist.md` §*0. Before starting* | The refresh box leaves; a box a person ticks is a prompt, and 0.21.1 skipped it on its first use |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below lists what the work takes out, and the review reads it against the diff |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | The release note is this item's `changelog.md` fragment, not an edit to the shared changelog |
| `docs/measuring-a-run.md` §*Where a reading goes* | A measurement nobody posted is one nobody has: every run writes the shards' measured seconds, the spread and the live suite seconds to its job summary |
| `skills/agent-contract/SKILL.md` §6 | The smith pushes nothing; the session pushes and runs the workflow, and the smith hands back at each push, as #874's plan placed it |
| `skills/implement/SKILL.md` §*3. The SDD file set* | A check's verdict and the sentence a contributor acts on change, which is the top rung |

## Scope

**What the frame measured** (`executed` 2026-10-13 at a04ba95b unless labelled; the commands are in `plan.md` §*Technical context*). The suite collects 13,914 cases; `.test_durations` holds 13,482 entries summing 7,861.7 s (mean 0.583 s). **460 collected cases (3.31 %) are unpriced** and 28 entries are dead, worth 0.9 s. The 5 % line is 695 cases, 235 away. The suite grew 655 cases over the 16 pull requests of 0.21.0 and 440 over the 10 of 0.21.1 (`read` for the first two counts from #874's issue and frame; collected here for the third): **about 44 cases per pull request, so the line is about 16 pull requests, one release cycle, from a refresh.** One unsharded refresh costs a 34–37 minute Windows job (2,055 s and 2,241 s in runs 38342987499 and 38332345615; the cancelled one ran 1,361 s) inside a 62-runner-minute run, and the committed file costs about 330 KB of packed history per refresh (3 blobs, 0.99 MB). The shards' spread by job wall-clock over 16 pull-request runs on 2026-10-13 is Windows median 1.35 (max 1.80) and macOS 1.28 (max 2.19) — with a fresh file as with a stale one — against 1.05 and 1.03 by pytest's own seconds in run 38335775781. **The file's age at 3 % is invisible under runner noise; what a refresh buys is the 1.05, and nothing on a pull request reads it today.**

**In.**

1. **Every run measures the file, on the shards, for nothing.** The four Windows shard entries of `test.yml` carry `store: "--store-durations --clean-durations"`, the pytest line hands it to pytest after the split, and each shard uploads the part it wrote (`if: always() && matrix.store != ''`, `include-hidden-files: true`, a short retention). With `--clean-durations` a shard writes exactly the reports of its own session (`pytest_split/plugin.py#PytestSplitCachePlugin.pytest_sessionfinish`, `read` 2026-10-13 from the 0.11.0 wheel), so the four parts union to the whole suite — #914's first way, made permanent.
2. **A `durations` job unions the parts and reports.** `needs: pytest`, `if: ${{ !cancelled() }}`, ubuntu. It runs `.github/scripts/durations_union.py` over the parts: the union, sorted, LF, uploaded as `test-durations`; and the job summary carries one line per fact — entries, the live sum of seconds beside the committed file's, unpriced and dead by the union, each shard's measured seconds and the slowest-to-mean spread, and each part's median price ratio against the committed file. A missing part, an id in two parts or a part that will not parse is exit 2, never a smaller file.
3. **The check is the schedule, in both directions.** `test_the_durations_file_prices_the_suite` fails when more than `STALE_SHARE` of the collected cases are unpriced — as now — **or when more than `STALE_SHARE` of the committed file's seconds belong to entries the suite no longer collects.** The first bounds growth the ratchet has not seen; the second bounds a cleanup it has not recorded, so a pull request that removes a twentieth of the suite's time brings the fresh file and #930's `suite-seconds` falls in the same pull request. Its message names the counts and the remedy: download `test-durations` from this branch's latest `tests` run (`gh run download <id> -n test-durations`), move it over the committed file, write the price level it implies with `python3 .github/scripts/budget_check.py --baseline origin/<base> --restate-price`, where `<base>` is the branch the pull request merges into, and commit both. The message gives the command as it runs: round 4 found it without `--baseline`, which the checker refuses with exit 2, held in place by the case that asserted the short form. One constant, one case, fixture cases at both boundaries.
4. **The words, rewritten in place.** `CONTRIBUTING.md`'s recipe paragraph states the new shape and nothing of the old one. `docs/release-checklist.md` §0 loses the box. `test.yml`'s comments stay true as written.
5. **The proof, on one leg.** Phase 1 commits the first union once, so the Windows leg's division is read before and after on the same mechanism: each shard's measured seconds and spread under the committed, unsharded-measured file, then under the shard-measured one. The commit is the experiment that answers the design's one open risk (`plan.md` §*Technical context*).
6. **The records.** `phases/phase-N.md` with the figures; `changelog.md`; `overview.md` closed.
7. **The level has one expression, and #930's records say what the family is** (the reframe after round 4). `budget_check.py` computes the level a refresh implies in one function, `expected_level`, which `price_problems` and `--restate-price` both read; round 4 found the expression written twice, so an edit to one copy would make the writer write a level the check refuses. And `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md`'s `slow-file` row and its `questions.md`'s gate-or-report judgment say `report`, rewritten in place and not annotated: that spec is what `settle` folds into `docs/` at the release, and the fact it would fold is the one this item changed in round 3.

**Out, and whose.**

- **The suite's cuts, the heavy fixtures, which legs run** — #929. Its cut pull requests download `test-durations` from their own run (`questions.md` Q5), which is why phase 1 lands before them.
- **`seal/budgets.md`, `budget_check.py`, the ratchet** — #930. `suite-seconds` and `slow-file:*` are read from the committed file and move only when it is refreshed; this item decides when that is. Its union is also what moves a single test file 0.67 to 1.72 times the level from one refresh to the next (round 3), past the 1.3 band, so this item makes the `slow-file` family a `report` row in `seal/budgets.md`; its rows still print in every summary and the release still lowers them from the trend. `suite-seconds` stays the gate, and a fresh file that crosses its ceiling owes #930's `Budget raised:` line, which is the ratchet working. The `## Price level` a refresh moves is written by `budget_check.py --restate-price` (round 3), from the number the checker would otherwise fail naming.
- **A macOS-measured part, or a macOS union for the spread line.** The file is Windows' (#864 D, #874); three more uploads for a report line nobody gates is scope the `ci-minutes:macos` row and the job times already cover.
- **Committing the file on every run, or by a bot.** A write scope #359 removed, and 330 KB of history per pull request.
- **A `workflow_dispatch` input for an unsharded measuring run (#914's body).** The shape it would have run is gone; the orchestrator may close #914 with this.
- **Normalising the parts by runner speed.** Built only if phase 1's per-part ratio exceeds the run-to-run noise (`questions.md` Q1).
- **Lowering or raising `STALE_SHARE`.** #874's Q1 set it; the grounds that remain are above, and the value is one line a reviewed commit moves.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 every Windows shard uploads its part | any `tests` run; when its four Windows jobs end, green or red; then four `test-durations-*` artifacts exist, each a JSON object of that shard's cases only | `executed`: `gh api …/runs/<id>/artifacts` on the branch's run; the cases T1–T3 pin the entries, the line and the step |
| S2 the union is the suite | given four parts; when `durations_union.py` runs; then one sorted LF file whose keys are the suite's collection, uploaded as `test-durations`; a missing part, a duplicate id or an unparseable part is exit 2 | `executed`: the artifact downloaded, `bin/test tests -q -k test_the_durations_file_prices_the_suite` against it reads 0 unpriced; T4–T5 |
| S3 the summary on every run | any run; then the `durations` job's summary carries entries, live seconds beside committed, unpriced and dead by the union, each shard's seconds and spread, each part's median ratio | `executed` on the branch's run; T6 pins the lines from fixture parts |
| S4 the check fails in both directions and names the remedy | more than `STALE_SHARE` of collected cases unpriced, or more than `STALE_SHARE` of the file's seconds dead; then the case fails naming the counts, the share, the download and the restate command with its `--baseline origin/<base>`; at the share it passes | `executed`: each fixture case red with its comparison inverted or the seconds side dropped; T7–T9; the restate command typed as the message gives it is not refused for a missing `--baseline` |
| S9 one expression, one record | `price_problems` and the restate branch of `check` read the level from `expected_level`; 1791876665's `spec.md` and `questions.md` call the `slow-file` family `report` | `read`: `git grep -n 'seconds(base_level' .github/scripts/budget_check.py` is one line, inside `expected_level`; neither record names `slow-file` among the gates; `executed`: `bin/test tests/test_a_budget_ratchets.py -q` green |
| S5 the remedy works and the leg divides as well | the committed union; then the case is green on every leg and the next run's Windows spread by measured seconds is within the band of the unsharded file's (1.05) plus noise | `executed`: phase 1's before and after in `phases/phase-1.md` |
| S6 the sentences and the box | a contributor reads `CONTRIBUTING.md` §*Running the checks* and `docs/release-checklist.md` §0; then the first describes the shards' parts, the `durations` job and the download, and the second has no refresh box | `read`; T11 pins both; `bin/test tests/test_docs_line_wrap.py` green |
| S7 nothing asks a person | the whole change; then no box, no dispatch, no measuring commit, no `AskUserQuestion`; the check prints the command | `read` over the diff; the prompt budget line in the pull request body |
| S8 the records | the merge; then every `## Removes` row is gone from the tree, `changelog.md` carries the numbers of phases 1 and 2, and `overview.md` is closed | `read` against the diff; `unverified_check.py --baseline` exit 0, read directly |

## Data & interfaces

- `.github/workflows/test.yml`: the Windows entries gain `store`; the pytest line ends `${{ matrix.split }} ${{ matrix.store }}`; one upload step after it; one `durations` job (`needs: pytest`, `if: ${{ !cancelled() }}`, `actions/download-artifact@v4` with `pattern: test-durations-*`, the script, `actions/upload-artifact@v4` as `test-durations`). Parts and the union retained 7 days, each uploaded with `overwrite: true`, because re-running failed jobs re-runs the `durations` job, which reads every part again; a run older than that is re-run (`gh run rerun <id>`), which is one command and no commit.
- `.github/scripts/durations_union.py`: `--parts <dir> --count <K> --committed <path> --out <path>`; exit 0 wrote the union, 2 refused; writes `$GITHUB_STEP_SUMMARY` when set, stdout otherwise; names no machine path; a `Reads:` line and the floor line. Spread is slowest shard over the mean, as #874's S5 read it.
- `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`: `staleness(collected, durations)` gains the seconds side under the same `STALE_SHARE`; the sentence names `gh run download <run id> -n test-durations -D <dir>` and `python3 .github/scripts/budget_check.py --baseline origin/<base> --restate-price`, and `test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe` asserts the whole restate command; `test_the_pytest_line_hands_the_split_to_pytest` reads the store expression after the split; new cases for the entries, the step, the job and the union script; `test_an_entry_nobody_collects_is_not_counted` keeps its name and says what the entry now counts toward.
- `.test_durations`: same shape, written whole by the union, LF.
- `.github/scripts/budget_check.py`: `expected_level(base_level, ratio)` beside `price_problems`, returning `seconds(base_level * ratio)` with a `Reads: nothing` line; `price_problems` and the `restate` branch of `check` call it, and that expression appears nowhere else in the file.
- `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md`, the `slow-file:<path>` row's Kind cell, and `questions.md`, the gate-or-report bullet: `report`, with the measurement that moved it (one union moves a single file 0.67 to 1.72 times the level from the next, #931) and `suite-seconds` named as the gate. The row's unit, measurer and starting ceiling stay as they were.

## Rule changes

- nothing
  why: internal: every run's Windows shards measure the durations, held by
    tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the release checklist's refresh box | `docs/release-checklist.md#"the Windows job runs the whole suite as one job and uploads the file."` | the staleness case is the schedule, and the recipe paragraph says a run's artifact is the refresh; a box skipped by decision was a prompt |
| the measuring shape of the recipe — one Windows job, `timeout` 60, the dispatch, the two-part upload condition, the restore | `CONTRIBUTING.md#"place of the four Windows shard entries, the three macOS shard entries left"` | the paragraph is rewritten in place: every run's Windows shards store, the `durations` job unions, the artifact is downloaded |
| the recipe's download-and-restore sentence | `CONTRIBUTING.md#"line ends LF, commit it, and restore the shards."` | there is nothing to restore; the download sentence is the remedy the case prints |
| the post-refresh instruction to re-read the macOS shards' times and set their `timeout` | `CONTRIBUTING.md#"whole macOS cost is unseen by the division: after a refresh, read the macOS"` | the rule beside the values in `test.yml` is the one reader of a `timeout`; a shard past it fails loudly and the rule moves it, and a refresh now lands on any pull request, not at a moment somebody reads |
| the second copy of the price-level expression (the reframe after round 4) | `.github/scripts/budget_check.py#"expected = seconds(base_level * ratio)"` | `expected_level` is the one expression, and `price_problems` and `check` call it |
| 1791876665's record of the `slow-file` family as a gate (the reframe after round 4) | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md#"gate · a slow file that grows past 1.3 times fails"`, and the `slow-file:*` entry in its `questions.md`'s list of gates | rewritten in place to `report`; `seal/budgets.md`'s row is the live fact and `settle` folds the spec, so the spec says what the row says |

## Open questions → questions.md

Nothing a person must answer before the build; the rows are the work's and a measurement's, with the phase that answers each.

Framed 2026-10-13 by framer, before the build.
Reframed 2026-10-15 by framer, after round 4.

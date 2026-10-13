# 1791876667-the-durations-refresh-has-a-schedule — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | open — the union commit after the branch's first run closes it, and `plan.md`'s Status cell takes that hash |
| Ran by | specseal:smith on Opus 5.5, as `routing.md` and `handoff.md` name it |

## What this phase was asked

Build phase 1 up to its first push point and stop there: the `store:` key on
the four Windows entries of `test.yml`, the store expression after the split
on the pytest line, the upload step and the `durations` job;
`.github/scripts/durations_union.py`; cases T1–T6 and T10, each seen red.
Verify locally what can be verified locally — the union script against
fixture parts, the workflow shape cases, each case red by its mutation — and
record the local numbers and the *before* readings from recent runs, read
with `gh api`. Say first whether the frame holds against the tree. Commit,
push nothing, and hand back what the run must show. The orchestrator pushes,
opens the draft pull request and resumes this phase with the run id, to read
the parts and commit the union. The plan was approved 2026-10-14 with its
two named judgments: phase 1 commits the union once, and the check gates
both ways. #930's `budgets` job stays a job of its own (`questions.md` Q4's
default).

## What this phase found

### Whether the frame holds

It holds for everything phase 1 builds, with four places where the tree
said something the frame did not.

1. **T2 keeps its old name.** `plan.md`'s test rows name T2
   `the_pytest_line_hands_the_split_then_the_store`, and `spec.md` §*Data &
   interfaces* says `test_the_pytest_line_hands_the_split_to_pytest` is
   rewritten. The second wins: released rows anchor the old name —
   0.20.0's S4 (`seal/releases/0.20.0.md`) and 0.21.0's macOS S1
   (`seal/releases/0.21.0.md`) cite
   `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#test_the_pytest_line_hands_the_split_to_pytest`,
   and a rename would make both stop resolving. The body now pins
   `${{ matrix.split }} ${{ matrix.store }}`; the anchor's hash moves, which
   phase 3 re-reads with the other `test.yml` rows.
2. **The shallow-checkout case read `needs: pytest` as running pytest.**
   `tests/test_ci_gives_the_checks_what_they_need.py#test_every_job_that_runs_pytest_has_the_whole_history`
   selected a job by the substring `pytest ` or `pytest\n`, so the
   `durations` job — a checkout and `needs: pytest` — was red for a depth it
   does not need: it resolves no SHA. The case now selects a job by a code
   line that calls pytest (`RUNS_PYTEST`: `run: pytest …`, a line of a
   `run: |` block, `python -m pytest`). Executed over every workflow, the old
   rule and the new select the same three jobs (`publish-release.yml:seal`,
   `test.yml:pytest`, `test.yml:arm-check-grammar`) and differ only on
   `test.yml:durations`. #930's `budgets` job has the same shape and meets
   the same rule whichever pull request lands second.
3. **The pytest job may not hold a blank line.**
   `tests/test_a_unit_the_extractor_cannot_bound_is_refused.py#test_a_quoted_line_resolves_in_any_file`
   bounds `test.yml#"pytest:"` at the first blank line and asserts the span
   reaches the job's last step. The upload step therefore follows the pytest
   line with no blank between them, and the anchor's span grows to include
   it.
4. **The four Windows job names change.** GitHub names a matrix job by every
   value of its entry, so they read
   `pytest (windows-latest, 3.12, --splits 4 --group k, --store-durations --clean-durations, 20)`
   from this run on. Read with `gh api …/rulesets/<id>`: the required checks
   of both rulesets are `lint`, `release` and `ledger`, so no required check
   moves. #930's plan reads a leg off the name, and the system is still its
   first value. The run shows the names; nothing here executed them.

### What building it settled

- **A part is every file under `--parts`, labelled by its directory.**
  `actions/download-artifact@v4` with `pattern:` and no `merge-multiple`
  puts each artifact in a directory of its own name, so a label is the
  artifact's name, `test-durations-<job-index>`, which is never a path of the
  machine. Merged, the four `.test_durations` would be one file written four
  times; T10 refuses `merge-multiple`.
- **The union is written in the committed file's own shape.** Executed: the
  committed `.test_durations` is byte-identical to
  `json.dumps(…, indent=4, sort_keys=True)` with no final newline, and the
  union is written that way with `newline="\n"`, so the committing diff is
  prices and ids and nothing else.
- **The refusals are the frame's three and five more.** A part missing, an id
  in two parts and a part that does not parse are the frame's. Building them
  added an empty part, a price that is not a non-negative number (a boolean
  among them), a part that is not UTF-8, no parts directory at all, and a
  committed file that does not parse. Each is exit 2 with nothing written,
  and each has its own case. A shard killed at its `timeout` leaves the
  committed file in place, and a shard that uploads it hands the union every
  id in two parts — which is why the upload is restricted to `store` and why
  the duplicate refusal says so.
- **Two values beside the frame's.** `if-no-files-found: error` on both
  uploads, so a part that vanished is a red step on its own shard. The
  `durations` job carries `timeout-minutes: 5`, a bound nobody waits on in
  the ordinary run (the frame's estimate is about a minute) and the only
  thing that stops a hung download.
- **The summary's spread and the before readings are different measures.**
  A part's *measured seconds* is the sum of its cases' setup, call and
  teardown over every xdist worker. Pytest's last line, which the before
  readings below take, is the session's wall clock. Phase 2's before and
  after must compare one measure with itself: the parts of this run against
  the parts of the next one.

### The local numbers

`executed` 2026-10-14 at 67422a3d.

- `bin/test tests --collect-only -q -p no:xdist`: 13,930 collected, 16 of
  them this phase's cases. Against the committed file: 476 unpriced
  (3.42 %; the frame's 460 plus the 16), 28 dead, worth 0.9 s of 7,861.7 s
  (0.012 %). Unpriced by file: `test_one_table_walker_reads_what_gfm_renders.py`
  228, `test_whether_a_line_is_live_is_asked_by_what_the_line_does.py` 72,
  `test_the_mode_question_is_asked_once.py` 64, `test_evidence_check.py` 43,
  this module 16.
- The phase's verification command, `bin/test
  tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py
  tests/test_ci_gives_the_checks_what_they_need.py
  tests/test_a_slow_case_names_itself.py
  tests/test_a_workflow_is_read_the_one_way.py
  tests/test_a_reader_declares_its_input_class.py
  tests/test_a_script_says_which_interpreter_it_needs.py -q -p no:xdist`:
  exit 0, 157 passed, 2 skipped, at 9902fe22. The other modules that read
  `test.yml` (`test_a_unit_the_extractor_cannot_bound_is_refused`,
  `test_arm_check`, `test_deferral_check`, `test_release_hygiene`,
  `test_the_gate_names_every_step_ci_runs`,
  `test_the_lenient_run_says_what_the_broad_gate_will_say`,
  `test_the_suite_has_a_command_that_is_cheap_twice`), with the reader and
  floor modules: exit 0, 467 passed, 2 skipped. After the refusal cases
  joined (67422a3d), this module, the CI module and the reader module: exit
  0, 116 passed, 2 skipped. `ruff check` and `ruff format --check` on the
  three Python files: exit 0.

### The before readings

`executed` 2026-10-14 with `gh api repos/<r>/actions/runs/<id>/jobs` and
each job's log, on the five most recent `pull_request` runs whose head holds
the committed file (blob equal to this branch's). Pytest's own seconds are
the session's last line; *max/mean* is the slowest shard over the four.

| Run | Windows groups 1 · 2 · 3 · 4, pytest s | max/mean | max/min | wall max/mean |
|---|---|---|---|---|
| 38359863214 | 727.6 · 469.9 · 693.8 · 677.0 | 1.13 | 1.55 | 1.12 |
| 38359676917 | 668.7 · 437.4 · 667.0 · 720.5 | 1.16 | 1.65 | 1.16 |
| 38359441348 | 729.7 · 532.0 · 618.1 · 548.9 | 1.20 | 1.37 | 1.19 |
| 38355857651 | 706.0 · 559.6 · 632.6 · 670.0 | 1.10 | 1.26 | 1.09 |
| 38355824134 | 551.1 · 614.7 · 381.6 · 611.4 | 1.14 | 1.61 | 1.15 |

The same five runs on macOS read 1.19, 1.05, 1.08, 1.12 and 1.29 by
pytest's seconds.

**The frame's 1.05 is one run on another file.** Run 38335775781 ran at
cc1768d1, whose `.test_durations` is #874's first measurement (run
38332345615, introduced by 3d2324ce: 14,105 entries summing 9,065.7 s, ids
not yet one spelling). It reads 1.05 on Windows and 1.03 on macOS by the
same reading. The committed file is the second measurement (run
38342987499, c59c7664: 13,482 entries, 7,861.7 s), and on it the five runs
above read 1.10 to 1.20, median 1.14. The slowest group is not one group:
group 1 in three runs, group 4 and group 2 in one each. S5's *within the band of the
unsharded file's (1.05) plus noise* is phase 2's to read against these five
rather than against the one.

### The mutations

Every case below was seen red through `bin/mutation-check`, one break at a
time, after the commit; exit 0 is `red`. The cases are named by their row in
`plan.md`; the last two are the shallow-checkout case's.

| Case | Break | Red |
|---|---|---|
| T1 | a Windows entry loses `store` · a macOS entry gains it | 1 failed · 1 failed |
| T2 | the line ends at the split · the store precedes the split | 1 · 1 |
| T3 | `always()` dropped · `matrix.store != ''` dropped · `include-hidden-files` dropped | 1 · 1 · 1 |
| T10 | `needs:` dropped · `if:` dropped · `if: ${{ success() }}` · `--count 3` · `merge-multiple: true` | 1 · 1 · 1 · 1 · 1 |
| T4 | a part skipped in the union · keys unsorted · CRLF written | 3 · 1 · 1 |
| T5 | fewer parts read as complete · a duplicate overwritten · an unparseable part read as empty · a non-number let through · a boolean let through · a non-object let through · a non-UTF-8 part read · an empty part let through · no parts directory read as none · the refusal kept out of the summary | 1 · 1 · 2 · 1 · 1 · 1 · 1 · 1 · 1 · 10 |
| T6 | the spread over the fastest · the committed sum not read · a machine path in a label · the ratio inverted · dead not counted · unpriced not counted · the no-ratio line dropped | 1 · 1 · 8 · 1 · 1 · 1 · 1 |
| shallow checkout | the pytest job's `fetch-depth: 0` dropped · `publish-release.yml`'s `seal` job's, whose pytest is a line of a `run: \|` block | 1 · 1 |

T4's CRLF break is `newline="\r\n"`, because on macOS `newline=None`
writes LF and nothing could see it. The plain `newline=None` break is one
only a Windows shard can see, and this module runs on one; that is `read`,
not executed.

### For phase 1's second half and for phase 2

- **The run must show** four `test-durations-<4…7>` artifacts from the
  Windows shards, one `test-durations` artifact from the `durations` job,
  and that job's summary; `phases/phase-1.md` takes each part's seconds, the
  spread and the per-part ratio from it as this phase's *after the build,
  before the commit*.
- **Not verified here: whether `gh run download <id> -n test-durations`
  overwrites a `.test_durations` that is already in the directory.** The
  artifact holds the file at its root, so downloading into the repository
  root writes it in place if `gh` overwrites. If it refuses an existing file,
  the remedy phase 2 prints needs `-D <dir>` and a move. Answered by phase
  1's own download of the union.

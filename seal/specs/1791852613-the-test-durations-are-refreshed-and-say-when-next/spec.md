# Feature Specification: the test durations are refreshed and say when next (#874)

<!-- seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against — verification that runs unattended* | Between a sentence saying when the file is refreshed next and a check that refuses a file past its age, the check is chosen, and the refresh itself is run by the session under `automation` rather than dispatched by the owner |
| `CONTRIBUTING.md` §*Running the checks*, the paragraph beginning *`.test_durations` goes stale as cases are added* | The refresh recipe this work executes as written: one Windows job with `--store-durations`, the macOS shards left in place, `timeout` 55 for the whole leg, the upload step's two-part condition, `gh run download`, LF, commit, restore the shards. Also the sentence that after a refresh the macOS shard times are read again and their `timeout` re-set |
| `.github/workflows/test.yml`, the `timeout` comment above the matrix | The budget rule every leg is held to: 1.5 times the leg's slowest measured job, rounded up to 5 minutes, the base being the slowest of the runs measured, the run id written beside the value (#841's Q6 (a), inherited by #864) |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The new case is a new red a contributor can meet, so it carries a test seen red, a failure direction (*block more*) and a prompt budget (zero: it asks nobody, it prints the counts and the recipe's section) |
| `skills/agent-contract/SKILL.md` §6 | Push nothing: the measuring run's push and dispatch, and the post-refresh run's, are the orchestrating session's acts, as #864's plan placed them. §15: the new case is seen red before it is planted — on the real tree, where the file is 9.4 % stale today |
| `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*; `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | 0.21.0's S1–S5 and 0.20.0's S4/S8/S9 anchor `test.yml#"pytest:"`, the shard module's cases and three quoted lines of `CONTRIBUTING.md`; this work's edits drift or break them, and each re-read or correction is a row in `seal/ledger/1791852613-the-test-durations-are-refreshed-and-say-when-next.md`, never in the released files |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below is read by `evidence-check`'s records arm, since `seal/config.md` declares `Removes from` 1791780031 and this item is above it |
| `docs/release-checklist.md` §*0. Before starting* | Where the planned refresh lives from now on: a box at release preparation, so the check below is the backstop and not the schedule |

## Scope

**The measurement, from this tree** (`executed` 2026-10-13 by this frame:
`bin/test tests/ --collect-only -q` on the worktree at
`release/v0.21.1`'s tip, compared with the committed file by a script in
the session's scratch directory, not the tree). The suite collects 13,474
cases. The file holds 13,042 entries summing 7,530 s, a mean of 0.577 s.
**1,270 collected cases (9.43 %) have no price in it, and 838 of its entries
are no longer collected.** The issue measured 504 and 727 at 5623d728 five
days earlier; the 0.21.0 cycle added 655 cases, 4.9 % of today's suite. The
unpriced cases sit in 64 modules, 172 of them in
`tests/test_the_seal_is_taken_once_by_the_sealer.py` and 170 in
`tests/test_a_moved_rule_leaves_its_definition.py`. Reproducing
`pytest-split`'s contiguous division over this collection order with the
mean for every unpriced case gives Windows groups of 2,662 · 7,266 · 1,093 ·
2,453 cases at 1,970–1,974 file-seconds each, and macOS groups of 6,485 ·
3,884 · 3,105 — equal in the file's seconds, which is the only balance the
file can promise, and 9.4 % of the cases are priced at a guess.

**In.**

1. **The file is refreshed by the recipe, on Windows, from this branch.**
   One commit puts `test.yml` into the measuring shape the recipe names;
   the session pushes the branch and dispatches `test.yml` on it (a push
   with no pull request open runs nothing by itself, which is what
   `workflow_dispatch` is there for); the Windows job runs the whole suite
   as one job with `--store-durations` and uploads `.test_durations`. The
   next commit restores `test.yml` byte for byte and commits the downloaded
   file with LF line ends. The measuring commit is not on the branch's
   final tree in any form but a reverted one, and a squash removes it from
   history.
2. **A check says when the file is refreshed next.** A case in
   `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`
   compares the suite's collection with the file and fails when more than
   one collected case in twenty is unpriced — `STALE_SHARE = 0.05` (NAME
   NOT IN TREE: phase 1 plants it) beside `SHARDED`. Its message names the
   unpriced count, the collected count, the share, and
   `CONTRIBUTING.md` §*Running the checks* as where the recipe is. It reads
   the collection as `pytest-split` does, before the split trims it:
   `tests/conftest.py` gains a `pytest_collection_modifyitems` hook that
   records every collected node id on the session (NAME NOT IN TREE), and
   `pytest-split`'s own hook is `trylast`, so the record is the whole suite
   on every shard. Where the invocation did not name `tests/`, the case
   declines with a reason rather than judging a module's collection against
   the suite's file. Dead entries are not counted: the division never reads
   them, so they cost nothing but bytes.
3. **The sentence that answers the issue's second half.** The recipe
   paragraph of `CONTRIBUTING.md` says the file is refreshed at each
   release's preparation and whenever that case goes red, and names the
   case. `docs/release-checklist.md` §*0. Before starting* gains one box:
   dispatch the measuring run from the release branch now, by the recipe,
   and commit the downloaded file in the preparation commit — so the file
   prices every case of the release and the next cycle starts at zero, and
   the check is what catches a release that skipped it.
4. **The budgets are re-set from the next run, by the rule beside the
   values.** After the restore commit the session pushes and dispatches
   once more; the phase that reads that run sets each macOS shard's
   `timeout` — and any other leg's whose base moved — from the measured
   slowest job, 1.5 times rounded up to 5, the base being the slowest of
   the runs measured, and writes the run id in the comment. A value whose
   rounded result does not change is left as it is, and the comment still
   gains the run.
5. **The records.** `phases/phase-N.md` per phase with the measured
   figures; the ledger fragment with one row per scenario below and the
   re-reads and corrections of the released rows this work drifts;
   `changelog.md` with one `### Changed` entry; `overview.md` closed.

**Out, and why.**

- **A `workflow_dispatch` input that runs the measuring leg without a
  commit.** `inputs.store` on the pytest line, the timeout and an upload
  step would make a refresh one command and never put the shard cases in
  the red. It changes three expressions the readers pin
  (`test_the_pytest_line_hands_the_split_to_pytest` wants the line to end
  in `${{ matrix.split }}`, the timeout case wants
  `${{ matrix.timeout }}`), and `matrix` is not a context a job-level
  `if` can read, so the three other Windows shards would still start. It
  is `plan.md` Alternatives E, the design to adopt when the per-release
  refresh proves costly by the recipe, and the report asks the orchestrator
  to file it. This item executes the recipe the tree already has.
- **A macOS-measured durations file.** #864's Alternatives D: two files
  ageing apart, and collection is identical across legs.
- **Cases whose price changed.** A case the file prices at 1 s that now
  runs 10 s is invisible to a count; each leg's `--durations=50` table and
  the budgets catch that, and nothing here claims to.
- **Removing the 838 dead entries by hand.** The refresh replaces the whole
  file; nothing edits it.
- **The shell oracle's macOS cost and #826's cuts.** Left where #841 and
  #864 left them.
- **The `evidence-check` heading cut at a fence** that #864's phase 2
  found: whoever owns that script, not this item.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 · the file is measured on Windows and committed whole | Given the measuring commit on this branch, when the session dispatches `test.yml` on it, then the run's Windows job runs the whole suite as one job with `--store-durations` and uploads `.test_durations` whether or not the job is green; and the committed file has LF line ends, parses, and prices every case the tree at the restore commit collects, so the count of unpriced cases is zero there | **Executed**: the dispatched run read with `gh run view --json jobs` (the Windows job's time, `startedAt` to `completedAt`, and its summary line), `gh run download`; locally `file .test_durations` says no CRLF, and `bin/test tests -q -k test_the_durations_file_prices_the_suite` passes at the restore commit, exit read directly |
| S2 · the check fails past one in twenty, and says so | Given the suite's collection and the file, when more than `STALE_SHARE` of the collected cases are unpriced, then `test_the_durations_file_prices_the_suite` fails with a message naming the unpriced count, the collected count, the share and `CONTRIBUTING.md` §*Running the checks*; at or under it the case passes; the arithmetic is one function with fixture cases at the boundary (exactly one in twenty passes, one more fails, an empty collection is refused, dead entries do not count) | **Executed**: the case red on the real tree before the refresh (9.4 % today), each fixture case red with the comparison inverted, and `bin/mutation-check` or the sentence deleted, recorded in `phases/phase-1.md` |
| S3 · the check reads the whole collection on every shard, and declines a partial one | Given a sharded invocation (`--splits K --group k`), when the case runs, then the collection it compares is the whole suite and not the group; given an invocation that named a module rather than `tests/`, the case declines with a reason naming what it needed | **Executed**: locally through `uvx` with `pytest-split==0.11.0` on this tree, `-k test_the_durations_file_prices_the_suite` under each group of `--splits 3`, exactly one group runs it and it passes; `bin/test tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q` reports it skipped with the reason; and the post-refresh run's seven shards all green on it |
| S4 · the sentences say when | Given a contributor reading `CONTRIBUTING.md`'s recipe paragraph and `docs/release-checklist.md` §0, then the first names the case as the moment of the next refresh and the release's preparation as the planned one, and the second has the box; `tests/test_docs_line_wrap.py` is green over both | **Read** against the two files; `bin/test tests/test_docs_line_wrap.py -q` executed |
| S5 · the balance after the refresh is read off the legs | Given the post-refresh run at the restore commit, when its eight jobs are read, then the four Windows shards' `passed` plus `skipped` sum to ubuntu's and so do the three macOS shards'; the slowest Windows shard is under the inherited 12 minutes; and the record carries every job's time, summary line and the slowest shard's ratio to the mean by pytest's own seconds, beside the 1.37 the issue traced to the file's age | **Executed**: `gh run view <id> --json jobs` and each job's log, in `phases/phase-3.md` |
| S6 · the budgets follow the rule | Given the figures of S5, then each leg's `timeout` is 1.5 times its slowest measured job rounded up to 5, the base being the slowest of the runs the comment lists, the comment names the post-refresh run beside each value it changed or confirmed, and the job still reads `${{ matrix.timeout }}` | **Executed**: `bin/test tests/test_a_slow_case_names_itself.py tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/test_ci_gives_the_checks_what_they_need.py -q`; that GitHub reads the new values is the pull request's run at the final SHA |
| S7 · the records | Given the merge, then `seal/ledger/1791852613-…md` carries S1–S6 with run ids and dates, the `Re-read ·` and `Corrected ·` rows for every released row this work drifted, and `evidence-check --strict .` exits 0; `changelog.md` has its entry; `overview.md`'s `## Not verified` names the sealer for the whole suite | **Executed**: `python3 skills/evidence-check/scripts/evidence_check.py --strict .`, exit read directly |

## Data & interfaces

- `.test_durations` keeps its shape: a JSON object, `tests/<file>::<case>`
  to seconds, written whole by `pytest-split`, LF.
- `tests/conftest.py`: one hook, `pytest_collection_modifyitems(session,
  items)` at default order, which records `[item.nodeid for item in items]`
  on the session under one attribute and changes nothing else. It runs
  before `pytest-split`'s `trylast` hook and before nothing else that
  matters: a `-k` or `--deselect` trims later, so the record is the
  collection and the case runs on it when `-k` selects it alone.
- `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`:
  `STALE_SHARE`, one pure function over `(collected, durations)` returning
  the unpriced ids, the suite case, and the fixture cases. The three existing
  cases keep their names and bodies, so 0.20.0's S4 and 0.21.0's S1 anchors
  do not move for this.
- `.github/workflows/test.yml`: the matrix entries unchanged in count and
  shape; `timeout` values and the comment's figures where the rule moves
  them. The measuring shape exists on exactly one commit and is reverted on
  the next.
- Ledger anchors this work drifts, for the fragment's re-reads (`read`
  2026-10-13 from `seal/releases/0.21.0.md` and `0.20.0.md`):
  `.github/workflows/test.yml#"pytest:"` (0.21.0 S1, S2, S3, S4,
  S5; the re-reads of 0.20.0's S1/S2/S8 cite it too), the three quoted
  `CONTRIBUTING.md` lines of 0.21.0's S5 and the re-read of 0.20.0's S9
  (the recipe paragraph's first line is one of them, so editing it breaks
  rather than drifts, which is a `Corrected ·` row), and
  `tests/conftest.py` units only if an existing one is touched, which the
  hook does not require.

## Rule changes

- nothing
  why: internal: the durations file and its refresh, held by
    tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py.

## Removes

nothing — the work replaces the data file whole and adds a case, a hook, a
constant and sentences; no unit, rule sentence, test pin or copy leaves the
tree. The 838 dead entries leave with the data, and a data entry is no
coordinate the records arm reads. The measuring shape of `test.yml` is
reverted within the branch, not removed from anything released.

## Open questions → questions.md

Nothing a person must answer before the build: `questions.md` records the
share (Q1) and the checklist box (Q5) as decided by this frame under
`automation`, with the values the owner may overturn at the plan's approval,
and the measurements (Q2, Q3) and the work's row (Q4) with the phase that
answers each.

Framed 2026-10-13 by framer, before the build.

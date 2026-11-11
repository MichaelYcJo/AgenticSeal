# Implementation Plan: 1794383425-a-committed-durations-file-turns-ci-red (#1486)

## Technical context

The tree as read at `196a450a5`.

**Durations.** The Windows leg of `.github/workflows/test.yml` runs in four
shards (`:108-111`) and macOS in three (`:105-107`). `pytest-split` divides
both by the committed `.test_durations`. Each Windows shard stores its own
session with `--store-durations --clean-durations` and uploads it as a part
(`:176-184`). The `durations` job unions the parts through
`.github/scripts/durations_union.py` (382 lines) and, on a pull request into
`main`, fails where the committed file is past `STALE_SHARE` (`:200-223`).
`.github/scripts/release_report.py#durations` reads the file from the tag's
tree and from this tree, and exits 2 where it cannot.

**YAML.** `tests/text/test_ci_gives_the_checks_what_they_need.py:85-470`
reads jobs, steps, triggers, concurrency and matrix entries by indentation
and regular expressions. `tests/conftest.py:78-187` holds a second reading of
steps. `tests/behaviour/test_a_release_publishes_its_note.py:59-98` holds a
third, by line indentation. `.github/scripts/run_tests.py:95-130` pins the
suite's two oracles and installs them on a fresh build and into an adopted
`.venv` through two near-copies, `add_markdown_it` (`:241`) and
`add_cmarkgfm` (`:290`).

**The failure scenario of the chosen approach, in six months.** The cache
is evicted, or an `actions/cache` major release changes how a key or a
cross-OS archive matches. Either way the Windows shards restore nothing and
split by count. No job turns red. The `durations` job's spread line in its
summary and pytest-split's `No test durations found` line in each Windows
log are the only signals, and the slowest Windows shard grows by an
estimated 60 to 90 s per pull request, the issue's figure, until someone
reads them. The Windows timeout of 10 minutes covers a count split.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. The union from `main` runs in `actions/cache`, restored by the Windows shards; the `durations` job saves on every run that is not a pull request's | The six-month scenario above: a silent fall back to a count split | Chosen, by the issue's decision. Saving on `push` and on `workflow_dispatch` alike lets a dispatched run seed a branch's cache, at no cost to the push path. |
| B. Keep the committed file and its age verdict (the structure kept) | The issue's six red runs on the file's age, each followed by a refresh pull request | Rejected by the issue's decision. The premise that keeps it, that the tree at a tag must hold the measurement, was checked: only `release_report.py` reads it at a tag, and the push run's artifact, kept 90 days (*Grounding*), serves that read. |
| C. Split by count and drop the durations machinery | Shard totals of 177, 392, 680 and 368 s against about 404 s balanced, the issue's model | Rejected by the issue's decision. |
| D. Save the cache on pull-request runs too | A pull request's cache is scoped to its merge ref, so no other pull request restores it, and each one spends quota (`actions/cache` README, *Grounding*) | Rejected. It costs quota and balances nothing. |
| E. Run the `durations` job only on runs into or on `main` | Every other pull request loses the per-shard seconds and spread, the one signal of scenario A's silent fallback | Rejected. The job's median is 8 s (*Grounding*), and `release-report` needs its union on the release pull request anyway. |
| F. Read workflows with `yaml.safe_load` | The trigger key `on:` comes back as `True` in all six workflow files, and `timeout: 15` as an integer where the cases compare strings | Rejected for `yaml.BaseLoader` (*Grounding*). |
| G. Move only the readers the issue names, and keep `tests/conftest.py`'s step readers (the structure kept) | Two readings of a workflow's steps stand side by side. The premise comments at `tests/conftest.py:69` and `tests/test_conftest.py:107`, "No YAML parser is installed where this suite runs", become false, and contract rule 19 asks the same change to remove what stood on them. | Rejected. The premise that would keep them, that a reader without a parser serves somewhere a parser cannot, was checked: no test runs without the suite's packages, and `bin/test` installs them. The one reading a parser does not give, the shell comments inside a `run:` script, keeps `code_line` for that alone. |
| H. A third copy of the install pair in `run_tests.py` for PyYAML (the structure kept) | Each pin brings a `has_`/`add_` pair and four or five cases. `bin/seal layout --pairs` already reports 91 similar case pairs in `tests/github/test_run_tests.py`, the count #1489 cites | Rejected for one pair over a table of the pins. The premise that would keep the copies, that each failure sentence names what imports its package, was checked: the two sentences differ only in the package and its reader, which a column holds. |
| I. Keep macOS in three shards | Three jobs each pay about 45 s of fixed cost, while every macOS shard (128 s at most) already finishes inside the Windows leg's slowest shard (242 s at most), so the shards shorten no run | Rejected for one job: estimated at 160 s on the median run and 222 s on the slowest, still inside the slowest Windows shard (*Grounding*, a model). Its failure scenario is a macOS job that grows past the Windows shards and sets the run's length. Its timeout and the release table's leg minutes show that. |
| J. Five or six Windows shards | The slowest shard is an estimated 33 s or 55 s shorter, at the cost of one or two more jobs of about 62 s fixed cost each | Rejected. The issue's decision keeps the four-shard balance. The after reading of *Scope* item 8 is what a later change would weigh. |
| K. Drop the release table's suite row and test-file table | The owner loses the per-file seconds the checklist's *Each release clears what grew* reads | Rejected for the run artifacts, as the issue proposes. |
| L. Fall back to the tag's tree `.test_durations` where the tag's artifact is gone | A reader of the old fact kept for one release | Rejected. The first release table after this work reads the tag's suite as no reading where the artifact is gone, and fails nothing. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1 and 2 | `tests/github/test_run_tests.py`, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py`, `tests/behaviour/test_the_release_seal_is_drawn.py`, `tests/behaviour/test_release_hygiene.py`, and the new loader case, seen red under `yaml.SafeLoader` | `2fc78c903` |
| 2 | *Scope* item 3 | `tests/text/test_ci_gives_the_checks_what_they_need.py`, `tests/behaviour/test_a_release_publishes_its_note.py`, `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` | `e51c4bb79` |
| 3 | *Scope* item 4 | The enumeration's command and its list in the phase record; `tests/test_conftest.py` and each module the list names | `0fc6e80a5` |
| 4 | *Scope* items 5, 6 and 7 | `tests/github/test_durations_union.py`, `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, `tests/github/test_release_report.py`, `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`, `tests/test_censuses.py`, `tests/behaviour/test_the_release_check_watches_what_ships.py`; `git ls-files .test_durations` prints nothing | `6f38a1209` |
| 5 | *Scope* item 8 | `tests/text/test_ci_gives_the_checks_what_they_need.py`, `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`; `grep -c -E '[0-9]{11}' .github/workflows/test.yml` prints 0; this work item's own CI run, the `workflow_dispatch` run 42996432567 at `25133f410`, its job times written in the phase record | `0cd12880c` |

## Overlap with the release

Read: the issues of all nine items, and the frames committed on four
branches, each taken from the branch with `git show` (executed): #1481 at
`d2040b335`, #1483 at `0dd6d89f3`, #1487 at `af8bccf1f` and #1488 at
`17674989a`. #1498 has merged into `release/v0.37.4` as `10e721f11`
(executed, `git log 18a7e18fb..origin/release/v0.37.4`). Four items have not
started: #1482, #1484, #1485 and #1489. Two items meet where both change a
file, or where one changes something the other's change reads
(`agents/framer.md` *Order of work* step 4). The milestone's note that
#1486 shares no file with the others does not hold, as the rows below show.
#1481 changes `skills/settle/scripts/settle.py` and `tests/skills/test_settle.py`
and meets nothing here; its frame reads the `--stale-fails` verdict this work
removes only to conclude that its new cases do not cross it.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1498 | `tests/censuses.py`: it changed `#_root_names`, this work changes `#OLD_NAME_RECORDS` | #1498 | Already merged into the release branch. The hunks are apart, so this branch takes it with a merge of the release branch and no conflict. |
| #1483 | It removes `tests/behaviour/test_the_gate_names_every_step_ci_runs.py` and the section of `skills/verify/scripts/broad_gate.py` that held `job_steps`, with their cases in `tests/skills/test_broad_gate.py`, and the last case of `tests/behaviour/test_a_release_publishes_its_note.py`. | #1483 | #1483 merged first (#1524). This branch merged it at `3ed9a1bff`: the resolution keeps #1483's deletions of the module, the gate's section and its cases, and this work's removal of the conftest step readers and their cases in `tests/test_conftest.py`. |
| #1487 | `.test_durations`, whose entries for its deleted cases it removes (its Scope 12) and which this work deletes, a modify/delete conflict. `tests/censuses.py`: its module docstring, `#refused_domains`, `#OLD_NAME_RECORDS` and `#KEPT_FILES` change there, and `#OLD_NAME_RECORDS` and the sentence above it here. Its tests take 115 s on Windows, 7 % of the suite (the issue's figure), which moves the before and after readings of *Scope* item 8. | #1487 | #1487 merged first (#1525, `957a3bc7d`), removing its own `.test_durations` entries nowhere since its frame declined that edit, and this branch took it at `3ed9a1bff` with no conflict. Any after reading on this branch is taken without #1487's cases, and the phase record of *Scope* item 8 says so beside the before reading, which includes them. |
| #1488 | It leaves out the modules this work rewrites: `tests/text/test_ci_gives_the_checks_what_they_need.py`, `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` and `tests/behaviour/test_a_release_publishes_its_note.py:124-149`. Its asserts read `CONTRIBUTING.md` and `docs/releasing/release-checklist.md`, which this work changes. `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py`, which its issue counts 21 literal asserts in, is rewritten by *Scope* items 1 and 3. | #1486 | Its frame states the same order: its phase 4 rules the release-note module's other cases after this rewrite. Merged second, it counts and judges each assert once, on this work's text. |
| #1482 (not started) | Loaders by path: `.github/scripts/run_tests.py#_LAUNCH` and `.github/scripts/release_report.py#script` are two of its 22 files' kind | #1486 | Not framed. Its frame reads these files after this work changes them. |
| #1484 (not started) | `.github/scripts/release_report.py:125-128`, which this work's `--durations` change sits beside | #1486 | The same grounds as #1482. |
| #1485 (not started) | Docstrings and comments of `.github/scripts/*.py`, `run_tests.py`, `durations_union.py` and `release_report.py` among them, which this work rewrites | #1486 | A sweep over docstrings reads the final text once. |
| #1489 (not started) | `tests/github/test_run_tests.py`, whose similar case pairs it counts and this work's install-pair fold reduces | #1486 | Its count is taken once, on the folded file. |

## Operational impact

- **A new test-only dependency, PyYAML 6.0.3.** A plugin user installs
  nothing, because nothing under `lib/`, `skills/`, `hooks/` or `bin/`
  imports it. An adopted `.venv` gains it on its next `bin/test`. A
  contributor on the fallback commands installs it from the line in
  `CONTRIBUTING.md`.
- **New action dependencies**: `actions/cache/restore@v4` and
  `actions/cache/save@v4`.
- **No balanced division until a push to `main` runs this workflow.** The
  repository holds no cache (*Grounding*). Every pull request into
  `release/v0.37.4` after this one merges, and the 0.37.4 release pull
  request itself, split the Windows shards by count, each within its
  timeout. A dispatched run on the release branch,
  `gh workflow run test.yml --ref release/v0.37.4`, saves a cache scoped
  to that branch. Whether a pull request into that branch restores a base
  branch's cache is GitHub's documented behaviour as the framer recalls it,
  not read (`frame/questions.md` Q1).
- **The 0.37.4 release table.** Its tag-side reading comes from v0.37.3's
  push run, 42979122827 of 2026-11-11, whose `test-durations` artifact is
  kept 7 days. A release pull request run after 2026-11-18 reads the tag's
  suite as no reading.
- **The cache's footprint.** One file of about 880 KB per push to `main`
  (the committed file's size, executed), against the repository's 10 GB.
- **No version move here.** #1498 carries the move to 0.37.4.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-11 | The orchestrator folded each phase's frame statements in its own commit (`40a47e18f`, `1af6425ce`, `bf15c27a1`, `a0c2b1a39`, `98b475f64`, `237d75ac5`) and resolved the merge of #1483 at `3ed9a1bff` by keeping #1483's deletions and this work's removal of the conftest step readers | Each fold was a frame sentence a crafter's hand-back named and the tree contradicted (read); the merge's six conflicts were a module and sections #1483 deleted that this branch had rewritten | `skills/implement/SKILL.md` *1. Read the documents that outrank the code first* |
| 2026-11-11 | The orchestrator pushed the branch and dispatched `tests` (run 42996432567) for *Scope* item 8's reading, which phase 5's crafter declined under contract rule 6 | A push and a run of the full suite are the orchestrator's; the crafter wrote the run's figures into its phase record afterwards | `skills/agent-contract/SKILL.md` rules 2 and 6 |
| 2026-11-11 | The `durations` job's change to a gate: its failure direction is allow more, since the union step no longer exits 1 on a stale share; its prompt budget is zero | A wrong allow here is a shard split by count, which costs wall time bounded by each leg's timeout and fails no pull request; the deny it removes turned CI red six times on a stale file with no defect behind it (the issue). No step asks a person anything | `CONTRIBUTING.md` *What a change to a gate must carry* |
| 2026-11-11 | Round 1's finding 2, and the two frame lists fix pass 1's `62a2fb4f1` leaves incomplete, went to the framer to fold | Each is a sentence of `frame/design.md` or `frame/plan.md` the tree contradicts or leaves short: the release-note module's third case, which #1483 removed; the after reading's source, a dispatch run; and the settle skill's refresh clause, which neither *Scope* item 7 nor `## Removes` names | `skills/implement/fold-and-reframe.md` |
| 2026-11-11 | The title takes `refactor:`, as the issue's title does | The suite's verdict on any test is unchanged; what changes is where the durations live, how the workflow is read in tests, and how CI is sized | `~/.claude/skills/commit-pr-convention/SKILL.md` *커밋 메시지* |

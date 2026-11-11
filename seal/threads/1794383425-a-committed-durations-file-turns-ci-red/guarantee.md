# Guarantee: 1794383425-a-committed-durations-file-turns-ci-red

Audited on 2026-11-11 by the sealer, at `1a9a7a44d` against the base
`release/v0.37.4`, whose upstream resolved to `1a01c761a` (`executed`:
`git rev-parse --verify --quiet 'release/v0.37.4@{upstream}'`; the local
branch resolves to the stale `18a7e18fb`, which was not used). HEAD holds
the base (`executed`: `git merge-base --is-ancestor 1a01c761a HEAD`). The
gate record `trail/gate.md` names `run: 3ee85274f against 1a01c761a`.
`3ee85274f` is an ancestor of HEAD, and the one commit after it,
`1a9a7a44d`, touches only `trail/gate.md` (`executed`:
`git log --no-merges --name-only 3ee85274f..HEAD ^1a01c761a`).
`seal pr-body <item> --body <file> --check` exited 0 with the installed
plugin's `seal` and with the tree's `bin/seal` (`executed`). The repository
declares no `seal/parity.json` (`executed`: `git ls-files seal/parity.json`
prints nothing), and `routing.md` answers `open the pull request`, so no
comparison with an original is owed. `seal/config.json` names English for
both language keys, and no `pr.<lang>.md` is owed.

The broad gate's pass is the orchestrator's account. The sealer read
`trail/gate.md` at HEAD and ran nothing broad (`read`, contract rule 2).

## Claims re-run

The sample is weighted toward the claims the outcome rests on: the `seen
red` claims of the gate's own change (the S3 guard that round 1's finding 1
fixed, the release table's no-union reading), the loader's choice of
`yaml.BaseLoader`, the PyYAML pin's CI line, and the macOS one-job guard.
It adds the plan's narrow modules as an `executed` claim and the CI run's
job times that phase 5 records. Each test ran in a scratch clone at
`1a9a7a44d` with `PYTHONDONTWRITEBYTECODE=1`, using the worktree's `.venv`
interpreter. The tree under audit was not changed. A first pass of three
mutants ran against a stale `.pyc` of `tests/workflows.py` left by the
SafeLoader mutant, which has the same byte length. Those three were re-run
with the source touched, a clean control first, and only the re-runs are
reported below.

| Claim | Source | Command | Result |
|---|---|---|---|
| The plan's narrow modules pass at HEAD | `frame/plan.md` *Phases*, rows 1 to 5; `trail/rounds/round-1.md` *Confirmations*, the narrow modules | `python -m pytest -q -p no:cacheprovider` over `tests/test_workflows.py`, `tests/github/test_durations_union.py`, `tests/github/test_release_report.py`, `tests/github/test_run_tests.py`, the shard module, `tests/text/test_ci_gives_the_checks_what_they_need.py`, `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py`, `tests/behaviour/test_a_release_publishes_its_note.py`, `tests/text/test_settle_reads_before_it_removes.py` | Holds. 169 passed, 1 skipped, exit 0 (`executed`) |
| The release table's cases fail against the script that read the tree | `trail/phases/phase-4.md` *Seen red*, the second item | `.github/scripts/release_report.py` restored from `1a01c761a`, then `tests/github/test_release_report.py` | Holds. 19 failed, 11 passed, exit 1. The record counts 18 before the one-side case was added, which is the 19th (`executed`) |
| `test_a_union_this_side_alone_reads_against_no_reading_at_the_tag` is the case that catches `or` turned into `and` in the suite row's Change cell | `trail/phases/phase-4.md`, *A case added beyond the plan's cells* | HEAD's script with `ABSENT if old is None or new is None` changed to `and`, then `tests/github/test_release_report.py` | Holds. That case alone failed, 29 passed (`executed`) |
| The loader cases are red under `yaml.SafeLoader` | `trail/phases/phase-1.md` *Seen red*, the third item; `frame/plan.md` *Alternatives considered* F | `tests/workflows.py` with `BaseLoader` changed to `SafeLoader`, then `tests/test_workflows.py` | Holds. 2 failed, each on `assert 'on' in {... True: {...}}`, the trigger key read as `True` (`executed`) |
| `test_ci_installs_the_parser_the_runner_pins` is red against a `pytest` install line without PyYAML | `trail/phases/phase-1.md` *Seen red*, the first item | `.github/workflows/test.yml` restored from `1a01c761a`, then the case by `-k` | Holds. Exit 1 at `assert any(rt.PYYAML in words for words in installs)` (`executed`) |
| The union step's reader refuses a bare `--stale-fails` (round 1's finding 1, fixed at `bd4ec54d8`) | `trail/rounds/round-1.md` finding 1's close; `frame/design.md` S3 | A case that asserts a flag is not let through, so it was shown both ways. (1) HEAD's `test.yml` with ` --stale-fails` appended to the union line, then `test_the_durations_job_needs_pytest_and_runs_unless_cancelled`. (2) The same mutant with the shard module restored from `335cc0e75`, the guard's old body | Holds. (1) Exit 1 on `the union step passes an option with no value after it: [... '--stale-fails']`. (2) Exit 0, 1 passed: the old reader let the flag through, so the failing line in (1) is the new guard's (`executed`) |
| A macOS entry carrying a split is refused | `trail/phases/phase-5.md` *Seen red*, the first two items | HEAD's `test.yml` with `split: "--splits 3 --group 1"` given to the one `macos-latest` entry, then the shard module | Holds. `test_every_group_of_each_sharded_leg_runs_exactly_once` failed at the assertion that no entry outside `SHARDED` carries a split, listing the macOS entry (`executed`) |
| S6: the tree holds no durations file, and `.gitignore` keeps it out | `frame/design.md` S6; `trail/phases/phase-4.md` *S6* | `git ls-files .test_durations`; `git check-ignore -v --no-index .test_durations` | Holds. No line, and `.gitignore:23:/.test_durations` (`executed`) |
| S10: `test.yml` names no run | `frame/design.md` S10; `trail/phases/phase-5.md` *S10* | `grep -c -E '[0-9]{11}' .github/workflows/test.yml` at HEAD and at `1a01c761a` | Holds. 0 at HEAD, 14 at the base, the count the design and the changelog give. The matrix holds ubuntu 5 and 5, one `macos-latest` entry at 10 and four Windows shards at 10 (`executed`, `read`) |
| Run 42996432567's job times and conclusion | `trail/phases/phase-5.md`, the job table | `gh run view 42996432567 --json conclusion,headSha,event,jobs` | Holds. success, `workflow_dispatch`, head `25133f410`. ubuntu 116 s and 87 s, macOS 199 s, Windows 104, 145, 244 and 147 s, `durations` 11 s, `release-report` skipped (`executed`) |
| A shard's stored part holds only its own cases, though a restored union stands at the root when it runs | `.github/workflows/test.yml`, the comment above the part upload; `frame/design.md` *Scope* item 5 | Read `pytest_split/plugin.py#pytest_sessionfinish` of pytest-split 0.11.0 | Holds. Under `--clean-durations` the plugin writes `dict(test_durations)` of the session alone and does not merge the restored file (`read`) |
| Each `## Removes` row and each removal the changelog names stands nowhere in the tree | `frame/design.md` `## Removes`; `changelog.md` | `git grep` outside `seal/threads/` for `STALE_SHARE`, `REMEDY`, `Staleness`, `staleness`, `--committed`, `stale-fails`, and in `durations_union.py` for `verdict`, `stale` and `committed`. `git grep -w` over `tests`, `.github` and `CONTRIBUTING.md` for the walker's names, the conftest readers, `job_steps`, `step_fields`, `job_keys`, `ASK_THE_VERDICT`, `DURATIONS`, `suite_seconds`, `job_block`, `keyed_under_env`, `workflow_settings` and the four old install functions. The `.test_durations` export rule; `durations refresh` and the refresh recipe's and removed cases' names; `test_durations` in the three census files; `test_conftest` in `LINKED`; the macOS split entries | Holds. The only hits are unrelated `verdict` functions in other files, `hygiene_step`, which stays as a name and reads `load(HYGIENE)` (`read`, `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py:21-29`), and `DURATIONS` as a docstring parameter in `tests/github/test_release_report.py:42`. `durations_union.py` holds none of the three words (`executed`) |
| The checklist sentence `## Rule changes` removes stands as its `from:` text | `frame/design.md` `## Rule changes` | Whitespace-normalised containment of the `from:` text in `docs/releasing/release-checklist.md` | Holds. Found at `:139-148`. The sentence stays in the tree until the settle, as `skills/implement/SKILL.md` *Document layout* gives a work item whose subject is the code (`executed`, `read`) |

Not re-run, each `unverified` with its answerer, as `gaps.md` *Not
verified* names it:

- A Windows shard restoring a union an ubuntu job saved on `main`
  (`frame/questions.md` Q1, S1). The orchestrator answers it from the
  restore step's log in the first pull request run after a push run on
  `main` with this workflow. The changelog's sentence "Each Windows shard
  restores the newest such key before it divides" describes what the
  workflow's step is written to do. It is read as that, and this hit is not
  yet observed.
- `release-report`'s two downloads, which the orchestrator answers from the
  0.37.4 release pull request's run.
- `publish-release.yml`'s `seal` job installing `PyYAML==6.0.3`, which the
  repository owner answers at the 0.37.4 tag's run.

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| The design (`frame/design.md`, `frame/plan.md`) | The committed file leaves, and the union lives in `actions/cache`, saved on runs that are not a pull request's and restored by the split entries. The age verdict goes. The release table reads run artifacts. PyYAML 6.0.3 is pinned, and `tests/workflows.py#load` with `BaseLoader` is the one reading of a workflow. `test.yml` names no run, its timeouts are 5, 5, 10 and 10, and macOS runs as one job. Gate change: allow more, prompt budget zero | The issue's two *Decisions*. Each *Done when* item: no `.test_durations` (S6 above); no run fails on a file's age (no `--stale-fails` and no age code, above); the checklist's refresh sentence goes through `## Rule changes`, the route `skills/implement/SKILL.md` *Document layout* gives code-subject work; the slowest Windows shard before (200 s median, 242 s max) and after (244 s, count split, with Q2 naming the balanced reading); no run id and recomputed timeouts. The tree's restore, union, upload and save steps are *Data & interfaces*' text (`read`, the diff of `test.yml`) | None |
| The build (the diff, `trail/phases/phase-1.md` to `phase-5.md`) | Five phases. Each record states its departures from the frame with grounds, and the orchestrator's folds carried each into the frame (`40a47e18f`, `1af6425ce`, `bf15c27a1`, `a0c2b1a39`, `98b475f64`, `237d75ac5`) | The design as folded. Every phase whose *Phases* Status cell holds a commit has its record, five of five, as `routing.md`'s `Implementation` row `crafter` asks (`read`). The sampled `seen red` and `executed` claims re-ran as recorded | None |
| The last round (`trail/rounds/round-2.md`) | Round 1's three fixes stand. One `should` finding located in `frame/plan.md` alone was `fixed a969da80c` | The tree. `a969da80c` touches `frame/plan.md` alone and `3ee85274f` touches `round-2.md` alone (`executed`, `git show --stat`). Read as the fix pass's claim with the sealer as its reader: the plan at HEAD holds the #1481 row the finding asked for, and the sentence "meets nothing here" is gone (`executed`, `grep` exit 1; `read`, `frame/plan.md` *Overlap with the release*) | None |
| The changelog (`changelog.md`) | Four items: no run red on a file's age, the union in the cache, and the settle clause gone; the release table from artifacts; the suite reads workflows through PyYAML; `test.yml` names no run, and macOS is one job | The tree and the run: 14 run-id lines at the base; 15, 15, 15 and 20 minutes at the base; 199 s and 244 s in run 42996432567; six red runs, the issue's five and 42714377663; the settle clause removed at `skills/settle/SKILL.md:233` (`read`, `executed`) | None. The restore sentence is a description of the step, and its hit is the `unverified` row above |
| The orchestrator's part of the pull request body (`pr.md`) | Four quotes and `Closes #1486` | Each quote stands word for word at its coordinate: *Alternatives considered* row A, and *Judgments of the run* rows 2, 3 and 5 (`read`). The gate-change quote matches the base, where `durations_union.py` returned 1 under `--stale-fails` (`read`, `git show 1a01c761a:.github/scripts/durations_union.py`, `:322`, `:368`) | None |
| `routing.md` *Why this way*, the orchestrator's choice under `agentic` | Framer, crafter, the review chain and automation, on the grounds that the change rewrites CI steps and the test runner's environment | The diff: workflows, `run_tests.py`, the test modules and `CONTRIBUTING.md`. The one shipped-skill edit, the clause in `skills/settle/SKILL.md`, was added by round 1's finding and read by round 2, and the route chosen is the fullest one. The grounds understate nothing that a lighter route would have skipped (`read`) | None |

```seal
target: 1a9a7a44d09ef8b727d305f24dcb72610030432e against 1a01c761ab6189af458c11e0cd8339edea9f21ff
Verdict: sealed
```

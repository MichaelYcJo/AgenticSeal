# Implementation Plan: the suite runs on Python 3.14 (#1065)

## Technical context

The base tree is `release/v0.32.5` at `a73e0b8c`, with `routing.md` on top at `e925d585` (the spawn's fact, executed by the orchestrator; `git log --oneline -3` here shows the same). A G-number is a row of `frame/design.md` *Grounding*, and a Scope number an item of its *Scope*.

- At that base, `.github/workflows/test.yml#pytest` holds eight `include:` entries at 3.12 that share one set of steps. `durations` and `release-report` need the job, and `fail-fast` is `false` (`frame/design.md` G5).
- `tests/text/test_ci_gives_the_checks_what_they_need.py#matrix_include_entries` is the suite's one reader of the entries. It requires `include:` to be the matrix's only key and each entry to be a one-line flow mapping. So a leg is added as one more entry, and a per-entry condition such as `if:` or `exclude:` is not available to it.
- `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py#test_ci_runs_the_suite_at_the_floor_the_runner_holds` turned red at that base on any entry above the floor, and Scope 2 rewrites it.
- `.github/scripts/release_report.py#leg_minutes` keys a leg by operating system alone (`frame/design.md` G9).
- The leg runs where every other `pytest` leg runs: on each `pull_request`, on a push to `main`, and on `workflow_dispatch`, which the orchestrator uses before the pull request opens (G10).

**The chosen approach's failure scenario, six months on.** A Python 3.14 behaviour that only Windows or macOS shows reaches a user, because the 3.14 leg runs on ubuntu alone. That kind of change exists: `ntpath.isabs('/x')`, Windows' `os.path.isabs`, is `True` on 3.12.9 and `False` on 3.13.5 and 3.14.4 (executed with each local interpreter, 2026-11-05), and the ubuntu leg runs `posixpath`. Or 3.15 changes something the suite meets, and nothing runs 3.15 until somebody adds it, which is `questions.md` Q1. Or the 3.14 leg turns red on a pull request that changed nothing interpreter-related, because a 3.14 patch release moved a message the suite pins. That pull request's work item then repairs it (G10), at the cost of one fix commit in a work item it does not belong to. `"3.12"` already floats over patch releases the same way.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. One more `include:` entry in the `pytest` job, ubuntu, 3.14, on every event the workflow runs on | *Technical context* above. Cost: one ubuntu job of about 2 minutes per run, which ends before the slowest Windows shard, and the run drops from 13 jobs to 12 (G6) | **Chosen.** One set of steps serves every leg, and the existing shard and timeout cases hold the new entry's shape (G7, G8) |
| B. A job of its own, as `arms-grammar` was, running the whole suite on 3.14 | It copies the `pip install` line with its three pins, the `git config` step and the `pytest` line with its report flags. A pin moved in `run_tests.py` is then held against two lines, and a flag added to one `pytest` line and not the other leaves one leg's log naming less. This replaces the single-matrix structure, and it is weighed as an equal of keeping it. Keeping it stands on one premise, checked: an entry with no `split` and no `store` runs the steps unchanged (G7) | Rejected: the copy is the cost, and it buys nothing A lacks |
| C. 3.14 only on pull requests into `main` | Needs a separate job (B), because an `if:` on the job applies to every entry. A 3.14 defect one work item brings in is found at the release pull request, after that item was sealed and merged, and is repaired in a work item it does not belong to. That contradicts G10 and the owner's rule that a defect is fixed where it arises. It saves about 2 runner-minutes per run and no wall clock (G6) | Rejected |
| D. A scheduled or dispatch-only run | A red nobody's pull request owns, read when somebody remembers. The same costs as C, with no owner | Rejected |
| E. A non-blocking leg (`continue-on-error: true`) | A red that does not stop a merge is a red that merges. Q3 of 1790690762 put it as "a warning can be ignored" (G3) | Rejected |
| F. 3.14 on all three systems | Seven more jobs, four Windows shards of 2.4 to 4.1 minutes and three macOS shards of 1.0 to 1.9 minutes (G6), so 19 jobs per run. The interpreter dependence this issue is about, #684's `ast` node types and the census lists, does not depend on the system. The system dependence is covered by the floor legs | Rejected for this item. Its failure scenario is the chosen approach's first one |
| G. Keep a 3.13 leg beside 3.14, as `arms-grammar` had | One more job. 3.12 and 3.14 bracket 3.13, and a removal in 3.13 is still absent in 3.14. So a module red only on 3.13 needs a behaviour 3.13 alone has | Rejected. The failure scenario is that such a behaviour exists and a 3.13 user meets it |
| H. A floating `"3.x"` leg | A pull request's verdict changes with no commit on the day a new Python ships, and every record here binds a verdict to a commit. That is 1790690762's plan alternative H (G3) | Rejected |
| I. 3.15 in place of 3.14, or beside it | 3.15.2 is stable in `actions/python-versions` (executed: its `versions-manifest.json`, 2026-11-05). `cmarkgfm==2025.10.22` has no `cp315` wheel on PyPI (executed), so a 3.15 leg builds it from source on every run, against a pin `run_tests.py` chose for having a wheel everywhere. The owner named 3.14 (G1) | Not this frame's to decide: `questions.md` Q1. The build proceeds on 3.14 |
| J. Shard the 3.14 leg | It runs the whole suite in about 2 minutes (G6), and shards would read `.test_durations`, which prices cases on Windows. The ubuntu floor leg stays one job for the same reason (`test.yml`'s comment, "ubuntu stays one job") | Rejected |
| K. Release table: leave `leg_minutes` summing every ubuntu job | At 0.32.5 against v0.32.4 the `ubuntu` row roughly doubles, and the new leg's cost cannot be read apart from the floor leg's. G4 needs that cost readable for the leg to be kept or dropped later | Rejected |
| L. Release table: key every leg as `<os> <python>`, the three fixed rows included | Every row's label changes, and a leg absent from both job lists no longer prints its `no run found` row, which `Test_main` pins today. When the floor moves, all three rows split into two half-empty rows | Rejected in favour of Scope 4, which keeps the three rows for the floor and adds rows for other Pythons |
| M. A case that requires a 3.14 entry in the matrix | A copy of `test.yml` beside it, which goes stale the day the leg moves to 3.15. `docs/releasing/branch-and-release.md` gives the same reason for not requiring a `pytest` check name, and `skills/core/SKILL.md` *The rule a mechanism is kept against* says nothing is kept beside the tree to stay in step with it. The workflow file is the one source | Rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope 1, 2, 3 | `bin/test tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py tests/text/test_ci_gives_the_checks_what_they_need.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/behaviour/test_release_hygiene.py -q` green. The rewritten case shown red as Scope 2 says, and how, in `trail/phases/phase-1.md` | 0cc0ae23 |
| 2 | Scope 4 | `bin/test tests/github/test_release_report.py tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py -q` green. The new case shown red against the old `leg_minutes`, in `trail/phases/phase-2.md` | 6100c089 |
| 3 | Scope 5. The orchestrator pushes the branch after phase 2 closes, runs `gh workflow run tests --ref test/1065-the-suite-has-not-run-on-3-14`, and spawns this phase with the run id. The crafter reads the run with `gh run view` and `gh api`, writes the observation, repairs each red, and writes the run into `test.yml`'s comment. Where it repaired something, the orchestrator dispatches again at the repair's commit and the crafter adds that run to the record | The dispatched run's `pytest (ubuntu-latest, 3.14, 15)` job concludes `success` at the phase's last commit. Each repaired module's narrow run is green locally. `trail/phases/phase-3.md` names each run id, its commit, and the counts | |

## Operational impact

- One more CI job on every `tests` run. It needs no secret, no new dependency and no ruleset change, and it is not a required check (G11).
- `setup-python` resolves `"3.14"` to the newest 3.14 patch release on each run, as `"3.12"` resolves today.
- The release table for 0.32.5 shows a `` `ubuntu 3.14` leg (minutes) `` row reading `no run found` at v0.32.4. That is the new leg, not a regression, and whoever weighs the table reads it so.
- No migration, environment variable or compatibility break. The plugin's floor stays 3.12.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-05 | Folded phase 1's contradicted statements: design *Grounding* is labelled as the tree at `a73e0b8c`, *Technical context*'s two bullets on the matrix and the floor case say "at that base", and G12's package-index URL is written in words | At HEAD the matrix holds a 3.14 entry and the floor case reads each operating system, so the base's description needs its label; the URL's domain failed `tests/test_censuses.py`'s real-identifier census. A frame change is the orchestrator's to fold from the crafter's account | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-05 | Phase 1 builds on `frame/questions.md` Q1's default, 3.14; the owner was told the question and the default after routing | Routing is Automation yes, so no question to a person follows the routing answer; changing the version later is one matrix line | `skills/core/SKILL.md` *The first value: efficient development through the workflow*, the invariants table's routing row |

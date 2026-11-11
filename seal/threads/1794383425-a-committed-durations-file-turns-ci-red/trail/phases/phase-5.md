# Phase 5: 1794383425-a-committed-durations-file-turns-ci-red

## What this phase found

**The frame holds for this phase, with two corrections.** Each coordinate *Scope* item 8 and S10 name was opened at `a0c2b1a39` before the build (read).

- `frame/design.md` *Out of scope* keeps `tests/conftest.py#posix_id` because it keeps a reason. The reason its docstring gave was that the union is measured on Windows and read on every sharded leg. That reason ended when macOS became one job. The union is now measured and read on the Windows leg alone, so an id written with `\` would be priced the same way on both sides. The docstring now states what remains: a case has one id on every system, and `repo_relative` writes a path with the function. The one `ids=posix_id` parametrization, `tests/behaviour/test_the_contributor_has_a_procedure.py:144`, stays, as *Out of scope* asks. `gaps.md` `## Not done` says so.
- `frame/plan.md` *Overlap with the release* writes the #1487 row as a merge still to come. #1487 merged into `release/v0.37.4` as #1525 (`957a3bc7d`), and this branch holds it since the merge `3ed9a1bff` (executed: `git merge-base --is-ancestor 957a3bc7d HEAD`). The before reading in `frame/design.md` *Grounding* comes from runs up to 2026-11-11 08:51, before #1525 merged, so it includes #1487's test cases. The issue puts them at 115 s on Windows. An after reading taken on this branch does not include them, so the two readings are not of one suite.

**Decisions, each judged against `frame/design.md` *Scope* item 8 and S10.**

- **The timeouts are 5, 5, 10 and 10 minutes.** The rule the comment states is 1.5 times the leg's slowest measured job, rounded up to 5. The bases are the slowest jobs in `frame/design.md` *Grounding*, over 39 runs from 2026-11-09 to 2026-11-11 (read there, measured by the framer): ubuntu 3.12 130 s, ubuntu 3.14 140 s, and a Windows shard 242 s. When the values were set, macOS as one job had no measured run, so its base is the framer's model of 222 s on the slowest run. Run 42996432567 measured it later, below. The arithmetic: 195 s, 210 s, 333 s and 363 s, rounded up to 5, 5, 10 and 10 minutes.
- **The comment states the rule and holds no measurement.** `skills/core/SKILL.md` *The rule a mechanism is kept against* says nothing is kept beside the tree to stay in step with it. A base written into the comment would age the way the run ids did. The measurement stands here instead. The comment says where a leg's minutes are read: a run's jobs, and the release table's leg rows.
- **The comment no longer cites `questions.md` Q6's rule (a) of work item 1791270165.** That work item's directory is not in the tree (executed: `ls seal/threads`), so the citation pointed at nothing. The comment states the rule itself.
- **The comment says macOS's budget was set before its one job had run, from its shards' case time plus one fixed cost.** A reader holding the rule against a measured run then knows that 10 rests on a model.
- **The sizing argument left with the run ids.** That is the 62 s and 45 s fixed costs, the 7,530 s suite, and the per-count minutes. `frame/design.md` *Removes* names those lines. What stays is the one sentence that says why a shard count matters: a shard's job is a fixed cost plus the leg's case time over the count.

**Seen red (executed).**

- `SHARDED` lost its macOS row before `test.yml` changed. `test_every_group_of_each_sharded_leg_runs_exactly_once` then failed at its line 104, `assert others and not any("split" in e for e in others)`, and the message listed the three macOS entries that still carried `split`. It passed once the workflow held one macOS entry.
- `seal mutate` on `.github/workflows/test.yml` at `60838ede9`, over `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, ran 2 mutants and both were red. Each gave the macOS entry a split, `--splits 3 --group 1` in one and `--splits 1 --group 1` in the other. The second shows that a split of one is refused too, even though it would run the whole suite.
- The other changes are prose: the `test.yml` comments, `CONTRIBUTING.md`, the comment above `PYTEST_SPLIT_VERSION` in `.github/scripts/run_tests.py`, and docstrings in `tests/conftest.py` and two test modules. Each module still imports and ran in the set below. No case reads the sentences that changed.

**S10 (executed, at `60838ede9`).** `grep -c -E '[0-9]{11}' .github/workflows/test.yml` prints 0. The matrix holds ubuntu at 3.12 and 3.14 with `timeout: 5`, one `macos-latest` entry with no split and `timeout: 10`, and four Windows shards with `timeout: 10` (read).

**The old fact's other statements (a sample).** `git grep -n -i` was run over the whole tree less `seal/threads/`, on `three shards`, `macos shard`, `macos leg`, `splits 3`, `#864`, `shards of the`, `sharded leg`, `macOS and Windows`, `Windows and macOS`, `four shards`, `15 minutes`, `20 minutes`, `timeout: 15`, `timeout: 20` and `which runs they`. A second search ran on `shard` and `timeout-minutes` over `docs`, `skills`, `agents`, `templates`, `lib`, `hooks` and the READMEs, which found nothing. Every hit that stated the macOS shards or the old sizing was rewritten:

- `CONTRIBUTING.md` *Running the checks*: the list of CI jobs, the sentence on where the timeouts come from, the restore sentence, and the paragraph saying the union divides the macOS leg too.
- The comment above `run_tests.py#PYTEST_SPLIT_VERSION`.
- The docstring of `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py#test_ci_runs_the_suite_at_the_floor_the_runner_holds`, whose example was a macOS shard.
- The module docstring of the shard module, and the docstrings of its S4 case and its interpreter-path case.
- The `pytest-split` comment in `test.yml`.

A search for wording is a sample. A sentence that states the macOS shards in other words is not reached by it.

**The phase-boundary run (executed, at `60838ede9`, clean tree).** The set was the plan row's two modules; each test file this phase changed; and each test file that reads a path it changed. Those readers are `tests/test_conftest.py`, `tests/test_censuses.py`, `tests/test_workflows.py`, `tests/github/test_run_tests.py`, `tests/github/test_release_report.py`, `tests/skills/test_deferral_check.py`, `tests/skills/test_passages.py` and `tests/skills/test_chain_check.py`, plus the tree-wide `tests/text` and `tests/behaviour`. The command was `bin/test tests/text tests/behaviour tests/test_conftest.py tests/test_censuses.py tests/test_workflows.py tests/github/test_run_tests.py tests/github/test_release_report.py tests/skills/test_deferral_check.py tests/skills/test_passages.py tests/skills/test_chain_check.py -q`. It gave 2455 passed and 8 skipped. `b858bea3a` then committed this work item's records, and `tests/text` and `tests/behaviour`, which hold every test file that walks the records directory, ran green over it (1838 passed, 8 skipped). `0cd12880c` then reworded the macOS comment in `test.yml` and two docstrings of the shard module, so that they say why macOS is one job and no longer tell its history. The modules that load `test.yml` ran green over it in one command (86 passed, 1 skipped): the shard module, `tests/text/test_ci_gives_the_checks_what_they_need.py`, `tests/behaviour/test_release_hygiene.py`, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py`, `tests/test_workflows.py` and `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`.

**This work item's CI run: run 42996432567, a `workflow_dispatch` of `tests` at `25133f410`, conclusion success.** The spawn asked this phase to push the branch and dispatch the run. Contract rule 6 withholds a push from every agent, and contract rule 2 gives the full suite to the orchestrator, so the phase declined both. The orchestrator pushed the branch at `25133f410` and dispatched the run. Each time below runs from a job's `startedAt` to its `completedAt`. The orchestrator measured them, and this phase measured them again with `gh run view 42996432567 --json jobs` (executed). The `pytest` time and the case counts come from each job's log, read with `gh run view 42996432567 --log` (executed).

| Job | Time | Timeout | pytest's summary line |
|---|---|---|---|
| lint | 8 s | none | none |
| ubuntu 3.12 | 116 s | 5 min | 5820 passed, 8 skipped in 102.01 s |
| ubuntu 3.14 | 87 s | 5 min | 5819 passed, 9 skipped in 74.63 s |
| macOS 3.12, one job | 199 s | 10 min | 5820 passed, 8 skipped in 177.82 s |
| Windows group 1 | 104 s | 10 min | 1441 passed, 16 skipped in 70.13 s |
| Windows group 2 | 145 s | 10 min | 1456 passed, 1 skipped in 112.94 s |
| Windows group 3 | 244 s | 10 min | 1440 passed, 17 skipped in 216.74 s |
| Windows group 4 | 147 s | 10 min | 1457 passed in 119.04 s |
| durations | 11 s | 5 min | none |

Every job finished inside its timeout. The four Windows groups ran 5794 passed and 34 skipped between them, 5828 cases in all. That is ubuntu 3.12's 5820 passed and 8 skipped, so the parts made the whole suite (read off the summary lines).

The run exercised the following cache steps, from its step conclusions and logs (executed):

- A `workflow_dispatch` run is no pull request's. Each Windows shard ran `actions/cache/restore@v4`, and the step succeeded with no key matched. All four logs print `Cache not found for input keys: test-durations-42996432567, test-durations-`. Each of the four Windows logs prints `No test durations found`, so each shard split by count. That is S2.
- The macOS job and both ubuntu jobs skipped the restore step, because they carry no split.
- The `durations` job ran the download, the union with `--count 4`, the upload and `actions/cache/save@v4`, and every one of those steps succeeded. Its log prints `Cache saved with key: test-durations-42996432567-1`, which is the save half of S4. Because the run was a dispatch, the saved entry is scoped to this branch.
- `release-report` was skipped, because a dispatched run has no `base_ref`.

A restore that hits a cache is still unverified. It is `frame/questions.md` Q1, and the first pull-request run after a push to `main` answers it.

**S11, the before and after readings of the slowest Windows shard.** Before: `frame/design.md` *Grounding* gives a median of 200 s and at most 242 s, over 38 runs that a balanced union divided, taken before #1487 merged. After: 244 s, from group 3 of run 42996432567, split by count, and #1487 is merged in it. The two readings are not of one suite and not of one division. #1487 took its cases out, about 115 s on Windows by the issue's figure, and the after run divided by count, not by the union. So the after reading answers `frame/questions.md` Q2 as its default states: a count split's slowest Windows shard took 244 s, and the balanced reading waits for a run that restores a union. On the count split the four groups took 104 s, 145 s, 244 s and 147 s.

**`frame/questions.md` Q3.** macOS as one job took 199 s. Every Windows shard took 104 s to 244 s, so macOS finished inside the slowest shard by 45 s. One job stays. The framer's model estimated 160 s on the median run and 222 s on the slowest, and 199 s falls between the two.

**The macOS budget stays at 10 minutes, though this one run alone would give 5.** By the rule, 1.5 times 199 s is 298.5 s, which rounds up to 5 minutes. That is 1.5 s under the bound. The rule's base is the slowest job over several runs, because the same suite runs slower from one run to the next. One run is a thin base, and the framer's model of the slowest run, 222 s, gives 333 s and so 10 minutes. The value stays at 10, and the comment beside it still says the budget was set before the one job had run. That judgment was weighed against the rule the comment in `.github/workflows/test.yml` states. The other legs agree with their budgets on this run. For ubuntu 3.12, 1.5 times 116 s is 174 s, and for ubuntu 3.14, 1.5 times 87 s is 131 s, so both round up to 5 minutes. For Windows, 1.5 times 244 s is 366 s, which rounds up to 10.

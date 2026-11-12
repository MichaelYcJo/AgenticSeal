# Review round 2: 1794465688-feature-prs-wait-on-the-macos-runner

```seal
target: 8b3438ae4, fixes 8cca6ed80..8b3438ae4
```

This round verifies the fixes. The code it reviews is the fix diff
`8cca6ed80..8b3438ae4`, without round 1's own record. That diff holds one
code unit, the replaced refusal case in `tests/test_workflows.py`, and
changes to `frame/design.md`, `frame/plan.md`, `gaps.md` and `pr.md`. The
work item's records were read whole in round 1 at `8cca6ed80`.
`git diff 8cca6ed80..8b3438ae4` over the work item's directory shows that
only those four hunks and round 1's close blocks changed since then. Each
hunk was read against the target, so the read of the present records stands
whole at `8b3438ae4`. The facts round 1 carried from the frame (G3 to G5,
G9, G11 to G13) are carried again and not established anew. Every run was
made in a `git clone --no-local` of the repository at `8b3438ae4`, under
this round's scratch directory.

## Findings

### 1. The *Removes* sentence still counts one `Test_pytest_jobs` case, and the class holds two

```seal
severity: should
location: `seal/threads/1794465688-feature-prs-wait-on-the-macos-runner/frame/design.md:94`
evidence: read `seal/threads/1794465688-feature-prs-wait-on-the-macos-runner/frame/design.md:94`, `tests/test_workflows.py:102-136`
reopens: round-1#4
```

Why it matters: round 1 finding 4 was that this sentence counted fewer
cases than the build adds. The sentence is the answer to `CONTRIBUTING.md`
*What a change to a gate must carry*, and the sealer and the settle read
it. The close at `1f5944325` applied round 1's snippet word for word.

That snippet rested on finding 1's fix removing a case. It says "With
finding 1 applied, the work adds two cases." The fix pass did not remove
the case; it replaced it, on grounds this round confirms below. So
`tests/test_workflows.py#Test_pytest_jobs` holds two cases at `:103` and
`:116`, and the sentence's "with the case of
`tests/test_workflows.py#Test_pytest_jobs` that holds it" names one. The
plan row that `1f5944325` added says the sentence now states what the build
adds "without a count of cases". The singular "the case" is still a count.
The defect the finding named still stands in the unit that commit changed,
so this finding reopens it.

```markdown
This work adds a CI job, its condition, the case of *Scope* item 3, and `tests/workflows.py#pytest_jobs` in the place of `tests/text/test_ci_gives_the_checks_what_they_need.py#runs_pytest`, with the cases of `tests/test_workflows.py#Test_pytest_jobs` that hold it. In return it removes the two legs from every pull request into `release/*`.
```

```seal
verdict: fixed f46ec0b0f
answer: The framer folded the sentence and the orchestrator committed it at f46ec0b0f. That commit changes `frame/design.md:94` to the finding's snippet word for word: "with the cases of `tests/test_workflows.py#Test_pytest_jobs` that hold it", which matches the two cases at `tests/test_workflows.py:103` and `:116`. It also adds a judgment row to `frame/plan.md`. This fix pass made no change for this finding (read).
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the duplicate case is gone. The departure from round 1's
snippet is grounded. `skills/verify/scripts/test_layout.py:30` refuses a
class that lacks a `test_refuses_` case, so removing the case alone would
have made `seal layout --check` refuse `Test_pytest_jobs` (read). The
replacement, `test_refuses_a_job_whose_script_names_a_plugin_or_a_file_of_pytest`
at `tests/test_workflows.py:116-136`, is a new unit, and it was reviewed as
code. It holds the word boundary of `RUNS_PYTEST` at `tests/workflows.py:59`,
and no other case of its group holds that boundary. With the lookbehind
dropped, and separately with the lookahead dropped, `tests/test_workflows.py`,
`tests/text` and the two behaviour modules that read `pytest_jobs` ran 456
cases. In each run this case was the only one that failed (executed). Its
docstring says what the fixture holds: `pytest-xdist` and `pytest-split`
stand on `test.yml:124` beside `pytest`. The first case's docstring now
names the two decoys that its equality at `:113` refuses. The module
passes, and ruff's check and format pass on it (executed).

```seal
confirms: round-1#2
```
What holds: the row of `frame/plan.md` *Judgments of the run* takes
`refactor:`. It stands on the table's example "a gate retired because what
it caught did not outweigh its cost", and it drops the issue's prefix as a
ground. The section it cites, *Commit messages*, holds the table
(`skills/commit-pr-convention/SKILL.md:125-217`). `pr.md:5` quotes "The
title takes `refactor:`", word for word as the row says it (read). Issue
#1516's title now opens with `refactor:` (executed,
`gh issue view 1516 --json title`).

```seal
confirms: round-1#3
```
What holds: `gaps.md:9` names a `workflow_dispatch` run of `tests` on this
branch, before the merge, as the answer. It keeps the step half on jobs
130936327013 and 130936327217 of run 43143655875, which round 1 opened. It
keeps actionlint's report beside the statement that actionlint is no check
of this repository (read). Dispatch run 43175185653 is the orchestrator's
to read, and this round did not open it.

What matched: the second row `1f5944325` added to *Judgments of the run*
cites `skills/implement/fold-and-reframe.md`, and that file stands in the
tree and in the installed plugin (executed). Nothing else in the fix diff
contradicts `gaps.md` *Not done*, `changelog.md` or `routing.md`, and
nothing else there contradicts the target (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| What dispatch run 43175185653 shows: the alias read, and `pytest-wide`'s check names | `gaps.md:9` | the orchestrator |
| Whether this pull request's first `pull_request` run skips `pytest-wide`, and under which name | `frame/questions.md` Q1, `gaps.md:8` | the orchestrator |
| The suite, the repository-wide lint and the format check at HEAD | `gaps.md:7` | the orchestrator's broad gate |

## Probes

| Command | Result |
|---|---|
| `RUNS_PYTEST` at `tests/workflows.py:59` edited to `r"pytest(?:\s\|$)"`, then `bin/test tests/test_workflows.py tests/text tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py -q` | exit 1: only `test_refuses_a_job_whose_script_names_a_plugin_or_a_file_of_pytest` failed; 455 passed, 1 skipped |
| `RUNS_PYTEST` edited to `r"(?<![\w.-])pytest"`, the same command | exit 1: the same one case failed; 455 passed, 1 skipped. The file was restored with `git checkout -- tests/workflows.py`, and the clone's status was clean afterwards |
| `bin/test tests/test_workflows.py -q` | exit 0: 6 passed |
| `uvx ruff check tests/test_workflows.py`; `uvx ruff format --check tests/test_workflows.py` | exit 0 and exit 0 |
| `bin/seal layout --check tests/test_workflows.py` | exit 0, with the one report round 1 saw: `job_scripts` has no class `Test_job_scripts` |

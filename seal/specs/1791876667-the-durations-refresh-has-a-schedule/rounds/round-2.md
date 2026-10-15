# 1791876667-the-durations-refresh-has-a-schedule — review round 2

| Field | Value |
|---|---|
| Target SHA | 5456402900bdf3316c0eef51cc659c574a11519b |
| Written late | no |
| Ran by | warden on Opus 5.5 |
| PR | 937 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | `b4a327f6ec31541ae1cc86c78717ddb6baf982d5..b4a327f6ec31541ae1cc86c78717ddb6baf982d5`, 0 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | first — 🟡 5 at tests/test_ci_gives_the_checks_what_they_need.py#runs_pytest, a unit round-1's fixes added |
| Needs a fix | no |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 2 of #931 against 54564029: the verifying round over round 1's fix pass (b16bee7f..524c9783). Open each fix against its finding, check that the fix pass introduced nothing new, and check the re-stamped claims.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 1's finding 1 is closed — parts and union kept seven days and uploaded with `overwrite: true` | `.github/workflows/test.yml:168-177` | confirmed | read at ef894749: both uploads carry both keys; T3 and T10 assert them; the comment states the re-run reason |
| 🟢 | round 1's finding 2 is closed — `REMEDY` and the recipe name `gh workflow run test.yml --ref <branch>` | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:279-288`, `CONTRIBUTING.md:215-218` | confirmed | read at 6787cd3e: T8 and T11 assert the sentence; the `gone` tuple now holds a phrase of the old measuring recipe |
| 🟢 | round 1's finding 3 is closed — pytest read as a word on every code line but `needs:` | `tests/test_ci_gives_the_checks_what_they_need.py#runs_pytest` | confirmed | executed: over every workflow the guard selects the same three jobs and not `test.yml:durations`; the four spellings round 1 named are selected |
| 🟢 | round 1's finding 4 is closed — a `--count` below one is a refusal | `.github/scripts/durations_union.py:234-235` | confirmed | read at 91e383a8: raised before `find_parts`, exit 2, no file written; the case covers 0 and -1 |
| 🟡 5 | a block-list `needs:` (`- pytest` on its own line), a step `name:` and an `env:` value containing pytest each make `runs_pytest` select a job that runs nothing | `tests/test_ci_gives_the_checks_what_they_need.py#runs_pytest` | answered | the shapes it names (a block-list `needs:`, a step `name:`, an `env:` value) make `runs_pytest` select a job that runs nothing, which errs toward refusing a shallow checkout and never toward silence; the base's substring rule had the same reach; no job in the tree has the shape, and #930's `budgets` job uses the one-line `needs: pytest` the guard already skips; widening the reader would add a mechanism for a shape nobody writes, against the owner's rule to subtract rather than add; executed: the block-list shape through `shallow_pytest_jobs` returns the job; fails toward refusing, the base's rule had the same reach, and no job in the tree or at PR #938's head has the shape |
| ⬜ 6 | the re-stamped S1 claim and the changelog state that a re-run's part replaces its first, which is the open ❓ rather than a verified fact | `seal/ledger/1791876667-the-durations-refresh-has-a-schedule.md` | answered | executed by the orchestrator: run 38496738041, attempt 2, re-ran `pytest (windows-latest, …, --group 1, …)` alone, and attempt 2's `durations` job re-ran and succeeded, so a part uploaded under the name attempt 1 used, with `overwrite: true`, is accepted and read; the statement holds as written; read: the evidence is the `overwrite: true` key and the action's README; whether an earlier attempt's artifact is visible to the action is unanswered |
| carried | round 1's ❓, whether `upload-artifact@v4` refuses a name an earlier attempt of the same run uploaded | `.github/workflows/test.yml:168-177`, `.github/workflows/test.yml:203-210` | deferred PR #937 | already deferred in round 1; the orchestrator answers it by a re-run on PR #937 |

## Paste-ready fixes

```python
def runs_pytest(block):
    """Whether a line of `block`'s code names pytest as a word, other than
    what its `needs:` lists (on its own line or as a block list below it) and
    a step's or job's `name:`."""
    listing = False
    for line in block.splitlines():
        if re.match(r"^\s*needs:", line):
            listing = not line.split("needs:", 1)[1].strip()
            continue
        if listing and re.match(r"^\s*-\s", line):
            continue
        listing = False
        if re.match(r"^\s*(?:-\s+)?name:", line):
            continue
        if RUNS_PYTEST.search(line):
            return True
    return False
```
```python
        "  reads-a-part:\n"
        "    needs: pytest\n"
        "    steps:\n"
        "      - uses: actions/checkout@v4\n"
        "      - run: echo needs-names-a-job\n"
        "  reads-a-list:\n"
        "    needs:\n"
        "      - pytest\n"
        "    steps:\n"
        "      - name: report the pytest parts\n"
        "        uses: actions/checkout@v4\n"
        "      - run: echo needs-lists-a-job\n"
```

## Executed probes

| What was run | Result |
|---|---|
| `tests/test_tmp_runs_pytest_reach.py`, one file, run once with `bin/test … -q -s -p no:xdist` in the review clone, then deleted: `runs_pytest` over every job of every workflow, eight block shapes, and one block-list `needs:` job through `shallow_pytest_jobs` | 1 passed, exit 0; selected `publish-release.yml:seal`, `test.yml:pytest`, `test.yml:arm-check-grammar` and no other job; shapes selected: block-list `needs:`, `name: pytest`, `name: report the pytest parts`, `env:` value `pytest`, `pip install pytest`; not selected: `needs: [lint, pytest]`, `if: needs.pytest.result …`, `name: pytest-parts`; `shallow_pytest_jobs` returned `['reads-parts']` |
| `test.yml`'s `budgets` job at PR #938's head 65e973fd, read through `gh api` | `needs: pytest` in the flow form, checkout with `fetch-depth: 0` |
| the full suite, lint and typecheck at 54564029 | not yet: the sealer's, after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `.github/workflows/test.yml:175` | round 1's 🟡 1 — fixed |
| round-1 | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:272` | round 1's 🟡 2 — fixed |
| round-1 | `tests/test_ci_gives_the_checks_what_they_need.py:325` | round 1's 🟡 3 — fixed |
| round-1 | `.github/scripts/durations_union.py:153` | round 1's 🟡 4 — fixed |
| round-1 | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` | round 1's 🟢 — confirmed |
| round-1 | `.github/scripts/durations_union.py`, `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#staleness` | round 1's 🟢 — confirmed |
| round-1 | `CONTRIBUTING.md:169`, `seal/specs/1791876667-the-durations-refresh-has-a-schedule/survivors.md` | round 1's 🟢 — confirmed |
| round-1 | `.github/workflows/test.yml:186-207` | round 1's 🟢 — confirmed |
| round-1 | `tests/` | round 1's 🟢 — confirmed |
| round-1 | `.github/workflows/test.yml:168-175`, `.github/workflows/test.yml:201-207` | round 1's ❓ — out of verified scope |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| round 1's ❓, `upload-artifact@v4` across run attempts | the orchestrator's re-run on PR #937 | the orchestrator |

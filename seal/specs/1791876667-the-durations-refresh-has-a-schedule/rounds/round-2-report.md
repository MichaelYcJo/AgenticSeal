# Round 2 report — 1791876667-the-durations-refresh-has-a-schedule (#931)

Reviewed by warden (Opus 5.5) on 2026-10-14, at 54564029, in a
`git clone --no-local` of the branch at that SHA. This is a verifying round.
Its target is round 1's fix range `b16bee7f..524c9783` (7 commits), and
`rounds/round-1.md` records those fixes as closed. The round answers two
questions. First, whether each of round 1's four findings is actually closed.
Second, whether the new units the record names (`runs_pytest`,
`shallow_pytest_jobs`, `SHALLOW_RUNNERS` and two cases) are correct as code.
Nothing outside the fix diff was re-reviewed.

## Summary

- **Round 1's four findings are closed.** Each fix does what its finding
  asked, and each has a case that pins it.
- **The widened `RUNS_PYTEST` selects no wrong job in today's tree.** It
  selects the same three jobs as before, and the `durations` job is not
  among them (executed).
- **Two shapes still reach the guard (🟡 5).** A `needs:` written as a YAML
  block list, and a step `name:` containing the word pytest, both make the
  guard read a job as running pytest. The guard fails toward refusing, and
  the base's substring rule had the same reach, so the smith can answer this
  with grounds.
- **One re-stamped claim says more than was verified (⬜ 6).** It states the
  cross-attempt `overwrite` behaviour as fact, though that behaviour is the
  open ❓.

## Round 1's findings, one by one

### 1. Parts were kept one day — closed

At ef894749, both uploads carry `retention-days: 7` and `overwrite: true`
(`.github/workflows/test.yml:176-177`, `.github/workflows/test.yml:209-210`).
The comment at lines 166–168 now gives the reason: the `durations` job reads
every part again on a re-run. T3 and T10 assert both keys. That is the fix
the finding proposed. Whether a re-run attempt can actually replace the
first attempt's artifact remains the ❓, which the orchestrator answers.

### 2. The remedy had no path for a branch without a run — closed

At 6787cd3e, `REMEDY` and `CONTRIBUTING.md:215-218` both give
`gh workflow run test.yml --ref <branch>` for a branch with no pull request
and for a run too old to re-run. T8 and T11 assert the sentence. T11's
`gone` tuple now holds `for a single run` in place of `gh workflow run`.
That phrase came from the old measuring recipe, so the guard checks a real
remnant again. The dispatch is a command a session types itself, so S7
(nothing asks a person) still holds.

### 3. The shallow-checkout guard was narrowed — closed

At a4e67849 and 24eda548, `RUNS_PYTEST` reads pytest as a word, and
`runs_pytest` skips only `needs:` lines. Comments are already stripped by
`read` and `strip_comments`, so the docstring's "comments are off" is true.

Executed with a probe: over every workflow, the guard selects
`publish-release.yml:seal`, `test.yml:pytest` and `test.yml:arm-check-grammar`.
That is the same set as before, and `test.yml:durations` is not selected.
The four spellings round 1 named are now selected, which is what
`test_a_job_that_calls_pytest_any_way_is_held_to_the_whole_history` pins.
The fixture's second job uses the flow form `needs: pytest`, and 24eda548's
commit message says why it now names pytest.

### 4. `--count 0` crashed — closed

At 91e383a8, a count below one raises `Refusal` before any part is read,
which means exit 2 and no file written. The docstring lists the new
refusal. `test_a_count_below_one_is_exit_2_naming_it` covers 0 and -1. The
crash I reproduced in round 1 can no longer be reached.

## New in the fix pass

### 5. A block-list `needs:` and a step `name:` still read as running pytest (🟡, executed)

`runs_pytest` (`tests/test_ci_gives_the_checks_what_they_need.py:330-337`)
skips the line that starts with `needs:`. YAML has a second spelling of the
same key, where the jobs follow on their own lines:

```
    needs:
      - pytest
```

The `- pytest` line is not a `needs:` line, so the word match selects it. A
probe ran the shape through `shallow_pytest_jobs` with a shallow checkout
and `run: echo union`. The result was `['reads-parts']`: the job is named an
offender although it runs nothing. The same probe selected
`name: pytest`, `name: report the pytest parts` and an `env:` value
`LEG: pytest`.

**What this costs.** The guard fails toward refusing, not toward silence. A
job written in one of these shapes is told to take `fetch-depth: 0`, which
costs it nothing. The base's substring rule selected these shapes too.

**Why it is still raised.** The block-list `needs:` is the very job shape
round 1's fix existed to stop flagging, the `durations` job written another
way. #930's `budgets` job, read at PR #938's head 65e973fd, uses the flow
form and carries `fetch-depth: 0`, so nothing near triggers it.

**How to answer.** Either the smith answers with those grounds, or the fix
below lands. Either way, this round sees nothing here that needs a fix
before the run ends.

### 6. A re-stamped claim states the re-run behaviour as fact (⬜, correction)

The fragment's re-stamped S1 now reads "kept seven days, a re-run attempt's
part replacing its first" (`seal/ledger/1791876667-the-durations-refresh-has-a-schedule.md`,
row S1). The changelog fragment says "a re-run of failed jobs replaces them,
so a partial re-run days later still has every part to union". Both rest on
the `overwrite: true` key, which T3 asserts, and on the action's README.
Whether the action sees an earlier attempt's artifact at all is the ❓ that
is still open. Until the orchestrator's re-run answers it, the claim should
say what is configured rather than what GitHub does, for example "uploaded
with `overwrite: true`".

## The other re-stamped claims

`read`: the fix pass corrected the claims of S2, S4, S6, S7 and C1. Each now
says what its fix ships, and each cites the cases that pin it. S2 cites
`test_a_count_below_one_is_exit_2_naming_it`, and C1 cites the new fixture
case. The eleven `Re-read ·` rows and the `Corrected · S5` row changed only
their anchor hashes, `CONTRIBUTING.md#"## Running the checks"@9150364b` and
`.github/workflows/test.yml#"pytest:"@2223784d`. I did not re-hash them
myself. The orchestrator's `evidence-check --strict` exit 0 at 54564029 is
what says they match, and I carry that rather than re-establish it.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 1's finding 1 is closed — parts and union kept seven days and uploaded with `overwrite: true` | `.github/workflows/test.yml:168-177` | confirmed | read at ef894749: both uploads carry both keys; T3 and T10 assert them; the comment states the re-run reason |
| 🟢 | round 1's finding 2 is closed — `REMEDY` and the recipe name `gh workflow run test.yml --ref <branch>` | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:279-288`, `CONTRIBUTING.md:215-218` | confirmed | read at 6787cd3e: T8 and T11 assert the sentence; the `gone` tuple now holds a phrase of the old measuring recipe |
| 🟢 | round 1's finding 3 is closed — pytest read as a word on every code line but `needs:` | `tests/test_ci_gives_the_checks_what_they_need.py#runs_pytest` | confirmed | executed: over every workflow the guard selects the same three jobs and not `test.yml:durations`; the four spellings round 1 named are selected |
| 🟢 | round 1's finding 4 is closed — a `--count` below one is a refusal | `.github/scripts/durations_union.py:234-235` | confirmed | read at 91e383a8: raised before `find_parts`, exit 2, no file written; the case covers 0 and -1 |
| 🟡 5 | a block-list `needs:` (`- pytest` on its own line), a step `name:` and an `env:` value containing pytest each make `runs_pytest` select a job that runs nothing | `tests/test_ci_gives_the_checks_what_they_need.py#runs_pytest` | open | executed: the block-list shape through `shallow_pytest_jobs` returns the job; fails toward refusing, the base's rule had the same reach, and no job in the tree or at PR #938's head has the shape |
| ⬜ 6 | the re-stamped S1 claim and the changelog state that a re-run's part replaces its first, which is the open ❓ rather than a verified fact | `seal/ledger/1791876667-the-durations-refresh-has-a-schedule.md` | open | read: the evidence is the `overwrite: true` key and the action's README; whether an earlier attempt's artifact is visible to the action is unanswered |
| carried | round 1's ❓, whether `upload-artifact@v4` refuses a name an earlier attempt of the same run uploaded | `.github/workflows/test.yml:168-177`, `.github/workflows/test.yml:203-210` | deferred PR #937 | already deferred in round 1; the orchestrator answers it by a re-run on PR #937 |

## Executed probes

| What was run | Result |
|---|---|
| `tests/test_tmp_runs_pytest_reach.py`, one file, run once with `bin/test … -q -s -p no:xdist` in the review clone, then deleted: `runs_pytest` over every job of every workflow, eight block shapes, and one block-list `needs:` job through `shallow_pytest_jobs` | 1 passed, exit 0; selected `publish-release.yml:seal`, `test.yml:pytest`, `test.yml:arm-check-grammar` and no other job; shapes selected: block-list `needs:`, `name: pytest`, `name: report the pytest parts`, `env:` value `pytest`, `pip install pytest`; not selected: `needs: [lint, pytest]`, `if: needs.pytest.result …`, `name: pytest-parts`; `shallow_pytest_jobs` returned `['reads-parts']` |
| `test.yml`'s `budgets` job at PR #938's head 65e973fd, read through `gh api` | `needs: pytest` in the flow form, checkout with `fetch-depth: 0` |
| the full suite, lint and typecheck at 54564029 | not yet: the sealer's, after the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| round 1's ❓, `upload-artifact@v4` across run attempts | the orchestrator's re-run on PR #937 | the orchestrator |

## Paste-ready fixes

### 5 — skip what `needs:` lists and what a `name:` says

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

Needs a fix: no

Loses a record or crashes: no

The broad gate has come due once 🟡 5 is answered, with grounds or the fix
above. Nothing this round found needs a fix before then, so what comes due
is the sealer's spawn. ⬜ 6 closes at the run's end.

## Proof

Files opened in the review clone at 54564029: the diff
`b16bee7f..524c9783` of `.github/scripts/durations_union.py`,
`.github/workflows/test.yml`, `CONTRIBUTING.md`,
`tests/test_ci_gives_the_checks_what_they_need.py` and
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`; the
word diff of `seal/ledger/1791876667-the-durations-refresh-has-a-schedule.md`
and `seal/specs/1791876667-the-durations-refresh-has-a-schedule/changelog.md`
over the same range; `tests/test_ci_gives_the_checks_what_they_need.py`
for `strip_comments`, `read` and `jobs`; `rounds/round-1.md` (first 80
lines). Read through `gh api`: `test.yml` at PR #938's head 65e973fd, the
`budgets` job. Not opened: `rounds/round-1-fixes.md`, if one exists, and the
phase records.

# Round 4 report — 1791876667-the-durations-refresh-has-a-schedule (#931)

Reviewed by warden (Opus 5.5) on 2026-10-15, at 25728e2c, in a
`git clone --no-local` of the branch at that SHA, against
`origin/release/v0.22.0` at 5b1f6fae (the remote's tip, read with
`git ls-remote`; the merge base of the branch is that commit). This is a
verifying round: its target is round 3's fix range
`5c93835e..2ce9df33` (e16fcabb, fae2679c, 2ce9df33) and the PR body, and
round 3's verdicts were read for coordinates only. Round 3's notes ⬜ 3
and ⬜ 4 are carried open to the run's end and are not reported again.

## Summary

Both of round 3's 🟡 hold on this tree, and one sentence the second fix
wrote is wrong.

- **Round 3's 🟡 2 holds (executed).** `slow-file` is a `report` row, the
  case that pins it goes red when the row is set back to `gate`, and the
  PR body's 20 `Budget removed:` lines take the checker to exit 0. The
  union refresh that round 3 saw fail on the unlisted
  `tests/test_worktree_guard.py` now holds.
- **Round 3's 🟡 1 holds in the recipe (executed).** On round 3's union,
  the checker without the flag names level 1136. With
  `--restate-price` it writes 1136, changes one line of
  `seal/budgets.md`, and the run with the PR body is exit 0.
- **The failing case's message gives a command that cannot run (🟡 1,
  new).** `REMEDY` says `budget_check.py --restate-price` with no
  `--baseline`. Typed as given, the checker refuses it with exit 2. The PR
  body and the work item's changelog both say the message gives the
  `--baseline origin/<base>` form.
- **🟡 1 sits in a unit round 3's fixes changed.** `REMEDY` was edited by
  2ce9df33. A trial of `round-record new` on this report in the round's
  clone wrote `Fix of a fix | second — 🟡 1 at …#REMEDY`, which under
  `skills/code-review/orchestration.md` §*A fix of a fix twice sends the
  work item back to its framer* stops the fix passes. It is reported at
  the severity found; what the count does to the run is the
  orchestrator's to apply.
- Three notes: the level is computed by one expression written twice
  (⬜ 2); another live work item's spec still says `slow-file` gates
  (⬜ 3); the PR body says "eight refreshes" where round 3 measured eight
  pairs (⬜ 4).

## 1. The flag is the one writer and computes the check's number

**Read.** `## Price level` is written in one place in the tree:
`restate_price` at `.github/scripts/budget_check.py:1439`. A
`git grep` for the table's title and header in every script and workflow
outside `tests/` finds the reader, the message and this writer, and
nothing else.

The number it writes is `seconds(base_level * ratio)` at
`.github/scripts/budget_check.py:1396`, from the same `base_level` and
`ratio` that `price_problems` turns into its demand at
`.github/scripts/budget_check.py:1423`. Both values come from the one
call of `price_level` above them, so the two numbers cannot differ
today. They are two copies of one expression, though, and not one
source: a later change to the rounding in `price_problems` leaves the
writer writing a level the check then refuses. That is ⬜ 2.

**Executed.** In the round's clone, run 38655519975's union over
`.test_durations` (the artifact round 3 used):

| Command | Exit | What it said |
|---|---|---|
| `budget_check.py --baseline 5b1f6fae` | 1 | level 1132 x 1.003 = 1136, plus the 20 removals with no body |
| `budget_check.py --baseline 5b1f6fae --restate-price` | 1 | "`--restate-price` wrote 1136 per mille"; `git diff` shows one line of `seal/budgets.md`, 1132 to 1136; the 20 removals remain, as no body was given |
| the same check after the write, with the PR body through `--pr-body-env` | 0 | `suite-seconds` 7,132 of 9,185; `tests/test_worktree_guard.py` printed, not failed |

So the flag writes exactly what the check demands, and the commit it
produces passes the hygiene step's command with this body.

## 2. Whether adding a flag in a fix pass oversteps

**It does not.** Round 3's 🟡 1 left two forms open: tell the person to
copy the number out of the failing output, or write it. The first form
stops for a person on every refresh, and `CLAUDE.md` §*The goal a design
is chosen against* names that as the more expensive design. The flag
costs one function that reuses the table walker the reader already uses,
one branch in `check`, and two refusals that exit 2 and leave the file
untouched. Each new case was shown red (section 4). The flag widens no
gate: it only writes where the check would fail on the level, and the
level is not ratcheted.

## 3. The failing case's message gives a refused command (🟡 1)

`REMEDY` at
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:284`
tells a contributor to "write the price level it implies into
seal/budgets.md with `budget_check.py --restate-price`". The flag refuses
to run without `--baseline`, by design, because the level is the base's
times the file's move. The command as given has neither the base nor the
script's path.

- **Executed.** `python3 .github/scripts/budget_check.py --restate-price`
  in the clone exits 2: "--restate-price was given without --baseline".
- **Read.** The PR body's *What changes* item 2 says "Its message gives
  the whole refresh: … run `budget_check.py --baseline origin/<base>
  --restate-price`". The work item's `changelog.md:48-50` says "the
  recipe and the failing case's message both give that command". Neither
  is true of the message. `CONTRIBUTING.md:182` does give the full form.
- **The test pins the short form.**
  `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:401`
  asserts "`budget_check.py --restate-price`, and commit both", so the
  incomplete text is held in place.

Why it matters: the staleness case is the refresh schedule, and its
message is the instruction a contributor meets when the case goes red.
Followed as written, the step that round 3's 🟡 1 added fails, and the
person has to find the recipe in `CONTRIBUTING.md` to finish. The refusal
is loud, so nothing is lost, but the release would ship a message that
names a command that does not run, and a changelog and PR body that say
it does. The fix is the full command in `REMEDY`, the assertion beside
it, and the changelog's line 23.

## 4. Round 3's 🟡 2 and what stood on the old fact

**Executed.** With `seal/budgets.md`'s `slow-file` row set back to
`gate`, `test_a_slow_file_is_reported_and_the_suite_seconds_are_gated`
fails. With the line that clears the price problem after a restate
removed from `check`,
`test_restate_price_writes_the_level_a_refresh_implies` fails. Both
mutations were reverted and the clone checked clean. The three touched
modules pass.

**Read.** The PR body's 20 `Budget removed:` lines name the family row
and the 19 file rows, which is every row `effective` gives the family's
kind. The checker prints each as "no longer a gate (report)" and reads
the body's reason (executed above). `ratchet` skips any base row that is
not a gate, so from this merge on a `slow-file` ceiling moves with no
line. That is what a `report` row is, and the docstring at
`.github/scripts/budget_check.py:115` now says the unlisted-file rule
holds "where the family is a `gate`".

The places that stated the old fact on this branch were rewritten:
`budget_check.py`'s docstring, `seal/budgets.md`'s comment, the work
item's `spec.md:36`, `plan.md:85`, `overview.md:29` and `changelog.md`.
`docs/release-checklist.md:75` still asks the release to lower a
`slow-file` row from the trend; that is still true of a report row's
printed ceiling.

One record off the branch still states the old fact. The spec of work
item 1791876665, which is in the release branch and not yet settled,
says at `spec.md:36` that `slow-file` is "gate · a slow file that grows
past 1.3 times fails; a file not listed that crosses 120 s fails", and
its `questions.md:8` lists `slow-file:*` among the gates. When that item
is settled at the 0.22.0 release, its spec is what gets folded into a
`docs/` policy. That is ⬜ 3.

## 5. The PR body against the branch

- **Executed.** `budget_check.py --baseline 5b1f6fae --base-ref
  release/v0.22.0 --pr-body-env PR_BODY` with the body from
  `gh pr view 937`: exit 0 at 25728e2c.
- **Executed.** The *How it was checked* row "A union applied by the
  documented steps … exit 0 with this body; before `--restate-price`,
  exit 1 asking for the level" reproduces (section 1).
- **Read.** Item 2's claim about the message is false (🟡 1). Item 4 says
  "Measured over eight refreshes, one union moves a single test file 0.67
  to 1.72 times the level from the next". Round 3's table measured eight
  pairs, one of them unsharded to unsharded, and 0.67 to 1.72 is the
  range over its four union-to-union pairs. The conclusion stands; the
  count describes the wrong thing (⬜ 4).
- **Not run by this round.** "538 passed, 2 skipped" and "every mutation
  red" are the implementer's. This round ran three modules and two
  mutations.

## Regression tests to plant

- `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`:
  the assertion at line 401 changed to the full command, as in the fix
  below. Not run by this round: whoever plants it shows it red against
  the current `REMEDY` before changing the constant.

## Facts for the record

- Run 38655519975's union against 5b1f6fae: level 1136, `suite-seconds`
  7,132 at that level against a ceiling of 9,185 (executed).

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the staleness message gives `budget_check.py --restate-price` with no `--baseline`, which the checker refuses with exit 2; the PR body's item 2 and the work item's changelog say the message gives the `--baseline origin/<base>` form, and the case asserts the short form | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:284` | open | executed: the command without `--baseline` exits 2 in the clone; read: `REMEDY`, the assertion at line 401, `changelog.md:23` and `:48-50`, PR body item 2 |
| ⬜ 2 | the level `--restate-price` writes and the level `price_problems` demands are one expression written twice, so a change to one copy makes the writer write a level the check refuses | `.github/scripts/budget_check.py:1396` | open | read: `:1396` and `:1423`; executed: today both give 1136 on round 3's union |
| ⬜ 3 | work item 1791876665's spec still says `slow-file` is a gate that fails an unlisted file over 120 s, and its questions list it among the gates; that item is settled into `docs/` at the 0.22.0 release | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:36` | open | read: `spec.md:36`, `questions.md:8`; this branch's `seal/budgets.md:41` makes the family `report` |
| ⬜ 4 | the PR body says "Measured over eight refreshes"; round 3 measured eight pairs, and 0.67 to 1.72 is the range over its four union-to-union pairs | PR #937 body, *What changes* item 4 | open | read: round 3's report §3 table |
| 🟢 | round 3's 🟡 2 is closed — the `slow-file` family is a `report` row and `suite-seconds` stays the gate | `seal/budgets.md:41` | confirmed | executed: the case goes red with the row set to `gate`; the PR body's 20 removal lines give exit 0; round 3's union with the level restated holds with the body |
| 🟢 | round 3's 🟡 1 is closed — `--restate-price` writes the level the check demands and the recipe gives the full command | `.github/scripts/budget_check.py:1439`, `CONTRIBUTING.md:182` | confirmed | executed: on round 3's union the check names 1136, the flag writes 1136 on one line, and the run with the body is exit 0; the case goes red without the line that clears the price problem; the message's remaining gap is this round's 🟡 1 |
| 🟢 | adding `--restate-price` in a fix pass does not overstep | `.github/scripts/budget_check.py:1341` | confirmed | read: the alternative stops for a person on every refresh, against `CLAUDE.md`'s first goal; the flag writes only where the check would fail on the level, and both refusals leave the file untouched (executed by the module's cases) |
| 🟢 | the PR body passes the hygiene step's command at the tip | PR #937 body | confirmed | executed: `--baseline 5b1f6fae --base-ref release/v0.22.0 --pr-body-env PR_BODY`, exit 0 |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on `tests/test_a_budget_ratchets.py`, `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, `tests/test_every_reader_ends_a_line_where_gfm_does.py` at 25728e2c | exit 0: 339 passed, 2 skipped |
| `budget_check.py --baseline 5b1f6fae --base-ref release/v0.22.0 --pr-body-env PR_BODY`, body from `gh pr view 937` | exit 0 |
| run 38655519975's union over `.test_durations`, `budget_check.py --restate-price` with no baseline | exit 2: "given without --baseline"; the file untouched |
| the same union, `budget_check.py --baseline 5b1f6fae` | exit 1: level 1136 named, plus the 20 removals with no body |
| the same union, `--baseline 5b1f6fae --restate-price` | exit 1: wrote 1136, one line of `seal/budgets.md` changed; the 20 removals remain with no body |
| the same, then the check with the PR body | exit 0 |
| mutation: `slow-file` row set to `gate`, and the clearing of the price problem after a restate removed; the two new cases run | exit 1: both fail; reverted, clone clean |
| `round-record new` on a copy of this report, in the clone only | exit 0; wrote `Fix of a fix` as second for 🟡 1 at `REMEDY`, and said this record ends the run |
| `bin/test tests/test_no_real_identifiers.py` with that copy staged in the clone | exit 0: 6 passed |
| the full suite, lint and typecheck | not yet: the sealer's, after the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

## Paste-ready fixes

### 🟡 1 — the message gives the command that runs

`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:279-290`:

```python
REMEDY = (
    "Refresh it from this branch's latest `tests` run, whose `durations` job "
    "unioned the Windows shards' parts: `gh run download <run id> -n "
    "test-durations -D <dir>`, then move <dir>/.test_durations over the "
    "committed .test_durations, write the price level it implies into "
    "seal/budgets.md with `python3 .github/scripts/budget_check.py "
    "--baseline origin/<base> --restate-price`, where <base> is the branch "
    "the pull request merges into, and commit both; "
    "the file's line ends are already LF. "
    "A run older than the artifact's seven days is re-run first, with "
    "`gh run rerun <run id>`; a branch with no pull request, or whose run "
    "is too old to re-run, gets one with `gh workflow run test.yml --ref "
    "<branch>` (CONTRIBUTING.md §Running the checks)."
)
```

`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:401`:

```python
    assert (
        "`python3 .github/scripts/budget_check.py --baseline origin/<base> "
        "--restate-price`, where <base> is the branch the pull request merges "
        "into, and commit both" in sentence
    )
```

`seal/specs/1791876667-the-durations-refresh-has-a-schedule/changelog.md:22-23`:

```markdown
    the file over the committed one, write its price level with
    `budget_check.py --baseline origin/<base> --restate-price`, commit both. The download needs a
```

### ⬜ 2 — one expression for the level

`.github/scripts/budget_check.py`, beside `price_problems`, and its two
callers using it:

```python
def expected_level(base_level, ratio):
    """The price level here, per mille: the base's times the ratio the
    durations file moved by, rounded.

    Reads: nothing — a number from the numbers handed to it"""
    return seconds(base_level * ratio)
```

```python
            if restate and priced:
                level = restate_price(root, head_text, expected_level(base_level, ratio))
```

```python
    expected = expected_level(base_level, ratio)
```

### ⬜ 3 — the other item's spec

`seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:36`,
the Kind cell of the `slow-file:<path>` row:

```markdown
| report · gated at first; #931 made the family a `report` row, because one union of the Windows shards' parts moves a single file 0.67 to 1.72 times the level from the next, and `suite-seconds` is the gate |
```

### ⬜ 4 — the PR body's count

```markdown
4. **`slow-file` rows report instead of gating.** Over four unions of one tree, a single test file moved 0.67 to 1.72 times the level from one union to the next, past the 1.3 band, on files nobody changed.
```

Needs a fix: yes — 🟡 1, the staleness message gives a restate command without `--baseline`, which exits 2

Loses a record or crashes: no


## Proof block

Files opened this round, at 25728e2c in the clone unless noted:
`.github/scripts/budget_check.py` (the fix diff; `stated_price`,
`seconds`, `price_level`, `check`, `price_problems`, `restate_price`,
`ratchet`, the docstring's families paragraph), `hooks/config.py`
(`gfm_table`'s docstring and head), `.github/workflows/hygiene.yml` (the
budget step and its checkout), `CONTRIBUTING.md` §*Running the checks*,
`docs/release-checklist.md:68-82`, `seal/budgets.md:1-41`,
`tests/test_a_budget_ratchets.py` (the fix diff),
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`
(the fix diff and lines 255-330),
`tests/test_every_reader_ends_a_line_where_gfm_does.py` (the fix diff),
the work item's `changelog.md`, `rounds/round-3.md`, and
`rounds/round-3-report.md` (summary, §3 table, header, proof block);
work item 1791876665's `spec.md:30-40`, `questions.md:1-12` and
`changelog.md:1-14`; the PR #937 body from `gh pr view`; the
`test-durations` artifact of run 38655519975.

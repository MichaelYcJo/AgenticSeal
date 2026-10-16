# Round 3 report — 1791876667-the-durations-refresh-has-a-schedule (#931)

Reviewed by warden (Opus 5.5) on 2026-10-15, at e14cdff4, in a
`git clone --no-local` of the branch at that SHA, against
`origin/release/v0.22.0` at 5b1f6fae (#944's squash). The round was asked
five things: whether the rebase's conflict resolutions hold, whether the
cleanup commit e14cdff4 rewrote in place, how the design handles a union
commit that moves the price level, the open retention divergence, and
whether round 1's and round 2's fixes still hold on the rebased tree.
Rounds 1 and 2 were read for coordinates; every verdict below is
re-derived on this tree.

## Summary

- **The rebase lost nothing and brought nothing back.** The 20 files of
  the diff are the item's own; no ledger, `evidence-check` or survivor
  file returned, and the six-job sentence counts what the tree runs. On
  the tip, `budget_check.py --baseline 5b1f6fae` holds every gate row
  (executed).
- **Round 1's four fixes hold on the rebased tree**, judged by content
  (read), and the narrow modules pass (executed).
- **The refresh the item ships fails the budget gate on the commit it
  makes (🟡 1).** The recipe ends at "commit it". The tip's own run,
  38655519975, produced a union. Committed over this tree, that union
  fails the hygiene workflow's budget step twice: once for the price level
  (1132 to 1136), and once, after the level is restated, for
  `tests/test_worktree_guard.py`, which crosses the 120 s that unlisted
  files are held to. Neither the recipe nor the failing case's sentence
  names either step (executed).
- **A union refresh moves single test files further than the `slow-file`
  band was set to hold (🟡 2).** Seven union refreshes were measured, and
  each one fails at least one `slow-file` row on files nobody changed. In
  the union-to-union pairs, slow files moved 0.67 to 1.72 times the level.
  The one unsharded pair on record moved them 0.80 to 1.19. Each refresh
  therefore needs `Budget raised:` lines, and those ratchet one-sided
  ceilings up on noise.
- **Two record corrections (⬜ 3, ⬜ 4).** `spec.md` still says the parts
  are kept one day, with no divergence row. The changelog and overview
  name the `budgets` job as the step that names the price level, and that
  job never reads the price level.

Causal order: 🟡 2 is why 🟡 1 is more than a missing sentence. A recipe
that named only the price level would still meet a red gate on every
refresh measured.

## 1. The rebase's conflict resolutions

- `test.yml` (read): the diff against 5b1f6fae is the `store` entries, the
  pytest line, the part upload, the `durations` job, one `workflow_dispatch`
  comment, and the `budgets` job's `fetch-depth: 0` and its comment
  removed. The jobs are `lint`, `pytest`, `durations`, `arm-check-grammar`
  and `budgets`; #944's `ledger` job did not come back.
- `budgets` without `fetch-depth: 0` (read): it runs
  `budget_check.py --ci-jobs` only, which reads no history. `RUNS_PYTEST`
  does not select the job, because its one pytest word is on its `needs:`
  line. The guard case passes (executed, below).
- `CONTRIBUTING.md:135-145` (read): "six jobs" lists lint, the suite,
  `durations`, `arm-check`, `budgets` and the hygiene workflow. That is
  the base's five, with `ledger` already gone, plus `durations`.
- `CONTRIBUTING.md`'s refresh paragraph (read): the old measuring recipe,
  the release-preparation schedule and the post-refresh macOS re-read are
  gone. Nothing outside `seal/specs/` and released changelogs still names
  them (`git grep`, read).
- `seal/budgets.md` (executed): only `docs/release-checklist.md`'s
  `docs-history` ceiling moves, from 11 to 10, which is what the box's
  removal measures. `## Price level` stays at #944's 1132, and so does
  `.test_durations`. `budget_check.py --baseline 5b1f6fae` on the tip
  exits 0 with "every gate row holds".
- `docs/release-checklist.md` (read): the box is removed whole and §0
  reads on without it.

## 2. The cleanup commit e14cdff4

Read. The ledger fragment and `survivors.md` are deleted. `spec.md` In 6
and S8, its grounding rows, and its Data & interfaces ledger bullet are
rewritten in place. `plan.md` phase 3 and the Status column name the
rebased commits. `overview.md`'s divergence table gains two rows (the
committed file and the ledger records), which is that table's purpose,
and its other rows are edited in place. `phases/phase-3.md` and the
round files are untouched, so history stayed history. Among the item's
live records, only the divergence row that says the ledger left still
names it.

## 3. The design on the new tree

### 🟡 1 — the refresh recipe ends at the commit, and that commit is refused

`CONTRIBUTING.md:177-185` and `REMEDY` at
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:279-288`
say: download `test-durations`, move it over the committed file, commit
it. On this tree that commit fails the hygiene workflow's step *every
budget holds its ceiling, and a raised ceiling says why*
(`.github/workflows/hygiene.yml:175-184`), which runs
`budget_check.py --baseline origin/<base>`:

- **The price level, always.** `price_problems`
  (`.github/scripts/budget_check.py:1384`) requires `## Price level` to be
  the base's level times the median per-file ratio. No union prices
  exactly like the file it replaces, so the row moves on every refresh:
  0.901 to 1.054 across the pairs measured below.
- **A `slow-file` row, in every refresh measured.** See 🟡 2.

Executed, on the exact refresh the recipe makes today: the `test-durations`
artifact of run 38655519975 (this tip, e14cdff4, every job green) was put
over the clone's `.test_durations`. `budget_check.py --baseline 5b1f6fae`
exits 1. It names the level ("Write 1136 there"), and it names
`slow-file: tests/test_worktree_guard.py is not listed and measures 124
seconds, over the 120`. With 1136 written, it still exits 1 on that file
(123 s). The same probe with the pre-rebase union of run 38523258950, with
the entries of the 21 test files #944 deleted taken out, names level 1088
and two listed rows (`test_one_heredoc_shape_is_data_to_the_commit_gate.py`
253 over 224, `test_pact_check.py` 168 over 157). With 1088 written, it
still fails those two rows.

Why it matters: the paragraph a contributor reaches from a red staleness
case tells them the job is done at the commit. The next red arrives on
another workflow and asks for a judgment (`Budget raised: <reason>`) about
a file they never touched. `overview.md`'s *Not done* already says the
recipe does not name the row, and it gives that gap no answerer. S7
("nothing asks a person") does not hold for the commit the remedy
produces.

The fix states both in the two places the recipe lives. It also lets the
`durations` job say, before the commit, what the commit will be told.
`budget_check.py --baseline HEAD` with the union in the working tree gives
exactly the verdict `--baseline <base>` gives (executed: the same three
lines, exit 1). The step is informational: exit 1 is the preview, and exit
2 fails the job. Whether `git merge-base HEAD HEAD` resolves on the job's
depth-1 checkout is `unverified`. The pull request's first run answers it,
and the smith owns that answer.

### 🟡 2 — a union moves single files further than the `slow-file` band holds

`.github/scripts/budget_check.py:86-96` sets `suite-seconds` and every
`slow-file` row one-sided at 1.3 times the reading, because "one refresh
moved each of its 19 test files of 100 seconds or more 0.76 to 1.14 times
the level … which holds that spread with room." The unlisted files share
one row at 120 s. That spread was read off one refresh. This branch makes
the shards' union the only refresh there is.

Executed (probe `test_tmp_spread.py`, deleted, plus the tip probe above).
For each pair, the probe took the level `price_level` computes, then took
each test file whose reading × 1.3 reaches 120 s and divided the file's
ratio by that level:

| Pair | Measured how | Level | Listed-size files | Range | Over 1.3 | Gate on that refresh |
|---|---|---|---|---|---|---|
| 0.21.1's file → #944's file | unsharded → unsharded | 1.132 | 17 | 0.80–1.19 | 0 | not probed |
| #944's file → union 38655519975 (this tip) | unsharded → union | 1.003 | 18 | 0.82–1.14 | 0 | fails: unlisted `tests/test_worktree_guard.py` 123 s |
| #944's file → union 38523258950 | unsharded → union | 0.961 | 18 | 0.75–1.54 | 3 | fails: two listed rows |
| #944's file → union 38506858134 | unsharded → union | 0.901 | 18 | 0.77–1.40 | 1 | not probed |
| union 38487467049 → union 38499299992 | union → union | 0.990 | 20 | 0.67–1.64 | 2 | not probed |
| union 38499299992 → union 38506858134 | union → union | 0.944 | 20 | 0.77–1.72 | 2 | not probed |
| union 38506858134 → union 38523258950 | union → union | 1.041 | 21 | 0.73–1.57 | 5 | not probed |
| union 38487467049 → union 38523258950 | union → union | 1.054 | 20 | 0.78–1.52 | 4 | not probed |

The four pre-rebase union runs share one committed file and nearly one
tree, so the movement comes from the measurement and not from the code.
For example, `tests/test_the_seal_is_taken_once_by_the_sealer.py` read
860 s in one union and 1,398 s in the next. One unsharded pair is a
sample of one, so "unsharded is calmer" is suggested rather than shown.
That a union refresh trips a `slow-file` row is shown on every refresh
measured. Two of them were run through the gate itself, and the rest
have a listed-size file over 1.3.

Why it matters: each refresh the staleness case asks for fails the gate
on files nobody changed. The way through is a `Budget raised:` line per
file. A one-sided ceiling raised that way is lowered only at a release,
from the trend, so every refresh ratchets the slow-file ceilings up on
noise. The checker's docstring then states a spread the tree no longer
produces.

This is a decision rather than an edit, because the band is #930's
design: `budget_check.py` is outside this diff, while the measurement
that breaks the band is this item's. Two forms:

- **(a) A refresh re-prices, it does not grow.** Where `--baseline` sees
  `.test_durations` differ from the base's, the `slow-file` rows (listed
  and unlisted) are shown and not gated in that pull request.
  `suite-seconds` and the price level still gate. What is lost: a pull
  request that both refreshes and grows one file past its ceiling passes
  that one time. The next pull request reads it at its new price against
  the same ceiling.
- **(b) Widen the band to what a union spreads**, about 1.8, and correct
  the docstring's figures. What is lost: the gate on a slow file loosens
  on every pull request, not only on a refresh.

The paste-ready fix below is (a), the narrower loss. Who answers: the
orchestrator decides between (a) and (b), and whether this branch or
1791876665's owner carries it. The owner's rule is that a defect is fixed
where it arises, and that points at this branch, because the union is
what produces the spread.

### `--clean-durations` through the union

The behaviour is the same as in the unsharded run. Read: `spec.md` In 1
cites pytest-split's `pytest_sessionfinish` (NAME NOT IN TREE), which with
`--clean-durations` writes the reports of its own session. A shard's
session is its group, and the groups partition the collection. Executed:
the tip's union holds 9,242 entries, and `bin/test tests -q -k
test_the_durations_file_prices_the_suite` on the same tree reports
"1 passed, 9241 deselected", so the collection is 9,242 cases. The union
is the collection, one for one in count, with nothing left over from
deleted files.

Two shards can differ from that, and only in failure. A shard killed at
its timeout leaves the committed file whole, and the union refuses it as
"ids in two parts". A shard stopped at collection writes an empty map,
which is refused as "prices no case". Both are pinned by
`test_a_missing_part_a_duplicate_id_or_an_unparseable_part_is_exit_2`.

## 4. Parts retained 1 day (⬜ 3)

`spec.md:58` says "Parts retained 1 day, the union 7". The code keeps
both seven days with `overwrite: true` (`.github/workflows/test.yml:176`,
`:209`), as round 1's 🟡 1 fix decided. `overview.md`'s divergence table
has no row for it. `plan.md:58`'s phase 1 still describes
`retention-days: 1`, but that is the phase's history and can stay. The
code and tests are right; the frame and the overview disagree with them
without saying why. A divergence row closes it.

## ⬜ 4 — the record names the wrong step for the price level

`changelog.md:40` says a union commit restates the level "to the number
the `budgets` step names", and `overview.md:43` says "the `budgets` job
names it". The `budgets` job in `test.yml` runs
`budget_check.py --ci-jobs`. With that flag, `check` keeps only the
`ci-minutes` rows and takes no baseline
(`.github/scripts/budget_check.py:1341-1351`, read), so that job never
names a price level. The step that does is the hygiene workflow's budget
step. A person who reads the changelog and opens the `budgets` job finds
it green.

## 5. Rounds 1 and 2 on the rebased tree

By content, read at e14cdff4:

- Round 1 finding 1: both uploads carry `retention-days: 7` and
  `overwrite: true` (`test.yml:168-176`, `:203-209`), asserted by
  `test_the_upload_step_runs_always_and_only_where_store_is_set` and
  `test_the_durations_job_needs_pytest_and_runs_unless_cancelled`.
- Round 1 finding 2: `REMEDY` and `CONTRIBUTING.md:183-185` give
  `gh workflow run test.yml --ref <branch>`, and T11's `gone` tuple does
  not forbid it.
- Round 1 finding 3: `RUNS_PYTEST` and `SHALLOW_RUNNERS` are as fixed
  (`tests/test_ci_gives_the_checks_what_they_need.py:328`), and they now
  also keep the `budgets` job's `needs:` line out.
- Round 1 finding 4: `durations_union.py:234-235` refuses `--count` below
  one.
- Round 2 finding 5 (answered with grounds): the grounds still hold. The
  new `budgets` job writes `needs: pytest` on one line, which the guard
  skips.
- Round 2 finding 6 and the carried ❓: run 38496738041's attempt 2
  answered them in the record. Nothing on this tree changes the upload
  keys that answer rested on.

## Regression tests to plant

- For 🟡 1, in
  `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`:
  `test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe` and
  `test_the_recipe_names_the_artifact_and_the_checklist_has_no_box` each
  assert `## Price level` and `Budget raised:` in their text. If the
  preview step is taken,
  `test_the_durations_job_needs_pytest_and_runs_unless_cancelled` asserts
  a step running `budget_check.py --baseline HEAD` after the union. Each
  is seen red by deleting the sentence or the step.
- For 🟡 2 (a), in `tests/test_a_budget_ratchets.py`: a base file and a
  head file with every case ×1.0 except one listed file ×1.6. With the
  level restated, the run exits 0, and the summary shows the file as over
  but not gated. With the durations file unchanged and that file's
  seconds grown, the run still exits 1. Seen red against the current
  `check`.

## Facts for the record

- Unsharded to unsharded refresh (0.21.1's file to #944's): slow files
  0.80–1.19 of the level. Union to union, four runs of this branch:
  0.67–1.72, with one to five files over 1.3 in each pair. The tip's
  union against #944's file: level 1136, one unlisted file over 120 s
  (executed, this round).
- With a candidate `.test_durations` in the working tree,
  `budget_check.py --baseline HEAD` gives the verdict the refresh pull
  request will get (executed).
- The tip's union, 9,242 entries, equals the tip's collection (executed).

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the refresh recipe and `REMEDY` end at "commit it", and the hygiene budget step refuses that commit: for the price level on every refresh, and for a `slow-file` row on every refresh measured; neither text names either step | `CONTRIBUTING.md:177` | open | executed: run 38655519975's union over the tip's file, `budget_check.py --baseline 5b1f6fae` exit 1 naming level 1136 and unlisted `tests/test_worktree_guard.py` at 124 s; with 1136 written, still exit 1 on that file; `REMEDY` at `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:279` read |
| 🟡 2 | a union refresh moves single test files 0.67–1.72 times the level, past the 1.3 one-sided `slow-file` band that was set from one refresh's 0.76–1.14, so every refresh needs `Budget raised:` lines for files nobody changed | `.github/scripts/budget_check.py:91` | open | executed: eight pairs through `price_level`; one unsharded pair 0.80–1.19 with none over; seven union refreshes each trip a `slow-file` row, two of them run through the gate; the choice between (a) and (b), and which branch carries it, is the orchestrator's |
| ⬜ 3 | `spec.md` Data & interfaces says parts are kept 1 day; the code keeps them 7 with `overwrite: true`, and `overview.md` has no divergence row | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/spec.md:58` | open | read: `.github/workflows/test.yml:176`, `:209`; round 1's finding 1 decided seven days |
| ⬜ 4 | the changelog and overview say the `budgets` job names the price level; that job runs `--ci-jobs`, which keeps only `ci-minutes` rows | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/changelog.md:40` | open | read: `.github/scripts/budget_check.py:1341-1351`; the step that names it is `.github/workflows/hygiene.yml:175-184`; `overview.md:43` says the same |
| 🟢 | the rebase's conflict resolutions mean what both sides mean: nothing #944 removed came back, and the job count, recipe, budgets row and checklist hold | `.github/workflows/test.yml`, `CONTRIBUTING.md:135`, `seal/budgets.md:85` | confirmed | executed: `budget_check.py --baseline 5b1f6fae` at the tip, exit 0; read: the diff against 5b1f6fae, `git grep` for the old recipe |
| 🟢 | e14cdff4 rewrites the live records in place and leaves history records as history | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/` | confirmed | read: `git show e14cdff4`; phases and rounds untouched |
| 🟢 | round 1's finding 1 is closed — parts and union kept seven days with `overwrite: true` | `.github/workflows/test.yml:168-176` | confirmed | read at e14cdff4; the two cases assert both keys and pass (executed) |
| 🟢 | round 1's finding 2 is closed — the dispatch for a branch with no run | `CONTRIBUTING.md:183-185` | confirmed | read at e14cdff4: `REMEDY` and the recipe both carry it |
| 🟢 | round 1's finding 3 is closed — pytest read as a word on every code line but `needs:` | `tests/test_ci_gives_the_checks_what_they_need.py:328` | confirmed | executed: the module passes; the `budgets` job is not selected |
| 🟢 | round 1's finding 4 is closed — a `--count` below one is refused | `.github/scripts/durations_union.py:234` | confirmed | read at e14cdff4; its case passes (executed) |
| 🟢 | round 2's finding 5 stays answered with grounds | `tests/test_ci_gives_the_checks_what_they_need.py#runs_pytest` | confirmed | read: no job on the rebased tree has the shapes it names; `budgets` uses the one-line `needs:` |
| 🟢 | `--clean-durations` through the union drops what the unsharded run dropped: the union is the collection | `.github/workflows/test.yml:94` | confirmed | executed: union of run 38655519975 holds 9,242 entries; the collection is 9,242 |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on the six touched modules (`test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, `test_ci_gives_the_checks_what_they_need.py`, `test_docs_line_wrap.py`, `test_release_hygiene.py`, `test_the_contributor_has_a_procedure.py`, `test_a_budget_ratchets.py`) | exit 0: 309 passed, 2 skipped |
| `bin/test tests -q -k test_the_durations_file_prices_the_suite -p no:xdist` | exit 0: 1 passed, 9241 deselected |
| `budget_check.py --baseline 5b1f6fae` at the tip, unmodified | exit 0: every gate row holds |
| the same, with run 38655519975's union over `.test_durations` | exit 1: level 1136; unlisted `tests/test_worktree_guard.py` 124 s |
| the same, with `## Price level` at 1136 | exit 1: `tests/test_worktree_guard.py` 123 s |
| the same, with run 38523258950's union (the 21 files #944 deleted taken out) | exit 1: level 1088; two listed rows over |
| the same, with `## Price level` at 1088 | exit 1: the same two rows, 263 over 224 and 174 over 157 |
| `budget_check.py --baseline HEAD` with that union in the working tree | exit 1: the same three lines as against the base |
| `test_tmp_spread.py` over the eight pairs in §3 | exit 0: the table in §3 |
| the full suite, lint and typecheck at the tip | not yet: the sealer's, after the rounds settle |

### The broad gate

Not yet. No full-suite run has been taken at e14cdff4 or at any earlier
SHA of this rebased branch. The run comes due for the sealer's spawn once
🟡 1 and 🟡 2 are fixed or answered, not before.

## Paste-ready fixes

### 🟡 1 — `CONTRIBUTING.md:177-185`, the recipe's last sentences

```markdown
To refresh the file, take the artifact from your branch's latest `tests`
run: `gh run download <run id> -n test-durations -D <dir>`, then move
`<dir>/.test_durations` over the committed file and commit it. Its line
ends are already LF. The download goes to a directory of its own because
`gh` will not write over a file that is already there. A run older than
seven days is re-run first, with `gh run rerun <run id>`. A branch with no
pull request has no `tests` run until one is dispatched, and neither has a
branch whose run is too old to re-run:
`gh workflow run test.yml --ref <branch>` starts one. A new file moves
the prices `seal/budgets.md` reads it at. In the same commit, write the
`## Price level` the `durations` job's summary names, and answer each
`slow-file` row it names over its ceiling, as the hygiene workflow's
budget step will ask.
```

### 🟡 1 — `REMEDY`, the sentence's tail

```python
    "<branch>` (CONTRIBUTING.md §Running the checks). In the same commit, "
    "write the `## Price level` the `durations` job's summary names in "
    "seal/budgets.md, and answer each `slow-file` row it names, with a "
    "`Budget raised:` line where one is asked."
)
```

### 🟡 1 — `.github/workflows/test.yml`, a step after the union in `durations`

```yaml
      # What committing the union asks of `seal/budgets.md`, before anyone
      # commits it (#931): the price level the refresh moves, and any
      # `slow-file` row its prices put over a ceiling. `--baseline HEAD`
      # reads the committed file as the base and the union as the tree,
      # which is the verdict the refresh's pull request gets. Exit 1 is that
      # preview and leaves the job green; exit 2 is a checker that could not
      # read the tree, and fails it.
      - name: what committing the union asks of seal/budgets.md
        shell: bash
        run: |
          cp union/.test_durations .test_durations
          set +e
          python .github/scripts/budget_check.py --baseline HEAD
          code=$?
          [ "$code" -le 1 ] || exit "$code"
```

### 🟡 2 — `.github/scripts/budget_check.py`, form (a) in `check`

```python
        if any(row.name.partition(":")[0] in PRICED for row in head):
            text = blob_at(root, base, DURATIONS, against)
            before = (
                None
                if text is None
                else durations_from(text, f"{DURATIONS} at {against}")
            )
            here = durations(root)
            ratio, common = price_level(before, here, against)
            cache["price"] = (ratio, common)
            # A refresh re-prices the suite and does not grow it (#931): one
            # union moves single files 0.67 to 1.72 times the level from the
            # next, past the 1.3 band, so where the file moved against the
            # base its `slow-file` rows are shown and not gated.
            cache["refreshed"] = before is not None and before != here
            priced = price_problems(base_level, ratio, common, level)
    for row in head:
        try:
            results.append(measured_row(root, row, names, cache))
        except Unreadable as error:
            refusals.append(str(error))
    refreshed = cache.get("refreshed", False)
    problems = priced + [
        (r.row.name, p)
        for r in results
        if r.row.kind == GATE
        and not (refreshed and r.row.name.partition(":")[0] == "slow-file")
        for p in r.problems
    ]
```

The docstring at `budget_check.py:86-96` then states the union's spread
and this exemption in place of "which holds that spread with room".

### ⬜ 3 — `overview.md`'s divergence table, one row

```markdown
| Part retention | `spec.md` Data & interfaces: "Parts retained 1 day, the union 7" | parts and union both `retention-days: 7`, uploaded with `overwrite: true` | round 1's finding 1: re-running failed jobs re-runs the `durations` job, which reads every part again, so a part is kept as long as the union it makes |
```

### ⬜ 4 — `changelog.md:38-40` and `overview.md:43`

```markdown
    on, so no scaling is applied to the union. A pull request that commits
    a union restates `## Price level` in `seal/budgets.md` to the number the
    hygiene workflow's budget step names for it.
```

Needs a fix: yes — 🟡 1, the refresh recipe and `REMEDY` omit the price
level and the `slow-file` rows the refresh commit is refused for; 🟡 2,
the `slow-file` band does not hold a union refresh's spread (a decision
between forms (a) and (b), and which branch carries it).

Loses a record or crashes: no

## Proof block

Files opened this round, all at e14cdff4 in the clone unless noted:
`.github/workflows/test.yml`, `.github/workflows/hygiene.yml`,
`.github/scripts/durations_union.py`, `.github/scripts/budget_check.py`,
`CONTRIBUTING.md` §*Running the checks*, `docs/release-checklist.md` §0,
`seal/budgets.md`,
`tests/test_ci_gives_the_checks_what_they_need.py` (diff),
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` (diff),
the work item's `spec.md`, `changelog.md`, `overview.md` and `plan.md`
(e14cdff4's diff), `rounds/round-1.md`, `rounds/round-2.md` and the head
of `rounds/round-2-report.md`; `.test_durations` at a8d83663 and 5b1f6fae;
the `test-durations` artifacts of runs 38655519975, 38523258950,
38506858134, 38499299992 and 38487467049.

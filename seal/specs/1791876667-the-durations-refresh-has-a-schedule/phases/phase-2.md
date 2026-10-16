# 1791876667-the-durations-refresh-has-a-schedule — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | eafbfd8f |
| Ran by | specseal:smith on Opus 5.5, as `routing.md` and `handoff.md` name it |

## What this phase was asked

Build phase 2 and stop before phase 3. Read the after-run 38477758775 at
7569c1ab first, because its parts expire in a day: the parts, the union, and
the spread on both scales, the parts' summed seconds and the session's wall
clock. Answer Q1 against the before band phase 1 measured (1.10–1.20), not
the frame's 1.05. Give `staleness` its seconds side; make its sentence name
the download, which has to go to a directory of its own and be moved,
because `gh run download` will not overwrite; add the boundary fixtures;
T7–T9 and T11, each seen red. Rewrite `CONTRIBUTING.md`'s recipe paragraph
in place, remove the checklist's §0 box, and re-read the `test.yml`
comments. The orchestrator decided for #930 that `suite-seconds` and
`slow-file:*` are compared in baseline prices, normalised by the
seconds-weighted ratio over the ids both files hold, so a refresh's runner
price level cancels; record that here and raise nothing.

## What this phase found

### The after-run

`executed` 2026-10-14. Run 38477758775, `pull_request` at 7569c1ab, every
job green, the four parts and the union downloaded to the scratchpad. The
local union over the parts, against the committed file, is byte-identical
to the artifact (`cmp` exit 0), and its summary reads:

```
- entries: 13,930 in the union of 4 parts, 13,930 in the committed file
- seconds: 8,634.1 s live, 8,490.3 s in the committed file
- unpriced: 0 of the union's 13,930 cases (0.00%) have no price in the committed file
- dead: 0 entries of the committed file are no case a part ran, 0.0 s (0.00% of its seconds)
- part test-durations-4: 2,919 cases, 2,258.1 s measured, median price 1.01 x the committed file's over 2,919 cases both price
- part test-durations-5: 7,314 cases, 1,866.0 s measured, median price 0.78 x the committed file's over 7,314 cases both price
- part test-durations-6: 1,257 cases, 2,255.7 s measured, median price 1.06 x the committed file's over 1,257 cases both price
- part test-durations-7: 2,440 cases, 2,254.3 s measured, median price 1.00 x the committed file's over 2,440 cases both price
- spread: the slowest part, test-durations-4, measured 1.05 x the parts' mean of 2,158.5 s
```

The committed file divided the four groups to within 0.4 % of each other by
its own prices (2,122.6 · 2,125.7 · 2,124.4 · 2,117.7 s). The run then
measured them 2,258.1 · 1,866.0 · 2,255.7 · 2,254.3 s. The whole union
reads 1.017 × the committed file.

**The leg divides as well as before, on both scales (S5).**

| Division by | Run | Summed seconds, max/mean | Session clock, max/mean | max/min |
|---|---|---|---|---|
| the unsharded file (13,482 entries) | five runs, `phases/phase-1.md` | — | 1.10 · 1.13 · 1.14 · 1.16 · 1.20 | 1.26–1.65 |
| the unsharded file | 38475370013 (phase 1's run) | 1.04 | 1.10 | 1.26 |
| the shard-measured union | 38477758775 | 1.05 | 1.12 | 1.34 |

Session seconds of the after-run, groups 1–4: 598.3 · 498.4 · 614.9 ·
668.2 s, and the job wall clock reads 1.16. The after-run's 1.12 falls
inside the 1.10–1.20 the old file gave over six runs, so the shard-measured
file divides no worse. It does not divide better either: one run cannot
tell 1.12 from the band's middle.

**Q1 — no per-runner skew to correct; no scaling is built.** The
seconds-weighted ratio of each part to the file it was divided by, over the
cases both price:

| Run | Group 1 | Group 2 | Group 3 | Group 4 | max/min |
|---|---|---|---|---|---|
| 38475370013, against the unsharded file | 1.082 | 1.096 | 1.064 | 1.040 | 1.054 |
| 38477758775, against the union | 1.064 | 0.878 | 1.062 | 1.065 | 1.213 |

Group 2 is the highest of the four in the first run and the lowest in the
second, so what moves is the runner a group lands on in a given run, not a
skew a part carries from one refresh to the next. Scaling each part to the
mean ratio would correct one run's noise into the file and would not remove
a bias. The default stands, `questions.md` Q1 is ticked, and the summary's
ratio line stays the reading a later skew would show up on.

**macOS read wider on this run.** Groups 1–3: 370.8 · 319.0 · 611.9 s,
1.41 max/mean, against 1.05–1.34 on the old file. Group 3's job took
10 m 35 s, under its 15-minute `timeout`. One run, and the macOS division
is out of this item's scope (`spec.md` §*Out*). The `timeout` and its rule
in `test.yml` are what hold it, and #929, whose cuts change the macOS
groups, reads it next.

**`durations` cost 7 s and 11 s** in the two runs (`gh pr checks 937`).
That is Q3's job time; the price page was not opened, so Q3 stays open with
this as its input.

### `suite-seconds` under #930's design

The orchestrator decided, from phase 1's finding, that #930 compares
`suite-seconds` and `slow-file:*` in baseline prices: each side is
normalised by the seconds-weighted ratio over the ids both files hold, so a
refresh's runner price level cancels. Computed here by that definition
(`executed`): the ratio over the 13,454 shared ids is 1.0706, so the
union's 8,490.3 s reads 7,930.5 s in the old file's prices, +0.88 % over
7,861.7 s rather than +8.0 %, and inside the 5 % band. So that
commit owes no `Budget raised:` line under the design #930 is building, and
this branch raises nothing. Whether a `slow-file:*` row still crosses
after normalisation is #930's checker's to say; this item has no reader
for it. `read`: #930's checker is not on this branch, and the arithmetic
above is this phase's reading of the orchestrator's definition, not that
checker's output.

### The check and the words

- **One constant, two sides.** `staleness` fails past `STALE_SHARE` of the
  collected cases unpriced, as before, or past `STALE_SHARE` of the file's
  seconds in entries the suite no longer collects. The seconds side's share
  is taken over the file's whole sum, dead entries included, as `spec.md`
  In 3 words it. An empty file is all unpriced and has no seconds to share,
  which is not a division by zero.
- **The sentence names the download.** `REMEDY` says to download
  `test-durations` from the branch's latest `tests` run with `-D <dir>`,
  move the file over the committed one and commit it, and to re-run a run
  past the artifact's seven days with `gh run rerun <run id>`. It no longer
  sends anyone to a recipe for a measuring run. It still names
  `CONTRIBUTING.md` §Running the checks, which now holds the same steps.
- **T8 and T9 keep their released names.** 0.21.1's S2
  (`seal/releases/0.21.1.md`) anchors
  `test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe` and
  `test_an_entry_nobody_collects_is_not_counted` by name, so T8 is the first
  with its body rewritten to the download, and T9 is the second, now
  asserting that 5,000 dead entries fail the seconds side and leave the
  unpriced side at zero. T7 is new:
  `test_dead_seconds_past_the_share_fail_and_at_the_share_pass`, on 950
  cases with 50 dead entries (exactly the share) and then 51. Two more
  cases pin what building found: both sides named in one sentence with one
  download, and the empty file.
- **`CONTRIBUTING.md`.** The recipe paragraph is rewritten in place: every
  run's Windows shards store, the `durations` job unions them into
  `test-durations`, the staleness case says when, and the download goes to
  its own directory and is moved. The measuring-run shape, the 60-minute
  leg, the restore and the post-refresh `timeout` re-read are gone, which
  are the three `CONTRIBUTING.md` rows of `spec.md` §*Removes*. The macOS
  `timeout` sentence now says the rule beside the values sets it when a
  shard grows past it. The job-count sentence above it, *CI runs five
  jobs*, was made false by the `durations` job and now says six. #930's
  plan rewrites the same sentence for its `budgets` job, so whichever pull
  request lands second merges the two by hand.
- **`docs/release-checklist.md` §0 has no refresh box**, the fourth
  `## Removes` row.
- **`test.yml`'s comments, re-read.** One was false: the `workflow_dispatch`
  comment called the Windows leg's `--durations` table the only per-case
  figure for a pushed branch with no pull request. It now names the
  `test-durations` artifact beside it. The rest stand as written.
- **The survivors.** `survivor-check --root <worktree> --range
  origin/release/v0.22.0...HEAD`, the range the hygiene workflow runs,
  reported six places carrying removed wording: five in the frames of
  shipped work items (1791852613's plan three times and its spec, and
  1791384162's spec), and 0.21.1's S4 in a frozen release file. Each is
  answered in `survivors.md` with its quote and grounds, and the same
  command with `--exempt` exits 0. Over this phase's own commits alone
  (`7569c1ab..64e4b38e`) the check also reports the upload steps in
  `test.yml` and the shard module's docstrings, which are true text about
  the mechanism this branch adds, and those do not appear over the branch's
  whole range.

### The local numbers

`executed` 2026-10-14.

- The phase's command, the modules of phase 1 plus `test_docs_line_wrap`,
  `test_the_contributor_has_a_procedure` and `test_release_hygiene`: exit 0,
  277 passed, 2 skipped. `test_ci_gives_the_checks_what_they_need`,
  `test_a_unit_the_extractor_cannot_bound_is_refused` and the shard module,
  after the `test.yml` comment edit: exit 0.
- `bin/test tests -q -k test_the_durations_file_prices_the_suite`: exit 0,
  1 passed, run rather than skipped. The four cases this phase added are
  unpriced, 4 of 13,934.
- `ruff check` and `ruff format --check` on the module: exit 0.

### The mutations

Each through `bin/mutation-check` after the commit 64e4b38e, one at a time;
all 14 exit 0, `red`.

| Case | Break | Failed |
|---|---|---|
| T7 | the seconds side dropped · `>=` at the share · the share over the live seconds · no first gone entry named | 3 · 1 · 1 · 1 |
| T8 | the artifact's name gone · the download into the repository with no move · the re-run gone · the unpriced side dropped | 2 · 2 · 1 · 3 |
| T9 | a dead entry counted as unpriced | 2 |
| empty file | the guard on an empty sum dropped | 1 |
| T11 | *restore the shards* re-added · the download sentence dropped · the seconds side unsaid · the checklist box re-added | 1 · 1 · 1 · 1 |

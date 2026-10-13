# 1791852613-the-test-durations-are-refreshed-and-say-when-next — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 2fc7d694 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Build phase 3 of `plan.md` from post-refresh run 38335775781
(`workflow_dispatch` at `cc1768d1`, every job green). For each pytest job,
read its time and summary line. Check that each leg's sum equals ubuntu's,
that the slowest Windows shard is inside its budget, and how far the shards
spread by pytest's seconds. Answer Q4. Set every leg's `timeout` and its
comment by the rule beside the values. Write the ledger fragment (S1–S7, the
`--reverify --into` re-reads, any `Corrected ·`), `changelog.md`, and a
closed `overview.md`, with `evidence-check --strict` exiting 0. In
`overview.md`, keep the 213 POSIX-path ids and the recipe's merge visible as
issue candidates for the orchestrator to file, without widening this item.
Under the owner's new rule, a `docs/` or `CONTRIBUTING.md` change rewrites
what the file already states in place, and phase 1's sentence and box are
checked against it. No push and no dispatch.

## What this phase found

**Run 38335775781, read with `gh run view --json jobs` and each job's log
(executed 2026-10-13).**

| Job | Time | Summary line |
|---|---|---|
| ubuntu | 6 m 20 s | `13397 passed, 83 skipped in 358.88s` |
| Windows group 1 | 11 m 27 s | `3000 passed, 17 skipped in 646.88s` |
| Windows group 2 | 10 m 20 s | `6902 passed, 38 skipped in 588.99s` |
| Windows group 3 | 10 m 51 s | `1569 passed, 105 skipped in 615.44s` |
| Windows group 4 | 10 m 54 s | `1784 passed, 65 skipped in 615.16s` |
| macOS group 1 | 7 m 14 s | `6524 passed, 9 skipped in 410.94s` |
| macOS group 2 | 7 m 11 s | `3789 passed, 76 skipped in 409.23s` |
| macOS group 3 | 7 m 29 s | `3077 passed, 5 skipped in 430.48s` |

- **Sums.** Windows 3,017 + 6,940 + 1,674 + 1,849 = 13,480, and macOS
  6,533 + 3,865 + 3,082 = 13,480. Both equal ubuntu's 13,480.
- **Spread, by pytest's seconds.** Windows mean 616.62 s, slowest 646.88 s,
  ratio **1.05**. macOS mean 416.88 s, slowest 430.48 s, ratio **1.03**.
  The issue traced 1.37 to the file's age. On the old file, run 38332345615's
  macOS groups ran 253.57 s, 436.17 s and 489.50 s, a ratio of 1.25.
- **The slowest Windows shard** took 11 m 27 s, under the inherited 12
  minutes and inside its budget of 20.

**Q4: the hook reads the whole collection on GitHub's shards.** Two facts
show it.

1. In run 38332345615, macOS group 3 ran under `--splits 3 --group 3` on
   GitHub, and the suite case reported *1276 of the 13480 collected cases*.
   That is the whole suite, not the group's 3,110.
2. In run 38335775781 every shard is green, and each leg's sum is ubuntu's.

The green alone would not prove Q4. A group-only record holds the group's
cases, which are mostly priced, so it would also be green. Fact 1 is what
answers it.

**The budgets: no value moves.** The base is the slowest job measured on
the leg, read with `gh run view --json jobs`.

| Leg | Slowest measured | Run | 1.5 times | Budget |
|---|---|---|---|---|
| ubuntu | 9 m 43 s | 38332345615 | 14.6 | 15 |
| macOS, per shard | 8 m 29 s, group 3, on the old file | 38332345615 | 12.7 | 15 |
| Windows, per shard | 12 m 42 s, group 4 | 37576998008 | 19.1 | 20 |

The comment above the values named 9 m 03 s, 6 m 56 s and 10 m 34 s. It now
names the three bases above, with the other runs beside each.

- The Windows base comes from 0.21.0's `Corrected · S4` row, which recorded
  12 m 42 s (37576998008) and 12 m 15 s (37577753583). The comment had never
  carried them. Both times were re-read with `gh run view`.
- 0.21.0's S3 named 6 m 56 s as the macOS base, so it takes a
  `Corrected ·` row in the fragment.
- The measuring leg's budget in `CONTRIBUTING.md` was 55, and the rule gives
  60 from its 37 m 21 s. It was rewritten in place.
- No budget was lowered below a measured job, so no further dispatch is owed.

**`c058fbf3`'s message is inaccurate about Windows.** It names 11 m 52 s as
the Windows base. The comment was corrected to 12 m 42 s in `2fc7d694`,
which closes this phase. The value, 20, is the same either way.

**The owner's rule, applied to phase 1's text.** Phase 1 had appended the
"when it is refreshed" sentence after the recipe's last line. `c058fbf3`
moves it into the paragraph, before *To refresh it*, where the paragraph
already describes the file, and drops the appended copy. The same commit
rewrites the measuring budget's parenthesis in place. The
`docs/release-checklist.md` box states a new step as a rule and narrates no
change, so it stays as written.

**The ledger.** Rows S1–S6 and a `Corrected · S3` are in the fragment.
`--reverify --into seal/ledger/1791852613-….md --checked 2026-10-13` wrote 15
`Re-read ·` rows and left no released row. Every released row citing
`CONTRIBUTING.md#"## Running the checks"`, `docs/release-checklist.md#"## 0.
Before starting"`, `.github/workflows/test.yml#"pytest:"` or the quoted
`CONTRIBUTING.md` line was listed and its claim read first. Only 0.21.0's S3
had stopped holding.

- **S7 has no row.** Its claim is that the records exist, and the only
  coordinate for that is this directory's `overview.md`, which
  `settle --retire-process` removes after the release. The strict exit below
  is its evidence.
- **Three record lines quoted stamps the build then moved.** `spec.md`
  and `plan.md` quoted the `test.yml` pytest anchor with its released hash,
  and `phase-1.md` quoted the `CONTRIBUTING.md` section anchor the same way.
  The records
  arm read each as a claim on the current tree, and the first strict run
  exited 2 with three DRIFTED lines. Each line now names the anchor without
  its hash. The rows it names are unchanged, and the hashes stay in the
  released files.
- **The first `--reverify` pass refused four rows as MALFORMED.** Each mixed
  a test with a code coordinate. S2 now holds its four tests alone. S3, S6
  and `Corrected · S3` hold code coordinates and name their tests in the
  evidence cell.

**Verified at this phase's closing tree (executed 2026-10-13, exit codes
read directly, `SPECSEAL_CASE_CEILING_S=600`).**

- `python3 skills/evidence-check/scripts/evidence_check.py --strict .`:
  exit 0, with `0 stamps read · 0 refused · 0 drifted` in the records arm.
- `bin/test` over the twelve modules this item touches or that read its
  documents (the shard module, `test_a_slow_case_names_itself`,
  `test_ci_gives_the_checks_what_they_need`,
  `test_a_workflow_is_read_the_one_way`, `test_docs_line_wrap`,
  `test_a_reader_declares_its_input_class`,
  `test_no_passage_is_pasted_into_a_second_file`,
  `test_no_real_identifiers`, `test_one_word_one_meaning`,
  `test_release_hygiene`, `test_a_moved_rule_leaves_its_definition`,
  `test_the_contributor_has_a_procedure`): exit 0, `445 passed, 1 skipped`.
- `bin/test tests -q -k test_the_durations_file_prices_the_suite`: exit 0,
  `1 passed`.
- `python3 skills/verify/scripts/unverified_check.py --baseline
  origin/release/v0.21.1`: exit 0. This overview has two rows open (the
  sealer, and the pull request's run) and two closed.
- No Python changed in this phase, so ruff was not run again.

**Unverified, and who answers it.** The whole suite is the sealer's. That
GitHub reads the budgets at the final SHA is the pull request's run.

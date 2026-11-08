# Phase 1: 1794178397-a-durations-refresh-costs-no-round

## What this phase found

**The frame holds for this phase.** Every coordinate the phase 1 row
stands on was where the frame says at `56c72c42`. `.github/scripts/durations_union.py#report`
counted unpriced and dead entries itself. `tests/github/test_durations_union.py#write_parts`
builds parts and a committed file. `STALE_SHARE`, `REMEDY`, `unpriced`,
`dead`, `staleness` and the seven fixture cases stand in
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`
as `frame/design.md` *Removes* rows 2 to 4 name them. `seal layout --pairs`
named no pair in the test file before or after the phase (executed).

**The script now has three new names.**

- `Staleness` is a named tuple: `unpriced`, `dead`, `cases`, `held` and
  `dead_seconds`. It carries the two shares as the properties
  `unpriced_share` and `dead_share`.
- `staleness(merged, committed)` returns that reading.
- `verdict(stale)` returns the sentence, or None within the share.

`main` calls `staleness` once, inside the refusal block, and hands the
result to `report` and to `verdict`. So `report` gained a fourth parameter,
`stale`. `STALE_SHARE` (0.05) and `REMEDY` are module constants. The
comment above `STALE_SHARE` carries over the old test module's grounds.

**The decisions, each judged against `frame/design.md` *Data & interfaces*.**

- The design says the one function returns the two id lists and the two
  shares. The tuple also carries the union's case count, the file's seconds
  and the dead seconds. The report's lines and the verdict's sentence both
  print those three, and the tuple keeps them from being summed a second
  time. The shares are properties of the tuple, so one expression defines
  each.
- An empty union raises `Refusal`, as the design asks. `main` cannot reach
  it, because `union` already refuses an empty part and `--count` below
  one. The guard serves a direct caller, and `Test_staleness::test_refuses_an_empty_union`
  holds it.
- `--stale-fails` is an `argparse` flag with no value (`store_true`). The
  verdict runs only after the union is written and reported. Exit 1 means
  the union was written and the file is past the share.
- The sentence goes to stderr every time. It goes to the summary only where
  `GITHUB_STEP_SUMMARY` is set. Without that variable the report goes to
  stdout, as before, and the sentence stays on stderr alone. That follows
  the refusal path's existing behaviour.
- The verdict's words follow the report's. It says "N of the union's M
  cases" where the old suite case said "collected cases". It says "entries
  no part ran" and "First dead:" where the old one said "no longer
  collects" and "First gone:". The design's S3 calls them "the first dead
  ids".
- `REMEDY` states *Scope* item 4: download into a directory of its own,
  move over the committed file, commit it alone with the trailer
  `Seal-Routing: no work item` on a branch cut from `release/vX.Y.Z`, merge
  it by a pull request, and the release pull request's next run reads the
  refreshed file. It also says a work item never commits `.test_durations`,
  and keeps the old remedy's note that the line ends are already LF. It
  drops the old remedy's `gh run rerun` and `gh workflow run` steps,
  because `frame/design.md` *Removes* row 6 removes the per-branch recipe
  they served.

**Seen red.** Each of the 11 new or changed cases failed against the old
script (executed). One case was already in the file:
`Test_module::test_a_part_the_committed_file_does_not_price_says_so`, whose
`report` call now passes the reading. Against the old script the module
fails at collection, because `du.STALE_SHARE` does not exist. So for one
run `AT_THE_SHARE` was set to the literal 50 and then put back. In that run
the two `Test_main` cases failed with `SystemExit: 2`, the unknown switch.
The other nine failed with `AttributeError` on `staleness` or `verdict`.

**Mutation (executed).** One batch of 18 mutants over
`bin/test tests/github/test_durations_union.py -q -p no:xdist` gave 18
red. The mutants covered these breaks:

- the empty-union guard, and the unpriced and dead comprehensions;
- the file order of the dead list (`sorted`);
- the dead seconds and the file's seconds;
- both share properties, including the zero-seconds guard;
- `>` turned into `>=` on each side;
- each `First ...` line;
- the value of `STALE_SHARE`;
- the switch's condition both ways, and `return 1`;
- the stderr write and the summary write;
- `report` reading the file.

Five guards were run again one at a time, to read which line fails:

- `>=` on the unpriced side and `>=` on the dead side each fail
  `Test_verdict::test_accepts_exactly_the_share_on_each_side`, on that side's
  assertion.
- The zero-seconds guard fails with `ZeroDivisionError` in
  `test_refuses_an_empty_file_as_all_unpriced_and_nothing_dead` and in the
  `Test_module` case.
- The empty-union guard fails with `DID NOT RAISE Refusal`.
- `sentence = verdict(stale)` without the switch fails the two existing
  `Test_main` cases that read exit 0 over the stale fixture.

That last result is how scenario S2 is held. The fixture file is 16.67 %
unpriced, and `test_the_summary_names_each_parts_seconds_the_spread_and_the_live_sum`
and `test_accepts_the_parts_and_writes_their_union_sorted_with_lf` drive it
without the switch and read exit 0. No new case was written for S2,
because those two already pin it.

**A sentence the range made false, corrected.**
`Test_main::test_a_count_below_one_is_exit_2_naming_it` called the script's
exit codes "0-or-2". It now says a traceback is none of the script's exit
codes. `git grep -nE "0-or-2|0 or 2|exits 2|exit 2"` outside `seal/threads`
finds no other statement of the old codes (executed).

**What phase 2 needs.**

- The workflow half of *Scope* item 3 is not wired. `test.yml`'s union step
  passes no `--stale-fails`. The `durations` job's comment
  (`.github/workflows/test.yml:186-194`) still says the job is red only when
  the parts cannot make the whole. Phase 2 rewrites that comment with the
  step.
- Both answers to `frame/questions.md` Q2 work with the script as it
  stands:
  - The switch on the union step makes that step exit 1. The upload then
    needs a condition that still runs after a red step whose union was
    written.
  - A separate last step can run the script again with `--stale-fails`
    over the same `parts`, writing `--out` to a path of its own. The union
    step and the upload then stay as they are.

  `test_the_durations_job_needs_pytest_and_runs_unless_cancelled` reads the
  union step's words in pairs. A bare flag on that step changes what it
  parses.
- `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`
  still holds everything *Removes* rows 1 to 4 name: the suite case,
  `unpriced`, `dead`, `staleness`, `REMEDY`, `STALE_SHARE`, `_collection`,
  `_with_gone`, `FIXTURE_SIZE`, `AT_THE_SHARE` and the seven fixture cases.
  Each fixture case now has its rewrite in the script's file:

  | Old case | Its rewrite |
  |---|---|
  | `test_exactly_the_share_unpriced_passes` | `Test_verdict::test_accepts_exactly_the_share_on_each_side` |
  | `test_dead_seconds_past_the_share_fail_and_at_the_share_pass` | the same case, and `Test_verdict::test_refuses_one_more_dead_second_naming_the_seconds_and_the_first` |
  | `test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe` | `Test_verdict::test_refuses_one_more_unpriced_naming_the_counts_and_the_remedy` |
  | `test_an_empty_collection_is_refused` | `Test_staleness::test_refuses_an_empty_union` |
  | `test_an_entry_nobody_collects_is_not_counted` | `Test_staleness::test_accepts_an_entry_no_part_ran_as_dead_and_never_unpriced` |
  | `test_both_sides_over_are_named_in_one_sentence` | `Test_verdict::test_refuses_both_sides_over_in_one_sentence` |
  | `test_an_empty_file_is_all_unpriced_and_nothing_gone` | `Test_verdict::test_refuses_an_empty_file_as_all_unpriced_and_nothing_dead` |

- Phase 2's `git grep -n 'prices_the_suite\|STALE_SHARE'` lists the
  behaviour module until those rows go. After that it lists the script,
  its cases and `CONTRIBUTING.md`.
- `REMEDY` ends by citing `CONTRIBUTING.md` *Running the checks*. That
  section still gives the per-branch recipe (`CONTRIBUTING.md:162-191`).
  It agrees with the sentence only once phase 2 rewrites the paragraph as
  *Scope* item 4 gives it. The S5 case phase 2 rewrites can check the
  paragraph against the sentence's terms: the trailer, the branch cut from
  `release/vX.Y.Z`, and the pull request into it.

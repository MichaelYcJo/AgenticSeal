# 1791876667-the-durations-refresh-has-a-schedule — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | e473f13e |
| Ran by | specseal:smith on Opus 5.5, as `routing.md` names it |

## What this phase was asked

The reframe after round 4, the one phase of it. `REMEDY` gives the whole
restate command, `python3 .github/scripts/budget_check.py --baseline
origin/<base> --restate-price`, and says what `<base>` is; the assertion
near line 401 pins that whole command and is seen red against 9021bc49's
`REMEDY` before the constant changes. `budget_check.py` gains one
`expected_level(base_level, ratio)` beside `price_problems`, called by
`price_problems` and by `check`'s restate branch, so `git grep -n
'seconds(base_level' .github/scripts/budget_check.py` shows one line. Work
item 1791876665's `spec.md` `slow-file:<path>` Kind cell and its
`questions.md` gate-or-report bullet say `report` with the grounds,
rewritten in place. This item's `changelog.md` gives the full command.
Verified by the four modules, the grep, and the command `REMEDY` gives,
typed with `<base>` as `release/v0.22.0` over run 38655519975's union,
exiting 1 and not 2, with `.test_durations` and `seal/budgets.md` restored
after.

## What this phase found

- **The frame held at every coordinate it named.** `REMEDY` at line 284,
  the assertion at line 401, the two copies of the expression at
  `budget_check.py` lines 1396 and 1423, 1791876665's `spec.md:36` and
  `questions.md:8`, and this item's `changelog.md:23` all read as the
  reframe described them at 9021bc49, and the tip 179e8ef3 had not moved
  either file since.
- **How the red was shown.** The assertion was changed first, with
  `REMEDY` still byte-identical to 9021bc49's (`git diff --quiet 9021bc49
  HEAD` on both files, exit 0). `bin/test
  tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q -p
  no:xdist -k test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe`
  exited 1, failing at line 401 on the whole command. The constant changed
  after that, and the same case passed in the module run below.
- **`expected_level` has something behind it.** `bin/mutation-check` with
  its `return` given `+ 1`, over `tests/test_a_budget_ratchets.py`: `red`,
  10 of 159 cases failing, among them
  `test_restate_price_writes_the_level_a_refresh_implies` and
  `test_the_price_level_follows_the_durations_file_and_nothing_else`. The
  file was restored and the tree read clean.
- **The command ran by the script's absolute path.** The spawn forbade a
  `cd` into the worktree, so `.github/scripts/budget_check.py` was given
  by its full path. The script's `--root` defaults to its own repository,
  so this is the same run the relative spelling makes from the root. On
  run 38655519975's union it exited 1. It wrote 1136 per mille into
  `## Price level`, one line of `seal/budgets.md`, and named the 20
  `Budget removed:` lines a body would carry, which is what round 4's
  run with the baseline gave. Nothing said `--baseline` was missing.
- **One copy of the old `slow-file` text stays in 1791876665.** That
  item's `overview.md:24` quotes the spec's former "a file not listed that
  crosses 120 s fails (the list may not grow)" as the clause its phase 2
  built against. It is a divergence record of that build, which the frame
  did not name, so it is left as written and handed back.
- **No ledger rows.** The evidence ledger left the tree with #944, and
  this phase has no fragment to write.

`executed` 2026-10-15, exit read directly:

- `bin/test tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py
  tests/test_a_budget_ratchets.py
  tests/test_every_reader_ends_a_line_where_gfm_does.py
  tests/test_a_reader_declares_its_input_class.py -q`: exit 0, 415 passed,
  2 skipped.
- `git grep -n 'seconds(base_level' .github/scripts/budget_check.py`: one
  line, `:1424`, the `return` of `expected_level`.
- The two `## Removes` texts of the reframe, `grep -c -F`: 0 each.
- `bin/test tests/test_docs_line_wrap.py
  tests/test_the_changelog_is_gathered_at_release.py
  tests/test_no_real_identifiers.py tests/test_one_word_one_meaning.py -q`:
  exit 0, 116 passed.
- `uvx ruff check` and `uvx ruff format --check` on the two changed
  Python files: exit 0 each.

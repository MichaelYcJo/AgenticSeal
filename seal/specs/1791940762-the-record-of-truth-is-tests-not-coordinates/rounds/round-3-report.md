# 1791940762-the-record-of-truth-is-tests-not-coordinates — round 3 report

Verifying round over `04edf1aa..ce1795fa` (three commits: the fix 005919e3,
the overview paperwork fa8f9872, and round 2's close ce1795fa), reviewed at
`ce1795fad460ffa4025bfd492bef934b060ddb8d` in a `git clone --no-local` of the
worktree, against `origin/release/v0.22.0` at f975ea66 (the merge base).

## What the account asserted, and what the tree has

- **Claimed:** `tests/test_pact_check.py`'s ceiling is now 157, 1.3 times its
  121 s reading, and the PR body says `120 -> 157`. **Found:**
  `seal/budgets.md:73` reads 157. The file's raw `.test_durations` total is
  136.62 s; at the price level x1.132 that is 120.69 s, and 1.3 times that is
  156.89, which `seal/budgets.md:15-17` rounds up to 157. The PR body carries
  exactly one `Budget raised:` line, the `120 -> 157` one (executed: `gh pr
  view 950`).
- **Claimed:** the checker passes with the body and refuses without it.
  **Found (executed):** exit 0 with the body, 36 s headroom (22.9 %). Exit 1
  with an empty body, and the run's only refusal line names
  `slow-file:tests/test_pact_check.py` and asks for `120 -> 157`. A body whose
  line still says `120 -> 121` also exits 1, and the refusal quotes the stale
  value, so the check reads the number and not only the presence of a line.
- **Claimed:** the removed `Budget removed: ledger-rereads` line and the six
  `unenforced:` `Budget raised:` lines were inert. **Found (executed):** the
  empty-body run refuses one line only. Nothing else in the budget table asks
  the body for a declaration, so removing them changed no verdict.
- **Claimed (round 2's ⬜ 2):** the overview now says what the tree has, in
  its three places. **Found:** each place is true now.
  - `overview.md:34`: the row now reads "pruned, then refreshed". Executed:
    `.test_durations` held 11,863 entries before 8a63e245 and 9,208 after it,
    which is the 2,655 the row names. Run 38646055747 is a `pull_request` run
    at e05213e0, and its Windows leg ran with `--store-durations
    --clean-durations` and no split. That leg's three failures are the three
    cases in `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`
    that the temporary unsharding was expected to break. None of them is a
    timing failure, so the measurement is the one the row describes (read,
    from the run's failed log).
  - The `Not verified` row that said the durations case is red is gone, and
    executed: `test_the_durations_file_prices_the_suite` passes at the tip.
  - The bullet about the roughly 37 ledger ids and 2,600 pact ids left in the
    file is gone, and executed: no id in `.test_durations` names a file that
    is missing from the tree. Six ids mention `ledger`, and each one is a
    parameter or a name of a case that still exists.
- **Nothing else changed in the range** (executed: `git diff --stat
  04edf1aa..ce1795fa`). Three files changed: `seal/budgets.md` (one row),
  `overview.md` (one row rewritten, one row and one bullet removed), and
  `rounds/round-2.md`. The round-2 edits fill the four fields the close
  writes and set finding 1's verdict to `fixed 005919e3`. The fix range named
  there, `04edf1aa..005919e3`, holds one commit, as the field says. No unit
  was added, so `New units` is none.

## ⬜ 1 — the changelog's suite figure is in the base's prices, and the committed file no longer is

This is outside the range, and it was opened because `round-record`'s
chain check names the fragment: it last changed before 8a63e245, which no
round's fix range holds. `changelog.md:49` says "the suite's priced total
fell by 796.5 seconds". That figure is the base file's price for the
deleted cases, 777.4 for the deleted modules plus 19.1 for cases cut from
kept ones, and it still holds as that. The executed totals are these:

- the base's `.test_durations`, at price level 1000: 7,861.7 s;
- the pruned file before 8a63e245: 7,066.9 s, which is the 796.5 fall;
- the refreshed file at the tip: 7,758.7 s raw, 6,854 s at x1.132.

So a reader who checks the release note against the committed file finds
a fall of 1,008 priced seconds, or 103 raw ones, and never 796.5. The
behaviour and the measurement are both right, and only the sentence does
not say which prices it is in. Its location is under `seal/specs/`, so it
is a correction and is not counted in `Needs a fix`. A wording that says
which prices it uses is fenced under `## Paste-ready fixes`. Whoever closes
the run's notes decides whether to apply it.

## What else was read

One place still names the old state and is left alone on purpose:
`phases/phase-8.md:105` says the case is red until "the same refresh
`overview.md` §*Not verified*" names. A phase record states what was true
when the phase ended. Rewriting it would rewrite history, so it is not a
finding.

Round 2's ⬜ 2 is carried and not re-reported. It closes at the run's end.
The 🟢 row below says only that its text is true now.

The PR's CI was read at the tip, not run: lint, release and both
arm-check-grammar legs pass, and every pytest leg was still pending when it
was read.

The broad gate has come due. This round leaves nothing open that needs a
fix, so the next act is the sealer's spawn, not a run for the reading session
to assemble. One step comes first. This record's ⬜ 1 keeps its `Pass` box
unticked until `round-record notes` closes the run's notes, round 2's ⬜ 2
with it. The dry run inside the clone showed this: without ⬜ 1 the box
ticked, and with it the box stays empty.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 2's finding 1 is closed — `tests/test_pact_check.py`'s ceiling is 157, 1.3 times its 120.69 s priced reading rounded up, and the PR body's one line says `120 -> 157` | `seal/budgets.md:73` | confirmed | executed: `budget_check.py` exit 0 with the PR body (36 s headroom), exit 1 with an empty body naming only that line, exit 1 with a stale `120 -> 121` line quoting it; read: `seal/budgets.md:15-17` |
| 🟢 | the overview text round 2's note 2 named now says what the tree has, in all three places | `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/overview.md:34` | confirmed | executed: entries 11,863 to 9,208 across 8a63e245; no id names a missing file; the durations case passes; read: run 38646055747's Windows leg is unsharded with `--clean-durations`; the note itself is carried and closes at the run's end |
| 🟢 | the range changes nothing beyond the fix, the overview paperwork and round 2's close | `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/rounds/round-2.md:10` | confirmed | executed: `git diff --stat 04edf1aa..ce1795fa` is three files; the close's fix range holds one commit; no new unit |
| 🟢 | the lines removed from the PR body were inert | PR #950 body | confirmed | executed: with an empty body the checker's only refusal is the `slow-file:tests/test_pact_check.py` raise |
| ⬜ 1 | the changelog's "the suite's priced total fell by 796.5 seconds" is in the base's prices, and the refreshed `.test_durations` prices the suite at x1.132, a fall of 1,008 priced seconds against the base | `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/changelog.md:49` | open | executed: totals 7,861.7 at the base, 7,066.9 before 8a63e245, 7,758.7 raw at the tip; read: the fragment last changed at 7b8edffb, before 8a63e245; paperwork, not counted in `Needs a fix` |

## Paste-ready fixes

```markdown
  Measured against the merge base `f975ea66`: the branch is 4,302 lines in
  and 54,867 out, and 19.1 more Windows seconds left with cases cut from
  kept modules, so the deleted cases cost 796.5 seconds at the base's
  prices. The refreshed `.test_durations` prices the whole suite at 6,854
  seconds against the base's 7,862.
```

## Executed probes

| What was run | Result |
|---|---|
| `python3 .github/scripts/budget_check.py --root <clone> --baseline origin/release/v0.22.0 --pr-body-env PRB --base-ref release/v0.22.0`, with `PRB` from `gh pr view 950 --json body -q .body`, at ce1795fa | exit 0; `slow-file:tests/test_pact_check.py` 121 s (raw 137 at x1.132) against 157, 36 (22.9 %) headroom; "every gate row holds" |
| the same with `PRB` empty | exit 1; one refusal line, naming only `slow-file:tests/test_pact_check.py` `120 -> 157` |
| the same with the body's line edited to `120 -> 121` | exit 1; the refusal quotes "The body's line says 120 -> 121" |
| `python3` over `.test_durations`: the file's total for `tests/test_pact_check.py`, entry counts at 8a63e245's parent, 8a63e245 and HEAD, ids naming a missing file | 136.62 s raw, 120.69 s priced, 156.89 at 1.3 times; 11,863 / 9,208 / 9,208; no missing file; six `ledger` ids, each a case that exists |
| `bin/test tests -q -k test_the_durations_file_prices_the_suite` in the clone | 1 passed, exit 0 |
| `.test_durations` totals at f975ea66, 8a63e245's parent and HEAD | 7,861.7 s / 7,066.9 s / 7,758.7 s raw (6,854 at x1.132); the base's price level is 1000 |
| `round-record new` on this report, inside the clone, then discarded with it | run twice, exit 0 both times. The first run, before ⬜ 1 was written, ticked `Pass`; its chain check printed the changelog-fragment notice that led to ⬜ 1. The second run, with ⬜ 1 in the table, left `Pass` unticked. `Needs a fix` read no both times |
| `gh run view 38646055747` and its failed log | read, not run: a `pull_request` run at e05213e0; the Windows leg ran with `--store-durations --clean-durations` and no split; its 3 failures are in the shard test module |
| `gh pr checks 950` | read, not run: lint, release and arm-check-grammar pass; every pytest leg pending |
| the broad gate (full suite, lint, typecheck) | not yet — the sealer's, once, after the rounds settle; nothing above stands for it |

Needs a fix: no
Loses a record or crashes: no

## Proof block

Files opened this round: `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/rounds/round-2.md`,
the diff of `seal/budgets.md` and `overview.md` over `04edf1aa..fa8f9872`, the
diff of `rounds/round-2.md` over `fa8f9872..ce1795fa`, `seal/budgets.md:10-20`,
the argument list of `.github/scripts/budget_check.py`, `bin/test`, the
checker's three outputs, `.test_durations` at four commits, the work item's
`changelog.md`, `seal/budgets.md`'s price level at f975ea66, and the PR body.

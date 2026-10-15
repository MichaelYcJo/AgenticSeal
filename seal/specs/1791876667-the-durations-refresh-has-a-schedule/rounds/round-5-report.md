# Round 5 report — 1791876667-the-durations-refresh-has-a-schedule (#931)

Reviewed by warden (Opus 5.5) on 2026-10-15, at a6919ade, in a
`git clone --no-local` of the branch at that SHA, against
`origin/release/v0.22.0` at 5b1f6fae (the worktree's remote-tracking ref,
fetched into the clone). This is the first round after the reframe at
5e195708. Its target is phase 4, `179e8ef3..a6919ade` (8dccf1a8, e473f13e,
a6919ade), read against `plan.md` row 4 and the reframed `spec.md` In 3,
In 7, S4 and S9, and then the branch as a whole, briefly: the PR body and
the records against the tree. Rounds 1 to 4 were read for coordinates.
Round 4's three open verdicts are answered below.

## Summary

Phase 4 does what its plan row asks. Two things the branch changed in
round 3 are still described wrongly elsewhere, and one of them is a
behaviour the tree lost.

- **The phase holds (executed).** The restate command, typed as `REMEDY`
  gives it, exits 1 and writes one line. With the PR body it exits 0. The
  case that pins the command goes red against the old `REMEDY`.
  `expected_level` is the one expression of the level, and a mutation of
  it turns both the writer's case and the check's case red.
- **Round 4's ⬜ 3 is only half closed (🟡 1).** Work item 1791876665's
  `slow-file` row and its questions bullet now say `report`. Its S7 still
  says an unlisted slow file is "exit 1 naming the file". The tree exits 0
  on that input.
- **1791876665's changelog fragment still describes a gate (🟡 2).** It
  says each slow file is "held to a ceiling" and that "Two reports fail
  nothing". The release gathers that fragment word for word, and 0.22.0
  ships three reports.
- **A report row never prints its problems, so an unlisted slow file is
  no longer named (🟡 3).** The family's summary line reads `266 seconds
  (largest unlisted) … report | over` and gives no path. The PR body, this
  item's changelog and `seal/budgets.md` all say each file's reading
  prints.
- **The two things the implementer left on purpose both stand (🟢).**

## 1. Phase 4 against its plan row

**`REMEDY` gives a command the checker runs (executed).** The test module
now holds the whole command at
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:284-286`.
In the clone I copied run 38655519975's union over `.test_durations` and
typed `python3 .github/scripts/budget_check.py --baseline
origin/release/v0.22.0 --restate-price` from the root. The result:

- exit 1, not 2;
- the summary says "`--restate-price` wrote 1136 per mille";
- `git diff` showed one line of `seal/budgets.md` changed, 1132 to 1136;
- the 20 `Budget removed:` problems remained, which is the branch's own
  gate-to-report change with no body to declare it.

The same command with `--pr-body-env` carrying PR #937's body exits 0,
"every gate row holds". Both writes were reverted afterwards.

**The case is seen red (executed).** I set `REMEDY` back to its 9021bc49
text, the short `budget_check.py --restate-price` form, and kept the new
assertion. `test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe`
exits 1 at the assertion on the whole command. The phase record's account
of how it showed the red (`phases/phase-4.md`) matches this.

**One expression (read and executed).** `git grep -n 'seconds(base_level'`
over the checker prints one line, `:1424`, the `return` of
`expected_level`. `price_problems` (`:1434`) and the restate branch of
`check` (`:1397`) both call it. Its message's
`{base_level} x {ratio:.3f} = {expected}` formats the value that
`expected_level` returned, so it is no second copy. I gave the `return`
a `+ 1`. Then
`test_restate_price_writes_the_level_a_refresh_implies` and
`test_the_price_level_follows_the_durations_file_and_nothing_else` ran,
and 3 cases failed. The plan's claim that the existing case pins the
writer against the check holds, so no new case is owed.

**1791876665's records (read).** `spec.md:36` and `questions.md:8` say
`report`, give the 0.67–1.72 measurement and #931, and tell no story of
what they said before. The reframe asked for exactly that. The rest of the
row stays as it was. Both `## Removes` texts of the reframe are gone from
the tree. S7 in the same spec was missed. It is §2 below.

**This item's changelog (read).** `changelog.md:23-25` gives
`python3 .github/scripts/budget_check.py --baseline origin/<base>
--restate-price` and says what `<base>` is. Line 50 names it again in the
short form with `--baseline`. That line refers to the command and gives no
recipe, so it is fine.

The narrow modules the plan names all pass: 415 passed and 2 skipped,
exit 0. So do the record checks (line wrap, changelog gathering, no real
identifiers, one word one meaning): 116 passed, exit 0.

## 2. 1791876665's S7 still says a slow file fails (🟡 1)

Round 4's ⬜ 3 named the spec saying `slow-file` "is a gate that fails an
unlisted file over 120 s". Phase 4 rewrote the row at `spec.md:36`. The
acceptance scenario at `spec.md:59` still reads:

> S7 a slow file appears · a test file not listed reaches ≥ 120 s in
> `.test_durations` · exit 1 naming the file

**Executed.** In the clone I added 300 s to one case of
`tests/test_docs_line_wrap.py`, which is not listed. Then I ran the
checker with no baseline. It exits 0, "every gate row holds", and the
family's line reads `266 seconds (largest unlisted) | 120 | -146 (-121.7%)
| report | over`.

**Why it matters.** This spec is what `settle` folds into `docs/` at the
release. That was the reframe's own reason for rewriting the Kind cell.
The spec's S9 says "neither record names `slow-file` among the gates".
S7 is a gate's behaviour, written as an acceptance criterion. A fold
would carry it into a policy document that the tree contradicts.

This is a finding located in a record. So under
`docs/review-chain-spec.md` §*The last round verifies* it is a correction:
it closes `answered` with `corrected at <sha>`, and `Needs a fix` does
not count it. The fix assumes 🟡 3's fix lands. Without that fix, "names
the file" is false too.

## 3. 1791876665's changelog fragment describes the gate that no longer ships (🟡 2)

`seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/changelog.md:17-19`:
"The suite's seconds and each slow file … are held to a ceiling 1.3 times
their reading". And `:27`: "Two reports fail nothing: the largest round
records in the tree, and how many rows a release re-read."

**Read.** `seal/budgets.md:41` makes `slow-file` a `report` row, so each
slow file has a ceiling and is held to nothing. The tree carries three
report families, not two. The release gathers both fragments verbatim
into the 0.22.0 section. Under *Added* a reader would get a slow-file gate
that never shipped. Under *Changed*, this item's fragment would say "this
change makes the `slow-file` rows … `report` rows". That changes a state
no release ever had.

`docs/the-record-layout.md` §*A commit after the build brings its changelog
fragment along* names this class: "a later commit that changes behaviour
can leave it describing something that no longer ships", and 0.18.2
shipped three such fragments. The rule binds a work item's own fragment.
Here e16fcabb, a commit of this branch, made another item's fragment false,
and `chain_check`'s notice reads only this item's fragment. So nothing
mechanical names it.

The sentence is located in a record, so it is a correction like 🟡 1 and
`Needs a fix` does not count it.

## 4. A report row drops its problems, so an unlisted slow file goes unnamed (🟡 3)

`.github/scripts/budget_check.py:1410` collects problems only from rows
whose kind is `GATE`. `render` (`:1217`) prints one line per row, and for a
family it writes only `(largest unlisted)` beside the value (`:1265`). The
sentence `unlisted_band` builds, "`<path>` is not listed and measures …",
is the only place the path appears. For a `report` row it is computed and
then thrown away.

**Executed.** This is the same probe as §2. A 266-second unlisted file
gives exit 0. The `slow-file` line in the summary reads `over`, and no
line in the output names `tests/test_docs_line_wrap.py`.

**Failure scenario.** A pull request adds a test file that runs 200 s.
The budget step is green, as a report should be. The summary says the
`slow-file` family is `over` and gives no file. The release lowers these
rows from the trend, and `seal/budgets.md` says "every test file whose
reading times 1.3 reaches the 120 s threshold is listed". Whoever lists
it has to rebuild the per-file sums by hand to learn which file it is.

**What the records claim.** Three places say every reading prints:

- PR body item 4: "The rows still print every file's reading";
- this item's `changelog.md:45`: "each file's reading still prints in the
  summary and fails nothing";
- `seal/budgets.md:19-21`: "each file's reading is printed in every
  summary".

Each is true for the twenty listed files and false for the file the list
is missing.

The mechanism is #930's: `rounds-bytes` was already a report. The branch
is what made it matter for `slow-file`, in e16fcabb. It sits in `check`
and `render`, neither of them a unit an earlier round's fixes created.

The fix below adds a list under the table, with each report row's
problems and the heading "failing nothing". Tried in the clone: the new
case passes with the fix and fails without it (exit 1). With the fix,
`tests/test_a_budget_ratchets.py` and
`tests/test_a_reader_declares_its_input_class.py` give 236 passed, exit 0.
The §2 probe then names the file. The sentence it prints still ends with
`unlisted_band`'s "Bring it under, or list it there and write `Budget
raised:` …". Under the "failing nothing" heading I read that as advice
rather than a demand. The smith may prefer to word it for a report row.

## 5. The two things left on purpose

**1791876665's `overview.md:24` stands (read).** The row is a divergence
record. Its second column is, by the table's shape, what the frame said
when phase 2 built: "a file not listed that crosses 120 s fails (the list
may not grow)". The decision in its third column still holds in the tree:
the family's own row holds every file its table does not list, at 120 s.
The §2 probe read exactly that. Rewriting the quoted column would make
the record say the frame said something it did not. Settle folds what is
still true, and this row's claim about the frame is true.

**`seal/budgets.md:25`'s short pointer stands (read).** The sentence sits
inside the file's opening comment. It gives the flag's name and sends the
reader to `CONTRIBUTING.md` §*Running the checks* "as … gives the
command". It does not offer itself as a command to type. The checker's
own usage line (`budget_check.py:19`) says "with --baseline". If someone
types the short form anyway, the exit-2 refusal says what is missing:
"--restate-price was given without --baseline", which round 4 executed.

## 6. The PR body and the records against the tree

- **Item 2's command (read and executed).** It is the `--baseline` form,
  which now matches `REMEDY`. Round 4's 🟡 1 was this mismatch, and it is
  closed.
- **The 20 `Budget removed:` lines (executed).** The checker names
  exactly 20 removals, and the body clears them: exit 0.
- **Item 4 (read).** "The rows still print every file's reading" is
  🟡 3's third coordinate.
- **"538 passed, 2 skipped" (not run).** This round did not run it. Round
  4 recorded the same, and phase 4's own runs were 415 and 116 over other
  module sets. The row names no SHA, so it is the implementer's figure. I
  leave it as that and it is not a finding.
- **This item's `overview.md:7-8` (⬜ 4).** The closing memo still lists
  "S1–S8" and "`plan.md` (phases 1–3 …)". The reframed spec has S9 and the
  plan has phase 4. The memo's evidence line counts mutation breaks for
  phases 1 and 2 only, while phase 4 recorded its own mutation (10 of 159
  red). This is prose in a record that no check reads, so it is a ⬜.

## Regression tests to plant

- `tests/test_a_budget_ratchets.py`, beside
  `test_a_slow_file_is_reported_and_the_suite_seconds_are_gated`: a
  report-kind `slow-file` family with an unlisted 130-second file exits 0
  and its summary names the file. The case is in the 🟡 3 fence below.
  NAME NOT IN TREE: its proposed name, `test_an_unlisted_slow_file_under_a_report_row_is_named`.
  I showed it red in the clone: exit 1 without the fix, passing with it.

## Facts for the record

- Run 38655519975's union over 5b1f6fae restates the level to 1136 per
  mille, from 1132. This is the same number round 4 read.
- At a6919ade the repository's summary prints `suite-seconds` 7,119 s (raw
  8,059 at x1.132) against a ceiling of 9,185.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | work item 1791876665's S7 still says an unlisted slow file is "exit 1 naming the file"; the family is a `report` row and the tree exits 0; round 4's ⬜ 3 is closed at `spec.md:36` and `questions.md:8` and not here | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:59` | open | executed: an unlisted file at 266 s gives exit 0 and an `over` report line; read: `spec.md:59`, S9 of this item's spec; a record correction, which `Needs a fix` does not count |
| 🟡 2 | work item 1791876665's changelog fragment says each slow file is "held to a ceiling" and "Two reports fail nothing"; 0.22.0 ships `slow-file` as a third report, and the fragment is gathered verbatim | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/changelog.md:17` | open | read: `:17-19`, `:27`, `seal/budgets.md:41`; `docs/the-record-layout.md` §*A commit after the build brings its changelog fragment along*; a record correction, which `Needs a fix` does not count |
| 🟡 3 | a `report` row's problems are never printed, so an unlisted file past the `slow-file` threshold is not named anywhere; the PR body, this item's changelog and `seal/budgets.md` say each file's reading prints | `.github/scripts/budget_check.py:1410` | open | executed: an unlisted file at 266 s gives `266 seconds (largest unlisted) … report \| over` and no path in the output; read: `render` `:1265`, `unlisted_band`; the fix tried in the clone, its case red without it |
| ⬜ 4 | this item's closing memo lists S1–S8 and phases 1–3 and phase 1–2 mutation counts; the reframed spec has S9 and the plan phase 4 | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/overview.md:7` | open | read: `overview.md:7-8`, `spec.md` S9, `plan.md` row 4, `phases/phase-4.md` |
| 🟢 | round 4's blocking finding is closed — the staleness message gives the whole restate command, and the case asserts it | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:284` | confirmed | executed: the command as typed exits 1 and writes one line, exit 0 with the PR body; the case exits 1 against 9021bc49's `REMEDY` |
| 🟢 | round 4's note 2 is closed — the price level has one expression, which the writer and the check both call | `.github/scripts/budget_check.py:1418` | confirmed | executed: the grep prints `:1424` alone; `+ 1` on its `return` turns 3 cases red, among them the writer's and the check's |
| 🟢 | the phase-4 records: 1791876665's `slow-file` Kind cell and questions bullet say `report` with no history narrative; this item's changelog gives the full command | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/questions.md:8` | confirmed | read: `spec.md:36`, `questions.md:8`, `changelog.md:23-25`; both `## Removes` texts absent |
| 🟢 | 1791876665's `overview.md:24` quoting the frame's old clause is left as written | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/overview.md:24` | confirmed | read: a divergence row's second column is what the frame said when phase 2 built; its decision still holds (executed: the family row holds an unlisted file at 120 s) |
| 🟢 | `seal/budgets.md:25`'s short `--restate-price` pointer is left as written | `seal/budgets.md:25` | confirmed | read: a comment that names the flag and points at the recipe for the command; the bare form's exit 2 names `--baseline` |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` over the four modules plan row 4 names | exit 0, 415 passed, 2 skipped |
| `bin/test` over line wrap, changelog gathering, no real identifiers, one word one meaning | exit 0, 116 passed |
| run 38655519975's union over `.test_durations`, `python3 .github/scripts/budget_check.py --baseline origin/release/v0.22.0 --restate-price` | exit 1; wrote 1136 per mille, one line of `seal/budgets.md` changed; 20 `Budget removed:` problems; reverted |
| the same with `--pr-body-env` holding PR #937's body | exit 0, "every gate row holds"; reverted |
| T8 against 9021bc49's `REMEDY` with the new assertion | exit 1 at the whole-command assertion; file restored |
| `expected_level`'s `return` given `+ 1`, the writer's and the check's cases | exit 1, 3 failed; file restored |
| 300 s added to one case of `tests/test_docs_line_wrap.py`, checker with no baseline | exit 0; `slow-file` line `266 seconds (largest unlisted)`, `report`, `over`; no path printed; reverted |
| 🟡 3's fix and case in the clone | with the fix: exit 0, 236 passed over two modules, and the probe above names the file; without it: the case exits 1 |
| the full suite, lint and typecheck at a6919ade | not yet — not this round's to run; the sealer runs it once the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

## Paste-ready fixes

### 🟡 1 — `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:59`

```markdown
| S7 a slow file appears | a test file not listed reaches ≥ 120 s in `.test_durations` | exit 0: the family is a `report` row (#931), so its summary line reads `over` and the list of report rows past their band names the file |
```

### 🟡 2 — `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/changelog.md:17-29`

```markdown
  3. The suite's seconds and each slow file are read off one run's
     `.test_durations`, so each has a ceiling 1.3 times its reading with no
     lower band. The suite's seconds are a gate. A slow file is a report,
     because one union moves a single file 0.67 to 1.72 times the level
     from the next. A refresh restates one number, its price level, rather
     than every seconds ceiling, so a refresh on faster or slower runners
     fails nothing, and a cleanup of one file moves only that file.
  4. Each leg's minutes are read off the run itself by a `budgets` job
     after the suite, held to a ceiling with no lower band, and printed with
     the run's billable minutes, priced at a figure the line says to check
     against GitHub's price list.
  5. Three reports fail nothing: each slow test file, the largest round
     records in the tree, and how many rows a release re-read. A release
     pull request prints every budget against the last release tag.
```

### 🟡 3 — `.github/scripts/budget_check.py`, in `render`, before `if moves:` (`:1272`)

```python
    noted = [
        (result.row.name, problem)
        for result in results
        if result.row.kind == REPORT
        for problem in result.problems
    ]
    if noted:
        lines += ["", "Report rows past their band, failing nothing:", ""]
        lines += [f"- `{name}`: {problem}" for name, problem in noted]
```

The case, in `tests/test_a_budget_ratchets.py` after
`test_a_slow_file_is_reported_and_the_suite_seconds_are_gated`:

```python
def test_an_unlisted_slow_file_under_a_report_row_is_named(tmp_path, capsys):
    """S7 under the kind this repository gives the family: a test file that
    crosses the threshold unlisted fails nothing, and the summary names it,
    because the family's own line reads only the largest unlisted value."""
    head = budgets(("slow-file", "seconds", 120, "one-sided", "report")) + table(
        "Seconds ceiling", []
    )
    root = tree(tmp_path, head, files={".test_durations": json.dumps(SMALL)})
    assert run(root) == 0
    out = capsys.readouterr().out
    assert "Report rows past their band, failing nothing:" in out, out
    assert (
        "- `slow-file`: tests/test_a.py is not listed and measures 130 seconds"
        in out
    ), out
```

Needs a fix: yes — 🟡 3, a report row's problems are never printed, so an unlisted slow file is not named; 🟡 1 and 🟡 2 are record corrections that `Needs a fix` does not count

Loses a record or crashes: no

## Proof block

Opened in the round's clone at a6919ade:

- `.github/scripts/budget_check.py` — lines 1–30, 130–170, 1080–1100, 1217–1290, 1335–1470, 1600–1654
- `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` — lines 265–300, 389–412, 770–800
- `tests/test_a_budget_ratchets.py` — lines 455–485, 595–625, 672–700
- `CONTRIBUTING.md` — lines 165–200
- `seal/budgets.md` — lines 1–45
- `seal/specs/1791876667-the-durations-refresh-has-a-schedule/` — `spec.md`, `plan.md`, `changelog.md`, `overview.md`, `phases/phase-4.md`, `rounds/round-4.md`, `rounds/round-4-report.md` (header and layout)
- `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/` — `spec.md` lines 24–70, `questions.md`, `changelog.md` lines 1–40, `overview.md` lines 15–30
- `docs/the-record-layout.md` — lines 47–80
- `docs/review-chain-spec.md` — lines 230–277, 374–420
- `skills/settle/SKILL.md` — lines 80–120
- PR #937's body, `gh pr view 937`

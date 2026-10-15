# Round 6 report — 1791876667-the-durations-refresh-has-a-schedule (#931)

Reviewed by warden (Opus 5.5) on 2026-10-15, at 701bc6c1, in a
`git clone --no-local` of the branch at that SHA, against
`origin/release/v0.22.0` at 5b1f6fae (fetched into the clone). This is a
verifying round. Its target is round 5's fix range,
`bbf2daa3..af18ab2e` (21ffe7fb, 4a61fb66, a3df4afd, 11159605, af18ab2e),
plus 701bc6c1, which closes round 5's record. Rounds 1 to 5 were read for
coordinates. The one new unit round 5 named,
`test_an_unlisted_slow_file_under_a_report_row_is_named`, was judged as
code.

## Summary

Round 5's three fixes hold, and the code in the range is correct. What is
left is four notes, and none of them changes what the tree does.

- **The checker now names an unlisted slow file and fails nothing
  (executed).** On the real tree, a test file pushed to 266 s unlisted
  gives exit 0. The `slow-file` line reads `over`, and the new list under
  it names the file. The new case goes red against both earlier versions
  of the checker.
- **A gate row's message is unchanged byte for byte (executed).** A probe
  compared the problems of every row of `seal/budgets.md`, as a gate and as
  a report, against the checker at bbf2daa3. There were 624 comparisons and
  no gate difference. A report row differs only in its last clause.
- **1791876665's changelog fragment still counts a report the tree no
  longer has (⬜ 1).** a3df4afd rewrote item 5 to "Three reports", and the
  third is `ledger-rereads`. #944 removed that row on the base, so the
  0.22.0 notes would advertise a report that 0.22.0 does not ship.
- **The open question gets a yes (⬜ 2, ⬜ 3).** S7 now describes the
  `report` kind. The one case linked to it, T10, asserts exit 1 under a
  `gate` fixture. The plan row and T10's docstring both need the new
  report-kind case beside T10, and T10 should stay.
- **A docstring paragraph was edited in place and not reflowed (⬜ 4).**

## What each fix does at its commit

### Round 5's finding 3 — render names the file (21ffe7fb, af18ab2e)

`render` at `.github/scripts/budget_check.py:1284-1294` collects every
problem of a `report` row and prints them under "Report rows past their
band, failing nothing:". A failing problem is still built only from gate
rows, at `:1432-1434`, so the new list changes no exit code. Read: a
result whose row was not read on this run carries no problems, so an
unread row adds nothing to the list.

af18ab2e changes the last clause of each report row's problem.
`band` (`:1067-1078`) and `unlisted_band` (`:1098-1109`) used to ask for a
`Budget raised:` line. Now they print "a report row's raise needs no
`Budget raised:` line" or "a report row's listing needs no `Budget raised:`
line". Read against `ratchet` (`:1169-1171`): a base row that is not a gate
is skipped, so the new clause is true. A file row takes its family's kind
when `parse_budgets` builds it (`:436`), and `effective` copies the family
row (`:1146`), so a listing under a report family is skipped as well.

One case is left out on purpose. Suppose a row was a gate at the base and
is a report at the head, and it is also over its ceiling. Its problem says
no raise line is needed, and `ratchet` still asks for a `Budget removed:`
line for the change of kind. The two messages say different things, and
both are true. This PR is that case, and its body declares the 20
removals. The checker exits 0 with that body and exits 1 with an empty one
(executed).

Executed for the new case, per §15 of the contract: the case exits 1
against bbf2daa3's checker, where the summary has no list. It exits 1
against 21ffe7fb's checker at `tests/test_a_budget_ratchets.py:714`, where
the listing still asked for a raise line. It passes at af18ab2e. The case
pins the heading, the unlisted path, both new clauses, and the absence of
"pull request body". It does not pin the family line's `over` verdict.
`test_a_slow_file_is_reported_and_the_suite_seconds_are_gated` pins that
verdict for a listed file, and the real-tree probe above showed it for an
unlisted one.

### The gate rows' messages

A probe file named test_tmp_* (since deleted) loaded the checker at
bbf2daa3 beside the one at 701bc6c1. For each of the 103 rows of the
tree's `seal/budgets.md`, it set the kind to `gate` and then to `report`.
It called `band` above the ceiling, above it with a detail sentence, and
far below it. For each per-file family it also called `unlisted_band`
with two files over the threshold and one under it. Every gate result was
equal to the old one. Every report result was the old text with the raise
clause replaced by the new one. Exit 0.

### Round 5's finding 1 — 1791876665's S7 (4a61fb66)

`spec.md:59` says exit 0, that the summary line reads `over`, and that the
list names the file. That matches the executed probe on the real tree.

### Round 5's finding 2 — 1791876665's changelog fragment (a3df4afd)

Items 3 and 5 no longer say each slow file is held to a ceiling. They say
the suite's seconds are a gate and each slow file is a report. That part
is fixed. The count in item 5 is not, and ⬜ 1 is about it.

1791876667's own fragment (`changelog.md:44-49`) states the report row and
its grounds once. Its new sentence about the list matches what `render`
prints. Read.

### 11159605 — round 5's ⬜ 4

The closing memo now names S1–S9 and phases 1–4. That note is carried
open to the run's end and is not reported again here.

### Nothing else in the range changed behaviour

The rest of the code diff is two docstrings and one comment. The test
diff is the one new case. The other modules that import the checker are
`tests/test_every_reader_ends_a_line_where_gfm_does.py` (149 passed) and
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` (in
the 191). Both are green. Read: the workflows call the checker with the
same flags as at bbf2daa3. On every pull request the summary now prints
one more section. On this branch that section is `rounds-bytes` at
151,863 bytes against 142,823, which is this work item's own round
records and fails nothing.

## Findings

### ⬜ 1 — 1791876665's fragment says three reports, and the tree has two

`seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/changelog.md:27-28`
reads "Three reports fail nothing: each slow test file, the largest round
records in the tree, and how many rows a release re-read." The last of
those is the `ledger-rereads` row. The base removed it in #944 (5b1f6fae),
and neither `seal/budgets.md` nor `.github/scripts/budget_check.py`
carries it at 701bc6c1 (executed: grep). The checker's summary lists two
report kinds, `slow-file` and `rounds-bytes`. The release gathers this
fragment word for word, so 0.22.0's notes would promise a report that
0.22.0 removes. Round 5's paste-ready fix kept the stale clause, and
a3df4afd applied it as written.

The same stale row has two more instances that the range did not touch.
They came from #944 landing on the base:
`seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:39`
still lists `ledger-rereads` in the budgets table, and settle folds that
file into `docs/`. `questions.md:8` of the same item gives it as a report.
`plan.md:40` and `:57` record what the plan was and can stay. This is
paperwork under `seal/specs/`, so it is a correction and `Needs a fix` does
not count it.

### ⬜ 2 — 1791876665's `plan.md:74` links S7 to the gate case alone

This is the implementer's open question, and the answer is yes. S7 now
says an unlisted slow file gives exit 0 and is named in the list. The row
links S7 to T10 alone, and T10 builds its tree with `slow()`, whose
family is a `gate` (`tests/test_a_budget_ratchets.py:474`). T10 asserts
exit 1. Suppose somebody deletes `render`'s list of report problems. S7
as written is then broken, and T10 stays green.

Settle is where this matters. It folds S7 into `docs/` with an
`Enforced by:` line (`skills/settle/SKILL.md`, *A standing statement has
one shape*), and the plan row is the pointer a settler follows. If the row
names T10 alone, the folded rule is held by a case that pins the opposite
kind.

T10 should stay. The `gate` branch of `unlisted_band` is still live code
for the `docs-history` and `unenforced` families, and for any repository
that declares `slow-file` a gate. The row needs the report-kind case
beside it, with the mutation that case kills. Paperwork, so a correction.

### ⬜ 3 — T10's docstring still says S7 fails

`tests/test_a_budget_ratchets.py:619-620` reads "T10, S7: a test file over
the threshold that the table does not list fails, naming it". At 701bc6c1,
S7 says that file fails nothing. The behaviour is right and the sentence
is wrong. A reader who follows the docstring from S7 lands on the gate
case, which is the same trap as ⬜ 2 but in a file that outlives the work
item.

### ⬜ 4 — a docstring paragraph was edited and not reflowed

21ffe7fb inserted a sentence into the module docstring and joined the
next two lines into one. `.github/scripts/budget_check.py:120` is now 135
characters inside a paragraph wrapped near 76. The same commit left
`:1231` ("at, and where the docs were") as a short line in the middle of
`render`'s docstring. This is the shape #844 fixed in another file. Ruff
does not select E501 here, so nothing flags it (executed: ruff exit 0).

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| ⬜ 1 | work item 1791876665's changelog fragment says "Three reports", and the third, `ledger-rereads`, was removed on the base by #944; the same row stands at that item's `spec.md:39` and `questions.md:8` | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/changelog.md:27` | open | executed: grep finds `ledger-rereads` in neither `seal/budgets.md` nor the checker at 701bc6c1 or 5b1f6fae, and the summary lists two report kinds; read: `changelog.md:27-28`, `spec.md:39`, `questions.md:8`; a record correction, which `Needs a fix` does not count |
| ⬜ 2 | work item 1791876665's `plan.md:74` links S7 to T10 alone, and T10 asserts exit 1 under a `gate` fixture; S7 now states the `report` kind, which only `test_an_unlisted_slow_file_under_a_report_row_is_named` holds | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/plan.md:74` | open | read: `plan.md:74`, `spec.md:59`, `tests/test_a_budget_ratchets.py:474` and `:604-622`, settle's *A standing statement has one shape*; the implementer's open question, answered yes; a record correction |
| ⬜ 3 | T10's docstring says an unlisted file over the threshold "fails" under S7; S7 says it fails nothing | `tests/test_a_budget_ratchets.py:619` | open | read: `:619-620` against `spec.md:59` of work item 1791876665; the behaviour is right and the sentence is wrong |
| ⬜ 4 | a module docstring line runs 135 characters after 21ffe7fb's insert, and `render`'s docstring keeps a short line mid-paragraph | `.github/scripts/budget_check.py:120` | open | executed: awk line lengths, ruff exit 0 (E501 not selected); read: `:113-121`, `:1229-1232` |
| 🟢 | round 5's finding 3 is closed — `render` prints every report row's problems under a heading that says they fail nothing, and an unlisted slow file is named | `.github/scripts/budget_check.py:1284` | confirmed | executed: the real tree with 300 s added to an unlisted file gives exit 0, `slow-file` `over`, and the list names the file; the new case red against bbf2daa3 and 21ffe7fb and green at af18ab2e; failing problems still come from gate rows alone (`:1432-1434`, read) |
| 🟢 | a gate row's problem text is unchanged byte for byte across the range; a report row's differs only in its last clause | `.github/scripts/budget_check.py:1067` | confirmed | executed: probe over all 103 rows, `band` and `unlisted_band`, 624 comparisons against bbf2daa3's checker, exit 0 |
| 🟢 | a report row's problem saying it needs no `Budget raised:` line is true of `ratchet` | `.github/scripts/budget_check.py:1169` | confirmed | read: `ratchet` skips a base row that is not a gate; file rows inherit the family's kind (`:436`) and `effective` copies the family row (`:1146`); executed: the checker with PR #937's body exits 0 and with an empty body exits 1 on the 20 kind changes alone |
| 🟢 | round 5's finding 1 is closed — 1791876665's S7 says exit 0 and where the summary names the file | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:59` | confirmed | executed: the real-tree probe matches each clause; read: `spec.md:59` |
| 🟢 | round 5's finding 2 is closed in what it named — the fragment no longer holds each slow file to a ceiling and calls it a report | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/changelog.md:17` | confirmed | read: `:17-22`, `:27`; the count in item 5 is ⬜ 1 |
| 🟢 | 1791876667's changelog fragment states the report row and its grounds once, and its sentence about the list matches `render` | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/changelog.md:44` | confirmed | read: `:36-55` against `render` `:1284-1294` |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_a_budget_ratchets.py tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q` | exit 0, 191 passed, 2 skipped |
| `bin/test` over `tests/test_docs_line_wrap.py`, `tests/test_no_real_identifiers.py`, `tests/test_one_word_one_meaning.py`, `tests/test_the_changelog_is_gathered_at_release.py` | exit 0, 116 passed |
| `bin/test tests/test_every_reader_ends_a_line_where_gfm_does.py -q` | exit 0, 149 passed |
| a probe comparing `band` and `unlisted_band` at bbf2daa3 and 701bc6c1 over every row of `seal/budgets.md`, each as a gate and as a report | exit 0, 624 comparisons over 103 rows; gate text equal; report text differs only in its last clause; deleted |
| the new case against `.github/scripts/budget_check.py` at bbf2daa3, at 21ffe7fb and at af18ab2e | exit 1 (no list in the summary); exit 1 at `tests/test_a_budget_ratchets.py:714`; exit 0; file restored |
| `python3 .github/scripts/budget_check.py --baseline origin/release/v0.22.0 --pr-body-env PRBODY` with PR #937's body (`gh pr view 937 --json body -q .body`, head 701bc6c1) | exit 0; the list holds `rounds-bytes` alone, 151,863 over 142,823; 20 `slow-file` removals read as declared |
| the same with an empty body | exit 1, 20 `Budget removed:` problems, one per `slow-file` row that is no longer a gate |
| 300 s added to one case of `tests/test_docs_line_wrap.py` in `.test_durations`, the checker with no baseline | exit 0; `slow-file` `266 seconds (largest unlisted)`, `report`, `over`; the list names the file with the listing clause; reverted |
| `uvx ruff check` and `uvx ruff format --check` over the two changed Python files | exit 0, exit 0 |
| the full suite, lint and typecheck at 701bc6c1 | not yet — not this round's to run; the sealer runs it once, and this round leaves nothing needing a fix, so the sealer's spawn comes due |

## Paste-ready fixes

### ⬜ 1

```markdown
  5. Two reports fail nothing: each slow test file, and the largest round
     records in the tree. A release pull request prints every budget
     against the last release tag.
```

In `spec.md` of the same work item, delete the `ledger-rereads` row of the
budgets table at line 39. In its `questions.md:8`, drop "and
`ledger-rereads`" from the report clause.

### ⬜ 2

```markdown
| T10 `test_an_unlisted_file_over_the_threshold_fails_and_a_listed_one_may_not_grow`, `test_an_unlisted_slow_file_under_a_report_row_is_named` | S7 (the first under a `gate` family, the second under the `report` kind this repository gives it) | the threshold check removed; the per-file compare removed; `render`'s list of report rows' problems removed, or a report row's problem asking for a `Budget raised:` line |
```

### ⬜ 3

```python
    """T10, S7 under a `gate` family: a test file over the threshold that
    the table does not list fails, naming it; a listed one is held to its
    own ceiling. This repository's family is a `report` row, which
    `test_an_unlisted_slow_file_under_a_report_row_is_named` holds."""
```

### ⬜ 4

```python
ceiling of their own. So where the family is a `gate`, an unlisted file
over the threshold fails, and listing it is a raise from the threshold
that needs its line, as is a row the table drops whose ceiling was under
it. Where the family is a `report`, that file fails nothing and the
summary names it in the list of report rows past their band. Every test
file whose reading times 1.3 reaches the threshold is listed, so an
unlisted one has the same room to move before it reads over. A docs
```

```python
    """The summary as markdown: one line per budget, each report row's
    problems, the raises read, the price level the seconds rows were read
    at, and where the docs were classified, each document's history and
    rule lines.
```

## Regression tests to plant

None. The new case covers the list and both new clauses, and it was shown
red against both earlier versions. ⬜ 2 needs a plan row and no new case.

## Facts for the record

- `ledger-rereads` is absent from `seal/budgets.md` and
  `.github/scripts/budget_check.py` at 5b1f6fae and at 701bc6c1. The report
  kinds the tree carries are `slow-file` and `rounds-bytes`.
- This work item's round records measure 151,863 bytes, over the
  `rounds-bytes` ceiling of 142,823. That is a report and fails nothing.

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

Needs a fix: no
Loses a record or crashes: no

## Proof block

Opened in this round, in the clone at 701bc6c1 unless noted:

- `.github/scripts/budget_check.py` — `:100-130`, `:191-193`, `:273-275`,
  `:436`, `:1040-1147`, `:1150-1226`, `:1228-1320`, `:1395-1470`; the
  same file at bbf2daa3, 21ffe7fb and af18ab2e
- `tests/test_a_budget_ratchets.py` — `:471-490`, `:600-722`
- `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/` —
  `spec.md:30-70`, `plan.md:55-95`, `changelog.md` (whole), `questions.md:8`
- `seal/specs/1791876667-the-durations-refresh-has-a-schedule/` —
  `rounds/round-5.md` (whole), `rounds/round-5-report.md:1-30`,
  `changelog.md:36-55`, the range's diff of `overview.md`
- `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/` —
  `spec.md:1-30`, `changelog.md:50-64`, grep for `ledger-rereads`
- `seal/specs/1791852617-a-docstring-left-short-is-reflowed/overview.md`
- `skills/settle/SKILL.md` — `:105-125`, `:280-300`, `:395-403`
- `pyproject.toml` — the ruff selection
- `bin/test`
- PR #937's body, read through `gh`
- `git diff bbf2daa3..701bc6c1` over every file it touches

# Round 1 — review of #930 at 65e973fd

Target: `chore/930-nothing-holds-the-repositorys-size-and-speed` at 65e973fd,
against `origin/release/v0.22.0` (a8d83663). A first round: no earlier
`round-N.md` exists, so nothing is carried. Work was done in a
`git clone --no-local` of the target at the round's own scratch directory;
nothing was written in the implementer's worktree.

## How the findings relate

```
the seconds rows are two-sided and start at zero headroom
  -> at #931's real refresh they fail 14 ways after the level is restated   (1)
the ratchet reads the ceiling and the kind, never the slack
  -> the lowering half can be widened away with no line                    (2)
the extension points are claimed open
  -> a new per-file family is measured as docs history                      (3)
  -> a new reader that can be unread crashes the summary; the refusal
     already lists the families wrongly                                     (4)
the step count moved
  -> one shipped sentence about it did not                                  (5)
```

Notes (⬜, paperwork or wording, no fix pass): 6, 7, 8.

## Findings from execution

### 1. At #931's own refresh, the seconds rows fail fourteen ways after the level is restated

`.github/scripts/budget_check.py:321` (the one-sided rule in
`parse_budgets`), `seal/budgets.md:28-30` and the `## Slow test files` rows.

The work item lists this as not verified, for the orchestrator "when #931 and
this branch meet". I ran it. I took #931's refreshed `.test_durations`
(9ffc5f66, the union of run 38475370013) onto 65e973fd in my clone and ran
the checker with `--baseline 65e973fd`, the way the hygiene step runs it.

- With the level left at 1000, it exits 1 and names 1071, as designed.
- With the level restated to 1071, it still exits 1, with 14 problems.
  `suite-seconds` is over by 65. One unlisted file is at 127 s. Ten listed
  files are over their ceilings by 6 to 112 s. Two are under their band.

The cause is the shape of the rows, not the arithmetic. Per file, the refresh
moved prices between 0.76 and 1.14 times the suite's seconds-weighted ratio,
over the 19 files above 100 s. A two-sided band 10 % wide cannot hold that
spread wherever the ceiling sits. Every ceiling also starts at its reading,
with zero headroom (the checker's own summary at 65e973fd shows `0 (0.0%)`
on every gate row except the two family rows).

The same mechanism fails a cleanup. In a fixture, three files of 1000, 500
and 200 s; the first one's cases are made twice as fast under the same ids.
The ratio over shared ids becomes 0.706. Once the level is restated to 706,
the two untouched files read 708 and 283 s against ceilings of 500 and 200,
and `suite-seconds` reads 1700 again. The speedup is invisible, and the
untouched files need `Budget raised:` lines. That is the kind of pull request
#929 is framed to be.

What the account said. `phases/phase-2.md` says "one slow file moving shifts
the level a little … which reads every other file 1.6 % lower, inside the
10 % slack". That holds for a file that grows. A file that shrinks pushes
every other file up, and at zero headroom there is no slack on that side.

The code's own rule answers the design question. Its docstring says "A row
read off one run is one-sided", and the commit that produced 9ffc5f66 says
`.test_durations` is one run's union. The seconds rows meet that description.

### 2. A gate row's slack can be widened with no line, which turns off the lower band

`.github/scripts/budget_check.py:863-865` (`ratchet`).

`ratchet` compares the ceiling and the kind and nothing else. In a fixture
with `suite-seconds` at 5 %, five cases were removed (1700 to 1200 s). At
5 %, the run asks for the ceiling to be lowered. With the slack changed to
50 % in the same pull request, `suite-seconds` holds. The body carries no
line and the summary's "Ceilings moved since the base" is empty.

This matters because the lower band is the half of the ratchet that records
a cleanup (docstring, *The band*). Widening the slack keeps the old headroom
for the next pull request to grow into, and nothing reads that this
happened.

### 3. A third per-file family would be measured by the docs classifier

`.github/scripts/budget_check.py:632-644` (`file_values`) and `:328-345`
(`parse_budgets`'s per-file loop).

The account says, in `overview.md` §*Not done*: "each is one `MEASURERS`
entry, and one `FILE_TABLES` entry where it is read per file". The code does
not do this, in two places.

- `file_values` handles `slow-file` and sends every other family to
  `docs_lines`. With `test-lines` added to `FILE_TABLES` under its own
  header, its family row reported `docs/a.md is not listed and measures 1
  lines`. Its row for a file under `tests/` was refused as "not in docs/".
- `parse_budgets` finds each family's table by its header alone, through
  `gfm_table`, and uses the `## title` only in messages. A `test-lines`
  family with the header `| File | Lines ceiling |` read the docs-history
  table. The run then stopped at exit 2, saying there was no `docs-history`
  row.

#929 frames `test-lines`, and `| File | Lines ceiling |` is the header a
lines-per-file family would naturally take.

### 4. A new reader that can be unread crashes the summary, and the refusal already lists the families wrongly

`.github/scripts/budget_check.py:934` (`render`) and `:730-734` (`measure`).

- `render` looks a missing reading up in `UNREAD` by family, with no
  default. A family added to `MEASURERS` whose measurer returns None, as
  `measure_rereads` does, raises `KeyError` with a traceback. That exits 1,
  not 2. Nothing in this tree triggers it; the first extension that copies
  `measure_rereads` will.
- `measure`'s refusal for an unknown name lists `preload`, `suite-seconds`,
  `slow-file`, `docs-history` and `ci-minutes` as the families. It leaves out
  `rounds-bytes` and `ledger-rereads`, which are in `MEASURERS` at this tree.
  A misspelt `rounds-byte` row is told the family it meant does not exist.
  Each new family is a third place to edit this string.

## Findings from reading

### 5. The shipped verify skill still counts four unmirrored steps with a local answer

`skills/verify/SKILL.md:484-487`.

"Four steps of SpecSeal's own `release` job have a local answer and no arm:
three run a script under `.github/scripts/`, …". The budget step is a fifth:
it runs `.github/scripts/budget_check.py`, and `PARTITION` excludes it. The
diff corrected the same count in `broad_gate.py`'s comment ("four run a
script … The last five") but not in this skill, which ships to every
installation. No case pins the sentence, so nothing went red (§12: the class
is every sentence stating this count; I found these two).

### 6. ⬜ The ledger fragment re-reads a released row as holding when its count no longer does

`seal/ledger/1791876665-each-budget-ratchets-and-every-pull-request-measures-it.md:6`.

The `Re-read · N3` row says the claim of `seal/releases/0.15.1.md` N3 holds.
That claim says the release job "has four unmirrored steps", and on a feature
base it now has five. This is a paperwork correction: the row becomes a
`Corrected ·` row like N10 and P2 above it.

### 7. ⬜ `spec.md` still lists a `--json` flag that was not built

`seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:69`.

`overview.md` §*Not done* says so openly. Nothing reads the flag. The spec
line and the build should agree before `settle` folds the spec.

### 8. ⬜ The billable line points CI readers at a record that `settle` will remove

`.github/scripts/budget_check.py:1227`.

Every `budgets` summary ends "its date unverified (`questions.md` Q1)". The
file is this work item's own. `settle --retire-process` removes it after the
release, and the line will name nothing. The figure and "unverified" stay
true.

## The divergences, judged

- 1 (`PARTITION` and the counts 10/5 and 12/9). I counted fourteen named
  steps in the `release` job. Four are only-at-main, so ten run for a
  feature base. Five are mirrored there, so five are unanswered. On `main`,
  two are skipped, which leaves twelve; three are mirrored, so nine. The
  `Corrected ·` rows N10 and P2 state these numbers. Sound, apart from 5 and
  6 above.
- 2 (`edited`). A re-run replays the payload the run began with, so without
  `edited` the step reads the old body. Sound. It also re-runs the whole
  `release` job on a title edit. I judged that cost acceptable.
- 3 (`## Price level`). The row is right against the literal decision, which
  fails every pull request after a refresh. Finding 1 is about the rows the
  level divides, not about the level.
- 4 (one-sided `ci-minutes`). Sound, and the owner approved it. Finding 1
  asks for the same reasoning on the seconds rows.
- 5 (`--ci-jobs FILE`). Sound. The script reads no network, and only the
  `gh` step holds the token. The unused `fetch-depth: 0` is acknowledged,
  and `tests/test_ci_gives_the_checks_what_they_need.py` selects that job
  wrongly; #931 owns that.
- 6 (CRLF counted as LF, test names). Sound. `lf_bytes` is the one counter
  every byte reader uses.
- 7 (a rule block ends at its paragraph). Sound. Its error counts more
  history lines, not fewer, which is the safe side for a gate.

## Census modules no slice ran

I ran thirteen modules: interpreter floor, workflow reader, one format one
reader, no real identifiers, one table walker, one word one meaning, no
passage pasted twice, slow case, settle's process record, range ownership,
every agent reads the contract, the signer's CI and the gate's range. 1428
passed, exit 0. Together with the orchestrator's run of the reader registry,
encoding and GFM line census, I found no census broken by this diff.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the seconds rows are two-sided at zero headroom, and fail 14 ways at #931's real refresh after the level is restated; a cleanup of one heavy file fails the untouched ones | `.github/scripts/budget_check.py:321` | open | executed: #931's 9ffc5f66 file on 65e973fd, exit 1 at the named level 1071; fixture speedup, exit 1 on untouched files |
| 🟡 2 | a gate row's slack can be widened with no line, which turns off the lower band unseen | `.github/scripts/budget_check.py:863` | open | executed: 5 % to 50 % with cases removed holds, no move in the summary |
| 🟡 3 | a third `FILE_TABLES` family is measured by the docs classifier, and per-file tables are found by header alone | `.github/scripts/budget_check.py:632` | open | executed: a `test-lines` family read docs history; a shared header read the docs table |
| 🟡 4 | `render` raises KeyError for a new unreadable family; the unknown-family refusal omits two families that exist | `.github/scripts/budget_check.py:934` | open | executed: KeyError on a None-returning measurer; `rounds-byte` refused with a list lacking `rounds-bytes` |
| 🟡 5 | the shipped verify skill counts four unmirrored steps with a local answer, three of them scripts; there are five and four | `skills/verify/SKILL.md:484` | open | read: `PARTITION` excludes the budget step as a repository script |
| ⬜ 6 | the `Re-read · N3` row says a claim holds whose count of four unmirrored steps is now five | `seal/ledger/1791876665-each-budget-ratchets-and-every-pull-request-measures-it.md:6` | open | read: paperwork, a correction like N10 and P2 |
| ⬜ 7 | `spec.md` lists `--json`, which was not built | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:69` | open | read: paperwork; `overview.md` discloses it |
| ⬜ 8 | the billable line cites the work item's `questions.md` Q1, which settle removes | `.github/scripts/budget_check.py:1227` | open | read: the sentence will dangle after the release; the fact stays true |
| 🟢 | the step counts 10/5 and 12/9, the `PARTITION` row and the N10 and P2 corrections | `skills/verify/scripts/broad_gate.py:2416` | confirmed | read: fourteen steps counted in `hygiene.yml`'s `release` job |
| 🟢 | `edited` in the hygiene types, `--ci-jobs` in place of `--ci-run`, CRLF counted as LF, the paragraph-bounded rule block | `.github/workflows/hygiene.yml:17` | confirmed | read against the code |
| 🟢 | no census module is broken by this diff | `tests/` | confirmed | executed: 13 modules, 1428 passed, exit 0 |
| ❓ | the case bodies of the new test module, and the claim that each was seen red | `tests/test_a_budget_ratchets.py` | ❓ out of verified scope | read only its case names; the seen-red claims rest on the phase records. A later round or the orchestrator answers it |
| ❓ | that a body edit re-runs the hygiene job and the step reads the new body | `.github/workflows/hygiene.yml:17` | ❓ out of verified scope | needs a body edit on PR #938; the orchestrator answers it, as `overview.md` names |

## Executed probes

| What was run | Result |
|---|---|
| 13 census modules through `bin/test` in the clone at 65e973fd | 1428 passed, exit 0 |
| `budget_check.py` with `--baseline origin/release/v0.22.0 --base-ref release/v0.22.0 --pr-body-env PR_BODY --trend v0.21.1`, empty body | exit 0; every gate row reads headroom 0 (0.0%) except the `slow-file` family row |
| #931's `.test_durations` (9ffc5f66) committed on 65e973fd in the clone, `--baseline 65e973fd`, level 1000 | exit 1; names level 1071 |
| the same with the level restated to 1071 | exit 1; 14 problems: `suite-seconds` over by 65, one unlisted file at 127 s, ten listed files over, two under their band |
| the ratio across that refresh, read off both files | 13,454 shared ids; seconds-weighted 1.071; median per case 0.892; per-file ratio over the weighted one 0.76 to 1.14 over 19 files above 100 s |
| fixture: one heavy file's shared ids halved, level 1000 then 706 | at 1000 the level problem; at 706, both untouched files over and `suite-seconds` back at 1700 |
| fixture: `suite-seconds` slack 5 % then 50 %, cases removed | at 5 %, lower it; at 50 %, holds, with no move listed |
| a `test-lines` entry added to `FILE_TABLES`, own header, then the docs header | own header: docs history measured for it, its file row refused; shared header: exit 2 for a missing `docs-history` row |
| a `MEASURERS` entry whose measurer returns None | `KeyError` from `render` |
| a `rounds-byte` row | refused with a family list lacking `rounds-bytes` and `ledger-rereads` |
| the broad gate (full suite, lint, typecheck) at this branch's tip | not yet: the sealer's, after the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

## Paste-ready fixes

### 🟡 1

The code half: seconds rows may be one-sided, for the reason `ci-minutes`
rows must be. In `parse_budgets`:

```python
        family = name.partition(":")[0]
        per_run = family in PER_RUN
        # `.test_durations` is one run's union (#931), so a seconds row may be
        # one-sided for the reason a `ci-minutes` row must be: one run's
        # prices move a file 0.76 to 1.14 times the suite's ratio.
        one_run = per_run or family in PRICED
        one_sided = parsed.amount is None
        if per_run and not one_sided:
            raise Unreadable(
                f"{at}: {name}'s slack is `{slack}`, and a row read off one CI "
                f"run is `{ONE_SIDED}`: a run's minutes swing too far for a "
                "lower band"
            )
        if one_sided and not one_run and kind != REPORT:
            raise Unreadable(
                f"{at}: {name}'s slack is `{slack}`, and only a row read off "
                f"one CI run, a seconds row or a `{REPORT}` row is `{ONE_SIDED}`"
            )
```

The rows half: the starting values are a decision (see *Decisions left*).
In the shape the `ci-minutes` rows already have, they would read:

```
| suite-seconds | seconds | <ceiling with headroom> | one-sided | gate |
| slow-file | seconds | 120 | one-sided | gate |
```

Each `## Slow test files` ceiling would carry the headroom the decision
names. The docstring's "Only such a row may say `one-sided`" moves with the
code.

### 🟡 2

In `ratchet`, a widened slack is a raise:

```python
def widened(old, new, at):
    """Whether slack NEW lets a ceiling sit further above a reading of AT than
    slack OLD does: one-sided is the widest.

    Reads: nothing — compares the two slacks handed to it"""
    before, after = top_of_band(at, old), top_of_band(at, new)
    return before is not None and (after is None or after > before)
```

```python
        if new is not None and new.kind == GATE:
            wider = widened(old.slack, new.slack, old.ceiling)
            if new.ceiling <= old.ceiling and not wider:
                continue
            what = f"raised {old.ceiling} -> {new.ceiling}"
            if wider:
                what += f", slack {old.slack.text} -> {new.slack.text}"
```

The existing line `Budget raised: <name> <old> -> <new>: <reason>` covers
it, with the two ceilings equal where only the slack moved. The docstring's
*The ratchet* paragraph says so.

### 🟡 3

Fail closed for a family that has no reader, and refuse two families that
share a header:

```python
        elif family == "docs-history":
            cache["docs"] = docs_lines(root)
            cache[family] = {path: len(h) for path, (h, _) in cache["docs"].items()}
        else:
            raise Unreadable(
                f"{family}: `FILE_TABLES` names it and `file_values` has no "
                "reader for it"
            )
```

```python
    headers = [header for _title, header, _unit in FILE_TABLES.values()]
    if len(set(headers)) != len(headers):
        raise Unreadable(
            "two families in `FILE_TABLES` share a table header, and a table "
            "is found by its header"
        )
```

The second block goes just before `parse_budgets`'s per-file loop. The
`overview.md` sentence "each is one `MEASURERS` entry, and one `FILE_TABLES`
entry" then reads: one `FILE_TABLES` entry, a header of its own and a branch
in `file_values`.

### 🟡 4

```python
            why = UNREAD.get(row.name.partition(":")[0], "not read on this run")
```

```python
    if family not in MEASURERS or bool(subject) != MEASURERS[family][2]:
        known = sorted(
            [f"{f}:<subject>" if MEASURERS[f][2] else f for f in MEASURERS]
            + list(FILE_TABLES)
            + [f"{f}:<leg>" for f in PER_RUN]
        )
        raise Unreadable(
            f"{row.name}: no measurer here reads a budget of that name — the "
            f"families are {', '.join(f'`{f}`' for f in known)}"
        )
```

### 🟡 5

```
**The arms the plugin ships are the arms the gate can run.** Five steps of
SpecSeal's own `release` job have a local answer and no arm: four run a
script under `.github/scripts/`, which no plugin ships, and one is shell
written inline in the workflow with no script either side can share. A
```

## Regression tests to plant

All in `tests/test_a_budget_ratchets.py` unless named. Each fails on 65e973fd
by the probe that found it.

```
test_a_cleanup_of_one_file_under_shared_ids_holds_the_untouched_rows
    fixture of three files, the heaviest one's cases halved under the same ids,
    the level restated as the checker names it, slow-file rows one-sided:
    exit 0 for the untouched files (red now: two over)
test_a_widened_slack_on_a_gate_row_needs_its_line
    5 % -> 50 % with nothing else moved and no body line: exit 1 naming
    `Budget raised:`; with the line: exit 0 and the move in the summary
test_a_per_file_family_with_no_reader_is_exit_2
    a FILE_TABLES entry file_values does not branch on: exit 2, never docs counts
test_two_per_file_families_may_not_share_a_header
test_the_unknown_family_refusal_names_every_family
    the sentence names every MEASURERS, FILE_TABLES and PER_RUN key
test_an_unread_row_of_a_family_without_an_unread_reason_renders
tests/test_the_gate_names_every_step_ci_runs.py:
test_the_skill_counts_the_steps_with_a_local_answer_and_no_arm
    the verify skill's count equals PARTITION's script-and-inline exclusions
```

## Facts for the evidence ledger

- #931's refresh (9ffc5f66) against 65e973fd: 13,454 shared case ids,
  seconds-weighted ratio 1.071, median per case 0.892, per-file ratio over
  the weighted one 0.76 to 1.14 over the 19 files above 100 s. With the
  level restated to 1071, the checker reports 14 problems. Executed in this
  round. It belongs beside phase 2's claim of "inside the 10 % slack", which
  it contradicts on the shrinking side.
- `seal/releases/0.15.1.md` N3's "four unmirrored steps" is now five: a
  `Corrected ·` row in this work item's fragment (finding 6).

## Decisions left

- **The seconds rows' shape (finding 1).** These are the options.
  - One-sided, as `ci-minutes` is, with ceilings set by a rule like 1.3
    times. The release lowers them from the trend line. This is the fix
    above.
  - Two-sided with ceilings at the middle of the band. The measured spread
    (0.76 to 1.14) is wider than ±5 %, so this would still fail at every
    refresh.
  - Keep them as built. Then every refresh, starting with #931's, writes
    about a dozen `Budget raised:` lines. That is the "boilerplate" failure
    `plan.md` names for six months on.
  - The criterion: which rows #931 can pass without a line it cannot argue
    for. The orchestrator answers it, with the owner where the ceilings move.

Needs a fix: yes — 🟡 1 (seconds rows fail at the first real refresh), 🟡 2 (slack widening unratcheted), 🟡 3 and 🟡 4 (the extension points), 🟡 5 (the shipped skill's count)
Loses a record or crashes: no

The broad gate has not come due: this report leaves findings open, so the
sealer is not spawned yet.

## Proof block

Files opened this round, all at 65e973fd in the clone unless named:
`.github/scripts/budget_check.py` (whole), `seal/budgets.md`,
`.github/workflows/hygiene.yml` (diff, step list, lines 40-64),
`.github/workflows/test.yml` (lines 1-120 and the diff), `CONTRIBUTING.md`
(lines 36-100 and the diff), `docs/release-checklist.md` (diff),
`docs/the-record-layout.md` (diff), `skills/verify/SKILL.md` (lines 440-500
and the diff), `skills/verify/scripts/broad_gate.py` (lines 2355-2480 and the
diff), `skills/verify/scripts/seal_stamp.py` (lines 870-900),
`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` (lines
505-525), `.github/scripts/issue_claims_check.py` (lines 20-45, 288-330),
`seal/config.md` (the `Broad gate` row), the diffs of
`tests/test_the_gate_names_every_step_ci_runs.py`,
`tests/test_the_seal_is_taken_once_by_the_sealer.py`,
`tests/test_every_reader_ends_a_line_where_gfm_does.py` and
`tests/undeclared_readers.txt`, the `def test_` lines of
`tests/test_a_budget_ratchets.py` (not the module's bodies),
`seal/ledger/1791876665-each-budget-ratchets-and-every-pull-request-measures-it.md`,
`seal/releases/0.15.1.md:102`, the work item's `spec.md`, `plan.md`,
`questions.md`, `overview.md`, `handoff.md` and `phases/phase-2.md` (lines
18-65, 136-149), `bin/test` (head), and `.test_durations` at 9ffc5f66 in the
main checkout.

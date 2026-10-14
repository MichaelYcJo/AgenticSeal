# 1791876665-each-budget-ratchets-and-every-pull-request-measures-it — review round 1

| Field | Value |
|---|---|
| Target SHA | 65e973fddba8610423de52be23eaa637a59b22db |
| Written late | no |
| Ran by | warden on Opus 5.5 |
| PR | 938 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are not yet written |
| Fix range | none — the fixes are not yet written |
| Contract changes | none — the fixes are not yet written |
| New units | none — the fixes are not yet written |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (seconds rows fail at the first real refresh), 🟡 2 (slack widening unratcheted), 🟡 3 and 🟡 4 (the extension points), 🟡 5 (the shipped skill's count) |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 1 of #930 against 65e973fd on base origin/release/v0.22.0: spec compliance first, then quality, over the whole diff. Judge the seven recorded divergences from the frame, check the class of a new script breaking a census no slice ran, and judge whether the checker's extension points are as open as claimed for #923, #929 and #931.

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

## Paste-ready fixes

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
```
| suite-seconds | seconds | <ceiling with headroom> | one-sided | gate |
| slow-file | seconds | 120 | one-sided | gate |
```
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
```
**The arms the plugin ships are the arms the gate can run.** Five steps of
SpecSeal's own `release` job have a local answer and no arm: four run a
script under `.github/scripts/`, which no plugin ships, and one is shell
written inline in the workflow with no script either side can share. A
```

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

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

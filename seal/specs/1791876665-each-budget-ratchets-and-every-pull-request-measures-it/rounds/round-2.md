# 1791876665-each-budget-ratchets-and-every-pull-request-measures-it — review round 2

| Field | Value |
|---|---|
| Target SHA | 6a6d4fbe11823be430f80553ff6d0e0079650b5f |
| Written late | no |
| Ran by | warden on Opus 5.5 |
| PR | 938 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are not yet written |
| Fix range | none — the fixes are not yet written |
| Contract changes | none — the fixes are not yet written |
| New units | none — the fixes are not yet written |
| Fix of a fix | first — 🟡 1 at .github/scripts/budget_check.py#section, a unit round-1's fixes added |
| Needs a fix | yes — 🟡 1 (`section` reads headings off fenced and commented lines and takes a repeated heading as its first) |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 2 of #930 against 6a6d4fbe: the verifying round over round 1's fix pass (8e30ac1a..37d95bd9). Open each fix against its finding, judge the implementer's median price-level decision and whether a non-refresh change can move it, and check that the fix pass introduced nothing new.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | `section` reads headings off fenced and commented lines, so a fenced `##` line inside a per-file section cuts its table off and the checker refuses a file GitHub renders; a repeated heading is read as its first | `.github/scripts/budget_check.py:383` | open | executed: a fenced heading inside `## Docs history lines` gave exit 2, "no table" |
| ⬜ 2 | the per-file spread the ×1.3 rule cites, 0.76 to 1.16, does not reproduce | `.github/scripts/budget_check.py:76` | open | executed: 0.76 to 1.14 over files of 100 s or more, 0.46 to 1.54 over all 72; the rule still holds |
| 🟢 | round 1's finding 1 is closed — the seconds rows are one-sided at 1.3 times, the level is a median over files, and #931's refresh holds at the level the checker names | `.github/scripts/budget_check.py:324` | confirmed | executed: exit 1 naming 1073, then exit 0 at 1073, tightest row 0.892; the 20 listed files and every ceiling match their readings |
| 🟢 | round 1's finding 2 is closed — a widened slack is a raise and needs its line | `.github/scripts/budget_check.py:934` | confirmed | read: `widened` and the four cases |
| 🟢 | round 1's finding 3 is closed — each per-file family carries its reader and its table is read under its heading | `.github/scripts/budget_check.py:682` | confirmed | read and the case: a shared header reads both families |
| 🟢 | round 1's finding 4 is closed — an unread row has a default reason and the family list is derived | `.github/scripts/budget_check.py:805` | confirmed | read and the cases |
| 🟢 | round 1's finding 5 is closed — the skill says five and four, held to `PARTITION` | `skills/verify/SKILL.md:484` | confirmed | read: the case's sentence would not match the old text |
| 🟢 | the median moves only with the seconds of existing ids, and only when most priced files move | `.github/scripts/budget_check.py:568` | confirmed | executed: 72 files; five more would have to move to shift it 2 %; a rewrite of more than half asks for the level first |
| 🟢 | no census module is broken by the fix pass | `tests/` | confirmed | executed: 9 modules, 1170 passed, exit 0 |

## Paste-ready fixes

```python
def section(text, title):
    """`(text, lines before it)` of the part of `text` under its `## title`
    heading, to the next heading of level one or two, or None where no such
    heading stands. A per-file table is the one under its family's heading,
    so two families may share a header. A heading is one a renderer shows:
    a line in a fence or a comment is none, and a title written twice is
    refused, since then the table is not one.

    Reads: guess — a person's markdown, through `unverified_check.py#gfm_lines`, `#readable` and `#heading_level`; unknown refused"""
    reader = sibling("unverified_check")
    lines = reader.gfm_lines(text, keepends=True)
    shown = reader.readable(text)
    levels = [reader.heading_level(line) for line in shown]
    starts = [
        at
        for at, line in enumerate(shown)
        if levels[at] == 2 and line.strip().lstrip("#").strip() == title
    ]
    if not starts:
        return None
    if len(starts) > 1:
        raise Unreadable(
            f"`## {title}` stands {len(starts)} times, so its table is not one"
        )
    end = next(
        (at for at in range(starts[0] + 1, len(lines)) if levels[at] in (1, 2)),
        len(lines),
    )
    return "".join(lines[starts[0] + 1 : end]), starts[0] + 1
```

## Executed probes

| What was run | Result |
|---|---|
| the committed rows against `.test_durations` at 6a6d4fbe | `suite-seconds` 10,221 = ceil(1.3 × 7,862); the 20 listed files are exactly those whose reading × 1.3 reaches 120, every ceiling ceil(1.3 × reading) |
| #931's `.test_durations` (9ffc5f66) committed on 6a6d4fbe, `--baseline 6a6d4fbe`, level 1000 | exit 1; names level 1073 |
| the same with the level restated to 1073 | exit 0; tightest rows 0.892, 0.864, 0.847 of their ceilings |
| the per-file ratios across that refresh | 72 files of 10 s or more; median 1.073; 32 above 1.02 times it; spread against it 0.76 to 1.14 over 19 files of 100 s or more, 0.46 to 1.54 over all 72 |
| more than half the priced files' entries ×1.3, no refresh, level 1000 | exit 1: the level is asked for as 1300 |
| a fenced `## an example heading` inside `## Docs history lines`, before its table | exit 2: "a `docs-history` row and no `## Docs history lines` table" |
| a malformed ceiling in the slow-file table at file line 52 | refused as "line 52" |
| 9 census modules through `bin/test` at 6a6d4fbe | 1170 passed, exit 0 |
| the broad gate (full suite, lint, typecheck) at this branch's tip | not yet: the sealer's, after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `.github/scripts/budget_check.py:321` | round 1's 🟡 1 — fixed |
| round-1 | `.github/scripts/budget_check.py:863` | round 1's 🟡 2 — fixed |
| round-1 | `.github/scripts/budget_check.py:632` | round 1's 🟡 3 — fixed |
| round-1 | `.github/scripts/budget_check.py:934` | round 1's 🟡 4 — fixed |
| round-1 | `skills/verify/SKILL.md:484` | round 1's 🟡 5 — fixed |
| round-1 | `seal/ledger/1791876665-each-budget-ratchets-and-every-pull-request-measures-it.md:6` | round 1's ⬜ 6 — open |
| round-1 | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:69` | round 1's ⬜ 7 — open |
| round-1 | `.github/scripts/budget_check.py:1227` | round 1's ⬜ 8 — open |
| round-1 | `skills/verify/scripts/broad_gate.py:2416` | round 1's 🟢 — confirmed |
| round-1 | `.github/workflows/hygiene.yml:17` | round 1's 🟢 — confirmed |
| round-1 | `tests/` | round 1's 🟢 — confirmed |
| round-1 | `tests/test_a_budget_ratchets.py` | round 1's ❓ — out of verified scope |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain

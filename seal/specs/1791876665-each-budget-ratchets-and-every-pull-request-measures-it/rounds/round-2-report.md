# Round 2 — the verifying round over round 1's fix pass

Target: HEAD 6a6d4fbe of `chore/930-nothing-holds-the-repositorys-size-and-speed`.
The fix range is `8e30ac1a..37d95bd9`, nine commits. The review used a
`git clone --no-local` at the round's scratch directory, and nothing was
written in the implementer's worktree except this file.

The scope is the fix diff. Inside it are the units round 1's fixes created:
`section`, `slow_file_values`, `docs_history_values`, `families`, `widened`
and `FileFamily`. I judged those as new code.

## In short

- All five of round 1's findings are closed. Each fix was opened against its
  finding and each was re-run.
- The new price level is the median over files. It holds #931's real
  refresh. It moves only when most of the 72 priced files move, so a change
  that is not a refresh cannot move it. I judged it sound.
- One new unit, `section`, ends a per-file table's section at a heading that
  stands inside a fenced block. GitHub renders the table, and the checker
  then refuses the file (finding 1).
- One measured figure in the docstring and spec could not be reproduced. It
  does not change the ×1.3 rule it supports (note 2).
- Round 1's notes 6 to 8 are carried and wait for the run's end, so they are
  not reported again here.

## Round 1's findings, each against its fix

**1 (the seconds rows fail #931's refresh).** Fixed by 93cbdf9d. The seconds
rows are now one-sided, with ceilings at 1.3 times the reading. The price
level is the median, over files the base prices at 10 s or more, of each
file's ratio on the shared ids. Executed: I committed #931's
`.test_durations` (9ffc5f66) on 6a6d4fbe and ran with `--baseline`.

- With the level at 1000, the run exits 1 and names 1073.
- Restated to 1073, it exits 0. The tightest row is
  `slow-file:tests/test_a_corrected_sentence_survives_elsewhere.py` at 0.892
  of its ceiling. That matches the implementer's claim.

I also checked the committed rows against `.test_durations` at HEAD.
`suite-seconds` is 10,221, which is 1.3 × 7,862 rounded up. The 20 listed
files are exactly the files whose reading times 1.3 reaches 120 s, and each
listed ceiling is 1.3 times its reading rounded up.

**2 (a widened slack passes unseen).** Fixed by 01ab0714. `widened`
compares the top of the band at the old ceiling and counts `one-sided` as
the widest. A file row is skipped, because its family row answers for its
slack. The four new cases cover a widening with no line, one with its line,
a narrowing, and a family's slack. I read each one against the code, and
they hold.

**3 (a third per-file family is read as docs).** Fixed by acaf6c30.
`FileFamily` carries its reader, and each table is read from under its own
heading. The new case adds `test-lines` with the docs table's own header,
and both families read correctly. See finding 1 below for one shape the new
heading reader gets wrong.

**4 (a None measurer crashes, and the family list is wrong).** Fixed by
fc5921ce. `UNREAD.get` now has a default, and `families()` builds the list
from `MEASURERS`, `FILE_TABLES` and `PER_RUN`. The case checks every key.

**5 (the skill counts four steps).** Fixed by 82b83432. The skill now says
"Five … four". The new case derives that count from `PARTITION`'s reasons.
Read against the old text "Four … three", the case's sentence would not
match, which is the red the ledger row claims.

## The median, judged

Executed over the two durations files, 6a6d4fbe against 9ffc5f66:

- 72 files are priced at 10 s or more on the shared ids. Their median is
  1.073, and the seconds-weighted ratio is 1.071, so the two agree on a real
  refresh.
- On a refresh, the median moves only when most of those files move: at
  #931's distribution, five more files would have to rise past it to lift
  it by 2 %.

**Only a change to the seconds of existing case ids can move it.** A ratio
is taken over the ids both files hold, so these leave the level at 1:

- adding or removing a case;
- renaming a case;
- deleting a test file;
- a partial refresh of fewer than half the files.

That last case is #929's. Its files then read their own new seconds
directly, which is the point of the change.

**It can be gamed, in the same way and to the same degree as the weighted
ratio was.** Executed: rewriting more than half the files' entries ×1.3 made
the checker ask for level 1300 (exit 1). Once the level is restated, every
reading is divided by 1.3 and no `Budget raised:` line is asked for. The
diff that does this is large and visible, since it moves 37 or more files of
`.test_durations` and the level row together. I report it as a property, not
a finding. Holding a level change to a CI artifact would close it. That
belongs with #931's durations upload, not with this branch.

## Findings from execution

### 1. A fenced line that reads like a heading ends a per-file table's section, and the checker refuses a file GitHub renders

`.github/scripts/budget_check.py:383-404` (`section`, a unit round 1's fix
3 created).

`section` asks `heading_level` of every raw line, fenced and commented lines
included. The docstring of `heading_level` says every reader asks it of
lines with fences blanked, which is what `readable` returns.

Executed: I put a fenced example holding `## an example heading` between
`## Docs history lines` and its table. GitHub renders the table under its
heading. The checker exits 2, saying there is "a `docs-history` row and no
`## Docs history lines` table".

The same happens in reverse. A fenced or commented `## Slow test files`
would be taken as the section's start. The failure is closed: every shape I
tried refuses the file and none misreads it. But that refusal is wrong about
a valid file, in the unit the fix added for exactly this kind of table.

A second heading with the same title is also read silently as the first
one only. `round_record.py#section_body` refuses that shape instead.

## Findings from reading

### 2. ⬜ The per-file spread the ×1.3 rule cites does not reproduce

`.github/scripts/budget_check.py:76` and `spec.md`'s `suite-seconds` row.

Both say one refresh priced test files "0.76 to 1.16" times the level.
Against the median 1.073, I measured 0.76 to 1.14 over the 19 files of
100 s or more. Over all 72 priced files the spread is 0.46 to 1.54. Neither
set gives 1.16. The ×1.3 still holds the heavy files' spread, and the
refresh probe shows no unlisted file crossing 120 s, so the rule stands.
Only the figure needs to be rewritten.

## Checked for anything the fix pass introduced

- I ran nine census modules at 6a6d4fbe that the orchestrator's set did not
  include: format reader, interpreter floor, encoding, no real identifiers,
  one word one meaning, no passage pasted twice, slow case, table walker
  and fold room. 1170 passed, exit 0.
- File-table rows still report absolute line numbers after the section
  offset. A malformed ceiling on file line 52 is refused as "line 52".
- `slow_file_values`, `docs_history_values`, `families` and `widened` are
  correct as read.
- `survivors.md` and the ledger fragment's corrected rows (N3, B9 and the
  band rows) say what the code now does. I judged them on correctness only.

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

## Paste-ready fixes

### 🟡 1

Read the headings off `readable`, the lines a renderer shows, and refuse a
repeated heading, as `round_record.py#section_body` does:

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

## Regression tests to plant

In `tests/test_a_budget_ratchets.py`. Each fails at 6a6d4fbe by the probe
above.

```
test_a_fenced_heading_inside_a_file_section_does_not_end_it
    a fenced `## …` line between `## Docs history lines` and its table:
    exit 0 and the table's rows read (red now: exit 2, "no table")
test_a_file_section_written_twice_is_refused
    two `## Slow test files` headings: exit 2 naming the title
```

## Facts for the evidence ledger

- Across #931's refresh, against 6a6d4fbe, there are 72 files of 10 s or
  more. Their median is 1.073 and the weighted ratio is 1.071. With the
  level restated to 1073 the checker exits 0, and its tightest row is 0.892
  of its ceiling. The per-file spread against the median is 0.76 to 1.14
  over the files of 100 s or more. Executed in this round.

Needs a fix: yes — 🟡 1 (`section` reads headings off fenced and commented lines and takes a repeated heading as its first)
Loses a record or crashes: no

The broad gate has not come due. This round opened 🟡 1 in a unit round 1's
fixes created, so a fix and a further round come before the sealer is
spawned.

## Proof block

All files were opened at 6a6d4fbe in the clone, unless named otherwise:

- the fix diff `8e30ac1a..37d95bd9` of `.github/scripts/budget_check.py`,
  `seal/budgets.md`, `docs/release-checklist.md`, `skills/verify/SKILL.md`,
  `tests/test_a_budget_ratchets.py` and
  `tests/test_the_gate_names_every_step_ci_runs.py`;
- the diffs of the work item's `spec.md`, `overview.md` and `changelog.md`,
  and the word diff of
  `seal/ledger/1791876665-each-budget-ratchets-and-every-pull-request-measures-it.md`;
- `survivors.md`;
- `hooks/config.py#gfm_table`'s docstring;
- `skills/verify/scripts/unverified_check.py` (`gfm_lines`, `heading_level`,
  `readable`, `headings`, `sections`);
- `skills/code-review/scripts/round_record.py` (`section_end`,
  `section_body`) and `skills/code-review/scripts/chain_check.py#section_end`;
- `.test_durations` at 6a6d4fbe and at 9ffc5f66, the latter in the main
  checkout.

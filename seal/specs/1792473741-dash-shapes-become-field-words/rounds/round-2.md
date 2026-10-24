# 1792473741-dash-shapes-become-field-words — review round 2

target: 71eb87a3, fixes fce78495..743d3027

A verifying round over the four fix commits, 52e385ea, db30d32e, f3362250
and 743d3027. Carried from round 1 as coordinates, not re-searched: where
the verdict readers are called (`seal_stamp.py`, `hooks/commitgate.py`), and
that the sealer graders' patterns are generated in `evals/scripts/rule_cases.py`.
Probes ran in a `git clone --no-local` at 71eb87a3, through one file,
`test_tmp_round2_probe.py`, run once and deleted with the clone. As in
round 1, the HTML comment opener is written in words, "the opener".

## Findings

### 1. `comment_scan` is quadratic in the code spans on a line, and its timing case's bound hides it

severity: should
location: `skills/verify/scripts/unverified_check.py:217-265`, `tests/test_unverified_rows_close.py:1840-1849`
evidence: executed `python3 test_tmp_round2_probe.py`
verdict: fixed c6b7b92c
regression: round-1#2

The unit is `comment_scan`'s outside-a-comment branch, which db30d32e
rewrote. The frame asks a pattern that repeats to carry a timing case
(phase 1's direction, with #941's round 3 behind it). The fix added the case
`test_the_comment_scan_is_not_quadratic_in_backtick_runs`. But its loop
slices the rest of the line and searches it again for each code span, so the
scan is quadratic in the spans on one line. The shape came from round 1's
paste-ready fix, which this record's author wrote, so the defect is the
round's suggestion as much as the fix pass's.

Executed, on lines with no opener, each one span after another: 100000
characters took 0.9 s, 200000 took 3.4 s, 400000 took 13.3 s and 800000
took 53.9 s. Each doubling of the length multiplies the time by four. Before
db30d32e, a line with no opener cost one `find`. The case's second input,
100000 characters of single backticks, read in 0.36 s here, under its 1 s
bound but with no margin on a slow runner. Its name says "not quadratic",
and the scan is quadratic. Every reader goes through this scan
(`readable`, `strip_comments`, `unclosed`), the stamp and the commit gate
included. A long line is uncommon in a record, so this is a `should`.

The fix: walk the line by index, look for the opener once and again only
after passing it, and keep a line with no opener left without looking at
its spans at all.

```python
    inside = False
    for line in lines:
        began = not inside
        kept, pos, start = [], 0, -1
        while pos < len(line):
            if inside:
                end = line.find(CLOSER, pos)
                if end == -1:
                    break
                pos, inside = end + len(CLOSER), False
                continue
            if start < pos:
                start = line.find(OPENER, pos)
            if start == -1:
                kept.append(line[pos:])
                break
            run = BACKTICKS.search(line, pos, start)
            if run:
                # CommonMark 6.1: a span opened before the opener wins; a run
                # with no closer of its own length on the line is literal.
                width = run.end() - run.start()
                closer = next(
                    (m for m in BACKTICKS.finditer(line, run.end())
                     if m.end() - m.start() == width),
                    None,
                )
                upto = closer.end() if closer else run.end()
                kept.append(line[pos:upto])
                pos = upto
                continue
            kept.append(line[pos:start])
            pos, inside = start + len(OPENER), True
        yield began, "".join(kept)
```

A closer found past `start` puts `pos` past it, and `start < pos` then
searches again. The case should read 400000 characters of closed spans with
no opener, and 400000 with an opener at the end, each in under 1 s. The
quadratic scan takes 13 s on the first, so the case fails against it.

answer: Holds, and fixed with the record's index walk, which looks for the opener only once the walk passes it. Before the rewrite, the case's new inputs were seen failing: 2 failed in 26.7 s (executed). After it, with the walk cut back to search for the opener at every span, `mutation-check` reports the case red (executed). The orchestrator relayed `tests` run 39382007019 at 71eb87a3: the old case read 1.10 s against its 1 s bound on a loaded macOS runner. So 0763cff1 sets each of this item's four timing cases at 5 s. Those are this case, `test_the_near_miss_reading_is_linear_in_the_line`, `test_the_verdict_patterns_are_linear_in_the_line` and `test_the_title_line_pattern_is_linear_in_the_line`. The comment scan's case reads 800000 characters of closed spans, which takes under 0.2 s linear (executed). The quadratic scan took 13 s at 400000 characters and 54 s at 800000. With the walk cut back as above, the case went red at 52.7 s (executed). The other three cases run in under 0.1 s, and a backtracking pattern never ends (phase 1 to 4 records), so 5 s sits an order of magnitude from each. The case's name now states what it holds.

### 2. The template's verdict comment now opens three lines with `Verdict:`, so the sealer evals' verdict graders match the comment

severity: should
location: `templates/sdd-guarantee.md:29-36`, `evals/scripts/rule_cases.py:687-693`, `tests/test_the_sealer_guarantees.py`
evidence: executed `python3 test_tmp_round2_probe.py`
verdict: fixed b828ac92
regression: round-1#3

The unit is the template's verdict comment, which f3362250 changed. The
frame says the sealer graders' patterns still match the new verdict line
(spec S14, and plan A2a, which chose the shape partly for that). The fix
moved the three example lines out of their four-space indent to the start
of the line, inside the comment. The graders read the raw file with the `m`
flag (read, `evals/scripts/behaviour.py:48-60` and
`evals/behaviour/sealer/rule-sealer-sealed/graders/shape-verdict.md:1-6`): `^Verdict:\s*\**sealed\**\s*$` in the `sealed` case and
`^Verdict:\s*\**withheld\b` in four withheld cases. Executed against the
template: they now match its `Verdict: sealed` and `Verdict: withheld`
comment lines. Sealers keep that comment: two of the 13 live guarantees
carry the old one (`1792251842`, `1792368013`). A sealer that keeps the new
one passes its verdict grader whatever it wrote. The `sealed` case has no
truth grader, so its only check of the verdict goes vacuous. The defect
came from the fix, not the frame. Since f3362250, the reader refuses an
indented copy at its line, so the indent no longer had to go.

The fix: name the three shapes in the comment as code spans in a sentence,
so no line of the comment opens with `Verdict:`. After the opener, the
comment reads:

```markdown
 One line, exactly one of `Verdict: sealed`,
`Verdict: withheld reason: <the claim, its party, its coordinate>` or
`Verdict: undecided question: <the question, for the owner>`, at the start
of the line and with no emphasis. An owner's answer is a line under it,
`Answered <date> by <who>: <answer>`, which the next run keeps. -->
```

Add a case to `tests/test_the_sealer_guarantees.py`: no `SEALER_RUNS`
verdict pattern from `evals/scripts/rule_cases.py` matches a line of
`templates/sdd-guarantee.md`. Before the fix it fails on the two lines
above.

answer: Holds, and fixed with the record's comment. The three shapes are code spans in one sentence, and the line under the comment reads `<one of the three shapes above>`. `test_no_sealer_grader_matches_a_line_of_the_template` reads every `pattern: '^Verdict:` line of the generated sealer graders under `evals/behaviour/sealer/`, so it reads what the graders run rather than restating the generator. It asserts at least nine patterns and that none matches a template line. It passes. Against f3362250's template the same reading matched five patterns, the four `withheld` shape graders and the `sealed` one (executed).

### 3. A hyphen for the space in `earlier run` still drops the entry unread and unrefused

severity: should
location: `skills/code-review/scripts/chain_check.py:125`, `tests/test_the_sealer_guarantees.py`
evidence: executed `python3 test_tmp_round2_probe.py`
verdict: fixed de46b6db
reopens: round-1#4

743d3027 closed round-1#4 as fixed, and its close holds for the five
separators that finding listed. Its defect still stands for one spelling.
`EARLIER_MEANT` asks for whitespace between the two words, `earlier\s+runs?`.
Executed: for the cell `abc1234 against main; earlier-run: bbb2222 sealed`,
`earlier_verdicts` returns `[]`. That is the round-1 symptom, the entry
neither read nor refused. A hyphen typed for a space is this item's own
class, and the owner's direction is that no near miss passes. Round 1's
pattern carried the same gap, so the reopen is on the record's enumeration
as much as on the fix. A tab or a no-break space between the words is
already refused (executed).

```python
EARLIER_MEANT = re.compile(r"[;,]? ?earlier[\s_-]*runs?\b\s*:?\s*", re.IGNORECASE)
```

`[\s_-]*` before a literal is linear. The parametrised entry case should
take `; earlier-run: `, `; earlier_run: ` and `; earlierrun: `. The linear
case should take `earlier` followed by 100000 hyphens.

answer: Holds. It was fixed by deciding the row's shape once rather than with the record's wider pattern, on the orchestrator's direction: CLAUDE.md says that when fixes chase one mechanism's edge cases, you ask what it decides. The `Target SHA` value is now `TARGET_HEAD`, `<sha> against <base>` with each one word. After it comes nothing, or `; earlier run: ` and an `EARLIER_ENTRY` read exactly to the next separator, over and over. `earlier_verdicts` returns any other text after the target quoted with no word, and the arm refuses it at the row (`TARGET_WRITTEN`). `EARLIER_MEANT` is gone, so no spelling of the separator is looked for at all.
- Cases (executed): the parametrised case holds the five round-1 separators, the hyphen, the underscore and the joined word, a second word of base (` @ 4a6e24f6`) and a parenthesis. Each was seen red before the fix: 7 failed. A further case reads an entry exactly up to the next separator.
- Mutations (executed): returning nothing for unread text went red, and so did a base word allowed to hold `;` and the arm skipping the row. Stripping each entry survived until the exactness case was added, then went red.
- Live rows (executed): of the 13 merged guarantees, 4 now carry text after the target that the row refuses, as ` @ <sha>` or a parenthesis naming how the base resolved: `1792251842`, `1792252400`, `1792365855` and `1792459424`. They are merged, so no pull request judges them again. Their earlier entries now read no word for the stamp, which matters only when a guarantee is committed.
- Places stating the row, rewritten in the same commit (read): `templates/sdd-guarantee.md`'s placeholder, `agents/sealer.md`'s rule and the changelog fragment now say the row holds `<sha> against <base>`, each one word, and nothing else.
- Stands: `spec.md` names `against <base>` and no more, and is the framer's.

## Confirmations

confirms: round-1#1
The fallback finds its line with the search's own rule. 52e385ea replaces
the `splitlines` call with `re.search(rf"(?im)^[ \t]*...")`. Executed: a
capitalised line and an indented line are quoted, and a line separated only
by U+2028 is not, consistent with the search. Executed in the clone:
`bin/test tests/test_every_reader_ends_a_line_where_gfm_does.py -q` gave 18
passed, exit 0. Run 39382007019 at 71eb87a3 was still running when this
round ended (`## Not judged`).

confirms: round-1#2
The hidden verdicts are read. Executed at 71eb87a3: each of the 13 live
guarantees gives one verdict line, `1792449518` and `1792459424` now
`sealed`, and `unclosed` finds nothing in any of them. The smith's count
holds (executed): `bin/unverified-check seal/specs/` reads 120 overviews,
53 open, 333 closed, 0 unreadable. `guarantee()` now calls `unclosed` before
reading the verdict lines (read, `chain_check.py:1729-1730`). The scan cases
the orchestrator named (executed):
- **An opener and a span on one line, in either order.** An opener before a
  span opens the comment. A span before an opener is kept, and the comment
  after it is blanked.
- **Backticks inside a comment.** They are ordinary characters; the comment
  ends at its first closer.
- **A span inside a double-backtick span.** Kept whole.
- **An escaped backtick.** Read as a span opener, which differs from
  CommonMark. The page shows the text after it as text either way, because
  an unclosed inline opener is literal there too.
- **A span that wraps across lines.** Read as literal backticks, so the
  opener after it opens a comment. The docstring states this limit. With no
  later closer, `unclosed` names the line. With a later closer, the lines
  between are hidden silently, a `### ` heading among them in the probe
  (`## Not judged`).

Finding 1 above is a new defect in this unit, not a failure of this close.

confirms: round-1#3
The reader refuses an indented verdict line. Executed: four spaces, a tab
and a single space before `Verdict: sealed` each read as no word, so the arm
refuses the line naming the three shapes. Trailing spaces still read as
`sealed`, as the docstring says. One limit stands: a zero-width space
before the indent is removed by `visible` before the indent check, so that
line reads as `sealed` (executed). Nobody types that, so it is no finding.
Finding 2 above is a new defect in the template half of this fix.

confirms: none
The new tests, read against their groups: the five `comment_scan` shapes,
the counted row behind a quoted opener, the round record quoting the
opener, the guarantee arm on a quoted and an unclosed opener, every live
guarantee showing one verdict, the two indented near misses and the five
separators. Each pins a case the module did not hold before. None
duplicates a neighbour. The exception is the timing case, which finding 1
names.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a code span wrapped across lines should be read as a span. Today the opener inside it opens a comment, and a later closer hides the lines between without a refusal | `skills/verify/scripts/unverified_check.py#comment_scan` | the owner |
| The `tests` run 39382007019 at 71eb87a3 | CI | the orchestrator |
| The full suite, the repository-wide lint and the typecheck | the work item | the orchestrator's broad run, after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_round2_probe.py` (in the clone, run once, deleted) | Scan time grows four times per doubling of a line of spans (0.9 s at 100000 characters, 53.9 s at 800000). The nine scan shapes read as listed above. All 13 guarantees show one verdict and `unclosed` finds nothing. Indented verdicts read as no word. `earlier-run` gives `[]`. Both grader patterns match the template's comment lines |
| `bin/unverified-check seal/specs/` (in the clone) | 120 overviews, 53 open, 333 closed, 0 unreadable, exit 0 |
| `bin/test tests/test_every_reader_ends_a_line_where_gfm_does.py -q` (in the clone) | 18 passed, exit 0 |

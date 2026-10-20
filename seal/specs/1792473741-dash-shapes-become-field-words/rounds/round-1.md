# 1792473741-dash-shapes-become-field-words — review round 1

target: 565dfa24 against release/v0.22.3

Round 1 has no earlier round, so no fact was carried and every verdict below
was reached at 565dfa24. Probes ran in a `git clone --no-local` of the
repository at 565dfa24, through one file, `test_tmp_round1_probe.py`, run
twice and deleted with the clone. The HTML comment opener is written here in
words, "the comment opener" (less-than, exclamation mark, two hyphens),
because finding 2 is that this record's own reader would blank everything
after it.

## Findings

### 1. The cross-platform tests run fails: `title_from` splits the commit body with a second line rule

severity: must
location: `.github/scripts/publish_release_note.py:190-196`, `tests/test_every_reader_ends_a_line_where_gfm_does.py:490-507`
evidence: read `.github/scripts/publish_release_note.py:184-203`, `tests/test_every_reader_ends_a_line_where_gfm_does.py:350-365`, `tests/test_every_reader_ends_a_line_where_gfm_does.py:490-507`
verdict: fixed 52e385ea

The orchestrator relayed run 39380012235 at 565dfa24 (its `executed`, not
this round's): `test_every_splitlines_call_left_is_named_with_its_reason`
fails on ubuntu, one macOS split and one Windows split, naming
`('.github/scripts/publish_release_note.py', 'title_from'): 1`. Phase 4
added the call: the base's `publish_release_note.py` holds no `splitlines`
(`git show b451e503:.github/scripts/publish_release_note.py`, count 0). A
ready pull request fails CI on it.

The phase 4 record claims "the reader and the line the checklist copies
agree". The line rule disagrees inside `title_from` itself. The search,
`title_line_re`, reads with `re.M`, which ends a line at a newline alone.
The fallback quotes a line found by `str.splitlines`, which also ends a line
at U+2028, U+0085, a form feed and others. So the line the log quotes need
not be a line the search judged. Classifying the call into `OUT_OF_CLASS`
does not fit either: the nearest reason, `GIT`, is "paths, refs, subjects
or status", and a commit body carrying a pull request title is none of
those. The owner's direction is one rule stated once, so the fallback
should find its line with the search's own rule, and the call goes.

```python
    # The search's own line rule: `re.M` ends a line at "\n" alone, so the
    # line quoted is a line `title_line_re` judged. Any case, any indent.
    seen = re.search(rf"(?im)^[ \t]*{re.escape(TITLE_LABEL)}.*$", message or "")
    first = seen.group(0).strip() if seen else None
```

This replaces lines 190-196. The S16 cases (`Release:` and a leading space
among them) still find their line. `.` stops at a newline and keeps a
`\r`, which `strip` removes. The case then counts no call in `title_from`
and needs no `OUT_OF_CLASS` entry.

answer: Holds, and fixed as the record gives it. The fallback finds its line with `(?im)^[ \t]*release:.*$`, so `title_from` makes no `splitlines` call and `OUT_OF_CLASS` gains no entry. `tests/test_every_reader_ends_a_line_where_gfm_does.py` passes (executed); with a `splitlines` call planted back in `title_from`, `mutation-check` reports its case red (executed). The S16 cases pass, and with `(?im)` cut to `(?m)` they go red, the capitalised line no longer quoted (executed). The timing case reads a line of 100000 spaces and tabs before `Release` too.

### 2. A comment opener inside a code span hides every later line, so two merged guarantees' `Verdict: sealed` is invisible to the verdict reader

severity: must
location: `skills/verify/scripts/unverified_check.py:217-245`, `skills/code-review/scripts/chain_check.py:1640-1649`, `skills/code-review/scripts/chain_check.py:1720-1727`, `tests/test_the_sealer_guarantees.py`
evidence: executed `python3 test_tmp_round1_probe.py`
verdict: fixed db30d32e

Claimed (phase 2, and the orchestrator's relay of the hand-back): the
guarantees of `1792449518` and `1792459424` hold `Verdict: sealed` that
`verdicts_of` cannot see, because `unverified_check.py#readable` blanks
every line after a comment opener sitting in a code span of a table cell.
Found, executed: `verdicts_of` returns `[]` for both, while each file holds
the line `Verdict: sealed` at line 59 and line 45. The openers are a
code span in the `Result` cell at line 45 of the first, and a code span
quoting a `git grep` command at line 17 of the second. A three-line text, a
table row whose cell holds the opener in a code span and then the
verdict line `Verdict: sealed`, also reads `[]`. The other 11 guarantees read: 10
`sealed` and the retired `sound`.

The cause is `comment_scan`. It finds the opener anywhere on a line and
does not know code spans. CommonMark (6.1) gives a code span that opens
first precedence over an HTML construct inside it. GitHub renders those
two cells as code and the verdict line as text. The reader sees what no
reader of the page sees.

What it breaks, read from the callers:

- **The guarantee arm.** `guarantee()` reads 0 verdict lines and refuses
  at line 0 with "0 `Verdict:` lines; the guarantee carries one". The file
  carries one, and the line that hid it is never named. `unclosed()`, which
  names the opener's line for a round record, is not called for a
  guarantee (executed: `unclosed` on the three-line text names line 7).
  This item rewrote this arm and its message.
- **The stamp.** `seal_stamp.py#_queue_one` (lines 1195-1196) and
  `queue_for_local_guarantee` (lines 1325-1326) queue nothing for a
  `sealed` they cannot see. `sealed_before` (lines 1117-1118) counts no
  earlier seal. This round did not establish whether those two items drew
  their stamp when they merged (`## Not judged`).
- **The commit gate.** `hooks/commitgate.py#guarantee_off_history` (lines
  270-272) skips a guarantee whose verdict it cannot see. A `sealed` over a
  commit the branch does not hold then commits unjudged: the check fails
  open.
- **The release's chain check** does not reach them. `main` treats a
  routing file another pull request's squash carried as judged there, so
  the release pull request runs no guarantee arm for either item.
- **Round records.** They read through `read_whole`, which calls
  `unclosed`. A record quoting the opener in a code span is refused at the
  opener's line, so a correct record is refused there (executed: `readable`
  on such a line followed by `## Findings` keeps only the text before the
  opener). This record avoids the characters for that reason.

This is the owner's class, a symbol a reader trips on as syntax, and this
item's verdict reader is what reads through it. A sealer's guarantee for
this item is likely to quote this finding. If it does, its own verdict
vanishes.

Enumerated for the fix (contract 12): every reader through `readable` or
`strip_comments` inherits the blanking. Those are the overview reader
(`check_text`), the round records, the guarantee, `broad-gate.md` and the
stamp's and gate's guarantee reads. Of these, this round probed only the
guarantee and the round-record line. Hidden open rows of `## Not verified`
are a `## Not judged` row.

```python
# The run of backticks that opens or closes an inline code span.
CODE_RUN = re.compile(r"`+")  # NAME NOT IN TREE: new, beside comment_scan


def comment_scan(lines):
    inside = False
    for line in lines:
        began = not inside
        rest, kept = line, ""
        while rest:
            if inside:
                end = rest.find("-->")
                if end == -1:
                    rest = ""
                else:
                    rest, inside = rest[end + 3 :], False
                continue
            start = rest.find("<!" + "--")  # the opener, as line 239 finds it
            run = CODE_RUN.search(rest)
            if run and (start == -1 or run.start() < start):
                # CommonMark 6.1: a code span opened first wins, so an opener
                # inside it is text. A run with no closer of its own length on
                # this line is literal backticks, and the walk goes on after it.
                closer = re.compile(rf"(?<!`){run.group(0)}(?!`)")
                found = closer.search(rest, run.end())
                upto = found.end() if found else run.end()
                kept, rest = kept + rest[:upto], rest[upto:]
            elif start == -1:
                kept, rest = kept + rest, ""
            else:
                kept, rest, inside = kept + rest[:start], rest[start + 4 :], True
        yield began, kept
```

Precondition: a code span closes on its own line. A span wrapped across
lines (CommonMark allows it) still reads as literal backticks followed by
the opener, as today. `unclosed` walks `comment_scan`, so it changes with
it. In `guarantee()`, before `verdicts = verdicts_of(reader, text)`:

```python
    # A region nobody closed hides the verdict line; name where it opened.
    problems.extend(unclosed(reader, text, rel))
```

The regression cases belong in `tests/test_the_sealer_guarantees.py`. One
is a guarantee whose claims cell quotes the opener in a code span and
reads its `Verdict: sealed`. The other reads each live `guarantee.md` and
finds exactly one verdict line in it. Run the modules naming
`comment_scan`, `readable` or `strip_comments` at the phase boundary,
`tests/test_unverified_rows_close.py` and `tests/test_chain_check.py`
among them.

answer: Holds, and fixed. `comment_scan` lets a backtick run opened before the opener win when a run of its own length closes it on the line, and reads a run with no such closer as literal, `_liveness`'s reading A. It uses the file's own `BACKTICKS`, `OPENER` and `CLOSER`, so no `CODE_RUN` was added. `guarantee()` now extends its problems with `unclosed()` before it reads the verdict lines. Cases added: an opener in a code span opens no comment, and its literal-backtick, span-then-comment and inside-a-comment counterparts; an open row of `## Not verified` below such a cell is counted (this round's `## Not judged` row about the overview reader); a round record quoting the opener reads both findings; a guarantee quoting it in a claims cell passes the arm; one with an opener nobody closed is refused at the opener's line; and every committed `guarantee.md` shows its one verdict line. With the span branch cut, which is the old scan, `mutation-check` reports the cases red, and so it does for each of two other breaks of the branch and for the `unclosed` call removed (executed). The other readers in the class: every reader through `readable` or `strip_comments` (`check_text`, the round records, the guarantee, `broad-gate.md`, the stamp and the commit gate) reads through this one scan, so the one change reaches them. `hooks/blocks.py` models HTML comment blocks, which open only at the start of a line, and calls a line after a mid-line opener uncertain, never hidden (`leaves_open`'s docstring), so it stands. `rule_changes.py` reads through `live_lines`, which already knew code spans. The gather's markers are matched as whole lines. `bin/unverified-check seal/specs/` reads 120 overviews with 53 open and 333 closed: the 52 and 333 phase 1 counted, plus this item's own open row. No hidden row came to light (executed).

### 3. An indented verdict line, a code block when rendered, reads as `sealed`

severity: should
location: `skills/code-review/scripts/chain_check.py:1645-1648`, `templates/sdd-guarantee.md:31-33`, `tests/test_the_sealer_guarantees.py`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`
evidence: executed `python3 test_tmp_round1_probe.py`
verdict: fixed f3362250

`spec.md` *Scope* 2 says the verdict line "is read whole and exactly".
*Data & interfaces* adds "no markup before `Verdict:`". The changelog
fragment claims "it is exactly one of" the three shapes. Found, executed:
the line `    Verdict: sealed` (four spaces) and a tab before `Verdict: sealed` each
come back from `verdicts_of` as `Verdict: sealed`, and `verdict_word` reads
them as `sealed`. The cause is `reader.visible`, which strips both ends of
the line before the shape is matched. After a blank line, four spaces make
an indented code block, so the page shows code where the reader counts a
verdict. The stamp and the commit gate read the same `sealed`. The new
template invites this near miss: its comment shows the three shapes
indented four spaces (lines 31-33), so a sealer that copies one keeps the
indent. `blank_fences` hides a fenced example from the reader, and nothing
hides an indented one.

```python
    for i, raw in enumerate(reader.readable(text or "")):
        line = reader.visible(raw)
        if MEANT_VERDICT.match(line):
            # An indent is markup, a code block at four spaces: the line is
            # handed back with it, so no shape reads it whole.
            found.append((i + 1, raw.rstrip() if raw[:1].isspace() else line))
```

This replaces lines 1645-1648. Add `"    Verdict: sealed"` and
`"\tVerdict: sealed"` to `NEAR_MISSES` in
`tests/test_the_sealer_guarantees.py` and to `NEAR_SEALED` in
`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`. Each must be
seen red against the reader as it stands.

answer: Holds, and fixed as the record gives it. `verdicts_of` hands back an indented line with its indent, so no shape reads it whole and the arm refuses it, naming the three shapes. The two indented lines are in `NEAR_MISSES` and `NEAR_SEALED`, which also feed the commit gate's quiet-off-its-fact case; with the old return restored, `mutation-check` reports the near-miss cases red (executed). The template's comment now shows the three lines at the start of the line and says so, and `agents/sealer.md` step 5 and the changelog fragment say "at the start of its line" beside "with no emphasis". `spec.md`'s `## Rule changes` `to:` reads "written exactly so", which already covers the indent; it is the framer's file and is not edited here.

### 4. A misspelt `; earlier run: ` separator drops the entry unread and unrefused

severity: should
location: `skills/code-review/scripts/chain_check.py:1393-1404`, `skills/code-review/scripts/chain_check.py:117`, `tests/test_the_sealer_guarantees.py`
evidence: executed `python3 test_tmp_round1_probe.py`
verdict: fixed 743d3027

The spec says an earlier run "carries the word alone", with every other
spelling refused at its line (S9, and the owner's direction that no near
miss passes). The entry is refused only after the cell has been split on
the exact separator `EARLIER_RUN`. Found, executed: `earlier_verdicts`
returns `[]` for a cell in which `bbb2222 sealed` follows `;  earlier run: `
(two spaces), `; Earlier run: `, `; earlier run ` (no colon),
`; earlier runs: ` or `, earlier run: `. With `[]`, the guarantee arm has
nothing to refuse, and the row passes. The stamp reads the same `[]`, so an
earlier `sealed` under such a separator counts as no earlier stamp.
`_queue_one` still has `sealed_before` to stop a second stamp in shared
mode. `queue_for_local_guarantee` has nothing else (lines 1336-1340), so a
local-mode reseal draws the stamp twice. The separator is a field word like
the verdict's, and it is the one spelling on the row that the new reader
still does not judge.

```python
# The separator in any spelling, so a misspelt one is refused, not skipped.
# No leading `\s*`: on a cell of spaces it would backtrack quadratically.
EARLIER_MEANT = re.compile(r"[;,]? ?earlier\s+runs?\b\s*:?\s*", re.IGNORECASE)  # NAME NOT IN TREE


def earlier_verdicts(cell):
    cell = cell or ""
    out = []
    for sep, entry in zip(EARLIER_MEANT.findall(cell), EARLIER_MEANT.split(cell)[1:]):
        m = EARLIER_ENTRY.fullmatch(entry.strip()) if sep == EARLIER_RUN else None
        out.append((m.group(1), m.group(2)) if m else ((sep + entry).strip(), None))
    return out
```

The arm's existing loop then refuses each such entry at the `Target SHA`
row's line. The five separators above belong in the parametrised entry
case of `tests/test_the_sealer_guarantees.py`. A cell of 100000 spaces after
`earlier` belongs in `test_the_verdict_patterns_are_linear_in_the_line`.

answer: Holds, and fixed with the record's `EARLIER_MEANT` and loop. A refused entry is quoted with its separator in front. A separator with more spaces than the pattern's one before `earlier` is found from `earlier` on, and its entry is refused all the same; the case asserts that. The five separators are in the parametrised entry case, and `; Earlier run: ` is in the arm's case at the `Target SHA` row. The linear case reads `earlier` before 100000 spaces, and `earlier runs` between two runs of them. Two mutations went red: splitting on the exact separator again, and reading an entry whatever its separator. With the pattern nested as `(?:[;,]?\s*)*`, the linear case timed out after 30 s with no verdict (all executed). The 13 live earlier-run entries still read, none refused (executed). `broad_gate.py#EARLIER_RUN` writes the separator, and `tests/test_broad_gate.py` holds it equal to `chain_check.py`'s; it stands. The two readers that take only the newest run's first word, `newest_run` and `seal_stamp.py:1250`, read the part before the first exact separator, so a misspelt one changes nothing there; they stand.

## Confirmations

confirms: none
The stamp still draws for a `sealed` verdict. `verdicts_of` and
`verdict_word` read `Verdict: sealed` as `sealed`, and the stamp and the
gate compare with `chain.SEALED` unchanged (`seal_stamp.py:1195-1196`,
`hooks/commitgate.py:270-271`, read). Executed in the clone:
`bin/test tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py -q`
gave 111 passed, exit 0, `test_a_sealed_guarantees_commit_queues_one_stamp`
among them.

confirms: none
No new pattern nests a bounded repeat in a starred group. `VERDICT_SHAPE`,
`MEANT_VERDICT`, `EARLIER_ENTRY`, `NEAR_NOTHING`, the moved `ITEM_RE` and
`FIELD_RE`, and `title_line_re` are flat (read in the diff). Executed: each
one, given 60000 characters of its repeated class, returned in under 0.01 s.

confirms: none
The S6 near misses are refused at their line. Executed: `Verdict: sealed.`,
`> Verdict: sealed`, a no-break space after the colon and two spaces before
the reason each read as no word. `Verdict - sealed` and `The verdict: sealed`
are no verdict line, so a guarantee holding only one of them is refused as
holding none.

confirms: none
The `## Not verified` reader refuses at its line what it cannot read.
Executed: `none` and U+2014, `- Nothing`, `nothing.`, `1. nothing`,
`> nothing`, `_none_`, `N/A`, `nonesuch`, a block then a table, and
`  why:x` are each refused in the working tree. The block reads as no rows.
At a base, only the `NEAR_NOTHING` lines relax. The phase 1 claim that
`nonesuch` is refused as prose holds.

confirms: none
The release title falls back and says what it expected. Executed: a leading
space, two spaces before `symptoms:`, the dash line and a body with no line
each give `v1.2.3`. The log names `release: 1.2.3 symptoms: <the symptoms>`
and quotes the line found, or says none is there. A trailing `\r` or spaces
are stripped from a title that reads.

confirms: none
Phase 2 claims "All 13 earlier-run entries read as `withheld`", and S9
asks the live entries to read. Executed: the 13 entries of the live
guarantees all match `EARLIER_ENTRY`.

confirms: none
Phase 4's S13 sweep and S4's grep hold as recorded. Executed at 565dfa24:
the `git grep -nF` for each S13 string outside `seal/specs` and `changelog`
finds the lines `phases/phase-4.md` names and no others. S4's grep prints
lines 87 and 88 of `unverified_check.py` only.

confirms: none
This spec's one rule change applies. Executed: `rule_changes.parse` reads
one `change` with no error. `replay` over `docs/` applies it, and the
section then reads the three field-word shapes.

confirms: none
The tests the diff adds, read against their groups: the S6 refusal, the S7
stamp and gate cases, the S9 entry and row cases, and the linear-time case.
Each covers a unit or a shape its module did not hold before. None
duplicates a case beside it.

confirms: none
The smith's suite label is honest. `overview.md` `## Not verified` leaves
the full suite, lint and typecheck to the orchestrator's broad run, and
finding 1 is a case that run would have met.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether `1792449518` and `1792459424` drew their stamp, and how their pull requests passed a guarantee arm that read no verdict line | `seal/specs/1792449518-settle-squashes-specs-into-docs-in-place/guarantee.md:45`, `seal/specs/1792459424-docs-states-the-current-rule-in-one-read/guarantee.md:17` | the owner |
| Whether an overview's open `## Not verified` rows after the opener in a code span go uncounted, the same class as finding 2 in the overview reader | `skills/verify/scripts/unverified_check.py#check_text` | the fix pass for finding 2 |
| The full suite, the repository-wide lint and the typecheck at 565dfa24 | the work item | the orchestrator's broad run, after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_round1_probe.py` (in the clone, run twice, deleted) | 11 of 13 live guarantees give one verdict line, and `1792449518` and `1792459424` give none. An indented or tabbed `Verdict: sealed` reads `sealed`. Five misspelt separators give `[]`. Every new pattern finished in under 0.01 s on 60000 characters. The rule change replays. `unclosed` names the opener's line |
| `bin/test tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py -q` (in the clone) | 111 passed, exit 0 |
| `git grep -nF` per S13 string, and S4's `git grep -nE`, at 565dfa24 | the lines `phases/phase-4.md` names, and lines 87 and 88 of `unverified_check.py` |

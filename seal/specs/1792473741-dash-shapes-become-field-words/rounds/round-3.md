# 1792473741-dash-shapes-become-field-words — review round 3

target: 9f217441, fixes 8ee92665..598df477

A verifying round over c6b7b92c, 0763cff1, b828ac92, de46b6db and
598df477. Carried from rounds 1 and 2 as coordinates, not re-searched:
- **The callers of the verdict and row readers:** `seal_stamp.py`,
  `hooks/commitgate.py#guarantee_off_history` and `chain_check.py#main`.
- **Where the sealer graders are generated:** `evals/scripts/rule_cases.py`.

Probes ran in a `git clone --no-local` at 9f217441, through two files,
`test_tmp_round3_probe.py` and `test_tmp_round3_records.py`. Each ran once,
and both were deleted with the clone. As before, the HTML comment opener is
written in words, "the opener".

## Findings

None. Each close of round 2 holds, the new units read as their frame and the
orchestrator's direction say, and the four merged guarantees the new row
shape refuses are read by no check that gates anything (below).

## Confirmations

confirms: round-2#1
`comment_scan` is linear in the spans on a line. c6b7b92c walks the line by
index and looks for the opener again only once the walk passes it.
Executed, timings:
- 800000 characters of closed spans with no opener: 0.001 s.
- The same line with an opener at the end: 0.11 s.
- 800000 characters of single backticks: under 0.001 s.
- 1199 runs of growing width, then an opener: 0.24 s.
- Repeated blocks of widths 1 to 59: 0.002 s.

The quadratic scan took 53.9 s on the first in round 2. The shapes the
orchestrator named read as before the rewrite, with the line-start state
unchanged (executed):
- **Opener before a span:** a comment.
- **Span before an opener:** the span is kept and the comment after it blanked.
- **Backticks inside a comment:** ordinary characters.
- **A closer inside a span after a comment opener:** ends the comment, as
  CommonMark's first closer does.
- **Two comments on one line:** both blanked.
- **A span holding an opener, then a real comment:** the span is kept and
  the comment blanked.

A span wrapped across lines is still read as literal backticks, which round
2 left to the owner. The scan change reaches no round record. Executed:
none of the 131 committed `rounds/round-*.md` reads differently from the
base's scan (b451e503), so the release seal's finding counts
(`release_seal.py#chain_counts`) do not move. The overviews that read
differently keep the counts round 2 confirmed. The changelog gather reads
through `live_lines`, not through this scan (read,
`unverified_check.py:274-280` and `unverified_check.py:705-720`; only
`readable` and `check_text` call it there).

0763cff1 raises the four timing cases' bound from 1 s to 5 s. That is still
an order of magnitude below the 53.9 s quadratic time, and above the
linear times listed above. CI run 39382007019 failed the old bound at 1.10 s.

confirms: round-2#2
No line of the template opens with a verdict a grader reads. b828ac92
names the three shapes as inline code spans in the comment. Executed:
`^Verdict:\s*\**sealed\**\s*$`, `^Verdict:\s*\**withheld\b` and
`^Verdict:\s*\**undecided\b` match no line of `templates/sdd-guarantee.md`.
The one line opening `Verdict:` is the placeholder, `Verdict: <one of the
three shapes above>`.
`test_no_sealer_grader_matches_a_line_of_the_template` reads the generated
grader files rather than a copy of their patterns. Executed in the clone:
`bin/test tests/test_the_sealer_guarantees.py -q` gave 57 passed, exit 0.

confirms: round-2#3
The hyphen spelling is refused, and so is every other text after the target.
de46b6db and 598df477 give the `Target SHA` value one shape:
`<sha> against <base>`, each one word, then nothing or exact
`; earlier run: ` entries. Executed:
- `; earlier-run: `, two spaces before `earlier`, a parenthesis after the
  base, `@ <sha>`, a bare SHA, an upper-case SHA and a trailing comma each
  come back as one unread entry, which the arm refuses at the row.
- A space before the next separator leaves that entry unread and the next
  one read.
- `release/v0.22.3@{upstream}` reads as one base word.

**What refusing the four merged rows breaks.** The rows are those of
`1792251842`, `1792252400`, `1792365855` and `1792459424`. Executed, they
come back unread for ` @ <sha>` or a parenthesis after the base, as the
smith reported. The other nine read, every entry `withheld`. No check that
gates anything reads them:
- **The release pull request into `main`.** Executed: `chain_check.py
  --baseline origin/main` at 9f217441 in the clone, standing in for the
  0.22.3 release pull request. It marks every carried declaration "judged
  at its own pull request", `1792459424` by b451e503 (#1001) and
  `1792449518` by ac83bdf3 among them. It runs no guarantee arm for any of
  them, exit 0. Its only refusals are this item's own (round 2's open
  verdicts at the time, and no `broad-gate.md` or `guarantee.md` yet).
- **The stamp.** It reads a guarantee only when a commit changes it (read,
  `seal_stamp.py:1195-1210`), so none of the merged ones is read again.
  Their entries are all `withheld`, so no earlier `sealed` is lost. For a
  new row with stray text, entries behind the text now read as unread
  rather than read, so the stamp sees no earlier seal there. Two guards
  still stand: `sealed_before` over the history, and `already_queued`
  within the clone, which holds drawn values files too (read,
  `seal_stamp.py:1022-1044`). The arm refuses that row at the pull request.
- **The commit gate.** `guarantee_off_history` reads the verdict line and
  `target_of`, not the entries (read, `hooks/commitgate.py:262-282`).
- **Settle and the release seal.** `settle` reads no `guarantee.md`, and
  `release_seal.py` reads round records only (executed, `git grep` for the
  row and verdict readers).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the `Target SHA` row's one shape, which the orchestrator directed and `agents/sealer.md` now states, should also stand in `spec.md`'s `## Rule changes` `to:` for `docs/the-review-record.md` §*The guarantee*, which the settle writes and which today names only the earlier run's word | `seal/specs/1792473741-dash-shapes-become-field-words/spec.md#"Rule changes"` | the orchestrator |
| Whether a code span wrapped across lines should be read as a span, carried from round 2 | `skills/verify/scripts/unverified_check.py#comment_scan` | the owner |
| The `tests` run 39383686261 at 9f217441 | CI | the orchestrator |
| The full suite, the repository-wide lint and the typecheck | the work item | the orchestrator's broad run, now due |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_round3_probe.py` (in the clone, run once, deleted) | The eleven scan shapes read as listed above. Each long-line case finished in 0.24 s or less. Four of 13 live rows came back unread and nine read, all `withheld`. Ten row shapes gave the readings listed above. No grader pattern matched a template line |
| `python3 test_tmp_round3_records.py` (in the clone, run once, deleted) | Of 131 round records, none reads differently from the base's scan |
| `chain_check.py --baseline origin/main` at 9f217441 (in the clone) | Every carried declaration was judged at its own pull request. No guarantee arm ran for a merged item. Exit 0 |
| `bin/test tests/test_the_sealer_guarantees.py -q` (in the clone) | 57 passed, exit 0 |

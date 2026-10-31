# Phase 2: 1793411151-judgment-where-meaning-is-the-question

## What this phase found

**The fourth scenario does not hold whole against *Scope* item 5, and the
phase builds to item 5.** The scenario says the `refixes:` line "is printed
as not read". Item 5 derives the net from the one table's labels: a line
whose first word, case folded and stripped of emphasis, is a label's. `##
Removes` says the same: "the near-miss net is derived from the one table's
labels". `refixes` is no label's word, so that net does not name the line,
and naming it would need either the list of old spellings that item 5
removes or a wider net. A net of any one word followed by a colon was
measured over the 19 round records at HEAD: it named 20 lines, every one a
wrapped line of prose such as `holds:`, `re-run:` or `cause:` (executed, a
scratch script over `seal/threads/*/trail/rounds/*.md`). A notice on about
one prose line per record is the noise the plan's failure scenario fears,
where nobody reads the `not read:` lines. So the `refixes:` line is prose
and is not named, and the rest of the scenario holds: round 2 reads whole
and round 1's finding 2 is refused as unnamed by the next record. Judged
against `skills/core/SKILL.md` *The rule a mechanism is kept against* ("no
script carries a list of the spellings a label is written in") and the
frame's own item 5 and `## Removes` row. The case
`Test_channel::test_an_old_spelling_is_prose_and_names_no_finding` pins
that the line is not named, so a later decision to name it changes the
case on purpose.

**The guarantee's naming is a sibling of `verdicts_of`, not a change to
what it returns.** Item 5 says `verdicts_of` "names a line that opens like
the label" and that `seal_stamp.py` "reads through it unchanged". Both hold
only if `verdicts_of` keeps returning `[(line, text)]` of verdict lines. So
`verdicts_of` returns the exact `Verdict:` lines, and `unread_verdicts`
names the rest. `seal_stamp.py` is unchanged, and its 174 cases with
`tests/behaviour/test_the_sealer_guarantees.py` passed (executed).

**A guarantee holding `Verdict: sealed` beside `**Verdict:** withheld` now
passes the guarantee arm, and the stamp is drawn for it.** This is the
case `frame/plan.md` A2 names: the second line is printed as not read and
decides nothing. The same holds for the stamp, which reads through
`verdicts_of`. Whether the second line meant a verdict is the sealer's and
the orchestrator's reading.

**An indented `Verdict:` line is no verdict line.** Before, it was taken as
the verdict and refused at its line naming the three shapes. Now the
guarantee holding it alone is refused at line 0 as "0 `Verdict:` lines; the
guarantee carries one", and the line is named as not read. A line that
opens with `Verdict:` exactly and holds no shape is still refused at its
line, as before: `Verdict: Sealed` and `Verdict: withheld` among them.

**The form of a `not read:` line.** `main` prints each through the shared
reader's `annotate` as a notice, the same channel the trailer and carried
notices use. Off CI the line is `path:line  not read: <why>`. In CI it is
`::notice file=<path>,line=<n>::not read: <why>`, which GitHub renders as a
notice annotation, never as an error. A file under `trail/rounds/` that is
no `round-N.md` is named at line 0. `Test_main::test_names_a_line_it_did_not_read_as_a_notice_and_keeps_the_exit`
pins both forms and the exit code beside them (contract rule 14); the
module docstring states the form.

**A near `original:` line in a guarantee is not named.** `unread` names a
guarantee's lines that open like `Verdict:` only. The guarantee arm of the
parity check refuses such a guarantee as holding no `original:` line, at
line 0 naming the file, so the reader is sent to the file either way. A
round record's `Original:` line is named, because round records are read
for every label.

**Seen red.** Each case was run against the tree before the code changed
(executed). The first scenario's case failed on the refusal "a label in
another spelling" in place of "no `verdict:` line". The third scenario's
two cases failed because the misspelt line counted as present: the arm
exited 0, and `round_of` refused the line as another spelling. The fourth
failed on that same refusal at the `refixes:` line. The fifth failed with
the loader's "holds no table headed | Old spelling | Means |". The second
scenario's case and the guarantee's naming cases failed at base on the
missing `UNREAD_FILE` and `UNREAD_VERDICT` names before reaching their
assertions; the behaviour behind them is shown red by the mutation runs
below.

**Mutation.** One `seal mutate` call over `chain_check.py` at `84af7a2d`,
eight breaks, each run against the cases of `Test_findings`,
`Test_channel`, `Test_original_of`, `Test_originals_of`,
`Test_verdicts_of`, `Test_guarantee` and the `test_names_a` cases of
`Test_main`: 8 red, 0 survived (executed). The breaks were: a file under
another name not listed; the notices sent to the refusals, which changes
the exit code; `unread_lines` naming nothing; `opens_like` naming the exact
label too; `verdicts_of` back on the loose pattern; `verdicts_of` taking an
indented line; `unread_verdicts` naming the verdict line it read; and
`original_of` counting a line that opens like `original:`, the reading
before this phase.

**What the next phases meet.** `main` gathers the notices of a work item
in one place, `unread`. Phase 3's near `## Rule Changes` heading, which
`chain_check.py` is to print as not read, has no path there yet:
`rule_changes_of` returns refusals only. The tests that read the grammar
document still find the `Old spelling` table in `docs/the-review-record.md`,
which nothing reads now and which stays until the settle.
`Test_grammar::test_loads_beside_a_document_with_no_second_table` builds
the document without it, and reads the document itself once the settle has
removed it.

**Tests changed in place.** `BROKEN` lost its eight cases for the second
table. The near-miss cases of `Test_findings`, `Test_original_of` and
`Test_verdicts_of` are rewritten to the naming, and `NEAR_MISSES` is split
into the lines that open with `Verdict:` and hold no shape, still refused
at their line, and `OPENS_LIKE`, the lines that open like the label and
are named. `copied_tree` builds the copy both the exit-2 case and the
fifth scenario's case load.

# Phase 3: 1793411151-judgment-where-meaning-is-the-question

## What this phase found

**The frame holds at every coordinate the plan's technical context gives
for this phase.** `pact_check.py#header_key` and `#first_table`,
`rule_changes.py#parse`, `rules.py#NEAR` and `#check_lines`, and
`unverified_check.py`'s `NEAR_NOTHING`, `NEAR_CLOSED` and `LOOSE_HEADING`
stand where the plan says (read). Four readings follow, each judged against
the frame and the core.

**Item 9 removes the whole near-closed branch, not only the punctuation.**
The item says a row whose first word is `closed` followed by punctuation is
open. The branch it removes, `word.lower().rstrip(NEAR_CLOSED) == CLOSED`,
also refused `Closed` and `CLOSED`. The item's own heading says the reader
"reads `closed` exactly", so the phase removes the branch whole: a row
opening `Closed`, `CLOSED`, `closed.` or `closed:` is an open row. Such a
row is not named as not read. The reader does read it, as an open row, and
`seal unverified` prints every open row with its text, so the person sees
it either way. Judged against `skills/core/SKILL.md` *The rule a mechanism
is kept against* and item 9's "the safe direction".

**`NEAR_NOTHING`'s base reading stays.** `parse_section` with
`strict_header=False` reads a base revision's old `none — <why>` line as no
rows, so a base written before the block can still be compared. It refuses
nothing, and item 9 names the refusal alone. The `check_text` docstring
now says what the working tree does with the line instead. Judged against
item 9 and that docstring's account of what relaxes at a base.

**The naming of a near no-change block reaches a second reader, and that
is a departure.** Item 9 names `unverified_check.py`. The block is read
through one function, `nothing_block`, which `rule_changes.py#parse` also
calls, so the refusal left both readers at once (contract rule 12). In
`## Not verified`, which has no notice channel, the naming rides in the
refusal the section already gets for holding neither the table nor the
block, as `LOOSE_HEADING`'s naming rides in the missing-section refusal:
"... found prose. ... Not read: `none - x` opens like the block ... and is
not it, so it was read as prose". In a design's `## Rule changes`, the
items refuse the line as one outside an item, and the line goes to the new
`unread` field (`unverified_check.py#unread_block`), which `chain_check.py`
prints. `skills/settle/SKILL.md` *Rule changes* states both readers in
place.

**Item 7's dry-run clause held before this phase, by another path.** The
near heading was a parse error, and the dry run lists a design whose
section errs among those to read whole. It now parses as no section, which
the dry run lists the same way, with the reason "no `## Rule changes`
section". `settle.py` is unchanged, and no case was seen red for the
clause, since the listing is the same and only its reason moved.

**Departure e of phase 2 is closed.** `rule_changes.Parsed` gains
`unread`. `rule_changes_read` and `rule_changes_of` take a `notices` list,
the shape `originals_of` takes since `321c8e58`, and `main` passes its
list at both calls: the judged work items' designs and the designs the
branch edits. So a line is named only in a design the arm reads; a design
git does not carry, or one another pull request's squash carried, is not
read and names nothing. The line prints as `not read: <why>` through the
shared `annotate`, a notice annotation in CI.

**`seal rules` reads the one shape and names the rest.** `check_lines`
returns only lines that are `check: ` after their leading spaces;
`unread_lines` returns the other lines `NEAR` matches. `--check` prints
each as `seal rules: not read: path:line: heading: why` at exit 0, and
the summary counts read lines only. `seal rules <doc>` prints it as
`not read, line N: why`, and a section holding only such a line holds no
check line. A line that is a heading and opens like a check line stands
under itself as its heading, as it did before. #1125's decision is one
bullet of *A rule has one shape*, a limit with no case: nothing reads the
line below a check line. `test_every_check_line_in_the_tree_holds` planted
`Enforced by:` to make each rule-file glob exit 1; that line is now named
at exit 0, so the plant is an exact check line naming a gone file.
`seal rules --check` over this tree names no line (executed).

**`seal pact` grades the exact header alone.** `first_table` loses its
`key` argument. `near_headers` names each unfenced header whose cells
`header_key` folds to the anchor header's and that is not it, printed
`NOT READ <signer> <frame>:<line> — <why>`, in no exit class. The case
for a second lower-case table among `test_refuses_an_anchor_row_nobody_reads`'s
rows went, because that table is now named and not refused; its place is
`test_grades_the_exact_table_and_names_a_near_one_beside_it`.
`docs/the-pact.md` *The pact anchor* still states the normalisation, as
`frame/plan.md` A15 keeps it until the settle.

**Seen red.** Each new or rewritten case was run against the tree before
its code changed (executed). `rule_changes.py`: the near-heading cases
failed with no `unread` on the result, and the three chain_check cases on
the refusal at exit 1. `unverified_check.py`: the four closing-word rows
on their refusal, the old-line section case on the old refusal text, the
block cases on the missing `unread_block`, and the three block rows of
`test_rule_changes.py` on the refusal naming the block. `rules.py`: the
twelve near-line rows and the beside case on exit 1, the render case on
the line printed as refused. `pact_check.py`: the nine near-header rows on
the row graded and counted, the lower-case row on its refusal at exit 2,
and the beside case on the second-header refusal. Two boundary cases, a
prose line that does not open like the block and a line that does not open
like a check line, pass on both trees by design, and their mutants below
turn them red.

**Mutation.** `seal mutate` over each unit after its commit, each scope
boundary of a naming given a mutant (executed):

- `rule_changes.py#parse`: naming the exact heading too, naming level 2
  only, reading headings inside fences, and naming a heading with other
  letters. The first batch's version of the last was mistyped (`'rules'`
  is no heading's letters) and survived as a mutant that changed nothing;
  rewritten as `'ruleschanges'`, it was red. Then the block line not
  appended to `unread`: red.
- `chain_check.py`: the judged call without `notices`, the edited call
  without it, and the notices sent to the refusals: 3 red.
- `unverified_check.py`: `nothing_block` refusing the near line again,
  `unread_block` naming any first line, `unread_block` naming the block,
  the refusal without its naming, and `closed` read through case and
  punctuation: 5 red.
- `rules.py`: `unread_lines` naming exact lines, naming fenced lines, the
  named lines sent to the refusals, `check_lines` reading near lines, and
  `render` dropping its line: 5 red. The exact-line mutant survived the
  first draft, because the accepts case read its output with `in`; the
  case was tightened to the whole output before the commit was amended.
  `render`'s branch for a line that is both a heading and a near check
  line had no case after the run of the boundary set; `9701ff87` adds
  `test_a_heading_that_opens_like_a_check_line_is_printed_under_itself`,
  and the branch removed turned it red.
- `pact_check.py`: naming the exact header, reading fenced headers, naming
  any three-cell header, grading under a near header, dropping the
  `NOT READ` line, and putting it in exit class 2: 6 red.

**The boundary set ran green.** One `bin/test -n auto` over 67 modules at
`aa257233`: the plan's five, and every module under `tests/` that names
one of the six changed paths, imports them, or globs `skills/*/SKILL.md`,
a `scripts/` directory or the rule files. 3805 passed and 9 skipped, exit
0 (executed). The list was built by `git grep` over `tests/` and is not a
census: a module that reaches a changed path another way is the broad
gate's.

**Tests changed in place.** `test_rule_changes.py`'s near-heading case
and the three block rows; `test_unverified_check.py`'s closing-word rows,
which moved from the refusal case to the open-row case, and
`Test_nothing_block`; `test_rules.py`'s six near-spelling rows and the
block-markup case, merged into one naming case, the render case and the
tree case's plant; `test_pact_check.py`'s header-normalisation case and
the lower-case `UNDECLARED` case, both rewritten to the naming.

**What the next phases meet.** `docs/the-review-record.md`,
`docs/the-pact.md` and `docs/the-record-layout.md` state the refusals this
phase removed, until the settle applies `## Rule changes`.
`skills/implement/SKILL.md` *4. The closing memo* says any other spelling
of the heading, the header row or the block "fails the check", which still
holds: a near block leaves a section with neither, and that section is
refused.

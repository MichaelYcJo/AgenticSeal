# 1792619407-the-replay-scaffold-and-reader-misread-rounds — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 41cc627b |

## What this phase was asked

Build phase 3 as `plan.md` states it, after the reframe at 9fe7a57b that
round 3's second regression on the reader sent to the framer. Where
`chain_check.py#unclosed` refuses a record, `finding_rows` counts one empty
false row per raw `FINDING_LEVEL` heading line, fenced and commented ones
included, and no `truth-` grader reading that record passes. Every other
record keeps phase 1's split, and `unhidden` goes. The work is test-first:
S5a to S5c seen red at 9f8fe13b, the three cases at `:1093`, `:1136` and
`:1148` rewritten in place, and round 3's probe as a case. The three
mutations the plan names go red. The `finding_rows` docstring and the
changelog sentence on such a record are rewritten in place, and `git grep -n
unhidden -- ':!seal'` is empty.

## What this phase found

**The reader of a refused record is now one count.** `finding_rows` returns,
where `unclosed` refuses the text, one empty string for each line of
`reader.gfm_lines(text)` whose `reader.heading_level` is
`chain_check.py#FINDING_LEVEL`. An empty row matches no `truth-` pattern, so
`grade` finds no truth in such a run and `side_numbers` needed no branch of
its own. `unhidden` is removed, and no line of the tree outside `seal/`
names it (executed: `git grep -n unhidden -- ':!seal'` exit 1).

**Seen red.** `noninferiority.py` at 9e0db60c is the same file as at
9f8fe13b (executed: `git diff --quiet 9f8fe13b HEAD --
evals/scripts/noninferiority.py` exit 0). Against it, `bin/test
tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist -k
"never_closes or cannot_read or closed_fence or opener_inside"` exited 1
with 7 failed:

- S5a: the case at `:1093` and the three shapes at `:1136` each gave the
  three `location:` rows, not three empty ones.
- S5a: round 3's probe record gave one row, `location: src/b.py:1`, where
  the warden's own probe record gave two; the record here has a fenced fix
  in each later finding.
- S5b: `truth-1` passed one run where it should pass none.
- S5c: three rows came back where four empty ones are owed.

The case at `:1148`, with nested and repeated openers, was rewritten in
place to three empty rows. Its old reading was `unhidden`'s, which this
phase removes.

**Mutation.** Four runs of `bin/mutation-check`, each exit 0 `red`:

- the floor dropped (`if False:` for the `unclosed` branch);
- the count taken over `readable`'s lines, which `S5c`'s fenced `### ` line
  is not one of;
- a row holding the heading line's text;
- a row of a refused record holding the record's `location:` lines, which
  is the third mutation the plan names. The run before it put the heading
  text in the row, which is not what the plan names, so it was run again
  as named.

**What it costs, as plan row U4 accepts it.** A run whose record leaves a
region open loses every find and counts every heading line false. A
warden's step 7 runs the check, which refuses such a record, so the
penalty falls only on a run that handed back a record production refuses.

**Phase boundary, executed with this record staged.** `bin/test
tests/test_a_rewritten_definition_proved_non_inferior.py -q` exited 0. The
touched and meta modules named in the spawn ran in one `bin/test` call: 423
passed, 2 skipped, exit 0. `bin/rules --check`, `bin/settle --released-at
HEAD` and `bin/unverified-check seal/specs/` each exited 0. `ruff check` and
`ruff format --check` exited 0 on each touched `.py` file, one file per
call.

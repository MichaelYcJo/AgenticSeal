# 1792619407-the-replay-scaffold-and-reader-misread-rounds — review round 3

target: 8c7ba12d, fixes 4875eb7b..8c7ba12d

## Findings

### 1. A comment opener inside a closed fence still hides a later finding, because the reading again starts inside the fence

severity: should
location: `evals/scripts/noninferiority.py:298-312`, `tests/test_a_rewritten_definition_proved_non_inferior.py:1148`
evidence: executed `python3 test_tmp_986_round3.py`
verdict: deferred the frame
regression: round-2#1

The unit is `noninferiority.py#unhidden`, which 729cea97 added. `spec.md` scope item 1 and `plan.md` row R3 say
that a finding in a shape the check refuses is still a row. The fix reads the lines after the first opener
`chain_check.py#unclosed` reports again on their own. The defect comes from round 2's fix block, which assumed every
opener `unclosed` reports is a real one.

The shared reader scans comments before fences (`unclosed`'s docstring says so). So an HTML comment opener inside a
fenced fix block with no closer of its own opens a comment that swallows the fence's closer. Quoting the head of a template,
which opens with a comment, makes exactly that block. `unclosed` then reports two openers: the comment, and the
fence whose closer it hid. `unhidden` takes the lower line, the fence's, and reads the lines after it on their own.
That reading starts inside the fence, so the fence's closer now opens a fence. It hides the next finding's heading
up to that finding's own fix block.

The probe wrote three findings. Finding 1's fix was a fenced block holding a lone HTML comment opener, and findings 2 and 3 each
had a fenced fix. `finding_rows` gave 2 rows, and the check read 0 findings and refused the record. With no fence
after finding 1 it gave 3 rows, and with the opener in prose it gave 3 rows. Before 729cea97, the raw-line split
gave 3 rows for this record. Every shape the new cases at lines 1136 and 1148 hold still gives its three rows
(executed: 8 cases passed).

This is the third reading of an unclosed region in three rounds, and each has missed a shape. The fix this time
does not try a fourth reading. It sets a floor that fails closed. Where `unclosed` refuses the record, a side
counts at least as many rows as the raw text has `### ` heading lines. Fenced ones count too, which errs toward
more false rows, the direction a record the check refuses should take. `unhidden` stays as it is and still gives
the rows that truths are graded on. A case beside line 1148 holds this probe's record and asserts three rows. The
snippet assumes `FINDING_LEVEL` keeps its name in `chain_check.py` (`skills/code-review/scripts/chain_check.py:504`).

```python
    rows = [
        "\n".join(
            line
            for line in lines[first:stop]
            if check.label_of(line) == check.LOCATION_ROW
        )
        for first, stop in spans
    ]
    # Where a region never closes, the check refuses the record and no reading
    # of its lines is certain to find every finding, so the rows are at least
    # as many as the raw text's finding headings. A fenced heading counts too,
    # which errs toward more false rows, never fewer.
    if check.unclosed(reader, text, ""):
        heads = sum(
            1
            for line in reader.gfm_lines(text)
            if reader.heading_level(line) == check.FINDING_LEVEL
        )
        rows += [""] * (heads - len(rows))
    return rows
```

answer: The unit already had a regression routed to a fix pass in this run (round-2#1, from round-1#2), so by `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame* this second one goes to the framer. Three readings of an open region in three rounds each missed a shape; the framer decides what the reader owes where the check refuses a record, rather than a fourth reading.

## Confirmations

confirms: round-2#2
What the remote removal closes and what it leaves is stated once, in `seed_defects.py`'s module docstring at lines
16 to 18: a `git fetch` with no URL has no remote to fetch from, and a fetch naming the URL the tree holds still
reaches the shipped code. The `scaffold` docstring, the S10 case and the overview row point at it. The changelog
says only that a bare `git fetch` fetches nothing, which is true. `git grep` over the tree outside the round records
finds no text left saying no fetch brings the shipped code back (executed). In each of the four clones this round
built, `git remote` prints nothing (executed).

confirms: none
The CRLF change to `seed_defects.py#MUTATE` (`evals/scripts/seed_defects.py:272-283`, e8bea30b) is new code, so
round 2 has nothing to confirm about it; this entry reviews it. The probe ran the scaffold's mutation script on six
line-end shapes: LF, CRLF, a mixed file with the seed line CRLF, a mixed file with the seed line LF, a file with no
final newline, and a seed line whose content itself ends in a carriage return before its CRLF. The first five exited
0 and changed only the seeded text, with each line's end kept. The sixth exited 1 on the assertion, naming the line
(executed). That last shape fails closed and loudly. The generator reads source through `replay_targets.py#git`,
`text=True` with universal newlines, which would also read that carriage return as a line break, so the seed's line
number is already off for such a file before the scaffold runs (read: `evals/scripts/replay_targets.py:90-99`). A
lone carriage return in a Python source is a limit no shipped commit meets, and it is not raised. The two
parametrised CRLF cases and the two new reader cases passed on macOS (executed). Whether the Windows leg passes is in
`## Not judged`.

confirms: none
All four scaffolds regenerated at 8c7ba12d exited 0 in empty directories. Each clone keeps no remote, holds two refs,
shows HEAD with the original committer, and has no carriage return in `git diff HEAD^ HEAD`. Each `--stat` matches
phase 2's table of the Q5 residue (executed).

Carried from round 2 rather than re-established: the committer-date match and the S10 object checks of the scaffold
runs. Neither the amend line nor the cleanup lines changed in this diff. Re-derived: both verdicts above, the
`MUTATE` shapes and the reader's rows.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the CRLF fix and round 1 finding 1's `as_uri()` fix pass on the Windows leg | `tests/test_a_rewritten_definition_proved_non_inferior.py:2658` | the orchestrator, from `tests` run 39692693904 |
| The full suite, the repository-wide lint and the typecheck at 8c7ba12d, labelled `unverified` here | the branch | the orchestrator, at its one broad run |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_986_round3.py` in the scratch clone at 8c7ba12d | Exit 0. A: a lone comment opener in finding 1's closed fence, with fences in findings 2 and 3, gave 2 rows, 0 check findings, and `unclosed` at lines 14 and 13; with no later fence it gave 3, and with the opener in prose 3. B: `MUTATE` exited 0 and changed only the seed for LF, CRLF, both mixed shapes and no final newline, and exited 1 on its assertion for a content carriage return before CRLF |
| `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist -k "closed_fence_still_hides or never_close_nested or ends_with_crlf or seeded_scaffold_leaves or never_closes_hides"` | 8 passed, 120 deselected, exit 0 |
| `sh <case>/scaffold.sh` for the four seeded cases, each in an empty scratch directory | Exit 0 each; no remote, two refs, the original committer, no carriage return in `git diff HEAD^ HEAD`, and `--stat` as phase 2 records it |

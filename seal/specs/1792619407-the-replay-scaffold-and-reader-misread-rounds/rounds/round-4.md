# 1792619407-the-replay-scaffold-and-reader-misread-rounds — review round 4

target: ad78bfb6, fixes 8c7ba12d..ad78bfb6

## Findings

### 1. A record with two Findings sections still counts no false finding, though the reframe's rule says a refused record errs toward more

severity: should
location: `evals/scripts/noninferiority.py:298-330`, `seal/specs/1792619407-the-replay-scaffold-and-reader-misread-rounds/spec.md:240-241`, `seal/specs/1792619407-the-replay-scaffold-and-reader-misread-rounds/plan.md:106`
evidence: executed `python3 test_tmp_986_round4.py`
verdict: open

The reframe at 9fe7a57b sets a rule for a record the check cannot read. `spec.md` scope item 1 says the harness reads
no finding from such a record and counts one false row per raw finding heading. It adds that "the count errs toward
more false rows and fewer finds, never the other way, and it follows the check". Plan row U3 rejects giving such a
record no rows, because "a warden that leaves one comment open lowers its false count for that run to zero. That
fails open on the number rule 2 reads". Phase 3 applies the rule only where `chain_check.py#unclosed` refuses.
`finding_spans` has refusals of its own, which `finding_rows` discards as `_error` at line 322: no `## Findings`
section, and a second one. A record refused either way still gives no rows. `spec.md:240-241` and plan row R3 state
this as the check's own limit. That decision came before the reframe. U3's reason for rejecting the empty count
applies to it word for word.

The probe wrote three findings with a second `## Findings` heading before finding 2. `finding_rows` gave 0 rows,
and the check read 0 findings and refused the record for the second section. So a run that wrote three false
findings counts none. The `shape-findings` grader does not catch it. Its pattern needs one `## Findings` section
holding a `### <n>.` heading and a `verdict:` line, and the first section has both. R3 says the same. With the
heading misspelt as `## Findings (3)`, the record also gave 0 rows. There `shape-findings` fails the run, which pass
rule 3 reads, so that shape is caught elsewhere, but the count is still the empty one U3 rejects.

The fix extends the floor phase 3 built to every refusal of the split, so that the frame states one rule: a record
the check cannot split gives one empty, false row per raw finding heading. The framer rewrites `spec.md:240-241`
and plan row R3 in place to say so, since both state the limit this removes. Cases beside S5c hold both shapes. The
snippet keeps phase 3's branch and adds the split's refusal.

```python
    check, reader = rt.record_reader()
    lines = reader.readable(text)
    _section, spans, error = check.finding_spans(reader, lines)
    # A record the check cannot read or cannot split, a region that never
    # closes, no `## Findings` section or two, reads as no finding in
    # production: it gives one empty, false row per raw finding heading.
    if error or check.unclosed(reader, text, ""):
        return [
            ""
            for line in reader.gfm_lines(text)
            if reader.heading_level(line) == check.FINDING_LEVEL
        ]
```

answer:

## Confirmations

confirms: none
The redesign closes the reader shapes of rounds 1, 2 and 3. Round 3's finding was closed `deferred the frame` and
owes this round nothing, so it is named here as a claim, not by its reference. Executed: the probe's round 3 record
has a lone comment opener inside finding 1's closed fence and fenced fixes in findings 2 and 3. At 8c7ba12d it gave
2 rows. Here it gives 3 rows, all empty, and the check refuses it for both openers. The rewritten S5a cases at
`tests/test_a_rewritten_definition_proved_non_inferior.py:1093`, `:1136` and `:1148` hold round 1's and round 2's
shapes as three empty rows, and the case at `:1160` holds round 3's. Eleven reader cases passed under `bin/test`
(executed). `git grep -n unhidden -- ':!seal'` exits 1 (executed).

confirms: none
No run of a record the check accepts loses a truth. `finding_rows` still splits `readable`'s lines by
`finding_spans` wherever `unclosed` refuses nothing (`evals/scripts/noninferiority.py:298-330`, read), and S1 to S5
pin that reading. A refused record finds no truth by plan row U4's choice, as S5b at `:1112` pins. An empty row
matches no `^location:` pattern, so `grade` needs no branch of its own (read). Two shapes that look as though they
might trip `unclosed` do not: an HTML comment opener in inline code on one line, and round 1's line 51 written out
in full. Each gave 3 rows and 3 check findings with no refusal (executed).

confirms: none
The rewritten cases pin what plan row 3 says. S5a covers the three earlier shapes and round 3's record, S5b covers
a truth's line outside every region with the eval's `passed` recorded true, and S5c at `:1176` counts a fenced `###`
line as a fourth row. Phase 3's record shows each red against 9f8fe13b, and the four mutations the plan names went
red (read: `phases/phase-3.md`).

Carried from rounds 2 and 3 rather than re-established: the scaffold, the mask and the CRLF line check, none of which
this diff touches.

## Not judged

| What | Location | Who answers |
|---|---|---|
| A fenced fix that never closes but is closed by the next finding's fence opener hides that next finding from both the check and the harness, and the check refuses nothing: 2 rows and 2 check findings of 3 written (executed). The harness counts what the check counts, so this is the check's own reader and outside this diff, as round 1 left it | `skills/verify/scripts/unverified_check.py:417` | the repository owner |
| `tests` run 39693779473 at ad78bfb6 | the branch | the orchestrator |
| The full suite, the repository-wide lint and the typecheck at ad78bfb6, labelled `unverified` here | the branch | the orchestrator, at its one broad run |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_986_round4.py` in the scratch clone at ad78bfb6 | Exit 0. Round 3's record gave 3 empty rows, refused by the check for both openers. Two `## Findings` sections gave 0 rows and a misspelt heading 0 rows, each refused by the check with 0 findings read. A misnested fence gave 2 rows and 2 findings with no refusal. Inline code holding a comment opener and round 1's line 51 each gave 3 rows and 3 findings with no refusal |
| `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist -k "never_closes or cannot_read or closed_fence or opener_inside or never_close_nested or shape_the_check_refuses or fenced_fix or checks_split"` | 11 passed, 120 deselected, exit 0 |

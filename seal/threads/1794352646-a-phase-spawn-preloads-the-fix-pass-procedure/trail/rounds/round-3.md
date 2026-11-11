# Review round 3: 1794352646-a-phase-spawn-preloads-the-fix-pass-procedure

```seal
target: 05efbd381, fixes 4adad4f19..05efbd381
```

This is the verifying round over round 2's fold and fix pass. The range holds
four commits:

- `dfbde8092` commits round 2's record.
- `b8866b2e1` is the fold of round 2's finding 1 into `frame/design.md` and
  `frame/plan.md`, with the orchestrator's route row.
- `39be4b024` is the fix pass.
- `05efbd381` commits the close block.

The code reviewed is the fix diff: step 9 of `agents/crafter.md` and the case
in `tests/text/test_a_moved_rule_leaves_its_definition.py`.

`routing.md`, the three frame files, `gaps.md`, `changelog.md` and `pr.md`
were each read whole at `05efbd381`. No `pr.<lang>.md` stands, and none is
owed. `routing.md`, `frame/questions.md`, `gaps.md` and `pr.md` are
unchanged in the range (executed, `git diff --quiet 4adad4f19 05efbd381`
over the four, exit 0).

Two facts were carried from rounds 1 and 2 without being established again:

- the census of the old spellings outside `seal/threads/`, since no file in
  the range adds one;
- that `release_report.py#preloads` is the preload's measure, which
  *Probes* row 1 re-ran.

## Findings

No finding.

## Confirmations

```seal
confirms: round-2#1
```
What holds: step 9 now reads "in place of step 7's run and of the phase record
steps 5 and 8 write; steps 5 and 6 otherwise hold for each fix"
(`agents/crafter.md:62-64`). Step 5's census of a renamed or moved unit goes
into `trail/phases/phase-N.md` (`:47-49`). That is the phase record the
sentence replaces, and "otherwise" keeps that write out of what still holds.
So the sentence no longer conflicts with `skills/implement/fix-pass.md:53`,
"writes no phase record". Step 5's read against the verify table, its
test-first build and step 6's `seal mutate` run still hold for each fix, so
round 1's finding 1 stays answered. The scope matches `7c2801838`'s "instead
of steps 5 to 8's record", with step 7's run replaced as before.

The sentence is `frame/design.md:30` (*Scope* item 2) word for word. It
differs from round 2's paste-ready text by "phase" and "otherwise". Both
words narrow it the way the frame's grounds say. Step 8's other write,
`gaps.md`, is made only in the first phase, and the crafter's *Job*
paragraph (`agents/crafter.md:21-22`) keeps a fix pass's `gaps.md` rows. The
fix pass said in `answer:` that it wrote the frame's sentence rather than
the paste-ready text, as `skills/implement/fix-pass.md:39-41` asks.

The case pins the sentence at
`tests/text/test_a_moved_rule_leaves_its_definition.py:616-623`, and its
docstring (`:529-537`) says the same. The close also claims red runs. The
first is against round 1's step 9. Under `seal mutate`, two more:
"and step 8's record" put back, and "otherwise" removed. Those were read,
not re-run. The assertion is a containment check of the whole sentence, so
each change fails it.

Read, and executed for the preload. `changelog.md:3` quotes the sentence and
gives 33,807 B, which *Probes* row 1 reads at `05efbd381`. The drop is
`35,883 - 33,807 = 2,076`, so "about 2.1 KB" still holds in the process row
and in `frame/plan.md` rows 1 and 4.

What matched: the fold agrees with the fix commit. *Scope* item 2
(`frame/design.md:30`), S1's estimate of 33,807 B (`:51`), S3 (`:53`), S5's
grounds (`:55`) and the note under D1 (`:72`) each state the new sentence or
its effect. Row 11 of *Alternatives considered* (`frame/plan.md:29`) now
quotes "steps 5 to 8's record" as the old text read, and row 12 (`:30`)
rejects round 1's wording on round 2's finding. The route row
(`frame/plan.md:65`) cites `skills/code-review/orchestration.md` *A
regression is routed by comparing the fix with the frame*, which is the
heading at `:218`. The cited-section check passes (*Probes* row 2). Read.

The row of round 1's fold in *Judgments of the run* (`frame/plan.md:63`)
still names step 9 as round 1's fix wrote it. It records what that fold
did on its date, and the rows below it record the change after it. It
states no present that the target contradicts, so it opens no finding.

What matched: `pr.md` is unchanged in the range, and its six quotes still
stand word for word at the coordinates they name in `frame/plan.md`. Rows 1,
2 and 7 of *Alternatives considered* and the first two rows of *Judgments of
the run* did not change. The new rows 12 and 6 do not take quote 4's
wording, so its coordinate still finds one row. Read.

Nothing this round found is open. The next step is the orchestrator's
broad run, then the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the work item's HEAD; the suite is `unverified` here | `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/gaps.md:8` | the orchestrator, by `seal gate --record` after the rounds settle |
| Whether a fix pass, a resumed implementer among them, opens `skills/implement/fix-pass.md` at step 9 (S3) | `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/design.md:53` | the orchestrator, from the transcript of the first fix pass after the merge |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_preload.py <repository root>`, run from `<scratchpad>/<work-item-id>/round-3/`. It loads `.github/scripts/release_report.py` by path and prints `preloads(root, meter())` | `{'crafter': 33807, 'framer': 39806, 'proofer': 33254, 'sealer': 33962, 'tracer': 25402}`, exit 0. Run once; the file and its directory were deleted |
| `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_no_passage_is_pasted_into_a_second_file.py -q -p no:xdist` | 309 passed, 2 warnings, exit 0 |

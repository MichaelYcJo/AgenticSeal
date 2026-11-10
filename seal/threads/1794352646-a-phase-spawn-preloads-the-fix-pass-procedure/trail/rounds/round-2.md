# Review round 2: 1794352646-a-phase-spawn-preloads-the-fix-pass-procedure

```seal
target: 4adad4f19, fixes bbb765088..4adad4f19
```

This is the verifying round over round 1's fold and fix pass. The range holds
`ca723b9e2`, which commits round 1's record, and `447524fcf`, the fold of
both findings into `frame/design.md` and `frame/plan.md`. It also holds
`a53080e77`, the fix pass, and `4adad4f19`, the close blocks. The code
reviewed is the fix diff: `agents/crafter.md` step 9 and the case in
`tests/text/test_a_moved_rule_leaves_its_definition.py`.

`routing.md`, the three frame files, `gaps.md`, `changelog.md` and `pr.md`
were each read whole at `4adad4f19`. No `pr.<lang>.md` stands and none is
owed. `routing.md`, `frame/questions.md` and `pr.md` are unchanged in the
range (executed, `git diff --quiet bbb765088 4adad4f19 -- routing.md
frame/questions.md pr.md`, exit 0).

Two things were carried from round 1 and not established again. The first
is the census of the old spellings outside `seal/threads/`: no file in the
fix range adds one. The second is that the cited-section check resolves
bold leads (`tests/behaviour/test_a_cited_section_stands_in_its_file.py:170-190`).
Its run passed again here (*Probes* row 2).

## Findings

### 1. Step 9 now keeps step 5's write into the phase record for a fix pass, which writes no phase record

```seal
severity: should
location: `agents/crafter.md:62-63`, `tests/text/test_a_moved_rule_leaves_its_definition.py:530-531`, `tests/text/test_a_moved_rule_leaves_its_definition.py:616-618`, `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/changelog.md:3`, `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/design.md:30`
evidence: read `agents/crafter.md:42-63` at `4adad4f19`, `skills/implement/fix-pass.md:53`, `git show 7c2801838:agents/crafter.md` lines 62-66, `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/plan.md:29`
regression: round-1#1
```

Why it matters: a fix pass that renames or moves a unit gets two
instructions that cannot both hold. It cannot know where the census goes.

The unit is step 9 of `agents/crafter.md` as `a53080e77` rewrote it. The
frame (`frame/design.md:30`, *Scope* item 2 as `447524fcf` folded it) gives
the sentence word for word, and the fix applied it as given. The defect came
from round 1's paste-ready fix, which named step 7's run and step 8's record
but not step 5's write into the record.

- **Step 9 now** reads "in place of step 7's run and step 8's record; steps 5
  and 6 hold for each fix" (`agents/crafter.md:62-63`).
- **Step 5** ends: "the existing cases that prove it at the new name or path,
  and the census that table's row asks for, go into
  `trail/phases/phase-N.md`'s `## What this phase found`"
  (`agents/crafter.md:47-49`). Step 9 holds step 5 for each fix, so this
  write holds too.
- **`skills/implement/fix-pass.md:53`** says "A fix pass appends close
  blocks and writes no phase record."
- **Step 9 at `7c2801838`** read "append each close block instead of steps 5
  to 8's record". That covered step 5's write as well as step 8's, so the
  old text held no such conflict. `frame/plan.md:29` (*Alternatives
  considered* row 11) says step 9 at `7c2801838` "replaced step 7's run and
  step 8's record only". That reading of the old text drops step 5's write.

The fix names the record that steps 5 and 8 write, as the old text did:

```markdown
9. In a fix pass, open `skills/implement/fix-pass.md` and follow it in place
   of step 7's run and of the record steps 5 and 8 write; steps 5 and 6 hold
   for each fix.
```

The snippet covers `agents/crafter.md` alone. The fix pass also owes:

- the case's assertion at `:616-618` and its docstring at `:530-531`;
- `changelog.md:3`, both the quoted sentence and the preload figure, which
  is measured again because step 9 grows.

`frame/design.md:30` (*Scope* item 2) and `frame/plan.md:29` (row 11) are
frame statements of the same fact, for the orchestrator to fold.

## Confirmations

```seal
confirms: round-1#1
```
What holds: a fix pass is again bound by step 5's read against the verify
table and its test-first build, and by step 6's `seal mutate` run.
`agents/crafter.md:62-63` keeps steps 5 and 6 "for each fix", and the case
pins the sentence at
`tests/text/test_a_moved_rule_leaves_its_definition.py:615-622`. Its
docstring (`:529-536`) and `changelog.md:3` say the same, and so does the
fold in `frame/design.md:30` and `:72`. The close's claim that the
re-pointed assertion was seen red before the edit and under `seal mutate` was
read, not re-run: the assertion is a containment check of the whole sentence
over the *Order of work* section, so removing "steps 5 and 6 hold for each
fix" fails it. The preload of 33,770 B in `changelog.md:3` and the close
holds at `4adad4f19` (executed, *Probes* row 1). `35,883 - 33,770 = 2,113`,
so the process row's "about 2.1 KB" and `frame/plan.md` rows 1 and 4 hold.
Read and executed. The step-5 part this fix left uncovered is finding 1.

```seal
confirms: round-1#2
```
What holds: `gaps.md:12` and `frame/design.md:44` now say that `frame/plan.md`
*Judgments of the run* judges the sentence at
`docs/running/the-agent-set.md:93` takes no issue. That matches the row at
`frame/plan.md:59`. No sentence of the work item that states the present
still says the orchestrator files it. Executed: `git grep -n -i "files it\|to
file"` over the work item's directory at `4adad4f19`. It finds round 1's
record and `frame/plan.md:63`, the fold's row, which quotes the old bullet as
what it corrected. Its only other hit, "the files its" at `frame/plan.md:7`,
is a different phrase.

What matched: `pr.md`'s six quotes still stand word for word at the
coordinates they name. The fold changed rows 1 and 4 of *Alternatives
considered* only in their failure cells, from 2.2 KB to 2.1 KB, and
`pr.md` quotes row 1's verdict cell, which did not change. The fold added
two rows to *Judgments of the run*. The second of them names
`docs/running/the-agent-set.md:93` too. The text of quote 4 stands only in
the first row, so its coordinate still finds one row. Quote 6's "what a fix
pass does is unchanged" now holds, by round-1#1 above. Read.

What matched: the fold's new statements agree with the fix commit. These are
*Scope* item 2 (`frame/design.md:30`), the note under D1 (`:72`), S1's
estimate of 33,770 B (`:51`), S3's added clause (`:53`), and the
*Alternatives considered* and *Judgments of the run* rows the fold added
(`frame/plan.md:29`, `:62-63`). S5's grounds for no second smoke run say the
fix changes only what a fix pass does, and none of the five cases is a fix
pass. Under the frame's G11 that judgment holds. Finding 1 changes only the
record clause, so it does not move S5. Read.

The docstring of the case breaks a line early at
`tests/text/test_a_moved_rule_leaves_its_definition.py:535`, where "range
and" stands alone. That reads badly and holds no fact, so it opens no
finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the work item's HEAD; the suite is `unverified` here | `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/gaps.md:8` | the orchestrator, by `seal gate --record` after the rounds settle |
| Whether a fix pass, a resumed implementer among them, opens `skills/implement/fix-pass.md` at step 9 (S3) | `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/design.md:53` | the orchestrator, from the transcript of the first fix pass after the merge |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_preload.py <repository root>`, run from `<scratchpad>/<work-item-id>/round-2/`. It loads `.github/scripts/release_report.py` by path and prints `preloads(root, meter())` | `{'crafter': 33770, 'framer': 39806, 'proofer': 33254, 'sealer': 33962, 'tracer': 25402}`, exit 0. Run once; the file and its directory were deleted |
| `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_no_passage_is_pasted_into_a_second_file.py -q -p no:xdist` | 309 passed, 2 warnings, exit 0 |

# Review round 3: 1794362365-the-definitions-restate-the-contract

```seal
target: e3c9c4d60, fixes 0e677ac77..e3c9c4d60
```

This round verifies round 2's finding 1 and reads every commit after round
2's record, `0e677ac77..e3c9c4d60`: `85a918004`, `3024a14d3`, `efe66297c`,
`0b40627b2` and `e3c9c4d60`. The base is `release/v0.37.3` at
`9c6907942`. It ran in a `git clone --no-local` at `e3c9c4d60` under
`<scratchpad>/1794362365-the-definitions-restate-the-contract/round-3/clone`.
The work item's records were each read whole at `e3c9c4d60`:
`routing.md`, the three frame files, `gaps.md`, `changelog.md`, `pr.md`
and `trail/phases/phase-1.md`. No `pr.<lang>.md` stands or is owed.

Carried from rounds 1 and 2 and not re-established: where each statement
of the scratch rule stands, and the census probe's method, re-run below
from round 1's `## Probes` row. The owner's comment on #1503 was read in
round 2 and is quoted here from that reading: the orchestrator removes the
work item's scratch directory "once, after the pull request opens".

## Findings

### 1. The repair judgment gives the owner a reason the owner did not write, and the tree now departs from the issue's "once"

```seal
severity: should
location: `seal/threads/1794362365-the-definitions-restate-the-contract/frame/plan.md:80`
evidence: read `seal/threads/1794362365-the-definitions-restate-the-contract/frame/plan.md:74`, `seal/threads/1794362365-the-definitions-restate-the-contract/frame/plan.md:80`, `skills/implement/orchestration.md:43-53`, `seal/threads/1794362365-the-definitions-restate-the-contract/trail/rounds/round-2.md:23-31`
```

Why it matters: the owner's amendment of #1503 says the orchestrator
removes the work item's scratch directory "once, after the pull request
opens". Its reason is that nothing clears a session's scratch when the
session ends, and that a literal path runs with no prompt (round 2's
reading of `gh issue view 1503 --comments`). `frame/plan.md:74` records
that decision as written. The row at `:80` extends it: the removal "again
after each later repair". Its grounds say "The owner's decision is that no
work item's scratch outlives its run and no removal holds a run for a
person". The owner wrote the second half and not the first. The first is
the orchestrator's reading of the owner's reason, set down as the owner's
words.

The extension itself is a sound reading of that reason, and this round
does not find it wrong. The defect is where it is recorded. The sealer
reads every party's account against the issue, and the issue as amended
says "once". `skills/implement/orchestration.md:50-53` and both READMEs now
say "again after each repair". A row whose grounds put the step in the
owner's mouth hides that the step is the orchestrator's, and the sealer
cannot tell the two apart from the record. The orchestrator's judgment is
allowed here, under `skills/core/SKILL.md` *Asking a person is the most
expensive step*, when the row says it is the orchestrator's.

The fix is the row's grounds, which the orchestrator writes. Whether the
owner adds one line to the issue before the sealer runs is a person's
choice, so it stands under *Not judged* and is no part of the fix.

```markdown
frame/plan.md:80, Grounds cell, in place of "The owner's decision is that
no work item's scratch outlives its run and no removal holds a run for a
person, and a second removal with the same literal path keeps both":
The owner's decision says "once"; its reason is that nothing clears a
session's scratch when the session ends, and that a literal path holds no
run for a person. The orchestrator judges that the reason covers a
repair's clones too, and a second removal with the same literal path
keeps both of the reason's conditions. The repeat is the orchestrator's
judgment, not the owner's words
```

### 2. The rule change's `to` restates the README's sentence on the orchestrator's removal

```seal
severity: should
location: `seal/threads/1794362365-the-definitions-restate-the-contract/frame/design.md:232`
evidence: executed `python3 skills/code-review/scripts/chain_check.py --baseline 9c6907942 --root <the branch worktree> --worktree`; read `seal/threads/1794362365-the-definitions-restate-the-contract/frame/design.md:228-232`, `README.md:374-380`, `skills/implement/orchestration.md:43-53`
```

Why it matters: the chain check prints at `frame/design.md:232` "this `to`
repeats a passage of `README.md`: 5 of its runs of 15 words stand there,
one of them "the orchestrator removes the work item's directory once the
pull request is open, and again"". All five runs come from the `to`'s last
sentence, whose 19 words match `README.md:378-380`. After the settle the
fact would stand three times, in `skills/implement/orchestration.md`
step 2, in the README and in `docs/running/the-agent-set.md`, and the next
change to it must find all three. This round already had to: the repeat
after a repair was written into each of them in `85a918004` and
`3024a14d3`. The orchestrator judged that the operation is meant to state
the same fact as the README. The fact is the README's to state for a
person and the skill's for the orchestrator. The policy paragraph needs
only to say where the step stands and why it is there.

The fix is the frame's, for the orchestrator to fold. It drops the copy
and keeps the reason the README does not give.

```markdown
frame/design.md:232, the `to`'s last sentence, in place of "The
orchestrator removes the work item's directory once the pull request is
open, and again after each later repair it pushes to that pull request,
in one command whose path is written out in full, because nothing clears
a session's scratch when the session ends.":
The one removal is the orchestrator's, in
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket*, because nothing clears a session's scratch when the session ends.
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: `test_the_orchestrators_one_removal_names_the_work_items_directory`
(`tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:172-188`)
reads `skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket* and pins "`<scratchpad>/<work-item-id>/`, in one `rm -rf`" and
"removes nothing else of the scratchpad", both standing at `:48-49`. Claimed
seen red per clause with `seal mutate`. Read: each pinned phrase stands
once in the section, so deleting it fails its own assertion. The module
passes (executed). *Removes* names the old rule 21 case's fact as moved
to this case (read).

What matched: the repair sentence. `skills/implement/orchestration.md:50-53`
says the orchestrator "runs the same command again after each repair it
pushes to the open pull request", which matches the folded T22. The
repair path it answers stands at `skills/code-review/orchestration.md:347-357`
(read). The case's two clauses read the first sentence, and the repeat
names "the same command", so the case holds the path for both removals
(read).

What matched: the READMEs. `README.md:378-380` and `README.ko.md:375-377`
give T24's two renderings, and `tests/behaviour/test_both_editions_carry_the_same_folds.py`
passes (executed).

What matched: the census, re-run at `e3c9c4d60`. The fix touched two files
of the census's corpus, `README.md` and `skills/implement/orchestration.md`.
The reading stays at 865 of 11,561, as `changelog.md:5` gives it
(executed). No measured file changed, so the sizes stand as round 2
measured them.

What matched: `pr.md`. Each of its eight quotes stands word for word, with
whitespace collapsed, in `frame/plan.md` (executed). The two quotes of the
scratch removal, `pr.md:5-6`, quote the rows at `frame/plan.md:74` and
`:80`. Read in order, the second extends the first, and finding 1 is on
the second row's grounds.

What matched: `gaps.md:7` names fix pass 2's narrow set beside the earlier
ones and keeps the broad gate `unverified` for the orchestrator, which is
honest (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD, labelled `unverified`. The fix pass's claimed 1,861 passed was not re-run here | `seal/threads/1794362365-the-definitions-restate-the-contract/gaps.md:7` | the orchestrator, by `seal gate --record` |
| Whether the owner confirms on #1503 that the removal runs again after each repair, so the issue and the tree say the same before the sealer reads them | `seal/threads/1794362365-the-definitions-restate-the-contract/frame/plan.md:80` | the owner |
| Whether agents under the released text still write an `rm`, and take `-2` where their directory stands | `seal/threads/1794362365-the-definitions-restate-the-contract/frame/questions.md:20` | a measurement, as Q2 states |
| The crafter's eval cases, not run | `seal/threads/1794362365-the-definitions-restate-the-contract/gaps.md:10` | the owner, where the release runs them |

## Probes

| Command | Result |
|---|---|
| `python3 -I round-1/test_tmp_census.py round-3/clone e3c9c4d60`, from `<scratchpad>/1794362365-the-definitions-restate-the-contract/` | all 865 of 11561 |
| `bin/test` over the scratch module, `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_both_editions_carry_the_same_folds.py` and `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `-q`, one command in the clone | 129 passed, 2 warnings, exit 0 |

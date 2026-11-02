# Review round 2: 1793580304-a-measurement-no-record-asks-for-closes-its-row

```seal
target: 4463c732f, fixes a77bea51a..4463c732f
```

This verifying round read the diff `a77bea51a..4463c732f` in the branch's
own worktree. The diff holds the orchestrator's fold into the frame
(`d2d786022`, `a489af501`, `4463c732f`), the fix pass `6ab86e6a3` and its
close blocks (`149596234`). The fix pass changed `skills/settle/SKILL.md`
step 6 and the order case's docstring in
`tests/text/test_settle_reads_before_it_removes.py`; no code changed.

Carried from round 1 as coordinates and not re-established: where step 6's
table and `ROWS_HEADING` stand, the framer's probe P1 for the design's
`## Rule changes`, and the 0.22.4 issues #1061 and #1062 with the records
each cites. Round 1 opened those issues; this round did not open them again.
Re-run rather than carried: round 1 finding 1's `seal mutate` swap, and the
two changed modules. No `seal/parity.md` is declared, so the round block
holds no `original:` line. `seal/config.md` holds no `Record language` row,
so the record is English.

The orchestrator asked whether the order case now pins a fact a reader acts
on (`docs/what-a-script-gates.md` *The checks*, the row for the cases under
`tests/text/`). It does. The first confirmation gives the grounds. The one
finding this round opens is a `should`, not a `must`: it is a frame
sentence the fix left standing on the old fact, and no routing of a row and
no code turns on it.

## Findings

### 1. The design's Scope item 1 and its Removes row still say the last row was rewritten to cover only a measurement something on record needs

```seal
severity: should
location: `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/design.md:28`, `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/design.md:92`
evidence: executed `git show 5161c421e:skills/settle/SKILL.md | grep -n "a measurement nobody has taken |"`, `grep -n "covers only\|rewritten in place" seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/*.md`
```

Why it matters: round 1 finding 1's fix put the last row's *When* cell back
to the base sentence. At `4463c732f`, `skills/settle/SKILL.md:283` reads
"it names a run, a platform or a reading no record holds". That is the same
text as the base row at `5161c421e`, line 279, so the row is not rewritten
at all. Only the paragraph under the table and the new row before it change
what reaches it. Two frame sentences still state the fact the fix removed.

- `frame/design.md:28`, *Scope* item 1, says "*a measurement nobody has
  taken* covers only a measurement something on record needs". Read as the
  row's *When* cell, that is false. Under the fix, every measurement no
  record asks for also fits that row, and only the table's order keeps it
  out.
- `frame/design.md:92`, the `## Removes` row, says "The row and paragraph
  are rewritten in place to cover a measurement something on record needs".
  The row is unchanged from the base, so a reader who checks this claim
  against the diff finds no rewrite of the row.

The sealer reads the frame against the tree, and a proofer of a later round
reads *Scope* for what the build owes. Each gets two readings of *Scope*
item 1. One matches the tree and the other matches the cells round 1
refused. Contract rule 19 asks a change to remove what stood on the old
fact in the same commit. The fold `d2d786022` rewrote design `:65` and
`:67`, and left these two lines. This is not a reopen of round 1 finding 1:
the defect that finding named, an order that decides nothing, does not
stand (first confirmation). It is the rest of that finding's class in the
frame.

Claimed (plan *Judgments of the run*, `frame/plan.md:55`): the last kind's
*When* cell returns to the base sentence so the table's order decides.
Found: the skill and design `:65` do so, and design `:28` and `:92` still
describe the old cells.

```markdown
1. `skills/settle/SKILL.md` *The settling session's procedure* step 6. The table gains the kind **a measurement no record asks for** between *answered* and *a measurement nobody has taken*. *A measurement nobody has taken* keeps its base *When* cell, so every measurement no record asks for fits both kinds, and the table's order closes it before it can be re-homed. The rows read as `## Data & interfaces` gives them.
```

```markdown
| The duty to re-home every measurement nobody has taken as an issue. Its catch record: the 0.22.4 settle opened 27 issues under it, and 22 of them closed as not planned (G9) | `skills/settle/SKILL.md` *The settling session's procedure* step 6, the row *a measurement nobody has taken* and the paragraph under the table | The row keeps its base *When* cell. The new kind before it, and the order paragraph rewritten in place, leave it only a measurement something on record needs. A measurement nothing waits on is closed in its record with its reason, which the settle's pull request body lists |
```

```seal
verdict: fixed 02dad8e2f
answer: The orchestrator folded this round's two paste-ready texts into `frame/design.md` *Scope* item 1 (`:28`) and the `## Removes` row (`:92`) at 02dad8e2f, records only; `git diff 7f6104b47 02dad8e2f` shows both lines replaced by the round's text word for word and nothing else. They match the skill: `skills/settle/SKILL.md:283` reads `| a measurement nobody has taken | it names a run, a platform or a reading no record holds | the issue it is re-homed to |`, the base *When* cell. The fix pass changed no file for this finding.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the table's order now decides between the two measurement
kinds, and the order case pins that order (executed and read). Row 3's
*When* cell at `skills/settle/SKILL.md:282` is the base sentence plus "and
no failure, report or decision on record depends on its answer". Row 4's
cell at `:283` is the base sentence alone. So every row that fits row 3
also fits row 4, and first fit is what closes it. Swapped, row 4 would take
every unmeasured row and row 3 would never be reached. That is a fact a
settling session acts on, which is what `docs/what-a-script-gates.md`
*The checks* keeps a prose case for. This round re-ran the close's
`seal mutate` swap of rows 3 and 4. It was red, and the case read
`['moot', 'answered', 'a measurement nobody has taken', 'a measurement no
record asks for']`. The tree was clean after the run. The order paragraph
at `:292-297` and the case's docstring at
`tests/text/test_settle_reads_before_it_removes.py:78-83` state the same
grounds, and the changelog's "Such a row fits both kinds" agrees
(`changelog.md:3`). One premise of the docstring is unpinned: the case
reads only the kind column, so an edit that made row 4's cell exclusive
again would leave it green. That edit would route every row the same way,
so it changes no outcome, and this round raises no finding on it. The
design's `to` at `frame/design.md:79-86` still states the two measurement
kinds as disjoint descriptions. It names the same outcome as the skill:
only a measurement something on record needs opens an issue. So it is no
finding either.

```seal
confirms: round-1#2
```
What holds: "on record" no longer admits the row's own work item (read).
The paragraph at `skills/settle/SKILL.md:285-290` names a record that
outlives the settle and rests on the answer. Its list is an open issue, a
failed run, or a rule or design of another work item. It excludes the row's
own work item, its design, questions and rounds among them, and its `Who
must answer` cell. Read against round 1's coordinates, #1061's row cites its
own round 1 finding, which is now excluded. #1062's row cites its own
`questions.md` Q2, now excluded, and #616, which is closed and so is no open
issue. Both rows now take *a measurement no record asks for*, as the owner
closed them. The fix pass built to the frame's list (`frame/design.md:67`)
and not to round 1's paste-ready text, which also counted a finding of
another work item; the close says so. This round judges that departure
sound. A finding is closed before its own work item seals, and a work item
whose findings would still be open is not in the release a settle reads, so
a finding that outlives the settle has a `deferred` home, which is an issue
the list already holds. Design S1 at `frame/design.md:50`, `:67`,
`frame/questions.md:15` and `changelog.md:3` state the same list.

```seal
confirms: none
```
What matched: the orchestrator's new *Judgments of the run* row is one the
settle reads (executed). `settle.py#judgments` over this work item returned
the row at `frame/plan.md:55` under the group
`` `skills/settle/SKILL.md` *The settling session's procedure* ``, with
nothing named as not read. The template's placeholder line above the table
is the template's own line, `templates/records/sdd-plan.md:25`.

```seal
confirms: none
```
What matched: the two changed modules pass at `4463c732f` (executed:
`bin/test -p no:xdist -q tests/skills/test_settle.py
tests/text/test_settle_reads_before_it_removes.py`, exit 0, 136 passed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD; the suite stays `unverified` here, as `gaps.md` labels it | the branch at `4463c732f` | the orchestrator, by `seal gate --base origin/release/v0.28.0 --record seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row` once the rounds leave nothing open |
| Whether a heading that names the kinds meets the issue's *Done when* sentence "a settle's dry run of a row no record asks for proposes the new kind"; carried from round 1, outside the fix diff | `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/design.md:38` | the sealer, reading the account against the issue |

## Probes

| Command | Result |
|---|---|
| `bin/seal mutate skills/settle/SKILL.md --replace "<row 3>\n<row 4>" "<row 4>\n<row 3>" --tests "bin/test -p no:xdist -q tests/text/test_settle_reads_before_it_removes.py -k test_the_skill_orders_the_row_kinds"`, the two rows written out whole | red, the case failed against the mutation (exit 1); the command exited 0; `git status --short` empty after |
| `bin/test -p no:xdist -q tests/skills/test_settle.py tests/text/test_settle_reads_before_it_removes.py` | exit 0, 136 passed |
| `.venv/bin/python -c` calling `settle.judgments` on this work item | one group, one row at `frame/plan.md:55`, unread empty |
| `git show 5161c421e:skills/settle/SKILL.md`, grepped for the last row | line 279, the same text as `skills/settle/SKILL.md:283` at `4463c732f` |

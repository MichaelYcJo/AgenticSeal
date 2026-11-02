# Review round 1: 1793580304-a-measurement-no-record-asks-for-closes-its-row

```seal
target: a77bea51a against origin/release/v0.28.0
```

This round reviewed the branch at `a77bea51a` against
`origin/release/v0.28.0` (`5161c421e`), in the branch's own worktree. No
earlier round exists, so no verdict was carried. Carried as coordinates and
not re-established: the framer's probe P1 (`rule_changes.py#parse` reads the
design's `## Rule changes` as one `change`), the counts of design G9 for
#1061 to #1087 (this round opened three of the 27, #1061, #1062 and #1070),
and phase 1's seen-red run and its two `seal mutate` runs, which this round
read and did not re-run. No `seal/parity.md` is declared, so the round block
holds no `original:` line. `seal/config.md` holds no `Record language` row,
so the record is English.

The orchestrator asked three things. Whether the skill lets a settling
session tell *a measurement no record asks for* from *a measurement nobody
has taken* without guessing: it does not, for the rows the owner closed in
0.22.4, and finding 2 gives why. Whether anything lets a reader take the dry
run's heading for a proposal per row: nothing in the diff does, and the
first confirmation gives the reading. Whether the new order case pins a fact
a reader acts on: it pins an order that decides nothing between the two
measurement kinds, and finding 1 gives why.

## Findings

### 1. The order the new case pins decides nothing between the two measurement kinds, because their When cells already exclude each other

```seal
severity: should
location: `tests/text/test_settle_reads_before_it_removes.py:77-97`, `skills/settle/SKILL.md:283`, `skills/settle/SKILL.md:289-293`, `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/design.md:65`, `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/design.md:12`
evidence: read `skills/settle/SKILL.md:279-299`, `tests/text/test_settle_reads_before_it_removes.py:77-97`, `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/design.md:12`, `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/design.md:53`, `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/design.md:64-65`, `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/trail/phases/phase-1.md:73-82`, `docs/what-a-script-gates.md:53`
```

Why it matters: the owner's decision in #1045 places the new kind before
*a measurement nobody has taken* "so only a measurement something on record
needs is re-homed". The order was to be what routes an unmeasured row. The
build writes the routing into both When cells instead. Row 3 at
`skills/settle/SKILL.md:282` reads "no failure, report or decision on record
depends on its answer". Row 4 at `:283` reads "a failure, report or decision
on record depends on its answer". The two conditions are each other's
negation, so no row fits both, and first-fit never chooses between them.
Rows 3 and 4 swapped would close and re-home exactly the same rows.

The case's docstring at `tests/text/test_settle_reads_before_it_removes.py:78-81`
claims "the order decides that a measurement no record asks for is closed
before it can be re-homed as an issue". Against the table as built, that
claim is false. Design G6 (`frame/design.md:12`) gives the same ground: "it
decides which kind a row takes". The case therefore turns red on a swap of
rows 3 and 4 that changes no row's outcome, and on a rename of either kind.
The red phase 1 showed under `seal mutate` (`trail/phases/phase-1.md:77-81`)
was a rename, `a measurement no record asks for` to `a measurement nobody
asked for`. It was not a reorder. `docs/what-a-script-gates.md:53` keeps a
case that pins a fact a reader acts on and removes one that pins wording. As
built, the order of rows 3 and 4 is no such fact. The order of moot and
answered before the measurement kinds still is one. The order paragraph's
second ground at `skills/settle/SKILL.md:291-293` has the same false premise:
an order cannot close a row "before it can open an issue" when the cells
already keep that row out of row 4.

Claimed (frame G6, phase 1): the case pins the order, which is a fact. Found:
`skills/settle/SKILL.md:282-283` makes the order between rows 3 and 4
idle, so the case pins only that order's text.

The fix that keeps the owner's mechanism, and the case the issue's *Done
when* asks for, is to put row 4's When cell back to its base text, so the
condition is stated once, in row 3, and the order routes. The same cell in
`frame/design.md:65` changes with it. After the change, the case is shown
red with rows 3 and 4 swapped (contract rule 15), which then re-homes every
unmeasured row.

```markdown
   | a measurement no record asks for | it names a run, a platform or a reading no record holds, and no failure, report or decision on record depends on its answer | the reason, naming what the answer would have decided; nothing is opened |
   | a measurement nobody has taken | it names a run, a platform or a reading no record holds | the issue it is re-homed to |
```

The other route keeps the exclusive cells. It then removes the case and S4,
and puts back #1033's docstring. That route goes against the issue's *Done
when*, "a case pins the table's order", so the frame would have to say why.

```seal
verdict: fixed 6ab86e6a3
answer: Step 6's last row in `skills/settle/SKILL.md` reads the base sentence alone, "it names a run, a platform or a reading no record holds", as the finding's fix and design `:65` (folded at d2d786022) write it, so every measurement no record asks for also fits *a measurement nobody has taken* and the table's order is what closes it first. The order paragraph now says that in so many words, and the order case's docstring says the order closes such a row before it can be re-homed and that the two rows swapped re-home every unmeasured row. The case was shown red at 6ab86e6a3 by `bin/seal mutate skills/settle/SKILL.md` swapping the two measurement rows (red, the case read `['moot', 'answered', 'a measurement nobody has taken', 'a measurement no record asks for']`; the command exited 0 and the tree was clean after). The changelog fragment says a measurement no record asks for fits both kinds and the first fit closes it. Design G6 and `:65` are the orchestrator's and already state this.
```

### 2. "On record" admits the row's own work item's records, so a row citing its own review finding or question reads as a measurement something needs and is re-homed again

```seal
severity: should
location: `skills/settle/SKILL.md:285-287`, `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/design.md:67`, `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/questions.md:15`, `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/changelog.md:3`
evidence: executed `gh issue view 1045 --json title,body,comments`, `gh issue view 1061 --json number,title,stateReason,body`, `gh issue view 1062 --json number,title,stateReason,body`, `gh issue view 616 --json number,state,stateReason,title`
```

Why it matters: the paragraph at `skills/settle/SKILL.md:285-287` is the one
place a settling session learns what counts as on record. It reads "a record
other than the row itself: an open issue, a failed run, a review finding, or
a rule or design that rests on the answer", and it excludes only "the row's
own `Who must answer` cell". It does not say whether the row's own work
item's records count. Those are its design, its questions and its review
rounds. Every row has them, because a `## Not verified` row qualifies a
claim its own work item made. `docs/the-record-layout.md:98-102` says the
same: "the rule it qualifies reached users in the code with the release".

The owner's 0.22.4 closures show what the row cites. The #1045 body gives
the owner's ground for the 20 closed as not planned: "a run on a platform, a
version or a failure shape that no failure on record points to". #1061 is
closed as not planned, and its row cites "round 1's U+1F7E1 1", a review
finding of its own work item. #1062 is closed as not planned, and its row
cites its own `questions.md` Q2 and "#616's *Who acts*". #616 is closed as
completed. Read by the paragraph as written, both rows name "a review
finding" or "a design" that rests on the answer, so both take *a measurement
nobody has taken* and are re-homed. That is the outcome this work exists to
stop. To close them, a session has to assume an exclusion the text does not
state. That assumption is the guess the orchestrator asked about.
`frame/questions.md:15` states the assumption the build carried: "on record
counts a record other than the row itself". It is too wide for the same
reason.

The ground for narrowing it is in the tree: `seal settle --apply` removes the
released work item's directory with its record (`docs/the-record-layout.md:98-118`).
Nothing in that directory can still be waiting on the answer once the
settle ends.

Claimed (frame `## Data & interfaces`, phase 1's decision to write the
paragraph): the paragraph keeps every row from being re-homed again. Found:
it keeps out the `Who must answer` cell, and lets in the own work item's
finding, question and design, which are what #1061 and #1062 cite.

```markdown
   On record means a record that stays after this settle and names this
   measurement, or the doubt it would settle, as something it waits on: an
   open issue, a failed run whose cause the answer would settle, or a
   finding, rule or design of another work item that cites it. The row's own
   work item does not count, its `Who must answer` cell, its design, its
   questions and its rounds among them. Every row has those, and the settle
   removes them with the directory.
```

`frame/design.md:67` and `frame/questions.md:15` say the same in the
frame's words. The changelog sentence at `changelog.md:3`, "On record means a
record other than the row itself", follows the skill.

```seal
verdict: fixed 6ab86e6a3
answer: The *On record* paragraph under step 6's table in `skills/settle/SKILL.md` now says a record that outlives the settle and rests on the answer, an open issue, a failed run, or a rule or design of another work item, and that the row's own work item, its design, questions and rounds among them, is not one because `--apply` removes its directory; the row's own `Who must answer` cell is not one either. It follows design `:67` as the orchestrator folded it at d2d786022, in place of the finding's paste-ready text, which also counted a finding of another work item and "a failed run whose cause the answer would settle"; the frame's list is the one built to. `changelog.md:3` says the same. `frame/questions.md:15` was corrected by the orchestrator at d2d786022.
```

## Confirmations

```seal
confirms: none
```
What matched: nothing in the diff lets a reader take the dry run's heading
for a proposal per row (read). `ROWS_HEADING` at
`skills/settle/scripts/settle.py:434-439` prints once above every open row
and says the rows are "for the settling session to decide". The skill's new
sentence at `skills/settle/SKILL.md:196-198` says the heading "gives no row a
kind: the settling session decides each". The changelog at `changelog.md:3`
says the same. The heading names the fourth kind as "a measurement to
re-home", while the table at `:283` names it "a measurement nobody has
taken". The base heading had the same difference for the old third kind, so
this is not new. The frame reads the issue's "proposes the new kind" as the
heading naming the kinds. That reading rests on `skills/core/SKILL.md`
*Judgment is spent where meaning is the question, and a script answers the
rest*, and `plan.md` A4 gives a failure scenario for a per-row proposal. This
round agrees with that reading.

```seal
confirms: none
```
What matched: a closure of the new kind is read as closed (read).
`skills/settle/scripts/settle.py:1204-1212` takes each closed row with
whatever closed it from the reader's `check_text`, and requires no issue
number. A row closed with a reason and nothing opened leaves no open row.
`--apply` then removes the directory.

```seal
confirms: none
```
What matched: the re-home paragraph at `skills/settle/SKILL.md:295-299` adds
"the record that needs its answer" to the issue body, as design *Scope* item
3 and `plan.md` A9 ask (read).

```seal
confirms: none
```
What matched: phase 1's departure on #1033's docstring (read). In the base
docstring, "The steps, their order and the row kinds", "their order" grammatically
refers to the steps. Keeping the steps' order with the proofer and giving
the kinds' order to the new case is the narrower reading, and it is correct
(`tests/text/test_settle_reads_before_it_removes.py:66-69`). The docstring
inherits finding 1 only through what "the next case" holds.

```seal
confirms: none
```
What matched: the two changed modules pass at `a77bea51a` (executed:
`bin/test -p no:xdist -q tests/skills/test_settle.py
tests/text/test_settle_reads_before_it_removes.py`, exit 0, 136 passed).
The design's `from` stands at `docs/the-record-layout.md:105-107` (read). A
`git grep` outside `seal/threads` and `tests` for "re-home", "nobody has
taken", "no record asks", "as an issue" and "an issue per" lists no other
statement of the kinds than step 6, `ROWS_HEADING` and the policy sentence
(executed). This is a search for wordings, so it is a sample.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD; the suite stays `unverified` here, as `gaps.md` labels it | the branch at `a77bea51a` | the orchestrator, by `seal gate --base origin/release/v0.28.0 --record seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row` |
| Whether a heading that names the kinds meets the issue's *Done when* sentence "a settle's dry run of a row no record asks for proposes the new kind" | `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/design.md:38` | the sealer, reading the account against the issue |
| Whether `chain-check` reads the design's `## Rule changes` with no refusal at the pull request (S5); carried from probe P1, not re-run | `seal/threads/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/design.md:77-86` | `chain-check` in CI at the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test -p no:xdist -q tests/skills/test_settle.py tests/text/test_settle_reads_before_it_removes.py` | exit 0, 136 passed |
| `gh issue view 1045 --json title,body,comments` | the owner's decision: the new kind sits before *a measurement nobody has taken* "so only a measurement something on record needs is re-homed"; *Done when* asks that a case pin the table's order |
| `gh issue view 1061`, `gh issue view 1062`, `gh issue view 1070`, each `--json number,title,stateReason,body` | all three closed as not planned; #1061's row cites its own round 1 finding, #1062's its own `questions.md` Q2 and #616 |
| `gh issue view 616 --json number,state,stateReason,title` | closed, completed |

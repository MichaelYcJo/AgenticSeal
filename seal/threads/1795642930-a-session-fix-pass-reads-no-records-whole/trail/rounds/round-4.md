# Review round 4: 1795642930-a-session-fix-pass-reads-no-records-whole

```seal
target: 14974eb1d, fixes 237a8a127..14974eb1d
```

This is a verifying round over the fix range `237a8a127..14974eb1d`. The
range holds five commits: the round 3 record `5bb4c7dca`, the framer's fold
`1886588da` of the two frame files, the orchestrator's fix `143f205f1`, its
correction `1bd0f484d` of `changelog.md`, and the close blocks `14974eb1d`,
which touches `trail/rounds/round-3.md` alone (executed: `git show --stat`
on each). The code the round reviews is that range's diff outside the
round record: `skills/code-review/orchestration.md:36-39`,
`skills/implement/fix-pass.md:120-123`,
`skills/implement/orchestration.md:91-94`,
`tests/text/test_a_moved_rule_leaves_its_definition.py:302-305`,
`changelog.md:3-4` and its *Process changes* row, and the fold's hunks of
`frame/design.md` and `frame/plan.md`. The round read the branch's own
checkout and probed in a `git clone --no-local` at `14974eb1d` under the
round's scratch directory. `seal/parity.json` is not declared, so no parity
comparison was owed.

The work item's records were each read whole at `14974eb1d`: `routing.md`,
the three frame files, `gaps.md`, `changelog.md`, `pr.md`,
`trail/phases/phase-1.md`, and the three earlier round records for their
coordinates. `seal/config.json` names English for both language keys, so no
`pr.<lang>.md` is owed and none stands. Issue #1623 was read with
`gh issue view 1623 --json body,comments`. Its one comment, of
2026-11-25T22:33:54Z, records the prevention home, and its *Done when* is
met at `skills/implement/fix-pass.md:99-123` (read).

Carried from rounds 1 to 3 and not established again: that no executable
line changes, the reading of G8's measurement and of Owlery #236, the red
runs of the phase record, and round 2's observation that the paragraph's
order rests on where a read falls against the last fix commit
(`trail/rounds/round-2.md:247-256`). Re-derived here: every close of round
3, the code of the fix range, the new case's red run, and each sentence of
the records against `14974eb1d`.

The spawn asked the round to weigh four things. The new definition of the
implementer reads one way, and its citation gives it one home (round 3
finding 1 confirmed below). The account sentence reads two ways where the
read itself commits a correction (finding 2). This pass's account claims a
read of each hunk's paragraph that its command did not print (finding 1).
The pass checked the account against the session transcript, as round 3
did, and its numbers, `1 failed`, `1 passed` and `1516 passed`, match the
results the transcript holds (executed, *Probes*).

## Findings

### 1. The account of this pass says each hunk was read with its paragraph, and the one diff it printed after the fix commit carried five lines of context

```seal
severity: should
location: `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/rounds/round-3.md:217`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/rounds/round-4.md`
evidence: executed `<scratchpad>/1795642930-a-session-fix-pass-reads-no-records-whole/round-4/test_tmp_transcript_commands.py` and `test_tmp_transcript_results.py` over the orchestrator's session transcript `/Users/x/.claude/projects/<project>/<session>.jsonl` from 22:31:00Z to 22:38:30Z, `git reflog --date=iso -n 10`, `git diff 5bb4c7dca..143f205f1 -U5 -- skills tests seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/changelog.md | grep -n '^@@\|^diff'`, the account's sample `git grep -n -F -e "last build or fix" -e "wrote the work item's last" -e "last build phase or fix pass" -e "The fix pass is made by" -e "beside the crafter as the party" -e "held and not read" -e "commands made after"`; read `skills/code-review/orchestration.md:34-50`, `skills/implement/fix-pass.md:99-124`, `skills/implement/orchestration.md:76-94`, `tests/text/test_a_moved_rule_leaves_its_definition.py:277-310`, `agents/crafter.md:150-155`
reopens: round-3#2
```

Why it matters: round 3 finding 2's close does not hold. Its fix was this
pass's own account, written under the new sentence of
`skills/implement/fix-pass.md:120-123`, which has the account state only the
reads the pass's commands made after its last fix commit and name as held
and not read a part it did not print again. The account says that after
`143f205f1`, `git diff 5bb4c7dca..143f205f1 -U5 -- skills tests <this
item>/changelog.md` "was printed with no column cut and each hunk read
with its paragraph", over five paths (`trail/rounds/round-3.md:217`). The
rule the account answers to asks for each hunk "with the paragraph or unit
around it, a case's name, docstring and comments among them"
(`agents/crafter.md:152-154`).

The command ran at 22:34:45Z, six seconds after the fix commit, and its
`-U5` printed five lines on each side of each change (executed). Four of
the five hunks did not reach their paragraph or unit:

- `skills/code-review/orchestration.md`: printed 31-45, and the
  definition's paragraph runs 34-50.
- `skills/implement/fix-pass.md`: printed 115-128, and the bold paragraph
  the new sentence closes runs 99-124.
- `skills/implement/orchestration.md`: printed 86-99, and the paragraph
  opening **The framer writes a decision's fold** runs 76-94.
- `tests/text/test_a_moved_rule_leaves_its_definition.py`: printed 297-310,
  and the case runs from its `def` at 277. The hunk header names the case,
  and its docstring at 278-285 was not printed.

No later command of the pass printed those lines. The commands after the
fix commit are the diff, three prints of the work item's records, the
correction `1bd0f484d` with its one-line hunk, the sample cut at 200
columns, the narrow set, and the close blocks (executed, *Probes*). The
`changelog.md` hunk alone covered the whole file. So the account claims the
paragraph and docstring reads, which the pass held from its substitutions
and from earlier passes. The new sentence names that part as held and not
read. This is the third account in this run that claims a read its
commands did not make, and the first written with the prevention home in
the file it was written from.

Two smaller parts of the same account fall short of the paragraph it
answers to. First, it names `frame/design.md:1-19`, printed cut at 120
columns, as held and not read. Those lines are the dated *Grounding*, and
the crafter's rule calls the six files a closed set, none of it handed on
as a sample (`agents/crafter.md:165-166`). A part of that set the pass did
not read is a part it did not finish, and
`skills/implement/fix-pass.md:119-120` sends that to `gaps.md`
`## Not done`. Second, the sample printed `changelog.md:3` and
`changelog.md:4`, and the account's list of what it printed names neither
(executed: the sample, run again at the target).

This round read the four paragraphs, the case's docstring and
`frame/design.md:1-19` whole at the target. It found no statement in them
that HEAD contradicts. The docstring claims less than the case now pins, as
round 3 found for the sibling case, and misleads no reader. So the defect is
the account again, not a missed statement. It matters for the reason round
3 gave: the sealer reads the account at step 4, and the `seal/follow-up.md`
row counts it as a read made. That the home was in place and the claim
recurred is the signal `skills/implement/orchestration.md:170-177` and
`frame/plan.md` *Alternatives considered* row 17 weigh. Whether it calls for
more than the text is the orchestrator's judgment and no part of this
finding.

The fix is the next pass's account, in this record's close blocks. It
prints what it says it read, or names the rest as held.

```text
Method: the read starts from the fix commit <sha>. After it, each changed
prose file was printed whole at <sha> (`git show <sha>:<path>`), or each
hunk with enough context to reach the blank lines of its paragraph, and
each changed case from its `def` (executed). A part of a paragraph or case
outside what a command printed is named as held and not read. routing.md,
the three frame files, gaps.md and changelog.md were each printed whole
(read); a part of them not printed goes to gaps.md `## Not done` with why.
A correction the read committed, <sha>, had its hunk printed after that
commit. Sample: `git grep -n -F` on the words of each rule the range
reworded: <one phrase per rule>. It printed <every place>, each corrected
or standing for <why>; a sentence in other words escapes it.
```

### 2. The account sentence anchors its reads to the pass's last fix commit, and the read's own corrections land in fix commits after it

```seal
severity: should
location: `skills/implement/fix-pass.md:120-123`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:32`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:58`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:66`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/plan.md:62`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/changelog.md:3`
evidence: executed `git grep -n -F -e "last fix commit" -e "after that commit"`, `git grep -n -F -e "after your last commit" -e "its corrections" -e "corrections its read made"`, `git reflog --date=iso -n 10`; read `skills/implement/fix-pass.md:106-123`, `skills/implement/fix-pass.md:138-150`, `skills/code-review/orchestration.md:98-101`, `agents/crafter.md:150-155`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/rounds/round-2.md:247-256`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/rounds/round-3.md:217`
regression: round-3#2
```

Why it matters: the unit is the account sentence that `143f205f1` added to
`skills/implement/fix-pass.md` *The narrow set, then the read of the
range*. The frame's fold `1886588da` worded it "after its last fix commit"
(`frame/design.md:32`, `:66`), the fix built that wording as it stood, and
the defect came from the fold, which took the anchor from the orchestrator's
proposal without setting it beside the paragraph's own order.

The sentence reads "The account states only the reads the pass's commands
made after its last fix commit" (`fix-pass.md:120-121`). The same paragraph
says that "In its fix commits" the orchestrator corrects every statement
HEAD contradicts in its range, `gaps.md` and `changelog.md`
(`fix-pass.md:107-109`). Those statements are what the read finds, so a
correction the read finds lands in a fix commit made after the read. Read
that way, the last fix commit comes after the read whenever the read finds
something. The account can then state the read that found the correction
only by reading everything again after it. Two lines of the same file read
the other way. `fix-pass.md:148` has the close blocks appended "after its
last fix commit and its corrections", and
`skills/code-review/orchestration.md:99-100` "after its fix commits and the
corrections its read made". Both set the corrections apart from the fix
commits. The crafter's rule anchors its read to "your last commit"
(`agents/crafter.md:152`) and gives a crafter the same choice. Round 2 had
already found that "Where a read falls against the last fix commit is the
fact the paragraph's order rests on" (`trail/rounds/round-2.md:254-256`).

This pass shows the split. Its correction `1bd0f484d` changed
`changelog.md` at 22:35:15Z, after the whole-file reads of 22:34:50Z to
22:35:03Z (executed). The account lists it as "fix `1bd0f484d`", the
pass's last fix commit, and dates its whole-file reads "after `143f205f1`"
(`trail/rounds/round-3.md:217`). Under the first reading, those reads come
before the last fix commit and the account breaks the sentence. Under the
second, it keeps it. A round cannot tell which the sentence asked for, and
the prevention home exists so that a round can check an account against the
commits.

The search printed the sentence at `fix-pass.md:121` and `:123`. It also
printed four statements of the anchor in this item's records:
`frame/design.md:32`, `:58` and `:66`, `frame/plan.md:62`, and
`changelog.md:3`. `fix-pass.md:142` and `:148` use "last fix commit" for
the evidence command's rerun and the close blocks, and they agree with the
second reading. The issue comment of 2026-11-25T22:33:54Z states the
anchor too and is outside the tree. It is a search on words, so it is a
sample; a statement of the anchor in other words escapes it. The snippets
take the second reading, because `:148` and the orchestrator's half
already use it, and they name the commit. The frame lines go to the
framer's fold, and `frame/plan.md:62` is a judgment row the fold decides
whether to keep as dated.

```markdown
<!-- skills/implement/fix-pass.md:120-123 -->
`gaps.md` `## Not done` too. The account names the fix commit its read
starts from and states only the reads the pass's commands made after it,
each labelled as contract rule 4 asks. A correction the read commits has
its own hunk printed after that commit, and the account names the commit.
A part the pass held from its own edit or from a hand-back, and did not
print after the commit its read covers, it names as held and not read.
```

```markdown
<!-- frame/design.md:32, Scope item 1, the third bullet, the framer's fold -->
   - The account, in the crafter's hand-back or in the orchestrator's close blocks and `gaps.md`, names the fix commit its read starts from and states only the reads that the pass's commands made after it, each labelled as contract rule 4 asks. A correction the read commits has its own hunk printed after that commit. A part the pass held from its own edit, or from another party's hand-back, and did not print after the commit its read covers is named as held and not read. <the rest of the bullet as it stands>
```

```markdown
<!-- frame/design.md:58, S8, its Given / When / Then cell -->
Given any pass. When it writes the account of its read, then each read it states is one its commands made after the fix commit the read starts from, which the account names, and a part it held from its own edit or a hand-back is named as held and not read
```

```markdown
<!-- frame/design.md:66, the last two sentences of the wording -->
The account names the fix commit its read starts from and states only the reads the pass's commands made after it, each labelled as contract rule 4 asks. A correction the read commits has its own hunk printed after that commit, and a part the pass held from its own edit or a hand-back and did not print after the commit its read covers is named as held and not read.
```

```markdown
<!-- changelog.md:3, the sentence on the account -->
The account names the fix commit its read starts from and states only the reads the pass's commands made after it, labelled as contract rule 4 asks, and names as held and not read what the pass held from its own edit or a hand-back and did not print again, since this work's own passes twice claimed reads their commands had not made.
```

## Confirmations

```seal
confirms: round-3#1
```
What holds: `skills/code-review/orchestration.md:36-39` reads "The
implementer is the orchestrator where `routing.md` answers `Implementation`
with `the session`. In every other route it is the crafter that made the
work item's last build phase or fix pass, also where a fix the orchestrator
wrote after the last round came later", the finding's first snippet (read).
Under a crafter route after the orchestrator's fix of a sealer's verdict,
the head and the threshold's `agent-*.jsonl` now name the same crafter, and
the paragraph at `:57-61` keeps the orchestrator's own passes to
`the session`. `skills/implement/orchestration.md:91-94` now cites the
section and states no criterion of its own, so the definition has one home
(read). The search on the old criterion's words prints no statement outside
the records and released items' dated records, and every use of
"implementer" across the tree outside `seal/threads` names the term
without a criterion that differs (executed: `git grep -n -i implementer`,
the account's sample). `frame/design.md:35` and `:36`, S7 at `:57`, the
*Removes* rows at `:78-79`, rows 14 and 15 of *Alternatives considered* at
`frame/plan.md:36-37`, and `changelog.md:4` state the definition as HEAD
holds it (read).

What matched: the new pin. `contract rule 4` stands once in *The narrow
set, then the read of the range* (executed), as *Scope* item 5 states at
`frame/design.md:37`. With only the account sentence removed from the
clone, `test_whoever_makes_the_fix_pass_makes_the_reading_of_the_range`
failed on "no longer says 'contract rule 4'", and it passed restored
(executed, *Probes*), so S8's *Verifiable how* reads true. No other case in
`tests` pins that citation (executed: `grep -rn -F 'contract rule 4'
tests`), so the added fact covers nothing its group already covers.

What matched: the prevention home went the way
`skills/implement/orchestration.md:170-177` gives it. The framer folded it
at `1886588da` after the orchestrator's message of 22:31:26Z, the
orchestrator commented on the issue at 22:33:54Z, and the fix `143f205f1`
built it at 22:34:39Z (executed: the transcript listing and the reflog).
The rows the fold added, `frame/plan.md:36-39` and `:61-62`, cite
paragraphs that stand at `skills/implement/orchestration.md:61` and `:170`
and at `skills/core/SKILL.md:46` (read).

What matched: the records against the tree. `changelog.md:3-4` and its
*Process changes* row state what HEAD holds, apart from the anchor of
finding 2 (read). The two quotes of `pr.md` stand word for word at
`frame/questions.md:17`, in the *Default until answered* cell, and at
`gaps.md:12` (read). `routing.md`, `frame/questions.md`, `gaps.md` and
`trail/phases/phase-1.md` did not change in the range and still hold at
HEAD. Q1's "rows 8 and 9" still name the hook rows of *Alternatives
considered*, since the fold appended its rows after row 13 (read).
`seal/threads/1794289596-implement-orchestration-grew-back/frame/design.md:92`,
which the account's sample printed and left standing, belongs to an item
first released in `v0.37.2` (executed: `git tag --contains` on its
`routing.md` commit).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the suite is `unverified` here, since this round ran three modules only | `seal/config.json` `Broad gate` | the orchestrator, by its broad run after the rounds settle |
| Whether a mechanism beyond the text is owed for an account that claims reads, now that the claim recurred under the prevention home (finding 1) | `skills/implement/orchestration.md:170-177`, `frame/plan.md` *Alternatives considered* row 17 | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_docs_line_wrap.py -q -p no:xdist`, in the clone at `14974eb1d` | 100 passed, exit 0 |
| `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py -q -p no:xdist -k whoever_makes`, in the clone with the two sentences of `skills/implement/fix-pass.md:120-123` removed by an edit, restored after with `git checkout` | 1 failed, exit 1, on "no longer says 'contract rule 4'" |
| `test_tmp_transcript_commands.py`, the orchestrator's `tool_use` entries from 22:31:00Z to 22:38:30Z | the fold committed at 22:33:48Z; the edits, the red run and the narrow set at 22:34:05Z to 22:34:15Z; the fix commit; `git diff 5bb4c7dca..143f205f1 -U5` at 22:34:45Z; the records printed at 22:34:50Z, 22:34:57Z and 22:35:03Z; the correction commit at 22:35:15Z with `git show HEAD -U0 --word-diff=plain \| tail -2`; the sample cut at 200 columns at 22:35:20Z; the narrow set at 22:35:27Z; the close blocks |
| `test_tmp_transcript_results.py`, the tails of the results in the same window | `1 failed`, `1 passed`, `1516 passed`, and `1516 passed` again after the correction |
| `git diff 5bb4c7dca..143f205f1 -U5 -- skills tests <this item>/changelog.md \| grep -n '^@@\|^diff'` | hunks at changelog 1-11, `skills/code-review/orchestration.md` 31-45, `skills/implement/fix-pass.md` 115-128, `skills/implement/orchestration.md` 86-99, the test file 297-310 |
| the account's sample, run again at the target | the places the account names, and `changelog.md:3` and `changelog.md:4` beside them |

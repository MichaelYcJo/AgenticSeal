# Review round 2: 1795642930-a-session-fix-pass-reads-no-records-whole

```seal
target: d0f59251b, fixes fb9054e79..d0f59251b
```

This is a verifying round over the fix range `fb9054e79..d0f59251b`. The
range holds four commits: the framer's fold `a8dab6c96` for round 1
finding 4, the orchestrator's fix `9e2b4c5e2`, the orchestrator's fold
`c49e96507` of a frame sentence its read found, and the close blocks in
`d0f59251b`, which touches `trail/rounds/round-1.md` alone (executed:
`git show --stat` on each). The round was read in the branch's own
checkout and probed in a `git clone --no-local` at `d0f59251b` under the
round's scratch directory. `seal/parity.json` is not declared, so no parity
comparison was owed.

The work item's records were each read whole at `d0f59251b`: `routing.md`,
the three frame files, `gaps.md`, `changelog.md`, `pr.md`,
`trail/phases/phase-1.md` and `trail/rounds/round-1.md`. `seal/config.json`
names English for both language keys, so no `pr.<lang>.md` is owed and none
stands. Issue #1623 was read with `gh issue view 1623 --json body`; its
*Done when* is met at `skills/implement/fix-pass.md:99-120`, which binds the
reading to "whoever makes the pass, the crafter or the orchestrator" and
maps the rule's *Job* and hand-back for the orchestrator's pass (read).

Carried from round 1 and not established again: the coordinates of its
search lists, its reading of G8's measurement and of Owlery #236, the red
runs of the phase record, and that no executable line changes. Re-derived
here: every close, the code of the fix range, and each sentence of the
records against `d0f59251b`.

The round answers a question the spawn put beside the procedure. The
question asks whether the orchestrator's pass made the reading that the new
paragraph binds. The account stands in round 1 finding 5's `answer:`, as
that paragraph places it. It names a method, the files read whole, one fold,
a sample by four phrases and where the sample stops, so it has the shape the
paragraph asks for. The reading behind it did not reach its whole range,
and three statements that range or those files held still stand. Findings
3 and 4 are those statements, and finding 5 is the method.

## Findings

### 1. The rewritten definition of the implementer resolves to the orchestrator in every route, because the orchestrator writes the last commit each round reviews

```seal
severity: should
location: `skills/code-review/orchestration.md:36-38`
evidence: executed `git grep -n -F -e "the last commit the" -e "wrote the work item's last" -e "the party that wrote" -- ':!seal/threads'`; read `skills/code-review/orchestration.md:34-59`, `skills/code-review/orchestration.md:105-110`, `skills/code-review/orchestration.md:341-344`, `skills/implement/orchestration.md:36-43`, `skills/implement/orchestration.md:89-96`
regression: round-1#1
```

Why it matters: the unit is the definition at
`skills/code-review/orchestration.md:36-38`, which `9e2b4c5e2` rewrote from
round 1 finding 1's snippet. The frame's *Scope* item 3 asks the section to
state the implementer where `routing.md` answers `Implementation` with
`the session`. The fix did that, but it also changed the term's head from
"the crafter that wrote the last commit the round reviewed" to "the party
that wrote the last commit the round reviewed". It then lists the parties
as "the crafter, or the orchestrator where `routing.md` answers
`Implementation` with `the session`".

The last commit a round reviews is the orchestrator's in every route. Round
1 reads up to the commit of `pr.md`, which "The orchestrator writes ... and
commits ... before it spawns the first round"
(`skills/code-review/orchestration.md:341-344`,
`skills/implement/orchestration.md:40-43`). A verifying round reads up to
the commit of the round record, which the orchestrator makes "in one commit
for the whole pass" (`skills/code-review/orchestration.md:105-110`). This
round's own target, `d0f59251b`, is that commit. So under a crafter route
the head of the sentence names the orchestrator, and its list names the
crafter. The reader has to choose. The old head said "the crafter", so it
named the crafter in that case.

The same fact has a second statement that does not have this problem.
`skills/implement/orchestration.md:91-93` says "The fix pass is made by the
party that wrote the work item's last build or fix commit: the crafter,
resumed or spawned fresh, or the orchestrator where ...". That is *Scope*
item 4's wording. The search printed these two definitions and the
unrelated `skills/code-review/orchestration.md:152`. It matches words on a
single line, so it is a sample, and the definition at `:36-37` wraps its
phrase across a line break. The fix uses the criterion that the other
statement already uses. The paragraph keeps its bold lead.

```markdown
<!-- skills/code-review/orchestration.md:36-38 -->
otherwise.** The implementer is the party that wrote the work item's last
build or fix commit: the crafter, or the orchestrator where `routing.md`
answers `Implementation` with `the session`. Before the fix pass, the
orchestrator runs
```

```seal
verdict: fixed 6cb87fd8f
answer: The finding holds. `skills/code-review/orchestration.md` now defines the implementer as "the party that wrote the work item's last build or fix commit: the crafter, or the orchestrator where `routing.md` answers `Implementation` with `the session`", the snippet's wording and the criterion of `skills/implement/orchestration.md:91-93`. The paragraph's bold lead is unchanged. `git grep -n -F -e "last commit the" -e "wrote the work item's last" -e "the party that wrote"` outside released items' records prints the two definitions, which now agree, and `skills/code-review/orchestration.md:153`, which is about the party that wrote a named line and stands (executed).
```

### 2. The case written for *Scope* item 3's paragraph no longer goes red when that paragraph is removed

```seal
severity: should
location: `tests/text/test_the_rules_have_one_owner.py:448-451`, `skills/code-review/orchestration.md:55-59`
evidence: executed `bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k test_the_fix_pass_reads_the_implementers_context_before_it_resumes` in the clone with `skills/code-review/orchestration.md:55-59` removed; read `tests/text/test_the_rules_have_one_owner.py:429-453`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:53`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/phases/phase-1.md:6`
regression: round-1#1
```

Why it matters: the unit is the paragraph of
`skills/code-review/orchestration.md:55-59` and the facts that
`test_the_fix_pass_reads_the_implementers_context_before_it_resumes` holds
for it. The frame's S4 (`frame/design.md:53`) is verified by that case,
"seen red with only *Scope* item 3's sentence removed", and the phase
record says it was seen red that way (`trail/phases/phase-1.md:6`). The fix
of round 1 finding 1 moved `Implementation` and `the session` into the
definition at `:37-38` as well. After that, the section holds each fact
twice (executed: the section flattened and counted, 2 and 2). With the
paragraph at `:55-59` removed in the clone, the case passes (*Probes*). So
no case holds the paragraph that has the orchestrator make each fix pass
itself and sets the threshold and the spawn aside. That is a behaviour the
diff changed. The case's comment at `:448-449` also claims a pin of that
paragraph that it no longer has.

The fix pins the one fact that only that paragraph holds in the section:
the section it cites for the orchestrator's close blocks. It counts once in
the section (executed). The case has to be seen red with only that
paragraph removed (contract rule 15).

```python
        # The routing row and its answer under which the orchestrator is the
        # implementer (#1623).
        "`Implementation`",
        "`the session`",
        # The section the orchestrator's own pass follows for its close
        # blocks, cited only by the paragraph that has the orchestrator make
        # each fix pass itself under that answer (round 2 of #1623).
        "`skills/implement/fix-pass.md` *The close blocks, last*",
```

```seal
verdict: fixed 6cb87fd8f
answer: The finding holds. `test_the_fix_pass_reads_the_implementers_context_before_it_resumes` now also pins "`skills/implement/fix-pass.md` *The close blocks, last*", which in the section only the paragraph opening **Where `routing.md` answers `Implementation` with `the session`** holds, and its comment no longer claims that the two routing facts pin that paragraph. With only that paragraph removed the case failed, and with it restored it passed (executed: `bin/test tests/text/test_the_rules_have_one_owner.py -q -k implementers_context`, `1 failed`, then `1 passed`). So `frame/design.md` S4's verification holds again.
```

### 3. The `seal/follow-up.md` row reads the account of an orchestrator's pass in close blocks alone, after the fix of finding 4 gave it a second home in `gaps.md`

```seal
severity: should
location: `seal/follow-up.md:48`
evidence: executed `git grep -n -F "close block \`answer:\` of such a pass"`, `git grep -n -e "close blocks' \`answer:\`" -e "last close block" -e "answer:\` of the close block" -- ':!seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole'`; read `seal/follow-up.md:48`, `skills/implement/fix-pass.md:113-120`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/changelog.md:3`
regression: round-1#4
```

Why it matters: the unit is the row at `seal/follow-up.md:48`, which
`9e2b4c5e2` changed. The same commit's fix of round 1 finding 4 changed the
fact the row restates. The frame's fold `a8dab6c96` gave the read's account
a second home: "Where the pass appends no close block, because no finding
names its fix, they go into `gaps.md` `## Not done`"
(`skills/implement/fix-pass.md:118-119`). The row still says "the
mechanism's own record is read: each close block `answer:` of such a pass,
for whether it names the method of the read and where a sample stopped, as
`skills/implement/fix-pass.md` *The narrow set, then the read of the range*
asks". So whoever measures under it skips every pass that appends no close
block, the fix of a sealer's verdict among them. The orchestrator's account
says it caught the same fact in `changelog.md:3`, which now names
`gaps.md`, and it says nothing about this row. Outside this item's records,
the search on the account's homes printed `fix-pass.md:116-117` and this row
alone. It is a search on words, so it is a sample.

```markdown
<!-- seal/follow-up.md:48, the sentence on the mechanism's own record -->
Beside that count, the mechanism's own record is read: each close block `answer:` of such a pass, and its `gaps.md` `## Not done` where it appends no close block, for whether it names the method of the read and where a sample stopped, as `skills/implement/fix-pass.md` *The narrow set, then the read of the range* asks.
```

```seal
verdict: fixed 6cb87fd8f
answer: The finding holds. The row's sentence on the mechanism's own record now reads "each close block `answer:` of such a pass, and its `gaps.md` `## Not done` where it appends no close block, for whether it names the method of the read and where a sample stopped", the snippet's wording.
```

### 4. The folded *Data & interfaces* sentence still lists the diff without `seal/follow-up.md`, which the diff changes

```seal
severity: should
location: `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:59`
evidence: executed `git diff --stat 4e7ad2362..d0f59251b`, `git show --stat c49e96507`; read `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:57-59`, `skills/implement/orchestration.md:80-88`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/gaps.md:7`
regression: round-1
```

Why it matters: the unit is the sentence that the orchestrator's fold
`c49e96507` rewrote at `frame/design.md:59`. It is not dated to the
framer's commit, because it says what the work's diff is. The fold changed
"procedure text in three files ..., `changelog.md`" into "procedure text in
`skills/`, the cases of *Scope* item 5, the work item's records and
`.claude-plugin/plugin.json`". `git diff --stat 4e7ad2362..d0f59251b` also
prints `seal/follow-up.md`. That file is the repository's follow-up table,
not this work item's records, and `gaps.md:7` names the row this item adds
there. The build already left it out of the sentence. The fold rewrote the
list and kept it out, so the list still contradicts the diff.

A fold that comes from what a fix changed "removes the frame sentence HEAD
contradicts, or narrows it to what HEAD still holds"
(`skills/implement/orchestration.md:83-86`). The sentence is not needed,
because the rest of the paragraph says what no change adds. So the fix
removes it.

```markdown
<!-- frame/design.md:59 -->
No code, schema or interface changes. No new heading, file, hook, command, configuration key or record field is added, so no unit of `skills/implement/fix-pass.md` *A fix that needs a unit the frame does not name waits for the fold* is added. The new text keeps the repository's prose width, which `tests/behaviour/test_docs_line_wrap.py` holds for the files it lists.
```

```seal
verdict: fixed fa0693951
answer: The finding holds, and it went to the framer's fold, at `fa0693951`, by the orchestrator's row of `frame/plan.md` *Judgments of the run*. The fold removes the sentence listing the diff from `frame/design.md` *Data & interfaces*, as the snippet gives it, and narrows `frame/plan.md` *Operational impact*'s list of changed files, which also missed files of the diff, to a citation of `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file* with `skills/implement/fix-pass.md` among the files it lists (read). The framer named `skills/implement/SKILL.md` as a second file the removed sentence missed; it did not, since the sentence said "procedure text in `skills/`", so the orchestrator's row stands as written.
```

### 5. The pass's read did not reach its whole range, its sample skipped the rule finding 4's fix reworded, and its account gives an order the commits do not show

```seal
severity: should
location: `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/rounds/round-1.md:320`, `seal/follow-up.md:48`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:59`, `skills/code-review/orchestration.md:36-38`
evidence: executed `git show --stat 9e2b4c5e2`, `git reflog --date=iso -n 15`, `git grep -n -F "close block \`answer:\` of such a pass"`, `git grep -n -F "wrote the work item's last" -- ':!seal/threads'`; read `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/rounds/round-1.md:320`, `agents/crafter.md:150-173`, `skills/implement/fix-pass.md:99-120`
regression: round-1#5
```

Why it matters: the unit is the account in round 1 finding 5's `answer:`
(`trail/rounds/round-1.md:320`), which the pass added in `d0f59251b`. The
frame's *Scope* item 1 gives the orchestrator's pass the crafter's rule,
and that rule reads "every hunk of your range's diff"
(`agents/crafter.md:152`). Then it finds "the other places across the tree
that state each rule your range reworded or removed, by `git grep` on its
words" (`:167-168`). The account falls short of that in three places.

First, the account gives the method as "every hunk of `git diff
9f3bcd65f..HEAD -- skills`". `9e2b4c5e2` also changes `seal/follow-up.md`
and `changelog.md` (executed). `changelog.md` is in the records the account
read whole. The hunk of `seal/follow-up.md:48` is outside both parts of the
stated read, and finding 3 stands in that row.

Second, the sample's four phrases, "or a session's", "speak of a crafter",
"orchestrator is the implementer" and "an implementer never", come from the
rewordings of findings 1 to 3. None comes from the rule that finding 4's
fix reworded, which says where the account goes. A search on that rule's
words prints `seal/follow-up.md:48` (executed). No phrase comes from the
definition's criterion either, and a search on it prints
`skills/implement/orchestration.md:92`, the second statement of finding 1.
The account calls its list a sample, as the rule asks, but the sample
missed two of the rules the range reworded. `frame/design.md` was read whole
and folded, and the folded sentence is still wrong (finding 4).

Third, the account says that the read came "after the fix commit
`9e2b4c5e2`". It also says that the read "found `changelog.md`'s first
bullet silent on the new home of finding 4 and named it there, in
`9e2b4c5e2`". The reflog shows `9e2b4c5e2` committed once, at 07:11:28,
with no amend, and the fold `c49e96507` 25 seconds later (executed). A
correction inside the fix commit was made before that commit existed, so
either the read came before the fix commit or the correction did not come
from the read. Where a read falls against the last fix commit is the fact
the paragraph's order rests on: corrections "in its fix commits", then the
fold "in a commit of its own".

The fix is the next pass's account, written in this record's close blocks:
the hunks of every path the pass's commits touch, the sample's phrases
drawn from each rule the range rewords, and the order as the commits show
it.

```text
Method: after the last fix commit <sha>, every hunk of
`git diff <first fix>^..<last fix>` was read with the paragraph around it,
over every path it prints; routing.md, the three frame files, gaps.md and
changelog.md were read whole against HEAD. Sample: `git grep -n -F` on the
words of each rule the range reworded: <one phrase per rule>. It printed
<places>, each corrected or standing for <why>; a sentence in other words
escapes it.
```

```seal
verdict: fixed 6cb87fd8f
answer: The finding holds for round 1's pass, and this close is this pass's account, in the shape the finding gives. Round 1's account misstated one order: its correction of `changelog.md`'s first bullet was written before the fix commit `9e2b4c5e2`, in the same edit as the fixes, and not found by the read after it; the read after it found only the *Data & interfaces* sentence. That account stands in round 1's close block, which this pass does not edit. This pass: after the last fix commit `6cb87fd8f`, every hunk of `git diff 5f602858e..6cb87fd8f` was read with the paragraph around it, over every path it prints: `seal/follow-up.md`, `frame/design.md`, `frame/plan.md`, `skills/code-review/orchestration.md` and `tests/text/test_the_rules_have_one_owner.py`, the two frame files being the framer's fold `fa0693951`. Then `routing.md`, the three frame files, `gaps.md` and `changelog.md` were read whole against HEAD. The read found no statement HEAD contradicts: `changelog.md`'s "names it as the implementer where the session builds" holds under the definition's new criterion, and `frame/design.md` S4's red holds again by finding 2's case. Sample: `git grep -n -F` on the words of each rule the range reworded, with the released items' records left out: for the implementer's criterion "last commit the", "wrote the work item's last" and "the party that wrote"; for the account's homes "close block `answer:` of such" and "last close block"; for the frame's list of the diff "The diff changes" and "The diff is" (executed). Outside the round records it printed the two agreeing definitions, `skills/implement/fix-pass.md:117`, `seal/follow-up.md:48` as fixed, `skills/code-review/orchestration.md:153` and `tests/skills/test_chain_check.py:1974`, which speak of other things, and this item's frame sentences, each dated to `d399c049f` in *Grounding*, quoting the old text in *Removes*, or holding at HEAD. A sentence that states one of these rules in other words escapes the sample. Narrow set: the test files that read `skills/implement/fix-pass.md`, a `skills/*/orchestration.md` file or `seal/follow-up.md`, with `tests/test_*.py`, as one `bin/test` command: 2031 passed (executed).
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `skills/code-review/orchestration.md` holds one definition of
the implementer, at `:36-38`. The paragraph at `:55-59` no longer defines
the term, and `skills/implement/SKILL.md:22-23` reads "the crafter never
opens it, and everything below is the crafter's and the orchestrator's
alike". So `frame/design.md` *Removes* row 2 holds (read). `git grep -n -F -e
"orchestrator is the implementer" -e "an implementer never" -- ':!seal/threads'`
prints nothing (executed). It matches words on a single line, so it misses
the test comment at `tests/text/test_the_rules_have_one_owner.py:448-449`,
which wraps the phrase and which the close says stays true (read). The criterion of the rewritten definition is
finding 1 of this round, and the case's lost pin is finding 2.

```seal
confirms: round-1#2
```
What holds: the scoping clause is gone. `:58-59` reads "The orchestrator
appends the close blocks of its own pass, as `skills/implement/fix-pass.md`
*The close blocks, last* states". The ban at `:65-67` carries "where a
crafter makes the pass" at the sentence it limits, `:87` reads "A crafter's
hand-back carries", and the commit at `:105-110` binds "at the end of its
own pass where it leaves none open" (read). Read as the orchestrator in its
own pass, each act has one reading. It appends the close blocks
(`fix-pass.md:145-147`). It folds in a commit of its own before the close
blocks (`fix-pass.md:109-111`). It commits the round record alone, and
`d0f59251b` touches `trail/rounds/round-1.md` alone (executed). Read as the
crafter, nothing in its route changed (read). The opening words of both
bold leads stand, so a citation by "the paragraph opening" still resolves.

```seal
confirms: round-1#3
```
What holds: `skills/implement/SKILL.md:338` reads "A fix pass, the
crafter's or the orchestrator's, opens", and
`git grep -n -F "or a session's" -- ':!seal/threads'` prints nothing
(executed).

```seal
confirms: round-1#4
```
What holds: the framer's fold `a8dab6c96` chose `gaps.md` `## Not done` and
wrote it into *Scope* item 1's hand-back bullet (`frame/design.md:31`), S5
(`:54`), the *Data & interfaces* wording (`:63`) and `frame/plan.md` rows 1,
12 and 13 (read). `skills/implement/fix-pass.md:118-120` carries the fold's
wording word for word (read). The bullet's claim that `docs/forms/the-round-record.md`
calls this case "a fix pass no finding named" stands at `:72` there
(executed: `git grep -n -F`). Its claim that the sealer's verdict fix is
the orchestrator's stands at `skills/code-review/gate-to-pull-request.md:145-153`
(read). `templates/records/sdd-gaps.md` and `skills/implement/SKILL.md:290-294`
describe `## Not done` as "what was within reach and deliberately not
taken, with its grounds". The statements a read leaves standing, each with
why, are of that kind. The method sentence is not, and `frame/plan.md` row
12 weighs that cost against a new home. No reader acts on `## Not done` by
script (executed: `git grep -n -F "Not done" -- skills/settle agents lib docs`
prints the crafter's rule and a hint in `lib/gaps.py` alone), so that choice
is the frame's and no finding. The other statement of the fact that the fix
left standing is finding 3.

```seal
confirms: round-1#5
```
What holds: the last sentence of `seal/follow-up.md:48` names the two
mechanisms in words, and they match `frame/plan.md` rows 8 and 9 (read).
The row keeps the work item ids of the baseline, as the finding judged. The
row's other sentence is finding 3, and the account in this close is finding
5.

What matched: the records against the tree outside the fix range.
`changelog.md:3-4` and its *Process changes* row state what HEAD holds,
apart from what finding 1 says of "the implementer" (read). The two quotes
of `pr.md` stand word for word at `frame/questions.md:17`, in the *Default
until answered* cell, and at `gaps.md:12` (read). `frame/plan.md`
*Judgments of the run* records the route of round 1's findings, and the
commits follow it: the fold first, then the fix (executed:
`git log --oneline`). `trail/phases/phase-1.md:7` still describes the
scoping clause the build wrote. A phase keeps its record
(`skills/implement/fix-pass.md:144`), so it is no finding.

What matched: the fix-pass paragraph's new sentence
(`skills/implement/fix-pass.md:118-120`) is not pinned by a case. S5 says
the rounds read it, and `test_whoever_makes_the_fix_pass_makes_the_reading_of_the_range`
already holds `## Not done` through the sentence that follows it. So the
frame asks no case of it (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the suite is `unverified` here, since this round ran three modules only | `seal/config.json` `Broad gate` | the orchestrator, by its broad run after the rounds settle |
| The account's narrow set, "2384 passed", which this round did not re-run | `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/rounds/round-1.md:320` | the orchestrator, who ran it |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_docs_line_wrap.py -q -p no:xdist`, in the clone at `d0f59251b` | 100 passed, exit 0 |
| `bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k test_the_fix_pass_reads_the_implementers_context_before_it_resumes`, in the clone with `skills/code-review/orchestration.md:55-59` removed by an edit, restored after with `git checkout` | 1 passed, exit 0: the case does not go red without the paragraph |
| the section *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer* flattened, then `grep -o -F` for `` `Implementation` ``, `` `the session` `` and `*The close blocks, last*` | 2, 2 and 1 |
| `git reflog --date=iso -n 15` | `9e2b4c5e2` at 07:11:28, `c49e96507` at 07:11:53, `d0f59251b` at 07:12:31, no amend in the range |
| `git grep -n -F "close block \`answer:\` of such a pass"` | `seal/follow-up.md:48` alone |
| `git grep -n -F -e "the last commit the" -e "wrote the work item's last" -e "the party that wrote" -- ':!seal/threads'` | `skills/code-review/orchestration.md:36` and `:152`, `skills/implement/orchestration.md:92` |

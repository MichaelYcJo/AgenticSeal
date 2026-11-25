# Review round 1: 1795642930-a-session-fix-pass-reads-no-records-whole

```seal
target: fb9054e79 against origin/release/v0.39.1
```

The branch was read against `origin/release/v0.39.1` at `4e7ad2362`, over
its eight commits from `d399c049f` to `fb9054e79`, in the branch's own
checkout, which the spawn prompt names as the place the branch stands. This
is the first round, so no coordinate or verdict was carried from an earlier
one, and every fact below was established here. `seal/parity.json` is not
declared, so no parity comparison was owed. The work item's records were
each read whole at `fb9054e79`: `routing.md`, the three frame files,
`gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md`.
`seal/config.json` names English for both language keys, so no
`pr.<lang>.md` is owed and none stands. Issue #1623 was read with
`gh issue view 1623 --json title,body,comments`: it has no comment, and its
*Done when* is the bar this round reads the diff against.

The axes this change has are its own. The first is whether each new
paragraph reads one way to both of its readers, the crafter and the
orchestrator (`skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한
가지로만 읽히게 쓴다*). The second is whether every other sentence of the
tree that a fix pass opens still binds the reading, the close blocks or the
hand-back to the crafter alone. The third is whether each sentence the diff
amends was rewritten in place (contract rule 19). The fourth is whether the
records, `pr.md` and the new `seal/follow-up.md` row state the present at
HEAD and stay readable for the releases they are written for. The table's
axes of inputs, authorization, query scope, ordering, state, concurrency and
security have nothing to compare in a diff that changes procedure prose, two
text cases, a changelog fragment and a version string. No executable line
changes (read: `git diff 4e7ad2362..fb9054e79 -- lib hooks bin skills/*/scripts`
prints nothing).

The list of sentences that bind a fix pass's reading, close blocks or
hand-back to the crafter was made by one method: `git grep -n -i` on
`crafter`, `hand-back` and `implementer` over the files a fix pass opens or
is sent to, namely `skills/implement/fix-pass.md`,
`skills/implement/SKILL.md`, both `orchestration.md` files,
`skills/code-review/gate-to-pull-request.md`,
`docs/forms/the-round-record.md`, `docs/layout/the-record-layout.md`,
`templates/records/sdd-round.md` and `agents/sealer.md`, and
`git grep -n -w implementer` over `skills`, `agents`, `templates`, `docs`,
`README.md` and `CONTRIBUTING.md`. It is a search on words, so it is a
sample: a sentence that gives the crafter's part in other words escapes it.
Findings 1 to 3 are what it printed that the session route contradicts.

## Findings

### 1. The orchestrator is named the implementer beside the definition that names the crafter alone, which still stands, so `skills/implement/SKILL.md` now says the implementer never opens a file the orchestrator opens

```seal
severity: should
location: `skills/code-review/orchestration.md:36-37`, `skills/code-review/orchestration.md:54-56`, `skills/implement/SKILL.md:21-23`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:75`
evidence: executed `git grep -n -w implementer -- skills agents templates docs README.md CONTRIBUTING.md`; read `skills/code-review/orchestration.md:34-59`, `skills/implement/SKILL.md:20-23`, `skills/implement/orchestration.md:15`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:34`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:75`
```

Why it matters: `frame/design.md:75`, the second row of *Removes*, says "The
definition of the implementer as the crafter alone" in
`skills/code-review/orchestration.md` is "Rewritten in place by *Scope*
item 3". At HEAD the definition is unchanged. `skills/code-review/orchestration.md:36-37`
still says "The implementer is the crafter that wrote the last commit the
round reviewed." The build added a new paragraph at `:54-56` instead:
"Where `routing.md` answers `Implementation` with `the session`, the
orchestrator is the implementer". So the section now holds two definitions
of one term, and the reader has to choose between them. Contract rule 19
says a correction written beside the sentence it corrects leaves both for
the next reader to choose between.

The new meaning also reaches a file the diff did not open.
`skills/implement/SKILL.md:21-23` says "read
`skills/implement/orchestration.md` before the first edit; an implementer
never opens it". Under the new paragraph, an orchestrator that builds under
`the session` is an implementer, and it opens that file at step 1.
`skills/implement/orchestration.md:15` gives the same fact by role ("The
crafter opens that one at its first step and never this one"). So only the
sentence in `SKILL.md`, which uses the term, now contradicts the tree.
The other uses the search printed hold under both meanings. They are
`agents/proofer.md:90` and `:134`, `skills/agent-contract/SKILL.md:62`,
`skills/code-review/SKILL.md:27` and `:32`, `skills/implement/fix-pass.md:31`,
`docs/running/measuring-a-run.md:42`, `docs/running/the-agent-set.md:170`,
`docs/running/the-run.md:67`, `skills/verify/seal-mutate.md:11` and
`skills/verify/scripts/mutation_check.py:4`, plus the uses inside the
section at `:34-49`, which the new paragraph sets aside by name. The search
is on one word, so a sentence that uses the term in other words escapes it.

The fix rewrites the definition in place, as *Removes* says it is, and
gives `SKILL.md` the role in place of the term.

```markdown
<!-- skills/code-review/orchestration.md:36-37, the second sentence of the paragraph opening **A fix pass resumes the implementer only while** -->
otherwise.** The implementer is the party that wrote the last commit the
round reviewed: the crafter, or the orchestrator where `routing.md` answers
`Implementation` with `the session`. Before the fix pass, the orchestrator runs

<!-- skills/code-review/orchestration.md:54-56, the new paragraph, which then needs no definition of its own -->
**Where `routing.md` answers `Implementation` with `the session`, the
orchestrator makes each fix pass itself, by
`skills/implement/fix-pass.md`.** The resume threshold and the fresh spawn

<!-- skills/implement/SKILL.md:21-23 -->
`skills/implement/orchestration.md` before the first edit**; the crafter
never opens it, and everything below is the crafter's and the
orchestrator's alike.
```

The second snippet changes the bold lead that
`tests/text/test_the_rules_have_one_owner.py`'s comment at the
`Implementation` and `the session` facts describes as "the orchestrator is
the implementer". The case asserts the code spans only and stays green, and
the fix pass owes that comment and `changelog.md:4` ("names it as the
implementer where the session builds") the same check. Both stay true if
the definition at `:36-37` carries the orchestrator, as the first snippet
writes.

```seal
verdict: fixed 9e2b4c5e2
answer: The finding holds. `skills/code-review/orchestration.md` now defines the implementer once, in place, in the paragraph opening **A fix pass resumes the implementer only while**: "the party that wrote the last commit the round reviewed: the crafter, or the orchestrator where `routing.md` answers `Implementation` with `the session`". The paragraph opening **Where `routing.md` answers `Implementation` with `the session`** no longer defines the term. `skills/implement/SKILL.md`'s opening now reads "the crafter never opens it, and everything below is the crafter's and the orchestrator's alike", the snippet's wording. So `frame/design.md` *Removes* row 2, "Rewritten in place", holds at HEAD. The test comment at the `Implementation` and `the session` facts of `tests/text/test_the_rules_have_one_owner.py` and `changelog.md`'s "names it as the implementer where the session builds" both stay true under the definition in place, as the finding says, so neither changed (read). `git grep -n -F -e "orchestrator is the implementer" -e "an implementer never"` outside the records prints nothing at HEAD (executed).
```

### 2. The close-block ban and the round record's commit are scoped from a paragraph above them, not amended where they stand, and which paragraphs the scope reaches has two readings

```seal
severity: should
location: `skills/code-review/orchestration.md:56-59`, `skills/code-review/orchestration.md:65-66`, `skills/code-review/orchestration.md:86`, `skills/code-review/orchestration.md:104-108`
evidence: executed `git grep -n -F "writes no close block of a finding the fix pass answers"`, `git grep -n -F "On the hand-back that leaves no"`; read `skills/code-review/orchestration.md:54-108`, `skills/implement/fix-pass.md:121-146`, `docs/forms/the-round-record.md:95-100`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/phases/phase-1.md:7`
```

Why it matters: the phase record names one sentence written beyond the
frame's wording, inside *Scope* item 3 (`trail/phases/phase-1.md:7`). The
sentence is at `skills/code-review/orchestration.md:56-59`: "the
orchestrator appends the close blocks as the pass, so the paragraphs below
that leave the close blocks and the hand-back to the crafter speak of a
crafter's pass". The phase record is right that something was owed. Without
it, the bold lead at `:65-66`, "The orchestrator writes no close block of a
finding the fix pass answers", forbids the close blocks of the
orchestrator's own pass, which `skills/implement/fix-pass.md:143-145` has
whoever makes the pass append. The sentence is wrong in its form, though,
and that causes two defects.

First, the ban at `:65-66` still stands as written, with no condition. A
reader who opens the paragraph by its bold lead, as the frame of
`1795595957-the-next-round-is-a-fixs-first-reader` cites it
(`frame/design.md:51` there), reads the unconditioned ban. Contract rule 19
asks for the condition at the sentence it limits.

Second, the reach of "the paragraphs below that leave the close blocks and
the hand-back to the crafter" can be read two ways. Only `:61-72` names the
crafter. The paragraph at `:83-108` never names the crafter, but it speaks
of "The fix pass's hand-back" (`:86`). If it is in the scope, then its last
sentence (`:104-108`) speaks of a crafter's pass only. That is the sentence
that has the orchestrator commit the round record "in one commit for the
whole pass, before it reads whether a round follows the pass", holding
`trail/rounds/round-N.md` alone. If it is out, that sentence is triggered
"On the hand-back that leaves no finding open for a fold", and the
orchestrator's own pass has no hand-back to trigger it. So in the session
route, under either reading, nothing in this file binds the orchestrator to
the commit's shape. `skills/implement/fix-pass.md:145` says only "the
orchestrator commits the round record as the pass left it". It says neither
that the commit holds that file alone nor when the commit falls against the
chain check's read at `:139-142`.

The fix removes the scoping clause and gives each sentence it was meant to
limit its own condition. The opening words of both bold leads stay as they
are, so a citation by "the paragraph opening" still resolves.

```markdown
<!-- skills/code-review/orchestration.md:56-59 -->
above do not apply. The orchestrator appends the close blocks of its own
pass, as `skills/implement/fix-pass.md` *The close blocks, last* states.

<!-- skills/code-review/orchestration.md:65-66 -->
**The orchestrator writes no close block of a finding the fix pass answers
where a crafter makes the pass, and its fix-pass prompt leaves every such
block to the crafter.** A close the

<!-- skills/code-review/orchestration.md:86 -->
a later round; that is contract rule 12. A crafter's hand-back carries

<!-- skills/code-review/orchestration.md:104-107 -->
threshold above. **On the hand-back that leaves no finding open for a
fold, and at the end of its own pass where it leaves none open, the
orchestrator commits the round record as the fix pass left it, in one
commit for the whole pass, before it reads whether a round follows the
pass, and changes none of its lines.** That commit holds
```

`docs/forms/the-round-record.md:99-100` also has the orchestrator take the
round record "from the hand-back". That file is under `docs/`, and
`frame/design.md` *Scope*, Out, leaves its crafter-route sentences to the
settle. So this finding does not ask for that change. It names that file as
the one place the search printed and the snippet does not reach.

```seal
verdict: fixed 9e2b4c5e2
answer: The finding holds. The scoping clause is gone: the paragraph opening **Where `routing.md` answers `Implementation` with `the session`** now ends "The orchestrator appends the close blocks of its own pass, as `skills/implement/fix-pass.md` *The close blocks, last* states." The ban's bold lead carries its condition where it stands, "where a crafter makes the pass", the hand-back sentence reads "A crafter's hand-back carries", and the round record's commit binds "On the hand-back that leaves no finding open for a fold, and at the end of its own pass where it leaves none open", each the snippet's wording, with the opening words of both bold leads kept. `git grep -n -F "speak of a crafter"` outside the records prints nothing at HEAD (executed). `docs/forms/the-round-record.md:99-100` stays, as the finding asks, for the settle (`frame/design.md` *Scope*, Out). `trail/phases/phase-1.md` still describes the clause as the phase built it; the phase keeps its record (`skills/implement/fix-pass.md` *The close blocks, last*).
```

### 3. `skills/implement/SKILL.md` *5* calls the orchestrator's pass "a session's", and the file it sends that pass to now calls it the orchestrator's

```seal
severity: should
location: `skills/implement/SKILL.md:338`
evidence: executed `git grep -n -F "or a session's" -- ':!seal/threads'`; read `skills/implement/SKILL.md:20-23`, `skills/implement/SKILL.md:336-342`, `skills/implement/fix-pass.md:3-9`, `skills/writing-style/SKILL.md:275-279`
```

Why it matters: `skills/implement/fix-pass.md:4-8` now says "A fix pass is
the crafter's or the orchestrator's", and that "The orchestrator opens it
from `skills/implement/SKILL.md` *5. Incorporate review — read the round
records first*". The section it cites, at `skills/implement/SKILL.md:338`,
still says "A fix pass, the crafter's or a session's, opens
`skills/implement/fix-pass.md`". The diff rewrote the same fact in
`fix-pass.md`'s opening, which said "a session that fixes review feedback
opens it", and left the copy in `SKILL.md`. Contract rule 19 asks that
every sentence stating the fact be rewritten in the same commit.
`skills/implement/SKILL.md:22-23` says the file is "the implementer's and
the orchestrator's alike", so two parties open it.
`skills/writing-style/SKILL.md:275-279` says such a file names its actor by
role and never writes "the session", because the word reads as either
party. `frame/design.md` G6 applied that rule to `fix-pass.md` and G3 cites
this sentence, but *Scope* does not take it in. The search printed this one
line outside the records.

```markdown
<!-- skills/implement/SKILL.md:338 -->
A fix pass, the crafter's or the orchestrator's, opens
```

```seal
verdict: fixed 9e2b4c5e2
answer: The finding holds. `skills/implement/SKILL.md` *5. Incorporate review* now reads "A fix pass, the crafter's or the orchestrator's, opens", the snippet's wording. `git grep -n -F "or a session's" -- ':!seal/threads'` prints nothing at HEAD (executed).
```

### 4. The read's account has no home in the orchestrator's fix after the last round, the second case the paragraph names, where the pass appends no close block

```seal
severity: should
location: `skills/implement/fix-pass.md:113-118`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:31`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:54`
evidence: read `skills/implement/fix-pass.md:99-118`, `skills/code-review/orchestration.md:74-81`, `skills/code-review/gate-to-pull-request.md:150-153`, `docs/forms/the-round-record.md:64-73`, `skills/code-review/SKILL.md:162-163`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/plan.md:27`
```

Why it matters: `skills/implement/fix-pass.md:102-106` gives the
orchestrator the reading in two cases: every pass under `the session`, and
"in every route ... the fix it writes after the last round".
`skills/code-review/orchestration.md:79-81` sends that second fix to the
same paragraph. The paragraph's mapping of the hand-back then says the
account goes "into the `answer:` of the close block of the finding they
concern, and otherwise into the `answer:` of the last close block the pass
appends" (`fix-pass.md:113-117`). A fix written after the last round often
closes no finding. One example is the fix for a sealer's verdict that the
core's row gives to a round (`skills/code-review/gate-to-pull-request.md:150-153`).
The form names that case "a fix pass no finding named"
(`docs/forms/the-round-record.md:66-72`, `skills/code-review/SKILL.md:162-163`).
Such a pass appends no close block, so the method of the read, the
statements it left standing and where a sample stopped have nowhere to go.
`frame/plan.md:27`, row 5 of *Alternatives considered*, rejected the next
round's spawn prompt as that home, because a prompt is no record. So an
orchestrator that makes this read can either write it nowhere, or write it
into the prompt the frame rejected. S5 (`frame/design.md:54`) says the
orchestrator "makes the same reading" and names no home for its account.
*Scope* item 1's hand-back bullet (`frame/design.md:31`) has the same gap,
so the gap starts in the frame, and the build followed it.

The home is a design decision, so it is the framer's fold. Here is one
candidate the fold can weigh. It uses a record the orchestrator already
writes, and leaves the frame to choose:

```markdown
<!-- skills/implement/fix-pass.md:113-118, the hand-back mapping -->
ticket* states. That rule's hand-back stands for the close blocks. The
method of the read, each statement across the tree the read leaves
standing with why, and where the part a sample did not reach stands go
into the `answer:` of the close block of the finding they concern, and
otherwise into the `answer:` of the last close block the pass appends.
Where the pass appends no close block, because no finding names its fix,
they go into the row of `frame/plan.md` *Judgments of the run* that
records the fix.   # NAME NOT IN TREE: no rule yet says such a fix takes a row
What the pass did not finish goes to `gaps.md` `## Not done`.
```

The snippet is one candidate, not the fold's wording. *Scope* item 1's
bullet and S5 owe the same home, and the fold writes them.

```seal
verdict: fixed 9e2b4c5e2
answer: The finding holds, and its home went to the framer's fold first, at `a8dab6c96`, which chose `gaps.md` `## Not done` and wrote the candidate row of *Judgments of the run* and the removal of the second case as rows 12 and 13 of `frame/plan.md` *Alternatives considered*, with *Scope* item 1 and S5 naming the home. `skills/implement/fix-pass.md` *The narrow set, then the read of the range* now adds, after the close-block mapping, "Where the pass appends no close block, because no finding names its fix, they go into `gaps.md` `## Not done`. What the pass did not finish goes to `gaps.md` `## Not done` too.", the fold's wording. `changelog.md`'s first bullet names the same home.
```

### 5. The new `seal/follow-up.md` row says where the weighing begins by pointing at rows of this work item's `frame/plan.md`, which the settle deletes before the row is read

```seal
severity: should
location: `seal/follow-up.md:48`
evidence: executed `grep -n "frame/plan.md\|frame/design.md" seal/follow-up.md`, `grep -n "remove" skills/settle/SKILL.md`; read `seal/follow-up.md:38-48`, `skills/settle/SKILL.md:8`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/plan.md:30-31`
```

Why it matters: the row is for "the releases after 0.39.1". It ends "the
orchestrator weighs a mechanism for the read, beginning with the rejected
rows 8 and 9 of #1623's `frame/plan.md` *Alternatives considered*". The
settle writes each released item's decisions and then "remove[s] their
directories" (`skills/settle/SKILL.md:8`). So by the time a later release
reads the row, the file it points at is gone, and only git history holds
it. The search printed this row as the only one in the file that cites a
work item's frame. The other rows name a mechanism in words, as the row
above names "a `PreToolUse` hook on the orchestrator's `Agent` call ...
which #1614 weighed and rejected". The coordinates of the earlier findings
the row counts, round 2 of `1794797697-a-census-cell-states-an-impossible-result`
and of `1794986401-the-process-has-no-name`, leave with their directories
too. They are a dated baseline, and a reader recovers them from git by the
item ids the row gives. That is why this finding asks only for the
instruction a reader acts on.

```markdown
<!-- seal/follow-up.md:48, the row's last sentence -->
Where findings of that kind recur under the released text, the orchestrator weighs a mechanism for the read, beginning with the two #1623 rejected: `hooks/edit-leaves-copies.py` widened to search the item's records for the words any `Edit` replaced, and a `Stop` hook of type `prompt` or `agent` that asks, when a pass ends, whether the session read its records whole | the repository owner |
```

```seal
verdict: fixed 9e2b4c5e2
answer: The finding holds. The row's last sentence now names the two rejected mechanisms in words, the snippet's wording, and keeps the work item ids of the baseline as the finding judged. The account of this pass's reading, which `skills/implement/fix-pass.md` *The narrow set, then the read of the range* asks of the orchestrator's pass and places in the last close block where it concerns no one finding. Method: after the fix commit `9e2b4c5e2`, every hunk of `git diff 9f3bcd65f..HEAD -- skills` was read with the paragraph around it, and `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md` and `changelog.md` were read whole against HEAD. The read found one frame sentence HEAD contradicts: `frame/design.md` *Data & interfaces* listed three files of procedure text, and the fix changed `skills/implement/SKILL.md` too. The orchestrator folded it at `c49e96507` by narrowing the sentence to "procedure text in `skills/`". It found `changelog.md`'s first bullet silent on the new home of finding 4 and named it there, in `9e2b4c5e2`. The tree-wide sample was `git grep -n -F` over `or a session's`, `speak of a crafter`, `orchestrator is the implementer` and `an implementer never` (executed). Outside this item's records it printed only the records of `1794352646-a-phase-spawn-preloads-the-fix-pass-procedure` and `1794362365-the-definitions-restate-the-contract`. Those are dated records of released items, which the settle removes, so they stand. The sample is on words, so a sentence that gives the crafter's part in other words escapes it. The sentences of `docs/` that describe the crafter's route stay for the settle, as `frame/design.md` *Scope*, Out, says. Narrow set: the test files that read a changed path, by `git grep -l -e 'fix-pass' -e 'orchestration.md' -e 'implement/SKILL.md' -e '"SKILL.md"' -e 'follow-up.md'` over the test files, with `tests/test_*.py`, as one `bin/test` command: 2384 passed (executed).
```

## Confirmations

What matched: *Scope* item 1. `skills/implement/fix-pass.md:99-119` binds
the reading to "whoever makes the pass, the crafter or the orchestrator".
It keeps `agents/crafter.md` *Before you hand back, your range and the work
item's records are read whole against HEAD* as the rule's one home, maps
the *Job* to the orchestrator's corrections in its range, `gaps.md` and
`changelog.md`, maps the frame and `routing.md` statements to a fold in a
commit of its own, and maps the hand-back to `answer:` and `gaps.md`
`## Not done` (read). Read as the crafter, the paragraph changes nothing
the crafter does. Its mapping is conditioned on "In the orchestrator's
pass", and `agents/crafter.md` is not in the diff
(`git diff --stat 4e7ad2362..fb9054e79`, executed). Read as the
orchestrator, every act has an actor, a file and a point in the pass, apart
from the gap finding 4 names. The text drops the frame's "after its fix
commits" from the fold's place (`frame/design.md:30`). The reading the
paragraph opens with already falls after the fix commits, so the order
holds. *Scope* item 1 also says the paragraph "calls both cases of the rule
rather than its limit". The text does not say so in words, but
the framer's own wording in *Data & interfaces* (`frame/design.md:63`) does
not either, and the bold lead binds "whoever makes the pass", so no
reader takes the two cases as the bound. The issue's *Done when* is met in
`fix-pass.md` itself (read against `gh issue view 1623`).

What matched: *Scope* item 2. `skills/implement/fix-pass.md:3-18` names
both parties, gives the routing row as the case where the orchestrator
makes every pass, and maps the stop's hand-back at `:79-84` to the
orchestrator sending the finding to the framer before the pass that builds
the unit. That act is the one `skills/implement/orchestration.md:72-74`
gives it on a crafter's hand-back (read). It is S3, which no case pins, as
the frame says.

What matched: *Scope* item 4. `skills/implement/orchestration.md:91-96`
names the crafter, and the orchestrator under `the session`, as the party
the fix pass goes to (read). *Removes* rows 1 and 3 hold at HEAD (read).

What matched: *Scope* items 5 and 6. The new case
`test_whoever_makes_the_fix_pass_makes_the_reading_of_the_range` asserts
code spans and a cited section, not wording. The two facts added to
`test_the_fix_pass_reads_the_implementers_context_before_it_resumes` stand
only in the new paragraph of that section (read). Both modules and the
line-wrap case pass (executed, *Probes*). The phase record's red runs were
not re-run. Read against its group, the new case covers a section that no
other case of `tests/text/test_a_moved_rule_leaves_its_definition.py`
reads, so it adds coverage. Its docstring says the paragraph "says where
the orchestrator corrects, folds and names", but no assertion holds the
correction targets `changelog.md` or "corrects". That docstring, at
`tests/text/test_a_moved_rule_leaves_its_definition.py:278-285`, claims a
little more than the case pins. `.claude-plugin/plugin.json:4` reads
`0.39.1` in `202d76813`, the commit that adds `changelog.md` (executed:
`git show --stat 202d76813`).

What matched: the records against the tree. `changelog.md:3-4` and its
*Process changes* row state what HEAD holds. Finding 1 bears on the word
"implementer" in `changelog.md:4`. The two quotes of `pr.md` stand word for
word at `frame/questions.md:17`, in the *Default until answered* cell, and
at `gaps.md:12` (read). `trail/phases/phase-1.md:5` names the commits that
`git log` shows for the text and the changelog. Its *Phase boundary* line
names the `gaps.md` that `c5cd456e8` adds (executed: `git show --stat
c5cd456e8`). The `seal/follow-up.md` row's counts were re-read with
`frame/design.md` G8's command at HEAD. Round 2 findings 1 and 2 of
`1794797697-a-census-cell-states-an-impossible-result` and findings 1 to 4
of `1794986401-the-process-has-no-name` carry `regression:` lines and
record locations, and both items answer `Implementation` with `the session`
(executed). Finding 2 of the second item also names a test file, as G8
says. Owlery #236 says what `changelog.md:3` says of it (executed:
`gh issue view 236 -R MichaelYcJo/owlery --json title,body`).

What matched: the other statements the search printed. They are
`skills/code-review/gate-to-pull-request.md:77`,
`docs/layout/the-record-layout.md:56-57` and `:73`,
`skills/implement/orchestration.md:72-74`, `:107` and `:390-391`, and
`agents/sealer.md:95`. Each already names both parties, or acts on a
hand-back that `fix-pass.md:12-18` now maps, so none contradicts the
session route (read). `docs/forms/the-round-record.md:3`, "the crafter
closes its findings", is a sentence of the crafter's route that
`frame/design.md` *Scope*, Out, leaves to the settle, and the orchestrator
opens that form only at the two paragraphs `fix-pass.md:128-132` cites.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the suite is `unverified` here, since this round ran three modules only | `seal/config.json` `Broad gate` | the orchestrator, by its broad run after the rounds settle |
| The red runs of *Scope* item 5, which the phase record reports as executed and this round did not repeat | `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/phases/phase-1.md:6` | the orchestrator, who ran them; the next round re-runs them only where a fix touches either case |
| Owlery pull request MichaelYcJo/owlery#259, which `frame/design.md` G9 cites in a section dated to `d399c049f`; this round opened the issue and not the pull request | `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:17` | the framer's reading at `d399c049f` stands; nobody owes more for this work |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_docs_line_wrap.py -q -p no:xdist` | 100 passed, exit 0 |
| `git grep -n -w implementer -- skills agents templates docs README.md CONTRIBUTING.md` | 26 lines; the uses finding 1 lists, and `skills/implement/SKILL.md:22` as the one the session route contradicts |
| `git grep -n -F "or a session's" -- ':!seal/threads'` | `skills/implement/SKILL.md:338` alone |
| `git grep -n -F "writes no close block of a finding the fix pass answers"` and `git grep -n -F "On the hand-back that leaves no"` | `skills/code-review/orchestration.md:65` and `:104`, and citations of both bold leads in `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/` |
| `grep -n "^regression:\|^reopens:\|^location:\|^### " seal/threads/<id>/trail/rounds/round-2.md` for the two items the follow-up row names | the six `regression:` findings that row counts, at the locations above |

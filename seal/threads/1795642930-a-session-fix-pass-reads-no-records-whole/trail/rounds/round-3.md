# Review round 3: 1795642930-a-session-fix-pass-reads-no-records-whole

```seal
target: 237a8a127, fixes d0f59251b..237a8a127
```

This is a verifying round over the fix range `d0f59251b..237a8a127`. The
range holds four commits: the round 2 record `5f602858e`, the framer's fold
`fa0693951` for round 2 finding 4, the orchestrator's fix `6cb87fd8f`, and
the close blocks in `237a8a127`, which touches `trail/rounds/round-2.md`
alone (executed: `git show --stat` on each). The code the round reviews is
that range's diff outside the round record: `seal/follow-up.md:48`,
`skills/code-review/orchestration.md:36-39`,
`tests/text/test_the_rules_have_one_owner.py:448-455`, and the fold's two
frame sentences. The round read in the branch's own checkout and probed in
a `git clone --no-local` at `237a8a127` under the round's scratch
directory. `seal/parity.json` is not declared, so no parity comparison was
owed.

The work item's records were each read whole at `237a8a127`: `routing.md`,
the three frame files, `gaps.md`, `changelog.md`, `pr.md`,
`trail/phases/phase-1.md`, and `trail/rounds/round-1.md` and
`trail/rounds/round-2.md` for their coordinates. `seal/config.json` names
English for both language keys, so no `pr.<lang>.md` is owed and none
stands. Issue #1623 was read with `gh issue view 1623 --json body,comments`.
It has no comment, and its *Done when* is met at
`skills/implement/fix-pass.md:99-120`, which this range does not change
(read).

Carried from rounds 1 and 2 and not established again: that no executable
line changes, the reading of G8's measurement and of Owlery #236, and the
red runs of the phase record. Re-derived here: every close of round 2, the
code of the fix range, and each sentence of the records against
`237a8a127`.

The spawn asked the round to weigh whether this pass's reading reached its
whole range and each rule the range reworded. The account stands in round
2 finding 5's `answer:` (`trail/rounds/round-2.md:275`). Its sample now
draws one or more phrases from each rule the range reworded, and the round
found no statement it missed (finding 2 gives the search). Its read did not
happen as the account states it. The orchestrator's session transcript
lists each command the pass ran, and after the last fix commit none of
them read the six files whole or printed every hunk in full. Finding 2 is
that account. Finding 1 is a case that the new definition of the
implementer still reads two ways.

## Findings

### 1. The new criterion for the implementer counts the fix the orchestrator writes after the last round, so in a crafter route after that fix the head names the orchestrator and the list names the crafter

```seal
severity: should
location: `skills/code-review/orchestration.md:36-39`, `skills/implement/orchestration.md:91-96`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/design.md:35`
evidence: executed `git grep -n -F -e "last build or fix" -e "wrote the work item's last" -e "build or fix commit" -- ':!seal/threads'`, `grep -rn -F "last build or fix" seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/`; read `skills/code-review/orchestration.md:34-60`, `skills/code-review/orchestration.md:76-83`, `skills/implement/fix-pass.md:99-106`, `skills/code-review/gate-to-pull-request.md:141-155`, `docs/layout/the-record-layout.md:69-75`, `skills/implement/orchestration.md:61-96`
reopens: round-2#1
```

Why it matters: round 2 finding 1's close does not hold in one case. That
finding said that under a crafter route the head of the definition names
the orchestrator while its list names the crafter. The fix `6cb87fd8f`
changed the head to "the party that wrote the work item's last build or
fix commit". That fixes the general case, because the round record's commit
and `pr.md`'s commit are no build or fix commit. It leaves the case in
which the orchestrator itself writes the last fix commit under a crafter
route. The close's search found that the two definitions agree. They agree
because both carry that case.

The case is reachable in every route. The orchestrator writes the fix after
the last round (`skills/code-review/orchestration.md:76-83`,
`docs/layout/the-record-layout.md:73-75`), and
`skills/implement/fix-pass.md:102-106` treats that fix as the
orchestrator's pass. Where the core's row gives the fix of a sealer's
verdict to a round, the orchestrator commits it and spawns "a verifying
round on its diff" (`skills/code-review/gate-to-pull-request.md:151-153`).
A finding of that round opens a fix pass. The work item's last build or
fix commit is then the orchestrator's, so the head names the orchestrator.
The route is `crafter`, so the list names the crafter alone. The next
sentence has the orchestrator run
`seal cost --segments <the implementer's agent-*.jsonl>` on the
implementer's transcript, and the orchestrator has no such file. The
paragraph at `:56-60` gives the orchestrator its own passes only under
`the session`. So the orchestrator can read the definition two ways: make
the pass itself, or resume the crafter.

`skills/implement/orchestration.md:91-96` carries the same head and the
same list, and the frame's *Scope* item 4 (`frame/design.md:35`) states
them. Round 2 named that statement as the one without the defect, and the
fix copied it. *Scope* item 3 asks the section to state the implementer
under `the session` and does not decide this case. The search on the
criterion's words printed `skills/code-review/orchestration.md:36` and
`skills/implement/orchestration.md:92` outside the records. In this item's
records it printed `frame/design.md:35`, the *Removes* row at `:76` that
quotes the old text, and round 2's own record. No case pins the criterion
(executed: the first command over `tests` and `evals` prints nothing). It is
a search on words, so it is a sample. It reaches `:36` only because one of
its phrases ends before the line break there.

Which party makes the pass in that case is a decision the frame does not
hold, and *Scope* item 4 states the criterion. So the finding goes to the
framer's fold before the fix pass, as a round finding located in a frame
file (`skills/implement/orchestration.md:61-74`). The snippets take the
crafter, because the route names it and the threshold reads a crafter's
transcript. Where the fold decides for the orchestrator, the second
sentence of the first snippet changes with it. The second statement
becomes a citation of the first, so the criterion has one home.

```markdown
<!-- skills/code-review/orchestration.md:36-39 -->
otherwise.** The implementer is the orchestrator where `routing.md` answers
`Implementation` with `the session`. In every other route it is the crafter
that made the work item's last build phase or fix pass, also where a fix
the orchestrator wrote after the last round came later. Before the fix
pass, the orchestrator runs
```

```markdown
<!-- skills/implement/orchestration.md:91-96 -->
orchestrator spawns the next round or phase. The fix pass is the
implementer's, as `skills/code-review/orchestration.md` *Orchestrator: a
phase is a fresh crafter, and a fix pass resumes the implementer* defines
it: the crafter, resumed or spawned fresh, or the orchestrator where
`routing.md` answers `Implementation` with `the session`.
```

```markdown
<!-- frame/design.md:35, Scope item 4, the framer's fold -->
4. **`skills/implement/orchestration.md:89-94` names who makes the fix pass that a statement found in `gaps.md` or `changelog.md` goes to.** It is the implementer that item 3's section defines: the crafter, resumed or spawned fresh as that section states, or the orchestrator where `routing.md` answers `Implementation` with `the session`.
```

### 2. The account of this pass's read states that every hunk was read and six files were read whole, and the pass's commands after the last fix commit did neither

```seal
severity: should
location: `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/rounds/round-2.md:275`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/rounds/round-2.md:210`
evidence: executed a listing of the `tool_use` entries of the orchestrator's session transcript `/Users/x/.claude/projects/<project>/<session>.jsonl` timestamped from 22:20:29Z to 22:22:38Z (07:20:29 to 07:22:38 +0900), `git reflog --date=iso -n 12`, `awk 'NR==48' seal/follow-up.md | grep -b -o "and its \`gaps.md\`"`, `awk 'NR==49' seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/plan.md | grep -b -o "The diff changes files"`; read `agents/crafter.md:150-173`, `skills/implement/fix-pass.md:95-120`, `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/frame/plan.md:17`
reopens: round-2#5
```

Why it matters: round 2 finding 5's close does not hold. That close says
it is this pass's account "in the shape the finding gives". The shape
holds, and the read it describes was not made. The account says: "after
the last fix commit `6cb87fd8f`, every hunk of `git diff
5f602858e..6cb87fd8f` was read with the paragraph around it, over every
path it prints", the five paths named. It then says that "`routing.md`, the
three frame files, `gaps.md` and `changelog.md` were read whole against
HEAD" (`trail/rounds/round-2.md:275`). The rule the account answers to
asks for exactly those two reads after the last commit
(`agents/crafter.md:151-155`).

The transcript lists three commands between the fix commit at 07:21:57
and the close-block commit at 07:22:38, and the reflog agrees with those
two times (executed). The first is
`git diff --stat 5f602858e..6cb87fd8f; git diff 5f602858e..6cb87fd8f -U6 -- seal/follow-up.md seal/threads/*/frame | cut -c1-400`.
The second is the `git grep` sample, followed by
`grep -n 'implementer\|answer:\|Not done'` over `changelog.md` and
`gaps.md`, cut to 200 columns. The third is the script that wrote the close
blocks. So the account's read falls short in three ways.

- Two of the five paths' hunks, `skills/code-review/orchestration.md` and
  `tests/text/test_the_rules_have_one_owner.py`, were not printed after
  the commit. The pass printed the definition's lines once, with `sed -n
  34,40p`, after its edit and before the commit. It never printed the
  test hunk back.
- The two hunks it printed were cut at column 400. The changed words of
  `seal/follow-up.md:48` begin at byte 628, and those of
  `frame/plan.md:49` at byte 451 (executed). So neither changed sentence
  reached the reader.
- No command read any of the six files whole after the commit. The
  orchestrator never read the two frame files the framer folded at all.
  The fold reached it as the framer's hand-back, and it committed the fold
  at 07:21:22 with `git add` and `git commit` alone.

For the same reason, round 2 finding 4's close labels the fold's wording
of `frame/plan.md` *Operational impact* "(read)"
(`trail/rounds/round-2.md:210`). The orchestrator had that wording only
from the framer's hand-back. Contract rule 4 keeps `read` for what was
read.

This round read the six files whole and every hunk in full. It found no
statement in them that HEAD contradicts and that the pass left standing.
Finding 1's frame sentence agrees with HEAD, so it is not what that read
looks for. The defect is the account, not a missed statement, and it still
matters. `frame/plan.md:17` names the failure this work expects in six
months: an account that "names no method, so the next round cannot tell a
read made from one skipped". This account names a method and claims a read
that was skipped. The sealer reads the account at step 4, and the
`seal/follow-up.md:48` row would count it as a read made. The narrow set
also ran at 07:21:53, before the fix commit, over the uncommitted tree
that the commit then took unchanged. That order differs from
`skills/implement/fix-pass.md:95` and the tree does not, so it is no part
of the finding.

The fix is the next pass's account, written in this record's close blocks.
It states only the reads its commands made, and it makes the two the rule
asks for. The close carries a `location:` line of its own for the path its
commit touches (`docs/forms/the-round-record.md:55`).

```text
Method: after the last fix commit <sha>, `git diff <first fix>^..<last fix>`
was printed with no column cut, over every path it prints, and each hunk
was read with its paragraph. routing.md, the three frame files, gaps.md and
changelog.md were each opened whole at HEAD (read), a file a fold changed
among them. A part the pass held from its own edit and did not print again
is named as such. Sample: `git grep -n -F` on the words of each rule the
range reworded: <one phrase per rule>. It printed <places>, each corrected
or standing for <why>; a sentence in other words escapes it.
```

## Confirmations

```seal
confirms: round-2#2
```
What holds: `test_the_fix_pass_reads_the_implementers_context_before_it_resumes`
pins "`skills/implement/fix-pass.md` *The close blocks, last*"
(`tests/text/test_the_rules_have_one_owner.py:452-455`). With only the
paragraph at `skills/code-review/orchestration.md:56-60` removed, the case
failed on that fact's line (executed, *Probes*). The section holds that
citation once and each routing fact twice (executed), so the new comment's
claim that only that paragraph cites it holds. The comment at `:448-449`
no longer claims that the routing facts pin the paragraph. S4
(`frame/design.md:53`) is verified "with the facts of *Scope* item 5, seen
red with only *Scope* item 3's sentence removed". *Scope* item 3's text now
stands in the definition at `:36-38` and in the paragraph at `:56-60`.
With both removed, the facts *Scope* item 5 names go red, and with the
paragraph alone removed, the new fact goes red. So S4 reads true either way
(read).

```seal
confirms: round-2#3
```
What holds: `seal/follow-up.md:48` reads "each close block `answer:` of
such a pass, and its `gaps.md` `## Not done` where it appends no close
block, for whether it names the method of the read", the snippet's wording
(read). `git grep -n -F -e "close block \`answer:\` of such" -e "last close block" -- ':!seal/threads'`
prints that row and `skills/implement/fix-pass.md:117` alone (executed),
and the two agree on both homes.

```seal
confirms: round-2#4
```
What holds: `frame/design.md:59` no longer lists the diff, and the
paragraph reads as the snippet gives it (read). The fold also narrowed
`frame/plan.md:49` to "files that `docs/layout/the-record-layout.md` *A
change writes fragments, never a shared file* lists,
`skills/implement/fix-pass.md` among them", and that section lists
`skills/implement/fix-pass.md` at `docs/layout/the-record-layout.md:52`
(read). The fold was the framer's. The transcript shows the orchestrator
resuming the framer with the decision at 07:20:29 and the framer's
hand-back at 07:21:12 (executed). The row of `frame/plan.md` *Judgments of
the run* cites the paragraph opening **The framer writes a decision's
fold**. That paragraph stands at `skills/implement/orchestration.md:76`
and gives "the framer's, of a round finding that says a frame sentence no
longer holds" (read). The commits follow the row: the fold `fa0693951`
before the fix `6cb87fd8f` (executed: `git log --oneline`). The `(read)`
label in this close is part of finding 2.

What matched: the records against the tree. `changelog.md:3-4` and its
*Process changes* row state what HEAD holds: the orchestrator makes each
fix pass itself under `the session`, with no threshold and no spawn, and
appends the close blocks (read). The two quotes of `pr.md` stand word for
word at `frame/questions.md:17`, in the *Default until answered* cell, and
at `gaps.md:12` (read). `routing.md`, `frame/questions.md` and `gaps.md`
did not change in the range, and each still holds at HEAD (read). The
framer's hand-back named two frame sentences it left standing:
`frame/plan.md:7`, dated to `d399c049f` in its section, and S2's
"`agents/crafter.md` is not in the diff", which `git diff --stat
4e7ad2362..237a8a127` still bears out (executed). `trail/phases/phase-1.md:6-7`
describes the build's pins and its scoping sentence as they stood then. A
phase keeps its record (`skills/implement/fix-pass.md:143-144`), so it is
no finding.

What matched: the docstring of the case that the range extended
(`tests/text/test_the_rules_have_one_owner.py:430-434`) lists four of the
facts the case holds and none of #1623's. It claims less than the case
pins, not more, so it misleads no reader of the case (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the suite is `unverified` here, since this round ran three modules only | `seal/config.json` `Broad gate` | the orchestrator, by its broad run after the rounds settle |
| The account's narrow set, "2031 passed", which this round read in the transcript and did not re-run | `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/rounds/round-2.md:275` | the orchestrator, who ran it |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_docs_line_wrap.py -q -p no:xdist`, in the clone at `237a8a127` | 100 passed, exit 0 |
| `bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k test_the_fix_pass_reads_the_implementers_context_before_it_resumes`, in the clone with `skills/code-review/orchestration.md:56-60` removed by an edit, restored after with `git checkout` | 1 failed, exit 1, at `:457` on "`skills/implement/fix-pass.md` *The close blocks, last*" |
| the section *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer* flattened, then a count of `` `Implementation` ``, `` `the session` `` and "`skills/implement/fix-pass.md` *The close blocks, last*" | 2, 2 and 1 |
| the `tool_use` entries of the orchestrator's session transcript from 22:20:29Z to 22:22:38Z, listed by timestamp | the fold committed at 07:21:22 with no read of the folded files; the edit and the red run at 07:21:22 and 07:21:29; the narrow set at 07:21:35, `2031 passed`; the fix commit at 07:21:57; then the cut `git diff`, the sample, and the close blocks' script |
| `awk 'NR==48' seal/follow-up.md \| grep -b -o "and its \`gaps.md\`"`; `awk 'NR==49' <frame/plan.md> \| grep -b -o "The diff changes files"` | byte 628 and byte 451 |
| `git grep -n -F -e "last build or fix" -e "wrote the work item's last" -e "build or fix commit" -- ':!seal/threads'` | `skills/code-review/orchestration.md:36`, `skills/implement/orchestration.md:92` |

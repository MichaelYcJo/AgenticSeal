# Review round <N>: <work-item-id>

<!-- seal/specs/<unix-epoch-seconds>-<slug>/rounds/round-<N>.md holds what one
review round reviewed, what it found, and what answered it. The warden writes
this file in the branch worktree under review; the smith's fix pass rewrites
each finding's `verdict:` line and writes its `answer:` line, and changes
nothing else but a coordinate it appends to `location:`; the next round reads
it directly. Nobody edits or deletes an earlier round file. Words only: no
emoji anywhere in the file. Every labelled line and finding heading follows
its row of the grammar table in `docs/the-review-record.md` *The round
record*: the table, which `chain_check.py` reads at the pull request, gives
each line's shape, where it stands and how many of it there are, and the
check refuses any line it does not hold. -->

target: 1a2b3c4 against main

<!-- target: the commit this round reviewed, with the base a round that
reviewed the branch read it against, or the fix range a verifying round
read; its row of the table gives both forms.

A round past the cap carries one line here, written by the warden from
the reason the orchestrator's spawn prompt gives. The cap counts finding
rounds from the last design change, a reframe or a new phase the owner
approved, and <S> is the first round after it:
Extended past round <K>, counting from round <S>: round <K> found <n>, round <K-1> found <m>, and none is a regression.
A verifying round after a regression's fix pass is not an extension and
carries no such line. -->

<!-- original: owed in a repository that declares `seal/parity.md`, where
the pull request changes a path outside `docs/` and `seal/`. The warden
compares this round's target with the original through `legacy-parity`,
then writes one line here, outside this comment, naming the migration
config's `Baseline commit`:
original: 1a2b3c4
Where the original could not be resolved, the warden writes no line and
raises an `unread` finding. Elsewhere no line is written. -->

## Findings

<!-- One `### <n>. <symptom>` section per finding, numbered from 1. What
each of its labels means:
  severity:    must (fix before merge) or should (fix, or say why not); for
               people, and the check decides nothing on it
  location:    where the defect shows, and the file the fix changes where
               that is elsewhere, each path from the root. A `fixed` commit
               must change one of these paths or a path under one
  evidence:    what the claim rests on: `executed` and each command run, or
               `read` and each `path:line` opened. A claim of absence,
               that nothing catches, calls or states something, is
               `executed` only, naming the search that found nothing
  verdict:     the line the check decides on:
                 open               what the warden writes
                 fixed <commit>     the commit that fixed it, on this branch
                 rejected           the finding does not hold; the answer
                                    says why
                 deferred <home>    the issue or file it went to, by the
                                    filing ladder, or where a repair with
                                    no commit was made
                                    (docs/the-review-record.md)
  regression:  only on a finding in a unit a fix pass's own commits added
               or changed, where those commits introduced the defect: the
               earlier finding, or the fix pass no finding named. A `fixed`
               commit that left the defect standing takes `reopens:`. A unit
               a build phase made is new work and takes none. The grounds
               then owe one sentence comparing the fix with the frame, which
               the orchestrator routes the round on
               (docs/the-review-record.md). Delete the line otherwise
  reopens:     on a finding that raises an earlier `fixed` or `rejected`
               finding again, where its close does not hold and no fix
               pass's commit made the defect: the earlier finding. An
               ordinary finding, which gets its fix pass. Delete the line
               otherwise
  answer:      the fix pass: what was done, why the finding does not hold,
               or where it went
Then why it matters and the grounds (where
`regression:` stands, the unit, first; where `reopens:` stands, why the
earlier close does not hold, first); the paste-ready fix in a fenced
block, the artefact itself; and `answer:`. A fix that went to a path
`location:` does not name appends that coordinate to the line and says so in
`answer:`. A ready pull request fails while a finding reads `open`, for any
line the table refuses, and for what `docs/the-review-record.md`
*What the check reads at the pull request* names. -->

### 1. <what is wrong, as a symptom, in one line>

severity: must
location: `path:12`
evidence: read `path:12`
verdict: open
regression: round-1#1

<why it matters and the grounds>

```<lang>
<the paste-ready fix: the artefact, not a description of it>
```

answer: <the fix pass: what was done, why the finding does not hold, or where it went>

## Confirmations

<!-- One entry per thing this round confirmed holds: an earlier round's
finding truly closed, or a claim of the frame or the build that matched.
Never a finding. Each entry is a `confirms:` line naming the earlier finding,
then its prose on the lines after it; every `fixed` or `rejected` finding of
the round before is named by one here, or by a `reopens:` or `regression:`
line. A claim of the frame or the build reads `none`, and so does every
entry of round 1, which has no earlier round. A round with nothing to
confirm leaves this section out. -->

confirms: round-1#2
<what holds, at `path:line`, and how this round confirmed it, executed or read>

confirms: none
<a claim of the frame or the build that matched, at `path:line`, executed or read>

## Not judged

<!-- One row per thing this round could not judge, and who answers it. Never a
finding. -->

| What | Location | Who answers |
|---|---|---|

## Probes

| Command | Result |
|---|---|
| <the command> | <what came back: what ran, never what was read> |

# code-review, the orchestrator's half

This file is the orchestrator's: the session that spawns the proofer and the
crafter for each round, verifies what they report and opens the pull request.
It holds the procedure for **running** a review run: spawning each phase's
crafter, obtaining a fix pass, ending the run, opening the pull request, and
verifying the proofer's report.

`skills/code-review/SKILL.md` is the other half and holds the review itself:
the two stages, the comparison axes, the probe rules, the cross-session
records and the findings format. The orchestrator reads both. The proofer
preloads that one and never opens this one.

Every `##` heading here opens with `Orchestrator:`, and
`skills/implement/orchestration.md` *Orchestrator: which of these acts runs
itself* lists each act with what notices when it is skipped.

## Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer

**Each phase of a work item is built by a fresh `crafter` spawn, and the
orchestrator never resumes a crafter across a phase boundary.** The
orchestrator hands the fresh crafter the phase records the earlier phases
wrote, `trail/phases/phase-N.md`, and a brief in the shape of
`docs/the-review-record.md` *The handoff*: coordinates rather than prose,
each fact labelled. A phase record is written to carry what one phase found
to the next, and a resumed crafter pays its whole earlier context again on
every turn to hold what the record already holds.

**A fix pass resumes the implementer only while the implementer's largest
per-turn context is below 806,241 tokens, and is a fresh `crafter` spawn
otherwise.** The implementer is the crafter that wrote the last commit the
round reviewed. Before the fix pass, the orchestrator runs
`seal cost --segments <the implementer's agent-*.jsonl>` on the
implementer's own transcript, the file the harness's task output named, and
reads the largest value of its `context` column. Below the threshold, the
orchestrator resumes the implementer, whose context already holds the files
it wrote, the tests it ran and the grounds it recorded. At the threshold or
above it, the orchestrator spawns a fresh crafter and hands it the round record
and the phase records. The threshold is the largest context a fresh,
never-resumed crafter reached in the 0.22.0 run, read with
`seal cost --segments` over that run's transcripts (#945), so a resumed
implementer past it holds more context than any fresh build of that run
needed. The column reads the largest turn, so a compaction that shrank the
implementer's context does not lower the reading: the orchestrator then
spawns fresh where a resume was possible, which costs calls and never a
wrong tree.

A fix pass also takes a fresh spawn where the implementer's session no
longer exists, on a new day or another machine, and the orchestrator hands it
the same records. An orchestrator in a new session holds no `automation`
press until it puts question 1 through `AskUserQuestion` again, so it does
that before the spawn (`skills/implement/orchestration.md` *Question 1*).

**The crafter's fix pass changes two lines per open finding of
`trail/rounds/round-N.md`, its verdict and its answer, and nothing else but a
coordinate it appends to `location:` where its fix went elsewhere**
(`docs/the-review-record.md` *The round record*); it writes no
`trail/phases/phase-N.md` and no `plan.md` row.

**Two commits after the build are yours, not the crafter's**: a fix written after
the last round, and the commit that integrates a sibling's squash. Each one that
changes what the work item ships brings the work item's `changelog.md` along, the
way the crafter's fix pass does.
`docs/the-record-layout.md` *A commit after the build brings its changelog
fragment along* owns that rule.

**The fix pass then finds what the fixes left standing.** A fix repairs the
coordinate a finding named, and the fact the finding was about is usually
stated in more than one place, so the other statements survive and arrive as
a later round; that is contract rule 12. For each rule its range reworded or
removed, the crafter finds every other place stating it, by its words and by
the `check:` target that holds it, and corrects each or names it in the
hand-back with why it stands. The round that follows reads that list against
the diff.

**You type only the half of a spawn prompt that changes between rounds.**
`skills/agent-contract/SKILL.md` reaches every agent you spawn at startup,
through the `skills:` list in its definition, and each agent's own half is in
`agents/<name>.md`. So the prompt holds what is specific to this round and
nothing else.

**That contract binds you too, and reaches you only if you open it.** An
orchestrator reads this skill and never `agents/*.md`, so the contract
reaches it by being opened rather than by arriving: `user-invocable: false`
permits the load and does not oblige it.

## Orchestrator: the run ends with a verifying round

A round's findings are closed after it ends, by whoever writes the fixes. Every
round but the last has a reader for those fixes: the round that follows, which
answers each of its verdicts. The last round's fixes have none unless a round
is spawned for them.

So a run ends with a **verifying round**, and three things define it.

| Property | What |
|---|---|
| When | **after the fixes** for the previous round are committed, never before, or it reviews what has already been reviewed |
| Target | the **diff of those fixes**, not the branch. That is what keeps it bounded, and bounded is not cheap: its cost is set by the frame, the inherited records and the probes, so it runs close to a finding round. `docs/the-review-record.md` *The run* states the rule |
| Job | the answers, not new findings. For each finding the previous round closed `fixed <commit>` or `rejected`, is it actually closed: a `confirms:` line naming it where it is; where it is not, a finding whose `reopens:` line names it, or whose `regression:` line does where a fix pass's own commit made the defect |

The new units in that diff are the exception: they have been reviewed by
nobody, so the verifying round reviews them as code.

**A round that opens nothing needing a fix does not consume the cap.** The cap
counts rounds that found something, because it exists to stop a loop that is
not converging, and a round that finds nothing is the loop having converged.
A verifying round that opens something IS a finding round and consumes the cap
like any other, and one that opens nothing is by definition the last one,
because the run ends at it.

**A run has three finding rounds by default, counted from the last design
change, extends one round at a time while the findings shrink, and at the
cap every open finding takes the filing ladder.** `docs/the-review-record.md`
*The run* states the cap, where its count starts again, the verifying round
a regression's fix pass is owed whatever the count, the extension line the
spawn prompt gives the proofer, and the ladder.

The condition is not *this round found nothing*, which would be unbounded. A
verifying round that raises a `should` finding the crafter closes `rejected`,
with its grounds, has opened nothing needing a fix, and it does not consume
the cap. Its record is still not the last one: the check refuses a `fixed` or
`rejected` finding in the last record, so one more verifying round reads that
answer alone. Where the rejection holds, that round names it on a
`confirms:` line; where it does not, that round raises a finding with a
`reopens:` line naming it, which gets its fix pass and one more verifying
round; a round carrying a `regression:` line is routed as the section below
says, and where the work item returns to its framer the run goes on with the
redesign. The run ends only on a round whose record holds no `open`, `fixed`
or `rejected` finding and whose `target:` commit is HEAD, or is followed only
by the work item's own records (a verifying round, or the round at the cap
whose open findings took the filing ladder), since the check refuses a ready
pull request whose last record fails either. A fix committed after that
round, one the ladder's first rung sends to the diff among them, is followed
by one more verifying round.

### A regression is routed by comparing the fix with the frame

**The route comes first, because a stop that names no exit is a wall.** A
finding's `regression:` line routes nothing by itself. Its grounds open
with the unit and then one sentence comparing the fix with the frame: what
the frame says, what the fix did and where the defect came from. You route
the round on that sentence (`docs/the-review-record.md` *The run*):

| The sentence says | The route |
|---|---|
| the fix built the phase's `plan.md` row and `frame/design.md` as written, and the defect stands anyway | no fix pass; the work item goes back to its framer, by the steps below |
| the fix did something the frame does not say, or the defect is in how it was written, a review record's paste-ready fix applied as given among them | an ordinary fix pass, with the crafter told what the frame says |
| the unit already had a regression routed to a fix pass in this run | the framer, by the steps below, whatever the sentence says |

The framer's route:

| Step | What |
|---|---|
| The record | every open finding closes `deferred the frame` |
| The framer | spawned again with the run's round records as its input; they are in the tree, so the prompt names them and carries nothing else. It rewrites `plan.md` (new phase rows; a closed phase keeps its commit) and `frame/design.md` where the scope moves, and adds `Reframed <date> by <who>, after round <N>.` under the `Framed` line. Where `routing.md` answers `Automation` with `yes`, the spawn asks nobody |
| The redesign | you approve it when you spawn `crafter` for it, with a second `Approved` line in `plan.md` on a line of its own, in the shape `skills/implement/orchestration.md` *The plan is approved at the spawn* states; it is then built and reviewed, and its first finding round starts the cap's count again |

## Orchestrator: the pull request opens once the sealer seals

**The pull request opens ready, once the sealer has sealed, and CI runs
then.** Where `Destination` reads `open the pull request`, push the branch as
often as you like while the work is built and reviewed: a branch with no
pull request runs nothing. Under `stop before the pull request` nothing is
pushed, and the branch is handed back committed and unpushed. Once
`guarantee.md` reading `sealed` is committed, open the pull request with the
body the sealer read, `gh pr create --body-file <that file>`. CI runs then,
and again on every push to it.

**After the pull request opens, and after each push to it, the orchestrator
reads `gh pr view <N> --json mergeable` before it waits on CI.**
`CONFLICTING` means GitHub made no merge ref for the pull request and runs no
`pull_request` CI on it, and nothing else says so. `UNKNOWN` means GitHub
has not computed the answer yet, and the orchestrator reads it again.
`MERGEABLE` is the answer under which the orchestrator waits on CI.

**A conflict with the base is integrated by merging the base into the
branch, never by a rebase.** A rebase orphans the commits every round record
names on its `target:` line (`docs/release-checklist.md` *0. Before
starting*). The orchestrator merges once, after the branch whose changes
conflict with this one has landed on the base. Where the merge resolved a
conflict in a file outside the work item's records, the orchestrator spawns
a verifying round on that resolution, because the chain check lists the
branch's commits with `--no-merges` and reads no merge commit
(`skills/code-review/scripts/chain_check.py#follows`). The merge moves HEAD
past `trail/gate.md` and `guarantee.md`, so after the merge, and after that
verifying round's record is committed where one is owed, the orchestrator
runs the broad gate again, commits its record, runs `seal pr-body` on the
body file again and spawns the sealer again.

**Where the work's risk is platform-specific, run the other platforms before
the broad run.** Line endings, the shell and the Python version are such
risks. Push the branch once the build's last phase closes and run
`gh workflow run tests --ref <branch>`, then read that run's result before
you take the broad run. A leg that fails there is a defect like any a round
finds, and it is repaired before the rounds settle. Under `stop before the
pull request` push nothing: name the platform risk in the hand-back, for
whoever opens the pull request.

**The stated limit: a defect that only one platform shows, in work nobody
expected to be platform-specific, is found when the pull request opens,
after the sealer.** Its fix is a commit outside the work item's records, so
it takes the repair path below: a verifying round on its diff, the broad run
again, and the sealer again. Nothing else is built for it. The pull request
stays open through that repair. Once the repair's broad run is committed,
the orchestrator runs `seal pr-body` on the body file again and gives the
file to the open pull request with
`gh api -X PATCH repos/<owner>/<repo>/pulls/<N> -F body=@<file>`
(`docs/release-checklist.md` names why not `gh pr edit`).

**A repository that still opens a draft is not refused.** On a draft
`chain_check` prints what it would refuse and exits 0, and `hygiene`'s
`ready_for_review` event re-runs it when the draft is marked ready, so the
record is still owed then. Nothing that can reach `main` is exempt.

**`trail/gate.md` and `guarantee.md` are read at the pull request**, so four
more steps come before it opens: the preflight, the broad run, the pull
request body, and then the sealer's spawn. You take them once the work
item's `changelog.md` states what the work item ships and every row
`skills/implement/SKILL.md` *6. Drain the rows before the broad run, and
keep the records* names has reached its destination.
The party that builds the work item writes that fragment: the crafter, or you
where `routing.md` answers `Implementation` with `the session`
(`docs/the-record-layout.md` *A change writes fragments, never a shared
file*). The preflight and the broad run are yours, and no agent takes either.
**Run `seal gate --preflight --base <base>`; on its exit 0, with nothing else
running, run `seal gate --base <base> --record <item>`**, which takes the
one broad pass now that the rounds have settled and, on a green run, writes
`trail/gate.md`. `skills/verify/orchestration.md` *The broad gate* says what
the run covers and what each word beside a failing file means. Send its
output to `<scratchpad>/<work-item-id>/gate.log`, making the directory
first, and read the whole log and the exit code
directly. **On exit 0 commit `trail/gate.md`, then write the pull request
body, then spawn `sealer` with the base and the work item's directory**, the
issue and the file holding the pull request body. The
sealer reads that record, audits the work against the issue and the tree,
and writes `guarantee.md` (`docs/the-review-record.md` *The guarantee*); it
runs nothing broad, and a missing or stale record comes back
`Verdict: withheld reason: no broad run at HEAD`.

**You write the pull request body after `trail/gate.md` is committed,
because the body's first part copies that record.** Run
`seal pr-body <item> --body <scratchpad>/<work-item-id>/pr-body.md`, where
`<item>` is the work item's directory. It writes the part of that file above
the line `skills/code-review/scripts/pr_body.py#HEADING` holds, copied from
the work item's records, and keeps byte for byte whatever stands under that
line. On exit 1 its `refused:` lines name a record's file and line: repair
that record, commit it, and run the command again. Then write your own part
under that line, to the end of the file: what no record holds, such as the
motivation, a note to reviewers, the `Closes` or `Part of` line, the broad
run's printed figures, a CI run taken after the rounds, the chain section's
comparison table, and the attribution line. Your part restates no record:
where it needs a record's fact, it names the record's path. Edit nothing
above the line; the sealer's `seal pr-body --check` withholds on a part
above it that is not the records' text at HEAD. **Run the command again
before every later spawn of the sealer and before every `gh api -X PATCH`
of the body**, so the first part copies the records as the repair left
them; your part stays as you wrote it.
`skills/commit-pr-convention/SKILL.md` *Pull request bodies* says which
language each part is in.

**On the broad run's exit 1 spawn nothing.** The word beside each failing
file says whether it predates the work: `new` is this work's to repair,
`failing on base too`
is a follow-up to name, and `new?` carries the reason nothing at the base
measured it, so run that file at the base before treating it as either.
Review a repair where it touched a file outside the work item's records, and
run the gate again. On the broad run's exit 2 nothing ran; a refusal about the row goes
to a person, as *A refusal about the `Broad gate` row* below says.

**Pass the base as a plain branch name, and quote the lines only the gate can
tell.** The gate resolves the base to the ref CI reads: the base's upstream
where the checkout declares one, else `origin/<base>`. Quote, as printed,
where resolving the base moved it, where the run handed itself to the tree's
copy of the gate, and its `outputs kept under seal-gate-<random>/` line;
each is a fact a reader learns from nowhere else.

**Commit `guarantee.md`; a verdict other than `sealed` opens no pull
request.** `withheld` names the claim and the coordinate. Where the repair
touches only the work item's own records (a phase record, the changelog
fragment) or your part of the pull request body, make it, commit what it
changed in the records, run `seal pr-body` on the body file again, and spawn
the sealer again at the new HEAD, giving a repaired body to a pull request
already open as the stated limit above says: the record commits after the
run leave it standing.
Where it touches any other file it is a fix nobody reviewed: commit it, spawn
a verifying round on its diff, and once that round's record is committed run
the broad gate again, commit its record, run `seal pr-body` on the body file
again, and spawn the sealer. Your broad run
asks the records arm first, and that arm refuses a commit outside the work
item after the last round's `target:` commit, so a run taken straight after
the fix returns the same refusal. `undecided` is a question for the owner,
put after the run rather than during it; write the answer under the verdict
as `Answered <date> by <who>: <answer>`, commit, and spawn the sealer again.
`withheld reason: the base <name> resolves to no commit here` needs no
commit: a `git clone` of the branch worktree copies its branches and none
of its `origin/` refs, so spawn the sealer again with the branch worktree
itself as its clone, where `origin/<base>` or, with no remote, `<base>`
resolves.
Where the guarantee's row names a commit the branch does not hold, which
the pull request's check refuses as stale, spawn the sealer again at HEAD
and commit what it writes; never edit the row by hand. The stamp's writer
recorded the refusal at the write, so the new audit, which keeps the refused
verdict on its row, draws the work item's stamp (`docs/the-review-record.md`
*The stamp*).

**The preflight is yours, and it is not the broad gate.** It runs every
arm of the gate except the `Broad gate` row, in the gate's order and over the
same resolved base, once every refusal of the row has been applied; the row is
read and not run. It takes seconds where the broad run takes a suite, so a
refusal on a record arm, which the broad run would return after that suite,
arrives before it. Read its exit code directly and take the broad run only on 0. On
1 its `PREFLIGHT FAILED` lines name each failing arm with its first lines and
the file holding the rest: correct the record, commit, and run it again. On 2
it refused before anything ran, and a refusal about the row goes to a person,
as *A refusal about the `Broad gate` row* below says. It writes no file and
prints no `BROAD GATE` line, so nothing it prints reads as the broad run's.
An orchestrator that skips the preflight loses only time: the broad run asks
the same arms, and refuses the same way after its suite.

**The stamp is drawn for you at the end of the turn in which the sealer's
report arrives, and you never draw one.** The broad run
draws nothing: its stdout opens `BROAD GATE PASSED` or `BROAD GATE FAILED`,
which say whether the broad command passed and judge nothing. The stamp means
every party verified the work item, the sealer last, so it is drawn once per
work item from the sealer's verdict: where the one `Verdict:` of
`guarantee.md` reads `sealed`, the sealer's own `Write` of it queues the
stamp's values, under either root, and the `Stop` hook draws them after your
text. The line naming them is the edit hook's message, shown to the person
at that write. It is not in the sealer's report and does not reach you.
So put the result text first in that turn:
what was sealed, the lines worth quoting, and what happens next. Then end
the turn, and the drawing lands last with nothing after it. Draw none
yourself, neither with `seal stamp` nor by relaying a log: a relayed log
shows the person the stamp twice, the copy without its colour and cut. The
`BROAD GATE PASSED` line names the branch and the tree the run measured and
the ref and the commit it was compared against, the panel's rows follow it
as text, and the report's last line says `trail/gate.md` is written and not
committed: CI reads HEAD, so commit it before you push, or the one
broad run is recorded nowhere CI looks. On a red run relay the `BROAD GATE
FAILED` lines. Wherever a line you read names `seal stamp --from`, quote
it as it stands: that command is the person's to type, and never yours. The
edit hook's line never reaches you. Where no stamp appeared, name the file
under `<git-common-dir>/agentic-stamp/<session>/` whose name holds the work
item's id, and leave `seal stamp --from <that file>` to the person. The line
names the command because the hook draws nothing and says nothing where it
cannot: a `python3` that cannot load `seal_stamp.py`, a working directory
outside the clone, or a plugin older than the hook. Where no edit hook saw
the guarantee written, no line prints and no stamp is drawn, and the pull
request's check is what says the work item was sealed.

**A refusal about the `Broad gate` row goes to a person, and the run stops
until they answer.** Your broad run comes back exit 2 two ways that are
about the row rather than about the work: the repository declares no row, or
its row is one the gate would not run as the command it reads as. Neither is
yours to settle, and no agent's: the row is the one value in this flow only
a person may write, because there is no default and the broad run covers
exactly what a person wrote. Put the gate's own sentence in front of
whoever owns the repository, name `/agentic:config` as where they answer it, and
open no pull request until they have. A row filled in to get past the
refusal makes the broad run cover a command the person never saw.

**A session that has compacted hands the next round to a fresh one, and the
round record is the handoff.** A compacted context holds a summary of what
it read, and a round run from a summary either re-reads what the summary
dropped or trusts it. The record carries the target, the verdicts and the
probes as the reviewer wrote them, so the fresh session opens the record and
its coordinates rather than the summary.

## Orchestrator: verify before posting

Never post the proofer's output as it stands. Check, by opening the
coordinates yourself:

1. The coordinates behind every highest-severity finding, because those are
   the heaviest to act on and the hardest to retract.
2. Every claim that a state can occur, because a constraint, an enum or a
   default may forbid the state.
3. Spec citations, because clause numbers move while a review runs.
4. Test-pass claims: run them, and count the skips, which read as passes.

Also check whether HEAD moved during the review; if source changed, those
verdicts need a re-pass, and the next round's `target:` line names the new HEAD.

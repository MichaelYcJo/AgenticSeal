# code-review — the orchestrator's half

The five sections `skills/code-review/SKILL.md` used to carry under an
`Orchestrator:` prefix. They are the procedure for **running** a review run:
obtaining a fix pass, ending the run, opening the pull request, verifying the
reviewer's report, and closing the cycle.

**Read this if you are orchestrating a review run.**
`skills/code-review/SKILL.md` is the other half and holds the review itself —
the two stages, the comparison axes, the probe rules, the cross-session
records and the findings format. An orchestrator reads both; a `warden` spawn
preloads that one and never this.

The headings keep the `Orchestrator:` prefix they were written with, so a
reference to one of these sections names the section it always named and only
the file it names changed (#265).

## Orchestrator: a fix pass resumes the implementer

A round's findings are closed by fixes written after it ends, and the session
that writes them is obtained by **resuming the session that built the branch**
— never by spawning a fresh one while that session still exists. The resumed
session's context already holds what the fixes need: the files it wrote, the
tests it ran, the grounds it recorded. A fresh spawn holds none of it and
re-establishes all of it before the first fix lands — the rediscovery cost the
handoff before round 1 exists to bound, paid again in full for a pass that
needed none of it.

Measured three times, with no counterexample: as a fresh spawn, one fix pass
cost 282 calls and 45 minutes (#33); as a resume, 30 calls and 3.9 minutes
(#29) and 26 calls and 5.2 minutes (the #57 chain).

When the implementing session no longer exists — a new day, another machine —
the fresh spawn is the only option left, and what it takes is the handoff
(`docs/the-review-record.md` §*The handoff*): coordinates rather than
prose, each fact labelled. The rule decides which to reach for while both
options exist. A new session has no `automation` press until it puts the
routing question's first question through `AskUserQuestion` again, so it does
that before the spawn (`skills/implement/orchestration.md`, *A run resumed in
a new session*).

**The fix pass changes two lines per open finding of `rounds/round-N.md`,
its verdict and its answer, and nothing else but a coordinate it appends to
`location:` where its fix went elsewhere**
(`docs/the-review-record.md` §*The round record*); it writes no
`phases/phase-N.md` and no `plan.md` row.

**Two commits after the build are yours, not the smith's**: a fix written after
the last round, and the commit that integrates a sibling's squash. Each one that
changes what the work item ships brings the work item's `changelog.md` along, the
way the smith's fix pass does.
`docs/the-record-layout.md` §*A commit after the build brings its changelog
fragment along* owns that rule.

**Then ask what the fixes left standing.** A fix repairs the coordinate a
finding named, and the fact the finding was about is usually stated in more
than one place, so the other statements survive and arrive as a later round —
that is contract §12. The fix pass finds them: for each rule its range
reworded or removed, every other place stating it is found by its words and
by the `check:` target that holds it, and corrected, or named in the
hand-back with why it stands. The round that follows reads that list against
the diff.

**The half of a prompt that does not change between rounds is not yours to
type.** `skills/agent-contract/SKILL.md` reaches every agent you spawn at
startup, through the `skills:` list in its definition, and each agent's own
half is in `agents/<name>.md`. So the prompt is left holding what is specific
to this round and nothing else. That half used to be retyped from memory every
round and drifted without a trace: one rule arrived at round 2 of a seven-round
chain and round 1 ran without it.

**That contract binds you too, and only if you load it.** An orchestrator
reads this skill and never `agents/*.md`, so the file reaches it by being
opened rather than by arriving — `user-invocable: false` permits the load and
does not oblige it. #107's headline failure is an orchestrator breaking a rule
it had put into every prompt it sent, which no rule reaching only the agents
would have caught.

## Orchestrator: the run ends with a verifying round

A round's findings are closed after it ends, by whoever writes the fixes. Every
round but the last has a reader for those fixes — the round that follows, since
each of its verdicts needs an answer there. The last round's fixes have none
unless a round is spawned for them.

That is not an occasional slip. It is how every run ended, and it was measured
twice in a row: the one round that did open the previous round's fixes found
**seven** defects in them, and its own fixes then went in unread.

So a run ends with a **verifying round**, and three things define it.

| | What |
|---|---|
| When | **after the fixes** for the previous round are committed — never before, or it reviews what has already been reviewed |
| Target | the **diff of those fixes**, not the branch. That is what keeps it bounded, and bounded is not cheap: its cost is set by the frame, the inherited records and the probes, so it runs close to a finding round. `docs/the-review-record.md` §*The run* states the rule |
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
cap every open finding takes the filing ladder** — `docs/the-review-record.md`
§*The run* states the cap, where its count starts again, the verifying round
a regression's fix pass is owed whatever the count, the extension line the
spawn prompt gives the warden, and the ladder.

The condition is not *this round found nothing* — that would be unbounded, and
it was considered and rejected. A verifying round that raises a `should`
finding the smith closes `rejected`, with its grounds, has opened nothing
needing a fix, and it does not consume the cap. Its record is still not the
last one: the check refuses a `fixed` or `rejected` finding in the last
record, so one more verifying round reads that answer alone. Where the
rejection holds, that round names it on a `confirms:` line; where it does
not, that round raises a finding with a `reopens:` line naming it, which
gets its fix pass and one more verifying round; a round carrying a
`regression:` line is routed as the section below says, and where the work
item returns to its framer the run goes on with the redesign. The run ends
only on a round whose record holds no `open`, `fixed` or `rejected` finding
and whose `target:` commit is HEAD, or is followed only by the work item's
own records — a verifying round, or the round at the cap whose open
findings took the filing ladder — since the check refuses a ready pull
request whose last record fails either. A fix committed after that round,
one the ladder's first rung sends to the diff among them, is followed by
one more verifying round.

### A regression is routed by comparing the fix with the frame

**The route comes first, because a stop that names no exit is a wall.** A
finding's `regression:` line routes nothing by itself. Its grounds open
with the unit and then one sentence comparing the fix with the frame: what
the frame says, what the fix did and where the defect came from. Route the
round on that sentence (`docs/the-review-record.md` §*The run*):

| The sentence says | The route |
|---|---|
| the fix built the phase's `plan.md` row and `spec.md` as written, and the defect stands anyway | no fix pass; the work item goes back to its framer, by the steps below |
| the fix did something the frame does not say, or the defect is in how it was written, a review record's paste-ready fix applied as given among them | an ordinary fix pass, with the smith told what the frame says |
| the unit already had a regression routed to a fix pass in this run | the framer, by the steps below, whatever the sentence says |

The framer's route:

| Step | What |
|---|---|
| The record | every open finding closes `deferred the frame` |
| The framer | spawned again with the run's round records as its input — they are in the tree, so the prompt names them and carries nothing else. It rewrites `plan.md` (new phase rows; a closed phase keeps its commit) and `spec.md` where the scope moves, and adds `Reframed <date> by <who>, after round <N>.` under the `Framed` line. Under `Automation \| yes` the spawn asks nobody |
| The redesign | approved by a second `Approved` line in `plan.md` when `smith` is spawned for it, built, and reviewed, its first finding round starting the cap's count again |

## Orchestrator: the pull request opens once the sealer seals, and a phase is re-run

**The pull request opens ready, once the sealer has sealed, and CI runs
then.** Where `Destination` reads `open the pull request`, push the branch as
often as you like while the work is built and reviewed: a branch with no
pull request runs nothing. Under `stop before the pull request` nothing is
pushed, and the branch is handed back committed and unpushed. Once
`guarantee.md` reading `sealed` is committed, open the pull request with the
body the sealer read, `gh pr create --body-file <that file>`. CI runs then,
and again on every push to it. A pull request opened before round 1 ran the
suite on three platforms at every push of every round, and marking its draft
ready ran it once more on a commit it had already run (#943).

**Where the work's risk is platform-specific, run the other platforms before
your broad run.** Line endings, the shell and the Python version are such
risks. Push the branch once the build's last phase closes and run
`gh workflow run tests --ref <branch>`, then read that run's result before
you take the broad run. A leg that fails there is a defect like any a round
finds, and it is repaired before the rounds settle. Under `stop before the
pull request` push nothing: name the platform risk in the handback, for
whoever opens the pull request.

**The stated limit: a defect that only one platform shows, in work nobody
expected to be platform-specific, is found when the pull request opens,
after the sealer.** Its fix is a commit outside the work item's records, so
it takes the repair path below: a verifying round on its diff, the broad run
again, and the sealer again. Nothing else is built for it. The pull request
stays open through that repair, and a body the repair changes is written to
the file again and given to the open pull request with
`gh api -X PATCH repos/<owner>/<repo>/pulls/<N> -F body=@<file>`
(`docs/release-checklist.md` names why not `gh pr edit`).

**A repository that still opens a draft is not refused.** On a draft
`chain_check` prints what it would refuse and exits 0, and `hygiene`'s
`ready_for_review` event re-runs it when the draft is marked ready, so the
record is still owed then. Nothing that can reach `main` is exempt.

**`broad-gate.md` and `guarantee.md` are read at the pull request.** So the
sequence has three more steps before it opens, once the pull request body is
written to a file and the work item's `changelog.md` is written: the
preflight, the broad run, and then a spawn. The first two are yours, and no
agent takes either.
**Run `broad-gate --preflight --base <base>`; on its exit 0, with nothing else
running, run `broad-gate --base <base> --record <item>`**, which takes the
one broad pass now that the rounds have settled and, on a green run, writes
`broad-gate.md`. Send its output to `<scratchpad>/<work-item-id>/broad-gate.log`,
making the directory first, and read the whole log and the exit code
directly. **On exit 0 commit `broad-gate.md`, then spawn `sealer` with the
base and the work item's directory**, the issue and the file holding the pull
request body. The
sealer reads that record, audits the work against the issue and the tree,
and writes `guarantee.md` (`docs/the-review-record.md` §*The guarantee*); it
runs nothing broad, and a missing or stale record comes back `withheld —
no broad run at HEAD`.

**On exit 1 spawn nothing.** The word beside each failing file says whether
it predates the work: `new` is this work's to repair, `failing on base too`
is a follow-up to name, and `new?` carries the reason nothing at the base
measured it, so run that file at the base before treating it as either.
Review a repair where it touched a file outside the work item's records, and
run the gate again. On exit 2 nothing ran; a refusal about the row goes
to a person, as *A refusal about the `Broad gate` row* below says.

**Pass the base as a plain branch name, and quote the lines only the gate can
tell.** The gate resolves the base to the ref CI reads: the base's upstream
where the checkout declares one, else `origin/<base>`. Quote, as printed,
where resolving the base moved it, where the run handed itself to the tree's
copy of the gate, and its `outputs kept under broad-gate-<random>/` line;
each is a fact a reader learns from nowhere else.

**Commit `guarantee.md`; a verdict other than `sealed` opens no pull
request.** `withheld` names the claim and the coordinate. Where the repair
touches only the work item's own records — a phase record, the changelog
fragment — or the pull request body, make it, commit, and spawn the sealer
again at the new HEAD, giving a repaired body to a pull request already open
as the stated limit above says: the record commits after the run leave it standing.
Where it touches any other file it is a fix nobody reviewed: commit it, spawn
a verifying round on its diff, and once that round's record is committed run
the broad gate again, commit its record, and spawn the sealer. Your broad run
asks the records arm first, and that arm refuses a commit outside the work
item after the last round's `target:` commit, so a run taken straight after
the fix returns the same refusal. `undecided` is a question for the owner,
put after the run rather than during it; write the answer under the verdict
as `Answered <date> by <who>: <answer>`, commit, and spawn the sealer again.
`withheld — the base <name> resolves to no commit here` needs no commit: a
`git clone` of the branch worktree copies its branches and none of its
`origin/` refs, so spawn the sealer again with the branch worktree itself as
its clone, where `origin/<base>` or, with no remote, `<base>` resolves.
Where `pre-commit` refuses the commit of `guarantee.md` because its row names
a commit the branch does not hold, spawn the sealer again at HEAD and commit
what it writes; never edit the row by hand. The hook recorded the refusal,
so the new audit, which keeps the refused verdict on its row, draws the
work item's stamp (`docs/the-commit-gate-inside-git.md`).

**The preflight is yours, and it is not the broad gate (#638).** It runs every
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
A session that skips the preflight loses only time: the broad run asks the
same arms, and refuses the same way after its suite.

**The stamp is drawn for you at the end of the turn in which `guarantee.md`
reading `sealed` is committed, or in local mode the turn in which the
sealer's report arrives, and you never draw one (#975).** The broad run
draws nothing: its stdout opens `BROAD GATE PASSED` or `BROAD GATE FAILED`,
which say whether the broad command passed and judge nothing. The stamp means
every party verified the work item, the sealer last, so it is drawn once per
work item from the sealer's verdict: when you commit its `guarantee.md` and
the one `Verdict:` reads `sealed`, git's `post-commit` writes the stamp's
values and prints one line naming them, and the `Stop` hook draws them after
your text. In local mode no commit carries `guarantee.md`: the sealer's own
`Write` of it queues the values. The line naming them is the edit hook's
message, shown to the person at that write. It is not in the sealer's
report and does not reach you. So put the result text first in that turn:
what was sealed, the lines worth quoting, and what happens next. Then end
the turn, and the drawing lands last with nothing after it. Draw none
yourself, neither with `seal-stamp` nor by relaying a log. The 0.15.6 run
relayed the log, and the person saw the same stamp twice, the copy
colourless and cut. The `BROAD GATE
PASSED` line names the branch and the tree the run measured and the ref and
the commit it was compared against, the panel's rows follow it as text, and
the report's last line says `broad-gate.md` is written and not committed: CI
reads HEAD, so commit it before you push, or the one
broad run is recorded nowhere CI looks. On a red run relay the `BROAD GATE
FAILED` lines. Wherever the commit's line names `seal-stamp --from`, quote
it as it stands: that command is the person's to type, and never yours. In
local mode no such line reaches you. Where no stamp appeared, name the file
under `<git-common-dir>/specseal-stamp/<session>/` whose name holds the work
item's id, and leave `seal-stamp --from <that file>` to the person. The line
names the command because the hook draws nothing and says nothing where it
cannot: a
`python3` that cannot load `seal_stamp.py`, a working directory outside the
clone, or a plugin older than the hook. Where git's hooks slot is somebody
else's no line prints and no stamp is drawn, and the pull request's check is
what says the work item was sealed.

**A refusal about the `Broad gate` row goes to a person, and the run stops
until they answer.** Your broad run comes back exit 2 two ways that are
about the row rather than about the work: the repository declares no row, or
its row is one the gate would not run as the command it reads as. Neither is
yours to settle, and no agent's — the row is the one value in this flow only
a person may write, because there is no default and the broad run covers
exactly what a person wrote. Put the gate's own sentence in front of
whoever owns the repository, name `/specseal:config` as where they answer it, and
open no pull request until they have. Filling the row in to get
past the refusal is #401: it is what happened, and the run then covered a
command the person had never seen.

**A session that has compacted hands the next round to a fresh one, and the
round record is the handoff.** A compacted context holds a summary of what
it read, and a round run from a summary either re-reads what the summary
dropped or trusts it. The record carries the target, the verdicts and the
probes as the reviewer wrote them, so the fresh session opens the record and
its coordinates rather than the summary.

**A hand-back's verification claim is a claim.** Before spawning the next
phase, run the closed phase's suite and the lint of its changed files yourself
and read the output: a phase that reports green has reported, and a next phase
built on that report is built on prose. The section below already says this
of the reviewer's report; nothing said it of the implementer's until
2026-09-05. The broad gate still runs once, after the rounds settle
(`agent-contract` §2) — this is the narrow run at each phase boundary, and it
is yours rather than the phase's. A phase boundary is never that moment: the
gate comes due when the last round record has no finding open, which is a
record no phase writes.

## Orchestrator: verify before posting

Never post reviewer output as-is. Check, by opening the coordinates yourself:

1. Coordinates behind every highest-severity finding — heaviest, hardest to retract.
2. "This state can occur" claims — constraints/enums/defaults may forbid the state.
3. Spec citations (clause numbers move while a review runs).
4. Test-pass claims — run them; count skips, which masquerade as passes.

Also check whether HEAD moved during the review; if source changed, those
verdicts need a re-pass, and the next round's `target:` line names the new HEAD.

## Orchestrator: closing the cycle

Once the report is verified, mark the reviewed state so the commit gate (this
plugin's PreToolUse hook) can recognize the cycle. Reviewer workers never write
this mark — a review that certifies itself is what the gate exists to catch.

```bash
git rev-parse HEAD > "$(git rev-parse --git-dir)/specseal-reviewed"
```

A commit closes the cycle; the next change starts an unreviewed one.

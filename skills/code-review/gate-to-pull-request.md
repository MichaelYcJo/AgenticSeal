# code-review, from the preflight to the open pull request

This file is the orchestrator's, opened at the step
`skills/code-review/SKILL.md` names. `skills/code-review/orchestration.md`
*Orchestrator: the pull request opens once the sealer seals* states when
the pull request opens and what the body's first part holds. This file
holds the steps that get it there and the repairs an open pull request
takes.

## Orchestrator: from the preflight to the open pull request

Once `guarantee.md` reading `sealed` is committed, run `seal pr-body` once
more on the body file the sealer read, and open the pull request with it,
`gh pr create --body-file <that file>`. That run changes no copied line and
writes the seal mark where the repository turns it on
(`docs/forms/the-guarantee.md` *The guarantee*). CI runs then, and again on
every push to it. The pull request's check reads the body against what
`seal pr-body` composes at HEAD and refuses a ready pull request at each
line where they differ (`skills/code-review/scripts/chain_check.py#body`).
Such a refusal asks for `seal pr-body` once more on the body file, and the
file sent to the open pull request with the `gh api -X PATCH` call below.
No sealer runs for it, since the body is not a record.

**The orchestrator runs `seal pr-wait <N> --once` before each push to the
pull request's branch, and `seal pr-wait <N>` when the pull request opens
and after each push, and acts on the exit code as the table below gives
it.** The wait reads pull request N's checks at the checkout's HEAD, which
is the commit the orchestrator pushed last. It reads the checks of every
workflow on the pull request, because a single workflow's run, watched
alone, can pass while another workflow's check fails. Its one limit is on
the start, the time for a check of a `pull_request` run to be listed on
HEAD. Once one is listed, no time limit applies: the wait ends when no
check is pending, or at exit 3 where the pull request's head leaves HEAD,
since no check of HEAD can be read after that. The read before a push
reads the pull request's state alone, waits on nothing, and exits 0, 4 or
5.

| Exit | When | What the orchestrator does |
|---|---|---|
| 0 | every check on HEAD passed or was skipped; under `--once`, the pull request is open | treats the pull request as checked at HEAD; under `--once`, pushes |
| 1 | a check on HEAD failed or was cancelled, and the output names each such check | reads the named checks' logs and repairs the work |
| 2 | the command could not ask `gh` or `git`, or could not read the answer, and the output names the command and what it printed | reads the output, and takes nothing about the pull request as known |
| 3 | within the limit on the start, the pull request's head never became HEAD, GitHub never said whether the pull request is mergeable, or no check of a `pull_request` run was listed on HEAD; or, after the start, the head left HEAD. The output names the one cause that held and the commits it concerns | says in its report the cause the output names about those commits, waits no longer, and does not treat the pull request as checked |
| 4 | `state` is `MERGED` | pushes nothing more to the branch, and puts the repair on a new branch cut from the base, which holds the work |
| 5 | `state` is `CLOSED` | pushes nothing, and says in its report that the pull request was closed with a repair pending |
| 6 | `state` is `OPEN` and `mergeable` is `CONFLICTING` | merges the base into the branch, as `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* states for a conflict with the base |

**The stated limit: a defect that only one platform shows, in work nobody
expected to be platform-specific, is found when the pull request opens,
after the sealer.** Its fix is a commit outside the work item's records, so
it takes the repair path below: a verifying round on its diff, the broad run
again, and the sealer again. Nothing else is built for it. The pull request
stays open through that repair. Once the repair's broad run is committed,
the orchestrator runs `seal pr-body` on the body file again and gives the
file to the open pull request with
`gh api -X PATCH repos/<owner>/<repo>/pulls/<N> -F body=@<file>`, not
`gh pr edit`: that command's GraphQL query has stopped on an error about
Projects (classic), and the REST call sends the body alone. Whenever the
sealer's next `sealed` verdict is committed while the pull request is open,
after this repair, a merge from the base or any other repair, run
`seal pr-body` on the file once more and send it the same way. The body
sent before that verdict carries no seal mark, since the seal it stood on
no longer held at HEAD, and only a run after the verdict can write the mark
the `Pull request seal mark` key asks for.

**A repository that still opens a draft is not refused.** On a draft
`chain_check` prints what it would refuse and exits 0, and `hygiene`'s
`ready_for_review` event re-runs it when the draft is marked ready, so the
record is still owed then. Nothing that can reach `main` is exempt.

**`trail/gate.md` and `guarantee.md` are read at the pull request**, so four
more steps come before it opens: the preflight, the broad run, the pull
request body, and then the sealer's spawn. You take them once the work
item's `changelog.md` states what the work item ships and every row
`skills/implement/orchestration.md` *Orchestrator: drain the rows before
the broad run, and keep the records* names has reached its destination.
The party that builds the work item writes that fragment: the crafter, or you
where `routing.md` answers `Implementation` with `the session`
(`docs/layout/the-record-layout.md` *A change writes fragments, never a shared
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
and writes `guarantee.md` (`docs/forms/the-guarantee.md` *The guarantee*); it
runs nothing broad, and a missing or stale record comes back
`Verdict: withheld reason: no broad run at HEAD`.

**You write the pull request body after `trail/gate.md` is committed,
because the body's copy of the records includes that record.** Run
`seal pr-body <item> --body <scratchpad>/<work-item-id>/pr-body.md`, where
`<item>` is the work item's directory. It writes `pr.<lang>.md` where the
two language keys differ, then `pr.md`, then the line
`skills/code-review/scripts/pr_body.py#HEADING` holds, then the changelog
fragment, then the rest of the records' copy in one fold, as
`docs/forms/the-guarantee.md` *The guarantee* states, and replaces
whatever the file held. On exit 1 its `refused:` lines name a record's file
and line, `pr.md` and `pr.<lang>.md` among the records, a language key
`config.json` lacks, or the work item's directory with the files to repair
named in the line: repair that record or file or write that key, commit it,
and run the command again. Edit nothing in the file; the sealer's
`seal pr-body --check` withholds on a part above the line that is not
`pr.<lang>.md` and `pr.md` as the keys ask for them, and on a part below it
that is not the records' text at HEAD, and the pull request's check refuses
the body sent from it on the same lines.
**Run the command again before every later spawn of the sealer and before
every `gh api -X PATCH` of the body**, so the body holds `pr.md`, its
`pr.<lang>.md` where one stands, and the records as the repair left them.
`skills/commit-pr-convention/SKILL.md` *Pull request bodies* says which
language each part is in.

**On the broad run's exit 1 spawn nothing.** What the word beside each
failing file tells you, and what you do at each word, are
`skills/verify/orchestration.md` *The broad gate*'s. A failing suite that
names no file and counts sessions that stopped part-way, at exit 0 too, had
a pytest session at `HEAD` stop before its end: `records/` in the kept
output says what stopped it, and a stop the branch added is this work's to
repair.
Review a repair that the row *No fix that no round reads* of
`skills/core/SKILL.md` *Judgment is not licence to skip a party* gives to a
round, and run the gate again. On the broad run's exit 2 nothing ran; a
refusal about the key goes to a person, as *A refusal about the `Broad gate`
key* below says.

**Pass the base as a plain branch name, and quote the lines only the gate can
tell.** The gate resolves the base to the ref CI reads, in the order
`docs/running/the-broad-gate.md` *What the gate runs* gives. Quote, as printed,
in your report to the person and not in the pull request body, where
resolving the base moved it, where the run handed itself to the tree's copy
of the gate, and its `outputs kept under seal-gate-<random>/` line. Each is
a fact a reader learns from nowhere else, and the gate prints it after the
last round, so no record holds it and `pr.md` cannot quote it.

**Commit `guarantee.md`; a verdict other than `sealed` opens no pull
request.** `withheld` names the claim and the coordinate. Where the row *No
fix that no round reads* of `skills/core/SKILL.md` *Judgment is not licence
to skip a party* gives the repair to the sealer, as it does a repair to a
phase record, the changelog fragment or `pr.md`, make it, commit what it
changed in the records, run `seal pr-body` on the body file again, and spawn
the sealer again at the new HEAD, giving a repaired body to a pull request
already open as the stated limit above says. Whether the broad run is owed
again for that commit is `skills/code-review/orchestration.md`
*Orchestrator: the pull request opens once the sealer seals*'s.
Where the core's row gives it to a round it is a fix nobody reviewed: commit
it, spawn
a verifying round on its diff, and once that round's record is committed run
the broad gate again, commit its record, run `seal pr-body` on the body file
again, and spawn the sealer. Your broad run
asks the records arm after its suite, and that arm refuses a commit outside
the work item after the last round's `target:` commit, so a run taken
straight after the fix returns the same refusal. `undecided` is a question
for the owner, put after the run rather than during it; write the answer below the newest
verdict block as `Answered <date> by <who>: <answer>`, commit, and spawn the
sealer again.
`withheld reason: the base <name> resolves to no commit here` needs no
commit: a `git clone` of the branch worktree copies its branches and none
of its `origin/` refs, so spawn the sealer again with the branch worktree
itself as its clone, where `origin/<base>` or, with no remote, `<base>`
resolves.
Where the guarantee's newest verdict block names a commit the branch does
not hold, which the pull request's check refuses as stale, spawn the sealer
again at HEAD and commit what it writes; never edit a block by hand. The
sealer's `seal stamp --guarantee` recorded the refusal, so the new audit,
whose block stands below the refused verdict's block, draws the work item's
stamp (`docs/checks/the-stamp.md` *The stamp*).

**The preflight is yours, and it is not the broad gate.** It runs every
arm of the gate except the `Broad gate` command, in the gate's order and over
the same resolved base, once every refusal of the key has been applied; the
key is read and its command is not run. It takes seconds where the broad
run takes a suite, so a refusal on a record arm, which the broad run would
return after that suite, arrives before it. The chain arm judges as at a
ready pull request whatever the pull request's state, so a refusal on a
record arm, a verifying round owed among them, fails the preflight before
the pull request exists. The arms that read what is written after the gate,
`trail/gate.md`, `guarantee.md` and the body, print and do not fail. Read
its exit code directly and take the broad run only on 0. On 1 its `PREFLIGHT FAILED` lines name each
failing arm with its first lines and the file holding the rest: correct the
record, commit, and run it again. On 2 it refused before anything ran, and
a refusal about the key goes to a person, as
*A refusal about the `Broad gate` key* below says. It writes no file and
prints no `BROAD GATE` line, so nothing it prints reads as the broad run's.
A line the check names as not read, a fence near the opener of a `seal`
block, changes no exit code, and its lines are fields of nothing. Where the
preflight's output or the proofer's hand-back names one, read it against the
record's template: where it meant a block, correct its opener to three
backticks and `seal` alone, commit, and run the preflight again.
An orchestrator that skips the preflight loses only time: the broad run asks
the same arms, and refuses the same way after its suite.

**The stamp is drawn for you at the end of the turn in which the sealer's
report arrives, and you never draw one.** The broad run
draws nothing: its stdout opens `BROAD GATE PASSED` or `BROAD GATE FAILED`,
which say whether the broad command passed and judge nothing. The stamp is
drawn once per work item from the sealer's verdict
(`docs/checks/the-stamp.md` *The stamp*): where the newest verdict block of
`guarantee.md` reads `Verdict: sealed` and the block reader refuses none of
its lines, the sealer's `seal stamp --guarantee` queues the stamp's values,
under either root, and the plugin's `Stop` hook draws them after your text.
The line naming them arrives in the sealer's hand-back.
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
sealer's hand-back carries that line; quote it in the turn's text. The line
names the command because the plugin's `Stop` hook draws nothing where it
cannot: a `python3` that cannot load `seal_stamp.py`, or a working
directory outside the clone. Where the hand-back carries no such line,
no stamp was queued and none is drawn, and the pull request's check is what
says the work item was sealed.

**A refusal about the `Broad gate` key goes to a person, and the run stops
until they answer.** Your broad run comes back exit 2 two ways that are
about the key rather than about the work: the repository declares no key, or
its key holds a command the gate would not run as the command it reads as.
Neither is yours to settle, and no agent's: the key is the one value in this
flow only a person may write, because there is no default and the broad run
covers exactly what a person wrote. Put the gate's own sentence in front of
whoever owns the repository, name `/agentic:config` as where they answer it, and
open no pull request until they have. A key filled in to get past the
refusal makes the broad run cover a command the person never saw.

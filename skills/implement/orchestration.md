# implement, the orchestrator's half

This file is the orchestrator's: the session that starts a work item, asks
the person what only the person can answer, and spawns the agents. It holds
the order of the parties, the fold of a decision made after the frame, the
one batch of questions asked before the first edit, the rows of the routing
declaration, the route chosen under `agentic`, the ladder that says whether
a work item has a frame, the drain before the broad run, and where a
decision or a lesson is written. Where no `seal/` whose `README.md` opens
with the marker stands at any of the places the opening paragraph of
`skills/core/SKILL.md` names, which `seal mode` answers by exiting 1, the
orchestrator reads `skills/implement/bootstrap.md` first.

`skills/implement/SKILL.md` is the other half, and the orchestrator reads
both. The crafter opens that one at its first step and never this one,
because asking a person and writing `routing.md` are acts
`agents/crafter.md` leaves to the orchestrator. Every `seal/…` path here
resolves as `skills/implement/SKILL.md` *Document layout — two roots, three
lifetimes* states (contract rule 11).

## Orchestrator: the order inside a ticket

1. The orchestrator branches from the release branch and writes `routing.md`
   before the first edit (*Orchestrator: how the work is routed* below).
   The orchestrator makes the branch with `git switch`, and a worktree only
   where another session works in the same clone at the same time.
   Before the first edit the orchestrator holds the core once, which the
   plugin's `SessionStart` hook printed where a `seal/` root stood when the
   session started. Where no output opening `AgenticSeal core from` stands
   in the session's context, the orchestrator opens `skills/core/SKILL.md`
   once. The orchestrator opens `skills/agent-contract/SKILL.md` once,
   beside the core. In every route, the orchestrator's own commands, its
   commits and the broad run among them, follow contract rule 21. The text
   the orchestrator's commits write, its record edits, its folds of what a
   crafter names, `pr.md`, the rows of *Judgments of the run* and a merge's
   resolution among them, follows contract rule 19. By contract rule 4 and
   contract rule 5, a fact that text states of a commit, a run or the tree
   is one that a command the orchestrator ran printed or a file it opened
   showed, and a fact it holds from its memory of the run it opens again
   before it writes it. Where the orchestrator builds or fixes itself, every
   rule of that file binds it as the builder `skills/implement/SKILL.md`
   *The builder is the party that builds a phase or makes a fix pass* names.
2. The framer writes `frame/design.md`, `plan.md` and `questions.md`. The orchestrator
   reads the frame against the issue, settles what it finds with the framer
   and spawns the crafter, or builds itself where `routing.md` answers
   `Implementation` with `the session` (*The frame is read against the
   issue at the spawn* below). Once the build's last phase has closed, the
   orchestrator writes and commits the work item's `pr.md`, the pull request body's
   first part, with its `pr.<lang>.md` where the two language keys differ,
   before the first round. The proofer's rounds follow, then
   `seal gate --preflight` and `seal gate --record`, both run by the
   orchestrator, then `seal pr-body`, which the orchestrator runs to write
   the pull request body from `pr.md` and the records, then the sealer,
   and then the pull request opens
   (`skills/code-review/orchestration.md` *Orchestrator: the pull request
   opens once the sealer seals* owns when). Once the pull request is open,
   the orchestrator removes the work item's scratch directory,
   `<scratchpad>/<work-item-id>/`, in one `rm -rf` whose path is written
   out in full, with no variable in it, and removes nothing else of the
   scratchpad. It runs the same command again after each repair it pushes
   to the open pull request, a merge from the base among them, because the
   repair's round and audit clone again. No agent removes a scratch
   directory (contract rule 17).
3. The pull request body carries `Closes #N`, from the work item's `pr.md`
   where the work runs through the review chain; the release workflow
   closes the ticket when the release reaches `main`.

**A decision made after the frame is committed is folded, in place, into
`frame/design.md` or `plan.md` before the next crafter spawns or is
resumed.** A crafter reads the frame and not the issue's comments, so the
decision has to stand in the frame. A decision is anything that changes
what the frame says the work is or why: a round finding whose route
changes the frame, a round finding whose fix needs a unit the frame does
not name (`skills/implement/fix-pass.md` *A fix that needs a unit the
frame does not name waits for the fold*), a round finding located in a
frame file, an owner's remark, an issue comment, a prevention home, a
scope a spawn gives beyond a plan row, or the version move. These are
examples of the rule, not a closed list. The orchestrator sends a finding
whose fix needs such a unit to the framer with the round's other
decisions, before the fix pass, where its paste-ready fix or its grounds
show the unit, and when the fix pass's hand-back names it otherwise.

**The framer writes a decision's fold, because the framer judges what the
work should be.** `skills/implement/fold-and-reframe.md` states the fold,
and `skills/core/SKILL.md` *Each agent judges its own target, independently
of the others* the reason. A statement the framer's hand-back names in
`routing.md` or `pr.md` is the orchestrator's to repair. A statement a
crafter's hand-back names in a frame file or `routing.md` records what the
build changed rather than what the work is, so the orchestrator folds it in
a commit of its own and spawns no framer. A fold whose source is what a fix
or a build changed removes the frame sentence HEAD contradicts, or narrows
it to what HEAD still holds, and writes no new account of what was built,
since the code, its docstring, the phase record and the finding's close
block hold that. That fold is the orchestrator's, of a statement a
crafter's hand-back names, and the framer's, of a round finding that says
a frame sentence no longer holds. A statement found in a file the
crafter writes, `gaps.md` or `changelog.md`, goes to a fix pass before the
orchestrator spawns the next round or phase. That fix pass is the
implementer's, and `skills/code-review/orchestration.md` *Orchestrator: a
phase is a fresh crafter, and a fix pass resumes the implementer* defines
the implementer.

**One fold reaches every statement of the fact it changes.** Before the
spawn or the resume that will read the decisions, the orchestrator sends
every decision then pending to the framer in one message, each with its
grounds and the coordinates it stands on: the finding, the comment or the
owner's words.
The fact a decision changes often stands in sections the decision does not
name, such as *Scope*, *Removes*, *Alternatives considered*, *Judgments of
the run*, *Grounding* and *Technical context*, so the message names the
fact and says that its coordinates are the statements the orchestrator has
seen, not the whole list. The statements a crafter's hand-back names are
its reading of a file it does not write, so the orchestrator reads each
file that holds one whole against HEAD, not only the named line, and
folds every statement HEAD contradicts. In a section the frame dates to
the commit it read, a statement of the tree is not folded, and a sentence
that says what the work does or concludes is rewritten with a decision's
fact, and is otherwise folded as the paragraph opening **The framer writes
a decision's fold** states; a section that states the tree with no date
gets the date and keeps its text (`skills/implement/SKILL.md` *Document
layout — two roots, three lifetimes*). After a fold commit of its own, the
orchestrator reads that commit and each file of the work item's directory
that states the present whole against HEAD, the second method of contract
rule 12; a decision's fold is read by the framer that writes it.

**The orchestrator writes its row before it sends a decision, and commits
the fold before the spawn or the resume.** Until a decision is folded, the
orchestrator keeps one line of its own in `plan.md` naming the comments to
fold, below the title, and deletes that line in the commit that folds
them. Before it sends, the orchestrator writes each decision, its grounds
and the document it judged against as one row of `frame/plan.md`
*Judgments of the run* and leaves the row uncommitted, so the framer reads
the row when it reads
`plan.md` whole: the rewritten sentence keeps no reason for itself, and the
settle reads the row. A row of *Judgments of the run*, this one or any
other the orchestrator writes, names any commit only as a coordinate, and
gives no inventory of a change, whether a commit holds the change or the
change is still to come, as a fold's is when its row is written: no number
of lines, sentences or items, no list of what the change rewrote or will
rewrite, and no word for the kind of change a fold made or will make.
What a row sends, the findings and the files or sections a fold or a fix
pass is given, is its decision and the decision's coordinates, and not
that inventory. `git show <commit>` is that account once the commit exists.
A row whose judgment is about a change, such as a regression's route
(`skills/code-review/orchestration.md` *A regression is routed by comparing
the fix with the frame*) or why the title takes its prefix, states as its
grounds what the change means against the document it judges against, and
no inventory of it. The orchestrator resumes the work item's framer while
that session still exists, as a fix pass resumes the implementer, and
otherwise spawns a fresh framer and hands it the decisions and the commit
at which the frame was last written. The message that resumes the framer,
and the prompt that spawns a fresh one, each name
`skills/implement/fold-and-reframe.md` for the framer to open before it
answers. The row for a fold states the decision as it was sent. After the
fold the orchestrator changes it only where the framer's hand-back, a
round's finding or the sealer's verdict names a defect in it, which it
corrects, or where the framer rejects the decision, as the next paragraph
states. It then commits the frame files the framer
changed and its own rows in one commit, before the spawn or the resume
that reads them.

**A decision the framer rejects stands as its judgment, as a proposal left
after the exchange of *The frame is read against the issue at the spawn*
does.** The orchestrator rewrites its row of *Judgments of the run* to
record the rejection and what the decision's source takes instead, a
finding's route or the next spawn's scope, and quotes the framer's
*Alternatives considered* row in the work item's `pr.md`. The version move
and a prevention home are folded as an owner's decision is, because another
rule gives each to the orchestrator to decide: the move by *Orchestrator:
how the work is routed*, and the home by the paragraph opening *A problem
that recurs within a run gets a prevention home at once*. Where a crafter
builds the work item that carries the move and its `frame/plan.md`
*Operational impact* does not name it, the framer folds the move into that
section before the orchestrator spawns the last phase, because the crafter
reads its version write there.

**Before the frame is committed, the orchestrator folds a decision into the
issue body instead, in place.** The comment that carried it records why. A
body that contradicts a comment, or a block of updates written above the
old text, leaves the reader two versions to choose between, and GitHub
keeps the body's edit history, so rewriting it loses nothing. The
orchestrator's prompt that spawns the framer hands it the issue whole: the
body as folded, and one line naming the comments the issue has, none or
each comment's link, with the command that read them,
`gh issue view <N> --json body,comments`, and the date it ran.

**Where a work item stands is read from `plan.md`'s Status column,
`gaps.md` and the phase records.** The orchestrator that hands the work
over writes a `handoff.md` in the work item's directory only to move the
work to another session or another machine. The orchestrator that takes the
work over deletes it once it has read it.

**A problem that recurs within a run gets a prevention home at once.** When
the same problem appears a second time in one run, the orchestrator gives it
a home before the next spawn or resume: a mechanism that stops it, or a
rule written into the file the recurring act is read from. The work item
in progress builds that home. The home is a decision, so the framer folds
it into that work item's frame as the paragraph opening *A decision made
after the frame is committed is folded* states, and the orchestrator
records the home in a comment on the issue of the work item in progress.

### The frame is read against the issue at the spawn

**Wherever a framer drew the frame, the orchestrator reads
`frame/design.md` and `frame/plan.md` against the issue's decisions and its
*Done when* before the first crafter spawn, or before its own first edit
of the build where it builds itself, and settles what it finds with the
framer in one exchange.** It looks for where the frame is weaker than the
issue asks, departs from the issue's direction, or would grow the review
load. Each
reading goes to the framer in one message, as a proposal with its grounds
and coordinates and never as an instruction. The framer answers each with
agree, agree with a change, or reject with grounds, folds what it agreed
into its three files, and writes each rejected proposal as one row of
`plan.md`'s *Alternatives considered*; the orchestrator edits no frame file.
One exchange is the bound: a disagreement left after it stands as the
framer's judgment, which the orchestrator quotes in the work item's
`pr.md` from its `frame/plan.md` *Alternatives considered* row, because
each party judges its own target
(`skills/core/SKILL.md` *Each agent judges its own target, independently of
the others*) and a second round would be the orchestrator overriding the
framer. The spawn is the approval (`skills/implement/SKILL.md` *3. The SDD
file set*), so a frame spawned as committed, with no proposal, takes no row
of `frame/plan.md` *Judgments of the run*, and a question built on its
default stands in `frame/questions.md` alone. The counts of the run's
proposals, agreements, agreements with a change and rejections go into the
run's comment on the flow log
(`skills/verify/orchestration.md` *Measure the run, and feed the flow
log*), and the settle weighs the exchange against what it cost under the
core's mechanism rule.

**The spawn prompt is text an agent reads.** The orchestrator writes it to
the rules of `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한
가지로만 읽히게 쓴다*: each fact it hands over carries its coordinate or its
label (`docs/running/the-run.md` *The handoff*), and each instruction names
who acts, on which file, and what counts as done.

## Orchestrator: what needs a person is asked in one batch, before the first edit

**Collect what needs a person before the first edit, and ask it in one batch.**
The orchestrator reads the policy, the SDD set and each ticket the person's
request names, looking for the questions as well as the answers, and puts
every one of them in front of the person at the start: a decision only they
can make, an approval, a credential, a permission the session does not have.
Before it puts the batch, the orchestrator reads the *Done when* of every
issue the request names, and puts in the batch each line there that needs a
real session, a credential, an outside service or a permission. A *Done
when* line is what the run must deliver, so a need it carries that the batch
missed stops the run when the work reaches that line.

**A request that names several issues, such as a milestone or a release, has
one batch, and the batch covers every one of them.** The orchestrator asks it
once, before the first edit of the request's first work item. A later work
item of the same request asks nothing new when it starts. Its `routing.md` is
written from the routing answer the batch got. An answer the batch gave for
its issue is folded into that issue's body, as *Orchestrator: the order inside
a ticket* states for a decision made before the frame is committed. What
surfaces when a later work item starts goes where the paragraph opening *Once
the batch is answered* sends it. A new request is asked a batch of its own,
question 1 of `skills/implement/routing-question.md` among it.

The cost of a question is not its difficulty, it is when it arrives. Asked
before the work starts, it costs a reply. Asked at minute thirty, it stops
everything until someone is at the keyboard — and the longer a session is
meant to run unattended, the more of it a late question wastes. Asking one at
a time is the same failure spread out: three interruptions cost three waits.

Two things sharpen the list:

- **A question you can answer is not a question.** Read the documents and the
  code first. An issue's line that leaves a decision to a person is a claim
  dated by the issue: it records what was open when the issue was filed.
  Before its question enters the batch, the orchestrator checks it against
  the policy root, `seal/config.json`, the code, and the records under
  `seal/threads/` of the work items that came before. Where they answer it,
  the orchestrator does not ask. It writes the answer with its coordinate in
  *Why this way* of the `routing.md` of the work item the issue opens, when
  it writes that `routing.md` at the item's start. For a later work item of
  the request, it checks the line against the tree again at that start. For
  `direct`, the answer goes in the body of the commit that carries the
  change. What survives that is the batch.
- **Assume, in writing, whatever would not change what you build.** State the
  assumption in `questions.md` and continue. Only where different answers mean
  different code does the work actually have to wait.

Something a session cannot do for itself belongs on the same list — widening
its own permissions, for one, which the harness blocks by design. Better
found in the first minute than at the commit.

**A rule that restricts what agents may do in a run comes only from the
person's answer in this run's batch or from a policy document.** The
orchestrator writes such a rule under `## Why this way` in the work item's
`routing.md`, with its source: the batch question and its answer, or the
document's path and section. A spawn prompt carries such a rule only as that
`routing.md` states it. A rule a person gave for an earlier run bound that
run alone, and the orchestrator does not carry it into this one. A rule with
no source in this run turns a step an agent could take into a question only
the person can lift, and under `Automation` `yes` nobody is there to lift it.

**Once the batch is answered, the session runs to the pull request, through
every work item the request names.** What surfaces after it is written down
rather than raised: a decision only a person
can make goes to `questions.md`, a finding you neither fixed nor answered to
`seal/follow-up.md` with an answerer named — a deferral to nobody is how
"someone will look at it" becomes nobody did (`skills/verify/SKILL.md` *The
answerer has to exist*) — and what was deliberately left goes to the closing
memo's Not done section. Each is named in the PR body, because a leftover
nobody can find was not handed over.

## Orchestrator: how the work is routed

The orchestrator opens `skills/implement/routing-question.md` when it puts
the batch of questions, the routing question among them, to a person, and
where either of the two language keys is missing from `config.json` under
the `seal/` root, which it reads before the routing commit. That file holds
the routing question's two calls, what each answer writes, how a question
of the batch is worded, and what the batch does about the two keys.

### What the answer writes

| Row | Answers |
|---|---|
| Automation | `yes` or `no`, OPTIONAL; absent reads as never asked |
| Implementation | `crafter` or `the session`, OPTIONAL; absent reads as unanswered |
| Review | `through the review chain` or `straight to the PR` |
| Destination | `open the pull request` or `stop before the pull request` |
| Branch | the branch the work item is built on; two declarations naming one branch read as none |

**Each answer is written without backticks**, and the file starts from
`templates/records/sdd-routing.md`, which ships `Review` and `Destination`
answered and the optional rows as placeholders. An absent `Automation` row
means nobody was asked, so `no` is never written where the question was not
put; under `agentic` the person's answer puts it to the orchestrator, which
writes `yes` or `no` (*Under agentic*). The grounds of both are
`docs/running/the-review-and-parity-arms.md` *The declaration, and where
the check went*.

**`Implementation` is answered by whether the work is finding out or writing
down.** Finding out is a step to send to `tracer`, and the orchestrator that
reads the facts back and writes the code still answers `the session`;
`crafter` answers where the diff is large enough to threaten what the
orchestrator still has to hold (`docs/running/the-agent-set.md` *What a spawn
costs*). The file ends with `## Why this way`: one or two sentences where
the person chose the rows, and where the orchestrator chose them under
`agentic`, the grounds *Under agentic* asks for, which the sealer reads
against the diff (`agents/sealer.md` step 4).

**While the `Automation` row reads `yes`, the plugin's `PreToolUse` hook puts
the rule for the run in front of the orchestrator at each `AskUserQuestion`
call.** The rule is the paragraph of `docs/running/the-run.md` *The run* that
opens **On a run whose `routing.md` reads `Automation` `yes`**, and the
orchestrator follows it. The hook, `hooks/ask-under-automation.py`, refuses
an `AskUserQuestion` call while the `routing.md` of a work item whose branch
is checked out in a worktree of the repository reads `yes`, and its refusal
prints that paragraph, the open work items and the questions that do not
state why their default cannot be taken. It lets a call through where each
question of the call holds, in its text, the marker
`hooks/ask-under-automation.py#MARKER` gives, followed on the same line by
the reason. The hook does not judge whether a question is one only the owner
can decide: the orchestrator writes why, and the person reads it in the
question. The pull request's check decides nothing on the row.

**The declaration has one more row, and nobody is asked about it.**

| Axis | Answers |
|---|---|
| Planning | `framer` or `the session`, OPTIONAL; absent reads as unanswered |

It is a record, not a box. The question grows only where a decision is a
person's, and this one is not: `agents/framer.md`'s `## Job` says where the
framer runs. The orchestrator fills the row from what happened:
`framer` where the subagent drew the frame, `the session` where the
orchestrator drew it, and no row where no frame was called for or chosen.

**The orchestrator writes the answer down before the first edit**, in
`seal/threads/<work-item-id>/routing.md`, from `templates/records/sdd-routing.md`, and
commits it, because the check happens at the pull request and CI sees only
what is in the tree. Below the SDD ladder this may be the only file a work
item gets. No check refuses an earlier edit; the pull request's check judges
the declared work item, and a session that declares nothing is the limit
`docs/checks/the-routing-check.md` states.

**The orchestrator writes the file with the `Write` tool, then commits it.**
The commit goes as every commit does: each work item's `routing.md` in a
command of its own, the worktree's path written out after `git -C`, never a
loop over a variable naming it (`skills/implement/SKILL.md` *A commit names
its repository in the command that makes it*).

**What each combination of `Review` and `Destination` checks, and where**,
is `docs/running/the-review-and-parity-arms.md` *The declaration, and where the
check went*. Under `stop before the pull request` nothing runs at the end,
and the orchestrator says so in the handback.

**Where a migration config is declared, the comparison with the original is
recorded where the answer puts it**, as `skills/legacy-parity/SKILL.md`
*Recording the comparison* and `docs/running/the-review-and-parity-arms.md`
*Parity arm* state.

Work never headed for a reviewer, such as a release chore or a
documentation pass, declares `straight to the PR`. A change belonging to no
work item writes no declaration, and where the root is shared each of its
commits' trailers reads `no work item`
(`skills/commit-pr-convention/SKILL.md`).

**Which branch the pull request lands on is decided with the routing
question.** A pull request into the release branch is not a release: its
entry accumulates unreleased. Whether it moves the version is the
repository's convention. Where the repository names the version when it
cuts the release branch, as a branch named `release/vX.Y.Z` does, the
version moves to that name in the first pull request into the branch, and
every later pull request into the branch leaves it. The party that writes
that work item's changelog entry moves it, in the commit that adds the
entry: the last phase's crafter where `routing.md` answers
`Implementation` with `crafter`, and the orchestrator where it answers
`the session`. The orchestrator chooses which work item carries the move.
Where the release holds another work item, the orchestrator opens
`skills/implement/merge-order.md` when it starts this one, before its first
edit: that file holds what each framer's prompt names, the order the items
merge in, and which of them takes the move. Where the
repository moves the version at the release, a pull request into the
release branch leaves it alone. A pull request into `main` is a release:
the accumulated entries go out under the version, which moves there only
where it has not moved already, and the tag follows the merge. The release
branch is the default. The orchestrator takes `main` when the accumulated
entries read as one release, or when the change is a gate or a hook firing
where it should not, which does not wait for other changes.

**Where an entry accumulates is the repository's convention, so the
orchestrator reads it before the entry is written.** Two shapes are common
and they are not interchangeable: a heading in the changelog that every
branch appends to, or one fragment per work item that a release gathers.
Writing the first into a repository that uses the second invents a heading
its checks refuse, or appends to the shared region the fragments exist to
empty. Where the
repository gathers fragments, basing on `main` means running the gather,
because `main` is the branch where the entries are due; the contribution
guide names the command.

**The declaration moves the check and waives nothing**:
`straight to the PR` turns off the reviewer, and the broad run is owed just
the same
(`docs/running/the-review-and-parity-arms.md` *There is no standing waiver*).

**A work item that commits in more than one repository** asks the routing
question once and writes every answer into each gated repository it commits
in, by the procedure `skills/implement/multi-repository.md` holds.

### Under agentic

**What `agentic` buys is time.** The orchestrator reads each work item's
issue and the tree, and turns off every party the item does not need, so
two items of one batch may take different routes. What follows is what it
weighs, not a sequence to run (`skills/core/SKILL.md` *A rule is guidance
for a judgment, not a sequence to execute*).

**`direct` is weighed on four signals, and none of them is a bound**: the
change's size; what it touches; whether a gate, a hook or a check script is
among what it touches; and how a defect in it would show, as a suite that
fails at the pull request or as an agent that misreads the text in a later
run. A small change whose defect would show at once takes `direct`. A
change that touches a gate or a hook takes a work item, because a defect
there stops every session that runs it. So does a change that restates a
rule other text states, because finding every statement of the rule is a
reader's work (contract rule 12). The item's rung on the ladder of
*Orchestrator: when a work item is required* below is read beside these
signals and does not bound them: the ladder sorts by behaviour and not by
size, so as the bound it would send a two-line fix of an agent's
instructions through every party.

**Each row is chosen for what the item needs**, in the vocabulary of *What
the answer writes* above:

- **Planning**: `framer` where the issue leaves a design choice open, or
  where the work changes a rule several documents state; `the session`
  where the issue fixes the change at its coordinate; no row where the item
  needs no frame.
- **Implementation**: by the criterion *What the answer writes* states.
- **Review**: `through the review chain` where a reader independent of the
  build is worth its rounds; `straight to the PR` where the sealer's single
  reading of the diff against the issue is enough.
- **Automation**: `yes` where every question the orchestrator foresees has
  a default the tree or the framer can give; `no` where the item reaches
  outside the repository, or waits on a decision only a person can make
  that the build has to reveal first.
- **Destination**: `open the pull request`, as under `complete`, unless the
  issue or the person's words in the batch ask for the branch back.

**Three combinations do not stand, and every other one does.**

| Combination | Why it does not stand |
|---|---|
| a work item whose pull request opens without the broad run or without the seal | `skills/core/SKILL.md` *Judgment is not licence to skip a party*; only `direct`, which opens no work item, goes without both |
| `crafter` building with no frame | the crafter builds a phase of `frame/plan.md` and fills its Status cell (`agents/crafter.md` *Order of work*) |
| `framer` recorded where `frame/design.md`'s mark names anyone else | `chain_check.py` refuses it |

A framer and nothing more stands among the rest: `framer` for planning,
`the session` for the build, and `straight to the PR`.

**Where the choice is written.** For a work item the rows go into
`routing.md`, whose line reads
`Answered <date> by the orchestrator, before the first edit.`, and *Why
this way* names the person who answered question 1 and that answer, then
gives each row's grounds with this subsection as the document judged
against. For `direct`, the body of the commit that carries the change
holds one sentence of grounds, above the trailer.

**A route is raised when the work outgrows it, and never lowered.** A
`direct` change that grows past its grounds becomes a work item, with its
`routing.md`, before its next commit; the commits already made keep their
trailer, and the pull request's check prints them rather than refusing
them (`docs/checks/the-routing-check.md` *At the pull request*). A work
item routed `straight to the PR` takes the review chain where its diff
reaches what its grounds did not name, or where its sealer withholds on
that. Each raise is a row of `frame/plan.md` *Judgments of the run* where a
plan stands, and otherwise a sentence added under *Why this way*. A route
is not lowered when the build turns out smaller, because the orchestrator
would then waive a reader of a diff it has read itself
(`skills/core/SKILL.md` *Each agent judges its own target, independently
of the others*).

## Orchestrator: when a work item is required

**When a work item is required** — the same threshold the Design Gate uses,
because they are the same judgment. Drawing no line is how the set quietly
stops being written. Under `complete` and `manual` the rung decides what a
work item writes; under `agentic` it is one signal of those *Under
agentic* above weighs.

| Work | What to write |
|---|---|
| It **alters observable behaviour** — a gate's verdict, a hook's output, a skill's or agent's instructions, a public API, text a person reads and acts on. Or it changes a value someone waits on or is limited by — a timeout, a retry count, a rate, a size cap — and NAMING that value is what puts it on this rung | `frame/design.md` and `plan.md` **before** implementing — approval of `plan.md` IS the gate — then the closing memo |
| It alters none of that and is more than one line — a refactor, a performance pass, a formatting sweep, a test that pins what already holds. These four are DEFAULTS, not a closed list: a performance pass that moves a timeout a person waits on belongs on the rung above, and the value's name is what moves it | the closing memo. A one-line scope confirmation replaces the plan |
| A typo, a config value, a one-line fix | nothing |

**Behaviour, not file count, and the difference runs both ways.**

- **One file, and it qualifies.** A change to an agent's persona is two files
  of wording, and wording is what a session reads and acts on, so it needs a
  plan at file one.
- **Many files, and it does not.** Copying test repositories instead of
  running `git init` for each touched many files and altered nothing
  anyone can observe — no verdict, no output, no instruction. The suite runs
  faster and says the same things.

A count also has to say **when** it is taken, and the gate it guards — plan
approval — exists only before the first edit (issue #35); a test with no
number has no such moment, so the question stops needing an answer.

The way out of a default is to NAME the value a person waits on or is
limited by, which a reader can open and check. *I judged it observable* is
not something anyone can check, and it is not a way out.

## Orchestrator: drain the rows before the broad run, and keep the records

**A row whose destination stands outside `seal/threads/<work-item-id>/` is
committed before the round that reads it.** Such a row is a
`seal/follow-up.md` row or a policy document written directly, and its
commit is one that `docs/checks/the-pull-request-check.md` *What the check
reads at the pull request* gives to a round. The orchestrator commits a
leftover a crafter's hand-back names before it spawns the round after that
phase or fix pass, and a finding it defers in a round record before the
verifying round, where another finding of that round takes a fix pass.

**Every other row moves out once the last round record has no finding
open, and before the orchestrator runs `seal gate --preflight`**, whichever
party `routing.md`'s `Implementation` row names: a row whose destination
stands inside the work item's directory, and a row that makes no commit,
such as an issue or a comment on one. The orchestrator opens the pull
request, and every commit after the broad run leaves `trail/gate.md` stale
for the sealer (`skills/code-review/gate-to-pull-request.md`
*Orchestrator: from the preflight to the open pull request*).

**A row that first arises once no round is to follow is weighed.** Its
commit outside the work item's directory costs the verifying round
`docs/checks/the-pull-request-check.md` *What the check reads at the pull
request* names, and a home that needs no such commit costs none. The homes
are those `docs/running/the-run.md` *The run* gives.

A row is out when it stands at its destination below:

| Remaining item | Destination |
|---|---|
| Doable within this pull request | done now, by the party that builds the work item, and reviewed by a verifying round before the broad run, unless the sealer reads its fix, by the row *No fix that no round reads* of `skills/core/SKILL.md` *Judgment is not licence to skip a party*. Once a row of `frame/plan.md` *Judgments of the run* judges the run excessive, only a `must`, or an item whose fix the sealer reads by that row of the core, is done now, and every other item takes a home that costs no round, as `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* states |
| Waiting on prerequisite work | `seal/follow-up.md` |
| Needs a decision | the policy document's open-questions section: written there directly where the work item's subject is the policy root, and otherwise an `add` in `frame/design.md`'s `## Rule changes` (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*) |

Each finding that moves out reads `deferred <home>` in its round record. The
records themselves stay through the merge, and leave with their work item's
directory at the settle after its release.

## Orchestrator: where a decision or a lesson is written

**The orchestrator writes each decision and each lesson of a run into the
repository, never into a session's local memory.** The harness keeps that
memory on one machine, outside the repository, so a rule kept there is
unknown to a run on any other machine and to anyone who reads the
repository.

| What the orchestrator has | Where the orchestrator writes it |
|---|---|
| a decision about the work item in progress or a file it changes, with its grounds | the work item's records, as `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* states |
| a lesson about how an act is done | the file the act is read from, through the work item in progress where that work item changes the file: a skill or an agent definition edited in place, or a policy document, edited in place where the work item's subject is the policy root and through its `## Rule changes` otherwise (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*) |
| a lesson or a decision whose home no work item in progress changes | an issue that names the home, in the tracker of the repository that holds the home. Where the home is a file the plugin ships and the run is in another repository, the orchestrator names the lesson and the file in its report to the person, who can take it to the tracker the plugin's `.claude-plugin/plugin.json` names under `repository`; it edits no installed copy, which stays on one machine and is replaced at the next update |
| a reading of what a run cost | the log `skills/verify/orchestration.md` *Measure the run, and feed the flow log* names for that reading |

**A lesson seen once is given a home or judged not worth one.** The
orchestrator weighs it under `skills/core/SKILL.md` *The rule a mechanism is
kept against*. A lesson judged not worth a home leaves its grounds in the
work item's records, and nothing else keeps it. A lesson seen a second time
in one run takes the home the paragraph opening **A problem that recurs
within a run gets a prevention home at once** gives it.

Local memory holds what belongs to one machine, such as how that machine
stays awake or where its harness keeps the installed plugin, and how the
person wants to be worked with. A rule in it that another session has to
follow is a lesson with no home yet.

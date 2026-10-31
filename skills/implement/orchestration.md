# implement, the orchestrator's half

This file is the orchestrator's: the session that starts a work item, asks
the person what only the person can answer, and spawns the agents. It holds
the procedure for **starting** a work item: the order of the parties and the
one routing question, asked before the first edit. Where no `seal/` whose
`README.md` opens with the marker exists at `<repo>/seal/` or at
`$(git rev-parse --git-common-dir)/seal/`, the orchestrator reads
`skills/implement/bootstrap.md` first.

`skills/implement/SKILL.md` is the other half: the record language, the
document layout, the procedure that reads the documents before the code, the
test-first cadence, the SDD file set, the closing memo and the review
incorporation. The orchestrator reads both. The crafter opens that one at
its first step and never this one, because asking a person and writing
`routing.md` are acts `agents/crafter.md` leaves to the orchestrator. Every
`seal/…` path here means `<repo>/seal/` where that directory exists with
the marker, and
`$(git rev-parse --git-common-dir)/seal/` otherwise (contract rule 11).
`skills/implement/acts.md` tables each act addressed to the orchestrator in
this file and the files beside it, with what notices when the act is
skipped; a maintainer reads it, and an orchestrating session does not need
to.

## Orchestrator: the order inside a ticket

1. The orchestrator branches from the release branch and writes `routing.md`
   before the first edit (*Orchestrator: how the work is routed* below).
   The orchestrator makes the branch with `git switch`, and a worktree only
   where another session works in the same clone at the same time.
   Before the first edit the orchestrator runs `seal core` once. Where it
   reports no core entry, the orchestrator opens the file the output names
   once, which is then the session's one read of the core, and continues.
   Any other failure the orchestrator says in its next reply, and the work
   goes on.
2. The framer writes `frame/design.md`, `plan.md` and `questions.md`. The orchestrator
   reads the frame against the issue, settles what it finds with the framer
   and spawns the crafter (*The frame is read against the issue at the
   spawn* below). The proofer's rounds follow, then
   `seal gate --preflight` and `seal gate --record`, both run by the
   orchestrator, then `seal pr-body`, which the orchestrator runs to write
   the pull request body's copy of the records, then the sealer, and then
   the pull request opens
   (`skills/code-review/orchestration.md` *Orchestrator: the pull request
   opens once the sealer seals* owns when).
3. The pull request body carries `Closes #N`; the release workflow closes the
   ticket when the release reaches `main`.

**A decision made after the frame is committed is folded, in place, into
`frame/design.md` or `plan.md` before the next crafter spawns.** The orchestrator
rewrites the sentence of the frame the decision changes, where it stands,
because a crafter reads the frame and not the issue's comments. Until the
decision is folded, the orchestrator keeps one line of its own in `plan.md`
naming the comments to fold, below the title, and deletes that line in the
commit that folds them. Before the frame is committed, the orchestrator
folds the decision into the issue body instead
(`docs/issues-and-milestones.md` *An issue is its body and its comments
together*). The orchestrator's prompt that spawns the framer hands it the
issue whole: the body as folded, and one line naming the comments the issue
has, none or each comment's link, with the command that read them,
`gh issue view <N> --json body,comments`, and the date it ran.

**Where a work item stands is read from `plan.md`'s Status column,
`gaps.md` and the phase records.** The orchestrator that hands the work
over writes a `handoff.md` in the work item's directory only to move the
work to another session or another machine. The orchestrator that takes the
work over deletes it once it has read it.

**A problem that recurs within a run gets a prevention home at once.** When
the same problem appears a second time in one run, the orchestrator gives it
a home before the next spawn: a mechanism that stops it, or a rule written
into the file the recurring act is read from. The work item in progress
builds that home. The orchestrator folds it into that work item's frame, as
any decision after the frame is folded, and records the home in a comment on
the issue of the work item in progress.

### The frame is read against the issue at the spawn

**Before the first crafter spawn, wherever a framer drew the frame, the
orchestrator reads `frame/design.md` and `frame/plan.md` against the issue's
decisions and its *Done when*, and settles what it finds with the framer in
one exchange.** It looks for where the frame is weaker than the issue asks,
departs from the issue's direction, or would grow the review load. Each
reading goes to the framer in one message, as a proposal with its grounds
and coordinates and never as an instruction. The framer answers each with
agree, agree with a change, or reject with grounds, folds what it agreed
into its three files, and writes each rejected proposal as one row of
`plan.md`'s *Alternatives considered*; the orchestrator edits no frame file.
One exchange is the bound: a disagreement left after it stands as the
framer's judgment, which the orchestrator names in its part of the pull
request body, because each party judges its own target
(`skills/core/SKILL.md` *Each agent judges its own target, independently of
the others*) and a second round would be the orchestrator overriding the
framer. Reading the plan and spawning the build is the approval, and no line
records it. The counts of the run's proposals, agreements, agreements with a
change and rejections go with the framer segment's reading to the flow log
(`skills/verify/orchestration.md` *Measure the segment, and feed the flow
log*), and the settle weighs the exchange against what it cost under the
core's mechanism rule. Its first instance, #1148's frame: four proposals,
one agreed, two agreed with a change, one rejected.

**The spawn prompt is text an agent reads.** The orchestrator writes it to
the rules of `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한
가지로만 읽히게 쓴다*: each fact it hands over carries its coordinate or its
label (`docs/the-review-record.md` *The handoff*), and each instruction names
who acts, on which file, and what counts as done.

## Orchestrator: how the work is routed

**The routing question is one of the questions `skills/implement/SKILL.md`
*1. Read the documents that outrank the code first* has the orchestrator
ask in one batch before the first edit.** It is one decision about where the
work goes, and asking a part of it later is the mid-run question the batch
exists to remove. Opening a pull request is an outward-facing act, not a detail that
can wait for the end. Routing asked at the start, the reviewer in the middle
and the pull request at the end would be three waits where one is due.

**Ask question 1 alone; the boxes in a second call only under `per axis`.**
The orchestrator puts both. Question 1 goes in one call of its own, and two
of its three answers settle everything: `automation` writes every row, and `no work
item` opens nothing, so under either of them the boxes mean nothing and are
not shown. The harness shows every question of a call at once, so boxes put
beside question 1 would be shown under the two answers they mean nothing for.
Under `per axis` the second call follows the first at once, before the first
edit. `AskUserQuestion` allows at most four options per question, and two
presets beside the four boxes would be six, which is why the shape is two
questions rather than one.

### Question 1

A single-select question, put alone:

| Order | Label | Description |
|---|---|---|
| 1 | **automation** | Every party runs: the framer frames it, `crafter` builds it, `proofer` reviews it, the orchestrator takes the broad run, the sealer audits it, and the pull request opens. **This is the last question: nothing stops to ask again.** |
| 2 | **per axis** | The four boxes below are the answer. |
| 3 | **no work item** | No work item is opened: no frame, no review, no seal, no `routing.md`, and this session writes the change itself. The session runs `seal no-work-item` before its first edit; where the root is shared, every commit ends with the trailer `Seal-Routing: no work item`, and the pull request's check only lists those commits. |

**A label names what it turns off, not where it ends.** A label that names a
destination is read as what runs: `straight to the PR` was read as *call no
agents at all*, where that answer turns off `proofer` alone. So the exit
names no destination, and its description names the five things that do not
happen.

**The exit is last.** It is the least-verified path and one click, so it
sits where a reader's eye lands last, and its description states the cost.
It stays visible in use where the root is shared: every commit it covers
says `no work item` in its trailer, and the pull request's check prints each
one.

**A run resumed in a new session puts question 1 through `AskUserQuestion`
again, before the first spawn.** Where the declaration answers `Automation`
with `yes`, the question goes alone, because `hooks/question-gate.py` refuses
whatever shares its call; elsewhere it may share the call with what else the
resume asks. The boxes are not put again, because `routing.md` already holds
their answer. The orchestrator puts it from a directory inside the clone the
run works in: the readers keep the answer only where the result's own
directory and the gate's root are the same clone
(`docs/the-routing-check.md` *The edit check*). A new session is
a `/clear`, a new `claude` start, or another machine. A typed answer is not
the press: the gates read a harness-written result in the session's own
transcript and nothing else, and `routing.md` is not read
(`docs/the-routing-check.md` *The edit check*). `claude --resume` and
compaction keep the session's id and append to its transcript, so the press
survives both and nothing is put again.

### Question 2

A `multiSelect` question, asked only under `per axis`.

**The order is the specification.** The first box is a property of the run;
the three below name parties, in the order they run. A reader meeting four
boxes of apparently the same kind reads the first as a fourth party to switch
on, and the separation is the cheapest defence against it. A list that
generates these carries the order.

| Order | Box | Checked | Not checked |
|---|---|---|---|
| 1 | **run end to end without stopping to ask** | the run goes from here to its destination with nobody at the keyboard; `Automation` = `yes` | **this run may stop to ask**: somebody may be asked at minute thirty; `Automation` = `no` |
| 2 | **implement with `crafter`** | spawn the subagent; `Implementation` = `crafter` | **this session writes the code**; `Implementation` = `the session` |
| 3 | **review with `proofer`** | the review rounds run; `Review` = `through the review chain` | **nothing reviews this code before the pull request**; `Review` = `straight to the PR` |
| 4 | **open the pull request** | push it and open one; `Destination` = `open the pull request` | **the branch is handed back, committed and unpushed**; `Destination` = `stop before the pull request` |

**What is checked is the answer, and each box is a row of the declaration**,
which is why each box's description carries its unchecked meaning too: that
is the half a label cannot say. Box 1's unchecked half is the one most easily
misread: `no` says this run may stop to ask, never that a person did the work
by hand.

**The ceiling.** `AskUserQuestion` allows at most four options per question.
Question 2 sits at exactly four, and the room was made by taking the framer
and the sealer out of the question. **It is fully spent: a fifth box breaks this
shape**, and whoever adds one needs a third question of boxes or a preset
that hides the axes.

### What the answer writes

Question 1's first two options and question 2's four boxes write the same
rows; what differs is how many clicks it took and which row says so.

| Row | Answers |
|---|---|
| Automation | `yes` or `no`, OPTIONAL; absent reads as never asked |
| Implementation | `crafter` or `the session`, OPTIONAL; absent reads as unanswered |
| Review | `through the review chain` or `straight to the PR` |
| Destination | `open the pull request` or `stop before the pull request` |
| Answer pressed | `automation` or `per axis`, OPTIONAL; absent reads as unanswered |
| Branch | the branch the work item is built on; two declarations naming one branch read as none |

**Each answer is written without backticks**, and the file starts from
`templates/records/sdd-routing.md`, which ships `Review` and `Destination`
answered and the optional rows as placeholders. An absent `Automation` row
means nobody was asked, so `no` is never written where the question was not
put. The grounds of both are `docs/the-review-and-parity-arms.md` *The
declaration, and where the check went*.

**`Implementation` is answered by whether the work is finding out or writing
down.** Finding out is a step to send to `tracer`, and the orchestrator that
reads the facts back and writes the code still answers `the session`;
`crafter` answers where the diff is large enough to threaten what the
orchestrator still has to hold (`docs/the-agent-set.md` *What a spawn
costs*). The file ends with `## Why this way`, one or two sentences nothing
reads.

**`automation` writes all four party rows at their checked values**, plus
`Automation` = `yes`, plus `Answer pressed` = `automation`. Ticking all four
boxes under `per axis` writes the same four rows and `Answer pressed` =
`per axis`.

**The `Answer pressed` row tells a pressed preset from four boxes ticked by
hand**, and question 1's third option never reaches it
(`docs/the-review-and-parity-arms.md` *The declaration, and where the check
went*).

**`Automation` is held by a gate.** While the row reads `yes`,
`hooks/question-gate.py` refuses every question on the declared branch but
question 1 put alone before the person has answered it in this session, and
`docs/the-review-record.md` *The run* is the rule.

**The declaration has one more row, and nobody is asked about it.**

| Axis | Answers |
|---|---|
| Planning | `framer` or `the session`, OPTIONAL; absent reads as unanswered |

It is a record, not a box. The question grows only where a decision is a
person's, and this one is not: `agents/framer.md`'s `## Job` says the SDD
ladder decides, so the framer runs only where `skills/implement/SKILL.md`
*3. The SDD file set* calls for a `frame/design.md`. The orchestrator fills the row
from what happened: `framer` where the subagent drew the frame, `the session`
where the orchestrator drew it, and no row where the ladder called for no
frame. A wrong answer here is contradicted by nothing, which is why
`hooks/implementer-notice.py` says one line after a commit when a declared
agent left no mark, for this row and for `Implementation` together.

**The routing question is the orchestrator's, whether or not a framer runs.**
A subagent in this harness has no `AskUserQuestion` and no equivalent, so a
framer cannot ask. The one moment of human contact is here, before the first
edit, and the order does not change when a framer runs:

```
the orchestrator : ask question 1; the boxes only under per axis
the orchestrator : write and commit routing.md
the framer       : read, judge, write design, plan and questions
the orchestrator : read plan.md against the issue, settle it with the framer, spawn the build
```

`agents/framer.md`'s rule *You ask nobody anything* is the other half of this,
and its `## Job` tells a framer that arrives to a missing `routing.md` to
report it rather than write one: a declaration written from a guess is a
recorded answer nobody gave.

**The orchestrator writes the answer down before the first edit**, in
`seal/threads/<work-item-id>/routing.md`, from `templates/records/sdd-routing.md`, and
commits it, because the check happens at the pull request and CI sees only
what is in the tree. Below the SDD ladder this may be the only file a work
item gets.

**The first edit is held by a gate.** `hooks/routing-edit-gate.py` refuses a
`Write`, `Edit` or `NotebookEdit` of a file in the repository while no
`routing.md` names the branch checked out where the file is. A file under the
`seal/` root is never refused, so the declaration can always be written
first. Under `no work item` the session runs `seal no-work-item` once on the
branch it edits, before its first edit: it records, for this session on that
branch, that the change belongs to no work item, and the gate then lets its
edits on that branch through. A session that moves to another branch runs it
there again.

**The orchestrator writes the file with the `Write` tool, then commits it.**
The declaration is read from the working tree (`hooks/lib/routing.py`'s
`declarations()` opens the path rather than asking git), so the edits after
the write go through before the commit lands. The commit goes as every
commit does: each work item's `routing.md` in a command of its own, the
worktree's path written out after `git -C`, never a loop over a variable
naming it (contract rule 16).

**What each combination of `Review` and `Destination` checks, and where**,
is `docs/the-review-and-parity-arms.md` *The declaration, and where the
check went*. Under `stop before the pull request` nothing runs at the end,
and the orchestrator says so in the handback.

**Where a migration config is declared, the comparison with the original is
recorded where the answer puts it**: in each round record under `through
the review chain`, and in the sealer's `guarantee.md` under `straight to the
PR`. A change confined to `docs/` and `seal/` owes none
(`skills/legacy-parity/SKILL.md` *Recording the comparison*). The shapes
that leave code nobody compared, with nothing that reads it, are listed in
`docs/the-review-and-parity-arms.md` *Parity arm*.

The declaration is what the edit check reads, for **either** review answer,
so a declared work item edits whichever reviewer it named, and CI reads the
same file at the pull request. Work never headed for a reviewer, such as a
release chore or a documentation pass, declares `straight to the PR`. For a
change belonging to no work item, the session runs `seal no-work-item`, and
where the root is shared each commit's trailer reads `no work item`
(`skills/commit-pr-convention/SKILL.md`).

**Which branch the pull request lands on is decided with the routing
question.** A pull request into the release branch is not a release: its
entry accumulates unreleased. Whether it moves the version is the
repository's convention. Where the repository names the version when it
cuts the release branch, as a branch named `release/vX.Y.Z` does, the
orchestrator moves the version to that name in the first pull request into
the branch, in the commit that adds that work item's changelog entry,
and every later pull request into the branch leaves it. Where the
repository moves the version at the release, a pull request into the
release branch leaves it alone. A pull request into `main` is a release:
the accumulated entries go out under the version, which moves there only
where it has not moved already, and the tag follows the merge. The release
branch is the default. The orchestrator takes `main` when the accumulated
entries read as one release, or when the change is a gate or a hook firing
where it should not, which does not wait for other changes.

**Where an entry accumulates is the repository's convention, so the
orchestrator reads it before writing one.** Two shapes are common and they
are not interchangeable: a heading in the changelog that every branch appends
to, or one fragment per work item that a release gathers. Writing the first
into a repository that uses the second invents a heading its checks refuse,
or appends to the shared region the fragments exist to empty. Where the
repository gathers fragments, basing on `main` means running the gather,
because `main` is the branch where the entries are due; the contribution
guide names the command.

**The declaration moves the check and waives nothing**: the direct answer
turns off the reviewer, and the broad run is owed just the same
(`docs/the-review-and-parity-arms.md` *There is no standing waiver*).

**A work item that commits in more than one repository** asks the routing
question once and writes every answer into each gated repository it commits
in, by the procedure `skills/implement/multi-repository.md` holds.

## Orchestrator: where a decision or a lesson is written

**The orchestrator writes each decision and each lesson of a run into the
repository, never into a session's local memory.** The harness keeps that
memory on one machine, outside the repository, so a rule kept there is
unknown to a run on any other machine and to anyone who reads the
repository.

| What the orchestrator has | Where the orchestrator writes it |
|---|---|
| a decision about the work item in progress or a file it changes, with its grounds | the work item's records, as `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* states |
| a lesson about how an act is done | the file the act is read from, through the work item in progress where that work item changes the file: a skill or an agent definition edited in place, or a policy document through the work item's `## Rule changes` (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*) |
| a lesson or a decision whose home no work item in progress changes | an issue that names the home, in the tracker of the repository that holds the home. Where the home is a file the plugin ships and the run is in another repository, the orchestrator names the lesson and the file in its report to the person, who can take it to the tracker the plugin's `.claude-plugin/plugin.json` names under `repository`; it edits no installed copy, which stays on one machine and is replaced at the next update |
| a reading of what a segment cost | the log `skills/verify/orchestration.md` *Measure the segment, and feed the flow log* names for that reading |

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

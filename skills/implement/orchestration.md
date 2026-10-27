# implement, the orchestrator's half

This file is the orchestrator's: the session that starts a work item, asks
the person what only the person can answer, and spawns the agents. It holds
the procedure for **starting** a work item: the order of the parties, creating
the `seal/` root the first time a repository opts in, setting up parity mode
where a project ports an original, and the one routing question, asked before
the first edit.

`skills/implement/SKILL.md` is the other half: the record language, the
document layout, the spec-first procedure, the test-first cadence, the SDD
file set, the closing memo and the review incorporation. The orchestrator
reads both. The smith opens that one at its first step and never this one,
because asking a person and writing `routing.md` are acts `agents/smith.md`
leaves to the orchestrator. Every `seal/…` path here means `<repo>/seal/`
where that directory exists with the marker, and
`$(git rev-parse --git-common-dir)/seal/` otherwise (contract rule 11).

## Orchestrator: the order inside a ticket

1. The orchestrator branches from the release branch and writes `routing.md`
   before the first edit (*Orchestrator: how the work is routed* below).
2. The framer writes `spec.md`, `plan.md` and `questions.md`. The orchestrator
   reads `plan.md`, writes its approval line and spawns the smith (*The plan
   is approved at the spawn* below). The warden's rounds follow, then
   `broad-gate --preflight` and `broad-gate --record`, both run by the
   orchestrator, then the sealer, and then the pull request opens
   (`skills/code-review/orchestration.md` *Orchestrator: the pull request
   opens once the sealer seals* owns when).
3. The pull request body carries `Closes #N`; the release workflow closes the
   ticket when the release reaches `main`.

**A decision made after the frame is committed is folded, in place, into
`spec.md` or `plan.md` before the next smith spawns.** The orchestrator
rewrites the sentence of the frame the decision changes, where it stands,
because a smith reads the frame and not the issue's comments. Until the
decision is folded, the orchestrator keeps one line of its own in `plan.md`
naming the comments to fold, below the approval line where the plan carries
one and below the title where it does not, and deletes that line in the
commit that folds them. Before the frame is committed, the orchestrator
folds the decision into the issue body instead
(`docs/issues-and-milestones.md` *An issue is its body and its comments
together*).

**Where a work item stands is read from `plan.md`'s Status column,
`overview.md` and the phase records.** The orchestrator that hands the work
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

### The plan is approved at the spawn

**The orchestrator approves `plan.md` by writing one line under its title
when it spawns the smith; reading the plan and spawning the build is the
approval.** The line has one shape:

```
Approved <date> by <who>, when `smith` was spawned.
```

`<who>` is the person, or the orchestrator acting under the person's routing
answer. The clause after `when` may name what the smith was spawned for, as
in ``when `smith` was spawned for phases 1 to 3.``, and the line ends at its
full stop. A reason, a scope note or a second approval goes on a line of its
own below it, never after the full stop. Where `routing.md` answers
`Implementation` with `the session`, nothing is spawned, and the line names
the first edit as its moment: `Approved <date> by <who>, before the first
edit.` Nothing in the tree reads the line; a sentence appended to it once made
the reader that did see no approval at all.
check: none reader: the warden at review

**The spawn prompt is text an agent reads.** The orchestrator writes it to
the rules of `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한
가지로만 읽히게 쓴다*: each fact it hands over carries its coordinate or its
label (`docs/the-review-record.md` *The handoff*), and each instruction names
who acts, on which file, and what counts as done.

## Orchestrator: Bootstrap

When a root or file this skill needs does not exist, the orchestrator creates
it from `templates/` in this plugin and continues. In particular:

- `seal/README.md`, which says what the root holds and names the section of
  `skills/implement/SKILL.md` that states the export rules. Its first line
  is the marker the gates read, so the file is copied from
  `templates/seal-README.md` as it stands.
- **Not** policy documents. A repository that has none has none; judge from
  the SDD set and the code. Creating `docs/policies/<domain>/` imposes one
  project's documentation habit, and one field's vocabulary, on every
  repository this plugin touches.

**When no `seal/` whose `README.md` opens with the marker exists at either
place, the orchestrator asks once, in the one call step 1 states, before
creating anything, then does two more things before continuing.**
Creating the root is what opts the repository in: from the next command on,
every gate here is awake. Where the root lands, committed with the repository
or under the git directory on this machine only, is the person's decision and
not the orchestrator's. Nobody reads a README to discover a question they did
not know to ask, so this is the only place the mode and the migration
question are asked at all.

A repository still on the 0.3.x layout is moved by hand, with the commands
README.md *Coming up from 0.3.x* gives, because no code of the plugin opens
that layout. The orchestrator names that section in one line and continues
with the question below. A top-level `specs/` is the project's own, a team's
specifications or another tool's records, whatever its entries are named, and
stays where it is: the plugin writes only to its own root.

**A `<repo>/seal/` whose `README.md` does not open with the marker is the
project's own.** The marker is the first line of `templates/seal-README.md`,
and a package or a tool can keep a directory named `seal` for itself. The
orchestrator writes nothing into it and offers neither shared option, because
`<repo>/seal/` is the shared root's one place. The root goes under the git
directory, at `$(git rev-parse --git-common-dir)/seal/`, as the local option
below creates it, and the orchestrator says so in one line: *"`<repo>/seal/` is this
project's own, so the plugin keeps its root under the git directory, in local
mode"*. The one call of step 1 then carries the `Broad gate` question alone.

1. The orchestrator asks once, with one `AskUserQuestion` carrying **two
   questions**: the mode, and the `Broad gate` row. The mode's three options
   come first, in this order:

   - **shared, records only** (the default, listed first) creates
     `<repo>/seal/` in the tree; the routing commit made before the first
     edit carries it. It writes nothing under `.github/`, so nothing it
     installs can stop a teammate's pull request.
   - **shared, with pull-request checks** does the same, and then the
     orchestrator installs the checks with `seal pr-checks install`, run
     after `seal mode` below. That command writes
     `.github/workflows/hygiene.yml` from `templates/hygiene.yml` only when
     that path is absent, pinned to the release of the installed plugin, and
     stages it, so the routing commit carries it too. An existing file is
     never overwritten, and the orchestrator relays the line the command
     prints when it leaves one alone.
   - **local** creates `$(git rev-parse --git-common-dir)/seal/`, installs
     nothing, and touches nothing in the tree. The path is spelled through
     the common git directory rather than through `.git`, which is a file in
     a linked worktree; the root lands beside the smith mark, shared by every
     worktree of the clone, never a commit candidate, with no `.gitignore`
     line. The orchestrator says what it gives up: the pull-request checks
     read committed files, so CI cannot run them, and a new machine or a
     re-clone starts empty.

   Whichever the answer, the mode is the place: the hooks read
   `<repo>/seal/` and then the common git directory, and a repository with
   both is shared.

   **The answer is not a door that shuts.** `seal mode` reports where the
   root is, and `seal mode local` or `seal mode shared` moves it, writing the
   mode into `seal/config.md` on the way and leaving `.github/` alone.
   `seal pr-checks` reports whether the checks are installed, and
   `seal pr-checks install` and `seal pr-checks remove` put them in and take
   them out. The orchestrator says so in one line when it creates the root,
   because the question is asked once and the person answering it does not
   yet know what they will want.

   **The second question is the `Broad gate` row, and it is a proposal
   rather than a blank.** That row is the one value in this flow only a
   person can write (`templates/config.md` *Broad gate* says why it has no
   default). Unasked, it reaches the person as the gate's refusal after the
   review rounds have settled. A repository being opted in may not yet know
   its broad command, so **what the machine can derive is offered, the
   person picks, and nothing is guessed.**

   Read candidates off the repository, in this order, and offer each with
   the file it came from:

   | Where to look | What to take |
   |---|---|
   | `.github/workflows/*.yml` | the `run:` steps of whatever job gates a pull request. What CI already refuses a merge for is the repository's own answer, written down before anybody asked |
   | a runner under `bin/` | `bin/test`, `bin/check`, or whatever the contribution guide names first |
   | a package manifest | `package.json`'s `scripts.test`, a `pyproject.toml` tool section, `Cargo.toml` |
   | a `Makefile` | a `test`, `check` or `lint` target |

   Offer each candidate as **one shell command line** composed the way
   `templates/config.md` *The criterion for choosing a value* says to compose
   one, and name the file it came from: a candidate whose source is named is
   one the person can correct. Where nothing is findable, say so rather than
   inventing one: a guessed row is what `templates/config.md` *Broad gate*
   argues against by name.

   **A candidate carrying a `|` is written with the pipe escaped, `\|`**, and
   a CI `run:` step is where one is likeliest to come from. Offer it that way
   rather than dropping the pipe or moving to the next candidate: the cell is
   markdown's, and the reader reduces `\|` to a plain pipe before any shell
   sees it. Say why, because a bare one is refused: GitHub shows the row cut
   off at the pipe, the gate quotes that line back with the edit instead of
   reporting the row as absent, and every row written below it goes unread
   with it. `templates/config.md` *What is refused, and what stays allowed*
   carries the rule.

   **Name the criterion; do not restate it.** `templates/config.md`
   *The criterion for choosing a value* owns the criterion, three rules with
   the reason for each, and the person answering reads it there.

   **Offer a decline, and say what it costs.** *Not yet* is a real answer:
   one written to get past a question is worse than none. The cost is one
   sentence: the first `broad-gate` run refuses with nothing run, and that
   refusal lands after the review rounds have settled. `/specseal:config`
   fills the row in at any point before then.

   **Then record the answer: run `seal mode`, with no argument.** It writes
   the `Mode` row from where the folder is and moves nothing. The row is the
   only trace that anybody was asked: left unwritten, a root somebody chose
   and a root that appeared because a session followed the routing rule are
   the same bytes.
   `hooks/mode-gate.py` reads the absence and stops the next command to ask
   this same question, so running the command here keeps the person who just
   answered from being asked twice. Under **shared, with pull-request
   checks**, the orchestrator then runs `seal pr-checks install` and relays
   the line it prints; an exit 1 is that line's refusal, and the setup goes
   on without the checks.

   **Then the `Broad gate` row, where a command was chosen.** `seal mode` has
   just written a config file carrying `Mode` and nothing else, so the
   orchestrator adds the row the way `/specseal:config` step 3 adds one: the
   row **and the prose under `## Broad gate` down to but not including
   `### What is refused, and what stays allowed`**, taken from
   `$CLAUDE_PLUGIN_ROOT/templates/config.md`. The two lists and the criterion
   are pointed at rather than copied down, because a frozen copy in
   somebody's `seal/config.md` says something false at the plugin's next
   release. No command does this and none is being added:
   `skills/implement/scripts/seal.py`'s writer is the `Mode` row's, and
   `skills/config/SKILL.md` *What this does not do* refuses a generic setter
   for a file people edit by hand.

   **A decline writes nothing at all.** No row, no sentinel, no note. A
   repository that declined and one that was never asked meet the same
   refusal at the same moment and are told the same correct thing, so a trace
   would separate two states nothing treats differently. The mode row is the
   opposite: its absence makes a root somebody chose and a root nobody chose
   the same bytes.
2. The orchestrator says in three lines what it created, that its presence
   at that place with the marker as its README's first line is the opt-in,
   and what each part of the root is for. The
   layout is invisible otherwise: it appears in a diff the user did not
   request, or, in local mode, in no diff at all.
3. The orchestrator asks once:
   *"Does this project port behavior from an existing codebase? If so, tell
   me which one and I will set up parity mode."*
   - **Yes**: the orchestrator runs the parity setup below, then continues
     the work.
   - **No**: the orchestrator continues and never raises it again. Bootstrap
     does not re-run, so the question does not either.

Nothing else is asked. **`/specseal:config` is how any of it is changed
later**: it shows every row with its value and routes a change to whatever
owns that row. The orchestrator says so once, here, because a person who
answers a question in a batch has no reason to expect a way back to it.

Ask only here. A repository that has a `seal/` carrying the marker at either
place, `<repo>/seal/` or `$(git rev-parse --git-common-dir)/seal/`, has been
through this: the mode is read from where the folder is, and asking again is the
nagging this plugin exists to avoid.

## Orchestrator: Parity setup

Three of the four fields come from the machine; only one needs the user.
The orchestrator never guesses the original: a comparison against a guessed
repository proves nothing.

1. **Candidates for the original.** Sibling directories that are git
   repositories (a port usually sits beside its original), an upstream or
   fork relation in `git remote -v`, and repositories whose paths overlap
   this one's. The orchestrator presents what it found and lets the user pick
   or give a path.
2. **Baseline commit**: `HEAD` of the confirmed original checkout.
3. **Policy root**: the ratified-policy directory the tree already has, or
   `none`; never a proposed one.
4. **Coordinate-trust exceptions**: empty. Rows arrive from real work.

The orchestrator writes `seal/parity.md` from `templates/parity.md` with
those values, and records the machine-local checkout path in
`~/.claude/specseal/parity-paths.md`, keyed by the origin remote URL. The path
never goes in the committed file.

## Orchestrator: how the work is routed

**The routing question is one of the questions `skills/implement/SKILL.md`
*1. Read the spec before the code* has the orchestrator ask in one batch
before the first edit.** It is one decision about where the work goes, and
asking a part of it later is the mid-run question the batch exists to
remove. Opening a pull request is an outward-facing act, not a detail that
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
| 1 | **automation** | Every party runs: the framer frames it, `smith` builds it, `warden` reviews it, the orchestrator takes the broad run, the sealer audits it, and the pull request opens. **This is the last question: nothing stops to ask again.** |
| 2 | **per axis** | The four boxes below are the answer. |
| 3 | **no work item** | No work item is opened: no frame, no review, no seal, no `routing.md`, and this session writes the change itself. The session runs `seal no-work-item` before its first edit; where the root is shared, every commit ends with the trailer `SpecSeal-Routing: no work item`, and the pull request's check only lists those commits. |

**A label names what it turns off, not where it ends.** A label that names a
destination is read as what runs: `straight to the PR` was read as *call no
agents at all*, where that answer turns off `warden` alone. So the exit
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
(`docs/worktree-guard-spec.md` *Creation consent*, rule 4). A new session is
a `/clear`, a new `claude` start, or another machine. A typed answer is not
the press: the gates read a harness-written result in the session's own
transcript and nothing else, and `routing.md` is not read
(`docs/worktree-guard-spec.md` *Known limits*). `claude --resume` and
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
| 2 | **implement with `smith`** | spawn the subagent; `Implementation` = `smith` | **this session writes the code**; `Implementation` = `the session` |
| 3 | **review with `warden`** | the review rounds run; `Review` = `through the review chain` | **nothing reviews this code before the pull request**; `Review` = `straight to the PR` |
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
| Implementation | `smith` or `the session`, OPTIONAL; absent reads as unanswered |
| Review | `through the review chain` or `straight to the PR` |
| Destination | `open the pull request` or `stop before the pull request` |
| Answer pressed | `automation` or `per axis`, OPTIONAL; absent reads as unanswered |
| Branch | the branch the work item is built on; two declarations naming one branch read as none |

**Each answer is written without backticks**, since a backticked value reads
as unanswered. `templates/sdd-routing.md` ships `Review` and `Destination`
answered and the optional rows as placeholders: a wrong answer in the first
two is caught at the next commit, because the gate stops recognising the
file, and a wrong answer in the others is contradicted by nothing, so a file
copied and never revisited lands on not answered rather than on a confident
answer nobody gave. An absent `Automation` row means nobody was asked, which
is why `no` is never written where the question was not put.

**`Implementation` is answered by a criterion, not by habit: is the work
FINDING OUT or WRITING DOWN?** Finding out, what an unfamiliar codebase does
or what an original did, is a STEP to send to `scribe`: a large input and a
small output is what a subagent boundary is for. That is a step and not an
answer to this row; the orchestrator that reads the facts back and writes
the code still answers `the session`, so the row is never deleted because
the work is discovery. Writing down stays with the orchestrator too, because
a delegate re-buys the context the orchestrator holds, and `smith` answers
where the diff is large enough to threaten what the orchestrator still has
to hold. That threshold is a number nobody has; the axis it sits on is
REPLACEABILITY, not cost, because the orchestrator is the one participant a
release cannot replace mid-run. The row is deleted only for a work item that
has no answer to give. The file ends with `## Why this way`, one or two
sentences nothing reads: what a reviewer and the next session see instead of
guessing from the absence of a token.

**`automation` writes all four party rows at their checked values**, plus
`Automation` = `yes`, plus `Answer pressed` = `automation`. Ticking all four
boxes under `per axis` writes the same four rows and `Answer pressed` =
`per axis`.

**The `Answer pressed` row is why the preset buys anything.** Without it a
pressed preset and four boxes somebody ticked by hand are the same bytes, so
a chosen answer cannot be told from a question nobody read. Question 1's
third option never reaches the row: it opens no work item, so there is no
file to write it in.

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
*3. The SDD file set* calls for a `spec.md`. The orchestrator fills the row
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
the framer       : read, judge, write spec, plan and questions
the orchestrator : read plan.md, write the approval line, spawn the build
```

`agents/framer.md`'s rule *You ask nobody anything* is the other half of this,
and its `## Job` tells a framer that arrives to a missing `routing.md` to
report it rather than write one: a declaration written from a guess is a
recorded answer nobody gave.

**The orchestrator writes the answer down before the first edit**, in
`seal/specs/<work-item-id>/routing.md`, from `templates/sdd-routing.md`, and
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
The declaration is read from the working tree (`hooks/routing.py`'s
`declarations()` opens the path rather than asking git), so the edits after
the write go through before the commit lands. The commit goes as every
commit does: each work item's `routing.md` in a command of its own, the
worktree's path written out after `git -C`, never a loop over a variable
naming it (contract rule 16).

What the four combinations do:

| Review | Destination | During the work | At the end | What CI checks |
|---|---|---|---|---|
| chain | open the PR | edits go through | the PR opens | a round record is required, and the broad run's `broad-gate.md` beside it |
| chain | stop before the PR | edits go through | the branch is handed back, committed and unpushed | **nothing runs**; the orchestrator says so in the handback |
| direct | open the PR | edits go through | the orchestrator takes the broad run, the sealer audits it, then the PR opens | the broad run's `broad-gate.md` in the work item's directory, at a SHA, against the base, and no round record; the answer turns off the reviewer alone |
| direct | stop before the PR | edits go through | the branch is handed back | **nothing runs**; the orchestrator says so in the handback, and the broad run's record is owed when a pull request opens |

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
entry accumulates unreleased, and the version is left alone. A pull request
into `main` is a release: the version moves, the accumulated entries are
gathered and dated, and the tag follows the merge. The release branch is the
default. The orchestrator takes `main` when the accumulated entries read as
one release, or when the change is a gate or a hook firing where it should
not, which does not wait for other changes.

**Where an entry accumulates is the repository's convention, so the
orchestrator reads it before writing one.** Two shapes are common and they
are not interchangeable: a heading in the changelog that every branch appends
to, or one fragment per work item that a release gathers. Writing the first
into a repository that uses the second invents a heading its checks refuse,
or appends to the shared region the fragments exist to empty. Where the
repository gathers fragments, basing on `main` means running the gather,
because `main` is the branch where the entries are due; the contribution
guide names the command.

What must not happen instead is a standing waiver nobody sees: a switch
that turns the check off and leaves no trace. The routing declaration is not
that switch. It moves the check rather than removing it: the chain answer is
checked at the pull request against the round record, the direct answer
against the broad run's `broad-gate.md` at the same place, and no third
value means no enforcement anywhere. Nor is `seal no-work-item`: where the
root is shared, every commit it covers says `no work item` in its trailer,
which the pull request's check prints. What the direct answer
turns off is the reviewer, and the broad run is owed just the same. Deciding
at the start moves the question to the minute where answering it costs a
reply rather than a stopped run.

### A work item that commits in more than one repository

The routing question is still asked once, in the shape above, and every
answer it writes goes into every repository the work item commits in. Asking
it again per repository is the mid-run question this section exists to
remove, arriving once per checkout.

**Only a gated repository gets a declaration.** A gated repository is one
with a `seal/` root at either place (contract rule 11). Write
`seal/specs/<work-item-id>/routing.md` into each one before that
repository's first edit, each naming that repository's own branch, each in a
command of its own, and commit each with that repository's absolute path
written out after `git -C` (contract rule 16). A repository with no root is not
opted in by this step: writing the file would create its root, and creating
a root is the bootstrap's decision and the person's. Name such a repository
in the handback and write nothing into it.

**One id, minted once, names the directory in every repository.** Take
`date +%s` once, pick one slug, and use the resulting directory name in every
repository. The id is what every share is keyed by:
its changelog fragment and the `<!-- specs/<work-item-id> -->` marker the
changelog gather writes. A directory named differently in each repository
would have to be renamed later, and the rename moves both. Nothing checks
this, because nothing can tell an id minted twice from a signer's own work
item that cites the pact without changing it, and that second case is
legitimate and common.

**Where the repositories keep a contract together, they sign a pact.**
`docs/the-pact.md` holds the model. Two conditions decide it, and both must
hold: the work item commits in more than one repository, and those
repositories share contract. A sentence is contract when another
repository's code would be wrong if it changed. Where both hold:

- the one copy of the contract is `seal/pact.md` in one of the repositories,
  begun from `templates/pact.md` and written by the build there, framed by
  that repository's own spec. That repository is the pact's repository;
- every other repository of the work item is a signer, and the orchestrator
  writes one row into its `seal/config.md` where it is absent: `Pact`, the
  origin remote URL of the pact's repository. `templates/config.md` *Pact*
  documents it. The pact's repository needs no row, because it is identified
  by holding `seal/pact.md`;
- each signer cites the clauses it was built against as pact anchors, in its
  spec's Grounding, and `pact-check`, run at the pact's repository, reads
  every signer and says where they disagree.

Where only the first condition holds, the repositories get their
declarations and nothing else: no pact, and no `Pact` row.

## Orchestrator: which of these acts runs itself

Every act addressed to the orchestrator sits under a heading carrying the
`Orchestrator:` prefix, in this file or in
`skills/code-review/orchestration.md`, and this is the list of them.
`tests/test_every_orchestrator_act_names_its_delivery.py` holds it against
both files from both sides: an act with no row fails, and a row naming an act
no file carries fails.

**The row set is mechanical.** Every `##` heading whose text begins
`Orchestrator:` in either file, plus every `###` heading directly beneath
one. This section is one of those headings, so it has a row of its own.

**`Delivered by` answers one question: when the orchestrator forgets this
act, what notices?** Four values and nothing else.

| Value | What it says |
|---|---|
| `command: <path>` | the act is one command somebody types, so there is nothing to reconstruct from prose. The path has to exist |
| `check: <path>` | something refuses, or says so, when the act did not happen. The path has to exist |
| `part of its parent's act` | a `###` describing its parent's act rather than naming one of its own. A `##` cannot take it |
| `still a sentence` | nothing notices. The `Grounds` cell says what was looked at and came back empty, and an empty cell there fails |

**A command does not make anybody run it, and a row naming one says so where
that is the case.** The grounds of a row whose delivery reaches only part of
its act name the part it does not reach. A row that reads closed over a tree
that is not is worse than no row at all, because the next work item picks
its subject from this table.

**What this does not catch**: an act written for the orchestrator under a
heading carrying no marker has no row and nothing notices. The check reads
the marker, not the meaning, which is the limit
`tests/test_a_section_marked_for_one_role_reaches_only_that_role.py` states
for itself. The two read the headings through one parser, so they cannot
come to different answers about what a heading is.

**One act is outside this table, because the table cannot hold it.** Posting
a segment's reading to the flow log is the orchestrator's (contract rule 6
withholds posting from every agent), and it lives in
`skills/verify/orchestration.md` *Measure the segment, and feed the flow
log*, under a heading carrying no
marker, in a file the row rule above does not read. Its delivery is
`session-cost … --post`, which resolves the label, applies the invariant and
posts the reading with what a person says about it. **Nothing makes it
run**: the measurement can go untaken while the posting never fails. So this
paragraph is the row that act would have, and it is not a closed-looking
one.

| Act | File | Delivered by | Grounds |
|---|---|---|---|
| Orchestrator: the order inside a ticket | `skills/implement/orchestration.md` | still a sentence | Nothing reads the order. Each step it sequences has a row of its own, and what the sequence itself asserts, which party runs when, is in no file a check opens. A run that opened the pull request after the rounds leaves the same tree as one that opened it before them. Nothing reads the three rules under the steps either: a decision left in an issue comment, a `handoff.md` kept after its move and a recurring problem given no home leave a tree no check refuses |
| The plan is approved at the spawn | `skills/implement/orchestration.md` | part of its parent's act | The approval line of the step where its parent's order spawns the smith, and the rules the spawn prompt is written to. It names no act of its own |
| Orchestrator: Bootstrap | `skills/implement/orchestration.md` | check: `hooks/mode-gate.py` | A root with no `Mode` row in `config.md` is exactly nobody was asked, and this gate stops the next command until `seal mode` writes it. It reaches the mode question alone. Nothing reads the `Broad gate` proposal, so a repository that was never offered candidates meets `bin/broad-gate`'s own refusal after the rounds have settled. The workflow file is written by `seal pr-checks install`, whose substitution of the version `tests/test_seal.py` holds, and nothing checks that the orchestrator ran it under the second answer |
| Orchestrator: Parity setup | `skills/implement/orchestration.md` | still a sentence | The four fields are derived by hand and nothing reads the result. The pull request's parity arm wakes on `seal/parity.md` existing, so a setup that never happened is silence rather than a refusal, and a guessed original produces a file that parses |
| Orchestrator: how the work is routed | `skills/implement/orchestration.md` | check: `hooks/routing-edit-gate.py` | The first `Write`, `Edit` or `NotebookEdit` is refused until a declaration naming the branch stands under the `seal/` root or the session ran `seal no-work-item` on that branch, and `templates/claude-md-block.md` carries the question's shape into every session on the machine. What neither reaches is the shape of the asking: a declaration built from four separate questions parses exactly like one built from the asking this section mandates |
| Question 1 | `skills/implement/orchestration.md` | part of its parent's act | The three options of the first `AskUserQuestion` call its parent describes, put alone. It names no act of its own |
| Question 2 | `skills/implement/orchestration.md` | part of its parent's act | The four boxes of the second call, put only after a `per axis` answer, and the ceiling on how many there may be. It names no act of its own |
| What the answer writes | `skills/implement/orchestration.md` | check: `skills/code-review/scripts/chain_check.py` | It refuses a `Review` or `Destination` value outside the vocabulary at the pull request, and `hooks/routing.py` parses the same rows at every edit. The three optional rows are read by nothing that refuses: `hooks/implementer-notice.py` says one line after a commit where a declared agent left no mark, and blocks nothing |
| A work item that commits in more than one repository | `skills/implement/orchestration.md` | check: `hooks/routing-edit-gate.py` | In each opted-in repository the first edit is refused until a declaration naming that repository's branch stands there, so a repository the step skipped is noticed at its first edit. What it does not reach: an id minted twice is legitimate in a signer's own work item and nothing tells the two apart, and a missing `Pact` row is noticed only when somebody runs `bin/pact-check` at the pact's repository, which refuses a relationship recorded on one side |
| Orchestrator: which of these acts runs itself | `skills/implement/orchestration.md` | check: `tests/test_every_orchestrator_act_names_its_delivery.py` | The test reads this table against the headings of both files, in both directions. What it reads is the marker rather than the meaning, so a heading with no prefix puts its act in neither the table nor the test |
| Orchestrator: a phase is a fresh smith, and a fix pass resumes the implementer | `skills/code-review/orchestration.md` | still a sentence | A phase built by a resumed smith and one built by a fresh smith leave identical trees, and so do a resumed fix pass and a fresh one, so nothing at the pull request can tell them apart, and the choice of session is in no file. `session-cost --segments` prints the context the threshold is read against and gates nothing, so the reading can go untaken while the spawn succeeds |
| Orchestrator: the run ends with a verifying round | `skills/code-review/orchestration.md` | check: `skills/code-review/scripts/chain_check.py` | It fails a ready pull request when a commit touching a file outside the work item's records follows the commit on the last record's `target:` line, or a finding of that record reads `fixed <commit>` or `rejected`, which is the run whose own last fixes nobody opened; on a draft it prints and names the verifying round. What it cannot read is the cap: the extension lines are the warden's, and the sealer reads the count |
| A regression is routed by comparing the fix with the frame | `skills/code-review/orchestration.md` | still a sentence | The warden's `regression:` line routes nothing mechanical, and neither does the sentence of its grounds the route reads: `skills/code-review/scripts/chain_check.py` reads the line only as a reference to an earlier finding, and the `Reframed` line only for its author against the declaration, and the sealer reads the records |
| Orchestrator: the pull request opens once the sealer seals | `skills/code-review/orchestration.md` | still a sentence | A pull request opened before the sealer leaves the same tree as one opened after it, so nothing reads the timing, nothing records that a platform-specific change ran `gh workflow run tests` before the broad run, nothing records that `mergeable` was read before CI was waited on, and nothing gives a merge that resolved a conflict outside the records its verifying round, because the chain check reads no merge commit. What is delivered is the step the section ends on: `skills/code-review/scripts/chain_check.py` fails a ready pull request whose `broad-gate.md` is absent or names a commit other than HEAD, which is what makes the orchestrator's broad run and the sealer's spawn after it happen. The step before that run, `broad-gate --preflight`, is recorded nowhere either, and a session that skips it loses time and nothing else: the broad run asks the same arms and refuses the same way |
| Orchestrator: verify before posting | `skills/code-review/orchestration.md` | still a sentence | The four checks are readings the orchestrator takes before posting, and nothing in the tree records that any of them happened. The one part a record carries is the new HEAD on the next round's `target:` line where HEAD moved |
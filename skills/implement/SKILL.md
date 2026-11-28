---
name: implement
description: |
  Spec-driven implementation methodology: document layout (docs/ + iadd/), policy-first
  judgment, the test-first cadence, and review incorporation.
  Use when: implementing a feature, starting a ticket — including deciding how to
  start one, incorporating review feedback, or when a repo needs its document
  layout bootstrapped.
  NOT for: reviewing someone else's code (use `code-review`), or explaining how
  something already works. The line is whether the question names a work item to
  be built: "how should I approach TICKET-4" is this skill, "how does the review
  chain work" is not.
---

# implement — spec-driven implementation

Methodology for implementing against a written design, leaving a case behind
each rule, and closing the loop with review. Opened by the `crafter` agent at
its first step; usable directly.

**If you are orchestrating a work item rather than building it, read
`skills/implement/orchestration.md` before the first edit**; the crafter
never opens it, and everything below is the crafter's and the
orchestrator's alike.

## The language the records are written in

**Read `Record language` in `config.json` before writing any of the documents
below**, the same way `commit-pr-convention` reads its own key before a commit
or a pull request. The root is resolved the way every path in this skill is.

```json
{
  "Record language": "Korean"
}
```

It governs the **prose** of the records `templates/setup/config.md` *Record
language* lists. What an absent key is and does is
`templates/setup/config.md` *An absent language key is a refusal at the pull
request body, and never at a commit*.

**It is independent of `Commit and pull request language`.** Setting one does
not carry the other; `docs/layout/one-root-by-lifetime.md` *What the repository
decides for itself, and how it is read* gives the reasons.

**What stays English whatever it says**, because these are read literally
rather than by a person: every field name, section heading and vocabulary
word the checkers match, listed in `templates/setup/config.md` under *What no key
governs* — that list is derived from the checkers' own constants, so it
cannot drift from them; the `<!-- -->` markers; the `closed` that opens a
closed row; and all code — identifiers, comments,
docstrings, file names, test function names. A translated field name is
not a translation, it is a checker that stops reading.

## Document layout — two roots, three lifetimes

Every artifact this skill produces goes to one of two roots, and the second is
laid out by **lifetime**, not by who wrote it:

| Root | Lifetime | Test | Authority |
|---|---|---|---|
| `docs/` | Permanent, cumulative | Must still be true in 6 months | **Norms, ratified by humans.** Read when the repository has them; the documentation convention is the project's. The policy root (`docs/` unless `iadd/config.json`'s `Policy root` names another) is the baseline. A work item whose subject is the policy root itself, its structure or its documents' text, edits the policy root directly in its pull request, as the settle does, and re-points in that pull request every unsettled design's `## Rule changes` operation that names a document or a section it moved. A work item whose subject is the code states the rules its work changes in `## Rule changes`, for the settle, so that work items running side by side do not each rewrite the same section. Which subject a work item has is the framer's judgment, read by the proofer at review. The settle after the release writes each section as the latest decision the released designs state, checked against the code (`skills/settle/SKILL.md`), and the policy in force is the baseline plus the latest decision the unsettled designs' rule changes state at each section, in merge order |
| `iadd/threads/<work-item-id>/` | One work item | Its role ends when this work ships (the frame, the trail, the closing memo) | The contract this work executes against. A human approves `frame/plan.md`, which is why this is a repository document and not tool state |
| `iadd/`, everything above `threads/` | Permanent | Everything this plugin maintains | Written and read by machines |

A `specs/` the project kept before the plugin is neither root: it is a
**reference root**, as `templates/setup/config.md` *Reference specs* says — history
read where the work touches what it describes, cited in `frame/design.md` where it was
read, and never written by anything this skill produces.

Inside the policy root, documents are grouped by who opens them and at which
step, and any party may open any group.

`iadd/` stands at the places the opening paragraph of `skills/core/SKILL.md`
names, and its presence at one of them, with a `README.md` that opens with
the marker `lib/optin.py#MARKER` holds, is what tells the gates this
repository runs the workflow. **Every `iadd/…` path in this plugin's skills
and agents means the first of those places that holds the marker**, and
`iadd/` there is the records root's name, as the same paragraph defines it.
The two places in the tree are shared mode: committed, because gitignored
files do not follow worktrees or other machines. The place under the common
git directory is local mode: every linked worktree of the clone shares it,
and it is never a commit candidate. The order decides a repository with a
root at more than one place, and nothing else, no config key, is read. What
sits directly under it is permanent; what sits under
`iadd/threads/` lives as long as its work item. Each file the root holds,
and the question it answers, is in `docs/layout/the-record-layout.md`
*iadd/*, and each file of a work item's directory is in
`docs/layout/the-record-layout.md` *iadd/threads/<work-item-id>/*.

The review round records live beside the work item they are about, with the
routing declaration and the rest of the SDD set
(`docs/forms/the-round-record.md`).
A work item's directory exists from its first commit, because routing is
written into it before the first edit.

**Nothing else follows them, because there is nothing else.** A round record
carries the SHA it reviewed, so it never asserts a present state and can live
beside the contract. Progress does the same thing one file up, in `plan.md`'s
Status column, where a closed phase carries the commit that closed it — the
same past-state trick, for the same reason. The frame's account of the tree
before the build does it too: the framer names the commit it read once, at
the head of `frame/design.md` *Grounding* and `frame/plan.md` *Technical
context*, so each coordinate and present-tense statement of the tree there
is a claim about that commit, which the build was bound to move and HEAD
does not contradict. A sentence there that says what the work does or
concludes is no claim about that commit: a fold rewrites it with a
decision's fact, and otherwise folds it as the paragraph opening **The
framer writes a decision's fold** of `skills/implement/orchestration.md`
*Orchestrator: the order inside a ticket* states, and a reader holds it
against HEAD.

**Judgment precedence is policy > SDD > code where policy exists, and
SDD > code where it does not.** Most repositories are the second kind. Do not
manufacture the first by writing policy documents nobody asked for: the SDD set
is the root of judgment, and a policy document is a thing a human decides to
keep.

## Procedure

**The builder is the party that builds a phase or makes a fix pass: the
crafter or the orchestrator.** The orchestrator builds every phase and makes
every fix pass where `routing.md` answers `Implementation` with
`the session`, and in every route it makes the fix it writes after the last
round (`skills/code-review/orchestration.md` *Orchestrator: a phase is a
fresh crafter, and a fix pass resumes the implementer*). Each rule of this
file that names the builder binds both. So does each rule of
`skills/agent-contract/SKILL.md`, and a rule there that withholds an act
from every agent, such as the broad gate of contract rule 2 or the acts
contract rule 6 withholds, withholds it from the crafter and leaves the
orchestrator the acts its own procedure gives it. Where a rule has the
crafter name something in its hand-back for the orchestrator, the
orchestrator that builds acts on it at the point its build meets it, by the
step of its own procedure that acts on that hand-back.

### 1. Read the documents that outrank the code first

Judgment precedence: **policy (`docs/`) > SDD (`iadd/threads/`) > the ticket >
existing code** — and, where the repository declares a migration config, the
original sits between the ticket and the existing code, because policy being
silent is what makes the original decide (see `legacy-parity`).

A work item's design that contradicts policy gets fixed, not followed. **A ticket is a
request, not an authority**: it says what someone wants, which is why it ranks
above the code as it happens to be, and why it ranks below the documents that
were ratified. A ticket asking for something policy forbids is a question for a
person, not an instruction — write it into `questions.md` rather than building
it or dropping it.

- Policy documents delegate to each other. "This document doesn't answer it"
  is not a policy gap until sibling documents in the same domain are checked.
- Read `iadd/follow-up.md` before starting. It holds items
  whose answer exists but which waited on prerequisite work — **this work may
  be that prerequisite.** If so, include the item in this change and delete its
  row; what remains in that file is the definition of remaining scope.
- Verify clause numbers a ticket cites. Tickets are written before (or drift
  from) the documents they cite; a missing clause gets a freshly allocated
  number, as an `add` in the design's `## Rule changes`, or written in place
  where the work item's subject is the policy root (*Document layout — two
  roots, three lifetimes* above).
- A spawn prompt's facts arrive under `docs/running/the-run.md`'s
  handoff: coordinates rather than prose, each fact labelled
  executed, read, or unverified. What a fact with neither is, and why an
  aggregate is not a coordinate, is contract rule 5.

**The frame is judged before it is built to.** A `frame/design.md` and a
`frame/plan.md` another party drew are a drawing, and a drawing can be wrong
about the tree: a path its row states, a list it hands the builder, a file
it says exists. The builder checks them after the requirements read, before
anything is spent. A *no* goes to `trail/phases/phase-N.md`'s
`## What this phase found`, and the crafter also names it in its hand-back
and never sends it back to the framer. The builder builds to the part that
holds.

### 2. Implement test-first, and let each rule name its test

**Each scenario that adds behaviour is built the same way: its case first,
seen red against the tree as it stands, then the code, then the case
green.** A case asserting that something is not named, counted, read or
let through that is already green against the tree as it stands takes its
red from contract rule 15. A rename or a move adds no behaviour, and is
proved as `skills/verify/SKILL.md` *The narrow command still has to be
able to fail* says: by the cases it already has, with no case written
new. A rule the work
states or changes ends with a `check:` line naming that case — in its home
under `docs/`, or in the *Verifiable how* cell of the design's scenario table —
so the case is the record that the rule holds, and CI running the suite is
the check. A rule no case can hold carries no check line, and review reads
it. The grammar is `skills/settle/rule-changes.md` *A rule has one shape*.

**A new test starts from its group.** Before writing a case, the builder
reads the tests of the function it covers and any pair a duplicate check in
the repository names, and adds the case to that group; a case that covers
nothing its group does not already cover is not added. In a repository
whose test files declare `TARGET`, `iadd layout --pairs` is that check.

**The build holds to the request.** It adds no speculative feature, no
drive-by refactor and no TODO stub in a core path.

**Find the runner, and type the narrow form.** A wrapper in `bin/`, or
whatever the contribution guide names first, is cheap on the second call.
The builder types the one command the *Phase boundary* row or the *Review
rounds 1..n* row of `skills/verify/SKILL.md` *Scope: cheap and often, broad
and once* names, never the whole suite (`docs/running/the-run.md` *The
handoff*). Asking whether the suite catches something is a coverage probe,
a different act: the builder runs it over the module that should catch it
and reports it as a probe.

**Commit at the smallest step that stands on its own.** No gate stops a
commit: the routing is checked at the pull request
(`docs/checks/the-routing-check.md`). What an intermediate commit costs is a
property of the repository rather than a fact about committing: where
feature branches **squash** into their base, every commit the branch wrote
stops existing at the merge and none is left for anyone to read. Read that
off the repository before leaning on it; one that merges without squashing
keeps every commit in its history.

What committing *buys* is a separate matter, and that one holds everywhere. A
review round records the commit it read, so work still sitting in the working
tree is not visible to the reviewer at all — there is no spelling for *and
also the four files that were not committed yet*.

**A commit names its repository in the command that makes it.** Commit with
the repository's absolute path written out after `git -C`, in a command of
its own. Where a `cd` comes first, join it to the commit with `&&` and
nothing else. A file edit is contract rule 9's.

Your shell starts in the session's directory at every call, so a command
reaches your worktree through a `cd`, and whatever follows a `;` or a new
line after that `cd` also runs where a failed `cd` leaves the shell: the
session's own directory. A commit written with its path out lands where it
says whichever way the `cd` went, and a person reading the transcript can
see where that is.
check: tests/behaviour/test_a_commit_names_its_repository.py

**Before each commit, lint, format and typecheck the files it changes**,
with the tools the repository configures; the repository-wide run of each
is the broad gate's (contract rule 2). Nothing runs them when a file is
saved, so the party that commits runs them. The project's own package
manager wins; where it names none, Python runs through `uv` and Node.js
through `pnpm`.

**Commit before you mutate, and restore from `iadd mutate`'s copy.** A
revert through `git checkout -- <file>` restores the committed state and
takes every uncommitted fix in that file with it; `iadd mutate` holds the
bytes it read and compares the hash after the restore.

**Mutation-test every unit that adds behaviour, one command each.** The
builder breaks one unit, runs the cases that cover it, and watches one go
red; a unit that stays green while broken has nothing behind it. A unit
only renamed or moved adds nothing to break, and owes no run
(`skills/verify/SKILL.md` *The narrow command still has to be able to
fail*).

```
iadd mutate <file> --replace "<old>" "<new>" --tests "<the runner> <module> -k <cases>"
```

Each run is bounded at 300 s unless `--timeout` says otherwise, and a
timed-out run is a result to report. Where the runner starts pytest-xdist
workers by default, the builder adds `-p no:xdist` for a handful of cases.
`skills/verify/iadd-mutate.md` carries the verdicts and their exit codes.

**Three failed fixes stop the work.** The same bug through three failed
fixes is the architecture talking: stop, and the next step is the
architecture question, not a fourth fix.

**Before the builder closes a phase or a fix pass, its range and the work
item's records are read whole against HEAD.** After its last commit the
builder runs `iadd range <item> --from <commit> --out <file>`. `<item>` is
the work item's directory, `--from` names the commit the range starts
after, HEAD as the phase began or the commit
`skills/implement/fix-pass.md` *The narrow set, then the read of the range*
names for a pass, and `<file>` stands under the builder's scratch directory
(contract rule 17). The builder reads that file to its last line. It holds
every hunk of the range with the paragraph or unit around it, a case's
name, docstring and comments among them, and then each file of
`iadd/threads/<work-item-id>/` that states the present, whole: `routing.md`,
the three frame files, `gaps.md` and `changelog.md`. A coordinate or a
statement of the tree in a frame section dated to the commit the framer
read states that commit, not the present, and a sentence there that says
what the work does or concludes states the present (*Document layout — two
roots, three lifetimes* above). The builder fixes in its range every
statement HEAD contradicts in a file it writes: the code and tests of the
work, `gaps.md`, `changelog.md`, the phase record and the phase's Status
cell in `frame/plan.md`. A statement HEAD contradicts in `routing.md`,
or in a frame line the builder does not write, the crafter names in its
hand-back with its coordinate and the fact HEAD gives, and the orchestrator
folds it in a commit of its own, as `skills/implement/orchestration.md`
*Orchestrator: the order inside a ticket* states; the orchestrator that
builds folds it in such a commit itself. That set is closed, and reading it
whole is contract rule 12's second method, so none of it is handed on as a
sample. Then the builder finds the other places across the tree that state
each rule its range reworded or removed, by `git grep` on its words and by
its `check:` target, and corrects each or says in the account why it
stands; that list is a sample, and the account calls it one and says where
the part it did not reach stands. What the builder did not finish goes to
`gaps.md` `## Not done` with why. Neither that nor the part a sample did not
reach is the proofer's share.

**The account of that read quotes its commands and describes no read in
other words.** It names the commit the read ran at, which is HEAD after
the builder's last build or fix commit. It quotes, as typed, the
`iadd range` line with the lines the command printed, each command that
printed a correction's hunk after the commit that made the correction, and
each `git grep` of the sample. Then it gives each statement the read leaves
standing, with why, and where the part the sample did not reach stands.
The crafter writes the account in its hand-back. The orchestrator writes it
in `trail/phases/phase-N.md` `## What this phase found` for a phase, which
it commits last, and for a fix pass where `skills/implement/fix-pass.md`
*The narrow set, then the read of the range* puts it.

### 3. The SDD file set

Which files of the set a work item has is the orchestrator's to decide, by
the ladder in `skills/implement/orchestration.md` *Orchestrator: when a work
item is required*.

`questions.md` is not on that ladder: it starts with the batch collected
before the first edit (`skills/implement/orchestration.md` *Orchestrator:
what needs a person is asked in one batch, before the first edit*) and
gains a row whenever a decision only a human can make appears later, at any
size. A late one still gets written — the
batch is what keeps it from being the only way they arrive. A question is a
row there and never a sentence of `frame/design.md`, because an unanswered question
in prose reads as decided.

**A row's `Who can answer` cell takes one of three values.** **a person**:
what the product should be, or a value somebody has to be accountable for,
and the only kind of row that blocks the build. **a measurement**: a probe,
a command or a count settles it, so a person is the wrong instrument and a
row queued behind one wastes a round trip. **the work**: unknowable at
framing time; the phase that meets it decides it there and records the
decision in its phase record, and it does not travel back to the framer. **The framer
opens rows and does not own their answers**: the `Status` column is written
by whoever answered, as `answered <date> by <who>`, never by whoever asked.

A work item's directory is `iadd/threads/<unix-epoch-seconds>-<slug>/` (e.g.
`iadd/threads/1784780439-center-list-sort/`), bootstrapped from `templates/`. The
timestamp prefix keeps directories in creation order and collision-free
without a registry — take it from `date +%s` when creating the directory.

| File | Starts from | Written by | Holds | When |
|---|---|---|---|---|
| `routing.md` | `templates/records/sdd-routing.md` | the session that spawns the work, from the batch it asked — never a subagent, which has no way to put the question to anybody | the routing answer | before the first edit, and so before a framer is spawned |
| `frame/design.md` | `templates/records/sdd-design.md` | the framer | WHAT — scope, mandatory user scenarios & acceptance, grounding clauses, the rule changes the settle writes into the policy root (`## Rule changes`), and the framer's mark at its foot, with a `Reframed` line under it for each time the review chain sent the work item back (`docs/running/the-run.md` *The run* owns that rule and spells the line) | before implementing |
| `frame/plan.md` | `templates/records/sdd-plan.md` | the framer; the orchestrator adds the rows of `## Judgments of the run` | HOW — phases as vertical slices, alternatives with failure scenarios; this is the Design Gate's artifact, approved by the spawn that builds it. Its last section holds the orchestrator's judgments of the run, each with its grounds and the document it stands on, which `iadd settle`'s dry run reads | before implementing (gated work); a judgment's row when it is made |
| `frame/questions.md` | `templates/records/sdd-questions.md` | the framer opens the rows; each row's `Who can answer` cell names who closes it | decisions only a human can make — extracted so nothing ships on a silent assumption | one batch before the first edit, then as they arise |
| `gaps.md` | `templates/records/sdd-gaps.md` | the builder | the closing memo — what went out unproved and who answers it, and what was within reach and not taken (below) | written from its template when the first phase closes; every later phase and fix pass adds to it |
| `trail/phases/phase-N.md` | `templates/records/sdd-phase.md` | the builder | what building this phase found, each departure from the frame among it — never what the work removes, which the frame names as `docs/running/the-agent-set.md` *What each party writes, and when* says, and never the commit or what the phase was asked, which `plan.md`'s Status and Delivers cells own | written when the phase closes |
| `pr.md` | no template: `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared* gives its shape | the orchestrator, where the work runs through the review chain | the pull request body's first part, after `pr.<lang>.md` where `config.json`'s two language keys differ, which `iadd pr-body` writes above the records' copy. What `pr.md` and `pr.<lang>.md` hold is stated in `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared* | once the build's last phase has closed, before the first round, with its `pr.<lang>.md` where the keys differ |

Reading `plan.md` and spawning the build is the approval, and no line
records it: the phase's Status cell is the trace that the build happened.

**`trail/phases/phase-N.md` holds one section, `## What this phase found`:
what building the phase taught that `plan.md`'s cells do not.** That is a
decision settled while writing the code, a constraint found only by trying,
each `seen red` and mutation claim, every departure from the frame, a
removal the frame did not name among them (`docs/running/the-agent-set.md`
*What each party writes, and when*), and anything the next phase needs.
What the phase was asked is the plan's Delivers cell, and a scope a spawn
gives beyond it is a decision the framer folds into the plan before the
spawn (`skills/implement/orchestration.md` *Orchestrator: the order inside
a ticket*), so the record copies neither. A discovery reaches the next phase
only through that section or through the orchestrator retyping it into the
next spawn prompt, and the second goes missing without a trace when the
orchestrator does not.

**`plan.md`'s Phases table is the task list, and there is no other.** Each
phase carries a **Verified by** column, so it cannot be called done the way a
checkbox can be ticked, and a **Status** column that is empty, holds the
commit that closed the phase, or reads `deferred #N` for a phase the work
item handed to issue #N. A commit and an issue each name something someone
can open, so a tick and the word `done` are refused where neither is named.
The party that builds a phase fills its cell as the phase closes, not at the
end.

**`frame/design.md` ends with its frame's mark**, `Framed <date> by <who>, before the
build.`, where `<who>` is the `Planning` row's answer in `routing.md`,
`framer` or `the session`; `chain_check.py` refuses a `Planning | framer`
work item whose mark names anyone else.

### 4. The closing memo — only what the diff cannot show

`iadd/threads/<work-item>/gaps.md` is not a summary of the work. `git diff --stat`
already holds the file list and the diff holds the detail; re-deriving them at
the end costs a re-read of your own change and lands further from the truth
than the command would.

Two things go in it, and after the session closes neither is anywhere else.
The first phase writes it from its template when it closes, and every later
phase and fix pass adds to it. Write each row **when it happens** — a call
made at minute ten is invisible by minute ninety, and reconstruction is the
expensive way to get a worse answer.

1. What was not verified — with **who has to answer it**, at the moment you
   decide not to run something (`## Not verified`).
2. What was within reach and deliberately not taken, with its grounds, in
   prose, because those are decisions rather than pending claims
   (`## Not done`).

On the ladder's second rung (`skills/implement/orchestration.md`
*Orchestrator: when a work item is required*), `## Scope confirmation`
holds the one line that replaces `plan.md`. Why the work exists is the
changelog fragment's, and a departure from the frame is the phase record's
that made it. A memo with nothing unverified and nothing left is correct and
short: the no-change block and `nothing`.

**`## Not verified` is read by a machine, so it has one shape** — a
`| Item | Who must answer |` table, or alone the no-change block
`skills/settle/rule-changes.md` *Rule changes* states, `- nothing` with the
reason in its one field `why:`, which the block may leave out. Any other
spelling of the heading, of the header row or of the `- nothing` line, a
second item, a field other than `why:` or an empty `why:` fails the check
rather than reporting zero, because zero reads as "everything has been
closed". The template's placeholder row fails it too, until it is filled in
or the block replaces the table.

An item is closed by marking it, never by deleting it: the Item cell opens
with the word `closed`, lower case, then the item.

```
| closed how the gates render in a TUI | seen on screen, session of 2026-08-25 |
```

An unmarked row counts open, so the silent direction is "still open", except
for an open item whose own text begins with the word `closed`, which reads as
closed and which only a reader catches: word such an item to open with
another word. A bare `closed` with nothing after it is refused the same way a
ticked checkbox is. No check at the pull request refuses a deleted row, or a
deleted file: the proofer reads the closing memo's diff, where a row that left
without the word `closed` shows, and so does a memo that left whole. That
reading is what keeps "I verified it" and "I tidied it away" from being the
same edit.

No check judges whether the second cell of a closed row says what closed
the item. `iadd unverified` refuses that cell only where it is empty or
still the template's placeholder, and `iadd settle` prints it as it stands.
Leaving the original answerer in place beside the word is how a closing goes
out unproven, and only a reader catches it.

### 5. Incorporate review — read the round records first

A fix pass, the crafter's or the orchestrator's, opens
`skills/implement/fix-pass.md` before it judges the first finding, and
follows it: where the pass starts, how it reads a finding and a paste-ready
fix, what it runs once the fixes are committed, and the close blocks it
appends to `trail/rounds/round-N.md`.

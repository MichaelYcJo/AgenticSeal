---
name: implement
description: |
  Spec-driven implementation methodology: document layout (docs/ + seal/), policy-first
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

**`skills/agent-contract/SKILL.md` binds this session too, and only if you
load it.** A session driving the work directly reads this skill and never
`agents/*.md`, so the contract every agent it spawns receives at startup
reaches it by being opened rather than by arriving — `user-invocable: false`
permits the load and does not oblige it.

**If you are orchestrating a work item rather than building it, read
`skills/implement/orchestration.md` before the first edit**; an implementer
never opens it, and everything below is the implementer's and the
orchestrator's alike.

## The language the records are written in

**Read `Record language` in `config.md` before writing any of the documents
below**, the same way `commit-pr-convention` reads its own row before a commit
or a pull request. The root is resolved the way every path in this skill is.

```markdown
| Item | Value |
|---|---|
| Record language | Korean |
```

It governs the **prose** in `frame/design.md`, `plan.md`, `gaps.md`,
`questions.md`, `changelog.md`, the cell contents of `trail/rounds/round-N.md` and
`trail/phases/phase-N.md` and the text beneath their tables.

**Every way of not naming one lands on English** — no file, no such row, an
empty value, a file that cannot be read. A config nobody can read must not
stop the work.

**It is independent of `Commit and pull request language`.** Setting one does
not carry the other; `docs/layout/one-root-by-lifetime.md` *What the repository
decides for itself, and how it is read* gives the reasons.

**What stays English whatever it says**, because these are read literally
rather than by a person: every field name, section heading and vocabulary
word the checkers match, listed in `templates/setup/config.md` under *What no row
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
| `docs/` | Permanent, cumulative | Must still be true in 6 months | **Norms, ratified by humans.** Read when the repository has them; the documentation convention is the project's. The policy root (`docs/` unless `seal/config.md`'s `Policy root` names another) is the baseline. A work item whose subject is the policy root itself, its structure or its documents' text, edits the policy root directly in its pull request, as the settle does, and re-points in that pull request every unsettled design's `## Rule changes` operation that names a document or a section it moved. A work item whose subject is the code states the rules its work changes in `## Rule changes`, for the settle, so that work items running side by side do not each rewrite the same section. Which subject a work item has is the framer's judgment, read by the proofer at review. The settle after the release writes each section as the latest decision the released designs state, checked against the code (`skills/settle/SKILL.md`), and the policy in force is the baseline plus the latest decision the unsettled designs' rule changes state at each section, in merge order |
| `seal/threads/<work-item-id>/` | One work item | Its role ends when this work ships (the frame, the trail, the closing memo) | The contract this work executes against. A human approves `frame/plan.md`, which is why this is a repository document and not tool state |
| `seal/`, everything above `threads/` | Permanent | Everything this plugin maintains | Written and read by machines |

A `specs/` the project kept before the plugin is neither root: it is a
**reference root**, as `templates/setup/config.md` *Reference specs* says — history
read where the work touches what it describes, cited in `frame/design.md` where it was
read, and never written by anything this skill produces.

The axis is lifetime and authority, **not audience** — humans and AI read all
three. (Labeling policies "for humans" would push sessions away from reading
them, and policy outranks everything else when a repository has it.)

Inside the policy root, documents are grouped by who opens them and at which
step, and any party may open any group.

`seal/` lives at one of two places, and its presence at either, with a
`README.md` that opens with the marker `hooks/lib/optin.py#MARKER` holds, is what
tells the gates this repository runs the workflow. **Every `seal/…` path in
this plugin's skills and agents means `<repo>/seal/` where that directory
exists with the marker, and
`$(git rev-parse --git-common-dir)/seal/` otherwise.** The first is
shared mode: committed, because gitignored files do not follow worktrees or
other machines. The second is local mode: under the common git directory, so
every linked worktree of the clone shares it, and never a commit candidate.
A repository with both is shared, and nothing else — no config key — is
read. What sits directly under it is permanent; what sits under
`seal/threads/` lives as long as its work item. Each file the root holds,
and the question it answers, is in `docs/layout/the-record-layout.md`
*seal/*, and each file of a work item's directory is in
`docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/*.

The review round records live beside the work item they are about, with the
routing declaration and the rest of the SDD set
(`docs/forms/the-round-record.md`).
A work item's directory exists from its first commit, because routing is
written into it before the first edit.

**Nothing else follows them, because there is nothing else.** A round record
carries the SHA it reviewed, so it never asserts a present state and can live
beside the contract. Progress does the same thing one file up, in `plan.md`'s
Status column, where a closed phase carries the commit that closed it — the
same past-state trick, for the same reason.

**Judgment precedence is policy > SDD > code where policy exists, and
SDD > code where it does not.** Most repositories are the second kind. Do not
manufacture the first by writing policy documents nobody asked for: the SDD set
is the root of judgment, and a policy document is a thing a human decides to
keep.

## Procedure

### 1. Read the documents that outrank the code first

Judgment precedence: **policy (`docs/`) > SDD (`seal/threads/`) > the ticket >
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
- Read `seal/follow-up.md` before starting. It holds items
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

What needs a person is asked once, in one batch, before the first edit, by
the orchestrator, which opens `skills/implement/orchestration.md`
*Orchestrator: what needs a person is asked in one batch, before the first
edit* when it starts a work item.

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

This is the input for the reviewer and the next ticket: a case somebody can
run rather than a reading somebody did. A judgment settled by opening code
and leaving no case behind gets redone by every session that follows — the
single largest avoidable cost in multi-session work.

**Commit at the smallest step that stands on its own.** No gate stops a
commit: the routing is checked at the edit tools and at the pull request
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
is the broad gate's (contract rule 2). `hooks/lint-python.py` already runs
`ruff` on each Python file an edit tool saves, where the project configures
ruff. The project's own package manager wins; where it names none, Python
runs through `uv` and Node.js through `pnpm`.

**An edit must be able to fail.** Prefer the `Edit` tool: a pattern that does
not match is an error you see immediately. When the environment routes edits
through the shell instead — `sed -i`, a heredoc, a short script — a
substitution whose pattern misses does nothing, says nothing, and exits zero.
The miss surfaces at the next check, and the cost is another edit and another
run of whatever you had already run.

So assert the landing. Every shell substitution states what it expected to
match and fails loudly when it did not:

```python
assert old in text, f"pattern did not match: {old[:60]}"
```

This is `verify`'s second condition — *a check that cannot fail is a
counterfeit seal* — applied one step earlier. An edit that cannot fail is an
unverified edit, and reporting it as made is the same claim as reporting a
`read` as passing.

**Three failed fixes stop the work.** The same bug through three failed
fixes is the architecture talking: stop, and the next step is the
architecture question, not a fourth fix. Three returns through the broad
gate read the same way: a fourth says the narrow scope misses a class of
breakage.
check: tests/text/test_a_moved_rule_leaves_its_definition.py

### 3. The SDD file set

Which files a work item has, and whether it has a `frame/design.md` and a
`plan.md` at all, is the ladder's: the orchestrator reads it in
`skills/implement/orchestration.md` *Orchestrator: when a work item is
required* before it spawns a framer.

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

A work item's directory is `seal/threads/<unix-epoch-seconds>-<slug>/` (e.g.
`seal/threads/1784780439-center-list-sort/`), bootstrapped from `templates/`. The
timestamp prefix keeps directories in creation order and collision-free
without a registry — take it from `date +%s` when creating the directory.

| File | Starts from | Written by | Holds | When |
|---|---|---|---|---|
| `routing.md` | `templates/records/sdd-routing.md` | the session that spawns the work, from the batch it asked — never a subagent, which has no way to put the question to anybody | the routing answer | before the first edit, and so before a framer is spawned |
| `frame/design.md` | `templates/records/sdd-design.md` | the framer | WHAT — scope, mandatory user scenarios & acceptance, grounding clauses, the rule changes the settle writes into the policy root (`## Rule changes`), and the framer's mark at its foot, with a `Reframed … after round <N>.` line under it for each time the review chain sent the work item back (`docs/running/the-run.md` *The run* owns that rule) | before implementing |
| `frame/plan.md` | `templates/records/sdd-plan.md` | the framer; the orchestrator adds the rows of `## Judgments of the run` | HOW — phases as vertical slices, alternatives with failure scenarios; this is the Design Gate's artifact, approved by the spawn that builds it. Its last section holds the orchestrator's judgments of the run, each with its grounds and the document it stands on, which `seal settle`'s dry run reads | before implementing (gated work); a judgment's row when it is made |
| `frame/questions.md` | `templates/records/sdd-questions.md` | the framer opens the rows; each row's `Who can answer` cell names who closes it | decisions only a human can make — extracted so nothing ships on a silent assumption | one batch before the first edit, then as they arise |
| `gaps.md` | `templates/records/sdd-gaps.md` | the builder | the closing memo — what went out unproved and who answers it, and what was within reach and not taken (below) | written from its template when the first phase closes; every later phase and fix pass adds to it |
| `trail/phases/phase-N.md` | `templates/records/sdd-phase.md` | the builder | what building this phase found, each departure from the frame among it — never what the work removes, which the frame's `## Removes` names once, and never the commit or what the phase was asked, which `plan.md`'s Status and Delivers cells own | written when the phase closes |

The `Starts from` column is not decoration. A template that no shipped
document names is a template a session cannot find: it reads *bootstrapped
from `templates/`*, cannot tell which file that means, and writes one from
scratch.

`Written by` is the same kind of column, for the same kind of reason. The
split it records is what `agents/framer.md` exists for, and
`docs/running/the-agent-set.md` *One contract every agent receives, and one
definition each* says why the party that draws a contract is not the party
that executes it. A table that lists the set without naming an author reads
as a list one session works through. Below the ladder's top rung there is no
framer and no `frame/design.md`; the session that builds writes whatever that
rung asks for, and the column is about who holds the pen when both parties
exist.

Reading `plan.md` and spawning the build is the approval, and no line
records it: the phase's Status cell is the trace that the build happened.

**`trail/phases/phase-N.md` holds one section, `## What this phase found`:
what building the phase taught that `plan.md`'s cells do not.** That is a
decision settled while writing the code, a constraint found only by trying,
each `seen red` and mutation claim, every departure from the frame, a
removal the frame's `## Removes` did not name among them, and anything the
next phase needs. What the phase was asked is the plan's Delivers cell, and
a scope a spawn gives beyond it is a decision the orchestrator folds into
the plan before the spawn, so the record copies neither. A discovery reaches
the next phase only through that section or through the orchestrator
retyping it into the next spawn prompt, and the second goes missing without
a trace when the orchestrator does not.

**`plan.md`'s Phases table is the task list, and there is no other.** Each
phase carries a **Verified by** column, so it cannot be called done the way a
checkbox can be ticked, and a **Status** column that is empty or holds the
commit that closed the phase. A commit asserts a **past** state that someone
can open, so a tick and the word `done` are refused where a hash is not. The
party that builds a phase fills its cell as the phase closes, not at the end.
Where feature branches squash, those commits stop resolving at the merge.
Nothing measures from the column, which is why that is tolerable. A rebase
during the work would orphan them earlier and more quietly, because the
orphaned object still answers `git cat-file` in the worktree that wrote it,
and it would orphan the commits the round records name as well. So a work
item's branch is never rebased (`skills/code-review/orchestration.md`
*Orchestrator: the pull request opens once the sealer seals*).

**`frame/design.md` ends with its frame's mark**, `Framed <date> by <who>, before the
build.`, where `<who>` is the `Planning` row's answer in `routing.md`,
`framer` or `the session`; `chain_check.py` refuses a `Planning | framer`
work item whose mark names anyone else.

### 4. The closing memo — only what the diff cannot show

`seal/threads/<work-item>/gaps.md` is not a summary of the work. `git diff --stat`
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
without the word `closed` shows, and `seal unverified --baseline
origin/<base>`, run by a person, names each one. That reading is what keeps
"I verified it" and "I tidied it away" from being the same edit.

What the command reads is the **number** of rows, not their text. So the second
cell saying what closed the item is a convention it cannot enforce: swapping
one row for another keeps the count and passes. Leaving the original answerer
in place beside the word is how a closing goes out unproven, and only a
reader catches it.

Never record something as passing that you did not run. Findings from reading
and findings from execution are labeled separately.

### 5. Incorporate review — read the round records first

A session fixing review feedback starts at `seal/threads/<work-item-id>/trail/rounds/`,
**not** at the inline comments: the proofer writes `round-N.md`, and the next
review round reads it (`docs/forms/the-round-record.md` *The round record*).

A finding is a claim too, and it arrives from someone who did not write the
code. Open the coordinate and judge it yourself: fix what holds, and where it
does not, answer it in `round-N.md` with the grounds — the policy clause, the
original's behavior, the constraint that makes the state unreachable. What is
not allowed is the third path, changing the code to quiet a finding you do not
believe. A review the implementer cannot argue with is not a review, it is a
handoff of judgment.
Probes already run by a previous round (listed in `round-N.md`) are not
rebuilt — only re-checked for whether the finding is now fixed.

**A fix pass appends one close block to each open finding in
`trail/rounds/round-N.md`, edits nothing else in it, and writes no phase
record** — `docs/forms/the-round-record.md` *The round record* names the three
closing verdicts, and `hooks/lib/fields.py` spells the block's lines. A
`fixed` commit must touch a path the finding's `location:` names; where the
fix went somewhere else, the close block carries a `location:` line naming
that coordinate, and its `answer:` says so. The build's phases keep theirs.

A fix that changes what the work item ships brings the work item's
`changelog.md` along, because the release note is built from that fragment as
it stands at the tag;
`docs/layout/the-record-layout.md` *A commit after the build brings its changelog
fragment along* owns that rule.

Once the last round record has no finding open, the orchestrator moves the
rows still open to their destinations, as
`skills/implement/orchestration.md` *Orchestrator: drain the rows before the
broad run, and keep the records* states.

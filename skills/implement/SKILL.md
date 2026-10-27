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

Methodology for implementing against written specs, leaving a case behind
each rule, and closing the loop with review. Opened by the `crafter` agent at
its first step; usable directly.

**`skills/agent-contract/SKILL.md` binds this session too, and only if you
load it.** A session driving the work directly reads this skill and never
`agents/*.md`, so the contract every agent it spawns receives at startup
reaches it by being opened rather than by arriving — `user-invocable: false`
permits the load and does not oblige it. #107's headline failure is an
orchestrator breaking a rule it had put into every prompt it sent.

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
not carry the other, and the two surfaces have different audiences: a pull
request is read by whoever opens it, and a record is read by whoever comes
back to the decision six months later.

**What stays English whatever it says**, because these are read literally
rather than by a person: every field name, section heading and vocabulary
word the checkers match, listed in `templates/config.md` under *What no row
governs* — that list is derived from the checkers' own constants, so it
cannot drift from them; `<!-- specs/<work-item-id> -->` and the other
markers; a `drained` line and the `closed` that opens a closed row; and all
code — identifiers, comments, docstrings, file names, test function names. A
translated field name is not a translation, it is a checker that
stops reading.

## Document layout — two roots, three lifetimes

Every artifact this skill produces goes to one of two roots, and the second is
laid out by **lifetime**, not by who wrote it:

| Root | Lifetime | Test | Authority |
|---|---|---|---|
| `docs/` | Permanent, cumulative | Must still be true in 6 months | **Norms, ratified by humans.** Read when the repository has them; the documentation convention is the project's. The policy root (`docs/` unless `seal/config.md`'s `Policy root` names another) is the baseline, and a pull request does not edit it. A spec states its changes in `## Rule changes`, the settle after the release writes each section as the latest decision the released specs state, checked against the code (`skills/settle/SKILL.md`), and the policy in force is the baseline plus the latest decision the unsettled specs' rule changes state at each section, in merge order |
| `seal/threads/<work-item-id>/` | One work item | Its role ends when this work ships (the frame, the trail, the closing memo) | The contract this work executes against. A human approves `frame/plan.md`, which is why this is a repository document and not tool state |
| `seal/`, everything above `threads/` | Permanent | Everything this plugin maintains | Written and read by machines: the repository's config, the migration config, the follow-up list |

A `specs/` the project kept before the plugin is neither root: it is a
**reference root**, as `templates/config.md` *Reference specs* says — history
read where the work touches what it describes, cited in `frame/design.md` where it was
read, and never written by anything this skill produces.

The axis is lifetime and authority, **not audience** — humans and AI read all
three. (Labeling policies "for humans" would push sessions away from reading
them, and policy outranks everything else when a repository has it.)

`seal/` lives at one of two places, and its presence at either, with a
`README.md` that opens with the marker `hooks/optin.py#MARKER` holds, is what
tells the gates this repository runs the workflow. **Every `seal/…` path in
this plugin's skills and agents means `<repo>/seal/` where that directory
exists with the marker, and
`$(git rev-parse --git-common-dir)/seal/` otherwise.** The first is
shared mode: committed, because gitignored files do not follow worktrees or
other machines. The second is local mode: under the common git directory, so
every linked worktree of the clone shares it, and never a commit candidate.
A repository with both is shared, and nothing else — no config key — is
read. What sits directly under it is permanent; what sits under
`seal/threads/` lives as long as its work item:

```
seal/
├── README.md         what the root holds, and where the export rules are
├── parity.md         migration config, only when declared
├── pact.md           the pact, only in the repository that holds one
├── follow-up.md      schedulable items in a repository with no tracker
└── threads/<work-item-id>/
    ├── routing.md    the routing answer, written by the session before the
    │                 first edit; a framer reads it and never writes it
    ├── frame/        design.md, plan.md, questions.md: the design before the build
    ├── trail/phases/phase-N.md   one build phase's record
    ├── trail/rounds/round-N.md   one review round — closed at merge, removed
    │                             with its work item at the settle after its release
    ├── trail/gate.md             the one broad run, written by `seal gate --record`
    ├── changelog.md  this work item's entry in the next release's notes
    ├── gaps.md       the closing memo
    └── guarantee.md  the sealer's verdict, from `templates/sdd-guarantee.md`
```

The review round records live beside the work item they are about, with the
routing declaration and the rest of the SDD set (`docs/the-review-record.md`).
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

### 1. Read the spec before the code

Judgment precedence: **policy (`docs/`) > SDD (`seal/threads/`) > the ticket >
existing code** — and, where the repository declares a migration config, the
original sits between the ticket and the existing code, because policy being
silent is what makes the original decide (see `legacy-parity`).

A spec that contradicts policy gets fixed, not followed. **A ticket is a
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
  from) the documents they cite; a missing clause is an `add` in the spec's
  `## Rule changes`, with a freshly allocated number.
- A spawn prompt's facts arrive under `docs/the-review-record.md`'s
  handoff: coordinates rather than prose, each fact labelled
  executed, read, or unverified. A fact with no coordinate and no label is an
  assertion nobody has opened — open it before building on it, however
  confident the prompt that carried it. An aggregate (a count, a total) is
  not a coordinate: the number can be checked while the claim it stands for
  cannot, and one such fact reached five documents before a review round
  found it false.

**Collect what needs a person before the first edit, and ask it in one batch.**
Read the spec chain looking for the questions as well as the answers, and put
every one of them in front of the user at the start: a decision only they can
make, an approval, a credential, a permission the session does not have.

The cost of a question is not its difficulty, it is when it arrives. Asked
before the work starts, it costs a reply. Asked at minute thirty, it stops
everything until someone is at the keyboard — and the longer a session is
meant to run unattended, the more of it a late question wastes. Asking one at
a time is the same failure spread out: three interruptions cost three waits.

Two things sharpen the list:

- **A question you can answer is not a question.** Read the documents and the
  code first. What survives that is the batch.
- **Assume, in writing, whatever would not change what you build.** State the
  assumption in `questions.md` and continue. Only where different answers mean
  different code does the work actually have to wait.

Something a session cannot do for itself belongs on the same list — widening
its own permissions, for one, which the harness blocks by design. Better
found in the first minute than at the commit.

**A question in this batch names its answers, and every answer continues.**
"Should I release this?" and "should the proofer review it?" both have a `no`
that leads nowhere — the session that answers it is holding finished work with
no destination, which is a gate wearing the shape of a question. A yes/no is
the tell. Ask which of two named paths instead, and say what each one does.

**The first edit waits for the routing answer, and a gate holds that.**
`hooks/routing-edit-gate.py` refuses a `Write`, `Edit` or `NotebookEdit` of
a file in an opted-in repository while no `routing.md` names the branch
checked out where the file is and the session has not run
`seal no-work-item` on that branch. A file under the `seal/` root or one git
ignores is not judged, so the declaration can always be written first.
`seal no-work-item` records, for this session on the branch checked out
where it runs, that its change belongs to no work item; on a detached HEAD
it records nothing.

**Once the batch is answered, the session runs to the pull request.** What
surfaces after it is written down rather than raised: a decision only a person
can make goes to `questions.md`, a finding you neither fixed nor answered to
`seal/follow-up.md` with an answerer named — a deferral to nobody is how
"someone will look at it" becomes nobody did (`skills/verify/SKILL.md` *The
answerer has to exist*) — and what was deliberately left goes to the overview's Not done
section. Each is named in the PR body, because a leftover nobody can find was
not handed over. On a branch whose `routing.md` answers `Automation` with
`yes`, `hooks/question-gate.py` holds this, and `docs/the-review-record.md`
*The run* is the rule.

The test for whether something is a question or a row: would a different
answer change what you build *now*? If it would not, raising it spends a
person's attention on something that was never blocking, and the session that
waits for the reply spends more.

### 2. Implement test-first, and let each rule name its test

**Each scenario is built the same way: its case first, seen red against the
tree as it stands, then the code, then the case green.** A rule the work
states or changes ends with a `check:` line naming that case — in its home
under `docs/`, or in the *Verifiable how* cell of the spec's scenario table —
so the case is the record that the rule holds, and CI running the suite is
the check. A rule no case can hold says `check: none reader: <who reads it>`,
and the reader is who holds it instead. The grammar is
`skills/settle/SKILL.md` *A rule has one shape*.

This is the input for the reviewer and the next ticket: a case somebody can
run rather than a reading somebody did. A judgment settled by opening code
and leaving no case behind gets redone by every session that follows — the
single largest avoidable cost in multi-session work.

**Commit at the smallest step that stands on its own.** No gate stops a
commit: the routing is checked at the edit tools and at the pull request
(`docs/the-routing-check.md`). What an intermediate commit costs is a
property of the repository rather than a fact about committing: where
feature branches **squash** into their base, every commit the branch wrote
stops existing at the merge and none is left for anyone to read. Read that
off the repository before leaning on it; one that merges without squashing
keeps every commit in its history.

What committing *buys* is a separate matter, and that one holds everywhere. A
review round records the commit it read, so work still sitting in the working
tree is not visible to the reviewer at all — there is no spelling for *and
also the four files that were not committed yet*.

*Commit as you go* alone does not settle the cadence. One session was told
exactly that and did it, eight commits across two rounds, and still had five
modified files in the working tree when an unrelated command reached the
worktree guard. That window has a price wherever this plugin is installed: the
guard asks whether the changes should ride along to the other branch, and
*commit them here first* — the answer that is usually right — is not one of
the two buttons. Nothing had said how early early is.

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

### 3. The SDD file set

**When a work item is required** — the same threshold the Design Gate uses,
because they are the same judgment. Drawing no line is how the set quietly
stops being written.

| Work | What to write |
|---|---|
| It **alters observable behaviour** — a gate's verdict, a hook's output, a skill's or agent's instructions, a public API, text a person reads and acts on. Or it changes a value someone waits on or is limited by — a timeout, a retry count, a rate, a size cap — and NAMING that value is what puts it on this rung | `frame/design.md` and `plan.md` **before** implementing — approval of `plan.md` IS the gate — then the closing memo |
| It alters none of that and is more than one line — a refactor, a performance pass, a formatting sweep, a test that pins what already holds. These four are DEFAULTS, not a closed list: a performance pass that moves a timeout a person waits on belongs on the rung above, and the value's name is what moves it | the closing memo. A one-line scope confirmation replaces the plan |
| A typo, a config value, a one-line fix | nothing |

**Behaviour, not file count, and the difference runs both ways.** The top rung
used to read *6+ files, a new module, or an architectural choice*, and two of
those three conditions measured size.

- **One file, and it qualifies.** A change to an agent's persona is two files
  of wording, and wording is what a session reads and acts on, so it needs a
  plan at file one.
- **Many files, and it does not.** Copying test repositories instead of
  running `git init` for each touched more files than that and altered nothing
  anyone can observe — no verdict, no output, no instruction. The suite runs
  faster and says the same things.

A count also has to say **when** it is taken, and the gate it guards — plan
approval — exists only before the first edit (issue #35); a test with no
number has no such moment, so the question stops needing an answer.

What it costs: *does this alter observable behaviour* is a judgment where
*six files* was a count, and two people can disagree about a borderline case.
That is the trade — a judgment that is about the right thing beats a
measurement of the wrong one, and the list in the rung is what keeps the
judgment from being free-form. The way out of a default is to NAME the value a
person waits on or is limited by, which a reader can open and check. *I judged
it observable* is not something anyone can check, and it is not a way out.

`questions.md` is not on that ladder: it starts with the batch collected
before the first edit (step 1) and gains a row whenever a decision only a
human can make appears later, at any size. A late one still gets written — the
batch is what keeps it from being the only way they arrive. A question is a
row there and never a sentence of `frame/design.md`, because an unanswered question
in prose reads as decided.

**A row's `Who can answer` cell takes one of three values.** **a person**:
what the product should be, or a value somebody has to be accountable for,
and the only kind of row that blocks the build. **a measurement**: a probe,
a command or a count settles it, so a person is the wrong instrument and a
row queued behind one wastes a round trip. **the work**: unknowable at
framing time; the phase that meets it decides it there and records a
divergence row, and it does not travel back to the framer. **The framer
opens rows and does not own their answers**: the `Status` column is written
by whoever answered, as `answered <date> by <who>`, never by whoever asked.

A work item's directory is `seal/threads/<unix-epoch-seconds>-<slug>/` (e.g.
`seal/threads/1784780439-center-list-sort/`), bootstrapped from `templates/`. The
timestamp prefix keeps directories in creation order and collision-free
without a registry — take it from `date +%s` when creating the directory.

| File | Starts from | Written by | Holds | When |
|---|---|---|---|---|
| `routing.md` | `templates/sdd-routing.md` | the session that spawns the work, from the batch it asked — never a subagent, which has no way to put the question to anybody | the routing answer | before the first edit, and so before a framer is spawned |
| `frame/design.md` | `templates/sdd-design.md` | the framer | WHAT — scope, mandatory user scenarios & acceptance, grounding clauses, the rule changes the settle writes into the policy root (`## Rule changes`), and the framer's mark at its foot, with a `Reframed … after round <N>.` line under it for each time the review chain sent the work item back (`docs/the-review-record.md` *The run* owns that rule) | before implementing |
| `frame/plan.md` | `templates/sdd-plan.md` | the framer | HOW — phases as vertical slices, alternatives with failure scenarios; this is the Design Gate's artifact, and its `Approved <date> by <who>` line is the record that the gate happened | before implementing (gated work) |
| `frame/questions.md` | `templates/sdd-questions.md` | the framer opens the rows; each row's `Who can answer` cell names who closes it | decisions only a human can make — extracted so nothing ships on a silent assumption | one batch before the first edit, then as they arise |
| `gaps.md` | `templates/sdd-gaps.md` | the builder | the closing memo — one line of purpose, then what the diff cannot show (below) | opened at the first divergence, unverified item, or fed-back clause; closed when implementation ends |
| `trail/phases/phase-N.md` | `templates/sdd-phase.md` | the builder | what this phase was asked and what building it found — never what the work removes, which the frame's `## Removes` names once, and never the commit or the one-line delivery description `plan.md`'s Status/Delivers cells already own | written when the phase closes |

The `Starts from` column is not decoration. A template that no shipped
document names is a template a session cannot find: it reads *bootstrapped
from `templates/`*, cannot tell which file that means, and writes one from
scratch.

`Written by` is the same kind of column, for the same kind of reason. The
split it records is what `agents/framer.md` exists for: a `frame/design.md` written by
whoever then builds against it stops being a contract and becomes an account
of what got built, which leaves the review's first stage comparing the work
with its own description of itself. A table that lists the set without naming
an author reads as a list one session works through — which is what every work
item here did before the framer shipped, and what nothing in the set could say
was wrong. Below the ladder's top rung there is no framer and no `frame/design.md`;
the session that builds writes whatever that rung asks for, and the column is
about who holds the pen when both parties exist.

Where a work item records the approval is the `plan.md` line above, and it is
the only durable trace of the gate. `routing.md` records who answered the
routing batch, the review chain records what it read, and neither of them says
a person saw the plan.

**What goes into `trail/phases/phase-N.md`'s `## What this phase was asked`
section is the phase-specific content of the spawn or task that started
it** — never the boilerplate the contract, this skill, and `agents/crafter.md`
already carry, which every phase gets told by definition and none of them
need repeated in their own record. Copy it in when the phase closes: what
the spawn prompt or task description said this phase, specifically, had to
build. The section is how a reader opening the record later, with the spawn
prompt gone, tells a scope the orchestrator gave the phase from one the phase
invented. `## What this phase found` holds what building the phase taught
that `plan.md`'s cells do not: a decision settled while writing the code, a
constraint found only by trying, anything the next phase needs. A discovery
reaches the next phase only through that section or through the orchestrator
retyping it into the next spawn prompt, and the second goes missing without
a trace when the orchestrator does not.

**`plan.md`'s Phases table is the task list, and there is no other.** Each
phase carries a **Verified by** column, so it cannot be called done the way a
checkbox can be ticked, and a **Status** column that is empty or holds the
commit that closed the phase. A commit asserts a **past** state that someone
can open, so a tick and the word `done` are refused where a hash is not. The
party that builds a phase fills its cell as the phase closes, not at the end.
Where feature branches squash, those commits stop resolving at the merge, and
**a rebase during the work does the same earlier and more quietly**, because
the orphaned object still answers `git cat-file` in the worktree that wrote
it; **the party that rebases the branch re-reads the column after the
rebase**. Nothing measures from the column, which is why that is tolerable.

**`frame/design.md` ends with its frame's mark**, `Framed <date> by <who>, before the
build.`, where `<who>` is the `Planning` row's answer in `routing.md`,
`framer` or `the session`; `chain_check.py` refuses a `Planning | framer`
work item whose mark names anyone else. The mark, `plan.md`'s approval line
and `routing.md`'s `Answered` line share one shape, the verb, the date, who
and the moment, so the three stay one convention.

### 4. The closing memo — only what the diff cannot show

`seal/threads/<work-item>/gaps.md` is not a summary of the work. `git diff --stat`
already holds the file list and the diff holds the detail; re-deriving them at
the end costs a re-read of your own change and lands further from the truth
than the command would.

Four things go in it, and after the session closes three of them are nowhere
else. Write each **when it happens** — a call made at minute ten is invisible
by minute ninety, and reconstruction is the expensive way to get a worse
answer.

1. Why this work exists and what the result changes — **one line**, not a walk
   through the diff. Where the change alters nothing observable no `frame/design.md`
is written, so this is
   the only place the purpose stays in the repository.
2. Where spec and implementation diverged — both sides quoted, which side won,
   and the grounds, at the moment you decide it. "The document probably said
   so" is not grounds; quote it.
3. What was not verified — with **who has to answer it**, at the moment you
   decide not to run something.
4. What was fed back into the spec — clauses this work added, marked as
   *inferred during implementation* so planners know they may overturn them.

A memo whose last three sections are empty is correct and four lines long.
`## Not done` holds what was within reach and deliberately not taken, with
its grounds, in prose, because those are decisions rather than pending
claims.

**`## Not verified` is read by a machine, so it has one shape** — a
`| Item | Who must answer |` table, or alone the no-change block
`skills/settle/SKILL.md` *Rule changes* states, `- nothing` with its one
field `why:`. Any other spelling of the heading, the header row or the block
fails the check rather than reporting zero, because zero reads as "everything
has been closed". The template's placeholder row fails it too, until it is
filled in or the block replaces the table.

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
deleted file: the proofer reads the overview's diff, where a row that left
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
review round reads it (`docs/the-review-record.md` *The round record*).

A finding is a claim too, and it arrives from someone who did not write the
code. Open the coordinate and judge it yourself: fix what holds, and where it
does not, answer it in `round-N.md` with the grounds — the policy clause, the
original's behavior, the constraint that makes the state unreachable. What is
not allowed is the third path, changing the code to quiet a finding you do not
believe. A review the implementer cannot argue with is not a review, it is a
handoff of judgment.
Probes already run by a previous round (listed in `round-N.md`) are not
rebuilt — only re-checked for whether the finding is now fixed.

**A fix pass rewrites the `verdict:` line and writes the `answer:` line of
each open finding in `trail/rounds/round-N.md`, and writes no phase record** —
`docs/the-review-record.md` *The round record* names the three closing
verdicts. A `fixed` commit must touch a path the finding's `location:`
names; where the fix went somewhere else, the pass appends that coordinate
to the line and says so in `answer:`. The build's phases keep theirs.

A fix that changes what the work item ships brings the work item's
`changelog.md` along, because the release gathers that fragment as it stands;
`docs/the-record-layout.md` *A commit after the build brings its changelog
fragment along* owns that rule.

### 6. Drain the rows before the broad run, and keep the records

**The orchestrator moves every unresolved row out once the last round record
has no finding open, and before it runs `seal gate --preflight`**, whichever
party `routing.md`'s `Implementation` row names: the orchestrator opens the
pull request, and every commit after the broad run, a `seal/follow-up.md` row
among them, leaves `trail/gate.md` stale for the sealer
(`skills/code-review/orchestration.md` *Orchestrator: the pull request opens
once the sealer seals*). A row is out when it stands at its destination
below:

| Remaining item | Destination |
|---|---|
| Doable within this pull request | done now, by the party that builds the work item, and reviewed by a verifying round before the broad run |
| Waiting on prerequisite work | `seal/follow-up.md` |
| Needs a decision | An `add` in `frame/design.md`'s `## Rule changes` to the policy document's open-questions section |

Each finding that moves out reads `deferred <home>` in its round record. The
records themselves stay through the merge, and leave with their work item's
directory at the settle after its release.

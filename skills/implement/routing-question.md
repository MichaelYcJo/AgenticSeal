# implement, the routing question

The orchestrator opens this file on either of two conditions, and not
otherwise. The first is that it is about to put the batch of questions to a
person, the routing question among them. The second is that `config.json`
under the `seal/` root, read before the routing commit, lacks either of the
two language keys. `skills/implement/orchestration.md` holds the rest of
starting a work item, and its *What the answer writes* holds the rows of
the declaration.

## Orchestrator: why the routing question is asked once, at the start

**The routing question is one of the questions
`skills/implement/orchestration.md` *Orchestrator: what needs a person is
asked in one batch, before the first edit* has the
orchestrator ask in one batch before the first edit.** It is one decision
about where the work goes, and asking a part of it later is the mid-run
question the batch exists to remove. Opening a pull request is an
outward-facing act, not a detail that can wait for the end. Routing asked at
the start, the reviewer in the middle and the pull request at the end would
be three waits where one is due.

**Ask question 1 alone; the boxes in a second call only under `manual`.**
The orchestrator puts both. Question 1 goes in one call of its own, and
three of its four answers settle everything: under `agentic` the
orchestrator writes every row, `complete` writes every row, and `direct`
opens nothing, so under any of them the boxes mean nothing and are not
shown. The harness shows every question of a call at once, so boxes put
beside question 1 would be shown under the three answers they mean nothing
for. Under `manual` the second call follows the first at once, before the
first edit. `AskUserQuestion` allows at most four options per question, and
three presets beside the four boxes would be seven, which is why the shape
is two questions rather than one.

**The routing question is the orchestrator's, whether or not a framer runs.**
A subagent in this harness has no `AskUserQuestion` and no equivalent, so a
framer cannot ask. The one moment of human contact is here, before the first
edit, and the order does not change when a framer runs:

```
the orchestrator : ask question 1; the boxes only under manual
the orchestrator : write and commit routing.md
the framer       : read, judge, write design, plan and questions
the orchestrator : read plan.md against the issue, settle it with the framer, spawn the build
```

`agents/framer.md`'s rule *You ask nobody anything* is the other half of this,
and its `## Job` tells a framer that arrives to a missing `routing.md` to
report it rather than write one: a declaration written from a guess is a
recorded answer nobody gave.

## Question 1, the mode

A single-select question, put alone:

| Order | Label | Description |
|---|---|---|
| 1 | **agentic** | The orchestrator reads each work item's issue and the tree and chooses that item's route: which of the framer, `crafter` and `proofer` run, and whether the run may stop to ask you. Where it judges a change small enough, such as a two-line fix, it takes `direct` for it. It writes each choice down with its grounds, and you are not asked the route again. |
| 2 | **complete** | Every party runs: the framer frames it, `crafter` builds it, `proofer` reviews it, the orchestrator takes the broad run, the sealer audits it, and the pull request opens. **This is the last routing question: the run stops again only for what only you can decide and would be costly to undo.** |
| 3 | **manual** | You set each part: the four boxes below are the answer. |
| 4 | **direct** | This session writes the change itself: no agent, no work item, no frame, no review, no seal and no `routing.md`. Where the root is shared, every commit ends with the trailer `Seal-Routing: no work item`, and the pull request's check only lists those commits. |

**A label names no destination, and its description says what it turns
off.** A label that names a destination is read as what runs:
`straight to the PR` reads as *call no agents at all*, where that answer
turns off `proofer` alone. So each label names a mode, each description
says what its answer does, and the exit's description names every party and
record that does not run or is not written.

**The exit is last.** It is the least-verified path and one click, so it
sits where a reader's eye lands last, and its description states the cost.
It stays visible in use where the root is shared: every commit it covers,
whether the person chose it or the orchestrator chose it under `agentic`,
says `no work item` in its trailer, and the pull request's check prints
each one.

**Question 1 is put every time, whatever the ladder reads, and `agentic` is
the answer marked.** The person chooses the route, even for a typo fix, and
choosing `agentic` leaves each item's route to the orchestrator, which reads
the item on the ladder of `skills/implement/orchestration.md`
*Orchestrator: when a work item is required* among what it weighs (its
*Under agentic*). A mark read off the ladder
would mark `complete` for nearly every item, because nearly every change
alters observable behaviour and sits above its last rung. The mark is
` (Recommended)` after the label, and the options keep the order of the
table above, so the marked answer comes first and the exit stays last.

## Question 2, the boxes

A `multiSelect` question, asked only under `manual`.

**The order is the specification.** The first box is a property of the run;
the three below name parties, in the order they run. A reader meeting four
boxes of apparently the same kind reads the first as a fourth party to switch
on, and the separation is the cheapest defence against it. A list that
generates these carries the order.

| Order | Box | Checked | Not checked |
|---|---|---|---|
| 1 | **run end to end without stopping to ask** | the run goes from here to its destination and stops only for what only you can decide; `Automation` = `yes` | **this run may stop to ask**: somebody may be asked at minute thirty; `Automation` = `no` |
| 2 | **implement with `crafter`** | spawn the subagent; `Implementation` = `crafter` | **this session writes the code**; `Implementation` = `the session` |
| 3 | **review with `proofer`** | the review rounds run; `Review` = `through the review chain` | **nothing reviews this code before the pull request**; `Review` = `straight to the PR` |
| 4 | **open the pull request** | push it and open one; `Destination` = `open the pull request` | **the branch is handed back, committed and unpushed**; `Destination` = `stop before the pull request` |

**What is checked is the answer, and each box is a row of the declaration**,
which is why each box's description carries its unchecked meaning too: that
is the half a label cannot say. Box 1's unchecked half is the one most easily
misread: `no` says this run may stop to ask, never that a person did the work
by hand.

**The ceiling.** `AskUserQuestion` allows at most four options per question.
Question 1 and question 2 each sit at exactly four. **Both are fully spent:
a fifth answer or a fifth box breaks this shape.** Whoever adds an answer
to question 1 needs another shape for the routing question, and whoever
adds a box to question 2 needs a third question of boxes or a preset that
hides the axes.

## What each answer writes

Question 1's first three options and question 2's four boxes write the same
rows; what differs is who chose them and how many clicks it took.

**`complete` writes all four party rows at their checked values**, plus
`Automation` = `yes`. Ticking all four boxes under `manual` writes the same
rows. Under `agentic` the orchestrator writes the rows it chose for the
item.

## Orchestrator: a question in the batch names its answers

**A question in this batch names its answers, and every answer continues.**
"Should I release this?" and "should the proofer review it?" both have a `no`
that leads nowhere — the session that answers it is holding finished work with
no destination, which is a gate wearing the shape of a question. A yes/no is
the tell. Ask which of two named paths instead, and say what each one does.

## Orchestrator: the two language keys

**The two language keys join the batch wherever either is missing.** Before
the routing commit, the orchestrator reads `Commit and pull request
language` and `Record language` in `config.json` under the `seal/` root.
Where both stand, nothing is asked. Where either is absent in any of the
four ways `skills/commit-pr-convention/SKILL.md` *Every way of not naming a
language lands on English* names, the batch asks for both, as
`skills/implement/bootstrap.md` step 1 asks for them at first setup: the
recent titles from `gh pr list --state all --limit 10` stand beside the
question, and the language read from them is the option listed first. The
routing commit writes both keys into the file's object, each as
`"<key>": "<answer>"`. Where the batch reaches no person, because
the routing answer was given for the release and the run is unattended, the
orchestrator writes both keys as the language it reads the titles in, and
as `English` where the list gives none. `routing.md` *Why this way* then
says in one sentence that the two keys were written as a default taken
until answered, naming the language and what it was read from, and `pr.md`
quotes that sentence. A repository whose `config.json` predates the keys is
caught here, at its next work item, because `seal pr-body` refuses to
compose a body without them.

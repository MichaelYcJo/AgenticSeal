# Routing: 1792627930-the-section-sign-is-still-syntax

<!-- seal/specs/<unix-epoch-seconds>-<slug>/routing.md holds the answer the
orchestrator was given before the first edit, in the batch
`skills/implement/SKILL.md` *1. Read the spec before the code* has it ask.
The orchestrator commits it, and CI reads it at the pull request
(`skills/implement/orchestration.md` *Orchestrator: how the work is routed*).

It is the first file a work item gets, and below the SDD ladder it may be the
only one: a typo fix writes no `spec.md`, and this file is what gives the work
a place to exist.

Machines read the rows, and their vocabulary is fixed. Everything else in
this file is for people. -->

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | smith |
| Automation | yes |
| Answer pressed | automation |
| Branch | chore/1005-the-section-sign-is-still-syntax |

<!-- Review: `through the review chain` or `straight to the PR`. The first
     owes a committed `rounds/round-N.md` at the pull request. The second
     turns off the reviewer alone and owes the broad run's `broad-gate.md` in
     this directory at a ready pull request: the one broad run, at a SHA,
     against the base. Neither is no enforcement. A change belonging to no
     work item is question 1's `no work item` answer, recorded as
     `[no-review]` in front of each commit.
     Destination: `open the pull request` or `stop before the pull request`.
     Planning: `framer` or `the session`. Who draws the frame (`spec.md`,
     `plan.md` and `questions.md`): the `framer` subagent, or the
     orchestrator itself. OPTIONAL, on exactly the terms the `Implementation`
     row below has, and for its reasons.
     HOW TO ANSWER IT: nobody is asked. The ladder of
     `skills/implement/SKILL.md` *3. The SDD file set* decides whether a
     frame is drawn at all, so the orchestrator RECORDS here which way it
     went. The answer is written WITHOUT backticks, as below.
     Implementation: `smith` or `the session`. Who writes the code: the
     `smith` subagent, or the orchestrator itself. OPTIONAL: a declaration
     without this row is still a declaration, and the row reads as not
     answered. The orchestrator deletes the row rather than inventing a third
     answer.
     HOW TO ANSWER IT, by the criterion rather than by habit. The
     orchestrator asks whether this work is FINDING OUT or WRITING DOWN.
     Finding out (what an unfamiliar codebase does, where a behaviour lives,
     what an original actually did) is a STEP to send to `scribe`: a large
     input and a small output is what a subagent boundary is for. That is a
     step and not an answer to this row, which has two values and no third:
     the orchestrator that reads those facts back and writes the code still
     answers `the session`. Writing down stays with the orchestrator too,
     because a delegate re-buys the context the orchestrator already holds.
     The one case `smith` answers is a diff large enough to threaten what the
     orchestrator still has to hold. So the row is never deleted because the
     work is discovery: `the session` is the answer there, and the sentence
     above about deleting the row is for a work item that has no answer to
     give.
     The threshold in that last case is a number nobody has, and this comment
     does not invent one. What it can say is which axis it is on: the case
     for a delegate there is REPLACEABILITY, not cost, because the
     orchestrator is the single participant a release cannot replace
     mid-run. A cheaper delegate is not a reason.
     This row and the `Planning` row ship as PLACEHOLDERS while `Review` and
     `Destination` ship answered. A wrong answer in those two is caught at
     the next commit, because the gate stops recognising the file and goes
     back to asking. A wrong answer here is contradicted by nothing that can
     stop a commit: a confident `smith` nobody performed earns one printed
     line after a commit, and a confident `the session` earns nothing. So a
     file copied and never revisited lands on not answered rather than on a
     confident answer nobody gave. A backticked value reads as unanswered
     here, so the answer is written WITHOUT backticks.
     Automation: `yes` or `no`. Whether this run goes from here to its
     destination without stopping to ask. OPTIONAL, on the terms of the two
     rows above.
     HOW TO ANSWER IT: it is the one box in the routing question that names
     no party. The other three each switch a party on or off; this one says
     whether the run may come back with a question at minute thirty. `no` is
     NOT "a person did it by hand". It is "this run may stop to ask", and the
     first reading records a supervised run as a manual one.
     UNCHECKED IS A VALUE HERE, not an absence: a question that is asked
     always writes one of the two, so an absent row means nobody was asked.
     Writing `no` where the question was never put is the one mistake this
     row cannot survive, because the file is then byte-identical to one
     nobody read.
     WHAT HOLDS IT is `hooks/question-gate.py`. While the row reads `yes`, it
     refuses every question on this branch but the routing question put
     alone before the person has answered it in this session, so the run
     builds on the default a question states instead.
     Answer pressed: `automation` or `per axis`. WHICH answer the person
     pressed, not what it derived to. OPTIONAL, on the same terms.
     HOW TO ANSWER IT: `automation` where the person pressed the preset,
     `per axis` where the person ticked the boxes. The third answer,
     `no work item`, writes no file and so never reaches this row.
     Branch: one declaration per branch. Two is not an answer, and the gate
     reads it as none. -->

Answered 2026-10-22 by the repository owner, before the first edit: the owner pressed `automation` for #1005, on `release/v0.22.3` at a16acb40. Models: framer, smith, warden and sealer on Opus 5.5.

## Why this way

The section sign leaves the preloaded agent files, the contract's numbering and the readers' grammar, so a frame is drawn first. It is framed beside #988 and #1009, which touch 22 files that carry a section sign; the build starts once both have merged.

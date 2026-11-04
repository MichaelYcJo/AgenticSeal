# The run and its handoffs

The orchestrator's rules for the review chain's run and for what it hands
each agent; an agent opens the section its definition cites.

## The run

**A run ends with a verifying round.** It is spawned after the last fixes are committed, and a fix pass owes none only where each finding it closed is located in `seal/threads/<id>/` alone and its commits touched nothing else, as `docs/checks/the-pull-request-check.md` *What the check reads at the pull request* states; its target is the diff of those fixes, new units included; it
asks of every finding marked closed whether the fix holds, and says so on a
`confirms:` line where it holds, and where it does not on a finding's
`reopens:` line, or its `regression:` line where a fix pass's own commit
made the defect. A round opening nothing that needs a fix does not count
toward the cap: the cap stops a loop that is not converging, and such a
round is the loop having converged.
check: run-ends-with-verifying-round

**The orchestrator ends the rounds when they stop paying, and a run has three finding rounds by default, counted from the last design change, as the point where it weighs that rather than spawning the next round by habit.** A design change is a reframe, or a new phase the owner approved in `frame/plan.md`, so the first finding round that reviews new work starts the count again at one, whatever the record's number. The signals that a run is not converging, and what going on and stopping each cost, are `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*'s. A regression's fix pass is followed by one verifying round whatever the count, because no fix goes unread by a round, an invariant the table of `skills/core/SKILL.md` *Judgment is not licence to skip a party* holds. Every such decision, past the third round or at it, is a row of `frame/plan.md` *Judgments of the run* naming the counts weighed and this section; the proofer writes no line for it. When the orchestrator stops, every finding still open takes a home from the table below and reads `deferred <home>`. No person is asked mid-run.
check: tests/behaviour/test_chain_hooks_hardening.py

**A regression is routed by comparing the fix with the frame.** A
regression is a defect a fix pass's own commit introduced. Where a finding
stands in a unit a fix pass's own commits added or changed, and those
commits introduced its defect, the proofer writes its `regression:` line,
naming the finding whose fix made the unit
as `round-<N>#<n>`, or that round as `round-<N>` where no finding named the
unit, and names the unit first in the grounds. Then one sentence of the
grounds says what the frame says, from the phase's `frame/plan.md` row and
`frame/design.md`, what the fix did, and where the defect came from. No label
carries that sentence, and the orchestrator routes the round on it, at any
round of the run. Where the fix built what the frame says and the defect is
still there, the frame is wrong, and the round gets no fix pass: the work
item goes back to its framer, who writes
`Reframed <date> by <who>, after round <N>.` under the mark at the foot of
`frame/design.md`, and the run goes on with the redesign's build and its rounds.
Where the fix departed from the frame, or the defect came from how the fix
was written, a paste-ready fix taken from a review record among them, the
round gets an ordinary fix pass, and the crafter is told what the frame says.
A second regression on the same unit after a fix-pass route is the signal that the frame is wrong whatever the sentence reads, and the orchestrator routes it to the framer unless it can write, as the row's grounds in `frame/plan.md` *Judgments of the run*, why the frame holds and the fix alone was wrong. A defect in a unit a build phase made,
one the framer designed and the owner approved in `frame/plan.md`, is an ordinary
finding of new work, with no `regression:` line, even where the round that
finds it reads that phase. A close that does not hold where no fix pass's
commit made the defect, a `rejected` finding that holds after all or a
`fixed` commit that left the defect standing, in the unit that commit
changed or in another, is raised again as an ordinary finding with a
`reopens:` line naming it, and gets its fix pass.
check: tests/text/test_the_rules_have_one_owner.py

**A leftover finding goes where somebody will act on it, and the orchestrator writes why there.** The homes, with when each fits, are the rows below; the cheapest home that reaches a party who agreed to act is the one to take, a new issue is not the default, and the row the orchestrator writes in `frame/plan.md` *Judgments of the run* names the home and the party:

| Rung | When it fits | Where the finding goes |
|---|---|---|
| 1 | the branch owns the unit, or the crafter answers the finding with grounds | the diff, or the round record with the grounds |
| 2 | an open issue already owns the ground | a comment on that issue; the verdict reads `deferred #N` |
| 3 | the finding names a party who agreed to act on it | a new issue labelled `from-review`, or a `seal/follow-up.md` row where there is no tracker; the verdict reads `deferred #N` |
| 4 | it names nobody | the round record alone, and the pull request body |

**On a branch whose `routing.md` reads `Automation` `yes`, the
question tool is refused on every call.** The person who answered the
routing question was promised that nothing stops to ask, and a
question put at minute thirty waits for somebody who is not there.
The session builds on the default the question states, records that
default in the work item's `frame/questions.md` as one row, and names it in
the pull request body, where the owner can overturn it. The routing
question put alone goes through until this session has answered it
here, and what the gate reads and each case it lets through is
`hooks/question-gate.py`'s docstring. A session
sitting in a checkout whose branch is not the declared one is not
held, and neither is a question asked as plain text. A gate whose own
reason says to ask with the question tool meets this refusal too, and
its question states no default: the session takes none of the ways on
that question offers, and hands the stop back at the end of the run.
check: tests/hooks/test_question_gate.py

**The orchestrator's judgments of a run are rows of `frame/plan.md` *Judgments of the run*, each with its grounds and the document it stands on.** The decisions this section leaves to the orchestrator, to go on past the third round or to stop, a regression's route, a leftover's home, and a decision folded into the frame after the frame was committed, are judgments and not sequences, and `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* asks that each be written where the next session reads it. The settle's dry run prints the judgment rows of the released work items and, beside them, those earlier settles removed, which the history still holds. The settling session rewrites the section where one kind of judgment keeps costing rounds, in one release or across several, and deciding that two rows are one kind is its own judgment. The framer's judgments stand in its *Alternatives considered* and the proofer's in its findings, and neither is copied here.

## The handoff

**The orchestrator hands an agent coordinates, never prose.** A fact carries
the coordinate that makes it falsifiable — the line, the grep that returned
nothing, the test whose assertion constrains the wording — or is labelled
`executed`, `read` or `unverified`. An aggregate is not a coordinate
(`skills/agent-contract/SKILL.md` rule 5). A claim that flips on
where it is measured says where; a command with two forms names the one it
means and what the other is for; a runner the repository ships is named, not typed into every prompt, and the form handed over is the narrow one. A prompt that hands an agent a path outside the repository, such as the worktree it works in, says in the same prompt not to write that path into any record: an agent copies a prompt's paths into the records it writes, where `CONTRIBUTING.md` *House rules* forbids a real path and the `real_identifiers` census in `tests/censuses.py` refuses it.
check: tests/text/test_the_handoff_before_round_one.py

**While an agent runs, the orchestrator reads the age of its transcript at least every 30 minutes, and `frame/plan.md`'s Status column says which phase it has reached.** The implementer fills the Status column with the commit that closed each phase, so the orchestrator opens it rather than asking. A phase can run for an hour, so the stall signal is the time since the agent's transcript last changed, read through the link that the harness's task output is, with `stat -L`, because the link's own time is the moment it was made. Where the transcript has not moved for 30 minutes, the orchestrator reads the agent's slowest calls with `seal cost` on that transcript and the processes the agent started, and then decides whether to stop it. A completion notice is never waited on alone: an agent can end without one. An unattended run keeps its machine awake for its whole length, and a spawn prompt asks for a probe that may run past a minute as a background command, never as a foreground `&` followed by `wait`. After the run, `skills/verify/scripts/session_cost.py` reads the transcript.
check: tests/text/test_the_handoff_before_round_one.py

### The per-segment bars

**A segment is judged against its kind**, and the bar is a lens for rounds of
ordinary size, never a refusal threshold: no gate fails a round on it.

| Segment | Judged on | Grounds |
|---|---|---|
| reviewing | tools per turn **≥ 1.8** | a review's reads are independent, so they go out together |
| framing | tools per turn **≥ 1.4** | a frame is a wide read of independent documents |
| implementing | **`repeats = 0`** and calls per deliverable, never tools per turn | an edit-test loop is serial; a command re-run unchanged is the waste |
| verifying | exempt | it answers a diff's closed findings, which leaves few independent axes |

`--segments` applies the bars above by kind: each row is joined to a spawn,
and the spawn's `subagent_type` names the kind; a row with no kind is not
graded, and is counted as ungraded. `session_cost.py` prints its batching
advisory below 1.2 and stays there, because the plain reading cannot tell a
reviewer's transcript from an edit-test loop.

The bars judge a segment against its kind; the run-level table judges a run
against the last run measured. The table asks what the whole run cost, and
its rows are `skills/verify/orchestration.md` *Measure the segment, and
feed the flow log*'s; it is not a destination of its own.
check: tests/text/test_the_handoff_before_round_one.py

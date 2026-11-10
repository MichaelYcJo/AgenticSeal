# The run and its handoffs

The orchestrator's rules for the review chain's run and for what it hands
each agent; an agent opens the section its definition cites.

## The run

**A run ends with a verifying round.** It is spawned after the last fixes are committed, and a fix pass owes none only where each finding it closed is located in `seal/threads/<id>/` alone and its commits touched nothing else, as `docs/checks/the-pull-request-check.md` *What the check reads at the pull request* states. It answers every finding the round before closed, on the lines `skills/code-review/SKILL.md` *Earlier rounds* defines. A round opening nothing that needs a fix does not count toward the three finding rounds, which mark where the orchestrator weighs a loop that is not converging and are no cap: such a round is the loop having converged.
check: run-ends-with-verifying-round

**The orchestrator ends the rounds when they stop paying, and a run has three finding rounds by default, counted from the last design change, as the point where it weighs that rather than spawning the next round by habit.** A design change is a reframe, or a new phase the owner approved in `frame/plan.md`, so the first finding round that reviews new work starts the count again at one, whatever the record's number. The signals the orchestrator weighs at that point, and the routes of a regression, are `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*'s. A regression's fix pass is followed by one verifying round whatever the count, because no fix goes unread by a round, an invariant the table of `skills/core/SKILL.md` *Judgment is not licence to skip a party* holds. Every such decision, past the third round or at it, is a row of `frame/plan.md` *Judgments of the run* naming the counts weighed and this section; the proofer writes no line for it. When the orchestrator stops, every finding still open takes a home from the table below and reads `deferred <home>`. These decisions are the orchestrator's, and the orchestrator asks no person to make them.
check: tests/behaviour/test_chain_hooks_hardening.py

**A regression is routed by comparing the fix with the frame.** A
regression is a defect a fix pass's own commit introduced. The grounds of
its finding carry the comparison, as `skills/code-review/SKILL.md` *Earlier
rounds* states, and the orchestrator routes the round on it. A work item
the route sends back to its framer gets
`Reframed <date> by <who>, after round <N>.` under the mark at the foot of
`frame/design.md`, written by that framer, and the run goes on with the
redesign's build and its rounds.
check: tests/text/test_the_rules_have_one_owner.py

**A leftover finding goes where somebody will act on it, and the orchestrator writes why there.** The homes, with when each fits, are the rows below; the cheapest home that reaches a party who agreed to act is the one to take, and a new issue is not the default. The row the orchestrator writes in `frame/plan.md` *Judgments of the run* names the home and the party:

| Rung | When it fits | Where the finding goes |
|---|---|---|
| 1 | the branch owns the unit, or the crafter answers the finding with grounds | the diff, or the round record with the grounds |
| 2 | an open issue already owns the ground | a comment on that issue; the verdict reads `deferred #N` |
| 3 | the finding names a party who agreed to act on it | a new issue labelled `from-review`, or a `seal/follow-up.md` row where there is no tracker; the verdict reads `deferred #N` |
| 4 | it names nobody | the round record alone, and the pull request body |

**On a run whose `routing.md` reads `Automation` `yes`, the orchestrator
does not stop the run with a question that the tree or the framer can
answer.** The person who answered the routing question was told that the
run would stop only for what only they can decide, or answered
`agentic` and left the `Automation` row to the
orchestrator, which wrote `yes` because it foresaw no such question.
Either way, a question put at minute thirty waits for somebody who may
not be there. Where a question
arises, the orchestrator looks for its answer in the tree and in the work
item's `frame/questions.md` first. Where neither answers it, the orchestrator
proceeds on the default the question states, writes that default as one
row of `frame/questions.md`, and quotes that row in the work item's
`pr.md`, which the pull request body's first part holds, after
`pr.<lang>.md` where the two language keys differ, where the owner can
overturn it. The orchestrator keeps a blocking question for what only the
owner can decide, and only where proceeding on a default would be costly to undo or
would reach outside the repository. A question or a remark the owner raises
during the run is taken up when it arrives: the framer folds it into the
frame, or it goes into the code, and it is never deferred to the pull
request body.

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

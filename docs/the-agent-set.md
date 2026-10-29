# The agent set

A work item is built by more than one party. This document is the standing
account of how the rules are split between them, what each one is allowed to
write, and what it costs to spawn one.

## One contract every agent receives, and one definition each

**The rules true of every agent live in one file every agent receives before
its first tool call, without a prompt asking for it.** A rule kept only in
whoever last wrote a spawn prompt goes missing without a trace, and a round
that runs without it leaves nothing saying so.

**A rule that would need a per-role exception is not universal.** That is the
test the shared file applies to itself: what is true of every agent is
shared, what is one agent's own is in that agent's definition, and an agent
whose definition is silent about an act does not take it.

**The contract's rule numbers are stable.** A prompt saying *contract rule 3
is narrowed this round*, and a round record compared with another months
later, hold only while the number still means what it meant; how a retired
rule keeps its number is the contract's own preamble.
check: tests/text/test_every_agent_reads_the_contract.py

**The agents are the framer, the crafter, the proofer, the sealer and the
tracer, and each name says its part of one order.** The framer designs the
work, the crafter builds it, the proofer finds its defects, the sealer gives
the final guarantee and seals it, and the tracer, outside that order, traces
what an original codebase does for a migration. The crafter is named for the
Software Craftsmanship movement, and the proofer for the proof impression a
seal maker strikes to find a defect before the seal is used. An agent's name
is its definition's file name under `agents/` and the word every spawn, mark
and record uses for it, so a rename is a `git mv` of the definition and of
every text that names it, in one release.
check: tests/censuses.py

**The party that draws a contract is not the party that executes it.** A
specification written by whoever then builds against it stops being a
contract and becomes an account of what got built, which leaves the review's
first stage comparing the work with its own description of itself. So the
frame, what the work is, how it is phased and what only a person can decide,
is drawn by one agent, and the building is another's. The builder's first act
on a drawing is to say whether it holds, because a drawing can be wrong about
the tree it describes and the cheapest moment to find out is before anything
is spent. The readiness and decomposition questions belong to the frame,
because they are about work nobody has started. So does a question whose
answer is a behaviour, a time or an output a read-only command gives: the
framer runs that probe outside the tree before it writes anything down, and
only a question no probe can run in its environment reaches the build as a
row.
check: agents/framer.md evals/behaviour/framer/rule-framer-sharp-s/

**A subagent cannot ask anybody anything.** No question-asking tool reaches
an agent this plugin spawns, so a framer meeting a missing routing
declaration reports it rather than writing one, and the question is put by
the session that spawns the work, before the first edit.
check: tests/skills/test_chain_check.py

## What each party writes, and when

**A review round is one file the proofer writes, the fix pass writes two lines
of each finding it answers, the orchestrator's broad run writes
`trail/gate.md`, and the sealer's verdict is `guarantee.md` at the thread's
top.**
`docs/the-review-record.md` holds what each of those files carries.
check: tests/skills/test_chain_check.py

No case runs the tracer. That a spawn opens `legacy-parity` first, returns
facts and no verdict, and returns `original not found` where the original
does not resolve is read from `agents/tracer.md`, not observed.

**The last party audits the others, and is independent of them.** The
sealer's reference is the issue body and the tree, so the orchestrator's
part of a pull request body, a phase record or a review verdict that says
what the tree does not is caught by a party that wrote none of them. It
re-judges neither the frame nor the code's quality, which stay the framer's
and the proofer's, and it runs on Opus, the level of the agents it audits.
`docs/the-review-record.md` *The guarantee* holds the rule.
check: tests/behaviour/test_the_sealer_guarantees.py

**A build phase leaves a record, the way a review round does.** What a phase
discovers reaches the next phase only if somebody retypes it into the next
spawn prompt. So a phase writes what it was asked and what building it found
that the next phase needs, beside the plan whose Status cell carries the
commit. *What this phase was asked* is the scope the spawn gave, which a
later reader cannot otherwise tell from a scope the phase invented. What a
work item removes is named once, in the frame's `## Removes`
(`templates/records/sdd-design.md`), which the review reads against the diff, and a
removal the frame did not name is a divergence in `gaps.md`.
check: tests/behaviour/test_a_phase_hands_the_next_one_a_record.py

**A document that describes a transition is deleted when the transition is
over, and its standing rules move first.** A file whose last instruction is
*delete this when the boxes are ticked* keeps being read as current after it
stops being, and every sentence in it borrows the authority of the sentences
still true. The rules that survive move into the documents that own their
subjects, with the cases that pin them, because a case deleted with its
document is coverage nobody decided to give up.
check: none reader: review

**What an agent leaves in the scratchpad is named for the work item it
serves, so two agents alive at once cannot pick the same name.** Every agent
of one session shares one scratchpad, and a name any parallel agent would
also pick is a file somebody else can overwrite. So the proofer's clone is
`<scratchpad>/<work-item-id>/round-<n>/clone` with every probe of the round
beside it, and the orchestrator's `seal gate` log carries the work item id.
The name lives in the definitions, where a rule arrives by mechanism, and one
directory per work item and round is what lets the agent that made a leaving
say every one of them is gone.
check: tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py

## What a spawn costs

**A spawn's payload is measurable, and it is paid on every spawn.** An
agent's definition, every skill its own list injects and the instruction
files the harness adds are written into the context of every segment that
agent runs, whether or not the segment has an act to apply them to. The meter
resolves a definition's list to files and reports the composition per file
and as a total, in bytes, characters and tokens, split at headings.

**A section marked for one role reaches that role and no other.** An
orchestrator's procedure preloaded into every implementer spawn is procedure
for asking a person a question, delivered to a party that cannot ask anybody
anything, and paid once per spawn.
check: tests/skills/test_payload_meter.py tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py

**The orchestrator's acts are counted, each against what delivers it.** An
agent's rules arrive by mechanism, while the orchestrator has no spawn for a
preload to attach to, so each of its acts is a sentence until something
refuses when the act did not happen. `skills/implement/orchestration.md`
tables every `##` heading carrying the `Orchestrator:` marker in
`skills/implement/orchestration.md`, `skills/implement/bootstrap.md` and
`skills/code-review/orchestration.md`, and every `###` directly beneath one,
against its delivery: a command, a check, part of its parent's act, or a
sentence with its grounds. A test holds the table against the three files
from both sides. It reads the marker and not the meaning, so an act written
outside a marked section is counted by nobody.
check: tests/behaviour/test_every_orchestrator_act_names_its_delivery.py

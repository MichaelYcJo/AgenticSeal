# implement, the fix pass

A fix pass opens this file before it judges the first finding of a round
record, and nothing else opens it. A fix pass is the crafter's or the
orchestrator's. The crafter opens this file at step 9 of
`agents/crafter.md`. The orchestrator opens it from
`skills/implement/SKILL.md` *5. Incorporate review — read the round records
first*, and makes every fix pass where `routing.md` answers
`Implementation` with `the session`. `skills/code-review/orchestration.md`
*Orchestrator: a phase is a fresh crafter, and a fix pass resumes the
implementer* holds the orchestrator's half: who runs the pass, what it is
handed, and the commit of the round record after it. Where this file has a
crafter's hand-back name something for the orchestrator, the orchestrator
in its own pass acts on it at the point the pass meets it, by the step of
its own procedure that acts on that hand-back. So where its pass meets the
stop of *A fix that needs a unit the frame does not name waits for the
fold*, the orchestrator sends the finding to the framer before the pass
that builds the unit.

## Read the round records first

A fix pass starts at `seal/threads/<work-item-id>/trail/rounds/`,
**not** at the inline comments: the proofer writes `round-N.md`, and the next
review round reads it (`docs/forms/the-round-record.md` *The round record*).

A finding is a claim too, and it arrives from someone who did not write the
code. The fix pass opens the coordinate and judges it itself: it fixes what
holds, and where it does not, answers it in `round-N.md` with the grounds —
the policy clause, the original's behavior, the constraint that makes the
state unreachable. What is not allowed is the third path, changing the code
to quiet a finding the pass does not believe. A review the implementer
cannot argue with is not a review, it is a handoff of judgment.
Probes already run by a previous round (listed in `round-N.md`) are not
rebuilt — only re-checked for whether the finding is now fixed.

## A paste-ready fix is read before it is applied

A paste-ready fix is the proofer's claim and not the fix, and a spawn
prompt or a judgment row that tells the fix pass to apply it names the fix
without waiving the reading below. The fix pass applies it only after
reading it against the frame and the code: what `frame/design.md` and the
`frame/plan.md` row of the phase that built it say the changed unit does,
and every input the code hands that unit. A procedure step is also read as
its own reader would: in either `seal/` root (contract rule 11), under
every condition its file names, and in the release that ships it. In that
release, a section the step cites holds the text the release ships, not the
text a design's `## Rule changes` writes at a later settle. A paste-ready
fix that writes a count or a universal contract rule 19 refuses fails that
reading too. Where that reading fails, the fix pass writes the fix in its
own words and says so in `answer:`.

## A fix that needs a unit the frame does not name waits for the fold

**A fix that needs a unit the frame does not name is built only once the
framer's fold has designed the unit.** A unit the fix pass designs and
builds in one act reaches the next round with no judge but its builder,
and `skills/core/SKILL.md` *Each agent judges its own target, independently
of the others* gives the framer what the work should be.

A unit is a new name or path that the frame holds nowhere: a file or a
directory; a function, a class, a type or a module-level name, private
helpers among them; a hook's entry; a `seal` subcommand or flag; a
configuration key; a field of a record's form; or a heading of a skill, a
document or a template. A name or path is new where the tree at the
round's `target:` holds no part by it. The frame holds a unit where
`frame/design.md` *Scope* or *Data & interfaces*, or the `frame/plan.md`
row of the phase that built the code, writes the unit's name or path. A
helper whose job the frame states, but whose name the frame does not hold,
is a unit.

Two kinds of change add no unit. One is a change to the body of a part the
tree already holds, whether or not the frame names the part, such as a
branch added to a function or a sentence added to a section. The other is
a part only the tests read, such as a test module, or a helper, a fixture
or a constant in one. So a fix that writes a helper's code into an existing
body is not stopped: that is the stop's stated limit, and the round after
reads such a fix as it reads any fix.

Where a finding's fix needs a unit the frame does not hold, a paste-ready
fix's among them, the fix pass builds no part of that fix and writes no
close block for the finding, which stays open. It fixes the other
findings. Its hand-back names the finding, the unit's name or path, and
why neither `frame/design.md` *Scope*, nor its *Data & interfaces*, nor
the phase's `frame/plan.md` row holds it. Once
the orchestrator has committed the framer's fold, the fix pass that
follows builds the unit to the fold's design and closes the finding, and
its `answer:` names the *Scope* item the fold added. Where the framer
rejects the decision, the fix pass that follows answers the finding by the
route the orchestrator's row of `frame/plan.md` *Judgments of the run*
gives it, and its `answer:` names that row.
check: tests/text/test_the_rules_have_one_owner.py

## The narrow set, then the read of the range

Once the fixes are committed, the fix pass runs the set the *Review rounds
1..n* row of `skills/verify/SKILL.md` *Scope: cheap and often, broad and
once* names, as one command through the repository's runner.

**Then whoever makes the pass, the crafter or the orchestrator, makes the
reading `agents/crafter.md` *Before you hand back, your range and the work
item's records are read whole against HEAD* asks for.** The orchestrator
makes every fix pass where `routing.md` answers `Implementation` with
`the session`, and in every route it makes the fix it writes after the
last round, which `skills/code-review/orchestration.md` *Orchestrator: a
phase is a fresh crafter, and a fix pass resumes the implementer* gives
it. In the orchestrator's pass, that rule's *Job* stands for what the
orchestrator writes in a fix pass. In its fix commits it corrects every
statement HEAD contradicts in its range, in `gaps.md` and in
`changelog.md`. A statement HEAD contradicts in `routing.md` or a frame
file, it folds as it folds one a crafter's hand-back names, in a commit of
its own before it appends the close blocks, as
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket* states. That rule's hand-back stands for the close blocks. The
method of the read, each statement across the tree the read leaves
standing with why, and where the part a sample did not reach stands go
into the `answer:` of the close block of the finding they concern, and
otherwise into the `answer:` of the last close block the pass appends.
Where the pass appends no close block, because no finding names its fix,
they go into `gaps.md` `## Not done`. What the pass did not finish goes to
`gaps.md` `## Not done` too.
check: tests/text/test_a_moved_rule_leaves_its_definition.py

## The close blocks, last

**A fix pass appends close blocks and writes no phase record.** It appends
one close block per finding it answers, the `seal` block
`templates/records/sdd-round.md` places in the finding's section after its
paste-ready fix, each line spelt as `lib/fields.py` reads it. Two
paragraphs of the form state what the block holds, and the fix pass reads
both before it writes the first block: `docs/forms/the-round-record.md` *A
finding's `verdict:` decides it, and severity is for people* gives the
values its `verdict:` takes, and `docs/forms/the-round-record.md` *The fix
pass appends one close block per finding and edits nothing else in the
file* gives when the block carries a `location:` line of its own. Its
`answer:` says what was done. Where a finding's `evidence:` line names the
command that lists each place stating a fact, as
`skills/code-review/SKILL.md` *A paste-ready fix reaches every statement of
the fact it repairs, or names where it stops* asks, the fix pass runs it
again after its last fix commit, and the close block's `answer:` names each
place it still prints with why that place stands, or says that it prints
none.
The pass edits nothing else in the record: the finding's own block is the
proofer's (`docs/forms/the-round-record.md` *The round record*). The
build's phases keep their records.
Last, after its last fix commit and its corrections, the fix pass appends
the close block of every finding it answered, and commits none of them:
the orchestrator commits the round record as the pass left it.
check: tests/text/test_a_moved_rule_leaves_its_definition.py

## The changelog fragment comes along

A fix that changes what the work item ships brings the work item's
`changelog.md` along, because the release note is built from that fragment as
it stands at the tag;
`docs/layout/the-record-layout.md` *A commit after the build brings its changelog
fragment along* owns that rule.

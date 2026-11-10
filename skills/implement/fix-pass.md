# implement, the fix pass

A fix pass opens this file before it judges the first finding of a round
record, and nothing else opens it. The crafter opens it at step 9 of
`agents/crafter.md`, and a session that fixes review feedback opens it from
`skills/implement/SKILL.md` *5. Incorporate review — read the round records
first*. `skills/code-review/orchestration.md` *Orchestrator: a phase is a
fresh crafter, and a fix pass resumes the implementer* holds the
orchestrator's half: who runs the pass, what it is handed, and the commit
of the round record after it.

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
text a design's `## Rule changes` writes at a later settle. Where that
reading fails, the fix pass writes the fix in its own words and says so in
`answer:`.

## The narrow set, then the read of the range

Once the fixes are committed, the fix pass runs the set the *Review rounds
1..n* row of `skills/verify/SKILL.md` *Scope: cheap and often, broad and
once* names, as one command through the repository's runner. A crafter
then makes the reading `agents/crafter.md` *Before you hand back, your
range and the work item's records are read whole against HEAD* asks for.

## The close blocks, last

**A fix pass appends close blocks and writes no phase record.** It appends
one close block per finding it answers, the `seal` block
`templates/records/sdd-round.md` places in the finding's section after its
paste-ready fix, each line spelt as `lib/fields.py` reads it. The values its
`verdict:` takes are stated in `docs/forms/the-round-record.md` *A
finding's `verdict:` decides it, and severity is for people*, and when it
carries a `location:` line of its own in `docs/forms/the-round-record.md`
*The fix pass appends one close block per finding and edits nothing else in
the file*; the fix pass reads both paragraphs before it writes the first
block. Its `answer:` says what was done.
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

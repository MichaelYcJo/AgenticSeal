# What a review round leaves

The proofer writes this record, the crafter closes its findings, and
`skills/code-review/scripts/chain_check.py` reads it at the pull request.

## The round record

**A round is one file the proofer writes.** `seal/threads/<id>/trail/rounds/round-N.md`,
from `templates/records/sdd-round.md`, in the branch worktree under review: a `seal` block holding its `target:` line, then `## Findings` with one `### <n>. <symptom>` section per finding, `## Confirmations` where the round confirmed something, `## Not judged` and `## Probes`. A finding holds one `seal` block of its fields, why it matters with its grounds, the paste-ready fix in a fenced block, and, once it is closed, its close block. The record is written in words, and no
emoji stands anywhere in it. No report file stands beside it and nothing
generates, copies or derives any part of it.
check: tests/skills/test_chain_check.py tests/text/test_the_record_is_written_in_words.py

**The record's fields stand in `seal` blocks, and `hooks/lib/fields.py` is the one spelling of their grammar.** A `seal` block is a fenced block opened by a line of three backticks and `seal`, with nothing before or after them, outside every other fence. The first line of a block names its kind. `target:` opens the round's one block, which stands outside every finding and holds at most one `original:` line. `severity:` opens a finding's one block, which stands in the finding's `### <n>. <symptom>` section with its `location:` and `evidence:` lines and at most one of a `regression:` and a `reopens:` line. `verdict:` opens a finding's close block, at most one in its section, with its `answer:` line and a `location:` line where the fix went to a path the finding does not name. `confirms:` opens a confirmation's block outside every finding. Every line of a block is a field its kind takes, written `<key>: <value>` with the key exactly as the module spells it and the value matching the key's shape whole; a line that is not, a key over its count and a blank line are refused at their line, and the block is not read past it. Nothing outside a block is a field: a line shaped like one in prose decides nothing and is named by nothing, and where a field is owed its absence is refused. A finding with no close block is open. The record holds one `## Findings` heading, under which each `### <n>. <symptom>` heading opens a finding, and no two findings share a number. No `Record language` translates a key, a value's fixed words or the info string. A list of the ways a label is written grows by one row for every near miss a round finds and never converges, and a block leaves a reader nothing to guess: inside it every line is the form, and outside it none is (`skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*).
check: tests/skills/test_chain_check.py

**A finding's `verdict:` decides it, and severity is for people.** A finding with no close block is open; the fix pass's close block answers it with `fixed <commit>`, `rejected` (the finding does not hold, and `answer:` says why) or `deferred <home>`. `severity:` is `must` (fix before merge) or `should`
(fix, or say why not); no script decides on the word, and the agents judge
it. What this round confirmed holds is a `confirms:` entry of
`## Confirmations`, and what it could not judge a row of `## Not judged`
with who answers it; neither is a finding. A wrong sentence an agent reads and acts on is `should`, and so is a wrong line of a work item's own record that a script reads or copies: a line the check reads, a row `seal unverified` reads, or a line `seal pr-body` copies into the pull request body. A sentence of a record that restates another record's fact and has drifted from it is a finding, answered by removing the copy and citing the home, never by correcting the copy; one that has not drifted is no finding, since no template holds a place for a copy (`docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/*). A sentence in a record that merely reads badly is not a finding.
check: tests/skills/test_chain_check.py

**A finding's `location:` names where the defect shows, and a `fixed` commit
touches it.** Its coordinates are each place the defect shows, and the file
its paste-ready fix changes where that is elsewhere, each path from the
root. A line the check cannot read is refused whatever the verdict. A
`fixed <commit>` changes at least one named path, or a path under one;
whether a fix that touched one of three is complete is the verifying round's
to judge. It errs where a commit touches a named path and fixes nothing,
which the verifying round reads.
check: location-touched-by-fix

**A finding's `evidence:` line names what its claim rests on.** `executed`
names each command the round ran for it, and `read` each `path:line` it
opened, so a later reader repeats the act instead of trusting the prose. A
claim resting on neither is no finding but a row of `## Not judged`. No
script decides on the line: the check takes it in any words, or a finding
without it, and `seal pr-body` copies it with its block.
check: tests/skills/test_chain_check.py

**A claim of absence is `executed` only.** A finding that says something is
missing, that nothing catches, calls or states it, names the search that
found nothing, because no coordinate opened can show an absence. The
proofer who writes the line and the round that reads it judge whether a
claim is one of absence.

**A later round re-runs an `executed` line rather than re-deriving the
claim.** Where it weighs an earlier finding, it runs the commands the line
names again. A probe the line names was deleted under the agent contract's
probe rule, so the round writes it again from its `## Probes` row. The sealer weighs no finding: a finding's verdict is the
check's to read (`agents/sealer.md` step 3).
check: tests/text/test_review_axes.py

**The fix pass appends one close block per finding and edits nothing else in the file.** The block stands in the finding's section, after its paste-ready fix, and holds its `verdict:` line, with the commit for `fixed`, and its `answer:` line: what was done, why the finding does not hold, or where it went. Where its fix went to a path the finding's `location:` does not name, the close block carries a `location:` line naming it, and its answer says so. The finding's own block is the proofer's and is never edited.
A repair a commit made, a correction to a record among them, closes
`fixed <commit>`, with the record's path on `location:`. A repair made
outside the tree, an issue or a pull request body edited, makes no commit
on the branch and closes `deferred <where it was repaired>`, such as
`deferred #<issue>`, with `answer:` saying what changed there; it owes the next
round nothing. `rejected` means only that the finding does not hold.
check: fix-pass-two-lines

**Each round answers to the next by reference.** A reference names an
earlier record by its number and one of its findings by the finding's
heading number, or, for a round's fix pass that no finding named, the
record alone; the table's rows say which line takes which. A round names an
earlier finding by one of three relations, each its own line: `confirms:`
where its close holds; `reopens:` on a new finding where the close does not
hold and no fix pass's commit made the defect; `regression:` on a new
finding where a fix pass's own commit introduced it. A `reopens:` line
names a finding, since a fix pass no finding named closed nothing to
reopen. A claim of the frame or the build that matched, with no earlier
finding to name, is prose under `## Confirmations` and holds no block.
Every finding of round N at `fixed <commit>` or `rejected` is named by a
`confirms:`, a `reopens:` or a `regression:` line of round N+1, and one
left unnamed is refused at its own heading in round N's record; a
`deferred <home>` finding owes nothing. Round 1 has no earlier record, so
it writes no `confirms:`, `reopens:` or `regression:` line. A round with
nothing to confirm leaves `## Confirmations` out.
check: tests/skills/test_chain_check.py

**Every round file stays, so a finding can be followed from the round that
found it to the commit that closed it.** The next round's proofer reads the
earlier records directly; nothing summarises them. They leave with their
work item's directory, which the settle after its release removes.
check: tests/skills/test_settle.py

**`target:` names a commit, not a content anchor, because a round records a
moment.** The record's one `target:` line names the reviewed commit, with
the base a round that read the branch read it against, or the fix range a
verifying round read. A squash orphans the commit after the merge, and the
check reads it only while the branch that holds it is open.
check: tests/skills/test_chain_check.py

**Each finding's close block has one writer, and the blocks written at one step reach the branch in a single commit.** A finding a fix pass answers is the pass's to close: it writes the close block last, after
its fix commits and the corrections its sweep made, because a `fixed`
verdict names a commit that is already there, and it commits neither. The
orchestrator takes the round record from the hand-back as it stands and
commits it, once for the whole pass, before it spawns the verifying round,
which can read only what a commit holds. It edits no line in that commit,
and a close it doubts goes into that round's spawn prompt. A finding closed
with no fix pass, such as `deferred the frame` on the framer's route or a
`deferred <home>` the orchestrator files at the cap, has the orchestrator
as its writer, and the orchestrator writes and commits the close block of every finding it closes at that step together. A second hand on a close block gives a reader nothing: made before the orchestrator's commit it leaves no trace
in the history, and made after it the round pays one more record commit.
check: tests/text/test_the_rules_have_one_owner.py tests/text/test_a_moved_rule_leaves_its_definition.py

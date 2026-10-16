# The review record

What one review round leaves in the tree, what the check at the pull request
reads of it, and the rules the run around the rounds keeps. The orchestrator's
acts are `skills/code-review/orchestration.md`'s; this document is what they
produce and what holds them.

## The round record

**A round is one file the warden writes.** `seal/specs/<id>/rounds/round-N.md`,
from `templates/sdd-round.md`, in the branch worktree under review: `Target
SHA`, then `## Findings` with one `### <n>. <symptom>` section per finding,
`## Confirmations`, `## Not judged` and `## Probes`. A finding holds its
`severity:`, `location:` and `verdict:` lines, a `refixes:` line where it
applies, why it matters with its grounds, the paste-ready fix in a fenced
block, and its `answer:` line. The record is written in words, and no emoji
stands anywhere in it. No report file stands beside it and nothing
generates, copies or derives any part of it.
Enforced by: tests/test_chain_check.py::TestFindings::test_the_template_is_the_record_the_check_reads

**Every label is one lowercase word at the start of its line, and no other
spelling is read.** The five are `severity:`, `location:`, `verdict:`,
`refixes:` and `answer:`, each followed by one space, with no emphasis. A
line that means one of them, or the old `fix of a fix`, and is spelt another
way — `VERDICT:`, `**verdict:**`, `verdict :` — is refused at its line, and
the finding carrying it is not read past it, so a finding holding both
spellings does not pass on the lowercase one.
Enforced by: tests/test_chain_check.py::TestFindings::test_a_label_in_another_spelling_is_refused_by_line

**A finding's `verdict:` reads one of four values, and severity is for
people.** The warden writes `open`; the fix pass answers with
`fixed <commit>`, `answered` or `deferred <home>`. `severity:` reads `must`
(fix before merge) or `should` (fix, or say why not), and no check reads
it. What this round confirmed holds is a row of `## Confirmations`, and what
it could not judge a row of `## Not judged` with who answers it; neither is
a finding. A wrong sentence an agent reads and acts on is `should`; a
sentence in a record that merely reads badly is not a finding.
Enforced by: tests/test_chain_check.py::TestVerdictOf::test_the_four_values_read_and_nothing_else_does

**A finding's `location:` names where the defect shows, and a `fixed` commit
touches it.** A finding's one such line lists a backticked coordinate for
each place the defect shows, and for the file its paste-ready fix changes
where that is elsewhere, joined by `, `; a coordinate is `path`,
`path:line` or `path:first-last`, the path from the root. A line the check
cannot read is refused whatever the verdict. A `fixed <commit>` changes at
least one named path, or a path under one; whether a fix that touched one of
three is complete is the verifying round's to judge. It errs where a commit
touches a named path and fixes nothing, which the verifying round reads.
Enforced by: tests/test_chain_check.py::TestLocationOf::test_one_or_more_backticked_coordinates_read_and_nothing_else_does, tests/test_chain_check.py::TestMain::test_a_fixed_commit_that_touches_nothing_of_the_finding_is_refused

**The fix pass writes two lines per finding and nothing else in the file.**
It rewrites the finding's `verdict:` line, with the commit for `fixed`, and
writes its `answer:` line: what was done, why the finding does not hold, or
where it went. Where its fix went to a path `location:` does not name, it
appends that coordinate to the line, joined by `, `, and its answer says so.
A correction to a record, or a repair made outside the tree, produced no
commit on the branch and closes `answered` with where the repair is.
Enforced by: tests/test_chain_check.py::TestMain::test_a_fixed_commit_that_touches_nothing_of_the_finding_is_refused

**Each round answers to the next by reference.** A reference is
`round-<N>#<n>`, the earlier record's number and the finding's heading
number, or `round-<N>` for a round's fix pass that no finding named. The
`Confirms` cell, the first column of `## Confirmations`, reads
`round-<N>#<n>` or `none`; a `refixes:` line reads a reference. Every
finding of round N at `fixed <commit>` or `answered` is named by a
`Confirms` cell or a `refixes:` line of round N+1, and a `deferred <home>`
finding owes nothing. Round 1 has no earlier record, so its cells read
`none`.
Enforced by: tests/test_chain_check.py::TestReferenceOf::test_a_round_and_a_finding_read_and_nothing_else_does, tests/test_chain_check.py::TestChannel::test_every_fixed_or_answered_finding_is_confirmed_or_refixed_by_the_next_round

**Every round file stays, so a finding can be followed from the round that
found it to the commit that closed it.** The next round's warden reads the
earlier records directly; nothing summarises them. `settle --retire-process`
removes them after the release that ships the work item, when no round is
left to read them.
Enforced by: tests/test_settle_retires_the_process_record.py::test_the_process_record_leaves_and_the_sdd_set_stays

**`Target SHA` names a commit, not a content anchor, because a round records a
moment.** The first SHA in the row is the reviewed commit; a verifying round
writes `<sha>, fixes <a>..<b>`. A squash orphans the commit after the merge,
and the check reads it only while the branch that holds it is open.
Enforced by: tests/test_chain_check.py::TestFollows

## What the check reads at the pull request

**`chain_check.py` reads the declaration, the frame, the records, the broad
gate's file and the sealer's guarantee, and nothing else of a round record.** It judges the
`routing.md` naming the pull request's branch and every one its own commits
add or change. A ready pull request fails on any refusal, each named
`path:line  why`; a draft, or a run that observed no pull request, prints the
same lines and exits 0.
Enforced by: tests/test_chain_check.py::TestMain

**An item is judged at the pull request that carries it.** A declaration
that reached the branch inside another pull request's squash, where every
commit after the base that touched it is a squash merge GitHub committed with
a subject ending `(#N)`, was judged at that pull request. The check names it
with the squash and judges nothing else of it. So the release pull request
into `main` judges the declarations naming the release branch and those a
commit made on the release branch itself changed, never an item squashed into
it, whose records name commits the squash orphaned. It errs both ways, by
the commit's signature: a squash a person committed, or one whose subject
lost its number, reads as the branch's own and is refused loudly, and a
commit someone makes under GitHub's identity with a number reads as carried.
Enforced by: tests/test_chain_check.py::TestCarriedBy, tests/test_chain_check.py::TestMain::test_a_release_pull_request_leaves_a_squashed_item_to_its_own_pull_request, tests/test_chain_check.py::TestMain::test_an_item_the_release_pull_requests_own_commit_changes_is_judged

**Of a round record the check reads its labelled lines and its `Confirms`
cells, and refuses what it cannot read.** Inside each `### ` section of the
one `## Findings` section it reads one `verdict:` line, one `location:` line
and at most one `refixes:` line, and of the one `## Confirmations` section
the `Confirms` column, each in the one spelling the record's rules give. A
ready pull request fails while a finding reads `open`, and for anything the
check cannot read: a verdict outside `open`, `fixed <commit>` (seven to
forty lowercase hex digits), `answered` and `deferred <home>`; a label in
another spelling; a finding with no `verdict:` or `location:` line, or two
of either; a labelled line outside a finding; a location or a reference it
cannot read; a `Confirms` column that is not the table's first; a record
with no `## Findings` or `## Confirmations` section, or two; a `fixed`
naming a commit HEAD does not descend from, or one that changed no located
path; a reference naming no earlier record, or a finding that record does
not hold, and any reference in round 1; a `fixed` or `answered` finding the
next record neither confirms nor refixes. A labelled line inside a fence or
a comment is not a line, so a finding whose only verdict stands in its fix
block has none, and a fence or a comment that never closes, which would hide
every finding after it, is refused at the line that opened it. Each refusal
names the record, the line and the finding's heading. No emoji, severity or
answer is read for the decision. It errs two ways where the shape holds and
the fact does not: a `fixed` commit that touches a named path and fixes
nothing passes, and the verifying round's warden, whose `Confirms` cell the
check then requires, is who reads the fix; and a fence closed on the wrong
line hides the lines between it and its false closer without being unclosed,
which the orchestrator's reading of each record against the template and the
next round's reading of the earlier records are there to catch.
Enforced by: tests/test_chain_check.py::TestFindings::test_what_the_check_cannot_read_is_refused_by_name, tests/test_chain_check.py::TestRecordFindings::test_a_fence_or_comment_that_never_closes_is_refused_by_its_opener, tests/test_chain_check.py::TestConfirmations::test_a_cell_or_a_header_the_check_cannot_read_is_refused_by_line, tests/test_chain_check.py::TestChannel::test_a_reference_the_check_cannot_read_or_naming_no_finding_is_refused, tests/test_chain_check.py::TestMain::test_an_open_finding_fails_a_ready_pull_request, tests/test_chain_check.py::TestMain::test_a_fixed_commit_head_does_not_descend_from_is_refused, tests/test_chain_check.py::TestMain::test_a_fixed_commit_that_touches_nothing_of_the_finding_is_refused

**The last record is at HEAD, or only the work item's own records follow
it, and none of its findings is `fixed` or `answered`.** A commit after the
last record's `Target SHA` that touches a file outside `seal/specs/<id>/` is
a fix nobody reviewed, and the refusal names it and says a verifying round
is owed. So is a `fixed` or `answered` finding of the last record, since no
round after it read the fix or the answer; a last record whose findings all
read `deferred <home>`, or that holds none, passes.
Enforced by: tests/test_chain_check.py::TestFollows, tests/test_chain_check.py::TestMain::test_the_last_record_is_at_head_or_only_record_commits_follow, tests/test_chain_check.py::TestMain::test_the_last_records_fixed_or_answered_finding_owes_a_verifying_round

**The broad run has one home, `broad-gate.md`, on either routing answer.**
`broad-gate --record <item>` writes `<tree> against <base>` there on a green
run, newest first, every earlier run kept behind it as `; earlier run: …`. At
a ready pull request its newest run is HEAD, or only the work item's records
follow it.
Enforced by: tests/test_broad_gate.py::TestGate, tests/test_broad_gate.py::TestKeptRuns, tests/test_chain_check.py::TestMain

**Nothing reads a record of the old table's shape.** The check opens the
records of the work items this pull request's own commits declare or change
and no other, so a record a merged pull request left behind is read by
nothing again, whatever its shape. One of the old shape under an item this
pull request carries has no `## Findings` section, and is refused by name. A
work item in flight across the update rewrites its records into the shape
before its pull request goes ready.
Enforced by: tests/test_chain_check.py::TestMain::test_a_reviewed_branch_passes_a_ready_pull_request, tests/test_chain_check.py::TestMain::test_an_old_shape_record_under_the_declared_item_is_refused

**The check reads the diff as declarations, not as file identity.** It diffs
without rename detection, so a deleted declaration beside a similar added one
is two declarations and the deletion is judged. A declaration moved with its
bytes unchanged is neither judged nor missed, because the pull request that
only moved it did not make it.
Enforced by: tests/test_chain_check.py::TestChanged, tests/test_chain_check.py::TestRetired

## The guarantee

**The sealer is the final, independent guarantor: it verifies, independently
of the smith and the warden, that the work before it is sound.** Its
reference is the issue body and the tree, never an agent's word or the
orchestrator's summary. It runs after the pull request body and the
changelog fragment are written, on both routing answers, and its order of
work is `agents/sealer.md`'s.

**It checks a claim against the fact, and the parties against each other.**
The acts are `agents/sealer.md` step 3's and step 4's, and this section
names none of them, so the list has one home. Each act is one row of
`## Claims re-run` or `## The parties` in `guarantee.md`. It does not
re-judge the design or the code's quality.
Enforced by: tests/test_the_sealer_guarantees.py::TestDocument::test_the_guarantee_section_points_at_step_3_and_lists_no_act

**Its verdict is `guarantee.md`, from `templates/sdd-guarantee.md`**: the
commit and base, the broad gate's result, the claims re-run, the parties
compared, and one `Verdict:` line — `sound`, `not sound — <what>`, or
`undecidable — <question>`. An undecidable question is the owner's: the
answer goes on a line under the verdict, and the sealer runs again at the
new HEAD.
Enforced by: tests/test_the_sealer_guarantees.py::TestTemplate, tests/test_the_sealer_guarantees.py::TestDefinition

**A ready pull request passes only where `guarantee.md` names HEAD and reads
`sound`.** Only the sealer's two files, `broad-gate.md` and `guarantee.md`,
may follow the commit it names, since every other file on the branch is one
it audited. `not sound`, `undecidable`, an unfilled template, two `Verdict:`
lines or a stale commit each fail naming the file; a draft prints them.
Enforced by: tests/test_the_sealer_guarantees.py::test_a_verdict_other_than_sound_fails_a_ready_pull_request, tests/test_the_sealer_guarantees.py::TestGuarantee

**How it errs.** It samples, so a false claim outside the sample passes, and
the sample is written in the file so the miss can be found afterwards.
Whether five stories agree is a judgment, so a disagreement it does not see
is missed.
Enforced by: nothing — the guarantee's own tables are what a reader audits

## The run

**A run ends with a verifying round.** It is spawned after the last fixes are
committed; its target is the diff of those fixes, new units included; it
asks of every finding marked closed whether the fix holds, and says so in a
`Confirms` cell or a `refixes:` line. A round opening nothing that needs a
fix does not count toward the cap: the cap stops a loop that is not
converging, and such a round is the loop having converged.
Enforced by: tests/test_chain_check.py::TestFollows, tests/test_chain_check.py::TestMain::test_the_last_records_fixed_or_answered_finding_owes_a_verifying_round

**A run has three finding rounds by default, and extends one round at a time
while the findings shrink.** Past round 3 the orchestrator spawns one more
finding round only while the latest round found fewer findings than the one
before it and none of them is a fix of a fix. Each extension is one line in
that round's record, written by the warden from the reason the spawn prompt
gives:

```
Extended past round 3: round 3 found 2, round 2 found 4, and none is a fix of a fix.
```

At the cap every finding still open takes the filing ladder below and reads
`deferred <home>`. No person is asked mid-run.
Enforced by: nothing — the orchestrator applies it, and the sealer reads the count and the extension lines

**A fix of a fix stops the fix passes, at any round.** Where a finding stands
in a unit the fixes under review added or changed, the warden writes its
`refixes:` line, naming the earlier finding as `round-<N>#<n>`, or the
earlier round as `round-<N>` where no finding named the unit, and names the
unit first in the grounds. A round carrying such a line gets no fix pass:
the work item goes back to its framer, who writes `Reframed <date> by <who>,
after round <N>.` under the mark at the foot of `spec.md`.
Enforced by: nothing — the orchestrator applies it, and the sealer reads the mark in the records

**A leftover finding takes the first rung that fits.** A new issue is the
third rung, not the default:

| Rung | When it fits | Where the finding goes |
|---|---|---|
| 1 | the branch owns the unit, or the smith answers the finding with grounds | the diff, or the round record with the grounds |
| 2 | an open issue already owns the ground | a comment on that issue; the verdict reads `deferred #N` |
| 3 | the finding names a party who agreed to act on it | a new issue labelled `from-review`, or a `seal/follow-up.md` row where there is no tracker; the verdict reads `deferred #N` |
| 4 | it names nobody | the round record alone, and the pull request body |

Enforced by: nothing — the orchestrator files, and the sealer reads every `deferred <home>`

## The handoff

**The orchestrator hands an agent coordinates, never prose.** A fact carries
the coordinate that makes it falsifiable — the line, the grep that returned
nothing, the test whose assertion constrains the wording — or is labelled
`executed`, `read` or `unverified`. An aggregate is not a coordinate: a count
can be checked while the claim it stands for cannot. A claim that flips on
where it is measured says where; a command with two forms names the one it
means and what the other is for; a runner the repository ships is named, not
typed into every prompt, and the form handed over is the narrow one.
Enforced by: tests/test_the_handoff_before_round_one.py::test_the_protocol_carries_the_handoff_before_round_one

**While an agent runs, `plan.md`'s Status column is the readout.** The
implementer fills it with the commit that closed each phase, so the
orchestrator opens it rather than asking, and the stall signal is the time
since it last advanced. After the run, `skills/verify/scripts/session_cost.py`
reads the transcript.
Enforced by: tests/test_the_handoff_before_round_one.py::test_the_protocol_names_the_progress_channel_and_the_stall_signal

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
its rows are `skills/verify/SKILL.md` §*Measure the segment, and feed the flow
log*'s; it is not a destination of its own.
Enforced by: tests/test_the_handoff_before_round_one.py::test_the_protocol_names_a_bar_per_segment_kind, tests/test_the_handoff_before_round_one.py::test_the_scripts_bars_are_the_protocols

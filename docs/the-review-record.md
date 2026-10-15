# The review record

What one review round leaves in the tree, what the check at the pull request
reads of it, and the rules the run around the rounds keeps. The orchestrator's
acts are `skills/code-review/orchestration.md`'s; this document is what they
produce and what holds them.

## The round record

**A round is one file the warden writes.** `seal/specs/<id>/rounds/round-N.md`,
from `templates/sdd-round.md`, in the branch worktree under review: `Target
SHA`, the five-column `## Verdicts` table, `## Paste-ready fixes` and
`## Executed probes`. No report file stands beside it and nothing generates,
copies or derives any part of it.
Enforced by: tests/test_chain_check.py::TestVerdictTable

**The vocabulary is four severities and five verdict words.** 🔴 blocks
merge, 🟡 fix or justify, 🟢 matches, ❓ out of verified scope. 🔴 and 🟡 rows
take a bare-integer id and start `open`; the fix pass closes each
`fixed <commit>`, `answered` or `deferred <home>`. A 🟢 row reads `confirmed`
and a ❓ row `❓ out of verified scope`. A wrong sentence an agent reads and
acts on is a 🟡; a sentence in a record that merely reads badly is not a
finding.
Enforced by: tests/test_chain_check.py::TestVerdictOf, tests/test_chain_check.py::TestOpenFindings, tests/test_chain_check.py::TestOpenFindings::test_a_finding_row_closes_only_by_a_fix_passs_word

**The fix pass fills two cells per open row and nothing else in the file.**
`Verdict` takes the closing verdict, with the commit for `fixed`; `Grounds`
keeps the warden's text and adds the fix pass's after it as
` · fix pass: <what was done, or why not>`. A correction to a record, or a
repair made outside the tree, produced no commit on the branch and closes
`answered` with where the repair is.
Enforced by: nothing — the next round's warden reads the cells against the commits, and the sealer re-checks every `fixed <commit>`

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

**A ready pull request fails while any row of any record reads a word that
does not close it.** A row whose first cell opens with 🔴 or 🟡 is a
finding, and it closes only by the fix pass's three: `fixed` with the commit
in the cell, `answered`, or `deferred <home>`. Any other row — 🟢, ❓, an old
record's ⬜, a bare number or nothing — closes where its `Verdict` cell
begins with one of those, `confirmed` or `out of verified scope` (or a word
the old generator's records used), and is open otherwise. The refusal names
the row and lists the words that close a row of its mark: the fix pass's
three for 🔴 and 🟡, `confirmed` for 🟢, `❓ out of verified scope` for ❓,
and all of them for any other mark. So a 🟢 row left at `open` fails, and so
does a 🔴 row that reads `confirmed` or a bare `fixed`. It errs where a row's
severity stands only in its Finding cell: that row has no mark in its first
cell, and it closes by any closing word.
Enforced by: tests/test_chain_check.py::TestOpenFindings, tests/test_chain_check.py::TestOpenFindings::test_a_finding_row_closes_only_by_a_fix_passs_word, tests/test_chain_check.py::TestMain

**The last record is at HEAD, or only the work item's own records follow
it.** A commit after the last record's `Target SHA` that touches a file
outside `seal/specs/<id>/` is a fix nobody reviewed, and the refusal names it
and says a verifying round is owed.
Enforced by: tests/test_chain_check.py::TestFollows, tests/test_chain_check.py::TestMain

**The broad run has one home, `broad-gate.md`, on either routing answer.**
`broad-gate --record <item>` writes `<tree> against <base>` there on a green
run, newest first, every earlier run kept behind it as `; earlier run: …`. At
a ready pull request its newest run is HEAD, or only the work item's records
follow it.
Enforced by: tests/test_broad_gate.py::TestGate, tests/test_broad_gate.py::TestKeptRuns, tests/test_chain_check.py::TestMain

**A record the generator wrote reads under the check.** It reads `Target SHA`
and the verdict table of every record in the tree, and refuses nothing for
the fields it no longer judges.
Enforced by: tests/test_chain_check.py::TestMain

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
asks of every finding marked closed whether the fix holds. A round opening
nothing that needs a fix does not count toward the cap: the cap stops a loop
that is not converging, and such a round is the loop having converged.
Enforced by: tests/test_chain_check.py::TestFollows

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

**A fix of a fix stops the fix passes, at any round.** The warden marks
`fix of a fix` in a finding's `Finding` cell where its unit is one the fixes
under review added or changed. A round carrying the mark gets no fix pass:
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

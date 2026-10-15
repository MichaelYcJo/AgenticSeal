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
merge, 🟡 fix or justify, 🟢 matches, ❓ out of verified scope. A 🔴 or 🟡 row
carries a bare-integer id and opens at `open`; the fix pass closes it
`fixed <commit>`, `answered` or `deferred <home>`. A 🟢 row reads `confirmed`
and a ❓ row `❓ out of verified scope`. A wrong sentence an agent reads and
acts on is a 🟡; a sentence in a record that merely reads badly is not a
finding.
Enforced by: tests/test_chain_check.py::TestVerdictOf, tests/test_chain_check.py::TestOpenFindings

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

**`chain_check.py` reads the declaration, the frame, the records and the
broad gate's file, and nothing else of a round record.** It judges every
`routing.md` the pull request adds or changes and the one naming its branch.
A ready pull request fails on any refusal, each named `path:line  why`; a
draft, or a run that observed no pull request, prints the same lines and
exits 0.
Enforced by: tests/test_chain_check.py::TestMain

**A ready pull request fails while any 🔴 or 🟡 row of any record reads a
word that closes nothing.**
Enforced by: tests/test_chain_check.py::TestOpenFindings, tests/test_chain_check.py::TestMain

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

## The run

**A run ends with a verifying round.** It is spawned after the last fixes are
committed; its target is the diff of those fixes, new units included; it
answers whether each closed finding is actually closed. A round that opens
nothing needing a fix does not count toward the cap, because the cap stops a
loop that is not converging and such a round is the loop having converged.
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
Enforced by: tests/test_chain_check.py::TestFrame

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

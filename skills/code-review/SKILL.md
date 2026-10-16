---
name: code-review
description: |
  Two-stage review methodology (spec compliance, then quality) with comparison axes,
  cross-session review records, and re-review inheritance.
  Use when: reviewing a PR or diff, re-reviewing after fixes, orchestrating reviewer agents.
  NOT for: implementing fixes (use `implement`), style-only linting a formatter
  can do, or a plain bug-and-cleanup sweep of a diff — Claude Code's built-in
  `/code-review` covers that. This one judges spec compliance before quality and
  carries earlier rounds' coordinates across sessions.
---

# code-review — spec first, then quality

Loaded by the `warden` agent; also drives the orchestrator running a
review. The default assumption is **"this code has defects"** — try to find
them, not to prove their absence. An ungrounded LGTM is forbidden; when
uncertain, write a question, not a pass.

## The orchestrator's half is a file of its own

**If you are orchestrating a review run rather than reviewing a diff, read
`skills/code-review/orchestration.md` before round 1.** The five sections
this file used to carry under an `Orchestrator:` prefix are there, verbatim
and under the same headings: how a fix pass is obtained, how a run ends, when
the pull request opens, what to check before posting, and how the cycle
closes.

**A reviewer never opens it**, and that is why it is a path rather than an
entry in a `skills:` list. Deciding whether a run ends, resuming an
implementer, opening or marking a pull request, and posting are four acts
`agents/warden.md` forbids the reviewer — so 24,948 characters of procedure
reached every `warden` spawn with no act of its own to apply them to (#265).

Everything else in this file is the reviewer's, and the orchestrator reads it
too: a run is judged against the same two stages and the same axes as the
diff it reviews.

## The language the round records are written in

The prose in `rounds/round-N.md` — what follows each label, the text under
its headings and the cells of its tables — follows `Record language` in
`config.md`, English when the row is absent. The root is `<repo>/seal/`
where that directory exists and `$(git rev-parse --git-common-dir)/seal/`
otherwise.

What stays English regardless: every field name, section heading, label and
vocabulary word the checkers match, listed in `templates/config.md` under
*What no row governs*. `chain_check.py` reads those strings literally, so a
translated `## Findings` heading or `verdict:` label is not a translation —
it is a record the checker cannot read.

**The report you post to the pull request is not a record.** It is prose for
whoever opens that pull request, and follows `Commit and pull request
language` instead, per `commit-pr-convention`. Posting and recording are
separate acts producing different texts, which is why the two rows split
here.

## Two stages, in order

1. **Spec compliance** — actual code vs. the written spec (`docs/` policies
   first, then `seal/specs/` SDD). Look for both missing *and* unrequested extra
   behavior. Do not trust the implementer's report; read the code.
2. **Quality** — only after stage 1 passes: correctness, error handling,
   security, performance, test quality.

The SDD set includes the work item's `overview.md`, which arrives in the diff
rather than needing a search — the change writes it. It is the implementer's
account, so stage 1 governs it: read the code, never adopt what it concludes.
Three sections carry that account. **Where spec and implementation diverged**
declares where the code left the document; **Not verified** is the author's own
list of claims nobody has checked; **Fed back into the spec** holds clauses the
implementer added to the spec set during this change, which is why an account
citing them is citing itself.
Settle what you can and report each result; what only a person can answer stays
open, and the report says which of the two happened. Reviewers do not edit the
file.

Review scope is not limited to changed files. New code that calls into
untouched files makes *their* query conditions and boundary operators take
effect for the first time — follow every call the change introduces.

## Comparison axes

Fix the axes before starting and cover **all** of them; picking whatever
catches the eye misses something different every time.

| Axis | Compare |
|---|---|
| Inputs | names, types, required/optional, defaults, accepted ranges |
| Authorization | who acts/queries as whom; self/admin/other branches |
| Query scope | which set is targeted: period, ownership, status filters |
| Exclusions & boundaries | excluded states, overlap conditions, **boundary values** (rarely written down — most frequent divergence point) |
| Deliberate non-exclusions | what the spec intentionally does *not* filter; new code tends to "clean it up" |
| Ordering, dedup, response shape | sort keys, tie-breaking, dedup basis, included/excluded fields |
| Error paths | failure conditions, codes, messages; failure vs. empty result. Count **new failure paths the change introduces** separately — someone must classify each as fix or regression |
| State transitions | against the spec's state machine, if one exists |
| Concurrency & atomicity | what can change between the read that decides and the write that acts: state held across an external call or `await`, transaction boundary against lock scope, whether a retry executes twice |
| Security | who can reach this path and as whom; the trust of every input that crosses an OS or process boundary; whether each failure fails open or closed; what a crafted name, path, or payload reaches |

Every axis above the last two is settled by reading a single request from end
to end. The concurrency axis is not: it asks what a *second* actor does while
the first is mid-flight, and no amount of following one path answers it. It was
added after a review walked all eight of the others cleanly and a second
reviewer, working from no list at all, found a window where a reservation was
mutated while an external call was in flight.

The security row earned its place the same way. Stage 2 has always named
security, and the table is what makes an axis mandatory — an axis that lives
in prose leaves no row of `## Not judged` when nobody walks it. It also
shares the concurrency row's exemption on its own grounds: it asks what an
input
nobody sends in good faith does, and no amount of following the request in
front of you answers it. Three of one round's four
blocking findings had a stronger security frame than the one they were given,
and one was a fail-open — an error path that answered "nothing to see" — in a
repository that keeps `tests/test_gates_do_not_fail_open.py` for that class
alone.

### The table is a floor, not a ceiling

A fixed list covers the same ground on a bad day as on a good one, which is
what it is for. The cost is the other half: an axis nobody wrote down is not
reported as unjudged, it leaves no trace at all. A row of `## Not judged`
records that you looked and could not decide — there is no row for what was
never on the list.

So name this change's own axes before starting, in the round's first minutes,
the way the base branch and the review-chain marker are settled there. Read the
diff for what could go wrong that the table does not ask about — money and
rounding, time zones, resource lifetime, migration ordering, pagination
stability while writes land — and add those rows for this round. An axis you
name here is walked and reported like any other; the ones above are the
minimum, not the set.

Distinguish findings from reading vs. findings from execution, always.
Something you did not run is never reported as passing.

### Probes vs. regression tests

| | What | Handling |
|---|---|---|
| Probe | Temporary test to settle what reading can't | You write it, run it, **delete it** (name `test_tmp_*`) — and everything else it made goes with it. The verified fact goes into the report |
| Regression test | Test that should exist but doesn't | **You don't write it.** Hand it over as a list with the target file per row |

Batch probe cases into one file and run once. Never probe what reading answers
— schema constraints, enums, defaults settle "can this state even exist"
claims without running anything. Don't touch `test_tmp_*` files another
session created.

**The file is not the whole of it.** Contract §7 is about leavings, not files:
a worktree, a branch, a checkout, a scratch clone or a virtual environment your
probe made for itself is a leaving too, and the probe is not over until every
one of them is gone. Deleting the named file and stopping there is what left a
git worktree behind through a whole review chain — the report said the probe
files were deleted, and there was nothing wrong with that sentence. §7 carries
the incident that cost this rule.

**A fixture chain is `&&`, never `|`.** A pipe between two commands does not
sequence them, it feeds the first one's output to the second, and a chain
built that way can sit waiting on stdin with nothing ever arriving. One
review round lost **68 minutes to a single such call** — `mkdir … | cd t3 &&
git init …` — while every other call it made totalled thirty-five seconds. The
hang exceeded the tool's own maximum timeout, so nothing cut it off, and the
parent's meter showed a healthy segment the whole time because a child's
command time is invisible to it.

So: build fixtures with `&&`, and give any call that could run long a timeout
you chose rather than one you assumed. A probe that hangs costs more than
every probe that round put together.

## Cross-session records — `seal/specs/<work-item-id>/`

**Before starting**, read this directory if it exists. Axes a previous round
already judged are not re-walked — unchanged code keeps its verdict. Probes a
previous round ran are only re-checked for "is it fixed now".

The work item is the key, and its `routing.md` names the branch. The warden
writes `rounds/round-N.md` from `templates/sdd-round.md`, the fix pass
writes each finding's `verdict:` and `answer:` lines, and every round file
stays for the next round to read: `docs/the-review-record.md` §*The round
record* states the labels, the values and who writes what.

What carries is **where to look, not what was concluded**. A later round opens
those coordinates and reaches its own verdict; an axis marked clean in round 1
can be broken by the fixes made for round 2, and inheriting that verdict is
exactly how it goes unseen. Earlier verdicts set the agenda, on this round's
grounds: every finding the round before closed `fixed <commit>` or
`rejected` is named by this round, by a `confirms:` line where the close
holds or by a finding's `regression:` line where it does not, and the check
refuses a finding no later round names.

Re-deriving the verdict is not re-walking the code. Finding the coordinates is
the expensive half, and `round-N.md` exists so it is paid once; a later round
opens what they name instead of searching again. The cost added is a re-read
at known locations, which is what keeps a round-1 pass from covering for a
round-2 regression.

The test for what may be carried is whether staleness is detectable, not
whether the fact feels durable. A rule's `Enforced by:` target carries because
`rules --check` fails the suite when it is gone; what the original
does carries because `seal/parity.md` pins the baseline SHA it was read at.
Both are re-established when their check fails, or when `parity.md` lists the
path under coordinate-trust exceptions. A verdict on current code carries
nothing — no check exists that would tell you it went stale, which is exactly
why the round has to reach it again.
## Findings format

**A finding is one `### <n>. <symptom>` section under `## Findings`,
numbered from 1, and the number in its heading is its id.** Its `severity:`
line names the required action, not just a rank:

```
severity: must     — spec violation or defect; fix before merge
severity: should   — a defect the release would ship: the tool does something wrong, or tells a person something wrong; fix, or say why not
```

A wrong sentence that an agent reads and acts on is a `should` defect. A
record's sentence that is only awkward is no finding at all.

**Two other kinds of entry are never findings.** What this round confirmed
holds — a closed finding of the round before, read and found closed, or a
claim the frame or the build made that held — is a `confirms:` line under
`## Confirmations`. What
it could not judge is a row of `## Not judged` naming who answers it, and it
is never silently counted as a pass. An earlier round's finding is named
`round-<N>#<n>` wherever this round refers to it
(`docs/the-review-record.md` §*The round record*).

Every finding carries its `location:` line, what is wrong, why it matters,
and a paste-ready fix. Its labels are lowercase words at the start of their
lines, and the record is written in words, with no emoji anywhere in it. The
report is written for posting as a PR comment, but **the user posts it** —
publishing externally is the user's call.

**Paste-ready means the snippet cannot mislead on its own.** A fix often needs
a name the tree does not have yet — a field the schema never defined, a helper
nobody wrote. Saying so in the paragraph above does not travel: people copy the
block, not the prose around it. Mark every such name inside the snippet, at the
line that uses it:

```python
if requester != order["paid_by"]:   # NAME NOT IN TREE — no order schema found
    raise PermissionError(...)
```

An invented identifier that reads as verified is worse than no suggestion. If
too many names are missing for a snippet to stand, describe the change in
sentences and say which document would have to exist for the code to be
written.

**Every one of those blocks goes inside the finding it fixes**, after the
grounds and before the `answer:` line, so the fix pass opens one section and
finds the what, the where, the why and the paste together. A fix described
in prose alone is rebuilt from the description by the fix pass.

**A fix touching an OS boundary states its assumed precondition.** The
premises are the ones a snippet assumes without a line to show for them —
path resolution, file modes, symlinks, subprocess working directory,
encoding — and a sketch that assumes one reads as paste-ready and is not. The
clause
above covers invented *names*; this covers unexamined *premises*. State the
precondition beside the line that relies on it, the way a missing name is
marked, or in one sentence under the snippet — and "it has none" is a
statement worth making, because silence and "none" read alike. Three of one
round's four blocking findings arrived as sketches that read as paste-ready
and were not.

### Verdicts that close too early

Three shapes of closing recur, and each is written down here because each was
measured costing rounds.

**An enumeration over an unbounded domain is a recorded limit, not a closed
finding.** A fix that answers a finding by enumerating cases — keywords,
spellings, constructs — from a domain nothing bounds has narrowed the finding,
not closed it. The verdict says so, and the limit goes where it will be read
again: the skill's Known limits or a `deferred <home>` verdict. Measured: one
such rule cost three rounds and two owner decisions, and closed only when the
uncertainty moved out of the classifier instead of being argued inside it.

**A mutation score licenses *tested*, never *safe* — say so where the number
is reported.** A score like `12/12 killed` establishes that the pins
discriminate — the fix is *tested* — and says nothing about whether it is
*safe*. Three consecutive rounds each reported a perfect score, and all three
were rounds whose fixes opened findings.

**A document claim gets a pin.** A claim a fix writes into a document — a
limit, a vocabulary, a behaviour — closes when a test pins the document, not
when the sentence lands. The same class of finding returned one round apart
because no test pinned any of the three documents involved, and the moment
pins existed they found a fourth file nobody had covered.

End with the proof block. Fill it only with files actually opened; write
`none — <reason>` otherwise:

```
📋 code-review applied
· spec:     <policy/SDD files and clauses read>
· compared: <files opened for comparison, file:line>
· verdict:  must n · should n · confirmed n · not judged n
```

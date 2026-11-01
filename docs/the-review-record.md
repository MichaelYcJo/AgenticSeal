# The review record

What one review round leaves in the tree, what the check at the pull request
reads of it, and the rules the run around the rounds keeps. The orchestrator's
acts are `skills/code-review/orchestration.md`'s; this document is what they
produce and what holds them.

## The round record

**A round is one file the proofer writes.** `seal/threads/<id>/trail/rounds/round-N.md`,
from `templates/records/sdd-round.md`, in the branch worktree under review: a `seal` block holding its `target:` line, then `## Findings` with one `### <n>. <symptom>` section per finding, `## Confirmations` where the round confirmed something, `## Not judged` and `## Probes`. A finding holds one `seal` block of its fields, why it matters with its grounds, the paste-ready fix in a fenced block, and, once it is closed, its close block. The record is written in words, and no
emoji stands anywhere in it. No report file stands beside it and nothing
generates, copies or derives any part of it.
check: tests/skills/test_chain_check.py tests/text/test_the_record_is_written_in_words.py

**The record's fields stand in `seal` blocks, and `hooks/lib/fields.py` is the one spelling of their grammar.** A `seal` block is a fenced block opened by a line of three backticks and `seal`, with nothing before or after them, outside every other fence. The first line of a block names its kind. `target:` opens the round's one block, which stands outside every finding and holds at most one `original:` line. `severity:` opens a finding's one block, which stands in the finding's `### <n>. <symptom>` section with its `location:` and `evidence:` lines and at most one of a `regression:` and a `reopens:` line. `verdict:` opens a finding's close block, at most one in its section, with its `answer:` line and a `location:` line where the fix went to a path the finding does not name. `confirms:` opens a confirmation's block outside every finding. Every line of a block is a field its kind takes, written `<key>: <value>` with the key exactly as the module spells it and the value matching the key's shape whole; a line that is not, a key over its count and a blank line are refused at their line, and the block is not read past it. Nothing outside a block is a field: a line shaped like one in prose decides nothing and is named by nothing, and where a field is owed its absence is refused. A finding with no close block is open. The record holds one `## Findings` heading, under which each `### <n>. <symptom>` heading opens a finding, and no two findings share a number. No `Record language` translates a key, a value's fixed words or the info string. A list of the ways a label is written grows by one row for every near miss a round finds and never converges, and a block leaves a reader nothing to guess: inside it every line is the form, and outside it none is (`skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*).
check: tests/skills/test_chain_check.py

**A finding's `verdict:` decides it, and severity is for people.** A finding with no close block is open; the fix pass's close block answers it with `fixed <commit>`, `rejected` (the finding does not hold, and `answer:` says why) or `deferred <home>`. `severity:` is `must` (fix before merge) or `should`
(fix, or say why not); the check holds it to its shape and decides nothing on
it. What this round confirmed holds is a `confirms:` entry of
`## Confirmations`, and what it could not judge a row of `## Not judged`
with who answers it; neither is a finding. A wrong sentence an agent reads and acts on is `should`, and so is a wrong line of a work item's own record that a script reads or copies: a line the check reads, a row `seal unverified` reads, or a line `seal pr-body` copies into the pull request body. A sentence of a record that restates another record's fact and has drifted from it is a finding, answered by removing the copy and citing the home, never by correcting the copy; one that has not drifted is no finding, since the templates no longer invite it and #1147 audits what stands. A sentence in a record that merely reads badly is not a finding.
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
claim resting on neither is no finding but a row of `## Not judged`. The
check holds the line to its shape and reads nothing out of it. A backtick
ends a command on the line, so a command that holds one is written and run
with `$(printf '\140')` in place of the character, and the line names the
command the round ran.
check: tests/skills/test_chain_check.py

**A claim of absence is `executed` only.** A finding that says something is
missing, that nothing catches, calls or states it, names the search that
found nothing, because no coordinate opened can show an absence. The check
reads the line's shape and never whether a claim is one of absence; the
proofer who writes the line and the round that reads it judge that.
check: none reader: the proofer and the next round

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
reopen, and a `confirms: none` entry is a claim of the frame or the build
that matched, with its prose on the lines after it. Every finding of round
N at `fixed <commit>` or `rejected` is named by a `confirms:`, a
`reopens:` or a `regression:` line of round N+1, and one left unnamed is
refused at its own heading in round N's record; a `deferred <home>`
finding owes nothing. Round 1 has no earlier record, so its entries read
`none`. A round with nothing to confirm leaves `## Confirmations` out.
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

## What the check reads at the pull request

**`chain_check.py` reads the declaration, the frame, the `## Rule changes`
section of each `frame/design.md` it parses, the records, the broad gate's
file, the sealer's guarantee, the `Seal-Routing` trailers of the pull
request's own commits and, where `seal/parity.md` is declared, the
migration config's `Baseline commit`, and nothing else of a round
record.** It judges the
`routing.md` naming the pull request's branch and every one its own commits
add or change. A ready pull request fails on any refusal, each named
`path:line  why`; a draft, or a run that observed no pull request, prints the
same lines and exits 0.
check: tests/skills/test_chain_check.py

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
check: judged-where-carried

**Of a round record the check reads its `seal` blocks and its finding headings, and refuses what it cannot read.** It reads every block *The round record* describes, and a ready pull request fails for any line that grammar refuses. It names each file under `trail/rounds/` whose name is no `round-N.md` as one it did not read, so a record under another name is a line of the check's output and never a silent pass, and it names each fence whose info string's first word, case folded, is `seal` and whose opener is not the block's, which changes no exit code. It fails, too, while a finding has no close block; for a `fixed` naming a commit HEAD does not descend from, or one that changed no path the finding's or its close's `location:` names; for a reference naming no earlier record, or a finding that record does not hold, and any reference in round 1; and for a `fixed` or `rejected` finding the next record names on no `confirms:`, `reopens:` or `regression:` line. A `seal` block inside another fence is part of that fence, so a finding whose block stands inside its fix block lacks its finding block and is refused for it, and a whole finding written inside a closed fence is no finding: the orchestrator's read of the record before its commit, against the template, is what catches it. A record written before the fields stood in blocks holds no round block, and is refused with one message naming the template. A fence that never closes, which would hide every block after it, is refused at the line that opened it. A line
outside every fence that begins with `<!--` is refused at its line, because
the check reads a comment as text. Each refusal names the record, the line and the
finding's heading. No emoji is read, and neither severity nor answer
decides anything. It errs two ways where the
shape holds and the fact does not: a `fixed` commit that touches a named
path and fixes nothing passes, and the verifying round's proofer, whose
`confirms:` line the check then requires, is who reads the fix; and a fence
closed on the wrong line hides the lines between it and its false closer
without being unclosed, which the orchestrator's reading of each record
against the template and the next round's reading of the earlier records
are there to catch.
check: round-record-read-by-label

**The last record is at HEAD, or only the work item's own records follow it, and none of its findings is `rejected`, nor `fixed` with a path beyond the work item's records in its `location:` or in its commit.** A commit after the last record's `target:` commit that touches a file outside `seal/threads/<id>/` is a fix nobody reviewed, and the refusal names it and says a verifying round is owed. So is a `rejected` finding of the last record, a `fixed <commit>` whose commit touched any path outside `seal/threads/<id>/`, and a `fixed` finding whose `location:` names any path outside `seal/threads/<id>/`, whatever its commit touched, since no round after it read the fix, the rejection or the code half of the finding. A `fixed <commit>` finding located in the work item's own records alone and fixed by a commit that touched them alone passes: the sealer reads every record at HEAD (`agents/sealer.md` step 2), and in 0.22.1 to 0.22.4 five verifying rounds confirmed such fixes and found nothing else (#1045). A last record whose findings all read `deferred <home>` or such a `fixed`, or that holds none, passes.
check: last-record-at-head
check: last-record-at-head

**The broad run has one home, `trail/gate.md`, on either routing answer.**
`seal gate --record <item>` appends there, on a green run, a `seal` block holding `run: <tree> against <base>`, below the block of every earlier run, and appends nothing where the last block names the same run. At a ready pull request its newest run, the last block, is HEAD, or only the work item's records follow it.
check: tests/skills/test_broad_gate.py tests/skills/test_chain_check.py

**The check reads no record of the old table's shape.** It opens the
records of the work items this pull request's own commits declare or change
and no other, so a record a merged pull request left behind is never judged
at a pull request again, whatever its shape. Three readers outside the check
still open merged records: `.github/scripts/release_seal.py#chain_counts`
reads every record of a release with the `chain_check` of the tree it runs
from, and `evals/scripts/replay_targets.py` and `evals/scripts/seed_defects.py`
read each labelled record, and each record in `seal` blocks, with the
`chain_check` of the commit that last wrote it, from either layout a release
has kept its records in: the one before 0.23.0, and
`seal/threads/<id>/trail/rounds/` since (`evals/scripts/replay_targets.py#LAYOUTS`
names both). A record of an older shape under an item this pull request carries holds no round block, and is refused with the message that names the template. A work item in flight across a change to the grammar meets the change as its records stand: its round records are rewritten into blocks, and its `guarantee.md` and `trail/gate.md` take a block below their old text when the sealer and `seal gate --record` run again. An added field is never supplied after the round that would have written it, so an item whose records predate an added field merges before the change or has its rounds written after it. A record written before a line was added lacks
it, and the lack is no finding for a later round.
check: old-table-shape-refused

**The check reads the diff as declarations, not as file identity.** It diffs
without rename detection, so a deleted declaration beside a similar added one
is two declarations and the deletion is judged, except where the tree the
check reads has no top-level `seal` entry. A deletion whose work item's
directory stood at the merge base and is gone whole reads as a settle and
is accepted (`docs/the-record-layout.md` *The fold, and what tells it from a
deletion*). A declaration moved with its
bytes unchanged is neither judged nor missed, because the pull request that
only moved it did not make it.
check: tests/skills/test_chain_check.py

**The check parses the `## Rule changes` section of the `frame/design.md` of
every work item whose `routing.md` it judges, and of every work item
`frame/design.md` the pull request's own commits add or change, with
`skills/settle/scripts/rule_changes.py`, the one reader of that
section, and a section the reader refuses is a refusal at the line the
reader names, carrying the reader's reason.** `settle` groups the
released designs by the sections their rule changes name, and a design
whose section does not parse joins no group, so a section first read
there is a rule change the settle can place only by reading the whole
design, with no pull request left to fix it in. A
declared work item can edit another work item's section without
touching that work item's `routing.md`, which is why the diff is read
as well as the declarations. A pull request that declares nothing
reads no `frame/design.md`. A `frame/design.md` a squash of another pull request
carried, and one the pull request only moved, are read at the pull
request that made them. A `frame/design.md` with no `## Rule changes` section
is left alone here, and the settle reads such a design whole. The refusal
reads a fact from the file and puts no question to a person.
check: rule-changes-read-at-the-pull-request

**Where `seal/parity.md` is declared and the change reaches outside
`docs/` and `seal/`, every round record of a work item declaring `through the review chain` carries one `original:` line in its round block naming the migration config's baseline.** The check reads `seal/parity.md` at HEAD
and the paths the pull request changes against its base, through the
parity arm's own rule for a change confined to the document roots. A
diff it cannot read ends the check with exit 2 before any record is
judged. A ready pull request fails while a round record holds no
`original:` line, or holds one whose commit and the
`Baseline commit` row's SHA are not one a prefix of the other, and a
migration config whose `Baseline commit` holds no SHA fails it too. Each
refusal names the record, or the config, and both commits where two are
compared. The proofer writes the line in the round where it compared that
round's target with the original through `legacy-parity`. A round that
could not resolve the original writes no line and raises an `unread`
finding, so the refusal stands until a round compares. What the check
cannot read is whether the comparison was a good one, which is the
proofer's.
check: parity-at-the-pull-request

**Where `seal/parity.md` is declared and the change reaches outside
`docs/` and `seal/`, the `guarantee.md` of a work item declaring
`straight to the PR` carries one `original:` line in its newest verdict block naming the migration config's baseline.** The sealer writes it after comparing the audited
commit with the original through `legacy-parity`, and the check reads it by
the rule a round record's line is read by: a ready pull request fails while
the guarantee holds no such line, or one whose commit and the
`Baseline commit` row's SHA are not one a prefix of the other. What the
check cannot read is whether the comparison was a good one, which is the
sealer's.
check: parity-in-the-guarantee

**On every pull request, the check reads the `Seal-Routing` trailer of
each of its own commits, as `docs/the-routing-check.md` *At the pull
request* states.**
check: routing-trailer-at-the-pull-request

**Where the tree the check reads has no top-level `seal` entry, the
check reads nothing as declared.** The tree is HEAD, and the working
tree under `--worktree`. The pull request that moves a root to local
mode deletes every `routing.md` with the root, and a deleted declaration
is otherwise judged. With no `seal` entry there is nothing to declare,
so the check judges the trailers as for any pull request that declares
nothing. Where git cannot say whether HEAD has the entry, the
declarations stay judged.
check: nothing-declared-nothing-owed

## The guarantee

**The sealer is the final, independent guarantor: it verifies, independently
of the crafter and the proofer, that the work before it holds.** Its
reference is the issue body and the tree, never an agent's word or the
orchestrator's summary. It runs after the changelog fragment is written, the
orchestrator's broad run has written `trail/gate.md`, and the pull request
body is written from the records, on both routing answers; it reads that
record and runs nothing broad, and its order of work is
`agents/sealer.md`'s.

**It checks a claim against the fact, and the parties against each other.**
The acts are `agents/sealer.md` step 3's and step 4's, and this section
names none of them, so the list has one home. Each act is one row of
`## Claims re-run` or `## The parties` in `guarantee.md`. It does not
re-judge the design or the code's quality.
check: tests/behaviour/test_the_sealer_guarantees.py

**The pull request body opens with the orchestrator's part, in the repository's language, and the records' copy follows it in one fold; the sealer reads only the orchestrator's part.** `seal pr-body` writes the part of the body below the line `skills/code-review/scripts/pr_body.py#HEADING` holds, copied from the work item's records inside one `<details>` block whose `<summary>` names the copy and is followed by a blank line, with nothing inside it folded again; the orchestrator writes above that line only what no record holds. A reader who stops after the first screen has the orchestrator's part, and the squash commit keeps the block's tags as text. The sealer runs `seal pr-body --check` on the body file before it compares the parties, and withholds where the part below the line is not what the records give. That part then gives it nothing to compare: the records it copies are what the sealer audits.
check: tests/skills/test_pr_body.py tests/behaviour/test_the_sealer_guarantees.py
check: tests/skills/test_pr_body.py tests/behaviour/test_the_sealer_guarantees.py

**Its verdict is `guarantee.md`, from `templates/records/sdd-guarantee.md`**: the broad gate's run, the claims re-run and the parties compared, in tables for people, and one `seal` block per run of the sealer, appended below the blocks of earlier runs and never edited after its run. A verdict block holds `target: <sha> against <base>`, each one word, the `original:` line where *What the check reads at the pull request* owes one, and one `Verdict:` line, `sealed`, `withheld reason: <the claim, its party, its coordinate>` or `undecided question: <the question, for the owner>`, written exactly so. The last block is the newest run and the others are the earlier runs, which the stamp reads. A guarantee with no verdict block, or with a line of a block that does not parse, is refused naming the file and the line. An undecided question is the owner's: the answer goes on a line below the newest block, and the sealer runs again at the new HEAD and appends its block.
check: tests/behaviour/test_the_sealer_guarantees.py tests/skills/test_chain_check.py

**A ready pull request passes only where the newest verdict block of `guarantee.md` names HEAD and reads `sealed`.** Only the closing records, `trail/gate.md` and `guarantee.md`,
may follow the commit it names, since every other file on the branch is one
the sealer audited. A newest block reading `withheld` or `undecided`, an unfilled template, a block that does not parse or a stale commit each fail naming the file; a draft prints them.
check: ready-needs-sealed

**How it errs.** It samples, so a false claim outside the sample passes, and
the sample is written in the file so the miss can be found afterwards.
Whether five stories agree is a judgment, so a disagreement it does not see
is missed.
check: none reader: a reader of the guarantee's own tables

## The stamp

**The stamp is drawn once per work item, from the sealer's `sealed`, at the
end of the turn in which `guarantee.md` came to read it, at its write, in
either mode.** The stamp means every party
verified the work item, the sealer last, and the work is done, so it is
drawn from that verdict and never from the broad gate's run, which comes
before the sealer has read anything and draws nothing
(`docs/the-broad-gate.md` *One act, one owner*). A `post-edit` gate,
`hooks/sealer-stamp-queue.py`, runs after each `Write` or `Edit` of a
`seal/threads/<id>/guarantee.md` under either root. Where the reader the pull request's check reads it through refuses none of its lines and its newest verdict block reads `Verdict: sealed`, it writes the stamp's values under
`<git-common-dir>/agentic-stamp/<session>/` for the payload's session,
which a subagent's write carries as the main session's, and says one line
naming the file and `seal stamp --from <path>` as its message. A `Stop` hook draws each undrawn file
of its own session once, after that turn's text, and a subagent's end draws
nothing. `withheld` and `undecided` queue nothing. Once per work item is held
by what the clone and the tree carry, with no count beside them: a values
file already named for the work item, pending or drawn, under any session's
directory is not written twice, whatever commit it named; a `sealed` whose
audited commit is not an ancestor of the branch the work item's `routing.md`
names queues nothing; and in shared mode a guarantee that read `sealed` at
an earlier commit of HEAD's history, or one of whose earlier verdict blocks reads `sealed`, counts as stamped then, which holds across clones; the earlier blocks alone skip a `sealed` this clone recorded refusing (the next rule). A guarantee in the history that holds no verdict block, written before the fields stood in blocks, counts nothing. It does
not hold for a `sealed` committed over a history that carries no earlier
`sealed` in a clone that holds no values file for the work item, which draws
the stamp again in that clone: the sealing commit amended or rewritten there
over its own parent, or a second seal on a copy of the branch that had not
fetched the first. A `sealed` that drew in another clone, brought onto a
copy of its declared branch that does not hold its audited commit, by hand
or by `checkout`, `cherry-pick -n` or `merge --squash`, is refused at its
write and recorded, and the new audit the refusal asks for draws again
there; it joins that class. The
clone that drew the stamp keeps its values file, so an amend there draws
nothing. That is a stated limit, since across clones the history is the only
record the rule reads, and nothing beside the tree counts stamps. In local
mode no history is read, because none exists: the root and the values
directory share the common dir, so a values file for the work item, pending
or drawn, is a complete record of its stamp in that clone. There once is held by that, by the earlier verdict blocks, and by the audited commit being an ancestor of the branch the work item's `routing.md` names in
its `Branch` row, a branch the clone must still hold. That last keeps a
`sealed` written long ago quiet, since a local-mode work item stays under
the root until the settle after its release removes it; one whose branch still stands draws late, once, at its first edit. The
stamp carries what the records say: the audited commit and its branch, the
base, the work item, the newest broad run and the count of round records.
check: stamp-drawn-once

**A `sealed` refused because its audited commit is not on the branch leaves
a refusal record in the clone that refused it, and an earlier verdict block reading `sealed` that this clone recorded refusing is skipped, so the sealer's new audit draws the work item's one stamp.** The new audit's block stands below the refused verdict's block, and without a record that earlier block would count as the stamp. The record is an empty file,
`<git-common-dir>/agentic-stamp-refused/<id>-<target>`, beside the values
directory and never listed with it. One writer leaves it, for a row that
stands in its own clone and nowhere else: `hooks/sealer-stamp-queue.py`, in
either mode, where the `Branch` row's branch stands and does not hold the
audited commit. It says one line naming the commit and the branch. In
shared mode the pull request's check refuses the same row as stale; in
local mode no check reads it. A recorded target matches a SHA when one is a
prefix of the other and both are at least seven characters long; any other
spelling finds no record, and the verdict counts as stamped. `sealed_before`
skips a `sealed` this clone recorded refusing, as the earlier-run chain
does, because no gate stops a refused row from becoming history before the
pull request's check refuses it; any other `sealed` in the history drew
where it was made, and counts. So a `sealed` that drew, went stale under a rebase and was
refused when its row was edited still holds the work item's stamp, and its
repair draws nothing.
check: refused-sealed-leaves-a-record

**The hook holds its whole message under a budget named in the code, and
steps the drawing down rather than letting the harness persist it.** The
harness writes a `Stop` hook's `systemMessage` longer than 10,000 characters
to a file and shows the person a 2 KB preview, so a stamp past that size is
not seen. `seal_stamp.MESSAGE_LIMIT` is that number, measured with a scratch
hook; `MESSAGE_BUDGET` keeps 1,000 characters of it back for the gate-failure
report `hooks/dispatch.py` prepends to the same message. The harness counts
UTF-16 units, so a character outside the BMP is two, and so does the hook.
One message carries as many of the oldest pending stamps as fit together
with their disc. A stamp has two rungs, with its disc and then without it:
the owner's disc is drawn 28 cells across and has one size, so there is no
smaller disc to step to, and no scale either. That disc is most
of a stamp's size, so one stamp of a real work item's size
goes out per message and a second waits for the next turn. A seal past
what one message can carry stays pending and is drawn at the next turn's
end, and a single stamp that does not fit with its disc by itself is the
only one drawn as the text block with no disc. A stamp can
come out without its disc or a turn later, and a session that ends first
leaves it for `seal stamp --from`. `seal stamp` is not budgeted, because it
is no hook's message.
check: tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/hooks/test_sealer_stamp.py

**What the person's screen shows is not checked, and neither is the order of
the text above it.** The cases prove that the hook emits the right bytes for
the right payload. A screenshot of the probe proved once that such bytes
render unfolded, in colour, after the turn's final text. Whether a given
work item's stamp was seen, and whether the orchestrator wrote its result in
the turn the stamp closed, are read by the person and by nobody else. So is
how the stamp reads on a light background as well as a dark one. Nothing
outside the disc is painted, so its text is in the terminal's own colours and
theme — dim labels, a green `✓`, the title in the stamp's red — and the owner
reads the first real stamp on each background. The line reaches the person
as the edit hook's message, and nobody has watched that message on a screen
yet.
**Nor is the hook's silence where it cannot draw.** No stamp is queued, and
nothing is said, for a `guarantee.md` that arrived by a shell write, a
commit fetched from elsewhere or `seal import` rather than by `Write` or
`Edit`, which no edit hook sees; or for a verdict whose work item names no
branch, or a branch the clone no longer holds. A `sealed` over a commit the
branch does not hold still counts as the work item's stamp, so its repair
draws none, where no edit hook saw it written: by a shell, by a person, or
under a plugin older than the hook. The pull request's check still refuses
that landed row as stale. The hook judges a write's newest verdict block alone, never the earlier blocks, so a `sealed` that drew and whose
audited commit a later rebase, amend or cherry-pick moved out of the history
counts as stamped, which it is. In
local mode the record is the clone's own: a values directory emptied by hand,
or a guarantee brought by `seal import` from a clone that drew and re-sealed
here, draws again. A wrong row that names, by coincidence, the very commit a
copy of the item on another branch was sealed and drawn over draws a second
time once the hook refuses and records it, a class this rule accepts as a
second run of the item. So does a `sealed` that drew in another clone and
was brought onto a copy of its declared branch that does not hold its
audited commit, whatever brought it: the hook refuses and records it, and the
new audit it asks for draws again. No guard can tell that copy from a stale
row the same clone wrote after a push and a rebase. The
hook draws nothing and says nothing where the main session's `python3`
cannot load `seal_stamp.py`, since no launcher stands in front of a hook;
where that session's working directory is outside the clone the stamp was
queued in; or where its plugin predates the hook. Where a file was written,
the edit hook's message names `seal stamp --from <path>`, and a stamp that did not appear is drawn by
hand from it, once. Where none was, the pull request's check is what says the
work item was sealed.
No case, hook or workflow can observe a screen.
check: none reader: the owner on the first real run after a change here

## The run

**A run ends with a verifying round.** It is spawned after the last fixes are committed, and a fix pass owes none only where each finding it closed is located in `seal/threads/<id>/` alone and its commits touched nothing else, as *What the check reads at the pull request* states; its target is the diff of those fixes, new units included; it
asks of every finding marked closed whether the fix holds, and says so on a
`confirms:` line where it holds, and where it does not on a finding's
`reopens:` line, or its `regression:` line where a fix pass's own commit
made the defect. A round opening nothing that needs a fix does not count
toward the cap: the cap stops a loop that is not converging, and such a
round is the loop having converged.
check: run-ends-with-verifying-round

**The orchestrator ends the rounds when they stop paying, and a run has three finding rounds by default, counted from the last design change, as the point where it weighs that rather than spawning the next round by habit.** A design change is a reframe, or a new phase the owner approved in `frame/plan.md`, so the first finding round that reviews new work starts the count again at one, whatever the record's number. The signals that a run is not converging, and what going on and stopping each cost, are `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*'s. A round that opens nothing needing a fix is the loop having converged and counts toward nothing. A regression's fix pass is followed by one verifying round whatever the count, because a fix nobody read is the invariant Table B of the core holds. Every such decision, past the third round or at it, is a row of `frame/plan.md` *Judgments of the run* naming the counts weighed and this section; the proofer writes no line for it. When the orchestrator stops, every finding still open takes a home from the table below and reads `deferred <home>`. No person is asked mid-run.
check: tests/text/test_the_rules_have_one_owner.py

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

check: none reader: the sealer at every deferred verdict

**On a branch whose `routing.md` reads `Automation` `yes`, the
question tool is refused on every call.** The person who answered the
routing question was promised that nothing stops to ask, and a
question put at minute thirty waits for somebody who is not there.
The session builds on the default the question states, records that
default in the work item's `frame/questions.md` as one row, and names it in
the pull request body, where the owner can overturn it. The routing
question put alone, single-select and with its text, goes through
while this session's transcript can be read and holds no answer to
it from this clone, because a run resumed in a new session has to
put question 1 again for the gates that read the press; once it is
answered, it is refused like any other question. Any routing answer
from this clone in the session spends the exemption, including one
given for another work item, so a session that has already answered
for another branch cannot put question 1 again; that is outside the
one-issue flow. The declaration is read through `hooks/lib/routing.py` for the
branch checked out where the session sits, and every way of not
reading it is the attended answer. The file is written by the model,
which is why no gate reads the `automation` press from it. It is read
here only to refuse, so a row the model forged binds only the model,
and a row edited to `no` is in the diff the review reads. A session
sitting in a checkout whose branch is not the declared one is not
held, and neither is a question asked as plain text. A gate whose own
reason says to ask with the question tool meets this refusal too, and
its question states no default: the session takes none of the ways on
that question offers, and hands the stop back at the end of the run.
check: tests/hooks/test_question_gate.py

**The orchestrator's judgments of a run are rows of `frame/plan.md` *Judgments of the run*, each with its grounds and the document it stands on.** The decisions this section leaves to the orchestrator, to go on past the third round or to stop, a regression's route, a leftover's home, and a decision folded into the frame after the frame was committed, are judgments and not sequences, and `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* asks that each be written where the next session reads it. The settle's dry run prints the rows of every released work item grouped by the document they stand on, and the settling session rewrites the section where one kind of judgment keeps costing rounds. The framer's judgments stand in its *Alternatives considered* and the proofer's in its findings, and neither is copied here.
check: none reader: the settling session at the dry run's judgments

## The handoff

**The orchestrator hands an agent coordinates, never prose.** A fact carries
the coordinate that makes it falsifiable — the line, the grep that returned
nothing, the test whose assertion constrains the wording — or is labelled
`executed`, `read` or `unverified`. An aggregate is not a coordinate: a count
can be checked while the claim it stands for cannot. A claim that flips on
where it is measured says where; a command with two forms names the one it
means and what the other is for; a runner the repository ships is named, not typed into every prompt, and the form handed over is the narrow one. A prompt that hands an agent a path outside the repository, such as the worktree it works in, says in the same prompt not to write that path into any record: an agent copies a prompt's paths into the records it writes, where `CONTRIBUTING.md` *House rules* forbids a real path and the `real_identifiers` census in `tests/censuses.py` refuses it, which in 0.18.1 and in #1174 cost a repair and once a rewrite of the branch's history.
check: tests/text/test_the_handoff_before_round_one.py

**While an agent runs, the orchestrator reads the age of its transcript at least every 30 minutes, and `frame/plan.md`'s Status column says which phase it has reached.** The implementer fills the Status column with the commit that closed each phase, so the orchestrator opens it rather than asking. A phase can run for an hour, so the stall signal is the time since the agent's transcript last changed, read through the link that the harness's task output is, with `stat -L`, because the link's own time is the moment it was made. Where the transcript has not moved for 30 minutes, the orchestrator reads the agent's slowest calls with `seal cost` on that transcript and the processes the agent started, and then decides whether to stop it. A completion notice is never waited on alone: in 0.16.0 one crafter call hung for 4 h 48 min and nobody noticed (#680), and an agent can end without one. An unattended run keeps its machine awake for its whole length, and a spawn prompt asks for a probe that may run past a minute as a background command, never as a foreground `&` followed by `wait`. After the run, `skills/verify/scripts/session_cost.py` reads the transcript.
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

# The review record

What one review round leaves in the tree, what the check at the pull request
reads of it, and the rules the run around the rounds keeps. The orchestrator's
acts are `skills/code-review/orchestration.md`'s; this document is what they
produce and what holds them.

## The round record

**A round is one file the warden writes.** `seal/specs/<id>/rounds/round-N.md`,
from `templates/sdd-round.md`, in the branch worktree under review: a
`target:` line, then `## Findings` with one `### <n>. <symptom>` section per
finding, `## Confirmations` where the round confirmed something,
`## Not judged` and `## Probes`. A finding holds the labelled lines the table
below places in a finding, why it matters with its grounds, and the
paste-ready fix in a fenced block. The record is written in words, and no
emoji stands anywhere in it. No report file stands beside it and nothing
generates, copies or derives any part of it.
check: tests/test_chain_check.py tests/test_the_record_is_written_in_words.py

**The record's grammar is the two tables below, and nothing else states
it.**
Each labelled line and finding heading of a record is one row's, and the
check accepts it only where it matches the row's `Shape` whole, stands where
`Where` says and is as many as `How many` allows. Otherwise it is refused at
its line with the row's `Refused as`. `How many` counts per finding for a
line in a finding, and per record for every other line. A label is its
`Line` cell exactly: lowercase, at the start of the line, followed by one
space or by nothing, with no emphasis and no table cell. A line that means a
label and is spelt another way, in another case, under emphasis, with a
space before the colon, or as an old spelling the second table names, is
refused at its line as the label its `Means` cell names, and the finding
carrying it is not read past it. So a
finding holding both spellings does not pass on the lowercase one. Three
rules span rows: a finding carries at most one of a `regression:` and a
`reopens:` line, no two findings share a heading number, and
`## Confirmations` holds no table row. No `Record language` translates a
cell of the table.
check: tests/test_chain_check.py

| Line | Shape | Where | How many | Refused as |
|---|---|---|---|---|
| `target:` | `target: (?P<commit>[0-9a-f]{7,40})(?: against [\w./-]*\w\|, fixes [0-9a-f]{7,40}\.\.[0-9a-f]{7,40})` | outside every finding | one | it names the reviewed commit as `<sha> against <base>`, or `<sha>, fixes <a>..<b>` for a verifying round |
| `original:` | `original: (?P<commit>[0-9a-f]{7,40})` | outside every finding | at most one | it names the migration config's baseline commit this round compared against, as 7 to 40 hex digits |
| `## Findings` | `## Findings` | the record | one | a round record holds one, with a `### ` section and one `verdict:` line per finding |
| `### <n>. <symptom>` | `### (?P<number>[1-9][0-9]*)\. .+` | `## Findings` | each number once | no number: a finding's heading reads `### <n>. <symptom>`, and a later round names it by that `n` |
| `severity:` | `severity: (?:must\|should)` | a finding | one | a severity is `must` or `should` |
| `location:` | `` location: `[^`\s:/#][^`\s:#]*(?::[0-9]+(?:-[0-9]+)?)?`(?:, `[^`\s:/#][^`\s:#]*(?::[0-9]+(?:-[0-9]+)?)?`)* `` | a finding | one | a location is one or more of `path`, `path:line` or `path:first-last`, each backticked, joined by `, ` |
| `evidence:` | `` evidence: (?:executed `[^`]+`(?:, `[^`]+`)*\|read `[^`\s:/#][^`\s:#]*:[0-9]+(?:-[0-9]+)?`(?:, `[^`\s:/#][^`\s:#]*:[0-9]+(?:-[0-9]+)?`)*) `` | a finding | one | evidence is `executed` and each command run, or `read` and each `path:line` or `path:first-last` opened, each backticked, joined by `, ` |
| `verdict:` | `verdict: (?:open\|rejected\|fixed (?P<commit>[0-9a-f]{7,40})\|deferred (?P<home>\S(?:.*\S)?))` | a finding | one | a verdict is `open`, `fixed <commit>`, `rejected` or `deferred <home>` |
| `regression:` | `regression: round-(?P<round>[1-9][0-9]*)(?:#(?P<finding>[1-9][0-9]*))?` | a finding | at most one | a reference is `round-<N>#<n>` or `round-<N>` |
| `reopens:` | `reopens: round-(?P<round>[1-9][0-9]*)#(?P<finding>[1-9][0-9]*)` | a finding | at most one | a reopened close is a finding's, so the reference is `round-<N>#<n>` |
| `answer:` | `answer:(?: .*)?` | a finding | one | an answer is prose after the label |
| `## Confirmations` | `## Confirmations` | the record | at most one | each entry is a `confirms:` line at the start of a line, then its prose |
| `confirms:` | `confirms: (?:none\|round-(?P<round>[1-9][0-9]*)#(?P<finding>[1-9][0-9]*))` | `## Confirmations` | any | it is `round-<N>#<n>` or `none` |

| Old spelling | Means |
|---|---|
| `Target SHA:` | `target:` |
| `refixes:` | `regression:` |
| `fix of a fix:` | `regression:` |

**`chain_check.py` reads the two tables from this section and stops at
exit 2 where it cannot.** It loads them once, when it is imported, from
`docs/the-review-record.md` beside itself, which every copy of the plugin
carries, the hygiene workflow's clone among them. It finds each table by this
section's heading and the table's header row. A document it cannot open, a
section or a header row it cannot find, and a row it cannot read stop it at
exit 2 naming this file, never a pass. An old spelling's row it cannot read
is one whose cell is not one code span, whose `Means` is no label of the
first table, whose `Old spelling` is one, or which names a spelling a row
above it names. A row of the first table it cannot read is one whose
shape does not compile, whose `Where` or `How many` is a word the table does
not use, a row the check reads a meaning from that is missing, one whose
shape lacks the named part, such as `(?P<commit>…)`, the check reads out of
it, or one that stands where the check does not look for it or whose
`How many` the check cannot keep. `target:` stands outside every finding
and is `one`, and `original:` stands there and is `at most one`. `location:`, `verdict:`, `regression:` and `reopens:` stand in
a finding, and since the check reads one line of each, the first two are
`one` and the last two `one` or `at most one`. `confirms:` stands in
`## Confirmations`. Every other row may take any `Where` and `How many` the
table uses for its kind, because the check counts each: a section, or a
line in a section, that the table says is `one` is refused where a record
leaves it out, `## Confirmations` included. So a change that moves this
heading or either table moves the loader's path in the same commit, or
every check that reads a record stops.
check: tests/test_chain_check.py

**A finding's `verdict:` decides it, and severity is for people.** The
warden writes `open`; the fix pass answers with `fixed <commit>`,
`rejected` (the finding does not hold, and `answer:` says why) or
`deferred <home>`. `severity:` is `must` (fix before merge) or `should`
(fix, or say why not); the check holds it to its row and decides nothing on
it. What this round confirmed holds is a `confirms:` entry of
`## Confirmations`, and what it could not judge a row of `## Not judged`
with who answers it; neither is a finding. A wrong sentence an agent reads
and acts on is `should`; a sentence in a record that merely reads badly is
not a finding.
check: tests/test_chain_check.py

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
check holds the line to its row and reads nothing out of it. A backtick
ends a command on the line, so a command that holds one is written and run
with `$(printf '\140')` in place of the character, and the line names the
command the round ran.
check: tests/test_chain_check.py

**A claim of absence is `executed` only.** A finding that says something is
missing, that nothing catches, calls or states it, names the search that
found nothing, because no coordinate opened can show an absence. The check
reads the line's shape and never whether a claim is one of absence; the
warden who writes the line and the round that reads it judge that.
check: none reader: the warden and the next round

**A later round re-runs an `executed` line rather than re-deriving the
claim.** Where it weighs an earlier finding, it runs the commands the line
names again. A probe the line names was deleted under the agent contract's
probe rule, so the round writes it again from its `## Probes` row. The sealer weighs no finding: a finding's verdict is the
check's to read (`agents/sealer.md` step 3).
check: tests/test_review_axes.py

**The fix pass writes two lines per finding and nothing else in the file.**
It rewrites the finding's `verdict:` line, with the commit for `fixed`, and
writes its `answer:` line: what was done, why the finding does not hold, or
where it went. Where its fix went to a path `location:` does not name, it
appends that coordinate to the line, joined by `, `, and its answer says so.
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
check: tests/test_chain_check.py

**Every round file stays, so a finding can be followed from the round that
found it to the commit that closed it.** The next round's warden reads the
earlier records directly; nothing summarises them. They leave with their
work item's directory, which the settle after its release removes.
check: tests/test_settle.py

**`target:` names a commit, not a content anchor, because a round records a
moment.** The record's one `target:` line names the reviewed commit, with
the base a round that read the branch read it against, or the fix range a
verifying round read. A squash orphans the commit after the merge, and the
check reads it only while the branch that holds it is open.
check: tests/test_chain_check.py

## What the check reads at the pull request

**`chain_check.py` reads the declaration, the frame, the `## Rule changes`
section of each `spec.md` it parses, the records, the broad gate's
file, the sealer's guarantee, the `SpecSeal-Routing` trailers of the pull
request's own commits and, where `seal/parity.md` is declared, the
migration config's `Baseline commit`, and nothing else of a round
record.** It judges the
`routing.md` naming the pull request's branch and every one its own commits
add or change. A ready pull request fails on any refusal, each named
`path:line  why`; a draft, or a run that observed no pull request, prints the
same lines and exits 0.
check: tests/test_chain_check.py

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

**Of a round record the check reads its labelled lines, and refuses what it
cannot read.** It reads every line *The round record*'s table has a row
for, and a ready pull request fails for any line that table refuses. It
fails, too, while a finding reads `open`; for a `fixed` naming a commit HEAD
does not descend from, or one that changed no located path; for a reference
naming no earlier record, or a finding that record does not hold, and any
reference in round 1; and for a `fixed` or `rejected` finding the next
record names on no `confirms:`, `reopens:` or `regression:` line. A labelled
line inside a fence is not a line, so a finding whose only verdict stands
in its fix block has none, and a fence that never closes, which would hide
every finding after it, is refused at the line that opened it. A line
outside every fence that begins with `<!--` is refused at its line, because
the check reads a comment as text. Each refusal names the record, the line and the
finding's heading. No emoji is read, and neither severity nor answer
decides anything. It errs two ways where the
shape holds and the fact does not: a `fixed` commit that touches a named
path and fixes nothing passes, and the verifying round's warden, whose
`confirms:` line the check then requires, is who reads the fix; and a fence
closed on the wrong line hides the lines between it and its false closer
without being unclosed, which the orchestrator's reading of each record
against the template and the next round's reading of the earlier records
are there to catch.
check: round-record-read-by-label

**The last record is at HEAD, or only the work item's own records follow
it, and none of its findings is `fixed` or `rejected`.** A commit after the
last record's `target:` commit that touches a file outside
`seal/specs/<id>/` is a fix nobody reviewed, and the refusal names it and
says a verifying round is owed. So is a `fixed` or `rejected` finding of the
last record, since no round after it read the fix or the rejection; a last
record whose findings all read `deferred <home>`, or that holds none,
passes.
check: last-record-at-head

**The broad run has one home, `broad-gate.md`, on either routing answer.**
`broad-gate --record <item>` writes `<tree> against <base>` there on a green
run, newest first, every earlier run kept behind it as `; earlier run: …`. At
a ready pull request its newest run is HEAD, or only the work item's records
follow it.
check: tests/test_broad_gate.py tests/test_chain_check.py

**The check reads no record of the old table's shape.** It opens the
records of the work items this pull request's own commits declare or change
and no other, so a record a merged pull request left behind is never judged
at a pull request again, whatever its shape. Two readers outside the check
still open merged records: `.github/scripts/release_seal.py#chain_counts`
reads every record of a release with the `chain_check` of the tree it runs
from, and `evals/scripts/replay_targets.py` reads each labelled record with
the `chain_check` of the commit that last wrote it. One of the old shape
under an item this pull request carries has no `## Findings` section, and is
refused by name. A
work item in flight across a change to the table meets the change as its
records stand: a renamed line is rewritten into its new spelling, and an
added line is never supplied after the round that would have written it, so
an item whose records predate an added line merges before the change or has
its rounds written after it. A record written before a line was added lacks
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
check: tests/test_chain_check.py

**The check parses the `## Rule changes` section of the `spec.md` of
every work item whose `routing.md` it judges, and of every work item
`spec.md` the pull request's own commits add or change, with
`skills/settle/scripts/rule_changes.py`, the one reader of that
section, and a section the reader refuses is a refusal at the line the
reader names, carrying the reader's reason.** `settle` groups the
released specs by the sections their rule changes name, and a spec
whose section does not parse joins no group, so a section first read
there is a rule change the settle can place only by reading the whole
spec, with no pull request left to fix it in. A
declared work item can edit another work item's section without
touching that work item's `routing.md`, which is why the diff is read
as well as the declarations. A pull request that declares nothing
reads no `spec.md`. A `spec.md` a squash of another pull request
carried, and one the pull request only moved, are read at the pull
request that made them. A `spec.md` with no `## Rule changes` section
is left alone here, and the settle reads such a spec whole. The refusal
reads a fact from the file and puts no question to a person.
check: rule-changes-read-at-the-pull-request

**Where `seal/parity.md` is declared and the change reaches outside
`docs/` and `seal/`, every round record of a work item declaring
`through the review chain` carries one `original:` line naming the
migration config's baseline.** The check reads `seal/parity.md` at HEAD
and the paths the pull request changes against its base, through the
parity arm's own rule for a change confined to the document roots. A
diff it cannot read ends the check with exit 2 before any record is
judged. A ready pull request fails while a round record holds no
`original:` line, or holds one whose commit and the
`Baseline commit` row's SHA are not one a prefix of the other, and a
migration config whose `Baseline commit` holds no SHA fails it too. Each
refusal names the record, or the config, and both commits where two are
compared. The warden writes the line in the round where it compared that
round's target with the original through `legacy-parity`. A round that
could not resolve the original writes no line and raises an `unread`
finding, so the refusal stands until a round compares. What the check
cannot read is whether the comparison was a good one, which is the
warden's, as it is for the parity mark.
check: parity-at-the-pull-request

**Where `seal/parity.md` is declared and the change reaches outside
`docs/` and `seal/`, the `guarantee.md` of a work item declaring
`straight to the PR` carries one `original:` line naming the migration
config's baseline.** The sealer writes it after comparing the audited
commit with the original through `legacy-parity`, and the check reads it by
the rule a round record's line is read by: a ready pull request fails while
the guarantee holds no such line, or one whose commit and the
`Baseline commit` row's SHA are not one a prefix of the other. What the
check cannot read is whether the comparison was a good one, which is the
sealer's.
check: parity-in-the-guarantee

**On every pull request, the check reads the `SpecSeal-Routing` trailer of
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
of the smith and the warden, that the work before it holds.** Its
reference is the issue body and the tree, never an agent's word or the
orchestrator's summary. It runs after the pull request body and the
changelog fragment are written and the orchestrator's broad run has written
`broad-gate.md`, on both routing answers; it reads that record and runs
nothing broad, and its order of work is `agents/sealer.md`'s.

**It checks a claim against the fact, and the parties against each other.**
The acts are `agents/sealer.md` step 3's and step 4's, and this section
names none of them, so the list has one home. Each act is one row of
`## Claims re-run` or `## The parties` in `guarantee.md`. It does not
re-judge the design or the code's quality.
check: tests/test_the_sealer_guarantees.py

**Its verdict is `guarantee.md`, from `templates/sdd-guarantee.md`**: the
commit and base, the broad gate's result, the claims re-run, the parties
compared, and one `Verdict:` line, `sealed`,
`withheld reason: <the claim, its party, its coordinate>` or
`undecided question: <the question, for the owner>`, written exactly so
and with no emphasis. Any other spelling of the line is refused at it.
The `Target SHA` row holds `<sha> against <base>`, each one word, then
nothing or one `; earlier run: <sha> <word>` entry per earlier run, with
`against <base>` after its SHA where it names one and its verdict's
word alone; any other text on the row is refused at it. An undecided question is the owner's: the
answer goes on a line under the verdict, and the sealer runs again at the
new HEAD.
check: tests/test_the_sealer_guarantees.py tests/test_chain_check.py

**A ready pull request passes only where `guarantee.md` names HEAD and reads
`sealed`.** Only the closing records, `broad-gate.md` and `guarantee.md`,
may follow the commit it names, since every other file on the branch is one
the sealer audited. `withheld`, `undecided`, an unfilled template, two
`Verdict:` lines or a stale commit each fail naming the file; a draft prints
them. A word the verdict used before it read `sealed` fails naming its line
and saying the word changed.
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
`seal/specs/<id>/guarantee.md` under either root. Where its one `Verdict:`
reads `sealed`, it writes the stamp's values under
`<git-common-dir>/specseal-stamp/<session>/` for the payload's session,
which a subagent's write carries as the main session's, and says one line
naming the file and `seal-stamp --from <path>` as its message. A `Stop` hook draws each undrawn file
of its own session once, after that turn's text, and a subagent's end draws
nothing. `withheld` and `undecided` queue nothing. Once per work item is held
by what the clone and the tree carry, with no count beside them: a values
file already named for the work item, pending or drawn, under any session's
directory is not written twice, whatever commit it named; a `sealed` whose
audited commit is not an ancestor of the branch the work item's `routing.md`
names queues nothing; and in shared mode a guarantee that read `sealed` at
an earlier commit of HEAD's history, or whose `Target SHA` row's `; earlier run:`
chain reads `sealed`, counts as stamped then, which holds across clones; the
earlier-run chain alone skips a `sealed` this clone recorded refusing (the
next rule). It does
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
or drawn, is a complete record of its stamp in that clone. There once is
held by that, by the `Target SHA` row's earlier-run chain, and by the audited
commit being an ancestor of the branch the work item's `routing.md` names in
its `Branch` row, a branch the clone must still hold. That last keeps a
`sealed` written long ago quiet, since a local-mode work item stays under
the root until the settle after its release removes it; one whose branch still stands draws late, once, at its first edit. The
stamp carries what the records say: the audited commit and its branch, the
base, the work item, the newest broad run and the count of round records.
check: stamp-drawn-once

**A `sealed` refused because its audited commit is not on the branch leaves
a refusal record in the clone that refused it, and the earlier-run chain
skips a `sealed` this clone recorded, so the sealer's new audit draws the
work item's one stamp.** The new audit keeps the refused verdict on its
`Target SHA` row as `; earlier run: <sha> sealed`, and without a record the
chain would count that entry as the stamp. The record is an empty file,
`<git-common-dir>/specseal-stamp-refused/<id>-<target>`, beside the values
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
leaves it for `seal-stamp --from`. `seal-stamp` is not budgeted, because it
is no hook's message.
check: tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/test_sealer_stamp.py

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
that landed row as stale. The hook judges a write's newest verdict
alone, never the `; earlier run:` chain, so a `sealed` that drew and whose
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
the edit hook's message names `seal-stamp --from <path>`, and a stamp that did not appear is drawn by
hand from it, once. Where none was, the pull request's check is what says the
work item was sealed.
No case, hook or workflow can observe a screen.
check: none reader: the owner on the first real run after a change here

## The run

**A run ends with a verifying round.** It is spawned after the last fixes are
committed; its target is the diff of those fixes, new units included; it
asks of every finding marked closed whether the fix holds, and says so on a
`confirms:` line where it holds, and where it does not on a finding's
`reopens:` line, or its `regression:` line where a fix pass's own commit
made the defect. A round opening nothing that needs a fix does not count
toward the cap: the cap stops a loop that is not converging, and such a
round is the loop having converged.
check: run-ends-with-verifying-round

**A run has three finding rounds by default, counted from the last design
change, and extends one round at a time while the findings shrink.** A
design change is a reframe, or a new phase the owner approved in `plan.md`,
so the first finding round that reviews new work starts the count again at
one, whatever the record's number. Past the third round of the count the
orchestrator spawns one more finding round only while the latest round
found fewer findings than the one before it and none of them is a
regression. A regression routed to a fix pass is followed by one verifying
round, whatever the count, which reads that fix and is not an extension. A
second regression it finds on the same unit goes to the framer, as the next
paragraph says, and anything else it leaves open past the cap takes the
ladder. Each extension is one line in that round's record, written by the
warden from the reason the spawn prompt gives:

```
Extended past round 3, counting from round 1: round 3 found 2, round 2 found 4, and none is a regression.
```

At the cap every finding still open takes the filing ladder below and reads
`deferred <home>`. No person is asked mid-run.
check: tests/test_the_rules_have_one_owner.py

**A regression is routed by comparing the fix with the frame.** A
regression is a defect a fix pass's own commit introduced. Where a finding
stands in a unit a fix pass's own commits added or changed, and those
commits introduced its defect, the warden writes its `regression:` line,
naming the finding whose fix made the unit
as `round-<N>#<n>`, or that round as `round-<N>` where no finding named the
unit, and names the unit first in the grounds. Then one sentence of the
grounds says what the frame says, from the phase's `plan.md` row and
`spec.md`, what the fix did, and where the defect came from. No label
carries that sentence, and the orchestrator routes the round on it, at any
round of the run. Where the fix built what the frame says and the defect is
still there, the frame is wrong, and the round gets no fix pass: the work
item goes back to its framer, who writes
`Reframed <date> by <who>, after round <N>.` under the mark at the foot of
`spec.md`, and the run goes on with the redesign's build and its rounds.
Where the fix departed from the frame, or the defect came from how the fix
was written, a paste-ready fix taken from a review record among them, the
round gets an ordinary fix pass, and the smith is told what the frame says.
A second regression on the same unit after a fix-pass route goes to the
framer whatever the comparison says. A defect in a unit a build phase made,
one the framer designed and the owner approved in `plan.md`, is an ordinary
finding of new work, with no `regression:` line, even where the round that
finds it reads that phase. A close that does not hold where no fix pass's
commit made the defect, a `rejected` finding that holds after all or a
`fixed` commit that left the defect standing, in the unit that commit
changed or in another, is raised again as an ordinary finding with a
`reopens:` line naming it, and gets its fix pass.
check: tests/test_the_rules_have_one_owner.py

**A leftover finding takes the first rung that fits.** A new issue is the
third rung, not the default:

| Rung | When it fits | Where the finding goes |
|---|---|---|
| 1 | the branch owns the unit, or the smith answers the finding with grounds | the diff, or the round record with the grounds |
| 2 | an open issue already owns the ground | a comment on that issue; the verdict reads `deferred #N` |
| 3 | the finding names a party who agreed to act on it | a new issue labelled `from-review`, or a `seal/follow-up.md` row where there is no tracker; the verdict reads `deferred #N` |
| 4 | it names nobody | the round record alone, and the pull request body |

check: none reader: the sealer at every deferred verdict

**On a branch whose `routing.md` reads `Automation` `yes`, the
question tool is refused on every call.** The person who answered the
routing question was promised that nothing stops to ask, and a
question put at minute thirty waits for somebody who is not there.
The session builds on the default the question states, records that
default in the work item's `questions.md` as one row, and names it in
the pull request body, where the owner can overturn it. The routing
question put alone, single-select and with its text, goes through
while this session's transcript can be read and holds no answer to
it from this clone, because a run resumed in a new session has to
put question 1 again for the gates that read the press; once it is
answered, it is refused like any other question. Any routing answer
from this clone in the session spends the exemption, including one
given for another work item, so a session that has already answered
for another branch cannot put question 1 again; that is outside the
one-issue flow. The declaration is read through `hooks/routing.py` for the
branch checked out where the session sits, and every way of not
reading it is the attended answer. The file is written by the model,
which is why the worktree guard never reads it as consent. It is read
here only to refuse, so a row the model forged binds only the model,
and a row edited to `no` is in the diff the review reads. A session
sitting in a checkout whose branch is not the declared one is not
held, and neither is a question asked as plain text. A gate whose own
reason says to ask with the question tool meets this refusal too, and
its question states no default: the session takes none of the ways on
that question offers, and hands the stop back at the end of the run.
check: tests/test_question_gate.py

## The handoff

**The orchestrator hands an agent coordinates, never prose.** A fact carries
the coordinate that makes it falsifiable — the line, the grep that returned
nothing, the test whose assertion constrains the wording — or is labelled
`executed`, `read` or `unverified`. An aggregate is not a coordinate: a count
can be checked while the claim it stands for cannot. A claim that flips on
where it is measured says where; a command with two forms names the one it
means and what the other is for; a runner the repository ships is named, not
typed into every prompt, and the form handed over is the narrow one.
check: tests/test_the_handoff_before_round_one.py

**While an agent runs, `plan.md`'s Status column is the readout.** The
implementer fills it with the commit that closed each phase, so the
orchestrator opens it rather than asking, and the stall signal is the time
since it last advanced. After the run, `skills/verify/scripts/session_cost.py`
reads the transcript.
check: tests/test_the_handoff_before_round_one.py

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
check: tests/test_the_handoff_before_round_one.py

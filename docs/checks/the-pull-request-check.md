# The pull request check

What `skills/code-review/scripts/chain_check.py` reads at a pull request, for
a person who changes it; the sealer cites its code.

## What the check reads at the pull request

**`chain_check.py` reads the declaration, the frame, the `## Rule changes`
section of each `frame/design.md` it parses, the records, the broad gate's
file, the sealer's guarantee, the `Seal-Routing` trailers of the pull
request's own commits and, where `seal/parity.md` is declared, the
migration config's `Baseline commit`, and, against a design's
operations, the string constants of the test files under `tests/` and
the rule documents, and nothing else of a round record.** It judges the
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

**Of a round record the check reads its `seal` blocks and its finding headings, and refuses what it cannot read.** It reads every block `docs/forms/the-round-record.md` *The round record* describes, and a ready pull request fails for any line that grammar refuses. It names each file under `trail/rounds/` whose name is no `round-N.md` as one it did not read, so a record under another name is a line of the check's output and never a silent pass, and it names each fence whose info string's first word, case folded, is `seal` and whose opener is not the block's, which changes no exit code. It fails, too, while a finding has no close block; for a `fixed` naming a commit HEAD does not descend from, or one that changed no path the finding's or its close's `location:` names; for a reference naming no earlier record, or a finding that record does not hold, and any reference in round 1; and for a `fixed` or `rejected` finding the next record names on no `confirms:`, `reopens:` or `regression:` line. A `seal` block inside another fence is part of that fence, so a finding whose block stands inside its fix block lacks its finding block and is refused for it, and a whole finding written inside a closed fence is no finding: the orchestrator's read of the record before its commit, against the template, is what catches it. A record written before the fields stood in blocks holds no round block, and is refused with one message naming the template. A fence that never closes, which would hide every block after it, is refused at the line that opened it. A line
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

**The last record is at HEAD, or only the work item's own records follow it, and none of its findings is `rejected`, nor `fixed` with a path beyond the work item's records in its `location:` or in its commit.** A commit after the last record's `target:` commit that touches a file outside `seal/threads/<id>/` is a fix nobody reviewed, and the refusal names it and says a verifying round is owed. So is a `rejected` finding of the last record, a `fixed <commit>` whose commit touched any path outside `seal/threads/<id>/`, and a `fixed` finding whose `location:` names any path outside `seal/threads/<id>/`, whatever its commit touched, since no round after it read the fix, the rejection or the code half of the finding. A `fixed <commit>` finding located in the work item's own records alone and fixed by a commit that touched them alone passes: the sealer reads every record at HEAD (`agents/sealer.md` step 2). A last record whose findings all read `deferred <home>` or such a `fixed`, or that holds none, passes.
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
is accepted (`docs/checks/the-fold.md` *The fold, and what tells it from a
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
each of its own commits, as `docs/checks/the-routing-check.md` *At the pull
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

**Each check line inside an `add` or `change` `to` of a design whose
`## Rule changes` the check parses is read by `.github/scripts/rules.py`,
the reader `seal rules --check` uses, and a line that reader refuses is a
refusal at its line in the design, carrying the reader's reason.** The
settle writes each `to` into the policy root as it stands. Where that
root is `docs`, `seal rules --check` first reads the line there, and a
line refused there has no pull request left to fix it in. A line that
opens like a check line and is not one is named at its line as not read
and refuses nothing. A `from` is read for no check line,
since the settle writes none into the policy root.
check: a-check-line-in-a-to-is-read-at-the-pull-request

**For each operation of a design whose `## Rule changes` the check
parses, the check names the test pins and the copies the settle will
make, each as a notice at the operation's line in the design, and
refuses nothing for them.** A pin is a string constant of at least four
words in a Python file under `tests/`, read through `ast` with its
docstrings left out, that a `from` holds, or the section a `remove`
with no `from` takes out, and that the `to` does not hold. A copy is a
run of 15 words a `to` shares with another rule document, read as
`tests/text/test_no_passage_is_pasted_into_a_second_file.py` reads one,
through `skills/settle/scripts/passages.py`. A design's operations
reach the policy root only at the settle, so without the notice a pin
and a copy meet the suite first there, after the pull request that
could answer them has merged. The proofer weighs each notice at review.
A pin of a rule's wording and a copy another file keeps after the
settle are findings, and the settle repoints a pin of a fact. A
source the reading cannot read, a test file, a rule document, a
section a `remove` names or a file listing, is named as not read. A pin
the reader cannot list, such as a literal built at run time, meets the
suite at the settle's broad run.
check: a-rule-change-names-the-pins-and-copies-it-breaks

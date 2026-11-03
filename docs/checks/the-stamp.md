# The seal stamp

What `hooks/sealer-stamp.py` and `skills/verify/scripts/seal_stamp.py` draw,
for a person who changes them; no agent acts on it.

## The stamp

**The stamp is drawn once per work item, from the sealer's `sealed`, at the
end of the turn in which `guarantee.md` came to read it, at its write, in
either mode.** The stamp means every party
verified the work item, the sealer last, and the work is done, so it is
drawn from that verdict and never from the broad gate's run, which comes
before the sealer has read anything and draws nothing
(`docs/running/the-broad-gate.md` *One act, one owner*). A `post-edit` gate,
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
check: tests/hooks/test_sealer_stamp.py

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

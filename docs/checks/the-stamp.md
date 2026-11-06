# The seal stamp

What `skills/verify/scripts/seal_stamp.py` draws, and the one hook a person may
install to draw it, for a person who changes them; no agent acts on it.

## The stamp

**The stamp is drawn once per work item, from the sealer's `sealed`, at the end
of the main session's turn after the sealer queued it, in either mode, where
the person installed the stamp's `Stop` hook.** The stamp means every party
verified the work item, the sealer last, and the work is done, so it is drawn
from that verdict and never from the broad gate's run, which comes before the
sealer has read anything and draws nothing (`docs/running/the-broad-gate.md`
*One act, one owner*). The plugin registers no hook. The sealer runs
`seal stamp --guarantee <path>` once, after it writes `guarantee.md` with
`Verdict: sealed`, under either root. Where the reader the pull request's check
reads it through refuses none of its lines and its newest verdict block reads
`Verdict: sealed`, the command writes the stamp's values under
`<git-common-dir>/agentic-stamp/` of the clone the path is in, and prints one
line naming the file and `seal stamp --from <path>`, which the sealer's
hand-back carries to the orchestrator. The queue is keyed by the clone and by
nothing else, so the stamp script reads no environment variable. The `Stop`
hook runs `seal stamp --stop`, which draws each undrawn file of the clone the
payload's `cwd` is in, once, after that turn's text, and a subagent's end draws
nothing. `withheld` and `undecided` queue nothing. Once per work item is held
by what the clone and the tree carry, with no count beside them: a values file
already named for the work item, pending or drawn, in the clone's values
directory is not written twice, whatever commit it named; a `sealed` whose
audited commit is not an ancestor of the branch the work item's `routing.md`
names queues nothing; and in shared mode a guarantee that read `sealed` at an
earlier commit of HEAD's history, or one of whose earlier verdict blocks reads
`sealed`, counts as stamped then, which holds across clones; the earlier blocks
alone skip a `sealed` this clone recorded refusing (the next rule). A guarantee
in the history that holds no verdict block, written before the fields stood in
blocks, counts nothing. It does not hold for a `sealed` committed over a
history that carries no earlier `sealed` in a clone that holds no values file
for the work item, which draws the stamp again in that clone: the sealing
commit amended or rewritten there over its own parent, or a second seal on a
copy of the branch that had not fetched the first. A `sealed` that drew in
another clone, brought onto a copy of its declared branch that does not hold
its audited commit, by hand or by `checkout`, `cherry-pick -n` or
`merge --squash`, is refused when it is queued and recorded, and the new audit
the refusal asks for draws again there; it joins that class. The clone that
drew the stamp keeps its values file, so an amend there draws nothing. That is
a stated limit, since across clones the history is the only record the rule
reads, and nothing beside the tree counts stamps. In local mode no history is
read, because none exists: the root and the values directory share the common
dir, so a values file for the work item, pending or drawn, is a complete record
of its stamp in that clone. There once is held by that, by the earlier verdict
blocks, and by the audited commit being an ancestor of the branch the work
item's `routing.md` names in its `Branch` row, a branch the clone must still
hold. That last keeps a `sealed` written long ago quiet, since a local-mode
work item stays under the root until the settle after its release removes it.
The stamp carries what the records say: the audited commit and its branch, the
base, the work item, the newest broad run and the count of round records.
Two limits follow from the queue's key. Where two sessions work in one clone,
the one whose turn ends first draws every stamp pending there. A values file an
earlier release wrote into a per-session directory under
`<git-common-dir>/agentic-stamp/` is neither drawn nor counted, and
`seal stamp --from` draws it by hand.
check: stamp-drawn-once

**A `sealed` refused because its audited commit is not on the branch leaves a
refusal record in the clone that refused it, and an earlier verdict block
reading `sealed` that this clone recorded refusing is skipped, so the sealer's
new audit draws the work item's one stamp.** The new audit's block stands below
the refused verdict's block, and without a record that earlier block would
count as the stamp. The record is an empty file,
`<git-common-dir>/agentic-stamp-refused/<id>-<target>`, beside the values
directory and never listed with it. One writer leaves it, for a row that stands
in its own clone and nowhere else: `seal stamp --guarantee`, in either mode,
where the `Branch` row's branch stands and does not hold the audited commit. It
says one line naming the commit and the branch. In shared mode the pull
request's check refuses the same row as stale; in local mode no check reads it.
A recorded target matches a SHA when one is a prefix of the other and both are
at least seven characters long; any other spelling finds no record, and the
verdict counts as stamped. `sealed_before` skips a `sealed` this clone recorded
refusing, as the earlier-run chain does, because nothing stops a refused row
from becoming history before the pull request's check refuses it; any other
`sealed` in the history drew where it was made, and counts. So a `sealed` that
drew, went stale under a rebase and was refused when it was queued again still
holds the work item's stamp, and its repair draws nothing.
check: refused-sealed-leaves-a-record

**The stamp's `Stop` hook is the person's, written on their yes, and the
plugin registers none.** `seal stamp --install <data-dir> --settings <file>`
writes a Python launcher, `<data-dir>/stamp.py`, that runs
`<plugin root>/skills/verify/scripts/seal_stamp.py --stop` by the absolute path
of the root the command ran from, and merges one `Stop` entry whose command is
`python3 "<data-dir>/stamp.py" || py -3 "<data-dir>/stamp.py"` into the
settings file, leaving every other key and adding nothing where that entry
stands. A settings file that does not parse as a JSON object is refused with
exit 2 and left as it is. `seal stamp --remove <data-dir> --settings <file>`
takes that one entry and the launcher out, and nothing else.
`seal stamp --decline <data-dir>` writes an empty `<data-dir>/stamp-declined`,
the record of a no, which `--install` removes. `seal stamp --hook <data-dir>`
prints `installed <root>`, `declined` or `neither`. The data directory is
`${CLAUDE_PLUGIN_DATA}`, which a skill body receives substituted and which
Claude Code keeps across updates; the settings file is
`${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json`, which the shell expands.
The command reads neither from its environment. The question "draw the
sealer's stamp in your terminal?" is put once, where neither the launcher nor
the marker stands: in `skills/implement/bootstrap.md`'s batch at first setup,
and in `/agentic:update` for a person set up before. Where the launcher stands,
`/agentic:update` runs `--install` again from the installed copy, so it names
the new root. The launcher exits 0 whatever happens, since a `Stop` hook that
exits 2 keeps the turn going, and one naming a root that is gone draws nothing.
A person who updates by `claude plugin update` alone keeps a launcher naming
the old root, which stays on disk and draws until the next `/agentic:update`;
`seal stamp --hook` says which root it names.
check: tests/skills/test_seal_stamp.py

**`--stop` holds its whole message under a limit named in the code, and steps
the drawing down rather than letting the harness persist it.** The harness
writes a `Stop` hook's `systemMessage` longer than 10,000 characters to a file
and shows the person a 2 KB preview, so a stamp past that size is not seen.
`seal_stamp.MESSAGE_LIMIT` is that number, measured with a scratch hook, and
nothing else shares the message. The harness counts UTF-16 units, so a
character outside the BMP is two, and so does `--stop`. One message carries as
many of the oldest pending stamps as fit together with their disc. A stamp has
two rungs, with its disc and then without it: the owner's disc is drawn 28
cells across and has one size, so there is no smaller disc to step to, and no
scale either. That disc is most of a stamp's size, so one stamp of a real work
item's size goes out per message and a second waits for the next turn. A seal
past what one message can carry stays pending and is drawn at the next turn's
end, and a single stamp that does not fit with its disc by itself is the only
one drawn as the text block with no disc. A stamp can come out without its disc
or a turn later, and a session that ends first leaves it for
`seal stamp --from`. `seal stamp` is not limited, because it is no hook's
message.
check: tests/skills/test_seal_stamp.py

**What the person's screen shows is not checked, and neither is the order of
the text above it.** The cases prove that `--stop` emits the right bytes for
the right payload. A screenshot of the probe proved once that such bytes render
unfolded, in colour, after the turn's final text, and the owner's spike of
2026-11-06 proved a `Stop` command hook in the person's own settings runs as a
plugin's did. Whether a given work item's stamp was seen, and whether the
orchestrator wrote its result in the turn the stamp closed, are read by the
person and by nobody else. So is how the stamp reads on a light background as
well as a dark one. Nothing outside the disc is painted, so its text is in the
terminal's own colours and theme — dim labels, a green `✓`, the title in the
stamp's red — and the owner reads the first real stamp on each background. The
line reaches the person through the sealer's hand-back and the orchestrator's
quote of it, and nobody has watched a stamp the installed hook draws on a
screen yet.
**Nor is the drawer's silence where it cannot draw.** No stamp is queued, and
nothing is said, for a `guarantee.md` the sealer wrote without running
`seal stamp --guarantee`, as a sealer of an earlier release does, or one that
arrived by a commit fetched from elsewhere or `seal import`; or for a verdict
whose work item names no branch, or a branch the clone no longer holds. A
`sealed` over a commit the branch does not hold still counts as the work item's
stamp, so its repair draws none, where nothing queued it: by a person, or under
a sealer that runs no `--guarantee`. The pull request's check still refuses
that landed row as stale. `--guarantee` judges the file's newest verdict block
alone, never the earlier blocks, so a `sealed` that drew and whose audited
commit a later rebase, amend or cherry-pick moved out of the history counts as
stamped, which it is. In local mode the record is the clone's own: a values
directory emptied by hand, or a guarantee brought by `seal import` from a clone
that drew and re-sealed here, draws again. A wrong row that names, by
coincidence, the very commit a copy of the item on another branch was sealed
and drawn over draws a second time once `--guarantee` refuses and records it,
a class this rule accepts as a second run of the item. So does a `sealed` that
drew in another clone and was brought onto a copy of its declared branch that
does not hold its audited commit, whatever brought it: `--guarantee` refuses
and records it, and the new audit it asks for draws again. No guard can tell
that copy from a stale row the same clone wrote after a push and a rebase.
Nothing draws, and nothing says so, where the person installed no hook or
declined it; where the `python3` the harness finds cannot load
`seal_stamp.py`; where the main session's working directory is outside the
clone the stamp was queued in; or where the launcher names a root that is
gone. Where a file was written, the line `--guarantee` printed names
`seal stamp --from <path>`, and a stamp that did not appear is drawn by hand
from it, once. Where none was, the pull request's check is what says the work
item was sealed.
No case, hook or workflow can observe a screen.

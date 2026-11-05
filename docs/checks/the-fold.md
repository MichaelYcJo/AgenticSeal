# The fold

What `seal settle` and `seal fold` read to tell a settle from a deletion, for
a person who changes them and for the settling session.

## The fold, and what tells it from a deletion

The procedure is `skills/settle/SKILL.md`. This section holds the rules its
readers share.

**A work item directory a pull request removes whole is a settle, not a
deletion, where the directory stood at the merge base.** A settle removes
released directories whole, and no other step of the workflow removes
another work item's directory, so the whole removal is the fact the readers
read. What the settle wrote into `docs/` is not read here: the settling
session writes each section in its own words, a reader could only guess at
that from words, and the settle's pull request states each decision for the
owner to review. A pull request that removes part of a directory, a
`gaps.md` from a directory that stays, or a row from a table is still a
deletion. One predicate, `unverified_check.py#settled`, answers
`seal unverified --baseline` and `chain-check`. A pull request outside a
settle that removes a whole work item directory reads as a settle too; its
diff shows the removal to its review.
check: a-settle-is-no-deletion

**A released work item leaves at the settle whatever it wrote, and the
settling session decides every open row of its record before it goes.** An
open `## Not verified` row is a claim with an answerer, and the rule it
qualifies reached users in the code with the release, so holding the
directory back stops nothing. The settling session reads each row against
the tree. A row naming a unit the tree no longer holds is moot; a row
another record or a later run already answered is answered, and the closure
names that record; a row naming a measurement no failure, report or
decision on record depends on is closed with that reason and opens
nothing; and a row naming a measurement something on record needs is
re-homed as an issue, or as a `seal/follow-up.md` row in a repository
with no tracker. A row that fits more than one kind takes the first
that fits, in this order, so only a measurement something on record
needs opens an issue, since an issue no record waits on is read only to
be closed. Each is closed in the record, `closed` with what closed it, and
`seal settle --apply` removes a directory only once its record holds no open row
in the working tree. The settle's pull request body carries every closure,
an issue carries every re-homed row, and git keeps the record. A released
work item that wrote no `frame/design.md` states no rule and goes the same way.
A file in its directory with the name of a record the settle reads, a
`gaps.md`, a `design.md` or a `plan.md`, at any path but that record's
own, is named by the dry run and by `seal settle --apply` as a file the
settle did not read. The settling session opens it and decides each item
in it that reads as an open row, as it decides a row. `--apply` decides
nothing on it and removes it with the directory. Keeping the directory
for it would take a file's name as a guess at what it holds.
check: tests/skills/test_settle.py

**The settle writes each section as the latest decision the released
designs state for it, checked against the code.** The designs whose rule
changes name one section, or a section holding it, are one group, and merge
order sorts it, so a group is that rule's history. Within a group the latest
design that states a rule decides it, and an earlier operation it restates is
superseded: it is settled with the group and not applied. Where the code
has moved past the latest decision, the code is the later fact and the
section states what the code does. The settling session writes the section;
an operation's `from` locates the text its design's framer read, and a
`from` that no longer matches is history, not a refusal. The rest of the
document stays as it was, and no marker is written. `settle` groups the
designs, shows each group's history and removes the directories. Run with
`--draft`, it first writes every released operation
into the policy root in merge order, a superseded one among them, where the
operation's design places it, and names each one it could not place with
the reason. The draft decides nothing: the settling session reads every
section it wrote against the code, as it reads a section it wrote itself,
and takes out what the latest decision does not keep.
check: tests/skills/test_rule_changes.py tests/skills/test_settle.py

**A settle is not a work item.** It opens no directory under `seal/threads/`.
Its session records `seal no-work-item` on the settle's branch, its commits
carry the trailer `Seal-Routing: no work item` where the root is shared,
and what it wrote is reviewed at its pull request. What it leaves already has a home, the pull request and
git history, so it keeps no log of its own. Were it a work item, each settle
would leave a directory for the next one to remove, and settling would never
end; `skills/settle/SKILL.md` *A settle is not a work item* is the procedure.
check: tests/text/test_settle_reads_before_it_removes.py

**A population floor over the records is replaced, never lowered.** A check
asserting that a sweep of `seal/threads/` read *enough* — `len(records) > 200` —
is answering *did the walk read anything* with a literal that stops being true
the moment the corpus shrinks, and a fold shrinks it by design. The repair
compares the walk against an independent listing of the same tree —
`git ls-tree HEAD` — which holds at any size, and a property the real corpus no
longer exercises moves to a record built in `tmp_path`. A repair is green
before the fold and after it; one green only once the directories are gone is
a lowering. `skills/settle/SKILL.md` *Answer every check that reads the
corpus* gives the three answers.

**A document with a `.ko.md` edition changes with it, heading for heading.**
The two editions are prose in two languages, so the check compares what is
language-neutral: the sequence of heading levels. Whether a Korean paragraph
says what its English one says is review's to read. `CONTRIBUTING.md` *House
rules* owns the rule.
check: tests/behaviour/test_both_editions_carry_the_same_folds.py

**Whether a line is live is asked by what the line does, and the four
readers that ask it give three answers.** These are all four readers, grouped
by the kind of line they read, with the cost each answer is chosen against.
check: tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py tests/hooks/test_routing.py

- **A line that HOLDS something — a claim or an anchor — is read on
  doubt.** The coordinate kernel's `quoted_lines`, which its `unquoted` and
  `markdown_lines` read through. A fence nobody closed is a malformed file
  whose lines are read, and a commented-out row is a parked claim and is
  read. What this protects is that a claim never leaves a record in silence.
  The wrong answer is loud instead: `BROKEN`, a refused name or exit 2, and a
  person answers it with an edit or a marker.
  check: tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py
- **A line that EXCUSES or DECLARES something — a `seal/config.md` row, a
  `routing.md` row — is not taken on doubt, except
  where a declaring reader keeps an older reading that took it.**
  `unverified_check.py#live_lines` parks a line inside any fence or comment,
  closed or not, and a line its two span readings disagree about.
  `hooks/lib/config.py#hidden_lines`, which reads `seal/config.md`, keeps,
  wherever its walk is unsure, the fence-only reading it gave before the walk:
  a row below a fence nobody closed declares nothing, and a row below a
  comment opener nobody closed is not hidden, because that reading never hid
  one, and the walk may miss no row the older reading saw. That row declares
  nothing either: `hooks/lib/config.py#config_table` refuses a
  `| Item | Value |` header inside an HTML block opened above it and never
  closed, because GFM renders no table there, so every item of that table is
  a refusal, which a hook reads as silence and a command prints with exit 2
  (`templates/setup/config.md` *Repository config*).
  `hooks/lib/routing.py#shown`, which reads a `routing.md` and is not one of
  the four, keeps the reading it gave before the walk the same way, and that
  reading hid nothing: a row below a fence or a comment opener nobody closed
  still declares there, unless a fence that closes holds it. Those
  `routing.md` rows are the places a line nobody wrote live declares
  something; at every other fence or comment,
  what this protects is that nothing is excused or declared by a line
  nobody wrote live. The wrong answer is a statement left unbound, a hook
  that says nothing, or a gate that asks.
  check: tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py
- **A line a record's rows are COUNTED on is blanked the same way on both
  sides of a comparison.** `unverified_check.py#readable` blanks fenced lines
  with the indices intact, and a fence nobody closed to the end of the file.
  It reads a comment as text, because a record carries none, and the reader
  that judges a record refuses a line that begins with `<!--`. So the working
  tree and the base revision count the same
  table, and the readers that judge a record refuse a hidden table as absent
  rather than read it as empty.
  check: tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py

No one rule serves all three kinds. The holding bias would let a
`seal/config.md` row quoted in an example declare a value nobody set, and the
excusing bias would drop a parked row without a word. A reader of a new kind of line is a
fourth answer, and it is argued against these three.

**A `seal/` root with no work item under it is the state a complete fold ends
in, and it reads as settled, never as unusable.** Git keeps no empty
directory, so the state is two: the tree that ran `seal settle --apply` holds an
empty `seal/threads/`, and a fresh checkout of that commit holds none. Read as
unusable, `settle` would exit 2 on its own finished work, and `seal unverified
--baseline` would read the root's own `threads` path as a typo when a person
runs it after the fold, and refuse a finished settle. Only that one path is
settled; any other missing path is still refused, which keeps a misspelt
path from passing in silence.
check: an-empty-root-is-settled

**In local mode a work item counts as released by its pull request's merge
commit, not by its directory's presence at a ref.** The directory sits under
the common git directory, where no ref holds it, so `settle` asks which pull
request from the branch its `routing.md` names has merged and whether
`--released-at` reaches that merge commit; `skills/settle/local-mode.md` *In
local mode* gives the states that leave a work item unreleased. The settling
session writes the committed policy root as in shared mode, and
`seal settle --apply` removes each released local directory whose record holds no
open row, with no commit holding what it removed. The settle's pull request
changes the policy root alone, so no check reads a removal there, and its
commits carry no trailer, as no local-mode commit does.
check: tests/skills/test_settle.py

**A directory a person names at the settle is read and never
written, and only the documents the person marks promote reach the
policy root.** A repository's decisions also stand outside `seal/`, in
architecture decision records, RFCs and another tool's spec files, and
nothing gathers them into the policy root on its own. So the settling
session asks the person, before its first edit, whether any directory
besides `seal/` holds decisions to fold. `seal settle --from <dir>`
lists every document of each directory named, placed in the timeline by
the commit that added it and the commit that last changed it. The
session proposes each document as promote or skip, with the section it
bears on and the grounds, read from the document and checked against
the code, and the person marks each row in one more question. A
promoted decision is written into its section as a released design's
is, and the section cites the document by its path. The settle's pull
request body states each row with its mark. No step writes, moves or
removes a file under a named directory, and `seal settle --apply`
removes only under `seal/threads/`. A first answer of "none" runs the
settle with no `--from`, and no configuration row names such a
directory. `skills/settle/SKILL.md` *The settling session's procedure*
is the procedure.
check: tests/skills/test_settle.py

**The settle removes a released work item's directory only once the
published note of the version that shipped it carries its entry.** Once
the directory goes, git history holds the fragment and the note is its
only other copy, so the settle is where a missing entry has to be found.
Which note is read, what counts as carrying an entry, and which work
items and repositories have no note to read are stated in
`skills/settle/SKILL.md` *What `--apply` does*. Where no note can be
read, the open-row rule alone decides, and the reason is printed.
check: tests/skills/test_settle.py

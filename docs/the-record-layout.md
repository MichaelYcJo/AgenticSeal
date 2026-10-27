# The record layout

Where each kind of record lives. Every kind of record this repository keeps
has one home, and this document is the index: one table per place, each row naming a file
or a file shape and the one question it answers. A reader looking for a rule
or a record opens this index and then one file.

It is a policy document. A file that states a rule this index gives another
home links to that home and does not restate it, because two copies of one
rule are one rule today and two after the first edit to either. Where a copy
is found, the copy is the defect.

## Every kind of record, at a glance

| Kind | Home | Size target | Index |
|---|---|---|---|
| The changelog | `seal/threads/<work-item-id>/changelog.md` while a work item is open; `changelog/<X.Y.Z>.md`, the release's own file, once its release gathers it | each release file is under target, and is the unit | the file name, by version, and `CHANGELOG.md`, which heads each release newest first with a link to its file |
| A work item's files | `seal/threads/<work-item-id>/` | each file under target | the table under *seal/threads/<work-item-id>/* below |
| The repository's rules | `CLAUDE.md` for the rules a session must hold, `CONTRIBUTING.md` for a contributor's procedure, and the `docs/` document each one links to | each file under target | this document, and `docs/README.md` |
| The configuration | `seal/config.md`, one row per item; `templates/config.md` documents every row | under target | the `Item` column |
| The follow-up list | `seal/follow-up.md`, one row per item that waits on a named party | under target | its rows, each naming who answers it |
| The process archive | `seal/process/<X.Y.Z>.md`, one file per release, written at its preparation | each file under target | the file name, by version |

## The size a reader takes whole

**A file a reader is meant to take whole fits one read.** The row and the
estimate are `templates/config.md` *The fold's values*, and what a document
past it owes is `skills/settle/SKILL.md` *A document past its ceiling is
split, never trimmed*.
check: tests/test_fold_check.py

## A change writes fragments, never a shared file

A file every branch appends to costs a conflict at the worst moment — after
the broad gate has run, which forces it to run again. So a change writes its
changelog entry into a file of its own, `seal/threads/<work-item-id>/changelog.md`,
never under a heading of `CHANGELOG.md`. No two work items share an id, so no
two branches share a file. A changelog fragment has no line starting `## `,
because that line ends the released section, and the gather refuses a
fragment that has one.

**The fragments are gathered at the release, by one command in one commit**,
and `docs/release-checklist.md` *2. Gather, bump* holds it. The fragments are
concatenated into the release's own file, `changelog/X.Y.Z.md`, and the
release's heading goes into the index, `CHANGELOG.md`. A fragment lives from
the work item's first entry to the release that ships it.
check: tests/test_the_changelog_is_gathered_at_release.py tests/test_gather_changelog.py

## A commit after the build brings its changelog fragment along

**A commit after the build that changes what the work item ships updates the
work item's `changelog.md` in the same range.** The build's last phase writes
the fragment and the release gathers it verbatim, so a later commit that
changes behaviour can leave it describing something that no longer ships. The
rule binds whoever writes the commit: the crafter's fix pass, a fix written after
the last round, and an integration commit after a sibling's squash, which the
orchestrator writes. A commit that changes nothing a release note states owes
the fragment nothing.
check: none reader: the next round's proofer and the sealer

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
names that record; a row naming a measurement nobody has taken is re-homed
as an issue, or as a `seal/follow-up.md` row in a repository with no
tracker. Each is closed in the record, `closed` with what closed it, and
`seal settle --apply` removes a directory only once its record holds no open row
in the working tree. The settle's pull request body carries every closure,
an issue carries every re-homed row, and git keeps the record. A released
work item that wrote no `frame/design.md` states no rule and goes the same way.
check: tests/test_settle.py

**The settle writes each section as the latest decision among the released
specs states it, checked against the code.** The specs whose rule changes
name one section, or a section holding it, are one group, and merge order
sorts it, so a group is that rule's history. Within a group the latest spec
that states a rule decides it, and an earlier operation it restates is
superseded: it is settled with the group and not applied. Where the code
has moved past the latest decision, the code is the later fact and the
section states what the code does. The settling session writes the section;
an operation's `from` locates the text its spec's framer read, and a `from`
that no longer matches is history, not a refusal. The rest of the document
stays as it was, and no marker is written. `settle` groups the specs, shows
each group's history and removes the directories; it writes no policy
document.
check: tests/test_rule_changes.py tests/test_settle.py

**A settle is not a work item.** It opens no directory under `seal/threads/`.
Its session records `seal no-work-item` on the settle's branch, its commits
carry the trailer `Seal-Routing: no work item` where the root is shared,
and what it wrote is reviewed at its pull request. What it leaves already has a home, the pull request and
git history, so it keeps no log of its own. Were it a work item, each settle
would leave a directory for the next one to remove, and settling would never
end; `skills/settle/SKILL.md` *A settle is not a work item* is the procedure.
check: tests/test_settle_reads_before_it_removes.py

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
check: tests/test_settle_reads_before_it_removes.py

**A document with a `.ko.md` edition changes with it, heading for heading.**
The two editions are prose in two languages, so the check compares what is
language-neutral: the sequence of heading levels. Whether a Korean paragraph
says what its English one says is review's to read. `CONTRIBUTING.md` *House
rules* owns the rule.
check: tests/test_both_editions_carry_the_same_folds.py

**Whether a line is live is asked by what the line does, and the four
readers that ask it give three answers.** These are all four readers, grouped
by the kind of line they read, with the cost each answer is chosen against.
check: tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py tests/test_routing.py

- **A line that HOLDS something — a claim or an anchor — is read on
  doubt.** The coordinate kernel's `quoted_lines`, which its `unquoted` and
  `markdown_lines` read through. A fence nobody closed is a malformed file
  whose lines are read, and a commented-out row is a parked claim and is
  read. What this protects is that a claim never leaves a record in silence.
  The wrong answer is loud instead: `BROKEN`, a refused name or exit 2, and a
  person answers it with an edit or a marker.
  check: tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py
- **A line that EXCUSES or DECLARES something — a changelog marker, a
  `seal/config.md` row, a `routing.md` row — is not taken on doubt, except
  where a declaring reader keeps an older reading that took it.**
  `unverified_check.py#live_lines` parks a line inside any fence or comment,
  closed or not, and a line its two span readings disagree about.
  `hooks/config.py#hidden_lines`, which reads `seal/config.md`, keeps,
  wherever its walk is unsure, the fence-only reading it gave before the walk:
  a row below a fence nobody closed declares nothing, and a row below a
  comment opener nobody closed still declares unless a fence that closes
  holds it, because that reading never hid one, and the walk may miss no row
  the older reading saw. `hooks/routing.py#shown`,
  which reads a `routing.md` and is not one of the four, keeps the reading
  it gave before the walk the same way, and that reading hid nothing: a row
  below a fence or a comment opener nobody closed still declares there,
  unless a fence that closes holds it. Those rows are the places a line
  nobody wrote live declares something; at every other fence or comment,
  what this protects is that nothing is excused or declared by a line
  nobody wrote live. The wrong answer is a statement left unbound, a hook
  that says nothing, or a gate that asks.
  check: tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py
- **A line a record's rows are COUNTED on is blanked the same way on both
  sides of a comparison.** `unverified_check.py#readable` blanks fenced lines
  with the indices intact, and a fence nobody closed to the end of the file.
  It reads a comment as text, because a record carries none, and the reader
  that judges a record refuses a line that begins with `<!--`. So the working
  tree and the base revision count the same
  table, and the readers that judge a record refuse a hidden table as absent
  rather than read it as empty.
  check: tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py

No one rule serves all three kinds. The holding bias would let a changelog
marker quoted in an example stand for an entry nobody gathered, and the excusing bias
would drop a parked row without a word. A reader of a new kind of line is a
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
`--released-at` reaches that merge commit; `skills/settle/SKILL.md` *In
local mode* gives the states that leave a work item unreleased. The settling
session writes the committed policy root as in shared mode, and
`seal settle --apply` removes each released local directory whose record holds no
open row, with no commit holding what it removed. The settle's pull request
changes the policy root alone, so no check reads a removal there, and its
commits carry no trailer, as no local-mode commit does.
check: tests/test_settle.py

## The unverified record, and the baseline it is read against

**A baseline reference is resolved once, to a merge base, and every arm reads
that commit.** A branch name is not a commit: it moves while the pull request
is open, so two arms reading it a second apart can compare against two
different trees. The report names the revision it actually compared against,
and a reference sharing no history with the head is exit 2 — a comparison
against nothing is not a comparison.
check: one-merge-base

**A pull request that declares nothing owes the unverified check nothing.**
Handed a `seal/` root's own `threads` path, `seal unverified` exits 0 and
names the state in two more cases beside the settled root: where no `seal/`
directory is in the tree, and where `threads/` holds work items none of which
carries a `gaps.md`. There is no row to read, and none could have left.
Where the root is not in the tree it compares nothing against the base
either, so the pull request that moves a root to local mode is not read as
deleting its records. Every other path holding no `gaps.md` is still
exit 2, which keeps a misspelt path from passing in silence.
check: nothing-declared-nothing-owed

## docs/

The standing policy. Its index is `docs/README.md`.

## seal/

What the plugin maintains, read and written by machines. Every `seal/…` path
means `<repo>/seal/` where that directory exists, and the root under the git
common directory otherwise.

| File | The question it answers |
|---|---|
| `seal/README.md` | what the root holds, where it lives in each mode, and which file states the export rules |
| `seal/config.md` | what this repository says about itself, one row per item |
| `seal/follow-up.md` | which items wait on a named party, and who |
| `seal/process/<X.Y.Z>.md` | what one release changed in the way of working, and why |
| `seal/threads/<work-item-id>/` | one work item's records, the table below |

## seal/threads/<work-item-id>/

One work item's records, from its first commit to the `settle` fold that
retires the directory. Which file each agent writes is
`skills/implement/SKILL.md` *3. The SDD file set*; this table says what each
file answers.

| File | The question it answers |
|---|---|
| `routing.md` | who frames, builds and reviews this work, and where it ends — answered before the first edit |
| `frame/design.md` | what is built, its scenarios, and the decisions with their grounds |
| `frame/plan.md` | in which phases it is built, how each is shown, and the approval line |
| `frame/questions.md` | which decisions only a person could make, and how each was answered |
| `gaps.md` | where the build departed from the frame, what was not verified and who answers it, and what was not done |
| `trail/phases/phase-N.md` | what one build phase was asked, found and removed |
| `trail/rounds/round-N.md` | what one review round read, found and closed |
| `changelog.md` | this work item's entry in the next release's notes |
| `trail/gate.md` | the orchestrator's one broad run, on either routing answer |
| `guarantee.md` | whether the sealer sealed the work, against the issue and the tree |

**The files keep these paths until the settle after their release, and
leave together.** `routing.md`, the frame (`frame/design.md`,
`frame/plan.md`, `frame/questions.md`), the trail (`trail/rounds/`,
`trail/phases/`, `trail/gate.md`) and the files at the thread's top
(`gaps.md`, `changelog.md`, `guarantee.md`, and a `pr.*.md` where one was
written) go with the directory, whole, when the settle removes it. A
repository installed before the plugin was renamed AgenticSeal holds the
files at their old names in the earlier layout, which
`hooks/root-migrate.py#THREAD_PATHS` maps onto this one, and the hook moves them into this layout
at the session start of each branch whose tree still holds them, as staged
`git mv` in shared mode and as renames under the git directory in local mode
(*The fold, and what tells it from a deletion* above, and
`docs/release-checklist.md` *2b*). What a document still cites of it
resolves at the tag of the release that shipped it.
check: tests/test_settle.py

**A record a template starts carries no HTML comment.** Its template holds
headings, table headers, placeholders, the labelled lines the record's
grammar asks for and the foot line, and nothing else. The guidance for
writing the record is in the skill or agent definition its writer reads,
stated there once. A comment copied into every record is a second copy of
that guidance, and every reader of the record has to model it.
check: tests/test_a_record_carries_no_comment.py

**A record holds a fence only around a finding's paste-ready fix, and a
labelled line a check reads stands outside every fence, at the start of its
line.** The readers keep one fence state, by the fence rule of
`hooks/blocks.py`, because a fix to a record's own grammar can hold a line
shaped like a label, and that line belongs to the fix.
check: tests/test_chain_check.py

**A reader of a record keeps no comment state: it reads `<!--` as text, and
refuses at its line a line outside every fence that begins with `<!--`.** A
record carries no comment, so a comment state in its reader models nothing
the record holds, and that state is where three reader defects of one
release came from. The refusal stands where the reader reads:
`chain_check.py` in a round record, a `guarantee.md` and a `trail/gate.md`,
`unverified_check.py` in a `gaps.md`, and `rule_changes.py` in a
`frame/design.md`'s `## Rule changes`. A base revision that holds such a line is not compared,
because nobody can edit a commit that already happened. A `routing.md` is
the exception: its reader, `hooks/routing.py`, runs in the edit check
(`docs/the-routing-check.md` *The edit check*) before every edit in an
opted-in repository, where a refusal would stop the edits of a work item
framed before its template lost its comments, so that reader keeps the
comment walk of `hooks/blocks.py`.
check: record-comment-line-refused

## The root records

| File | The question it answers |
|---|---|
| `CLAUDE.md` | the rules a session in this repository must hold, each linking to its home |
| `CONTRIBUTING.md` | how a contribution is made and checked, and what a change to a gate must carry |
| `CHANGELOG.md` | which releases there are: the index, one `## X.Y.Z — <date>` heading each, newest first, with a link to the release's file |
| `changelog/<X.Y.Z>.md` | what one release changed, that release's section alone |
| `README.md` and `README.ko.md` | what the plugin is and how to install it |

**`CHANGELOG.md` and each release's own file carry that release's one
`## X.Y.Z — <date>` line.** `changelog/<X.Y.Z>.md` opens with it, and the
index keeps the same line above the link to the file, because the update
skill an installed copy already carries checks that an update landed by the
first `## ` line of `CHANGELOG.md`. The GitHub Release reads the release's
own file.
check: tests/test_the_changelog_is_gathered_at_release.py tests/test_gather_changelog.py

**A `CLAUDE.md` row that points at a home carries three things: the home's
path and section, the moment a session needs the rule, and the act in one
sentence of the row's own, with the value the act needs.** It carries no
table, reasoning or history. Only the home's sentences are pinned, so a stale
value in a row is a reviewer's finding. No two rule documents may share more
15-word runs than their pair was measured at, which does not see a rule
restated in fresh words.
check: tests/test_the_rules_claude_md_names_have_one_home.py tests/test_no_passage_is_pasted_into_a_second_file.py

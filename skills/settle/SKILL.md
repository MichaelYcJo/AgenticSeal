---
name: settle
description: |
  Settle the released work items: show the rule changes their `frame/design.md`
  files state, grouped by the section each names and in merge order, write
  each section of the policy documents (`docs/` unless `Policy root` names
  another) as its group's latest decision, checked against the code, decide
  every open row of their records, then remove their directories.
  Use when: preparing a release and the work items have accumulated; a
  session asks what `seal/threads/` is still holding, or runs `seal settle`.
  NOT for: the release notes, which the tag's workflow builds from the
  fragments; anything in a work item that has not shipped.
---

# settle — write each section's latest decision

A work item's design states the rules its work changes in its `## Rule
changes` section, and the section is reviewed with the design. Released
designs pile up into a timeline: a later design may restate what an earlier
one decided, and the code may have moved past both. **The designs say what
was decided and in what order,
the code says what holds now, and the settling session writes each section as
the latest decision the code bears out. The script reads and removes; it
neither writes `docs/` nor judges.**

The settling session is the session the owner runs the settle in. **It puts
the person at most two questions, both before its first edit, and none after
them**: which directories besides `seal/` hold decisions to fold, and, where
the dry run lists a document of one, which of the documents listed the
settle promotes (*Directories a person names*). Everything else it decides
from the tree: it takes a default where the tree does not decide and writes
it down, and the owner reviews its pull request.

```
seal settle                  the dry run: each group of released designs that
                             name one section, the designs to read whole, every
                             open row, the files named like a record and not
                             read, and what --apply removes
seal settle --from DIR       the dry run, and every document of DIR, a
                             directory a person names, with the commits that
                             added and last changed each; repeatable
seal settle --apply          remove each released directory whose record
                             holds no open row
seal settle --released-at REF  what counts as released (default origin/main)
```

The script is `skills/settle/scripts/settle.py`, and `seal settle` runs it;
`bin/seal` is on the Bash tool's PATH while the plugin is enabled. It needs
python 3.12 or newer.
Where the `seal/` root is under the common git directory, *In local mode*
below says what changes.

## Rule changes

A work item's design states the rules it changes in its `## Rule changes`
section, one item per operation. The operation's line comes first, then one
field per line, indented two spaces:

```
- change
  file: docs/the-review-record.md
  section: The round record
  from: the sentence as it reads now.
  to: the sentence as it will read.
```

| Operation | Fields | What it says |
|---|---|---|
| `add` | `file`, `to`; `section` optional | `to` belongs at the end of the section's own text, before its first sub-heading. With no `section`, `to` is a new document, `file` |
| `change` | `file`, `section`, `from`, `to` | the text `from` quotes becomes `to` |
| `remove` | `file`, `section`; `from` optional | the text `from` quotes goes, or with no `from` the whole section, up to the next heading of its level or higher |
| `nothing` | `why` | changes no rule, and stands alone in the section |

- `file` is a top-level `.md` file of the policy root, `seal/config.md`'s
  `Policy root` row (`docs` when absent), joined with `/` and holding no `\`
  or `:`. `section` is a heading's text at any level.
- **`from` is the text as the design's framer read it.** It locates the change
  for the settling session and for a reviewer, and it is not a
  precondition: a `from` the section no longer holds is history, and the dry
  run says so. The dry run compares it, and `to`, with runs of whitespace
  collapsed; every other character, emoji included, is matched as itself.
- A value continues on the lines below it indented four spaces, and lands
  with that indent removed. A code span closes on the line that opens it: a
  line that begins inside a span an earlier line opened is refused at its
  line.
- A design that changes no rule writes the no-change block in place of the
  items, `- nothing` with its one field `why:`, and the block is read in
  that one spelling. A first line that opens like it and is not it, such as
  `nothing — <why>` or `- none`, is no block: the section is refused at that
  line as the items refuse any line outside them, and the reader names the
  line as one it did not read. `## Not verified` reads the block the same
  way.
- A block that does not match whole is refused at its line, and its design
  joins no group: the settling session reads it whole.
- The section's heading is `## Rule changes`, spelt exactly so, and no
  other heading is read as it. A heading whose letters, case folded, are
  those of `Rule changes`, that is not that heading and that stands outside
  the section, is another section: the reader names it, `chain-check`
  prints it at its line as one it did not read and refuses nothing for it,
  and the settle reads the design whole. Such a heading below level 2
  inside the section is a line of the section, refused as any line outside
  an item is. Whether a named heading meant the section is the judgment of
  whoever reads the design, the proofer at review among them.

`skills/settle/scripts/rule_changes.py` is the one reader.
`chain-check` asks the same reader at the pull request, for each work item
whose `routing.md` it judges and, on a pull request that declares at least
one work item, for every work item `frame/design.md` its own commits add or change
(`docs/the-review-record.md` *What the check reads at the pull request*).

## A rule has one shape

**A rule has one shape: the rule, its grounds, and the line naming what
reads it.** A `to` value that states a rule opens with the rule as one bold
sentence, gives its grounds as prose, and ends with one check line, which
stays English in every edition.

- A check line is a shown line of a rule file whose text, after any leading
  spaces, starts with `check: `, lowercase, one space after the colon.
- It names one or more targets separated by single spaces, or no target,
  written exactly `check: none reader: <who reads it>`.
- A target is a file of the repository, an eval case directory
  `evals/behaviour/<agent>/<case>/` holding `case.yaml`, or a marker:
  lowercase letters, digits and hyphens, carried by at least one test as
  `@pytest.mark.rule("<marker>")`.
- A marker names the tests of a rule whose test drives a script that can
  refuse a commit or fail a required pull-request job. Every other rule names
  files.
- Only the exact shape above is read. A line that opens like a check line
  and is not one, the label in another case, under emphasis, behind
  Markdown block markup, with a space before the colon, in the plural or as
  the word `Enforced by`, is named at its line as not read and refused for
  nothing; whether it meant a check line is review's to judge.
- A check line is one line. A target wrapped onto the line below is not
  read, and nothing names it, since the line below is prose: a check line
  naming more targets than a wrapped line holds is written past the wrap.
- A check line is refused at its line for a value holding `::`, a comma or
  an em dash, a reader with a space more after `reader:`, a path that is no
  file of the repository, and a marker no test carries.

**What this plugin checks, and what it does not.** It ships `seal rules --check`
(`.github/scripts/rules.py`), which reads every check line in a rule file,
refuses one the grammar refuses and names one it did not read. At the pull
request, `chain-check` asks the same reader for each check line inside an
`add` or `change` `to` of a design, and refuses a line that reader refuses
at that line of the design. A refused
line inside a section that a
pending `remove` with no `from` takes out at the settle is printed as
excused, with the work item that removes it, and is no refusal. A pending
`change`, or a `remove` with a `from`, excuses nothing, and where the `seal/`
root is local no line is excused. Whether
a target really enforces its rule, whether a rule paragraph carries the
line at all, and whether two rules contradict each other, it cannot read:
that is review's, and it is review's to find.

## The index

**`<policy root>/README.md` is the index: one table row per topic, naming
its file.** A row names its documents as backticked paths, a `.ko.md`
edition on its English edition's row. A framer picks each `file:` from it.
Where it exists, `seal fold` refuses a top-level document no row names, one
named on two rows, and a row that names none. A settling session that
creates the policy root writes the index with it, and after the removals
`--apply` names the row each new document is owed.

## When it runs

**When the owner calls it, as `docs/release-checklist.md` *2b. Settle what
earlier releases left behind* says.** It
is invoked, never triggered: no hook runs it and no gate refuses a branch
over an unsettled work item.

## What the dry run shows

`seal settle` reads the work items released at `--released-at`, each `frame/design.md`
as that ref holds it, or in local mode as its directory holds it, and writes
nothing:

- **Each group**: the designs whose operations name one place, a file and a
  section, in merge order. Two places are one group where one section holds
  the other, because a section's range holds its sub-sections. A design's
  place in the order is the first commit on `--released-at` that adds its
  `frame/design.md`, or its design at the path it held before the session-start
  move brought it into `seal/threads/` (`rule_changes.py#EARLIER`), or in local
  mode its pull request's merge commit's place on `--released-at`. The group
  opens with each place's lines in the working tree, or the words saying its
  heading is not there, and lists each operation with its design's coordinate
  and whether its `from` and its `to` are found in the section now. Two designs
  whose commits no ancestry orders are marked `unordered`, for the settling
  session to order by content.
- **The designs to read whole**: one whose `## Rule changes` does not parse,
  with the reader's reason, one with no such section, and one in which the
  reader names a line it did not read, a heading near `## Rule changes`
  among them, with that line and its reason.
- **Every open `## Not verified` row** of every released record, each with
  the backticked paths it names and whether each is in the working tree.
  Their heading names the four kinds of *The settling session's procedure*
  step 6 in its table's order, and gives no row a kind: the settling
  session decides each.
- **The files named like a record and not read**: a file in a released
  work item's directory whose name is that of a record the settle reads
  there, `gaps.md`, `frame/design.md` or `frame/plan.md`, at any path but
  that record's own, such as `trail/gaps.md` or a top-level `design.md`,
  each with the record it is named like. Only the exact name is read, and
  no file's content, so none of its rows is counted and none keeps its
  directory: what it holds is the settling session's to judge. The section
  is printed only where it names a file.
- **The judgments**: every row of every released `frame/plan.md` *Judgments
  of the run*, the decisions the orchestrator made in its run with their
  grounds, grouped by the `Judged against` cell, the document each stands
  on, with each work item's round count beside it. A plan with no such
  section prints nothing. A heading whose letters, case folded, are the
  section's and that is not it is named as not read at its line, and so is
  a section whose table is not under the exact header. A `trail/rounds`
  that is not a directory the dry run can list is named in place of a
  count. `--apply` removes the plans, so this is the one reading the rows
  get.
- **The named directories**, printed only with `--from`: each directory
  named, with its count of documents, and under it one line per document.
  A document is every file
  `git ls-files --cached --others --exclude-standard` lists under the
  directory, at any depth and of any extension, so a file git ignores is
  not one. Each line holds the file's path, the commit that added it and
  the commit that last changed it, each as a short hash and a date, read
  from one `git log` per directory. Renames are off, so a moved file counts
  as added where it lands, and a merge's own change is read (`--cc`): a
  merge whose result at the file differs from every parent's changed it,
  and added it where no parent holds it, however the result came to
  differ. A commit that deleted the file is neither its add nor its
  change; for example, a deletion on a branch whose merge kept another
  branch's content is not the file's last change. The
  person's `log.showRoot` and `log.showSignature` change none of these
  dates. A line ends `changed in the working tree` where `git diff HEAD`
  names the file.
  A file no commit adds, untracked or staged and never committed, reads
  `no commit adds it`. Documents are listed in the order of the commits
  that add them, and those no commit adds come last, in path order. A file
  two named directories hold is listed under the first one named. A root
  holding no work item prints the listing before its settled line. No line
  of it is a proposal (*Directories a person names*).
- **What `--apply` removes**, the citations into it from outside
  `seal/threads/`, and the checks under `tests/` that read `seal/threads`.

Nothing is refused or held in the dry run: a stale `from`, a section that
does not parse, an unordered pair and an open row are all shown.

## The settling session's procedure

1. Put the first question of *Directories a person names* to the person:
   which directories besides `seal/` hold decisions to fold. A session that
   cannot put it takes the answer "none".
2. Run `seal settle`, the dry run, on the settle's branch, with
   `--from <dir>` for each directory the answer named.
3. Where the dry run lists a document of a named directory, read each
   document whole with the code it bears on, write its proposal row, and
   put the table to the person as the second question of *Directories a
   person names*. The listing is git's facts about each file, and the row
   is yours to write. Where it lists none, ask nothing more. Both questions
   come before the first edit, and no step after this one asks anything.
4. For each group, read every operation in merge order, the section as it
   stands, and the code the rule names, its `check:` targets first. Each
   row the person's answer left marked `promote` joins the group of the
   place it names, as *Directories a person names* says. Write the section
   as the latest decision states it, in your own words. Where the code has
   moved past that decision, write what the code does. An earlier
   operation the latest one restates is superseded: it is settled with its
   group and not applied. The rest of the document stays as it was, and no
   marker is written.
5. Read each design listed to read whole, and write any rule it states the
   same way. Then read *The judgments*: where one kind of judgment recurs
   across work items under one document, or kept costing rounds, rewrite
   that document's section in this settle, as step 4 writes a group's, so
   the guidance improves from the record (`skills/core/SKILL.md` *A judgment
   stands on a source document, and is written down with both*).
6. Decide each open row against the tree, and close it in its record with
   `closed` and what closed it:

   | The row is | When | What closes it |
   |---|---|---|
   | moot | it names a unit the tree no longer holds | the coordinate showing the unit gone |
   | answered | another record or a later run already answered it | that record or run, named |
   | a measurement no record asks for | it names a run, a platform or a reading no record holds, and no failure, report or decision on record depends on its answer | the reason, naming what the answer would have decided; nothing is opened |
   | a measurement nobody has taken | it names a run, a platform or a reading no record holds | the issue it is re-homed to |

   On record means in a record that outlives the settle and rests on the
   answer: an open issue, a failed run, or a rule or design of another work
   item. The row's own work item is not such a record, its design, its
   questions and its rounds among them, because `--apply` removes its
   directory and nothing in it can wait on the answer. The row's own `Who
   must answer` cell is not one either.

   A row that fits more than one kind takes the first that fits, in the
   table's order. A measurement of a unit the tree no longer holds can no
   longer be taken, so it is moot. Every measurement no record asks for
   also fits *a measurement nobody has taken*, and it comes first, so it is
   closed before it can open an issue: an issue nothing on record waits on
   costs its reader a reading and a close.

   A measurement something on record needs is re-homed with one issue per
   distinct measurement (`gh issue create`), its body listing each row it
   would answer with the row's work item, its text, its answerer and the
   record that needs its answer. A repository with no tracker re-homes it
   as a `seal/follow-up.md` row.

   Open each file the dry run names as not read, and decide each item in it
   that reads as an open row by the same table. Write nothing into the
   file, since `--apply` removes it with its directory; the pull request
   body names each such item with its kind and what closed it, as it does
   a row.
7. Where the tree does not decide, take a default and write it down for the
   pull request body. Ask the person nothing: the questions of steps 1 and 3
   are the only ones a settle puts.
8. Run each rule's `check:` targets over what you wrote, and change what a
   failure shows still standing on the old fact. Then run the dry run
   again: a `to` not found is where you reworded, which the body explains.
   The step is done when every `check:` target passes. It does not look
   for the other checks that read what you wrote, such as a line-length
   check, a pin on a sentence you rewrote, or a check that reads the
   corpus: a search of the tests' text finds a module only by how it
   spells a path, so no such search lists them all, and step 10 runs every
   one.
9. Run `seal settle --apply`, with no `--from`, which it refuses.
10. Run the repository's `Broad gate` row. It is the one run that reads
    every check. Where a case fails because a pin under `tests/` or a copy
    such as a README row still states the old fact, change that pin or
    copy, and name each in the pull request body. Where a check that reads
    the corpus fails, answer it as *Answer every check that reads the
    corpus* says. Run the failing modules until they pass, then run the
    row again. The step is done when the row passes with no edit after it.
11. Open the pull request. Its body lists, per group, the decision and its
    grounds (the work item ids in merge order, the superseded operations,
    the code coordinate, and the path of each promoted document), the rows
    by kind with what closed each, the defaults it took, the answers for
    the checks that read the corpus, and how it was checked. It names the
    directories the first question's answer named, or says the answer was
    "none" and whether the session took it for want of a way to ask. It
    lists every proposal row with its place, its proposal, its grounds and
    the person's mark.

## Directories a person names

**A directory besides `seal/` that holds decisions, such as architecture
decision records, RFCs or another tool's spec files, reaches the policy
root only through a settle, only where a person names it, and only in the
documents the person marks `promote`.** Nothing in the plugin finds or opens
such a directory on its own, and no configuration row names one. Which
directories hold decisions, and which of their decisions becomes policy,
are the person's to decide, and the tree answers neither, so the settle
asks. Every other judgment of the settle stays the settling session's.

**The first question asks which directories besides `seal/` hold decisions
to fold.** The settling session puts it before its first edit. Its answers
are "none", which runs the settle as it runs without `--from`, or one or
more paths, each passed to the dry run as `--from <dir>`, relative to the
directory `seal settle` runs in or absolute. The question states the one
limit no guard covers, in this sentence: a directory that holds the `seal/`
root, such as the repository's top, lists the root's own files too, and the
settling session proposes each of them `skip`, because the settle already
reads those records. A session that cannot put the question takes "none",
and its pull request body says so.

**`--from` refuses four things, each with exit 2 and one sentence, and reads
and removes nothing**: a path that names no directory in the working tree,
a path outside the repository, the `seal/` root or a path under it, whose
records the settle already reads, and `--from` beside `--apply`. `--apply`
removes only under `seal/threads/`, and a flag it accepted would read as
one it acted on. Each sentence about a path names it as it was read, from
the directory `seal settle` runs in. A named directory holding no document
is listed with 0 documents.

**The listing is not a proposal.** Each of its lines is what git answers
about one file, as *What the dry run shows* gives them: its path, its two
commits, and whether the working tree changed it. The script reads no
document's content, so a line says nothing of what the document decides,
which section it bears on, or whether it is promoted, and neither does the
document's place in the listing, its directory, its name or its extension.
The proposal is the settling session's to write, and the mark is the
person's.

**The settling session writes one proposal row per document**, after
reading the document whole with the code it bears on:

- **The place** is named as an operation of *Rule changes* names one: a
  `file` picked from the index (*The index*) and a `section`. It names an
  existing heading, or a new section or a new document marked as new. A
  document bearing on several sections names each in its one row. The
  document's own headings decide nothing.
- **The proposal** is `promote` or `skip`.
- **The grounds** say what a promote writes, read from the document and
  checked against the code. A document holding one decision the code bears
  out and one the code has left is proposed `promote`, with grounds naming
  the first alone. A plan not yet built, a decision the code has since
  left, a document whose decisions bear on no section of the policy, and a
  file of the `seal/` root are each proposed `skip`, with that reason as the
  grounds.
- **A document skipped at an earlier settle** is proposed `skip` again, with
  grounds naming that settle's pull request, where two facts hold: the last
  settle's pull request body holds the document's row marked `skip`, and
  the document's last change is a commit that settle's merge commit reaches
  (`git merge-base --is-ancestor <last change> <merge commit>` exits 0). The
  session finds the last settle's pull request from the last commit that
  changed the policy root. Every other document is new, a document no
  commit adds among them.

**The second question puts the numbered table to the person once**, before
the first edit, in this shape:

| # | Document | Place | Proposal | Grounds | Mark |
|---|---|---|---|---|---|

The `Mark` cell is empty in the question and holds the person's mark in
the pull request body. The answers are "as proposed", "skip every row", or
the numbers of the rows whose mark the person flips, and every answer
continues. A listing that holds no document asks nothing.

**Only a row the person's answer leaves marked `promote` is written, and it
is written as a released design's operation is.** It joins the group of the
place it names, and the group is ordered by commits, the listing's beside
the designs', a document deciding as of its last change. The session writes
the section as the group's latest decision checked against the code, in its
own words and with no marker, and the section's grounds cite the document
by its repository path, as the paragraph on reference roots under *What
`--apply` does* asks of a statement a settle writes.

**A named directory is read and never written.** No step of the settle
writes, moves or removes a file under it, and `seal settle --apply` removes
only under `seal/threads/` and refuses `--from`. A promoted decision reaches
the policy root in the settling session's words with the document's path,
and the document stays where it was, as it was.

## What `--apply` does

- **It removes every released work item directory whose record holds no
  open row in the working tree**, whole, its process record included,
  whether or not it wrote a `frame/design.md`. A row closed on disk and not yet
  committed is closed.
- **It keeps a directory whose record still holds an open row**, or whose
  record cannot be read, and names each row.
- **It names each file the dry run names as not read, and decides nothing
  on it.** A `not read:` line under the directory's `removed` or `kept`
  line names the file, which goes or stays with its directory; the
  directory's record at its place alone decides which.
- **It prints, for each directory it removed, the rows its record closed
  with what closed each**, so the pull request body can copy them.
- **It writes no policy document.** The settling session has written them
  by then, and `--apply` prints `seal fold`'s lines over the policy root
  after the removals.

It exits 0 when it kept nothing, 1 when it kept a directory, and 2 when the
arguments or the tree are unusable. Its last line counts each.

**A reference root is history, read where the work touches what it
describes, and input to a settle only where a person names it.** A
project's own `specs/`, as `templates/setup/config.md` *Reference specs*
says, is read where the work touches what it describes, and cited in the
`frame/design.md` whose rule changes it informed or in the section a settle
writes from it. It reaches a settle only as a directory the person names at
the first question of *Directories a person names*, and the settle does not
read the row. `seal settle` never writes there, and neither does the
settling session: `--apply` removes only under `seal/threads/`.

## In local mode

**In local mode `seal settle` reads the work items under the common git
directory, and a work item is released when the pull request from the
branch its `routing.md` names has merged, its merge commit reachable from
`--released-at`.** No ref holds a local work item's directory, so presence
at a ref cannot say that it shipped. What reaches the ref is its pull
request's merge commit, whatever the merge method was.

- **Where it reads.** Every `seal/threads/<id>/` path is read and removed
  under `$(git rev-parse --git-common-dir)`, so a work item's directory is
  `<git-common-dir>/seal/threads/<id>/`, and it is printed as
  `seal/threads/<id>/`. The policy root, the tracked files the citations are
  read from, and `tests/` are read from the repository's top.
- **What released means.** `seal settle` reads the `Branch` row of each work
  item's `routing.md` and asks
  `gh pr list --head <branch> --state merged --json number,mergeCommit`
  from the repository's top, once per branch. A work item is unreleased,
  and untouched, in three states: no `routing.md` that `hooks/lib/routing.py`
  reads as a declaration naming a branch, no merged pull request from that
  branch, or no listed merge commit reachable from `--released-at`, a pull
  request listed with no merge commit among them. Shared mode never asks
  `gh`.
- **A `gh` that cannot be asked stops the run.** Where `gh` is not on
  `PATH` or its query fails, `seal settle` exits 2 with one sentence naming `gh`
  and what it said, and reads and removes nothing. Every work item would
  otherwise read as unreleased, and the run would say there is nothing to
  settle.
- **The design and the order.** Each `frame/design.md` is read from its directory,
  since no ref holds it. The released designs are listed by their merge
  commits' place in `git rev-list --topo-order --reverse` of
  `--released-at`, and two whose merge commits no ancestry orders are marked
  `unordered`.
- **What the dry run adds.** Its first line names the root's path and says
  it is local mode. Each released work item is listed with its pull
  request's number and its merge commit, for the settle's pull request body
  to cite, and each unreleased one with which of the three states holds.
  The heading of what `--apply` removes says that no commit holds those
  directories, and that `seal export` takes a copy for whoever wants one.
- **What `--apply` does.** It removes each released local directory whose
  record holds no open row, from the git directory, and keeps and names one
  that holds a row, with the exit codes *What `--apply` does* states. No
  commit holds what it removes, and none needs to: a work item's records
  end their role when it ships, and the settling session closes its rows
  first.
- **The settling session's procedure is the same.** It writes the
  repository's committed policy root, and creates it with its index where
  it is absent (*The index*).

**The limits, which no guard covers.** A work item whose branch reached
`--released-at` without a pull request reads as unreleased, and its
directory is removed by hand. A repository on a host `gh` cannot ask cannot
settle in local mode, and the exit-2 sentence says so. A branch name that a
later work item reuses, after an earlier pull request from it merged, reads
that later work item as released. So does a merged pull request from a fork
whose branch has the same name, since `gh pr list --head` matches a branch's
name and not its owner. The one-issue flow names each branch after its
issue, which makes either match unlikely; it does not rule out the second,
because the flow does not name a fork's branches.

## A released work item with no `frame/design.md`

A released work item with no `frame/design.md` states no rule, and it leaves like
any other: `--apply` removes it once its record holds no open row. The dry
run lists it as stating no rule, and its open rows with every other record's.

## Answer every check that reads the corpus

**A settle is not finished until every check in your repository that carries
a population floor over `seal/threads/` has been answered.** A floor is an
assertion like `len(records) > 200` over a walk of `seal/threads/`, and a
settle shrinks the corpus by design (`docs/one-root-by-lifetime.md` *The
dependency rule*), and a list of readers written in any document is not the
whole list.
The dry run lists every `tests/` file that reads `seal/threads`, and every path
outside it that cites into what `--apply` removes. Each check gets one answer,
written down:

| Answer | When it fits |
|---|---|
| **retire the case** | it was about a shape the settle removes, and nothing is left for it to be about |
| **re-point it at a fixture corpus** | the property is still worth checking, and a built tree checks it better than whatever the repository happens to hold |
| **decline** | the case and the floor are right, and the settle waits for that population to exist again |

Lowering the floor until the run passes is not an answer: it turns a check
into a comment.

## A document past its ceiling is split, never trimmed

After the removals, `--apply` names each document past the `Document token
ceiling` row in `seal/config.md`, as `seal fold` does, and neither refuses
it. Such a document is recommended to be split by topic along its own
headings, in that pull request or a later one, and nothing is cut to fit.
The plugin sets no ceiling; a repository states its own.

## A settle is not a work item

**A settle opens no directory under `seal/threads/`**: no `routing.md`, no
frame, no round records, and the routing question is not asked for it. It
edits under `seal no-work-item`, run on the branch the settle is made on.
Where the root is shared, its commits carry
`Seal-Routing: no work item` as their trailer
(`skills/commit-pr-convention/SKILL.md`). What it wrote is reviewed at
its pull request. It keeps no log: what
changed is the diff. Where the root is shared the removed designs are in git
history; in local mode no commit holds them, and the dry run names
`seal export` for whoever wants a copy. A settle that
opened a work item would leave a directory for the next settle to remove, and
settling would never end.

## What this does not do

- The script does not judge. Which decision is latest, whether the code has
  moved past it, what each row is, and the place, the proposal and the
  grounds of each named document are the settling session's, the mark on
  each document is the person's, and the owner reviews them at the pull
  request.
- It does not fail a build. No gate refuses a branch for an unsettled work
  item.

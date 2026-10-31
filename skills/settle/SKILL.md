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

The settling session is the session the owner runs the settle in. **It asks
nobody at any step**: it decides from the tree, takes a default where the
tree does not decide and writes it down, and the owner reviews its pull
request.

```
seal settle                  the dry run: each group of released designs that
                             name one section, the designs to read whole, every
                             open row, and what --apply removes
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
  other heading is read as it. A heading at any level whose letters, case
  folded, are those of `Rule changes`, and that is not that heading, is
  another section: the reader names it, and `chain-check` prints it at its
  line as one it did not read and refuses nothing for it, so a design
  holding only it has no section and the settle reads it whole. Whether it
  meant the section is the judgment of whoever reads the design, the
  proofer at review among them.

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
- A line whose only content before the label is Markdown block markup or
  emphasis is a near miss and is refused at its line; only the exact shape
  above is read.
- Every other spelling of the label is refused at its line too: another
  case, a space before the colon, the plural, the word `Enforced by`. So is
  a value holding `::`, a comma or an em dash, a reader with a space
  more after `reader:`, a path that is no file of the repository, and a
  marker no test carries.

**What this plugin checks, and what it does not.** It ships `seal rules --check`
(`.github/scripts/rules.py`), which reads every check line in a rule file and
refuses one the grammar refuses. A refused line inside a section that a
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
  with the reader's reason, and one with no such section.
- **Every open `## Not verified` row** of every released record, each with
  the backticked paths it names and whether each is in the working tree.
- **What `--apply` removes**, the citations into it from outside
  `seal/threads/`, and the checks under `tests/` that read `seal/threads`.

Nothing is refused or held in the dry run: a stale `from`, a section that
does not parse, an unordered pair and an open row are all shown.

## The settling session's procedure

1. Run `seal settle`, the dry run, on the settle's branch.
2. For each group, read every operation in merge order, the section as it
   stands, and the code the rule names, its `check:` targets first. Write
   the section as the latest decision states it, in your own words. Where
   the code has moved past that decision, write what the code does. An
   earlier operation the latest one restates is superseded: it is settled
   with its group and not applied. The rest of the document stays as it
   was, and no marker is written.
3. Read each design listed to read whole, and write any rule it states the
   same way.
4. Decide each open row against the tree, and close it in its record with
   `closed` and what closed it:

   | The row is | When | What closes it |
   |---|---|---|
   | moot | it names a unit the tree no longer holds | the coordinate showing the unit gone |
   | answered | another record or a later run already answered it | that record or run, named |
   | a measurement nobody has taken | it names a run, a platform or a reading no record holds | the issue it is re-homed to |

   A row that fits more than one kind takes the first that fits, in the
   table's order: a measurement of a unit the tree no longer holds can no
   longer be taken, so it is moot.

   A measurement is re-homed with one issue per distinct measurement
   (`gh issue create`), its body listing each row it would answer with the
   row's work item, its text and its answerer. A repository with no tracker
   re-homes it as a `seal/follow-up.md` row.
5. Where the tree does not decide, take a default and write it down for the
   pull request body.
6. Run each rule's `check:` targets over what you wrote, and change what a
   failure shows still standing on the old fact. Then run the dry run
   again: a `to` not found is where you reworded, which the body explains.
   The step is done when every `check:` target passes. It does not look
   for the other checks that read what you wrote, such as a line-length
   check, a pin on a sentence you rewrote, or a check that reads the
   corpus: a search of the tests' text finds a module only by how it
   spells a path, so no such search lists them all, and step 8 runs every
   one.
7. Run `seal settle --apply`.
8. Run the repository's `Broad gate` row. It is the one run that reads
   every check. Where a case fails because a pin under `tests/` or a copy
   such as a README row still states the old fact, change that pin or
   copy, and name each in the pull request body. Where a check that reads
   the corpus fails, answer it as *Answer every check that reads the
   corpus* says. Run the failing modules until they pass, then run the
   row again. The step is done when the row passes with no edit after it.
9. Open the pull request. Its body lists, per group, the decision and its
   grounds (the work item ids in merge order, the superseded operations, the code
   coordinate), the rows by kind with what closed each, the defaults it
   took, the answers for the checks that read the corpus, and how it was
   checked.

## What `--apply` does

- **It removes every released work item directory whose record holds no
  open row in the working tree**, whole, its process record included,
  whether or not it wrote a `frame/design.md`. A row closed on disk and not yet
  committed is closed.
- **It keeps a directory whose record still holds an open row**, or whose
  record cannot be read, and names each row.
- **It prints, for each directory it removed, the rows its record closed
  with what closed each**, so the pull request body can copy them.
- **It writes no policy document.** The settling session has written them
  by then, and `--apply` prints `seal fold`'s lines over the policy root
  after the removals.

It exits 0 when it kept nothing, 1 when it kept a directory, and 2 when the
arguments or the tree are unusable. Its last line counts each.

**A reference root is history, never input.** A project's own `specs/`, as
`templates/setup/config.md` *Reference specs* says, is read where the work touches
what it describes and cited in the `frame/design.md` whose rule changes it informed.
`seal settle` never writes there, and neither does the settling session:
`--apply` removes only under `seal/threads/`.

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
  moved past it, and what each row is are the settling session's, and the
  owner reviews them at the pull request.
- It does not fail a build. No gate refuses a branch for an unsettled work
  item.

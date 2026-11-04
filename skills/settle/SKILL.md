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

Where its subject is the code, a work item's design states the rules the
work changes in its `## Rule changes` section, and the section is reviewed
with the design. A work item whose subject is the policy root edits the root
in its own pull request (`skills/implement/SKILL.md` *Document layout — two roots, three
lifetimes*). The
section's grammar, the shape of a rule and the index are
`skills/settle/rule-changes.md`, which the design's author opens to write
the section and the settling session opens before step 4 of the procedure.
Released
designs pile up into a timeline: a later design may restate what an earlier
one decided, and the code may have moved past both. **The designs say what
was decided and in what order,
the code says what holds now, and the settling session writes each section as
the latest decision the code bears out. The script reads and removes, and
with `--draft` writes the released operations literally into the policy root
as a starting text; it judges nothing.**

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
seal settle --draft          write every released operation into the policy
                             root in merge order, and name each one not
                             placed; it decides nothing
seal settle --apply          remove each released directory whose record
                             holds no open row and whose version's published
                             note, where one is read, carries its entry
seal settle --released-at REF  what counts as released (default origin/main)
```

The script is `skills/settle/scripts/settle.py`, and `seal settle` runs it;
`bin/seal` is on the Bash tool's PATH while the plugin is enabled. It needs
python 3.12 or newer.
Where the `seal/` root is under the common git directory,
`skills/settle/local-mode.md` *In local mode* says what changes, and the
settling session opens it before step 2 of the procedure.

## When it runs

**When the owner calls it, not at every release.** Released work items wait
on disk until then. It is invoked, never triggered: no hook runs it and no
gate refuses a branch over an unsettled work item.

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
  count.
- **The judgments earlier settles removed**: every row of every
  `seal/threads/<id>/frame/plan.md` a commit on `--released-at` deleted,
  where no directory `<id>` stands in the working tree. One `git log -z
  --no-renames --full-history --diff-filter=D` of the ref over
  `seal/threads` lists the deletions. `-z` keeps a path holding a
  character past ASCII unquoted, and `--no-renames` keeps a deletion a
  deletion where the same commit adds a similar plan, such as another work
  item's. Each plan is read once, at the
  parent of the newest commit that deleted it, by the reader *The
  judgments* uses: a near heading and a table not under the exact header
  are named as not read, at the coordinate `<short>^:<path>`. The rows are
  grouped by the `Judged against` cell exactly as written, in the order
  first met, the removing commits newest first. Each work item's line gives
  the lowest `vX.Y.Z` tag that holds the commit adding its plan, or says no
  tag holds that commit, and the removing commit's short hash with its
  `(#N)`. A `git` that fails is named with what it said, and the dry run
  goes on. The section counts nothing and matches no row to another, so a
  row here sharing a cell with a row above is not a recurrence, and two
  cells spelt apart are not two kinds: whether two rows are one kind is the
  settling session's judgment (step 5). The section is printed only where
  it holds a row or a line not read. Two limits no guard covers: a shallow
  clone lists no plan deleted past its boundary, and a plan only a merge
  commit's own resolution deleted is not listed, because the query reads
  non-merge diffs.
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
  branch's content is not the file's last change. A line ends `changed in
  the working tree` where `git diff HEAD` names the file.
  A file no commit adds, untracked or staged and never committed, reads
  `no commit adds it`. Documents are listed in the order of the commits
  that add them, and those no commit adds come last, in path order. A file
  two named directories hold is listed under the first one named. A root
  holding no work item prints the listing before its settled line. No line
  of it is a proposal (`skills/settle/named-directories.md` *Directories a
  person names*).
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
   put the table to the person as the second question of
   `skills/settle/named-directories.md` *Directories a person names*. The
   listing is git's facts about each file, and the row
   is yours to write. Where it lists none, ask nothing more. Both questions
   come before the first edit, and no step after this one asks anything.
4. Optionally, first run `seal settle --draft`, after opening
   `skills/settle/draft.md` *What `--draft` writes*,
   and commit what it wrote as one commit before any other edit, so the
   pull request shows the literal pass and the settling session's judgment
   as two diffs. The draft decides nothing: every section it wrote is read
   below against the code like a section the settling session wrote, and
   each operation it printed as not placed is written by hand. Then, for
   each group, read every operation in merge order, the section as it
   stands, and the code the rule names, its `check:` targets first. Each
   row the person's answer left marked `promote` joins the group of the
   place it names, as `skills/settle/named-directories.md` *Directories a
   person names* says. Write the section
   as the latest decision states it, in your own words. Where the code has
   moved past that decision, write what the code does. An earlier
   operation the latest one restates is superseded: it is settled with its
   group and not applied, and where the draft wrote it, it is taken out.
   The rest of the document stays as it was, and no marker is written.
5. Read each design listed to read whole, and write any rule it states the
   same way. Then read *The judgments* and *The judgments earlier settles
   removed*: where one kind of judgment recurs across work items or across
   releases, or kept costing rounds, rewrite the section that kind stands on
   in this settle, as step 4 writes a group's, so the guidance improves from
   the record (`skills/core/SKILL.md` *A judgment stands on a source
   document, and is written down with both*). Whether an earlier row is one
   kind with a current row is your judgment, read from what each row says
   and not from its cell's spelling: the dry run groups by the cell as
   written and decides no kind.
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
    the code coordinate, and the path of each promoted document), each
    operation the draft did not place with how it was written, the rows
    by kind with what closed each, the defaults it took, the answers for
    the checks that read the corpus, each kind of judgment that recurred
    across releases with the releases it recurred in, and how it was
    checked. It names each
    directory `--apply` kept for its note, with the tag, the pull request
    and where its fragment can be read, as its `kept` line gives them, so
    the owner can repair that note before a later `--apply` removes the
    directory. It names the
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

Where the answer names a directory, the settling session opens
`skills/settle/named-directories.md` before step 2 of the procedure. It
holds what `--from` refuses, the proposal row the session writes for each
document, the second question, and how a promoted row is written.

## What `--apply` does

- **It removes every released work item directory whose record holds no
  open row in the working tree**, whole, its process record included,
  whether or not it wrote a `frame/design.md`. A row closed on disk and not yet
  committed is closed.
- **It keeps a directory whose record still holds an open row**, or whose
  record cannot be read, and names each row.
- **Where the root is shared and the repository's notes are built from the
  fragments, it keeps a released directory whose version's published note
  does not carry its entry, and names it.** The published note is the one
  copy of a fragment outside the history, and the removal leaves the
  history as the only copy, so a note that lost an entry is caught before
  that. The check runs after the open-row check, for each directory that
  check would remove.
  - A note is read where `--released-at` holds the work item's
    `changelog.md` with text in it, the oldest commit adding it ends its
    subject with `(#N)`, and a `vX.Y.Z` tag holds that commit. The version
    is the lowest such tag by number. An empty fragment gets no entry in a
    note, so none is read for it.
  - The note is the version's release in one
    `gh api --paginate 'repos/{owner}/{repo}/releases?per_page=100'` list,
    drafts left out. It carries the entry where its body links
    `https://github.com/<owner>/<name>/pull/<N>`, under any owner and name
    and with no digit after N, or holds the HTML comment naming the work
    item's id, which the notes published before entries linked their pull
    requests carry.
  - **Notes are read only where the repository builds them from the
    fragments.** The release workflow that builds a note from the fragments
    is AgenticSeal's own (`.github/scripts/publish_release_note.py`), and
    the plugin ships no copy, so a repository's notes may be written by
    hand or by another tool and say nothing of a fragment. The same list
    tells the two apart: where no published release holds a whole line
    `[#N](https://github.com/<owner>/<name>/pull/N)`, the line that opens
    an entry, or the old comment on a line of its own, no note is read and
    every directory goes.
  - A directory whose note does not carry the entry is kept, and its `kept`
    line names the tag, the pull request and `git show <commit>:<path>` for
    its fragment's text. So is one whose version has no published release,
    where the list holds at least one; where it holds none, the repository
    publishes no Releases, and the directory goes.
  - A directory with no note to read goes, in each of these cases: no
    `changelog.md` at `--released-at` or one with no text, an adding commit
    that names no pull request, no version tag, no published release, or
    notes not built from the fragments. A `no note read:` line under its
    `removed` line says which case held.
  - The list is asked once, before the first removal, and only where some
    directory gets as far as a version tag. A list `gh` cannot give, and a
    `git` that cannot read what a note is checked by, stop the run with
    exit 2 and one sentence saying what was said, and nothing is removed.
    The dry run reads no note.
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
arguments or the tree are unusable, a note that cannot be checked among
them. Its
last line counts each, the directories kept for a row apart from those kept
for a note.

**A reference root is history, read where the work touches what it
describes, and input to a settle only where a person names it.** A
project's own `specs/`, as `templates/setup/config.md` *Reference specs*
says, is read where the work touches what it describes, and cited in the
`frame/design.md` whose rule changes it informed or in the section a settle
writes from it. It reaches a settle only as a directory the person names at
the first question of *Directories a person names*, and the settle does not
read the row. `seal settle` never writes there, and neither does the
settling session: `--apply` removes only under `seal/threads/`.

## A released work item with no `frame/design.md`

A released work item with no `frame/design.md` states no rule, and it leaves like
any other: `--apply` removes it once its record holds no open row, unless
its published note keeps it (*What `--apply` does*). The dry
run lists it as stating no rule, and its open rows with every other record's.

## Answer every check that reads the corpus

**A settle is not finished until every check in your repository that carries
a population floor over `seal/threads/` has been answered.** A floor is an
assertion like `len(records) > 200` over a walk of `seal/threads/`, and a
settle shrinks the corpus by design (`docs/layout/one-root-by-lifetime.md` *The
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
it. Such a document is recommended to be split by who opens each section
and at which step, as `skills/core/SKILL.md` *The first value: efficient
development through the workflow* states, in that pull request or a later
one, and nothing is cut to fit.
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

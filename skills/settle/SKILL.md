---
name: settle
description: |
  Apply the rule changes each released work item's `spec.md` states to the
  policy documents (`docs/` unless `Policy root` names another), in place
  and in merge order, then remove the work item's directory.
  Use when: preparing a release and the work items have accumulated; a
  session asks what `seal/specs/` is still holding, or runs `settle`.
  NOT for: gathering changelog fragments, which release preparation
  already does; anything in a work item that has not shipped.
---

# settle — apply what released specs decided

A spec states the rules its work changes in its `## Rule changes` section.
The section is reviewed with the spec, and `settle --apply` applies it to
`docs/` after the release. **The spec decides; the command applies.**
`docs/one-root-by-lifetime.md` §*What keeps `settle` light* says the step
"moves and does not verify": what a spec decided is not judged again here,
and whether a rule still holds is the suite's to say.

```
settle                       the dry run: pending changes, refusals, and what
                             --apply would remove
settle --apply               apply the changes and remove what they settle
settle --released-at REF     what counts as released, and the base the records
                             are asked at (default origin/main)
```

The script is `skills/settle/scripts/settle.py`, and `bin/settle` is on the
Bash tool's PATH while the plugin is enabled. It needs python 3.12 or newer.

**It refuses to run in local mode.** A `seal/` root under the common git
directory is never committed, so no ref holds the work item directories and
nothing removed from them could be recovered. `seal mode shared` moves the
root into the tree and `settle` works from there.

## Rule changes

A spec states the rules it changes in its `## Rule changes` section, one
item per operation. The operation's line comes first, then one field per
line, indented two spaces:

```
- change
  file: docs/the-review-record.md
  section: The round record
  from: the sentence as it reads now.
  to: the sentence as it will read.
```

| Operation | Fields | What it does |
|---|---|---|
| `add` | `file`, `to`; `section` optional | puts `to` at the end of the section's own text, before its first sub-heading. With no `section` it creates `file`, and is refused where `file` exists |
| `change` | `file`, `section`, `from`, `to` | rewrites `from` where it stands |
| `remove` | `file`, `section`; `from` optional | deletes `from`, or with no `from` the whole section, up to the next heading of its level or higher |

- `file` is a top-level `.md` file of the policy root, `seal/config.md`'s
  `Policy root` row (`docs` when absent). `section` is a heading's
  text at any level, and appears once in the file. `from` appears once in
  the section, compared with runs of whitespace collapsed; every other
  character, emoji included, is matched as itself.
- A value continues on the lines below it indented four spaces, and lands
  with that indent removed.
- A spec that changes no rule writes `nothing — <why>` in place of the
  items.
- A block that does not match whole is refused at its line, and its spec
  applies nothing.

`skills/settle/scripts/rule_changes.py` is the one reader.

## A rule has one shape

**A rule has one shape: the rule, its grounds, and what enforces it.** A
`to` value that states a rule opens with the rule as one bold sentence, gives
its grounds as prose, and ends with one line naming what reads it:
`Enforced by: <target>[, …]`, where a target is a repository path with an
optional `::<name>` for a `def` or `class`, or `Enforced by: nothing — <why>`
with a reason. `Enforced by:` stays English in every edition.

**What this plugin checks, and what it does not.** It ships `fold-check`
(`skills/settle/scripts/fold_check.py`), which reads that shape over the top
level of the policy root from the `Fold shape from` row in `seal/config.md`,
and a row a repository does not write is a check it does not run
(`templates/config.md` §*The fold's values*). Whether a target really
enforces its rule, and whether two rules contradict each other, it cannot
read: that is review's, and it is review's to find.

## The index

**`<policy root>/README.md` is the index: one table row per topic, naming
its file.** A row names its documents as backticked paths, a `.ko.md`
edition on its English edition's row. A framer picks each `file:` from it.
Where it exists, `fold-check` refuses a top-level document no row names, one
named on two rows, and a row that names none. `--apply` writes an empty index
when it creates the policy root, and after applying it names the row each new
document is owed.

## When it runs

**When the owner calls it, as `docs/release-checklist.md` §*2b* says.** It
is invoked, never triggered: no hook runs it and no gate refuses a branch
over an unsettled work item.

## What `--apply` does

- **In merge order, and the later spec wins.** A spec's place is the first
  commit on `--released-at` that adds its `spec.md`. Two specs whose adding
  commits no ancestry orders, and that name one file and section, are a
  conflict: neither applies, and both are printed for the owner.
- **Whole or not at all.** A spec whose section does not parse, whose
  section or `from` text is not there, or whose record holds an open
  `## Not verified` row applies nothing, and its directory stays. A later
  spec at one of its places waits with it.
- **In place.** Each change lands where its text stands, and the rest of
  the document is byte-identical. No marker is written.
- **A directory goes only with the rule changes it applied**, whole, its
  process record included. A `nothing — <why>` spec has nothing to apply and
  goes. A spec with no `## Rule changes` was written before the section
  existed; it is named and stays.
- The documents are written before any directory is removed.

It exits 0 when nothing was refused or kept, 1 when something was, and 2 when
the arguments or the tree are unusable.

**A reference root is history, never input.** A project's own `specs/`, as
`templates/config.md` §*Reference specs* says, is read where the work touches
what it describes and cited in the `spec.md` whose rule changes it informed.
`settle` never writes there: `--apply` writes the policy root and removes only under
`seal/specs/`.

## A released work item with no `spec.md`

A released work item with no `spec.md` states no rule, and `--apply` removes
it when nothing in its record is open; the dry run lists it as *retired by
the rule*. One whose record holds an open row is *kept by the rule*, with
every row named. The row leaves by being closed (`closed` with what closed
it), a row re-homed being closed too with where it went, and never with the
directory. A spec's directory is held by an open row the same way.

**Close it in a pull request of its own, and let that one merge first.** The
CI readers ask the rule of the merge base, so a row closed and its directory
removed in one pull request is still open where they look.

**Merged first means merged to the branch the release merges to.** The CI
readers on the release pull request ask at the merge base of its base and its
merge ref, which is the base's tip. So `settle` asks the merge base of
`--released-at` and `HEAD` as well as the working tree, which is CI's commit
until `--released-at` moves past this branch's fork. A directory closed here
and open there is listed under *kept until the closure reaches <base>*, or,
once `--released-at` has moved, *kept: the closure has not reached <base>*.
Where `--released-at` already holds the closure, merging it into this branch
and running `settle` again lets the directory go. A `--released-at` sharing
no commit with `HEAD` is refused at exit 2.

## Answer every check that reads the corpus

**A settle is not finished until every check in your repository that carries
a population floor over `seal/specs/` has been answered.** A floor is an
assertion like `len(records) > 200` over a walk of `seal/specs/`, and a
settle shrinks the corpus by design. `docs/one-root-by-lifetime.md` §*The
dependency rule* names two such readers, and that list is not the whole list.
The dry run lists every `tests/` file that reads `seal/specs`, and every path
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

After applying, `--apply` names each document past the `Document token
ceiling` row in `seal/config.md`, as `fold-check` does, and neither refuses
it. Such a document is recommended to be split by topic along its own
headings, in that pull request or a later one, and nothing is cut to fit.
The plugin sets no ceiling; a repository states its own.

## A settle is not a work item

**A settle opens no directory under `seal/specs/`**: no `routing.md`, no
frame, no round records, and the routing question is not asked for it. Every
commit carries `: '[no-review]';` in front of the command, quotes included,
and what it applied is reviewed at its pull request. It keeps no log: what
changed is the diff, and the removed specs are in git history. A settle that
opened a work item would leave a directory for the next settle to remove, and
settling would never end.

## What this does not do

- It does not verify. Whether a rule still holds is the suite's job, through
  the test its `Enforced by:` line names.
- It does not fail a build. No gate refuses a branch for an unsettled work
  item.

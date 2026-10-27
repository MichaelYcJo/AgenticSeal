# One root, laid out by lifetime

*English · [한국어](./one-root-by-lifetime.ko.md)*

Everything this plugin keeps in a repository sits under one root it owns,
`seal/`, and what sits there is sorted by how long it lives. This document
says where that root is, what opts a repository in, what first setup asks,
and what a repository's config row decides.

## The root and its lifetimes

**One root the plugin owns holds everything the plugin keeps, sorted by how
long each file lives.** "Owns" means the plugin creates, moves and removes it
and its checkers define the formats, the way `.github/` is GitHub's. Three
lifetimes, each with one home: a session's state sits beside the root under
the common git directory and is never committed; a work item's directory,
`seal/specs/<id>/`, lives until the settle writes its spec's sections and
removes it;
everything else under `seal/`, with `docs/` and `CHANGELOG.md`, is
permanent. The layout, file by file, is `skills/implement/SKILL.md`
*Document layout — two roots, three lifetimes* and `docs/the-record-layout.md`.

**The plugin writes only to its own root.** A `specs/` directory anywhere
else is the project's own, read as history and never taken
(`templates/config.md` *Reference specs*). Where the root is, as a path a
session can type, is stated once, in contract rule 11.
check: tests/test_no_document_names_the_old_roots.py tests/test_optin.py

## The dependency rule

**Anything that must outlive a release may not read `seal/specs/<id>/` after
the merge.** `settle` removes the directory, so every permanent purpose
treats it as already gone. A round record's `target:` line is read only while
its pull request is open. A comment naming a work item, above a released
changelog entry, is a pointer rather than a read, and where the root is
shared it still resolves through git history once the folder is gone; in
local mode no history holds the folder, so the pointer names a work item
that has left. Every check in a repository
that reads the corpus owes an answer when a settle removes part of it
(`skills/settle/SKILL.md` *Answer every check that reads the corpus*). A new
reader of `seal/specs/<id>/` after the merge is a finding for the review
that meets it.

**Behind it is a wider rule: nothing may need to be found and updated when
something else moves.** A record citing `path:line` breaks it: a line moves
for edits unrelated to the claim, so the citation has to be re-anchored, and
a squash orphans it. A settle rewrites `docs/` and removes directories at
every release it is called for, so anything coupled to a path or a position
inside a work item breaks the same way. The coupling left is a round
record's `target:` line, read while its pull request is open and gone with the
record.

## The opt-in signal is the root itself

**A repository is opted in when `seal/` exists at its mode's location**:
`<repo>/seal/` in shared mode, `$(git rev-parse --git-common-dir)/seal/` in
local mode. The hooks look at the two places in that order; whichever exists
says both "on" and which mode. Nothing else is read, and there is no config
key: a git config key, a marker under `.git/` or a fetched ref would say
twice what the folder already says.

| | Shared mode | Local mode |
|---|---|---|
| Who decides | whoever committed `seal/`, for every clone that installed the plugin | the developer of that clone |
| A collaborator who set nothing up | gated, once the plugin is installed | runs nothing, because their clone has no root under its git directory |

A collaborator who never installed the plugin runs nothing in either mode,
because the hooks are the plugin's. The fail direction is that no folder at
either place means not opted in, and a hook that cannot tell does nothing.
A throwaway repository turns the gates off with an empty file,
`.git/specseal-scratch`, under the common git directory, which no commit can
carry to another clone.
check: tests/test_optin.py

## What first setup asks

**The one moment this project allows a question about the root is first
setup, and it asks one.** One `AskUserQuestion` with three options, in this
order, the first the default, each saying what it does:

- **shared, records only** creates `<repo>/seal/`, which the routing commit
  carries, and writes nothing under `.github/`.
- **shared, with pull-request checks** does the same, then runs
  `seal pr-checks install`, which writes `.github/workflows/hygiene.yml`
  from `templates/hygiene.yml` where that path is absent: a clone of the
  plugin at the release installed at setup, and the pull-request checks.
- **local** creates `$(git rev-parse --git-common-dir)/seal/`, touches nothing
  in the tree, and installs nothing, because the checks read committed files
  and local mode commits none.

A repository with `seal/` at either place has been through this and is never
asked again; the mode is read from where the folder is. A repository still on
the layout that came before the root is told, not asked, and the session-start
hook moves it once (`skills/implement/orchestration.md`, its bootstrap). Once
a root exists at either place, that hook stamps the repository as moved, so a
local-mode repository that later checks out an old branch is not moved into
the tree it chose to keep clean.
check: tests/test_first_setup_asks_once.py

### Shared or local

**The question is not "commit the folder or not" but "do collaborators and
every other clone see the records".** Which answer fits is mostly decided by whose repository
it is.

| | Local mode | Shared mode |
|---|---|---|
| Fits | a repository with its own conventions where this plugin's files must not appear in the tree: a company repository, a contribution to someone else's project. Also a solo repository that wants nothing extra committed | your own repository, or any repository where a committed `seal/` bothers nobody |
| Where `seal/` lives | `.git/seal/`, inside the common git dir | `<repo>/seal/`, in the tree |
| Committed | never; nothing to gitignore either | yes |
| Linked worktrees and parallel sessions | read each other's records, because the git dir is common to every worktree of the clone | read each other's records, because the files are committed |
| Other machines and a re-clone | start empty; `seal export` / `seal import` carry a copy by hand | have everything |
| CI (the pull-request checks) | cannot run; `seal pr-checks install` refuses here | runs where first setup's answer or `seal pr-checks install` put the workflow in the tree |
| Switching later | `seal mode shared` moves `.git/seal/` to `<repo>/seal/` and stages it; you commit | `seal mode local` moves `<repo>/seal/` back and stages the removal; you commit |

**`seal/config.md`'s `Mode` row is not the opt-in, and the difference is what
reads it.** The row says where the root *should* be; the folder's location
says where it *is*, and no hook, gate or check resolves the root through the
row: `hooks/optin.py#home_at` is the only reader of the question. A gate that
trusted a hand-editable row would look in a place with no folder, and that
module fails toward *not opted in* rather than toward a guess. What the row
buys is a repository that can say which mode it wants before the folder is
moved, and a check that names a disagreement left standing. An absent row is
filled in from where the folder is, the only value that cannot be wrong.

**Where the records live and whether CI checks pull requests are two
answers, and the workflow file is the record of the second.** `seal mode`
moves the root and writes the `Mode` row, and leaves `.github/` alone.
`seal pr-checks install` writes `.github/workflows/hygiene.yml` from
`templates/hygiene.yml` where that path is absent, pinned to the installed
release, and stages it. It refuses where `<repo>/seal/` is not a directory,
because the checks read committed records. `seal pr-checks remove` takes out
a workflow this plugin wrote and leaves any other file alone. No config row
says whether the checks are installed: the file says it, and a second record
would be a second answer. A workflow left behind in local mode and pinned to
a release that has the no-root state passes having examined nothing:
`chain_check.py`, the one record check it runs, finds no root in the tree,
so nothing is declared, and exits 0. One pinned to an older release fails every pull request there until
its `--branch` line moves or `seal pr-checks remove` takes it out, and
`seal mode local` names the pin when it leaves such a file.
check: tests/test_seal.py

**Local mode lives under the git directory, not in a gitignored folder.** A
linked worktree checks out committed files only, so an ignored
`<repo>/seal/` would be absent from every worktree, and parallel sessions
could not read each other's records. Under the common git directory the root
is shared by every worktree of that clone, never a commit candidate, and
needs no `.gitignore` line. Local mode has no per-branch isolation of
uncommitted state; the per-work-item layout keeps parallel items apart. It
never leaves that clone on that machine: a new machine or a re-clone starts
with no work-item records, and CI's pull-request checks cannot run. That is the
whole trade-off.

**Local records can be carried to another clone by hand, and a copy is not a
sync.** `seal export` zips the root alone, never the session state beside it,
into `seal-<repo>-<date>.zip` with a manifest naming the remote URL and the
HEAD SHA at export. `seal import <zip>` never overwrites: a missing file is
added, and a file already present with other bytes lands beside it as
`<name>.incoming<ext>`, reported and not asked about. The last copy wins and
the person tracks which rows went, so needing a copy twice is the signal to
switch to shared mode. `seal export --check` prints how many work items
changed since the last export, and nothing is uploaded anywhere.

**The mode is not a one-way door; the history is.** Going to shared puts the
records in the tree, and the moment that commit lands they are in the
repository's history; coming back removes them from the tree and not from the
history. That is the one direction local mode exists to prevent, so
`seal mode shared` says so before it acts and stages rather than commits,
which leaves the point of no return with the person.
check: tests/test_first_setup_asks_once.py tests/test_optin.py tests/test_seal.py

## Naming

**The product is SpecSeal, and bare `seal` is the vocabulary inside it**: the
root `seal/`, the `seal export` / `seal import` commands, "the seal" for the
record.

| Name | Its one sentence |
|---|---|
| SpecSeal | seals a spec to the code that implements it |
| `seal/` | the root, visible beside `docs/`, because the work items in flight are what people read while a pull request is open |
| `seal/specs/<id>/` | a work item's directory, named for the primary artifact it holds |

A directory says what is in it to whoever opens it first, so no directory is
named for a metaphor; smith and warden stay agent personas. Every shipped
artifact is written in English, because the plugin is for others and every
token is paid for. The language a repository's own records and pull requests
are written in is that repository's answer, below.

## What the repository decides for itself, and how it is read

`seal/config.md` is the one file a repository writes about itself, one row
per item, read by the checkers and editable by hand. The rows that exist are
documented in `templates/config.md`, and an absent row has a default that is
stated there rather than left to whoever reads the code.

**A setting nobody can find is a setting nobody has.** Every row is reachable
from a command that shows the whole file and routes a change, because first
setup asks its questions in one batch and never asks again, and the rows that
arrive after it would otherwise be found only by reading a template a person
has no reason to open. The routing layer holds no logic of its own: a row
with a side effect routes to the script that performs it, and a row that is
only a row is written directly. Logic inside a skill cannot be
mutation-tested the way a script can, and that is what decides where the line
runs.
check: tests/test_the_settings_have_a_front_door.py

**What language this plugin writes in is the repository's answer, not the
plugin's.** A skill that requires English of everyone is a decision made in a
file nobody who disagrees with it can edit, so the language lives in a config
row, and the mirror file a translated pull-request body goes in is named for
the language it holds rather than for one language.
check: tests/test_the_pull_request_language_is_the_repositorys.py tests/test_config.py

**Two rows, because one cannot express the middle answer.** The combinations
people actually want are three: everything English; the commits and pull
requests in the team's language with the documents in English; or both in it.
One row cannot say the middle, and one row per document kind is seven rows
where nobody sets the sixth differently from the fifth. So
`Commit and pull request language` governs what the outside world reads, the
commit subject and body and the pull request title and body, and
`Record language` governs the prose in the documents a work item writes.
Setting one does not carry the other, because the two surfaces have different
audiences: a pull request is read by whoever opens it, and a record by
whoever comes back to the decision six months later.

Whatever either row says, **the names a checker matches stay English**: the
field names, the verdict words, the markers, and all code. A translated field
name is not a translation; it is a checker that stops reading.
check: tests/test_the_pull_request_language_is_the_repositorys.py

**A cell may carry an escaped pipe, and one line that will not parse is named
rather than treated as the end of the table.** A value like a shell command
with a pipe in it is ordinary content, and a reader that stopped at it
silently took every row below it out of the config. The reader and the writer
share the constant that describes a row, because their disagreement about
which line is a given row is what turns one edit into a duplicate row in a
person's file.
check: tests/test_config.py tests/test_seal.py

**A git call that fails is not a git call that answered "nothing".** Empty
output because a thing is absent and empty output because the question could
not be asked are different facts, and a caller that cannot tell them apart
reports the absence as settled: no remote, no other worktree, no tracked
file. Every call site whose caller needs the distinction returns it, and the
refusal says which call failed rather than reporting a confident nothing.
check: tests/test_seal.py

# One root, laid out by lifetime

*English · [한국어](./one-root-by-lifetime.ko.md)*

Everything this plugin keeps in a repository sits under one root it owns,
`iadd/`, and what sits there is sorted by how long it lives. This document
says where that root is, what opts a repository in, what first setup asks,
and what a repository's config key decides.

## The root and its lifetimes

**One root the plugin owns holds everything the plugin keeps, sorted by how
long each file lives.** "Owns" means the plugin creates, moves and removes it
and its checkers define the formats, the way `.github/` is GitHub's. Three
lifetimes, each with one home: a session's state sits beside the root under
the common git directory and is never committed; a work item's directory,
`iadd/threads/<id>/`, lives until the settle writes its design's sections
and removes it; everything else under `iadd/`, with `docs/`, is permanent.
The layout, file by file, is `docs/layout/the-record-layout.md` *iadd/* and
*iadd/threads/<work-item-id>/*.

**The plugin writes only to its own root.** A `specs/` directory anywhere
else is the project's own, read as history and never taken
(`templates/setup/config.md` *Reference specs*), and no code of the plugin
opens a top-level `specs/` or `.specseal/` on its own. `iadd settle --from`
reads a directory only where a person names it at the settle, and writes
nothing there. Where the root is, as a path a session can type, is stated
once, in the opening paragraph of `skills/core/SKILL.md`.
check: tests/lib/test_optin.py

## The dependency rule

**Anything that must outlive a release may not read `iadd/threads/<id>/` after
the merge.** `settle` removes the directory, so every permanent purpose
treats it as already gone. A round record's `target:` line is read only while
its pull request is open. A comment naming a work item, above a released
changelog entry, is a pointer rather than a read, and where the root is
shared it still resolves through git history once the folder is gone; in
local mode no history holds the folder, so the pointer names a work item
that has left. Every check in a repository
that reads the corpus owes an answer when a settle removes part of it
(`skills/settle/SKILL.md` *Answer every check that reads the corpus*). A new
reader of `iadd/threads/<id>/` after the merge is a finding for the review
that meets it.

**Behind it is a wider rule: nothing may need to be found and updated when
something else moves.** A record citing `path:line` breaks it: a line moves
for edits unrelated to the claim, so the citation has to be re-anchored, and
a squash orphans it. A settle rewrites `docs/` and removes directories at
every release it is called for, so anything coupled to a path or a position
inside a work item breaks the same way. The coupling left is a record of
what a party ran at the branch's own commits: a round record's `target:`
line, and a `<commit>:<path>` that a work item's `trail/` or `inspection.md`
cites at such a commit. Both are read while the pull request is open and go
with the record. Every other `<commit>:<path>` names a commit `main` or a
release branch reaches (`docs/layout/the-record-layout.md`
*iadd/threads/<work-item-id>/*). A citation that names its unit by path and
heading, or by `path#name`, outlives the edits that move a line, and every
cited heading and name stands in its file.
check: tests/behaviour/test_a_cited_section_stands_in_its_file.py

## The opt-in signal is the root itself

**A repository is opted in when `iadd/` exists at one of the places the
opening paragraph of `skills/core/SKILL.md` names and its `README.md` opens
with the plugin's marker.** The marker is the first line of
`templates/setup/iadd-README.md`, written at first setup. The `iadd`
commands, the pull request's check and the stamp's `--stop` look at those
places in the core's order; the first that exists with the marker says both
"on" and which mode. An `iadd/` whose README does not open with the marker is a
project's own directory,
as a package named `iadd` has one, and reads as not opted in. First
setup that meets one writes nothing into it, and the root goes under the
git directory. Nothing else is read, and there is no config
key: a git config key, a marker under `.git/` or a fetched ref would say
twice what the folder already says.

| | Shared mode | Local mode |
|---|---|---|
| Who decides | whoever committed `iadd/`, for every clone that installed the plugin | the developer of that clone |
| A collaborator who set nothing up | in the IADD process, once the plugin is installed | runs nothing, because their clone has no root under its git directory |

A collaborator who never installed the plugin runs nothing in either mode,
because the hooks, the skills and the `iadd` commands are the plugin's. The fail
direction is that no folder at either place means not opted in, and a
command that cannot tell reads the repository as not opted in.
A throwaway repository reads as not opted in with an empty file,
`.git/iadd-scratch`, under the common git directory, which no commit can
carry to another clone.
check: tests/lib/test_optin.py

## What first setup asks

**The one moment this project allows a question about the root is first
setup, and it asks one.** One `AskUserQuestion` with three options, in this
order, the first the default, each saying what it does:

- **shared, records only** creates `<repo>/iadd/`, which the routing commit
  carries, and writes nothing under `.github/`.
- **shared, with pull-request checks** does the same, then runs
  `iadd pr-checks install`, which writes `.github/workflows/hygiene.yml`
  from `templates/setup/hygiene.yml` where that path is absent: a clone of the
  plugin at the release installed at setup, and the pull-request checks.
- **local** creates `$(git rev-parse --git-common-dir)/iadd/`, touches nothing
  in the tree, and installs nothing, because the checks read committed files
  and local mode commits none.

A repository with `iadd/` at either place has been through this and is never
asked again; the mode is read from where the folder is.
check: tests/behaviour/test_first_setup_asks_once.py

### Shared or local

**The question is not "commit the folder or not" but "do collaborators and
every other clone see the records".** Which answer fits is mostly decided by whose repository
it is.

| | Local mode | Shared mode |
|---|---|---|
| Fits | a repository with its own conventions where this plugin's files must not appear in the tree: a company repository, a contribution to someone else's project. Also a solo repository that wants nothing extra committed | your own repository, or any repository where a committed `iadd/` bothers nobody |
| Where `iadd/` lives | `.git/iadd/`, inside the common git dir | `<repo>/iadd/`, in the tree |
| Committed | never; nothing to gitignore either | yes |
| Linked worktrees and parallel sessions | read each other's records, because the git dir is common to every worktree of the clone | read each other's records, because the files are committed |
| Other machines and a re-clone | start empty; `iadd export` / `iadd import` carry a copy by hand | have everything |
| CI (the pull-request checks) | cannot run; `iadd pr-checks install` refuses here | runs where first setup's answer or `iadd pr-checks install` put the workflow in the tree |
| Switching later | `iadd mode shared` moves `.git/iadd/` to `<repo>/iadd/` and stages it; you commit | `iadd mode local` moves `<repo>/iadd/` back and stages the removal; you commit |

**`iadd/config.json`'s `Mode` key is not the opt-in, and the difference is
what reads it.** The key says where the root *should* be; the folder's
location says where it *is*, and no hook, gate or check resolves the root
through the key: `lib/optin.py#home_at` is the only reader of the question.
A gate that trusted a hand-editable key would look in a place with no
folder, and that module fails toward *not opted in* rather than toward a
guess. What the key buys is a repository that can say which mode it wants
before the folder is moved, and a check that names a disagreement left
standing. An absent key is filled in from where the folder is, the only
value that cannot be wrong.

**Where the records live and whether CI checks pull requests are two
answers, and the workflow file is the record of the second.** `iadd mode` moves the root and writes the `Mode` key, and leaves `.github/` alone.
`iadd pr-checks install` writes `.github/workflows/hygiene.yml` from
`templates/setup/hygiene.yml` where that path is absent, pinned to the installed
release, and stages it. It refuses where `<repo>/iadd/` is not a directory,
because the checks read committed records. `iadd pr-checks remove` takes out
a workflow this plugin wrote and leaves any other file alone. No config key
says whether the checks are installed: the file says it, and a second record
would be a second answer. A workflow left behind in local mode and pinned to
a release that has the no-root state reads nothing as declared:
`chain_check.py`, the one record check it runs, finds no root in the tree, so
nothing is declared, and judges the commit trailers alone. It passes the
commits a local-mode session writes, which carry no `IADD-Routing` trailer,
and fails a ready pull request where a commit made before the switch carries
a trailer naming a work item. One pinned to an older release fails every pull
request there until its `--branch` line moves or `iadd pr-checks remove`
takes it out, and `iadd mode local` names the pin when it leaves such a file.
check: tests/skills/test_iadd.py

**Local mode lives under the git directory, not in a gitignored folder.** A
linked worktree checks out committed files only, so an ignored
`<repo>/iadd/` would be absent from every worktree, and parallel sessions
could not read each other's records. Under the common git directory the root
is shared by every worktree of that clone, never a commit candidate, and
needs no `.gitignore` line. Local mode has no per-branch isolation of
uncommitted state; the per-work-item layout keeps parallel items apart. It
never leaves that clone on that machine: a new machine or a re-clone starts
with no work-item records, and CI's pull-request checks cannot run. That is the
whole trade-off.

**Local records can be carried to another clone by hand, and a copy is not a
sync.** `iadd export` zips the root alone, never the session state beside it,
into `iadd-<repo>-<date>.zip` with a manifest naming the remote URL and the
HEAD SHA at export. `iadd import <zip>` never overwrites: a missing file is
added, and a file already present with other bytes lands beside it as
`<name>.incoming<ext>`, reported and not asked about. The last copy wins and
the person tracks which rows went, so needing a copy twice is the signal to
switch to shared mode. `iadd export --check` prints how many work items
changed since the last export, and nothing is uploaded anywhere.

**The mode is not a one-way door; the history is.** Going to shared puts the
records in the tree, and the moment that commit lands they are in the
repository's history; coming back removes them from the tree and not from the
history. That is the one direction local mode exists to prevent, so
`iadd mode shared` says so before it acts and stages rather than commits,
which leaves the point of no return with the person.
check: tests/behaviour/test_first_setup_asks_once.py tests/lib/test_optin.py tests/skills/test_iadd.py

## What the repository decides for itself, and how it is read

`iadd/config.json` is the one file a repository writes about itself, one
JSON object with one key per item, read by the checkers and editable by
hand. The keys that exist are documented in `templates/setup/config.md`,
which also states what an absent key means, rather than leaving it to
whoever reads the code.

**A setting nobody can find is a setting nobody has.** Every key is
reachable from a command that shows the whole file and routes a change,
because first setup asks its questions in one batch and never asks again,
and the keys that arrive after it would otherwise be found only by reading
a template a person has no reason to open. The routing layer holds no logic
of its own: a key with a side effect routes to the script that performs it,
and a key that is only a key is written directly. Logic inside a skill cannot be
mutation-tested the way a script can, and that is what decides where the line
runs.
check: tests/text/test_the_settings_have_a_front_door.py

**What language this plugin writes in is the repository's answer, not the
plugin's.** A skill that requires English of everyone is a decision made in a
file nobody who disagrees with it can edit, so the language lives in a config
key, and the mirror file a translated pull-request body goes in is named for
the language it holds rather than for one language. The two language keys of
`iadd/config.json` are required: first setup and the batch before a work
item's first edit ask for them, with the language of the recent pull request
titles shown beside the question, and `iadd pr-body` refuses to compose a body
without them. Where nobody is there to answer, the orchestrator writes them as
the titles' language and `routing.md` says so. A commit is never refused for
them.
check: tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/lib/test_config.py

**Two keys, because one cannot express the middle answer.** The combinations
people actually want are three: everything English; the commits and pull
requests in the team's language with the documents in English; or both in it.
One key cannot say the middle, and one key per document kind is seven keys
where nobody sets the sixth differently from the fifth. So
`Commit and pull request language` governs what the outside world reads, the
commit subject and body and the pull request title and body, and
`Record language` governs the prose in the documents a work item writes.
Setting one does not carry the other, because the two surfaces have different
audiences: a pull request is read by whoever opens it, and a record by whoever
comes back to the decision six months later. Where the two keys differ, the
pull request body opens with `pr.<lang>.md`, written in the team's
language, and `pr.md` follows it, so the records keep one language
and the team reads the body in theirs.

Whatever either key says, **the names a checker matches stay English**: the
field names, the verdict words, the markers, and all code. A translated field
name is not a translation; it is a checker that stops reading.
check: tests/behaviour/test_the_pull_request_language_is_the_repositorys.py

**The file is read by the standard library's JSON parser and written by its
serializer, and what will not read is refused, never read as absent.** A
parser's result is a fact a script reads exactly, and a markdown table read
by a walker held to a renderer is not one: each shape the two could
disagree on was a defect of its own. A file that will not parse, or whose
top level is not an object, is refused whole. A key written twice, or one
whose value is not a string, has no value, and every other key is read.
Each value is a string in the grammar `templates/setup/config.md` gives
its key, so a shell command carries a pipe as written.
check: tests/lib/test_config.py tests/skills/test_iadd.py

**A git call that fails is not a git call that answered "nothing".** Empty
output because a thing is absent and empty output because the question could
not be asked are different facts, and a caller that cannot tell them apart
reports the absence as settled: no remote, no other worktree, no tracked
file. Every call site whose caller needs the distinction returns it, and the
refusal says which call failed rather than reporting a confident nothing.
check: tests/skills/test_iadd.py

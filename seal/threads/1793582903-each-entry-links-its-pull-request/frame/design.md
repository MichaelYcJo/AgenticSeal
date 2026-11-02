# Design: each entry links its pull request (#1139)

Every coordinate below was opened in the worktree at `55dd3c585`, the tip of
`feat/1139-a-released-entry-reaches-its-work-only-through-a-hidden-id`. That
branch was cut from `release/v0.28.0` at `405109767`, which holds #1215, #1054
and #1045. The issue had no comments when the orchestrator read it on
2026-11-02 with `gh issue view 1139 --json body,comments` (the orchestrator's
finding, carried here as its spawn prompt states it).

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/branch-and-release.md` *Cutting a release*: "The fragments follow, folded, each under an HTML comment naming its work item." | The rule this work rewrites, through `## Rule changes`. It is the text #1053's design (`f15b3f998:seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md` *Rule changes*) wrote and a later settle landed, so the issue's third *Done when* item is met by rewriting the policy text where it now stands. |
| `docs/branch-and-release.md` *Work accumulates on a release branch*: the fragments are written "each under an HTML comment naming its work item, invisible to a reader and the only link from a released entry back to the work that produced it" | The same rule's second statement. It is rewritten in the same `## Rule changes`, and the marker's mentions outside the policy root go in the build (`## Removes`). |
| `docs/the-record-layout.md` *A change writes fragments, never a shared file*: "The GitHub Release at the tag is the release's notes … A fragment lives from the work item's first entry to the settle after the release that ships it, and the history keeps it after that." | The published note is the one copy outside the history. The settle is the step that leaves the history as the only copy, so the settle is where a note that lacks the entry is caught. |
| `docs/the-record-layout.md` *The fold, and what tells it from a deletion*: "`seal settle --apply` removes a directory only once its record holds no open row in the working tree." | The condition this work adds to. The added rule goes into that section through an `add`, beside the open-row rule it extends. |
| `docs/release-checklist.md` *2b. Settle what earlier releases left behind*: "The second removes every released work item directory whose record holds no open row, and names any it keeps." | This restates the removal condition, so it changes with it. |
| `docs/release-checklist.md` *6. After the merge*: the box "A GitHub Release exists at `vX.Y.Z`" | A release that was never published is already caught at the box that follows the merge. The settle check therefore reads a note only where one exists (`questions.md` Q1). |
| `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A script holds a gate only on a fact it reads exactly … It names as not read a line or a file that looks like one of its form's and is not one, and decides nothing on it." | The settle keeps a directory only on three facts it reads exactly: the releases API's JSON, a URL string in the note's body, and the `(#N)` that ends a commit subject. Where one of them is missing, it names the work item as one whose note it did not read, and decides nothing on that. |
| `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A mechanism stays only while its record of what it caught outweighs what it costs" | The new check on `--apply` is a mechanism. `## Removes` names what goes in return: the hidden marker, whose writer no script read. |
| `skills/settle/SKILL.md` *In local mode*: "A `gh` that cannot be asked stops the run." | The issue asks for the same stop when the release list cannot be read. The skill's sentence "Shared mode never asks `gh`." stops being true and is rewritten. |
| #1053, merged as `f15b3f998` (#1140); its design *Scope* items 1 and 3 (read at that commit) | Built on: the note is read from the history at the tag, `--full-history` reaches a fragment that a settle removed before the tag (0.22.4), and a fragment the previous tag holds is skipped (0.15.3). Departed from: item 3 put each fragment "under an HTML comment `<!-- specs/<work-item-id> -->`". The grounds for the departure: the comment's only reader was a person, who had to search the history for the id (`git log --all -- seal/threads/<id>/`), and no script reads it (`git grep -n '<!-- specs/'` outside `seal/threads/` finds the writer at `.github/scripts/publish_release_note.py:292` and no reader, executed). |
| #1117, merged as `6310a6e85` (#1144), as `.github/scripts/publish_release_note.py`'s docstring states it (read) | Built on: the tag is created by the publish workflow on the push to `main`, and the note is built in the same CI run. So the pull request number is computed once, by CI, at the tag. The process rows that `section` lifts into one table stay as they are. |
| #1044, merged as `5e5275e53` (#1103); its design *Scope* items 1 to 3 (read) | Built on: `seal pr-body` copies the records' text into the pull request body, where it stays after the settle removes the directory. A link to the pull request leads to that text in one click. |
| The owner's report, in the issue, that an early note naming commit SHAs was dropped as inefficient | Built on: the link names the pull request, never a commit. An entry whose adding commit names no pull request gets no link, and no SHA in its place. |
| #1054, merged as `5161c421e` (#1284): `--from` is refused beside `--apply` (`skills/settle/SKILL.md` *What `--apply` does*, read) | Untouched. The note check runs only in `--apply`, so `--from` never meets it. |
| Executed 2026-11-02, a read-only probe over the ten releases `v0.24.0` to `v0.27.3` (the ones built since #1053), `git log --no-renames --diff-filter=A --full-history --format='%h%x09%s' <previous>..<tag> -- seal/threads/<id>/changelog.md` per fragment, with `gh release view <tag> --json body` and `gh pr list --state merged --limit 1500 --json number` | Of 54 fragments, each has exactly one adding commit in its range, and each adding commit's subject ends with `(#N)`, where N is a merged pull request. Each published note carries `<!-- specs/<id> -->` for each of its fragments, and none carries a `https://github.com/<owner>/<name>/pull/<N>` link. So the subject reading gives a number for every entry since #1053. The seven released work items in the tree at `v0.27.3` would each be kept by a check that reads only the new link (*Scope* item 4 reads the old marker for that reason). |
| Executed 2026-11-02, `gh api --paginate 'repos/{owner}/{repo}/releases?per_page=100' --jq '.[] \| [.tag_name, .draft] \| @tsv'` from the worktree | Exit 0 and 68 releases listed, so one call lists every release with its `tag_name`, `draft` and `body`, and gh resolves `{owner}/{repo}` from the checkout's remote. |
| Read: the 26 of 58 published notes that did not hold their release file's text, as #1053's design *Scope* item 5 states its measurement of 2026-10-28 | This is the drift the settle check catches at the step that would make it permanent. It was measured by #1053, and this work did not re-measure it. |

## Scope

In scope:

1. **Each entry links its pull request, and the hidden marker goes.**
   `.github/scripts/publish_release_note.py` reads, for each fragment it
   selects, the commit of the range that added it: the oldest commit
   that `git log --no-renames --diff-filter=A --full-history <range> -- <path>`
   lists. Where that commit's subject ends with `(#N)`, the entry's first
   line is the link `[#N](https://github.com/<REPO>/pull/N)`, on the line
   `<!-- specs/<id> -->` held, and the fragment's text follows. Where the
   subject ends with no `(#N)`, the entry is the fragment's text alone. No
   entry carries the marker. The docstring and the `section` docstring say
   so.
2. **One reader of a fragment's adding commit and its pull request.** The
   oldest adding commit and the trailing `(#N)` of its subject are read by
   one function, which the renderer (over the tag's range) and the settle
   (over `--released-at`) both import. Where several `(#N)` end the subject,
   as in a title that ends with its issue, the last one is the pull request,
   because GitHub appends it to the title when it squashes.
3. **The marker leaves the documents that name it.** Nothing writes
   `<!-- specs/<work-item-id> -->` any more. Its mentions as a marker that
   stays English, and as the key the release note carries, go, together
   with the old-roots check's entry that keeps it (`## Removes`).
4. **`seal settle --apply` keeps a released directory whose published
   note does not carry its entry, and names it.** The check runs after the
   open-row check, for each directory that check would remove. A work item
   is checked when its `changelog.md` is at `--released-at`, and when a
   `vX.Y.Z` tag holds that fragment's adding commit (item 2). The version
   is the lowest such tag. Its note is the release in one
   `gh api --paginate repos/{owner}/{repo}/releases` list whose `tag_name`
   is that tag and whose `draft` is false. The note carries the entry where
   its body holds `https://github.com/<owner>/<name>/pull/<N>` with no digit
   after N, for any owner and name, or `<!-- specs/<id> -->`, the marker
   that notes published before this change carry. A directory whose note
   carries neither is kept and named, with the tag, the pull request
   number, and the commit and path where its fragment's text can be read.
   The list is read once, before the first removal, and only where some
   directory to be removed has a version tag. A list that cannot be read
   stops the run with exit 2 and removes nothing, as an unanswerable `gh`
   already does in local mode. Where no note can be read for a work item,
   its directory goes as before, and the line under `removed` says which
   case applied: no fragment, no pull request named, no version tag, or no
   published release at the tag (`questions.md` Q1).
5. **The settle's own text states it.** `skills/settle/SKILL.md` covers the
   usage block, *What `--apply` does*, *In local mode* (its sentence that
   shared mode never asks `gh`), and the procedure's pull-request-body
   step, which names each directory kept for its note so the owner can
   repair the note. The other places are the docstring and `--apply` help
   of `skills/settle/scripts/settle.py`, the line in
   `templates/setup/seal-README.md` that restates what `--apply` removes,
   and the `seal settle [--apply]` row of `README.md` and `README.ko.md`.
6. **The policy text changes through `## Rule changes`**, which the settle
   after the release writes.

Out of scope:

- The note's layout beyond the entry's link line: the owl and the stamp
  side by side, and each category folded under its name and count, are
  #1153's, which follows this work item and edits the same renderer.
- `seal pr-body`'s `<details>` refusal (#1218), and the config rows that
  show the seal mark (#1204).
- `seal settle --draft` (#1217) and #1281, which follow this work item and
  edit `skills/settle/SKILL.md` and `settle.py`.
- The dry run. It asks no `gh` in shared mode and stays that way. The note
  is read by `--apply` alone (`plan.md` *Alternatives considered*).
- Local mode. No fragment is committed there, so no note is built from the
  history, and `--apply` removes as it does today.
- Editing a published note. The settle names a directory kept for its note
  and edits nothing on GitHub. Repairing the note is the owner's act.
- The 26 published notes #1053 left as they are. Their work items were
  settled long ago and nothing here reads them.
- `tests/skills/test_unverified_check.py`'s `live_lines` cases on
  marker-shaped lines (`MARKER`, `:675`). They pin how `live_lines` reads a
  comment-shaped line, which needs no writer of the marker.
- `.claude-plugin/plugin.json`.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 an entry links its pull request | Given a range whose fragment was added by a commit whose subject ends `(#42)`. When the note is built with `REPO=o/r`, then the entry opens with the line `[#42](https://github.com/o/r/pull/42)` followed by the fragment's text, and the body holds no `<!-- specs/`. | A case in `tests/github/test_publish_release_note.py`, seen red against the current renderer |
| S2 an entry whose adding commit names no pull request | Given the adding commit's subject ends with no `(#N)`. Then the entry is the fragment's text with no link line and no marker. | A case in the same module, seen red |
| S3 the adding commit names the number, not a later edit | Given a fragment added by `... (#42)` and edited in the same range by `... (#43)`. Then the entry links #42. Given a subject `title (#7) (#42)`, the entry links #42. | Cases in the same module |
| S4 the settle keeps a directory its note does not carry | Given a released work item whose fragment was added by `... (#42)`, a tag `v1.2.3` that holds that commit, and a stubbed release list where `v1.2.3`'s body carries neither the pull request's URL nor `<!-- specs/<id> -->`. When `seal settle --apply` runs, then it exits 1, the directory stays, and its `kept` line names `v1.2.3`, `#42`, and where the fragment can be read. | A case in `tests/skills/test_settle.py` with a `gh` stub on PATH, seen red |
| S5 a carried entry goes | The same tree, where the body carries `https://github.com/o/r/pull/42` (or `<!-- specs/<id> -->`). Then the directory is removed and the exit is 0. A body that carries only `https://github.com/o/r/pull/420` does not carry #42. | Cases in the same module |
| S6 an unreadable list stops the run | Given a `gh` stub that fails or prints something that is not a JSON list. Then the run exits 2 with one sentence naming `gh` and what it said, and removes no directory, including those that need no note. | A case in the same module, seen red |
| S7 no note to read | Given a released work item with no `changelog.md`, one whose adding commit names no pull request, one that no `vX.Y.Z` tag holds, and one whose tag has no release (or only a draft) in the list. Then each is removed, and the line under its `removed` line names which case held. Given no candidate with a version tag, `gh` is never run: a `GH` that is not on PATH leaves the exit at 0. | Cases in the same module |
| S8 an open row still decides first | Given a directory whose record holds an open row and whose note lacks its entry. Then it is kept for the row, as today, and the note is not read for it. | A case in the same module |
| S9 the rule changes parse | `skills/settle/scripts/rule_changes.py#parse` reads this design's `## Rule changes` with no refusal and no unread line. | Executed by the framer in a scratch clone (`plan.md` *Technical context*), and by `seal chain-check` at the pull request |

## Data & interfaces

- **The adding commit and its number** (*Scope* item 2): a function taking
  the repository's top, a revision range or ref, and a fragment's path. It
  returns `(commit, number or None)` for the oldest commit that
  `git log --no-renames --diff-filter=A --full-history --format=%H%x00%s <revisions> -- <path>`
  lists, or `(None, None)` where none adds it. The number is the digits of
  the last `(#N)` that ends the stripped subject. `--full-history` is needed
  for the reason `publish_release_note.py#fragments` gives: the tag is a
  merge into `main` whose first parent never held the path. The crafter
  picks the module both import (`questions.md` Q3).
- **The entry** (*Scope* item 1): `section(entries, repo)`, where each
  entry carries `(work item id, body, number or None)`. The entry's first
  line is `[#N](https://github.com/{repo}/pull/N)`, where it has a number.
  `REPO` is already in the publish step's environment
  (`.github/workflows/publish-release.yml:90`).
- **The release list** (*Scope* item 4):
  `gh api --paginate 'repos/{owner}/{repo}/releases?per_page=100'`, run from
  the repository's top with the same `GH` and `GH_TIMEOUT` as
  `settle.py#merged_pull_requests`. It raises `Unasked` where `gh` is not
  on PATH, does not run, exits non-zero, or answers anything but a list of
  objects, so the existing `UNASKED` sentence and exit 2 answer it.
- **The version**: the lowest `vX.Y.Z` among
  `git tag --contains <commit> --list 'v*'`, read by number as
  `publish_release_note.py#previous_tag` reads tags. A tag of any other
  shape is no version.
- **Carried**: the body holds a match of
  `https://github\.com/[^/\s]+/[^/\s]+/pull/<N>(?!\d)`, or the literal
  `<!-- specs/<id> -->`. Any owner and name are accepted because a
  repository renamed after a note was published keeps the old name in that
  note's links, and GitHub redirects them.
- **Output**: a `kept` line for a note, in the shape of the open-row `kept`
  line, ends by saying what to do (repair the note, then run
  `seal settle --apply` again). A line under `removed` says no note was
  read and why, in the shape of the `not read:` lines. The closing count
  line names the directories kept for a note apart from those kept for a
  row. Every new or changed line is pinned by a case (contract rule 14).
- **Exit codes**: 1 also covers a directory kept for its note. 2 also
  covers a release list that cannot be read.

## Rule changes

- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: The fragments follow, folded, each under an HTML comment naming its
    work item.
  to: The fragments follow, folded, each under a link to the pull request
    that added it.
- change
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: and writes each under an HTML comment naming its work item, invisible
    to a reader and the only link from a released entry back to the work that
    produced it.
  to: and writes each under a link to the pull request that added it. The
    commit of the range that adds a fragment is its pull request's squash
    commit, whose subject ends with `(#N)`, so the number is read once, at
    the tag, from the history. The pull request's body holds the records'
    text (`seal pr-body`), so one click leads from an entry to the reasons
    behind it. A fragment whose adding commit names no pull request is
    written with no link.
- add
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  to: **`seal settle --apply` keeps a released work item's directory whose
    version's published note does not carry its entry, and names it.** The
    published note is the one copy of a fragment outside the history, and
    the settle is the step that leaves the history as the only copy, so a
    note that lost an entry is caught there, before it becomes permanent.
    The version is the lowest `vX.Y.Z` tag that holds the commit adding the
    work item's `changelog.md`, and the note is that tag's published GitHub
    Release. The note carries the entry where it links the pull request
    that commit names, or where it holds the comment naming the work item
    that notes carried before entries linked their pull requests. A release
    list that cannot be read stops the run and removes nothing. A work item
    with no fragment, no pull request named, no version tag or no published
    release at its tag has no note to read, and its directory goes as the
    open-row rule decides, with the reason printed beside it.
    check: tests/skills/test_settle.py
- change
  file: docs/release-checklist.md
  section: 2b. Settle what earlier releases left behind
  from: The second removes every released work item directory whose record
    holds no open row, and names any it keeps.
  to: The second removes every released work item directory whose record
    holds no open row and whose version's published note carries its entry,
    and names any it keeps with why. The settle's pull request body names
    each directory kept for its note, and the owner repairs that note
    before a later `--apply` removes it.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The hidden marker each entry was written under, `<!-- specs/{item} -->` | `.github/scripts/publish_release_note.py#section` | The pull request link (*Scope* item 1). This is what the new `--apply` check takes out in return. The marker's catch record is empty: no script reads it (`git grep`, executed, *Grounding*), and its one reader was a person searching the history for the id. |
| The docstring sentence "Each goes under an HTML comment naming its work item, the one link from a released entry back to the work that produced it." | `.github/scripts/publish_release_note.py`, module docstring, `:24-25` | A sentence saying each entry links the pull request that added it, and why. |
| `<!-- specs/<work-item-id> -->` in the list of what stays English | `skills/implement/SKILL.md` *The language the records are written in*, `:61` | Nothing writes the marker into a record or a note, so there is nothing to keep English. The settle reads the old marker in published notes, which no record language governs. |
| `<!-- specs/<work-item-id> -->` in *The markers and anchors* | `templates/setup/config.md` *What no row governs*, `:145` | The same reason. The item keeps its other markers and anchors. |
| The clause "and the `<!-- specs/<work-item-id> -->` marker the release note carries above that fragment", with "the rename moves both" adjusted to the one share left | `skills/implement/multi-repository.md`, `:28-30` | The id still names the fragment's directory. The note no longer carries it. |
| The `KEEP` entry `"<!-- specs/<work-item-id> -->"` and the docstring line naming that marker as history kept on purpose | `tests/behaviour/test_no_document_names_the_old_roots.py`, `:15` and `:50` | Each `KEEP` entry is checked to still occur, and none of the scanned documents names the marker once the three rows above go. `skills/settle/SKILL.md` describes the old marker in words, so it needs no entry. |
| The cases' pins of the marker | `tests/github/test_publish_release_note.py`, `:239`, `:248`, `:296-298`, `:538-539`, `:569`, `:847-870` | Rewritten to the link form, or to the bare fragment where a case's range has no `(#N)`. The behaviour each case pins is otherwise unchanged. |
| "Shared mode never asks `gh`." | `skills/settle/SKILL.md` *In local mode*, `:483` | A sentence saying when shared mode asks `gh`: for the release list, only where a directory to be removed has a version tag. |
| The policy sentences on the marker, and the removal condition the checklist restates | `docs/branch-and-release.md`, `docs/release-checklist.md` | `## Rule changes` above, written at the settle, never by this pull request. |

Framed 2026-11-02 by framer, before the build.

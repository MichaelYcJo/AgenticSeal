# Feature Specification: 1793188384-the-release-notes-are-kept-twice

Issue #1053. Every coordinate below was opened at `8a1173c8`, the tip of
`origin/release/v0.24.0` this work item's branch was cut from; the branch's
only later commit, `91e85823`, adds `routing.md` and nothing else. Issue
#1117 lands after this work and changes the same publishing path, and the
seam this work leaves it is stated under *Scope*.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against*: "A fact has one source, and every other place links to it." | A change's note is written once, in its work item's `changelog.md`. The GitHub Release at the tag is the published form, built from the fragments. `changelog/` and `CHANGELOG.md` are a third place holding the same text, and they go. |
| `CLAUDE.md` *The rule a mechanism is kept against*: "A mechanism stays only while its history shows what it caught against what it costs" | The hygiene step that runs `gather_changelog.py --check`, and the gather's refusals of a fragment carrying a `## ` line (#586) or leaving a block open (#584), each guarded the gathered file or its section reader. With no gathered file and no section reader, each is weighed in `plan.md`'s Alternatives table and goes. |
| `CLAUDE.md` *The rule a mechanism is kept against*: "A change rewrites the text it amends in place, and in the same commit removes what stood on the old fact: a check, an exception, a comment, a copy." | Every case, comment, census entry and sentence outside the policy root that names `changelog/`, `CHANGELOG.md` or the gather is removed or re-pointed in the phase that removes what it names (`## Removes`). |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*: the policy root "is the baseline, and a pull request does not edit it" | `docs/the-record-layout.md`, `docs/branch-and-release.md`, `docs/release-checklist.md`, `docs/one-root-by-lifetime.md`, its `.ko.md` edition and `docs/issues-and-milestones.md` change through `## Rule changes` only. `CLAUDE.md`, `CONTRIBUTING.md` and the skills are outside the policy root, and the build edits them in place. |
| `tests/test_the_retired_rules_await_their_settle.py` at `de11df75^`, module docstring (read): a test file a `check:` line names is kept with no case until the settle that applies the rule change, and a retired marker is carried by a caseless class | `docs/release-checklist.md:67`, `:74`, and `docs/the-record-layout.md:47`, `:336` name `tests/text/test_the_changelog_is_gathered_at_release.py`, `tests/github/test_gather_changelog.py` and the marker `second-gather-appends` on their `check:` lines. `seal rules --check` refuses a target that does not resolve (`.github/scripts/rules.py#unresolved`). So the two files stay with no case, and the marker stays on a caseless class, until the settle; the settle's pull request deletes them. |
| `docs/branch-and-release.md` *Cutting a release*: the tag's job "never republishes a release that exists" | The workflow keeps that rule, and this work republishes no note: the 26 notes that lack their file's text are left as they are (*Scope* item 5). |
| `docs/release-checklist.md` *6. After the merge*: "A missing title line is not one of them: it falls back to the tag name." | The theme line is read the way the title is: a milestone that cannot be read, or carries no description, leaves the note without a theme line and the job log says which. It never fails the job. |
| `docs/issues-and-milestones.md` *A milestone answers when, and takes three shapes*: "A scheduled release milestone's description states the release's purpose" | The theme line's source is the milestone `release: X.Y.Z`'s description. Most descriptions since 0.15.0 open with `Purpose:` (read: the milestone list, 2026-10-28), and some earlier ones carry none. |
| `docs/the-record-layout.md` *The fold, and what tells it from a deletion*: "A line that EXCUSES or DECLARES something — a changelog marker, ..." | The changelog marker is read through `live_lines` only by `gather_changelog.py#live_markers`. With the gather gone the example names a reader that no longer exists, so `## Rule changes` replaces it. |

## Scope

In scope:

1. **The tag's step builds the note from the fragments, read from the
   history.** `.github/scripts/publish_release_note.py` stops reading
   `changelog/X.Y.Z.md`. For a tag `vX.Y.Z` it takes the previous version
   tag, the highest `vA.B.C` tag merged into the tagged commit's first
   parent, and reads every `seal/threads/<work-item-id>/changelog.md` that a
   commit in that range added and the previous tag does not already hold: a
   fragment that tag holds was released there, though a commit in the range
   restored its directory (0.15.3). Each fragment's text is the blob at the newest
   commit of the range whose tree holds the path, so a fragment a settle
   removed before the tag is still read. This answers the issue's question
   of where the work items are found once the settle has removed their
   directories: from the history, never from a file built before the settle.
   Executed on 2026-10-28 for the eleven releases 0.19.0 to 0.23.1: the set
   of work item ids this selection gives equals the set of markers in each
   release's `changelog/X.Y.Z.md`, including 0.22.4, whose own fragments the
   settle in `de11df75` removed before the tag. The tree at `v0.22.4` holds
   no `changelog.md` at all (executed, `git ls-tree`), so a selection that
   read the tree at the tag would have given that release an empty note.
2. **The note opens with the release's theme.** The theme is one sentence
   of the description of the milestone titled `release: X.Y.Z`: the leading
   `Purpose:` label, where there is one, is left out, the sentence runs to
   the first `.` followed by whitespace or the end of the text, or to the
   first line end if that comes first, its whitespace is collapsed, and its
   first letter is upper-cased. It stands alone as the note's first line. A
   milestone that cannot be listed, is not found, or has an empty
   description gives no theme line, and the job log says which of the three
   it was.
3. **The note's body.** The note is the theme line, then what it is today
   (the glance block, one line per pull request under its type, the thanks,
   how to update), then the fragments folded under the existing
   `📋 Full changelog — what each change does and why` summary, each under
   an HTML comment `<!-- specs/<work-item-id> -->` and in work item id
   order. The line linking to `changelog/X.Y.Z.md` at the tag goes. With no
   pull request to read, the note is the theme line and the fragments,
   unfolded, as it is the section alone today.
4. **The gather goes.** `.github/scripts/gather_changelog.py`, the hygiene
   step that runs its `--check`, and the step's row in
   `skills/verify/scripts/broad_gate.py` go.
5. **`changelog/` and `CHANGELOG.md` go**, and the 26 published notes that
   lack their file's text are left as they are. Executed on
   2026-10-28 for all 58 versions (58 files, 58 tags, 58 releases): 32
   notes hold their file, and 26 do not. The criterion: each paragraph of
   the file below its heading line, whitespace collapsed, is a substring of
   the note with whitespace collapsed. The 26 are 0.2.0, 0.3.0, 0.4.0,
   0.5.0, 0.6.0, 0.7.0, 0.8.0, 0.8.1, 0.8.2, 0.8.3, 0.9.0, 0.9.1, 0.9.2,
   0.9.3, 0.9.4, 0.9.5, 0.10.0, 0.11.0, 0.11.1, 0.11.2, 0.11.3, 0.11.5,
   0.12.0, 0.12.2, 0.12.3 and 0.13.0. The owner decided on 2026-10-28 not
   to republish them (`frame/questions.md` Q2): every file stays readable at
   `v0.23.1` after the removal, `git show v0.23.1:changelog/X.Y.Z.md`, the
   26 are releases from before 0.14.0 that no reader traces, and editing 26
   published releases, each backed up first, buys no reader anything. The
   issue's "republished from the file" is not built. A version's own tag
   is no source: #770 split the per-release files out of `CHANGELOG.md`, so
   the 44 tags before `v0.18.1`, the 26 above among them, hold no file of
   their own, and `v0.23.1` holds all 58.
6. **The `update` skill reads what it needs elsewhere.** Step 2b confirms
   the update landed by the `version` of the installed copy's
   `.claude-plugin/plugin.json`. Step 3 shows what changed from the GitHub
   Releases after the old version up to the new one, oldest first, read from
   the public API without credentials, the repository taken from the
   marketplace clone's `origin` remote. A read that fails says so, names
   the releases page, and does not stop the procedure, because the update
   has already landed by then.
7. **`CLAUDE.md`'s sentence "History goes to git, the changelog and the work
   record."** names the release notes instead.
8. **Every other reader outside the policy root** is rewritten in place:
   `CONTRIBUTING.md` *House rules* and *Cutting a release*,
   `skills/implement/SKILL.md:492`, `skills/settle/SKILL.md:11`,
   `skills/verify/orchestration.md:328`, `:349`, `:368`,
   `skills/verify/scripts/session_cost.py:2850-2866` and its pin,
   the comments in `skills/verify/scripts/unverified_check.py:98-114`,
   `:532-537`, `:579-585` and `.github/scripts/issue_claims_check.py:93`,
   the header comment of `.github/workflows/publish-release.yml:13-18`, and
   the two `seal/follow-up.md` rows that name `changelog/0.12.2.md`. Those
   two rows go. Each asked whether a correction is carried into a released
   copy of 0.12.2. The v0.12.2 GitHub Release holds neither sentence and is
   not republished (*Scope* item 5). The only copy holding them is
   `changelog/0.12.2.md` in the tree of `v0.23.1`, which no commit changes.
   The owner's answer to `frame/questions.md` Q2 is the answer to both.

Out of scope, each with why:

- **Everything #1117 builds.** The version moving at the start of a
  release, a work item's process row in its own fragment, the workflow that
  tags and publishes on the push to `main`, and the removal of
  `docs/release-checklist.md` steps 1 to 4 and of the tag push in step 6.
  This work leaves #1117 three seams. First, `publish_release_note.py` keeps
  its environment interface (`TAG`, `REPO`, `GH_TOKEN`, `DRY_RUN`,
  `GITHUB_OUTPUT`) and its `created` output, so #1117's workflow can run it
  after creating the tag in the same job; the tag only has to exist in that
  job's checkout. Second, the fragments are selected by one function and
  rendered by one function, so a heading #1117 adds to a fragment is read in
  one place. Third, no step of this work needs a preparation commit: the
  gather is gone and the note reads the history. `PREPARATION_RE`, the
  workflow's trigger, the bump in step 2 and `seal/process/` are left as
  they are, because the preparation pull request still exists until #1117.
- **The heading `2. Gather, bump` of `docs/release-checklist.md`.** The
  gather paragraphs under it go through `## Rule changes`, and the heading
  is left, because #1117 removes the step whole and both rule changes reach
  the same settle.
- **`skills/implement/orchestration.md:530` and `:578`.** Each states the
  gather ("the accumulated entries are gathered and dated", "the marker the
  changelog gather writes"), and the file belongs to #1041's work item
  (`frame/questions.md` Q4).
- **`.test_durations`.** It is the cache the test runner rewrites
  (`tests/censuses.py:1053`); the build does not edit it by hand.
- **Correcting the 0.12.2 sentences the two follow-up rows described.** No
  released copy can take the correction (*Scope* item 8), and the rows go.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the note is built from the release's fragments | Given a repository with tags `v1.2.2` and `v1.2.3`, a fragment added before `v1.2.2`, two added after it, and one of the two removed by a later commit before `v1.2.3`; when the script runs with `DRY_RUN=1` and `TAG=v1.2.3`; then the printed note holds both fragments added after `v1.2.2`, the removed one included, each under its `<!-- specs/<id> -->` line and in id order, holds nothing of the older fragment, and names no `changelog/` path | a case in `tests/github/test_publish_release_note.py` driving a real `git` repository in `tmp_path`, seen red against the script at `8a1173c8` |
| S2 the note opens with the theme | Given that repository and a milestone `release: 1.2.3` whose description is `Purpose: the notes come from the fragments. Order: ...`; when the dry run prints the note; then its first line is `The notes come from the fragments.` | a case in the same module, seen red against the script at `8a1173c8` |
| S3 the theme sentence | A description with no `Purpose:` label gives its own first sentence; one whose first line ends before any `.` gives that line; a number such as `0.18.0` inside the sentence does not end it | a case of the theme function's own, one assertion per shape |
| S4 no theme, no failure | Given the milestone list cannot be read, or no milestone has the title, or its description is empty; when the script runs; then the note has no theme line, the job log says which of the three, and the exit code is what it would have been with a theme | a case per arm in the same module |
| S5 a range that added no fragment | Given a tag whose range added no `changelog.md`; when the script runs; then it exits 1, names the two tags of the range, and creates no release | the case that pins A3 today, re-pointed from the missing file to the empty range |
| S6 the previous tag | Given tags that are not version shaped and a version tag that is not merged into the tagged commit's first parent; when the previous tag is read; then it is the highest version tag merged into the first parent, and with none the range is the whole history to the tag | a case of the function's own |
| S7 the update lands by `plugin.json` | Step 2b of `skills/update/SKILL.md` reads the installed copy's `.claude-plugin/plugin.json` `version` and compares it with the version step 2 reported, and names no `CHANGELOG.md` | `tests/behaviour/test_release_hygiene.py#test_update_reads_the_installed_copy_before_it_summarises`, re-pointed, seen red against the skill at `8a1173c8` |
| S8 the update shows the GitHub Releases | Step 3 reads the releases from `api.github.com` with no token, takes the repository from the marketplace clone's `origin`, reads every release after the old version up to the new one oldest first, says so and names the releases page when the read fails, and names no `changelog/` path | a new case beside S7's, seen red against the skill at `8a1173c8` |
| S9 the gather is gone from CI and the gate | `.github/workflows/hygiene.yml` has no step running `gather_changelog.py`, and `skills/verify/scripts/broad_gate.py`'s step partition matches the workflow's steps | `tests/behaviour/test_the_gate_names_every_step_ci_runs.py` green after the step and its row go together |
| S10 every check line still resolves | The `check:` lines in `docs/` that name the two emptied test files and the marker `second-gather-appends` resolve, because the files stay with no case and a caseless class carries the marker | `bin/seal rules --check` exits 0, and `tests/github/test_rules.py` runs green |
| S11 every released version keeps its notes | Each of the 58 versions has its text in one of two places: its GitHub Release, for the 32 *Scope* item 5 measured, or `changelog/X.Y.Z.md` at `v0.23.1`, for the other 26; `git cat-file -e v0.23.1:changelog/X.Y.Z.md` exits 0 for all 58 | `git cat-file -e` over the 58, run in phase 5 and recorded in its record |
| S12 no living text names the gathered files as where the notes are | `git grep -n -E 'changelog/\|CHANGELOG\.md'` outside `docs/`, `seal/` and the two emptied test files finds no line that sends a reader to those paths for the notes | the grep, run by the crafter at phase 4's close, its hits read by the proofer at review. No case holds it, because `docs/` names both paths until the settle |

## Data & interfaces

`.github/scripts/publish_release_note.py`, after the build:

- **The range.** The previous tag is the highest tag matching `TAG_RE`
  among `git tag --merged <tag>^ --list 'v*'`, or none. The range is
  `<previous>..<tag>`, or every commit reachable from `<tag>` where there is
  none.
- **The fragments.** One function returns `[(work item id, body)]`: every
  path `seal/threads/<id>/changelog.md` that
  `git log --no-renames --diff-filter=A --name-only --format=` over the
  range lists and the range's lower tag does not already hold, each read
  at the newest commit of
  `git log --full-history --format=%H <range> -- <path>` whose tree holds
  the path, the body stripped, an empty body skipped, sorted by id.
  `--no-renames` keeps a fragment from reading as a rename of an older one
  the settle deleted in the same range. `--full-history` walks the release
  branch behind a merge-commit tag, whose first parent never held the path.
- **The theme.** One function reads the milestones through
  `gh api --paginate repos/<REPO>/milestones?state=all` and returns the
  description of the one titled `release: <version>`, or why there is none.
  A second function, with no I/O, turns a description into the sentence
  *Scope* item 2 states. The workflow's `permissions` block is not changed:
  the job already lists the pull requests with `contents: write` alone
  (executed: the published v0.23.1 note carries its pull request summary),
  and whether the milestone read needs `issues: read` is
  `frame/questions.md` Q3.
- **The section.** One function renders the fragments as each id's marker
  line, the body, and a blank line. It is the function #1117 extends.
- **`release_body`** takes the theme and the rendered fragments where it
  takes the gathered section today, and drops the trailing link. The names
  `.github/scripts/release_seal.py` imports from this module (`glance`,
  `sealed_glance`, `GLANCE_HEADING`, `merged_pulls` and the counting
  helpers) keep their names and shapes.
- **Exit codes.** 0 published, already published, or a dry run. 1 the tag
  is not `vX.Y.Z`, or its range added no fragment the previous tag does not
  already hold.

`skills/update/SKILL.md` step 2b reads
`<installPath>/.claude-plugin/plugin.json` through `python3`'s `json`
module, as step 2b already reads `installed_plugins.json`. Step 3 reads
`https://api.github.com/repos/<owner>/<repo>/releases?per_page=100` with no
`Authorization` header and no `gh`, which needs a login.

## Rule changes

- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: fires on the `v*` tag push and publishes the release's own file,
    `changelog/X.Y.Z.md`, which the preparation commit gathered, titled from
    the tagged commit's
  to: fires on the `v*` tag push and publishes a note built from the
    release's changelog fragments, titled from the tagged commit's
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: It goes red on a tag with no release file, or one with no section
    for the tag, which is the release shipping unexplained. The note opens
    with a summary read from the pull requests merged into
    `release/vX.Y.Z`:
  to: The fragments are the ones the commits after the previous `vX.Y.Z`
    tag added and that tag does not already hold, each read at the newest
    commit of that range that holds it,
    so a work item a settle removed before the tag still has its entry. It
    goes red on a tag whose range added no fragment the previous tag does
    not already hold, which is the release shipping unexplained. The note
    opens with the release's theme, the
    first sentence of its milestone's description with a leading
    `Purpose:` left out; a milestone that cannot be read leaves the note
    without one and never fails the job. A summary read from the pull
    requests merged into `release/vX.Y.Z` follows:
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: The gathered section follows, folded.
  to: The fragments follow, folded, each under an HTML comment naming its
    work item.
- change
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: carrying one commit of its own: the one that gathers the changelog
    fragments into `changelog/X.Y.Z.md` under `## X.Y.Z — <date>`, heads
    the index `CHANGELOG.md` with that line, and moves `plugin.json`.
  to: carrying one commit of its own: the one that moves `plugin.json`.
- change
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: and leave `CHANGELOG.md`, `changelog/` and `plugin.json` alone.
  to: and leave `plugin.json` alone.
- change
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: **The changelog entries arrive as fragments, and the release
    gathers them.** Which file a change writes, and why, is
    `docs/the-record-layout.md` *A change writes fragments, never a shared
    file*. Release preparation runs:
  to: **The changelog entries arrive as fragments, and the release note is
    built from them at the tag.** Which file a change writes, and why, is
    `docs/the-record-layout.md` *A change writes fragments, never a shared
    file*. No branch gathers them. `.github/scripts/publish_release_note.py`
    reads, from the history at the tag, the fragments the release's commits
    added and the previous version tag does not already hold, and writes
    each under an HTML comment naming its work item,
    invisible to a reader and the only link from a released entry back to
    the work that produced it. `DRY_RUN=1` prints the note and writes
    nothing.
    check: tests/github/test_publish_release_note.py
- remove
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: python3 .github/scripts/gather_changelog.py --version X.Y.Z
- remove
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: It concatenates every fragment that no release file carries yet
    into `changelog/X.Y.Z.md`, a file of the release's own that opens with
    its dated `## X.Y.Z — <date>` line, and heads the index `CHANGELOG.md`
    with that same line and a link to the file. A second gather for the
    same version appends into the file and keeps its date. Each entry is
    written under an HTML comment naming its work item, invisible to a
    reader and the only link from a released entry back to the work that
    produced it. `--check` reports fragments that never arrived, and the
    hygiene workflow runs it on every pull request into `main`, so a
    release cannot go out with a change that ships unexplained.
    `--dry-run` prints the section and writes nothing, in either file.
- remove
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: A fragment carries no line starting `## `, and it closes every
    fenced block and HTML comment it opens. The released section ends at
    the next `## ` line, for the gather and for the release note alike, so
    every entry after it would ship under no version; and a block left open
    would hide the next work item's marker, so `--check` would call a
    gathered entry missing. The gather refuses either fragment, with or
    without `--dry-run`, before it writes or prints a section, and names
    the fragment, the line number and the line. Demote the line to `###`
    or lower, or close the block, in a pull request into the release
    branch, then gather again. A fragment already in a release file is not
    read again. `CHANGELOG.md` holds no section that entries accumulate
    under, such as `## Unreleased`; the fragments are that region.
- change
  file: docs/the-record-layout.md
  section: Every kind of record, at a glance
  from: `changelog/<X.Y.Z>.md`, the release's own file, once its release
    gathers it | each release file is under target, and is the unit | the
    file name, by version, and `CHANGELOG.md`, which heads each release
    newest first with a link to its file
  to: the GitHub Release at the `vX.Y.Z` tag once its release is published
    | each fragment is under target | the repository's releases on GitHub,
    by tag
- remove
  file: docs/the-record-layout.md
  section: A change writes fragments, never a shared file
  from: A changelog fragment has no line starting `## `, because that line
    ends the released section, and the gather refuses a fragment that has
    one.
- change
  file: docs/the-record-layout.md
  section: A change writes fragments, never a shared file
  from: **The fragments are gathered at the release, by one command in one
    commit**, and `docs/release-checklist.md` *2. Gather, bump* holds it.
    The fragments are concatenated into the release's own file,
    `changelog/X.Y.Z.md`, and the release's heading goes into the index,
    `CHANGELOG.md`. A fragment lives from the work item's first entry to
    the release that ships it.
    check: tests/text/test_the_changelog_is_gathered_at_release.py tests/github/test_gather_changelog.py
  to: **The release note is built from the fragments at the tag, and no
    copy of the notes is kept in the tree.** On the `vX.Y.Z` tag push,
    `.github/scripts/publish_release_note.py` reads every fragment the
    commits after the previous `vX.Y.Z` tag added and that tag does not
    already hold, from the history, so a
    fragment a settle removed before the tag is still read. The GitHub
    Release at the tag is the release's notes. A copy in the tree is the
    one nobody works from, and so the one that drifts from its fragment. A
    fragment lives from the work item's first entry to the settle after the
    release that ships it, and the history keeps it after that.
    check: tests/github/test_publish_release_note.py
- change
  file: docs/the-record-layout.md
  section: A commit after the build brings its changelog fragment along
  from: the fragment and the release gathers it verbatim, so a later commit
  to: the fragment and the release note is built from it as it stands at
    the tag, so a later commit
- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: **A line that EXCUSES or DECLARES something — a changelog marker, a
    `seal/config.md` row, a `routing.md` row — is not taken on doubt,
  to: **A line that EXCUSES or DECLARES something — a `seal/config.md`
    row, a `routing.md` row — is not taken on doubt,
- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: The holding bias would let a changelog marker quoted in an example
    stand for an entry nobody gathered, and the excusing bias
  to: The holding bias would let a `seal/config.md` row quoted in an
    example declare a value nobody set, and the excusing bias
- remove
  file: docs/the-record-layout.md
  section: The root records
  from: | `CHANGELOG.md` | which releases there are: the index, one
    `## X.Y.Z — <date>` heading each, newest first, with a link to the
    release's file |
- remove
  file: docs/the-record-layout.md
  section: The root records
  from: | `changelog/<X.Y.Z>.md` | what one release changed, that
    release's section alone |
- remove
  file: docs/the-record-layout.md
  section: The root records
  from: **`CHANGELOG.md` and each release's own file carry that release's
    one `## X.Y.Z — <date>` line.** `changelog/<X.Y.Z>.md` opens with it,
    and the index keeps the same line above the link to the file, because
    the update skill an installed copy already carries checks that an
    update landed by the first `## ` line of `CHANGELOG.md`. The GitHub
    Release reads the release's own file.
    check: tests/text/test_the_changelog_is_gathered_at_release.py tests/github/test_gather_changelog.py
- remove
  file: docs/release-checklist.md
  section: 2. Gather, bump
  from: **The preparation commit gathers the changelog fragments.**
- remove
  file: docs/release-checklist.md
  section: 2. Gather, bump
  from: python3 .github/scripts/gather_changelog.py --dry-run --version X.Y.Z
- remove
  file: docs/release-checklist.md
  section: 2. Gather, bump
  from: Read it. Then:
- remove
  file: docs/release-checklist.md
  section: 2. Gather, bump
  from: python3 .github/scripts/gather_changelog.py --version X.Y.Z
- change
  file: docs/release-checklist.md
  section: 2. Gather, bump
  from: git add -A changelog/ CHANGELOG.md seal/ .claude-plugin/plugin.json
  to: git add -A seal/ .claude-plugin/plugin.json
- remove
  file: docs/release-checklist.md
  section: 2. Gather, bump
  from: The gather writes a new file, the release's own
    `changelog/X.Y.Z.md`, and heads the index `CHANGELOG.md` with its line.
    It is staged before step 3 runs anything, because the suite lists
    files with `git ls-files`, which reads the index: an untracked release
    file is a tree the listing does not describe.
    check: tests/text/test_the_changelog_is_gathered_at_release.py tests/github/test_gather_changelog.py
- remove
  file: docs/release-checklist.md
  section: 2. Gather, bump
  from: **A second gather for the same version appends into its section.**
    A fragment landing after this step, while the release pull request is
    red, is the ordinary shape. Run the same command again: the new entries
    join the existing section, the section keeps the first gather's date,
    and `tests/behaviour/test_release_hygiene.py` refuses a file that heads
    a version twice.
    check: second-gather-appends tests/behaviour/test_release_hygiene.py
- change
  file: docs/release-checklist.md
  section: 3. Verify before committing
  from: The preparation commit is the first time a fragment's prose is read
    by the tests that scan the release files under `changelog/`. So the
    whole gate runs on this tree, and every exit code
  to: The whole gate runs on this tree, and every exit code
- remove
  file: docs/release-checklist.md
  section: 3. Verify before committing
  from: python3 .github/scripts/gather_changelog.py --check
- remove
  file: docs/release-checklist.md
  section: 4. Commit, push, open the first pull request
  from: The title's count of fragments is the count `--version` gathered,
    not the count `--check` reports: the latter includes every fragment of
    every earlier release.
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: which publishes it from the release's file step 2 already gathered,
    with the title
  to: which builds it from the changelog fragments the release's commits
    added and the previous version tag does not already hold, with the title
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: The job fails for a tag whose release file, `changelog/X.Y.Z.md`,
    is not there or carries no section for it, which is step 2 not having
    happened; for
  to: The job fails for a tag whose range added no changelog fragment the
    previous version tag does not already hold; for
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: The note opens with a summary of the release's pull requests
  to: The note opens with the release's theme line, then a summary of the
    release's pull requests
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: over the section folded; where the job log says the pull requests
    could not be listed, the note went out as the section alone,
  to: over the fragments folded; where the job log says the pull requests
    could not be listed, the note went out as the theme line and the
    fragments alone,
- change
  file: docs/one-root-by-lifetime.md
  section: The root and its lifetimes
  from: everything else under `seal/`, with `docs/` and `CHANGELOG.md`, is
    permanent.
  to: everything else under `seal/`, with `docs/`, is permanent.
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 루트와 그 안의 수명
  from: 그 밖의 `seal/` 아래 파일은 `docs/`, `CHANGELOG.md` 와 함께
    영구적입니다.
  to: 그 밖의 `seal/` 아래 파일은 `docs/` 와 함께 영구적입니다.
- change
  file: docs/issues-and-milestones.md
  section: Reconstructing a missing milestone
  from: the close date against `CHANGELOG.md`'s release dates is what is
    left
  to: the close date against the publication dates of the GitHub Releases
    is what is left
- change
  file: docs/the-record-layout.md
  section: A change writes fragments, never a shared file
  from: never under a heading of `CHANGELOG.md`.
  to: never under a heading of a file every branch shares.
- change
  file: docs/release-checklist.md
  section: 3. Verify before committing
  from: never from this file, because this commit writes the heading and
    the bump together
  to: never from a file this commit writes

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The gather script, whole | `.github/scripts/gather_changelog.py` | Nothing writes a release file. The note is built at the tag by `publish_release_note.py`'s fragment reader, and the marker it wrote moves into the note |
| The hygiene step "every changelog fragment reached the released file" and its comment | `.github/workflows/hygiene.yml:110-130` | No gathered file exists for a fragment to reach. Every fragment the release's commits added and the previous tag does not already hold is in the note by construction. The Alternatives table weighs a replacement step |
| The step's row in the gate's partition, and the step's name among the steps that run only on a pull request into `main` | `skills/verify/scripts/broad_gate.py:2219-2224`, `:2254-2262` | The step is gone, and the comment's count of such steps drops with it |
| The release-file reader: `RELEASES`, `release_file`, `section_heading_re`, `section_body`, the gather advice in `main`, the link line in `release_body`, and the docstring's account of the gathered file | `.github/scripts/publish_release_note.py:16-26`, `:46-55`, `:84-86`, `:103-104`, `:134-142`, `:158-176`, `:505`, `:541-556` | The range, fragment, theme and section functions of *Data & interfaces* |
| The header comment's sentence naming `changelog/X.Y.Z.md` | `.github/workflows/publish-release.yml:15-18` | The note is built from the fragments, as the script's docstring says |
| `changelog/`, 58 files, and `CHANGELOG.md` | the repository root | The GitHub Release at each tag for the 32 that hold their file's text, and `changelog/X.Y.Z.md` at `v0.23.1` for all 58 |
| `gathered_entry` | `tests/conftest.py:311-345` | Its only callers are in `tests/text/test_the_changelog_is_gathered_at_release.py`, whose cases go |
| Every case and helper of `tests/github/test_gather_changelog.py`, the `second-gather-appends` case included | the whole module | The script is gone. The module keeps a docstring saying it holds no case until the settle applies this work item's rule changes, and one caseless class carrying `@pytest.mark.rule("second-gather-appends")`, so the `check:` lines in `docs/` resolve until then. The settle's pull request deletes the module |
| Every case of `tests/text/test_the_changelog_is_gathered_at_release.py` | the whole module | The same: a docstring and no case until the settle, which deletes it |
| `GATHERER`, the gatherer loader, the release-file fixture and `Test_module::test_the_reader_reads_what_the_gatherer_writes`, and the docstring's account of both | `tests/github/test_publish_release_note.py:6-29`, `:49`, `:83`, `:575-602` | No gatherer and no section reader remain to hold against each other. S1 to S6 replace the A1 and A3 cases in place |
| `shipped_versions` | `tests/behaviour/test_release_hygiene.py:218-226` | `shipped_tags` in the same module, which reads the `v*` tags, the truthful source the docstring of `shipped_tags` already names |
| `test_no_section_accumulates_entries_in_the_shared_file`, `duplicated_version_headings`, `test_a_version_heading_appears_once_in_a_changelog`, `test_no_version_heads_two_sections_of_this_changelog`, `test_the_newest_changelog_entry_is_the_version_being_shipped` | `tests/behaviour/test_release_hygiene.py:1081-1170` | No shared file exists for entries to accumulate in or for a version to head twice. An entry with no bump is held by the hygiene step "a change to what ships must move the version", and a bump with no entry by S5 at the tag |
| The words "`CHANGELOG.md` and `changelog/`" in the timer case's docstring | `tests/behaviour/test_release_hygiene.py:586` | The two paths no longer exist to be outside the scanned set |
| `test_plugin_version_is_in_changelog` | `tests/behaviour/test_chain_hooks_hardening.py:107-118` | `.claude-plugin/plugin.json` is the version's one source. The case would skip forever once the file is gone |
| The `changelog` span read from `changelog/0.20.0.md`, and every assertion that reads it, present and gone | `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py#test_what_a_line_names_a_file_by_is_told_where_each_reader_meets_it`, `:719-760` | The released fragment is in the v0.20.0 note and at the tag. The case's assertions about the recorder and its docstring stay |
| `"changelog/"` and `"CHANGELOG.md"` in `RECORDS` and `OLD_NAME_RECORDS`, and the comment words naming them | `tests/censuses.py:846-850`, `:1045-1056` | No such paths remain to exempt |
| The planted `changelog/0.1.0.md` and `CHANGELOG.md` fixture paths | `tests/test_censuses.py:788-789`, `:808-809`, `:930-931` | They pinned the two exemptions above |
| `"changelog/"` in `RENAMED_RECORDS` | `tests/behaviour/test_one_word_one_meaning.py:944-947` | The case asserts each prefix there holds a tracked file, and this one will hold none |
| `"CHANGELOG.md"` and `"changelog"` in `STAYS_HOME` | `tests/behaviour/test_the_release_check_watches_what_ships.py:59-60` | Neither is a top-level entry any more |
| `"gather_changelog"` in the `stays_home` parameters | `tests/behaviour/test_first_setup_asks_once.py:454` | Its absence from the template is true of a script that no longer exists, so the parameter reads nothing |
| The mentions of `tests/github/test_gather_changelog.py`, `gather_changelog` and `CHANGELOG.md` in module docstrings | `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py:27`, `tests/behaviour/test_a_body_naming_two_issues_claims_one.py:63`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py:15` | Each is rewritten to name what remains |
| The consumers named for the gather in comments | `skills/verify/scripts/unverified_check.py:101`, `:111-113`, `:532-537`, `:579-585`; `.github/scripts/issue_claims_check.py:93` | Each comment names the readers that remain. The loading pattern `issue_claims_check.py` cites is its own |
| "the changelog gather writes one" in the docstring of the marker-shaped `live_lines` cases | `tests/skills/test_unverified_check.py:662-667` | The cases stay: they pin `live_lines` on a declaring line, and the marker is still a line of that shape. The docstring stops naming a gather |
| "which its file under `changelog/` names" in the printed message and its comment | `skills/verify/scripts/session_cost.py:2850-2866`, pinned by `tests/skills/test_session_cost.py:3761` | The message names the release note. The pin moves with it in the same commit |
| "the release whose file under `changelog/` lists" three times | `skills/verify/orchestration.md:328`, `:349`, `:368` | The release note lists the issue |
| Step 2b's read of `CHANGELOG.md`, and step 3's reading of `changelog/<X.Y.Z>.md` with the index sentence | `skills/update/SKILL.md:44-53`, `:71-76` | `.claude-plugin/plugin.json`'s `version`, and the GitHub Releases read from the public API |
| "the changelog" in "History goes to git, the changelog and the work record." | `CLAUDE.md:33` | "the release notes", as the issue words it |
| The paragraph "One branch does write the changelog, and it is the one based on `main`." through "expecting to." | `CONTRIBUTING.md` *House rules*, `:397-407` | `docs/branch-and-release.md` *Work accumulates on a release branch*, as `## Rule changes` rewrites it: no branch writes the notes |
| "how the changelog fragments are gathered" | `CONTRIBUTING.md` *Cutting a release*, `:462` | "how the release note is built from the changelog fragments" |
| "because the release gathers that fragment as it stands" | `skills/implement/SKILL.md:492` | "because the release note is built from that fragment as it stands at the tag" |
| "NOT for: gathering changelog fragments, which release preparation already does" | `skills/settle/SKILL.md:11` | "NOT for: the release notes, which the tag's workflow builds from the fragments" |
| The coordinate `changelog/0.12.2.md` and the sentence on how `gather_changelog.py#ungathered` decides | `seal/follow-up.md:47`, `:49` | Nothing: both rows go, since no released copy of 0.12.2 can take the correction (*Scope* item 8) |
| The policy root's sentences on the gather and the gathered files | `docs/` | `## Rule changes` above, written at the settle, never by this pull request |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-28 by framer, before the build.

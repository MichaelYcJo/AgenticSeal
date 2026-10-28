# Review round 8: 1793188384-the-release-notes-are-kept-twice

target: 7ed78978 against 8df3b7ff

This round reviews what landed after round 7, the range `8df3b7ff..7ed78978`.
It holds four commits. `9477538d` merges `origin/release/v0.24.0` at
`faf093f1`, which carries #1137 (#1041's work item) and #1138. `9f2f34ee`
adds phase 6 to `frame/plan.md` and rewrites Q4's Status in
`frame/questions.md`. `0ae4229a` is the phase 6 build in
`skills/implement/orchestration.md`, and `7ed78978` writes the phase record
and the plan row's Status. The round ran in the branch worktree the spawn
prompt names, read only, at `7ed78978`. The repository declares no
`seal/parity.md`, so this round writes no `original:` line.

The merge's own changes were reviewed on #1137 and #1138, as the spawn
prompt says. This round judged only that the merge is clean and that
nothing this branch removed came back through it. Carried from round 7 and
not established again: the 58 version tags and `v0.23.1` holding all 58
files (no commit in the range touches a tag or `changelog/`), and the
published release listing. Re-established this round: the merge's
cleanliness, the readers of the removed files, each of the four sentences
of `skills/implement/orchestration.md` the phase judged, the phase record's
grep table, and a sweep of `skills/`, `agents/`, `templates/` and `hooks/`
for anything else that names this plugin's gather or what it wrote.

The account checked. The phase record (`trail/phases/phase-6.md`) claims
four things. First, it claims the two rewrites change only the words
quoted and the rewrap changes no word. `git diff -w --word-diff 9477538d
0ae4229a` shows exactly "are gathered and dated," replaced by "go out
under it," and "changelog gather writes." replaced by "release note
carries above that fragment.", with no other word changed (executed).
Second, it claims its grep table lists every hit. Its regex over
`skills/` and `agents/` at `7ed78978` gives the same 14 hits the table
judges (executed). Third, it claims the 35 modules naming
`orchestration.md` pass. This round ran them, see the last confirmation.
Fourth, it claims no sentence under `skills/` or `agents/` names this
plugin's gather any longer. That holds for its regex. The plan row's
grep is scoped to `skills/` and `agents/`, and it matches the words
"gather" and "changelog". So it could not see `templates/setup/config.md`,
which names the gather's own output heading without either word. That is
finding 1.

## Findings

### 1. The template's list of literals a checker reads still names the gathered file's release heading, which no checker reads any more

severity: should
location: `templates/setup/config.md:143-144`
evidence: executed `git grep -n -E "release section|X\.Y\.Z — <date>" -- tests/ skills/ hooks/ .github/ agents/ templates/`, `git show 8a1173c8:.github/scripts/gather_changelog.py`, `git show 8a1173c8:.github/scripts/publish_release_note.py`

`templates/setup/config.md` *What no row governs* tells a repository which
strings stay English whatever `Record language` says. Its grounds, at
`:127-128`, are "The field names, section headings and vocabulary a
checker or a pinned case reads literally". The bullet at `:143-144` lists
"a release section's `## X.Y.Z — <date>`" among the markers and anchors.
That heading was the gathered file's section line. Two readers matched it
at `8a1173c8`: `gather_changelog.py#heading_re` (its docstring reads "The
`## X.Y.Z — <date>` line for one version") and
`publish_release_note.py#section_body`, through the pattern at `:142`.
Phase 3 removed the first and phase 1 removed the second. At `7ed78978`,
`git grep` over `tests/`, `skills/`, `hooks/`, `.github/`, `agents/` and
`templates/` finds the heading only in this template line. No checker and
no pinned case reads it.

The template ships to every repository that sets up the plugin, and an
agent setting `Record language` reads this list to decide what not to
translate. The bullet now gives it a reason that is false. It also keeps
the gathered file's shape alive in a shipped file, which `frame/design.md:15`
says this work removes: "Every case, comment, census entry and sentence
outside the policy root that names `changelog/`, `CHANGELOG.md` or the
gather is removed or re-pointed". The sentence names the gather's output,
not the gather by name, which is why the plan row's grep missed it.

The suite did not catch it either.
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#test_the_exclusion_list_holds_every_string_a_checker_matches`
checks one direction only: every literal its five checkers hold is in the
list. It does not check that every entry in the list is still read. So a
removed reader leaves its entry behind with every case green.
`skills/implement/SKILL.md:60-61` says the list "is derived from the
checkers' own constants, so it cannot drift from them", which is true of
that direction only.

The same heading stands in `docs/the-record-layout.md:326` and `:331` and
`docs/branch-and-release.md:211` and `:231`. Those are the policy root's,
and this work item's `## Rule changes` hands them to the settle. They are
not part of this finding.

Delete the clause from the bullet. Line 143 to 147 then read:

```markdown
- **The markers and anchors.** `<!-- specs/<work-item-id> -->`, the word
  `closed` that opens a closed `## Not verified` row, the line
  `## Not from the records` that ends the part of a pull request body
  `seal pr-body` copies from the records, and the anchor table's header
  cells `Pact`, `Clause` and `Hash`.
```

The marker `<!-- specs/<work-item-id> -->` stays: `publish_release_note.py:242`
still writes it into the note above each fragment. Removing the clause
breaks no case: `_literal_strings` does not hold the heading, so
`test_the_exclusion_list_holds_every_string_a_checker_matches` has no
parameter for it.

verdict: open
answer:

## Confirmations

confirms: none
The merge is clean, and nothing this branch removed came back through it.
`9477538d`'s parents are `8df3b7ff` and `faf093f1`, and `faf093f1` is
`origin/release/v0.24.0` (executed: `git rev-parse`). The merge base is
`8a1173c8`. The branch's own change, `git diff 8a1173c8 8df3b7ff`, equals
the merge's change against the release side, `git diff faf093f1 9477538d`,
line for line once `index` lines are dropped: 111 files, 3671 insertions
and 14720 deletions each (executed, `diff` exit 0). So the merge took every
change of this branch as it was, and took nothing of the release side's
beyond the release side itself. `git cat-file -e 7ed78978:<path>` exits 128
for `changelog`, `CHANGELOG.md` and `.github/scripts/gather_changelog.py`
(executed). `git grep -n -E 'gather_changelog|CHANGELOG\.md|changelog/'`
over the tree outside this work item finds 159 lines at `8df3b7ff` and 165
at `7ed78978` (executed). The six new lines all stand in records of the two
merged work items: `1793174169-a-round-with-fixes-costs-three-record-commits/trail/rounds/round-7.md`
(two lines) and `1793188383-rule-5-judges-tokens-per-tool-call`'s
`frame/plan.md`, `guarantee.md`, `trail/phases/phase-1.md` and
`trail/rounds/round-1.md` (one line each). Each states where a removal
search looked or what a released file held. None reads a removed file
(read). So no reader came back.

confirms: none
The rewrite at `skills/implement/orchestration.md:529-530` holds for this
plugin and for a host repository. It now reads "A pull request into `main`
is a release: the version moves, the accumulated entries go out under it,
and the tag follows the merge". The paragraph states what any release
does, unconditionally, and the old words "gathered and dated" described
this plugin's gather. The new words name no mechanism. For this plugin,
the tag's workflow publishes the fragments under the version's tag
(`CONTRIBUTING.md:396-397`). For a host repository that still gathers, the
entries also go out under the version. So both readings are true (read).

confirms: none
The rewrite at `skills/implement/orchestration.md:577-578` holds for this
plugin. It now says the id keys "its changelog fragment and the
`<!-- specs/<work-item-id> -->` marker the release note carries above that
fragment". `publish_release_note.py#section`, at `:239-242`, writes
`<!-- specs/{item} -->` on the line above each fragment's body (read). For
a host repository the sentence is true where the host builds its note the
plugin's way. That is the same scope the old wording had, since "the
changelog gather" was this plugin's script too. So the rewrite narrows
nothing and widens nothing (read).

confirms: none
The two kept sentences describe a host repository's own convention.
`:535-538` is the paragraph "Where an entry accumulates is the
repository's convention, so the orchestrator reads it before writing one".
It names two common shapes a repository may use, and "one fragment per
work item that a release gathers" is one of them. `:540-542` is
conditioned: "Where the repository gathers fragments, basing on `main`
means running the gather", and it sends the reader to "the contribution
guide" for the command. In this repository the guide says no branch
writes the notes and the tag's workflow builds them (`CONTRIBUTING.md:394-397`),
so the condition is false here and the sentence asks for nothing (read).
The policy root still describes a gather (`docs/branch-and-release.md:221`
and `docs/release-checklist.md:47-67`). The design hands those to the
settle through `## Rule changes`, and phase 6 does not touch them.

confirms: none
Q4's new Status in `frame/questions.md` holds. `fdfb20d5` on the release
side is titled "(#1137)", and its work item's `frame/design.md:3` reads
"Issue #1041 is the spec" (executed: `git log 8a1173c8..faf093f1`; read).
That work item changed `skills/implement/orchestration.md:666`, and the
merge kept that change, by the first confirmation. No other directory under
`seal/threads/` has a plan row that edits `skills/implement/orchestration.md`
and has not merged (executed: `git grep -l "implement/orchestration.md"` over
`seal/threads/`, each hit a record of a merged work item). Phase 6's row
matches the four coordinates at `9477538d`: `:530`, `:538`, `:541` and
`:578` hold the four phrases (executed: `git grep -n` at `9477538d`).

confirms: none
Apart from finding 1, nothing in `skills/`, `agents/`, `templates/` or
`hooks/` names this plugin's gather or what it wrote. Three greps ran at
`7ed78978` (executed). The first matched `gather`, `changelog marker`,
`CHANGELOG\.md`, `changelog/`, `dated` and `unreleased`, case-insensitive.
Its hits outside the phase table are the following. `hooks/lib/optin.py:60`
and `hooks/root-migrate.py:92` name the fragment file `changelog.md`.
`templates/setup/config.md:95` and `templates/setup/seal-README.md:98` name
the fragment too. `hooks/lib/cmdline_base.py:1117` says "updated".
`skills/settle/` and `skills/update/SKILL.md` say "unreleased" or
"Updated" of a work item or a version. The second grep matched the marker
`<!-- specs/` and `specs/<`. Its hits name the marker as a literal
(`skills/implement/SKILL.md:62`, `templates/setup/config.md:143`), its
writer (`publish_release_note.py:242`), or the retired `seal/specs/`
directory. The third matched "changelog", "release file", "release's file"
and "release note". Its hits name the fragment, the note built at the tag,
or a release note by issue number (read). The class was enumerated as
these three greps and the release-heading grep under finding 1. Finding 1
is its one instance.

confirms: none
The narrow verification for this round passed. `git grep -l -E
"orchestration\.md" -- tests/` finds 35 files, all modules, and
`tests/behaviour/test_docs_line_wrap.py` is among them. With
`tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` and
`tests/test_censuses.py` added, `bin/test -q` over the 37 modules gave 1242
passed, exit 0 (executed). No line of `skills/implement/orchestration.md`
from 526 to 585 is longer than 88 columns (executed: `awk`). `bin/seal
layout --check` exited 0 (160 files read, 0 refused). `bin/seal rules
--check` exited 0 (all 266 check lines in 55 rule files hold). This is not
the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck: unverified | the branch at `7ed78978` | the orchestrator, at `seal gate`, before the sealer is spawned |
| The changes #1137 and #1138 brought in through the merge, beyond the merge's cleanliness and the removed files' readers | `9477538d` | their own pull requests' review rounds, as the spawn prompt says |
| Whether the tag's job can list the milestones under `contents: write` alone (Q3, default (a)) | `.github/workflows/publish-release.yml` | the orchestrator, reading the log of the tag run of the release carrying this work |
| Step 3 of the update skill, run by a session updating across a real release | `skills/update/SKILL.md` | the first person to update to the release carrying this work |

## Probes

| Command | Result |
|---|---|
| `git rev-parse 9477538d^1 9477538d^2 origin/release/v0.24.0`, `git merge-base` of the two parents | parents `8df3b7ff` and `faf093f1`, the release branch's tip; merge base `8a1173c8` |
| `diff` of `git diff 8a1173c8 8df3b7ff` and `git diff faf093f1 9477538d`, `index` lines dropped | exit 0; 111 files, 3671 insertions, 14720 deletions on each side |
| `git cat-file -e 7ed78978:<path>` for `changelog`, `CHANGELOG.md`, `.github/scripts/gather_changelog.py` | exit 128 for each |
| `git grep -n -E 'gather_changelog\|CHANGELOG\.md\|changelog/'` at `8df3b7ff` and at `7ed78978`, outside this work item | 159 and 165 lines; the 6 new lines stand in the two merged work items' records |
| `git diff -w --word-diff 9477538d 0ae4229a -- skills/implement/orchestration.md` | two phrases replaced, no other word changed |
| `git grep -n -i -E "gather\|changelog marker\|CHANGELOG\.md\|changelog/"` over `skills/` and `agents/` | the 14 hits the phase record's table lists |
| the three sweep greps over `skills/`, `agents/`, `templates/` and `hooks/` the sixth confirmation names | the hits that confirmation lists |
| `git grep -n -E "release section\|X\.Y\.Z — <date>"` over `tests/`, `skills/`, `hooks/`, `.github/`, `agents/` and `templates/` | `templates/setup/config.md:144`, and one unrelated message in `tests/behaviour/test_release_hygiene.py:1316` |
| `git show 8a1173c8:` of `gather_changelog.py` and `publish_release_note.py` | `heading_re` and `section_body` read the `## X.Y.Z` heading at that commit |
| `bin/test -q` over the 37 modules the last confirmation names | 1242 passed, exit 0 |
| `bin/seal layout --check`, `bin/seal rules --check` | exit 0, exit 0 |

No probe file was written. The diffs, the module list and the command
outputs this round saved sat in the session's scratch directory and are
removed before hand-back.

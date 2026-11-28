# Design: 1795841828-settle-only-release-note

## Grounding

The tree as read at `3729b409`, the routing commit on the release branch's tip `991a51c7`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/core/SKILL.md` *The rule a mechanism is kept against* | A script holds a gate only on a fact it reads exactly, and carries no list of the spellings a label is written in. So the script tells a settle by a git fact, and not by a title prefix, a branch name or a trailer's wording. |
| G2. `docs/checks/the-fold.md` *The fold, and what tells it from a deletion* | **A work item directory a pull request removes whole is a settle, where the directory stood at the merge base**, and `chain_check.py#settled` is the one predicate that reads it. The paragraph accepts that a pull request outside a settle which removes a whole directory reads as a settle too. This work asks that predicate and adds no second reading of what a settle is. |
| G3. `skills/settle/SKILL.md` *A settle is not a work item* | A settle opens no directory under `agentory/threads/`, so it writes no changelog fragment. That is why a release of settles alone reaches `publish_release_note.py` with no fragment. |
| G4. `skills/implement/routing-question.md` row 4, **direct** (read) | A change routed `direct` also writes `IADD-Routing: no work item` on every commit. The trailer therefore does not tell a settle from a direct change, and the issue's second *Done when* line keeps a direct change's range failing. |
| G5. Issue #1655 *Done when* (read with `gh issue view 1655 --json body,comments`; no comments, executed on 2026-11-28) | The owner decided on 2026-11-28 that a settle-only release is a shape this repository releases and that its note is built from the release pull request's body. Every other range that added no fragment still fails. A settle that writes a fragment of its own was declined. This frame does not reopen that decision. |
| G6. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | This work item's subject is the code, `.github/scripts/publish_release_note.py`. So the rules it changes in `docs/` are stated in `## Rule changes` below for the settle, and are not edited in this pull request. `skills/settle/SKILL.md` is not under the policy root, `docs/`, so the build edits it directly. |
| G7. `docs/releasing/branch-and-release.md` *Cutting a release*, the paragraph on `dist` (read) | A cited section of a file marked `export-ignore` fails the census of cited sections. `.github/` is marked so. A sentence that `skills/settle/SKILL.md` adds names `.github/scripts/publish_release_note.py` by path alone, as that skill's *What `--apply` does* already does, and cites no section of it. |
| G8. Probe, executed: `DRY_RUN=1 TAG=v0.40.1 REPO=MichaelYcJo/AgenticSeal python3 .github/scripts/publish_release_note.py` in a `git clone --no-local` at `991a51c7`, under the framer's scratch directory | Exit 1, and the line `v0.40.1 was pushed and no commit after v0.40.0 up to v0.40.1 added a changelog fragment that v0.40.0 does not already hold, agentory/threads/<work-item-id>/changelog.md, so this release would be published with no notes at all.` This is the failure the issue reports, reproduced at the current code. The cause is shown by the code read: `publish_release_note.py#main` returns 1 at lines 867 to 875 wherever `fragments` returns no entry. |
| G9. Probe, executed: a script `test_tmp_settle_only.py` in the same clone loaded `chain_check.py` through `lib/sibling.py#load`, took each commit of `git rev-list --no-merges <range>`, listed the directories under `agentory/threads/` that `git diff-tree -r -z --no-renames --diff-filter=D --name-only <c>^ <c>` deletes a path of and `git ls-tree <c>` holds nothing of, and asked `settled(root, "<c>^", gone)` | `v0.40.0..v0.40.1`: one commit, `31a5dfac`, a settle removing 2 directories whole. `v0.39.4..v0.40.0`: 2 commits, no settle. `v0.39.2..v0.39.3`: 3 commits, no settle. `v0.39.3..v0.39.4`: one commit, `235d41ff`, read as no settle, because that settle removed `seal/threads/`, the root's name before #1660, and `lib/optin.py#HOME` now reads `agentory`. That release's note is already published by hand, and the script never republishes. |
| G10. Probe, executed: `git log -1 --format='%(trailers:key=IADD-Routing,valueonly)' 31a5dfac` printed nothing, and `git log -1 --format=%B 31a5dfac` shows `IADD-Routing: no work item` inside the squash body's middle paragraphs | GitHub's squash commit keeps each commit's trailer as body text, above its own `Co-authored-by` paragraph, so git's trailer parser does not read it on `main`'s history. The trailer is readable only from the pull request's own commits, through `gh`. `235d41ff` holds `Seal-Routing: no work item` instead, read with `git log -1 --format=%B 235d41ff`. |
| G11. Probe, executed: `gh pr view 1663` and `gh pr view 1652` | The two settle pull requests carry no label, and their head branches are `chore/settle-0.40.0` and `settle/v0.39.3`. No label and no branch-name form marks a settle. |
| G12. Probe, executed: `gh pr list --repo MichaelYcJo/AgenticSeal --base main --head release/v0.40.1 --state merged --json number,mergeCommit` printed `1664 991a51c7e0114e2f8d67ed989da5a19d2b3a276d`, and `git rev-parse 'v0.40.1^{commit}'` printed the same commit. The same pair for `release/v0.39.4` printed `1653` and `35bef264...`, equal to `v0.39.4^{commit}` | The release pull request is found exactly as the merged pull request from `release/v<version>` into `main` whose merge commit is the tagged commit. The head branch's form is the one `publish_release_note.py#merged_pulls` already reads as a base, `release/v<version>`. |
| G13. `.github/scripts/release_mark.py#mark_release` lines 530 to 563 (read) | The mark lists the pull requests with `publish_release_note.py#merged_pulls`, computes `header(work, closed, people)`, and edits nothing unless the note holds that header exactly once. The `mark` job runs where `publish` wrote `created=true` (`.github/workflows/publish-release.yml` line 107). So the mark runs on a settle-only note with no change to the mark or to the workflow's jobs, where the note opens with `release_body`'s header and the run writes `created=true`. |
| G14. The release pull request bodies, executed: `gh pr view 1664 --json body` and `gh pr view 1653 --json body`, set beside the notes published by hand, `gh release view v0.40.1` and `gh release view v0.39.4` | #1664's body states what the release changed, its operational impact, and a `## Not verified` row saying the note is written by hand once the release merges. The note published by hand restates the same facts. Once this work ships, the body is published as written, so a sentence in it about a note still to be written would reach the note. Rule change 3 below says so for the release pull request. |

## Scope

1. **`publish_release_note.py` tells a range of settles alone.** Where `fragments` returns no entry for the range, the script lists the range's commits other than merges. For each commit it takes the work item directories, the directories directly under the path that `lib/optin.py#HOME` and `lib/optin.py#WORK_ITEMS` name, from which the commit deletes a path and in which the commit's tree holds no path, and asks `chain_check.py#settled` of them at the commit's parent. A commit is a settle where that answer holds at least one directory. The range carries settles alone where it holds at least one commit and every commit is a settle. A git read the script makes itself, the commit list and each commit's deleted paths and tree, stops the run in `lib/gitcmd.py#Failed`'s line where it fails, as the script's other git reads do. A git read inside `settled` that fails returns no path there, so that commit reads as no settle and the range goes to the refusal of item 3.
2. **A range of settles alone publishes from the release pull request's body.** The script lists the merged pull requests whose base is `main` and whose head is `release/v<version>`, with `gh pr list --json number,body,mergeCommit`, and takes the one whose `mergeCommit.oid` is the commit `git rev-parse <tag>^{commit}` names. Its body takes the place `section(entries, repo)` takes in `release_body`: the header, the theme, the folds by type, the thanks, the update section and the folded part are built as for any other note. The title comes from `title_from`, and the release is created and `created=true` written as for any other note. `release_exists` still runs first, so a release already at the tag is left as it is.
3. **Every other range that added no fragment still fails, with exit 1.** That is a range with no commit other than merges, and a range with a commit that is no settle. The existing refusal line keeps its words, and the job log also names each commit of the range that is no settle, by its short hash and subject, so the person reading the log sees why the settle path was not taken.
4. **A range of settles alone whose release pull request cannot be read fails, with exit 1, and creates nothing.** That is a `gh pr list` that fails or prints no JSON, no merged pull request whose merge commit is the tagged commit, and one whose body is empty after stripping. The line says which. A note cannot be built without that body, so this read is one the note cannot go without, as `create` is, and not one the summary may skip, as `merged_pulls` is.
5. **The texts that state the old rule are rewritten in place.** They are the module docstring of `publish_release_note.py`, its paragraphs on what the body is built from, on the failure for a range that added no fragment and on exit codes; the header comment of `.github/workflows/publish-release.yml`, lines 17 to 21; the module docstring of `tests/github/test_publish_release_note.py`, its A3 line and a new line for the settle-only case. So are the texts that state the old fact that the note's folded text is the fragments, which round 1's finding 1 names: in `publish_release_note.py` the module docstring's paragraphs opening *The fragments are also a page of reasoning per change* and **The summary adds no way to fail**, the `merged_pulls` docstring and the two lines `merged_pulls` prints, with the case that pins those printed words, and the sentence of `docs/releasing/release-checklist.md` *After the merge* that rule change 5 below rewrites. A note built where `merged_pulls` fails is the theme line and the fragments, or for a range of settles alone the theme line and the release pull request's body.
6. **`skills/settle/SKILL.md` *A settle is not a work item* states the settle-only release.** One or two sentences: a settle writes no changelog fragment, and where a release carries settles alone, this repository's release workflow, `.github/scripts/publish_release_note.py` named by path alone (G7), builds the note from the release pull request's body.
7. **Cases in `tests/github/test_publish_release_note.py` pin each scenario below**, each shown red against the code at `3729b409` as contract rule 15 asks.

Out of scope:

- Republishing or marking the notes of v0.39.4 and v0.40.1, which were published by hand. The script never republishes (its docstring *It never republishes*), and marking a published note by hand is the checklist's procedure in `docs/releasing/release-checklist.md` *After the merge*, a person's act.
- A settle under a root name other than the current `lib/optin.py#HOME`. G9 shows v0.39.4 reads as no settle for that reason, and no release after this work has that shape unless the root is renamed again inside a settle-only release.
- Any change to `.github/scripts/release_mark.py` or to the jobs of `.github/workflows/publish-release.yml` (G13).
- A settle that writes a fragment of its own, which the owner declined (G5).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. A release of settles alone | Given a range that added no fragment and whose every commit other than a merge removes whole a work item directory that stood at its parent, and a merged release pull request whose merge commit is the tagged commit. When the script runs. Then it creates the release once, its body holds `header(work, closed, people)` exactly once and the release pull request's body inside the fold `FULL_SUMMARY` opens, it writes `created=true`, and exits 0. | A case in `tests/github/test_publish_release_note.py` driving `main` through `wire`, with the settle reading and the release pull request's list stubbed; seen red at `3729b409`, where `main` returns 1. |
| S2. A range with a commit that is no settle | Given a range that added no fragment, holding one settle commit and one commit that removes no directory whole. When the script runs. Then it exits 1, creates nothing, prints the existing refusal line, and names the second commit by short hash and subject. | A case of the same module; the naming of the commit is shown red at `3729b409`. |
| S3. The predicate on a real history | Given a git repository in `tmp_path` with a previous tag, a commit removing one work item directory whole, a commit removing one file from a directory that stays, and a commit outside the root. When the settle reading runs over each range. Then only the first commit is a settle, and a range holding no commit other than a merge is not a range of settles alone. | A case of the same module on a real `git` repository, the way `test_a_fragment_the_settle_removed_reaches_a_note_tagged_on_a_merge` builds one; seen red at `3729b409`, where the reading does not exist. |
| S4. A release of settles alone with no readable release pull request | Given S1's range, and in turn a `gh pr list` that fails, a list with no pull request whose merge commit is the tagged commit, and one whose body is empty. When the script runs. Then it exits 1, creates nothing, and its line names which of the three held. | Cases of the same module; seen red at `3729b409`, where no line names the release pull request. |
| S5. A range that added a fragment | Given any range with a fragment. When the script runs. Then the note is the one the code at `3729b409` builds, and the settle reading and the release pull request's list are not asked. | The existing cases of `Test_main` pass unchanged, and one case asserts that the stubbed settle reading was not called. |
| S6. The real history at v0.40.1 | Given a clone at the build's HEAD with the tags fetched. When `DRY_RUN=1 TAG=v0.40.1 REPO=MichaelYcJo/AgenticSeal python3 .github/scripts/publish_release_note.py` runs. Then it exits 0 with the line that a release already exists at `v0.40.1`, where G8's run exited 1 with the refusal. | Run by the crafter, executed, its output in the phase record. The dry run stops at `release_exists`, so it shows the refusal no longer fires and does not show the note; S1 shows the note. |

## Data & interfaces

- `publish_release_note.py` gains two readers. The names are the crafter's to choose; the contract is this. A settle reading over `revisions`, which returns the commits of the range other than merges that are no settle, each by its short hash and subject, and says whether the range held a commit other than a merge at all. A release pull request reader over `(repo, version, tag)`, which returns the body, or no body with the sentence saying why.
- `publish_release_note.py` loads `skills/code-review/scripts/chain_check.py` with `sibling.load`, as it loads `skills/settle/scripts/settle.py`, and asks its `settled`. G9 shows the load and the call work from a clone.
- `release_body(theme, rendered, pulls, owner)` keeps its signature; a settle-only note passes the release pull request's body as `rendered`.
- `wire` in the test module stubs the two new readers, so the cases that stub `fragments` with `ROOT` at a `tmp_path` that is no git repository do not reach git.
- No environment variable, no output name, no workflow job and no permission changes. `gh pr list` already runs under the workflow's `contents: write` block (`.github/workflows/publish-release.yml` lines 54 to 61).

## Rule changes

- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: It goes red on a tag whose range added no fragment the previous tag does not already hold, which is the release shipping unexplained.
  to: It goes red on a tag whose range added no fragment the previous tag
    does not already hold, which is the release shipping unexplained,
    unless the range carries settles alone. A range carries settles alone
    where every commit in it other than a merge removes whole a work item
    directory that stood at its parent, which `chain_check.py#settled`
    reads as `docs/checks/the-fold.md` *The fold, and what tells it from a
    deletion* states. A settle writes no fragment (`skills/settle/SKILL.md`
    *A settle is not a work item*), so such a release's note carries the
    body of the release pull request whose merge commit is the tagged
    commit where any other note carries the fragments, and the job goes
    red where that body cannot be read or is empty. The run that publishes
    it created the release, so the mark runs on it as on any other.
- change
  file: docs/releasing/release-checklist.md
  section: After the merge
  from: The job fails where GitHub refuses the tag; for a tag whose range added no changelog fragment the previous version tag does not already hold; for a `v*` tag that is not `vX.Y.Z`; and when a `gh` call it makes fails.
  to: The job fails where GitHub refuses the tag; for a tag whose range
    added no changelog fragment the previous version tag does not already
    hold and carries more than settles, as
    `docs/releasing/branch-and-release.md` *Cutting a release* reads a
    range; for a range of settles alone whose release pull request cannot
    be read or has an empty body; for a `v*` tag that is not `vX.Y.Z`; and
    when a `gh` call it makes fails.
- add
  file: docs/releasing/release-checklist.md
  section: The release pull request
  to: **Where the release carries settles alone, the release pull
    request's body is its release note.** A settle writes no changelog
    fragment, so the publish workflow puts the body of the release pull
    request whose merge commit the tag names where any other note carries
    the fragments (`docs/releasing/branch-and-release.md` *Cutting a
    release*). The orchestrator writes that body for a user reading the
    note: what the release changed, and what it costs an installed
    repository. A sentence in it saying that the note is still to be
    written would be published with it.
    check: tests/github/test_publish_release_note.py
- change
  file: docs/checks/the-fold.md
  section: The fold, and what tells it from a deletion
  from: `chain-check` asks one predicate, `chain_check.py#settled`.
  to: `chain-check` and `.github/scripts/publish_release_note.py` ask one
    predicate, `chain_check.py#settled`. The check asks it of a pull
    request's removed directories against the merge base, and the note
    asks it of each commit of a release's range against that commit's
    parent, where the range added no changelog fragment.
- change
  file: docs/releasing/release-checklist.md
  section: After the merge
  from: Where the job log says the pull requests could not be listed, the note went out as the theme line and the fragments alone, which one `gh release edit` repairs.
  to: Where the job log says the pull requests could not be listed, the
    note went out as the theme line and the fragments alone, and for a
    range of settles alone as the theme line and the release pull
    request's body alone. One `gh release edit` repairs either.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The docstring's claim that a range which added no fragment always fails | `.github/scripts/publish_release_note.py#module docstring`, the paragraph opening **It does fail for a range that added no fragment** | Rewritten in place to state the exception for a range of settles alone and the failures of Scope items 3 and 4. |
| The exit-code sentence's list of exit 1 causes | `.github/scripts/publish_release_note.py#module docstring`, the paragraph opening `Exit codes:` | Rewritten in place with the two new causes of Scope item 4. |
| The workflow header's sentence that the note is built from the fragments | `.github/workflows/publish-release.yml`, the header comment, lines 17 to 21 | Rewritten in place to name the release pull request's body as the source for a range of settles alone. |
| The test module's A3 line, that a range with no fragment goes red | `tests/github/test_publish_release_note.py#module docstring` | Rewritten in place to a range with no fragment that carries more than settles, beside a new line for the settle-only case. |
| The statements that a note built without its summary is the theme line and the fragments alone | `.github/scripts/publish_release_note.py#module docstring`, its paragraphs opening *The fragments are also a page of reasoning per change* and **The summary adds no way to fail**; `.github/scripts/publish_release_note.py#merged_pulls`, its docstring and its two printed lines; `docs/releasing/release-checklist.md` *After the merge* | Rewritten in place to name the release pull request's body for a range of settles alone (Scope item 5); the checklist sentence through rule change 5. |
| The hand step that wrote a settle-only release's note, and the note's missing mark and badges | Outside the tree: the notes at `v0.39.4` and `v0.40.1`, and the `## Not verified` row of #1664's body (G14) | The publish workflow writes the note and the mark job draws on it (Scope item 2, G13). The work adds a path to an existing refusal and no new gate, check, hook, label or mark, so the hand step is what it takes out in return. |

Framed 2026-11-28 by framer, before the build.

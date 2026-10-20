# Branching and releasing

Where a branch is cut from, how it merges back, and what carries the
version. It is read before a merge, which is why it is not a section of
`CONTRIBUTING.md`.

## Cutting a release

The day-of list, in the order the steps run, is `docs/release-checklist.md`.
This section is the why.

Two things carry the version, and different code reads each. A release
needs both, or the people already running the plugin are never told of it.

1. `.claude-plugin/plugin.json`: the version a session reports as loaded, and
   what `claude plugin update` installs from the marketplace clone.
2. **A `vX.Y.Z` git tag on the release commit, pushed.** `hooks/version-check.py`
   asks `git ls-remote --tags` and nothing else. An untagged release is one no
   installed session is ever told about, and a user on the previous version
   is told of a different release or of none.

```
git tag vX.Y.Z <release commit> && git push origin vX.Y.Z
```

Check both agree before announcing anything:

```
git describe --tags   # must name the release, not "<tag>-N-g<sha>"
```

**A release pull request that changes what the plugin ships moves the
version.** `tests/test_chain_hooks_hardening.py` binds the changelog to
whatever `plugin.json` says, and the `hygiene` workflow fails a release pull
request, one whose base is `main`, that changes `skills/`, `agents/`,
`hooks/`, `templates/`, `bin/` or `.claude-plugin/` without moving the
version. The tag is still the maintainer's to push; nothing in CI can do it.
check: tests/test_the_release_check_watches_what_ships.py .github/workflows/hygiene.yml

**Every act the release performs once it reaches `main` belongs to a machine or
to a command that answers it, and none of them waits on somebody remembering.**
A step a person can skip is a step that gets skipped. Two different pushes
fire two of the acts. The merge to `main` fires the close-issues workflow, so
the label is created and spent before any tag exists. The tag push, the
maintainer's last act, fires the note, because a note has to name a tag.

- **The release note publishes itself.** `.github/workflows/publish-release.yml`
  fires on the `v*` tag push and publishes the release's own file,
  `changelog/X.Y.Z.md`, which the preparation commit gathered, titled from the
  tagged commit's `release: X.Y.Z — <symptoms>` line
  (`docs/release-checklist.md` *5. The release pull request*), the dash being
  part of the title the workflow matches. It never republishes a release that exists,
  and falls back to the tag name when that line is missing or carries no
  symptoms. It goes red on a tag with no release file, or one with no section
  for the tag, which is the release shipping unexplained. The note opens with
  a summary read from the pull requests merged into `release/vX.Y.Z`: counts,
  one line per pull request under its conventional-commit type with the issues
  it closed, a `### 🙌 Thanks to` line for every author other than the
  repository owner and bots, and how to update. The gathered section follows,
  folded. A pull request title is therefore a line of the release note: write
  it as one. **Then the release's seal is attached.** A second job in the same
  workflow runs only when this run created the release. It runs the suite at
  the tag, draws the owner's seal from `.github/scripts/release-seal.svg` with
  `rsvg-convert`, which the job installs, attaches it as `seal.png`, and
  replaces the glance table with the image at its display width and one line
  of the table's counts. That edit is the only change it makes to a note, and
  only to one whose glance table is still exactly as it was generated. Any
  failure is a `::warning::` in the job log and leaves the note as it was
  published, so the seal can never turn the release red. How a browser shows
  the image on the release page is seen by a person; the job reads no page.
- **The marketplace files are read by a command that never fails a release, and
  the plugin directory by a person.** `.github/scripts/plugin_directory_check.py`
  reads the two marketplace files on GitHub, a curated catalog that takes
  outside plugins through the directory's submission and a nightly mirror of
  its review pipeline, and says per file whether the plugin has an entry, which
  commit it pins and whether that commit is on `main`. It exits 0 whatever it
  finds: those files sync on somebody else's schedule, and a red nobody here
  can act on is what `CLAUDE.md`'s first goal is against. The directory's own
  state, whether the plugin is published there and at which version, is not
  among its answers, because no script can reach the directory; the command
  says so and prints the page a person opens. Nothing fires it; a person runs
  it at the checklist's box. Submitting a plugin, or moving a Console listing
  to the developer portal, is a person's act.
- **A label a document specifies is created and spent by a workflow.** When
  the release reaches `main`, the close-issues workflow runs
  `.github/scripts/tracker_labels.py --apply`, which creates every declared
  label the tracker lacks, and takes `size: now` off each issue it closes.
  `docs/issues-and-milestones.md` owns what the label means; this says only who
  performs the acts. Whether the label exists is what `gh label list` says.

`docs/release-checklist.md` *6. After the merge* carries a box for each of the
first two. The first confirms the workflow fired and is not where the note
gets written; the second is where the command is run.
check: tests/test_a_release_publishes_its_note.py tests/test_the_release_tail_does_not_end_at_the_tag.py tests/test_the_release_seal_is_drawn.py

Which workflows GitHub starts on which event, and which run a newer push
cancels, is GitHub's behaviour. No case here can start a run, so
`gh run list --branch <branch>` on a pull request is what reads it.

### Work accumulates on a release branch

The marketplace clone tracks `main`, so `claude plugin update` installs
whatever `main` holds. Merging is shipping, and the tag only decides whether
anyone is told. Batching tags is therefore not a way to release less often:
it ships the content and announces nothing, the same silence as an untagged
release.

So `main` moves once per release, and work collects on a branch cut for that
release.

```
main ──cut──▶ release/vX.Y.Z ──cut──▶ feature branches
                    ▲                        │
                    └────── squash ──────────┘
                    │
              merge commit
                    ▼
                  main ──▶ tag
```

**Which button, for each direction.** The method is not a preference. Pick the
other one and something downstream stops resolving, so this table is the whole
rule and the paragraphs below are why.

| From | To | How | The button on GitHub |
|---|---|---|---|
| `main` | `release/vX.Y.Z` | cut a branch | — |
| `release/vX.Y.Z` | a feature branch | cut a branch | — |
| a feature branch | `release/vX.Y.Z` | **squash** | *Squash and merge* |
| the release-prep branch | `release/vX.Y.Z` | **squash** | *Squash and merge* |
| `release/vX.Y.Z` | `main` | **3-way merge** | *Create a merge commit* |
| a hotfix branch | `main` | **3-way merge** | *Create a merge commit* |

The last two rows are one rule: **anything reaching `main` is a merge commit.**
A hotfix squash costs nothing only while no round record names its commits,
and that is a condition nobody should have to check at the merge button, so
the ruleset does not offer the choice.

**What breaks when the last row is squashed.** A squash discards every commit
the release branch wrote, and anything naming one of them by SHA stops
resolving.

**The `target:` line in every `round-N.md` names a commit.** After a squash it
resolves for nobody, which is why the check reads it only while the branch
that holds the commit is open (`docs/the-review-record.md` *The round record*).
check: tests/test_a_rider_reaches_its_file.py

**A third reader of those commits is outside this repository.** A marketplace
file lists an external plugin by pinning a commit of its source repository,
and an entry that also carries a `ref` usually names `main` or `master`, so
the `sha` is what a reader resolves. The plugin directory, the catalog people
browse inside Claude, holds a commit too: a plugin submitted at its developer
portal is served from a scanned commit of the branch or tag the submission
tracks (`claude.com/docs/plugins/submit`). Breaking the rule above therefore
also breaks a consumer nobody here can reach, for people the owner cannot
name. `docs/release-checklist.md` *6. After the merge* carries the box that
reads what is pinned. This paragraph is a record rather than a rule: a
marketplace file pins a commit of each outside plugin's source repository.
The rule it supports, that anything reaching `main` is a merge commit, is held
outside the tree by the `main` ruleset.
check: none reader: the main ruleset on GitHub

**The plugin's name is fixed, and that is not a style question.** Everybody
already running it installed it under its slug, so renaming it breaks their
install, and a marketplace file keys its entry on the same name, so a rename
reads there as the plugin having vanished rather than moved.
`.claude-plugin/plugin.json` holds the one copy; nothing else in the tree
spells it, which is why `plugin_directory_check.py` reads the name out of that
file instead of carrying a literal.

**Two rulesets enforce the merge methods.** The repository-wide merge-method
setting is one switch for every branch, so it cannot allow a squash into the
release branch while requiring a merge commit into `main`. A ruleset targets a
branch pattern, so two of them can disagree on purpose.

| Ruleset | Targets | `allowed_merge_methods` |
|---|---|---|
| Main | `main` | `merge` |
| Release branches | `release/*` | `squash` |

GitHub hides the merge methods a ruleset excludes, so the wrong button is not
offered. Both rulesets require a pull request, so neither branch takes a
direct push, and there are no bypass actors: the rule applies to the owner
too. The release-preparation commit therefore needs a branch of its own and a
squash merge, like any other work.

- **`release/vX.Y.Z` is cut from `main`.** Not from the previous release
  branch, and not from a long-lived branch that outlives its release. An
  accumulation branch that survives a release has to be brought back to `main`
  afterwards, and nothing enforces that.
- **Feature branches are cut from the release branch** and squash back into
  it. One squashed commit per branch, so the release branch reads as the
  changelog it is about to become.
- **A squashed feature branch can be deleted once its pull request merged.**
  `chain_check.py` reads a round's `target:` commit only as HEAD or an ancestor
  of it, so the commits a round reviewed are read while the pull request that
  carries them is open, and no step fetches a ref the checkout lacks. The
  checks ship to user repositories as `templates/hygiene.yml`, run from a
  clone of this repository at the release installed when the `implement`
  skill wrote the file at a shared-mode first setup; local mode installs
  none, because the checks read committed files and local mode commits none.

  Keeping the branch is still worth something: it leaves the rounds and the
  verdict readable on a branch nobody merged, which is the only place the
  reason it was not merged is written down.
- **The release branch merges into `main` as a merge commit**, carrying one
  commit of its own: the one that gathers the changelog fragments into
  `changelog/X.Y.Z.md` under `## X.Y.Z — <date>`, heads the index
  `CHANGELOG.md` with that line, and moves `plugin.json`. Then the tag. It is
  also the moment every issue this release closes gets closed, by a workflow
  rather than by anybody's hand; the paragraphs below say how, and what a
  feature pull request writes so it has something to read.
- Feature pull requests write their entry to
  `seal/specs/<work-item-id>/changelog.md` and leave `CHANGELOG.md`,
  `changelog/` and `plugin.json` alone. The hygiene workflow asks for the bump
  only when the base is `main`, which is what makes that enforceable.

**The changelog entries arrive as fragments, and the release gathers them.**
Which file a change writes, and why, is `docs/the-record-layout.md` *A change
writes fragments, never a shared file*. Release preparation runs:

```
python3 .github/scripts/gather_changelog.py --version X.Y.Z
```

It concatenates every fragment that no release file carries yet into
`changelog/X.Y.Z.md`, a file of the release's own that opens with its dated
`## X.Y.Z — <date>` line, and heads the index `CHANGELOG.md` with that same
line and a link to the file. A second gather for the same version appends
into the file and keeps its date. Each entry is written under an HTML comment
naming its work item, invisible to a reader and the only link from a released
entry back to the work that produced it. `--check` reports fragments that
never arrived, and the hygiene workflow runs it on every pull request into
`main`, so a release cannot go out with a change that ships unexplained.
`--dry-run` prints the section and writes nothing, in either file.

A fragment carries no line starting `## `, and it closes every fenced block
and HTML comment it opens. The released section ends at the next `## ` line,
for the gather and for the release note alike, so every entry after it would
ship under no version; and a block left open would hide the next work item's
marker, so `--check` would call a gathered entry missing. The gather refuses
either fragment, with or without `--dry-run`, before it writes or prints a
section, and names the fragment, the line number and the line. Demote the line
to `###` or lower, or close the block, in a pull request into the release
branch, then gather again. A fragment already in a release file is not read
again. `CHANGELOG.md` holds no section that entries accumulate under, such
as `## Unreleased`; the fragments are that region.

**The two merge shapes are not interchangeable.** Squash into the release
branch keeps one entry per change; a merge commit into `main` keeps
`git log --first-parent main` at one line per release. Reversing them buries
the release history under every review round.

**A closing keyword does nothing when the base is `release/vX.Y.Z`.** GitHub
acts on `Closes #N` only when the pull request carrying it merges into the
repository's default branch, and that branch is `main`. A branch cut from the
release branch merges back into it, so nothing reads the keyword, the merge
goes through, and the issue is still open afterwards.

The base is what decides this, not the kind of branch. A hotfix taken straight
into `main` has its `Closes #N` fire, so a hotfix that goes to `main` writes
the keyword and gets the close. What follows is about everything that goes to
the release branch first, which is nearly everything.

**Such a pull request left no LINK either, though the mention survives.** The
formal link, the one in an issue's sidebar and the one `gh pr view --json
closingIssuesReferences` reports, is not created outside the default branch,
and no `connected` event lands on the issue's timeline. What survives is the
cross-reference, so the issue still shows the pull request mentioning it. The
issue knows a pull request talked about it and does not know one answered it.

**The squash commit message does not carry the keyword either**, so the
release merge does not fire one as a side effect. GitHub builds that message
from the branch's commit subjects, which reference issues by bare number at
most. A release closes nothing on its own.

**So a workflow reads the keywords instead, when the release reaches `main`.**
`.github/workflows/close-issues-on-release.yml` runs on a push to `main`, takes
the `(#N)` out of each squash-commit subject that arrived, reads those pull
request bodies, and closes what their keywords name. The session that knew
which issue it was answering wrote the answer down, and this is what acts on
it.

**A second workflow reads the same keywords earlier, and writes no close.**
`.github/workflows/label-merged-on-release-branch.yml` runs on a push to
`release/*` and puts `merged: X.Y.Z` on the issues those same bodies name, so
that a ticket already in the release stops looking like one nobody has
started. It answers *is this in yet*, which the paragraph above leaves open
for the length of a release; *is this done* is still the close, still when
`main` moves. `docs/issues-and-milestones.md` owns both mechanisms and the
reason the two moments are different.

Collecting the numbers into the release pull request's own body would be a
step somebody has to remember. The workflow is the same act with nobody to
forget it, and it needs no new writing: keep putting `Closes #N` in a feature
pull request body.

It only ever closes, and an issue already closed is skipped rather than
re-announced, so a re-run changes nothing. A force-push is a different case
and not a safe one: GitHub sends the SHA the push displaced, and where the
runner cannot reach it the range fails and the run stops, which is the right
direction and not the same as being harmless. `DRY_RUN=1` prints what it would
do and writes nothing.

**One issue the tracker refuses does not leave the rest open.** Every issue is
attempted. A refusal on `gh issue close` falls back to the REST route
(`gh api -X PATCH …/issues/<n> -f state=closed`, then the same comment through
`gh api …/issues/<n>/comments` where the refused route did not already post
it; `gh issue close --comment` comments before it closes, so it usually did).
Each fallback is printed, so the job log says how many took it, and the run
exits non-zero only at the end, naming each issue both routes refused with
both errors. A partial close is repaired by re-running the script with the
run's `BEFORE`, `AFTER` and `REPO`: it skips what is already closed and
reaches the rest.
check: tests/test_the_closer_carries_on_past_a_refusal.py

```
Closes #88
```

One keyword, one number, in the body of the pull request that answers that
issue. Where one pull request answers several, the keyword repeats before
every number, because GitHub's documentation asks for the full syntax before
each issue and sanctions no shorter form. What GitHub does with
`Closes #88, #92` is written down nowhere, and the workflow above does not
read it as two either.

`Part of #N` remains the form for a pull request that advances an issue without
finishing it. It links for a reader and asks nothing to close.

**The version is provisional until the content settles.** Release when the
accumulated changes read as one changelog entry, not on a commit count, so
whether the number is a minor or a patch is known at the end, not at the cut.
Rename the branch if the answer changes; while it is unpushed that costs
nothing.

**`main` stays the default branch.** A fresh marketplace clone lands on the
default branch, so making a release branch the default would hand every user
the unreleased tree.

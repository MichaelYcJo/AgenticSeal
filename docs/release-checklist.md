# Release checklist

The sequence in `docs/branch-and-release.md`, as the list to work down on the
day. That document says why each step exists; this one says what to type and
what to look at before the next step.

`X.Y.Z` is the release. Nothing below names a real version, because
`tests/behaviour/test_release_hygiene.py` refuses a loaded document that names the one
running.

## 0. Before starting

- [ ] Every work item of the release is squash-merged into `release/vX.Y.Z`
      and its pull request's CI was green **at the commit that merged**. A
      merge pressed while a later push was still on its way takes the earlier
      commit; the corrections then need a pull request of their own.
- [ ] Merge the release branch into a work item's branch only when the
      branch needs something the release branch holds; the squash discards
      the merge commit either way.
      **Never rebase a work item's branch, for any reason.** Every round
      record names its branch's commits on its `target:` line, and a rebase
      orphans them.
- [ ] **The milestone `release: X.Y.Z` holds what this release is actually
      carrying, and nothing else.** Every open issue in it that is not
      shipping moves to another milestone now, a planning act that needs no
      code. Left, the release pull request goes red at step 5:
      `release_completeness_check.py` refuses while the milestone claims an
      open issue the release branch does not carry, and names each one, at
      the worst moment to do the planning.
- [ ] No other Claude session is working in this checkout, and the editor is
      not about to pull. An editor's pull can switch the checkout to another
      branch between two commands, and the preparation commit lands there.
      `git status -sb` after every `switch` is the cheap check.

## 1. The preparation branch

```bash
git fetch origin
git switch -c chore/the-fragments-become-X.Y.Z origin/release/vX.Y.Z
git status -sb          # the branch you asked for, tracking the release
seal no-work-item       # this branch's changes belong to no work item
```

The `release/*` ruleset takes no direct push, so the preparation commit needs
this branch and a squash merge like any other work.

## 2. Gather, bump

**The preparation commit gathers the changelog fragments.**

```bash
python3 .github/scripts/gather_changelog.py --dry-run --version X.Y.Z
```

Read it. Then:

```bash
python3 .github/scripts/gather_changelog.py --version X.Y.Z
sed -i '' 's/"version": "A.B.C"/"version": "X.Y.Z"/' .claude-plugin/plugin.json
git add -A changelog/ CHANGELOG.md seal/ .claude-plugin/plugin.json
```

The gather writes a new file, the release's own `changelog/X.Y.Z.md`, and
heads the index `CHANGELOG.md` with its line. It is staged before step 3 runs
anything, because the suite lists files with `git ls-files`, which reads the
index: an untracked release file is a tree the listing does not describe.
check: tests/text/test_the_changelog_is_gathered_at_release.py tests/github/test_gather_changelog.py

**A second gather for the same version appends into its section.** A fragment
landing after this step, while the release pull request is red, is the
ordinary shape. Run the same command again: the new entries join the
existing section, the section keeps the first gather's date, and
`tests/behaviour/test_release_hygiene.py` refuses a file that heads a version twice.
check: second-gather-appends tests/behaviour/test_release_hygiene.py

**The preparation commit writes the process archive,
`seal/process/X.Y.Z.md`, from `templates/records/process.md`.** The archive records
what this release changed in the way of working and why, one row per change.
`CLAUDE.md`, `agents/*.md` and `skills/*/orchestration.md` are the way of
working, and `git log vA.B.C..HEAD` over those paths, with the milestone's
issue comments, gives the rows. Each row is a date, the change, one line of
why, and a link to the issue comment or commit it came from, and nothing
else. It is written once, here, because one file that every branch edits is
the conflict the changelog fragments ended. A release that changed none of
those files writes no archive file.
check: none reader: the framer of the next release

## 2b. Settle what earlier releases left behind

**`settle` runs when the owner calls it, not at every release.** A release
whose owner has not called it skips this step, and the work items wait on
disk for the settle the owner calls.

```bash
seal settle
seal settle --apply
seal fold
```

The first prints each group of released specs whose rule changes name one
section, in merge order, and every open row of every released record.
Between the first and the second, the session running the settle writes each
section as its group's latest decision, checked against the code, and closes
each open row with what closed it, asking nobody. The second removes every
released work item directory whose record holds no open row, and names any
it keeps. `seal fold` then reads
the documents the settle wrote, and names each one past its ceiling as one
to split (`skills/settle/SKILL.md` *A document past its ceiling is split,
never trimmed*). The settle's pull request body states each decision with
its grounds and lists the defaults it took, and the owner reviews it.

`skills/settle/SKILL.md` is the procedure. **A settle is not a work item**:
it opens no directory under `seal/threads/`, its session runs
`seal no-work-item` on the settle's branch before the first edit, and each
of its commits carries the trailer `Seal-Routing: no work item`, as
step 4 shows. It owes an answer for every check in this repository carrying
a population floor over `seal/threads/`.

## 3. Verify before committing

The preparation commit is the first time a fragment's prose is read by the
tests that scan the release files under `changelog/`. So the whole gate runs
on this tree, and every exit code is read directly rather than through a
`| tail`.

**A sweep that walks a git listing judges what remains instead of stopping at
the first tracked file the disk lacks, and a case whose verdict needs the
whole corpus says so.** A tree can hold tracked files the disk does not have,
a removal nothing has staged yet. So a count line reading `… passed, N
skipped` with reasons naming paths is that state rather than something to
debug; one appears when the tree is mid-edit somewhere a check like that
reads, under `docs/`, `skills/`, `templates/`, `tests/` or a shipped `.py`.

```bash
python3 .github/scripts/gather_changelog.py --check
uvx ruff check . && uvx ruff format --check .
bin/test -q
python3 skills/code-review/scripts/chain_check.py --baseline origin/main
```

What each one has caught, so a failure is recognised rather than debugged:

| Check | What it found at a release |
|---|---|
| the full suite | a gathered entry prescribed a `git mv` whose destination nothing creates |
| `test_no_loaded_file_names_a_version_at_or_above_the_running_one` | living prose that named the release by number, or a version ahead of it. A record of a moment is listed in the test; anything else is reworded to name the change, or to the illustrative version the test's own message points at. A version this repository has *tagged* is history and may be named: the shipped set is read from the root's `v*` tags, never from this file, because this commit writes the heading and the bump together |

check: tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py tests/test_conftest.py

## 4. Commit, push, open the first pull request

The commit belongs to no work item: it is the routing question's
`no work item` answer (`skills/implement/orchestration.md` *Question 1*), and
that answer's recorded form is `seal no-work-item`, run in step 1 before the
first edit, and the trailer `Seal-Routing: no work item` on each commit:

```bash
git commit -m "chore: release X.Y.Z — <what the fragments say>" -m "Seal-Routing: no work item"
git push -u origin chore/the-fragments-become-X.Y.Z
gh pr create --base release/vX.Y.Z --head chore/the-fragments-become-X.Y.Z \
  --title "chore: release X.Y.Z — <the same line>" --body-file <file>
```

The title's count of fragments is the count `--version` gathered, not the count
`--check` reports: the latter includes every fragment of every earlier release.

- [ ] **Wait for CI on the pull request head before pressing *Squash and
      merge*.** Read `gh pr checks <n>` and compare the head SHA to the one
      just pushed.
- [ ] A body edit goes through `gh api -X PATCH repos/<owner>/<repo>/pulls/<n>
      -F body=@<file>`; `gh pr edit` fails on a deprecated Projects query in
      some `gh` versions and leaves the body unchanged without saying so.

## 5. The release pull request

```bash
gh pr create --base main --head release/vX.Y.Z \
  --title "release: X.Y.Z symptoms: <the symptoms the release answers>" --body-file <file>
```

Its hygiene checks fail until step 4 is squashed in, by design. Then they go
green without a push. Press ***Create a merge commit***, never squash: the
review records name the release branch's commits on their `target:` lines, and a
squash discards them.

**Read the release table before the merge.** The pull request's `tests` run
carries it in the `release-report` job's summary, under *Against vA.B.C*:
each agent's preload bytes, the suite's seconds, each leg's minutes and each
document's bytes, beside the same reading at the last release tag, and under
it each test file's priced cases and seconds at the tag and now. It fails
nothing. A preload or a document that grew is a question the pull request's
body answers, or an issue it opens. A leg's minutes compare one run with one
run and swing on the same code, so they are read and never acted on alone.

**Each release clears what grew.** The test file rows are a report and never
a ceiling: a heavily exercised module needs the cases it needs. The owner
reads the rows whose seconds or cases grew most since the tag and sweeps each
such module with one `bin/seal mutate` call carrying a mutant per class,
for cases that kill nothing another case does not. The sweep's cuts land in
a work item of the next release with one line per cut case, the shape
`CONTRIBUTING.md` *The test layout* gives.
check: none reader: the owner at release preparation

### What a release pull request is held to

**A loaded file naming a version at or above the running one is a timer.** A
document that names a version which does not exist yet goes red on the commit
that writes it rather than on the release that ships it, so the refusal
covers every version at or above the running one rather than the running one
alone, less the versions this repository has tagged: from the preparation
commit until the next bump the running version is one that has already
shipped, and a tag is what says so. Three exemptions, each argued where the
rule is: the illustrative version this repository already writes, records of
a moment under `docs/experiments/`, and a version belonging to another
product.
check: tests/behaviour/test_release_hygiene.py

**A contributor whose base is wrong is told the base is wrong.** The
procedure a contributor needs is the first thing in the contributing guide,
not the fourth: which branch to base on and how to find it, what they do, and
what they are not asked to do. A pull request template carries the
base-branch fact itself rather than only a link, because its whole advantage
is that it reaches somebody who opened no document, and the refusal message
of the check that fires on a wrong base says which fact is wrong.
check: tests/behaviour/test_the_release_check_watches_what_ships.py tests/behaviour/test_the_contributor_has_a_procedure.py

## 6. After the merge

```bash
git tag vX.Y.Z <merge commit> && git push origin vX.Y.Z
git describe --tags     # names the release, not "<tag>-N-g<sha>"
```

The version hook reads tags and nothing else; an untagged release is one no
installed session is ever told about.

Two acts come after the tag: publishing the release note, and telling the
plugin directory. The first box carries the command that answers it; the
second carries the command that reads what a script can and names the page
that answers the rest, because a box a reader cannot act on is the same
defect one layer up.

```bash
gh release view vX.Y.Z                              # did the note publish
python3 .github/scripts/plugin_directory_check.py   # what the marketplace files hold
```

- [ ] **A GitHub Release exists at `vX.Y.Z`**, by `gh release view vX.Y.Z`.
      The tag push fires `.github/workflows/publish-release.yml`, which
      publishes it from the release's file step 2 already gathered, with
      the title taken from the `release: X.Y.Z symptoms: <symptoms>` line
      step 5 prescribes. **This box confirms the workflow fired; it is not where the
      note gets written.** Nothing there means the job went red or never ran,
      and `gh run list --workflow publish-release.yml` says which. The job
      fails for a tag whose release file, `changelog/X.Y.Z.md`, is not there
      or carries no section for it, which is step 2 not having happened; for
      a `v*` tag that is not `vX.Y.Z`; and when a `gh` call it makes fails.
      A missing title line is not one of them: it falls back to the tag
      name. The note opens with a summary of the release's pull requests
      and a `### 🙌 Thanks to` line for each outside contributor, over the
      section folded; where the job log says the pull requests could not be
      listed, the note went out as the section alone, which one
      `gh release edit` repairs. After the note, the same workflow's `seal`
      job attaches `seal.png` and puts it where the glance table stood.
      Where the note still shows the table, the `seal` job's log says why on
      a `::warning::` line: the suite at the tag did not pass, the seal could
      not be drawn or written, a `gh` call failed, or
      the glance table was not in the note as generated: edited before the
      job reached it, published without one, or the pull requests moved
      between the two lists. That job never fails the release.
      To draw one by hand, from a checkout at the tag, with a `python3` that
      imports Pillow, run the suite with the broad gate's recorder loaded
      (`PYTHONPATH="$PWD/skills/verify/scripts/pytest_record"`,
      `PYTEST_ADDOPTS='-p agentic_pytest_record'`, and
      `AGENTIC_RECORD_DIR` and `AGENTIC_RECORD_KEY` naming a directory
      that exists and a key you choose), then run
      `DRY_RUN=1 python3 .github/scripts/release_seal.py` with `TAG`,
      `REPO`, `SUITE_RECORDS` (that directory) and `SUITE_KEY` (that key)
      set; attach the PNG it names with
      `gh release upload`, then apply the note it prints with
      `gh release edit --notes-file`.
- [ ] **The marketplace files and the directory's page have been read**, by
      `python3 .github/scripts/plugin_directory_check.py`. It reads the two
      marketplace files on GitHub and says, per file, whether this plugin has
      an entry, which commit the entry pins, and whether that commit is an
      ancestor of `main`. **It reports and never fails**, deliberately: the
      files sync on somebody else's schedule, one of the two once went
      twenty-eight days without a commit, and a red nobody can act on is what
      `CLAUDE.md`'s first goal is against. Those files are not the directory,
      the catalog people browse inside Claude, and the directory is readable
      from nowhere a script can reach, so the command ends by saying it was
      not read and printing the address of the page that answers. A portal
      listing is answered on the portal's Submissions page, with its status
      and the version that is live. It picks up each new version from its
      tracked branch without a resubmission, and a version that passes goes
      live by the listing's publish setting, which by default waits for
      somebody to select Publish (`claude.com/docs/plugins/submit`, *Publish
      a passing version*). A Console listing is answered on the Console
      page. The plugin's listing is a Console listing, by the repository
      owner's reading of the Console page on 2026-10-07, and a Console
      listing takes no new
      version until a person moves it to the portal
      (`claude.com/docs/directory/publish`, *Move an earlier submission to
      the developer portal*), so no release reaches the directory through it
      until then. Whether it shows up at all is what a search for the
      plugin inside Claude answers. Neither that search nor the Console page, which
      sits behind the owner's login, is open to a script or a case here:
      both answers are the owner's reading.

**A notice telling somebody an update landed names the move it costs them.**
An installed copy is what a session loads, so an update that has landed on
disk is not an update that is in force until the session reloads, and
reloading is the expensive part, not the install. Every place this repository
tells a user what to do after an update names the reload command, says what a
reload was measured to do, and says what nobody has measured about it. A
session-start hook writes into a session and cannot type into one, so running
it for the user is not on offer, and a notice that leaves the cost out reads
as though there were none.

The close-issues workflow has already run by now. It fires when `main` moves,
which is the merge above rather than anything you do here, and it reads the
**pull request bodies** the release carries: every `Closes #N` a feature
pull request wrote, acted on at last, because GitHub reads a closing keyword
only for a pull request whose base is the default branch. It does not read
the changelog section.

- [ ] **Every issue the run named is closed**, by `gh run list --workflow
      close-issues-on-release.yml --limit 1`, then the job log. The run
      attempts every issue and falls back to the REST route where `gh issue
      close` is refused; a red job is one where both routes refused an
      issue, and its last lines name each one with both errors. Repair it
      from a clone that has both commits, with the run's own inputs:

      ```bash
      BEFORE=<github.event.before> AFTER=<github.event.after> REPO=<owner>/<repo> \
        python3 .github/scripts/close_issues_on_release.py
      ```

      It skips what is already closed and reaches the rest; `DRY_RUN=1` in
      front of it prints the plan and writes nothing.

Leave the `merged: X.Y.Z` labels where they are. They accumulate, one per
release, and that is deliberate: deleting a label deletes it from every issue
that ever carried it, which falsifies the record the label was created to
leave.

- [ ] Local `release/vX.Y.Z` and `main` fast-forwarded; the preparation
      branch deleted or left, either is fine.
- [ ] The next release branch is cut from `main`, not from this one.

check: tests/hooks/test_version_check.py

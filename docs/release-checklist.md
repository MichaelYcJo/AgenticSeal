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

## 2b. Settle what earlier releases left behind

**`settle` runs when the owner calls it, not at every release.** A release
whose owner has not called it skips this step, and the work items wait on
disk for the settle the owner calls.

```bash
seal settle
seal settle --apply
seal fold
```

The first prints each group of released designs whose rule changes name one
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
of its commits carries the trailer `Seal-Routing: no work item`, the
recorded form of the routing question's `no work item` answer
(`skills/commit-pr-convention/SKILL.md`). It owes an answer for every check
in this repository carrying a population floor over `seal/threads/`.

**Before `seal settle --apply`, the settling session counts, for each released work item routed through the review chain, the findings, the findings that carry a `regression:` or `reopens:` line, the findings whose every `location:` path is under `seal/threads/`, and the rounds, and posts the four numbers as a comment on the open `flow-baseline` issue.** The four are read from the work item's `trail/rounds/round-*.md` with `grep -h`, which reads a file wherever it lies: the `### <n>.` finding headings; the `regression:` and `reopens:` lines; the `location:` lines left with no backticked path once every path under `seal/threads/` is deleted from them; and the files. They are this repository's measure of #1148, which removed the records' copies of one another: 0.24.0's four work items read 17 recurring of 36 findings, 12 in records alone, and 0.25.0's one read 3 of 10, 1 in a record alone. A release whose records-alone count does not fall says the records still restate one another, and the next step is #1020's check that reads recurrence. The step is this repository's and ships to no user: the plugin's settle procedure (`skills/settle/SKILL.md` *The settling session's procedure*) does not take it, because the reader of the four numbers is this repository's owner and most installed repositories keep no `flow-baseline` log.
check: none reader: the owner's settling session at this step

**What `seal settle --apply` removed is committed before anything switches that checkout to another branch.** `--apply` deletes each directory from the working tree and stages nothing, and `git switch` exits 0 over an unstaged deletion while it restores every deleted file that differs between the two branches, saying nothing about it. In the 0.24 settle a switch to `main` and back restored 28 `gaps.md` files, the removal commit left them tracked, and the broad gate refused the tree. A comparison with another ref runs in a `git worktree` of that ref.
check: none reader: the owner's settling session at this step

**Before `seal settle --apply`, the settling session reads the dry run's *The judgments*, the orchestrators' rows from every released `frame/plan.md` grouped by the document each stands on, and rewrites a section where one kind of judgment recurs across work items or kept costing rounds.** The rows leave with their directories at `--apply`, so this is the one reading they get; `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* says the guidance improves from that record and not from memory.
check: none reader: the owner's settling session at this step

## 5. The release pull request

```bash
gh pr create --base main --head release/vX.Y.Z \
  --title "release: X.Y.Z symptoms: <the symptoms the release answers>" --body-file <file>
```

**The orchestrator opens the release pull request, and the owner's one
required act at a release is its merge.** The reads below and the boxes of
step 6 are reports that fail nothing. The version moved in the release's
first pull request, so no pull request comes between the last work item and
this one. The orchestrator opens it with the first work item pull request
into `release/vX.Y.Z` that finds none open, and leaves it open. Its milestone
check fails while the milestone claims an issue the branch does not carry,
by design, and goes green on the push that merges the last one.
check: tests/github/test_release_completeness_check.py

Press ***Create a merge commit***, never squash: the review records name the
release branch's commits on their `target:` lines, and a squash discards
them.

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
check: none reader: the owner before the release pull request's merge

### What a release pull request is held to

**A loaded file naming a version at or above the running one is a timer.** A
document that names a version which does not exist yet goes red on the commit
that writes it rather than on the release that ships it, so the refusal
covers every version at or above the running one rather than the running one
alone, less the versions this repository has tagged: from the release's
merge until the next release's first pull request moves the version, the
running version is one that has already shipped, and a tag is what says so.
Three exemptions, each argued where the rule is: the illustrative version
this repository already writes, records of a moment under
`docs/experiments/`, and a version belonging to another product.
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
git fetch origin --tags
git describe --tags origin/main   # names the release, not "<tag>-N-g<sha>"
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
      The merge's push to `main` fires
      `.github/workflows/publish-release.yml`, which tags the merge commit
      `vX.Y.Z` and then, in the same run, builds the note from the changelog
      fragments the release's commits added and the previous version tag
      does not already hold, with the title taken from the
      `release: X.Y.Z symptoms: <symptoms>` line step 5 prescribes. **This
      box confirms the workflow fired; it is not where the note gets
      written.** Nothing there means the job went red or never ran, and
      `gh run list --workflow publish-release.yml` says which. A run that
      created no tag says why on its tag step's `no tag:` line: the push did
      not move `plugin.json`'s version, which the release's first pull
      request owed, or `vX.Y.Z` already names another commit. The job fails
      where GitHub refuses the tag; for a tag whose range added no changelog
      fragment the previous version tag does not already hold; for a `v*`
      tag that is not `vX.Y.Z`; and when a `gh` call it makes fails. A
      missing title line is not one of them: it falls back to the tag name.
      The note opens with the release's theme line, then a summary of the
      release's pull requests and a `### 🙌 Thanks to` line for each outside
      contributor, over the fragments folded; where the job log says the
      pull requests could not be listed, the note went out as the theme line
      and the fragments alone, which one `gh release edit` repairs. After
      the note, the same workflow's `seal` job attaches `seal.png` and puts
      it where the glance table stood. Where the note still shows the
      table, the `seal` job's log says why on a `::warning::` line: the
      suite at the tag did not pass, the seal could not be drawn or
      written, a `gh` call failed, or the glance table was not in the note
      as generated: edited before the job reached it, published without
      one, or the pull requests moved between the two lists. That job never
      fails the release. To draw one by hand, from a checkout at the tag,
      run the suite with the broad gate's recorder loaded
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
      twenty-eight days without a commit, and a red nobody can act on is what `skills/core/SKILL.md` *The first value: efficient development through the workflow* is against. Those files are not the directory,
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
the changelog fragments.

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

- [ ] Local `release/vX.Y.Z` and `main` fast-forwarded.
- [ ] The next release branch is cut from `main`, not from this one, named
      for the version its milestone `release: X.Y.Z` carries, and its first
      pull request moves `plugin.json` to that version.

check: tests/hooks/test_version_check.py

**The milestone `release: X.Y.Z` is closed once the close-issues run has closed its issues, by `gh api -X PATCH repos/<owner>/<repo>/milestones/<number> -f state=closed`.** Nothing else closes it: `.github/scripts/close_issues_on_release.py` closes each issue and leaves the milestone open with none in it, which reads as a release still in flight. `release: 0.20.0` stood open eleven days after its tag and `release: 0.21.0` five, each closed by hand.
check: none reader: the orchestrator after the tag

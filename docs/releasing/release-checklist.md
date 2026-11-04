# Release checklist

The sequence in `docs/releasing/branch-and-release.md`, as the list to work down on the
day. That document says why each step exists; this one says what to type and
what to look at before the next step.

`X.Y.Z` is the release. Nothing below names a real version, because
`tests/behaviour/test_release_hygiene.py` refuses a loaded document that names the one
running.

## 0. Before starting

- [ ] Every work item of the release is squash-merged into `release/vX.Y.Z`
      and no check of its pull request was red **at the commit that
      merged**. The rulesets hold the `lint` and `release` jobs there
      (`docs/releasing/branch-and-release.md` *Work accumulates on a
      release branch*), so the look is for the checks no ruleset requires.
      A merge pressed while a later push was still on its way takes the
      earlier commit; the corrections then need a pull request of their
      own.
- [ ] Merge the release branch into a work item's branch only when the
      branch needs something the release branch holds; the squash discards
      the merge commit either way.
      **Never rebase a work item's branch, for any reason.**
      `skills/code-review/orchestration.md` *Orchestrator: the pull request
      opens once the sealer seals* states the rule and its reason.
- [ ] **The milestone `release: X.Y.Z` holds what this release is actually
      carrying, and nothing else.** Every open issue in it that is not
      shipping moves to another milestone now, a planning act that needs no
      code. Left, the release pull request goes red at step 5:
      `release_completeness_check.py` refuses while the milestone claims an
      open issue the release branch does not carry, and names each one, at
      the worst moment to do the planning.

## 2b. Settle what earlier releases left behind

`skills/settle/SKILL.md` *When it runs* says when the settle runs. A release
whose owner has not called the settle skips this step.

```bash
seal settle
seal settle --apply
seal fold
```

The first prints each group of released designs whose rule changes name one
section, in merge order, and every open row of every released record.
Before the first, the session running the settle asks the person whether
any directory besides `seal/` holds decisions to fold, and passes each one
named to the first as `--from <dir>`. Where the first lists a document of
one, the session proposes each document as promote or skip, and the person
marks the rows in a second question, before the session's first edit.
Between the first and the second, the session writes each section as its
group's latest decision, checked against the code, writes each decision the
person marked promote into its section, and closes each open row with what
closed it, asking nobody about either. A named directory is read and never
written (`docs/checks/the-fold.md` *The fold, and what tells it from a
deletion*). The second removes every released work item directory whose
record holds no open row and whose version's published note carries its
entry where the repository's notes are built from the fragments, and names
any it keeps with why. The settle's pull request body names each directory
kept for its note, and the owner repairs that note before a later `--apply`
removes it. `seal fold` then reads the documents the settle wrote, and names
each one past its ceiling as one to split (`skills/settle/SKILL.md` *A
document past its ceiling is split, never trimmed*). The settle's pull
request body states each decision with its grounds and lists the defaults
it took, and the owner reviews it.

`skills/settle/SKILL.md` is the procedure. **A settle is not a work item**:
it opens no directory under `seal/threads/`, its session runs
`seal no-work-item` on the settle's branch before the first edit, and each
of its commits carries the trailer `Seal-Routing: no work item`, the
recorded form of the routing question's `no work item` answer
(`skills/commit-pr-convention/SKILL.md`). It owes an answer for every check
in this repository carrying a population floor over `seal/threads/`.

**Before `seal settle --apply`, the settling session counts, for each released work item
routed through the review chain, the findings, the findings that carry a `regression:`
or `reopens:` line, the findings whose finding block names only paths under
`seal/threads/` on its `location:` line, and the rounds, and posts the four numbers as a
comment on the open `flow-baseline` issue.** `python3 .github/scripts/finding_counts.py`
prints the four as the table the comment carries, one row per such work item. It reads
each round record through `skills/code-review/scripts/chain_check.py#record_findings`,
the reader the pull-request check holds a record to. So a finding is counted once: by
its `### <n>. <symptom>` section that holds a finding block, by that block's
`regression:` or `reopens:` line, and by that block's `location:` line alone. A close
block's `location:` names where the fix went, not where the defect shows, and the count
does not read it. A work item whose record the reader refuses a line of reads `not read`
in its finding cells, and the refusal is printed under the table, because a count that
skipped a refused finding is a wrong number. They are this repository's measure
of #1148, which removed the records' copies of one another. A records-alone count
that does not fall is no verdict. #1148 is measured by this count falling, so a count
that holds level is read as one that rose: it is a row for the judgment
`docs/running/measuring-a-run.md` *A band flags a reading for judgment, and a judgment
decides whether it is worse* asks, because a release's mix of work moves the count as
well as stale copies do. A stale copy is a record that restates a fact another record
holds and was left as it stood when that source changed. The settling session's
comment names the work items whose records-alone findings kept the count up, and
says of each such finding whether it found a stale copy. The count is `worse` only
where stale copies are what kept it up. Where it is, the session files one issue that
names each such stale copy, the record it stood in, and the file the lesson belongs in.
An issue naming that file is where `skills/implement/orchestration.md` *Orchestrator:
where a decision or a lesson is written* writes a lesson whose home no work item in
progress changes. The step is this repository's and ships to no user: the plugin's
settle procedure (`skills/settle/SKILL.md` *The settling session's procedure*) does not
take it, because the reader of the four numbers is this repository's owner and most
installed repositories keep no `flow-baseline` log.
check: tests/github/test_finding_counts.py

**What `seal settle --apply` removed is committed before anything switches that checkout
to another branch.** `--apply` deletes each directory from the working tree and stages
nothing, and `git switch` exits 0 over an unstaged deletion while it restores every
deleted file that differs between the two branches, saying nothing about it. A
comparison with another ref runs in a `git worktree` of that ref.

**Before `seal settle --apply`, the settling session reads the dry
run's *The judgments* and *The judgments earlier settles removed*, and
rewrites a section where the same kind of judgment came back, within
this release or over several, or cost rounds each time it was made.**
*The judgments* holds the orchestrators' rows from every released
`frame/plan.md`. *The judgments earlier settles removed* holds the rows of
every plan an earlier settle removed, read from the history with the
release each shipped in. Both are grouped by the document each row stands
on. The pull request body names each kind that recurred across releases
with the releases it recurred in. The rows leave the tree with their
directories at `--apply`, and the history keeps them for the next settle,
so nothing is kept beside the tree to carry them; `skills/core/SKILL.md` *A judgment
stands on a source document, and is written down with both* says the
guidance improves from that record and not from memory.

## 5. The release pull request

```bash
gh pr create --base main --head release/vX.Y.Z \
  --title "release: X.Y.Z symptoms: <the symptoms the release answers>" --body-file <file>
```

**The orchestrator opens the release pull request once the last pull
request into `release/vX.Y.Z` has merged, and the owner's one required act
at a release is its merge.** The reads below and the boxes of step 6 are
reports that fail nothing. The version moved in the release's first pull
request, so no pull request comes between the last work item and this one.
A release pull request opened earlier takes each later squash merge into
the branch as a push to its head. Its `tests` run then reads a tree the
merged pull request tested on its own merge ref only where nothing else
merged into the branch after that test started, since `main` stays where
the release branch was cut unless a hotfix moves it. Where something did,
the run is the first to read the two together, and the one run after the
last merge reads them together as well. Opened after the last merge, it
runs `tests` once, on the tree the release ships, and what runs only on a
pull request into `main` answers once: `release-report`, and the
`hygiene` workflow's version and milestone steps. The orchestrator reads
that moment from two commands after `git fetch origin`.
`gh pr list --base release/vX.Y.Z --state open` lists no pull request; a
settle's pull request closes no issue, so only this command sees it. And the
release pull request's own milestone check exits 0 and prints its
`M (open in 'release: X.Y.Z')` line, run as
`python3 .github/scripts/release_completeness_check.py` with
`HEAD_BRANCH=release/vX.Y.Z`, `HEAD_SHA=origin/release/vX.Y.Z` and `REPO`
set to what `gh repo view --json nameWithOwner --jq .nameWithOwner`
prints. Exit 0 alone does not read the moment: the script also exits 0
when the branch name is not a release name and when no milestone of that
title exists, and then prints a line saying so in place of the `M` line.
That check fails the release pull request while the milestone claims an
issue the branch does not carry, and names each one. An issue it names
that no branch is building is step 0's milestone box, left undone. Where
it fails for another reason, a patch carrying a `feat:` or a label on an
issue the branch does not carry, its `::error::` line names the repair.
check: tests/github/test_release_completeness_check.py

Press ***Create a merge commit***, never squash: the review records name the
release branch's commits on their `target:` lines, and a squash discards
them.

**Read the release table before the merge.** The pull request's
`tests` run carries it in the `release-report` job's summary, under
*Against vA.B.C*: each agent's preload bytes, the suite's seconds,
each leg's minutes and each document's bytes, beside the same reading
at the last release tag, and under it each test file's priced cases
and seconds at the tag and now. It fails nothing, and no row of it is
a verdict. The table has no band, so a preload or a document that grew
is a row for the judgment `docs/running/measuring-a-run.md` *A band flags a
reading for judgment, and a judgment decides whether it is worse*
asks. The orchestrator writes that weighing in the pull request's
body, and opens an issue only for a row the weighing judges `worse`. A
leg's minutes compare one run with one run and swing on the same code,
so they are read and never acted on alone.
check: tests/github/test_release_report.py tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py

**Each release clears what grew.** The test file rows are a report and never
a ceiling: a heavily exercised module needs the cases it needs. The owner
reads the rows whose seconds or cases grew most since the tag and sweeps each
such module with one `bin/seal mutate` call carrying a mutant per class,
for cases that kill nothing another case does not. The sweep's cuts land in
a work item of the next release with one line per cut case, the shape
`CONTRIBUTING.md` *The test layout* gives.

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

`docs/releasing/branch-and-release.md` *Cutting a release* says why the tag has to
name the release.

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
      The note opens with a header of the release's counts and the theme
      line under it, then the release's pull requests, one fold per
      conventional-commit type under its name and count, and a
      `### 🙌 Thanks to` line for each outside contributor, over the
      fragments folded; where the job log says the pull requests could not
      be listed, the note went out as the theme line and the fragments
      alone, which one `gh release edit` repairs. After the note, the same
      workflow's `seal` job attaches `seal.png` and puts it in the header,
      beside the results the stamp states as badges, where
      `seal/config.md`'s `Release note seal mark` row reads `yes`; under any
      other value it attaches nothing and puts the results in the header
      alone. Where the header still shows the counts as text, the `seal`
      job's log says why on a `::warning::` line: the suite at the tag did
      not pass or its counts could not be read, the icon could not be
      copied, a `gh` call failed, or the header was not in the note as
      generated: edited before the job reached it, already replaced by an
      earlier run of the job, published without one, or the pull requests
      moved between the two lists. A row written with a value other than
      `yes` is named on a `::warning::` line of its own, and the results go
      in without the image. That job never
      fails the release. To seal one by hand, from a checkout at the tag,
      run the suite with the broad gate's recorder loaded
      (`PYTHONPATH="$PWD/skills/verify/scripts/pytest_record"`,
      `PYTEST_ADDOPTS='-p agentic_pytest_record'`, and
      `AGENTIC_RECORD_DIR` and `AGENTIC_RECORD_KEY` naming a directory
      that exists and a key you choose), then run
      `DRY_RUN=1 python3 .github/scripts/release_seal.py` with `TAG`,
      `REPO`, `SUITE_RECORDS` (that directory) and `SUITE_KEY` (that key)
      set; attach the PNG it names, where it names one, with
      `gh release upload`, then apply the note it prints with
      `gh release edit --notes-file`.
- [ ] **The marketplace files and the directory's page have been read**, by
      `python3 .github/scripts/plugin_directory_check.py`. It reads the two marketplace
      files on GitHub and says, per file, whether this plugin has an entry, which commit
      the entry pins, and whether that commit is an ancestor of `main`. **It reports and
      never fails**, for the reason `docs/releasing/branch-and-release.md` *Cutting a
      release* gives. Those files are not the directory,
      the catalog people browse inside Claude, and the directory is readable from
      nowhere a script can reach, so the command ends by saying it was not read and
      printing the address of the page that answers. A portal listing is answered on
      the portal's Submissions page, with its status and the version that is live. It
      picks up each new version from its tracked branch without a resubmission, and a
      version that passes goes live by the listing's publish setting, which by default
      waits for somebody to select Publish (`claude.com/docs/plugins/submit`, *Publish a
      passing version*). A Console listing is answered on the Console page. The
      plugin's listing is a Console listing, by the repository owner's reading of the
      Console page on 2026-10-07, and a Console listing takes no new version until a
      person moves it to the portal (`claude.com/docs/directory/publish`, *Move an
      earlier submission to the developer portal*), so no release reaches the directory
      through it until then. Whether it shows up at all is what a search for the plugin
      inside Claude answers. Neither that search nor the Console page, which sits
      behind the owner's login, is open to a script or a case here: both answers are the
      owner's reading.

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

**The milestone `release: X.Y.Z` is closed once the close-issues run has closed its
issues, by `gh api -X PATCH repos/<owner>/<repo>/milestones/<number> -f state=closed`.**
Nothing else closes it: `.github/scripts/close_issues_on_release.py` closes each issue
and leaves the milestone open with none in it, which reads as a release still in flight.

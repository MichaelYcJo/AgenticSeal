# Design: the release pull request opens after the last work item merges (#1258)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| G1 `docs/release-checklist.md` *5. The release pull request*, lines 106 to 114 at `5f0cf7a7` (read) | The one paragraph that sets the moment: "The orchestrator opens it with the first work item pull request into `release/vX.Y.Z` that finds none open, and leaves it open", followed by "Its milestone check fails while the milestone claims an issue the branch does not carry, by design, and goes green on the push that merges the last one." Both sentences stand on the early moment, and *Rule changes* rewrites the paragraph |
| G2 The class of sentences that state the early moment (executed: `git grep -i` for `finds none open`, `leaves it open`, `first work item`, `release pull request` and `release/v` over `skills/`, `agents/`, `docs/`, `templates/`, `hooks/`, `.github/` and `CONTRIBUTING.md`, `seal/threads/` left out) | G1's paragraph is the only place that says when the release pull request opens. `skills/implement/orchestration.md` and `skills/code-review/orchestration.md` name no such moment, so the issue's *Done when* item for them has nothing to rewrite. The other mentions agree with a late opening: `docs/release-checklist.md` *0. Before starting* ("Left, the release pull request goes red at step 5"), `docs/issues-and-milestones.md` *One thing reads a milestone, and it can stop a release* ("a red release pull request, at the moment the release is being cut"), and `.github/scripts/release_completeness_check.py:7` ("the last moment anybody is looking"). The search is a sample over spellings (contract rule 12). It covers every file that mentions the release pull request or the release branch, and every hit was read |
| G3 `docs/branch-and-release.md`, read whole (read; executed: the G2 search) | It holds no sentence about when the release pull request opens. Its *Cutting a release* says "The day-of list, in the order the steps run, is `docs/release-checklist.md`. This section is the why." The issue says this document "states the same", and the tree does not show that. Writing the moment here as well would give the fact a second source (`skills/core/SKILL.md` *The rule a mechanism is kept against*: "A fact has one source"), so *Rule changes* names no section of this file (`plan.md` *Alternatives considered*, A7) |
| G4 `docs/release-checklist.md` *0. Before starting* (read) | Its first box already asks that every work item of the release is squash-merged into `release/vX.Y.Z`, with CI green at the merging commit, before the release steps start. Its milestone box has the orchestrator move each issue that is not shipping out of the milestone. Opening the release pull request at step 5 after the last merge makes step 5 agree with step 0's first box. The old wording opened it before step 0 could hold |
| G5 The policy in force (executed: `grep -n 'file: docs/(release-checklist\|branch-and-release)\.md'` over the 15 `seal/threads/*/frame/design.md`) | Only `1793521559-a-finding-is-counted-once` changes `docs/release-checklist.md`, at *2b. Settle what earlier releases left behind*. No unsettled design touches *5. The release pull request* or `docs/branch-and-release.md`, so the `from` below quotes the section as it stands at the base |
| G6 Where the early moment came from (executed: `git log -S 'finds none open'` names `53f21b54`, the 0.24.x settle #1182; `git show 53f21b54^:seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/frame/questions.md`) | Work item `1793226631` (#1144) asked the moment as Q1, a row for a person. Its options were (a) open with the first work item pull request and leave it open, (b) open with the pull request of the last work item, and (c) a session the owner starts after the last merge. It took (a) as the default, with the cost "the release pull request's CI runs on every merge into the branch". The settle wrote (a). #1258 is the owner reopening that default with a measurement (G7), so the decision is made again here and not argued from the start. The race Q1 found in (b), two last work items in flight that each see the other, does not arise here: the moment is read after the merges and not at a work item's pull request |
| G7 0.27.2's release pull request #1251 (executed: `gh run list --branch release/v0.27.2`; `gh run view 41307757654 --json jobs`; `gh api repos/MichaelYcJo/AgenticSeal/actions/runs/<id>/jobs --paginate` summing `completed_at - started_at`; `gh pr view` for #1248, #1250, #1251, #1252, #1253, #1257 and #1261) | #1251 opened at 09:33 on 2026-11-01, after #1248 had merged. `tests` ran six times on it: at the opening (`ad5246ce`), cancelled by the next push (`161a42aa`), then `a8269d90`, `94b03636` and `569780ef`, and last on `783a7fe8`, the merge of #1261 and the tree that shipped. Every run holds 13 jobs. The summed job minutes, unweighted by platform, are 16.6, 11.1, 16.2, 14.3 and 15.1 for the five runs before the last, and 15.5 for the last. The issue's "about 50 runner-minutes" per run comes from #947's per-leg medians, a different method that was not re-run here. The `hygiene` workflow's `release` job failed on every run before the last, the milestone reading red by design, and passed on the last. None of the five earlier `tests` runs failed |
| G8 `.github/workflows/test.yml` (read: `on:`, `concurrency:`, the `release-report` job) and `.github/workflows/hygiene.yml` (read: the milestone step) | `tests` runs on GitHub's default `pull_request` events, and a newer push cancels the run in progress. `release-report` runs only when the base is `main`. `hygiene` has one job, `release`, whose version step and milestone step exit 0 on any other base. So these answer only on the release pull request, and only its last run reads the tree that ships |
| G9 Reading the moment (executed: `python3 -I .github/scripts/release_completeness_check.py` in a `git clone --no-local` under the scratchpad, with `HEAD_BRANCH=release/v0.27.3`, `HEAD_SHA=origin/release/v0.27.3` and `BASE=origin/main`) | With `REPO=MichaelYcJo/AgenticSeal` it exits 1 and names the seven open issues of `release: 0.27.3` that the branch does not carry. So the release pull request's own milestone check, run by hand, reads whether the last work item has merged. With `REPO=MichaelYcJo/SpecSeal`, the name the repository had before its rename, it exits 0 and reads M as empty. `gh issue list --repo MichaelYcJo/SpecSeal --milestone 'release: 0.27.3' --state open` answers 0 issues with exit 0, while the milestones read follows the redirect and finds the title. So the step reads `REPO` from `gh repo view`. That the script passes on a redirected name is a defect of its own, outside this scope (*Scope*, out) |
| G10 What the milestone check cannot see (read: #1182's body, a settle into `release/v0.25.0` that closes no issue; executed: `gh pr list --base release/v0.27.3 --state all`, none yet) | A settle is no work item and closes no milestone issue, so the milestone check passes while a settle's pull request into the release branch is still open. `gh pr list --base release/vX.Y.Z --state open` sees it. The moment is therefore read from both commands |
| G11 The step's `check:` line, `tests/github/test_release_completeness_check.py` (read: its docstring and `Test_main`'s purpose) | The cases read the script's refusal of an issue the milestone claims and the branch does not carry, and the inputs its run is handed. The new paragraph still states that refusal and now has the orchestrator run the script, so the line still names cases that read what the step says, and it stays unchanged |
| G12 `seal/follow-up.md` and the latest Release's `### Process changes` (executed: `grep` of the follow-up list; `gh release view --json body`) | No follow-up row is about the release pull request. The one process change, #1222's wait on a pull request's checks, is unrelated |

## Scope

In:

1. *5. The release pull request* in `docs/release-checklist.md` says the orchestrator opens the release pull request once the last pull request into `release/vX.Y.Z` has merged. It also says why: an early run mostly re-tests a tree its own pull request already tested, and the one run after the last merge reads every tree the early runs would have read first, the tree that ships. It names the two commands that read the moment, G9's milestone check and G10's open pull request list. It no longer says that the milestone check is red by design. The `check:` line stays (G11). This item is written as the `change` in *Rule changes*, and the settle after the release writes it into `docs/`.
2. The work item's `changelog.md`: one entry, and one `### Process changes` row in the shape of `templates/records/process.md`, because the change moves an act of the way of working.
3. No other file in the tree changes, because no other sentence states the early moment (G2, G3).

Out:

- `docs/branch-and-release.md`: no rule change (G3; `plan.md` A7).
- `.github/workflows/test.yml`: no gate that holds `tests` back on a release pull request. The issue weighed it and did not take it (`plan.md` A3).
- #1263's wording of the same section and its change to `docs/measuring-a-run.md`. #1263 is built after this work item merges and rewrites the section as it then stands.
- `.github/scripts/release_completeness_check.py` passing on a redirected repository name (G9). The orchestrator files it. This work only reads the name from `gh repo view`.
- Moving `.claude-plugin/plugin.json` to 0.27.3. If this is the first pull request into the release branch, the move is the orchestrator's, in the commit that adds the changelog fragment (`docs/branch-and-release.md` *Cutting a release*).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A work item pull request opens mid-release | Given a release whose milestone still holds open work, when an orchestrator opens a work item pull request into `release/vX.Y.Z` and finds no release pull request open, then it opens none | No case can run an orchestrator's act. The proofer reads the settled text of *5. The release pull request* at review, and it states no such act |
| S2 The last pull request into the release branch merges | Given `gh pr list --base release/vX.Y.Z --state open` lists none, and the milestone check run by hand exits 0 and prints its `M` line, when the orchestrator works the release down the checklist, then it opens the release pull request, and `tests` runs on it once for the tree that ships | After 0.27.3's release, `gh run list --branch release/v0.27.3` lists one `tests` run for each push to the release pull request's head, and no `pull_request` run before the last merge. That is `questions.md` Q1 |
| S3 The milestone check names an issue | Given the milestone claims an issue the branch does not carry, when the orchestrator runs the check by hand, then it exits 1 and names each issue. An issue that no branch is building is step 0's milestone box, left undone | `tests/github/test_release_completeness_check.py` (the step's `check:` line) |
| S4 The rule change reads at the pull request and at the settle | Given this design, when `skills/settle/scripts/rule_changes.py` parses its `## Rule changes`, then it yields one `change` and no refusal, and the `from` stands in the section at the base with whitespace collapsed | Executed at framing (`plan.md` *Technical context*). `chain-check` at the pull request, and the settle's dry run |

## Data & interfaces

None. No schema, no script and no workflow changes. The step calls `.github/scripts/release_completeness_check.py` with the inputs its `main()` already reads (`HEAD_BRANCH`, `HEAD_SHA`, `REPO`, and `BASE` defaulting to `origin/main`), as `hygiene.yml` hands them in CI.

## Rule changes

- change
  file: docs/release-checklist.md
  section: 5. The release pull request
  from: **The orchestrator opens the release pull request, and the owner's one
    required act at a release is its merge.** The reads below and the boxes of
    step 6 are reports that fail nothing. The version moved in the release's
    first pull request, so no pull request comes between the last work item and
    this one. The orchestrator opens it with the first work item pull request
    into `release/vX.Y.Z` that finds none open, and leaves it open. Its milestone
    check fails while the milestone claims an issue the branch does not carry,
    by design, and goes green on the push that merges the last one.
  to: **The orchestrator opens the release pull request once the last pull
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
    `hygiene` workflow's version and milestone steps.
    The orchestrator reads that moment from two commands after
    `git fetch origin`. `gh pr list --base release/vX.Y.Z --state open` lists no
    pull request; a settle's pull request closes no issue, so only this command
    sees it. And the release pull request's own milestone check exits 0 and
    prints its `M (open in 'release: X.Y.Z')` line, run as
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

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The sentence that opens the release pull request with the first work item pull request and leaves it open | `docs/release-checklist.md` *5. The release pull request* | Replaced by the `change` above. The new bold sentence and the two commands state the moment |
| The sentence that the milestone check fails by design until the last merge | `docs/release-checklist.md` *5. The release pull request* | It can go, because the release pull request now opens when that check already reads green. A red milestone check at the opening is now step 0 left undone, which the new last sentence says |
| Outside the tree: each release's `tests` runs on the release pull request before its last merge, five of six on 0.27.2's (G7), and the `hygiene` `release` job's red on each of them | the release pull request's CI | The cause goes: the pull request is not open while work still merges. This design adds no mechanism (no gate, check, hook, CI step, label or mark), so `skills/core/SKILL.md` *The rule a mechanism is kept against* asks nothing to go in return. The step reads its moment with a script the release pull request already runs |

Framed 2026-11-01 by framer, before the build.

# Implementation Plan: 1795849901-number-read-at-cut

## Technical context

The tree as read at `9d7a8fe2`.

- `.github/scripts/release_completeness_check.py` (397 lines) holds the one
  exact reading of a release's subjects: `merge_base` and `subjects_since`
  at lines 111 and 134, and `FEAT`, `first_word_is_feat` and `judge_feat`
  from line 284 to 343. `main`, from line 346, reads the version from
  `HEAD_BRANCH` through `label_merged_on_release_branch.py#version_of`, and
  then the milestone through `milestone_titles` and `open_in_milestone`,
  lines 144 to 196. `judge`, from line 228, is pure and holds the `M`, `D`
  and `L` arms. The version comes
  from a name today, and from `plugin.json` at two commits after this
  work, read as `hygiene.yml`'s version step already reads it, with
  `git show "$base:.claude-plugin/plugin.json"`.
- `.github/scripts/label_merged_on_release_branch.py` (257 lines) holds the
  name mapping, lines 61 to 97, and the label's description from line 115,
  which a case holds under GitHub's 100-character limit.
  `release_completeness_check.py` loads it as `signal`, and so does the
  closer's test.
- `.github/scripts/close_issues_on_release.py#spend_label`, lines 215 to
  237, spends one label, `SPENT_ON_CLOSE`, at three call sites in `main`.
  `merged: next` is a second label spent at the same three sites.
- `.github/scripts/publish_release_note.py` (1069 lines): `merged_pulls`
  from line 606, `release_pull_body` from line 345, `milestone_description`
  and `theme_of` from lines 475 and 507, and `main` from line 983. `previous_tag`, lines 220 to 233, gives the range's
  start. `.github/scripts/release_mark.py#main` calls `merged_pulls` at line
  530.
- `.github/workflows/hygiene.yml`, the `release` job: the version step,
  lines 70 to 114, and the milestone step, lines 123 to 163.
- The contributor surfaces: `CONTRIBUTING.md` lines 3 to 37 and the table at
  lines 70 to 77, `.github/PULL_REQUEST_TEMPLATE.md`'s opening comment,
  lines 1 to 16, `README.md` line 474 and `README.ko.md` line 470.

**Failure scenario of the chosen approach, six months on.** A person
merges a fix straight into `main`, as #523 was on 2026-09-23, and moves its
version there. The next release pull request from `release/next` then
conflicts on `plugin.json`, and no squash into `release/next` can resolve
it (design G5 (d)). The rule this design writes, as the default of
`frame/questions.md` Q2, is that nothing but the release pull request
reaches `main`, and nothing enforces it beyond the
`main` ruleset's required checks, which such a pull request can pass. The
repair then is to cut `release/next` again from `main`, and deleting it
reaches every pull request open into it, which GitHub retargets or closes
by rules this frame did not measure: each is based on the new branch again
by hand. A second scenario: a `feat:` squashes into `release/next`
after the version pull request moved a patch. The release check goes red at
that push, exactly, and a second version pull request is the repair, one
more wait.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. `release/next` heads every release pull request, cut from `main` once; the last pull request into it moves the version to the number read | the two scenarios above | chosen: design G5 (a) merges clean release after release, and the range from the merge base holds only that release's subjects, so the branch is never cut again; the cost is one pull request's wait, and none where the release settles |
| A2. A cut branch outside every ruleset, made from `release/next` at the cut with a direct commit that moves the version, heads the release pull request; `release/next` never moves the version | design G5 (b): the second release conflicts on `plugin.json`, since `release/next` keeps the version it was cut with while `main` moves; merging `main` into each cut branch would repair that and leave `release/next` holding a stale version and none of `main`'s merges, which every session in the tree then reads as the running version | rejected: it saves the version pull request's wait and costs a conflict or a stale integration branch every release |
| A3. Keep a numbered branch, read the number at the cut, and cut the branch again under it | every work item's branch is cut from a branch that is later deleted, so GitHub moves or closes each open pull request into it; design G5 (c) shows two numbered branches cut side by side conflict on `plugin.json` | rejected: #1671 asks for an integration branch with no number, and the re-cut is the churn the issue removes |
| A4. Open `release: X.Y.Z` at the cut and move the release's issues into it, so the milestone check keeps an `M` to read | the milestone is written from what merged, so `M` equals `D` by construction and the check it serves catches nothing; each issue leaves its goal milestone | rejected: a mechanism with nothing to catch (G1). The structure kept by A1 instead is `D` and `L`, whose premise holds: an issue's state moves only when `main` moves (`close-issues-on-release.yml`'s trigger, read), so *is this in yet* is still asked for a release's length |
| A5. The orchestrator proposes the number and the owner approves it, as owlery#279 does | a person asked at every release, for a judgment each pull request's prefix already made | rejected: G2, and #1671 rejects it by name |
| A6. Keep the hotfix route into `main` beside `release/next` | design G5 (d): the next release conflicts on `plugin.json`, and no pull request into `release/next` can record `main` as a parent | rejected as the default of `frame/questions.md` Q2, a person's row, since #1671 does not ask for the removal and the rulesets that force it are the owner's: an urgent fix squashes into `release/next` and the release is cut then. `release/next` holds only cleared work, so cutting early ships nothing unfinished, and the route has gone unused since 2026-09-23 (G6). Q2 holds the two shapes that keep a route, and what each costs |
| A7. `merged:` between the squash and the cut: `merged: next`, spent at the close | none found: the label names only what is in and not yet shipped, and an issue the closer misses keeps it and is named by the next release's `L \ D` | chosen. Against it: relabel to `merged: X.Y.Z` at the close, which makes the closer add labels, the act its docstring gives to the signal alone, to keep a record the close and the tag already hold (`docs/releasing/issues-and-milestones.md` *Reconstructing a missing milestone*); and no label until the cut, which leaves *is this in yet* unanswered for a release's length, the gap #359 closed |
| A8. Drop the `L` and `D` comparison with the milestone arms | a label naming a release an issue is not in goes unread until someone queries it | rejected: the comparison reads the branch and the label alone, both still standing, and `L \ D` stays the one failing direction whose repair is one command |
| A9. The work item judged last carries the move, as the first carries it today | the number is known only once every item has merged, so the item that carries it must merge last, and one merged after it moves the number again with no round reading the move | rejected: a pull request at the cut reads the number from the finished range |
| A10. Rename `release_completeness_check.py`, and its rule markers, to what it now reads | until the settle, `docs/releasing/` names the old path and the old marker in check lines and prose, and a check line naming a missing file or an uncarried marker fails `agentic rules --check` | rejected: the name stays, its docstring's opening says what it reads, and the marker `a-patch-carries-no-feat` still states a truth of the new reading (design G14) |
| A11. Replace the label script with a step of `release_completeness_check.py` that labels at the release pull request | a `pull_request` run holds a read-only token (`hygiene.yml`'s `permissions:`, read), and the label would appear only once the release is cut | rejected: the push to `release/next` is where a write token and the moment both are |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1, 2, 3 and 4, with item 9 for their cases | `bin/test tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py tests/github/test_close_issues_on_release.py tests/github/test_publish_release_note.py tests/github/test_roll_flow_measurement_issue.py tests/github/test_issue_claims_check.py tests/lib/test_closing.py tests/text tests/behaviour -q`, the one suite those files fall in; and `git grep --no-color --no-line-number -P 'merged: \{\|merged: X\.Y\.Z\|milestone_title\|open_in_milestone\|HEAD_BRANCH' -- . ':!agentory/threads/1795849901-number-read-at-cut' \| LC_ALL=C sort \| diff - agentory/threads/1795849901-number-read-at-cut/frame/keep-1.txt` prints nothing | 0203c27a |
| 2 | *Scope* items 5 and 6, with item 9 for their cases | `bin/test tests/github/test_publish_release_note.py tests/github/test_release_mark.py tests/github/test_tag_release.py tests/github/test_close_issues_on_release.py tests/lib/test_console.py tests/skills/test_settle.py tests/text tests/behaviour -q`; and `git grep --no-color --no-line-number -P 'MILESTONE_TITLE\|milestone_description\|PURPOSE_LABEL\|release/v\{\|release/v<version>' -- . ':!agentory/threads/1795849901-number-read-at-cut' \| LC_ALL=C sort \| diff - agentory/threads/1795849901-number-read-at-cut/frame/keep-2.txt` prints nothing | 8ad177a7 |
| 3 | *Scope* items 7, 8 and 10, with item 9 for their cases, and the work item's `changelog.md` | `bin/test tests/github/test_issue_claims_check.py tests/text tests/behaviour -q`; and `git grep --no-color --no-line-number -P 'release/v' -- . ':!agentory/threads/1795849901-number-read-at-cut' \| LC_ALL=C sort \| diff - agentory/threads/1795849901-number-read-at-cut/frame/keep-3.txt` prints nothing | ccd4fd68 |

`bin/test` is the one runner `CONTRIBUTING.md` *Running the checks* names
for `tests/`, and `tests/text` and `tests/behaviour` hold the tree-wide
files that its *The test layout* names. No phase changes an eval case
under `evals/`. A cell's search is written with `\|` for the table; typed,
each `\|` is a `|`.

## Overlap with the release

The spawn of 2026-11-28 names the work items of two releases built side by
side and shipping before this one: #1648 and #1593, and #1631 with #1583 as
one work item. Read at 2026-11-28: `fix/1648-submodule-pointer-in-typed-diffs`
at `12249764` changes `agents/inspector.md`, `agents/proofer.md`,
`tests/behaviour/test_the_inspector_inspects.py`,
`tests/behaviour/test_the_proofer_reads_a_merge_round.py` and
`.claude-plugin/plugin.json`; `fix/1593-body-decision-with-its-question` at
`92b2f13f` and `feat/1583-merge-owes-what-it-can-catch` at `0148aa63` hold
their `routing.md` alone, and #1583's routes the rewrite of the paragraph of
`skills/code-review/orchestration.md` on merging the base. This work does
not change that paragraph.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1648 | `.claude-plugin/plugin.json`'s version line | #1648 | its release ships first, so this branch merges `main` after it, and the conflict resolves to this release's version in that merge |
| #1631 and #1583 | `.claude-plugin/plugin.json`'s version line; and `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* and `docs/releasing/release-checklist.md` *Before starting*, where that item's frame states rule changes there | #1583 | its release ships first. The rule changes here quote sentences of those sections that its routing does not name, so the settle applies both in merge order; where its frame quotes one of the same sentences, this design's `from` is history at the settle, and the settling session writes the section to the later decision |
| #1593 | `.claude-plugin/plugin.json` only where it carries a move, and its routing says #1648 does | #1593 | its release ships first |

## Operational impact

- **This pull request carries its release's version move**, under the rule
  its release branch was cut with (`routing.md`), in phase 3's commit that
  adds `changelog.md`. The value is the one the spawn of 2026-11-28
  assigned, `0.43.0`, and phase 3 confirms it as the next minor of
  `git show origin/main:.claude-plugin/plugin.json` after the merge of
  `main` that brings the previous release, and with the changed
  `release_completeness_check.py` run by hand against the branch.
- **The release pull request of this release is the first the new check
  judges.** A `pull_request` run takes its workflow from the merge ref,
  which holds this change (GitHub's documented behaviour, unmeasured here;
  the release pull request's own `hygiene` run reads it), so the release
  step reads the number from the release's range and holds the move to it. The squash of this pull request
  runs the new label script, which labels only `release/next`, so #1671
  carries no `merged:` label and the check's `D \ L` line reports it and
  passes.
- **That release pull request merges clean only where its release branch
  descends from `main`'s merge of the release before it** (design G5 (c)).
  Its branch and the earlier releases' were cut from one commit, and the
  `release` ruleset takes squashes alone, so the orchestrator cuts this
  release's branch again from `main` once the release before it has
  merged, before this pull request opens (the ruleset holds no `deletion`
  rule, design G4), and this branch then merges `main`.
- **After that release merges, the orchestrator's tracker acts, in order:**
  cut `release/next` from `main`'s release merge commit; base each open pull
  request into a `release/v…` branch on `release/next` with
  `gh pr edit --base release/next`; close the release's own milestone as
  the checklist it shipped under says; and rename by its goal each open
  `release:` milestone whose release has not been cut. At G12 the open
  numbered milestones were shipped releases and the three releases built
  now, each of which ships under its number before or with this change,
  so their titles state shipped releases and none is renamed. The old
  numbered branches stay. None of these acts is a file.
- No environment variable, dependency or migration. An installed plugin
  meets one change, *Scope* item 8's sentence in
  `skills/commit-pr-convention/SKILL.md`; the scripts and workflows run in
  this repository alone and do not ship to a connected repository
  (`templates/setup/hygiene.yml` clones a tag, design G15).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-28 | Which prefix the pull request's title takes: `feat:`. | A contributor now bases every pull request on `release/next` instead of a numbered branch, and the release check reads the number instead of refusing one, so whoever works on a later change meets a new branch and a new check. | `skills/commit-pr-convention/SKILL.md`, its prefix table |
| 2026-11-28 | Which route the statements phase 3 named outside the frame's rule changes take: the framer folds them into `## Rule changes` and the frame before round 1. | `docs/releasing/release-checklist.md:150` and `:156` contradict Q2's answer and phase 1's check, and no operation of `## Rule changes` reaches them, so the settle would leave them standing. | `skills/implement/orchestration.md` *A decision made after the frame is committed is folded* |

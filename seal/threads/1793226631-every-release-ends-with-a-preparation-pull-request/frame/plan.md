# Implementation Plan: 1793226631-every-release-ends-with-a-preparation-pull-request

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned.

## Summary

A release ends today with a preparation pull request into the release
branch and a tag the owner pushes by hand. This work removes both. The
version moves in the release's first pull request, a work item that changes
the way of working writes its own process row in its fragment, and the merge
to `main` creates the `vX.Y.Z` tag and publishes the note in one workflow
run. What is left at the end of a release is the release pull request, which
the orchestrator opens, and the owner's merge of it. 0.24.0 is the first
release cut this way: this work item's pull request moves its version.

## Technical context

- `.github/workflows/publish-release.yml:35-37` fires on `push: tags: ['v*']`
  only, and its header comment (`:3-19`) says nothing in CI creates a tag.
  Its `publish` job (`:48-71`) checks out with `fetch-depth: 0` and runs
  `publish_release_note.py` with `TAG: ${{ github.ref_name }}`; its `seal`
  job (`:73-135`) reads `TAG` the same way and checks out the default ref.
  On a push to `main`, `github.ref_name` is `main`, so both jobs take the tag
  from the new step's output instead.
- `.github/scripts/publish_release_note.py`, after #1053: `previous_tag`
  (`:168-180`), `commit_range` (`:183-186`), `fragments` (`:189-236`) and
  `section` (`:239-242`); `main` (`:643-700`) reads `TAG` and `REPO`, leaves
  an existing release as it is (`:671-678`) and writes `created`. Nothing in
  it needs the tag to have been pushed by a person: it needs the tag in the
  checkout, which `git tag` in the same job gives.
- `.github/workflows/hygiene.yml:70-108`, the step *a change to what ships
  must move the version*, runs only when the base is `main` and compares the
  base's `plugin.json` with the merge ref's. It keeps holding a release whose
  first pull request did not move the version.
- The `release` ruleset takes no direct push and has no bypass actor, and no
  ruleset targets a tag (executed, `gh api .../rulesets`, 2026-10-29). The
  repository's default workflow token is read-only (executed,
  `gh api .../actions/permissions/workflow`), and `publish-release.yml`
  declares `contents: write`, which creating a ref through the API needs.
- `seal/process/` holds `0.22.4.md`, `0.23.0.md` and `0.23.1.md`, all three
  at the tag `v0.23.1` (executed, `git ls-tree`). Their readers are
  `agents/framer.md:64-67`, `.github/scripts/release_report.py:54`,
  `tests/censuses.py:1056` and the cases in `## Removes`.

**The chosen approach's failure scenario, six months on.** A release's first
work item is opened by a session that does not move the version, so every
pull request into the branch merges with the old one. Nothing says so until
the release pull request, whose version step goes red. The repair is one
more pull request into the release branch, which is the preparation pull
request this work removes, on that one release. `frame/questions.md` Q3 asks
whether a check should catch it at the first pull request instead.

A second one: GitHub refuses the tag creation (a ruleset on tags added
later, or the token's scope narrowed). The tag step exits 1 and the run is
red, so the release is visibly untagged; a tag pushed by hand still fires
the same workflow and publishes.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the preparation pull request and the hand-pushed tag | Every release keeps two waits at its end: the preparation pull request's CI and squash, then the release pull request's CI, then a person's tag push. The owner measured the cost on 2026-10-28 (issue #1117) | Rejected: the issue exists to remove it |
| A workflow commits the version to the release branch at the end, through a bypass actor on the `release` ruleset (the owner's 2026-09-02 variant) | Needs a ruleset change only the owner can make, and a bypass the rule *there are no bypass actors: the rule applies to the owner too* (`docs/branch-and-release.md`) gives up | Rejected: the owner chose on 2026-10-28 to need no bypass, and the design needs zero owner commands |
| Replace the `release` ruleset rather than keep it, so a workflow may push to a release branch | A release branch then takes an unreviewed commit from anything holding the token, which is what the squash-only, pull-request-only rule exists to stop | Rejected. The premise that keeps it is checked: the ruleset has no bypass actor and targets only `refs/heads/release/**/*` (executed), so it costs this design nothing once the version moves at the start |
| The version moves in the release's first pull request (chosen) | A first pull request that forgets it leaves the release red at its end, repaired by one pull request (*Technical context*) | Chosen: the version is known at the cut, from the milestone, and nobody installs from a release branch |
| Tag and publish from a separate workflow file on the push to `main` that repeats the publish and seal steps | Two copies of the publish and seal steps, which drift | Rejected: one fact, one source |
| Push the tag with a token that does start workflows (a personal access token or an app), so the existing tag trigger fires | Needs a secret the owner creates and rotates, an owner command once and again at each expiry | Rejected: zero owner commands |
| A separate `tag` job that the `publish` job needs | Three jobs, and the `publish` job must fetch a tag created after another job's checkout; the case's pin that `publish` has no `needs` goes | Rejected for a step inside `publish` that creates the tag remotely and in its own checkout |
| The issue's decision alone, "version moved and no tag yet, and nothing otherwise" | A re-run of the whole workflow after a failed note step finds the tag it created and publishes nothing, so the release stays without a note until someone runs the script by hand | Rejected for one more arm: where the tag already names the pushed commit, the step passes it on and creates nothing. The note step's own rule, never republish, keeps that arm safe |
| Keep `seal/process/` as history and stop writing to it | Two homes for process rows, and the framer's read of "the highest version's archive" goes stale at 0.23.1 for ever | Rejected: history goes to git, and `v0.23.1` holds all three files |
| Fold the three archives into their published notes | Edits three published notes, which `publish_release_note.py` never does; the owner declined editing published notes for #1053 | Rejected |
| Leave the process rows inside each fragment, folded with it | A reader of the note, the framer among them, has to open every fragment to find them | Rejected for one table lifted by `section` |
| Give `release_body` a parameter for the process table | Changes the signature `tests/github/test_release_seal.py#note` calls, for a table `section` can place itself | Rejected: `section` is the one renderer #1053 left for this |
| A hygiene step that refuses a pull request into `release/vX.Y.Z` whose tree does not name `X.Y.Z` | Moves the count sentence in `skills/verify/orchestration.md`, which #1111 owns, and the two branches conflict | Deferred to `frame/questions.md` Q3; the release pull request's version step holds meanwhile |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The merge to `main` tags and publishes: `.github/scripts/tag_release.py` and `tests/github/test_tag_release.py` (S1 to S7), `publish-release.yml`'s trigger, tag step and `seal` wiring (S8), and the workflow's, the script's and the three test modules' accounts of the tag push (`## Removes`) | `bin/test tests/github/test_tag_release.py tests/behaviour/test_a_release_publishes_its_note.py tests/github/test_publish_release_note.py tests/github/test_release_seal.py -q`; each new case and the rewritten S8 case seen red, against no script and against the workflow at `4134055a` | 9a5d05c1 |
| 2 | Process rows: `section` lifts them (S9, S10), `templates/records/process.md` reshaped, `seal/process/` removed with every reader `## Removes` lists for it, `agents/framer.md` step 4 re-pointed | `bin/test tests/github/test_publish_release_note.py tests/github/test_release_report.py tests/test_censuses.py tests/text/test_a_record_carries_no_comment.py -q`; S9 seen red against `section` at `4134055a` | |
| 3 | The version at the start, and the rest of the preparation's readers: `PREPARATION_RE` and its case, `skills/implement/orchestration.md:526-533`, `skills/settle/SKILL.md:176`, the roll's docstring, and the release hygiene docstrings and refusal message with its pin | `bin/test tests/behaviour/test_release_hygiene.py tests/github/test_publish_release_note.py tests/github/test_roll_flow_measurement_issue.py -q`; the refusal pin seen red against the old message; S11's grep run at the phase's close; `bin/seal rules --check` exit code read directly (S12) | |

## Operational impact

- **No new secret, permission, ruleset or dependency.** The workflow keeps
  `contents: write` alone.
- **The new workflow first runs at 0.24.0's merge into `main`**, because a
  push runs the workflow file of the commit it pushed. Until then the old
  tag-only workflow is what `main` holds.
- **What the orchestrator does for this work item, outside the phases.** In
  the commit that adds this work item's `changelog.md`, it moves
  `.claude-plugin/plugin.json` to `0.24.0` and ends the fragment with a
  `### Process changes` table: one row for this work item, and one for each
  of `f15b3f99`, `fdfb20d5`, `5287dd42`, `7da1a77e`, `c825fd2c` and
  `822d75bb` that changed the way of working (`frame/design.md` *Scope*
  item 6). It opens the release pull request, `release/v0.24.0` into `main`,
  with this work item's pull request, unless `frame/questions.md` Q1 is
  answered otherwise.
- **What the owner does at 0.24.0.** He squash-merges this pull request, as
  he does every work item's, and merges the release pull request with
  *Create a merge commit*. The tag, the note and the seal follow from that
  merge. `frame/questions.md` Q2 names the steps the checklist still gives
  him that this work does not touch.
- **If the tag step fails at 0.24.0's merge**, the run is red and names the
  refusal. The release is on `main` and untagged; `frame/questions.md` Q4 is
  the measurement and names who reads it.

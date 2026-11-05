# Review round 1: 1793843890-the-directory-tracks-a-dist-branch

```seal
target: d1431e49 against release/v0.32.3
```

The diff read is `git diff 9dd67e2a d1431e49`, the merge base with `release/v0.32.3`. The spawn prompt gave `origin/release/v0.32.3` as `9dd67e2a` with #1375 unmerged. The remote-tracking ref in the worktree names `2b72f892`, which is #1375 merged (#1377). `git merge-tree --write-tree HEAD origin/release/v0.32.3` exits 0, so the branch merges onto the moved base without a conflict (executed). This is round 1, so no earlier round carries a coordinate or a close. Every fact below was established this round.

## Findings

### 1. The `dist` job pushes `.github/workflows/` with the workflow's own token, which GitHub refuses, so the release's push to `dist` fails

```seal
severity: must
location: `.gitattributes:12-16`, `.github/workflows/publish-release.yml:176-197`, `.github/scripts/dist_branch.py:157`, `seal/threads/1793843890-the-directory-tracks-a-dist-branch/frame/design.md:59`, `seal/threads/1793843890-the-directory-tracks-a-dist-branch/frame/design.md:82`, `seal/threads/1793843890-the-directory-tracks-a-dist-branch/changelog.md:3`
evidence: executed `DRY_RUN=1 TAG=vprobe python3 .github/scripts/dist_branch.py` in the round's clone with `vprobe` at d1431e49, then `git ls-tree -r --name-only` of the tree it printed; read `.github/workflows/publish-release.yml:176-197`, `.github/scripts/dist_branch.py:157`, and GitHub Community discussion 35410
```

Why it matters: the `dist` job checks out with the default persisted credentials, which are the workflow's `GITHUB_TOKEN`, and `dist_branch.py:157` pushes with them. Every commit it pushes carries the tag's `.github/workflows/`. The tree the script built for HEAD holds 187 files, and `close-issues-on-release.yml`, `hygiene.yml`, `label-merged-on-release-branch.yml`, `publish-release.yml` and `test.yml` are among them (executed). GitHub refuses a push that creates or updates a file under `.github/workflows/` unless the token has the `workflows` permission. The refusal reads "refusing to allow a GitHub App to create or update workflow `.github/workflows/<file>` without `workflows` permission". The `GITHUB_TOKEN` cannot be granted that permission: the `permissions:` block has no `workflows` key, and `contents: write` does not include it ([GitHub Community discussion 35410](https://github.com/orgs/community/discussions/35410), read; a web search listed further reports of the same refusal, which this round did not open).

v0.32.3's run makes `dist` as a commit with no parent, so the push creates every workflow file. Each later release whose tag changes a workflow file updates one, and this release changes two. The job has no `continue-on-error` (`publish-release.yml:176-197`), so the release run goes red and `dist` is never created. The directory then has nothing to track, which defeats the purpose of the work item.

No case can see this. `tests/github/test_dist_branch.py` pushes to a bare local repository, and the workflow-text case reads YAML. `gaps.md` *Not verified* names "the push that creates `dist` under the workflow's token" and sends it to the v0.32.3 publish run. That run is the release itself, and GitHub's documented rule already answers the question. Whether GitHub applies the refusal to a commit with no parent whose blobs `main` already holds is the one point no command here could run, and `## Not judged` carries it. Even if that first commit got through, the refusal still applies to every later release that changes a workflow file.

The repair that stays inside the frame's mechanism is a sixth `export-ignore` line. Nothing the plugin runs reads its own `.github/workflows/`. `skills/verify/scripts/deferral_check.py#workflow_files` and `skills/verify/scripts/broad_gate.py#WORKFLOW` both join the path to the user's repository root (read). The census's two archive cases still pass with the line added. A probe in the round's clone added `/.github/workflows/ export-ignore`, and `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -k what_the_archive_holds` ended 2 passed, exit 0 (executed; the line was then removed). The other repair is a token that holds `workflows`: a GitHub App token, or a personal access token, stored as a secret. That needs a secret only the owner can create, and the run was routed `Automation` `yes`. The repair departs from `frame/design.md:59`, which puts `.github/workflows/` *Out* because "None raised a finding in the form". The departure needs a reason in the frame, and the orchestrator owns that change.

```gitattributes
/tests/ export-ignore
/evals/ export-ignore
/seal/ export-ignore
/.test_durations export-ignore
/CLAUDE.md export-ignore
# The workflow's own token cannot create or update a file here, so a `dist`
# commit holding these would be refused at the push, and the directory
# runs none of them.
/.github/workflows/ export-ignore
```

The snippet does not reach every statement of the five paths. The fix pass or the orchestrator also owes these changes. The design's `.gitattributes` item (`frame/design.md:82`, "Five lines follow") becomes six lines. The *Out* bullet at `frame/design.md:59` drops `.github/workflows/`. The changelog fragment's list of marked paths (`changelog.md:3`) gains the new path. So does the plan's *Operational impact* line on GitHub's source archives (`frame/plan.md:59`). The frame's *Grounding* row that lists the archive's top-level entries stays as it is, since its coordinates are dated to `efd8edec`.

```seal
verdict: fixed 60b917be
answer: `.gitattributes` marks `/.github/workflows/ export-ignore` as its sixth line, and its comment says why the workflows leave. The paste-ready snippet was read against `frame/design.md` *Scope* 1 and *Out* as folded at 5e0fa2c5 and taken with the comment worded into the file's existing paragraph. `tests/behaviour/test_a_cited_section_stands_in_its_file.py#test_this_repository_s_archive_holds_no_workflow_file` (A7, moved there at 5124a6d9) reads this repository's archive with the census's `archived`, the index's tree under the working tree's attributes, and asserts that no path under `.github/workflows/` is in it. A first form at 60b917be read HEAD through `dist_branch.py#archived`, and `seal mutate` showed it SURVIVED a removal of the line from the working tree. A7 was red against the tree without the line, and red under two `seal mutate` breaks of the line, removed and misspelt (executed). A dry run of `dist_branch.py` over HEAD in a scratch clone built a tree of 182 files with none under `.github/workflows/` (executed). The changelog fragment lists the six paths and why the workflows leave. `frame/design.md` *Data & interfaces*, the `.gitattributes` item ("Five lines follow"), and `frame/plan.md` *Operational impact*, the line on GitHub's source archives, still name five and are the orchestrator's to fold. Whether GitHub would have refused a first commit whose workflow blobs `main` already holds is moot with the directory left out.
```

### 2. A failure of the note step still skips `dist`, which is the reason the plan gives for putting `dist` in a job of its own

```seal
severity: should
location: `.github/workflows/publish-release.yml:47`, `.github/workflows/publish-release.yml:177-178`, `tests/behaviour/test_a_release_publishes_its_note.py:193-194`, `tests/behaviour/test_a_release_publishes_its_note.py:203`, `seal/threads/1793843890-the-directory-tracks-a-dist-branch/frame/plan.md:41`, `seal/threads/1793843890-the-directory-tracks-a-dist-branch/changelog.md:3`
evidence: read `.github/workflows/publish-release.yml:69-108`, `.github/workflows/publish-release.yml:176-197`, `seal/threads/1793843890-the-directory-tracks-a-dist-branch/frame/plan.md:41`
```

Why it matters: `frame/plan.md:41` rejects a `dist` step inside the `publish` job because "A failure of the note step skips it". It chooses instead a job "which `needs: publish` and conditions on the tag alone". The tag step and the note step are two steps of the one `publish` job (`publish-release.yml:69-108`, the steps `id: tag` at line 90 and `id: note` at line 101). A failed note step fails `publish`. A job with `needs: publish` and an `if:` that holds no status function runs only where `publish` succeeded, so `dist` is skipped on exactly that failure. The tag has already been created by then. The plan's stated reason does not hold for the design that was built.

Three sentences a person reads say otherwise. The workflow's header comment (`publish-release.yml:47`) and the changelog fragment (`changelog.md:3`) say the job "runs wherever `publish` passed on a tag". The case's docstring (`test_a_release_publishes_its_note.py:193-194`) says the same. The shipped run is red either way, and a re-run of the failed jobs fills `dist`, so the cost is a wrong account of when `dist` is filled, not a lost release.

The repair that matches the plan's reason makes the job's condition independent of `publish`'s status. The condition then rests on the tag output alone. Precondition this assumes: GitHub hands a dependent job the outputs a failed job's completed steps set. The fix pass confirms that from GitHub's documentation before taking this form. Where it does not hold, the repair is the other one: correct the plan row, the header comment, the changelog sentence and the docstring to say `dist` runs where `publish` succeeded with a tag.

```yaml
  dist:
    needs: publish
    if: ${{ !cancelled() && needs.publish.outputs.tag != '' }}
```

```python
    assert "    if: ${{ !cancelled() && needs.publish.outputs.tag != '' }}" in dist, dist
```

The snippet does not reach `frame/design.md` *Data & interfaces*, the `publish-release.yml` item, which spells the `if:` as built. The orchestrator owes that frame cell, and the fix pass owes a red run of the changed assertion against the old line.

```seal
verdict: fixed 60b917be
answer: The `dist` job's `if:` reads `${{ !cancelled() && needs.publish.outputs.tag != '' }}`, with a comment saying `!cancelled()` lifts the default `success()`. GitHub's documentation was read on 2026-11-05 (read, WebFetch of the workflow syntax, contexts and expressions references). `jobs.<job_id>.needs` says "If a job fails or is skipped, all jobs that need it are skipped unless the jobs use a conditional expression". `jobs.<job_id>.outputs` says "Job outputs are available to all downstream jobs that depend on this job". The expressions page says "A default status check of `success()` is applied unless you include one of these functions" and recommends `if: ${{ !cancelled() }}` to run "regardless of its success or failure". No page says whether a failed job's outputs reach a dependent job, so the round's precondition is neither confirmed nor refuted. The form was taken because it cannot do worse than the old line: where the output does not arrive, the tag reads empty and the job is skipped as before. `gaps.md` *Not verified* names that question and who answers it. The changed assertion in `tests/behaviour/test_a_release_publishes_its_note.py` was red against the old line before the edit, and `seal mutate` putting the old condition back was red at 60b917be (executed). The workflow's header comment, the case's docstring and the changelog fragment now say the job also runs where the note step failed after the tag step passed a tag on. `frame/plan.md`'s row for the `dist` step inside `publish` holds as written. `frame/design.md` *Data & interfaces*, the `publish-release.yml` item, still spells the old `if:` and is the orchestrator's to fold.
```

## Confirmations

What matched: no ruleset reaches `dist`. `gh api repos/MichaelYcJo/AgenticSeal/rulesets/<id>` shows the `main` ruleset limited to `~DEFAULT_BRANCH` and the `release` ruleset limited to `refs/heads/release/**/*`, and neither has bypass actors (executed). So the plan's *Operational impact* is right that a ruleset on `dist` is still to be added by the owner.

What matched: no workflow starts on a push to `dist`. `close-issues-on-release.yml`, `publish-release.yml` and `test.yml` start on pushes to `main`, `publish-release.yml` also on `v*` tags, `label-merged-on-release-branch.yml` on `release/*`, and `hygiene.yml` on pull requests (read, each file's `on:` block). So a `dist` commit that carries the workflows does not run them against a tree with no `tests/`.

What matched: the tree `dist_branch.py` builds is the archive. The dry run at d1431e49 exited 0 and printed `would push a commit of tree c5ec6aab... for vprobe as the first commit of dist`. `git ls-tree -r --name-only` of that tree and the file entries of `git archive vprobe | tar -t` were equal (`diff`, exit 0), with 187 files. None of them is under `tests/`, `evals/` or `seal/`, and neither `.test_durations` nor `CLAUDE.md` is among them (executed). This re-runs phase 3's claim of a 187-file `dist` at `b6b72d54`, now at HEAD.

What matched: every `from:` passage of the six rule changes stands in its section, and the `add` goes to the right section. `bin/seal settle --released-at HEAD`, run from the extracted archive of HEAD against the round's clone, listed the work item's `change` rules at `frame/design.md:118`, `:125`, `:142`, `:148` and `:155` as "from found, to not found". It placed the `add` at `frame/design.md:92` in `docs/releasing/branch-and-release.md` *Cutting a release*, and exited 0 (executed). So the rule change the orchestrator folded in at d1431e49, for the *Cutting a release* sentence phase 3 named as exception 2, matches the doc's text.

What matched: the `add` rule's last sentence, that `marketplace.json`'s `source` is `./` and `/plugin marketplace add` installs from `main`, matches `.claude-plugin/marketplace.json` at HEAD, where `plugins[0].source` is `"./"` (read).

What matched: the archive runs the repository's rule check. `bin/seal rules --check`, run from the extracted archive against the round's clone, exited 0 with `all 226 check lines in 70 rule files hold.` (executed). So a `check:` line that names `tests/` resolves in the user's repository, not in the plugin root. This repeats part of phase 3's Scope 7 smoke run, which this round did not run whole.

What matched: the crafters claimed their narrow runs passed. This round ran the nine test modules the diff writes in one `bin/test ... -q` command in the round's clone, and it ended 417 passed, exit 0 (executed). Phase 3's 107-module run, its `seal mutate` breaks and its seen-red runs were not re-run, and `## Not judged` names who answers them.

What matched: phase 3 claimed the frame named a hand push to `dist` as refused, and that the script in fact stacks on it. `dist_branch.py#remote_tip` reads the tip with `ls-remote` at each run, and the commit names it as its parent (`.github/scripts/dist_branch.py:117-123`, `:146-156`). `frame/plan.md` *Technical context*, as folded at d1431e49, now says the next release stands on a commit pushed by hand. It also says a push is refused only where `dist` moves between the read and the push, which D4 holds (read).

What matched: phase 1 claimed `extract` stops on a file already standing where it writes, and that neither caller meets one. `run_side` writes the plugin tree into a fresh `tempfile.mkdtemp` directory and removes `evals/behaviour/` before the suite is extracted into it (`evals/scripts/noninferiority.py:625-634`, read).

What matched: Q1 is open, and the build took its default. The job's environment names `github-actions[bot]` with `41898282+github-actions[bot]@users.noreply.github.com` as author and committer (`.github/workflows/publish-release.yml:192-195`, read). No real person's address appears in the diff.

What matched: the new cases were read against their groups. `bin/seal layout --pairs` exited 0 and named one pair, in `tests/github/test_plugin_directory_check.py::Test_main`, between two cases that already stood at the base (`test_accepts_absence_and_a_failed_fetch_at_exit_zero` and `test_the_run_claims_nothing_about_the_directory_and_names_the_pages`). It named no new case. The two new `Test_module` cases read two refs, which no earlier case reads. The four new `Test_extract` cases each hold one guard the old `extract` did not have.

Some cases hold a choice made in a phase record and no fact the frame states: `tests/evals/test_noninferiority.py#Test_extract::test_accepts_an_into_relative_to_the_caller`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py#test_the_archive_is_read_while_another_process_holds_the_index`, and D5's index assertion in `tests/github/test_dist_branch.py`. Each pins its whole guard by the mutant the phase record names, so none leaves a gap.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether GitHub refuses the first `dist` commit, which has no parent, for the workflow files it holds, given that `main` already holds the same blobs. The later releases that change a workflow file meet the documented refusal whatever the answer. | `.github/scripts/dist_branch.py:157` | the fix pass, which decides finding 1. If the finding is rejected, the v0.32.3 publish run's `dist` job answers it. |
| The full suite, the repository-wide lint and the format check at HEAD. This round ran nine modules. | the whole tree | the orchestrator's broad run |
| Phase 3's 107-module run, its 23 `seal mutate` breaks and its seen-red runs, and phases 1 and 2's runs. Read as claims and not re-run. | `trail/phases/phase-1.md`, `trail/phases/phase-2.md`, `trail/phases/phase-3.md` | the sealer's sample of the crafters' claims |
| The Windows rows of `gaps.md` *Not verified*, and the `release-report` job's worktree line on a GitHub runner | `gaps.md` | the `tests` workflow's Windows legs and the `release-report` job on the release pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the nine test modules the diff writes, `-q` | 417 passed, exit 0 |
| `git tag vprobe HEAD`, then `DRY_RUN=1 TAG=vprobe python3 .github/scripts/dist_branch.py`, then `diff` of the printed tree's paths against `git archive vprobe \| tar -t`'s files | exit 0. The tree had 187 files, `diff` exited 0, and no dropped path was in the tree. The tag was deleted afterwards. |
| `/.github/workflows/ export-ignore` added to `.gitattributes` with the `Edit` tool, then `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -k what_the_archive_holds` | 2 passed, exit 0. The line was then removed with `git checkout -- .gitattributes`. |
| `bin/seal settle --released-at HEAD` from the extracted archive of HEAD | exit 0. All five `from:` passages were found, and the `add` was placed in *Cutting a release*. |
| `bin/seal rules --check` from the extracted archive of HEAD | exit 0, `all 226 check lines in 70 rule files hold.` |
| `bin/seal layout --pairs` | exit 0. One pair, which already stood at the base, and none involving a new case. |
| `gh api repos/MichaelYcJo/AgenticSeal/rulesets/23858898` and `.../23856929` | `~DEFAULT_BRANCH` and `refs/heads/release/**/*`, with no bypass actors |
| `git merge-tree --write-tree HEAD origin/release/v0.32.3` in the worktree | exit 0 |

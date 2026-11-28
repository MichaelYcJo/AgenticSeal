# Closing memo: 1795849901-number-read-at-cut

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the branch's head, the `Broad gate` command of `agentory/config.json` | the orchestrator, at the broad gate after the review rounds settle |
| The changed step of `.github/workflows/hygiene.yml` on a real `pull_request` run: `git show` of `plugin.json` at `origin/main` and at the head the event names, and `gh issue list --label "merged: next"` with the job's read-only token. The cases stub every `git` and `gh` call, and the phase 1 probe read `git` alone, in this clone | the orchestrator, at the release pull request of the release that carries #1671, the first the changed check judges (`frame/plan.md` *Operational impact*) |
| The label workflow's run on a real push to `release/next`, which creates `merged: next` with its description on the tracker, and the close-issues run that takes it off at a real release. No run here reached the tracker | the orchestrator, at the first squash into `release/next` and at the first release cut from it |
| The publish workflow's reads at a real tag: `gh pr list --base main --state merged --limit 100` for the release pull request and one `gh pr view` per pull request the range names, under the workflow's `permissions: contents: write` token, in the `publish` job and again in the `mark` job. The cases stub every `gh` call, and the phase 2 probe ran the reads with a person's token against `v0.40.1` and `v0.41.0` | the orchestrator, at the publish run of the release that carries #1671 |

## Not done

The test file `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py`
keeps its name, though its step no longer reads a milestone. Its docstring
now says what the step holds. A rename moves a test file, which
`CONTRIBUTING.md` *The test layout* holds to its move check, and the name is
cited in the docstrings of `.github/scripts/release_completeness_check.py`
and `tests/github/test_release_completeness_check.py`. No *Scope* item names
the move, and `frame/plan.md` A10 kept the script's own name for a like
reason, so the move is left to the framer's judgment.

The fixture workflow `FIXTURE_WORKFLOW` of `tests/skills/test_broad_gate.py`
keeps the old step name, `the milestone this release claims is the work it
carries, and a patch carries no feat`. It is an example workflow the case
writes into a fixture repository to show that the broad gate reads no
workflow, and nothing reads the name from this repository's `hygiene.yml`.

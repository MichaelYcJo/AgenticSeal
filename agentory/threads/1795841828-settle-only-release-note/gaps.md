# Closing memo: 1795841828-settle-only-release-note

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the branch's head, the `Broad gate` command of `agentory/config.json` | the orchestrator, at the broad gate after the review rounds settle |
| The settle-only path's `gh release create` and the `mark` job's header replacement at a real tag. The cases stub `create` and the two new readers, and the dry run of `frame/design.md` S6 stops at `release_exists`, so no run here created a note or marked one (`frame/questions.md` Q1) | the orchestrator of the first release of settles alone after this ships, reading `gh release view vX.Y.Z` and `gh run list --workflow publish-release.yml` |

## Not done

The docstring of `skills/code-review/scripts/chain_check.py#settled` names `retired` as the predicate's caller and does not name `.github/scripts/publish_release_note.py#settles`. It was left as it stands. The policy sentence that names both askers is rule change 4 of `frame/design.md`, which the settle writes into `docs/checks/the-fold.md`. A list of callers in a docstring is one that a later caller makes false without editing it (contract rule 19).

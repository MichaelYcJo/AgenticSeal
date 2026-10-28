### Changed

- **A release's merge into `main` tags it and publishes its note in one run (#1117).** `.github/workflows/publish-release.yml` now fires on the push to `main` as well as on a `v*` tag. Its first step, `.github/scripts/tag_release.py`, creates the `vX.Y.Z` tag on the pushed commit where that push moved `.claude-plugin/plugin.json`'s version and no such tag exists. The note step and the seal job then run for that tag. A re-run passes on a tag that already names the pushed commit, and a tag pushed by hand still publishes. Nobody pushes a tag at the end of a release any more.
- **The version moves in a release's first pull request (#1117).** `skills/implement/orchestration.md` says that where a repository names the version when it cuts the release branch, as this one does, the orchestrator moves the version in the first pull request into the branch, and every later pull request into it leaves the version alone. No preparation pull request closes a release any more. The release note lists every pull request merged into the branch, the one that moved the version among them.
- **A work item that changes the way of working writes its process row in its own changelog fragment (#1117).** The fragment ends with a `### Process changes` table in the shape `templates/records/process.md` gives. The release note lifts every fragment's rows into one table of that name, above the folded fragments, and each fragment follows without its table. The framer reads that table in the latest GitHub Release and in the fragments of work items still open.
- **The check that refuses a loaded file naming an unreleased version says when it fires (#1117).** Its message says such a line goes red in the commit that moves the version to it, the first pull request of that version's release.

### Removed

- **`seal/process/` (#1117).** The three process archives, `0.22.4.md`, `0.23.0.md` and `0.23.1.md`, are readable at the tag `v0.23.1`. The release report no longer has a row for them.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| <the date the change landed> | <what this work item changed in the way of working> | <one line of why> | <a link to the issue comment or the commit the change came from> |

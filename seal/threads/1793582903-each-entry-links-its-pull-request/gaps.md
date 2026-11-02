# Closing memo: 1793582903-each-entry-links-its-pull-request

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the work item's head. Phase 1 ran its phase-boundary set of 43 modules, and ran `ruff check` and `ruff format --check` on its five changed Python files alone (`trail/phases/phase-1.md` *The phase-boundary run*, contract rule 2) | the orchestrator, by `seal gate` after the review rounds settle |
| closed whether `log.showSignature=true` changes what `settle.py#adding_commit` reads for a signed commit | measured by phase 1 in a scratch repository, since removed, with a commit signed by an ssh key: the verification (`No signature`) came on stdout ahead of the commit's line, the last line was `<commit>\0feat: signed (#3)`, and the reader's parse reads `3` from it (`trail/phases/phase-1.md` departure 1) |
| Whether `v0.28.0`'s published note opens each entry with its pull request's link. The cases build the note from fixture histories, and the first real run is the publish workflow at that tag | the orchestrator of the 0.28.0 release, reading the note at `v0.28.0` after the publish job |

## Not done

nothing

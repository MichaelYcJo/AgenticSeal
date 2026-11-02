# Closing memo: 1793582903-each-entry-links-its-pull-request

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the work item's head. Phase 1 ran its phase-boundary set of 43 modules and phase 2 its set of 72, and each ran `ruff check` and `ruff format --check` on its own changed Python files alone (`trail/phases/phase-1.md` and `trail/phases/phase-2.md` *The phase-boundary run*, contract rule 2) | the orchestrator, by `seal gate` after the review rounds settle |
| closed whether `log.showSignature=true` changes what `settle.py#adding_commit` reads for a signed commit | measured by phase 1 in a scratch repository, since removed, with a commit signed by an ssh key: the verification (`No signature`) came on stdout ahead of the commit's line, the last line was `<commit>\0feat: signed (#3)`, and the reader's parse reads `3` from it (`trail/phases/phase-1.md` departure 1) |
| Whether `v0.28.0`'s published note opens each entry with its pull request's link. The cases build the note from fixture histories, and the first real run is the publish workflow at that tag | the orchestrator of the 0.28.0 release, reading the note at `v0.28.0` after the publish job |
| Whether the first real `seal settle --apply` under this change removes the released work items whose notes `v0.27.3` and earlier published, through the old marker. The cases read a `gh` stub's list, and phase 2's probe read the real list through `settle.py#published_releases` alone, without running `--apply` (`trail/phases/phase-2.md` *The probe*) | the owner, at the settle after `v0.28.0` (`docs/release-checklist.md` *2b. Settle what earlier releases left behind*) |

## Not done

`.test_durations` still names `tests/skills/test_settle.py::Test_main::test_shared_mode_never_asks_gh`, which phase 2 renamed. The file holds timings that the next recording rewrites, and an entry for a case that no longer exists costs the run nothing but that case's recorded time (`trail/phases/phase-2.md` departure 6).

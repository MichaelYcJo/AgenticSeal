# Closing memo: 1793582903-each-entry-links-its-pull-request

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the format check at the work item's head. Phase 1 ran its phase-boundary set of 43 modules and phase 2 its set of 72, and each ran `ruff check` and `ruff format --check` on its own changed Python files alone (`trail/phases/phase-1.md` and `trail/phases/phase-2.md` *The phase-boundary run*, contract rule 2) | answered: `trail/gate.md`, the `Broad gate` row passed at `852178961` against `30ba21373`, and `guarantee.md` sealed on it |
| closed whether `log.showSignature=true` changes what `settle.py#adding_commit` reads for a signed commit | measured by phase 1 in a scratch repository, since removed, with a commit signed by an ssh key: the verification (`No signature`) came on stdout ahead of the commit's line, the last line was `<commit>\0feat: signed (#3)`, and the reader's parse reads `3` from it (`trail/phases/phase-1.md` departure 1) |
| closed Whether `v0.28.0`'s published note opens each entry with its pull request's link. The cases build the note from fixture histories, and the first real run is the publish workflow at that tag | answered: `gh release view v0.28.0`: each of its ten fragments opens with a `[#N](https://github.com/MichaelYcJo/AgenticSeal/pull/N)` line |
| closed Whether the first real `seal settle --apply` under this change removes the released work items whose notes `v0.27.3` and earlier published, through the old marker. The cases read a `gh` stub's list, and phase 2's probe read the real list through `settle.py#published_releases` alone, without running `--apply` (`trail/phases/phase-2.md` *The probe*) | answered: this settle (`chore/settle-0.28-0.29`) read `settle.py#notes` over the published list before `--apply`: v0.27.3's note carries its seven work items through the old marker, and v0.28.0's and v0.29.0's carry theirs through the link, so `--apply` kept none for its note |

## Not done

`.test_durations` still names `tests/skills/test_settle.py::Test_main::test_shared_mode_never_asks_gh`, which phase 2 renamed. The file holds timings that the next recording rewrites, and an entry for a case that no longer exists costs the run nothing but that case's recorded time (`trail/phases/phase-2.md` departure 6).

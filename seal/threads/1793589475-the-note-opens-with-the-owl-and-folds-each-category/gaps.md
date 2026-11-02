# Closing memo: 1793589475-the-note-opens-with-the-owl-and-folds-each-category

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the work item's head. Phase 1 ran its phase-boundary set of five modules, and ran `ruff check` and `ruff format --check` on its own three changed Python files alone (`trail/phases/phase-1.md` *The phase-boundary run*, contract rule 2) | the orchestrator, by `seal gate` after the review rounds settle |
| Whether the releases page draws each category fold as one element holding its lines. The render case reads the note through `cmarkgfm` 2025.10.22 with raw HTML kept, and the framer's probe read a sample through GitHub's own renderer. Neither is the releases page | the orchestrator of the 0.28.0 release, reading the note at `v0.28.0` after the publish job, with `frame/questions.md` Q1 |
| Whether a real `seal` job's `gh release edit` leaves the two-cell header on the releases page as the cases build it, with the owl beside the results, and whether a re-run of the job then uploads and edits nothing. The cases stand in for `gh` (`tests/github/test_release_seal.py#GitHub`), and phase 2 rendered no header through any renderer (`trail/phases/phase-2.md`) | the orchestrator of the 0.28.0 release, reading the note at `v0.28.0` after the `seal` job, with `frame/questions.md` Q1 |

## Not done

- `release_seal.py#plural` and the new `publish_release_note.py#plural` were not made one function. The seal would then call the publisher in `release_rows`, which the seal loads only when first asked (`trail/phases/phase-2.md` *Decision: `publish_release_note.py` gets its own `plural`*).
- `.test_durations` keeps the old ids of the cases phase 2 renamed. The test runner rewrites that cache, and `tests/censuses.py#OLD_NAME_RECORDS` exempts it from the old-name census.

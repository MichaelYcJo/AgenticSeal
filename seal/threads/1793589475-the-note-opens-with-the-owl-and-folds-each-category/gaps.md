# Closing memo: 1793589475-the-note-opens-with-the-owl-and-folds-each-category

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the format check at the work item's head. Phase 1 ran its phase-boundary set of five modules, and ran `ruff check` and `ruff format --check` on its own three changed Python files alone (`trail/phases/phase-1.md` *The phase-boundary run*, contract rule 2) | answered: `trail/gate.md`, the `Broad gate` row passed at `9b502c09a` against `47ec17cb8`, and `guarantee.md` sealed on it |
| closed Whether the releases page draws each category fold as one element holding its lines. The render case reads the note through `cmarkgfm` 2025.10.22 with raw HTML kept, and the framer's probe read a sample through GitHub's own renderer. Neither is the releases page | answered: the releases page of v0.28.0, fetched from https://github.com/MichaelYcJo/AgenticSeal/releases/tag/v0.28.0, renders each category as one `<details>` element under its `<summary>`: Features (8), Fixes (2), and the full changelog |
| closed Whether a real `seal` job's `gh release edit` leaves the two-cell header on the releases page as the cases build it, with the owl beside the results, and whether a re-run of the job then uploads and edits nothing. The cases stand in for `gh` (`tests/github/test_release_seal.py#GitHub`), and phase 2 rendered no header through any renderer (`trail/phases/phase-2.md`) | answered for the header: publish-release run 41397352734's `seal` job printed `attached seal.png to v0.28.0 and put it in the note`, and the published note opens with the two-cell table, the owl beside the results. A re-run of that job is a measurement no record asks for: the job ran once (attempt 1) at each tag since, and the answer would have decided whether a re-run edits the note twice |

## Not done

- `release_seal.py#plural` and the new `publish_release_note.py#plural` were not made one function. The seal would then call the publisher in `release_rows`, which the seal loads only when first asked (`trail/phases/phase-2.md` *Decision: `publish_release_note.py` gets its own `plural`*).
- `.test_durations` keeps the old ids of the cases phase 2 renamed. The test runner rewrites that cache, and `tests/censuses.py#OLD_NAME_RECORDS` exempts it from the old-name census.

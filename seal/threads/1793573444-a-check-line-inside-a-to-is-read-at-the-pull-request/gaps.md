# Closing memo: 1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request

## Not verified

| Item | Who must answer |
|---|---|
| closed The suite beyond phase 1's narrow run, the repository-wide lint and the format check | answered: `trail/gate.md`, the `Broad gate` row passed at `33419ffe5` against `57d6665b5`, and `guarantee.md` sealed on it |
| closed that `seal rules --check` prints at this branch what it printed at the base for the same rule files (design S7) | round 1 (`trail/rounds/round-1.md`) ran base and head code over base and head trees, each exit 0 with the same output; the rewritten `unresolved` branch was read, since the tree holds no refused line |
| closed that `chain_check.py` loads `.github/scripts/rules.py` in a user's CI, from the plugin clone `templates/setup/hygiene.yml` makes (design G9) | round 1 (`trail/rounds/round-1.md`) read `templates/setup/hygiene.yml:63-78` cloning the whole plugin, found `rules.py` at tag v0.27.3, and ran the head `chain_check.py` from a clone outside the repository over the main clone, exit 0 |
| closed That the release note the tag builds shows this fragment under its `<!-- specs/... -->` marker once: read from `.github/scripts/publish_release_note.py#section`, not run against this fragment | answered: `gh release view v0.28.0` holds #1282's fragment once, in the full changelog under its `[#1282](https://github.com/MichaelYcJo/AgenticSeal/pull/1282)` line, the form #1291 gave entries in the same release |

## Not done

nothing

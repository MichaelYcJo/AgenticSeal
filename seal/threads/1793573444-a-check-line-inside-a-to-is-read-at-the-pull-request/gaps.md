# Closing memo: 1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request

## Not verified

| Item | Who must answer |
|---|---|
| The suite beyond phase 1's narrow run, the repository-wide lint and the format check | the orchestrator's broad gate, `seal gate --base origin/release/v0.28.0 --record seal/threads/1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request` |
| closed that `seal rules --check` prints at this branch what it printed at the base for the same rule files (design S7) | round 1 (`trail/rounds/round-1.md`) ran base and head code over base and head trees, each exit 0 with the same output; the rewritten `unresolved` branch was read, since the tree holds no refused line |
| closed that `chain_check.py` loads `.github/scripts/rules.py` in a user's CI, from the plugin clone `templates/setup/hygiene.yml` makes (design G9) | round 1 (`trail/rounds/round-1.md`) read `templates/setup/hygiene.yml:63-78` cloning the whole plugin, found `rules.py` at tag v0.27.3, and ran the head `chain_check.py` from a clone outside the repository over the main clone, exit 0 |
| That the release note the tag builds shows this fragment under its `<!-- specs/... -->` marker once: read from `.github/scripts/publish_release_note.py#section`, not run against this fragment | the tag's workflow at the 0.28.0 release, and the orchestrator reading the published note |

## Not done

nothing

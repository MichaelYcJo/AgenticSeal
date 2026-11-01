# Closing memo: 1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request

## Not verified

| Item | Who must answer |
|---|---|
| The suite beyond phase 1's narrow run, the repository-wide lint and the format check | the orchestrator's broad gate, `seal gate --base origin/release/v0.28.0 --record seal/threads/1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request` |
| That `seal rules --check` prints at this branch what it printed at the base for the same rule files (design S7): it was run at phase 1's commit alone, exit 0, and not at the base for a comparison | the proofer at round 1, reading the `unresolved` diff in `.github/scripts/rules.py` |
| That `chain_check.py` loads `.github/scripts/rules.py` in a user's CI, from the plugin clone `templates/setup/hygiene.yml` makes: read from the template and the installed plugin's tree (design G9), never run in a user's repository | the proofer at round 1, reading `templates/setup/hygiene.yml` |

## Not done

nothing

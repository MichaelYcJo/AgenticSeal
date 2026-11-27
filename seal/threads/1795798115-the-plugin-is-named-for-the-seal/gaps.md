# Closing memo: 1795798115-the-plugin-is-named-for-the-seal

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate over phase 1's commits: the full suite, the repository-wide lint and the format check of `seal/config.json`'s `Broad gate` key. The crafter ran the phase-boundary set and linted the files it changed | the orchestrator, at the broad run |

## Not done

Phase 1 left two readers that still compute the root's name, though the name is now always `lib/optin.py#HOME`: `skills/implement/scripts/seal.py#display`, called with the shared place, and `skills/settle/scripts/settle.py#threads`, which reads the basename of the root it is given. Both read a path they are handed and fall back to nothing for a second name, so neither stands on the removed fact.

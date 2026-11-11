# Closing memo: 1794383426-eval-code-the-verdict-does-not-read

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check over phase 1's tree. Every module file runs `tests/censuses.py` through `census_case`, and phase 1 ran only the phase boundary set. | the orchestrator, at the broad gate |

## Not done

Phase 1 leaves the 101 `.test_durations` keys of the cases it removed or renamed in `tests/evals/test_noninferiority.py`. `frame/plan.md` *Phases* gives Scope 12 to phase 2, which drops them with the entries of the cases it removes, where #1486 has not removed the file first.

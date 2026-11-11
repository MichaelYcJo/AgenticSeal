# Closing memo: 1794383424-the-gate-ships-a-copy-of-one-workflow

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate at HEAD: the full suite, `uvx ruff check .` and `uvx ruff format --check .` (contract rule 2) | the orchestrator |
| S2: at HEAD the gate's report carries no `CI also` row, and its stderr no line opening `seal gate: .github/workflows/hygiene.yml's` | the orchestrator, reading its broad run's output |
| S3's case on CI's `windows-latest` leg, where the searched workflow path takes the platform's separator | CI on the pull request |

## Not done

nothing

# Closing memo: 1794530293-three-compatibility-paths-still-stand

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check, the `Broad gate` key of `seal/config.json`, at the work item's HEAD | the orchestrator, once the review rounds settle |
| `frame/design.md` S2: bare `seal mode` over a root holding `config.md` and no `config.json` writes a `Mode` key from the folder and leaves `config.md` as it was. No case builds that root, by the frame's choice | the proofer, reading `skills/implement/scripts/seal.py#mode_report` |
| `frame/design.md` S3: `chain-check`'s parity arm refuses nothing for a `seal/parity.md` that stands without a `seal/parity.json`. The case the phase ran, `Test_originals_of`'s case for no migration config, carries no `parity.md`, by the frame's choice | the proofer, reading `skills/code-review/scripts/chain_check.py#originals_of` |

## Not done

`tests/conftest.py`'s comment above `FENCED_ABOVE` says that two cases
build on those bytes. One case does, in `tests/lib/test_tables.py`, and so
the comment was already wrong before this work began. It describes no
compatibility path, so this phase left it as it was.

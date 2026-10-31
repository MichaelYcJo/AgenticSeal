# Closing memo: 1793457436-row-deletion-check-and-a-symlink

## Not verified

| Item | Who must answer |
|---|---|
| `frame/questions.md` Q1: whether the link cases of `tests/skills/test_unverified_check.py` run on the Windows legs or skip there through `symlink_or_skip`. They ran on macOS here and skipped none | a measurement: the Windows legs of `.github/workflows/test.yml` on this pull request. Naming a skip there is #1221's |
| A tracked link whose target stands on another Windows drive, run end to end. The `another volume` case makes `os.path.relpath` raise to reach the branch, so what Windows `os.path.realpath` answers for such a link was not run | a maintainer with a Windows machine holding two drives |
| The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch | the orchestrator, through `seal gate` |

## Not done

Nothing beyond the list under *Out* in `frame/design.md` *Scope*, which gives each item left and its grounds.

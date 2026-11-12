# Closing memo: 1794465691-the-orchestrator-polls-ci-by-hand

## Not verified

| Item | Who must answer |
|---|---|
| The whole suite, the repository-wide lint and the format check over the branch at its last commit: no phase runs them | the orchestrator, through `seal gate` |
| `tests/skills/test_pr_wait.py` on Linux, on Windows, and under Python 3.12 and 3.14. On Windows its `gh` stub is a `gh.cmd`, which the command finds through `shutil.which`. Phase 1 ran the cases on macOS under Python 3.13 alone | the pull request's `tests` workflow, whose matrix runs each of them |
| Whether the paragraph on `seal pr-wait` in `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* keeps every act the two paragraphs it replaced gave, and whether each row's act is the one its exit code asks for. The pin holds each command, each exit code and the states behind exits 4 to 6, and not the act in a row; phase 2 read the rows against the old paragraphs and against `pr_wait.py` | the proofer, reading the paragraph against `frame/design.md` *Grounding* G3 and S10 |

## Not done

nothing

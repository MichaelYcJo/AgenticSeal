# Closing memo: 1793599987-a-script-reads-git-the-same-under-any-config

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the format check at the work item's head | answered: `trail/gate.md`, the `Broad gate` row passed at `9cd0a3530` against `5e45418fb`, and `guarantee.md` sealed on it |
| closed `tests/hooks/test_gitcmd.py`, the readers built by `gitcmd.argv`, and phase 2's six cases over a work item, fragment or test file whose name is not ASCII, on the Windows and Linux legs of `.github/workflows/test.yml`; phases 1 and 2 ran on macOS with git 2.50.1 alone (`frame/questions.md` Q1) | answered: #1306's `tests` run 41537341558 at `e1363fe0f` passed on its four `windows-latest` legs and every Linux leg |
| closed That each `git log` and `git status` a script under `hooks/`, `skills/` or `.github/scripts/` starts is built by `gitcmd.argv`. No case pins a call site: `settle.py#adding_commit` put back to a hand-written argv survived its cases (`trail/phases/phase-1.md`) | round 1's first confirmation: an `ast` walk of every tracked script listed 16 `log` and `status` calls, each built by `argv` (`trail/rounds/round-1.md`) |
| closed That no script under `hooks/`, `skills/` or `.github/scripts/` takes paths out of git's output without `-z`, beyond the six readers phase 2 changed. Each of the six has a case; a search for the argv words that list paths is a sample, and the framer's `ast` walk is the whole list (`trail/phases/phase-2.md`) | round 1's second confirmation: the same walk found no reader of a path git quotes under `core.quotePath` without `-z` beyond the six (`trail/rounds/round-1.md`) |

## Not done

nothing

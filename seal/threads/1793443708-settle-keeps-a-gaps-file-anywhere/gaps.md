# Closing memo: 1793443708-settle-keeps-a-gaps-file-anywhere

## Not verified

| Item | Who must answer |
|---|---|
| The suite, the repository-wide lint and format check, the `Broad gate` row in `seal/config.md` | the orchestrator, by `seal gate --base <base> --record 1793443708-settle-keeps-a-gaps-file-anywhere` |
| The two cases of `tests/skills/test_settle.py#Test_misplaced` on Windows: each skips where the platform makes no symbolic link, so the walk's handling of links is unproved there until a run shows both passed and neither skipped | the `windows-latest` legs of `.github/workflows/test.yml`, which run on the pull request |

## Not done

- **Keeping the directory for a misplaced `gaps.md`, as the issue's first *Done when* line asks.** The frame rejects it (`frame/plan.md` A1) on the core's rule that a script decides nothing on a reading guessed from a name.
- **Naming the misplaced file at the pull request through `seal unverified`.** #1038 holds that question, and #1198 is editing `skills/verify/scripts/unverified_check.py` (`frame/plan.md` A6).
- **A subdirectory of a work item's directory that cannot be listed.** `os.walk` passes over it without a word, so a misplaced file inside it is not named. The frame's *Scope* item 1 does not ask for it, no work item has written one (`frame/design.md` *Grounding*, the history row), and naming it would be a second reading of an unreadable directory beside the one `hooks/lib/routing.py#rounds_unreadable` gives `trail/rounds`. What `shutil.rmtree` does with such a directory at `--apply` was not run.

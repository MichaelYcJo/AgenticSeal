# Closing memo: 1793504229-a-linked-memo-named-as-the-argument

## Not verified

| Item | Who must answer |
|---|---|
| `frame/questions.md` Q1: whether the new link cases of `tests/skills/test_unverified_check.py` run on the Windows legs or skip there through `symlink_or_skip`. They ran on macOS here and none skipped | a measurement: the Windows legs of `.github/workflows/test.yml` on this pull request. Naming a skip there is #1221's |
| Whether `as_named` keeps a Windows path as named, where git spells the top with `/` and `os.path.realpath` answers with the case the disk holds. `os.path.samefile` finds the top, so the spelling should not matter, but no Windows run read it | a maintainer with a Windows machine, or the Windows legs of `.github/workflows/test.yml` where the link cases do not skip |
| Whether a component typed on Windows in another case than the disk holds reads the base in the disk's case again. Round 1 found that `as_named` keeps the typed case, so the typo check and the presence check matched no line of `ls-tree`. `spellings` ends at `real()`'s spelling, which `ntpath.realpath` gives in the disk's case, so both should match again, and the second arm should answer None at the typed spelling. All of it was read, and no Windows run reached it | the Windows legs of `.github/workflows/test.yml` on this pull request; no case types a component in another case, so a maintainer with a Windows machine running `seal unverified --baseline <base> SEAL/threads` |
| The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch | the orchestrator, through `seal gate` |

## Not done

The list under *Out* in `frame/design.md` *Scope* gives each item left there and its grounds.

A link inside one repository to a closing memo in a second repository (P7 and Q1 of `frame/design.md` *Grounding*) still exits 0 where the target lost nothing against the second repository's base. The repository is the one the real path is in, so the link's own path in the first repository is never compared. Taking the repository from the link instead breaks a checkout reached through a link from a directory that is itself a repository, and `Test_repository_of::test_accepts_the_repository_the_real_path_is_in_over_the_links` now pins that layout. Comparing in both repositories breaks `#main`'s rule that every argument is read against one repository. No layout of the plugin puts a closing memo's link into another repository.

`spellings` does not give a spelling that keeps a link above a link it resolves, because `real()` resolves every link before the one it is asked about (`trail/phases/phase-1.md` *Round 1's fix pass*, *Where the class stays open*). The base spells a path that way only where a component that was a directory at the base is now a link, and holds below it a link that stood at the base too. Giving that spelling needs a reader that resolves one link at a time through `os.readlink`, which is a second resolver beside `real()`. No layout of the plugin makes it.

A component typed in another case than the disk holds, on a case-insensitive macOS volume, passes a dropped row and a deleted memo with exit 0, because `posixpath.realpath` does not fold case. That held at 48d035aa before this work (executed, `trail/phases/phase-1.md` *Round 1's fix pass*). Reading the disk's case means asking the directory for each name, a reader of its own. The issue does not report it, so it is #1238.

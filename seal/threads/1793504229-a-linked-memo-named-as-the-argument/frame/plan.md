# Implementation Plan: 1793504229-a-linked-memo-named-as-the-argument

## Technical context

The code is `skills/verify/scripts/unverified_check.py` at 4da937fa.

- `#overviews` (lines 929–956) resolves each argument with `real()` at line 943, then walks it without following linked directories.
- `#real` (lines 1022–1033) is `os.path.realpath`. Its docstring gives the reason a path must be resolved at all: `git rev-parse --show-toplevel` answers with links resolved, so a tree reached through a link produced a `../link/...` path that matched no line of `ls-tree`.
- `#main` reads the argument through `real()` again for the root (line 1569), the other-volume refusal (line 1608), the typo check (line 1626) and the presence arm's prefixes (line 1708).
- The second arm (lines 1680–1706), added by #19, compares a path at its own name where `os.path.islink(path)` and the base did not record a link there. It reads the base through `#mode_at` and `#compare_at`.
- The comment that #1235 edits is at line 113, outside every line above.

The cases are in `tests/skills/test_unverified_check.py`: `Test_real` (line 1532), `Test_overviews` (line 1454), and the link cases of `Test_main` from line 2228. Links are made through `tests/conftest.py#symlink_or_skip`.

The chosen approach's failure scenario in six months: someone replaces a closing memo with a link to a memo in another repository, deletes a row there, and names the link. The run compares the other repository's memo against that repository's base and exits 0 (P7 and Q1, `frame/design.md` *Scope*, *Out*). A second failure: on a Windows leg without the link privilege, every new case skips, and nothing names the skip (#1221).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep resolving the argument with `real()` (the structure kept as it stands) | The premise that keeps it is that resolving the argument costs nothing the comparison needs. It is false: P1, P2, P3, P7 and Q1 pass a lost row with exit 0, and P8 exits 2 with a reason that is false (`frame/design.md` *Grounding*, the first probe row, executed). | rejected |
| Resolve only the argument's directory, in `#overviews` and in the prefixes (`seal/threads/1793457436-row-deletion-check-and-a-symlink/gaps.md` *Not done*) | A memo deleted from a tree named through a link to its top exits 0, where it exits 1 now. The kept link makes the prefix `../<link>`. P2 and P3 still exit 0, because the arm asks `os.path.islink` of the file alone (`frame/design.md` *Grounding*, the second probe row, executed). | rejected |
| **One reader that resolves the path up to the repository's top and keeps the components inside it; the repository found from the real path as now, and from the deepest link only where the real path is in none; the second arm widened to every path reached through a link** | See *Technical context*. P1, P2, P3 and P8 exit 1 against a scratch build of it, and every probe of what it keeps keeps its exit (`frame/design.md` *Grounding*, the chosen-approach probe row, executed). P7 and Q1 stay open. | **chosen** |
| The same reader, with the repository always taken from the deepest link on the path | P7 and Q1 exit 1. A repository reached through a link that stands in a second repository exits 2 with a row dropped, where it exits 1 now, because the base is resolved in the second repository (`frame/design.md` *Grounding*, the deepest-link probe row, executed). It trades a layout no plugin record makes for one a person's own machine makes. | rejected |
| Keep `real()` for the argument, and add an arm after the scan that compares each argument that is a link at its own path | It is a third copy of the per-link comparison. The prefixes and the root still come from the real path, so P8 still exits 2, and a named directory link and a linked ancestor each need the arm again. Each repair adds a branch for one more shape of argument. | rejected |
| Ask git for the path as named (`git rev-parse --show-prefix` from the argument's directory) | git answers with links resolved: from a linked `specs/a` it prints `specs/b/` (`frame/design.md` *Grounding*, executed). It gives back the path `real()` gives. | rejected |
| Refuse a named argument that is, or passes through, a link (exit 2) | P9, a named link whose target holds every row, is refused with nothing wrong. A run without `--baseline` on a linked memo, which reads its open rows today, would stop reading them. | rejected |
| Replace the walk, the second arm and the presence arm with one loop over the base's listing, reading each listed path in the working tree through whatever links it holds | The prefixes still come from the argument, so the argument reader of the chosen row is owed under this structure as well. It also turns the scanned directory link's `present at HEAD and not here` into a row comparison, which the issue does not ask for, and it rebuilds the arm #19's three rounds reviewed. The premise that keeps the two lists, that `ls-tree` lists a tracked link under its own path, was checked by #19 (`seal/threads/1793457436-row-deletion-check-and-a-symlink/frame/plan.md`, the row that replaces the two-list structure) and holds here: the scanned runs keep their exits under the chosen build. | rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope items 1, 2, 3, 4, 5 and 6 | `tests/skills/test_unverified_check.py`, the classes `Test_real`, `Test_overviews`, `Test_unique_by_target`, `Test_main`, the new reader's class, `Test_repository_of` and `Test_spellings`, in one command. Each new case is seen red against 4da937fa's `unverified_check.py`: the named file link, directory link and linked-ancestor cases exit 0 there; the outside-every-repository case exits 2. `test_refuses_a_deletion_reached_through_a_linked_path` stays green, and is seen red against a build that keeps the argument's last component unresolved, which is the directory-only alternative. | e4ba92f5 |

## Operational impact

None to deploy. A person who names a link, or a path through a linked directory, now sees the run exit 1 where a row left the memo the path held at the base. A named link to a file outside every repository is compared at its own path, where the run used to exit 2 with `is not in one`. The changelog fragment states each of these under `### Fixed`. The new cases are absent from `.test_durations`, so `pytest-split` gives them the average duration.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
| 2026-11-01 | Round 1's *Not judged* row on `..`: a `..` in a named path is read as the file system reads it, not by text. Each `..` steps up from where the component before it leads: that component is resolved where it is a link, and every other component, a link the `..` does not step out of among them, is kept as named; a case pins it | `os.path.abspath` drops `specs/a/..` by text, so where `specs/a` is a link the reader names a directory the file system does not reach, and the deletion check would compare a path nobody named. Reading `..` physically is what `git` and the shell's `cd -P` do with it, so the argument means what the person's own tools mean by it | `frame/design.md` *Scope* item 1, which keeps "the components inside the repository as typed" and says nothing of `..` |
| 2026-11-01 | Round 1's fix pass left two framer cells for the orchestrator, folded in place: design's scenario *A tree reached through a link* names the link inside the repository round 1 found and its case, and phase 1's *Verified by* names `Test_repository_of` and `Test_spellings`. The pre-existing case-fold defect the fix pass found on macOS is filed as #1238, in `backlog: gates & hooks`, and `gaps.md` names it | Each fold makes the frame say what the build now verifies. The case-fold defect held at the base, so it is no regression of this work, and its fix is a reader of the disk's case that the issue did not ask for | `docs/the-review-record.md` *The run*; `skills/implement/orchestration.md`, the table row on a lesson whose home no work item in progress changes |
| 2026-11-01 | Round 2's finding on `absolute`: the `..` row above is rewritten in place to resolve only the link a `..` steps out of. The first wording resolved every component up to the last `..`, so a link the `..` never left was resolved too, and round 2 showed a dropped row passing behind it | The first wording was wider than the physical reading it cited: `cd -P` resolves the directory a `..` leaves, not every link before it. The fix pass builds round 2's form of `absolute` | `frame/design.md` *Scope* item 1, "the components inside the repository as typed" |

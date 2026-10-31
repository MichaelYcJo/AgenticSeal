# Implementation Plan: 1793457436-row-deletion-check-and-a-symlink

## Technical context

The code is `skills/verify/scripts/unverified_check.py` at a92c358b.

- `#unique_by_target` (lines 1103–1118) keeps the first path per `os.path.realpath`, in the order `#overviews` sorted them.
- `#main` loops over that list (line 1589). Under `--baseline` it reads the base side with `show(root, base, repo_relative(path, root))` (line 1604) and the tree side with `check_file(path)`, which follows a link.
- The presence arm builds `here` from the unresolved `files` (line 1641) and leaves the kept path out of it.
- `#show` (lines 1440–1447) already decodes UTF-8 with `errors="replace"`.

The cases are in `tests/skills/test_unverified_check.py`:

- the `linked` fixture (lines 157–171), whose link sorts after its target;
- `Test_main::test_accepts_a_tracked_link_counted_once_and_not_deleted` (line 2151);
- `Test_unique_by_target` (line 1588);
- `Test_show` (line 1718).

Links are made through `tests/conftest.py#symlink_or_skip`.

The chosen approach keeps the real path (design Scope items 1 and 2). Its failure scenario in six months: a person runs the check on one work item's directory, and the report names a file in another directory, the link's target. The report is true, but it names a path the person did not type. A second failure: on a Windows leg without the link privilege, every case of this work skips, and nothing names the skip (#1221). The privilege is the Developer Mode or elevated-shell right that `symlink_or_skip` asks for.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the first path in sort order, as now (the structure kept as it stands) | The premise that keeps it is that the real file always sorts first. It is false, as probe 1 shows: a link at `specs/a` beside `specs/b` passes two deleted rows with EXIT=0 (design *Grounding*, executed). | rejected |
| The issue's first box read literally: among the paths to one real file, prefer the one that is not a link, and otherwise keep the link | Probe 3: the link alone is under the scanned path and the target lies elsewhere in the repository. The link is still kept, the base side still reads its blob, and two deleted rows still pass with EXIT=0. Closing that needs a second rule, a refusal for a link with no real sibling, where reading the target answers it. | rejected |
| Keep the survivor as now, and read the base side at `repo_relative(os.path.realpath(path))` | Correct for probes 1–3. But one report line would then name the link's path while counting the target's rows, so the line and the comparison would rest on two paths. The chosen approach uses one path for both. | rejected |
| **Keep the real file's own path for every real file, and name a real path outside the repository as not compared** | See *Technical context*: a report can name a path the person did not type. Probes 1–3 exit 1 against a scratch build of it, and probe 4 shows that Scope item 2 is needed (design *Grounding*, executed). | **chosen** |
| Replace the two-list structure, so that `overviews` resolves every file and `files` is de-duplicated once | `overviews_at` lists a tracked link under its own path, and `here` must hold that path. Built from resolved paths, the presence arm reports a link that is right there as deleted. `overviews`'s own comment records that failure, and `test_accepts_a_tracked_link_counted_once_and_not_deleted` pins it. The premise that keeps two lists was checked and holds (read). | rejected |
| Refuse any tracked `gaps.md` that is a link (exit 1 or 2) | A repository that links one record from two work items goes red with nothing wrong. The `linked` fixture is that repository, and the script's docstring calls the pair one record. | rejected |
| Resolve the link at the base through git (`git show` the link's blob, join it to the link's directory, then `git show` that path) | This re-implements `realpath` over git trees: chains, retargeted links, and targets outside the repository all need their own branches. It also asks a different question, *what the link pointed at then*, where the check asks *which rows this branch removed from this file*. | rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope items 1, 2, 3 and 4 | `tests/skills/test_unverified_check.py`, the classes `Test_unique_by_target`, `Test_show` and `Test_main`, in one command. Each new case is seen red first: the two link-order and link-alone cases against a92c358b's `unique_by_target`; the outside-repository case with Scope item 2 left out, where it exits 0 with no notice (design *Grounding*, the second probe); the `show()` case with `show()` reverted to `text=True`, which raises `UnicodeDecodeError` under a UTF-8 locale. | 7f9339c1 |

## Operational impact

None to deploy. Three report lines change for a person who reads them: a deletion found through a link names the target's path; a link to a file outside the repository is listed under `not compared` with a new reason; and a closing memo that was a file at the base and is a link now is reported under the link's own path where it holds fewer rows. The changelog fragment states all three under *Fixed*. The new cases are absent from `.test_durations`, so `pytest-split` gives them the average duration, and each still runs in exactly one shard (`.github/workflows/test.yml`, read).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-01 | Round 1's finding 1, a closing memo that became a link on the branch passing its deleted rows, was fixed by asking git each link's mode at the base (d64de886), and the frame's *Data & interfaces* is folded to state it. The opposite direction, a link at the base replaced by a real file, stays out as *Scope* says | The frame's reason for reading no mode, that no deletion passes, held for that direction and not for this one, which phase 1's change turned from a refusal into a pass; the crafter reads the frame, so the fold comes before the verifying round | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* (a decision after the frame is folded in place) |

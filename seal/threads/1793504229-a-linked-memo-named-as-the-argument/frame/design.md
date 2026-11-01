# Design: 1793504229-a-linked-memo-named-as-the-argument

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-record-layout.md` *The fold, and what tells it from a deletion* | A row removed from a `## Not verified` table, or a `gaps.md` removed from a directory that stays, is a deletion, and `seal unverified --baseline` fails on it. This work changes no part of that rule. It makes the code meet the rule when the path a person names is, or passes through, a symbolic link inside the repository. |
| `docs/the-record-layout.md` *The unverified record, and the baseline it is read against* | The base is resolved once, to the merge base, and every arm reads that commit. This work keeps that, and keeps the repository it is resolved in, except where the old rule found none (Scope item 2). |
| `docs/what-a-script-gates.md` *The checks*, row `seal unverified` | The row says what the check reads and what it refuses. Nothing in the row changes, so no rule change is owed (`## Rule changes`). |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | A script names what it did not read and decides nothing on it. A real path that no commit of the repository holds stays named as not compared, as #19 made it. |
| read: issue #1225, through `gh issue view 1225 --json body,comments` (executed) | The issue has no comments. Its *Done when* asks that a link named as the argument be compared at its own path, as a scanned link is, with a case showing the refusal. |
| read: `seal/threads/1793457436-row-deletion-check-and-a-symlink/gaps.md` *Not done* and `trail/rounds/round-2.md` line 60 | #19 left this case open on purpose. Its round 1 defined the class as scanned paths, and an argument is resolved before the scan. The memo suggests resolving only the argument's directory. The second probe row below shows that suggestion fails an existing case. |
| executed: `grep -n 'real(' skills/verify/scripts/unverified_check.py` | Five sites read an argument through `real()`, which resolves every link on the path: `#overviews` (line 943), and in `#main` the repository root (line 1569), the other-volume refusal (line 1608), the typo check (line 1626) and the presence arm's prefixes (line 1708). The list is whole because it is built from the one function that produces the defect. |
| read: `skills/verify/scripts/unverified_check.py#overviews`, `#unique_by_target` and `#main` | `#overviews` resolves each argument with `real()` before it walks. The second arm of `#main` (lines 1680–1706) compares a path at its own name only where `os.path.islink(path)` is true. A named link therefore reaches the scan as its target's path, and the arm never sees it. The presence arm builds its prefixes from the same resolved argument, so the link's own path is outside every prefix. |
| executed: `sh <scratch>/test_tmp_probe.sh` against `unverified_check.py` at 4da937fa, in a `git clone --no-local` of this branch. Each fixture has `specs/a/gaps.md` with 2 rows and `specs/b/gaps.md` with 1 row at the base, then the change shown, run with `--baseline HEAD` | P1, `specs/a/gaps.md` replaced by a link to `../b/gaps.md`: named `specs/a/gaps.md` EXIT=0; named `specs/a` and scanned `specs` both EXIT=1 with `specs/a/gaps.md:1  2 rows at HEAD, 1 here`. P2, the directory `specs/a` replaced by a link to `b`: named `specs/a` EXIT=0; scanned `specs` EXIT=1 with `present at HEAD and not here`. P3, the same tree, named `specs/a/gaps.md`: EXIT=0. P8, the link pointing at a 1-row memo outside every repository: EXIT=2 with `--baseline HEAD needs a git repository, and specs/a/gaps.md is not in one`, although the link stands in one. P7, the link pointing at a 1-row memo in a second repository, and Q1, `specs/a` replaced by a link to a directory of a second repository: EXIT=0, because the root and the base come from the second repository. Unchanged and correct: P5 (a link at the base and now), P6 (a directory link at the base and now) and P9 (a named link whose target holds as many rows as the base did) EXIT=0; P4 (the argument is a link to the repository's top, a row dropped) EXIT=1. |
| executed: the same probe against a scratch copy that resolves only the argument's directory, in `#overviews` and in the prefixes (#19's suggestion) | P1 EXIT=1. P2 and P3 stay EXIT=0, because the arm still asks `os.path.islink` of the file alone. With `specs/a/gaps.md` deleted and the run naming a link to the repository's top, it exits 0 where 4da937fa exits 1. The kept link component makes the presence arm's prefix `../<link>`, which matches no line of `ls-tree`. That is the failure `tests/skills/test_unverified_check.py#Test_main::test_refuses_a_deletion_reached_through_a_linked_path` pins in its `a file` case. |
| executed: the same probe against a scratch copy that takes the repository from the deepest link on the path | P7 and Q1 exit 1. A repository reached through a link that stands in a second repository, with a row dropped, exits 2 where 4da937fa exits 1: the root became the second repository, and `HEAD` was resolved there. That layout is the one `#real`'s docstring exists for, one level up, such as a checkout linked from a home directory that is itself a repository. |
| executed: the same probe against a scratch copy of the chosen approach (Scope items 1 to 3) | P1, P2, P3 and P8 exit 1, each with `specs/a/gaps.md:1  2 rows at HEAD, 1 here`. P8 also lists the target under `not compared` with the outside-the-repository reason. P4, P5, P6, P7, P9 and Q1 keep their exits. The scanned runs of P1, P2 and P8 keep theirs. The deleted memo reached through a link to the top, and the repository reached through a link in a second repository, still exit 1. |
| executed: `git ls-tree HEAD -- specs/a/gaps.md` and `git show HEAD:specs/a/gaps.md` where `specs/a` is a tracked directory link (P6) | `ls-tree` prints nothing and exits 0, so `#mode_at` answers None. `show` exits 128, so `#compare_at` answers None. A path that passed through a link at the base therefore compares nothing there, and the widened arm (Scope item 3) needs no new skip for it. |
| executed: `git -C <P2>/specs/a rev-parse --show-prefix` | Prints `specs/b/`. git answers with links resolved, so git cannot tell the check the path as the person named it. The check has to keep that path itself. |
| read: `tests/skills/test_unverified_check.py` | The cases that pin what this work keeps: `Test_main::test_refuses_a_deletion_reached_through_a_linked_path` (a link to the repository's top), `Test_main::test_refuses_a_row_deleted_through_a_tracked_link_naming_the_real_file`, `test_refuses_a_memo_replaced_by_a_link_to_one_holding_fewer_rows` and `test_accepts_a_tracked_link_counted_once_and_not_deleted` (scanned links), `Test_overviews::test_accepts_every_overview_under_a_path_once_skipping_build_output` (a directory in no repository, read as its real path), and `Test_real`. Links are made through `tests/conftest.py#symlink_or_skip`. |
| read: issue #1235 (`gh issue view 1235`, executed) | It edits the comment at `skills/verify/scripts/unverified_check.py` line 113, the one that names `overwide_rows`. No line this work changes is near it, so that comment stays as it is. |
| read: `seal/follow-up.md` | No row waits on this check, so no row joins this scope. |
| read: the `### Process changes` table of the latest GitHub Release (`gh release view`, executed), and `seal/threads/*/changelog.md` | No process row bears on this check. No fragment under `seal/threads/` holds a `### Process changes` section. |
| read: `docs/the-record-layout.md` *A change writes fragments, never a shared file*, and `.claude-plugin/plugin.json` | The work owes `seal/threads/1793504229-a-linked-memo-named-as-the-argument/changelog.md` with a `### Fixed` entry, because a person sees a new refusal. No file that section names changes, so no `### Process changes` section is owed. The version already reads 0.27.1, so no version move is owed. |

## Scope

In:

1. **One reader turns an argument into the path the check compares.** It resolves the links on the way to the repository's top. It keeps every component inside the repository as the person named it. A path in no repository is read as its real path, as now. All five sites the Grounding lists read the argument through this reader, and no site reads an argument through `real()` directly after this work.
2. **The repository is still the one the argument's real path is in.** Only where the real path is in no repository is it the repository that holds the deepest link on the path (P8). The root, and so the base, come from that repository.
3. **The second arm compares every path reached through a link inside the repository at its own path.** Its condition widens from "the file is a link" to "the path is not its own real path". A path that was a link, or passed through one, at the base still compares nothing there (Grounding, the `ls-tree` row).
4. The text that states the old reading is rewritten in place: `#real`'s docstring sentence "Every path this compares has to come through here", the comment in `#overviews` that says the argument is resolved once, the comment above the second arm in `#main`, and the sentence of `#unique_by_target`'s docstring that says a link whose own path held a file is read there by `main`.
5. Cases in `tests/skills/test_unverified_check.py`, each shown red against 4da937fa's script before it is committed:
   - a named file link whose target holds fewer rows than the base held at the link's path: exit 1, the line naming the link's own path (the issue's *Done when*);
   - the same through a named directory link, and through a named file under a linked directory;
   - a named link whose target lies outside every repository: exit 1, with the target under `not compared`;
   - a named link whose target holds as many rows as the base did: exit 0;
   - a unit case for the reader of item 1, beside `Test_real`.
6. The changelog fragment, `seal/threads/1793504229-a-linked-memo-named-as-the-argument/changelog.md`, under `### Fixed`. It states each run that now exits 1, and the corrected exit for P8.

Out:

- **A link inside one repository to a memo in a second repository** (P7 and Q1). It still exits 0 where the target lost nothing against the second repository's base. The base is read in the repository the real path is in, so the link's own path in the first repository is never compared. Taking the repository from the link instead breaks a layout that works now (Grounding, the deepest-link probe row). Comparing in both repositories breaks `#main`'s rule that every argument is compared against one repository. No layout of the plugin puts a closing memo's link into another repository. The builder names this in `gaps.md` *Not done*.
- **A scanned directory link** (P2 scanned). The walk does not enter a linked directory, so the presence arm reports `present at HEAD and not here`, even where the target holds every row. That is a refusal, not a pass, and the issue does not report it. Changing it means following links in the walk, which changes what every scanned run reads.
- **The other readers that take a path from a person and resolve it.** The issue names only this check. #19's frame listed the other `git show` readers and left them out on grounds that still hold (`seal/threads/1793457436-row-deletion-check-and-a-symlink/frame/design.md` *Scope*, *Out*).
- **Naming the skipped link cases on Windows.** That is #1221's.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A named link to a smaller memo | Given `specs/a/gaps.md` held 2 rows at the base and is now a link to a memo of 1 row. When `seal unverified --baseline <ref> specs/a/gaps.md` runs, then it exits 1 with `specs/a/gaps.md:1  2 rows at <ref>, 1 here`. | the first case of Scope item 5, seen red at 4da937fa (P1 exits 0 there) |
| A named directory link | Given the directory `specs/a` held a 2-row memo at the base and is now a link to a directory whose memo holds 1. When the check runs on `specs/a`, or on `specs/a/gaps.md`, then each exits 1 with the same line. | the second case of Scope item 5, seen red at 4da937fa (P2 and P3 exit 0 there) |
| A named link out of every repository | Given the link points at a smaller memo outside every repository. When the check runs on the link, then it exits 1 with the same line, and lists the target under `not compared` with the reason `the file lies outside the repository, so no commit of the repository holds it`. | the third case of Scope item 5, seen red at 4da937fa (P8 exits 2 there) |
| A named link that lost nothing | Given a named link whose target holds as many rows as the base held at the link's path. When the check runs, then it exits 0. | the fourth case of Scope item 5 |
| A tree reached through a link | Given a run that names a link to the repository's top, or a path through a link inside the repository, with a row dropped, or with a memo deleted. Then it exits 1, as a run through the top's link does now. | `test_refuses_a_deletion_reached_through_a_linked_path`, unchanged and green; `Test_main::test_refuses_a_memo_deleted_behind_a_link_inside_the_repository` |
| Scanned links keep their reports | Given the scanned link cases #19 added. Then each keeps its exit and its line. | the `Test_main` cases the Grounding names, unchanged and green |

## Data & interfaces

- A new function beside `skills/verify/scripts/unverified_check.py#real` takes an argument and returns the path the check compares: the repository's top, resolved, joined to the components the person named inside it. The crafter names it. The shortest prefix of the absolute argument whose real path is the repository's top marks where the named components start. Where no prefix resolves to the top, it returns the real path, as `real()` does.
- The repository is found by Scope item 2's rule: `#repo_root` of the real path of the argument's nearest existing ancestor, as now. Where that answers None, the probe's version walks up from that ancestor, asks `#repo_root` about the resolved directory of each link it meets, and takes the first answer.
- `#overviews(paths)` keeps its signature and calls the new function where it calls `real()` now. `#reference_rule` then receives a path inside the repository, and its `repo_relative` forms still hold.
- `#main`: the root (line 1569), the other-volume refusal (line 1608), the typo check (line 1626) and the prefixes (line 1708) read the argument through the new function, and the root through Scope item 2's rule. The second arm (line 1688) skips a path only where `os.path.realpath(path) == path`.
- What a person sees changes in two ways. A run that names a link to a smaller memo, or names a path through a linked directory, now exits 1, and the deletion line names the path as typed. A named link to a file outside every repository no longer exits 2 with `is not in one`; it is compared at its own path, and the target is listed under `not compared`.

## Rule changes

- nothing
  why: The policy already says a `## Not verified` table that lost rows against the merge base fails the run (`docs/the-record-layout.md` *The fold, and what tells it from a deletion*). This work makes the code meet that rule when the named path is a link. How the check reads an argument is a property of the script, stated in its docstrings.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| Reading an argument through `real()`, at five sites | `skills/verify/scripts/unverified_check.py#overviews` and `#main` | The new reader of Scope item 1, which every site calls. |
| The claim that every compared path comes through `real()` | `skills/verify/scripts/unverified_check.py#real` | The docstring is rewritten in place: `real()` is what the new reader uses for the part of a path that leads to the repository. |
| The comment that the argument is resolved once and nothing below it is | `skills/verify/scripts/unverified_check.py#overviews` | The comment is rewritten in place to say what the new reader keeps. Its reason, that `ls-tree` lists a tracked link under its own path, stays. |
| The second arm's test `os.path.islink(path)`, and the comment that says only a link is compared at its own path | `skills/verify/scripts/unverified_check.py#main` | The widened condition of Scope item 3, and its comment rewritten in place. |
| The `#unique_by_target` docstring sentence on a link whose own path held a file | `skills/verify/scripts/unverified_check.py#unique_by_target` | The same sentence, rewritten to name a path reached through a link. |

Framed 2026-11-01 by framer, before the build.

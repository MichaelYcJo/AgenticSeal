# Design: 1793443708-settle-keeps-a-gaps-file-anywhere

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A script holds a gate only on a fact it reads exactly ... It names as not read a line or a file that looks like one of its form's and is not one, and decides nothing on it." and "A reading that is noisy or guessed from words is reported, never used to block." | The form of the closing memo is `gaps.md` at the work item's top (`docs/the-record-layout.md` *seal/threads/<work-item-id>/*, `hooks/lib/optin.py#GAPS`, read). A `gaps.md` anywhere else looks like the form and is not it. The settle names it as a file it did not read and decides nothing on it: it does not read its rows, and it does not keep the directory for it. Keeping the directory would take the file's name as a guess that it holds open rows, and use that guess to hold the settle at exit 1. `frame/plan.md` A1 and A2 weigh the two shapes. |
| `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md` *Table D*, the #1126 row: "Kept for 0.26.1; the fix is naming the `gaps.md` the script did not read, not keeping the directory on a guess" (read) | #1167's frame decided this shape for #1126 when it wrote the core sentence above, and 0.26.0 released it. This frame builds that decision and does not argue it again. The issue's first *Done when* line asks for the other shape, the directory kept. The core and that decision outrank the ticket (`skills/implement/SKILL.md` *1.*), so the build names the file and does not keep the directory, and the pull request body says so against the issue. |
| `skills/settle/SKILL.md` *What this does not do*: "The script does not judge. ... what each row is are the settling session's" | What a misplaced file holds is a question of meaning, so the settling session answers it. The script's part is to put the file in front of the session in the dry run, the one reading before `--apply` removes it. |
| `skills/settle/SKILL.md` *What the dry run shows*, *The judgments*: "A heading whose letters, case folded, are the section's and that is not it is named as not read at its line ... `--apply` removes the plans, so this is the one reading the rows get." (read) | The same script already names a near-miss as not read in the dry run and removes the directory at `--apply`. This work gives the misplaced record file the same treatment. |
| `docs/the-record-layout.md` *The fold, and what tells it from a deletion*: "A released work item leaves at the settle whatever it wrote, and the settling session decides every open row of its record before it goes." | Kept. The rule gains the misplaced file in `## Rule changes`. The directory still leaves once its record at the top holds no open row. |
| `docs/what-a-script-gates.md` *The checks*, the `seal settle` row, as #1167's pending `add` states it (`seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md` `## Rule changes`, read) | Policy in force through an unsettled design. The row's *Unread* cell says what the settle names. It gains the misplaced record file in `## Rule changes`, since that document says "a row that drifts is found when that script's home is read". |
| The reprobe at the base, `5560c742` (executed): a scratch repository holding three released work items on `main`, each with the same open row, in `gaps.md`, `trail/gaps.md` and `frame/gaps.md`. The command was `python3 <clone>/skills/settle/scripts/settle.py --root <repo> --released-at main [--apply]`, from a `git clone --no-local` of this worktree checked out at `5560c742` | The dry run exited 0 and named neither misplaced file. `--apply` exited 1: it kept the top-level one, "kept ... holds 1 open row", and printed `removed seal/threads/1700000002-trail/` and `removed seal/threads/1700000003-frame/` with nothing else about either. #956's R31 still stands at the base. |
| History (executed): `git log --all --name-only` over `seal/threads/*`, `seal/specs/*` and `specs/*` for a `gaps.md`, `design.md` or `plan.md` at a path other than the record's own or the earlier top-level layout, and `git ls-files 'seal/threads/*'` for the same at the base | None, in either. No work item has written a misplaced record file. #956's probe (`53f21b54^:seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-3.md`, R31, read) is the only instance. So the change must stay cheap: it is a report that blocks nothing (`frame/plan.md` A2). |
| `unverified_check.py#open_record_rows` and its two calls in `skills/settle/scripts/settle.py` (`#open_rows`, `#apply`, read); #1198's diff `15a5ce66...feat/1198-fields-stand-in-marked-blocks` (executed, `git diff --name-only`) | #1198 edits `skills/verify/scripts/unverified_check.py`. It does not edit `settle.py`, `skills/settle/SKILL.md`, `tests/skills/test_settle.py` or `README.md`. This work leaves `unverified_check.py` and `open_record_rows`'s interface unchanged. Its code goes in `settle.py` only, so the two branches share no file. |
| The ticket, #1126 (executed, `gh issue view 1126 --json body,comments`, 2026-10-31): no comments; milestone 75, `release: 0.27.0`. `.claude-plugin/plugin.json` reads `0.27.0` at the base (read) | The release is 0.27.0 into `release/v0.27.0`. The version does not move. |

## Scope

In.

1. **The settle names each misplaced record file in a work item's directory.** A misplaced record file has the basename of one of the three files the settle reads in a work item's directory, `gaps.md`, `frame/design.md` and `frame/plan.md`, and stands at any other path in that directory. Examples: `trail/gaps.md`, `frame/gaps.md`, a top-level `design.md`, `trail/plan.md`. The three are derived from the constants the settle already reads by, `unverified_check.py#OVERVIEW`, `settle.py#DESIGN` and `settle.py#PLAN`, so no list of names is kept beside them. The match is the exact basename. No other spelling is read, and no file's content is read. The walk covers every regular file and every link to a file under the directory. It does not follow a linked directory. It reads the directory where `--apply` removes it: the repository's top in shared mode, and under the common git directory in local mode.
2. **The dry run lists them.** A section of its own follows the open rows. Its heading says that the files are named like a record the settle reads, stand away from that record's place, and were not read. It also says that the settling session opens each one, and that `--apply` decides nothing on it and removes it with its directory. Each line gives the file's path from `seal/threads/` and the record it is named like. The dry run prints the section only when it holds a line. Its exit code is 0, as before.
3. **`--apply` names them and decides nothing on them.** `--apply` reads the misplaced files from the tree again, as it reads the rows (`settle.py#apply`'s docstring). The directory is removed or kept on its top-level record's rows, as now. Under the `removed` or `kept` line, one `not read:` line names each misplaced file. The exit code and the last line's counts do not change.
4. **`skills/settle/SKILL.md` says it, in place.**
   - *What the dry run shows* gains the section.
   - *The settling session's procedure* step 4: the session opens each named file and decides each item in it that reads as an open row, as the step decides a row (moot, answered, or re-homed to an issue). It writes nothing into the file, since `--apply` removes it.
   - *What `--apply` does*: it names the files and decides nothing on them.
   - `settle.py`'s module docstring says the same.
   - `README.md`'s `seal settle [--apply]` row names the section among what the dry run prints.
   Every other statement of what the dry run lists or `--apply` keeps is found with `git grep` and changed in the same commit (contract rule 19). `docs/` changes only through `## Rule changes`.
5. **Cases in `tests/skills/test_settle.py`, each seen red by reverting the fix (contract rule 15), with the texts a person reads pinned (contract rule 14).** They are the scenarios below.
6. **The release.** It is a `fix:`: the settle lost a record's rows without a word. It goes into milestone 75 on `release/v0.27.0`. `changelog.md` holds the fix under `### Fixed`, and one `### Process changes` row: the settling session opens each file the dry run names as not read before `--apply`. The pull request does not close #1038, and says how this work differs from the issue's first *Done when* line (the second row of *Grounding*).

Out.

- **Keeping the directory for a misplaced `gaps.md`, as the issue's first *Done when* line asks.** `frame/plan.md` A1 rejects it, and *Grounding* rows 1 and 2 give the grounds.
- **Reading a misplaced `gaps.md`'s rows as a record.** `frame/plan.md` A3 rejects it: that would make a second place for the closing memo without saying so.
- **`seal unverified` at the pull request, and the other readers that read a record at one path and say nothing of one at another** (#956's R11 and R25). #1038 holds the question of one reader for that class, and this work does not settle it. The misplaced file is still unread at the pull request, so the settle is where this work puts it in front of a reader.
- **`unverified_check.py`.** #1198 edits it, and this work's code needs nothing from it beyond `OVERVIEW`.
- **Other spellings**, such as `Gaps.md` or `gaps.ko.md`. No script carries a list of spellings (`skills/core/SKILL.md`). The domain of spellings is unbounded, so the exact-basename class is the whole class this script can list (contract rule 12).
- **`routing.md` and `trail/rounds/` written elsewhere.** The settle reads `routing.md` only in local mode, and only to decide whether a work item was released. A misplaced one leaves the item unreleased and kept, so nothing is lost. `trail/rounds/` is read for a count only, and no row of it is carried forward.
- **`docs/release-checklist.md` *2b*.** It cites `skills/settle/SKILL.md` as the procedure, and nothing it states becomes false.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 An open row in `trail/gaps.md` (#956's R31) | Given a released work item whose only `gaps.md` is `trail/gaps.md` holding an open row, when `seal settle` runs, then the new section lists `seal/threads/<id>/trail/gaps.md` as named like `gaps.md` and not read, at exit 0; when `--apply` runs, then the directory is removed, and the `removed` line is followed by a `not read:` line naming `trail/gaps.md`, at exit 0 | a case in `tests/skills/test_settle.py`, seen red by reverting the fix: at `5560c742` the probe printed neither line |
| S2 A misplaced copy beside the record | Given a released work item with a top-level `gaps.md` holding an open row and a `frame/gaps.md` holding none, when `--apply` runs, then the directory is kept on the top-level row, at exit 1, and the `kept` line's rows are followed by a `not read:` line naming `frame/gaps.md` | the same module, seen red |
| S3 The class, not the coordinate | Given released work items holding a top-level `design.md` and a `trail/plan.md`, when `seal settle` runs, then each is listed as named like `frame/design.md` or `frame/plan.md` and not read | the same module, seen red |
| S4 Nothing misplaced | Given the existing fixtures, where every record stands at its place, when the dry run and `--apply` run, then neither prints the section or a `not read:` line, and every existing case passes unchanged | the module's existing cases, run at the phase boundary |
| S5 Local mode | Given a local root with a released work item holding `trail/gaps.md`, when `--apply` runs, then the directory under the git directory is removed and the file is named | a case beside `test_apply_in_local_mode_removes_under_the_git_directory_alone`, seen red |

## Data & interfaces

- `skills/settle/scripts/settle.py`: one function that reads a work item's directory under `records` and returns the relative paths of its misplaced record files, each with the place it is named like, sorted. `survey` adds its result to `found` for `report`. `apply` calls it again from the tree. One heading constant holds the dry run's section text, and one line format holds the `not read:` line. The exit codes, the summary lines and `open_rows`'s return shape do not change.
- `skills/verify/scripts/unverified_check.py`: unchanged. Only `OVERVIEW` is read from it, through the loader `settle.py` already uses.

## Rule changes

- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: A released
    work item that wrote no `frame/design.md` states no rule and goes the same way.
  to: A released
    work item that wrote no `frame/design.md` states no rule and goes the same way.
    A file in its directory with the name of a record the settle reads, a
    `gaps.md`, a `design.md` or a `plan.md`, at any path but that record's
    own, is named by the dry run and by `seal settle --apply` as a file the
    settle did not read. The settling session opens it and decides each item
    in it that reads as an open row, as it decides a row. `--apply` decides
    nothing on it and removes it with the directory. Keeping the directory
    for it would take a file's name as a guess at what it holds.
- change
  file: docs/what-a-script-gates.md
  section: The checks
  from: a heading near *Judgments of the run* is named, and a `trail/rounds` it cannot list is named
  to: a heading near *Judgments of the run* is named, a `trail/rounds` it cannot list is named, and a file in a work item's directory with the name of a record it reads, at another path, is named and removed with the directory

## Removes

- nothing
  why: The work adds a report, and nothing in the tree stands on the fact it changes. No reader before it named a misplaced record file, so no check, exception or copy goes. The report blocks nothing and changes no exit code, so it is no gate that would owe a removal in return.

Framed 2026-10-31 by framer, before the build.

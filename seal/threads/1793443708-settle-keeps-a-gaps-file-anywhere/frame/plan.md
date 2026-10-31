# Implementation Plan: 1793443708-settle-keeps-a-gaps-file-anywhere

## Technical context

The settle reads three files in a work item's directory, each at one path. The paths, read at the base `5560c742`:

- The closing memo is `unverified_check.py#OVERVIEW` (`skills/verify/scripts/unverified_check.py:130`, `gaps.md`). It is read through `open_record_rows` (`:1325`), which opens `<directory>/gaps.md` and nothing else.
- The design is `settle.py#DESIGN` (`skills/settle/scripts/settle.py:116`, `frame/design.md`). It is read by `timeline` (`:598`), at `--released-at` where the root is shared.
- The plan is `settle.py#PLAN` (`:119`, `frame/plan.md`). It is read by `judgments` (`:503`).

`open_rows` (`:474`) and `survey` (`:699`) feed the dry run's `report` (`:809`). `apply` (`:950`) reads the tree again, keeps a directory whose top-level record holds an open row or cannot be read, and removes the rest with `shutil.rmtree`. A file with one of those names at any other path is read by none of them, and `--apply` removes it without a word. The reprobe in `frame/design.md` *Grounding* shows this (executed).

The change adds one reader of the directory's file names to `settle.py`, and two places that print what it found. The shape of the change is decided in `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md` *Table D*: name the file, and do not keep the directory on a guess.

The failure scenario of the chosen approach, in six months:

- A settling session runs `--apply` without opening a file the dry run named. The file leaves with its directory, and so does any open row in it. In shared mode the settle's pull request shows the deletion, and the release tag still holds the file. In local mode nothing holds it once it is removed; the dry run already names `seal export` for a copy. Nothing stops a session that skips the section. The procedure's step 1 runs the dry run first, and step 4 is where the session decides what the file holds.
- A later change makes the settle read a fourth file in the directory and does not add its constant to the reader's tuple. A misplaced copy of that file is then not named. The tuple sits beside `DESIGN` and `PLAN`, where that change has to touch.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 Keep a directory that holds a `gaps.md` anywhere but at its top, naming the file (the issue's first *Done when* line) | A copy that holds nothing open holds the settle at exit 1 on every run until a person moves or deletes it. Examples: a template copied by mistake, a memo quoted in a phase record's directory, a closed memo left beside the real one. The script would be deciding on a file name, a reading guessed from a word, and using it to block, which `skills/core/SKILL.md` *The rule a mechanism is kept against* says a script never does. Keeping the directory also tells the session nothing it would not learn from the dry run's line: the session still has to open the file. The catch record of the kept directory is one audit probe and no work item (`frame/design.md` *Grounding*, the history row) | Rejected. #1167's *Table D* already decided this shape against keeping, and this frame builds that decision. The ticket ranks below the core (`skills/implement/SKILL.md` *1.*) |
| A2 Name each misplaced record file in the dry run and at `--apply`, and decide nothing on it: the directory goes or stays on its top-level record alone (chosen) | The first failure scenario under *Technical context*: a session that skips the named section loses the file's rows. The premise that the session reads the dry run before `--apply` was checked in `skills/settle/SKILL.md` *The settling session's procedure*, steps 1, 4 and 7 (read) | Chosen. It meets the core's sentence word for word, it is the same handling the script already gives a heading near *Judgments of the run*, and it blocks nothing for a file whose meaning is the session's to judge |
| A3 Read a misplaced `gaps.md`'s rows as the record, keeping the directory while any is open (replace the fixed-path structure with discovery) | The closing memo would get a second place, declared nowhere. `seal unverified` at the pull request still reads the top-level file alone, so two readers would disagree about where the record is, and the misplaced file would pass the pull request and block the settle. Every reader of the layout would owe the same widening. The premise that keeps the fixed path was checked: `docs/the-record-layout.md` *seal/threads/<work-item-id>/* places `gaps.md` at the thread's top, and `hooks/lib/optin.py#GAPS` holds it once for every reader (read) | Rejected |
| A4 Name every file in the directory that the layout table does not list | It needs a copy of `docs/the-record-layout.md`'s table in code, and that copy drifts each time the layout changes. It also names files the settle never reads, which nothing in them depends on | Rejected |
| A5 Name a misplaced `gaps.md` alone, the coordinate the issue gives | The same cause leaves a misplaced `design.md` or `plan.md` unread: a top-level `design.md` from before the session-start move, or a plan under `trail/`. Their rule changes or judgments then leave unread, the defect contract rule 12 asks to be fixed as a class | Rejected. The class is built from what produces it, the three paths the settle reads, so the list is whole for this script |
| A6 Put the reader in `unverified_check.py`, so `seal unverified` names the file at the pull request too | That is the one-reader question for #956's R11, R25 and R31, which #1038 holds. #1198 is editing `unverified_check.py` at the same time | Rejected for this work; #1038 decides it |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 6 | The cases for S1, S2, S3 and S5 in `tests/skills/test_settle.py`, each seen red with the fix reverted in `settle.py`, the printed texts pinned. S4: the module's existing cases pass unchanged. `tests/text/test_settle_reads_before_it_removes.py`, `tests/behaviour/test_settle_applies_rule_changes_in_place.py`, and every other module contract rule 2 names for a path the phase changes. `git grep` on the changed statements' words, run by contract rule 19. `chain_check.py --worktree` reads this design's `## Rule changes` without a refusal | 2c44e0ef |

## Operational impact

- The dry run gains one section, printed only when a released work item holds a misplaced record file. `--apply` gains `not read:` lines in the same case. No exit code changes, and no other line changes.
- No migration, no environment variable and no dependency is added. No released work item's directory holds a misplaced record file at the base (executed, `git ls-files 'seal/threads/*'`), so the next settle of this repository prints nothing new.
- `docs/the-record-layout.md` and `docs/what-a-script-gates.md` gain the rule at the settle after 0.27.0, through `frame/design.md` `## Rule changes`. Until then the policy in force is the documents plus those changes.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |

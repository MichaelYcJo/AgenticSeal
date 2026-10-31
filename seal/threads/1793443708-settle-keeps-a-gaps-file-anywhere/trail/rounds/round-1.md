# Review round 1: 1793443708-settle-keeps-a-gaps-file-anywhere

target: 1090b7c3 against origin/release/v0.27.0

## Findings

### 1. The settling session's new step and the new `--apply` bullet in the skill are pinned by no case

severity: should
location: `skills/settle/SKILL.md:246-250`, `skills/settle/SKILL.md:284-287`, `skills/settle/SKILL.md:188-195`, `tests/text/test_settle_reads_before_it_removes.py:107-131`, `tests/text/test_settle_reads_before_it_removes.py:153-155`
evidence: executed `git grep -n -F "Open each file the dry run names" -- tests evals`, `git grep -n -F "names each file the dry run names" -- tests evals`, `git grep -n -F "The files named like a record and not read" -- tests evals`
verdict: fixed a7bca714

The frame's chosen approach rests on one sentence of the skill. `frame/plan.md` A2 names its own failure scenario: a settling session that skips the dry run's new section loses the misplaced file's rows, because `--apply` removes the file and decides nothing on it. The only defence is the new paragraph of step 4 in `skills/settle/SKILL.md:246-250`, which tells the session to open each file the dry run names, to write nothing into it, and to name each decided item in the pull request body. The crafter's departure 3 adds the last clause.

No case reads that paragraph. The three searches above, over `tests` and `evals`, found nothing for the step-4 sentence, for the new *What `--apply` does* bullet at `:284`, or for the new dry-run bullet at `:188`. The module that owns the procedure does pin it clause by clause: `test_the_skill_states_the_settling_sessions_procedure` lists every step's clause and asserts that they stand in order, and its docstring records that round 4 of #1033 asked for each clause to be pinned. `test_the_skill_says_a_from_locates_and_is_no_precondition` pins the *What `--apply` does* section the same way. The printed heading and line of `settle.py` are pinned in `tests/skills/test_settle.py`. The procedure text the session acts on is not. A later edit of step 4 can drop the one sentence the design's failure scenario depends on, and every case stays green. `skills/code-review/SKILL.md` says that a claim a fix writes into a document closes when a test pins the document.

The fix adds the clauses to the existing list in order, and pins the two bullets. Each addition is seen red by deleting its sentence from the skill (contract rule 15).

```python
# tests/text/test_settle_reads_before_it_removes.py, in
# test_the_skill_states_the_settling_sessions_procedure's `steps`, after the
# "A row that fits more than one kind ..." entry:
        "A row that fits more than one kind takes the first that fits, in the "
        "table's order",
        "Open each file the dry run names as not read",
        "Write nothing into the file, since `--apply` removes it with its directory",
        "the pull request body names each such item with its kind and what "
        "closed it",
        "take a default and write it down",

# in test_the_skill_says_a_from_locates_and_is_no_precondition, after the
# two asserts on `apply`:
    assert (
        "It names each file the dry run names as not read, and decides nothing "
        "on it." in apply
    )
    assert "the directory's record at its place alone decides which" in apply
    shows = text.split("## What the dry run shows")[1].split("## ")[0]
    assert "The files named like a record and not read" in shows
```

answer: The finding holds, and 5c9a8b52 and a7bca714 fix it. Step 4's paragraph joins `test_the_skill_states_the_settling_sessions_procedure`'s ordered list as three clauses, as proposed. The two items went into a new case, `test_the_skill_says_a_misplaced_record_file_is_named_and_decides_nothing`, not into `test_the_skill_says_a_from_locates_and_is_no_precondition`, whose name and docstring are about `from` and the policy write. The proposed split of the dry run's section on `"## "` would also stop at the item above, which quotes `## Not verified`, so the new case cuts that section from the raw text at line-start headings. The class is every sentence this phase added to the skill and the READMEs. It was listed by taking apart `git diff -U0 a83ce23e..1090b7c3 -- skills/settle/SKILL.md README.md README.ko.md` (executed), which gives six places: the command block, the dry run's item, step 4's paragraph, `--apply`'s item, and the cheat-sheet row of each README. Every clause of all six is now pinned. The new case holds the command block and both items, and `test_both_cheat_sheets_carry_the_command` holds each edition's clause. Each of the 16 pins was seen red: `bin/seal mutate` deleted or cut its sentence in `skills/settle/SKILL.md`, `README.md` or `README.ko.md`, and the module failed on that pin's assertion, with the tree clean after each run (executed). The `settle.py` docstrings this phase changed are code text outside the class, and no case pins them, as none pins the rest of that dry-run paragraph.

### 2. The new `link` helper copies `tests/conftest.py#symlink_or_skip` and drops its missing-parent guard

severity: should
location: `tests/skills/test_settle.py:702-706`, `tests/conftest.py:626-647`
evidence: read `tests/skills/test_settle.py:702-706`, `tests/conftest.py:626-647`
verdict: fixed 851fb4cc

`tests/conftest.py#symlink_or_skip` is the suite's one statement of how a case makes a symbolic link: it asks by attempting the call, and it skips where the platform refuses. Its docstring also states why it first asserts that the link's parent exists. Every error of a misbuilt fixture is an `OSError` too, so without that assertion a fixture bug reads as "no privilege here" on a machine that has the privilege, and the case skips instead of failing.

The new `link` in `tests/skills/test_settle.py:702-706` makes the same call with its own `try`, and catches `OSError` without that assertion. It exists because the shared helper takes no `target_is_directory` argument, which the linked-directory case in `Test_misplaced::test_refuses_a_directory_a_link_to_nothing_and_another_spelling` needs on Windows. A misbuilt fixture in either `Test_misplaced` case would now skip on every platform, and `gaps.md` names the Windows run as the answer to whether these cases ran. The rule now stands in two places, and the copy lacks part of it (`skills/core/SKILL.md` *The rule a mechanism is kept against*: a fact has one source). The fix gives the shared helper the flag and removes the copy.

Precondition: `target_is_directory` matters on Windows alone, where a link to a directory must be made as one; POSIX ignores it.

```python
# tests/conftest.py
def symlink_or_skip(target, link, directory=False):
    """... (docstring as it stands) ...

    DIRECTORY makes the link as a directory link, which Windows needs for a
    target that is a directory and POSIX ignores.
    """
    parent = os.path.dirname(os.path.abspath(str(link)))
    assert os.path.isdir(parent), f"the link's parent does not exist: {parent}"
    try:
        os.symlink(target, link, target_is_directory=directory)
    except OSError as exc:
        pytest.skip(f"symbolic links are not available here ({exc})")

# tests/skills/test_settle.py: delete `link`, import the shared helper, and
# call it where `link` was called:
from conftest import symlink_or_skip

        symlink_or_skip(top / "gaps.md", top / "trail" / "gaps.md")
        symlink_or_skip(elsewhere, top / "linked", directory=True)
        symlink_or_skip(tmp_path / "nowhere", top / "notes" / "plan.md")
```

answer: The finding holds, and 851fb4cc fixes it as proposed. `symlink_or_skip` takes `directory=False` and passes it as `target_is_directory`, the copy `link` is gone, and the three calls go through the shared helper. Seen both ways with `bin/seal mutate tests/skills/test_settle.py`, deleting `(top / "trail").mkdir()` from `test_accepts_a_file_or_a_link_to_one_at_another_path` (executed). At e6c957da the case skipped as "this platform makes no symbolic link" and the mutation survived. At 851fb4cc it failed on `the link's parent does not exist`. The class is every copy of a conftest helper in the files this phase touched. It was listed from the helpers this phase added to `tests/skills/test_settle.py`, read from `git diff a83ce23e..1090b7c3 -- tests/` (executed), against the definitions in `tests/conftest.py` (read). `link` was one copy. `released_item` and `records_in_place` restated `conftest.py#write`, which makes a file's parent directories and writes its text, so both now call `write` in the same commit. `not_read` has no counterpart in conftest. This module's own `git` and `commit` resemble conftest's `git_out` and `commit_everything`, but they stood there before this phase (a83ce23e), so they stay. `tests/text/test_settle_reads_before_it_removes.py`, touched by finding 1's fix, gained no helper. The modules that call `symlink_or_skip` or name `conftest.py`, with the two changed modules and `tests/skills/test_test_layout.py`, ran green: 24 modules, 2192 passed and 3 skipped, and neither changed module skipped (executed).

## Confirmations

confirms: none
The build holds to `frame/design.md` *Scope* item 1. `settle.py#misplaced` at `skills/settle/scripts/settle.py:519-542` derives the three names from `reader.OVERVIEW`, `DESIGN` and `PLAN`, matches the exact basename, keeps a name only where `os.path.isfile` holds, walks without `followlinks`, and walks under `records`, which is the repository's top in shared mode and the common git directory in local mode (read). The crafter's class claim (contract rule 12) was checked against `settle.py`'s reads: `OVERVIEW` through `open_record_rows` and `closed_rows` (`:995`), `DESIGN` through `has_spec` (`:347`) and `timeline` (`:661`), `PLAN` through `judgments` (`:574`), `routing.md` only in local mode, and `trail/rounds` only for a count (read). `unverified_check.py#open_record_rows` at `skills/verify/scripts/unverified_check.py:1325` opens `gaps.md` alone (read). The list is built from what produces the defect, and the design's *Out* covers the two other reads. `git ls-files` finds no misplaced record name in any tracked work item (executed), so the next settle of this repository prints nothing new, as `frame/plan.md` *Operational impact* says.

confirms: none
*Scope* items 2 and 3 hold. The dry run prints `MISPLACED_HEADING` after the open rows and only where a line exists (`settle.py:920-925`). `--apply` computes the misplaced files from the tree before `shutil.rmtree`, writes the `not read:` lines after the open rows under `kept` and right after the `removed` line, and changes neither the exit code nor the count line (`settle.py:1020-1042`, read). The texts a person reads are pinned: the heading's clauses in `Test_report::test_names_a_gaps_md_away_from_its_place_as_not_read`, and the line format through the test's own `not_read` helper in every S case (read). `bin/test tests/skills/test_settle.py tests/text/test_settle_reads_before_it_removes.py -q` at 1090b7c3: 118 passed, none skipped (executed).

confirms: none
The cases are seen red. Claimed: seven cases failed against `settle.py` at a83ce23e, two of them on a missing name rather than on an assertion, with eight `seal mutate` runs supplying the assertion failures. Found: with `misplaced` made to return `[]` in a scratch clone, the six cases that expect a misplaced file failed, and the two that expect none passed, which is their expected result (executed, `## Probes`). With the `os.path.isfile` test removed, `test_refuses_a_directory_a_link_to_nothing_and_another_spelling` failed on the dangling link `notes/plan.md` (executed). That reproduces the second of the crafter's eight mutations. The other seven were carried, not re-run. The test diff adds cases and changes no existing one, so S4's "every existing case passes unchanged" holds (read, `git diff 5560c742..1090b7c3 -- tests/`). `bin/seal layout --check tests` exits 0, and `seal layout --pairs` names no pair for `test_settle.py`, so the three cases beyond the frame's list are read against their class alone. Each covers what no other case covers: S4's absence, the link to a file, and the refused shapes (executed, read).

confirms: none
The four departures in `trail/phases/phase-1.md` hold on the grounds the crafter gives. Departures 1 and 2: `README.ko.md:259` and the command block at `skills/settle/SKILL.md:33-35` state the same list of what the dry run prints as `README.md:265`, so contract rule 19 brings them into the commit (read). Departure 3: a decision on an item in a file `--apply` removes would otherwise be written nowhere. Naming it in the pull request body follows step 9's handling of a row and `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* (read). Departure 4: covered in the confirmation above. The other statements a search of the changed words finds, `docs/release-checklist.md:44-48`, `seal/README.md` and `templates/setup/seal-README.md`, summarise the settle and remain true (read).

confirms: none
The frame's departure from the issue's first *Done when* line is stated where a reader of the issue meets it. Claimed: the pull request body says so (*Scope* item 6). Found: the changelog fragment's `### Fixed` entry ends by saying the issue asked that `--apply` keep the directory, and why it does not. `gaps.md` *Not done* opens with the same item. `skills/code-review/scripts/pr_body.py:11-14` copies the changelog fragment and `gaps.md`'s `## Not done` into the pull request body, so the release note and the pull request that closes the issue both carry it (read). The issue (`gh issue view 1126`, executed) holds no comment. Nothing on the issue page itself states the departure, and no agent may post one.

confirms: none
The labels are honest. `gaps.md` labels the suite, the lint and the format check `unverified` and names the orchestrator's `seal gate` as the answerer. The Windows row names the `windows-latest` legs of `.github/workflows/test.yml:105-108`, which exist. `tests/conftest.py:626-636` records that such a runner holds the symbolic-link privilege, so those legs run both `Test_misplaced` cases rather than skipping them (read). The changelog fragment's `### Process changes` row has the shape `templates/records/process.md` gives, and its source is an issue link, as the other fragments in the tree use (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite, the repository-wide lint and the format check (the `Broad gate` row) | `seal/config.md:10` | the orchestrator, by `seal gate --base origin/release/v0.27.0 --record 1793443708-settle-keeps-a-gaps-file-anywhere` |
| The crafter's 71-module boundary run, 3403 passed: an aggregate, not re-run; two of its modules were re-run here | `trail/phases/phase-1.md` *The phase-boundary set* | the orchestrator's broad gate |
| Whether the pull request closes #1126 while the issue's first *Done when* line is not met as written, or names the departure and leaves the issue for the owner to close | `frame/design.md` *Scope* item 6 | the orchestrator writing the pull request body, and the owner reviewing it |
| Both `Test_misplaced` cases run, neither skipped, on Windows | `gaps.md` *Not verified* | the `windows-latest` legs of `.github/workflows/test.yml` on the pull request |
| What `shutil.rmtree` does at `--apply` with a subdirectory of a work item that cannot be listed | `gaps.md` *Not done* | the settling session, at the next settle that meets one |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_settle.py tests/text/test_settle_reads_before_it_removes.py -q`, in a `git clone --no-local` of the worktree at 1090b7c3 | exit 0, 118 passed, none skipped |
| The same clone, `settle.py#misplaced` edited to return `[]` at its top, then `bin/test tests/skills/test_settle.py -q -p no:xdist -k "misplaced or away or names_a_misplaced or keeps_on_the_record or no_section_where"` | exit 1: 6 failed (both S1 halves, S2, S3, S5, `test_accepts_a_file_or_a_link_to_one_at_another_path`), 2 passed (`test_prints_no_section_where_nothing_is_misplaced`, `test_refuses_a_directory_a_link_to_nothing_and_another_spelling`); edit reverted |
| The same clone, `if place is None or not os.path.isfile(path):` edited to `if place is None:`, then `bin/test tests/skills/test_settle.py -q -p no:xdist -k Test_misplaced` | exit 1: `test_refuses_a_directory_a_link_to_nothing_and_another_spelling` failed, naming `notes/plan.md`; edit reverted |
| `bin/seal layout --check tests` and `bin/seal layout --pairs tests` in the same clone | both exit 0; 0 refused, and no pair names `test_settle.py` |
| `git grep -n -F` over `tests` and `evals` for the step-4 sentence, the `--apply` bullet and the dry-run bullet | each exit 1, no match |
| `git ls-files 'seal/threads/*'` filtered for a `gaps.md`, `design.md` or `plan.md` away from its place | no match |

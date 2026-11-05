# Design: 1793862998-seal-arms-is-run-by-nothing

## Grounding

Each row says how its fact was reached: `executed` is a command this framer ran at `fd294cc0`, `read` is a file it opened.

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | A mechanism stays only while what it caught outweighs what it costs. A change removes, in the same commit, every check, comment and copy that stood on the old fact. |
| G2 Issue #1393 (executed: `gh issue view 1393 --json title,body,comments,milestone`, no comments) | The owner decided on 2026-11-05 that `seal arms` leaves. The decision is not reopened here. The issue's *Done when* names the files that go, says `seal mutate` and its documents stop pointing at `seal arms`, and says #312, #313, #314, #315, #317, #687 and #710 close with this pull request. |
| G3 Milestone `release: 0.32.5` (executed: `gh api repos/MichaelYcJo/AgenticSeal/milestones/89 --jq .description`) | The decision comes first, as #1038 decided its verifiers. Where `seal arms` leaves, #1065 puts the whole suite on Python 3.14 in the job's place. #706 repairs `seal mutate`, which stays. Both are separate work items. |
| G4 `routing.md` (read) | Planning framer, Implementation crafter, Review through the review chain, Automation yes. |
| G5 `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | Which subject a work item has is the framer's judgment. A work item whose subject is the policy root's text edits `docs/` directly in its pull request. The decision for this item is G6 and G7, and `## Rule changes` below states it. |
| G6 `skills/settle/rule-changes.md` *A rule has one shape* and `.github/scripts/rules.py` lines 42 to 51 (read) | `seal rules --check` refuses a check line that names a path that is no file of the repository. It excuses only a line inside a section that a pending `remove` with no `from` takes out at the settle. A `change`, or a `remove` with a `from`, excuses nothing. `tests/github/test_rules.py#test_every_check_line_in_the_tree_holds` runs that check over the tree. |
| G7 `docs/running/the-broad-gate.md` *A check that cannot fail is not a check*, lines 170 to 178 (read) | Its first rule, that a module's arms are enumerated and the arms no case kills are reported, ends `check: skills/verify/scripts/arm_check.py tests/skills/test_arm_check.py`. Both files leave in this work, so a `remove` with a `from` would leave that line refused at HEAD until the settle. A `remove` with no `from` would take out the whole section, and its other rules stay. So the rule leaves `docs/` in this pull request. Work item `1793756609-an-enumeration-the-tree-does-not-hold` made the same call on the same grounds (read: its `frame/design.md` `## Rule changes`). |
| G8 `skills/verify/scripts/mutation_check.py` lines 105 to 111 and 135 to 177 (read) | `seal mutate` loads `arm_check.py` by path and takes three functions from it: `clear_bytecode_cache`, `restore` and `command_words`. Its call sites are lines 396, 411, 450, 554, 566 and 616 (executed: `grep -n`). Every call to `clear_bytecode_cache` passes `cwd`. |
| G9 `tests/skills/test_arm_check.py` lines 785 to 871 and 1400 to 1466, and `tests/skills/test_mutation_check.py` lines 1070 to 1105 (read) | Four behaviours of those three functions are held only in `test_arm_check.py`: `restore` raising when the bytes on disk do not hash to the original (`test_mutation_check.py`'s restore case replaces `restore` with a fake); `clear_bytecode_cache` removing a `.pyc` an import wrote; `clear_bytecode_cache` reading a `PYTHONPYCACHEPREFIX` against `cwd` when called alone, relative and absolute; and `command_words` keeping a backslash on Windows and escaping it on POSIX. No case of `test_mutation_check.py` names a Windows command line (executed: `grep -n` for `command_words`, `python.exe` and backslashes). |
| G10 `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py` lines 71 and 145 to 168 (read) | `reachable` maps a script to its subcommand through `seal.py#TOOLS` by the script's basename. Its cases at lines 337 to 344, 373 to 380 and 414 to 422 use `arm_check.py` with `seal arms` as their example of a script that has a subcommand, so they fail once `arms` leaves `TOOLS`. |
| G11 `.github/workflows/test.yml` lines 38 to 44 and 218 to 243 (read) | The `arms-grammar` job runs `pytest tests/skills/test_arm_check.py -q` at 3.13 and 3.14 and nothing else. The `pytest` job's comment explains the floor-only matrix by that job. `tests/behaviour/test_release_hygiene.py` lines 1015 to 1018 take the lowest `python: "x.y"` in the file as the floor, and with the job gone the lowest stays 3.12 (read). |
| G12 `skills/verify/scripts/broad_gate.py` lines 2143 to 2200 (read) | The gate's partition of CI steps reads named steps, and the `arms-grammar` job's steps carry no `- name:`, so the partition names none of them. |
| G13 `.test_durations` (executed: `grep -c "test_arm_check.py::"` gives 98, and `grep -n` gives two more parameter entries at lines 94 and 4315) | 100 entries price cases that leave. Pull request #1333 removed the entries of the cases it deleted (executed: `git show 94635718 -- .test_durations`). A case missing from the file still runs in one shard (read: `test.yml` lines 66 to 72). |
| G14 The class of statements that name the command (executed: `git grep -n -e "seal arms" -e arm_check -e arm-check -e arms-grammar -e seal-arms -e ONLY_ON_SOME_PYTHONS -e node-type -e "module's arms" -- ':!seal/threads'`) | This command made the list in *Scope* items 3 to 7. A search for the bare words `arm` and `arms` returns 35 KB of other meanings, such as the broad gate's arms and the chain check's arms, so that list is the command's output and not a word search. |
| G15 Earlier decisions (executed: `git show 14bfd992^:` the three phase records of `1793521558-the-record-decides-each-proposed-verifier`, #1038's work item; read: `test_arm_check.py` lines 222 to 238) | #1038's record holds no row on `seal arms`. The job came from #684 by S6 of work item 1790690762, so that 3.14's grammar change would be seen. The reason for the job is the tables in `arm_check.py`, and the tables leave with it. |
| G16 `agents/` (executed: `git grep -n "seal arms" -- agents`, no match; read: `agents/crafter.md` line 46) | No agent definition names `seal arms`. The crafter runs `seal mutate` over each unit that adds behaviour. |
| G17 Unsettled designs on the same documents (executed: `grep -n -A3` over `seal/threads/*/frame/design.md`) | `1793829111` changes `docs/running/the-broad-gate.md` *One act, one owner, and the owner is the orchestrator*. `1793843890` changes another paragraph of `docs/releasing/branch-and-release.md` *Work accumulates on a release branch*. This work moves no section and touches neither paragraph, so no operation is re-pointed. |
| G18 `seal/follow-up.md` and the process changes (read; executed: `gh release view --json body`, which holds no `### Process changes`, and a grep of each fragment's rows) | No follow-up row waits on this work. No process change row touches `seal arms`, `seal mutate` or this CI job. No `seal/parity.md` is declared. |

## Scope

In:

1. `skills/verify/scripts/mutation_check.py` holds `clear_bytecode_cache`, `restore` and `command_words` as its own functions, moved from `arm_check.py` with their docstrings rewritten to name `seal mutate` alone. The path loader `_sibling`, `ARM_CHECK` and `_ARM_CHECK` go. The module docstring's paragraphs that name `arm_check` or `seal arms` (lines 79, 100 and 105 to 111) and `_environment`'s docstring (line 492) say what stands now.
2. The four cases G9 names move into `tests/skills/test_mutation_check.py`, called against `mutation_check`'s own functions: `test_a_restore_that_did_not_land_stops_the_run`, `test_a_stale_bytecode_cache_cannot_decide_an_arms_verdict`, `test_a_windows_command_line_keeps_the_backslashes_of_its_paths`, and the part of `test_a_cache_under_a_pycache_prefix_is_cleared_where_the_cases_read_it` after the comment `# And the function on its own, as mutation_check.py calls it.`, with both parameters. Each moved case's name and docstring describe `seal mutate`'s use.
3. `seal arms` leaves: `skills/verify/scripts/arm_check.py`, `tests/skills/test_arm_check.py`, `skills/verify/seal-arms.md`, the `arms` entry of `skills/implement/scripts/seal.py#TOOLS`, and the `arms` parameter of `tests/skills/test_seal.py`'s tool table (line 3789).
4. `.github/workflows/test.yml` loses the `arms-grammar` job and its comment. The `pytest` matrix comment (lines 39 to 44) states the present: the suite runs at the floor alone, and whether a module's result depends on the interpreter has not been measured.
5. The policy root's statements of the command go, edited in place (`## Rule changes`): the first rule of `docs/running/the-broad-gate.md` *A check that cannot fail is not a check* with its check line; `seal arms` from the `seal layout --check` row of `docs/running/what-a-script-gates.md` *The checks*; and `arms-grammar` from `docs/releasing/branch-and-release.md` *Work accumulates on a release branch*, whose sentence then names the `pytest` job alone.
6. The other documents say what stands now: `skills/verify/SKILL.md`'s section `#### A module or a unit: ...` names `seal mutate` alone, under a heading that names only a unit; `skills/verify/seal-mutate.md` lines 11, 52 to 53, 105 and 116 to 117 stop naming `seal arms` and keep what they say of `seal mutate`; `CONTRIBUTING.md` lines 145 to 152 drop the job from the list of CI jobs.
7. The tests that named the command change: `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`'s three cases (G10) take `skills/verify/scripts/mutation_check.py` and `seal mutate` as their example, and the case at line 420 keeps its point with `seal mutate-length` and `unseal mutate`; `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py` drops `arm_check._lines` from S17 and its docstring line, holding the two copies that remain; `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py` drops the `"seal arms"` row; `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py` drops the `"seal arms"` pin at line 90 and rewrites its docstring lines 17 to 22; `tests/text/test_ci_gives_the_checks_what_they_need.py` lines 269 to 270 and `tests/skills/test_mutation_check.py` lines 542, 640, 737 and 1385 stop naming the module or the command.
8. `.test_durations` loses the 100 entries G13 counts.

Out:

- A Python 3.13 or 3.14 leg, or the whole suite on 3.14. That is #1065, a separate work item that runs after this one merges into `release/v0.32.5` (G3).
- The repairs #706 names in `seal mutate`'s restore after a refused or timed-out baseline. That is its own work item (G3). Scope item 1 moves `restore` into `mutation_check.py`, where #706 will find it.
- `seal unverified --baseline`, the milestone's second decision (G3).
- Records under `seal/threads/` that name `seal arms`. They state a past state, and history goes to the record (G1).
- Closing the seven issues. The pull request body's closing keywords are the orchestrator's, and *Done when* in #1393 names them.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The command is gone | Given the tree after the work, when a person runs `bin/seal --help` or `bin/seal arms`, then the help lists no `arms`, and the subcommand parser refuses `arms` as an invalid choice (read: `skills/implement/scripts/seal.py#main` hands over only a first word in `TOOLS`, and builds its subparsers from `TOOLS` and its own commands) | `tests/skills/test_seal.py`, whose tool table no longer names `arms`; the crafter runs `bin/seal arms` once and reads its exit code |
| S2 `seal mutate` behaves as before | Given `mutation_check.py` holding the three functions, when its cases and the four moved cases run, then all pass, and `mutation_check.py` opens no other script by path | `bin/test tests/skills/test_mutation_check.py tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py -q`; `grep -n "spec_from_file_location" skills/verify/scripts/mutation_check.py` prints nothing |
| S3 Nothing names the command | Given the tree after the work, when the command of G14 runs over everything outside `seal/threads/`, then it prints nothing and exits 1 | that command, run by the crafter at the phase's commit |
| S4 Every check line still holds | Given the rule and its check line gone from `docs/running/the-broad-gate.md`, when `seal rules --check` reads the tree, then no line names a missing file | `tests/github/test_rules.py` |
| S5 CI keeps its floor | Given `test.yml` with no `arms-grammar` job, when the floor case reads the file, then the lowest `python:` is still the floor | `tests/behaviour/test_release_hygiene.py`, `tests/text/test_ci_gives_the_checks_what_they_need.py` |
| S6 The script rule still sees subcommands | Given the cases of G10 rewritten to `seal mutate`, when they run, then each still fails against a reader that accepts any mention | `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py` |

## Data & interfaces

- `seal arms` stops existing as a subcommand of `bin/seal`. No other command changes its arguments, output or exit codes.
- `mutation_check.clear_bytecode_cache(path, cwd=None)`, `mutation_check.restore(path, original, original_sha)` and `mutation_check.command_words(text, windows=None)` keep the signatures and behaviour they had in `arm_check.py`. Only their module changes.

## Not covered until #1065

This note is for the crafter's `gaps.md` and is not scope. The `arms-grammar` job was the only CI leg that ran any case on Python 3.13 or 3.14 (G11). After this work no leg runs a Python newer than the floor, 3.12, until #1065 lands. The node-type tables in `arm_check.py` lose nothing by it, because they leave with the script. The four cases of *Scope* item 2 do lose a run: on 3.13 and 3.14 they tested `clear_bytecode_cache`, `restore` and `command_words`, which `seal mutate` calls, and after the move they run at 3.12 alone. #1065 answers this when it puts the whole suite on 3.14. The row's answerer is #1065's work item.

## Rule changes

- nothing
  why: This work item's subject includes the policy root's text, so it edits `docs/` directly in its pull request under `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*. The rule in `docs/running/the-broad-gate.md` *A check that cannot fail is not a check* names `skills/verify/scripts/arm_check.py` and `tests/skills/test_arm_check.py` in its check line, both of which leave here, and a `remove` with a `from` would leave that line refused by `seal rules --check` at HEAD until the settle (G6, G7). The other two `docs/` edits state facts of the tree, a table cell and a job name. No section moves, so no unsettled design's operation is re-pointed (G17).

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `seal arms` command | `skills/verify/scripts/arm_check.py` | Nothing replaces it. No agent runs it, and the crafter runs `seal mutate` over each unit that adds behaviour (G2, G16). Its three shared functions land in `skills/verify/scripts/mutation_check.py` (*Scope* item 1). |
| The command's cases | `tests/skills/test_arm_check.py` | They test a command that is gone. The four cases G9 names land in `tests/skills/test_mutation_check.py` (*Scope* item 2). |
| The command's document | `skills/verify/seal-arms.md` | The command is gone, and no other file opens it after *Scope* item 6. |
| The subcommand entry | `skills/implement/scripts/seal.py#TOOLS`, key `arms`; `tests/skills/test_seal.py`, the `arms` parameter | The script it ran is gone. |
| The CI job | `.github/workflows/test.yml`, job `arms-grammar` | It ran only `tests/skills/test_arm_check.py`, at 3.13 and 3.14 (G11). What leaves without cover until #1065 is in *Not covered until #1065* below. |
| The loader of a sibling script | `skills/verify/scripts/mutation_check.py#_sibling`, `ARM_CHECK`, `_ARM_CHECK` | The functions it loaded are `mutation_check.py`'s own. |
| The rule that a module's arms are enumerated and reported | `docs/running/the-broad-gate.md` *A check that cannot fail is not a check*, its first bold sentence through its check line | The mechanism it states is gone (G1, G7). The section's other rules stay. |
| `seal arms` in a check row | `docs/running/what-a-script-gates.md` *The checks*, the row opening `` `seal layout --check`, `seal arms` `` | The row keeps `seal layout --check`. |
| `arms-grammar` among the jobs a ruleset does not require | `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* | The job is gone; the sentence names the `pytest` job. |
| The job in the list of CI jobs | `CONTRIBUTING.md`, the paragraph opening `CI runs these jobs` | The job is gone. |
| The pointers from `seal mutate` to `seal arms` | `skills/verify/SKILL.md` *A module or a unit: `seal arms` and `seal mutate`*; `skills/verify/seal-mutate.md` *`seal mutate` asks condition 2 of one unit, one break at a time* | `seal mutate` stays and its file says what it does without the comparison. |
| A copy of the line splitter | `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py#test_every_copy_of_the_splitter_is_the_readers`, the `arm_check._lines` assertion | The copy leaves with its module. The case still holds the two copies that remain. |
| A census row | `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`, the `"seal arms"` key | The command it classifies is gone. |
| A pin on `seal mutate`'s file | `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py`, the `"seal arms"` item at line 90 | It pinned the sentence *Scope* item 6 removes. |
| Durations of cases that leave | `.test_durations`, the 100 entries of G13 | The cases are gone, and a moved case runs unpriced until the `durations` job measures it (G13). |

Framed 2026-11-05 by framer, before the build.

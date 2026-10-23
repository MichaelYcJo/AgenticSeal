# Feature Specification: tests rebuilt one file per module (#942)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against* | A test is a mechanism. A case stays while the mutation table shows what it kills that no other case kills. Nothing is kept beside the tree to stay in step with it, so a census's stored exception list goes where a fact in the code can replace it |
| `CLAUDE.md` *The goal a design is chosen against* | The checks this work adds fail on a fact they read and report the rest. A report never stops a pull request to ask |
| `CONTRIBUTING.md` *What a change to a gate must carry* | Removing the commit gate's text reading changes what the gate allows. That bar is why the removal is a person's decision in `questions.md` and not this work's default |
| `docs/the-commit-gate-inside-git.md` *Where each state of a repository stands* | Names the states only the PreToolUse reading judges: a foreign hooks slot and an opted-in clone no session has reached. These are what the reading catches that git cannot |
| `docs/the-reader-registry.md` *A frame names what its work removes* | `## Removes` below names every removal once |
| `docs/release-checklist.md` *5. The release pull request* | The release table is where the per-module rows land, and the sweep is a step of that section |
| `skills/settle/SKILL.md` *Rule changes* | The grammar `## Rule changes` below is written in |
| `skills/agent-contract/SKILL.md` sections 2 and 15 | The smith runs the module it touches, never the suite. A new case is seen red before it is committed |
| `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-1.md` | The worked example of a file cut by a sampled set and a mutation table, and the shape of the record each batch here writes |
| `seal/specs/1790815613-a-gate-decides-at-the-moment-of-the-action-not-from-the-text/spec.md` *What the tree answered* item 1 | The static reading of shell text is the stopped class. This work adds no rule to it and samples its tests |

## Measured at a16acb40

Each figure was executed by the framer on 2026-10-22 in the worktree, unless labelled read.

- 148 test files, all directly under `tests/`; no `tests/e2e/` exists.
- 108,791 lines of test code against 48,932 lines of shipped Python (every `.py` outside `tests/` and `.venv/`), a ratio of 2.2.
- 7,466 cases collected (`bin/test --collect-only -q -p no:xdist`); 3,621 `def test_` lines.
- `.test_durations` (read) prices 7,284 cases in 142 files at 3,999.5 Windows seconds. Sixteen files price at a minute or more; together they hold 3,071.2 of those seconds and 2,655 of those cases. The five heaviest are the sealer file at 761.1 s, the commit-gate file at 519.7 s, and the three text-reading files at 279.1 s, 242.8 s and 203.9 s.
- Helper twins: 46 distinct non-test function bodies are defined byte-identically in two or more test files, 141 definitions in all, 632 lines of which 396 are beyond one copy. The most copied names are `read` (39 definitions) and `flat` (16). No `git init` helper body is a twin. The issue's 249 twins and 1,413 lines were measured before #929 and #944.
- Shipped units: 1,306 top-level functions and classes in 72 shipped `.py` files; 404 are named in no test file's text. The three files with most unnamed units are `hooks/cmdline.py` (34), `skills/code-review/scripts/chain_check.py` (28) and `hooks/worktree-guard.py` (23).
- `tests/undeclared_readers.txt` is gone, and `agents/smith.md` line 98 and `agents/warden.md` line 131 already carry the group sentences. #923 did both.

## Scope

The work is four rules the smith applies to any module without asking, the two checks and one report that hold them, and the module batches that apply them. This frame fixes the layout, the rules and the order of work. It does not fix per-module case lists, counts or call sites: each phase's first step recomputes those at the tree it builds on, because #988, #1009 and #1005 merge before the smith starts.

### Rule 1, the layout

- One test file per shipped module: `tests/test_<stem>.py`, where `<stem>` is the module's file name without `.py` and with each hyphen written as an underscore. Where two shipped modules share a stem, each file name takes the parent directory before the stem. The target is declared once, as the first assignment after the imports: `TARGET = "<tracked path>"`. A file whose cases run a `bin/` command names the script the launcher runs.
- Inside a file, one class per public top-level function of the target (one whose name does not start with an underscore), named `Test_<function>` with the function's name spelt as the code spells it; a private function gets a class where a case needs one. Behaviour of the module as a whole sits in `Test_module`. A function's class holds at least one case whose name starts with `test_accepts_` (the behaviour on good input) and one whose name starts with `test_refuses_` (the refusal or error on bad input). Other cases in the class take any `test_` name.
- A flow across modules lives under `tests/e2e/<flow>/`, its `TARGET` names the command or hook the flow starts from, and its classes are scenarios that keep the accepting and refusing pair. The commit gate run through real git is the first flow. A worktree creation run as the harness runs one Bash call, the `pre-bash` group, the command under real git in a clone carrying the installed stubs, then the `post-bash` group, is the second: `tests/e2e/creation/test_creation_flow.py`, whose `TARGET` is `hooks/dispatch.py`.
- A case whose assertion reads a shipped document names that document as `TARGET`; its classes are free-named. Such cases are #923's and this work moves none of them.
- A helper used by two files is defined once, in `tests/conftest.py`. The fixture repositories a module needs are built once per module by a module-scoped fixture. Where a case writes into the world, each case takes a copy and the copy is the reset; where no case writes into it beyond a marker keyed by a session id, each case makes its own session id and that is the reset, with no copy.
- The censuses are cases of each module's file: `tests/censuses.py` holds one function per census that judges one file, and each module file ends with `test_census = census_case(TARGET)` from `tests/conftest.py`, so running a module's tests runs every census over its target. A census's exemption is a comment line of its own, directly above the exempted line, because `ruff format` moves a comment written at the end of a line; the census reads it, refuses one above a line the census would not have flagged, refuses one written at the end of a line, and reads no comment that has no reason after its colon. No census keeps a list of exemptions in a test file. A tracked file whose module file does not yet declare it is judged by the sweep in `tests/test_censuses.py`, one git listing per run.

### Rule 2, how each existing case is classified

The smith reads the target's functions first and lists the classes the file must have. Then every old case that exercises the target gets one verdict and no second one:

| Verdict | When | What the batch records |
|---|---|---|
| place | the case fits a class as it is | nothing |
| merge | a case of the class already covers it | the surviving case |
| cut | the mutation table shows every mutation it kills is killed by another case, or the behaviour it guards left the tree | one line: the case name, what it guarded, which case or tree fact now holds it |
| rewrite | the class is written anew under rule 3; the old cases are read for their inputs, then deleted | one line per old case, as for cut |
| to #923 | the assertion reads prose | the case name, in the batch's list left to #923 |
| left for its module | the case's rows pin how another module reads a shape, so the target's mutants cannot show that a sample of the rows protects what the rows did; the case stays in its old file, rewritten in place without git where it ran the gate's `main`, until the phase that rebuilds the module it pins | the case name and the module it waits for |

A pair `bin/test-layout --pairs` names is a reading for the smith and not a verdict, because the report is noisy where two cases call one function with equal literal arguments over different worlds on disk (`plan.md` *Alternatives considered*, the row *`--pairs` compares a call and leaves out only the argument that reads a local*). The pair is merged where one of its cases covers the other. Otherwise both cases are placed, and the batch's record names the pair and says why neither covers the other.

### Rule 3, when a module's tests are written anew from the code

A module's tests are written anew when the old files that exercise it price at 60 seconds or more in `.test_durations`, or when `bin/test-layout --pairs` names a pair inside one of its classes. Every other module's old cases are placed and merged. A module written anew gets its accepting and refusing cases from reading the code, one class per function, and the old cases are read as a reference for inputs. The proof of equal protection below is what shows the new file protects what the old ones did, and rule 4 bounds what the new file may cost.

### Rule 4, what a rewritten module may cost

The target the rebuild works toward is the issue's: the suite's real protection at a fraction of today's time, with no case that runs for tens of minutes and no file or flow that dominates the run. The smith applies this rule while writing each module, and it binds the rewrite and nothing in CI: a time reading is noisy, the per-case ceiling is a report for that reason, and the per-module rows and the release sweep are what act on a slow module after the fact.

- A rewritten module builds its fixture repositories once, in a module-scoped fixture, and resets them between cases by the means rule 1 names, a copy or a per-case session id; it does not build one per case.
- A case about a reading of a command is judged without real git or a real shell. The real-git rows that stay are the ones showing the reading and git agree, and a batch names them.
- A case does not enumerate a whole input space where a sampled set, one row per kind, holds the same behaviour; the proof of equal protection is what shows it does.
- Each rewritten module's record states its seconds before and after, from `bin/test <files> -q` at the build machine, beside the cases before and after.

### The proof of equal protection

#942 changes no shipped code, so the one risk a rebuilt module carries is a fault the old cases caught and the new ones miss. The proof shows that a module's rebuild lost no protection; it decides nothing about what to cut. A module whose cases were only moved, with nothing cut, merged or rewritten, cannot have lost protection, so it skips the mutants. Whether the modules of a group were only moved is decided by the move check below, from the two trees and never from the smith's record. The owner set the mutants' cost on 2026-10-22 and the move check's rule on 2026-10-23; the orchestrator set the check's shape, a set of old files against a set of new files, on 2026-10-23, after phase 6's first step had built it for one new file and found that most old files in `hooks/` hold cases of two or more modules (`phases/phase-6.md` *What the frame's check cannot pass*). The orchestrator gave the check its fourth condition on 2026-10-23, after round 3 found that a group whose moved cases read a changed helper, constant or module binding passed the other three (`rounds/round-3.md` finding 1). The framer extended the fourth condition to the test files directly under `tests/` on 2026-10-24, after round 4 found it reading an import from another test file as the import alone, and stated the condition's readings and limits as the code makes them (`rounds/round-4.md` findings 1 and 2).

- The move check: `bin/test-layout --moved`, with the arguments *Data & interfaces* gives, reads a set of old files at the base commit and a set of new files in the working tree, and passes only where the conditions below hold for the two sets. First, pytest collects as many items from the new set as from the old set at the base, each parametrize row counting as one item and every `test_census` item left out on both sides. Second, each old case's body is in exactly one case of the new set, unchanged apart from its name, its place, the class around it and the `self` parameter, compared as an AST with the docstring of the case, and of every function and class it defines, dropped, because the formatter the edit hook runs re-indents a nested docstring to the case's new depth; a case of the new set that stands for no old case fails this condition too, so an old case that lands in two new files is named by its second landing and not only by the count. Third, every fixture a case requests resolves, in the case's file or in `tests/conftest.py`, to a fixture definition whose AST, decorator included and docstrings dropped as for a case, is the same in both trees, so a world built once where it was built per case is a change. Fourth, every module-level name a case reads, or a fixture it requests reads, the fixtures followed through the fixtures they request as for the third condition, has the same definition in the working tree as at the base: a helper function, a constant a parametrize mark reads, a module bound to a name by an import or by a loader's call, a helper a fixture calls. Each such definition is followed in turn through the names it reads. A name a file imports by `from <module> import`, where `<module>` is a module directly under `tests/`, `tests/conftest.py`, a test file or any other, is read where that module defines it, in the same tree, so a helper moved unchanged into `tests/conftest.py`, or a constant moved unchanged into another test file and imported from there, compares equal. A name read as `<module>.<name>`, where `import <module>` binds a module directly under `tests/`, is read where that module defines it. A name read as `self.<name>` is read where the case's class binds it, outside a function or lambda that takes a `self` of its own. A function or class definition is compared in the form a case's body is compared in, its docstrings dropped at any depth; an assignment is compared as written; an import is compared as the one alias that binds the name, which is the module, the name taken and the relative level, so a statement that also imports other names compares equal. A name bound in neither tree is a builtin or pytest's and is not compared. A name bound in one tree only is a change, and so is a name one tree's reading reaches and the other's does not. Each name is compared as the set of its distinct definitions, wherever the reading reaches them, so one definition reached from two files counts once. The condition has two limits. A name a case reaches only through a string, such as `globals()["x"]`, is not read. Two definitions of one name in two places a case reaches, swapped between the trees, compare equal, because each name is compared as that set; a move does not swap two definitions, so the check carries no guard for it. The check tests a case on the fourth condition only where it passed the second and the third, and a case that fails the fourth prints one line, `moved: <old file>::<case>: name <name>: its definition differs from the base's`, where `<name>` is the first name in alphabetical order whose own definition differs, so a changed name reached through a helper is named itself and the helper is not. The check prints each case that fails with the condition it failed, exits 0 where the group passes and 1 where it does not, and the smith records the command and its last line in place of a mutant table. One run covers one group: the modules of one shipped directory's commit, or any smaller group the smith rebuilds together, and the run names every old file the group's cases were drawn from and every new file the group wrote. An old file that keeps cases for a module of a later group is named in both sets, so its remaining cases compare to themselves in the working tree. A group whose check exits 1 runs the mutants for each of its modules, as below. A failing case that stands in a file declaring no `TARGET` counts for the shipped module whose function it calls as its subject, placed as `questions.md` places a moving case. Where it calls no shipped module as its subject, as a check across files or a case reading prose does, it counts for the definition its line names, in the file that defines it in the working tree, and that definition's decision points carry the mutants: each branch of a function, and each entry of a collection the case reads.
- Where the mutants go, for a module the check does not pass: one or two per class, at each public function's decision points, the branches where a case accepts or refuses, and one more for each further decision point a function holds. The count follows the module's classes and no figure is set for it, so a module of many public functions runs many mutants, each once.
- How the new file's column runs: in one `bin/mutation-check` call carrying every mutant of the module, which runs the baseline once and then each mutant once. The smith puts `-x` in the `--tests` command, so that pytest stops a mutant's run at its first failing case; the tool itself stops nothing.
- When the old files' column runs: only for a mutant the new file lets survive. Where the old files miss it too, the record states an old gap. Where they kill it, the smith adds a case to the new file and sees it red on that mutant before the batch commits.
- What the record carries: the table of mutants with the new column's verdict, the old column's verdict where it ran, each old gap, and each case added.

`broad_gate.py` and `seal_stamp.py` ran under the earlier proof, a table of about 100 mutants each, and their records stay as they were written. `seal_stamp.py`'s table ran in both columns in full. `broad_gate.py`'s new column ran in full, and its old column ran for g1 to g9, for each mutant the new file first let survive and for g104; the rest of that column was stopped for time, and a mutant red against the new file needs no old verdict (`phases/phase-5.md`, each module's *The mutation table*). The commit flow's record says at which mutant it switched to this proof. Every phase 5 module was rewritten, so each ran the mutants and none is re-proved under the move check; the check is phase 6's first step, for the modules whose old cases are placed and merged, built for one new file at 6e7214be and extended to the two sets before Batch B starts.

### What holds the rules

- `skills/verify/scripts/test_layout.py`, run as `bin/test-layout`. `--check` reads every `tests/**/test_*.py` that declares `TARGET` and fails on: a `TARGET` git does not track, a file name that does not match it, a `Test_<function>` naming no top-level definition of the target, a function class lacking the accepting or refusing case, a non-test top-level function whose source is byte-identical to one in another test file where one of the two files declares `TARGET`. It prints the files that declare no `TARGET` and every twin between two undeclared files, and with `--all` fails on both. It prints each public top-level function of the target that has no class, and fails on none. `--pairs` prints, for each class, two cases that call the target's function with equal argument expressions, or whose bodies are equal once names and string constants are normalised, and exits 0 whatever it prints. A call with an argument that reads a name the case assigns or takes as a parameter is not compared at all: its input is on disk or in a fixture, where the report cannot see it. A call with no argument is not compared either, because any two such calls are equal. `--moved` is the move check *The proof of equal protection* states, in the same script because the reader of a test file's classes and cases has one home; it reads the base's files through `git show <base>:<path>` and collects the base's items in a detached worktree of the base that it adds under a temporary directory and removes before it exits.
- `tests/test_test_layout.py` holds the script's own cases on fixtures, and one case that runs `--check` over this repository's `tests/`; the last phase gives that case `--all`.
- `.github/scripts/release_report.py` prints, under its existing table, one row per test file: priced cases and seconds in `.test_durations` at the pull request head and at the last release tag, sorted by seconds. It reads the two trees it already reads and nothing else.
- `tests/conftest.py` prints each case whose call ran past `SLOW_CASE_S` (90 seconds) in the terminal summary and fails nothing. `SPECSEAL_CASE_CEILING_S` is not read. The legs' `timeout-minutes` in `.github/workflows/test.yml` stay.

### What the frame decided on the issue's questions

- Question 5, the commit gate's text reading: it stays, and its three files are cut on #929's pattern, a sampled row per kind with a mutation table. The reading alone judges the two states `docs/the-commit-gate-inside-git.md` names and the stub-removal escape in its known limits; no record since #692 names a commit it caught (three records mention the reading, executed grep over `seal/specs/179[12]*/rounds`, `overview.md` and `phases`); the tree holds no count of installs in either state. Removing it allows more, which is the gate bar's costly direction, so the removal is `questions.md` Q1 with a default of keep.
- Question 6: decided by the owner, built as above.
- The censuses: a census moves into `tests/censuses.py` and runs per module through `test_census` when it judges one file by reading that file alone. A check that reads a document's prose, compares files with each other, derives a set across files, or judges records or markdown against an oracle stays where it is. `tests/test_censuses.py` sweeps every tracked file whose module file does not declare it, so a document and a module not yet rebuilt keep their censuses. The stored lists `OUT_OF_CLASS` (two blocks), `ALLOWED`, `ENTRY_POINTS_CLASSIFIED`, `COORDINATE_EXEMPT` and `HEADING_EXEMPT` become comment lines above the exempted lines. The `Reads:` census is already gone.
- The release sweep: `docs/release-checklist.md` section 5, through `## Rule changes` below.

### The check lines the remaining groups meet

One survey at 44525de4 read every `check:` line in the files `.github/scripts/rules.py#RULE_FILES` lists, and took each line that names a test file declaring no `TARGET`, or a declared file holding a case left for a later group. Each line was judged by `questions.md`'s answer on which files a line names once its cases move. A `docs/` line whose files change has its item under *Rule changes* below, and the installer's line waits on Q10. A line outside the policy root is rewritten in place by the group that moves its cases, in that group's commit:

| Line at 44525de4 | What it names once the group moves | The group that rewrites it |
|---|---|---|
| `agents/sealer.md` line 144 | `tests/test_the_sealer_guarantees.py tests/test_chain_check.py` | `skills/code-review/scripts/` |
| `agents/smith.md` line 109 | `tests/test_a_moved_rule_leaves_its_definition.py tests/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py tests/test_mutation_check.py` | `skills/verify/scripts/` |
| `agents/smith.md` line 123 | `tests/test_the_handoff_before_round_one.py tests/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py tests/test_mutation_check.py` | `skills/verify/scripts/` |
| `agents/warden.md` line 99 | `tests/test_a_reference_root_is_read_and_never_taken.py tests/test_config.py` | `hooks/config.py` |
| `skills/writing-style/SKILL.md` line 268 | `tests/test_rules.py tests/test_rule_changes.py tests/test_censuses.py tests/test_the_agent_contract_holds_the_universal_rules.py` | `.github/scripts/` writes `tests/test_rules.py` in place of `tests/test_the_rules_command_reads_each_rule_off_its_test.py`, and `skills/settle/scripts/` writes `tests/test_rule_changes.py` in place of `tests/test_settle_applies_rule_changes_in_place.py` |

A file a remaining group draws cases from keeps the lines below unchanged, because the cases their rules rest on stay in it, or because the file already carries the module's rule 1 name:

| File | The lines it keeps, at 44525de4 |
|---|---|
| `tests/test_session_cost.py` | `docs/measuring-a-run.md` lines 21, 31, 38, 46 and 68: the file takes `skills/verify/scripts/session_cost.py`'s cases under the name it has |
| `tests/test_arm_check.py` | `docs/the-broad-gate.md` line 153, for the same reason |
| `tests/test_chain_check.py` | all 13 of its lines: the one case it gives up, `test_the_baseline_is_the_first_code_span_of_its_one_row`, holds the `Baseline commit` reader, whose rule is `skills/legacy-parity/SKILL.md`'s and names other files |
| `tests/test_pact_check.py` | `docs/the-pact.md` lines 102 and 141 |
| `tests/test_a_signer_declares_its_pact.py` | `docs/the-pact.md` lines 45 and 61, held by the template and routing cases that stay |
| `tests/test_chain_hooks_hardening.py` | `agents/smith.md` lines 85 and 173, held by the definition cases that stay |
| `tests/test_the_suite_has_a_command_that_is_cheap_twice.py` | `agents/smith.md` line 142 and `agents/warden.md` line 162, held by the definition cases that stay |
| `tests/test_the_sealer_guarantees.py` | `agents/sealer.md` line 109, `docs/the-agent-set.md` line 61 and `docs/the-review-record.md` line 282, held by the definition and document cases that stay |
| `tests/test_a_release_rolls_the_flow_measurement_issue.py` | `docs/issues-and-milestones.md` line 179, whose rule no case of the roll holds |
| `tests/test_the_pull_request_language_is_the_repositorys.py` | `docs/one-root-by-lifetime.md` line 214 and the Korean edition's line 204, held by the cases that compare the template's exclusion list with the checkers |
| `tests/test_release_hygiene.py` | `docs/release-checklist.md` lines 76 and 192, held by the version sweep and the changelog heading cases; line 76's marker moves with the gather case that carries it |
| `tests/test_settle_reads_before_it_removes.py` | `docs/the-record-layout.md` lines 117 and 129, held by the skill cases that stay |

Every other line the survey found names a file no remaining group draws a case from: its cases read prose, which #923 places, or compare files with each other, which *What the frame decided* keeps where it is. Those files are `tests/test_waiver_decided_at_start.py`, `tests/test_a_question_says_who_can_answer_it.py`, `tests/test_a_phase_hands_the_next_one_a_record.py`, `tests/test_the_handoff_before_round_one.py`, `tests/test_the_rules_have_one_owner.py`, `tests/test_a_moved_rule_leaves_its_definition.py`, `tests/test_a_probe_that_commits_says_so.py`, `tests/test_a_probe_does_not_outlive_its_round.py`, `tests/test_absence_claims.py`, `tests/test_broad_gate_rule.py`, `tests/test_the_seal_is_taken_once_by_the_sealer.py`, `tests/test_review_axes.py`, `tests/test_the_verifying_round_is_bounded_not_cheapest.py`, `tests/test_the_record_is_written_in_words.py`, `tests/test_edits_go_through_the_edit_tool.py`, `tests/test_a_commit_names_its_repository.py`, `tests/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`, `tests/test_a_rider_reaches_its_file.py`, `tests/test_the_release_check_watches_what_ships.py`, `tests/test_the_release_tail_does_not_end_at_the_tag.py`, `tests/test_a_release_is_sized_by_a_criterion.py`, `tests/test_a_segment_feeds_the_flow_log.py`, `tests/test_the_settings_have_a_front_door.py`, `tests/test_first_setup_asks_once.py`, `tests/test_a_shrunken_corpus_declines_to_judge.py`, `tests/test_the_contributor_has_a_procedure.py`, `tests/test_every_orchestrator_act_names_its_delivery.py`, `tests/test_every_agent_reads_the_contract.py`, `tests/test_one_word_one_meaning.py`, `tests/test_the_agent_contract_holds_the_universal_rules.py`, `tests/test_the_gate_asks_the_range_ci_will_ask.py`, `tests/test_both_editions_carry_the_same_folds.py`, `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`, `tests/test_the_rules_claude_md_names_have_one_home.py`, `tests/test_no_passage_is_pasted_into_a_second_file.py`, `tests/test_the_hook_surface_git_offers.py` and `tests/test_the_frozen_reading_never_grows.py`. The last two are named by `docs/the-commit-gate-inside-git.md` line 183, which stands under the heading Q10 found doubled and so could carry no item; it needs none, because the hook surface file probes git itself and the frozen reading file's cases compare files with each other or wait on Q10 with the installer.

### Out

- Cases whose assertion reads this repository's prose: #923. Each batch lists the ones it left.
- Which CI legs a pull request runs: #943. `.test_durations` cadence: #931.
- Removing the text reading itself: a work item of its own if Q1 is answered remove.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a misplaced test is refused | Given a test file declaring `TARGET` whose class names no function of the target, when `bin/test-layout --check` runs, then it exits 1 and names the file and class | `tests/test_test_layout.py`, seen red by removing the refusal |
| S2 a class without its pair is refused | Given a function class with only `test_accepts_` cases, when `--check` runs, then it exits 1 naming the class and the missing kind | `tests/test_test_layout.py` |
| S3 a twin is refused | Given two test files defining one helper byte-identically, one of them declaring `TARGET`, when `--check` runs, then it exits 1 naming both | `tests/test_test_layout.py` |
| S4 a likely pair is named, not refused | Given two cases in one class calling the function with equal arguments, when `--pairs` runs, then both names print and the exit is 0 | `tests/test_test_layout.py` |
| S5 a rebuilt module protects what the old files did | Given a module's new file and its mutants, one or two per class at the public functions' decision points, when one `bin/mutation-check` call runs them against the new file, then every mutant is killed, or each survivor is run against the old files and either recorded as an old gap or answered by a case seen red on it | the phase record's table |
| S6 a slow case is reported | Given a case whose call runs past `SLOW_CASE_S`, when the run ends, then one line names it and its seconds and the run exits 0 | `tests/test_conftest.py`, an inner pytest run with the value lowered |
| S7 the release table has module rows | Given `.test_durations` at the head and at the tag, when `release_report.py` runs, then one row per test file prints with cases and seconds at both | `tests/test_release_report.py` on two fixture trees |
| S8 a census runs with its module | Given `tests/test_<stem>.py`, when `bin/test tests/test_<stem>.py` runs, then `test_census` judges `TARGET` under every census | `tests/test_censuses.py` with a fixture target that fails one census |
| S9 a spent exemption is refused | Given an exemption comment line directly above a line no census flags, when the census runs, then it fails naming the line | `tests/test_censuses.py` |
| S10 the whole suite is placed | Given the last batch merged, when `--check --all` runs over `tests/`, then it exits 0 | the suite case in `tests/test_test_layout.py` |
| S11 a module only moved skips the mutants | Given a fixture repository with old test files at a base commit and a new file holding the same cases in classes, when `bin/test-layout --moved` runs with the old files as `--from` and the new file as `--to`, then it exits 0; given instead one old case cut, two old cases merged into one, one case's body edited, or one fixture's scope changed from function to module, then it exits 1 naming the case and the condition it failed | `tests/test_test_layout.py::Test_moved::test_accepts_a_pure_move` and `Test_moved::test_refuses_a_cut_a_merge_an_edited_body_and_a_changed_fixture`, one row per failing kind, each seen red with its condition removed from the script |
| S12 an old file split across two modules passes | Given one old file at the base whose cases belong to two modules, when `--moved` runs with that file as `--from` and the two new files holding its cases as `--to`, then it exits 0; given instead a second old file at the base that keeps cases for a module of a later group, named in `--from` and in `--to`, with the cases it keeps unchanged in the working tree, then it exits 0 | `Test_moved::test_accepts_an_old_file_split_across_two_new_files`, one row per passing shape, each seen red against the script at 6e7214be, which refuses `--to` |
| S13 a case that lands twice is refused | Given one old case whose body is in two cases of the new set, when `--moved` runs over the sets, then it exits 1 naming the second landing's case and the condition it failed, beside the count | a row of `Test_moved::test_refuses_a_cut_a_merge_an_edited_body_and_a_changed_fixture`, seen red with the condition's line removed from the script |
| S14 a nested docstring the formatter re-indented still passes | Given an old case at the base that defines a function whose docstring runs over three lines, and the same case in a class of the new set with that docstring's continuation lines indented four spaces deeper, when `--moved` runs over the two sets, then it exits 0; given instead one statement of the nested function changed, then it exits 1 naming the case and the body condition | a row of `Test_moved::test_accepts_a_pure_move`, seen red against the script at 54b41700, and a row of `Test_moved::test_refuses_a_cut_a_merge_an_edited_body_and_a_changed_fixture` |
| S15 a moved case that reads a changed name is refused | Given an old file at the base and a new file whose cases are the old cases unchanged in classes, with only a module-level name the cases read changed, when `--moved` runs over the two, then it exits 1 and prints the case with `name <name>`, for each of five shapes: a helper's body changed, `parse` returning `[1, 2]` in place of `json.loads(s)`; a module bound by an import rebound to another module, `subject` from `posixpath` to `ntpath`; a row constant a parametrize mark reads changed with its length kept, `ROWS` from `[('a', 1), ('bb', 2)]` to `[('a', 1), ('a', 1)]`; a helper a requested fixture calls changed to return `[]`; and a name bound by a loader's call given another module's path. It does the same for each reading the fourth condition names beside those: a name read as `<module>.<name>` changed in that module under `tests/`; a helper read as `self.<name>` changed in the case's class; a module re-exported through `tests/conftest.py` and read as `<module>.<name>`, which one tree's reading reaches and the other's does not; and a name both trees import from one test file, changed in that file. Given instead a helper moved unchanged from the old file into `tests/conftest.py` and imported from there, a constant moved unchanged into a module under `tests/` that is not a test file and imported from there, a name imported from another test file that defines it as the base's file did, or a name imported in a statement that imports one more name than the base's, then it exits 0 | five rows of `Test_moved::test_refuses_a_cut_a_merge_an_edited_body_and_a_changed_fixture`, each seen red against the script at 76551ca7, which exits 0 on all five; three more rows of that case, `a-changed-module-attribute`, `a-changed-class-helper` and `a-module-reached-another-way`, seen red against the same script (`phases/phase-7.md` *S15, in round 3's fix pass*); its row `a-changed-name-in-another-test-file`, seen red against the script at a1047bfe, which compares the import alone and exits 0 on it; three rows of `Test_moved::test_accepts_a_pure_move`, each seen red with the reading it needs removed from the new script: the following into `tests/conftest.py`, the following into the other modules under `tests/`, the import read as its one alias; and the row `a-name-imported-from-another-test-file`, moved from the refusing case to the accepting one, seen red against the script at a1047bfe, which exits 1 on it. The swap of two definitions is the condition's limit, stated in *The proof of equal protection*, and has no row |

## Data & interfaces

- `bin/test-layout --check [--all] [paths]`, `bin/test-layout --pairs [paths]` and `bin/test-layout --moved <base> --from <old file>... --to <new file>...`, launched through `hooks/launch.py` like `bin/mutation-check`. With `--moved`, `<base>` is a commit the repository holds, each `--from` path names an old test file at that commit, each `--to` path names a test file in the working tree, and one path may stand in both lists; the exit is 0 where the two sets pass every condition *The proof of equal protection* states, 1 where they do not, and 2 where the base or a file cannot be read. A path after the two lists, and the earlier spelling that took the new file as `--from`'s last word, do not parse and exit 2: once either list may hold several paths, a path's list is told by the word before it and by nothing a reader has to count.
- `tests/conftest.py#census_case(target)` returns the one case; `tests/censuses.py` exposes `def <census>(rel, root=None) -> list[str]`, one per census, where `rel` is the file's path relative to the repository root and `root` is the tree read, the repository root when absent.
- `release_report.py#module_rows(at, now)` reads `.test_durations` in both trees.
- `bin/mutation-check <path> --tests <command> --replace OLD NEW`, with `--replace` given once per mutant: a call with several pairs runs the baseline once, then each mutant once, restores the file after each, and prints one verdict line per pair in the order given. It exits 0 where every mutant is red, 1 where any mutant survived, and 2 where none survived but a run gave no verdict. It stops no run early: a `--tests` command that should stop at its first failing case carries pytest's `-x`. A call with one pair runs as it does today.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the failing ceiling and its environment variable | `tests/conftest.py#CASE_CEILING_S`, `#ceiling_from`, `#over_the_ceiling`, `#pytest_runtest_makereport` | `SLOW_CASE_S` and a terminal-summary report in the same file; a report needs no raise |
| the slow-case module | `tests/test_a_slow_case_names_itself.py` | `tests/test_conftest.py` under rule 1, except its case that reads the legs' `timeout-minutes` in `test.yml`, which lands in `tests/test_ci_gives_the_checks_what_they_need.py` beside the cases that read the same workflow |
| the stored exemption lists | `tests/test_every_reader_ends_a_line_where_gfm_does.py#OUT_OF_CLASS`, `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py#ALLOWED` and `#ENTRY_POINTS_CLASSIFIED`, `tests/test_a_format_has_one_reader.py#COORDINATE_EXEMPT` and `#HEADING_EXEMPT` | a comment line directly above each exempted line, read by the census in `tests/censuses.py` |
| the helper twins | every non-test top-level function defined byte-identically in two or more files under `tests/` | one definition in `tests/conftest.py` |
| every test file not in the layout | `tests/test_*.py` as they stand at the build's start | `tests/test_<stem>.py`, `tests/e2e/<flow>/`, or the batch's cut lines. An old file a `check:` line names stays in the tree, holding no case once its cases leave, until `settle --apply` applies this spec's `## Rule changes` after the release, because a pull request does not edit `docs/` and `bin/rules --check` refuses a line naming a file that does not exist |
| cases whose kills another case makes, and cases guarding behaviour that left the tree | named per batch in `phases/phase-N.md` | the batch's one line per case |
| the priced ids of removed cases | `.test_durations` | pruned by the smith with one `Edit` per batch, whose match on the removed lines is what asserts each id was present |
| the one-new-file form of the move check, the new file taken as `--from`'s last word or as a path after it | `skills/verify/scripts/test_layout.py#main`, the branch under `args.moved` that pops the last `--from` word into the new file | `--to <new file>...`, read by `main` as the second list; `Test_moved`'s rows run with `--to` |
| the paragraph heading a case's budget | `CONTRIBUTING.md` *A case has a budget, and so does each leg* | rewritten in place to the report, same section; the four rules and the record shape go under a new heading `CONTRIBUTING.md` *The test layout*, which `.github/scripts/rules.py` reads like every `CONTRIBUTING.md` heading |

## Rule changes

- change
  file: docs/release-checklist.md
  section: 5. The release pull request
  from: each agent's preload bytes, the suite's seconds, each leg's minutes and each document's bytes, beside the same reading at the last release tag.
  to: each agent's preload bytes, the suite's seconds, each test file's priced
    cases and seconds, each leg's minutes and each document's bytes, beside
    the same reading at the last release tag.
- add
  file: docs/release-checklist.md
  section: 5. The release pull request
  to: **Each release clears what grew.** The module rows are a report and
    never a ceiling: a heavily exercised module needs the cases it needs. The
    owner reads the rows whose seconds or cases grew most since the tag and
    sweeps each such module with one `bin/mutation-check` call carrying a
    mutant per class, for cases that kill nothing another case does not. The
    sweep's cuts land in a work item of the next release with one line per
    cut case, the shape `CONTRIBUTING.md` *The test layout* gives.
- change
  file: docs/the-broad-gate.md
  section: What the gate runs, and how the list is kept true
  from: row, and it is three rules rather than an example. check: tests/test_the_seal_is_taken_once_by_the_sealer.py
  to: row, and it is three rules rather than an example.
    check: tests/test_broad_gate.py
- change
  file: docs/the-broad-gate.md
  section: What the gate runs, and how the list is kept true
  from: half a repair. check: tests/test_the_seal_is_taken_once_by_the_sealer.py
  to: half a repair.
    check: tests/test_broad_gate.py
- change
  file: docs/the-broad-gate.md
  section: What the gate runs, and how the list is kept true
  from: it says nothing a reader acts on. check: tests/test_the_seal_is_taken_once_by_the_sealer.py
  to: it says nothing a reader acts on.
    check: tests/test_broad_gate.py
- change
  file: docs/commit-review-gate-spec.md
  section: The PreToolUse reading of a commit
  from: check: tests/test_no_shape_the_base_stops_reads_silent.py
  to: check: tests/test_commit_review_gate.py tests/test_cmdline.py
- change
  file: docs/worktree-guard-spec.md
  section: Creation consent
  from: `test_the_command_word_class_is_what_the_allow_covers` pins members of each group, and is where a new spelling is checked.
  to: `Test_only_creates_a_worktree` in `tests/test_worktree_guard.py` pins
    members of each group in the rows of its two cases, and is where a new
    spelling is checked.
- change
  file: docs/worktree-guard-spec.md
  section: Creation consent
  from: `test_the_guard_is_never_silent_where_the_writer_records` walks every shape it lists in four tree states, from two shell directories, three attempts each, and `test_a_dirty_tree_does_not_decide_whether_the_creation_is_questioned` holds the fifth.
  to: `Test_main::test_refuses_to_be_silent_where_the_writer_records` in
    `tests/test_worktree_guard.py` walks every shape `CREATIONS` lists in four
    session states, from two shell directories, three attempts in the two
    states whose budget the attempts spend, and
    `Test_main::test_refuses_a_line_weaker_than_its_switch_or_its_creation`
    holds the fifth state, the dirty tree.
- change
  file: docs/worktree-guard-spec.md
  section: Creation consent
  from: check: tests/test_the_guard_asks_once_per_session.py tests/test_guard_resolves_the_tree_it_judges.py
  to: check: tests/test_worktree_consent.py tests/test_worktree_guard.py
- change
  file: docs/worktree-guard-spec.md
  section: Known limits
  from: `test_a_shell_built_word_is_the_named_limit` and the braced half of `test_no_listed_form_moves_head_under_git` in `tests/test_worktree_guard.py` pin the limit.
  to: The braced rows of `Test_main::test_accepts_data_no_shell_runs_as_no_command`
    and the braced half of
    `Test_shape_of::test_accepts_no_listed_form_that_moves_head_under_git` in
    `tests/test_worktree_guard.py` pin the limit.
- change
  file: docs/worktree-guard-spec.md
  section: Known limits
  from: moves HEAD fails `test_no_listed_form_moves_head_under_git`; a form no case
  to: moves HEAD fails
    `Test_shape_of::test_accepts_no_listed_form_that_moves_head_under_git`; a
    form no case
- change
  file: docs/one-root-by-lifetime.md
  section: Shared or local
  from: check: tests/test_first_setup_asks_once.py tests/test_optin_home.py tests/test_the_records_can_be_carried_out_and_in.py
  to: check: tests/test_first_setup_asks_once.py tests/test_optin.py tests/test_seal.py
- change
  file: docs/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: check: tests/test_the_records_can_be_carried_out_and_in.py tests/test_the_mode_is_a_row_and_a_command.py
  to: check: tests/test_seal.py
- change
  file: docs/one-root-by-lifetime.ko.md
  section: shared 인가 local 인가
  from: check: tests/test_first_setup_asks_once.py tests/test_optin_home.py tests/test_the_records_can_be_carried_out_and_in.py
  to: check: tests/test_first_setup_asks_once.py tests/test_optin.py tests/test_seal.py
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 저장소가 스스로 정하는 것, 그리고 그것을 읽는 방법
  from: check: tests/test_the_records_can_be_carried_out_and_in.py tests/test_the_mode_is_a_row_and_a_command.py
  to: check: tests/test_seal.py
- change
  file: docs/one-root-by-lifetime.md
  section: The root and its lifetimes
  from: check: tests/test_no_document_names_the_old_roots.py tests/test_optin_home.py
  to: check: tests/test_no_document_names_the_old_roots.py tests/test_optin.py
- change
  file: docs/one-root-by-lifetime.md
  section: The opt-in signal is the root itself
  from: check: tests/test_optin_home.py
  to: check: tests/test_optin.py tests/test_commit_review_gate.py
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 루트와 그 안의 수명
  from: check: tests/test_no_document_names_the_old_roots.py tests/test_optin_home.py
  to: check: tests/test_no_document_names_the_old_roots.py tests/test_optin.py
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 옵트인 신호는 루트 자체다
  from: check: tests/test_optin_home.py
  to: check: tests/test_optin.py tests/test_commit_review_gate.py
- change
  file: docs/commit-review-gate-spec.md
  section: Registration
  from: check: tests/test_a_gate_that_fails_says_so.py
  to: check: tests/test_dispatch.py tests/test_a_gate_that_fails_says_so.py
- change
  file: docs/commit-review-gate-spec.md
  section: The implementer mark and notice
  from: check: tests/test_the_implementer_is_recorded.py
  to: check: tests/test_implementer_mark.py tests/test_implementer_notice.py tests/test_commit_review_gate.py
- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: check: tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py tests/test_routing_is_recorded.py
  to: check: tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py tests/test_routing.py
- change
  file: docs/worktree-guard-spec.md
  section: A. Branch switch
  from: check: tests/test_the_guard_asks_once_per_session.py tests/test_worktree_guard.py
  to: check: tests/test_worktree_consent.py tests/test_worktree_guard.py
- change
  file: docs/worktree-guard-spec.md
  section: A. Branch switch
  from: check: tests/test_worktree_guard.py tests/test_the_guard_asks_once_per_session.py tests/test_guard_resolves_the_tree_it_judges.py
  to: check: tests/test_worktree_guard.py tests/test_worktree_consent.py
- change
  file: docs/worktree-guard-spec.md
  section: Decided before git runs
  from: check: tests/test_a_creation_is_judged_before_git_runs.py tests/test_the_hook_surface_git_offers.py
  to: check: tests/e2e/creation/test_creation_flow.py tests/test_the_hook_surface_git_offers.py
- change
  file: docs/worktree-guard-spec.md
  section: Decided before git runs
  from: never carried to a git hook. check: tests/test_a_creation_is_judged_before_git_runs.py
  to: never carried to a git hook.
    check: tests/e2e/creation/test_creation_flow.py
- change
  file: docs/worktree-guard-spec.md
  section: Choice sites
  from: check: tests/test_a_creation_in_another_clone_asks_nobody.py tests/test_worktree_guard.py tests/test_the_idle_session_rows_ask_nobody.py
  to: check: tests/test_worktree_guard.py
- change
  file: docs/worktree-guard-spec.md
  section: Activity: what makes a session ACTIVE without a lease
  from: check: tests/test_worktree_guard_signals.py
  to: check: tests/test_worktree_guard.py
- change
  file: docs/worktree-guard-spec.md
  section: Which tree
  from: check: tests/test_worktree_guard.py tests/test_guard_resolves_the_tree_it_judges.py
  to: check: tests/test_worktree_guard.py tests/test_worktree_consent.py
- change
  file: docs/the-review-record.md
  section: The stamp
  from: check: tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py
  to: check: tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/test_sealer_stamp.py
- change
  file: docs/commit-review-gate-spec.md
  section: The PreToolUse reading of a commit
  from: check: tests/test_an_automation_run_meets_no_commit_prompt.py
  to: check: tests/test_commit_review_gate.py tests/test_worktree_consent.py
- change
  file: docs/commit-review-gate-spec.md
  section: Which repository
  from: check: tests/test_gate_judges_the_repo_it_commits_to.py tests/test_what_the_reader_understands.py
  to: check: tests/test_commit_review_gate.py tests/test_cmdline.py
- change
  file: docs/commit-review-gate-spec.md
  section: Which repository
  from: check: tests/test_a_commit_behind_a_reserved_word_is_judged.py tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py
  to: check: tests/test_commit_review_gate.py tests/test_cmdline.py
- change
  file: docs/the-review-and-parity-arms.md
  section: Review arm
  from: check: tests/test_the_waiver_can_be_typed.py
  to: check: tests/test_commit_review_gate.py
- change
  file: docs/the-review-and-parity-arms.md
  section: Parity arm
  from: check: tests/test_chain_hooks_hardening.py
  to: check: tests/test_commit_review_gate.py tests/test_commitgate.py tests/test_gate.py
- change
  file: docs/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: check: tests/test_the_mode_question_is_asked_once.py
  to: check: tests/test_config.py tests/test_seal.py
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 저장소가 스스로 정하는 것, 그리고 그것을 읽는 방법
  from: check: tests/test_the_mode_question_is_asked_once.py
  to: check: tests/test_config.py tests/test_seal.py
- change
  file: docs/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: than for one language. check: tests/test_the_pull_request_language_is_the_repositorys.py
  to: than for one language.
    check: tests/test_the_pull_request_language_is_the_repositorys.py tests/test_config.py
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 저장소가 스스로 정하는 것, 그리고 그것을 읽는 방법
  from: 이름을 붙입니다. check: tests/test_the_pull_request_language_is_the_repositorys.py
  to: 이름을 붙입니다.
    check: tests/test_the_pull_request_language_is_the_repositorys.py tests/test_config.py
- change
  file: docs/the-pact.md
  section: The words
  from: check: tests/test_one_word_one_meaning.py tests/test_a_signer_declares_its_pact.py
  to: check: tests/test_one_word_one_meaning.py tests/test_config.py
- change
  file: docs/the-pact.md
  section: The words
  from: check: tests/test_pact_check.py tests/test_a_signer_declares_its_pact.py tests/test_one_word_one_meaning.py
  to: check: tests/test_pact_check.py tests/test_config.py tests/test_one_word_one_meaning.py
- change
  file: docs/the-pact.md
  section: How a signer names the pact
  from: check: tests/test_a_signer_declares_its_pact.py tests/test_pact_check.py
  to: check: tests/test_a_signer_declares_its_pact.py tests/test_pact_check.py tests/test_config.py
- change
  file: docs/the-pact.md
  section: The pact anchor
  from: check: tests/test_pact_check.py tests/test_a_unit_is_bounded_where_a_parser_decides.py
  to: check: tests/test_pact_check.py tests/test_coordinates.py
- change
  file: docs/the-pact.md
  section: `pact-check` reconciles, locally
  from: check: tests/test_pact_check.py
  to: check: tests/test_pact_check.py tests/test_config.py
- change
  file: docs/the-agent-set.md
  section: What a spawn costs
  from: check: tests/test_the_payload_meter_says_what_it_measured.py
  to: check: tests/test_payload_meter.py
- change
  file: docs/the-broad-gate.md
  section: What the gate runs, and how the list is kept true
  from: check: tests/test_the_gate_names_every_step_ci_runs.py
  to: check: tests/test_the_gate_names_every_step_ci_runs.py tests/test_broad_gate.py
- change
  file: docs/the-broad-gate.md
  section: What the runner owes the person who typed it
  from: nothing else. check: tests/test_the_suite_has_a_command_that_is_cheap_twice.py
  to: nothing else.
    check: tests/test_the_suite_has_a_command_that_is_cheap_twice.py tests/test_run_tests.py
- change
  file: docs/the-broad-gate.md
  section: What the runner owes the person who typed it
  from: carries on. check: tests/test_the_suite_has_a_command_that_is_cheap_twice.py
  to: carries on.
    check: tests/test_the_suite_has_a_command_that_is_cheap_twice.py tests/test_run_tests.py
- change
  file: docs/the-broad-gate.md
  section: What the runner owes the person who typed it
  from: or `--pdb`. check: tests/test_the_suite_has_a_command_that_is_cheap_twice.py
  to: or `--pdb`.
    check: tests/test_run_tests.py
- change
  file: docs/measuring-a-run.md
  section: What a measurement must survive, and what it must not invent
  from: check: tests/test_a_derived_number_reaching_an_int_carries_a_guard.py
  to: check: tests/test_session_cost.py
- change
  file: docs/measuring-a-run.md
  section: Where a reading goes
  from: remember to run it. check: tests/test_session_cost_post.py
  to: remember to run it.
    check: tests/test_session_cost.py
- change
  file: docs/measuring-a-run.md
  section: Where a reading goes
  from: reaching it would. check: tests/test_session_cost_post.py
  to: reaching it would.
    check: tests/test_session_cost.py
- change
  file: docs/issues-and-milestones.md
  section: A label answers *what it is about*, and survives the move
  from: answers no lookup. check: tests/test_a_release_rolls_the_flow_measurement_issue.py
  to: answers no lookup.
    check: tests/test_roll_flow_measurement_issue.py
- change
  file: docs/issues-and-milestones.md
  section: A label says a ticket is already in, before the release ships
  from: check: tests/test_a_merged_ticket_says_so_on_the_tracker.py
  to: check: tests/test_label_merged_on_release_branch.py
- change
  file: docs/issues-and-milestones.md
  section: A keyword claims the one number after it
  from: check: tests/test_a_body_naming_two_issues_claims_one.py
  to: check: tests/test_a_body_naming_two_issues_claims_one.py tests/test_issue_claims_check.py
- change
  file: docs/issues-and-milestones.md
  section: A keyword claims the one number after it
  from: check: tests/test_release_hygiene.py
  to: check: tests/test_close_issues_on_release.py
- change
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: check: tests/test_the_closer_carries_on_past_a_refusal.py
  to: check: tests/test_close_issues_on_release.py
- change
  file: docs/the-record-layout.md
  section: The size a reader takes whole
  from: check: tests/test_a_document_has_room_for_the_next_fold.py
  to: check: tests/test_fold_check.py
- change
  file: docs/the-record-layout.md
  section: A change writes fragments, never a shared file
  from: check: tests/test_the_changelog_is_gathered_at_release.py
  to: check: tests/test_the_changelog_is_gathered_at_release.py tests/test_gather_changelog.py
- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: applies its rule changes. check: tests/test_settle_reads_before_it_removes.py
  to: applies its rule changes.
    check: tests/test_settle.py
- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: check: tests/test_settle_applies_rule_changes_in_place.py tests/test_settle_reads_before_it_removes.py
  to: check: tests/test_rule_changes.py tests/test_settle.py
- change
  file: docs/the-record-layout.md
  section: seal/specs/<work-item-id>/
  from: check: tests/test_settle_applies_rule_changes_in_place.py
  to: check: tests/test_settle.py
- change
  file: docs/the-record-layout.md
  section: The root records
  from: check: tests/test_the_changelog_is_gathered_at_release.py
  to: check: tests/test_the_changelog_is_gathered_at_release.py tests/test_gather_changelog.py
- change
  file: docs/the-review-record.md
  section: The round record
  from: check: tests/test_settle_applies_rule_changes_in_place.py
  to: check: tests/test_settle.py
- change
  file: docs/the-review-record.md
  section: The guarantee
  from: at the new HEAD. check: tests/test_the_sealer_guarantees.py
  to: at the new HEAD.
    check: tests/test_the_sealer_guarantees.py tests/test_chain_check.py
- change
  file: docs/release-checklist.md
  section: 2. Gather, bump
  from: check: tests/test_the_changelog_is_gathered_at_release.py
  to: check: tests/test_the_changelog_is_gathered_at_release.py tests/test_gather_changelog.py
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: check: tests/test_a_release_publishes_its_note.py tests/test_the_release_tail_does_not_end_at_the_tag.py tests/test_the_release_seal_is_drawn.py
  to: check: tests/test_a_release_publishes_its_note.py tests/test_publish_release_note.py tests/test_the_release_tail_does_not_end_at_the_tag.py tests/test_the_release_seal_is_drawn.py tests/test_release_seal.py
- change
  file: docs/release-checklist.md
  section: 3. Verify before committing
  from: check: tests/test_a_shrunken_corpus_declines_to_judge.py
  to: check: tests/test_a_shrunken_corpus_declines_to_judge.py tests/test_conftest.py

## Open questions → questions.md

Framed 2026-10-22 by framer, before the build.
Reframed 2026-10-23 by framer, after round 3.
Reframed 2026-10-24 by framer, after round 4.

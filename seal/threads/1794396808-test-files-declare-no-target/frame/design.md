# Design: 88 of 141 test files declare no TARGET, so the layout and its duplicate finder never read them (#1489)

## Grounding

The tree as read at `b9ca37404`.

| Policy clause | What it fixes for this work |
|---|---|
| **G1** `CONTRIBUTING.md` *The test layout* (read whole) | Each shipped module has one test file, `tests/<area>/test_<stem>.py`, that declares `TARGET`, holds one class per public function with an accepting and a refusing case, and ends with the census line. A file whose cases read a shipped document names it as `TARGET`, and its name and classes are free. At this commit the section placed a file that declares none in `tests/behaviour/` or `tests/text/` by what its cases run, a placement the files `trail/rounds/round-1.md` finding 2 lists did not follow (executed: each one's imports and loader read with `git show b9ca37404:<file>`), and called those two directories the tree-wide files `skills/verify/SKILL.md` *Scope: cheap and often, broad and once* runs at every phase boundary. This work restates both: the tree-wide files are the files that declare no `TARGET`, wherever they stand (*Scope* item 3), and such a file stands in `tests/behaviour/` or in `tests/text/`, which together hold every file that declares none, with no rule on which of the two (`1ebd4cf19`, `trail/rounds/round-1.md` finding 2). A rebuilt module's record carries `bin/seal layout --moved` with exit 0, or a mutation table. The section is a rule file outside the policy root (`.github/scripts/rules.py#RULE_FILES`), so this work rewrites it in place. |
| **G2** `skills/verify/scripts/test_layout.py`, its docstring, `#check`, `#_calls`, `#pairs` and `#main` (read) | `--check` reports a file that declares no `TARGET`, and `--all` refuses it. `--pairs` prints two cases of one class that call the class's function with equal argument expressions, and leaves out a call with no argument "because any two such calls are equal", and a call whose argument reads a local, because its input is "on disk or in a fixture, where the report cannot see it". |
| **G3** The issue (executed: `gh issue view 1489 --json body,comments`, no comment) and its counts re-taken from a `git clone --no-local` of the worktree under the framer's scratch directory | The files `seal layout --check --all` refuses for declaring no `TARGET` are those of *The files*, 24,339 lines (executed: `wc -l` over them), and *The counts* gives the report's last lines at the base (executed). The issue's 141, 88, 130 and 91 were taken before #1488 and #1486 merged. |
| **G4** The pairs `seal layout --pairs` prints in `tests/github/test_run_tests.py::Test_main`, 66 at the base (executed), and the class itself (read: `:469-803`); a probe that leaves out a call whose every argument is an empty list, tuple or dict display or `None` (executed: `#_calls` wrapped in a scratch script over every test file of the clone) | Twelve cases each call `rt.main([])` under a different monkeypatched world, so every two of them pair. Each pair is correct code that the reader misreads, the case contract rule 18 names. The probe prints none of that class's pairs and 41 pairs in all, 29 by equal arguments and 12 by equal bodies. `[]` carries no input, so the docstring's own reason for leaving out a call with no argument holds for it. |
| **G5** #1488's frame, `seal/threads/1794383427-asserts-pin-literal-phrases/frame/design.md` *What an assert reads*, *The criterion*, *Out* and `frame/plan.md` A3 and A9 (read) | *The criterion* rules an assert that reads a file of the tree as text. #1488 read whole each case of the two directories that held a listed assert, and left "a case that holds no listed assert" to #1489 for "each case it moves". The issue asks that a case reading a document goes through that criterion first. `tests/behaviour/test_no_document_names_the_old_roots.py` keeps #1059's three cases, which walk the tracked texts and read the core and both READMEs. |
| **G6** The cases #1488 read (executed: #1488's *The listing*, cut to print `path::case`, over `tests/text/` and `tests/behaviour/` written at `18a7e18fb` with `git show`) | 341 cases held a listed assert at #1488's base. 250 of the cases of *The files* carry one of those names at `b9ca37404` (executed: `ast` over each file, a parametrized case counted once). The other 442 are what *Scope* item 4 rules, with the printed cases *The cases #1488 read* names as unread. |
| **G7** Where each case's subject is (executed: a scratch `ast` probe that follows each case through the module-level names it reads to a loader call, `load_module`, `load`, `load_lib_module` and their kin, or to an import from a module file) | 110 of the cases of *The files* reach exactly one shipped module, 41 reach several, and 541 reach none. The probe reads names, not what an assert holds, so it is a candidate list; *The files* below starts from it and the docstrings, and each case is ruled by reading it (`frame/questions.md` Q1). Every module those cases reach already has its module file. |
| **G8** Check lines that name a file of *The files* (executed: `git grep -n '^ *check: ' -- . ':!seal/threads' ':!tests' ':!*.py'`) | 79 lines name 46 of the files: 65 under `docs/`, 14 in `CONTRIBUTING.md` and `skills/`. `seal rules --check` refuses a line naming a path that is no file, and a pending `change` excuses nothing (`.github/scripts/rules.py`, docstring, read). |
| **G9** `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read); `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/frame/design.md` `## Rule changes` (read); #1488's `frame/plan.md` A9 and A10 (read) | Which subject a work item has is the framer's judgment. #1483 deleted a test file a `docs/` check line named, judged that its subject includes the policy root's text, and edited the line in place. #1488 stated its check-line changes for the settle, kept each named file until then, and left a module it emptied to a successor issue. This work re-points the lines and the prose that cite the test files it moves, and changes no rule's sentence or grounds, so it takes #1483's route (`## Rule changes`). |
| **G10** The unsettled designs' `## Rule changes` (read: each design under `seal/threads/`) | #1488's six operations hold four `docs/` check lines that name files of this work: `docs/layout/one-root-by-lifetime.md:29` and its Korean edition's, `docs/forms/the-round-record.md:107`, `docs/running/the-broad-gate.md:33` and `docs/layout/the-pact.md:39`. *Scope* item 9 leaves a line an operation holds alone. No other design's operation names a file of `tests/text/` or `tests/behaviour/`. |
| **G11** `tests/behaviour/test_this_repository_passes_its_own_checks.py::Test_seal_layout` (read); `git grep -n -e '--all' -e 'every=' -- skills/verify/scripts/test_layout.py tests .github` (executed) | The suite runs `seal layout --check` without `--all` and reads its last line. Nothing in the tree runs `--all` except its own cases in `tests/skills/test_test_layout.py`. |
| **G12** `seal/follow-up.md` (read) | Both tables are empty. No item waits on this work. |
| **G13** The latest release's `### Process changes`, v0.37.3 (executed: `gh release view --json body`) | Its rows move agent rules between files. One bears on the build: a fix pass opens `skills/implement/fix-pass.md`. |
| **G14** The release's other open work items (executed: `git diff --stat $(git merge-base <branch> HEAD) <branch>` for #1482; `gh issue view` for #1484 and #1485) | `frame/plan.md` *Overlap with the release* holds where each meets this work. |

## Scope

In:

1. **The pair reader leaves out a call that carries no input.** `skills/verify/scripts/test_layout.py#_calls` leaves out a call whose every argument is an empty list, tuple or dict display or `None`, for the reason it leaves out a call with no argument. Its docstring and the module docstring's paragraph on `--pairs` say so, and the cases of `tests/skills/test_test_layout.py::Test_pairs` hold it: one that a call of empty displays and `None` alone is no pair, shown red against the reader before the change, and one that a call passing `[]` beside an input is still compared, which holds *every* apart from *any*.
2. **`--all` goes.** The flag, the `every` parameter of `#check` and the refusals it made, the docstring lines that state them, and the cases of `tests/skills/test_test_layout.py` that hold them are removed (`## Removes`). `seal layout --check` keeps reporting each file that declares no `TARGET` and keeps its count on the last line.
3. **`CONTRIBUTING.md` *The test layout* states the three kinds of *The kinds* and the reason line, in place.** The paragraph that opens "A test file that declares no `TARGET` stands by what its cases run" is rewritten to them. The tree-wide test files become the files that declare no `TARGET`, wherever they stand. "Lists the files that do not declare one yet" becomes "lists the files that declare none". A moved case keeps its name. A pair the report prints carries its reason in its class's docstring (item 11). `CONTRIBUTING.md:43`, *What a contribution is asked for*, which calls the two directories the tree-wide files, is corrected with it (contract rule 19). Phase 1 wrote the section before the fold `3fc2aca87` widened *The kinds*, so phase 8 brings the paragraph that opens "A case stands in the file of what it holds" to *The kinds*: a module is a shipped one or a module under `tests/` that is not a test file, a case whose subject is such a module's source is M for it, a case that uses one only to read another file has that file as its subject, and the T3 ground counts several modules, shipped or under `tests/`. No `check:` line stands under that paragraph and no case reads its sentences (executed: `awk` over `CONTRIBUTING.md:216-345` for `check:` lines, which stand at `:252` and `:261`, above it; `git grep` of its sentences over `tests/`, `skills/` and `lib/`).
4. **The criterion comes first.** Each case of *The files* that #1488 did not read whole (G6, *The cases #1488 read*) is read whole before it is moved or its file is filed, and each of its asserts that reads a file of the tree as text is kept or removed by #1488's *The criterion*, with #1488's *What an assert reads* deciding what an assert reads. The ruling is committed before the move or the filing, so the move check compares the ruled case with its moved copy.
5. **A case of kind M moves to its module's file, unchanged.** It lands in the existing `Test_<function>` class of the function it calls, or in `Test_module` where the module has no class for it, and keeps its name. Its helpers, fixtures and constants move with it unchanged into the destination file. One that cases bound for two files use is defined once, in one of them, which the other imports by its name, or in `tests/conftest.py` where nothing it needs at import keeps `tests/conftest.py` from loading alone, as `CONTRIBUTING.md` *The test layout* allows either. Where a destination already binds a name a moving case reads, such as its module under another registered name, a commit before the move makes the old file bind it as the destination does, and the phase record names each case that commit rewrote. Where the module is one under `tests/` with no module file yet, the phase writes `tests/test_<stem>.py`, which declares `TARGET` first after its imports and ends with `test_census = census_case(TARGET)`, as `CONTRIBUTING.md` *The test layout* states, and the move check lists it in `--to`. Each phase runs one `bin/seal layout --moved` per shipped directory it moved cases into, and records its command and last line in its phase record (G1). Where one exits 1, the phase writes the mutation table `CONTRIBUTING.md` *The test layout* asks for.
6. **A file of kind D declares its file.** Its first statement after the imports is `TARGET = "<the file every case reads>"`, and it ends with `test_census = census_case(TARGET)`. It keeps its name and its place.
7. **A file of kind T carries the reason line** of *The reason line*.
8. **A file left with no case is deleted.** Where a line under `docs/` that an unsettled design's operation holds names it, the file stays, carries the reason line `# No TARGET: a check line under docs/ names this file until the settle.`, and the phase names it in its phase record for the orchestrator's successor issue.
9. **Every citation of a moved case, a deleted file or a moved helper is rewritten in place** (contract rule 19). The phase finds them by `git grep -n` on the case's name, on the file's stem and on the helper's name, over the whole tree outside `seal/threads/`: check lines, prose under `docs/`, rule files, workflow comments, scripts' docstrings and test files, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#APPLIES_THE_SHARED_GUARD` among them. A check line names the case's new file. A line under `docs/` is edited in its English and its Korean edition alike (G9). A line an unsettled design's operation holds (G10) is not edited: the phase names it in its phase record, and the framer folds a `change` whose `from` is that operation's `to`. The grep is a sample, and the orchestrator's broad gate answers what it misses.
10. **Each docstring of a file a phase changes is brought to what the file now holds.** A sentence that says its cases wait for #923, or names where cases stood before the move, is rewritten in place.
11. **Each pair `bin/seal layout --pairs` prints carries its reason.** The docstring of the class holding the pair states, in one sentence, the input that differs between its cases where they call the function alike, such as the world a fixture or a monkeypatch builds. Where the two cases read one input and hold different facts of what the call gave, the sentence says so and names the fact each holds, and the pair counts toward the threshold below, as the pair of `tests/skills/test_session_cost.py::Test_main` does (`trail/phases/phase-8.md`); `CONTRIBUTING.md` *The test layout*'s sentence on a pair's reason states the same. A phase that moves a case into a class writes the reason for each pair the move makes there. Phase 8 writes it for each pair that stood before the build, and rewrites the threshold sentence of `CONTRIBUTING.md` *The test layout* that names a pair inside one of a module's classes, so that it counts a pair only where its class's docstring states no input its cases differ by: a pair with its reason is two cases a reader has judged distinct, so it is no ground to write the module's tests anew.
12. **The counts of *The counts* are taken at the base and at the last phase's commit**, and stand in phase 1's and phase 8's records and in the work item's `changelog.md`.
13. **The work item's `changelog.md`**, written by phase 8.

Out, each with its reason:

- **Grouping the cases that read one document into one file per document**, the direction #942's owner gave #923. The issue moves script cases and asks the rest to say why they stay. Grouping would rename every file of kind T2, losing what the issue names as the cost, finding a rule by its sentence, and would re-point most of the check lines G8 counts for a `TARGET` line and a census the sweep already runs (`frame/plan.md` A5).
- **Splitting a file whose cases read several documents.** The same grounds.
- **Renaming `tests/behaviour/test_no_document_names_the_old_roots.py`.** Its three cases are kind T1 and stay. Two lines #1488's pending operation holds name it until the settle (G10).
- **Cutting or merging a case for a pair.** A merge rewrites both cases, so the move check fails and the module owes a mutation table; a reason in the class docstring costs one sentence (`frame/plan.md` A10).
- **The `report:` lines for a public function with no class.** The issue does not name them.
- **#1484's and #1485's changes.** `frame/plan.md` *Overlap with the release*.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The empty call is not a pair | Given phase 1's commit, when `bin/seal layout --pairs` runs, then it names no pair of `tests/github/test_run_tests.py`, and the case of *Scope* item 1 fails with the reader's change reverted | phase 1, executed; the red run in its phase record |
| S2 `--all` is gone | Given phase 1's commit, when `bin/seal layout --check --all` runs, then it exits 2 for an unknown argument, and `git grep -n -e '--all' -- skills/verify/scripts/test_layout.py` lists nothing | phase 1, executed |
| S3 Fewer files declare no TARGET, and each says why | Given the last phase's commit, when `bin/seal layout --check` runs, then its last line counts fewer files that declare no `TARGET` than *The counts* gives at the base, and each file it reports holds exactly one line opening `# No TARGET: ` | phase 8, executed; the proofer reads each reason against *The kinds* |
| S4 A moved case is the case it was | Given a phase that moved cases, when its `bin/seal layout --moved` runs for each shipped directory, then each exits 0, or the phase record carries the mutation table | phases 2 to 5, executed |
| S5 The criterion ruled each case #1488 did not read | Given a phase's last commit, when its record is read, then for each file it ruled it gives the cases of *The cases #1488 read* it read whole and the asserts it kept and removed | each phase, executed by the crafter; the proofer reads kept and removed asserts against #1488's *The criterion* |
| S6 Every citation resolves | Given a phase's last commit, when `bin/seal rules --check` runs, and `git grep -n` runs for each moved case's name, each deleted file's stem and each moved helper's name outside `seal/threads/`, then the first exits 0 and the second lists only the new homes | each phase, executed |
| S7 The layout holds | Given a phase's last commit, when `bin/seal layout --check` runs, then it exits 0 | each phase, executed |
| S8 Each pair carries its reason | Given phase 8's commit, when `bin/seal layout --pairs` runs, then each pair it prints stands in a class whose docstring states the input its cases differ by, or that they read one input and the fact each holds | phase 8, executed for the list; the proofer reads each sentence |
| S9 The narrow run passes | Given a phase's last commit, when the modules *The narrow run* gives for it run in one command, then each passes | each phase, executed; the rest of the suite is `unverified`, answered by the orchestrator's broad gate |

## Data & interfaces

### The kinds

Each case is one of three kinds, read from the case whole and not from its file's name.

- **M, a module's case.** The case calls a function of one shipped module, directly or through a loader, or runs the `seal` subcommand or the script that one module is, and its asserts read what that call returned, printed, raised or wrote. A case that reads a document only to build the call's input is M. A case that holds a document's sentence against a value it takes from a module is not M, because what it asserts is the document's text. A module under `tests/` that is not a test file, such as `tests/gfm_table_oracle.py`, counts as a module here, because `CONTRIBUTING.md` *The test layout* gives it a module file at `tests/`, as `tests/test_conftest.py`, `tests/test_censuses.py` and `tests/test_workflows.py` are for theirs: a case whose subject is one such module, by calling it or by reading its own source, is M for it. A case that uses such a module only to read another file has that file as its subject, as a case that reads a workflow through `tests/workflows.py` does.
- **D, one file's case.** The case reads the text of one tracked file that is not a test file, a document, a template, a workflow or a config file, and runs no shipped code as its subject.
- **T, a case the layout has no one file for**, on one of three grounds. **T1**: it walks the tree or a whole directory of it, lists tracked files, or runs a check over the root, which is the ground `CONTRIBUTING.md` *The test layout* already states. **T2**: it holds one rule across the text of several files. **T3**: it holds one property across several modules, shipped or under `tests/`, such as a property every reader of markdown keeps.

A file's kind is the kind of the cases left in it once its M cases have moved. A file whose cases are all D on one and the same file is D. A file left with D cases on more than one file, or with any T case, is T, on the ground its cases hold. Two D files may declare the same document, and they are not merged.

### The reason line

A file of kind T carries one comment line as the first line after its imports, where `TARGET = "..."` would stand:

```python
# No TARGET: <the ground, in words>.
```

The ground names what the cases read or run, for example `# No TARGET: its cases walk every rule file of the tree.` for T1, `# No TARGET: its cases hold the sealer's rule across agents/sealer.md, the guarantee template and docs/forms/the-guarantee.md.` for T2, and `# No TARGET: its cases hold one property across every reader under lib/.` for T3. The line is prose for the next reader. No script reads it, and `git grep -c '^# No TARGET: ' -- tests` lists the files that carry it.

### The pair reader

`skills/verify/scripts/test_layout.py#_calls` compares the calls of a case's class function. After this work it also leaves out a call whose every positional and keyword argument is an empty list display `[]`, an empty tuple `()`, an empty dict display `{}` or the constant `None`. Such a call carries no input of its own, so two of them are equal whatever their cases test, as two calls with no argument are. The probe of G4 applies exactly that rule.

### The cases #1488 read

The crafter saves this script under its scratch directory (contract rule 17) and runs it as `python3 -I <script> <root>` over a tree holding `tests/text/` and `tests/behaviour/` as they stood at `18a7e18fb`, written there with `git show`, because `.gitattributes` keeps `tests/` out of `git archive`. It prints `path::case` for each case that held an assert #1488's *The listing* lists. A case of *The files* whose file and name it does not print is one *Scope* item 4 rules. A printed case #1488 still did not read is ruled the same way: each case of a file #1488's `frame/design.md:45` *Out* names, and the one case of `tests/behaviour/test_a_release_publishes_its_note.py` that line names. Phase 2 ruled `tests/text/test_ci_gives_the_checks_what_they_need.py` whole (`trail/phases/phase-2.md`). Phase 6 rules that publish-note case, and phase 7 rules `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` whole. A case another phase renamed is matched by its body.

```python
import ast
import pathlib
import sys

root = pathlib.Path(sys.argv[1])
seen = set()
for folder in ("tests/text", "tests/behaviour"):
    for path in sorted((root / folder).glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for unit in ast.walk(tree):
            if not isinstance(unit, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if not unit.name.startswith("test"):
                continue
            for node in ast.walk(unit):
                if not isinstance(node, ast.Assert):
                    continue
                for compare in ast.walk(node.test):
                    if not isinstance(compare, ast.Compare):
                        continue
                    left = compare.left
                    literal = isinstance(left, ast.JoinedStr) or (
                        isinstance(left, ast.Constant) and isinstance(left.value, str)
                    )
                    if literal and any(
                        isinstance(op, (ast.In, ast.NotIn)) for op in compare.ops
                    ):
                        seen.add(f"{path.relative_to(root).as_posix()}::{unit.name}")
for line in sorted(seen):
    print(line)
```

### The files

The 86 files, 51 under `tests/behaviour/` and 35 under `tests/text/`, holding 692 cases at `b9ca37404`, each with its cases (G6), the check lines that name it (G8) and its starting kind. The starting kind comes from G7's probe and the file's docstring, and is not a ruling: each phase reads each case whole, rules it by *The kinds*, and names in its phase record each file whose kind or destination it found otherwise (`frame/questions.md` Q1). At the start, 48 files are T2, 20 are T1, 11 are D, 5 are T3 and 2 are M, the two whose every case moves. A file with a destination in its last cell meets the move phase of that destination before the phase that files it (`frame/plan.md` *Phases*).

| File | Cases | Check lines | Starting kind | Destination of its M cases, or its document |
|---|---|---|---|---|
| `tests/text/test_a_cited_commit_outlives_the_squash.py` | 12 | 1 | T1 |  |
| `tests/text/test_a_document_has_room_for_the_next_fold.py` | 2 | 0 | T2 |  |
| `tests/text/test_a_language_section_of_writing_style_opens_alone.py` | 2 | 0 | T2 |  |
| `tests/text/test_a_merged_ticket_says_so_on_the_tracker.py` | 3 | 0 | D | `.github/workflows/label-merged-on-release-branch.yml` |
| `tests/text/test_a_moved_rule_leaves_its_definition.py` | 13 | 2 | T2 |  |
| `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py` | 7 | 1 | T2 |  |
| `tests/text/test_a_question_says_who_can_answer_it.py` | 2 | 0 | T2 |  |
| `tests/text/test_a_record_carries_no_comment.py` | 3 | 1 | T1 |  |
| `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py` | 4 | 0 | D | `.github/workflows/hygiene.yml` |
| `tests/text/test_a_rider_reaches_its_file.py` | 4 | 0 | T2 | `seal/follow-up.md`, since #1484, merged at `2e4ac4459`, removed its rider case (`frame/plan.md` *Overlap with the release*, the #1484 row) |
| `tests/text/test_a_segment_feeds_the_flow_log.py` | 13 | 2 | D | `skills/verify/orchestration.md`, where the one case reading `skills/verify/SKILL.md` goes by the criterion; T2 otherwise |
| `tests/text/test_broad_gate_rule.py` | 8 | 1 | T2 |  |
| `tests/text/test_ci_gives_the_checks_what_they_need.py` | 9 | 0 | T2 |  |
| `tests/text/test_edits_go_through_the_edit_tool.py` | 4 | 0 | T2 |  |
| `tests/text/test_every_agent_reads_the_contract.py` | 13 | 2 | T1 |  |
| `tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` | 1 | 0 | D | `CONTRIBUTING.md` |
| `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` | 2 | 0 | T1 |  |
| `tests/text/test_no_passage_is_pasted_into_a_second_file.py` | 4 | 1 | T1 |  |
| `tests/text/test_review_axes.py` | 10 | 6 | T2 |  |
| `tests/text/test_settle_reads_before_it_removes.py` | 9 | 1 | T2 |  |
| `tests/text/test_the_agent_contract_holds_the_universal_rules.py` | 11 | 3 | D | `skills/agent-contract/SKILL.md` |
| `tests/text/test_the_chain_section_has_one_shape.py` | 2 | 0 | T2 |  |
| `tests/text/test_the_direct_answer_owes_the_sealers_record.py` | 3 | 0 | T2 |  |
| `tests/text/test_the_gate_hands_cmd_a_path_it_can_run.py` | 1 | 0 | D | `templates/setup/config.md` |
| `tests/text/test_the_handoff_before_round_one.py` | 5 | 2 | T2 |  |
| `tests/text/test_the_mode_is_a_row_and_a_command.py` | 3 | 0 | T2 |  |
| `tests/text/test_the_record_is_written_in_words.py` | 3 | 3 | T2 |  |
| `tests/text/test_the_records_can_be_carried_out_and_in.py` | 2 | 0 | T2 |  |
| `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py` | 3 | 1 | T2 |  |
| `tests/text/test_the_release_tail_does_not_end_at_the_tag.py` | 7 | 2 | T2 |  |
| `tests/text/test_the_rules_claude_md_names_have_one_home.py` | 6 | 1 | T2 |  |
| `tests/text/test_the_rules_have_one_owner.py` | 13 | 4 | T2 |  |
| `tests/text/test_the_settings_have_a_front_door.py` | 7 | 2 | T2 |  |
| `tests/text/test_the_suite_runs_with_gh_logged_out.py` | 1 | 0 | D | `CONTRIBUTING.md` |
| `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py` | 3 | 0 | T2 |  |
| `tests/behaviour/test_a_body_naming_two_issues_claims_one.py` | 4 | 1 | T2 | its `issue_claims_check` case moved to `tests/github/test_issue_claims_check.py` in phase 5; phase 6 removed the case that read `templates/setup/hygiene.yml`, so the file is D on `.github/workflows/hygiene.yml` (`trail/phases/phase-6.md`) |
| `tests/behaviour/test_a_cited_section_stands_in_its_file.py` | 34 | 4 | T1 |  |
| `tests/behaviour/test_a_commit_names_its_repository.py` | 5 | 1 | T2 |  |
| `tests/behaviour/test_a_declared_label_reaches_the_tracker.py` | 4 | 0 | T2 | case calling `tracker_labels` moves to `tests/github/test_tracker_labels.py` |
| `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py` | 14 | 0 | T1 |  |
| `tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py` | 25 | 0 | M | each case moved to the module of the command it runs: `tests/skills/test_seal.py`, `test_chain_check.py`, `test_unverified_check.py`, `test_seal_stamp.py`, `test_pr_body.py`, `test_pact_check.py`, `test_broad_gate.py`, `test_settle.py` and `test_fold_check.py` in phase 4 (`trail/phases/phase-4.md`), and `tests/github/test_rules.py` in phase 5; its world went to `tests/conftest.py`, and phase 5 deleted the file (`trail/phases/phase-5.md`) |
| `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py` | 3 | 0 | T2 |  |
| `tests/behaviour/test_a_phase_hands_the_next_one_a_record.py` | 9 | 3 | T2 |  |
| `tests/behaviour/test_a_probe_that_commits_says_so.py` | 3 | 1 | T2 |  |
| `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py` | 2 | 0 | T2 | no case moves: `test_every_shipped_command_is_classified` lists `bin/` and `seal.py#TOOLS` against the file's own table, kind T1 (`trail/phases/phase-4.md`) |
| `tests/behaviour/test_a_release_is_sized_by_a_criterion.py` | 1 | 1 | D | phase 6 removed its one case, which held wording alone, and deleted the file with its check line at `docs/releasing/issues-and-milestones.md:68` (`trail/phases/phase-6.md`) |
| `tests/behaviour/test_a_release_publishes_its_note.py` | 3 | 1 | T2 | `test_the_line_the_checklist_copies_is_the_line_the_reader_reads` moved to `tests/github/test_publish_release_note.py::Test_module` in phase 5; no case calls `dist_branch.py`, since the dist case reads the workflow alone (`trail/phases/phase-5.md`); the two cases left read the workflow alone, so the file is D on `.github/workflows/publish-release.yml` (`trail/phases/phase-6.md`) |
| `tests/behaviour/test_a_release_rolls_the_flow_measurement_issue.py` | 2 | 1 | D | `docs/releasing/issues-and-milestones.md` |
| `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py` | 9 | 1 | T1 |  |
| `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` | 9 | 1 | T1 |  |
| `tests/behaviour/test_a_signer_declares_its_pact.py` | 4 | 3 | T2 | no case moves: `test_s4_the_configs_this_plugin_writes_are_silent` holds `seal.py#serialized`'s output and this repository's `seal/config.json` to `lib/config.py`, kind T3 (`trail/phases/phase-4.md`), and the two key cases hold a template's and a skill's sentence to `lib/config.py`, which *The kinds* does not make M (`trail/phases/phase-3.md`) |
| `tests/behaviour/test_a_test_file_takes_the_root_from_the_conftest.py` | 2 | 1 | T1 |  |
| `tests/behaviour/test_both_editions_carry_the_same_folds.py` | 7 | 1 | T1 |  |
| `tests/behaviour/test_chain_hooks_hardening.py` | 28 | 2 | T2 | no case moves: no case runs `hooks/core-start.py` (`trail/phases/phase-3.md`), and `test_bin_wrapper_resolves_the_checker_from_any_cwd` holds the chain from `bin/seal` through `lib/launch.py` and `seal.py` to `fold_check.py`, kind T3 (`trail/phases/phase-4.md`) |
| `tests/behaviour/test_docs_line_wrap.py` | 8 | 0 | T1 |  |
| `tests/behaviour/test_evals_layout.py` | 15 | 0 | T1 |  |
| `tests/behaviour/test_every_entry_point_runs_at_the_floor.py` | 4 | 0 | T3 |  |
| `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py` | 1 | 0 | T3 |  |
| `tests/behaviour/test_every_shipped_agent_and_document_is_measured.py` | 2 | 0 | T1 |  |
| `tests/behaviour/test_every_tracked_file_meets_every_census.py` | 1 | 0 | T1 |  |
| `tests/behaviour/test_first_setup_asks_once.py` | 31 | 4 | T2 |  |
| `tests/behaviour/test_no_document_names_the_old_roots.py` | 3 | 2 | T1 |  |
| `tests/behaviour/test_one_heading_rule_holds_to_commonmark.py` | 2 | 0 | T3 | T1: both cases read every tracked `.md` file through `git ls-files` (`trail/phases/phase-6.md`) |
| `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py` | 18 | 0 | M | the cases calling `lib/tables.py`, the two corpus cases and the case holding the corpus's `config` header moved to `tests/lib/test_tables.py` in phase 3 (`trail/phases/phase-3.md`); the three cases left hold `tests/gfm_table_oracle.py` alone, so by *The kinds* they are M for it: phase 7 moved them to a new `tests/test_gfm_table_oracle.py` and deleted the emptied file (`trail/phases/phase-7.md`) (`trail/phases/phase-6.md`) |
| `tests/behaviour/test_release_hygiene.py` | 34 | 2 | T1 |  |
| `tests/behaviour/test_settle_applies_rule_changes_in_place.py` | 1 | 0 | D | `skills/settle/rule-changes.md` |
| `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py` | 10 | 0 | T2 | cases calling `broad_gate.py` move to `tests/skills/test_broad_gate.py` |
| `tests/behaviour/test_the_contributor_has_a_procedure.py` | 10 | 1 | T2 | T1: `test_no_loaded_file_names_a_concrete_release_branch` sweeps every file the plugin loads (`trail/phases/phase-7.md`) |
| `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py` | 10 | 1 | T2 | `test_the_panel_prints_the_ref_on_the_base_row` was M and moved to `tests/skills/test_broad_gate.py::Test_panel` in phase 4 (`trail/phases/phase-4.md`) |
| `tests/behaviour/test_the_old_block_leaves_through_update.py` | 12 | 0 | T2 |  |
| `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` | 31 | 4 | T2 | no case moves: each case calling `lib/config.py` holds the file's own model of `skills/commit-pr-convention/SKILL.md` (`trail/phases/phase-3.md`), and each read of `chain_check.py` walks `git ls-files` or holds a template to that script's constants (`trail/phases/phase-4.md`); T on both the T1 and the T2 ground, since the mirror case globs `seal/threads/*/pr.*.md` and the template cases ask `git ls-files` (`trail/phases/phase-7.md`) |
| `tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py` | 12 | 0 | T3 | the cases calling one reader alone moved to `tests/lib/` in phase 3 (`trail/phases/phase-3.md`); each case left holds `tests/commonmark_oracle.py`, phase 7 moved the six whose subject is that oracle alone to a new `tests/test_commonmark_oracle.py`, and the import case, which holds the oracle and `tests/block_shapes.py`, stays, T3 (`trail/phases/phase-7.md`) |
| `tests/behaviour/test_the_release_check_watches_what_ships.py` | 12 | 2 | T1 |  |
| `tests/behaviour/test_the_release_seal_is_drawn.py` | 2 | 1 | T2 | no case moves: its one case holds the publishing workflow's install line to `run_tests.py`'s pinned versions, which *The kinds* does not make M (`trail/phases/phase-5.md`) |
| `tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py` | 3 | 0 | T2 | D on `skills/settle/rule-changes.md`: phase 5 moved the cases calling `rules.py`, and phase 7 moved `test_the_rule_marker_is_registered`, M for `tests/conftest.py`, to `tests/test_conftest.py::Test_module` (`trail/phases/phase-7.md`) |
| `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` | 13 | 1 | T2 |  |
| `tests/behaviour/test_the_sealer_guarantees.py` | 12 | 4 | T1 | `test_the_unfilled_template_is_no_guarantee`, M for `lib/fields.py`, moved to `tests/lib/test_fields.py::Test_read` (`trail/phases/phase-7.md`) |
| `tests/behaviour/test_the_set_a_work_item_always_has.py` | 6 | 0 | T2 |  |
| `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py` | 7 | 0 | T2 | no case moves: the runner case holds `seal_stamp.py --help` and `broad_gate.py --help` to one fact, kind T3, and the others read documents (`trail/phases/phase-4.md`) |
| `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` | 15 | 2 | T2 | no case moves: each case reading `run_tests.py` holds `.github/workflows/test.yml` or `CONTRIBUTING.md` to the runner's constants, which *The kinds* does not make M (`trail/phases/phase-5.md`); T1, since its cases list `bin/` (`trail/phases/phase-7.md`) |
| `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` | 8 | 0 | T2 | T1: two cases read every node id the suite collects through `tests/conftest.py#COLLECTED_NODE_IDS` (`trail/phases/phase-7.md`) |
| `tests/behaviour/test_this_repository_passes_its_own_checks.py` | 5 | 0 | T1 |  |
| `tests/behaviour/test_unverified_rows_close.py` | 5 | 1 | T2 | `test_the_fence_walks_agree_shape_by_shape` is T3 and stays (`trail/phases/phase-3.md`); since #1482 the other cases call `lib/gaps.py`, not `unverified_check.py` (read: the file's docstring at `30e82d2f8`), so none is phase 4's; phase 7 moved two to `tests/lib/test_gaps.py`, and the file is T on the T3 ground, its other case reading `templates/records/sdd-gaps.md` (`trail/phases/phase-7.md`) |
| `tests/behaviour/test_update_reads_the_config_directory_in_use.py` | 6 | 0 | D | `skills/update/SKILL.md`, where no case reads `.claude-plugin/plugin.json` as its subject; T2 otherwise |
| `tests/behaviour/test_waiver_decided_at_start.py` | 27 | 1 | T2 | T on both the T1 and the T2 ground: two cases glob `agents/*.md` and `seal/threads/*/routing.md` (`trail/phases/phase-7.md`) |
| `tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py` | 3 | 4 | T3 |  |

### The counts

Taken at the base and at phase 8's commit (*Scope* item 12), from the worktree.

| Count | Command | At `b9ca37404` |
|---|---|---|
| files that declare no `TARGET` | the last line of `bin/seal layout --check` | `139 files read, 0 refused, 86 declare no TARGET` (executed) |
| pairs | the last line of `bin/seal layout --pairs` | `139 files read, 107 pairs` (executed) |
| reason lines | `git grep -c '^# No TARGET: ' -- tests \| wc -l` | 0 (executed) |

### The narrow run

Each phase runs, in one command at its boundary, the modules it edited, the destination module files it moved cases into, and the modules that read a path it changed, taken by `git grep -l` on each changed path's name at the phase's own base. Beside them it runs `tests/behaviour/test_this_repository_passes_its_own_checks.py`, which runs `seal rules --check` and `seal layout --check` over the tree, `tests/behaviour/test_every_tracked_file_meets_every_census.py` where a file declared a `TARGET`, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` where a helper moved, `tests/github/test_rules.py` where a check line changed, and `tests/skills/test_test_layout.py` where `skills/verify/scripts/test_layout.py` changed. A module that reads a changed path by another spelling is outside the list, so the list is a sample (contract rule 12), and the orchestrator's broad gate answers the rest.

## Rule changes

- nothing
  why: No rule's sentence or grounds changes. The rules this work changes stand in `CONTRIBUTING.md` *The test layout*, a rule file outside the policy root, which the work rewrites in place. Under `docs/` it re-points the check lines and the sentences that cite a test file it moves or deletes, in both editions, under `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, as #1483's design did (design G9). A line an unsettled design's operation holds is left alone, and the framer folds a `change` for it (*Scope* item 9)

## Removes

The work adds one line form, the reason line of *The reason line*, and widens one rule of the pair reader. What goes in return is the first three rows below. The catch record of `--all`: nothing in the tree runs it outside its own cases (G11), so it has caught nothing a run could act on, and after this work it refuses each file `CONTRIBUTING.md` keeps without a `TARGET`.

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the `--all` flag, the `every` parameter and the refusals it makes, and the docstring lines that state them | `skills/verify/scripts/test_layout.py#main`, `#check` and the module docstring | nowhere: the report line and the count on `--check`'s last line name each file that declares no `TARGET`, and *The reason line* says why each one does |
| the cases that hold `--all` | `tests/skills/test_test_layout.py::Test_check::test_accepts_an_undeclared_file_as_a_report_until_every_file_is_asked`, its `every=True` half, `::Test_main::test_refuses_all_without_check`, and the `--all` word in the arguments of `::Test_main::test_refuses_a_directory_outside_a_repository` | the report half stays in a case renamed for it, and the last case keeps its refusal with `--check` alone; the flag's refusal goes with the flag |
| the sentence that `--check` "lists the files that do not declare one yet", and the sentence that the files declaring no `TARGET` are `tests/text/` and `tests/behaviour/` | `CONTRIBUTING.md` *The test layout* | rewritten in place to *The kinds* (*Scope* item 3) |
| each assert of a case #1488 did not read that pins wording, or the absence of what a shipped release removed with no rule of that text forbidding it | the cases *The cases #1488 read* does not print | nowhere: the proofer reads prose for meaning (`docs/running/what-a-script-gates.md` *The checks*); a fact one of them carried stays as a kept assert |
| each file left with no case | the M files of *The files*, and any file a phase empties | its cases stand in their module files; the phase names each deletion in its record (*Scope* item 8) |
| each docstring sentence saying a file's cases wait for #923, and each that names where moved cases stood | the files the phases change, found by `git grep -n '#923' -- tests` and by *Scope* item 9's grep | rewritten in place to what the file holds (*Scope* item 10) |
| the pairs of `tests/github/test_run_tests.py::Test_main` that G4 names | `bin/seal layout --pairs` output | nowhere: each was two calls of `main([])`, which carry no input (*The pair reader*) |

Framed 2026-11-11 by framer, before the build.

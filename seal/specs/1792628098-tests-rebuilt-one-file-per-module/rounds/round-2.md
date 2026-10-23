# 1792628098-tests-rebuilt-one-file-per-module — review round 2

target: cfb846b2 against release/v0.22.3

This round did two things at cfb846b2: it checked round 1's eight closes at c6d2bfc4, and it reviewed phase 5 as built, the commits from 8f4b7431 to cfb846b2. Every run was in a scratch clone of the target or in a second clone moved between the old commits the phase record names. The review read `spec.md` and `plan.md` at the target, with the proof of equal protection as amended at 099119b8, and 93a009c6, which the framer committed after the target, was not reviewed. Two facts were carried from round 1 and not established again: the 29 shipped scripts that compared equal by AST at 8aa42bf8, which this round compared only over 8aa42bf8..cfb846b2, and the 60 exemption comments phase 3 placed. Round 1's finding 8 is deferred to phase 7 and is not raised again.

## Findings

### 1. The records state a proof that departs from the frame in two places, and the overview names neither

severity: should
location: `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:9-15`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:82`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/plan.md:22`, `CONTRIBUTING.md:290-291`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:96`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:167`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:355`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:421`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:492`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:691`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:772`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:836`
evidence: read `seal/specs/1792628098-tests-rebuilt-one-file-per-module/plan.md:22`, `CONTRIBUTING.md:290-291`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:82`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:96`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:167`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:355`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:421`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:492`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:559`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:624`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:691`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:772`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:836`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:9-15`
verdict: fixed 73f35a4c

The overview is where a reader learns how the build departed from the frame. The sealer reads it, and the pull request body copies it. Two departures in the proof are written in the phase record and missing from the overview.

The first is when the mutants were chosen. `plan.md:22` makes choosing the mutants before the old cases are read the guard against the plan's own failure scenario, and `CONTRIBUTING.md:290-291` gives a rebuilt module's record the same order. Three tables follow it: `broad_gate.py` (`phases/phase-5.md:96`), `pact_check.py` (:559) and `hooks/root-migrate.py` (:624). Seven tables say their mutants were chosen after the old files or their cases were read: `seal_stamp.py` (:167), `hooks/commit-review-gate.py` (:355), `hooks/worktree-guard.py` (:421), `chain_check.py` (:492), `seal.py` (:691), `noninferiority.py` (:772) and `unverified_check.py` (:836). The overview's divergence table, `overview.md:9-15`, has no row for this. This finding claims no lost protection. The twelve mutants this round rebuilt from the tables' descriptions gave the verdicts the tables state (Confirmations).

The second is what the earlier proof ran. `spec.md:82` says `broad_gate.py` and `seal_stamp.py` each ran a table of about 100 mutants in both columns. `phases/phase-5.md:96` says `broad_gate.py`'s old column ran only for g1 to g9 and for each mutant the new file first let survive, and "the rest of that column was stopped for time". The proof the phase was asked for is still met: a mutant red against the new file needs no old verdict. The sentence the sealer reads in the frame is the one that is wrong.

```markdown
overview.md, ## Where spec and implementation diverged, a row after the last:

| When a module's mutants were chosen | `plan.md` *Technical context* and `CONTRIBUTING.md` *The test layout*: the mutants are "chosen from the code before the old cases are read". The tables of `seal_stamp.py`, `hooks/commit-review-gate.py`, `hooks/worktree-guard.py`, `chain_check.py`, `seal.py`, `noninferiority.py` and `unverified_check.py` were chosen after the old files were read (`phases/phase-5.md`, each module's *The mutation table*) | the tables as they ran | the frame states the order and no reason for leaving it is recorded; the orchestrator decides whether the frame's order stands or the sentence changes |

spec.md, *The proof of equal protection*, the paragraph after the bullets, its first sentence:

`broad_gate.py` and `seal_stamp.py` ran under the earlier proof, a table of about 100 mutants each: `seal_stamp.py`'s ran in both columns in full, and `broad_gate.py`'s old column ran for g1 to g9 and for each mutant the new file first let survive. Their records stay as they were written.
```

answer: The overview half was applied at bcab5b41 as two divergence rows. The framer then committed the spec half at f783cb2a: `spec.md` *The proof of equal protection* states which columns each earlier table ran, and `plan.md` drops the order of choosing the mutants from the rule. Both departures then stood in the frame, so 73f35a4c moved the two rows to the overview's *Fed back into the spec*, as finding 3 does for the earlier rows. The driver output of `broad_gate.py`'s old column (`executed` at 482fed97 by phase 5's first spawn, kept outside the tree) holds g104 red, so 28a977a2 names g104 among the old column's runs in `phases/phase-5.md:96` to match the table at :110. `CONTRIBUTING.md:290-292` is rewritten in phase 6's first step, as `plan.md`'s phase 6 row asks.

### 2. A comment in `seal_stamp.py` sends its reader to a case that is gone, and no case now measures the width it says is measured

severity: should
location: `skills/verify/scripts/seal_stamp.py:436-439`, `tests/test_seal_stamp.py`
evidence: executed `python3 refs.py clone 6046f062 cfb846b2`, `grep -n "\b80\b\|widest" tests/test_seal_stamp.py tests/test_broad_gate.py tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/test_the_seal_is_taken_once_by_the_sealer.py`, `bin/mutation-check skills/verify/scripts/seal_stamp.py --replace 'PANEL_VALUE_WIDTH = 41' 'PANEL_VALUE_WIDTH = 42' --tests "bin/test tests/test_seal_stamp.py tests/test_broad_gate.py -q -p no:xdist"`, `bin/test tests/test_tmp_r2_width.py -q -p no:xdist`
verdict: fixed d8874fc5

`skills/verify/scripts/seal_stamp.py:436-439` says the width is "Stated here and measured over there", and that `test_the_panel_value_width_is_what_the_stamp_actually_gives` "draws a value of this width and measures the stamp's widest line". That case was in `tests/test_the_gate_asks_the_range_ci_will_ask.py` at 6046f062 (line 1042). In both shapes it drew a value of `PANEL_VALUE_WIDTH` under a seven-column label, and it asserted that the widest line is exactly 80 columns. Phase 5 rewrote it. `phases/phase-5.md:120` places its behaviour in `Test_resolve_base`, `Test_moved_line`, `Test_names_a_branch`, `Test_a_runner_could_hold`, `Test_panel` and `Test_module`.

None of those classes draws the stamp at that width. `Test_panel` compares each value with `stamp.PANEL_VALUE_WIDTH` itself (`tests/test_broad_gate.py:1175`), so it moves with the constant. `Test_fit` restates the width as the literals 38 and 41 (`tests/test_seal_stamp.py:606-610`). A search of the four files that draw the stamp finds no `widest` measure and no 80-column bound. A mutant that sets the constant to 42 is red only through `Test_fit`'s literals and one `Test_guarantee_rows` case. So a deliberate change that also updates those literals ships an 81-column stamp, and no case fails. A probe ran the old measurement unchanged against today's stamp: it passes, and it is red with the constant at 42.

This is the class of comment phase 5 already rewrote in five shipped files: comments that name a test the rebuild moved (`phases/phase-5.md:406`, `:673`, `:821`). This instance was missed. A search of every tracked file outside `tests/` and the records, for test names that resolved at 6046f062 and do not resolve at the target, found it and only the `docs/worktree-guard-spec.md` and `docs/commit-review-gate-spec.md` lines that `spec.md` *Rule changes* already moves. Comments are allowed in a shipped file, and so is this fix.

```python
# tests/test_seal_stamp.py, in class Test_stamp:
    def test_accepts_a_value_as_wide_as_the_panel_at_eighty_columns(self):
        """A value of exactly `PANEL_VALUE_WIDTH` under a seven-column label,
        beside the disc, makes the stamp's widest line 80 columns, whole: the
        width is measured by drawing, not restated."""
        width = stamp.PANEL_VALUE_WIDTH
        rows = [("SEALED", ""), ("CI also", "x" * width)]
        for shape in (False, True):
            lines = [stamp.strip_ansi(line) for line in stamp.stamp(rows, shape)]
            assert max(len(line) for line in lines) == 80, lines
            assert any(line.endswith(" " + "x" * width) for line in lines), lines


# skills/verify/scripts/seal_stamp.py, lines 436 to 439:
# Stated here and measured over there, and neither may move without the other
# going red: `tests/test_seal_stamp.py`'s
# `Test_stamp::test_accepts_a_value_as_wide_as_the_panel_at_eighty_columns`
# draws a value of this width and measures the stamp's widest line.
```

answer: Applied as written, with the assertion message naming the width drawn. `Test_stamp::test_accepts_a_value_as_wide_as_the_panel_at_eighty_columns` was seen red alone through `bin/mutation-check` with `PANEL_VALUE_WIDTH` set to 42 and to 40, and green as committed. The comment at `seal_stamp.py:437-440` names the case, and `phases/phase-5.md`'s cut line for `test_the_panel_value_width_is_what_the_stamp_actually_gives` now names it as the case that holds it. The class of comment naming a moved test was not searched again; round 2's search found this instance and the `docs/` lines `spec.md` *Rule changes* moves.

### 3. The overview says nothing was fed back into the spec, but three of its divergence rows quote spec text that 95e88420 and f74be021 rewrote to match the build

severity: should
location: `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:13-15`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:35-37`
evidence: read `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:13-15`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:35-37`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:43`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:57`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:86`
verdict: fixed 6428be03

The overview template's `## Fed back into the spec` holds the clauses the work added to the spec. At the target it reads `none` (`overview.md:35-37`). Three of the five divergence rows quote spec text that no longer stands. Each was written into the spec because the build had done it:

- Row 13 quotes rule 1 at 8aa42bf8 and says "The framer writes the sentence into `spec.md` *What holds the rules*". 95e88420 wrote the whole-call rule there, and f74be021 added the no-argument rule. `spec.md:86` now states both.
- Row 14 quotes rule 2 with five verdicts. f74be021 added `left for its module`, and `spec.md:57` now holds it.
- Row 15 quotes rule 1 as "copied for each case; the copy is the reset". f74be021 added the session-id reset, and `spec.md:43` now states it.

The overview was last edited at cfb846b2, after all three spec changes. A reader of the overview is told that three behaviours diverge from a frame that now asks for them, and that nothing was fed back.

```markdown
## Where spec and implementation diverged
(rows 13, 14 and 15 removed; rows 11 and 12 stay)

## Fed back into the spec

- `spec.md` *What holds the rules*: a call whose argument reads a name the case assigns or takes as a parameter is not compared at all (95e88420), and a call with no argument is not compared either (f74be021). Inferred during implementation: c343efe9 and 00674174
- `spec.md` rule 2: the verdict `left for its module` (f74be021). Inferred during implementation: the commit gate's three old files at 54c9e803
- `spec.md` rule 1: where no case writes into the world beyond a marker keyed by a session id, the session id is the reset (f74be021). Inferred during implementation: `tests/test_commit_review_gate.py` at 54c9e803
```

answer: Applied as written, with each bullet carrying the grounds its removed row held: the 31 pairs and the revert at c343efe9, the three modules a left case pins, the cost of a copy per case. The same commit corrects three sentences of `phases/phase-5.md` that sent the reader to those rows (:212, :339, :340), each now naming the commit that wrote the clause and the overview's *Fed back into the spec*.

### 4. One old case of the root migration left the tree with no line in the record

severity: should
location: `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:652-667`
evidence: executed `python3 gone.py clone 8aa42bf8 cfb846b2 records.txt`, `bin/mutation-check hooks/root-migrate.py --replace '        if not attempted(root) and has_root(root):' '        if not attempted(root):' --replace '        if (n in marks if marks is not None else marked(root, n))' '        if True' --tests "bin/test tests/test_root_migrate.py -q -p no:xdist -x"`
verdict: fixed 9c6bff01

`spec.md` rule 2 and `CONTRIBUTING.md` *The test layout* require one line per old case that is cut or rewritten. Between 8aa42bf8 and the target, 931 test and class names left the files that held them. A script checked each one against the text of phases 2, 3 and 5 and round 1. It found 54 names that no record writes out. Fifty-three of them are covered anyway: by a sentence that names the whole old class (for example, "every case of `TestMain` under a new name" for `chain_check.py`), by "the twelve cases of the old `tests/test_broad_gate.py`", or by round 1's fix pass. One name is covered by nothing: `test_a_joined_project_holding_only_its_own_specs_hears_nothing`, in `tests/test_the_root_migrates_itself.py` at 7c2fff8c (line 601). That case guarded B1: a project with a `specs/` of its own and no `.specseal/` is left silent, with nothing staged and nothing stamped. The list at `phases/phase-5.md:652-667` and the cases left at :667 do not name it.

The case's fact is still held. A mutant that stamps without a root and a mutant that takes every directory under `specs/` as a work item are both red against `tests/test_root_migrate.py`. So the defect is the record's line, and the fix is that line.

```markdown
phases/phase-5.md, *Each old case, and where it went* of `hooks/root-migrate.py`, after the bullet held by `Test_main::test_refuses_to_speak_where_nothing_is_old_or_the_marker_answered`:

- Rewritten, held by `Test_main::test_refuses_to_speak_where_nothing_is_old_or_the_marker_answered` and `Test_main::test_accepts_only_work_items_under_specs_and_names_the_rest`: `test_a_joined_project_holding_only_its_own_specs_hears_nothing`. The first holds the silence and the missing stamp of a repository with nothing old. The second holds that a team's directory under `specs/` is neither moved nor staged.
```

answer: Applied as written, with the fact the case guarded and the two mutants. The round's two mutants were run again before the line was written, with the same command at 6428be03: 2 red.

## Confirmations

confirms: round-1#1
The close holds at the target. `skills/verify/scripts/test_layout.py#runs_the_censuses` refuses a declared file without the census line. Executed: probe P1 handed `check` the source of `tests/test_release_report.py` without that line, and the refusal named `.github/scripts/release_report.py`. Round 1's executed line was re-run with the census line dropped and a `.splitlines(` call planted in `.github/scripts/release_report.py`. `bin/test tests/test_release_report.py tests/test_censuses.py -q -p no:xdist` then failed the sweep (1 failed, 173 passed), and `bin/test-layout --check` exited 1. Both files were restored by `git checkout`.

confirms: round-1#2
The close holds. `tests/test_censuses.py` lists with `check=True` and asserts that something was listed. Executed: probe P2 patched the module's `git_listing` to return nothing, and the sweep failed with "git ls-files listed no tracked file, so the sweep judged nothing".

confirms: round-1#3
The close holds. `tests/censuses.py#_trailing` reads a comment that ends a line of code. Executed: probe P3 judged `x = 1  # exempt from splitlines: git output` in `hooks/x.py` and got the refusal at line 1. Round 1's probe had got nothing.

confirms: round-1#4
The close holds. Executed: probe P4 planted `a.splitlines() + b.splitlines()` under one exemption, and `censuses.splitlines` named line 3 with "two calls on one line".

confirms: round-1#5
The close holds for every spelling of the path. Executed: probe P5 wrote a copy of `conftest.flattened` into a declared file. `main(["--check", <path>])` named the twin, exit 1, for the relative path, the absolute path and the `./` path, and for the bare name run from `tests/`.

confirms: round-1#6
The close holds. Executed: probe P6 ran `main(["--check", "tests/test_no_such_file.py"])`. It returned 2 and printed "names no file or directory".

confirms: round-1#7
The close holds. `tests/test_conftest.py` pins `SLOW_CASE_S == 90`, and its inner run holds a slow call that fails. Executed: `bin/mutation-check tests/conftest.py` with `SLOW_CASE_S = 9000` and with the summary reading the passed reports alone, over `tests/test_conftest.py` and `tests/test_ci_gives_the_checks_what_they_need.py`: both mutants red. `phases/phase-2.md` gains the seven lines.

confirms: round-1#9
The close holds. Read: `CONTRIBUTING.md:233-235` names one class per public top-level function and lets a class or a private function have one. The heading at :265-266 states the threshold once, and the docstring at `skills/verify/scripts/test_layout.py:8-12` takes the same wording.

confirms: none
The record's case counts match a run. Executed: `pytest --collect-only` at the target gives every after count `phases/phase-5.md` states: 181, 160, 179, 13, 75, 169, 186, 106, 72, 315, 252 and 313 for the new files, and 23, 10, 62, 2, 392, 6, 197, 41, 6, 8, 5, 35 and 43 for the old files that remain. At each module's before commit, the old files give every before count: 373, 36 and 12 at 482fed97, 71 and 115 at c343efe9, 189 at 00674174, 672, 51 and 277 at 4a509442, 103 and 148 at 0e6a02b3, 126 at 2b5669e3, 68 at 3e5cbb59, 54 at 7c2fff8c, 96 and 87 at b7a1ad9d, 133 at fc09a1dd and 236 at 0eb61e14. Serial seconds on this machine sit beside the record's: for example 45.1 s against 43.4 s for the commit flow, 32.6 s against 32.7 s for `chain_check.py`, and 12.8 s against 11.4 s for `seal.py`.

confirms: none
The shipped files the phase touched change in docstrings and comments only, apart from the two the frame changes. Executed: an `ast.dump` comparison over 8aa42bf8..cfb846b2. `seal_stamp.py` and `unverified_check.py` compare equal. `hooks/root-migrate.py`, `hooks/worktree-guard.py` and `skills/implement/scripts/seal.py` compare equal once docstrings are dropped. `mutation_check.py` and `test_layout.py` differ by design. Read: each diff renames the test a comment points at, and `bin/mutation-check`, `evals/README.md`, `skills/verify/SKILL.md` and `CONTRIBUTING.md` change in prose only.

confirms: none
The per-case resets leak nothing between cases that order can show. Executed: each of the twelve new files run serially in reverse order, through a plugin outside the clone that reverses the collected items. All passed. Read: `tests/test_commit_review_gate.py` and `tests/test_worktree_guard.py` give every case its own `uuid` session id, apart from two cases that reuse one id on purpose to test a second attempt. `hooks/commit-review-gate.py#already_asked` is the only write into that world. The worktree guard's `lru_cache` is keyed by directory, and the world's directories never change which repository they are in. The commit flow hardlinks only files with the execute bit, and those are the stubs. `hooks/hook-install.py#write_stubs` replaces a stub through `os.replace`, and no case in the flow writes, removes or changes the mode of a stub.

confirms: none
Twelve mutants rebuilt from the tables' descriptions give the verdicts the tables state. Executed with `bin/mutation-check` against the new files, all red: w4 and w5 (`hooks/worktree-guard.py`); p6 and p7 (`pact_check.py`); n87; m40; s51 (`seal_stamp.py`); u14; k29; r9 and r16 (`hooks/commit-review-gate.py`). Against the old files at the commits the record names: u14, m40 and n87 SURVIVED, as the record states, and k29 is red, as it states. The commit flow's c17 SURVIVED against `tests/e2e/commit/test_commit_flow.py` and against the old commit-gate file at 00674174, as the table states. It is red against `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, which phase 6 places. A mutation score licenses *tested*, never *safe*.

confirms: none
The cut of `broad_gate.py`'s layout corpus lost no protection of the recorder it drove, on a sample of twelve. Executed: twelve mutants of `skills/verify/scripts/pytest_record/specseal_pytest_record.py`, at its decision points, against the five files that reach it today. Ten are red. The two that survive, the invocation directory read as the working directory and `wasxfail` never written, also survive the same files at 482fed97, the old sealer file's layout cases included.

confirms: none
Sampled cut lines hold against the old files at 6046f062. Read: `test_a_linked_worktree_reads_the_same_remote_tracking_refs` exercised git's own resolution, and `broad_gate.py#resolve_base` asks only git. `test_the_disc_draws_the_same_bytes_in_every_process` guarded set iteration, and `seal_stamp.py`'s one `set` is inside `sorted`. The S2 rows the commit flow left out each repeat a kind a kept row has: every left-out row commits into `main` with the variable exported, and `env -i` and `env -iS` are kept. The `\git` row cut from the worktree guard's allow is the lexer's word `git` on POSIX, and the predicate's `tokens[0] != "git"` holds it with `'git'`.

confirms: none
The Windows rows of `overview.md`'s *Not verified* are answered by CI at the target. Executed: `gh run view 39881863859` at cfb846b2. Windows shards 1 to 3 pass. Shard 4 and the ubuntu and macOS group-3 legs fail only on `test_the_durations_file_prices_the_suite`, the known red until phase 7. Run 39878465114 at 0eb61e14 reads the same.

confirms: none
The layout and the rules hold at the target. Executed: `bin/test-layout --check` exits 0 with 153 files read, 0 refused and 137 that declare no `TARGET`. `bin/test-layout --pairs tests/` names 0 pairs. `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. `bin/test tests/test_test_layout.py tests/test_censuses.py tests/test_conftest.py tests/test_release_report.py -q -p no:xdist` gives 219 passed.

confirms: none
The batch mode is the interface `spec.md` *Data & interfaces* states. Read: `skills/verify/scripts/mutation_check.py#batch_run` checks every pair before any run, runs the baseline once, then writes, runs and restores each mutant alone. The restore clears the bytecode, so the next mutant's write meets no `.pyc`. `_report_batch` exits 1 on any survivor, 2 where none survived and a run measured nothing, and 0 where every mutant is red. Executed: nine batch calls this round ran as described.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The other 750-odd mutants of the twelve tables. Their exact replacements are kept outside the tree, so this round rebuilt twelve from their descriptions and re-ran no others | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md` | the orchestrator |
| Whether `skills/implement/scripts/seal.py:307-309`, which says `Test_export` asserts the zip's namelist against the walk, reads as the case does: the case compares the namelist with the constant `MEMBERS`, which is the walk's output on its fixture | `tests/test_seal.py:698` | the orchestrator |
| Phase 4's survivors h2, h4, h6, h12, h14, h21 and h23. Phase 5 closes none, as its record says, and this round re-ran none | `tests/conftest.py` | phase 6 |
| `hooks/root-migrate.py#move`'s empty directory, which the new cases pin as shipped | `hooks/root-migrate.py` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck, unverified | the whole tree | the orchestrator, at the broad gate |
| 93a009c6, the framer's commit after the target | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md` | the next round |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the branch worktree into a scratch directory at cfb846b2, and a second clone moved between 00674174, 482fed97, 0eb61e14, 7c2fff8c, 2b5669e3 and fc09a1dd | every run below ran in one of the two; both removed after the round |
| `pytest --collect-only -q -p no:xdist` over each new and remaining old file at cfb846b2, and over each module's old files at its before commit | every count the record states, listed in Confirmations |
| `bin/test tests/test_tmp_r2_probe.py -q -p no:xdist -s`, seven cases P1 to P7, deleted after the run | 7 passed; P1 to P6 as in round 1's confirmations |
| census line of `tests/test_release_report.py` removed and a `.splitlines(` call planted in `.github/scripts/release_report.py`, then `bin/test tests/test_release_report.py tests/test_censuses.py -q -p no:xdist` and `bin/test-layout --check`; restored by `git checkout` | exit 1, the sweep failed, 173 passed; the layout check exit 1 |
| `bin/mutation-check tests/conftest.py` with two mutants over `tests/test_conftest.py` and `tests/test_ci_gives_the_checks_what_they_need.py` | 2 red |
| `python3 astcmp.py clone 8aa42bf8 cfb846b2`, a script outside the clone | 2 equal, 3 equal once docstrings are dropped, 2 changed by design |
| the twelve new files, each `bin/test <file> -q -p no:xdist -p reverse_order_r2`, with a plugin outside the clone | 12 exit 0 |
| `bin/mutation-check` batches over `hooks/worktree-guard.py`, `pact_check.py` and `hooks/commit-review-gate.py`, and single mutants over `noninferiority.py`, `hooks/root-migrate.py`, `seal_stamp.py`, `unverified_check.py` and `chain_check.py`, each against its new file with `-x` | 11 mutants, all red |
| the same tool over the old files with `--cwd` the second clone: u14 at 0eb61e14, m40 at 7c2fff8c, k29 at 2b5669e3, n87 at fc09a1dd, c17 at 00674174 | SURVIVED, SURVIVED, red, SURVIVED, SURVIVED |
| c17 against `tests/e2e/commit/test_commit_flow.py` and against `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` | SURVIVED; red |
| twelve mutants of `specseal_pytest_record.py` against the five files that reach it today, then the two survivors against the same files and `tests/test_the_gate_asks_the_range_ci_will_ask.py` at 482fed97 | 10 red, 2 SURVIVED; both SURVIVED at 482fed97 |
| `PANEL_VALUE_WIDTH` set to 40 and 42, `LABEL_WIDTH` to 8 and `GAP` to 4, against `tests/test_seal_stamp.py` and `tests/test_broad_gate.py` | all red; at 42 only `Test_fit` and one `Test_guarantee_rows` case fail |
| `bin/test tests/test_tmp_r2_width.py -q -p no:xdist`, the old width measurement as a probe, then under `PANEL_VALUE_WIDTH = 42`; deleted after | 1 passed; red |
| `python3 refs.py clone 6046f062 cfb846b2`, test names resolving at 6046f062 and not at the target, over every tracked file outside `tests/` and the records | `seal_stamp.py:438` and the `docs/` lines `spec.md` *Rule changes* moves |
| `python3 gone.py clone 8aa42bf8 cfb846b2 records.txt`, names gone from their file against the records' text | 931 gone, 54 not written out, 53 covered by a sentence naming their class or by round 1's fix pass |
| `bin/mutation-check hooks/root-migrate.py`, two mutants against `tests/test_root_migrate.py` | 2 red |
| `bin/test-layout --check`, `bin/test-layout --pairs tests/`, `bin/rules --check`, `bin/unverified-check seal/specs/` and `bin/test tests/test_test_layout.py tests/test_censuses.py tests/test_conftest.py tests/test_release_report.py -q -p no:xdist` | exit 0 with 153 read, 0 refused and 137 undeclared; 0 pairs; exit 0; exit 0; 219 passed |
| `gh run view 39881863859` and `gh run view 39878465114`, with `--log-failed` | each failing leg fails only `test_the_durations_file_prices_the_suite`; Windows shards 1 to 3 pass |

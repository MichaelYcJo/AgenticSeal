# Phase 2: 1793862998-seal-arms-is-run-by-nothing

## What this phase found

**The frame holds.** Before the build, design G14's command ran at `4526dc6c` and listed 194 lines in 19 files (executed). They were the three files that leave, the 100 entries of `.test_durations`, and the statements *Scope* items 4 to 7 name. Phase 1 moved three coordinates of *Scope* item 7. The lines of `tests/skills/test_mutation_check.py` stood at 543, 738 and 1386, and line 640 was already corrected by phase 1. The `"seal arms"` pin of `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py` stood at line 87 (executed: `grep -n`). The docstring lines 17 to 22 of that file were rewritten in phase 1, so this phase left them alone.

**Departure: two statements G14's command did not list were corrected.** Each was found by reading the paragraph around a hunk, as `agents/crafter.md` *Before you hand back, your range and the work item's records are read whole against HEAD* asks.

| Statement | What HEAD gives |
|---|---|
| `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py`, module docstring: "three modules on one corpus" | two modules, `unverified_check.py` and `coordinates.py` |
| `tests/text/test_ci_gives_the_checks_what_they_need.py#matrix_include_entries`: "Two other readings of the file remain, each asking something else" | one other reading, `tests/behaviour/test_release_hygiene.py` |

The second sentence only lost the reading that left with `tests/skills/test_arm_check.py`. Whether other modules read `.github/workflows/test.yml` was the sentence's own claim before this phase, and this phase did not survey it again.

**Decision: `_load` in the GFM module keeps registering the script in `sys.modules`.** Its docstring gave `arm_check.py`'s dataclasses as the reason, and that reason went with the script. The registration stays, because removing it would change how the two remaining scripts load, and *Scope* item 7 asks only that `arm_check._lines` and its docstring line go. Judged against `frame/design.md` *Scope* item 7.

**Decision: three sentences of `skills/verify/seal-mutate.md` were rewritten, not only cut.** The first sentence of *`seal mutate` asks condition 2 of one unit, one break at a time* compared the unit with `seal arms`'s arms. It now says what the unit can be. "That is the hole `seal arms`'s bound still has." and the closing pointer to `seal-arms.md` went whole, and the paragraph after the first cut was rewrapped. What the file says of `seal mutate` is unchanged. Judged against *Scope* item 6. The heading in `skills/verify/SKILL.md` is now `#### A unit: \`seal mutate\``. No file cited the old heading (executed: `git grep -n "A module or a unit"` printed only the heading itself, before the edit).

**Decision: the clause in `tests/skills/test_mutation_check.py` that cited `arm_check.run_arms`'s two-spaces incident went with nothing in its place.** The incident's only record in the tree was that docstring, which left with the script, and git keeps it. The case's rule is stated in the sentence before the clause. Judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*: history goes to git.

**The commit was amended once, before any record named it.** `279c2c02` became `11c848ed` to rewrap the `seal-mutate.md` paragraph where the removal left one line 94 characters wide (executed: `awk` over the line at `279c2c02`). Nothing else changed between the two (executed: `git diff 279c2c02 11c848ed --stat`, one file, three lines).

**No `seal mutate` run is owed, and three were run for S6.** The phase adds no behaviour: it deletes, and it changes the example in three existing cases. `frame/design.md` S6 asks that each rewritten case still fail against a reader that accepts any mention. `seal mutate` ran three mutants of `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py` at `279c2c02`, each against the one case it targets, and each read `red` (executed). The mutants were `return typed or script in text` to `return True` against `test_a_document_with_no_locator_is_caught`, the lookahead `(?![\w-])` dropped against `test_a_subcommand_in_prose_or_inside_a_longer_word_does_not_count`, and `SEAL.TOOLS.items()` replaced by `{}.items()` against `test_the_failure_message_offers_a_repair_that_actually_works`. The three runs together, in one call over all three cases, exited 0 with `3 red, 0 SURVIVED` (executed). The tree was clean after each run (executed: `git status --short`).

**What the plan row's commands gave.**

- Design G14's command at `11c848ed` prints nothing and exits 1. The same command at `4526dc6c` prints 194 lines, so the search can find (executed).
- `bin/seal arms` exits 2 with argparse's `invalid choice: 'arms'`, `bin/seal --help` names no `arms`, and `bin/seal mutate --help` exits 0 (executed).
- `grep -n "spec_from_file_location" skills/verify/scripts/mutation_check.py` exits 1 (executed).
- `.github/workflows/test.yml` parses as YAML with the jobs `durations`, `lint`, `pytest` and `release-report` (executed: `yaml.safe_load` through `uvx --with pyyaml`). No `needs:` named the removed job, since G14's command found no other line naming it.
- `.test_durations` lost the 100 entries of G13 and loads as JSON with 6214 entries (executed).
- The rulesets `main` and `release` require the checks `lint` and `release` alone (executed: `gh api repos/MichaelYcJo/AgenticSeal/rulesets/<id>`), so removing the `arms-grammar` job changes no ruleset.
- The phase boundary ran as one `bin/test` command at `279c2c02`'s tree over 79 modules and gave 3336 passed and 11 skipped, exit 0 (executed). The modules were every test module that names a path the phase changed (executed: `git grep -l` over `tests/` for each path), with plan row 2's modules among them. Six more were added because they walk `docs/`, `skills/` or `tests/`: `tests/github/test_rules.py`, `tests/skills/test_fold_check.py`, `tests/skills/test_test_layout.py`, `tests/skills/test_broad_gate.py`, `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py` and `tests/test_censuses.py`. After the amend, the two modules that read `seal-mutate.md`, `tests/behaviour/test_docs_line_wrap.py` and `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py`, gave 50 passed, exit 0 (executed).
- `uvx ruff check` and `uvx ruff format --check` pass on the eight Python files the phase changed (executed).

**For the orchestrator: two coordinates in `trail/phases/phase-1.md` that its commit `8eb4b2d5` contradicts.** Its line 27 places the `"seal arms"` pin of `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py` at line 90, and says the case reads `skills/verify/SKILL.md`'s section. At `8eb4b2d5` the pin is at line 87, and the case reads `skills/verify/seal-mutate.md` (executed: `git show 8eb4b2d5:<path> | grep -n`). This phase does not write `phase-1.md`.

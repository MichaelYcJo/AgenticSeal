# Phase 1: 1793599985-a-mutant-that-does-not-compile-reads-as-caught

## What this phase found

**The frame held against the tree.** Every coordinate `plan.md` *Technical context* names was opened at `e6b7f84a` and stood where it says: `mutation_check.py#mutated`, `#_held`, `#mutation_run`, `#batch_run`, `#_baseline`, `#main`, `#_line` and `#_report_batch`, the test groups and cases at the lines given, the skill's section at `:144-225`, `agents/crafter.md:133` and `bin/seal:20-21` (read). The compile behaviour design G8 and G9 record was re-measured under Python 3.15.0, 3.13.5 and 3.12.9: the syntax error, the three compile-only errors and the null byte each raise `SyntaxError`, a byte-order-marked file compiles from its bytes, and an invalid escape compiles with a `SyntaxWarning` (executed).

**A null byte's `SyntaxError` carries no line.** The frame asks the refusal to name the error's line. Under every interpreter measured, `exc.lineno` is `None` for a null byte, so a sentence built as `line {lineno}` would print `line None`. `compile_error` names the line where the error has one, and otherwise the message alone. The `null-byte` parameter of the S1 case pins it, and it went red when the branch was replaced by `if True` (M3 below). Judged against design *Scope* item 1 and *Data & interfaces*, which leave the sentence's wording to the crafter.

**The sentences the frame left to the crafter.** A refusal reads `refused: the mutant does not compile (<path>, line <N>: <message>), so the cases would fail on that error whatever the unit does. Nothing was written and the cases did not run.`, with `pair <n>: ` after `refused: ` in a batch. The not-compiled clause reads `no mutant was compiled, because <path> does not compile as it is under Python <version> (line <N>: <message>)`. It joins the first line after a semicolon and before the seconds, so the seconds stay last on the line, where the existing cases read them. The clause rides the detail that `mutation_run` returns for a red or a SURVIVED, and the baseline item of a batch, so `main` and `_report_batch` print it without a branch of their own. Grounds: design *Data & interfaces* ("the crafter words the sentences") and `skills/verify/SKILL.md` *`seal mutate` asks condition 2 of one unit, one break at a time* ("The first line printed is the verdict").

**Where the exit code sits in a red's detail now has one reader.** `_baseline` already cut `(exit N)` out of `run_cases`' red detail with `rfind`. The batch's red line needs the same code, so both read it through one helper, `_exit_of`. The no-baseline line's text is unchanged. Judged against `skills/core/SKILL.md` *The rule a mechanism is kept against* ("A fact has one source").

**Three units the scenarios did not cover got a case each.** Mutating each unit that adds behaviour found three that S1 to S7 left unwatched. Each case was added to its group in `Test_main`, and each was seen red under its mutation:

- The warnings silenced while compiling (*Scope* item 1). `test_a_warning_raised_while_compiling_is_not_printed` records warnings around a run whose target holds an invalid escape. It went red when `simplefilter("ignore")` became `"always"` (M4).
- The clause kept off a run that measured nothing (*Scope* item 2). `test_a_run_that_measured_nothing_carries_no_clause` patches `run_cases` to pass the baseline and time out the mutated run. It went red when `if uncompiled and verdict in EXIT` became `if uncompiled` (M12).
- The SURVIVED batch line staying as it was (*Scope* item 4 changes only the red line). `test_refuses_a_batch_with_a_survivor_or_a_run_with_no_verdict` gained an assertion that each SURVIVED line ends at its seconds. It went red when the red-only branch took SURVIVED too (M15).

Grounds: `agents/crafter.md` *Mutation-test every unit that adds behaviour, one command each*, and `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test*.

**How the scenarios sit in their groups, and where that departs from the scenario table.**

- S3 is a fourth parameter, `does-not-compile`, of the existing `Test_batch_run::test_refuses_every_pair_when_one_cannot_land_once`. That case already asserts the `pair <n>: ` prefix, that no case ran and that the file is unchanged, which is all S3 asks. Grounds: `agents/crafter.md` *A new test starts from its group*.
- S5 is a new case, `test_a_file_whose_name_does_not_end_in_py_is_not_compiled`, beside the markdown case, with three parameters: `notes.md`, a script with no suffix and `target.PY`. The markdown case asserts a SURVIVED through a probe that records the text it saw. S5 needs a mutant that would not compile and cases that go red on it. That is another shape, so it was not added as a parameter there.
- S4 gained a batch parameter beside the two the table names. *Scope* item 2 places the clause on the baseline line for a batch, and without that parameter nothing pinned that line (M13).

**Seen red (contract rule 15).** S1's three parameters, S3, S4's two `does-not-compile` parameters and S6 went red against the script as it stood at `e6b7f84a`. That was one run of the new cases before the script was edited: 7 failed and 9 passed. S1 printed `red ... (exit 1)` where it expected `refused`, and S6 printed `mutant 1: red (0.0s)` (executed). S2, S4, S5 and S7 went red under the mutations the scenario table names, M2, M6, M5 and M7 below.

**Mutations (executed).** Each run was one call of this worktree's `bin/seal mutate` over `skills/verify/scripts/mutation_check.py` at `7229c7459`. Its tests command was `bin/test tests/skills/test_mutation_check.py -q -p no:xdist -x -k <cases>`. All sixteen printed `red`, exit 0. Each failing case was read in the output, and each was the case named here, failing on its own assertion. Each mutant compiled: this command refuses a `.py` mutant that does not compile, and none was refused. The file was left as committed (`git status` clean after the runs).

| # | Unit | OLD to NEW | Red case |
|---|---|---|---|
| M1 | the compile call | `compile(source, path, "exec", dont_inherit=True)` to `pass` | S1 `syntax-error` |
| M2 | `compile`, not `ast.parse` | the same to `__import__("ast").parse(source, path)` | S2 `compile-only-error` |
| M3 | a line only where the error has one | `if exc.lineno else exc.msg` to `if True else exc.msg` | S1 `null-byte` |
| M4 | warnings silenced | `simplefilter("ignore")` to `simplefilter("always")` | the warning case |
| M5 | `.py` only | `if not path.endswith(".py"):` to `if False:` | S5 `markdown` |
| M6 | the original compiled first | `error = compile_error(original, path)` to `error = None` | S4 `does-not-compile` |
| M7 | the bytes, not the text | the same to `compile_error(original.decode("utf-8"), path)` | S7 `byte-order-mark` |
| M8 | the interpreter's version | `under Python {platform.python_version()}` to `under Python` | S4 `does-not-compile` |
| M9 | each mutant compiled | `error = compile_error(after.encode("utf-8"), path)` to `error = None` | S1 `syntax-error` |
| M10 | the pair's place | `place = f"pair {number}: " if numbered else ""` to `place = ""` | S3 `does-not-compile` |
| M11 | the clause on one pair's verdict | `if uncompiled and verdict in EXIT:` to `if False:` | S4 `does-not-compile` |
| M12 | only on a verdict | the same to `if uncompiled:` | the measured-nothing case |
| M13 | the clause on a batch's baseline | `f"{passed}; {uncompiled}" if uncompiled else passed` to `passed` | S4 `does-not-compile-in-a-batch` |
| M14 | the exit code on a batch red | `({_exit_of(detail)}, {seconds:.1f}s)` to `({seconds:.1f}s)` | S6 |
| M15 | red alone carries it | `if verdict == RED:` to `if verdict in EXIT:` | the `a-survivor` parameter |
| M16 | `_exit_of`'s slice | `detail.rfind("(exit ") + 1 :` to `detail.rfind("(exit ") :` | S6 |

**The lint hook strips an import added before its first use.** `hooks/lint-python.py` runs `ruff` with fixes on every save. An `import platform` or `import warnings` saved in its own edit, before the code using it, was removed at once. The first module run then failed with `NameError` in 40 cases. Each import was re-added after its use existed. A later phase that edits Python adds an import in the same edit as its first use, or after it.

**The documents.** The script's docstring, its verdict table and its batch paragraph, `skills/verify/SKILL.md`'s section and the `--replace` help now state the compile, the refusal, the `.py`-only scope, the not-compiled clause and the exit code on a batch red. The skill states the two limits, the compile's grammar and a mutant that fails at import, and names the file kinds that are not parsed. `agents/crafter.md` cites the skill for the verdicts and was not edited, as *Scope* item 5 says. S8 is read at review.

**Other places stating the reworded rules (contract rule 19).** `git grep` was run, outside `seal/threads/` and this module, for `mutant <n>`, `mutant [0-9]: red`, `refused.*nothing was written`, `any UTF-8 text file` and `land exactly once`, and for `compile` in the four documents that name `seal mutate`. It found only the script and the skill, both edited, and `hooks/routing-edit-gate.py`'s own unrelated refusal (executed). This is a search for wordings, so it is a sample in the sense of contract rule 12. `docs/what-a-script-gates.md:47` still lists `seal mutate` in the shared `ast` row. The design's `## Rule changes` amends that row at the settle, and a pull request does not edit the policy root (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*). It stands until then.

**The phase-boundary run (executed).** One `bin/test -q` call took 24 modules: the four the plan names, plus every module that names `mutation_check.py`, `seal mutate` or `skills/verify/SKILL.md`, or walks the tracked `.md` and `.py` files, found with `git grep -l`. The first run gave 1441 passed, 11 skipped and 1 failed. The failure was `test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`, which asks for this work item's `gaps.md`, written at this close. After the records were written the same command gave 1442 passed, 11 skipped, exit 0. `bin/seal layout --check tests` exited 0, with 149 files read and 0 refused. `uvx ruff check` and `uvx ruff format --check` on the two changed Python files exited 0.

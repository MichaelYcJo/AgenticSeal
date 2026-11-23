# Phase 1: 1795390621-the-broad-gate-rewrites-cmd-exe-commands

## What this phase found

**The frame holds, with three coordinates HEAD contradicts.** Each was judged against the frame's own grounding commit, `ad40d6ef8`.

- `design.md` G3 and *Scope* item 3 place `not_as_written`'s sentence *Nothing is stripped or rewritten* at `broad_gate.py:728-729`. At `ad40d6ef8` it stands at `:738-739` (read: `git show ad40d6ef8:skills/verify/scripts/broad_gate.py`). The sentence stays, as item 3 asks.
- `design.md` *Scope* item 5 and the *User scenarios* rows *The same key on a POSIX shell* and *A real `cmd.exe`* name `Test_run#test_the_row_runs_on_the_real_platform`. At HEAD that case is `Test_run#test_refuses_the_row_only_under_cmd_exe_and_runs_it_on_the_real_platform`. The grounds come next in this record.
- `design.md` *Data & interfaces* says the scan's cases answer from no filesystem. *Scope* item 4 asks that each case be driven with a root built for the case, in `Test_not_as_written`. This phase followed item 4. The scan still takes the directory question as an argument (`names_in_a_directory(command, is_directory)`), and no case drives it with a predicate of its own.

**The real-platform case is renamed so that `Test_run` keeps a refusal case.** `seal layout --check` refuses a class with no `test_refuses_` case (`skills/verify/scripts/test_layout.py` docstring, read; `tests/behaviour/test_this_repository_passes_its_own_checks.py#Test_seal_layout`, executed red at the first boundary run). `Test_run`'s one refusal case was `test_refuses_to_hide_what_cmd_exe_was_handed`, which `design.md` *Removes* takes out. The real-platform case is the one case of the class that holds a refusal: under `cmd.exe` it asserts that `bin/probe` is refused. A case that `run` refuses something would pin no guard, because `run` refuses nothing. Judged against `CONTRIBUTING.md` *The test layout* and contract rule 18, which keeps the check and changes no code to pass it.

**The key as meant is built by a second pass over the read part.** `backslashed` walks the part before the cut with `command_names` and turns each word the refused list holds. A refusal depends only on the word's text, so a word on the list is refused wherever it stands as a command name. An argument spelt the same is not a command name and keeps its `/`. `Test_not_as_written#test_refuses_each_name_and_turns_each_in_the_key_as_meant` holds that. Judged against `design.md` *Data & interfaces*, which fixes the scan's return as two lists of words.

**An empty part, `.` and `..` are answered by the root, not by a list.** `os.path.isdir(os.path.join(root, part))` answers true for all three on both platforms, since `os.path.join(root, "")` is the root with a separator. A fixed set beside it would change no output that reaches `not_as_written`, and a branch that changes no output is one no case can hold. Judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*.

**`not_as_written` writes the not-read line itself where it refuses nothing.** `design.md` *Data & interfaces* fixes its return as `str | None`, and `plan.md` *Alternatives considered* keeps one refusal site in `gate`. So the one stderr line of *Scope* item 2 is written inside the function, before it returns `None`, and is appended to the refusal where it refuses.

**A separator glued to a word is not a separator to the reading.** The reading takes a word as a command name only after a word that is exactly `&&`, `||`, `&` or `|` (*Scope* item 1). In `echo a^&& bin/x` the word before `bin/x` is `a^&&`, so `bin/x` is neither refused nor named, though `cmd.exe` would read it as a command name. The same holds for `a&& bin/x` with no caret. The case for the cut at `^` uses `echo a^& && bin/x` for that reason. Phase 2 states the bounds in `templates/setup/config.md` *Broad gate* (*Scope* item 6), and this bound is not among the ones item 6 lists.

**A name that opens with a drive is refused on Windows.** On Windows, `os.path.join(root, "C:")` is `C:`, a directory, so `C:/Python/python.exe -m pytest` is refused naming `C:\Python\python.exe`. The part names a directory on the drive and not one under the root, which is the wording of *Scope* item 1. Whether `cmd.exe` runs such a name as written is unmeasured here, because no Windows shell is in reach. `gaps.md` *Not verified* names it.

**This repository's key is refused on the Windows shards until phase 3.** `test_this_repositorys_own_config_is_answered_exactly_as_before` now passes `ROOT`, which holds `bin/`. Asked with `windows=True` and `cmd.exe`, `not_as_written` refuses `uvx ruff check . && uvx ruff format --check . && bin/test -q` naming `bin/test`, and asked with `windows=False` it returns `None` (executed: the module loaded from this worktree, over `seal/config.json`). So the four Windows shards turn that case red from this phase's commits until phase 3 changes the key (`plan.md` *Phases*, row 3). No CI leg runs before the pull request, so nothing reads that red in between.

**`Test_gate#test_refuses_a_row_it_cannot_run_and_runs_nothing` holds that `gate` asks its own root.** Its `cmd-exe-row` patches `cmd_exe_reads` to answer true, makes `bin/` in the fixture repository, and moves the working directory to one without `bin/`. Passing `os.curdir` in place of `root` at `gate`'s call turns the row red (mutant 22 below).

**The cases the Windows leg may now refuse, listed whole.** The method: every call of `gate.gate`, `gate.main`, `run_gate`, `compare_at_base` and `tool(..., "gate", ...)` in the tree, found by `git grep` over `tests/` and `evals/` for those names, then the key each case writes. Only `tests/skills/test_broad_gate.py` runs the gate over a key. `tests/skills/test_seal.py` hands `gate` to a patched `hand_over`, and `tests/skills/test_agentic_pytest_record.py` calls `read_record` and `suite_counts` alone.

| Cases | Key | Refused on `cmd.exe` |
|---|---|---|
| `Test_compare_at_base`, `Test_gate`'s runs, `LATE_ACTS`' first three rows | `{sys.executable} -m pytest -q -p no:cacheprovider tests` | no: the command name is the interpreter's path, written with `\` on Windows |
| `LATE_ACTS["row-or-interpreter"]` | the same, then `\|\| {sys.executable} -c pass` | no, for the same reason |
| `Test_main`'s `run_gate` cases, `test_s5_gate_reads_its_key_from_agentic_seal_and_names_it_where_none_is` | `{sys.executable} -c pass` | no |
| `Test_gate#test_refuses_a_row_it_cannot_run_and_runs_nothing` | no key; the key in backticks; `uvx ruff check . && bin/test -q` | the first two are refused by their own forms; the third is refused by design, with `cmd_exe_reads` patched |
| `Test_gate#test_refuses_a_root_that_is_no_repository_or_not_opted_in` | `bin/test -q` | not reached: the gate refuses at the missing root marker before it reads the key |
| `Test_main#test_accepts_the_trees_own_copy_with_the_same_arguments`, and `Test_main`'s cases that exit 2 before the key | none read: the first runs a stub gate the fixture ships | not reached |

**Seen red (contract rule 15).** Against `137db01f6`, 30 of the phase's selected cases failed (executed). The new `Test_not_as_written` cases failed on the signature, which names nothing they guard. `Test_gate`'s `cmd-exe-row` failed on its own line: the old gate rewrote the key and ran it. So each guard was then removed alone with `seal mutate` over `skills/verify/scripts/broad_gate.py` at `bf2771e11`, with `-k 'Test_not_as_written or Test_run or test_refuses_a_row_it_cannot_run'` (executed). 22 of 23 mutants were red:

1. the `cmd_exe_reads` guard removed;
2. the directory question answering true;
3. a name read only as the first word;
4. every word read as a name;
5. to 8. each of `&&`, `||`, `&` and `|` dropped from `CMD_SEPARATORS`;
9. to 11. each of `"`, `^` and `%` dropped from `CMD_CUT`;
12. the not-read list taking words before the cut;
13. a word with no `/` asked about;
14. the part split at its last `/`;
15. every command name turned in the key as meant;
16. `listed` dropping its `and`;
17. a sentence of the pinned message deleted;
18. the not-read line never written;
19. its stderr write removed;
20. the refusal not carrying it;
21. refused names not made unique;
22. `gate` passing `os.curdir` for its root.

Mutant 23, the not-read list cut to its first word, SURVIVED. `bef46c52b` added a row naming two words, and two mutants of that list, its first word only and its words not made unique, were then both red with `-k test_names_what_it_did_not_read` (executed). Each case that asserts nothing is refused was then run alone against the one mutant that removes its guard, and its failing line read (executed, outputs under the phase scratch): `[sh]` and `[another-comspec]` against mutant 1; `[no-bin]` and the glued-switch case against mutant 2; the three `call`, `echo` and argument rows against mutant 4; the no-slash case against mutant 13; the POSIX half of the real-platform case against mutant 1. Each failed on its `is None` assertion, the refusal of the name its row names printed beside it.

The `cmd.exe` half of both real-platform cases did not run, because the shell here is `/bin/sh`. The second case skipped here. `gaps.md` *Not verified* names CI's `windows-latest` leg.

**The rewriter's search.** `git grep -n -E 'handed_to_shell|command_names_backslashed|as_cmd_expands|CMD_BUILTINS|CMD_VARIABLE|handed_line|cmd\.exe was handed' -- . ':!seal/threads'` prints two lines at the phase's last commit, `tests/text/test_the_gate_hands_cmd_a_path_it_can_run.py:11` and `:12` (executed). Phase 2 removes that file.

**Where the reworded rule stands elsewhere, a sample.** `git grep` on `cmd.exe`, `three forms`, `was handed` and the rewriter's names, over `docs/`, `skills/`, `agents/`, `templates/`, `tests/` and the two root guides, finds the rule `not_as_written` now states in four more places. `templates/setup/config.md:256-308` and `skills/config/SKILL.md:115` still state the rewrite and count three forms; phase 2 rewrites both (*Scope* items 6 and 7). `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:156-176` counts three forms; phase 2 adds the fourth (*Scope* item 8). `docs/running/the-broad-gate.md` *What the gate runs* takes the rule at the settle (`design.md` *Rule changes*). A statement in other words is not reached by that search.

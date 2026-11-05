# Review round 2: 1793862998-seal-arms-is-run-by-nothing

```seal
target: e24b5fe8, fixes c40764c0..e24b5fe8
```

This verifying round read the fix diff c40764c0..e24b5fe8. That diff holds
the fix commit af0f2245, the record correction e4912226, the close blocks
at 7f1d5b2f, and e24b5fe8, the orchestrator's fold of finding 1's fix into
the frame. The probes ran in a `git clone --no-local` of the worktree
checked out at e24b5fe8, and the clone is gone. No `seal/parity.md` is
declared, so no parity comparison was owed.

Carried from round 1 as coordinates, not re-established: the base,
`release/v0.32.5` at a0303ee9; the `ast.dump` equality of the three moved
functions; design G14's empty census; the `.test_durations` count; and the
rulesets. The fix diff touches none of the files those facts rest on. Every
verdict below was reached this round.

## Findings

This round raises no finding. All four of round 1's `fixed af0f2245`
closes hold.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the fix pass claimed that the stale-cache case is gone, that
the prefix case keeps its absolute half alone, and that one `seal mutate`
run gave 3 red of 3. At HEAD the stale-cache case is gone, and
`tests/skills/test_mutation_check.py:1736-1773` is the prefix case without
its parameter (read). This round ran six mutants of
`skills/verify/scripts/mutation_check.py` against the whole module, and
all six were red (executed). Those mutants were the three of the claim and
the three holdings round 1 kept: `if prefix:` to `if prefix and cwd:`, the
hash compare to `if False:`, and `lexer.escape = ""` to `pass`. Each
holding the fix narrowed or moved was then shown against one case alone
(executed):

- `return removed` to `return []` and `if prefix:` to `if prefix and cwd:`
  were each red against the narrowed prefix case alone.
- The `cwd` join dropped was red against `Test_main`'s
  `test_a_relative_pycache_prefix_is_cleared_where_the_cases_run`
  (`test_mutation_check.py:634`), which the new docstring names.
- `os.remove(...)` to `pass` was red against `Test_main`'s
  `test_no_bytecode_for_the_mutated_file_exists_while_the_cases_run`
  (`:529`).

Both `Test_main` cases stand at a0303ee9 at lines 528 and 634 (executed:
`git show a0303ee9:tests/skills/test_mutation_check.py | grep -n`). So the
plan's *Technical context*, which states the tree at a0303ee9, is true
where it says `Test_main` also holds two of the four behaviours.
`import hashlib` and `import importlib.util` are each still read by a
remaining case. `uvx ruff check` and `uvx ruff format --check` pass on both
changed Python files (executed). The statements outside the module agree
with HEAD (read): `changelog.md:3` names the three cases and what each
holds; `gaps.md:8` names three cases; and the frame's G9, *Scope* item 2,
S2, *Not covered until #1065*, the cases row of `## Removes` and
`plan.md:7` say three cases moved. Those six are the statements the fix
pass's answer named. `skills/code-review/orchestration.md` *Orchestrator: a
phase is a fresh crafter, and a fix pass resumes the implementer*, which
the new *Judgments of the run* row cites, says the orchestrator folds them
(read). A `git grep` for the removed case's name and for the parameter ids
finds only `trail/phases/phase-1.md:15` (executed). That record states
8eb4b2d5, where the case stood. `frame/plan.md:29` still says "The four
moved cases" pass. That is phase 1's acceptance row, and it names 8eb4b2d5,
where four had moved, so HEAD does not contradict it.

```seal
confirms: round-1#2
```
What holds: the fix pass claimed that the docstring now names both other
readings. `tests/text/test_ci_gives_the_checks_what_they_need.py:266-271`
names `tests/behaviour/test_release_hygiene.py` and
`tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`
(read). A `git grep -n "test\.yml" -- tests` at HEAD lists the same six
modules as round 1 (executed). Two of them read the file through the shared
`jobs` and `matrix_include_entries`, and one writes fixtures. The release
table module slices `release-report` with its own `job_block` (lines 20,
36 and 53, executed: `grep -n`). The row at `phase-2.md:12` now names the
same two. The sentence under that table says phase 2 wrote the count
without a survey and round 1's fix pass corrected it (read).

```seal
confirms: round-1#3
```
What holds: the paragraph at `skills/verify/seal-mutate.md:99-110` is
rewrapped as round 1's fix gave it (read). `awk 'length>80'` over the file
lists only lines 16, 38 and 78, at 107, 102 and 86 columns. The same `awk`
over the file at a0303ee9 lists lines 17, 39 and 80 at the same widths
(executed). The fix pass also claimed that the range adds no prose line
over 80 columns outside `seal/threads/` except the table row of
`docs/running/what-a-script-gates.md`. `git diff a0303ee9 e24b5fe8 --
'*.md' ':!seal/threads'` adds one line wider than 80, and that line is the
table row (executed). The amend sentence at `phase-2.md:22` now says the
amend left line 105 at 99 columns and that round 1's fix pass rewrapped the
paragraph. The decision sentence above it now points to the amend (read).

```seal
confirms: round-1#4
```
What holds: `phase-1.md:27` now gives `seal-mutate.md` lines 11, 104 and
115 to 116. It gives the `"seal arms"` pin at line 87, read from
`skills/verify/seal-mutate.md`. It gives `test_mutation_check.py` lines
543, 738 and 1386. Each one matches 8eb4b2d5 (executed:
`git show 8eb4b2d5:<path> | grep -n` and `sed -n` over each file). The fix
pass claimed one more correction, in e4912226: `phase-1.md:37` now places
the moved block at lines 151 to 245. At 8eb4b2d5, line 151 is `def
clear_bytecode_cache` and line 245 is `return list(lexer)` (executed). The
closing paragraph of `phase-2.md` that handed that line to the orchestrator
is gone (read).

What matched: the five modules the fix touched or that read what it
changed pass at e24b5fe8. One `bin/test` run over `test_mutation_check.py`,
`test_ci_gives_the_checks_what_they_need.py`, `test_docs_line_wrap.py`,
`test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py` and
`test_the_release_table_reads_two_trees_and_fails_nothing.py` gave 148
passed, exit 0 (executed). That is a narrow run, not the suite. The fix
pass's counts of 229 passed and 3937 passed with 1 skipped were not
re-run.

Three things in the fix diff read badly and are no finding, since no
agent acts on them wrongly. First, G9 at `frame/design.md:17` puts its list
of the four behaviours after a colon that follows "`Test_main`". A reader
can take the list for what `Test_main` holds, though the sentence says two
of them. Second, the row at `trail/phases/phase-2.md:12` now quotes "Two
other readings" in one cell and gives "two other readings" in the other.
Only the sentence under the table says what changed. Third,
`trail/phases/phase-2.md` lost its final newline in af0f2245 (executed:
`od -c`). No check in the tree reads that.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at e24b5fe8. The crafter labelled them `unverified`, and the label is honest | the tree at `e24b5fe8` | the orchestrator, at the broad gate |
| The moved cases on Windows, including `command_words`'s default reading where `os.name == "nt"` | `tests/skills/test_mutation_check.py:1716-1798` | the `pytest` job's Windows legs in CI |
| The moved cases on any Python above 3.12 | `tests/skills/test_mutation_check.py:1716-1798` | #1065's work item, as `gaps.md:8` records |

## Probes

| Command | Result |
|---|---|
| `bin/seal mutate skills/verify/scripts/mutation_check.py` with six pairs (`os.remove(...)` to `pass`; the `cwd` join to `pass`; `return removed` to `return []`; `if prefix:` to `if prefix and cwd:`; `if back != original_sha:` to `if False:`; `lexer.escape = ""` to `pass`) against `bin/test tests/skills/test_mutation_check.py -q` | `6 mutants, 6 red, 0 SURVIVED`, exit 0; `git status --short` empty |
| the same, `return removed` to `return []` and `if prefix:` to `if prefix and cwd:`, against `-k test_a_cache_under_a_pycache_prefix_is_cleared_where_the_cases_read_it` | `2 mutants, 2 red, 0 SURVIVED` |
| the same, the `cwd` join to `pass`, against `-k test_a_relative_pycache_prefix_is_cleared_where_the_cases_run` | `red`, exit 0; that case failed |
| the same, `os.remove(...)` to `pass`, against `-k test_no_bytecode_for_the_mutated_file_exists_while_the_cases_run` | `red`, exit 0 |
| `bin/test` over the five modules named under *What matched* | 148 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over the two changed Python files | exit 0 each |

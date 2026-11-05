# Review round 1: 1793862998-seal-arms-is-run-by-nothing

```seal
target: c40764c0 against release/v0.32.5
```

This is round 1, so no earlier round's coordinate was carried; every fact
below was opened this round. The review ran in a `git clone --no-local` of
the worktree at `c40764c0`, with `release/v0.32.5` at `a0303ee9` as the base.
No `seal/parity.md` is declared, so no parity comparison was owed.

The code holds to the frame. `seal arms` is gone, `seal mutate` holds the
three functions with bodies equal to the ones it borrowed, and no statement
of the command survives outside `seal/threads/`. The four findings are a
duplicate pair of moved cases, one false sentence the diff wrote into a
docstring, and two records that misstate the commits they name.

## Findings

### 1. Two of the four moved cases hold nothing that `Test_main` does not already hold

```seal
severity: should
location: `tests/skills/test_mutation_check.py:1736-1770`, `tests/skills/test_mutation_check.py:1772-1817`, `seal/threads/1793862998-seal-arms-is-run-by-nothing/changelog.md:3`, `seal/threads/1793862998-seal-arms-is-run-by-nothing/gaps.md:8`, `seal/threads/1793862998-seal-arms-is-run-by-nothing/frame/design.md:17`, `seal/threads/1793862998-seal-arms-is-run-by-nothing/frame/design.md:33`
evidence: executed `bin/seal mutate skills/verify/scripts/mutation_check.py` with five `--replace` pairs against `bin/test tests/skills/test_mutation_check.py -q -k 'not <the four moved cases>'`, then each red pair alone with `-rf`, then `--replace '    return removed' '    return []'` against the module with only the stale-cache case deselected
```

Why it matters: design G9 (`frame/design.md:17`) grounds *Scope* item 2 on
the claim that four behaviours of the three moved functions were held only
in `tests/skills/test_arm_check.py`. That claim is true of two behaviours and
false of the other two. With the four moved cases deselected:

- If `clear_bytecode_cache` removes nothing (`os.remove(...)` becomes
  `pass`), six cases already in the module go red:
  `Test_main::test_no_bytecode_for_the_mutated_file_exists_while_the_cases_run`,
  `test_bytecode_the_baseline_wrote_is_gone_before_the_mutated_run`,
  `test_bytecode_the_cases_wrote_for_the_mutant_is_not_left_behind`,
  `test_a_same_length_mutation_reads_red_over_a_trusted_cache`,
  `test_a_relative_pycache_prefix_is_cleared_where_the_cases_run` and
  `Test_batch_run::test_accepts_each_pair_alone_after_one_baseline`. The
  first plants the import-written kind of `.pyc` through
  `plant_import_cache` (line 269).
- If the relative prefix is no longer joined to `cwd`,
  `Test_main::test_a_relative_pycache_prefix_is_cleared_where_the_cases_run`
  goes red.
- If the function returns `[]`, the moved prefix case goes red in both
  parameters without the stale-cache case. The command reads that return
  value nowhere (`mutation_check.py` lines 464, 479, 518 and 633 discard it).

So `test_a_stale_bytecode_cache_cannot_decide_a_mutants_verdict` (line 1736)
covers nothing its group does not already cover. The `relative` parameter of
`test_a_cache_under_a_pycache_prefix_is_cleared_where_the_cases_read_it`
(line 1772) is in the same position. Three moved holdings are each pinned by
a moved case alone, and they stay: the `absolute` parameter's call with no
`cwd` (`--replace '    if prefix:' '    if prefix and cwd:'` survived), the
real `restore`'s hash compare (`if back != original_sha:` to `if False:`
survived), and `command_words` on Windows (`lexer.escape = ""` to `pass`
survived). `seal layout --pairs tests/skills/test_mutation_check.py` names 0
pairs, so the repository's duplicate check could not see this.

The fix drops the stale-cache case whole and narrows the prefix case to its
absolute half. It also owes three statements outside the module.
`changelog.md:3` says "the four cases that held them moved", and
`gaps.md:8` names "The four cases phase 1 moved"; both become "two cases
and one parameter" or name the cases. Design G9 and *Scope* item 2
(`frame/design.md:17` and `:33`) are the orchestrator's to fold. A fix pass
that keeps the cases says why in its answer; a cheaper failure message is a
reason, and the release ships either way.

```python
    @pytest.mark.parametrize("relative", [True, False], ids=["relative", "absolute"])
    def test_a_cache_under_a_pycache_prefix_is_cleared_where_the_cases_read_it(
        self, tmp_path, monkeypatch, relative
    ):
```

becomes

```python
    def test_a_cache_under_a_pycache_prefix_is_cleared_where_the_cases_read_it(
        self, tmp_path, monkeypatch
    ):
        """#703. Under `PYTHONPYCACHEPREFIX` the cache is a mirror of the
        source tree under the prefix. An absolute prefix is read the same from
        anywhere, so the clear finds it with the `cwd` every call in the
        command hands it, and with no `cwd` at all. The relative prefix, read
        against the cases' `--cwd`, is held by `Test_main`'s
        `test_a_relative_pycache_prefix_is_cleared_where_the_cases_run`.

        The path the cases read is taken from `cache_from_source` itself, so
        this case asks CPython where the file is rather than repeating the
        clear's own join."""
        mc = module()
        module_path = tmp_path / "under_test.py"
        module_path.write_text("VALUE = 1\n", encoding="utf-8")
        other = tmp_path / "other"
        other.mkdir()
        prefix = str(tmp_path / "absolute-prefix")
        monkeypatch.setattr(sys, "pycache_prefix", prefix)
        planted = importlib.util.cache_from_source(str(module_path))
        # The prefix the clear reads is the environment's, as a session's would be.
        monkeypatch.setattr(sys, "pycache_prefix", None)
        monkeypatch.setenv("PYTHONPYCACHEPREFIX", prefix)

        def plant():
            os.makedirs(os.path.dirname(planted), exist_ok=True)
            with open(planted, "wb") as f:
                f.write(b"stale")

        plant()
        removed = mc.clear_bytecode_cache(str(module_path), cwd=str(other))
        assert not os.path.exists(planted)
        assert [os.path.normcase(os.path.abspath(p)) for p in removed] == [
            os.path.normcase(os.path.abspath(planted))
        ]
        plant()
        assert mc.clear_bytecode_cache(str(module_path)) and not os.path.exists(
            planted
        )
```

The stale-cache case, lines 1736 to 1770, is deleted. `import hashlib`
(line 23) stays, because the moved restore case still reads it.

```seal
verdict: fixed af0f2245
answer: The finding holds. The stale-cache case is deleted, and the prefix case keeps its absolute half alone, with a docstring that names the Test_main case holding the relative prefix. changelog.md now names the three cases that moved and what each holds, and gaps.md row 2 names the three moved cases. Shown after the fix by seal mutate over mutation_check.py against the whole module, 3 red of 3 (executed): os.remove to pass, red alone against test_no_bytecode_for_the_mutated_file_exists_while_the_cases_run; the relative prefix's cwd join dropped, red alone against test_a_relative_pycache_prefix_is_cleared_where_the_cases_run; return removed to return [], red alone against the narrowed prefix case. The three holdings kept rest on this round's survived mutants (read, not re-run). Left for the orchestrator to fold: frame/design.md lines 17, 33, 54, 67 and 79, and frame/plan.md line 7, which still say four cases or four behaviours.
```

### 2. A docstring the diff rewrote counts one other reader of `test.yml`, and the tree has two

```seal
severity: should
location: `tests/text/test_ci_gives_the_checks_what_they_need.py:266-269`, `seal/threads/1793862998-seal-arms-is-run-by-nothing/trail/phases/phase-2.md:12`
evidence: executed `git grep -l -e "test\.yml" -- tests`; read `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py:17-24`, `tests/behaviour/test_release_hygiene.py:1012-1015`
```

Why it matters: phase 2 changed `matrix_include_entries`'s docstring from
"Two other readings of the file remain" to "One other reading of the file
remains", naming `tests/behaviour/test_release_hygiene.py` alone. The phase
record says the phase "did not survey it again" (`phase-2.md:14`). A survey
finds a second one. `git grep -l "test\.yml" -- tests` lists six modules.
Two of them read the file through the shared `jobs` and
`matrix_include_entries` (`test_the_windows_leg_runs_in_shards_that_make_the_whole.py`,
`test_the_suite_has_a_command_that_is_cheap_twice.py`). One writes fixtures
(`test_deferral_check.py`). `test_release_hygiene.py` takes the floor with
its own regex. `test_the_release_table_reads_two_trees_and_fails_nothing.py`
opens `test.yml` at lines 31 and 48 and slices the `release-report` job out
with its own `job_block` (line 20). That module was already at the base
(`e391ea04`, 2026-10-28), so the sentence the diff rewrote was short of it
before. The rewrite then wrote a count that excludes it. An agent that
changes the workflow's layout reads this docstring to learn which readers
it has to update, and it would miss `job_block`. The phase record's
departure row (`phase-2.md:12`) states the same count as what HEAD gives.

```python
    entry written another way was not an entry, and nothing said so. Two
    other readings of the file remain, each asking something else:
    `tests/behaviour/test_release_hygiene.py` takes the floor from every
    `python:` in it, and
    `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`
    slices the `release-report` job out with its own `job_block`.
```

The `phase-2.md:12` row's second cell becomes: "two other readings,
`tests/behaviour/test_release_hygiene.py` and
`tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`".

```seal
verdict: fixed af0f2245
answer: The finding holds. git grep -n "test\.yml" -- tests confirms it (executed): test_the_release_table_reads_two_trees_and_fails_nothing.py reads test.yml at line 17 through its own job_block, and the windows-leg and cheap-twice modules read it through the shared functions. The docstring now names both other readings, as the fix gives. phase-2.md's row now says two, and the sentence under the table says that phase 2 wrote one without a survey and that this pass corrected it.
```

### 3. Phase 2's record says the amend rewrapped a paragraph that it left one line wider

```seal
severity: should
location: `skills/verify/seal-mutate.md:103-108`, `seal/threads/1793862998-seal-arms-is-run-by-nothing/trail/phases/phase-2.md:22`
evidence: executed `git show 279c2c02:skills/verify/seal-mutate.md | awk 'length>88'` and the same over `skills/verify/seal-mutate.md` at `11c848ed`; `git diff 279c2c02 11c848ed`
```

Why it matters: `phase-2.md:22` says `279c2c02` "became `11c848ed` to
rewrap the `seal-mutate.md` paragraph where the removal left one line 94
characters wide". At `279c2c02` that paragraph's line 103 is 94 columns.
The amend broke that line earlier and joined the rest onto line 105. At
`11c848ed` and at HEAD, line 105 is 99 columns: "outlives the verdict nor
holds it back. A process that put itself in yet another session is
outside". At the base that line was 75 columns, so the diff made it. The
file is not in `tests/behaviour/test_docs_line_wrap.py`'s `COVERED`, so no
case could see it. The paragraph alone only reads badly. The finding is the
record: the sealer reads `phase-2.md` as the account of `11c848ed`, and its
sentence claims a repair the commit does not hold.

```markdown
**The bound ends the run, not only the process it spawned.** `--timeout` is
300 seconds by default for each of the two runs, and `0` removes it. On
POSIX the command runs in a session of its own and a timed-out run's whole
process group is killed, so a wrapper's pytest does not outlive the verdict.
The group of a run that exited is ended too, and the wait is on the process
rather than on its output, so a child the cases leave behind neither
outlives the verdict nor holds it back. A process that put itself in yet
another session is outside the group and outlives the kill; the verdict
names that as the bound's limit, and cannot tell whether one did. Ctrl-C
reaches this command rather than the cases, and it ends the group before the
restore. On Windows only the direct child is ended, and the verdict says that
anything it started was not.
```

`phase-2.md:22` then states what the amend did, for example: "`279c2c02`
became `11c848ed`, which moved the 94-column line's break one line down and
left line 105 at 99 columns (executed: `git diff 279c2c02 11c848ed`); round
1's fix pass rewrapped the paragraph."

```seal
verdict: fixed af0f2245
answer: The finding holds. The cause: phase 2's rewrap Edit matched only the start of the line holding "holds it back. A process that put itself in yet another session is outside", so the rest of that line stayed joined. The paragraph is rewrapped as the fix gives, and awk 'length>80' over seal-mutate.md now lists only lines 16, 38 and 78, which are at the base too (executed). phase-2.md's amend sentence now says what the amend did and that this pass rewrapped the paragraph. Its decision sentence on seal-mutate.md now names the paragraph that was rewrapped (e4912226). Over the whole range, git diff 4526dc6c af0f2245 -- '*.md' ':!seal/threads' adds no prose line wider than 80 columns. Its one wide line is the table row of what-a-script-gates.md (executed).
```

### 4. Phase 1's record places three of phase 2's coordinates where its own commit does not have them

```seal
severity: should
location: `seal/threads/1793862998-seal-arms-is-run-by-nothing/trail/phases/phase-1.md:27`
evidence: executed `git show 8eb4b2d5:tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py | grep -n`, `git show 8eb4b2d5:skills/verify/seal-mutate.md | grep -n "seal arms"`, `git show 8eb4b2d5:tests/skills/test_mutation_check.py | grep -n`
```

Why it matters: the orchestrator relayed phase 2's note on this line
without checking it. This round checked it, and the line is wrong in three
places. It also has one coordinate that phase 2's note did not name. The
record states `8eb4b2d5`, and at that commit:

| What `phase-1.md:27` says | What `8eb4b2d5` holds |
|---|---|
| the `"seal arms"` pin at line 90 | line 87 |
| the case "reads `skills/verify/SKILL.md`'s section" | it reads `skills/verify/seal-mutate.md` (line 76, `flat("skills", "verify", "seal-mutate.md")`), and has since #1312 by its own docstring |
| `seal-mutate.md` lines 11, 105 and 116 to 117 | lines 11, 104 and 115 to 116; phase 1's own cut at line 52 moved the last two up one |

The `test_mutation_check.py` lines the sentence names (543, 738 and 1386)
are right at `8eb4b2d5`. The wrong values are the base's, carried from the
frame. Phase 2 and #706 build on this record's coordinates, which is why the
sentence has to be right.

```markdown
Phase 2 still owns the rest of those items: `seal-mutate.md` lines 11, 104
and 115 to 116; the `"seal arms"` pin at line 87 of
`test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py`, which
reads `skills/verify/seal-mutate.md`'s section; and `test_mutation_check.py`'s
lines that name `test_arm_check.py` (543), `arm_check.run_arms` (738) and
`seal arms` (1386). Each of the three still states a true fact while
`arm_check.py` stands.
```

```seal
verdict: fixed af0f2245
answer: The finding holds. All three coordinates match 8eb4b2d5 (executed: git show 8eb4b2d5 with grep -n over seal-mutate.md and the mutation test module), and phase-1.md line 27 now carries them. The sweep of phase-1.md's other coordinates against 8eb4b2d5 found one more: line 37 placed the three functions at lines 151 to 243, where the block ends at 245 with return list(lexer). That is corrected in e4912226. Its other line numbers hold at 8eb4b2d5 (executed: sed -n over each): 48, 253, 484 to 485, 520 to 523 and 719 to 723. phase-2.md's closing paragraph, which handed this line to the orchestrator, is removed.
```

## Confirmations

What matched: the move is a move. An `ast.dump` of `clear_bytecode_cache`,
`restore` and `command_words`, with the docstring dropped, compares equal
between `arm_check.py` at the base and `mutation_check.py` at HEAD
(executed). The crafter claimed the same at phase 1. `mutation_check.py`
imports `shlex` and no longer imports `importlib.util`, and `_sibling`,
`HERE`, `ARM_CHECK` and `_ARM_CHECK` are gone. Every call site of the three
functions resolves to the module's own definitions at lines 151, 201 and 224
(read).

What matched: the class of statements naming the command is empty outside
`seal/threads/`. Design G14's `git grep` exits 1 at HEAD (executed). A
wider search, which is a sample, also found nothing that names the removed
command or job: bare `arm`, `run_arms`, `arms_of`, `two_arms`, `per-arm`,
`an arm`, the quoted tokens `"arms"` and `'arms'`, the seven issue numbers,
`3.13` and `3.14` (executed). The remaining hits name the broad gate's arms,
the chain check's arms, the review and parity arms, or the evals' arms.
`.test_durations` lost exactly 100 entries, every one naming
`test_arm_check.py` or an `arm_check` parameter, gained none, and loads as
JSON with 6214 entries (executed).

What matched: the removed command refuses as the changelog says. `bin/seal
arms` exits 2 with `invalid choice: 'arms'`, and `bin/seal --help` has no
`arms` (executed). The crafter's claim of exit 2 holds.

What matched: the three rewritten cases of
`tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`
can still fail (design S6). This round re-ran the crafter's three mutants in
one `seal mutate` batch over the three cases and got `3 red, 0 SURVIVED`
(executed). This run does not tell which case caught which mutant.

What matched: the narrow modules pass at HEAD. One `bin/test` run over the
eight modules the diff changed or that hold its scenarios gave 249 passed and
8 skipped, exit 0: `test_mutation_check.py`, the four changed behaviour
modules, `test_ci_gives_the_checks_what_they_need.py`, `test_rules.py` and
`test_release_hygiene.py`. `tests/skills/test_seal.py` gave 399 passed, exit
0. The four modules that read `test.yml` gave 49 passed and 2 skipped, exit
0. `tests/behaviour/test_docs_line_wrap.py` gave 47 passed, exit 0 (all
executed). These are narrow runs, not the suite. The crafter's counts of
690 passed / 11 skipped and 3336 passed / 11 skipped were not re-run. The
second was taken at `279c2c02`, a commit no branch holds, and the amend
between it and `11c848ed` touched only `seal-mutate.md` (executed:
`git diff 279c2c02 11c848ed`, one file).

What matched: removing the job changes no ruleset. The `main` and `release`
rulesets require `lint` and `release` alone (executed: `gh api` over each
ruleset), as `docs/releasing/branch-and-release.md` now says.

What matched: each of the seven issues closes on a defect that leaves with
the script, or one `seal mutate` already answers. #687, #315 and #317 name
`arm_check.py` alone. #710's four items sit in `arm_check.py` and
`test_arm_check.py`, including its `CANNOT_LOCK`, which is gone at HEAD
(executed: `git grep`). #313 is answered by `seal mutate`'s process-group
bound. #314's traceback on `nan` and `inf` does not recur in `seal mutate`:
`--timeout nan` gives `could not run: ValueError ... No verdict.` at exit 2,
and `--timeout inf` runs unbounded (executed, probe). #312's lost-on-SIGKILL
mutation is a limit `mutation_check.py`'s docstring states under *What it
does not protect* (read), and #706 holds `seal mutate`'s restore.

What matched: the policy root's edits are the three *Scope* item 5 names, in
place, and the section *A check that cannot fail is not a check* keeps its
other two rules (read `docs/running/the-broad-gate.md:170-185`).
`tests/github/test_rules.py` passes with the check line gone (executed,
within the eight-module run).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD; the crafter labelled them `unverified`, and the label is honest | the tree at `c40764c0` | the orchestrator, at the broad gate |
| `command_words`'s default reading on Windows (`os.name == "nt"`) and the moved cases on Windows | `skills/verify/scripts/mutation_check.py:224-245` | the `pytest` job's Windows legs in CI |
| The moved cases on any Python above 3.12, now that no CI leg runs one | `tests/skills/test_mutation_check.py:1716-1842` | #1065's work item, as `gaps.md:8` records |

## Probes

| Command | Result |
|---|---|
| `bin/seal mutate skills/verify/scripts/mutation_check.py` with five pairs (no removal; no `cwd` join; `if prefix and cwd:`; `if False:` for the hash compare; `pass` for `lexer.escape = ""`) against `bin/test tests/skills/test_mutation_check.py -q -k 'not <the four moved cases>'` | `5 mutants, 2 red, 3 SURVIVED`, exit 1; mutants 1 and 2 red, 3 to 5 survived; file restored, `git status --short` empty |
| the same, mutant 1 alone with `-rf` | red; six named `Test_main` and `Test_batch_run` cases failed, 61 passed |
| the same, mutant 2 alone with `-rf` | red; `test_a_relative_pycache_prefix_is_cleared_where_the_cases_run` failed, 66 passed |
| `bin/seal mutate ... --replace '    return removed' '    return []'` against the module with only the stale-cache case deselected | red; both parameters of the moved prefix case failed, 69 passed |
| `bin/seal mutate tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py` with the crafter's three pairs against the three rewritten cases | `3 mutants, 3 red, 0 SURVIVED`, exit 0 |
| `bin/seal mutate <scratch>/test_tmp_timeout_target.py --replace 'VALUE = 1' 'VALUE = 2' --tests "python3 -c pass" --timeout nan`, then `inf` | `nan`: exit 2, `could not run: ValueError: Invalid value NaN (not a number). No verdict.`; `inf`: exit 1, `SURVIVED`; the target was restored, and then deleted with the probe |
| `ast.dump` of the three functions without docstrings, `arm_check.py` at the base against `mutation_check.py` at HEAD | all three equal |

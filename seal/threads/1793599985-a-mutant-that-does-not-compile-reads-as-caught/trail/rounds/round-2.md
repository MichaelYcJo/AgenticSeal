# Review round 2: 1793599985-a-mutant-that-does-not-compile-reads-as-caught

```seal
target: ef81822e, fixes 0a6fe9e6..ef81822e
```

This is a verifying round. Its target is the fix diff `0a6fe9e6..ef81822e`: the fix pass's `edc09b4c` and its close blocks in `1b3dd815`, then two commits the orchestrator added afterwards and asked this round to read. `0b37d14a` moves the version to `0.29.0`, and `ef81822e` folds that version into the frame. The base is now `release/v0.29.0`, the same commit `40e6c23e` as `release/v0.28.1`. The work happened in a `git clone --no-local` of the branch worktree at `ef81822e`, under `<scratchpad>/898-round-2/clone`. Every mutation run used that clone's own `bin/seal mutate`, which resolves the clone's `skills/implement/scripts/seal.py` and so the branch's `mutation_check.py`, not the installed 0.28.0 copy. No `seal/parity.md` is declared, so the round block has no `original:` line.

Carried from round 1 without re-running: where S1, S3 and S4 stand in `tests/skills/test_mutation_check.py`, that `bin/seal layout --pairs` names no pair for this module, and the `## Not judged` rows below that are marked as carried. Re-derived this round: the mutants of both findings, the module's run, and every verdict below.

## Findings

### 1. The compile's `dont_inherit=True` is pinned by no case, and the fix pass's reading that its mutant is equivalent does not hold under 3.12 and 3.13

```seal
severity: should
location: `skills/verify/scripts/mutation_check.py:222`, `tests/skills/test_mutation_check.py:742-778`
evidence: executed `bin/seal mutate skills/verify/scripts/mutation_check.py --replace 'dont_inherit=True' 'dont_inherit=False' --tests "bin/test tests/skills/test_mutation_check.py -q -p no:xdist -x"`, `bin/seal mutate skills/verify/scripts/mutation_check.py --replace 'dont_inherit=True' 'dont_inherit=False' --tests "bin/test tests/skills/test_tmp_898_round2.py -q -p no:xdist"`
```

Why it matters: design *Scope* item 1 names the call as `compile(<bytes>, <path>, "exec", dont_inherit=True)`. The fix pass's close of round-1#1 left this unit without a case and said: "Reading says that last mutant is equivalent: the one future flag the script would pass on is `annotations`, and it changes no refusal". The first half is right. `mutation_check.py:120` holds `from __future__ import annotations`, and with `dont_inherit=False` the compile at `:222` inherits it. The second half is wrong under the floor interpreter and under the repository's test interpreter. Under that flag, CPython 3.12.9 and 3.13.9 refuse a named expression, a `yield` or an `await` inside an annotation. A file without the import compiles the same text: `x: (y := 1) = 2` compiles under both, and is refused once the flag is on (`## Probes`, row 4). So with the mutant in place, `seal` running under 3.12 or 3.13 would refuse at exit 2 a mutant that compiles in the target and that the cases can run. That is a refusal the target's own grammar does not make. Under 3.15.0 the two compile the same, because those annotations are refused in every file there.

The module stayed green under the mutant: `mutant 4: SURVIVED` in the four-pair batch (`## Probes`, row 2). The fix pass took every added code line of `mutation_check.py` as its list, which is a method that makes the list whole (contract rule 12). Its verdict on this one line came from reading, and no probe tested it. Behaviour the account calls equivalent is a question until something shows it, so this line is the one unit the list leaves unwatched.

The fix is a case beside S1 in `Test_main`. It was shown red under the mutant by a probe of the same body, run under the clone's 3.13.9 virtualenv (`## Probes`, row 5). It is skipped where the interpreter refuses the annotation in every file, since the mutant is equivalent there:

```python
    @pytest.mark.skipif(
        sys.version_info >= (3, 14),
        reason="3.14 refuses a named expression in an annotation in every file",
    )
    def test_a_mutant_is_compiled_without_the_scripts_own_future_flags(
        self, tmp_path, capsys
    ):
        """`dont_inherit=True`: this script's `from __future__ import
        annotations` would refuse a named expression in an annotation, which
        a target holding no such import compiles under 3.12 and 3.13."""
        target = tmp_path / "target.py"
        target.write_text("VALUE = 1\nOTHER = 2\n", encoding="utf-8")
        code, out = run(
            [
                target,
                "--replace",
                "OTHER = 2",
                "OTHER: (y := 1) = 2",
                "--tests",
                red_on(tmp_path, target, "(y := 1)"),
            ],
            capsys,
        )
        assert code == 0, out
        assert out.startswith("red: "), out
```

```seal
verdict: fixed f8532a373
answer: The finding holds. My round-1 close called this mutant equivalent, and that was a reading with no probe behind it. Under this worktree's 3.13.9 venv and 3.12.9, `OTHER: (y := 1) = 2` compiles with no flags and is refused under `__future__.annotations.compiler_flag`. Under 3.15.0 it is refused both ways (executed). The case is the proofer's body, applied after reading it against `compile_error`, with one change in my own words: the skip is computed, not keyed to a version. `ANNOTATIONS_FLAG_REFUSES_MORE` compiles `ANNOTATED` with and without the flag on the running interpreter, and the case is skipped only where the flag changes nothing, where the mutant really is equivalent. This avoids asserting that 3.14 behaves like 3.15, which nothing here measured. The case ran, not skipped, under the 3.13.9 venv, and the module passed with 67 cases (executed). `compile_error`'s docstring now says what `dont_inherit=True` keeps out. Under this branch's own `bin/seal mutate`, the call's `dont_inherit=True` to `dont_inherit=False` reads red at `test_a_mutant_is_compiled_without_the_scripts_own_future_flags` (executed). OLD had to name the whole call, because the docstring now holds the bare words too. The file was restored and `git status` is clean.
```

### 2. The fold to 0.29.0 left the frame and the closing memo naming 0.28.1 where a reader acts on the version

```seal
severity: should
location: `seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught/frame/design.md:19-20`, `seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught/frame/plan.md:39`, `seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught/frame/plan.md:46`, `seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught/gaps.md:7`
evidence: executed `git grep -n -E '0\.28\.1' -- seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught`
```

Why it matters: `ef81822e` rewrote *Scope* item 6 and S9 to `0.29.0`. It left five sentences that still stand on the old version, and each tells a reader what to do or what the branch is:

- Design G11 (`frame/design.md:19`) tells the orchestrator how #883's and #1283's agents reach the fix. It says the installed plugin "stays 0.28.0 until 0.28.1 is released and installed", and that their worktree "is cut from `release/v0.28.1` after this pull request merges". This pull request now merges into `release/v0.29.0`. A worktree cut from `release/v0.28.1` after that merge holds no fix, and 0.28.1 will never be released.
- Design G12 (`:20`) says "This is the first pull request into `release/v0.28.1`".
- The plan's phase 2 row (`frame/plan.md:39`) still verifies "`plugin.json` reads `0.28.1` (S9)". The folded S9 now says `0.29.0` at HEAD, so the row and the scenario it cites disagree.
- The plan's *Operational impact* (`:46`) says a bare `seal` "gets the fix only once 0.28.1 is released and installed".
- `gaps.md:7` names the broad gate's answer as `seal gate --base release/v0.28.1 --record` this work item. The pull request's base is `release/v0.29.0`. Both branches are at `40e6c23e` today (`## Probes`, row 7), so the command gives the same result now, but its base no longer names the branch the pull request goes into.

Contract rule 19 asks a change to correct, in the same commit, every sentence that stood on the old fact. The listing above is every line of the work item's records that holds `0.28.1`. I left out the hits that record what happened at the time: `routing.md:17` (the owner's dated answer), `trail/phases/phase-2.md` and `trail/rounds/round-1.md`. The same search for the spelling `v0.28.1` gives no other line. Those are the two ways a version is spelt in these files, so the search covers both.

The fix, one replacement per line:

```text
design.md:19  ... the installed plugin, which stays 0.28.0 until 0.29.0 is released and installed. So a crafter, proofer or sealer of #883 or #1283 uses the fix by typing `<its worktree>/bin/seal mutate ...`, where that worktree is cut from `release/v0.29.0` after this pull request merges, or has merged it in. ...
design.md:20  ... This is the first pull request into `release/v0.29.0`, which the orchestrator cut from `release/v0.28.1` at `40e6c23e` when the release was renamed (the orchestrator's finding; `.claude-plugin/plugin.json:4` reads `"version": "0.28.0"`, read). Plan phase 2 does it.
plan.md:39    ... `git show --stat` of the commit lists both files, and `plugin.json` reads `0.29.0` at HEAD (S9). ...
plan.md:46    - A session that types a bare `seal` runs the installed plugin, and gets the fix only once 0.29.0 is released and installed. ...
gaps.md:7     | ... | the orchestrator's broad gate, `seal gate --base release/v0.29.0 --record` this work item |
```

```seal
verdict: fixed dd9ec76d
answer: Read `git show dd9ec76d` against each line the finding lists. G11 now says the installed plugin stays 0.28.0 until 0.29.0 is released, and the worktree is cut from `release/v0.29.0`. G12 names the first pull request into `release/v0.29.0`, renamed from `release/v0.28.1`. The plan's phase 2 row reads `0.29.0` at HEAD (S9). *Operational impact* says the fix arrives once 0.29.0 is released. `gaps.md:7` names `--base release/v0.29.0`. All five are fixed (read). A `0\.2[89]\.[01]` search over the work item's records at HEAD found one more line that still stands on the old version, outside both the finding's listing and dd9ec76d: `frame/plan.md:14`, *Technical context* "The version", which says `docs/branch-and-release.md` *Cutting a release* "puts the move to `0.28.1` in the commit that adds the release's first fragment". The crafter's definition allows no edit to `frame/plan.md` outside the Status cell, so that line is for the orchestrator. The other hits record what happened at the time, and they stand: design G4's milestone read, *Scope* item 6's history clause, the plan's *Judgments of the run* row, `routing.md:17`, the phase records and the round records.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: S1 at `tests/skills/test_mutation_check.py:774` now asserts `out.startswith("refused: the mutant does not compile")`, so a `pair 1:` on a one-pair call fails it. Under the clone's `bin/seal mutate`, `numbered=False` to `numbered=True` at the single call site (`skills/verify/scripts/mutation_check.py:386`) went red, and the failing case was `test_a_python_mutant_that_does_not_compile_is_refused_before_any_write[syntax-error]`. The fix pass also claimed the batch call site, and that claim holds: `numbered=True` to `numbered=False` at `:443` went red at `Test_batch_run::test_refuses_every_pair_when_one_cannot_land_once[does-not-compile]` (executed, `## Probes` rows 2 and 3). The close's sentence on the units still without a mutant is answered by finding 1 of this round, which takes up only `dont_inherit=True`.

```seal
confirms: round-1#2
```
What holds: S4 at `tests/skills/test_mutation_check.py:781-852` has the new parameter `a-survivor-of-a-file-that-does-not-compile`. It was read as code. Its marker `NOT IN THE FILE` is in neither the original nor the mutant, so `FAILS_ON_THE_MUTANT` exits 0 against both. The baseline passes, the verdict is `SURVIVED`, and `main` exits 1. The case asserts that exit, the `SURVIVED: ` first word, the clause, the interpreter's version, the original's `line 2:`, and the file's bytes after the run. The new `exits` column replaces the literal `0` for the other three parameters with the same value, and their `marker` is the old `"VALUE = 2"`, so they assert what they asserted before. In its group, the parameter covers the one half of `verdict in EXIT` that no other case covers. `if uncompiled and verdict in EXIT:` to `if uncompiled and verdict == RED:` at `skills/verify/scripts/mutation_check.py:409` went red, and the failing case was this parameter (executed, `## Probes` rows 2 and 3). The module passed whole at `ef81822e`, 66 cases (executed, `## Probes` row 1).

```seal
confirms: none
```
What holds: the fix pass's claim that it set every added code line of `mutation_check.py` against a mutant and found three left. I listed the added lines (`git diff 40e6c23e ef81822e -U0 -- skills/verify/scripts/mutation_check.py`, executed). I then set each code line against phase 1's M1 to M16, round 1's six pairs and the fix pass's two. Every line except three has a mutant that went red. The first exception is the clause's sentence at `:242-245`, past the parts M8 and the S4 assertions pin. The second is the refusal's sentence at `:250-254`, past the opening that S1 now pins. Design *Data & interfaces* leaves both wordings to the crafter. The third is `dont_inherit=True`, which is finding 1 (read). `with warnings.catch_warnings()` has no mutant of its own. It only restores the filter after the call, in a process that ends after one run, and M4 watches the filter itself (read). So the list holds as the fix pass gave it, apart from its verdict on `dont_inherit`.

```seal
confirms: none
```
What holds: the fix pass's statement that `trail/phases/phase-1.md` *Three units the scenarios did not cover got a case each* is now known to be incomplete and stands as the phase's record. I weighed it and found no defect. The phase record is the crafter's account of what that phase ran. Round 1's finding 1 records the correction, with the method and the two units it missed, and the fix pass's close says where the sentence stands. `skills/core/SKILL.md` *The rule a mechanism is kept against* sends history to "git, the release notes and the work record", and a phase record is work record. A sealer that reads the phase record also reads both rounds (read).

```seal
confirms: none
```
What holds: the version line and the folded frame agree with `docs/branch-and-release.md` *Cutting a release*. "The version moves at the start of a release, in the first pull request into `release/vX.Y.Z`": `origin/release/v0.29.0` and `origin/release/v0.28.1` both stand at `40e6c23e`, which is this branch's base, so no pull request has landed in the renamed release (executed, `## Probes` row 7). Milestone 81 reads `release: 0.29.0`, and its description records the rename from 0.28.1 (executed). `.claude-plugin/plugin.json:4` reads `"version": "0.29.0"` at `ef81822e` (read). The section also says "The orchestrator moves it in the commit that adds the changelog fragment". On the branch the move is two commits: `b17253e5`, with the fragment, and `0b37d14a`. The section's table squashes a feature branch into `release/vX.Y.Z`, so the release branch receives one commit that holds both (read: `docs/branch-and-release.md:145-150`). *Scope* item 6 says this in its own words, and the plan's *Judgments of the run* row cites the section (read). The 19 test modules that name `.claude-plugin` or `plugin.json`, with `tests/test_censuses.py`, passed at `ef81822e`: 1395 passed, 1 skipped (executed, `## Probes` row 6). Both commits carry the `Seal-Routing:` trailer (read: `git show`).

```seal
confirms: none
```
What holds: the fix pass's count of 1443 passed and 11 skipped at `edc09b4c` was read and not re-run. This round ran the narrower module set named in `## Probes` instead (contract rule 2).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `ef81822e`. The hand-back's narrow count was read, not re-run, and `gaps.md` labels the broad run `unverified`. That label is honest. | `seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught/gaps.md` | the orchestrator's broad run, `seal gate --base release/v0.29.0 --record` this work item |
| Whether the new cases pass on CI's four `windows-latest` legs, on Python 3.12 (`frame/questions.md` Q1; carried from round 1). Finding 1's case would run there and not be skipped. | `tests/skills/test_mutation_check.py` | the orchestrator, reading the pull request's CI run |
| Whether the five commits without a `Seal-Routing:` trailer are rewritten before the pull request, or left for the squash to replace (carried from round 1). | `skills/commit-pr-convention/SKILL.md:185-187` | the orchestrator |
| The pull request body's statements that `CONTRIBUTING.md` *What a change to a gate must carry* asks for. No body exists at this round (carried from round 1). | `CONTRIBUTING.md` | the sealer, reading `seal pr-body`'s file |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_mutation_check.py -q -p no:xdist`, in the clone at `ef81822e` | 66 passed, exit 0 |
| `bin/seal mutate skills/verify/scripts/mutation_check.py` with four pairs (`numbered=False` to `numbered=True` at the single call, `verdict in EXIT` to `verdict == RED`, `numbered=True` to `numbered=False` at the batch call, `dont_inherit=True` to `dont_inherit=False`) and `--tests "bin/test tests/skills/test_mutation_check.py -q -p no:xdist -x"`, from the clone | baseline passed; mutants 1 to 3 `red (exit 1, ...)`; mutant 4 `SURVIVED`; exit 1 |
| The first three of those pairs, each run alone with the same tests command | each `red ... (exit 1)`, exit 0. The failing cases were S1 `syntax-error`, S4 `a-survivor-of-a-file-that-does-not-compile` and S3 `does-not-compile`, in that order |
| A script `<scratchpad>/898-round-2/probe_flags.py`, run with `-I` under `python3` 3.15.0, `python3.12` 3.12.9 and the clone's `.venv` 3.13.9. It compiled six annotation sources over bytes with `dont_inherit=True`, once with no flags and once with `__future__.annotations.compiler_flag`. It was then deleted. It was written through a shell heredoc, not the Write tool, and not named `test_tmp_*`. Both are departures from the proofer's probe rules, and both are reported here | under 3.12.9 and 3.13.9, `x: (y := 1) = 2`, `def f(x: (y := 1))` and a local `x: (yield) = 1` compile with no flags and are refused with the flag; under 3.15.0 all six are refused both ways |
| A probe `tests/skills/test_tmp_898_round2.py`, written with the Write tool and holding finding 1's case as a module-level function. It ran as `bin/seal mutate skills/verify/scripts/mutation_check.py --replace 'dont_inherit=True' 'dont_inherit=False' --tests "bin/test tests/skills/test_tmp_898_round2.py -q -p no:xdist"`, then was deleted | baseline passed; `red ... (exit 1)`, exit 0. The failure was `refused: the mutant does not compile (..., line 2: named expression cannot be used within an annotation)` against `assert code == 0`. The file is gone, and `git status` is clean |
| `bin/test` over the 19 modules `git grep -l -E '\.claude-plugin|plugin\.json' -- 'tests/*.py'` lists, without `tests/censuses.py`, plus `tests/test_censuses.py`, at `ef81822e` | 1395 passed, 1 skipped, exit 0 |
| `git ls-remote --heads origin 'release/*'` from the branch worktree; `gh api repos/MichaelYcJo/SpecSeal/milestones/81` | `release/v0.28.1` and `release/v0.29.0` both at `40e6c23e`; the milestone's title is `release: 0.29.0` |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.29.0 --root <branch worktree> --worktree`, the plugin's copy, after this record was written | exit 0. It refused only this record's findings 1 and 2, as open for want of a close block, and named the absent gate record and guarantee file. It printed no notice at a line of `frame/design.md` |

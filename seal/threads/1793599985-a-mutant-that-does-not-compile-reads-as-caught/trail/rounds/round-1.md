# Review round 1: 1793599985-a-mutant-that-does-not-compile-reads-as-caught

```seal
target: 95e7dea7 against release/v0.28.1
```

This is the first round, so no earlier round's coordinates were carried; every fact below was established this round. The work happened in a `git clone --no-local` of the branch worktree at `95e7dea7`, under the round's scratch directory `<scratchpad>/898-round-1/clone`. Every mutation run used that clone's own `bin/seal`, which resolves the clone's `skills/implement/scripts/seal.py` and so runs the fixed `mutation_check.py` at `95e7dea7`, not the installed 0.28.0 copy. No `seal/parity.md` is declared, so the round block has no `original:` line.

## Findings

### 1. A single pair's compile refusal could name a pair, and no case would notice

```seal
severity: should
location: `tests/skills/test_mutation_check.py:742-778`, `skills/verify/scripts/mutation_check.py:386`
evidence: executed `bin/seal mutate skills/verify/scripts/mutation_check.py --replace 'compiled(path, original, [after], numbered=False)' 'compiled(path, original, [after], numbered=True)' --replace 'if uncompiled and verdict in EXIT:' 'if uncompiled and verdict == RED:' --replace 'error = compile_error(after.encode("utf-8"), path)' 'error = compile_error(after, path)' --replace 'if exc.lineno else exc.msg' 'if True else exc.msg' --replace '({_exit_of(detail)}, {seconds:.1f}s)' '({seconds:.1f}s)' --replace 'as it is ({_exit_of(detail)}), so' 'as it is (), so' --tests "bin/test tests/skills/test_mutation_check.py -q -p no:xdist -x"`
```

Why it matters: `mutation_run` passes `numbered=False` to `compiled` at `skills/verify/scripts/mutation_check.py:386`, so a single pair's refusal reads `refused: the mutant does not compile (...)`, with no place. That choice is a unit that adds behaviour. With `numbered=True` a single run would print `refused: pair 1: the mutant does not compile ...`, which tells the reader of a one-pair call about a pair list it never gave. Pair 1 of the batch above made exactly that mutant, and the module stayed green: `mutant 1: SURVIVED`. The S1 case at `tests/skills/test_mutation_check.py:773` asserts only `out.startswith("refused: ")`, and `"does not compile" in out` holds either way.

The phase record claims "Mutating each unit that adds behaviour found three that S1 to S7 left unwatched" (`trail/phases/phase-1.md`, *Three units the scenarios did not cover got a case each*) and lists sixteen mutants as that run. I took the new code apart into its units: `compile_error`, `compiled`, the two call sites, the clause's join on a verdict and on the baseline, `_exit_of`, and `_report_batch`'s two branches. I then set each unit against the sixteen mutants and the new cases. Two units no mutant of the sixteen touched survived their mutants: this one and finding 2's. So the sixteen were a sample handed back as the whole list (contract rule 12). The units left out of my own list are wording alone, such as the path inside the clause and the refusal's sentence, which design *Data & interfaces* leaves to the crafter, and the order of the compile after every pair lands, which a text replacement cannot move.

The fix is one assertion, replacing line 773. It was shown red under this mutant by a probe (`## Probes`, last row):

```python
        assert code == 2, out
        assert out.startswith("refused: the mutant does not compile"), out
```

### 2. The not-compiled clause on a single pair's SURVIVED is pinned by no case

```seal
severity: should
location: `tests/skills/test_mutation_check.py:780-823`, `skills/verify/scripts/mutation_check.py:409`
evidence: executed `bin/seal mutate skills/verify/scripts/mutation_check.py --replace 'compiled(path, original, [after], numbered=False)' 'compiled(path, original, [after], numbered=True)' --replace 'if uncompiled and verdict in EXIT:' 'if uncompiled and verdict == RED:' --replace 'error = compile_error(after.encode("utf-8"), path)' 'error = compile_error(after, path)' --replace 'if exc.lineno else exc.msg' 'if True else exc.msg' --replace '({_exit_of(detail)}, {seconds:.1f}s)' '({seconds:.1f}s)' --replace 'as it is ({_exit_of(detail)}), so' 'as it is (), so' --tests "bin/test tests/skills/test_mutation_check.py -q -p no:xdist -x"`
```

Why it matters: design *Scope* item 2 puts the clause on "the verdict line for one pair", and `mutation_run`'s docstring at `skills/verify/scripts/mutation_check.py:382` says "A red or a SURVIVED carries `compiled`'s clause". The code does that through `verdict in EXIT` at `:409`. Every parameter of the S4 case at `tests/skills/test_mutation_check.py:780-823` runs cases that go red on the mutant, so only the red half is watched. Pair 2 of the batch above narrowed the condition to `verdict == RED`, and the module stayed green: `mutant 2: SURVIVED`. Under that mutant, a SURVIVED on a file `seal` could not compile would say nothing about the compile having been skipped. M11 and M12 in `trail/phases/phase-1.md` mutate the same line, but each one changes the red case or the timed-out case, never the SURVIVED case. Finding 1 gives the method that found both units.

The fix is a parameter of S4 whose cases pass against the mutant. A probe showed a case of this shape go red under the mutant (`## Probes`, last row):

```python
    @pytest.mark.parametrize(
        ("source", "pairs", "marker", "exits", "first_word", "uncompiled"),
        [
            (b"VALUE = 1\nprint(\n", [("VALUE = 1", "VALUE = 2")], "VALUE = 2", 0, "red", True),
            (
                b"VALUE = 1\nprint(\n",
                [("VALUE = 1", "VALUE = 2")],
                "NOT IN THE FILE",
                1,
                "SURVIVED",
                True,
            ),
            (
                b"VALUE = 1\nprint(\n",
                [("VALUE = 1", "VALUE = 2"), ("VALUE = 1", "VALUE = 2 ")],
                "VALUE = 2",
                0,
                "baseline",
                True,
            ),
            (b"\xef\xbb\xbfVALUE = 1\n", [("VALUE = 1", "VALUE = 2")], "VALUE = 2", 0, "red", False),
        ],
        ids=[
            "does-not-compile",
            "a-survivor-of-a-file-that-does-not-compile",
            "does-not-compile-in-a-batch",
            "byte-order-mark",
        ],
    )
    def test_a_python_file_is_compiled_as_it_is_before_its_mutants(
        self, tmp_path, capsys, source, pairs, marker, exits, first_word, uncompiled
    ):
        # The body as it stands, with `red_on(tmp_path, target, marker)` in place
        # of `red_on(tmp_path, target, "VALUE = 2")` and `assert code == exits, out`
        # in place of `assert code == 0, out`.
```

## Confirmations

```seal
confirms: none
```
What holds: claimed that a `.py` mutant that does not compile is refused at exit 2 before anything is written or run. `compiled` runs at `skills/verify/scripts/mutation_check.py:386` and `:443`, after `mutated` has landed every pair and before `_environment`, the bytecode clearing and `_baseline`. A `Refused` reaches `main`'s `refused:` branch at exit 2 (read). The S1 case asserts the unchanged directory snapshot and that the logging cases never ran. The whole module passed at `95e7dea7`, 65 cases (executed, `## Probes` row 1).

```seal
confirms: none
```
What holds: a sample of the crafter's sixteen mutation runs. M3 (`if True else exc.msg`) and M14 (the exit code dropped from a batch red) read `red (exit 1, ...)` again under the clone's `bin/seal mutate`. Two units the table does not list also went red: each mutant compiled from its text rather than its bytes, which the byte-order-mark parameter catches, and `_baseline`'s use of `_exit_of` (executed, `## Probes` row 2). Every mutant in that batch compiled; none was refused. The crafter's claim that its seven cases failed at `e6b7f84a` before the edit was read and not re-run. The base has no compile step and printed `mutant <n>: red (<s>s)`, so S1, S3 and S6 cannot pass there (read: `git diff 40e6c23e 95e7dea7 -- skills/verify/scripts/mutation_check.py`).

```seal
confirms: none
```
What holds: the batch red line `mutant <n>: red (exit <N>, <s>s)` at `skills/verify/scripts/mutation_check.py:705` reads its code through `_exit_of` (`:530-532`). Only a `run_cases` red reaches that branch, and that detail ends in `(exit N)` (`:355-359`). The clause is joined only to a single pair's detail (`:409-410`) and to the baseline's item (`:456-457`), never to a batch red, so the slice to the last `)` cannot meet the clause's own parenthesis (read). `_baseline`'s no-baseline sentence prints the same `(exit N)` it printed before (read; its mutant went red, `## Probes` row 2).

```seal
confirms: none
```
What holds: the account's departures. A null byte's `SyntaxError` carries no line, and `compile_error` prints the message alone (`skills/verify/scripts/mutation_check.py:224`), which the `null-byte` parameter pins (read; M3 red, executed). S3 is a fourth parameter of `test_refuses_every_pair_when_one_cannot_land_once` (`tests/skills/test_mutation_check.py:118-133`), and that case already asserts the `pair <n>:` prefix, an unchanged file and no run (read). S5 is its own case at `:1353-1378`, because the markdown case's probe asserts a SURVIVED (read). Each new case covers behaviour no case of its group covered. `seal layout --pairs` names no pair in this module (executed, `## Probes` row 3).

```seal
confirms: none
```
What holds: design S8. The docstring (`skills/verify/scripts/mutation_check.py:22-31`, `:46-47`, `:60-67`), the `--replace` help (`:583-586`) and `skills/verify/SKILL.md:159-177`, `:196-197`, `:205-216` state the compile, the refusal, the `.py`-only scope, the not-compiled clause, the exit code on a batch red and the two limits (read). `agents/crafter.md:133` sends a reader to the skill for the verdicts and needed no edit (read). A search for the changed lines' wordings outside `seal/threads/` and `tests/` found only the script and the skill (executed, `## Probes` row 4). The `from:` of design `## Rule changes` is `docs/what-a-script-gates.md:47` character for character. `chain_check.py --worktree` refused nothing in the design (executed, `## Probes` row 5), and its run printed no notice at a line of `frame/design.md`.

```seal
confirms: none
```
What holds: design S9 and *Scope* item 6. `git show --stat b17253e5` lists `.claude-plugin/plugin.json`, one line changed to `"version": "0.28.1"`, and this work item's `changelog.md`, and nothing else (executed). That is what `docs/branch-and-release.md:31-43` asks of the release's first pull request. The version line was judged as the frame wrote it, as the spawn prompt asked; the possible rename to 0.29.0 is a later commit. The changelog's sentences match the code: the refusal names the file, the line where the error has one, and the message, a batch is refused whole by place, and only the red line gains its code (read: `seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught/changelog.md:3-4`).

```seal
confirms: none
```
What holds: a compile that raises something other than `SyntaxError` fails closed. Design G9 says `SyntaxError` is "the one exception the refusal has to read". Under 3.15.0 and 3.12.9, a 200,000-term sum raises `RecursionError` and 200,000 unary minuses raise `MemoryError` from `compile` (executed, `## Probes` row 6). Neither is caught in `compile_error`, so each reaches `main`'s `except Exception` at `skills/verify/scripts/mutation_check.py:659-668`. The result is `could not run: ... No verdict.` at exit 2, before anything is written, and never a false red. An original of that shape also fails to import under the same interpreter, so this is no finding. G9's sentence is not whole, but the frame does not ship.

```seal
confirms: none
```
What holds: the phase-2 crafter's reading of the trailer rule as far as the check goes. `954bf5a5`, `e6b7f84a`, `ffa2fbe6`, `7229c745` and `18a02b6d` carry no `Seal-Routing:` trailer, and `b17253e5` and `95e7dea7` do (executed: `git log --format='%h %s | %(trailers:key=Seal-Routing,valueonly)' 40e6c23e..95e7dea7`). `docs/the-routing-check.md:120-126` says `chain-check` does not judge a commit with no such trailer, so the five do not fail it (read). `skills/commit-pr-convention/SKILL.md:185-187` still says a session's commit at a shared root ends with one, so the five did not keep the convention. Whether to rewrite them is a row of `## Not judged`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `95e7dea7`. The hand-back labels them `unverified` in `gaps.md` `## Not verified`, which is honest, and the phase-boundary counts (1442 and 11; 1580 and 1) were read, not re-run (contract rule 2). | `seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught/gaps.md` | the orchestrator's broad run, `seal gate --base release/v0.28.1 --record` this work item |
| Whether the new cases pass on CI's four `windows-latest` legs (`frame/questions.md` Q1). | `tests/skills/test_mutation_check.py` | the orchestrator, reading the pull request's CI run |
| Whether the five commits without a `Seal-Routing:` trailer are rewritten before the pull request, or left for the squash to replace. | `skills/commit-pr-convention/SKILL.md:185-187` | the orchestrator |
| The pull request body's statements that `CONTRIBUTING.md` *What a change to a gate must carry* and design G7 ask for: a failure direction, a prompt budget, the platforms not tested and what the change removes. No body exists at this round. | `CONTRIBUTING.md` | the sealer, reading `seal pr-body`'s file |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_mutation_check.py -q`, in the clone at `95e7dea7` | 65 passed, exit 0 |
| `bin/seal mutate skills/verify/scripts/mutation_check.py` with the six `--replace` pairs of finding 1's `evidence:` line and `--tests "bin/test tests/skills/test_mutation_check.py -q -p no:xdist -x"`, from the clone | baseline passed; mutant 1 (`numbered=True`) SURVIVED; mutant 2 (`verdict == RED`) SURVIVED; mutants 3 to 6 red, each at exit 1; exit 1; `git status` clean afterwards |
| `bin/seal layout --pairs`, from the clone | exit 0; no pair names `tests/skills/test_mutation_check.py` |
| `git grep -n -E` over five alternatives, `mutant <n>`, `mutant [0-9]+: red`, `seal mutate.*(compile` or `syntax)`, `Any UTF-8 text file` and `any UTF-8 text file`, excluding `seal/threads` and `tests` | hits only in `skills/verify/SKILL.md` and `skills/verify/scripts/mutation_check.py` |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.28.1 --root <branch worktree> --worktree`, the plugin's copy, before this record was written | exit 0; it named only the absent round record, gate record and guarantee file |
| `compile` over a 200,000-term sum, 200,000 unary minuses and 5,000 nested calls, under `python3` 3.15.0 and `python3.12` 3.12.9 | `RecursionError`, `MemoryError` and `SyntaxError` (too many nested parentheses) respectively, under both |
| A probe file `tests/skills/test_tmp_898_round1.py` holding finding 1's assertion and finding 2's survivor case, run as `bin/seal mutate skills/verify/scripts/mutation_check.py` with pairs 1 and 2 of finding 1's line and `--tests "bin/test tests/skills/test_tmp_898_round1.py -q -p no:xdist"`, then deleted | baseline passed; both mutants red at exit 1; exit 0; the probe file is gone and `git status` is clean |

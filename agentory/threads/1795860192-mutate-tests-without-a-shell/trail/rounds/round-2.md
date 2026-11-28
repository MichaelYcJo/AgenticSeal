# Review round 2: 1795860192-mutate-tests-without-a-shell

```iadd
target: d1a9a4dd, fixes e782ba51..48d3b4ba
```

A verifying round over round 1's fix pass. The code reviewed is the fix diff `e782ba51..48d3b4ba`, one commit, and the commit `d1a9a4dd` after it holds round 1's close blocks alone. The range holds no merge of the base. The work item's records named by `agents/proofer.md` step 3 were read whole at `d1a9a4dd`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/rounds/round-1.md`. `Commit and pull request language` is English, so no `pr.<lang>.md` is owed.

Carried from round 1, not re-established: the Grounding rows at `frame/design.md:9`, `:10`, `:12` and `:13` stand at `8e130543`, the fix diff left them unchanged, and no check of them failed. G2's dated `executed` claim about `shlex` in non-POSIX mode was not re-run, as round 1 did not re-run it, since the code does not use that reader. `.github/workflows/test.yml:81-84` as the Windows leg was carried as a coordinate. Re-derived this round: every verdict below, the Grounding row at `frame/design.md:11` that the fix changed, and the search over the other work items' frames, which printed none of this item's files.

Axes walked over the fix diff: inputs (`--tests` holding a newline at its start, its end and between words), exclusions and boundaries (a newline inside quotes, after a backslash, beside another operator), response shape (the refusal's stream, first line and exit code, walked from S1 and `skills/verify/agentic-mutate.md:65-75` to `skills/verify/scripts/mutation_check.py:735-748`), error paths and the four record rows. Error paths: the fix diff moves the refusal from `parser.error` on stderr to a `refused:` line on stdout with return 2, and adds the newline to what is refused. The second is a new failure path, and finding 1 classes one part of it as a regression. Concurrency and atomicity do not apply: the refusal still returns before `started` and before anything is written.

## Findings

### 1. A `--tests` that ends or opens with a newline is refused, though no program would get the newline as an argument

```iadd
severity: should
location: `skills/verify/scripts/mutation_check.py:258-294`, `tests/skills/test_mutation_check.py:1934-1960`, `skills/verify/agentic-mutate.md:26-28`, `agentory/threads/1795860192-mutate-tests-without-a-shell/frame/design.md:15`, `agentory/threads/1795860192-mutate-tests-without-a-shell/frame/design.md:23`, `agentory/threads/1795860192-mutate-tests-without-a-shell/changelog.md:3`
evidence: executed `round-2/test_tmp_round2.py` (see `## Probes`), and `git grep -n -F 'newline' -- skills/verify tests/skills/test_mutation_check.py agentory/threads/1795860192-mutate-tests-without-a-shell ':!*/trail/rounds/*'` at `d1a9a4dd`
regression: round-1#1
```

Why it matters: the unit is `OPERATOR_CHARACTERS` at `skills/verify/scripts/mutation_check.py:255`, which the fix pass widened with `\n`, read by `shell_operators` at `:258-294`. The frame's G1 at `frame/design.md:15` says the refusal reads a character a POSIX shell would read as an operator or a command's end, and G2 at `:17` rejects a reader because it "would refuse a command a shell would run as one". The fix counts every newline outside quotes, so a newline before the first word or after the last is refused too. The probe printed `shell_operators("true\n", windows=False)` as `['\n']` while `command_words("true\n")` is `['true']`, the same words as `true`. `main` with `--tests "true\n"` exited 2 and printed `refused: --tests holds `\n` outside quotes, ... so the first program would get it as an argument and the cases after it would never run.` Both halves of that line are false for this input: `shlex` reads the trailing newline as a blank, and no second command exists. `sh -c` reads the same line as one command (`sh -c "$(printf 'echo one\n')"` printed `one` and exited 0). Round 1's grounds named a heredoc or a YAML block as where a multi-line `--tests` comes from, and a YAML block scalar written with `|` keeps its final newline, so the commonest such line is the one now refused. The refusal fails closed, with exit 2, but a person is told something wrong and has to rewrite a correct command.

The fix set beside the frame: Scope item 1 asked for "the newline" in the refused set, round 1's snippet added it as one more member of the set, and the fix pass took it as written. The defect came from that snippet, which did not separate a newline between two words from one at either end. Round 1's own grounds said what the class is: the separators between two commands.

The search `git grep -n -F 'newline'` over the slice printed the statements of the rule: `changelog.md:3`, `frame/design.md:15`, `frame/design.md:23`, `skills/verify/agentic-mutate.md:27`, `mutation_check.py:254` and `tests/skills/test_mutation_check.py:1957`. The comment at `mutation_check.py:254` and the case comment at `:1957` say a newline ends a command as `;` does, which holds after the fix below. The search is a sample under contract rules 12 and 19, since a statement of the rule in other words escapes it. The snippet covers the code and the cases. The fix pass also owes the four prose statements: `agentic-mutate.md:26-28`, `design.md:15`, `design.md:23` and `changelog.md:3`, where "a newline" becomes "a newline between two words".

The precondition: `shlex` splits on its `whitespace` attribute, `" \t\r\n"`, and `command_words` keeps that default, so stripping those four characters from both ends removes only what `command_words` reads as a blank. None of them is a quote or a backslash, so the strip changes no quote state the scan reads.

```python
def shell_operators(text, windows=None):
    # The docstring as it stands, with this sentence added after "in order.":
    # A newline before the first word or after the last separates no two
    # commands, and `command_words` reads it as a blank, so it is none.
    if windows is None:
        windows = os.name == "nt"
    # `shlex`'s whitespace, which `command_words` splits on.
    text = text.strip(" \t\r\n")
    found, run, quote, i = [], "", None, 0
    # ... the scan as it stands
```

The cases added to the parametrize list at `tests/skills/test_mutation_check.py:1957-1959`, each red at `d1a9a4dd` by the probe's first line:

```python
            # A newline ends a command as `;` does, and one before the first
            # word or after the last separates no two commands.
            ("true\nfalse", False, ["\n"]),
            ("bin/test -q\n", False, []),
            ("\nbin/test -q", False, []),
            ("true\n\nfalse\n", False, ["\n\n"]),
            ('x "a\nb"', False, []),
```

The prose at `skills/verify/agentic-mutate.md:26-27`:

```markdown
operator, redirect or expansion. So a `--tests` holding `;`, `&`, `|`, `<`
or `>`, or a newline between two words, outside quotes, and on POSIX not
after a backslash, is
```

### 2. No case holds how the refusal names a newline, so its rendering on one line is unpinned

```iadd
severity: should
location: `skills/verify/scripts/mutation_check.py:737-739`, `tests/skills/test_mutation_check.py:1054-1073`
evidence: executed `bin/agentic mutate skills/verify/scripts/mutation_check.py` with five `--replace` pairs and `--tests 'bin/test tests/skills/test_mutation_check.py -q -k "shell_operators or refuses_a_tests" -p no:xdist'` (see `## Probes`), mutant 5
regression: round-1#1
```

Why it matters: the unit is the `named` expression at `skills/verify/scripts/mutation_check.py:737-739`, which the fix pass added. It writes a newline as the two characters `\n`, so the refusal stays one line. `skills/verify/agentic-mutate.md:65` says the first line printed is the verdict, and the paragraph the fix rewrote at `:28` says "the line names each operator". Without the `.replace`, the refusal for `true\nfalse` breaks inside its backticks, and its first line reads `refused: --tests holds `` with the operator and the `sh -c` form on the next line. This round removed the `.replace("\n", "\\n")` call, and the mutant `SURVIVED` the cases. The `Test_main` case at `:1054-1073` drives `&&` alone, and the `Test_module` cases call `shell_operators`, not `main`. Contract rule 14 asks that a changed message be pinned in the same commit, and this is the *Regression test* row's `should`: a behaviour the fix diff changed that no case then holds.

The fix set beside the frame: Scope item 1 says the message names each operator, round 1's snippet named a newline in words for this reason, and the fix pass chose `\n` instead without a case for it. The defect is the missing case, not the choice.

```python
    @pytest.mark.parametrize(
        ("tests", "named"),
        [("true && false", "`&&`"), ("true\nfalse", "`\\n`")],
    )
    def test_refuses_a_tests_command_a_shell_would_read_as_two(
        self, tmp_path, capsys, tests, named
    ):
        """S1 of #1677. (The docstring as it stands, then:) A newline is named
        as `\\n`, so the refusal stays the one line the verdict is."""
        target = tmp_path / "target.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        code = module().main([str(target), "--replace", "1", "2", "--tests", tests])
        assert code == 2
        out = capsys.readouterr().out
        # The verdict is the first line, as every run that measured nothing
        # prints it (`skills/verify/agentic-mutate.md`), and the refusal is
        # that one line.
        assert out.startswith("refused: ") and out.count("\n") == 1, out
        # The operator the shell would have read, and the form that runs it.
        assert named in out, out
        assert "sh -c '" in out, out
        assert target.read_text(encoding="utf-8") == "VALUE = 1\n"
```

### 3. The Scope, the Removes row and the routing say the diff changes one paragraph of `agentic-mutate.md`, and the fix also changed its verdict list

```iadd
severity: should
location: `agentory/threads/1795860192-mutate-tests-without-a-shell/frame/design.md:24`, `agentory/threads/1795860192-mutate-tests-without-a-shell/frame/design.md:51`, `agentory/threads/1795860192-mutate-tests-without-a-shell/routing.md:19`
evidence: executed `grep -n 'one paragraph' routing.md frame/design.md` in the work item's directory and `git show 48d3b4ba -- skills/verify/agentic-mutate.md` at `d1a9a4dd`
regression: round-1#2
```

Why it matters: the unit is the verdict list item at `skills/verify/agentic-mutate.md:69-73`, whose `refused` entry the fix pass extended with "or `--tests` holds a shell's operator". The frame's Scope item 2 at `frame/design.md:24` still lists the file's change as "one paragraph after the command's synopsis", the *Removes* row at `:51` says "the change adds a refusal and one paragraph", and `routing.md:19` grounds the routing on "one paragraph of `skills/verify/agentic-mutate.md`". The target's diff of that file changes the new paragraph and a clause of the verdict list. These are sentences saying what the work does, and the target contradicts them. A reader holding the diff to the Scope, the inspector among them, finds a change no *Scope* item names.

The fix set beside the frame: round 1 finding 2 asked for the verdict list's clause, the fix pass wrote it, and no sentence of the frame that lists the file's changes was updated with it. The search printed `routing.md:19`, `design.md:24` and `design.md:51`; it is a sample under contract rules 12 and 19.

```markdown
2. `skills/verify/agentic-mutate.md`: one paragraph after the command's synopsis, saying `--tests` is split into words and run with no shell, and what the refusal reads; and in the verdict list, the refusal named among the cases of `refused`.
```

```markdown
| nothing | | the change adds a refusal, one paragraph and a clause of the verdict list |
```

```markdown
- **Implementation, the session:** the diff is one reader in `skills/verify/scripts/mutation_check.py`, its cases, and one paragraph and a clause of the verdict list of `skills/verify/agentic-mutate.md`.
```

## Confirmations

```iadd
confirms: round-1#1
```
What holds: a newline between two words is refused, executed. The probe's `main` call with `--tests "true\nfalse"` exited 2 with the `refused:` line on stdout and the target holding `VALUE = 1`, where round 1 saw exit 1 and `SURVIVED`. The mutant that drops `\n` from `OPERATOR_CHARACTERS` read `red` (mutant 1), and the only case it can fail is `("true\nfalse", False, ["\n"])` at `tests/skills/test_mutation_check.py:1958`, read. The four prose statements round 1 listed now name the newline: `skills/verify/agentic-mutate.md:27`, `frame/design.md:15`, `frame/design.md:23` and `changelog.md:3`, read. Findings 1 and 2 above are new defects in units this fix made, and they leave the close standing for the input round 1 named.

```iadd
confirms: round-1#2
```
What holds: S1 at `frame/design.md:34` now holds, executed. `main` with `--tests "true && false"` returned 2, printed `refused: --tests holds `&&` outside quotes, ...` as stdout's first line, named `--tests "sh -c '<command>'"`, and wrote nothing to stderr. The case at `tests/skills/test_mutation_check.py:1054-1073` asserts `out.startswith("refused: ")`, and the mutant that drops `{REFUSED}: ` read `red` (mutant 2). The verdict list at `skills/verify/agentic-mutate.md:69-73` names the refusal under `refused`, and the sentence about `parser.error` is gone from `trail/phases/phase-1.md`, read. Finding 3 is a record this fix left stale, not this finding's defect.

```iadd
confirms: round-1#3
```
What holds: both quoting behaviours round 1 saw survive are now held, executed. The mutant that keeps the double quote open (`quote = quote`) read `red` (mutant 3), and the mutant that limits the POSIX backslash rule to outside quotes read `red` (mutant 4), against the cases at `tests/skills/test_mutation_check.py:1950-1956`. The fix pass's `fix-1/mutate.txt` shows the same case, `x "a\" ; b"`, failing for the backslash mutant, read. `trail/phases/phase-1.md:7` no longer claims the double quote's close was red, and says round 1 found it survived, read.

```iadd
confirms: round-1#4
```
What holds: `frame/plan.md:20` has four cells, and its Status cell reads `d86d5c6f`, read.

```iadd
confirms: round-1#5
```
What holds: `frame/design.md:11` cites the paragraph opening **The bound ends the run, not only the process it spawned**. `git show 8e130543:skills/verify/agentic-mutate.md` holds that opening at line 99, the commit the Grounding is dated to, and the target holds it at line 112, executed.

What matched: the module's cases pass at the target, executed: `bin/test tests/skills/test_mutation_check.py -q -p no:xdist` printed 90 passed and 1 skipped. `uvx ruff check` and `uvx ruff format --check` over `skills/verify/scripts/mutation_check.py` and `tests/skills/test_mutation_check.py` exited 0.

What matched: the records stating the present agree with the target outside findings 1 and 3, read. `frame/plan.md:28` says the line is now refused with exit 2. `gaps.md` keeps its two `## Not verified` rows and its *Not done* line, and the fix diff removed no row. `pr.md:3-4` still quotes `frame/plan.md:34` word for word. `frame/questions.md` holds no open row. A search over the other work items' frames, `grep -n -F 'agentic-mutate'` and `grep -n -F 'mutation_check'` on `agentory/threads/*/frame/design.md` outside this item, printed nothing, executed.

The new cases were read against their group. `('x "a" ; y', False, [";"])` is the one case that holds the double quote's close, `(r'x "a\" ; b"', False, [])` the one that holds a backslash inside double quotes, `("true\nfalse", False, ["\n"])` the one that holds the newline, and `('x "a\nb"', False, [])` the one that holds a newline inside quotes. Each holds a fact no earlier case of the list holds. The case comment at `tests/skills/test_mutation_check.py:1950-1952` now says what its two cases hold.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check; the suite is `unverified` here, as `gaps.md:7` labels it | `agentory/config.json` `Broad gate` | the orchestrator |
| The refusal on a Windows runner, where a backslash is no escape; this round drove the `windows=True` reading from macOS only | `gaps.md:8`, `.github/workflows/test.yml:81-84` | the pull request's CI |
| The plan's *Verified by* run over `tests/text` and `tests/behaviour`, which reach past the slice | `frame/plan.md:20` | the orchestrator's broad run |
| Whether `command_words` owes a case or an issue of its own for a backslash before a newline: the probe printed `command_words("a \\\nb")` as `['a', '\nb']`, where a shell joins the two lines into `a b`. It is outside the fix diff, and it makes no line two commands | `skills/verify/scripts/mutation_check.py:229-250` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `.venv/bin/python test_tmp_round2.py`, in the round's scratch directory `round-2/`, loading `skills/verify/scripts/mutation_check.py` from the worktree and calling `main` on a scratch target | `shell_operators` printed `['\n']` for `true\nfalse`, `true\n` and `\ntrue`, `['\n\n']` for `true -q\n\n`, `[';\n']` for `true;\nfalse`, and `[]` for `a \` and a newline then `b`; `command_words` printed `['true']` for `true\n` and `\ntrue`. `main` exited 2 with a one-line `refused:` stdout and empty stderr for `true && false`, `true\nfalse`, `true\n` and `true;\nfalse`, naming `` `&&` ``, `` `\n` ``, `` `\n` `` and `` `;\n` ``. The target held `VALUE = 1` after each |
| `sh -c "$(printf 'echo one\n')"` | printed `one`, exit 0 |
| `bin/agentic mutate skills/verify/scripts/mutation_check.py --replace 'OPERATOR_CHARACTERS = ";&\|<>\n"' 'OPERATOR_CHARACTERS = ";&\|<>"' --replace 'f"{REFUSED}: --tests holds' 'f"--tests holds' --replace "quote = None if char == '\"' else quote" "quote = quote" --replace 'elif char == "\\" and not windows:' 'elif char == "\\" and not windows and quote is None:' --replace '.replace("\n", "\\n")' '' --tests 'bin/test tests/skills/test_mutation_check.py -q -k "shell_operators or refuses_a_tests" -p no:xdist'` | exit 1: baseline passed; mutants 1 to 4 `red`, mutant 5 (the newline's rendering) `SURVIVED`. `git status --short` was empty after |
| `bin/test tests/skills/test_mutation_check.py -q -p no:xdist` | exit 0, 90 passed, 1 skipped |
| `uvx ruff check` and `uvx ruff format --check` on `skills/verify/scripts/mutation_check.py` and `tests/skills/test_mutation_check.py` | exit 0 each |

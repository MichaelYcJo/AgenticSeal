# Review round 1: 1795860192-mutate-tests-without-a-shell

```iadd
target: fe56d151 against release/v0.41.1
```

A finding round over the whole branch, `596c79a6..fe56d151`: the routing, frame and records commits, and the build `d86d5c6f`. No earlier round exists, so no fact is carried; every coordinate below was opened at `fe56d151`. The planning and the build were the session's own (`routing.md:7-8`), so this round is the first reader of the frame and of the code.

Axes walked: inputs (the `--tests` string and the `windows` argument), exclusions and boundaries (quotes, backslashes, operator runs, the end of the line), deliberate non-exclusions (*Out*: `$( )`, backticks, `$VAR`), response shape (the refusal's stream, exit code and words, from S1 to the code), error paths, security, and the four record rows. This change's own axes are the two platforms' readings of a backslash and the class of shell syntax that makes one line more than one command. Error paths: the diff adds one failure path, the refusal in `main` (`skills/verify/scripts/mutation_check.py:733-742`), which is the fix the issue asks for. Concurrency and atomicity do not apply: the refusal runs before anything is written or started. Security: `--tests` is the caller's own command, and the change only refuses more of it.

## Findings

### 1. A `--tests` holding a newline still runs as one program, and each mutant reads `SURVIVED`

```iadd
severity: should
location: `skills/verify/scripts/mutation_check.py:253-292`, `skills/verify/scripts/mutation_check.py:733-742`, `tests/skills/test_mutation_check.py:1932-1958`, `skills/verify/agentic-mutate.md:26-28`, `agentory/threads/1795860192-mutate-tests-without-a-shell/frame/design.md:15`, `agentory/threads/1795860192-mutate-tests-without-a-shell/frame/design.md:23`, `agentory/threads/1795860192-mutate-tests-without-a-shell/changelog.md:3`
evidence: executed `round-1/test_tmp_round1.py` (see `## Probes`), and `git grep -n -F '; & | < >'`, `git grep -n -F '`;`, `&`, `|`, `<`'`, `git grep -n -F 'OPERATOR_CHARACTERS'` at `fe56d151`
```

Why it matters: the work's title, in `changelog.md:3`, claims that `agentic mutate` refuses a `--tests` that a shell would read as more than one command. A POSIX shell also reads a newline as a command separator, like `;`. `OPERATOR_CHARACTERS` at `skills/verify/scripts/mutation_check.py:253` is `";&|<>"`, so `shell_operators` reads no operator in `"true\nfalse"`. `command_words` splits the line into `['true', 'false']`, so `true` runs with `false` as its argument. The probe ran `main` with `--tests "true\nfalse"`: it exited 1 and printed `SURVIVED: the cases passed against the mutation`. That is the defect of #1677 in another spelling, and the release ships it under a changelog line saying it is fixed. A multi-line `--tests` is plausible where a caller builds the line from a heredoc or a YAML block.

The class was listed from the POSIX shell grammar's separators, the method contract rule 12 asks for: `;`, `&`, `&&`, `||`, `|` and newline separate commands. The diff covers every member but newline. `(` and `)` are not in the class: a line holding them without one of those separators is a syntax error to a shell, so no person writes it as two commands. A newline inside quotes is literal, and a backslash before a newline is a line continuation, which the backslash rule already skips on POSIX.

The search `git grep -n -F '; & | < >'` printed `frame/design.md:15` and `frame/design.md:23`. `git grep -n -F '`;`, `&`, `|`, `<`'` printed `changelog.md:3` and `skills/verify/agentic-mutate.md:26`. `git grep -n -F 'OPERATOR_CHARACTERS'` printed `mutation_check.py:253`, `:258` and `:282`. These searches are a sample under contract rules 12 and 19: a statement of the set in other words escapes them. The snippet below covers the code and the cases. The fix pass also owes the four prose statements: `agentic-mutate.md:26-28` ("holding `;`, `&`, `|`, `<` or `>`, or a newline, outside quotes"), `design.md:15` and `design.md:23` (the set, plus a newline), and `changelog.md:3` (the same list).

```python
OPERATOR_CHARACTERS = ";&|<>"
NEWLINE = "a newline"


def shell_operators(text, windows=None):
    # ... docstring as it stands, with "and each newline, which a shell
    # reads as a separator, as `NEWLINE`" added after "in order."
    if windows is None:
        windows = os.name == "nt"
    found, run, quote, i = [], "", None, 0
    while i < len(text):
        char = text[i]
        if quote == "'":
            quote = None if char == "'" else quote
        elif char == "\\" and not windows:
            i += 1
        elif quote == '"':
            quote = None if char == '"' else quote
        elif char in "'\"":
            quote = char
        elif char in OPERATOR_CHARACTERS:
            run += char
            i += 1
            continue
        elif char == "\n":
            if run:
                found.append(run)
                run = ""
            found.append(NEWLINE)
        if run:
            found.append(run)
            run = ""
        i += 1
    if run:
        found.append(run)
    return found
```

In `main`, the message names a newline in words, since a newline inside backticks would break the line:

```python
        named = ", ".join(
            op if op == NEWLINE else f"`{op}`" for op in dict.fromkeys(operators)
        )
```

The cases added to the parametrize list at `tests/skills/test_mutation_check.py:1934-1951`:

```python
            # A newline separates commands, as `;` does; inside quotes it is
            # a character of the word.
            ("true\nfalse", False, ["a newline"]),
            ("x 'a\nb'", False, []),
```

```iadd
verdict: fixed 48d3b4ba
answer: `OPERATOR_CHARACTERS` now holds the newline, named in its comment as a command's end, and the refusal prints it as `\n`. Cases `("true\nfalse", False, ["\n"])` and a newline inside double quotes, which reads none, were added. The mutant that drops the newline from `OPERATOR_CHARACTERS` reads `red` (executed, `<scratchpad>/1795860192-mutate-tests-without-a-shell/fix-1/mutate.txt`, mutant 3). `skills/verify/agentic-mutate.md`, `frame/design.md` G1 and *Scope* item 1, and `changelog.md:3` name the newline beside the five characters.
```

### 2. The refusal prints no `refused`, against S1, and the verdict list does not name it

```iadd
severity: must
location: `skills/verify/scripts/mutation_check.py:733-742`, `tests/skills/test_mutation_check.py:1054-1071`, `skills/verify/agentic-mutate.md:69-75`, `agentory/threads/1795860192-mutate-tests-without-a-shell/frame/design.md:34`, `agentory/threads/1795860192-mutate-tests-without-a-shell/trail/phases/phase-1.md:7`
evidence: executed `round-1/test_tmp_round1.py` (see `## Probes`), and `git grep -n -F 'refused' -- skills/verify/agentic-mutate.md agentory/threads/1795860192-mutate-tests-without-a-shell` at `fe56d151`; read `skills/verify/agentic-mutate.md:65-75`, `skills/verify/scripts/mutation_check.py:139`
```

Why it matters: S1 at `frame/design.md:34` says that for `--tests "a && b"` the command exits 2 and "prints `refused` naming `&&` and the `sh -c` form". The code at `skills/verify/scripts/mutation_check.py:736` refuses through `parser.error`. The probe ran `main` with `--tests "true && false"`: stdout was empty, and stderr held the usage line, then `agentic mutate: error: --tests holds `&&` outside quotes, ...`. The word `refused` appears nowhere in the output. `skills/verify/agentic-mutate.md:65` says the first line printed is the verdict, and `:69-72` lists `refused` as a verdict with the cases where it is printed: `<old>` does not land once, or a `.py` mutant does not compile. A party reading this run's first line for its verdict finds the usage line, and a reader of the verdict list does not find this refusal in it. The new paragraph at `agentic-mutate.md:27` says the line "is refused with exit 2", which reads as that verdict.

`phase-1.md:7` records the choice of `parser.error` as matching the refusal of a `--tests` that names nothing (`mutation_check.py:732`). Claimed: a match with existing behaviour. Found: the design's acceptance row asks for the verdict word, and the phase record names no departure from S1. The case at `tests/skills/test_mutation_check.py:1054-1071` asserts `` `&&` `` and `sh -c '` on stderr and never `refused`, so it holds the code and not S1.

The fix below keeps S1 and the verdict list true. The other way, amending S1 to the usage error, would leave `agentic-mutate.md:65` ("The first line printed is the verdict") false for this exit 2. The search for `refused` printed `design.md:10`, `design.md:34`, `design.md:35`, `plan.md:28`, `gaps.md:12`, `changelog.md:3` and `agentic-mutate.md:27`, `:35`, `:51`, `:71`. Of these, `agentic-mutate.md:71` is the one the fix changes. The others hold after it. The sentence at `phase-1.md:7` becomes stale, and the fix pass owes it a correction.

```python
    operators = shell_operators(args.tests)
    if operators:
        named = ", ".join(f"`{op}`" for op in dict.fromkeys(operators))
        print(
            f"{REFUSED}: --tests holds {named} outside quotes, and --tests "
            "runs with no shell, so the first program would get it as an "
            "argument and the cases after it would never run. Pass one "
            "command, or give the shell the line on purpose: --tests "
            "\"sh -c '<command>'\". Nothing was written.",
            flush=True,
        )
        return 2
```

The case at `tests/skills/test_mutation_check.py:1054-1071`:

```python
        assert (
            module().main(
                [str(target), "--replace", "1", "2", "--tests", "true && false"]
            )
            == 2
        )
        out = capsys.readouterr().out
        # The verdict word first, then the operator and the form that runs it.
        assert out.startswith("refused: "), out
        assert "`&&`" in out, out
        assert "sh -c '" in out, out
        assert target.read_text(encoding="utf-8") == "VALUE = 1\n"
```

The verdict list at `skills/verify/agentic-mutate.md:71-72`:

```markdown
  start`, `could not run`, `refused` (nothing was written: `<old>` does not
  land once, a `.py` mutant does not compile, or `--tests` holds a shell
  operator outside quotes), `not restored`
```

```iadd
verdict: fixed 48d3b4ba
answer: The refusal no longer goes through `parser.error`. `main` prints `refused: …` as its first line on stdout and returns 2, as `Refused` does. The `Test_main` case now calls `main` and asserts the return code and that stdout opens with `refused: `. The mutant that drops `{REFUSED}: ` from the line reads `red` (executed, `fix-1/mutate.txt`, mutant 4). `skills/verify/agentic-mutate.md`'s verdict list names a shell's operator in `--tests` under `refused`. `frame/design.md` *Scope* item 1 says the refusal prints `refused` first, and `trail/phases/phase-1.md`'s sentence on `parser.error` was removed.
```

### 3. No case holds a double quote's close or a backslash inside double quotes, and the phase claims the close was seen red

```iadd
severity: should
location: `tests/skills/test_mutation_check.py:1932-1958`, `skills/verify/scripts/mutation_check.py:276-279`, `agentory/threads/1795860192-mutate-tests-without-a-shell/trail/phases/phase-1.md:6`
evidence: executed `bin/agentic mutate skills/verify/scripts/mutation_check.py` with three `--replace` pairs and `--tests 'bin/test tests/skills/test_mutation_check.py -q -k "shell_operators or refuses_a_tests" -p no:xdist'` (see `## Probes`)
```

Why it matters: `phase-1.md:6` claims that `agentic mutate` over five pairs, "either quote's close" among them, read `red` 5 of 5. This round replaced the double quote's close at `mutation_check.py:279`, `quote = None if char == '"' else quote`, with `quote = quote`, and the mutant `SURVIVED`. With that break, `bin/test -k "a" && b` reads no operator, which is the defect of #1677 again: a `-k` with a quoted expression followed by `&&` would run as before the fix. Every case in the list at `:1934-1951` that holds a double quote holds no operator after the quote closes, so none of them can see the close. The single quote's close (`:275`) was red against the same command, so the claim holds for one of the two closes.

The second pair limited the POSIX backslash rule at `mutation_check.py:276` to outside quotes, so that `\"` inside double quotes closed the quote. That mutant also `SURVIVED`. Scope item 1 says a backslash escapes outside single quotes, which includes inside double quotes, and no case holds that. The comment at `:1948-1949` says "A backslash inside double quotes escapes nothing that is an operator", and its one case, `x 'a\' ; y`, holds only the single-quote half.

Both are behaviours this diff adds that no case then holds, so this is the *Regression test* row's `should`, and the false claim at `phase-1.md:6` is a finding on its own terms. The fix pass owes the phase record a correction of that sentence.

```python
            # A double quote closes, and an operator after it is read.
            ('bin/test -k "a" && b', False, ["&&"]),
            # Inside double quotes a backslash escapes the quote on POSIX, so
            # the `;` stays quoted; on Windows the quote closes before it.
            (r'x "a\" ; b"', False, []),
            (r'x "a\" ; b"', True, [";"]),
```

```iadd
verdict: fixed 48d3b4ba
answer: Two cases were added: `('x "a" ; y', False, [";"])` holds the double quote's close, and `(r'x "a\" ; b"', False, [])` holds a backslash inside double quotes. The mutant that keeps the double quote open reads `red` (`fix-1/mutate.txt`, mutant 1). The mutant that limits the backslash rule to outside quotes, the one round 1 saw survive, reads `red` too (`fix-1/mutate-2.txt`). Both are executed. `trail/phases/phase-1.md` now says the single quote's close was seen red, and that round 1 found the double quote's pair survived the cases as they stood.
```

### 4. Phase 1's Status cell is empty: `||` moves `d86d5c6f` into a fifth cell

```iadd
severity: should
location: `agentory/threads/1795860192-mutate-tests-without-a-shell/frame/plan.md:20`
evidence: read `agentory/threads/1795860192-mutate-tests-without-a-shell/frame/plan.md:18-20`, `templates/records/sdd-plan.md:17-19`, `skills/implement/SKILL.md:355-356`, `skills/implement/SKILL.md:373-378`; executed `git show fe56d151 -- agentory/threads/1795860192-mutate-tests-without-a-shell/frame/plan.md`
```

Why it matters: the Phases table has four columns (`plan.md:18`). Commit `fe56d151` turned the row's ending ` | |` into ` || d86d5c6f |`. That row has five cells: the fourth, Status, is empty, and `d86d5c6f` stands in a fifth that the table has no header for, which a Markdown renderer drops. `skills/implement/SKILL.md:356` makes the Status cell the trace that the build happened, and `:373-378` reads an empty one as a phase not closed. A reader of the plan, the inspector among them, sees phase 1 open.

```markdown
| 1 | *Scope* items 1 to 4 | the new cases red against `8e130543` and green after; `uv run --no-project tests/run_tests.py -q tests/skills/test_mutation_check.py tests/text tests/behaviour`; `uvx ruff check` and `format --check` on both Python files | d86d5c6f |
```

```iadd
verdict: fixed 48d3b4ba
answer: `frame/plan.md` phase 1's row has four cells again, and its Status cell reads `d86d5c6f`.
```

### 5. The Grounding cites a paragraph of `agentic-mutate.md` by the opening of a docstring in `mutation_check.py`

```iadd
severity: should
location: `agentory/threads/1795860192-mutate-tests-without-a-shell/frame/design.md:11`
evidence: executed `git grep -n -F 'The bound ends what the run started'` at `fe56d151`, and `git show 8e130543:skills/verify/agentic-mutate.md | grep -n 'bound ends'`
```

Why it matters: the Grounding is dated to `8e130543` (`design.md:5`), and its row at `:11` sends a reader to "`skills/verify/agentic-mutate.md`, the paragraph opening **The bound ends what the run started**". The search printed one hit, `skills/verify/scripts/mutation_check.py:78`, a module docstring. At `8e130543` the paragraph of `agentic-mutate.md` on the bound is at line 99, and at `fe56d151` it is at line 111. It opens "**The bound ends the run, not only the process it spawned.**" An agent that opens the cited file and looks for the cited words finds nothing. The fact the row states, the process-group kill on POSIX, is true of both texts. The search is a sample under contract rules 12 and 19, and it found no other statement of the coordinate.

```markdown
| `skills/verify/agentic-mutate.md`, the paragraph opening **The bound ends the run, not only the process it spawned** | the timeout kills the command's process group on POSIX, which the verdict's bound rests on |
```

```iadd
verdict: fixed 48d3b4ba
answer: `frame/design.md` *Grounding* now cites the paragraph opening **The bound ends the run, not only the process it spawned**, the heading `skills/verify/agentic-mutate.md:111` holds.
```

## Confirmations

What matched: S1's exit code, operator and form, executed. The probe's `main` call with `--tests "true && false"` exited 2, named `` `&&` `` and `--tests "sh -c '<command>'"`, and left the target holding `VALUE = 1`. The refusal sits before `started` and before `mutation_run` or `batch_run` (`skills/verify/scripts/mutation_check.py:733-744`), so nothing is written or started, read. Finding 2 is about the word and the stream, not these.

What matched: S2 and S3, executed. The eleven parametrized cases at `tests/skills/test_mutation_check.py:1934-1951` and the `Test_main` case passed under `bin/test tests/skills/test_mutation_check.py -q -k "shell_operators or refuses_a_tests or names_no_command" -p no:xdist` (12 passed). Their lines were traced by hand against `shell_operators`: `\;` is no operator on POSIX and is one with `windows=True`, and an operator inside either quote is not read, read.

What matched: the `Test_main` case holds the guard it names, executed. `agentic mutate` with `if operators:` replaced by `if False:` read `red`, failing at `pytest.raises(SystemExit)` with `DID NOT RAISE`, the line for that guard. The phase's claim that the single quote's close was red holds too (finding 3, mutant 3). The phase's claim that the eleven `Test_module` cases were red before the build was read, not re-run: `shell_operators` does not exist at `aec6390b`, so each case fails on the attribute.

What matched: `shell_operators` reads a backslash as `command_words` does, read. On POSIX, `command_words` (`mutation_check.py:229-250`) uses `shlex` in POSIX mode, where a backslash escapes outside single quotes and escapes `"` inside double quotes. On Windows it sets `escape = ""`. `shell_operators` skips the character after a backslash on POSIX in both of those places, and reads no escape on Windows.

What matched: the Grounding rows at `frame/design.md:9`, `:10`, `:12` and `:13` stand at `8e130543` and at `fe56d151`, read. `command_words` and `main` split `--tests` and start it with no shell. `agentic-mutate.md:69-75` makes every run that measured nothing exit 2. `.github/workflows/test.yml:81-84` runs the suite on `windows-latest`.

What matched: the *Out* list at `frame/design.md:28`, read. A `$( )`, a backtick or a `$VAR` reaches the program as literal text, and `gaps.md:12` names it as not done. The issue's open choice, refusal or `sh -c`, is answered by G1 with grounds the tree holds. G2's claim about `shlex` in non-POSIX mode is a dated `executed` claim, and this round did not re-run it, since the code does not use that reader.

What matched: `pr.md:3-4` quotes `frame/plan.md:34` word for word, and `Commit and pull request language` is English, so no `pr.<lang>.md` is owed, read. `frame/plan.md` *Overlap with the release* (`:24`) names #1648 and #1676 with the date they were read. `agentory/threads/` at `fe56d151` holds three other work items, and none of their frames' `## Rule changes` names `skills/verify/agentic-mutate.md` or `mutation_check.py`. That was executed as `grep -n -F 'agentic-mutate' agentory/threads/*/frame/design.md`, which printed only this item's lines.

The new cases were read against their groups. The `Test_main` case sits beside the case for a `--tests` that names nothing and covers a different refusal. Among the parametrized cases, `pnpm a&&pnpm b` holds an operator against a word with no space, which `pnpm a && pnpm b` does not. The case `x "a | b" 'c & d'` holds nothing that the two earlier quote cases do not: a double quote that never closes reads the same (finding 3). That case states S2, so it is no gap of its own.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check; the suite is `unverified` here, as `gaps.md:7` labels it | `agentory/config.json` `Broad gate` | the orchestrator |
| The refusal on a Windows runner, where a backslash is no escape; this round drove the `windows=True` reading from macOS only | `gaps.md:8`, `.github/workflows/test.yml:81-84` | the pull request's CI |
| The plan's *Verified by* run `uv run --no-project tests/run_tests.py -q tests/skills/test_mutation_check.py tests/text tests/behaviour`, which this round did not re-run, since `tests/text` and `tests/behaviour` reach past the slice | `frame/plan.md:20` | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_mutation_check.py -q -k "shell_operators or refuses_a_tests or names_no_command" -p no:xdist` | exit 0, 12 passed |
| `.venv/bin/python round-1/test_tmp_round1.py`, in the round's scratch directory, loading `skills/verify/scripts/mutation_check.py` from the worktree and calling `main` on a scratch target | `shell_operators("true\nfalse", windows=False)` returned `[]`, and `command_words` returned `['true', 'false']`. `main` with `--tests "true && false"` exited 2 with stdout empty and stderr holding the usage line and `agentic mutate: error: --tests holds `&&` outside quotes, ...`. `main` with `--tests "true\nfalse"` exited 1 and printed `SURVIVED: the cases passed against the mutation, so nothing they run watches this unit`. The target held `VALUE = 1` after both |
| `bin/agentic mutate skills/verify/scripts/mutation_check.py --replace "quote = None if char == '\"' else quote" "quote = quote" --replace 'elif char == "\\" and not windows:' 'elif char == "\\" and not windows and quote is None:' --replace "quote = None if char == \"'\" else quote" "quote = quote" --tests 'bin/test tests/skills/test_mutation_check.py -q -k "shell_operators or refuses_a_tests" -p no:xdist'` | exit 1: baseline passed; mutant 1 (double quote's close) `SURVIVED`, mutant 2 (backslash only outside quotes) `SURVIVED`, mutant 3 (single quote's close) `red`. `git status --short` was empty after |
| `bin/agentic mutate skills/verify/scripts/mutation_check.py --replace "    if operators:" "    if False:" --tests 'bin/test tests/skills/test_mutation_check.py -q -k refuses_a_tests -p no:xdist'` | exit 0, `red`, failing at `with pytest.raises(SystemExit)` with `DID NOT RAISE SystemExit`. `git status --short` was empty after |

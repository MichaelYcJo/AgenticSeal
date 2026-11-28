# Review round 3: 1795860192-mutate-tests-without-a-shell

```iadd
target: 1a7f366a, fixes 059fc3bf..84191b5e
```

This is a verifying round over round 2's fix pass. The code reviewed is the fix diff `059fc3bf..84191b5e`, which is one commit. The commit after it, `1a7f366a`, holds round 2's close blocks and nothing else. The range holds no merge of the base. The work item's records named by `agents/proofer.md` step 3 were read whole at `1a7f366a`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/rounds/round-1.md` and `trail/rounds/round-2.md`. `Commit and pull request language` is English, so no `pr.<lang>.md` is owed.

Carried from rounds 1 and 2, not re-established: the Grounding rows at `frame/design.md:9` to `:13` stand at `8e130543`. The fix diff left them unchanged, and no check of them failed. G2's dated `executed` claim about `shlex` in non-POSIX mode was not re-run, since the code does not use that reader. `.github/workflows/test.yml:81-84` was carried as the Windows leg. Re-derived this round: every verdict below, the evidence lines of round 2's three findings, and the search over the other work items' frames. That search, `grep -n -F 'agentic-mutate'` and `grep -n -F 'mutation_check'` on `agentory/threads/*/frame/design.md` outside this item, printed nothing (executed).

The round walked these axes over the fix diff. Inputs: `--tests` with a newline, a space, a tab or a carriage return at either end, alone and beside each other. Exclusions and boundaries: a backslash before a final newline, an operator before a final newline, and a newline between two words. Response shape: the refusal's first line and its line count, from `skills/verify/agentic-mutate.md:67` to `skills/verify/scripts/mutation_check.py:738-751`. Also error paths and the four record rows. Error paths: the fix diff adds no failure path. It narrows the refusal, so a line with blank space at its ends now runs where round 2 saw it refused. Concurrency and atomicity do not apply, because the strip runs before anything is written or started.

## Findings

### 1. No case holds that a space, a tab or a carriage return at an end is left out, so a strip of the newline alone passes every case

```iadd
severity: should
location: `tests/skills/test_mutation_check.py:1964-1967`, `skills/verify/scripts/mutation_check.py:273-275`
evidence: executed `bin/agentic mutate skills/verify/scripts/mutation_check.py` with six `--replace` pairs and `--tests 'bin/test tests/skills/test_mutation_check.py -q -k "shell_operators or refuses_a_tests" -p no:xdist'` (see `## Probes`), mutant 1; executed `round-3/test_tmp_round3.py` (see `## Probes`); read `agentory/threads/1795860192-mutate-tests-without-a-shell/frame/design.md:23`, `skills/verify/agentic-mutate.md:28-30`
regression: round-2#1
```

Why it matters: the unit is the strip at `skills/verify/scripts/mutation_check.py:275`, `text = text.strip(" \t\r\n")`, and the two cases at `tests/skills/test_mutation_check.py:1966-1967`, all of which the fix pass added. The frame's *Scope* item 1 at `frame/design.md:23` says the reader leaves out "blank space at either end". `skills/verify/agentic-mutate.md:28-30` says "Blank space at either end of the line, a final newline among it, separates no two commands and is not read". This round replaced the strip with `text.strip("\n")`, and that mutant `SURVIVED` the cases. Under that mutant the line `true\n ` keeps its newline, because the strip stops at the final space, so the line is refused. The probe printed `command_words("true\n ")` as `['true']`, and at the target `main` with `--tests "true\n \n"` ran it as one command and exited 1. So the code does what the frame says. No case holds the space, the tab or the carriage return, though. The case `"\n true -q \r\n"` puts each of them inside the newlines, and a strip of the newline alone leaves the inside unread. This is the *Regression test* row's `should`: a behaviour the fix diff changed that no case then holds.

Here is the fix set beside the frame. *Scope* item 1 names blank space, and round 2's snippet stripped the four characters of `shlex`'s whitespace. The fix pass wrote that strip and wrote one case that holds the newline and not the other three. The defect is the case, and the code is correct.

The class was built from what makes the defect: each character of the strip's set, and each end. The case below holds every member. Its reading against each mutant, read and not run: with only the newline stripped, the leading space stops the strip, and both newlines stay. Without the space in the set, the strip stops at once. Without the tab, it stops at the tab before the first newline. Without the carriage return, the trailing strip stops at `\r` with the last newline in front of it. With `rstrip` or `lstrip`, one end keeps its newline. Each of these reads at least one operator, and so fails the case. With the case in place, `("true\n", False, [])` holds nothing the new case does not hold, so the snippet replaces both cases. Its comment keeps the YAML line as the reason.

```python
            # Blank space at either end separates nothing: `command_words`
            # drops each of its blanks there, a YAML block's final newline
            # among them, so a newline beside a space, a tab or a carriage
            # return at an end is no operator either.
            (" \t\ntrue -q\n\r ", False, []),
```

```iadd
verdict: fixed 61a61101
answer: The two cases became the round's one, `(" \t\ntrue -q\n\r ", False, [])`, which puts a space, a tab, a carriage return and a newline at each end. Six mutants of the strip each read `red`: stripping only the newline, dropping the space, the tab or the carriage return from its set, `rstrip`, and `lstrip`. That run was executed, at `<scratchpad>/1795860192-mutate-tests-without-a-shell/fix-3/mutate.txt`. `bin/test tests/skills/test_mutation_check.py -q -p no:xdist` passes at `61a61101`.
```

## Confirmations

```iadd
confirms: round-2#1
```
What holds: a newline at either end of `--tests` is no longer refused, and a newline between two words still is, executed. The probe printed `shell_operators` as `[]` for `true\n`, `\ntrue` and `true -q\n\n`, the three lines round 2's probe saw refused, and as `['\n']` for `true\nfalse`. `main` with `--tests "true\n"` ran the line as the command `true` and exited 1 with `SURVIVED`, where round 2 saw exit 2 and a false `refused:` line. `main` with `--tests "true\nfalse"` still exited 2 with a one-line `refused:` stdout. The target held `VALUE = 1` after each call. The mutant that drops the strip (`text = text`) read `red` (mutant 4), and so did `rstrip` (mutant 2) and `lstrip` (mutant 3). The four prose statements round 2 listed now say that the ends are not read, read: `frame/design.md:15` says "a newline between two words", `frame/design.md:23` says "with blank space at either end left out", `skills/verify/agentic-mutate.md:28-30` adds the sentence on blank space, and `changelog.md:3` says "blank space at either end of the line left out". They agree with each other and with `skills/verify/scripts/mutation_check.py:273-275`. Finding 1 above is a new gap in a case this fix added, and it leaves the close standing for the input round 2 named.

```iadd
confirms: round-2#2
```
What holds: the refusal is held to one line, executed. The `Test_main` case at `tests/skills/test_mutation_check.py:1054-1078` is parametrized over `true && false` and `true\nfalse`. It asserts that stdout opens with `refused: `, that it holds one newline (`:1074`), and that it names `` `&&` `` or `` `\n` ``. The mutant that drops `.replace("\n", "\\n")` read `red` (mutant 5), where round 2 saw it survive. The probe's `main` call with `--tests "true\nfalse"` printed `` refused: --tests holds `\n` outside quotes, ... `` as one line, with stderr empty.

```iadd
confirms: round-2#3
```
What holds: the records name both changes to `skills/verify/agentic-mutate.md`, read and executed. `grep -n 'one paragraph'` over `routing.md` and `frame/design.md` printed `frame/design.md:24` and `:51`. *Scope* item 2 at `:24` now names the verdict list's `refused` entry beside the paragraph. The *Removes* row at `:51` names "one paragraph and a clause of the verdict list". `routing.md:19` now names "the text of `skills/verify/agentic-mutate.md` that states the refusal". The verdict list's entry at `skills/verify/agentic-mutate.md:73-75` and the paragraph at `:23-35` are the file's two changes at the target.

What matched: the module's cases pass at the target, executed. `bin/test tests/skills/test_mutation_check.py -q -p no:xdist` printed 93 passed and 1 skipped. That is round 2's 90 plus the new `Test_main` parameter and the two new `Test_module` cases. `uvx ruff check` and `uvx ruff format --check` over `skills/verify/scripts/mutation_check.py` and `tests/skills/test_mutation_check.py` each exited 0.

What matched: the records that state the present agree with the target, read. `frame/plan.md:28` says the line is now refused with exit 2. `gaps.md` keeps its two `## Not verified` rows and its *Not done* line, and the fix diff did not touch it. `pr.md:3-4` still quotes `frame/plan.md:34` word for word. `frame/questions.md` holds no open row. `trail/phases/phase-1.md` states what phase 1 found at its build, and the fix diff makes none of it false.

The new cases were read against their group. The `true\nfalse` parameter of `Test_main` is the one case that drives the newline's rendering through `main`. The `Test_module` cases `true\n` and `"\n true -q \r\n"` are the subject of finding 1.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check. The suite is `unverified` here, as `gaps.md:7` labels it | `agentory/config.json` `Broad gate` | the orchestrator |
| The refusal on a Windows runner, where a backslash is no escape. This round drove the `windows=True` reading from macOS only | `gaps.md:8`, `.github/workflows/test.yml:81-84` | the pull request's CI |
| The plan's *Verified by* run over `tests/text` and `tests/behaviour`, which reach past the slice | `frame/plan.md:20` | the orchestrator's broad run |
| Carried from round 2, outside this fix diff: whether `command_words` owes a case or an issue of its own for a backslash before a newline. This round's probe printed `command_words("true \\\n")` as `['true', '\n']`, where a shell joins the lines and runs `true` alone. It makes no line two commands | `skills/verify/scripts/mutation_check.py:229-250` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `.venv/bin/python test_tmp_round3.py`, run from the round's scratch directory `round-3/`, which loads `skills/verify/scripts/mutation_check.py` from the worktree and calls `main` on a scratch target | `shell_operators` printed `[]` on both platforms for `true\n`, `\ntrue`, `true -q\n\n`, `\n true -q \r\n`, `true\n `, `true \n`, ` \ntrue`, `true\n\t`, `true\r\n`, `true \` then a newline, and `true\` then two newlines. It printed `['\n']` for `true\nfalse`, `[';\n']` for `true;\nfalse` and `[';']` for `true;\n`. `main` exited 2 with a one-line `refused:` stdout and empty stderr for `true && false`, `true\nfalse` and `true;\nfalse`, naming `` `&&` ``, `` `\n` `` and `` `;\n` ``. It exited 1 with `SURVIVED` for `true\n` and `true\n \n`, which ran as `true`. The target held `VALUE = 1` after each call |
| `bin/agentic mutate skills/verify/scripts/mutation_check.py --replace 'text = text.strip(" \t\r\n")' 'text = text.strip("\n")' --replace 'text = text.strip(" \t\r\n")' 'text = text.rstrip(" \t\r\n")' --replace 'text = text.strip(" \t\r\n")' 'text = text.lstrip(" \t\r\n")' --replace 'text = text.strip(" \t\r\n")' 'text = text' --replace '.replace("\n", "\\n")' '' --replace 'OPERATOR_CHARACTERS = ";&\|<>\n"' 'OPERATOR_CHARACTERS = ";&\|<>"' --tests 'bin/test tests/skills/test_mutation_check.py -q -k "shell_operators or refuses_a_tests" -p no:xdist'` | exit 1. The baseline passed. Mutant 1 (only the newline stripped) `SURVIVED`. Mutants 2 to 6 (`rstrip`, `lstrip`, no strip, the newline's rendering, the newline dropped from the set) read `red`. `git status --short` was empty after |
| `bin/test tests/skills/test_mutation_check.py -q -p no:xdist` | exit 0, 93 passed, 1 skipped |
| `uvx ruff check` and `uvx ruff format --check` on `skills/verify/scripts/mutation_check.py` and `tests/skills/test_mutation_check.py` | exit 0 each |

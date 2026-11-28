# Inspection: 1795860192-mutate-tests-without-a-shell

The base `release/v0.41.1` resolves through `release/v0.41.1@{upstream}` to `596c79a6`, the commit tagged `v0.41.0`, whose `.claude-plugin/plugin.json` reads `0.41.0` (executed). `trail/gate.md`'s last `iadd` block reads `run: 9451f62b against 596c79a6`. `9451f62b` is an ancestor of HEAD `5370f462`, and `git log --ignore-submodules=none --no-merges --name-only 9451f62b..HEAD ^596c79a6` lists one commit, `5370f462`, touching `agentory/threads/1795860192-mutate-tests-without-a-shell/trail/gate.md` alone (executed). `agentic pr-body agentory/threads/1795860192-mutate-tests-without-a-shell --body <scratchpad>/1795860192-mutate-tests-without-a-shell/pr-body.md --check` exited 0 (executed). `agentory/parity.json` is not in the tree, so no parity comparison is owed.

The re-runs were made in `<scratchpad>/1795860192-mutate-tests-without-a-shell/at-base/`, a clone at `5370f462`. Outputs are at `<scratchpad>/1795860192-mutate-tests-without-a-shell/at-base-main.txt`, `inspector-mutate.txt`, `inspector-module.txt` and `inspector-probe/`. The tree under audit was not changed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| `seen red`: the new `Test_main` case and the `shell_operators` cases fail against the code before the change, and the `Test_main` case printed `SURVIVED` for `true && false` | `trail/phases/phase-1.md:5` | in the clone, `git checkout 596c79a6 -- skills/verify/scripts/mutation_check.py skills/verify/agentic-mutate.md` with HEAD's tests, then `bin/test tests/skills/test_mutation_check.py -q -p no:xdist -k "refuses_a_tests or shell_operators"` | holds, executed. 18 failed. Both `Test_main` parameters fail at `assert code == 2` with `assert 1 == 2`, and their output reads `SURVIVED: the cases passed against the mutation`, which is the defect of #1677. The 16 `shell_operators` cases fail on `AttributeError: ... no attribute 'shell_operators'`. The phase record's "eleven" is the case count at its build, and five cases came later through the fix passes |
| The cases that assert something is not read or let through are each red with their one guard removed: the end strip (round 2 #1, round 3 #1), the POSIX backslash rule, the double quote's close (round 1 #3), the newline's rendering (round 2 #2), the refusal in `main`, and the newline in `OPERATOR_CHARACTERS` (round 1 #1) | `trail/rounds/round-2.md`, `round-3.md` and `round-4.md` close blocks and confirmations; `trail/phases/phase-1.md:6` | in the clone with HEAD's code restored, `bin/agentic mutate skills/verify/scripts/mutation_check.py` with seven `--replace` pairs (`text = text`, `text.strip("\n")`, `elif False:` for the backslash rule, `quote = quote` for the double quote, `.replace("\n", "\\n")` removed, `if False:` for `if operators:`, the newline dropped from `OPERATOR_CHARACTERS`) and `--tests 'bin/test tests/skills/test_mutation_check.py -q -k "shell_operators or refuses_a_tests" -p no:xdist'` | holds, executed. The baseline passed, and all seven mutants read `red`, exit 0. `git status --short` in the clone was empty after |
| The module's cases pass at the target: 92 passed, 1 skipped | `trail/rounds/round-4.md` *Confirmations*, third paragraph | `bin/test tests/skills/test_mutation_check.py -q -p no:xdist` in the clone at HEAD's code | holds, executed: `92 passed, 1 skipped` |
| `uvx ruff check` and `uvx ruff format --check` on both Python files exit 0 | `trail/rounds/round-3.md` and `round-4.md` *Probes* | both commands on `skills/verify/scripts/mutation_check.py` and `tests/skills/test_mutation_check.py` in the clone | holds, executed: exit 0 each |
| S1: `--tests "a && b"` exits 2, prints `refused` naming `&&` and the `sh -c` form, and writes nothing | `frame/design.md:34` | `bin/agentic mutate <scratch>/inspector-probe/t.py --replace 1 2 --tests 'true && false'` in the clone | holds, executed. Exit 2. Stdout is one line, opening `` refused: --tests holds `&&` outside quotes `` and naming `--tests "sh -c '<command>'"`. Stderr is empty, and the target still reads `VALUE = 1` |
| Round 4's fix: the row on round 3's fix pass now reads as round 4's paste-ready row, word for word | `trail/rounds/round-4.md` finding 1 `verdict: fixed 1c9f74a4` | a Python comparison of `frame/plan.md` line 35 at HEAD with the `markdown` block of `round-4.md` finding 1 | holds, executed: equal |
| Round 4's fix: "A new last row records that round 4's fix, located in that row alone, goes to the inspector" | `trail/rounds/round-4.md` finding 1 `answer:` | `git diff 0489f328..HEAD -- agentory/threads/1795860192-mutate-tests-without-a-shell/` and `git grep -n -F 'this row'` and `'located in'` over the work item's records | does not hold, executed. The new row at `frame/plan.md:36` reads "Round 4's one finding is located in this row alone". In that row's cell, "this row" is row 36, the row on round 4's fix pass. Round 4 finding 1's `location:` line names `frame/plan.md:35`, the row on round 3's fix pass, which `git show 0489f328:…/frame/plan.md` holds at line 35 and HEAD still holds there |
| `pr.md` quotes `frame/plan.md` *Judgments of the run* word for word | `pr.md:3-4` | a Python check that each quoted sentence stands in `frame/plan.md` line 34 at HEAD | holds, executed |
| `frame/plan.md:36` and `:35` are judged against `docs/running/the-run.md` *The run* | `frame/plan.md:35-36`, the last column | `grep -n` on `docs/running/the-run.md` at HEAD | holds, executed. `:8` says a fix pass is followed by no round where its reader is the inspector, and `:11` says a regression's fix pass is followed by one verifying round whatever the count |
| Each `## Removes` row and each removal the changelog names stands nowhere in the tree | `frame/design.md` *Removes*, `changelog.md` | read | holds, read: *Removes* is one row reading `nothing`, and the changelog names no removal, so nothing is owed |

The sample is the phase record's `seen red`, the guard of every case that asserts something is not read or let through, the module's run, the lint and format, S1 end to end, and both halves of round 4's fix. Not re-run: G2's dated `executed` claim on `shlex` in non-POSIX mode (`frame/design.md:17`), since no code reads that way, and the `windows=True` reading on a Windows host, which `gaps.md:8` gives to the pull request's CI (`unverified`, answered by the pull request's CI). The broad gate is `trail/gate.md`'s and was not run here.

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `frame/design.md` G1 chooses a refusal over `sh -c`, with grounds. *Scope* items 1 to 4 name `shell_operators`, the refusal in `main`, a paragraph and the `refused` clause of `skills/verify/agentic-mutate.md`, the cases, and the changelog. *Removes* names nothing | the issue's *Done when*: a refusal with exit 2 that writes nothing and names the operator and the `sh -c` form, the choice written with its grounds, the doc stating how `--tests` is read, and a case red against 0.41.0. The diff `git diff 596c79a6...HEAD -- skills tests` changes those three files and no others | none |
| the build | the diff adds `OPERATOR_CHARACTERS` and `shell_operators` (`skills/verify/scripts/mutation_check.py:253-297`), the refusal in `main` (`:738-751`), the paragraph and clause in `skills/verify/agentic-mutate.md:23-35` and `:73-75`, and one `Test_main` case and one `Test_module` list. `trail/phases/phase-1.md` records the build's red runs | the design's *Scope*, S1 to S3, and the claims re-run above | none |
| the last round | `trail/rounds/round-4.md` confirms round 3 #1 and opens one finding on `frame/plan.md:35`, closed `fixed 1c9f74a4`, with a new last row that gives the fix to the inspector | its finding's row 35, which now reads as its snippet | its close's new row: `frame/plan.md:36` says the finding is located in "this row alone", where `round-4.md` finding 1's `location:` names `frame/plan.md:35`. The tree contradicts the row. Read and not decided here: `docs/running/the-run.md:11` asks that every decision past the third round name "the counts weighed and this section", and row 36 names the section and no counts |
| the changelog | `changelog.md:3`: `;`, `&`, `|`, `<`, `>` or a newline outside quotes, on POSIX not after a backslash, with blank space at either end left out, are refused with exit 2 and a first line reading `refused`, naming each operator and `--tests "sh -c '<command>'"` | the build (`mutation_check.py:255`, `:273-275`, `:738-751`), `skills/verify/agentic-mutate.md:23-35`, and S1 as re-run | none |
| the orchestrator's part of the pull request body | `pr.md`: `Closes #1677` and two quotes of `frame/plan.md` *Judgments of the run* on the `fix:` prefix | the issue number, `frame/plan.md:34` word for word, and the build: the defect is a run that measured nothing reported as `SURVIVED`, against `skills/verify/agentic-mutate.md`'s rule that such a run exits 2 | none |
| the routing's grounds | `routing.md` *Why this way*, chosen by the orchestrator under the routing answer `agentic`: one reader in `mutation_check.py`, its cases, and the text of `agentic-mutate.md` that states the refusal | the diff, which changes exactly those three files in those places | none |

`routing.md`'s `Implementation` row reads `the session`, not `crafter`, so no phase record is owed by a declared party. Phase 1's Status cell `d86d5c6f` has its `trail/phases/phase-1.md` all the same.

```iadd
target: 5370f462 against 596c79a6
Verdict: withheld reason: the orchestrator's round 4 fix pass (1c9f74a4) added frame/plan.md:36, whose grounds say "Round 4's one finding is located in this row alone", but trail/rounds/round-4.md finding 1's location: line names frame/plan.md:35, the row on round 3's fix pass, so row 36 misstates where the finding it hands to the inspector stands
```

## Re-run at 67be69e2

Two commits follow `5370f462`. `fc68eeaa` adds `inspection.md` alone, and `67be69e2` rewrites the grounds of `frame/plan.md:36` alone. `git diff --stat 5370f462..HEAD` lists those two files and nothing outside the work item's records (executed). `trail/gate.md` still reads `run: 9451f62b against 596c79a6`, and `git log --ignore-submodules=none --no-merges --name-only 9451f62b..HEAD ^596c79a6` lists `trail/gate.md`, `inspection.md` and `frame/plan.md`, each under `agentory/threads/1795860192-mutate-tests-without-a-shell/` (executed). `agentic pr-body agentory/threads/1795860192-mutate-tests-without-a-shell --body <scratchpad>/1795860192-mutate-tests-without-a-shell/pr-body.md --check` exited 0 against the rewritten body file (executed). The only claim whose coordinate a commit since `5370f462` touched is the one at `frame/plan.md:36`. The claims in the first run's table stand on code, cases and records that no commit since has touched, so they were not re-run.

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| Round 4's finding "is located in the row on round 3's fix pass alone" | `frame/plan.md:36` | `grep -n 'location:'` on `trail/rounds/round-4.md`, and `sed -n 35p` on `frame/plan.md` | holds, executed. The `location:` line at `round-4.md:19` names `frame/plan.md:35`, and line 35 at HEAD opens "Whether a round follows round 3's fix pass" |
| "Round 4, the fourth round, opened one finding, after rounds of five, three and one findings" | `frame/plan.md:36` | `awk` counting the `### <n>.` headings under `## Findings` in each `trail/rounds/round-N.md` | holds, executed: 5, 3, 1 and 1 for rounds 1 to 4 |
| The row names the counts weighed and `docs/running/the-run.md` *The run*, as `docs/running/the-run.md:11` asks of every decision past the third round | `frame/plan.md:36`, its last two columns | read against `docs/running/the-run.md:8` and `:11` | holds, read. The row gives the counts, names *The run* in its last column, and gives the fix to the inspector, as `:8` allows where the row *No fix that no round reads* does |
| No other record states the row's old wording or a fact the rewrite changed | the work item's records | `git grep -n -F` on `this row`, `five, three`, `fourth round` and `row on round 3's fix pass` over `agentory/threads/1795860192-mutate-tests-without-a-shell/` | holds, executed, a sample under contract rules 12 and 19. Outside this file's first run, which stays as it was written, the hits are `frame/plan.md:35`, `:36` and `round-4.md:30`, the round's snippet of row 35 |

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | unchanged since the first run | the issue's *Done when* and the diff, as the first run read them | none |
| the build | unchanged since the first run: `git diff --stat 5370f462..HEAD` lists no file outside the records | the design's *Scope* and the claims the first run re-ran | none |
| the last round | `trail/rounds/round-4.md` finding 1, located at `frame/plan.md:35` and closed `fixed 1c9f74a4`, with the fix given to the inspector | row 35, which reads as its snippet, and row 36, which now names row 35 as the place of the finding | none |
| the changelog | unchanged since the first run | the build and `skills/verify/agentic-mutate.md:23-35` | none |
| the orchestrator's part of the pull request body | `pr.md` is unchanged: `Closes #1677` and two quotes of `frame/plan.md:34` | `frame/plan.md:34` word for word, and the body check's exit 0 | none |
| the routing's grounds | unchanged since the first run | the diff | none |

```iadd
target: 67be69e2 against 596c79a6
Verdict: cleared
```

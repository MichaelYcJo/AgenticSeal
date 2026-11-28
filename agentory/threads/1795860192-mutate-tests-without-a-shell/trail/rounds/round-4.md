# Review round 4: 1795860192-mutate-tests-without-a-shell

```iadd
target: 0489f328, fixes 2efb5739..61a61101
```

This is a verifying round over round 3's fix pass. The code reviewed is the fix diff `2efb5739..61a61101`, which is one commit. It changes one line of `tests/skills/test_mutation_check.py`: two cases of the `shell_operators` list become one. The commit after it, `0489f328`, holds round 3's close block and a new last row of `frame/plan.md` *Judgments of the run*, and nothing else. The range holds no merge of the base. The work item's records named by `agents/proofer.md` step 3 were read whole at `0489f328`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/rounds/round-1.md` to `round-3.md`. `Commit and pull request language` is English, so no `pr.<lang>.md` is owed.

Carried from rounds 1 to 3, not re-established: the Grounding rows at `frame/design.md:9` to `:13` stand at `8e130543`. The fix diff left them and the code unchanged, and no check of them failed. G2's dated `executed` claim about `shlex` in non-POSIX mode was not re-run, since the code does not use that reader. `.github/workflows/test.yml:81-84` was carried as the Windows leg. The reading of the strip at `skills/verify/scripts/mutation_check.py:273-275` against *Scope* item 1 was carried from round 3, since no commit of the range touches that file (`git diff --stat 2efb5739..HEAD -- skills docs` printed nothing, executed). Re-derived this round: every verdict below, round 3's `evidence: executed` mutation run, and the search over the other work items' frames. That search, `grep -n -F 'agentic-mutate'` and `grep -n -F 'mutation_check'` on `agentory/threads/*/frame/design.md` outside this item, printed nothing (executed).

The round walked these axes over the fix diff. Inputs: the new case's line, with a space, a tab, a carriage return and a newline at each end. Exclusions and boundaries: each character of the strip's set and each end, one mutant at a time. Test quality: the new case against the cases of its parametrize list, and whether each red reads this case's line. The fix diff adds no failure path and changes no code, so error paths, concurrency, atomicity and security do not apply to it. The records were walked on the rows *Record against the code* and *Record against record*, and that walk gives finding 1.

## Findings

### 1. The new *Judgments of the run* row reads a `regression:` line as a sign the run converges, and cites no `docs/running/the-run.md` *The run*

```iadd
severity: should
location: `agentory/threads/1795860192-mutate-tests-without-a-shell/frame/plan.md:35`
evidence: read `skills/code-review/orchestration.md:174`, `docs/running/the-run.md:11`, `agentory/threads/1795860192-mutate-tests-without-a-shell/trail/rounds/round-3.md:21`; executed `git grep -n -F 'so the run converges'` and `git grep -n -F 'a regression of the fix before it'` at `0489f328`
```

Why it matters: the row at `frame/plan.md:35` grounds round 4 on "The findings fell from five to three to one, each round's a regression of the fix before it, so the run converges." The document the row names, `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*, lists at `:174` the signals that a run is not converging, and one of them reads "a finding carries a `regression:` line". So the row cites a non-convergence signal as evidence that the run converges, against the document it says it was judged against. The fall from five to three to one is the one convergence fact the row states. Then `docs/running/the-run.md:11` says two things the row leaves out. First, "A regression's fix pass is followed by one verifying round whatever the count", and round 3's one finding carries `regression: round-2#1` (`trail/rounds/round-3.md:21`). That rule is the ground on which round 4 is owed, and the row does not state it. Second, every such decision, at or past the third finding round, is a row "naming the counts weighed and this section". Round 3 is the run's third finding round. The row names the counts and does not name *The run*.

The decision itself holds: round 4 is owed. The defect is in the grounds, and the row is the record the settle reads: `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* has the settle read judgment rows against what they cost and caught. A row that reads a `regression:` line as convergence teaches that reading the wrong way round. That makes it a wrong sentence an agent reads and acts on.

The two searches each printed `frame/plan.md:35` alone, and `pr.md` quotes only the row at `:34`, so no other record states these grounds. The searches are a sample under contract rules 12 and 19, since a statement in other words escapes them. The row was written by the orchestrator in a commit that holds only the work item's records, so no `regression:` line stands here.

```markdown
| 2026-11-28 | Whether a round follows round 3's fix pass: yes, round 4, a verifying round on that fix. | Round 3's one finding carries `regression: round-2#1`, and a regression's fix pass is followed by one verifying round whatever the count. Round 3 is the third finding round, and the counts weighed are five, three and one findings: the count falls, while each finding of rounds 2 and 3 is a regression, a signal that the run is not converging. The fix pass changes one test case and no code, so the round it is owed is bounded to that case. That fix is outside the records, and the row *No fix that no round reads* of `skills/core/SKILL.md` *Judgment is not licence to skip a party* gives it to a round. | `docs/running/the-run.md` *The run*, `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* |
```

```iadd
verdict: fixed 1c9f74a4
answer: `frame/plan.md` *Judgments of the run*'s row on round 4 now reads as the round's paste-ready row, word for word. It names the rule that owed round 4, a regression's fix pass followed by one verifying round whatever the count, and it reads the regressions as the signal they are. A new last row records that round 4's fix, located in that row alone, goes to the inspector.
```

## Confirmations

```iadd
confirms: round-3#1
```
What holds: one case now holds every character of the strip at both ends, executed. The fix replaced `("true\n", False, [])` and `("\n true -q \r\n", False, [])` with `(" \t\ntrue -q\n\r ", False, [])` at `tests/skills/test_mutation_check.py:1966`, which is the snippet round 3 gave. Round 3's evidence line was re-run as six mutants of the strip at `skills/verify/scripts/mutation_check.py:275`: the newline alone stripped, the space, the tab or the carriage return dropped from the set, `rstrip`, and `lstrip`. The baseline passed and all six read `red`, against the same `--tests` round 3 named. At round 3's target the first of these `SURVIVED`. The probe `test_tmp_round4.py` then applied each mutant and ran all 16 cases of the list. Under each mutant the new case is the one case that fails, and none fails without a mutant, so each red is read on this case's line and on no other guard. The close's claim that the six mutants read `red` at `fix-3/mutate.txt` was read there too, and it matches. The case comment kept at `:1964-1965` says that `command_words` drops blank space at either end and that a YAML block leaves a final newline. That is true of the new line, so the fix keeps it in place of the snippet's longer comment, and no assertion depends on it.

What matched: the new case against its group, read and executed. The removed `("true\n", False, [])` held a final newline, which the new case holds at its end with three more characters. The removed `("\n true -q \r\n", False, [])` held each of the four characters, but only inside the newlines. Each of the six mutants of the strip fails the new case (the probe's rows), so for those six the removal loses nothing. The six are a sample of the strip's mutants, built from its set and its two ends as round 3 built them. Of the cases left, `("true\nfalse", False, ["\n"])` holds a newline between two words and `('x "a\nb"', False, [])` holds a newline inside quotes. The new case is the only one that holds the strip.

What matched: the module's cases pass at the target, executed. `bin/test tests/skills/test_mutation_check.py -q -p no:xdist` printed 92 passed and 1 skipped, which is round 3's 93 less the one case the fix took away. `uvx ruff check` and `uvx ruff format --check` on `tests/skills/test_mutation_check.py` each exited 0.

What matched: the records that state the present agree with the target outside finding 1, read. `frame/design.md:15` and `:23`, `skills/verify/agentic-mutate.md:23-35` and `changelog.md:3` say that blank space at either end is not read and that a newline between two words is. The code at `skills/verify/scripts/mutation_check.py:273-275` does that, and the new case holds it. `frame/plan.md:28` says the line is now refused with exit 2. `gaps.md` keeps its two `## Not verified` rows and its *Not done* line, and the range did not touch it. `pr.md:3-4` still quotes `frame/plan.md:34` word for word. `frame/questions.md` holds no open row. `trail/phases/phase-1.md` states what phase 1 found at its build, and the range makes none of it false.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check. The suite is `unverified` here, as `gaps.md:7` labels it | `agentory/config.json` `Broad gate` | the orchestrator |
| The refusal on a Windows runner, where a backslash is no escape. This round drove no `windows=True` reading, since the fix diff changes no Windows case | `gaps.md:8`, `.github/workflows/test.yml:81-84` | the pull request's CI |
| The plan's *Verified by* run over `tests/text` and `tests/behaviour`, which reach past the slice | `frame/plan.md:20` | the orchestrator's broad run |
| Carried from rounds 2 and 3, outside this fix diff and not re-run: whether `command_words` owes a case or an issue of its own for a backslash before a newline. It makes no line two commands | `skills/verify/scripts/mutation_check.py:229-250` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/agentic mutate skills/verify/scripts/mutation_check.py` with six `--replace` pairs on `text = text.strip(" \t\r\n")`, to `text.strip("\n")`, `text.strip("\t\r\n")`, `text.strip(" \r\n")`, `text.strip(" \t\n")`, `text.rstrip(" \t\r\n")` and `text.lstrip(" \t\r\n")`, with `--tests 'bin/test tests/skills/test_mutation_check.py -q -k "shell_operators or refuses_a_tests" -p no:xdist'` | exit 0. The baseline passed, and mutants 1 to 6 read `red`. Output at `round-4/mutate.txt`. `git status --short` was empty after |
| `python3 -I test_tmp_round4.py <the worktree>`, run from the round's scratch directory `round-4/`. It reads the case list of `test_shell_operators_reads_what_a_shell_would_read_outside_quotes` with `ast` and runs it against `shell_operators` under the unchanged strip and under each of the six mutants | 16 cases. The unchanged strip failed none. Each mutant failed only `(" \t\ntrue -q\n\r ", False, [])`: the newline alone and the space dropped read `['\n', '\n']`, and the other four read `['\n']` |
| `bin/test tests/skills/test_mutation_check.py -q -p no:xdist` | exit 0, 92 passed, 1 skipped |
| `uvx ruff check` and `uvx ruff format --check` on `tests/skills/test_mutation_check.py` | exit 0 each |

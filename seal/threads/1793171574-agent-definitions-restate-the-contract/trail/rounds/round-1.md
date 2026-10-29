# Review round 1: 1793171574-agent-definitions-restate-the-contract

target: 7b43db02 against 6e322bb7

## Findings

This round found no defect. Stage 1 read the diff `6e322bb7..7b43db02` of `agents/crafter.md`, `agents/proofer.md`, `agents/sealer.md`, `agents/framer.md`, `agents/tracer.md`, the three test modules and `.test_durations`. It read them against #1040's body and its *Done when*, and against `frame/design.md` *Scope*, *User scenarios & acceptance* and `## Removes`. Each clause is built. Stage 2 walked the axes below and found nothing to fix. Each check is an entry under `## Confirmations`, labelled executed or read.

The axes walked are these. For each removed sentence, the round checked where the contract states it and whether every agent still receives that rule. It read each shortened paragraph the way its agent reads it, against `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*. It looked for an antecedent a removed sentence left dangling, and for the class of restatements of rules 2, 6, 7 and 9 still in `agents/*.md`. It searched the whole tree for readers of a removed sentence, not only `tests/` and `evals/`, and for line citations into the five files, which the removal shifts. It checked whether each re-pointed assertion can fail and whether its group already pins the same words. It read the `check:` lines under the shortened paragraphs, the changelog fragment against the diff, and `gaps.md` against the tree. The change touches no code path. It changes text that agents read and the assertions that read it. The axes of concurrency, security, error paths and ordering therefore have nothing to act on.

`frame/questions.md` P1 is built on its default (a), and the four glosses it names stand. The owner has not answered P1, and this round raises nothing on it.

## Confirmations

confirms: none
S1 holds. The crafter claimed 15 occurrences at the base and none at the phase's commit. Executed in a `git clone --no-local` of the branch: each of the five definitions was read through `git show <rev>:agents/<name>.md`, with runs of whitespace collapsed as `tests/conftest.py#flat` collapses them, and searched for the ten phrases S1 lists. At `6e322bb7` the search found 15 occurrences, each phrase in the file its sentence stands in: `post, push` in four files and `repository-wide lint` in three. At `7b43db02` it found 0.

confirms: none
Each of `## Removes` rows 1 to 12 is gone, and the home each row names says what the sentence said (read). Contract rule 2 says "no agent runs any of the three" (`skills/agent-contract/SKILL.md:41`). Rule 6 withholds the four acts (`:85-87`). Rule 7 opens "Probe only what reading cannot settle" (`:93`). Rule 9 names "a `sed -i`, a redirection or a script" (`:120`). Each row's other landing holds too. Row 4's `unverified` label is in the crafter's step 10 (`agents/crafter.md:51-53`). Row 8's "you read it" is the sealer's step 1, which ends "Nothing broad is run in its place." (`agents/sealer.md:65`). Row 9's owner of the run is the sealer's *Job*, "`trail/gate.md` is the orchestrator's run's" (`agents/sealer.md:31`). The tracer's rule *Constraints, enums and defaults are read, not probed.* keeps its rule 7 citation (`agents/tracer.md:62-64`).

confirms: none
Each narrowing of `frame/design.md` *Scope* item 2 stays and cites its rule (read). The crafter's paragraph (`agents/crafter.md:134-139`) keeps `failing on base too` and `new?` and cites `rule 2`. The proofer's paragraph (`agents/proofer.md:136-142`) keeps the label audit, the `## Not judged` row and what comes due. The sealer's paragraph (`agents/sealer.md:123-124`) has a new lead that names the pointer to step 1, and it cites `rule 2` in lower case. "Fix the code under review." is a bullet of its own (`agents/proofer.md:59`). "Name any party as the runner of the broad gate." stays (`agents/crafter.md:65`). The three cases S2 names in `tests/text/test_broad_gate_rule.py` and the three in `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` passed (executed, the module runs under `## Probes`).

confirms: none
Each shortened paragraph has one reading for the agent that follows it (read). In the crafter's paragraph, "The run is rule 2's, and the label is step 10's." points the run at contract rule 2 without naming a runner, which the crafter's *Never* forbids (`agents/crafter.md:65`). The bold lead says the label is the crafter's, and step 10 is the crafter's own step, which states the suite labelled `unverified` with the orchestrator as its answerer. The two sentences therefore name one owner. In the proofer's paragraph, "one of the three" lost its antecedent with the removed sentence. Its replacement, "a check rule 2 excludes", is the phrase contract rule 3 uses (`skills/agent-contract/SKILL.md:52`), so the proofer reads the same set of checks in both files. In the sealer's paragraph, "the run rule 2 names" is the `seal gate` run of contract rule 2, which "spawns the sealer, which reads the record that run wrote". No new sentence uses a symbol as syntax or states a value a second time.

confirms: none
No reader of a removed sentence remains in the tree. Executed: `git grep -F` at `HEAD` outside this work item's directory, on the words of each removed sentence and of the removed case's name. The only matches are three. One is `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/design.md:206-215`, another work item's frame that records the tree of its own time. Another is `templates/setup/config.md:216` and `tests/text/test_the_rules_have_one_owner.py:212`, which use "the orchestrator runs it" of other subjects. The last is unrelated uses of "one of the three". Executed: `git grep -E` for a line citation into any of the five definitions found only a fixture string at `tests/github/test_rules.py:474`. So no citation points at a line the removal shifted.

confirms: none
The class #1040 measured is closed in `agents/*.md`, and what stays is narrowing or citation. Executed: `git grep` of `agents/` for `spawn`, `push`, `pull request`, `full suite`, `typecheck`, `lint`, `heredoc`, `sed -i` and every `rule <N>`. What stays falls into three groups. First are the four glosses P1's default (a) keeps (`agents/tracer.md:62-64`, `agents/proofer.md:156-160`, `agents/crafter.md:51-56` and the sealer's step 6). Second is the sealer's "Under rule 6, `guarantee.md` is the whole of what you may write" (`agents/sealer.md:30`), which is the write naming that rule 6 asks each definition for. Third are the citations of rules 4 and 10 in `agents/framer.md:83` and `:170`, which point at a rule without restating it.

confirms: none
Each re-pointed assertion can fail. The crafter claimed S3 red through `seal mutate`. Executed in the clone, with two mutants made through the `Edit` tool in different files. `failing on base too` became `failing on base` in `agents/crafter.md:136`, and `is the orchestrator's run's` became `is the orchestrator's` in `agents/sealer.md:31`. Run against the two re-pointed cases alone, both failed. `test_the_crafter_names_no_runner_of_the_broad_gate` read the crafter's mutant, and `test_the_window_the_sealer_shipped_under_is_closed` read the sealer's. The clone was then deleted.

confirms: none
No re-pointed assertion copies a pin its group already holds. Executed: `git grep` over `tests/` and `evals/` for `failing on base too`, `` `new?` `` and `orchestrator's run's`. The crafter's `` `new?` `` sentence is also pinned whole-file by the `readers` map (`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:420-430`). The re-pointed assertion reads it inside the broad gate paragraph, together with `failing on base too`, and no other case pins either of those two things. The sealer's "is the orchestrator's run's" has no other pin. The diff adds no case, so the group rule has nothing more to read. The removed case's `CRAFTER` constant stays because `test_no_carrier_claims_a_fact_about_the_reader_repository` reads it (`tests/text/test_edits_go_through_the_edit_tool.py:81`, read).

confirms: none
The `check:` lines stay as `frame/design.md` *Scope* item 4 says, and each one names a reader of what its paragraph keeps (read). The diff changes no `check:` line. Under the sealer's paragraph, `tests/behaviour/test_the_sealer_guarantees.py#test_step_1_reads_the_record_and_runs_nothing` pins step 1, the target of the pointer, and the two evals that #1040's *Done when* names stay on the line. The sealer's lead sentence itself is pinned by nothing. `gaps.md` *Not verified* says so, and `## Not judged` carries it.

confirms: none
The rewritten docstrings say what the code now holds (read). `test_the_crafter_names_no_runner_of_the_broad_gate`'s docstring names the citation and the two words it asserts. The module docstring of `tests/text/test_edits_go_through_the_edit_tool.py` names the proofer's half of rule 9 alone, and the proofer's half is `agents/proofer.md:156-160`. `test_step_1_reads_the_record_and_runs_nothing` lost only the *Never* assertion, and its docstring still claims only what its remaining assertions read.

confirms: none
The crafter's account of the narrow runs holds. Executed in the clone with the worktree's existing virtualenv interpreter, one module per command, each with exit 0: `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` (23 passed), `tests/text/test_broad_gate_rule.py` (17), `tests/behaviour/test_the_sealer_guarantees.py` (15), `tests/text/test_edits_go_through_the_edit_tool.py` (5) and `tests/text/test_a_moved_rule_leaves_its_definition.py` (221). These are the counts the phase record gives. `uvx ruff check` and `uvx ruff format --check` over the three changed test files exited 0.

confirms: none
`changelog.md` and `gaps.md` match the diff (read). The fragment names the five definitions and the four rules, and it states the three narrowings that stay as the paragraphs now hold them. `gaps.md`'s one divergence, the `.test_durations` key, removes the key of the case the diff removes. `git grep` for the case name finds nothing else (executed). `gaps.md` *Not verified* labels the full suite, the lint and the typecheck `unverified` and names the orchestrator through `seal gate`, and that label is honest: the crafter's phase record reports module runs only.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The three units no case reads: the proofer's `a check rule 2 excludes`, the sealer's lead `A missing or stale gate record earns what step 1 says.`, and the crafter's `the label is step 10's`. `frame/design.md` *Out of scope* gives the phrase-pin decision to #1111, so this round raises no finding on them | `agents/proofer.md:138-139`, `agents/sealer.md:123`, `agents/crafter.md:134-135` | the repository owner, through #1111 |
| The crafter's other `seal mutate` runs. This round re-made two of the S3 mutants and re-ran none of the other mutants the phase record reports, the three survivors among them | `trail/phases/phase-1.md` *What this phase found* | the sealer, which re-runs a sample of the crafter's claims |
| The sealer's conduct with no gate record and with a stale one. This round read the evals' directories and did not run them | `evals/behaviour/sealer/rule-sealer-no-gate/`, `evals/behaviour/sealer/rule-sealer-stale-gate/` | the repository owner, through an eval run |
| The full suite, the repository-wide lint and the typecheck at `7b43db02`. This round ran none of them, under contract rule 2 | `gaps.md` *Not verified* | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the branch worktree into the round's scratch directory, then `git checkout --detach 7b43db02` in the clone | the clone at `7b43db02` |
| `python3 -I -c` reading each `agents/<name>.md` through `git show 6e322bb7:` and `git show 7b43db02:`, whitespace collapsed, counting the ten S1 phrases | 15 at `6e322bb7`, 0 at `7b43db02` |
| `python -m pytest -q -p no:cacheprovider tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, in the clone | exit 0, 23 passed |
| the same over `tests/text/test_broad_gate_rule.py` | exit 0, 17 passed |
| the same over `tests/behaviour/test_the_sealer_guarantees.py` | exit 0, 15 passed |
| the same over `tests/text/test_edits_go_through_the_edit_tool.py` | exit 0, 5 passed |
| the same over `tests/text/test_a_moved_rule_leaves_its_definition.py` | exit 0, 221 passed |
| with `failing on base too` mutated to `failing on base` in `agents/crafter.md` and `is the orchestrator's run's` to `is the orchestrator's` in `agents/sealer.md`, `python -m pytest -q -p no:cacheprovider tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -k "test_the_crafter_names_no_runner_of_the_broad_gate or test_the_window_the_sealer_shipped_under_is_closed"` | exit 1, 2 failed |
| `uvx ruff check` and `uvx ruff format --check` over the three changed test files | exit 0 each |
| `git grep -F` at `HEAD` for the words of each removed sentence, outside this work item's directory, the changelogs excluded | matches only in another work item's frame and in unrelated sentences |
| `git grep -E "agents/(crafter\|sealer\|proofer\|tracer\|framer)\.md:[0-9]"` outside `seal/threads/` and the changelogs | one fixture string, `tests/github/test_rules.py:474` |
| `git grep` of `agents/` for `spawn`, `push`, `pull request`, `full suite`, `typecheck`, `lint`, `heredoc`, `sed -i` and `rule <N>` | no restatement of rules 2, 6, 7 or 9 beyond the four glosses P1 keeps |
| `git grep` over `tests/` and `evals/` for `failing on base too`, `` `new?` `` and `orchestrator's run's` | the `readers` map and the re-pointed assertions; the sealer's phrase pinned once |

# Design: each run reaches the tree-wide guards (#1441)

## Grounding

The tree as read at `94d04d30`.

A tree-wide test file, in this design, is a test file whose cases hold the whole tree, or a whole directory of it, to a rule, rather than one module's behaviour on inputs the case builds.

| Policy clause | What it fixes for this work |
|---|---|
| `skills/verify/SKILL.md` *Scope: cheap and often, broad and once*, the `Phase boundary` row (line 144) | The set a crafter runs when a phase closes: the plan row's cases and "the test modules that read a path the phase changed, whether they name it, import it or glob the directory that holds it". The glob clause is the only clause that reaches a tree-wide file, and it reaches it by a text search that also matches every file that writes the same directory name into a fixture of its own. `read` |
| The same table, the `Review rounds 1..n` row (line 146) | A fix pass runs "what the fix touches". No clause of the row reaches a tree-wide file, so a fix pass that edits a record or a document runs nothing that reads the tree. `read` |
| `agents/crafter.md` *Order of work* steps 7 and 9 | Step 7 sends the crafter to the `Phase boundary` row. Step 9, the fix pass, names no set at all. `read` |
| `agents/proofer.md` *Runs are narrow, through the repository's runner* | The proofer types one module, and its runs are probes for findings. It reads a committed tree that the phase boundary or the fix pass already ran. `skills/core/SKILL.md` *The rule a mechanism is kept against* says a thing is re-checked only when the diff or CI shows it changed, so the proofer's runs stay as they are. `read` |
| `CONTRIBUTING.md` *The test layout*, lines 267 to 269 | "A test file that declares no `TARGET` stands by what its cases run": in `tests/behaviour/` where its cases load or run shipped code, in `tests/text/` where they only read text. `executed`: at `94d04d30` a parse of `^TARGET = "` over the 134 tracked `tests/**/test_*.py` files found 82 that declare no `TARGET`. All 82 stand in `tests/text/` or `tests/behaviour/`, and no file in either directory declares one. So this repository already holds its tree-wide files in two directories, and the layout says so. |
| `CONTRIBUTING.md` *What a contribution is asked for*, line 42 | A contributor runs `bin/test tests/<file> -q` "on each module the change touched", and CI runs the rest. `read` |
| `skills/verify/scripts/broad_gate.py` module docstring, lines 102 to 113 (#638) | `seal gate --preflight` runs arm 2 (`chain_check.py --baseline <base> --sealing`) and arm 3 (`seal.py mode --check`), reads the `Broad gate` row without running it, and runs no test. It does not already do what this work asks. `read` |
| `skills/verify/orchestration.md` *The broad gate* | The broad run is the orchestrator's, after the rounds settle. A failure there costs a fix, a verifying round, a second gate and a second sealer (`skills/code-review/orchestration.md`, as the ticket cites it). `read` |
| `skills/agent-contract/SKILL.md` rule 2 | No agent runs the full suite. A crafter ran #1421's phase set (the next row), so a set that size is a phase set and not the broad gate. `read` |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | Nothing is kept beside the tree to stay in step with it. A list of guard modules kept in a skill or a runner would be such a list, so the guard set has to be a place the layout already defines. `read` |
| The #1421 phase record, `git show v0.34.1:seal/threads/1794096494-compare-reads-a-grader-with-a-string-target/trail/phases/phase-1.md` | The crafter drew its phase set with `git grep -l -F` over `tests/` for 14 terms: `noninferiority`, `evals/scripts`, `"evals"`, `evals/behaviour`, `"behaviour"`, `plugin.json`, `plugin_json`, `.claude-plugin`, `seal/threads`, `"threads"`, `changelog.md`, `gaps.md`, `phase-` and `plan.md`. That gave 68 modules and one command that passed 4,409 cases. The change was `evals/scripts/noninferiority.py` (+4 -2), its test file, the version move in `.claude-plugin/plugin.json`, and the work item's own records (`gh pr view 1427 --json files`, `executed`). The flow log #1424's first comment says most of the crafter's 9.2M tokens went to that set. `read` |
| The phase set measured from `.test_durations` (done-when 2) | `executed`, by a script under the scratchpad that summed the per-case seconds of `git show v0.34.1:.test_durations` by module, which is the Windows leg's stored price of each case. The same file stands at `94d04d30`. The full suite is 1,599.8 s over 132 modules. The terms of the row above, re-run at `v0.34.1`, give the same modules the #1421 record counts, at 1,488.5 s, 93% of the suite. The six terms that match the work item's records (`seal/threads`, `"threads"`, `changelog.md`, `gaps.md`, `phase-`, `plan.md`) pull 57 modules and 1,453.2 s on their own. `tests/skills/test_chain_check.py` alone is 408.1 s, and it names `seal/threads` because it builds fixture repositories. The two directories of tree-wide files, `tests/text/` and `tests/behaviour/`, cost 118.9 s together (16.9 s and 102.0 s). The files that name `evals/scripts/noninferiority.py` or its test file in full are 4, at 38.6 s. That set joined with the two directories is 83 files and 143.1 s. With the files that name `.claude-plugin/plugin.json` in full added for the version move, it is 89 files and 460.6 s. |
| Tree-wide cases that stand in a file declaring a `TARGET` | `executed`, as a sample: a search for walk calls (`rglob`, `ls-files`, `os.walk`, `iterdir`, `glob`) in the files that declare a `TARGET`, each match read at its line. These cases read this repository's own tree and run only where their file is named: `tests/github/test_rules.py#Test_main.test_every_check_line_in_the_tree_holds` (2.32 s), `tests/lib/test_routing.py#Test_parse.test_every_declaration_in_this_repository_still_parses`, `tests/test_censuses.py#Test_module.test_every_file_no_module_file_declares_meets_every_census` (27.38 s), `tests/skills/test_test_layout.py#Test_main.test_accepts_this_repositorys_tests` (4.06 s), the case in `tests/test_conftest.py` that reads `python_files` over `tests/`, and the cases in `tests/lib/test_launch.py` that read `floor_carriers` and `before_any_floor` over the tracked files. The keyword search found these. It does not make the list whole, and *Scope* item 1 owes the whole list. The layout case is the one #1176's round 4 met as "seal layout". |
| `seal/follow-up.md` | No row waits on this work. `read` |
| The policy root, `docs/` | No document states which tests run at a phase boundary or in a fix pass. `executed`: `git grep -n -i -E 'narrow\|phase boundar\|slice' -- docs` returns no such statement. `docs/running/the-broad-gate.md` opens with "Narrow and often, broad once" and then states the broad run alone. |
| The ticket's comments | None. `executed`: `gh issue view 1441 --json body,comments` returned 0 comments, which agrees with the orchestrator's line. |
| `### Process changes` of `v0.35.1`, the latest release | Two rows, on `CLAUDE_CONFIG_DIR` and on the parity walk. Neither touches narrow runs. `executed` |
| The ticket's citation of #717 for the glob clause's grounds | `#717` in this repository is the seal-stamp issue (`gh issue view 717`, `executed`). A search of the `v0.16.0` to `v0.21.0` release notes for `glob` and `phase boundary` found no statement of the clause (`executed`). The history before the initial commit `716d8548` is not in this clone. The design keeps what the ticket says the clause was for: tree-wide readers stay in every phase set. `unverified` as history, and the owner answers it. |

## Scope

In:

1. **Every tree-wide case that stands in a file declaring a `TARGET` moves into a file under `tests/behaviour/` that declares none.** The body of each case stays as it is, and so does its name, unless the destination file already holds that name. The *Grounding* row on such cases lists the ones known at `94d04d30`. The phase that builds this item lists the class whole, by reading each file that declares a `TARGET` for a case that walks a directory of the repository root, lists its tracked files, or runs a check over the root. Each case found moves.
2. **`CONTRIBUTING.md` *The test layout* says where a tree-wide case stands.** The paragraph at line 267 gains two sentences. A case that reads this repository's own tree beyond its `TARGET` stands in a file that declares none. The files that declare no `TARGET`, `tests/text/` and `tests/behaviour/`, are this repository's tree-wide files, which `skills/verify/SKILL.md` *Scope: cheap and often, broad and once* runs at every phase boundary and every fix pass.
3. **The `Phase boundary` row of `skills/verify/SKILL.md` is rewritten.** Its set is one command holding four parts. The first is the cases the phase's plan row names. The second is each test file the phase changed. The third is each test file that reads a changed path: a case opens it, imports it or loads it, directly or through another test file, and a file that only writes the path's name in a fixture, a parameter or a docstring does not read it. The fourth is the repository's tree-wide test files, where its contribution guide says which they are. Where the guide says nothing, the glob clause stands as the fallback for the fourth part: the files that glob the directory holding a changed path. Only a file that walks the records directory reads a work item's records, and such a file is a tree-wide file, so a records path pulls in nothing beyond the fourth part.
4. **The `Review rounds 1..n` row is rewritten** to the `Phase boundary` set, drawn over the paths the fix changed.
5. **`agents/crafter.md` step 9 names the fix pass's run**: the set the `Review rounds 1..n` row names, as one command through the repository's runner, before the close block is written.
6. **`CONTRIBUTING.md` line 42 asks a contributor for `bin/test tests/text tests/behaviour -q`** beside each touched module. A guard failure costs a contributor another push and three platforms of CI, and the two directories cost 118.9 s of stored price.
7. **The measurement of done-when 2 stands in the record of the phase that rewrites the row.** On one tree and one machine, the crafter runs and times two sets with `bin/test`'s default parallel run. The first is #1421's set, regenerated by `git grep -l -F <term> v0.34.1 -- tests/` for each term the *Grounding* row on the #1421 phase record lists. The second is the new row's set for #1421's changed paths. For each set, the record gives the command, the file count, the case count, the exit code and the wall-clock seconds. The *Grounding* row on `.test_durations` is the stored-price reading of the same comparison.

Out, each with its reason:

- **The proofer's own runs.** A finding round reads a committed tree that the phase boundary or the fix pass already ran with the tree-wide files. The core re-checks only what the diff shows changed.
- **`seal gate --preflight`.** It runs no suite, and #638 and #697 built it that way so that a record refusal costs seconds. A guard failing there would still come after the last round, so it would still cost a verifying round.
- **Lint.** `ruff`'s verdict on a file depends on that file and `ruff.toml`, so linting the changed files is exact. The #1421 crafter already did that, and none of the ticket's failures was a lint failure.
- **The orchestrator's records-only commits after the last round.** The core's invariant table gives those to the sealer. Whether a fold is read before the next round is #1442's.
- **A change to a file every test file imports**, such as `tests/conftest.py` or `tests/censuses.py`. The import clause then pulls the whole suite, as it does today. The row the verify table gives a dependency bump already answers that case.
- **A test file that declares no `TARGET` but stands outside the two directories.** Nothing refuses one at `94d04d30`, and none exists. It is a limit: the proofer reads a new file's placement against `CONTRIBUTING.md` *The test layout*. No check is added.
- **The version move to 0.36.0.** The orchestrator assigns it to one work item later.

Where this work meets the release's other items:

- **#1444 shares `CONTRIBUTING.md`.** This work edits line 42 and *The test layout*. #1444 edits the `.test_durations` paragraph of *Running the checks*. No sentence is shared, so either can merge first. The cases *Scope* item 1 moves leave their stored prices under the old ids. 36.3 s of 1,599.8 s goes stale, under the one-second-in-twenty bound of `test_the_durations_file_prices_the_suite`, so this work needs no refresh. If #1444 merges first, its refresh procedure is the one that clears those ids.
- **#1439 shares the `skills/verify/` directory and no file.** It edits `orchestration.md` and `scripts/session_cost.py`. This work edits `SKILL.md`.
- **#1440, #1442 and #1443** edit `agents/framer.md`, `agents/proofer.md`, `docs/running/the-run.md`, `skills/implement/orchestration.md` and `skills/code-review/orchestration.md`. This work edits none of them.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A small code change closes its phase | Given a phase that changes `evals/scripts/noninferiority.py`, its test file and the work item's records. When the crafter draws the set by the new `Phase boundary` row. Then the command holds `tests/evals/test_noninferiority.py`, the files that read either path (`tests/evals/test_rule_cases.py` and `tests/evals/test_seed_defects.py`), `tests/text/` and `tests/behaviour/`. It holds no file that only matched `seal/threads`, `plan.md` or `gaps.md`. | *Scope* item 7's measurement in the phase record names the set and its file count. |
| A fix pass edits only a record | Given a round finding fixed by a change to a work item's record. When the crafter closes the finding. Then its one command includes `tests/text/` and `tests/behaviour/`, so a record reader such as `tests/behaviour/test_docs_line_wrap.py` runs before the next round. | Read `agents/crafter.md` step 9 and the `Review rounds 1..n` row. This work item's own first fix pass, where one runs, names the command in its close block. |
| A tree-wide case runs with the guard directories | Given the case that runs `rules.py --check` over the root. When a phase runs `tests/behaviour/`. Then that case runs. | `bin/test tests/text tests/behaviour -q --collect-only` lists each moved case under its new path. |
| Moving the cases changes no behaviour | Given the cases *Scope* item 1 moves. When they run at their new paths. Then they pass, and the old paths hold none of them. | `bin/seal layout --moved <base> --from <old files> --to <new files>` and its last line, and a `git grep` for each moved case's name that finds it only at its new path. Both go in the phase record. |
| A repository whose contribution guide names no tree-wide set | Given a user repository that never says which test files read the whole tree. When its crafter reads the `Phase boundary` row. Then the fourth part falls back to the files that glob a changed path's directory. | Read the row. |
| Done-when 2 | Given #1421's set and the new row's set for #1421's changed paths. When both are run on one tree. Then the phase record states, for each, the command, file count, case count, exit code and wall-clock seconds. | Read the record of the phase that rewrites the row. |

## Data & interfaces

No interface, schema or script changes. Test files move, three documents and one agent definition change their text, and the comments and docstrings that named a moved case's old home follow it: `lib/launch.py`, `ruff.toml`, `.github/workflows/hygiene.yml` and `tests/censuses.py`.

- The set a crafter types at a phase boundary in this repository becomes `bin/test tests/text tests/behaviour <changed test files> <files reading a changed path> -q`.
- The cases *Scope* item 1 moves keep their bodies. Their pytest ids change from `tests/<area>/test_<stem>.py::<Class>::<case>` to a path under `tests/behaviour/`.

## Rule changes

- change
  file: docs/running/what-a-script-gates.md
  section: The checks
  from: `seal rules --check`, through `tests/github/test_rules.py`, and hygiene's step that
    prints the `check:` lines it did not read
  to: `seal rules --check`, through
    `tests/behaviour/test_this_repository_passes_its_own_checks.py`, and hygiene's step that
    prints the `check:` lines it did not read

## Removes

Each tree-wide case moves rather than leaves. The rows below are the text that goes. Every row's coordinate is as read at `94d04d30`.

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The glob clause as the `Phase boundary` row's way of reaching tree-wide files | `skills/verify/SKILL.md` *Scope: cheap and often, broad and once*, `Phase boundary` row | The row's fourth part names the tree-wide files the contribution guide declares. The glob clause stays only as the fallback where a guide declares none. In this repository, `CONTRIBUTING.md` *The test layout* declares the two directories. |
| "what the fix touches" | `skills/verify/SKILL.md` *Scope: cheap and often, broad and once*, `Review rounds 1..n` row | The row cites the `Phase boundary` set, drawn over the fix's paths. |
| Each tree-wide case at its place in a file that declares a `TARGET`: the *Grounding* row on such cases names the ones known, and *Scope* item 1's enumeration names the rest | `tests/github/test_rules.py#Test_main.test_every_check_line_in_the_tree_holds`, `tests/lib/test_routing.py#Test_parse.test_every_declaration_in_this_repository_still_parses`, `tests/test_censuses.py#Test_module.test_every_file_no_module_file_declares_meets_every_census`, `tests/skills/test_test_layout.py#Test_main.test_accepts_this_repositorys_tests`, the cases of `tests/test_conftest.py` and `tests/lib/test_launch.py` named in that row, and any case the enumeration adds | Files under `tests/behaviour/` that declare no `TARGET`. Each case's body is unchanged. |
| The "each module the change touched" ask standing alone | `CONTRIBUTING.md` *What a contribution is asked for*, line 42 | The same line, with `bin/test tests/text tests/behaviour -q` beside it. |

This work adds no mechanism: no check, no command, no mark and no list. The tree-wide set is two directories that `CONTRIBUTING.md` *The test layout* already defines by what their cases run.

Framed 2026-11-09 by framer, before the build.

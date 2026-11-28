# Inspection: 1795849897-submodule-pointer-in-typed-diffs

Audited `2fbd183c` against `596c79a6`, the commit `release/v0.41.1@{upstream}` resolves to. No earlier `inspection.md` stood, so this run audits the whole work item.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The gate's newest run is followed only by the work item's records | `trail/gate.md`, `run: 6b844b5b against 596c79a6` | `git merge-base --is-ancestor 6b844b5b HEAD`; `git log --ignore-submodules=none --no-merges --name-only 6b844b5b..HEAD ^596c79a6` | holds (`executed`): ancestor, and only `2fbd183c` follows, touching `trail/gate.md` alone |
| The body file is `pr.md` above the heading and the records' text below it | the spawn prompt's body file | `agentic pr-body agentory/threads/1795849897-submodule-pointer-in-typed-diffs --body <file> --check` | holds (`executed`): exit 0, `matches` |
| `seen red`: step 2's case failed against `4a63fef1` on its missing command | `trail/phases/phase-1.md:5` | at-base clone at HEAD with `agents/inspector.md` and `agents/proofer.md` restored from `596c79a6`; `uv run --no-project tests/run_tests.py -q tests/behaviour/test_the_inspector_inspects.py::TestDefinition::test_step_2_reads_the_diff_with_submodules_shown tests/behaviour/test_the_proofer_reads_a_merge_round.py` | holds (`executed`): fails at `test_the_inspector_inspects.py:212`, the `git diff --ignore-submodules=none <base>...HEAD` assertion |
| `seen red`: the merge round's case failed against `4a63fef1` on its missing command | `trail/phases/phase-1.md:5` | the same run | holds (`executed`): fails at `test_the_proofer_reads_a_merge_round.py:33`, the `git log` assertion. The case's second assertion, at `:38`, was shown red apart by restoring HEAD's `agents/proofer.md` with only the `git show` flag removed: it fails at `:38` |
| Both cases pass after the edit | `trail/phases/phase-1.md:5` | `uv run --no-project tests/run_tests.py -q tests/behaviour/test_the_inspector_inspects.py`, then the same for `tests/behaviour/test_the_proofer_reads_a_merge_round.py`, at HEAD | holds (`executed`): 15 passed, 1 passed |
| The probe: under `diff.ignoreSubmodules=all` the three reads hide a moved pointer, and show it with the flag | `frame/design.md:13` | scratch repository with a submodule: `git diff base...HEAD`, `git log --no-merges -p base..HEAD ^base`, and `git show <merge>` on a merge whose resolution sets a third pointer, each with and without `--ignore-submodules=none` | holds (`executed`): 0 `Subproject` lines without the flag, 2, 2 and 3 with it. The same holds with `.gitmodules` `ignore = all` and the config unset, as `changelog.md:3` states |
| No test module held a case of the proofer's merge paragraph | `trail/phases/phase-1.md:6` | `git grep -l -F 'round after a merge' 4a63fef1 -- tests`; `git grep -F 'git show <merge>' 4a63fef1 -- tests` | holds (`executed`, a sample by wording): no match |
| The plan's coordinates at `4a63fef1` | `frame/plan.md:9` | `git show 4a63fef1:agents/inspector.md` lines 63 and 81, `git show 4a63fef1:agents/proofer.md` lines 157-158 | holds (`executed`) |
| The records-only diff stands in `agents/inspector.md` step 3 | `frame/design.md:19`, `frame/plan.md:13` | `grep -n -E '^[0-9]\. \*\*' agents/inspector.md` at HEAD and at `4a63fef1` | does not hold (`executed`): the command stands at `agents/inspector.md:124` at HEAD (`:122` at `4a63fef1`), under `4. **The parties against each other.**` at `:97` (`:95`); step 3 is *A claim against the fact* |
| The version move | `frame/plan.md` *Operational impact* | `git diff 596c79a6...HEAD -- .claude-plugin/plugin.json`; `git grep -n '0\.41\.'` outside the records | holds (`executed`): `0.41.0` to `0.41.1`, the one version field in the tree |
| `## Removes`: nothing | `frame/design.md` *Removes* | `git diff --stat 596c79a6...HEAD` | holds (`executed`): the diff removes two lines, the two lines that took the flag |
| The class of typed git reads that show a party the diff it judges | the issue's *Done when* | `git grep -n -E 'git +(-C +[^ `]+ +)?(diff\|log\|show\|range-diff\|whatchanged\|format-patch\|status)'` over `agents/`, `skills/*.md`, `templates/`, `docs/`, `CLAUDE.md`, `CONTRIBUTING.md` | holds (`executed`, a sample by spelling): the diffs a party judges, `agents/inspector.md:82` and `agents/proofer.md:157` and `:159`, carry the flag. The rest read history, a file's text or a metric. Step 4's records-only diff, `agents/inspector.md:124`, stood in the definition when the issue was written (`fe8cee01`, 2026-11-25), and the issue names two reads, so the design leaving it out holds against the issue |
| Whether an inspector and a round type the commands as the definitions now state them | `gaps.md:8` | none | `unverified`: this run read the installed 0.41.0 definition, whose step 2 still reads `git diff <base>...HEAD`. The first inspector and the first merge round under a release carrying `8de791d6` answer it |
| The broad gate passed at `6b844b5b` | `trail/gate.md` | none (rule 2) | `read`: the record's run line; the orchestrator ran it |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | the three typed reads that show a party the diff it judges carry `--ignore-submodules=none`, each pinned by a case; step "3"'s records-only diff is out | the issue, the diff, the probe, the changelog | the tree: `frame/design.md:19` names the records-only diff as step 3's, and it is step 4's (`agents/inspector.md:124`, under `:97`); `frame/plan.md:13` repeats "step 3's records-only diff" |
| the build | `8de791d6` adds the flag to `agents/inspector.md:82`, `agents/proofer.md:157` and `:159`, a case for each in `tests/behaviour/test_the_inspector_inspects.py` and the new `tests/behaviour/test_the_proofer_reads_a_merge_round.py`, and moves the version | the design, the plan's phase row, the phase record, the re-runs above | none |
| the last round | no round ran: `routing.md` reads `Review` `straight to the PR` | | |
| the changelog | the inspector's diff and a merge round's `git log … -p` and `git show <merge>` carry the flag; both settings hid the pointer from all three; the scripts already carried the flag | the diff, the probe re-run under both settings, `lib/gitcmd.py:121` | none |
| the orchestrator's part of the pull request body | `Closes #1648`, and the quote of `frame/plan.md` *Judgments of the run* | `frame/plan.md:38`, the diff | none |
| the orchestrator's routing grounds | `routing.md:19`: "the diff is two commands in two agent definitions and the cases that pin them" | the Review row's grounds, `routing.md:20`, which describe the one flag | the diff: it changes three commands (`agents/inspector.md:82`, `agents/proofer.md:157`, `:159`), the frame's third read being `git show <merge>`. `routing.md:18` says the issue fixes "the two git reads", which the issue does, and the frame widened to three on the probe's grounds |

```iadd
target: 2fbd183c3b9bfeefe535d34fd0428b66928dadb2 against 596c79a6fd4a36fa55ea7fe383d12c8b97119e40
Verdict: withheld reason: the design's frame/design.md:19 and the plan's frame/plan.md:13 name the records-only diff `git -C <root> diff <the last record's target>..HEAD -- agentory/threads/<item>/` as agents/inspector.md step 3's, and the tree holds it in step 4 (agents/inspector.md:124, under step 4 at :97, at HEAD and at 4a63fef1); and the orchestrator's routing.md:19 grounds say the diff is two commands, where the diff changes three (agents/inspector.md:82, agents/proofer.md:157 and :159)
```

## Run 2: `12249764` against `596c79a6`

The commits since the block above's target, `bc3e02c2` and `12249764`, touch only `inspection.md`, `frame/design.md`, `frame/plan.md` and `routing.md`. No code, case or version file changed (`git diff --stat 2fbd183c..HEAD -- . ':!agentory'` is empty), so the claims of the first run that rest on those stand as re-run there. This run re-reads the claims whose coordinates the two commits touched.

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The gate's newest run is followed only by the work item's records | `trail/gate.md`, `run: 6b844b5b against 596c79a6` | `git log --ignore-submodules=none --no-merges --name-only 6b844b5b..HEAD ^596c79a6` | holds (`executed`): `2fbd183c`, `bc3e02c2` and `12249764` follow, each touching only paths under `agentory/threads/1795849897-submodule-pointer-in-typed-diffs/` |
| The rewritten body file is `pr.md` above the heading and the records' text below it | the spawn prompt's body file | `agentic pr-body agentory/threads/1795849897-submodule-pointer-in-typed-diffs --body <file> --check` | holds (`executed`): exit 0, `matches` |
| The records-only diff stands in `agents/inspector.md` step 4 | `frame/design.md:19`, `frame/plan.md:13` | `sed -n '95,98p;122,125p' agents/inspector.md` at HEAD | holds (`executed`): the command at `:124` stands under `4. **The parties against each other.**` at `:97` |
| No other record sentence still names step 3, two commands, or a count of the release's items | the records | `git grep -n -F 'step 3'` and `git grep -n -E 'two commands\|two to merge\|release.s two'` over the work item's directory, `inspection.md` aside | holds (`executed`, a sample by wording): no match |
| The Implementation row's grounds describe the diff | `routing.md:19` | `git diff 596c79a6...HEAD -- agents tests .claude-plugin` read against the row | holds (`read`): a flag on the typed git reads of `agents/inspector.md` and `agents/proofer.md`, and the cases pinning them; the version move is the last paragraph's |
| The merge order and version move are the orchestrator's choice, with grounds | `routing.md:24` | read against `frame/plan.md:28` and `:32` | holds (`read`): the plan's *Overlap with the release* row names #1648 to merge first on the same grounds, and *Operational impact* names the version move |

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | the three typed reads that show a party the diff it judges carry the flag, each pinned by a case; step 4's records-only diff is out | the issue, the diff, the probe, the changelog, `agents/inspector.md:124` | none |
| the build | `8de791d6`, unchanged since the first run | the design, the plan, the phase record | none |
| the last round | no round ran: `routing.md` reads `Review` `straight to the PR` | | |
| the changelog | unchanged since the first run | the diff, the probe | none |
| the orchestrator's part of the pull request body | `Closes #1648`, and the quote of `frame/plan.md:38` | `frame/plan.md:38` | none |
| the orchestrator's routing grounds | `routing.md:19`: a flag on the typed git reads of two agent definitions; `routing.md:24`: the orchestrator chose this item to carry the version move and merge first | the diff, `frame/plan.md:28` and `:32` | none |

`unverified`, as in the first run: whether an inspector and a round type the commands as the definitions now state them (`gaps.md:8`). The first inspector and the first merge round under a release carrying `8de791d6` answer it.

```iadd
target: 122497641f95296a4a26c6583232db9c85287fe6 against 596c79a6fd4a36fa55ea7fe383d12c8b97119e40
Verdict: cleared
```

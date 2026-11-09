# Review round 2: 1794178394-each-run-reaches-the-tree-wide-guards

```seal
target: 84331b77 against release/v0.36.0
```

This is a verifying round. Its target is the branch at `84331b77` against `release/v0.36.0` at `c7bb14ca`, which is the merge base (executed: `git merge-base HEAD origin/release/v0.36.0`). The fix pass's own commits are `abde6b8c`, `69f00945` and `4ad34865`, and round 1's close blocks stand in `6a0bfadd`. `46e30c7d` is the orchestrator's fold of the frame and `pr.md`. `84331b77` merges the base, which now holds `e244aa49` (#1443), `74211b76` and `c7bb14ca` (#1444). The merge resolved nothing by hand: `git merge-tree --write-tree HEAD^1 HEAD^2` gives tree `5b745a6d`, which is the tree of `84331b77` (executed). The round read the whole diff against the base, as the spawn asked, and answered round 1's two closes.

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` whole at `84331b77`, then both phase records and `trail/rounds/round-1.md`. `seal/parity.md` is absent. `seal/config.md` has no `Record language` row and no `Pact` row.

Facts carried from round 1 and not re-established: the base coordinates of the four manifest readers round 1 named, and the `seal layout --moved` result for the fourteen moved cases. The merge changed none of the ten source files or the five destination files (executed: `git show --stat` of `e244aa49`, `74211b76` and `c7bb14ca`), so that run's check did not fail. Everything else, every verdict included, was re-derived at `84331b77`.

The spawn said finding 2 closed `fixed 69f00945`. Its close block reads `fixed abde6b8c` (`trail/rounds/round-1.md:97`), and `69f00945` is the rewrap after it. Both are ancestors of HEAD, so the chain is unaffected.

## Findings

### 1. Phase 2's corrected set for #1421 still leaves out a test file that opens this repository's own `.claude-plugin/plugin.json`

```seal
severity: should
location: `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/trail/phases/phase-2.md:138-217`, `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/frame/questions.md:16`
evidence: executed `PYTHONPATH=<scratch>/test_tmp_manifest_probe bin/test tests/e2e/teammate/test_teammate_flow.py -q`, an audit hook that logged each open of the real manifest with the running case; read `tests/e2e/teammate/test_teammate_flow.py:134-146`, `tests/e2e/teammate/test_teammate_flow.py:148-162`, `tests/e2e/teammate/test_teammate_flow.py:177-184`, `tests/e2e/teammate/test_teammate_flow.py:271`, `skills/implement/scripts/seal.py:1858-1870`, `skills/implement/scripts/seal.py:1957-1990`
reopens: round-1#1
```

Why it matters: the close does not hold. It rests on re-reading "the eleven files that list held, a closed set" (`phase-2.md:173-176`). Those eleven are the files a search for the manifest's name matched. Round 1 said that such a search is a sample over spellings, and that a case can reach the manifest through a helper and never name it (`round-1.md:30`). The fix pass took the eleven as the class, and the record states the result as whole: "Seven test files outside the two directories read this repository's own `.claude-plugin/plugin.json`" (`phase-2.md:140-142`).

`tests/e2e/teammate/test_teammate_flow.py` names no manifest, and it opens the real one. Its case `test_accepts_the_pull_request_that_moves_the_root_to_local_mode` (`:271`) builds `switching_repository`, which calls `base_repository(..., checks=True)` (`:182`). That runs `seal pr-checks install` (`:161`) through `seal()`, which starts the tree's `seal.py` and asserts it exits 0 (`:134-146`). `install_workflow` calls `plugin_version()` (`seal.py:1988`), which opens `PLUGIN_ROOT/.claude-plugin/plugin.json`, the tree the script stands in (`seal.py:1858-1870`). With no version readable, the install returns `no-version` and the case fails at the exit-code assert. So the file reads a path #1421 changed, by the row's own definition. The probe confirmed it: the hook logged two opens of the real manifest from that case, and the file passed 7 at exit 0 (executed).

The miss is the method, not the count. The class is built from the shipped code that opens the manifest: `plugin_directory_check.py#plugin_name`, `release_seal.py#draw`, `roll_flow_measurement_issue.py:273`, `tag_release.py#version_at`, `lib/core.py#manifest`, `pr_body.py#MANIFEST`, `seal.py#plugin_version` and `broad_gate.py#plugin_version` (executed: `git grep -n -E 'plugin\.json|\.claude-plugin|MANIFEST|PLUGIN_JSON'` over `lib`, `skills`, `hooks`, `bin`, `.github/scripts` and `evals/scripts`). Outside the two directories, 23 test files name one of those scripts or a `seal` subcommand that reaches one (`mode`, `pr-checks`, `pr-body`, `gate`). This was executed as a `git grep` over `tests/` for the script names and the subcommands. Ten of the 23 are among the eleven. `tests/evals/test_rule_cases.py` is in the set already. `tests/github/test_release_report.py` was read: its remaining cases run a stand-in for `payload_meter.py` (`:93`), and its tree case moved in phase 1. The hook ran over the other eleven, the teammate flow in one run and the ten others in a second (`## Probes`). It logged opens from the teammate flow and from no other file. The teammate flow is the one addition this round found. The search for readers is still a sample over the spellings a shipped script opens the manifest by, and the fix pass says so where it states the method.

The fix adds the eighth file to part 3, states the method above in place of "a closed set", and re-runs the set once. The statements that move with it are `phase-2.md:140` ("Seven"), `:173` ("these seven"), the command and its figures at `:186-197`, the comparison at `:199-203`, and the stored-price sums at `:208-217`, which say the 97 files cost 514.6 s and the seven readers 300.8 s. `frame/questions.md:16` Q2's Status quotes "97 files, 24.84 s", and it is the orchestrator's to fold.

```markdown
   - `tests/e2e/teammate/test_teammate_flow.py`:
     `test_accepts_the_pull_request_that_moves_the_root_to_local_mode`
     runs `seal pr-checks install`, whose `plugin_version` reads the
     version for the workflow's pin from the tree `seal.py` stands in.

Phase 2 first set these readers aside after reading each `git grep` match
by eye, and the fix pass of round 1 re-read the eleven files that search
matched. Round 2 found an eighth that names no manifest. So the list is
built from the shipped code that opens the manifest:
`plugin_directory_check.py#plugin_name`, `release_seal.py#draw`,
`roll_flow_measurement_issue.py`, `tag_release.py#version_at`,
`lib/core.py#manifest`, `pr_body.py#MANIFEST`, `seal.py#plugin_version`
and `broad_gate.py#plugin_version`. Each test file outside the two
directories that imports, loads or runs one of them ran once under the
audit hook. That list of shipped readers comes from a search for the
manifest's spellings, so it is a sample over spellings, and a shipped
script that builds the path some other way is the part it did not reach.

- Command: `bin/test tests/text tests/behaviour
  tests/evals/test_noninferiority.py tests/evals/test_rule_cases.py
  tests/evals/test_seed_defects.py tests/github/test_plugin_directory_check.py
  tests/github/test_release_seal.py tests/skills/test_broad_gate.py
  tests/skills/test_pr_body.py tests/skills/test_seal.py
  tests/lib/test_core.py tests/hooks/test_core_start.py
  tests/e2e/teammate/test_teammate_flow.py -q`.
- The file count, the passed and skipped counts, the exit code and the
  wall-clock seconds, as that one run prints them, and the stored-price
  sums at :208-217 taken again over the same files.
```

### 2. The frame's sentences on the release's other items describe the base before the merge, and one names a case `c7bb14ca` removed

```seal
severity: should
location: `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/frame/design.md:50`, `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/frame/design.md:54`, `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/frame/plan.md:46`
evidence: executed `git grep -n 'test_the_durations_file_prices_the_suite' HEAD -- . ':!seal/threads'`, which finds the name only as a stored id at `.test_durations:1234`; executed `git show 94d04d30:.claude-plugin/plugin.json` (0.35.1) beside `.claude-plugin/plugin.json:4` at HEAD (0.36.0), and `git show --stat e244aa49`; read `CONTRIBUTING.md:165-198`
```

Why it matters: these three sentences state the present, and HEAD contradicts each one. None stands in a section dated to `94d04d30`. The orchestrator reads *Operational impact* for the version move (`skills/implement/orchestration.md`, the version paragraph), and the sealer reads the frame against the tree.

- `frame/design.md:54` says the moved cases' 36.3 s go stale "under the one-second-in-twenty bound of `test_the_durations_file_prices_the_suite`, so this work needs no refresh", and "If #1444 merges first, its refresh procedure is the one that clears those ids." `c7bb14ca` removed that case. The staleness verdict now belongs to the `durations` job on the release pull request, against `STALE_SHARE` in `.github/scripts/durations_union.py`. A work item never commits the file (`CONTRIBUTING.md:165-198`). #1444 has merged, so the conditional now reads as an open question when it is already decided.
- `frame/design.md:50` says of the version move to 0.36.0, "The orchestrator assigns it to one work item later." `frame/plan.md:46` says the same. `e244aa49`, #1443's pull request, moved `.claude-plugin/plugin.json` from 0.35.1 to 0.36.0, and this branch holds that commit through the merge. An orchestrator reading these sentences at HEAD can take the move as still owed.

`gaps.md:13-16` and `frame/plan.md:44` stay true at HEAD: `.test_durations` has not changed since `94d04d30` (executed: `git log 94d04d30..HEAD -- .test_durations` lists nothing), the release refresh is still the step that clears the old ids, and the 5% bound still exists, now as `STALE_SHARE`. The three sentences are frame text, so the orchestrator's fold rewrites them.

```markdown
- **The version move to 0.36.0.** `e244aa49`, #1443's pull request, made it on the release branch, and this branch holds it through its merge of the base, so this work does not move the version.
```

```markdown
- **#1444 shares `CONTRIBUTING.md`.** This work edits line 42 and *The test layout*. #1444 rewrote the `.test_durations` paragraph of *Running the checks*. No sentence is shared, #1444 merged first (`c7bb14ca`), and the merge into this branch resolved no conflict. The cases *Scope* item 1 moves leave their stored prices under the old ids, 36.3 s of 1,599.8 s. Since #1444, no work item commits `.test_durations`. The release pull request's `durations` job judges the file against `STALE_SHARE`, and the release refresh clears those ids.
```

```markdown
This pull request does not move the version. `e244aa49`, #1443's pull request, moved it to 0.36.0 on the release branch, and this branch holds that commit through its merge of the base.
```

## Confirmations

```seal
confirms: round-1#2
```
What holds: `CONTRIBUTING.md:277-282` now reads "A case that walks this repository's tree or a whole directory of it, lists its tracked files, or runs a check over its root stands in a file that declares none". That is *Scope* item 1's class, and it has one reading. The changelog's bold sentence (`changelog.md:4`) uses the same terms. `pr.md:4` quotes it word for word, and so does `frame/design.md:35`, *Scope* item 2, after `46e30c7d` (read). The paragraph wraps within the line bound: `tests/behaviour/test_docs_line_wrap.py` passed in the run below (executed).

What matched: the fold `46e30c7d`. `frame/questions.md:16` Q2 states the set the fix pass timed, with its commit and conditions. *Scope* item 2 states the new class. `pr.md:4` follows the changelog. `frame/plan.md:54` names the three statements and their grounds (read). Q2's figures move with finding 1.

What matched: the parts of round 1's finding 1 that the fix got right. `tests/skills/test_broad_gate.py`, `tests/skills/test_pr_body.py:627-635` and `tests/skills/test_seal.py` read the real manifest, through `broad_gate.plugin_version`, `PR.MANIFEST` and `SEAL.plugin_version` (read). The four files the record leaves out build or name a manifest of their own, and round 2's hook over the ten files below logged no open from any other file. The set at `phase-2.md:186-191` is 35, 52 and 10 files, so 97 (read).

What matched: `pr.md`'s six quotes, each found word for word at the coordinate it names after runs of whitespace collapse (executed, a comparison script over `changelog.md`, `frame/plan.md` and `gaps.md`).

What matched: this work item's text beside #1444. `CONTRIBUTING.md:42-44` asks for `bin/test tests/text tests/behaviour -q`. #1444 removed the case that ran only against the whole collection and that "naming one module skips". So the ask now runs nothing that judges `.test_durations`, and no sentence of *Running the checks* (`CONTRIBUTING.md:143-198`) conflicts with line 42 or *The test layout* (read). `skills/verify/SKILL.md`'s rewritten rows name no durations file (executed: `git grep -n -i durations HEAD -- skills/verify agents/crafter.md` finds only `session_cost.py:2175`). The moved cases run at HEAD in the tree-wide set below, and `bin/seal layout --check` exits 0 (executed).

What matched: the changelog's "as 28 test files do". `git grep -l -P '^[ \t]*(from test_\w+ import|import test_\w+)' HEAD -- tests` lists 28 files at HEAD, as at `49dbc59b` (executed).

What matched: the acceptance row on a fix pass that edits a record (`frame/design.md:63`). Finding 1's close block names the run of the set at `69f00945` and its figures, and the command stands at `phase-2.md:186-191`. Finding 2's close names the run that refused the 117-column line (read).

`frame/plan.md` has no `## Overlap with the release` section. `e244aa49` added that section to `templates/records/sdd-plan.md` after this frame was written. `frame/design.md:52-56`, *Where this work meets the release's other items*, holds the same content, and no check reads a plan for the section. This is no finding. Finding 2's snippet keeps that list true.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `84331b77`; `gaps.md:7` labels them `unverified`, and the label is honest, since no party claims a broad run | the branch at `84331b77` | the orchestrator, at the broad gate |
| Whether the two timed runs of *Scope* item 7 compare like with like, since each is one run on a machine under the release's other sessions (`phase-2.md:109-117`) | `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/trail/phases/phase-2.md` | the orchestrator, where it weighs done-when 2 |
| Where the glob clause came from, which the frame labels `unverified` as history | `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/frame/design.md:28` | the owner |

## Probes

| Command | Result |
|---|---|
| `PYTHONPATH=<scratch>/test_tmp_manifest_probe bin/test tests/e2e/teammate/test_teammate_flow.py -q`, with a `sitecustomize` audit hook logging each open of the real `.claude-plugin/plugin.json` with `PYTEST_CURRENT_TEST` | exit 0, 7 passed; two opens logged, both from `test_accepts_the_pull_request_that_moves_the_root_to_local_mode` |
| The same hook over `tests/evals/test_replay_targets.py`, `tests/github/test_publish_release_note.py`, `tests/lib/test_config.py`, `tests/skills/test_agentic_pytest_record.py`, `tests/skills/test_passages.py`, `tests/skills/test_seal_stamp.py`, `tests/skills/test_session_cost.py`, `tests/test_censuses.py`, `tests/test_conftest.py` and `tests/skills/test_chain_check.py` | exit 0, 1,277 passed; no open logged |
| `bin/test tests/text tests/behaviour -q` at `84331b77`, the `Review rounds 1..n` set over the fix pass's paths, since no test file outside the two directories reads `CONTRIBUTING.md` or the records | exit 0, 1,789 passed and 8 skipped in 10.11 s |
| `bin/seal layout --check` at `84331b77` | exit 0; `seal layout: 139 files read, 0 refused, 87 declare no TARGET` |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.36.0 --root <the branch worktree> --worktree`, after this record | exit 0; it refused this record's two findings as open, with no close block, and named the gate record and the guarantee, which the broad run and the sealer write; it printed no notice at `frame/design.md`; the probe's hook and its scratch directory were removed before the run |

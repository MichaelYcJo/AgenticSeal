# Review round 1: 1794383425-a-committed-durations-file-turns-ci-red

```seal
target: ef4732d70 against origin/release/v0.37.4
```

This is the first round, so no earlier round's coordinates were carried. Every fact below was opened at `ef4732d70`, in a `git clone --no-local` of the branch made for this round. The base is `957a3bc7d`.

## Findings

### 1. The S3 case drops a word left over after the last option, so a bare `--stale-fails` passes it

```seal
severity: should
location: `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:165-173`, `seal/threads/1794383425-a-committed-durations-file-turns-ci-red/frame/design.md:61`
evidence: executed `bin/test tests/behaviour/test_tmp_union_step_probe.py -q -p no:xdist -s` in the round's clone, and `git grep -n -e stale -e committed` over the shard module and `tests/github/test_durations_union.py`, which printed nothing; read `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:165-205`
```

Why it matters: S3's *Verifiable how* cell at `frame/design.md:61` says "A workflow case asserts the union step's command carries no `--committed` and no `--stale-fails`." That case is `test_the_durations_job_needs_pytest_and_runs_unless_cancelled`. It asserts that `sorted(opts) == ["--count", "--out", "--parts"]`, and `union_step` builds `opts` from `range(2, len(words) - 1, 2)`. When the word count is odd, the last word is never read. `--stale-fails` takes no value, so it is exactly that last word when it is appended to the command. The probe passed `... --out .test_durations --stale-fails` to `union_step`, and the options came back as `['--count', '--out', '--parts']`. The case's assertion holds on that command. The shapes the case does catch are `--committed FILE` and the old `${{ ... && '--stale-fails' || '' }}` expression. The expression splits into nine words, and phase 4 showed it red. No other case names either flag (the `git grep` above).

What bounds the cost: `durations_union.py#arguments` would refuse the flag through argparse with exit 2, so the `durations` job would go red on the first run that carried it. The release therefore ships no age verdict through this hole. What it does ship is a frame row that claims more than its case holds, and the sealer verifies S3 by that row. The fix makes the claim true. The case's docstring and S3's wording then need no change.

```python
def union_step(steps):
    """`(index, options)` of the one of STEPS that runs the union script,
    its options being each `--name` word and the word after it; a word left
    with no value after it, such as a bare flag, is refused."""
    (at,) = [
        i for i, step in enumerate(steps) if "durations_union.py" in step.get("run", "")
    ]
    words = steps[at]["run"].split()
    assert words[:2] == ["python", ".github/scripts/durations_union.py"], words
    assert len(words) % 2 == 0, f"a word with no value after it: {words[2:]}"
    return at, {words[i]: words[i + 1] for i in range(2, len(words), 2)}
```

The new assertion needs to be seen red under contract rule 15, with `--stale-fails` appended to the union step's `run:` line in `test.yml`.

### 2. Three frame sentences state what the target does not hold

```seal
severity: should
location: `seal/threads/1794383425-a-committed-durations-file-turns-ci-red/frame/design.md:39`, `seal/threads/1794383425-a-committed-durations-file-turns-ci-red/frame/design.md:44`, `seal/threads/1794383425-a-committed-durations-file-turns-ci-red/frame/plan.md:60`
evidence: executed `git grep -n test_the_workflow_is_not_a_step_of_the_release_job` (hits only under `seal/threads/`) and `git log -S test_the_workflow_is_not_a_step_of_the_release_job -- tests/behaviour/test_a_release_publishes_its_note.py` (`eec0bd04`); executed `gh run view 42996432567 --json conclusion,headSha,event,jobs` (event `workflow_dispatch`); read `trail/phases/phase-5.md`, the run's section
```

Why it matters: neither section is dated to the commit the framer read. Each sentence says what the work does, so it is read against `ef4732d70`.

- `frame/design.md:39`, *Scope* item 3, says of `tests/behaviour/test_a_release_publishes_its_note.py`: "its third, `test_the_workflow_is_not_a_step_of_the_release_job`, reads `hygiene.yml`'s text by substring". At the target the module holds two workflow cases and no third. #1483 removed the case in `eec0bd04`, and this branch took that commit in the merge `3ed9a1bff`. `frame/plan.md` *Overlap with the release*, the #1483 row, already records the removal, so the two frame files disagree with each other.
- `frame/design.md:44`, *Scope* item 8, says the slowest Windows shard is recorded "after, from this work item's own pull request run, in the phase record". `frame/plan.md:60`, the phase 5 row, names "this work item's pull request run, its job times written in the phase record". The phase record's after reading comes from run 42996432567, which is a `workflow_dispatch` of `25133f410` and no pull request's run. S2 and S11 at `:60` and `:69` were folded to name that run, and these two sentences were not. A sealer who reads them looks for a pull request run that the record does not cite.

The fix rewrites the sentences in place:

```markdown
`frame/design.md:39`, the sentence on the release-note module:
`tests/behaviour/test_a_release_publishes_its_note.py#workflow`, `#job` and `#steps` go, and its two workflow cases read the loader; its third case, `test_the_workflow_is_not_a_step_of_the_release_job`, left the tree with #1483 (`eec0bd04`), merged at `3ed9a1bff`.

`frame/design.md:44`, the last sentence of *Scope* item 8:
The slowest Windows shard is recorded before, from the measurement in *Grounding*, and after, from this work item's own CI run (the `workflow_dispatch` run 42996432567 at `25133f410`), in the phase record.

`frame/plan.md:60`, the *Verified by* cell's last clause:
this work item's own CI run (the `workflow_dispatch` run 42996432567 at `25133f410`), its job times written in the phase record
```

### 3. `skills/settle/SKILL.md` keeps an exception for a durations refresh, a commit this work ends

```seal
severity: should
location: `skills/settle/SKILL.md:212`
evidence: executed `git grep -n -i -e 'durations refresh' -e 'refresh pull request'` (one hit outside this work item, `skills/settle/SKILL.md:212`), `git merge-base --is-ancestor f093d771 8657297d` (true), and `git log --oneline 8657297d..HEAD -- .test_durations` (only `4a85b176`); read `skills/settle/SKILL.md:200-217`, `frame/design.md:24`, `trail/phases/phase-4.md`, the paragraph on the old fact's other statements
```

Why it matters: step 5 of the settle skill tells the settling session which released commits carry `Seal-Routing: no work item` without a route having been chosen: "A settle's commit or a durations refresh carries that trailer with no route chosen and is not one." The durations refresh was the release's hand commit of `.test_durations`. This work removes the file and the recipe, and `CONTRIBUTING.md` *Running the checks* now says "nothing refreshes it by hand". No refresh commit remains for a future settle to read. The last one, `f093d771`, came before the 0.37.0 settle `8657297d`, and the only later commit to touch the file is this work's deletion. The clause is an exception that stood on the old fact. `skills/core/SKILL.md` *The rule a mechanism is kept against* and contract rule 19 say the same change removes it. `skills/` is outside the policy root, so the clause is rewritten in place and not stated for the settle.

The method missed it. The *Grounding* row of readers at `frame/design.md:24` was built from `git grep` on `test_durations`, `test-durations` and `durations_union`, and the clause names none of them. Phase 4's `git grep -i refresh` covered only `.github`, `CONTRIBUTING.md` and the changed test modules. Phase 4 called its search a sample and said where it stopped, so the account is honest about that limit. The miss lies in `skills/`, outside the search.

```markdown
   grounds its body gives. A settle's commit carries that trailer with no
   route chosen and is not one. `git log --grep` on a commit's short hash
```

No case pins the clause (the `git grep` above found no test holding "durations refresh"), so no case changes with it.

## Confirmations

What matched: the cache steps in `.github/workflows/test.yml:128-134` and `:204-209` are the steps `frame/design.md` *Data & interfaces* gives: the path, the save key with `run_attempt`, the `test-durations-` prefix, the cross-system flag on both sides, and the save guarded off pull requests. The restore runs only where `matrix.split` is set, so only the four Windows shards restore. Run 42996432567 shows the restore skipped on the ubuntu and macOS jobs. (read; the run's steps are phase 5's account, and its job list was executed below.)

What matched: phase 5's job times hold. `gh run view 42996432567 --json jobs` gives ubuntu 3.12 116 s, ubuntu 3.14 87 s, macOS 199 s, Windows groups 104, 145, 244 and 147 s, and `durations` 11 s. The run's head is `25133f410`, and the only files changed from there to the target are this work item's records (`git diff --stat 25133f410 HEAD`). (executed)

What matched: `.github/scripts/release_report.py#durations` returns None for no path or no file, raises `Unreadable` for a file that is present but does not parse, and `main` reads both unions before any tree. The suite row's Change cell is the absent mark where either side is None. `module_rows` writes `no union found` in both cells of a side with none, and `—` for a file that one present union lacks. This matches S5 and phase 4's decisions. (read, `release_report.py:144-197`, `:320-331`, `:367-394`)

What matched: `durations_union.py` writes the union only after every refusal has passed, and exits 2 having written nothing. The upload and save guards `!cancelled() && hashFiles('.test_durations') != ''` pick the same runs as the default `success()` in every case but one. That case is a union that was written whole, after which `emit` failed to append the summary. There the guards upload and save a complete union, which is the better outcome. They cost two expressions, and the save guard is the one *Data & interfaces* gives. This round keeps both, and opens no finding on phase 4's open question. (read, `durations_union.py:186-217`)

What matched: macOS's budget of 10 minutes. The comment at `test.yml:43-51` states the rule, and it says that macOS's budget was set before its one job had run, from the shards' case time plus one fixed cost. The base the rule names is the slowest of the runs measured, because one run varies from the next. The one measured macOS job gives 298.5 s at 1.5 times, which is 1.5 s under 5 minutes. The framer's model of the slowest of 38 runs gives 222 s, so 333 s and 10 minutes. Phase 5's choice follows the rule's own reason, and the comment tells a reader why the value is above the one-run figure. (read)

What matched: `gaps.md` `## Not verified` loses no row without the word `closed`. Each row that a commit in the range removed comes back in the same commit, reworded or marked `closed` (executed, `git log -p 957a3bc7d..HEAD -- .../gaps.md`, each removed line set against the lines added). The five readers that `## Not done` names as stripping shell comments with no case watching are the full list of `code_lines` callers outside `tests/conftest.py` and `tests/test_conftest.py`, less the two that have cases, `tests/text/test_ci_gives_the_checks_what_they_need.py#job_scripts` and `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py#base_spellings` (executed, `git grep -n -w -e code_lines -e code_line -- tests`).

What matched: each quote in `pr.md` stands word for word at the source it names, in `frame/plan.md` *Alternatives considered* row A and *Judgments of the run* rows 2 to 4 (read). `Commit and pull request language` is English, so no `pr.<lang>.md` is owed. The `changelog.md` items agree with the tree and with the run's figures (read).

What matched: the merge `3ed9a1bff` holds #1483's deletions. `git diff 957a3bc7d HEAD` names neither `skills/verify/scripts/broad_gate.py`, `tests/skills/test_broad_gate.py` nor `tests/behaviour/test_the_gate_names_every_step_ci_runs.py`, and `git show --remerge-diff` names the six files the plan's judgment row counts (executed).

What matched: the narrow modules of phases 1, 4 and 5 pass in the clone: `tests/github/test_durations_union.py`, `tests/github/test_release_report.py`, `tests/github/test_run_tests.py`, `tests/test_workflows.py`, the shard module, `tests/text/test_ci_gives_the_checks_what_they_need.py` and `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`. `bin/seal layout --pairs` names no pair in the three rewritten files that declare `TARGET` (executed). The suite as a whole stays `unverified`. Every phase record and `gaps.md` labels it so, with the orchestrator named, so the label is honest.

Phase 2's duplicate-key row: no fact the frame states is about a key written twice. `yaml.BaseLoader` keeping the last value changes what a test reads only for a workflow that writes a key twice, and no workflow in the tree does. So the round opens no finding on it. Whether GitHub refuses such a workflow on its own is a row of `## Not judged`.

Phase 3's comment-stripping readers stay without a fixture. Each is a test helper whose stripping no frame fact states. The scripts they read hold no shell comment that their strings match, so the round opens no finding. The five are `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py:28`, `tests/behaviour/test_the_release_check_watches_what_ships.py:183`, `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py:35`, `tests/behaviour/test_the_release_seal_is_drawn.py:33` and `tests/behaviour/test_a_body_naming_two_issues_claims_one.py:60`.

The `chain_check.py` run printed five notices at `frame/design.md:137`, the `## Rule changes` removal from `docs/releasing/release-checklist.md`. Each notice names a test that holds "`Seal-Routing: no work item`" or "`CONTRIBUTING.md` *Running the checks*". The five tests read other files. Two read `skills/implement/routing-question.md`, one reads the settle skill, one writes the trailer into a chain-check fixture commit, and one uses the section's name as a label in its own case. None of them reads the checklist, and the checklist keeps the trailer at `:71`. No pin holds a rule's wording that the removal takes out, so the round opens no finding on them.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether GitHub's workflow parser refuses a mapping key written twice, which would make phase 2's lost refusal moot. This round recalls that it does and did not read it | `gaps.md` `## Not done`, the first paragraph | the orchestrator, from GitHub's workflow syntax documentation or one dispatched run of a branch carrying such a key |
| A Windows shard restoring the union an ubuntu job saved, on a pull request after a push to `main` (`frame/questions.md` Q1) | `.github/workflows/test.yml:128-134` | the orchestrator, from the restore step's log in that run, as `gaps.md` names |
| The full suite, lint and format over the tree | the whole tree | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_tmp_union_step_probe.py -q -p no:xdist -s`, a probe that hands `union_step` the union command with a bare `--stale-fails` appended | 1 failed: `union_step` returned the options `['--count', '--out', '--parts']`, so the shard case's assertion holds on that command |
| `bin/test` over the seven narrow modules named under `## Confirmations` | 129 passed, 1 skipped, exit 0 |
| `gh run view 42996432567 --json conclusion,headSha,event,jobs` | success, event `workflow_dispatch`, head `25133f410`; the job times phase 5 records |
| `bin/seal layout --pairs tests/test_workflows.py tests/github/test_durations_union.py tests/github/test_release_report.py` | 3 files read, 0 pairs |

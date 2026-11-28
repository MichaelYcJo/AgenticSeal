# Phase 1: 1795841829-skill-descriptions

## What this phase found

**The frame holds for phase 1.** Each coordinate of `frame/plan.md` *Technical context* and of `frame/design.md` G9 that the build used stood at the phase's base, `41cc6ba8`: the docstring sentence on `disable-model-invocation` at lines 39 to 42 of `tests/text/test_the_agent_contract_holds_the_universal_rules.py`, the contract-only assertion inside `#test_the_contract_is_a_skill_that_preloads_and_is_not_a_command`, `#skill_groups` and `#test_auto_firing_skills_declare_when_not_to_fire` in `tests/behaviour/test_chain_hooks_hardening.py`, and the nine `NOT for` lines S2 counts. M1 printed 4,860 at `41cc6ba8`, the total G5 gives for `24c5276f`. The skill files, the agent definitions and the manifest at `41cc6ba8` are those of the `v0.40.1` tag (executed: `git diff --stat v0.40.1 fdb878b7` lists only files under `agentory/threads/`, and `fdb878b7..41cc6ba8` touches only `frame/questions.md`).

**The measurement's record was written from this crafter's own reading.** `grep -c "SENTINEL-CORE-b8c05beca29b"` and `grep -c "SENTINEL-CONTRACT-b8c05beca29b"` over each run's `subagents/agent-*.jsonl` printed 3 and 3 for session `125e9be9-ce8c-416f-98b9-d022f6555a8e` (flag off) and 0 and 0 for session `2a7a59dd-1eaa-4957-a2ad-07a50ed0d450` (flag on), as the orchestrator's spawn said. Two readings were added that the spawn did not name. A phrase of each body that no prompt holds stands in the flag-off transcript (3 and 2 lines) and nowhere in the flag-on one, so the flag-on agent's `skills:` entries did not fall back to the installed plugin's skills. Neither session's own transcript holds `agentic:`, so the `--settings` override kept the installed plugin out. The flag-off run shows both sentinels, so by `frame/plan.md` *The measurement step, before phase 1* the run is not void and decides that the flag blocks the preload. The record is `docs/experiments/2026-11-28-disable-model-invocation-blocks-preload.md`, in the sections `docs/experiments/README.md` gives (`frame/design.md` G13).

**The record names the `v0.40.1` tag where it first named the clones' commit.** `tests/text/test_a_cited_commit_outlives_the_squash.py#test_every_cited_commit_outlives_the_squash` refused the bare `fdb878b7` the first draft wrote, because the squash drops it. The tag holds the same skills, agents and manifest (first paragraph above). For the same reason `changelog.md` states its totals of the release `0.40.1` and of this change, not of `24c5276f` and `cc6a6f2b`. Judged against contract rule 19's paragraph on a count stated of a named commit or a published release.

**The record joins `tests/behaviour/test_docs_line_wrap.py`'s `COVERED` list at birth.** The frame does not name this edit. The list's own comment asks for a file to be added once its prose fits, and the two dated records before it were added the same way. The entry was seen red: with one line of the record lengthened to 95 columns, `bin/test tests/behaviour/test_docs_line_wrap.py -k 2026-11-28 -q -p no:xdist` printed `docs/experiments/2026-11-28-disable-model-invocation-blocks-preload.md:7 is 95 columns (limit 88)`, and it passed with the line restored.

**S4, the new case seen red and green.** `tests/behaviour/test_chain_hooks_hardening.py#test_no_preloaded_skill_carries_the_flag_that_blocks_its_preload` was written first and passed against the tree as it stood. With `disable-model-invocation: true` added below `user-invocable: false` in `skills/core/SKILL.md`, the case failed on its one assertion:

```
E       AssertionError: these skills are listed in an agent's `skills:` and carry `disable-model-invocation: true`, which stops them reaching the agent: ['core']
```

With the line removed it passed. After the build commit `cc6a6f2b`, `agentic mutate` made the same edit to each of the two preloaded skills:

```
bin/agentic mutate skills/core/SKILL.md --replace "user-invocable: false" "user-invocable: false
disable-model-invocation: true" --tests "bin/test tests/behaviour/test_chain_hooks_hardening.py -q -p no:xdist -k test_no_preloaded_skill_carries_the_flag_that_blocks_its_preload"
```

It printed `red: the cases failed against the mutation (exit 1)` with the case naming `['core']`, and the same command over `skills/agent-contract/SKILL.md` printed `red` with the case naming `['agent-contract']`. Both files were restored from the command's held bytes, and `git status --short` printed nothing after them. No shipped code adds behaviour in this phase: the other changes are frontmatter text and the removal of a case and an assertion, which owe no mutation run.

**S1, S2 and S3 at `8fc3c2fe`.** M1, as `frame/plan.md` *Technical context* gives it, printed:

```
agent-contract 119
code-review 475
commit-pr-convention 428
core 266
implement 326
legacy-parity 332
settle 512
verify 331
writing-style 597
total 3386
```

`git grep -n 'NOT for' -- 'skills/*/SKILL.md'` printed one line in each of `skills/code-review/SKILL.md`, `skills/commit-pr-convention/SKILL.md` and `skills/writing-style/SKILL.md`, each opening `NOT for:`, and no other line. `git grep -n -E 'Use when|NOT for|disable-model-invocation' -- skills/core/SKILL.md skills/agent-contract/SKILL.md` printed nothing and exited 1.

**The contract's case keeps its name.** `#test_the_contract_is_a_skill_that_preloads_and_is_not_a_command` no longer holds the preload itself: the new case does, for every preloaded skill. The frame names no rename, and a rename of a case is no part of *Scope* item 4, so the name stays and the module docstring names the case that holds the preload.

**The phase-boundary set ran as one command at `fbbe27a1`, before the record's citation was fixed and before this record and `gaps.md` were written:**

```
bin/test tests/text tests/behaviour tests/lib/test_core.py tests/lib/test_gaps.py tests/hooks/test_core_start.py tests/hooks/test_edit_leaves_copies.py tests/skills/test_payload_meter.py tests/skills/test_session_cost.py tests/skills/test_passages.py tests/skills/test_rules.py tests/skills/test_settle.py tests/skills/test_rule_changes.py tests/skills/test_fold_check.py tests/skills/test_chain_check.py tests/skills/test_agentic.py tests/skills/test_broad_gate.py tests/github/test_release_mark.py -q
```

`tests/text` and `tests/behaviour` hold the tree-wide files (`CONTRIBUTING.md` *What a contribution is asked for*). The other files are the ones that name a path the phase changed, `plugin.json`, a `SKILL.md` or `docs/experiments/`, and open the repository's own tree, found by `grep` over the test files outside those two directories. That list is a sample: a file that reads a changed path through a helper without naming it is the part the `grep` did not reach. The run before the record and the memo printed `3 failed, 2667 passed, 11 skipped`. Two of the failures, `test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview` and `test_this_repository_passes_its_own_checks.py::Test_agentic_unverified::test_this_repositorys_own_overviews_are_all_readable`, read the work item's `gaps.md`, which this phase writes as it closes. The third was the cited commit above. The hand-back gives the run after this record.

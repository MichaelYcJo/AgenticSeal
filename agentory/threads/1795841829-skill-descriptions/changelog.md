### Changed

- **The descriptions of the plugin's skills, which every session holds in its skill listing, shrink from 4,860 characters in 0.40.1 to 3,386 with this change (#1650).** The count is each description that a model may invoke, as `frame/plan.md` *Technical context* M1 measures it. `core` and `agent-contract` each carry a description of two sentences or fewer that says what the file holds and that every agent receives it preloaded. Both keep `user-invocable: false`. `implement`, `legacy-parity`, `settle` and `verify` carry no `NOT for:` clause. `code-review`, `commit-pr-convention` and `writing-style` each keep the one item a recorded confusion asked for: a typed `/code-review` runs Claude Code's built-in command, the prose of a PR body belongs to `writing-style`, and the format of a commit, a PR title or a branch belongs to `commit-pr-convention`.
- **A skill that an agent preloads cannot take `disable-model-invocation: true`.** On Claude Code 2.1.332 the flag stops a skill from reaching an agent through the agent's `skills:` list, and the agent says nothing of the loss, as `docs/experiments/2026-11-28-disable-model-invocation-blocks-preload.md` records. `tests/behaviour/test_chain_hooks_hardening.py#test_no_preloaded_skill_carries_the_flag_that_blocks_its_preload` refuses the flag on each skill a definition under `agents/` lists in its `skills:`, and replaces the assertion that held the contract alone.

### Removed

- **No case requires a `NOT for:` clause in a skill a model may invoke.** `test_auto_firing_skills_declare_when_not_to_fire` is gone: its history records no catch, and it made the core carry a clause for its own sake. Whether a clause names a confusion worth its characters is read at review.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-11-28 | The core's description says what the file holds and that every agent receives it preloaded and the `SessionStart` hook prints it into a session, with no `Use when:` line and no `NOT for:` clause. A skill an agent preloads takes no `disable-model-invocation: true` | Every session pays for the description in its listing, and the flag stops the preload every agent depends on | https://github.com/MichaelYcJo/AgenticSeal/issues/1650 |

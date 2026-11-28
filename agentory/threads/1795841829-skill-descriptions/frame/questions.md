# Questions for the planner: 1795841829-skill-descriptions

The ticket left these judgments open, and the tree answered each. Their grounds stand where each line points, and nobody reopens them here:

- Whether `core` and `agent-contract` leave the model's listing or only shorten: `frame/plan.md` *Alternatives considered* rows A1 and A2.
- What the short descriptions of `core` and `agent-contract` hold: `frame/design.md` *Scope* item 2.
- Which `NOT for:` clauses name a confusion on record: `frame/design.md` *Grounding* G10.
- Where the run's result is recorded: `frame/design.md` *Grounding* G13.
- Which merges first against #1655 and #1659: `frame/plan.md` *Overlap with the release*.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | On Claude Code as installed when the run is made, does a skill whose frontmatter carries `disable-model-invocation: true` still reach an agent, with its whole body, through that agent's `skills:` list? The framer ran no probe, for three reasons. The spawn assigned the run to a step after the frame. The 2026-09-03 method needs `/reload-plugins`, which no subagent can type. The headless session that replaces it spawns an agent, which contract rule 6 withholds from every agent, so the orchestrator takes the run (`frame/plan.md` *The measurement step, before phase 1*). | a measurement | The preload survives: the record states that the measured behaviour contradicts Claude Code's documentation (`frame/design.md` G7), and the build is unchanged, because `frame/plan.md` row A1 is rejected whatever the run shows. The preload is blocked: the record measures what `tests/text/test_the_agent_contract_holds_the_universal_rules.py` states, and the build is unchanged | `core` and `agent-contract` keep `user-invocable: false`, take no `disable-model-invocation`, and carry a short description (`frame/design.md` *Scope* item 2) | answered 2026-11-28 by the orchestrator: the preload is blocked. On Claude Code 2.1.332, the control run (flag-off) delivered both sentinels to `probe:sentinel` (`grep -c` 3 and 3 in its subagent transcript) and the run with `disable-model-invocation: true` on both skills delivered neither (0 and 0); commands and transcript paths are in `docs/experiments/2026-11-28-disable-model-invocation-blocks-preload.md` |

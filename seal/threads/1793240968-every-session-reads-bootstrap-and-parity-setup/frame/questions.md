# Questions for the planner: 1793240968-every-session-reads-bootstrap-and-parity-setup

## Answered by the tree, not to be reopened

- **The parity setup becomes one sentence and does not move.** The issue
  hands this choice to the framer. The section restates steps 2, 3, 5 and 6
  of `skills/parity-setup/SKILL.md` *Procedure*, and `CLAUDE.md` *The rule a
  mechanism is kept against* gives a fact one source. `plan.md` A2 weighs
  the move. This replaces the issue's Done-when wording "the new file holds
  both unchanged in substance": the new file holds the bootstrap unchanged,
  and the parity setup lives in the skill.
- **One pointer sentence in `orchestration.md` serves both sections.** The
  parity question is reached only through the bootstrap's step 3 and
  through `/agentic:parity-setup`, so a second sentence would name a
  condition no session meets in that file.
- **The new file is `skills/implement/bootstrap.md`, and its heading stays
  `## Orchestrator: Bootstrap`.** The issue asks for a file under
  `skills/implement/`. Keeping the heading keeps every citation's italic
  text, so only the path moves, and keeps the acts table's mechanical row
  set (`plan.md` A4).
- **The acts check reads a third file rather than a glob.** `plan.md` A6.
- **`.github/scripts/rules.py#RULE_FILES` does not gain the file.** The
  moved text holds no `check:` line (executed, `grep`). `plan.md` A7.
- **The process-row rule names the new file.** A change to first setup
  changes the way of working as much as a change to `orchestration.md`
  does, and the rule's reader, the next framer, needs it for the same
  reason. `frame/design.md` *Rule changes*, the last item.
- **The orchestrator reads the parity-setup skill's file; it does not invoke
  the skill.** The skill's frontmatter carries
  `disable-model-invocation: true`.
- **Test function names stay.** `.test_durations` keys on them, and none of
  them names the file the text lives in, except
  `test_both_orchestration_files_are_read`, whose body iterates whatever
  `FILES` holds.
- **No `docs/` file is edited.** The four `docs/` sentences change through
  `frame/design.md` *Rule changes* (`skills/implement/SKILL.md` *Document
  layout, two roots, three lifetimes*).

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does `tests/text/test_no_passage_is_pasted_into_a_second_file.py` stay green with `skills/implement/bootstrap.md` in its corpus? The framer's reimplementation of the module's normalisation placed the one baselined `README.md` run outside the moved lines, but it skipped the module's fence handling, so it is an approximation and not the module's answer | a measurement | Green: nothing to do. A new pair over its baseline: the pair's shared text is cited from its home rather than copied, and the `BASELINE` key `("README.md", "skills/implement/orchestration.md")` moves to the new file only where the run is the baselined one | Green; phase 2 runs the module and records its exit code | open |

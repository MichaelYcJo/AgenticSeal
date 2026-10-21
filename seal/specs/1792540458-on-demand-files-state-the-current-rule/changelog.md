### Changed

- **Text an agent or a check reads has three writing rules of its own
  (#940).** `skills/writing-style/SKILL.md` states them in one section under
  its structure rules: no symbol used as syntax, no value stated twice and no
  shape a near miss passes; one word, one meaning; and an instruction names
  who acts, when, on which file and what counts as done. Each ends with the
  `check:` line naming what reads it, both language sections link the
  section, and the skill's description names this kind of text, so a session
  writing a skill, an agent definition, a template or a frame loads it.
- **The orchestrator's half of `implement` states the current rule, once
  (#940).** `skills/implement/orchestration.md` drops the history it
  narrated, says its order in words and names the party of each act. The
  approval line's shape is stated at the step where the orchestrator spawns
  the smith: `Approved <date> by <who>, when `smith` was spawned.`, ending
  at its full stop, with anything more on a line of its own. The routing
  section holds the reasoning the CLAUDE.md block no longer carries, and
  its headings are *Orchestrator: Bootstrap*, *Orchestrator: Parity setup*,
  *Orchestrator: how the work is routed*, *Question 1* and *Question 2*.

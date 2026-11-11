### Fixed

- **The framer settles its three readiness assumptions itself, and no text it opens tells it to ask a person (#1480).** Step 5 of `agents/framer.md` sent a framer to `skills/confidence-check/SKILL.md`, which said "say which, and ask", and to `skills/feature-planner/SKILL.md`, which said "Get user confirmation before starting". The framer's definition says it asks nobody anything. Step 5 now names the three assumptions a frame may rest on: that nothing in the tree already does what the work adds, that a library's API is the one its installed version holds, or the version the work moves it to, and that a bug's cause is shown and not guessed. The framer settles each by reading the tree or by a probe, and an assumption neither settles becomes a row of `frame/questions.md`. The framer's definition grows by 227 bytes, to 15,051.

### Removed

- **The skills `/agentic:feature-planner` and `/agentic:confidence-check` (#1480).** A person who typed either command, or a session that loaded either by its description, finds no such skill after the update. No transcript on the owner's machine holds a framer opening either one. Their parts that a frame uses already stand in the frame templates and in `agents/framer.md`: scope in and out, acceptance, phases and risks in `frame/design.md` and `frame/plan.md`, and the three readiness checks in step 5. The skills row of `README.md` and `README.ko.md` no longer lists them. The three cases that read the two files go with them.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-11-11 | `agents/framer.md` step 5 settles three assumptions before a frame rests on one, a duplicate in the tree, a library's API at its installed version or at the version the work moves it to, and a bug's cause, by reading or by a probe, and routes one neither settles to a row of `frame/questions.md`. It no longer opens `skills/confidence-check/SKILL.md` or `skills/feature-planner/SKILL.md`, which are removed | Both skills told the framer to ask a person, which its definition forbids, and no framer was seen opening either | https://github.com/MichaelYcJo/AgenticSeal/issues/1480 |

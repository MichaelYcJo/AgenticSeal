# Questions for the planner: the dispatcher passes on deny and ask alone (#1381)

The ticket left these judgments open, and the tree answered each of them. Do not reopen them:

- What a group prints when its only decision is a gate's `allow`: no decision, with the reason kept as text. See `frame/design.md` *Data & interfaces* and `plan.md` *Alternatives considered*, the row on dropping the reason.
- Whether the JSON path is in scope: yes. See `frame/design.md` *Grounding*, the hooks reference row and the probe row, and `plan.md` *Alternatives considered*, the row on the issue's proposal alone.
- What the JSON path removes there: only `updatedInput` and a top-level `decision` other than `block`, so that no refusal is dropped. See `plan.md` *Alternatives considered*, the row on passing `systemMessage` alone, and `frame/design.md` *What a change to a gate must carry*.
- Whether `defer` and other decision values pass: no. See `plan.md` *Alternatives considered*, the row on passing `defer`.
- Whether the printed decision keeps the gate's spelling: no. See `plan.md` *Alternatives considered*, the row on the gate's own spelling.
- Whether the policy root is edited in this pull request: no. See `frame/design.md` *Grounding*, the row on `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does this change clear `HOOK_GRANTS_PERMISSION` in the plugin directory's validation? The validator's reading is not documented, and it runs only on a submission at the directory's portal, which no probe in this environment can reach. Its input is the `dist` commit of a published release, which does not exist until this release ships. | a measurement | Cleared: #1381's second done-when bullet is written and the issue closes. Still held: the result names what the validator read, and a new issue takes it, with #1376 as the place for command-hook readiness. | Build as framed. The owner resubmits the next release's `MichaelYcJo/AgenticSeal@dist` after this release ships and writes the result on #1381. | open |

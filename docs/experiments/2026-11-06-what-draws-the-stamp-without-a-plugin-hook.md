# What can draw the sealer's stamp after the turn's final text if the
# plugin ships no command hook?

Measured 2026-11-06 on Claude Code 2.1.319, for #1376. Transcribed on
2026-11-10, for #1492, from the owner's comment on #1376 that recorded it,
comment 6675898172 of 2026-11-06, its section *The terminal stamp*.

## Question

#1376 weighed shipping the plugin with no command hook, because the
marketplace's pre-submission check refused one. The sealer's stamp was drawn
through command hooks the plugin shipped, `Stop` among them: in colour,
after the turn's final text, without anyone asking for it, and as the exact
bytes the script wrote. Whether any other place could draw it that way is a
property of the harness at run time, so reading the plugin's code could not
settle it.

## What it established

1. **A `Stop` command hook in the person's own settings runs the way a
   plugin's does.** Its environment holds no `CLAUDE_PLUGIN_ROOT` and puts
   no plugin `bin/` on `PATH`, so its command carries an absolute path.
2. **`${CLAUDE_PLUGIN_DATA}` is kept across plugin updates, and a skill body
   receives it substituted to an absolute path.** A file written there
   survives an update.
3. **No other surface keeps all four properties of the stamp**: colour,
   after the turn's final text, drawn without being asked, and the exact
   bytes. Each surface tried lost at least one; *Results* names which.
4. **A `hooks:` block in a skill's frontmatter runs a command hook when the
   skill is invoked.** It is a command hook the plugin ships, so it does not
   answer the question.

## Method

The comment records what each surface did and not the steps that showed
it. Its account: each surface below was read and run in a scratch plugin,
on Claude Code 2.1.319, on 2026-11-06. The comment marks fact 1
and fact 4 as executed, and fact 2 as read and then executed. It gives no
mark for each surface of fact 3.

The outline that follows is not the comment's. It was written on
2026-11-10, for #1492, and nobody has run it: build a scratch plugin whose
`Stop` hook prints a coloured `systemMessage`, then try each surface in
*Results* in turn. Restore by removing the scratch plugin and any entry
written into the settings.

## Results

| # | Surface | What it did | Ruled out |
|---|---|---|---|
| 1 | A `Stop` command hook in the person's settings | Ran as a plugin's does, with no `CLAUDE_PLUGIN_ROOT` and no plugin `bin/` on `PATH` | a relative command path |
| 2 | `${CLAUDE_PLUGIN_DATA}` | Kept across updates, and substituted to an absolute path in a skill body | — |
| 3 | The orchestrator's own Bash call | Kept the colour, and landed above the final text | drawing from the session |
| 4 | A `type: prompt` hook | Returned no `systemMessage` | a prompt hook |
| 5 | `terminalSequence` | Rejected colour sequences | a terminal sequence |
| 6 | A status line, an output style, a monitor | Did not draw after the reply | each of the three |
| 7 | A `hooks:` block in a skill's frontmatter | Ran a command hook when the skill was invoked | nothing: it is a command hook the plugin ships |

## What it did not establish

- **The steps.** The scratch plugin is not in this repository, and the
  comment records results. The first paragraph of *Method* is the comment's
  account, which gives no steps, and its second is an outline written for
  this record that nobody has run.
- **Any build other than Claude Code 2.1.319.**
- **That a person saw the plugin's own hook draw a stamp.**
  `docs/checks/the-stamp.md` *What the person's screen shows is not checked*
  keeps that open.
- **The marketplace's verdicts.** The same comment records two runs of the
  pre-submission check, and this record does not transcribe them.

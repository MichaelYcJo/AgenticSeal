# SubagentStop `agent` hook probe, 2026-11-25 (orchestrator, executed)

Claude Code 2.1.332, `claude -p --model haiku --plugin-dir <plug>`, plugin `probe1615` with agent `editor` (tools Read, Write, Edit) and in `hooks/hooks.json` one `SubagentStop` entry, matcher `^probe1615:editor$`, holding a `command` hook that logs stdin and an `agent` hook.

## Probe A (q1615/): small transcript
- The hook fired for the plugin agent with the plugin-scoped matcher. stdin held `agent_type` `probe1615:editor`, `stop_hook_active` false, `agent_transcript_path` (92,570 bytes).
- The `agent` hook read the transcript, found the `Write` of "I like BANANA bread.", returned ok false; the reason reached the subagent as its next instruction and it rewrote the file to "I like APPLE bread.".
- The second stop came with `stop_hook_active` true (transcript 127,065 bytes) and the hook let it stop.
- First stop to second stop: 14.1 s (hook evaluation and the subagent's fix). Whole session 27.4 s.

## Probe B (q1615b/): a 9,058,789-byte crafter transcript (#1612's phase 2 crafter)
- The hook was told to read that file in place of the stopping agent's own. The truth by script: 9 `Edit` calls on `frame/`, `changelog.md` or `gaps.md`.
- Run 1 (told to find the calls): the hook returned ok false with a reason saying it could not search the file without grep or jq; the subagent received that as its instruction and answered with it. 11.7 s between the stops.
- Run 2 (told to use its Grep tool with a given regular expression, which matches 9 lines by `grep -c`): the hook returned ok false with a reason that handed the check to the subagent; the subagent said it could not open the file. 8.6 s between the stops.
- In neither run did the hook's reason hold the count or a path. In both, the block cost the subagent one turn on a task it could not do.

## Read
- At a small transcript the mechanism holds as the docs state: fires on a plugin agent, gets the transcript path, its ok false reason drives the subagent, `stop_hook_active` stops a loop.
- At the size this repository's crafters reach (5.5 MB and 9.1 MB in this session), two runs produced no review and blocked the subagent with an instruction it could not act on. The hook's own transcript and model were not visible to the orchestrator, so why it failed is not measured.

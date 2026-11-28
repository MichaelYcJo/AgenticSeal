# Does `disable-model-invocation: true` stop a skill from reaching an
# agent through the agent's `skills:` list?

Measured 2026-11-28 on Claude Code 2.1.332, for #1650's Q1. The
orchestrator of #1650 made the runs. This record was written from the
run's outputs and transcripts, which the phase 1 crafter of #1650 read and
counted itself.

## Question

#1650 asked whether `core` and `agent-contract` could leave the model's
skill listing by taking `disable-model-invocation: true`. Every agent this
plugin spawns receives both skills through the `skills:` list of its
definition. Claude Code's skills documentation says the flag "also
prevents the skill from being preloaded into subagents". The 2026-09-03
record measured `user-invocable: false` and stated only what the
documentation said of this flag. Whether the installed Claude Code does
what its documentation says is a property of the harness at run time, so
reading could not settle it.

## What it established

1. **`disable-model-invocation: true` stops the preload.** With the flag
   on both skills, an agent whose `skills:` list names them received
   neither body. The agent had no error and no note that a skill was
   missing, and it answered as though nothing had been withheld.
2. **The flag also takes both skills out of the session's own skill
   listing.** The session with the flag said neither skill stood in its
   listing, and the session without it said both did. This is the
   session's answer, not a count of the transcript.
3. **Without the flag, `user-invocable: false` still lets both bodies
   through whole.** The control run delivered both sentinels, each
   appended as the last line of its skill's body. This agrees with fact 1
   of the 2026-09-03 record.

## Method

Two clones of #1650's branch, `flag-off/` and `flag-on/`, each made with
`git clone --no-local` at a commit whose `skills/`, `agents/` and
`.claude-plugin/` are those of the `v0.40.1` tag. Four edits in each
clone:

- `.claude-plugin/plugin.json`'s `name` becomes `probe`, so the clone's
  skills and agents stand apart from the installed plugin.
- A definition `agents/sentinel.md` is added. Its `skills:` list holds
  `core` and `agent-contract`, its `tools:` holds `Read`, and its body asks
  the agent to answer from the text it received at startup and to use no
  tool.
- One line `SENTINEL-CORE-<token>` is appended to the body of
  `skills/core/SKILL.md`.
- One line `SENTINEL-CONTRACT-<token>` is appended to the body of
  `skills/agent-contract/SKILL.md`.

The token was `b8c05beca29b`. In `flag-on/` alone,
`disable-model-invocation: true` was added to both frontmatters, below
`user-invocable: false`.

The working directory was an empty repository made with `git init`. It
holds no `agentory/` root, so no core hook prints the core into the
session. Each clone was run from it, both runs in parallel:

```
claude -p "$P" --plugin-dir <clone> \
  --settings '{"enabledPlugins":{"agentic@agenticseal":false}}' \
  --max-budget-usd 2 --output-format json
```

`$P` was this prompt, as the session's transcript holds it:

```
Spawn the subagent probe:sentinel exactly once with this question: "Quote
every line of the text you received at startup that begins with
SENTINEL-, or answer NONE." Then report its answer verbatim. Also answer,
from your own skill listing: do probe:core and probe:agent-contract appear
in it? Answer yes or no for each.
```

The `session_id` of each run's JSON output locates the agent's
transcript, `~/.claude/projects/<working directory with each / as ->/`
`<session_id>/subagents/agent-*.jsonl`. The result is the count of lines
holding each sentinel there:

```
grep -c "SENTINEL-CORE-b8c05beca29b" <transcript>
grep -c "SENTINEL-CONTRACT-b8c05beca29b" <transcript>
```

A second count looks for a phrase of each body that no prompt holds:
`The rule a mechanism is kept against` for the core, and `Read exit codes
directly, never through a pipe` for the contract. The agent's answer is a
third reading. Nothing in the plugin's tree was edited, so nothing has to
be restored: each clone and the working directory stand in a scratch
directory.

## Results

| Run | Session | Cost (USD) | `SENTINEL-CORE` | `SENTINEL-CONTRACT` | Body phrases | Agent's answer | Listing answer |
|---|---|---|---|---|---|---|---|
| flag-off | `125e9be9-ce8c-416f-98b9-d022f6555a8e` | 0.2315 | 3 | 3 | 3 and 2 | both lines quoted | both listed |
| flag-on | `2a7a59dd-1eaa-4957-a2ad-07a50ed0d450` | 0.1869 | 0 | 0 | 0 and 0 | `NONE` | neither listed |

In the flag-off transcript, each sentinel stands in three lines. The first
is the message that delivers the skill's body at startup, whose base
directory is the `flag-off/` clone, not the installed plugin. The second is
the request sent to the model. The third is the agent's answer. The
flag-on transcript holds none of the sentinels or body phrases anywhere,
so the agent's `skills:` entries did not fall back to the installed
plugin's `core` and `agent-contract` either.

The flag-off run decides that the setup delivers the clone's preload, so
the flag-on run is not void, and it decides fact 1. In the flag-on run the
session still listed the clone's other skills under `probe:`, so the clone
loaded and only the two flagged skills were gone. Neither session's own
transcript holds the string `agentic:`, so the `--settings` override kept
the installed plugin's skills and agents out of both sessions. The flag-on
agent's transcript holds no line that names a skill it failed to load.

## What it did not establish

- Whether a later Claude Code release keeps this behaviour. The
  documentation states it, so a change would be a change to the
  documented contract.
- Whether the flag changes what a person sees in the `/` menu. The runs
  were headless and opened no menu.
- Whether the flag acts the same on a skill that a session loads on demand
  and no agent preloads. Only the two preloaded skills carried it.

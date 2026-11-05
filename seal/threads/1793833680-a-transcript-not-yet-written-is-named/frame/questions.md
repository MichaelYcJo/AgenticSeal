# Questions for the planner: 1793833680-a-transcript-not-yet-written-is-named

The judgments the issue left open that the tree or a probe answered, so nobody reopens them:

- **Does this work item take the comment's `--bare` measurement?** Yes, and it is answered: `frame/design.md` *Grounding*, rows Probe B1 and Probe B2; `frame/plan.md` *Alternatives considered* A7.
- **Does a `--bare` session write a transcript at all, #1177's Q3 option "It cannot find the transcript"?** It does: `frame/design.md` *Grounding*, row Probe B1.
- **Can the script tell a session's first input from a wrong session id?** No: `frame/plan.md` *Alternatives considered* A2.
- **Does the `--transcript PATH` reason change too?** No: `frame/design.md` *Scope*, *Out*, first item.
- **Does the policy document about `seal core` change?** No: `frame/design.md` *Rule changes*; `frame/plan.md` *Alternatives considered* A6.
- **Is the transcript written after the first exchange, or once a message is sent?** Once a message has been sent, which fits both the issue's interactive observation and the headless probe: `frame/design.md` *Grounding*, row "The same probe B2, read for when the transcript is written".

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | In an interactive session with plugin 0.32.2 installed, does `! seal core` typed as the session's first input print the new reason and exit 1, and does `seal core` pass once one message has been sent? The tree cannot answer it: it holds the script and planted transcripts, not an interactive session. No probe can run here: a subagent cannot type an interactive session's first input, and probe B2 was headless, where the first message is sent before any tool runs. The measurement: after `/agentic:update` to 0.32.2, start a new session, type `! seal core` first, then send one message and type it again. | a measurement: the owner, once, after updating to 0.32.2 | **The new reason prints, then the check passes:** nothing to do. **The first input finds a transcript:** Claude Code now writes it at session start, and the added sentence describes a case that no longer happens. A later work item takes the sentence out. **It still finds none after one message:** the transcript is written later than the issue observed, or under another directory. The reason's first sentence names the directory searched, and the added sentence is reworded to the observed moment. | The new reason prints, then the check passes. Grounds: the issue's 2026-10-30 observation under 0.25.0, and probe B2, which found the transcript within the first turn of a headless session (`frame/design.md` *Grounding*) | open |

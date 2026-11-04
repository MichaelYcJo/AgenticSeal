# Implementation Plan: 1793833680-a-transcript-not-yet-written-is-named

## Technical context

Every line coordinate and every quoted text of the tree in this plan is the tree's at 920a9584, before the build.

`skills/verify/scripts/core_check.py#find` (`:104-123`) looks for the session's transcript in two ways. It takes the path `--transcript` names, or else it globs `<config>/projects/*/<id>.jsonl`, where `<config>` is `CLAUDE_CONFIG_DIR` or `~/.claude` (`:117`) and `<id>` is `CLAUDE_CODE_SESSION_ID`. Where nothing matches, it returns `no transcript for session {session} under {projects}.` (`:122`). `main` prints that reason after `seal core: ` and returns 1 (`:263-266`). The module docstring lists the failure reasons at `:45-51`. The cases are in `tests/skills/test_core_check.py`: `Test_find::test_refuses_with_a_reason_where_no_transcript_can_be_named` at `:127-140` and `Test_main::test_refuses_with_exit_1_and_names_the_plugins_core_to_open` at `:419-445`. The reason's text is pinned at `:138` and `:432` and nowhere else (`frame/design.md` *Grounding*, the `git grep` row).

The constraint is that `find` has no fact that separates "this session has sent no message yet" from "this id names no transcript". Both look like an empty glob. So the added sentence is a condition the person recognises: they know whether `seal core` was their first input. The script does not decide which case it is in.

Failure scenario of the chosen approach, six months on: a Claude Code release starts writing the transcript at session start. The new sentence would then describe a case that no longer happens. It would still be printed only where no file exists, so it would mislead nobody into a wrong act. The person sends one message, gets the same reason, and the session id and directory in its first sentence point at the real cause. A wrong `CLAUDE_CONFIG_DIR` in the shell that runs `seal core` behaves the same way: one wasted message, then the directory named. The record that shows the sentence has gone stale is a report of `seal core` failing after a message. No check reads for it, because the cost is one re-run.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 Keep the reason's sentence and add one sentence: the transcript is written once a message has been sent, so a session whose first input was `seal core` sends one message and runs it again (Scope 1) | The sentence goes stale if Claude Code changes when it writes the transcript (*Technical context*). The cost is one wasted message, and the first sentence still names the session and the directory. | Chosen. It is the change the issue asks for. It keeps exit 1 and the one-line output, and it decides nothing the script cannot read. |
| A2 Detect the first-input case and print a different reason only there, for instance when no project directory holds any file newer than the session's start, or when the session id is unknown to every project | No such fact is read exactly. A heuristic such as file times or directory counts would sometimes print the first-input reason for a wrong id, or the plain reason for a fresh session. `skills/core/SKILL.md` *The rule a mechanism is kept against* says a reading guessed from signals is reported and never decides. | Rejected. Both cases share one empty glob. A1 names the condition and leaves the person, who knows whether this was their first input, to recognise it. |
| A3 Return a different exit code for "no transcript" | The issue says the exit stays 1, since nothing was read. `skills/implement/orchestration.md` step 1 and every caller read 1 as "failed, with the reason". A new code is a new meaning that every caller would have to learn, and no caller acts differently on it. | Rejected. |
| A4 Wait, or poll, until the transcript appears | A `!` command blocks the session's input. The transcript is written only once a message is sent, so a poll would run until it timed out and then print the same reason. | Rejected. |
| A5 Replace the structure: read what the session holds from somewhere other than the transcript, for instance a record the `SessionStart` hook writes under the git directory, used when no transcript exists | A hook's own record says what the hook printed, not what the model received. The check exists to compare `attachment.content`, what the model received, with the hook's `stdout` and with the file (`core_check.py:34-43`). Past the harness's cap of about 10,000 characters the two differ (`docs/checks/the-session-hooks.md`), and a hook-side record would pass a session that holds only a preview. It would also be a second record kept beside the transcript. | Rejected. The premise that keeps the structure is that only the transcript holds what the model received. Checked: `judge` compares `content` with `stdout` (`core_check.py:212-220`), and #1177's frame chose to read `content` for this reason (`git show 334189fd:seal/threads/1793273065-the-core-reaches-no-users-repository/frame/questions.md`, *What does `seal core` read?*). |
| A6 Also add the first-input fact to `docs/checks/the-session-hooks.md` as a `## Rule changes` `add` | The section states what the check reads and when it exits 1, and none of the reasons. Adding one reason's case would make it the only reason the policy lists. The next reason added would face the same question, and the policy would grow a second copy of the docstring's list. | Rejected. The reason's own text and the docstring (Scope 2) say it where a person reads it. `## Rule changes` holds the no-change block. |
| A7 Leave the `--bare` measurement open for an authenticated run, as #1177's Q3 framed it ("anyone with an `ANTHROPIC_API_KEY`") | An open row that a probe answered costs every later reader a re-read. `ANTHROPIC_API_KEY` is unset on this machine (executed: `test -n`), so the row would stay open. | Rejected. Probe B2 ran a real `claude --bare -p` session against a stand-in Messages API (`frame/design.md` *Grounding*). `seal core`'s output depends on the harness's environment and transcript, which were real, and not on the model's words. It printed the expected line and exited 1. An authenticated run would change nothing that gets built. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope 1, 2 and 3 | `tests/skills/test_core_check.py`, run narrow; the new assertion shown red against `find` without the added sentence, and its failing line read for that sentence (contract rule 15) | 5dee05dc |

Scope 4 needs no phase: its answer is probe B2 in `frame/design.md` *Grounding*. No phase re-runs it.

## Operational impact

None. No migration, environment variable, dependency or compatibility break. A person who types `seal core` as a session's first input sees one more sentence, and the exit code is unchanged.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-05 | The frame's line coordinates and quoted tree text, which the phase 1 crafter listed as contradicted by HEAD, are dated to 920a9584 by one sentence at the head of `frame/design.md` *Grounding* and `frame/plan.md` *Technical context*, and are not rewritten to HEAD's lines. | They state the tree the work changes: the old reason and the docstring that named it only as "no transcript" are the grounds of the change, and rewriting them to HEAD would erase them. Dating them makes each a past-state claim, as a round record's `target:` line and a Status cell's commit are. | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*; `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (the past-state trick) |

# Design: 1793833680-a-transcript-not-yet-written-is-named

## Grounding

Every line coordinate and every quoted text of the tree in this frame is the tree's at 920a9584, before the build.

| Policy clause | What it fixes for this work |
|---|---|
| `routing.md` (read, committed at 26095393) | Planning framer, Implementation crafter, Review through the review chain, Destination open the pull request, Automation yes. So nothing in this frame waits on a person, and a measurement no agent can run stays a row with a default. |
| Issue #1190 body and its one comment (executed: `gh issue view 1190 --json body,comments`, 2026-11-05) | The body asks for one change: the "no transcript" reason says a session's transcript is written after its first exchange, so a session whose first input was `seal core` sends one message and runs it again. The exit stays 1. The comment re-homes #1177's `--bare` measurement here: `seal core` should exit 1 in a session started with `--bare`, naming no core entry and `--bare`. |
| `seal/config.md` (read) | No `Record language` row, so the records are English. No `Policy root` row, so the policy root is `docs/`. |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | This work item's subject is the code, one message of one script. So it states its rule changes in `## Rule changes` for the settle and does not edit `docs/`. It changes no rule (*Rule changes* below). |
| Unsettled `## Rule changes` (executed: `awk` over every `seal/threads/*/frame/design.md` for the `file:` and `section:` lines) | Pending operations name `docs/running/the-run.md`, `docs/layout/the-record-layout.md`, `docs/running/measuring-a-run.md`, `docs/layout/one-root-by-lifetime.md` and its Korean copy, and `docs/running/the-broad-gate.md`. None names `docs/checks/the-session-hooks.md`, the one policy section about `seal core`. |
| `docs/checks/the-session-hooks.md` *The core reaches a session from the plugin's own `SessionStart` hook, once* (read, `:41-53`) | The policy says `seal core` "reads the entry back from the session's transcript and exits 1 unless the context holds it once and whole". It lists none of the check's reasons, so a reason's new clause leaves it true. |
| `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* step 1 (read, `:28-31`) | The orchestrator runs `seal core` before its first edit, after the person's first message has been exchanged, and says any failure other than "no core entry" in its next reply. The new clause does not change what the orchestrator does. |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | A script decides only on facts it reads exactly. `find` cannot tell a session that has sent no message from a session id that names no transcript, because in both cases no file matches. So the reason states the first-input case as a condition the person recognises. It does not guess which case it is in (`frame/plan.md` A2). |
| `agent-contract` rules 14 and 15 (read); the 2026-11-04 process row widening rule 15 (read: the `### Process changes` table of `seal/threads/1793718241-a-fix-pass-applied-paste-ready-text-as-given/changelog.md`) | A change to a message a person reads is documented and pinned in the same commit, and the pinning case is shown red with only the new clause removed. The latest GitHub Release, v0.32.1, carries no `### Process changes` table (executed: `gh release view --json body`). |
| `skills/verify/scripts/core_check.py#find` (read, `:104-123`) and `#main` (read, `:263-266`) | `find` returns `(None, "no transcript for session {session} under {projects}.")` where no `<config>/projects/*/<id>.jsonl` exists, and `main` prints it after `seal core: ` and returns 1. The `--transcript PATH` branch returns its own reason, `no transcript at {given}.` (`:110`). |
| `core_check.py` module docstring *It fails, exit 1* (read, `:45-51`) | The docstring lists each failure reason, and names this one only as "no transcript". It is where a person changing the script reads the reasons, so it states the new clause too. |
| Every pin of the reason's text (executed: `git grep -n -i 'no transcript'` over the tree outside `seal/threads/`) | `core_check.py:122` is the one place that writes the sentence. `tests/skills/test_core_check.py:138` asserts that the reason names `session abc` and the directory, and `:432` asserts `"no transcript for session abc"` in `main`'s output. No document, README row or other test quotes it. The list comes from the tree, so it is complete, not a sample. |
| #1177's Q3 (read: `git show 334189fd:seal/threads/1793273065-the-core-reaches-no-users-repository/frame/questions.md`) | Q3 asked whether `seal core` fails under `--bare`. Its answerer was "anyone with an `ANTHROPIC_API_KEY`". Its default was "It exits 1". One of its options was "It cannot find the transcript: a bare session writes none". The two probes below answer it without a key. |
| Probe B1 (executed: `CLAUDE_CONFIG_DIR=<scratch>/cfg claude --bare -p "print ok"` with `ANTHROPIC_API_KEY` unset, Claude Code 2.1.318) | It exits 1 and prints `Not logged in · Please run /login`. That is #1177's Q3 obstacle, still present on this machine. The run still wrote `<scratch>/cfg/projects/<dir>/<id>.jsonl` holding the `user` entry. So a `--bare` session does write a transcript, and Q3's "writes none" option is ruled out. |
| Probe B2 (executed: a stand-in Messages API on `127.0.0.1` that answers the first request with one `Bash` tool call and the next with `done`, then `CLAUDE_CONFIG_DIR=<scratch>/cfg ANTHROPIC_API_KEY=stub-key ANTHROPIC_BASE_URL=http://127.0.0.1:48713 claude --bare -p --plugin-dir <clone> --allowedTools Bash --output-format json "run seal core"`, from a `git clone --no-local` of this branch at 26095393) | The Bash call ran `python3 <clone>/skills/verify/scripts/core_check.py; echo "exit=$?"; echo "SIMPLE=$CLAUDE_CODE_SIMPLE"`, and the transcript's `tool_result` reads: `seal core: no core entry in this session's context: the session runs under --bare (CLAUDE_CODE_SIMPLE=1), which skips plugin hooks; open <clone>/skills/core/SKILL.md once.`, then `exit=1`, then `SIMPLE=1`. The transcript holds no `SessionStart` `hook_success` attachment. The harness, its environment and its transcript are Claude Code's own; only the model's two replies are canned. `seal core`'s output depends on the environment and the transcript, not on what the model says. So this is the comment's measurement, and it matches the expected answer. |
| The same probe B2, read for when the transcript is written (executed) | The transcript existed while the session's first turn was still running: `find` located it from inside that turn's Bash call. In headless mode the file is written when the first message is sent. The issue's interactive observation is that a `!` command typed before any message finds no file, and that the file is there after one message. Both observations fit one sentence: the transcript is written once a message has been sent. The interactive half is the issue author's observation (read), and no subagent can type an interactive session's first input (`frame/questions.md` Q1). |
| `seal/follow-up.md` (read) | No row names `core_check.py` or `seal core`, so this work is no row's prerequisite. |
| Earlier work items on `core_check.py` (executed: `git log -- skills/verify/scripts/core_check.py tests/skills/test_core_check.py`) | 334189fd (#1186, for #1177) wrote the script. c8f235df (#1358) changed only its `__main__` stream loop. Neither changed `find`, and no earlier round argued its reason text. |
| Release 0.32.2's other work items: #1184 (`skills/update/SKILL.md`, `CLAUDE_CONFIG_DIR`) and #1185 (`skills/verify/scripts/payload_meter.py#imports_of`) (read: the spawn prompt, quoting the milestone description) | This work touches neither file. The version move to 0.32.2 is #1184's. |

## Scope

In:

1. `skills/verify/scripts/core_check.py#find`: the reason returned where `CLAUDE_CODE_SESSION_ID` names no transcript under `<config>/projects` keeps its present sentence, which names the session id and the directory searched. A second sentence follows it. That sentence says that Claude Code writes a session's transcript once a message has been sent in it, so where `seal core` was the session's first input, the person sends one message and runs `seal core` again. The exit stays 1. One wording that holds both parts: `no transcript for session {session} under {projects}. Claude Code writes a session's transcript once a message has been sent in it, so where seal core was this session's first input, send one message and run it again.` The crafter may word it otherwise if both parts stay.
2. The module docstring's *It fails, exit 1* list (`core_check.py:45-51`) names this reason with what it now adds, in the same commit as item 1.
3. `tests/skills/test_core_check.py`: `Test_find::test_refuses_with_a_reason_where_no_transcript_can_be_named` asserts the new sentence's two parts, the transcript written once a message has been sent and the instruction to send one and run again. The case is shown red against the reason without the new sentence (contract rule 15). The existing assertions on the session id, the directory and the `--transcript` reason stay.
4. The comment's `--bare` measurement is answered by probe B2 in *Grounding*, and no code changes for it. The changelog fragment and the pull request body carry its answer from that row.

Out:

- The `--transcript PATH` reason, `no transcript at {given}.`. A path the person named is not a file the harness has yet to write, so the first-input case does not apply to it.
- Telling a session that has sent no message apart from a session id that names no transcript. No fact the script can read separates the two (`frame/plan.md` A2).
- `docs/checks/the-session-hooks.md`. It lists none of the reasons, and the new clause leaves its one sentence about `seal core` true (`frame/plan.md` A6).
- `skills/implement/orchestration.md` step 1. The orchestrator runs `seal core` after the first message, so it never meets the case.
- The README rows for `seal core` (`README.md:217`, `:330`; `README.ko.md:221`, `:334`). They say what the command answers, and none of the reasons.
- The files of #1184 and #1185, and the version move.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A first input | Given `CLAUDE_CODE_SESSION_ID=abc` and a config directory whose `projects/` holds no `abc.jsonl`, when `seal core` runs, then it exits 1. It prints one line naming session `abc` and the `projects` directory. The line says the transcript is written once a message has been sent, and says to send one message and run it again. | `tests/skills/test_core_check.py` `Test_find` (Scope 3), seen red without the new sentence; `Test_main::test_refuses_with_exit_1_and_names_the_plugins_core_to_open` keeps exit 1 and the `no transcript for session abc` prefix |
| S2 A named path | Given `--transcript` names a file that is not there, when `seal core` runs, then the reason is exactly `no transcript at <path>.` and the exit is 1, as before. | the existing assertion at `tests/skills/test_core_check.py:140` stays unchanged |
| S3 A transcript is found | Given a transcript exists for the session, when `seal core` runs, then every outcome is as before. | the rest of `tests/skills/test_core_check.py`, unchanged |
| S4 A `--bare` session | Given a session started with `claude --bare`, when its Bash tool runs `core_check.py`, then it exits 1 and names no core entry and `--bare`. | probe B2 (executed at framing, *Grounding*); the planted-transcript case in `Test_main` holds the same reading in the tree |
| S5 An interactive first input, after the release | Given plugin 0.32.2 installed, when `! seal core` is the first input of a new interactive session, then the new reason prints, and after one message `seal core` passes. | `frame/questions.md` Q1: the owner, once, after the update |

## Data & interfaces

One string changes: the second return of `core_check.py#find` for the session lookup (`:121-122`). Its first sentence is kept word for word. `find`'s signature, its `(path, reason)` return shape, `main`'s exit codes and the one-line output are unchanged.

## Rule changes

- nothing
  why: The policy's one sentence about `seal core` (`docs/checks/the-session-hooks.md` *The core reaches a session from the plugin's own `SessionStart` hook, once*) names what the check reads and when it exits 1, and none of its reasons. A reason's added sentence leaves it true. The reasons are listed in the script's docstring, which Scope 2 updates.

## Removes

- nothing
  why: The work rewrites one reason's text in place and adds no mechanism: no gate, check, hook, mark or rule. The old sentence is kept as the reason's first sentence, so no copy of it is left to remove. The test pin is extended, and no pin goes.

Framed 2026-11-05 by framer, before the build.

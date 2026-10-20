# 1792533444-automation-refuses-mid-run-questions — review round 2

target: 067a37a8, fixes ec757244..067a37a8

This is a verifying round. It read the fix diff ec757244..067a37a8 in a
`git clone --no-local` checked out at 067a37a8. Carried from round 1: where
the press reader keeps the last answer per clone
(`hooks/worktree_consent.py`, the loop that sets `pressed`), and that the
commit gate's parity arm fires on a declared branch (`hooks/gate.py:162-168`).
Both were reopened at their lines, not re-derived. Every verdict below is
this round's own.

## Findings

### 1. The exemption's new bound fails open: with no readable transcript, a question dressed in the routing labels still passes on every call

severity: should
location: `hooks/question-gate.py:97-104`, `hooks/worktree_consent.py:330-332`, `hooks/worktree_consent.py:391-392`, `tests/test_an_automation_run_puts_no_question.py:263`
evidence: executed `bin/test tests/test_tmp_round2_probe.py -q -s -n0`
verdict: open
reopens: round-1#1

Round 1's finding 1 is closed `fixed 1ccd15cf`. The close holds wherever the
session's transcript can be read. Its third shape, a framer question dressed
in question 1's labels, is still standing wherever the transcript cannot be
read. `last_routing_answer` returns None for "no answer yet". It returns the
same None for no session id, a path that names no file, a clone it cannot
resolve and a read error (`hooks/worktree_consent.py:330-332`,
`hooks/worktree_consent.py:391-392`). The gate grants the exemption on that
None. The probe ran on a branch declared `yes`:

- No `session_id`: the dressed question was silent, twice.
- A transcript path that names no file: silent.
- A readable transcript holding the routing answer from this clone: deny.
  This is the close holding.
- The same answered transcript made unreadable: silent. A session that has
  already answered goes back to passing the dressed question.

The gate says "Failure direction: it blocks more", and this reading allows
more. Refusing here loses nothing. The exemption exists so the press readers
find the press, and those readers read the same transcript. Where it cannot
be read they find no press anyway, so a routing question let through serves
no gate. In the normal flow the harness passes a transcript that exists, so
this is an edge. But the fix is one condition, and it removes a pass that has
no bound.

```python
    session = event.get("session_id")
    transcript = worktree_consent.transcript_for(
        session, event.get("transcript_path") or ""
    )
    # Precondition: a transcript the press readers can open. Where none can,
    # no gate finds a press, so the routing question has nothing to record.
    if (
        routing_question_alone(event.get("tool_input"))
        and os.path.isfile(transcript)
        and os.access(transcript, os.R_OK)
        and worktree_consent.last_routing_answer(top, session, transcript) is None
    ):
        return
```

The cases belong beside
`test_the_routing_question_goes_through_only_until_it_is_answered`. With no
`session_id`, the routing question put alone is `deny`. With a
`transcript_path` that names no file, it is `deny` too. The module's
`payload` currently names a path no case writes, so the existing silent case
for the routing question put alone writes an empty transcript first.

answer:

### 2. plan.md's summary still describes the exemption as unbounded

severity: should
location: `seal/specs/1792533444-automation-refuses-mid-run-questions/plan.md:14-16`
evidence: read `seal/specs/1792533444-automation-refuses-mid-run-questions/plan.md:11-19`
verdict: open

The framer's amendment 067a37a8 rewrote `spec.md` and `questions.md` to say
the routing question passes only until this session has answered it. The
plan's summary still reads "the gate denies every call except the routing
question put alone". That is the fact the amendment replaced. The plan is
the Design Gate's artifact, and the sealer reads every party against the
tree. Two frame documents now give two exemptions. Contract §19 asks for the
sentence to be rewritten in place.

```
gate denies every call except the routing question put alone before this
session has answered it from this clone, and its reason
```

answer:

## Confirmations

confirms: round-1#2
The reason names the work item's directory once, as "`routing.md` in
`<dir>`", and then "`questions.md` in the same directory"
(`hooks/question-gate.py:58-70`). `test_the_refusal_says_where_the_default_goes`
counts the directory once (`tests/test_an_automation_run_puts_no_question.py:123`),
and the fail-open case pins the absolute directory. The rewrite also replaces
"so nobody is at the keyboard to answer it" with "so this run does not stop
to ask". That is the promise itself, and it is true under `per axis` with
box 1 checked, which answers round 1's *Not judged* row. This was read.

confirms: round-1#3
The limit and its way on are now stated where they survive. They are in the
rule's `to:` text (`seal/specs/1792533444-automation-refuses-mid-run-questions/spec.md:221-225`),
the gate's docstring (`hooks/question-gate.py:27-30`), both README rows and
the reason itself. A case pins the reason's sentence: "A question that states
no default, such as another gate's choice, is not yours to answer: take none
of its ways on and hand that stop back at the end of the run." This matches
the commit gate's own reason under `automation` (`hooks/gate.py:279-288`).
This was read.

confirms: none
`last_routing_answer` keeps `automation_answered`'s meaning for every
existing caller. `automation_answered` now returns
`last_routing_answer(...) is True` (`hooks/worktree_consent.py:282-285`). Each
failure path that returned False now returns None, which `is True` reads as
False. The callers are `hooks/worktree-guard.py:2617`,
`hooks/commit-review-gate.py:857`, `hooks/commitgate.py:100` and
`hooks/worktree_consent.py:412`, and each reads only a truth value. The two
press-reader modules are unedited in the fix diff. This was read, using
`git grep` for both names.

confirms: none
The transcript is not read on every call. `routing_question_alone` comes
first in an `and` (`hooks/question-gate.py:97-104`), so the scan runs only
for a call in question 1's shape on a branch declared `yes`. The scan's
measured cost stands in its docstring: 0.09 s on a 17.3 MB transcript. This
was read.

confirms: none
A resumed session whose transcript is a new file behaves as the frame says.
The new file holds no routing answer from this clone, so question 1 put alone
passes once. After the answer, the probe's readable case came back `deny`,
and the module's case pins both an `automation` and a `per axis` answer. An
answer to another question leaves the exemption open (8885929b). This was
executed by the probe above, and the module's case was read.

confirms: none
The frame amendment's `spec.md` describes the build. These match the code:
scope item 3 (`spec.md:38-41`), the exemption paragraph in *Data &
interfaces*, S8, and the rule's `to:` text. That code is
`routing_question_alone` with `multiSelect is False` and a string text, plus
`last_routing_answer(...) is None`. `questions.md` matches too. The one gap
is `plan.md`, finding 2. Neither frame document weighs an unreadable
transcript, finding 1. This was read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Any routing answer from this clone in the session spends the exemption, including one given for another work item. If a session answered `per axis` for item A and later resumes item B on a branch declared `yes`, it cannot put question 1 again, and the press readers keep reading A's `per axis`. This is outside the one-issue flow, so it may want a limit sentence rather than a mechanism | `hooks/question-gate.py:97-104` | the orchestrator, for the owner's limits direction |
| Two `AskUserQuestion` calls in one assistant message both reach the gate before either result is in the transcript, so both pass while no answer is recorded. Whether the harness runs them at once was not measured | `hooks/question-gate.py:97-104` | the orchestrator, beside the `questions.md` Q1 measurement |
| The full suite, the lint and the typecheck at 067a37a8, labelled `unverified` | CI run 39510899298; `bin/broad-gate` | the orchestrator: the relay of run 39510899298, then its broad run |
| Whether the harness runs the hook and honours its deny | `seal/specs/1792533444-automation-refuses-mid-run-questions/questions.md` Q1 | the orchestrator, by the measurement after install |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_tmp_round2_probe.py -q -s -n0` | Branch declared `yes`, with the framer question dressed in question 1's labels each time. No `session_id`: silent, then silent again. A `transcript_path` that names no file: silent. A readable transcript holding the routing answer from this clone: deny. The same path replaced by a directory, so the transcript cannot be read: silent. The file was deleted |

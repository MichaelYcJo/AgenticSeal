# 1792533444-automation-refuses-mid-run-questions — review round 1

target: ec757244 against release/v0.22.3

No earlier round exists, so nothing was carried: every coordinate below was
opened in this round, in a `git clone --no-local` checked out at ec757244.

## Findings

### 1. The routing-question exemption passes shapes the press reader does not read as question 1, and such a call takes the press back

severity: should
location: `hooks/question-gate.py:61-67`, `hooks/worktree_consent.py:168-183`, `tests/test_an_automation_run_puts_no_question.py:206-217`
evidence: executed `bin/test tests/test_tmp_question_gate_probe.py -q -s -n0`
verdict: fixed 1ccd15cf

The exemption exists for one reason (`spec.md` *Scope*, `questions.md`
"The routing question put alone passes"): a resumed run must put question 1
again so the press readers find the press. The gate tests only the option
labels (`is_routing_question`). It reads neither `multiSelect` nor the
question text, both of which `_routing_preset` requires before it counts a
press (`hooks/worktree_consent.py:234`, and the `text` check below it). On a
branch declared `Automation` `yes`, the probe found:

- A routing question with `multiSelect: true` is silent. `_routing_preset`
  reads no press from it, and `_routing_answer` returns False. The press
  reader keeps the last answer from the clone
  (`hooks/worktree_consent.py:370-380`), so whatever the person presses, an
  earlier `automation` press is taken back. After that, the worktree guard
  and the commit gate go back to asking the person. One call that passes this
  gate is a stop, and then it causes more stops.
- A routing question with no `question` text is silent, and the press reader
  skips it in the same way.
- A framer question dressed in the three labels is silent. The probe used the
  question "Which default should the hook print?" with the options
  `automation - keep the short default`, `per axis - switch to the long
  default` and `no work item - print nothing`. `_routing_preset` reads its
  first option as the `automation` press.

The first two are near misses of question 1, which the owner's direction
rules out. The fix closes them by requiring the press reader's own
conditions. The third comes from the free text the predicate never reads:
the question, the header, the descriptions and whatever follows a label's
decoration. That domain is unbounded. Requiring the press reader's
conditions narrows the finding but does not close it. Two things would
close it. One is to grant the exemption only while this clone holds no
routing answer in this session's transcript, which is the resume the
exemption is for. The other is a limit sentence in the rule. The frame
weighed "a call that contains the routing question" (`plan.md`,
*Alternatives*), but not a question that only looks like it.

```python
def routing_question_alone(tool_input):
    """One question, in the shape the press reader counts as question 1: the
    routing labels, single-select, with its text a string."""
    questions = tool_input.get("questions") if isinstance(tool_input, dict) else None
    if not isinstance(questions, list) or len(questions) != 1:
        return False
    question = questions[0]
    return (
        worktree_consent.is_routing_question(question)
        and question.get("multiSelect") is False
        and isinstance(question.get("question"), str)
    )
```

```python
    for changed in (
        {**ROUTING_QUESTION, "options": options[:2]},
        {**ROUTING_QUESTION, "options": [*options, {"label": "automation", "description": "Again."}]},
        {**ROUTING_QUESTION, "options": [*options, {"label": "later", "description": "A fourth."}]},
        {**ROUTING_QUESTION, "multiSelect": True},
        {k: v for k, v in ROUTING_QUESTION.items() if k != "question"},
    ):
        assert decision_of(run(repo, questions=(changed,))) == "deny", changed
```

If the free-text half stays a limit, it goes into the rule's `to:` text in
`spec.md` `## Rule changes`, beside the two limits already there:

```
    held, and neither is a question asked as plain text, nor one dressed in
    the routing question's three options.
```

answer: Both halves are closed in code, so no limit sentence is needed. `routing_question_alone` now requires the press reader's own conditions: one question, its labels, `multiSelect` False and a string text. The near-miss case adds the multi-select, the absent `multiSelect` and the missing text. For the free-text shape, the exemption is granted only while `worktree_consent.last_routing_answer` holds no answer to the routing question from this clone in this session's transcript. That reader now carries the body `automation_answered` had, and `automation_answered` reads its True. Once any answer is recorded, every question is refused under `yes`, the routing question and the dressed framer question included. That is the resume the exemption exists for, and it closes the open set without listing spellings. `test_the_routing_question_goes_through_only_until_it_is_answered` pins an exempt first call, an answer to another question that leaves it exempt (8885929b), and both shapes refused after an `automation` and after a `per axis` answer. Each new condition was mutated red; the two press-reader modules pass unedited.

### 2. The refusal prints the work item's directory twice

severity: should
location: `hooks/question-gate.py:48-58`, `tests/test_an_automation_run_puts_no_question.py:99-112`, `tests/test_gates_do_not_fail_open.py:252`
evidence: executed `bin/test tests/test_tmp_question_gate_probe.py -q -s -n0`
verdict: fixed 1ccd15cf

The owner's direction for this work is binding: no value stated twice, and
compact. The reason prints `<item>/routing.md` and then `<item>/questions.md`,
so the directory appears twice in one message. The cost grows with the path.
From a linked worktree in local mode, the probe printed
`../lrepo/.git/seal/specs/1787708604-a-work-item/` both times. Naming the
directory once, then the two file names, carries the same information.

```python
def reason(top, item):
    return (
        f"SpecSeal refused this question. The `{routing.FILENAME}` in "
        f"`{shown(item, top)}` answers `{routing.AUTOMATION}` with "
        f"`{routing.AUTOMATION_YES}`, so nobody is at the keyboard to answer it. "
        "Build on the default the question states, write that default as a row "
        f"of `{QUESTIONS}` beside it, and name it in the pull request body, where "
        "the owner can overturn it. Asking again meets the same refusal. The "
        "routing question put alone goes through."
    )
```

The two cases that pin the paths whole change with it. The first pins
`` f"`{item}`" `` together with `` f"`{routing.FILENAME}`" `` and
`` f"`{QUESTIONS}`" `` in `test_the_refusal_says_where_the_default_goes`. The
second pins `` f"`{item}`" `` in the fail-open case.

answer: The reason names the directory once, as `` `routing.md` in `<dir>` ``, and `` `questions.md` in the same directory ``. `test_the_refusal_says_where_the_default_goes` pins the directory in backticks, counts it once, and pins both file names; the fail-open case pins the absolute directory. A mutation that printed the joined path again was red. The rewrite also replaces "so nobody is at the keyboard to answer it" with "so this run does not stop to ask", which is the promise itself and true under `per axis` with box 1 checked (this round's *Not judged* row).

### 3. The limit for gates that tell the model to ask is stated only in spec.md, and "build on the default" points the model at choices reserved for the person

severity: should
location: `seal/specs/1792533444-automation-refuses-mid-run-questions/spec.md:186-208`, `hooks/question-gate.py:1-24`
evidence: executed `git grep -n -i "question-gate" -- . ':!seal/specs'`, `sed -n 186,208p seal/specs/1792533444-automation-refuses-mid-run-questions/spec.md`
verdict: fixed 1ccd15cf

`spec.md` *Out* (lines 91-95) covers `review-skill-gate.py`, `mode-gate.py`,
the commit gate's first deny and the worktree guard's choice sites. It says
their instruction to ask meets this refusal, that the session builds on a
default, and that "This is a stated limit". Searching outside `seal/specs/`
finds no statement of it. The rule text this item adds (`spec.md:186-208`)
names two limits, another checkout and plain text, but not this one. The
gate's docstring and both README rows leave it out too. `settle` removes
`spec.md` after the release, and then the limit has no home.

The limit also carries more than the frame weighed. That instruction reaches
a branch declared `yes` wherever no press is in this session's transcript:
`per axis` with box 1 checked, or a resumed run before question 1 is put
again. Each case below pairs another gate's "Do not choose for the user" with
this gate's "Build on the default the question states":

- **The commit gate's parity arm.** It fires on a declared branch
  (`hooks/gate.py:162-168`) and offers the waiver as an option. Under
  `automation`, the commit gate's own reason withholds that waiver from a
  work item's commit. It says to hand the commit back instead
  (`hooks/gate.py:279-288`, `docs/commit-review-gate-spec.md:67-83`).
- **The mode gate.** Its cheapest option, `seal mode`
  (`hooks/mode-gate.py:224-250`), writes a row that records a person was
  asked (`skills/implement/orchestration.md:358-361`).

The search found nothing else. The rule text was read for the limit and
does not carry it. The other coordinates were read: `spec.md:91-95`,
`hooks/gate.py:320-333` (the deny that says to ask), and the lines named
above.

Questions like these state no default, so the reason leaves the model to
pick. Its pick is a waiver or a record that only the person may give.

```
    held, and neither is a question asked as plain text. A gate whose own
    reason says to ask with the question tool meets this refusal too, and
    its question states no default: the session takes none of the ways on
    that question offers, and hands the stop back at the end of the run, as
    the commit gate's reason under `automation` says.
```

answer: The record's sentence now stands in the gate's docstring, and both README rows describe it. The refusal carries the instruction where the model acts on it: "A question that states no default, such as another gate's choice, is not yours to answer: take none of its ways on and hand that stop back at the end of the run." A case pins that sentence, and a mutation deleting it was red. The changelog fragment says it too. The `to:` text of `spec.md` `## Rule changes` is the framer's, so the sentence is named for the framer in this pass's hand-back, as is the exemption's new bound.

## Confirmations

confirms: none
The branch and root resolve as the commit gate's reading resolves them. The
gate calls `routing.declared(cwd, optin.repo_root(cwd))`
(`hooks/question-gate.py:79-81`), which is the same call as
`hooks/gate.py:155-158`. The probe executed a subdirectory `cwd`, which was
denied, and a linked worktree in local mode, which was denied. The module's
own cases cover the linked worktree in shared mode, the detached HEAD and
local mode.

confirms: none
The smith's divergence row holds. `is_routing_question`
(`hooks/worktree_consent.py:180-183`) keeps the sorted comparison, so a
doubled label is refused, and `test_a_near_miss_of_the_routing_labels_is_refused`
pins it. One copy of the label comparison remains, and both press readers
call it (`hooks/worktree_consent.py:234`, `hooks/worktree_consent.py:265`).
This was read.

confirms: none
The claim that no `cwd` guard is needed holds. `optin.repo_root` answers ""
for a missing or non-directory `cwd` (`hooks/optin.py:57-58`).
`routing.for_branch` answers None for an empty root (`hooks/routing.py:357-358`),
so `current_branch`'s fallback to "." is never consulted. This was read.

confirms: none
S13 holds. Neither `tests/test_the_guard_asks_once_per_session.py` nor
`tests/test_an_automation_run_meets_no_commit_prompt.py` changed against the
base. This was executed with `git diff --stat ebbbd2f0 ec757244` on both.

confirms: none
The `## Removes` sentences are gone. Searching for each of the five phrases
outside `seal/specs/` finds only the S14 case that pins its absence. This was
executed with `git grep -F`. Leaving `docs/the-review-record.md` untouched
matches the policy that `settle --apply` applies `## Rule changes` after the
release (`skills/implement/SKILL.md:75`).

confirms: none
`questions.md` Q1, judged only on the payload shape. The keys the cases
assume are the keys the frame recorded: `questions`, each with `question`,
`header`, `options` (`label`, `description`) and `multiSelect`. A keys-only
`python3 -I` scan of this machine's transcripts found 250 `AskUserQuestion`
`tool_use` inputs. 247 had that shape, and some options also carried a
`preview` key the gate does not read. 3 carried `__unparsedToolInput` alone,
which the gate refuses under `yes` as an unreadable call. That matches the
frame's "an unreadable question is refused". The scan reads transcript
inputs, not the PreToolUse payload, which is still the measurement Q1 names.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the harness runs the hook for `AskUserQuestion`, hands it the same `tool_input`, and honours its deny | `seal/specs/1792533444-automation-refuses-mid-run-questions/questions.md` Q1 | the orchestrator, by the measurement Q1 names after a release carrying the gate is installed |
| The full suite, the repository-wide lint and the typecheck at ec757244, labelled `unverified` | `bin/broad-gate`; CI run 39508418498 | the orchestrator: its broad run after the rounds settle, and the relay of run 39508418498 |
| "so nobody is at the keyboard to answer it" is something the gate cannot know under `per axis` with box 1 checked, where the promise is only that nothing stops to ask | `hooks/question-gate.py:53-54` | the orchestrator, as the owner's wording call |
| An attended session on a branch still declared `yes` after its run has ended, for example a later session answering pull request comments, has every question refused for the work item's life, and the reason names no way out such as editing the row to `no`. `plan.md` *Operational impact* accepts the first half | `hooks/question-gate.py:48-58` | the orchestrator, for the owner |
| Behaviour on Linux and Windows. The gate does no process inspection and only makes `git rev-parse` calls (read), but only macOS ran | `hooks/question-gate.py:70-81` | CI's platform legs |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_tmp_question_gate_probe.py -q -s -n0` (run twice: the first run, under xdist, swallowed the printed result) | Branch declared `yes`. A routing question with `multiSelect` true: silent. A routing question with no `question` text: silent. A framer question in the three routing labels: silent. A subdirectory `cwd`: deny. A linked worktree in local mode: deny, with both paths printed as `../lrepo/.git/seal/specs/1787708604-a-work-item/...`. `_routing_preset` on the multiSelect shape answered with the preset label: False. `_routing_answer` on the same: False. `_routing_preset` on the dressed framer question answered with its first option: True. An unborn-branch case was inconclusive, because the fixture's branch row could not name an unborn branch, and it is not used. The file was deleted |
| `python3 -I test_tmp_shape_scan.py` over the transcripts on this machine, keys only | 250 `AskUserQuestion` inputs. 247 had `questions` with `question`, `header`, `options` and `multiSelect`, with options `label` and `description` and sometimes `preview`. 3 had `__unparsedToolInput`. The file was deleted |

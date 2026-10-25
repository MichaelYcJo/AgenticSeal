# Review round 2: 1792926874-the-records-carry-no-comment-and-the-readers-drop-it

target: 0c532fe8, fixes b8a3697d..0c532fe8

## Findings

### 1. The rewritten `fence_spans` docstring says `rule_changes.py#parse` walks fences only through `liveness`, and `parse` also walks them through `fence_spans`

severity: should
location: `skills/verify/scripts/unverified_check.py:238-243`, `skills/verify/scripts/unverified_check.py:573-575`
evidence: read `skills/verify/scripts/unverified_check.py:238-243`, `skills/settle/scripts/rule_changes.py:115`, `skills/verify/scripts/unverified_check.py:289`, `skills/code-review/scripts/chain_check.py:1162`, `skills/verify/scripts/unverified_check.py:334-346`, `skills/verify/scripts/unverified_check.py:368`, `skills/verify/scripts/unverified_check.py:386-387`, `skills/verify/scripts/unverified_check.py:573-575`
verdict: open
regression: round-1#2

The unit is the docstring of `unverified_check.py#fence_spans`, which `32ff54c4` rewrote. `plan.md` *Phases* row 1 and `spec.md` *Data & interfaces* ask for the docstrings that describe the comment state to be rewritten in place, `#fence_spans` among them. The fix pasted round 1's own suggested text, and the defect came from that text. Round 1 read `rule_changes.py:106-115` for the code-span state of `parse`, and did not check the `blank_fences` call on line 115 against the split its own text draws.

The docstring splits the readers in two. A reader with no comment or code-span state of its own takes `fence_spans`. A reader with either state walks with `fence_opener` and `fence_closes` directly, and the docstring names `parse` in that second group, through `liveness`. But `rule_changes.py:115` computes `commented = set(r.comment_lines(r.blank_fences(lines)))`. `blank_fences` walks `fence_spans` (`unverified_check.py:289`). So `parse` takes both walks: `liveness` for its spans and fences, and `fence_spans` for the lines its comment-line refusal reads. The first sentence also says `chain_check.py` takes the walk through `readable`. `chain_check.py#unclosed` instead asks `fence_spans` directly, on `gfm_lines` (`chain_check.py:1162`).

This matters for the next change to `fence_spans`, for example to how it treats a block that never closes. An agent making it reads this docstring to find who is affected. The docstring sends that agent to `readable`, `check_text` and `chain_check.py`, and not to the refusal in `parse`.

Nothing misreads today. `parse` calls `liveness` with `comments=False` and `spans_cross_lines=False`. Under those arguments `comment` is never set (`:368`) and `span` is never set (`:386-387`). So the fence state of `liveness` is the same `fence_opener` and `fence_closes` walk that `fence_spans` makes (`:334-346`). The two differ only on the opener line, which `liveness` calls live and `blank_fences` blanks. The defect is in the sentence, not the behaviour.

The `live_lines` docstring makes the same omission at `:573-575`. It says `blank_fences` and `readable` serve "the readers of a record — `check_text` and `chain_check.py`", and does not name `parse`'s line 115. That sentence came from phase 1, not from the fix. It is named here so the fix pass covers the whole class (contract rule 12). The fix pass also searches for any other sentence that names who walks `fence_spans` or `blank_fences`.

The fix rewrites lines 238-243 of `fence_spans`' docstring:

```python
    The walk for a reader whose fences depend on no comment or code-span
    state: `readable`, and through it `check_text` and `chain_check.py`;
    `chain_check.py#unclosed`, on the raw lines; and `rule_changes.py#parse`,
    through `blank_fences`, for the lines its comment-line refusal reads
    (#1012). `liveness` keeps both states, so it walks with `fence_opener`
    and `fence_closes` directly, because whether a line can open a fence at
    all depends on the state it began in. `parse` also reads `liveness`, with
    no comment state and with spans kept to their line. Under those two
    arguments `liveness` finds the same fences as this walk, so the two
    readings `parse` takes agree on every fence.
```

and lines 573-575 of `live_lines`' docstring:

```python
    **What this may not touch.** `blank_fences` and `readable` serve the
    readers of a record — `check_text`, `chain_check.py`, and
    `rule_changes.py#parse` for its comment-line refusal — which keep no
    comment state (#1012). Neither is on this path. What this scan and
```

answer:

## Confirmations

confirms: round-1#1
The fix holds. `32ff54c4` pins the message's words as a literal string in `Test_check_text::test_refuses_a_comment_line_at_its_line` (`tests/test_unverified_check.py:1383-1387`). `check_text` returns `COMMENT_LINE` itself (`skills/verify/scripts/unverified_check.py:890`), so any change to the constant's words breaks the equality. Round 1's evidence was re-run: `git grep -n -F 'delete the comment' 0c532fe8 -- .` now finds the case at `tests/test_unverified_check.py:1385` beside the constant at `skills/verify/scripts/unverified_check.py:167` (executed). The smith claimed two message mutants, each red, with only the pinning case failing. Two `mutation-check` mutants were run over the `comment_line` cases of the three test modules. Mutant one rewords `delete the comment` to `remove the comment`, and mutant two removes the message's first clause. Both were red (executed). With the pinning case deselected, the first mutant survived and 9 cases passed. So only the pinning case reads the words, and the others compare against the constant (executed). That matches the case's new docstring: the words are pinned once, and every other case pins that each reader says the one message. `chain_check.py:1177` and `rule_changes.py:128` both return the shared reader's `COMMENT_LINE`, so no reader spells a copy of its own (executed: `git grep -n COMMENT_LINE 0c532fe8`).

confirms: round-1#2
The defect round 1 named is gone. The docstring no longer says that every reader of a record lacks a code-span state, and it now names `rule_changes.py#parse` as a reader that keeps one (`skills/verify/scripts/unverified_check.py:238-243`). `comment_lines`' docstring now says a mid-line refusal would need a code-span state "in `readable` and every reader of a record through it". That is true: `parse` keeps that state and does not refuse a mid-line opener either (`skills/verify/scripts/unverified_check.py:300-306`, `skills/settle/scripts/rule_changes.py:106-130`, read). The new text the fix wrote carries a different defect, finding 1 above.

confirms: none
The smith's sibling sweep for round-1#2 was read against the diff. Its standing items each speak of the comment state alone, and each holds at `0c532fe8`. They are the `live_lines` docstring (`skills/verify/scripts/unverified_check.py:573-575`), the `readable` docstring (`:602-604`), `chain_check.py#comment_lines` (`skills/code-review/scripts/chain_check.py:1168-1175`), the two cases at `tests/test_rule_changes.py:167` and `:234`, `hooks/blocks.py:19`, `bin/unverified-check:2` and `tests/test_a_phase_hands_the_next_one_a_record.py:32-34` (read). The sweep looked for claims about code-span state. It did not ask who walks `fence_spans`, which is how the omission at `:573-575` in finding 1 got past it. Round 1's answer names five of these items. The hand-back adds `hooks/blocks.py:19`, `bin/unverified-check:2` and the phase test, and all three hold.

Carried, not re-established: the orchestrator's `uvx ruff check`, `uvx ruff format --check` and `bin/test -n auto -q` run over the four modules at `0c532fe8`, 792 passed (executed by the orchestrator, not re-run here). Also carried from round 1: S1, S2, S11, the reading of every record, and the confirmations of phases 1 and 2. The fix diff touches none of the code they rest on, since it changes two docstrings and one test.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at `0c532fe8`, which `overview.md` labels unverified, honestly | the whole tree | the orchestrator, through `broad-gate` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `git grep -n -F 'delete the comment' 0c532fe8 -- .` | `tests/test_unverified_check.py:1385`, `skills/verify/scripts/unverified_check.py:167`, and round 1's record |
| `git grep -n -E 'COMMENT_LINE' 0c532fe8 -- '*.py' bin hooks` and the same at `62e0b133 -- tests` | readers at `chain_check.py:1177`, `rule_changes.py:128` and `unverified_check.py:890`; 8 test lines at `62e0b133`, 7 at `0c532fe8`, the eighth now the literal |
| `bin/test -q tests/test_unverified_check.py -k "comment_line or Test_comment_lines"` | exit 0, 4 passed |
| `bin/mutation-check skills/verify/scripts/unverified_check.py`, two `--replace` mutants of the message, `--tests` the `comment_line` cases of `tests/test_unverified_check.py`, `tests/test_chain_check.py` and `tests/test_rule_changes.py` | baseline passed; mutant 1 red, mutant 2 red; file restored, `git diff --quiet` exit 0 |
| The same with the first mutant, `--deselect` the pinning case | SURVIVED, 9 passed; file restored, `git diff --quiet` exit 0 |
| `git grep -n -E 'closed_fence_lines\|fence_spans\|blank_fences\(' 0c532fe8 -- '*.py' ':!tests/'` | `fence_spans` reached from `blank_fences`, `closed_fence_lines`, `chain_check.py:1162` and `rule_changes.py:115` through `blank_fences` |

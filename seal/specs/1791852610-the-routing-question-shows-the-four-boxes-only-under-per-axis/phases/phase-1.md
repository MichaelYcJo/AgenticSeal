# 1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 976f92e0 |
| Ran by | unknown — the spawn prompt named no agent or model for this segment; the orchestrator fills this row |

## What this phase was asked

Pin `hooks/worktree_consent.py#_routing_preset` before any document changes:
one case in `tests/test_the_guard_asks_once_per_session.py` that builds both
result shapes against the `ask_entries` fixture (question 1 alone, and
question 1 with a second `multiSelect: true` question carrying the four boxes
and a joined answer) and asserts that `automation` is the press in either,
`per axis` is not in either, and a later `per axis` in the one-question shape
takes back an earlier press given in the two-question shape. Seen red by a
throwaway edit to the reader, then reverted. `docs/worktree-guard-spec.md`
§*Creation consent* rule 3 gains the sentence that both shapes read the same,
and the case joins the section's `Enforced by:` line. The reader is not
changed.

## What this phase found

**The case.** `test_question_1_alone_and_the_boxes_beside_it_read_the_same_press`,
with a helper `with_the_boxes` that deep-copies `ask_entries`' two entries
and appends the boxes question to both the `tool_use` input and the
`toolUseResult`, answering it with the four labels joined by `, `.

**Seen red.** The throwaway edit, made through `Edit` and reverted through
`Edit`, inserted at the top of `_routing_preset`, after the type checks:

```python
    if len(questions) != 1:  # THROWAWAY-RED-911
        return False
```

`bin/test tests/test_the_guard_asks_once_per_session.py -q -p no:xdist -k
read_the_same_press` then exited 1:

```
>           assert wc.automation_answered(str(repo), "me") is True, shape
E           AssertionError: the boxes beside it
E           assert False is True
tests/test_the_guard_asks_once_per_session.py:1465: AssertionError
1 failed, 101 deselected in 0.30s
```

Against the shipped reader the same command exited 0 (`1 passed`), and after
the revert the whole module exited 0 (`102 passed`). `git diff` over
`hooks/` was empty before the commit.

**Q3 is now a measured fact, not a reading.** The reader keeps both shapes
because it skips any question whose `multiSelect` is not `False`, so phase 2
may write that both shapes read the same.

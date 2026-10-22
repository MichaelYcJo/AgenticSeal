# Phase 5: 1792627930-the-section-sign-is-still-syntax

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 281f8960 |

## What this phase was asked

One fence rule. `unverified_check.py` imports `fence_opener`,
`fence_closes`, `GFM_LINE_RE` and `gfm_lines` from `hooks/blocks.py`, and
its own copies and the two in-step cases go (S12). A labelled line in a
closed fence is still not read, and an unclosed fence is still refused at
its line. The record recomputes its coordinates at HEAD before the first
edit.

Coordinates at HEAD 770f23ff, before the first edit (executed):
`git grep -n -E 'fence_opener|fence_closes|GFM_LINE_RE|gfm_lines' -- . ':!seal/specs'`
printed 123 lines; the definitions stand at
`skills/verify/scripts/unverified_check.py` lines 157, 160, 283 and 358 and
`hooks/blocks.py` lines 115, 124, 135 and 372, and every other line is a
caller or a mention. The new case
`tests/test_unverified_rows_close.py::test_the_fence_rule_and_the_line_split_are_the_hooks`
failed at that HEAD against the copies (executed).

## What this phase found

**The import.** `unverified_check.py` loads `hooks/blocks.py` by path at
import, from the `hooks/` beside it, which the config reader already reached
the same way; the `HERE` and `HOOKS` it defined further down moved to the
top so both loaders share them. The four names are re-exported, so every
caller that asks `reader.fence_opener`, `reader.gfm_lines` and the rest
works unchanged. The reasons the removed docstrings carried went to one
comment at the import (the readers that ask the rule, the readers that keep
their own on purpose, the walk kept apart from `live_lines`) and to
`hooks/blocks.py`'s own comments (the three-space bound and why a fourth
space inverts the fence state), which now say the rule is written there
once.

**Two readers loaded the reader without its new sibling, and the class was
three.** `evals/scripts/replay_targets.py#CHECK_FILES` copies the files a
commit's check needs into a scratch tree, and the grammar case of
`tests/test_chain_check.py` and the replay case of
`tests/test_a_rewritten_definition_proved_non_inferior.py` build such trees
by hand; all three failed with `hooks/blocks.py` missing (executed: 43
failed). `CHECK_FILES` now carries `hooks/blocks.py`, skipped where a commit
does not hold it, so a reader from before this change still loads; the
replay case copies `CHECK_FILES` itself rather than a second list, and the
grammar case writes the hook module beside the reader. A search for every
other caller that copies or extracts the reader (`git grep
unverified_check.py`, executed) found none: the rest load it from a whole
checkout.

**What stayed as it was (executed, the boundary run).** A labelled line in
a closed fence is still not read (`test_the_template_is_the_record_the_check_reads`
plants a `verdict:` in the fix block), and a fence that never closes is still
refused at its opening line; `tests/test_chain_check.py` and
`tests/test_unverified_rows_close.py` passed whole.

**Mentions that named the old definitions** were pointed at
`hooks/blocks.py`: `payload_meter.py`, `.github/scripts/rules.py` and three
test modules. `.test_durations` still lists the two removed cases; it is
measured and rewritten by CI, and no case reads a stale entry as a failure
(executed: the Windows-shards meta module passed).

**Mutation-check, each killed (exit 0, executed):** the re-exported
`fence_opener`, `fence_closes` and `gfm_lines`, each replaced by a local
stand-in.

**Preload bytes at the end (executed):**

| Agent | Base 0d62145a | Head | Change |
|---|---|---|---|
| framer | 25255 | 25194 | -61 |
| smith | 24746 | 24668 | -78 |
| warden | 25370 | 25300 | -70 |
| sealer | 23383 | 23302 | -81 |
| scribe | 18545 | 18486 | -59 |

Q5 holds: every preload is below the base this branch has.

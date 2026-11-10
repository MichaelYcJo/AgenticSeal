# Review round 2: 1794352647-a-first-frame-preloads-the-fold-procedure

```seal
target: ff0927ffb, fixes 493553094..ff0927ffb
```

This is a verifying round over the fix pass of round 1. The range holds
three commits: `8227339c3` commits the round 1 record, `f4a5169c9` is the
fix of finding 1, and `ff0927ffb` commits the fix pass's close block.
`git diff --stat 493553094 ff0927ffb` lists `skills/implement/orchestration.md`,
`tests/text/test_the_rules_have_one_owner.py` and the round 1 record alone
(executed). The records that state the present, `routing.md`, the three
frame files, `gaps.md`, `changelog.md` and `pr.md`, are byte for byte the
text round 1 read whole at `493553094`. No sentence in them names the
wording the fix changed, and *Scope* item 4 of `frame/design.md` still
reads true of the paragraph. No `pr.<lang>.md` is owed, since both
language keys are English. Carried from round 1, and not re-established:
the coordinates of finding 1 and of the D1 row it cites,
`seal/threads/1794289596-implement-orchestration-grew-back/frame/design.md:83`.

## Findings

None.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `skills/implement/orchestration.md:110` reads "The orchestrator
corrects its row where the framer's hand-back names a defect in it", so
the sentence after the one ending "before it answers." names its actor,
as row 8 of D1 does (read). The paragraph is otherwise unchanged, and its
wrapping holds (`tests/behaviour/test_docs_line_wrap.py`, executed). Row 8
of `tests/text/test_the_rules_have_one_owner.py#test_a_decision_after_the_frame_is_folded_into_it`
(`:512-518`) pins the new first words. The pinned string is absent from
the sentence as it read at `493553094`, so the row fails against the
unfixed text, which matches the close's account of the pin seen red
(read). Finding 1's `evidence:` search, re-run as
`git grep -n "corrects its row"` outside `seal/threads/`, finds only the
fixed sentence and the pin (executed). The fix is the finding's snippet,
and no new unit enters the fix diff beside it: the comment above row 8
names the round that changed the row. No `regression:` is owed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at `ff0927ffb`. This round ran two modules narrow, and the suite stays `unverified`. | `Broad gate` in `seal/config.json` | the orchestrator, by `seal gate --record` |
| `release_report.py`'s `preloads` row for the framer, unchanged from round 1. | `.github/scripts/release_report.py#preloads` | the orchestrator, at the release's pull request into `main`, as `gaps.md:8` says |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_docs_line_wrap.py -q` | exit 0 |
| `git grep -n "corrects its row" -- ':!seal/threads'` | `skills/implement/orchestration.md:110` and `tests/text/test_the_rules_have_one_owner.py:516` only |
| `git diff --stat 493553094 ff0927ffb` | the two fixed files and the round 1 record |

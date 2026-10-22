# 1792619408-an-automation-run-stops-at-the-parity-arm — review round 2

target: 43eb0af3, fixes 77eef010..43eb0af3

This is a verifying round. Its target is the fix range 77eef010..43eb0af3: 7eacbe1c, 6a87e4a8 and f0507fed, with the record commits cf7a032f, e6aa982c and 43eb0af3. Round 1's coordinates were carried rather than searched again: the `## Rule changes` replay, the liveness reading of spec line 200, and the routes the round-1 probe built. Every verdict below was reached again on the tree at 43eb0af3. No probe line of round 1 was taken on trust: the replay and the parse were run again. This repository declares no `seal/parity.md`, so no parity comparison was made and this record carries no `original:` line. The review ran in a `git clone --no-local` of the branch at 43eb0af3.

The coordinator said `release/v0.22.3` moved to a16acb40, where #986 merged, and that it shares no file with this branch. Checked: of the 69 paths that eae7f0ad..a16acb40 changes, none is among the paths eae7f0ad..43eb0af3 changes (executed, `comm -12`).

The coordinator asked for the hardest look at 7eacbe1c. Every `spec.md` blob git holds, 392 of them, was parsed by the reader at 77eef010 and the reader at 43eb0af3, and the results were compared. Only two blobs differ, both this work item's own `spec.md` before f0507fed, and the new reader refuses them at the wrapped line, as intended. Crafted shapes found one shape the old reader parsed correctly that the new one does not. That shape is finding 1.

## Findings

### 1. The fix for round 1's finding 2 silently drops Rule changes operations after a fenced comment opener

severity: must
location: `skills/settle/scripts/rule_changes.py:103-113`, `tests/test_settle_applies_rule_changes_in_place.py`
evidence: executed `python3 -I skills/settle/scripts/test_tmp_parse_diff.py`, `python3 -I skills/settle/scripts/test_tmp_fix.py`
verdict: fixed 8aeda705
regression: round-1#2

The unit is `rule_changes.py#parse` lines 103-113, which 7eacbe1c added. The frame does not touch this reader: neither `spec.md` nor a `plan.md` phase names it. The fix followed round 1's paste-ready block, which this round's reviewer wrote. The defect came from that block. It took the comment state from `unverified_check.py#comment_scan`, which reads a comment opener even inside a fenced block. `live_lines`, which `parse` already reads, decides a fence before anything else on the line, and its docstring names `comment_scan` as a reader that stays off its path (`skills/verify/scripts/unverified_check.py:685-687`).

What it breaks: `began_outside` now says a line began inside a comment whenever a comment opener stands in an earlier fenced block, such as an HTML example in a spec's prose, with no closer on its line. That holds up to the next comment closer anywhere in the spec. Every body line in that region is skipped as a comment, without an error.

- Shape A. The section lies wholly in that region, and the next closer comes after it. `parse` refuses with "the section is empty". The old reader read the operation whole, so this shape is now refused where it was parsed correctly.
- Shape B. A comment between two items closes the region inside the section. `parse` returns only the operations after that comment, with no error. In the probe, three `add` operations went in and one came out, for `docs/c.md`; the old reader returned all three. `settle` would apply the one and drop the two, and `chain-check` passes it. That is the loss #1006 and round 1's finding 2 exist to stop, moved to a new shape.

No spec in history has either shape: all 392 blobs read the same under the old reader and the new one, apart from the intended refusal. So nothing is lost today. But this reader is the one every spec passes through, and the shape is ordinary prose.

The fix keeps the intent of 7eacbe1c and reads the comment state from the same walk `live_lines` makes. `live_lines` ANDs two readings, and in the first, `_liveness(lines, spans_cross_lines=False)`, a code span never leaves its line. A line dead in that reading is inside a comment or a fence, read fence first, and is skipped as the old reader skipped it. A line live there but dead in `live` begins inside a span an earlier line opened, and it is refused.

Precondition: `lines` is `r.gfm_lines(text)`, the list `live` and `fenced` are indexed by. `_liveness` is private to `unverified_check.py`, so the fix pass may give it a public name; the probe called it as it is. The probe ran this candidate over the 392 blobs and every shape. It equals 43eb0af3's reader on every blob, keeps the wrapped-span refusal, and returns all three operations of shape B and the operation of shape A.

A case beside `test_a_line_that_begins_inside_a_code_span_is_refused_at_its_line` would pin it. Its spec opens with a fenced html example whose one line opens a comment and does not close it. Its `## Rule changes` holds three `add` items with a one-line comment between the second and the third, and it expects three operations and no error. Run against 43eb0af3, it returns one operation.

```python
    live = [flag for _, flag in r.live_lines(lines)]
    fenced = r.closed_fence_lines(lines)
    # `live_lines` ANDs two readings. In this one a code span never leaves
    # its line, so a line dead here is in a comment or a fence, read fence
    # first as `live_lines` reads it, and is skipped as before. A line live
    # here and dead in `live` begins inside a span an earlier line opened,
    # and is refused (#988).
    literal = r._liveness(lines, spans_cross_lines=False)

    body = []
    for n in range(start + 1, end):
        line = lines[n]
        # opens_comment: NAME NOT IN TREE, the test at rule_changes.py:111
        # for a line that opens an HTML comment, unchanged
        if opens_comment(line) or (not live[n] and n not in fenced and not literal[n]):
            continue
        if not live[n] and n not in fenced:
            why = (
                "this line begins inside a code span an earlier line opened, "
                "and settle would drop it: close each span on the line that "
                "opens it"
            )
            return Parsed([], None, [(n + 1, why)])
        body.append((n + 1, line))
```

answer: The finding holds, and it is fixed. In 8aeda705, `rule_changes.py#parse` reads its comment state from `unverified_check.py#liveness`. That is the reader formerly named `_liveness`, given its public name in the same commit, with no copy made. It reads with `spans_cross_lines=False`, the same reading `live_lines` ANDs, which decides a fence first. `test_a_comment_opener_inside_a_fence_above_the_section_hides_no_operation` was seen red against 43eb0af3's reader: shape B returned `docs/c.md` alone, and shape A was refused as empty. Round 1's case still passes, so a wrapped span is still refused. 630a63b0 added two shapes to the case. A wrapped span below such a fence is refused at its line, and a fence inside the section is refused at its opener as no field. With those shapes, `mutation-check` showed that the fenced-line term of the record's candidate could not be told from its absence. A fence's opener is live, so the section is refused there either way. 4d37579b therefore reduced the condition to: skip a line dead in `liveness`, and refuse one live there and dead in `live_lines`. `mutation-check` turned the case red for four mutations: the comment state read from `comment_scan` again, the skip removed, the refusal removed, and the crossing reading. Over all 120 `seal/specs/*/spec.md`, the reader at HEAD returns exactly what 43eb0af3's reader returns, and refuses none. The changelog fragment's sentence does not change.

## Confirmations

confirms: round-1#1
f0507fed closes each code span of the second `add` operation on its own line (`spec.md:205-226`). At 43eb0af3 `rule_changes.parse` reads the section as eight operations with no error. `rule_changes.replay` placed all eight on the docs at HEAD, and the settled paragraph in `docs/the-review-record.md` names the answer and the `original:` line whole (executed, `## Probes`). The lines f0507fed added to the Parity arm `add` operation open and close every span on one line, and they parse.

confirms: round-1#2
The defect round 1 named holds closed. A line that begins inside a code span an earlier line opened is refused at its number. The 0f665edc and b765c132 blobs of this spec are refused at lines 200 and 174, and the crafted wrapped span is refused too (executed). `tests/test_settle_applies_rule_changes_in_place.py` passes, 82 cases, and `tests/test_chain_check.py -k RuleChanges` passes, 20 cases (executed). The comment state the fix reads is a new defect, finding 1 of this round.

confirms: round-1#3
The orchestrator took the limit sentence, and the answer gives the grounds: the review arm's declaration carries the same cost in local mode. The limit stands in the Parity arm `add` operation (`spec.md:184-195`), which settles whole (executed). It also stands under the wake/quiet table (`skills/implement/orchestration.md:459-469`), behind a pointer in `skills/legacy-parity/SKILL.md:123-125`, and in the changelog fragment. S13 now says where the place that refuses exists (`spec.md:87`). The table text and the operation's text match. That is the same pairing the arm tables already have, because a settle runs when the owner calls it (`docs/release-checklist.md:80`), so the shipped skill states the rule until then.

confirms: round-1#4
The pin and the rewritten declaration are stated in the changelog fragment, in the Parity arm `add` operation and in the orchestration paragraph. `plan.md` *Operational impact* now names the pin as the condition under which the refusal is met, and *Summary*, the failure scenario and row B name the shapes (read, `plan.md:28-31`, `plan.md:79-82`, `plan.md:96`, `plan.md:142-152`).

confirms: round-1#5
`skills/parity-setup/SKILL.md:58-66` names the chain-declared branch as the exception, after the sentence on `<git-dir>`, so "That is" still points at the mark's path. `templates/hygiene.yml:89-93` lists the new refusal after the `## Rule changes` one (read).

confirms: round-1#6
`overview.md` *Not done* names the two operations 77eef010 added, and *Fed back into the spec* names the four divergences carried at 77eef010 (read, `overview.md:23-37`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| CI run 39699178855 at 43eb0af3, which nobody has read yet | CI | the orchestrator, who relays a failure |
| The full suite, the repository-wide lint and the typecheck at 43eb0af3 | the whole tree | the orchestrator's broad run, `broad-gate --base release/v0.22.3 --record seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm` |
| `unverified_check.py#readable` and `chain_check.py#unclosed` read a comment before a fence too, the same order as finding 1. In round 1 this round's own record was refused at a fenced comment opener. Whether a fenced opener closed later can hide a whole finding from the pull-request check was not probed: it is base code outside this round's fix range | `skills/verify/scripts/unverified_check.py:703-718`, `skills/code-review/scripts/chain_check.py:1145-1170` | the orchestrator, whether to open an issue |

## Probes

| Command | Result |
|---|---|
| `python3 -I skills/settle/scripts/test_tmp_parse_diff.py` in the clone | 392 `spec.md` blobs; the reader at 77eef010 and at 43eb0af3 differ on 2, both this spec before f0507fed, refused at lines 200 and 174; of the crafted shapes, a fence earlier in the spec holding an unclosed comment opener went from 2 operations to "the section is empty"; two fenced-value shapes the old reader cut short are now refused; four shapes read the same |
| `python3 -I skills/settle/scripts/test_tmp_fix.py` in the clone | shape B: old 3 operations, 43eb0af3 1 operation with no error, the candidate 3; shape A: old 1, 43eb0af3 refused, the candidate 1; the wrapped span is refused by 43eb0af3 and by the candidate; over the 392 blobs the candidate equals 43eb0af3 on every one |
| `python3 -I skills/settle/scripts/test_tmp_replay.py` in the clone | this spec at 43eb0af3 parses into 8 operations with no error, and `replay` applies all 8; the settled paragraphs are whole |
| `bin/test tests/test_settle_applies_rule_changes_in_place.py -q` | 82 passed, exit 0 |
| `bin/test tests/test_chain_check.py -q -k RuleChanges` | 20 passed, exit 0 |
| `comm -12` over the paths of eae7f0ad..a16acb40 and eae7f0ad..43eb0af3 | nothing in common |

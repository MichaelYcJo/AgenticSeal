# 1792619408-an-automation-run-stops-at-the-parity-arm — review round 3

target: d5f9fc31, fixes 43eb0af3..d5f9fc31

This is a verifying round over 43eb0af3..d5f9fc31. The fix range is 8aeda705, 630a63b0 and 4d37579b, with the record commits 7b947a07 and d5f9fc31. From round 2 two things were carried, not searched for again: the shapes A and B, and the method of comparing readers over every `spec.md` blob git holds. Both were run again here. Every verdict below was reached on the tree at d5f9fc31. This repository declares no `seal/parity.md`, so no parity comparison was made and this record carries no `original:` line. The review ran in a `git clone --no-local` of the branch at d5f9fc31.

The probe built three readers, each with its own `unverified_check.py`: the base at eae7f0ad, round 2's target 43eb0af3, and d5f9fc31. It ran them over 394 `spec.md` blobs and 17 crafted shapes.

- d5f9fc31 returns exactly what 43eb0af3 returns on all 394 blobs. The smith said 120 specs; the claim holds and extends to every version in history.
- It differs from the base on two blobs only. Both are this spec before f0507fed, refused at the wrapped line, as round 1 intended.
- On the shapes, every one the base parsed is still parsed, and every one 43eb0af3 refused correctly is still refused.
- One shape that all three readers drop without an error is finding 1. It is round 1's finding 2 in a form the fix did not reach.

## Findings

### 1. A wrapped code span whose next line opens with a comment opener is still dropped with no error

severity: should
location: `skills/settle/scripts/rule_changes.py:110-122`, `skills/settle/SKILL.md:66-68`, `tests/test_settle_applies_rule_changes_in_place.py`
evidence: executed `python3 -I <scratch>/test_tmp_three_readers.py <clone> <scratch>/work`
verdict: fixed fcc7e989
reopens: round-1#2

Round 1's finding 2 was closed `fixed 7eacbe1c`, and round 2 confirmed it on the shapes it named. Its close does not hold for one shape the fix range rewrote but did not reach. `skills/settle/SKILL.md:66-68` now tells the person writing a spec that "a line that begins inside a span an earlier line opened is refused at its line". The reader breaks that sentence when such a line starts with the comment opener.

In the loop at `rule_changes.py:113`, the test for a line that starts with the comment opener runs before the code-span refusal at `:115`. The probe's shape is three lines:

1. a `to:` value that ends by opening a code span;
2. a line that begins with the comment opener and closes the span after it;
3. a line that closes the comment.

In markdown the opener on line 2 is inside the code span, so it is text. The reader skips line 2 as a comment opener, and skips line 3 as dead in `liveness`. It returns the operation with both lines gone and no error. Line 2 is live in `liveness` and dead in `live_lines`, which is exactly the refused case (executed, the flags printed for each line).

The base and 43eb0af3 drop it the same way, so this is a sub-shape the fix left standing, not a regression. No blob in history has it.

The fix moves the span refusal ahead of the comment skip. The probe ran that candidate over all 394 blobs and 17 shapes. It equals d5f9fc31 everywhere except this shape, which it refuses at line 2's number. A line that starts with the comment opener and is live in both readings is still skipped, as before. Precondition: `lines`, `live` and `literal` are indexed alike, as at `rule_changes.py:101-108`.

A case beside `test_a_line_that_begins_inside_a_code_span_is_refused_at_its_line` would pin it: the three-line value above, with the refusal expected at the second line. Run against d5f9fc31, that case returns the operation with no error.

```python
    body = []
    for n in range(start + 1, end):
        line = lines[n]
        if literal[n] and not live[n]:
            why = (
                "this line begins inside a code span an earlier line opened, "
                "and settle would drop it: close each span on the line that "
                "opens it"
            )
            return Parsed([], None, [(n + 1, why)])
        # opens_comment: NAME NOT IN TREE, the test now at rule_changes.py:113
        # for a line that opens an HTML comment, unchanged
        if opens_comment(line) or not literal[n]:
            continue
        body.append((n + 1, line))
```

answer: The finding holds, and fcc7e989 fixes it with the one reorder the record gives. In `rule_changes.py#parse` the refusal of a line that is live in `liveness` and dead in `live_lines` now runs before the comment skip, and the skip is otherwise unchanged. The comment above the loop says why the refusal comes first. `test_a_line_that_begins_inside_a_code_span_is_refused_at_its_line` gained the three-line shape: a value opening a span, a line that opens with `<!--` and closes the span, and a line that closes the comment. Against d5f9fc31's reader that shape returned the operation with no error. Now it is refused at the second line. `mutation-check` turned the module red for four mutations: the refusal removed, its `literal[n]` term dropped, the comment opener exempted from the refusal again, and the comment skip narrowed. Over all 120 `seal/specs/*/spec.md` the reader at fcc7e989 returns exactly what d5f9fc31's returns, and refuses none. `skills/settle/SKILL.md:66-68` now holds as written, so it is unchanged.

## Confirmations

confirms: round-2#1
The close holds. With `parse` reading the comment state from `unverified_check.py#liveness`, shape A returns its one operation and shape B returns all three, as the base does. A tilde-fence form of shape B also returns all three, while 43eb0af3 returned only `docs/c.md`. Shape C, a wrapped span below a fenced comment opener, is refused at its own line; 43eb0af3 called that section empty (executed). The new case and the module pass, 83 cases (executed).

confirms: none
The rename leaves no reader behind. `_liveness` is now `liveness`, with no copy. `git grep _liveness` outside `seal/specs/` finds only `tests/test_unverified_rows_close.py:2452`, a comment describing the code before #491, which is history, not a call (executed). `live_lines` calls the new name at `unverified_check.py:700-701`. `rule_changes.py`'s docstring lists the four functions it calls, and `closed_fence_lines` and `comment_scan` are no longer among them (read). Five modules that read the walk pass at d5f9fc31 (executed): `test_settle_applies_rule_changes_in_place` 83, `test_every_reader_ends_a_line_where_gfm_does` 17, `test_unverified_rows_close` 237, `test_whether_a_line_is_live_is_asked_by_what_the_line_does` 42, `test_settle_reads_before_it_removes` 63.

confirms: none
Dropping `n not in fenced` changes no result. A fence opener has at most three spaces of indent, a field continues only at four, and the opener begins live. So a fence inside the section is refused at its opener as "a line that is not a field of the item above", closed or not, exactly as the base refuses it (executed). An unclosed fence is refused at its opener too. 43eb0af3 refused it one line lower, with the code-span message.

confirms: none
Shapes 43eb0af3 refused correctly are still refused at d5f9fc31: the wrapped span, the wrapped span below a fenced opener, and a four-space fence in a value holding a comment opener. Shapes the base parsed are still parsed the same: a comment block between items, a comment holding a fence, a comment opened mid-line in a value, a comment opener inside a one-line code span, a stray backtick earlier in the spec, a double-backtick span, a section quoted in a fence above the real one, and the no-change block (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| CI run 39700796713 at d5f9fc31, which nobody has read yet | CI | the orchestrator, who relays a failure |
| The full suite, the repository-wide lint and the typecheck at d5f9fc31 | the whole tree | the orchestrator's broad run, `broad-gate --base release/v0.22.3 --record seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm` |
| Round 2's question: `readable` and `chain_check.py#unclosed` read a comment before a fence, and whether that can hide a finding from the pull-request check was not probed | `skills/verify/scripts/unverified_check.py:703-718`, `skills/code-review/scripts/chain_check.py:1145-1170` | the orchestrator, whether to open an issue |

## Probes

| Command | Result |
|---|---|
| `python3 -I <scratch>/test_tmp_three_readers.py <clone> <scratch>/work` | readers at eae7f0ad, 43eb0af3 and d5f9fc31 over 394 blobs: d5f9fc31 equals 43eb0af3 on all, and differs from the base on 2, both this spec before f0507fed; over 17 shapes, d5f9fc31 equals the base on every shape the base parsed correctly and refuses the rest; the reordered candidate equals d5f9fc31 on all 394 blobs and 16 shapes, and refuses the wrapped span whose next line opens with a comment opener |
| `python3 -I -c` over that shape with the d5f9fc31 reader | no error, the value cut to its first and last lines; `live_lines` false and `liveness` true on line 2 |
| `bin/test tests/<module>.py -q` for the five modules in the second confirmation, one command each | 83, 17, 237, 42 and 63 passed, each exit 0 |
| `git grep -n "_liveness"` and `git grep -n "liveness("` at d5f9fc31 | no call to the old name; the new name called at `unverified_check.py:700-701` and `rule_changes.py:108` |

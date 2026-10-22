# 1792619408-an-automation-run-stops-at-the-parity-arm — review round 4

target: 86917c2e, fixes d5f9fc31..86917c2e

This verifying round read the fix range d5f9fc31..86917c2e: round 3's record (c0e885e0), the fix fcc7e989, and the fix pass's record (86917c2e). fcc7e989 changes `skills/settle/scripts/rule_changes.py#parse` and one case in `tests/test_settle_applies_rule_changes_in_place.py`. Two things were carried from round 3 and run again here, not taken on trust: its 17 shapes, and its comparison of readers over every `spec.md` blob git holds. This repository declares no `seal/parity.md`, so no parity comparison was made and this record carries no `original:` line. The review ran in a `git clone --no-local` of the branch at 86917c2e.

The coordinator told this round to write a finding only for a defect the reorder introduces, or one it leaves standing on a shape that occurs in practice. The warden's definition says a round told the run is capped still reports what it finds at the severity it finds it. This round found nothing to report under either reading, so the two instructions did not conflict.

## Findings

None.

## Confirmations

confirms: round-3#1
The close holds. At `rule_changes.py:114-122` the refusal of a line that is live in `liveness` and dead in `live_lines` now runs before the comment skip, which is otherwise unchanged. This is the reorder round 3's record gives, line for line. The shape round 3 named, a value that opens a code span followed by a line that starts with the comment opener and closes the span, is refused at that second line. The base, 43eb0af3 and d5f9fc31 all returned it with no error (executed). The case now carries that shape, and `tests/test_settle_applies_rule_changes_in_place.py` passes, 83 cases (executed).

confirms: none
The reorder introduces no regression. The probe ran four readers, each with its own `unverified_check.py`: the base at eae7f0ad, 43eb0af3, d5f9fc31 and fcc7e989. It used 395 `spec.md` blobs, one more than round 3 because this branch has since committed another spec version, and 21 shapes: round 3's 17 plus four the reorder could reach. The new four are a comment line right after a closed one-line span; a one-line comment between items after a stray backtick in a value; a multi-line comment there; and a template comment at the head of the section.

fcc7e989 returns exactly what d5f9fc31 and 43eb0af3 return on all 395 blobs. It differs from the base on two only, both this spec before f0507fed, refused at the wrapped line as round 1 intended. On the shapes, it returns what d5f9fc31 returns on all but round 3's shape, and what the base returns on every shape the base parsed correctly, the four new ones included (executed). `tests/test_settle_reads_before_it_removes.py`, 63 cases, and `tests/test_chain_check.py -k RuleChanges`, 20 cases, pass at 86917c2e (executed).

confirms: none
The new lines in the case were read against their group. They extend round 1's case with the one shape that case did not hold, and no other case in the module covers it (read, `tests/test_settle_applies_rule_changes_in_place.py:207-239`). The comment above the loop states the new order and its reason, a comment opener inside a span being text (read, `rule_changes.py:102-108`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| CI run 39701879271 at 86917c2e, which nobody has read yet | CI | the orchestrator, who relays a failure |
| The full suite, the repository-wide lint and the typecheck at 86917c2e | the whole tree | the orchestrator's broad run, `broad-gate --base release/v0.22.3 --record seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm` |
| Round 2's question: `readable` and `chain_check.py#unclosed` read a comment before a fence, and whether that can hide a finding from the pull-request check was not probed | `skills/verify/scripts/unverified_check.py:703-718`, `skills/code-review/scripts/chain_check.py:1145-1170` | the orchestrator, whether to open an issue |

## Probes

| Command | Result |
|---|---|
| `python3 -I <scratch>/test_tmp_four_readers.py <clone> <scratch>/work` | 395 blobs: fcc7e989 equals d5f9fc31 and 43eb0af3 on all, and differs from the base on 2, both this spec before f0507fed; 21 shapes: fcc7e989 differs from d5f9fc31 only on round 3's shape, which it refuses at line 8, and equals the base on every shape the base parsed correctly |
| `bin/test tests/<module>.py -q` for `test_settle_applies_rule_changes_in_place` and `test_settle_reads_before_it_removes`, one command each | 83 and 63 passed, each exit 0 |
| `bin/test tests/test_chain_check.py -q -k RuleChanges` | 20 passed, exit 0 |

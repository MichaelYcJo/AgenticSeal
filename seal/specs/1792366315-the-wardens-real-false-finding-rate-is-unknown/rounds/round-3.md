# 1792366315-the-wardens-real-false-finding-rate-is-unknown — review round 3

target: 037cfda7, fixes bba75175..037cfda7

## Findings

None. This round read `git diff bba75175..037cfda7`. That range changes the
range branch of `truths_with`, adds one row to the stale-entry test, and
writes round 2's `verdict:` and `answer:` lines. Round 2's one finding
closes, as the confirmation below shows, and the new refusal makes no new
defect.

Carried from rounds 1 and 2 rather than re-established: everything outside
these three files. The suite, the sides, the figures and every record
other than round 2's are unchanged in this range (`git diff --name-only
bba75175 037cfda7`, executed).

## Confirmations

confirms: round-2#1
The close holds at acc86196 (executed).

The probe ran `truths_with` on four entries:

- `src/x.py:100-10` stops, naming the location and "a range that ends
  before it starts".
- `src/x.py:20–10`, an en-dash range, stops in the same way.
- A good location followed by `src/x.py:9-8` stops at the reversed one.
- `src/x.py:10-10` still writes a truth, which matches line 10.

Two things were also run at 037cfda7:

- `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q`
  passed 104, the new `a-range-that-ends-before-it-starts` row among them.
- The three generators regenerated every case and left `git status
  --porcelain` clean, so no committed truth moved.

The answer's red-first claim was not re-run. By reading it holds: at
bba75175 the branch has no refusal, so the row's `pytest.raises` could not
be met.

The new row has one limit. It checks that the message contains the
location, and the "no coordinate" refusal before it prints the location
too. So the row shows that the generator stops. It does not show which of
the two refusals stopped it. Today the range form passes the coordinate
check, so the new refusal is the one that fires (executed above). The row
would read green if a later change moved this location to the other
refusal. That is a weakness of the row, not a wrong result, and I raise no
finding on it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Round 1's row on five credits from rows no entry's `from` names, unchanged by this range | `seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/rounds/round-1.md` | the repository owner |
| The finding wording behind every class, which only #971's first comment holds | `seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/evals/false-rows.md` | the repository owner |
| The full suite, the repository-wide lint and the typecheck over the branch. This round ran one module | the branch | the orchestrator, through `broad-gate` |

## Probes

| Command | Result |
|---|---|
| `test_tmp_round3.py`, one file at the root of a `--shared` clone at 037cfda7, run once and deleted | the four entries listed under the confirmation: three stopped, naming the reversed range; the equal-ends entry wrote a truth matching line 10 |
| `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q` | 104 passed |
| `replay_targets.py --case` for the four replay cases, `seed_defects.py --case` for the four seeded cases and `rule_cases.py` | all exited 0; `git status --porcelain` showed only the probe file |

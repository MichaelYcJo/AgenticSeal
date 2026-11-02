# Review round 2: 1793588973-pr-body-reads-a-details-tag-as-github-does

```seal
target: 59ea22429, fixes 02c740e95..59ea22429
```

This is a verifying round. Its target is the diff of round 1's fixes, `02c740e95..59ea22429`. That range holds three commits: `d13f81643` (round 1's record), `662bca509` (one parameter of `tests/skills/test_pr_body.py`) and `59ea22429` (round 1's close block). `git diff --stat 02c740e95 59ea22429` lists `trail/rounds/round-1.md` and `tests/skills/test_pr_body.py` and nothing else (executed). No `seal/parity.md` is declared, so the round block holds no `original:` line. The review ran in a `git clone --no-local` of the branch worktree at `59ea22429`, under the round's scratch directory.

Carried from round 1 and not re-established: round 1's verdicts on the phase's code at `02c740e95`, which this round does not re-review; the coordinate `skills/code-review/scripts/pr_body.py:470-478` for where the refusal sentence is composed; and the framer's executed probe of how GitHub renders each line (`frame/design.md:16-18`). Re-run rather than carried: round 1's `evidence: executed` line for finding 1, the mutant that removes the repair clause.

## Findings

This round opens no finding, and none is a `must`.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the case for the line `a sentence <details` now pins the whole refusal sentence, so it pins the tag name and the repair clause "write it in a code span". The fix pass claimed that round 1's mutant alone turns exactly that parameter red. This round re-ran the mutant in the clone, and `bin/seal mutate` printed "red: the cases failed against the mutation" (executed, *Probes*). One case failed, `test_refuses_a_record_it_cannot_copy_faithfully[changelog.md-text10-3-said10]`, which is the `a sentence <details` parameter (`tests/skills/test_pr_body.py:373-380`). The failing line is `tests/skills/test_pr_body.py:409`, `assert said in refused.value.causes[0][2]`. It compared the parameter's sentence ending in "; write it in a code span" with the mutant's sentence ending at the backticked `<details>`. The other 30 cases passed against the mutant, and the clone's status was clean afterwards. Without the mutant, the module passes 31 cases (executed). So the parameter's `said` is the sentence the unmutated code composes, which round 1 read off `pr_body.py:474-478`.

The fix pass also claimed that every other new parameter's `said` still pins its tag name. Each of them is a backticked tag: `</details>` (twice), `</DETAILS>`, `<details open>` and `<details/>` (`tests/skills/test_pr_body.py:363-372`). None of them is a substring of the fixed tail every refusal ends with, the backticked `<details>` followed by the repair clause. So no other case passes on the tail alone (read).

```seal
confirms: none
```
What matched: the new parameter was read against its group, the parameters of `test_refuses_a_record_it_cannot_copy_faithfully`. It replaces the parameter it amends in place and adds no case. It is the only parameter that pins the repair clause, which no other case in the file pins (round 1's `git grep` for the clause, carried). One case is enough, because the clause is the same f-string for every tag the reading refuses (`pr_body.py:474-478`, read). `uvx ruff format --check` and `uvx ruff check` over `tests/skills/test_pr_body.py` each exit 0 in the clone (executed).

```seal
confirms: none
```
What matched: S5, this work item's records compose with no refusal with this record in them. This record writes every `details` tag in a code span. `bin/seal pr-body` over the work item's directory in the worktree, with this record written, exited 0 (executed, *Probes*).

## Edges weighed and not opened

The owner asked that the review not be overdone. Each edge below was weighed and not opened as a finding, with its grounds.

1. **The assertion is `in`, not equality.** A clause appended after "code span" would still pass the case. The case pins the sentence from "holds" to its last word, which holds the tag name, the claim about the fold and the repair. The other refusal parameters share this assertion, so changing it is a change to the whole test, not to the fix. A shipped appendix would cost a reader one extra clause, not a wrong repair.
2. **The `said` value copies the f-string.** A later rewording of the refusal has to edit this parameter too. That is what contract rule 14 asks the pin to do, so it is no cost to weigh.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `59ea22429` | the whole tree | the orchestrator's broad run, `seal gate`, after the rounds settle |
| How GitHub renders each line in the reading and in *Limits*; not probed again this round | `frame/design.md:16-18` | carried from the framer's executed probe; the orchestrator, should a later change alter the reading |

This round leaves nothing open. What comes due is the orchestrator's broad run, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pr_body.py -q -p no:xdist`, in a `git clone --no-local` at `59ea22429` | exit 0, 31 passed |
| `bin/seal mutate skills/code-review/scripts/pr_body.py --replace '; write it in a code span"' '"' --tests "bin/test tests/skills/test_pr_body.py -q -p no:xdist"`, in the same clone | red: 1 failed, 30 passed; the failure is the `said10` parameter at `tests/skills/test_pr_body.py:409`; the file was restored and the clone's status was clean |
| `uvx ruff format --check tests/skills/test_pr_body.py` and `uvx ruff check tests/skills/test_pr_body.py`, in the same clone | exit 0 and exit 0 |
| `bin/seal pr-body` over `seal/threads/1793588973-pr-body-reads-a-details-tag-as-github-does` in the worktree, with this record written, the body written to the round's scratch directory | exit 0 |

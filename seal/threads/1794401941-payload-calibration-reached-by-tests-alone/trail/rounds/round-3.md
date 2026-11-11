# Review round 3: 1794401941-payload-calibration-reached-by-tests-alone

```seal
target: 248d1fd5a, fixes 2751e1048..248d1fd5a
```

This is a verifying round. Its code bound is the range from round 2's
record commit `2751e1048` to `248d1fd5a`. In that range, `git diff --stat`
names one file outside the work item's records:
`skills/verify/scripts/payload_meter.py`. There `31480faea` rewrites the
`tokens` paragraph of the module docstring and nothing else (executed).
The records the range changes are `changelog.md:3` (`31480faea`),
`frame/design.md:32` and a new last row of `frame/plan.md` (the fold
`93fd4522e`), and round 2's close block (`248d1fd5a`). Every run below ran
in a `git clone --no-local` of the branch at `248d1fd5a`, under the round's
scratch directory.

`routing.md`, the three frame files, `gaps.md`, `changelog.md`, `pr.md`,
both phase records and rounds 1 and 2 were read whole at `858ebb12f` in
the session that wrote round 2. At `248d1fd5a` they differ from that
reading only at the lines the range changes, which this round read in the
diff (executed: `git diff 2751e1048 248d1fd5a`). No `pr.<lang>.md` stands,
and none is owed, since `seal/config.json` names English for both language
keys (read). No `seal/parity.json` is declared.

Carried from rounds 1 and 2 and not re-established, because the range
changes no code they judged: S1, S2, S3, S4, the `comm` of `## Removes`
against the diff, the callers of the four changed signatures, and the
`pr.md` quotes. The range changes no sentence `pr.md` quotes.

## Findings

No finding this round.

## Confirmations

```seal
confirms: round-2#1
```
What holds: each of the three texts round 2 located now says what the
meter prints. `31480faea` gives `changelog.md:3` and the `tokens`
paragraph at `skills/verify/scripts/payload_meter.py:23-29` round 2's
replacement text, word for word (read: the diff against round 2's two
snippets). `93fd4522e` gives `frame/design.md:32` round 2's sentence for
the framer, and drops the clause "so the column a reader adds up is the
total under it" (read). `31480faea` touches `changelog.md` and
`payload_meter.py`, two of the finding's locations (executed:
`git show --stat`).

Each text was then checked against the meter's output. On this tree
`bin/seal payload` prints the pair line of all five agent tables at
2,717 bytes and 850 tokens. That is 362 plus 488, the two files' own
figures in the session table, so the pair line is the sum of the file
figures it covers (executed). The probe tree round 2 built, whose
`CLAUDE.md` imports `notes.md`, gave the same result at `248d1fd5a`. With
`--json`, the agent `x` held file rows of 22, 19, 18 and 0 tokens. Each is
`round(bytes / 3.2)`. The three harness rows add to 37, the pair line round
2 saw. The total is 59, the sum of the four file rows (executed). The
new texts therefore hold where an import prints an indented line, which
the texts they replace did not.

Round 2's close block names `31480faea` and `93fd4522e`, and both commits
stand in the range with those contents. Its answer says "no printed figure
changes, so no case changes". That holds: the range changes no line of
code, and `bin/test tests/skills/test_payload_meter.py -q` passed 45
cases (executed). `uvx ruff check` and `uvx ruff format --check` on the
meter both exited 0 (executed).

What matched: the new row at the end of `frame/plan.md` *Judgments of the
run*. It says round 2's frame location went to the framer as a fold after
`31480faea`. `93fd4522e` is that fold, and it follows `31480faea` (executed:
`git log`).

Two sentences on the same fact stand outside the range. This round weighed
both and opened no finding for either. The docstring of `_estimated`
(`skills/verify/scripts/payload_meter.py:363-366`) keeps "so the token
column a reader adds up is the total under it". It speaks of the rows that
function returns, and those rows add up to its total in every table
(executed above). The indented import line under the pair line is
`render`'s repetition of a row already counted. The module docstring's
`tokens` paragraph now names that case. The docstring of
`test_every_token_figure_reads_estimated_at_the_assumed_ratio`
(`tests/skills/test_payload_meter.py:512-522`) gives the same clause as the
reason a total is not a second division. That reason holds.

The basis cell of a missing file prints `missing` in the text, not the one
label. `changelog.md:3` says "all under one basis". The JSON row for that
file still carries `BASIS`, and its figure is 0, which is no estimate
(executed: the probe's `$CLAUDE_CONFIG_DIR/CLAUDE.md` row). `render` printed
that cell the same way at the base. So this round reads the sentence as
true of every estimated figure and opens no finding.

`python3 skills/code-review/scripts/chain_check.py --baseline 52f87b8d3
--root <worktree> --worktree` ran before this record. It printed no notice
at a line of `frame/design.md` naming a test pin or a copy (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| the full suite, the repository-wide lint and the format check beyond the one test module and the one Python file this round ran | the tree at `248d1fd5a` | the orchestrator's broad gate |
| the Windows run of `test_refuses_a_root_that_defines_no_agent`, and the phase mutants round 1 did not re-run, which the range does not touch | `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/trail/rounds/round-1.md:275-276` | the answerers that round 1's two rows name |

## Probes

| Command | Result |
|---|---|
| `git diff --stat 2751e1048 248d1fd5a` | four records files and `skills/verify/scripts/payload_meter.py`, 14 lines |
| `bin/seal payload` | exit 0; five pair lines at 2,717 bytes and 850 tokens; six totals |
| `python3 skills/verify/scripts/payload_meter.py --root <scratch>/fixture --json`, with `HOME` and `CLAUDE_CONFIG_DIR` under round 2's scratch directory, read with `python3 -c` | exit 0; file rows 22, 19, 18, 0; harness rows sum to 37; total 59 |
| `bin/test tests/skills/test_payload_meter.py -q` | exit 0, 45 passed |
| `uvx ruff check` and `uvx ruff format --check` on `skills/verify/scripts/payload_meter.py` | both exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline 52f87b8d3 --root <worktree> --worktree`, before the record | exit 0; no notice on `frame/design.md` |

This round made no new file outside its scratch directory except this
record. It read round 2's probe tree and did not change it.

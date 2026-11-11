# Review round 2: 1794401941-payload-calibration-reached-by-tests-alone

```seal
target: 858ebb12f, fixes 238411e42..858ebb12f
```

This is a verifying round. Its code bound is the range from round 1's
target `238411e42` to `858ebb12f`. In that range, `git diff --stat`
names one file outside the work item's records:
`skills/verify/scripts/payload_meter.py`, where `df5b6d30b` rewrites the
`tokens` paragraph of the module docstring and nothing else (executed).
The records the range changes are `pr.md` (`2e534f6ad`), `changelog.md`
(`df5b6d30b`), `frame/design.md` *Scope* item 2 and `frame/plan.md` (the
fold `9cd2aaf1e`), and round 1's close blocks (`858ebb12f`). Every run
below ran in a `git clone --no-local` of the branch at `858ebb12f`, under
the round's scratch directory.

`routing.md`, the three frame files, `gaps.md`, `changelog.md` and `pr.md`
were each read whole at `858ebb12f`, then both phase records and round 1.
No `pr.<lang>.md` stands, and none is owed, since `seal/config.json` names
English for both language keys (read). No `seal/parity.json` is declared.

Carried from round 1 and not re-established, because the range changes no
code they judged: S3's byte-identical release report, S4's vulture and
`git grep` runs, the `comm` of `## Removes` against the diff, and the
callers of the four changed signatures. Re-run here: S1, S2, the
`strip_ansi` grep of S4, and the meter's own test module.

## Findings

### 1. The fixed texts say every row's token figure is its bytes over 3.2, and the `CLAUDE.md` pair line of each agent's table is a sum of rounded figures

```seal
severity: should
location: `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/changelog.md:3`, `skills/verify/scripts/payload_meter.py:23-29`, `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/frame/design.md:32`
evidence: executed `bin/seal payload` and `bin/seal payload --json` in the clone, the second read with `python3 -c`; executed `python3 skills/verify/scripts/payload_meter.py --root <scratch>/fixture` with `HOME` and `CLAUDE_CONFIG_DIR` under the scratch directory; read `skills/verify/scripts/payload_meter.py:362-372`, `skills/verify/scripts/payload_meter.py:451-480`, `tests/skills/test_payload_meter.py:242-291`
reopens: round-1#2
```

Why the close does not hold: round 1 found that three texts call a
figure its bytes over 3.2 where the meter prints a sum of rounded
figures, and named the totals. The fix and the fold restate the totals
correctly. But each new text says every row is its bytes over the ratio.
One row of every agent's table is not: the `CLAUDE.md` pair line. So the
same defect stands in the sentence the fix wrote.

Why it matters: `render` (`skills/verify/scripts/payload_meter.py:457-464`)
prints the pair as one line. Its bytes, characters and tokens are each
`sum(...)` over the harness rows. The token figure is therefore the sum of
the rounded figures of each file, not the line's bytes over
`ASSUMED_RATIO`. The summing is deliberate:
`test_an_import_in_either_file_of_the_pair_is_a_harness_row_under_it`
says "the pair's line sums and names it" (`tests/skills/test_payload_meter.py:250-251`).

On this tree the two numbers differ in all five agent tables. Each pair
line reads 2,717 bytes and 850 tokens. `round(2717 / 3.2)` is 849
(executed). A person who checks the release note's arithmetic against
that line finds it one token off.

`changelog.md:3` now reads "Every row, the session's and each agent's, is
its bytes over an assumed 3.2 bytes per token, and every total is the sum
of the rows above it". The first clause fails at the pair line. The second
clause fails in an agent's table where a file of the pair imports another.
`render` prints each imported file again as an indented line under the
pair line (`:465-475`), and the pair line already counts it. In a probe
tree whose `CLAUDE.md` imports `notes.md`, the agent table printed the
definition at 22 tokens, the pair line at 37, the indented import at 18,
and a total of 59. The lines above the total add to 77 (executed). The
pair line's own 120 bytes give `round(120 / 3.2)` 38, not 37.

The module docstring at `skills/verify/scripts/payload_meter.py:23-25`
says "Every row's token figure, the session's and each agent's, is its
bytes over `ASSUMED_RATIO`". It fails at the pair line in the same way.

The fold's *Scope* item 2 at `frame/design.md:32` says "Every row's token
figure, an agent's and the session's, is the row's bytes over
`ASSUMED_RATIO`, rounded, and each total's is the sum of its rows', so the
column a reader adds up is the total under it". The pair line contradicts
its first clause. Its last clause is contradicted where an import prints
an indented line, as the probe above shows.

The class was listed from what produces it. Every token figure the meter
prints comes from one of six lines: `_file_line` (`:544`), the indented
import line (`:473`), the session's row (`:522`), the two totals (`:479`,
`:527`) and the pair line (`:462`). Only the pair line and the totals are
sums. The texts were listed by `git grep` for "bytes over", "over an
assumed", "sum of its rows" and "sum of the rows" over `skills`, `lib`,
`docs`, `tests`, `.github`, `agents`, both READMEs and the work item's
frame, changelog and memo (executed). That grep is a sample by wording.
It found the three texts above, and three that hold. `_estimated`'s docstring
(`:363-366`) speaks of the data rows, where it is true. The plan's failure
scenario at `frame/plan.md:13` says the meter "estimates each file's tokens
at 3.2 bytes per token and sums them", which is true. The `BASIS` comment
at `:85` says only that every figure carries the label.

Fix for `changelog.md:3`, the second sentence:

```markdown
Every file's row, the session's and each agent's, is its bytes over an assumed 3.2 bytes per token, and the `CLAUDE.md` pair line of an agent's table and every total are the sums of the file rows they cover, all under one basis that reads `estimated (3.2 B/token, an assumed ratio)`.
```

Fix for `skills/verify/scripts/payload_meter.py:23-29`, the whole
`tokens` paragraph:

```python
  tokens          NEVER counted. Every file's token figure, the session's
                  and each agent's, is its bytes over `ASSUMED_RATIO`, and
                  the `CLAUDE.md` pair line and each total are the sums of
                  the file figures they cover, all labelled `BASIS`. A bare
                  number is refused by the module's own tests, because the
                  six calibration spawns put three agents at 2.7, 3.2 and
                  3.4 bytes per token — one ratio does not fit all of them.
```

These two snippets do not reach `frame/design.md:32`, which is the
framer's. That fold is owed too: its first sentence becomes "Every file's
token figure, an agent's and the session's, is the file's bytes over
`ASSUMED_RATIO`, rounded, and the `CLAUDE.md` pair line of an agent's table
and each total are the sums of the file figures they cover." The clause
"so the column a reader adds up is the total under it" goes, or is limited
to the lines that are not indented under the pair line. No case changes:
the fix changes no figure the meter prints.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `pr.md` at `858ebb12f` holds nine quotes, the `Closes #1484.`
line and the attribution line. Each quote is found word for word in
`frame/plan.md`, runs of whitespace collapsed (executed: a `python3` check
of each quote against the plan's text). The four *Approach* cells and their
four verdict cells come from the rows at `frame/plan.md:19`, `:21`, `:24`
and `:27`. The title row comes from `frame/plan.md:57`. Each coordinate
names the record, the heading and the row, and nothing follows it. No
sentence frames or joins the quotes (read). The fold `9cd2aaf1e` changes
no sentence `pr.md` quotes. The verdict on the two labels still cites
*Scope* item 2, and that item still asks for one basis label (read).
`2e534f6ad` touches `pr.md`, the finding's location (executed:
`git show --stat`).

What matched: the half of round 1's finding 2 that concerns totals.
`changelog.md:3`, the docstring and *Scope* item 2 now say each total is
the sum of its rows. In all six tables of `bin/seal payload --json`, each
total's tokens equal the sum of its rows' tokens. Each row's tokens equal
`round(bytes / 3.2)` (executed). The finding above is the half that does
not hold.

What matched: the fold's other sentence. The failure scenario at
`frame/plan.md:13` now reads "The meter now only estimates each file's
tokens at 3.2 bytes per token and sums them". This is true of
`_estimated` and of the pair line (read). The new *Judgments of the run*
row at `frame/plan.md:58` says the frame location went to the framer as a
fold. `9cd2aaf1e` is that fold, and its message names *Scope* item 2 and
the failure scenario (executed: `git show`).

What matched: round 1's close blocks. `df5b6d30b` touches
`changelog.md` and `skills/verify/scripts/payload_meter.py`, two of
finding 2's locations (executed: `git show --stat`). Its answer names
`payload_meter.py:22-28`. The rewritten paragraph stands at `:23-29`,
since it grew by one line, and `:22` is the `bytes, chars` line above it
(read). The commit touched the right paragraph; only the answer's span is
one line off, and no reader acts on that span.

What matched: the docstring commit breaks nothing that runs.
`bin/test tests/skills/test_payload_meter.py -q` passed 45 cases.
`uvx ruff check` and `uvx ruff format --check` on the meter both exited 0
(executed).

What matched: the records against the target, beyond the range. S1
holds: `bin/seal payload` with each of `--calibrate x`,
`--baseline-agent x`, `--baseline x` and `--sections x` exited 2. S2 holds:
`--json` exited 0 with the keys `agents`, `measured_at`, `root` and
`session`, and every table held `files` and `total` alone. Every basis was
the one label (executed). `strip_ansi` stands only at
`tests/skills/test_seal_stamp.py:275`, `:821` and `:862`, as
`changelog.md:8` says (executed: `git grep -n -w`). The case *Scope* item 6
keeps, `test_a_frontmatter_line_ends_only_where_yaml_ends_it`, stands at
`tests/skills/test_payload_meter.py:632`. The plan's two Status commits,
`2ec7b9776` and `1e3c11fb7`, exist with the subjects of their phases.
`.claude-plugin/plugin.json` reads `0.37.4`, as *Operational impact* says
(executed). `gaps.md` *Not done* still describes the tree: the docstring's
`tokens` paragraph still cites "the six calibration spawns" after the fix
(read).

`python3 skills/code-review/scripts/chain_check.py --baseline 52f87b8d3
--root <worktree> --worktree`, run before this record, printed no notice
at a line of `frame/design.md` naming a test pin or a copy (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| the full suite, the repository-wide lint and the format check beyond the one test module and the one Python file this round ran | the tree at `858ebb12f` | the orchestrator's broad gate |
| the Windows run of `test_refuses_a_root_that_defines_no_agent`, and the phase mutants round 1 did not re-run, which the range does not touch | `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/trail/rounds/round-1.md:275-276` | the answerers that round 1's two rows name |

## Probes

| Command | Result |
|---|---|
| `git diff --stat 238411e42 858ebb12f` | five records files and `skills/verify/scripts/payload_meter.py`, 13 lines |
| `bin/seal payload` | exit 0; each agent's pair line reads 2,717 bytes and 850 tokens |
| `bin/seal payload --json`, read with `python3 -c` | exit 0; keys `agents`, `measured_at`, `root`, `session`; every row `round(bytes / 3.2)`; every total the sum of its rows; one basis label |
| `python3 skills/verify/scripts/payload_meter.py --root <scratch>/fixture`, with `HOME` and `CLAUDE_CONFIG_DIR` under the scratch directory | exit 0; agent `x`: 22, pair line 37 at 120 bytes, indented import 18, total 59 |
| `bin/seal payload` with each of `--calibrate x`, `--baseline-agent x`, `--baseline x`, `--sections x` | exit 2 each |
| `bin/test tests/skills/test_payload_meter.py -q` | exit 0, 45 passed |
| `uvx ruff check` and `uvx ruff format --check` on `skills/verify/scripts/payload_meter.py` | both exit 0 |
| `python3` check of each `pr.md` quote against `frame/plan.md`, whitespace collapsed | nine of nine found |
| `python3 skills/code-review/scripts/chain_check.py --baseline 52f87b8d3 --root <worktree> --worktree`, before the record | exit 0; no notice on `frame/design.md` |

The probe tree's three files (`agents/x.md`, `CLAUDE.md`, `notes.md`) were
written under the round's scratch directory with `printf` in the shell, not
with the `Write` tool the proofer's rule on probe files asks for. They
stay there, and nothing outside the scratch directory was written but this
record.

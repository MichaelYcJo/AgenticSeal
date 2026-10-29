# Review round 2: 1793251203-seal-pact-passes-near-misses-of-an-anchor

target: 239819c7, fixes 09718b2f..239819c7

## Findings

### 1. A row four columns in, right under a paragraph line, passes in silence, and three texts call every such line a code block

severity: should
location: `skills/verify/scripts/pact_check.py:42-50`, `skills/verify/scripts/pact_check.py:501-512`, `tests/skills/test_pact_check.py:579-586`, `seal/threads/1793251203-seal-pact-passes-near-misses-of-an-anchor/frame/design.md:200-207`, `seal/threads/1793251203-seal-pact-passes-near-misses-of-an-anchor/trail/phases/phase-1.md:59-63`
evidence: executed `bin/test tests/skills/test_tmp_r2_probe.py -p no:xdist -q -s`
verdict: open
regression: round-1#1

The unit is `row_cells` (`skills/verify/scripts/pact_check.py:501`), which
`1783b55a` changed. The frame reads every line `config.unfenced` shows and
refuses a row naming a declared pact and a clause "whatever header it stands
under, or with none" (`frame/plan.md` phase 1, `frame/design.md` *Scope*
item 2 and `## Rule changes`). The fix returns no row for every line four
columns in and calls each one an indented code block. The defect came from
round 1's own paste-ready fix, which took the column count from
`gfm_table`'s heading test and left out the CommonMark condition that an
indented code block cannot interrupt a paragraph.

The fix pass claimed, in `row_cells`' docstring, that a line four columns
in "is an indented code block". That holds below a blank line, and the
probe confirms it there (P1, P2). It does not hold right under a paragraph
line. In CommonMark such a line continues the paragraph, so GitHub renders
`x` followed by a tab and a row as paragraph text. That is exactly how it
renders the headerless row of the id `a row with no header`, which the
group `test_refuses_an_anchor_row_no_anchor_table_holds` refuses. The probe
wrote both shapes under a signer declaring the pact. P7, a tab-indented row
under a paragraph line, exited 2 with the `OUTSIDE_TABLE` sentence (the
refusal of a row no anchor table holds) at `09718b2f` and exits 0 at
`239819c7`, printing nothing. P6, the same row four spaces in, exits 0 at
both commits, so the space shape predates the fix pass and the tab shape is
its own.

No text states the limit. The module docstring (`pact_check.py:42-50`)
says every other line that reads as a row is read, "whatever header it
stands under, or with none", and does not mention the column guard. The
docstring of `row_cells` and `trail/phases/phase-1.md:59-63` call the line
an indented code block. The `## Rule changes` limit names two misses only:
the `Pact` cell and the `Clause` cell. A signer who writes this shape misses
twice: the row has no header, and it is indented four columns. So a limit
sentence is the proportionate fix. Telling paragraph text from code by the
line above would be a second block grammar beside `gfm_table`, which
`frame/plan.md` A4 turns down. The limit's pin is one more line in the
passes case's frame z. Without the guard (P7 at `09718b2f`) that line is
refused, so the pin can fail.

```python
# skills/verify/scripts/pact_check.py, the module docstring, after
# "has no anchor's shape a fact can tell.":
A line four columns in, a tab counting to the next multiple of four, is
read as no row. Below a blank line it is an indented code block. Right
under a paragraph line GitHub renders it as text, a row with no header
that is also indented, and it is passed over as a row that misses twice.

# skills/verify/scripts/pact_check.py, row_cells:
def row_cells(config, line):
    """The cells of LINE read as a table row by `config.table_cells`, with
    an outer pipe given where LINE leaves one out, so a row of a table
    written without them reads too; None where LINE holds no pipe, does
    not read as a row even so, or stands four columns in, a tab counting to
    the next multiple of four (`blocks.columns`, as `gfm_table` counts a
    heading's). Below a blank line such a line is an indented code block;
    right under a paragraph line it is paragraph text, which the module
    docstring states as a limit."""

# tests/skills/test_pact_check.py, the passes case's frame z, one more line
# after the two-spaces-and-a-tab line:
            f"\n  \t| {PACT_URL} | {CLAUSE_PATH} | deadbeef |\n"
            f"\nx\n\t| {PACT_URL} | {CLAUSE_PATH} | deadbeef |\n",
```

```text
seal/threads/1793251203-seal-pact-passes-near-misses-of-an-anchor/frame/design.md,
the `add` entry of `## Rule changes`, its last sentence followed by:

    Each miss alone is refused. A line four columns in, a tab counting to
    the next multiple of four, is read as no row: below a blank line it is
    an indented code block, and right under a paragraph line, where GitHub
    renders it as text, it is a row with no header that is also indented.

trail/phases/phase-1.md:61-62, "is an indented code block and reads as no
row" becomes "reads as no row; below a blank line it is an indented code
block, and right under a paragraph line round 2, finding 1, states it as a
limit".
```

answer:

## Confirmations

confirms: round-1#1
The close holds for the shape round 1 named, a row in an indented code
block below a blank line. `row_cells` returns no row where
`config.blocks.columns(line) >= 4` (`pact_check.py:511-512`). The
kept-indentation step is gone, which is equivalent for a run of three
spaces or fewer, since `TABLE_ROW` admits three. Round 1's executed line,
written again as P1 and P2, now exits 0 with nothing refused. P8 and P9,
a row three spaces in with and without outer pipes, are still refused at
line 3, so the guard does not exclude a row it should read. The fix pass
claimed its case was red before the fix at frame z line 7. It is: the test
module of `239819c7` run over the `pact_check.py` of `09718b2f` failed the
passes case alone, with `OUTSIDE_TABLE` at `design.md:7`. It also claimed
that the mutants `if False:` and `>= 5` on the guard are red. Each, run
here, failed the passes case alone. Executed. Finding 1 is the paragraph
shape this close leaves unstated, not a reopening of this one.

confirms: round-1#2
The id `a row naming another pact the signer declares` stands in
`test_refuses_an_anchor_row_no_anchor_table_holds`
(`tests/skills/test_pact_check.py:941-945`), and every id now runs under a
signer config declaring the pact and `BILLING` (`:970-974`). With
`frozenset({ours})` passed in place of `declared_remotes` at the
`stray_rows` call, the module failed that id alone (1 failed, 107 passed).
The fix pass claimed it was red there, and it is. The added declaration
changes no other id's outcome: the module passes whole at `239819c7`. The
new id covers a shape no case of its group held. `seal layout --pairs` names
no pair in this module. Executed.

confirms: none
The fix pass wrote two lines per finding in `round-1.md`, a `verdict:` and
an `answer:` (`87cf5747`), and nothing else in that file. `1783b55a` touches
`skills/verify/scripts/pact_check.py` and `tests/skills/test_pact_check.py`,
every path the two findings' `location:` lines name. Read.

confirms: none
The phase record's mutation paragraph, corrected in place at `bbfbe93e`,
matches round 1: ten mutants, none of which narrowed the scan to this pact
(`trail/phases/phase-1.md:96-102`). Its column sentence matches the code
except for the paragraph shape finding 1 names. Read.

confirms: none
The changelog fragment matches the code and `## Rule changes`. The row
naming an undeclared remote is refused (`pact_check.py:759-761`, the
`UNDECLARED` arm). A row outside the anchor table naming a declared remote
and a clause is refused whatever its header (`stray_rows`). The token is
case-folded, and its space limit and the limit on a row that misses twice
are stated. The fragment's "misses both the header and the remote" names
one of the two misses `## Rule changes` lists, a narrower sentence, not a
wrong one. Its sentence "A line of an indented code block is not read as a
row" is true and says nothing of the paragraph shape. Read.

confirms: none
`gaps.md` matches the records. Its two divergence rows are phase 1's first
two corrections (`trail/phases/phase-1.md:20-31`). Its `## Not verified`
row names the orchestrator for the broad gate. Its `## Not done` is the
walker over-refusal round 1 left under `## Not judged`. Read.

confirms: none
The handoff's label is honest. The fix pass gave "608 passed over eight
modules", an aggregate this round did not re-run. It labels the full
suite, the repository-wide lint and the typecheck `unverified`, with the
orchestrator answering through `seal gate`, and this round ran none of the
three (contract rule 2). The narrow command below ran four modules: 310
passed. Executed.

Carried from round 1, not re-established: probe P3 (a four-space row below
a blank line reads as no row) and P5 (one refusal for the walker shape),
the frame's d01 to d26 reprobe, and the confirmations of *Scope* items 1
and 3, S5 and the `## Rule changes` `from:` text. None of them stands in
the fix diff.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck | the branch at `239819c7` | the orchestrator, by the broad gate |
| The fix pass's "608 passed over eight modules": the hand-back does not name the eight modules, and this round ran four | the fix pass's hand-back | the sealer, by its sample |
| Whether the issue `gaps.md` *Not done* says the orchestrator names for the walker over-refusal exists | `hooks/lib/config.py#gfm_table` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_r2_probe.py -p no:xdist -q -s` in a `git clone --no-local` at `239819c7`, seven cases, the signer declaring the pact and `BILLING` | P1, a tab-indented row below a blank line, and P2, two spaces and a tab: exit 0, nothing refused. P4, a near-miss header over a row naming `BILLING`: exit 2, `OUTSIDE_TABLE` at line 3. P6, a row four spaces in right under the paragraph line `x`, and P7, the same with a tab: exit 0, nothing refused. P8, a headerless row three spaces in, and P9, the same without outer pipes: exit 2, `OUTSIDE_TABLE` at line 3 |
| The same probe with `pact_check.py` taken from `09718b2f` | P1, P2 and P7 exit 2 with `OUTSIDE_TABLE`; P6 exits 0; P4, P8 and P9 exit 2 |
| `bin/test tests/skills/test_pact_check.py -q`, the tests of `239819c7` over the `pact_check.py` of `09718b2f` | 1 failed, 107 passed: the passes case, `OUTSIDE_TABLE` at `design.md:7` of frame z |
| `bin/test tests/skills/test_pact_check.py -q` with `frozenset({ours})` in place of `declared_remotes` at the `stray_rows` call | 1 failed, 107 passed: the id `a row naming another pact the signer declares` |
| `bin/test tests/skills/test_pact_check.py -q` with the guard written `if False:` | 1 failed, 107 passed: the passes case |
| `bin/test tests/skills/test_pact_check.py -q` with the guard written `>= 5` | 1 failed, 107 passed: the passes case, `OUTSIDE_TABLE` at lines 5, 7 and 9 of frame z |
| `bin/test tests/skills/test_pact_check.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_a_signer_declares_its_pact.py tests/test_censuses.py -q` at `239819c7`, unmodified | 310 passed, exit 0 |

Each edit was made with the Edit tool in the clone and reverted with
`git checkout` before the next. The probe file was deleted, and the clone
was removed before hand-back.

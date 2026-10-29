# Review round 3: 1793251203-seal-pact-passes-near-misses-of-an-anchor

target: 70472134, fixes d932b091..70472134

## Findings

### 1. The passes case's docstring calls a row right under a paragraph line a row in an indented code block

severity: should
location: `tests/skills/test_pact_check.py:546-552`
evidence: read `tests/skills/test_pact_check.py:546-552`, `skills/verify/scripts/pact_check.py:50-54`
verdict: open
regression: round-2#1

The unit is the docstring of `test_accepts_a_signer_citing_the_current_clause`
(`tests/skills/test_pact_check.py:540-552`), which `5c046e90` changed. The
frame, as round 2, finding 1 fixed it in `frame/design.md` `## Rule changes`
and the module docstring (`pact_check.py:50-54`), says a line four columns
in is an indented code block only below a blank line, and paragraph text
right under a paragraph line. The fix appended "below a blank line or right
under a paragraph line" to the docstring's noun phrase "a row in an indented
code block", so the paragraph shape is again called a code block. The
defect came from widening the existing phrase instead of splitting it.

Round 2's finding was that texts called every such line a code block. The
fix pass corrected the module docstring, the `row_cells` docstring, the
comment over frame z (`:580-582`) and `trail/phases/phase-1.md:60-68`. In
the same commit it wrote the same misreading into the docstring of the case
that pins the limit. An agent that edits this case reads that docstring
first, and it states the fact round 2 found wrong: CommonMark does not let an
indented code block interrupt a paragraph. Before `5c046e90` the docstring
named only shapes below a blank line, so it was true. The defect is the fix
pass's own.

```python
        """S6, S7 and S9's passes: two frames cite the current hash, one
        naming the pact by another spelling of its URL. A row naming another
        pact the signer's `Pact` row declares is passed over whatever its
        other cells hold, and neither a table nor a `pact:` token inside a
        closed fence, nor `compact:`, nor the word and its colon with a space
        on either side of the colon (#1132, S7), nor a table
        naming the pact's remote beside no heading, nor a row that misses
        twice, nor a row four columns in, by spaces or by a tab, in a frame
        holding no anchor table, is read: below a blank line it is an
        indented code block, and right under a paragraph line it is the
        paragraph text the module docstring states as a limit. Exit 0, and
        the `READ` and summary lines name the pact by its URL (contract
        rule 14)."""
```

answer:

## Confirmations

confirms: round-2#1
The close holds for every coordinate round 2 named. The module docstring
states the limit (`skills/verify/scripts/pact_check.py:50-54`). The
`row_cells` docstring calls the line a code block only below a blank line
(`:508-513`). The comment over frame z names the paragraph shape as the
stated limit (`tests/skills/test_pact_check.py:580-582`).
`trail/phases/phase-1.md:60-68` and the `add` entry of `## Rule changes`
(`frame/design.md:207-211`) match the module docstring. The code did not
change: the diff to `pact_check.py` is docstring lines only. The fix pass
claimed the new pin is red against the `pact_check.py` of `09718b2f`, with
frame z lines 7, 9 and 12 refused `OUTSIDE_TABLE`. Run here, the passes
case failed alone, refusing exactly those three lines. Line 12 also pins the
paragraph shape apart from line 7. With a mutant that reads a line under a
non-blank line with its indentation stripped, the passes case failed alone,
refusing line 12 and not lines 5, 7 or 9. Round 2's P6, a row four spaces
in right under the paragraph line `x`, was added to frame z at `70472134`
and passes, so the space shape is passed over as the limit states. No line
pins it, and the tab line already turns red for any paragraph reader.
Executed. Finding 1 is a text the same commit got wrong, not a reopening.

confirms: none
`70472134` changed two lines of `round-2.md`, the finding's verdict line
and its answer line, and nothing else in that file. The answer matches the
commit.
`5c046e90` touches `pact_check.py`, `test_pact_check.py` and
`trail/phases/phase-1.md`, three paths the finding's `location:` names.
Read.

confirms: none
The `add` entry folded into `frame/design.md` `## Rule changes` parses.
`rule_changes.parse` over the design at `70472134` returned three entries
and no errors, the third an `add` to `docs/the-pact.md`
*What this does not see*, which stands at `docs/the-pact.md:128`.
`seal rules --check` exits 0. The orchestrator claimed both, and both hold.
Executed.

confirms: none
`trail/phases/phase-1.md:53-55` now says the orchestrator wrote W1's Status
cell at `9c8252d3`. That commit changed the W1 row of `frame/questions.md`
from `open` to an answer naming `UNDECLARED` and `OUTSIDE_TABLE`. Read.

confirms: none
The changelog sentence matches the code: a line four columns in is not read
as a row, below a blank line or under a paragraph line
(`pact_check.py:518-519`, the `blocks.columns` guard). Read.

confirms: none
The handoff's label is honest. The fix pass gave "608 passed over eight
modules", an aggregate this round did not re-run. It skipped `seal mutate`
because the change adds no behaviour, and the `pact_check.py` diff is
docstring lines only, so that holds. The narrow command below ran four
modules: 310 passed. This round ran no broad gate (contract rule 2).
Executed.

Carried from rounds 1 and 2, not re-established: P1, P2, P4, P8 and P9 of
round 2, its `if False:` and `>= 5` mutants on the column guard, and round
2's confirmation of `round-1#2`. The fix diff changes no code they read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck | the branch at `70472134` | the orchestrator, by the broad gate |
| The fix pass's "608 passed over eight modules": the hand-back does not name the eight modules, and this round ran four | the fix pass's hand-back | the sealer, by its sample |
| Whether GitHub ends an anchor table at a row four columns in, as `gfm_table`'s docstring says, or reads it as one more row of the table, which `row_cells` would then pass over in silence; outside the fix diff, and nothing was rendered here | `hooks/lib/config.py#gfm_table`, `skills/verify/scripts/pact_check.py:518-519` | the orchestrator |
| Whether the issue `gaps.md` *Not done* says the orchestrator names for the walker over-refusal exists | `hooks/lib/config.py#gfm_table` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pact_check.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_a_signer_declares_its_pact.py tests/test_censuses.py -q` in a `git clone --no-local` at `70472134`, unmodified | 310 passed, exit 0 |
| `bin/seal rules --check` at `70472134` | exit 0, 17 excused in 268 check lines of 55 rule files |
| `rule_changes.parse` over the work item's `frame/design.md` at `70472134`, policy root `docs` | three entries, two `change` to *The pact anchor* and one `add` to *What this does not see*; errors empty |
| `bin/test tests/skills/test_pact_check.py -q`, the tests of `70472134` over the `pact_check.py` of `09718b2f` | 1 failed, 107 passed: the passes case, `OUTSIDE_TABLE` at frame z lines 7, 9 and 12 |
| `bin/test tests/skills/test_pact_check.py -q` with `stray_rows` passing a line whose line above is not blank to `row_cells` with its indentation stripped, and frame z given a four-space row under `x` at line 15 | 1 failed, 107 passed: the passes case, `OUTSIDE_TABLE` at frame z lines 12 and 15 alone |
| `bin/test tests/skills/test_pact_check.py -q` at `70472134` with the same line 15 in frame z and the checker unmodified | 108 passed, exit 0 |

Each edit was made with the Edit tool in the clone and reverted with
`git checkout` before the next run. The clone is removed before hand-back.

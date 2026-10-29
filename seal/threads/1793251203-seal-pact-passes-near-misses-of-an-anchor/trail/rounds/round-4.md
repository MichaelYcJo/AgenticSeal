# Review round 4: 1793251203-seal-pact-passes-near-misses-of-an-anchor

target: e7f26219, fixes fa710970..e7f26219

## Findings

## Confirmations

confirms: round-3#1
The close holds. The docstring of `test_accepts_a_signer_citing_the_current_clause`
(`tests/skills/test_pact_check.py:541-553`) now names a row four columns in,
by spaces or by a tab, and then gives the two shapes apart. Below a blank
line it is an indented code block. Right under a paragraph line it is the
paragraph text the module docstring states as a limit. That matches the
module docstring (`skills/verify/scripts/pact_check.py:50-54`) and the
`add` entry of `## Rule changes` (`frame/design.md:207-211`). The fix pass
claimed the docstring carries round 3's replacement word for word. A
substring search for round 3's fenced block in the test module found it,
opening at line 541. Executed.

confirms: none
The fix pass claimed a docstring change alone, with no behaviour changed.
`e68d8b41` changes one file, `tests/skills/test_pact_check.py`, and its
diff touches only lines inside the docstring that opens at `:541`. The case
body, frame z and the assertions are unchanged. That file is the path round
3, finding 1, names on `location:`. `bin/test tests/skills/test_pact_check.py`
passed 108 of 108 at `e7f26219`. Executed.

confirms: none
The fix pass claimed that every other sentence `5c046e90` wrote names the
two shapes apart. It cited `pact_check.py:52`, `:511`,
`tests/skills/test_pact_check.py:581`, `trail/phases/phase-1.md:63` and
`changelog.md:3`. It also claimed that the walker sentences,
`gaps.md:26` and `trail/phases/phase-1.md:87`, describe a line below a
blank line, where "code block" is the right word. This round searched
`e7f26219` for "code block", "paragraph line" and "four columns" over
`pact_check.py`, its test module, `docs/the-pact.md` and the work item's
directory, case folded. Each hit in code, a frame, a phase record or the
changelog is one of three kinds. It names the two shapes apart (the seven
coordinates above and `frame/design.md:207-211`). Or it names a fenced
code block (`pact_check.py:251`, its copy at
`tests/skills/test_pact_check.py:102`, and `frame/design.md:180` and
`:195`). Or it names the walker's line below a blank line (`gaps.md:26`,
`trail/phases/phase-1.md:87`). The `INLINE` message at `pact_check.py:251`
predates the branch. The other hits stand in round records, which record
what each round found and are not amended. So the docstring was the only
sentence of its class, and the claim holds. Executed.

confirms: none
`e7f26219` changes two lines of `round-3.md`, finding 1's `verdict:` line
and its `answer:` line, and nothing else in the file. The answer matches
`e68d8b41`. Read.

confirms: none
`tests/behaviour/test_one_word_one_meaning.py` names the changed test
module in `RENAMED_COMPAT` (`:940`) and sweeps its prose. It passed 24 of
24 at `e7f26219`, so the new docstring spells nothing that module refuses.
Executed.

Carried from rounds 2 and 3, not re-established: round 3's red runs of the
passes case against the `pact_check.py` of `09718b2f` and against its
paragraph-reading mutant, round 2's P1 to P9, and round 3's confirmations
of `round-2#1` and of the `## Rule changes` parse. The fix diff changes no
code, no frame and no rule that those runs read.

This round leaves nothing open. The next step is the orchestrator's broad
gate, then the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck, which stay `unverified`; this round ran none of them (contract rule 2) | the branch at `e7f26219` | the orchestrator, by the broad gate |
| Whether GitHub ends an anchor table at a row four columns in, as `gfm_table`'s docstring says, or renders it as one more row of the table, which `row_cells` would then pass over in silence. This is carried from round 3. It is outside this fix diff, and nothing was rendered here | `hooks/lib/config.py#gfm_table`, `skills/verify/scripts/pact_check.py:518-519` | the orchestrator |
| Whether the issue that `gaps.md` *Not done* says the orchestrator names for the walker's over-refusal exists. This is carried from round 3 | `hooks/lib/config.py#gfm_table` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pact_check.py -q` in a `git clone --no-local` at `e7f26219`, unmodified | 108 passed, exit 0 |
| `bin/test tests/behaviour/test_one_word_one_meaning.py -q` in the same clone | 24 passed, exit 0 |
| `git grep -n -i 'code block\|paragraph line\|four columns' e7f26219` over `skills/verify/scripts/pact_check.py`, `tests/skills/test_pact_check.py`, `docs/the-pact.md` and the work item's directory | the hits sorted in the third confirmation; none outside a round record names a line right under a paragraph line as a code block |
| A Python substring search for round 3's fenced replacement in `tests/skills/test_pact_check.py` at `e7f26219` | found, opening at line 541 |

The clone and its outputs sit under the round's scratch directory and are
removed before hand-back.

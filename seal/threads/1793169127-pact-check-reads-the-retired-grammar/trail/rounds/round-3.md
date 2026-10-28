# Review round 3: 1793169127-pact-check-reads-the-retired-grammar

target: 6e59b1ea, fixes 49bb6ba5..6e59b1ea

## Findings

None. Both round-2 closes hold. The changed `opens_table` and the `beside`
arm introduce no defect this round could show, so no finding names a
regression.

## Confirmations

confirms: round-2#1
The close holds. `opens_table` (`hooks/lib/config.py:1052-1072`) no longer asks what stands above the other table's header. It asks two things: that the header is written `| … |`, and that a delimiter row of the header's width sits on the next shown line directly below it. The `***` shape left the refusal group. `test_accepts_an_anchor_table_above_another_table_in_its_section` now runs `a blank line`, `a sentence` and `a thematic break` between the two tables. These are the shapes round 2's probe found refused. Executed: run against `config.py` and `pact_check.py` as at `49bb6ba5`, `a sentence` and `a thematic break` failed. At `6e59b1ea`, all three pass (`## Probes`). A second anchor header under the anchor table is still named by `first_table`'s scan. The id `a second table under a blank line` holds that, and it passes.

confirms: round-2#2
The close holds. The `beside` arm marks the other table's header with `other = index` and does not end the walk (`config.py:1196-1224`). Each following line directly under it that is not a table end is stepped over as that table's delimiter or row. After a blank line or a hidden line, the adjacency test cannot hold again, because shown indices only grow. So a `| … |` line before the next heading reaches the stray-row refusal again. That is why removing the `other = None` reset in `693d6dc6` changes no result (read). The id `a row below another table` is round 2's probe shape. The id `a row a comment parts from another table` pins the adjacency test, where GFM ends the other table at the HTML comment. Executed: both failed against the code as at `49bb6ba5` and pass at `6e59b1ea` (`## Probes`).

confirms: none
`seal/config.md`'s readers and the machine-local map accept what they did before. `other` is set only inside the `beside` branch, and `beside` defaults to false. So for `config_table`, `read_table` and the map's `first_table`, the new adjacency test never holds, and the walk is the one round 2 confirmed (read, `config.py:1196-1224`). Executed: `tests/hooks/test_config.py` and `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py` passed inside the five-module run (`## Probes`).

confirms: none
The crafter's runs hold, with one difference in a count that the commit order explains. Against `49bb6ba5` this round got 4 failed, 6 passed. The crafter reported 3 failed, which was before `693d6dc6` added the comment case. At `49bb6ba5` that case also fails, because the walk stopped at the other table and printed nothing. At `6e59b1ea`, 10 passed, and the five modules gave 975 passed. `gaps.md` *Fed back into the spec* and the changelog fragment state the rule as built: whatever stands above the other table's header, it is no refusal where its delimiter row is directly under it, and a row after it before the next heading is still refused (read).

Carried rather than re-established: round 2's coordinates for `opens_table`, `gfm_table`'s ended branch and `first_table`. I opened them at their new lines and did not search again. Every verdict here was reached this round. Round 2's row of `## Not judged` about the line above the other table is moot now, because `opens_table` no longer asks about it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck | the branch | the orchestrator, through `seal gate` now that the rounds leave nothing open |
| The rebase onto #1058's `tests/conftest.py` change near `:418-433` | `tests/conftest.py` | the orchestrator, after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pact_check.py tests/skills/test_coordinates.py tests/hooks/test_config.py tests/test_censuses.py tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py -q`, in a clone at `6e59b1ea` | 975 passed, exit 0 |
| `git checkout 49bb6ba5 -- hooks/lib/config.py skills/verify/scripts/pact_check.py`, then `bin/test tests/skills/test_pact_check.py -q -k "anchor_row_nobody or above_another_table"`, in the clone | 4 failed, 6 passed, exit 1. The four: the accept case's `a sentence` and `a thematic break`, and the refusal ids `a row below another table` and `a row a comment parts from another table` |
| the same `-k` run after `git checkout 6e59b1ea -- hooks/lib/config.py skills/verify/scripts/pact_check.py`, in the clone | 10 passed, exit 0 |

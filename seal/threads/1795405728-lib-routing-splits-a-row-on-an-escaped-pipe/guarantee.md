# Guarantee: 1795405728-lib-routing-splits-a-row-on-an-escaped-pipe

Audited on 2026-11-23 by the sealer, at `bf5cd5cd3` against the base
`release/v0.38.6`. `release/v0.38.6@{upstream}` resolved first, to
`74ba63423` (executed: `git rev-parse --verify --quiet`). The branch merged
that commit at `9603d3fed`.

The gate record `trail/gate.md` names `run: 69e3217ac against 74ba63423`.
`69e3217ac` is an ancestor of HEAD (executed: `git merge-base
--is-ancestor`, exit 0). The one commit after it, `bf5cd5cd3`, touches only
this work item's `trail/gate.md` (executed: `git log --no-merges
--name-only 69e3217ac..HEAD ^74ba63423`). The broad gate's pass is the
orchestrator's account. The sealer read the gate log's verdict line,
`BROAD GATE PASSED ... @ 69e3217ac`, with 5764 passed, 9 skipped and chain
exit 0, and ran nothing broad (read, contract rule 2).

`bin/seal pr-body <item> --body <file> --check` exited 0 on the body the
spawn named (executed). The tree's `seal/config.json` names English for both
language keys, so no `pr.<lang>.md` is owed and none stands (read).
`git ls-files seal/parity.json` prints nothing, so no comparison with an
original is owed (executed).

## Claims re-run

The sample takes every `seen red` claim the phase records make for a case
the issue's *Done when* or a scenario rests on, and none of the rounds
re-ran them. Each one ran in a `git clone --no-local` of the worktree at
`bf5cd5cd3`, under the sealer's scratch directory `sealer/at-base/`, with the
nine changed code files under `lib/` and `skills/` restored from
`74ba63423` and HEAD's tests kept. One command ran them all: `bin/test -q -p
no:xdist -p no:cacheprovider tests/lib/test_routing.py
tests/lib/test_tables.py tests/skills/test_passages.py
tests/skills/test_pact_check.py -k "<the cases named below>"`. It exited 1,
with 13 failed and 11 passed (executed). The tree under audit was not
changed.

| Claim | Source | Command | Result |
|---|---|---|---|
| S1: `parse` read `fix/a\|b` as `fix/a` and a backslash before the change | `trail/phases/phase-1.md`, *Seen red*, first item | The at-base run above, `Test_parse::test_reads_an_escaped_pipe_and_an_open_row_as_cmark_gfm_does` | Holds. Red, with the failing line `('fix/a\\', 'framer') == ('fix/a|b', 'framer')`, the one the record quotes (executed) |
| S1 and S2: the routing shapes `an escaped pipe` and `an escaped last pipe` were red before the change | `trail/phases/phase-1.md`, *Seen red*, first item | The at-base run above, `Test_table_rows::test_reads_each_row_as_cmark_gfm_renders_it` | Holds. Both red: `('Branch', 'fix/a\\') != ('Branch', 'fix/a|b')` and `('Branch', 'fix/a \\') != ('Branch', 'fix/a |')` (executed) |
| S2: `gfm_table` refused a row without its closing pipe before the change | `trail/phases/phase-1.md`, *Seen red*, second item | The at-base run above, `test_a_row_without_its_closing_pipe_is_read_and_the_rows_below_arrive` | Holds. Red, `[] != [('Mode', 'shared'), ('Broad gate', 'x')]`, as the record quotes (executed) |
| The re-pinned backslash case and three `Test_table_cells` shapes were red before the change | `trail/phases/phase-1.md`, *Seen red*, third and fourth items | The at-base run above | Holds. `test_a_backslash_against_a_pipe_is_an_escaped_pipe` failed on `Right contains one more item: ('Broad gate', 'C:\\Users\\x\\tools|')`. `open at the end`, `an escaped last pipe` and `a backslash last` each failed on `None == <cells>` (executed) |
| A copy of `lib/routing.py` taken without `lib/tables.py` did not stop before the change | `trail/phases/phase-1.md`, *Seen red*, fifth item | The at-base run above, `Test_module::test_a_reader_copied_without_the_walk_names_it[without the row splitter]` | Holds. Red on `assert done.returncode != 0`, because the import exited 0 (executed) |
| S3: a routing cell holding a U+2028 was cut there before the change | `trail/phases/phase-2.md`, the paragraph on S3's case | The at-base run above, the shape `a U+2028 inside a cell` | Holds. Red, `('Branch', 'fix/a') != ('Branch', 'fix/a\u2028b')`, as the record quotes (executed) |
| `seal pact` counted a header after a U+2028 one line too far before the change | `trail/phases/phase-2.md`, *Three test files outside Scope item 6's list changed*, third item | The at-base run above, the two `U+2028` rows of `tests/skills/test_pact_check.py` | Holds. Both red, each naming line 8 where the case expects line 7 (executed) |
| S5: `passages.py#words` dropped the prose after a backtick run four spaces in before the change | `trail/phases/phase-3.md`, the paragraph on S5's case | The at-base run above, `test_reads_the_words_after_a_backtick_run_four_spaces_in` | Holds. Red on `assert shared(text, run)`, the line the record names (executed) |
| `Test_table_cells`' `four spaces in` refusal pins the three-space limit of `TABLE_ROW` (a case that asserts a line is not let through) | `trail/phases/phase-1.md`, the `seal mutate` table, the row `TABLE_ROW taking any indentation` | In `sealer/at-base/`, HEAD's code restored, `TABLE_ROW` edited from `r" {0,3}\|"` to `r" *\|"` alone, then `bin/test -q -p no:xdist -p no:cacheprovider tests/lib/test_tables.py -k Test_table_cells`; the edit was reverted afterwards | Holds. Exit 1, one failure: `four spaces in`, on `('a', 'b') is None` for `'    | a | b |'`. The failing line names that guard (executed) |
| S6: the seven searches print nothing at HEAD, and search 6 could fail | `frame/design.md` *User scenarios & acceptance*, the searches S6 names; each phase record's search paragraph | The seven `git grep` commands with the design's pathspecs, at HEAD; search 6 again at `74ba63423` | Holds. All seven exit 1 at HEAD. Search 6 at the base prints `lib/lines.py:93` and `lib/routing.py:147` (executed) |
| S7: no committed `routing.md` reads differently | `trail/phases/phase-1.md`, *S7's probe* | `test_tmp_s7.py` in `sealer/`, run with `python3 -I` under `git archive 74ba63423 lib` and under HEAD's `lib/`, over `git ls-files 'seal/threads/*/routing.md'` | Holds. `42 files; 0 differ`. Since phase 1 ran its probe, the base merge has brought in two more `routing.md` files than the 40 it read (executed) |
| G9 and the changelog: no tracked `.md` file holds any of the eight characters only `str.splitlines` ends a line at | `frame/design.md` G9; `changelog.md` *Fixed*, third bullet | A Python scan of `git ls-files '*.md'` at HEAD for VT, FF, `\x1c` to `\x1e`, NEL, U+2028 and U+2029 | Holds. `833 md files; 0 hold one` (executed) |
| The reader changes the changelog's *Fixed* and *Changed* sections name | `changelog.md` *Fixed*, first three bullets; *Changed*, both bullets | `test_tmp_shapes.py` in `sealer/`, `routing.table_rows` and `tables.table_cells` on five rows, under the base's `lib/` and HEAD's | Holds. At HEAD the escaped pipe reads `fix/a|b`, the open row reads, and the U+2028 cell reads whole. The even-run row and the four-space row are no row at HEAD, and both were read at the base (executed) |
| The test modules the diff changed pass at HEAD | `trail/rounds/round-2.md`, *Probes*; each phase record's boundary run | `xargs bin/test -q < changed-tests.txt` in `sealer/at-head/`, over the ten `tests/**/test_*.py` files the diff changes | Holds. 1302 passed, exit 0 (executed) |
| *Done when*: no `# exempt from splitlines` marker and no `splitlines` call stands in `lib/` | Issue #1574 *Done when*, first line; `changelog.md` *Removed*, first bullet | `git grep -c 'exempt from splitlines' -- lib` and `git grep -n splitlines -- lib` at HEAD | Holds. The first exits 1. The second prints seven docstring and comment lines that name `str.splitlines` in prose, and no call (executed, read) |
| Each `## Removes` row and each removal the changelog names stands nowhere in the tree | `frame/design.md` `## Removes`; `changelog.md` *Removed* | Searches 1 to 7 above, and `git grep -nE` at HEAD over `lib skills tests hooks .github` for `_starts_in_inline_html`, `def _starts`, `def _tokens`, `SENTINEL`, `SPACES`, `Test_split_row`, `Test_walk_text` and both removed refusal sentences, and `git grep -nw _heading_level` | Holds. Each prints nothing outside this work item's records, apart from `Test_heading_level`, an unrelated class that the unanchored pattern matched (executed) |

Not re-run, and carried as each party's account: phase 3's corpus probe
(`71 files; 1 differ`), the three `seal mutate` tables apart from the row
above, and the phase boundary runs. The Windows leg of CI is `unverified`.
The plan's row on what the gate change carries leaves it to CI, and the
orchestrator answers it when it reads CI.

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| The design (`frame/design.md`, `frame/plan.md`, `routing.md`) | One row splitter, `lib/tables.py#table_cells`, widened to the open end cmark-gfm reads. Every reader hands the walk `gfm_lines`. `passages.py` reads fences through `lib/lines.py#readable`. `## Removes` lists eleven removals. The routing grounds name `lib/routing.py`, `lib/lines.py` and the gates that read them | The issue's *Direction* and its three *Done when* lines. The diff, which changes exactly the files *Scope* items 1 to 7 name. The rows re-run above | None. The *Why this way* grounds describe the diff: the readers under `lib/` and the scripts that call them, with nothing outside that set such as a hook |
| The build (the diff `74ba63423...HEAD` and `trail/phases/phase-1.md` to `phase-3.md`) | The three phases deliver *Scope* items 1 to 3, 4 to 6 and 7. The departures the records name are `CELL`'s third alternative, `TABLE_ROW` matching a row's start only, the removal of `_heading_level`, and Q1's default | The design, whose fold at `179c682bc` and `71d7587cf` and round 1's fix carry those departures. Every phase whose `frame/plan.md` Status cell holds a commit (`b24a84ad0`, `f418c6af8`, `0c6943d76`) has its phase record, as `routing.md`'s `crafter` row owes. Every `seen red` re-run above | None that stands at HEAD. Round 1 noted that phase 1's mutate table names the wrong mutant for the routing shape `a third cell`, and showed that the case pins its own guard (read) |
| The last round (`trail/rounds/round-2.md`) | It confirms round 1's four findings and finds the base merge resolved for both sides. It opens no finding | The tree at HEAD. Round 1's findings 1, 2 and 4 read `fixed 9a06f602f`, and finding 3 reads `fixed b6425753e`. Round 2, not the sealer, is the reader of each, and `chain-check` passed the chain at the gate run (read, `gate.log`). The last record holds no `fixed` finding for the sealer to read | None |
| The changelog (`changelog.md`) | Four *Fixed* bullets, two *Changed* bullets for the four-space row and the even-run row, and three *Removed* bullets | The diff and the shape probe above. The six markers it counts are search 1's six lines at the base | None. Its *Removed* list leaves out `passages.py#_heading_level`, a private helper with no caller, which phase 3 records. Omitting it leaves no claim false |
| The orchestrator's part of the pull request body (`pr.md`, above `## From the records`) | Two quotes of `frame/plan.md` *Judgments of the run*, `Closes #1574.`, and the attribution line | Both quotes stand word for word in the plan's Judgment cells (read). Issue #1574 is the issue this work item closes. `seal pr-body --check` exit 0 | None |

```seal
target: bf5cd5cd3e67602c531e1e63817823bf190978a2 against 74ba63423339693a36e063e890e4878b9e160285
Verdict: sealed
```

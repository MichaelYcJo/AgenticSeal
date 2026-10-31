# Review round 11: 1793411151-judgment-where-meaning-is-the-question

target: 20160b89, fixes 07b9f3f8..20160b89

This is the verifying round over round 10's fix pass. It reads the fix
diff `07b9f3f8..20160b89` alone. That diff holds `58d9c003` (finding 1 and
the orchestrator's extra ask), `abb459a9` (the fix pass's answer) and
`20160b89` (the orchestrator's fold of `frame/design.md:55` and one row of
`frame/plan.md` *Judgments of the run*). This round read `20160b89` as a
new unit. Outside the diff it opened only the code the diff's cases call
into: `hooks/lib/routing.py#rounds_unreadable` and `#_ordered`,
`skills/settle/scripts/rule_changes.py#headings`, and
`skills/verify/scripts/unverified_check.py#live_lines`. The repository
declares no `seal/parity.md`, so this record holds no `original:` line.

Carried from round 10 and not re-derived: that `rules.headings` takes the
plan's live headings once for both the naming and the read of the exact
section, and that before `58d9c003` the `comments=False` mutant and the
absent-section mutant survived the module's 90 cases. Re-derived this
round: what `rounds_unreadable` does for a directory `os.listdir` refuses
(`hooks/lib/routing.py:637-644`), what `headings` passes to `live_lines`
(`skills/settle/scripts/rule_changes.py:82-91`), the module's count, each
mutant below, and every verdict.

The spawn prompt and the answer in `abb459a9` were read as claims. The
answer claims each new case went red under its own mutant, the unlistable
row went red under two mutants, and the module runs 93 of 93. This round
ran all of it again in a clone at `20160b89`, and each claim held
(executed). The prompt says the `os.listdir` patch is unverified on
Windows. That stands, and it is a row of `## Not judged`.

## Findings

This round opens no finding.

## Confirmations

confirms: round-10#1
The close `fixed 58d9c003` holds. `58d9c003` adds
`test_accepts_a_near_heading_inside_a_comment_without_a_word` and
`test_a_near_heading_is_named_beside_the_section_it_is_not` to `Test_main`
(`tests/skills/test_settle.py:1061-1099`, read). Both match round 10's
paste-ready cases. The one change is the one the answer names: the second
case asserts the whole `not read:` line, ending "so none of its rows were
read". That is the `NEAR_JUDGMENTS` text at
`skills/settle/scripts/settle.py:123-126` (read). Round 10's two mutants
were run again under `bin/seal mutate` against the two cases at
`20160b89`. `rules.headings(lines, comments=False)` is red, and naming a
near heading only where the exact section is absent is red (executed). The
docstring at `settle.py:521-523` now says a heading inside a fence or an
HTML comment is no heading and cites `unverified_check.py#live_lines`. That
function stands at `skills/verify/scripts/unverified_check.py:533`, and
`headings` hands it `comments=True` by default (`rule_changes.py:82-87`,
read). So the docstring states the scope the code reads. The citation
module passes 43 cases (executed).

confirms: none
The orchestrator's extra ask closes round 10's fourth `## Not judged` row.
The unlistable `trail/rounds` branch of `routing.rounds_unreadable` now has
a case, the third parameter of
`test_a_work_item_whose_rounds_cannot_be_listed_is_not_counted_as_none`
(`tests/skills/test_settle.py:961-1012`, read). It makes a real directory
holding `round-1.md` and commits it. It then patches `os.listdir` to raise
`PermissionError` for that one path, compared through `realpath` and
`normcase`, and restores it through `monkeypatch`. Without the patch, the
work item would print `1 round`. Three runs show the row reaches the
branch. First, with `os.listdir(where)` at `hooks/lib/routing.py:641`
replaced by `pass`, the row is red at its first assertion, not by a crash:
`_ordered` catches the `PermissionError` as `OSError`
(`routing.py:554-568`, read), and the dry run prints a count in place of
the name (executed). Second, with settle's `rounds_unreadable` check
removed, the row is red (executed). Third, the same `routing.py` mutant
survives `test_settle.py` and `tests/hooks/test_routing.py` with this row
deselected, 147 passed (executed). So the row covers what its group does
not.

confirms: none
Each new test was read against its group. The comment case is the only
case red under `comments=False`. The fence case beside it survives that
mutant, because a fence is not read as live under either value. The
beside-the-section case is the only case red under the absent-section
mutant. The three parametrised near headings each hold no exact section,
so they cannot tell the two forms apart. The unlistable row is the only
case red under the `routing.py` mutant (executed, above). The module
declares `TARGET = "skills/settle/scripts/settle.py"`
(`tests/skills/test_settle.py:47`, read). `seal layout --pairs` prints no
pair naming `test_settle.py`, and `seal layout --check` refuses nothing
(executed).

confirms: none
`20160b89`'s fold says what `58d9c003` built. *Scope* item 12
(`frame/design.md:55`) now names "a live heading near *Judgments of the
run*, one outside a fence and an HTML comment", which is round 10's wording
and the scope `headings` reads (read). The rest of the line is unchanged
(executed, `git diff 07b9f3f8..20160b89`). No other sentence stood on the
fence-only fact. `git grep` over `skills`, `docs`, `hooks`, the work item's
records and `CHANGELOG.md` found each other statement of the near-heading
naming, and none of them names a scope: `settle.py:44-46`,
`skills/settle/SKILL.md:191-193`, `changelog.md:3`, and Table A's
`seal settle` row at `frame/design.md:298` (executed, then read). The new
row at `frame/plan.md:91` says the fix pass named the frame sentence as
stale. The answer in `abb459a9` does so in its last sentence (read). Its
`Judged against` cell names *The fix pass then finds what the fixes left
standing*, which stands as the bold lead at
`skills/code-review/orchestration.md:71` (read). `20160b89` changes
`frame/design.md` and `frame/plan.md` alone, as its message says
(executed, `git show --stat`).

confirms: none
`abb459a9` changes two lines of `trail/rounds/round-10.md`: it sets the
finding's verdict to `fixed 58d9c003` and fills its answer (executed,
`git show --stat` and the diff). `58d9c003` touches
`tests/skills/test_settle.py` and `skills/settle/scripts/settle.py`, both
named in the finding's `location:` (executed). `test_settle.py` runs 93
cases, and all pass at `20160b89` (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and `seal gate` over the branch. `gaps.md` labels them `unverified`, and this round leaves nothing open, so they come due now | the branch at `20160b89` | the orchestrator, by `seal gate --base release/v0.26.0 --record` |
| The crafter's 199-module run, not re-run here. This round ran `test_settle.py` whole, `tests/hooks/test_routing.py` under one mutant, the citation module and five mutants of its own | `skills/settle/scripts/settle.py`, `hooks/lib/routing.py`, `tests/skills/test_settle.py` | the orchestrator's broad run |
| The new cases on Windows, the unlistable row above all. Its patch matches the path `routing.py` hands `os.listdir` through `realpath` and `normcase`, and it ran on macOS only. `gaps.md`'s Windows row still names "two judgments cases", and the module now holds more than that. The row's answer, the Windows legs of CI, reads the whole module either way | `tests/skills/test_settle.py:961-1012`, `tests/skills/test_settle.py:1061-1099`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/gaps.md` | the orchestrator, at the Windows legs of the pull request's CI run |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the repository at `20160b89` under the round's scratch directory, then `bin/test tests/skills/test_settle.py -q -p no:xdist` | 93 passed |
| `bin/seal mutate hooks/lib/routing.py --replace "            os.listdir(where)" "            pass" --tests "bin/test tests/skills/test_settle.py -q -p no:xdist -k unlistable"` | red: the unlistable row failed at its first assertion, a count printed in place of the name |
| `bin/seal mutate skills/settle/scripts/settle.py` with three pairs: the `rounds_unreadable` check removed, `rules.headings(lines, comments=False)`, and naming only where the exact section is absent; `--tests "bin/test tests/skills/test_settle.py -q -p no:xdist -k 'unlistable or inside_a_comment or beside_the_section'"` | baseline passed; mutants 1, 2 and 3 red |
| `bin/seal mutate hooks/lib/routing.py` with the same `pass` pair, `--tests "bin/test tests/skills/test_settle.py tests/hooks/test_routing.py -q -p no:xdist -k 'not unlistable'"` | SURVIVED, 147 passed and 1 deselected |
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist` | 43 passed |
| `bin/seal layout --pairs`; `bin/seal layout --check` | no pair names `test_settle.py`; 153 files read, 0 refused |
| `git show --stat` of `58d9c003`, `abb459a9` and `20160b89`; `git grep` for the near-heading sentences over `skills`, `docs`, `hooks`, the work item and `CHANGELOG.md` | each commit touches the files its message names; no other sentence states a scope for the near-heading naming |

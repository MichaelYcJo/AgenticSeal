# Review round 2: 1794178397-a-durations-refresh-costs-no-round

```seal
target: fc0b4b28, fixes f237ce30..fc0b4b28
```

This is the verifying round after round 1's fix pass. The code under review
is the diff from `f237ce30` to `fc0b4b28`. It holds three commits: the
record commit `5b9d0ce4`, the fix `e1658160` and the close commit
`fc0b4b28`. The round worked in a scratch clone at `fc0b4b28`. It read the
issue (#1444, no comments), `routing.md`, the three frame files, `gaps.md`,
`changelog.md` and `pr.md` whole at the target, and both phase records for
their coordinates. No `seal/parity.md` is declared.

Carried from round 1 and not searched again: where `REMEDY` stands
(`.github/scripts/durations_union.py:78-89`), that `main` appends the
verdict's sentence to `$GITHUB_STEP_SUMMARY`, that `cmarkgfm` is the
renderer the `pytest` job pins (`.github/workflows/test.yml:150`), and the
seven fixture cases `frame/design.md` *Removes* row 4 names. Round 1's
confirmations of the workflow expressions, `CONTRIBUTING.md` and the census
of the old schedule cover files the fix diff does not touch, so this round
did not reach them again. Every verdict below was reached again on the
target.

The orchestrator's account was read as a claim. It said `5b9d0ce4` commits
round 1's record and `fc0b4b28` commits the close blocks. `git show --stat`
gives `5b9d0ce4` as 172 lines added to `trail/rounds/round-1.md` alone, and
`fc0b4b28` as 15 lines added to the same file: three close blocks of five
lines each (read). It said `e1658160` also rewrote the test module's
docstring at lines 18-19. The commit's diff holds that hunk and changes
three files in all: the script, the test module and `gaps.md` (read).

## Findings

No finding this round.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `REMEDY` now writes `` `<dir>/.test_durations` `` in a code
span (`.github/scripts/durations_union.py:82`). The `said` tuple of
`Test_verdict::test_refuses_one_more_unpriced_naming_the_counts_and_the_remedy`
pins the backticked words (`tests/github/test_durations_union.py:364`).
Round 1's probe was written again from its *Probes* row. It rendered
`durations_union: ` plus the 51-of-1,000 verdict sentence through
`cmarkgfm.github_flavored_markdown_to_html` in safe and in unsafe mode. Both
outputs read `then move <code>&lt;dir&gt;/.test_durations</code> over the
committed`, and neither holds "raw HTML omitted" (executed). The close
claims the case was seen red with the bare path back. With line 82 edited
back to the bare `<dir>/.test_durations`, that case alone failed, on "the
sentence does not say move `<dir>/.test_durations` over the committed
.test_durations" (executed). The file was restored afterwards. `git grep`
for `<dir>/.test_durations` outside the work item's round records finds
only the script, its case and `CONTRIBUTING.md:187`, each in a code span.
No other string literal of the script carries a bare `<` (executed).

```seal
confirms: round-1#2
```
What holds: `gaps.md:23-37` now names eight entries. The round rebuilt the
list from the diff. Every `def test_` that `git diff 94d04d30..fc0b4b28 --
tests/` removes and does not add back gives exactly the eight names the
paragraph lists (executed). `grep -n` finds each once in `.test_durations`,
at lines 1223 to 1227, 1229, 1231 and 1234. Their seconds sum to 0.0291, so
"Together they hold 0.029 s" holds (executed). The paragraph says phase 2
removed all eight. Only `554c24e3`, phase 2's first commit, removes a
`def test_` from the behaviour module, and it removes eight (executed). The
seven fixture names match *Removes* row 4 of `frame/design.md:91` one for
one (read).

```seal
confirms: round-1#3
```
What holds: `Test_staleness` keeps two cases
(`tests/github/test_durations_union.py:315-332`). Each assertion of the
deleted case still stands in another case. The dead ids stay out of the
unpriced list: `test_accepts_the_union_and_the_file_and_names_each_side_in_order`
asserts the exact `unpriced` and `dead` lists. The seconds side fails while
"have no price" stays absent:
`Test_verdict::test_refuses_one_more_dead_second_naming_the_seconds_and_the_first`.
`verdict` writes "have no price" and "First unpriced" under the one
`unpriced_share > STALE_SHARE` guard (`.github/scripts/durations_union.py:231-237`),
so that case's absence assertion holds both (read). The base case the
deleted one rewrote, `test_an_entry_nobody_collects_is_not_counted`, asserted
nothing beyond these (read, `git show 94d04d30:` of the behaviour module,
lines 404-417). So *Removes* row 4's "each is rewritten as a case of the
script's function" still holds for that row: its facts stand in
`Test_staleness` and `Test_verdict`. The `module` parameter of `priced`,
which the deleted case used, is still used by three `Test_verdict` cases
(`:344`, `:380`, `:393`; read). The plan row's three modules passed with 60 cases and 1 skip, one
fewer than round 1's 61, which is the deleted case (executed).

What matched: the docstring rewrite at
`tests/github/test_durations_union.py:18-19`, which round 1 named under
*Confirmations*. It now says `Test_verdict` sits at the share's boundary on
a thousand cases. `Test_verdict`'s boundary cases build on `FIXTURE_SIZE`,
which is 1000 (`:110`), and `AT_THE_SHARE` (`:111`). No case of
`Test_staleness` uses either (read).

What matched: the records read whole at the target. `routing.md`, the three
frame files, `changelog.md` and `pr.md` are unchanged since `f237ce30`. The
one record the fix changes is `gaps.md`, and the target contradicts no
sentence of it. `pr.md` quotes four sentences of `changelog.md`, one of
`frame/plan.md` and one of `gaps.md`. Each stands word for word at its
source, with runs of whitespace collapsed (executed). `gaps.md:9`, the row
`pr.md` quotes, did not move in the fix. The phase records name
`test_accepts_an_entry_no_part_ran_as_dead_and_never_unpriced`
(`trail/phases/phase-1.md:140`) and one leftover entry
(`trail/phases/phase-2.md:109`). Each states the commit it names, so the target
does not contradict them.

What matched: `gaps.md` *Not done*'s eight functions. `bin/seal layout
--check` exits 0 and reports exactly `arguments`, `durations_map`, `emit`,
`find_parts`, `read_map`, `rendered`, `report` and `union` for
`durations_union.py`, as round 1 found (executed). The fix diff adds no
test, so no new case is read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether GitHub evaluates `github.base_ref == 'main' && '--stale-fails' \|\| ''` to the switch on a pull request into `main` and to nothing elsewhere, and whether `hashFiles('union/.test_durations')` matches the dot-named union file. The fix diff does not touch them, and no run evaluated either. | `.github/workflows/test.yml:214-215`, `gaps.md:9` | a measurement: this branch's pull request run and 0.36.0's release pull request, read by the orchestrator |
| Whether the verdict reads a real four-part union and renders in a real step summary. The probe rendered the sentence through `cmarkgfm`, not on GitHub. | `gaps.md:8`, `frame/questions.md` Q1 | a measurement: the `durations` job on 0.36.0's release pull request, read by the orchestrator of that release |
| The full suite, the repository-wide lint and the format check at the target; `unverified`, which `gaps.md:7` labels honestly | the branch | the orchestrator, at the broad gate |

This round leaves nothing open. What comes due is the orchestrator's broad
run at `fc0b4b28`, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_tmp_summary_render.py -q -p no:xdist -s`, which rendered the 51-of-1,000 verdict sentence through `cmarkgfm` in safe and unsafe mode; the file was deleted afterwards | exit 0; both modes give `<code>&lt;dir&gt;/.test_durations</code>`, and no "raw HTML omitted" |
| `.github/scripts/durations_union.py:82` edited back to the bare `<dir>/.test_durations`, then `bin/test tests/github/test_durations_union.py -q -p no:xdist`, then `git checkout` of the file | exit 1; 1 failed, `Test_verdict::test_refuses_one_more_unpriced_naming_the_counts_and_the_remedy`, on the `said` line; 24 passed |
| `bin/test tests/github/test_durations_union.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/text/test_ci_gives_the_checks_what_they_need.py -q` | exit 0, 60 passed, 1 skipped |
| `git diff 94d04d30..fc0b4b28 -- tests/` for every removed `def test_` not added back, then `grep -n "::<name>\""` on `.test_durations` for each, and a sum of their seconds | eight names, one line each, 0.0291 s together |
| `bin/seal layout --check` | exit 0; the eight functions of `durations_union.py` `gaps.md` names |

# 1792129100-the-mechanics-leave-before-the-agents-are-rewritten — review round 3

target: 5242643b, fixes 8de484b4..5242643b

The verifying round on round 2's fix pass: two commits, 6597fe14 and
5242643b, read in a `git clone --no-local` of the checkout at 5242643b.
Rounds 1 and 2 were carried for their coordinates; the verdict below was
re-derived from the fix diff and the tree. This is the last round under the
default cap of three.

Round 2's one finding is closed, and this round opens nothing. The fix took
the first of round 2's two repairs: `confirmations` now counts a section
left out, and the loader refuses only the rows the check reads a meaning
from, now on both axes, place and count. The smith's enumeration of 13
`Where` and `How many` combinations was recounted from `grammar_row` and
then executed one combination at a time; every one holds.

The narrow modules named in the probes were run. The full suite was not run
by this round: it is `unverified` here, and the sealer answers it. With
nothing left open, what comes due is the sealer's spawn.

## Findings

None. No unit the fix diff added or changed holds a defect this round could
find, by reading or by execution.

## Confirmations

confirms: round-2#1
The class is closed, and the hand-back's count is right. Recounted by
construction from `grammar_row` (`skills/code-review/scripts/chain_check.py:355-408`):
the two section rows in `the record` at `one` or `at most one` (`:388`),
the finding heading in `## Findings` at `each number once` (`:390`), an old
spelling `nowhere` at `none`, and a label in each of three places at each
of `one`, `at most one` and `any` (`:396`). That is 2 + 1 + 1 + 9 = 13
combinations, and `grammar_row` admits no other.

Executed (probe P1). Each combination was loaded from a scratch copy of the
plugin layout, with a new label `x:` for the nine label combinations and the
document's own rows for the rest. Each was then fed a record holding none,
one, two and a misplaced line, and, for `## Confirmations`, a record with
the section left out. All 13 are kept by their reader: `one` refuses none,
`one` and `at most one` refuse two, `any` refuses neither, and a line in
another place is refused. A label at `one` in `## Confirmations` with the
section absent is refused, "no `x:` line: `## Confirmations` carries one",
and `## Confirmations` itself at `one` is refused, "no `## Confirmations`
section". At `at most one` and at `any`, the absent section still passes.
Three of the probe's 121 checks disagreed with the probe and not with the
code. They expected a label placed `outside every finding` to be refused
inside `## Confirmations`. That section is outside every finding, so the
check is right to accept it, and `record_lines` counts the line there.

Executed (probe P1). The read rows were checked on both axes. Each of the
six rows `target:`, `location:`, `verdict:`, `regression:`, `reopens:` and
the row for `confirms:` was put at each of 3 places and 3 counts, 54
tables. Each table
loads exactly where `READ_ROWS` (`chain_check.py:132-143`) gives that
`Read`, and is refused at load everywhere else, by place first and then by
count. Where a `Read` admits a count the document does not use, the reader
keeps it: `regression:` or `reopens:` at `one` refuses a finding without
the line, `confirms:` at `one` refuses a record with the section left out,
and `confirms:` at `at most one` refuses two lines.

Executed (probe T2). The five new cases fail against the pre-fix check:
`skills/code-review/scripts/chain_check.py` from 8de484b4 checked out in the
clone, the two tests selected, 5 failed and 22 passed. Three cases fail
with "DID NOT RAISE GrammarError", one with the `HONOURED` refusal of
`## Confirmations` at `one`, and one with `AssertionError: []` for the
`signed:` row. That matches the fix pass's account of its red run. The file
was then checked out at 5242643b again, and `git status` was clean.

Read. The test `test_a_section_left_out_is_counted_where_the_table_says_one`
(`tests/test_chain_check.py:1348`) is two-sided. It asserts first that the
document's own table passes the record without the section, so a reader
that refused every absent section would fail it. It then asserts one error
at line 0 for each of the two tables. `confirmations`
(`chain_check.py:1194-1234`) returns early only for a second section, and
`counted` reports a missing `one` row at index -1, so line 0 is the line
`finding_spans` already uses for `NO_FINDINGS`.

Read. The document (`docs/the-review-record.md:56-77`) and the changelog
fragment (`changelog.md:24-28` in the work item's directory) now say what
the code does. The document names each read row's place and its counts in
the same terms as `READ_ROWS`, and says that every other row may take any
place and count, because its reader counts each one. The fragment's exit-2
sentence now names the place as well as the count. Executed: `bin/rules
--check` exits 0 with the new `Enforced by:` target.

One sentence of the fix pass's `answer:` in round 2 is loose about history,
not about code: "Twelve were kept by their place's reader already". At
8de484b4, `## Confirmations` at `one` was refused at load by `HONOURED`
and not kept by its reader. Only the `## Findings` half of the section
combination was. The count of 13 and the state at 5242643b are both right,
and no agent acts on that sentence.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, repository-wide lint and typecheck at 5242643b: `unverified` in this round | the whole tree | the sealer, through `broad-gate` after the rounds settle |
| CI run 38985850726, dispatched at 5242643b, was running when this round ended and was not read | `.github/workflows/` | the orchestrator |
| `record_findings`, which `broad_gate.py` and `release_seal.py` read a record through, does not call `confirmations`, so a `## Confirmations` refusal reaches only `round_of`'s callers. That was already true at the base for every `## Confirmations` refusal, and the fix diff did not change it. Whether those two readers owe it is a question about their scope, not about this fix | `skills/code-review/scripts/chain_check.py:1184-1191` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| T1 `bin/test tests/test_chain_check.py tests/test_a_script_copied_alone_exits_2.py tests/test_the_changelog_is_gathered_at_release.py tests/test_no_real_identifiers.py tests/test_the_record_is_written_in_words.py -q`, in the clone | 149 passed, exit 0 |
| T2 `git checkout 8de484b4 -- skills/code-review/scripts/chain_check.py` in the clone, then `bin/test tests/test_chain_check.py -q -p no:xdist -k "test_a_section_left_out_is_counted or test_a_document_the_check_cannot_read_is_exit_2"`, then the file checked out at 5242643b again | 5 failed, 22 passed, 51 deselected, exit 1; clone clean afterwards |
| `bin/rules --check`, in the clone | exit 0 |
| P1 one probe file `<scratchpad>/<item>/round-3/test_tmp_enumerate.py`, run once with the clone's venv and `python -I`, then deleted with its scratch trees, loading a copy of the clone's `chain_check.py`, `unverified_check.py` and a varied `docs/the-review-record.md` per table | 121 checks over the 13 combinations and the 54 read-row tables; 118 agreed with the expectation, and the 3 that did not were the probe's own error, a label `outside every finding` standing in `## Confirmations`, which is outside every finding |
| `git grep -n -F` over `tests`, `evals`, `skills`, `docs`, `templates`, `agents`, `.github`, `hooks` and `bin` for fragments of every sentence the fix diff changed, old and new, and for `HONOURED`, `READ_ROWS` and `can honour only` | the old sentences and `HONOURED` have no reader left; the live pins are in `tests/test_chain_check.py`, run in T1 |

## Files opened

`seal/specs/1792129100-the-mechanics-leave-before-the-agents-are-rewritten/rounds/round-1.md`
(its head), `seal/specs/1792129100-the-mechanics-leave-before-the-agents-are-rewritten/rounds/round-2.md`,
the fix diff `8de484b4..5242643b` whole, `skills/code-review/scripts/chain_check.py`
(`:60-496` and `:740-1330`), `docs/the-review-record.md` (`:1-140`),
`templates/sdd-round.md`, `tests/test_chain_check.py` (its helpers
`finding`, `confirm`, `record`, `doc_with`, `row_of`, and the two changed
tests), and `bin/test`.

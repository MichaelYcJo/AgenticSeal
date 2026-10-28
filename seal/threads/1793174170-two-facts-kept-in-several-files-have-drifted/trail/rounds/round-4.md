# Review round 4: 1793174170-two-facts-kept-in-several-files-have-drifted

target: b18a8b01, fixes 5fc78725..b18a8b01

## Findings

None. The range holds four commits: `c81cb9ff` and `27b8deee`, the fix pass; `43b9f087`, the `gaps.md` row; and `b18a8b01`, the answers in `trail/rounds/round-3.md`. This round read all four and nothing outside them except the census module those commits are held to.

## Confirmations

confirms: round-3#1
The close holds. `test_every_paired_document_carries_the_same_headings` (`tests/behaviour/test_both_editions_carry_the_same_folds.py:107-119`) runs the outline comparison over every pair on disk before anything can decline. The liveness half is `unread()` (`:90-104`), the last step. Read as code, `unread()` declines only where every named pair that went unread has a deleted half in `missing`. Where some of them are explained and some are not, it returns the ones not explained and the case fails. Where every named pair was read, `absent` is empty, so a neighbour mid-edit declines nothing. That is the shape `tests/behaviour/test_no_document_names_the_old_roots.py#uncovered` has. The outline case's comparison and `assert not found` both come before the call, so a deleted edition no longer takes another pair's disagreement with it.

The case my round 3 supplied had a gap, and `27b8deee` closed it. A skip raised inside a case counts as a pass, so an unconditional decline still passed my case. The `reported()` helper (`:146-151`) now turns a decline into `pytest.fail` at each call that must report. The three calls cover the bare report, a neighbour mid-edit with both named pairs read, and one named pair lost while the other is simply not there. Each asserts what `unread()` returns for that shape (read). The module passed in this round's run with no skip (executed, `-rs` listed none).

confirms: round-3#2
The close holds. `pairs(root)` (`:60-73`) is round 3's text. It makes one `git ls-files -- *.md` call, runs `on_disk` over the whole listing, pairs a `.ko.md` only with a tracked `.md` on disk, and returns as missing only a deleted file that is a half of a listed pair. The case deletes `README.md` together with `docs/alone.md`, a file with no edition. It asserts `missing == ["README.md"]`, which pins both the English half and the filter (read, `:122-144`). The scope still makes one listing call and mentions `on_disk`, so the census row's count of 1 stays true, and the census module passed in this round's run (executed).

confirms: none
The `gaps.md` row `43b9f087` rewrote says what happened across `d91641fb`, round 3 and the fix pass. Its grounds quote `tests/conftest.py#on_disk` and name the precedent it copied (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `b18a8b01`. The review rounds leave nothing open, so this is what comes due next, then the sealer's spawn | the whole tree | the orchestrator, through `seal gate` (contract rule 2) |
| The fix pass's red-first run and its `seal mutate` table. This round read the case against the mutants it names and re-ran none | `tests/behaviour/test_both_editions_carry_the_same_folds.py` | the sealer, which samples the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/test_conftest.py tests/hooks/test_root_migrate.py tests/skills/test_seal.py -q -p no:cacheprovider -rs`, the two modules and every module `git grep -l` finds naming either | 530 passed, no skip, exit 0 |
| `bin/seal layout --check` | exit 0, 158 files read, 0 refused |

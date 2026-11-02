# Review round 2: 1793586643-the-settle-drafts-the-released-operations-literally

```seal
target: 1ad922165 against 84e810ec0
```

The target is the merge commit `1ad922165`, which merges `bf18be7d1` (#1139 as #1291 on `origin/release/v0.28.0`) into this branch at `39eced4c0`. No fix pass ran, and round 1 closed no finding, so no `confirms:`, `reopens:` or `regression:` line is owed. The round answers what `chain_check.py` cannot read in a merge commit: whether the conflict resolution kept both sides. It stays inside the merge. It reads the resolution against both parents and how the auto-merged `skills/settle/SKILL.md` and `tests/skills/test_settle.py` read together. No `seal/parity.md` is declared, so no `original:` line is owed.

Carried from round 1, not re-established: the coordinates of `settle.py#draft`, `rule_changes.py#apply_op` and the S8 replay. They carry because the merge changed none of them. `git diff 84e810ec0 1ad922165 -- skills/settle/scripts/rule_changes.py` is empty, and the body of `settle.py#draft` is byte-identical at both commits (both executed). Its line numbers moved: `draft` now stands at `skills/settle/scripts/settle.py:1553-1589`, and the refusals at `:1747-1755`. Every verdict below was reached this round.

Claimed by the orchestrator: three files conflicted, each resolved keeping both sides; `skills/settle/SKILL.md` and `tests/skills/test_settle.py` merged clean; seven narrow modules passed, 535 tests. The first two claims were checked through `git show --remerge-diff 1ad922165` (executed), which sets the resolution beside git's own conflicted merge. The 535 was not re-run as given. This round ran its own eight modules, listed under `## Probes`.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: none
```
What matched: the `seal settle` row of `README.md` keeps both sides. In the remerge diff (executed), the resolved row is the base side's row with one sentence added, this branch's `--draft` sentence, placed before `--apply refuses --from` as this branch had it. Every other word of the base side's row stands: the `--apply` text naming the published GitHub Release note, the pull request link, and *What `--apply` does*. The branch side's older `--apply` ending ("and names any it keeps") is gone, and the base side's ending replaces it. Nothing is lost, because the base side's sentence states everything the older one did.

```seal
confirms: none
```
What matched: the `seal settle` row of `README.ko.md` has the same shape. The resolved row is the base side's row with the branch's two `--draft` sentences inserted before the `--apply` sentence, in the order the English row gives them. `tests/behaviour/test_both_editions_carry_the_same_folds.py` passed in the clone (executed).

```seal
confirms: none
```
What matched: the exit-code paragraph of `settle.py`'s module docstring keeps both sides. Read at `skills/settle/scripts/settle.py:147-162`: exit 0 names `--draft` ran, whatever it placed (branch); exit 1 names a published note that does not carry its entry (base); exit 2 names the release list `gh` cannot give and the unreadable `git` (base) and `--draft` beside `--apply` or `--from` (branch, auto-merged). Each clause matches the code. `main` returns 2 for each draft refusal at `:1747-1752` before the root is resolved. `apply`'s `Unasked` and `Unread` return 2 at `:1821-1828`. `draft` returns 0 at `:1589`.

```seal
confirms: none
```
What matched: `main` runs `--apply` as #1139 built it and `--draft` as round 1 confirmed it. Read at `skills/settle/scripts/settle.py:1820-1830`: the `try` around `apply` with its two `except` arms is the base side's, byte for byte in the remerge diff. The `if args.draft` branch follows it, as it followed the bare `apply` return on this branch. The two arms cannot meet. `--draft` beside `--apply` is refused at `:1747`, before either is reached. `draft` (`:1553-1589`) calls neither `published_releases` (`:496`) nor `notes` (`:574`), which raises `Unread` at `:615`, so the `try` needed no arm for it. The merged `skills/settle/SKILL.md` agrees in four places. *Shared mode* says `gh` is asked "only in `--apply`". *What `--draft` writes* says it "reads what the dry run reads". *What `--apply` does* says "The dry run reads no note". Its exit-code sentence names 2 for a note that cannot be checked.

```seal
confirms: none
```
What matched: the auto-merged `skills/settle/SKILL.md` reads as one text. `git diff 39eced4c0 1ad922165` and `git diff bf18be7d1 1ad922165` over it (both executed) show each side's hunks landing apart, and each passage was read in place. The usage block lists `--draft` before `--apply`, and `--apply` carries the base side's note clause. Step 11 of the procedure carries the branch's "each operation the draft did not place" and the base side's "each directory `--apply` kept for its note" in one sentence that still reads in order. No sentence of one side states a fact the other side changed.

```seal
confirms: none
```
What matched: the auto-merged `tests/skills/test_settle.py` keeps both sides' cases. The module docstring names #1139's note check and #1217's `--draft`. The branch's `--draft` cases (`:2224`, `:2685-2770`) are present beside the base side's note cases. The one case the base side removed, `test_shared_mode_never_asks_gh`, has a replacement at `:1728`, `test_shared_mode_asks_gh_for_no_note_it_cannot_read`. That case covers the dry run and `--apply` but not `--draft`, and neither parent covered `--draft` there either. `draft` reads no `gh` (`skills/settle/scripts/settle.py:1553-1589`, read), so the gap leaves no behaviour unpinned that the merge could have changed.

```seal
confirms: none
```
What matched: the narrow modules pass at the target. In a `git clone --no-local` at `1ad922165`, `bin/test` over eight modules exited 0, with 384 passed and 9 skipped (executed): `tests/skills/test_settle.py`, `tests/skills/test_rule_changes.py`, `tests/text/test_settle_reads_before_it_removes.py`, `tests/behaviour/test_settle_applies_rule_changes_in_place.py`, `tests/behaviour/test_no_document_names_the_old_roots.py`, `tests/behaviour/test_both_editions_carry_the_same_folds.py`, `tests/github/test_publish_release_note.py`, and `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`. This is a probe of the slice the merge touched, not a seal.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `1ad922165`. The suite stays `unverified`; `trail/gate.md` and `guarantee.md` name `84e810ec0`, not this merge. | the whole tree | the orchestrator, at `seal gate` at HEAD, then the sealer's spawn after it |
| #1139's own changes that the merge brought in without a conflict (`.github/scripts/publish_release_note.py`, `skills/implement/`, `templates/setup/`, the `seal/` README) | outside this round's target | #1139's own rounds and sealer, which reviewed them on the base |

## Probes

| Command | Result |
|---|---|
| `git show --remerge-diff --format= 1ad922165 -- README.md README.ko.md skills/settle/scripts/settle.py skills/settle/SKILL.md tests/skills/test_settle.py` | conflicts in the three files the orchestrator named, and no remerge hunk for `SKILL.md` or `test_settle.py`; each resolution is the base side's text with this branch's `--draft` text added, and nothing of either side dropped |
| `git diff 84e810ec0 1ad922165 -- skills/settle/scripts/rule_changes.py`, and `settle.py#draft` extracted at `84e810ec0` and at `1ad922165` and compared with `diff` | empty diff; `diff` exit 0 |
| `bin/test` over the eight modules named under `## Confirmations`, `-q`, in a `git clone --no-local` at `1ad922165` under `<scratchpad>/1793586643-the-settle-drafts-the-released-operations-literally/round-2/clone` | exit 0; 384 passed, 9 skipped |

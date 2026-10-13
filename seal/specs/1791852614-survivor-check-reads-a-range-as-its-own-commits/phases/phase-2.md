# 1791852614-survivor-check-reads-a-range-as-its-own-commits — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 68071552 |
| Ran by | unknown — the spawn prompt named no agent or model for this row, and this record transcribes only what it was given |

## What this phase was asked

`plan.md` phase 2: one unit reading each own commit and its parent at the
commit's changed paths intersected with the two-ends list, returning the
pairs lost and gained; `corrected` keeping a `gone` and a `fresh` sentence
only where the pairs hold it, on a two-dot range, before the pairing across
paths; `A...B` unfiltered; `examine` and `survivors` carrying the input. S1,
S2, S3, S4 and S6 seen red first, saying which mutation turned which; the
path-list case counting and classifying the new list (S10); `Reads:` on
`corrected` and the unit, census lines removed; Q1 measured and answered.

## What this phase found

- **The unit is `own_changes(root, own, paths)`.** It counts each own commit
  against its parent the way `corrected` counts a file between the two ends,
  a changelog's newly released sentences held included, so on a range whose
  every commit is its own, every sentence `corrected` counts is in a pair and
  the filter keeps everything. `corrected`, `examine` and `survivors` take
  `own=None` last, so a caller that names no own commits, and `A...B`, read
  exactly as before. `examine` and `survivors` changed, so they declare too
  and left the census beside `corrected`.
- **The frame's fixture was one commit short of its own description.** As
  first built, `f1` wrote `f.md` and `f2` rewrote it, so `f2` removed `f1`'s
  sentence and the report said one sentence removed, which is true. Each
  commit now adds a file no other commit touches. The same change fixed S3's
  control: with the default file written only when the case passed none,
  the two histories differed by one file at the tip, and the pool size moved
  the score from 1.81 to 1.80.
- **S3 compares two histories with the same tree at the tip.** The spec's
  *the same score as on a history without `S1`* cannot be met literally: the
  sentence `S1` writes is in the pool at the tip and moves every phrase's
  weight. So the control is the history where the same sentence stood in
  `root`, before the range, and the case asserts the two scores are equal.
- **S10.** `own_commits` is counted by the name called
  (`LISTS_PATHS_BY_NAME`), since the call carries no constant; `owned` is
  its one site, and `INTERSECTED_WITH_THE_RANGE` classifies it as filtered
  by `own_changes`' `& set(paths)`, asked of `corrected` alone with
  `corrected`'s `paths`. Dropping the intersection is red.
- **How each case was seen red.** Against the old code (the pass switched
  off in `corrected`): S1, S2, S3 and S4. Gone unfiltered: S1 and S4. Gone
  dropping every sentence: S2. A filter of `gone` alone: S3. A per-path
  restriction (alternative D): S4. The pass applied to `A...B`
  (alternative F): S6. Each through `bin/mutation-check` on the committed
  file.
- **Mutations of `own_changes`.** Red: the intersection dropped (the
  path-list case), `lost` not collected and the parent read as the commit
  itself (S2, S3, S4), `gained` not collected (four cases of the survivor
  module, among them the round-record and phase-record cases), the
  changelog's released sentences not held per commit
  (`test_a_release_that_rewords_an_entry_still_reports_its_verbatim_copy`).
  SURVIVED: the `if not mine: continue` skip, because `read_blobs` already
  returns nothing for no paths. It was removed in `68071552` rather than
  kept as a unit nothing watches.
- **Q1, measured** with a scratch script calling `owned`, `examine` with
  and without the list, and `own_changes` alone, on this repository:

  | Range | Own commits | `own_changes` alone | A run |
  |---|---|---|---|
  | `d2b76587..27920e58` (1791384160 round 1's `Fix range`) | 2 | 0.92 s | 27–28 s |
  | `24cfb66f..fadd8270` (round 2's) | 2 | 0.46 s | 6.5–6.9 s |
  | `6445933a..76de29c3` (round 4's) | 2 | 0.28 s | 6.9–23.6 s |
  | `5f11923f~40..5f11923f`, 24 merges | 169 | 54.95 s | 23.4 s without, 89.0 s with |

  Every range reported the same rows and the same count with the pass and
  without it. On a fix pass's range the pass is a small fraction of the run,
  so the answer is (a), no skip. The one range where it dominates holds
  merges, so a skip for a range with no merge would not reach it either;
  its spelling for a whole branch is `A...B`, which does not run the pass.

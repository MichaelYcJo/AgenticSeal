## Fixes

| # | Verdict | Commit or grounds |
|---|---|---|
| 1 | fixed | d2eed6d1 — with no payload and no `gh` answer the check reads the state as unknown, does not judge it as a ready pull request, and names every source tried; a payload that cannot answer stays ready; a record `new`, `close` or `seal` writes mid-run is not failed for it; the sealer advice says *once the rounds have settled*; `docs/round-record-spec.md` §*`Pass` has to be checked* and `docs/review-chain-spec.md` say so, and the `stop before the pull request` reading is `questions.md` Q1 with the default unknown |
| 2 | fixed | d2eed6d1 — the suite's `gh` stub defaults to the unknown answer; the ten helpers that mean a ready pull request say ready through `gh_answers`, the two ready-named cases among them now run ready, and the generator is pinned under the unknown state |
| 3 | fixed | d2eed6d1 — `rounds_rows` hands `says_reopened` `reader.visible(needs).strip()`, the gate's string; U+200B and U+FEFF cells pinned |
| 4 | fixed | d2eed6d1 — `deferred_parts` cuts the note from the cell as written (`DEFERRED_HEAD_RE`) and takes `HOME_MARKS` off the home alone; the reviewer's two cells added to S2 |
| ⬜ 5 | answered | a note, left as it stands: `gh pr view` picks the PR by branch name and answers a merged PR as not draft; only a hand-run `chain_check` meets it, and CI always reads the payload |
| ⬜ 6 | answered | a note, left as it stands: `--sealing` excuses only the last record's `Broad gate` cell and prints that it did; CI never passes it |

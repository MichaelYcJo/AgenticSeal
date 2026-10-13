# 1791852614-survivor-check-reads-a-range-as-its-own-commits — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 3a7bd455 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

`plan.md` phase 4: `changelog.md`; the ledger fragment with a row per
scenario; `evidence-check --reverify --into` for every released row whose
anchor on `corrected` or `parse_range` moved; `overview.md` with its
divergences and *Not verified*; `survivors.md` only where the branch's own
run reports a place; `phases/phase-N.md` for each phase. Verified by
`bin/evidence-check --strict`, `survivor-check --range
origin/release/v0.21.1...HEAD` with the item's `survivors.md`, and the
hygiene modules.

## What this phase found

- **The drift reached further than the two anchors the plan named.** At
  `613e6e2d`, `evidence-check --strict` named 71 drifted rows: 40 on
  `corrected`, 28 on `test_the_rules_have_one_owner.py#RULES`, 2 on the
  path-list case and 1 on the home section. `parse_range`, `main`,
  `examine` and `survivors` were cited by no released row. Each row's claim
  was read before `--reverify --into` wrote 27 citing rows. Two claims no
  longer held as written, 0.9.3's `S3` and 0.11.2's `S2`, and those two
  rows became `Corrected ·` rows (`overview.md` says why).
- **An evidence cell that names a file and a line in backticks reads as an
  old-format coordinate.** The first `--strict` run after the fragment
  refused one cell for that reason, and the cell now says it in words.
- **No `survivors.md`.** The sweep over the branch reported nothing, in both
  spellings: `origin/release/v0.21.1...HEAD` and `321e9de1..HEAD`, the
  second running the own-commits pass over this branch's own commits.
- **The runs at `3a7bd455`:** `bin/evidence-check --strict` exit 0, 8506
  ok; `bin/survivor-check --range origin/release/v0.21.1...HEAD` exit 0, 4
  sentences removed and none standing; `bin/unverified-check --baseline
  origin/release/v0.21.1` exit 0, this item's three rows open; the hygiene
  modules (`test_docs_line_wrap`, `test_no_passage_is_pasted_into_a_second_file`,
  `test_one_word_one_meaning`, `test_no_real_identifiers`,
  `test_release_hygiene`, `test_a_document_has_room_for_the_next_fold`,
  `test_a_folded_statement_names_what_enforces_it`) with the registry check,
  278 passed, exit 0.

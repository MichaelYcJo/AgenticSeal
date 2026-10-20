# 1792459424-docs-states-the-current-rule-in-one-read — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 4b40d109 |

## What this phase was asked

The `<!-- specs/<id> -->` lines out of `docs/`, with the readers that exist
only for them: the marker arm of
`tests/test_both_editions_carry_the_same_folds.py`, the marker exemption of
`tests/test_docs_line_wrap.py`, the `CONTRIBUTING.md` sentence requiring the
same fold markers in both editions, and `unverified_check.py#FOLD_MARKER`
where no reader is left.

## What this phase found

- **125 marker lines left, not 127.** Phase 1 removed two with the two
  statements whose subject went. Each was removed with a `replace_all` edit
  per id and file, and the diff deletes 125 lines and nothing else. One
  marker stood directly under a prose line in `docs/branch-and-release.md`;
  a comment line interrupts a paragraph, so without it the two paragraphs
  ran together, and a blank line now separates them.
- **`FOLD_MARKER` is gone from `unverified_check.py`.** Its last reader in a
  test, `tests/test_unverified_rows_close.py#live_markers`, pins `live_lines`
  on marker shapes and now holds its own line-anchored pattern, the one
  `gather_changelog.py` writes. `tests/test_one_word_one_meaning.py` blanked
  markers before its word sweep; after this phase the only marker holding the
  old word is in `changelog/`, which the sweep excludes, so the blanking and
  its pattern went, and the pact span it cut is now found by the statement's
  bold opening.
- **Cases that cut a section at a marker now cut at a statement's opening:**
  the stamp section's three cases, the commit gate's refusal case, the
  release tail's, and the liveness statement's. The gate-failure case and
  the stamp cases no longer assert a marker is present.
- **Prose that stated the marker fact was corrected:**
  `docs/the-record-layout.md`'s editions rule (heading levels alone) and its
  liveness bullet (a changelog marker as the example), the wrap-limit
  statement for a marker (removed with its exemption), and
  `docs/the-pact.md`'s sentence keying a marker by the work item id.
- **A phase 1 conversion was wrong, and this phase found it.**
  `tests/test_the_release_tail_does_not_end_at_the_tag.py` pins the record
  line of the third-reader paragraph of `docs/branch-and-release.md`. That
  `nothing` line stood under another paragraph at the base, so phase 1 wrote
  `check: none reader: review` there and dropped its reason. The reason is
  back under the paragraph it describes, as a prose sentence and
  `check: none reader: the main ruleset on GitHub`, and the misplaced line is
  gone. Phase 1's boundary run had not read that module: it names no label
  and holds no node id.
- **The checks at the boundary (executed):** `git grep -c '<!-- specs/' --
  docs` printed nothing, exit 1; the 73 modules that read a changed document
  or were touched, with the meta modules, 4000 passed and 2 failed, and both
  passed after their cut points were moved; `bin/rules --check` exit 0 over
  240 lines; `bin/fold-check` exit 0; ruff clean over the 10 changed Python
  files; the three rewritten helpers were each mutated once, and each run was
  red.

# 1791852614-survivor-check-reads-a-range-as-its-own-commits — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | e2f59527 |
| Ran by | unknown — the spawn prompt named no agent or model for this row, and this record transcribes only what it was given |

## What this phase was asked

`plan.md` phase 1: the loader for `chain_check.py` in `evidence()`'s shape,
refusing with a sentence naming what the sibling is for (S8); the run's own
two-dot `--range` refused where its start does not reach its end, through
`chain.is_ancestor`, the message naming both ends and `A...B` (S7), in
`main`'s path and not inside `whole_range`'s resolution; `parse_range`'s
docstring rewritten and the sentence `spec.md` §*Removes* names gone;
`Reads:` on `parse_range`, `main` and the new units, their census lines
removed; the new test module opened with S7's two cases and S8, each seen red
first. Q2 answered here.

## What this phase found

- **Q2.** The module is `tests/test_the_sweep_reads_a_range_as_its_own_commits.py`
  and takes answer (a): `commit`, `merge` and `switch` from
  `tests/test_a_range_owns_what_git_lists_for_it.py`, `git` and `write` from
  `tests/test_the_record_is_generated.py`. The shape module's `commit` stages
  nothing when it is given no path, so the module adds `put`, which writes
  the files, runs `git add -A` and then calls that `commit`. `history` builds
  the measured shape (`root`, `f1`, `S1`, the merge, `f2`) with whatever each
  commit writes, so every later case is one call.
- **The spelling has one reader.** `parse_range` and `owned` both need to
  know whether the range was typed with two dots or three, so a new unit
  `separator` reads the dots and `parse_range`'s own loop over the
  separators became a call to it. Without that, the spelling would have had
  two readers, the class #866–#870 closed.
- **`owned` returns the list phase 2 needs.** It is called in `main` for the
  refusal alone in this phase, and its return value, `own_commits`' list,
  is what phase 2 passes to `corrected`. A three-dot spelling returns None
  and never loads `chain_check.py`, so S8's refusal is a two-dot range's
  alone.
- **The census.** `main` had no docstring, so it gained one to carry its
  `Reads:` line. `parse_range` and `main` left `tests/undeclared_readers.txt`;
  `separator`, `owned` and `chain` were never on it.
- **How each case was seen red**, each through `bin/mutation-check` on the
  committed file: S7's refusal case red with `if not loaded.is_ancestor(root,
  a, b):` replaced by `if False:` (exit 0 and a report); S8 red with `if not
  os.path.isfile(CHAIN):` replaced by `if False:` (the load raised a
  traceback instead of exit 2); S7's declaration case red with the refusal
  moved into `parse_range` (plan alternative H), where the row printed under
  `unresolved`.

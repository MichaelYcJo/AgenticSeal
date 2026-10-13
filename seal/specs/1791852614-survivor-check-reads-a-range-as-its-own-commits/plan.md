# Implementation Plan: survivor-check reads a range as its own commits (#873)

<!-- seal/specs/1791852614-survivor-check-reads-a-range-as-its-own-commits/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-13 by the orchestrating session, under the owner's `automation` answer, when `smith` was spawned.

## Summary

`survivor_check.py#corrected` keeps counting a file's sentences at the two
ends of the range, and on a two-dot range keeps a removed or written
sentence only where one of the range's own commits — what
`chain_check.py#own_commits` lists — removed or wrote it. `A...B` is read at
its two ends as today, because its start is the merge base. A two-dot range
whose start does not reach its end is refused. The sweep becomes a carrier
of the rule's one home and defines nothing beside it.

## Technical context

Coordinates are at `2cf7956a` (the branch's routing commit; the tree equals
`main` at `321e9de1`).

- `skills/code-review/scripts/survivor_check.py`: `git` :426, `resolves`
  :443, `parse_range` :452 (the `...` merge-base resolution at :475–:478),
  `tracked` :481, `read_blobs` :489, the loaders `reader` :1053 and
  `evidence` :1133 (the shape the new loader takes, with `Refused` and a
  sentence naming what the sibling is for), `corpus` :1279, `corrected`
  :1301 — the two-ends path list at :1378, the per-path loop at :1429, the
  `gone` append at :1444, the `fresh` append at :1470, the pairing at
  :1473 — `examine` :1713, `survivors` :1730, `whole_range` :1986 (calls
  `parse_range` at :2060 inside a `try` and reads `Refused` as *does not
  resolve*), `main` :2228.
- `skills/code-review/scripts/chain_check.py`: `own_commits` :4942 returns
  `[(full, short, [(status, path), …])]` oldest first, `None` where git
  fails, `[]` for a start that does not reach its end; `paths_of` :4998;
  `is_ancestor` :1621. `round_record.py#parse_range` :3333 is the model for
  the refusal and its text (:3366–:3369).
- Tests: `tests/test_a_corrected_sentence_survives_elsewhere.py` (4988
  lines) holds `module` :74, `run` :91, `over` :102 (`commit^..commit`),
  `build` :444 (git from Python), `one_survivor` :1494, and the path-list
  case :1210 with its constants :1097–:1134 (`LISTS_PATHS = {"--name-only",
  "ls-files", "ls-tree"}`, `PATH_LIST_CALLS = {"corrected": 1, …}`).
  `tests/test_a_range_owns_what_git_lists_for_it.py` holds `commit`,
  `merge`, `switch` and a session-scoped template repository, the shape
  helpers the new module can import. `tests/test_the_rules_have_one_owner.py`
  rule 18 :364; `tests/test_the_range_rule_states_no_shape.py` `LINKERS`
  :47 and `SHAPE_WORDS` :40. `tests/test_the_gate_asks_the_range_ci_will_ask.py`
  pins that `A...B` resolves through the merge base (0.12.2 R3).
- Policy: `docs/the-record-layout.md` §*A range owns the commits that
  descend from its start* :119–:157 (323 lines in the file; room);
  `docs/review-chain-spec.md` §*The survivor sweep* :856 (999 lines; no
  room). `seal/config.md`: `Document line ceiling | 1000`, `Ledger frozen
  from | 1790993141`, `Removes from | 1791780031`.
- Census: `tests/undeclared_readers.txt` :869–:920 lists every unit of
  `survivor_check.py`, `corrected@fde86cfa` :878, `parse_range@8a702916`
  :894, `main@1bd887a9` :888 among them.
- Measured in the frame (`spec.md` §*Measured in this frame*): the two-dot
  report over a merge, the three-dot silence, and what `--ancestry-path`
  lists from a merge-base start.

**What breaks in 6 months.** A change made only inside a merge commit's
conflict resolution stops being measured on a two-dot range; the home states
that limit and the module docstring repeats it as a limit. The own-commits
pass reads two trees per own commit, so a hand-typed range over hundreds of
commits costs hundreds of `cat-file` batches more than today; Q1 measures the
cost on a real range before deciding whether a no-merge range skips it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **A. the two-ends count kept, each removed and written sentence kept only where an own commit (`own_commits`) removed or wrote it, on a two-dot range; `A...B` at its ends; a non-reaching two-dot start refused** | a conflict-resolution-only change is unseen, the home's declared limit; the pass costs two reads per own commit | chosen |
| B. refuse a two-dot range that holds a merge, naming `A...B` as the spelling | `A...B` asks a different question — the whole branch, not the fix pass — so the caller can no longer ask the one the orchestration tells it to ask after every fix pass, and the answer exists in the tree | rejected |
| C. state the limit in the docstring and leave the reading | a reader that lets the unknown through; the orchestrator then excuses a false report in `survivors.md`, a row quoting a survivor that was never this range's | rejected |
| D. restrict the two-ends list to the own commits' paths, no per-sentence filter | a file both sides changed keeps the merged side's removed sentences; #860 measured the same class at unit level, 22 against 2, and S4 is the case that keeps this rejected | rejected |
| E. read each own commit against its parent and union the results, replacing the two-ends count | a sentence removed and restored inside the range is reported; the net reading is what 77 real ranges calibrated the floor against, and every existing case would move | rejected |
| F. run the own-commits pass on `A...B` as well, from the merge base | measured: from the merge base the own commits made before the merge are not on an ancestry path, so `f1`'s correction is dropped | rejected; S6 pins it |
| G. a second `git log --ancestry-path` in `survivor_check.py` instead of loading `chain_check.py` | a second reader of one input, the class #866–#870 closed; the owner sentence would have two readers to drift between | rejected |
| H. the refusal of a non-reaching start in `parse_range`, where `whole_range` also calls it | a two-dot declaration row whose start no longer reaches its end would change from *not this run's range* (no line) to `unresolved` (printed when owned); nothing asked for that | rejected; the refusal is `main`'s path, on the run's own range |
| I. let a non-reaching two-dot start own nothing and report silence | *examined N files against 0 sentences* over a range nobody meant, the shape the inventory calls *unknown passed*; `close` refuses the same range since #860 | rejected |
| J. the bold statement in `docs/review-chain-spec.md` beside the sweep's | the file is one line under the ceiling | rejected; the home carries it |
| K. skip the pass where `git rev-list --merges a..b` is empty, decided now | an optimisation with no measured cost behind it; on a linear range the filter keeps everything, so the skip changes no output and buys only time | deferred to Q1, a measurement in phase 2 |

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | the loader for `chain_check.py` in `evidence()`'s shape, refusing with a sentence naming what the sibling is for (S8); the run's own two-dot `--range` refused where its start does not reach its end, through `chain.is_ancestor`, with the message naming both ends and `A...B` (S7), applied in `main`'s path and not inside `whole_range`'s resolution; `parse_range`'s docstring rewritten and the removed sentence gone (`spec.md` §*Removes*); `Reads:` on `parse_range` and `main` and the new units, their census lines removed. The new test module (name the work's, Q2) opened with S7's two cases and S8, each seen red first | the new module; `tests/test_a_reader_declares_its_input_class.py`; `tests/test_a_corrected_sentence_survives_elsewhere.py` whole at the boundary | |
| 2 | the own-commits pass: one unit reading each own commit and its parent at the commit's changed paths intersected with the two-ends list, returning the pairs lost and gained; `corrected` keeps a `gone` and a `fresh` sentence only where the pairs hold it, on a two-dot range, before the pairing across paths; `A...B` unfiltered; `examine` and `survivors` carry the input. S1, S2, S3, S4 and S6 seen red first, the handover saying which mutation turned which; the path-list case counting and classifying the new list (S10); `Reads:` on `corrected` and the unit, census lines removed; Q1 measured and its answer written into the row | the new module; `tests/test_a_corrected_sentence_survives_elsewhere.py` whole (S5); `bin/mutation-check` over the unit and over `corrected`'s two appends | |
| 3 | the texts and pins: `corrected`'s docstring and the module docstring's §*What it does not answer* linking the home in a sentence holding no listed word and stating the inherited limit; the home's new bold statement with its `Enforced by:` line naming the new module and `corrected`; rule 18's carriers and the guard's `LINKERS` gaining `survivor_check.py` (S9); `skills/code-review/orchestration.md` §*Then ask what the fixes left standing* unchanged unless its sentence states the two-ends reading | `tests/test_the_rules_have_one_owner.py`, `tests/test_the_range_rule_states_no_shape.py`, `tests/test_a_folded_statement_names_what_enforces_it.py`, `test_docs_line_wrap`, `test_no_passage_is_pasted_into_a_second_file`, `test_one_word_one_meaning` over the changed files | |
| 4 | the records: `changelog.md`; the ledger fragment `seal/ledger/1791852614-….md` with a row per scenario; `evidence-check --reverify --into` for every released row whose anchor on `corrected` or `parse_range` moved; `overview.md` with its divergences and *Not verified*; `survivors.md` only where the branch's own run reports a place; `phases/phase-N.md` for each phase | `bin/evidence-check --strict` (S12); `survivor-check --range origin/release/v0.21.1...HEAD` with the item's `survivors.md`; the hygiene modules | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true, which is the failure the evidence ledger exists to prevent.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. A phase reconstructed
afterwards is reconstructed from the diff, which is where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. Write it to
`seal/specs/<work-item-id>/phases/phase-N.md`, from `templates/sdd-phase.md`,
when the phase closes.

One caveat, so nobody builds on it, and it has two halves. Where feature
branches squash, these commits stop resolving at the merge — and **a rebase
during the work does the same thing earlier and far more quietly**, because the
orphaned object still answers `git cat-file` in the worktree that wrote it.
The quiet half is the one that bites: this column was wrong on its own first
use, nine SHAs deep, and only a reviewer opening them found it. **Re-read the
column after any rebase**, or it names commits that resolve in one clone and
nowhere else. That is tolerable because nothing measures from this column.
The evidence ledger had the same problem and no such tolerance. It no longer
has it at all: a ledger row names a symbol and a content hash, so there is no
commit in it for a rebase to orphan.

## What the build must not write

- No sentence, in the home, in a docstring's linking sentence or in a
  record, that states which commits a given history owns by its shape or by
  time. `tests/test_the_range_rule_states_no_shape.py` holds the word list,
  and the reframe of 1791384160 is why: three rounds each found such a
  sentence false. A shape is a case; `spec.md` §*Measured in this frame* is
  the frame's measurement and not a sentence to copy into the tree.
- No change to `round_record.py` or `chain_check.py`.

## Operational impact

- No migration, no new environment variable, no new dependency.
  `chain_check.py` already ships beside the sweep.
- Compatibility: CI's and the broad gate's spelling, `origin/<base>...HEAD`,
  reads exactly as before. A two-dot range with no merge reads exactly as
  before (S5). A two-dot range holding a merge reports fewer sentences as
  removed, which is the true count, and a two-dot range whose start does not
  reach its end is refused at exit 2 where it used to be measured over two
  unrelated trees. Direction: the step allows more on the one shape nobody
  intends and blocks more on the other; neither reaches a person, because
  the fix pass's range is `close`'s own and `close` has refused the second
  shape since #860. Prompt budget: zero.
- Cost: two `cat-file` batches per own commit on a two-dot range; Q1
  measures it on a real range before a skip is added.

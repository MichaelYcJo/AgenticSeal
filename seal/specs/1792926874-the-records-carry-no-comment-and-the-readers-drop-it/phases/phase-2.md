# Phase 2: 1792926874-the-records-carry-no-comment-and-the-readers-drop-it

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 0635a040 |

## What this phase was asked

Build phase 2 as `plan.md` *Phases* row 2 says: `evals/scripts/replay_targets.py` reads a historic record's lines with the reader of the commit that judged it (`spec.md` *Scope* item 4). Verify it with `tests/test_replay_targets.py` and with S10: `--list` at the phase's base and head identical, and `--case` for each committed replay case regenerating identical files. Show the new case red against the old code. Write the work item's `changelog.md`, carrying the consuming-repository case of `plan.md` *Operational impact* and naming `questions.md` Q1's default.

## What this phase found

**A commit's check is asked for its judgment and nothing else.** The first build read the record's lines with the check and the reader of the commit that judged it. `--list` then stopped with `AttributeError: module 'specseal_chain_check_b454513446d6_0' has no attribute 'label_of'`: the check of a commit that wrote a labelled record spells its helpers as that commit did. `labelled_round` now asks that commit's check for `round_of` alone, reads the lines with that commit's reader, and names the labels and the finding split with this tree's check. This tree's `finding_spans` asks the reader only for what every reader since 0.22.0 holds; S10 below ran it over every labelled record at the last two tags and at every tag for the named cases.

**`labelled` keeps this tree's reader, a divergence from `spec.md` *Data & interfaces*.** The spec names `labelled` among the functions that read with the judging reader. `labelled` decides a record's shape before anything judges it, and the check of a commit before 0.22.0 has no `target:` label to ask. A `target:` line inside a comment would have to open a comment's inner line, and the round template carried no label-led line at `v0.20.0`, `v0.21.0` or `v0.21.1` (executed: `git show <tag>:templates/sdd-round.md | grep -c -E '^(target|severity|location|evidence|verdict|regression|reopens|answer|confirms|original):'` printed 0 at each). From `v0.22.0` the template carries a real `target:` line, so such a record is labelled however the comment is read. `labelled`'s docstring states this, and `overview.md` records the divergence.

**The new case, and how it was seen red.** `tests/test_replay_targets.py::Test_module::test_a_labelled_record_is_read_by_the_reader_that_judged_it` judges a record with a stand-in for a reader before #1012, one that blanks a comment's lines, and puts a comment holding a `location:` line that names `src/z.py:1` above finding 1's own `location:` line. Against phase 2's base it failed: finding 1's location read `src/z.py:1`, the comment's line. `mutation-check` with this tree's reader put back for the lines (`check, _ = record_reader()` read as `check, reader = record_reader()`) turned it red, executed after the commit.

**S10, executed.** At phase 2's base, `a9d8c93e`, and at its head, `replay_targets.py --list` printed 144 lines, byte for byte the same (`cmp` exit 0). `--case replay-1791382684-r2 --case replay-1791382684-r5 --case replay-1791384160-r2 --case replay-1791779434-r5 --out <dir>` wrote the four cases at both, and each matches its directory under `evals/behaviour/warden/` (`diff -r` exit 0); the printed lines were the same at both too. So the four committed cases and the listed targets read no record that a comment changes, and the case above is what holds the reading.

**Tests, executed.** `tests/test_replay_targets.py`, `tests/test_noninferiority.py` and `tests/test_seed_defects.py`, which load the generator: 275 passed. `test-layout --pairs tests/test_replay_targets.py`: 0 pairs. `uvx ruff check` and `uvx ruff format --check` over both changed files: clean.

**The changelog fragment** carries the three consuming-repository bullets of `plan.md` *Operational impact*, and says no strip command ships while the owner's Q1 is open.

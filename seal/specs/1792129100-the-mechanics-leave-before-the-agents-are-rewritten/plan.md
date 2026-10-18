# Implementation Plan: the mechanics leave before the agents are rewritten (#964)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-16 by the repository owner, when `smith` was spawned.

## Summary

Four pieces of mechanics leave or change before any agent is rewritten, so
that #957's agents and their paid proof build on a tree that is green, that
refuses no unit edit for a missing declaration or a drifted hash, that
states the round record's grammar once where the check reads it, and whose
`## Not verified` rows close with a word. The Windows-red case of the
release is fixed where the defect is and the evaluation harness reads the
0.22.0 record. The `Reads:` census with its 994-line list and the rider
stamps with their checker leave. The round record's grammar becomes one
table in `docs/the-review-record.md` that `chain_check.py` loads and
matches whole. The closing mark becomes the word `closed`, and the four
0.22.0 items' overviews are rewritten once. Every phase is verified by CI
alone; no agent's cases are run.

## Technical context

Read at d4552372, the release this item's base is cut from; `executed`
where `spec.md` §*The tree as it stands, measured* says so.

- **The marks and their readers** are `spec.md` §*Marks and labels*' table.
  The one emoji a gate reads is `unverified_check.py#CLOSED` (line 75),
  called at `:823` and in two messages at `:1675` and `:1792`.
- **The census.** `docs/the-reader-registry.md` (152 lines) states the
  grammar, the population, K1, the census and the `## Removes` rule;
  `tests/reader_registry.py#GRAMMAR` and
  `tests/test_a_reader_declares_its_input_class.py` read it;
  `CONTRIBUTING.md:247-251` asks for the line. `rider_check.py`'s stamp is
  `Verified <date> against <anchor>@<hash>`, resolved by
  `skills/verify/scripts/coordinates.py`; `tests/test_a_rider_reaches_its_file.py`
  holds the stamp cases beside the `seal/follow-up.md` cases.
- **The check.** `chain_check.py:93-191` holds the label constants, the
  exact and misspelt label patterns, and the value patterns; `records`
  (`:1230` on) reads through them; `ROUTING` (`:63`) shows how the script
  finds a sibling file by relative path, which the grammar loader reuses.
  `templates/sdd-round.md:3-14, 32-60` and `templates/config.md` §*What no
  row governs* restate the labels; `tests/test_the_pull_request_language_is_the_repositorys.py#ROUND_RECORD_FIELDS`
  derives the literal list. The user's hygiene workflow clones this
  repository at the pinned tag into `$RUNNER_TEMP/specseal` and runs the
  check from there (`templates/hygiene.yml:58-59, 92`), so the document is
  beside the script wherever it runs.
- **The harness.** One case this item owns is red on `main` at d4552372
  (run 38852872472, `read`): the Windows path case at
  `tests/test_a_rewritten_definition_proved_non_inferior.py:623`. The same
  run's sealer-guarantees case is fixed by #963 outside this item (the
  fixture clears `GITHUB_ACTIONS`, under which the check prints `::error`
  annotations), and this plan does not touch it. `evals/README.md:34-35`
  names a `--list` flag that does not exist, and `replay_targets.py` reads
  a round's asked paragraph from a section new records do not carry (#923
  `overview.md` §*Not done*, `read`). The cases are regenerated through
  `--case`; nothing runs them here.
- **The suite and CI.** 7,329 cases priced at 3,371 s; one run is 55 runner
  minutes over three legs, under 11 minutes wall, 208 billable minutes if
  private. The census module is 38.4 s of that, the rider module 3.5 s.

**What breaks in six months with the chosen approach.** The grammar table
is read by the check from a document under `docs/`, so a `docs/` rewrite
(#941) that moves the heading or splits the file breaks the check loudly, at
exit 2, in CI, which is the direction chosen. A `closed` word read
fail-closed refuses every `U+2705` row a user's in-flight overview still
carries at the moment they move their hygiene pin, and the changelog is
where they learn the edit. With the census gone, nothing refuses a reader
whose input class is undeclared, and which way a reader fails on an input it
cannot read is read from the code by #956's audit, not from a line the
reader's author wrote about it.

## Alternatives considered

CI cost is the billable minutes a private repository would pay per pull
request (Linux 1×, Windows 2×, macOS 10×), against the 208 measured at
d4552372. The suite's priced seconds are the share this item moves.

| Approach | Failure scenario (six months on) | CI cost if private | Verdict |
|---|---|---|---|
| A. The red case fixed where the defect is and the harness reading the record; the census and the stamps gone with everything that stood on them; the grammar one table the check loads and matches whole; the closing mark the word `closed`, the shipped overviews rewritten once | above | ≈ −1 minute a run: 42 s of priced cases leave (the census and stamp modules), a handful of document-reading cases arrive; the 208 is the macOS multiplier's, which this item does not touch | **chosen** |
| B. Keep the `Reads:` lines as documentation once the census leaves | a line no check reads goes stale the way the registry's own limit 5 says, and a stale claim about which way a reader fails misleads #956's auditor; 31 KB read by whoever opens the files | none | rejected |
| C. Keep the rider stamps, drop the census alone | the same hash kept beside the tree, asking `--reverify` on a comment edit, as it did on #923's round 1 fix pass | none | rejected |
| D. The grammar as a constant in the script, with a test that the document's table equals it | two statements held in step by a pin, where the tenet asks one source; the document's reader then reads the script's constant | none | rejected; the document is the source and the script loads it |
| E. A generated-variant or mutation test over the grammar | #929 measured a generator chasing the next gap never converging | seconds a run | rejected (the owner) |
| F. `U+2705` stays as the one emoji a check reads | the one exception to the owner's rule, in the one place the rule came from: a mark a gate reads | none | rejected; the word `closed`, Q2 answered by the owner |
| G. `## Not verified` redesigned into labelled lines, as the round record was | a second 1,800-line checker rewritten for a table one reader reads with its own spec; the word in the cell is the change the rule asks for | none | rejected here; a labelled-line redesign is #940's or #956's to weigh |
| H. The grammar document read by the check from `docs/` breaks in a user's repository where no `docs/` is checked out | the hygiene template clones this repository whole at the pinned tag and runs the script from there (`templates/hygiene.yml:58-59`); a clone with no `docs/` is exit 2 naming the file, never a pass | none | not a failure of A; stated so the loader's refusal is read as intended |

## The split

This item is the first of the two the owner made of #957 on 2026-10-16. It
merges into `release/v0.22.1` first; #957 rebases onto that branch after
the merge and builds its agents on the tree this item leaves. The
measurement that asked for the split, and what each item holds, is #957's
`plan.md` §*The split*. Nothing in #957's phases depends on an order inside
this item beyond the table below.

## Phases

Vertical slices — each phase ends with something runnable and verified. No
phase changes a file under `agents/` or a skill a definition opens, so no
agent's cases run. Every phase enumerates the class of what it removes by the
`git grep` its record names, and every new case is seen red first (contract
§15), with the exit named in the phase record.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The tree is green and the harness reads the record.** The Windows-red case of run 38852872472 fixed where the defect is: `test_a_side_runs_the_tree_it_measures_and_no_installed_plugin`'s path comparison on Windows, or `noninferiority.py#side_path` where the harness is what is wrong (the sealer-guarantees case of the same run is #963's, already fixed outside this item). `evals/scripts/replay_targets.py` reads the asked paragraph the new record carries, or none, and the four replay cases are regenerated through `--case`. `evals/README.md:34-35` rewritten to the generators' usage as it is | `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py -q` exit 0; CI green on all three legs at the phase's commit; the regenerated cases read by hand against `templates/sdd-round.md` | 74083e67 |
| 2 | **The census and the stamps leave.** `tests/undeclared_readers.txt`, `tests/reader_registry.py`, `tests/test_a_reader_declares_its_input_class.py` and `.github/scripts/rider_check.py` removed; the 364 `Reads:` lines and the 55 stamp lines removed by one-shot scripts under the scratch directory, run once and deleted (contract §7), each asserting its count before and after; the stamp cases of `tests/test_a_rider_reaches_its_file.py` removed and its `seal/follow-up.md` cases kept (T1); `docs/the-reader-registry.md` rewritten in place to §*A frame names what its work removes* alone; `CONTRIBUTING.md:247-251` removed; `seal/follow-up.md:27-47` rewritten to *a rider is a comment, and a rider outliving its fix is the reader's finding*; `.github/workflows/test.yml:110-112`'s comment rewritten to the reason that stays, or removed with `fetch-depth` where none does; `spec.md` §*Removes*' rows for the census and the stamps read against the diff | `git grep -n "Reads: " -- '*.py'` finds nothing; `git grep -n -E "Verified [0-9-]+ against"` finds nothing outside `seal/specs/` and `changelog/`; `git ls-files` names none of the four removed paths; `bin/rules --check` exit 0 with every `Enforced by:` that named the census module gone from its paragraph; `bin/test tests/test_a_rider_reaches_its_file.py tests/test_the_rules_have_one_owner.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py -q` exit 0; `ruff check` and `ruff format --check` on the touched `.py` files | 17b6e581 |
| 3 | **The grammar is one table, and the check reads it whole.** `docs/the-review-record.md` §*The round record* gains the table of `spec.md` §*Data & interfaces* and its five prose paragraphs are rewritten to point at the rows they stated; `chain_check.py#grammar(path)` loads it at import from `docs/the-review-record.md` beside the script, exit 2 naming the file where the document or a row cannot be read, and `records` matches every labelled line and heading against its row whole, the constants at `:93-191` gone; `templates/sdd-round.md`'s comment and `templates/config.md` §*What no row governs* point at the table and restate nothing; `ROUND_RECORD_FIELDS` of the language test derived from the table. Test-first in `tests/test_chain_check.py::TestGrammar` (T2): the table loads and its rows are the eight labels and the heading; each row's shape matches the template's example line whole and refuses the line with a trailing word; a document with a broken row is exit 2 naming it; T32, T33, T35 and T36 re-pointed at the table unchanged in what they refuse (T3) | T2 red on d4552372's reader (no loader), green after; `mutation-check` red for: `fullmatch` loosened to `match` (T2's trailing-word case), the loader's exit 2 dropped (T2), a row's shape read by `search` (T33); `bin/test tests/test_chain_check.py tests/test_the_pull_request_language_is_the_repositorys.py tests/test_the_record_is_written_in_words.py tests/test_docs_line_wrap.py tests/test_the_rules_have_one_owner.py -q` exit 0; `chain_check.py --baseline origin/release/v0.22.1 --root <worktree>` exit 0 on this branch; `ruff check` and `ruff format --check` | 3a5351cf |
| 4 | **The closing word, and the close.** `unverified_check.py#CLOSED` reads `closed` as the first word of the row's first cell, a bare `closed` refused as the bare mark was, `U+2705` refused naming the row and the edit; its messages at `:1675` and `:1792` in words; the test module's success and failure case per changed function (T4); `templates/sdd-overview.md:38`, `templates/config.md:139`, `docs/the-record-layout.md`'s and `skills/implement/SKILL.md` §4's sentences to the word; the `## Not verified` rows of the four 0.22.0 items' overviews rewritten once by a one-shot script, its diff read whole by the smith (Q2, answered). Then this item's close: `overview.md` (one line of purpose, divergences, `## Not verified` in the new word, fed-back clauses) and `changelog.md`, the paragraph a plugin user reads: the `closed` word and the edit an in-flight overview owes, the grammar table and the whole-line refusal, the census and the stamps gone, the tree green on Windows | T4 red on the reader as it stands, green after; `mutation-check` red for the bare word accepted and for `U+2705` accepted; `bin/test tests/test_the_unverified_record_is_readable.py -q` (or the module that owns the reader, named in the record) exit 0; `unverified-check seal/specs/ --baseline origin/release/v0.22.1` exit 0 on this branch with every closed row counted closed; `bin/rules --check` exit 0; the hygiene step green at the pull request | 6bceef00 |

This table is also where the work records how far it got. **Status is empty,
or the commit that closed the phase.** Re-read the column after any rebase.

### Test rows — what each case protects and the mutation it kills

| Case | Protects | Mutation it kills |
|---|---|---|
| T1 `tests/test_a_rider_reaches_its_file.py` as it stands after phase 2, its stamp cases gone | S3 — a coordinate-tied row back in `seal/follow-up.md` | unchanged |
| T2 `tests/test_chain_check.py::TestGrammar::test_the_table_loads_and_every_line_matches_its_row_whole` and `::test_a_document_the_check_cannot_read_is_exit_2_naming_it` (phase 3) | S4 — a fourth statement drifting, and a partial match | `fullmatch` loosened to `match`; the loader's exit 2 dropped; a row's label read case-insensitively |
| T3 T32, T33, T35, T36 of #923 (re-pointed in phase 3) | S5 — the known leaks reopening | unchanged |
| T4 `tests/test_the_unverified_record_is_readable.py::TestClosedRow::test_the_word_closes_and_the_mark_and_the_bare_word_are_refused` (phase 4; the module name is the one that owns `unverified_check.py`, named in the phase record) | S6 — the emoji mark read by a gate | `U+2705` still accepted; `closed` with nothing after it accepted; `Closed` accepted |

Phase 1 writes no new case: it fixes a case that exists and regenerates
cases from their generators, and S1 is held by CI on the phase's commit.

## Operational impact

- **What a plugin user sees.** A `## Not verified` row closes with the word
  `closed`, and an overview in flight with `U+2705` rows fails the hygiene
  step naming the row and the edit when the user moves their `hygiene.yml`
  pin to this release (`templates/hygiene.yml:58`); the changelog says so.
- **The check.** `chain_check.py` loads its grammar from
  `docs/the-review-record.md` beside itself and exits 2 naming the file
  where it cannot; the hygiene template's clone carries the document. A
  record's lines are matched whole, so a value with a trailing word is
  refused where it passed before. The refusal names the line and the row.
- **The census and the stamps.** No pull request is refused for a missing
  `Reads:` line or a drifted rider hash; `grep -rn "RIDER:"` is still the
  list of riders, unstamped.
- **CI.** About a minute less a run for the suite; no paid run.
- **What #957 inherits.** A green tree, a smith that writes `closed`, a
  record check that reads one table, and no census refusal on the unit
  edits its rewrite makes.
- No new dependency; stdlib Python at the floor.

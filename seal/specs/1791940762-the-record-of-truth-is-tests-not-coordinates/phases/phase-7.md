# 1791940762-the-record-of-truth-is-tests-not-coordinates — phase 7

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | c46c95d4 |
| Ran by | smith on Opus 5.5, as the attribution line in the spawn prompt names it |

## What this phase was asked

Remove what still stood on the ledger, under the tenet's sentence that a
change removes, in the same commit, what stood on the old fact. Every line
of `git grep -in ledger` outside `seal/specs`, `seal/process`, `changelog/`,
`CHANGELOG.md` and `tests/` takes one of three verdicts: code that reads,
writes or guards ledger files is deleted with the cases only it needs; a
sentence describing the ledger as current is rewritten to what stands or
deleted; a use meaning something else is left and named.
`skills/writing-style/SKILL.md`'s example pointing at the gone
`templates/ledger.md` is replaced in place. The five test functions naming
the ledger are renamed for what they guard or deleted with their behaviour;
phase 5 had deferred that to #940, #941 and #942, and the tenet takes the
deferral back.

Mid-phase the owner answered Q2 with option 1, relayed by the orchestrator
(7fc76195): `pact-check` grades anchors in specs only, and the reading of
`seal/pact-changes/`, the signer-side ledger glob, the pact review
procedure, `templates/pact-review.md` and every reader of those two records
leave with their cases. The pact itself, `templates/pact.md`,
`docs/the-pact.md` and spec-anchor grading stay, each rewritten where it
described the removed half; `README.md`, `skills/config/SKILL.md` and
`templates/config.md` checked too.

## What this phase found

**The frame holds, with three corrections to the spawn's picture.**

- **Two of the five test names were a different ledger.**
  `test_the_body_drops_the_ledger_clause_where_no_durable_log_exists` and
  `test_the_ambiguous_ledger_note_reaches_the_issue_it_is_about` guard the
  flow-baseline issue, which `roll_flow_measurement_issue.py` called both
  the durable log and the durable ledger. Its neighbours were already named
  for the durable log, so the word goes everywhere that issue is meant: the
  roller's docstrings and the two notes it writes into an issue body,
  `skills/verify/SKILL.md`, `docs/issues-and-milestones.md` and two test
  modules. The cases are renamed for the baseline clause and note they
  guard. A new pin holds the ambiguous note's wording, red against the old
  text, and so does the skill's pin (executed).
- **`test_a_planted_ledger_file_is_named` guards only ledger files, and it
  stays.** The premise checked: PRs #937 and #939, open into
  `release/v0.22.0` on 2026-10-14, each add a `seal/ledger/<id>.md`
  (`git diff --name-status <merge-base> origin/<branch>`, executed). A merge
  brings a new file back with no conflict, and this guard and the tree
  assertion beside it are what name it. Its comment now says why it stays.
- **`Pact notify` is part of Q2's half and is not removed.** Its only
  effect was choosing which record rows `pact-check` read, and #759's
  one-spelling rule was argued from it. Removing the row returns two values
  from `pact_declaration` and changes about 60 cases; removing the rule
  with it is a subtraction of its own. Both are Q3 for the owner. Every
  text now says the value is printed and acted on by nothing.

**The other two renames.** `test_the_target_is_resolved_by_named_unit`
and `test_the_census_hash_is_content_hash_over_the_unit` name the units
they pin. The budget check named the layout's `Enforced by:` line as
unresolved after the rename and before the line was changed (executed), so
the rename cannot leave the line behind.

**Each grep line, by verdict.**

| Where | Verdict |
|---|---|
| `docs/one-root-by-lifetime.md` and `.ko.md` | rewritten: `.specseal/` holds the follow-up list and the migration config; the map line, the ledger-rows lifetime row and ticket order item 2 (#78's fold) leave; #85's orphan branch is "its home" |
| `hooks/root-migrate.py` | rewritten: `.specseal/` held the records that outlive a work item |
| `skills/verify/scripts/coordinates.py` | rewritten: the parse count names "one caller's run"; "Found by migrating this repository's own ledger" leaves |
| `skills/verify/scripts/mutation_check.py` | rewritten: "ledgered there" leaves |
| `skills/writing-style/SKILL.md` | replaced: the term example opens `templates/sdd-overview.md` and finds a closing memo, not a summary; the idiom row says `keeps the record honest` |
| `.github/scripts/roll_flow_measurement_issue.py`, `skills/verify/SKILL.md`, `docs/issues-and-milestones.md` | rewritten: the durable log, above |
| `docs/the-record-layout.md:249` | the renamed case |
| `skills/verify/scripts/pact_check.py`, `hooks/config.py:1578` | deleted with Q2's half |
| `.test_durations` | four renamed cases carry their prices; about 37 entries for gone ledger cases stay for the refresh's `--clean-durations` |
| `assets/seals/*.ans` | left: archived renders of past stamps, which `assets/seals/README.md` names with the released command that drew each; the word is a sample row's text |
| fold markers in `docs/release-checklist.md:95`, `docs/the-record-layout.md:242`, `:260` | left: work-item ids; `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py` holds one literally |
| `seal/follow-up.md:67` | left: its subject is a sentence of the released `changelog/0.12.2.md`, and amending a release is the owner's |

**Q2's half was larger than its readers.** The table walker's corpus took
one pass per header, and two of its four headers were the records'. Those
passes are 434 cases and hold headers no reader uses now, which the config
pass's own docstring says holds nothing, so they go; the backslash case
moves to the config header. `pact-check`'s `READ` line and summary stop
counting pact changes, and a pin holds that, red against a mutation adding
the count back (executed, `mutation-check`).

**What left, by commit.**

| Commit | What |
|---|---|
| 3875e5cb | the design record, three docstrings, the writing-style example; `text_regions` declares; four budget rows |
| d4e61bab | the durable log, two renames, two pins; four roller units declare |
| 37cb85b9 | two renames and the layout's `Enforced by:`; the S7 guard's premise |
| ee1deeca | Q2's half: the record readers in `pact_check.py` and `hooks/config.py`, the ledger glob, the review procedure and its delivery row, `templates/pact-review.md`, `tests/test_a_pact_review_takes_a_pact_change.py`, the walker's two passes, the layout trees, both READMEs, `docs/the-pact.md`; `anchor_files` and `check` declare; two budget rows |
| 6506a26f | `Pact notify`'s text in four files; Q3; one budget row |
| c46c95d4 | the four carried prices |

Budget rows lowered to what is measured: `docs-history` 32 → 31 and
37 → 36 and `unenforced` 37 → 36 and 37 → 36 for the two design-record
editions, `unenforced:docs/the-pact.md` 1 → 0,
`unenforced:skills/implement/orchestration.md` 41 → 38 and
`unenforced:templates/config.md` 37 → 34.

**Verification, executed unless named.** Each step ran the modules naming
a file it changed, with the census, one-reader, encoding, line-end and
interpreter modules. After the first step: 2,334 passed and the census red
for `text_regions`, then green. After the durable log: 1,440 passed and the
census red for four roller units, then green. After the renames: 1,191
passed. After Q2's half: 7,589 passed, 78 skipped. After the notify text:
4,547 passed, 78 skipped. `budget_check.py` exit 0 on the tree and against
`origin/release/v0.22.0` after each step; `bin/pact-check --help` exit 0;
`uvx ruff check` and `ruff format --check` on every changed Python file.
`test_the_durations_file_prices_the_suite` is red: 609 of 11,810 collected
cases unpriced (5.16 %), because the deletions took 457 priced cases out,
and only a Windows run can price the rest (`overview.md` §*Not verified*).
The full suite is the sealer's.

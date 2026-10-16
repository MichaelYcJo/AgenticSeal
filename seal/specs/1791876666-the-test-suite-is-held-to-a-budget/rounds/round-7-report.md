# 1791876666 — review round 7, report

Target: `a7638aca` on `chore/929-the-test-suite-only-grows` (PR #939, local
tip, not pushed), against `origin/release/v0.22.0` at `642441fc`. This is the
first round after the second reframe. Its target is phase 4's removal,
`e5ee4c97..a7638aca` (`423c916d` code, `f8e86a40` records, `a7638aca` the
orchestrator's plan rewrite and one sentence of #944's frame). The round
also judges whether the branch as a whole is ready for the sealer. Reviewed
in a `git clone --no-local` of the worktree at `a7638aca`, under this
session's scratchpad, deleted when the round was done. Paths are relative to
the repository root. Probes ran on macOS arm64, pytest 9.1.1, in the
virtualenv `bin/test` built inside the clone (CPython 3.12), and
`budget_check.py` on CPython 3.12.

## How the findings relate

The removal itself is complete. Nothing in code, tests, CI, the reader
registry, the interpreter census, `CONTRIBUTING.md`, `docs/` or the skills
still names `case_check.py`, its test module, the `cases` job or
`--baseline-passed`. Nothing live needed any of them. `test.yml` is
byte-identical to the base again, and the release ruleset requires no status
check that a `cases` job could have filled. The three recorded departures
hold on their grounds. The narrow modules, `budget_check.py` and ruff on the
changed Python files are green.

What is left is paperwork, all of it under `seal/specs/`, so all of it is
graded as correction notes (⬜) and none needs a fix pass:

- ⬜ 1. `plan.md`'s alternatives table still marks the removed design
  **chosen**, and alternative H's failure scenario still leans on it.
- ⬜ 2. #944's frame still names #929's regrowth check in three sentences.
  `a7638aca` corrected the fourth (the `cases` job one, `spec.md:46`), so
  this is the same class one line further on.
- ⬜ 3. Two of `overview.md`'s divergence rows still describe how the removed
  check drew its mutants, as a "Chosen" design, with no word that it left.

One question sits outside the tree. PR #939's body is still the phase 1
draft, and it names `evidence-check`. The orchestrating session pushes the
branch and owns that body, so it is a ❓ with that session named as its
answerer.

## What phase 4 removed, checked against the tree

**The class sweep** (`executed`). `git grep -i` over the whole tree at
`a7638aca` for `case_check`, `case-check`, `cases job`, `` `cases` ``,
`test_a_new_case_protects`, `baseline-passed`, `baseline_passed`,
`regrowth`, `only killer`, `kills nothing`, `per-case`,
`caller_that_ran_the_baseline`, `baseline=False`, `TRACER_SOURCE`,
`traced_run` and `sole_killer`. Outside this work item's own records, the
only hits are the three #944 sentences of ⬜ 2. The `per-case` hits are all
about the per-case time ceiling in `tests/conftest.py`, which is a different
thing. `tests/test_a_budget_ratchets.py:726` matches only on the word
`CASES`. Inside the work item, every remaining hit is a phase record, a
round record, or a sentence of `spec.md`, `plan.md`, `questions.md` or
`overview.md` that says the check left.

**What phase 4 changed in shipped code** (`read`: the whole
`e5ee4c97..a7638aca` diff). Two edits only:

- `mutation_check.py` loses `--baseline-passed`, the `baseline` parameter
  of `mutation_run`, and the docstring paragraph and comment that named the
  caller. Against the base, the module's only remaining differences are the
  `command_words` import that replaces `shlex.split`, and the `Reads:` lines
  on `mutation_run` and `main` that took those units out of
  `tests/undeclared_readers.txt`. All three ship with the Windows fix and
  the reader registry. None of them stood on the check.
- `arm_check.py#command_words`' docstring drops the clause naming the
  check's `--runner`.

**Departure 1, `--baseline-passed` removed** (`executed` and `read`). Holds.
`git grep` finds no caller of the option or of the parameter. On the base the
option did not exist, so removing it restores the base's command line.
`bin/mutation-check … --baseline-passed` exits 2 with argparse's
`unrecognized arguments`, which is S4. The module's own case file passes.

**Departure 2, the Windows command-line case moved** (`executed`). Holds.
The case sits in `tests/test_arm_check.py:1372`, uses that module's `ARM`
and loads nothing of its own. I reproduced the red the smith recorded:
`bin/mutation-check skills/verify/scripts/arm_check.py --replace
'        lexer.escape = ""' '        pass'`, with the case selected, exits
0 (`red`). Its failing line is `tests/test_arm_check.py:1379`, the
`windows=True` assertion. The file is restored and `git status` is clean.
`.test_durations` never priced the old module, and
`test_the_durations_file_prices_the_suite` passes with the one new id
unpriced.

**Departure 3, the `CONTRIBUTING.md` paragraph deleted rather than
rewritten** (`executed` and `read`). Holds. The paragraph was this branch's
own, and `git diff origin/release/v0.22.0 -- CONTRIBUTING.md` now shows only
the floor paragraph that phase 2 rewrote (S10). `budget_check.py` reads
`enforced-unresolved` 0 and `unenforced:CONTRIBUTING.md` 22 against a
ceiling of 22, so S6 holds. A rewritten paragraph would have needed an
`Enforced by:` target, and none stands in the tree.

**What else the brief asked** (`executed` unless marked).

- S2: `git diff origin/release/v0.22.0 -- .github/workflows/test.yml` is
  empty.
- The release ruleset requires no status checks. `main`'s requires `lint`
  only (`gh api …/rulesets`), so no required `cases` context is left
  dangling.
- `OUT_OF_CLASS` lost exactly the two `case_check.py` rows, and its module
  passes.
- The counts in `spec.md` §*Removes* (`git show e5ee4c97:…`):
  - the check's file is 1,105 lines with 26 top-level functions;
  - the test module is 618 lines, 13 test functions and 27 collected ids;
  - the job and its comment are lines 211–243 of `test.yml`, 33 lines with a
    15-line comment;
  - the paragraph is 17 prose lines and its `Enforced by:` line.
- The changelog's numbers: `SAMPLE` holds 35 rows, the commit-gate file
  collects 178 cases, and `budget_check.py` reads that file at 441 raw
  Windows seconds.

**The work item says only what ships** (`read`: `spec.md`, `plan.md`,
`questions.md`, `changelog.md`, `overview.md`, `phases/phase-4.md`, in
full). `spec.md`, `questions.md` and `changelog.md` say only what ships. The
changelog fragment carries the launcher, the stamp on an old `python3`, the
Windows backslash fix, and the commit-gate cut with the junit twins and the
hook-run census. No `Added` entry is left. `spec.md` §*Scope* item 2 names
once what the item no longer claims, and §*The per-pull-request check
leaves* says how that errs. `questions.md`'s Q6 and Q8 close as answered and
moot. `phases/phase-4.md` is a record of its own time. Its paragraphs on
`plan.md` and #944 described the tree at `f8e86a40`, and `a7638aca` then
acted on both. `plan.md` and `overview.md` each keep the stale sentences ⬜ 1
and ⬜ 3 name.

## ⬜ 1 — `plan.md` still marks the removed design chosen

`seal/specs/1791876666-the-test-suite-is-held-to-a-budget/plan.md:38`
(`read`).

Alternative A is the per-case check that phase 4 removed, and its verdict
cell still reads **chosen**. Its failure-scenario cell reads "above", and
"above" is now the removal's own *What breaks in 6 months*, so the row
pairs the removed design with the risks of the design that replaced it.
Alternative H's failure scenario (`:45`) still says "#942's pull requests
are each held by the regrowth check this item adds". `:63` says the CI cost
is unchanged "except the ubuntu minutes the `cases` job no longer spends".
The base never ran that job, so this item saves no minutes against the base.

The cost is to a reader. `settle` folds what is still true out of a work
item, and a reader who opens the alternatives table finds A chosen and
removal absent from it. The rest of the plan already says the right thing:
the Summary, the phase 4 row and the Technical context.

## ⬜ 2 — #944's frame still names #929's regrowth check

`seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/spec.md:48`
(`read`), with `spec.md:104` and `plan.md:31` in the same frame.

`a7638aca` removed *the `cases` job of #929 proves a new case kills what it
says* from `spec.md:46`. Three sentences of the same claim remain:

- `spec.md:48` states, as a limit of `enforced-unresolved`, that whether a
  target runs or asserts the rule is read by "#929's regrowth check and
  review".
- `plan.md:31` calls "#929's regrowth check" the per-case complement of the
  resolution gate.
- `spec.md:104`, the row for #929 in the table of what #944 changes in other
  items, says "the `Kills:` line and the regrowth check are the per-case
  complement of `Enforced by:`".

After this branch merges, none of these exists, and `spec.md` §*Scope* item 2
of this work item says so in as many words. `phases/phase-4.md:79-84` names
the failure: `settle` folding #944's frame would carry a check that never
shipped into a `docs/` policy. `spec.md:48` is the sentence most likely to be
folded, because it states what a gate cannot read and who covers it. The
cover it names is gone, so after the merge only review reads that question.
Under `skills/agent-contract/SKILL.md` §12 the fix at `:46` owed the class.
Scenario S3's `git grep 'case_check\|cases job'` misses these three lines,
which is why the sweep did not catch them.

## ⬜ 3 — two divergence rows describe the removed check as chosen

`seal/specs/1791876666-the-test-suite-is-held-to-a-budget/overview.md:28`
(`read`), and `:29`.

The row *A case names what it guards, and the regrowth check runs that line*
and the row *The draw ranked and capped* both describe how the removed check
derived and ranked its mutants. Their `Chosen` cells read as standing
decisions. Neither says the check left in phase 4. Rows `:34` to `:36`, and
the *Why this work exists* paragraph, do say it, and `:30`'s
`--baseline-passed` row has its removal row at `:34`. A one-clause "left in
phase 4" in each `Chosen` cell would match how `plan.md` marks phase 3's row.

## Earlier rounds' findings

Carried as coordinates from `rounds/round-6.md` and `rounds/round-3.md`;
each re-derived against `a7638aca`.

- Round 6's 🟡 1 (a skipped subtest read as stopping short) sat at
  `.github/scripts/case_check.py:208`. That file is gone at `423c916d`, and
  nothing in the tree reads pytest's call report for whether a case ran
  (`git grep` for the tracer's names finds none). Closed by the removal.
- Round 6's ⬜ 2 (the heading pin in the deleted test module) and ⬜ 3 (the
  deleted module's docstring) went with their files.
- Round 6's ⬜ 4 (`plan.md:30` named two unstable names) is closed. `:30` now
  says the reading of pytest's report is history in `phases/` and the
  rounds.
- Round 3's 🟡 1 and 🟡 2, deferred to the frame, sat in the same tracer and
  are closed by the same removal.
- Round 1's deferral to #942 (growth by parametrized rows) is already
  deferred, to #942. It is not re-found here: no job now proves any case,
  and #942 still owns the `test-cases` rows.

## What was carried

The base SHA `642441fc` and the round records' coordinates were carried and
not re-derived. Every verdict above was re-derived at `a7638aca`.

## Regression tests to plant

None. All three findings are prose under `seal/specs/`.

## Facts for the record

The evidence ledger is removed in 0.22.0, so no ledger rows. For the
sealer: the full suite has not run at `a7638aca`. Nothing is left open that
needs a fix, so the broad gate comes due now. What comes due is the
sealer's spawn.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| ⬜ 1 | `plan.md`'s alternative A, the per-case check phase 4 removed, still reads **chosen**; H's failure scenario cites the regrowth check this item adds; `:63` counts ubuntu minutes saved against a base that never ran the job | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/plan.md:38` | open | read: `plan.md:14-18`, `:32`, `:38`, `:45`, `:63`, `:74`; a correction to the run's paperwork |
| ⬜ 2 | #944's frame still names #929's regrowth check as what reads whether an `Enforced by:` target runs, and as the per-case complement: the class of the `:46` sentence `a7638aca` removed | `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/spec.md:48` | open | read: `spec.md:46`, `:48`, `:104`, `plan.md:31` of that frame, and `phases/phase-4.md:79-84`; executed: `git grep -i regrowth` names these three lines and only records otherwise; a correction to a frame `settle` will fold |
| ⬜ 3 | Two divergence rows describe the removed check's derivation and draw as `Chosen`, with no word that it left in phase 4 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/overview.md:28` | open | read: `overview.md:9-14`, `:28-36`; a correction to the run's paperwork |
| 🟢 | everything that stood only on the check, its test module and the `cases` job is gone, and nothing live needed them | `.github/workflows/test.yml` | confirmed | executed: the class sweep at `a7638aca`; `git diff origin/release/v0.22.0 -- .github/workflows/test.yml` empty; `gh api` rulesets: release requires no status check, `main` requires `lint`; 23 modules, 1,103 passed, 4 skipped, exit 0 |
| 🟢 | the departure removing `mutation-check --baseline-passed` holds | `skills/verify/scripts/mutation_check.py:286` | confirmed | read: the phase 4 diff and the net diff against the base; executed: the option exits 2 as unrecognized (S4); `git grep` finds no caller |
| 🟢 | the departure moving the Windows command-line case holds, and the case is red without the fix | `tests/test_arm_check.py:1372` | confirmed | executed: `mutation-check` removing `lexer.escape = ""` exits 0 (`red`), failing at `:1379`, file restored; `test_the_durations_file_prices_the_suite` passes |
| 🟢 | the departure deleting rather than rewriting the `CONTRIBUTING.md` paragraph holds | `CONTRIBUTING.md:117` | confirmed | executed: `budget_check.py` reads `enforced-unresolved` 0 and `unenforced:CONTRIBUTING.md` 22 of 22; the net diff against the base is the floor paragraph only |
| 🟢 | the work item's spec, questions and changelog say only what ships, and their counts hold | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/changelog.md:36` | confirmed | read: all three in full; executed: `SAMPLE` 35 rows, 178 cases collected, 441 raw Windows seconds, 27 ids and 13 functions in the removed module, 33 lines of the removed job |
| 🟢 | round 6's finding 1 is closed — the tracer it sat in left the tree with `case_check.py` at `423c916d` | `.github/scripts/case_check.py:208` | confirmed | executed: the file is absent at `a7638aca`, and `git grep` for the tracer's names finds no reader of pytest's call report; round 3's two deferred findings in the same tracer close the same way |
| 🟢 | round 6's notes 2, 3 and 4 are closed — their files left, and `plan.md:30` now says the tracer's reading is history | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/plan.md:30` | confirmed | read: `plan.md:30`; executed: the test module and the check are absent at `a7638aca` |
| ❓ | PR #939's body is the phase 1 draft at `2aa76b37`: "Phase 1 of four", "Phases 2–4 apply the same methods to the remaining 15 slowest files", and a checks row naming `evidence-check`, a tool 0.22.0 removes | PR #939 | ❓ out of verified scope | read: `gh pr view 939`; the branch is not pushed and the body is rewritten at the push, so the body that ships cannot be judged here; the orchestrating session of #929 answers it, and it squashes into the release branch's commit message |

## Paste-ready fixes

### ⬜ 1

```markdown
| A. Derived: each new or changed case must be its file's only killer of a mutant the check draws from the lines it runs, the units it names and the changed shipped lines; one run per mutant; a five-minute bound | six review rounds each found the next way a case stops short of its body on the runner (`rounds/round-1.md` to `round-6.md`) | chosen on 2026-10-14, built in phases 2 and 3, and **removed in phase 4** by the owner's decision of 2026-10-15 |
```

```markdown
| H. Split: this item ships the first proved cuts; #942 takes the rest of the cleanup under the same rule | not split, 185 files at a session each never ships and 0.22.0 waits on it; split, #942's pull requests meet the removal criterion in its own tables | **chosen**, and the split fell after phase 2: the owner closed this item there on 2026-10-15, because #923 waits on this item's merge, and phases 3–6 went to #942 |
```

```markdown
... ≈ 311 Linux-equivalent minutes ≈ US$2.49 (prices `read`, mid-2026), unchanged by this item; #943 decides the legs.
```

### ⬜ 2

```markdown
What it cannot read is stated: whether the test runs or is skipped on the sealing leg, and whether it asserts the rule (review is the reader of that).
```

```markdown
A target that resolves but is skipped on every leg, or asserts nothing, passes the resolution gate: the stated limit, with review as the reader.
```

```markdown
| #929 | Phase 6's ledger fragment step goes |
```

### ⬜ 3

```markdown
| ... | no line, no list: the check derives each case's mutants ...; a five-minute bound. Left in phase 4 with the check | ... |
| ... | ranked by how many siblings run a line, ...; four operators added (...). Left in phase 4 with the check | ... |
```

## Executed probes

| What was run | Result |
|---|---|
| `python3.12 .github/scripts/budget_check.py --baseline origin/release/v0.22.0` at `a7638aca` | exit 0, `budget-check: every gate row holds`; `suite-seconds` 6,031 of 7,841, `enforced-unresolved` 0, `unenforced:CONTRIBUTING.md` 22 of 22; `rounds-bytes` over at 193,857 of 142,823, a `report` row |
| `bin/test` over 23 modules: `test_arm_check`, the mutation-check module, `test_every_reader_ends_a_line_where_gfm_does`, the reader-registry, workflow, CI-step, Windows-shard, slow-case, contributor, line-wrap, one-word, pasted-passage, moved-rule, rules-command, claude-md-rules, old-roots, interpreter-census, no-real-identifiers, release-hygiene, budget-ratchet and work-item-set modules, `-q -rfEs` | exit 0: 1,103 passed, 4 skipped (two t-string cases below 3.14, and two whole-suite cases that skip when the suite is not collected) |
| `bin/test tests -q -p no:xdist -k 'test_the_durations_file_prices_the_suite or test_no_collected_id_carries_the_interpreters_path'` | exit 0: 2 passed, 9,029 deselected |
| `bin/mutation-check skills/verify/scripts/arm_check.py --replace '        lexer.escape = ""' '        pass' --tests "bin/test tests/test_arm_check.py -q -p no:xdist -k windows_command_line"` | exit 0 (`red`), failing at `tests/test_arm_check.py:1379`; `git status --short` empty after |
| `bin/mutation-check skills/verify/scripts/arm_check.py --replace a b --tests true --baseline-passed` | exit 2, `unrecognized arguments: --baseline-passed` |
| `git diff origin/release/v0.22.0 -- .github/workflows/test.yml` | empty |
| `git grep -n -i -E` over the class sweep's patterns, whole tree | outside this work item's records, only #944's `spec.md:48`, `:104` and `plan.md:31` |
| `uvx ruff@0.17.0 check` and `format --check` on `arm_check.py`, `mutation_check.py`, `tests/test_arm_check.py`, `tests/test_every_reader_ends_a_line_where_gfm_does.py` | exit 0 both |
| `gh api repos/…/rulesets/<id>` for both rulesets | `release`: no `required_status_checks` rule; `main`: requires `lint` |
| `ast` over `git show e5ee4c97:` the removed check and its test module; `--collect-only` of each test file named | 1,105 lines and 26 functions; 618 lines, 13 test functions, 27 ids; `SAMPLE` 35; 178 cases in the commit-gate file |
| The full suite, the repository-wide lint and the typecheck | not yet: the sealer's, once, and this round leaves nothing open that needs a fix |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| A row added to an existing parametrized function is not proved on its own | #942, already deferred in round 1; no job proves any case after phase 4, and #942 still owns the `test-cases` rows | #942's framer, with the repository owner |

Needs a fix: no
Loses a record or crashes: no

## Proof block

Opened in the round's clone at `a7638aca`:

- `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/spec.md`,
  `plan.md`, `questions.md`, `changelog.md`, `overview.md`,
  `phases/phase-4.md`, `rounds/round-6.md` (head), `rounds/round-6-report.md`
  (head), and the `## Deferred` tables of `rounds/round-1.md` to `round-6.md`
- `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/spec.md`
  (`:15`, `:27-28`, `:46-48`, `:77`, `:100-108`), `plan.md:31`,
  `questions.md:6`, `routing.md`
- the diffs `e5ee4c97..a7638aca` of `.github/workflows/test.yml`,
  `CONTRIBUTING.md`, `skills/verify/scripts/arm_check.py`,
  `skills/verify/scripts/mutation_check.py`, `tests/test_arm_check.py` and
  `tests/test_every_reader_ends_a_line_where_gfm_does.py`
- the diffs against `origin/release/v0.22.0` of the same files, and of
  `tests/undeclared_readers.txt`, `seal/budgets.md`, `seal/follow-up.md`,
  `docs/round-record-spec.md`, `docs/the-broad-gate.md` and
  `skills/code-review/orchestration.md`
- `bin/test`, `.github/scripts/run_tests.py` (venv lines),
  `tests/test_the_record_is_generated.py:2027-2033`,
  `tests/test_no_real_identifiers.py:1-25`
- `gh issue view 929`, `gh pr view 939`

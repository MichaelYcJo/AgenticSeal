# 1791876666-the-test-suite-is-held-to-a-budget — review round 7

| Field | Value |
|---|---|
| Target SHA | a7638acafb738ef74e51af0390f0f6ea8384b5dc |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #939 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | none |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 7 of #929, the first after the second reframe: phase 4's removal of the per-case check and the cases job over e5ee4c97..f8e86a40 and the orchestrator's a7638aca, the three recorded departures, whether the records say only what ships, and readiness for the sealer. Narrow checks only.

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

```markdown
| A. Derived: each new or changed case must be its file's only killer of a mutant the check draws from the lines it runs, the units it names and the changed shipped lines; one run per mutant; a five-minute bound | six review rounds each found the next way a case stops short of its body on the runner (`rounds/round-1.md` to `round-6.md`) | chosen on 2026-10-14, built in phases 2 and 3, and **removed in phase 4** by the owner's decision of 2026-10-15 |
```
```markdown
| H. Split: this item ships the first proved cuts; #942 takes the rest of the cleanup under the same rule | not split, 185 files at a session each never ships and 0.22.0 waits on it; split, #942's pull requests meet the removal criterion in its own tables | **chosen**, and the split fell after phase 2: the owner closed this item there on 2026-10-15, because #923 waits on this item's merge, and phases 3–6 went to #942 |
```
```markdown
... ≈ 311 Linux-equivalent minutes ≈ US$2.49 (prices `read`, mid-2026), unchanged by this item; #943 decides the legs.
```
```markdown
What it cannot read is stated: whether the test runs or is skipped on the sealing leg, and whether it asserts the rule (review is the reader of that).
```
```markdown
A target that resolves but is skipped on every leg, or asserts nothing, passes the resolution gate: the stated limit, with review as the reader.
```
```markdown
| #929 | Phase 6's ledger fragment step goes |
```
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

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `bin/test:35`, `bin/test.cmd:14` | round 1's 🔴 1 — fixed |
| round-1 | `tests/test_a_script_says_which_interpreter_it_needs.py:185`, `skills/verify/scripts/unverified_check.py:641` | round 1's 🟡 2 — fixed |
| round-1 | `.github/scripts/case_check.py:861` | round 1's 🟡 3 — fixed |
| round-1 | `.github/scripts/case_check.py:875` | round 1's 🟡 4 — fixed |
| round-1 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-2.md:6` | round 1's ⬜ 5 — answered |
| round-1 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/overview.md:7` | round 1's ⬜ 6 — answered |
| round-1 | `CONTRIBUTING.md:146` | round 1's ⬜ 7 — answered |
| round-1 | CI run 38658107547 | round 1's ❓ — out of verified scope |
| round-2 | `.github/scripts/case_check.py:848` | round 2's 🟡 1 — fixed |
| round-2 | `CONTRIBUTING.md:128`, `ruff.toml:41` | round 2's 🟡 2 — fixed |
| round-2 | `tests/test_a_script_says_which_interpreter_it_needs.py:409` | round 2's ⬜ 3 — answered |
| round-2 | `tests/test_a_script_says_which_interpreter_it_needs.py:395` | round 2's ⬜ 4 — answered |
| round-2 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/questions.md:25` | round 2's ⬜ 5 — answered |
| round-2 | `bin/test:36`, `bin/test.cmd:17` | round 2's 🟢 — confirmed |
| round-2 | `tests/test_a_script_says_which_interpreter_it_needs.py:401`, `ruff.toml:42` | round 2's 🟢 — confirmed |
| round-2 | `.github/scripts/case_check.py:599` | round 2's 🟢 — confirmed |
| round-2 | CI run 38664361183 | round 2's 🟢 — answered |
| round-3 | `.github/scripts/case_check.py:188` | round 3's 🟡 1 — deferred |
| round-3 | `.github/scripts/case_check.py:180` | round 3's 🟡 2 — deferred |
| round-3 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/rounds/round-2.md:5` | round 3's ⬜ 3 — answered |
| round-3 | `.github/scripts/case_check.py:862` | round 3's 🟢 — confirmed |
| round-3 | `CONTRIBUTING.md:124`, `ruff.toml:35` | round 3's 🟢 — confirmed |
| round-3 | `seal/budgets.md:40`, `seal/budgets.md:60` | round 3's 🟢 — confirmed |
| round-3 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/spec.md:99` | round 3's 🟢 — confirmed |
| round-3 | `.github/workflows/test.yml`, `CONTRIBUTING.md`, `tests/test_every_reader_ends_a_line_where_gfm_does.py` | round 3's 🟢 — confirmed |
| round-3 | CI run 38668484642 | round 3's 🟢 — confirmed |
| round-4 | `.github/scripts/case_check.py:190` | round 4's 🟡 1 — fixed |
| round-4 | `.github/workflows/test.yml:223` | round 4's ⬜ 2 — answered |
| round-4 | `.github/scripts/case_check.py:882` | round 4's 🟢 — confirmed |
| round-4 | `.github/scripts/case_check.py:193` | round 4's 🟢 — confirmed |
| round-4 | `.github/scripts/case_check.py:182` | round 4's 🟢 — confirmed |
| round-4 | `tests/test_a_new_case_protects_what_its_file_did_not.py:192` | round 4's 🟢 — confirmed |
| round-4 | `.github/scripts/case_check.py:76` | round 4's 🟢 — confirmed |
| round-4 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-2.md:464` | round 4's 🟢 — confirmed |
| round-4 | PR #939 | round 4's ❓ — out of verified scope |
| round-5 | `.github/scripts/case_check.py:993` | round 5's ⬜ 2 — answered |
| round-5 | `.github/scripts/case_check.py:192` | round 5's 🟢 — confirmed |
| round-5 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/plan.md:28` | round 5's 🟢 — confirmed |
| round-5 | `.github/scripts/case_check.py:871` | round 5's 🟢 — confirmed |
| round-6 | `.github/scripts/case_check.py:208` | round 6's 🟡 1 — deferred |
| round-6 | `.github/scripts/case_check.py:160` | round 6's 🟢 — confirmed |
| round-6 | `.github/scripts/case_check.py:985` | round 6's 🟢 — confirmed |
| round-6 | `tests/test_a_new_case_protects_what_its_file_did_not.py:610` | round 6's ⬜ 2 — deferred |
| round-6 | `.github/scripts/case_check.py:80` | round 6's ⬜ 3 — deferred |
| round-6 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/plan.md:30` | round 6's ⬜ 4 — deferred |
| round-6 | `.github/scripts/case_check.py:194` | round 6's 🟢 — confirmed |
| round-6 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/rounds/round-5.md:11` | round 6's 🟢 — confirmed |
| round-6 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/spec.md:95` | round 6's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| A row added to an existing parametrized function is not proved on its own | #942, already deferred in round 1; no job proves any case after phase 4, and #942 still owns the `test-cases` rows | #942's framer, with the repository owner |

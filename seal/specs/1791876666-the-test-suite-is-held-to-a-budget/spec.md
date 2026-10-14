# Feature Specification: the test suite is held to a budget

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | Nothing here asks a person. A new case is proven by a run CI makes, never by a sentence in a hand-back |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The regrowth check is a gate: a test seen red, the direction (it blocks more), a prompt budget of zero, platform honesty (it runs on ubuntu alone), a `Reads:` line per unit, `## Removes` below |
| `CONTRIBUTING.md` §*Running the checks*, the paragraph opening `**A case has a budget, and so does each leg.**` | Rewritten in place: what a case owes (its `Kills:` line), how a case is proven redundant, and the rows that hold the suite. Nothing is appended |
| `skills/implement/SKILL.md` §*2. Implement test-first, and let each rule name its test* | The convention this work extends to the case itself: a rule's `Enforced by:` line names the test that holds it, and the test is proved by the mutation it kills |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | The changelog goes to the work item's fragment; a removed or renamed case an `Enforced by:` line names moves that line to the case that holds the rule now |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below; a removal a phase makes that the frame did not name is a divergence in `overview.md` |
| `skills/agent-contract/SKILL.md` §15 | Today's rule for a new case, which the regrowth check makes a run CI performs rather than a thing a hand-back says |
| #930's `seal/specs/1791876665-…/spec.md` §*The budgets* | The ratchet every row proposed here follows: `measured ≤ ceiling ≤ measured × (1 + slack)`; a raise is a `Budget raised:` line in the pull request body |
| #931's `seal/specs/1791876667-…/spec.md` §*Scope* item 3 | A pull request that removes a twentieth of the suite's seconds brings the fresh `.test_durations` from its own run; `suite-seconds` falls in the same pull request |
| `skills/implement/SKILL.md` §*3. The SDD file set* | A check's verdict and a sentence a contributor acts on change, which is the top rung |

## Scope

**The problem.** The suite grew by appending: every fix planted cases and nothing took any out. Whether 13,714 cases guard 13,714 things is unknown, and nothing stops the next pull request from adding 44 more that guard nothing new. Time was the first frame's measure; it is a consequence here.

**In.** Three parts, in the owner's order.

1. **Compact what exists, proven by mutation.** A case guards a sentence of the unit under test, and it says which (`## A case names what it guards`). A case is removed only when a mutation table shows that every mutation it kills is killed by a case that stays (`## The removal criterion`). The whole suite is in scope, not the slow files; this item takes the module already done, the three enumeration files that hold 31 % of the cases, the byte-identical helper twins and the sealer file, and item C takes the long tail under the same rule (`plan.md` §*Alternatives considered* H).
2. **Change how a case is added**, so the suite does not regrow: a new or changed case carries a `Kills:` line, and CI runs it — red with the case, not red without it (`## The regrowth check`). This lands in 0.22.0 whatever else does.
3. **Hold it there.** Rows for #930's `seal/budgets.md`: `test-cases`, `test-lines`, `test-cases:<file>`, `test-lines:<file>`, `unguarded-files`, each a ratchet with its measurer in `budget_check.py` (`## Rows for seal/budgets.md`).

**Out, and whose.**

- **A case whose assertion reads this tree's prose** — `agents/`, `skills/*/SKILL.md`, `orchestration.md`, `docs/`, `README*`, `CONTRIBUTING.md`, `CLAUDE.md`, `templates/` — is #923's and moves with that text. By function body or a constant or helper the function names (`executed` at fcd735bc, `plan.md` §*Technical context*): 1,201 functions, 1,586 collected cases, in 135 files; the measure errs over, counting a case that writes `docs/` into a fixture tree. Every other case — 12,128 — is this item's. A phase that opens a file lists which of its cases it left to #923 in `phases/phase-N.md`.
- **Which legs run on a pull request** — item B, as before (`plan.md` D1–D4); D4 until it is framed.
- **The long tail of the cleanup** — item C: every test file this item's phases do not open, under the criterion and the `Kills:` convention this item ships, held by the rows this item adds.
- **`.test_durations`' cadence** (#931) and **the budget mechanism** (#930): read, not changed. A measurer this item adds to `budget_check.py` is a row's, not the ratchet's.
- **A suite-wide mutation census as a CI job.** The regrowth check runs a new case's own mutation; nothing re-runs every case's. Item C's tables are where the existing cases meet theirs.

## What the suite is

`executed` 2026-10-14 at fcd735bc on macOS arm64 unless labelled; commands in `plan.md` §*Technical context*.

| | Value |
|---|---|
| Collected cases | 13,714 in 185 files (`--collect-only`, 1.8 s); 5,478 test functions, 4,779 with a docstring (87 %), none with a line naming what it guards |
| Test code | 160,228 lines (`tests/*.py`); 157,826 in `test_*.py`; shipped Python 68,755 lines, so 2.33× |
| Where the cases are | three enumeration files hold 4,228 (31 %): `test_a_signer_declares_its_pact.py` 2,652 cases in 1,564 lines, `test_one_table_walker_reads_what_gfm_renders.py` 904, `test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py` 672 |
| Where the lines are | 18 files have over 40 lines per case; `test_the_seal_is_taken_once_by_the_sealer.py` is 10,142 lines for 457 cases |
| Guarded units | 1,529 top-level units in 65 shipped modules; 971 are named by a test function in a file that loads the module, 558 by none (36 %); 41 units are named by over 100 functions each (`hooks/gate.py#git` by 902) — the count reads names, not calls, so it errs both ways |
| Helpers | 1,770 top-level helpers in test files, 1,140 names; 249 are byte-identical twins of another file's (1,413 lines): `read` ×64 in 12 bodies, `flat` ×44 in 13, `repo` ×36 in 16, `git` ×30 in 11, `write` ×25 in 6; 64 files run `git init` themselves beside `conftest.py`'s 50 fixtures |
| Dead parametrizations | 3 `pytest.param` rows marked skip; 44 files carry `skipif` or `pytest.skip`; which rows never run on any leg is each phase's `-rs` to read |
| Time | 7,035 s priced over 13,279 entries (Windows, the committed file); 7,746 entries (58 %) under 0.05 s. #931's union prices 13,930 at 1.07× |
| CI minutes | medians of the last five green runs: ubuntu 9.9, Windows 42.4, macOS 21.6; `gh api …/jobs` on 38480484016, 38477758775, 38475370013, 38378390028, 38360379166 |

**What one fast module shows** (`mutation-check`, the file restored, `git status` clean after each). Six mutations across two files:

| Module · cases | Mutation | Killers |
|---|---|---|
| `issue_claims_check.py` · 50 cases, 0.2 s | `;` dropped from `SENTENCE_END` | **survived** |
| the same | `\b` dropped from `ISSUE_REF` | **survived** |
| `hooks/config.py#table_end`, run under the 904- and 2,652-case files | a heading no longer ends a table | 1 (`test_every_way_the_table_ends_is_read_or_refused`) |
| the same | a list item no longer ends a table | 2, the same function |
| the same | a thematic break no longer ends a table | 2, the same function |
| `#table_cells` | an even run of backslashes before a pipe read as a cell | 2 (`test_a_pipe_after_an_even_run_of_backslashes_is_refused`) |
| `#table_cells` | `\|` left unescaped in a cell | **survived** |

So the case count is not where the guarding is. The 904-row enumeration kills none of the four `table_end` mutations, because its property lets the walker refuse; each sentence there is held by one function, and three sentences in two fast modules are held by nothing. Phase 1 found the other shape: 156 of 226 corpus rows killed one mutant. Compact means both — rows that kill what a sibling kills leave, and a sentence nobody kills gets one case.

## A case names what it guards

Every test function carries one `Kills:` line in its docstring: the path of a unit under test and one replacement that `mutation-check <path> --replace OLD NEW` applies unchanged, such that the file's cases are red with this function and not red without it. One line per function; a parametrized function's rows share it. For a case that pins prose, the path is the document and OLD is the sentence. The grammar round-trips any string and is the work's to fix (`questions.md`). A file whose every function carries the line is out of `tests/unguarded-files.txt`; the list holds the 185 files at this frame and only shrinks (the shape of `tests/undeclared_readers.txt`).

## The removal criterion

A case is removed only when a mutation table shows it guards nothing alone: a battery of mutations of the unit under test, each killed (`mutation-check` exit 0) by the file as it stands, is still killed by the file without the case. The battery is drawn from what the file's cases say they guard — each case's `Kills:` line, or its docstring where it has none yet — and for an enumeration it holds one mutation per kind the enumeration names, so a row that a kind's mutation needs stays. A candidate whose guarded sentence no mutation negates gets its mutation added before anything is removed; a sentence the battery shows unguarded gets one case, which the suite may grow by. A case whose bare run shows it asserts nothing is removed on that showing. A byte-identical helper twin is removed on the hash alone. Judgment removes nothing. The table — mutation · killed before · killed after · the sentence's one remaining killer — is in each phase's `phases/phase-N.md`, and every kept case leaves the phase with its `Kills:` line.

## The regrowth check

A new or changed test function — new at HEAD against the merge base by id, or whose source differs — is read by `.github/scripts/case_check.py`, a job of `test.yml` on ubuntu after collection. For each, it runs the function's file twice through `mutation-check`: with the function, which must be red, and with it deselected, which must not be. A function with no `Kills:` line, a line whose replacement does not land, a mutation the function does not kill, or one the file kills without it fails the job naming the function. Exit 0 every function proved, 1 a function named, 2 nothing compared. Gate, not report: a report that is read by nobody is the mechanism #908's table already had. Platform honesty: it runs on ubuntu alone; a case guarding a Windows-only sentence proves itself on a run that skips there, which the line's path cannot fix and the phase record says. Its scope is the function's file: a case in another file that kills the same mutation is not seen, and the frozen list is where the suite-wide question is answered, file by file.

## Rows for `seal/budgets.md`

Proposed to #930's file, measured by this item's measurers in `budget_check.py`, each a `gate` under the ratchet. Ceilings at this frame; targets at this item's close, re-set from each phase's table where the table shows less.

| Row | Measured as | Ceiling now | Target · slack |
|---|---|---|---|
| `test-cases` | ids `pytest --collect-only -q` lists | 13,714 | ≤ 10,500 · 2 % |
| `test-lines` | lines of `tests/*.py` | 160,228 | ≤ 150,000 · 2 % |
| `test-cases:<file>` | one file's collected ids, listed at ≥ 200 | the eight files at ≥ 200 | the three enumeration files ≤ 400 each · 5 % |
| `test-lines:<file>` | one file's lines, listed at ≥ 2,000 | the 15 files at ≥ 2,000 | the sealer file ≤ 7,000 · 5 % |
| `unguarded-files` | lines of `tests/unguarded-files.txt` | 185 | ≤ 175 · +0 |

`suite-seconds`, `slow-file:*` and `ci-minutes:*` stay #930's and fall as a consequence: each cut pull request brings the union from its own run (#931), so the rows move with the cut.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 one module first | phase 1's record stands: 367 → 179 cases, 1,137 → 368 Windows seconds, m1–m5 red before and after, the mutation table in `phases/phase-1.md` | `read`; the enumeration phase repeats the shape on `test_a_signer_declares_its_pact.py`: cases, lines, seconds and the table before and after |
| S2 a new case without its line | a pull request adds a test function with no `Kills:` line | `case_check.py` exit 1 naming the function; the job is red |
| S3 a new case that kills nothing new | the line's mutation is red with the function deselected | exit 1 naming the function and the case that already kills it |
| S4 a new case proven | red with, green without | exit 0; the summary lists each function and its two runs |
| S5 a case that pins prose | the line's path is a `.md` and OLD its sentence | S4 holds through `mutation-check` on the document |
| S6 the list only shrinks | a file leaves `tests/unguarded-files.txt` | every function in it carries the line (`case_check.py` reads the file whole); a file added to the list fails `unguarded-files` |
| S7 a removal is proven | each phase's table | every mutation red before and after; the remaining killer named; a survivor gets a case |
| S8 the rows move with the cut | a phase lowers `test-cases` and the others; the union downloaded from the phase's run | `budget_check.py` exit 0; `test_the_durations_file_prices_the_suite` green |
| S9 the rules follow | a removed function an `Enforced by:` line names; a renamed one | the line names the case that holds the rule now; `budget_check.py`'s `enforced-unresolved` at 0 |
| S10 docs state the rule | the `CONTRIBUTING.md` paragraph | rewritten in place; `docs-history:*` at +0 |
| S11 nothing asks a person | the whole change | no `AskUserQuestion`, no prompt, no box |
| S12 every new unit declares | `case_check.py` and the measurers | a `Reads:` line each; the census passes |

## Data & interfaces

`.github/scripts/case_check.py` — `--baseline REF`, `--root DIR`, `--list tests/unguarded-files.txt`; stdout and `$GITHUB_STEP_SUMMARY`; names no machine path. `tests/unguarded-files.txt` — one test file path per line, sorted. `budget_check.py` — five measurers and two per-file tables (`## Large test files`, `| File | Cases ceiling | Lines ceiling |`) in the shape of `## Slow test files`. A `Kills:` docstring line per test function.

## Removes

nothing — the frame names no unit: which cases leave is each phase's mutation table and which helper twins leave is the hash, so every removed test function or helper is a divergence row in `overview.md`, and an `Enforced by:` line naming it moves to the case that stays, as `docs/the-reader-registry.md` §*A frame names what its work removes* has it. The `CONTRIBUTING.md` paragraph is rewritten, not removed.

## Open questions → questions.md

Framed 2026-10-13 by framer, before the build.
Reframed 2026-10-14 by framer, after round 0.

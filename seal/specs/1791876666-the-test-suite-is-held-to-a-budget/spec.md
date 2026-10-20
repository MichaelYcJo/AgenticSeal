# Feature Specification: the test suite is held to a budget

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | Nothing here asks a person. The cuts and the launcher are held by cases CI runs, never by a sentence in a hand-back |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | No gate on the base changes: the `cases` job this branch added leaves before the merge, so the release branch never carried it (`## The per-pull-request check leaves`). The launcher is a new refusal, and carries a test seen red for each case, a prompt budget of zero, a `Reads:` line per unit and `## Removes` below |
| `CONTRIBUTING.md` §*Running the checks*, the paragraph opening `**A case is owed by a mutant only it kills**` | Removed, not rewritten. The paragraph and its `Enforced by: .github/scripts/case_check.py::check` were this branch's own, and what a case owes stands in no file of the tree a paragraph could cite with an enforcer: the layout, a success and a failure case per function and the placement check are #942's, the smith's and warden's rules #923's. The paragraph after it, `**A case has a budget, and so does each leg.**`, is unchanged |
| `skills/implement/SKILL.md` §*2. Implement test-first, and let each rule name its test* | Unchanged by this item: a rule's `Enforced by:` line names the test that holds it. What a test itself owes is #942's and #923's |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | The changelog goes to the work item's fragment; a removed or renamed case an `Enforced by:` line names moves that line to the case that holds the rule now |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below; a removal the frame did not name is a divergence in `overview.md` |
| `docs/commit-review-gate-spec.md` §*Registration* | A hook that fails is skipped and said, and the call goes ahead. That is why the launcher stands in front of the `bin/` wrappers and not in front of `hooks/hooks.json`, where exit 2 blocks the call |
| `skills/agent-contract/SKILL.md` §15 | The rule for a new case stays the hand-back's: the smith says how it saw the case red. Phases 2 and 3 made that a run CI performs; since phase 4 it is not (`## Scope` item 2) |
| #930's `seal/specs/1791876665-…/spec.md` §*The budgets* | The ratchet the rows this item lowers stand under: `measured ≤ ceiling`, a `one-sided` row's ceiling 1.3 times its reading, rounded up; a lowering needs no `Budget raised:` line |
| #931's `seal/specs/1791876667-…/spec.md` §*Scope* item 3 | A pull request that removes a twentieth of the suite's seconds brings the `.test_durations` its cut leaves; `suite-seconds` falls in the same pull request |
| `skills/implement/SKILL.md` §*3. The SDD file set* | A check's verdict and a sentence a contributor acts on change, which is the top rung |

## Scope

**The problem.** The suite grew by appending: every fix planted cases and nothing took any out. Whether 13,714 cases guard 13,714 things is unknown, and nothing stopped the next pull request from adding 44 more that guard nothing new. Time was the first frame's measure; it is a consequence here.

**In.** What this item ships. The owner closed it at phase 2 on 2026-10-15, and the rest of the plan went to #942.

1. **One module compacted, proven by mutation.** `tests/test_the_commit_gate_decides_at_the_commit.py` replays `SAMPLE`, one or more representatives of each corpus subgroup, where it replayed the whole corpus (phase 1). The sealer file's six corpus layouts that differ from a kept twin only by a junit option leave with their 12 ids (f13b0dfa). Each removal meets `## The removal criterion`.
2. **No mutation check runs on a pull request** (`## The per-pull-request check leaves`). The regrowth check phase 2 built, `.github/scripts/case_check.py` and the `cases` job, leaves the tree in phase 4 with its cases and every line that stood only on it. **What this item no longer claims, said once here:** that a test case is owed by a mutant only it kills in its file, that a new or changed case is proved on the pull request, that a pull request's changed shipped lines are mutated on it, or that any check knows whether a case ran its body on the runner. Rounds 1–6 each found the next spelling of that last question — a marker skip, a body skip, an imperative xfail, a unittest expected failure on a method and on a class, pytest's own stop inside one, a skipped subtest. The reframe after round 6 kept the changed-lines half as a report, and the owner chose removal instead on 2026-10-15 (#929, *What this item ships, and where the rest went*, item 3): that half could only report, because a mutant that changes nothing observable is no defect, and within its five-minute bound it reached about fifty lines. Which cases a file needs is #942's (one file per module, grouped by function; a success and a failure case per function; duplicate pairs named; a sweep each release) and #923's (the smith's and warden's rules); `mutation-check` and the mutation table stay as the tool #942's release sweep runs, without a bound (`## The removal criterion`).
3. **The rows the cuts moved are lowered** in #930's `seal/budgets.md` (`## Rows for seal/budgets.md`).
4. **One launcher holds the Python floor.** `hooks/launch.py` holds `FLOOR`, and every `bin/` wrapper but `bin/test`, and its `.cmd` twin, runs its script through it; `bin/test`'s runner starts on any `python3` because it builds the virtualenv at the floor (`hooks/launch.py`'s docstring). Below the floor it refuses with one sentence and exits 2 before the script is read; at or above it the script runs as if run directly. The floor's eight copies and the cases that pinned them leave (`## Removes`).

**Out, and whose.**

- **A case whose assertion reads this tree's prose** — `agents/`, `skills/*/SKILL.md`, `orchestration.md`, `docs/`, `README*`, `CONTRIBUTING.md`, `CLAUDE.md`, `templates/` — is #923's and moves with that text. By function body or a constant or helper the function names (`executed` at fcd735bc, now f13b0dfa, `plan.md` §*Technical context*): 1,201 functions, 1,586 collected cases, in 135 files; the measure errs over, counting a case that writes `docs/` into a fixture tree. A cut that opens a file lists which of its cases it left to #923.
- **Which legs run on a pull request** — #943 (item B); every leg on every pull request until it is framed.
- **The rest of the cleanup — #942.** The three enumeration files that hold 31 % of the cases, the 249 byte-identical helper twins, the sealer file's inventory of its `run_gate` call sites and its mutation battery, and every test file this item did not open, each under `## The removal criterion`. With them go the rows the frame proposed for `seal/budgets.md` — `test-cases`, `test-lines`, `test-cases:<file>` and `test-lines:<file>`, their measurers in `budget_check.py` and a per-file table for them — whose ceilings are #942's to set from its own tables.
- **`unguarded-files` and `tests/unguarded-files.txt`** — not built and not moved. The list was to hold the files whose cases still owed a written line, and no case owes one (the owner's decisions of 2026-10-14).
- **`hooks/hooks.json` and the git hook stubs** stay outside the launcher. A hook below the floor is protected by `dispatch.py`'s own isolation, as before (`phases/phase-2.md` gives the grounds).
- **`.test_durations`' cadence** (#931) and **the budget mechanism** (#930): read, not changed. This item adds no row and no measurer.
- **A mutation check of any shape in CI** — per case, per changed line, or over the suite. #942's release sweep is where cases meet their mutations, through `mutation-check`.
- **Whether a case ran its body on the runner, and what one case owes** — out since phase 4, by the owner's decision of 2026-10-15 (item 2 above). Nothing in the tree reads pytest's call report for it.

## What the suite is

`executed` 2026-10-14 at fcd735bc, before the rebase onto #944 (now f13b0dfa), on macOS arm64 unless labelled; commands in `plan.md` §*Technical context*.

| | Value |
|---|---|
| Collected cases | 13,714 in 185 files (`--collect-only`, 1.8 s); 5,478 test functions, 4,779 with a docstring (87 %), none with a line naming what it guards |
| Test code | 160,228 lines (`tests/*.py`); 157,826 in `test_*.py`; shipped Python 68,755 lines, so 2.33× |
| Where the cases are | three enumeration files hold 4,228 (31 %): `test_a_signer_declares_its_pact.py` 2,652 cases in 1,564 lines, `test_one_table_walker_reads_what_gfm_renders.py` 904, `test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py` 672 |
| Where the lines are | 18 files have over 40 lines per case; `test_the_seal_is_taken_once_by_the_sealer.py` is 10,142 lines for 457 cases |
| Guarded units | 1,529 top-level units in 65 shipped modules; 971 are named by a test function in a file that loads the module, 558 by none (36 %); 41 units are named by over 100 functions each (`hooks/gate.py#git` by 902) — the count reads names, not calls, so it errs both ways |
| Helpers | 1,770 top-level helpers in test files, 1,140 names; 249 are byte-identical twins of another file's (1,413 lines): `read` ×64 in 12 bodies, `flat` ×44 in 13, `repo` ×36 in 16, `git` ×30 in 11, `write` ×25 in 6; 64 files run `git init` themselves beside `conftest.py`'s 50 fixtures |
| Dead parametrizations | 3 `pytest.param` rows marked skip; 44 files carry `skipif` or `pytest.skip`; which rows never run on any leg is a cut's `-rs` to read |
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

## The removal criterion

A case is removed only when a mutation table shows it guards nothing alone: a battery of mutations of the unit under test, each killed (`mutation-check` exit 0) by the file as it stands, is still killed by the file without the case. The battery is drawn from what the file's docstrings say its cases guard, and for an enumeration it holds one mutation per kind the enumeration names, so a row that a kind's mutation needs stays. A candidate whose guarded sentence no mutation negates gets its mutation added before anything is removed; a sentence the battery shows unguarded gets one case, which the suite may grow by. A case whose bare run shows it asserts nothing is removed on that showing. A byte-identical helper twin is removed on the hash alone. Judgment removes nothing. The table — mutation · killed before · killed after · the sentence's one remaining killer — is in the record of the phase that made the cut: phase 1's in `phases/phase-1.md`, the sealer cut's in `phases/phase-2.md`.

## The per-pull-request check leaves

A pull request meets no mutation check. `.github/scripts/case_check.py`, the `cases` job of `test.yml` and the test module that held the check leave the tree, and so does every line that stood only on them (`## Removes`). Nothing replaces them on the pull request; the base, `release/v0.22.0`, never carried any of them, so after the merge the tree is what it was before this item on that axis.

- **What stays.** `mutation-check`, its wrapper and its script, with the options it had on the base, as the tool #942's release sweep runs per module without a bound, and the mutation table `## The removal criterion` names. Its `--tests` is split by `arm_check.py#command_words`, which keeps a Windows path's backslashes; that fix stays, and its case moves to `tests/test_arm_check.py`, the group of the function it calls.
- **What a pull request's tests are held to instead.** Nothing in this item. The layout, a success and a failure case per function, the placement check and the named duplicate pairs are #942's; the smith's and warden's rules for a new test are #923's.
- **Why removal and not the report.** The reframe after round 6 kept the changed-lines half: mutate a pull request's changed shipped lines, run the test files that name the module, list a line nothing kills and fail nothing. The owner chose removal on 2026-10-15 (#929 item 3): a mutant that changes nothing observable is no defect, so that check could only report, and within its five-minute bound it reached about fifty of a release's hundreds or thousands of changed lines, so a large change went mostly unread.

How it errs: a changed line nothing tests reaches the release branch unread, and what finds it is #942's release sweep, a mutation table per module, or a defect. The removed check would not have caught most of them either: it reported rather than failed, and it reached about fifty lines a pull request.

## Rows for `seal/budgets.md`

This item adds no row. It lowers the `one-sided` rows its cuts moved, each to 1.3 times its reading at the 1132 price level, rounded up, the rule `seal/budgets.md` states:

| Row | Reading at the base | Reading at this branch | Ceiling before | Ceiling now |
|---|---|---|---|---|
| `suite-seconds` | 6,854 | 6,031 | 9,185 | 7,841 |
| `slow-file:tests/test_the_commit_gate_decides_at_the_commit.py` | 1,178 | 389 | 1,479 | 506 |
| `slow-file:tests/test_the_seal_is_taken_once_by_the_sealer.py` | 946 | 915 | 1,538 | 1,190 |

The `ci-minutes:*` rows are read off a CI run, not off the tree, so the release lowers them from the trend line. The rows the frame proposed are #942's (`## Scope`).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 one module first | phase 1's record stands: 367 → 179 cases, 1,137 → 368 Windows seconds, m1–m5 red before and after, the mutation table in `phases/phase-1.md` | `read` |
| S2 no check on the pull request | a pull request into the release branch | `test.yml` has no `cases` job and no step runs a mutation; `test.yml` reads as it did on the base |
| S3 nothing names the removed check | the tree after phase 4 | `git grep 'case_check\|cases job'` names only records of what happened: phase and round records, and the history sentences of this work item and of #944's frame |
| S4 `mutation-check` as it was | `mutation-check <file> --replace OLD NEW --tests CMD` | the verdicts, exit codes and baseline run of the base; `--baseline-passed` is refused as an unknown option, exit 2 |
| S5 a Windows path in `--tests` | `command_words` on a line holding `C:\py\python.exe` | on Windows the backslashes stay; on POSIX `shlex.split`'s reading; the case sits in `tests/test_arm_check.py` |
| S6 the rules follow the removal | the `CONTRIBUTING.md` paragraph and its `Enforced by: .github/scripts/case_check.py::check` | both gone; `enforced-unresolved` at 0 and `unenforced:CONTRIBUTING.md` unchanged |
| S7 a removal is proven | each cut's table | every mutation red before and after; the remaining killer named |
| S8 the rows move with the cut | the cut's `.test_durations` in the tree | `suite-seconds` and the two `slow-file` rows lowered to 1.3 times their readings; `budget_check.py` exit 0; `test_the_durations_file_prices_the_suite` green |
| S9 the rules follow | a removed case an `Enforced by:` line names | the line names the case that holds the rule now; `budget_check.py`'s `enforced-unresolved` at 0 |
| S10 docs state the rule | the `CONTRIBUTING.md` paragraph on the floor | rewritten in place; `docs-history:*` at +0 |
| S11 nothing asks a person | the whole change | no `AskUserQuestion`, no prompt, no box |
| S12 every new unit declares | `hooks/launch.py`, and the units this item changed in shipped modules | a `Reads:` line each; the census passes |
| S14 below the floor | any `bin/` command but `bin/test` run on a Python older than 3.12 | the launcher's one sentence, exit 2, the script never read |
| S15 at the floor | the same command on 3.12 or newer | the script runs with the arguments, `sys.path[0]`, `__file__` and exit code a direct run gives |

S13, S16 and S17 described the changed-lines check and left with it in phase 4.

## Data & interfaces

- `mutation-check <file> --replace OLD NEW --tests CMD [--timeout S] [--cwd DIR]` — the options of the base. Its `--tests`, and `arm-check`'s, are split by `arm_check.py#command_words`, which on Windows keeps a backslash as a character of its word.
- `hooks/launch.py <script> [arguments...]` — `FLOOR = (3, 12)`, the floor's one source; `.github/scripts/run_tests.py` reads it, and a case holds `ruff.toml` equal. Exit 2 below the floor or with no script named; otherwise the script's own.
- `seal/budgets.md` — three ceilings lowered; no row, table or measurer added.

## Rule changes

- nothing
  why: internal: one launcher holds the Python floor, held by
    tests/test_a_script_says_which_interpreter_it_needs.py, and one module replays a
    sample of its corpus; the per-pull-request case check left within the item.

## Removes

- The floor's eight copies: the guard (`FLOOR`, `FLOOR_TEXT`, `BELOW_FLOOR`, `below_floor`) in `skills/code-review/scripts/round_record.py`, `skills/settle/scripts/settle.py`, `skills/settle/scripts/fold_check.py`, `skills/verify/scripts/broad_gate.py`, `skills/verify/scripts/payload_meter.py`, `skills/verify/scripts/seal_stamp.py` and `.github/scripts/claude_block.py`, and `run_tests.py`'s own `FLOOR` number, which now reads the launcher's.
- The cases that pinned those copies: the 18 functions `tests/test_a_script_says_which_interpreter_it_needs.py` held, its census of constructs above the floor (`ABOVE_THE_FLOOR`, `CLASSIFIED`, `shipped_python`) with the `seal/follow-up.md` row it fed, and the raised-floor case in each of the payload-meter and `CLAUDE.md`-block modules. Five launcher cases replace them.
- 191 parametrized ids of `test_s2_a_commit_bash_makes_into_an_undeclared_repository_does_not_land`, which now runs `SAMPLE`, and phase 1's `test_every_sampled_name_is_a_corpus_row`, whose mutant S2's own row kills.
- The sealer file's six junit-twin layouts (`Qf-row`, `Qf-env`, `Qf-ini`, `R1-row`, `R1-ini`, `Q8`) and their 12 ids.
- The 227 ids those removals take out of `.test_durations`, and the 13 lines of `tests/undeclared_readers.txt` whose units were removed or now declare their `Reads:` line.
- **Phase 4, the regrowth check whole:** `.github/scripts/case_check.py`, 1,105 lines — 26 functions (`check`, `traced_run`, `drawn`, `sole_killer` and the rest) and 21 module constants, the tracer's source among them — with the verdicts a person read in its step summary: `proved — the only killer in its file of …`, `kills nothing its file does not …`, `not proved: none of its ids ran its call to the end on this runner …` and `restructure: test the decision directly …`.
- **Phase 4, its cases:** `tests/test_a_new_case_protects_what_its_file_did_not.py`, 618 lines, 13 test functions and 27 ids, 15 of them `test_each_real_path_end_to_end`'s rows. One case outlives the module: `test_a_windows_command_line_keeps_the_backslashes_of_its_paths` calls `arm_check.py#command_words`, which stays, and moves to `tests/test_arm_check.py`. No line of `.test_durations` named the module (`executed` at e5ee4c97), so none leaves it.
- **Phase 4, the job and its comment:** the `cases` job in `.github/workflows/test.yml`, 33 lines with its 15-line comment.
- **Phase 4, what stood only on the check:** `mutation-check --baseline-passed`, the `baseline` parameter of `mutation_check.py#mutation_run` and the docstring paragraph and comment that named `case_check.py` as its caller, with `test_a_caller_that_ran_the_baseline_skips_it_in_mutation_check`; the two `OUT_OF_CLASS` rows `tests/test_every_reader_ends_a_line_where_gfm_does.py` held for `case_check.py`'s `main` and `traced_run`; the clause of `arm_check.py#command_words`' docstring naming `case_check.py`'s `--runner`.
- **Phase 4, the contributor's paragraph:** `**A case is owed by a mutant only it kills**` in `CONTRIBUTING.md` §*Running the checks*, 17 lines, and its `Enforced by: .github/scripts/case_check.py::check`. It is removed rather than rewritten: what a case owes is #942's layout and #923's rules, and neither stands in the tree yet for a paragraph to state with an enforcer.
- **Phase 4, the changelog's `Added` entry** for the check, and its `### Added` heading, which held nothing else.

Each of these that the frame did not name is a divergence row in `overview.md`; the `Enforced by:` line that named the removed guard cases names the launcher and its cases now (`docs/round-record-spec.md` §*What it refuses before anything is written*).

## Open questions → questions.md

Framed 2026-10-13 by framer, before the build.
Reframed 2026-10-14 by framer, after round 0.
Reframed 2026-10-15 by framer, after round 3.
Reframed 2026-10-15 by framer, after round 6.

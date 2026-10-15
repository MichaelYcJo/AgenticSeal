# Feature Specification: the test suite is held to a budget

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | Nothing here asks a person. A new case is proven by a run CI makes, never by a sentence in a hand-back |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The `cases` job changes what it refuses, and after round 6 in the direction of refusing less: it reports a changed line nothing kills and fails on nothing (`## The changed-lines check`), and the grounds a pull request owes for that direction are `plan.md` §*Alternatives considered*, T against U. A test seen red for each row, a prompt budget of zero, platform honesty (ubuntu alone), a `Reads:` line per unit, `## Removes` below |
| `CONTRIBUTING.md` §*Running the checks*, the paragraph opening `**A case is owed by a mutant only it kills**` | Rewritten in place, opening `**A pull request's changed shipped lines are mutated**`: what the `cases` job runs, that a survivor is listed and fails nothing, that a skipped case kills nothing, and that a case leaves only on a mutation table; `Enforced by:` keeps naming `.github/scripts/case_check.py::check`. Nothing is appended, and the paragraph after it, `**A case has a budget, and so does each leg.**`, is unchanged |
| `skills/implement/SKILL.md` §*2. Implement test-first, and let each rule name its test* | Unchanged by this item: a rule's `Enforced by:` line names the test that holds it. What a test itself owes is #942's and #923's after round 6 |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | The changelog goes to the work item's fragment; a removed or renamed case an `Enforced by:` line names moves that line to the case that holds the rule now |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below; a removal the frame did not name is a divergence in `overview.md` |
| `docs/commit-review-gate-spec.md` §*Registration* | A hook that fails is skipped and said, and the call goes ahead. That is why the launcher stands in front of the `bin/` wrappers and not in front of `hooks/hooks.json`, where exit 2 blocks the call |
| `skills/agent-contract/SKILL.md` §15 | The rule for a new case stays the hand-back's: the smith says how it saw the case red. Before round 6 this item made that a run CI performs; it no longer does (`## Scope` item 2) |
| #930's `seal/specs/1791876665-…/spec.md` §*The budgets* | The ratchet the rows this item lowers stand under: `measured ≤ ceiling`, a `one-sided` row's ceiling 1.3 times its reading, rounded up; a lowering needs no `Budget raised:` line |
| #931's `seal/specs/1791876667-…/spec.md` §*Scope* item 3 | A pull request that removes a twentieth of the suite's seconds brings the `.test_durations` its cut leaves; `suite-seconds` falls in the same pull request |
| `skills/implement/SKILL.md` §*3. The SDD file set* | A check's verdict and a sentence a contributor acts on change, which is the top rung |

## Scope

**The problem.** The suite grew by appending: every fix planted cases and nothing took any out. Whether 13,714 cases guard 13,714 things is unknown, and nothing stopped the next pull request from adding 44 more that guard nothing new. Time was the first frame's measure; it is a consequence here.

**In.** What this item ships. The owner closed it at phase 2 on 2026-10-15, and the rest of the plan went to #942.

1. **One module compacted, proven by mutation.** `tests/test_the_commit_gate_decides_at_the_commit.py` replays `SAMPLE`, one or more representatives of each corpus subgroup, where it replayed the whole corpus (phase 1). The sealer file's six corpus layouts that differ from a kept twin only by a junit option leave with their 12 ids (f13b0dfa). Each removal meets `## The removal criterion`.
2. **A pull request's changed shipped lines are mutated on the pull request** (`## The changed-lines check`). Each changed line of a `.py` outside `tests/` gets its mutants; the test files that name the changed file run under each; a line none of whose mutants fails a case is listed in the job's summary. A skipped case kills nothing and is named for nothing. The check reports and never fails on a survivor; `plan.md` §*Alternatives considered* T and U hold the grounds and the six-month failure mode of each. **What this item no longer claims, said once here:** that a test case is owed by a mutant only it kills in its file, that a new or changed case is proved on the pull request, or that the check knows whether a case ran its body on the runner. Rounds 1–6 each found the next spelling of that last question — a marker skip, a body skip, an imperative xfail, a unittest expected failure on a method and on a class, pytest's own stop inside one, a skipped subtest — and the owner took the per-case check and the tracer's never-ran machinery out of the gate on 2026-10-15 (#929, *What this item ships, and where the rest went*, item 3). Which cases a file needs is #942's (one file per module, grouped by function; duplicate pairs named; a sweep each release) and #923's (the smith's and warden's rules); `mutation-check` and the mutation table stay as the tool those use (`## The removal criterion`).
3. **The rows the cuts moved are lowered** in #930's `seal/budgets.md` (`## Rows for seal/budgets.md`).
4. **One launcher holds the Python floor.** `hooks/launch.py` holds `FLOOR`, and every `bin/` wrapper but `bin/test`, and its `.cmd` twin, runs its script through it; `bin/test`'s runner starts on any `python3` because it builds the virtualenv at the floor (`hooks/launch.py`'s docstring). Below the floor it refuses with one sentence and exits 2 before the script is read; at or above it the script runs as if run directly. The floor's eight copies and the cases that pinned them leave (`## Removes`).

**Out, and whose.**

- **A case whose assertion reads this tree's prose** — `agents/`, `skills/*/SKILL.md`, `orchestration.md`, `docs/`, `README*`, `CONTRIBUTING.md`, `CLAUDE.md`, `templates/` — is #923's and moves with that text. By function body or a constant or helper the function names (`executed` at fcd735bc, now f13b0dfa, `plan.md` §*Technical context*): 1,201 functions, 1,586 collected cases, in 135 files; the measure errs over, counting a case that writes `docs/` into a fixture tree. A cut that opens a file lists which of its cases it left to #923.
- **Which legs run on a pull request** — #943 (item B); every leg on every pull request until it is framed.
- **The rest of the cleanup — #942.** The three enumeration files that hold 31 % of the cases, the 249 byte-identical helper twins, the sealer file's inventory of its `run_gate` call sites and its mutation battery, and every test file this item did not open, each under `## The removal criterion`. With them go the rows the frame proposed for `seal/budgets.md` — `test-cases`, `test-lines`, `test-cases:<file>` and `test-lines:<file>`, their measurers in `budget_check.py` and a per-file table for them — whose ceilings are #942's to set from its own tables.
- **`unguarded-files` and `tests/unguarded-files.txt`** — not built and not moved. The list was to hold the files whose cases still owed a written line, and no case owes one (the owner's decisions of 2026-10-14).
- **`hooks/hooks.json` and the git hook stubs** stay outside the launcher. A hook below the floor is protected by `dispatch.py`'s own isolation, as before (`phases/phase-2.md` gives the grounds).
- **`.test_durations`' cadence** (#931) and **the budget mechanism** (#930): read, not changed. This item adds no row and no measurer.
- **A suite-wide mutation census as a CI job.** The check mutates the lines a pull request changed; nothing re-runs the suite's. #942's tables are where the existing cases meet theirs.
- **Whether a case ran its body on the runner, and what one case owes** — out since round 6, by the owner's decision of 2026-10-15 (item 2 above). The check names no case, and no part of it reads pytest's call report.
- **A changed `.md` line.** Only a case that pins the sentence kills a prose line removed, and those cases are #923's; mutating every edited sentence would list a docs pull request's whole diff as survivors (`plan.md` alternative AA).

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

## The changed-lines check

`.github/scripts/case_check.py`, the `cases` job of `test.yml`, on ubuntu, on pull requests. It reads the lines the pull request changed in shipped code — a `.py` outside `tests/`, against the merge base with `--baseline` — and asks of each whether a case somewhere in the suite notices the line broken. It reads no test function, names no case, and decides nothing about whether a case ran.

- **The candidates.** The suite cannot run under every mutant: one ubuntu run is 9.9 minutes at the medians (`plan.md` §*Technical context*) and the whole check has five. So for each changed file the candidates are the test files that name it, by its basename (`gate.py`) or its import (`hooks.gate`), best-named first. Measured (`executed` 2026-10-15 at 6f512f12, `grep -l` over `tests/test_*.py` for each shipped basename): 68 of the 69 shipped modules are named by at least one test file, the median by 6; `hooks/gate.py` by 48, whose cases `.test_durations` prices at 2,706 Windows seconds; `.github/scripts/case_check.py` by 2, at 9 seconds. The candidates of one changed file run once, together, as they stand, under the tracer that records the lines each case's call runs and its seconds — that is all the tracer records — and must pass. The run is bounded by half of what is left of the check's bound, and the candidates are taken best-named first only as far as the committed `.test_durations` prices them inside that half; the changed files go cheapest candidate set first, so one heavy module's candidates do not starve the others. A changed file whose candidates do not fit, or do not pass as they stand, has its lines counted `not run`, with the reason, and the check moves on.
- **The mutants.** Each changed line's mutants are `mutants_of`'s — the operators the module docstring lists — the statement removed first. Under a mutant, through `mutation-check --baseline-passed`, the cases whose call ran the line run; where no call ran it (a line run at import, in a fixture, or in a child process the tracer cannot see), the candidate files run whole, and those mutants go after every traced line has its verdict, in what is left. A line is **killed** at its first mutant that fails a case, and its other mutants are not run. A line is a **survivor** when every one of its mutants ran and none failed a case; a line one of whose mutants is killed is not one, whatever its others do, which is what keeps an equivalent mutant on a tested line out of the list.
- **What the job says.** The summary lists each survivor with its mutants' labels, counts the lines killed, and counts the lines not run with the reason: the bound, candidates that fail as they stand, candidates priced past the trace's share. The heading says how many seconds the traces and the mutants took of the bound.
- **Report, not gate.** Exit **0** whenever lines were compared, **2** when nothing was (no merge base, no root). A survivor fails nothing. Three grounds, each a way a red would be wrong: an equivalent mutant survives on a tested line, so a survivor is not always a defect; the candidates are who names the file, so a kill by a file that does not is never run; and the bound truncates, so a gate's verdict would turn on the pull request's size. This repository gates what it measures reliably — `CLAUDE.md` §*The goal a design is chosen against*, and #931's decision that made `slow-file`, a per-file row that one refresh moved 0.67 to 1.72 times, a `report` row while `suite-seconds`, the sum, gates. `plan.md` §*Alternatives considered* T and U hold the gate's and the report's six-month failure modes side by side, and what would make the flip to a gate a one-line change.
- **A skipped case kills nothing.** A case pytest skipped, before or inside its body, fails under no mutant, so it is not a killer, and the check does not say so, name it or ask why. A sibling that fails makes the line killed; none makes it a survivor, which the author reads. This is the whole of what the check knows about skipping.
- **The bound.** `--bound` is five minutes for the whole check and `timeout-minutes: 15` the job's; the check ends on the bound and never on the timeout. How long it takes, `read` 2026-10-15 from `rounds/round-5.md` and the CI logs it names: on the runner one traced run of the case module took 12 s and each narrowed mutant run about 3 s (`proved in 35 s` for at most twelve mutants), so five minutes holds about 150 s of traces and the first mutants of some fifty lines. This branch changed 1,346 shipped lines (`executed`, `git diff --numstat 642441fc HEAD -- '*.py' ':!tests/*'`), so a pull request of its size has most of its lines counted `not run`, and the summary says so. The figures the job prints on #939's next run are `questions.md` Q8.

How it errs: under, because a kill by a test file that does not name the changed file is never run, and because a line reached only in a child process runs under its mutant only in the whole-candidates pass, which the bound reaches last; over, because an equivalent mutant on a line no case asserts is listed as a survivor, and a reader has to tell the two apart. Platform honesty: ubuntu alone, so a case another leg runs is not among the killers here, and a line only it kills is listed as a survivor. Nothing is named for it.

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
| S2 the lines compared | the pull request changes a `.py` outside `tests/`, a test file and a `.md` | the `.py`'s changed lines get mutants, as their bytes stand (CRLF kept); the test file's and the `.md`'s get none |
| S3 a killed line | a mutant of a changed line fails a case in a test file that names the module | the line counts killed; its other mutants are not run |
| S4 a survivor | every mutant of a changed line ran and none failed a case | the line is listed in the summary with its mutants' labels; exit 0. A line one of whose mutants was killed is not listed |
| S5 a skipped case kills nothing | the only candidate case whose call reaches the changed line skips in its body, before its assertion | the line is a survivor; no case is named, and nothing says the case skipped |
| S6 an untraced line | the changed line is run by no traced call — at import, in a fixture, or in a child process | its mutants run against the candidate files whole, after every traced line has its verdict, within the bound |
| S7 a removal is proven | each cut's table | every mutation red before and after; the remaining killer named |
| S8 the rows move with the cut | the cut's `.test_durations` in the tree | `suite-seconds` and the two `slow-file` rows lowered to 1.3 times their readings; `budget_check.py` exit 0; `test_the_durations_file_prices_the_suite` green |
| S9 the rules follow | a removed case an `Enforced by:` line names | the line names the case that holds the rule now; `budget_check.py`'s `enforced-unresolved` at 0 |
| S10 docs state the rule | the `CONTRIBUTING.md` paragraph | rewritten in place; `docs-history:*` at +0 |
| S11 nothing asks a person | the whole change | no `AskUserQuestion`, no prompt, no box |
| S12 every new unit declares | `case_check.py` and `hooks/launch.py` | a `Reads:` line each; the census passes |
| S13 the bound | more changed lines than five minutes hold | the summary counts them `not run within the bound`; nothing is proved past it, and the job ends on the bound, never on its timeout |
| S14 below the floor | any `bin/` command but `bin/test` run on a Python older than 3.12 | the launcher's one sentence, exit 2, the script never read |
| S15 at the floor | the same command on 3.12 or newer | the script runs with the arguments, `sys.path[0]`, `__file__` and exit code a direct run gives |
| S16 candidates that cannot run | a changed file whose candidate files fail as they stand, or which `.test_durations` prices past the trace's share | its lines count `not run` with the reason; the other changed files still get verdicts |
| S17 nothing compared | no merge base of `--baseline` and HEAD, or no root | exit 2, one line saying which |

## Data & interfaces

- `.github/scripts/case_check.py --baseline REF [--root DIR] [--runner CMD] [--bound MIN]` — stdout and `$GITHUB_STEP_SUMMARY`; names no path outside the root; exit 0/2 as above, and no exit 1. Inside it, the tracer's per-process JSON carries every id's lines and its call's seconds and nothing else; `traced_run` hands `check` five things, the exit, the seconds, the last line, the lines and the call seconds. The command line is unchanged by the reframe; the summary's sentences are `## The changed-lines check`'s.
- The `cases` job in `.github/workflows/test.yml` — pull requests only, `ubuntu-latest`, `contents: read`, `--bound 5`, a 15-minute timeout.
- `mutation-check --baseline-passed` — skips the run against the unmutated file, for a caller that already ran it; a call without it is unchanged.
- `hooks/launch.py <script> [arguments...]` — `FLOOR = (3, 12)`, the floor's one source; `.github/scripts/run_tests.py` reads it, and a case holds `ruff.toml` equal. Exit 2 below the floor or with no script named; otherwise the script's own.
- `seal/budgets.md` — three ceilings lowered; no row, table or measurer added.

## Removes

- The floor's eight copies: the guard (`FLOOR`, `FLOOR_TEXT`, `BELOW_FLOOR`, `below_floor`) in `skills/code-review/scripts/round_record.py`, `skills/settle/scripts/settle.py`, `skills/settle/scripts/fold_check.py`, `skills/verify/scripts/broad_gate.py`, `skills/verify/scripts/payload_meter.py`, `skills/verify/scripts/seal_stamp.py` and `.github/scripts/claude_block.py`, and `run_tests.py`'s own `FLOOR` number, which now reads the launcher's.
- The cases that pinned those copies: the 18 functions `tests/test_a_script_says_which_interpreter_it_needs.py` held, its census of constructs above the floor (`ABOVE_THE_FLOOR`, `CLASSIFIED`, `shipped_python`) with the `seal/follow-up.md` row it fed, and the raised-floor case in each of the payload-meter and `CLAUDE.md`-block modules. Five launcher cases replace them.
- 191 parametrized ids of `test_s2_a_commit_bash_makes_into_an_undeclared_repository_does_not_land`, which now runs `SAMPLE`, and phase 1's `test_every_sampled_name_is_a_corpus_row`, whose mutant S2's own row kills.
- The sealer file's six junit-twin layouts (`Qf-row`, `Qf-env`, `Qf-ini`, `R1-row`, `R1-ini`, `Q8`) and their 12 ids.
- The 227 ids those removals take out of `.test_durations`, and the 13 lines of `tests/undeclared_readers.txt` whose units were removed or now declare their `Reads:` line.
- **After round 6, from `.github/scripts/case_check.py`:** in `TRACER_SOURCE`, `_watch_expected`, `pytest_runtest_makereport`, `_skipped` and the JSON's `short`; at module level `PYTHON_LINE_END`, `PROVED`, `KILLS_NOTHING_NEW`, `NEVER_RAN`, `DRAW_CAP`, `RESTRUCTURE`, `REMOVED`, `test_functions`, `named_units`, `sole_killer`, `own_ids`, `drawn`, `top_units`, `tests_at` and `base_functions`; `check`'s per-function draw and proof, its never-ran naming and its removed-functions list; `shipped`'s `.md` branch; `traced_run`'s sixth element; the docstring's paragraphs on which cases are read, where a case's mutants come from and the pass rule. Nothing lands anywhere: the claim they carried leaves the item (`## Scope` item 2).
- **After round 6, from `tests/test_a_new_case_protects_what_its_file_did_not.py`, which the phase renames `tests/test_a_changed_line_is_mutated_on_the_pull_request.py`** because the old name states the dropped claim and nothing prices its ids (`executed`: no line of `.test_durations` names it): `test_the_sole_killer_is_one_function_or_none`, `test_a_case_draws_first_the_lines_fewest_of_its_siblings_run`, `test_a_case_draws_no_more_mutants_than_the_cap`, `test_a_function_named_in_a_case_is_followed_through_its_helpers` and `test_a_line_end_python_does_not_read_moves_no_function`, and twelve of `test_each_real_path_end_to_end`'s fifteen rows — S4 and S3 as framed before, every way a case skips, a file skipped at import, the three expected-failure rows, the sibling that skips, the tests-only draw, S5's prose pin, S2's changed function and the removed case — with the fixtures only they read (`ELSEWHERE`, `NEVER_STARTED`, `NEVER_RAN`, `AT_IMPORT`, `EXPECTED`, `UNITTEST_EXPECTED`, `CLASS_EXPECTED`, `PARTIAL`, `PIN`, `TWIN`, `S4`). Seventeen of the module's 27 ids; the three rows kept (CRLF, the survivor, the bound) are reshaped to the new summary, and `test_a_traced_run_that_times_out_hands_back_nothing_it_traced` to five elements.
- **After round 6, the sentences a person read:** the `cases` job's exit 1 and the verdicts `proved — the only killer in its file of …`, `kills nothing its file does not …`, `not proved: none of its ids ran its call to the end on this runner …` and `restructure: test the decision directly …`, from the step summary, the `CONTRIBUTING.md` paragraph, the `cases` comment in `test.yml` and the changelog's `Added` entry; the paragraph `**A case is owed by a mutant only it kills**`, rewritten in place under its new opening. The `Enforced by:` line under it keeps its target, `case_check.py::check`.

Each of these that the frame did not name is a divergence row in `overview.md`; the `Enforced by:` line that named the removed guard cases names the launcher and its cases now (`docs/round-record-spec.md` §*What it refuses before anything is written*). The `CONTRIBUTING.md` paragraph is rewritten, not removed.

## Open questions → questions.md

Framed 2026-10-13 by framer, before the build.
Reframed 2026-10-14 by framer, after round 0.
Reframed 2026-10-15 by framer, after round 3.
Reframed 2026-10-15 by framer, after round 6.

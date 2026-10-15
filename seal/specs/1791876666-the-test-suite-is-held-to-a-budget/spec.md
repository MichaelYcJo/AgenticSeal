# Feature Specification: the test suite is held to a budget

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | Nothing here asks a person. A new case is proven by a run CI makes, never by a sentence in a hand-back |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The regrowth check is a gate: a test seen red, the direction (it blocks more), a prompt budget of zero, platform honesty (it runs on ubuntu alone), a `Reads:` line per unit, `## Removes` below |
| `CONTRIBUTING.md` §*Running the checks*, the paragraph opening `**A case has a budget, and so does each leg.**` | Rewritten in place: what a case owes (a mutant only it kills in its file, which the `cases` job derives) and how a case is proven redundant, in a paragraph of its own before it, opening `**A case is owed by a mutant only it kills**`; then the budget each case and leg keeps. Nothing is appended |
| `skills/implement/SKILL.md` §*2. Implement test-first, and let each rule name its test* | The convention this work extends to the case itself: a rule's `Enforced by:` line names the test that holds it, and the test is proved by a mutant it alone kills |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | The changelog goes to the work item's fragment; a removed or renamed case an `Enforced by:` line names moves that line to the case that holds the rule now |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below; a removal the frame did not name is a divergence in `overview.md` |
| `docs/commit-review-gate-spec.md` §*Registration* | A hook that fails is skipped and said, and the call goes ahead. That is why the launcher stands in front of the `bin/` wrappers and not in front of `hooks/hooks.json`, where exit 2 blocks the call |
| `skills/agent-contract/SKILL.md` §15 | Today's rule for a new case, which the regrowth check makes a run CI performs rather than a thing a hand-back says |
| #930's `seal/specs/1791876665-…/spec.md` §*The budgets* | The ratchet the rows this item lowers stand under: `measured ≤ ceiling`, a `one-sided` row's ceiling 1.3 times its reading, rounded up; a lowering needs no `Budget raised:` line |
| #931's `seal/specs/1791876667-…/spec.md` §*Scope* item 3 | A pull request that removes a twentieth of the suite's seconds brings the `.test_durations` its cut leaves; `suite-seconds` falls in the same pull request |
| `skills/implement/SKILL.md` §*3. The SDD file set* | A check's verdict and a sentence a contributor acts on change, which is the top rung |

## Scope

**The problem.** The suite grew by appending: every fix planted cases and nothing took any out. Whether 13,714 cases guard 13,714 things is unknown, and nothing stopped the next pull request from adding 44 more that guard nothing new. Time was the first frame's measure; it is a consequence here.

**In.** What this item ships. The owner closed it at phase 2 on 2026-10-15, and the rest of the plan went to #942.

1. **One module compacted, proven by mutation.** `tests/test_the_commit_gate_decides_at_the_commit.py` replays `SAMPLE`, one or more representatives of each corpus subgroup, where it replayed the whole corpus (phase 1). The sealer file's six corpus layouts that differ from a kept twin only by a junit option leave with their 12 ids (f13b0dfa). Each removal meets `## The removal criterion`.
2. **Change how a case is added**, so the suite does not regrow: a new or changed case must be its file's only killer of a mutant the tree yields, and CI derives and runs that mutant (`## What a case owes`, `## The regrowth check`). This lands in 0.22.0. After round 3 the reframe fixed one thing inside it: what "this case did not run its body here" means is one rule read from pytest's own call report, and the traced lines no longer carry that decision (`## The regrowth check` §*Platform honesty*).
3. **The rows the cuts moved are lowered** in #930's `seal/budgets.md` (`## Rows for seal/budgets.md`).
4. **One launcher holds the Python floor.** `hooks/launch.py` holds `FLOOR`, and every `bin/` wrapper but `bin/test`, and its `.cmd` twin, runs its script through it; `bin/test`'s runner starts on any `python3` because it builds the virtualenv at the floor (`hooks/launch.py`'s docstring). Below the floor it refuses with one sentence and exits 2 before the script is read; at or above it the script runs as if run directly. The floor's eight copies and the cases that pinned them leave (`## Removes`).

**Out, and whose.**

- **A case whose assertion reads this tree's prose** — `agents/`, `skills/*/SKILL.md`, `orchestration.md`, `docs/`, `README*`, `CONTRIBUTING.md`, `CLAUDE.md`, `templates/` — is #923's and moves with that text. By function body or a constant or helper the function names (`executed` at fcd735bc, now f13b0dfa, `plan.md` §*Technical context*): 1,201 functions, 1,586 collected cases, in 135 files; the measure errs over, counting a case that writes `docs/` into a fixture tree. A cut that opens a file lists which of its cases it left to #923.
- **Which legs run on a pull request** — #943 (item B); every leg on every pull request until it is framed.
- **The rest of the cleanup — #942.** The three enumeration files that hold 31 % of the cases, the 249 byte-identical helper twins, the sealer file's inventory of its `run_gate` call sites and its mutation battery, and every test file this item did not open, each under `## The removal criterion`. With them go the rows the frame proposed for `seal/budgets.md` — `test-cases`, `test-lines`, `test-cases:<file>` and `test-lines:<file>`, their measurers in `budget_check.py` and a per-file table for them — whose ceilings are #942's to set from its own tables.
- **`unguarded-files` and `tests/unguarded-files.txt`** — not built and not moved. The list was to hold the files whose cases still owed a written line, and no case owes one (the owner's decisions of 2026-10-14).
- **`hooks/hooks.json` and the git hook stubs** stay outside the launcher. A hook below the floor is protected by `dispatch.py`'s own isolation, as before (`phases/phase-2.md` gives the grounds).
- **`.test_durations`' cadence** (#931) and **the budget mechanism** (#930): read, not changed. This item adds no row and no measurer.
- **A suite-wide mutation census as a CI job.** The regrowth check derives a new case's mutants; nothing re-runs every case's. #942's tables are where the existing cases meet theirs.

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

## What a case owes

Nobody writes down what a case guards. A test function is owed by a mutant that it alone, in its file, kills: under that mutant its own ids fail, and no other case of its file that ran the mutated line fails. The ids of one parametrized function are one case, so a kill its rows share is the function's own. The mutant is derived from the tree, never named by hand (`## The regrowth check`). A case that pins prose is owed by its sentence removed. These are the owner's decisions of 2026-10-14, recorded as a divergence in `overview.md`.

## The removal criterion

A case is removed only when a mutation table shows it guards nothing alone: a battery of mutations of the unit under test, each killed (`mutation-check` exit 0) by the file as it stands, is still killed by the file without the case. The battery is drawn from what the file's docstrings say its cases guard, and for an enumeration it holds one mutation per kind the enumeration names, so a row that a kind's mutation needs stays. A candidate whose guarded sentence no mutation negates gets its mutation added before anything is removed; a sentence the battery shows unguarded gets one case, which the suite may grow by. A case whose bare run shows it asserts nothing is removed on that showing. A byte-identical helper twin is removed on the hash alone. Judgment removes nothing. The table — mutation · killed before · killed after · the sentence's one remaining killer — is in the record of the phase that made the cut: phase 1's in `phases/phase-1.md`, the sealer cut's in `phases/phase-2.md`.

## The regrowth check

`.github/scripts/case_check.py`, the `cases` job of `test.yml`, on ubuntu, on pull requests. It reads every test function new at HEAD against the merge base with `--baseline`, or whose text differs from the base's, docstring included.

- **Where the mutants come from.** Each file holding such a function runs once as it stands, under a tracer that records which lines each case runs, and must pass. For each function at most twelve mutants are drawn, best first: the lines it runs, those fewest of its siblings run first; then the units of its own file it names, followed through the helpers they name; then the lines the pull request changed in shipped code, a `.py` outside `tests/` or a `.md` outside `seal/`. A line a sibling ran and it did not is never drawn, a test function's own lines are never mutated, and a changed `.md` line is mutated by removing it.
- **The pass rule.** Under each mutant, through `mutation-check --baseline-passed`, the function's own ids run first, and where they fail, the other cases that ran the line (every other case of the file where no call ran it). The function is proved at its first mutant that fails it alone. A function whose draw runs out first is named, `kills nothing its file does not`.
- **What nothing kills is a report.** The changed shipped lines' mutants that no case killed are listed, and so are the test functions the pull request removed. Neither fails the job: a gate there would be red for a mutant a file outside the run kills.
- **The bound.** `--bound` is five minutes for the whole check, each file taking an equal share of what is left. A file whose proof would pass it is named, `restructure: test the decision directly`, so the job ends on the bound and never on its timeout.
- **Exit 0** every new or changed function proved, **1** one named, **2** nothing compared. Gate, not report: a report read by nobody is the mechanism #908's table already had.

How it errs: under, because a line reached only through a subprocess or a fixture's setup is not traced, so such a case gets its mutants from the names it uses and from the diff alone; over, because a line one case runs alone may be setup only it needs. Its scope is the function's file: a case in another file that kills the same mutant is not seen.

**Platform honesty: what "ran its body here" means is decided once, from pytest's own report, never from the traced lines.** The check runs on ubuntu, and a new or changed case none of whose ids ran its body there is named `not proved: none of its ids ran its call to the end on this runner`, no mutant is run against it, and the job fails. That naming is a finding and not a report line, which the tree answers in `questions.md` Q7. The rule has two halves, and each half has one reader:

- **An id ran its body** when pytest wrote a call-phase report for it whose outcome is `passed` or `failed`, or `skipped` because the body itself raised and an expected-failure mark excused the raise. **An id stopped short** when pytest wrote no call-phase report for it — it was never collected, deselected, or skipped before its call by a mark, a fixture or `xfail(run=False)` — or wrote one whose outcome is `skipped` because pytest's own stop ended the call: `pytest.skip()`, `pytest.importorskip`, `skipTest`, a raised `unittest.SkipTest` or `pytest.xfail()` in the body, whatever spelling. The one translation is pytest's: its unittest plugin raises the xfail stop itself on behalf of an `@unittest.expectedFailure` whose body raised, and `__unittest_expecting_failure__` on the method or on the `TestCase` instance, and so on its class, says so, as the stdlib reads both, so that case ran its body. The same mark on a function that is not a `TestCase` method excuses nothing, because pytest's unittest plugin never ran it. The reader is the tracer's `pytest_runtest_makereport` wrapper, which sees the report and the call's exception after every other implementation has had them; the stopped ids are written apart from the lines. No list of spellings is a source of this rule: an enumeration is what each of rounds 1–3 patched one entry of, and the next spelling is not in any list written today.
- **Every traced line is kept for every id**, stopped or not. A case that asserted and then skipped ran its first lines, a mutant of one of them fails it before it stops, and it is a killer of that mutant — so it is drawn from and run under mutants like any other case. Only the never-ran naming of a new or changed case reads the stopped ids; the draw and the choice of which siblings run under a mutant read the lines.

An expected failure that ran its body is proved like any other case: a mutant fails it by making a strict one pass, by raising other than the exception its mark names, or by making a `unittest` one pass unexpectedly.

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
| S2 a changed function is read as new | a pull request edits an existing test function, its docstring alone included | `case_check.py` reads it and proves it as it proves a new one |
| S3 a case its file already covers | every mutant drawn for a new case is killed by a sibling too | exit 1 naming the function, `kills nothing its file does not`; the job is red |
| S4 a new case proven | a mutant of changed code fails the new case alone | exit 0; the summary names the function and the line of its mutant |
| S5 a case that pins prose | the pull request changes a `.md` line a new case reads | the line removed is a mutant, and the case proves by it |
| S6 what nothing kills is reported | a mutant of changed shipped code no case kills; a test function the pull request removed | both listed in the summary; the exit is unchanged |
| S7 a removal is proven | each cut's table | every mutation red before and after; the remaining killer named |
| S8 the rows move with the cut | the cut's `.test_durations` in the tree | `suite-seconds` and the two `slow-file` rows lowered to 1.3 times their readings; `budget_check.py` exit 0; `test_the_durations_file_prices_the_suite` green |
| S9 the rules follow | a removed case an `Enforced by:` line names | the line names the case that holds the rule now; `budget_check.py`'s `enforced-unresolved` at 0 |
| S10 docs state the rule | the `CONTRIBUTING.md` paragraph | rewritten in place; `docs-history:*` at +0 |
| S11 nothing asks a person | the whole change | no `AskUserQuestion`, no prompt, no box |
| S12 every new unit declares | `case_check.py` and `hooks/launch.py` | a `Reads:` line each; the census passes |
| S13 a file past the bound | a file whose proof would take longer than its share of five minutes | named, `restructure: test the decision directly`; the job ends on the bound |
| S14 below the floor | any `bin/` command but `bin/test` run on a Python older than 3.12 | the launcher's one sentence, exit 2, the script never read |
| S15 at the floor | the same command on 3.12 or newer | the script runs with the arguments, `sys.path[0]`, `__file__` and exit code a direct run gives |
| S16 a sibling that asserts and then skips still kills | the base holds a case that asserts on the unit and then `pytest.skip()`s; the pull request adds a case the same mutant fails | exit 1, the new case named `kills nothing its file does not`; it was `proved` at e0e0d485, round 3's 🟡 1 |
| S17 a call pytest stopped is named for never having run; an excused raise is a run | a new case calls `pytest.xfail()` before its assertion; another is a `@unittest.expectedFailure` whose body raises | the first is named `not proved: none of its ids ran its call to the end on this runner`, never `kills nothing`; the second is run under its mutants and never named `not proved`; round 3's 🟡 2 |

## Data & interfaces

- `.github/scripts/case_check.py --baseline REF [--root DIR] [--runner CMD] [--bound MIN]` — stdout and `$GITHUB_STEP_SUMMARY`; names no path outside the root; exit 0/1/2 as above. Inside it, the tracer's per-process JSON carries the ids that stopped short beside every id's lines, and `traced_run` hands both to `check`; the command line and its verdict sentences are unchanged by the reframe.
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

Each of these that the frame did not name is a divergence row in `overview.md`; the `Enforced by:` line that named the removed guard cases names the launcher and its cases now (`docs/round-record-spec.md` §*What it refuses before anything is written*). The `CONTRIBUTING.md` paragraph is rewritten, not removed.

## Open questions → questions.md

Framed 2026-10-13 by framer, before the build.
Reframed 2026-10-14 by framer, after round 0.
Reframed 2026-10-15 by framer, after round 3.

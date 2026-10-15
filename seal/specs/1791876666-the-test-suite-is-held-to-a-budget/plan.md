# Implementation Plan: the test suite is held to a budget

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-14 by the repository owner, when `smith` was spawned.
Approved 2026-10-14 by the repository owner, when `smith` was spawned for the reframed plan.

## Summary

Two phases. Phase 1 cut one module by a mutation table: the commit-gate test file replays a sampled set of each corpus subgroup instead of the whole corpus. Phase 2 built the regrowth check, which 0.22.0 cannot ship without. Every new or changed test function must be its file's only killer of a mutant the check derives from the tree, and a CI job runs that proof, so a case is proven by a run and not by a sentence in a hand-back. Phase 2 also built one launcher that holds the Python floor for every `bin/` command but `bin/test`, and recorded the sealer file's junit-twin cut with its table. The rows the cuts moved are lowered in `seal/budgets.md`. The rest of the cleanup — the enumeration files, the helper twins, the sealer file's inventory and every file not opened here — is #942's, under the same rule (alternative H).

## Technical context

Read at fcd735bc, before the rebase onto #944 (now f13b0dfa), unless marked `executed`.

- **Measurements** (`executed` 2026-10-14, macOS arm64; each number is in `spec.md` §*What the suite is*). Cases: `bin/test --collect-only -q -p no:xdist | grep '::'` (13,714; 1.8 s wall). Lines: `wc -l tests/*.py`. Shipped lines: `find . -name '*.py'` outside `tests/`, `.venv/`, `.git/`. Docstrings, prose readers, helper twins and the unit census: `ast` over `tests/test_*.py` against `git show HEAD:<module>` for the 65 shipped modules (`hooks/*.py`, `skills/*/scripts/*.py`, `.github/scripts/*.py`); a twin is the same name and the same body after the docstring and whitespace. Prices: the committed `.test_durations`. CI minutes: `gh api repos/<r>/actions/runs/<id>/jobs`, the `pytest` jobs' `started_at`–`completed_at` summed per leg (NAME NOT IN TREE: two fields of GitHub's jobs API). Mutations: `bin/mutation-check <file> --replace OLD NEW --tests "bin/test <tests> -q -rf -p no:xdist"`, killers counted as `FAILED` lines.
- `skills/verify/scripts/mutation_check.py` — one mutation, one command, exit 0 red · 1 survived · 2 measured nothing; refuses a replacement that does not land exactly once; `--timeout`; restores from the bytes it read. The regrowth check calls it once per mutant with `--baseline-passed`, which skips the run against the unmutated file because the check's traced run already passed it.
- `.github/scripts/budget_check.py` and `seal/budgets.md` — the families, `## Slow test files`, `## Price level`, `--baseline`, exit 0/1/2. A `one-sided` row's ceiling is 1.3 times its reading, rounded up, and a lowering needs no body line. This item adds no row and no measurer; it lowers `suite-seconds` and the two `slow-file` rows its cuts moved.
- `.github/workflows/test.yml` — #931's `durations` job (`needs: pytest`, ubuntu) is the shape for the `cases` job, except that it needs no artifact and runs the cases itself; `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#staleness` fails when more than a twentieth of the file's seconds are dead.
- `tests/test_the_commit_gate_decides_at_the_commit.py#SAMPLE` and `#test_every_corpus_family_has_a_sampled_row` — phase 1's pattern for an enumeration: a representative per subgroup, pinned against the corpus.
- `hooks/launch.py` — `FLOOR`, the refusal sentence, and the script run with `runpy` as `__main__`. `.github/scripts/run_tests.py` reads its `FLOOR`; `hooks/hooks.json` does not run through it, because exit 2 from a hook blocks the call (`docs/commit-review-gate-spec.md` §*Registration*).
- `Enforced by:` lines naming tests (#944): a rule names the case that holds it, and `budget_check.py`'s `enforced-unresolved` row, a gate at 0, names a target that is gone or renamed. A removed or renamed case an `Enforced by:` line names takes that line to the case that holds the rule now, in the same pull request.

**What breaks in 6 months with the chosen approach.** First, the draw errs over: a line one case runs alone may be setup only it needs, so a case can prove itself by a mutant of its own fixture while the behaviour it was meant to guard is guarded elsewhere; the warden reads the summary's proving line, and nothing else does. Second, the draw errs under: a case whose decision runs in a child process is not traced, gets its mutants from the names it uses and the diff alone, and may be named although it guards something; its author restructures it to test the decision directly, which is the bound's own advice. Third, the bound: a case added to a slow file meets `restructure` before it meets a mutant, and the author moves the case to a new file to dodge it. The check's scope is one file, so the move passes; #942's rows are what would hold it.

## Alternatives considered

| Approach | Failure scenario (six months on) | Verdict |
|---|---|---|
| A. Derived: each new or changed case must be its file's only killer of a mutant the check draws from the lines it runs, the units it names and the changed shipped lines; one run per mutant; a five-minute bound | above | **chosen**, the owner's decisions of 2026-10-14 |
| B. A `Guards:` line naming a unit, read by a census and run by nothing | every line names the file's unit under test; two cases guard one sentence and both are legal; the census passes on boilerplate | rejected |
| C. `Mutation:` lines in the pull request body, as `Budget raised:` is | the proof lives in a body nobody re-runs; the case stays unlabelled in the tree, and #942's tables start from nothing | rejected |
| D. Per-file ceilings only (`test-cases:<file>`, `test-lines:<file>`) | a feature's cases go in a new file each time; the files multiply under the threshold | rejected alone; the suite and per-file rows are #942's |
| E. A suite-wide mutation census as a CI job | 1,529 units, hours per run, and a generated mutation is not a sentence anybody named; the job is made `report` and read by nobody | rejected; the existing cases meet their mutations in #942's tables |
| F. A `test-ratio` row, test lines over shipped lines | shipped code that grows lowers it; a cleanup of code raises it | rejected |
| G. `test-cases` at slack 0 with no raise | a sentence nobody guards cannot get its case without a `Budget raised:` line; the line is boilerplate within one release | rejected; the row's slack is #942's to set |
| H. Split: this item ships the mechanism and the first proved cuts; #942 takes the rest of the cleanup under the same rule | not split, 185 files at a session each never ships and 0.22.0 waits on it; split, #942's pull requests are each held by the regrowth check this item adds | **chosen**, and the split fell after phase 2: the owner closed this item there on 2026-10-15, because #923 waits on this item's merge, and phases 3–6 went to #942 |
| I. Delete by judgment | a guard goes with the case; #841's 165 s case held a cited guard | rejected |
| J. Heavy files on a nightly or `main`-only job | a red that reaches no pull request is ignored | rejected |
| K. Which legs run (D1–D4 of the first frame) | #943's (item B); D4 until then | not decided here |
| L. A `Kills:` line per test function, run by CI with and without the function, and a frozen list of the files that still owe one | nobody annotates a case, and a line chosen to be killable by its own fixture proves nothing; the list sits at its ceiling | rejected by the owner, 2026-10-14; built in phase 2 and removed there |

**CI cost if this repository goes private** (`executed` for the medians; prices `read` from #929, mid-2026, $0.008 · $0.016 · $0.08 per Linux · Windows · macOS minute, date unverified). Per pull request at the medians: 9.9 + 2 × 42.4 + 10 × 21.6 = 310.7 Linux-equivalent minutes ≈ US$2.49, 70 % of it macOS. The `cases` job adds ubuntu minutes only, its proof bounded at five minutes; CI run 38518943105 read 22 functions in 297 s, beside a Windows leg of 42 minutes, so no wait is added. The cuts move `ci-minutes:*` by the removed seconds' share, and #943 is where the macOS figure is decided.

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `test_the_commit_gate_decides_at_the_commit.py`: `SAMPLE` beside `CORPUS`, S2 over the sample, a vacuous row failing rather than skipping, three pins, the m1–m5 table, 191 ids pruned; 249bd6d2 fixed the three rows CI found | `phases/phase-1.md`: 367 → 179 cases, 87.6 → 29.2 s wall, 1,137 → 368 Windows seconds, every mutation red before and after with the same other-case killers | 610a9273 |
| 2 | **The regrowth check, derived (the owner's decisions of 2026-10-14).** `.github/scripts/case_check.py`: new and changed test functions against `--baseline`; mutants drawn from the lines each runs and its siblings do not, the units of its file it names, and the shipped lines the range changed, a traced run of the file first; one run per mutant, of the cases that ran its line, through `mutation-check --baseline-passed`, its killers read; an equal share of the bound per file; each such function its file's only killer of one mutant, or named; the mutants of changed code nothing kills listed as a report; a five-minute bound with `restructure: test the decision directly` past it; the summary, exit 0/1/2. The `cases` job in `test.yml` on ubuntu; the cases in `tests/test_a_new_case_protects_what_its_file_did_not.py`; the `CONTRIBUTING.md` paragraph rewritten in place. Nothing is written by hand: no annotation, no list of files. **One launcher**, `hooks/launch.py`, holding the Python floor for every `bin/` wrapper and `.cmd` twin but `bin/test`'s, whose runner builds the virtualenv at the floor; the floor's eight copies and their guard cases removed. The sealer file's junit-twin cut (f13b0dfa) recorded with its table | the decisions tested directly, and each path once end to end on a fixture repository: a case that alone kills a mutant of changed code → 0, a case its file already covers → 1, a survivor of changed code → listed and 0, a tests-only case → proved from the lines it runs, a prose pin → proved by its sentence removed, a changed function → read, a removed case → listed, a file past the bound → restructure; the job on PR #939; the five launcher cases, each seen red with `mutation-check` | 692cef31 |

This table is also where the work records how far it got. **Status is empty, or the commit that closed the phase.** Re-read the column after any rebase.

### Test rows — the mutation each case kills

| Case | Guards | Mutation it kills |
|---|---|---|
| T1 `test_each_real_path_end_to_end`, row *S4 a new case alone kills a mutant of changed code* | S4 | a proof read off a run whose killers are not one function's alone |
| T2 `test_each_real_path_end_to_end`, row *S3 a case its file already covers is named* | S3 | a case that kills only what a sibling kills read as proved |
| T3 `test_each_real_path_end_to_end`, row *a mutant of changed code nothing kills is reported* | S6 | a survivor of changed code left out of the summary, or made a failure |
| T4 `test_each_real_path_end_to_end`, row *a tests-only change draws from the lines its case runs* | S4 | the traced lines a case runs alone not drawn first |
| T5 `test_each_real_path_end_to_end`, row *S2 a changed function is read as new* | S2 | only names absent at the base read |
| T6 `test_each_real_path_end_to_end`, row *S5 a prose pin is proved by its sentence removed* | S5 | a changed `.md` line not mutated |
| T7 `test_each_real_path_end_to_end`, row *a file whose proof would pass the bound is named to restructure* | S13 | the bound read after the mutants run, or never |

Each is seen red by its mutation before it is committed, and the `cases` job proves each on PR #939 by a mutant it derives.

## Operational impact

- One new script, one new CI job (ubuntu, `contents: read`), one launcher every `bin/` command but `bin/test` runs through, and three ceilings lowered in `seal/budgets.md`. No new dependency, no new row, no new measurer.
- Every test function added or changed from phase 2 on must be its file's only killer of a derived mutant, or the `cases` job is red and names it.
- A `bin/` command other than `bin/test` run on a Python older than 3.12 refuses with one sentence and exit 2 before its script is read. `bin/test` builds its virtualenv at the floor from an older `python3`, as before. The plugin's hooks do not go through the launcher and behave as before.
- `.test_durations` loses the 227 ids the cuts removed and no price is changed; a later refresh replaces it with #931's union, never by hand.
- An `Enforced by:` line naming a removed or renamed case moves with it in the same pull request; `enforced-unresolved` holds that.
- #943 (item B) and #942 (the rest of the cleanup) are issues the orchestrating session holds; nothing here posts.

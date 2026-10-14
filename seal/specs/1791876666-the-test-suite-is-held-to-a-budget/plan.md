# Implementation Plan: the test suite is held to a budget

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-14 by the repository owner, when `smith` was spawned.
Approved 2026-10-14 by the repository owner, when `smith` was spawned for the reframed plan.

## Summary

The regrowth check first, because it is what 0.22.0 cannot ship without: every new or changed test function carries a `Kills:` line, and a CI job runs it — red with the function, not red without it — so a case is proven by a run and not by a sentence in a hand-back (phase 2). Then the cleanup where the cases are: the three enumeration files that hold 31 % of them, sampled by kind on phase 1's pattern (phase 3); the 249 byte-identical helper twins, moved to `conftest.py` on the hash (phase 4); the sealer file, which is 10,142 lines for 457 cases (phase 5). Every removal is proven by a mutation table, every kept case leaves with its `Kills:` line, every cut pull request brings the union `.test_durations` from its own run and lowers the rows (phase 6 closes the records). The long tail — every file these phases do not open — is item C, under the same rule and held by the same rows.

## Technical context

Read at fcd735bc unless marked `executed`.

- **Measurements** (`executed` 2026-10-14, macOS arm64; each number is in `spec.md` §*What the suite is*). Cases: `bin/test --collect-only -q -p no:xdist | grep '::'` (13,714; 1.8 s wall). Lines: `wc -l tests/*.py`. Shipped lines: `find . -name '*.py'` outside `tests/`, `.venv/`, `.git/`. Docstrings, prose readers, helper twins and the unit census: `ast` over `tests/test_*.py` against `git show HEAD:<module>` for the 65 shipped modules (`hooks/*.py`, `skills/*/scripts/*.py`, `.github/scripts/*.py`); a twin is the same name and the same body after the docstring and whitespace. Prices: the committed `.test_durations`. CI minutes: `gh api repos/<r>/actions/runs/<id>/jobs`, the `pytest` jobs' `started_at`–`completed_at` summed per leg (NAME NOT IN TREE: two fields of GitHub's jobs API). Mutations: `bin/mutation-check <file> --replace OLD NEW --tests "bin/test <tests> -q -rf -p no:xdist"`, killers counted as `FAILED` lines.
- `skills/verify/scripts/mutation_check.py` — one mutation, one command, exit 0 red · 1 survived · 2 measured nothing; refuses a replacement that does not land exactly once; `--timeout`; restores from the bytes it read. The regrowth check calls it twice per function, the second time with `--deselect <id>` in the tests command.
- `tests/test_a_reader_declares_its_input_class.py` + `tests/undeclared_readers.txt` — the frozen list that only shrinks, read by a census over `ast`; `tests/unguarded-files.txt` takes the shape one level up, per file.
- `.github/scripts/budget_check.py` — the families, the per-file tables (`## Slow test files`, the family row giving unit, slack and kind, an unlisted file over the threshold failing), `--baseline`, the body line, exit 0/1/2. The five rows add measurers and one two-column per-file table; the ratchet is untouched. #930 is at 661dc60b with phases 1–3 closed; where its file is not in the tree when a phase runs, the numbers go to the phase record and the later pull request lowers the rows.
- `.github/workflows/test.yml` — #931's `durations` job (`needs: pytest`, ubuntu, `actions/download-artifact`) is the shape for the `cases` job, except that it needs no artifact and runs `bin/test` itself; `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#staleness` fails when more than a twentieth of the file's seconds are dead, and its message names `gh run download <id> -n test-durations`, which is how each cut phase refreshes the file.
- `tests/test_the_commit_gate_decides_at_the_commit.py#SAMPLE`, `#test_every_corpus_family_has_a_sampled_row`, `#test_every_sampled_name_is_a_corpus_row` — phase 1's pattern for an enumeration: a representative per subgroup, pinned against the corpus.
- The enumeration files: `tests/test_a_signer_declares_its_pact.py` — `BLIND_SIDE` (118 spellings) × `gap` (2) at line 1019 and `OTHER_ITEMS` × `place` at 676, 2,652 cases in 1,564 lines, 36.6 s; `tests/test_one_table_walker_reads_what_gfm_renders.py` — `KINDS` × positions × five indents × three headers, 904 cases, 23.8 s, whose property (cells equal cmark-gfm's or the walker refuses) kills none of four `table_end` mutations; `tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py` — 672 cases, 164.6 s. The battery for each is one mutation per kind its docstring names.
- `tests/test_the_seal_is_taken_once_by_the_sealer.py` — `#run_gate` (98 call sites), `#a_sealed_run` (six cases sharing one run, the precedent), `REGRESSED` (fcd735bc took six junit twins out, 12 ids, each shown to kill what its twin kills); 1,126 s, the file's 160 cases at ≥ 5 s hold 1,045 s (`read`, the first frame at c22f7472).
- `Enforced by:` lines naming tests (#944): a rule names the case that holds it, and `budget_check.py`'s `enforced-unresolved` row, a gate at 0, names a target that is gone or renamed. A removed or renamed case an `Enforced by:` line names takes that line to the case that holds the rule now, in the same pull request.

**What breaks in 6 months with the chosen approach.** The `Kills:` line is chosen to be killable by the new function alone — a string its own fixture asserts — and the check is green while the behaviour the case was meant to guard is guarded elsewhere; the warden reads the diff's `Kills:` lines as it reads `Reads:` lines, and nothing else does. Second: the `cases` job's runtime is 1 + 2N file runs, so a pull request adding ten cases to the sealer file waits on ten runs of a two-minute file, and the author moves the cases to a new file to dodge it — which `test-cases` and the frozen list then hold. Third: `unguarded-files.txt` sits at its ceiling the way the docs sat at 1,000 lines, trimmed by one file per release; what moves it is item C's phases, and the `unguarded-files` row prints how many are left on every run.

## Alternatives considered

| Approach | Failure scenario (six months on) | Verdict |
|---|---|---|
| A. A `Kills:` line per test function, run by CI with and without the function; a frozen file list that only shrinks; five ratchet rows; removal by mutation table | above | **chosen** |
| B. A `Guards:` line naming a unit, read by a census and run by nothing | every line names the file's unit under test; two cases guard one sentence and both are legal; the census passes on boilerplate | rejected |
| C. `Mutation:` lines in the pull request body, as `Budget raised:` is | the proof lives in a body nobody re-runs; the case stays unlabelled in the tree, and item C's tables start from nothing | rejected; the line goes in the docstring, where `mutation-check` can read it again |
| D. Per-file ceilings only (`test-cases:<file>`, `test-lines:<file>`) | a feature's cases go in a new file each time; the files multiply under the threshold | rejected alone; kept beside the suite rows |
| E. A suite-wide mutation census as a CI job | 1,529 units, hours per run, and a generated mutation is not a sentence anybody named; the job is made `report` and read by nobody | rejected; a mutation here is hand-named, and the census is item C's tables |
| F. A `test-ratio` row, test lines over shipped lines | shipped code that grows lowers it; a cleanup of code raises it | rejected |
| G. `test-cases` at slack 0 with no raise | a sentence nobody guards cannot get its case without a `Budget raised:` line; the line is boilerplate within one release | rejected; 2 % slack, the raise with its reason |
| H. Split: this item ships the mechanism and four proved cuts; item C takes the long tail under the same rule | not split, 185 files at a session each never ships and 0.22.0 waits on it; split, item C's pull requests are each held by the rows this item adds, so the tail cannot regrow while it is cut | **chosen** |
| I. Delete by judgment | a guard goes with the case; #841's 165 s case held a cited guard | rejected |
| J. Heavy files on a nightly or `main`-only job | a red that reaches no pull request is ignored | rejected |
| K. Which legs run (D1–D4 of the first frame) | item B's; D4 until then | not decided here |

**CI cost if this repository goes private** (`executed` for the medians; prices `read` from #929, mid-2026, $0.008 · $0.016 · $0.08 per Linux · Windows · macOS minute, date unverified). Per pull request at the medians: 9.9 + 2 × 42.4 + 10 × 21.6 = 310.7 Linux-equivalent minutes ≈ US$2.49, 70 % of it macOS. The `cases` job adds ubuntu minutes only: 1 + 2N runs of each touched file; at 44 new cases in ten-second files about 15 minutes ≈ $0.12, beside a Windows leg of 42 minutes, so no wait is added; a case in the sealer file costs about four minutes of ubuntu each. The cuts move `ci-minutes:*` by the removed seconds' share and item B is where the macOS figure is decided.

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `test_the_commit_gate_decides_at_the_commit.py`: `SAMPLE` beside `CORPUS`, S2 over the sample, a vacuous row failing rather than skipping, three pins, the m1–m5 table, 191 ids pruned; badc0bd4 fixed the three rows CI found | `phases/phase-1.md`: 367 → 179 cases, 87.6 → 29.2 s wall, 1,137 → 368 Windows seconds, every mutation red before and after with the same other-case killers | cf77665c |
| 2 | **The regrowth check, derived (the owner's decisions of 2026-10-14).** `.github/scripts/case_check.py`: new and changed test functions against `--baseline`; mutants drawn from the lines each runs and its siblings do not, the units of its file it names, and the shipped lines the range changed, a traced run of the file first; one run per mutant, of the cases that ran its line, through `mutation-check --baseline-passed`, its killers read; an equal share of the bound per file; each such function its file's only killer of one mutant, or named; the mutants of changed code nothing kills listed as a report; a five-minute bound with `restructure: test the decision directly` past it; the summary, exit 0/1/2. The `cases` job in `test.yml` on ubuntu; the cases in `tests/test_a_new_case_protects_what_its_file_did_not.py`; the `CONTRIBUTING.md` paragraph rewritten in place. Nothing is written by hand: no `Kills:` line, no list of files. The five measurers wait for #930 | the decisions tested directly, and each path once end to end on a fixture repository: a case that alone kills a mutant of changed code → 0, a case its file already covers → 1, a survivor of changed code → listed and 0, a tests-only case → proved from the lines it runs, a prose pin → proved by its sentence removed, a changed function → read, a removed case → listed, a file past the bound → restructure; the job on PR #939 | 652bf297 |
| 3 | **The enumerations.** `test_a_signer_declares_its_pact.py` first (S1's second module: cases, lines, seconds, the table before and after), then the walker and wrapper files: a battery of one mutation per kind each file's docstring names, a sampled set per kind with phase 1's pins, a survivor's sentence given one case, `Kills:` lines on every kept function, the three files out of `unguarded-files.txt`; the union downloaded from the phase's run; rows lowered | each file ≤ 400 cases, or the table's count with the reason; every battery mutation red before and after; `test_the_durations_file_prices_the_suite` green; `budget_check.py` exit 0; the table in `phases/phase-3.md` | |
| 4 | **The helpers.** The 249 byte-identical twins replaced by one definition each in `tests/conftest.py`, and the `git init` bodies that are twins by one fixture; the hash table (name · files · sha) in `phases/phase-4.md`; `test-lines` lowered | the modules touched green; `test-lines` ≤ 158,800; no `Kills:` line changes, because no case changed | |
| 5 | **The sealer file.** fcd735bc's junit twins recorded here with their table; the inventory of the 98 `run_gate` call sites by (template state, arguments, environment); one memoized run per signature for cases that only read, on `#a_sealed_run`; the battery over `broad_gate.py`'s words, exit codes and the stamp; twins out on it; `Kills:` lines; the file out of the list; the union downloaded; rows lowered | ≤ 700 Windows seconds and ≤ 7,000 lines, or the inventory's figures with the reason; every battery mutation red before and after; `phases/phase-5.md` | |
| 6 | **The records.** Every `Enforced by:` line naming a case that left or moved pointed at the case that holds the rule now; the changelog fragment; the rows at their final ceilings; the count of files left on `unguarded-files.txt` and the list of what each phase left to #923, for item C's frame | `budget_check.py` exit 0, `enforced-unresolved` at 0; `unverified-check --baseline origin/release/v0.22.0` exit 0 | |

This table is also where the work records how far it got. **Status is empty, or the commit that closed the phase.** Re-read the column after any rebase.

### Test rows — the mutation each case kills

| Case | Guards | Mutation it kills |
|---|---|---|
| T1 `test_each_real_path_end_to_end`, row *S4 a new case alone kills a mutant of changed code* | S4 | a proof read off a run whose killers are not one function's alone |
| T2 `test_each_real_path_end_to_end`, row *S3 a case its file already covers is named* | S3 | a case that kills only what a sibling kills read as proved |
| T3 `test_each_real_path_end_to_end`, row *a mutant of changed code nothing kills is reported* | S7 | a survivor of changed code left out of the summary, or made a failure |
| T4 `test_each_real_path_end_to_end`, row *a tests-only change draws from the lines its case runs* | S4 | the traced lines a case runs alone not drawn first |
| T5 `test_each_real_path_end_to_end`, row *S2 a changed function is read as new* | S2 | only names absent at the base read |
| T6 `test_each_real_path_end_to_end`, row *S5 a prose pin is proved by its sentence removed* | S5 | a changed `.md` line not mutated |
| T7 `test_each_real_path_end_to_end`, row *a file whose proof would pass the bound is named to restructure* | S2 | the bound read after the mutants run, or never |
| T8 `test_the_five_rows_measure_the_tree_and_an_unlisted_large_file_fails` | S8 | `test-cases` counting functions instead of ids; the `≥ 200` threshold dropped · NAME NOT IN TREE: planted with the measurers, after #930 lands |
| T9 `test_every_kind_has_a_sampled_row` (per enumeration file) | S7 | one kind's rows all removed from the sample: the kind is in the enumeration and has no representative · NAME NOT IN TREE: planted in phase 3 |

Each is seen red by its mutation before it is committed, and the `cases` job proves each on PR #939 by a mutant it derives.

## Operational impact

- One new script, one new job (ubuntu, `contents: read`), one new list file, five rows and one table in `seal/budgets.md` (where #930 is in the tree), measurers in `budget_check.py`. No new dependency.
- Every test function added or changed from phase 2 on owes a `Kills:` line, or the `cases` job is red. The 185 files on `unguarded-files.txt` are exempt for their existing functions until a phase takes them off.
- `.test_durations` is replaced per cut phase by the union #931's job uploads, never edited by hand; a phase that removes under a twentieth of the seconds may leave it.
- An `Enforced by:` line naming a removed or renamed case moves with it in the same pull request; `enforced-unresolved` holds that.
- Item B (legs) and item C (the long tail) are issues the orchestrating session opens; nothing here posts.

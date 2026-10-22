# Phase 5: 1792628098-tests-rebuilt-one-file-per-module

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | |

## What this phase was asked

Batch A: the modules whose old test files price at 60 seconds or more in `.test_durations`. The first step runs the command the plan names, `python3 -c` over `.test_durations` grouped by file and sorted descending, and writes the command and its list here before any edit. The sealer's file goes first, then the commit-gate flow into `tests/e2e/<flow>/`, then the rest heaviest first, one commit per module. The three text-reading files of the commit gate are sampled per kind under `questions.md` Q1's answer, keep.

Each module applies the spec's four rules: the layout; one verdict per old case, with one line per cut or rewritten case in the shape `CONTRIBUTING.md` *The test layout* gives; a rewrite from the code where the module is heavy or `bin/test-layout --pairs` names a pair; and the owner's rule on cost. Under that rule a module builds its fixture repositories once and resets them between cases, judges a command's reading without real git or a real shell and names the real-git rows it keeps, samples one row per kind, and records its seconds before and after.

Each module is proved by a mutation table on #929's pattern, at least one mutation per class. A mutation the old files killed dies in the new file, and one that survives gets a case seen red before the commit. `--pairs` names no pair in the new file, and the record carries the case counts before and after. Phase 4's survived mutations h2, h4, h6, h12, h14, h21 and h23 close where this batch rebuilds the module whose cases reach them. `overview.md` is written now and kept current.

At every module commit and at the phase end the run covers the rebuilt module and every module importing what it moved, `tests/test_censuses.py` and every file `git grep -l "git_listing\|tracked_text_files\|ls-files" tests/` lists, the ten meta modules of phase 1's record, `bin/test-layout --check`, `bin/rules --check` and `bin/unverified-check seal/specs/`. Ruff runs over each changed file alone, never over the repository.

## What this phase found

**Measured at 8aa42bf8, before the first edit** (`executed`). The command:

```
python3 -c "
import json,collections
d=json.load(open('.test_durations'))
s=collections.defaultdict(float); n=collections.Counter()
for k,v in d.items():
    f=k.split('::')[0]; s[f]+=v; n[f]+=1
for f,v in sorted(s.items(), key=lambda x:-x[1]):
    if v>=60: print(f'{v:8.1f} {n[f]:5d} {f}')
print('total', round(sum(s.values()),1), len(d), len(s))
"
```

It prints sixteen files, with their Windows seconds and priced cases:

| Seconds | Cases | File |
|---|---|---|
| 761.1 | 373 | `tests/test_the_seal_is_taken_once_by_the_sealer.py` |
| 519.7 | 185 | `tests/test_the_commit_gate_decides_at_the_commit.py` |
| 279.1 | 672 | `tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py` |
| 242.8 | 51 | `tests/test_no_shape_the_base_stops_reads_silent.py` |
| 203.9 | 277 | `tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py` |
| 173.0 | 103 | `tests/test_the_guard_asks_once_per_session.py` |
| 167.4 | 101 | `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` |
| 126.4 | 83 | `tests/test_chain_check.py` |
| 107.1 | 68 | `tests/test_pact_check.py` |
| 86.1 | 54 | `tests/test_the_root_migrates_itself.py` |
| 82.1 | 148 | `tests/test_worktree_guard.py` |
| 77.3 | 96 | `tests/test_the_records_can_be_carried_out_and_in.py` |
| 62.0 | 106 | `tests/test_a_rewritten_definition_proved_non_inferior.py` |
| 61.8 | 215 | `tests/test_unverified_rows_close.py` |
| 61.3 | 36 | `tests/test_the_gate_asks_the_range_ci_will_ask.py` |
| 60.2 | 87 | `tests/test_the_mode_is_a_row_and_a_command.py` |

The file as a whole prices 7,276 cases in 141 files at 3,996.6 seconds. The frame counted the same sixteen files at a16acb40.

**The modules those files exercise** (`read`, from each file's imports and docstring). A batch is a list of modules, and several files exercise one module.

| Module | Its files in the list above |
|---|---|
| `skills/verify/scripts/broad_gate.py` | the sealer's file, the range file |
| `skills/verify/scripts/seal_stamp.py` | the sealer's file, the stamp file |
| the commit through real git, `tests/e2e/commit/` | the commit-gate file |
| `hooks/commit-review-gate.py` | the wrapper file, the base-shape file, the heredoc file |
| `hooks/worktree-guard.py` | the once-per-session file, `tests/test_worktree_guard.py` |
| `skills/code-review/scripts/chain_check.py` | `tests/test_chain_check.py` |
| `skills/verify/scripts/pact_check.py` | `tests/test_pact_check.py` |
| `hooks/root-migrate.py` | the root-migration file |
| `skills/implement/scripts/seal.py` | the export file, the mode file |
| `evals/scripts/noninferiority.py` | the non-inferiority file |
| `skills/verify/scripts/unverified_check.py` | the unverified-rows file |

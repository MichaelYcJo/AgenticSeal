# Overview: close the mutation gaps the old tests had (#1017)

## Why this work exists

#942 proved its rebuilt test files protect what the old ones did, and on the
way recorded 180 rows, mutants of shipped code or of test helpers that both
the rebuilt and the old files let survive; each row now has one recorded
outcome, and the 123 that stood as gaps are each killed by a case seen red on
its mutant.

## The outcomes across the seven phases

Counted from the outcome tables of `phases/phase-1.md` to `phases/phase-7.md`
and from `spec.md` *Rows whose code left the tree*, which settled 30 rows
before the build and ran no mutant for them. The 150 rows the phases rebuilt
ran as 145 mutants.

| Phase | Rows | Killed by a case seen red | Already closed | Equivalent | Left the tree | Finding |
|---|---|---|---|---|---|---|
| `spec.md` | 30 | 0 | 0 | 0 | 30 | 0 |
| 1 | 25 | 21 | 1 | 3 | 0 | 0 |
| 2 | 24 | 18 | 2 | 3 | 1 | 0 |
| 3 | 21 | 15 | 3 | 3 | 0 | 0 |
| 4 | 20 | 20 | 0 | 0 | 0 | 0 |
| 5 | 18 | 12 | 2 | 2 | 2 | 0 |
| 6 | 25 | 22 | 0 | 3 | 0 | 0 |
| 7 | 17 | 15 | 1 | 0 | 1 | 0 |
| **Total** | **180** | **123** | **9** | **14** | **34** | **0** |

180 is the list `spec.md` *What the list is* defines: the body's 135 rows,
the three comments' 33, 6 and 4, and the two `specseal_pytest_record.py`
survivors. Of the 123 kills, 120 are by an added case, 2 by an existing case
given the ruff config it lacked (phase 2), and 1 by a rewritten case (phase
6, ch6). No row showed a defect in shipped code, so no row is a finding. The
one change to shipped code is the removal of `gh_json`, which closes c13
(`phases/phase-7.md`).

The merge of `release/v0.22.4` at 95fa9fb7, between phases 5 and 6, moved no
outcome. Each of phase 4's 17 pairs in `session_cost.py` and
`broad_gate.py`, the two modules with rows that the merge changed, still
lands once in its module, and s46, the one
row whose function the merge changed, is still red on the case phase 4 named
(`phases/phase-6.md` *The rows the merge moved*).

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Modules with no commit | `plan.md` *Summary*: "each module lands in one commit" / `hooks/one_heredoc.py`, `hooks/tokens.py` and `hooks/blocks.py` (phase 3) and `skills/implement/scripts/seal.py` (phase 5) have none | the code | each of their rows needed no case: four are equivalent and one, k8, was already closed. Their tables stand in `phases/phase-3.md` and `phases/phase-5.md` |
| One module, two commits | `plan.md` *Summary*: one commit per module / `.github/scripts/issue_claims_check.py` took 0a1c3676 and fea473fc | the code | at 0a1c3676 `bin/test-layout --pairs` paired i27's case with `test_an_anchor_is_not_an_issue_number`, and folding them rewrote that case's `def` line, which phase 7's check reads as a removed case. fea473fc restores the case unchanged and gives i27 a case of its own (`phases/phase-6.md`) |
| Rows closed by an existing case | `spec.md` *In* item 1: "a case is added that is seen red on it and green on the code" / phase 2 gave two existing `hooks/lint-python.py` cases the `ruff.toml` they lacked; phase 6 rewrote the case asserting no decline for ch6 | the code | the lint cases built no ruff config, so `uses_ruff` returned before the decision each names, and a new case beside each would assert what the old one meant to; ch6's case could not fail, because the mutant's `pytest.skip` reads as no failure. Each was seen red on its mutant (`phases/phase-2.md`, `phases/phase-6.md`) |
| Rows equivalent against the real dependency, killed by a case that fakes it | `spec.md` *In* item 1: equivalent where "no input tells the mutant from the code" / 8 rows are recorded killed by a case that removes the guarantee: phase 1's `hooks/session-lease.py#git_dir` and `hooks/mode-gate.py#git_dir_of` on a non-zero exit, and the directory tests of `session-lease`'s target and `optin.repo_root`; phase 2's `hooks/implementer.py#git_dir` and `hooks/review-skill-gate.py#git` on a non-zero exit, and s4 of `hooks/sealer-stamp.py`; phase 3's k3 of `hooks/worktree_consent.py` | the code, with each pair recorded so a warden can read the row as equivalent | contract rule 13: a defence resting on a guarantee is not verified until the guarantee is removed. `phases/phase-2.md` says four of its rows rest on such a guarantee and names three |
| The conftest rows' before column | `plan.md` *How a phase rebuilds a row* step 4: a survivor runs against every other test file that loads the module / phase 6 ran the `tests/conftest.py` mutants against `tests/test_conftest.py` alone | the phase 6 row | `plan.md`'s Phases row for phase 6 says so. Every test file runs under `conftest.py`, so step 4's set of files would be the whole suite (`read`) |
| k8 of `hooks/blocks.py` does not reproduce | the round 3 comment of #1017: k8 survives the rebuilt and the old files / red on `tests/test_the_hooks_hide_what_a_renderer_hides.py` under the table's pair and three other readings | already closed | that file, `tests/commonmark_oracle.py` and `hooks/blocks.py` are byte-identical between 208803e6 and the head, so #942's mutant was likely a replacement none of the four is (`phases/phase-3.md`) |
| A module's after batch exits 1 | `spec.md` *A gap that stands is closed*: "the module's `bin/mutation-check` batch with `-x` exits 0 at the phase's commit" / where a module holds an equivalent row, or a row closed by a case in another file, its own-file batch prints `SURVIVED` for that row and exits 1 | the code | the outcomes already closed and equivalent leave those mutants standing on the module's own file by definition. Every row killed by a case is `red` in its after column |

## Names no input reaches, for the repository owner

Each name below decides nothing anyone receives: no input tells the code from
the code without it, or the value it writes is read by nothing. Under
`CLAUDE.md` *The rule a mechanism is kept against*, each may be code to
remove rather than to keep. `spec.md` *Out* leaves shipped code alone apart
from `gh_json`, so this work records them and removes nothing. The repository
owner decides each.

- **`invocation_dir` and `wasxfail`**, two fields
  `skills/verify/scripts/pytest_record/specseal_pytest_record.py` writes into
  each record line. No code reads either; `broad_gate.py#read_record` takes
  neither. Phase 4's cases pin what the module's docstring says a line
  carries (`phases/phase-4.md`).
- **k12, `skills/code-review/scripts/chain_check.py#reopened_of`'s match
  against the `reopens:` row.** `finding_of`, its one caller, has already
  matched the same line whole (`phases/phase-5.md`).
- **s47, `NotImplementedError` in `skills/implement/scripts/seal.py#import_`'s
  except clause.** It is a subclass of `RuntimeError`, which stands in the
  same clause. The comment above it keeps the name as the record of a
  traceback measured on 2026-09-03 (`phases/phase-5.md`).
- **i12, the `< end` bound in `.github/scripts/issue_claims_check.py#read`.**
  Every number the loop reads starts before `end`, so a claim past the end is
  never counted before one (`phases/phase-6.md`).
- **i13, `read`'s `if not here: continue`.** A segment with no claim appends
  no warning either way (`phases/phase-6.md`).
- **i7, the whitespace filter of `issue_claims_check.py#segments`.** `read`
  never needs it, and phase 6 gave it a case only because `segments` is
  public and its docstring promises the filter (`phases/phase-6.md`).

## Not verified

| Item | Who must answer |
|---|---|
| the full suite and the repository-wide lint and format check at the branch head. `seal/config.md`'s `Broad gate` row names no typecheck. Each phase ran its own modules only | the orchestrator, by `broad-gate --base <base> --record` before the sealer |
| the cases on Linux and Windows: every phase ran its cases on macOS only, and each case that reads the platform fakes it | the orchestrator, from the pull request's `tests` workflow on its three legs |
| whether `.test_durations` still prices the suite within its share (`questions.md` Q5): the work item adds 184 lines holding `def test_` since 134d7203 and prices none of them | the orchestrator's broad gate, through `test_the_durations_file_prices_the_suite`; on a failure the orchestrator refreshes the file from the branch's `tests` run artifact and commits it |
| m47's case reads GNU env's grammar, `env -iS '' -vS 'git commit'`, from its documentation; GNU env is not installed where phase 3 ran (`phases/phase-3.md`) | the warden, against GNU coreutils' `env` documentation |

## Not done

The removal of the names in *Names no input reaches*. Each removal changes
shipped code, which `spec.md` *Out* leaves to another work item, so they are
recorded for the repository owner instead.

The classes `bin/test-layout --check` reports as missing, for the public
functions no row names, such as `close_issues_on_release.py#drop_label` or
`tracker_labels.py#missing`. Adding them is a sweep of each module's
functions, which `spec.md` *Out* leaves to another item.

The prices of the new cases in `.test_durations`. The file is refreshed from
the branch's `tests` run artifact, never by hand, and only where the broad
gate's case fails (`plan.md` *Operational impact*).

## Fed back into the spec

none

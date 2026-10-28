# Phase 1: 1793174171-code-no-input-reaches

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | af0c79cc |

## What this phase was asked

Build #1056 with no frame, on the ladder's second rung. For each unit the
issue lists, either remove it or keep it with a comment giving its reason.
Remove a unit only after a `seal mutate` that removes it leaves the module's
tests green, and record each command and its exit code. Keep a unit only
where an input reaches it, and write the reason in the code. Where an item's
premise no longer holds at the tree, record that and build the rest. Do not
edit files held by parallel work items: #1041 holds `chain_check.py`,
`agents/crafter.md`, `docs/the-review-record.md` and
`skills/code-review/orchestration.md`. #1055 holds the READMEs,
`skills/config/SKILL.md`, the hygiene workflows, `docs/the-agent-set.md`,
`skills/implement/SKILL.md` and `CLAUDE.md`. #1042 holds `evals/`. #1043
holds a citation module, `gather_changelog.py` and `mutation_check.py`.
Write a `changelog.md` fragment only if a release note would state the
change.

## What this phase found

**Every premise held at `5287dd42`** (read). The issue's line numbers were
taken at `0b75346f` and still matched. `hooks/worktree_consent.py` stands,
since #1049 has not removed it.

Each `seal mutate` below ran from the worktree's `bin/seal`, with
`-p no:xdist` added to `--tests` (executed). A removal's `--tests` names
every test module that `git grep -l` finds reading the file.

| Item | Mutation | Cases | Verdict, exit | Outcome |
|---|---|---|---|---|
| `invocation_dir` on the recorder's `session` line | `"invocation_dir": _invocation_dir(self.config),` to nothing | `tests/skills/test_agentic_pytest_record.py`, `tests/skills/test_broad_gate.py`, `tests/github/test_release_seal.py`, `tests/behaviour/test_a_release_publishes_its_note.py` | red, 0 | removed, with `_invocation_dir` and the cases pinning it |
| `wasxfail` on the recorder's `test` line | `if hasattr(report, "wasxfail"):` to `if False:` | the same four modules | red, 0 | removed, with the cases pinning it |
| both recorder fields, pinning cases deselected | the same two mutants | the same modules, less `Test_pytest_configure::test_accepts_the_measured_process_as_the_one_that_records`, `-k 'not wasxfail and not xfail_reason'` | SURVIVED for both, 1 | the red came from those three cases alone |
| k12, `chain_check.py#reopened_of`'s None branch | `found = as_row(...)` and `return reference(found) if found else None` to `return reference(as_row(REOPENS_ROW, value))` | `tests/skills/test_chain_check.py` | SURVIVED, 1 | not edited: #1041 holds the file |
| s47, `NotImplementedError` in `import_`'s clause | the tuple without it | `tests/skills/test_seal.py` | SURVIVED, 1 | removed; the comment says `RuntimeError` catches both |
| i12, the `< end` bound in `read` | `start <= c[1] < end` to `start <= c[1]` | `tests/github/test_issue_claims_check.py`, `tests/behaviour/test_a_body_naming_two_issues_claims_one.py`, `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py` | SURVIVED as mutant 1 of one call with i13 and i7, which exited 1 | removed |
| i13, `read`'s `if not here: continue` | the two lines to nothing | the same three modules | SURVIVED as mutant 2 of that call | removed |
| i7, `segments`' whitespace filter | `if text[a:b].strip()]` to `]` | the same three modules | red, 0, from `Test_segments::test_refuses_a_run_of_whitespace_as_a_segment` alone | see the next row |
| i7, its pinning case deselected | the same | the same, `-k 'not test_refuses_a_run_of_whitespace_as_a_segment'` | SURVIVED, 1 | removed, with that case |
| k3, `worktree_consent.py#main`'s `if not session` return | the two lines to nothing | `tests/hooks/test_worktree_consent.py`, `tests/hooks/test_dispatch.py`, `tests/behaviour/test_the_guard_asks_once_per_session.py`, `tests/hooks/test_worktree_guard.py`, `tests/behaviour/test_the_frozen_reading_never_grows.py`, `tests/text/test_guard_resolves_the_tree_it_judges.py` | SURVIVED, 1 | removed |
| m6, `LABEL_DESCRIPTION_LIMIT` | `= 100` to `= 10` | `tests/github/test_label_merged_on_release_branch.py` and `tests/github/test_tracker_labels.py` | red, 0, from one case in each | kept, with its reason |
| `UnicodeDecodeError` in `read_manifest`'s clause | the tuple to `ValueError` alone | `tests/skills/test_seal.py`, `tests/text/test_the_records_can_be_carried_out_and_in.py` | SURVIVED, 1 | removed; the docstring says `ValueError` covers both |

**s47's input is in the suite, and the clause still catches it.**
`tests/skills/test_seal.py:1564` hands `testzip` "a method with no
decompressor", and that case passed with `NotImplementedError` gone from the
clause (executed).

**i12 and i13 fold into one comprehension.** With both gone, `here` was only
the claims from the segment's start onward. `read` now takes the claims
before each number directly, with `start <= c[1] < m.start(1)`. Every number
found in the segment starts before `end`, so the result is the same as
before.

**m6 is kept because the cap belongs beside the description it bounds.** A
person editing `label_description` meets the cap there. A test would show
it only after the edit fails. `tracker_labels.py`'s comment already points
to the constant for its own descriptions. Setting it to 10 turns
`test_the_label_description_fits_the_trackers_cap_for_a_long_version` and
`test_every_declared_description_fits_the_trackers_cap` red, measured again
at `6ced9c82` with exit 0 (executed).

**The class of s47 had one other member.** Every except tuple in the
shipped Python was read for a builtin exception named beside its own base
class (executed, an `ast` walk over `git ls-files '*.py'` less `tests/` and
`seal/`). The only other hit was `read_manifest`'s
`(UnicodeDecodeError, ValueError)`, which was removed in `af0c79cc`.

**`.test_durations` priced six cases this work removed or renamed.** The
five removed entries are deleted. The moved case keeps its time under its new
name. After that, `git grep` outside `seal/threads/`, `seal/process/`,
`changelog/` and `CHANGELOG.md` finds no removed name (executed). The only
hit left is `collects_the_suite`'s parameter `invocation_dir`, which is
pytest's own value and not the recorder's field.

**No unit was added, so no new case was planted.** Each change removes a
unit or rewrites a comment, and the cases that stayed are the measurement.

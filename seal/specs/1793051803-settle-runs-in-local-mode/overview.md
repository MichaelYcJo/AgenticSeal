# Overview: settle runs in local mode (#955)

## Why this work exists

`settle` refused a `seal/` root under the common git directory, so a
local-mode repository's policy root never changed. Now `settle` reads the
local work items there. One is released when the pull request from its
branch merged and `--released-at` reaches the merge commit, and `--apply`
removes the released local directories.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Where S2's case of the new ordering function stands | S2: "a case in `tests/test_rule_changes.py` for the new ordering function" / the case is `tests/test_settle.py::Test_module::test_merge_order_of_local_specs_is_their_merge_commits_place` | the code | `tests/test_rule_changes.py`'s docstring: "Merge order and the ancestry `unordered` reads are facts only git holds, so the cases that read them run `settle` over a repository and are in `tests/test_settle.py`". The case of `rule_changes.py#order` stands in that class, and a new case starts from its group (`agents/smith.md`) |
| A `gh` answer that is not a list | *In* item 4: "Where `gh` is not on `PATH`, or a query exits non-zero, `settle` exits 2" / it also exits 2 where `gh` exits 0 with an answer that is not a list | the code | the same item's reason: "Every local work item reading as unreleased would be the quiet zero the `--released-at` refusal is written against". An answer that cannot be read leads to that same zero |
| What S9's place line says | S9: "the group's place says the heading is not in the working tree" / for an `add` with no `section`, it says "the document is not in the tree in the working tree" | the code | `rule_changes.py#section_lines` answers "the document is not in the tree" for an absent file, whatever the section, and shared mode prints the same line. The case pins the printed words |
| Where a run from a subdirectory reads | *Out*: "Shared mode. Every shared-mode behaviour of both commands stays as #1033 left it." / `settle.py#main` resolves `--root`, or the working directory, to the repository's top through `optin.repo_root` in both modes, so a shared-mode run from a subdirectory reads the repository rather than refusing with "has no seal/specs/ at either place" | the code | round 1 finding 2: from a subdirectory local mode found its root under the git directory but read the policy root under the subdirectory, so a document that is there read as not in the tree. Shared mode's refusal there said the repository has no root, which is false, and a run from the top is unchanged in both modes. `fold_check.py#main` resolves a root typed from a subdirectory the same way. The case is `Test_main::test_a_local_run_from_a_subdirectory_reads_the_repositorys_top` |
| The name of S10's case | S10 and *Removes*: `test_the_module_and_the_skill_both_say_local_mode_is_refused`, "rewritten to these assertions" / it is rewritten and renamed `test_the_module_and_the_skill_both_say_how_local_mode_settles` | the code | the old name states the refusal this work removes. Its `.test_durations` entry went with it, as did the entry of the removed `Test_main::test_refuses_local_mode_rather_than_reading_an_empty_repository` |

## Not verified

| Item | Who must answer |
|---|---|
| the new and rewritten cases of `tests/test_settle.py` and `tests/test_settle_reads_before_it_removes.py` on Windows, where the `gh` stub is a `gh.cmd` that `shutil.which` finds through `PATHEXT` | the branch's `tests` workflow run, its four Windows groups, read by the orchestrator |
| the full suite, the repository-wide lint and format check, and the typecheck at the branch head | the orchestrator's `broad-gate --base <base> --record 1793051803-settle-runs-in-local-mode` run, read by the sealer |

## Not done

Running a settle, in this repository or in a local-mode one. `spec.md` *Out*
leaves it out, since a settle is not a work item. The local path ran against
fixture repositories with a `gh` stub. The real `gh` was asked once, read
only, for a branch of this repository (`phases/phase-2.md`).

The policy sentences of `spec.md` *Rule changes*, and the pin in
`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` on "`settle`
retires no local-mode work item". `docs/` is the policy root, which this pull
request does not edit; the next release's settle writes both and changes the
pin with them.

The prices of the new cases in `.test_durations`. The two removed cases'
entries went. The new cases stay unpriced until the next refresh from a
`tests` run's artifact, well inside `STALE_SHARE`.

## Fed back into the spec

Inferred during implementation, for a planner to overturn:

- In local mode `--released-at` is checked with `git rev-parse --verify`
  before `gh` is asked, so a ref that does not resolve gets the existing
  refusal and `gh` is never asked.
- A listed pull request whose `mergeCommit` is null counts as no merged pull
  request. Where several merged pull requests come from one branch, the
  first one `gh` lists whose merge commit `--released-at` reaches is taken.
- A `routing.md` that `hooks/routing.py#parse` does not read as a
  declaration, such as one whose `Review` row is unreadable, reads as naming
  no branch, even where it has a `Branch` row.
- The `gh` query is bounded at 60 s (`settle.py#GH_TIMEOUT`), and a timeout
  is a refusal.
- The dry run's local line shapes, recorded in `phases/phase-1.md` and pinned
  in `tests/test_settle.py`.

# Review round 3: 1793051803-settle-runs-in-local-mode

target: 49a2dd0d, fixes 137d0a9c..49a2dd0d

This is a verifying round. It read the fix range `137d0a9c..49a2dd0d` and,
as the caller asked, looked over the whole diff `91d57028...49a2dd0d` once
more only for what the fix could have broken. It worked in a
`git clone --no-local` of the repository at `49a2dd0d`. Carried from rounds 1
and 2 and not established again: where `main` resolves the root
(`skills/settle/scripts/settle.py:897`), what the `repo`, `local` and `gh`
fixtures of `tests/test_settle.py` build, and that no `seal/parity.md` is
declared. The fix range changes `tests/test_settle.py`, the divergence row
of `overview.md` and round 2's record, and no file under `skills/`. Every
verdict below was reached again on the code at `49a2dd0d`.

## Findings

No finding opened this round.

## Confirmations

confirms: round-2#1
6d4412ac holds. `Test_main::test_a_shared_run_from_a_subdirectory_reads_the_repositorys_top`
stands at `tests/test_settle.py:863-882`, beside the local case at `:844`.
It runs shared mode with `--root` at `docs/` and asserts that the exit code
and the output equal those of a run from the top, that the refusal "at
either place" is absent, and that `gh` is never asked. What was claimed: the
case was seen red under two mutants. This round wrote both mutants again in
the clone and ran the two subdirectory cases under each. With the refusal
kept for shared mode only, resolving to the top only where the top has no
`seal/`, the shared case fails with "has no seal/specs/ at either place" and
the local case passes. With the resolution removed, which is
`optin.repo_root` answering "", both cases fail. Restored, both pass. So an
edit that brings back the shared-mode refusal now fails the module, which is
what the finding asked for.

The smith departed from round 2's ready-to-paste case in two ways, and both
are right. First, `item` gets `op(...)` and not a list. `spec()` puts its
argument into `## Rule changes` through an f-string
(`tests/conftest.py:1948-1954`), and `op()` returns one string
(`tests/conftest.py:1984-1989`). A list would have put its repr into the
spec. Every other `item` and `local_item` call in the module passes
`op(...)` bare. Round 2's snippet was wrong there. Second, the case asserts
that the run from the top exits 0 and places group 1 at `docs/a.md:3-9`.
Without those two lines the equality holds for any two runs that fail the
same way, for example a spec the reader cannot parse. With them, the
equality compares a real dry run. The place line is the one the local case
already pins at `:858-860`. The `overview.md` divergence row now names both
cases (`overview.md:18`). Executed for the mutants and the module, read for
the rest.

confirms: none
Nothing the fix range touched breaks the rest of the diff. The fix adds one
case and rewrites one table row. No code changed after round 2, so the
reader, the release test for local work items and `--apply` stand as round 2
confirmed them. The new case covers what no case of its group covers: it is
the only shared-mode `main` call in the module whose `--root` is not the
repository's top, and the shared-refusal mutant fails it alone.
`test-layout --pairs` names no pair over `tests/test_settle.py`. The new
case has no `.test_durations` entry, as the local case beside it has none,
and the durations case passes. `uvx ruff check` and `uvx ruff format
--check` over `tests/test_settle.py` report nothing. Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The branch on Windows and macOS at `49a2dd0d`. The dispatched `tests` run 40418119834 at this head was still in progress when this round read it: lint, ubuntu, one macOS group and Windows group 2 had passed | `tests/test_settle.py:863-882` | the orchestrator, from run 40418119834's remaining groups |
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three | `broad-gate.md` | the orchestrator, by `broad-gate` once the rounds settle |
| A local-mode settle run end to end against a real local root and the real `gh`. Only fixture repositories with a stub have run it | `spec.md` *Out* | the owner, at the first local-mode settle |
| Q1's default, `gh` alone, against the hosts and merge methods the owner wants local mode to support | `questions.md` Q1 | the repository owner, at the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_settle.py -q -p no:xdist -k run_from_a_subdirectory`, with `settle.py:897` replaced so that the root resolves to the top only where the top has no `seal/` | exit 1; the shared case fails with "has no seal/specs/ at either place", the local case passes. Line restored |
| the same command, with `settle.py:897` replaced by `root = "" or root` | exit 1; both subdirectory cases fail. Line restored, `git status` in the clone empty, both cases pass |
| `bin/test tests/test_settle.py tests/test_rule_changes.py tests/test_settle_reads_before_it_removes.py tests/test_censuses.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py -q` | exit 0, 366 passed |
| `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite` | exit 0, 1 passed |
| `bin/test-layout --pairs tests/test_settle.py` | 1 file read, 0 pairs |
| `uvx ruff check tests/test_settle.py` and `uvx ruff format --check tests/test_settle.py` | exit 0 each |
| `gh run list --branch feat/955-settle-runs-in-local-mode`, then `gh run view 40418119834` | run 40418119834 at `49a2dd0d` in progress; its completed jobs succeeded |

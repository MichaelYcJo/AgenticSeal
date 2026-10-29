# Review round 2: 1793169126-a-case-passes-before-the-pull-request-and-fails-on-it

target: 98a3b114, fixes c54456d9..98a3b114

This round verifies the fix pass over round 1 and stays inside the fix diff, `git diff c54456d9..98a3b114`. From round 1 it carried only coordinates: the finding's two locations and the reader at `skills/code-review/scripts/chain_check.py:785-787`. The verdict below was reached again on the code at `98a3b114`. `seal/parity.md` is not declared, so no `original:` line is written.

## Findings

None. The one close this round answers holds, and the docstring the fix pass changed, read as new code, holds no defect.

## Confirmations

confirms: round-1#1
Round 1's finding 1 closed `fixed d28b2375`, and the close holds. Read: `tests/conftest.py:418-427` now says every workflow run sets `GITHUB_ACTIONS`, `GITHUB_EVENT_PATH` and the rest, that only a `pull_request` run sets `GITHUB_HEAD_REF`, and that a local run and the broad gate set none. The changelog fragment's first entry (`seal/threads/1793169126-a-case-passes-before-the-pull-request-and-fails-on-it/changelog.md:3`) now opens with the same two facts. Its next sentence, "passed on all three", still names three runs: the dispatch run, the local run and the broad gate. The sweep's code at `tests/conftest.py:432-433` is unchanged in the diff. The crafter claimed `CONTRIBUTING.md:205-208`, `skills/code-review/orchestration.md:195-197` and the purpose line of `gaps.md` stand as true. Each states what a case sees after the sweep, or only that `GITHUB_HEAD_REF` is pull-request-only, so each is true. Executed: `git grep -nE 'workflow_dispatch|no pull request|run with no'` at `98a3b114` over `tests`, `CONTRIBUTING.md`, the orchestration skill and the work item's documents, rounds excluded, found no other sentence saying a dispatch run lacks workflow variables. `frame/design.md:8` says only that the runs before the pull request leave `GITHUB_HEAD_REF` empty, which is true.

confirms: none
The new docstring at `tests/test_conftest.py:560-566` was read as new code. Its old words, "the environment of a run with no pull request", were wrong for the same reason as the finding: a dispatch run has no pull request and still sets workflow variables. The new words say a case and its children "see no workflow variable". That follows from the clause before it, "leaves no name that starts with `GITHUB_`", and the conftest comment uses "workflow variable" in the same sense (`tests/conftest.py:418`). `RUNNER_` variables and `CI` survive the sweep, and `frame/design.md` *Scope* puts them out on purpose: no reader in the tree takes either. Read in context, the sentence names the `GITHUB_` set and no wider one. The case's assertions are untouched. Executed: `bin/test tests/test_conftest.py -q` in a clone at `98a3b114` exited 0 with 54 passed, the figure the crafter reported.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over this branch; `unverified` | the branch at `98a3b114` | the orchestrator, by its one `seal gate` run after the rounds settle |
| `frame/questions.md` M1: this pull request's own `pull_request` run on every platform leg | `.github/workflows/test.yml:35` | the orchestrator, reading the `pull_request` run once the pull request opens |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_conftest.py -q`, in a clone at `98a3b114` | exit 0, 54 passed |
| `git grep -nE 'workflow_dispatch\|no pull request\|run with no' 98a3b114 -- tests CONTRIBUTING.md skills/code-review/orchestration.md seal/threads/1793169126-a-case-passes-before-the-pull-request-and-fails-on-it`, rounds excluded | no sentence left saying a dispatch run lacks workflow variables |

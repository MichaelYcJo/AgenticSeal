# Closing memo: 1793437163-fields-stand-in-marked-blocks

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck over the branch after phase 1 | the orchestrator, by `seal gate --base <base> --record <item>` once the review rounds settle |
| `tests/evals/test_seed_defects.py` failed 7 of its 17 cases twice during phase 1: once in a run with uncommitted edits in the tree, once in a run with a `git stash` entry present. It passed 17 of 17 at `b72008ec` in a clean worktree and on the branch with a clean tree. The cause was not found, and no phase 1 change touches what it reads | the orchestrator, at the broad gate |

## Not done

Phase 1 left the writers' instructions and the evals as they stand, because `frame/plan.md` gives them to phase 3. So `agents/sealer.md`, `skills/code-review/orchestration.md` (its line naming "the one `Verdict:`" of the guarantee), `templates/setup/config.md` *What no row governs* (`Target SHA`, `Broad gate`) and the sealer eval scaffolds and graders still describe the `Target SHA` row, its `; earlier run:` chain and the one `Verdict:` line. The case `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` no longer lists `chain_check.TARGET` and `chain_check.BROAD_GATE`, which left the code; it lists no key of `hooks/lib/fields.py` yet, since the list must match `templates/setup/config.md`, which phase 3 rewrites.

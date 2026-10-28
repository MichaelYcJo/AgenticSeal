# Review round 2: 1793171573-three-cases-pin-the-retired-commit-gate

target: 15b60149, fixes 355576a1..15b60149

This round reads the fix diff, `f8703927`, and the answers `15b60149` wrote
into round 1. It carries round 1's coordinates only: the spec lines
`docs/worktree-guard-spec.md:576-587` and the phase 1 record at `c7f4ed67`.
It opened both again rather than taking round 1's reading of them. Every
verdict below was reached this round.

## Findings

## Confirmations

confirms: round-1#1
The close holds. The module docstring at
`tests/behaviour/test_the_hook_surface_git_offers.py:28-38` now says the four
creation cases pin *Decided before git runs* "and with it the creation half
of *Which tree*". It also says the first two cases are the creation facts
*Which tree* rests on, and that a change retiring *Decided before git runs*
keeps them. In the listing order the first two are
`test_a_refused_creation_leaves_no_worktree_and_keeps_its_branch` and
`test_post_checkout_tells_a_creation_from_a_switch_and_runs_in_the_tree`.
Those are the two that round 1 named as grounds for
`docs/worktree-guard-spec.md:582-584`. The answer claims that no other file
assigns these cases to a rule. A `git grep -l` for the four case names finds
them only in the module, `.test_durations` and round 1's record. The answer
leaves the sentence at `trail/phases/phase-1.md:42-44` as the record of
`5f2efce2`. That sentence describes what that commit did, so it is history
and no rule rests on it (executed for the search; read for the docstring
and the phase record).

confirms: round-1#2
The close holds. The assertion message at
`tests/behaviour/test_the_hook_surface_git_offers.py:175-181` now says that
"The guard's reading of the command can be weighed against a hook again",
and it points to `docs/worktree-guard-spec.md` *Which tree*. That matches
the docstring at `:25-26`. After the fix, `git grep -n "buildable as framed"`
finds the phrase only in round 1's record. The answer lists the other
"switch arm" hits as naming the guard's own arm. Round 1 enumerated the same
hits and found none of them steering to #692's design inside a hook
(executed for the search; read for the message).

confirms: round-1#3
The close holds. The docstring at
`tests/behaviour/test_the_hook_surface_git_offers.py:10-13` now says phase 1
measured the switch and a creation's take-back on 2.34.1, 2.39.5, 2.43.0
and 2.50.1. It says what a take-back cannot undo was found in round 1 of
#692, on 2.50.1 only. Both statements agree with phase 1 at `c7f4ed67`: M1
and M3 there read "executed, 4 gits", and M14 stands under the line saying
everything below it ran on the four gits. Round 1's search of that file for
`-B` and `--no-checkout` found nothing. They also agree with the case's own
docstring at `:284-286`.

The answer says the other statements of these limits give no git version,
and four of them were opened to check:

- `docs/worktree-guard-spec.md:352-357`
- `hooks/lib/cmdline_base.py:15-18`
- `tests/e2e/creation/test_creation_flow.py:4-7`, which says round 1 found them
- `changelog/0.17.0.md:153-156`

None of the four dates them to a git version, so each stands (read).

confirms: none
The fix pass left the module green and the rules whole. `bin/test` on the
module exits 0 with 7 passed on git 2.50.1. `uvx ruff check` and
`uvx ruff format --check` on the module both exit 0. `bin/seal rules --check`
exits 0, and all 266 check lines hold. The crafter's report of 7 passed
matches (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch, which stay labelled `unverified` | the branch at `15b60149` | the orchestrator, through `seal gate` |
| The seven cases on git 2.34.1, 2.39.5 and 2.43.0; this round ran them on 2.50.1 only | `tests/behaviour/test_the_hook_surface_git_offers.py` | the orchestrator, from the CI legs of the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_the_hook_surface_git_offers.py -q -p no:xdist` | exit 0, 7 passed in 3.48 s, git 2.50.1 |
| `uvx ruff check` and `uvx ruff format --check` on `tests/behaviour/test_the_hook_surface_git_offers.py` | exit 0 both |
| `bin/seal rules --check` | exit 0, all 266 check lines in 55 rule files hold |
| `git grep -n "buildable as framed"` | hits only in round 1's record |
| `git grep -l` for the four creation case names | the module, `.test_durations` and round 1's record |
| `git grep -n -i "no-checkout"` over the spec, `hooks/lib/cmdline_base.py`, the creation flow test and `changelog/0.17.0.md` | none of the hits names a git version for the limits |

# Review round 1: 1793171573-three-cases-pin-the-retired-commit-gate

target: 5cd718bd against 6e322bb7

No earlier round record exists, so no fact is carried; every coordinate below
was opened this round. The spec is issue #1039, read with `gh issue view 1039`.

## Findings

### 1. The docstring gives the four creation cases to *Decided before git runs* alone, so the creation half of *Which tree* reads as pinned by no case

severity: should
location: `tests/behaviour/test_the_hook_surface_git_offers.py:16-33`
evidence: read `tests/behaviour/test_the_hook_surface_git_offers.py:4-33`, `docs/worktree-guard-spec.md:576-587`, `tests/behaviour/test_the_hook_surface_git_offers.py:191-242`
verdict: open

Issue #1039 asks the docstring to state "what the seven remaining cases pin
for `docs/worktree-guard-spec.md`". The phase record claims the docstring
"names both rules of the worktree guard and the cases that pin each". The
spec's *Which tree* paragraph at `docs/worktree-guard-spec.md:576-587`
covers a branch switch and a worktree creation. Its creation sentence at
`:582-584` says a creation "can be judged only after git made it, in
`post-checkout`". The docstring states that rule at `:4-6`. Then `:16-17`
gives *Which tree* only the three switch cases, and `:26` gives all four
creation cases to *Decided before git runs*.

Two of those creation cases are the grounds for the creation sentence of
*Which tree*. `test_a_refused_creation_leaves_no_worktree_and_keeps_its_branch`
at `:191` shows that a refusal in `reference-transaction` comes too late to
stop the branch `-b` made. `test_post_checkout_tells_a_creation_from_a_switch_and_runs_in_the_tree`
at `:226` shows that a creation reaches `post-checkout` only after git made
the tree.

Why it matters: this work item chose which cases to delete by reading which
rule each case pins. The issue leaves open whether the guard stays. A later
work item that retires *Decided before git runs* and reads this docstring
would delete the four creation cases. The creation sentence of *Which tree*
would then have no case, and `seal rules --check` would still pass, because
the `check:` line at `:587` names the module and no case.

```python
The four creation cases pin *Decided before git runs*, and with it the
creation half of *Which tree*:
`test_a_refused_creation_leaves_no_worktree_and_keeps_its_branch`,
`test_post_checkout_tells_a_creation_from_a_switch_and_runs_in_the_tree`,
`test_post_checkout_can_take_back_a_fresh_worktree` and
`test_what_a_take_back_cannot_undo`. A creation reaches a hook only once git
has made it. `post-checkout` can take it back, but a branch that `-b` made
stays, `-B` has already reset an existing branch, and `--no-checkout` runs
no `post-checkout` at all. The first two of these are the creation facts
*Which tree* rests on, so a change that retires *Decided before git runs*
keeps them.
```

answer:

### 2. The switch case's failure message still sends its reader to #692's retired design, which the rewritten docstring no longer names

severity: should
location: `tests/behaviour/test_the_hook_surface_git_offers.py:170-175`
evidence: executed `git grep -n "buildable as framed"`, `git show 6e322bb7:tests/behaviour/test_the_hook_surface_git_offers.py`, `git grep -n "writes nothing into a clone's git hooks" docs`
verdict: open

The old docstring ended "that is the moment the design's switch arm becomes
buildable as framed". Commit `5f2efce2` rewrote that sentence at `:22-24`
to "the guard's reading of the command can be weighed against a hook
again". The assertion message of the same case at `:172-174` still says
"The design's switch arm may now be buildable as framed." Only this
message holds the phrase in the tree.

That design put the switch arm inside `reference-transaction`. The spec now
says this plugin writes nothing into a clone's git hooks
(`docs/worktree-guard-spec.md:585`, `docs/the-routing-check.md:13`), so no
document frames that arm. An agent reads the message at the moment the case
goes red, and it points that agent at a design with no document. The commit
corrected one copy of the sentence and left the other, which contract rule
19 asks the same commit to remove.

The class was enumerated over the module: every comment, docstring and
message that names #692's design. The M14 comment at `:245-248` and the
docstring at `:277-279` describe where the creation ladder went and end at
the current rule, so they steer nowhere. This message is the one instance.

```python
    assert (d / "marker.txt").read_text(encoding="utf-8") == "other\n", (
        f"git {verb} left the tree on `main` after reference-transaction "
        "refused it: this git refuses a switch before the tree moves, which "
        "phase 1 of #692 found no git doing. The guard's reading of the "
        "command can be weighed against a hook again "
        "(docs/worktree-guard-spec.md *Which tree*).\n"
        f"hook log:\n{text}"
    )
```

answer:

### 3. The docstring dates the take-back limits to phase 1 on four gits, and they were found in round 1, on 2.50.1 only

severity: should
location: `tests/behaviour/test_the_hook_surface_git_offers.py:7-11`
evidence: executed `git show c7f4ed67:seal/specs/1790815613-a-gate-decides-at-the-moment-of-the-action-not-from-the-text/phases/phase-1.md`, `git log -S"test_what_a_take_back_cannot_undo" --format='%h %s' -- tests`
verdict: open

The rewritten docstring lists "a take-back cannot undo all of it" among
"these facts" at `:7-9`. At `:10` it says phase 1 of #692 measured them on
2.34.1, 2.39.5, 2.43.0 and 2.50.1. Phase 1 at `c7f4ed67` measures the switch
(M1) and a creation's take-back (M3, M14) on the four gits. It has no row for
`-B` or `--no-checkout`, and a search of the file for both found nothing.
The case that pins those two limits says in its own docstring at `:277-279`
that they were found in round 1 of #692, executed on 2.50.1. The case came in
with `9da8cd1a`.

The old docstring said "phase 1 measured them" of the facts the design
depended on, without listing any. The rewrite lists them, which turns the
vague claim into a wrong one. The phase record shows the crafter held the
rebase sentence to the one git that measured it. This sentence did not get
the same care. A reader who asks whether a git older than 2.50 keeps the
`-B` and `--no-checkout` limits reads them as measured there.

```python
decides a creation before git runs. The manual does not state these facts.
Phase 1 of #692 measured the switch and a creation's take-back on git
2.34.1, 2.39.5, 2.43.0 and 2.50.1
(`c7f4ed67:seal/specs/1790815613-a-gate-decides-at-the-moment-of-the-action-not-from-the-text/phases/phase-1.md`);
what a take-back cannot undo was found in its round 1, on 2.50.1 only.
```

answer:

## Confirmations

confirms: none
The issue's three deletions hold. Claimed: the three cases, their three
`.test_durations` entries and `AUTHOR_DATE_LOG` are gone. `git diff
6e322bb7..HEAD` removes exactly those, along with the two `@pytest.mark.rule`
markers. A `git grep` for the three case names, both markers and
`AUTHOR_DATE_LOG` finds them only in this work item's records and in
`seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/design.md:172`.
That file is another work item's quotation of the issue, and the settle
removes it with that item (executed).

confirms: none
The issue's last Done-when line holds. `docs/worktree-guard-spec.md:360` and
`:587` still name the module. `bin/seal rules --check` exits 0 with "all 266
check lines in 55 rule files hold". The module run through `bin/test` exits
0 with 7 passed, on git 2.50.1. `uvx ruff check` and `uvx ruff format --check`
on the module both exit 0. Every import and the `REFUSING_RT`, `ZERO`,
`head`, `POST_CHECKOUT_LOG` and `UNDO` helpers still serve a remaining case
(executed for the runs; read for the helpers, `:47-255`).

confirms: none
The three removed cases protected nothing the seven do not. No hook,
document or skill reads `GIT_AUTHOR_DATE`. A `git grep` outside `seal/` finds
only `GIT_COMMITTER_*` in the eval scaffolds. `reference-transaction` is
named in `docs/` only by the *Which tree* paragraph. In `hooks/` it is named
only by `hooks/stub-remove.py`, which deletes an earlier release's stubs and
relies on no refusal fact (executed). One lost property was weighed: the
removed `--no-verify` case was the module's only refusal at
`refs/heads/main`. The switch case's else branch at `:184-188` would pass
if the hook never ran at all. But the creation case at `:191-205` still makes
`reference-transaction` refuse and asserts a non-zero exit. That shows the
hook runs and refuses in the same harness, on all four gits by phase 1's M3
(read).

confirms: none
Having no changelog fragment is right. Claimed in `gaps.md`: nothing a
plugin user installs, runs or reads changes. The diff touches
`.test_durations`, one test module and this work item's records, and none
of these is something a plugin user installs, runs or reads.
`docs/the-record-layout.md:57-58` says a change to nothing a release note
states owes the fragment nothing. The account gives #1028 as precedent, and
that precedent holds as stated: `changelog/0.22.4.md` has no #1028 entry.
It is a weak ground, though. That removal rode the settle commit `de11df75`,
routed `no work item`, and a settle writes no fragment for anything. The
layout rule is the ground that holds. `changelog/0.22.0.md:73-76` does state
a suite-price change, but there it is one line inside the entry for a
change that shipped (executed for the searches; read for the rule).

confirms: none
The account's figures hold against the diff. The three removed
`.test_durations` values are 3.0129, 7.0986 and 6.1912 seconds, which sum to
16.30 s. The base module defines 10 cases (three parametrized and seven
plain), so 7 remain. `bin/test tests -q -k test_the_durations_file_prices_the_suite`
exits 0 with 1 passed against the whole collection. The 10 passed before the
change was read from the base file, not run (executed for the durations case;
read for the counts, `.test_durations:874-880`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch; the crafter labelled them `unverified`, and that label is honest | the branch at `5cd718bd` | the orchestrator, through `seal gate` |
| The seven cases on git 2.34.1, 2.39.5 and 2.43.0; this round ran them on 2.50.1 only | `tests/behaviour/test_the_hook_surface_git_offers.py` | the orchestrator, from the CI legs of the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_the_hook_surface_git_offers.py -q -p no:xdist` | exit 0, 7 passed in 4.50 s, git 2.50.1 |
| `bin/seal rules --check` | exit 0, all 266 check lines in 55 rule files hold |
| `bin/test tests -q -k test_the_durations_file_prices_the_suite` | exit 0, 1 passed; `git status --short` empty afterwards |
| `uvx ruff check tests/behaviour/test_the_hook_surface_git_offers.py` and `uvx ruff format --check` on the same file | exit 0 both |
| `git grep -n` for the three case names, both markers and `AUTHOR_DATE_LOG` | hits only in `seal/threads/` records |
| `git grep -n "buildable as framed"` | one hit, `tests/behaviour/test_the_hook_surface_git_offers.py:174` |
| `git show c7f4ed67:<phase-1.md>` searched for `no-checkout` and `-B` | no hit |

# Review round 1: 1793240969-pre-rename-readings-outlived-their-release

target: 5b8fcd02 against origin/release/v0.24.1

This is the work item's first round, so no earlier round has coordinates to
carry. Every fact below was established this round, in a clone of the branch
at 5b8fcd02. The implementer's account (the phase records, `gaps.md`, the
commit messages and the spawn prompt) was read as claims, and each claim
below says what was claimed and what was found.

## Findings

### 1. The census comment on the old trailer key counts the lines that spell it, and the count is wrong

severity: should
location: `tests/censuses.py:1007-1012`
evidence: executed `git grep -n SpecSeal-Routing -- :!seal/threads`
verdict: open

The comment on this `KEPT_OLD_NAMES` item tells the next reader when the
item can leave. It says "Two living lines still spell it". The search prints
four lines: `docs/the-routing-check.md:101`, and
`tests/skills/test_chain_check.py:2969`, `:2974` and `:2976`, which are the
S1 case's docstring and its two commits. The comment names two places and
calls them two lines. At the settle that removes the policy sentence, an
agent reading this comment is told one line is left, while three are.

The count is also a value kept beside the tree, which every edit of the S1
case would have to keep in step. `CLAUDE.md` *The rule a mechanism is kept
against* says nothing of that kind is kept. The plan asked for the two
remaining readers to be named, not counted (`frame/plan.md`, the phase 1
row). Naming the two places with no count keeps the comment true however
the case changes.

```python
    # The trailer key a commit made before the rename carries, which
    # `chain_check.py` no longer reads. It is still spelt by the case in
    # `tests/skills/test_chain_check.py#Test_routing_trailers` that pins the
    # key as unread, and by `docs/the-routing-check.md` *At the pull
    # request* until the settle after the release removes that sentence.
    "Spec" + "Seal-Routing",
```

answer:

### 2. The version moved in a commit of its own, not in the commit that adds the work item's changelog entry

severity: should
location: `.claude-plugin/plugin.json`, `seal/threads/1793240969-pre-rename-readings-outlived-their-release/changelog.md`
evidence: executed `git log --format=%h --name-status 1e82fd0a..HEAD -- .claude-plugin/plugin.json seal/threads/1793240969-pre-rename-readings-outlived-their-release/changelog.md`
verdict: open

The orchestrator's account cites `skills/implement/orchestration.md`
*Orchestrator: how the work is routed* for 5b8fcd02. Half of that claim
holds. This is the first pull request into `release/v0.24.1`: the base
1e82fd0a is that branch's head, and no `0.24.0` string is left in the tree
outside the records (executed, `git grep -n 0\.24\.0`). The same paragraph
also says which commit carries the move, at
`skills/implement/orchestration.md:531-533`: "in the first pull request into
the branch, in the commit that adds that work item's changelog entry". The
log shows the entry added at 6306f1f1, the crafter's records commit, and the
version moved at 5b8fcd02, the commit after it.

A pull request into a release branch is squashed (`CLAUDE.md`, the
merge-method rule), so the release branch receives one commit either way and
what ships does not change. The divergence is in this branch's history: a
revert of the changelog commit before the squash leaves the version moved.
The fix folds the version move into the commit that adds the entry. It
rewrites pushed history, so the push is the orchestrator's act. The
precondition is an index with nothing else staged; the uncommitted round
record is untracked, and `reset --soft` leaves it where it is.

```sh
git -C <worktree> reset --soft 6306f1f1
git -C <worktree> commit --amend --no-edit
git -C <worktree> push --force-with-lease
```

answer:

## Confirmations

confirms: none
S1 holds, and its case pins it. Claimed (`trail/phases/phase-1.md`): the case
was seen red at 1e82fd0a. Found: with `key=SpecSeal-Routing` put back into
the format line at `skills/code-review/scripts/chain_check.py:2115` in the
clone, the S1 case
`tests/skills/test_chain_check.py:2965-2980` fails, and the other seven
cases of `Test_routing_trailers` pass. With the branch's line, all eight
pass (executed, the probe rows below). So the case kills the restored
reading, and no sibling in its class does.

confirms: none
S2 holds, and its case pins something its group does not. `bin/seal layout
--pairs` prints `test_reads_the_answer_written_before_the_rename_as_unanswered`
and `test_refuses_an_unreadable_third_axis_as_an_answer_and_keeps_the_declaration`
as equal bodies once strings are normalised (executed). The pair is a
likeness, not duplicate coverage. With the two lines that map the old answer
to `crafter` put back after `hooks/lib/routing.py:251` in the clone, the S2
case at `tests/hooks/test_routing.py:128-141` fails and the sibling passes
(executed). The report exits 0 whatever it prints
(`skills/verify/scripts/test_layout.py:132`), so the pair is no gate either.

confirms: none
S3 and S4 hold: `tests/hooks/test_routing.py` passes whole (55 cases), and
`Test_routing_trailers` passes (8 cases), with
`test_refuses_a_commit_naming_a_work_item_no_declaration_names` and
`test_accepts_the_third_axis_where_it_is_there` unchanged (executed).

confirms: none
S5 holds. `git grep -n -e OLD_TRAILER -e OLD_BY_CRAFTER -- :!seal/threads`
prints nothing (executed, exit 1). The hits under `seal/threads/` are this
work item's frame and the records of 1793201097, which are history.
`tests/test_censuses.py` passes whole (175 cases, executed), and each changed
test module's `census_case` ran inside its module's run.

confirms: none
The frame's measurement holds at this round (`frame/design.md` *Scope*).
For every local branch and every `origin/` branch, `git log
--grep=SpecSeal-Routing <ref> ^origin/main` finds one commit, e1fc252d, on
this branch only; the key stands in its subject, and its trailers carry no
`SpecSeal-Routing`. `git grep` finds no `seal/threads/*/routing.md` on any of
those refs that answers `Implementation` with the old name (executed).

confirms: none
The build matches the design's `## Removes` rows. `OLD_TRAILER`, its
comment, the second `key=` and the docstring words are gone from
`skills/code-review/scripts/chain_check.py:11-15` and `:2096-2115`.
`OLD_BY_CRAFTER`, its comment, its exemption line and the two lines of
`parse` are gone from `hooks/lib/routing.py:72-74` and `:251`. The
`Implementation` row at `skills/implement/orchestration.md:398` reads
`crafter` or `the session`, OPTIONAL; absent reads as unanswered (read).

confirms: none
The policy root is untouched, as `skills/implement/SKILL.md:75` requires of a
pull request. The design's `remove` block quotes
`docs/the-routing-check.md:99-103` word for word, so the settle finds the
sentence it removes (read).

confirms: none
The design's claim that only a reminder is lost holds. The parsed
`implementation` is read against `routing.BY_CRAFTER` at
`hooks/implementer-notice.py:60` and nowhere else under `hooks`, `skills` or
`bin` (executed, `git grep`). No message text changed, so contract rule 14
asks for no new pin.

confirms: none
The class is enumerated (contract rule 12). Every other one-release promise
in a living file is one the design's *Out* list names: `install.sh:49`,
`uninstall.sh:18`, the `SPECSEAL_LANG` lines through 0.24.x, and
`skills/verify/scripts/pact_check.py:190` (executed, `git grep` for *next
minor release*, *minor release after*, *minor release of the rename* and
*through 0.23* or *0.24*). The other `KEPT_OLD_NAMES` items at
`tests/censuses.py:1014-1033` carry no removal promise (read).

confirms: none
`gaps.md` *Not done* says the two stale `.test_durations` entries sit far
below the bound. They are 2 of 6774 entries and 3.284 s of 1235.6 s, which
is 0.27% against `STALE_SHARE = 0.05` at
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:90`
(executed). The label holds.

confirms: none
`gaps.md` *Not verified* labels the full suite, the repository-wide lint and
the typecheck `unverified` and names the orchestrator as their answerer. No
phase record claims a broad run (read, `trail/phases/phase-1.md:1-46`,
`trail/phases/phase-2.md:1-49`). The label is honest.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch | the branch at 5b8fcd02 | the orchestrator, through `seal gate` |
| How long a straight upgrade from a release before 0.23.0 is supported, which decides the readings `gaps.md` *Not done* leaves in place | `frame/questions.md` Q1 | a person: the owner |
| Whether the one issue `gaps.md` *Not done* says the orchestrator files for those readings exists | `gaps.md` *Not done* | the orchestrator |
| The orchestrator's run of three release modules after 5b8fcd02, which this round did not repeat | `.claude-plugin/plugin.json` | the orchestrator, whose run it is |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/hooks/test_routing.py -q`, in the round's clone | exit 0, 55 passed |
| `bin/test tests/skills/test_chain_check.py -q -k Test_routing_trailers`, in the clone | exit 0, 8 passed |
| `bin/test tests/test_censuses.py -q`, in the clone | exit 0, 175 passed |
| `bin/seal layout --pairs`, in the clone | exit 0; 128 pairs printed, one of them the S2 case with `test_refuses_an_unreadable_third_axis_as_an_answer_and_keeps_the_declaration` |
| In the clone, through the Edit tool: `key=SpecSeal-Routing` put back into the format line of `routing_trailers`, and the two lines that map the old answer to `crafter` put back into `parse`. Then `bin/test tests/skills/test_chain_check.py tests/hooks/test_routing.py -q -p no:randomly -k "Test_routing_trailers or test_reads_the_answer_written_before_the_rename_as_unanswered or test_refuses_an_unreadable_third_axis_as_an_answer_and_keeps_the_declaration"` | exit 1: 2 failed, the S1 case and the S2 case; 8 passed. Both edits reverted through the Edit tool, and `git status --short` in the clone printed nothing |
| For each local and `origin/` ref, `git log --format=%H --grep=SpecSeal-Routing <ref> ^origin/main` counted, and `git grep -l` for an `Implementation` row answering the old name in `seal/threads/*/routing.md` at that ref | one commit, e1fc252d, on this branch and its remote; no `routing.md` on any ref |
| `git log --format=%h %(trailers:key=SpecSeal-Routing,valueonly) --grep=SpecSeal-Routing 1e82fd0a..HEAD` | e1fc252d, with an empty trailer value: the key stands in its subject only |
| `python3 -I` over `.test_durations`, summing the two old ids against the file | 2 of 6774 entries, 3.284 s of 1235.6 s, 0.27% |

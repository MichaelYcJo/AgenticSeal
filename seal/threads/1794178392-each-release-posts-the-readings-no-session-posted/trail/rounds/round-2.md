# Review round 2: 1794178392-each-release-posts-the-readings-no-session-posted

```seal
target: 76b01be8 against release/v0.36.0
```

This is a verifying round. The code it reviews is the diff from `9bac36c0`,
round 1's target, to `76b01be8`: the frame fold `d9c51db7`, the merge
`f8e0c3e8` of `origin/release/v0.36.0`, the fix `3ec956f1`, the `gaps.md`
row `466b444a`, and the close blocks `76b01be8`. The round read
`routing.md`, the three frame files, `gaps.md`, `changelog.md` and `pr.md`
whole at `76b01be8`. Round 1's coordinates were carried, not searched again:
`work_item_keys` at `skills/verify/scripts/session_cost.py:3135`, the
*A real work item* scenario at `frame/design.md:182`, and the phase 2 fold
row at `frame/plan.md:81`. Every verdict below was reached again in this
round.

## Findings

### 1. `pr.md` quotes the real-tracker row as the fourth row of *Not verified*, and since `466b444a` it is the fifth

```seal
severity: should
location: `seal/threads/1794178392-each-release-posts-the-readings-no-session-posted/pr.md:7`, `seal/threads/1794178392-each-release-posts-the-readings-no-session-posted/gaps.md:10-11`
evidence: executed `grep -n "^| " seal/threads/1794178392-each-release-posts-the-readings-no-session-posted/gaps.md`; read `seal/threads/1794178392-each-release-posts-the-readings-no-session-posted/pr.md:7`
regression: round-1
```

Why it matters: the unit is `gaps.md` *Not verified*, the table the fix
pass changed in `466b444a`. `frame/plan.md`'s phase rows say the suite stays
`unverified` until the orchestrator's broad gate, and the fix pass recorded
its own unverified suite by inserting a row at line 10, above the
real-tracker row, which moved that row from fourth to fifth. `pr.md:7`
still gives its coordinate as "`gaps.md` *Not verified*, the fourth row".
The quote's words still stand in `gaps.md`, but the coordinate now names
the fix pass's suite row, whose text is not the quote. `seal pr-body` builds
the pull request body from `pr.md`, and the sealer checks each quote at the
coordinate it names, so the sealer meets a quote that is not at its
coordinate. `pr.md` is the orchestrator's to repair. No other sentence of
the work item's records counts the rows of *Not verified*.

```markdown
- "`seal cost --work-item <dir> --post` against the real tracker: a real comment posted, and `gh api --paginate` read over a log whose comments span more than one page." (`gaps.md` *Not verified*, the fifth row)
```

```seal
verdict: fixed 102ac764
answer: The orchestrator applied the round's line as given. `pr.md:7` now cites the real-tracker row as the fifth row of `gaps.md` *Not verified*, which is where `466b444a` left it, and the quoted text is unchanged.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `work_item_keys` takes the name as
`os.path.basename(os.path.abspath(directory))`
(`skills/verify/scripts/session_cost.py:3135`), so `.` and `..` key on the
directory's own name. The new case
`test_a_relative_directory_is_keyed_by_its_own_name` covers `.` from inside
the directory and `..` from `trail/`. Beside the `./bin/test` prompt it puts
a prompt naming the directory, so it shows that the real name is the key.
This round put `normpath` back in place of `abspath` through the Edit tool
and ran the case. Both items failed on its first assertion, with
`1 naming . or feat/12-a-work-item` and `1 naming .. or feat/12-a-work-item`.
It then restored the line, and `git status --short` was empty (executed).
The close's claim about the class holds. Every other `basename` call in the
module takes a transcript's path, not a directory (executed, `grep -n basename`).
`--work-item /` keys on the empty string, has no `routing.md`, and is refused
before the walk (read, `skills/verify/scripts/session_cost.py:3136-3148`). The
new case is read against `Test_work_item`. No other case gives a relative
directory, and `bin/seal layout --pairs` printed no pair for the class in
round 1. The fix adds no unit beyond the one line and the case.

```seal
confirms: round-1#2
```
What holds: the scenario at `frame/design.md:182` now gives three
transcripts for this work item's directory: #1439's framer, #1443's framer
and the crafter. `trail/phases/phase-2.md:158` quotes the same three. The
phase 2 fold row at `frame/plan.md:81` now reads "gives the transcripts each
run found", and a new row at `frame/plan.md:83` records the fold. Both
clauses match the round 1 snippets word for word (read, the diff of
`d9c51db7`).

What matched: the merge `f8e0c3e8` touches none of this work item's files.
`git diff --name-only 9bac36c0 f8e0c3e8` lists no README, no
`skills/verify/orchestration.md`, no `session_cost.py`, no
`test_session_cost.py`, no `test_a_segment_feeds_the_flow_log.py`, and none of
`docs/running/measuring-a-run.md`, `docs/releasing/release-checklist.md`,
`lib/routing.py` or `lib/blocks.py` (executed). So the overlap paragraph of
`frame/design.md` *Scope*, which says the #1441 and #1442 branches change
none of this item's files, still holds now that both have merged. #1441
rewrote the *Phase boundary* and *Review rounds 1..n* rows of
`skills/verify/SKILL.md`. The phase records cite their runs at the commits
they name and no rule of that table, so neither contradicts HEAD. #1441 also
moved `tests/test_censuses.py`'s tree-wide run to
`tests/behaviour/test_every_tracked_file_meets_every_census.py`. The
`splitlines` exemption phase 2 names at `log_comments` still passes there
(executed, below). Every section the records cite still stands under its
name at HEAD: `skills/implement/orchestration.md` *Orchestrator: the order
inside a ticket* and `skills/implement/SKILL.md` *Document layout — two
roots, three lifetimes* (executed, `grep -n` of the headings).

What matched: each quote in `pr.md` stands word for word, with runs of
whitespace collapsed, in the file its coordinate names (executed,
`python3 -I` comparison). Finding 1 is about the row ordinal, not the words.

What matched: the new `gaps.md` row names the orchestrator as the answerer
of the fix pass's unverified suite, so the label is honest (read,
`gaps.md:10`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether HEAD's rule asks for the framer to read `d9c51db7`. Since #1442 merged in `f8e0c3e8`, *Orchestrator: the order inside a ticket* counts "a round finding located in a frame file" among the decisions the framer folds. The orchestrator folded round 1's finding 2 itself, at `d9c51db7`, before the merge, under the rule then on the branch, and `frame/plan.md:83` cites that section as what it judged against. The fold's text is right; whether the process owes a framer read now is a reading of the rule, not of the tree | `frame/plan.md:83`, `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* | the orchestrator |
| The full suite, the repository-wide lint and the format check at `76b01be8`. Contract rule 2 gives them to the orchestrator, and `gaps.md` labels them so | the branch at `76b01be8` | the orchestrator, at the broad gate |
| Whether the `--spawns` page's description labels may leave the machine, carried open from round 1 | `skills/verify/scripts/session_cost.py:2433`, `gaps.md` *Not done* | the repository owner |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_session_cost.py -q -p no:xdist -k test_a_relative_directory_is_keyed_by_its_own_name`, with line 3135 set back to `normpath` | 2 failed, each on `1 naming . or ...` / `1 naming .. or ...`; the line was restored and `git status --short` was empty |
| `bin/test tests/skills/test_session_cost.py tests/text/test_a_segment_feeds_the_flow_log.py -q` | 291 passed, exit 0 |
| `bin/test tests/behaviour/test_every_tracked_file_meets_every_census.py tests/skills/test_test_layout.py -q` | 83 passed, exit 0 |

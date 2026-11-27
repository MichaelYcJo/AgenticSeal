# Review round 3: 1795736973-the-preflight-passes-where-a-round-is-owed

```seal
target: 30d8f7ab6, fixes 540c757fa..30d8f7ab6
```

This is a verifying round. It answers the two findings round 2 closed. The fix diff is `540c757fa..30d8f7ab6`, which holds four commits. `c0b2acbfc` is round 2's record. `246ac9e78` is the framer's fold of `frame/design.md:49` and `:96` together with the orchestrator's new row of `frame/plan.md` *Judgments of the run*. `c8b561469` is the crafter's change to `tests/behaviour/test_chain_hooks_hardening.py`, and `30d8f7ab6` adds the close blocks. The code this round reviews stays inside that diff. Beside it, this round read these files whole at `30d8f7ab6`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/rounds/round-1.md` and `trail/rounds/round-2.md`. `Commit and pull request language` is English, so no `pr.<lang>.md` stands. No `seal/parity.json` is declared, so no comparison with an original is owed.

Facts carried from rounds 1 and 2 and not re-established: `chain_check.py#follows` admits only commits inside the work item's directory after the last `target:`. `.github/workflows/hygiene.yml` and `templates/setup/hygiene.yml` pass no `--sealing`. Round 1 walked the check's nine arms against what exists when the preflight runs. The `--sealing` branch of `#_checked` and the one call of `pull_request_from_gh` stand as round 2 read them. Round 2 also confirmed `gate-to-pull-request.md:186-191`. The fix diff touches no script, no skill and no README, so none of these facts was re-derived. This round re-established `origin/release/v0.39.2` at `e65830869`, the version `0.39.2` in `.claude-plugin/plugin.json`, the files the work changes outside `seal/threads/`, #1630's state, and the S7 search.

## Findings

### 1. A *Judgments of the run* row counts what the third round reads and calls the `## Removes` row the one cell of its kind, while its own commit narrows a second

```seal
severity: should
location: `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/frame/plan.md:53`
evidence: executed `git diff 540c757fa 30d8f7ab6 -- seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/frame tests`, `git grep -n -F -e 'one frame cell' -e 'the one cell' -e 'one test line' -- seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed ':!seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/trail/rounds'`; read `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/frame/plan.md:53`, `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/frame/design.md:49`, `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/frame/design.md:96`, `git show 246ac9e78`, `skills/implement/orchestration.md:31-36`, `skills/agent-contract/SKILL.md` rule 19
regression: round-2#2
```

Why it matters: the unit is the second row of `frame/plan.md` *Judgments of the run* (`:53`), which `246ac9e78` added. That is the commit round 2's finding 2 closes as `fixed`. The frame does not cover this row: neither the phase-1 row of `frame/plan.md` nor `frame/design.md` names it. The fold was meant to narrow one `## Removes` cell, and the same commit wrote the orchestrator's row. The row's count describes round 2's paste-ready fixes, not the fold that the commit made.

The row makes two claims that the target contradicts:

- Its judgment cell says "a third round reads one test line and one frame cell". The fix diff holds two frame cells, `frame/design.md:49` and `:96`. It also holds three changed lines of the test module: the tuple entry and two lines of the comment above it (`git diff 540c757fa 30d8f7ab6`, executed).
- Its grounds cell says "no *Scope* item claims to be the whole list" and "The `## Removes` row is the one cell that does". The commit message of `246ac9e78` says that "the *Scope* Out item of the same shape is narrowed the same way". That item is `frame/design.md:49`, which the same commit narrowed. So the framer judged a second cell to be of the same kind, in the commit that wrote the row calling `## Removes` the one cell.

`skills/implement/orchestration.md:31-36` says the rows of *Judgments of the run* follow contract rule 19. Rule 19 says that what a change writes states no count and no universal about the tree that a later change can make false without editing the sentence. These two were false when they were written. The settle reads this row against what the run cost and caught (`skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both*), so its account of the third round's size and of which cells claimed a whole list is a sentence that a reader acts on.

The grounds quote round 2's confirmation, which said that the fold "narrowed the two that did, S7 and item 3". That confirmation missed `:49`. This round carries no verdict from it.

The crafter's close of round 2's finding 2 says its whole read of `frame/plan.md` found no statement that HEAD contradicts. That read reached this row. The row can be read as the size of round 2's paste-ready fixes, and that reading holds. This round judges that the crafter took a different reading of one sentence, not that it handed a sample back as a whole list, so the method half is confirmed below.

The search above prints `frame/plan.md:53` alone. It is a sample under contract rules 12 and 19, since the same count can be stated in other words.

`frame/plan.md:53`, in the judgment cell, the last clause:

```markdown
The run goes on: round 2's findings are two `should`s with a paste-ready fix each, and a third round reads the fix of `NETWORK_PLACES` and the fold of `frame/design.md`
```

`frame/plan.md:53`, the grounds cell whole:

```markdown
A fold whose source is a fix removes or narrows what HEAD contradicts and writes no account of what was built (round 2, its confirmation of the orchestrator's judgment). The `## Removes` row named its coordinates as every sentence of the kind, which the parity and README rewrites show they are not
```

This finding is located in the work item's records alone. Its fix is the orchestrator's row, which the sealer reads by the row *No fix that no round reads* of `skills/core/SKILL.md` *Judgment is not licence to skip a party*.

```seal
verdict: fixed 596b456cf
answer: The finding holds. The orchestrator made this fix pass itself, by `skills/implement/fix-pass.md`. `596b456cf` replaces the row's judgment clause with the paste-ready sentence, and its grounds with the orchestrator's own words, which name both cells the fold `246ac9e78` narrowed, the `## Removes` row and the *Scope* Out item, in place of the paste-ready "The `## Removes` row named its coordinates", which names one. The reading: after `596b456cf`, the orchestrator printed `routing.md`, `gaps.md`, `changelog.md`, `pr.md` and the three frame files whole into one file with `cat` and read that file whole, 225 lines, none cut. It found one more statement HEAD contradicts, the first row of `frame/plan.md` *Judgments of the run*, which said the framer folds "the two frame lines" while the fold of round 1's findings, `adf2bf488`, narrowed a third, *Scope* item 3's opening sentence. `c3ab1d1d9` narrows it to "their frame lines", and its hunk was printed with `git show -U0 --word-diff=plain` after that commit. It also checked the one present-tense statement of the tree the read met outside a dated section, `frame/plan.md` *Overlap with the release*: after `git fetch`, `origin/release/v0.39.2` is `e65830869` and no branch names #1624, #1628 or #1629 (executed). The statements of `## Grounding`, *Technical context* and `routing.md` *Why this way* are dated to `a1cae2026` and stand as dated. Run again after `c3ab1d1d9`, the finding's search, `git grep -n -F -e 'one frame cell' -e 'the one cell' -e 'one test line'` over the work item outside `trail/rounds`, prints nothing (executed). Held and not read again after `c3ab1d1d9`: the six files other than `frame/plan.md`, which neither fix commit changed (`git log --oneline 901bb5c96..HEAD` names the two commits, both on that file alone), and `frame/plan.md` apart from that hunk. The fix touched the records alone, so the sealer reads it in place of a round.
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: `tests/behaviour/test_chain_hooks_hardening.py:430` now holds `"--sealing"`, and both README rows carry that string (`README.md:409`, `README.ko.md:406`, read). A `grep -n -e '--sealing'` over both editions prints those two rows and no other line (executed), so no other line of either passage carries the string. In the clone at the target, the `Edit` tool put `README.md:409` back to its text at `15e831a0e`, and `git diff --quiet 15e831a0e -- README.md` exited 0. `test_the_places_that_reach_the_network_are_named` then failed at `:470` with `AssertionError: ('README.md', '--sealing')` (executed). The row was restored, and the same was done for `README.ko.md:406`, which failed with `('README.ko.md', '--sealing')` (executed). Both files were restored. This matches the close's seen-red account. The case is now red against each stale row, which is what round 2 found missing. The comment above the tuple says that `--sealing` finds the row, which is what the tuple holds.

```seal
confirms: round-2#2
```
What holds: the frame half. `frame/design.md:96` now reads "The sentences the frame located that say the gate's run is judged by the pull request's state", which is round 2's paste-ready cell (read). The fold also narrowed `:49` to "The sentences the frame located that open the gate's step". That sentence holds: `git grep -n -i 'no finding open' -- ':!seal/threads'` prints `skills/code-review/SKILL.md:20`, `skills/implement/orchestration.md:531` and `skills/verify/orchestration.md:25`, the three places `:49` names, plus a test docstring (executed). The narrowed sentence states nothing that HEAD contradicts.

The method half. The close says the pass read `routing.md`, `gaps.md`, `changelog.md`, the three frame files and `frame/questions.md` whole after `c8b561469`, and ran two checks. Both checks reproduce at the target (executed). First, `git diff --stat e65830869 30d8f7ab6 -- ':!seal/threads'` lists thirteen files at the target, and none is a file that `frame/plan.md` *Overlap with the release* gives to #1624, #1628 or #1629. Second, `gh issue view 1630` shows the issue open and labelled `from-review`. This round's own whole read found one sentence that HEAD contradicts, the row of finding 1. Finding 1 says why this round reads it as a difference of reading and not a sample.

What matched: the records read whole at the target, apart from finding 1. `routing.md` dates its account of the check to `a1cae2026`, and its version claim holds: `.claude-plugin/plugin.json:4` reads `0.39.2` (read). `frame/plan.md` *Overlap with the release* says `origin/release/v0.39.2` stands at `e65830869` and that no branch names #1624, #1628 or #1629. Both still hold (executed: `git ls-remote origin` on those patterns and `git branch -a`). S5's `a_sealed_run` and `test_the_fixture_branch_passes` stand at `tests/skills/test_broad_gate.py:2137` and `:2335` (executed). S7's search prints nothing (executed). `gaps.md` *Not done* says `docs/checks/the-pull-request-check.md` still has no clause for `--sealing`, and that file's lines 17-19 bear it out (read). `pr.md` quotes `frame/plan.md:44` in two parts, and both are its words (read). `changelog.md` and `trail/phases/phase-1.md` are unchanged in the fix diff and state nothing the fix diff contradicts (read).

What matched: the fix diff adds no test case. It changes one tuple entry and its comment. `chain_check.py --worktree` at the target, before this record was written, printed no pin or copy notice at a line of `frame/design.md` (executed, `## Probes`).

The comment at `tests/behaviour/test_chain_hooks_hardening.py:423-424` now says the place is found by `--sealing`, "which the row held before #1620 did not carry". That clause is about a former state, and `skills/core/SKILL.md` *The rule a mechanism is kept against* sends history to git and the work record. The case holds no fact the frame states, since *Scope* names no README. So by `skills/code-review/SKILL.md` *The record* the clause gets this sentence and no finding.

What matched: the label. `gaps.md:7` leaves the broad gate `unverified` and names the orchestrator as its answerer. That is honest, because this round ran four test modules and no broad run.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the target: the full suite and the repository-wide lint, which no agent runs (contract rule 2). Finding 1 is located in the records alone, so once it is closed no round is owed. The orchestrator's broad run comes due then, and the sealer's spawn after it | `seal gate --base origin/release/v0.39.2 --record seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed` | the orchestrator |
| The fix pass's narrow set, `1112 passed` (`round-2.md:38`), which this round read and did not run | `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/trail/rounds/round-2.md:38` | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `README.md:409` set back in the clone at `30d8f7ab6` to its text at `15e831a0e` with the `Edit` tool; `git diff --quiet 15e831a0e -- README.md`; `bin/test -q -p no:xdist tests/behaviour/test_chain_hooks_hardening.py -k test_the_places_that_reach_the_network_are_named` | `git diff` exit 0; test exit 1, 1 failed, `AssertionError: ('README.md', '--sealing')` at `:470`; the row was restored with the `Edit` tool |
| The same for `README.ko.md:406`, with `README.md` restored | `git diff` exit 0 for each file as described; test exit 1, 1 failed, `AssertionError: ('README.ko.md', '--sealing')`; the row was restored, and `git status --short` in the clone printed nothing |
| `bin/test -q tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/text/test_no_passage_is_pasted_into_a_second_file.py`, in the clone at `30d8f7ab6` | exit 0, 87 passed |
| `python3 skills/code-review/scripts/chain_check.py --baseline e65830869 --root <the branch worktree> --worktree`, before this record was written | exit 0. The state line is the unseen one, and `gh pr view` found no pull request. One line on `round-2.md:37` says a verifying round is owed for finding 1. One says the last `target:` is behind HEAD at `c8b56146`. Notices say git carries no `trail/gate.md` and no `guarantee.md`. No pin or copy notice appears |

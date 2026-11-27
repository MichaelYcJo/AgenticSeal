# Review round 2: 1795736973-the-preflight-passes-where-a-round-is-owed

```seal
target: 540c757fa, fixes 15e831a0e..540c757fa
```

This is a verifying round. It answers the five findings round 1 closed. The fix diff is `15e831a0e..540c757fa`: the round record `c534251cb`, the framer's fold `adf2bf488`, the crafter's fix commits `acf0a786f`, `056c77b95`, `d862d06d3` and `647361d95`, the close blocks `5b6806084`, and the orchestrator's `gaps.md` sentence `540c757fa`. The code this round reviews stays inside that diff. Beside it, this round read these files whole at `540c757fa`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/rounds/round-1.md`. `Commit and pull request language` is English, so no `pr.<lang>.md` stands. No `seal/parity.json` is declared, so no comparison with an original is owed.

Facts carried from round 1 and not re-established: `chain_check.py#follows` admits only commits inside the work item's directory after the last `target:` (`skills/code-review/scripts/chain_check.py:1003-1029`); `.github/workflows/hygiene.yml` and `templates/setup/hygiene.yml` pass no `--sealing`; and round 1's walk of the check's nine arms against what exists when the preflight runs. The fix diff touches none of them. This round re-established the `--sealing` branch of `#_checked` (`chain_check.py:2237-2249`), the split of the `original:` arm (`:2349-2358`), the one call of `pull_request_from_gh` (`:588`), and the two places that print `VERIFYING_ROUND` (`:959-966`, `:1505-1515`), all read at the target.

## Findings

### 1. `NETWORK_PLACES` pins a word the stale README rows also held, so the README fix is not pinned

```seal
severity: should
location: `tests/behaviour/test_chain_hooks_hardening.py:422-433`
evidence: executed in the clone at `540c757fa`: both README rows set back to their text at `15e831a0e` with the `Edit` tool, `git diff --quiet 15e831a0e -- README.md README.ko.md` (exit 0), then `bin/test -q -p no:xdist tests/behaviour/test_chain_hooks_hardening.py -k test_the_places_that_reach_the_network_are_named` (exit 0, 1 passed); `awk` over each edition's passage, from its opening sentence to the next heading, into `grep -c -e '--sealing' -e '--worktree'` (0 for each edition with the old rows); read `tests/behaviour/test_chain_hooks_hardening.py:422-469`, `README.md:409`, `README.ko.md:406`
regression: round-1#1
```

Why it matters: `tests/behaviour/test_chain_hooks_hardening.py#NETWORK_PLACES`, which `acf0a786f` changed, now finds the README row by the string `"chain_check.py"` (`:429`). The rows the fix replaced held that string too. `README.md` said "asked by its `chain_check.py` step", and `README.ko.md` said "`chain_check.py` 를 돌리는 단계가". So `test_the_places_that_reach_the_network_are_named` passes over both editions with the stale rows put back, as this round ran. The rows tell a person which runs reach their repository through their own `gh` login. A later edit that puts back "`seal gate` asks `gh`" stays green.

Contract rule 14 asks that a fix that changes what a person reads is pinned in the same commit. The diff changed that row, and no case holds it, which is the `should` that `skills/code-review/SKILL.md` *The record* gives a gap of this kind. The close block says the case was seen red by deleting the new row. That run removes the place's name itself, not the fact the fix wrote. Under contract rule 15 it does not show that the case holds the fix. The frame says nothing of the README: *Scope* items 1 to 7 name no README file, and the phase-1 row of `frame/plan.md` names no README case. The fix took round 1's paste-ready entry `"chain_check.py"` as written, and the defect came from that snippet, which chose a string the old rows held too.

Both new rows hold `` `--sealing` ``. The awk run above found no `--sealing` in either passage with the old rows in place. So that string tells the two rows apart, as `"--post"` stands for `seal cost --post`.

`tests/behaviour/test_chain_hooks_hardening.py:429`:

```python
    "--sealing",
```

The comment above the tuple (`:422-425`) already names the place as "`chain_check.py` run without `--sealing`" and stays. The fix pass shows the case red with the two README rows put back to their text at `15e831a0e`, not with a row deleted.

### 2. The frame's *Removes* row still names its five coordinates as all the sentences of the old judgment, and the fix pass read the records by search

```seal
severity: should
location: `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/frame/design.md:96`, `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/trail/rounds/round-1.md:175`
evidence: executed `git grep -n -i -e 'old judgment' -e 'old fact' -e 'rewritten in place' -e 'judged by the pull request' -- seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed ':!seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/trail/rounds'`; read `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/frame/design.md:39`, `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/frame/design.md:62`, `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/frame/design.md:96`, `git show 056c77b95 -- skills/parity-setup/SKILL.md`, `git show acf0a786f -- README.md`, `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/trail/rounds/round-1.md:175`, `agents/crafter.md` *Before you hand back, your range and the work item's records are read whole against HEAD*, `skills/implement/orchestration.md:84-87`
reopens: round-1#5
```

Why it matters: round 1 finding 5 found that the frame handed back a sample of the old judgment's statements as the whole list. The fold `adf2bf488` narrowed S7 to "The four statements of the old judgment the frame located" (`design.md:62`). It also narrowed *Scope* item 3 to "These statements of the old fact in the code" (`:39`). The `## Removes` row at `:96` makes the same claim and was not narrowed. Its first cell reads "The sentences that say the gate's run is judged by the pull request's state", and its coordinates name five places in `broad_gate.py`, `chain_check.py` and `skills/core/SKILL.md`.

At the target the work also rewrote two other such statements. `056c77b95` rewrote `skills/parity-setup/SKILL.md:71-76`, which said that the gate "refuses a round record without it once a ready pull request is open for the branch, and that before then it names the record and passes". That sentence says the gate's run is judged by the pull request's state. `acf0a786f` rewrote the README rows, which said the gate's chain step asks `gh` whether the pull request is a draft. The row names neither. The sealer reads `## Removes` against the tree, and a first cell that names a whole class tells it the five coordinates are all of them. The search above prints the three frame lines `:39`, `:62` and `:96`, and no other statement of that list in the records. It is a sample under contract rules 12 and 19, since the list can be stated in other words.

`skills/implement/orchestration.md:84-87` gives the fold that is owed. A fold whose source is what a fix changed "removes the frame sentence HEAD contradicts, or narrows it to what HEAD still holds, and writes no new account of what was built". So the row is narrowed, and the parity and README rewrites are not added to it. That is the orchestrator's judgment for *Scope*, and it holds there (`## Confirmations`).

The fix pass's account is the other half of the finding, the one about its method. Its close of round 1 finding 5 (`round-1.md:175`) says: "My records read after `647361d95` (executed): `routing.md`, the three frame files and `gaps.md` by search for this pass's facts, and `changelog.md` and `phase-1.md` by their diff. Each statement in them that HEAD now leaves incomplete is in the hand-back for the orchestrator to fold." `agents/crafter.md` *Before you hand back, your range and the work item's records are read whole against HEAD* asks that those files be read whole. It calls them a closed set of which "none of it is handed on as a sample". A search for the pass's own facts is a sample, and the account's last sentence makes a claim about each statement on the strength of it. The row above is one that a whole read of `frame/design.md` reaches once `056c77b95` stands. No record shows it folded or named, so whether the hand-back named it is a row of `## Not judged`.

`frame/design.md:96`, the row's first cell:

```markdown
| The sentences the frame located that say the gate's run is judged by the pull request's state |
```

The cell is the framer's to fold, as finding 5's S7 line was (`frame/plan.md` *Judgments of the run*, the row of 2026-11-27). The fix pass that answers this finding reads `routing.md`, the three frame files, `gaps.md` and `changelog.md` whole after its last fix commit. Its `answer:` says it did, and names each statement HEAD contradicts that the read found, or says it found none.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `README.md:409` and `README.ko.md:406` now name `chain_check.py` run without `--sealing` as the place that sends `gh pr view --json isDraft`, and say that `seal gate` asks `gh` nothing. That is what the code does. Under `--sealing`, `#_checked` does not call `pull_request_state` (`chain_check.py:2237-2239`, read). That function holds the one call of `pull_request_from_gh` (`:588`, read). `GITCMD.gh` is called at `chain_check.py:635` and nowhere in `broad_gate.py`; under `skills/verify/scripts/` the one other call is `session_cost.py:2802`, which the `seal cost --post` row covers (executed, `grep` over both scripts and `grep -rn` over `skills/verify/scripts/`). The departure at `CONTRIBUTING.md:202-206`, "and `--sealing` is not given", states the same limit. The finding's evidence search, run again at the target, prints `CONTRIBUTING.md:202`, `README.md:409`, `README.ko.md:406` and `docs/releasing/branch-and-release.md:361`, as the close says (executed). The rows hold. The case that should pin them is finding 1.

```seal
confirms: round-1#2
```
What holds: `skills/parity-setup/SKILL.md:71-76` says that the gate's preflight and broad run refuse a round record without its `original:` line, whatever the pull request's state. Under `--sealing`, `#_checked` moves only the guarantee's `original:` line to the notices (`chain_check.py:2349-2358`, read). So a round record's missing line stays a problem, and the strict run fails on it. "No workflow refuses it at the pull request" agrees with the sentence's own premise, that under shared, records only, no workflow reads a round record. The finding's evidence search, run again at the target, prints `skills/code-review/scripts/chain_check.py:335` and `skills/implement/bootstrap.md:137`, as the close says, and neither states when the gate refuses (executed).

```seal
confirms: round-1#3
```
What holds: `skills/code-review/gate-to-pull-request.md:186-191` now says that no edit of a record answers a line carrying `VERIFYING_ROUND`, and that the orchestrator spawns the round it owes. The fix pass departed from the paste-ready text, and its grounds hold. The check prints those words in two places (read): a `fixed` or `rejected` close that no later round read (`chain_check.py:959-966`), and a commit outside the work item after the last `target:` (`:1505-1515`). Both lines name the last round record. So "spawn the verifying round it owes" covers both, and "on the last fixes' diff" covers only the first. The cited heading stands at `skills/code-review/orchestration.md:125` (read). No other text tells the orchestrator what to do with a preflight's exit 1 (executed: `git grep -n -e 'PREFLIGHT FAILED' -e 'correct the record' -e 'BROAD GATE FAILED' -- ':!seal/threads' ':!tests' ':!evals'`, whose other hits describe the output). `tests/behaviour/test_docs_line_wrap.py` passed over the file (executed, `## Probes`).

```seal
confirms: round-1#4
```
What holds: the four statements now keep the limit to the state. `changelog.md:3` reads "asks neither the event payload nor `gh` for it". The comment at `chain_check.py:314-316` reads "neither the payload nor `gh` is asked for the state". `phase-1.md:7` adds that the body arm still reads the payload. S6 at `frame/design.md:61` names `pull_request_state` as "the one caller of `#pull_request_from_gh`, which starts `gh`". Each agrees with `:588`, `:2237-2249` and the module docstring at `:132-134` (read). The evidence search, run again at the target outside `trail/rounds/`, prints `changelog.md:3` alone, as the close says (executed).

What matched: the method account in the close of round 1 finding 5, for the tree-wide search. `git grep -n -i -e 'seal gate' -e 'preflight' -e 'broad run' -e 'broad gate' -- ':!seal/threads'` prints 614 lines at both `adf2bf488` and the target. A diff of the two lists shows the two README rows, the moved and added lines of `gate-to-pull-request.md`, `parity-setup/SKILL.md:74`, the two `NETWORK_PLACES` lines, and one `CONTRIBUTING.md` line moved from `:217` to `:218` by the `:202` edit (executed). The close names all of them but the moved line. Its read of the records is finding 2.

What matched: the orchestrator's judgment, which the spawn prompt gave and no record holds, that `frame/design.md` *Scope* need not list what the fix pass changed, because a fold after a fix only narrows. `skills/implement/orchestration.md:84-87` says so. No *Scope* item claims to be the work's whole list, and the fold narrowed the two that did, S7 and item 3 (read). The fix pass added no unit. A sentence rewritten in an existing section and an entry changed in a test module's tuple each add none, by `skills/implement/fix-pass.md` *A fix that needs a unit the frame does not name waits for the fold* (read). The one exception is the `## Removes` row, finding 2. The judgment stands in no row of `frame/plan.md` *Judgments of the run*. `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* has whoever judges write it down there, so the row is the orchestrator's to write.

What matched: the orchestrator's `gaps.md` sentence of `540c757fa`. #1630 is open and labelled `from-review` (executed: `gh issue view 1630 --json number,title,labels,state`). The sentence's account of the drain step matches `skills/implement/orchestration.md:530-537` (read), and its account of the refusal matches `chain_check.py#follows` (carried). This work's `gaps.md` holds no row that the drain step would move (read).

What matched: the framer's fold `adf2bf488` and its *Judgments of the run* row. The row dates the decision, gives its grounds, and names `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* and `skills/implement/fold-and-reframe.md`. The S6 and S7 cells read as round 1's paste-ready cells (read).

What matched: the release's other items. #1624, #1628 and #1629 name no file the fix diff changes (executed: `gh issue view` on each), and no branch names their numbers (executed: `git branch -a`). `frame/plan.md` *Overlap with the release* still holds.

What matched: the fix diff adds no test case and no new name. `chain_check.py --worktree` at the target, before this record was written, printed no pin or copy notice at a line of `frame/design.md` (executed, `## Probes`).

What matched: the label. `gaps.md:7` leaves the broad gate `unverified` and names the orchestrator as its answerer. That is honest: this round ran six modules and nothing broad.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the target: the full suite and the repository-wide lint, which no agent runs (contract rule 2). Findings 1 and 2 are open. Finding 1 is in a test module, so its fix pass is followed by a verifying round, and the broad run and the sealer's spawn come after that | `seal gate --base origin/release/v0.39.2 --record seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed` | the orchestrator |
| Whether the fix pass's hand-back named the `## Removes` row of finding 2, and, where it did, why no fold followed | the fix pass's hand-back, which no record holds | the orchestrator |
| The fix pass's narrow set, `3627 passed` (`round-1.md:175`), read and not run | `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/trail/rounds/round-1.md:175` | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:xdist tests/behaviour/test_chain_hooks_hardening.py -k test_the_places_that_reach_the_network_are_named`, in the clone at `540c757fa` | exit 0, 1 passed |
| `README.md:409` and `README.ko.md:406` set back in the clone to their text at `15e831a0e` with the `Edit` tool; `git diff --quiet 15e831a0e -- README.md README.ko.md`; the same `bin/test` command | `git diff` exit 0; test exit 0, 1 passed. The two rows were restored with the `Edit` tool, and `git status --short` in the clone printed nothing |
| `awk` over each README edition's passage, from "No hook reaches a network." and "훅은 모두 네트워크를 타지 않습니다." to the next heading, into `grep -c -e '--sealing' -e '--worktree'`, with the old rows in place | 0 for each edition |
| `bin/test -q tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/text/test_the_rules_have_one_owner.py tests/skills/test_passages.py`, in the clone at `540c757fa` | exit 0, 146 passed |
| `python3 skills/code-review/scripts/chain_check.py --baseline e65830869 --root <the branch worktree> --worktree`, before this record was written | exit 0. The state line is the unseen one, and `gh pr view` found no pull request. Five lines on `round-1.md` say a verifying round is owed, one for each closed finding, and one says the last `target:` is behind HEAD at `acf0a786f`. Notices say git carries no `trail/gate.md` and no `guarantee.md`. No pin or copy notice appears |

# Review round 1: 1795736973-the-preflight-passes-where-a-round-is-owed

```seal
target: 15e831a0e against origin/release/v0.39.2
```

The base is `origin/release/v0.39.2` at `e65830869`. No earlier round exists, so no fact is carried from one; every fact below was established at `15e831a0e` in a `git clone --no-local` under this round's scratch directory, or read in the branch worktree at the same commit.

The code change holds to the frame, and its cases pin it (`## Confirmations`). The findings below are statements that the change made false and that the build's search did not reach, plus one instruction the new preflight sentence leaves without an act that answers it.

## Findings

### 1. The README editions say `seal gate` asks `gh` for the pull request's state, which its run no longer does

```seal
severity: should
location: `README.md:409`, `README.ko.md:406`, `tests/behaviour/test_chain_hooks_hardening.py:426-433`
evidence: executed `git grep -n -i -e 'gh pr view' -e 'isDraft' -- README.md README.ko.md CONTRIBUTING.md docs skills agents templates ':!skills/code-review/scripts'`; read `skills/code-review/scripts/chain_check.py:2237-2249`, `skills/verify/scripts/broad_gate.py:2042-2050`, `tests/behaviour/test_chain_hooks_hardening.py:426-469`
```

Why it matters: the README table under *What runs on your machine* lists each place the plugin reaches a network. A person reads it to learn what reaches their repository through their own `gh` login. `README.md:409` says that `seal gate` sends `gh pr view --json isDraft`, "asked by its `chain_check.py` step", on "each run outside GitHub Actions". `README.ko.md:406` says the same in Korean. At the target, the gate's chain arm always passes `--sealing` (`broad_gate.py:2046-2050`). Under that flag `chain_check.py#_checked` does not call `pull_request_state` (`chain_check.py:2237-2239`), and that function is the only caller of `pull_request_from_gh`. So the gate run asks `gh` nothing. The row now names a network call the gate does not make. The call it describes is still made by `chain_check.py` run without the flag, which is what the orchestrator's and the proofer's `--worktree` reads run. That step is a place the table owes.

`tests/behaviour/test_chain_hooks_hardening.py#NETWORK_PLACES` lists `"seal gate"` as a place that reaches the network, and `test_the_places_that_reach_the_network_are_named` requires both passages to name it. That list states the same stale fact, so the fix changes it too. The search above printed `CONTRIBUTING.md:202` too. That line says `chain_check.py` asks `gh` where no event payload exists, which stays true of a run without the flag, so the fix leaves it. The search is a sample under contract rules 12 and 19, since a statement in other words escapes it.

`README.md:409`, the row replaced whole:

```markdown
| `chain_check.py` run without `--sealing`, as the orchestrator's and the proofer's `--worktree` reads run it ([`skills/code-review/scripts/chain_check.py`](skills/code-review/scripts/chain_check.py)) | your repository's pull request, through your `gh` login | `gh pr view --json isDraft`, to learn whether the branch's pull request is a draft. The run `seal gate` makes passes `--sealing`, reads no pull request's state, and asks `gh` nothing | each such run outside GitHub Actions, where `gh` is on the PATH |
```

`README.ko.md:406`, the row replaced whole:

```markdown
| `--sealing` 없이 돌리는 `chain_check.py`, 곧 orchestrator 와 proofer 가 `--worktree` 로 읽는 실행 ([`skills/code-review/scripts/chain_check.py`](skills/code-review/scripts/chain_check.py)) | 사용자 저장소의 pull request. 사용자의 `gh` 로그인으로 닿는다 | `gh pr view --json isDraft` 로 브랜치의 pull request 가 draft 인지 묻는다. `seal gate` 가 하는 실행은 `--sealing` 을 넘기므로 pull request 의 상태를 읽지 않고 `gh` 에 아무것도 묻지 않는다 | 그런 실행이 GitHub Actions 밖에서 돌 때마다. `gh` 가 PATH 에 없으면 묻지 않는다 |
```

`tests/behaviour/test_chain_hooks_hardening.py:429`:

```python
    "chain_check.py",
```

### 2. `skills/parity-setup/SKILL.md` tells the user the gate passes a round record without `original:` until a ready pull request is open

```seal
severity: should
location: `skills/parity-setup/SKILL.md:72-75`
evidence: read `skills/parity-setup/SKILL.md:60-78`, `skills/code-review/scripts/chain_check.py:2237-2239`, `skills/code-review/scripts/chain_check.py:2349-2358`; executed `git grep -n -i -e 'before then' -e 'once a ready pull request' -e 'ready pull request is open' -- skills agents docs templates lib README.md CONTRIBUTING.md`
```

Why it matters: step 7 of the parity setup has the agent tell the user what changes now. Under `shared, records only` it says that `seal gate` "refuses a round record without it once a ready pull request is open for the branch, and that before then it names the record and passes." At the target the gate's run is strict whatever the state (`chain_check.py:2237-2239`). In the original arm only the guarantee's line moves to the notices under `--sealing` (`chain_check.py:2355`). A round record's missing `original:` line therefore stays a problem and fails the gate's preflight and broad run before any pull request exists. The agent would tell the user the opposite of what the gate does, and the user would first meet the refusal at a preflight they were told passes. The search above printed only this sentence and, among the hits on "before then", `skills/implement/bootstrap.md:137`, which is about the `Broad gate` key and stays. The search is a sample.

```markdown
   shared, records only, no workflow reads a round record, but `seal gate`
   runs the same check: say that the `original:` line is still written, that
   the gate's preflight and broad run refuse a round record without it
   whatever the pull request's state, and that no workflow refuses it at the
   pull request.
```

### 3. The preflight's exit-1 instruction does not answer the refusal the new sentence names as its example

```seal
severity: should
location: `skills/code-review/gate-to-pull-request.md:179-187`
evidence: read `skills/code-review/gate-to-pull-request.md:174-197`, `skills/code-review/orchestration.md:143-158`
```

Why it matters: the paragraph **The preflight is yours, and it is not the broad gate** now says that a refusal on a record arm, "a verifying round owed among them", fails the preflight (`:179-182`). The next instruction says what to do on exit 1: "correct the record, commit, and run it again" (`:184-187`). A verifying round owed is not repaired by correcting a record. The act that answers it is the round itself, as `skills/code-review/orchestration.md:143-158` states for the same line of the check: where the output names a record with the words `chain_check.py#VERIFYING_ROUND` holds, "a round reads the pass, and the orchestrator spawns it". An orchestrator that follows the preflight paragraph as written has one act to take, an edit of the round record. Such an edit could turn a `fixed` close into another verdict, or otherwise quiet the line, and the invariant *No fix that no round reads* is the one this work item exists to hold. Before this change the preflight never failed on that line, so the instruction was never reached for it. The diff is what makes the instruction reachable for it.

```markdown
its exit code directly and take the broad run only on 0. On 1 its
`PREFLIGHT FAILED` lines name each failing arm with its first lines and the
file holding the rest. Where a line names a round record with the words
`skills/code-review/scripts/chain_check.py#VERIFYING_ROUND` holds, spawn
the verifying round on the last fixes' diff, as
`skills/code-review/orchestration.md` *Orchestrator: the run ends with a
verifying round* states, commit its record, and run the preflight again.
On any other refusal, correct the record, commit, and run it again. On 2
it refused before anything ran, and
```

The wrap of the lines after it follows whatever `test_prose_stays_within_the_wrap_limit` asks.

### 4. Four statements say the `--sealing` run reads no event payload, or that `pull_request_state` is the one reader of it, while the body arm still reads the payload

```seal
severity: should
location: `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/changelog.md:3`, `skills/code-review/scripts/chain_check.py:314-316`, `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/frame/design.md:61`, `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/trail/phases/phase-1.md:7`
evidence: read `skills/code-review/scripts/chain_check.py:2334`, `skills/code-review/scripts/chain_check.py:571-627`, `skills/code-review/scripts/chain_check.py:128-134`; executed `git grep -n -F -e 'payload and `gh` are not asked' -e 'reads the payload or starts' -e 'reads the event payload or starts' -e 'event payload nor `gh`' -- seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed skills tests`, and `grep -n 'GITHUB_EVENT_PATH' skills/code-review/scripts/chain_check.py`
```

Why it matters: `_checked` calls `pull_request_body()` under `--sealing` as well (`chain_check.py:2334`). That function opens the file `GITHUB_EVENT_PATH` names (`:611-616`), and the body arm prints what it found as notices. Three functions read that variable: `event_payload_present` (`:573`), `pull_request_state` (`:584`) and `pull_request_body` (`:611`). The flagged run skips only the first two. The module docstring states the bound correctly: "The run asks neither the event payload nor `gh` for the pull request's state" (`chain_check.py:132-133`). The four statements below drop that bound.

- `changelog.md:3`, which becomes the release note a person reads: "Under `--sealing` the check now reads no pull request's state, asks neither the event payload nor `gh`, and judges as at a ready pull request". Read as three acts, the second is false.
- The comment above `SEALING_JUDGED_SAYS` (`chain_check.py:314-316`): "the payload and `gh` are not asked".
- S6 of `frame/design.md:61`, a cell the orchestrator's fold `7be8b7bfc` wrote from the crafter's hand-back: "`chain_check.py#pull_request_state`, the one function that reads the payload or starts `gh`". The sealer reads this cell against the tree.
- `phase-1.md:7`: "`pull_request_state` is the one function that reads the event payload or starts `gh`, so a run that never calls it does neither".

The S6 claim itself holds. `pull_request_from_gh` is the one function that starts `gh` (`:635`), and only `pull_request_state` calls it. So a run that never calls `pull_request_state` starts no `gh`. That is what the case pins. The two records only overstate what the recorder proves. The search printed these four lines. It is a sample, since the fact can be stated in other words.

`changelog.md:3`, the sentence:

```markdown
Under `--sealing` the check now reads no pull request's state, asks neither the event payload nor `gh` for it, and judges as at a ready pull request, whatever the state.
```

`chain_check.py:314-316`:

```python
# The first line of a `--sealing` run, printed in place of the state line:
# the broad gate's run precedes the ready pull request CI judges, so it is
# judged as one, and neither the payload nor `gh` is asked for the state.
```

`frame/design.md:61`, the last cell:

```markdown
The `tests/skills/test_chain_check.py` case of *Scope* item 6, with a recorder on `chain_check.py#pull_request_state`, the one caller of `#pull_request_from_gh`, which starts `gh` |
```

`phase-1.md:7`, the sentence:

```markdown
`pull_request_state` is the one caller of `pull_request_from_gh`, which starts `gh`, so a run that never calls it starts no `gh` and reads no state from the payload.
```

### 5. The build's search for statements of the old judgment was a sample handed back as the whole list

```seal
severity: should
location: `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/frame/design.md:62`, `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/trail/phases/phase-1.md:9`
evidence: executed `git grep -n -e 'refuses only a ready' -e 'state as the check reads it' -e "is the check's to read" -e 'asks the records arm first' -- ':!seal/threads'` (no output), and the two searches on findings 1 and 2; read `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/frame/design.md:39-41`, `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/trail/phases/phase-1.md:9`
```

Why it matters: the frame titles S7 "No text states the old judgment for the gate" and verifies it with a search on four phrases, the four lines the framer had found. Commit `28512d9c1` says "the docstrings and comments that stated the old judgment are rewritten in place". Both are claims of a whole list. At the target the four-phrase search prints nothing, and findings 1 and 2 still state the old judgment. One says the gate asks `gh` for the state. The other says the gate passes before a ready pull request. The phase record's own search (`phase-1.md:9`) is labelled a sample, which is honest. Its pathspec, `tests skills lib docs`, still left out both README editions, where finding 1 stands.

The class is every text that says what the gate's chain arm asks, or when it refuses. One method that builds the list from what produces it is to list every text that names the gate or its runs, `git grep -n -i -e 'seal gate' -e 'preflight' -e 'broad run' -e 'broad gate' -- ':!seal/threads'`, and read each hit for a clause on the pull request's state, `gh`, a draft, or passing before a pull request. That is how this round reached findings 1 and 2. The list stays a sample, since the same fact can be stated without any of those names, and the phase record says so. The fix is to the method's record, not only to the two instances, which findings 1 and 2 carry.

`frame/design.md:62`, the row's first cell:

```markdown
| S7. The four statements of the old judgment the frame located are rewritten |
```

`trail/phases/phase-1.md`, a line added under the item at `:9`:

```markdown
- **The statements of the old judgment, enumerated by the texts that name the gate (executed).** `git grep -n -i -e 'seal gate' -e 'preflight' -e 'broad run' -e 'broad gate' -- ':!seal/threads'`, each hit read for a clause on the pull request's state, `gh`, a draft, or passing before a pull request, found `README.md:409`, `README.ko.md:406` and `skills/parity-setup/SKILL.md:72-75` beyond the frame's four lines. The list is a sample: a statement of the fact that names none of the four is not reached.
```

## Confirmations

What matched: *Scope* item 1. `chain_check.py#_checked` sets `strict = True` and prints `SEALING_JUDGED_SAYS` under `--sealing`, and calls `pull_request_state` only without the flag (`skills/code-review/scripts/chain_check.py:2237-2249`, read). Both returns use that `strict`, the early return for a branch that declares nothing (`:2268-2273`) and the last one (`:2360-2364`) (read). The four arms the flag already printed still move to the notices: the broad gate and guarantee arms (`:2328-2333`), the body arm (`:2341-2344`) and the guarantee's `original:` line (`:2355-2356`) (read). No later line of `_checked` reads `state`, `where` or `unseen`, which the flagged branch leaves unset (executed: a search of `:2250-2400` for the three names printed nothing).

What matched: the orchestrator asked whether every caller of `chain_check.py --sealing` agrees with the new judgment. `git grep -n -e '--sealing' -e '\.SEALING\b' -e 'args.sealing'` outside `seal/threads/` names `broad_gate.py#gate` as the one caller that passes the flag (executed). `.github/workflows/hygiene.yml:120-121` and `templates/setup/hygiene.yml:87-88` pass only `--baseline` (read), so CI's judgment is unchanged, as S4 says. The loaders `seal_stamp.py`, `pr_body.py`, `release_seal.py` and `finding_counts.py` do not call `_checked` with the flag (executed, the same search).

What matched: the orchestrator asked whether any arm that only a record written after the gate can satisfy is left failing. This round walked the nine arms of the module docstring (`chain_check.py:9-91`, read) against what exists when the preflight runs. The trailer, declaration, frame and rule-changes arms read records and commits that exist before the gate. The records arm admits commits after the last `target:` that touch only the work item's directory (`chain_check.py#follows`, `:1003-1029`, read). `trail/gate.md`, `pr.md`, the body file's records and `guarantee.md` are written there, so none of them fails that arm. A round record's `original:` line is written by the round, before the gate. The arms that read `trail/gate.md`, `guarantee.md`, the guarantee's `original:` line and the body are the four the flag prints. None is left failing.

What matched: *Scope* item 2 and S6. The constant reads as `phase-1.md:6` quotes it (`chain_check.py:314-320`, read). `Test_main::test_refuses_a_verifying_round_owed_under_sealing_whatever_the_state` pins its text and its place as the first line, asserts `UNSEEN_SAYS` is absent, and holds the recorder on `pull_request_state` (`tests/skills/test_chain_check.py:4686-4726`, read).

What matched: contract rule 15 for the new and rewritten cases. In the clone, `if args.sealing:` at `chain_check.py:2237` was changed to `if False:`. The two new chain cases, the rewritten `test_accepts_a_draft_or_an_unseen_pull_request_with_a_notice` and the new gate case then failed, each at its exit assertion: `assert code == 1` three times and `assert gate.gate(...) == 1` once. The line was restored and the clone left clean (executed, `## Probes`). This re-establishes one of the six mutations `phase-1.md:11` claims; the other five were read, not run.

What matched: the two modules the plan's row names pass narrowly at the target (executed, `## Probes`). `test_the_fixture_branch_passes` is among them, which S5 names. So Q1's answer in `frame/questions.md:13`, that no fixture refuses, holds for these modules. The suite beyond them is `## Not judged`.

What matched: each new test against its group. The gate case is the only preflight case whose chain arm refuses a records problem with no payload. The chain case adds the draft state, the state line and the unasked state to what the rewritten case pins. `bin/seal layout --pairs` names neither file's new cases (executed).

What matched: S7's search prints nothing at the target (executed). The four lines it named at `a1cae2026` are rewritten at `skills/code-review/gate-to-pull-request.md:156`, `skills/core/SKILL.md:117-123`, `skills/verify/scripts/broad_gate.py:26-30` and `:2042-2045` (read). Finding 5 is about what the search does not reach.

What matched: `skills/core/SKILL.md:117-123` says the gate's run holds the first two rows before the pull request and prints the last two. In local mode it says the sealer and the orchestrator hold all four. Two readings bear that out. At a local root `trailer_findings` turns every work item's trailer into a notice (`chain_check.py:2054-2068`, read). The tree holds no committed declaration there, so the check judges no work item.

What matched: the rule change. Its `from` is the text of `docs/checks/the-pull-request-check.md:17-19` (read). `chain_check.py --worktree` at the target prints no refusal and no pin or copy notice on `frame/design.md` (executed, `## Probes`). Two other unsettled designs change the same section. `1794383426-eval-code-the-verdict-does-not-read/frame/design.md:76-92` changes the paragraph on the readers outside the check. `1794530293-three-compatibility-paths-still-stand/frame/design.md:218-222` removes the `parity.md` sentence. Neither touches the sentence this work's `to` extends (read). The other sections the records cite appear in no other `## Rule changes` with an edit that meets this work's sentences (executed: `grep -n -F` on each cited heading over `seal/threads/*/frame/design.md`).

What matched: the orchestrator's two commits after the build. `7be8b7bfc` dates the routing statement to `a1cae2026`, and the base code at that commit gives that judgment. It adds the `tests/conftest.py` comment to *Scope* item 3, which the diff changed (`tests/conftest.py:342-344`). It rewrites *Scope* item 5 to the wording the document holds (`gate-to-pull-request.md:179-183`), S6 to the recorder the case holds, and Q1's Status to the phase record's answer (read). `15e831a0e` adds `pr.md`. Its two quotes are the sentences of `frame/plan.md:44` with the closing period left out, and its closing line and attribution follow the earlier work items' `pr.md` (read).

What matched: the label. `gaps.md:7` leaves the broad gate `unverified` with the orchestrator as its answerer, which is honest, since this round ran two modules and nothing broad. `gaps.md:11` holds the `docs/` rule in `## Rule changes` for the settle, as `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* has it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the target: the full suite and the repository-wide lint, which no agent runs (contract rule 2). Once findings 1 to 5 are closed and a verifying round leaves nothing open, the orchestrator's broad run comes due, and the sealer's spawn after it | `seal gate --base origin/release/v0.39.2 --record seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed` | the orchestrator |
| A drain row homed in `seal/follow-up.md` fails the records arm. This was already so at the ready pull request, and the gate's preflight now meets it first. `skills/implement/orchestration.md:531-542` has the orchestrator move a row to `seal/follow-up.md` after the last round and before `seal gate --preflight`. `chain_check.py#follows` (`:1003-1029`) admits only the work item's directory after the last `target:` commit, and `seal/follow-up.md` is outside it. The fault predates this diff and is outside it. Whether it owes an issue is not this round's to decide | `skills/implement/orchestration.md:531-542`, `skills/code-review/scripts/chain_check.py:1003-1029` | the orchestrator |
| Five of the six mutations `phase-1.md:11` names, and the boundary set's `3079 passed` at `ea37e1908` (`phase-1.md:14`), which this round read and did not run | `seal/threads/1795736973-the-preflight-passes-where-a-round-is-owed/trail/phases/phase-1.md:11-14` | the orchestrator's broad run, for the suite |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/skills/test_chain_check.py`, in the clone at `15e831a0e` | exit 0, 262 passed |
| `bin/test -q tests/skills/test_broad_gate.py`, in the clone at `15e831a0e` | exit 0, 203 passed, 1 skipped |
| `chain_check.py:2237` changed in the clone from `if args.sealing:` to `if False:` through the `Edit` tool, then `bin/test -q -p no:xdist tests/skills/test_chain_check.py tests/skills/test_broad_gate.py -k "verifying_round_owed_under_sealing or test_accepts_a_draft_or_an_unseen_pull_request_with_a_notice or preflight_where_a_verifying_round_is_owed"` | exit 1, 4 failed: the rewritten case and both runs of the new chain case at `assert code == 1`, the gate case at `assert gate.gate(namespace(repo, keep, preflight=True)) == 1`; the line was restored and `git status --short` in the clone printed nothing |
| `bin/seal layout --pairs`, in the clone | exit 0; no pair names `tests/skills/test_chain_check.py` or `tests/skills/test_broad_gate.py` |
| `python3 skills/code-review/scripts/chain_check.py --baseline e65830869 --root <the branch worktree> --worktree`, before this record was written | exit 0; the unseen state line, and notices that `trail/rounds/` holds no record and that git carries no `trail/gate.md` and no `guarantee.md`; no rule-changes refusal and no pin or copy notice |

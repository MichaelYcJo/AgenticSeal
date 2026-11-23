# Review round 4: 1795406406-code-stands-on-facts-that-no-longer-hold

```seal
target: 0de0f2f00, fixes 61c1042ea..0de0f2f00
```

This is the verifying round after round 3's fix pass. The range `61c1042ea..0de0f2f00` holds five commits. `28fcacb6f` commits round 3's record. `8fd693b26` is the fix of round 3's finding: it changes `skills/code-review/scripts/chain_check.py`, `tests/skills/test_chain_check.py` and this work item's `changelog.md`. `2fd26e1ae` appends the close block to `trail/rounds/round-3.md`. `24cf05d80` gives the "passes" statements the trailer condition: `skills/implement/scripts/seal.py`, `templates/setup/hygiene.yml`, `tests/skills/test_seal.py` and `changelog.md`. `0de0f2f00` rewrites the `to` of the two `## Rule changes` operations on *Shared or local* in `frame/design.md` (executed: `git diff --stat 61c1042ea 0de0f2f00`, and the diff read whole). The round worked in a `git clone --no-local` of the branch worktree, checked out at `0de0f2f00`, under `<scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-4/clone`. The work item's records were read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` to `phase-5.md`, and `trail/rounds/round-1.md` to `round-3.md`. Of these, only `changelog.md`, `frame/design.md` and `round-3.md` changed in the range (executed: `git diff --stat 61c1042ea 0de0f2f00 -- seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold`). No `pr.<lang>.md` stands, and none is owed, because `Commit and pull request language` is English. No `seal/parity.json` is declared.

Carried from round 3 and not established again: the merge of the base at `61c1042ea` and the acceptance searches of `frame/design.md` S4, S5, S7, S9, S14 and S15. The range changes no file those searches read except `chain_check.py` and `seal.py`, and it adds no name they search for (read: the diff). The parse of `## Rule changes` was not carried, because `0de0f2f00` changed two `to` texts: the `chain_check.py --worktree` run below reads the design through the rule-changes arm and reports no unread line and no refusal.

The orchestrator's prompt asked this round to read every no-root and left-workflow statement the work now makes against what the check prints in each state, and not against each other. The probe `test_tmp_round4_states.py` ran the target's `chain_check.py` and `seal.py mode --check` in nine runs. Each repository had commits whose author is their committer, and the CI runs set `GITHUB_HEAD_REF` and a ready or draft event payload:

| Run | State | Exit | What the check printed |
|---|---|---|---|
| 1a | left workflow in CI: the switch merged, no root in the tree, none local; commit with no trailer | 0 | "declared neither way, so the review-chain check judged the commit trailers and nothing else", and no commit line |
| 1b | as 1a; trailer `no work item` | 0 | the same notice, then `NO_WORK_ITEM_TRAILER` |
| 1c | as 1a; trailer `some-item`, ready | 1 | the same notice, then `UNDECLARED_TRAILER` |
| 1d | as 1c, draft | 0 | the same lines, as notices |
| 1e | as 1c, committer email differs from author email | 0 | the notice alone; the commit is not judged |
| 1f | `seal.py mode --check` in 1e's repository | 0 | "no seal/ here, so nothing is declared and nothing can disagree." |
| 2a | the switching pull request in CI: a commit before the switch with trailer `some-item`, then the commit that takes `seal/` out | 1 | "declared neither way", then `UNDECLARED_TRAILER` for the earlier commit |
| 2b | 2a's repository from the switching session's clone, root under `.git/seal`, `--worktree` | 0 | the local-root notice with `PRINTED_TRAILERS`, then `LOCAL_TRAILER` |
| 3a | a local-mode clone, `--worktree`, ready payload, trailer `some-item` | 0 | the local-root notice with `PRINTED_TRAILERS`, then `LOCAL_TRAILER` |

In 2a the declaration was added on the branch, so the diff deletes none and `ROOT_LEFT_SAYS` is not printed. Where the declarations stood at the merge base, `_checked` prints `ROOT_LEFT_SAYS` (`chain_check.py:2159-2186`, read), and `test_accepts_every_declaration_leaving_with_the_root` and `test_a_root_that_left_for_a_local_root_says_the_check_judged_nothing` hold its two forms. Both passed in the narrow run below.

The statements, each read against those runs:

- `templates/setup/hygiene.yml:17-23` says the review-chain step judges the commit trailers alone, that every step passes the commits a local-mode session writes, and that a commit made before the switch whose trailer names a work item still fails a ready pull request. Runs 1a, 1c, 1f and 2a bear it out.
- `seal.py#left_workflow_line` (`:1739-1745`) and its docstring (`:1728-1735`) say the same. Runs 1a and 1c bear it out, and `tests/skills/test_seal.py:2744-2750` pins the printed line.
- `seal.py#remove_workflow`'s docstring (`:1856-1864`) states the same premise. Its conclusion at `:1864-1867` is finding 1. Its coordinate at `:1861` is finding 2.
- `seal.py#mode`'s comment (`:2428-2432`) says the left workflow's review-chain step reads no routing declaration. Runs 1a to 1e bear that out, and its coordinate is finding 2.
- `changelog.md:4` describes each of the texts above, and the local-root notices, as runs 1a, 1c, 2b and 3a show them.
- The `## Rule changes` operation on `docs/layout/one-root-by-lifetime.md` *Shared or local* (`frame/design.md:160-166`) says the workflow reads nothing as declared and judges the commit trailers alone. It passes the commits a local-mode session writes and fails a ready pull request on a commit made before the switch that names a work item. Runs 1a, 1c and 2a bear it out. Its Korean edition (`:174-179`) renders each clause, the draft and committer conditions left out in both.

"Commits a local-mode session writes carry no `Seal-Routing` trailer" rests on `docs/checks/the-routing-check.md:31-33` and `skills/commit-pr-convention/SKILL.md:195` (read), not on a run. "Fails a ready pull request" holds for a commit committed by its author (run 1e). `docs/checks/the-routing-check.md` *At the pull request* states that bound, and the three texts that cite or follow it summarise the rule rather than restate it, so no finding stands on the omission.

## Findings

### 1. `remove_workflow`'s docstring now says the left workflow fails a ready pull request on an earlier commit's trailer, and still concludes that removing it is never a repair

```seal
severity: should
location: `skills/implement/scripts/seal.py:1864-1867`
evidence: executed `python3 -I <scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-4/test_tmp_round4_states.py <clone> <scratch>` (runs 1c and 2a), `git grep -n -i -e 'never a repair' -e "person's choice" -e 'not a repair' -- ':!seal/threads' ':!evals'`, `git log -S'never a repair' -- skills/implement/scripts/seal.py`; read `skills/implement/scripts/seal.py:1724-1758`, `skills/implement/scripts/seal.py:1853-1867`, `skills/code-review/scripts/chain_check.py:1945-1949`, `docs/checks/the-routing-check.md:42-56`
```

Why it matters: `24cf05d80` rewrote the premise of the docstring's last sentence and left its conclusion. The docstring now says, at `:1862-1864`, that "a commit made before the switch whose trailer names a work item still fails a ready pull request there". The next sentence, at `:1864-1865`, still reads: "So there the removal is the person's choice and never a repair". Run 1c is that pull request: the left workflow at this release exits 1 on it. The check's own message offers two ways out: "commit its `routing.md`, naming this branch, or correct the trailer" (`UNDECLARED_TRAILER`, `chain_check.py:1945-1949`). In local mode nothing under the root is committed, so the first is not open. `seal pr-checks remove` is the plugin's other way out, the one `left_workflow_line` names for an older pin (`:1754-1757`). So for that pull request the removal is a repair, and the docstring says it never is.

The sentence came in with #1034 (`2974871d`, executed: `git log -S`), when the premise said every step examines nothing and passes. Phase 3 rewrote the premise for *Scope* item 2 and kept the conclusion. So did the fix of round 1's finding 3. `24cf05d80` then gave the premise the condition the runs found and left the conclusion that stood on the old premise. That breaks `skills/agent-contract/SKILL.md` rule 19, and it is the defect this work item's issue names. An agent that reads the docstring to decide whether to offer `seal pr-checks remove` on a failing pull request in local mode is told it is not a repair there, so the severity is `should`. The defect is in a unit phase 3 made, so the finding takes neither a `regression:` nor a `reopens:` line.

The search found no other statement of the conclusion: `never a repair` and `person's choice` match only `:1865` outside `seal/threads/` and `evals/` (executed). The snippet below rewrites the docstring from `:1864` to `:1867`. Finding 2 rewrites `:1859-1862` and does not overlap it.

```python
# skills/implement/scripts/seal.py, remove_workflow's docstring, :1864-1867
    (`docs/checks/the-routing-check.md` *At the pull request*). So there the
    removal is the person's choice, except on a pull request such a commit
    fails, where correcting the trailer is the repair the check names and
    the removal is the other way out. Pinned to an older release, it is the
    way out of a workflow that fails every pull request (`left_workflow_line`).
```

### 2. Two texts of `seal.py` cite `ROOT_LEFT_SAYS` for what the left workflow's review-chain step reads, a message no pull request after the switch prints

```seal
severity: should
location: `skills/implement/scripts/seal.py:1859-1862`, `skills/implement/scripts/seal.py:2428-2432`
evidence: executed `python3 -I <scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-4/test_tmp_round4_states.py <clone> <scratch>` (runs 1a to 1e and 2a), `git grep -n ROOT_LEFT_SAYS`; read `skills/code-review/scripts/chain_check.py:1887-1925`, `skills/code-review/scripts/chain_check.py:1933-1939`, `skills/code-review/scripts/chain_check.py:2159-2186`, `docs/checks/the-pull-request-check.md:136-144`, `seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold/trail/phases/phase-3.md:85`, `seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold/trail/rounds/round-1.md:114`, `seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold/trail/rounds/round-2.md:22-31`
```

Why it matters: `remove_workflow`'s docstring says `chain_check.py` "reads no routing declaration where the tree holds no root and judges the commit trailers alone", and it cites `chain_check.py#ROOT_LEFT_SAYS` for that (`:1859-1861`). `#mode`'s comment cites the same constant for the left workflow's review-chain step (`:2431`). Phase 3, which wrote both texts, calls the constant "the message the review-chain step prints when the tree has no root" (`trail/phases/phase-3.md:85`). The runs say otherwise. In runs 1a to 1e, the pull requests that follow the switch, the tree has no root and the check prints the shared return of `declared_for_this_branch`, "this pull request declared neither way, so the review-chain check judged the commit trailers and nothing else" (`chain_check.py:1919-1924`). `_checked` prints `ROOT_LEFT_SAYS` only where the pull request's own diff deletes declarations that stood at its merge base (`:2159-2186`). That happens on the switching pull request alone, and in run 2a not even there. Since `8fd693b26` the constant also holds no fixed words: it ends in `{trailers}`, which `_checked` fills with `JUDGED_TRAILERS` or `PRINTED_TRAILERS` (`:1933-1939`, `:2183-2186`).

This coordinate has already cost the review chain a round. Round 1's fix pass applied its fix "as read against `seal.py#remove_workflow`, `#mode`'s `--check` branch and `chain_check.py#ROOT_LEFT_SAYS`" (`round-1.md:114`). It missed the two notices of `declared_for_this_branch`. Round 2 reopened the finding on them (`round-2.md:22-31`), and round 3 found the regression the fix made there. An agent that next edits what the left workflow says follows the same citation to the same constant, so the severity is `should`. The defect is in two units phase 3 made, so the finding takes neither a `regression:` nor a `reopens:` line.

The coordinate that holds for every pull request with no root in the tree is the rule, not a message. `docs/checks/the-pull-request-check.md` *What the check reads at the pull request* says, over `check: nothing-declared-nothing-owed`, that where the tree has no top-level `seal` entry the check reads nothing as declared and "judges the trailers as for any pull request that declares nothing" (`:136-144`). `git grep -n ROOT_LEFT_SAYS` lists the constant, its one use, and these two citations, so the snippets reach every citation of it. Phase 3's sentence and `trail/phases/phase-4.md:121` are records of what their phases did, and the snippets leave them as written.

```python
# skills/implement/scripts/seal.py, remove_workflow's docstring, :1859-1862
    `Seal-Routing` trailer: `chain_check.py` reads no routing declaration
    where the tree holds no root and judges the commit trailers alone
    (`docs/checks/the-pull-request-check.md` *What the check reads at the
    pull request*), and `mode --check` finds no root to disagree with. A
    commit made before the switch whose trailer names a
```

```python
# skills/implement/scripts/seal.py, #mode's --check branch, :2428-2432
            # A check that fails where there is nothing to check teaches
            # people to delete the check. A workflow pinned to this release
            # that outlived its root reads no routing declaration in its
            # review-chain step either (`docs/checks/the-pull-request-check.md`
            # *What the check reads at the pull request*), and this one has
            # nothing to add to that.
```

## Confirmations

```seal
confirms: round-3#1
```
What holds: at a local root the review-chain check now says it judged nothing, beside trailer lines that agree with it. In runs 2b and 3a the local-root return of `declared_for_this_branch` printed "the review-chain check judged nothing: at a local root each commit's `Seal-Routing` trailer is printed, not judged". Each work item's trailer followed as `LOCAL_TRAILER`, and the check exited 0. In runs 1a to 1e and 2a, with no local root, the shared return printed `JUDGED_TRAILERS`, and the trailers were judged (executed). `_checked` reads `local_root` once and passes the one answer to `ROOT_LEFT_SAYS` and to `trailer_findings` (`chain_check.py:2183-2186`, `:2209`, read). The CI and the local form of `ROOT_LEFT_SAYS` are held by `test_accepts_every_declaration_leaving_with_the_root` and the new `test_a_root_that_left_for_a_local_root_says_the_check_judged_nothing`, and both passed. The new case holds a state its neighbour does not, a local root, so it covers something its group did not. The renamed `test_local_mode_says_the_check_judged_nothing` holds the local return's words. `test_the_shared_sentence_says_what_it_searched_and_for_what` holds the shared return's. The changelog's sentence on these notices (`changelog.md:4`) says what the runs print.

What matched: the fix pass claimed that six runs of five states printed each notice beside trailer lines that agree with it, and that the left-workflow run exited 1 on a commit whose trailer names a work item. This round's nine runs agree on every state the claim names (executed). The claim that the new and renamed cases were seen red against the old notices follows from the diff: each asserts words the old code did not print (read). The mutations under `seal mutate` were not run again here.

What matched: the fact that the new "fails a ready pull request" sentences state was already held by a case. The `undeclared` fixture of `tests/skills/test_chain_check.py:3811-3820` is a repository with no root in the tree and none local, the left-workflow state. `test_refuses_a_commit_naming_a_work_item_no_declaration_names` (`:3825-3859`) asserts exit 1 on a ready pull request for a commit naming a work item, a notice for `no work item`, nothing for a commit with no trailer, and exit 0 on a draft (read). So the statements add no behaviour that a case does not hold.

What matched: the records read whole state nothing else that the target contradicts. The quotes of `pr.md` stand word for word, runs of whitespace collapsed, at `frame/plan.md` *Judgments of the run*: the title row's Judgment cell, and the gate row's Judgment cell (executed: a comparison of each quote against `plan.md`). `trail/phases/phase-3.md:85` is weighed under finding 2.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the target: the full suite, the repository-wide lint and the format check (`Broad gate` of `seal/config.json`). The suite stays `unverified` (contract rule 2) | `seal/config.json` | the orchestrator's broad run, after findings 1 and 2 are closed |
| The close-issues workflow without the label step, on a push to `main` | `.github/workflows/close-issues-on-release.yml` | the close-issues run when this release reaches `main`, read by the repository owner (`gaps.md`) |
| The mutations of `8fd693b26`'s cases under `seal mutate`, which the fix pass reports and this round did not run again | `tests/skills/test_chain_check.py:3701-3714`, `tests/skills/test_chain_check.py:4810-4831` | the sealer, from the fix pass's account |

## Probes

| Command | Result |
|---|---|
| `python3 -I <scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-4/test_tmp_round4_states.py <clone> <scratch>`: the nine runs of the table above, at `0de0f2f00` | exits as the table gives: 1c and 2a exit 1, every other run exits 0; the printed lines are the ones the table names |
| `bin/test -q tests/skills/test_chain_check.py tests/skills/test_seal.py` at `0de0f2f00` | 645 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over `chain_check.py`, `seal.py`, `tests/skills/test_chain_check.py` and `tests/skills/test_seal.py` | both exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline 459116a4e --root <the branch worktree> --worktree`, run on this record before hand-back | exit 0 on an unknown pull request state; it names findings 1 and 2 as open, with no close block, and names the gate record and the guarantee as not yet written; the rule-changes arm reads the design with no refusal, and no notice at a line of the design names a pin or a copy |

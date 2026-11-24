# Review round 2: 1795499830-the-orchestrator-asks-under-automation-yes

```seal
target: 61513fa00, fixes 0305f5e73..61513fa00
```

This is the verifying round over round 1's fixes. The code read is the diff `0305f5e73..61513fa00`. It holds the fix pass's commits `7a7febdb4`, `992ad7670`, `94ece093e` and `61025f3d4`, the framer's fold `c35d7f384`, and the close blocks in `87e164afe`. It also holds the orchestrator's three commits: `0b65dda2e` folds *Scope* item 2, and `c8777b6e9` and `61513fa00` repair `pr.md`. Outside that bound, each of the work item's records was read whole at `61513fa00`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, both phase records and `trail/rounds/round-1.md`. `seal/config.json` names English for both language keys, so no `pr.<lang>.md` is owed. `seal/parity.json` is not declared, so no parity comparison was owed.

Carried from round 1 as coordinates and not re-established here, since the fix diff does not touch them: the fail-toward-allow paths of `hooks/ask-under-automation.py#main` and its `__main__` block, the `STATED` and `NEAR` patterns, *Scope* item 7's three passages against #1608's *Done when*, the S10 and S11 searches, and the phase 1 mutation rows. `frame/questions.md` Q1, the orchestrator's measurement that the main session honours the deny, is carried as well. Re-established here: each of the three closes, with round 1's `evidence: executed` lines run again; the fold of *Scope* item 2; every quote in `pr.md`; the two new judgment rows of `frame/plan.md`; and the `gaps.md` diff.

## Findings

### 1. S1's pin of the sentence on what ends the refusal leaves out its condition, and the close calls the pin whole

```seal
severity: should
location: `tests/hooks/test_ask_under_automation.py:121-127`, `hooks/ask-under-automation.py:138-141`
evidence: executed `bin/seal mutate hooks/ask-under-automation.py --replace 'Where its run has ended, checking out ' 'Now, checking out ' --tests "bin/test tests/hooks/test_ask_under_automation.py -q -p no:xdist"` in the round's clone, which read SURVIVED; read `tests/hooks/test_ask_under_automation.py:111-128`, `hooks/ask-under-automation.py:136-141`
regression: round-1#2
```

Why it matters: the unit is S1's case, `test_refuses_a_question_under_automation_yes_with_the_rule`, which `992ad7670` and `94ece093e` changed. *Scope* item 2, as `0b65dda2e` folds it, says the reason holds a sentence that "where its run has ended", checking out another branch or removing the worktree ends the refusal. The fix pass pinned that sentence from "checking out another branch" onward and left the condition out, so the defect came from the pin's starting point and not from the frame.

The close of round 1 finding 2 says that "S1 pins both sentences, the second whole in `94ece093e`", and that commit's title says "S1 pins the whole sentence on what ends the refusal". Claimed: the whole sentence is pinned. Found: the `ends` string at `tests/hooks/test_ask_under_automation.py:122-126` opens at "checking out another branch", and the sentence at `hooks/ask-under-automation.py:139` opens with "Where its run has ended,". This round replaced that clause with "Now," and the hook's whole module passed, 11 cases. The condition matters to the session that reads the refusal. Without it, the reason tells an orchestrator whose run is still going on to check out another branch in its own worktree, which is advice that ends that run's protection. The first sentence's pin at line 121 also stops at "is checked out" and leaves out "in a worktree of this repository", so a reason that says "checked out here" would pass too.

This is a gap in a case that holds a fact the frame states, so it is a `should` under contract rule 14. The fix pins both sentences whole. The fix pass shows the new pin red with only the condition removed, as this round's mutation did (contract rule 15). It also corrects "the second whole" in its close. The S1 docstring at lines 114 to 116 stays true.

```python
        # in test_refuses_a_question_under_automation_yes_with_the_rule (S1),
        # in place of the assertion at line 121 and the `ends` pin at 122-127
        opened = (
            "A work item counts as open while its branch is checked out in a "
            "worktree of this repository."
        )
        ends = (
            "Where its run has ended, checking out another branch in that "
            "worktree, or removing the worktree, ends this refusal, and that "
            "work item's records take nothing from this call."
        )
        assert opened in reason, reason
        assert ends in reason, reason
```

### 2. The close of finding 3 hands the settle a change that no record the settle reads carries

```seal
severity: should
location: `seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/gaps.md:3-11`, `skills/implement/orchestration.md:304-317`
evidence: read `seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/trail/rounds/round-1.md:136`, `seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/frame/design.md:15`, `seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/frame/design.md:147`, `skills/implement/orchestration.md:304-317`, the settle skill's step 6 in the installed plugin
regression: round-1#3
```

Why it matters: the unit is the work item's `gaps.md`, which the fix pass changed in `61025f3d4`, together with the close block of finding 3 that `87e164afe` added. The frame keeps `skills/` outside the policy root and has the build edit it directly, while the settle writes only the policy root from `## Rule changes` (`frame/design.md` G7, line 15). The fix pass answered round 1's open question by naming the settle as the party that makes the change. It wrote that answer only into the close block, which the settle does not read. So the question ends up with nobody, and the gap comes from round 1's own wording, "a question for the settle's diff", which named no home either.

The close says that once the settle writes the hook's row of `docs/running/what-a-script-gates.md` *The checks*, the sentence of `skills/implement/orchestration.md` on what counts as open "can cite it in place of restating the reading, which is the settle's diff to make". Claimed: the settle makes that change. Found: the settle writes the sections that `## Rule changes` names, under `docs/`. It then decides each open row of the work item's records and removes the directory, close blocks included. No `## Rule changes` item can name `skills/implement/orchestration.md`, and no row of `gaps.md` names it. After the settle, `skills/implement/orchestration.md:308-317` and the *The checks* row at `frame/design.md:147` will both say when the hook refuses a call and what lets the call through. They will also both say that the hook does not judge whether a question is the owner's. The chain check prints no repeat notice for the row (executed, `## Probes`), because the words differ, so no script will raise it either. The next change to what counts as open would then have two places to change, and `skills/core/SKILL.md` *The rule a mechanism is kept against* gives a fact one source.

Before the settle, the paragraph has to keep its statement, because the row does not stand until then and the released plugin ships `docs/` without it. So the fix gives the deferral a home the settle reads: a row of `## Not verified`, whose open rows the settle decides at its step 6. A tracker issue would also be a home. If the fix pass takes that route, its close names the issue in place of the row.

```markdown
| Whether `skills/implement/orchestration.md` *Orchestrator: how the work is routed*, the paragraph opening **While the `Automation` row reads `yes`**, still states when the hook refuses a call after the settle writes the hook's row of `docs/running/what-a-script-gates.md` *The checks* from `frame/design.md` `## Rule changes`. After the settle both would state it, and the paragraph can cite the row in its place (round 1 finding 3). The settle writes the policy root alone (`frame/design.md` G7), so this row is what puts the paragraph in front of it. | the settle after the 0.38.8 release |
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `lib/routing.py:394-401` normalises each worktree path git prints before `declarations` joins the records' path onto it, and the comment cites `optin.home_paths`. The new case `test_accepts_a_worktree_path_git_spells_otherwise_in_its_native_spelling` turns red at `tests/lib/test_routing.py:577` when `normpath` is dropped (executed: `seal mutate` in the round's clone). Its left side read `.../repo/./seal/threads/...`. Round 1's `evidence: executed` line was run again against the new run: run 45343775784 at `61513fa00` concluded `success` on every leg, all four Windows 3.12 groups among them (executed: `gh run view 45343775784 --json conclusion,status,headSha,jobs`). The durations file of Windows group 2 lists every case of `Test_open_declarations`, the new case and the one at `tests/lib/test_routing.py:550` among them (executed: `gh run download 45343775784 -p 'test-durations-*'`, then a grep). The orchestrator also reported the same run's success to this round. The `gaps.md` row at line 9 now has its answer in that run. Closing the row is the orchestrator's act, before the sealer.

```seal
confirms: round-1#2
```
What holds: the reason's open-items part at `hooks/ask-under-automation.py:136-141` says what makes a work item open and what ends the refusal. The next part sends the session to the `frame/questions.md` of the work item it runs. `main` at lines 176 to 182 names each item once. Round 1's probe was written again from its `## Probes` row and run once, as `test_tmp_round2.py`. From the main checkout (case A) and from the `chore/other` worktree (case C), the hook refused with exit 0 and nothing on stderr, and named `1780000000-old on branch feature/old` once. Each reason held "checked out", the sentence on removing the worktree, and "the work item this session runs". Dropping the dedupe turns `test_refuses_naming_a_work_item_once_whatever_worktrees_hold_copies` red at line 140 with the item named twice, while S1 stays green (executed: `seal mutate`). So the new case holds what S1 does not. The changelog's first item states what the reason now carries, and states it truly (read `changelog.md:3`). Finding 1 above is a regression on S1's pin alone.

```seal
confirms: round-1#3
```
What holds: the first `## Rule changes` item's `to` at `frame/design.md:132-142` keeps the rule and the marker's form, and cites *The checks* for when the hook refuses. The *The checks* row at line 147 states the refusal in its Reads cell. At the target the chain check prints no repeat notice at either item (executed). A probe calling `parse` and `apply_op` of `skills/settle/scripts/rule_changes.py` on the frame read no error and no unread line, and it placed all four items (executed: `test_tmp_rule_changes.py`). `tests/behaviour/test_a_cited_section_stands_in_its_file.py` passed, 64 cases (executed). The second judgment row of `frame/plan.md` records the fold with its grounds, and `c35d7f384`'s diff matches that row. Finding 2 above is a regression on where the close's deferral was left.

What matched: `0b65dda2e` rewrites *Scope* item 2's second bullet at `frame/design.md:56` in place, and the bullet agrees with `hooks/ask-under-automation.py:136-141` and `:176-182`. It records what the fix pass changed, so the orchestrator folding it in a commit of its own, with no framer, is what `skills/implement/orchestration.md:71-74` says. No other sentence of the frame is contradicted at the target. S1's "Then" names the paragraph, the item and the branch, and the reason still holds all three. `frame/plan.md:9` says each refusal names the work item and branch, and it does.

What matched: the three quotes of `pr.md` stand word for word, with whitespace collapsed, at their sources (executed: a script comparing each quote with `frame/plan.md`, `frame/questions.md` and `gaps.md`). Each coordinate names one place: the judgment row on the title's prefix at `frame/plan.md:60`, the Status cell of Q1 at `frame/questions.md:13`, and the `gaps.md` row whose answerer is the repository owner on Windows hardware at line 8.

What matched: the third judgment row of `frame/plan.md` answers round 1's `## Not judged` row on the reading of open. Its quote, "the `seal/` root of the session's repository and its worktrees", stands in #1608's first *Done when* item (executed: `gh issue view 1608`). The answer is the orchestrator's judgment against the issue, and this round does not re-judge it.

What matched: the `gaps.md` diff rewrites the Windows row in place and adds one row, and no row leaves it (read: the diff of `0305f5e73..61513fa00`). The Windows row's claims hold. `.github/workflows/test.yml:81-84` holds the four Windows legs, and `tests/hooks/test_core_start.py:27-38` runs the command's `python3` half with the runner's interpreter in its place (read).

Each new case was read against its group. The routing case holds on every platform what the case at `tests/lib/test_routing.py:550` holds on Windows alone. The hook's dedupe case holds a guard S1 does not catch, as round 1 finding 2's mutation above shows. Neither repeats another case of its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the suite is `unverified` at `61513fa00` beyond the three modules this round ran, and the CI run 45343775784 is not the broad gate's command | the `Broad gate` key of `seal/config.json` | the orchestrator's broad run, after this round's two findings are closed |
| Whether the main session honours the deny and shows no question: carried from `frame/questions.md` Q1, measured by the orchestrator, not re-established here | `seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/frame/questions.md:13` | the orchestrator |
| The hook's `py -3` half and a real session on Windows | `hooks/hooks.json:30` | the repository owner, on Windows hardware |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/hooks/test_ask_under_automation.py tests/lib/test_routing.py -q` in a `git clone --no-local` at `61513fa00` | 87 passed, on macOS |
| `bin/seal mutate lib/routing.py`, `normpath` dropped, running the new routing case | red at `tests/lib/test_routing.py:577`, the path spelt with `/.` |
| `bin/seal mutate hooks/ask-under-automation.py`, ` and item not in items` dropped, running the dedupe case and S1 | the dedupe case red at line 140, `assert 2 == 1`; S1 passed |
| `bin/seal mutate hooks/ask-under-automation.py`, ", or removing the worktree" dropped, running S1 | red at line 127 |
| `bin/seal mutate hooks/ask-under-automation.py`, "Where its run has ended, checking out " read as "Now, checking out ", running the whole hook module | SURVIVED, 11 passed (finding 1) |
| `python3 test_tmp_round2.py` in the round's scratch directory, run once: round 1's cases A and C | A and C: exit 0, nothing on stderr, the item named once, each sentence of the fix present |
| `python3 test_tmp_rule_changes.py` in the round's scratch directory, run once | no error, no unread line, four items placed |
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` | 64 passed |
| `gh run view 45343775784 --json conclusion,status,headSha,jobs` and `gh run download 45343775784 -p 'test-durations-*'` | `success` at `61513fa0`, every leg; Windows group 2's durations list every `Test_open_declarations` case |
| `python3 skills/code-review/scripts/chain_check.py --baseline 7c8f67103 --root <the checkout> --worktree`, before the record | exit 0; the three owed-verifying-round notices for round 1's closes, the target-behind-HEAD notice, and the missing gate and guarantee; no repeat notice at `frame/design.md` |

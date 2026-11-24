# Review round 1: 1795499830-the-orchestrator-asks-under-automation-yes

```seal
target: 65b34c3c7 against origin/release/v0.38.8
```

The range is `7c8f67103..65b34c3c7`, the base being `origin/release/v0.38.8` at `7c8f67103`. No earlier round exists, so nothing is carried from one. Two facts are carried from the orchestrator and not re-established by this round. The first is `frame/questions.md` Q1, the measurement that Claude Code 2.1.331 honours the deny in the main session. The second is the result of run 45341773186, which this round re-read with `gh run view 45341773186 --log-failed` and did not re-run. The records `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and both phase records were read whole at `65b34c3c7`. `Commit and pull request language` and `Record language` are both English, so no `pr.<lang>.md` is owed.

## Findings

### 1. `open_declarations` returns each path spelt two ways on Windows, and the Windows leg of the suite fails on it

```seal
severity: must
location: `lib/routing.py:394-396`, `lib/routing.py:362-384`, `tests/lib/test_routing.py:543-550`, `seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/gaps.md:8`
evidence: executed `gh run view 45341773186 --log-failed`; read `lib/routing.py:394-403`, `lib/optin.py:180-187`
```

Why it matters: the pull request's `tests` workflow is red on one leg, so the pull request cannot merge as it stands. The orchestrator reported the failure, and this round read it in the run's log: `tests\lib\test_routing.py:550: AssertionError`, `assert [('C:/Users/x/...ng.md', 'no')] == [('C:\\Users\...ng.md', 'no')]`, on `pytest (windows-latest, 3.12, --splits 4 --group 2, ...)`.

The defect is in the reader, not in the case. `lib/routing.py:394-396` takes each worktree path from the `worktree` line of `git worktree list --porcelain` as git prints it, and git prints `/` on Windows. `declarations(tree)` then joins the root and `threads/<item>/routing.md` onto it with `\`, so each path the function returns reads `C:/Users/x/repo\seal\threads\...\routing.md`. The tree has already ruled on this shape. `lib/optin.py:180-187` normalises the git-derived half of `home_paths` because a git answer joined with native separators gives "one path spelled two ways". It also says that normalising at the source fixes the path for every caller. The docstring of `open_declarations` says it returns pairs "as `declarations` gives them", and a caller that passes a native root to `declarations` gets a native path. The S6 cases pass on Windows only because they compare `os.path.realpath` on both sides. The hook itself is not affected, because `os.path.basename(os.path.dirname(path))` reads both separators on Windows. The next caller that prints or compares the path will be.

The fix normalises the path where git hands it over. With that change, the case at `tests/lib/test_routing.py:550` holds as written. One precondition applies: `os.path.normpath` changes separators and nothing else. If the runner's temporary directory were also spelt as an 8.3 short name on one side, the case would still differ. In that case the fix pass compares real paths, as the S6 cases at `tests/lib/test_routing.py:582` and `:593` do, and says so. The `gaps.md` row on Windows (line 8) says the cases run the `python3` half under "this interpreter". The workflow's Windows legs ran `Test_open_declarations` and the hook's module, and those legs found this defect. So the fix pass also rewrites that row to say what the Windows CI legs ran and what stays unrun: the `py -3` half, and a real session on Windows.

```python
    lines = done.stdout.split("\n")
    # `normpath` on git's answer, as `lib/optin.py#home_paths` does: git
    # prints a worktree's path with `/` on Windows, and `declarations` joins
    # the records' path onto it with `\`, which would spell one path two ways.
    trees = [
        os.path.normpath(line[len(WORKTREE_LINE) :])
        for line in lines
        if line.startswith(WORKTREE_LINE)
    ]
```

### 2. The refusal does not say what makes a work item open or what ends the refusal, so after a merge it sends a session to record its default in a finished work item

```seal
severity: should
location: `hooks/ask-under-automation.py:134-145`, `tests/hooks/test_ask_under_automation.py:103-112`, `seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/frame/plan.md:9`
evidence: executed `python3 test_tmp_round1.py <the checkout>` in the round's scratch directory (see `## Probes`); read `hooks/ask-under-automation.py:117-159`, `frame/plan.md:9`, `frame/plan.md:51`
```

Why it matters: `frame/plan.md:9` names the failure it chose to accept: a work item's branch stays checked out after its pull request merges, and every `AskUserQuestion` call in that repository is then refused. The plan's mitigation is its last sentence: "Each refusal names the work item and branch that caused it, which tells the person what to switch or remove." The code does not do that. The probe built that state: `main` holds a released item whose branch `feature/old` is still checked out in a linked worktree. The session asks from the main checkout. The hook refused. Its reason said only that "a work item open in this repository reads `Automation` `yes`", then listed the item and its branch. It then said "Where the tree or the work item's frame/questions.md answers a question, proceed on its default and record it as that paragraph says". The words "checked out" and "switch" are not in the reason. A session that is not in that item's run is told that the item is open, and is sent to write a row into that finished item's `frame/questions.md`. Nothing in the reason tells it that the branch left checked out is the cause. `frame/plan.md:51` also says "The person sees nothing of the refused call", so the person cannot read the work item and branch either unless the session repeats them. The orchestrator's alternative is to write `No default:` on every question, which is the habit `frame/plan.md:9` says ends the hook's use.

The same probe showed a second defect in the same reason. In shared mode each worktree that branched after the merge holds its own committed copy of the released item. `open_declarations` counts each file once by its real path, as `frame/design.md` *Scope* item 1 says. That is three files for one work item here, and the reason printed `1780000000-old on branch feature/old` three times.

This is a defect in the reason's text, which the session acts on. It is not a challenge to the frame's choice of what counts as open. The frame's question of whether that choice answers #1608's "whose work item is still open" is a row of `## Not judged`. The fix says what makes an item open and what ends the refusal, and names each item once. The fix pass also pins the sentence and the single naming in the S1 case, under contract rule 14. `frame/plan.md:9` is true once the fix lands, so it needs no change.

```python
    named = ", ".join(_label(one) for one in unstated)
    listed = []
    for item in items:
        if item not in listed:
            listed.append(item)
    parts = [
        ...,
        rule,
        "Open work items reading `Automation` `yes`: "
        + "; ".join(name + " on branch " + branch for name, branch in listed)
        + ". A work item counts as open while its branch is checked out in a "
        "worktree of this repository. Where its run has ended, checking out "
        "another branch in that worktree, or removing the worktree, ends this "
        "refusal, and that work item's records take nothing from this call.",
        ...
    ]
```

```python
        # in test_refuses_a_question_under_automation_yes_with_the_rule (S1)
        assert "counts as open while its branch is checked out" in reason, reason
        assert reason.count(ITEM + " on branch " + BRANCH) == 1, reason
```

The single-naming assertion holds the deduplication only where two worktrees hold the item. So the fix pass either adds a case that builds a linked worktree holding a copy, as `tests/lib/test_routing.py:573` builds one, or says why S1 is enough.

### 3. The first `## Rule changes` item's `to` repeats the passage `skills/implement/orchestration.md` keeps on the hook

```seal
severity: should
location: `seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/frame/design.md:132-146`, `skills/implement/orchestration.md:304-317`
evidence: executed `python3 skills/code-review/scripts/chain_check.py --baseline 7c8f67103 --root <the checkout> --worktree`; read `frame/design.md:132-146`, `frame/design.md:150`, `skills/implement/orchestration.md:304-317`
```

Why it matters: the chain check prints this notice at the item:

`seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/frame/design.md:132  this `to` repeats a passage of `skills/implement/orchestration.md`: 11 of its runs of 15 words stand there, one of them "hook, hooks/ask-under-automation.py, refuses an askuserquestion call while the routing.md of a work item whose branch"`

Read side by side, the notice is right on meaning as well as words. Both texts say:

- the hook refuses a call while the `routing.md` of a work item whose branch is checked out in a worktree reads `yes`;
- it lets the call through where every question states why;
- it does not judge whether a question is the owner's, and the person reads the reason in the question.

After the settle, `docs/running/the-run.md` *The run* and `skills/implement/orchestration.md:304-317` would both state these facts. The third item's *The checks* row (`frame/design.md:150`) states what makes an item open and that the hook does not judge the owner's question a third time. The hook prints *The run*'s paragraph into its refusal, so after the settle one refusal would also state its own let-through form twice. `skills/core/SKILL.md` *The rule a mechanism is kept against* gives a fact one source, and the next change to what counts as open would have to find three places to change.

The orchestrator asked whether the hook is now stated in more places than its one home needs. This is the instance that answers yes. The fix cuts the `to` down to the rule *The run* owns: a blocking question states why its default cannot be taken, after the marker. The hook's reading is left to *The checks*, which the same settle writes. `skills/implement/orchestration.md:304-317` stays until the settle, because before the settle it is the only text the orchestrator reads on the hook. The fix pass also says whether its sentence on what counts as open (lines 308 to 311) should cite *The checks* once the settle has written that row. That is a question for the settle's diff, and this round names it rather than closing it.

```markdown
- change
  file: docs/running/the-run.md
  section: The run
  from: The orchestrator keeps a blocking question for what only the
    owner can decide, and only where proceeding on a default would be costly to undo or
    would reach outside the repository. A question or a remark the owner raises
    during the run is taken up when it arrives: the framer folds it into the
    frame, or it goes into the code, and it is never deferred to the pull
    request body.
  to: The orchestrator keeps a blocking question for what only the
    owner can decide, and only where proceeding on a default would be costly to undo or
    would reach outside the repository. Each question of such a call states why
    its default cannot be taken, in its text, after the marker
    `hooks/ask-under-automation.py#MARKER` holds, and the plugin's
    `PreToolUse` hook refuses a call that does not, as
    `docs/running/what-a-script-gates.md` *The checks* states. A question or a remark the owner raises
    during the run is taken up when it arrives: the framer folds it into the
    frame, or it goes into the code, and it is never deferred to the pull
    request body.
    check: tests/hooks/test_ask_under_automation.py
```

The fix pass runs `parse` and `apply_op` of `skills/settle/scripts/rule_changes.py` on the rewritten item, as `frame/design.md:49` records the framer did. It also runs `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, since the `to` now cites *The checks*, a section the third item adds a row to and does not create.

## Confirmations

What matched: the orchestrator's first point asked whether the hook refuses only where the rule asks and never blocks a session with no open work item. Where no declaration of a checked-out branch reads `yes`, the hook prints nothing. That holds for a `no` row, a `yes` row for a branch no worktree has checked out, a repository with no root and a directory outside git (executed: `bin/test tests/hooks/test_ask_under_automation.py tests/lib/test_routing.py -q`, 85 passed; read `tests/hooks/test_ask_under_automation.py:151-164`). Where a merged branch stays checked out, the hook does refuse (executed: the probe's case A). `frame/plan.md:9` chooses that cost, and `frame/plan.md:17` chooses to read every worktree, so the hook also refused a session in an unrelated worktree on `chore/other` (the probe's case C). So the claim that it "never blocks a session with no open work item, including a branch left checked out after its pull request merged" does not hold. The code does what the frame says. Finding 2 covers what the refusal tells the session in that state, and `## Not judged` asks whether the frame's reading of open answers the issue.

What matched: a worktree whose directory was removed without `git worktree prune` does not make the hook fail. `lib/optin.py:140-143` answers `""` for its common directory and `declarations` finds no root there. The branch still counts as checked out, as git still lists it. The hook refused with the main checkout's copy (executed: the probe's case B, exit 0, nothing on stderr).

What matched: the hook fails toward letting the call through on every path *Scope* item 2 lists. `main` reads `payload["cwd"]` and `tool_input` and returns before printing on no items, a list of another shape, or every question stated. The `__main__` block catches `BaseException`, which takes in `lib/gitcmd.py#Failed`, and exits 0 (read `hooks/ask-under-automation.py:162-213`). `open_declarations` catches `gitcmd.Failed` and reads a non-zero exit as no answer (read `lib/routing.py:385-392`). The phase 1 mutation rows R4, R6b, H9, H11 and H12 report those guards each seen red or surviving as stated, and this round did not re-run them.

What matched: `STATED`, at `hooks/ask-under-automation.py:73`, requires a non-blank character after the marker on the same line, and `NEAR` names a case variant only for a question that does not state why (read `hooks/ask-under-automation.py:73-76`, `:147-158`). This is the form G1 and *Scope* item 2 give.

What matched: of *Scope* item 7's three passages, the second and third each state one *Done when* item of #1608 once. Lines 201 to 205 say that the *Done when* of every named issue is read before the batch, which is item 3. Lines 246 to 254 say that a rule restricting agents comes only from this run's batch or a policy document, is written with its source under `## Why this way`, and is not carried from an earlier run, which is item 2 (read `skills/implement/orchestration.md:196-254`, `gh issue view 1608`). The first passage states item 1 once inside `skills/implement/orchestration.md` and is the passage finding 3 is about. S10's search prints nothing and exits 1 at `65b34c3c7`. S11's search prints `docs/running/measuring-a-run.md:140` and `:143` alone (executed, both searches as `frame/design.md` gives them).

What matched: the three quotes in `pr.md` stand word for word at their coordinates: `frame/plan.md:60`, the Status cell of `frame/questions.md` Q1 at line 13, and `gaps.md:8` (read). `changelog.md` describes what the diff does, and its `### Process changes` rows each name a passage of item 7 (read). `.claude-plugin/plugin.json` reads `0.38.8` (read).

Other statements of the hook's form: `README.md:356` and `README.ko.md:354` spell `No default:`, while the comment at `hooks/ask-under-automation.py:59-61` says a document that states the form cites `#MARKER`. The README is the person's account of what runs on their machine, and *Scope* item 6 asks it to say what lets the call through, so this round opens no finding for it. A rename of `MARKER` would leave both READMEs stale, and no case pins their spelling.

Each new case was read against its group. The hook-level S5 case builds the same four trees as `Test_open_declarations`. Its `no` tree pins the hook's `yes` filter (row H8), and its other trees hold *Scope* S5's "and the hook's command runs there". No new case repeats another in its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether reading open as a branch checked out in any worktree answers #1608's *Done when* item 1, "whose work item is still open", for a merged branch left checked out and for a session doing unrelated work in another worktree. The frame chose it with grounds at `frame/plan.md:9` and `:16-19`, and finding 2 covers only what the refusal says. | `lib/routing.py:362-406`, `seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/frame/plan.md:9` | the orchestrator, against #1608 |
| Whether the main session honours the deny and shows no question: carried from `frame/questions.md` Q1, measured by the orchestrator, not re-established here | `seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/frame/questions.md:13` | the orchestrator |
| The hook's `py -3` half and a real session on Windows | `hooks/hooks.json:30` | the repository owner, on Windows hardware |
| The broad gate: the suite is `unverified` at `65b34c3c7` beyond the two modules this round ran, and the CI run at `26e35d4e1` is red on finding 1 | the `Broad gate` key of `seal/config.json` | the orchestrator's broad run, after the fix pass |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_round1.py <the checkout>` in the round's scratch directory, run once: a repository on `main` holding a released item for `feature/old`, a linked worktree on `feature/old` and one on `chore/other` | A: from the main checkout the hook refused, exit 0, nothing on stderr; the reason listed `1780000000-old on branch feature/old` three times and held neither "checked out" nor "switch". C: from the `chore/other` worktree it refused. B: with the `feature/old` worktree's directory removed and not pruned, `open_declarations` answered two paths and the hook refused, exit 0, nothing on stderr |
| `bin/test tests/hooks/test_ask_under_automation.py tests/lib/test_routing.py -q` | 85 passed, on macOS |
| `gh run view 45341773186 --log-failed` | one failure, `Test_open_declarations::test_accepts_a_declaration_on_the_branch_checked_out` at `tests\lib\test_routing.py:550`, mixed separators on the left side, native on the right |
| `git grep -n -i -E 'decides anything on it' 65b34c3c7 -- . ':!seal/threads'` | nothing, exit 1 |
| the count search of `frame/design.md:36` at `65b34c3c7` | `docs/running/measuring-a-run.md:140` and `:143` alone |
| `python3 skills/code-review/scripts/chain_check.py --baseline 7c8f67103 --root <the checkout> --worktree`, before the record | exit 0; the notice finding 3 quotes, and the open-chain notices for a round, gate and guarantee not yet written |

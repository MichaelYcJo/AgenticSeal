# Review round 1: 1794372899-two-skills-tell-the-framer-to-ask

```seal
target: 2af43c27f against 7b2b0fe6a
```

This is the first round, so no earlier record carries a coordinate and every fact below was established in this round. The range `7b2b0fe6a..2af43c27f` holds the routing (`b578ffb77`), the frame (`bc6d22eea`), the build (`7ffcf1ab9`), the phase records (`39bf13e1b`) and `pr.md` with the title row (`2af43c27f`). The build changes `agents/framer.md`, `README.md`, `README.ko.md`, two test modules, and removes `skills/feature-planner/SKILL.md` and `skills/confidence-check/SKILL.md` (executed, `git diff --stat 7b2b0fe6a..HEAD`). Every command ran in a `git clone --no-local` at `2af43c27f` under the round's scratch directory. The branch worktree received this record and nothing else.

The records read whole at the target are `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md`. Both language keys of `seal/config.json` are English, so no `pr.<lang>.md` stands. No `seal/parity.json` stands, so no original is compared. The issue was read with `gh issue view 1480 --json title,body,comments`: it has no comment, and its *Decision* records the owner's choice of fold and remove on 2026-11-11.

The axes for this change are the text an agent acts on (step 5 of `agents/framer.md`), the reach of the removal across every tracked file, the cases that read the removed files, the size of the framer's preload, and the records' statements against the target. The comparison table's runtime rows (authorization, query scope, concurrency, security) have no code to walk here: the diff changes prose, two README rows and test units, and adds no executable path.

## Findings

### 1. Step 5 tells a framer to read the installed version's API, so the upgrade half of confidence-check's check 3 has no home

```seal
severity: should
location: `agents/framer.md:101-103`, `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/frame/design.md:60-71`, `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/frame/design.md:85`, `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/frame/design.md:14`, `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/frame/design.md:49`, `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/frame/plan.md:15`, `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/changelog.md:3`, `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/changelog.md:13`
evidence: read `agents/framer.md:101-103`, `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/frame/design.md:60-73`, `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/frame/design.md:85`; executed `git show 7b2b0fe6a:skills/confidence-check/SKILL.md`
```

Why it matters: every framer spawn preloads step 5, and a framer whose work moves a library to a new version reads "a library's API is the one its installed version holds, read there" as an order to read the old version. The new version's API, and the breaking changes between the two, are what such a frame rests on. The removed skill covered that case. `skills/confidence-check/SKILL.md:33-35` at the base holds check 3 as two bullets: "Library or framework API verified against current version" and "Breaking changes checked if upgrading". The frame claimed check 3 lands in D1 whole: `frame/design.md:85` reads "confidence-check checks 1, 3 and 5: no duplicate, the API against the installed version, the cause understood | D1", and `:73` repeats it. `agents/framer.md:101-103` holds only the first bullet. No other row of D2 places the second bullet, and no other text the framer opens names an upgrade (read). So the release ships the definition saying less than the frame says it says, and the frame's D2 row is contradicted by the target.

The same D2 row also reads check 5 as "the cause understood". Check 5 at the base (`:41-43`) has a second bullet, "For features: clear understanding of requirements". That half does have a home: D2's first feature-planner row puts requirements and acceptance in *Scope* and *User scenarios & acceptance* (`frame/design.md:79`). So the row only needs to say so; nothing is lost there.

The fix reaches these statements. The byte figures change with the step: measured in memory on the target's file, the text below makes `agents/framer.md` 15,051 B, 227 B over the base's 14,824 B, with its longest line 74 columns (executed, in the probe row of `## Probes`). D1 grows from 726 B to 766 B by the same 40 B. The framer's preload becomes 37,179 B. The fix pass owes each figure where it stands: `frame/design.md:14` (G6, "187 B", "15,011 B", "37,139 B", "0.187 KB"), `:49` (S4, "15,011 B"), `frame/plan.md:15` (row 1, "187 B"), and `changelog.md:3` ("grows by 187 bytes, to 15,011"). `changelog.md:3` and `:13` name the assumption as "a library's API is the one its installed version holds" and "a library's API at its installed version", and each gains the version the work moves to. `trail/phases/phase-1.md` states the build commit it names and stays.

Step 5 at `agents/framer.md:96-105`, the same text going into D1 at `frame/design.md:60-71`:

```markdown
5. Judge: answer everything the tree can answer, by reading it, and by a
   probe where the answer is a behaviour, a time or an output (*A question
   a command answers is answered by running it* below). Settle three
   assumptions the same way before the frame rests on one: that nothing in
   the tree already does what the work adds, or could be extended to do
   it, found by searching for what it does and not for its name; that a
   library's API is the one its installed version holds, or the version
   the work moves it to, read there and not recalled; and that a bug's
   cause is shown, by the code read or by a probe that reproduces the bug,
   and not guessed. An assumption that neither reading nor a probe settles
   is a row of `frame/questions.md`.
```

D2's row at `frame/design.md:85`:

```markdown
| confidence-check checks 1, 3 and 5: no duplicate, the API against the installed version or the version the work moves to, the cause understood | D1. Check 5's second bullet, the requirements of a feature, stands in *Scope* and *User scenarios & acceptance*, as the first feature-planner row gives |
```

Where the fix pass judges that the upgrade bullet should go rather than land, the other repair is a D2 row naming it as going, with its grounds, and step 5 keeps its text. That route still owes `frame/design.md:85` and `:73`, which now say check 3 lands in D1 whole.

```seal
verdict: fixed 89a0546cf
answer: The finding holds: at 2af43c27f step 5 read a library's API at its installed version alone, and confidence-check's check 3 at 7b2b0fe6a also covered the breaking changes of an upgrade. The paste-ready step was read against D1, D2 and G6 as the fold at 03606ef77 states them, and it matches D1 word for word (executed, a python3 substring test of D1 against agents/framer.md). Commit 89a0546cf puts it in place of step 5's last four lines through the Edit tool. agents/framer.md now holds 15,051 B, the figure S4 gives, its diff against 7b2b0fe6a is one hunk inside step 5, the core and the contract are unchanged, and no new line is over 88 columns (executed). In the same commit changelog.md:3 names the version the work moves to and gives 227 bytes and 15,051, changelog.md:13 names the same version, and gaps.md's broad gate row names fix pass 1's run. The D2 row and the figures at frame/design.md:14, :49, :73 and :85 and frame/plan.md:15 are the framer's and were folded at 03606ef77. trail/phases/phase-1.md describes the build commit 7ffcf1ab9 and is unchanged. The narrow run of the four modules S7 names gave 100 passed, exit 0, at 89a0546cf (executed).
```

## Confirmations

What matched: S1 and S2. `git grep -n -i -E 'feature-planner|confidence-check' -- . ':!seal/threads' ':!.test_durations'` printed nothing and exited 1. `git ls-files skills/feature-planner skills/confidence-check` printed nothing, and `ls skills` lists neither directory (executed). A wider search, `git grep -n -i -E 'feature.?planner|confidence.?check|planner skill|readiness'` outside this work item, found only `docs/running/the-agent-set.md:51` and `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/plan.md:40`, the two lines the frame keeps by *Out* (executed). Searches for paraphrases of the old step and of the skills' role (`need neither`, `readiness is`, `a cause still guessed`, `utility skill`, `calls rather than preload`, `is driving`, `stand down`, `two skills`) found no shipped text outside the records and test fixtures that name other skills (executed). That reach is a sample, since a paraphrase is an open class.

What matched: S3, against D1. `agents/framer.md:96-105` at the target is D1 at `frame/design.md:60-71` word for word, and `git diff 7b2b0fe6a -- agents/framer.md` holds one hunk inside step 5, removing six lines and adding eight (executed). The crafter claimed the first two lines of D1 are unchanged; the hunk's context shows them unchanged (read). The definition's seven `check:` lines moved by two lines each and kept their text (executed, `grep -n '^check:'` at the base and the target), which agrees with `frame/plan.md:35` on #1475.

What matched: S4. `wc -c` gives `agents/framer.md` 15,011 B at the target and 14,824 B at the base, so it grows by 187 B, and `skills/core/SKILL.md` 9,322 B and `skills/agent-contract/SKILL.md` 12,806 B are unchanged, 37,139 B in all (executed). No tracked file outside the records pins either figure (executed, `git grep` on the four figures). Finding 1 changes these figures.

What matched: S5, with a wider list than the frame's. The crafter claimed G8's grep over eight files gives 16 hits and none tells the framer to ask a person. The count is 16 (executed). G8's list leaves out four files `agents/framer.md` itself names for the framer: `skills/implement/SKILL.md` (step 3 opens three of its sections), `templates/records/process.md`, and the two preloads. I ran the same grep over those (executed). `skills/implement/SKILL.md:143-145` says a ticket asking for what policy forbids is written into `questions.md`, and `:163-166` gives the asking to the orchestrator. The core's hits at `:76` and `:92-97` weigh asking and give it to the orchestrator's one batch. The contract's hit at `:49` is the hand-back's naming of what a prompt asked. None tells the framer to ask (read). So the issue's first *Done when* item holds at the target, though G8 stated it from a list that was not every file the framer opens.

What matched: S6 and S7. `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_docs_line_wrap.py tests/text/test_review_axes.py -q` exited 0 with 100 passed, the count the crafter claimed (executed). `#test_the_skills_row_lists_the_on_demand_skills_without_a_count` (`tests/behaviour/test_chain_hooks_hardening.py:462-479`) compares the README sentence against the on-demand set derived from `skills/*/SKILL.md` and the agents' frontmatter (`:425-447`), so the two names left in either row would be red while the directories are gone (read). That matches the crafter's `seal mutate` run, which I did not re-run. `uvx ruff check` and `uvx ruff format --check` over the two changed test modules exit 0 (executed). The crafter's 99 passed and 1 failed at `7ffcf1ab9`, before the records stood, was not re-run.

What matched: the README rows. `README.md:276` and `README.ko.md:277` each lose the two names and change nothing else in the row (read, the diff).

What matched: the removed test units. `tests/behaviour/test_chain_hooks_hardening.py` loses its opening comment, `UTILITY_SKILLS`, `definitions_naming` and the two cases, and keeps two blank lines between the units on each side (read, the diff). `definitions_naming` imported `glob` locally, so no module import is left unused, and ruff agrees (executed). `tests/behaviour/test_the_set_a_work_item_always_has.py` loses the five-line comment and its separator, the tuple in `INSTRUCTING`, and `test_the_planner_writes_into_the_plan` (read). The fact *Removes* says that case pinned stands at `skills/implement/SKILL.md:325`, "`plan.md`'s Phases table is the task list, and there is no other." (executed, `grep -n -F`). The remaining glob readers at `tests/behaviour/test_chain_hooks_hardening.py:318`, `:433`, `:593` and `:657` are in S7's run (executed, `git grep`). No tracked test asserts a count of skills or a byte figure of a definition (executed, `git grep`). The range adds no test, so no new case is read against its group.

What matched: `.test_durations:236,257,1238` name the three removed cases and stay, as G10 and `frame/design.md:36` say (executed, `sed -n`).

What matched: G4, run again. Of the 2,226 `.jsonl` transcripts under the owner's `~/.claude/projects/`, none holds a `Skill` call naming either skill, a typed command of either, or a loaded skill's base-directory line for either (executed, `grep -l`). Two hold a `file_path` ending in either `SKILL.md`, and every such call in them is `Edit` or `Write` (executed). One of them also edits and writes `skills/confidence-check/SKILL.md`, which G4's "Edit or Write of `skills/feature-planner/SKILL.md`" leaves out. The conclusion, that no transcript holds a framer opening either skill, holds, and the changelog's *Removed* item states only that.

What matched: `changelog.md`. The *Fixed* item's quotes, "say which, and ask" and "Get user confirmation before starting", stand at the base's `skills/confidence-check/SKILL.md:47` and `skills/feature-planner/SKILL.md:42` (executed, `git show`). The *Removed* item's three cases are the three the diff removes (read). Its figures are finding 1's.

What matched: `pr.md`. Its three quotes stand word for word at `frame/plan.md:15`, `:17` and `:45`, the rows their coordinates name (read). The tree's `bin/seal pr-body` composed the body into the round's scratch directory with exit 0 (executed).

What matched: `gaps.md`. Row 1 labels the broad gate unverified and names the orchestrator, and row 2 names the test files outside S7 that walk `skills/` as a sample and gives them to the broad gate, which is honest: the phase record says the spawn narrowed the run to S7's modules (read). Row 3 names the owner for other installations' use. No row was removed, since the file is new in the range.

What matched: `routing.md`, `frame/questions.md` and `frame/plan.md` *Overlap with the release*. The routing's decision line agrees with the issue's *Decision* (read). `frame/questions.md` holds no row, and each line of its head points at a Grounding or Alternatives row that stands (read). `frame/plan.md:35` gives #1475's `check:` lines at their base coordinates, which the base's `grep -n '^check:'` prints (executed).

What matched: the routing's planner, framer, is the party whose step changes, and its rule *You ask nobody anything.* (`agents/framer.md:140-145`) now has no text beside it that says otherwise (read).

What matched: the chain check over this record. `python3 skills/code-review/scripts/chain_check.py --baseline 7b2b0fe6a --root <the branch worktree> --worktree` exited 0 and printed no notice at a line of `frame/design.md` naming a test pin or a copy. Its other lines are finding 1 standing open, and that git carries no `trail/gate.md` and no `guarantee.md` yet, which the orchestrator's broad run and the sealer write after the rounds (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD; the suite stays `unverified` in this round, which ran S7's four modules alone | `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/gaps.md:7` | the orchestrator, by `seal gate --record` |
| The test files outside S7 that walk `skills/`, which the crafter's sample lists and this round did not run | `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/gaps.md:8` | the orchestrator, by the broad gate |
| Whether another installation typed either removed command, which `frame/design.md:19` (G11) rests `fix:` on | `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/gaps.md:9` | the owner, from what users report after the release |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_docs_line_wrap.py tests/text/test_review_axes.py -q`, in the clone | exit 0, 100 passed |
| `uvx ruff check` and `uvx ruff format --check` over the two changed test modules, in the clone | exit 0 each |
| `git grep -n -i -E 'feature-planner\|confidence-check' -- . ':!seal/threads' ':!.test_durations'`, in the clone | no output, exit 1 |
| `grep -n -i -E '\b(ask\|asks\|asking)\b\|confirm'` over G8's eight files, then over `skills/implement/SKILL.md`, `templates/records/process.md`, `skills/core/SKILL.md` and `skills/agent-contract/SKILL.md`, in the clone | 16 hits over the eight; each hit over the four read in its section, none telling the framer to ask |
| `find . -name '*.jsonl'` under the owner's `~/.claude/projects/`, then `grep -l` for a `Skill` call, a typed command, a loaded skill's base-directory line and a `file_path` naming either skill | 2,226 transcripts; 0, 0 and 0 for the first three; 2 for the last, every call in them `Edit` or `Write` |
| a `python3` heredoc reading `agents/framer.md` in the clone, replacing step 5's last five lines with finding 1's text in memory, and printing the sizes | 15,011 B before, 15,051 B after, 227 B over the base, longest replaced line 74 columns; nothing written |
| `bin/seal pr-body seal/threads/1794372899-two-skills-tell-the-framer-to-ask --body <scratch>/body.md`, in the clone | exit 0, the body written into the round's scratch directory |

# Review round 3: 1795590951-a-fix-builds-a-unit-no-frame-designed

```seal
target: 4836857a1, fixes fc096778b..4836857a1
```

This is the verifying round. The range read is `fc096778b..4836857a1`, read in a `git clone --no-local` at the target. Besides the round 2 record and its close blocks, it holds two commits. `42e4c8fe2` is the orchestrator's: it narrows `frame/design.md:58`, `:70` and `:86`, rewrites the #1614 row of `seal/follow-up.md:46`, and adds the first row of `frame/plan.md` *Judgments of the run* (`:72`). `34887c899` is the crafter's: it rewrites `gaps.md:9`, and the comment and the name of `RULES` key `"33 "` in `tests/text/test_the_rules_have_one_owner.py:388-393`. The range changes nothing under `skills`, `agents`, `docs` or `templates` (`git diff --stat fc096778b 4836857a1 -- skills agents docs templates` printed nothing, executed). No unit of the fix diff is new. Each change rewrites a sentence or a row the tree held, and the test change renames a dict key in a part only the tests read. No case is new, so no test is read against its group.

The work item's records that state the present were each read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`. `trail/phases/phase-1.md` was read too, and so were `trail/rounds/round-1.md` and `round-2.md` for their coordinates. No `pr.<lang>.md` stands, since `Commit and pull request language` is English. `seal/parity.json` is not declared.

Carried from rounds 1 and 2 and not re-derived: the coordinates each earlier finding named; the target's sections of `skills/implement/fix-pass.md`, `skills/implement/orchestration.md`, `skills/implement/fold-and-reframe.md` and `skills/code-review/orchestration.md`, which the range did not change; the G11 counts in `seal/follow-up.md:46`; and `trail/phases/phase-1.md`'s seen-red table. Re-derived here: every verdict below, round 2 finding 1's search, the key's references, and the narrow run of the test module the range changed (*Probes*).

The fix range's new *Judgments of the run* row (`frame/plan.md:72`) was read against the target. Its narrowing commit, "the commit after `156408b2a`", is `42e4c8fe2`, which `git log` places right after `156408b2a`. Its grounds cite the paragraph of round 2's record at `156408b2a` that weighed the orchestrator's judgment (`round-2.md:13-18`). Its three unfolded places agree with that paragraph. It answers round 2's prose note that the judgment stood in the spawn prompt alone. Read.

Round 2's fix pass reworded `gaps.md:9` and did not add a `## Not verified` row for its own run at `34887c899`, which changed a Python test file. `skills/implement/SKILL.md` *4. The closing memo — only what the diff cannot show* has every fix pass add such a row, and rows 7 and 8 of the memo carry one for phase 1 and for round 1's fix pass. This round opens no finding on it. The branch's next commit, `b49136386`, records the broad gate's run at `4836857a1`, the target, and the target holds `34887c899` (`trail/gate.md`, read). So the row would ask a question that record already answers. Rows 7 and 8 stand open in the memo with the broad gate as their answerer, and closing them is the crafter's next act on the memo.

## Findings

None. Each finding round 2 closed holds, and the fix range opens no new one.

## Confirmations

```seal
confirms: round-2#1
```
What holds: at the target, `gaps.md:9` reads "the narrowing of every other fold whose source is a fix or a build". `frame/design.md:70` reads "each fold commit after a fix pass or a build phase". `seal/follow-up.md:46` reads "the narrowing, as each fold commit after a fix pass or a build phase read for a frame sentence it added that describes what was built". The comment at `tests/text/test_the_rules_have_one_owner.py:389-392` and key `:393` read "a fix or a build removes or narrows". Each matches the home, `skills/implement/orchestration.md:83-84`, "A fold whose source is what a fix or a build changed". All read. Round 2's own search, run again over `agents`, `skills`, `docs`, `templates`, `tests`, `seal/follow-up.md` and the work item's frame, `gaps.md`, `changelog.md` and `pr.md`, printed no statement of the scope as a fix alone, executed. The lines it printed that do not say "a fix or a build" are `frame/design.md:16` (G6, dated to `d13c274e1`), the comment at `tests/text/test_the_rules_have_one_owner.py:388`, which says what a fold did in #1612, and lines on other facts. `git grep -n -F '33 a fold'` and `git grep -n -F 'fix removes or narrows'` print only `:393` and the round records, so the renamed key breaks no reference, executed. The narrow run of the test module passed (*Probes*). The close calls its list a sample, as round 2's grounds did.

```seal
confirms: round-2#2
```
What holds: `frame/design.md:58`, *Scope* item 4's first bullet, now says the orchestrator "commits the fold where the framer designs the unit". `:86`, A2's Then, says the same. The target's paragraph at `skills/code-review/orchestration.md:86-91` says the orchestrator "commits the fold, or its row that records the framer's rejection". So the two frame sentences now state only the case where they hold, and they write no account of the rejection path, which the narrowing's home asks of a fold. All read. The other frame statements of the same act were read against the target: *Scope* item 1's fifth bullet (`:45`) keeps its condition, and the changelog's second item (`changelog.md:4`) and the fourth *Process changes* row (`:17`) name both the fold and the rejection's row. None is contradicted.

```seal
confirms: round-2#3
```
What holds: `seal/follow-up.md:46`'s held-commit clause now describes the hook in the row: "a `PreToolUse` hook on the orchestrator's `Agent` call that spawns `agentic:proofer` and denies the spawn while the work item's newest round record holds a finding with no close block, which #1614 weighed and rejected". It no longer says "#1614's rejected hook". That description agrees with the row it carries, `frame/plan.md:35`. Read. `frame/design.md:69` still points at the *Alternatives considered* row. That pointer holds inside the frame, which the settle removes together with the row it names, and the follow-up row no longer depends on it.

What matched: `pr.md:1` stands word for word in the *Verdict* cell of `frame/plan.md:17`, and `pr.md:2` in the *Default until answered* cell of `frame/questions.md:14`. Read. No `pr.<lang>.md` stands.

What matched: each list item of `changelog.md` and each *Process changes* row was read against the target, and the fix range changed no fact any of them states. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the crafter's hand-back named `frame/design.md:70` before the orchestrator folded it. The narrowing's home (`skills/implement/orchestration.md:87-89`) gives the orchestrator the fold of a statement a crafter's hand-back names, and the framer the fold of a frame sentence a round finding says no longer holds. `42e4c8fe2` is the parent of `34887c899`, so the orchestrator's fold was committed before the round 2 fix pass's commit. Only the hand-back shows which fold this was. The sentence the fold wrote is round 2's snippet, and it holds at the target | `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/plan.md:72`, `42e4c8fe2` | the orchestrator |
| The suite outside this round's narrow run, the repository-wide lint and the format check at `4836857a1`, `unverified` by this round | the tree at `4836857a1` | the orchestrator's broad gate, whose run record stands at `b49136386` |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/text/test_the_rules_have_one_owner.py tests/lib/test_gaps.py tests/behaviour/test_docs_line_wrap.py`, in the clone at the target | exit 0, 167 passed |
| `git grep -n -i -E "after a fix\|source is (what )?a fix\|whose source\|fold after\|narrowing"` over `agents`, `skills`, `docs`, `templates`, `tests`, `seal/follow-up.md` and the work item's frame, `gaps.md`, `changelog.md` and `pr.md`, in the clone at the target | no line gives the narrowing's scope as a fix alone; the lines listed under round 2 finding 1's confirmation stand on other facts or on a dated tree |
| `python3 -I skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.0 --root <the branch worktree> --worktree`, with this record in the working tree | exit 0; no refusal of this record, no notice at a line of `frame/design.md`, and one line saying git carries no `guarantee.md` yet |

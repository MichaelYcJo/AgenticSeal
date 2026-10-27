# Review round 4: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

target: ea711b79, fixes fdb90e40..ea711b79

This round reads the fix diff `fdb90e40..ea711b79` and the two round 3 findings it answers, and nothing else of the branch. The diff is two commits. f8732393 changes two lines of `hooks/root-migrate.py` and two lines of `docs/one-root-by-lifetime.ko.md`. ea711b79 writes the two `answer:` lines of round 3. Carried from round 3, not re-established: each finding's coordinates, the cases that pin the other entries of the docstring's boundary list, and bd326e20's case for the first limit. Re-established this round: both verdicts below, and round 3's `evidence: executed` grep for finding 1, run again. The fix pass left both verdict lines at `open`. This round set them to `fixed f8732393`, as the spawn prompt directs. `frame/plan.md` *Verification this work item owes* binds the round: no finding asks for red-first evidence or a mutation run.

## Findings

None. The fix diff adds no defect.

## Confirmations

confirms: round-3#1
The claim was that the heading now says the second limit is stated and not pinned. `hooks/root-migrate.py:26-27` reads "Boundaries, each pinned in `tests/test_root_migrate.py` except the second limit under **on any branch**, which is stated and not pinned:". That is the second fix round 3 offered. The heading points to the right sentence: `:42` opens "A second limit, not guarded", and that limit sits inside the **on any branch** entry at `:35`. The heading is true. Round 3's grep over `tests/test_root_migrate.py` for a detached HEAD, `symbolic-ref`, `MERGE_HEAD`, a rebase or a cherry-pick ran again and found nothing (exit 1), so the second limit still has no case. The answer explains why no case was added: a case would make staging the move on a detached HEAD wanted behaviour, and the limit does not claim that. The limit sentence calls that shape one the flow does not produce, so the answer holds. `git grep` for "each pinned in" finds no test that reads the heading. It also finds `frame/plan.md:34`, which says the hook "keeps six boundaries, each pinned in `tests/test_root_migrate.py`". That sentence describes the hook before the move and still names `stamp`. It is the frame's account of the starting tree, not a statement of the boundaries, and f8732393 did not touch it. `bin/test` over `tests/test_root_migrate.py` passed after the docstring change. Executed and read.

confirms: round-3#2
The claim was that `:106` no longer uses 표시 and `:108` uses 표식. `docs/one-root-by-lifetime.ko.md:106` reads "이미 옮겼다는 기록이 브랜치의 이동을 막지 않습니다". `:108` reads "트리 안에서 옮겨지고 표식이 붙으며". The paragraph now uses 표식 only for the README marker, as `:55-61` does, so the contradiction round 3 found is gone. The new `:106` sentence does not assume a stamp exists. A record of an earlier move can exist: `hooks/root-migrate.py:119-120` keeps `stamp` and `stamp-refused` in `STATE_NAMES`, and `rename_state` carries them to the new state directory. No line of the hook reads either one as a gate. In the file, "stamp" appears only at `:35`, `:119` and `:120`. So the sentence is true, and it states the same fact as the English edition at `docs/one-root-by-lifetime.md:111-112`. The fix's `:108` is shorter than round 3's proposal ("그 `README.md` 가 표식으로 시작하게 되며"). It names the marker by the edition's own word, and that settles the finding. `tests/test_first_setup_asks_once.py` pins "앞선 배치가 남아 있는 브랜치마다" only, and that line is unchanged. The module passed in this round's run. I read the rule that a claim written into a document closes only when a test pins it as a rule about behaviour a document promises. This fix corrects a word and promises no new behaviour, so the finding closes without a new pin. Executed and read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| the full suite, the repository-wide lint and the typecheck over this branch | the branch | the orchestrator's broad run after the rounds settle |
| whether `frame/plan.md:34`, which still says six boundaries are each pinned and names `stamp`, should be brought up to date; it lies outside this fix diff and the frame is not this round's to change | `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/frame/plan.md:34` | the orchestrator, or the settle of this work item |

## Probes

| Command | Result |
|---|---|
| `grep -n -i "detach\|symbolic-ref\|MERGE_HEAD\|rebase\|cherry" tests/test_root_migrate.py` | exit 1, no line |
| `git grep -n "each pinned in\|stated and not pinned\|이미 옮겼다는\|표식이 붙"` | `docs/one-root-by-lifetime.ko.md:106`, `:108`, `hooks/root-migrate.py:26-27`, `frame/plan.md:34` and round 3's record; no test |
| `bin/test tests/test_root_migrate.py tests/test_first_setup_asks_once.py -q -p no:xdist` | exit 0, 110 passed |
| `ls -la ~/.claude/agentic` and a count of `~/.claude/specseal/` before and after the run | `~/.claude/agentic` did not exist before or after, so nothing was removed; `~/.claude/specseal/` held seven entries both times |

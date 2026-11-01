# Review round 2: 1793538228-the-release-pr-opens-after-the-last-merge

```seal
target: 68ee8eea, fixes 6248f372..68ee8eea
```

This is a verifying round over the diff of round 1's fixes, and it stays inside that diff. The diff changes four paths, all under `seal/threads/` (executed: `git diff --name-only 6248f372..68ee8eea`). No `seal/parity.md` is declared and no path outside `docs/` and `seal/` changes, so the round block holds no `original:` line.

Carried from round 1 rather than re-established: the 0.27.2 merge and run times in round 1's *Probes* (#1250 merged at 09:48:00Z, #1252's last `tests` run started at 09:43:26Z, six `tests` runs on #1251 with the last at `783a7fe8`). The fix pass's close of finding 1 says it re-ran the two commands and got the same times, which is its claim; GitHub's record of a finished release does not move, so no check of mine would fail where those times stand. Re-derived this round: every coordinate in `.github/scripts/release_completeness_check.py` that round 1 cited, and every verdict below.

## Findings

### 1. The *Removes* row still says the `to`'s last sentence names step 0, and the fold of round 1's finding 2 put another sentence last

```seal
severity: should
location: `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/design.md:99`
evidence: read `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/design.md:85-99`
regression: round-1#2
```

The unit is the second row of `frame/design.md` *Removes*, which points into the `to` of *Rule changes* by position. Phase 1's row in `frame/plan.md` builds no part of the `to`, and *Removes* says the step-0 sentence is the `to`'s last; the fix, 99642896, applied round 1's paste-ready `to` for finding 2 as given, which added a sentence on the two other refusals after it; the defect came from that paste-ready text, which named no other place that reads the `to`, applied as given.

Why it matters: the row's last cell reads "A red milestone check at the opening is now step 0 left undone, which the new last sentence says" (`frame/design.md:99`). Before 99642896 the `to` ended with "An issue it names that no branch is building is step 0's milestone box, left undone" (read, `git show 583ff676` of the design). It now ends with "Where it fails for another reason, a patch carrying a `feat:` or a label on an issue the branch does not carry, its `::error::` line names the repair" (`frame/design.md:90-92`). So the row is wrong twice:

- The coordinate is wrong. The last sentence of the `to` is now the one on the other refusals, and the step-0 sentence is second to last (`frame/design.md:89-90`).
- The claim is wrong. The new last sentence says a red check at the opening can be a `feat:` on a patch or a stray label (`.github/scripts/release_completeness_check.py:326-340` and `:256-265` print those two `::error::` lines, read). So a red check at the opening is not always step 0 left undone, and the row says it is.

The settle reads *Removes* to check that each removal lands somewhere, and the sealer reads the frame against the tree. Either reader that follows "the new last sentence" lands on a sentence that says something else. Contract rule 19 asks a change to correct what stood on the old fact in the same commit, and this row stood on the old order of the `to`.

The class, by taking the `to` apart: 99642896 changed the `to`'s sentences at `frame/design.md:67-73` and `:80-92`. I searched the work item outside the round records for every line that points at a sentence of the `to` by position or speaks of the check reading red (executed, *Probes*). The hits are `frame/design.md:98` and `:99`. Line 98 cites "the new bold sentence and the two commands", and both still stand (`frame/design.md:62-64`, `:77-87`). Line 99 is this finding. This is a sample over spellings, not a whole list.

The last cell of `frame/design.md:99`, rewritten:

```markdown
It can go, because the release pull request now opens when that check already reads green. A milestone check that names an issue at the opening is now step 0's milestone box left undone, and one that fails for a `feat:` on a patch or for a stray label names its own repair. The `to`'s last two sentences say both
```

```seal
verdict: fixed fa60e10c
answer: The finding holds. The orchestrator rewrote the *Removes* cell at `frame/design.md:99` in place with the round's paste-ready text, so it names both the step-0 reading and the other refusals' own repair and points at the `to`'s last two sentences. The commit touched only the work item's records.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: 99642896 applied round 1's paste-ready text word for word to the `to` at `frame/design.md:67-76`, to *Scope* item 1 at `frame/design.md:24`, to plan A2's verdict cell at `frame/plan.md:24`, and as the fifth failure scenario at `frame/plan.md:16` (read, the diff against round 1's fenced blocks). Plan A1's failure cell now says "The five in *Technical context*", and `frame/plan.md:13-17` holds five (read). 4e4f7f3c applied the paste-ready sentences to `changelog.md:3` word for word (read). The fix pass also changed the process row's Why cell at `changelog.md:9`, beyond the paste-ready text, to "mostly over trees already tested; on 0.27.2 five of six runs came before the last merge, and none of them failed". Claimed: that this corrects the same fact. Found: against round 1's run list, six `pull_request` runs on #1251 with only the run at `783a7fe8` after #1261, the last merge, so five came before it, and none failed (one was cancelled). 68ee8eea's A2 failure cell, "came before the last merge and read trees their own pull requests had mostly already tested" (`frame/plan.md:24`), holds against the same figures (read). The rewritten `to` still parses as one `change` with no error and no unread line, its `from` still stands in the section at `5f0cf7a7`, and its widest line is 76 columns, which `frame/plan.md:9` states (executed, *Probes*).

```seal
confirms: round-1#2
```
What holds: the `to` at `frame/design.md:80-92` is round 1's paste-ready text word for word (read). I re-read `main()` at `.github/scripts/release_completeness_check.py:355-401`. The not-a-release path prints "nothing to judge" and returns 0 at `:362-363`. The no-milestone path prints the `::warning::` line and returns at `:382-390`. Neither reaches `judge`, the only place that adds the `M (open in ...)` line (`:284`), so neither prints it. `judge` adds the `M` line on every call, the failing ones included (`:237-287`), so neither half of "exits 0 and prints its `M` line" is enough alone, and the `to` names both. The new last sentence says the other two refusals name their repair: the `feat:` error at `:326-340` names the rename and the re-cut, and the `L \ D` error at `:256-265` names `gh issue edit` (read). `changelog.md:3` and `:9` carry the clause in round 1's wording (read), and 68ee8eea brought scenario S2 at `frame/design.md:41` to the same reading (read). The redirected repository name still exits 0 with an `M` line reading "none" (design G9); the `to` closes that path by reading `REPO` from `gh repo view`, and *Scope* puts the script's defect out of this work item.

```seal
confirms: none
```
What matched: bebc807e holds `trail/rounds/round-1.md` alone and adds the two close blocks and nothing else; no line of round 1's findings changed (executed: `git show --stat bebc807e`; read, its diff). 99642896's new row in `frame/plan.md` *Judgments of the run* cites `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer*, and that section has the orchestrator fold a frame statement the fix pass names, in a commit of its own (`skills/code-review/orchestration.md:78-82`, read). The row lists 99642896's folds. S2 and the A2 failure cell came later, in 68ee8eea, and I read them in that commit's diff rather than taking its message for them.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format at `68ee8eea`. The fix pass changed records only, and no hand-back in this range claims the suite passed, so the `unverified` label stands honest: no agent runs them (contract rule 2) | the branch at `68ee8eea` | the orchestrator, through `seal gate`, before the sealer's spawn |
| Whether 0.27.3's release pull request runs `tests` once, with no `pull_request` run before the last merge (design S2, `frame/questions.md` Q1), carried from round 1 | `gaps.md:7` | the orchestrator of 0.27.3's release, with `gh run list --branch release/v0.27.3` after the merge into `main` |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -s tests/test_tmp_round2_rule_change.py tests/github/test_rules.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_the_set_a_work_item_always_has.py`, in a scratch clone at `68ee8eea` | 126 passed, exit 0. The `test_tmp_` case asserted that `skills/settle/scripts/rule_changes.py#parse` reads the design as one `change` with no error and no unread line, that `#pattern` finds the `from` inside `#section_lines` of *5. The release pull request* at `5f0cf7a7` and does not find the `to` there, and that no line of the `to` is wider than 88 columns. The probe and the clone were deleted after the run |
| `awk` over `frame/design.md:62-92`, the indent taken off each line of the `to` | widest line 76 columns, at line 78 |
| `git grep -n -i -E` for references to a sentence of the `to` by position (`last sentence`, `new sentence`, `bold sentence`, `first sentence`) and to the check reading red (`red milestone`, `goes red`, `is red`, `reads red`), over the work item outside `round-1.md` | `frame/design.md:98` and `frame/design.md:99` |

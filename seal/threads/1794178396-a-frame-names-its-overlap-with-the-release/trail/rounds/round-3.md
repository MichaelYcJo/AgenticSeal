# Review round 3: 1794178396-a-frame-names-its-overlap-with-the-release

```seal
target: ffe97115, fixes 63a55797..ffe97115
```

This is the verifying round over round 2's fix pass, `ea6fa689` and `da6e2bc3`, and over the orchestrator's commits around it: `63a55797` commits round 2's record, `1200d2c1` folds round 2's findings into the frame, `894fbddb` commits the close blocks, and `ffe97115` folds the fix pass's departure clause into *Scope* item 4 (executed: `git log` and `git diff --stat 084ec22b ffe97115`). The base is `release/v0.36.0` at `94d04d30`. The round was worked in a `git clone --no-local` of the branch worktree at `ffe97115`. `seal/parity.md` is absent, and `seal/config.md` has no `Pact` row and no `Record language` row, so no parity comparison applies and the record is English.

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/rounds/round-1.md` and `trail/rounds/round-2.md` whole at `ffe97115`. The issue has no comments, as the spawn prompt states; this round did not re-run `gh issue view 1443`.

Carried from earlier rounds and not re-established: the `94d04d30` coordinates of `frame/design.md` *Grounding* and `frame/plan.md` *Technical context*, which round 1 opened at that commit and which no commit since has changed; phase 1's seen-red result for `test_the_plan_template_carries_the_overlap_table`, whose case file no commit since round 1's target touches; and the map of rewritten hashes in round 2's orchestrator's note, whose old commits this clone does not hold. Re-opened this round: `skills/implement/orchestration.md:376-416`, the whole paragraph, and `docs/releasing/branch-and-release.md:30-42`, the policy the carrier rule answers to.

**The carrier rule holds in every sentence of the paragraph.** The spawn prompt asked whether each sentence of `skills/implement/orchestration.md` holds the rule's two conditions: the carrier is an item no plan orders after another, and the carrier merges before every other item. The paragraph runs from line 376 to line 416, three lines past the 376 to 413 the fix pass's close names. Lines 414 to 416 hold the sentence on `main`, which the close names by its words, so its read covered them. This round read each sentence against both conditions:

- Lines 376 to 386 say the version moves in the first pull request into the branch, by the party that writes "that work item's" changelog entry, and that the orchestrator chooses the carrier. This matches `docs/releasing/branch-and-release.md:30-42`, which this work leaves unchanged (executed: `git diff --quiet 94d04d30 HEAD -- docs/` exited 0).
- Lines 391 and 392 merge the items in the order the plans state. No plan orders the carrier after another item, so merging it first keeps that order.
- Lines 392 to 396 cover two plans that disagree or a first item that stalls. The orchestrator now chooses "with the item that carries the move still first". Where two plans state opposite orders for a pair, each item of the pair is ordered after the other by one plan, so neither can be the carrier, and "still first" keeps a third item ahead of both. Where the stalled first item is the carrier, the clause keeps the stated order. No item then merges out of it, and the sentence's row goes to "the plan of the item it merges out of the stated order", so no row is owed. Scenario S4 (`frame/design.md:52`) names the same plan.
- Lines 396 to 401 give the move to an item no plan orders after another, merge it before every other item, and let unordered items merge as each is sealed once it has landed.
- Lines 401 to 404 fold the move into "that work item", the carrier.
- Lines 404 to 409 hold the fallback. It is "another item that no plan orders after another", so it meets the first condition. "The move goes to" makes it the item lines 396 to 399 merge before every other item, so it meets the second.
- Lines 409 to 416 cover a repository that moves the version at the release, and `main`. Neither names a carrier.

`changelog.md:3` holds the same carrier and adds "whatever order it chooses for a pair". `changelog.md:6` and `changelog.md:13` state the carrier as the paragraph does. *Scope* item 4 (`frame/design.md:34`) now holds every sentence of the paragraph, including the departure clause `ffe97115` folded and the fallback `1200d2c1` folded. No other statement of the fallback stands in the tree (executed: `git grep -n -E` for "next item whose rounds", "rounds have already ended", "carries the move", "still first" and "item first in", outside the round records).

This release's other plans do not put #1443 behind another item, so #1443 still meets the paragraph's first condition as the carrier. Each plan was read as its sibling worktree held it on 2026-11-09. `seal/threads/1794178395-a-fold-is-read-before-the-next-round/frame/plan.md:17` on #1442's branch says "#1443 should merge first". The plans of #1439, #1440, #1441 and #1444 order nothing against #1443. Their disagreement with this plan's overlap rows is a row of *Not judged* below.

**The routing commit `305055a8` carries no `Seal-Routing` trailer.** It is the orchestrator's commit that adds `routing.md`, before round 1's target, and its message ends with the co-author line alone (executed: `git show --stat 305055a8`). `skills/commit-pr-convention/SKILL.md:185-187` says a session's commit at a shared root ends with one. `skills/code-review/scripts/chain_check.py` `trailer_findings` judges only the trailers a commit carries. So a commit with none is read as a person's, as `docs/checks/the-routing-check.md` *A session that declares nothing is not caught* states, and nothing refuses the pull request for it. This is no finding, as round 2 judged of the two short trailers. A trailer is no file a fix commit touches, and the branch's commits do not reach `release/v0.36.0`, which takes a feature branch by squash (`docs/releasing/branch-and-release.md:205`). The orchestrator answers whether to rewrite it.

## Findings

None. The round found no defect in the fix diff, and no sentence of the records that state the present is contradicted at `ffe97115`.

## Confirmations

```seal
confirms: round-2#1
```
What holds: `skills/implement/orchestration.md:404-409` match round 2's paste-ready block line for line (executed: a read-only Python comparison of the block against those six lines printed True). The fallback carrier is an item no plan orders after another, and where no such item is, the chosen item takes the move and the verifying round it owes. The sentence round 2 reopened no longer lets an item ordered after another carry the move. The fix pass's account of the paragraph was read as a claim and holds, as the sentence-by-sentence reading above shows. One part is off: it gives the range as 376 to 413, and the paragraph ends at 416. `ea6fa689` and `da6e2bc3` change no Python file (executed: `git show --stat` lists `changelog.md` and `skills/implement/orchestration.md` for the first and `gaps.md` for the second).

```seal
confirms: round-2#2
```
What holds: `frame/design.md:51` is round 2's S3 row word for word (executed: the same Python comparison printed True). S3's Then now gives the move to an item no plan orders after another and merges that item before every other item, which `skills/implement/orchestration.md:396-399` says.

What matched: the *Judgments of the run* row `1200d2c1` adds (`frame/plan.md:60`) describes `1200d2c1` and `ffe97115`. Its quoted clause "with the item that carries the move still first" stands at `frame/design.md:34` and `skills/implement/orchestration.md:394`. Read.

What matched: the `gaps.md` *Not verified* first row (`gaps.md:7`), amended in place by `da6e2bc3`, says the fix passes of rounds 1 and 2 each ran the plan row's three modules and `tests/behaviour/test_docs_line_wrap.py`. The same four modules were re-run here, and 149 passed (executed, under *Probes*). The row also says neither pass changed a Python file, which `git show --stat` confirms. The row keeps the full suite, the lint and the format check `unverified`, with the orchestrator at the broad gate as their answerer, so the label is honest. No row left the memo.

What matched: each of the six quotes in `pr.md` stands at the file its coordinate names, word for word with runs of whitespace collapsed. The third quote is the departure sentence of `changelog.md:3`, which `ea6fa689` left as it stood (executed: a Python comparison over `changelog.md`, `frame/plan.md` and `gaps.md` printed True for each).

What matched: every commit from `94d04d30` to `ffe97115` except the routing commit `305055a8` carries `Seal-Routing: 1794178396-a-frame-names-its-overlap-with-the-release` (executed: `git log` over the trailer). None of the two short trailers round 2 found is left after the rewrite its orchestrator's note names.

What matched: the fix diff adds no test, so no new case is read against its group, and `frame/design.md` *Rule changes* still holds the no-change block. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether this plan's overlap rows match the siblings' frames, which now stand. The siblings disagree with two rows. #1440's plan (`seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/plan.md:49` on its branch) says #1440 does not edit `agents/framer.md`, so it does not meet this work, but this plan's row says it does. #1444's plan (`seal/threads/1794178397-a-durations-refresh-costs-no-round/frame/plan.md:18` on its branch) says #1444 shares no file with #1443, but this plan's row names `skills/code-review/orchestration.md`. The rows are labelled `unverified` and dated to before those frames stood (G16), so the target does not contradict them. | `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/plan.md:36-44` | the orchestrator, reading the six plans, as `frame/design.md` G16 names |
| The full suite, the repository-wide lint and the format check at `ffe97115`; contract rule 2 keeps them out of a round | `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/gaps.md:7` | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_the_set_a_work_item_always_has.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py -q -p no:randomly`, in the clone at `ffe97115` | exit 0, 149 passed |
| A read-only `python3` comparison in the clone at `ffe97115`: each `pr.md` quote against its source with whitespace collapsed, round 2's first block against `skills/implement/orchestration.md:404-409`, and round 2's second block against `frame/design.md:51` | printed True for all eight |
| `git log --format='%h %(trailers:key=Seal-Routing,valueonly)' 94d04d30..ffe97115`, in the clone | 17 commits carry the full work item id; `305055a8` carries none |

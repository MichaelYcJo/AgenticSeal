# Review round 2: 1793541310-a-band-flags-a-row-and-a-judgment-decides

```seal
target: 1b392135, fixes 3afdefad..1b392135
```

This is a verifying round. The target is the diff of round 1's fixes, `3afdefad..1b392135`: the orchestrator's routing row (`c81dafcf`), the framer's fold of round 1 into the frame (`25295dfe`), the fix pass's `changelog.md` and `gaps.md` (`efbac823`), and the four close blocks (`1b392135`). The diff touches only the work item's own records. The fourth `change`, to `docs/release-checklist.md` *2b. Settle what earlier releases left behind*, is policy no earlier round read, so it is reviewed here as new.

Facts carried from round 1 and not re-established: G9's three readers, #1259's close and title, and the #51 edit (G7, G8). The fix diff does not touch them. Facts re-established this round: every section span, every `from`, the absence of every `to`, #1258's stacking on *5*, and the citation of the new bold lead. The probe in `## Probes` read all of them again. The release branch has moved to `361ed0cb` (#1274). That move changes none of `docs/release-checklist.md`, `docs/measuring-a-run.md`, `docs/README.md` or `evals/README.md` (executed: `git diff cd694aa3 origin/release/v0.27.3` over the four files prints nothing).

## Findings

### 1. The new *2b* `to` sends a records-alone count to a weighing that decides `worse`, then makes #1020's check depend on a finding that weighing never makes, and the `add` has the settling session file an issue on a question #1020 already holds open

```seal
severity: should
location: `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:121-131`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:23`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:55`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:82-84`
evidence: executed `gh issue view 1020 --json title,state,stateReason,closedAt`, `python3 .github/scripts/finding_counts.py --released-at HEAD --root .`
regression: round-1#1
```

Why it matters: the unit is the fourth operation of `frame/design.md` *Rule changes*, lines 121 to 131. It is the `change` to *2b* that `25295dfe` added, with its grounds G17 and its scenario S5. *Scope* item 6 says the sentence "becomes a row for item 1's judgment". The fix wrote a `to` that does that and then makes #1020's check depend on whether "the weighing finds the records still restate one another". The defect came from round 1's own paste-ready `to` for finding 1, which the fix took almost word for word.

The `add` says what the weighing holds and what it decides. It holds "the change that moved it, what that change cost, what it bought, and the record each stands in". It decides `worse` or not: "The reading is `worse` only where the cost outweighs what was bought" (`frame/design.md:75-78`). Nothing in it finds whether records restate one another. So the settling session weighs the count as `worse` or not, then meets a condition its weighing did not answer. It can take two readings:

- `worse` means the records restate one another, so #1020's check is next. Then the `add`'s "An issue follows a reading judged `worse` so, filed by the orchestrator or the settling session" (`frame/design.md:82-84`) applies too, and the session files a new issue. #1020 is open, titled "...a check reads the recurrence and owes the whole class" (executed). The new issue restates #1020. Its reader pays a reading and a close, the cost the `add` says it removes.
- Restatement is a second question beside the weighing. Then a count judged not `worse` can still send the session to #1020. A count judged `worse` with no restatement files an issue under the `add`, and #1020 goes unnamed.

"Does not fall" also covers a count equal to the last release's. The `add` weighs "a reading past its band toward more cost", and its weighing opens with "the change that moved it". A count that stayed level did not move. So under the `add` it owes nothing, and under *2b* it is a row for the judgment.

G17 places the sentence in the class on a wrong fact: "this work item's four round 1 findings all lie in its own records". `finding_counts.py` counts a finding as records-alone only where every path on its `location:` line lies under `seal/threads/`. It reads this work item as 4 findings and 1 in records alone (executed). Round 1's findings 1 to 3 also name `docs/release-checklist.md`, `evals/README.md` and `skills/verify/orchestration.md`. G17's conclusion holds on other grounds. The one records-alone finding, round 1's finding 4, is about a missing reader and restates nothing. The example as written measures the count by a rule the count does not use.

The `to` also opens "The count has no band". The paragraph before it names four numbers, so "the count" has no single referent until the clause after it.

```markdown
The fourth operation's `to`, whole:
  to: A records-alone count that does not fall is a row for the
    judgment `docs/measuring-a-run.md` *A band flags a reading for
    judgment, and a judgment decides whether it is worse* asks, and no
    verdict: a release's mix of work moves the count as well as
    restatement does. The settling session's comment names the work
    items whose records-alone findings kept the count up, and says
    whether those findings restate one another. The count is `worse`
    only where they do. #1020's check is then the next step, and #1020
    is the issue that follows, so the session files no other.

G17, the sentence "The count has no band, and a release's mix of work
moves it: this work item's four round 1 findings all lie in its own
records.", replaced by:
  The count has no band, and a release's mix of work moves it: this
  work item's round 1 reads four findings and one in records alone
  (executed: `python3 .github/scripts/finding_counts.py --released-at
  HEAD`), and that one, finding 4, is about a missing reader and
  restates nothing.

S5's Then cell, from "then its comment weighs the count" to the cell's end:
  then its comment names the work items whose records-alone findings
  kept the count up and whether those findings restate one another;
  the count is `worse` only where they do, and #1020's check is then
  the next step, with no other issue filed
```

`changelog.md` describes the old *2b* sentence and names *2b* among the sections the settle cites the rule from. Both stay true under this fix, so the entry needs no change.

### 2. `plan.md`'s Phase 1 row still verifies one `add` and two `change` operations, and the sentence that widens its search stands beside it, so the cell's search, run as widened, contradicts the cell's own claim

```seal
severity: should
location: `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/plan.md:43`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/plan.md:11`
evidence: executed `git grep -n -i -E 'issue it opens|that grew|does not fall' -- ':!seal/threads'`, `bin/test tests/behaviour/test_tmp_round2_rule_changes.py -q -s -p no:xdist`
regression: round-1#1
```

Why it matters: the unit is `frame/plan.md` as `25295dfe` changed it. *Technical context* gained the fourth operation and a sentence on how the fix pass confirms it (line 11). The Phases row for Phase 1 (line 43) stayed as it was. *Scope* item 6 adds a fourth operation, and the fix rewrote every other sentence on the operation count (G15, S4, *Technical context*) but not the row's Verified-by cell. The defect came from writing the widened check beside the cell instead of in it.

The cell says `rule_changes.py#parse` "returns one `add` and two `change` operations". The design now parses as one `add` and three `change` (executed, the probe). The cell says its search "lists only `docs/release-checklist.md`". *Technical context* says the fix pass ran "the search of Phase 1's Verified-by cell, with `does not fall` added to the search". Run that way, the search also lists `tests/skills/test_unverified_check.py:2206` and `tests/text/test_ci_gives_the_checks_what_they_need.py:613` (executed). So the cell's claim fails under either reading. Its narrow list lacks `tests/github/test_finding_counts.py`, which the fix pass added. Its Delivers cell names *Scope* items 1 to 3 and 5, and no row names item 6.

The sealer reads `frame/plan.md` against the phase records and the last round (`agents/sealer.md` step 4, *The parties against each other*). It will find the plan saying two `change` and the design saying three. The prompt that spawned this round says the fix pass noted the mismatch. None of round 1's four close blocks carries that note, so the sealer has no record to read it from. Contract rule 19 names this shape: "A correction written beside the sentence it corrects leaves both for the next reader to choose between."

```markdown
plan.md, the Phases row for Phase 1:
| 1 | *Scope* item 4. It confirms items 1 to 3 and 5 at the build's head, and the fix pass over round 1 confirms item 6 | `rule_changes.py#parse` on `frame/design.md` returns one `add` and two `change` operations at `6718f5de`, and one `add` and three `change` after round 1's fold, with no error, and `#pattern` finds each `from` in `#section_lines` of its section, run once as a `test_tmp_*` probe and deleted. `git grep -n -i -E 'issue it opens\|that grew\|does not fall'` outside `seal/threads/` lists `docs/release-checklist.md` and, for `does not fall`, two test lines that use the words for something else: `tests/skills/test_unverified_check.py:2206` and `tests/text/test_ci_gives_the_checks_what_they_need.py:613`. Narrow: `tests/github/test_rules.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/behaviour/test_release_hygiene.py`, `tests/github/test_publish_release_note.py`, `tests/text/test_a_record_carries_no_comment.py` and `tests/github/test_finding_counts.py`, the modules that read a pending design, a work item's set, a changelog fragment or the counts *2b* reads | 6718f5de |

plan.md *Technical context*, the end of the sentence that opens "Phase 1
closed before round 1":
  ..., which also confirms them by Phase 1's Verified-by cell.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: G5 (`frame/design.md:11`) now builds the producer list from `git ls-files` over the shipped script directories and names `.github/scripts/finding_counts.py` and `.github/scripts/durations_union.py`. *2b*'s sentence is placed in the class with a fourth operation. The method is contract rule 12's first, from what produces the defect, and it no longer rests on memory. As a check, executed: `grep -c -i -E 'baseline|last (release|tag|run)|previous|earlier reading|against the (last|base)|grew|shrank|delta'` over every shipped `.py` under `.github/scripts`, `skills/*/scripts`, `evals/scripts` and `hooks`. Each file it hit was read at its docstring. `roll_flow_measurement_issue.py`, `mutation_check.py`, `unverified_check.py`, `arm_check.py` and `chain_check.py` use those words for a log's version, a mutation's baseline run or a base commit. None of them sets a reading beside an earlier one. That grep is a sample over words, and it found no producer G5 lacks. `hooks/` lies outside G5's `git ls-files` patterns, and none of its scripts produces such a number. The text of the new operation is finding 1 of this round.

```seal
confirms: round-1#2
```
What holds: G10 (`frame/design.md:16`) places pass rules 2 and 5 outside the class with `FALSE_MARGIN = 0.05` and `TOKEN_MARGIN = 0.07`. Those values stand at `evals/scripts/noninferiority.py:102` and `:108` (executed: `grep -n "MARGIN\s*="`). The `add` carries the sentence that a margin a claim fixes before its run is not a band (`frame/design.md:71-75`, read). *Out* names rules 2, 4 and 5.

```seal
confirms: round-1#3
```
What holds: the `add` (`frame/design.md:63-90`, read) no longer names `--says`. Its places for the weighing are a release pull request's body, the settling session's `flow-baseline` comment and a measuring work item's phase record. *Out* names the `--says` sentence with G18 as its grounds (`frame/design.md:44`). The only other `--says` in the design is G9's quotation of `seal cost` (`frame/design.md:15`), which states a fact and places no weighing.

```seal
confirms: round-1#4
```
What holds: the `add`'s last line reads `check: none reader: the proofer at review and the owner before a release or settle pull request's merge` (`frame/design.md:90`, read). Its value holds no comma, `::` or em dash. G18 names which reader reads which place. *5* keeps its two modules.

```seal
confirms: none
```
What matched: the fix pass's probe claim, the frame's G15 and S4 (`frame/design.md:21`, `:54`). Executed in this round's probe: `rule_changes.py#parse` reads one `add` and three `change`, with no error, no unread line and no no-change block. `#section_lines` places *What a measurement must survive, and what it must not invent* at lines 50 to 78, *5. The release pull request* at 105 to 165, *2b. Settle what earlier releases left behind* at 31 to 103 and *The checks* at 33 to 44. Each `from` is found once in its section, and no `to` is in its file. The widest prose line of the three rule `to` values is 71, 70 and 67 columns. #1258's `change` was applied first and these four after it. Every `from` was still found. Both citations of the new bold lead, at lines 80 and 160 of the applied `docs/release-checklist.md`, resolve under `tests/behaviour/test_a_cited_section_stands_in_its_file.py#resolves`. The widest applied line of *2b* is 87 columns, within the 88 of `tests/behaviour/test_docs_line_wrap.py`.

```seal
confirms: none
```
What matched: G17's claim that no other pending design names *2b* (`frame/design.md:23`). Executed: `grep -n "section: 2b"` over the three `seal/threads/*/frame/design.md` finds only this design. #1258's G5 names `1793521559-a-finding-is-counted-once` as changing *2b*. That directory left the tree with the 0.27.x settle, `14bfd992` (executed: `git log -- seal/threads/1793521559-a-finding-is-counted-once`), before the base.

```seal
confirms: none
```
What matched: the fix pass's narrow run and its search. Re-run at `1b392135` in this round's clone: the 13 modules of `trail/phases/phase-1.md` *The phase-boundary run* and `tests/github/test_finding_counts.py`, one `bin/test -q`, 974 passed, exit 0 (executed). The search lists `docs/release-checklist.md:79`, `:131` and `:132` and the two test lines the close names (executed).

```seal
confirms: none
```
What matched: `changelog.md:3` and its process row (`changelog.md:9`, read) against the folded frame. The entry names the three places for the weighing and the two readers. It describes the records-alone count as `finding_counts.py` counts it. It says the behaviour suite's pass rules stay as they are, and names *2b* and *5* as the sections the settle cites the rule from. `gaps.md:9`, the new row for the first settle under the rule, names the settling session and the owner as its answerers (read).

```seal
confirms: none
```
What matched: the `unverified` label on the full suite, the lint and the format check. `gaps.md:7` names the orchestrator's `seal gate` as the answerer, and no record claims a passing suite (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `1b392135` | the branch | the orchestrator, by `seal gate` |
| Whether 0.27.3's release pull request body weighs each grown row and opens an issue only for one judged `worse` (S3) | the release pull request, not yet open | the orchestrator that writes the body, and the owner before the merge |
| Whether the settle after 0.27.3 weighs its records-alone count in its `flow-baseline` comment as *2b* asks (S5) | the settle after 0.27.3 | the settling session, and the owner before the settle pull request's merge |
| #1258's G5 still names `1793521559-a-finding-is-counted-once` as a pending change to *2b*, and the settle removed that directory before the base. That design is outside this target | `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/design.md:11` | the orchestrator, at #1258's next round or its sealer |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_tmp_round2_rule_changes.py -q -s -p no:xdist`, in a `git clone --no-local` at `1b392135` under `<scratchpad>/1793541310-a-band-flags-a-row-and-a-judgment-decides/round-2/`. The file parsed both pending designs with `rule_changes.parse`, read each section and `from` before any change, applied #1258's `change` and then this design's four operations in merge order, and resolved each citation of `docs/measuring-a-run.md` with the cited-section test's own reader | First run: exit 1, a `KeyError` in the probe's own file key, after the before-change readings had printed. The key was corrected and the file ran a second time: 1 passed, exit 0. Four operations, no errors. Each section was found once and each `from` once, and no `to` stood in the tree. Both citations resolve after the `add`. The widest applied *2b* line is 87 columns. The file was deleted after the second run |
| `bin/test -q` over the 13 modules of the phase-boundary run and `tests/github/test_finding_counts.py`, in the same clone | 974 passed, exit 0 |
| `python3 .github/scripts/finding_counts.py --released-at HEAD --root .`, in the same clone | exit 0. This work item reads 4 findings, 0 with a regression or reopens line, 1 in records alone, 1 round |
| `git grep -n -i -E 'issue it opens\|that grew\|does not fall' -- ':!seal/threads'`, in the same clone | five lines: `docs/release-checklist.md:79`, `:131`, `:132`, `tests/skills/test_unverified_check.py:2206`, `tests/text/test_ci_gives_the_checks_what_they_need.py:613` |
| `gh issue view 1020 --json title,state,stateReason,closedAt` | `OPEN`, not closed |

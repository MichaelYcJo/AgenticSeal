# Review round 3: 1793541310-a-band-flags-a-row-and-a-judgment-decides

```seal
target: 585c6b05, fixes 9c75a7fa..585c6b05
```

This is a verifying round. The target is the diff of round 2's fixes, `9c75a7fa..585c6b05`: the orchestrator's routing row (`83e8b232`), the framer's fold of round 2 into the frame (`5e841a17`, which touches `frame/design.md` and `frame/plan.md`), the fix pass's `changelog.md` and `gaps.md` (`71410b52`), and the two close blocks (`585c6b05`). The diff touches only the work item's own records. The merge base is still `cd694aa3` (executed: `git merge-base HEAD origin/release/v0.27.3`).

Facts carried from rounds 1 and 2 and not re-established, because the fix diff does not touch them: G5's producer list, G9's three readers, G10's margins at `evals/scripts/noninferiority.py:102` and `:108`, #1259's close, the #51 edit (G7, G8), and #1258's `change` covering only the first paragraph of *5* (G3). Facts re-established this round: every section span, every `from`, the absence of every `to`, the citations of the new bold lead after all five operations apply, G17's count, and the state of #1020 and #1148. The probe in `## Probes` read them.

Whether the fixes converge. Round 1 found four findings, in the substance of the frame's rule changes. Round 2 found two, both in text round 1's fix wrote, and both in the work item's records alone. This round finds one, in one clause of the *2b* `to` and the five records that copy it. The count falls each round, and each finding is narrower than the last; none reopens a choice the design made. One pattern recurs, and the orchestrator should weigh it: round 2's finding 1 came from round 1's paste-ready `to`, and this round's finding 1 came from round 2's. Each time the framer took the proofer's paste as written. The paste-ready fix below changes one clause and its copies, and was measured against the 76-column rule G14 states.

## Findings

### 1. The *2b* `to` asks whether the records-alone findings "restate one another", and calls that the cost #1148 removed; #1148 removed records restating one another, and the two readings give different verdicts on this work item's own count

```seal
severity: should
location: `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:132-135`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:23`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:35`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:55`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:143`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/changelog.md:3`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/changelog.md:9`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/gaps.md:9`
evidence: executed `gh issue view 1148 --json title,state,stateReason,closedAt,body`, `gh issue view 1020 --json title,state,stateReason,closedAt`, `python3 .github/scripts/finding_counts.py --released-at HEAD --root .`
regression: round-2#1
```

Why it matters: the unit is the fourth operation's `to` in `frame/design.md` *Rule changes*, lines 126 to 136, as `5e841a17` rewrote it for round 2's finding 1. The frame says the count measures #1148, "which removed the records' copies of one another" (`docs/release-checklist.md:76-77`, the paragraph the `from` stands in), and the old sentence and the round-1 `to` both judged whether "the records still restate one another"; the fix asks instead "whether those findings restate one another" and calls that "the cost #1148 removed"; the defect came from round 2's paste-ready `to`, which first moved the subject from records to findings, as round 2's own defect came from round 1's paste.

The sentence a settling session reads after the settle is: "The settling session's comment names the work items whose records-alone findings kept the count up, and says whether those findings restate one another, the cost #1148 removed. The count is `worse` only where they do." It has two readings, and a settling session acts on whichever it takes:

- Each finding stands on one record restating another: a copy that fell out of step with its source. This is the cost #1148 removed. #1148's body names its instances: "a plan cell restating the design, a phase record or `gaps.md` quoting a design sentence a fold had changed" (executed: `gh issue view 1148`, closed `COMPLETED` on 2026-10-31).
- The findings restate one another: one finding repeats another, which is recurrence. #1020, the issue the `to` names next, is titled "when one kind of finding recurs across review rounds, each fix pass fixes one instance and the next round finds the next" (executed: `gh issue view 1020`, `OPEN`). So the words "findings restate one another" read naturally as #1020's subject.

The two readings give different verdicts on this work item. `finding_counts.py` reads it as 6 findings, 3 in records alone (executed): round 1's finding 4, and round 2's findings 1 and 2. Round 2's finding 2 is a plan cell that still stated the operation count the design had changed (`trail/rounds/round-2.md`, finding 2). That is #1148's first named instance. Under the first reading, the work item holds one restatement finding, and its records-alone findings count toward `worse`. Under the second, none of the three repeats another, and they do not. The appositive "the cost #1148 removed" points to the first reading, while the words before it state the second. A rule the settle writes into `docs/release-checklist.md` *2b* is policy an agent reads and acts on, so it needs one reading (`skills/core/SKILL.md` *Each agent judges its own target, independently of the others*, the last sentence).

The class, listed by taking the work item's records apart into each sentence that names what the settling session judges at *2b* (a `grep -n` for `restate` over `frame/design.md`, `frame/plan.md`, `changelog.md` and `gaps.md`, with each hit read at the sentence, and the `to`'s wrapped lines read by eye): the `to` (`frame/design.md:132-135`), *Scope* item 6 (`:35`), S5 (`:55`), the *Removes* row (`:143`), G17's "finding 4 ... restates nothing" (`:23`), the changelog entry (`changelog.md:3`), its process row (`changelog.md:9`), and `gaps.md:9`. `frame/plan.md:36` (A11) says "whether or not the records restate one another", which is the first reading, and stands. The quotations of the old sentence at `frame/design.md:23`, `:125` and `:143`, and `changelog.md:3`'s "said the records still restated one another", quote text that was there before and stand.

```markdown
frame/design.md, the fourth operation's `to`, whole (widest line 73 columns):
  to: A records-alone count that does not fall is no verdict. #1148 is
    measured by this count falling, so a count that holds level is read
    as one that rose: it is a row for the judgment
    `docs/measuring-a-run.md` *A band flags a reading for judgment, and a
    judgment decides whether it is worse* asks, because a release's mix
    of work moves the count as well as restatement does. The settling
    session's comment names the work items whose records-alone findings
    kept the count up, and says whether each of those findings stands on
    one record restating another, the cost #1148 removed. The count is
    `worse` only where one does. #1020's check is then the next step, and
    #1020 is the issue that follows, so the session files no other.

frame/design.md G17, "and that one, finding 4, is about a missing reader
and restates nothing." becomes:
  and that one, finding 4, is about a missing reader and stands on no
  record restating another.

frame/design.md Scope item 6, S5, the Removes row, changelog.md:3,
changelog.md:9 and gaps.md:9: each "the findings that kept it up restate
one another" or "whether those findings restate one another" becomes
"a finding that kept it up stands on one record restating another" or
"whether each of those findings stands on one record restating another",
and each following "only where they do" becomes "only where one does".
```

## Confirmations

```seal
confirms: round-2#2
```
What holds: `frame/plan.md:43`, the Phases row for Phase 1, now delivers *Scope* item 4, confirms items 1 to 3 and 5 at the build's head, and names the fix pass over round 1 for item 6. Its Verified-by cell says one `add` and two `change` at `6718f5de` and one `add` and three `change` after round 1's fold. That matches `trail/phases/phase-1.md:9` and the probe in `## Probes`. Its search with `does not fall` lists `docs/release-checklist.md` and the two test lines it names, `tests/skills/test_unverified_check.py:2206` and `tests/text/test_ci_gives_the_checks_what_they_need.py:613` (executed). Its narrow list holds `tests/github/test_finding_counts.py`. *Technical context* (`frame/plan.md:11`) no longer states a widened check beside the cell (read).

The close: the fix pass says its own commit fixed nothing here, and that is true. `71410b52` touches `changelog.md` and `gaps.md` only, and its change to `changelog.md` is finding 1's (executed: `git show --stat`). The repair is `5e841a17`, which touches `frame/plan.md`, the path the finding's `location:` names. So `verdict: fixed 5e841a17`, with no `location:` line in the close, is the form `docs/the-review-record.md` *The round record* gives: "A repair a commit made ... closes `fixed <commit>`". The chain check would pass on it too. As written, the verdict names a commit that did not repair this finding, and the close's `location:` names `changelog.md`, which is not where this fix went. The close's `answer:` states both facts in words and names `5e841a17`, so a reader of the close reaches the commit that did the repair. The defect itself does not stand, so this round confirms the close and raises no finding on its coordinates. The round records leave the tree at the settle, and `finding_counts.py` does not read a close block. Judged against `skills/core/SKILL.md` *The first value*: a fix pass and a fourth round to change one SHA in a record the sealer reads whole would cost more than they catch.

```seal
confirms: none
```
What matched, from round 2's finding 1, the parts the regression above leaves standing: the `to` no longer sends the count to a weighing that cannot answer its condition, because the comment now names the work items and judges them. A count that held level is read as one that rose, on #1148's measure, so the `add`'s "the change that moved it" has an answer at *2b* (G17, read). The `to` names #1020 as the issue that follows and says the session files no other. The `add`'s "An issue follows a reading judged `worse` so, filed by the orchestrator or the settling session" (`frame/design.md:82-84`) still stands, and *2b*, which cites it, names the issue that follows as one already filed. So the two read as one rule and its case. The changelog's "with one exception at the settle" (`changelog.md:3`) says the same. "This count" in the `to`'s second sentence has one referent. G17's count reads 6 findings, 3 in records alone, over 2 rounds, and round 1 holds 1 of its 4 (executed, `## Probes`).

```seal
confirms: none
```
What matched: G15, S4 and `frame/plan.md` *Technical context* (claimed: four operations, each `from` in its section, no `to` in the tree, the citations resolve, the widest rule `to` line 71 columns). Executed in this round's probe at `585c6b05`: `rule_changes.py#parse` reads one `add` and three `change` operations from this design, with no error and no unread line, and #1258's design with none either. `#section_lines` places *What a measurement must survive, and what it must not invent* at lines 50 to 78, *5. The release pull request* at 105 to 165, *2b. Settle what earlier releases left behind* at 31 to 103 and *The checks* at 33 to 44. Each `from` is found once in its section, and no `to` is in its file. The widest prose lines of the `to` values are 71, 70 and 69 columns, and the index row of 128 is a table row. #1258's `change` was applied first, then these four. Both citations of the new bold lead resolve under `tests/behaviour/test_a_cited_section_stands_in_its_file.py#resolves`, at lines 82 and 165 of the applied `docs/release-checklist.md`. The widest applied line of *2b* is 87 columns, the line the `from` began on. The sentence after the `to` reads "The step is this repository's and ships to no user", as it did before.

```seal
confirms: none
```
What matched: `changelog.md:3` and its process row (`changelog.md:9`) against the folded frame, apart from the clause in finding 1. The entry states the settle's case: a level count read as one that rose, and #1020, already open, as the issue that follows, with no other filed. That matches the `to`, *Scope* item 6, S5 and the *Removes* row. `gaps.md:9` asks what S5 asks, and names the settling session and the owner as its answerers (read). `frame/plan.md`'s second *Judgments of the run* row names its grounds and the document it stands on (read).

```seal
confirms: none
```
What matched: the fix pass's narrow run, and the `unverified` label. Re-run at `585c6b05` in this round's clone: the plan's seven narrow modules, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/skills/test_unverified_check.py` and `tests/behaviour/test_a_phase_hands_the_next_one_a_record.py`, one `bin/test -q`, 655 passed, exit 0 (executed). `gaps.md:7` names the orchestrator's `seal gate` as the answerer for the full suite, the lint and the format check, and no record claims a passing suite (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `585c6b05` | the branch | the orchestrator, by `seal gate` |
| Whether 0.27.3's release pull request body weighs each grown row and opens an issue only for one judged `worse` (S3) | the release pull request, not yet open | the orchestrator that writes the body, and the owner before the merge |
| Whether the settle after 0.27.3 weighs its records-alone count in its `flow-baseline` comment as *2b* asks (S5) | the settle after 0.27.3 | the settling session, and the owner before the settle pull request's merge |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_tmp_round3_rule_changes.py -q -s -p no:xdist`, in a `git clone --no-local` at `585c6b05` under `<scratchpad>/1793541310-a-band-flags-a-row-and-a-judgment-decides/round-3/`. The file parsed both pending designs with `rule_changes.parse`, read each section, `from` and `to` before any change, applied #1258's `change` and then this design's four operations in merge order, and resolved each citation of `docs/measuring-a-run.md` with the cited-section test's own reader | First run from outside the clone: exit 4, pytest found no file at the path given, and nothing ran. Second run: exit 1, on the probe's own assertion, which compared the bold lead without its closing period; the readings before it had printed. The assertion was changed to the test's own `resolves`, and the third run passed, exit 0, with the readings in the confirmation above. The file was deleted after the third run |
| `bin/test -q` over the ten modules named in the last confirmation, in the same clone | 655 passed, exit 0 |
| `python3 .github/scripts/finding_counts.py --released-at HEAD --root .`, in the same clone | exit 0. This work item reads 6 findings, 2 with a regression or reopens line, 3 in records alone, 2 rounds |
| `git grep -n -i -E 'issue it opens\|that grew\|does not fall' -- ':!seal/threads'`, in the same clone | five lines: `docs/release-checklist.md:79`, `:131`, `:132`, `tests/skills/test_unverified_check.py:2206`, `tests/text/test_ci_gives_the_checks_what_they_need.py:613` |
| `gh issue view 1020 --json title,state,stateReason,closedAt` and `gh issue view 1148 --json state,closedAt,stateReason` | #1020 `OPEN`; #1148 `CLOSED`, `COMPLETED`, 2026-10-31 |

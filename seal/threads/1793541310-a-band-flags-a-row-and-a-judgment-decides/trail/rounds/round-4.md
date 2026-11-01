# Review round 4: 1793541310-a-band-flags-a-row-and-a-judgment-decides

```seal
target: 85fa5858, fixes 0431ef33..85fa5858
```

This is a verifying round. The target is the diff of round 3's fixes, `0431ef33..85fa5858`. It holds four commits. `adbd6d33` is the orchestrator's row deciding to go on past round 3. `48e57eef` is the framer's fold of round 3 into `frame/design.md` and `frame/plan.md`. `85444c5f` is the fix pass's `changelog.md` and `gaps.md`. `85fa5858` is the close block. The diff touches only the work item's own records (executed: `git diff --stat 0431ef33..85fa5858`). The merge base is still `cd694aa3` (executed: `git merge-base HEAD origin/release/v0.27.3`). The pull request changes no path outside `docs/` and `seal/`, and no `seal/parity.md` is declared, so the round block has no `original:` line.

Facts carried from rounds 1 to 3 and not re-established, because the fix diff does not touch them: G5's producer list, G9's three readers, G10's margins at `evals/scripts/noninferiority.py:102` and `:108`, #1259's close, the #51 edit (G7, G8), #1258's `change` covering only the first paragraph of *5* (G3), and the `from` of every operation. Facts re-established this round: the parse of both pending designs, every section span, each `from` found once, the absence of every `to`, the two citations of the new bold lead after all five operations apply, the work item's finding count, and the state and bodies of #1020 and #1148. The probe in `## Probes` read them.

The verdict this round reaches on the new sentence, with its grounds, is in the first confirmation. The round finds nothing needing a fix.

## Findings

None.

## Confirmations

```seal
confirms: round-3#1
```
What holds: the fourth operation's `to` (`frame/design.md:126-139`) now has one reading of what the settling session judges of each finding. Round 3 found two readings: each finding stands on one record restating another, which is #1148's subject, or the findings repeat one another, which is #1020's recurrence. The fix names the thing judged and defines it: "A stale copy is a record that restates a fact another record holds and was left as it stood when that source changed; #1148 removed the records' copies of one another so that none could go stale. The settling session's comment ... says of each such finding whether it found a stale copy." The words "restate one another" no longer describe the findings, so the recurrence reading has nothing to attach to (read). In the definition, "that source" can only be the other record, the one holding the fact.

Read against the two issues (executed: `gh issue view 1148`, `gh issue view 1020`). #1148's body says "Each record restates facts another record holds, and keeping those copies consistent is most of what 0.24.0's review rounds did", and names its records-alone instances as "a plan cell restating the design, a phase record or `gaps.md` quoting a design sentence a fold had changed, a round's answer miscounting, the changelog fragment repeating a frame sentence". The definition's two parts, a restated fact and a copy left behind when its source changed, are that body's own. The clause "so that none could go stale" is the body's "keeping those copies consistent" in other words. The definition matches the base text it replaces, `docs/release-checklist.md:77`, "#1148, which removed the records' copies of one another". #1148's body also asks for record fields that store a copy of the tree, a count or a coordinate. The definition reaches only a record's copy of another record, as `:77` does, and every instance #1148 counted in records alone is a record's copy of another record, except the miscount, which is no copy. So the narrower scope follows the ratified sentence and changes no verdict on #1148's own evidence. #1020's title is "when one kind of finding recurs across review rounds, each fix pass fixes one instance and the next round finds the next". Under the new sentence it is the next step and the issue that follows, and not the question asked of each finding. That is the relation G17 states (read: `frame/design.md:23`).

The verdict clause changed too, from round 3's "only where they do" to "The count is `worse` only where stale copies are what kept it up." It differs from round 3's paste-ready "only where one does". The framer's words ask a causal question: did stale copies keep the count from falling, as against the mix of work the sentence before names ("a release's mix of work moves the count as well as stale copies do"). Where both causes kept the count up, the sentence does not set a threshold. The `add` sends that case to the weighing, "worse only where the cost outweighs what was bought", which the `to` makes this count a row of. So the clause is guidance for a judgment that the settling session writes and the owner reads before the settle pull request merges, and not a second rule. Either way the clause is answered, the outcome names #1020 and files no new issue. I read it as one question and raise no finding.

The copies were brought along. Each place that states the *2b* question was listed by a search for `stale` and for `restate one another|they do|restatement|only where one does` over `frame/`, `changelog.md`, `gaps.md` and `trail/phases/` (executed). *Scope* item 6 (`frame/design.md:35`), S5 (`:55`), the *Removes* row (`:146`), G17 (`:23`), `changelog.md:3`, `changelog.md:9` and `gaps.md:9` each ask whether a finding found a stale copy. Each reads the count as `worse` only where stale copies are what kept it up. The remaining hits of the old wording are the `from` (`:125`), the quotation in the *Removes* row (`:146`), `frame/plan.md:36` (A11, a rejected option's own grounds), and the quotation on `changelog.md:3`. Round 3 left all four standing. The appositive "which is what #1148 removed" on `changelog.md:3`, and "the copies #1148 removed" in *Scope* item 6, gloss a definition stated in full beside them, so they set no second meaning. G17's classification of this work item holds: round 2's finding 2, a plan cell still stating the operation count the design had changed (`trail/rounds/round-2.md:71`), found a stale copy. Round 1's finding 4, a missing `check:` reader (`trail/rounds/round-1.md:116`), and round 2's finding 1, a `to` that made #1020's check wait on a finding the weighing never makes (`trail/rounds/round-2.md:13`), did not (read).

The close names `85444c5f`, which touches `changelog.md` and `gaps.md`, paths the finding's `location:` names. Its `answer:` names `48e57eef` as the commit that rewrote the frame locations. Both statements hold (executed: `git show --stat`).

```seal
confirms: none
```
What matched: G15 and `frame/plan.md` *Technical context* (`frame/plan.md:13`) at the fix's head. Claimed: four operations, one `add` and three `change`, with no error and no unread line; each `from` in its section; no `to` in the tree; both citations of the new bold lead resolve; the longest prose line of the three rule `to` values is 71 columns. Executed in this round's probe at `85fa5858`: `rule_changes.py#parse` reads that from this design and one `change` from #1258's, with no error and no unread line. `#section_lines` places *5* at 105 to 165 before #1258's `change` and at 105 to 158 after it, *2b* at 31 to 103, and *The checks* at 33 to 44. Each `from` is found once in its section, and no `to` is in its file. After #1258's `change` and then this design's four, the new bold lead stands in `docs/measuring-a-run.md`, and the applied `docs/release-checklist.md` cites it twice. The *2b* `to` is now 14 lines. Its widest line is 69 columns with the indent stripped, so the 71 the plan states is still the widest of the three. G14's 76-column limit holds.

```seal
confirms: none
```
What matched: the orchestrator's row at `adbd6d33` (`frame/plan.md:55`), read against `skills/code-review/orchestration.md:132-153`. That paragraph asks for a row for each decision to go on past the third round. It wants the counts and signals weighed as grounds, and the document judged against. The row gives the fall of 4, 2 and 1 findings, the one recurring signal (a regression born of a round's paste-ready `to`), and the verifying round a regression's fix pass is owed. It names its documents. The fold followed the row: `48e57eef` writes the *2b* sentence in the framer's own words, not round 3's paste, and grounds it on `docs/release-checklist.md:77`, which holds "#1148, which removed the records' copies of one another" (read). The proofer writes no line for that decision, and this record states none.

```seal
confirms: none
```
What matched: the fix pass's narrow run and the `unverified` label. Re-run at `85fa5858` in this round's clone: the modules that read a changelog fragment, a closing memo or the counts, plus the cited-section test, in one `bin/test -q`. That is `tests/behaviour/test_release_hygiene.py`, `tests/github/test_publish_release_note.py`, `tests/skills/test_unverified_check.py`, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/text/test_a_record_carries_no_comment.py`, `tests/github/test_rules.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/github/test_finding_counts.py`. 643 passed, exit 0 (executed). The fix pass claimed 691 over seven modules it does not name, so the two numbers are not one set and this round compares none. `gaps.md:7` names the orchestrator's `seal gate` as the answerer for the full suite, the lint and the format check, and no record claims a passing suite (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `85fa5858` | the branch | the orchestrator, by `seal gate` |
| Whether 0.27.3's release pull request body weighs each grown row and opens an issue only for one judged `worse` (S3) | the release pull request, not yet open | the orchestrator that writes the body, and the owner before the merge |
| Whether the settle after 0.27.3 weighs its records-alone count in its `flow-baseline` comment as *2b* asks, including where stale copies and the mix of work both kept the count up (S5) | the settle after 0.27.3 | the settling session, and the owner before the settle pull request's merge |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_tmp_round4_rule_changes.py -q -s -p no:xdist`, in a `git clone --no-local` at `85fa5858` under `<scratchpad>/1793541310-a-band-flags-a-row-and-a-judgment-decides/round-4/`. The file parsed both pending designs with `rule_changes.parse`, read each section, `from` and `to` before any change, applied #1258's `change` and then this design's four operations in merge order by `rule_changes.pattern`, and resolved the new bold lead with the cited-section test's own `resolves` | 1 passed, exit 0, with the readings in the second confirmation. The file was deleted after the run |
| `bin/test -q` over the nine modules named in the last confirmation, in the same clone | 643 passed, exit 0 |
| `python3 .github/scripts/finding_counts.py --released-at HEAD --root .`, in the same clone | exit 0. This work item reads 7 findings, 3 with a regression or reopens line, 4 in records alone, 3 rounds |
| `gh issue view 1148 --json title,state,stateReason,closedAt,body` and `gh issue view 1020 --json title,state,stateReason,body` | #1148 `CLOSED`, `COMPLETED`; #1020 `OPEN`; the bodies quoted in the first confirmation |
| A search for `stale` and for `restate one another`, `they do`, `restatement` and `only where one does` over `frame/`, `changelog.md`, `gaps.md` and `trail/phases/` in the worktree | the lines named in the first confirmation, and no other |

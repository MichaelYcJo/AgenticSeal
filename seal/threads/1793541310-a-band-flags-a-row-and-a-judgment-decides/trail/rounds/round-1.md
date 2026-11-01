# Review round 1: 1793541310-a-band-flags-a-row-and-a-judgment-decides

```seal
target: 20b1162b against cd694aa3
```

The target is the branch at `20b1162b` against its merge base `cd694aa3` on `release/v0.27.3`. The diff touches only the work item's own records, so the review reads the frame's three rule changes as the deliverable, against the policy root at the base. No earlier round exists, so no fact is carried; every fact below was opened in this round. The release branch has since moved to `81414aae` (#1273). That commit changes `.github/scripts/release_report.py` only in its `__main__` stream setup, and touches neither `HEADER` nor either module the new `check:` line names (executed: `git diff --stat cd694aa3 81414aae`), so nothing here depends on the branch merging it.

## Findings

### 1. The producer list G5 calls whole misses `finding_counts.py`, and its reader in step 2b turns a count that did not fall into a verdict with no weighing

```seal
severity: should
location: `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:11`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:16`, `docs/release-checklist.md:79-80`
evidence: executed `ls .github/scripts skills/*/scripts evals/scripts`, `git grep -n -E "finding_counts|does not fall" -- :!seal/threads :!.test_durations`
```

Why it matters: G5 sets the class as "every sentence that turns a moved number into an issue or a verdict directly". It builds the list by contract rule 12's first method, from what produces the number, and says "the producer list is whole for the scripts this tree ships". The list names `release_report.py`, `session_cost.py`, `payload_meter.py`, `noninferiority.py`, `.test_durations` and a measuring work item. `.github/scripts/finding_counts.py` is not on it, and its search pattern does not name it. That script prints the four counts the settling session posts to `flow-baseline` at every release. `docs/release-checklist.md:76-80` (*2b. Settle what earlier releases left behind*) reads them release against release: "0.24.0's four work items read 17 recurring of 36 findings ... and 0.25.0's one read 3 of 10". Then it gives a verdict and a next step straight from the number: "A release whose records-alone count does not fall says the records still restate one another, and the next step is #1020's check that reads recurrence." No weighing comes between the count and the verdict. That is the shape the new rule removes from *5*.

So the list is a sample that was handed back as whole, and contract rule 12 makes that a finding whatever the instances on it hold. *Scope* item 5 ("No other file in the tree changes, because no other sentence turns a moved number into an issue directly") rests on this list. It does not hold until the frame weighs the step 2b sentence one way or the other. The sentence could be a criterion the owner set for #1148, which would place it in G10 with its grounds. Or it could be an instance of the class, which would need a fourth operation.

```markdown
G5, in the Producers sentence, after "`.test_durations` (the release table's test-file rows);", add:
`.github/scripts/finding_counts.py` (the four counts the settling session
posts to `flow-baseline`, read release against release in
`docs/release-checklist.md` *2b. Settle what earlier releases left behind*);

## Rule changes, a fourth operation, where the fix pass reads the sentence as in the class:

- change
  file: docs/release-checklist.md
  section: 2b. Settle what earlier releases left behind
  from: A release whose records-alone count does not fall says the records
    still restate one another, and the next step is #1020's check that reads
    recurrence.
  to: A records-alone count that does not fall is a row for the judgment
    `docs/measuring-a-run.md` *A band flags a reading for judgment, and a
    judgment decides whether it is worse* asks. The settling session writes
    that weighing in its comment, and #1020's check is the next step only
    where the weighing finds the records still restate one another.

Where the fix pass reads it as outside the class instead, G10 gains the
sentence with its grounds, and Scope item 5 names it.
```

### 2. The new rule's first sentence is unscoped, and it reads over the behaviour suite's pass rules 2 and 5, which fail a side from a noise band alone; G10 weighed only rule 4

```seal
severity: should
location: `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:16`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:61-80`, `evals/README.md:18-49`, `evals/scripts/noninferiority.py:102-108`
evidence: read `evals/README.md:18-49`, `evals/scripts/noninferiority.py:102-108`, `evals/scripts/noninferiority.py:895-912`
```

Why it matters: the `add` opens "A band flags a reading for judgment, and a judgment decides whether it is worse". It defines a band as "how far a reading may move from the reading it is compared with and still read as the same". Nothing in the `to` limits it to a report, a log or a table. `evals/README.md:18-21` states that a preload rewrite "is proved not worse by running this suite on the old tree and on the new one". Its pass rule 2 holds the false-finding rate "within `FALSE_MARGIN` of the baseline's". Rule 5 fails a side "only where both rose by more" than `TOKEN_MARGIN`. `evals/scripts/noninferiority.py:103-108` sets `TOKEN_MARGIN = 0.07` as "the smallest whole percent that covers that spread" of two takes of one text. That is a noise band in the design's own sense. `noninferiority.py:903-912` returns `fail` when a reading is past it toward more cost, with no weighing of what the rewrite bought.

G10 places only "`noninferiority.py#verdict`'s fourth rule" outside the class. Rule 4 is a byte comparison with no margin, so G10's grounds ("the criterion a preload rewrite states for its own claim, chosen before the run") were never applied to the two rules that do carry a band. After the settle, a framer of a preload rewrite reads two policies. `docs/measuring-a-run.md` says a judgment decides whether a reading is worse. `evals/README.md` lets a 7 per cent band decide it. The design calls itself whole on the class, and two band-decided verdicts stand unweighed.

```markdown
G10, after the sentence on the fourth rule:
Rules 2 and 5 carry a band, `FALSE_MARGIN` and `TOKEN_MARGIN`, and are
placed outside on the same ground: each is a criterion the rewrite's claim
fixes before its run, the run decides that claim alone, and it files nothing.

The `add`'s `to`, a sentence after its first two sentences:
    A margin a claim fixes before its run is that claim's criterion and not
    a band in this sense: `evals/README.md` *The behaviour suite*'s pass
    rules decide whether a preload rewrite proved itself not worse, and file
    nothing.
```

### 3. The rule names the orchestrator's `--says` sentence as a place for the weighing, and that sentence has no band and two readings of what it owes

```seal
severity: should
location: `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:70-74`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:47-50`, `skills/verify/orchestration.md:415-475`
evidence: read `skills/verify/orchestration.md:158-197`, `skills/verify/orchestration.md:415-475`, `docs/the-review-record.md:514-536`
```

Why it matters: the `add` says "The party that writes the reading writes the weighing: the orchestrator in the sentence its `--says` carries or in a release pull request's body". The `--says` sentence goes beside the segment readings and the run-level table (`skills/verify/orchestration.md:182-191`, `:415-424`). The segment readings are graded against per-kind bars, "never a refusal threshold" (`docs/the-review-record.md:516-517`). The run-level table sets "this run beside the last run measured" with no band (`orchestration.md:420-421`), and "carries no verdict" (`:463`). So no reading that `--says` carries is "past its band". Two readings follow, and an orchestrator acts on whichever it takes:

- No band means nothing is past it, so the clause owes nothing at `--says`.
- The changed *5* reads a table with no band the other way: "The table has no band, so a preload or a document that grew is a row for the judgment" (design line 98-100). Read that way, every run-level row that grew owes a weighing in the comment.

No scenario, S1 to S4, covers `--says`. The orchestrator writes that sentence from `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*, which does not cite the rule. Outside `seal/threads/`, nothing in the tree cites `docs/measuring-a-run.md` except its index row (executed: `git grep -n "measuring-a-run" -- :!seal/threads`). So the clause binds a writer through a document that writer's procedure never opens, and it has two readings once opened. Taking the clause out leaves one reading. G9 already places the `--says` path among the readers that file nothing.

```markdown
In the `add`'s `to`, the sentence on who writes the weighing:
    what was bought. The party that writes the reading writes the weighing:
    the orchestrator in a release pull request's body, and the crafter in
    the phase record of a work item that measures the process. The
    orchestrator files an issue for a reading judged `worse` so, and for
    none whose only ground is its band.
```

The other fix keeps the clause. It would have to say that a comparison with no band reads every move toward more cost as past it. It would also have to add a citation of the rule to `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*, and add a scenario for it. The `changelog.md` entry names no `--says`, so it stands either way.

### 4. No `check:` line names a reader for the release pull request body's weighing, the one tree instance this work replaces

```seal
severity: should
location: `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:80`, `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:105`
evidence: read `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md:47-50`, `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py:1-45`, `tests/github/test_release_report.py:197-227`
```

Why it matters: the `add` ends `check: none reader: the proofer at review`. A proofer reviews a work item's diff, and S1 places it at a measuring work item's phase record. No proofer reads a release pull request's body, which is where the changed *5* sends the weighing ("The orchestrator writes that weighing in the pull request's body, and opens an issue only for a row the weighing judges `worse`"). The changed *5* ends with a `check:` line naming `tests/github/test_release_report.py` and `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`. The first reads that the script prints the table and exits 0. The second reads the `release-report` job's placement in the workflow. Neither can read a weighing in a body, as design G11 itself says ("Together they read what the paragraph states as fact"). S3 names the owner as the reader: "The owner reads the body before the merge". Neither line names the owner. After the settle, the duty that replaced "a question the pull request's body answers, or an issue it opens" stands with no reader on either check line. A later framer that reads the lines to learn who holds the rule finds only a party that never sees the body.

```markdown
The `add`'s last line:
    check: none reader: the proofer at review and the owner before the release pull request's merge
```

The value holds no comma, `::` or em dash, as `skills/settle/SKILL.md` *A rule has one shape* requires. The changed *5* keeps its two modules for the facts they read.

## Confirmations

```seal
confirms: none
```
What matched: S4 and G15 (claimed: three operations, each `from` in its section, no `to` in the tree). Executed: the probe in `## Probes` parsed `frame/design.md` as one `add` and two `change` operations. `section_lines` found each section once: `docs/measuring-a-run.md` lines 50 to 78, `docs/release-checklist.md` lines 105 to 165, `docs/README.md` lines 33 to 44. `pattern` found each `from` in its section and no `to` in its file. The probe applied #1258's `change` first, in merge order, and the `from` of this work's *5* change was still found (G3). With all four operations applied, the citation in the changed *5* resolves to the new bold lead under the reader of `tests/behaviour/test_a_cited_section_stands_in_its_file.py`. `chain_check.py --worktree` over the clone refused no line of the design's `## Rule changes`.

```seal
confirms: none
```
What matched: G2 and G3. At `cd694aa3`, `docs/release-checklist.md:126-133` is the paragraph that opens **Read the release table before the merge.**, and it carries no `check:` line. `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/design.md` holds one `change` to *5*, whose `from` is the paragraph that opens **The orchestrator opens the release pull request** and nothing after it (read).

```seal
confirms: none
```
What matched: G9's `release_report.py#HEADER` ends "so no row is a verdict" (`.github/scripts/release_report.py:60-65`, read). The changed *5*'s "no row of it is a verdict" states the same fact.

```seal
confirms: none
```
What matched: the crafter's claim for Scope item 5's search. `git grep -n -i -E 'issue it opens|that grew' -- ':!seal/threads'` lists `docs/release-checklist.md:131` and `:132` only (executed). Finding 1 is about the method behind that list, not this search.

```seal
confirms: none
```
What matched: `changelog.md:3` on #1259. `gh issue view 1259` gives the title with 9,658 B against 9,261 B, state `CLOSED`, reason `NOT_PLANNED`, at 2026-11-01T12:57:30Z (executed). The crafter's departure from the design's "not a defect" wording (`trail/phases/phase-1.md:18`) keeps the release note to what the event log records. #1263's body says "The owner closed #1259 as not a defect", so the `add`'s wording has that source.

```seal
confirms: none
```
What matched: the crafter's narrow run, re-run at `20b1162b` over eight of the 13 modules, including the plan's six, `tests/behaviour/test_chain_hooks_hardening.py` and `tests/skills/test_unverified_check.py`: 625 passed, exit 0 (executed). The `unverified` label on the full suite, lint and format is honest. `gaps.md:7` names the orchestrator's `seal gate` as its answerer, and no claim of a passing suite stands anywhere in the records.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `20b1162b` | the branch | the orchestrator, by `seal gate` |
| Whether 0.27.3's release pull request body weighs each grown row and opens an issue only for one judged `worse` (S3) | the release pull request, not yet open | the orchestrator that writes the body, and the owner before the merge |
| #1258's pending `to` for *5* holds a line that comes to 90 characters by `len` once applied (the line ending "`--state open` lists no"). That is over `tests/behaviour/test_docs_line_wrap.py`'s 88, which reads `display_width` and which this probe did not run. That design is outside this target | `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/design.md:78` | the orchestrator, at the settle's broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_tmp_round1_rule_changes.py -q -s -p no:xdist`, in a `git clone --no-local` at `20b1162b` under the round's scratch directory; the file parsed both pending designs with `rule_changes.parse`, applied #1258's `change` and then this design's three operations in merge order, and resolved each citation of `docs/measuring-a-run.md` with the cited-section test's own reader | 1 passed, exit 0. Three operations, no errors. Each section found once, each `from` found, no `to` in the tree. The citation in *5* resolves after the `add`. The only applied line over 88 characters is #1258's (row 3 of `## Not judged`). The file was deleted after its one run |
| `bin/test -q` over `tests/github/test_rules.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/behaviour/test_release_hygiene.py`, `tests/github/test_publish_release_note.py`, `tests/text/test_a_record_carries_no_comment.py`, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/skills/test_unverified_check.py`, in the same clone | 625 passed, exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline cd694aa3 --root . --worktree` in the clone, before this record | exit 0. It named the missing round record, gate record and guarantee, and refused no rule-change line |

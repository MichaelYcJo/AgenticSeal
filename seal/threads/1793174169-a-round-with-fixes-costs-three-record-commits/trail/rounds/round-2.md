# Review round 2: 1793174169-a-round-with-fixes-costs-three-record-commits

target: 8311f660, fixes 77f9d619..8311f660

## Findings

### 1. The orchestrator's file still places the answer commit before the sweep's corrections, and the policy text gives the orchestrator's own closes no commit count

severity: should
location: `skills/code-review/orchestration.md:58-60`, `skills/code-review/orchestration.md:73-80`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:170-171`, `tests/text/test_the_rules_have_one_owner.py:192-193`
evidence: read `skills/code-review/orchestration.md:54-80`, `agents/crafter.md:148-158`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:26-36`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:170-171`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/changelog.md:3`
verdict: fixed ea5f22e6
reopens: round-1#1

Why the close does not hold. Round 1's finding named two gaps. The first
was the count: one commit per finding or one per pass. The second was the
timing: whether the answer commit comes before or after the corrections
the fix pass makes for the rules its range reworded. `b413456f` closes both
gaps in `agents/crafter.md:156-158`, which now reads "Then commit ... in one
commit for the whole pass, after your last fix commit and its
corrections." It closes only the count in the orchestrator's file. Part of
the defect therefore still stands in two of round 1's locations.

The orchestrator's file. `skills/code-review/orchestration.md:58-60` says
the fix pass "commits the two lines of every finding it answered in one
commit for the whole pass, after its last fix commit". The paragraph at
`:73-80` comes after it and opens "The fix pass then finds what the fixes
left standing", and the fix pass corrects each of those places. Read in
order, the orchestrator's file puts the answer commit first and the
corrections after it. `agents/crafter.md` puts them the other way round.
The orchestrator writes the fix pass's spawn prompt from this file, and
#955's split started in a spawn prompt (`frame/design.md` Scope item 4).
The frame as folded at `8311f660` asks for the timing in this paragraph.
`frame/design.md:30-32` says the paragraph states "after its last fix
commit and its corrections". The changelog fragment (`changelog.md:3`)
says the orchestrator's file "says so" for the sweep's corrections too.
Neither is true of `:58-60`. Round 1's own paste-ready block for this file
left out the corrections clause, and `b413456f` applied it as given. The
gap comes from round 1's text and not from how the fix was written, so the
grounds for reopening are round 1's.

The policy text. The `to:` lead at `frame/design.md:170` says "one commit
carries every finding that party closes in the pass". The orchestrator
closes findings without a fix pass: `deferred the frame` on the framer's
route, and the cap's `deferred <home>`. In those cases "the pass" refers to
nothing. The body at `:171` says only that such a finding "takes both lines
from the orchestrator", with no commit count. Row *The record* at
`skills/code-review/orchestration.md:161` does state one commit for every
open finding. The rule's policy home, which the settle writes, does not.

The fix moves the orchestrator's commit sentence to the end of the
paragraph on what the fixes left standing. It also gives the policy text a
count that holds for both parties. In `skills/code-review/orchestration.md`,
the paragraph at `:54-64` loses its commit sentence:

```markdown
(`docs/the-review-record.md` *The round record*); it writes no
`trail/phases/phase-N.md` and no `plan.md` row. **The orchestrator writes
neither line of a finding the fix pass answers, and its fix-pass prompt leaves
both lines to the crafter.** A close the orchestrator doubts goes into the
verifying round's spawn prompt, since that round weighs every close, and the
orchestrator does not rewrite the line.
```

The paragraph at `:73-80` ends with it:

```markdown
hand-back with why it stands. The round that follows reads that list against
the diff. Last, the fix pass commits the two lines of every finding it
answered in one commit for the whole pass, after its fix commits and those
corrections, because a `fixed` verdict names a commit that already exists.
```

The pin at `tests/text/test_the_rules_have_one_owner.py:192-193` becomes
`"commits the two lines of every finding it answered in one commit for the
whole pass, after its fix commits and those corrections"`, seen red against
`8311f660` first. The `to:` item at `frame/design.md:170-171`:

```markdown
  to: **A finding's `verdict:` and `answer:` lines are one party's, and each time that party closes findings, one commit carries the lines of all of them.**
    A finding a fix pass answers is the fix pass's alone. After its last fix commit and the corrections its sweep made, the pass writes the lines of all the findings it closed and commits them together, once, since the `fixed` verdict must name a commit that exists before it. The orchestrator writes neither line of such a finding, and a close it doubts goes into the verifying round's spawn prompt, since that round weighs every close. A finding closed without a fix pass, such as `deferred the frame` on the framer's route or a `deferred <home>` the orchestrator files at the cap, takes both lines from the orchestrator, which commits the lines of every finding it closes at that step in one commit. A second party's commit adds a record commit to the round and nothing a reader uses.
```

These texts were measured in memory against the paste check's own
functions, and no file was written. The proposed orchestrator file shares
no run of 15 words with `agents/crafter.md` or with the proposed `to:`
text. The tree with the proposed orchestrator file passes `over_baseline`.
So does the tree with the proposed `to:` text appended to
`docs/the-review-record.md` (executed, `## Probes`). The frame is not the
crafter's to write (`agents/crafter.md:17-21`), so the orchestrator
decides who edits `frame/design.md`.

answer: The finding holds. `skills/code-review/orchestration.md` put the commit sentence before the paragraph on what the fixes left standing, so the answer commit read as coming before the sweep's corrections. That order came from round 1's paste-ready block, which `b413456f` applied as given. `ea5f22e6` takes this record's two blocks. The fix-pass paragraph loses its commit sentence. The paragraph on what the fixes left standing now ends "Last, the fix pass commits the two lines of every finding it answered in one commit for the whole pass, after its fix commits and those corrections, because a `fixed` verdict names a commit that already exists." The pin in `tests/text/test_the_rules_have_one_owner.py` follows the moved words. It exited 1 against the text at `8311f660` before the text changed, and exited 0 after. The changelog fragment now says the orchestrator's file states the commit at the end of that paragraph, so the answer commit follows the corrections there too. The policy half of this finding is the `to:` text in `frame/design.md`, which the orchestrator rewrote at `4fa7a630`; the crafter does not write the frame. The `git grep` sweep for "after its last fix commit", "after any fix commit" and "in one commit for the whole pass" finds no other statement of the timing without the corrections: `frame/design.md:30-32` and `:55`, and `frame/plan.md:73`, all name the corrections.

### 2. The rule-change text still shares a 15-word run with the orchestrator's file, so settling it word for word fails the paste check

severity: should
location: `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:171`, `skills/code-review/orchestration.md:60-61`
evidence: executed `.venv/bin/python -c longest_run(to text, orchestration.md) at 87e89f17 b413456f 3630fbbd 8311f660`, `.venv/bin/python -c over_baseline(tree with the to text appended to docs/the-review-record.md)`
verdict: fixed ea5f22e6

Why it matters. Commit `8311f660` says it reworded the `to:` body "so it
shares no 15-word run with the new `skills/code-review/orchestration.md`
sentence". One run is left. The body at `frame/design.md:171` reads
"since a `fixed` verdict names a commit that already exists. The
orchestrator writes neither line of such a finding". The orchestrator's
file at `:60-61` reads "because a `fixed` verdict names a commit that
already exists. **The orchestrator writes neither line of a finding". The
check strips backticks and asterisks. What is left is "a fixed verdict
names a commit that already exists. the orchestrator writes neither line
of", which is 15 words, the check's `WINDOW`. The pair
`docs/the-review-record.md` and `skills/code-review/orchestration.md` has
no `BASELINE` entry
(`tests/text/test_no_passage_is_pasted_into_a_second_file.py:189-221`), so
it is allowed no shared run.

With the `to:` text appended to `docs/the-review-record.md` the way a
settle that copies it word for word would write it, `over_baseline`
returns "docs/the-review-record.md and skills/code-review/orchestration.md
share 1 runs of 15 words where 0 were measured" (executed). The run is
not new to this range. It stands at `87e89f17`, `3630fbbd` and `8311f660`.
At `b413456f` the longest run was the 21-word run the crafter's answer
reported (executed). The `to:` text is a unit the build made, so this
finding carries no `regression:` line and no `reopens:` line.

Round 1 also missed it, and round 1's record says the opposite. Round 1's
S4 entry said the longest run between the orchestrator's paragraph and the
`## Rule changes` text was 14 words. That was counted by hand, and it
missed this run. That entry is wrong, and this round withdraws it.

Finding 1's proposed `to:` text already removes the run, because it
rewords the clause to "since the `fixed` verdict must name a commit that
exists before it". Finding 1's move of the orchestrator's sentence also
removes it from the other side. Either edit alone is enough. Where finding
1's `to:` text is not taken, this is the smallest change at
`frame/design.md:171`:

```markdown
... and commits them together, once, since the `fixed` verdict must name a commit that exists before it. The orchestrator writes neither line of such a finding, ...
```

answer: The finding holds, and the run is gone from both sides. The orchestrator rewrote the `to:` text at `4fa7a630`. In `ea5f22e6` the orchestrator's file no longer puts "a `fixed` verdict names a commit that already exists." in front of "The orchestrator writes neither line", because the commit sentence moved to the end of the next paragraph but one. Measured at `ea5f22e6` with `.venv/bin/python`, using the paste check's own `longest_run` between `rule_changes.parse(text, 'docs').ops[0].new` and `skills/code-review/orchestration.md`: 0. That function reports only runs of `WINDOW` (15) words or more, so 0 means no shared run of 15. The same function gives 0 between that text and `agents/crafter.md`, and 0 between the two agent-facing files. `parse` returned one `add` and no errors. `over_baseline` on the tree read in memory, with that `to:` text appended to `docs/the-review-record.md`, returned no refusal (all executed). `tests/text/test_no_passage_is_pasted_into_a_second_file.py` exited 0 at the edited tree, with 8 passed.

## Confirmations

confirms: none
The count half of round-1#1 is closed. `agents/crafter.md:156-158` and row
*The record* at `skills/code-review/orchestration.md:161` each have one
reading. They say one commit for the whole pass, and one commit for every
open finding (read). In `agents/crafter.md` the sentence now comes after
the sweep and names its corrections, so the crafter's file has one
reading for the timing too (read). The pins at
`tests/text/test_a_moved_rule_leaves_its_definition.py:510-514` and
`tests/text/test_the_rules_have_one_owner.py:192-193` and `:217` hold the
new words. The 29 modules that `git grep -l` finds naming `agents/crafter.md`,
`crafter.md` or `skills/code-review/orchestration.md`, together with the two
changed test modules, passed (executed). `b413456f` touches
`agents/crafter.md`, a path on round 1's `location:` line, and `c4c6e52e`
commits the finding's two lines alone after it, as the new rule says
(executed, `git diff --stat`). The crafter's red-at-`87e89f17` runs were
read, not repeated: the pinned words are new in `b413456f` (read).

confirms: none
The frame folds at `8311f660` match the built crafter text, each with one
reading. `frame/design.md:51-57` (Scope item 3), `:153` (S3) and
`frame/plan.md:73` (row A) say one commit for the whole pass, after the
last fix commit and its corrections, as `agents/crafter.md:156-158` does.
Scope item 1 (`frame/design.md:30-32`) has one reading as well. The
orchestrator's file does not match it, which is finding 1. `git grep` over
the tree for the old wordings finds them only in round 1's record (executed).

confirms: none
`rule_changes.parse` on `frame/design.md` at `8311f660` returns one whole
`add` operation and no errors. `chain_check.py --baseline 5287dd42
--worktree` refuses nothing in the frame. Its refusals are what a
verifying round is owed before this record exists, plus the missing
`trail/gate.md` and `guarantee.md` (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `8311f660`. Not run, under contract rule 2 | the branch | the orchestrator, through `seal gate` after the rounds settle |
| Whether the settle writes the `to:` text into `docs/the-review-record.md` word for word or in its own words. Finding 2 holds only for the first. Under the second, the run may or may not survive | `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:170-171` | the settle after the release |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the 29 modules that `git grep -l` finds under `tests/` naming `agents/crafter.md`, `crafter.md` or `skills/code-review/orchestration.md`, plus the two changed test modules, `-q` | exit 0, 773 passed |
| `bin/seal layout --check` | exit 0 |
| `bin/seal rules --check` | exit 0: all 266 check lines in 55 rule files hold |
| `git diff --check 77f9d619..8311f660` | exit 0, nothing printed |
| `python3 skills/code-review/scripts/chain_check.py --baseline 5287dd42 --root <worktree> --worktree`, before this record was written | the verifying round owed for round-1#1 and for `b413456f`; no gate record; no guarantee; nothing in the frame |
| the repository venv's python calling `longest_run` from `tests/text/test_no_passage_is_pasted_into_a_second_file.py` on the parsed `to:` text against `skills/code-review/orchestration.md`, read through `git show` at each commit | 15 words at `87e89f17`, 21 at `b413456f`, 15 at `3630fbbd`, 15 at `8311f660` |
| the same module's `over_baseline` on the tree read in memory, with the `to:` text at `8311f660` appended to `docs/the-review-record.md` | one refusal: the pair shares 1 run of 15 words where 0 were measured |
| the same `over_baseline`, in memory, with finding 1's proposed orchestrator file and proposed `to:` text in place of the current ones | no refusal; longest run 0 between each pair of the proposed texts and `agents/crafter.md` |
| `git grep` over the tree for "each finding together", "of each finding in one commit", "in one commit after your" and "in one commit after any", and "written in one commit" | matches only in `trail/rounds/round-1.md` |

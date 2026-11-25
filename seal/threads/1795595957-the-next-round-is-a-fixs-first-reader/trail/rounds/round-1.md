# Review round 1: 1795595957-the-next-round-is-a-fixs-first-reader

```seal
target: 72b8642c1 against origin/release/v0.39.0
```

The range read is `a9cc9cf93..72b8642c1`, eleven commits, in a `git clone --no-local` at the target under the round's scratch directory. This is the first round, so no earlier round's facts are carried: each fact below was opened or run in this round. The work item's records that state the present were each read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`, then `trail/phases/phase-1.md` and `trail/subagentstop-probe.md`. No `pr.<lang>.md` stands, since `Commit and pull request language` is English. `seal/parity.json` is not declared. Outside the diff, this round opened `skills/code-review/orchestration.md:40-260`, `skills/code-review/scripts/chain_check.py:100-140`, `:870-1000`, `:1456-1505` and `:2150-2290`, `agents/sealer.md:30-122`, `docs/running/the-run.md:1-40`, `docs/forms/the-round-record.md:60-110`, `skills/code-review/SKILL.md:240-275`, `skills/implement/SKILL.md` *4. The closing memo — only what the diff cannot show*, `skills/core/SKILL.md:27` and `:113`, `skills/code-review/gate-to-pull-request.md:46-54` and `:148-158`, `skills/implement/merge-order.md:26-35`, and the sibling cases of each new test.

The spawn prompt named three doubts, and this paragraph answers each. First, the orchestrator's new paragraph does not read one way (finding 1). Its split itself agrees with the core's row *No fix that no round reads* and with `agents/sealer.md` step 4: `chain_check.py#records` hands `#channel` exactly the row's case, a `fixed` finding located in the work item's records whose commit touched them alone (`chain_check.py:1487-1489`), and prints the words "a verifying round is owed" only at the last record, at each other `fixed` or `rejected` finding (`:941-955`) and at line 0 for a commit after its `target:` outside the records (`:1497-1503`). Step 4 opens on the same condition (`agents/sealer.md:105-108`). What step 4 then reads over the diff is wider than the records the proofer's rule names (finding 2). Second, of the four record rows, *Record against the code* and *Figure against its text* name a read a proofer runs anywhere. *Record against record* and *Record against another work item's frame* name a `git grep` that lists nothing in local mode (finding 3). Third, the move of a regression's records-only fix to the sealer holds at both statements of the old rule: `skills/code-review/orchestration.md:155-159` at the target, and `docs/running/the-run.md:11` through the design's first `change`, whose `from:` the chain check matched. `git grep` on "whatever the count", "no fix goes unread" and "regression's fix" outside the work items finds no third. Two sentences of the same section state the same kind of rule for a `must` after the stop row and for a `reopens:` finding, and the new paragraph now contradicts them (finding 5). A sentence written on the old premise that a round follows every pass sends a doubted close to a round that no longer comes (finding 4).

## Findings

### 1. The orchestrator's new read offers a stop where a round is owed, and sends every other refusal on the record to the sealer

```seal
severity: should
location: `skills/code-review/orchestration.md:126-136`, `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/frame/design.md:51`, `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/changelog.md:5`
evidence: read `skills/code-review/orchestration.md:126-136`, `:155-162`, `:219-225`, `skills/code-review/scripts/chain_check.py:881-956`, `:1456-1505`, `skills/core/SKILL.md:113`
```

Why it matters: this paragraph is where the orchestrator decides between a verifying round and the sealer, and it decides on two branches of the output that do not cover the output.

The first branch reads "a round reads the pass, and the orchestrator spawns it or stops the run as this section states" (`skills/code-review/orchestration.md:132-133`). At that point the pass is committed and the check has named a `fixed` or `rejected` finding that no round read. The section's own paragraph says "The run ends only on a round whose record holds ... no `fixed` one the core's row gives to a round" (`:219-221`), and the core's row holds that every change after the last round is read by a round or by the sealer (`skills/core/SKILL.md:113`). So the section states no stop at this point, and "or stops the run" reads either as a stop that leaves a code fix unread, or as a stop at some later round that the sentence does not name. The frame carries the same words, "spawns it or stops the run as the section already states" (`frame/design.md:51`).

The second branch reads "Where no line of its output names that record with those words, no round follows the pass" (`:133-135`). The check prints other lines at the same record. A close block the check cannot read leaves its finding with no verdict, and `#records` then names it as a finding with no close block, while `#channel` prints no "a verifying round is owed" for it, since its test is `f.verdict[0] == FIXED` (`chain_check.py:944-945`). A code fix whose close block is misspelt therefore takes the branch that opens `skills/code-review/gate-to-pull-request.md`, and `frame/questions.md` Q1 records that the preflight there does not refuse where a verifying round is owed. The changelog says the same, "the orchestrator opens `skills/code-review/gate-to-pull-request.md` otherwise" (`changelog.md:5`).

The snippet replaces `skills/code-review/orchestration.md:126-136`. It keeps the three phrases `test_the_orchestration_reads_whether_a_round_follows_off_the_check` pins. The fix pass also owes `changelog.md:5`, whose "otherwise" becomes "where no line of the output names that record". `frame/design.md:51` is a frame sentence, which the fix pass does not edit, so it goes to the framer's fold.

```markdown
**Whether a round follows a fix pass is read off the chain check, not
judged by eye.** Once it has committed the pass's round record, the
orchestrator runs the read the proofer runs before it hands back,
`python3 skills/code-review/scripts/chain_check.py --baseline <base>
--root <the branch worktree> --worktree`. Where its output names that
record with the words `skills/code-review/scripts/chain_check.py#VERIFYING_ROUND`
holds, "a verifying round is owed", a round reads the pass, and the
orchestrator spawns it, since the run does not end on a fix that the row
*No fix that no round reads* of `skills/core/SKILL.md` *Judgment is not
licence to skip a party* gives to a round. Where a line names that record
with other words, the check could not read the record as the pass left it,
and the orchestrator has the party that wrote the line it names repair it,
the fix pass for a close block, before it runs the read again. Where no
line of its output names that record, no round follows the pass, and the
orchestrator opens `skills/code-review/gate-to-pull-request.md`.
```

### 2. The sealer's diff read takes in the round record and the gate record, whose sentences state their own commit, and reads them against HEAD

```seal
severity: should
location: `agents/sealer.md:111-122`, `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/frame/design.md:49`, `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/changelog.md:4`
evidence: read `agents/sealer.md:105-122`, `agents/proofer.md:116-134`, `skills/code-review/orchestration.md:91-95`
```

Why it matters: the step tells the sealer to withhold on "a sentence HEAD contradicts" among every sentence the diff adds, and the diff it names holds sentences that HEAD contradicts by design.

Step 4 runs `git -C <root> diff <the last record's target>..HEAD -- seal/threads/<item>/` and reads "against HEAD each sentence the diff adds or rewrites" (`agents/sealer.md:111-114`). The last record is written after the commit its `target:` names and committed after the fix pass (`skills/code-review/orchestration.md:91-95`), so the diff adds that whole record. A finding located in the records says what a record said at the target, such as "`frame/plan.md:12` says X", and the fix pass made HEAD say something else. `trail/gate.md`, which the broad run writes and the orchestrator commits before the sealer, is in the diff too and states the commit its `run:` line names. The step cites the proofer's rule only for "How a frame section dated to the framer's commit reads" (`:118-120`). That rule names which records state the present, and a round record is not among them (`agents/proofer.md:116-134`). On the literal reading the sealer withholds on the finding's own grounds. On the other reading the sealer applies a scope that the step does not state. `frame/design.md:49` and `changelog.md:4` repeat "each sentence the diff adds or rewrites".

The snippet replaces `agents/sealer.md:113-122`, from "and read against HEAD". It keeps the two commands and the `withheld` phrase that `test_step_4_reads_a_records_only_fix_over_its_diff` pins. The fix pass also owes `changelog.md:4`, and `frame/design.md:49` goes to the framer's fold.

```markdown
   and read against HEAD each sentence the diff adds or rewrites in the
   records `agents/proofer.md` *Every round reads the work item's records
   that state the present, whole, against its target* names, and each other
   statement in those records of a fact the diff changed. List those with
   `git -C <root> grep -n -F '<the fact's words>' -- seal/threads/<item>/`,
   a sample under rule 12 and rule 19. That rule also says how a frame
   section dated to the framer's commit reads. A
   record that does not say what the finding asked, and a sentence HEAD
   contradicts, are each a disagreement like any other, and a `withheld`
   reason naming its coordinate.
```

### 3. Two record rows list the other statements with `git grep`, which prints nothing over a records root in local mode

```seal
severity: should
location: `skills/code-review/SKILL.md:85-86`, `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/frame/design.md:46-47`
evidence: read `skills/core/SKILL.md:27`, `docs/layout/one-root-by-lifetime.md:157-162`, `skills/code-review/SKILL.md:85-86`; executed `git grep -n -F 'ref' -- .git/HEAD` in the round's clone, exit 1 with nothing on stderr
```

Why it matters: an empty listing reads as "no other statement of this fact", and the row's command gives that answer wherever the records live under the git directory.

In local mode the records root is `$(git rev-parse --git-common-dir)/seal/` (`skills/core/SKILL.md:27`), which no commit holds (`docs/layout/one-root-by-lifetime.md:157-162`). `git grep` reads tracked files only. The probe gave it a path inside the git directory and it exited 1 with nothing on stderr, the same exit as a search that matched nothing. The row *Record against record* lists the statements with `git grep -n -F '<the fact's words>' -- seal/threads/<item>/`, and the row *Record against another work item's frame* with `git grep -n -F '<the section's heading>' -- 'seal/threads/*/frame/design.md'` (`skills/code-review/SKILL.md:85-86`). Contract rule 11 resolves `seal/` to the records root, so in local mode both commands point at untracked files and list nothing. `grep -rn` reads the root at each of the three places. The sealer's command at `agents/sealer.md:116` is outside this finding, since in local mode no commit holds the records and no records-only `fixed` commit reaches step 4.

The snippet replaces the two rows. `frame/design.md:46-47` states the same commands and goes to the framer's fold.

```markdown
| Record against record | each fact a record states, against every other statement of it in the work item's records. List them with `grep -rn -F '<the fact's words>' seal/threads/<item>/` at the target, which reads the records root wherever it stands, local mode's untracked one among them, a sample under contract rule 12 and contract rule 19, as *A paste-ready fix reaches every statement of the fact it repairs, or names where it stops* says of a finding's search |
| Record against another work item's frame | each rule, section or file the records cite that another work item of the release changes, against that item's frame: the unsettled designs' `## Rule changes`, which with the policy root make the policy in force (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*), and the rows of this item's `frame/plan.md` *Overlap with the release*. List them with `grep -n -F '<the section's heading>' seal/threads/*/frame/design.md` at the target, outside the work item's own directory |
```

### 4. A close the orchestrator doubts still goes to the verifying round's prompt where no round follows the pass

```seal
severity: should
location: `skills/code-review/orchestration.md:57-61`, `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/frame/design.md:87-91`, `docs/forms/the-round-record.md:99-102`
evidence: read `skills/code-review/orchestration.md:57-61`, `:126-136`, `docs/forms/the-round-record.md:96-102`, `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/frame/design.md:87-91`
```

Why it matters: this work gives more passes to the sealer, a regression's records-only fix among them, and a regression is the case where a pass already broke something once. For such a pass, the one channel the orchestrator has for a doubted close leads nowhere.

`skills/code-review/orchestration.md:59-61` reads "A close the orchestrator doubts goes into the verifying round's spawn prompt, since that round weighs every close". The design's `change` on `docs/forms/the-round-record.md` rewrites the sentence before the policy's copy of this rule to "before it reads whether a round follows the pass, ... since that round can read only what a commit holds" (`frame/design.md:91`). It leaves the next sentence, "It edits no line in that commit, and a close it doubts goes into that round's spawn prompt" (`docs/forms/the-round-record.md:101-102`). After the settle, "that round" refers to a round that may not follow. The new paragraph at `:126-136` says no round follows such a pass. Contract rule 19 asks a change to remove what stood on the old fact in the same commit.

The snippet replaces `skills/code-review/orchestration.md:59-61` from "A close the". The design's `change` owes the same reach in `docs/forms/the-round-record.md:101-102`, with its `from:` extended to that sentence, which is the framer's fold. The framer can choose the other route, a verifying round spawned for a doubted close, since the core's row is a floor and a round may always read a pass. That route costs a round where the snippet costs a line of the sealer's prompt.

```markdown
A close the
orchestrator doubts goes into the verifying round's spawn prompt, since that
round weighs every close. Where the row *No fix that no round reads* of
`skills/core/SKILL.md` *Judgment is not licence to skip a party* gives the
pass to the sealer and no round follows it, the doubt goes into the
sealer's spawn prompt, since the sealer reads that close at step 4 of
`agents/sealer.md`. The orchestrator does not rewrite the block.
```

### 5. The section still owes a verifying round after a `must`'s and a `reopens:` finding's fix pass that the core's row gives to the sealer

```seal
severity: should
location: `skills/code-review/orchestration.md:164-166`, `skills/code-review/orchestration.md:216-217`, `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/changelog.md:6`
evidence: executed `git grep -n -i -E "verifying round|one more round|its round\b" -- agents skills docs templates` in the round's clone, each line it printed read; read `skills/code-review/orchestration.md:126-136`, `:155-171`, `:209-227`
```

Why it matters: after this work two sentences of one section give two answers for the same pass, and the orchestrator picks one.

The new paragraph says that where no line names the record with the words, "no round follows the pass" (`skills/code-review/orchestration.md:133-135`), whatever the finding was. The same section says "From that row on, a `must` gets its fix pass and its verifying round" (`:165-166`), and "A finding of that round that carries a `reopens:` line gets its fix pass and one more verifying round" (`:216-217`). Neither carries the core's exception. For a `must` or a `reopens:` finding located in the records and fixed in the records alone, the new paragraph sends the orchestrator to the sealer, and these two sentences send it to a round. The regression sentence had the same shape, and this work narrowed it (`:155-159`). The frame's G3 and G4 list that sentence and the one in *The run* only.

Method: `git grep` on "verifying round", "one more round" and "its round" over `agents`, `skills`, `docs` and `templates`, each printed line read. Of the lines that owe a round after a fix, `skills/code-review/gate-to-pull-request.md:51` and `:153`, `skills/implement/merge-order.md:30` and `skills/code-review/orchestration.md:280` speak of a fix outside the records, and `:225-227` and `skills/implement/orchestration.md:541` carry the exception. A rule stated without the words "verifying round" escapes this search, so the list is a sample.

The snippet replaces the sentence at `:165-166` and the clause at `:216-217`. The fix pass also owes `changelog.md:6`, whose bullet names the regression case alone.

```markdown
that row on, a `must` gets its fix pass, and its verifying round unless the
core's row gives that pass to the sealer. Every
```

```markdown
*Earlier rounds* states. A finding of that round that carries a `reopens:`
line gets its fix pass, and one more verifying round unless the core's row
gives that pass to the sealer; a round carrying a
```

## Confirmations

What matched: *Scope* item 1 is built at `skills/code-review/SKILL.md:84-99`. The four rows stand in the table, each *Compare* cell naming both sides and a read or a command. The sentence after the table names *Concurrency & atomicity* and *Security* by label, and the next sentence names the four record rows and cites the proofer's rule for which records they cover (read). `git grep -n -F "The last two rows" -- agents skills docs tests` prints only `docs/releasing/branch-and-release.md:221`, which is about another table (executed).

What matched: *Scope* item 3 and S4. `agents/proofer.md:129-133` names a round as the first reader at its target and the sealer as the first reader of a sentence a fix pass writes after the last round. `git grep -n -F 'the sealer, the first reader of each sentence' -- agents skills docs` exited 1 (executed).

What matched: *Scope* items 4 and 5 at `skills/code-review/orchestration.md:93-94`, `:126-136` and `:157-159`. The round record is committed "before it reads whether a round follows the pass", and the regression sentence cites the core's row by the words `tests/text/test_the_rules_have_one_owner.py` row 22 holds (read; that module passed, executed). Finding 1 is about what the paragraph's two branches say.

What matched: *Scope* item 6. `chain_check.py --worktree` printed no line at `frame/design.md` `## Rule changes`, so each `from:` stands in its file and no operation was named as a pin or a copy (executed). The `add` names `docs/running/the-agent-set.md` *What each party writes, and when*, a heading at `docs/running/the-agent-set.md:94` (read).

What matched: *Scope* item 7 at `seal/follow-up.md:47`. Its counts, 33 of 270 and 6 of 71, with 12 of 33 and 2 of 6, are G17's. It names the owner, and it names each mechanism's record in the shape of the #1612 and #1614 rows above it (read).

What matched: *Scope* item 8. The three cases stand, and the narrow runs passed (executed). `test_passes_a_last_records_regression_fixed_in_its_records_alone` covers what its sibling `test_passes_a_last_records_fixed_finding_that_touched_only_its_records` does not. The sibling reads one record, and `#channel` reads a `regression:` line only from the second record on (`chain_check.py:899-903`). The new case is a two-record chain whose last finding carries the line (read). The phase record's mutation runs that saw each case red were read and not re-run; the sealer's step 3 samples them.

What matched: `pr.md`'s two quotes stand word for word at `frame/plan.md:25`, in the *Failure scenario* cell of the `SubagentStop` `agent` row, and at `frame/questions.md:17`, in Q1's Status cell (read). The changelog's counts, 8 of 17 and 43 of 72, are the issue body's (executed: `gh issue view 1615 --json body,comments`).

`gaps.md` `## Not done` still names the sentence of `docs/forms/the-round-record.md` that phase 1 left, and the framer's `change` at `4bfd026ee` now reaches it. The entry records phase 1's decision and stays true at the target, so it is no finding. `trail/phases/phase-1.md:7` and `:11` quote the plan row and *Scope* item 4 as they read before the orchestrator narrowed them at `5b4e2f26d`. A phase record states the commit it was written at, so these are no finding either. Row 3's command takes a section's heading, and a file the records cite by path alone has none. Every `## Rule changes` operation carries a `file:` line, so the same `grep` with the path in place of the heading lists those, and this round opens no finding for it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check, `unverified`; this round ran three modules and six cases of `tests/skills/test_chain_check.py` | `seal/config.json` `Broad gate` | the orchestrator's broad run |
| Whether a proofer walks the record rows and a sealer runs step 4's diff read in a real run, `unverified` | `gaps.md:8`, `seal/follow-up.md:47` | the repository owner, through #1615's row of `seal/follow-up.md` |
| Whether `skills/code-review/gate-to-pull-request.md` *The preflight is yours, and it is not the broad gate* states the preflight's record arm truly, which `frame/questions.md` Q1 measured as not refusing where a round is owed | `skills/code-review/gate-to-pull-request.md:178`, `frame/questions.md:17` | the repository owner, through `pr.md` |
| *Figure against its text* over a real figure: this work item holds no image, so the row was not exercised | `skills/code-review/SKILL.md:87` | the next round of a work item whose frame holds one |

## Probes

| Command | Result |
|---|---|
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.0 --root <clone> --worktree`, before this record | exit 0; lines only for the missing round record, gate record and guarantee, none at `frame/design.md` |
| `bin/test -q tests/behaviour/test_the_sealer_guarantees.py tests/text/test_review_axes.py tests/text/test_the_rules_have_one_owner.py` | exit 0, `58 passed` |
| `bin/test -q tests/skills/test_chain_check.py -m 'rule("run-ends-with-verifying-round")'` | exit 3, an xdist `INTERNALERROR` before any case ran; the marker form was replaced by the next row |
| `bin/test -q -p no:xdist tests/skills/test_chain_check.py -k "last_records or verifying_round"` | exit 0, `6 passed, 254 deselected` |
| `git grep -n -F 'the sealer, the first reader of each sentence' -- agents skills docs` | exit 1, no line |
| `git grep -n -F 'ref' -- .git/HEAD` in the clone | exit 1, nothing on stderr: a path under the git directory reads as no match |
| `git grep -n -i -E "verifying round\|one more round\|its round\b" -- agents skills docs templates` | 35 lines, each read for finding 5 |

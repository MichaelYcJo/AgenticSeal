# Review round 2: 1795595957-the-next-round-is-a-fixs-first-reader

```seal
target: a5c5f4dbd, fixes 72b8642c1..a5c5f4dbd
```

This is a verifying round. The range read is `72b8642c1..a5c5f4dbd`: the fix pass at `fce5a7d1b`, the close blocks at `f14600436` and the framer's fold at `a5c5f4dbd`. The round ran in a `git clone --no-local` at the target under its scratch directory. The code read is the fix diff, `agents/sealer.md`, `skills/code-review/SKILL.md` and `skills/code-review/orchestration.md`, and the records the fold and the fix changed. The work item's records that state the present were each read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`, then `trail/phases/phase-1.md` and `trail/rounds/round-1.md`. No `pr.<lang>.md` stands, since `Commit and pull request language` is English. `seal/parity.json` is not declared. Outside the diff, this round opened `skills/code-review/orchestration.md:23-300` and `:372-385`, `skills/code-review/scripts/chain_check.py:840-1000` and `:1420-1530`, `agents/sealer.md:1-199`, `agents/proofer.md:20-40` and `:112-160`, `skills/code-review/gate-to-pull-request.md:66-120`, `docs/forms/the-round-record.md:90-112` and `skills/implement/orchestration.md:66-125` and `:536-543`.

Carried from round 1 and not re-established: the issue body's counts, 8 of 17 and 43 of 72, which round 1 read with `gh issue view`; the phase record's mutation runs; the `git grep` on "the sealer, the first reader of each sentence", since `agents/proofer.md` is outside the fix range; and `trail/subagentstop-probe.md`, which the range does not touch. Re-established here: what `chain_check.py#channel` and `#records` print at the last record, the counts of G18 for the two owlery rounds after a `reopens:` finding, and the round 1 evidence command of finding 5.

The spawn prompt asked whether two texts read one way. The first is the fold's sentence that sends a doubted close into the sealer's spawn prompt where no round follows a pass (`skills/code-review/orchestration.md:61-65`, `frame/design.md:51`). The second is `agents/sealer.md:23-25`, where the sealer's reference is "never an agent's word and never the summary in the prompt". They read one way. The Job sentence says what a verdict is judged against. A doubt is not a reference. It is a claim with a coordinate, which contract rule 5 has the sealer open, and the sealer then judges that close against the issue body and the tree. The doubt also changes no scope: step 4 already reads every `fixed` finding of the last record that the core's row gives to the sealer (`agents/sealer.md:105-122`), so a sealer that set the doubt aside would still read the close. One gap remains, and it is no finding. `agents/sealer.md:36-37` and `skills/code-review/gate-to-pull-request.md:89-90` list what the sealer's prompt carries, and neither names a doubt. Neither list says "and nothing else", and the verifying round's prompt has the same shape: `agents/proofer.md` names no doubt either, and the proofer weighs every close anyway.

## Findings

### 1. The changelog bullet now names three cases, and its count still covers the regression rounds alone

```seal
severity: should
location: `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/changelog.md:6`
evidence: read `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/changelog.md:6`, `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/frame/design.md:28`, `:114`; executed `git show <commit>:seal/threads/1795591289-225-the-broad-gate-hands-a-panes-owlery/trail/rounds/round-<n>.md | grep -n -E '^(target|severity|location|verdict|regression|reopens|confirms):'` in owlery for rounds 2, 3 and 4, each at the last commit `git log --all -1` names for it
regression: round-1#5
```

Why it matters: `changelog.md` becomes the release note. A reader takes its last sentence as the catch record of the rounds this change removes, and the sentence reports none of the rounds that found something.

At `fce5a7d1b` the fix pass widened the bullet's subject from the regression case to three cases: "A regression's fix pass that touched the records alone takes no verifying round, and neither does such a pass for a `must` after the row that judges the run excessive or for a `reopens:` finding". The sentence that ends the bullet stayed as it was: "the two such rounds after #1507 found nothing". With the new subject, "such rounds" are the rounds after a records-only fix pass in any of the three cases. The frame counts four of those, not two. G18 (`frame/design.md:28`) lists two rounds after a `regression:` finding, which found nothing. It lists three rounds after "a `reopens:` or a plain fix", which found 1, 0 and 2. The folded `## Removes` row (`frame/design.md:114`) splits them: "the two after a `regression:` finding found nothing, and the two after a `reopens:` finding found one and nothing". This round read owlery's records to check that split. Round 2 of `1795591289-225-the-broad-gate-hands-a-panes-owlery` holds one finding, located in `changelog.md` and `frame/design.md`, carrying `reopens: round-1#3` and closed `fixed ca92695b`. Round 3 read that pass and found one finding, itself carrying `reopens: round-2#1`. Round 4 read that pass and found nothing. So of the four such rounds, one found a finding, and the bullet says that none did.

This sets the fix beside the frame. Phase 1's row of `frame/plan.md` and *Scope* item 5, as it stood at `fce5a7d1b`, covered the regression sentence alone. Round 1's finding 5 asked for the `must` and `reopens:` cases and named `changelog.md:6` for the fix pass. The fix pass widened the bullet's opening sentence and left the count, which was written for the old subject. The defect comes from the fix and not from the frame, because G18 already held the numbers that disagree.

The snippet replaces the bullet's last sentence. The fact has two other statements. `frame/plan.md:36` counts the regression case alone and is still true. The `## Removes` row already holds the split. So no other statement is owed.

```markdown
Counted on 2026-11-25 over this repository and one other that runs the chain, the two such rounds after #1507 that followed a regression found nothing, and the two that followed a `reopens:` finding found one finding between them; none followed a `must` after that row.
```

### 2. *Scope* item 4 places the paragraph on a doubted close in a section it is not part of

```seal
severity: should
location: `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/frame/design.md:51`, `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/frame/design.md:14`
evidence: read `skills/code-review/orchestration.md:23`, `:54-65`, `:95-99`, `:112`, `seal/threads/1795595957-the-next-round-is-a-fixs-first-reader/frame/design.md:14`, `:51`; executed `grep -n '^## ' skills/code-review/orchestration.md` in the round's clone
```

Why it matters: the sealer reads *Scope* against the diff at step 4. A coordinate that names the wrong section gives it a disagreement between the design and the build that the build did not cause.

*Scope* item 4 opens on `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*. The fold at `a5c5f4dbd` added this clause to it: "the section's paragraph opening **The orchestrator writes no close block of a finding the fix pass answers** says so beside the verifying round's prompt" (`frame/design.md:51`). That paragraph stands at `skills/code-review/orchestration.md:58`, under *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer* (`:23`). The section *Scope* item 4 names starts at `:112`. G4 (`frame/design.md:14`) makes the same slip for the paragraph opening **On the hand-back that leaves no finding open for a fold**. It calls that paragraph "The section's paragraph ... (line 91)", but its own range for the section is lines 108 to 145. So G4 was wrong at the commit it is dated to, and the dating does not cover it. The same paragraph now stands at `:95`, also outside the section.

This finding carries no `regression:` and no `reopens:` line. The fold is the framer's commit, not a fix pass's. Round 1's finding 4 asked for the doubt to reach the sealer, and its close holds (confirmed below). The defect is a coordinate the fold added.

Both lines are frame statements, so this is a fold, with the framer or the orchestrator as its writer by `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*. The snippet gives the two phrases.

```markdown
and the paragraph opening **The orchestrator writes no close block of a finding the fix pass answers**, in *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer*, says so beside the verifying round's prompt
```

```markdown
The paragraph opening **On the hand-back that leaves no finding open for a fold** (line 91), in the section before this one,
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `skills/code-review/orchestration.md:130-145` no longer offers a stop where a round is owed. A round follows where the output names the record with the words "a verifying round is owed", and a line that names the record in other words goes back to the party that wrote it. This round read what `chain_check.py#records` and `#channel` print at the last record (`chain_check.py:881-956`, `:1420-1528`). Each of those lines takes one of the paragraph's three branches. The paragraph's reason for the second branch is too narrow for two of them. "the check could not read the record as the pass left it" fits a block `round_read` refuses. It does not fit a `fixed` whose commit HEAD does not descend from, or one whose commit changed no path its `location:` names (`:1430-1453`): the check read both and refused what they say. The action the paragraph orders still fits both, since the fix pass repairs its own close block, so this is no finding (read). `changelog.md:5` reads "where no line of the output names that record" (read). The run in the round's clone printed the words at each of round 1's findings and at line 0 for `fce5a7d1b`, which touched `agents/sealer.md` (executed, Probes).

```seal
confirms: round-1#2
```
What holds: `agents/sealer.md:113-118` reads the sentences the diff adds or rewrites "in the records" the proofer's rule names, and the other statements "in those records". The rule reads "the files step 3 reads whole" (`agents/proofer.md:116-118`), and the last round record and `trail/gate.md` are not among them. The two commands and the `withheld` phrase stand, and `tests/behaviour/test_the_sealer_guarantees.py` passed (executed). `changelog.md:4` and the folded *Scope* item 2 (`frame/design.md:49`) state the same scope (read).

```seal
confirms: round-1#3
```
What holds: the rows *Record against record* and *Record against another work item's frame* (`skills/code-review/SKILL.md:85-86`) list the statements with `grep -rn` and `grep -n` over `seal/threads/`, which read a records root that no commit holds. The folded *Scope* item 1 (`frame/design.md:46-47`) names the same commands (read).

```seal
confirms: round-1#4
```
What holds: `skills/code-review/orchestration.md:58-65` sends the doubt to the sealer's spawn prompt where the core's row gives the pass to the sealer. The design's `change` on `docs/forms/the-round-record.md` now reaches "It edits no line in that commit, and a close it doubts goes into that round's spawn prompt", and its `to` sends the doubt to the sealer's prompt where no round follows. `chain_check.py --worktree` printed no line at `frame/design.md` (executed), so the extended `from:` stands in its file and no notice named a test pin or a copy. No other unsettled design changes that sentence: `grep -n -F` on "a close it doubts", "edits no line in that commit", "once for the whole pass" and "close block has one writer" over the other designs printed only `1794383427-asserts-pin-literal-phrases/frame/design.md:244`, which cites the `check:` line after the paragraph (executed). The answer to the spawn prompt's doubt about this sentence is above the findings.

```seal
confirms: round-1#5
```
What holds: the `must` sentence (`skills/code-review/orchestration.md:175-176`) and the `reopens:` clause (`:226-228`) carry the core's exception. The folded *Scope* item 5 and the first `## Removes` row name both (read). The close says round 1's evidence command printed "37 lines" at `fce5a7d1b`. This round ran it at `72b8642c1`, `fce5a7d1b` and `a5c5f4dbd`, and it printed 35 lines at each (executed). The lines the close names do stand as it says (read), so the count is no finding, since nothing turns on it. Finding 1 of this round is a regression from the same fix, in `changelog.md:6`.

What matched: round 1's method was a line-based `git grep`, so it could not see a phrase split across two lines. This round searched the same files again with each paragraph joined into one line first (executed, Probes). That search found two more sentences that assume a round follows every fix pass. `skills/code-review/orchestration.md:82-86` folds a statement the fix pass's hand-back names "before it spawns the verifying round". `:381-383` commits a rewritten `pr.<lang>.md` rendering "before it spawns the next round". Where no round follows, neither sentence gives a time. Both acts are still ordered, though. `skills/implement/orchestration.md:119-120` commits a fold "before the spawn or the resume", which includes the sealer's spawn. `seal pr-body` refuses a stale rendering before the sealer is spawned (`skills/code-review/gate-to-pull-request.md:96-116`). So this round opens no finding for either. Both lines are outside the fix diff, and round 1's close called its list a sample.

What matched: `frame/plan.md:58`, the new row of *Judgments of the run*, records that the six statements went to the framer's fold, and the fold diff changes *Scope* items 1, 2, 4 and 5, the `change` on `docs/forms/the-round-record.md` and the first `## Removes` row (read). `pr.md`'s two quotes stand at `frame/plan.md:25` and `frame/questions.md:17`, lines the range did not change (read). The fix range adds no test, so no new case is read against its group.

`gaps.md` `## Not done` still names the sentence of `docs/forms/the-round-record.md` that phase 1 left. Round 1 judged that it records phase 1's decision, and the fold's wider `change` does not make it false, so it is still no finding. *Scope* item 5 quotes the old wording, "its fix pass and its verifying round", to identify the sentence the build changed. At the target a comma follows "fix pass", so `grep` on the quoted words finds nothing there. The `## Removes` row names the same sentence by its opening words, which still stand. This round opens no finding for it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check, `unverified`; this round ran five modules | `seal/config.json` `Broad gate` | the orchestrator's broad run |
| Whether a proofer walks the record rows and a sealer runs step 4's diff read in a real run, `unverified` | `gaps.md:8`, `seal/follow-up.md:47` | the repository owner, through #1615's row of `seal/follow-up.md` |
| *Figure against its text* over a real figure: this work item holds no image | `skills/code-review/SKILL.md:87` | the next round of a work item whose frame holds one |

## Probes

| Command | Result |
|---|---|
| `python3 skills/code-review/scripts/chain_check.py --baseline a9cc9cf93 --root <clone> --worktree`, before this record | exit 0; "a verifying round is owed" at each of round 1's five findings and at line 0 for `fce5a7d1b`; lines for the missing gate record and guarantee; none at `frame/design.md` |
| `bin/test -q tests/behaviour/test_the_sealer_guarantees.py tests/text/test_review_axes.py tests/text/test_the_rules_have_one_owner.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_a_cited_section_stands_in_its_file.py` | exit 0, `127 passed` |
| `git grep -n -i -E "verifying round\|one more round\|its round\b" <commit> -- agents skills docs templates \| wc -l` at `72b8642c1`, `fce5a7d1b` and `a5c5f4dbd` | 35 at each |
| a `perl -0777` pass over each tracked `.md` file under `agents`, `skills`, `docs` and `templates`, each paragraph joined into one line, printing each sentence holding "verifying round", "one more round" or "next round" | 50 sentences, each read; two more that assume a round after every pass, `skills/code-review/orchestration.md:82-86` and `:381-383` |
| owlery: `git show` of `1795591289-225-the-broad-gate-hands-a-panes-owlery` rounds 2, 3 and 4, their field lines | round 2's finding carries `reopens: round-1#3`, located in records; round 3 holds one finding carrying `reopens: round-2#1`; round 4 holds only `confirms: round-3#1` |
| `grep -n '^## ' skills/code-review/orchestration.md` | sections at lines 23, 112, 269 and 399 |

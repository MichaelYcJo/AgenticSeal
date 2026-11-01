# Review round 1: 1793490088-each-kind-of-restatement-is-measured

```seal
target: 20e300df against origin/release/v0.27.1
```

The round reviews the branch `chore/1147-each-kind-of-restatement-is-measured` at `20e300df` against `origin/release/v0.27.1` at `bf9efcba`. The diff holds this work item's seven records and nothing else. No earlier round exists, so no fact is carried; every coordinate below was opened this round. The work is an audit, so the axes are the plan's *Technical context* list: each row's command repeats its count at `bf9efcba` (S1), each drifted instance is opened (S2), each decision's grounds are read against `skills/core/SKILL.md` *The rule a mechanism is kept against* (S3), each draft is read (S4), the joined comment is measured (S5), and the diff's paths are listed (S6). The two orchestrator rows of `frame/plan.md` *Judgments of the run* add two axes of their own. The first is whether K10 and K12 are measured. The second is the owner's direction that the audit writes no restatement of its own: each figure stands once, each figure carries its commit, the tracker overlap is named, and no decision stands silently against the policy at `bf9efcba`.

## Findings

### 1. D1 keeps the agent definitions' sanctioned passages as stored text in the paste check, and its *Done when* cannot be met in the milestone it proposes

```seal
severity: must
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md:593`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md:599`
evidence: read `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md:593`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md:599`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md:25`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md:28`, `docs/what-a-script-gates.md:53`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py:188-219`
```

Why it matters: D1 is the issue the orchestrator files and another work item builds. The build would follow a design that stands against the rule this audit applies.

The grounds:

- D1's *Scope* says "the module names the sanctioned passages of the agent definitions by their text, so a new copy between two definitions fails and a sanctioned one needs no edit to the table" (`phase-1.md:593`). The module would then hold the text of six passages of `agents/*.md`. That is a copy kept beside the tree to stay in step with it, which is what `skills/core/SKILL.md` *The rule a mechanism is kept against* forbids in "Nothing is kept beside the tree to stay in step with it, such as a stored count or coordinate". K2's own grounds apply that sentence to `BASELINE` (`phase-1.md:25`).
- A copy of a definition's wording held by a case is also a phrase pin. K5's decision removes phrase pins, on `docs/what-a-script-gates.md:53` "a case pins a fact a reader acts on; one that pins wording goes" (`phase-1.md:28`). D1 adds the kind of pin D4 removes.
- The claim "a sanctioned one needs no edit to the table" does not hold. A sanctioned passage reworded in its definitions no longer matches the stored text, so the check refuses it until the module's copy is edited. That is the cost of the stored count the row says goes.
- The *Done when* says "the module stores no count" (`phase-1.md:599`). The same *Scope* says "The `README.md` entries leave when #1102 drains them". #1102 is in `release: 0.29.0`, and D1 proposes `release: 0.27.1`. At `bf9efcba`, `BASELINE` holds `("README.md", "skills/implement/SKILL.md"): 2` and `("README.md", "skills/implement/acts.md"): 1` (`tests/text/test_no_passage_is_pasted_into_a_second_file.py:188-219`). D1 cannot meet its *Done when* until #1102 lands.

The fix rewrites D1's *Scope* sentence on the agent entries and its *Done when*. It takes one of two forms. The form below leaves pairs of two agent definitions out of the corpus, on the grounds K2's row already gives: each passage between definitions is a fact about the file that holds it. The other form keeps a stored text, and then the draft weighs that copy against the core sentence and K5's decision instead of claiming it costs no edit.

```markdown
> **Scope.** Each of K2.6, K2.8 and K2.9 stays in one file, its home by `skills/implement/SKILL.md` *1. Read the documents that outrank the code first*, and the other place links to it by path and section. `tests/text/test_no_passage_is_pasted_into_a_second_file.py#BASELINE` loses every entry whose pair shares no run, among them the stale `README.md` with `skills/parity-setup/SKILL.md`. The module leaves a pair of two agent definitions out of what it counts, as it leaves `*.ko.md` out, since each passage between two definitions states a fact about the file that holds it (`trail/phases/phase-1.md` *The table*, row K2); a definition paired with any other file is still read. The module keeps no text of a passage. The `README.md` entries stay until #1102 drains them.
>
> **Done when.** The three passages each stand in one file; `BASELINE` holds no agent-definition pair and no entry but the `README.md` ones #1102 drains; a case shows a paste between an agent definition and a skill refused.
```

```seal
verdict: fixed b58bfdb0
answer: The finding holds, and D1 is split at #1102. D1's *Scope* and *Done when* take the first form above, so pairs of two agent definitions leave what the check counts and the module keeps no passage text; that keeps no copy beside the tree and adds no pin of wording, so it agrees with K5's decision. The paste-ready text left the `README.md` entries standing with no work named to remove `BASELINE`, so in my own words D1 now names them as the stored count `skills/core/SKILL.md` *The rule a mechanism is kept against* refuses in "Nothing is kept beside the tree to stay in step with it, such as a stored count or coordinate", standing only until #1102, and D2, the comment for #1102, hands #1102 their removal with `BASELINE`, the ratchet and its policy sentence. D1's title, *Rule change* and *Order* follow, and K2's *Decision*, *Grounds* and *Issue* cells in `trail/phases/phase-1.md` *The table* now say the same, the last reading D1, D2. Each part is achievable in the milestone its draft proposes.
```

### 2. D1, D3, D5 and D7 propose `release: 0.27.1` on its purpose alone, and do not weigh the sizing rule the design names for a draft's milestone

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md:601`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md:629`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md:667`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:952`
evidence: executed `gh issue list --milestone "release: 0.27.1" --state all --json number,state,title`, `gh api repos/:owner/:repo/milestones/77 --jq .description`, `git show bf9efcba:docs/issues-and-milestones.md`
```

Why it matters: the orchestrator files each draft in the milestone the draft proposes. A proposal that stands silently against a policy sentence is the third kind of finding the orchestrator's row of *Judgments of the run* names.

The grounds:

- Design G11 names `docs/issues-and-milestones.md` *A milestone answers when, and takes three shapes* as the grounds for "the reason its proposed milestone fits". That section states "**A release is sized by what has to be in effect before the next work item starts, and not by a count.**" and "**Three or four is a ceiling, not a target.**"
- `release: 0.27.1` holds eight open work items on 2026-11-01: #19, #1128, #1147, #1150, #1197, #1224, #1225 and #1228 (executed). Four more drafts would make twelve.
- Phase-1 D1's reason quotes only the description's purpose, "the reader fixes and the restatement audit" and "fixes, audits and removes, and builds no feat". D3, D5 and D7 cite D1's reason. None of the four says what in 0.27.2 needs its change in effect first, and none names the ceiling.

The fix rewrites D1's milestone paragraph so that it weighs the sizing rule, and D3, D5 and D7 keep citing it. The milestone itself stays the orchestrator's choice at filing.

```markdown
Proposed milestone: `release: 0.27.1`, or the next release that can take it. The 0.27.1 description's purpose is "the reader fixes and the restatement audit", a patch that "fixes, audits and removes, and builds no feat", and this removes a restatement and a stored count and adds no feat. Against it: the milestone holds eight work items on 2026-11-01, past the three or four `docs/issues-and-milestones.md` *A milestone answers when, and takes three shapes* gives as a ceiling, and nothing #1038 or #947 reads in 0.27.2 needs this change in effect first. The orchestrator weighs the two when it files D1, D3, D5 and D7.
```

```seal
verdict: fixed b58bfdb0
answer: The finding holds; the paste-ready paragraph was not applied, because it copies the 0.27.1 milestone description and leaves the choice open, where the drafts are filed as they say. `trail/phases/phase-1.md` *Drafts* now weighs every proposed milestone once against `docs/issues-and-milestones.md` *A milestone answers when, and takes three shapes*, its sizing sentence and its ceiling, with the counts of 0.27.1, 0.27.2 and 0.28.0 on 2026-11-01, and each draft states its own ground under it with no copy of a milestone description. D1, D3, D4 and D7 go to a new patch milestone, `release: 0.27.3`, four work items at the ceiling, after 0.27.2 and before 0.28.0, whose #1216, #1204 and #1215 start from what D1, D4 and D7 change; D5 goes to `backlog: review chain & agents`, since nothing needs it in effect first; D2 and D6 stay comments for #1102 and #1038, which add no work item.
```

### 3. K13 names no overlap with #506, an open issue on the same ground, which the phase's own tracker search returns

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:913`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:29`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:830`
evidence: executed `gh issue list --state all --search docstring --limit 15 --json number,state,title`, `gh issue view 506 --json body,milestone`
```

Why it matters: the owner's direction says the tracker is searched first and an overlap names the issue. K13 decides "nothing for the lists" and leaves the figure class to `seal/follow-up.md`. D7 repairs `hooks/lib/console.py:46`, a docstring stating a count of the inline copies. #1038 and the owner read K13's row without the open issue that already holds the class.

The grounds:

- The claim: *Command tracker* found "#1020, #1038, #1139, #1153, #1215, #1216 and #1229" on the same ground, and "No issue holds ... the three drifts of *Instances K13*" (`phase-2.md:830`).
- What I found: the command's own query `docstring` returns #506 second (executed). #506 is open in `backlog: review chain & agents` and is titled "design: an enumeration the tree does not hold in step, three times — the acts table, its marker, and a docstring nothing reads". Its item 1 is "Nothing pins a module docstring's enumeration to its module", which is the class of the `console.py:46` figure and of *Command lists*.
- *Instances K13*'s *Overlaps* line (`phase-2.md:913`) names `seal/follow-up.md`'s row and #1038's candidate 3, and not #506.

```markdown
The open part: a coordinate whose path has no directory, one in `tests/` or `evals/behaviour/`, a figure in code text, and a figure the keyword list does not spell. Overlaps: `seal/follow-up.md`'s figure row, which names the owner; #1038's candidate 3, through #1129; #506 (`backlog: review chain & agents`), an enumeration the tree does not hold in step, whose item 1 is a module docstring's enumeration of its module, the class of `hooks/lib/console.py:46`. D7 repairs that instance and builds nothing #506 proposes.
```

The fix also adds #506 to *Command tracker*'s list of open issues found (`phase-2.md:830`).

```seal
verdict: fixed b58bfdb0
answer: The finding holds. #506 now stands in *Command tracker*'s list and in *Instances K13*'s overlaps, in my own words where the paste-ready text calls `hooks/lib/console.py:46` the class of #506's item 1: that item's proposed case compares a module docstring's enumeration with its own module, and the `console.py` figure counts copies in other files under `skills/*/scripts/`, so the case would not reach it. No draft becomes a comment for #506, since the instance is not a catch #506's case would have made and K13's row leaves the figure class to `seal/follow-up.md`'s row; D7 repairs the instance. The first loop of *Command tracker* was run again on 2026-11-01, and #506 is the one open issue on K13's ground it returns that the list lacked, by reading the titles it returns.
```

### 4. Phase 1's *Phase-boundary run* names 18 modules as the ones its two searches found, and the two searches list 28 files at `bf9efcba`

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md:673`
evidence: executed `git grep -l -E 'ROOT[^\n]{0,40}("seal"|seal/)|("seal", "threads")' bf9efcba -- tests`, `git grep -l -E 'ls-files|os\.walk\(ROOT|glob\(.*ROOT.*\*\*' bf9efcba -- tests`, `git diff --stat bf9efcba HEAD -- tests`
```

Why it matters: the phase record is the crafter's executed claim of its phase-boundary run, and the sealer samples it as stated. The record says the run covered what two named searches list. It covered 17 of their 28 files, plus `tests/behaviour/test_docs_line_wrap.py`.

The grounds:

- The claim: "one command ran it and the modules found by two searches at `bf9efcba`", followed by a list of 18 modules (`phase-1.md:673`).
- What I found: the first search lists 14 files and the second 16. Their union is 28 files: 27 test modules and `tests/conftest.py` (executed). `tests/` does not differ between `bf9efcba` and `HEAD` (executed: `git diff --stat`, no output). The run left out 11 of the 28. Ten are test modules: `tests/behaviour/test_a_signer_declares_its_pact.py`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, `tests/behaviour/test_both_editions_carry_the_same_folds.py`, `tests/hooks/test_implementer_notice.py`, `tests/hooks/test_question_gate.py`, `tests/hooks/test_routing_edit_gate.py`, `tests/hooks/test_launch.py`, `tests/skills/test_seal.py`, `tests/test_conftest.py` and `tests/text/test_a_rider_reaches_its_file.py`. The eleventh is `tests/conftest.py`.
- Phase 2's crafter reports the same 28 at its branch head. That run holds all 28, with phase 1's records in the tree (`phase-2.md:991`), so no module is left unrun. The defect is phase 1's sentence, which gives a list of 18 as the searches' output.

The fix rewrites the sentence that names the modules. The module list after it stays as it is.

```markdown
With the records written, one command ran it and 17 of the 28 files the two searches list at `bf9efcba` (27 test modules and `tests/conftest.py`): those that read `seal/` of the tree, by `git grep -n -E 'ROOT[^\n]{0,40}("seal"|seal/)|("seal", "threads")' bf9efcba -- tests`, and those that walk the whole tree, by `git grep -l -E 'ls-files|os\.walk\(ROOT|glob\(.*ROOT.*\*\*' bf9efcba -- tests`, with `tests/behaviour/test_docs_line_wrap.py` added because it reads Markdown. The ten test modules the run left out are run by `trail/phases/phase-2.md` *Phase-boundary run*.
```

```seal
verdict: fixed b58bfdb0
answer: The finding holds; the two searches at `bf9efcba` list the files the finding counts (executed). The sentence in `trail/phases/phase-1.md` *Phase-boundary run* is rewritten in place as the paste-ready text has it, and it also names the ten test modules the run left out and says why `tests/conftest.py` needs no run of its own; the module list and the run's result after it stand as they were.
```

### 5. Three records restate a figure that has a home in a row, and four of the copies carry no commit

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:18`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/gaps.md:8`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/gaps.md:22`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/gaps.md:24`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:940`
evidence: read `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:18`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md:27-30`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:783`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/gaps.md:8-24`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:940-946`
```

Why it matters: the orchestrator's second row of *Judgments of the run* binds this work. It says "a count, command or decision stands once, in its kind's row of its phase record", that `gaps.md` and every draft cite the row, and that "every figure carries its commit". It makes a copy between the work item's records a finding whether or not the copy has drifted. None of the copies below has drifted, and each states a figure a second time.

The grounds:

- `frame/design.md:18`, G12, states the `bf9efcba` counts "5 lines under `skills/` and 24 under `.github/` (19 in scripts, 5 in workflows)" and "50". Phase 1's K9 row holds the first set as its *Held twice* cell (`phase-1.md:30`), and phase 2's *Command nones* prints the second (`phase-2.md:783`). The rows are the homes.
- `gaps.md:8` says "the four edition pairs", the count K4's row holds (`phase-1.md:27`), with no commit.
- `gaps.md:22` says "the two lists of the `seal/` layout". K3's row counts the same drift as "1 list" (`phase-1.md:26`), drawn in two holders. The copy states it in another unit, so a reader meets 1 in the row and two in the memo.
- `gaps.md:24` says "The three drifts" and "the three stream answers", the counts of K13's and K12's *Drifted* cells, with no commit.
- D7's title says "a docstring counts five copies where fourteen stand" (`phase-2.md:940`). Once filed, the issue states the figure with no commit, and D7's body names none either.

The fix rewrites each copy as a citation. It touches only these lines.

```markdown
design.md G12, the cell's second and third sentences:
Item 1's six shipped citations and 13 comment lines were counted at `6be0c1f1`, and item 3's 33 `check: none` lines at the same commit. Each row counts again at `bf9efcba`: `trail/phases/phase-1.md` *The table* row K9, and `trail/phases/phase-2.md` *Command nones*.

gaps.md:8   | Whether the sections of the edition pairs that `trail/phases/phase-1.md` *Instances K4* names as unread ...
gaps.md:22  The drifted row of `README.ko.md` and the drifted `seal/` layout that `trail/phases/phase-1.md` *Instances K3* and *Instances K4* name ...
gaps.md:24  The drifts `trail/phases/phase-2.md` *Instances K13* names and the stream answers its *Instances K12* names ...

D7 title:   `fix: two comments cite code the tree has moved, a docstring counts fewer inline copies than stand at bf9efcba, and three release scripts degrade stderr otherwise than the console module says every copy must; each is brought to the tree`
D7 body:    > The measure, at `bf9efcba`, is `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md` at the sealed commit, ...
```

```seal
verdict: fixed b58bfdb0
answer: The finding holds, and the class was listed by comparing every numeral and number word outside code spans and fences across `frame/design.md`, `frame/plan.md`, `gaps.md` and both phase records, then reading each value that stands in two of them; a figure in a code span, one below four followed by another word, and one written in other words are not compared, and `gaps.md` *Not verified* names that open part. Fixed: `gaps.md` rows on the edition pairs, the `seal/` layout and the drifts and stream answers, as the paste-ready text has them; D7's title without any count, its *Done when* naming its scope's items in place of counts, and its body at `bf9efcba`; and, beyond the finding's list, the suite's total time stated by both phase records (phase 2's K7 cell and *Command durations*' suite line removed), #1216's count of pinning cases (phase 2's K7 cell cites phase 1's row K5), D2's and D6's counts of passages and entry points, the two *Drafts* intros' counts, phase 2's *Whether the frame holds* citing G12 for the fiftieth `check: none` line, and phase 2 restating the comment length design S5 gives; every draft's measure line now carries `bf9efcba`. Not fixed: `frame/design.md:18`, G12, which is the framer's file and a write the crafter's definition does not name; `gaps.md` *Not done* records it, the hand-back names it for the orchestrator, and no record cites G12's copy any more.
```

### 6. K12 leaves the eight committed proofer cases unmeasured, and a record at `bf9efcba` and this round's regeneration both measure them

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:28`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:889`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/gaps.md:14`
evidence: executed `git fetch origin '+refs/pull/*/head:refs/pull/*/head'`, `python3 evals/scripts/replay_targets.py --case replay-1791382684-r2 --case replay-1791382684-r5 --case replay-1791384160-r2 --case replay-1791779434-r5 --out <scratch>/gen8`, `python3 evals/scripts/seed_defects.py --case seeded-279a580b --case seeded-8a100e13 --case seeded-ad447367 --case seeded-f1c9932d --out <scratch>/gen8`, `diff -r <scratch>/gen8/<case> evals/behaviour/proofer/<case>`
```

Why it matters: K12's row goes into the comment, and the comment is the audit's output. As written, the row's *Held twice* and *Drifted* cells cover 17 generated eval cases. They name the other 8 only through `gaps.md:14`, which hands them to this round. The measure was reachable at `bf9efcba`.

The grounds:

- The claim: "The 8 proofer cases `replay_targets.py` and `seed_defects.py` write were not regenerated: that needs the reviewed commits fetched through `refs/pull/*/head`" (`phase-2.md:889`).
- `seal/threads/1793457435-replay-targets-reads-both-layouts/guarantee.md:16` at `bf9efcba` already holds the measure: "the four seeded cases are identical and each replay case differs only in its scaffold's `git remote add origin` line". #1229, which K12's *Overlaps* names, also states it. The row did not open either.
- This round regenerated the 8 at `bf9efcba`. The clone had `refs/pull/*/head` fetched and `origin` set to the GitHub remote (executed). Both generators exited 0. The 4 seeded cases are byte for byte the committed ones. Each of the 4 replay cases differs in one line, `scaffold.sh:3`. It reads `git remote add origin …/AgenticSeal.git` as written and `…/SpecSeal.git` as committed. The generator reads that line from the clone's remote, so the difference is an input of the run and not a change in the generator.

The fix writes the measure into the row's one home and removes the `gaps.md` row.

```markdown
phase-2.md *Instances K12*, the sentence on the proofer cases:
The 8 proofer cases `replay_targets.py` and `seed_defects.py` write were regenerated by round 1 of this work item at `bf9efcba`, in a clone with `refs/pull/*/head` fetched: the 4 seeded cases are byte for byte their generator's output, and each of the 4 replay cases differs in its scaffold's `git remote add origin` line alone, which the generator reads from the clone's remote (`…/AgenticSeal.git` written, `…/SpecSeal.git` committed). `seal/threads/1793457435-replay-targets-reads-both-layouts/guarantee.md` *Scenario 5 after 9237e34b* holds the same result. Not counted as drifted. #1229 (`release: 0.27.2`) replaces the 8.

phase-2.md K12 row, *Held twice*: "... 17 eval cases that `evals/scripts/rule_cases.py` writes and 8 that `replay_targets.py` and `seed_defects.py` write, at `bf9efcba`"
phase-2.md K12 row, *Drifted*: "... and the 25 cases are their generators' output, the 4 replay scaffolds but for the remote their generator reads from the clone (*Instances K12*)"

gaps.md:14: the row is removed.
```

```seal
verdict: fixed b58bfdb0
answer: The finding holds. `trail/phases/phase-2.md` *Instances K12* now records the measure by citing this record's finding 6 and its *Probes* row for the two generators, with none of their figures, judges the replay scaffolds' remote line an input of the run and not drift, and cites `seal/threads/1793457435-replay-targets-reads-both-layouts/guarantee.md` *Claims re-run* for the same result; K12's *Held twice* and *Drifted* cells name the proofer cases and cite that measure. The `gaps.md` row is marked `closed` with what closed it instead of removed, since `skills/implement/SKILL.md` *4. The closing memo* closes an item by marking it, never by deleting it.
```

## Confirmations

```seal
confirms: none
```
What matched: S1 holds for every command block of both records. The claim: "Every command block above was run again from a fresh scratch copy after this record was written, and each printed the figure its block states" (`phase-1.md:673`, `phase-2.md:993`). I extracted all 34 sh blocks except the two *Command tracker* blocks from the records at `20e300df`. I ran them in order with `sh` from a `git clone --no-local` of the worktree, and each printed the figure its block states (executed). The figures checked: K1 0/153; K2 9/793; citations 31; baseline 61/16/1, with `README.md + skills/parity-setup/SKILL.md: stored 1, now 0`; both durations blocks to the hundredth; K3 2/422; trees, with `skills/implement/SKILL.md` lacking `config.md` and the table listing four names; K4 10 sections and four outlines `same`; K5 518 in 57 and 0/6786; K6 1/705 and `cmp exit 0`; templates 33/17 and 14/5; K9 29, 5 and 19; phase 1 caught 24; K7 5/477 and 4/684; quotes 2/2; K8 36 fragments, 0 missing; K10 33/226; K11 50/3168; K12 62, 100 and 60 passages with holders 164, 220 and 367; clones 4, 3 and 0; entry 47, with the tally 16/13/10/5/3; regenerate exit 0, no `differs:` line, 17; layout exit 0 and 0; coordinates 9/113/3; lists 33; figures 33; history 62, 24 and 14; nones 49/40/26 and 50; cited 3180 records at 32 tags, 4 and 30/15; phase 2 caught 47. *Command K8*'s `releases` line failed on the first run because my clone's `origin` named the local worktree. Run again with `origin` set to the GitHub remote, it printed `fragments 36; not in their Release 0` (executed).

```seal
confirms: none
```
What matched: S2. Each drifted instance the rows name, opened at `bf9efcba` (read). K4: `README.md:181` has "and the two moves that load a release" and `README.ko.md:174` does not. `0d9e0d55` (2026-09-08) changed both READMEs and stands in 35 `v` tags, the first `v0.13.1` (executed: `git tag --contains`). K3: `skills/implement/SKILL.md:102-118` draws `seal/` without `config.md`, and `docs/the-record-layout.md` *seal/* tables no `parity.md` or `pact.md`. K12: `.github/scripts/release_report.py:315`, `release_seal.py:536` and `rules.py:516` reconfigure with `errors="replace"`, and `hooks/lib/console.py:57` gives `stderr` `backslashreplace`. K13: `hooks/lib/cmdline.py:28` cites `hooks/dispatch.py:72`, which reads `FAILED = []`. `tests/behaviour/test_release_hygiene.py` defines no `overwide_rows` at `bf9efcba` (executed: `git grep`, no output). `hooks/lib/console.py:46` says "five", and 14 files under `skills/*/scripts/` hold `for _name, _errors in` (executed).

```seal
confirms: none
```
What matched: S5 and S6. *Command comment* joined the preamble and the 14 rows with exit 0 into 23,834 bytes and 23,832 characters, under 65,536 (executed). `git diff --name-only bf9efcba..HEAD` prints seven paths, each under `seal/threads/1793490088-each-kind-of-restatement-is-measured/` (executed).

```seal
confirms: none
```
What matched: the orchestrator's first row of *Judgments of the run*. K10 has its row, `phase-2.md:26`, with its command and its 33 passages read. K12 has its row, `phase-2.md:28`, with five readers (read, executed above). Each decision's grounds quote a sentence of `skills/core/SKILL.md` *The rule a mechanism is kept against* or the policy section that decides the kind, and weigh what the mechanism caught against its cost (read: `phase-1.md:24-30`, `phase-2.md:24-30`). Apart from findings 1 and 2, no decision stands against a sentence I opened at `bf9efcba`. Those sentences: `docs/the-review-record.md:23`, `docs/what-a-script-gates.md:53`, `docs/one-root-by-lifetime.md:44`, `docs/the-record-layout.md:333` and `:348-350`, `docs/release-checklist.md:20`, `docs/issues-and-milestones.md:290`, `CONTRIBUTING.md:431` and `hooks/lib/console.py:49`. Each rule a draft changes is named by its sentence and file, and goes through the building work item's `## Rule changes`. The one exception is D6's `CONTRIBUTING.md` sentence, and D6 says why: `CONTRIBUTING.md` lies outside the policy root.

```seal
confirms: none
```
What matched: the tracker half of the owner's direction, except finding 3. D2 and D6 are comments for the open issues that hold their ground, #1102 and #1038, and not new issues (read: `phase-1.md:605-613`, `phase-2.md:925-936`). Phase 1's tracker queries, run again, return no open issue on D1's, D3's, D4's or D5's ground that the rows do not name (executed: the first loop of phase 1's *Command tracker*, open issues only). I also ran `parity.md`, `record layout`, `layout tree`, `cmdline`, `dispatch.py`, `stderr`, `backslashreplace` and `STREAMS`, and they return none either (executed).

```seal
confirms: none
```
What matched: two `gaps.md` rows that name this round as their answerer. First, the `path#name` coordinates under `tests/` and `evals/behaviour/` (`gaps.md:18`). A probe with *Command coordinates*' name pattern and definition test, run over the scratch copy of `bf9efcba`, read 111 such coordinates, and 5 name no definition in their file (executed). By reading, none has drifted. `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py:637` and `tests/hooks/test_config.py:1111` state in the past tense a case and a function that are gone. The three seeded graders name functions at the seeded commit, not of the tree. Second, the core sections that `agents/` and `skills/` cite (`gaps.md:9`). `git grep` on the path `skills/core/SKILL.md` lists each citation with a section. Those are `agents/framer.md:206`, `skills/code-review/orchestration.md:145`, `skills/implement/orchestration.md:96`, `:366` and `:372`, and `skills/settle/SKILL.md:226`, and each says what its section says (read). A citation of the core in words, without its path, is not listed, so the second list is a search on one spelling.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The prose of the sections of the four edition pairs other than README *The gates*, which `gaps.md:8` hands to this round. I read one more section pair, `docs/one-root-by-lifetime.md` *The dependency rule* against `docs/one-root-by-lifetime.ko.md` *종속 규칙*, and it states the same facts. The rest is unread. | `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md` *Instances K4* | the repository owner; #1102 rewrites both README editions in `release: 0.29.0` |
| Phase 2's *Command tracker*, run whole. I ran its `docstring` query and the searches the Confirmations name. | `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md` *Command tracker* | the next round, after the fix pass |
| The full suite, the repository-wide lint and the format check. Phase 2 hands the suite over as `unverified` with the orchestrator named, which is an honest label. This round leaves findings open, so the broad run does not come due yet. | `seal/config.md` *Broad gate* | the orchestrator, by `seal gate` once the rounds settle |
| Whether the four replay scaffolds' committed `origin` line changes what a proofer run of those cases reads. | `evals/behaviour/proofer/replay-1791382684-r2/scaffold.sh:3` | #1229's owner, at the measurement it holds |

## Probes

| Command | Result |
|---|---|
| `git clone -q --no-local <worktree> <scratch>/round-1/clone`, checked out at `20e300df` | the clone, 67 tags; every command below ran in it or in a copy made from it |
| `<scratch>/round-1/test_tmp_rerun.sh`: extracts each `#### Command <X>` sh block of `phase-1.md` and `phase-2.md` except *Command tracker*, and runs the 34 in order with `sh` from the clone | every block exit 0, except *Command layout*'s last line, whose `grep -c` prints `0` and exits 1 as its block states, and *Command K8*'s `releases`, which failed while `origin` named the local worktree; every printed figure is the one its block states |
| `python3 -I "$S/audit2.py" releases <clone>` with the clone's `origin` set to the GitHub remote | 16, 5, 4, 1, 2, 5, 3 fragments, 0 missing each; `fragments 36; not in their Release 0` |
| `git fetch origin '+refs/pull/*/head:refs/pull/*/head'` in the clone, then a worktree of it at `bf9efcba`; `replay_targets.py --case` for the four replay names and `seed_defects.py --case` for the four seeded names, `--out <scratch>/gen8`; `diff -r` of each against `evals/behaviour/proofer/<case>` | 299 pull refs; both generators exit 0; four seeded cases identical; each replay case differs in `scaffold.sh:3` alone, `…/AgenticSeal.git` written against `…/SpecSeal.git` committed |
| the two `git grep -l` searches of `phase-1.md:673` at `bf9efcba` over `tests`, and `git diff --stat bf9efcba HEAD -- tests` | 14 and 16 files, union 28 (27 test modules and `tests/conftest.py`); `tests/` unchanged |
| `<scratch>/round-1/test_tmp_names.py <scratch copy of bf9efcba>`: *Command coordinates*' `path#name` reader over `tests/` and `evals/behaviour/` | `path#name under tests/ and evals/behaviour/: 111; not defined: 5`, each read in Confirmations |
| `gh issue list --state all --search docstring --limit 15` | #506 second, open, in `backlog: review chain & agents` |
| `gh issue list --milestone "release: 0.27.1" --state all` | eight open issues: #19, #1128, #1147, #1150, #1197, #1224, #1225, #1228 |

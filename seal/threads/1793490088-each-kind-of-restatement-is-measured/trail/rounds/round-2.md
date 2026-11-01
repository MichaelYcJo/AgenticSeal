# Review round 2: 1793490088-each-kind-of-restatement-is-measured

```seal
target: d0e51dce, fixes 3b2aee91..d0e51dce
```

The round verifies the two commits after round 1's record: `b58bfdb0`, the fix pass over `gaps.md` and both phase records, and `d0e51dce`, the orchestrator's fold of G12 in `frame/design.md`, its row in `frame/plan.md` *Judgments of the run*, and round 1's close blocks. The base is `origin/release/v0.27.1` at `bf9efcba`. Carried from round 1, and not searched again: the coordinates of each finding, the two `git grep` searches of finding 4, the regeneration of the eight proofer cases (finding 6, not run again), and round 1's reading of the drifted instances (its S2 confirmation). Re-derived this round: every verdict below, the command blocks the fixes touched, the milestone counts, and the issues the drafts now cite. Round 1's *Not judged* gave *Command tracker* of phase 2, run whole, to this round, so its first loop was run and its returns were read against every row of phase 2, not only K13's.

## Findings

### 1. `gaps.md` *Not done* says G12 still states figures and was not rewritten, and the fold rewrote it

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/gaps.md:27`
evidence: read `seal/threads/1793490088-each-kind-of-restatement-is-measured/gaps.md:27`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:18`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/plan.md:62`
regression: round-1#5
```

Why it matters: the sealer and the settle read `gaps.md` *Not done* as what the work item left undone. This paragraph tells them a frame cell states figures that no longer stand there, and that a fix was never made.

The unit is the third paragraph of `gaps.md` *Not done*, which `b58bfdb0` added for round 1 finding 5. The frame's row for the fold (`frame/plan.md:62`) says G12 cites rows K9 and K14 and keeps no re-count of its own. The fold `d0e51dce` rewrote G12 that way (`frame/design.md:18`) but left this paragraph, which `b58bfdb0` wrote about the old G12, so the defect came from a fix that changed a fact and not the sentence written on it (contract rule 19).

The grounds:

- The paragraph says "`frame/design.md` G12 states figures at `bf9efcba` that `trail/phases/phase-1.md` *The table* row K9 and `trail/phases/phase-2.md` *Command nones* hold" and "The fix pass of round 1 did not rewrite G12" (`gaps.md:27`).
- G12 at HEAD reads "The comment counted item 1's citations and item 3's `check: none` lines at `6be0c1f1`. Each row re-counts its item at `bf9efcba` and holds the figure once". It states no figure (`frame/design.md:18`).
- The paragraph now names work as undone that was done, by the orchestrator, for reasons the plan's row records. *Not done* has nothing left to say about G12.

The fix removes the paragraph. The plan's row already records why the fold, and not the fix pass, rewrote G12.

```diff
 The drifts `trail/phases/phase-2.md` *Instances K13* names and the stream answers its *Instances K12* names were within reach and are not repaired here, for the same constraint. D7 carries them to their own work item.
-
-`frame/design.md` G12 states figures at `bf9efcba` that `trail/phases/phase-1.md` *The table* row K9 and `trail/phases/phase-2.md` *Command nones* hold, and the owner's comment figure at `6be0c1f1` that phase 2's row K14 holds. Round 1 finding 5 names the first two. The fix pass of round 1 did not rewrite G12: `frame/design.md` is the framer's (`skills/implement/SKILL.md` *3. The SDD file set*, column *Written by*), and the crafter's definition names no write to it. Each phase record cites its own rows and not G12, so no record leans on G12's copy.
```

### 2. Two figures in the frame remain in the class finding 5 named, inside the comparison its close describes, and the close names only G12

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/plan.md:32`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:90`
evidence: executed `python3 -I <scratch>/round-2/test_tmp_figures.py <scratch>/round-2/clone/seal/threads/1793490088-each-kind-of-restatement-is-measured`, `git show bf9efcba:seal/follow-up.md`
reopens: round-1#5
```

Why it matters: the owner's direction in `frame/plan.md` *Judgments of the run* says each count stands once, in its kind's row, and "every figure carries its commit". Finding 5's close says it found the class by comparing every numeral outside code spans across `frame/design.md`, `frame/plan.md`, `gaps.md` and both phase records, then reading each value found in two of them, and it names `frame/design.md:18` as the one line it did not fix. The close does not hold for the whole class: two more lines stand inside that comparison. Both are the framer's, as G12 was, so their fix is a fold like `d0e51dce`.

The grounds:

- `frame/plan.md:32`, the A4 alternative, says "538 files make about 145,000 pairs" and names no commit. The figure is G13's probe at `bf9efcba` (`frame/design.md:19`, "538 files read"). It stands in two records, and the copy carries no commit.
- `frame/design.md:90`, K12's *Record of drift in the issue* cell, says "`seal/follow-up.md`, the row on `console.to_utf8()`: 6 of 13 entry points call it", with no commit. The follow-up row measured that figure "2026-09-22 at `11f3cde8`", for the `.py` files under `.github/scripts/` (executed: `git show bf9efcba:seal/follow-up.md`, line 49). Phase 2 gives the figure at `bf9efcba` as "5 of the 14 `.github/scripts/` entry points" (`trail/phases/phase-2.md:883`). So the design states a figure about the tree with no moment, and the figure no longer holds at the audited commit. That is the class K13 measures, standing in the audit's own frame.
- The probe compared every figure in the five records, in code spans and fences included, written in digits or as a number word, and listed each value that stands in two of them. These are the two among them that state the audit's own measure, or another record's, without its commit. The other values found in two records are listed under *Confirmations* and hold.
- What does hold of finding 5's close: the `gaps.md` rows, D7's title, *Done when* and body, the K7 cell, the removed suite line of phase 2's *Command durations*, every draft's measure line carrying `bf9efcba`, and the fold of G12. The suite's 994.8 s now stands once, in `trail/phases/phase-1.md:25` and the block it cites.

The fix rewrites the two cells to cite their homes.

```markdown
frame/plan.md:32, the A4 alternative's failure cell:
Every pair of the files design G13's probe reads at `bf9efcba`, and the reading would still not be whole, because a paraphrase has no bounded spelling

frame/design.md:90, K12's cell *Record of drift in the issue*:
`seal/follow-up.md`, the row on `console.to_utf8()`, measured at `11f3cde8`
```

### 3. *Instances K11* says no open issue reads its class, and phase 2's own tracker search returns four that hold docstrings out of step with their code

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:875`
evidence: executed `sh <scratch>/round-2/blocks/phase-2-tracker-loop.sh`, `gh issue view 146`, `gh issue view 317`, `gh issue view 706`, `gh issue view 710`, `git show bf9efcba:.github/scripts/roll_flow_measurement_issue.py`, `git show bf9efcba:skills/verify/scripts/arm_check.py`, `git grep -n 'wrote nothing' bf9efcba -- skills/verify/scripts/mutation_check.py`
```

Why it matters: the owner's direction says "the tracker is searched first, and a decision an open issue covers names that issue". K11's row goes into the comment that #1038 and the owner read. *Instances K11*, which K11's row cites, tells them no open issue covers this class. Round 1 finding 3 applied the same clause to K13. The fix pass read the loop's returns for K13's ground alone ("#506 is the one open issue on K13's ground it returns that the list lacked"). Round 1 gave the whole loop to this round, and the loop's returns hold the same defect on K11.

The grounds:

- K11's row counts, in its *Caught in the record* cell, the findings where "a docstring or a stated limit [is] out of step with a rule text or with the code" (`trail/phases/phase-2.md:27`). So the row places a docstring out of step with its own code in K11.
- *Instances K11* ends: "Overlaps: none of the open issues reads this class" (`trail/phases/phase-2.md:875`).
- The first loop of phase 2's *Command tracker*, run on 2026-11-01, returns four open issues in `backlog: review chain & agents` on that ground (executed). #146: a module docstring of `.github/scripts/roll_flow_measurement_issue.py` describes code that changed. #317: `arm_check.py#Verdict`'s docstring defines its fields as they were before a fix. #706: a comment of `mutation_check.py`'s `main` is behind the code. #710: two comments of `arm_check.py` name the wrong cause.
- Three of them still stand at `bf9efcba` (executed). `.github/scripts/roll_flow_measurement_issue.py:76-77` says a lag "can only ever produce a reading that is short a result, never one with an extra issue in it", and the same file at `:452-453` says a lag behind a close "is a reading with an extra issue in it rather than one short a result". `skills/verify/scripts/arm_check.py:736-738` holds the sentence #317 quotes, "the whole reason `refused` exists". `skills/verify/scripts/mutation_check.py:574` holds the comment #706 names, "An interrupt during the baseline wrote nothing". This round did not re-derive whether the code behind #706's and #710's comments is what those issues say.
- The open part of K11 names "a docstring that restates a rule in fresh words", and not a docstring out of step with the code it describes. No command of phase 2 reads that half of the class, and the record does not say so.

The fix rewrites the last paragraph of *Instances K11*, and changes no decision.

```markdown
The open part: a docstring that restates a rule in fresh words, a docstring or comment out of step with the code it describes, which no command here reads, and a printed message built by concatenation of pieces under four words. Overlaps: #146, #317, #706 and #710 (`backlog: review chain & agents`), each a docstring or comment of a script out of step with the code it describes; at `bf9efcba` the sentences #146, #317 and #706 name still stand (`.github/scripts/roll_flow_measurement_issue.py`'s module docstring, `skills/verify/scripts/arm_check.py#Verdict`, `skills/verify/scripts/mutation_check.py#main`). No draft extends them, since K11's decision is a written rule the proofer reads and each issue repairs its own instance.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: D1 no longer keeps any passage's text, and its *Done when* can be met in the milestone it proposes (read: `trail/phases/phase-1.md:587-604`). The claim: the module leaves a pair of two agent definitions out of what it counts, "as it leaves `*.ko.md` out". At `bf9efcba`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py#test_the_corpus_is_found` asserts that no `.ko.md` file is in the corpus, so the comparison is to a rule the module already holds (read). `BASELINE` at `bf9efcba` holds 16 entries. Ten are pairs of two agent definitions, which leave by D1's exclusion. Three are `README.md` pairs: D1 removes the stale one with `skills/parity-setup/SKILL.md`, and keeps the two that #1102 drains. The other three are the pairs of K2.6, K2.8 and K2.9, which share no run once each passage has one home (read: the module at `bf9efcba`, lines 188-222; *Instances K2*). So after D1 the table holds the two `README.md` entries alone, which is its *Done when*, and nothing in it waits on #1102. D1 says in its *Scope* that those two entries are the stored count the core refuses, and that they stand until #1102. The phase's *Drafts* intro names that standing as well, so no decision stands silently against the core. K2's row cells say the same as the draft. *Command baseline* run again prints `corpus 61 files; 16 stored pairs; 1 differ from now` (executed).

```seal
confirms: round-1#2
```
What holds: each draft's milestone is weighed against `docs/issues-and-milestones.md` *A milestone answers when, and takes three shapes* at `bf9efcba`, by its sizing sentence (line 23) and its ceiling (line 32). I judged each placement against those lines:

- **The counts.** `release: 0.27.1` holds 8 issues, `release: 0.27.2` 9 and `release: 0.28.0` 9 on 2026-11-01, all open (executed: `gh issue list --milestone "<title>" --state all`). The *Drafts* intro states the same (`trail/phases/phase-1.md:585`). Each is past the ceiling, so none of the three takes a draft.
- **D1 and D4 to 0.27.3.** #1216's *Done when* names each `to` sharing a 15-word run "by the reader `test_no_passage_is_pasted_into_a_second_file.py` uses", and each pin of a `from` under `tests/` (executed: `gh issue view 1216`). D1 sets which pairs that reader counts, and D4 removes the pins of wording. So what #1216 reports depends on both, and both need to be in effect before #1216 starts. That is the sizing sentence's test.
- **D3 and D7 to 0.27.3.** Each fixes a drift a reader acts on at `bf9efcba`. D3 fixes the `seal/` tree in the skill every building party reads. D7 fixes code text that cites moved code and a stderr handler three release scripts print by. A patch "fixes, audits and removes" (the 0.27.1 description). Line 48 asks only that a patch's purpose say it builds no `feat:`, and D3 and D7 are `fix:`. D7's second ground is that #1204 and #1215 edit the same files. That is an order, which a milestone's order line settles, not a need. It does not carry the placement, and it does not make the placement wrong.
- **The ceiling.** The four items of 0.27.3 sit at the ceiling, which line 32 allows ("Three or four is a ceiling, not a target").
- **The description.** Line 46 asks a scheduled release milestone's description to state its purpose and the grounds for its order. The intro gives the purpose: each item removes a restatement or a stored copy, and none builds a `feat:`. Each draft gives its order: D1 and D3 one after the other, D4 after #1197, and D7 beside both. The orchestrator writes the description from these when it creates the milestone.
- **D5 to `backlog: review chain & agents`.** D5 repairs no drift and has no item that needs it first. Line 15 gives `backlog:` to "work with no release yet, bucketed by area". The milestone's description, "Rounds, verdicts, the cap, coverage questions, and the agents that run the chain" (executed: `gh api repos/:owner/:repo/milestones/3`), covers two of the three skills D5 edits.
- **D2 and D6.** Each is a comment on the open issue that holds its ground, #1102 in 0.29.0 and #1038 in 0.27.2, and a comment adds no work item to a milestone.

```seal
confirms: round-1#3
```
What holds: #506 now stands in *Command tracker*'s list (`trail/phases/phase-2.md:829`) and in *Instances K13*'s overlaps (`:912`). The claim: #506's item 1 proposes a case comparing a module docstring's enumeration with that module, so the case would not reach `hooks/lib/console.py:46`, which counts copies in other files. #506's item 1 says "A case comparing the block's backticked names against the module's own AST closes it" (executed: `gh issue view 506`), so the reading holds. The same clause on K11's row is this round's finding 3, a new instance and not this close.

```seal
confirms: round-1#4
```
What holds: the sentence at `trail/phases/phase-1.md:677` names 17 of the 28 files the two searches list. Run again at `bf9efcba`, the searches list 14 and 16 files, 28 in their union (executed). Taking the record's 18 run modules out of the union leaves the ten test modules the sentence names and `tests/conftest.py` (executed). Phase 2's run names those ten as well.

```seal
confirms: round-1#6
```
What holds: *Instances K12* cites round 1's finding 6 and its *Probes* row for the measure, and states none of its figures. It judges the replay scaffolds' remote line an input of the run (`trail/phases/phase-2.md:888`). The row it cites stands as `seal/threads/1793457435-replay-targets-reads-both-layouts/guarantee.md:16`, under *Claims re-run* at line 9, at `bf9efcba` (executed: `git show`). The `gaps.md` row opens with `closed` (`gaps.md:14`), the mark `skills/implement/SKILL.md:443-444` gives at `bf9efcba` (read). The regeneration was carried from round 1 and not run again.

```seal
confirms: none
```
What matched: the command blocks the fixes touched, run again in order from a clone at `d0e51dce` with a fresh scratch copy of `bf9efcba` (executed). Phase 1's *Command durations* prints 4.70, 0.61, 0.09, 0.04, 0.48 and 1.28 s and `suite 994.8 s`. Phase 2's prints 5.80, 0.35, 2.51, 20.32 and 3.65 s, with no suite line. *Command baseline* prints the line under round-1#1 above. *Command K9* prints 29, 5 and 19. *Command nones* prints `check: none lines 49 in 40 sections, naming 26 readers`, then `50`, then `bf9efcba:tests/text/test_every_agent_reads_the_contract.py`. *Command comment* prints `join exit 0`, 24622 bytes and 24620 characters, which is the figure `trail/phases/phase-2.md:992` states. Each of its 14 rows and the header stand as whole lines in the two records, with no miss (executed: `grep -qxF`). The last commit to change either table is `b58bfdb0`, the commit the round 1 close blocks name. The first loops of both *Command tracker* blocks ran on 2026-11-01 with the clone's `origin` set to the GitHub remote. Phase 2's returns #506, open. Phase 1's returns no open issue on D1's, D3's, D4's or D5's ground that the rows do not name. Phase 2's returns are read in finding 3.

```seal
confirms: none
```
What matched: the fold of G12 (`frame/design.md:18`). G12 states no figure and cites row K9 and row K14. Row K9 holds 29, 5 and 24 (`trail/phases/phase-1.md:30`). Row K14 holds the 49 lines in the rule files and the comment's 33 at `6be0c1f1` (`trail/phases/phase-2.md:30`). The whole-tree 50, which differs from row K14's 49, is printed by *Command nones*. Phase 2's departure line on K14 cites that block for the fiftieth line (`trail/phases/phase-2.md:14`). So G12's citation of row K14 is a citation of the row's own measure, and the difference is accounted for where the record says.

```seal
confirms: none
```
What matched: three `gaps.md` rows that name the proofer are answered.

- **Row 9, the core sections that `agents/` and `skills/` cite.** Round 1 read every citation that names the path `skills/core/SKILL.md`, and called the rest a search on one spelling. This round listed every line of `agents/*.md` and `skills/**/*.md` at `bf9efcba` that holds the word `core` in any case (executed: `git grep -n -i core`). One line cites the core in words: `skills/implement/orchestration.md:101-103`, "the settle weighs the exchange against what it cost under the core's mechanism rule". That is what *The rule a mechanism is kept against* says (read). The other lines name `seal core`, the `skills:` list or the hook.
- **Row 18, `path#name` coordinates under `tests/` and `evals/behaviour/`, and those written without their directory.** Round 1 read the first half. This round read the second half with `<scratch>/round-2/test_tmp_bare_names.py` over the scratch copy of `bf9efcba`, outside `seal/threads/` (executed). It found 196 coordinates of a `.py`, `.md`, `.sh`, `.json`, `.toml` or `.yml` file written without a directory. 13 name no tracked file. Eleven of those are fixtures inside test modules or case ids in `.test_durations`. Two are `skills/verify/scripts/seal_stamp.py:452` and `:598`, which cite "the owner's `frames.py`", a file the tree never held. None names a name its file does not define. The definition test is lenient for Markdown, and a coordinate of another extension is not read, so this half is a sample.
- **Row 19, figures in two records outside what the fix pass compared.** `test_tmp_figures.py` compared every figure, in code spans and fences included and number words to twenty included (executed). Finding 2 holds the defects it found. The other values that stand in two records hold. 65,536 is GitHub's limit, given in design S5 and cited by plan row 2. "0.24.0's 12 of 17" quotes `docs/the-record-layout.md`, with its release, in `frame/design.md:88` and `trail/phases/phase-2.md:26`. "Seven sentences" is one finding's heading, quoted under K2 and K11 because that finding counts in both kinds. Every other value names a different fact in each record. A figure written in other words, such as "a dozen", is not listed, and that part of the class has no bound.

Each of the three rows can be marked `closed`, citing round 1's confirmation and this one.

```seal
confirms: none
```
What matched: S6. `git diff --name-only bf9efcba..HEAD` prints eight paths, each under `seal/threads/1793490088-each-kind-of-restatement-is-measured/` (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The prose of the edition pairs' sections other than those round 1 read. Round 1 gave this to the owner, and `gaps.md:8` still names the proofer of this work item. Two rounds have now left it unread, so the row's answerer is the orchestrator's to decide. | `seal/threads/1793490088-each-kind-of-restatement-is-measured/gaps.md:8` | the orchestrator, who names its answerer; #1102 rewrites both README editions in `release: 0.29.0` |
| Whether the code behind the comments #706 and #710 name is what those issues say. Their sentences stand at `bf9efcba`; the code was not re-derived. | `skills/verify/scripts/mutation_check.py:574`, `skills/verify/scripts/arm_check.py:958` | the fix pass, as it writes finding 3's overlaps |
| The full suite, the repository-wide lint and the format check. Phase 2 hands the suite over as `unverified` and names the orchestrator, which is an honest label. This round leaves findings open, so the broad run is not due yet. | `seal/config.md` *Broad gate* | the orchestrator, by `seal gate` once the rounds settle, then the sealer's spawn |

## Probes

| Command | Result |
|---|---|
| `git clone -q --no-local <worktree> <scratch>/round-2/clone`, checked out at `d0e51dce` | the clone, 67 tags; `origin` later set to the GitHub remote for the `gh` loops |
| `python3 -I <scratch>/round-2/test_tmp_extract.py <clone> <scratch>/round-2/blocks`: writes each `#### Command <X>` sh block of both phase records to a file, with phase 1's `mktemp` line replaced by the round's scratch directory | 36 blocks |
| the setup blocks of both records, then phase 1's *Command durations*, *Command baseline* and *Command K9*, and phase 2's *Command nones*, *Command durations* and *Command comment*, each with `sh` from the clone | every figure the record states; the comment at 24622 bytes and 24620 characters, exit 0 |
| a `grep -qxF` of each joined comment row over the two records | 15 lines (the header and 14 rows), no miss |
| the first loop of both *Command tracker* blocks | 152 and 231 lines on stdout, no error; read in finding 3 and under *Confirmations* |
| `gh issue list --milestone "<title>" --state all` for 0.27.1, 0.27.2 and 0.28.0; `gh api` milestones 3, 70, 76, 77 and 78; `gh issue view` 146, 317, 506, 706, 710, 1204, 1215, 1216, 1222 and 1225 | 8, 9 and 9 open issues; the descriptions and bodies the findings and confirmations quote |
| the two `git grep -l` searches of `trail/phases/phase-1.md:677` at `bf9efcba`, less the record's 18 run modules | 14 and 16 files, 28 in the union; 11 left, the ten the record names and `tests/conftest.py` |
| `python3 -I <scratch>/round-2/test_tmp_figures.py <records>`: every figure in the five records, keyed by value and next word, printed where it stands in two of them | 87 keys, read; the two defects in finding 2 |
| `python3 -I <scratch>/round-2/test_tmp_bare_names.py <scratch copy of bf9efcba>` | `bare path#name 196; no file 13; not defined 0`, each of the 13 read |

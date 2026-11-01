# Review round 3: 1793490088-each-kind-of-restatement-is-measured

```seal
target: be61bfac, fixes d0e51dce..be61bfac
```

The round reads every commit after round 2's target: `e3ec7f3d`, the round 2 record with the orchestrator's fold of finding 2; `a15b9e96`, the fix pass over round 2; `bcfb181f`, the framer's reframe; `bb5d658b` and `43c4cb1d`, the close blocks and a plan row; `7358c7a3` and `8d674e4c`, phase 3; and `be61bfac`, the orchestrator's fold of phase 3's two frame findings. The base is `origin/release/v0.27.1` at `bf9efcba`.

What the reframe means for this round. `docs/the-review-record.md` *The run* calls a reframe a design change, and the first finding round that reviews new work after one starts the count of finding rounds again at one. So this round does two jobs. It is the verifying round for round 2's three closes, and it is the first finding round over the reframe, phase 3 and the fold. Phase 3 is a build phase the reframe planned (`frame/plan.md`, row 3 of *Phases*), so a defect in a unit it made is new work and takes no `regression:` line. The fold `be61bfac` answers no round finding, so it is new work as well.

Carried from round 2, and not run again: the regeneration of the proofer cases (round 1 finding 6), the bare-name probe, and the milestone counts behind D1 to D7. Round 2's readings of the drifted instances of K1 to K14 are carried too, except the six K13 coordinates the fix pass added, which this round opened. Re-derived this round: every verdict below, S7 over all 78 pairs, and the command blocks *Probes* names.

## Findings

### 1. The issue's *Order* line against the milestone's order is answered twice, as the framer's in *The kinds* and as D8's in the section after it

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:107`
evidence: read `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:107`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:133`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:16`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:112`
```

Why it matters: design G4 and S7 give each pair one answer, and the orchestrator asked whether any pair is answered in two contradicting places. D8's answerer reads the section and the paragraph before it to learn which pairs are its own. Here one instance is given to two answerers.

The grounds:

- The fourth bullet of *The kinds*' paragraph says the framer answers "an open issue's body or a milestone's description against the tree", for "The same pairs as the bullet above". The pairs in that bullet are P11 with P1 to P6, P8 to P10 and P12. P11 with P11 is not among them. The bullet then says "This audit's own spawn is an instance: the issue's *Order* line against the milestone's order (G10)" (`frame/design.md:107`).
- The issue's *Order* line and the milestone's order both stand in the tracker, so the instance is P11 with P11. *Pairs no command of this audit reads* names the same instance as the known instance of P11 with P11, and that section's opening gives each of its pairs to D8 (`frame/design.md:112`, `:133`).
- G10 records the instance as "the orchestrator's finding, read against the milestone" (`frame/design.md:16`), not the framer's. So the instance does not show what the bullet says it shows: a framer who takes the issue and catches the line.

The fix takes the instance out of the bullet. The section's row keeps it, and D8's milestone paragraph already counts it as a drift in D8's pairs.

```diff
-... The same pairs as the bullet above. An open body is a request that ranks below the tree's documents, and the framer of the work item that takes it opens what it cites (`skills/implement/SKILL.md` *1. Read the documents that outrank the code first*, "Verify clause numbers a ticket cites"). This audit's own spawn is an instance: the issue's *Order* line against the milestone's order (G10).
+... The same pairs as the bullet above. An open body is a request that ranks below the tree's documents, and the framer of the work item that takes it opens what it cites (`skills/implement/SKILL.md` *1. Read the documents that outrank the code first*, "Verify clause numbers a ticket cites").
```

### 2. K13 reads no list in code text, phase 3 says the unread rest of K13's pairs stands in the section D8 carries, and no record gives those lists an answerer

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:135`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:29`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:923`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-3.md:12`
evidence: read `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:426`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:448`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:29`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:917`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:923`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-3.md:12`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:93`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:110-135`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:992`
```

Why it matters: G4's third answer is a pair "named ... with who answers it". The comment's preamble, which #1038 and the owner read, says every pair no command read is named in the design's section and that D8 carries those pairs. One part of a pair is in neither place, and nobody answers it.

The grounds:

- Design K13 places P12 with P8 whole, and says its commands list "each figure about the tree stated without its moment" and "each list of an enumerable source" (`frame/design.md:93`).
- *Command lists* and *Command figures* read `.md` files only: `audit2.py#lists` and `#figures` each filter the corpus to `.md` (`trail/phases/phase-2.md:426`, `:448`). Phase 3 wrote the narrowing into the K13 row: "In code text they read the coordinates, and no list or figure" (`trail/phases/phase-2.md:29`).
- Phase 3 says "For K12 and K13 the rest stands in *Pairs no command of this audit reads*" (`trail/phases/phase-3.md:12`). For K13 that holds for tests and eval cases. It does not hold for code text: the section has no row for P12 with P8 (`frame/design.md:110-135`).
- Figures in code text have an answerer. K13's decision leaves "the figure class" to `seal/follow-up.md`'s figure row, which names the owner. Lists in code text have none. K13's decision "nothing for the lists" rests on the 33 `.md` blocks *Instances K13* read (`trail/phases/phase-2.md:917`). The row's open part names "a figure in code text" and no list in code text (`:923`). So a docstring, comment or printed message that lists the hooks, agents, skills or `seal` subcommands is read by no command, named in no open part, and carried by no draft.
- The shape is in the record: #506's first item is a docstring's enumeration that a review round found out of step. That one stands in a test, but nothing in the shape keeps it out of code text.

The fix adds the pair to the section, so D8 carries it, and narrows K13's decision and open part to what was read.

```markdown
frame/design.md, *Pairs no command of this audit reads*, a row after P12 with P10:
| P12 with P8, for a list | a docstring, comment or printed message listing the members of an enumerable source | K13 reads P8's coordinates only, since *Command lists* reads `.md` files (`trail/phases/phase-2.md` *The table*, row K13); a figure in code text stays with `seal/follow-up.md`'s figure row, as K13's decision says |

trail/phases/phase-2.md *The table*, row K13, *Decision* cell, the clause on lists:
nothing for the lists in shipped `.md`

trail/phases/phase-2.md *Instances K13*, the open part:
The open part: a coordinate whose path has no directory, one in `tests/` or `evals/behaviour/`, a figure or a list in code text, a figure the keyword list does not spell, and a docstring, comment or printed line out of step with the code of its own file that no open issue holds.
```

### 3. *The parts* now says the parts are not the whole tree, and G4 and plan row A8 still say the parts make the list of kinds whole

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:10`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/plan.md:39`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:992`
evidence: read `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:10`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:60`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/plan.md:39`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/plan.md:68`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-3.md:14`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:974`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:992`
```

Why it matters: the orchestrator asked whether any record still claims coverage the audit does not have. G4 is the sentence a reader applying contract rule 12 opens, such as #1038 or a later audit, to learn why the list of kinds is whole. The fold corrected the section under the fact and left the two sentences that stand on the old fact (contract rule 19).

The grounds:

- G4: "the list of kinds is built by a method that makes it whole: the tree is taken apart into its parts (*Data & interfaces*, *The parts*)", and "The list is whole because every pair is answered" (`frame/design.md:10`).
- Plan row A8's verdict: "the parts make the list whole (design G4)" (`frame/plan.md:39`).
- *The parts*, as `be61bfac` writes it: "The parts are not the whole tree: the tracked files no part holds are listed by `trail/phases/phase-3.md` *Command parts*, and D8 carries them with the unmeasured pairs" (`frame/design.md:60`). *Command parts*, run again, prints the eleven files phase 3 names (executed; *Probes*).
- Phase 3 put the finding this way: "The frame claims its list of pairs whole because the parts are whole (design G4), so this is a *no*" (`trail/phases/phase-3.md:14`). The judgments row for the fold says naming makes the claim true (`frame/plan.md:68`). Naming makes *The parts* true. It leaves G4 and A8 as they were.
- The preamble that #1147's readers get says "D8 carries those pairs", meaning the unread pairs. It does not name the files in no part, which D8 also carries (`trail/phases/phase-2.md:974`, `:992`).

The fix narrows each claim to what the parts hold. The preamble changes the comment, so *Command comment* has to run again after it.

```markdown
frame/design.md G4, from its second sentence:
Each kind is a class, so the list of kinds is built by a method that makes it whole over what the parts hold: the tree is taken apart into its parts (*Data & interfaces*, *The parts*), the tracked files no part holds are listed by `trail/phases/phase-3.md` *Command parts* and carried by D8, and every pair of parts gets one of three answers in *The kinds* and the section after it: ... The list is whole over the parts because every pair is answered, not because every pair is measured. ...

frame/plan.md A8, its verdict:
chosen: the issue enumerates by pair, and the parts make the list whole over the files they hold (design G4)

trail/phases/phase-2.md *Preamble*, the end of its fourth sentence:
...; D8 carries those pairs and the tracked files no part of that design's *The parts* holds.
```

### 4. D8 tells its answerer to measure each pair with "the kind that section names nearest it", and the section names a kind for 7 of its 20 pairs

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:974`
evidence: read `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:974`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:112`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:114-135`
```

Why it matters: D8's *Scope* is the method its answerer follows, and its *Done when* asks for each pair "measured, with its command". For most pairs the method points at a kind that is not there.

The grounds:

- D8's *Scope*: "A pair is measured by the command of the kind that section names nearest it, widened to the pair" (`trail/phases/phase-2.md:974`).
- The section's third column names a kind, or a kind's reader or mechanism, for 7 pairs: P1 with P10 (K5), P4 with P9 (K6), P5 with P6 (K3), P5 with P9 (K3's mechanism), P8 with P10 (K12), and P12 with P9 and P12 with P10 (K13). For 11 pairs it says "none": P3 with P6, P4 with P4, P4 with P8, P4 with P10, P5 with P8, P5 with P10, P6 with P6, P6 with P8, P6 with P9, P6 with P10, and P9 with P10. For P8 with P9 and P11 with P11 it names an instance and no kind (read, each row of `frame/design.md:114-135`).
- The design's own sentence says only "the command of the kind nearest it" (`frame/design.md:112`). It does not claim the section names that kind. D8 claims it does.

The fix says what each kind of row is measured by.

```markdown
> **Scope.** Each pair that section names, read at the work item's base. A pair whose row names a kind, or a kind's reader, is measured by that kind's command widened to the pair. Any other pair is measured by a reader chosen for the fact the row's second column names: a passage reader for shared prose, and a coordinate, list or figure reader for the tree's state. Each command is written whole in the work item's records, as #1147's commands are; a pair no command can list whole is read by a stated sample, and the record calls it one. ...
```

### 5. Phase 3 places #379 on K5's ground, and K5's overlaps leave it out, though round 2 finding 3's close read #379 and said every kind named every issue its loops return

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md:561`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:829`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-3.md:30`
evidence: executed `sh <scratch>/round-3/phase-2-tracker-loop1.sh`, `sh <scratch>/round-3/blocks/phase-3-tracker.sh`, `gh issue view 379`, `git grep -n -A12 'def test_every_spec_directory_that_reached_the_ladder_has_an_overview' bf9efcba -- tests/behaviour/test_chain_hooks_hardening.py`, `git grep -n -i 'gaps.md\|overview' bf9efcba -- agents/framer.md`
reopens: round-2#3
```

Why it matters: the owner's direction says "the tracker is searched first, and a decision an open issue covers names that issue". Both tracker paragraphs say "Each kind's overlaps are named under its *Instances*". The work item's records now disagree on whether #379 is on a kind's ground.

Why the close does not hold: the close says the class was listed by "reading each of the 62 open issues they return against the ground of every kind", and that "K1 and K3 to K10 already named every one". Phase 2's first loop returns #379, open (executed). Phase 3 reads #379 as "an instance in a pair a kind already reads: #379 (K5)" (`trail/phases/phase-3.md:30`). Phase 1 *Instances K5*'s overlaps name #1197 and #1216 only (`trail/phases/phase-1.md:561`). Phase 2's list of the issues its loop returns "on a kind's ground" leaves #379 out (`trail/phases/phase-2.md:829`). So an issue inside the set the close read is on K5's ground by the work item's own reading, and K5 does not name it.

Which reading holds. I read #379 as K5's. Its case, `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`, holds that a directory with a `frame/design.md` or `frame/plan.md` owes its memo (its docstring at `bf9efcba`, executed). `agents/framer.md:120` tells the framer not to write `gaps.md` (executed). So a test (P9) and a definition (P3) state differently what a framed directory holds. This work item met the case red at its own framing (`trail/phases/phase-1.md:677`, "exit 1"). Design K5 places P9 with P3, and plan row A8 sorts kinds by pair. The case pins no wording, so K5's count, drifted count and decision stand. Only its overlaps are short.

The fix names #379 where each tracker paragraph says overlaps stand.

```markdown
trail/phases/phase-1.md *Instances K5*, the end of the open part:
... D4 takes the other modules and names both. #379 (`backlog: review chain & agents`): `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview` holds a memo in every framed directory, where `agents/framer.md` gives the memo to the builder, so the case is red from each framing commit until a phase writes `gaps.md`; it pins no wording, so D4 does not take it, and the repair is #379's.

trail/phases/phase-2.md *Command tracker*, the list of the first loop's returns on a kind's ground:
... #1215, #1216 and #1228, with #379, which `trail/phases/phase-1.md` *Instances K5* names, and its second loop views #1229. ...
```

### 6. Phase 3 and D8 restate three facts whose home is another record: the 28 modules, the milestone's open count, and phase 2's reading of #238's line

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-3.md:68`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-3.md:32`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:982`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-3.md:15`
evidence: executed `python3 -I <scratch>/round-3/test_tmp_figures.py <scratch>/round-3/clone seal/threads/1793490088-each-kind-of-restatement-is-measured`, `grep -n -i 'open=0\|no open issue' -r <records>`
```

Why it matters: the owner's direction in `frame/plan.md` *Judgments of the run* says "a count, command or decision stands once" and that every other place cites it. Round 1 finding 5 and round 2 finding 2 were this class. Phase 3 is the first build after both, and it adds three more. None has drifted, so the cost is the rule the audit measures, applied to its own records.

The grounds:

- `trail/phases/phase-3.md:68` says "the 28 modules `trail/phases/phase-2.md` *Phase-boundary run* names". The count is phase 2's (`trail/phases/phase-2.md:1021`), cited and restated. Phase 3's own run result, "1641 passed", is that run's own fact, and it stands.
- Milestone 4's open count stands at its home, *Command tracker*'s paragraph, as "`backlog: docs drift open=0 closed=9`" (`trail/phases/phase-3.md:62`). It is restated at `:32`, "The milestone has no open issue on 2026-11-01", and in D8's *Proposed milestone*, "on 2026-11-01 it holds no open issue (executed: `gh api repos/:owner/:repo/milestones/4`)" (`trail/phases/phase-2.md:982`). That paragraph is not part of the body the orchestrator files, so it can cite.
- `trail/phases/phase-3.md:15` restates phase 2's reading of #238's line, "names one property where #238 measured two", which stands in `trail/phases/phase-2.md` *Instances K13*.
- Method. The probe keyed every figure, in digits or a number word to twenty, outside fenced blocks, by its value and the next word, across `routing.md`, the three frame files, `gaps.md` and the three phase records. It printed each key that stands in two files and has a line the diff `d0e51dce..HEAD` added: 42 keys, each read. The two figures above are the ones among them that restate a fact; every other key names a different fact in each file. The milestone's count is written in words, so it was found by a search on two spellings. A figure written in other words has no bounded spelling, so that half is a sample.

The fix cites each home.

```markdown
trail/phases/phase-3.md:68:
... and the modules `trail/phases/phase-2.md` *Phase-boundary run* names, the two searches ...

trail/phases/phase-3.md:32, its third sentence:
The milestone's open and closed counts are *Command tracker*'s last two lines.

trail/phases/phase-2.md:982, the clause on the milestone's state:
... and it held #755, the survey of verbatim restatements across rule documents; its counts on 2026-11-01 are `trail/phases/phase-3.md` *Command tracker*'s. ...

trail/phases/phase-3.md:15:
... `trail/phases/phase-2.md` *Instances K13* reads #238's line `tests/hooks/test_version_check.py:107` against #238's measure; ...
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: `gaps.md` *Not done* no longer holds the paragraph on G12. The paragraph before it now says D7 carries the stream answers and the drifts row K13 repairs, and that each other drift stays with the open issue that holds it (`gaps.md:27`). That matches K13's *Decision* cell, "the three drifts repaired; ... the six an open issue holds stay that issue's" (`trail/phases/phase-2.md:29`) (read).

```seal
confirms: round-2#2
```
What holds: plan row A4 cites design G13 for the files its probe read, with no figure (`frame/plan.md:32`). Design K12's last cell cites `seal/follow-up.md`'s `console.to_utf8()` row "measured at `11f3cde8`" and phase 2's row K12, with no figure (`frame/design.md:92`) (read). The four framer locations the close left for a fold were folded at `bcfb181f`, and the word diff shows each (executed: `git diff --word-diff=plain d0e51dce..HEAD`). A1's alternative now reads K4's editions "section by section in both languages". Phase 2's *Verified by* cites "design S5". G7 cites *Command K8*'s second line for 0.27.1's fragments, and the three fragments stand at `bf9efcba` (executed: `git ls-tree -r --name-only bf9efcba seal/threads`). K10's cell cites the policy section for the 0.24.0 figure. The figure probe run again found none of the six close locations restating a figure; what it found is finding 6, all in phase 3's new work.

```seal
confirms: none
```
What matched: S7's first clause over all 78 pairs, with the two exceptions findings 1 and 2 name (read). The list was made by pairing each part P1 to P12 with itself and with each part after it, which is rule 12's method of taking the artefact apart. Each pair was found in the *Pairs of parts* column of *The kinds*, in a bullet of the paragraph after it, or in a row of *Pairs no command of this audit reads*. Per part, counting the pairs it opens: P1 12, P2 11, P3 10, P4 9, P5 8, P6 7, P7 6, P8 5, P9 4, P10 3, P11 2 and P12 1. No pair is missing. K3's command reads P5 with P5 and P6 with P1 and P2, as the first bullet says: `audit.py`'s `KINDS["K3"]` lists those pairs and not P5 with P6, so the section's "no command reads the pair's passages" holds for P5 with P6 (`trail/phases/phase-1.md` *Command setup*, read). The P11 bullets split the tracker into dated entries and open bodies, and the two answers do not contradict each other except for the one instance finding 1 names. S7's second clause holds for K4, K7, K8, K9, K10 and K12, and K13 names its code-text narrowing in its row. Finding 2 is that the narrowing has no answerer.

```seal
confirms: none
```
What matched: phase 3's *Command parts* and the comment, run again from a clone at `be61bfac` (executed). *Command parts* prints the eleven files phase 3 lists, exit 0. `skills/` holds no file outside `.md` and `scripts/` at `bf9efcba`, `templates/` holds one, `templates/setup/hygiene.yml`, and every `scripts/` directory sits one level under `skills/`. The last filter drops only `.claude-plugin/icon.png` and the files under `assets/seals/`. *Command comment* prints `join exit 0`, 26675 bytes and 26673 characters, which is what `trail/phases/phase-3.md:70` states. Its 16 table lines (the header, the separator and 14 rows) each stand as a whole line in the two records, with no miss (executed: `grep -qxF`). The `be61bfac` fold changed no table and no preamble, so the figure is current at HEAD.

```seal
confirms: none
```
What matched: a sample of the other blocks, run in order from fresh scratch copies of `bf9efcba` (executed). Phase 1's and phase 2's *Command setup* exit 0. Phase 1's *Command K3* prints `K3: 2 passages over 422 file pairs`. Phase 2's *Command lists* ends `blocks naming three or more and half of a source 33`, its *Command figures* `figure candidates with no moment on their line 33`, and its *Command coordinates* `path:line coordinates 9; path#name coordinates 113; printed for reading 3`. Each is the figure its record states.

```seal
confirms: none
```
What matched: D8's overlaps and milestone, apart from findings 4 and 6 (executed). Phase 3's *Command tracker* ran on 2026-11-01 with exit 0 and no stderr. #238, #390 and #506 are open, #238 and #506 in `backlog: review chain & agents` and #390 in `backlog: gates & hooks` (executed: `gh issue view`). #238 measures the pin of `hooks/version-check.py#notice` and the record that undercounts it. #506's first item is `tests/test_every_orchestrator_act_names_its_delivery.py`'s docstring enumeration, a test. #390's third item is `command_name`'s docstring counting eleven pairs. `git show bf9efcba:tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py | grep -c eleven` prints 0, and the log's first line is `8350c578`. So D8 takes none of the three and states each one rightly. None of the first loop's other returns carries a whole pair D8 names (read by title, and by body where the title did not settle it). Milestone 4 is open, with 0 open and 9 closed, #755 among the closed. The milestone fits by `docs/issues-and-milestones.md` *A milestone answers when, and takes three shapes*: `backlog:` holds "work with no release yet", and D8 states why nothing needs it first. Its area, "Documents, skills, templates and agent files that claim behaviour the code does not have", covers the pairs with P1 to P6 and not the pairs of tests, eval cases and the tracker. D8 rests its choice on #755's precedent, and the closer fit, `backlog: review chain & agents`, is weighed and refused with a reason. The title takes `chore:` as #1147's does, for a work item that changes records only, which *An issue is titled like a commit* allows.

```seal
confirms: none
```
What matched: the six drifts the fix pass over round 2 added to *Instances K13*, opened at `bf9efcba` (executed: `git show bf9efcba:<path>`). `.github/scripts/roll_flow_measurement_issue.py:76-78` says a lag "can only ever produce a reading that is short a result", and `:450-453` says a lag behind a close "is a reading with an extra issue in it". `evals/scripts/replay_targets.py:52-53` and `evals/scripts/seed_defects.py:51` say "A name given twice is one name", and each `say_unanswered` walks the names as given (`replay_targets.py:963-964`, `seed_defects.py:394-395`). `skills/verify/scripts/arm_check.py:1146-1147` prints "the reason beside each says whether it was ever mutated". `arm_check.py:953-958` says a put-back failure propagates "as the loop's own first write would fail on it". `skills/verify/scripts/mutation_check.py:570-575` says "An interrupt during the baseline wrote nothing". Each sentence is the one *Instances K13* quotes. This answers round 2's *Not judged* row on #706 and #710 for the sentences. The code behind #315 and #710 was not re-derived past the lines the record cites.

```seal
confirms: none
```
What matched: S6. `git diff --name-only bf9efcba..HEAD` prints ten paths, each under `seal/threads/1793490088-each-kind-of-restatement-is-measured/` (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check. Phase 3 hands them over as `unverified` and names the orchestrator, which is an honest label. This round leaves findings open, so the broad run is not due yet. | `seal/config.md` *Broad gate* | the orchestrator, by `seal gate` once the rounds settle, then the sealer's spawn |
| Whether findings 1, 3 and 4, which change `frame/design.md` and `frame/plan.md`, go to an orchestrator's fold or back to the framer. Finding 2 changes the design's section and phase 2's row K13. | `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/plan.md` *Judgments of the run* | the orchestrator, by `docs/the-review-record.md` *The run* |

## Probes

| Command | Result |
|---|---|
| `git clone -q --no-local <worktree> <scratch>/round-3/clone`, checked out at `be61bfac`, `origin` set to the GitHub remote | the clone, 67 tags |
| `python3 -I <scratch>/round-3/test_tmp_extract.py <records> <scratch>/round-3/blocks <scratch>/round-3`: writes each `#### Command <X>` sh block of the three phase records to a file, with the `mktemp` line replaced by the round's scratch directory | 38 blocks |
| phase 3's *Command parts*; the same pipeline with the last filter inverted; `git ls-tree` of `skills` and `templates` for files outside `.md` and `scripts/` | the eleven files; `.claude-plugin/icon.png` and `assets/seals/` alone dropped by the last filter; `templates/setup/hygiene.yml` alone |
| phase 3's *Command tracker*, whole | exit 0, 67 lines, no stderr; `grep -c` prints 0; `8350c578`; `backlog: docs drift open=0 closed=9` |
| the first loops of phase 1's and phase 2's *Command tracker* | 231 and 152 lines; #379, #238, #390 and #506 in phase 2's, #390 in phase 1's |
| both *Command setup* blocks, then phase 1's *Command K3* and phase 2's *Command lists*, *Command figures*, *Command coordinates* and *Command comment*, each with `sh` from the clone | exit 0 each; the figures under *Confirmations* |
| a `grep -qxF` of each table line of the joined comment over the two records | 16 lines, no miss |
| `python3 -I <scratch>/round-3/test_tmp_figures.py <clone> <item>` | 460 keys; 42 standing in two files with a line the diff added, each read; finding 6 |
| `gh issue view` 238, 379, 390 and 506; `gh api` milestone 4 and the milestone list | the bodies and states the findings and confirmations quote |
| `git show bf9efcba:<path>` over the six K13 coordinates; `git grep` over `agents/framer.md` and the ladder case at `bf9efcba` | the sentences quoted under *Confirmations* and finding 5 |
| `git diff --name-only bf9efcba..HEAD` | ten paths, all under the work item |

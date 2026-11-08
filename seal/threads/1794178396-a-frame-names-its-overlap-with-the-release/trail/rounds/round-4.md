# Review round 4: 1794178396-a-frame-names-its-overlap-with-the-release

```seal
target: da67a09d, fixes dde649d4..da67a09d
```

This is the verifying round over the fix for the regression the broad gate found after round 3. The fix diff is three commits: `8aa5cbb4` rewrites the placeholder of `templates/records/sdd-plan.md` *Overlap with the release*, `09257cf4` amends the first row of `gaps.md` *Not verified*, and `da67a09d` folds the same placeholder into `frame/design.md` *Data & interfaces* and adds a row to `frame/plan.md` *Judgments of the run* (executed: `git show --stat` over the three). `dde649d4` commits round 3's record. The base is `release/v0.36.0` at `94d04d30`. The round was worked in a `git clone --no-local` of the branch worktree at `da67a09d`. `seal/parity.md` is absent, and `seal/config.md` has no `Pact` row and no `Record language` row, so no parity comparison applies and the record is English (executed: `grep` over `seal/config.md`).

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/rounds/round-1.md` to `round-3.md` whole at `da67a09d`. The issue has no comments, as the spawn prompt states; this round did not re-run `gh issue view 1443`. `trail/gate.md` does not exist at the target, as the spawn prompt states (executed: `ls trail`).

Carried from earlier rounds and not re-established: the `94d04d30` coordinates of `frame/design.md` *Grounding* and `frame/plan.md` *Technical context*, which round 1 opened at that commit and which no commit since has changed; phase 1's seen-red result for `test_the_plan_template_carries_the_overlap_table`, whose case file no commit since round 1's target touches; and the sibling plans' disagreement with this plan's overlap rows, which round 3 read on 2026-11-09 and which stays a row of *Not judged* below. Re-opened this round: `agents/framer.md:54-92`, the step the new placeholder cites, and `templates/records/sdd-plan.md:21-27`.

**The template still serves a reader who starts from it alone.** The placeholder (`templates/records/sdd-plan.md:23`) no longer states when two items meet. It names where that is stated: "When two items meet is defined once, in `agents/framer.md` *Order of work* step 4." Step 4 holds the definition at `agents/framer.md:84-87`, the G9 kind of a check and the content it reads included (read). The two readers of the template reach it as follows. A framer's own definition is `agents/framer.md`, so its context already holds the sentence the placeholder cites. A session that draws the frame itself, where `Planning` is `the session` (`skills/implement/orchestration.md:313-318`), is sent by path and section to the one statement. The path is the plugin's, as the citations of `agents/sealer.md` step 5 in `templates/records/sdd-guarantee.md:17-18` are. `tests/behaviour/test_a_cited_section_stands_in_its_file.py` reads the citation, since `agents` is a top-level entry of the tree, and it passed (executed, under *Probes*). The heading exists; that step 4 holds the definition was read, not checked by the module. What a row holds still stands in the placeholder: the file and section both change, or the rule or check and what of the other's change it reads; the item that merges first; and why that order costs less. So `frame/design.md:69` ("The meaning of each column stands in the placeholder") still holds; the definition of a meeting is no column. The claim "defined once" holds for the files the paste guard reads: "adds content to" stands only at `agents/framer.md:86` there, and otherwise only in this work item's records (executed: `git grep -n`).

**Round 1's finding 2 stays answered, by a different text than its paste-ready fix.** Its defect was that a reader of the template held a second, narrower definition of a meeting than `agents/framer.md` step 4 (`trail/rounds/round-1.md`, finding 2). Round 1's fix pass answered it by copying the full definition into the placeholder (`6f9669aa`), and round 2 confirmed that. The copy was a regression in the unit that fix pass changed. The frame asked for it: *Data & interfaces*, as the orchestrator folded it at `dfc639f2`, carried round 1's paste-ready line. With the copy in place, the paste guard fails, as the broad gate reported. Restoring the template of `dde649d4` in the clone failed `tests/text/test_no_passage_is_pasted_into_a_second_file.py` at line 151. The case named `agents/framer.md` and `templates/records/sdd-plan.md` as sharing three runs of 15 words, the longest of 17 words (executed, under *Probes*). At `da67a09d` the template holds no second definition, narrower or whole, so the reader round 1 worried about can no longer take a narrower one. The guard passes. No regression finding stands, because the defect is already fixed in this fix diff. Round 3 closed no finding, so this round owes no `confirms:` line, and round 2 already confirmed round 1's finding 2.

**The spawn prompt's run.** The prompt asked for `tests/text/` and `tests/behaviour/` to be run with the narrow command's module set. This round read that as a named module set: two of the suite's eight test directories, with no lint and no typecheck. That is not the broad gate contract rule 2 keeps from a round, so it ran them (executed, under *Probes*: 1796 passed, 9 skipped, exit 0). The full suite, the lint and the format check stay the orchestrator's.

`frame/plan.md:62`, the new *Judgments of the run* row, says "No round's narrow run included `tests/text/`". Rounds 1 to 3 each ran one module under that directory, `tests/text/test_the_rules_have_one_owner.py` (their *Probes*), so the sentence is true of the directory as a whole and not of every module under it. Read with the clause after it, "which is #1441's subject", it means the directory whole: #1441 weighs running the 35 modules under `tests/text/` in every narrow run (executed: `gh issue view 1441`). The module that caught the copy reads every template, so it is a module that reads a path round 1's fix pass changed. This round reads that as #1441's subject, and opens no finding on the sentence.

## Findings

None. The fix diff holds no defect, and no sentence of the records that state the present is contradicted at `da67a09d`.

## Confirmations

What matched: `frame/design.md:62` is identical to `templates/records/sdd-plan.md:23` (executed: `diff` of the two lines exited 0), so *Data & interfaces* shows the placeholder as the template carries it, as *Scope* item 1 says.

What matched: the `frame/plan.md:62` row describes the fix diff. `8aa5cbb4` replaced the copy with the citation, and `da67a09d` folded the same line into *Data & interfaces* (executed: `git show`). Its grounds say the guard asks a passage to link to its home. The guard's message ends "Link to the home instead of copying it, per `docs/layout/the-record-layout.md`" (`tests/text/test_no_passage_is_pasted_into_a_second_file.py:68-70` and `:126`, read, and in the probe's output). Its claim that the template copied the definition "as round 1's finding 2 asked" matches round 1's paste-ready line (read).

What matched: `09257cf4` amends the first row of `gaps.md` *Not verified* in place, and no row left the memo. The row says the regression's fix pass ran the plan row's three modules, `tests/behaviour/test_docs_line_wrap.py` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py`. All five are inside this round's run, which passed (executed, under *Probes*). The row also says no pass changed a Python file. `8aa5cbb4`, `09257cf4` and `da67a09d` change `templates/records/sdd-plan.md`, `gaps.md`, `frame/design.md` and `frame/plan.md` only (executed: `git show --stat`). The row keeps the full suite, the lint and the format check `unverified`, with the orchestrator at the broad gate as their answerer, so the label is honest.

What matched: each of the six quotes in `pr.md` stands at the file its coordinate names, word for word with runs of whitespace collapsed (executed: a read-only Python comparison printed True for each). The second quote, the meet definition in `changelog.md:3`, is a record and outside the files the paste guard reads, so the fix left it as it stood.

What matched: every commit from `ffe97115` to `da67a09d` carries `Seal-Routing: 1794178396-a-frame-names-its-overlap-with-the-release` (executed: `git log` over the trailer).

What matched: the fix diff adds no test, so no new case is read against its group. `frame/design.md` *Rule changes* still holds the no-change block. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether this plan's overlap rows match the siblings' frames. Round 3 found that #1440's and #1444's plans each say they do not meet this work, against this plan's rows. The rows are labelled `unverified` and dated to before those frames stood (G16), and this round did not re-read the siblings. | `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/plan.md:36-44` | the orchestrator, reading the six plans, as `frame/design.md` G16 names |
| The full suite, the repository-wide lint and the format check at `da67a09d`; contract rule 2 keeps them out of a round | `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/gaps.md:7` | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text tests/behaviour -q -p no:randomly`, in the clone at `da67a09d` | exit 0, 1796 passed, 9 skipped |
| `git checkout dde649d4 -- templates/records/sdd-plan.md`, then `bin/test tests/text/test_no_passage_is_pasted_into_a_second_file.py -q -p no:xdist`, then `git checkout HEAD -- templates/records/sdd-plan.md`, in the clone | exit 1, 1 failed and 4 passed; an `AssertionError` at line 151 naming `agents/framer.md` and `templates/records/sdd-plan.md` as sharing 3 runs of 15 words, the longest 17 words: "one changes a rule, a check or a fact that the other's change reads or adds content"; the clone was clean afterwards |
| `git grep -n -e 'adds content to' -e 'items meet' -e 'defined once'`, in the clone at `da67a09d` | among the files the paste guard reads, the meet definition stands only at `agents/framer.md:84-86`; the other hits are this work item's records and two unrelated "defined once" sentences |
| A read-only `python3` comparison in the clone at `da67a09d`: each `pr.md` quote against its source with whitespace collapsed | printed True for all six |
| `git log --format='%h %(trailers:key=Seal-Routing,valueonly)' ffe97115..da67a09d`, in the clone | four commits, each carrying the full work item id |

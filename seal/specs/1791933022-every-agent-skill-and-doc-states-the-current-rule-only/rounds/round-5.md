# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — review round 5

| Field | Value |
|---|---|
| Target SHA | 66d0180b, fixes b065c7a5..66d0180b |

Extended past round 4: round 4 found 2, round 3 found 2, and the frame took round 4's fix of a fix.

A verifying round over the reframe after round 4 (76d7df7d), its approval
(dcf32452) and phase 5b (1011463b, 704395b1, 66d0180b), part A only. Both of
round 4's findings are closed in the units they named. Two new 🟡 rows
follow, and both are marked `fix of a fix`, because each sits in a unit these
commits wrote.

- 🟡 1 is in the one list phase 5b made. Step 3 and the template's comment,
  the two places this phase pointed at each other, now give two different
  shapes for the `Result` cell of the row step 3 adds. The frame states both
  shapes, so the build copied the disagreement rather than making it.
- 🟡 2 is in the frame's new rule on figures. S21 and the reframe's sentence
  "the frame's own three documents were rewritten to it at the reframe" are
  not true at the target. Phase 5b's divergence 3 lists the counts that break
  it. The reader the rule names, the sealer's step 4, does not read two of
  the five documents.

The changelog fragment is judged in a 🟢 row: what it still tells a user is
true, and no figure in it can go stale. Findings from reading and from
execution are labelled in each Grounds cell, and every command named there
is in `## Probes`. The full suite was not run: it is `unverified`,
and the sealer answers it.

## Findings

### 1. Step 3 and the template's comment give two different shapes for the `Result` cell of the row step 3 adds

severity: should
location: `agents/sealer.md:66-69`, `templates/sdd-guarantee.md:15-17`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:86-87`
verdict: deferred the frame
refixes: round-4#1

The unit refixed: step 3's sentence and the template's comment, units 1011463b changed. A sealer that follows the template drops the answering row step 3 asks it to name. One that follows step 3 writes a cell the template does not allow. 1011463b's step 3 says each 🔴 or 🟡 row closed by another kind's word is written into `## Claims re-run`, "its `Result` the later round's row that answers it or `does not hold`". The same commit's comment over that table says "`Result` reads `holds`, or `does not hold — <what came back>`". For a row a later round answered, the two give different cells. The template's `holds` loses the coordinate of the answering row, which is the naming round 3's fix added and round 4 asked a place for. Step 3's form is neither of the template's two. The frame holds both forms: `spec.md:86-87` is step 3's, and `spec.md:397-398` (§*Data & interfaces*) is the template's. So the build copied a disagreement the reframe wrote. It is the class this phase removed, one cell stated in two files that do not match. A second gap goes with it. The old comment gave one row per claim, per `fixed <commit>` row and per removal. The new "One row per act … whatever the act" no longer says a row is per thing checked, while step 3's acts each cover many things. The template's `Command` column reads `<the command re-run>`, and this act re-runs nothing. `fix of a fix`: step 3's sentence and the template's comment are units 1011463b changed

read: `agents/sealer.md:60-71`, `:129-134` (each claim's row names the command re-run); `templates/sdd-guarantee.md:13-21`; `spec.md:76-92`, `:388`, `:396-399`. read: `chain_check.py#guarantee` reads only the `Verdict:` line, so no check reads the `Result` cell and nothing refuses either shape. A sealer reading both files gets two answers for one cell. executed: the paste below applied in the clone. The new T21 fails on the shipped step 3 (exit 1) and passes on the pasted one. The module (14 passed), `test_docs_line_wrap.py`, `test_no_passage_is_pasted_into_a_second_file.py` and `test_the_rules_have_one_owner.py` (63 passed) all pass with it. The clone was restored after

`agents/sealer.md:64-69`, step 3 from "Read every 🔴 and 🟡 row" to "For":

```markdown
   the row's `Location`. Read every 🔴 and 🟡 row of every record: the
   check reads a row's word and not its mark, so one closed `confirmed` or
   `❓ out of verified scope` passes it and answers nothing. Write each one
   as a row of `## Claims re-run`, its `Command` the records you read, its
   `Result` `holds — <the later round's row that answers it>` or
   `does not hold — <no later round answers it>`; unless a later round's
   row answers it, the verdict is `not sound`. For
```

`templates/sdd-guarantee.md:15-17`, the comment over `## Claims re-run`:

```markdown
<!-- One row per act of `agents/sealer.md` step 3, whatever the act, and one
per thing the act checks. `Result` reads `holds`, or `does not hold — <what
came back>`, and a `does not hold` is what the verdict names. -->
```

`tests/test_the_sealer_guarantees.py:302-304`, T21's third assertion:

```python
        assert (
            "its `Result` `holds — <the later round's row that answers it>` or "
            "`does not hold — <no later round answers it>`"
        ) in step
```

`seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:85-88`,
so the frame states the one form:

```markdown
   word and not the mark, and it answers no finding — write a row of
   `guarantee.md`'s `## Claims re-run`, its `Result` `holds — <the later
   round's row that answers it>` or `does not hold — <no later round
   answers it>`; a `does not hold` makes the verdict
   `not sound`. For every `## Removes` row of `spec.md` and every removal this
```

answer: orchestrator: both are fixes of a fix, the third reframe in this run; the frame re-examines what the sealer duty and S21 exist to cover

### 2. S21 and the reframe's statement that the frame's three documents follow its rule on figures are not true at the target, and the reader the rule names does not read two of the five documents

severity: should
location: `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:389`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:461-463`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/plan.md:39-40`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/questions.md:65-66`
verdict: deferred the frame
refixes: round-4#2

The unit refixed: S21, the two compliance sentences and the enforcement sentence, units 76d7df7d added. 76d7df7d wrote S21 ("every figure in them is a measurement naming its commit, round or tag, a bound …, or gone") and wrote at `plan.md:39-40` and `questions.md:65-66` that "the frame's own three documents were rewritten to it at the reframe". Phase 5b's divergence 3 lists the figures that break it. Judged one by one against §*A number in this frame*: (a) `questions.md:44-45`, "caught nothing in the 36 records in the tree", is wrong. It is round 2's probe, and `spec.md:227` and `plan.md:146` say so, but this sentence names no moment, and the tree holds 39 records at the target. (b) `questions.md:79` (Q3, answered), "the 70 test modules", is the wording of a question asked before phase 3 and answered by `phases/phase-3.md`. It is a moment by its context and not wrong. (c) `questions.md:81` (Q5, open), "the 52 test modules", is `plan.md:99`'s figure at 680142f2 (`plan.md:63`, "Read at 680142f2"). It is a frame-time figure for part B, whose phases sort the modules themselves, so nobody acts on it wrongly. By S21's letter, though, its sentence has to say which kind it is. (d) `questions.md:83`, "`carried_by` and its four cases", is true at the target and is still a count of the tree with no moment. (e) `plan.md:186`, "the 35 `§N` citations", is pinned to 680142f2 at `spec.md:263` and `questions.md:32` but not in the row part B's smith is spawned from. S18's grep holds the result at any count. (f) `plan.md:187`, "the 32 modules pinning the definition", is pinned nowhere, and S17 holds it. (g) Alternatives E and F (`plan.md:133-134`) give the grounds of a rejected design. They are frame-time by the table they sit in, and what they count has left, so no commit can move them. So one figure is wrong, and four more fall short of the rule's letter while no agent would act on them wrongly. The defect is the criterion and the claim of compliance, which are units these commits wrote. A sealer that checks S21 against the tree names `spec.md` as the party the tree contradicts, at the end of the run. The rule's only reader also does not read these files. `spec.md:461-463` and S21 say "the sealer's step 4 reads the five documents against the tree", but `agents/sealer.md` step 2 reads `spec.md`, `plan.md` and `changelog.md` and neither `questions.md` nor `overview.md`, and step 4's parties are the spec, the build, the last record, the changelog and the pull request body. Those two documents reach the sealer only inside `git diff <base>...HEAD`. `fix of a fix`: S21, the two compliance sentences and the enforcement sentence are units 76d7df7d added. The counts themselves are older (41bf39d1 for (a), earlier frames for the rest)

executed: `git ls-tree -r --name-only <rev>` filtered to `seal/specs/*/rounds/round-N.md` gives 35 at 680142f2, 37 at 41bf39d1, 39 at 1011463b and 39 at 66d0180b. `git blame` puts `questions.md:44` at 41bf39d1, `:79-83` and `plan.md:133-134`, `:186-187` at fcbb164b, cba5e0cd and d3da26dd, none of them in b065c7a5..66d0180b. read: `plan.md:61-100` (Technical context, "Read at 680142f2", with 52 at `:99`), `spec.md:263`, `:388-389`, `:442-463`, `agents/sealer.md:56-76`. read: the counts of modules for (b), (c) and (f) could not be recomputed by the frame's method, which no document names. `git grep -l` over `tests/test_*.py` gives 69 → 42 modules naming the three scripts and 63 → 48 naming `agents/` between 680142f2 and the target. These are another method's counts and are not the frame's figures. They show only that a present-tense reading of (b) and (c) is false now. The paste pins each figure at the sentence that states it, using the moments the frame already records, and makes the enforcement sentence say who reads what

`seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/questions.md:44-45`:

```markdown
  the next round found, and the finding-only word set caught nothing in the 36
  records round 2's probe read (`spec.md` §*What leaves*; alternative R). What that
```

`questions.md:81`, Q5's question cell:

```markdown
| Q5 | Of the pins the test modules naming an `agents/` file hold on it (52 at 680142f2, `plan.md` §*Technical context*), which pin a rule and which pin narration? |
```

`questions.md:83`, the last sentence of Q7's status cell:

```markdown
Overturning it is a change to `carried_by` and the cases phase 5 added for it (`phases/phase-5.md`) |
```

`plan.md:186`, row 6's clause:

```markdown
the `§N` citations outside the rewritten files (35 at 680142f2; counted again on part B's tree) rewritten in the same commit
```

`plan.md:187`, row 7's clause:

```markdown
the modules pinning the definition re-pointed or removed with a row
```

`spec.md:459-463`, the rule's enforcement sentence:

```markdown
`rounds/round-N.md` and `phases/phase-N.md` are moments by construction and
keep their figures, and so are a question's wording once it is answered and
the grounds in `plan.md`'s Alternatives table. Enforced by: nothing — a
reading that sorts figures by their sentences is a report, not a gate
(`CLAUDE.md`). Each round's warden reads the five documents; the sealer
reads `spec.md`, `plan.md` and `changelog.md` in its step 2, and
`questions.md` and `overview.md` only inside the diff.
```

`spec.md:389`, S21's third cell:

```markdown
every figure in them is a measurement naming its commit, round or tag, a bound a named check holds the tree to, or gone (§*A number in this frame*); the `## Removes` row *the present-tense counts* lists each one that left, and each round's warden reads the five documents against the tree
```

answer: orchestrator: both are fixes of a fix, the third reframe in this run; the frame re-examines what the sealer duty and S21 exist to cover

## Confirmations

| Confirms | What holds | Location | Grounds |
|---|---|---|---|
| round-4#1 | round-4#1 is closed: the sealer's acts are listed in `agents/sealer.md` step 3, the document and the template point at it and list none, and the row the old "Name each one" had nowhere to put is a row of `## Claims re-run` | `agents/sealer.md:60-71`, `docs/the-review-record.md:118-123`, `templates/sdd-guarantee.md:15-17` | read: §*The guarantee*'s second paragraph keeps its bold sentence and *It does not re-judge…*, and between them names step 3 and step 4 and no act. The template's comment names no act. Step 3 tells the sealer to write each 🔴 or 🟡 row closed by another kind's word into `## Claims re-run`, and the open-row paragraph at `docs/the-review-record.md:79-81` says the same. read: `git grep` for "re-runs a sample", "sample of the smith", "touches the row's" and "stands in the tree" outside `seal/specs/` finds the acts only in step 3. It also finds the definition's frontmatter `description` and `README.md:42`, both one-line summaries of the role, and no list a duty could be missing from. The one disagreement left between the two homes is the `Result` cell, which is 🟡 1 |
| round-4#2 | round-4#2 is closed: no sentence states a count of unpriced cases, and the bound and its case stand where the count stood | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:481`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/questions.md:51-54` | read: `grep` for 226, 228 and 229 in the five documents finds only `spec.md:458`, the rule's own example of a figure that leaves. `spec.md:481` names `STALE_SHARE` and the case that holds it. `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:98` sets `STALE_SHARE = 0.05`, and `:344` is the named case. executed: `bin/test tests -q -rs -k test_the_durations_file_prices_the_suite` exit 0, 1 passed, so the bound the sentence names holds at the target. The module alone skips the case by design ("the suite was not collected") |
| none | T21, T22 and T23 are meaningful pins: each fails on the tree before its sentence and holds the sentence against the regression it names | `tests/test_the_sealer_guarantees.py:154-165`, `:290-304`, `:311-321` | executed: with `agents/sealer.md`, `templates/sdd-guarantee.md` and `docs/the-review-record.md` at b065c7a5, all three fail (exit 1, 3 failed), and at 66d0180b they pass (exit 0). executed: step 3's `Result` clause changed to another wording fails T21 (exit 1). read: `between` slices step 3 by its two step headings and §*The guarantee* by its own heading and `## The run`, the next `##` heading, so a sentence moved to another step or section fails too. executed: a limit, not a finding. The absence lists name four and three tokens, so the template re-listing the acts as "per claim re-run, per commit confirmed and per deletion checked" passes T22, and §*The guarantee* re-listing them as "re-runs the smith's sampled claims and confirms each fixed commit and each removal" passes T23 (exit 0 each). A pin on wording cannot refuse every paraphrase. What it catches is the copy round 4 found, `fixed <commit>` back in either file, and the pointer dropped. That is what each Test row in `plan.md:210-212` says it catches, and the next round's warden reads the rest |
| none | the figures that stayed in `changelog.md` and `overview.md` name their moment and hold at it | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/changelog.md:92-103`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/overview.md:39-40`, `:45`, `:58`, `:60`, `:84` | executed: `git show ce448bbe:<file> \| wc -l` gives 6,153, 5,596, 3,648, 303, 460, 998 + 880 + 847 = 2,725, and 268, as the table says. `origin/release/v0.22.0` resolves to ce448bbe in the clone. `git show 4632eeea:.test_durations` gives 7,348 entries summing to 3,371.9 s. `git grep -E "round [0-9]+'s ⬜"` outside Markdown gives 19 lines at 665f4706 and 16 at 1011463b, as phase 5b says. read: every other figure in `overview.md` is a past-tense account at a commit, a round or a phase record, or an estimate stated as one. The changelog's remaining numbers are rule constants (five facts, three finding rounds). Nothing in either file is a count of the tree with no moment |
| none | the changelog fragment still tells a 0.21.1 user what changed, and no figure in it can go stale | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/changelog.md:3-103` | read: the four entries under `### Changed` say what a user meets: one round file, what the check fails on, where the broad run is written, and that a sealer spawn costs an Opus session. Each says what to do where something is owed (the `hygiene.yml` tag and the removed fetch step). The `### Removed` entry says what is gone, what a script typing `round-record` meets now, and which documents give way to which. Its table no longer shows how much each kept file shrank. It now says how large each was at ce448bbe, which files are gone, and that the three documents became one, and it sends a reader who wants the size after to `wc -l`. That is less than the old table told, and none of it is false. A count in a release note that a later commit could make false is gone. A release note recording a moment is history, so the column at ce448bbe can stay. "before this work item" is this repository's word in a user-facing line, which is a sentence that reads badly and not a finding |
| none | round 4's ❓ (whether a behaviour eval is owed for step 3's duty) has an answerer and a default | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/questions.md:84`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/plan.md:154`, `:189` | read: Q8 states the question with the owner as its answerer and part B's phase 9 as the default. Alternative Z records the choice, and row 9 names the case `rule-sealer-closed-by-another-kinds-word` and what its verdict line must match. Nothing in part A runs it, and S20 says part A holds it by wording only |

## Not judged

| What | Location | Who answers |
|---|---|---|

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the worktree into `<scratchpad>/923-r5/clone`, checked out at 66d0180b, with `origin/release/v0.22.0` fetched from the worktree | every run below ran there. The worktree was only read, apart from this file |
| `bin/test tests/test_the_sealer_guarantees.py -q -p no:xdist` | exit 0, 14 passed |
| `test_tmp_r5_mutations.py` (plain `python3 -I`), `bin/test tests/test_the_sealer_guarantees.py -q -p no:xdist -k "<T21> or <T22> or <T23>"` per state | at 66d0180b: exit 0, 3 passed. The three files at b065c7a5: exit 1, 3 failed (T21, T22, T23). The template re-listing the acts in other words: exit 0, 3 passed. §*The guarantee* re-listing them in other words: exit 0, 3 passed. Step 3's `Result` clause reworded: exit 1, T21 failed. The files were restored and `git status` was empty |
| `test_tmp_r5_paste.py` (plain `python3 -I`): 🟡 1's paste applied | the new T21 on the shipped step 3: exit 1, 1 failed. With the paste applied, `tests/test_the_sealer_guarantees.py`: exit 0, 14 passed. `test_docs_line_wrap.py`, `test_no_passage_is_pasted_into_a_second_file.py` and `test_the_rules_have_one_owner.py`: exit 0, 63 passed. The files were restored and `git status` was empty |
| `bin/test tests/test_the_sealer_guarantees.py tests/test_chain_check.py tests/test_docs_line_wrap.py tests/test_no_real_identifiers.py tests/test_one_word_one_meaning.py tests/test_the_rules_have_one_owner.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_a_document_that_names_a_script_says_how_to_reach_it.py -q -rs` | exit 0, 168 passed, 6 skipped ("no shipped document names it, so nobody goes looking") |
| `bin/test tests -q -rs -k test_the_durations_file_prices_the_suite` | exit 0, 1 passed. The module run alone skips it ("the suite was not collected") |
| `bin/rules --check --root <clone>` | exit 0: all 402 `Enforced by:` targets in 60 rule files resolve |
| `chain_check.py --baseline origin/release/v0.22.0 --root <clone>`, before this file | exit 0. The pull request's state is unknown, so nothing was judged as ready. Three lines owed later: round 4's `Target SHA` is behind 1011463b, so a verifying round is owed, and `broad-gate.md` and `guarantee.md` are the sealer's |
| `git show ce448bbe:<file> \| wc -l` for the changelog's nine files; `git show 4632eeea:.test_durations` summed; `git grep -E "round [0-9]+'s ⬜"` outside Markdown at 665f4706 and 1011463b | 6,153 · 5,596 · 3,648 · 303 · 460 · 998 + 880 + 847 · 268; 7,348 entries, 3,371.9 s; 19 and 16 lines |
| `git ls-tree -r --name-only` filtered to round records at 680142f2, 41bf39d1, 1011463b and 66d0180b; `git grep -l` over `tests/test_*.py` at 680142f2 and 66d0180b; `git blame` on the lines 🟡 2 names | 35 · 37 · 39 · 39 records; 69 → 42 modules naming the three scripts, 63 → 48 naming `agents/`, by this method; blame as in 🟡 2's Grounds |
| this file copied into the clone and staged, then `bin/test tests/test_no_real_identifiers.py tests/test_one_word_one_meaning.py tests/test_docs_line_wrap.py tests/test_chain_check.py -q` | exit 1, 96 passed, 1 failed. The one failure is `TestMain::test_a_record_written_by_the_old_generator_reads`, which reads every `round-N.md` in the tree. It names this file's two rows as open, `(41, '🟡 1', 'open')` and `(42, '🟡 2', 'open')`, with no parse error. So the case stays red until those two rows read a closing word |
| the full suite | not run: `unverified`, the sealer's |

Every probe file and the clone sat under `<scratchpad>/923-r5/` and were
deleted with it.

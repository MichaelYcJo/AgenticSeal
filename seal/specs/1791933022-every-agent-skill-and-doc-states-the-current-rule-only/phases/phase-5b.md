# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — phase 5b

| Field | Value |
|---|---|
| Phase | 5b |
| Commit | 704395b1, the last build commit; this record's commit follows it |

## What this phase was asked

`plan.md`'s row 5b, the repair after round 4 and part A's last phase. It
adds no mechanism and changes no code beyond tests. (i) The sealer's acts are
listed once, in `agents/sealer.md` step 3. Its "Name each one" becomes a row
of `## Claims re-run` whose `Result` is the later round's row that answers it
or `does not hold`, and the `not sound` clause stays.
`docs/the-review-record.md`'s open-row paragraph ends with the sealer writing
such a row into `guarantee.md`, and its `Enforced by:` gains T21.
§*The guarantee*'s second paragraph drops its copy of the list, points at
steps 3 and 4, and gains `Enforced by:` T23. The comment in
`templates/sdd-guarantee.md` over `## Claims re-run` lists no act. T21, T22
and T23 go in `tests/test_the_sealer_guarantees.py`, each seen red first.
The changelog's sealer entry gains one clause on where the row lands.
(ii) The stored counts leave the builder's two documents: `changelog.md`'s
*Lines after* column and its sentence on test modules and test lines leave,
and `overview.md`'s two durations figures name 4632eeea. §*Part A and part
B* names 5a and 5b. (iii) This record. `rounds/*.md` are not edited, and part
B is out of scope.

## What this phase found

**The frame held at its coordinates.** Round 4's two locations,
`templates/sdd-guarantee.md:15-16` and `docs/the-review-record.md:117-125`,
held the old three acts as quoted. Step 3 held "Name each one".

**T21, T22 and T23, red then green** (`executed`, `bin/test
tests/test_the_sealer_guarantees.py -q -p no:xdist`, with `-k` on the three
for the red run):

| Run | Exit | What failed |
|---|---|---|
| the three cases, on the tree before any sentence | 1, 3 failed | T21: `'each one as a row of \`## Claims re-run\`' in` step 3. T22: `'One row per act of \`agents/sealer.md\` step 3, whatever the act' in` the comment, which read `per claim sampled, per \`fixed <commit>\` verdict and per removal`. T23: `'\`agents/sealer.md\` step 3' in` §*The guarantee* |
| the module, after the sentences | 0, 14 passed | — |

My first T21 lowered the step text and then looked for a capitalised
heading, so it could never pass. The red run showed that, and the case was
fixed before any sentence was written.

**Six breaks through `mutation-check`, each `red`** (exit 0 from the tool,
the case exit 1). In step 3, the `## Claims re-run` clause was replaced and
the `does not hold` result was dropped (T21). In the template, `fixed
<commit>` was put back into the comment with the pointer kept, and the
pointer was dropped (T22). In §*The guarantee*, `fixed <commit>` was put
back with the pointer kept, and the pointer was dropped (T23). The first
break of each pair is the mutation the Test rows name. The template break
first tried as `step 3, whatever the act.` → `step 3, per \`fixed
<commit>\` verdict.` also removed the pointer phrase, so it went red on the
pointer. A second break that kept the pointer went red on `AssertionError:
\`fixed <commit>\``.

**What the class check finds beyond the frame's three.** `git grep -n
"fixed <commit>"` outside `seal/specs/` and `changelog/` finds the three the
row names: `docs/the-review-record.md:20` and `:32`, both in §*The round
record*, `templates/sdd-round.md:31` and `agents/sealer.md:63`. It also
finds `chain_check.py:87`, the refusal's words for a 🔴 or 🟡 row in
`CLOSES_BY`, with its two pins at `tests/test_chain_check.py:529` and `:563`,
and the absence strings in T22 and T23. None of these lists what the sealer
does, so they stay. The divergence row is in `overview.md`. `:32`'s
`Enforced by: nothing — … the sealer re-checks every \`fixed <commit>\`` names
one sealer act as the enforcement of a fix-pass rule. It is in §*The round
record*, which the frame expected, and it is not a list.

**The counts that left or were pinned** (`executed` where a figure was
recomputed). The changelog's *Lines before* figures were recomputed at
ce448bbe with `git show ce448bbe:<file> | wc -l`, and every one held: 6,153,
5,596, 3,648, 303, 460, 268, and 998 + 880 + 847 = 2,725. The column is now
headed with that commit. Each gone file says `gone` in its own cell, and
`wc -l <file>` in the release stands where the after column was.
`overview.md`'s 7,348 entries, 3,371.9 s, and 1,144.7 s over 42 modules were
recomputed from `git show 4632eeea:.test_durations` and the modules naming
`chain_check` or `broad_gate` at that commit. All four held, and each
sentence now names 4632eeea. Reading the overview against the frame's three
kinds found four more present-tense counts, and each now names its moment:

- the 38 runs and the 22 rounds with truth, both from the suite build
  (`phases/phase-2-suite-build.md`);
- the four smith cases, at c7d8bcc8;
- the 19 code comments citing a ⬜, at 665f4706. That one had already gone
  false: `git grep -E "round [0-9]+'s ⬜"` outside the Markdown files finds
  19 lines at 665f4706 and 16 at 1011463b.

**The five documents read against §*A number in this frame*** (`read`,
except where a cell says `executed`):

| Document | What stays, and why |
|---|---|
| `changelog.md` | the *Lines before* column, at ce448bbe; release numbers. The rest are rule constants: five facts, three finding rounds, eleven fields |
| `overview.md` | each figure names a commit (c7d8bcc8, 4632eeea, 665f4706, ed63c3af, e8155d0d, cba5e0cd, 27dd748d), a round's finding, a phase record, or phase 5 in the proof block. Estimates are stated as estimates. `three guarantor cases` is the design's count |
| `spec.md` | §*The chain as it stands, measured* is at 680142f2 by its heading, and §*What leaves*' evidence column repeats those figures for what left. The 36 records at `:227` is round 2's probe. The 35 and 423 citations are at 680142f2. S12's 1,500 s is a bound held by its check. Estimates (≈ $2–4, 5–9 KB a definition, ≈ 120 runs) are stated as estimates or as the owner's budget |
| `plan.md` | the Technical context is "Read at 680142f2". 4,553 s is at 680142f2, `:225`. The 301 entries and 36 records are round 2's. Costs are estimates |
| `questions.md` | 35 is at 680142f2. Q1's per-item round counts and Q7's probe (cba5e0cd, af4d0c31) are history. ≈ 120 runs and ≈ $150 is the owner's budget, dated |

**Where the frame does not hold: counts in the framer's documents with no
moment.** These are the framer's to rewrite and are not edited here:

- `questions.md:44` says the word set "caught nothing in the 36 records in
  the tree", with no moment. `executed`: 39 files match
  `rounds/round-[0-9]*.md` at 1011463b. `spec.md:227` names the same figure
  as round 2's probe, and the questions sentence does not.
- `questions.md:79` (Q3, answered) says "the 70 test modules", and
  `questions.md:81` (Q5, open) says "the 52 test modules". Both are
  680142f2's figures in `plan.md`'s Technical context, and neither sentence
  says so.
- `questions.md:83` (Q7) ends with "`carried_by` and its four cases". It is
  true at 1011463b: `TestCarriedBy`'s two cases and two `TestMain` cases. It
  is a count of the tree with no moment.
- `plan.md:186` (row 6) says "the 35 `§N` citations outside the rewritten
  files", and `plan.md:187` (row 7) says "the 32 modules pinning the
  definition". The first is pinned to 680142f2 in `spec.md:263` and
  `questions.md:32` but not in the row. The second is pinned nowhere.
- `plan.md`'s Alternatives E and F say "365 s of tests", "8 of 14 failed
  October hygiene runs" and "227 spec lines". These describe the tree before
  this branch, and the frame's measurement at 680142f2 is their moment. The
  sentences do not say so. What they count has left, so later commits cannot
  move them.

**The checks** (`executed`, at 704395b1):

| Check | Exit |
|---|---|
| `bin/test tests/test_the_sealer_guarantees.py -q -p no:xdist` | 0, 14 passed |
| `bin/test` over `test_the_sealer_guarantees.py`, `test_docs_line_wrap.py`, `test_no_passage_is_pasted_into_a_second_file.py`, `test_the_rules_have_one_owner.py`, `test_a_document_that_names_a_script_says_how_to_reach_it.py` (`-q -rs`) | 0, 108 passed, 6 skipped ("no shipped document names it, so nobody goes looking") |
| `bin/test` over `test_docs_line_wrap.py`, `test_no_passage_is_pasted_into_a_second_file.py`, `test_no_real_identifiers.py`, `test_one_word_one_meaning.py`, after the overview and changelog edits | 0, 72 passed |
| `bin/rules --check --root <worktree>` | 0, all 402 `Enforced by:` targets in 60 rule files resolve. That is 400 before this phase and the two new targets |
| `chain_check.py --baseline origin/release/v0.22.0 --root <worktree>` | 0. The pull request's state was unknown, so nothing was judged as ready. It printed no row refusal. It printed three lines owed later: round 4's `Target SHA` is behind 1011463b, so a verifying round is owed, and `broad-gate.md` and `guarantee.md` are the sealer's |
| `ruff check` and `ruff format --check` (`uvx ruff`) on `tests/test_the_sealer_guarantees.py` | 0 and 0 |
| the full suite | not run: `unverified`, the sealer's |

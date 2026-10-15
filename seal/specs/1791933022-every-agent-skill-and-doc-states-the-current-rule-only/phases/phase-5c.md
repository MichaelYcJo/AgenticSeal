# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — phase 5c

| Field | Value |
|---|---|
| Phase | 5c |
| Commit | 4c552b0b, the last build commit; this record's commit follows it |

## What this phase was asked

`plan.md`'s row 5c, the repair after round 5 and part A's last phase. It
closes the trade the reframe after round 2 made, in the check, and removes
the sealer duty that rounds 3, 4 and 5 each repaired. (i)
`chain_check.py#open_findings`: a row whose first cell opens with a mark of
`FINDINGS` closes only by `fixed` with a commit, `answered` or `deferred`
with a home, and every other row closes by any word of `CLOSED_WORDS`, as
phase 5a reads it. The refusal's wording is unchanged. The module docstring,
`open_findings`'s docstring and the comment over `CLOSES_BY` are rewritten
in place. T24 replaces T20 test-first and is seen red on 704395b1's
`open_findings`. The refusal case gains a `🔴 1 … confirmed` row, and the
corpus case reads every record in the tree under the new reading. (ii) The
duty sentence leaves `agents/sealer.md` step 3, with round 3's pin and T21;
T22 and T23 stay. `templates/sdd-guarantee.md`'s comment takes round 5's
paste. `docs/the-review-record.md`'s open-row paragraph and its `Enforced
by:`, the vocabulary paragraph's `Enforced by:` and `templates/sdd-round.md`'s
closing comment are rewritten, and the class `git grep` the row names is
run, with each hit stating the old reading rewritten outside `seal/specs/`.
(iii) The changelog fragment's check sentence and sealer clause, and one
divergence row in `overview.md`, with the row on the sealer's acts re-read.
(iv) This record. `rounds/*.md` are not edited, and part B is out of scope.

## What this phase found

**The frame held at its coordinates.** `chain_check.py:17-18` held "every
row of every record reads a closing word, whatever its mark", the comment
over `CLOSES_BY` held "It picks the message only", and `agents/sealer.md`
step 3 held the duty from *Read every 🔴 and 🟡 row* to *the verdict is
`not sound`*. `open_findings` was unchanged between 704395b1 and 543c74eb
(`git diff --stat 704395b1 HEAD` over `skills/` and `tests/` printed
nothing), so the red run at the phase's start is a run on 704395b1's
`open_findings`.

**How the check reads the fact.** Two constants carry it: `FINDING_WORDS`
(`fixed`, `answered`, `deferred`) and `FIXED`. `CLOSED_WORDS` is now
`FINDING_WORDS` and the warden's and the old generator's words, so the two
sets cannot drift apart. A finding row closes where its verdict word is in
`FINDING_WORDS` and, for `fixed`, `SHA_RE` finds a commit in the visible
`Verdict` cell. The home of a `deferred` is read as phase 5a reads it,
through `verdict_of`, so a homeless `deferred` stays open for every mark.

**How it errs, beyond the spec's stated case.** `SHA_RE` takes any word of 7
to 40 hex letters, so `fixed accede1` reads as a commit; nothing checks the
commit exists. The sealer's step 3 confirms each `fixed <commit>` is on the
branch, so a word that is not one is caught there. The old generator's
`agreed, fixed`, `withdrawn` and `not a defect` no longer close a 🔴 or 🟡
row; the corpus case reads every record in the tree with none of them on a
finding row.

**T24, red then green** (`executed`, `bin/test tests/test_chain_check.py -q
-p no:xdist -k test_a_finding_row_closes_only_by_a_fix_passs_word`):

| Run | Exit | What failed |
|---|---|---|
| T24 on 704395b1's `open_findings` | 1, 1 failed | `assert [] == [('🔴 1', 'confirmed'), ('🟡 2', 'out of verified scope'), ('🔴 3', 'fixed')]` |
| `tests/test_chain_check.py` after the change, all cases | 0, 33 passed | — |

T24 carries the row's ten rows and three more that pass: `🔴 6 … fixed
abc1234`, `🟡 7 … answered` and `🟢 … fixed abc1234`. The first two hold the
narrowing against refusing a fix pass's own words; the third is S3's *a 🟢
row at `fixed <sha>` passes*.

**The corpus run.** `test_a_record_written_by_the_old_generator_reads` read
every `rounds/round-N.md` in the tree under the new reading and passed: 41
files at 4c552b0b (`ls seal/specs/*/rounds/round-*.md` lists 75, of which 34
are `round-N-report.md`), this item's rounds 1–5 among them.

**Four breaks through `mutation-check`, each `red`** (the tool's exit 0, the
cases' exit 1):

| Break | Cases | What failed |
|---|---|---|
| the `FINDINGS` narrowing dropped (`if seen[0]…startswith(FINDINGS):` → `if False:`) | T24 | `assert [] == [('🔴 1', …)]` |
| `fixed` with no commit accepted (the `SHA_RE` clause → `True`) | T24 | right contains one more item, `('🔴 3', 'fixed')` |
| the narrowing applied to every mark (→ `if True:`) | T24 | left contains three more items, the first `('🟢', 'confirmed')` |
| the narrowing dropped, against the refusal case | `TestMain::test_the_refusal_names_the_words_that_close_a_row_of_its_mark` | four lines named, not five; the `🔴 1 … confirmed` row went unnamed |

The fourth is the refusal case's new row seen red, which the row asks for by
naming the row and not a break. `git status --short` was empty after each.

**The class grep.** `git grep` for the row's five phrases outside
`seal/specs/` and `changelog/0.*.md`, after the edits: `whatever its mark`,
`whatever mark`, `reads the word and not the mark` and `another kind's word`
find nothing; `answers nothing` finds `skills/verify/SKILL.md:358`, a
message in `broad_gate.py` and two test docstrings, none about a verdict
row. Widened to `changes nothing`, `picks the message only`, `closing word`,
`still open`, `closes by` and `out of verified scope`: the hits that state
the rule are `.github/workflows/hygiene.yml:169-170` (*a verdict row of any
mark still open*), `templates/hygiene.yml:83` (*a verdict row still open*),
`templates/config.md:121-127` (the verdict words a translation keeps),
`docs/the-agent-set.md:56` and `README.md:42`. Each stays true under the new
reading. `skills/code-review/scripts/chain_check.py:84`'s *picks the message
only* is the rewritten comment, which now says it of the rest of the table.

**Where the row was narrower than the paragraph.** The row names the
open-row paragraph's last two sentences. The paragraph's third sentence, *The
mark at the head of the row … changes nothing*, stated the old reading too,
so the paragraph is rewritten from its second sentence on. The rewrite also
gives the spec's *How it errs* (`spec.md` §*What leaves*, the severity row):
a row whose severity stands only in its Finding cell closes by any closing
word. `overview.md` §*Part A and part B* named phases 5a and 5b as the last;
it names 5c now.

**`overview.md`'s row *What the class check for the sealer's acts finds*,
re-read** (`read`, at 4c552b0b): it holds. Step 3 still names `fixed
<commit>` as an act, `CLOSES_BY` still carries the fix pass's words with two
pins in `tests/test_chain_check.py`, and the list of the sealer's acts stands
in step 3 alone, now three acts.

**The checks** (`executed`):

| Check | Exit |
|---|---|
| `bin/test tests/test_chain_check.py tests/test_the_sealer_guarantees.py tests/test_docs_line_wrap.py tests/test_one_word_one_meaning.py -q`, at 2fab5421's tree | 0, 103 passed |
| `bin/test tests/test_the_sealer_guarantees.py -q -p no:xdist --collect-only`, grepped for T21 and round 3's pin | 0; neither name collected |
| `bin/test tests/test_docs_line_wrap.py tests/test_one_word_one_meaning.py -q`, after the changelog and overview edits | 0, 58 passed |
| `bin/rules --check --root <worktree>` | 0, all 403 `Enforced by:` targets in 60 rule files resolve: 402 at 704395b1, less T21, and T24 named in two paragraphs. `git grep` finds T21's name nowhere outside `seal/specs/` |
| `chain_check.py --baseline origin/release/v0.22.0 --root <worktree>`, at 4c552b0b | 0. The pull request's state was unknown, so nothing was judged as ready, and no row was refused under the stricter reading. It printed three lines owed later: round 5's `Target SHA` is behind dea5471a, so a verifying round is owed, and `broad-gate.md` and `guarantee.md` are the sealer's |
| `uvx ruff check` and `uvx ruff format --check` on `chain_check.py`, `tests/test_chain_check.py` and `tests/test_the_sealer_guarantees.py` | 0 and 0 |
| the full suite | not run: `unverified`, the sealer's |

# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — review round 6

| Field | Value |
|---|---|
| Target SHA | 5930b506, fixes 81e8d785..5930b506 |

Extended past round 5: round 5 found 2, round 4 found 2, and the frame took round 5's fixes of a fix by changing the mechanism, not patching it.

A verifying round over the reframe after round 5 (4e2a5068), its approval
(543c74eb) and phase 5c (dea5471a, 2fab5421, 4c552b0b, 5930b506), part A
only. Both of round 5's findings are closed. The repair moved the rule into
the check instead of patching the sealer's duty a fourth time, and that move
holds. The check can only refuse more than phase 5a did. Every shape rounds 1
and 2 found hiding still fails, and the duty left with no reference behind
it.

One new 🟡 row follows, marked `fix of a fix`, because it sits in
`open_findings`, the unit dea5471a changed. The check finds the finding's mark
with `startswith` on the raw first cell. So a mark in bold, italics or a code
span reads as no mark, and such a row closes `confirmed` as phase 5a would
read it. The `Verdict` cell beside it is read with emphasis taken off, so the
two cells of one row are read by two rules. The paragraph that says how the
check errs names one case only. It leaves out this one and the hex-word
reading of `fixed`.

Two figures in the work item's own documents are wrong at the moment they
name. They are not graded, since a frame-time figure in a planning document
is not a finding this round, but the frame should know of them when it takes
🟡 1. `spec.md` §*What leaves* (the severity row, "How it errs") says "204 🟢
rows in the tree name an earlier round's 🔴 or 🟡 there", and `plan.md`
Alternative AB says the reading would refuse `confirmed` "on most 🟢 rows in
the tree (204 at 81e8d785)". At 81e8d785 the tree holds 205 🟢 rows, and 204
of them read `confirmed`. 21 name a 🔴 or 🟡 in the Finding cell and 34 in any
cell. The rejection AB records still holds at 34, because those rows would
still fail records the check must read. `phases/phase-5c.md` §*The corpus
run* says 41 records at 4c552b0b, and `git ls-tree` finds 40 there: 75 files,
35 of them `round-N-report.md`.

Findings from reading and from execution are labelled in each Grounds cell,
and every command named there is in `## Executed probes`. The full suite was
not run. It is `unverified`, and the sealer answers it.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 5's 🟡 1 is closed: the `Result` cell of `## Claims re-run` has one shape, the template's, and the row that had two shapes left with the duty that wrote it | `agents/sealer.md:60-65`, `templates/sdd-guarantee.md:15-21`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:85-90`, `:399-404` | confirmed | read: step 3 holds three acts and states no `Result` shape. The template's comment gives `holds` or `does not hold — <what came back>` and now says one row per thing the act checks, which was round 5's second gap. `spec.md` §*The sealer* item 3 and §*Data & interfaces* give the same shape and say step 3 gives none. The sealer's rule *Each claim's row names the command you re-ran* (`agents/sealer.md:123-127`) agrees with the template's `Command` column, and the act whose row re-ran nothing has left. executed: `tests/test_the_sealer_guarantees.py` passes in the narrow run, so T22 and T23 hold the template's and the document's pointers unchanged |
| 🟢 | round 5's 🟡 2 is closed: S21 covers the shipped surface, the two claims of compliance are gone, the frame says which documents the sealer reads as step 2 reads them, and `questions.md:44` names its moment | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:393`, `:454-496`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/plan.md:40-41`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/questions.md:41-48`, `:62-71` | confirmed | read: S21 now covers `changelog.md` and the `docs/` sentences this item rewrote, and the work item's documents are readings at a moment. "the frame's own three documents were rewritten to it at the reframe" stands in neither `plan.md` nor `questions.md`. `spec.md:491-496` says the sealer reads `spec.md`, `plan.md`, every phase record, every round record and `changelog.md` in step 2, which is `agents/sealer.md:56-59` word for word. It also says step 4 counts nothing against the tree. executed: `git grep` for "five documents", "five living", "step 4 reads" and "reads the five" finds only `spec.md:492`, the warden's line, and `spec.md:517`, the `## Removes` row recording the claim's removal. `questions.md:44` reads "records round 2's probe read". read: the changelog fragment's figures are rule constants and the *Lines before* column at ce448bbe, and the range changed no figure in it. Two wrong figures in the frame are named in the prose above and not graded |
| 🟢 | the stricter reading refuses only more than phase 5a: every hiding shape of rounds 1 and 2 still fails, a finding closed by a 🟢 or ❓ row's word or by a bare `fixed` fails, and the tree's records all read | `skills/code-review/scripts/chain_check.py:95-113`, `:591-618`, `tests/test_chain_check.py:413-446` | confirmed | read: `FINDING_WORDS` is a subset of `CLOSED_WORDS` by construction, and a finding row needs its word in it AND, for `fixed`, a hex word in the cell. A row of any other mark is read exactly as at 704395b1. executed: `test_tmp_r6_probe.py` names a 🟢, ❓ or ⬜ first cell at `open`, an empty, bare or worded first cell at `open`, `deferred` with no home under 🟡 and 🟢, and under the `No.` header. It also names `🔴 1`, a bare `🔴` and `🔴` with U+FE0F or a zero-width space before it, each at `confirmed`, at `❓ out of verified scope`, at a bare `fixed`, at `fixed` with the commit only in Grounds, at `fixed ABC1234`, at `withdrawn` and at `agreed, fixed abc1234`. `fixed accede1`, `fixed on 20261015` and `fixed · fix pass: the line was defaced` pass, which is the hex-word limit `phases/phase-5c.md` states. executed: T24 and the refusal case fail on 704395b1's `chain_check.py` (exit 1, both) and pass at the target. executed: the 40 records hold 83 rows led by 🔴 or 🟡, 67 `fixed`, 15 `deferred`, 1 `answered`, and the corpus case passes. Where the check misses a mark, it is 🟡 1 |
| 🟢 | the sealer's duty left whole: no sentence, pin, `Enforced by:`, eval case or question still names it | `agents/sealer.md:60-65`, `docs/the-review-record.md:70-83`, `templates/sdd-round.md:34-36`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/plan.md:214`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/questions.md:97-100` | confirmed | executed: `git grep` outside the round records and `changelog/0.*` for "Read every 🔴", "another kind's word", "rule-sealer-closed", both removed case names and "answers nothing" finds the duty only in this item's own frame and phase records, each a record of its removal. No eval case was added under `evals/behaviour/sealer/`, which holds the three cases it held. `bin/rules --check` resolves all 403 targets, so no `Enforced by:` names a removed case. read: plan row 9 says three acts and three cases. Q8's row is gone and the paragraph after the table says why. The README, both `hygiene.yml` copies and `docs/the-agent-set.md` say *a row still open*, which stays true. read: Alternative W's verdict still names the row-per-finding design. It sits in the grounds of a rejected design, AA records the later reversal under it, and no agent builds from it |
| 🟢 | the changelog fragment's check and sealer entries are true of the code | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/changelog.md:25-47`, `:55-75` | confirmed | read: "A 🔴 or 🟡 row closes only by the fix pass's three … so a finding closed `confirmed` fails" is `open_findings`. "A refusal names the words for the row's mark" is `records`' lookup in `CLOSES_BY`. "A 🟢 row's word is `confirmed` and a ❓ row's `❓ out of verified scope`" states what the warden writes. The check also closes such a row by any word of `CLOSED_WORDS`. That makes the check looser than this line reads, never stricter, so no user meets a refusal the line does not foretell. The sealer entry now lists the three acts of step 3 and the comparison of step 4, and nothing of the removed duty |
| 🟡 1 | **`fix of a fix`: a finding's mark in bold, italics or a code span is not read as a mark, so `**🔴 1** … confirmed` passes the check the spec says refuses it, and the paragraph saying how the check errs names neither this nor the hex-word reading of `fixed`.** `open_findings` tests `seen[0].strip().startswith(FINDINGS)` on the first cell as written. `verdict_of` takes emphasis off the `Verdict` cell before it reads the word (`EMPHASIS`), so one row's two cells are read by two rules. A row whose first cell is `**🔴 1**`, `` `🟡 2` `` or `_🔴 1_` is read as a row of no mark. It then closes by `confirmed` or `❓ out of verified scope`, which is phase 5b's reading, the trade this phase exists to close. The spec puts the mark "in the first cell alone, where the template puts the mark" (Alternative AB), and these rows carry it there. The refusal for such a row, when it is open, also lists every kind's words rather than the fix pass's three, because `records` matches the same raw cell against `CLOSES_BY`. `docs/the-review-record.md:80-82` is the one place a reader of the check is told how it errs, and it names the Finding-cell case only. The hex-word reading of `fixed` (`fixed accede1` and `fixed on 20261015` pass) is stated only in `phases/phase-5c.md`, which leaves the tree when the item settles. `fix of a fix`: `open_findings`' narrowing and the paragraph's err sentence are units dea5471a and 2fab5421 wrote | `skills/code-review/scripts/chain_check.py:610`, `:617`, `:786-789`, `docs/the-review-record.md:79-82` | deferred the frame | executed: `test_tmp_r6_probe.py` at the target passes `**🔴 1**` and `_🔴 1_` at `confirmed`, `**🟡 2**` at `❓ out of verified scope` and `` `🔴 1` `` at `confirmed` (4 of 30 cases against what the spec says). U+FE0F and a zero-width space are already taken off by `reader.visible`. read: no record in the tree has an emphasised first cell (`git grep` over every `rounds/` file), so nothing in the corpus changes under the fix. executed: with the paste below applied in the clone, the probe has 0 mismatches. `tests/test_chain_check.py`, `test_docs_line_wrap.py`, `test_the_rules_have_one_owner.py`, `test_no_passage_is_pasted_into_a_second_file.py`, `test_one_word_one_meaning.py`, `test_the_pull_request_language_is_the_repositorys.py` and `test_no_real_identifiers.py` pass (exit 0, 216 passed), and `bin/rules --check` exits 0. The two new T24 rows fail on the shipped `open_findings` (exit 1, "Right contains 2 more items, first extra item: ('🔴 8', 'confirmed')"). The clone was restored after · orchestrator: the fourth miss of one fact; the owner chose on 2026-10-16 to design the round record anew from its jobs rather than patch the table |

## Paste-ready fixes

### 🟡 1

`skills/code-review/scripts/chain_check.py:607-618`, the loop of
`open_findings`, and a reader beside it:

```python
    found = []
    for line, seen in rows:
        word = verdict_of(seen, col)
        mark = mark_of(seen[0])
        if mark.startswith(FINDINGS):
            closes = word in FINDING_WORDS and (
                word != FIXED or SHA_RE.search(seen[col]) is not None
            )
        else:
            closes = word in CLOSED_WORDS
        if not closes:
            found.append((line, mark or "the row", word))
    return found, errors


def mark_of(cell):
    """A verdict row's first cell as its mark reads: emphasis off, as
    `verdict_of` takes it off the `Verdict` cell, so `**🔴 1**` and
    `` `🟡 2` `` open with their mark.

    Reads: guess — a cell a person wrote; unknown refused"""
    return EMPHASIS.sub("", cell).strip()
```

`tests/test_chain_check.py`, T24's `named` list and its expected pairs:

```python
        named = [
            "| 🔴 1 | x | `a:1` | confirmed | g |",
            "| 🟡 2 | x | `a:2` | ❓ out of verified scope | g |",
            "| 🔴 3 | x | `a:3` | fixed | g |",
            "| **🔴 8** | x | `a:14` | confirmed | g |",
            "| `🟡 9` | x | `a:15` | ❓ out of verified scope | g |",
        ]
```

```python
        assert [(mark, word) for _line, mark, word in found] == [
            ("🔴 1", "confirmed"),
            ("🟡 2", "out of verified scope"),
            ("🔴 3", "fixed"),
            ("🔴 8", "confirmed"),
            ("🟡 9", "out of verified scope"),
        ]
```

`docs/the-review-record.md:79-82`, the open-row paragraph from "So a 🟢
row":

```markdown
and all of them for any other mark. So a 🟢 row left at `open` fails, and so
does a 🔴 row that reads `confirmed` or a bare `fixed`. The mark is read
through emphasis, as the `Verdict` cell is, so `**🔴 1**` is a finding. It
errs where a row's severity stands only in its Finding cell: that row has no
mark in its first cell, and it closes by any closing word. And `fixed`
closes a finding where any word of seven to forty hex digits stands in the
cell, so `fixed accede1` passes; the sealer's step 3 confirms the commit.
```

## Executed probes

| What was run | Result |
|---|---|
| `git clone --no-local` of the worktree into `<scratchpad>/923-r6/clone`, checked out at 5930b506, with `origin/release/v0.22.0` fetched from the worktree (ce448bbe) | every run below ran there. The worktree was only read, apart from this file |
| `bin/test tests/test_chain_check.py tests/test_the_sealer_guarantees.py tests/test_docs_line_wrap.py tests/test_one_word_one_meaning.py tests/test_the_rules_have_one_owner.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_no_real_identifiers.py tests/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/test_the_pull_request_language_is_the_repositorys.py -q` | exit 0, 259 passed, 6 skipped |
| `bin/rules --check --root <clone>` | exit 0: all 403 `Enforced by:` targets in 60 rule files resolve |
| `chain_check.py --baseline origin/release/v0.22.0 --root <clone>`, before this file | exit 0. The pull request's state is unknown, so nothing was judged as ready. Three lines owed later: round 5's `Target SHA` is behind dea5471a, so a verifying round is owed, and `broad-gate.md` and `guarantee.md` are the sealer's |
| `test_tmp_r6_probe.py` (plain `python3 -I`): `open_findings` over 30 one-row records and a `No.` header record | exit 1, 4 mismatches: the bold, italic and code-span marks of 🟡 1. The other 26 cases and the `No.` header record read as the Grounds of the third 🟢 row say |
| `git checkout 704395b1 -- skills/code-review/scripts/chain_check.py`, then `bin/test tests/test_chain_check.py -q -p no:xdist -k "test_a_finding_row_closes_only_by_a_fix_passs_word or test_the_refusal_names_the_words_that_close_a_row_of_its_mark"` | exit 1, both failed: T24 "Right contains 3 more items, first extra item: ('🔴 1', 'confirmed')", the refusal case with four lines named, no `🔴 1` among them. The file was restored and `git status` was empty |
| 🟡 1's paste applied with `Edit` in the clone; `bin/test tests/test_chain_check.py tests/test_docs_line_wrap.py tests/test_the_rules_have_one_owner.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_one_word_one_meaning.py tests/test_the_pull_request_language_is_the_repositorys.py tests/test_no_real_identifiers.py -q`; the probe; `bin/rules --check` | exit 0, 216 passed; the probe 0 mismatches; rules exit 0 |
| the shipped `chain_check.py` with the two new T24 rows, `bin/test tests/test_chain_check.py -q -p no:xdist -k test_a_finding_row_closes_only_by_a_fix_passs_word` | exit 1, "Right contains 2 more items, first extra item: ('🔴 8', 'confirmed')". The clone was restored after, and `git status` was empty |
| `git ls-tree -r --name-only` filtered to `rounds/round-N.md` at 81e8d785 and 4c552b0b; `ls seal/specs/*/rounds/round-*.md` at the target; `git diff --stat 81e8d785 5930b506` over the round directories | 40 and 40; 75 files, 40 of them `round-N.md`; no record changed in the range |
| a count over the 40 records with `verdict_table` and `verdict_of` | 83 rows led by 🔴 or 🟡: 67 `fixed`, 15 `deferred`, 1 `answered`. 205 🟢 rows: 204 `confirmed`, 34 naming 🔴 or 🟡 in some cell, 21 in the Finding cell |
| `git grep` outside `seal/specs/*/rounds/` and `changelog/0.*` for "Read every 🔴", "another kind's word", "rule-sealer-closed", the two removed case names, "answers nothing", "five documents" and "Q8"; `git grep -E` over every `rounds/` file for a first cell opening with emphasis before 🔴 or 🟡 | as in the Grounds of the second and fourth 🟢 rows and of 🟡 1 |
| this file through `target_of` and `open_findings`; then copied into the clone and staged, `bin/test tests/test_no_real_identifiers.py tests/test_one_word_one_meaning.py tests/test_docs_line_wrap.py tests/test_chain_check.py -q` | `5930b506`; one row open, `(52, '🟡 1', 'open')`, no parse error. exit 1, 96 passed, 1 failed: `TestMain::test_a_record_written_by_the_old_generator_reads` names this file's 🟡 1 row as open, and it stays red until that row reads a fix pass's word |
| the full suite | not run: `unverified`, the sealer's |

Every probe file and the clone sat under `<scratchpad>/923-r6/` and were
deleted with it.

# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — review round 3

| Field | Value |
|---|---|
| Target SHA | adc4acc3, fixes 76f2b569..adc4acc3 |

A verifying round over the reframe after round 2 (41bf39d1), its approval
(93903107) and phase 5a's six commits (fad5be2d..adc4acc3), part A only. Each
of round 2's three findings, all read `deferred the frame`, is answered
below, and each closes. Two new 🟡 rows follow. Neither sits in a unit the
phase-5a commits added or changed, so neither is marked `fix of a fix`. Both
come from the trade the reframe chose: the check now reads every row by its
word alone. 🟡 1: the reader the trade names as its backstop, the sealer, is
not told to look. 🟡 2: the refusal the check prints still gives a fix pass's
three words to every row it names, 🟢 and ❓ rows included. Findings from
reading and from execution are labelled in each Grounds cell, and every
command named there is in `## Probes`. The full suite was not run:
it is `unverified`, and the sealer answers it.

## Findings

### 1. The trade's backstop is not in the sealer's definition, so a 🔴 or 🟡 row that the last round closed `confirmed` reaches the merge with nobody named to catch it

Severity: fix or justify
Location: `agents/sealer.md:60-65`
Verdict: fixed 1f152c5c

`docs/the-review-record.md:76-78`, rewritten in 9aa8b7b5, says a 🔴 row that reads `confirmed` passes the check and that "the next round's warden and the sealer read the record, and that is where such a row is caught". `spec.md:212` says "the sealer's step 4 open every record and read it there". For an earlier round, the next warden is told to answer every earlier finding (`agents/warden.md:205-206`). The last round has no next round, and the sealer is the one reader left. `agents/sealer.md` step 2 reads every record, but step 3 checks only rows closed `fixed <commit>`. Step 4 compares "the warden's last record" with the other parties' accounts, and nothing tells the sealer that a 🔴 or 🟡 row read `confirmed` or `❓ out of verified scope` answers no finding. So the rule the check gave up is held by a sentence in the documentation, and the definition of the agent that sentence names does not carry it. The unit that needs the fix, the sealer's order of work, predates phase 5a, so this is not marked `fix of a fix`. The sentence that relies on it is phase 5a's

read: `agents/sealer.md:56-70`, `agents/warden.md:205-206`, `docs/the-review-record.md:70-79`, `spec.md:212`. executed: `test_tmp_open_rows.py` shows `| 🔴 1 | … | confirmed |` and `| 🟡 2 | … | ❓ out of verified scope |` passing `open_findings`, and the 37 records hold no such row today. So the gap has cost nothing yet. Its reader is the sealer, the next time a warden writes one

`agents/sealer.md`, step 3 (`:60-65`), with one sentence added after the
`fixed <commit>` sentence:

```markdown
3. **A claim against the fact.** Choose a sample of the smith's `executed`
   and `seen red` claims in the phase records, where the evidence is thinnest
   or the outcome rests on it, and re-run each. For every round-record row
   closed `fixed <commit>`, confirm the commit is on the branch and touches
   the row's `Location`. A 🔴 or 🟡 row that reads `confirmed` or
   `❓ out of verified scope` answers no finding, and the check passes it,
   because it reads the word and not the mark: name each one, and unless a
   later round's row answers it, the verdict is `not sound`. For every
   `## Removes` row of `spec.md` and every removal the changelog names,
   confirm nothing of it stands in the tree.
```

`tests/test_the_sealer_guarantees.py`, in `TestDefinition`:

```python
    def test_the_sealer_names_a_finding_closed_by_another_kinds_word(self):
        """The check reads a row's word and not its mark, so a 🔴 or 🟡 row
        closed `confirmed` passes it; `docs/the-review-record.md` names the
        sealer as where such a row is caught, and this holds the sentence
        that tells it to."""
        text = " ".join(SEALER.read_text(encoding="utf-8").split())
        assert (
            "A 🔴 or 🟡 row that reads `confirmed` or `❓ out of verified scope` "
            "answers no finding"
        ) in text
```

`seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:212`,
in the decision cell:

```markdown
A finding closed by another kind's word (`🔴 1 … confirmed`) passes the check; the next round's warden answers every earlier finding, and the sealer's step 3 names every such row and reads it as `not sound` unless a later round answers it.
```

Answer: step 3 now reads every 🔴 and 🟡 row of every record, says the check passes one closed `confirmed` or `❓ out of verified scope` because it reads the word and not the mark, and makes the verdict `not sound` unless a later round's row answers it (four lines, `agents/sealer.md` 8,017 → 8,292 bytes). `spec.md:212` names step 3. `TestDefinition::test_the_sealer_reads_every_red_and_yellow_row_not_only_fixed_ones` was seen red before the sentence (exit 1, the first assertion), green after, and red again when `mutation-check` deleted the `not sound` clause. The changelog fragment's sealer entry says the same

### 2. The refusal gives a fix pass's three words to every row it names, so a 🟢 or ❓ row left open is told to be closed `fixed` or `answered`

Severity: fix or justify
Location: `skills/code-review/scripts/chain_check.py:763-767`
Verdict: fixed 6e9fd4eb

Since fad5be2d, `open_findings` hands `records` every row whose word does not close it, 🟢, ❓ and ⬜ rows included. The message at `chain_check.py:765-766` still reads "`<mark>` reads `open`, which closes no finding: a fix pass writes `fixed <commit>`, `answered` or `deferred <home>`". For `| ❓ | … | pending |` that tells the smith to write `answered` on a question the warden left to someone else, and `answered` passes. For a 🟢 row it names three words the template gives to 🔴 and 🟡 rows (`templates/sdd-round.md:26-35`) and leaves out `confirmed`, the one the row needs. "Closes no finding" also states the rule this phase removed. `phases/phase-5a.md:62-67` kept the message on purpose and left whether a 🟢 row at `open` needs other words to this round: it does. `records` was not changed by phase 5a, so this is not marked `fix of a fix`. What changed is which rows reach the message

read: `records` at `:739-767`, and the pin at `tests/test_chain_check.py:527`. executed: `test_tmp_open_rows.py` shows `open_findings` naming `('🟢', 'open')` and `('❓', 'open')`, which `records` turns into this message. read: no file outside `seal/specs/` quotes the message (`git grep "closes no finding"` finds only `:765` and the pin)

`skills/code-review/scripts/chain_check.py`, `records` (`:763-767`):

```python
        for line, mark, word in still_open:
            problems.append(
                (
                    path,
                    line,
                    f"{mark} reads `{word or 'empty'}`, which does not close it: "
                    "a 🔴 or 🟡 row closes by `fixed <commit>`, `answered` or "
                    "`deferred <home>`, a 🟢 row by `confirmed`, and a ❓ row by "
                    "`❓ out of verified scope`",
                )
            )
```

and its docstring's first line (`:740-741`):

```python
    """[(path, line, problem)] for a work item declared through the review
    chain: no record, a row whose verdict does not close it, a last record
    behind HEAD.
```

`tests/test_chain_check.py:527`, the pin:

```python
        assert "`open`, which does not close it: a 🔴 or 🟡 row closes by" in line
        assert "a 🟢 row by `confirmed`" in line
```

Answer: the refusal reads "`<mark>` reads `<word>`, which does not close it:" and then the words `CLOSES_BY` gives the mark — a fix pass's three for 🔴 and 🟡, `confirmed` for 🟢, `❓ out of verified scope` for ❓, and all three kinds' for any other mark. `open_findings` is unchanged, so the mark still decides nothing. The docstring, the comment over the severities and `docs/the-review-record.md:74-80` say so. The pin at `tests/test_chain_check.py:527` and a new `TestMain::test_the_refusal_names_the_words_that_close_a_row_of_its_mark` (🟡 2, 🟢, ❓ at `pending`, a bare `9`) were red on the old message (exit 1, 2 failed) and green after. `mutation-check` was red for the 🟢 entry, the ❓ entry, the fallback, and the message ignoring the mark; dropping 🟡 from the first entry survived the first case, and 896ea583 makes the 🟡 line end at the fix pass's words, after which it is red

## Confirmations

| What holds | Location | Grounds |
|---|---|---|
| round 2's 🔴 1 is closed: no verdict cell that is not a closing word passes, whatever the row's `#` cell, the header order or a missing `#` column | `skills/code-review/scripts/chain_check.py:576-594` | executed: `test_tmp_open_rows.py` fed 26 rows that should fail through the shipped `open_findings`, and it named all 26. They were 🔴, 🟢, ❓ and ⬜ `#` cells at `open`; a bare number with 🔴 in the Finding cell; an empty `#` cell; `carried`; `deferred`, `deferred —` and `deferred:` with no home; an empty verdict; `Open`, `OPEN`, `**open**` and `` `open` ``; and `open — fixed later`, `still open`, `not fixed`, `unfixed`, `fixedabc`, `fixed?`, `pending`, `✅`, a bare `❓`, `open, but confirmed` and `confirmed?`. A table with no `#` column, one with `#` third, a `No.` header, and a ` verdict ` header in another case with spaces around it each named their open row. A short row and a second table inside `## Verdicts` are refused as errors, which fail a ready pull request too (`records` extends `problems` with them). Of 21 closing cells, all 21 pass, case, emphasis, padding and a leading marker included. The 37 `round-N.md` in the tree read with no named row and no error. read: round 2's ⬜ ground is gone, since `tests/test_chain_check.py:430`'s `⬜ 7 … open` passing case is deleted and T19 names `⬜ 3 … open`. The one shape that still passes an `open` is a header with two `Verdict` columns, where the first is read (`verdict_table`, `header.index`). It predates this branch, and the template's header has one. What round 2 also listed, a 🔴 row read `confirmed` passing, is now the frame's deliberate trade (`spec.md:212`, `plan.md` alternative R, approved). 🟡 1 below is where that trade falls short |
| round 2's 🟡 2 is closed: `.test_durations` lost only the 301 uncollected entries, and the durations case passes | `.test_durations` | executed: `test_tmp_durations.py` compared the file at 2f0b4460 and adc4acc3. Both round-trip through `json.dumps(…, indent=4)`. 7,649 entries become 7,348, and 3,717.2 s become 3,371.9 s. 0 entries were added and 0 changed, the order is kept, and 301 were removed, 345.3 s. `git diff --numstat` shows 0 lines added and 301 deleted, and 445ecd68 is the one commit in the range that touches the file. executed: `pytest --collect-only` in the clone collected 7,574 cases. None of the 301 removed ids is among them, every kept id is, and 226 collected cases have no price. executed: `bin/test tests -q -k test_the_durations_file_prices_the_suite` exit 0, 1 passed, run and not skipped. read: `release_report.py` is untouched, as alternatives S and T decide |
| round 2's 🟡 3 is closed: the docstring counts the four `.py` members the pinned set holds | `tests/test_one_word_one_meaning.py:472` | read: `:472` says four, and the set at `:495-500` holds `seal_stamp.py`, `broad_gate.py`, `session_cost.py` and `tests/test_session_cost.py`. 101343c1 changes that one line. executed: the module among the 157 passed |
| T19 and T20 were red on round 2's `open_findings`, and two of phase 5a's four mutations are red as it says | `tests/test_chain_check.py:382-434` | executed: with 2f0b4460's `chain_check.py` checked out in the clone, `-k TestOpenFindings` exit 1, 2 failed. T19 printed `At index 2 diff: ('4', 'open') != ('🟢', 'open')` and T20 printed `[(11, '🔴 1', 'confirmed'), (12, '🟡 2', 'out of verified scope')] != []`, the lines `phases/phase-5a.md:39` quotes. executed: with `confirmed` dropped from `CLOSED_WORDS` and the `the row` fallback dropped, both cases failed, each on its own break. The other two mutations, ⬜ skipped and a word outside the set skipped, were not re-run; T19's red run above covers both shapes |
| The rewritten sentences are true of the tree, and the fragment's counts are the tree's | `docs/the-review-record.md:70-79`, `templates/sdd-round.md:34-36`, `skills/code-review/scripts/chain_check.py:17-18`, `README.md:182`, `README.ko.md:173`, `.github/workflows/hygiene.yml:169-170`, `templates/hygiene.yml:83`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/changelog.md:30-33`, `:84-97` | read: each sentence against `open_findings` and `verdict_of`. One is stricter than the code. The template's "a word other than these five" fails `withdrawn`, `not a defect` and `agreed, fixed`, and the check passes them. The template instructs the warden, and the old words are there for old records (`chain_check.py:84-88`), so the stricter sentence asks nothing wrong of anyone. `docs/the-review-record.md` names them. executed: `wc -l` gives 1,110, 46, 230, 3,400 and 143; `git diff --numstat ce448bbe adc4acc3 -- tests` gives 3,076 added and 31,996 deleted; there are 143 test modules against 167 at the base. Each matches the fragment. executed: `overview.md`'s S12 figure, 1,144.7 s over the 42 files naming `chain_check` or `broad_gate`, recomputed equal. executed: `bin/rules --check` exit 0, 400 targets in 60 files |
| `phases/phase-5a.md`'s divergences are acceptable, apart from the refusal wording, which is 🟡 2 | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/phases/phase-5a.md:52-90` | read: the class grep still finds `agents/warden.md:154`, `:268`, `skills/code-review/SKILL.md:217`, `:221` and `templates/sdd-round.md:28`. Each says where the warden writes a severity and which rows take an id, and none says what the check reads, so leaving them for part B is right. The released `changelog/0.*.md` files are history. That the durations case prints no count on a pass is true, so the prune script's own line is the right evidence. Leaving `rounds/round-1.md` unedited follows the template ("Earlier round files are never deleted"; the fix pass fills only open rows). The fragment carries no suite seconds (`grep`), so there was nothing to recount there. Two stale figures, which are paperwork and need no fix pass: `phases/phase-5a.md:64` puts the refusal pin at `tests/test_chain_check.py:569`, which is its line at 2f0b4460, and at adc4acc3 it is `:527`. `spec.md:431` and `questions.md:53` say 229 unpriced cases, round 2's count at 7,577 collected, and the phase record's 226 is the current one |
| The reframe in `spec.md`, `plan.md` and `questions.md` matches the code that shipped, apart from the sealer step it names | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:212`, `:354`, `:363`, `:384-387`, `:430-431`; `plan.md:17-23`, `:129-132`, `:162`, `:185-186`, `:205-210` | read: §*Data & interfaces*, S3, S12, the two `## Removes` rows, alternatives R–U and the 5a row against `open_findings`, `verdict_of` and the constants. `severity_of`, `NOT_FINDINGS`, `FINDING_CLOSES` and `ID_COLUMN` are gone (`grep`), and `FINDINGS` stays, read at `tests/test_the_pull_request_language_is_the_repositorys.py:1195`. S3 says the refusal names "the row's `#` cell". The code names the first cell (`seen[0]`), which is the `#` cell in the template's column order, and in a reordered table it is the Finding cell (executed, the `#`-third table above). The row is still named by its line, so the refusal stays loud. `spec.md:212`'s "the sealer's step 4 open every record and read it there" is the coordinate 🟡 1 corrects |

## Not judged

| What | Location | Who answers |
|---|---|---|

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the worktree into `<scratchpad>/923-r3/clone`, at adc4acc3 | every run below ran there, and the worktree was only read |
| `bin/test tests/test_chain_check.py tests/test_one_word_one_meaning.py tests/test_the_pull_request_language_is_the_repositorys.py tests/test_the_release_table_reads_two_trees_and_fails_nothing.py -q -rs` | exit 0, 157 passed, none skipped |
| `test_tmp_open_rows.py`: the shipped `open_findings` over 47 crafted rows in nine table shapes, and over every `round-N.md` in the tree | all 26 rows that should fail are named and all 21 closing rows pass. The no-`#`, `#`-third, `No.` and spaced-header tables name their open row. A short row and a second table are errors. Two `Verdict` columns read the first and pass an `open` in the second. 37 records, 0 named, 0 errors; 0 🔴 or 🟡 rows closed `confirmed` or `out of verified scope` |
| 2f0b4460's `chain_check.py` checked out in the clone, `bin/test tests/test_chain_check.py -q -k TestOpenFindings -p no:xdist` | exit 1, 2 failed, with the two diffs `phases/phase-5a.md:39` quotes. The file was restored to adc4acc3 after |
| `confirmed` dropped from `CLOSED_WORDS` and the `the row` fallback dropped, same command | exit 1, 2 failed: T19 `('', 'open') != ('the row', 'open')`, T20 `[(11, '🔴 1', 'confirmed')] != []`. The file was restored after, and `git status` was clean |
| `.venv/bin/python -m pytest tests --collect-only -q -p no:xdist` | exit 0, 7,574 collected |
| `test_tmp_durations.py`: `.test_durations` at 2f0b4460 and adc4acc3, against the collection | both round-trip; 7,649 → 7,348 entries, 3,717.2 → 3,371.9 s; 0 added, 0 changed, order kept, 301 removed (345.3 s); 0 removed ids collected, 0 kept ids uncollected, 226 collected unpriced; numstat 0 added, 301 deleted; one commit, 445ecd68 |
| `bin/test tests -q -rs -k test_the_durations_file_prices_the_suite` | exit 0, 1 passed |
| the 42 files naming `chain_check` or `broad_gate`, summed from `.test_durations` | 1,144.7 s |
| `wc -l` at adc4acc3 and `git diff --numstat ce448bbe adc4acc3 -- tests` | 1,110 · 46 · 230 · 3,400 · 143 lines; 3,076 added, 31,996 deleted; 143 test modules against 167 |
| `bin/test` over `test_ci_gives_the_checks_what_they_need.py`, `test_docs_line_wrap.py`, `test_no_passage_is_pasted_into_a_second_file.py`, `test_the_sealer_guarantees.py`, `test_the_rules_have_one_owner.py`, `test_a_document_that_names_a_script_says_how_to_reach_it.py`, `test_release_hygiene.py`, `test_no_real_identifiers.py` (`-q -rs`) | exit 0, 177 passed, 6 skipped: "no shipped document names it, so nobody goes looking" |
| `bin/rules --check --root <worktree>` | exit 0: all 400 `Enforced by:` targets in 60 rule files resolve |
| the full suite | not run: `unverified`, the sealer's |

Every probe file and the clone sat under `<scratchpad>/923-r3/` and were
deleted with it.

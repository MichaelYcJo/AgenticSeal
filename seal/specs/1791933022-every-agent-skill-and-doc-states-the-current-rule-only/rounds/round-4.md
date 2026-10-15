# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — review round 4

| Field | Value |
|---|---|
| Target SHA | 2aa66591, fixes d52605db..2aa66591 |

Extended past round 3: round 3 found 2, round 2 found 3, and none is a fix of a fix.

A verifying round over round 3's fix pass, part A only. Its target is the
diff of the five commits after round 3's record (1f152c5c, 6e9fd4eb,
896ea583, 5ea6506c, 2aa66591). Both of round 3's findings are closed in the
unit they named. Two new 🟡 rows follow. 🟡 1: the sealer's new duty reached
its definition, but the guarantee template and the review-record document,
which list what the sealer's step 3 does, still list the old three acts. It
is not marked `fix of a fix`, because neither unit was changed by these
commits. 🟡 2: the fix pass rewrote the stale count of unpriced cases in
`spec.md` and `questions.md` to 226, after its own two commits had added two
more unpriced cases. The count is 228 at the target. It is marked `fix of a
fix`, because 5ea6506c wrote both sentences. One ❓ row asks whether the
sealer's new sentence needs a behaviour eval. Findings from reading and from
execution are labelled in each Grounds cell, and every command named there is
in `## Executed probes`. The full suite was not run: it is `unverified`, and
the sealer answers it.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 3's 🟡 1 is closed: the sealer's definition now tells it to read every 🔴 and 🟡 row and to read one closed by another kind's word as `not sound` | `agents/sealer.md:60-69` | confirmed | read: step 3's new sentence is a duty the sealer can carry out with what it reads. Step 2 already has it read every `rounds/round-N.md`, and a 🔴 or 🟡 mark is visible to a reader in any column order. It does not contradict the other steps. Step 1's exit 1 still ends the audit before step 3, step 4 compares only the last record and does not narrow step 3's "every record", and the `not sound` it produces is the shape the rule *A verdict names what it rests on* asks for. It does not contradict *You do not re-judge the design*: it reads a record and judges no code. The one inconsistency is with the guarantee template and `docs/the-review-record.md` §*The guarantee*, which is 🟡 1 below. executed: `TestDefinition::test_the_sealer_reads_every_red_and_yellow_row_not_only_fixed_ones` fails on d52605db's `agents/sealer.md` (exit 1, on the first assertion) and passes at 2aa66591. read: the pin is a presence pin on three clauses: the reading of every row, why the check passes such a row, and the `not sound` outcome. It is the same kind of pin as the module's other `TestDefinition` cases. A part-B rewrite that drops or rewords any of the three clauses fails it, so the duty cannot leave the definition silently, and that is the pin's job. executed: one clause is not held. With "Name each one" deleted, the case still passes (exit 0). The *A verdict names what it rests on* rule already makes a `not sound` verdict name its row, so what is lost is only the naming of a row a later round answered, which is 🟡 1's subject. Whether a sealer acts on the sentence is not something a wording pin can show, and that is the ❓ row below. executed: `agents/sealer.md` is 8,017 bytes at d52605db and 8,292 at 2aa66591, as the fix pass says |
| 🟢 | round 3's 🟡 2 is closed: the refusal names the words that close a row of its mark, and the mark picks the message only | `skills/code-review/scripts/chain_check.py:81-92`, `:774-786` | confirmed | read: `closes` is computed inside the loop over `still_open` and used only in the f-string, and `open_findings` is unchanged. executed: `test_tmp_r4_marks.py` wrote one record of 120 rows: ten first cells (`🔴 1`, `🟡 2`, `🟢`, `❓`, `⬜ 3`, `9`, empty, `**🔴 1**`, `❓` with U+FE0F, `carried`) against six closing words and six that do not close (`open`, `pending`, empty, a bare `deferred`, `✅`, `still open`). Through the shipped `main` it named exactly the 60 rows with a non-closing word and exit 1. A record of the 60 closing rows, sealed at HEAD, exit 0. With `CLOSES_BY` emptied, the same 60 rows were named, so the mark decides nothing. Every named line ends with the words for its mark. 🔴 and 🟡 get the fix pass's three, 🟢 gets `confirmed`, ❓ (with or without U+FE0F) gets `❓ out of verified scope`, and `⬜ 3`, `9`, `carried`, an empty cell (named `the row`) and `**🔴 1**` get every kind's words. An empty verdict reads `` reads `empty` ``. The bold `**🔴 1**` falls to the fallback because the lookup does not strip emphasis the way `verdict_of` does, but its line still lists the fix pass's words, and `docs/the-review-record.md:76-78` says "all of them for any other mark", so nothing is told a wrong word |
| 🟢 | 896ea583's `endswith` holds the 🟡 entry that the `in` form let go | `tests/test_chain_check.py:565-567` | confirmed | executed: with `CLOSES_BY`'s first entry narrowed from `FINDINGS` to `(BLOCKING,)`, 6e9fd4eb's version of the case passes (exit 0, 1 passed). 2aa66591's version fails at `:565` on `yellow.endswith` (exit 1). The `:527` pin passes under that break, as it should, because it names a 🔴 row. read: the 🟢 and ❓ lines are also held by `endswith`, so mapping either of them to the fallback fails too. Both files were restored after the run, and `git status` showed only the probe |
| 🟢 | `docs/the-review-record.md:70-81` states what the check does, and the changelog fragment's new sentences and recounted figures are the tree's | `docs/the-review-record.md:70-81`; `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/changelog.md:32-34`, `:62-65`, `:93-103` | confirmed | executed: the matrix above is the paragraph's claim, row for row, including "all of them for any other mark". read: "changes nothing. It names the row in the refusal and picks the words" puts two sentences side by side that a quick reader can take as contradicting each other. The first means that the mark decides no row, and that is true, so this is a sentence that reads tightly and not a finding. The same holds for `spec.md:212` and `chain_check.py:596`, which still say the cell "only names the row". What each asserts, that the cell decides nothing, holds. read: the fragment's refusal sentence leaves out the fallback for other marks, but nothing in it is false. Its sealer sentence matches step 3. executed: `wc -l` gives 1,128 for `chain_check.py`, 3,400 for `broad_gate.py`, 46 for `templates/sdd-round.md`, 232 for `docs/the-review-record.md` and 147 for `agents/sealer.md`. `git diff --numstat ce448bbe 2aa66591 -- tests` gives 3,135 added and 31,996 deleted. `git ls-tree` gives 167 test modules at ce448bbe and 143 at 2aa66591. Each matches the fragment |
| 🟢 | `phases/phase-5a.md:64`'s corrected coordinate is right | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/phases/phase-5a.md:64` | confirmed | read: at 2aa66591 the pin's `assert (` stands at `tests/test_chain_check.py:527` and its string at `:528`. The paragraph around it still says the old message "is left", which is what phase 5a did, and a phase record keeps that. The other two corrected figures are 🟡 2 |
| 🟡 1 | **The sealer's new step-3 duty is in its definition only. The guarantee template and the review-record document still list the old three acts, so a finding the sealer names has no row to go in.** 1f152c5c added to `agents/sealer.md` step 3: read every 🔴 and 🟡 row, and "name each one". Step 5 then says to write `guarantee.md` "every row of its two tables filled", and the template's comment over `## Claims re-run` says what those rows are: "One row per claim sampled, per `fixed <commit>` verdict and per removal named." That is step 3's old three acts, with no row for the fourth. A 🔴 row closed `confirmed` that a later round answered leaves the verdict `sound`, and the sealer is told to name it with nowhere in the file to do so. `docs/the-review-record.md` §*The guarantee* (`:117-125`) lists the same three acts as what the sealer checks, while `:79-80` of the same document says the sealer is where such a row is caught. The fix pass carried the duty to the changelog fragment's sealer entry and to `spec.md:212`, so it knew the duty had more than one home, and it missed these two. Neither unit was changed by d52605db..2aa66591, so this is not marked `fix of a fix`. The sentence that needs them is 1f152c5c's | `templates/sdd-guarantee.md:15-16`, `docs/the-review-record.md:117-125` | deferred the frame | read: `agents/sealer.md:60-69`, `:75-76`; `templates/sdd-guarantee.md:13-20`; `docs/the-review-record.md:70-81`, `:117-125`. read: `git grep "fixed <commit>"` outside `seal/specs/` finds the sealer's duties listed in exactly these three places and the definition. executed: deleting "Name each one" from step 3 leaves the definition's pin green, so nothing holds the naming either · orchestrator: round 4 marked a fix of a fix, so no fix pass runs and the work item goes back to its framer |
| 🟡 2 | **`fix of a fix`: the fix pass corrected the count of unpriced cases to 226 after its own commits had made it 228, so a `## Removes` row the sealer reads against the tree is false again.** 5ea6506c changed `spec.md:431` and `questions.md:53` from 229 to 226. It came after 1f152c5c and 6e9fd4eb, which add `TestDefinition::test_the_sealer_reads_every_red_and_yellow_row_not_only_fixed_ones` and `TestMain::test_the_refusal_names_the_words_that_close_a_row_of_its_mark`, and neither case has a price in `.test_durations`. At 2aa66591, 7,576 cases are collected and 228 have no price. The sealer's step 3 reads every `## Removes` row of `spec.md` against the tree, and its step 4 names the party the tree contradicts. So a sealer that counts writes `not sound` on a sentence this branch wrote. The cause is the stored count itself, not the arithmetic. Every case a later commit adds moves it, and `CLAUDE.md` §*The rule a mechanism is kept against* says "Nothing is kept beside the tree to stay in step with it, such as a stored count". Round 3 called this class paperwork that needs no fix pass. That held for a figure nobody touched. The fix pass did touch it, and the share the sentence also states (3 %) is the part that stays true. Marked `fix of a fix`: both sentences are units 5ea6506c changed | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:431`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/questions.md:53` | deferred the frame | executed: `unpriced.py` ran `pytest --collect-only` in the clone (the probe module ignored) against `.test_durations`. Exit 0, 7,576 collected, 228 unpriced (3.01 %), and the two new cases are among the 228. read: `git log` puts 5ea6506c after 1f152c5c and 6e9fd4eb. read: `phases/phase-5a.md:72`'s 226 is that phase's own count at its own commit, which is history, and is left · orchestrator: round 4 marked a fix of a fix, so no fix pass runs and the work item goes back to its framer |
| ❓ | Whether a sealer acts on step 3's new sentence: no behaviour eval puts a 🔴 or 🟡 row closed `confirmed` in front of one | `agents/sealer.md:64-67`, `evals/behaviour/sealer/`, `docs/the-review-record.md:81` | ❓ out of verified scope | read: `evals/behaviour/sealer/` holds `rule-sealer-false-red`, `rule-sealer-sound` and `rule-sealer-untrue-body`, and none of them carries such a row. `docs/the-review-record.md:81`'s `Enforced by:` names `TestOpenFindings` and `TestMain`, which prove the check's half of the paragraph ("a 🔴 row that reads `confirmed` passes the check") and not the sealer's half ("that is where such a row is caught"). `CLAUDE.md` says a rule's proof is "the test or behaviour eval its `Enforced by:` names". The wording pin shows the sentence is there, not that a sealer reads it as told. Running an eval spends the proof's run budget, which `questions.md` records as the owner's, so the owner answers whether one is owed here or in part B |

## Paste-ready fixes

### 🟡 1

`templates/sdd-guarantee.md:15-16`, the text of the comment over
`## Claims re-run` (the comment markers stay as they are):

```markdown
One row per claim sampled, per `fixed <commit>` verdict, per 🔴 or 🟡 row
closed `confirmed` or `❓ out of verified scope`, and per removal named.
```

`docs/the-review-record.md:117-125`:

```markdown
**It checks a claim against the fact, and the parties against each other.**
It re-runs a sample of the smith's `executed` and `seen red` claims, chosen
where the evidence is thinnest or the outcome rests on it; confirms each
`fixed <commit>` commit is on the branch and touches its `Location`; names
every 🔴 or 🟡 row closed `confirmed` or `❓ out of verified scope`, which is
`not sound` unless a later round answers it; and confirms nothing removed in
this release stands in the tree. It reads the spec, the build, the warden's
last record, the changelog fragment and the pull request body as one story,
and where two disagree it names the one the issue and the tree contradict. It
does not re-judge the design or the code's quality.
```

`tests/test_the_sealer_guarantees.py`, a new case in `TestTemplate`:

```python
    def test_the_template_has_a_row_for_a_finding_closed_by_another_kinds_word(
        self,
    ):
        """The sealer's step 3 names every 🔴 or 🟡 row closed by a 🟢 or ❓
        row's word; the template's claims table is where it names one."""
        text = " ".join(TEMPLATE.read_text(encoding="utf-8").split())
        assert (
            "per 🔴 or 🟡 row closed `confirmed` or `❓ out of verified scope`"
        ) in text
```

### 🟡 2

`seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:431`,
the last sentence of the row's third cell:

```markdown
The collected cases with no price (about 3 %, under `STALE_SHARE`) are priced by the next refresh from a `tests` run, which `CONTRIBUTING.md` §*Running the checks* owns |
```

`seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/questions.md:52-53`:

```markdown
  (`gh run list`, `gh pr list` on 2026-10-15: none), so the refresh that
  prices the unpriced cases waits for the pull request's first run.
```

## Executed probes

| What was run | Result |
|---|---|
| `git clone --no-local` of the worktree into `<scratchpad>/923-r4/clone`, checked out at 2aa66591 | every run below ran there, and the worktree was only read, apart from this file |
| `bin/test tests/test_chain_check.py tests/test_the_sealer_guarantees.py -q -rs` | exit 0, 44 passed |
| `bin/test tests/test_tmp_r4_marks.py -q -s -p no:xdist`: the 120-row matrix, the 60 closing rows sealed, and the matrix with `CLOSES_BY` emptied | exit 0, 3 passed. 60 of 120 rows named, exactly those at a non-closing word, each ending with its mark's words. The 60 closing rows exit 0. With `CLOSES_BY` emptied, the same 60 rows are named, exit 1 |
| `CLOSES_BY`'s first entry narrowed to `(BLOCKING,)`, then `bin/test tests/test_chain_check.py -q -p no:xdist -k "test_the_refusal_names_the_words_that_close_a_row_of_its_mark or test_an_open_verdict_fails_a_ready_pull_request"` | exit 1, 1 failed (`:565`, `yellow.endswith`), 1 passed (the `:527` pin) |
| the same break, with `tests/test_chain_check.py` at 6e9fd4eb, `-k test_the_refusal_names_the_words_that_close_a_row_of_its_mark` | exit 0, 1 passed: the `in` form let the break go. The file was restored to 2aa66591 after |
| "Name each one" deleted from `agents/sealer.md` step 3, `bin/test tests/test_the_sealer_guarantees.py -q -p no:xdist -k test_the_sealer_reads_every_red_and_yellow_row_not_only_fixed_ones` | exit 0, 1 passed: the clause is not held. The file was restored after |
| `agents/sealer.md` at d52605db, the same case | exit 1, 1 failed on `'Read every 🔴 and 🟡 row of every record' in …`. The file was restored to 2aa66591 after, and `git status` showed only the probe |
| `unpriced.py`: `.venv/bin/python -m pytest tests --collect-only -q -p no:xdist --ignore=tests/test_tmp_r4_marks.py`, its ids against `.test_durations` | exit 0. 7,576 collected, 228 unpriced (3.01 %), the two new cases among them |
| `wc -l`, `wc -c`, `git diff --numstat ce448bbe 2aa66591 -- tests` and `git ls-tree` in the clone | 1,128 · 3,400 · 46 · 232 · 147 lines; `agents/sealer.md` 8,017 → 8,292 bytes; 3,135 added, 31,996 deleted; 167 → 143 test modules |
| `bin/test tests/test_docs_line_wrap.py tests/test_no_real_identifiers.py tests/test_one_word_one_meaning.py tests/test_the_rules_have_one_owner.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_a_document_that_names_a_script_says_how_to_reach_it.py -q -rs` | exit 0, 121 passed, 6 skipped: "no shipped document names it, so nobody goes looking" |
| `bin/rules --check --root <worktree>` | exit 0: all 400 `Enforced by:` targets in 60 rule files resolve |
| the full suite | not run: `unverified`, the sealer's |

Every probe file and the clone sat under `<scratchpad>/923-r4/` and were
deleted with it.

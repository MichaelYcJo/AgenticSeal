# Review round 4: 1793726048-the-stop-judgment-holds-against-later-rows

```seal
target: ff99adcd9, fixes c307135a2..ff99adcd9
```

This verifying round read the diff of the last fixes, `c307135a2..ff99adcd9`, in a `git clone --no-local` of the main clone at `ff99adcd9`. The clone was made in the round's scratch directory and removed before hand-back. The diff holds three commits. `62141ac4e` is the orchestrator's row 5 of `frame/plan.md` *Judgments of the run* and its fold of `frame/design.md` *Scope* item 3's first point. `67cac0f00` is the fix pass for round 3's finding 1. `ff99adcd9` is round 3's close block. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` holds no `Record language` row, so the record is English. The diff adds no test, so *Each new test is read against its group* had nothing to read. The orchestrator named this round as the run's last (row 5).

Carried from rounds 1 to 3, not re-established: the location of #1216's record at tag `v0.28.0`, the base `5005355d8`, and that `in_corpus` is the helper whose test round 5 of #1216 wrote its finding on. Re-derived this round: every verdict below; the reading of #1216's *Scope* item 1 and G8 that S5 rests on; and #1216's acceptance row S5, which no earlier round of this work weighed. Round 1's finding 1 stays `deferred frame/design.md ## Rule changes, the orchestrator's fold`, which round 2 confirmed; this round does not write it up again.

This round opens one finding, a `should`, on a `regression:` line. It stands outside the fix diff, in the changelog fragment's second process row, which round 1's fix pass rewrote. It came up while listing every statement of the definition the fix kept. The fix to it is confined to the work item's records.

## Findings

### 1. The changelog's second process row states the definition without "of a rule the diff changes", so it tells the next framer that any `check:` line's fact counts

```seal
severity: should
location: `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/changelog.md:11`
evidence: read `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/changelog.md:4`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/changelog.md:11`, `skills/code-review/SKILL.md:132-136`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:42`, `docs/layout/the-record-layout.md:51-62`
regression: round-1#4
```

The unit is the *Change* cell of the second row under `### Process changes` in the work item's `changelog.md` (`:11`). The frame's *Scope* item 6 asks for one process row for items 3 and 4, and item 3's first point (`frame/design.md:42`) defines the case by "a `check:` line of a rule the diff changes". The fix for round 1's finding 4 at `89480ded9` rewrote this cell to carry the definition and wrote "a `check:` line states", without the qualifier. The defect came from the fix pass's own wording: round 1's paste-ready text covered the bullet alone, and its note on where it stopped named `agents/proofer.md` and the frame, not the changelog. Executed: `git log --follow` on the file lists `4551db29` (phase 1, whose row stated no definition) and `89480ded9`, and `git show` of each shows the qualifier first missing at `89480ded9`.

Why it matters: the row tells its reader that a case asserting a fact of any `check:` line holds a fact the frame states. The bullet says only a `check:` line of a rule the diff changes counts (`skills/code-review/SKILL.md:134-135`). Under the row's wording, a case that asserts a fact of an unchanged rule's `check:` line is weighed as an ordinary case, while the bullet makes it one whose gap is no `should` by default. Round 3's finding 1 named the same omission in `bffc022d6`'s sentence as part of its grounds. The fragment's own bullet at `:4` keeps the qualifier, so the fragment states the rule two ways. A process row is read by an agent: `docs/layout/the-record-layout.md:57` says "the next framer reads what the way of working became and why", and `:59-62` say the release note lifts every row into its *Process changes* table. So this is a wrong sentence an agent reads, which the bullet opening "A finding is a defect." makes a `should`.

Claimed (round 3's grounds): "The changelog's bullet and its second *Process changes* row state the definition alone". Read: both state no example. The row still drops the qualifier, which round 3 did not compare.

The statements of the definition, listed by taking apart each file that states it: the bullet (`skills/code-review/SKILL.md:132-136`), *Scope* item 3's first point (`frame/design.md:42`), the changelog's bullet (`changelog.md:4`) and its second process row (`:11`). `agents/proofer.md:139-141` cites the bullet and states no definition. `trail/phases/phase-1.md:115-119` records the build's reading at `72c77856e` and stays true as a record of that act. Only `:11` lacks the qualifier, so the fix reaches every statement. In the row's *Change* cell, the clause before the first semicolon becomes:

```markdown
`skills/code-review/SKILL.md` *The record*: a case whose assertions hold no behaviour a *Scope* item, an acceptance row or a `check:` line of a rule the diff changes states, a fact only a *Grounding* row states not counting, holds no fact the frame states and is weighed by what the release ships without the fix, and a gap in it is no `should` by default
```

The rest of the row stands as written.

```seal
verdict: fixed cdaf42d8b
answer: The finding holds. The second process row of `changelog.md` now reads "a `check:` line of a rule the diff changes", as `:4`, the bullet and `frame/design.md` *Scope* item 3 do. The orchestrator made the fix after judging the run excessive at this round (`frame/plan.md` *Judgments of the run* row 6): the fix is confined to the work item's records, so the sealer reads it and no round follows.
```

## Confirmations

```seal
confirms: round-3#1
```
What holds: the bullet of `skills/code-review/SKILL.md` *The record* now states the definition and names no kind of case. Executed: `git diff --word-diff=plain c307135a2 HEAD -- skills/code-review/SKILL.md` shows the helper-test sentence removed and every other word of the bullet unchanged. The rewrap moved only line breaks, and no line from `:132` to `:148` is wider than 75 columns. Read: *Scope* item 3's first point (`frame/design.md:42`), folded at `62141ac4e`, states the same definition and the same *Grounding* exclusion, and it says the bullet names no kind of case. Executed: `git grep` for "helper the work moved", "what the helper does", "wrote beside its", "test of a helper" and "such as a test" over the whole tree finds no rule that still states the helper condition. The changelog's line 4 keeps "a test of a helper that moved with its body" as the history of #1216, and `frame/plan.md:56` keeps the frame's old example as the record of row 2. The rest are this work's round records.

S5 holds under the bullet as it now stands. Read at `v0.28.0`: #1216's *Scope* item 1 (`frame/design.md:43` there) names `in_corpus(rel)` as "the selection rule of G8 as a predicate on a repository path" and moves it as it stands. The membership and exclusion that `Test_in_corpus` asserts appear only in G8's text (`:14` there): the four directories, the three top files, and no `*.ko.md`. The bullet's "A fact that only a *Grounding* row states does not count" turns on where a fact is stated. Item 1 points at G8 and states no membership, so the fix pass's reading in its close is the one the bullet gives. Read, and not weighed by any earlier round: #1216's acceptance row S5 (`frame/design.md:70` there) states that `chain-check` prints nothing for a `to` landing in a `*.ko.md` file. That row describes `chain-check`'s output, and #1216's round 5 names the case in `tests/skills/test_chain_check.py` as the one that pins it (`trail/rounds/round-5.md:25` and `:53` there). `Test_in_corpus`'s assertions hold the predicate's results, not `chain-check`'s output. So its case holds no behaviour that an acceptance row states, and round 5's finding, on a parameter that pins nothing and a `TOP_FILES` guard no case pins, is no `should`.

```seal
confirms: none
```
What matched: the orchestrator's route in row 5 (`frame/plan.md:58`), labelled for this round to weigh. Read: the third row of `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame* sends a unit's second regression to the framer, unless a judgment row writes why the frame holds and the fix alone was wrong. Row 5 writes it. Before row 4's fold, the frame defined the case by what its assertions hold and gave the helper test as an example under "such as". `89480ded9` made the example a rule, `bffc022d6` gave it a second condition, and the fold `a4be575e4` copied that condition into the frame. The paragraph opening **Where the signal is one mechanism whose edges each fix pass chased** (`orchestration.md:187-203`) says that the fix states the rule and lists no kinds where the inputs are open, and that the deciding row names the next verifying round as the run's last. The fix and row 5 do both. The fold at `62141ac4e` returns the frame's first point to that definition, and the bullet matches it. The weighing of #1216's S5 above found no further edge that this route left standing.

```seal
confirms: none
```
What matched: the crafter's executed claims. Executed in the clone at `ff99adcd9`, with `bin/test`, in one command: `tests/behaviour/test_docs_line_wrap.py`, `tests/text/test_the_rules_have_one_owner.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py` and `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, with `tests/text/test_the_record_is_written_in_words.py` added, exited 0 with 130 passed. Executed: `chain_check.py --baseline 5005355d8 --root . --worktree` in the clone exited 0. It printed no rule-change refusal, no pin notice and no copy notice. Its lines name the verifying round owed for round 3's finding 1 and for `67cac0f00`, which this record answers, and they name the gate record and guarantee as not yet written. So no notice at a line of `frame/design.md` was left to weigh. Executed: S8's `git diff --stat 5005355d8...HEAD -- ':!seal/'` lists `agents/proofer.md`, `skills/code-review/SKILL.md`, `skills/code-review/orchestration.md` and `skills/implement/orchestration.md`, and nothing else.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the full suite passes at `ff99adcd9`. This round ran five modules, and the suite stays `unverified` | the repository's `Broad gate` row | the orchestrator, at the broad run |
| Where finding 1 goes. It is a `should`, and row 5 names this round as the run's last. Its fix is confined to the work item's records, which the sealer reads | `frame/plan.md` *Judgments of the run* | the orchestrator |
| Q1: whether a fix that changes no assertion owes no verifying round. The build stands on the default **No**, carried from rounds 1 to 3 | `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/questions.md` | the repository owner |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_docs_line_wrap.py tests/text/test_the_rules_have_one_owner.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_the_record_is_written_in_words.py -q`, in the clone | exit 0, 130 passed |
| `python3 skills/code-review/scripts/chain_check.py --baseline 5005355d8 --root . --worktree`, in the clone at `ff99adcd9` | exit 0; no rule-change refusal, pin notice or copy notice; it names the verifying round owed for round 3's finding 1 and `67cac0f00`, and no gate record or guarantee yet |
| `git diff --word-diff=plain c307135a2 HEAD -- skills/code-review/SKILL.md`, and the widths of lines 132 to 148 | only the helper-test sentence removed; widest line 75 columns |
| `git grep -n -i -e 'helper the work moved' -e 'what the helper does' -e 'wrote beside its' -e 'test of a helper' -e 'such as a test' -- .` | no rule states the helper condition; the hits are the changelog's history line, `frame/plan.md:56` and this work's round records |
| `git log --oneline --follow` on `changelog.md`, and `git show` of line 11 at each commit it lists | `4551db29` states no definition; `89480ded9` states it without "of a rule the diff changes" |
| `git show v0.28.0:seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/design.md`, and that work item's `trail/rounds/round-5.md`, searched for `corpus`, `ko.md` and the acceptance table | *Scope* item 1 at `:43` points at G8; G8 at `:14` alone states the corpus; S5 at `:70` states `chain-check`'s output for a `to` into a `*.ko.md` file, which round 5 places in `tests/skills/test_chain_check.py` |
| `git diff --stat 5005355d8...HEAD -- ':!seal/'`, in the clone | four files, as S8 names |

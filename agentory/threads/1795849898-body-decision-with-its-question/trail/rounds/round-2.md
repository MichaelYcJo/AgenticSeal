# Review round 2: 1795849898-body-decision-with-its-question

```iadd
target: 2cff328e, fixes 205e2eb2..2cff328e
```

A verifying round over the commits after round 1's record: `7a5135eb`, the orchestrator's and the framer's repairs and the fold of *Scope* item 6; `46f97246`, the fix pass; `ec0ac7af` and `cf2fb730`, the closing memo's row and round 1's close blocks; and `2cff328e`, the prefix row's `Grounds` cell and its quote in `pr.md`. The range holds no merge of the base. The code reviewed is the fix diff, read in a `git clone --no-local` of the branch at `2cff328e` under the round's scratch directory, with a second clone at `596c79a6` for the base. The records read whole at the target are `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/rounds/round-1.md`. No `pr.<lang>.md` stands, because `agentory/config.json` names English for both language keys. No `agentory/parity.json` stands, and `agentory/config.json` has no `Pact` key.

Carried from round 1 and not established again: the builders that feed `_unfolded`'s `copied` (design G16, read against `pr_body.py:777-891` for their names alone), the phase record's mutation runs, and round 1's confirmations of *Scope* items 2 and 3. Every verdict below is this round's own.

## Findings

### 1. The fold says a round record and `trail/gate.md` could carry an unclosed fence into the body before this work, and the base already refused both

```iadd
severity: should
location: `agentory/threads/1795849898-body-decision-with-its-question/frame/design.md:44`, `agentory/threads/1795849898-body-decision-with-its-question/frame/plan.md:63`, `agentory/threads/1795849898-body-decision-with-its-question/changelog.md:4`
evidence: executed `bin/test tests/skills/test_tmp_round2_fence_probe.py -q -s -p no:xdist` in the round's clone at 2cff328e and in its clone at 596c79a6; read `skills/code-review/scripts/pr_body.py:103-108`, `skills/code-review/scripts/pr_body.py:807-851`, `skills/code-review/scripts/chain_check.py:720-760`, `lib/fields.py:229-230`, `lib/fields.py:351`; executed `git grep -n -F "could carry such a line" 2cff328e`, `git grep -n -F "every copied record" 2cff328e`, `git grep -n -F "every record the body copies" 2cff328e` and `git grep -n -F "trail/gate.md" 2cff328e`, each over the work item's directory without `trail/rounds`
regression: round-1#1
```

Why it matters: the unit is the set of record sentences that state what *Scope* item 6's refusal reaches. The framer's fold wrote them at `7a5135eb`, and the fix pass wrote the changelog's at `46f97246`. Round 1's finding 1 left one question open: it "did not re-derive whether that reader already refuses an unclosed fence for those two copies", the round records and `trail/gate.md`. The fold answered it without a check. Design *Scope* item 6 (`design.md:44`) says "All of those but the questions copy could carry such a line before this work", and the list it closes names the round records and `trail/gate.md`. The new *Operational impact* bullet (`plan.md:63`) names "a round record, `trail/gate.md`" among the records whose line "is now refused at that line, where before its body was written with the fold's end inside a code block". The base contradicts both sentences for those two records. The module docstring says round records are read through `chain_check.py#round_read` and `trail/gate.md` through `lib/fields.py`, and "a record either refuses is refused here with its sentence" (`pr_body.py:103-108`). `lib/fields.py:351` refuses each unclosed fence with `UNCLOSED`, "a fence opened here never closes, so every line after it is hidden from the reader" (`lib/fields.py:229-230`). The probe composed the same five shapes against both trees. At `596c79a6`, a round record with an unclosed fence in its prose was refused at `trail/rounds/round-1.md` line 28 with that sentence, and so was `trail/gate.md` at line 11. The `gaps.md`, `## Phases` and changelog shapes composed, with the fold's end after the opener. At `2cff328e` the first two give the same `lib/fields.py` refusal, and the new branch of `_unfolded` never runs for them. The other three are refused by the new branch. So the code is right, and the class the frame says the fix closed is narrower than the records state. Three of the frame's records fit what was actually open: plan A15 (`plan.md:34`), which names "The changelog above the fold, the `## Phases` copy and both `gaps.md` sections", design G16, and design S9. `changelog.md:4` tells the release note's reader that such a line "is now refused at that line, in every record the body copies", but two of those records were refused before. The inspector reads *Scope* and *Operational impact* against the diff, so this is a wrong sentence an agent acts on.

The four searches printed `design.md:16` (G16, which lists the copied records and claims nothing of the base), `design.md:44`, `plan.md:9`, `plan.md:32` (A13, the chosen approach, true of the code), `plan.md:34`, `plan.md:63` and `changelog.md:4`. The fix covers `design.md:44`, `plan.md:63` and `changelog.md:4` and leaves the rest as they read. The prefix row's `Grounds` cell (`plan.md:72`) and its quote (`pr.md:4`) say `agentic pr-body` "now refuses a copied record that opens a fence it never closes" without naming which records. That stays true of the four records it now refuses, so this round leaves them. A search on these words is a sample under contract rules 12 and 19, since a statement in other words escapes it.

In `frame/design.md` *Scope* item 6, the sentence "All of those but the questions copy could carry such a line before this work." becomes:

```markdown
Of those, `changelog.md`, the `## Phases` section and both sections of `gaps.md` could carry such a line into the body before this work. A round record and `trail/gate.md` could not: `chain_check.py#round_read` and `lib/fields.py#read` refuse a fence that never closes with `lib/fields.py#UNCLOSED`, and `agentic pr-body` refuses the record with that sentence before `_unfolded` reads its lines, after this work as before it.
```

In `frame/plan.md` *Operational impact*, the last bullet becomes:

```markdown
- A work item whose copied records hold a line that opens a fence the record never closes, in `changelog.md`, the `## Phases` section of `frame/plan.md`, either copied section of `gaps.md` or `frame/questions.md`, is now refused at that line, where before its body was written with the fold's end inside a code block (design *Scope* item 6). A round record or `trail/gate.md` that holds one was refused before this work, with the sentence of `lib/fields.py#UNCLOSED`, and still is.
```

In `changelog.md` line 4, the sentence "A copied line that opens a fence no line of its record closes is now refused at that line, in every record the body copies, since GitHub would show every line after it as code, the fold's end among them." becomes:

```markdown
A copied line that opens a fence no line of its record closes is now refused at that line in the changelog fragment, the plan's `## Phases` section, `gaps.md` and `frame/questions.md`, as it already was in a round record and `trail/gate.md`, since GitHub would show every line after it as code, the fold's end among them.
```

## Confirmations

```iadd
confirms: round-1#1
```
What holds: the code of the close. `_unfolded` builds `unclosed` from `READER.fence_spans(BLOCKS.gfm_lines(text))` for each record (`skills/code-review/scripts/pr_body.py:1023-1034`). The branch `elif line - 1 in unclosed[rel]` (`pr_body.py:1045`) refuses with the sentence the close quotes. It is indexed on the same split as `seen`, so `line - 1` names the opener. The module docstring (`pr_body.py:84-86`) and `_unfolded`'s docstring (`pr_body.py:999-1002`) name the refusal. The two rows of S9 (`tests/skills/test_pr_body.py:707-714`) assert both the line and the sentence through `UNCLOSED` (`tests/skills/test_pr_body.py:297-301`). Re-run as the close's executed line gives it: with the branch replaced by `elif False:` in the round's clone, both rows failed on `DID NOT RAISE Refused`, and the other 18 rows passed. With the branch restored and `git diff --quiet -- skills` exiting 0, `bin/test tests/skills/test_pr_body.py -q` exited 0 with 125 passed. `uvx ruff check` and `uvx ruff format --check` over the two files each exited 0 (executed). The probe of finding 1 shows the branch refusing the `gaps.md`, `## Phases` and changelog shapes that composed at `596c79a6` (executed). Finding 1 of this round is about the records' account of the refusal's reach, not about the code. The new rows each hold S9 for a record the group's other rows do not test for an unclosed fence: the group's fence rows (`tests/skills/test_pr_body.py:676-682`) close their fence. The changelog's line 4 says what the refusal does, as the close says, and finding 1 above narrows its "every record".

```iadd
confirms: round-1#2
```
What holds: `skills/code-review/orchestration.md:374-388` now gives the pair as "two quote lines from that row, the naming cell's first", and the *Judgments of the run* clause as "the `Judgment` cell, which names the question and its answer, then the `Grounds` cell". The general clause no longer says which line holds "the decision's", so the reading in which the `Grounds` cell is the decision's line is gone (read). `changelog.md:3` and `changelog.md:10` read "that cell first" (read). Round 1's two searches, run again at the target, print round 1's record, `frame/design.md:59` (S1, where a `frame/questions.md` row's `Question` and `Default until answered` cells are two cells), `frame/design.md:32`, `frame/plan.md:20` and `orchestration.md:377`. Each of them reads as the close says (executed).

```iadd
confirms: round-1#3
```
What holds: the false claim is gone. No record says any longer that the copy's closing-keyword refusal is one the change states. `grep -rn -F "rule the change"` over the work item prints round 1's record and the prefix row's `Grounds` cell at `frame/plan.md:72` with its quote at `pr.md:4` (executed). `2cff328e` rewrote that cell, and now its words "a refusal on a rule the change itself states" name the unclosed-fence refusal that the fix pass added, not the base's closing-keyword refusal. The diff does add that refusal (`pr_body.py:1045`). The prefix holds on the cell's first clause alone: "a record format" stands in the `feat:` row of `skills/commit-pr-convention/SKILL.md:128`, and the `Judgment` cell's form is one. Whether the second clause's "a rule the change itself states" holds is a row of *Not judged*. `pr.md:4` quotes the cell word for word, and `agentic pr-body` composed the body at the target with exit 0, which also checks each quote of `pr.md` against its file (executed).

```iadd
confirms: round-1#4
```
What holds: no record outside the round records names a planned milestone. `grep -rn -E '0\.4[0-9]\.[0-9]|milestone|release: '` over the work item, rounds left out, prints only `0.39.0` and `0.41.0` (`frame/design.md:7`, `frame/design.md:42`, `trail/phases/phase-1.md:7`), each a published release (executed). The release row's `Judgment` cell names the release by its role, "the planned minor after the one that carries #1671" (`frame/plan.md:71`), and `pr.md:5` quotes it word for word. The version-move bullet ends "Where the version moves at the end of the release in a pull request of its own, this item moves none." (`frame/plan.md:60`, read).

What matched: the third row of *Judgments of the run* (`frame/plan.md:73`). The finding's fix is a refusal in `_unfolded`, which no *Scope* item named before the fold. Its document, `skills/implement/fix-pass.md` *A fix that needs a unit the frame does not name waits for the fold*, stands at that heading (`skills/implement/fix-pass.md:52`, read). The fold put *Scope* item 6, S9, G16 and A13 to A16 into the frame at `7a5135eb`, before the fix pass's commit `46f97246` (executed: `git log --oneline 596c79a6..HEAD`).

What matched: `gaps.md:7`. It says the crafter ran the phase-boundary set again after round 1's fixes. The close of round 1's finding 1 gives those figures at `46f97246`. At the target this round ran `tests/skills/test_pr_body.py` alone, 125 passed, which is the 123 cases round 1 counted plus the two S9 rows (executed). The rest of the set is carried as the close states it, and the row's `unverified` label for the broad gate is honest: no party has run it.

What matched: `gaps.md:8`, the row on S1 and S8, read at this work item's own `pr.md`. `frame/questions.md:14-15` holds a table with no row, so no default pair is owed. Both quoted *Judgments of the run* rows are quoted as their `Judgment` cell, then their `Grounds` cell (`pr.md:3-6`), and each `Judgment` cell names its question, then its answer. `pr.md` quotes no part of the third row, and no rule asks for it.

What matched: the record against another work item's frame. The fix diff touches `skills/code-review/orchestration.md`, `skills/code-review/scripts/pr_body.py` and `tests/skills/test_pr_body.py`, the paths round 1 checked against the unsettled designs' `## Rule changes`. No commit in the range adds a design under `agentory/threads/` outside this work item (executed: `git diff --stat 205e2eb2..2cff328e`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the prefix row's second clause, "a refusal on a rule the change itself states", holds for the unclosed-fence refusal. At `596c79a6` the module docstring already says "the rest of the copy stands in one `<details>` fold" (the paragraph opening "Below the line `HEADING` holds", line 66 there), and the base let an unclosed fence in `changelog.md`, `## Phases` or `gaps.md` break that fold. If the refusal enforces that stated layout for those records, it is the convention's `fix:` example, "a check that let through what its rule refused", and not its `feat:` example. Which reading is right is a judgment of meaning, and the title's `feat:` stands on the record format either way | `agentory/threads/1795849898-body-decision-with-its-question/frame/plan.md:72`, `agentory/threads/1795849898-body-decision-with-its-question/pr.md:4` | the orchestrator, who writes the row, and the inspector, at `agents/inspector.md` step 4 |
| The tree-wide set `bin/test tests/text tests/behaviour -q` after the fix pass, and the broad gate of `agentory/config.json`'s `Broad gate` key. Both stay `unverified` | `agentory/threads/1795849898-body-decision-with-its-question/gaps.md:7` | the orchestrator, at the broad run |
| The phase record's `agentic mutate` runs and the close's 3 mutants of the new branch, carried as the records state them. This round ran again only the mutant `elif False:` | `agentory/threads/1795849898-body-decision-with-its-question/trail/phases/phase-1.md:21-34` | the inspector |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round2_fence_probe.py -q -s -p no:xdist`, in the round's clone at `2cff328e` | exit 0, 1 passed. It printed five shapes, each with an unclosed fence appended. The round record's prose was refused at `trail/rounds/round-1.md` line 28 and `trail/gate.md` at line 11, both with `lib/fields.py`'s `UNCLOSED` sentence. `gaps.md` was refused at line 13, the `## Phases` section at `frame/plan.md` line 10 and `changelog.md` at line 3, each with the new branch's sentence |
| The same command, in the round's clone at `596c79a6` | exit 0, 1 passed. The round record and `trail/gate.md` were refused at the same lines with the same `lib/fields.py` sentence. The `gaps.md`, `## Phases` and changelog shapes composed, with `</details>` after the opener |
| `bin/test tests/skills/test_pr_body.py -q -p no:xdist -k test_refuses_a_record_it_cannot_copy_faithfully`, in the clone at `2cff328e` with `elif line - 1 in unclosed[rel]:` replaced by `elif False:` through the `Edit` tool | exit 1: 2 failed, 18 passed. The failures were the S9 rows `frame/questions.md` line 10 and `changelog.md` line 3, each on `DID NOT RAISE Refused`. The line was restored through the `Edit` tool afterwards, and `git diff --quiet -- skills` exited 0 |
| `bin/test tests/skills/test_pr_body.py -q`, then `uvx ruff check` and `uvx ruff format --check` over `skills/code-review/scripts/pr_body.py` and `tests/skills/test_pr_body.py`, in the clone at `2cff328e` | exit 0 (125 passed), exit 0, exit 0 |
| `bin/agentic pr-body agentory/threads/1795849898-body-decision-with-its-question --body <scratch>/body.md`, in the clone at `2cff328e` | exit 0. The body was written, and its first part is `pr.md` as it stands |

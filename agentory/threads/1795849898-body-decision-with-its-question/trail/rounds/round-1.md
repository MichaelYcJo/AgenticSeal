# Review round 1: 1795849898-body-decision-with-its-question

```iadd
target: acf99157 against release/v0.41.1
```

A finding round over the whole branch, `596c79a6..acf99157`, read in a `git clone --no-local` of the branch at `acf99157`. No earlier round exists, so no fact is carried from one and every verdict below is this round's own. The records read whole at the target are `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md`. No `pr.<lang>.md` stands, because `agentory/config.json` names English for both language keys. No `agentory/parity.json` stands, and `agentory/config.json` has no `Pact` key.

## Findings

### 1. A fence the questions file never closes is copied into the body, and GitHub then shows the fold's end as code

```iadd
severity: should
location: `skills/code-review/scripts/pr_body.py:1017-1051`, `skills/code-review/scripts/pr_body.py:889-919`, `tests/skills/test_pr_body.py`
evidence: executed `bin/test tests/skills/test_tmp_round1_questions_probe.py -q -s -p no:xdist` in the round's clone at acf99157, the shape `unclosed_fence`; read `skills/code-review/scripts/pr_body.py:950-957`, `skills/code-review/scripts/pr_body.py:981-1051`, `lib/lines.py:98-100`, `lib/lines.py:133-145`, `lib/lines.py:466-484`
```

Why it matters: the old `_questions` copied only the lines that `readable` shows outside a fence, so no fence delimiter of `frame/questions.md` could reach the body. The new loop (`pr_body.py:907-915`) copies every raw line. Take a file whose fence opener has no closing line. `readable` blanks everything from the opener to the end (`lib/lines.py:133-145`). The refusals of `_unfolded` (`pr_body.py:1019-1051`) read those blanked lines, so they see nothing, and the opener is copied raw. The probe composed `# Q`, a blank line, then an opener followed by two table lines. The section came out as `From`, the opener, the two lines, and `` `frame/questions.md` holds no table line. ``, and no refusal was raised. *Questions* is the last row of `SECTIONS` (`pr_body.py:950-957`), so under CommonMark's fenced code block rule the code block runs to the end of the document (read, not rendered on GitHub). The fold's end `</details>` then shows as code. The module docstring refuses an unclosed `<!--` on the same grounds: "GitHub hides the lines after it, the fold's end among them" (`pr_body.py:81-84`). So a refusal the module already holds for one opener is missing for the other.

The class, listed from what produces it: every pair in `_unfolded`'s `copied` (`pr_body.py:1016`) that is a record's raw line. That covers `_changed`, which copies the whole changelog above the fold, where an unclosed fence would also take in `FOLD` and the summary; the *Phases* copy of `_built`; and both `_gaps` sections. Each of those could already carry such a line before this change. The change adds the prose of `frame/questions.md` to them. A refusal in `_unfolded` covers every member. The round records and `trail/gate.md` are read through `lib/fields.py` first, and this round did not re-derive whether that reader already refuses an unclosed fence for those two copies. Design G5 claimed that "The copy's existing refusals cover the new lines with no change". It rests on the census of 198 historical files. That census is a sample of shapes that occurred, not of the shapes the copy now takes.

```python
    seen = {rel: READER.readable(text) for rel, text in texts.items()}
    # The opener of each fence no line of the record closes. Precondition:
    # `fence_spans` reads `gfm_lines(text)`, the split `readable` blanks and
    # every copied line's source counts from (`lib/lines.py#readable`), so
    # `line - 1` indexes it; it is the walk `blank_fences` reads, so a line
    # refused here is one `readable` blanked to the end.
    unclosed = {
        rel: {
            first
            for first, last in READER.fence_spans(BLOCKS.gfm_lines(text))
            if last is None
        }
        for rel, text in texts.items()
    }
    causes = []
    for said, (rel, line) in (pair for pair in copied if pair[1]):
        if said == HEADING:
            ...  # as it stands
        elif line - 1 in unclosed[rel]:
            causes.append(
                (
                    rel,
                    line,
                    "opens a fence that no line of the record closes, and "
                    "GitHub shows every line after it as code, the fold's "
                    f"end `{FOLD_END}` among them; close the fence",
                )
            )
        elif (opened := CLOSER.COMMENT.match(seen[rel][line - 1])) and (
            ...  # as it stands
```

The fix pass also owes two more things. First, the refusal in the module docstring's paragraph opening "Below the line `HEADING` holds" and in `_unfolded`'s docstring. Second, a row of `Test_compose#test_refuses_a_record_it_cannot_copy_faithfully` for `frame/questions.md` and one for `changelog.md`, each seen red without the new branch (contract rules 14 and 15).

### 2. The rewritten sentence puts the decision's cell on the second line, and its own *Judgments of the run* case puts the decision on the first

```iadd
severity: should
location: `skills/code-review/orchestration.md:374-388`, `agentory/threads/1795849898-body-decision-with-its-question/changelog.md:3`, `agentory/threads/1795849898-body-decision-with-its-question/changelog.md:10`
evidence: read `skills/code-review/orchestration.md:374-388`, `templates/records/sdd-plan.md:35`; executed `grep -rn -F "on the line before it" agentory/threads/1795849898-body-decision-with-its-question` and `grep -rn -F "naming cell" agentory/threads/1795849898-body-decision-with-its-question skills/code-review/orchestration.md`
```

Why it matters: the general clause at `orchestration.md:375-377` gives the pair as "the naming cell's first and the decision's on the next line". The *Judgments of the run* clause at lines 383-385 gives it as "the `Judgment` cell, then the `Grounds` cell". By lines 386-388 and `templates/records/sdd-plan.md:35`, that `Judgment` cell holds both the question and its answer. In that row, then, the naming cell and the decision's cell are one cell, and the second line holds the grounds, not the decision. An orchestrator that reads the general clause first can read it two ways. Either the `Judgment` cell alone meets the pair, or the `Grounds` cell is "the decision's" line. The specific clause settles this work item's `pr.md`, which quotes the `Judgment` cell, then the `Grounds` cell, as the rule asks. But the sentence an orchestrator acts on at every pull request has two readings, against `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*, which `skills/core/SKILL.md` cites. `changelog.md:3` states the same pair as "the cell of the same row that names what was decided on the line before it". The process row at `changelog.md:10` does too, so a reader of the release note meets the same split. The two searches printed those three places and design *Scope* item 1 and plan A1. The frame says "the naming cell first" and no more, so the frame stands as it reads. A search on these words is a sample under contract rules 12 and 19, since a statement in other words escapes it.

```markdown
the owner must see before the fold is quoted from the record that holds
it, and a decision quoted from a table row is quoted with the cell of the
same row that names what was decided: two quote lines from that row, the
naming cell's first, with no sentence joining them.
[...]
orchestrator's row of `frame/plan.md` *Judgments of the run*, which it
writes before `pr.md`, as the `Judgment` cell, which names the question
and its answer, then the `Grounds` cell.
```

In `changelog.md:3`: "Where `pr.md` quotes a decision from a table row, the orchestrator quotes it with the cell of the same row that names what was decided, that cell first, and no sentence joins the two." In `changelog.md:10`: "The orchestrator quotes each decision `pr.md` takes from a table row with the cell of the same row that names what was decided, that cell first, and writes every *Judgments of the run* row's `Judgment` cell as the question it answers, then its answer".

### 3. The prefix's grounds say the change states the rule its new refusal enforces, and the base already stated it

```iadd
severity: should
location: `agentory/threads/1795849898-body-decision-with-its-question/frame/plan.md:64-65`, `agentory/threads/1795849898-body-decision-with-its-question/pr.md:4`, `agentory/threads/1795849898-body-decision-with-its-question/pr.md:6`
evidence: read `git show 596c79a6:skills/code-review/scripts/pr_body.py` lines 70-77, `skills/code-review/scripts/pr_body.py:1051`, `skills/commit-pr-convention/SKILL.md:127`, `skills/commit-pr-convention/SKILL.md:159-162`; executed `grep -rn -F "rule the change" agentory/threads/1795849898-body-decision-with-its-question`
```

Why it matters: the prefix row's `Grounds` cell (`plan.md:65`) claims the copy now refuses a closing keyword above or below the table, "a refusal on a rule the change itself states". The release row (`plan.md:64`) claims "The build adds a refusal on a rule the change states". At `596c79a6` the module docstring already refuses "a copied line where `lib/closing.py#keywords_in` reads a closing keyword" (lines 73-74 there), and `_unfolded` already ran `_claims` on every copied line. The diff changes no refusal. It widens what `_questions` copies (`pr_body.py:889-919`), so the existing refusal reaches lines it did not see before. `changelog.md:4` says so correctly: "as a table line was". The prefix itself holds: the `feat:` row of the prefix table lists "a record format" (`skills/commit-pr-convention/SKILL.md:127`), and the form the `Judgment` cell now takes is one. But the inspector reads these grounds against the diff (`skills/commit-pr-convention/SKILL.md:159-162`), and `pr.md:4` and `pr.md:6` quote both cells above the fold, so the owner reads a fact the base contradicts. The search printed `plan.md:64`, `plan.md:65`, `pr.md:4` and `pr.md:6`, a sample under contract rules 12 and 19.

```markdown
| 2026-11-28 | Which release ships this work item: [the cell as finding 4 leaves it] | The build adds a record format, so the title takes `feat:`, which the patch cannot carry. The owner chose on 2026-11-28 to move it to a minor of its own, not to rename the planned releases forward. | [as it stands] |
| 2026-11-28 | Which prefix the pull request's title takes: `feat:`. | Every *Judgments of the run* row's `Judgment` cell takes a new form, a record format a party now writes, and a closing keyword above or below the questions table now meets the refusal a table line met before. | `skills/commit-pr-convention/SKILL.md`, its prefix table |
```

`pr.md:4` and `pr.md:6` then quote the two rewritten `Grounds` cells word for word, since `agentic pr-body` refuses a quote its file does not hold.

### 4. A planned milestone's name and another item's frame are stated as values of releases still open

```iadd
severity: should
location: `agentory/threads/1795849898-body-decision-with-its-question/frame/plan.md:64`, `agentory/threads/1795849898-body-decision-with-its-question/pr.md:5`, `agentory/threads/1795849898-body-decision-with-its-question/frame/plan.md:54`
evidence: read `docs/releasing/branch-and-release.md:438`; executed `grep -rn -E "release|v0\.|0\.4[0-9]|milestone|branch" agentory/threads/1795849898-body-decision-with-its-question`, each line it printed read
```

Why it matters: the release row's `Judgment` cell (`plan.md:64`) names the release as `release: 0.44.0`, and `pr.md:5` carries the name into the body and the squash commit. That is a planned milestone's name. `docs/releasing/branch-and-release.md:438` states that "Until a branch is cut under a name, the planned milestones' names follow their goals, and a regrouping renames them in one act". That act makes no commit on this branch. Contract rule 19 holds such a value, the version a release carries before its cut, as a state outside the branch ("a release still open is no such moment"), and asks that the release be named by the role it plays. `plan.md:54` states "as #1671's frame proposes" with no date or commit. That is what another work item has framed, which a reframe of that item changes with no commit here. The conditional sentence it stands in reads whole without it. The search's other lines hold: `routing.md:16` and `routing.md:24` are dated, `plan.md:43` names the release by its role, and `plan.md:47-49` are read on a named date. `frame/questions.md:11` restates the conclusion of `plan.md:43` in the form the plan template's *Overlap with the release* guidance gives it, so this round leaves both. The search is a sample under contract rule 19, since a statement in other words escapes it.

```markdown
| 2026-11-28 | Which release ships this work item: a minor of its own, the planned minor after the one that carries #1671, not the patch it was routed into. | [as finding 3 leaves it] | [as it stands] |
```

`pr.md:5` then quotes that cell word for word. In `plan.md:54`, the last sentence reads: "Where the version moves at the end of the release in a pull request of its own, this item moves none."

## Confirmations

What matched: `frame/design.md` *Scope* item 2 against `skills/code-review/scripts/pr_body.py:889-919`, clause by clause. The title is the first level 1 heading `readable` gives, and a file with none is copied whole. Blank ends are dropped through `_trimmed` (`pr_body.py:742-748`). Each heading moves one level down by `"#" + line.lstrip(" ")`, the form `_round` uses at `pr_body.py:825`. A run of exactly two table lines whose second is a delimiter row is replaced by `NO_QUESTION_ROW` (`_rowless`, `pr_body.py:871-886`). `NO_QUESTION_TABLE` follows where no table line stands, `FROM` opens the section whenever the file stands, and an absent file gets `ABSENT`. Read, and executed through the probe's shapes `title_only`, `rowless_then_row_table`, `rowless_at_top_no_title`, `title_not_first` and `three_header_like`, each composed as the clause says.

What matched: *Scope* item 3 and *Data & interfaces*. `NO_QUESTION_ROW` is spelt as the frame gives it at `pr_body.py:339` and listed in `FIXED` at `pr_body.py:422`. The module docstring at `pr_body.py:15-21` says what the copy takes. `lib/tables.py` is loaded at `pr_body.py:208` with its comment. `FIXED` has no reader outside `tests/skills/test_pr_body.py#unsourced` (executed: `git grep -n "\bFIXED\b" -- '*.py'`). `_tables` has no caller left (executed: `git grep -n "_tables\b"`).

What matched: the phase record's account that each new or rewritten case is seen red (`trail/phases/phase-1.md:11-19`). The target's `tests/skills/test_pr_body.py`, run against `pr_body.py` at `596c79a6`, failed 6 cases and passed the pipe-lines case. That matches the five failures the record names at `1383f97c` plus the no-title case, and the pipe-lines case's green against the old copy (executed, *Probes*). The record's mutation runs, the pipe-lines case's red with the delimiter test removed among them, were not run again, and this round carries them as the record states them.

What matched: the phase record's narrow figure of 776 passed. `tests/skills/test_pr_body.py` passed 123 and `tests/skills/test_chain_check.py tests/evals/test_rule_cases.py tests/skills/test_agentic.py` passed 653 at the target (executed). The search of design G12, which S7 names, printed nothing at the target (executed: the command as G12 gives it, exit 1).

What matched: `gaps.md:12`, *Not done*. A level 1 heading after the title moves to level 2 and stands beside `## Questions`. The probe's shape `level1_after_title` printed `## Second` (executed). The docstring of `_questions` (`pr_body.py:893-894`), "so it nests under `ASKED`", does not hold for that shape, and `gaps.md` names it. No historical file holds the shape (design G4), and no `## ` reader reads the composed body by its headings, so this round opens no finding for it.

What matched: `gaps.md:8`, the row on S1 and S8, read at this work item's own `pr.md`. `routing.md` reads `Automation` `yes`. `frame/questions.md:14-15` holds a table with no row, so no default was taken and no pair from that file is owed. Each *Judgments of the run* row is quoted as its `Judgment` cell, then its `Grounds` cell (`pr.md:3-6`). Both `Judgment` cells name a question, then an answer, in the form `templates/records/sdd-plan.md:35` now asks for. No proposal of the orchestrator's was rejected in the exchange (`frame/plan.md:30`, A11, "agreed with a change"), so no *Alternatives considered* pair is owed. Findings 2, 3 and 4 stand beside this row: they bear on the rule's wording and on cells this `pr.md` quotes, not on whether the pairs stand.

What matched: the tests against their group. The new and rewritten cases of `Test_compose` (`tests/skills/test_pr_body.py:472-590`) each hold a clause of *Scope* item 2 that no other case of the class holds, and the S6 row (`tests/skills/test_pr_body.py:675-683`) is the only one that reads a line of `frame/questions.md` outside its table. The no-title case's docstring calls itself S2 and the pipe-lines case's calls itself S3. Both pin clauses of *Scope* item 2 beyond those scenarios' *Given*, which the frame's item 4 names.

What matched: the record against another work item's frame. The unsettled designs at the target, `1795841828-settle-only-release-note`, `1795841829-skill-descriptions` and `1795841830-find-leftovers-before-a-round`, name in their `## Rule changes` neither `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared*, nor `templates/records/sdd-plan.md`, nor `pr_body.py` (executed: `grep -n -F` on those headings and paths over their `frame/design.md`).

What matched: the implementer's account against the code. The account claimed that "`is_separator` answers false for `None`, so no default is passed" (`trail/phases/phase-1.md:39`), and `lib/lines.py:84-85` returns `bool(cells) and ...`. It also claimed that "The trim of blank ends moved from `_copied` into `_trimmed`", and `pr_body.py:736-748` shows that. The prefix `feat:` holds on the record format, as finding 3 says.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The tree-wide set `bin/test tests/text tests/behaviour -q`, which holds the plan template's heading and header (design S8), and the broad gate of `agentory/config.json`'s `Broad gate` key; both stay `unverified` | `frame/plan.md:37` | the orchestrator, at the broad run |
| The phase record's `agentic mutate` runs, twelve mutants red, carried as the record states them and not run again | `trail/phases/phase-1.md:19-34` | the inspector |
| How GitHub renders the body that finding 1's shape composes; the round read CommonMark's fenced code block rule and rendered nothing | `skills/code-review/scripts/pr_body.py:889-919` | the fix pass, through the case it adds |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round1_questions_probe.py -q -s -p no:xdist`, in the clone at `acf99157` | 1 passed; printed the *Questions* section of ten shapes. `unclosed_fence` copied the opener and both table lines, then `NO_QUESTION_TABLE`, with no refusal. `level1_after_title` printed `## Second`. `level6` printed `####### Deep`. The other shapes composed as *Scope* item 2 states |
| `bin/test tests/skills/test_pr_body.py -q -p no:xdist -k Test_compose`, in a clone at `596c79a6` with `tests/skills/test_pr_body.py` checked out from `acf99157` | exit 1: 6 failed, 32 passed. The failures were `test_accepts_a_work_item_as_the_records_text`, the S2 and S4 case, the S3 case, the S5 case, the no-title case and the S6 row; the pipe-lines case passed |
| `bin/test tests/skills/test_pr_body.py -q`, then `bin/test tests/skills/test_chain_check.py tests/evals/test_rule_cases.py tests/skills/test_agentic.py -q`, in the clone at `acf99157` | exit 0 and exit 0: 123 passed, then 653 passed |

# Review round 1: 1793411151-judgment-where-meaning-is-the-question

target: 2532cc4e against release/v0.26.0

This round reads phase 1 alone, as `frame/plan.md` *Phases* and the spawn
prompt narrow it: `frame/design.md` *Scope* items 1, 2 and 3, the pin in
`tests/text/test_a_language_section_of_writing_style_opens_alone.py`, and
the frame, since this is the first round. It is round 1, so no fact is
carried from an earlier record; every coordinate below was opened this
round. The five scripts that still refuse a line spelt otherwise while
writing-style and the core say it is named are the interim state
`trail/phases/phase-1.md` records, and no finding counts them.

## Findings

### 1. The core's first invariant forbids a question that the `Automation` `no` answer allows

severity: should
location: `skills/core/SKILL.md:99`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:102`
evidence: read `skills/core/SKILL.md:92-99`, `skills/implement/orchestration.md:179`, `hooks/question-gate.py:104`
verdict: fixed 24b7a5ed

Table B's first row states, as an invariant "not open to judgment", that no
question to a person follows the routing answer, and its protection says
"nothing stops to ask afterwards". The routing question the orchestrator
puts offers `Automation` `no` as "this run may stop to ask: somebody may be
asked at minute thirty" (`skills/implement/orchestration.md:179`). The
mechanism the row names, `hooks/question-gate.py`, returns at `:104` unless
the declaration reads `yes`, so on an attended run nothing holds the
invariant, and the core's own sentence at `:93-94` says every invariant is
held by a mechanism. An orchestrator on an attended run that reads the core
first is told it may not ask what its routing answer let it ask. The row
came from the frame's Table B (`frame/design.md:102`), which turned the base
list's "no question to a person after the routing answer" into a row with a
mechanism; the mechanism's condition shows the invariant is conditional and
the invariant's cell does not say so. The paragraph *Asking a person is the
most expensive step* (`skills/core/SKILL.md:80-84`) says "asked once,
together, before the first edit" without the condition too; it predates this
phase, and whether it is the same cause is the fix pass's sweep to decide
(contract rule 12).

```markdown
| The routing answer comes before the first edit, and on a run routed `Automation` `yes` no question to a person follows it | a person is asked once, before the first edit, and a run the person sent end to end does not stop to ask | `hooks/routing-edit-gate.py` refuses the first edit on an undeclared branch; `hooks/question-gate.py` refuses the question tool under `Automation` `yes` |
```

The same text replaces the frame's row at `frame/design.md:102`.

answer: Holds: `hooks/question-gate.py:104` returns unless the declaration reads `yes`, and `skills/implement/orchestration.md:179` offers `no` as a run that may stop to ask. The core's row now says the invariant holds on a run routed `Automation` `yes`, and its protection names the run the person sent end to end. The paragraph *Asking a person is the most expensive step* stands: it states the cost order, not an invariant, and it says what `skills/implement/SKILL.md` *1. Read the documents that outrank the code first* says, so it is not the same cause. The frame's row at `frame/design.md:102` keeps its words, because the frame is the framer's text and the orchestrator authorized a layout move only; the core is what parties read.

### 2. Table B says the check holds four invariants in every repository, and it refuses only at a ready pull request where its workflow is installed

severity: should
location: `skills/core/SKILL.md:100-103`
evidence: read `templates/setup/hygiene.yml:14-20`, `docs/one-root-by-lifetime.md:128`, `skills/code-review/scripts/chain_check.py:2259-2261`, `skills/verify/scripts/broad_gate.py:28-31`
verdict: fixed 24b7a5ed

The core is read in every user's repository, and rows two to five name
`skills/code-review/scripts/chain_check.py` as the mechanism, the fifth as
"a ready pull request fails without `Verdict: sealed` at HEAD", with no
condition. The check fails nothing outside one case. It reads committed
records through `git ls-tree HEAD`, so in local mode it reads none
(`templates/setup/hygiene.yml:14-20`), and the pull-request checks "cannot
run" there (`docs/one-root-by-lifetime.md:128`). In shared mode it runs at a
pull request only where first setup's answer or `seal pr-checks install`
wrote `.github/workflows/hygiene.yml`. At the broad run, before the pull
request opens, `gh pr view` finds none, the state is `unknown` and `strict`
is false (`chain_check.py:2259-2261`), so `seal gate`'s second arm prints
and exits 0; that arm also prints `trail/gate.md` and `guarantee.md` rather
than judging them (`broad_gate.py:28-31`). So in a local-mode repository, or
a shared one set up "records only", rows two, three and five are held by no
mechanism, and row four by `agents/sealer.md` step 1 alone. An orchestrator
there reads that a script will stop a pull request opened without a seal,
and none will. The frame's spawn asked that each mechanism Table B names do
what its row says; it does, only where it runs, and the row does not say
where. The core's margin under `hooks/lib/core.py#CAP` was 1,847 characters
in this round's measure, so one sentence fits.

```markdown
The check refuses only a ready pull request, and only where first setup or
`seal pr-checks install` put its workflow in the tree: before a pull request
is open it prints and exits 0, and in local mode it reads no committed
record. Where it does not run, the last four rows are held by
`agents/sealer.md` step 1 and by the orchestrator keeping
`skills/code-review/orchestration.md` *Orchestrator: the pull request opens
once the sealer seals*.
```

The paragraph goes directly under the table, before `## The rule a
mechanism is kept against`.

answer: Holds: `templates/setup/hygiene.yml:14-20` says the checks read committed files and examine nothing in local mode, and the check exits 0 before a pull request exists. One sentence under the table says the check refuses only a ready pull request where first setup or `seal pr-checks install` put its workflow, and that before the pull request and in local mode the last four rows are held by `agents/sealer.md` step 1 and by the orchestrator keeping `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*. It is shorter than the paste-ready paragraph. The core measures 8,525 of 10,000 characters after the fix, a margin of 1,475.

### 3. Table B's second row says every record's `target:` is a commit the branch holds, and the check holds only the last one's

severity: should
location: `skills/core/SKILL.md:100`
evidence: executed `grep -n "\.target\b\|TARGET_ROW" skills/code-review/scripts/chain_check.py`
verdict: fixed 24b7a5ed

The row reads "`target:` and every `fixed` commit are commits the branch
holds". The search finds `target:` read at two places only: `round_of`
takes the commit out of the line by its shape (`chain_check.py:1350`), and
`records` resolves the last record's alone through `follows`
(`:1765-1776`). An earlier record's `target:` is held to 7 to 40 hex digits
and never resolved, so a round 1 record naming a commit that does not exist
passes once a later round exists. The `fixed` half holds: `verdict_problems`
refuses a `fixed` commit HEAD does not descend from (`:1700`). The row's
protection, "a round reads a committed tree and its record names the
commit", is held for the last round, which is also what row three says; for
the earlier rounds the row claims a check that does not run. Either the row
says what the check does, or the check resolves every record's `target:`;
the first is phase 1's, since the second is a reader change no phase of this
frame delivers.

```markdown
| No review without a build | a round reads a committed tree and its record names the commit | `skills/code-review/scripts/chain_check.py`'s records arm: every record carries one `target:` line naming a commit, the last record's is one HEAD descends from, and so is every `fixed` commit |
```

answer: Holds: `chain_check.py:1765-1776` resolves the last record's `target:` alone, and `:1700` holds every `fixed` commit. The row now reads: every record carries one `target:` line, and HEAD descends from the last record's commit and from every `fixed` commit. The paste-ready text's "naming a commit" was dropped, because an earlier record's `target:` is held to its shape only.

### 4. The core's script sentence names "what it did not read" and "the record", both wider than the rule it states

severity: should
location: `skills/core/SKILL.md:115-120`, `skills/writing-style/SKILL.md:264-266`
evidence: read `skills/core/SKILL.md:115-120`, `skills/writing-style/SKILL.md:264-266`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:298`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:302`
verdict: fixed 24b7a5ed

"What it did not read it names and decides nothing about" has two readings.
Read whole, a script names every line it did not read: every line of prose
in a round record, a frame or a skill. Read as the frame means it, it names
a line that opens like one of its form's lines and is not one, and a file
standing where its form's file should (`frame/design.md:298`, the
`chain_check.py` row of Table A). A contributor following the new
`CONTRIBUTING.md` bullet *What it reads* builds the gate from this sentence,
and the first reading builds a script that prints every prose line. The
same sentence gives the judgment to "the agent that reads the record". A
record is a defined term here, the files under `seal/`; `seal rules --check`
reads `check:` lines in skills and policy documents, which are not records,
and Table A gives its judgment to review (`frame/design.md:302`).
`skills/writing-style/SKILL.md:264-266` already narrows the first half to
"다르게 쓴 줄" and repeats the second as "그 기록을 읽는 에이전트".

```markdown
criterion. A script holds a gate only on a fact it reads exactly: an exit
code, a parser's result, or a line of the plugin's own forms in the one
spelling the form gives it. A line that opens like one of its form's lines
and is not one, it names as not read and decides nothing on, and no script
carries a list of the spellings a label is written in: whether that line
meant the label is the judgment of the agent that reads the text. A reading
that is noisy or guessed from words is reported, never used to block.
```

The writing-style sentence changes with it, in finding 5's block:
"그 기록을 읽는 에이전트" becomes "그 글을 읽는 에이전트".

answer: Holds. The core's sentence now reads: the script names as not read a line or a file that looks like one of its form's and is not one, and decides nothing on it, and whether such a line meant the label is the judgment of the agent that reads the text. The file half covers a record under another name, which the frame's Table A row names. The paste-ready text's fronted object ("A line that opens like one of its form's lines and is not one, it names") was rewritten in subject-first order, because it reads two ways. Writing-style's "그 기록을 읽는 에이전트" became "그 글을 읽는 에이전트".

### 5. Writing-style's bold rule still says a form must not let a misspelt line pass, over a body that now says a check lets it through named

severity: should
location: `skills/writing-style/SKILL.md:257-258`, `skills/writing-style/SKILL.md:264-266`
evidence: read `skills/writing-style/SKILL.md:257-258`, `skills/writing-style/SKILL.md:264-266`
verdict: fixed 24b7a5ed

The paragraph's bold opener ends "철자가 조금 틀린 줄이 통과할 수 있는 모양을
쓰지 않는다". At the base, the body explained it: a misspelt line is refused
at its line, and a check that lets one pass silently has not read it. Phase
1 rewrote the body to the opposite: a check names a line spelt otherwise
and never refuses it for its spelling. The opener was left, so the
paragraph's rule and its body now disagree on whether a misspelt line may
pass, and a reader of the bold sentence alone, as a citation by its bold
sentence reads it (`skills/writing-style/SKILL.md:262-263`), takes the
removed rule. Contract rule 19 asks the commit that changed the fact to
correct every sentence stating it; `frame/design.md` *Scope* item 2 named
only the body's sentences, so the frame missed this one too. The opener can
carry the new rule itself, which also removes the body's restatement of it.

```markdown
**읽는 쪽이 문법으로 받아들일 수 있는 기호를 쓰지 않고, 같은 값을 두 곳에
적지 않고, 검사가 읽는 줄은 검사가 읽는 철자 하나로 쓴다.** 줄표,
```

and at `:264-266`:

```markdown
골라야 한다. 검사는 다르게 쓴 줄을 읽지 않은 줄이라고 그 자리에서 알리고,
철자를 이유로 거절하지 않는다. 그 줄이 라벨을 뜻했는지는 그 글을 읽는
에이전트가 판단한다. 사례는 `plan.md` 의 승인 줄이다. 그 줄 뒤에 문장 하나를
```

`tests/text/test_a_language_section_of_writing_style_opens_alone.py` pins
the heading and the `check:` line, not these sentences (executed in this
round's search for the phrases under `tests/`), so no pin moves.

answer: Holds. The bold opener now ends "검사가 읽는 줄은 검사가 읽는 철자 하나로 쓴다", and the body's restatement of that sentence was removed, so the body carries only the naming and the reader's judgment. `git grep` found no other text citing the opener's old words outside `seal/threads/`.

### 6. The frame's Table B renders with four rows, its fifth standing alone below a paragraph

severity: should
location: `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:105-108`
evidence: read `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:98-108`
verdict: fixed b993444b

`37bfa307` inserted the paragraph "The rows go into the core as written..."
between the fourth row and the fifth, so the table ends at `:105` and
`:108`, "No pull request without a seal", is a stray row under a paragraph.
The crafter noticed and read the fifth row from below it
(`trail/phases/phase-1.md`), and the sealer reads this frame against the
core at the guarantee; a reader of the rendered frame sees four invariants
where the core holds five. The paragraph goes under the table.

```markdown
| No seal without the broad run at HEAD | the sealer guarantees a tree the repository's `Broad gate` row in `seal/config.md` passed at HEAD | `agents/sealer.md` step 1 withholds without `trail/gate.md` at HEAD; `chain_check.py`'s broad gate arm |
| No pull request without a seal | nothing reaches the base that the last independent party did not guarantee | `chain_check.py`'s guarantee arm: a ready pull request fails without `Verdict: sealed` at HEAD |

The rows go into the core as written, with `chain_check.py` spelt by its path in the first row that names it and "the same check" after; the core is shipped to every repository, so the fourth row names the `Broad gate` row by its coordinate and no tool, since what the row runs is each repository's own (this one's runs ruff and `bin/test`, and no typecheck).
```

answer: Holds. The paragraph moved under the fifth row, with no word changed (a diff of the removed and added lines matches line for line), as the orchestrator authorized.

## Confirmations

confirms: none
The committed core fits under the hook's cap with the `Held by` cells kept
whole. `hooks/lib/core.py#output` over this round's clone at `2532cc4e`
printed 8,153 characters against `#CAP` 10,000, a margin of 1,847
(executed). The crafter's 8,017 differs by the length of the clone's path
in the header line, which `frame/design.md:37` says it carries; both are
over the 1,000 the frame set for cutting the cells.

confirms: none
Phase 1's *Verified by* holds. The six modules its row names passed, 141
cases (executed), and `seal rules --check` printed "all 265 check lines in
54 rule files hold" (executed), matching the crafter's count.

confirms: none
Rows three and four do what they say. `records` refuses a last record
behind HEAD unless only the work item's records follow it
(`skills/code-review/scripts/chain_check.py:1763-1776`), and `channel`
refuses a `fixed` or `rejected` finding the next record does not name
(`:1755-1762`); `agents/sealer.md:57-67` withholds without `trail/gate.md`
at HEAD, and `broad_gate` refuses a gate record behind HEAD
(`chain_check.py:1886-1908`), at a ready pull request (finding 2 says
where). The fifth row's guarantee arm refuses a guarantee whose verdict is
not `sealed` (`:1951-2010`). All read.

confirms: none
`CONTRIBUTING.md:386-391`, the bullet *What it reads*, says what Scope item
3 asks and cites a section the core holds. The crafter's claim that
`.github/PULL_REQUEST_TEMPLATE.md:29-34` names the section as the whole of
it, so no bullet is copied there, holds (read). The pin change in
`tests/text/test_a_language_section_of_writing_style_opens_alone.py:43-48`
matches the new `check:` line at `skills/writing-style/SKILL.md:268`; the
base copy lacks `tests/skills/test_chain_check.py`, so it fails against the
new line, as the phase record says it was shown (read). The phase record
says the line "keeps the four modules it named"; the base line named five
and the new line keeps all five.

confirms: none
The orchestrator's fold at `2532cc4e` agrees with itself: *Scope* item 4,
the *Grounding* row at `frame/design.md:36`, `frame/plan.md` A13 and the
Delivers cell of phase 1, and `gaps.md` *Not done* all say the module stays
and its removal is #1197, and `## Removes` no longer lists it (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and `seal gate` over the branch, labelled `unverified` in `gaps.md` | the branch at `2532cc4e` | the orchestrator, by `seal gate --base release/v0.26.0 --record` after the rounds settle |
| The crafter's 123-module boundary set and 46 record-reading modules, which this round did not re-run | `trail/phases/phase-1.md` | the orchestrator's broad run |
| Whether `frame/design.md:23` and *Scope* item 2, which say the writing-style sentence changes in the commit that changes its readers, should be corrected to the plan's phase 1, or stand as the departure `trail/phases/phase-1.md` records; the spawn prompt calls it a known interim state | `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:23` | the orchestrator |
| Phases 2 to 5 and their Scope items, outside this round by `frame/plan.md` *Phases* | `frame/design.md` *Scope* items 5 to 14 | the rounds that read those phases |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_review_axes.py tests/text/test_every_agent_reads_the_contract.py tests/skills/test_core_check.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_a_language_section_of_writing_style_opens_alone.py tests/behaviour/test_release_hygiene.py -q`, in a `git clone --no-local` at `2532cc4e` | 141 passed, exit 0 |
| `bin/seal rules --check`, in the same clone | "all 265 check lines in 54 rule files hold", exit 0 |
| `python3 -c` calling `core.output(root, root)` from `hooks/lib/core.py`, in the same clone | 8,153 characters, 1,847 under `CAP` |
| `grep -n "\.target\b\|TARGET_ROW" skills/code-review/scripts/chain_check.py` | `target:` read at `:213` (the grammar row), `:1350` (by shape) and `:1765-1772` (the last record only) |
| `grep -rln` over `tests/`, `docs/`, `skills/` and `agents/` for the phrases of findings 1, 4 and 5 | only `skills/core/SKILL.md` and `skills/writing-style/SKILL.md`; no case pins them |

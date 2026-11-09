# Review round 1: 1794188289-the-body-reads-in-the-teams-language

```seal
target: 1677d096 against origin/release/v0.36.0
```

The whole diff `origin/release/v0.36.0...1677d096` (38 files) was read
against issue #1453, its one comment (the owner's decision), the work item's
`routing.md`, the three frame files, `gaps.md`, `changelog.md`, `pr.md` and
both phase records. No earlier round exists, so no fact was carried and
every fact below was established this round. The work item holds no
`pr.<lang>.md`, and this repository's two language rows both read `English`
(`seal/config.md:9-10`), so none is owed. No `seal/parity.md` is declared.

## Findings

### 1. The frame's `## Rule changes` does not parse, so the pull request's check refuses it and the settle cannot group the design

```seal
severity: must
location: `seal/threads/1794188289-the-body-reads-in-the-teams-language/frame/design.md:129-130`
evidence: executed `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.36.0 --root <worktree> --worktree`; executed the same check over the scratch clone with the span joined (`## Probes`)
```

Why it matters: the chain check printed this notice at the frame:

> seal/threads/1794188289-the-body-reads-in-the-teams-language/frame/design.md:130  `## Rule changes` does not parse, so `settle` cannot group this design by the sections it names and the settle has to read it whole: this line begins inside a code span an earlier line opened, and settle would drop it: close each span on the line that opens it

The first operation's `to:` opens the span `` `Commit and pull request `` at
`frame/design.md:129` and closes it on line 130. By
`docs/running/what-a-script-gates.md` *The checks*, the `seal settle` row, a
section that does not parse is refused at its line at the pull request, so a
ready pull request fails `chain_check.py`, and `seal gate --preflight`'s
chain arm refuses it before the broad run. It also hides every other read of
the section: no test pin a `from` takes out and no run a `to` shares with
another rule document is named while the section does not parse. With the
span joined in the scratch clone, the check named nothing at the frame, so
no pin or copy notice stands behind this one. The repair is the
orchestrator's, since the finding is located in a frame file
(`skills/code-review/orchestration.md` *Orchestrator: the pull request opens
once the sealer seals*).

In `frame/design.md`, replace lines 127-132, the first operation's `to:`,
with:

```markdown
  to: `seal pr-body` writes above the line
    `skills/code-review/scripts/pr_body.py#HEADING` holds the work item's
    `pr.<lang>.md`, where `seal/config.md`'s
    `Commit and pull request language` and `Record language` rows name
    different languages, and then `pr.md`, each as its bytes stand, and
    below that line the copy of the work item's records
```

No other line of `## Rule changes` opens a span it does not close: a count
of backticks per line over `frame/design.md:119-230` found lines 129 and 130
alone odd.

```seal
verdict: fixed 78f083c8
answer: The orchestrator repaired it at 78f083c8 by joining the code span onto one line; the fix pass ran `chain_check.py --baseline origin/release/v0.36.0 --worktree` at f71c31ba, exit 0, and no line names `frame/design.md`.
```

### 2. Four places still say the body's first part is `pr.md`, and three of them put the correction in a later paragraph beside it

```seal
severity: should
location: `skills/code-review/orchestration.md:402-403`, `skills/commit-pr-convention/SKILL.md:237-242`, `templates/setup/config.md:92-94`, `lib/optin.py:58-59`
evidence: executed `git grep -n "first part is\|first part, \|body's first part\|body opens with" -- skills agents templates lib docs`; read `skills/code-review/scripts/pr_body.py:429-482`, `skills/code-review/orchestration.md:402-439`, `skills/commit-pr-convention/SKILL.md:234-266`, `templates/setup/config.md:86-100`, `lib/optin.py:58-60`
```

Why it matters: `pr_body.py#first_part` (`pr_body.py:472-482`) composes the
first part as `pr.<lang>.md` and then `pr.md` wherever the two rows differ.
Four statements still define the first part as `pr.md`:

- `skills/code-review/orchestration.md:402`, the section's bold lead: "The
  pull request body's first part is the work item's `pr.md`". The paragraph
  at line 426 then adds `pr.<lang>.md` above it.
- `skills/commit-pr-convention/SKILL.md:237-239`: "The first part is the
  work item's `pr.md`, ... and `seal pr-body` writes it above the line".
  Line 266 then says "the body's first part is the mirror and then `pr.md`".
- `templates/setup/config.md:92-94`: "the lines of the body's first part,
  the work item's `pr.md` above the line". The sentence at lines 98-100
  then adds the mirror.
- `lib/optin.py:58`, the comment on `PR`: "The pull request body's first
  part".

The orchestrator reads the first three before it writes `pr.md` and the
body. Contract rule 19 says the change rewrites the sentence it amends in
place, and that a correction written beside the sentence it corrects leaves
both for the next reader to choose between. The phase 1 departures and the
`## Removes` rows rewrote these sections, so these sentences were in the
diff's reach. The list above comes from a search for wordings, so it is a
sample of the class, which is every statement of what the first part holds.
The fix pass owes a `git grep` for the other wordings, such as "above the
line" and "opens with", over `skills`, `agents`, `templates` and `lib`.
`docs/` is outside it: `frame/design.md` *Rule changes* carries its
statements to the settle.

In `skills/code-review/orchestration.md`, replace lines 402-404 with:

```markdown
**The pull request body's first part is the work item's `pr.md`, opened by
its `pr.<lang>.md` where the two language rows differ, as the paragraph on
`pr.<lang>.md` below says. The orchestrator writes `pr.md` once the build's
last phase has closed and commits it before it spawns the first round.**
```

In `skills/commit-pr-convention/SKILL.md`, replace the sentence at lines
237-242 that opens "The first part is the work item's" and ends "opens once
the sealer seals*)." with:

```markdown
The first part is the work item's `pr.md`, opened by its mirror where the
two rows name different languages (below). The orchestrator commits `pr.md`
before the first round, and `seal pr-body` writes the first part above the
line `skills/code-review/scripts/pr_body.py#HEADING` holds, then the second
part under that line from the work item's other records, inside one
`<details>` fold (`skills/code-review/orchestration.md` *Orchestrator: the
pull request opens once the sealer seals*).
```

In `templates/setup/config.md`, replace lines 92-95, up to "attribution
lines.", with:

```markdown
In the body of a pull request routed through the review chain, the row
governs the lines of the work item's `pr.md` that quote no record: its
`Closes`, `Part of` and attribution lines. `pr.md` stands in the body's
first part, above the line `skills/code-review/scripts/pr_body.py#HEADING`
holds.
```

In `lib/optin.py`, replace the comment at lines 58-59 with:

```python
# The work item's own file of the pull request body's first part, which
# `seal pr-body` writes above the copy of the records, after the work item's
# `pr.<lang>.md` where the two language rows differ.
```

No test pins any of the four sentences (executed: `git grep` over `tests`
and `evals` for each one).

```seal
verdict: fixed f71c31ba
answer: Fixed in f71c31ba, which rewrites the four listed paths, and in a98be282 after it, which touches none of them and carries the Korean statement below. The four sentences were rewritten in place as the paste-ready fixes give them, read first against `frame/design.md` *Scope* items 3 and 4 and `pr_body.py#first_part`; in `skills/code-review/orchestration.md` the paragraph was rewrapped to the 88-column limit `tests/behaviour/test_docs_line_wrap.py` holds. The class was searched with `git grep -i` for "first part", "above the line", "opens with `pr", "body opens", "opens the body", "above the heading" and "orchestrator's part" over `skills`, `agents`, `templates`, `lib`, `hooks`, `bin`, `.github`, `evals/scripts` and the root documents. That search found more statements of the first part as `pr.md` alone, each rewritten in the same commit: the `pr.md` line of the tree in `templates/setup/seal-README.md` and `seal/README.md`, which the suite holds equal; the `pr.md` row of `skills/implement/SKILL.md` *3. The SDD file set*, whose correction stood in a second sentence of the cell; and three test comments and docstrings, `tests/skills/test_pr_body.py` at `OWN` and `Test_read_own`, and `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`. A second pass over the Korean lines naming `pr.md` in the same directories found `skills/writing-style/outside-the-review.md`, whose paragraph opening *리뷰 체인을 거친 작업 항목의 PR 본문은 두 부분이고* said the first part is `pr.md` and put `pr.<lang>.md` in a later sentence, and whose PR-body paragraph gave `pr.md` alone as the part holding no sentence of the orchestrator's; a98be282 rewrites both in place, and wraps the two test texts f71c31ba left past the 88-column line. Four stand, each naming both files in its own sentence or naming sources rather than the first part: `agents/sealer.md` step 2 and its `description`, `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* step 2, and `skills/implement/scripts/seal.py`'s `pr-body` line, where `pr.<lang>.md` is one of the work item's records. The search is a sample of wordings; `docs/` was left to `frame/design.md` *Rule changes*.
```

### 3. `lib/config.py#declared_mode` still says every other row has a default

```seal
severity: should
location: `lib/config.py:557-558`
evidence: read `lib/config.py:1-12`, `lib/config.py:557-561`, `templates/setup/config.md:213-215`; executed `git grep -n "falls back to what" -- ':!seal/threads'`, which does not return line 557 because the phrase wraps onto line 558
```

Why it matters: the docstring of `declared_mode` says "Every other item in
`config.md` falls back to what every repository got before the row existed".
The module docstring this diff rewrote (`lib/config.py:4-10`) says four rows
have no default, the two language rows among them. `frame/design.md`
*Removes* names the same sentence in `templates/setup/config.md` *Mode*,
"Every other item here falls back to what repositories got before the row
existed", and phase 1 rewrote it there (`templates/setup/config.md:214`).
The copy in `lib/config.py` stands, so one file now gives two answers. The
phase 2 census searched "every absent row but two" and "The file is
optional" under `lib`. The phase 1 census did not search the *Mode*
sentence's words, and a search on them misses this copy, because it wraps
across two lines. That is the sample contract rule 12 names: a list built
from wordings already seen. A crafter who edits the config reader reads this
docstring and acts on it.

In `lib/config.py`, replace lines 557-558, up to "existed;", with:

```python
    **There is no default.** An item with a default falls back to what
    every repository got before the row existed; for the mode that is
```

```seal
verdict: fixed f71c31ba
answer: The sentence was rewritten in place as the paste-ready fix gives it. The class was searched with `git grep -i` for "row existed", "every other item", "every other row", "has a default" and "no default" over `lib`, `skills`, `agents`, `templates`, `hooks` and `bin`; the remaining hits name one row each, `Reference specs` and `Policy root` in `lib/config.py`, or already name the four rows without a default, so none was changed.
```

## Confirmations

What matched: the eight *Scope* items of `frame/design.md` stand in the
tree. Item 1 is `skills/implement/bootstrap.md:46-49`, `:130-139` and
`:151-156`. Item 2 is `skills/implement/orchestration.md:200-218`. Item 3 is
`skills/code-review/scripts/pr_body.py:429-482` and its use in `compared`
(`pr_body.py:956-974`) and `main` (`pr_body.py:1021-1059`). Item 4 is
`skills/code-review/orchestration.md:426-438`, `agents/proofer.md:122-132`
and `agents/sealer.md:74-86`. Item 5 is
`skills/commit-pr-convention/SKILL.md:78-91` and
`skills/config/SKILL.md:9-11` and `:41-58`. Item 6 is
`seal/config.md:9-10`. Item 7 is the cases of `tests/skills/test_pr_body.py`
and the five sealer scaffolds. Item 8 is `changelog.md` with three
*Process changes* rows (read).

What matched: the phase 2 record claimed that each new case of
`tests/skills/test_pr_body.py` was seen red against `pr_body.py` as
`4527db5f` left it, and that `one language in two cases` passes there. With
the base's `pr_body.py` checked out in the scratch clone, 19 of those cases
failed and `one language in two cases` passed (executed). `pr_body.py` is
the same at `c4bb8877` and `4527db5f` (executed: `git diff --stat`).

What matched: the narrow run over the seven test modules the diff changes
passed, 502 cases (executed, exit 0). The suite as a whole is `unverified`,
as `## Not judged` says.

What matched: the body arm's path. The phase 2 record claimed that a cause
about a language row is placed at `seal/config.md` in both `seal pr-body`
and the body arm. `chain_check.py:1822` normalises the joined path, and
`pr_body.py:986-989` does the same through `_place`. Both
`#test_refuses_a_repository_without_a_language_row_at_its_config` and
`#test_refuses_a_repository_without_a_language_row_naming_it` assert the
`seal/config.md` line, and both passed in the narrow run (executed).

What matched: a `config.md` that will not read is named once and without a
machine path. `pr_body.py:445-464` strips the path that
`lib/config.py#unreadable_config` opens with, and drops a cause both rows
give. `#test_refuses_a_language_row_no_one_reads_naming_no_machine_path`
asserts one line and no `tmp_path` in it (read; executed in the narrow run).

What matched: every quote of `pr.md`, twelve in all, stands word for word,
with runs of whitespace collapsed, at the record its coordinate names
(executed: a script comparing each quote with `changelog.md`,
`frame/plan.md` and `gaps.md`). Each coordinate's item or row is the one
that holds the sentence (read).

What matched: each `from:` of `frame/design.md` *Rule changes* stands in its
policy document at HEAD (executed: a whitespace-collapsed search of each
`from:` in its file). The `add` to `docs/checks/the-pull-request-check.md`
*What the check reads at the pull request* names a section that exists
there (read).

What matched: the merge at `4527db5f` kept both sides in
`skills/code-review/orchestration.md` *Orchestrator: the pull request opens
once the sealer seals*. #1452's sentences on the body arm
(`orchestration.md:266-271`) and this work item's paragraphs
(`orchestration.md:426-468`) do not contradict each other (read).

What matched: the census of the `## Removes` sentences. "links it from the
body", "So not under the git directory", "That folder sits under the root,
which is resolved", "keeps a Korean mirror", "keeps an English mirror",
"carrying **two", "The body opens with the work item's", "every absent row
but two" and "The file is optional" return nothing outside
`seal/threads/` (executed). Finding 3 is a copy those searches could not
reach.

What matched: the changelog's source link,
`issues/1453#issuecomment-6730134448`, is the owner's comment on #1453
(executed: `gh api`).

One case gap holds no defect the release would ship, so it is no finding:
`tests/behaviour/test_first_setup_asks_once.py:181` asserts the bold lead
"**Then the two language rows.**". Its message claims that nothing writes
the answered rows into the stub. What it pins is the lead's wording: the
phase 1 mutation that renamed the lead turned it red. A paragraph that kept
the lead and dropped the instruction would pass. The instruction's own
shape, `` `| <row> | <answer> |` `` (`skills/implement/bootstrap.md:155`), is
the fact the message names.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite as a whole, the repository-wide lint and the typecheck: `unverified`, since contract rule 2 leaves the broad gate to the orchestrator | the `Broad gate` row of `seal/config.md` | the orchestrator, at `seal gate --record` once the rounds settle |
| Whether an orchestrator following `skills/implement/bootstrap.md` step 1 and the batch of `skills/implement/orchestration.md` asks the four questions in one call and writes the rows, or the default and its `routing.md` sentence, as `gaps.md` *Not verified* row 1 states | `skills/implement/bootstrap.md:130-156`, `skills/implement/orchestration.md:200-218` | the repository owner, on the first bootstrap and the first work item of a repository without the rows under the release that ships this |
| Whether a downstream repository with `Record language` `English` and `Commit and pull request language` `Korean` gets a body that opens with `pr.ko.md` and passes both checks, as `gaps.md` *Not verified* row 2 states | `skills/code-review/scripts/pr_body.py:429-482` | the repository owner, on that repository's next pull request under the release |
| Whether the settle owes `docs/layout/one-root-by-lifetime.ko.md` the two sentences the *Rule changes* operations add to the English edition's *What the repository decides for itself, and how it is read*: no operation names the Korean edition, and `CONTRIBUTING.md` says every document with a `.ko.md` edition moves with it | `frame/design.md:185-209`, `docs/layout/one-root-by-lifetime.ko.md:213-229` | the settling session, at `seal settle` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pr_body.py tests/skills/test_chain_check.py tests/evals/test_rule_cases.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_waiver_decided_at_start.py tests/text/test_the_settings_have_a_front_door.py -q`, in a `git clone --no-local` at `1677d096` under `<scratchpad>/1453-r1/clone` | exit 0, 502 passed |
| `git checkout c4bb8877 -- skills/code-review/scripts/pr_body.py` in that clone, then `bin/test tests/skills/test_pr_body.py -q -p no:xdist -k "language_row or first_part_the_rows or without_one_translation or not_the_translation"`, then `git checkout HEAD -- skills/code-review/scripts/pr_body.py` | exit 1: 19 failed, 1 passed (`one language in two cases`); the clone was clean again afterwards |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.36.0 --root <worktree> --worktree` | exit 0; the notice at `frame/design.md:130` that finding 1 quotes, and the refusals owed before the first round record, the gate record and the guarantee |
| lines 129-130 of the clone's `frame/design.md` joined with the Edit tool, then `chain_check.py --baseline c4bb8877 --root <scratchpad>/1453-r1/clone --worktree`, then the edit reverted | exit 0; no line at `frame/design.md`, so no test pin or copy notice stands behind finding 1 |
| a script comparing each quote of `pr.md` with its source, runs of whitespace collapsed | 12 of 12 found |
| `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6730134448` | the owner's comment on #1453, 2026-11-09 |

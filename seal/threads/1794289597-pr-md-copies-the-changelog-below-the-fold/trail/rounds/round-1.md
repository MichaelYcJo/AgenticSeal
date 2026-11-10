# Review round 1: 1794289597-pr-md-copies-the-changelog-below-the-fold

```seal
target: b1a1227c0 against origin/release/v0.37.2
```

This round reviews `origin/release/v0.37.2...b1a1227c0`, with the base at
`ce915f17e`. The range holds the merge `6e84fe633`, which brought #1477 in
after phase 1. The local `release/v0.37.2` stands at `df775c52c` and was not
used. The round applies the tree's `agents/proofer.md`, which this diff
changes, and not the installed 0.37.1 copy it was spawned with. The two
differ in three places that bear on this round: the sentence on a dated
frame section (`agents/proofer.md:126-130`), the three findings on
`pr.<lang>.md` (`:134-138`), and the verifying-round rule, which round 1
does not use. No `pr.<lang>.md` stands here, because `seal/config.json`
names English for both language keys (read), so the three `pr.<lang>.md`
findings have nothing to read.

Round 1 has no earlier record, so no fact is carried from one. Every
verdict below is this round's own.

**`frame/questions.md` Q2, measured.** `chain_check.py --baseline
origin/release/v0.37.2 --root <the worktree> --worktree` printed no pin
notice and no copy notice at any line of `frame/design.md`, and no line
naming a rule change as not read (executed; the run's whole output is in
*Probes*). The reading ran for this work item: `main` calls
`rule_changes_of` for each declared item (`chain_check.py:2186`), and its
notices print before its problems (`:2228-2231`). So the check names no
test literal that a `from` holds and its `to` drops, and no 15-word run a
`to` shares with another rule document. Q2's default, that the build
proceeds as if no notice is printed, matches the measurement. No finding
here is taken from a notice. Each `from` stands once in the document its
`file:` names (executed, `git grep -c -F` on a distinctive run of each).

## Findings

### 1. `pr.md` does not quote the row that says why the title takes `refactor:`

```seal
severity: must
location: `seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold/pr.md:1-6`, `seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold/frame/plan.md:72`
evidence: executed `grep -n "title takes" seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold/pr.md` (no line, exit 1); read `skills/commit-pr-convention/SKILL.md:260-262`, `skills/code-review/orchestration.md:413-419`, `seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold/frame/plan.md:72`, `seal/threads/1794289595-the-verifying-round-rule-has-four-owners/pr.md:9`, `seal/threads/1794289596-implement-orchestration-grew-back/pr.md:9`
```

Why it matters: `skills/commit-pr-convention/SKILL.md:260-262` says that
why the title takes its prefix "is one row of `frame/plan.md` *Judgments of
the run*, which `pr.md` quotes". The owner of `pr.md`'s shape,
`skills/code-review/orchestration.md:413-419`, lists the same row among what
the owner must see before the fold. The orchestrator wrote that row at
`frame/plan.md:72` ("The title takes `refactor:`"), and the commit that
wrote it, `b1a1227c0`, also rewrote `pr.md`. `pr.md` holds four quotes and
none of them is that row. The two sibling items of this release quote it at
their `pr.md:9`. `agents/sealer.md` step 4 reads the title's grounds in this
part of the body and compares them with the diff
(`skills/commit-pr-convention/SKILL.md` *The orchestrator states the grounds
for a pull request's title*). With no quote, the sealer has no grounds to
compare. The repair is the orchestrator's, since no crafter writes `pr.md`
(`skills/code-review/orchestration.md:444-450`). No `pr.<lang>.md` stands,
so no rendering is owed beside the quote.

```markdown
<!-- seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold/pr.md, after line 4 -->
- "The title takes `refactor:`" (`frame/plan.md` *Judgments of the run*, the row of the title)
- "The diff moves where `seal pr-body` writes one record and where the `pr.md` rule is stated; no gate is added or removed, the body arm reads the same function, and every finding the proofer could name before it can name after" (`frame/plan.md` *Judgments of the run*, the row of the title, its Grounds cell)
```

```seal
verdict: fixed c3029edd7
answer: The orchestrator, who writes `pr.md`, added the two lines of the fix at `pr.md:5-6`, word for word as the finding gives them. Each of `pr.md`'s six quotes stands word for word, whitespace collapsed, in the file its coordinate names, and the two new ones equal the Judgment and Grounds cells of the title row at `frame/plan.md:72` (executed, a script over `pr.md`, `frame/plan.md` and `frame/design.md`). The tree's `bin/seal pr-body` writes the body with the title row above `## From the records`, and its `--check` on that body exits 0 (executed).
```

### 2. `frame/design.md` S5 asks for a body-arm case holding a stale body, which the build declined and no fold records

```seal
severity: should
location: `seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold/frame/design.md:55`
evidence: executed `grep -c "What changed" tests/skills/test_chain_check.py` (0), and an `awk` listing of `Test_body`'s cases (`tests/skills/test_chain_check.py:3230-3516`, sixteen cases, none holding a whole stale body); read `seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold/trail/phases/phase-1.md:13`, `skills/code-review/scripts/chain_check.py:1793-1834`, `tests/skills/test_chain_check.py:3334-3348`, `tests/skills/test_pr_body.py:1291-1318`, `seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold/frame/plan.md:65-72`
```

Why it matters: S5's *Verifiable how* cell ends "the crafter adds one for
the second half where none holds a whole stale body". No case of
`tests/skills/test_chain_check.py` holds a whole stale body, and the build
added none. Phase 1 states the departure at `phase-1.md:13` and leaves it
to this round to weigh. Its reading holds. The arm holds no layout of its
own: `chain_check.py#body` calls `pr_body.py#compared` and prints each cause
at the body's line (`:1793-1834`). The S4 case of
`tests/skills/test_pr_body.py:1291-1318` drives a 0.37.1 body through
`compared`. `Test_body::test_refuses_a_drifted_body_at_its_line`
(`test_chain_check.py:3334`) holds the arm's refusal at the body's line. A
case in the arm with a stale body would cover nothing its group does not
already cover, which `agents/proofer.md` *Each new test is read against its
group* names as a `should` finding.

So the defect is the sentence, not the missing case. `frame/plan.md`
*Judgments of the run* holds no row for this departure, though the folds
`7bf23ef25`, `d8febe0fc` and `f778a164f` brought the other departures the
phase records named (S7, D3, `frame/plan.md` *Technical context*) into the
frame. The sealer reads S5 against the tree at step 4 and finds a case the
frame promises and the tree lacks. `frame/design.md` is the framer's file,
so the repair is a fold. The snippet covers S5's row. The orchestrator's
*Judgments of the run* row recording the fold is the other statement the
repair owes, and the snippet does not write it.

```markdown
<!-- seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold/frame/design.md:55, the Verifiable how cell of S5 -->
The body-arm cases of `tests/skills/test_chain_check.py`, green with fixtures in the new layout. The second half rests on `pr_body.py#compared`, which the arm calls (G3): `tests/skills/test_pr_body.py` `Test_main::test_refuses_the_changelog_inside_the_fold_until_written_again` drives the S4 body through it, and `Test_body::test_refuses_a_drifted_body_at_its_line` holds the arm's refusal at the body's line, so no case of the arm holds a whole stale body (`trail/phases/phase-1.md`).
```

```seal
verdict: fixed dd9169206
answer: The framer, who writes `frame/design.md`, folded the fix into S5's *Verifiable how* cell at `frame/design.md:55`. The cell equals the fix with one addition, "of `tests/skills/test_chain_check.py`" after `Test_body::test_refuses_a_drifted_body_at_its_line`, which names the module of a case the fix left unplaced (executed, a string comparison of the cell with the fix). The cell holds against the tree: the S4 case stands at `tests/skills/test_pr_body.py:1291` in `Test_main` and calls `main` with `--check`, which calls `compared` (`pr_body.py:1043`), and the drifted-body case stands at `tests/skills/test_chain_check.py:3334` in `Test_body` (read); both pass (executed). The same commit adds the *Judgments of the run* row at `frame/plan.md:73`, the second statement the finding said the repair owes.
```

## Confirmations

What matched: *Scope* item 1 and D1. `_composed` lays `_changed`'s blocks
through `_laid` after the mark and before `FOLD`, and the other sections
after `SUMMARY` (`skills/code-review/scripts/pr_body.py:769-806`, read).
The refusals still walk `below` whole, so a changelog line is refused at its
record as before. An empty block is dropped as the old loop dropped it. This
work item's own body, composed with the tree's `bin/seal pr-body`, stands in
D1's order: `pr.md`, the heading, `## What changed`, the fragment, then
`<details>` (executed; `--check` on it exits 0). The module docstring
(`:22-55`), the `FOLD` and `TAG` comments (`:184-196`) and `_composed`'s
docstring state the new layout. `main`'s parser description (`:1014-1018`)
names no fold, so it needed no change, as phase 1 claimed (read).

What matched: *Scope* item 2 and S1 to S4. `EXPECTED` takes D1's layout,
`test_accepts_a_missing_changelog_above_the_fold` holds S2, and
`test_refuses_the_changelog_inside_the_fold_until_written_again` holds S4 at
the body's lines 5 and 15 (read). Each is red against the 0.37.1 placement
by reading alone: the old `_composed` gives the old layout, a part with
nothing before the fold, and a body equal to the stale one. So no probe was
written to re-run the `seen red` claims. The refusal cases of S3 are
unchanged in what they assert. The three line-number repairs phase 1 names
(13 to 10, 14 to 11, and 13 to 10 in `Test_body`) follow from the
changelog moving three lines up (read). The five sealer scaffolds match the
generator (executed, `tests/behaviour/test_evals_layout.py` green).

What matched: *Scope* items 3 to 6. The owner's new sentence stands at
`skills/code-review/orchestration.md:403-407`. The `pr.<lang>.md`
paragraph (`:426-442`) states *Scope* item 4 in its order. The fix-pass
paragraph (`:444-450`) keeps the sentence on a finding located in `pr.md`
word for word and drops the re-read before each spawn of the sealer. The
body paragraph (`:455-460`) names the fragment between the heading and the
fold. `agents/proofer.md:134-138` names the three findings and
`agents/sealer.md:84-86` reads the renderings (read). A search for the
removed step's words outside `seal/threads/` finds it nowhere outside the
owner's new sentence and `docs/layout/the-record-layout.md:117`, which
`## Rule changes` carries (executed).

What matched: *Scope* item 7, D3, S7 and S8. D3's command at HEAD lists 18
files: the table's nine, its list's six, and the three files *Scope* items 3
and 6 edit (executed). Each table row is built as worded, and
`seal/README.md` and `templates/setup/seal-README.md` are identical
(executed, `diff`). The six listed files' sentences on `pr.md` state nothing
the new facts change (read). `RULES` row 23 holds the owner's sentence and
four carriers. S7's `git diff --stat` prints nothing, and S8's `git grep`
gives the four hits phase 3 names, each in the new shape (executed).

What matched: *Scope* item 8 and `changelog.md`, sentence by sentence
against the tree. `seal pr-checks remove` and `install` behave as the
`Updating:` paragraph says (`skills/implement/scripts/seal.py:36-41`,
`templates/setup/hygiene.yml:6-12`, read). `### Process changes` holds one
row each for *Scope* items 3, 4, 5 and 6.

What matched: `pr.md`. Each of its four quotes stands word for word at its
coordinate (`frame/design.md:11`, `:18`, `frame/plan.md:57`, `:69`, read).
No line carries a `changelog.md` coordinate, as S6 asks.

What matched: the dated sections, read under the tree's
`agents/proofer.md:126-130`. Each sentence of `frame/design.md` *Grounding*
and `frame/plan.md` *Technical context* that says what the work does or
concludes holds at the target. These include G1's "the build edits no file
under `docs/`", G3's "`chain_check.py` is not edited", G10's "this work does
not edit `skills/implement/orchestration.md`" and G13's "this work moves no
version" (executed, `git diff --stat`; read, `.claude-plugin/plugin.json`).

What matched: `gaps.md` *Not done*, first paragraph. The refusal sentence a
`</details>` on a changelog line still gets says "the end of the copy's one
`<details>`", which no longer fits a line above the fold
(`pr_body.py:832-839`). S3 keeps the existing refusal cases "with no change
to what they assert", and the remedy the sentence names, a code span, is
still right. So the frame bears this out and it is no finding. The `MARK`
comment at `pr_body.py:272-276` still places the mark "between `HEADING`'s
blank line and `FOLD`", which stays true with the changelog also between
them.

What matched: the new tests against their group. The S2 case asserts the
absent line's place, which `test_accepts_a_missing_record_as_its_fixed_line`
does not. The S4 case is the one case that drives a whole 0.37.1 body. Row
23 is a parameter of the existing `RULES` cases (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD; the suite is `unverified` here and the label in `gaps.md` is honest | `gaps.md:7` | the orchestrator, through the broad gate |
| The five sealer eval cases run by an agent against the new layout | `gaps.md:8` | the repository owner, at the next run of the behaviour evals |
| Whether `refactor:` fits a diff that changes what `seal pr-body` composes and asks a workflow pinned to an earlier release to move; the issue's title takes `refactor:` and the release is a patch | `frame/plan.md:72` | the sealer at step 4, reading the row finding 1 quotes |
| `frame/questions.md` Q2's Status cell, which still reads `open` after the measurement above | `frame/questions.md:22` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.37.2 --root <the worktree> --worktree` | exit 0; no pin or copy notice, and no rule change named as not read; it named the body as not read under `--worktree`, no `round-N.md` yet, and no gate record or guarantee yet |
| `bin/test tests/skills/test_pr_body.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py -q` | exit 0, 226 passed |
| `bin/test tests/skills/test_chain_check.py -q -k Test_body` | exit 0, 18 passed |
| `bin/test tests/behaviour/test_evals_layout.py tests/evals/test_rule_cases.py -q` | exit 0, 38 passed |
| `bin/test tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` | exit 0, 117 passed |
| `uvx ruff check` and `uvx ruff format --check` on the five changed Python files | exit 0 each |
| `bin/seal pr-body seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold --body <scratchpad>/1794289597-pr-md-copies-the-changelog-below-the-fold/round-1/pr-body.md`, then the same with `--check` | exit 0 each; the body stands in D1's order; the file was removed before hand-back |
| `git grep -l -E 'pr\.md\|pr\.<lang>'` outside `tests/`, `evals/`, `seal/threads/` and `docs/` | 18 files, as D3 accounts for them |
| `git grep -n -E 'quotes? of .pr\.md.'` outside `docs/`, `tests/` and `seal/threads/`; `git diff --stat origin/release/v0.37.2...HEAD -- skills/implement/orchestration.md` | the four hits phase 3 names; nothing |

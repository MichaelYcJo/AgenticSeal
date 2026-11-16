# Review round 1: 1794797697-a-census-cell-states-an-impossible-result

```seal
target: 598315485 against release/v0.38.2
```

This is the first round, so no earlier record carries a coordinate or a close. The round read every file of the work item whole at `598315485`, the diff from `13290d7f8`, and the files the frame cites, in a `git clone --no-local` of the repository checked out at the target.

## Findings

### 1. The pull request body says neither what the new rule removes nor its prompt budget

```seal
severity: must
location: `seal/threads/1794797697-a-census-cell-states-an-impossible-result/pr.md`, `seal/threads/1794797697-a-census-cell-states-an-impossible-result/frame/plan.md:40-45`
evidence: read `CONTRIBUTING.md:389-430`, `CLAUDE.md:18-21`, `skills/code-review/scripts/pr_body.py:9-17`, `seal/threads/1794797697-a-census-cell-states-an-impossible-result/pr.md:1-8`, `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/pr.md`
```

Why it matters: the diff adds a rule to `agents/framer.md`, and a rule is a mechanism by `skills/core/SKILL.md` *The rule a mechanism is kept against*. `CLAUDE.md:18-21` names `CONTRIBUTING.md` *What a change to a gate must carry* as where a pull request to this repository answers that rule. Its bullet *What it removes* (`CONTRIBUTING.md:402-406`) names "a rule" among the mechanisms whose pull request says what it removes, or why none can go, with what that one caught against what it costs. Its closing paragraph (`CONTRIBUTING.md:426-430`) says the prompt budget and what a change removes "are answered in the pull request body or they are not answered."

The body is `pr.md` followed by what `seal pr-body` copies: the changelog fragment, the plan's `## Phases`, the phase records' paths, the round blocks, `gaps.md`'s two sections and the questions table (`pr_body.py:9-17`). It copies no line of `frame/design.md`, so the `## Removes` answer at `frame/design.md:67-68` never reaches the body. `pr.md` quotes the failure scenario, row A8, the byte count, a gaps row and the title judgment. None of them says that nothing is removed, or why, and no record sentence states the prompt budget, so `pr.md` has nothing to quote for it. Work item `1794383424-the-gate-ships-a-copy-of-one-workflow` shows the form: its `pr.md` quotes a *Judgments of the run* row on what the change carries, prompt budget included.

The fix pass adds one row to `frame/plan.md` *Judgments of the run* and two quotes to `pr.md`. The second quote takes the `## Removes` sentence as finding 2's fix leaves it, so the fix pass writes it after that fix.

```markdown
| 2026-11-16 | What the rule carries as a mechanism, by `CONTRIBUTING.md` *What a change to a gate must carry* | Its prompt budget is zero: it puts no question in front of a person. It removes nothing, for the reason `frame/design.md` *Removes* gives, and its cost is the bytes `trail/phases/phase-1.md` counts | `CONTRIBUTING.md` *What a change to a gate must carry*, the bullets *A prompt budget* and *What it removes* |
```

```markdown
- "Its prompt budget is zero: it puts no question in front of a person." (`frame/plan.md` *Judgments of the run*, the row on what the rule carries as a mechanism)
- "Its catch record is G2 and G3: three searches in one run whose stated results no build could give, two of them visible at the frame's commit and the third, scenario S8's, caught by C3." (`frame/design.md` *Removes*, the why)
```

The second quote is the sentence finding 2's snippet writes at `frame/design.md:68`. Where the fix pass words that sentence otherwise, it quotes the sentence as it then stands.

### 2. The changelog and two frame sentences count two failed cells in #1500, and the frame's own G2 shows three

```seal
severity: should
location: `seal/threads/1794797697-a-census-cell-states-an-impossible-result/changelog.md:3`, `seal/threads/1794797697-a-census-cell-states-an-impossible-result/changelog.md:10`, `seal/threads/1794797697-a-census-cell-states-an-impossible-result/frame/plan.md:44`, `seal/threads/1794797697-a-census-cell-states-an-impossible-result/frame/design.md:68`
evidence: read `seal/threads/1794797697-a-census-cell-states-an-impossible-result/frame/design.md:10`, `seal/threads/1794530293-three-compatibility-paths-still-stand/frame/plan.md` *Judgments of the run* row 2; executed `git show 9dc095ac6:seal/threads/1794530293-three-compatibility-paths-still-stand/frame/design.md` (S8 at line 167) and `git show 9dc095ac6:seal/threads/1794530293-three-compatibility-paths-still-stand/frame/plan.md` (Phases rows at lines 66-67), in the main checkout
```

Why it matters: the changelog fragment becomes the release note, and a person reads its count as the catch record the rule was weighed on. The fragment says "In the run of #1500 the framer wrote two such cells" (`changelog.md:3`), where "such cells" covers *Verifiable how* cells too. Its process row says "Two cells in #1500's frame stated results no build could give" (`changelog.md:10`). The title judgment's grounds say "two frame cells in #1500" (`frame/plan.md:44`). The `## Removes` why says "two searches in one run whose stated results no build could give" (`frame/design.md:68`).

The frame's G2 (`frame/design.md:10`) names three: phase 1's *Verified by* cell, phase 2's *Verified by* cell, and scenario S8's *Verifiable how* cell, whose search `git grep -n 2027-02-07` found #1500's own frame files. #1500's `frame/plan.md` *Judgments of the run* row 2 folds "Phase 2's Verified by cell, `frame/design.md` S8 and R22". At `9dc095ac6`, S8 read "then 2027-02-07 stands only in #1492's records other than its `changelog.md`", and no build could leave that true once #1500's frame quoted the date. The issue counts two because it names only *Verified by* cells. This work widened the rule to *Verifiable how* cells on the strength of S8 (G2, `frame/questions.md:7`), so its own count leaves out the cell that justified the widening. In `frame/design.md:68`, "both visible at the frame's commit" holds for the two re-run in G3. S8 was not visible there, and C3 is what catches it, so that sentence needs the third cell and says why it differs.

```markdown
changelog.md:3, the sentence opening "In the run of #1500":
In the run of #1500 the framer wrote three such cells without running their searches, and the crafters found that none could give its stated result: one matched two names the same plan keeps, another matched lines the design left in place and the work item's own frame, and a scenario's search matched the work item's own frame alone.

changelog.md:10, the Why cell:
Three cells in #1500's frame stated results no build could give, and they cost two crafters' searches for the cause and two orchestrator folds after the build

frame/plan.md:44, the Grounds cell, its first clause:
The framer's definition already asked it to answer by running a command, and three frame cells in #1500 stated results no build could give; ...

frame/design.md:68, the second sentence of the why:
Its catch record is G2 and G3: three searches in one run whose stated results no build could give, two of them visible at the frame's commit and the third, scenario S8's, caught by C3.
```

### 3. The rule's first kind of line, "a line the build removes", leaves no kind for a line the build edits

```seal
severity: should
location: `agents/framer.md:176-179`, `seal/threads/1794797697-a-census-cell-states-an-impossible-result/frame/design.md:55`, `seal/threads/1794797697-a-census-cell-states-an-impossible-result/changelog.md:3`
evidence: read `agents/framer.md:172-188`, `seal/threads/1794797697-a-census-cell-states-an-impossible-result/frame/design.md:18`, `seal/threads/1794797697-a-census-cell-states-an-impossible-result/frame/plan.md:30`; executed `git grep -n -F '0.38.1' 75a725770 -- . ':!seal/threads'` (one line, `.claude-plugin/plugin.json:4`)
```

Why it matters: the paragraph has the framer "account for each line it prints as one of three kinds", and the first is "A line the build removes" (`agents/framer.md:177`). The usual line such a search prints is one the build edits so it no longer matches, and the line itself stays. This work's own search is that case. At `75a725770` it prints `.claude-plugin/plugin.json:4`, which the frame calls "the line the build changes" (`frame/design.md:18`) and "the line this phase changes" (`frame/plan.md:30`). A framer that reads "removes" literally has to file such a line under the second kind, "a line the design keeps". The rule then has it narrow the search until the line no longer matches, or name the line's file as where the search still finds something. The first leaves a search that cannot fail on the line it exists to catch. The second states a result the build will not leave. The verify citation at `agents/framer.md:186-188` might catch the first, but not the second. The frame's C2 (`frame/design.md:55`) and the changelog (`changelog.md:3`) carry the same wording, so the fix reaches all three.

```markdown
agents/framer.md:176-179, rewrapped within 88 columns:
commit `## Grounding` names, and you account for each line it prints as one
of three kinds. A line the build removes, or changes so that the search no
longer matches it, is named by a *Scope* item or a `## Removes` row. For a
line the design keeps, you narrow the search until it no longer matches that
line, or the cell names that line's file. A line in a

frame/design.md:55, the third sentence of C2:
It is a line the build removes, or changes so that the search no longer matches it, under a *Scope* item or a `## Removes` row.

changelog.md:3, the clause opening "account for each line it prints":
account for each line it prints as one the build removes or changes so the search no longer matches it, one the design keeps, or one in a file the cell excludes
```

The `agents/framer.md` snippet ends mid-sentence at the line where the original's line 179 ends, so the fix pass joins it to the unchanged line 180. It reruns `tests/behaviour/test_docs_line_wrap.py` after the edit.

### 4. Two grounding rows cite commits that #1500's squash left on no branch

```seal
severity: should
location: `seal/threads/1794797697-a-census-cell-states-an-impossible-result/frame/design.md:10-11`
evidence: executed `git branch -a --contains 9dc095ac6` and `git branch -a --contains dda87704c` in the main checkout (no ref), `git show 9dc095ac6:...` in the clone (`fatal: invalid object name`), `git ls-remote origin refs/pull/1549/head` (`c02ece3f3`), `git merge-base --is-ancestor` of each commit against `c02ece3f3` (both ancestors); read `tests/text/test_a_cited_commit_outlives_the_squash.py:1-35`, `tests/censuses.py:1238`
```

Why it matters: G2 rests on `git show 9dc095ac6:<that plan.md>`, and G3 on that `git show` and two `git grep` runs at `dda87704c`. #1500 merged as the squash `c97514d6`, and no `main` or `release/*` ref contains either commit. A `git clone --no-local` of the repository lacks `9dc095ac6`. So a reader who later checks G2 and G3, the sealer or the settle in a fresh clone, finds no source. That reader cannot reproduce the frame's main evidence that a run at the frame's commit would have shown both defects. `tests/text/test_a_cited_commit_outlives_the_squash.py` exists for this defect. Its docstring says a citation of a squashed commit "opens in no clone after the merge, and a reader sent to it finds no source", and that three frames reached a release with one. The two rows escape that check because they write the path as a placeholder (`<design.md>`), which `tests/censuses.py#COMMIT_PATH` does not match. The commits survive only under #1500's pull request ref, `refs/pull/1549/head`, which holds both. The fix names that ref where the rows name the commits.

```markdown
frame/design.md:10, the parenthesis closing G2's first cell:
(executed: `git fetch origin pull/1549/head`, then `git show 9dc095ac6:seal/threads/1794530293-three-compatibility-paths-still-stand/frame/plan.md`; #1500's squash, `c97514d6`, left `9dc095ac6` on no branch, and #1500's pull request ref holds it)

frame/design.md:11, the head of G3's first cell:
**G3** The two searches as framed, run at `dda87704c`, the commit #1500's frame names at the head of its *Grounding*, which only #1500's pull request ref, `refs/pull/1549/head`, still holds (executed: `git fetch origin pull/1549/head`, then `git show 9dc095ac6:seal/threads/1794530293-three-compatibility-paths-still-stand/frame/design.md`, then ...
```

## Confirmations

What matched: *Scope* item 1 holds. The paragraph stands at `agents/framer.md:172-188`, directly after the paragraph opening *A question a command answers is answered by running it* (`:155-170`), read. Against `gaps.md` row 2, which names this round as its answerer, the paragraph states C1 at `:173-175`, C2 at `:175-180`, C3 at `:180-183`, C4 at `:183-185`, and C5 at `:185-188`, citing `skills/verify/SKILL.md` *An absence claim is only as good as the search behind it*, a heading that stands at `skills/verify/SKILL.md:50` (read). C2's wording is finding 3. The paragraph never says "census", as G9 asks (read).

What matched: *Scope* item 2 holds. `.claude-plugin/plugin.json` reads `0.38.2`, in `19a111be9`, the commit that adds `changelog.md`. The fragment ends with a `### Process changes` table in the shape of `templates/records/process.md` (read). `git grep -n -F '0.38.1' -- . ':!seal/threads'` printed `.claude-plugin/plugin.json:4` alone at `75a725770` and nothing at `598315485`, exit 1 (executed). This matches G10, the phase row and `trail/phases/phase-1.md`.

What matched: the phase's *Verified by* modules. The orchestrator claimed 148 passed at `19a111be9`. The same command run in the clone at `598315485` gave 148 passed, 5 warnings, exit 0 (executed). The warnings are cited-section notices about other work items' pending rule changes.

What matched: the frame's measured facts, re-run (executed). `wc -c` gives 14,533 bytes for `agents/framer.md` at `75a725770` and 15,759 at `598315485`, and 9,322 and 12,029 for the core and the contract, so 35,884 bytes in all (G14, `trail/phases/phase-1.md`). The longest line is 87 columns before and after (G8, plan *Technical context*). The `## Removes` search prints four lines, none a rule for writing a cell. The G6 search prints nothing, exit 1. The cited sections of G5, G6, G7, G11 and of the plan's rows stand at their files (`git grep -n -F` on each heading).

What matched: `pr.md`'s six quotes stand word for word at their coordinates once whitespace is collapsed: `frame/plan.md:11` twice, `frame/plan.md:24`, `trail/phases/phase-1.md:6` (inside its bold lead-in), `gaps.md:9` and `frame/plan.md:44` (read). The two language keys name English, so no `pr.<lang>.md` is owed, and none stands (executed: `ls pr.*.md`, no match).

What matched: `routing.md` *Why this way* now names no case, and the frame adds none (*Scope*, Out; plan A8). `routing.md`'s version bullet matches `19a111be9`, which holds both the move and the fragment (`git show --stat`, executed).

What matched: `gaps.md` labels the suite, the lint and the format check unverified and names the orchestrator as their answerer. That label is honest: no record claims the broad gate ran.

What did not match, with no finding: `trail/phases/phase-1.md:5` says the paragraph was rewrapped "at 76 columns". `agents/framer.md:179` is 79 columns and `:172` is 76, within the 88 the line-wrap case holds, so no reader acts on the difference. The spawn prompt's account of `598315485` lists the Status cell, two Judgments rows, `pr.md` and a `routing.md` bullet. The commit also rewrites `trail/phases/phase-1.md:6`'s byte figures, from 1,195 to 1,226. That rewrite matches the tree (read: `git show 598315485`).

No new test is in the diff, so no case was read against its group. The chain check printed no notice at a line of `frame/design.md`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a framer spawned from 0.38.2 on runs the search before it writes the cell; no paid run was made | `seal/threads/1794797697-a-census-cell-states-an-impossible-result/gaps.md:9` | the settle of 0.38.2, reading the next frames' `## Grounding` |
| The full suite, the repository-wide lint and the format check at HEAD (contract rule 2) | `seal/config.json` `Broad gate` | the orchestrator, once the rounds settle |
| G4's count of 11 phase rows in 9 plans, a sample the frame labels as one; the round did not recount it | `seal/threads/1794797697-a-census-cell-states-an-impossible-result/frame/design.md:12` | nobody owes it: no claim of the build rests on the number |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_release_hygiene.py -q`, in the clone at `598315485` | 148 passed, 5 warnings, exit 0 |
| `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py tests/text/test_a_record_carries_no_comment.py tests/behaviour/test_every_shipped_agent_and_document_is_measured.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/text/test_the_rules_have_one_owner.py -q`, in the clone | 93 passed, 8 skipped, exit 0: no module that reads `agents/` or the records refuses the diff, and the squash check does not read finding 4's placeholder citations |
| `git grep -n -F '0.38.1' 75a725770 -- . ':!seal/threads'`, then the same at `HEAD` | one line, `.claude-plugin/plugin.json:4`; then nothing, exit 1 |
| `git branch -a --contains 9dc095ac6`, the same for `dda87704c`, in the main checkout; `git ls-remote origin refs/pull/1549/head` | no ref for either commit; the pull request ref at `c02ece3f3`, which both commits are ancestors of |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.38.2 --root <the branch worktree> --worktree`, before the record | exit 0; it named the missing round record, gate record and guarantee, and no notice on `frame/design.md` |

# Review round 2: 1795132764-a-pr-body-can-pass-githubs-length-limit

```seal
target: 8b397ac7f, fixes 6a135ec96..8b397ac7f
```

This is a verifying round over round 1's fix pass. It reviewed the range `6a135ec96..8b397ac7f` in a `git clone --no-local` of the repository at `8b397ac7f`, in the round's scratch directory. The range holds round 1's record and its four close blocks (`925283279`, `3939e69a8`), the merge of `origin/release/v0.38.3` after #1557's squash `c63d0b070` (`33961b5ad`), the fix pass's five commits (`3536256a5`, `0a36e832f`, `dae62ca25`, `6d00248ed`, `9f34ceb37`), and the orchestrator's fold of five frame statements (`8b397ac7f`). The merge base with `origin/release/v0.38.3` is now `c63d0b070`.

Each record the proofer's step 3 names was read whole at `8b397ac7f`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md`. No `pr.<lang>.md` stands, since both language keys of `seal/config.json` read `English` (read).

Carried from round 1 and not established again: the coordinates of `_folded`, `_room` and `TOO_LONG` in `skills/code-review/scripts/pr_body.py`; the mark's room of 114 units, from round 1's probe and `frame/design.md` G15's 112 for the line alone; and round 1's `## Not judged` row on how GitHub counts a line end, which stands below unchanged. Every verdict below was reached this round.

## Findings

### 1. The pull request body states no failure direction, prompt budget or reading for a change to two gates

```seal
severity: should
location: `seal/threads/1795132764-a-pr-body-can-pass-githubs-length-limit/pr.md`, `seal/threads/1795132764-a-pr-body-can-pass-githubs-length-limit/frame/plan.md:45-49`
evidence: read `CONTRIBUTING.md:373-430`, `docs/running/what-a-script-gates.md:56`, `docs/running/what-a-script-gates.md:66`, `seal/threads/1795132764-a-pr-body-can-pass-githubs-length-limit/pr.md:1-10`, `seal/threads/1795132764-a-pr-body-can-pass-githubs-length-limit/frame/design.md:110`; executed `git grep -n -i "direction\|block more\|allow more\|prompt budget\|question in front\|no gate\|What it reads\|platform" -- seal/threads/1795132764-a-pr-body-can-pass-githubs-length-limit`
```

Why it matters: this round found the gap while reading `pr.md` whole, as the definition asks, and it lies outside the fix diff. `docs/running/what-a-script-gates.md` lists every check that gates. It lists `seal pr-body` and `seal pr-body --check` (`:66`), and it lists the body arm of `chain_check.py` (`:56`). This work changes what both of them accept. `seal pr-body` now exits 1 on a body that still passes the limit with every section folded, and before it wrote that body. The body arm now refuses the unfolded body of records past the limit as D1 and D4 count it, and before it accepted that body. That includes a body GitHub would keep, within the mark's room or in the band outside the Basic Multilingual Plane. The project's `CLAUDE.md` names `CONTRIBUTING.md` *What a change to a gate must carry* as where a pull request to this repository answers *The rule a mechanism is kept against*. That section asks the pull request to say "whether the change makes the gate block more or allow more, and why that direction is the cheaper mistake here" (`CONTRIBUTING.md:383-388`). It asks for "how many times the change puts a question in front of a person" (`:389-398`), and for the form the gate reads and what it names as not read (`:410-418`). It closes with "Both are answered in the pull request body or they are not answered" (`:428-429`).

`pr.md` holds eight quotes and a `Closes` line (`pr.md:1-10`). None of them answers any of these. The search above finds one sentence in the records that touches them. It is `frame/design.md:110`: "The fold adds one constant, `LIMIT`, and one fixed line, `FOLDED`, and no gate, check or mark." It sits in `## Removes`, which the body's copy does not carry and `pr.md` does not quote. Earlier work items answered the list with a row of `frame/plan.md` *Judgments of the run* and a quote of it in `pr.md`. One read "The `durations` job's change to a gate: its failure direction is allow more ... its prompt budget is zero". The pr_body work item of #1478 quoted "no gate is added or removed, the body arm reads the same function" (executed: `git log -- 'seal/threads/*/pr.md'`, read). The *Test seen red* item is answered already, by `trail/phases/phase-1.md`, which the body copies.

`frame/plan.md` *Judgments of the run* is a frame table, and a finding located in `pr.md` is the orchestrator's to repair (`skills/code-review/orchestration.md:421-424`), so the orchestrator owns both repairs. Add one row to `frame/plan.md` *Judgments of the run*:

```markdown
| 2026-11-20 | The change to two gates carries what a gate change must | `seal pr-body` and the pull request's body arm are gates (`docs/running/what-a-script-gates.md` *The checks*). The failure direction is block more: `seal pr-body` exits 1 on a body that still passes the limit with every section folded, which it wrote before, and the body arm refuses the unfolded body of records whose body, counted in UTF-16 code units with the seal mark's room, passes the limit, which it accepted before. That is the cheaper mistake: a wrong deny stops the run at `seal pr-body`, before the seal, naming the files to shorten, while the allow it replaces let `gh pr create` refuse the body after the seal (#1559). The prompt budget is zero, since no step the change adds asks a person. The gates read one fact more, the composed body's length against `LIMIT`, and name no line as not read for it. What goes is `frame/design.md` *Removes* | `CONTRIBUTING.md` *What a change to a gate must carry* |
```

Then add a quote of that row's Grounds cell to `pr.md`, word for word, above the `Closes` line:

```markdown
- "`seal pr-body` and the pull request's body arm are gates (`docs/running/what-a-script-gates.md` *The checks*). The failure direction is block more: `seal pr-body` exits 1 on a body that still passes the limit with every section folded, which it wrote before, and the body arm refuses the unfolded body of records whose body, counted in UTF-16 code units with the seal mark's room, passes the limit, which it accepted before. That is the cheaper mistake: a wrong deny stops the run at `seal pr-body`, before the seal, naming the files to shorten, while the allow it replaces let `gh pr create` refuse the body after the seal (#1559). The prompt budget is zero, since no step the change adds asks a person. The gates read one fact more, the composed body's length against `LIMIT`, and name no line as not read for it. What goes is `frame/design.md` *Removes*" (`frame/plan.md` *Judgments of the run*, the row on the change to two gates)
```

`CONTRIBUTING.md:402-409` also asks a pull request that adds a mechanism to name what it removes. The frame holds that the change adds none (`frame/design.md:110`). If the orchestrator keeps that reading, the row's last sentence answers the item. Where it would rather show the reader the frame's own words, it can quote that sentence of `frame/design.md:110` in `pr.md` as well.

```seal
verdict: fixed 87769186e
answer: fixed in 87769186e, the orchestrator's repair, read by the fix pass against this finding: `frame/plan.md` *Judgments of the run* gains the row "The change to two gates carries what a gate change must", judged against `CONTRIBUTING.md` *What a change to a gate must carry*, and `pr.md` quotes its Grounds cell word for word above the `Closes` line. The cell gives the failure direction, block more, at both `seal pr-body` and the body arm, with why that is the cheaper mistake. It gives the prompt budget, zero, and the one fact more both gates read, which they compute and never read from a line, so no line is named as not read. `pr.md` also quotes the `frame/design.md` *Removes* sentence "The fold adds one constant, `LIMIT`, and one fixed line, `FOLDED`, and no gate, check or mark.", which stands word for word at HEAD, for the item on what a mechanism removes. The commit changes `pr.md` and `frame/plan.md` alone, both paths the finding names.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `TOO_LONG` now reads "the body, counted with room for the seal mark's line whether or not it is written, would be {length:,} characters ... past GitHub's 65,536" (`skills/code-review/scripts/pr_body.py:307-316`). Its comment says the length is the measure with `_room` in it. `_folded`'s docstring says "naming its length with ROOM counted" (`pr_body.py:958`). The number printed is still the measure with the room, and the line now says so, so the line no longer tells a person something false about the body GitHub would get. This covers every statement round 1's grounds listed: the expected line of S5's case (`tests/skills/test_pr_body.py:1665-1673`) and its docstring, `changelog.md:5`, and D5 at `frame/design.md:74`, which the orchestrator folded in `8b397ac7f`. Where the mark is written, `_room` returns 0 and the mark's line stands in the measured body, so the line's "whether or not it is written" holds there too (`pr_body.py:934-944`, read). Executed: the narrow run of the three modules passed, and with the room clause taken out of `TOO_LONG` in the clone, S5's case `test_refuses_a_first_part_and_changelog_past_the_limit` failed on its expected line, the diff showing the clause.

```seal
confirms: round-1#2
```
What holds: the *Updating* paragraph (`changelog.md:8`) no longer says that no open pull request changes. It says a body folds where, counted in UTF-16 code units with the mark's room, it would pass 65,536. It names both bands round 1 found, and says the next `seal pr-body` run before a `gh api -X PATCH` writes the body folded. That rerun is what `skills/code-review/orchestration.md:443-444` asks for (read). The paragraph's last sentence now covers updating a pull request as well as opening one. The same class stood in the first bullet's heading, which `9f34ceb37` gave the room (`changelog.md:3`), in `frame/plan.md:43` *Operational impact*, and in the first sentence of the `## Rule changes` add (`frame/design.md:83-86`). The orchestrator folded those two frame statements in `8b397ac7f`. Each one now states the room and the two bands where it states the trigger. Read. Method: `git grep -n -i` for `GitHub's limit`, `65,536`, `65536`, `past the limit`, `passes the limit` and `length limit` over the tree, outside the round records and this frame (executed). That is a search on wordings, so it is a sample. It found no other statement that a body folds only past GitHub's limit. `pr_body.py:68-76` states the room in the sentence after the trigger.

```seal
confirms: round-1#3
```
What holds: the sentence at `skills/code-review/orchestration.md:434-438` now lists "the work item's directory with the files to repair named in the line" among the places a `refused:` line names. Its repair reads "repair that record or file or write that key". It was rewritten in place, and no sentence was added. That fits the amended Out bullet at `frame/design.md:43`. The close's added `location:`, `changelog.md`, carries the fragment's new bullet (`changelog.md:6`) and the `### Process changes` table (`changelog.md:10-14`). `docs/layout/the-record-layout.md:51-53` asks for that table of a diff that changes a `skills/*/orchestration.md` file, in the shape `templates/records/process.md` gives. The table has that shape, and its Source cell links the issue, as the release's other rows do (read). Method: `git grep -n -i` for `pr-body` within two lines of `refus`, `exit 1` or `record's file`, over `docs`, `skills`, `agents`, `templates`, `CONTRIBUTING.md` and `README.md` (executed). That is a search on wordings, so it is a sample. It found no other list of the places a `refused:` line of `seal pr-body` names. `agents/sealer.md:67-71` acts on "the first line the command printed" and lists no place. `docs/running/what-a-script-gates.md:66`'s *Fails on* cell lists the language-key refusals alone. The frame's `change` op leaves that cell for the settle.

```seal
confirms: round-1#4
```
What holds: `Test_compose.test_refuses_a_first_part_alone_past_the_limit` (`tests/skills/test_pr_body.py:770-784`) stands as round 1's snippet, with one docstring sentence on how it was seen red. Executed: with `which` always "one of them" in the clone, the case failed on its `endswith`. The printed line ended "so one of them is shortened", and S5's three-file case is not affected by that mutant. The case holds the one-file branch at `pr_body.py:984`, which no other case of `Test_compose` or `Test_main` held. S5 pins the three-file form alone (read). So it covers something its group did not. `gaps.md:10-12` `## Not done` now reads `nothing`. That is the spelling `skills/implement/SKILL.md` *4. The closing memo* gives for nothing left. The paragraph that left was a decision of `## Not done`, not a `## Not verified` row, so no `closed` was owed (read).

What matched: the orchestrator's fold in `8b397ac7f`, read against HEAD. *Scope* item 1 (`frame/design.md:30`) counts the mark's room, as `pr_body.py:959-970` adds `room`. The Out bullet (`frame/design.md:43`) names the one sentence of `orchestration.md` that was amended, which `6d00248ed` changed. D5 (`frame/design.md:74`) gives the room and the one-file wording, as `pr_body.py:311-316` and `:984` write them. The add's first sentence (`frame/design.md:83-86`) and `frame/plan.md:43` state the trigger as the code holds it. Read.

What matched: the merge `33961b5ad` meets this work in no file. The `comm -12` of `git diff --name-only fab41dc91 c63d0b070` against `git diff --name-only c63d0b070...HEAD` printed nothing (executed). It moves `.claude-plugin/plugin.json` to 0.38.3, the version `changelog.md:8` and `routing.md:23` name (read). A `git grep` for `efficient development` and `through the workflow` over this work's changed files matches only `frame/design.md:24`, G16's own record of that search (executed). `routing.md:20`'s "every repository that installs the workflow" names the GitHub Actions workflow, the sense #1557 left that word (read). `frame/plan.md:35-39` *Overlap with the release* calls #1557 "sealed and open" at `e6d1945a0`. That is a statement of the commit the framer read. Its conclusion, that the merge costs no conflict, holds at `33961b5ad`.

What matched: each of the eight quotes of `pr.md` stands word for word, whitespace collapsed, in the file it names (executed: a script over `pr.md` against `frame/questions.md`, `frame/plan.md` and `trail/phases/phase-1.md`, eight of eight found). Each also stands at its coordinate: row Q1's Question, Default and Options cells (`frame/questions.md:14`), row 3's Verdict and Failure scenario cells (`frame/plan.md:19`), the second and seventh items of `trail/phases/phase-1.md` (`:6`, `:11`), and the title row of *Judgments of the run* (`frame/plan.md:49`). Read.

What matched: the narrow run of the three modules the phase row names passed at `8b397ac7f`, with 355 cases, one more than round 1's 354. That one is finding 4's case (executed).

What matched: round 1's `## Not judged` row on the broad gate stays honest. `gaps.md:7` labels the suite, the lint and the format check as not verified and names the orchestrator, and no record of the range claims otherwise (read).

Two sentences of the range read loosely and mislead no one, so neither is a finding. `changelog.md:3` says a body with no mark folds "once it comes within that line's length of the limit". The room is the line and two units more, 114 against 112. S5's docstring says "the seal mark's room counted and said to be" (`tests/skills/test_pr_body.py:1646`). `frame/design.md:71` still lacks the full stop between "copies from it" and "It names no commit", as round 1 noted, and the fold did not touch it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether GitHub counts a line end as one character, or counts the body after turning each LF into CRLF. This row is carried from round 1 unchanged. A body of many lines folded to 65,536 units would be refused under the second count | `seal/threads/1795132764-a-pr-body-can-pass-githubs-length-limit/frame/questions.md:14` | a measurement by whoever may post to a scratch pull request, with a body of many short lines added to Q1's |
| The full suite, the repository-wide lint and the format check at `8b397ac7f`. This round ran only the three modules below | `seal/config.json` `Broad gate` | the orchestrator's broad run once the rounds settle, then the sealer's spawn |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pr_body.py tests/skills/test_chain_check.py tests/evals/test_rule_cases.py -q -p no:xdist`, in the clone at `8b397ac7f` | exit 0, 355 passed |
| `bin/test tests/skills/test_pr_body.py -q -p no:xdist -k "first_part_alone_past_the_limit or first_part_and_changelog_past_the_limit"`, with `TOO_LONG`'s room clause taken out and `which` made always "one of them" | exit 1, 2 failed. The one-file case failed on its `endswith`, the line reading "so one of them is shortened". S5's case failed on its expected line, the diff showing the room clause. The clone was restored with `git checkout`, and `git status --short` printed nothing |
| A Python script that reads each quote of `pr.md`, collapses whitespace, and looks for it in the file it names | eight of eight found |
| `comm -12` of `git diff --name-only fab41dc91 c63d0b070` against `git diff --name-only c63d0b070...HEAD`, both sorted | no line |
| `git grep -n "efficient development\|through the workflow"` over the files `git diff --name-only c63d0b070...HEAD` lists | one line, `frame/design.md:24` |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.38.3 --root <the branch worktree> --worktree`, before this record | exit 0. It named round 1's findings 1, 3 and 4 and `3536256a5` as owing a verifying round. It named `trail/gate.md` and `guarantee.md` as absent. It printed no notice at a line of `frame/design.md` |

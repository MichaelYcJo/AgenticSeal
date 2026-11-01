# Review round 2: 1793516191-a-wording-pin-module-leaves-by-rule-changes

```seal
target: bce060a1, fixes a6c5fb76..bce060a1
```

The round is the verifying round after round 1. It reviews the fixes from round 1's target `a6c5fb76` to `bce060a1` on `refactor/1197-a-wording-pin-module-leaves-by-rule-changes`. The base is `origin/release/v0.27.1` at `ad4556f4`. The fix range holds six commits. `49f3b00b` is the orchestrator's: round 1's record and the plan's last judgment row. `c66f09cf` is the framer's reframe. `417a11d2` is the fix pass on `trail/phases/phase-1.md`. `953c6e54` and `15eb91e7` are phase 2. `bce060a1` adds round 1's close blocks. The branch changes no path outside this work item's directory (executed: `git diff --stat ad4556f4 bce060a1 -- . ':!seal/threads'` printed nothing). No `seal/parity.md` is declared, so the round block names no original.

The round answers each of round 1's six closes and reads the reframe as new work. The reframe is the fix for findings 2 to 6, so a defect it brought into a unit it wrote takes a `regression:` line. The round weighs three things hardest. The first is the `add` in `## Rule changes`: whether it states a true rule and cites the core rightly. The second is whether the line-18 `to` still holds with the `add` beside it. The third is whether *The successor issue* resolves outside this directory and is complete. It also judges phase 2's account of S3's module list.

The round carried these facts from round 1 and did not establish them again. The first is G8's coordinates in `tests/skills/test_broad_gate.py` (`:2445`, `:2460-2461`, `:2472`, `:2739`, `:2757`). The line-33 item is the same at `c66f09cf` as at `a6c5fb76`, so the round did not run S4 again. The second is the coordinates of the 22 rows round 1 confirmed in *What each case held*. The third is the line spans P3 gave for the two sections. The round opened again, and judged again, the coordinates of the rows and the bullets the reframe changed. The diff adds no test, so no test is read against its group.

## Findings

### 1. The `add`'s last sentence says no case sweeps the tree for another word, which is false from the settle until the successor removes the module

```seal
severity: should
location: `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:126-130`
evidence: read `tests/behaviour/test_one_word_one_meaning.py:953-999`, `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/plan.md:19`, `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/plan.md:23`, `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/plan.md:40`, `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:126-130`
regression: round-1#2
```

The unit is the `add` item of `## Rule changes` (`frame/design.md:126-130`), which the reframe wrote for round 1's finding 2. Plan row A1 says every sentence in the tree stays true at every commit, row A5 keeps the module's removal out of the settle's own pull request, and design G7 asks the `add` to name the proofer as the reader of the words. The reframe named that reader and also wrote a sentence about the tree as it will stand after the removal, so the defect comes from grounds written as a fact about the tree instead of a fact about the rule's reader.

Why it matters: the settle writes the `add` into `docs/the-pact.md` while `tests/behaviour/test_one_word_one_meaning.py` still runs (`frame/plan.md:40`, and A5 at `:23`). From that merge until the successor's change, the policy document says "No case sweeps the tree for another word" while case 24, `test_no_live_text_says_the_word_0_19_0_renamed`, reads every tracked file for the 0.18.x word (`tests/behaviour/test_one_word_one_meaning.py:953-999`). The owner calls the settle, and the successor waits in `release: 0.27.3`, so nothing bounds that time. This is the kind of false fact plan A2 rejects for the places outside `docs/` (`frame/plan.md:20`). A1's verdict, "Every sentence in the tree stays true at every commit" (`frame/plan.md:19`), would not hold.

The grounds:

- The claimed state: the `add`'s sentence reads "No case sweeps the tree for another word, because a case that refuses a word wherever it stands turns red where the meaning has not changed" (`frame/design.md:129`).
- The tree in the interval: this round wrote the four operations into `docs/` in its scratch clone, as the settle would, and ran the module there. It passed, so case 24's sweep runs beside the added sentence (executed: the S3 command under `## Probes`).
- The rest of the rule is true at every commit. The `add`'s first three sentences name the reader and what it reads, and none of them states what the suite holds. Its citation is also right: `skills/core/SKILL.md:36-45` says a script that answers "these differ" where the meaning is the same is the worst result the workflow can give. The `add`'s reason restates that point for a word sweep (read).
- Neither probe could catch this. P2 checks for a copied passage and for the old word, and P3 checks the parse and each `from`. Phase 2 ran checks over the text and did not read the sentence against the tree in the interval.

The fix makes the last sentence a fact about the rule's reader. That fact is true while the module runs, because the module is not on this rule's check line, and it stays true after the module goes. The citation stays as it is. P2 and P3 run again over the new `to`.

```markdown
- add
  file: docs/the-pact.md
  section: The words
  to: **The three names are the owner's, and a text this plugin ships that names one of them another way is the proofer's to find at review, the word 0.18.x used for a signer included.** That holds for code, its comments and the names of its tests as it holds for prose. A text that spells the 0.18.x header in order to read it, as the rule on a pact headed with that word says, names no signer another way. The reader is the proofer and not a case, because a case that refuses a word wherever it stands turns red where the meaning has not changed (`skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*).
    check: none reader: the proofer at review
```

### 2. The successor's *How the list was made* bullet names `49f3b00b`, a branch commit that a clone of the base will not hold after the merge

```seal
severity: should
location: `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:94`
evidence: executed `git ls-remote origin 'refs/heads/chore/1167*' 'refs/heads/*1214*' 'refs/heads/*1237*' 'refs/heads/*1226*'`, `git log --oneline -8 --first-parent origin/release/v0.27.1`, `git diff --stat ad4556f4 bce060a1 -- . ':!seal/threads'`, `git grep -n -w -f <(the module's 55 top-level names) ad4556f4 -- . ':!seal/threads' ':!tests/behaviour/test_one_word_one_meaning.py' ':!.test_durations'`
regression: round-1#5
```

The unit is the *How the list was made* bullet of *The successor issue* (`frame/design.md:94`), which the reframe wrote for round 1's finding 5. The design's own preface says every coordinate in the body resolves outside this directory, at a named commit or at the `v0.27.1` tag (`frame/design.md:89`), and the orchestrator files the body as written. The reframe wrote the bullet with the branch commit `49f3b00b`. The defect came from round 1's own paste-ready text, which named the branch commit `a6c5fb76` the same way.

Why it matters: the successor's builder starts from a clone of the base after the settle. In that clone the commit where the search was run does not exist, so `git grep ... 49f3b00b` refuses with a bad revision, and the claim cannot be re-run where it was made.

The grounds:

- Work-item pull requests reach a release branch as one squashed commit each. The first-parent history of `origin/release/v0.27.1` is one commit per pull request, each titled with its number, such as `ad4556f4 ... (#1242)` (executed). The branch's own commits stay on the branch.
- The branches of merged work items are gone from the remote. `git ls-remote` lists no branch for #1167, #1214, #1237 or #1226 (executed). The repository's `delete_branch_on_merge` is `false` (executed: `gh api repos/:owner/:repo --jq .delete_branch_on_merge`), so the branches were removed some other way. Either way, after the merge `49f3b00b` is reachable only through the pull request's own ref, which a clone does not fetch.
- `ad4556f4` gives the same result and stays reachable. A release branch reaches `main` by a merge commit (executed: `git log --oneline --first-parent -6 origin/main`). The branch changes no path outside `seal/threads` (executed: the `git diff --stat` above printed nothing). The 55-name search at `ad4556f4` lists the same one line as at HEAD, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:77` (executed, both revisions).
- No other commit in the body names the branch. *What the removal owes* names `ad4556f4`, and every other coordinate is a path in the tree or at the `v0.27.1` tag (read: `frame/design.md:91-98`).

The fix names the base in the branch commit's place. The rest of the bullet stays as it is:

```markdown
- **How the list was made.** The module was taken apart into its 55 top-level names: its 24 cases, its 28 constants and its helpers `flat`, `pact_texts` and `without_the_policy_span`. Each name was searched with `git grep -n -w` outside the module, `.test_durations` and `seal/threads`, at `ad4556f4`. Apart from other units named `flat`, which import nothing from the module, the search lists one line, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:77`, which is on the list above. Beside it, `git grep -n one_word_one_meaning -- . ':!seal/threads'` lists the places above and the 24 rows of `.test_durations`, and `seal rules --check` with the module deleted, in a clone where the `to` values stood in `docs/`, refused one line, `skills/writing-style/SKILL.md:276`. For paths and identifiers the list is whole. No search lists a sentence that names the module in prose alone, with no path or identifier. That part is a sample, and this build's reviewer reads for it.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `trail/phases/phase-1.md:18` names the worktree as `<the worktree>` and the clone under `<scratchpad>/...` (read). `tests/test_censuses.py` passed at `bce060a1` as part of this round's S3 command in its scratch clone, whose records are the branch's (executed). A `grep -rn` over the work item's directory for `/Users/`, `/home/`, `/private/` and the session's scratch directory name listed only lines holding the census's own `/Users/x/` placeholder (executed). The boundary paragraph at `phase-1.md:57` now names `tests/test_censuses.py` and says phase 1 left it out (read).

```seal
confirms: round-1#2
```
What holds: the reader of the pact's words now stands on a check line. Claimed: the line-18 `to` is `check: tests/hooks/test_config.py`, and the `add` ends `check: none reader: the proofer at review`. Found, executed in this round's scratch clone with the four operations written into `docs/` by the `Edit` tool: `bin/seal rules --check` exited 0 and printed `all 282 check lines in 55 rule files hold`. `bin/seal rules docs/the-pact.md` lists *The words* at line 17 with `tests/hooks/test_config.py` alone, line 30 with `tests/skills/test_pact_check.py` and `tests/hooks/test_config.py`, and line 41 as `no target, read by the proofer at review`. Phase 2's claims at `trail/phases/phase-2.md:9` and `:11` match these numbers. The defect the round found in the `add`'s last sentence is finding 1. It does not undo this close, which was about where the reader stands.

```seal
confirms: round-1#3
```
What holds: row 2 (`frame/design.md:61`) cites `tests/hooks/test_mode_gate.py:318` and its assertions at `:330-339`, and says that case reads no README. The case runs the hook from two work trees and asserts deny, ask, then silent (read: `tests/hooks/test_mode_gate.py:318-339`). Row 2 places the README's spelling of each grain, and the absence of "Fires once per session,", with the proofer. Row 7 (`frame/design.md:66`) places the second assertion at `tests/hooks/test_routing_edit_gate.py:296-299`. That case is parametrised over both `Review` answers, under `docs/the-review-and-parity-arms.md:34-37`, which says an edit goes ahead for either answer (read).

```seal
confirms: round-1#4
```
What holds: every coordinate the body gives resolves outside this directory, except the branch commit finding 2 names, which is new with the bullet finding 5's fix wrote. The precondition is the search `git grep -n one_word_one_meaning -- docs`. Phase 2 ran it with the operations written and it listed nothing (`trail/phases/phase-2.md:24`, claimed). This round reproduced the operations, and `bin/seal rules --check` passed with no `docs/` line naming the module (executed). The tag paths will resolve. A release tag holds its work items' directories: `git cat-file -e v0.27.0:seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md` succeeded (executed). The settle that removes them runs at a later release's step 2b. `gaps.md:9` is the third *Not verified* row the body cites (read).

```seal
confirms: round-1#5
```
What holds: the design's bullet (`frame/design.md:94`) names the 55 top-level names, and `trail/phases/phase-1.md:55` says phase 1's search took 26 of them and was a sample (read). Round 1's executed line ran again in this round's clone at `bce060a1`, with the names taken from the module by `grep -oE`. There are 55 names, and outside the lines holding `flat` the search lists one line, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:77` (executed). It lists the same line at `ad4556f4` (executed).

```seal
confirms: round-1#6
```
What holds: the successor goes to `release: 0.27.3` everywhere an agent acts on it: `frame/questions.md:9`, `frame/plan.md:13`, `:42` and `:49`, and `frame/design.md:89` and `:92` (read). Milestone 79's description reads "A patch: it fixes and removes" and "the wording-pin item follows #1197" (executed: `gh api repos/:owner/:repo/milestones/79 --jq '.title,.description'`). #1233 is open in `release: 0.27.3` (executed: `gh issue view 1233 --json title,milestone,state`). The first judgment row, `frame/plan.md:48`, still says "Q1 takes its default, `release: 0.27.2`" and cites `frame/questions.md` Q1, which no longer holds a row by that name. *Judgments of the run* is a dated log, and the next row, `:49`, records the move and its grounds. A reader of the log meets the later judgment, so the round raises no finding on the older row.

```seal
confirms: none
```
What matched: the line-18 `to` still holds with the `add` beside it. Once the sentence leaves, the definition paragraph states what the pact is, who signs it and where `seal pact` reads the signers. `tests/hooks/test_config.py`'s `Test_pact_signers` reads the `Signer` table of a pact's text, and the template's (read: `tests/hooks/test_config.py:1517-1554`). The words the sentence named stand as the `add`'s own rule, and the reader is on a check line. Rows 22 to 24 cite the `add` (read: `frame/design.md:81-83`). The `add` takes the pact's three names, the pact, the signer and the pact's repository, from the definition paragraph two paragraphs above it. Case 22's comment names the same three (read: `tests/behaviour/test_one_word_one_meaning.py:725-733`).

```seal
confirms: none
```
What matched: the `add` covers what the module's three pact cases left alone. Case 24 skips the records, the compatibility cases' header cell, `hooks/lib/config.py#renamed_header` and the policy span of *The words* (read: `tests/behaviour/test_one_word_one_meaning.py:921-999`). The `add`'s third sentence covers a text that spells the header in order to read it. The span is the rule it points to. The records are history, and a settle removes them. Outside the records and the module, `git grep -i -l signator` lists only the four compatibility files, `hooks/lib/config.py` and `docs/the-pact.md` (executed). No module outside the one being removed sweeps for the pact's other words (executed: `git grep -n -i -E 'pact repo|keeper|signator' -- tests evals`, outside the module, lists only the compatibility files' header strings).

```seal
confirms: none
```
What matched: *The successor issue* is complete against #1197's list. #1197's *What the removal owes* lists six bullets (executed: `gh issue view 1197 --json title,body,milestone,state`). This pull request answers the first, the three rule changes. The body names every other one: both writing-style sections, both pins, both script comments, the docstrings as six lines in four files, and the 24 `.test_durations` rows. At `ad4556f4`, `git grep -n one_word_one_meaning` lists exactly those lines outside the three `docs/` lines and the module's own line 950, and 24 rows in `.test_durations` (executed). The sentence at `skills/writing-style/SKILL.md:245-248` is the one that names the module (executed: `git show ad4556f4:skills/writing-style/SKILL.md`). The body also states the precondition, the order, the method, the open suite run, the README question and *Done when*, so no part of it relies on this directory.

```seal
confirms: none
```
What matched: S3's list now names its open part, as contract rule 12 asks. Claimed: the four modules phase 2 added came from two spellings of how a module reaches the tree, the list is a sample, and the full suite is `gaps.md`'s first row (`trail/phases/phase-2.md:5`, `gaps.md:7`). Found: the method is a search for spellings, so the list cannot be whole by that method. The run that would make it whole is the full suite with the `to` values in `docs/`, and contract rule 2 keeps that run from the crafter. `gaps.md:7` hands it to the settling session's step 8, which runs the broad gate. This round widened the sample to every module under `tests/` that walks, globs or lists files and mentions `docs`, tracked files or `ls-files`. That gave 29 more modules, and with the four operations written they passed: `1894 passed, 8 skipped` (executed, `## Probes`). The list is still a sample, because a module that reaches `docs/` through a helper it imports spells none of those words. Design S3 still lists thirteen modules. The departure stands in the phase record, which is where stage 1 reads a build's departures from the frame.

```seal
confirms: none
```
What matched: S3 and phase 2's four modules pass with the four operations written. Claimed: `1110 passed, 1 skipped` and `143 passed` (`trail/phases/phase-2.md:13`, `:15`). Found, executed in one command in this round's clone: `1253 passed, 1 skipped`, which is the two counts added together.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD, `unverified`. This round ran the narrow modules named under `## Probes` and no full suite | `seal/config.md` | the orchestrator's broad run after the rounds settle, then the sealer |
| Whether the reader of the writing-style line reaches `README.md` and `README.ko.md`, carried from round 1 and still in the body's *The README's reader* bullet | `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:96` | the framer of the successor issue |
| The `to` values in the settle's own words, and the full suite with them in `docs/` | `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/gaps.md:7-8` | the settling session, at `skills/settle/SKILL.md` *The settling session's procedure* step 8 |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local -q <the worktree> <scratchpad>/1793516191-a-wording-pin-module-leaves-by-rule-changes/round-2/clone`, then `git checkout -q bce060a1` | the clone stood at `bce060a1` |
| the four operations written into the clone's `docs/the-pact.md` and `docs/the-broad-gate.md` with the `Edit` tool, as the design spells them; `git diff --stat` | `docs/the-broad-gate.md` 2 lines changed; `docs/the-pact.md` 15 insertions, 5 deletions |
| `bin/seal rules --check`, exit code read directly | `exit=0`; `all 282 check lines in 55 rule files hold` |
| `bin/seal rules docs/the-pact.md` | *The words*: line 17 `tests/hooks/test_config.py`; line 30 `tests/skills/test_pact_check.py`, `tests/hooks/test_config.py`; line 41 `no target, read by the proofer at review` |
| `bin/test` over S3's thirteen modules and phase 2's four, one command, `-q -p no:randomly` | `exit=0`; `1253 passed, 1 skipped` |
| `bin/test` over 29 modules that walk, glob or list files and mention `docs`, tracked files or `ls-files`, outside the seventeen above | `exit=0`; `1894 passed, 8 skipped` |
| `git grep -n -w -f <(the module's 55 top-level names)` at HEAD and at `ad4556f4`, outside the module, `.test_durations` and `seal/threads`, lines holding `flat` left out | one line at each revision: `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:77` |
| `git ls-remote origin` for the branches of #1167, #1214, #1237 and #1226; `gh api repos/:owner/:repo --jq .delete_branch_on_merge` | no branch listed; `false` |

The clone, with the `.venv` that `bin/test` built in it, and the four logs written beside it, the chain check's among them, under `<scratchpad>/1793516191-a-wording-pin-module-leaves-by-rule-changes/round-2/` are removed.

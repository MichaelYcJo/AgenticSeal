# Review round 1: 1793516191-a-wording-pin-module-leaves-by-rule-changes

```seal
target: a6c5fb76 against origin/release/v0.27.1
```

The round reviews the branch `refactor/1197-a-wording-pin-module-leaves-by-rule-changes` at `a6c5fb76` against `origin/release/v0.27.1` at `ad4556f4`. The diff holds this work item's six records and nothing else (executed: `git diff --stat ad4556f4...HEAD`). No earlier round exists, so no fact is carried and every coordinate below was opened this round. No `seal/parity.md` is declared and the diff touches no path outside `seal/`, so the round block names no original.

The work changes no code, so the axes are the work's own. The first is whether each `from` stands in its section and each `to` states a rule that holds. The second is whether *What each case held* places every assertion of each of the module's 24 cases, at a holder that holds it. The third is whether changing nothing outside `docs/` now is right. The fourth is whether *The successor issue* works as a body filed on its own. The fifth is whether the records pass the checks that read them. The grounds are issue #1197's body and comment (executed: `gh issue view 1197 --json title,body,milestone,state`, `gh issue view 1197 --comments`) and milestone 77's description (executed: `gh api repos/:owner/:repo/milestones/77 --jq .description`).

## Findings

### 1. The phase 1 record writes a real user path, and `tests/test_censuses.py` fails on it at HEAD

```seal
severity: must
location: `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/trail/phases/phase-1.md:18`
evidence: executed `bin/test tests/test_censuses.py -q -x`
```

Why it matters: the repository's `Broad gate` row ends in `bin/test -q` (`seal/config.md`), and that run holds this module. At HEAD the module fails, so the orchestrator's broad run fails and the sealer withholds.

The grounds:

- Run in the round's scratch clone at `a6c5fb76`, the module printed `1 failed, 175 passed`. The failing case is `Test_module::test_every_file_no_module_file_declares_meets_every_census`, and its one entry reads `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/trail/phases/phase-1.md:18: real_identifiers: ... is a real user path, and fixtures use /Users/x/`. The path it names is the worktree's absolute path under the owner's home directory, inside the `git clone` command the line quotes.
- `tests/censuses.py#real_identifiers` reads every tracked text file and exempts no record prefix (`tests/censuses.py:948-970`), so a record under `seal/threads/` is held to it like any other file.
- The class is whole at HEAD. The census's own sweep reads every tracked file and listed this one line and no other.
- The phase claimed its boundary set is "the modules that read this work item's records" (`trail/phases/phase-1.md:57`). It named three modules and left out `tests/test_censuses.py`, which reads every tracked file. S3 did run that module, in the clone at `ad642d3f`, before `phase-1.md` was written.

The fix replaces the absolute path in line 18's command with a placeholder. The rest of the line stays as it is:

```markdown
**The rehearsal ran in one scratch clone, which is removed.** Executed: `git clone --no-local -q <the worktree> <scratchpad>/1793516191-a-wording-pin-module-leaves-by-rule-changes/clone`.
```

### 2. The line-18 `to` puts the pact words' reader in prose under a check line that does not read them, so the issue's own example gets no `check: none reader:` line

```seal
severity: should
location: `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:111-117`, `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:81-83`, `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:56`
evidence: read `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:111-117`, `tests/behaviour/test_one_word_one_meaning.py:953-999`, `skills/writing-style/SKILL.md:12`, `skills/writing-style/SKILL.md:252-253`, `docs/the-pact.md:8-31`, `tests/hooks/test_config.py:1518`, `tests/hooks/test_config.py:1528`, `skills/settle/SKILL.md:214-218`
```

Why it matters: #1197's second *Done when* bullet asks that each fact the module held is held by a case or "named as `check: none reader: …`", and its example is "a renamed word that must not come back". That is case 24. The settle writes each section in its own words (`skills/settle/SKILL.md` *The settling session's procedure* step 2). A reader that only a prose sentence names is the part of a `to` most easily reworded away.

The grounds:

- Case 24 reads every tracked file outside the records, code included: identifiers, comments and docstrings (`tests/behaviour/test_one_word_one_meaning.py:953-999`).
- The design places case 24's fact with "the proofer, as for case 23" (`frame/design.md:83`). It defines that reader as the one `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* names for its second rule (`frame/design.md:56`). That section applies to text an agent follows or a check reads (`skills/writing-style/SKILL.md:252-253`). The skill also says it is not for code comments or docstrings (`skills/writing-style/SKILL.md:12`). So for the code text case 24 sweeps, the one reader left is the sentence the line-18 `to` adds.
- That sentence stands above `check: tests/hooks/test_config.py`. That module's cases read the `Signer` table (`tests/hooks/test_config.py:1518`, `:1528`). None of them reads a text for another word. After the settle, `seal rules docs/the-pact.md` would name `tests/hooks/test_config.py` as what reads a paragraph whose last sentence it never reads. The proofer, who does read it, would stand on no check line.
- The claim "the line-18 item also rewrites the sentence ... so it names the proofer as the reader of the pact's words" (`frame/design.md:26`) holds for the sentence. It does not hold for the check line, which is where the rule shape `skills/settle/SKILL.md` *A rule has one shape* puts the reader.

The fix splits the rule. The definition paragraph keeps its test, and the words become a rule of their own, with the proofer on its check line. The `add` lands at the end of *The words*, after the paragraph line 31 ends. Rows 22 to 24 of *What each case held*, G7 and Scope item 1 then cite the added rule. P2's window probe runs again over the new `to`.

```markdown
- change
  file: docs/the-pact.md
  section: The words
  from: The three names are the owner's, and a case holds other words for them out of the shipped text.
    check: tests/behaviour/test_one_word_one_meaning.py tests/hooks/test_config.py
  to: check: tests/hooks/test_config.py
- add
  file: docs/the-pact.md
  section: The words
  to: **The three names are the owner's, and a text that names one of them another way, the word 0.18.x used for a signer included, is the proofer's to find at review.** No case sweeps the tree for other words, because a case that refuses a word wherever it stands turns red where the meaning has not changed (`skills/core/SKILL.md` *Judgment is spent where meaning is the question*).
    check: none reader: the proofer at review
```

### 3. Two rows of *What each case held* do not place what their case asserts

```seal
severity: should
location: `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:61`, `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:66`
evidence: read `tests/behaviour/test_one_word_one_meaning.py:88-96`, `tests/hooks/test_mode_gate.py:318-339`, `tests/behaviour/test_one_word_one_meaning.py:136-151`, `skills/implement/orchestration.md:314`, `tests/hooks/test_routing_edit_gate.py:296-299`, `docs/the-review-and-parity-arms.md:34-37`
```

Why it matters: the successor's change cites this table as the account the second *Done when* bullet asks for. A row that names a holder for something that holder does not read, or that leaves out an assertion, tells that change a fact is held when it is not, or hides a fact it has to account for.

Method: rule 12's second method. Each of the 24 cases was taken apart into its assertions, and each assertion was read against its row and the row's coordinate. Twenty-two rows hold what they state. Two do not:

- **Row 2.** The row claims `tests/hooks/test_mode_gate.py:321` is a case "whose case reads that README row against the marker's key". Line 321 is a docstring line of `test_accepts_one_local_root_as_one_question_for_the_whole_clone` (`tests/hooks/test_mode_gate.py:318-339`). The case runs the hook from two work trees and reads no README. The behaviour is held. Case 2's own assertions, that `README.md` spells each grain and does not say "Fires once per session," (`tests/behaviour/test_one_word_one_meaning.py:88-96`), have no holder named.
- **Row 7.** Case 7 asserts two things (`tests/behaviour/test_one_word_one_meaning.py:136-151`). The row places the first, that the old row is in neither implement file. The second, `"for **either** review answer" in orchestration`, is the fact that the declaration is read for either review answer (`skills/implement/orchestration.md:314`). The row does not place it. It is held elsewhere: `tests/hooks/test_routing_edit_gate.py:296-299` lets an edit through on a declared branch for both `Review` answers, under `docs/the-review-and-parity-arms.md` *The routing check reads `seal/threads/<work-item-id>/routing.md` before it reads anything else.* (`:34-37`).

```markdown
| 2 | `test_every_once_in_the_readme_states_its_grain` | the mode gate asks once per session per repository, the review-skill gate once per session per working tree | the behaviour: `tests/hooks/test_mode_gate.py:318`, one question for a local root across the clone's work trees, and `tests/hooks/test_review_skill_gate.py:137`, `:143` (read); the README's spelling of each grain, the proofer |
| 7 | `test_the_row_that_could_not_be_true_is_corrected_not_reworded` | an old routing row is in neither implement file; the routing declaration is read for either review answer (`skills/implement/orchestration.md:314`) | the first, history, which `tests/behaviour/test_waiver_decided_at_start.py:25` records in its docstring; the second, `tests/hooks/test_routing_edit_gate.py:296-299`, which lets an edit through on a declared branch for both `Review` answers (read); the wording, the proofer |
```

### 4. *The successor issue* cites coordinates that resolve only inside this frame, which the settle removes

```seal
severity: should
location: `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:89-96`
evidence: read `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:89-96`, `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:17`, `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/plan.md:13`, `skills/settle/SKILL.md:278-281`
```

Why it matters: the orchestrator files this text as the body the removal's work item acts on. The settle's `--apply` removes this directory in the same change that writes the `to` values (G11, `skills/settle/SKILL.md:278-281`). That happens before the successor starts. So every coordinate the body gives as a frame-relative name points at nothing on the branch the successor is built on.

The grounds, each at `frame/design.md`:

- `:91` cites "(G2)" and "this design's three `to` values".
- `:92` cites "#1197's *What the removal owes* list less its first bullet, which this design answers".
- `:93` cites "(`trail/phases/phase-1.md`, S5)".
- `:94` cites "(`gaps.md`)".
- Only `:95` gives a path that resolves, `v0.27.1:seal/threads/.../frame/design.md`.
- The precondition at `:91` reads "after the settle that writes this design's three `to` values into `docs/` has merged". The plan states it differently, as "the three lines no longer name the module, whatever their words" (`frame/plan.md:13`). A settle that rewords a `to` leaves the successor's builder unable to tell from the first form whether the precondition holds. The second form is a search it can run.

The fix rewrites the section so that each coordinate is a release-tag path or a path in the tree. The *How the list was made* bullet is finding 5's text, and the milestone sentence is finding 6's.

```markdown
### The successor issue

The orchestrator files it before `seal pr-body` runs, in the milestone `frame/questions.md` Q1 gives. Every coordinate in its body resolves outside this directory, which the settle's `--apply` removes (G11). Its body holds:

- **The precondition.** It is built once no `check:` line under `docs/` names `tests/behaviour/test_one_word_one_meaning.py`, whatever words the settle wrote: `git grep -n one_word_one_meaning -- docs` lists nothing. The settle after 0.27.1 writes the rule changes of `v0.27.1:seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md` *Rule changes*. Until then `seal rules --check` refuses the removal, because a pending `change` excuses no line (`.github/scripts/rules.py`, its module docstring).
- **What the removal owes.** The places outside `docs/` that #1197's *What the removal owes* lists, at `ad4556f4`. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* line 276 turns to `check: none reader: the proofer at review`, and `tests/text/test_a_language_section_of_writing_style_opens_alone.py#WRITING_RULE_CHECKS` follows it. The sentence of *여럿이 가질 수 있는 것은 누구 것인지 밝힌다* that names the module (lines 245-248) is rewritten so it no longer says a check holds the word. `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#APPLIES_THE_SHARED_GUARD` loses the module's row. The comments at `skills/verify/scripts/session_cost.py:63` and `hooks/lib/config.py:1414`, and six lines of four test files, no longer cite the module: `tests/behaviour/test_a_release_is_sized_by_a_criterion.py:57` (a comment), `:107` and `:333`, `tests/behaviour/test_chain_hooks_hardening.py:637` (a comment), `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:19` and `tests/text/test_edits_go_through_the_edit_tool.py:19`. The 24 rows leave `.test_durations`. The module goes.
- **How the list was made.** (finding 5's text)
- **The suite after the deletion.** Nobody has run which test modules other than `seal rules --check` turn red once the module goes (`v0.27.1:seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/gaps.md`, its third row). This build's phase boundary runs the suite with the module removed.
- **The facts.** `v0.27.1:seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md` *What each case held*.
- **Done when.** The module and every place above leave in one change, and each fact *The facts* names is held by the case, or the `check: none reader:` line, that its row names.
```

### 5. *How the list was made whole* calls whole a search that took two of the module's 31 names beyond its cases

```seal
severity: should
location: `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:93`, `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/trail/phases/phase-1.md:55`
evidence: executed `git grep -n -w -f names.txt -- . ':!seal/threads' ':!tests/behaviour/test_one_word_one_meaning.py' ':!.test_durations'`, `grep -oE '^(def [A-Za-z0-9_]+|[A-Z0-9_]+ =)' tests/behaviour/test_one_word_one_meaning.py`
```

Why it matters: contract rule 12 makes a sample handed back as a whole list a finding, even where every instance on it is right. The successor's reviewer reads this bullet to decide what is still open.

The grounds: the bullet claims the list was made whole by `git grep` on the path, by a `git grep -w` on "the module's 24 case names and its constants `SWEEP_MODULE` and `LITERAL_SEAM`", and by `seal rules --check`. The module defines 55 top-level names (executed, the second command). They are 24 cases, 28 constants and three helpers: `flat`, `pact_texts` and `without_the_policy_span`. The search took the cases and two of the 31 others. The phase record says the same (`trail/phases/phase-1.md:55`). This round searched all 55, written whole into `names.txt` in the round's scratch directory. Apart from other units named `flat` and the English word "flat", the search listed one line, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:77`, which is already on the list. So the list is whole for identifiers, but the bullet does not show the method that makes it so.

```markdown
- **How the list was made.** The module was taken apart into its 55 top-level names: its 24 cases, its 28 constants and its helpers `flat`, `pact_texts` and `without_the_policy_span`. Each name was searched with `git grep -n -w` outside the module, `.test_durations` and `seal/threads`, at `a6c5fb76`. Apart from other units named `flat`, the search lists one line, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:77`, which is on the list above. Beside it, `git grep -n one_word_one_meaning -- . ':!seal/threads'` lists the places above and the 24 rows of `.test_durations`, and `seal rules --check` after the deletion refuses one line, `skills/writing-style/SKILL.md:276`. For paths and identifiers the list is whole. No search lists a sentence that names the module in prose alone, with no path or identifier. That part is a sample, and this build's reviewer reads for it.
```

### 6. Q1's default files the successor in `release: 0.27.2`, whose purpose it does not share, and leaves out `release: 0.27.3`, which already orders a wording-pin item after #1197

```seal
severity: should
location: `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/questions.md:14`, `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/plan.md:46`, `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:89`
evidence: executed `gh api repos/:owner/:repo/milestones/76 --jq .description`, `gh api repos/:owner/:repo/milestones/79 --jq .description`, `gh api 'repos/:owner/:repo/milestones?state=open&per_page=50'`
```

Why it matters: the orchestrator took Q1's default under automation (`frame/plan.md:46`) and files the successor there. `docs/issues-and-milestones.md` *A milestone answers when, and takes three shapes* says a scheduled release milestone's description states the release's purpose. It says a patch's purpose is judged against that text by whoever files into it, and it puts the ceiling at three or four work items.

The grounds:

- Milestone 76, `release: 0.27.2`, gives its purpose as "whether the plugin needs new verification at all, then the measurement ... A patch: it decides and documents, and builds no feat". It holds nine open issues. Removing a test module and its references is neither deciding nor documenting.
- Milestone 79, `release: 0.27.3`, was created on 2026-11-01. Its purpose is to "remove the restatements and stored copies #1147's audit measured", among them "the wording pins outside #1197's module". It reads "A patch: it fixes and removes", and its order says "the wording-pin item follows #1197". Its description also records that #1147's drafts "weighed 0.27.1, 0.27.2 and 0.28.0 each past the ceiling".
- Q1 offers only (a) `release: 0.27.2` and (b) a `backlog:` milestone (`frame/questions.md:14`). The question claims the tree cannot answer it. The open milestones' descriptions answer most of it. Q1 and the plan's judgment row (`frame/plan.md:46`) name neither milestone's description.
- 0.27.3 is ordered after 0.27.2. A settle the owner calls at 0.27.2's `docs/release-checklist.md` *2b. Settle what earlier releases left behind* lands before the successor is built. Under (a), `release_completeness_check.py` refuses 0.27.2 until the successor merges, so the removal would have to be built inside 0.27.2's own release steps.

The fix adds the option and makes it the default. The plan's judgment row then reads "Q1 takes its default, `release: 0.27.3`". The successor's body carries the order, because grounds that belong to one ticket sit on that ticket and no milestone description is edited:

```markdown
| Q1 | Which milestone takes the successor issue that carries the module's removal? A milestone answers when (`docs/issues-and-milestones.md` *A milestone answers when, and takes three shapes*), and the removal can start only after a settle, which runs when the owner calls it (`docs/release-checklist.md` *2b. Settle what earlier releases left behind*). The open milestones' descriptions decide most of it. The answer changes nothing this pull request builds | a person | (a) `release: 0.27.2`. Its purpose, "it decides and documents", is not a removal's, it holds nine open issues past the ceiling, and its release is refused until the successor merges. (b) A `backlog:` milestone. No release is ever refused over it, and nothing schedules it either. (c) `release: 0.27.3`. Its purpose is to remove wording pins and stored copies, "it fixes and removes", its order already reads "the wording-pin item follows #1197", and it comes after 0.27.2, so a settle called at 0.27.2's step 2b lands first | (c) `release: 0.27.3`: the orchestrator files the successor there, and its body says the 0.27.3 wording-pin item follows it | open |
```

## Confirmations

```seal
confirms: none
```
What matched: the three items parse and each `from` stands in its section. Claimed (P3): `parse` returns three `change` operations with no error, and the third `to` is found before any settle. Found, executed in the round's scratch clone at `a6c5fb76`: `skills/settle/scripts/rule_changes.py#parse` returned three `change` operations, `errors=[]` and `unread=[]`. *One act, one owner, and the owner is the orchestrator* spans `docs/the-broad-gate.md` lines 8 to 42, and *The words* spans `docs/the-pact.md` lines 8 to 31. Each `from` is found by `pattern`. The first two `to` values are not found, and the third is, as P3 says.

```seal
confirms: none
```
What matched: the line-33 `to` names a target that runs the rule's behaviour. Claimed (G8): the gate's cases assert that stdout opens `BROAD GATE PASSED` or `BROAD GATE FAILED` exactly, and that a run queues no stamp. Found, read: `tests/skills/test_broad_gate.py:2445` asserts the first line is `BROAD GATE PASSED   feature @ ...`. `:2460-2461` asserts no `agentic-stamp` directory. `:2472` asserts that a failure opens `BROAD GATE FAILED`. `:2739` and `:2757` assert the same at the command line. The other targets of `docs/the-broad-gate.md` already name this module as a file (lines 59, 79, 87 and 107), so the `to` keeps the section's shape. Plan A7 is right that `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` alone would leave the printed line unread.

```seal
confirms: none
```
What matched: the line-31 `to` drops the module and states no false rule. The two targets it keeps read the 0.18.x header: `tests/hooks/test_config.py:1556`, `:1581`, and `tests/skills/test_pact_check.py:734`, `:1114` (read). The paragraph's last clause, "every text this plugin ships says `signer`", is true at `a6c5fb76`, and it claims no case holds it. With the line-18 rule split as finding 2 gives, its reader stands on a check line in the same section.

```seal
confirms: none
```
What matched: changing nothing outside `docs/` now is right. Claimed (G2, plan A2 and A3): a pending `change` excuses no refused line, so the module must stay until the settle, and each place outside `docs/` states a fact true until then. Found, read: `.github/scripts/rules.py:43-44` says "A pending `change`, or a `remove` with a `from`, whose `from` holds the line excuses nothing, so the test the line names stays until the settle". `skills/writing-style/SKILL.md:276` names a module that still runs. `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:60-77` classifies every scope that derives a path list from git, and the module's case 24 is one of them. A2 is right that each change made now would state a false fact. A3's widened excuse would leave three `docs/` lines naming a missing file between merge and settle. Milestone 77's description orders "this release writes those rule changes and the removal follows the settle", which A1 follows.

```seal
confirms: none
```
What matched: S5's list of places. Claimed: `git grep -n one_word_one_meaning -- . ':!seal/threads'` lists the 24 rows of `.test_durations` and 12 lines in 10 files, each mapped to an item of *The successor issue*. Found, executed at `a6c5fb76` in the worktree, where the module and the three `docs/` lines still stand: 16 lines in 12 files outside `.test_durations`, and 24 rows in it. Without the three `docs/` lines, which the settle changes, and the module's own `SWEEP_MODULE` line 950, which leaves with it, they are the phase's 12 lines in 10 files. Those 12 are the successor's list, item for item, at the line numbers the design gives.

```seal
confirms: none
```
What matched: the other 22 rows of *What each case held* hold what they state, each opened. Row 1: `tests/hooks/test_routing_edit_gate.py:3` and `:92`. Row 4: `docs/the-routing-check.md:61-71`, whose check names `tests/hooks/test_routing_edit_gate.py`. Row 5: `docs/the-review-record.md` *The run*, with `check: run-ends-with-verifying-round` and `check: tests/text/test_the_rules_have_one_owner.py`. Row 6: `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, whose corpus is every tracked file outside the records, `agents/crafter.md` among them. Row 7's first half: `tests/behaviour/test_waiver_decided_at_start.py:21-25`. Row 8: `tests/text/test_the_rules_have_one_owner.py:86`. Rows 12, 13 and 15: as the second confirmation, with `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:136`. Row 17: `tests/skills/test_session_cost.py:1854`, `:3518`, `:3543`. Rows 22 and 23: as the third confirmation, with `tests/hooks/test_config.py:1518` and `:1528`. Rows 14, 16 and 19 to 21 pin the module's own patterns, so they leave with it (`tests/behaviour/test_one_word_one_meaning.py:442-448`, `:488-515`, `:592-722`).

```seal
confirms: none
```
What matched: the diff is records only, and it owes no changelog fragment. Executed: `git diff --stat origin/release/v0.27.1...HEAD` lists six files, all under `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/`, so S6 holds at `a6c5fb76`. G13's precedent stands at `seal/threads/1793490088-each-kind-of-restatement-is-measured/guarantee.md:53` (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the reader the writing-style line will name reaches `README.md` and `README.ko.md`, which cases 2, 3 and 10 read. The section applies to text an agent follows or a check reads, and names skills, agent definitions, templates and frames as its examples (`skills/writing-style/SKILL.md:252-253`). Whether a README is such a text is a reading this round did not settle | `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md:56` | the framer of the successor issue, when it writes that line's reader |
| Phase 1's runs of S2, S3 and S4 in its scratch clone, including the `seal mutate` run on `GATE_PASSED`. This round read them and did not run them again | `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/trail/phases/phase-1.md:22-32` | the sealer, at its sample of the crafter's claims |
| The broad gate at HEAD, `unverified`. Finding 1 shows one module of it failing | `seal/config.md` | the orchestrator's broad run, then the sealer |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_parse.py` in the round's scratch clone at `a6c5fb76`, first run | exited 1 with a `KeyError` in the probe's own code, which read the operation's fields by the wrong names (`old` and `new` are the names). It settled nothing |
| the same probe, with the field names corrected, second run | exited 0: three `change` operations, `errors []`, `unread []`; sections (8, 42) and (8, 31); `from` found for all three; `to` found only for the third |
| `git grep -n -w -f names.txt -- . ':!seal/threads' ':!tests/behaviour/test_one_word_one_meaning.py' ':!.test_durations'`, over the module's 55 top-level names | apart from other units named `flat` and the English word, one line: `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:77` |
| `bin/test tests/test_censuses.py -q -x` in the round's scratch clone at `a6c5fb76` | `1 failed, 175 passed`; the failure is `trail/phases/phase-1.md:18`, a real user path (finding 1) |

The probe file, `names.txt` and the scratch clone, with the `.venv` that `bin/test` built in it, are removed.

# Review round 1: 1793661729-each-document-is-cut-by-who-opens-it

```seal
target: 5d0e07402 against release/v0.30.0
```

This round read the branch at 5d0e07402 against `origin/release/v0.30.0` at
95cbd99a4, in a `git clone --no-local` of the repository checked out at the
target. No earlier round exists, so no fact was carried; every fact below was
established here. `seal/parity.md` is not declared, so no `original:` line is
owed.

## Findings

### 1. Both READMEs still say a work item never edits the policy root, which the boundary D9 wrote replaced

```seal
severity: should
location: `README.md:119`, `README.ko.md:114`
evidence: executed `git grep -n -i -E "instead of editing|rather than editing|고치지 않고|does not edit|never edit|not edited" -- :!seal/threads :!CHANGELOG.md`
```

Why it matters: the `docs/` row of the layout table in `README.md:119` says
"A work item states its rule changes in its design instead of editing them",
and `README.ko.md:114` says the same ("작업 항목은 이 문서를 고치지 않고 바꿀
규칙을 설계에 적으며"). Both cite `skills/implement/SKILL.md` *Document layout
— two roots, three lifetimes* as their source. That row (`skills/implement/SKILL.md:73`)
now says the opposite for one kind of work item: a work item whose subject is
the policy root edits it directly in its pull request. This work item is that
kind and edits `docs/` itself. A reader who opens the README learns the rule
this pull request retired, and the citation sends them to a section that
contradicts it.

The crafter's account: phase 1 (`trail/phases/phase-1.md` *Two places stood
on the old clause*) searched for the clause's words and for statements that
the settle alone writes the policy root, and found `agents/framer.md` and one
test comment. It called that list a sample under contract rule 12. The two
README rows are restatements in other words, which that search could not
match. Phase 5 edited both READMEs to re-point paths and left these rows.
Contract rule 19 asks that a change remove or correct what stood on the old
fact in the same pull request.

```markdown
README.md:119, the docs/ row's last cell, from "A work item states" to the end:
A work item whose subject is the policy root itself edits it directly in its pull request; one whose subject is the code states its rule changes in its design, and the settle after the release writes each section as the latest decision those changes state (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*) |

README.ko.md:114, the docs/ row's last cell, from "작업 항목은" to the end:
정책 루트 자체가 주제인 작업 항목은 그 pull request 에서 이 문서를 직접 고치고, 코드가 주제인 작업 항목은 이 문서를 고치지 않고 바꿀 규칙을 설계에 적으며, 릴리스 뒤의 settle 이 그 변경이 말하는 가장 나중 결정으로 절마다 써 넣는다(`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*) |
```

```seal
verdict: fixed 170372c72
answer: Both README rows take the paste-ready text as given. The class was listed by two scans of every tracked .md, .py and .yml file outside seal/threads/ and CHANGELOG.md, sentence by sentence: one for a sentence naming the policy root or a design's rule changes with a write verb and a negation, one for a sentence naming the policy root or rule changes with a writer (settle, pull request, work item) and a write verb; each hit was read. Beyond the READMEs they found six more statements that every policy change goes through a design's rule changes or that only the settle changes the policy root, each now stating the subject boundary or dropping the premise: skills/implement/orchestration.md's open-decision row and lesson row, skills/implement/SKILL.md's missing-clause sentence, the opening of skills/settle/SKILL.md, the grammar's opening in skills/settle/rule-changes.md, skills/settle/named-directories.md's way of finding the last settle's pull request, which took the last commit that changed the policy root, and the docstring of test_the_orchestrators_run_judgments_are_rows_of_the_plan. The scans match the root's names and verbs they list, so a statement in other words still escapes them; this is a sample of that unbounded class.
location: `skills/implement/orchestration.md:472`, `skills/implement/orchestration.md:489`, `skills/implement/SKILL.md:146-149`, `skills/settle/SKILL.md:17-21`, `skills/settle/rule-changes.md:11-15`, `skills/settle/named-directories.md:51-55`, `tests/text/test_the_rules_have_one_owner.py:455-456`
```

### 2. The record layout still sends its reader to the fold section "above", which moved to another document

```seal
severity: should
location: `docs/layout/the-record-layout.md:123`
evidence: executed `git show base:docs/the-record-layout.md | grep -n "The fold, and what tells"`, `grep -n "The fold, and what tells" docs/layout/the-record-layout.md docs/checks/the-fold.md`
```

Why it matters: `docs/layout/the-record-layout.md:122-124` reads "go with
the directory, whole, when the settle removes it (*The fold, and what tells it
from a deletion* above, and `docs/releasing/release-checklist.md` *2b*)". At
the base that section stood above this paragraph in the same file
(`docs/the-record-layout.md:78`). Phase 5 moved it to
`docs/checks/the-fold.md`, so the file no longer holds it, "above" is false,
and the reference names a section of another document without its path.
That is the defect `frame/design.md` D7 *Path-less cross-references* exists
to prevent.

The crafter's account: `trail/phases/phase-5.md` *Four path-less
cross-references now cross documents* scanned the old review record and the
two sections cut from the record layout, and found four. Its scan read the
text that moved out, not the text that stayed behind and named what moved.
This reference is the second kind. `gaps.md` *Not verified* left this to the
proofer. This round's scan read every italic span in the 18 files the cuts
touched, the new documents, the cut documents and the skills' supporting
files, and listed each span whose text is a heading of another of those
files or of the cut files at the base. It found this one and one other. The
other is `skills/settle/named-directories.md:5`, which names its file
("that file's") and is correct. The scan is a sample: it matches a reference
spelt as the heading in italics, and a reference in other words is not in
it.

```markdown
docs/layout/the-record-layout.md:122-124:
written) go with the directory, whole, when the settle removes it
(`docs/checks/the-fold.md` *The fold, and what tells it from a deletion*,
and `docs/releasing/release-checklist.md` *2b*). A document that still cites a record of
```

```seal
verdict: fixed d990b38b5
answer: The record layout takes the paste-ready text as given. The class was listed from what produces it: every heading the base held in a file this branch renamed, cut or deleted and that file no longer holds at HEAD (32 headings), then every italic citation of each of those headings in the tracked files outside seal/threads/ and CHANGELOG.md (135), each checked for the nearest preceding backticked path in its paragraph naming the file that holds the heading now; and every italic heading followed by above or below (24), each checked against its own file. One more instance stood: skills/code-review/scripts/chain_check.py's docstring said the pull request check's document holds *The round record* and *The guarantee* ("its"), and it now names docs/forms/the-round-record.md and docs/forms/the-guarantee.md. The other hits resolve: a path named a line earlier or later, or a test variable holding the path. A reference to a moved section spelt in other words than its heading is outside both lists.
location: `docs/layout/the-record-layout.md:123-124`, `skills/code-review/scripts/chain_check.py:79-80`
```

### 3. The changelog says the moved policy text changed only in paths and four references, and leaves out the guarantee's rewritten opening

```seal
severity: should
location: `seal/threads/1793661729-each-document-is-cut-by-who-opens-it/changelog.md:5`, `seal/threads/1793661729-each-document-is-cut-by-who-opens-it/changelog.md:8`
evidence: executed `git diff --no-index --word-diff=plain base-guarantee-section.md head-guarantee-section.md`
```

Why it matters: the fragment's policy-root item (`changelog.md:5`) says "The
moved text is unchanged except for re-pointed paths and four
cross-references that now name the document they point to." A word diff of
the base's *The guarantee* section against `docs/forms/the-guarantee.md`
(executed, the section cut from each with one `awk` and compared) shows its
opening rewritten (read, `docs/forms/the-guarantee.md:8-9`). At the base it said the sealer verifies, independently of
the crafter and the proofer, against the issue body and the tree, never an
agent's word or the orchestrator's summary. Now it reads "what it verifies
against is `agents/sealer.md` *Job*'s." Phase 1 made that change on
purpose and gave its grounds (`trail/phases/phase-1.md` *A departure from
D6's second row*). The fragment's item on copies (`changelog.md:8`) names
the question gate, the stamp and the guarantee's form, and does not name
this one. *The run*'s gate paragraph changed too; item 8 does name that
change. The fragment is what the release notes and the pull request body
are built from, so a reader of the release is told that every other word of
the moved policy stands as it did.

```markdown
changelog.md:5, the sentence "The moved text is unchanged ...":
The moved text is unchanged except for re-pointed paths, four cross-references that now name the document they point to, and the passages the next item moves to one side.

changelog.md:8, at the end of the item:
*The guarantee*'s opening restated the sealer's job from its definition, and now cites `agents/sealer.md` *Job* for it.
```

```seal
verdict: fixed b204b7e8b
answer: Item 8 takes the paste-ready sentence as given. Item 5's paste-ready text points to "the next item", which is item 6, the readers of group directories, so item 5 is written in other words: the moved text changed in re-pointed paths, four cross-references, and two passages that now cite where their text stands, which the item on such passages names. A word diff of each of the seven moved sections against its base text (executed) found those changes and no others: the guarantee's opening and its two cross-references, the run's question-gate paragraph and its one cross-reference, one in the pull request check, and one re-pointed skills path in the fold. The fragment is the one statement of the fact against the release base; trail/phases/phase-5.md S7 measured the phase 5 moves against ecaa65963, after phase 1's edits, and holds there.
```

## Confirmations

```seal
confirms: none
```
What matched: S2. The crafter claimed (`trail/phases/phase-6.md` *S2*) that
no agent's preload grows: crafter 33203 to 33081, framer 36365 to 36362,
proofer 32414 to 32293, sealer 32262 to 31879, tracer 25212 to 25085. This
round computed `.github/scripts/release_report.py#preloads` from the HEAD
tree over a `git archive` of the base and over the clone at 5d0e07402
(executed) and got the same ten numbers. The base it used is 95cbd99a4, whose
tree differs from the frame's 2d38c75af only by `routing.md` (executed,
`git diff --stat 2d38c75af base`). The framer's 3-byte margin is as
`gaps.md` *Not done* says.

```seal
confirms: none
```
What matched: S1 and D1. `skills/core/SKILL.md:60-66` holds D1's paragraph
word for word, five sentences, after *Each agent judges its own target*
(read). D2 item 1's sentence is gone, and the invariant table's first row
still names `hooks/routing-edit-gate.py`, whose refusal names
*Orchestrator: how the work is routed* (`hooks/routing-edit-gate.py:98`,
read).

```seal
confirms: none
```
What matched: phase 6's offsets beyond D2. Contract rule 2 lost the sentence
that spelt `seal gate --base <base> --record <item>`. Only the orchestrator
types that command. `docs/running/the-broad-gate.md` and
`skills/verify/orchestration.md` *The broad gate* keep it, and rule 2 still
says no agent runs the broad gate and names the orchestrator as the suite's
answerer (read). The core's "where first setup or `seal pr-checks install`
put its workflow in the tree" became "where its workflow is installed", which
keeps the condition (read). Both are preload text that only the orchestrator
acts on, or that no agent acts on, which is what D2's last paragraph
licenses. Neither grows another file. Rule 20's retirement line is D2 item
2's text with the core cited by path. The core's *The rule a mechanism is
kept against* does not hold the premise clause, and the retirement line
states that clause itself (read).

```seal
confirms: none
```
What matched: D9 and S11. `skills/implement/SKILL.md:73` holds D9's text word
for word, and `git grep -n "does not edit it" -- ':!seal/'` printed nothing
and exited 1 (executed). Whether this work item's own policy-root edits
stay inside the boundary was read as follows. Each of the fourteen documents
`git diff -M` lists as renamed was word-diffed against its base path. Every
changed word holds a `docs/` path, except one re-pointed
`skills/settle/rule-changes.md` in `docs/forms/the-reader-registry.md`
(executed). The seven new documents hold their sections with titles, reader
sentences, D7's four references, re-pointed paths, and the two copy edits
phase 1 made under D6 (executed, section-wise word diff). The index is
rewritten as D3 states (read, `docs/README.md`). Finding 1 is the one place
that still states the old clause.

```seal
confirms: none
```
What matched: S9. `bin/seal fold` printed "held 23 documents under docs/ to
25000 estimated tokens, 0 past it" and "the index docs/README.md names every
document", and exited 0 (executed).

```seal
confirms: none
```
What matched: the nine lines phase 5 left naming `docs/the-review-record.md`
(`trail/phases/phase-5.md` *A departure from S8*). Each one names the file as
it stood at an earlier commit: `evals/scripts/replay_targets.py:24` uses the
`v0.22.0:` form; `:28` and `:281` name one of `CHECK_FILES`, the paths at
which the 0.22.0 tree holds each file the replay builds; the three lines of
`tests/evals/test_replay_targets.py` and `tests/evals/test_seed_defects.py:106`
write that tree; `hooks/lib/fields.py:127` and
`tests/skills/test_chain_check.py:4237` describe the check before #1198
(read). Re-pointing them would name a file the replayed tree never held. No
other old top-level policy path stands outside `seal/threads/` and
`CHANGELOG.md` (executed, `git grep` of all sixteen old names, including
`seal/` above `threads/`).

```seal
confirms: none
```
What matched: phase 2's and phase 3's readers.
`.github/scripts/rules.py#policy_documents` and
`.github/scripts/release_report.py#documents` resolve the root through
`hooks/lib/config.py#policy_root` and list it through
`skills/settle/scripts/fold_check.py#documents`. `RULE_FILES` no longer
names `docs/*.md`, so a repository whose `Policy root` names another
directory has that directory read instead (read). `RULE_FILES` and the emoji
census `CORPUS` read `skills/*/*.md` (read). `bin/seal rules --check`
printed "all 295 check lines in 71 rule files hold" and exited 0 (executed).
The new cases in `tests/github/test_rules.py`,
`tests/github/test_release_report.py`, `tests/skills/test_fold_check.py` and
`tests/skills/test_rule_changes.py` were read against their modules' other
cases. Each covers a group, a refused path or an unreadable index that no
earlier case covered.

```seal
confirms: none
```
What matched: D6's copies. The rule and limits `skills/verify/scripts/seal_stamp.py`
dropped stand in `docs/checks/the-stamp.md:27-61` (read). The question gate's
docstring gained "a row edited to `no` is in the diff the review reads". It
lost one paragraph, and `docs/running/the-run.md:71-73` holds that paragraph
(read). The sealer's guarantee paragraph keeps the acts it takes and cites
`docs/forms/the-guarantee.md` *The guarantee* for the form (read). Step 1
cites `skills/code-review/scripts/chain_check.py#follows`, which is
`chain_check.py:958` (read).

```seal
confirms: none
```
What matched: the re-pointed citations. Every `` `path` *section* ``
citation resolves (executed, the cited-section case). The bare re-pointings
of `docs/the-review-record.md` were tallied by target from the word diff
(executed). A sample of twelve was read in context, among them
`agents/framer.md:241-245`, `docs/releasing/issues-and-milestones.md:4`,
`skills/code-review/orchestration.md:133`,
`skills/implement/SKILL.md:107,148` and `docs/running/the-agent-set.md:84`.
Each names the document that now holds the subject it cites. Every relative
Markdown link in a tracked `.md` file outside `seal/threads/` resolves
(executed).

```seal
confirms: none
```
What matched: phase 7's replay (S10). This round wrote the script from
`trail/phases/phase-7.md` again and ran it against 2d38c75af and b1880c1db
over the same transcripts (executed). It also left out spawns whose
description names #1312 of every type, which takes this round out. The
results: crafter 78 spawns, 1258 calls, -6.5%; proofer 134, 44, +0.0%;
sealer 159, 13, -10.0%. Each matches the record. The framer came out at
168 spawns, 315 calls and -2.0%. The one framer spawn this round's filter
dropped is this work item's own framer, which the record's census counted.
The percentage is unchanged. The changelog's figures (preloads, the largest
document at about 11,884 tokens, the replay's percentages, 7,383 against
43,620 bytes, 5,388 bytes) match phases 3, 4, 6 and 7 (read).

```seal
confirms: none
```
What matched: the cut skills and the readers named in `gaps.md` *Not
verified*. `skills/settle/SKILL.md` names each of its four supporting files
at the step that opens it (lines 20, 60, 159-191, 303). `skills/verify/SKILL.md:69-70`
names both `seal` files. `skills/implement/SKILL.md` names
`skills/implement/orchestration.md` at the three places its passages left.
Each supporting file opens with its reader sentence (read). This round read
the text agents act on that phases 1 and 6 changed in `agents/framer.md`,
`agents/sealer.md`, the core, the contract and
`skills/code-review/orchestration.md`. Each act an agent takes is still
stated where it reads it, and the removed facts stand in the document cited
(read). Whether an agent behaves the same is not read; see `## Not judged`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a framer, a crafter, a proofer and a sealer under the installed 0.30.0 open the new paths and the cut files at the steps their texts name; no agent of this run receives them | `frame/questions.md` Q1 | the orchestrator of the first work item run under the installed 0.30.0 |
| The broad gate: the full suite, the lint and the typecheck at HEAD. This round ran 24 modules narrow, then the 84 modules that name a `docs/` path or `.test_durations` | the whole tree | the orchestrator's `seal gate` run after the rounds settle |
| A path-less reference to a moved section written in other words than its heading in italics; finding 2's scan matches only that spelling | the 18 files the cuts touched | the next round, or a reader who follows one |
| Links into `docs/` from outside the repository, which break at the release as `frame/plan.md` *Operational impact* states | outside the tree | the owner |

## Probes

| Command | Result |
|---|---|
| `bin/test -q --no-header` over 17 modules: the rules, release report, fold, rule-change, cited-section, emoji, line-wrap, census, broad-gate, contract, sealer, question-gate, review-axes, handoff, one-owner, rules-command and layout modules | 696 passed, exit 0 |
| `bin/test -q --no-header` over the 84 modules a `git grep -l` for `test_durations`, `"docs",` and `docs/` lists under `tests/` | 3885 passed, 11 skipped, exit 0 |
| `bin/seal fold` | 23 documents held, 0 past the ceiling, the index names every document, exit 0 |
| `bin/seal rules --check` | all 295 check lines in 71 rule files hold, exit 0 |
| `test_tmp_preloads.py`, `preloads` of the HEAD tree's `release_report.py` over the base archive and the clone | the ten numbers in the first confirmation, exit 0; deleted |
| `test_tmp_replay.py`, phase 7's replay written again, over 2d38c75af and b1880c1db | the per-type readings in the replay confirmation, exit 0; deleted |
| a read-only scan of italic spans in the 18 files the cuts touched, for a span naming a heading of another of those files | two spans, finding 2 and `skills/settle/named-directories.md:5` |
| `git diff --word-diff=porcelain` of each renamed document against its base path, words without a `docs/` path | one word, `skills/settle/rule-changes.md`, in `docs/forms/the-reader-registry.md` |

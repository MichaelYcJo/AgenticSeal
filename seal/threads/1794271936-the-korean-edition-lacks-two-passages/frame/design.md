# Design: 1794271936-the-korean-edition-lacks-two-passages (#1491)

## Grounding

The tree as read at `765f146ff`. A row marked `executed` rests on a command
the framer ran on 2026-11-10; every other row was opened and read.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, the `docs/` row | A work item whose subject is the policy root's documents' text edits the policy root directly in its pull request. This work's subject is two things: the text of `docs/layout/one-root-by-lifetime.ko.md`, a document of the policy root, which it edits in place; and `skills/settle/rule-changes.md`, a skill outside the policy root, which it edits as any work item edits a shipped file. So `## Rule changes` holds the no-change block, and no `change` operation carries the translation to the settle. |
| G2. Issue #1491 (`executed`: `gh issue view 1491 --json body,comments`, 2026-11-10) | The body under *Decided* records option (a), the owner's on 2026-11-10: keep the Korean edition, translate the two passages, and write into `skills/settle/rule-changes.md` that an operation on the English edition carries one for the Korean edition. *Done when* (a): the two editions' backtick tokens differ only where a placeholder is translated. The issue has no comments (`"comments":[]`). |
| G3. The two editions compared whole at HEAD (read, paragraph by paragraph; and `executed`: `grep -o` of every backtick span in each edition, `sort -u`, `diff`) | Every paragraph, table and check line of `docs/layout/one-root-by-lifetime.md` has a Korean counterpart except two passages, both in *What the repository decides for itself, and how it is read*. Passage A is the English paragraph opening **What language this plugin writes in is the repository's answer**, from "The two language keys of `seal/config.json` are required" to "A commit is never refused for them." (`.md:231-237`); the Korean paragraph opening **이 플러그인이 어느 언어로 쓰는지는** ends before it (`.ko.md:217-221`). Passage B is the last sentence of the English paragraph opening **Two keys, because one cannot express the middle answer**, "Where the two keys differ, the pull request body opens with `pr.<lang>.md` … reads the body in theirs." (`.md:250-253`); the Korean paragraph opening **키가 둘인 것은** ends before it (`.ko.md:224-232`). The token diff prints two English-only spans, `` `pr.<lang>.md` `` and `` `seal pr-body` ``, and none Korean-only. `seal/config.json`, English-only at the issue's commit, now stands in both. The gap is the issue's two passages, at new coordinates. |
| G4. What the 0.37.0 settle did to the two passages (`executed`: `git diff ba4d85629 8657297d5 -- docs/layout/one-root-by-lifetime.md`) | #1495 changed "row" to "key" inside both English paragraphs and left the two passages' text as it was, so the Korean text translates the English text at HEAD. |
| G5. Where the gap came from (`executed`: `git show --stat e5370691d -- docs/layout/`, and `grep 'file: docs/layout/one-root-by-lifetime'` over every design `e5370691d` removed, read at `e5370691d^`) | The settle of 0.35.0 to 0.36.0 changed `docs/layout/one-root-by-lifetime.md` and not its Korean edition. The one released design that named the document, `seal/threads/1794188289-the-body-reads-in-the-teams-language/frame/design.md`, carried two `change` operations on the English edition (its lines 187 and 202) and none on the Korean one. The settling session writes the sections its groups name (`skills/settle/SKILL.md` *The settling session's procedure*, step 4), so no group meant no Korean edit. The cause is a design that named one edition, and this is the mechanism's catch record. |
| G6. `skills/settle/SKILL.md` *A settle is not a work item*, and `docs/checks/the-fold.md` *The fold, and what tells it from a deletion*, its third paragraph | A settle opens no work item and has no round records; its pull request states each decision for the owner to review. A design that misses the Korean operation is read by the proofer only where its work item runs review rounds, and at the settle no proofer reads anything. The second reader that can still catch the miss is the settling session, which opens `skills/settle/rule-changes.md` before step 4 (`skills/settle/SKILL.md`, its opening paragraph). |
| G7. `CONTRIBUTING.md` *House rules*, the bullet opening **Both READMEs move together, and so does every document with a `.ko.md` edition**; `docs/checks/the-fold.md`, the paragraph opening **A document with a `.ko.md` edition changes with it, heading for heading.** | The edition rule exists for this repository: the editions tell the same story, the case `tests/behaviour/test_both_editions_carry_the_same_folds.py` compares heading levels only, and whether a Korean paragraph says what its English one says is review's. Both stay true under this work and are not edited. Neither says how a design's operations reach the Korean edition, which is the step the new sentence covers. |
| G8. `skills/settle/rule-changes.md` *Rule changes* and *The index* | *The index* says a row names a `.ko.md` edition on its English edition's row. No sentence of the file, of `skills/settle/`, or of `docs/` says that an operation on one edition carries one on the other (`executed`: `git grep -n -i 'ko\.md\|edition'` over the tree). `agents/framer.md`, `skills/implement/SKILL.md` and `docs/README.md` each send the design's author to *Rule changes* (`executed`: `git grep -n 'rule-changes.md'`), so a framer writing operations reads that section. |
| G9. The Korean editions the rule can reach (`executed`: `git ls-files '*.ko.md'`; read: `docs/README.md:69` and `:73`) | `docs/layout/one-root-by-lifetime.ko.md` is the only `.ko.md` edition the index names. `docs/experiments/` holds `.ko.md` files and is no policy; `README.ko.md` stands outside the policy root. |
| G10. A Korean operation passes the reader and names no copy (read) | `skills/settle/scripts/passages.py#in_corpus` excludes every `*.ko.md`. `tests/skills/test_rule_changes.py` case `a-korean-edition` and `tests/skills/test_chain_check.py` `test_refuses_to_name_a_copy_landing_in_a_korean_edition` pin that a `to` landing in a Korean edition names no copy. The released 0.37.0 design `1794200906` carried 11 operations on the Korean edition (`executed`: `git grep` at `ba4d85629`), so the form is already practised. |
| G11. The cases that read the touched files (read) | `tests/behaviour/test_both_editions_carry_the_same_folds.py` reads heading levels; the build adds no heading. `tests/behaviour/test_first_setup_asks_once.py:643-690` reads Korean strings of other sections. `tests/behaviour/test_docs_line_wrap.py` lists `skills/settle/rule-changes.md` (`LIMIT = 88` display columns) and lists neither edition of the layout document. `tests/behaviour/test_settle_applies_rule_changes_in_place.py` reads the first fenced block of *Rule changes* and the rows of its operation table; `tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py` reads four phrases of *A rule has one shape*; `tests/behaviour/test_a_phase_hands_the_next_one_a_record.py:142-146` reads the `## Rule changes` heading line. |
| G12. Korean wording already in the tree (read) | `README.ko.md:308-310`: "두 언어 키가 서로 다른 언어를 가리키면 본문은 `pr.md` 의 인용을 pull request 언어로 옮긴 `pr.<lang>.md` 로 시작합니다." `README.ko.md:145-146`: "언어 키 둘", "첫 편집 전에 두 키를 모두 묻습니다". The Korean edition writes "PR", "처음 설정" and the agent names in English. |
| G13. The unsettled designs and the policy root (`executed`: `ls seal/threads/`; `cat seal/config.json`; `git log` on the three sibling branches) | `seal/threads/` holds this work item alone. The siblings #1490, #1492 and #1493 carry a routing commit each and no frame. `seal/config.json` has no `Policy root` key, so the policy root is `docs/`. No `## Rule changes` operation elsewhere names a document or a section this work touches. |
| G14. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* | A sentence that tells a party to act names who acts, when, in which file, and what ends it. The new sentence names the design's framer and the settling session as the actors. |
| G15. `skills/core/SKILL.md` *The rule a mechanism is kept against*; `agents/framer.md` *A mark is not the answer to a blocked step* | A rule is a mechanism. Its catch record is G5, and `## Removes` says why nothing goes in return. |
| G16. The latest release's *Process changes* (`executed`: `gh release view --json body`) and `seal/follow-up.md` (`executed`: `grep -n -i 'korean\|ko\.md\|edition\|rule-changes'`) | No row of either touches editions or the rule-change grammar. |

## Scope

In:

1. Passage A in Korean. The Korean paragraph opening **이 플러그인이 어느 언어로 쓰는지는** (`docs/layout/one-root-by-lifetime.ko.md:217-221`) gains, after its last sentence and before its `check:` line, the Korean of the English sentences G3 names as passage A. The text is *Data & interfaces*, item A.
2. Passage B in Korean. The Korean paragraph opening **키가 둘인 것은** (`.ko.md:224-232`) gains, as its last sentences, the Korean of the English sentence G3 names as passage B. The text is *Data & interfaces*, item B.
3. The edition rule in the grammar. `skills/settle/rule-changes.md` *Rule changes* gains one paragraph at the end of its own text, after the paragraph opening `` `skills/settle/scripts/rule_changes.py` is the one reader. `` and before `## A rule has one shape`. The text is *Data & interfaces*, item C. It carries no `check:` line: no case holds it, and review reads it (`skills/settle/rule-changes.md` *A rule has one shape*).

Out:

- Retiring the Korean edition, option (b) of the issue. The owner decided (a) on 2026-11-10 (G2).
- A case or a `chain-check` arm that refuses a design naming an English edition and not its Korean one (`frame/plan.md` *Alternatives considered*, row D).
- `CONTRIBUTING.md` *House rules* and `docs/checks/the-fold.md`: both stay true (G7).
- `README.ko.md` and `docs/experiments/`'s Korean files. The first is outside the policy root and is #1492's file; the second is no policy (G9).
- The *Naming* table's `AgenticSeal` row, where the Korean edition names `README.ko.md` and the English one `README.md`. Each edition names its own reader's README, a localisation and not a gap; neither name is a backtick span.
- The version. #1495 moved `.claude-plugin/plugin.json` to 0.37.1, and this work does not move it.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. The tokens agree | Given the built tree, when every backtick span of each edition is listed once and the two lists are compared, then they are equal: no placeholder of this document is translated, so equal is what *Done when* (a) asks | `executed`: each edition's backtick spans listed by `grep -o` and `sort -u` into a file under the phase's scratch directory, and `diff` of the two files prints nothing |
| S2. A Korean reader learns the keys are required | Given the Korean edition, when a reader reads the paragraph opening **이 플러그인이 어느 언어로 쓰는지는**, then it says that the two keys are required, that first setup and the batch before a work item's first edit ask for them with the recent PR titles' language shown, that `seal pr-body` refuses without them, that where nobody can answer the orchestrator writes the titles' language and `routing.md` says so, and that a commit is never refused for them | read, sentence for sentence against `.md:231-237`, by the crafter and then the sealer |
| S3. A Korean reader learns what the body opens with | Given the Korean edition, when a reader reads the paragraph opening **키가 둘인 것은**, then its last sentences say that where the keys differ the body opens with `pr.<lang>.md`, the quotes of `pr.md` in the team's language, and `pr.md` follows | read, against `.md:250-253` |
| S4. The outline and the check lines stand | Given the built tree, when the edition case runs, then it passes, and the diff of the Korean edition adds no heading and changes no `check:` line | `tests/behaviour/test_both_editions_carry_the_same_folds.py` and `tests/behaviour/test_first_setup_asks_once.py`; `git diff` of the edition |
| S5. The framer and the settling session meet the rule where they read | Given `skills/settle/rule-changes.md`, when a framer opens *Rule changes* to write operations, or a settling session opens the file before step 4, then the section's last paragraph is item C, wrapped within 88 display columns, and the cases reading the file pass | `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_settle_applies_rule_changes_in_place.py`, `tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py`, `tests/behaviour/test_a_phase_hands_the_next_one_a_record.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` |

## Data & interfaces

Each item is the text to insert. The crafter wraps it to the lines around it
and may improve the Korean wording; S2 and S3 are what it must say.

**A.** Appended to the Korean paragraph of *Scope* item 1, as its own
sentences inside that paragraph:

> `seal/config.json` 의 두 언어 키는 반드시 있어야 합니다. 처음 설정과, 작업
> 항목의 첫 편집 전에 한 번에 묻는 질문이 두 키를 묻고, 그 질문 옆에 최근 PR
> 제목들의 언어를 보여 줍니다. `seal pr-body` 는 두 키가 없으면 본문을 만들지
> 않고 거절합니다. 답할 사람이 없으면 orchestrator 가 제목들의 언어로 두 키를
> 쓰고, `routing.md` 에 그렇게 했다고 적습니다. 커밋은 이 키 때문에 거절되지
> 않습니다.

**B.** Appended to the Korean paragraph of *Scope* item 2, as its last
sentences:

> 두 키가 서로 다르면 PR 본문은 `pr.md` 의 인용을 팀의 언어로 옮긴
> `pr.<lang>.md` 로 시작하고, 그 뒤에 `pr.md` 가 옵니다. 그래서 기록은 언어
> 하나를 지키고, 팀은 본문을 자기 언어로 읽습니다.

**C.** A new paragraph at the end of `skills/settle/rule-changes.md`
*Rule changes*, with a blank line before it and before `## A rule has one
shape`:

> **An operation on a document whose row in the index (*The index* below)
> names a `.ko.md` edition carries one on that edition, in the same design.**
> The settling session writes only the sections its groups name, so an
> edition that no operation names keeps its old text, and after the settle the
> two editions state different rules. The design's framer writes the
> edition's operation with the edition's own heading as its `section` and the
> edition's own text as its `from`, and with a `to` that says in Korean what
> the English `to` says; a check line stays English in both. Where the
> settling session meets a group on one edition and none on the other, it
> writes the other edition's section to the same decision in step 4 of
> `skills/settle/SKILL.md` *The settling session's procedure*. Whether the two
> `to` values say the same is review's to read: the proofer's at the design's
> review, and the owner's at the settle's pull request.

## Rule changes

- nothing
  why: this work item's subject includes the policy root's text, so it edits `docs/layout/one-root-by-lifetime.ko.md` in place in its pull request, as `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* permits (G1); the two passages it translates state rules the English edition already states (G3), so the policy in force does not change. The rule it adds stands in `skills/settle/rule-changes.md`, outside the policy root, and no document the index `docs/README.md` names states how a design writes an operation on an edition (G8). No unsettled design stands beside this one, and this work moves no document or section (G13).

## Removes

- nothing
  why: the work adds one rule, *Data & interfaces* item C, whose catch record is G5: a released design named the English edition alone and the settle left the Korean edition two passages behind. No text of the tree states the rule for operations (G8), so no copy goes. The edition rule it applies, `CONTRIBUTING.md` *House rules* and `docs/checks/the-fold.md`, states what both editions owe and stays (G7). The two translated passages add Korean text and replace none.

Framed 2026-11-10 by framer, before the build.

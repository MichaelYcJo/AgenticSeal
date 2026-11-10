# Implementation Plan: 1794271936-the-korean-edition-lacks-two-passages (#1491)

## Technical context

The tree as read at `765f146ff`.

The build touches two files. `docs/layout/one-root-by-lifetime.ko.md` (258
lines) lacks the two passages `frame/design.md` *Grounding* G3 locates, both
in *저장소가 스스로 정하는 것, 그리고 그것을 읽는 방법*; no heading and no
`check:` line changes. `skills/settle/rule-changes.md` (131 lines) gains one
paragraph at the end of *Rule changes*, its text fixed in `frame/design.md`
*Data & interfaces* item C. That file is held to 88 display columns by
`tests/behaviour/test_docs_line_wrap.py`, and the other cases G11 names read
parts of it that the new paragraph does not touch. The Korean prose follows
`skills/writing-style/SKILL.md` `## 문장 규칙`, and the wording `README.ko.md`
already uses for the same facts (G12).

The failure scenario in six months: a design written by a session with no
framer names the English edition alone, the work item routes straight to
the pull request with no proofer round, and the settling session reads the
group without reaching the last paragraph of *Rule changes*. The Korean
edition then falls behind again, as it did at G5, and only a reader comparing
the two editions finds it. The sentence lowers that risk at the two parties
that write the text, and holds nothing by itself; row D is the mechanism
that would, and its cost is weighed there.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Translate the two passages, and add one paragraph at the end of *Rule changes* that tells the design's framer to write the Korean operation and the settling session to write a Korean section no group names; review reads it | The scenario under *Technical context*: a party that does not read the paragraph lets an English-only design through, and nothing refuses it | Chosen. It is the owner's option (a) (G2), and it reaches both parties that write the policy text: the framer at the design, and the settling session at the settle, which no proofer reads (G6) |
| B. The paragraph addresses the design's framer alone, in the owner's words and no further | A design that misses the Korean operation, as `1794188289` did (G5), reaches a settle that passes no proofer (G6). The settling session writes only its groups' sections, so the miss repeats exactly as at `e5370691d` | Rejected. The clause for the settling session costs one sentence in a file that session already opens before step 4, and it covers the one step at which the G5 miss happened |
| C. The paragraph goes at the end of *The index*, beside the sentence that already names a `.ko.md` edition | `agents/framer.md`, `skills/implement/SKILL.md` and `docs/README.md` send the design's author to *Rule changes* (G8). A framer that reads that section to write operations never reaches *The index*'s last paragraph | Rejected. Item C cites *The index* for what an edition's row is, so the fact stays in one place |
| D. A `chain-check` arm, or a case over the released designs, that refuses a design whose operations name an English edition and never its `.ko.md` edition. File presence is an exact fact a script reads | A new arm of the check every ready pull request runs, kept against one catch (G5) in the record. Whether the Korean `to` says what the English one says is still review's, so the arm would hold the file and not the meaning. It adds a mechanism and nothing goes in return | Rejected. The owner decided (a) with a sentence and no check (G2); `skills/core/SKILL.md` *The rule a mechanism is kept against* weighs one catch against a permanent arm. A second miss after this rule stands is the record that would reopen it |
| E. Retire the Korean edition, the issue's option (b): remove the document's Korean edition and point `README.ko.md` at the English one. This replaces the structure that costs the operations | No failure in the tree: the operations and this gap go with the edition. A Korean reader loses the document they read at first setup | Rejected. The premise that keeps the structure is the owner's decision of 2026-11-10 to keep the edition for that reader, checked in the issue body under *Decided* (G2) |
| F. The settling session's clause goes into `skills/settle/SKILL.md` *The settling session's procedure* step 4, and only the framer's clause into `skills/settle/rule-changes.md` | The edition rule then has two homes, each stating half of it, and a fix to one leaves the other stale | Rejected. The settling session opens `skills/settle/rule-changes.md` before step 4 (`skills/settle/SKILL.md`, its opening paragraph), so one paragraph reaches both parties |
| G. A text case that pins the new paragraph's wording | It pins a sentence, not a behaviour: contract rule 14 asks a pin for a message or a verdict a person acts on, and `skills/settle/rule-changes.md` *A rule has one shape* gives a rule no case holds no check line | Rejected. Review reads the paragraph, as it reads every rule with no check line |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2 and 3 | `frame/design.md` *User scenarios & acceptance* S1 to S5: the token comparison of S1, run in the phase's scratch directory, prints nothing; the cases S4 and S5 name pass, run narrow; S2 and S3 read sentence for sentence against the English edition | `2ba8bb052` |

## Overlap with the release

The spawn names three other work items of 0.37.1, and none meets this work.
#1490 changes `docs/releasing/`, comments in `.github/scripts/` and
`tests/behaviour/test_release_hygiene.py`. #1492 changes `README.md`,
`README.ko.md` and `docs/checks/the-stamp.md`; `README.ko.md` is a Korean
edition outside the policy root, and `docs/checks/the-stamp.md` has none, so
the new paragraph of `skills/settle/rule-changes.md` does not apply to its
change. #1493 changes `seal/follow-up.md`, `skills/implement/SKILL.md` (the
Status sentence of *3. The SDD file set*, by its issue's row 2) and cases
under `tests/text/` and `tests/github/`; it does not touch *Document layout —
two roots, three lifetimes*, the clause G1 stands on. None of the three
changes either file this work changes, or a rule or check that reads them.
Each was read from its issue body (`executed`: `gh issue view`), since each
branch carries only its routing commit (G13).

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|

## Operational impact

None. No migration, no key, no dependency, and no compatibility break. The
pull request does not move the version: #1495 moved
`.claude-plugin/plugin.json` to 0.37.1.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-10 | The title takes `docs:` | The diff changes a Korean policy document and a skill's grammar text, and no executed line; `### Changed` names a rule of the design grammar, which the settling session reads as text, not a new capability, so the patch carries no `feat:` | `~/.claude/skills/commit-pr-convention/SKILL.md`; `docs/releasing/branch-and-release.md` *Cutting a release* |

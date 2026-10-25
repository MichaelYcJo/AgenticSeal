# 1792540458-on-demand-files-state-the-current-rule — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 92a89dc7 |


## What this phase was asked

The two writing rules the owner gave on 2026-10-21, written into
`skills/writing-style/SKILL.md` as one `###` section under `## 구성 규칙`, in
that section's language: three rules, each one bold sentence with its grounds
and its own `check:` line (`spec.md` *Data and interfaces*), each citing its
instances from Scope 1 in one line. A link line in `## English prose rules`
and in `## 문장 규칙`. The skill's description names text an agent or a check
reads among its uses. Each new pin is seen red with its sentence deleted. The
spawn also asked that every imperative sentence the phase rewrote whose actor
or condition the smith had to choose be listed here for the warden.

## What this phase found

**The frame holds for this phase.** `## 구성 규칙` stands as the prefix of the
heading `## 구성 규칙 — 문장보다 이쪽이 더 크게 작용한다`; the section was put
under it without renaming it, because `## 구성 규칙` is the spelling both
language sections and `tests/test_a_language_section_of_writing_style_opens_alone.py`
name, and the frame keeps this file's prose out of the rewrite (`spec.md`
*Out, and whose*).

**The section is `### 에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다`**,
placed after *여럿이 가질 수 있는 것은 누구 것인지 밝힌다*. The second rule
links that section for whose and for its `seal` instance rather than stating
either again, so the instance of one word read three ways stands once.

**The instances, one rule each.** The first rule cites the approval line
whose appended sentence made its old reader see no approval. The third cites
"So is" (#953's sealer), "The one writer that does is `settle`"
(`seal/specs/1792449518-settle-squashes-specs-into-docs-in-place/spec.md`)
and "the session" in a file two parties read. The second cites the `seal`
instance through the link above.

**The pin** is
`tests/test_a_language_section_of_writing_style_opens_alone.py#test_the_rules_for_text_an_agent_or_a_check_reads_reach_both_languages`,
in the module that already holds the two language sections. Seen red against
the tree before the section was written (executed). After the commit,
`mutation-check` turned it red under each of five mutations (executed): the
English link's italics removed, the Korean link's italics removed, the
description phrase broken, a second target added to one `check:` line, and the
section's heading raised to `##`, which takes it out from under `## 구성 규칙`.

**Imperative sentences whose actor or condition the smith chose**, for the
warden to read:

| Sentence | What was chosen |
|---|---|
| `## 문장 규칙`: 에이전트나 검사가 읽는 글(스킬, 에이전트 정의, 템플릿, 프레임)을 쓴다면 … 세 규칙도 따른다 | the actor is whoever writes that text, left unnamed because every party that opens the section writes; the condition is the kind of text |
| `## English prose rules`: Text an agent or a check reads … also follows the three rules | the same choice; the text is the subject, so the sentence names the kind of text rather than a party |
| rule 1: 그 자리는 낱말로 쓴다 | the condition is a symbol used as a separator inside a heading or a sentence, so a table's pipes and a code span are not covered |
| rule 1: 검사가 읽는 줄은 정해진 철자 하나만 읽히고 조금 틀린 철자는 그 줄에서 거절되어야 한다 | the actor is the check, not the writer: the writer's act is to choose a shape whose near miss a check refuses |
| rule 3: 하는 쪽은 orchestrator, framer, smith, warden, sealer 처럼 이름으로 적는다 | the five names are the spec's; the scribe is left out, as in Scope 1 (b) |
| rule 3: 두 당사자가 함께 여는 파일에서는 "you" 나 "the session" 이라고 쓰지 않는다 | the condition is a file two parties open; a file one party opens may still say "you" |

**Census (S11).** Nothing was removed in this phase, so no instruction lost a
home and no case pinned a removed sentence.

**Restatement pairs of this phase's file** (Scope 10, measured at the commit
with the module's own `shared_counts`, executed):
`skills/writing-style/SKILL.md` and `skills/writing-style/outside-the-review.md`
share 3 runs, as `BASELINE` holds. Both files are `writing-style`'s and the
pair is phase 9's to drain or keep.

**Measured for the later phases at the same commit** (executed), so phase 9
has the before: `CLAUDE.md` and `CONTRIBUTING.md` share 0 runs against a
baseline of 14; `agents/smith.md` and `templates/claude-md-block.md` 0 against
13; `skills/implement/orchestration.md` and `templates/sdd-routing.md` 4
against 10; `agents/smith.md`, `skills/code-review/orchestration.md` and
`skills/implement/SKILL.md` each 0 with `skills/implement/orchestration.md`,
against 1, 7 and 1.

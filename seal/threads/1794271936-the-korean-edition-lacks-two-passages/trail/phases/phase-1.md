# Phase 1: 1794271936-the-korean-edition-lacks-two-passages

## What this phase found

**The frame held against the tree.** Before the build, each coordinate
`frame/design.md` *Grounding* G3 names was opened at `ee69aa042`: the
English passages stand at `docs/layout/one-root-by-lifetime.md:231-237` and
`:250-253`, and the two Korean paragraphs at
`docs/layout/one-root-by-lifetime.ko.md:217-221` and `:224-232`. The place
*Scope* item 3 gives for the new paragraph, after the paragraph opening
`` `skills/settle/scripts/rule_changes.py` is the one reader. `` and before
`## A rule has one shape`, exists as stated. `skills/settle/SKILL.md` opens
by saying the settling session opens `skills/settle/rule-changes.md` before
step 4, and step 4 is where it writes each group's section, as G6 and item C
state.

**S1 was seen red before the build and is empty after it** (`executed`).
Each edition's backtick spans were listed with `grep -o` and `sort -u` into
the phase's scratch directory. Before the build, `diff` printed the two
English-only spans G3 names, `` `pr.<lang>.md` `` and `` `seal pr-body` ``,
and exited 1. After commit `2ba8bb052` it printed nothing and exited 0.

**The Korean wording departs from *Data & interfaces* items A and B where
`skills/writing-style/SKILL.md` `## 문장 규칙` asks.** The design lets the
crafter improve the wording, and S2 and S3 fix what it must say. The
departures, judged against the third point of *영어를 옮길 때는 구조를
버리고 뜻만 가져온다* (an inanimate subject carried over from English):

- Item A's "질문이 두 키를 묻고" made the question the one asking. The text
  now says when the keys are asked: "처음 설정할 때와, 작업 항목의 첫 편집
  전에 질문을 한꺼번에 물을 때 두 키를 함께 묻고". "한꺼번에" is the word
  `README.ko.md` uses for the same batch (G12).
- Item A's "제목들의 언어" became "제목들이 쓰인 언어", and "orchestrator 가
  제목들의 언어로 두 키를 쓰고" became "orchestrator 가 두 키를 그 제목들의
  언어로 적고, 그렇게 했다는 것을 `routing.md` 에 남깁니다".
- Item A's last sentence, "커밋은 이 키 때문에 거절되지 않습니다", became
  "두 키가 없어도 커밋은 거절되지 않습니다", which names the case the English
  "never refused for them" covers.
- Item B's "두 키가 서로 다르면" became "두 키가 서로 다른 언어를
  가리키면", the wording `README.ko.md:308-309` uses. Its "기록은 언어 하나를
  지키고" became "기록은 한 언어로 남고".

Item C stands as the design wrote it, wrapped to the file's lines; every
added line is at most 76 display columns, under the 88 that
`tests/behaviour/test_docs_line_wrap.py` holds. The Korean lines are at most
78 display columns, the width of the lines around them.

**S2 and S3 were read sentence for sentence against the English edition**
(`read`). Passage A's five statements, the keys required, who asks them
with the titles' language shown, `seal pr-body`'s refusal, the
orchestrator's default recorded in `routing.md`, and no commit refused, each
have one Korean sentence in that order. Passage B's statement, the body
opening with `pr.<lang>.md` followed by `pr.md`, and its consequence for the
records and the team, have two.

**No heading and no `check:` line changed** (`read`, `git diff ee69aa042
2ba8bb052`): both Korean additions sit inside their paragraphs, item A
before that paragraph's unchanged `check:` line.

**No case was written new, and no `seal mutate` run is owed.** The phase
changes prose only. `skills/verify/SKILL.md` *The narrow command still has to
be able to fail* gives prose the row "whatever actually parses those files",
and the cases S4 and S5 name are those parsers. `frame/plan.md`
*Alternatives considered* row G rejected a text case pinning item C, and
`skills/settle/rule-changes.md` *A rule has one shape* gives a rule no case
holds no check line. No unit adds behaviour, so no unit has anything to
break.

**No removal beyond the frame's `## Removes`, and no other statement of the
rule needed a change.** `git grep -n -i edition` over `skills/`, `agents/`,
`docs/`, `templates/` and `CONTRIBUTING.md` lists the two statements G7
names and the new paragraph. Both of G7's statements say what the two
editions owe and stay true beside it. That list is a sample: the search
finds the word "edition" and not a statement of the rule in other words.

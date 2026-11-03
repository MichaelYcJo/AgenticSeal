# Phase 3: 1793732301-the-readme-is-written-for-a-first-reader

## What this phase found

**The frame holds for this phase.** Read before the build at 7a3920e1d:
`docs/layout/one-root-by-lifetime.ko.md` has the heading
`### shared 인가 local 인가`, and
`docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.ko.md`
exists, so the Korean edition links those two Korean editions where the
English edition links their English ones. Every other document either
edition links has no Korean edition (`git ls-files '*.ko.md'`), so the
Korean edition cites it by its English path and heading. The Korean arms
phase 2's record names are the whole list of arms that pin a Korean
sentence: `git grep -l README.ko -- tests` lists eighteen modules, each in
the pin table and in this phase's narrow set, and a `git grep` of those
modules for Hangul found no other Korean literal of the edition. Q1 and Q2 stay open, and the Korean edition follows Q2's
default (a), as the English one does.

**The outline the Korean edition takes** is the English one, level for
level: `# AgenticSeal`, `## 설치`, `### 업데이트`, `## 첫 작업 항목`,
`### shared 인가 local 인가`, `## 동작 방식`, `### 누가 무엇을 하나`,
`### 리뷰 체인`, `### 기록이 남는 곳`, `### 마이그레이션`,
`## 내 컴퓨터에서 도는 것`, `## 명령`, `## 한계`, `## 기여`, `## 언어 정책`,
`## 라이선스`. The subsection *shared 인가 local 인가* keeps the Korean
policy edition's heading, so a reader who follows the link meets the same
words.

**The Korean edition read against the English one, section by section**
(read, at 9acaef644). Each section carries the English section's facts in
the same order, and links the same homes:

- The first screen: the owl with Korean alt text, the title, the sentence,
  the badge and the switch, the three paragraphs (what the plugin does,
  why the parties are separate, the three labels), and the `mermaid`
  chart with the same nodes, its labels in Korean and the party names in
  their original spelling.
- *설치* and *업데이트*: the Python 3.12 floor and why, `python3 -V`, the
  macOS and version-manager cases, the `py -3` fallback, the three install
  commands, nothing written into `CLAUDE.md`, the auto-format tools,
  uninstall, `/agentic:update`, the restart, the two by-hand commands and
  why both, and the old block with `templates/setup/claude-md-block.md`.
- *첫 작업 항목*: the request in one's own words, the orchestrator, the
  work item, the first-setup question, the three routing answers, the
  orchestration section, `routing.md` read by the hooks, the default under
  `automation`, the parties in turn, the broad gate once, the stamp, its
  image and `docs/checks/the-stamp.md`.
- *shared 인가 local 인가*: the three-row table, local mode's fit, the
  `seal mode` block, the way back's citation, `seal/README.md` for the
  by-hand moves, the `seal pr-checks` block, the workflow left behind, the
  export and import block, `.incoming`, the one refusal, `seal import
  --help`, and why a copy is not a sync.
- *동작 방식* and its four subsections: the core and the study, the parties
  table row for row, the review chain with its three links and its last
  sentence, the records with their two citations and the `check:` line,
  and migrations.
- *내 컴퓨터에서 도는 것*: one row per `GROUPS` script, the worktree
  sentence, the side effects, and the network paragraph. The version-check
  row carries the clause K4 found missing: "`/agentic:update` 와 릴리스를
  불러오는 두 방법을 짧게 알린다".
- *명령*, *한계*, *기여*, *언어 정책*, *라이선스*: the same fourteen rows,
  six bullets and paragraphs. Two command rows name their placeholder in
  Korean, `<트랜스크립트>` and `<경로>`, as the old Korean edition did.

The Korean edition differs from the English one in two ways, both from
`skills/writing-style/SKILL.md` *문장 규칙*. It unpacks each coined term at
its first use (orchestrator, framer, crafter, proofer, sealer, fix pass,
broad gate, seal, the hooks), under *용어는 실물을 확인하고 고른다*, where the
English edition names the parties first in its chart and lets its prose
carry them. And it splits a sentence the English edition joins wherever a
Korean sentence would otherwise carry an inserted clause, under *영어를
옮길 때는 구조를 버리고 뜻만 가져온다*.

**The sentence under the Korean title is one sentence.** The first draft
gave it as two. `docs/layout/one-root-by-lifetime.ko.md` *이름* says that
the plugin's one sentence stands under the title of `README.ko.md`, so
9acaef644 joins them. No case reads the Korean line: *Scope* 7 and S2
hold the English edition's paragraph against the manifest, and the Korean
line is a translation the manifest does not carry. Judged against
`frame/design.md` *Grounding*, whose *Naming* row cites the English policy
sentence only, and contract rule 19. This is the one statement the build
met that the frame does not name.

**The Korean pins kept their literals where the new wording kept the
phrase.** The plan's pin table expected the Korean literals of
`tests/behaviour/test_chain_hooks_hardening.py` and
`tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py`
to follow a new wording. The new edition keeps each pinned phrase: the
`| 게이트 |`, `| 스킬 |` and `| 코어 |` row heads, "알아서 로드", the network
sentence, and the stamp's side-effect phrases. So neither module changes,
and both pass against the new edition. Each phrase reads as a complete
Korean sentence or cell where it stands. Two pins moved with the wording:

- `READMES["README.ko.md"]` in `tests/behaviour/test_first_setup_asks_once.py`
  takes `## 첫 작업 항목`, and the subsection keeps its heading.
- `LEFT_BEHIND["README.ko.md"]` takes the edition's two sentences on the
  workflow a move to local leaves. The old sentence called a release pin
  "고정" with no noun it belonged to. The new one says a workflow file is
  fixed to a release, and links the Korean policy edition.

The two pins of facts the page now links lose their Korean arm, as the pin
table says: the `README.ko.md` entry of `readers` in
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, and the
`README.ko.md` row of
`tests/behaviour/test_unverified_rows_close.py::test_the_documents_state_the_merge_base_footing`.
With that row gone, nothing read `TIP_KO`, so the constant goes, and the
comment over `TIP_EN` and the case's docstring no longer speak of one
phrase per language. The docstring of
`test_the_readme_gives_the_switch_under_the_first_work_item` now says the
by-hand moves left both editions.

**The cases, each seen red** (executed):

- Before the Korean edition was written, the repointed
  `test_the_readme_gives_the_switch_under_the_first_work_item[README.ko.md]`
  ran red against the old edition, on the heading `## 첫 작업 항목`, which
  it did not have. `test_every_paired_document_carries_the_same_headings`
  was red from phase 2 on, as the plan expected.
- After the commit 267b2d201, three `seal mutate` runs over `README.ko.md`
  each read `red`. `### 업데이트` changed to `## 업데이트` turned the outline
  case red. `## 첫 작업 항목` changed back to `## 처음 실행`, and the
  `LEFT_BEHIND` clause "파일의 고정은 어떻게 바꾸는지는" changed to "파일은
  어떻게 옮기는지는", each turned the switch case's Korean arm red. Each run
  restored the file, and `git diff --quiet HEAD` exited 0 after them.
- The repoints add no behaviour: a case points at a new heading or a new
  sentence, or a parametrisation loses a row. So they owe no mutation run
  of their own (`skills/verify/SKILL.md` *The narrow command still has to
  be able to fail*). The runs above are the Korean edition's, a prose file
  whose readers are those cases.

**The narrow set** (executed, one command, over the tree 9acaef644
commits): `bin/test -q`
over the twenty-five modules of the pin table and the five that read every
tracked `.md` or test file (`test_a_cited_section_stands_in_its_file.py`,
`test_one_heading_rule_holds_to_commonmark.py`, `tests/test_censuses.py`,
`tests/text/test_a_cited_commit_outlives_the_squash.py`,
`test_a_shrunken_corpus_declines_to_judge.py`). 785 passed and none
failed. The outline case passes, and so does the census case, whose line
the fold commit 7a3920e1d changed. Phase 2's run of the same set counted
786 cases, and this one counts 785, because the `README.ko.md` row of the
merge-base case is gone. A run of the same set before the first commit
failed once, on
`test_prose_stays_within_the_wrap_limit[README.ko.md]`, which named line
376 at 96 columns. The line carried a link, and was re-wrapped. `uvx ruff
check` and `uvx ruff format --check` over the three changed test modules
exited 0.

**Other statements of the facts this phase moved** (contract rule 19). The
method is `git grep` outside `seal/threads/` and `README.ko.md` for
`README.ko`, `처음 실행`, `치트시트`, "Korean README" and "Korean edition",
with each hit read. A search on words makes this list a sample.

- `docs/layout/one-root-by-lifetime.ko.md` *이름*: the one sentence under
  the title. 9acaef644 makes the Korean edition agree, above.
- `docs/checks/the-session-hooks.md:19`: one gate-table row per `GROUPS`
  script in each edition. It stays true.
- `docs/layout/the-record-layout.md:179`, `CONTRIBUTING.md:431` and the
  hygiene step at `.github/workflows/hygiene.yml:177`: what the editions
  are, where Korean belongs, and the warning when one edition changes
  alone. Each stays true.
- `skills/settle/scripts/passages.py:55` and the paste check's docstring
  say a Korean edition is a mirror the corpus leaves out. They stay true.
- `.test_durations` still names `README.ko.md` rows of cases that have
  gone or been renamed. It is the runner's timing file, and this phase
  does not edit it, as phase 2 did not.

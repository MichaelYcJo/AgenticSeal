# Feature Specification: 1793174170-two-facts-kept-in-several-files-have-drifted

Issue #1055. Every coordinate below was opened at `5287dd42`, the commit this
branch was cut from; the branch's only later commit, `0e48c569`, adds
`routing.md` and nothing else.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against*: "A fact has one source, and every other place links to it." | Each of the seven facts gets one file that states it. Every other place links to that file, or is derived from it by a case that fails on a difference. |
| `CLAUDE.md` *The rule a mechanism is kept against*: "Nothing is kept beside the tree to stay in step with it, such as a stored count or coordinate." | A count in prose goes, and so does `NUMBER_WORDS`, the table of number words a case keeps so that it can read a count. A case reads the list a count stood for: the names in `hooks/dispatch.py#GROUPS`, or the skills under `skills/`. |
| `CLAUDE.md` *The rule a mechanism is kept against*: "A change rewrites the text it amends in place, and in the same commit removes what stood on the old fact: a check, an exception, a comment, a copy." | Each assertion that pins a removed sentence is removed or re-pointed in the commit that removes the sentence (`## Removes`). |
| `docs/the-record-layout.md` *The record layout*, opening: "A file that states a rule this index gives another home links to that home and does not restate it ... Where a copy is found, the copy is the defect." | The two pasted passages `tests/text/test_no_passage_is_pasted_into_a_second_file.py#BASELINE` carries for this issue are removed from the second file. The work does not argue them in place. |
| `docs/the-agent-set.md` *One contract every agent receives, and one definition each*, `:37-46` | This section is the one home of "The party that draws a contract is not the party that executes it." `skills/implement/SKILL.md` *3. The SDD file set* links to it. |
| `docs/one-root-by-lifetime.md` *Shared or local*, `:182-188`: "The mode is not a one-way door; the history is." | The policy already states the rule behind the warning. The warning is what a person is told before `seal mode shared`, with the way back before the commit. It gets one home, and that home cites this paragraph for the rule. |
| `docs/the-session-hooks.md` *Registration*: "adding one means adding it to `GROUPS` in `dispatch.py`" | `GROUPS` is the one list of the hooks the plugin registers. The README's gate table is derived from it, and `## Rule changes` adds that rule to this section. |
| `CONTRIBUTING.md` *House rules*, `:431-436`: "Both READMEs move together, and so does every document with a `.ko.md` edition." | The outline case reads every pair this sentence covers. Today it reads `docs/` top-level pairs only. The sentence says which case reads the rule, and it is rewritten in place to name every pair. |
| `tests/text/test_ci_gives_the_checks_what_they_need.py`, module docstring: "Each workflow that runs on `pull_request` cancels its own runs still in progress for the same pull request" | The reason holds for the workflow the plugin ships, which runs on `pull_request` in a user's repository. So the template gains `concurrency` as well as the `permissions` block #359 gave the repository's own file. |

## Scope

In scope. The issue's seven items, each given one source:

1. **The gate list.** The gate table of `README.md` *The gates* and of
   `README.ko.md` *게이트* holds one row for each script that
   `hooks/dispatch.py#GROUPS` registers, and a case derives the table's rows
   from `GROUPS`. Today `GROUPS` registers 15 scripts and each table holds
   13 rows. The work adds the two missing rows, `worktree_consent` and
   `root-migrate`. The count "Nine of the thirteen gates" (`README.md:417`,
   `README.ko.md:408`) goes. So do the lists of gate names in prose that
   repeat the table's Where column: `README.md` *First run* `:417-431`,
   `README.ko.md` *처음 실행* `:408-422`, and the `seal/` row of
   `README.md` *Where the records live* `:114` and of `README.ko.md`
   *저장소에 남는 기억* `:110`. Those sentences point at the Where column instead.
2. **The way back before the commit to shared.** It is told in
   `README.md:524-532`, `README.ko.md:517-526` and `skills/config/SKILL.md`
   *Before switching to shared, say what cannot be undone* `:163-172`. After
   the work, `skills/config/SKILL.md` is its one home among the documents.
   Both READMEs link to that section and no longer spell
   `git reset -- :/seal`. The section takes in the reasons only the README
   gave: the switch stages, the guard refuses a switch over a staged change,
   and the pathspec is there because a bare `git reset` unstages the whole
   index. `skills/implement/scripts/seal.py#indexed` holds the refusal (read).
   For the rule that the history is the one-way door, the section cites
   `docs/one-root-by-lifetime.md` *Shared or local* instead of restating it.
   It keeps the words "point of no return", which
   `tests/text/test_the_settings_have_a_front_door.py` pins.
3. **The shipped workflow and the repository's own.**
   `templates/setup/hygiene.yml` is the one source of the two steps it shares
   with `.github/workflows/hygiene.yml`: "a declared review chain has the
   round record it claimed" and "the mode the row declares is the mode the
   folder is in". The template gains `permissions: contents: read` and the
   `concurrency` block the repository's file carries. The repository's
   comments on the two shared steps go, and one comment line points at the
   template. The template's comment on the chain step stops listing the
   checker's refusals and names the plugin's `docs/the-review-record.md`
   *What the check reads at the pull request*, which owns that list. A case
   compares the shared steps, and `test_ci_gives_the_checks_what_they_need.py`
   reads the template as well as `.github/workflows/`.
4. **Counts in prose.** No count of gates, rules, hooks, lines or skills is
   left in prose:
   - the heading "Why the always-on context is 12 lines" and its Korean edition;
   - the CLAUDE.md block row's "12 always-on lines, four section headings ...
     over eight rules: one on tooling, three on safety, one on session cost,
     three on git" (`README.md:45`, `README.ko.md:45`). The row keeps
     `templates/setup/claude-md-block.md` as the block's one source, and
     lists neither the block's sections nor its rules;
   - "Two hooks reach the network" (`README.md:223`, `README.ko.md:216`) and
     `CONTRIBUTING.md:441-448`'s "Two hooks ... both ... A third ... the
     second". The README section names `lint-python` and `version-check`
     without a count. `CONTRIBUTING.md` says that every hook that reaches the
     network is named there, and that a new one needs the limits
     `version-check` carries;
   - the skills row's "Fourteen, in three groups ... The one ... Nine more ...
     Four" (`README.md:43`, `README.ko.md:43`). In its place, a case reads
     the names the row lists against the on-demand group, which it derives
     from the skills' and agents' frontmatter.
5. **Translated editions outside `docs/`.**
   `tests/behaviour/test_both_editions_carry_the_same_folds.py#pairs` reads
   every tracked `X.ko.md` that has an `X.md` beside it, wherever it stands.
   At `5287dd42` those are `README`, `docs/one-root-by-lifetime`,
   `docs/experiments/README` and
   `docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force`. All four
   agree on their outline (executed, a heading-level comparison written for
   this frame that skips fenced blocks). `CONTRIBUTING.md:431-436` is
   rewritten in place to say the case reads every pair.
6. **Passages pasted into a second file.** The 20 runs shared by
   `docs/the-agent-set.md` and `skills/implement/SKILL.md` are one sentence,
   at `skills/implement/SKILL.md:355-359`. It is replaced by a link to
   `docs/the-agent-set.md` *One contract every agent receives, and one
   definition each*. The README and `skills/config/SKILL.md` pair is item 2's
   passage (executed, a 15-word window comparison: 21 runs, all of them that
   passage). Both pairs leave `BASELINE`.
7. **The plugin's description.** `.claude-plugin/plugin.json`'s
   `description` is the one source. JSON cannot link, so a case fails when
   `.claude-plugin/marketplace.json`'s top-level `description` or its plugin
   entry's `description` differs from it.

Out of scope, and whose it is:

- **#1102** rewrites both READMEs for a first reader, last in the milestone.
  This work changes only the sentences named above, and adds two rows to
  each gate table. The README's side-effects paragraph under *The gates*
  holds no count and no copy, though it does not name what `worktree_consent`
  and `root-migrate` write; the new rows state that. Folding the paragraph is
  #1102's. #1102 inherits the cases this work adds, and they hold its rewrite
  to the same sources.
- **#1110** rewords `skills/implement/SKILL.md` after #1041. This work edits
  one paragraph of *3. The SDD file set*, `:355-364`, and no other line of
  that file.
- **#1053** changes the release scripts and docs, and **#1117** the release
  tail. Of `.github/workflows/hygiene.yml` this work touches only the
  comments of the two steps the template shares. The release steps (version,
  changelog fragments, milestone, the issue-claims report) are theirs.
- **#1041** owns `chain_check.py` and `docs/the-review-record.md`. The template
  links to the review record's section by its heading instead of listing the
  refusals, so a change #1041 makes to the refusals changes no comment here.
- **#1056** owns `hooks/worktree_consent.py` and its tests. The new
  `worktree_consent` row describes the hook as it is at `5287dd42`, and the
  case reads only the row's name.
- **The text `seal mode shared` prints** (`skills/implement/scripts/seal.py:2546-2556`
  and `:2674-2679`, pinned by `tests/skills/test_seal.py:3137`). It is what a
  person reads at the moment of the switch, and its own case holds it. It is
  output, not a document that restates one, and it stays.
- **The other `BASELINE` pairs.** The agent definitions' pairs, and the
  README's pairs with `skills/implement/SKILL.md`,
  `skills/implement/orchestration.md` and `skills/parity-setup/SKILL.md`, are
  not in #1055's list.
- **Drift inside a section of two editions.** No case can tell whether a
  Korean sentence says what an English one says, and a reading guessed from
  words is a report, not a gate (`CLAUDE.md`). The workflow step "both READMEs
  move together" (`.github/workflows/hygiene.yml:151-162`) stays as that
  report.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The gate table is derived from `GROUPS` | Given `hooks/dispatch.py#GROUPS` at the branch tip. When the case reads the gate table of `README.md` *The gates* and of `README.ko.md` *게이트*. Then each script `GROUPS` names has exactly one row whose first cell is its file name without `.py`, and no row names anything else. | A case in `tests/behaviour/test_chain_hooks_hardening.py`. Seen red against the tree at `5287dd42`, which lacks `worktree_consent` and `root-migrate`, and red again with one row deleted from one edition. |
| S2 No count of gates or hooks, and no copy of the Where column, stands in the README prose | Given `README.md` *First run* and the `seal/` row of *Where the records live*, and the Korean sections. When a person reads them. Then they point at the gate table's Where column, and name no count of gates and no list of gate names. | `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py#test_both_readmes_list_the_stamp_hook` asserts that the removed count phrases and opt-in lists are absent from both editions. Seen red by restoring "Nine of the thirteen gates". |
| S3 The always-on block is described without counts | Given `README.md` *Why the always-on context is ...* and the CLAUDE.md block row, and their Korean editions. Then no line count, section count or rule count stands there, and the row names `templates/setup/claude-md-block.md` as the block's one source. | An absence pin of "12 always-on lines", "eight rules", "12줄" and "규칙 여덟" in both editions, in a module that already reads the READMEs. Seen red by restoring one. |
| S4 Which hooks reach the network is stated once, without a count | Given `README.md`'s privacy paragraph, `README.ko.md`'s, and `CONTRIBUTING.md` *House rules*. Then the READMEs name `lint-python` and `version-check`. `CONTRIBUTING.md` says every hook that reaches the network is named in the README's privacy section. None of the three says how many there are. | An absence pin of "Two hooks reach the network", "네트워크를 타는 훅은 둘" and "A third needs" over the three files. Seen red by restoring one. |
| S5 The skills row lists the on-demand skills, without counts | Given every `skills/*/SKILL.md` and every `agents/*.md` frontmatter. When the case reads the skills row of each README. Then the backticked names in the row's on-demand sentence are exactly the skills no agent preloads and nobody has to type, and the row holds no number word. | A case in `tests/behaviour/test_chain_hooks_hardening.py` that replaces `test_both_readmes_count_the_skills_that_are_actually_there` and `test_the_readme_group_counts_are_derived_too`. Seen red by adding a preloaded skill's name to the row, and by removing an on-demand one. |
| S6 The way back before the commit to shared has one home | Given `README.md` *Shared or local* and `README.ko.md` *shared 인가 local 인가*. Then each links to `skills/config/SKILL.md` *Before switching to shared, say what cannot be undone* and holds no `git reset -- :/seal`. The skill's section holds the way back, the staged-change reason and the pathspec reason, and cites `docs/one-root-by-lifetime.md` *Shared or local* for the rule. | `tests/behaviour/test_first_setup_asks_once.py#test_the_readme_gives_both_moves_under_first_run`, re-pointed to assert the link and the command's absence. `tests/text/test_the_settings_have_a_front_door.py#test_the_one_way_door_is_named_before_it_is_walked_through` stays green. Seen red by restoring the README sentence. |
| S7 Both pasted pairs are drained | Given `BASELINE` without the entries `("README.md", "skills/config/SKILL.md")` and `("docs/the-agent-set.md", "skills/implement/SKILL.md")`. When `tests/text/test_no_passage_is_pasted_into_a_second_file.py` runs. Then it passes, because neither pair shares a 15-word run. | The module's own case `test_no_pair_shares_more_than_it_was_measured_at`. Seen red by removing the two entries before the passages are rewritten. |
| S8 The shipped workflow states its token scope and cancels superseded runs | Given `templates/setup/hygiene.yml`. When `tests/text/test_ci_gives_the_checks_what_they_need.py` reads it beside `.github/workflows/`. Then it has `permissions:` with `contents: read`, a `concurrency` group keyed on the pull request, the two draft events and checkout depth 0. | The module's cases, with the template added to what they read. Seen red against the template at `5287dd42`, which has neither `permissions` nor `concurrency`. |
| S9 The shared steps are one source | Given the steps of `templates/setup/hygiene.yml` and of `.github/workflows/hygiene.yml`. When the case pairs them by `name:`. Then each step the template names exists in the repository's file under the same name, and the two `run:` bodies are equal once the template's `"$RUNNER_TEMP/agentic/` prefix is taken off. The repository's file carries a one-line pointer to the template above each shared step, and no other comment on it. | A case in `tests/text/test_ci_gives_the_checks_what_they_need.py`. Seen red by changing `--baseline` in one file only. |
| S10 The template's chain step does not restate the checker's refusals | Given `templates/setup/hygiene.yml`'s comment on the chain step. Then it says what the step guards in one sentence and names the plugin's `docs/the-review-record.md` *What the check reads at the pull request*. | An assertion in the S9 case that the comment names that section. Proofer reads the rest. |
| S11 Every edition pair is read | Given every tracked `X.ko.md` beside an `X.md`. When `tests/behaviour/test_both_editions_carry_the_same_folds.py` runs. Then each pair is compared, `README` and a `docs/experiments/` pair among them. | The module's walk case gains an assertion that `README` and `docs/experiments/README` are among the pairs it read. Seen red against `pairs()` as it stands, and red with a heading planted in `docs/experiments/README.ko.md`. |
| S12 The rule's owner names every pair | Given `CONTRIBUTING.md` *House rules*. Then the sentence says the outline case reads every document with a `.ko.md` edition, not top-level `docs/` alone. | `test_the_contribution_guide_owns_the_rule_and_names_this_check`, whose phrase "every document with a `.ko.md`\n  edition" the rewrite keeps, plus an absence pin of "every top-level". |
| S13 The plugin's description is derived | Given `.claude-plugin/plugin.json`. When the case reads `.claude-plugin/marketplace.json`. Then its top-level `description` and its plugin entry's `description` both equal `plugin.json`'s `description`. | A case in a module that already reads `.claude-plugin/`. Seen red by editing one copy. |

## Data & interfaces

No schema, endpoint or payload changes. What changes shape:

- `tests/behaviour/test_both_editions_carry_the_same_folds.py#pairs` returns
  repository-relative names, such as `README` and `docs/experiments/README`,
  instead of names under `docs/`, and `read` joins them under `ROOT`. The
  listing comes from `git ls-files` (`tests/conftest.py#git_listing`), so an
  untracked file is not a pair.
- `tests/behaviour/test_chain_hooks_hardening.py` loses `NUMBER_WORDS` and
  the `spellings` table inside `test_the_readme_group_counts_are_derived_too`.
  It gains a gate-table reader: the rows of the table whose header row opens
  `| Gate |` in `README.md` and `| 게이트 |` in `README.ko.md`, up to the first
  line that is not a table row. `GROUPS` is read by loading `hooks/dispatch.py`,
  as `tests/hooks/test_dispatch.py` already does.
- `templates/setup/hygiene.yml` gains two top-level keys, `concurrency` and
  `permissions`. `seal pr-checks install` copies the file with `v<version>`
  substituted and nothing else, so an installed copy carries both keys.

## Rule changes

- add
  file: docs/the-session-hooks.md
  section: Registration
  to: **Each script `GROUPS` registers has one row in the gate table of
    `README.md` and of `README.ko.md`, and the table holds no other row.**
    A row's first cell is the script's file name without `.py`. The table
    is what a person reads to learn what runs on their machine, and
    `GROUPS` is the one list of what does, so a case derives the table's
    rows from `GROUPS`, and no count of the gates stands in prose beside
    it.
    check: tests/behaviour/test_chain_hooks_hardening.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| "Nine of the thirteen gates wake only under a condition" and the list of gate names after it | `README.md` *First run*, `:417-420` | The gate table's Where column, which the paragraph now points at. `GROUPS` decides the rows (S1) |
| "게이트 열셋 중 아홉은 조건이 맞아야 깨어납니다" and the list of gate names after it | `README.ko.md` *처음 실행*, `:408-410` | The same, in the Korean table |
| "The other four carry their own conditions. worktree-guard, session-lease and stub-remove act in every git repo." | `README.md` *First run*, `:428-429` | The Where column. The sentence on why ruff configuration is the condition may stay, since the table does not give that reason |
| "나머지 넷은 각자의 조건이 있습니다. worktree-guard, session-lease, stub-remove 는 모든 git 레포에서 돕니다." | `README.ko.md` *처음 실행*, `:419-420` | The same |
| The list of hooks that read the opt-in, from "the routing edit gate" to "lint-python follows ruff" | `README.md` *Where the records live*, the `seal/` row, `:114` | The gate table's Where column |
| The same list, from "라우팅 편집 게이트" to "ruff 설정을 따른다" | `README.ko.md` *저장소에 남는 기억*, the `seal/` row, `:110` | The same |
| "12" in the heading "Why the always-on context is 12 lines", and "12줄" in "상시 컨텍스트가 12줄인 이유" | `README.md:25`, `README.ko.md:26` | `templates/setup/claude-md-block.md`, which is the block. The heading says the context is small without a number |
| "12 always-on lines, four section headings (`Tooling`, `Safety`, `Session cost`, `Git`) over eight rules: one on tooling, three on safety, one on session cost, three on git." | `README.md` *What ships*, the CLAUDE.md block row, `:45` | `templates/setup/claude-md-block.md`, which the row already names as the one source |
| "늘 로드되는 12줄 — 절 제목 넷(...)에 규칙 여덟이다. 툴링 하나, 안전 셋, 세션 비용 하나, git 셋." | `README.ko.md` *무엇이 들어 있나*, `:45` | The same |
| "Two hooks reach the network." | `README.md:223` | The paragraph names the two hooks without a count |
| "네트워크를 타는 훅은 둘입니다." and "둘 다" | `README.ko.md:216`, `:221` | The same |
| "Two hooks reach the network, and both are named in the README's privacy section" and "A third needs the same three limits the second carries" | `CONTRIBUTING.md` *House rules*, `:441-445` | The README's privacy paragraph names which hooks reach the network. `CONTRIBUTING.md` keeps the rule for a new one, citing `version-check`'s limits by name |
| "Fourteen, in three groups", "The one", "Nine more", "Four you invoke by name" | `README.md` *What ships*, the Skills row, `:43` | The skills on disk and their frontmatter, read by S5's case |
| "열네 개이고 세 묶음이다", "한 개는", "아홉 개는", "나머지 네 개는" | `README.ko.md` *무엇이 들어 있나*, the 스킬 row, `:43` | The same |
| `NUMBER_WORDS`, `SKILL_ROW`'s use for counting, `test_both_readmes_count_the_skills_that_are_actually_there`, `test_the_readme_group_counts_are_derived_too` | `tests/behaviour/test_chain_hooks_hardening.py:237-421` | S5's membership case. `SKILL_ROW` stays if that case reads the row through it. `test_every_shipped_skill_is_named_in_both_readmes` stays |
| The `count` and `opt_in` columns of the editions table, and the old counts in its `gone` list | `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py#test_both_readmes_list_the_stamp_hook`, `:368-414` | S2's absence pins. The gate-row and side-effect assertions stay |
| "Until that commit, `git reset -- :/seal` and then `seal mode local` walk the whole thing back ... has never looked outside that path." | `README.md` *Shared or local*, `:529-532` | `skills/config/SKILL.md` *Before switching to shared, say what cannot be undone*, which the README links to |
| "그 커밋 전까지는 `git reset -- :/seal` 뒤에 ... 본 적이 없어서입니다." | `README.ko.md` *shared 인가 local 인가*, `:521-525` | The same |
| The README assertion `` "`git reset -- :/seal`" in body `` | `tests/behaviour/test_first_setup_asks_once.py#test_the_readme_gives_both_moves_under_first_run`, `:526` | Re-pointed: the body names the skill section and holds no `git reset -- :/seal` |
| "The split it records is what `agents/framer.md` exists for: a `frame/design.md` written by whoever then builds against it stops being a contract and becomes an account of what got built, which leaves the review's first stage comparing the work with its own description of itself." | `skills/implement/SKILL.md` *3. The SDD file set*, `:355-359` | `docs/the-agent-set.md` *One contract every agent receives, and one definition each*, `:37-40`, which the paragraph links to |
| The entries `("README.md", "skills/config/SKILL.md"): 22` and `("docs/the-agent-set.md", "skills/implement/SKILL.md"): 20` | `tests/text/test_no_passage_is_pasted_into_a_second_file.py#BASELINE` | Both pairs are drained (S7). The module's docstring says the work that drains a pair lowers its entry on purpose |
| The comments above the steps "a declared review chain has the round record it claimed" and "the mode the row declares is the mode the folder is in" | `.github/workflows/hygiene.yml:132-158`, `:208-224` | `templates/setup/hygiene.yml`'s comments on the same steps, with one pointer line in their place. The history they tell is in git |
| The list of the chain checker's refusals in the comment above the chain step | `templates/setup/hygiene.yml:58-79` | The plugin's `docs/the-review-record.md` *What the check reads at the pull request*, which the comment names |
| `pairs()`'s restriction to top-level `docs/` | `tests/behaviour/test_both_editions_carry_the_same_folds.py:60-67` | Every tracked `X.ko.md` beside an `X.md` (S11) |
| "Under `docs/` the outline is checked" and "reads every top-level `docs/X.ko.md` beside a `docs/X.md`" | `CONTRIBUTING.md` *House rules*, `:433-436` | The same sentence, rewritten to name every pair (S12) |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-28 by framer, before the build.

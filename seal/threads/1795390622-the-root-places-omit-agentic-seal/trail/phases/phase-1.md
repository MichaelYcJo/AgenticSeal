# Phase 1: 1795390622-the-root-places-omit-agentic-seal

## What this phase found

**The frame holds against the tree at `828b0137a`.** The frame was read at
`73a43735c`, and the two commits after it touch only this work item's
`frame/` (executed, `git diff --stat 73a43735c 828b0137a`). Each coordinate
of `frame/design.md` *Scope* items 1 to 3 held the text the item describes
(read). `lib/optin.py#home_at` reads `<root>/seal/`, then
`<root>/agentic-seal/`, then `<git-common-dir>/seal/`, as G3 says (read).
`skills/implement/scripts/seal.py#no_root` prints the shared and the local
place and returns 1, as G7 says (read). Every file the plan row's Verified
by cell names exists.

**The new `RULES` row was red before the text moved.** Row
`24 where the records root is found` of
`tests/text/test_the_rules_have_one_owner.py` was run against the text at
`828b0137a` (executed, `bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k 24`).
`test_the_owner_states_the_rule` failed because the core named none of
`` `<repo>/seal/` ``, `` `$(git rev-parse --git-common-dir)/seal/` `` and
`` `lib/optin.py#home_at` ``. `test_every_link_names_the_owner` failed at
`skills/implement/orchestration.md`, the first carrier in the row that did
not cite the core.

**Each owner fact and each link was seen red with its own guard removed,
at `222b5b5b5`.** Every run below was `seal mutate`, and `git status --short`
printed nothing after each restore (executed).

- The core's four facts, one mutant each, with
  `-k "owner_states_the_rule and 24"`: `<repo>/seal/` made `seal/`,
  `agentic-seal/` made `agentic/`, the common-dir path replaced by words,
  and `#home_at` dropped. All four were red. That selection holds only the
  owner case, so each red is that case's.
- The five carriers that cite the core once, with
  `-k "every_link and 24"`: the contract, `skills/implement/SKILL.md`,
  `skills/implement/orchestration.md`, `skills/commit-pr-convention/SKILL.md`
  and `skills/config/SKILL.md`. Each mutant replaced the citation with "the
  core". Each was red, and each failure named its own carrier.
- `skills/implement/bootstrap.md` cites the core three times. Taking out one
  citation leaves two, so the link case stays green by design. One mutant
  replaced the span from the file's opening paragraph to *Ask only here*
  with the same span minus all three citations, and the case went red
  naming the bootstrap.
- `tests/text/test_the_agent_contract_holds_the_universal_rules.py#test_moving_a_sentence_to_another_section_is_caught`
  was rewritten (below). It went red when `missing_facts` read the whole
  file in place of each rule's body, the one guard it names.

**Departures from the frame, each with its grounds.**

- `skills/config/SKILL.md` *Where the file is*: the paragraph after the
  frame's coordinate (`:25-28` at `73a43735c`) said "No root at either
  place" and "one of those two places". The sentence above it now cites a
  paragraph naming three places, so "two" and "either" read against it as
  a count that is wrong. Both now say "any of those places" and "one of
  those places". Judged against contract rule 19 and `skills/writing-style/SKILL.md`
  *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*.
- The contract module's `FACTS` loses entry 11, as `frame/design.md` D1 row
  (a) says. `test_moving_a_sentence_to_another_section_is_caught` moved
  rule 11's body and read `FACTS[11]`, so it now moves rule 21 under the
  rule before it. The module docstring says two facts are pinned and names
  where the places went. Judged against `frame/design.md` *Scope* item 11,
  its last sentence.
- `tests/behaviour/test_first_setup_asks_once.py`: the three cases D1 row
  (a) names leave, and with them `SESSION_RULE` and `SKILL`, which no other
  case read. `test_the_orchestrators_half_sends_a_fresh_repository_to_the_bootstrap`
  keeps its bootstrap citation alone, as D1 says, and its docstring names
  where the places are held. The module docstring and its `No TARGET` line
  drop the contract and the implement skill, which it no longer reads.
- `tests/text/test_the_settings_have_a_front_door.py`'s module docstring
  dropped "the paths that resolve the root" with the case that held them.
- The citation is worded differently in each file. The first draft gave
  `docs/layout/the-record-layout.md` and the contract one run of 15 words,
  and gave the commit skill and the config skill another, and
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py` failed on
  both (executed). Judged against `frame/design.md` *Grounding* G19.
- `skills/implement/SKILL.md` kept the clause that no config key is read,
  as *Scope* item 3 keeps the mode sentences, and says the order decides a
  repository with a root at more than one place. `skills/implement/bootstrap.md`
  (`:79-82` at `73a43735c`) says a root in the tree and one under the git
  directory make a shared repository, in place of "a repository with
  both", because the sentence no longer names two places for "both" to
  count.
- The row's key is `24 where the records root is found`, the number after
  the highest the table uses.

**What the next phase needs.** Rule 11's sentence on `Record language`,
which phase 2 rewrites, now opens at `skills/agent-contract/SKILL.md:124`
("The prose in the records follows"). `templates/setup/config.md` keeps its
line offsets above `:180`: the paragraph opening "An absent language key is
a refusal" is at `:31`, and *Record language* at `:95`.
`skills/commit-pr-convention/SKILL.md` *Every way of not naming a language
lands on English* opens at `:77`.

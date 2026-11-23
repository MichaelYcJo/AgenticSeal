# Phase 2: 1795390622-the-root-places-omit-agentic-seal

## What this phase found

**The frame holds against the tree at `2f6f438b6`, except for D1 row (c).**
Each coordinate of `frame/design.md` *Scope* items 4 and 5 held the text the
item describes (read). Phase 1 moved some line offsets, and phase 1's record
named the new ones: rule 11's language sentence opens at
`skills/agent-contract/SKILL.md:124`, and *Every way of not naming a
language lands on English* at `skills/commit-pr-convention/SKILL.md:77`.
No shipped script reads a phase record's prose (G9, read again at
`2f6f438b6`), so the phase record follows `Record language`.

**D1 row (c)'s facts could not be seen red as the frame spells them.**
`test_the_owner_states_the_rule` reads the owner's whole file, and
`templates/setup/config.md` already held `no such key` (the `seal mode`
sentence, now `:209`) and `` `seal pr-body` `` in seven lines outside it
(executed, `grep -n`). Taking either out of the paragraph would have left
the case green, so the case would pin nothing of the paragraph (contract
rule 15). Row `26 what an absent language key is and does` therefore pins
four spellings that only the paragraph holds, each containing one of the
frame's facts or the ways it names: `no file, no such key, an empty value`,
`does not parse as one JSON object`, `` `seal pr-body` refuses with nothing
written `` and `commit or a record is written in English`. The last fact
leaves out the sentence's capital `A`, because the case matches case for
case. Judged against contract rule 15 and `frame/design.md` *Scope* item 11,
which asks each owner fact to be seen red with that fact taken out.

**Both new rows were red before the text moved.** Rows `25 what Record
language governs` and `26 what an absent language key is and does` of
`tests/text/test_the_rules_have_one_owner.py` were run against the text at
`2f6f438b6` (executed,
`bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k "owner_states_the_rule and (25 or 26)"`).
Both failed. Row 25 named `` `trail/phases/phase-N.md` `` as missing, and
row 26 named all four of its facts.

**Each owner fact was seen red with its own guard removed, at `7aa027aaf`.**
Every run below was `seal mutate` on `templates/setup/config.md`, and
`git status --short` printed nothing after each restore (executed). Each
selection held only `test_the_owner_states_the_rule` for its row, so each
red is that case's, and each failure named the fact its mutant removed
(read).

- Row 25: `trail/phases/phase-N.md` taken out of *Record language*. Red.
- Row 26, one mutant at a time: `no such key` dropped, `no file` dropped,
  `an empty value` dropped, `as one` dropped from `does not parse as one
  JSON object`, `with nothing written` dropped after `` `seal pr-body`
  refuses ``, and `or a record` dropped. All six were red.

**The six citations of the paragraph are held by the citation case.**
Rows (b) and (c) carry no link, as D1 says. One `seal mutate` rewrote the
paragraph's bold lead, and
`test_a_cited_section_stands_in_its_file.py::test_every_cited_section_stands_in_its_file`
went red naming six dangling citations (executed):
`skills/agent-contract/SKILL.md:126`, `skills/code-review/SKILL.md:173`,
`skills/implement/SKILL.md:46`, `skills/config/SKILL.md:54`,
`skills/commit-pr-convention/SKILL.md:77` and
`skills/implement/routing-question.md:142`.

**Departures from the frame, each with its grounds.**

- The paragraph says what `seal pr-body` does in each of the four ways. It
  names the key where the key is absent or empty, and it prints the refusal
  of the paragraph after it where the file or the key will not read.
  `skills/code-review/scripts/pr_body.py#first_part` takes the second branch
  when `lib/config.py#declared_value` returns a refusal (read). *Scope* item
  5 says only "names the key and refuses with nothing written", which is
  wrong for the fourth way. Judged against contract rule 19, which has the
  owner state the fact as the code does.
- `templates/setup/config.md` *Commit and pull request language* and
  *Record language* drop the clauses on what `seal pr-body` and a commit do,
  and keep who asks. The first cites the paragraph by its opening words,
  because it stands in the same file. The second cites nothing, because the
  paragraph is the file's preamble, read before either section. Judged
  against `frame/design.md` *Scope* item 5, whose first bullet keeps the
  sentences on who asks.
- `skills/config/SKILL.md`: the two Default cells read "none, as the
  paragraph below the table says", and that paragraph holds the citation
  once. A citation in each cell would repeat a 17-word section name twice
  in one table. Judged against `skills/writing-style/SKILL.md`
  *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*, its first rule.
- Contract rule 11's last sentence now names `templates/setup/config.md`
  *What no key governs*, as *Scope* item 4 asks. The rule's short list of
  what stays English (`Target SHA`, the verdict words, the `<!-- -->`
  markers, code) stays, because an agent acts on it without opening the
  template.
- `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`:
  the comment above `UNNAMED` said "the skill's sentence says four". It now
  says the sentence is the paragraph of `templates/setup/config.md`. The
  case's five shapes do not change. Judged against contract rule 19.
- `ROW_READERS` in the same module stays as it is. Each of its six files
  still names `Record language` at HEAD (executed, the module's case is in
  the run below), and the case pins the key's name, which this work does
  not move, not a copy of the record list.

**The statements left standing, and why.** Each states part of what an
absent key does, beside the reason it is there. The list was made in round
2's fix pass, after phase 2 had listed one sentence by a search on a few
wordings and two rounds found more. Its method: every line of `skills`,
`agents`, `templates`, `docs`, `README.md`, `README.ko.md` and
`CONTRIBUTING.md` that names a language key (`language key`, either key's
name, `either key`, `both keys`, `the two keys`, and `언어 키` in the Korean
files), that says `seal pr-body` refuses, or that names English as what a
missing key leaves, with the paragraph around each read whole for whether
it says what an absent key does.

- `docs/forms/the-guarantee.md:22`: "`seal pr-body` refuses where either
  language key is absent, so a body is composed only for a repository that
  declared its languages." It is a policy document's reason for the
  sealer's reading, outside the list *Scope* item 5 names.
- `docs/layout/one-root-by-lifetime.md:232-237` and the Korean pair at
  `:221-226`: the policy paragraph on why the keys are required, which
  `frame/design.md` *Scope* names out of scope.
- `docs/checks/the-pull-request-check.md:186-187` and the `seal pr-body`
  row of `docs/running/what-a-script-gates.md:66`: each says what one check
  or script refuses, which is that document's subject.
- `skills/commit-pr-convention/SKILL.md:82-83`, the lead **Both keys are
  required all the same, and a commit is never refused for them.**, which
  *Scope* keeps with the sentences on who asks.

Two lines the search printed state something else and stay:
`skills/implement/bootstrap.md:123` says every command that reads the
config refuses a file that does not parse, which is the template's next
paragraph, not this one; `skills/code-review/orchestration.md:420-421`
gives the orchestrator's act on a `refused:` line naming a missing key.

Phase 2 also left five restatements that the review rounds removed, each
now a citation of the template's paragraph or a sentence that keeps only
its own reason or act. `skills/commit-pr-convention/SKILL.md:87-89` stood
at `:90-92` of `73a43735c`, outside the out-of-scope coordinate `:85-89`
that phase 2 read against the file's new numbering; round 1 finding 3
named it. Round 2 finding 1 named `skills/implement/bootstrap.md:139-141`,
and the list above found three more:
`skills/implement/routing-question.md:157-158`, and
`skills/commit-pr-convention/SKILL.md:117-119` and `:317-319`, the last a
sentence of the file's checklist.

**The phase boundary passed.** One command, the plan row's modules, each
test file this phase changed, each test file that names a changed path
(`git grep -l` over `tests/`), and the tree-wide `tests/text` and
`tests/behaviour` (`CONTRIBUTING.md` *What a contribution is asked for*):
`bin/test tests/text tests/behaviour tests/lib/test_config.py tests/lib/test_core.py tests/lib/test_gaps.py tests/skills/test_broad_gate.py tests/skills/test_chain_check.py tests/skills/test_fold_check.py tests/skills/test_passages.py tests/skills/test_pr_body.py tests/evals/test_noninferiority.py -q`
gave 2079 passed and 10 skipped (executed, at `7aa027aaf`). S4's search
`git grep -n -F 'no such key' -- skills agents templates docs ':!*.py'`
printed `templates/setup/config.md:32`, the paragraph, and `:209`, the
`seal mode` sentence, which is what S4 names (executed).

**What the next phase needs.** Phase 3 edits two files this phase
changed. In `skills/implement/SKILL.md` it edits the `frame/design.md` and
`trail/phases/phase-N.md` rows of *3. The SDD file set* and the paragraph
after them, and this phase shortened the file by three lines above them.
In `tests/text/test_the_rules_have_one_owner.py` it adds to row 16 and adds
rows (d) to (g). This phase took the keys `25` and `26`, so the next key
free is `27`.

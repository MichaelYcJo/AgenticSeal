# Phase 3: 1795390622-the-root-places-omit-agentic-seal

## What this phase found

**The frame holds against the tree at `844f81462`, with two gaps in
*Grounding*.** No file *Scope* items 6 to 10 edit changed after `73a43735c`
except `skills/implement/SKILL.md`, which phase 2 shortened by three lines
(executed, `git diff --stat 73a43735c 844f81462`). Each coordinate of those
items held the text the item describes, at that offset or three lines up
(read). The two gaps:

- G18 does not name
  `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py#test_the_unmeasured_word_says_so_and_every_reader_is_told_it`.
  Its `readers` table held `skills/code-review/orchestration.md` to
  `` `new?` `` and `skills/verify/orchestration.md` to `**New?**`, so it
  pinned the copy *Scope* item 8 removes and the label item 8 replaces. The
  case went red at the first build of item 8 (executed). G18's probe matched
  strings of 16 characters or more, and these are shorter.
- G14 says `tests/github/test_release_seal.py:382` pins *The broad gate*'s
  sentence on a line that did not parse. That line is an entry of the
  case's `REASONS` table, which pins a reason the release workflow prints,
  not a sentence of `skills/verify/orchestration.md` (read). Nothing this
  phase changed depends on it, and the module passed in the run below.

**The new rows were red before the text moved.** With the rows in
`tests/text/test_the_rules_have_one_owner.py` and `DESCRIBES_THE_BASE`
re-pointed, and no document edited (executed,
`bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py -q -p no:xdist -k "16 or 27 or 28 or 29 or describes or reading_as_the_ref"`):
rows 27, 28 and 29 of `test_the_owner_states_the_rule` failed, row 28 of
`test_every_link_names_the_owner` failed, and
`test_no_document_leaves_the_base_reading_as_the_ref_you_typed` failed
naming `docs/running/the-broad-gate.md`. Row 16's owner case passed,
because `docs/running/the-run.md` already spelt the `Reframed` line; its red
is the mutant below.

**Each owner fact, each link and each re-pointed case was seen red with its
own guard removed, at `30a0b05ef`.** Every run was `seal mutate`, and
`git status --short` printed nothing after the last restore (executed).
Each selection held one case for one row, and each failure line named the
fact or carrier its mutant removed (read, in the outputs kept under the
phase's scratch directory).

- Row 16: the `Reframed` line's spelling replaced by "the `Reframed` line"
  in `docs/running/the-run.md`. Red.
- Row 27, one mutant each in `skills/verify/orchestration.md`: each bullet's
  lead put back to **Failing on base too**, **New** and **New?**. All three
  red, each naming its word.
- Row 28's owner: `` `<base>@{upstream}`, `` and `` `origin/<base>`, `` each
  dropped from `docs/running/the-broad-gate.md`. Both red.
- Row 28's links: the citation replaced by "the policy" in
  `skills/verify/orchestration.md`, then in
  `skills/code-review/orchestration.md`. Both red, each naming its carrier.
  Each file holds the citation once (executed, a count over the flattened
  text).
- Row 29: `` `## Removes` `` and `` `skills/settle/rule-changes.md` *Rule
  changes* `` each dropped from `docs/running/the-agent-set.md`. Both red.
- `DESCRIBES_THE_BASE`: `` `origin/<base>`, `` dropped from the policy, with
  `-k reading_as_the_ref`. Red, naming the policy document.
- The sealer case's rewritten `readers` table: the verify bullet's lead put
  back to **New?**, with `-k unmeasured_word`. Red, naming
  `skills/verify/orchestration.md`.

**Departures from the frame, each with its grounds.**

- The sealer case above loses its `skills/code-review/orchestration.md`
  entry, and reads `skills/verify/orchestration.md` by its new bold lead
  `` **`new?`** ``. Its comment and docstring say why. Row 27 holds the
  word in its owner, and the citation from the code-review file is held by
  `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, so no link
  is added. Judged against `frame/design.md` *Scope* item 11, its last
  sentence and D1 row (e)'s "none".
- `test_the_crafters_gate_rule_names_the_failure_words_and_rule_2` keeps its
  assertions, which the crafter's new paragraph still meets. Its docstring
  and failure message said the paragraph tells what the words mean, and now
  say it gives the crafter's act at each word. Judged against contract
  rule 19.
- The crafter's paragraph cites no section for what a word means. *Scope*
  item 8 asks for the crafter's act and says the paragraph "does not say
  what a word means"; the owner is the orchestrator's half of the verify
  skill, which a crafter has no step to open. Judged against
  `skills/core/SKILL.md` *The first value: efficient development through
  the AgenticSeal process*, its paragraph on a party opening only what its
  step needs.
- In `skills/code-review/orchestration.md`, the second restatement's clause
  "with the counts and signals you weighed as its grounds and the document
  you judged against" leaves with the sentence it stood in. *The run* has
  the row name the counts weighed and that section, and the skill's table
  of signals, which the orchestrator weighs, stays. Judged against
  `frame/design.md` *Scope* item 6, which names the paragraph's first two
  sentences a restatement.
- `skills/verify/orchestration.md` *Which base, and it is the one the merge
  is judged by.* drops the sentence on a plain branch name being a local
  ref, as well as the order. The policy paragraph's first two sentences give
  that reason, and the skill now cites the section "with its reason".
  Judged against *Scope* item 9, which has the paragraph cite the section
  for the order and the reason.
- `docs/running/the-broad-gate.md` keeps its words for each step and puts
  the ref beside each, so the person doubting a seal reads both the step
  and its spelling. Judged against *Scope* item 9.
- The comment of `RULES` row 29 names "a document of `docs/forms/`" rather
  than the deleted file's path, so the search of `frame/design.md` *User
  scenarios* S8 prints nothing, as S8 asks.
- The new rows take the keys `27`, `28` and `29`, after phase 2's `26`.

**The searches and the rules check.** S5's search
`git grep -n -e 'Reframed <date>' -e 'Reframed …' -- ':!seal/threads'`
printed four lines: `docs/running/the-run.md:19`,
`skills/code-review/scripts/chain_check.py:1099`,
`tests/skills/test_chain_check.py:1423` and
`tests/text/test_the_rules_have_one_owner.py:145`, the four S5 names. S8's
search `git grep -n 'reader-registry' -- ':!seal/threads'` printed nothing
and exited 1. `bin/seal rules --check` printed "all 175 check lines in 67
rule files hold" and exited 0. All three executed at the build's tree.

**The other statements of each rule this phase moved, a sample.** Each was
listed by `git grep` on the rule's words over `skills`, `agents`, `docs`,
`templates`, `CONTRIBUTING.md` and `README.md`, every hit read (executed):
`three finding rounds`, `no cap` and `does not count` for the run's end;
`origin/<base>`, `@{upstream}` and `base's upstream` for the base order;
`` `new?` `` and `failing on base too` for the gate's words; `## Removes` and
`docs/forms/` for what a frame removes. Each hit is the owner, a citation of
it, or one of these, which stand:

- `skills/code-review/orchestration.md:478-481` names the refs a sealer's
  clone resolves the base to. That is the sealer's own resolution, which
  *Scope* leaves out of scope with `agents/sealer.md:42-48`, which is in the
  same list.
- `docs/running/what-a-script-gates.md:57` names the three words in its row
  for `seal gate` and says only that they are reported. It states no
  meaning, so nothing in it can drift from the owner.
- `skills/code-review/orchestration.md:185` says a round whose `should`
  finding is closed `rejected` does not count. It is in the paragraph *Scope*
  item 6 keeps, the orchestrator's account of when the run ends.
- `agents/framer.md:35`, `:120`, `:178` and `:240-241` and
  `agents/sealer.md:85` name `## Removes` as the section each party writes
  or reads, and none states the rule.

A rule stated in other words is outside what these searches reach, and the
proofer's to read for (contract rule 12).

**The phase boundary passed.** One command, with the plan row's modules,
each test file this phase changed, each test file outside `tests/text` and
`tests/behaviour` that names a changed file, and those two tree-wide
directories (`CONTRIBUTING.md` *What a contribution is asked for*):
`bin/test tests/text tests/behaviour tests/github/test_release_seal.py tests/github/test_publish_release_note.py tests/github/test_plugin_directory_check.py tests/github/test_release_report.py tests/github/test_rules.py tests/github/test_run_tests.py tests/lib/test_gaps.py tests/lib/test_launch.py tests/skills/test_chain_check.py tests/skills/test_fold_check.py tests/skills/test_mutation_check.py tests/skills/test_passages.py tests/skills/test_payload_meter.py tests/skills/test_session_cost.py tests/test_conftest.py tests/test_censuses.py -q`
gave 2426 passed and 9 skipped, exit 0 (executed, at `30a0b05ef`).

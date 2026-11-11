# Phase 2: 1794383427-asserts-pin-literal-phrases

## What this phase found

**The frame holds against the tree at `b39e4316e`, except where two of its
sentences disagree about one assert.** *The listing* of `frame/design.md`
gives 183 asserts, 37 absence asserts and 84 cases over the six modules of
group B at `18a7e18fb`, the counts of design *The groups* (executed). The
base `b39e4316e` gives the same per-module counts. The one change since
`18a7e18fb` is phase 1's comment in `tests/behaviour/test_waiver_decided_at_start.py`,
so every waiver line after 411 stands one line higher at the base
(executed, `git diff --stat 18a7e18fb HEAD`). The line numbers below are
the base's. Each file the phase row names exists (read).

The two sentences are these. Design *Scope* item 1 and `frame/plan.md` A7
say an assert that already carries #1233's comment stays as it stands.
Design *The criterion*, in its paragraph on a kept literal, names
`tests/behaviour/test_first_setup_asks_once.py:415` as cut to the command
in its code span. That assert carries #1233's comment ("the code span is
the fact"), written in `c3e020961` (executed, `git log -L`). The phase cut
`:415`, because the design names it, and left every other assert that
carries #1233's comment as it stands. Some of those also hold words around
the code span the comment names. They are
`tests/behaviour/test_the_sealer_guarantees.py:179` and `:253`, and
`tests/behaviour/test_first_setup_asks_once.py:94`, `:100`, `:240` and
`:398`. Which sentence rules is the framer's to fold.

**S1, per module of group B.** The unit is one assert, a distinct
`path:line`, as in phase 1. The base is `18a7e18fb`. The 183 add up as 96
kept, 74 removed and 13 not ruled (executed: the ledger summed against
*The listing* per module). The last column is *The listing* at
`2d076f545`. It equals the kept count plus the not-ruled count in every
module.

| Module of `tests/behaviour/` | Listed | Kept | Removed | Not ruled | Listed at `2d076f545` |
|---|---|---|---|---|---|
| `test_first_setup_asks_once.py` | 55 | 38 | 17 | 0 | 38 |
| `test_the_broad_gate_row_is_asked_for_and_runs_as_written.py` | 46 | 3 | 33 | 10 | 13 |
| `test_waiver_decided_at_start.py` | 24 | 22 | 2 | 0 | 22 |
| `test_the_pull_request_language_is_the_repositorys.py` | 27 | 13 | 11 | 3 | 16 |
| `test_the_set_a_work_item_always_has.py` | 15 | 6 | 9 | 0 | 6 |
| `test_the_sealer_guarantees.py` | 16 | 14 | 2 | 0 | 14 |
| Total | 183 | 96 | 74 | 13 | 109 |

Of the 37 absence asserts, 33 were removed and 4 were not ruled. Each
removed one held text or a design that a shipped release removed. Examples
are `judges nothing` in `agents/sealer.md`, `| 6+ files` and the
`tasks/` directory, `mixed — see below`, the README's
`git reset -- :/seal`, `refs/pull/` and `unverified_check.py` in the
workflow template, `[no-review]`, the retired `` `config.md` ``, and
`the-round-record.md` in the exclusion list.

The 13 not ruled read a program's output or a text the case built. In the
broad gate module they read the refusal that `broad_gate.py#missing_row`
returns. In the pull request language module they read the set the case
built from `LANGUAGE_CODES`, and the refusal `lib/config.py#declared_value`
returns (read).

**Asserts outside the listing were ruled as well**, as design *Scope*
item 1 asks of each case that holds a listed assert. They are not in the
counts above.

- The file-count sweep of `test_the_set_a_work_item_always_has.py` went,
  with `KNOWN_PROSE` and the `re` import. It raised where one of five
  documents names a count of files. That is the absence of the ladder's
  file-count rung, which a shipped release removed. A count of files in
  prose is no command, path or spelling a reader acts on.
- In the sealer's step 2 case, four phrases of the `pinned` list went:
  two from step 2, one from step 4 and one from *Never*. The step 4 and
  *Never* slices went with them. "On any exit but 0" was cut to
  `exit 0`, the exit code the sealer waits on.
- In `test_first_setup_asks_once.py`, the order of the three option labels
  is kept with a comment. `boot.count("AskUserQuestion") == 1` went with
  the case that held it, and so did `BROAD_ROW`, the lead of the
  `Broad gate` question. Cut to the key's name, that literal stands in
  eight places of the bootstrap. `text.count(SESSION_RULE) == 1` became a
  presence assert, since "once" is a property of the wording.
  `LEFT_BEHIND` was cut from two sentences per edition to the citation in
  each.
- In the broad gate module, `REFUSED_AND_ALLOWED` and `CRITERION` are kept
  as headings that a citation resolves. The `count(THREE_RULES[2]) == 1`
  of the fold case went with that case.
- In the pull request language module, the old first line's `!=` assert
  went with its case. The `copied` assert of the exclusion list is kept,
  under *Absence asserts kept* below.

**Six kinds of decision recur, each judged against `frame/design.md` *The
criterion*.**

- A literal that is a fact is kept, with a comment directly above it that
  names the fact and its reader. Examples are a path, a command, a config
  key, a workflow step's script and flag, the tag placeholder
  `skills/implement/scripts/seal.py#PLACEHOLDER` fills, a heading a
  citation resolves, the trailer `chain_check.py#TRAILER` reads, and the
  harness tool `AskUserQuestion`. A literal that held sentence words was
  cut to the fact. Examples are `:415` above, `` `Mode` and `Broad gate` ``
  in `templates/setup/config.md`, `` `<repo>/seal/` `` for the session rule,
  and the two README citations.
- A literal that is a sentence or a word of a sentence is removed.
  Examples are "Nothing is stripped", "lands on English", "four questions",
  "either place", "default", "prefix" and "not translated", "response
  language", "Committed", and the three rules' reasons.
- An assert that only locates the text a removed assert read is removed.
  Examples are `follow-up.md         schedulable items` in the layout trees
  and the `## Pull request bodies` split.
- A case left with no assert is removed, together with the helpers only it
  used (design *Scope* item 6). Eighteen cases went. In the broad gate
  module seven went: the criterion's two halves, both `&` cells, the pipe
  row, the module header, the paragraph above the lists, the rules'
  reasons, and the fold of rule three. In the pull request language module
  five went: the default's placement, the body section's first line, the
  prefix, ASCII branch names, and the response language. In
  `test_the_set_a_work_item_always_has.py` four went: the top rung, the
  task-list directory, the layout trees, and the permanent home. In
  `test_first_setup_asks_once.py` two went: the broad command riding the
  one call, and the "nowhere else" sentence. The helpers that went are
  `both_halves`, `broad_gate_section`, `BROAD_ROW`, `GATE_SCRIPT`,
  `INSTRUCTING`, `KNOWN_PROSE`, `module_header` and `refusal_paragraph`. No
  module was left with no case, and no module was deleted.
- A case whose name stated what a removed assert read is renamed for what
  it still reads. Eight were renamed:
  `test_the_template_carries_the_heading_of_the_two_lists`,
  `test_the_template_names_the_command_that_rewrites_a_refused_key`,
  `test_the_routing_question_names_the_trailer_that_records_no_work_item`,
  `test_the_review_skill_names_the_round_template`,
  `test_the_three_options_are_named_in_order`,
  `test_the_root_is_spelled_through_the_common_dir`,
  `test_the_session_rule_names_both_places` and
  `test_the_seal_readme_names_the_command_that_finds_the_local_root`.
- A docstring that stated what a removed assert pinned was rewritten in
  place (design *Scope* item 7). Examples are the module docstring of
  `test_the_set_a_work_item_always_has.py`, the docstring of `candidates()`,
  which named `BROAD_ROW`, and the docstrings of the cases above that kept
  a fact and lost a sentence.

**Absence asserts kept.** Three absence asserts stand outside the `not in`
form, and each cites a rule in force in its comment. *The listing* reads
the first two as presence asserts.

- `` no `AskUserQuestion` `` per line of each agent definition, which refuses
  any other line naming the tool. The rule is `agents/framer.md` *Never*,
  and the other definitions' *Never*: an agent asks no person.
- No `framer` or `Planning` box in the routing question's box tables. The
  rule is `skills/implement/orchestration.md` *What the answer writes*,
  under the bold lead **The declaration has one more row, and nobody is
  asked about it.**
- No key of `lib/fields.py` copied into the exclusion list of
  `templates/setup/config.md`. The rule is `skills/core/SKILL.md` *The rule
  a mechanism is kept against*: a fact has one source.

**These literals could be read either way, and the proofer reads each
against *The criterion* (S2).**

- `/bin/sh` and `cmd.exe` in the two `&` cells were removed with their
  case. Each stands inside a reason or cost cell, and the case's own
  docstring says it pins which shell the cell credits with a behaviour.
  That is meaning.
- "ASCII" in the skill and the template was removed as a word of a rule.
- `| Refused |` and `| Stays legal |` were removed. No script reads them.
  The two pairing cases, which hold no listed assert, still find each table
  by its header through `table()`.
- The header row of the plan template's *Overlap with the release* table
  was kept. No script reads it, but the orchestrator reads `Merges first`
  by its column. The *Phases* header is kept because
  `evals/scripts/rule_cases.py` matches it.
- `|---|---|---|---|` in the plan template was removed. It stands under
  each four-column table of the file, so it held nothing the Phases
  header's assert does not.
- `framer` in the file-set table's `Written by` cells was kept as the agent
  the orchestrator spawns. `builder` in the same column was removed as a
  word, since no agent and no file has that name.
- `exit 0` was cut from "On any exit but 0". It stands in step 2's "On
  exit 0" sentence, so the assert holds the exit code the sealer waits
  on.
- `` `.git/seal/` `` absent from the skill and the bootstrap was removed.
  `docs/layout/one-root-by-lifetime.md:124` itself names `.git/seal/` as
  where the local root lives, so no rule in force forbids the literal.
- The bootstrap's count of `AskUserQuestion` was removed. A sentence that
  names the tool a second time, for any reason, turns it red.
- `BROAD_ROW` was removed with its case, for the reason under *Asserts
  outside the listing*.
- `"run end to end"` and `"at most four options per question"` in the
  waiver module carry #1233's comment. They stay as they stand.

**No check line changed and none lost its last reader (design *Scope*
items 8 and 9).** The check lines naming a module of group B all stand
under `docs/` (executed, `git grep`). Each was read against the cases that
stand after the ruling, and each keeps a case that reads its rule (read).
They are `docs/forms/the-guarantee.md:20`, `:23` and `:26`,
`docs/layout/one-root-by-lifetime.md:113`, `:184`, `:238` and `:258`, the
same four lines of the Korean edition, `docs/running/the-agent-set.md:112`
and `docs/running/the-review-and-parity-arms.md:112`. No check line under
`RULE_FILES` outside `docs/` names a module of group B.

**What was run, and what each run showed.**

- S1: executed, as above. The ledger and both listings are in the phase's
  scratch directory.
- S4: `bin/seal rules --check` exits 0, "all 178 check lines in 69 rule
  files hold." (executed at `2d076f545`).
- S5: `git grep -n -w <name> -- . ':!seal/threads' ':!.test_durations'`
  over each removed case, each removed helper and each old case name lists
  nothing at `2d076f545` (executed). The first run, over the working tree
  before `a5b1675da`, found `BROAD_ROW` in the docstring of
  `candidates()`, which was rewritten before that commit. The same search
  finds the new name `test_the_review_skill_names_the_round_template` at
  its definition, so it can find a name that is present (executed).
- S9: the six edited modules gave 184 passed at `a5b1675da` (executed). The
  boundary set, `bin/test tests/text tests/behaviour
  tests/github/test_rules.py tests/lib/test_config.py -q`, gave 1984 passed
  and 8 skipped at `2d076f545` with this record, `gaps.md` and the Status
  cell in the tree (executed). `tests/text/` and `tests/behaviour/` are the
  tree-wide files and hold every module that reads an edited one.
  `tests/lib/test_config.py` names the pull request language module in its
  docstring.
- Mutation: `seal mutate` ran over four kept literals, each in the document
  it pins and each with its case. All four went red, each on the assert
  that names the literal (executed, failing line read). The literals were
  `` `Mode` and `Broad gate` `` in `templates/setup/config.md`, `On exit 0`
  in `agents/sealer.md`, `` no `AskUserQuestion` `` in `agents/framer.md`, and
  a box of `skills/implement/routing-question.md` relabelled `Planning`. A
  fifth run, over the README's `*Shared or local*` citation in the sentence
  on a workflow left behind, SURVIVED. The same citation stands twice more
  in that subsection, so the cut assert holds on either of them. That is
  the third failure scenario of `frame/plan.md` *Technical context*,
  measured here. The tree was clean after each restore (executed, `git
  status --short`).
- S2 and S3 are the proofer's at review.

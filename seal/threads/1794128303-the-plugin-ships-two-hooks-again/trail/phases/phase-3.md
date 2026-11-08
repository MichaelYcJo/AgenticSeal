# Phase 3: 1794128303-the-plugin-ships-two-hooks-again

## What this phase found

**The frame holds for this phase, with one coordinate already spent and
five statements of the entry it does not name.** Each was judged against
`frame/design.md` *Scope* item 3 and `## Removes`, and against the tree at
`a6eb207a`, with every target found by its text:

- *Scope* item 3 says `bootstrap.md:161` loses the entry's name with its
  question. Phase 2 already removed that text: the paragraph opening **The
  third question is the stamp** named `skills/start/SKILL.md` step 2, and
  it went whole (`git diff ce083d00f a6eb207a5 -- skills/implement/bootstrap.md`).
  This phase made no edit to `bootstrap.md`.
- `CONTRIBUTING.md` *Proposing a new gate or skill* said the core is loaded
  by "every session the entry skill `start` starts". It now says every
  session in a repository with a `seal/` root.
- `docs/layout/one-root-by-lifetime.md` *Shared or local*, and its Korean
  edition at the same place, said a collaborator without the plugin runs
  nothing "because the entry skill and the `seal` commands are the
  plugin's". Both now name the hooks, the skills and the `seal` commands.
- `tests/behaviour/test_waiver_decided_at_start.py#test_question_1_is_put_every_time_with_the_ladders_answer_marked`
  read `skills/start/SKILL.md` and would fail once that file went. Its two
  assertions on the entry and the docstring sentence about them are
  removed. The case keeps its four phrases of `skills/implement/orchestration.md`,
  which hold the rule.
- `skills/commit-pr-convention/SKILL.md`'s example trailer block had the
  title "feat: the entry writes the declaration before the first edit".
  `git log --all --grep` finds no commit with that subject, so it is an
  example and not a quote of history. It now names the orchestrator.
- `README.md` *Your first work item*, and the Korean edition, still said
  that first setup asks whether to draw the sealer's stamp. Phase 2 removed
  that question, and *Scope* item 2 did not name the sentence. *Scope* item
  3 rewrites the section, so the sentence went in both editions here.

**One paragraph of `skills/implement/orchestration.md` merged into the
paragraph above it instead of being rewritten.** *Scope* item 3 asks that
the paragraph opening **`/agentic:start` writes the declaration before the
first edit** say that the orchestrator writes and commits `routing.md`
before any other edit. The paragraph above it, opening **The orchestrator
writes the answer down before the first edit**, already says that. A second
statement of the same fact is what `skills/core/SKILL.md` *The rule a
mechanism is kept against* refuses ("A fact has one source"). So the
paragraph's first sentence went, and its one other sentence, on `no work
item`, now closes the paragraph above it. The paragraph opening **The first
edit waits for the routing answer** is rewritten as the frame says, and
names step 1.

**The cases as built.** `test_a_plain_request_to_change_code_is_the_entrys`
is now `tests/behaviour/test_chain_hooks_hardening.py#test_a_plain_request_to_change_code_is_implements`.
It holds that `skills/start/` is absent, that `implement`'s description
carries no `disable-model-invocation`, claims "implementing a feature,
starting a ticket", and names neither "a plain request to change code" nor
`` `start` ``. That description is byte for byte the first fourteen lines of
`1ae24b1e0^:skills/implement/SKILL.md` (executed: `diff` printed nothing).
`#test_the_review_skill_opens_the_core_once_where_it_orchestrates` pins the
review skill's new sentence. A third case is new:
`#test_the_orchestrator_holds_the_core_once_before_the_first_edit` pins step
1's sentence on the hook and the fallback open. The frame names no case
for it, but step 1 is the one place an orchestrating session reads where
the core comes from now that the entry is gone (contract rule 14). The
pinned sentence of `tests/behaviour/test_the_old_block_leaves_through_update.py#test_step_4_works_on_the_config_directorys_file_and_writes_no_block`
reads "from the plugin's `SessionStart` hook". The comment *Scope* item 3
places at `tests/behaviour/test_first_setup_asks_once.py:702` stood at
`:665`.

**Seen red, each before or by its one guard removed:**

- `test_a_plain_request_to_change_code_is_implements`, written before any
  other edit of this phase: red at its first assertion, since
  `skills/start/` stood. Over `fde58d65`, `seal mutate skills/implement/SKILL.md`
  ran two mutants, each alone. The first put back the parent's clause,
  "a plain request to change code that no work item has started yet, which
  `start` takes first", and the case went red at
  `assert "a plain request to change code" not in head`. That mutant is the
  description at the phase's parent once whitespace is folded, as the case
  reads it. The second put in "a request `start` takes first" alone, and the
  case went red at `assert "`start`" not in head`.
- `test_the_review_skill_opens_the_core_once_where_it_orchestrates` and
  `test_the_orchestrator_holds_the_core_once_before_the_first_edit`, written
  before the edits: both red at their sentence assertion against the tree at
  `a6eb207a`. Over `fde58d65`, `seal mutate` dropped "opening
  `AgenticSeal core from`" from each file's sentence, and each went red at
  the same assertion. A second mutant of each put an older opening back,
  "first opens the core once, as `skills/start/SKILL.md` says" in the
  review skill and "has read the core once" in step 1, and each went red
  too.
- The update step 4 pin: `seal mutate skills/update/SKILL.md` put back
  "`/agentic:start` opens it", and the case went red with
  `update step 4 does not say "from the plugin's `SessionStart` hook"`.

Every mutant left its file as `seal mutate` read it, and `git status` was
clean after each run. The other edits of this phase are prose, docstrings
and comments, and the removed file. They add no behaviour, so they owe no
mutation run.

**What the greps list at `270d3aed`.** `git grep -n "agentic:start\|skills/start" -- . ':!seal/threads'`
lists the preset block's marker `<!-- agentic:start -->` alone, in
`README.md`, `README.ko.md`, `skills/update/SKILL.md`,
`templates/setup/claude-md-block.md`, `tests/behaviour/test_release_hygiene.py`
and `tests/behaviour/test_the_old_block_leaves_through_update.py`.
`git ls-files skills/start/` prints nothing. The wider grep *Scope* item 3
names, with `the entry skill` and `entry's`, lists the entry skill only in
this phase's three hardening cases, which name it as gone. Every other hit
is an entry of another kind: a release note's fragment, a seal in
`assets/seals/README.md`, an eval's target or case, a pact's refusal and a
payload ratio. The launcher grep of the scenario *No shipped file
names the launcher* lists the same four kinds of line phase 2's record
names. `.test_durations` still names the removed case id; `frame/plan.md`
*Constraints* leaves that file to CI.

**The phase's scoped run.** One command, `bin/test` over the plan row's
modules, the whole of `tests/behaviour/` and `tests/text/`, and the 35
other test modules that name a path this phase changed or read
`git ls-files`, `os.walk` or `glob(` over the tree. It ran over `270d3aed`
with this record, `gaps.md` and the Status cell in the working tree, which
is the content of the commit that adds them, and gave 5323 passed, 10
skipped and none failed. `seal rules --check`, `seal layout --check` and
`seal layout --pairs` exit 0 at `270d3aed`.

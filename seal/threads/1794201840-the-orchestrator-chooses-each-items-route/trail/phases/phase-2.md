# Phase 2: 1794201840-the-orchestrator-chooses-each-items-route

## What this phase found

**The frame holds for this phase.** At `541e082e` every coordinate the
phase builds on stood where the frame put it (read):
`agents/sealer.md` step 4 and `skills/settle/SKILL.md` step 5; G22's lines
in `README.md` (`:15`, `:120`, `:122`, `:125`, `:131`), `README.ko.md`
(`:15`, `:122`, `:124`, `:127`, `:133`), `CONTRIBUTING.md:401`,
`skills/code-review/orchestration.md:417`, `evals/scripts/rule_cases.py:164`
and `tests/lib/test_routing.py:305-306`; G23's lines in
`tests/text/test_the_direct_answer_owes_the_sealers_record.py`. The rule
change on `docs/releasing/release-checklist.md` *2b. Settle what earlier
releases left behind* has a `from` text the section holds, so the policy in
force there reads `direct` (executed: the case below, green).

**Seen red before each case was committed** (executed, each through
`seal mutate`, which restored the file from its held bytes):

- `tests/lib/test_routing.py#Test_parse.test_refuses_an_unreadable_automation_answer`
  gains the spelling `complete`. It asserts a spelling is not read as an
  answer, so it was shown red with only that guard removed: `lib/routing.py`'s
  membership test widened to `AUTOMATION_ANSWERS + ("complete",)`. The case
  failed at `AssertionError: complete`.
- `tests/text/test_the_direct_answer_owes_the_sealers_record.py#test_the_release_checklist_names_the_waiver_as_the_no_work_item_answer`
  now reads step 2b as in force, through
  `tests/behaviour/test_waiver_decided_at_start.py#in_force`, and asserts
  "`direct` answer". The guard is this work item's rule change, so it was
  shown red with that change's `to` text set back to "`no work item`
  answer" in `frame/design.md`. The case failed at its assertion naming
  "`direct` answer". Against the root's text alone it would also fail, so
  it reads `direct` before the settle only through the rule change and
  after the settle through the root.

No unit of this phase adds code behaviour beyond those two cases. The
sealer's and the settle's sentences are prose an agent reads, which
`frame/design.md` rows S6 and S7 leave to review, so they owe no
`seal mutate` run; `gaps.md` *Not verified* names who answers them.

**Departures from the frame, each with its grounds.**

- **`README.md`'s and `README.ko.md`'s paragraph after the list is
  rewritten too.** It said "Under `automation`, the session does not stop
  to ask". *Scope* item 7 names the opening paragraph and the list, and
  G22 lists the line (`README.md:131`, `README.ko.md:133`). It now says
  this holds where `routing.md`'s `Automation` row reads `yes`, which
  `complete` always writes and `agentic` may choose. Judged against
  `frame/design.md` *Scope* item 10, which covers every statement naming
  an answer by its old label.
- **The opening paragraph of each README no longer says agents frame,
  build, review and seal every change.** Under `agentic` a small change
  takes `direct` and runs no agent, so the sentence now opens "Where an
  item needs them all". Judged against *Scope* item 7, which asks the
  paragraph not to promise what the marked answer may not do.
- **`skills/code-review/orchestration.md:417` names the `Automation` row,
  not `complete`.** *Scope* item 10 says so; the quoted default stands in
  `frame/questions.md` on any run whose row reads `yes`, whichever answer
  wrote it.
- **The settle's sentence names a settle's commit and a durations refresh
  as carrying the trailer with no route chosen.** G8 states both carry the
  value without a routing question, and a settling session listing the
  release's trailer commits meets its own earlier settle's commits among
  them.
- **A comment in `tests/text/test_the_direct_answer_owes_the_sealers_record.py`
  says why its file and function names keep "the direct answer"**: the
  names stay by `frame/plan.md` *Alternatives considered*, and a reader of
  the docstrings, which now say `straight to the PR`, would otherwise find
  two names for one answer with no reason given.

**Census of the old labels at HEAD** (executed: `git grep -n -w
"automation"`, `git grep -n "per axis\|\`no work item\`\|\*\*no work
item\*\*"` and `git grep -n -i "direct answer\|direct route"`, each outside
`seal/threads` and `CHANGELOG.md`). What remains:

- In the policy root, `docs/releasing/release-checklist.md:72`,
  `docs/running/the-review-and-parity-arms.md:53`, `:54` and `:61`, which
  the design's `## Rule changes` rewrite at the settle.
- History that stays: `evals/scripts/replay_targets.py:302`, and the notes
  naming the old label beside the new one in
  `tests/behaviour/test_waiver_decided_at_start.py:50`, `:379`, `:495`,
  `tests/text/test_review_axes.py:254` and
  `tests/text/test_the_direct_answer_owes_the_sealers_record.py:43` and
  `:89`.
- `automation` as the parser's key and the row's lower-case name in
  `lib/routing.py`, `tests/lib/test_routing.py` and
  `tests/behaviour/test_waiver_decided_at_start.py:321-333`; the trailer
  value `no work item` (G8); and the ordinary English uses G22 names.

**Decisions made while writing, each with its grounds.**

- The release checklist case imports `in_force` from
  `tests/behaviour/test_waiver_decided_at_start.py` rather than moving it
  into `tests/conftest.py`. *Scope* item 11 names that helper, test modules
  in this repository import from one another (for example
  `tests/behaviour/test_a_cited_section_stands_in_its_file.py`), and moving
  it is a refactor no row of the plan asks for (`agents/crafter.md`
  *Never*).
- `complete` joins `automation` in the spelling list rather than replacing
  it. `automation` is still the row's name in lower case, which a session
  reaching for the row writes.

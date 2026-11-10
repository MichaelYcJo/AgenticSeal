# Phase 1: 1794289595-the-verifying-round-rule-has-four-owners

## What this phase found

**Whether the frame holds.** It holds for phase 1, with one sentence it did
not place. Every
heading and bold lead the new citations name stands in its file, and
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` passes on them
(executed). Every literal `frame/plan.md` *Technical context* lists for the
four files stayed word for word, and the narrow run of the ten modules of
the phase's row is green on them (executed).

The sentence the frame did not place stands in
`skills/code-review/orchestration.md`, under `### A regression is routed by
comparing the fix with the frame`. At `0d73b6ed3` its lines 228 to 230
said what the grounds of a `regression:` finding open with and hold.
`frame/design.md` *Scope* item 3 says the section keeps the routing table
and the framer's route, and *Removes* names lines 115, 116, 118 to 119 and
209 to 213 of that file and not these. The first departure below is what
the phase did with it.

**Departures from the frame.** There are two.

1. **The sentence on what a regression's grounds hold became a citation,
   and `frame/design.md` *Removes* does not name that removal.** The
   paragraph now reads "Its grounds hold one sentence comparing the fix
   with the frame, as `skills/code-review/SKILL.md` *Earlier rounds*
   states, and you route the round on that sentence". Grounds: the table
   that opens `frame/plan.md` *Technical context* gives "a `regression:`
   line's reference and its grounds" to *Earlier rounds*, and the lead of
   *Scope* item 3 says `orchestration.md` states "nothing another file
   owns". Left as it read, the sentence was a second statement of a part
   that table gives one owner. Judged against `frame/plan.md` *Technical
   context* and `frame/design.md` *Scope* item 3. The routing table, the
   stop-row sentence and the framer's route are unchanged.
2. **The *Target* row no longer lists the record files a round reads.** It
   cites `agents/proofer.md` *Rules* twice by bold lead: **A verifying
   round answers the closed findings** for the bound, and **Every round
   reads the work item's records that state the present** for the read of
   the records. *Scope* item 3 asks for both citations and says nothing of
   the list of eight files the row held. The list is that second rule's
   own text, so the row keeps the citation alone. Judged against
   `skills/core/SKILL.md` *The rule a mechanism is kept against*, "A fact
   has one source, and every other place links to it".

**Decisions made while writing.** Each names its grounds and the document
it was judged against.

- **The defining sentence names the three lines, and three sentences after
  it give each line's meaning.** The sentence is "Every finding the round
  before closed `fixed <commit>` or `rejected` is named this round by
  exactly one of three lines: `confirms:`, `regression:` or `reopens:`."
  The `RULES` row and the changed case both read that one sentence.
  *Earlier rounds* is now three paragraphs, and its `check:` line stands
  after the last. Judged against `frame/design.md` *Scope* items 1 and 7.
- **A finding of new work "takes neither a `regression:` nor a `reopens:`
  line".** *Scope* item 1 says "takes neither line". The section names
  three lines, so the two are written out. A finding of new work names no
  earlier finding, which is what
  `docs/forms/the-round-record.md` *The round record* states for both
  lines. Judged against `skills/writing-style/SKILL.md` *에이전트와 검사가
  읽는 글은 한 가지로만 읽히게 쓴다*.
- **Each link of the `RULES` row is the citation alone**,
  `skills/code-review/SKILL.md` *Earlier rounds* in backticks and italics,
  the same string for the three carriers. `orchestration.md` holds it three
  times and `the-run.md` twice, so the row goes red for either file only
  when every one of its citations is gone. `agents/proofer.md` holds it
  once. Judged against `frame/design.md` *Scope* item 7, which asks for a
  link from each file and no more.
- **`docs/running/the-run.md` line 8 keeps the exception's clause**, from
  "and a fix pass owes none only where" to the citation of
  `docs/checks/the-pull-request-check.md`, as the phase's row in
  `frame/plan.md` says. The clause now ends its sentence, and the sentence
  that cites *Earlier rounds* follows it.

**Seen red, and the mutation runs.** The new row was red against the old
tree, and three `seal mutate` runs each ended `red`.

- The `RULES` row `21 a closed finding is answered on one of three lines`
  was red against the four files as they stood at `5c5f11695`:
  `test_the_owner_states_the_rule` and `test_every_link_names_the_owner`
  both failed for it (executed, `bin/test
  tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k "21 or
  reopens"`, exit 1, 2 failed and 1 passed).
- `test_a_close_that_does_not_hold_reopens_it` relaxes a requirement, so it
  was green against the old tree and took its red from contract rule 15.
  With the defining sentence taken out of *Earlier rounds*, it failed at
  `assert both(SKILL)` with "skills/code-review/SKILL.md names the channel
  nowhere", and the owner half of the `RULES` row failed with it
  (executed, `seal mutate skills/code-review/SKILL.md`, verdict `red`).
- With the citation taken out of `agents/proofer.md`,
  `test_every_link_names_the_owner` failed for row 21, naming
  `agents/proofer.md` (executed, `seal mutate agents/proofer.md`, verdict
  `red`).
- With `reopens:` taken out of the defining sentence, the changed case
  failed at its second assertion, "names the channel by `confirms:` and
  `regression:` alone" (executed, `seal mutate
  skills/code-review/SKILL.md`, verdict `red`).

Each `seal mutate` run restored its file, and `git status --short` printed
nothing after the last one (executed).

**`frame/questions.md` Q1, for the sections phase 1 rewrote.** No case holds a sentence of those sections through a string built at run
time. The first narrow run of the row's ten modules had two red cases and
neither was such a pin (executed). One was
`tests/behaviour/test_docs_line_wrap.py` on a line of
`skills/code-review/orchestration.md` this phase had left 128 columns wide,
which was rewrapped. The other was
`test_every_spec_directory_that_reached_the_ladder_has_an_overview`, red
until `gaps.md` existed. Phase 2 rewrites other sections, so the row stays
open for it.

**The runs.** Each was executed by this phase.

- The phase boundary set, in one command at `e15ed537d` (executed, exit 0,
  3170 passed and 9 skipped): `bin/test tests/text tests/behaviour
  tests/skills/test_chain_check.py tests/skills/test_settle.py
  tests/skills/test_passages.py tests/skills/test_payload_meter.py
  tests/skills/test_broad_gate.py tests/skills/test_test_layout.py
  tests/github/test_rules.py tests/github/test_release_report.py
  tests/lib/test_config.py tests/lib/test_core.py
  tests/evals/test_noninferiority.py tests/evals/test_rule_cases.py -q`.
  It holds the ten modules of the phase's row, the tree-wide files
  `CONTRIBUTING.md` names, and each test file outside them that names a
  changed path.
- `uvx ruff check` and `uvx ruff format --check` on
  `tests/text/test_the_rules_have_one_owner.py` (executed, exit 0 each).
- The greps of the scenarios (executed):
  - S1: `grep -c -F 'code-review/orchestration.md' docs/running/the-run.md`
    prints 1. The three greps that must find nothing find nothing.
  - S2: `grep -c -F` of `confirms:` in backticks prints 0 for
    `agents/proofer.md`, `skills/core/SKILL.md`,
    `skills/agent-contract/SKILL.md` and
    `skills/code-review/orchestration.md`.
  - S4: `grep -c -E 'regression:|reopens:|confirms:' agents/proofer.md`
    prints 0.
  - S5: the grep for "judged the run excessive" and "departed from the
    frame" in `docs/running/the-run.md` finds nothing, and `grep -c -i
    'signals'` prints 1.

**Other statements of the reworded rules, a sample.** `git grep -n -E 'confirms:|regression:|reopens:' -- '*.md'` outside
`seal/threads` lists, beyond the four files, the statements below
(executed). The list is a sample: a statement in other words is outside
it, and so is a docstring or comment under `skills/code-review/scripts/`,
`lib/` and `tests/`, which the search did not read.

| Coordinate | What it says | Why it stands |
|---|---|---|
| `docs/forms/the-round-record.md`, the paragraph **Each round answers to the next by reference** | the three relations as the check reads them | `frame/design.md` *Grounding* G7; `gaps.md` `## Not done` names it |
| `docs/checks/the-pull-request-check.md`, the paragraph **Of a round record the check reads its `seal` blocks** | which line the check requires | it says what the script refuses, and defines no line |
| `docs/releasing/release-checklist.md`, the lines on the findings that carry a `regression:` or `reopens:` line | what a release report counts | a count, and no meaning of a line |
| `agents/framer.md`, "when the orchestrator routes a `regression:` to you" | when the framer is spawned again | what a party does with such a finding |
| `templates/records/sdd-round.md` | the lines in an example record | the form |

The citations of `docs/running/the-run.md` *The run* across the tree were
listed with `git grep -n -F '*The run*'` and each was read against the
section as it now stands (executed for the list, read for each). None
cites it for the target of a verifying round, the two routes, the second
regression or the stop row: `README.md`, `README.ko.md`,
`agents/crafter.md`, `agents/framer.md`,
`docs/releasing/issues-and-milestones.md`,
`docs/running/the-agent-set.md`, `lib/routing.py`,
`skills/implement/SKILL.md`, `skills/implement/orchestration.md` and
`skills/verify/orchestration.md` each cite a sentence the section keeps.

**For phase 2.** Three things carry over.

- The frame's line numbers were read at `0d73b6ed3`. In
  `skills/code-review/orchestration.md` every line after 119 now stands
  three or four lines earlier, and `docs/running/the-run.md` is shorter by
  20 lines, so each site of *Scope* item 5 is found by its
  words. `docs/running/the-run.md` still holds its site on line 8.
- `RULES` in `tests/text/test_the_rules_have_one_owner.py` holds row 21 and
  the constant `EARLIER_ROUNDS`. The exception's row takes the next number.
- `agents/proofer.md` step 7 is unchanged: the notice sentence is phase
  2's.

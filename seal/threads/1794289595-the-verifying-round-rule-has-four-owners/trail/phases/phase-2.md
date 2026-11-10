# Phase 2: 1794289595-the-verifying-round-rule-has-four-owners

## What this phase found

**Whether the frame holds.** It holds for phase 2, with two statements the
tree does not bear out.

- `frame/design.md` *Scope* item 8 says `changelog.md` "is written from its
  template". `templates/records/` holds no template for the fragment
  (executed, `ls templates/records/`). It holds `process.md`, the shape of
  the `### Process changes` table, and the fragment was written in the
  shape the four fragments under `seal/threads/` have, with that table from
  `process.md`.
- `frame/design.md` *Scope* item 5 lists the sites of the exception and
  calls its list a sample. One site in `skills/code-review/orchestration.md`
  is outside it. The first departure below is what the phase did with it.

Every site item 5 lists was found by its words, as `trail/phases/phase-1.md`
advised, and each stood where the frame's list placed it.

**Departures from the frame.** There are two.

1. **One more site in `skills/code-review/orchestration.md` became a
   citation.** In *Orchestrator: the pull request opens once the sealer
   seals*, the paragraph **On the broad run's exit 1 spawn nothing** said
   "Review a repair where it touched a file outside the work item's
   records". That is the condition of the core's row, stated for a repair,
   and `frame/design.md` *Removes* gives "each statement of the exception's
   condition outside the core" to the row. The sentence now reads "Review a
   repair that the row *No fix that no round reads* of
   `skills/core/SKILL.md` *Judgment is not licence to skip a party* gives
   to a round". Judged against `frame/design.md` *Removes* and contract
   rule 12.
2. **In the paragraph on the run's end, the clause on what may follow the
   last record cites the row too.** It said the last record's `target:`
   commit "is HEAD, or is followed only by the work item's own records". It
   now says "or is followed only by commits the core's row gives to the
   sealer". *Scope* item 5 lists those lines as a site, and the clause is
   the first condition of the exception, so it went with the others. The
   search of scenario S3 does not match the old clause, so the scenario
   could not have shown it. Judged against `frame/design.md` *Scope* item 5.

**Decisions made while writing.** Each names its grounds and the document
it was judged against.

- **Each site says which party the row gives a change to, and no site says
  on what condition.** The forms are "a fix pass that the row … gives to
  the sealer", "a `fixed` one that the row … gives to a round" and "where
  its reader is the sealer, by the row …". The row's cell names two
  readers, a round and the sealer, so a site names one of them and the
  condition stays in the cell. Judged against `frame/design.md` *Scope*
  item 5, "states no condition of its own".
- **Inside one paragraph the row is named in full once, and after that as
  "the core's row".** *Orchestrator: the run ends with a verifying round*
  also speaks of rows of `frame/plan.md` *Judgments of the run*, so a bare
  "that row" would have had two readings. Judged against
  `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만
  읽히게 쓴다*.
- **The sentence "A finding located in code is read by a round whatever its
  fix touched" left `skills/code-review/orchestration.md`.** It restated
  the second condition, which the core's cell now holds. Judged against
  `frame/design.md` *Scope* item 5.
- **The sentence in `docs/checks/the-pull-request-check.md` keeps "which
  reads every record at HEAD (`agents/sealer.md` step 2)".** It says why
  the check passes such a finding and states no condition. The sentences
  before it, on what the check refuses, are unchanged: the paragraph's bold
  lead says what the script refuses, as *Scope* item 5 keeps it.
- **The wording around the citation differs from file to file.** The first
  draft used one clause, "the row … gives its fix to the sealer", in two
  files and another in two more, and
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py` named both
  pairs as runs of 15 words (executed, exit 1). `docs/running/the-run.md`
  and `skills/implement/orchestration.md` were reworded, and the case
  passes.
- **The notice sentence is two sentences.** Step 7 of `agents/proofer.md`
  reads "A finding you take from such a notice quotes the notice. Those
  quotes in the round records are the record `skills/core/SKILL.md` *The
  rule a mechanism is kept against* weighs the notices by, counted with
  `git grep -F` on a notice's words." Judged against `frame/design.md`
  *Scope* item 6 and *Grounding* G11.
- **`changelog.md` ends with `### Process changes`.** The work item's diff
  changes `skills/core/SKILL.md`, `agents/proofer.md` and two
  `skills/*/orchestration.md` files. The table has four rows, one per
  change to the way of working. Judged against
  `docs/layout/the-record-layout.md` *A change writes fragments, never a
  shared file*.
- **The build is one commit, amended once before any record named it.** A
  reading of the diff found "that row" with two readings in three places.
  The correction was folded into the unpushed build commit, so the commit
  that adds `changelog.md` and moves the version is still the one commit
  scenario S7 asks for. The mutation runs below were taken before the
  amend, and the amend changed no line they read.

**Seen red, and the mutation runs.** The new row was red against the tree
as it stood, and three `seal mutate` runs each ended `red`.

- The `RULES` row `22 a change after the last round is read by a round, or
  by the sealer` was red at `6296f28aa`: `test_the_owner_states_the_rule`
  and `test_every_link_names_the_owner` both failed for it, the second
  naming `docs/running/the-run.md` (executed, `bin/test
  tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k 22`, exit
  1, 2 failed).
- With the second condition taken out of the core's cell,
  `test_the_owner_states_the_rule` failed for row 22 with
  "skills/core/SKILL.md no longer states rule" (executed, `seal mutate
  skills/core/SKILL.md`, verdict `red`).
- With the row's name taken out of the citation in
  `docs/checks/the-pull-request-check.md`,
  `test_every_link_names_the_owner` failed for row 22, naming that file
  (executed, `seal mutate docs/checks/the-pull-request-check.md`, verdict
  `red`).
- With the citation in `skills/implement/orchestration.md` reworded to "by
  the table of", the same case failed, naming that file (executed, `seal
  mutate skills/implement/orchestration.md`, verdict `red`).

Each run restored its file, and `git status --short` printed nothing after
the last one (executed). `skills/code-review/orchestration.md` holds the
full citation six times and `docs/running/the-run.md` once, so the row
goes red for the first file only when all six are gone.

**`frame/questions.md` Q1, for the sections phase 2 rewrote.** No case
holds a sentence of those sections through a string built at run time. The
first narrow run of the row's six modules had two red cases, and neither
was such a pin (executed). One was
`tests/behaviour/test_docs_line_wrap.py` on a line this phase had left 98
columns wide. The other was the paste check named above, red on this
phase's own repeated wording. With phase 1's answer, the row is answered
for every rewritten section: no pin of that kind exists. The crafter's
definition names no write to `frame/questions.md`, so the row's Status
cell is the orchestrator's to fill.

**The runs.** Each was executed by this phase.

- The six modules of the phase's row, in one command at `54ebe2e74`
  (executed, exit 0, 192 passed): `bin/test
  tests/text/test_the_rules_have_one_owner.py
  tests/behaviour/test_a_cited_section_stands_in_its_file.py
  tests/text/test_no_passage_is_pasted_into_a_second_file.py
  tests/behaviour/test_docs_line_wrap.py
  tests/text/test_ci_gives_the_checks_what_they_need.py
  tests/lib/test_core.py -q`.
- The phase boundary set, in one command at `54ebe2e74` (executed, exit 0,
  3735 passed and 9 skipped): `bin/test tests/text tests/behaviour
  tests/evals/test_noninferiority.py
  tests/github/test_plugin_directory_check.py
  tests/github/test_release_completeness_check.py
  tests/github/test_release_report.py tests/github/test_release_seal.py
  tests/github/test_roll_flow_measurement_issue.py
  tests/github/test_rules.py tests/github/test_tag_release.py
  tests/hooks/test_core_start.py tests/lib/test_core.py
  tests/skills/test_broad_gate.py tests/skills/test_chain_check.py
  tests/skills/test_passages.py tests/skills/test_payload_meter.py
  tests/skills/test_pr_body.py tests/skills/test_seal.py
  tests/skills/test_settle.py tests/skills/test_test_layout.py -q`. It
  holds the six modules, the tree-wide files `CONTRIBUTING.md` names, and
  each test file outside them that names a path this phase changed, listed
  with `git grep -l` on the eight paths.
- `uvx ruff check` and `uvx ruff format --check` on
  `tests/text/test_the_rules_have_one_owner.py` (executed, exit 0 each).
- `tests/lib/test_core.py` passes with the core at 9,276 characters
  (executed, `wc -m`), below the cap `frame/design.md` *Grounding* G15
  names.
- The greps of the scenarios (executed):
  - S3: the search lists one line, `skills/core/SKILL.md:107`.
  - S6: `grep -n 'settle can count' agents/proofer.md` finds nothing, exit
    1.
  - S7: `grep -n '"version"' .claude-plugin/plugin.json` prints `0.37.2`
    on line 4. `git log` for `.claude-plugin/plugin.json` and `git log
    --diff-filter=A` for `changelog.md` both name `54ebe2e74`.

**Other statements of the reworded rules, a sample.** `git grep -n -i -E`
on "outside the work item", "only the work item's", "work item's (own )?
records" and "verifying round" over the `*.md` files outside
`seal/threads`, and `git grep` on "settle can count", "what the notices
caught" and "by the sealer where it touched" over the tree, list the
statements below beyond the changed sites (executed). The list is a sample:
a statement in other words is outside it, and so is a docstring or comment
under `skills/code-review/scripts/`, `lib/` and `tests/`, which
`frame/design.md` *Scope* puts out of scope and the search did not read.

| Coordinate | What it says | Why it stands |
|---|---|---|
| `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, "Where the merge resolved a conflict in a file outside the work item's records" | a merge resolution outside the records gets a verifying round | its grounds are its own, that the check reads no merge commit; `gaps.md` `## Not done` names it |
| the same section, the paragraph **The stated limit**, "Its fix is a commit outside the work item's records" | a platform defect's fix takes the repair path | a fact about one fix, and no condition for the sealer; `gaps.md` names it |
| `docs/running/the-review-and-parity-arms.md`, the row *through the review chain* | the last record's `target:` commit at HEAD or followed only by the records | what the check reads; `gaps.md` names it |
| `docs/checks/the-pull-request-check.md`, the sentences before the changed one in the paragraph **The last record is at HEAD** | what the check refuses in the last record | *Scope* item 5 keeps the paragraph's statement of what the script refuses |
| `docs/checks/the-pull-request-check.md`, the paragraph on the notices, "The proofer weighs each notice at review" | how a notice is weighed | `frame/design.md` *Scope*, out of scope; it names no settle as the reader of a quote |
| `skills/implement/orchestration.md`, the sentence on a version move after a work item's last round | such a move owes a verifying round | `frame/plan.md` *Overlap with the release* leaves it for #1477; it states no exception |
| `skills/core/SKILL.md`, the row's `Held by` cell | what the check reads | `frame/design.md` *Scope*, out of scope |

No file outside `seal/threads` holds "settle can count" or "what the
notices caught" (executed). The citation of
`docs/checks/the-pull-request-check.md` *What the check reads at the pull
request* that `docs/running/the-run.md` line 8 made is gone with the clause
it closed, and the heading still stands in its file.

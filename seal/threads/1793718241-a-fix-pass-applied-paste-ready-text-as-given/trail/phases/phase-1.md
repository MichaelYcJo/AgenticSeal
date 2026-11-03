# Phase 1: 1793718241-a-fix-pass-applied-paste-ready-text-as-given

## What this phase found

**The frame holds at the seven coordinates it builds to.** At `f75efb6a6`,
`agents/crafter.md:167` opened the paste-ready sentences, rule 15's heading
stood at `skills/agent-contract/SKILL.md:179`, and "A case that passes there
was never red" stood at `agents/sealer.md:145`. "observed failing against the
pre-change code" stood at `skills/verify/SKILL.md:43`, "seen red against the
tree as it stands" at `skills/implement/SKILL.md:163`, and "takes the snippet
as the repair" at `skills/code-review/SKILL.md:172`. The pin
`test_the_crafters_fix_pass_appends_a_close_block_and_sweeps_what_its_range_reworded`
stood at `tests/text/test_a_moved_rule_leaves_its_definition.py:454` (executed,
one `grep -n` per coordinate). The G8 search, run again before the build,
printed the hits `frame/design.md` G8 names and no other sentence that states
a new case's red (executed).

**Three of the frame's verification commands do not print what their rows
say, and the build follows the convention or the count the tree gives.**

- S5's command, `git grep -n 'contract rule 15' -- skills/verify/SKILL.md
  skills/implement/SKILL.md agents/sealer.md`, prints one line for each skill
  and none for `agents/sealer.md` (executed). A definition under `agents/`
  cites a contract rule as `rule <N>`, as `skills/writing-style/SKILL.md`
  *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* states and as the
  sealer's own citations of rules 2 and 6 do. So the sealer's sentence reads
  `(rule 15)`, and `git grep -n 'rule 15' -- agents/sealer.md` prints its line,
  `agents/sealer.md:147` (executed). Judged against that writing-style section.
- S6's command over `.` prints five lines, every one a quotation of the old
  sentence in this work item's own `frame/design.md` and `frame/plan.md`
  (executed). With `':!seal/'` added it prints nothing and exits 1 (executed),
  which is what the row means.
- S7's row says the diff holds "the six files of *Scope* items 1 to 7". Items
  1 to 6 are six files and item 7 is the test module, so the diff outside
  `seal/` holds seven files, those seven and no other (executed: `git diff
  --stat b47104fa6...HEAD -- ':!seal/'`).

**The sealer re-runs a guard case in its clone, not at HEAD.** `frame/design.md`
*Scope* item 3 says the case is "re-run at HEAD with that guard alone removed".
The same paragraph of `agents/sealer.md` says "never change the tree under
audit", and removing a guard at HEAD would change that tree. The sentence reads
"re-run in the clone at HEAD's code with that guard alone removed". Judged
against `agents/sealer.md` *A `seen red` is re-run against the code before the
change*.

**The crafter's sentences depart from the frame's draft in two places.** The
draft's "without waiving this reading" pointed at a reading the next sentence
states, so it reads "without waiving the reading below". The draft's "the
phase's `frame/plan.md` row" has no phase in a fix pass, which is the act the
paragraph governs, so it reads "the `frame/plan.md` row of the phase that built
it". The release sentence and the own-words sentence stand as they were, as
*Scope* item 1 says. Judged against `skills/writing-style/SKILL.md`
*에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*, the rule that a
sentence an agent reads has one reading.

**The verify clause and the implement sentence are worded apart, and neither
says "absence".** The two state one fact in two files, and
`tests/text/test_no_passage_is_pasted_into_a_second_file.py` refuses a run of
15 words shared by two files, so they share no such run (executed: the case
passes). The verify clause says "one asserting that nothing is named" because
the next section of that file, *An absence claim is only as good as the search
behind it*, uses "absence" for a search that found nothing.

**Each changed clause of the pin was seen red with its sentence deleted.**
`seal mutate agents/crafter.md` ran four mutants over `bin/test
tests/text/test_a_moved_rule_leaves_its_definition.py -q -p no:xdist -k
test_the_crafters_fix_pass_appends_a_close_block`, at `3f74055b5`. The baseline
passed and each mutant went red (executed). Each failing line was read, and
each names the clause its mutant deleted (executed):

| Deleted | Failing line |
|---|---|
| "A paste-ready fix is the proofer's claim and not the fix," | `the fix-pass rule lost "A paste-ready fix is the proofer's claim and not the fix"` |
| ", and a spawn prompt or a judgment row that tells you to apply it names the fix without waiving the reading below." | `the fix-pass rule lost 'a spawn prompt or a judgment row that tells you to apply it names the fix without waiving the reading below.'` |
| the sentence "Apply it only after reading it against the frame and the code: …" | `the fix-pass rule lost 'Apply it only after reading it against the frame and the code: …'` |
| "A procedure step is also read as its own reader would: " | `the fix-pass rule lost 'A procedure step is also read as its own reader would'` |

The pin's unchanged clauses, the release sentence and the own-words sentence
among them, pass at HEAD (S2, executed). No other unit adds behaviour: every
other change is prose, and the cases that parse those files are the boundary
run below.

**Other statements of the two old facts, found by `git grep` on their words,
stand true.** For the paste-ready reading, `git grep -n -i "paste-ready\|as
given"` over the shipped roots printed `docs/forms/the-round-record.md:57`,
`docs/running/the-run.md:36`, `skills/code-review/orchestration.md:206` and
`skills/code-review/SKILL.md:182` (executed). The first states the close
block's place, the next two route a fix applied as given to a fix pass, and
the last counts the regressions of 0.26.0 to 0.29.0. Each stays true after
this work. For a new case's red, the G8 search also prints
`skills/verify/SKILL.md:292`, "A new test that passed on first run and was
never seen red", which stays true, since a guard case shown red under its
guard was seen red. Both searches range over spellings, so their lists are a
sample (contract rule 12).

**The pin's docstring and comments were read.** The docstring says the case
holds the definition's paragraph, which stays true. The #1148 comment above
the first clause records why that clause came, and a new #1286 comment
records why the two new clauses came.

**The changelog fragment carries a `### Changed` entry beside the process
rows.** `frame/design.md` *Scope* item 8 names the two process rows. The
fragment is the work item's entry in the release notes
(`docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/*), and
`.github/scripts/publish_release_note.py#section` lifts the process rows out
of each fragment, so a fragment of process rows alone would leave the entry
with no text. Judged against that layout document and the publisher.

**The boundary run.** One `bin/test -q` over the 93 modules that name one of
the seven changed files or glob `agents/` or `skills/`, joined to the 13 that
read `seal/threads/`, ran after the records were written: 106 modules, 5222
passed and 12 skipped, exit 0 (executed). Before the records
were written, the same 93 modules gave one failure,
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
on this work item's missing `gaps.md` (executed), which this phase's records
answer.

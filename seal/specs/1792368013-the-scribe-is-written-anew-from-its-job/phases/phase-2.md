# 1792368013-the-scribe-is-written-anew-from-its-job — phase 2

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | c8391342 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Write `agents/scribe.md` anew to the four-section shape with
`skills: [agent-contract]`, opening `legacy-parity` at step 1, its
description saying the session spawns it rather than the smith. Sort the
scribe's pins per #957's Q7: re-point a pin whose rule stays, remove one that
pinned narration with one line here. Plant T3. Delete the scribe's
`NOT_YET_REWRITTEN` entry, rewrite the docstrings that named it, add the
scribe to `COVERED` and delete the follow-up row that waited on this item.
In both READMEs, change the scribe's row, the count of skills the agents
follow from their first tool call, and the four sentences naming the smith
as the party that asks a setup question. #968 edits the same test module and
README rows in its own worktree and rebases over this item.

## What this phase found

**The scribe fits the budget phase 1 set.** `agents/scribe.md` is 3,319 B
(3,763 at 1d665d48), and with `legacy-parity` at 5,688 B the two files read
9,007 B against the 9,088 B allowed. Phase 3 measures it with
`payload-meter`.

**Step 1 names the sections phase 1 named.** The scribe reads *The migration
config*, *What the original sends* and *The original's coordinates*, and the
step says the other sections are its caller's. Step 2 returns `original not
found` with what was tried, which is where the skill's resolution order ends
for a reader that cannot ask. The step that opens the skill says the path is
the plugin's, in the words the smith's and the warden's step 1 use, so the
pair counts with both stay within the `BASELINE` of
`tests/test_no_passage_is_pasted_into_a_second_file.py`.

**`Job` keeps the bound phrase the shape case reads.**
`tests/test_every_agent_reads_the_contract.py#BOUNDS` accepts *You write
nothing durable anywhere, and that is the whole of it*, which the old scribe
carried; the new `## Job` keeps it, so the case needed no new phrase.

**The README class is eight sentences, not four.** The frame's four
coordinates are not two pairs of twins: each README states the bootstrap as
the smith's act three times (the parity question, the `seal/` question in
*First run*, and the same question under *Shared or local*), and once more
as *the smith creates from `templates/`*. All eight now name the user's
session, which `skills/implement/orchestration.md` §*Orchestrator: Bootstrap
— create what's missing* gives both the question and the creation to.
`overview.md` records the widening.

**One more reader of the README count.**
`tests/test_chain_hooks_hardening.py::test_the_readme_group_counts_are_derived_too`
derives each group's size from the tree and spells it from a table that held
no entry for three or thirteen. It went red at the new counts, and the two
spellings were added, as its own message asks.

**A script prints the same false sentence, and is left.**
`skills/implement/scripts/seal.py:678` tells a person *The first time the
smith works in a repository it asks which one, and creates it.* No case reads
that output, and a change to it needs one (contract §14); the frame names no
script. `overview.md` §*Not done* holds it for the orchestrator to file.

### The pins (Q3), sorted

`git grep -n -w scribe -- tests`, re-read at c8391342. No pin on the scribe
pinned narration, so no case was removed.

| Case or hit | Rule or narration | Re-pointed to, or why it stands |
|---|---|---|
| `tests/test_absence_claims.py::test_the_scribe_does_not_file_an_unrepeatable_absence_as_a_fact` | rule | the rule *An absence carries its search.*, which keeps both asserted phrases |
| `tests/test_a_probe_that_commits_says_so.py::test_the_fact_finder_points_at_the_rule_it_no_longer_restates` | rule | the rule *Constraints, enums and defaults are read, not probed.*, which keeps `§8`; the docstring names the rule instead of *step 4* |
| `tests/test_a_probe_that_commits_says_so.py:109`, a docstring | — | stands: step 5 still points at §7 |
| `tests/test_every_agent_reads_the_contract.py#NOT_YET_REWRITTEN` and its two docstrings | — | the scribe's entry deleted; the docstrings now say *a definition not yet written anew* rather than naming #968 to #970, so #968's rebase deletes the last entry without rewording them |
| `tests/test_docs_line_wrap.py:21`, `:146-147`, `:152-154` | — | the scribe's maximum and the two comments naming it as uncovered rewritten; the scribe is in `COVERED` |
| `tests/test_no_passage_is_pasted_into_a_second_file.py#BASELINE`, four scribe pairs at 65 | — | unchanged and green: the contract sentence is still the shared run |
| `tests/test_chain_hooks_hardening.py:1327` | — | stands: a comment dating #426's measurement, which is history |
| `tests/test_session_cost.py`, `tests/test_the_implementer_is_recorded.py`, `tests/test_the_payload_meter_says_what_it_measured.py`, `tests/test_the_seal_is_taken_once_by_the_sealer.py#RUNNERS`, `tests/test_the_handoff_before_round_one.py:70`, `tests/test_waiver_decided_at_start.py` | — | stand: each names the scribe as an agent type, a runner word or `templates/sdd-routing.md`'s step, and none reads `agents/scribe.md` |

### The new cases, each seen red

T1 and T3 were run on the old scribe with its skip entry deleted and failed:
T1 named the `skills:` list, the opening paragraph and the headings, and T3
found no `## Rules`. After the commit, `mutation-check` broke each sentence
below; every run read `red: the cases failed against the mutation (exit 1)`,
exited 0 and left `git status` clean. One first attempt was refused with
exit 2 because its text crossed a line break the command did not carry, and
was run again with it.

| Case | Mutation | The assertion that went red |
|---|---|---|
| T1 | `- legacy-parity` added back to `skills:` | the shape case for `agents/scribe.md` |
| T2 | step 1's path made `skills/legacy_parity/SKILL.md` | `test_every_file_a_step_names_exists[agents/scribe.md]` |
| T3 | the rule *Facts, never verdicts.* deleted | *lost the rule 'Facts, never verdicts.'* |
| T3 | `original not found` in the rule made *nothing* | *lost 'return `original not found` naming what was tried, and no findings'* |
| T3 | the `Enforced by:` line under *A guessed original proves nothing.* deleted | *has no `Enforced by:` line* |
| T3 | step 2's `original not found` made *the question to the user* | *step 2 no longer says what the scribe returns* |
| absence pin | *, not under facts* deleted | `'not under facts' in …` |
| probe pin | *read, not probed* made *read first* | *the scribe's own half … went* |
| README counts | *The three the agents follow* made *four* | *does not say `The three the agents follow`* |

### Commands, each with its exit code

Read with `; echo $?` or from `mutation-check`'s own verdict line, never
through a pipe. `<mods>` is every `tests/test_*.py` that
`git grep -l -E 'README|follow-up\.md|"follow-up|agents/scribe|scribe\.md|"scribe"|legacy-parity|parity-setup|templates/parity|orchestration\.md'`
names, plus `test_every_agent_reads_the_contract`,
`test_the_payload_meter_says_what_it_measured`,
`test_a_section_marked_for_one_role_reaches_only_that_role` and
`test_the_record_is_written_in_words`: 68 modules.

| Command | Exit |
|---|---|
| `bin/test` T1 and T3 (`-k scribe`) on the old scribe | 1: 2 failed, 44 passed |
| `bin/test <mods> -q` | 1: `test_the_readme_group_counts_are_derived_too` failed, 3673 passed, 8 skipped |
| `bin/test tests/test_chain_hooks_hardening.py -q`, with the two spellings | 0: 56 passed |
| `bin/test` over the eight modules `plan.md` row 2 names, at c8391342 | 0: 342 passed, 1 skipped (the framer's shape case) |
| `bin/test tests/test_a_rider_reaches_its_file.py tests/test_unverified_rows_close.py tests/test_the_set_a_work_item_always_has.py -q` | 0: 246 passed |
| `bin/rules --check --root <worktree>` | 0 |
| `uvx ruff check` and `uvx ruff format --check` on the five changed `.py` files | 0, 0 |
| `git grep -n -i -E 'smith asks\|smith works in a repository it asks\|smith 가 그 레포' -- README.md README.ko.md` | 1: no line |
| `bin/unverified-check <worktree>` | 0 |
| `mutation-check`, nine runs above, `-p no:xdist` | 0 each, `red` each |

# Phase 3: 1794383427-asserts-pin-literal-phrases

## What this phase found

**The frame holds against the tree at `a484ff838`.** *The listing* of
`frame/design.md` gives 181 asserts, 53 absence asserts and 72 cases over
the six modules of group C at `18a7e18fb`, the counts of design *The
groups* (executed). The base gives the same counts per module, and none of
the six changed between the two commits (executed, `git diff --stat`). The
line numbers below are the base's. The coordinates design G4 and *Worked
examples* give for `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`
stand at the base (read). The fold at `a484ff838` ruled this phase's
#1233-commented asserts: each stays as it stands (design *Scope* item 1).

**One departure: the phase did not start after a merge of the release
branch.** `frame/plan.md` *Phases* says each phase starts from the branch
after it has taken `release/v0.37.4` by a merge. The local
`release/v0.37.4` is `18a7e18fb`, which the branch holds, but
`origin/release/v0.37.4` stands two commits further on: `10e721f11`
(#1523) and `eec0bd040` (#1524) (executed, `git log`). A merge is no write
the crafter's definition names, so the phase ruled group C at `a484ff838`.
#1524 changes one module of group C. In
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` it removes
the listed asserts at `:173` and `:178`, and the case
`test_the_documents_name_the_ci_also_row` with its assert at `:204`
(executed, `git diff 18a7e18fb origin/release/v0.37.4`). This phase
removed `:173` and `:178` as wording, with the whole docstring case
around them, and kept `:204` as it stands, because it carries #1233's
comment. The merge meets both changes in the same hunks. Where it takes
#1524's side at `:204`, that case leaves with the merge, as the plan's
*Phases* paragraph foresees.

**S1, per module of group C.** The unit is one assert, a distinct
`path:line`, as in phases 1 and 2. The base is `18a7e18fb`. The 181 add up
as 61 kept, 76 removed and 44 not ruled (executed: the ledger summed
against *The listing* per module). The last column is *The listing* at
`e2fc0cb74`.

| Module of `tests/behaviour/` | Listed | Kept | Removed | Not ruled | Listed at `e2fc0cb74` |
|---|---|---|---|---|---|
| `test_the_seal_is_taken_once_by_the_sealer.py` | 38 | 10 | 28 | 0 | 10 |
| `test_the_stamp_reaches_the_person_it_is_drawn_for.py` | 29 | 9 | 19 | 1 | 11 |
| `test_the_suite_has_a_command_that_is_cheap_twice.py` | 34 | 17 | 15 | 2 | 18 |
| `test_chain_hooks_hardening.py` | 29 | 17 | 11 | 1 | 20 |
| `test_release_hygiene.py` | 23 | 8 | 3 | 12 | 20 |
| `test_a_foreign_seal_dir_keeps_the_records_shared.py` | 28 | 0 | 0 | 28 | 28 |
| Total | 181 | 61 | 76 | 44 | 107 |

The last column equals the kept count plus the not-ruled count except in
three modules. In the stamp module, one more: the sealer case's command
`` `seal stamp --guarantee <path>` `` stood in a loop tuple, which the
listing does not read, and now stands in the assert. In the suite module,
one fewer: the floor sentence was cut to `rt.FLOOR_TEXT`, a name the
listing does not read. In the chain hooks module, two more: each of the two
core sentences was cut to two facts, `` `AgenticSeal core from` `` and
`` `skills/core/SKILL.md` ``, each in an assert of its own.

Of the 53 absence asserts, 47 were removed, 1 was kept and 5 were not
ruled. Each removed one held text or a design that a shipped release
removed, or a literal no rule in force names. Examples are the stamp's
retired names in `seal_stamp.py`'s docstring, the template's table-walk
paragraphs, the **New?** bullet's retired causes, `rule 6 withholds stays
withheld` in `agents/sealer.md`, `## Where the stamp is drawn` in the
broad gate's document, `${CLAUDE_PLUGIN_DATA}/stamp.py`, the sentence
that the suite needs only pytest, `five minutes`, `without asking anyone`
in `plugin.json`, and `def split_row` in `chain_check.py`.

The 44 not ruled read a program's output or a text the case built. The
whole of `test_a_foreign_seal_dir_keeps_the_records_shared.py` reads what
`seal`, `chain_check.py`, `pr_body.py`, `rules.py`, `unverified_check.py`
and `pact_check.py` print. In `test_release_hygiene.py` they read
`what_to_write_instead()` and `refusal()`, the module's own builders. The
others are `--help`'s output in the stamp module, a copied wrapper's
stderr in the suite module, and `seal fold --help` in the chain hooks
module (read).

**Asserts outside the listing were ruled as well**, as design *Scope*
item 1 asks of each case that holds a listed assert. They are not in the
counts above.

- In the sealer module, every loop of retired phrases went: the
  template's four, the stamp's 26, the **New?** bullet's nine and the
  recorder's seven. The bullet's ten sentences were cut to the two
  files a reader opens, `` `suite-at-base.txt` `` and `` `records/` ``.
  The four readers of `new?` were cut to the word, `` `new?` `` in three
  files and the bullet's lead **New?** in `skills/verify/orchestration.md`.
  The recorder's eight sentences went with their case.
- In the stamp module, the orchestrator section's eleven sentences were
  cut to four facts: `` `seal stamp --guarantee` ``,
  `` `BROAD GATE PASSED` ``, `` `BROAD GATE FAILED` `` and
  `` `seal stamp --from` ``. The **Form** bullet's three sentences were cut
  to `` `seal stamp --guarantee` `` and `` `Stop` ``. The refusal record's
  six were cut to its path, its writer, the floor `seven` and
  `` `sealed_before` ``. The sealer's five were cut to the command it runs.
  Each loop of retired phrases went.
- In the update case of `test_release_hygiene.py`, `mismatch`, `PID` and
  `stop` left the loop as words. The file, field, expression, directory
  and command stay, each with a comment.
- In the chain hooks module, the core row's five retired counts went.

**Six kinds of decision recur, each judged against `frame/design.md` *The
criterion*.**

- A literal that is a fact is kept, with a comment directly above it that
  names the fact and its reader. Examples are a path, a command, a shell
  line a wrapper runs, a workflow step's script and flag, a package and
  the constant that pins it, a marker `rules.py` reads, the opening of the
  `SessionStart` hook's output, and a skill name a description hands to. A
  literal that held sentence words was cut to the fact. Examples are the
  hook command shape in `CONTRIBUTING.md`, `` ` || exit 0` `` in the stamp
  policy, `` `guarantee.md` `` in the sealer's write list,
  `` `/code-review` `` in the review skill's description, and
  `skills/agent-contract/SKILL.md` in `bin/test` and in *Running the
  checks*.
- An assert that carries #1233's comment stays as it stands (the fold at
  `a484ff838`). In group C those are the sealer module's `:97`, `:204`,
  `:783`, `:789`, `:834`, `:837` and `:883`; the stamp module's `:158` and
  `:178`; the chain hooks module's `:273`, `:277`, `:282`, `:288`, `:1049`
  and `:1052`; and the release hygiene module's `:1036`, `:1208` and
  `:1217` (executed, `git blame` on `c3e020961`'s lines). None was cut.
- A literal that is a sentence or a word of a sentence is removed.
  Examples are the stamp docstring's layout sentences, the broad gate
  docstring's row diagram, the template's bold lead on a doubled key, "The
  broad runs come once", "fallback", "seconds each", "shell builtin", "in
  plain words and naming no skill", and the description's example
  requests.
- An absence assert is kept only where a rule in force forbids its literal
  and the rule can be cited. One stands, under *Absence asserts kept*
  below.
- A case left with no assert is removed (design *Scope* item 6). Ten went.
  In the sealer module three went: the template's table walk, what a line
  names a file by, and rule 6's withheld acts. In the suite module seven
  went: the runner's owner sentence, the slow form's cost, the broad-once
  sentence, `bin/test` absent from the agent definitions, the cheat sheet,
  the runner's placement, and the serial figure. The helpers that went are
  `SCRIPT` in the suite module and the `ast` import of the sealer module.
  No module was left with no case, and no module was deleted.
- A case whose name stated what a removed assert read is renamed for what
  it still reads. Nine were renamed:
  `test_the_stamp_docstring_names_the_file_its_mark_is_drawn_from`,
  `test_the_orchestrator_is_given_the_stamps_commands_and_the_runs_lines`,
  `test_the_verify_skill_names_what_queues_the_stamp_and_what_draws_it`,
  `test_the_stamp_draws_its_sample_and_neither_command_offers_a_scale`,
  `test_the_section_names_the_contract_and_the_narrow_form`,
  `test_the_house_rule_gives_the_shape_of_each_hook_command`,
  `test_the_review_skill_names_the_built_in_command_a_person_types`,
  `test_the_entry_skill_stays_gone` and
  `test_the_core_row_names_the_core_file`. Each case that kept a fact and
  lost a sentence had its docstring rewritten in place to say what it now
  reads (design *Scope* item 7).

**Absence asserts kept.** One stands, and its comment cites the rule:
`seal stamp --from` absent from `agents/sealer.md`. The rule is
`agents/sealer.md` *Never*, its bullet that the sealer draws no stamp, and
`docs/checks/the-stamp.md` *The stamp*, its bold lead. `seal stamp --from`
is the command that draws a stamp by hand, so a definition naming it
would hand the sealer the act its rule forbids. Phase 2 kept
`AskUserQuestion` out of the definitions on the same grounds.

**These literals could be read either way, and the proofer reads each
against *The criterion* (S2).**

- `seal stamp --from` absent from `agents/sealer.md` was kept, as above.
  It is also former text, from when the sealer passed on the gate's
  command, so the removal clause could rule it too.
- `"hooks" not in manifest`, `plugin.json` declaring no `hooks` key, was
  removed. The harness reads `hooks/hooks.json`, but no rule in force
  names the manifest key, so no rule could be cited.
- `disable-model-invocation` absent from `implement`'s frontmatter was
  removed on the same grounds. The key would keep the skill from firing on
  a plain request, but no rule in force names it there.
- `bin/test` absent from the crafter and proofer definitions, and from the
  README's cheat sheet, were removed. Their docstrings give reasons, and no
  rule in force names the literal (executed, `git grep` over `docs/`,
  `agents/`, `skills/` and `CONTRIBUTING.md`).
- `/Users/` absent from the update skill's step 2b was removed.
  `CONTRIBUTING.md` *House rules* allows `/Users/x/`, so the rule does not
  forbid the literal, and the `real_identifiers` census holds the rule.
- The legend of the twin's letters in `seal_stamp.py`'s docstring
  (`` `e` its outer edge's dark `` and the rest) was removed. The letters
  stand in the module's `KEY`, and the sentence around them is wording.
- `` `seal-mark.txt` `` in the same docstring was kept, cut to the path a
  person opens to change the disc's mark.
- `unverified_check.py` and `reader.readable(` in `chain_check.py`'s
  source were kept. They are the path the check loads the one reader from
  and the call into it, and the comment cites `skills/core/SKILL.md` *The
  rule a mechanism is kept against*: a fact has one source.
- `**2b.` in the update skill was kept as the step's bold number the slice
  opens at, which the session follows.
- `seven` in the refusal record's rule was kept as the matcher's floor, a
  number a writer of a commit's row acts on.
- `NOT for:` in `writing-style`'s frontmatter was kept as the label the
  model reads for the skill's boundary.
- The equality asserts on `broad_gate.py`'s message constants
  (`NO_RECORD_AT_HEAD` and the rest) were left unchanged. They pin what the
  gate prints, a program's output under contract rule 14.

**One check line under `docs/` may have lost this module's reader (design
*Scope* item 9).** `docs/running/the-broad-gate.md:33`, under **What the
run prints says only whether it passed, and it draws nothing.**, names
`tests/skills/test_broad_gate.py` and
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`. The asserts
in the second module that read the run's printed rows, in
`broad_gate.py`'s docstring, were removed as wording. No case left there
reads the rule's stdout opening or its drawing nothing (read). `:97` reads
the `gate` row rule of `:112-121`, whose check line names
`tests/skills/test_broad_gate.py` alone, and `:204` reads
`skills/verify/orchestration.md`. The phase edits no file under `docs/`.
The framer folds the line after phase 4, keeping `tests/skills/test_broad_gate.py`.

The other check lines naming a module of group C keep a case that reads
their rule (read). They are `docs/checks/the-routing-check.md:18`,
`docs/releasing/release-checklist.md:241` and `:344`,
`docs/running/the-broad-gate.md:130` and `:139`, and
`docs/running/the-run.md:12`. No check line under `RULE_FILES` outside
`docs/` names a module of group C (executed, `git grep`). No check line
changed.

**A comment outside group C cited a removed case, and was rewritten (design
*Scope* item 7).**
`tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py:57`
said the suite module holds the crafter's definition to naming no runner.
That case went, so the comment now says why the pattern names none.

**Two statements outside the range were stale before this phase and are
not its edits.**
`tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:12`
and `:260` say the sealer module holds the gate's executed half, which
#942 moved to `tests/skills/test_broad_gate.py`. `skills/verify/scripts/broad_gate.py:612`
says one assertion in the sealer module moved for the ref's resolution.
Neither names a unit this phase removed.

**What was run, and what each run showed.**

- S1: executed, as above. The ledger and the three listings are in the
  phase's scratch directory.
- S4: `bin/seal rules --check` exits 0, "all 178 check lines in 69 rule
  files hold." (executed at `e2fc0cb74`).
- S5: `git grep -n -w <name> -- . ':!seal/threads' ':!.test_durations'`
  over each removed case and each old case name lists nothing at
  `e2fc0cb74` (executed). The same search finds the new name
  `test_the_entry_skill_stays_gone` at its definition, so it can find a
  name that is present (executed). No `path#unit` citation names a removed
  unit (executed, `git grep` on each module's `#`).
- S9: the six edited modules gave 105 passed before `e2fc0cb74` was
  committed, over the same bytes (executed). The boundary set,
  `bin/test tests/text tests/behaviour -q`, gave 1819 passed and 8
  skipped at `e2fc0cb74` with this record, `gaps.md` and the Status cell
  in the tree (executed). `tests/text/` and
  `tests/behaviour/` are the tree-wide files and hold every module that
  reads an edited one, `test_a_shrunken_corpus_declines_to_judge.py` and
  `test_every_tracked_file_meets_every_census.py` among them. No module
  outside them imports from an edited module (executed, `git grep`).
- Mutation: `seal mutate` ran over seven kept literals, each in the file
  it pins and with its case. All seven went red, each on the assert that
  names the literal (executed, failing line read). They were the hook
  command shape in `CONTRIBUTING.md`, `` `AgenticSeal core from` `` in the
  review skill, `seal stamp --from` planted in the sealer's *Never* bullet,
  `skills/agent-contract/SKILL.md` in `bin/test`, `` `suite-at-base.txt` ``
  in the **New?** bullet, `` `sealed_before` `` in the stamp policy, and
  `rsync` in the update skill's step 2b. An eighth run, over the first of
  the two `` `BROAD GATE FAILED` `` in the orchestration section, SURVIVED,
  because the cut assert holds on the second. That is the third failure
  scenario of `frame/plan.md` *Technical context*, measured. The tree was
  clean after each restore (executed, `git status --short`).
- S2 and S3 are the proofer's at review.

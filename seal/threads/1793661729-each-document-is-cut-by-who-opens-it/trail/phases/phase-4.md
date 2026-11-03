# Phase 4: 1793661729-each-document-is-cut-by-who-opens-it

## What this phase found

**The frame holds for this phase.** It was read against the tree at
b29c630cc before the first edit (read). `skills/implement/SKILL.md` held
each passage D5's second row names, starting and ending at the sentences it
quotes: the batch from "Collect what needs a person before the first edit"
through "spends more." in *1.*, the ladder from "When a work item is
required" through "not a way out." in *3.*, and *6.* whole.
`skills/verify/SKILL.md` held the two `####` sections D5's third row names.

**What moved where.** `skills/implement/orchestration.md` holds three new
sections, moved in 7927ac736:

- *Orchestrator: what needs a person is asked in one batch, before the first
  edit*: the batch. It stands before *Orchestrator: how the work is routed*,
  which opens by naming it.
- *Orchestrator: when a work item is required*: the ladder, after the
  routing section.
- *Orchestrator: drain the rows before the broad run, and keep the records*:
  *6.*, after the ladder.

`skills/verify/seal-arms.md` and `skills/verify/seal-mutate.md` each hold one
section, moved in 362f8777f. Each opens with a title in the shape of
`skills/settle/draft.md` and one sentence naming who opens it and at which
step. `skills/implement/SKILL.md` names `orchestration.md` at the step each
passage left: a closing paragraph of *1.*, the opening paragraph of *3.*, and
the last paragraph of *5.*. `skills/verify/SKILL.md` names both files under
condition 2, in a new subsection *A module or a unit: `seal arms` and `seal
mutate`*. The moved sections stood under condition 2, and a sentence there
would have joined the subsection above it, so the pointer takes a heading.

**A decision: the three headings carry the `Orchestrator:` marker.** D5
names the passages and not their headings. `skills/implement/acts.md`
*Orchestrator: which of these acts runs itself* says every act addressed to
the orchestrator sits under a marked heading. D5's *Read by* cell calls the
batch, the ladder and the drain the orchestrator's acts. So each heading
carries the marker, and `acts.md` gained a row for each in 7927ac736:

- The batch: `check: hooks/question-gate.py`. On a branch answered
  `Automation` `yes`, the gate refuses a question asked after the routing
  answer. The grounds name what it does not reach.
- The ladder and the drain: `still a sentence`. Nothing reads the rung. For
  the drain, `chain_check.py` reaches only its timing, through
  `trail/gate.md` at HEAD.

Judged against `acts.md`'s rule and its four values.

**A decision: two sentences left in `SKILL.md` that named a moved passage
now carry its path.** These are the questions paragraph of *3.* ("not on that
ladder", "the batch ... (step 1)") and *4.*'s "the ladder's second rung".
*3.*'s "Below the ladder's top rung" keeps no path, since *3.*'s opening
paragraph now names the ladder's file. In `orchestration.md`, the routing
section's two citations of `SKILL.md` *1.* and *3.* now name the new
sections by heading with "above" and "below". That is the form the file
already uses for its own sections. Judged against D7's last bullet, which
phase 3 applied the same way.

**A departure: the two verify sections are `##` in their new files, not
`####`.** Each new file opens with a `#` title, and a `####` under it would
skip two levels. The heading's text is unchanged. No citation names either
section (the scan below, executed at b29c630cc), and the one case that finds the `seal
mutate` section, `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py`,
now finds it by `## `. Judged against D5's "the two `####` sections of those
names", read as which sections move and not at which level.

**A departure: one cross-reference in moved text changed.** At the end of
the `seal mutate` section, "`seal arms` above is the command" now reads
"`seal arms` (`skills/verify/seal-arms.md`) is the command", since that
section is no longer above. Judged against D7's last bullet.

**The core's citation of *1.*, and the rest.** `skills/core/SKILL.md` cited
*1.* twice. The citation at *A judgment stands on a source document* names
the precedence order, which stays in *1.*, so it stands. The citation at
*Asking a person is the most expensive step* names the batch, and it now
names *Orchestrator: what needs a person is asked in one batch, before the
first edit*. Phase 6 removes the sentence after it (D2 item 1), and this
phase leaves that sentence as it stood.

**The old citations, as D7 asks (executed).** A read-only `python3` script
read every file `git ls-files -z` lists outside `seal/threads/`, each file
whole, so a citation wrapped across lines matches. It matched this pattern:

```
implement/SKILL\.md`(?:'s)?\s+\*6\.\s+Drain
|verify/SKILL\.md`(?:'s)?\s+\*`seal\s+(?:arms|mutate)`
|verify/SKILL\.md`\s+carries\s+the\s+verdicts
|implement/SKILL\.md`(?:'s)?\s+\*(?:1\.|3\.)[^*]*\*
```

At b29c630cc, run in a temporary worktree since removed, it listed 16
hits. At 362f8777f it lists 5, exit 0:

```
agents/framer.md:171: implement/SKILL.md` *3. The SDD file set*
docs/the-record-layout.md:327: implement/SKILL.md` *3. The SDD file set*
seal/follow-up.md:43: implement/SKILL.md` *3. The SDD file set*
skills/core/SKILL.md:69: implement/SKILL.md` *1. Read the documents that outrank the code first*
tests/text/test_a_question_says_who_can_answer_it.py:15: implement/SKILL.md` *3. The SDD file set*
```

Each of the five names text that stays in its section. `framer.md:171` and
the test name the three `Who can answer` values. `the-record-layout.md:327`
names the file-set table. `follow-up.md:43` names the Status cell, and
`core:69` names the precedence order. The pattern lists *1.* and *3.*
whole because those sections keep part of their text, so a hit is judged by
reading it. A citation that names a moved passage in other words, without
the path and the italic heading, is not in this list. The list is a sample
for that spelling (contract rule 12). The 11 re-pointed sites were
`CONTRIBUTING.md`, `agents/crafter.md`, `agents/framer.md:22`,
`hooks/mode-gate.py`, `seal/README.md`, `skills/code-review/orchestration.md`,
the core's second citation, two in `skills/implement/orchestration.md`,
`templates/setup/seal-README.md` and a comment in
`tests/behaviour/test_chain_hooks_hardening.py`. `seal/README.md` is the
repository's copy of `templates/setup/seal-README.md`, and
`test_first_setup_asks_once.py` holds the two identical.

**The readers of the moved text, re-pointed (executed).** The first narrow
run after the move had 12 failures. Each was a case reading the moved text
at its old path, or a line past the wrap limit, so each reader was seen red
before it was re-pointed:

- `test_the_set_a_work_item_always_has.py`: three cases read the ladder.
  They now read `orchestration.md`. The file-count sweep now reads
  `orchestration.md` as well as `SKILL.md`. Its allow-list moves the ladder's
  three lines to that file's key, and adds one line that already stood
  there, "into its three files", which names the framer's three frame files.
- `test_waiver_decided_at_start.py`: `seal no-work-item` now is read in
  `orchestration.md`. The absence of `[no-review]` is read in both files.
- `test_question_gate.py`: the gate's name is read inside the batch section.
- `test_the_rules_claude_md_names_have_one_home.py`: the batch's home is the
  new section. `test_a_section_stops_at_its_sibling` names *1.*'s heading
  itself, so it still holds *1.* apart from *2.*.
- `test_first_setup_asks_once.py`: the drain's heading and citation.

One case was green for the wrong reason, so it never went red.
`test_the_skill_names_where_a_late_finding_goes` read `SKILL.md` for
`questions.md`, `seal/follow-up.md` and `Not done`. All three stand
elsewhere in `SKILL.md`, so it passed after the paragraph left. It now reads
`orchestration.md`. That file names `seal/follow-up.md` in the drain as
well, so the case still reads the file whole, as it did before.
`test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py` was
re-pointed to `seal-mutate.md` before a run, and the mutations below show
it watches that file.

No reader that globs a skill's files needed widening. Phase 3 widened
`.github/scripts/rules.py#RULE_FILES` and the emoji census to
`skills/*/*.md`. The cited-section case reads every tracked file.
`test_a_document_that_names_a_script_says_how_to_reach_it.py` globs
`skills/**/*.md`, and its case id moved from `skills/verify/SKILL.md` to
`skills/verify/seal-mutate.md`, so the key in `.test_durations` moved with
it. `tests/behaviour/test_docs_line_wrap.py#COVERED` does not hold
`skills/verify/SKILL.md`, so the two new files are not added. Their text is
the same hand-wrapped text the old file held.

**The moved text against its old text (executed).** A read-only `bash`
script cut each section out of `git show b29c630cc:<file>` and out of its
new file with `awk`, from its first line to the next heading, and ran
`diff`:

```
=== batch
diff exit 0
=== ladder
diff exit 0
=== drain
18a19
>
diff exit 1
=== seal arms
1c1
< #### `seal arms` asks condition 2 of a whole module, one arm at a time
---
> ## `seal arms` asks condition 2 of a whole module, one arm at a time
78d77
<
diff exit 1
=== seal mutate
1c1
< #### `seal mutate` asks condition 2 of one unit, one break at a time
---
> ## `seal mutate` asks condition 2 of one unit, one break at a time
109,110c109
< `seal arms` above is the command.
<
---
> `seal arms` (`skills/verify/seal-arms.md`) is the command.
diff exit 1
```

The drain gained the blank line before the next heading, since it ended the
old file. The two verify sections lost the blank line that ended them,
since each now ends its file. Each other difference is a decision above.

**Bytes (executed, `wc -c -l`).**

| File | b29c630cc | 362f8777f |
|---|---|---|
| `skills/implement/SKILL.md` | 31,149 bytes, 496 lines | 25,103 bytes, 403 lines |
| `skills/implement/orchestration.md` | 23,653, 385 | 30,937, 503 |
| `skills/implement/acts.md` | 13,018, 76 | 14,740, 79 |
| `skills/verify/SKILL.md` | 25,263, 487 | 15,098, 308 |
| `skills/verify/seal-arms.md` | absent | 4,465, 84 |
| `skills/verify/seal-mutate.md` | absent | 6,739, 117 |

A crafter that reads `skills/implement/SKILL.md` whole reads 6,046 bytes
fewer at each spawn. A party that opens `skills/verify/SKILL.md` for the
labels or the scope rule reads 10,165 fewer, and one that runs `seal mutate`
opens 6,739 bytes beside it.

**S4 (read).** `skills/implement/SKILL.md` at 362f8777f holds neither the
batch, the ladder nor the drain. It holds one paragraph at each of the three
places, which names the orchestrator and the section. `orchestration.md`
holds the three under the headings above.

**Mutation (executed),** each `bin/seal mutate <file> --replace … --tests
"bin/test -q -p no:xdist <module> -k <cases>"`, one call per mutant:

| Unit | Mutation | Verdict |
|---|---|---|
| the ladder's citation of the count's issue | `(issue #35)` to `(issue #36)` | red: `test_the_rung_cites_the_issue_that_measured_the_count` |
| the sweep over `orchestration.md` | the ladder's last row to "two files" | red: `test_the_top_rung_names_behaviour_rather_than_a_count` |
| the batch's heading | shortened | red: the cited-section case, the acts case, `test_each_home_states_its_rule_under_its_section`, `test_the_prose_points_to_the_gate…` |
| the drain's heading | shortened | red: the cited-section case, the acts case, `test_the_seal_readme_points_at_the_drain…` |
| the ladder's heading | renamed | red: the cited-section case (`agents/framer.md:22` dangles), the acts case |
| the gate's name in the batch | `hooks/question-gate.py` to "a gate" | red: `test_the_prose_points_to_the_gate…` |
| the bound in `seal-mutate.md` | `300` to `30` | red: both bound cases in the mutation test module |
| an `acts.md` row | its act renamed | red: `test_every_orchestrator_act_names_its_delivery` |
| the `seal mutate` heading's text after the command name | "condition 2" to "condition two" | SURVIVED |

The survivor is not a defect. The case finds the section by its opening,
"## `seal mutate`", and no citation names the heading. No case read the
`seal arms` section at b29c630cc, and none reads it now: `git grep` over
`tests/` for `900 seconds`, `seal-arms` and `arms.*SKILL` lists none of
them (executed).

**Narrow runs (executed).** The phase-boundary set is the test modules that
name, import or walk a path this phase changed. One `git grep -l -E` over
`tests/*.py` and `tests/**/*.py` listed them, with the changed files' names,
`ls-files`, `os.walk`, `rglob`, `glob(`, `RULE_FILES`, `"agents"` and
`"skills"` as the pattern: 120 modules. At 362f8777f, `bin/test -q` over the
120 gave 5176 passed, 14 skipped and 1 failed, exit 1.

The failure is `tests/skills/test_test_layout.py::Test_main::test_accepts_this_repositorys_tests`.
`seal layout --check tests` refuses `tests/github/test_release_report.py`:
class `Test_documents` has no `test_accepts_` case and no `test_refuses_`
case. The same command at b29c630cc, run in a temporary worktree since
removed, gives the same two refusals with exit 1. The class came in at
fd331c80b, phase 2 of this work item. This phase changed neither file, and
the defect is phase 2's, so it is handed back and not fixed here.

`uvx ruff check` and `uvx ruff format --check` over each changed Python file
passed before its commit.

**For the next phases.**

- `agents/crafter.md` and `agents/framer.md` changed in this phase. As phase
  3 noted, the changelog ends with `### Process changes`.
- Phase 6 removes the core's sentence on the routing question (D2 item 1).
  It stands right after the citation this phase re-pointed.
- Phase 5 re-points `docs/` paths. The moved batch text carries a citation
  of `docs/the-review-record.md` *The run*, which now stands in
  `skills/implement/orchestration.md` *Orchestrator: what needs a person is
  asked in one batch, before the first edit*.

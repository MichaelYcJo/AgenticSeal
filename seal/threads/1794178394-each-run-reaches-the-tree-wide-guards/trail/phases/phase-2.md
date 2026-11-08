# Phase 2: 1794178394-each-run-reaches-the-tree-wide-guards

## What this phase found

**The frame holds for this phase.** Every coordinate the phase 2 row
stands on was where the frame says at `60be65db`: the two rows of
`skills/verify/SKILL.md` *Scope: cheap and often, broad and once*, step 9
of `agents/crafter.md`, and the contributor's line of `CONTRIBUTING.md`
*What a contribution is asked for*. `git grep -n -F 'what the fix touches'`
found the phrase only in `skills/verify/SKILL.md` outside `seal/threads/`.
One word of *Scope* item 3 needed the judgment phase 1 handed on, below.
The commit that rewrote the two rows is `49dbc59b`, and it also carries
the clause of *Scope* item 2 that phase 1 deferred.

### The third part reads a path; it does not only write its name

Phase 1 left open whether the row's third part means a test file that
names a changed path in full, as the frame's *Scope* item 3 words it, or
one that reads it. This phase judged it as reading. The row now says "each
test file that reads a path the phase changed", and the paragraph under
the table says what reading is: the file's cases open the path, import it
or load it, directly or through another test file. A file that writes the
path's name only into a fixture, a parameter or a docstring does not read
it.

The grounds are three. First, `skills/verify/SKILL.md` *The narrow command
still has to be able to fail* picks the command by what can fail, and a
file that writes a name into a fixture parses nothing the change wrote.
`tests/skills/test_chain_check.py` writes `seal/threads` into fixture
repositories and costs 408.1 s of stored price, and its result cannot move
with a work item's records (`frame/design.md` *Grounding*, the
`.test_durations` row). Second, naming in full misses a file that loads
the path by another spelling. For #1421's change, `tests/evals/test_rule_cases.py`
loads the script as `load_script("noninferiority")` and never writes
`evals/scripts/noninferiority.py`. `tests/evals/test_seed_defects.py`
imports `truth_regex` from it, which calls `ni.grader_from`. Both read the
changed script, and a search for its full path finds neither. Third, the
core's first value gives the meaning question to judgment and keeps it out
of a grammar rule (`skills/core/SKILL.md` *The first value: efficient
development through the workflow*). Which file reads a path is such a
question, and the frame's own rejected alternative of a `--changed` option
rejects encoding it (`frame/plan.md` *Alternatives considered*).

The judgment pulls a file that reads a single shipped document through
this part, whatever file it stands in. `tests/skills/test_chain_check.py`
reads `agents/proofer.md` and `skills/code-review/SKILL.md` under `ROOT`
in `test_the_proofer_and_the_review_skill_name_every_line_a_finding_needs`,
so a phase that changes either runs it. That case reads named files, not
the tree, so it is not tree-wide by the design's definition, and phase 1's
enumeration rightly left it in place.

This departs from the wording of three frame statements, which the
hand-back names for the orchestrator: `frame/design.md` *Scope* item 3
("names a changed path in full, imports it or loads it"), its *Data &
interfaces* ("files naming, importing or loading a changed path"), and
the first scenario's Then cell ("the files that name either path in
full"). The same holds for `frame/plan.md` *Alternatives considered*, the
chosen row ("narrowed to naming a changed path in full, importing it or
loading it").

### Other decisions in the rewritten text

- **The `Review rounds 1..n` row's label moves from `executed`, narrow, to
  `executed`, scoped.** The row now runs the `Phase boundary` set, whose
  label is `scoped`. The frame does not name the label. The ground is
  the table's own column: one set carries one label.
- **The fourth part's fallback is a sentence under the table, not a clause
  of the row.** It reads: where the guide names none, the tree-wide files
  are the test files that glob the directory holding a changed path. This
  is *Scope* item 3's fallback in the frame's words. The row stays one
  line of four parts.
- **Step 9 runs the set once the fixes are committed and before the close
  blocks.** The frame asks for the run before the close block is written
  (*Scope* item 5). `agents/crafter.md` *A fix pass appends close blocks
  and writes no phase record* already orders the reading after the fix
  commit and the close blocks last. So the step says both, in that order.
- **`CONTRIBUTING.md` *What a contribution is asked for* names the two
  directories as "the tree-wide files *The test layout* names".** That
  cites the paragraph that defines them, so the set has one source.

### `CONTRIBUTING.md` *The test layout*, the helper sentence

The sentence read "A helper two test files use is defined once, in
`tests/conftest.py`". The tree does otherwise. A `git grep -l -P
'^[ \t]*(from test_\w+ import|import test_\w+)' -- tests` lists 28 test
files at `49dbc59b` that import a helper from another test file, across
`tests/behaviour/`, `tests/text/`, `tests/evals/`, `tests/github/` and
`tests/lib/`. The same search at `94d04d30` lists 24, 14 of them under
`tests/behaviour/`. Phase 1's record counts fifteen under
`tests/behaviour/` and does not give its search, so this record gives the
counts its own search makes. The import works because `tests/conftest.py`
puts every directory under `tests/` on `sys.path` and no two files share
a name, which the next paragraph of *The test layout* states. The sentence
now reads "defined once, in `tests/conftest.py` or in one of the two
files, which the other imports by its name". "Defined once" is what the
rule protects, and the tree holds it either way. The ground is
`skills/core/SKILL.md` *The rule a mechanism is kept against*: a change
rewrites the text it amends in place.

### *Scope* item 7: the two sets timed (`frame/questions.md` Q2)

Both runs were executed on one tree, `49dbc59b`, on one machine with 12
cores, back to back, under `bin/test`'s default parallel run. Each was run
once. Other work items of the release run in their own worktrees on the
same machine, and this phase did not measure their load, so each figure is
one sample.

The first set is #1421's. It is regenerated by `git grep -l -F <term>
v0.34.1 -- tests/` for each of the 14 terms the *Grounding* row on the
#1421 phase record lists. The union is 70 paths. Two are not test files,
`tests/censuses.py` and `tests/conftest.py`, so 68 test files remain,
which matches the #1421 record's count. Each of the 68 exists at
`49dbc59b`.

- Command: `xargs bin/test -q < <the 68 paths>`.
- 68 files, 4,393 passed and 10 skipped, exit 0.
- Wall clock: 70.14 s as pytest reports it, 71 s between `date +%s` taken
  before and after the command.

The second set is the new row's set for #1421's changed paths:
`evals/scripts/noninferiority.py`, `tests/evals/test_noninferiority.py`,
`.claude-plugin/plugin.json` and the work item's records.

1. The cases the plan row names: #1421's row named its test file, which is
   part 2.
2. The test files the change touched: `tests/evals/test_noninferiority.py`.
3. The test files that read a changed path: `tests/evals/test_rule_cases.py`
   and `tests/evals/test_seed_defects.py`, by the reading above. Outside
   the two directories, no test file reads this repository's own
   `.claude-plugin/plugin.json`. `tests/github/test_plugin_directory_check.py`,
   `tests/github/test_release_seal.py`, `tests/github/test_tag_release.py`,
   `tests/github/test_roll_flow_measurement_issue.py`,
   `tests/github/test_release_completeness_check.py`,
   `tests/skills/test_broad_gate.py`, `tests/skills/test_pr_body.py`,
   `tests/skills/test_seal.py`, `tests/skills/test_payload_meter.py`,
   `tests/lib/test_core.py` and `tests/hooks/test_core_start.py` write a
   manifest of that name into a fixture, or name it in a message, and were
   left out. The records paths pull no file.
4. `tests/text/` (35 files) and `tests/behaviour/` (52 files).

- Command: `bin/test tests/text tests/behaviour
  tests/evals/test_noninferiority.py tests/evals/test_rule_cases.py
  tests/evals/test_seed_defects.py -q`, typed as `xargs bin/test -q <`
  over those five paths.
- 90 files, 2,119 passed and 9 skipped, exit 0.
- Wall clock: 17.73 s as pytest reports it, 17 s between `date +%s` taken
  before and after the command, which counts whole seconds.

The new set ran 90 files against 68 and finished in about a quarter of
the time. 38 of the first set's 68 files stand in `tests/text/` or
`tests/behaviour/`, so the second set holds all of those. The first set
holds none of the five files phase 1 wrote, which postdate its list, so
it does not run the 14 cases phase 1 moved. The *Grounding*
row on `.test_durations` reads the same comparison as stored price:
1,488.5 s against 143.1 s, plus 36.3 s for the moved cases.

### The phase boundary

The set for this phase's paths, `skills/verify/SKILL.md`,
`agents/crafter.md`, `CONTRIBUTING.md` and the work item's records:

1. The plan row names no case.
2. The phase changed no test file.
3. No test file outside the two directories reads any of the three
   documents. `git grep` for each path, and for `"crafter.md"`,
   `"CONTRIBUTING.md"` and `"agents"` as path parts, lists the files that
   name one outside the two directories. Each match was read at its line.
   `tests/skills/test_passages.py` passes `agents/crafter.md` and
   `CONTRIBUTING.md` to `passages.in_corpus` as strings and opens neither.
   `tests/github/test_release_report.py` writes a `CONTRIBUTING.md` into a
   fixture. The others name a path in a docstring or a comment:
   `tests/skills/test_mutation_check.py`, `tests/skills/test_payload_meter.py`,
   `tests/skills/test_session_cost.py`,
   `tests/github/test_roll_flow_measurement_issue.py`,
   `tests/github/test_plugin_directory_check.py`,
   `tests/github/test_run_tests.py`, `tests/lib/test_launch.py`,
   `tests/skills/test_chain_check.py`, `tests/test_conftest.py`,
   `tests/censuses.py` and `tests/conftest.py`.
4. `tests/text/` and `tests/behaviour/`.

The command was `bin/test tests/text tests/behaviour -q`, at `49dbc59b`
with this record, `gaps.md`, `changelog.md` and the Status cell on disk.
It exited 0 in 9 s of wall clock: 1,809 passed, 9 skipped (executed).

### No case written new, and no mutation run

The phase changes prose an agent reads, and adds no code. The frame
verifies it by reading the rows and step 9, the `git grep` above, and the
two timed runs (`frame/plan.md` *Phases*, the phase 2 row, and
`frame/design.md` *User scenarios & acceptance*). The *Prose only* row of
`skills/verify/SKILL.md` *The narrow command still has to be able to
fail* applies: what can fail is whatever parses the files, which the
tree-wide files do. So no case is written new and no `seal mutate` run is
owed.

### The other statements of the reworded rules

`git grep -n -F 'what the fix touches'` returns nothing outside
`seal/threads/` at `49dbc59b`. The glob clause stands only as the
fallback sentence. A `git grep -n -i -E` for `phase boundar`, `cheap and
often`, `narrow` and `fix touches` over `README.md`, `README.ko.md`,
`docs/`, `templates/`, `skills/`, `agents/` and `evals/` found three
other statements on narrow runs: `CONTRIBUTING.md` *Running the checks*
("narrow runs while the work is still being edited"),
`docs/running/the-broad-gate.md`'s opening ("Narrow and often, broad
once"), and `skills/verify/orchestration.md` *The broad gate*, which cites
the section for why nothing broad runs before the rounds. None states
which files a narrow run holds, so each stands. This is a sample of the
statements across the tree. A statement that describes the old set in
other words is the part it did not reach.

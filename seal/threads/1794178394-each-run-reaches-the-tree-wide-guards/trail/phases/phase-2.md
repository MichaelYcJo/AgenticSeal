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
- **A work item's records reach the set through the tree-wide files, not
  through the reading part.** `49dbc59b` said a records path pulls no file
  through the reading part, as the frame's *Scope* item 3 says. Under the
  reading judged above that is false: a file that walks the records
  directory reads them. `4e5dc4af` rewrites the sentence: no test file
  names a new work item's records by their path, so only a file that walks
  the records directory reads them, and that file is tree-wide.
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

Both runs were executed on one machine with 12 cores, under `bin/test`'s
default parallel run, and each was run once. The first ran at `49dbc59b`.
The second ran at `69f00945`, in the fix pass of round 1, because the set
phase 2 first timed left out seven files (below). Other work items of the
release run in their own worktrees on the same machine. This phase did not
measure their load at the first run; at the second, `uptime` gave a
one-minute load average of 9.07 before the run and 13.55 after it. So
each figure is one sample under a load that varies, as the two boundary
runs below show.

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
3. The test files that read a changed path. `tests/evals/test_rule_cases.py`
   and `tests/evals/test_seed_defects.py` read
   `evals/scripts/noninferiority.py`, by the reading above. Seven test
   files outside the two directories read this repository's own
   `.claude-plugin/plugin.json`:
   - `tests/github/test_plugin_directory_check.py`: `main` and
     `plugin_name` over `ROOT`.
   - `tests/github/test_release_seal.py`: `draw` with the module's `ROOT`
     set back to the repository.
   - `tests/skills/test_broad_gate.py`: nine cases run the gate from the
     tree, and `plugin_version` reads the running copy's manifest for the
     line naming which copy ran.
   - `tests/skills/test_pr_body.py`:
     `Test_seal_mark::test_accepts_the_plugins_own_manifest`.
   - `tests/skills/test_seal.py`: 24 cases of `Test_pr_checks`,
     `Test_switch`, `Test_install_workflow`, `Test_remove_workflow` and
     `Test_workflow_at`, which read the plugin's version for the workflow's
     pin.
   - `tests/lib/test_core.py`: `core.rendered` reads the version into the
     header.
   - `tests/hooks/test_core_start.py`: the hook run with the plugin root at
     `ROOT`, and `printed` over `ROOT`.

   Four files write a manifest of that name into a fixture, or name it in
   a message, and were left out. `tests/github/test_tag_release.py` sets
   the module's `ROOT` to a fixture repository in every case that reaches
   `version_at`. `tests/github/test_roll_flow_measurement_issue.py` and
   `tests/skills/test_payload_meter.py` build the manifest under
   `tmp_path`. `tests/github/test_release_completeness_check.py` names it
   in an error message. The records paths pull no file through this part:
   the files that read a work item's records walk the records directory,
   and by phase 1's enumeration every such file stands in `tests/text/` or
   `tests/behaviour/`.
4. `tests/text/` (35 files) and `tests/behaviour/` (52 files).

Phase 2 first set these seven aside too, after reading each
`git grep` match by eye. Round 1's finding 1 named four of them. The fix
pass re-read the eleven files that list held, a closed set, by two
methods. The first was executed: a probe ran the eleven files once with a
`sitecustomize` audit hook on `PYTHONPATH`. The hook logged each open of
the real `.claude-plugin/plugin.json` from every Python process that
inherits the variable, with the case `PYTEST_CURRENT_TEST` named. It
logged the seven files above and none of the other four. The second was
read: a process that does not inherit `PYTHONPATH`, and a reader that is
not Python, such as `git show`, escape the hook. So each of the four left
out was read at the calls that reach a manifest, `test_tag_release.py`'s
`git show` under the module's `ROOT` among them.

- Command: `bin/test tests/text tests/behaviour
  tests/evals/test_noninferiority.py tests/evals/test_rule_cases.py
  tests/evals/test_seed_defects.py tests/github/test_plugin_directory_check.py
  tests/github/test_release_seal.py tests/skills/test_broad_gate.py
  tests/skills/test_pr_body.py tests/skills/test_seal.py
  tests/lib/test_core.py tests/hooks/test_core_start.py -q`.
- 97 files, 2,995 passed and 10 skipped, exit 0.
- Wall clock: 24.84 s as pytest reports it, 25 s between `date +%s` taken
  before and after the command, which counts whole seconds.
- The same command first ran at `abde6b8c` and exited 1 in 21.47 s:
  `tests/behaviour/test_docs_line_wrap.py` refused a 117-column line the
  fix pass had written into `CONTRIBUTING.md`. `69f00945` wraps it.

The set phase 2 first timed, without the seven, was 90 files, 2,119
passed and 9 skipped, exit 0, in 17.73 s at `49dbc59b`. It is not the set
the row names for #1421's change.

The new set ran 97 files against 68 and finished in about a third of
the time. 38 of the first set's 68 files stand in `tests/text/` or
`tests/behaviour/`, so the second set holds all of those. The first set
holds none of the five files phase 1 wrote, which postdate its list, so
it does not run the 14 cases phase 1 moved. The *Grounding* row on
`.test_durations` reads the comparison as stored price, 1,488.5 s
against 143.1 s, plus 36.3 s for the moved cases. Its 143.1 s holds none
of the seven manifest readers. Their stored price in the same file is
300.8 s, of which `tests/github/test_release_seal.py` is 98.7 s and
`tests/skills/test_seal.py` 91.0 s, and `tests/lib/test_core.py` and
`tests/hooks/test_core_start.py` have no stored price there. Summed by
file over the 97, `.test_durations` gives 514.6 s, and the moved cases
add their 36.3 s under their old ids, so the row's set for #1421's change
is about 551 s of stored price against 1,488.5 s (executed, a sum over
`.test_durations` by file).

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
   In round 1's fix pass, the audit-hook probe of *Scope* item 7 ran the
   eleven test files of this list once, with the three documents as its
   targets: 786 passed, exit 0, and it logged no open of any of the three
   (executed). `tests/censuses.py` and `tests/conftest.py` are not test
   files, and every run imports them. The probe's limit is the one
   *Scope* item 7 names: a process that does not inherit `PYTHONPATH`, or
   a reader that is not Python, escapes it.
4. `tests/text/` and `tests/behaviour/`.

The command was `bin/test tests/text tests/behaviour -q`. It ran twice,
each time with this record, `gaps.md`, `changelog.md` and the Status cell
on disk, and both runs are executed. At `49dbc59b` it exited 0 in 9 s of
wall clock: 1,809 passed, 9 skipped. At `4e5dc4af` it exited 0 with the
same counts in 75.08 s. Nothing in the set changed between the two
beyond one paragraph of `skills/verify/SKILL.md` and this record, so the
eightfold difference is the machine's load from the release's other
sessions, which this phase did not measure. The two timed runs of
*Scope* item 7 carry the same noise.

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

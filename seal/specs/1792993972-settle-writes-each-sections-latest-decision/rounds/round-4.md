# Review round 4: 1792993972-settle-writes-each-sections-latest-decision

target: 7b0ef4e7 against release/v0.22.4

Round 4 is the first round after the reframe. Round 3's one finding closed
`deferred the frame`, and the framer rewrote the frame at `21733772`. Phase 3,
a build phase, made `98e261ea` and `7b0ef4e7`. This round reads the phase 3
diff `d86b96f8..7b0ef4e7` against the reframed `spec.md`, `plan.md` and
`questions.md`, then the work item as a whole, `2974871d..7b0ef4e7`. Every
fact below was established this round in a `git clone --no-local` of the
repository at `7b0ef4e7`, except four carried from earlier rounds with their
coordinates and not re-derived, since phase 3 touches none of their files:
the dry run's counts over the real `origin/main` (S10, round 1's probe row
3), the rename rows counted against nothing at the old path
(`skills/verify/scripts/unverified_check.py:1597-1599`), the predicate not
letting a pull request escape a declaration of its own
(`skills/verify/scripts/unverified_check.py:1266-1279`), and round 3's
measure of step 6's old searched set (106 modules for one changed file).

## Findings

### 1. S13's case pins half of steps 6 and 8, and a revert of the failure path in step 8 leaves it green

severity: should
location: `tests/test_settle_reads_before_it_removes.py:92-126`, `skills/settle/SKILL.md:203-219`
evidence: executed `bin/mutation-check skills/settle/SKILL.md --tests "bin/test tests/test_settle_reads_before_it_removes.py tests/test_settle.py tests/test_no_passage_is_pasted_into_a_second_file.py -q -p no:xdist"`, `bin/mutation-check skills/settle/SKILL.md --tests "bin/test tests/test_settle_reads_before_it_removes.py tests/test_settle.py -q -p no:xdist"`, `git grep -n -e 'name each in the pull request body' -e 'run the row again' -e 'dry run again' -- tests/`
verdict: fixed 3ac7cddb

`spec.md` S13 says what the rewritten case verifies. For step 6, it is that
the step names each rule's `check:` targets and the dry run as what it runs.
For step 8, it is that the step "says how a failure on an old fact is changed
and named". The phase 3 row of `plan.md` lists the five new strings, and the
case holds exactly those five. None of them is in step 8's failure path or in
step 6's dry run. Two mutation runs removed one clause at a time from the
skill. Each `--replace` pair is a row of `## Probes`. All five mutants
survived:

- step 8 without "and name each in the pull request body";
- step 8 without "Run the failing modules until they pass, then run the row
  again.";
- step 8 without the sentence sending a corpus check to *Answer every check
  that reads the corpus*;
- step 6 without "and change what a failure shows still standing on the old
  fact";
- step 6 without "Then run the dry run again: a `to` not found is where you
  reworded, which the body explains."

The search found no module under `tests/` that pins any of those words.

The second mutant matters most. The reframe rests on step 8 having a path
after a failure. `plan.md` *Step 6 after round 3* says round 1's finding 5
"rested on step 8 having no path after a failure. Step 8 now has one". The
done condition, "passes with no edit after it", is pinned and implies a
second run. But the instruction that gives the path is not pinned, and a
later edit can drop it without a red case. The first mutant drops the
naming in the pull request body, which `spec.md` *In* item 3 and
`questions.md` A9 ask of every pin or copy the settle changes. The phase
record claims six mutants, all red (`phases/phase-3.md:50-55`). None of the
six it names removes one of the five clauses above, so that score does not
cover them.

The phase 3 claims that hold are a confirmation below. This finding is about
what the case leaves unpinned. Phase 3 is a build phase, so the finding
carries neither a `regression:` nor a `reopens:` line.

The case gains five strings in the order the skill holds them. A probe
holding every string below except the second was green at `7b0ef4e7`. It
was red against each of the naming, second-run and dry-run mutants
(executed). The second string was not probed:

```python
        "take a default and write it down",
        "Run each rule's `check:` targets over what you wrote",
        "and change what a failure shows still standing on the old fact",
        "Then run the dry run again",
        "The step is done when every `check:` target passes",
        "step 8 runs every one",
        "Run `settle --apply`.",
        "It is the one run that reads every check",
        "change that pin or copy, and name each in the pull request body",
        "then run the row again",
        "The step is done when the row passes with no edit after it",
        "Open the pull request.",
```

Where the corpus clause should be pinned too, the string
"answer it as *Answer every check that reads the corpus* says" goes between
"name each in the pull request body" and "then run the row again". The
`flattened` helper joins the wrapped lines, so each string matches as
written.

answer: The finding holds. The smith fixed it in 3ac7cddb: the case gains the five strings in the round's order (step 6's fix and second dry run, step 8's naming in the pull request body, its corpus answer and its second run), plus two clauses S13 names that the case also left unpinned, step 6's reason it does not search ("finds a module only by how it spells a path") and step 8's "Run the repository's `Broad gate` row.". `bin/mutation-check skills/settle/SKILL.md` over the case with seven `--replace` pairs, one per clause: baseline green, 7 mutants, 7 red, 0 survived; the four modules of the pass give 66 passed (executed by the smith).

## Confirmations

confirms: round-3#1
Round 3's defect is gone at its unit. Step 6 of `skills/settle/SKILL.md`
*The settling session's procedure* no longer names a searched set or claims
that a set holds every check reading a document (`skills/settle/SKILL.md:203-211`,
read). Instead it says it does not look for those checks and why, and it
names step 8 as the run that reads them all. The case asserts that the
procedure holds no `git grep`. With `27177bf2`'s skill text checked out in
the clone the case failed, naming all five new strings, and at `7b0ef4e7`
it passed (executed). Round 3's own example, a setext line written into a
policy document, now meets a rule that holds: step 6 promises nothing about
the heading module, and step 8 runs the row, changes the failure and runs
the row again. Round 3's finding closed `deferred the frame` and owes no
line. This entry records that the reframe closes the defect it named.

confirms: none
Steps 6 to 8 of the skill are S13's target text byte for byte: `diff` of
`spec.md` lines 182 to 198 against `skills/settle/SKILL.md` lines 203 to 219
exits 0 (executed). The smith claimed the changelog clause was rewritten as
the phase 3 row of `plan.md` gives it. It was, at `changelog.md:6` (read).
The smith also claimed `overview.md` states neither step and gains one
divergence row. The row keeps the docstring's half on round 1's row kinds,
which the case still asserts through "A row that fits more than one kind
takes the first that fits" (`tests/test_settle_reads_before_it_removes.py:112-113`,
read). The divergence holds.

confirms: none
The settle replay holds. In the clone, `Edit` applied all nine
`## Rule changes` operations to `docs/the-record-layout.md`,
`docs/release-checklist.md`, `docs/the-review-and-parity-arms.md` and
`docs/the-review-record.md`. Operations 2 and 3 replaced their paragraphs
with their check lines, as `1792628098`'s unsettled check-line changes
leave them. The dry run at `--released-at HEAD` then gave exit 0, and each
of this spec's nine operations printed `from not found, to found`. A
121-module probe set gave 4,822 passed, 14 skipped and one failure:
`tests/test_settle_reads_before_it_removes.py::test_the_documents_say_a_spec_less_directory_is_retired_by_the_rule`,
the spec-less pin `questions.md` A9 leaves red. The set is round 3's search
with `-e '*.md'` and the six changed file names, plus the settle, rule-change
and rules modules. Executed. The set is a probe and not the suite; the
`## Not judged` row below says why the full suite did not run. One
observation for the 0.22.4 settle: the failing module is the `check:`
target of the fold section's *A settle is not a work item* paragraph, which
operation 4 rewrites. So step 6 meets A9's pin before step 8 does, and
`plan.md` *Failure scenario*'s third case, a first broad run failing on
that pin, does not happen in this settle (read).

confirms: none
The modules phase 3 touches, and their neighbours, pass at `7b0ef4e7`: the
plan's *Verified by* command for phase 3 gave 66 passed, and
`tests/test_settle_reads_before_it_removes.py`, `tests/test_settle.py`,
`tests/test_rule_changes.py`, `tests/test_unverified_check.py` and
`tests/test_chain_check.py` gave 710 passed. `uvx ruff check` and
`uvx ruff format --check` over the changed test file report nothing, and
`bin/test-layout --pairs` over it names no pair. Phase 3 adds no case and
rewrites one, so no new test is read against a group. Executed.

confirms: none
The branch's `tests` run 40290437404 at `7b0ef4e7` completed `success` on
every leg, the four Windows groups and the `durations` job included (read,
`gh run view`). That run is the answer `overview.md` *Not verified* names
for its one row, the new and rewritten cases on Windows. The row stays open
in the record until the session that closes the work item writes the
closure.

confirms: none
The whole work item outside phase 3 holds where this round read it.
`settle.py#apply` takes its candidates from the working tree, not from the
dry run. It keeps a directory whose `overview.md` cannot be read, since
`unverified_check.py#open_record_rows` returns a row saying so. It prints
closed rows only from `overview.md`, the one file the open-row reader reads
(`skills/settle/scripts/settle.py:566-604`,
`skills/verify/scripts/unverified_check.py:1315-1341`, read).
`rule_changes.py#group` merges every pair of places `overlapping` joins, so
a place that two separate groups overlap joins them into one
(`skills/settle/scripts/rule_changes.py:305-339`, read). A search over the
tree outside the round records found no other file stating step 6's old set
or step 8's "once" for the settle. `README.md:55` says the broad gate runs
"ONCE", and it describes a work item's run, not a settle (executed, then
read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite over the replayed `docs/`. The spawn prompt asked this round to run it, and contract rule 2 and the warden's *The broad gate is not yours* refuse the full suite to every agent, so this round ran the 121-module probe set instead and declines the rest | the round's spawn prompt | the orchestrator, who asked for it |
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three; CI's `tests` run 40290437404 is green | `broad-gate.md` | the orchestrator, by `broad-gate` once the rounds settle |
| Whether the 0.22.4 settle runs the tree's `settle.py` and reads the tree's `skills/settle/SKILL.md`, since the installed 0.22.3 plugin holds the literal replay. Rounds 1 to 3 left this row, and phase 3 does not answer it | `plan.md` *Operational impact* | the orchestrator, at the release preparation |
| The pull request body's failure direction, prompt budget and removals, and the `Part of #1033` line of Q2's default | `CONTRIBUTING.md` *What a change to a gate must carry* | the orchestrator, when the body is written |
| Q1's default, one issue per distinct measurement, against how the owner wants the tracker to read | `questions.md` Q1 | the repository owner, at the settle's pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_settle_reads_before_it_removes.py -q -p no:xdist -k test_the_skill_states_the_settling_sessions_procedure` with `27177bf2`'s skill text, then with `7b0ef4e7`'s | 1 failed, naming the five new strings; then 1 passed |
| `bin/mutation-check skills/settle/SKILL.md` over the case's module, `tests/test_settle.py` and the passage check, four `--replace` pairs: step 8 without "and name each in the pull request body", without "Run the failing modules until they pass, then run the row again.", without the corpus sentence, and step 6 without "and change what a failure shows still standing on the old fact" | 4 mutants, 0 red, 4 survived |
| the same, the case's module and `tests/test_settle.py`, one mutant: step 6 without its dry run sentence | survived |
| a probe `tests/test_tmp_round4_pins.py` holding the proposed string list, run by `bin/mutation-check` against the naming, second-run and dry-run mutants | baseline green; 3 mutants, 3 red; the probe was then deleted |
| `diff` of `spec.md` lines 182 to 198 against `skills/settle/SKILL.md` lines 203 to 219 | exit 0 |
| the nine operations applied by `Edit` to the clone's four documents, then `python3 skills/settle/scripts/settle.py --released-at HEAD` | exit 0; the nine operations each `from not found, to found` |
| the same tree, `bin/test` over 121 modules: round 3's search with `-e '*.md'` and the six changed file names, plus `tests/test_settle*.py`, `tests/test_rule_changes.py` and `tests/test_rules.py` | 1 failed, 4,822 passed, 14 skipped: the spec-less pin A9 leaves red; the clone was removed afterwards |
| the plan's phase 3 *Verified by* command | 66 passed |
| `bin/test` over five touched and neighbouring modules | 710 passed |
| `bin/test-layout --pairs tests/test_settle_reads_before_it_removes.py`, `uvx ruff check` and `uvx ruff format --check` over it | 1 file read, 0 pairs; ruff exit 0 twice |
| `gh run view 40290437404` | completed, `success` on every leg |

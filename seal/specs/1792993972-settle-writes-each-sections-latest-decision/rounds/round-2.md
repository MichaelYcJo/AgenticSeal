# Review round 2: 1792993972-settle-writes-each-sections-latest-decision

target: 3903202c, fixes a82541df..3903202c

Round 2 verifies round 1's five closes and reads the fix diff
`a82541df..3903202c`: the orchestrator's ninth rule change (`423896f8`), the
fix pass `1caa3293`, `14a110e1` and `ffeadf29`, and the answers (`3903202c`).
Every fact below was established this round in a `git clone --no-local` of
the repository at `3903202c`, except three carried from round 1 with their
coordinates and not re-derived, since the fix diff touches none of their
files: the dry run's counts over the real `origin/main` (S10, round 1's
probe row 3), the rename rows being counted against nothing at the old path
(`skills/verify/scripts/unverified_check.py:1597-1599`), and the predicate
not letting a pull request escape a declaration of its own
(`skills/verify/scripts/unverified_check.py:1266-1279`).

## Findings

### 1. Step 6 names its set twice, and the command it gives misses modules that open a changed document by its parts

severity: should
location: `skills/settle/SKILL.md:203-212`, `tests/test_settle_reads_before_it_removes.py:113-115`, `seal/specs/1792993972-settle-writes-each-sections-latest-decision/changelog.md:6`
evidence: executed `git grep -l -F docs/ -- tests/`, `git grep -l -E '"docs"' -- tests/`, `git grep -l -e the-record-layout -e release-checklist -e the-review-and-parity-arms -e the-review-record -e README -e 'settle/SKILL' -e 'skills/settle' -- tests/`
verdict: fixed 72fc2c58
regression: round-1#5

Step 6 of `skills/settle/SKILL.md` *The settling session's procedure* is the
unit `ffeadf29` rewrote. `spec.md` *In* item 3 asks the settling session to
run the documents' checks over what it wrote, and `plan.md` *How a settle's
result is verified* lists them; the fix named that set as the modules
"whose text names the policy root's directory" and gave
`git grep -l -F docs/ -- tests/` as the command, so the defect came from
the command being narrower than the sentence it illustrates.

The sentence and its command are two readings of one set. A module that
opens a document as `os.path.join(ROOT, "docs", "release-checklist.md")`
names the policy root's directory in its text, and the command does not
find it. The command lists 95 modules. Three modules that open a document
this spec's rule changes rewrite are not among them:

- `tests/test_a_rider_reaches_its_file.py:84` reads
  `docs/the-review-record.md` and pins "`target:` names a commit, not a
  content anchor".
- `tests/test_review_axes.py:127` reads `docs/the-review-record.md`.
- `tests/test_unverified_rows_close.py:222` reads
  `docs/release-checklist.md`.

The same holds for a README copy the session changes. A module can read
`README.md` or `README.ko.md` by name without naming `docs/`, such as
`tests/test_the_root_migrates_itself.py:36-39`. In this round's replay all
of these modules passed, so the gap did not bite this spec's nine
operations. It bites the settle whose section one of them pins. A session
that takes the command as the set then finds that pin first at step 8,
which runs once. Round 1's finding 5 asked step 6 to close exactly that
path.

The other half of round 1's finding 5 holds. Step 4's sentence, "A row that
fits more than one kind takes the first that fits, in the table's order",
gives one reading, and its reason fits the table's order (moot, answered,
then a measurement), at `skills/settle/SKILL.md:193-195` (read).

The file names find what the directory misses. Each changed document, the
READMEs included, is named whole in every module that opens it, by any
spelling of the path.

```markdown
6. Run, over what you wrote, each rule's `check:` targets and every
   module under `tests/` whose text names the policy root's directory or
   the name of a file you changed. Where the root is `docs/`, the set is
   what `git grep -l -F -e docs/ -e <name> -- tests/` lists, with one
   `-e <name>` for each file you changed, such as
   `-e the-record-layout.md -e README.md`. The directory finds the checks
   that read every document rather than one by name, such as a
   line-length or a duplicated-passage check, which no `check:` line
   names. A file's name finds a module that opens that file by its parts,
   which the directory alone misses. Where a case fails because a pin
   under `tests/` or a copy such as a README row still states the old
   fact, change that pin or copy, and name each in the pull request body.
   Then run the dry run again: a `to` not found is where you reworded,
   which the body explains. The step is done when every one of those
   modules passes.
```

The pin keeps its two strings, since both stay true, and gains one for the
new clause, which a revert of the fix leaves red:

```python
        "module under `tests/` whose text names the policy root's directory or "
        "the name of a file you changed",
        "A file's name finds a module that opens that file by its parts",
```

The changelog fragment's bullet changes with it: "runs each rule's
`check:` targets and every test module naming the policy root's directory
or a file it changed over what it wrote".

answer: The finding holds, and as the first regression on this unit it took an ordinary fix pass. The smith fixed it in 72fc2c58: step 6 now names its set as every `tests/` module whose text holds the policy root's directory name as a word or the name of a file the session changed, and gives `git grep -l -w -F -e docs -e <name> -- tests/` with one `-e <name>` per changed file, which finds exactly that set. It takes the proposal's per-file names but matches the directory with `-w docs` rather than `docs/`, so a module joining a document's path from its parts is found by the directory itself, and the file names find the modules that open a file without it, such as a README reader. Over this spec's four documents and both READMEs the command lists 118 files, including `tests/test_a_rider_reaches_its_file.py`, `tests/test_review_axes.py`, `tests/test_unverified_rows_close.py` and `tests/test_the_root_migrates_itself.py`, and misses none of the modules naming README, `"docs"`, `docs/` or a changed document's name (executed by the smith). `test_the_skill_states_the_settling_sessions_procedure` pins the set, the command and the per-file clause, red against ffeadf29's text and green after, and the changelog fragment names a changed file beside the directory.

## Confirmations

confirms: round-1#1
`.test_durations` no longer turns the suite red. The case
`test_the_durations_file_prices_the_suite` passes over the whole collection
at `3903202c` (executed, round 1's command re-run). The branch's `tests`
run 40286070452 at `3903202c` completed `success` on every leg, the
`durations` job included (read, `gh run view`). The smith claimed the file
takes run 40282308738's entry set and keeps the old prices of the rest. The
artifact, downloaded this round, bears that out: the committed file holds
the artifact's 6,536 keys exactly, the 96 dropped entries are gone, the 133
added ones carry the artifact's prices, and the file is in the form
`.github/scripts/durations_union.py#rendered` writes. The other 6,403
entries keep the base's prices, so every one of them differs from the
artifact's (executed). The file is therefore not what the repository's
refresh produces. `CONTRIBUTING.md` *Running the checks* moves the artifact
over the file whole. That is no finding: `overview.md` *Not done* states it,
a stale price unbalances the shards and drops no case (`CONTRIBUTING.md`,
read), and the next refresh replaces the file whole. The `overview.md`
paragraph that called the file unmanaged is rewritten (read).

confirms: round-1#2
The two collisions are gone. In this round's clone, with all nine
`## Rule changes` operations applied by `Edit` to `docs/`, the 86 modules
that read a changed document, a README or the skill, together with the four
checks that read the whole root, gave 4,116 passed, 14 skipped and one
failure. The failure is
`tests/test_settle_reads_before_it_removes.py::test_the_documents_say_a_spec_less_directory_is_retired_by_the_rule`,
the pin `questions.md` A9 leaves red by design (executed). Both passage
cases are green. The README row in each edition now links
`skills/settle/SKILL.md` *The settling session's procedure*, and
`test_both_cheat_sheets_carry_the_command` pins the link in each
(`tests/test_settle_reads_before_it_removes.py:259`, read). The smith
claimed 3,312 passed over 75 modules with the same single failure; this
round's wider set agrees.

confirms: round-1#3
`spec.md` now holds nine operations, and the ninth rewrites
`docs/the-record-layout.md` *seal/specs/<work-item-id>/*. The dry run at
`--released-at HEAD` lists it at `spec.md:354` with its `from` found
(executed). Round 1's search, `settle[^.]{0,40}appl` over `docs/`, was
re-run. Each hit in this spec's four documents is an operation's `from`,
except `docs/the-review-record.md:168-169` ("at the settle that applies
it"), which names the act and stays true, as `spec.md` *Out* argues for
`docs/one-root-by-lifetime.md:17` (executed, then read).

confirms: round-1#4
The deletion message reads "Whatever it recorded as unverified left with
it, and its directory still stands, so this is no settle"
(`skills/verify/scripts/unverified_check.py:1670-1672`, read). The case
`test_refuses_a_removal_no_settle_explains` asserts the phrase on every
deletion line and that "renamed" is absent
(`tests/test_unverified_check.py:2310-2312`, read). The module passes
(executed). A search for "renamed directory", "read where it went" and
"reads the same way" outside the round records finds the old wording only
at `phases/phase-2.md:26-27` (executed). That sentence owes no change. A
phase record states what its phase found at its moment, and round 1's
finding 4 refutes this one at its coordinate. Rewriting it afterwards would
make the record say something the phase did not find. Git and the round
records keep the correction, as `CLAUDE.md` *The rule a mechanism is kept
against* puts history (read).

confirms: none
The modules the fix diff touches, and their neighbours, pass at `3903202c`
in the clone: `bin/test` over `tests/test_settle_reads_before_it_removes.py`,
`tests/test_unverified_check.py`, `tests/test_settle.py`,
`tests/test_rule_changes.py`, `tests/test_chain_check.py`,
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`,
`tests/test_no_passage_is_pasted_into_a_second_file.py`,
`tests/test_docs_line_wrap.py` and
`tests/test_both_editions_carry_the_same_folds.py` gave 778 passed and 2
skipped. `bin/test-layout --pairs` over the two changed test files names no
pair. The fix diff adds no case, only assertions to existing ones. Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three; CI's `tests` run 40286070452 is green | `broad-gate.md` | the orchestrator, by `broad-gate` once the rounds settle |
| Whether the 0.22.4 settle runs the tree's `settle.py` and reads the tree's `skills/settle/SKILL.md`, since the installed 0.22.3 plugin holds the literal replay. Round 1 left this row and nothing in the fix diff answers it | `plan.md` *Operational impact* | the orchestrator, at the release preparation |
| The pull request body's failure direction, prompt budget and removals, and the `Part of #1033` line of Q2's default | `CONTRIBUTING.md` *What a change to a gate must carry* | the orchestrator, when the body is written |
| Q1's default, one issue per distinct measurement, against how the owner wants the tracker to read | `questions.md` Q1 | the repository owner, at the settle's pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite` at `3903202c` | 1 passed, 6,535 deselected |
| `gh run download 40282308738 -n test-durations` into the round's scratch directory, then a Python comparison of the artifact with the committed `.test_durations` and the file at `a82541df` | same 6,536 keys; 96 removed and 133 added, the added at the artifact's prices; 6,403 kept at the base's prices, all differing from the artifact's; the file equals `durations_union.rendered` of its map |
| the nine operations applied by `Edit` to the clone's `docs/the-record-layout.md`, `docs/release-checklist.md`, `docs/the-review-and-parity-arms.md` and `docs/the-review-record.md`, then `bin/test` over the 86 modules that name a changed document, a README or the skill, or open `"docs"`, with the four whole-root checks | 1 failed, 4,116 passed, 14 skipped: the spec-less pin A9 leaves red; the documents restored afterwards |
| `git grep -l -F docs/ -- tests/` against the modules naming a changed document by name or opening `"docs"` | 95 modules listed; `tests/test_a_rider_reaches_its_file.py`, `tests/test_review_axes.py` and `tests/test_unverified_rows_close.py` open a changed document and are not listed |
| `python3 skills/settle/scripts/settle.py --released-at HEAD` | exit 0; this spec's nine operations placed, the ninth at `spec.md:354` with `from` found |
| `bin/test` over the nine touched and neighbouring modules | 778 passed, 2 skipped |
| `bin/test-layout --pairs` over the two changed test files | 2 files read, 0 pairs |

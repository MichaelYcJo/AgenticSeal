# Review round 5: 1792993972-settle-writes-each-sections-latest-decision

target: 548a7a4b, fixes 7b0ef4e7..548a7a4b

Round 5 is the verifying round for round 4. The fix diff holds two commits.
`3ac7cddb` changes `tests/test_settle_reads_before_it_removes.py` alone, and
`548a7a4b` rewrites round 4's `verdict:` and `answer:` lines and nothing else
in that record (`git diff 9466c886..548a7a4b -- seal/`, executed). The diff
touches no file under `skills/` (`git diff --quiet 7b0ef4e7 548a7a4b --
skills/`, exit 0, executed). So round 4's measure that steps 6 to 8 of
`skills/settle/SKILL.md` are `spec.md` S13's target text byte for byte is
carried with its coordinates and not re-derived: `spec.md` lines 182 to 198
against `skills/settle/SKILL.md` lines 203 to 219. Every other fact below was
established this round in a `git clone --no-local` of the repository at
`548a7a4b`.

## Findings

None. The round reopens nothing and finds no regression in the fix diff.

## Confirmations

confirms: round-4#1
Round 4's finding holds closed at `3ac7cddb`. The smith claimed the case now
pins round 4's five clauses and two more that S13 names. The case at
`tests/test_settle_reads_before_it_removes.py:108-130` holds all seven
strings, in the skill's order (read). This round removed each clause from
the skill in the clone, one mutant at a time, with the case's module,
`tests/test_settle.py` and the passage check as the tests (executed). All
seven mutants went red. Five are round 4's: step 6 without its fix of what a
failure shows, step 6 without its second dry run, step 8 without the naming
in the pull request body, step 8 without its failure path sentence, and step
8 without the corpus answer. Two are the smith's extra clauses: step 6
without its reason that a search finds a module only by how it spells a
path, and step 8 without "Run the repository's `Broad gate` row.". Each of
S13's verified clauses now maps to a string the case holds. The names of
step 6's checks and its dry run, its done condition, its reason it does not
search, step 8's one run, its change and naming of a failure, and its done
condition all have one. The `git grep` absence assertion pins "holds no
search". So the docstring's new sentence, that each clause of steps 6 and 8
that S13 names is pinned, is true of the case (read).

confirms: none
The smith left "Run the failing modules until they pass" unpinned on
purpose, and expected a mutant on it to survive. Two mutants show it does
(executed). The first deletes the clause and keeps the pinned lowercase
"then run the row again". The second replaces the clause with "Fix the
failure". A third mutant removed the clause and capitalised "Then", and it
went red only because the pinned string is lowercase. It does not count
against the claim. The clause is not one S13 names: S13 asks that step 8 say
how a failure on an old fact is changed and named, and that it be done when
the row passes with no edit after it. Both are pinned. The clause saves the
cost of a full broad gate run per fix. The pinned second run and done
condition still hold a session to a passing row with no edit after it. So
the release would ship no wrong instruction if a later edit dropped it, and
leaving it unpinned is no finding.

confirms: none
Two more clauses of step 6 survive a mutant, and neither is one S13 names as
verified (executed). Dropping "It does not look for the other checks that
read what you wrote", with its three examples, leaves "A search of the
tests' text finds a module only by how it spells a path". That sentence is
pinned, so the step still gives S13's reason. The `git grep` assertion still
pins that no search stands in the step. Dropping ": a `to` not found is
where you reworded, which the body explains." leaves "Then run the dry run
again", which is pinned and is the dry run S13 names. The dropped half
states the reading `plan.md:104` gives the second dry run. Neither leaves
the skill telling a session to do something wrong, and pinning every clause
of a procedure is an enumeration with no end. So this round records both
survivors and raises no finding.

confirms: none
`phases/phase-3.md:50-55` owes no change. It reports 6 mutants, 6 red, 0
survived at `98e261ea`, and it names each of the six (read). That is a true
record of what phase 3 ran. It does not claim the case pins every clause of
steps 6 and 8. Round 4's finding records that the six did not cover the
five clauses, and round 4's `answer:` line records the fix pass's seven
mutants. Rewriting the phase record now would change a record of
`98e261ea` to describe `3ac7cddb`. The coverage gap belongs in the round
record that found it, and it is there.

confirms: none
The fix diff adds no test, so no new test is read against its group. It
extends one case. `bin/test-layout --pairs` over the changed module reads 1
file and names 0 pairs (executed). `uvx ruff check` and `uvx ruff format
--check` over it exit 0 (executed). The plan's phase 3 *Verified by*
command gives 66 passed, as the smith's answer claims (executed). The smith's
answer also claims 7 mutants, 7 red, 0 survived. This round's seven mutants
above give the same result (executed).

confirms: none
The branch's `tests` run 40292155366 at `548a7a4b` completed `success` on
every leg (read, `gh run view`). The legs are lint, the two
`arm-check-grammar` jobs, ubuntu, the three macOS groups, the four Windows
groups and `durations`, and `release-report` was skipped. This round leaves
nothing open. What comes due is the orchestrator's broad gate run, then the
sealer's spawn after it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three; CI's `tests` run 40292155366 is green | `broad-gate.md` | the orchestrator, by `broad-gate` once the rounds settle |
| Whether the 0.22.4 settle runs the tree's `settle.py` and reads the tree's `skills/settle/SKILL.md`, since the installed 0.22.3 plugin holds the literal replay. Rounds 1 to 4 left this row, and the fix diff does not answer it | `plan.md` *Operational impact* | the orchestrator, at the release preparation |
| The pull request body's failure direction, prompt budget and removals, and the `Part of #1033` line of Q2's default | `CONTRIBUTING.md` *What a change to a gate must carry* | the orchestrator, when the body is written |
| Q1's default, one issue per distinct measurement, against how the owner wants the tracker to read | `questions.md` Q1 | the repository owner, at the settle's pull request |

## Probes

| Command | Result |
|---|---|
| `git diff --quiet 7b0ef4e7 548a7a4b -- skills/` | exit 0 |
| `bin/mutation-check skills/settle/SKILL.md --tests "bin/test tests/test_settle_reads_before_it_removes.py tests/test_settle.py tests/test_no_passage_is_pasted_into_a_second_file.py -q -p no:xdist"`, ten `--replace` pairs: round 4's five clauses, the smith's two extra clauses, step 8's narrow-run clause removed with "Then" capitalised, step 6's "It does not look for the other checks" sentence, and step 6's rewording half after the second dry run | baseline green; 10 mutants, 8 red, 2 survived: the two step 6 clauses that S13 does not name |
| the same command, two `--replace` pairs on "Run the failing modules until they pass, then run the": replaced by "then run the", and by "Fix the failure, then run the" | baseline green; 2 mutants, 0 red, 2 survived |
| `bin/test tests/test_settle_reads_before_it_removes.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_docs_line_wrap.py tests/test_one_heading_rule_holds_to_commonmark.py -q` | 66 passed |
| `bin/test-layout --pairs tests/test_settle_reads_before_it_removes.py`, `uvx ruff check` and `uvx ruff format --check` over it | 1 file read, 0 pairs; ruff exit 0 twice |
| `gh run view 40292155366` | completed, `success` on every leg, `release-report` skipped |

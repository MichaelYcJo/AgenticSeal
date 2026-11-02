# Phase 1: 1793599988-a-citation-opens-after-the-squash

## What this phase found

**The frame holds, and the build follows it.** Before the build, the
crafter opened the coordinates the frame builds on. `tests/censuses.py:1116`
holds `COMMIT_PATH` as `frame/plan.md` *Technical context* quotes it, and
`tests/censuses.py:850` holds `RECORDS` (read). `.github/workflows/test.yml`
checks the pytest job out with `fetch-depth: 0` (read, at lines 118 to 120).
`tests/behaviour/test_a_cited_section_stands_in_its_file.py#corpus` reads
its files through `git ls-files -z`, `conftest.on_disk` and a UTF-8 read
(read). `git for-each-ref --contains` on a commit the object store lacks
exits 129, prints `malformed object name` on standard error and prints
nothing on standard output (executed, on the frame's dead commit). Line 18
of `seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md`
held the one dead citation, and the squash `48d035aa` holds the cited path
(executed: `git cat-file -e`, exit 0).

**Departure: one more file changes than the frame names.**
`tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` lists every
scope in the suite that lists paths from git, and it turns red on a scope
that no table classifies. The new `cited` lists `git ls-files` and applies
`on_disk`, so it gains a row in `APPLIES_THE_SHARED_GUARD`, beside the
sibling's `corpus` row. The frame's *Data & interfaces* says that no shipped
file changes, and this file is not shipped, so the statement still holds.
The plan's narrow run did not name this module, and the phase-boundary run
below adds it.

**Decision: the unit names.** The build chose `read_here(rel)` for the
scope, and the frame's `cited`, `reaching` and `unreached`. It also chose
`refusal(found)` for the assertion message and the constants `REACHING`,
`NO_REF`, `REPAIR` and `FETCH`. Grounds: `frame/design.md` *Data &
interfaces* leaves the names to the build. A separate `read_here` gives S4's
mutants one place to break.

**Decision: `text_of` is imported from the sibling module, not copied.** The
new module reads each file through
`tests/behaviour/test_a_cited_section_stands_in_its_file.py#text_of`.
Grounds: `skills/core/SKILL.md` *The rule a mechanism is kept against*
says a fact has one source, and `frame/plan.md` *Technical context* asks
for the sibling's way of reading. The module does not use the sibling's
`flowing`, because `COMMIT_PATH` matches no whitespace, so a token never
spans two lines.

**Decision: the planted repositories set their refs with `git update-ref`.**
`planted` commits twice on a branch named `work`, then points each ref in
its arguments at one of the two commits. Grounds: a checkout of `main` would
depend on the machine's `init.defaultBranch`, and `update-ref` writes a
remote-tracking ref as easily as a local one. So S3 is parametrised over
`refs/heads/release/v9.9.9` and `refs/remotes/origin/main`, which covers
the local refs a contributor has and the remote-tracking refs CI's checkout
has (`frame/design.md` G9). S2 adds `refs/remotes/origin/feature/x` to show
that a remote feature ref does not count (G10). S6 adds a tag and a `trunk`
branch, so it shows that neither counts as a reaching ref.

**Decision: S7 asserts the module's own constants.** The case asserts that
the message holds each `file:line`, the commit, `REPAIR` and `FETCH`, so the
two sentences a person reads are pinned where they are defined (contract
rule 14). `frame/design.md` S7 asks for the message's parts as values the
case computes, and not a sentence pinned in the case.

**Decision: the tree case has no floor on the count it reads.** Grounds:
the frame asks for none. The planted cases hold the reader through the
imported `COMMIT_PATH`. A floor written as a number is a count kept beside
the tree, which `skills/core/SKILL.md` *The rule a mechanism is kept
against* refuses. The decision is in `gaps.md` *Not done*.

**Seen red, S1.** The tree case ran on the working tree before Scope item
5's edit. The run failed and named
`seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md:18
cites 79252e48`. The module's other nine cases passed (executed: `bin/test
tests/text/test_a_cited_commit_outlives_the_squash.py -p no:xdist`, exit 1,
1 failed and 9 passed). After the edit, the row cites the squash's copy of
the file and keeps the bare `79252e48` that issue #1235 cited.

**Mutation.** Each planted case was seen red against a mutant of the
module, committed first at the build commit in `frame/plan.md`'s Status
cell. #898's defect is not fixed in this tree, so `seal mutate` reads a
mutant that does not compile as red. Two checks guard against it. A probe
under the scratch directory applied each replacement in memory and passed
the result to `compile()`: each of the 11 replacements occurs once, and
each compiles (executed, exit 0, probe deleted). Each red run below failed
on an `assert` with no `ERROR collecting` line (executed: each run's output
searched). The batch of mutants 1 to 10 over the whole module with `-x`
gave `10 mutants, 10 red, 0 SURVIVED` (executed, exit 0). Each mutant was
then run alone against the case it was written for (executed, exit 0 each):

| # | Break | Red case |
|---|---|---|
| 1 | The work item branch of `read_here` returns `False`, so all of `seal/threads/` goes unread | `test_the_rest_of_a_work_item_is_read` |
| 2 | The containment call becomes `git cat-file -t <commit>` | `test_a_citation_of_a_feature_branchs_commit_is_refused`, both extensions |
| 3 | A non-zero exit reads as reached (`returncode != 0 or ...`) | `test_a_commit_no_clone_holds_is_refused` |
| 4 | `if not refs:` becomes `if False:` | `test_no_reaching_ref_judges_nothing` |
| 5 | `FETCH` is dropped from the message | `test_the_refusal_says_where_and_the_repair` |
| 6 | The `evals/behaviour/` exclusion becomes `if False:` | `test_a_record_of_what_a_party_ran_is_not_read` |
| 7 | The `guarantee.md` exclusion is deleted | `test_a_record_of_what_a_party_ran_is_not_read` |
| 8 | The `trail/` exclusion becomes `False` | `test_a_record_of_what_a_party_ran_is_not_read` |
| 9 | The line count drops its `+ 1` | `test_a_citation_of_a_feature_branchs_commit_is_refused`, both extensions |
| 10 | The commit is taken as the whole token, path included | `test_a_citation_of_the_squash_is_accepted`, both refs |

**Departure: the plan's third mutant has no branch to remove.** The plan
names a mutant that removes the missing-object branch. The build makes one
`for-each-ref --contains` call per commit and refuses unless the call exits
0 and lists a ref, as *Data & interfaces* asks ("reads the exit code and the
output"). A missing object is refused by the same test. Mutant 3 turns an
error into a pass, and S5 goes red on it. An eleventh mutant deletes the
exit-code half (`run.returncode == 0 and`). It SURVIVED over the whole
module (executed: exit 1, 10 passed). The cause is git's behaviour: when
`--contains` fails, git prints no ref, so the output half alone refuses the
missing object. The build keeps the exit-code half, because it refuses a
failed call whatever git prints, and the frame's interface reads both
halves. To show that half working alone, a case would need a git that fails
and still prints a ref, and this phase builds none. That is contract rule
13's case: a defence beside a platform guarantee, unverified until the
guarantee is removed.

**Scope item 6 and `frame/questions.md` Q1 are not done in this phase.**
The spawn told the crafter not to merge `release/v0.28.1` into the branch.
The orchestrator merges it before the review rounds, runs the tree case
again, and folds what it finds. At this phase's commit, the tree case
passes.

**The class (contract rule 12).** The method is a command that lists each
thing holding the property: the tree case lists each in-scope citation
whose commit no reaching ref contains. Before item 5 it listed one
instance, and after item 5 it lists none. The open part of the class is
what the frame's *Scope* puts out of reach: bare commits, `trail/`,
`guarantee.md`, issue bodies, and citations whose path `COMMIT_PATH` does
not match. The proofer reads those.

**The phase-boundary run.** One command,
`bin/test` over the new module,
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`,
`tests/test_censuses.py`,
`tests/text/test_ci_gives_the_checks_what_they_need.py`,
`tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`, and the
modules that read every tracked file and so read the new module and the
edited frame:
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`,
`tests/behaviour/test_one_heading_rule_holds_to_commonmark.py`,
`tests/behaviour/test_no_document_names_the_old_roots.py`,
`tests/behaviour/test_release_hygiene.py`,
`tests/behaviour/test_a_release_is_sized_by_a_criterion.py`,
`tests/behaviour/test_both_editions_carry_the_same_folds.py`,
`tests/hooks/test_launch.py` and
`tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`,
with `-rfEs --durations=0`. The result was 347 passed, with nothing skipped
(executed, exit 0). As `--durations` printed it on the crafter's machine,
the tree case's call took 0.70 s. The module's ten calls took 4.4 s in all,
spread over xdist workers. `uvx ruff check` and `uvx ruff format --check`
on the two changed test modules exited 0 (executed). `seal layout --pairs`
names no pair in the new module (executed, exit 0).

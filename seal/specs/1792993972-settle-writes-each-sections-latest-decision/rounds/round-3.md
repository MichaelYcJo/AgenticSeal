# Review round 3: 1792993972-settle-writes-each-sections-latest-decision

target: d86b96f8, fixes 3903202c..d86b96f8

Round 3 is the verifying round owed to round 2's regression. It reads the
fix diff `3903202c..d86b96f8`: the fix `72fc2c58` to step 6 of
`skills/settle/SKILL.md` *The settling session's procedure*, its pin in
`tests/test_settle_reads_before_it_removes.py`, the changelog bullet, and the
answer (`d86b96f8`). Every fact below was established this round in a
`git clone --no-local` of the repository at `d86b96f8`. Four facts are
carried with their coordinates and not re-derived, since the fix diff
touches none of their files: round 2's three carried facts (the dry run's
counts over `origin/main`, the rename rows at
`skills/verify/scripts/unverified_check.py:1597-1599`, and the predicate at
`skills/verify/scripts/unverified_check.py:1266-1279`), and round 2's replay
of the nine `## Rule changes` operations, whose result this round did not
repeat.

## Findings

### 1. Step 6 says its set holds the checks that read every document, and a check that reads every tracked Markdown file is not in it

severity: should
location: `skills/settle/SKILL.md:203-217`, `tests/test_settle_reads_before_it_removes.py:116-121`, `seal/specs/1792993972-settle-writes-each-sections-latest-decision/changelog.md:6`
evidence: executed `git grep -l -w -F -e docs -e the-review-record.md -- tests/`, `bin/test tests/test_one_heading_rule_holds_to_commonmark.py -q`, `bin/test $(cat probe_set.txt) -q`
verdict: deferred the frame
regression: round-2#1

The unit is step 6 of `skills/settle/SKILL.md` *The settling session's
procedure*, which `ffeadf29` made for round 1's finding 5 and `72fc2c58`
rewrote for round 2's finding 1. The frame asks the session to "run the
documents' checks over what it wrote" (`spec.md` *In* item 3), and `plan.md`
*How a settle's result is verified* names the instruments; the fix replaced
that with a set defined by a text search and wrote that the search "finds
the checks that read every document rather than one by name", so the defect
came from how the fix was written, not from the frame. `ffeadf29` brought in
the narrowing. Before it, step 6 said "Run the repository's checks over what
you wrote" (`a9789bb2`, read). `72fc2c58` rewrote the sentence and kept the
claim. This is the second regression on this unit after round 2's
regression was routed to a fix pass, so it goes to the framer whatever the
comparison says.

`tests/test_one_heading_rule_holds_to_commonmark.py:42-49` lists every
tracked `.md` file with `git ls-files -- '*.md'` and reads each one, the
policy documents and both READMEs included. Its text holds neither `docs`
as a word nor a document's name, so step 6's command does not list it, and
its sentence does not name it. The module pins two facts a settling session
can break while writing a section: no heading stands indented under a list
item, and no setext heading stands in a body. A paragraph line followed
directly by a `---` line is such a setext heading.

The probe wrote that `---` line under the opening paragraph of
`docs/the-review-record.md` in the clone. Step 6's set for that one changed
file is 106 modules, and `bin/test` over them gave 4,017 passed and 13
skipped, exit 0. So step 6 reads as done. The heading module alone failed
`test_every_setext_heading_in_the_tree_is_a_front_matter_line` at
`('docs/the-review-record.md', 3)`. A session that follows step 6 meets
this failure first at step 8, the broad gate that runs once. Round 1's
finding 5 asked step 6 to close exactly that path.

What was asked of this round:

- Step 6 now has one reading. The command and the sentence name one set.
  Matching the six file names with and without `-w` lists the same 74
  modules. Each of the 13 modules that hold `docs` only inside another
  word holds it in `docstring` (executed).
- The command finds exactly the set its sentence names, since `git grep -w
  -F` is the sentence's definition. What is wrong is the sentence after it,
  which says what that set holds.
- The smith's stated limit, a module that reads a document only through a
  `tests/conftest.py` helper, is one case of a wider class: a module that
  reaches a document other than by naming it. `tests/conftest.py:31-46`
  `review_chain_text` is one such helper today, and both its callers are in
  the set by name. A listing over the tree is another way, with one
  instance today, the module above. So "none today" does not hold for the
  class. The limit belongs in the skill, stated as the class, because a
  text search is an enumeration over spellings and cannot close it
  (`skills/code-review/SKILL.md` *A finding is not closed too early*).

The search for the class ran over every module under `tests/` outside the
set that holds `ls-files`, `os.walk(`, `glob(`, `rglob(`, `iterdir(`,
`"*.md"` or `endswith(".md")`. Only the heading module reads tracked policy
documents. The rest read fixture trees, `templates/`, `agents/` or Python
files (executed, then read).

Three fixes have now chased this set's edge cases. The framer should ask
what step 6 decides before it adds a fourth spelling (`CLAUDE.md` *The rule
a mechanism is kept against*). One option is to name the plan's
instruments and the `check:` targets, and to leave everything else to
step 8 with the limit stated. The other keeps the search, adds the pattern
that finds a listing, and states the class it cannot find. The second,
paste-ready:

```markdown
6. Run, over what you wrote, each rule's `check:` targets and every
   module under `tests/` that reads a file you changed. Where the root is
   `docs/`, `git grep -l -w -F -e docs -e '*.md' -e <name> -- tests/`
   finds them, with one `-e <name>` for each file you changed, such as
   `-e the-record-layout.md -e README.md`. The directory name finds a
   module that names or joins a document's path, such as a line-length
   or a duplicated-passage check, which no `check:` line names. `*.md`
   finds one that lists every tracked Markdown file, such as the heading
   check. A file's name finds one that opens that file without the
   directory, such as one reading a README. A module that reaches a
   document any other way, through a helper in another file or a script
   it runs over the tree, is found by none of them, and step 8 is where
   it shows. Where a case fails because a pin under `tests/` or a copy
   such as a README row still states the old fact, change that pin or
   copy, and name each in the pull request body. Then run the dry run
   again: a `to` not found is where you reworded, which the body
   explains. The step is done when every one of those modules passes.
```

With `-e '*.md'` the command lists 125 modules over this spec's four
documents and both READMEs, the heading module among them, and the six
other additions read templates, agents or fixtures (executed). The pin
replaces its set sentence and command and gains the limit. Each new string
is absent from the current text, so a revert leaves it red:

```python
        "module under `tests/` that reads a file you changed",
        "`git grep -l -w -F -e docs -e '*.md' -e <name> -- tests/`",
        "with one `-e <name>` for each file you changed",
        "is found by none of them, and step 8 is where it shows",
```

The changelog bullet's clause becomes "runs each rule's `check:` targets
and every test module that reads a file it changed over what it wrote".

answer: Routed to the framer, not to a fix pass. It is the second regression on step 6 of `skills/settle/SKILL.md`, whose first (round-2#1) was routed to a fix pass, and `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame* sends such a unit to the framer whatever the comparison says. The framer is spawned with rounds 1 to 3 as its input.

## Confirmations

confirms: round-2#1
Round 2's defect is closed. The set and its command are one reading, as
the first bullet under finding 1 says. The four modules round 2 named as
missed are now in the command's set: `tests/test_a_rider_reaches_its_file.py`,
`tests/test_review_axes.py`, `tests/test_unverified_rows_close.py` and
`tests/test_the_root_migrates_itself.py` (executed). The smith claimed the
command lists 118 files over this spec's four documents and both READMEs;
it lists 118 (executed). Two of them, `tests/conftest.py` and
`tests/censuses.py`, hold no test, which costs nothing. The smith claimed
the pin is red against `ffeadf29`'s text and green after. With
`3903202c`'s `skills/settle/SKILL.md` checked out in the clone,
`test_the_skill_states_the_settling_sessions_procedure` failed; at
`d86b96f8` it passed (executed). The changelog bullet names a changed file
beside the directory (read, `changelog.md:6`). Finding 1 above is a
different defect in the same unit: a module the set never held.

confirms: none
The modules the fix diff touches and their neighbours pass at `d86b96f8`
in the clone: `bin/test` over `tests/test_settle_reads_before_it_removes.py`,
`tests/test_settle.py`, `tests/test_docs_line_wrap.py`,
`tests/test_no_passage_is_pasted_into_a_second_file.py` and
`tests/test_one_heading_rule_holds_to_commonmark.py` gave 113 passed.
`bin/test-layout --pairs` over the changed test file names no pair. The fix
diff adds no case, only assertions to an existing one. The branch's `tests`
run 40287897601 at `d86b96f8` completed `success` (read, `gh run view`).
Executed, except the run, which was read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three; CI's `tests` run 40287897601 is green | `broad-gate.md` | the orchestrator, by `broad-gate` once the rounds settle |
| Whether the 0.22.4 settle runs the tree's `settle.py` and reads the tree's `skills/settle/SKILL.md`, since the installed 0.22.3 plugin holds the literal replay. Rounds 1 and 2 left this row and nothing in the fix diff answers it | `plan.md` *Operational impact* | the orchestrator, at the release preparation |
| The pull request body's failure direction, prompt budget and removals, and the `Part of #1033` line of Q2's default | `CONTRIBUTING.md` *What a change to a gate must carry* | the orchestrator, when the body is written |
| Q1's default, one issue per distinct measurement, against how the owner wants the tracker to read | `questions.md` Q1 | the repository owner, at the settle's pull request |
| Whether step 6 keeps a text-searched set at all, or names the plan's instruments and leaves the rest to step 8 | `plan.md` *How a settle's result is verified* | the framer, on finding 1's route |

## Probes

| Command | Result |
|---|---|
| `git grep -l -w -F -e docs -e <name> -- tests/` with the four documents and both READMEs as names | 118 files, all `.py`; `tests/conftest.py` and `tests/censuses.py` hold no test |
| `git grep -l -F docs -- tests/` against the `-w` set | 13 modules more, each holding `docs` only in `docstring` |
| the six names with and without `-w` | 74 modules either way |
| `bin/test tests/test_settle_reads_before_it_removes.py -q -p no:xdist -k test_the_skill_states_the_settling_sessions_procedure` with `3903202c`'s skill text, then with `d86b96f8`'s | 1 failed, then 1 passed |
| a `---` line written by `Edit` under the opening paragraph of the clone's `docs/the-review-record.md`, then `bin/test tests/test_one_heading_rule_holds_to_commonmark.py -q` | 1 failed, 1 passed: `('docs/the-review-record.md', 3)` |
| the same edit, then `bin/test $(cat probe_set.txt) -q`, the file holding the 106 modules `git grep -l -w -F -e docs -e the-review-record.md -- tests/` lists | 4,017 passed, 13 skipped, exit 0; the edit was then reverted by `Edit` and `git status` was clean |
| the search for whole-tree readers outside the set: `ls-files`, `os.walk(`, `glob(`, `rglob(`, `iterdir(`, `"*.md"`, `endswith(".md")` | one module reads tracked policy documents: `tests/test_one_heading_rule_holds_to_commonmark.py` |
| the command with `-e '*.md'` added | 125 modules; adds the heading module and six that read templates, agents or fixtures |
| `bin/test` over the five touched and neighbouring modules at `d86b96f8` | 113 passed |
| `bin/test-layout --pairs tests/test_settle_reads_before_it_removes.py` | 1 file read, 0 pairs |

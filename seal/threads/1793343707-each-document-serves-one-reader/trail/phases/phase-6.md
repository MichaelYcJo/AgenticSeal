# Phase 6: 1793343707-each-document-serves-one-reader

## What this phase found

**The frame held for the version and the fragment.** At `fbd6857f`,
`.claude-plugin/plugin.json` read `0.25.0`, as it does at the base
`fba13ab2`. `git grep -n '0\.25\.0'` outside `seal/threads/` finds no other
file that carries the plugin's version; the other hits are history in test
docstrings and fixtures (executed). `skills/implement/orchestration.md`
*Which branch the pull request lands on* moves the version in the first pull
request into `release/vX.Y.Z`, in the commit that adds the fragment, and
`b6d84d71` does both. `.github/scripts/publish_release_note.py#section`
lifts a fragment's `### Process changes` table by the heading and header
row of `templates/records/process.md`, and passes the rest of the body
through as it stands (read). `tests/behaviour/test_release_hygiene.py`
refuses a file under `LOADED` that names a version at or above the running
one, and at `0.25.1` it passes in the boundary run below (executed).

**The frame does not hold for scenario S10: the change adds more lines
than it removes outside `seal/threads/`.** The command and its output at
`b6d84d71` (executed, exit 0):

```
$ git diff --shortstat fba13ab2...HEAD -- . ':(exclude)seal/threads'
 60 files changed, 1128 insertions(+), 988 deletions(-)
```

That is 140 more lines added than removed. At `fbd6857f`, before this
phase, it read `59 files changed, 1127 insertions(+), 987 deletions(-)`;
this phase adds the version line's one-for-one swap. Broken down by
`git diff --numstat` over the same range (executed):

- `agents/` +62 -28, `templates/` +6 -37, `skills/` +412 -355, `evals/`
  +69 -212, `hooks/` +2 -2, the two READMEs +14 -11, `seal/README.md`
  +1 -1, `.claude-plugin/plugin.json` +1 -1. The shipped files outside
  `tests/` remove 80 more lines than they add.
- `tests/` +561 -341, 220 more lines added than removed.

The change was not padded or trimmed to meet the count. `gaps.md`
*Not done* records it with the numbers. Whether the issue's last bullet
stands unmet is for the owner at the pull request.

**The measure's first two commands print a count per file, not one
number.** `git grep -c` prints one `path:count` line per file that
matches, and none for a file with no match. Over
`seal/threads/1793273065-the-core-reaches-no-users-repository/` at
`fbd6857f` (executed, each exit 0):

```
$ git grep -c '^### [1-9]' -- 'seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-*.md'
seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-1.md:3
seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-2.md:2
seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-6.md:4
seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-7.md:1
$ git grep -c '^regression: \|^reopens: ' -- 'seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-*.md'
seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-2.md:2
seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-7.md:1
$ git grep -h '^location: ' -- 'seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-*.md' | grep -vc '`[^s`][^`]*`\|`s[^e][^`]*`'
1
$ ls seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/ | wc -l
       8
```

The third command's two pipe stages both exited 0 (read from zsh's
`pipestatus`). Summed, the first two give 10 and 3, and with the last two
the four read 10, 3, 1 and 8, the numbers `frame/design.md` *The measure's
command* states. Nothing prints 10 or 3 as such. A settling session that
reads the output as one number per command would read four or two lines
instead. The rule change that adds the measure to `docs/the-review-record.md`
*The run* names `git grep -c` and does not say the lines are summed. That
sentence is the framer's, and this phase did not change it. The hand-back
names it for the orchestrator.

**What the fragment covers.** `changelog.md` holds one `### Changed` entry
and twelve `### Process changes` rows. The entry states what a user of the
plugin meets: the reshaped templates (phases 1 and 2), the removed
`Approved` line and the spawn as the approval (phase 2), the phase record
as the home of departures and `gaps.md` from the first phase's close
(phase 2), the body's new order and fold and the refusal of a body 0.25.0
wrote (phase 5), the records-only `fixed` that owes no verifying round and
the refusal from an older check (phase 3), the split of
`skills/implement/orchestration.md` with its `wc -w` (phase 4), the
three-fix rule's home (phase 2), the framer's two new rules and the
exchange at the spawn (phases 1 and 4), the launcher's message (phase 4),
and that a work item in flight keeps its records (`frame/plan.md`
*Operational impact*). The rows are one per change to the way of working:
the records' homes, the departure's home, `gaps.md`'s trigger, the
`Approved` line, the exchange at the spawn, the records-only fix, the
body's order, the orchestration split, the three-fix rule's home, the
framer's mark rule, the narrowed direction rule, and the settle's measure.

**Decisions made under `automation`, each where the frame was silent.**

- The `### Changed` section is one entry, as the plan's row and #1177's
  fragment have it.
- Each row's Source is the issue, #1148, except the records-only fix's,
  which is #1045, the issue whose half the design takes in. No issue
  comment holds each change on its own.
- The measure has a row though the plan row's list does not name it. The
  design's `## Rule changes` adds it to the settle's work, which is a change
  in the way of working that the next release's settle meets.
- The departure's home and the `Approved` line have rows of their own,
  apart from the records' homes, because each changes what a party writes
  at a different moment.

**No case is new, and no mutant was run.** The fragment is a record, and
the version is a value; neither adds behaviour a case could break. The
cases that read them already stand: `tests/github/test_publish_release_note.py`
builds the note's process table from the template, and
`tests/behaviour/test_release_hygiene.py` reads the running version from
`plugin.json` against every loaded file and the tags.

**`seal pr-body` over this work item now copies the fragment.** Run through
the tree's `bin/seal` into the scratchpad's `pr-body-6.md`, it gave exit 0,
and `--check` on the same file gave exit 0 (executed). The body is 110
lines. Its `## What changed` section opens "From `changelog.md`." and copies
the fragment, where phase 5's said the file was absent.

**`gaps.md` gains two `## Not verified` rows and one `## Not done`
paragraph.** The rows are GitHub's rendering of the fold, answered by the
orchestrator at the first body, and the behaviour suite not run on
`frame/questions.md` Q1's default, answered by the owner at the pull
request. The paragraph is the shortstat above. `seal unverified` over the
work item reads `5 open · 1 closed`, exit 0 (executed).

**The phase-boundary set is 55 modules, run as one command.** It holds the
three modules row 6 names, every module that names `plugin.json`, and every
module that reads `seal/threads/`. The first attempt ran no tests, exit 5:
zsh does not split an unquoted variable into words, so the list reached
pytest as one argument. Passed as `$(cat <file>)`, the set gave exit 0,
`3987 passed, 1 skipped` with this record, `gaps.md` and the plan's Status
cell written over `b6d84d71` (executed). The three named modules, run
alone, gave exit 0, `84 passed` (executed).

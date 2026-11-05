# Phase 2: 1793862999-unverified-baseline-is-run-by-a-person-only

## What this phase found

**The frame held at every coordinate the phase changed, with one exception
in A5.** The clause naming `seal unverified --baseline origin/<base>` stood at
`skills/implement/SKILL.md:378`. The second command line stood at
`skills/verify/SKILL.md:231`. The command rows stood at `README.md:347` and
`README.ko.md:350`. These are the coordinates design *Scope* items 9 to 11
give. The exception is this: at `e8e53f01`, A5's command names one line,
`docs/checks/the-fold.md:21`. That sentence is the `from` of the design's
`## Rule changes` operation on `docs/checks/the-fold.md` *The fold, and what
tells it from a deletion*. The settle rewrites it, and this work item edits
no `docs/` file (plan *Alternatives considered* row 7). So A5's "names
nothing" holds for every file outside the policy root, and holds for the
policy root only after the settle. The frame is the framer's, so this goes to
the orchestrator in the hand-back.

**The closing memo says the proofer also reads a memo that left whole.** The
spawn named "a deleted row or memo". *Scope* item 9 removes the command's
clause and adds nothing. I wrote "and so does a memo that left whole" after
the row clause. That sentence is what the sentence's own "or a deleted file"
needs once no command names the file. It says what
`skills/verify/scripts/unverified_check.py`'s module docstring (lines 25-27)
already says: a row or a closing memo deleted rather than closed is read in
the closing memo's diff. I judged this against `skills/core/SKILL.md` *The
rule a mechanism is kept against*: a change removes what stood on the old
fact, and the old fact was that a command listed each deleted row.

**"No check at the pull request refuses ... a deleted file" stays.** This
repository's suite carries
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`.
That case fails where a framed work item has no `gaps.md`. It is this
repository's own case, though, not a check the plugin ships. The sentence is
read in a user's repository, where no such case runs. So the sentence still
holds there, and I left it as it was.

**The verify skill cites the closing memo by its full heading.**
`skills/implement/SKILL.md` *4. The closing memo — only what the diff cannot
show* is the spelling of the example under *용어는 실물을 확인하고 고른다*
in `skills/writing-style/SKILL.md`. The code block's comment column was
realigned to the one line left.

**The phase is prose only, so it adds no case and runs no `seal mutate`.**
`skills/verify/SKILL.md` *The narrow command still has to be able to fail*
gives the *Prose only* row for it: what can fail is whatever parses the four
files. Executed at `e8e53f01`, one `bin/test` command ran three sets. The
first was the 53 modules that `git grep -l -e SKILL.md -e README -- tests/behaviour
tests/text` lists, which plan row 2 names. The second was
`tests/github/test_rules.py`, `tests/skills/test_passages.py`,
`tests/skills/test_coordinates.py` and `tests/skills/test_payload_meter.py`,
each of which reads skill text. The third was `tests/test_censuses.py`. It
gave exit 0, with 1334 passed.

**The other statements of the reworded rule were looked for, and the list is a
sample.** I ran `git grep -n -i` outside `seal/threads` and `.test_durations`
for `deleted row`, `row that left`, `deleted rather than closed`,
`tidied it away`, `keeps the count`, `number of rows`, `nothing was deleted`
and `run by a person`. The search found only the two edited skills and
`unverified_check.py:25`, which phase 1 already rewrote. The sentences that
`docs/` states about the mode wait for the settle through the design's
`## Rule changes`.

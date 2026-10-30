# Review round 5: 1793343707-each-document-serves-one-reader

target: e88426a1, fixes 7976c096..e88426a1

This is a verifying round. It reads the diff of round 4's fix pass:
`2c7ba65a`, the orchestrator's fold of the frame lines; `f6c65dac`, finding
2; `8123af5b`, findings 1 and 3; and `e88426a1`, the fix pass's verdict
lines. `git diff --stat 7976c096..e88426a1` names six paths:
`agents/crafter.md`, the fragment, `frame/design.md`, `frame/plan.md`,
`round-4.md` and `tests/text/test_a_moved_rule_leaves_its_definition.py`
(executed). The `round-4.md` change is the three `verdict:` lines and
the three `answer:` lines and nothing else (executed). All four commits carry
`Seal-Routing: 1793343707-each-document-serves-one-reader` (executed).

Carried from round 4 and not searched again: the home of the second count
in the three places round 4 named, and the class round 4 gave for finding 2,
a reader whose copy differs in its root, under its conditions, or in the
release that ships it. Carried from round 2: that a design's
`## Rule changes` reaches the policy root at the settle after the work
item's release, not in the release. Re-established this round: every verdict
below, the count of the five lines, the pin red against the old paragraph
and against the deleted sentence, and the narrow module green (executed,
*Probes*).

## Findings

This round opens no finding.

## Confirmations

confirms: round-4#1
The three places now name the findings that carry the line.
Scope item 7 at `frame/design.md:57` reads "findings that carry a `regression:`
or `reopens:` line", and so does the `add`'s bold sentence at
`frame/design.md:267`; both came in the orchestrator's fold `2c7ba65a`
(read). The fragment's process row at `changelog.md:20` reads the same, in
`8123af5b`, which touches a path the finding's `location:` names (executed,
`git show --stat`). The `add`'s next sentence still reads the count from
"the `regression:` and `reopens:` lines", and since a finding holds at most
one of them, the two sentences now give one number. Round 4's executed
line, re-run over this item's rounds, prints 5 lines and 3 distinct values,
as before (executed). The bold sentence now counts the 5. The fix pass
claimed no other statement of the second count stands. A `git grep` for
"named again", "line names", "recurred" and "recurring of" over the tree,
the round records left out, finds the count only at `frame/design.md:31`
("17 of 36 findings recurred") and `:32` ("3 carry a `regression:`
or `reopens:` line"). Both count the carrying findings. Every other hit names
what a line points at (executed). The claim holds.

confirms: round-4#2
The fix pass claimed it took the release as the third axis in its own
words, and why: in the round's text, "where" could read as a condition on
the release axis, and "it" had two antecedents. `agents/crafter.md:168-174`
now reads "a procedure step is read in either `seal/` root (contract rule
11), under every condition its file names, and in the release that ships
it. In that release, a section the step cites holds the text the release
ships, not the text a design's `## Rule changes` writes at a later settle"
(read). I read it as its reader would. "It" in "ships it" has one
candidate, the step that is the sentence's subject. The second sentence
names "the step" and puts no condition on the release axis. "Where that
reading fails" still points back to the reading the colon opened, across
one statement and not across a rule of its own. Round 1's finding 4 is
the defect the axis is for. Run through the sentence, it fails the reading:
the step shipped in 0.25.1 and cited `docs/the-review-record.md` *The run*.
In 0.25.1 that section did not hold the text, because the text stood only
in the design's `## Rule changes` until the settle after 0.25.1 (carried
from round 2). So the sentence now stops that case. In a user's repository
and in a local `seal/` root the sentence still holds. Its terms are the
plugin's own: `## Rule changes` is a heading of
`templates/records/sdd-design.md:23`, and `skills/settle/SKILL.md` names it
five times (executed). The sentence names no path of this repository.
The pin holds the two sentences as two entries. With the paragraph put back
to its `2c7ba65a` text through `Edit` (`git diff --stat 2c7ba65a --
agents/crafter.md` empty), the case failed, exit 1, on "the fix-pass rule
lost 'in either `seal/` root (contract rule 11), under every condition its
file names, and in the release that ships it.'". With only the second
sentence deleted, it failed, exit 1, on that sentence. Restored, `git status
--short` was empty and the module passed (executed). This repeats the fix
pass's red run and its `seal mutate` run, and both hold. The frame's
Scope item 13 at `frame/design.md:63` and plan row A21b at
`frame/plan.md:64` name the three axes (read). No other file states the
reading: `git grep -n -i 'paste-ready'` over `skills`, `docs`, `agents`,
`templates` and the two READMEs finds the axes only in `agents/crafter.md`
(executed). No new case function was added. The two entries went into the
one case that reads the paragraph, so they have no group to be read
against.

confirms: round-4#3
`changelog.md:21` is a new last row of `### Process changes`, with a date,
the change, one line of why and a link. The link is
`#issuecomment-6520356879`, a comment of 2026-10-30 on #1148 that names
this run's recurrence and its prevention home (executed, `gh api`). The `### Changed` entry at
`changelog.md:3` gains two sentences after the framer's rule (read). Both
state the three axes. The fix pass claimed each "states the sentence as it
ends up after finding 2". That holds for the content and not for the form.
The entry and the row keep the round's construction, "in the release that
ships it, where a section the step cites holds that release's text", which
is the construction the answer to finding 2 split in the definition. I
judged that construction, not the fix pass's reason for the split. Here
"where" follows "the release" and reads as "in which". A reader taking it as
a condition on the axis gets a rule that skips exactly the case it names,
and no other sentence of the entry supports that reading. The row's reader is
the next framer (`docs/the-record-layout.md:51-60`). The framer learns from
it what the fix pass now does, and does not apply the fix pass's reading
itself. The rule's text, which a crafter does apply, is the definition's.
So the two forms differ in wording and say one thing, and this round raises
no finding on the difference. `8123af5b` touches `changelog.md`, a path the
finding's `location:` names (executed).

confirms: none
The narrow module `tests/text/test_a_moved_rule_leaves_its_definition.py`
passed at `e88426a1`, `222 passed`, exit 0. `uvx ruff check` and `uvx ruff
format --check` over it each exited 0 (executed). No `seal/parity.md` is
declared, so this record names no baseline commit. This round leaves
nothing open. What comes due is the orchestrator's broad run, then the
sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Carried from round 4: whether the settle after 0.25.1 takes the four counts before its step 7 removes the records they read | `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:267` | the owner's settling session, at the settle after 0.25.1 |
| Carried from round 4: the `add` says the step ships to no user, while the plugin's package holds `docs/release-checklist.md` and `skills/settle/SKILL.md:146` sends every settling session to its 2b | `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:267`, `skills/settle/SKILL.md:146` | #1147 |
| Round 1's finding 6 stands `deferred frame/questions.md Q2` and is not written up again | `seal/threads/1793343707-each-document-serves-one-reader/frame/questions.md` | the owner, answering Q2 |
| Carried: the behaviour suite over the agent definitions, the fix-pass sentence in `agents/crafter.md` among them, not run on Q1's default | `agents/crafter.md:168-174` | the owner, at the pull request |
| Carried from round 1: a finding located in `frame/design.md` `## Rule changes` and fixed there alone passes with no round, and the settle writes that text into the policy root | `skills/code-review/scripts/chain_check.py:1452-1456` | the owner |
| Carried from round 2: 19 of the 25 commits in `fba13ab2..b3b36143` carry no `Seal-Routing:` trailer | `fba13ab2..b3b36143` | the orchestrator |
| Carried from round 1: GitHub's rendering of the body's fold | `skills/code-review/scripts/pr_body.py` | the orchestrator, reading the first body this change writes |
| The full suite, the repository-wide lint and format check, and the cross-platform run at `e88426a1`. The suite is `unverified` here | the branch at `e88426a1` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `git diff --stat 7976c096..e88426a1`, and the diff of `round-4.md` over the range | six paths; `round-4.md` changes three `verdict:` and three `answer:` lines only |
| `git log --format='%h %(trailers:key=Seal-Routing,valueonly)' 7976c096..e88426a1` | four commits, each with the work item's id |
| `grep -h '^regression: \|^reopens: '` over this work item's rounds, with `wc -l` and with `sort -u` then `wc -l` | 5 and 3 |
| `git grep -n` for "named again", "line names", "recurred" and "recurring of" over the tree, round records left out | the count only at `frame/design.md:31-32` and the three fixed places; no other statement of it |
| `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py -q -p no:xdist` | exit 0, `222 passed` |
| The sentence "In that release, ..." deleted from `agents/crafter.md` through `Edit`, then `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py -k crafters_fix_pass -q -p no:xdist` | exit 1, the fix-pass rule lost that sentence |
| The paragraph put back to its `2c7ba65a` text through `Edit` (`git diff --stat 2c7ba65a -- agents/crafter.md` empty), the same command, then the HEAD text restored through `Edit` | exit 1, the fix-pass rule lost the first new entry; `git status --short` empty after the restore |
| `uvx ruff check` and `uvx ruff format --check` over the test file | exit 0 and exit 0 |
| `git grep -n -i 'paste-ready' -- skills docs agents README.md README.ko.md templates` | the axes stated only at `agents/crafter.md:168` |
| `git grep -n '^## Rule changes' -- templates`, `git grep -c 'Rule changes' -- skills/settle/SKILL.md` | `templates/records/sdd-design.md:23`; 5 |
| `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6520356879` | a comment of 2026-10-30 on #1148 that opens "A recurring problem in this run, and the prevention home it gets" |

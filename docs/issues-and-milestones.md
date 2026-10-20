# Issues and milestones

What the issue tracker's fields mean here, and which of them anything reads.
`docs/branch-and-release.md` owns the merge rules, `docs/the-review-record.md`
the round cap, and this document the tracker's conventions.

## A milestone answers *when*, and takes three shapes

**A milestone answers *when* and never a release's size, which is decided by
what has to be in effect before the next work item starts.**

| Prefix | Holds | Ends |
|---|---|---|
| `release:` | the work going out in that version | closed when the version ships |
| `backlog:` | work with no release yet, bucketed by area | closed when the area is empty |
| `log:` | **not work**: a record that is kept rather than finished | never closed |

`release:` milestones carry the version's release date as their due date, and
are closed when the release reaches `main`. An open milestone with a past due
date reads as overdue, which is the tracker's way of saying a release shipped
and nobody closed its milestone.

**A release is sized by what has to be in effect before the next work item
starts, and not by a count.** One change that decides how the next ticket runs
is a release on its own. The release that shipped the framer carried a single
work item, because the agent that writes a frame had to exist before anything
was framed; the release that replaced the deleted checklist with a gate carried
two, because the next work item had to start with the replacement in effect.
Neither was cut short of a target. Both are named rather than numbered, so
the description reads the same on every release.

**Three or four is a ceiling, not a target.** It is as much as one section can
describe while a reader still comes away knowing what the release is about, and
it says nothing about when to stop under it. The count is in work items rather
than in ticket numbers, because one branch's leftovers arrive as several
ticket numbers that a reader counts as several releases' worth of work. Size a
ticket set that will be one branch as one item.

**What the criterion does not change.** It decides a release's size and nothing
else. A `release:` milestone is still the pool a release is cut from rather than
the release itself, `backlog:` below is still the unscheduled pool, and nothing
schedules from either: the one thing that reads a milestone checks a cut
release against its pool and never decides what goes into one.

`backlog:` is the unscheduled pool, and an issue leaves it in one act: the
milestone changes. **A scheduled release milestone's description states the
release's purpose and the grounds for the order its issues sit in**, and
grounds belonging to one ticket sit on that ticket. So "what is in 1.2.3, and
why in that order" is answered without opening a file. The number is
illustrative, for the reason *A rolling log is titled after the version it
rolled from* gives below.

`log:` is the shape that surprises people, and there is one of it:
`log: measurement`. What it holds are not tasks. `#51` is the durable
performance log whose body is the current state, and the open
`flow-measurement` issue is this version's rolling log. Neither has a done
condition, so neither closes, so the milestone does not either.
check: tests/test_a_release_is_sized_by_a_criterion.py

## A label answers *what it is about*, and survives the move

GitHub gives an issue one milestone. That field is spent on *when*, so a
concern that outlives a schedule needs a label instead: `measurement` is
carried by `#51`, by the rolling log, and by the scheduled work that came out
of them, whichever milestone each one sits in. Query the concern by label and
the release by milestone; neither substitutes for the other.

**`from-review` marks an issue a review round filed.** A round that hands a
finding to the tracker puts it on the new issue, and nothing reads the label;
it exists for one query. `--label from-review --state all` beside
`--state closed` gives the share of filed findings anybody went on to act on,
and that share is why the filing decision is a ladder rather than a reflex.
**Quote the date with the number.** The label set moves, so a share written
without its as-of date goes false quietly, and a reader re-taking the query
cannot tell which of the two changed.
`docs/the-review-record.md` *The run* owns where a filed finding goes; this
section owns what the label means.

**`flow-measurement` is a label that is not an index.** It is a lookup key,
and it carries an invariant: *exactly one open at a time*.
`.github/scripts/roll_flow_measurement_issue.py` closes the current one and
opens the next on a push to `main`, and **only where a new version has
shipped** since the open log opened; it fails loudly on zero or on two
rather than guessing which is current. The workflow fires on every push to
the default branch, so a push that moved no version, a re-run of the job or
a merge that shipped nothing, rolls nothing and says so in the job log.
**A log rolled with no comment on it is said so in three places**: the close
comment on the old log, the new log's body, and the job's output. The release
ships anyway: the count is read off the list call the roll already makes, so a
release is never held for bookkeeping about a release, and a count the
listing could not answer rolls the log and says the count was unreadable.
`skills/verify/SKILL.md` finds the log to post a segment's measurement to by
that key. Reading `--label flow-measurement --state all` finds the rolling
logs and misses `#51`; reading `--label measurement` finds everything and
answers no lookup.
check: tests/test_a_release_rolls_the_flow_measurement_issue.py

**A rolling log is titled after the version it rolled from**, in the form
`chore: flow measurement — after 1.2.3`. That log opened at the 1.2.3
release, holds the measurements taken since, and is closed by whatever ships
next. The number here is illustrative on purpose: a real version written
into a loaded file is what
`test_no_loaded_file_names_a_version_at_or_above_the_running_one` refuses,
at or above the running one and not yet tagged, whether that is the version
being cut or one still ahead of it. **A version below the running one, or one
this repository has tagged, is history and is kept**, which is what lets this
document say which release an issue shipped in. The tag decides, never the
changelog: the preparation commit bumps the running version and writes its
heading in the same commit, so until the next bump the running version is one
that has already shipped, and only its tag says so.
The version in the title is a fact rather than a prediction:
`docs/branch-and-release.md` says whether the next number is a minor or a
patch is known at the end and not at the cut, so at the moment the roll runs
the next version is the one thing nobody can name.

**A title that does not begin with `chore: flow measurement — after ` is not
one the roll wrote, and the roll reads it as due.** The whole of that prefix
is what the roll writes, and the whole of it is what the roll requires, from
the first character of the title. A title carrying those words somewhere
inside it, `docs: explain flow measurement — after 1.2.3`, is not one of these
logs, and reading a version out of it would leave that log never due. A
title of the older form names the version its log was predicted to be *for*,
not the one it rolled from. A log titled another way is **not rewritten**: a
retitle would falsify every comment that cites it. Because a title the roll
cannot read as its own is due rather than silent, the first release after it
rolls it.

**`size: now` says this ticket has to be in effect before the next work item
starts.** It is where the sizing judgment above is written down, so the next
release is cut without re-reading every open issue body. Two states and no
more: a ticket carries it or it does not, and not carrying it means the ticket
rides the next release that happens to carry it. There is no second level and
no scale, because the sizing question has two answers and a taxonomy with four
levels is one nobody maintains.

**The prefix is what keeps it inside the rule this section opens with.** A
label answers *what it is about*, and this one is about sizing, a concern that
outlives every schedule, since every release is sized. What the release spends
is the value, `now`, and not the subject. Two states means the subject never
appears on the tracker carrying a second value, so a spent label is removed
whole rather than re-valued. So the subject sits in the prefix and the verdict
in the value, which is the shape `chain: capped` already has here, and
`flow-measurement` above stays the one label that is not a topic at all. A
bare `now` would be a schedule answer with no subject, and it reads as the
ordinary adverb.

**Nothing schedules from this label**: no workflow, no check and no script
reads it to decide what happens next, so a stale one costs a reader a wrong
answer about what has to go next and costs no automation anything.

**One thing reads it, and only to spend it.**
`.github/workflows/close-issues-on-release.yml` removes `size: now` from each
issue it closes when the release reaches `main`. The removal rides the close
rather than preceding it, so a label write that fails cannot cost an issue its
close.

**The judgment is made at filing, and again when an issue moves milestone.**
Those are the two moments somebody is already reading the body, which is the
whole argument for the label: the reading is cheap while it is happening
anyway and expensive when it has to be repeated from scratch at a cut. A
ticket filed without it is not a ticket judged *not now*: it is one nobody
has judged, and the absence reads the same either way, which is the price of
two states.

**No sweep of the standing backlog is owed, and none should be done.** The
judgment is cheap at filing and expensive in a batch; a sweep is the batch,
performed once, by the very party the label exists to spare. An old ticket
gets the label the next time somebody opens it for another reason.
**`merged: X.Y.Z` goes on earlier inside that same release**, at the squash
onto the release branch: *A label says a ticket is already in, before the
release ships* is that mechanism. It answers *is this in yet* while the
release is being assembled; this one is spent only once the work is out. A
label is the right home for the judgment for exactly that reason: it makes
the answer durable without making it a gate anybody has to satisfy.

**What it does not decide is which release the ticket lands in.** The criterion
answers *now or not now*; ordinary scheduling answers the rest, and a ticket
without the label can still be the next thing somebody picks up.
check: tests/test_a_release_rolls_the_flow_measurement_issue.py

## Closing one of these by hand breaks the next release

The invariant above is what makes `log: measurement` dangerous to tidy. A
milestone holding two issues that never close looks exactly like a milestone
somebody abandoned. **Closing the open `flow-measurement` issue leaves zero
open, and the next release fails on it**, which is the loud failure working
as designed, at the worst possible moment.

If a `log:` issue has been closed, reopen it rather than opening a new one:
two open ones fail the same check from the other side.

## One thing reads a milestone, and it can stop a release

`.github/scripts/release_completeness_check.py` runs on a pull request from
`release/vX.Y.Z` into `main` and reads the milestone `release: X.Y.Z`. It
**refuses the release** while that milestone holds an open issue the release
branch does not carry, and names each one. So a milestone left holding next
quarter's work produces a red release pull request, at the moment the release
is being cut, which is the worst moment to do the scheduling it is asking for.
`docs/release-checklist.md` *0. Before starting* is where that act belongs:
the box asking whether the milestone holds what the release is carrying is
ticked before any of the release's cost is paid.

What the gate compares the milestone against is the pull request bodies. It
reads the release branch's own commit subjects, takes the `(#N)` a squash
writes, fetches those bodies, and collects what their closing keywords name:
the same readers `.github/scripts/close_issues_on_release.py` uses to close
them when the release reaches `main`, imported rather than copied.
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket* says the same thing from the ticket's side.

**A missing `Closes #N` costs an issue that stays open, and something reports
it.** An issue nobody claimed is in the milestone and never enters what the
release carries, so it is indistinguishable from work that was never built,
and the release is refused until somebody writes the keyword, moves the
issue, or builds it. The failure lands on the release rather than on the work
item that caused it.

## A label says a ticket is already in, before the release ships

**An issue a pull request into a release branch claimed carries
`merged: X.Y.Z` before the release ships.**
An issue's state does not move until `main` moves, and `main` moves once per
release. Without the label, for the length of a release a finished work item
and one nobody has started look identical on the tracker.

`.github/scripts/label_merged_on_release_branch.py` runs on a push to
`release/*` and puts `merged: X.Y.Z` on every issue the arriving pull
requests claimed, creating the label the first time. One query answers *what
is already in*: `gh issue list --milestone "release: X.Y.Z"`, and the merged
ones carry the label.

Three things about it are worth knowing before anyone tidies it.

- **It never closes anything.** An issue closed at the release-branch merge
  is closed for something nobody has received; the close stays on `main`.
- **The labels accumulate and are never removed**, one per release. Deleting
  one deletes it from every issue that ever carried it, which falsifies the
  record it was created to leave.
- **A label is a cache and the commits are the truth.** The gate above
  recomputes what the release carries from the branch itself and never asks
  the labels, so a label write that failed cannot block a release. It does
  compare the two and says which way they disagree: a label naming a release
  the issue is not in **fails**, because that is always a hand-edit or a
  squash subject that lost its `(#N)` and one command repairs it, while a
  missing label only **reports**, because a release must not be held for a
  failure of the signal rather than of its contents.

check: tests/test_a_merged_ticket_says_so_on_the_tracker.py

## A keyword claims the one number after it

**A closing keyword claims the one number after it.**
`Closes #153 and #150` claims #153. The second number carries no keyword of
its own, so nothing reads it as a claim: not GitHub, and not the script
above, whose own comment says `Closes #1, #2` is not read as two either.

**Write the keyword in front of every number**: `closes #153 and closes #150`.

The hygiene workflow reports the split on every pull request.
`.github/scripts/issue_claims_check.py` prints every issue the body claims,
every one it merely mentions, and a warning for any sentence that claims one
number and names another beside it. It reports and never fails, so the
correction is the author's to make while the pull request is open. A body
quoting the failing shape inside a fence or a code span, the way this section
does, is not an instance of it.

The prose around those spans keeps its keywords out for the same reason. A
past-tense narrative keyword is still a keyword, so a sentence that used one
with a second number beside it would earn the warning like any body.
check: tests/test_a_body_naming_two_issues_claims_one.py

**A keyword inside a fence or a code span claims nothing, whatever the fence
or the span is made of.** A fence opens with backticks or tildes at any
indent and closes on its own delimiter; a span is one backtick or two.
Masking more closes fewer, and that is the safe direction: an issue left open
is visible and a re-run reaches it, while a wrong close is a false record.
Two shapes are still read as claims, each pinned by a case so a later
widening is a deliberate red: a four-space indented block, because this
repository's pull request bodies indent a bullet's continuation that way and
masking it would drop a real `Closes #N`, and an HTML comment, because
whether GitHub reads a keyword inside one is unmeasured.
`.github/scripts/issue_claims_check.py` imports the closer's two patterns
rather than spelling its own, so the check and the closer read one body the
same way.
check: tests/test_release_hygiene.py

## An issue is its body and its comments together

Corrections, measurements and improvements land as comments, and the question
a reader is answering, *what does this ticket now ask for*, is answered by
reading all of them and then judging.

What the body owes in return is that nobody has to **reconcile** it. A body
that contradicts a comment leaves the reader to work out which is current.
Two ways to pay it, and which one fits depends on whether the original text is
worth keeping:

- **Consolidate the body**, once the design is settled. The comments stay and
  are still part of the issue; what goes away is the need to cross-check four
  places to learn what the ticket asks for. #136 is the worked example.
- **Leave the body and open it with `> **Update <date>.**`**, naming what has
  moved since it was written. #30 is the worked example: the original design
  is preserved and the block says which two things below it have changed.

The exception is an issue that is a **log rather than a ticket**: `#51`
and the rolling `flow-measurement` log. There the body IS the current state
and is maintained: a better baseline replaces the table, an observation that
gets an answer is rewritten where it stands, and the comments are the evidence
a change was made on rather than the answer. `#51`'s own body says so at the
top, because the distinction is not guessable from the outside.

## An issue is titled like a commit

Same prefix vocabulary as commits and pull requests (`feat:`, `fix:`,
`docs:`, `chore:`, `test:`, `refactor:`, `perf:`), and the subject is the
**symptom**, not the classification.
`skills/commit-pr-convention/SKILL.md` is the authority for the vocabulary;
this is only the note that issues use it too.

```
good   chore: the round cap is a ceiling and has been spent like a budget
bad    Round cap improvements
```

## Reconstructing a missing milestone

The signal is the tag, not the branch. For a closed issue with no milestone,
find the pull request whose body names it with `Closes #N`, take that pull
request's merge commit, and read the **first tag that contains it**: that is
the release it shipped in.

A branch name is not that signal: the branch `release/v0.3.0` shipped as
0.2.0, and its own release pull request says so in its title. Where no pull
request names the issue at all, the close date against `CHANGELOG.md`'s
release dates is what is left, and it is a guess rather than a reading.

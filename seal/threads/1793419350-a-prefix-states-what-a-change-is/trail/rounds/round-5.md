# Review round 5: 1793419350-a-prefix-states-what-a-change-is

target: 9bd9acec, fixes 6c51a824..9bd9acec

This round reads the range `6c51a824..9bd9acec`, re-established with
`git log --oneline`: the fix commit `8793f1f7` (the skill and the
changelog fragment), the round 4 answers `d40bb24e`, and `9bd9acec`, the
orchestrator's fold of the frame, read as a unit of its own. Round 4's three
findings are each named below: finding 1 on a `reopens:` line, findings 2
and 3 on `confirms:` lines. Finding 2 below stands in the unit `9bd9acec`
wrote and takes a `regression:` line.

Facts carried from earlier rounds and not re-established: the release
check's coordinates (`judge_feat`, the early return, the step in
`hygiene.yml`), none of which is in this range; the shapes of `97e29b7a`
and `8cb58904`; and the list of six modules that read the skill, from
`frame/plan.md`'s phase 1 row. The six modules were run again
(`## Probes`). `agents/sealer.md` step 4 was opened again (`:84-92`), since
the sixth clarification cites it. No `seal/parity.md` is declared, so the
record names no original commit.

S10 was read for the sentences this range changed: the opening sentence
(`skills/commit-pr-convention/SKILL.md:118-119`), the `docs:` row (`:128`),
the behaviour clarification (`:138-144`), the fourth clarification
(`:146-149`), the sixth (`:156-159`) and the issue paragraph (`:161-164`).
Each has one reading. None states a decision procedure or claims that two
writers agree. The worked examples these sentences decide were read again
against them (`frame/design.md:76-95`), and each follows. Close cases that
two writers weigh differently are the frame's stated limit
(`frame/design.md:67-70`) and are not counted here. The skill's text holds.
Both findings are in the frame, which a crafter, the proofer and the sealer
read as the source the skill is built against.

## Findings

### 1. The frame's *Scope* item 1 still says text a party acts on is never `chore:`, after the fold removed the same sentence from *The classification*

severity: should
location: `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:30`
evidence: read `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:30`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:65`, `skills/commit-pr-convention/SKILL.md:138-144`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/plan.md:46`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/trail/rounds/round-3.md:52`, `agents/crafter.md:175-178`
verdict: open
reopens: round-4#1

The close holds in the skill and in the fragment, and does not hold in the
frame. Round 4's finding 1 named the frame among its locations, and the
class it reopened, round 3's finding 1, named *Scope* item 1 by its line
(`trail/rounds/round-3.md:52`).

Claimed (round 4's answer to finding 1): "`frame/design.md:83` still says
'never `docs:` and never `chore:`', and the orchestrator folds it". Claimed
(the subject of `9bd9acec`): the frame "points to the skill's guidance
instead of a copy round 4 left behind". Found: the fold removed the
sentence from *The classification*, and *Scope* item 1 (`:30`) still reads
"Text a party reads and acts on, such as a skill, an agent definition, a
template a party fills or a hook's message, is behaviour, so a change to it
is never `docs:` and never `chore:`." The skill (`:138-144`) gives `chore:`
two cases for such text, and the fold's own pointer paragraph (`:65`) says
the same. So the frame now says both things, five paragraphs apart.

This sentence is the one a later party reads as the frame's decision.
`frame/plan.md`'s phase 3 row (`:46`) delivers "*Scope* item 1 as reframed
after round 3". *Scope* item 1 sends its reader to *The classification* for
the rest, and *The classification* now sends that reader to the skill. A
sealer reading the design against the build finds the design saying "never
`chore:`" where the skill names two cases. `agents/crafter.md:175-178` asks
a fix pass to find every other place stating a rule it reworded, by
`git grep` on its words. That search finds `:30` (`## Probes`).

```markdown
In seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:30,
replace

so a change to it is never `docs:` and never `chore:`.

with

so a change to it is never `docs:`, and is `chore:` only as a work item's own records or as an effect a released change already decided.
```

answer:

### 2. The fold's pointer paragraph says every crafter's commit takes the pull request's kind, where the skill says so only of a commit that builds a rule stated in its own work item

severity: should
location: `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:65`
evidence: read `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:65`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:93`, `skills/commit-pr-convention/SKILL.md:129`, `skills/commit-pr-convention/SKILL.md:146-149`, `agents/crafter.md:158-161`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/plan.md:46`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/trail/rounds/round-4.md:197`
verdict: open
regression: round-4#3

The unit is the pointer paragraph `9bd9acec` wrote in place of *The
classification*'s copy (`frame/design.md:65`). `frame/plan.md`'s phase 3
row (`:46`) builds the fourth clarification as *The classification* stated
it, for a commit that builds a rule stated only in its own work item, and
`9bd9acec` restates it as "a crafter's commit takes the pull request's kind
on those grounds", a compression of round 4's answer to finding 3, which
opens "What a crafter's commit does instead" and then names the narrower
commit (`trail/rounds/round-4.md:197`).

The paragraph says the guidance "stands there once", in the skill, and then
restates three of its sentences. Two match the skill. The third does not.
The skill's fourth clarification (`skills/commit-pr-convention/SKILL.md:146-149`)
gives the pull request's kind to "a commit that builds" a rule stated only
in the change's own work item. The frame's worked example says the same,
"a build commit on a work item's branch after its frame" (`:93`). The
pointer paragraph widens it to every commit a crafter makes.

The two readings part on commits this branch already holds. A crafter
closes each phase with its record and commits it (`agents/crafter.md:158-161`).
A records-only commit is `chore:` by the skill's row
(`skills/commit-pr-convention/SKILL.md:129`), as `61c2a935`, phase 3's
record, is titled. By the pointer paragraph it takes this pull request's
`feat:`. The paragraph also narrows the rule: where `routing.md` answers
`Implementation` with `the session`, the orchestrator writes the build
commit, and the skill's sentence names no party.

```markdown
In seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:65,
replace

a crafter's commit takes the pull request's kind on those grounds

with

a commit that builds a rule stated only in its own work item takes the pull request's kind on those grounds
```

answer:

## Confirmations

confirms: round-4#2
The `docs:` row reads "text people read and no party acts on", with the
examples "a README, its install steps among them; a comment"
(`skills/commit-pr-convention/SKILL.md:128`). The line is drawn at a party,
the word the behaviour clarification uses (`:138`). The two README worked
examples (`frame/design.md:88`, `:90`) and the branch example
`docs/the-readme-says-how-to-install` (`:295`) are `docs:` by the row. A
settle writes the policy documents, which a party acts on, so it is not
`docs:`, and the settle examples (`frame/design.md:86-87`) stay `chore:` and
the rewrite's kind. The fragment (`changelog.md:7`) and the fold's pointer
paragraph (`frame/design.md:65`) say the same. The frame's old row is gone
with the copy. Read.

confirms: round-4#3
The opening sentence (`skills/commit-pr-convention/SKILL.md:118-119`) no
longer asks the writer for grounds. The sixth clarification (`:156-159`)
names the orchestrator and the one place grounds go, its part of the body,
which *Pull request bodies* asks for (`:250-251`). `agents/sealer.md` step 4
reads that part against the design and the build (`:84-92`). The fourth
clarification (`:146-149`) gives a commit that builds its work item's rule
the pull request's kind and the orchestrator's grounds, so a crafter states
none of its own. The issue paragraph (`:161-164`) names the orchestrator
and the moment, when it titles the pull request. The `## Rule changes` text
for `docs/issues-and-milestones.md` (`frame/design.md:166`) now says the
same. The fragment says all three (`changelog.md:7`). The skill's text
holds; finding 2 is in the fold's summary of it, not in the skill. Read.

confirms: none
The behaviour clarification `8793f1f7` wrote
(`skills/commit-pr-convention/SKILL.md:138-144`) has one reading. Its head
names text a party reads and acts on, with the four kinds as examples, so
the policy documents a settle writes are inside its scope. Its two `chore:`
cases name the paragraph that governs each: the records fall under the
second clarification, and the settle under *An effect is counted once*
(`:151-154`). Worked examples "a settle that writes released rule changes
only", "a work item's records alone" and "a settle that also rewrites
guidance no released work item decided" (`frame/design.md:83`, `:86-87`)
follow. The fix pass's departure from round 4's paste-ready text is the
reading round 4's finding 1 asked for. Read.

confirms: none
Round 4's answer to finding 1 corrects round 3's answer on the fragment.
Round 4 quoted `changelog.md:7` at `6c51a824` as "never `docs:` and never
`chore:`", and the entry at `9bd9acec` gives the two cases. Read.

confirms: none
`9bd9acec`'s other sentences in its pointer paragraph match the skill: text
a party acts on is never `docs:` and is `chore:` in the two cases; `docs:`
is text no party acts on; the orchestrator states the grounds and retitles
the issue (`frame/design.md:65`). The cells of *Round 3's findings under
this design* (`:103-107`) and the `## Removes` row (`:187`) that cite
*The classification*'s clarifications by number now resolve only through
the pointer, to the skill's paragraphs in the same order. They describe
where a sentence sits, and are no finding. Read.

confirms: none
The six modules that read the skill pass at `9bd9acec`, 189 passed, the
count the fix pass reported. Executed (`## Probes`).

confirms: none
The broad gate's label is honest. `gaps.md` *Not verified* lists the full
suite, the repository-wide lint and the format at this branch's head after
`release/v0.26.0` is merged in, with the orchestrator answering. This round
leaves two findings open, both one-phrase edits to the frame, so the next
act is their fix and a verifying round over it, not the broad run. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The fix pass's run of the round-record readers, 2,220 passed. This round ran the six modules that read the skill and not that set | `trail/rounds/round-4.md` | the orchestrator, by `seal gate` |
| The grounds sentence of this work's own pull request body, which S10 gives the sealer | the pull request body, not yet written | the sealer, at its seal |
| The core sentence that the release check's comment on `FEAT` cites, on #1167's branch | `.github/scripts/release_completeness_check.py` | the orchestrator, at the merge of `release/v0.26.0` into this branch |
| The renamed step and its `::error::` line on a real release pull request into `main` | `.github/workflows/hygiene.yml` | the orchestrator, at the release pull request |

## Probes

| Command | Result |
|---|---|
| `git log --oneline origin/release/v0.26.0..HEAD`, its first four lines | `9bd9acec`, `d40bb24e`, `8793f1f7`, then `6c51a824` |
| `git diff --stat 6c51a824..9bd9acec` | four files: `changelog.md`, `frame/design.md`, `trail/rounds/round-4.md`, `skills/commit-pr-convention/SKILL.md` |
| `bin/test -q -p no:xdist` over the six modules that name `commit-pr-convention` | exit 0, 189 passed |
| `git grep -n -E "never .docs:. and never .chore:"` | `frame/design.md:30`, and three round-record lines |
| `git grep -n "crafter's commit"` | `frame/design.md:65`, and one round-record line |
| `git log --format=%s -1 61c2a935` | `chore: close #1199's phase 3: its phase record, closing memo rows and Status cell` |

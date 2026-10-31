# Review round 3: 1793419350-a-prefix-states-what-a-change-is

target: 5b6dc48f, fixes 0febac0b..5b6dc48f

This round reads the range `0febac0b..5b6dc48f`: the reframe `fec2a3cc`,
phase 2's build `05b716f7` and its records `f746b6f2`, and `5b6dc48f`, the
orchestrator's fold of *Scope* item 1, read as a unit of its own. The range
was re-established with `git log --oneline`. Phase 2 is a build, so a defect
in what it wrote is new work and takes no `regression:` line. Each of round
2's three findings is answered by the reframe and is named below: finding 2
on a `confirms:` line, findings 1 and 3 on `reopens:` lines. Facts carried
from round 2 and not re-established: the release check's coordinates
(`judge_feat`, the early return, the step in `hygiene.yml`), none of which
is in this range. The shapes of `97e29b7a` and `8cb58904` and the six modules
that read the skill were run again (`## Probes`). The core sentence that the
release check's comment cites is on #1167's branch, and no finding counts
its absence. No `seal/parity.md` is declared, so the record names no
original commit.

S10 was run as a writer runs it: each case read against
`skills/commit-pr-convention/SKILL.md:113-167` at `5b6dc48f`, every
paragraph of the section taken as binding. The crafter claimed all twelve
hold (`trail/phases/phase-2.md:14`, read, not a case). Six give one prefix.
Five carry a work item's records and split on finding 1, and one splits on
finding 4. Rows 13 to 17 are cases the frame did not run.

| # | Case | The frame's prefix | This round's reading |
|---|---|---|---|
| 1 | #1167 | `feat:` | holds: items 11 and 12 are `feat:` parts, and no part ranks higher |
| 2 | #1198 | `feat:` | holds |
| 3 | #1199, this work | `feat:` | holds for the pull request; the build commit `05b716f7` took `fix:` by the table (finding 5) |
| 4 | a test with the fix it pins | `fix:` | holds as the frame states it, with no records |
| 5 | a dependency bump that changes nothing met, with its records | `chore:` | two readings: `chore:` by the row, above `chore:` by `:151-156` (finding 1) |
| 6 | a work item's records alone | `chore:` | two readings (finding 1) |
| 7 | a speed-up with its case and its records | `perf:` | two readings: `perf:` by the row and `:136-142`, `refactor:` or higher by `:151-156` (finding 1) |
| 8 | a test change with `.test_durations` and its records | `test:` | two readings (finding 1) |
| 9 | a settle that writes released rule changes only | `chore:` | holds (`:158-161`) |
| 10 | a settle that also rewrites guidance no released work item decided | the rewrite's kind | holds (`:161-165`) |
| 11 | a README edit with its changelog fragment | `docs:` | two readings (finding 1) |
| 12 | a case that refuses, added to the suite alone | `test:` | two readings: `test:` by the row, `feat:` or `fix:` by "a gate" at `:151-152` (finding 4) |
| 13 | a README edit with the case that pins its words | none | `docs:` by `frame/design.md:79`, `test:` by the skill's order (finding 2) |
| 14 | a gate removed with nothing in its place, or an unused skill removed | none | no row fits; `chore:`, `refactor:` or `fix:` (finding 3) |
| 15 | a build commit on a work item's branch, after its frame | none | `fix:` by the crafter's reading of `:144-145`, `feat:` by the frame's case 3 (finding 5) |
| 16 | a dependency bump that corrects a defect users met | none | holds: `fix:`, by its effect |
| 17 | a skill's section moved to another file, its instructions unchanged | none | holds: `refactor:` |

## Findings

### 1. A work item's records are `chore:` by the row and never `chore:` by the behaviour paragraph, so every case that carries records gives two prefixes

severity: should
location: `skills/commit-pr-convention/SKILL.md:151-156`, `skills/commit-pr-convention/SKILL.md:134`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:30`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/changelog.md:7`
evidence: read `skills/commit-pr-convention/SKILL.md:134-156`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:30`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/trail/phases/phase-2.md:9`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/changelog.md:7`
verdict: fixed b63534ef
reopens: round-2#3

The close does not hold for the records. Round 2's finding 3 asked that
*Scope* item 1 give `chore:` the two cases the skill gave it, a work item's
own records and the settle, and its paste-ready text named both. The
reframe kept the settle, as a part whose effect a released change already
decided. It dropped the records.

The skill's behaviour paragraph (`:151-156`) says text a party reads and
acts on is behaviour. A part that changes it is `feat:`, `fix:`, `perf:` or
`refactor:`, and `chore:` "only where a released change already decided its
effect". A work item's records are such text: the crafter builds against
the frame, and the fix pass answers the round record. The `chore:` row says
so itself, "which only its parties read" (`:134`). The crafter's departure 3
says the same (`trail/phases/phase-2.md:9`): "a change a party acts on" takes
in a work item's own records. The departure moved that wording out of the
"Apart from that" clause and left the same scope in the paragraph's head,
"Text a party reads and acts on". No released change decided what an
unreleased work item's records do. So the paragraph refuses `chore:` to the
part the row calls `chore:`.

Claimed (the subject of `5b6dc48f`, and the note at `frame/design.md:30`):
*Scope* item 1 now stands "without the contradiction it found". Found: the
contradiction stands at the records, in the frame and in the skill alike.

This is round 2's finding 1 in another place. A writer who applies the
behaviour paragraph gives the records part `refactor:` or `feat:`. Either
outranks `perf:`, `test:`, `docs:` and `chore:`, so the records decide the
prefix of cases 5, 6, 7, 8 and 11 above. The changelog fragment states it
more plainly (`changelog.md:7`): "a part that changes one is `feat:`,
`fix:`, `perf:` or `refactor:`, never `docs:`", with no `chore:` case at
all, and two sentences later it calls a settle `chore:`.

```markdown
In skills/commit-pr-convention/SKILL.md, the paragraph at :151-156:

**Text a party reads and acts on is behaviour, and so are a check outside
the tests, a gate, a record's shape and a process step.** A skill, an agent
definition, a template a party fills and a hook's message are such text. A
part that changes any of them is `feat:`, `fix:`, `perf:` or `refactor:`,
never `docs:`. It is `chore:` in two cases only, both in the `chore:` row: a
work item's own records, which only its parties read and which leave with
it, and a part whose effect a released change already decided, as the next
paragraph says.

In frame/design.md Scope item 1, replace "never `docs:`, and `chore:` only
where a released change already decided its effect and was titled for it"
with:

never `docs:`, and `chore:` only as a work item's own records, or where a
released change already decided its effect and was titled for it

In changelog.md, replace "a part that changes one is `feat:`, `fix:`,
`perf:` or `refactor:`, never `docs:`." with:

a part that changes one is `feat:`, `fix:`, `perf:` or `refactor:`, never
`docs:`, and `chore:` only as a work item's own records or where a released
change already decided its effect.
```

answer: Absorbed by phase 3's rewrite, as `frame/design.md` *Round 3's findings under this design* row 1 says; the paste-ready fix was not applied. The paragraph at `:151-156` is gone. The third clarification of *Commit messages* says a change to text a party acts on is never `docs:` and never `chore:`, and leaves a work item's own records to the second clarification, under which a change's own tests and records never decide its prefix. The `chore:` row's example names a work item's records committed alone. `changelog.md`'s `### Changed` entry was rewritten in the same commit and no longer says "never `docs:`" without the records. `frame/design.md:30` was rewritten by the reframe at ee035d00, not by this commit.

### 2. A `docs:` change that carries the case pinning its words takes `test:`, so its own test decides its prefix

severity: should
location: `skills/commit-pr-convention/SKILL.md:132-142`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:75-79`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/changelog.md:7`
evidence: read `skills/commit-pr-convention/SKILL.md:126-142`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:69-79`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/trail/phases/phase-2.md:5-10`
verdict: fixed b63534ef
reopens: round-2#1

The close holds for every kind above `test:` and fails for `docs:`. Round
2's finding 1 asked that a change's own tests and records never be the part
that decides its prefix, and it named a README edit among the instances.
Under the per-part rule, `perf:`, `fix:`, `refactor:` and `feat:` each keep
their prefix when they carry their case. `docs:` stands below `test:`
(`:132-133`). A README edit with the case that pins its words has a `docs:`
part and a `test:` part, and the order gives it `test:`. In this repository a
document's words are often pinned by a case under `tests/text/`, so the
shape is common.

The frame gives the other answer. `frame/design.md:79` says a part's tests
and records "never decide the prefix of a change that has another part".
The crafter's departure 4 (`trail/phases/phase-2.md:10`) changed the clause
to "a change that holds a part someone meets", on the ground that the
frame's order puts `test:` above `docs:`. Claimed (`phase-2.md:5`): the six
departures are "each in the wording and none in a case's answer". Found:
departure 4 moves this case from `docs:` (the frame's `:79`) to `test:` (the
skill). The fold `5b6dc48f` reached *Scope* item 1 only, so the frame's
`:79` still states the old answer beside a skill that states the new one.

The skill's own text splits the same way. Its ranking principle (`:137-139`)
is "how much of what is met changes", and its `docs:` row names a README,
which a user reads and installs by. The next sentence counts `docs:` among
"the three kinds nobody outside the change meets". A writer who takes a
README as met reads `:140-142` as keeping the case from deciding, and gives
`docs:`. A writer who takes the order gives `test:`.

Placing `docs:` above `test:` makes the order agree with the frame's
sentence. It changes no answer among the twelve: case 8 stays `test:`, case
11 `docs:` and case 12 `test:`.

```markdown
In skills/commit-pr-convention/SKILL.md, swap the two rows at :132-133:

| `docs:` | text read and acted on by nobody: an explanation, a README, a comment |
| `test:` | nothing outside the suite: a case added, removed or corrected; a suite is how a contributor checks a change, and no user or party outside it meets a case |

and in the paragraph at :136-142, replace from "something done another way"
to the end with:

something done another way, then text nobody acts on, then the two kinds
nobody outside the change meets. A part's tests and its work item's records
are `test:` and `chore:` parts, the two lowest kinds, so they never decide the
prefix of a change that has another part.

In frame/design.md, swap the `test:` and `docs:` rows at :75-76 the same way,
and in :79 replace "then the three kinds nobody outside the change meets"
with "then text nobody acts on, then the two kinds nobody outside the change
meets".

In changelog.md, the order reads `feat:`, `fix:`, `perf:`, `refactor:`,
`docs:`, `test:`, `chore:`.
```

answer: Absorbed by phase 3's rewrite, as `frame/design.md` *Round 3's findings under this design* row 2 says; the row swap in the paste-ready fix was not applied. The second clarification says a change's own tests and its work item's records never decide its prefix, and gives a README edit with the case that pins its words as `docs:`. The table keeps `test:` above `docs:`, and the precedence clarification acts only where a change does more than one of these, which the second clarification keeps its own case from counting toward. `changelog.md` states the README example in the same commit. `frame/design.md:75-79` was rewritten by the reframe at ee035d00, not by this commit.

### 3. A part that takes something away fits no row, so a removed gate or an unused skill removed gets three prefixes

severity: should
location: `skills/commit-pr-convention/SKILL.md:131`, `skills/commit-pr-convention/SKILL.md:118-124`
evidence: executed `git log origin/main --no-merges --format='%h %s' | grep -i -E ' (remov|drop|retire|delete)'`
verdict: fixed b63534ef

The skill says each part has one kind and the answers exclude one another
(`:118-124`). Each row describes what is met after the merge: something new,
something corrected, the same sooner, the same reached another way, or
nothing. A part that takes away something a user or a party met fits none
of them. Two shapes this repository makes often are a gate removed because
what it caught did not outweigh its cost (`skills/core/SKILL.md` *The rule a
mechanism is kept against*), with nothing in its place, and a skill nobody
used, removed. The search over `main` finds `e391ea04` ("eight unused skills
are removed"), `ed31ee55` (the worktree guard's keep, narrow or remove) and
`fd92215a` ("each is removed"), all titled `chore:` (executed).

Under the rewritten skill, `chore:` is a part through which "nothing" is met
(`:134`), and a removed skill a user could invoke is met. The `refactor:`
row's nearest words, "a script that stops refusing what an agent now reads"
(`:131`), need an agent that now reads it. So writers diverge. One keeps
`chore:` from the log, which the skill no longer lets decide a row
(`:175-181`). One takes `refactor:` from the frame, whose *#653* section says
"a refusal that loosens is `refactor:`" (`frame/design.md:150`, read). That
sentence did not reach the skill. One takes `fix:`, since the core's rule
stood in the tree and the mechanism now matches it. `fix:` and `refactor:`
are both patches, so the release reading is unaffected here. The rewrite
exists so that two writers reach one prefix, and here they reach three.

The fix carries the frame's own decision into the row. Whether removing a
command a user runs is also `refactor:`, or a `feat:` because it breaks
what the user did, the frame does not say. The fix pass routes that part to
the framer rather than choosing it.

```markdown
| `refactor:` | the same kinds of outcome, reached another way: which party holds a judgment, a script that stops refusing what an agent now reads, a refusal loosened or a mechanism removed with nothing in its place, a sequence rewritten as guidance, a structure moved; nothing is new, corrected or faster |
```

answer: Absorbed by phase 3's rewrite, as `frame/design.md` *Round 3's findings under this design* row 3 says, with the frame's judgment of the part this finding left open. The `refactor:` row's examples name a gate retired because what it caught did not outweigh its cost and a skill nobody used, removed. The `feat:` row's examples name a thing removed that its users must now work around, so a command its users ran, removed, is `feat:`, which answers this round's *Not judged* row on it (`frame/design.md` *Worked examples*). The claim at `:118-124` that the kinds exclude one another is gone.

### 4. "A gate" in the behaviour paragraph takes in a case the suite runs, so a refusing case added alone reads as `test:` or as `feat:` and `fix:`

severity: should
location: `skills/commit-pr-convention/SKILL.md:151-152`, `skills/commit-pr-convention/SKILL.md:132`
evidence: read `skills/commit-pr-convention/SKILL.md:121-132`, `skills/commit-pr-convention/SKILL.md:151-156`, `skills/core/SKILL.md:43`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/trail/phases/phase-2.md:9`
verdict: fixed b63534ef

The crafter's departure 3 (`trail/phases/phase-2.md:9`) says "outside the
tests" keeps a case added to the suite alone at `test:`. The words qualify
"a check" only. The same list goes on to "a gate". In this repository the
suite is part of the broad gate (`skills/core/SKILL.md:43`: "the suite, the
lint, the broad gate and the merge check"), and wherever a required CI job
runs the suite, a new case that refuses is what a later party's pull
request meets. The skill's question for a kind (`:121-123`) is what a party
working on a later change meets differently. The `test:` row answers it by
assertion: "no user or party outside it meets a case" (`:132`).

A writer who reads the row gives frame case 12 `test:`. A writer who reads
"a gate" at `:151-152` and asks the question gives `feat:` for a refusal on
a rule the change states, or `fix:` for a rule already stated. The frame
decided `test:` (`frame/design.md:102`), so the text should say so in the
place a writer reads it.

```markdown
In skills/commit-pr-convention/SKILL.md, the head of the paragraph at :151-152:

**Text a party reads and acts on is behaviour, and so are a check or a gate
outside the tests, a record's shape and a process step.**

and the `test:` row at :132:

| `test:` | nothing outside the suite: a case added, removed or corrected, even one that refuses where the suite gates the merge; a suite is how a contributor checks a change, and no user or party outside it meets a case |
```

answer: Absorbed by phase 3's rewrite, as `frame/design.md` *Round 3's findings under this design* row 4 says; the paste-ready fix was not applied. The third clarification names text a party reads and acts on and no gate or check. The `test:` row says nothing outside the repository's own tests is met, and its example is a case added or corrected, even one that refuses where the suite gates the merge, so frame case 12 is `test:` in the place a writer reads it.

### 5. The test between `feat:` and `fix:` does not say which base a commit on a work item's branch opens, and this branch's two build commits took two prefixes for one shape

severity: should
location: `skills/commit-pr-convention/SKILL.md:144-145`, `skills/commit-pr-convention/SKILL.md:128`
evidence: executed `git log --oneline f80f48e6..5b6dc48f`
verdict: fixed b63534ef

The test reads "whether the rule stood in the tree before the change, which
a reader answers by opening the base" (`:144-145`). The `feat:` row says "a
refusal on a rule this change states" (`:128`). Neither says what "the base"
and "this change" are for a commit that is one of several on a work item's
branch.

The crafter titled `05b716f7` `fix:`, because "the rule stood in the tree
before the commit": the frame at `fec2a3cc` stated it
(`trail/phases/phase-2.md:18`, read). The frame's case 3
(`frame/design.md:93`, read) gives the same part, "the prefix table's new
rule, which writers meet", `feat:`. Phase 1's build `c6ed2331`, written
against the frame committed at `9a0e06ea`, was titled `feat:` (executed).
Both are a build commit after its own frame, and they took two prefixes.

Read the crafter's way, every commit that builds what its own frame states
is `fix:`. In a repository that merges without squashing, the release then
sees no `feat:` for a feature built in phases, which is the defect #1199
exists for. Here the squash subject is the pull request's title, whose base
is the release branch, so the release check is not affected. The skill
ships to repositories that do not squash.

```markdown
The test between `feat:` and `fix:` is whether the rule stood in the tree
before the change, which a reader answers by opening the branch the change
merges into. A rule stated only in the change's own work item, such as its
frame on the same branch, is stated by the change and not by the tree, so a
commit that builds it reads the base its branch was cut from.
```

answer: Absorbed by phase 3's rewrite, as `frame/design.md` *Round 3's findings under this design* row 5 says; the paste-ready fix was not applied. The paragraph of tests between kinds at `:144-149` is gone, and the `feat:` row at `:128` is rewritten. The fourth clarification says "before the change" is the branch the change merges into, and that a rule stated only in the change's own work item, such as its frame, belongs to the change, so a commit that builds it takes the kind its pull request takes. This commit takes `feat:` by it. The limit the design names stands: `c6ed2331` `feat:` and `05b716f7` `fix:` keep their subjects, and the squash takes the pull request's title.

## Confirmations

confirms: round-2#2
The settle no longer has one answer grounded in a false description. The
`chore:` row no longer names the settle (`skills/commit-pr-convention/SKILL.md:134`).
*An effect is counted once, by the change that decided it* (`:158-167`)
gives a settle that writes released rule changes `chore:`, and a section it
rewrites that no released work item decided its own kind. The section it
cites, `skills/core/SKILL.md` *The first value: efficient development
through the workflow*, holds the rewrite sentence on this base
(`skills/core/SKILL.md:72-77`). Cases 9 and 10 each give one prefix. Read.

confirms: none
Phase 2's departures 1, 5 and 6 hold. (1) The release sentence of
`frame/design.md:79` would put a version map in a skill that ships to
repositories with their own versioning, which *Scope* item 1's last
sentence and `frame/plan.md` A7 forbid. (5) The table's header states the
question each row answers (`:126`). (6) The tests between kinds
(`:144-149`) keep the `feat:`/`refactor:` test and add the `fix:`/`refactor:`
and `perf:`/`refactor:` tests. Departures 2, 3 and 4 are findings 1, 4 and 2.
Read.

confirms: none
The crafter's claim that no case reads the table's rule holds. Six modules
name `commit-pr-convention`, and none reads the kinds or their order. No
case in `tests/` or `evals/` names "highest kind", "precedence among kinds"
or "counted once" for this skill. The six modules pass at `5b6dc48f`, 189
passed. Executed (`## Probes`). The rule is a judgment a writer applies, so
S10 is a reading, and this record labels it one.

confirms: none
No sentence outside the section still states the first-row rule. A search
for "first row that fits", "wholly of its kind", "Apart from those two" and
"the settle among it" outside `seal/threads/` finds nothing, and "never
`docs:` or `chore:`" survives only in round records and in the phase record
that quotes it. *First, check the title against the history* and *Before the
pull request opens* item 2 cite "the table in *Commit messages*", which
still reads true. Executed (`## Probes`).

confirms: none
The broad gate's label is honest. `gaps.md` *Not verified* lists the full
suite, the repository-wide lint and the format at this branch's head after
`release/v0.26.0` is merged in, with the orchestrator answering. This round
leaves five findings open, so the next act is their fix pass and a
verifying round, not the broad run. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The crafter's 82-module boundary set, 5,169 passed and 9 skipped. This round ran the six modules that read the skill and not the set | `trail/phases/phase-2.md` | the orchestrator, by `seal gate` |
| Whether a removed command a user runs is `refactor:` or `feat:`, which finding 3's fix leaves to the frame | `skills/commit-pr-convention/SKILL.md:131` | the orchestrator, routing finding 3 to the framer |
| The core sentence that the release check's comment on `FEAT` cites, on #1167's branch | `.github/scripts/release_completeness_check.py` | the orchestrator, at the merge of `release/v0.26.0` into this branch |
| The renamed step and its `::error::` line on a real release pull request into `main` | `.github/workflows/hygiene.yml` | the orchestrator, at the release pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the six modules that name `commit-pr-convention`, `-q -p no:xdist` | exit 0, 189 passed |
| `git grep -l "commit-pr-convention" -- tests evals` | the six modules and no other |
| `git grep -n -E "highest kind\|precedence among kinds\|counted once" -- tests evals` | three lines, none about this skill |
| `git grep -n -i -E "first row that fits\|wholly (of )?its kind\|Apart from those two\|the settle among it" -- ':!seal/threads'` | no match |
| `git grep -n -E "never .docs:. or .chore:.\|.chore:. is never a change"` outside the round records | `trail/phases/phase-2.md:8-9`, each quoting the old wording |
| `git show --stat 97e29b7a 8cb58904` | `97e29b7a`: hooks, `skills/evidence-check/`, one test module and its records; `8cb58904`: three test modules, `.test_durations` and its records |
| `git log origin/main --no-merges --format='%h %s' \| grep -i -E ' (remov\|drop\|retire\|delete)'` | removals titled `chore:` (`e391ea04`, `ed31ee55`, `fd92215a`, `475653e7`), `fix:`, `test:` and `feat:` |
| `git log --oneline f80f48e6..5b6dc48f` | `c6ed2331` titled `feat:` and `05b716f7` titled `fix:`, each a build after its frame |

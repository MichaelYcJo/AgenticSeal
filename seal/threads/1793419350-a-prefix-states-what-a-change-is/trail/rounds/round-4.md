# Review round 4: 1793419350-a-prefix-states-what-a-change-is

target: 20b013ae, fixes d171bc86..20b013ae

This round reads the range `d171bc86..20b013ae`, re-established with
`git log --oneline`: the closes of round 2 (`519b5433`, `c02dcc25`), the
reframe after round 3 (`ee035d00`), phase 3's build `b63534ef` and its
records `61c2a935`, the round 3 answers `bc0e3f99`, and `20b013ae`, the
orchestrator's fold of two frame sentences, read as a unit of its own. Phase
3 is a build, so a defect in a unit it wrote is new work and takes no
regression line. Round 3's five findings are each named below: finding 1
on a `reopens:` line, findings 2 to 5 on `confirms:` lines.

Facts carried from earlier rounds and not re-established: the release
check's coordinates (`judge_feat`, the early return, the step in
`hygiene.yml`), none of which is in this range, and the shape of
`8cb58904`. The shape of `97e29b7a` and the six modules that read the skill
were run again (`## Probes`). The core sentence that the release check's
comment cites is on #1167's branch, and no finding counts its absence. No
`seal/parity.md` is declared, so the record names no original commit.

S10 was read as the frame states it: each sentence of
`skills/commit-pr-convention/SKILL.md` *Commit messages* (`:113-176`) and the
new sentence of *Pull request bodies* (`:247-248`) at `20b013ae`, for one
reading each, for a decision procedure or a claim that two writers always
agree, and each row of `frame/design.md` *Worked examples* (`:97-116`)
against the text. No sentence claims that two writers agree, and none says
the kinds exclude one another (executed, `## Probes`). The precedence
paragraph (`:132-133`) is a rule over what the writer has already judged,
not a procedure for judging it. *Pull request bodies* asks the
orchestrator's part for one sentence of grounds (`:247-248`). Fifteen of the
eighteen worked examples follow from the text with one reading. Three do
not: the settle that writes released rule changes (finding 1) and the two
README edits (finding 2). Close cases where two writers weigh differently
are the frame's stated limit (`frame/design.md:88-91`) and are not counted
here.

## Findings

### 1. The behaviour clarification still refuses `chore:` to cases the `chore:` row and the counted-once clarification give `chore:`: the settle in the skill, and the records and the settle in the changelog

severity: should
location: `skills/commit-pr-convention/SKILL.md:139-142`, `skills/commit-pr-convention/SKILL.md:148-151`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/changelog.md:7`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:83`
evidence: read `skills/commit-pr-convention/SKILL.md:129-151`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/changelog.md:7`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:83-85`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:107`, `skills/code-review/SKILL.md:21-24`
verdict: fixed 8793f1f7
reopens: round-3#1

The close holds for the records in the skill and does not hold in the
changelog, one of the finding's four locations, nor for the second case of
the class the finding named. Round 3's finding 1 asked that the behaviour
paragraph give `chore:` its two cases, a work item's own records and a part
whose effect a released change already decided, and its paste-ready fix
named both, in the skill and in `changelog.md`.

Claimed (round 3's answer to finding 1): "`changelog.md`'s `### Changed`
entry was rewritten in the same commit and no longer says 'never `docs:`'
without the records." Found: `changelog.md:7` now reads "Text a party reads
and acts on, such as a skill, an agent definition, a template a party fills
or a hook's message, is behaviour, so a change to it is never `docs:` and
never `chore:`", with no case for the records. The same entry then calls "a
work item's records committed alone" and the settle `chore:`. That is the
contradiction round 3 found in the skill, now in the fragment a person reads
at the release.

In the skill the records are carved out (`:141-142`), but the settle is not.
The behaviour clarification (`:139`) opens with a general head, "Text a
party reads and acts on is behaviour", and says such a change is "never
`chore:`". A settle writes the policy documents, and the proofer reads those
first at stage 1 (`skills/code-review/SKILL.md:21-24`), so they are text a
party reads and acts on. The counted-once clarification (`:148-151`) and the
`chore:` row's example (`:130`) call that settle `chore:`. Phase 2's
paragraph reconciled the two with "and `chore:` only where a released
change already decided its effect, as the next paragraph says" (`d171bc86`,
`:155-156`). `b63534ef` dropped that clause and the frame's clarification
(`frame/design.md:83`) never had it. A writer who takes the head as general
gives the settle no `chore:`, and one who takes the four named kinds as the
whole scope gives it `chore:`. The worked example "a settle that writes
released rule changes only" (`frame/design.md:107`) follows from the second
reading only.

```markdown
In skills/commit-pr-convention/SKILL.md, the paragraph at :139-142:

**Text a party reads and acts on is behaviour**, so a change to a skill, an
agent definition, a template a party fills or a hook's message is never
`docs:`, and is `chore:` only where a released change decided its effect, as
the paragraph opening *An effect is counted once* says, while a work item's
own records, which describe their change and leave with it, fall under the
paragraph before this one.

In frame/design.md:83, replace "is never `docs:` and never `chore:`." with:

is never `docs:`, and is `chore:` only where a released change decided its
effect, as the next clarification says.

In changelog.md:7, replace "so a change to it is never `docs:` and never
`chore:`." with:

so a change to it is never `docs:`, and is `chore:` only where a released
change decided its effect, while a work item's own records never decide a
change's prefix.
```

answer: Holds, and round 3's answer to finding 1 was wrong about the fragment: `changelog.md:7` still said "never `docs:` and never `chore:`" with no case for the records. The behaviour clarification now names text a party reads and acts on, with the four kinds as examples, and says a change to it is never `docs:` and is `chore:` in two cases only: a work item's own records, which fall under the clarification before it, and an effect a released change already decided, such as a settle writing released rule changes, which *An effect is counted once* gives `chore:`. The fragment states the same two cases in the same commit. The paste-ready text was not applied as written: it made `chore:` a property of the four named kinds and left the policy text the settle writes outside the sentence's scope, which is the reading this finding refuses. Worked example "a settle that writes released rule changes only" now follows from one reading. `frame/design.md:83` still says "never `docs:` and never `chore:`", and the orchestrator folds it.

### 2. The `docs:` row says "text nobody acts on", where a user acts on a README's install steps, and the skill's own examples call a README edit `docs:`

severity: should
location: `skills/commit-pr-convention/SKILL.md:129`, `skills/commit-pr-convention/SKILL.md:135-137`, `skills/commit-pr-convention/SKILL.md:292`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:76`
evidence: read `skills/commit-pr-convention/SKILL.md:118-129`, `skills/commit-pr-convention/SKILL.md:135-142`, `skills/commit-pr-convention/SKILL.md:290-293`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:76`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:109-111`
verdict: fixed 8793f1f7

The unit is the `docs:` row `b63534ef` rewrote. The opening sentence
(`:118-120`) says whoever meets a change is "a user or a party working on a
later change", so the `docs:` row's "text nobody acts on" (`:129`) takes in
users. A README's install steps are text a user acts on. Read that way, a
README edit that changes how to install is not `docs:`, and a writer looks
higher: `feat:` for steps new to meet, which in this repository makes a
minor and pushes the milestones. The row's example narrows phase 2's "a
README" to "a README's explanation", which points the same way.

The rest of the skill reads the other way. The second clarification
(`:136-137`) calls "a README edit with the case that pins its words"
`docs:`, with no word on what the edit says. The branch-name example
`docs/the-readme-says-how-to-install` (`:292`) titles install steps
`docs:`. The worked examples "a README edit with its changelog fragment"
and "a README edit with the case that pins its words" (`frame/design.md:109`,
`:111`) give `docs:` to any README edit. They follow from the text only where
"nobody" means no party. The behaviour clarification (`:139`) draws its line
at a party, so the row that sits opposite it should say the same word.

The fix states the line the frame's examples already draw: users read
`docs:` text, and no party acts on it.

```markdown
In skills/commit-pr-convention/SKILL.md:129 and frame/design.md:76:

| `docs:` | text people read and no party acts on | a README, its install steps among them; a comment |
```

answer: Holds. The `docs:` row now reads "text people read and no party acts on", with the examples "a README, its install steps among them; a comment", the paste-ready row applied as written. The line is drawn at a party, the word the behaviour clarification uses, so a user acting on install steps does not lift a README edit out of `docs:`, and text a party acts on as part of its work, such as a skill or the policy documents, stays behaviour. Checked against every worked example: the two README edits (`frame/design.md:109`, `:111`) and the branch example `docs/the-readme-says-how-to-install` are `docs:` by the row; the settle examples are not `docs:`, because the policy documents are text a party acts on, and stay `chore:` or the rewrite's kind; no other example names a `docs:` change. The fragment's `docs:` sentence was rewritten in the same commit. `frame/design.md:76` still holds the old row, and the orchestrator folds it.

### 3. The opening and the grounds clarification give "the writer" a duty only the orchestrator can do, and the retitling sentence names nobody

severity: should
location: `skills/commit-pr-convention/SKILL.md:118-120`, `skills/commit-pr-convention/SKILL.md:153-156`, `skills/commit-pr-convention/SKILL.md:158-161`
evidence: read `skills/commit-pr-convention/SKILL.md:17-20`, `skills/commit-pr-convention/SKILL.md:118-161`, `skills/commit-pr-convention/SKILL.md:222-248`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/trail/phases/phase-3.md:16`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/plan.md:29`
verdict: fixed 8793f1f7

The units are the opening sentence and the sixth clarification `b63534ef`
wrote, and the half-sentence it added to the issue paragraph. The skill
defines "the writer" as whoever writes a commit, a pull request or a branch
name, the crafter or the orchestrator (`:17-20`). The opening says "the
writer states its grounds" for every prefix (`:118-120`), so it binds the
crafter at each commit. The sixth clarification (`:153-156`) then names the
one place grounds go, the orchestrator's part of the pull request body. The
crafter does not write that part, and a pull request outside the review
chain has no such part (`:222-224`). The frame asks for the grounds once,
in the orchestrator's part of every pull request body (`frame/plan.md:29`,
A20), not at each commit.

The two readings are already in this branch. Phase 3's crafter, the writer
of `b63534ef`, stated its commit's grounds in its phase record
(`trail/phases/phase-3.md:16`), a place the skill does not name. Read the
other way, a crafter states nothing, and the opening sentence is broken at
every commit.

The issue paragraph's new half (`:160-161`), "the issue is retitled where
the pull request takes a prefix other than the issue's", names no party and
no moment. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한
가지로만 읽히게 쓴다* asks a sentence that asks for an act to name who acts and
when. The crafter reads this file and posts nothing (contract rule 6), so
the orchestrator is the only party that can retitle, and the sentence should
say so.

```markdown
In skills/commit-pr-convention/SKILL.md:118-120:

**A prefix is the writer's judgment of what the change does for whoever
meets it after the merge, a user or a party working on a later change.**

At :153-156:

**The orchestrator states the grounds for a pull request's title** in its
part of the body, as *Pull request bodies* says, and `agents/sealer.md` step
4 reads that part against the design and the diff, so a prefix the change
does not bear out is a disagreement the sealer names.

At :158-161:

**An issue's title takes the prefix the pull request that closes it will
take**, chosen by this table, so no issue is filed `chore:` by default, and
where the pull request takes another prefix, the orchestrator retitles the
issue when it titles the pull request.
```

answer: Holds. The opening sentence drops "and the writer states its grounds", as the paste-ready text has it. The sixth clarification opens "The orchestrator states the grounds for a pull request's title", in its part of the body, as the paste-ready text has it. What a crafter's commit does instead is in the fourth clarification, which now ends "on the grounds the orchestrator states for that pull request", so a commit that builds its work item's rule takes its pull request's kind and states no grounds of its own. The issue paragraph now says that where the pull request takes a prefix other than the issue's, the orchestrator retitles the issue when it titles the pull request. The fragment says the same three things in the same commit. `trail/phases/phase-3.md:16` stays as a phase record of a decision made while building, which the skill no longer asks for and does not forbid; a fix pass writes no phase record. Stale in the frame, for the orchestrator to fold: `frame/design.md:65` "the writer states its grounds where a party reads them", `:67` the opening's "and the writer states its grounds", `:86` the sixth clarification's "The writer states the grounds" and "is retitled with it", and the `## Rule changes` text for `docs/issues-and-milestones.md`, "the issue is retitled when the pull request is", which names no actor.

## Confirmations

confirms: round-3#2
A README edit that carries the case pinning its words takes `docs:`. The
second clarification says a change's own tests and its work item's records
never decide its prefix, and names this case `docs:`
(`skills/commit-pr-convention/SKILL.md:135-137`). The precedence acts only on
what the change does (`:132-133`), so the case's `test:` is not weighed
against the README's `docs:`. `changelog.md:7` states the same example.
Finding 2 above is about which README edits are `docs:` at all, not about
the pinning case. Read.

confirms: round-3#3
A removal has a kind. The `refactor:` row's examples name a gate retired
because what it caught did not outweigh its cost and a skill nobody used,
removed, and the `feat:` row's examples name a thing removed that its users
must now work around (`skills/commit-pr-convention/SKILL.md:124`, `:127`).
The worked examples "a gate retired with nothing in its place" and "a
command users ran, removed" (`frame/design.md:112-113`) follow from the
rows. The claim that the kinds exclude one another is gone (`## Probes`).
The frame's judgment on a removed command answers round 3's *Not judged*
row on it. Read and executed.

confirms: round-3#4
A refusing case added to the suite alone is `test:`. The behaviour
clarification names text a party acts on and no gate or check (`:139-140`),
and the `test:` row's example says "a case added or corrected, even one
that refuses where the suite gates the merge" (`:128`). Worked example "a
case that refuses, added to the suite alone" (`frame/design.md:110`) follows.
Read.

confirms: round-3#5
"Before the change" now has one reading for a commit on a work item's
branch. The fourth clarification (`:144-146`) says it is the branch the
change merges into, and its second half settles the case round 3 found: a
rule stated only in the change's own work item belongs to the change, so a
commit that builds it takes the kind its pull request takes. The `fix:` row
uses the defined phrase (`:125`). The limit the frame names stands and is not
counted: `c6ed2331` and `05b716f7` keep their subjects, and the squash takes
the pull request's title. `b63534ef` takes `feat:` by this clarification.
Read.

confirms: none
Phase 3's four departures (`trail/phases/phase-3.md:7-10`). (1) The "release
reads any `feat:`" clause stays out of the skill: *Scope* item 1's last
sentence and `frame/plan.md` A7 keep the version map out of a skill that
ships to repositories with their own versioning, and `20b013ae` folds the
frame's precedence bullet to say so (`frame/design.md:81`). Holds. (2) The
sixth clarification split three ways: the grounds sentence stands once, in
*Pull request bodies* (`:247-248`), and the issue sentence joins the issue
paragraph, which removes "with it"'s two antecedents. Holds, apart from the
missing actor in finding 3. The frame still places the issue sentence in its
sixth clarification (`frame/design.md:86`) and the plan's phase 3 row still
says the issue paragraph stays (`frame/plan.md:46`); both describe where a
sentence sits, and the skill's meaning is the frame's, so neither is a
finding. (3) "The paragraph before this one" (`:142`) names the second
clarification, the paragraph that does stand before it, and reads one way
in the tree as it is. Holds. (4) The two framing sentences ("They are what
the writer weighs, not steps it executes") describe the skill rather than
give it text. The opening sentence states that the prefix is the writer's
judgment, which carries the same instruction. Holds. Read.

confirms: none
`20b013ae`, read as a unit. The precedence bullet (`frame/design.md:81`) now
matches the skill's sentence and says where the release's reading lives.
`frame/plan.md` A10 grounds #1167's `feat:` on the precedence clarification
instead of "the highest kind among its parts", the reframe after round 2's
words, which phase 3's record named as stale (`trail/phases/phase-3.md:18`).
The search for the replaced rule's words outside the work item's records
finds nothing (`## Probes`). Read and executed.

confirms: none
S8 and S9 hold. #1167's items 11 and 12 add a record section and a reading,
which the `feat:` row's "a record format" names, and the precedence gives
the change `feat:`; #1198 adds a record format and its commands, `feat:`. A
change to what a check outside the suite refuses is met by the next pull
request it refuses, so the `chore:` row's "changes nothing anyone meets"
cannot hold it, and the `feat:`, `fix:` and `refactor:` rows each name such
a change by example (`:124-127`). Read.

confirms: none
The six modules that read the skill pass at `20b013ae`, 189 passed, the
count the crafter reported (`trail/phases/phase-3.md:20`). The crafter's
claim that no case reads the guidance holds: none of the six reads the
kinds or the clarifications. Executed (`## Probes`).

confirms: none
The broad gate's label is honest. `gaps.md` *Not verified* lists the full
suite, the repository-wide lint and the format at this branch's head after
`release/v0.26.0` is merged in, with the orchestrator answering. This round
leaves three findings open, so the next act is their fix pass and a
verifying round, not the broad run. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The crafter's 81-module boundary set, 4,784 passed and 9 skipped, and the round-record readers, 2,220 passed. This round ran the six modules that read the skill and not those sets | `trail/phases/phase-3.md` | the orchestrator, by `seal gate` |
| The grounds sentence of this work's own pull request body, which S10 gives the sealer | the pull request body, not yet written | the sealer, at its seal |
| The core sentence that the release check's comment on `FEAT` cites, on #1167's branch | `.github/scripts/release_completeness_check.py` | the orchestrator, at the merge of `release/v0.26.0` into this branch |
| The renamed step and its `::error::` line on a real release pull request into `main` | `.github/workflows/hygiene.yml` | the orchestrator, at the release pull request |

## Probes

| Command | Result |
|---|---|
| `git log --oneline d171bc86..20b013ae` | seven commits: `519b5433`, `c02dcc25`, `ee035d00`, `b63534ef`, `61c2a935`, `bc0e3f99`, `20b013ae` |
| `bin/test -q -p no:xdist` over the six modules that name `commit-pr-convention` | exit 0, 189 passed |
| `git grep -n -i -E "highest kind\|exclude one another\|precedence among kinds\|each part of a change\|the test between .feat:\|first row that fits\|writes into the policy documents what" -- ':!seal/threads'` | no match |
| `git show d171bc86:skills/commit-pr-convention/SKILL.md`, lines 151-156 | phase 2's behaviour paragraph, ending "and `chore:` only where a released change already decided its effect, as the next paragraph says" |
| `git log -S'the-readme-says-how-to-install' -- skills/commit-pr-convention/SKILL.md` | `9944919e`, this branch's phase 1 fix |
| `git show --stat 97e29b7a` | hooks, `skills/evidence-check/SKILL.md`, `skills/evidence-check/scripts/evidence_check.py`, its records |

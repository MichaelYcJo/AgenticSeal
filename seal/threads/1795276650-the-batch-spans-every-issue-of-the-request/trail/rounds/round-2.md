# Review round 2: 1795276650-the-batch-spans-every-issue-of-the-request

```seal
target: cc31c3ee4, fixes 51ee61900..cc31c3ee4
```

This round verifies the fix pass of round 1. The code reviewed is the diff
`51ee61900..cc31c3ee4`, five commits: the round 1 record (`3ed8533b3`), the
framer's fold of findings 1 to 3 (`365337e1e`), the fix pass (`014c7e9e2`),
its close blocks (`68c83cd55`) and the orchestrator's fold of
`frame/plan.md` *Operational impact* (`cc31c3ee4`). `routing.md`, the three
frame files, `gaps.md`, `changelog.md`, `pr.md` and
`trail/phases/phase-1.md` were each read whole at `cc31c3ee4`. No
`pr.<lang>.md` stands and none is owed, since `seal/config.json` names
English for both language keys (read). No `seal/parity.json` is declared,
as round 1 executed; nothing in the fix diff adds one (read).

Carried from round 1 and not searched again: the sample of other statements
of the rule that round 1 listed under *Confirmations*, and its reading of
`skills/implement/routing-question.md:77` ("Question 1 is put every time")
as every request. Re-established here: each of the frame's blocks D1 to D7
against its file, the old text of `skills/implement/routing-question.md`
at the base, S6 and S7, and the reading of every sentence the fix pass
added.

The axes this round owns, beyond the table's floor: the referent of each
demonstrative in the rewritten sentences, the moment each act happens
(batch time against a later item's start), whether the new README and
`/agentic:config` sentences contradict any other statement of when a person
is asked, and whether the release note states the old and new text as they
stand.

## Findings

None. No finding is opened this round.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `skills/implement/orchestration.md:208-210` now reads "What
surfaces when a later work item starts goes where the paragraph opening
*Once the batch is answered* sends it" (read). The sentence names its moment,
so "there" no longer has the issue body as a second antecedent. The frame's
D1 block (`frame/design.md:79-80`) holds the same words, and S1
(`frame/design.md:50`) was rewritten to match. The paragraph that sentence
points to (`skills/implement/orchestration.md:241-249`) sends a decision to
`questions.md`, a finding to `seal/follow-up.md` and a deliberate leftover to
the closing memo. `changelog.md:3` says "what surfaces later goes to
`questions.md`, `seal/follow-up.md` or the closing memo as before", which
agrees.

```seal
confirms: round-1#2
```
What holds: the bullet at `skills/implement/orchestration.md:221-232` names
the file as *Why this way* of the `routing.md` of the work item the issue
opens. It names the moment as when that `routing.md` is written at the
item's start. A later work item checks the line against the tree again at
that start, and `direct` stands in a sentence of its own (read). "That
start" has one antecedent, the later work item's start in the same
sentence. The re-check is no question put to a person, so it does not
contradict "asks nothing new when it starts" at `:205`. Where the re-check
finds the tree no longer answers, that is something that surfaces when a
later work item starts, and `:208-210` sends it on. The frame states the
same text in D1 (`frame/design.md:83-94`), S2 (`:51`), G6 (`:14`) and
*Scope* Out (`:44`). `frame/plan.md:22` (*Alternatives considered* row 6)
and `changelog.md:4` say the same. `docs/running/the-run.md:33-53` covers
questions that arise during the run and names no home for a tree's answer
that the bullet would contradict (read).

```seal
confirms: round-1#3
```
What holds: `README.md:126-130`, `README.ko.md:131-134` and
`skills/config/SKILL.md:56-58` stand as D5, D6 and D7 word for word
(executed, the whitespace-collapsed comparison under `## Probes`). None of
the three makes a work item's start the moment the keys or the routing
question are asked any more. Each new sentence has one reading.

- In `README.md`, "the first edit" is the request's, and "The question has
  four answers" at `:131` still follows a sentence whose object is the
  routing question.
- In `README.ko.md`, "그 묶음" points back to the questions the sentence
  before gathers "한 번에 모아" for one request. It is the nearest
  collection, and the setup's four questions two sentences earlier are
  asked before the root exists, not per request.
- In `skills/config/SKILL.md`, "its first edit" is the next request's.

The sentences were read against the other statements of when a person is
asked, and none contradicts them (read). That covers the first-setup
sentence beside them (`README.md:122-126`) and the opening of each README
(`README.md:13-15`, `README.ko.md:13-14`). It covers
`skills/implement/bootstrap.md:205-208`, `templates/setup/config.md:88-90`,
`skills/commit-pr-convention/SKILL.md:85-88`,
`docs/layout/one-root-by-lifetime.md:232-234`,
`skills/implement/routing-question.md:3-7`, `:77` and `:155-157`,
`skills/implement/multi-repository.md:9-13` and `docs/layout/the-pact.md:43`.
The sentences there that say "before a work item's first edit wherever
either is missing" stay true. The request's batch comes before every item's
first edit, and asks for the keys wherever either is missing when the
request starts. `skills/implement/routing-question.md:156`, "caught here, at
its next work item", names the first work item of the next request, which is
where D7 puts the asking. The list is a sample of an open class, built from
`git grep -n -i -E` over `skills agents docs templates CONTRIBUTING.md
README.md README.ko.md CLAUDE.md hooks lib bin` for "routing question",
"question 1 is", "라우팅 질문", "next work item", "작업 항목마다", "작업
항목을 시작", "asks again", "every work item" and "each work item", with each
hit that says when a person is asked read in place (executed). The frame
folds the finding as *Scope* items 6 to 8, S8, G11 and three `## Removes`
rows (`frame/design.md:19`, `:34-36`, `:57`, `:173-175`), and *Scope* Out
(`:41`) now keeps only the sentences G11 finds true. The headings those rows
cite, *Your first work item* and *첫 작업 항목*, stand at `README.md:106` and
`README.ko.md:111` (executed, `grep -n '^#'`).

```seal
confirms: round-1#4
```
What holds: `changelog.md:6` now says the old section had a later item ask
for both keys again at its own start wherever its base lacked either. It
says the old section took the titles' language or `English` without asking
only where the run was unattended. At
`f8056edde:skills/implement/routing-question.md:148-150` the default needed
"the routing answer was given for the release and the run is unattended"
(executed, `git show f8056edde:skills/implement/routing-question.md`). The
entry's subject is a later item of a release, where the first condition
already holds, so "only where the run was unattended" states the old text
as it stood.

What matched: the fix pass's new release-note entry, `changelog.md:7`. Its
"Before" sentences quote what `README.md:126-129`, `README.ko.md:131-133` and
`skills/config/SKILL.md:56-57` said at `51ee61900` (read in the diff). "Now
each says one batch is asked for each request" holds for the config skill
too. "the batch of the next request" is one batch per request, though it
does not repeat "whatever number of issues it names". The heading lists the
three files and the two questions together, and the sentences after it say
which file stated which question.

What matched: the frame's claims the fold added. G10's growth of about 273
words holds: `skills/implement/orchestration.md` holds 5,326 words at
`f8056edde` and 5,599 at `cc31c3ee4` (executed, `wc -w`). G9's claim that
`tests/behaviour/test_docs_line_wrap.py#COVERED` lists every prose file the
work edits except `skills/config/SKILL.md` holds: `README.md` and
`README.ko.md` enter it through `README_PAIR` at `:116-119`, and the four
skill files at `:137`, `:150`, `:159` and `:190`. The config skill's edited
lines stay within its neighbours' width (read). S6 holds at `cc31c3ee4`:
`git diff --stat 5c4bdc8d5 HEAD` over the roots S6 names lists the eight
files S6 names and no other (executed).

What matched: `frame/plan.md:42`, *Operational impact* as `cc31c3ee4` folds
it. It names two `### Process changes` rows, and `changelog.md:14-15` holds
two. `docs/layout/the-record-layout.md:51-58` asks for the table wherever
the diff changes one of five kinds of file, `skills/core/SKILL.md` and a
`skills/*/orchestration.md` file among them, one row per change, and the
diff changes those two and no other of the five (read). The fix pass
changed the batch section again, but row 1's *Change* cell still describes
the section as it stands. The fix pass added no file of that list, so no
third row is owed. `trail/phases/phase-1.md:13`, which recorded the
departure from a plan that named one row, states its own commit and needs no
change.

What matched: the records read whole. `routing.md` and `frame/questions.md`
state nothing the target contradicts, and `frame/questions.md:9` now cites
*Scope* items 6 to 8. `gaps.md` holds the broad gate as its one `## Not
verified` row, labelled for the orchestrator, which is the honest label rule
2 asks for. It removes no row (read in the diff: `gaps.md` is not in the
range). Both quotes of `pr.md` stand word for word in `frame/plan.md:48`
(executed, `grep -c -F` of each: 1). `frame/plan.md:31` still gives phase 1
as delivering *Scope* items 1 to 5. Items 6 to 8 were built by the fix pass
`014c7e9e2` and are traced by round 1 finding 3's close, so the cell is true
and no phase record is owed for them.

No test was added in the range, so no new case was read against its group.
The crafter's S7 count of 259 passed matches this round's run below. Its
review-round set of 3040 passed and 10 skipped was not re-run and stands
under `## Not judged`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD, `uvx ruff check . && uvx ruff format --check . && bin/test -q`; the suite is `unverified` here, as rule 2 leaves it | `seal/config.json`, `Broad gate` | the orchestrator, once the review rounds settle |
| The crafter's review-round set, 3040 passed and 10 skipped, not re-run | the crafter's hand-back for `014c7e9e2` | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:randomly` over the nine files `frame/design.md` S7 names | 259 passed, exit 0, at `cc31c3ee4` |
| `python3 -I -c` comparing each of `frame/design.md` D1 to D7, whitespace collapsed, with its file | each block, and each of D1's four parts, found whole in its file |
| `git diff --stat 5c4bdc8d5 HEAD -- skills .claude-plugin docs agents templates README.md README.ko.md CONTRIBUTING.md tests` | eight files, the eight S6 names |

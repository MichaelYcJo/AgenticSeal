# Review round 1: 1795276650-the-batch-spans-every-issue-of-the-request

```seal
target: 51ee61900 against origin/release/v0.38.4
```

This is the first round, so no earlier record carries a coordinate and every
fact below was established here. The diff was read from the base
`f8056edde` to `51ee61900`, ten commits. `routing.md`, the three frame
files, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md` were
each read whole at `51ee61900`. No `pr.<lang>.md` stands, and none is owed:
`seal/config.json` names English for both language keys (read). No
`seal/parity.json` is declared (executed, `ls seal/parity.json`: no such
file). The issue was read with `gh issue view 1563 --json
title,body,comments,milestone` (executed 2026-11-22: 0 comments, milestone
`release: 0.38.4`).

The axes this change owns, beyond the table's floor: the referent of each
pronoun and demonstrative in the rewritten sentences, the moment each act
happens (batch time against a later item's start), where an answer waits
between those two moments, and every other statement of when a person is
asked across `skills`, `agents`, `docs`, `templates`, `CONTRIBUTING.md` and
the READMEs. That last class is open, so its list below is a sample: it was
built from `git grep -n -i -E "first edit|one batch|in a batch|the batch|asked
once|starts a work item|start of (the|a|each|every) (run|work item|request)|when
it starts|each work item's issue|every work item"` over those roots and a
second search for `routing question|every time|라우팅 질문` over the READMEs,
each hit that says when a person is asked read in place.

## Findings

### 1. The scope paragraph's "What surfaces there" has no place it can point to

```seal
severity: should
location: `skills/implement/orchestration.md:205-210`, `seal/threads/1795276650-the-batch-spans-every-issue-of-the-request/frame/design.md:71-76`
evidence: read `skills/implement/orchestration.md:202-211`, the issue body's *Decision* first bullet
```

Why it matters: the sentence tells the orchestrator where to send what comes
up when a later work item starts, and that is the one act this paragraph
adds for a later item. At `skills/implement/orchestration.md:205` the
paragraph says a later work item "asks nothing new when it starts". Two
sentences follow before "What surfaces there" at `:208-209`, and the nearest
place either of them names is "that issue's body" (`:207`), with "the frame"
inside the same sentence. So "there" reads as the issue body as readily as
the later item's start. A reader taking the first reading routes what
surfaces in the issue, such as a new comment, through the paragraph opening
*Once the batch is answered*, and is told nothing about what surfaces at the
later item's start. The issue's *Decision* has the sentence right after its
subject ("Starting a later item asks nothing new, and what surfaces there
goes where..."), where it has one reading; the build moved two sentences
between them. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한
가지로만 읽히게 쓴다* asks that an instruction name when it applies.

The fix names the moment. The frame's D1 block (`frame/design.md:71-76`)
states the same text as the text after the build, so the fix pass owes it
the same words.

```markdown
written from the routing answer the batch got. An answer the batch gave for
its issue is folded into that issue's body, as *Orchestrator: the order inside
a ticket* states for a decision made before the frame is committed. What
surfaces when a later work item starts goes where the paragraph opening *Once
the batch is answered* sends it. A new request is asked a batch of its own,
question 1 of `skills/implement/routing-question.md` among it.
```

### 2. The tree's answer goes to "that item's" `routing.md`, which names the earlier work item and, for a later item, a file not yet written

```seal
severity: should
location: `skills/implement/orchestration.md:221-229`, `seal/threads/1795276650-the-batch-spans-every-issue-of-the-request/frame/design.md:79-87`
evidence: read `skills/implement/orchestration.md:221-229`, `seal/threads/1795276650-the-batch-spans-every-issue-of-the-request/frame/plan.md:23`, `seal/threads/1795276650-the-batch-spans-every-issue-of-the-request/frame/design.md:13`, `skills/writing-style/SKILL.md:275-279`
```

Why it matters: this sentence is where the issue's second *Decision* bullet
lands, "the orchestrator writes that answer with its coordinate and does not
ask", and it has two defects of the same clause.

- **The referent.** The bullet never names the issue's own work item as an
  "item". The only noun "item" in it is "the work items that came before"
  (`skills/implement/orchestration.md:226-227`), the work items whose records
  answered the question. So "that item's `routing.md` *Why this way*"
  (`:228`) reads as the `routing.md` of the earlier work item that answered
  it. That is a committed record of another work item, often one already
  merged into the release branch. The intended file is the `routing.md` of
  the work item the issue opens.
- **The moment.** The check runs "Before its question enters the batch"
  (`:225`), which for a request of several issues is before the first edit
  of the request's first work item (`:204`). A later item's `routing.md` is
  written only when that item starts, and `frame/plan.md:23` (*Alternatives
  considered* row 7) rejects writing it earlier. So for a later item the
  file the sentence names does not exist when the orchestrator holds the
  answer. Answers the person gave have a home until then, the issue body
  (`frame/design.md:13`, G5), and the tree's answers have none: they live in
  the session's context until the item starts. A session that takes the
  request over through `handoff.md` meets the issue's line again with no
  record that the tree answered it.

`skills/writing-style/SKILL.md:275-279` asks that an instruction state who
acts, when, and in which file. The clause leaves "when" unsaid and "which
file" with two readings. The fix names the file and the moment, and has the
orchestrator check the line again when the later item starts, which costs
one search and needs no record kept between the two moments. The frame's D1
block (`frame/design.md:79-87`) states this text and is owed the same words.
`changelog.md:4` says "the item's `routing.md`", which reads one way, and
needs no change.

```markdown
- **A question you can answer is not a question.** Read the documents and the
  code first. An issue's line that leaves a decision to a person is a claim
  dated by the issue: it records what was open when the issue was filed.
  Before its question enters the batch, the orchestrator checks it against
  the policy root, `seal/config.json`, the code, and the records under
  `seal/threads/` of the work items that came before. Where they answer it,
  the orchestrator does not ask. It writes the answer with its coordinate in
  *Why this way* of the `routing.md` of the work item the issue opens, when
  it writes that `routing.md` at the item's start. For a later work item of
  the request, it checks the line against the tree again at that start. For
  `direct`, the answer goes in the body of the commit that carries the
  change. What survives that is the batch.
```

### 3. The READMEs and `/agentic:config` still tie the language-key question and the routing question to each work item's start

```seal
severity: should
location: `README.md:126-129`, `README.ko.md:131-133`, `skills/config/SKILL.md:56-57`, `seal/threads/1795276650-the-batch-spans-every-issue-of-the-request/frame/design.md:19`, `seal/threads/1795276650-the-batch-spans-every-issue-of-the-request/frame/design.md:38`
evidence: executed `git grep -n -i -E "routing question|every time|라우팅 질문" -- '*README*'` and the first-edit search named above the findings; read `README.md:120-130`, `README.ko.md:125-134`, `skills/config/SKILL.md:52-60`, `skills/implement/orchestration.md:202-211`, `seal/threads/1795276650-the-batch-spans-every-issue-of-the-request/frame/design.md:19`
```

Why it matters: the section now says a later work item of a request asks
nothing new when it starts, and that question 1 is put once per request
(`skills/implement/orchestration.md:204-211`). Three statements a person
reads say the opposite.

- `README.md:126-129`: "A work item that starts where either language key
  is missing asks for both before its first edit. Then it asks the routing
  question, every time and even for a typo fix". The subject of both
  sentences is the work item at its start, so a person running a milestone
  is told each item asks the keys and the routing question again.
- `README.ko.md:131-133` says the same: "작업 항목을 시작할 때 첫 편집 전에
  두 키를 모두 묻습니다. 그다음 라우팅 질문을 합니다. 오타 하나를 고칠 때도
  매번 묻고".
- `skills/config/SKILL.md:56-57`: "the orchestrator asks for both before the
  next work item's first edit". The next work item may be a later item of
  the same request, which by D4 (`skills/implement/routing-question.md:148-150`)
  asks nothing.

Claimed in `frame/design.md:19` (G11): each of the language-key sentences
"stays true: the request's batch comes before every item's first edit".
Found: that holds for the sentences whose subject is the batch
(`skills/implement/bootstrap.md:206-207`,
`docs/layout/one-root-by-lifetime.md:232-233`) or an act placed only
"before" an edit (`templates/setup/config.md:89`,
`skills/commit-pr-convention/SKILL.md:84-85`). It does not hold for the
three above, whose subject is a work item's start or the next work item. G11
also read only the language-key sentence of `README.md:127`, and the
routing-question sentence beside it (`:128`) was outside its search's
spellings. *Scope* Out (`frame/design.md:38`) and S6 keep these files out of
the diff, so the fix pass's change to them is a fold of the frame, which the
orchestrator routes to the framer.

For `README.md:126-129`:

```markdown
and `/agentic:config` changes any of them later. Each request you make is
asked one batch of questions before its first edit, whatever number of
issues it names. Where either language key is missing, the batch asks for
both. It asks the routing question too, on every request and even for a typo
fix, with the answer it recommends marked.
```

For `README.ko.md:131-133`, ending where the line's "답은 넷이고" continues:

```markdown
있습니다. 요청 하나에는 이슈를 몇 개 담든 첫 편집 전에 질문을 한 번에 모아
묻습니다. 언어 키 둘 가운데 하나라도 빠져 있으면 그 묶음에서 두 키를 모두
묻습니다. 라우팅 질문도 그 묶음에 들어갑니다. 오타 하나를 고칠 때도 요청마다
묻고, 권하는 답에 표시를 해 둡니다. 답은 넷이고, 표시가 붙는 답은
```

For `skills/config/SKILL.md:56-57`, the clause only:

```markdown
`seal pr-body` names the key and refuses with nothing written, and the
orchestrator asks for both in the batch of the next request, before its first
edit. A
```

### 4. The changelog says the old text took the default language at a later item wherever a key was missing; the old text took it only where the run was unattended

```seal
severity: should
location: `seal/threads/1795276650-the-batch-spans-every-issue-of-the-request/changelog.md:6`
evidence: executed `git show f8056edde:skills/implement/routing-question.md | sed -n 140,157p`; read `seal/threads/1795276650-the-batch-spans-every-issue-of-the-request/changelog.md:6`
```

Why it matters: the fragment becomes the release note a person reads to
learn what changed. Claimed at `changelog.md:6`: the old section "had a later
item of a release take the default language wherever its base lacked a key,
because the routing answer was given for the release". Found at
`f8056edde:skills/implement/routing-question.md:148-150`: "Where the batch
reaches no person, because the routing answer was given for the release and
the run is unattended". The default needed both conditions. With a person
present, the old per-item batch asked for the keys again at the later item,
which is the late question the issue removes. The sentence describes a
before that did not exist and hides the behaviour this change ends.

```markdown
- **A later work item of a request writes the language keys the request's batch gave (#1563).** `skills/implement/routing-question.md` *Orchestrator: the two language keys* had a later item of a release ask for both keys again at its own start wherever its base lacked either, and take the titles' language or `English` without asking only where the run was unattended. Now that item asks nothing, and its routing commit writes the answers the request's batch gave. The default stays for a run with nobody there to answer.
```

## Confirmations

What matched: `frame/design.md` D1 to D4 stand in the tree word for word, at
`skills/implement/orchestration.md:196-211`, `:221-229` and `:238-239`,
`skills/implement/SKILL.md:163-168`, `skills/core/SKILL.md:93-99` and
`skills/implement/routing-question.md:148-152` (read, each block set beside
its file). The phase record's claim that only line breaks moved elsewhere
holds for the paragraph opening *Once the batch is answered*
(`skills/implement/orchestration.md:238-246`) and the rewrap of
`skills/implement/routing-question.md:148-157` (read in the diff).

What matched: the issue's *Done when* items 1 and 2 are met apart from
findings 1 to 3. The section states the scope (`:202-211`) and the tree
check (`:221-229`). `skills/implement/SKILL.md:163-168` and
`skills/core/SKILL.md:95-99` cite the section by path and heading and copy
none of it, and `tests/text/test_no_passage_is_pasted_into_a_second_file.py`
passed in this round's run.

What matched: *Done when* item 3, that every test pinning a rewritten
sentence is rewritten. `git grep -n -i -E` over `tests evals lib bin` for the
removed phrases ("when it starts a work item", "routing answer was given",
"the SDD set and the ticket") and the changed ones (executed) printed one
line, the docstring at `tests/behaviour/test_waiver_decided_at_start.py:774`.
It quotes "Once the batch is answered the session runs to the pull request",
and those words still open the lead at `skills/implement/orchestration.md:238`.
The frame's G8 claim of no pin needing change holds for these spellings; a
pin written as a regular expression is reached only by the run below.

What matched: the crafter's S7 claim. This round ran the seven files of S7
through `bin/test` (executed): 210 passed, exit 0, at `51ee61900`. The
phase-boundary claim of 2393 passed was not re-run and stands under `## Not
judged`.

What matched: S5 and S6. `.claude-plugin/plugin.json:4` reads `0.38.4`, and
`git diff --stat 5c4bdc8d5 51ee61900` over the roots S6 names lists the five
files S6 names and no other (executed).

What matched: the records against the target. `routing.md:18` cites
`skills/implement/SKILL.md:163-168` and `skills/core/SKILL.md:95-99`, which
span the rewritten sentences at `51ee61900`, and `docs/running/the-run.md:33`
opens the paragraph it cites (read). Both quotes of `pr.md` stand word for
word in `frame/plan.md:48`, the title's row of *Judgments of the run*
(executed, `grep -c -F` of each: 1). `gaps.md` holds the broad gate as its
one `## Not verified` row, labelled for the orchestrator, which is the
honest label rule 2 asks for. The `### Process changes` table holds two
rows in the shape of `templates/records/process.md`, one for each of the two
files `docs/layout/the-record-layout.md:52` names that the diff changes.

What matched: the other statements of the rule outside the three findings
above, from the sample named at the top of this record. `CONTRIBUTING.md:397`
and `:430`, `skills/implement/routing-question.md:3-21` and `:58`,
`skills/implement/SKILL.md:28`, `:260-262` and `:286-289`,
`skills/implement/multi-repository.md:9-13`, `docs/running/the-agent-set.md:62`,
`docs/checks/the-routing-check.md:14-17`, `agents/crafter.md:77`,
`agents/framer.md:142` and `templates/records/sdd-routing.md:12` each place
the batch or the routing declaration before the first edit and stay true
when the request's batch precedes every item's first edit (read).
`skills/implement/routing-question.md:77`, "Question 1 is put every time,
whatever the ladder reads", reads as every request: the paragraph contrasts
it with a mark read off the ladder for small changes, and question 1's
`agentic` row says the route is not asked again (read).

What matched: the new term "the person's request" has one reading. The
tree used the bare word only as the tail of "pull request" before this
change (executed, `git grep -n -w "request"` over `skills agents docs
templates`), and each new use is bound by "the person's request" or by "a
request that names several issues" in the same paragraph.

No test was added, as `frame/plan.md:25` (*Alternatives considered* row 9)
decided, so no new case was read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD, `uvx ruff check . && uvx ruff format --check . && bin/test -q`; the suite is `unverified` here, as rule 2 leaves it | `seal/config.json`, `Broad gate` | the orchestrator, once the review rounds settle |
| The crafter's phase-boundary run, 2393 passed and 10 skipped at `56bd4ed7a`, not re-run | `seal/threads/1795276650-the-batch-spans-every-issue-of-the-request/trail/phases/phase-1.md:22` | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:randomly` over the seven files `frame/design.md` S7 names | 210 passed, exit 0, at `51ee61900` |
| `git grep -n -i -E` over `tests evals lib bin '*.py'` for the removed and changed phrases | one line, `tests/behaviour/test_waiver_decided_at_start.py:774`, a docstring whose words still stand |

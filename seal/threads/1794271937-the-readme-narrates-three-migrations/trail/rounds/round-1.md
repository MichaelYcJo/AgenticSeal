# Review round 1: 1794271937-the-readme-narrates-three-migrations

```seal
target: cbe9a186f against origin/release/v0.37.1
```

The branch was read against `origin/release/v0.37.1` at `8657297d5`, the
merge base, over its thirteen commits. This is the first round, so no
coordinate or verdict was carried from an earlier one; every fact below was
established here. `seal/parity.json` is not declared, so no parity
comparison was owed. The work item's records were each read whole at
`cbe9a186f`: `routing.md`, the three frame files, `gaps.md`,
`changelog.md`, `pr.md` and `trail/phases/phase-1.md`. No `pr.<lang>.md`
stands, and `seal/config.json` names English for both language keys, so
none is owed.

## Findings

### 1. The README says `/agentic:update` tells a person what the release they are leaving asks of them

```seal
severity: should
location: `README.md:95-99`, `README.ko.md:99-102`, `seal/threads/1794271937-the-readme-narrates-three-migrations/changelog.md:3`, `seal/threads/1794271937-the-readme-narrates-three-migrations/frame/design.md:31-33`
evidence: read `README.md:75-77`, `README.md:95-99`, `README.ko.md:99-102`, `skills/update/SKILL.md:87-135`, `seal/threads/1794271937-the-readme-narrates-three-migrations/changelog.md:3`, `seal/threads/1794271937-the-readme-narrates-three-migrations/frame/design.md:29-35`
```

Why it matters: `README.md:95-96` opens "An update from an earlier release
can leave work behind. `/agentic:update` tells you what that release asks
of you". The only release the sentence names is the earlier one, the
release the person is updating from. Update step 3 does not read that
release's note. It prints the note of every release after the old version,
up to the new one (`skills/update/SKILL.md:120-121`). A person on 0.36.x
is asked to run `seal mode` by 0.37.0's note, not by 0.36.x's. The same
section already states the fact correctly at `README.md:75-77`: the command
"names the changelog entries between your version and the new one, and
calls out each one that changes behaviour or asks something of you". So
the new clause is a second statement of that fact, and it names the wrong
release. `README.ko.md:99-100` carries the same clause ("그 릴리스가
사용자에게 요구하는 것을 알려 주고"). The source of the wording is
`frame/design.md` *Scope* item 1 (`:31-33`), which reworded the issue's
"tells a person coming from an earlier release what to do". The
`changelog.md` *Changed* first item repeats it, so it would also reach
every person through the 0.37.1 release note. No test pins this paragraph,
so no case changes with it.

The fix drops the clause and leaves the two things the paragraph alone
says. All four statements change together. The changelog's sentence is not
quoted in `pr.md`, so `pr.md` does not change.

```markdown
README.md, replacing lines 95-99 up to the link:
An update from an earlier release can leave work behind.
`/agentic:update` takes out what an earlier release wrote into your
`CLAUDE.md`, and names what an earlier release left that only you can
remove ([`skills/update/SKILL.md`](skills/update/SKILL.md)). If you update
by hand instead, two things are yours. ...

README.ko.md, lines 99-102:
이전 릴리스에서 업데이트하면 할 일이 남을 수 있습니다. `/agentic:update` 는
이전 릴리스가 `CLAUDE.md` 에 써 넣은 것을 들어내고, 이전 릴리스가 남긴 것
가운데 사용자만 지울 수 있는 것을 짚어
줍니다([`skills/update/SKILL.md`](skills/update/SKILL.md)). 손으로 ...

changelog.md:3, the sentence beginning "It says that":
It says that `/agentic:update` takes out what an earlier release wrote
into their `CLAUDE.md` and names what an earlier release left that only
they can remove, with a link to `skills/update/SKILL.md`.

frame/design.md *Scope* item 1, the sentence beginning "It says that":
It says that `/agentic:update` takes out what an earlier release wrote
into their `CLAUDE.md`, and names what an earlier release left that only
they can remove, with a link to `skills/update/SKILL.md`; the section's
first paragraph already says that step 3 names what each later release
asks.
```

Both READMEs are on the wrap list of `tests/behaviour/test_docs_line_wrap.py`,
so each line has to stay within its limit.

### 2. The experiment record calls its whole *Method* the comment's account, while its re-run outline is the transcriber's

```seal
severity: should
location: `docs/experiments/2026-11-06-what-draws-the-stamp-without-a-plugin-hook.md:41-43`, `docs/experiments/2026-11-06-what-draws-the-stamp-without-a-plugin-hook.md:59-61`
evidence: executed `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6675898172 --jq .body`; read `docs/experiments/2026-11-06-what-draws-the-stamp-without-a-plugin-hook.md:35-61`, `docs/experiments/README.md`, `seal/threads/1794271937-the-readme-narrates-three-migrations/trail/phases/phase-1.md:54-64`
```

Why it matters: `docs/experiments/README.md` gives the directory one job,
to say what was measured so nobody measures it twice, and
`docs/checks/the-stamp.md` now cites this record as the source of a
measurement. A reader of such a record has to be able to tell what the
measurement did from what someone wrote later. The comment's section *The
terminal stamp* says the surfaces were "Read and executed on Claude Code
2.1.319, 2026-11-06, in a scratch plugin", and it gives no steps. The
record's *Method* transcribes that at `:35-39`, under "Its account:". Then
`:41-43` adds "To re-run it, build a scratch plugin whose `Stop` hook prints
a coloured `systemMessage`, then try each surface in *Results* in turn".
That sentence is not in the comment: the transcriber wrote it for #1492.
`:59-61` then says "*Method* is the comment's account and not a procedure
anyone has re-run". That is false for `:41-43`, so a reader takes the
outline as the owner's procedure. The crafter's claim in `phase-1.md:62-63`,
"Its *Method* carries a re-run outline and says it is the comment's
account", describes this record accurately, and that is the defect.

The fix says whose the outline is, at both places. The record is on the
wrap list, so the lines stay short.

```markdown
docs/experiments/2026-11-06-what-draws-the-stamp-without-a-plugin-hook.md:41-43:
The comment gives no steps. This outline was written on 2026-11-10, for
#1492, and nobody has run it: build a scratch plugin whose `Stop` hook
prints a coloured `systemMessage`, then try each surface in *Results* in
turn. Restore by removing the scratch plugin and any entry written into the
settings.

:59-61:
- **The steps.** The scratch plugin is not in this repository, and the
  comment records results. The first paragraph of *Method* is the comment's
  account, and the outline after it was written for this record. Nobody
  has run either as a procedure.
```

### 3. A paragraph of the plan's *Technical context* cites a `routing.md` sentence that the fold rewrote

```seal
severity: should
location: `seal/threads/1794271937-the-readme-narrates-three-migrations/frame/plan.md:36-44`
evidence: executed `git diff 20f97977c 6de39c054 -- seal/threads/1794271937-the-readme-narrates-three-migrations/routing.md seal/threads/1794271937-the-readme-narrates-three-migrations/frame/plan.md`; read `seal/threads/1794271937-the-readme-narrates-three-migrations/routing.md:14-22`
```

Why it matters: `frame/plan.md:36-37` says "`routing.md` *Why this way*
says the diff touches the two READMEs and `docs/checks/the-stamp.md`". That
was the old Review bullet. The fold `6de39c054` replaced it with the
review-chain bullet, so `routing.md:20` at the target says nothing of the
kind. The section is dated to `20f97977c` (`frame/plan.md:5`), which would
leave the sentence standing as a statement of that commit. But the same
fold also wrote into this paragraph (`:40-44`, "Phase 1 also exempted ...
so the orchestrator routed the review through the review chain"), a fact
of a later commit. The paragraph therefore no longer states `20f97977c`
alone, and its first sentence cites in the present tense a `routing.md`
sentence that no longer stands. The sealer reads a chosen route's grounds
against the diff (`agents/sealer.md` step 4), so it reads this paragraph
beside `routing.md`. It would find two accounts of the route's grounds and
have to work out which was true when.

```markdown
frame/plan.md:36-37, the first sentence:
`routing.md` *Why this way* first sent the review straight to the pull
request, on the grounds that the diff touches the two READMEs and
`docs/checks/the-stamp.md`.
```

## Confirmations

What matched: **the exemption of `templates/setup/claude-md-block.md`
holds, and naming the template in a shipped document is the weaker
repair.** The routing change asks a round to weigh this
(`routing.md:20`). Three things hold, by reading and by execution. First,
the exemption's premise. The case
`test_every_template_is_named_by_a_document_that_ships` asks that a session
bootstrapping a template find it named in shipped prose. No session
bootstraps this template. 0.24.2's update step diffs the marketplace
clone's copy against the person's `CLAUDE.md` (read,
`git show v0.24.2:skills/update/SKILL.md`, lines 133-138), and the current
step 4 never opens it (read, `skills/update/SKILL.md:137-213`). The case's
own docstring calls a mention made only to pass it "the mention that looks
like a reader and is not". Second, the alternative. A sentence in a shipped
document naming the template would be text no agent acts on, written to
satisfy a check. In `skills/update/SKILL.md` every `/agentic:update` run
would pay for it, and step 4 may not name it
(`tests/behaviour/test_the_old_block_leaves_through_update.py:208`). The
comment above `READ_BY_AN_EARLIER_RELEASE` is where the core puts text no
agent acts on. Third, the exemption ends. The stale guard refuses an entry
the tree no longer holds, so the removal *Scope* item 7 schedules has to
take the exemption out with the template. The table in that item names it
(`frame/design.md:102`). `seal mutate` over the tuple turned the case red
twice: once with the tuple emptied and once with a gone path added
(executed, *Probes*). One phrase of the new comment is narrower than the
fact: "the update to 0.25.0 runs 0.24.x's own update step". Any update from
0.24.x, to 0.37.1 included, runs that step. The comment is read by whoever
edits the case and by no party at a step, so it is no finding.

What matched: the issue's *Done when* holds. The launcher is described in
`skills/update/SKILL.md` *4b* alone (executed: `git grep -n -i` for
`launcher`, `0.33.0`, `/stamp.py` and `stamp-hooks` outside `tests/` and
`seal/threads/`). `README.md:362-366`, `README.ko.md:358-362` and
`docs/checks/the-stamp.md:94-97` cite that step. The two READMEs carry the
same statements in the same order (read).

What matched: the acceptance greps of `frame/design.md` *User scenarios &
acceptance* rows 1 and 2. Row 1's grep printed nothing and exited 1. Row
2's grep hit `README.md:100` and `README.ko.md:104` in *Updating* and
*업데이트* (executed).

What matched: the experiment record against issue #1376's comment
6675898172 (executed, `gh api`). The four facts, the seven *Results* rows,
the marks the comment gives each fact, and the comment's date and Claude
Code build match the comment's section *The terminal stamp*. The record's
five sections stand in the order `docs/experiments/README.md` gives. Its
two-line heading follows the sibling record of 2026-09-03.

What matched: the removal date is stated the same way everywhere it
stands. That is the first release cut on or after 2027-02-07, all three
paths together, at `frame/design.md:88-91`, `frame/plan.md:89-92`,
`frame/questions.md:21-23`, `changelog.md:6` and `pr.md:4`. The date is 90
days after 2026-11-09, and `gh release view v0.37.0` gives that publication
date (executed). `frame/plan.md:57` says the one date keeps the earliest
path ten days past its own 90. That is true: 0.25.0 was published on
2026-10-30, and 90 days later is 2027-01-28. Whether 90 days is right is
the owner's question at the pull request.

What matched: each quote of `pr.md` stands word for word, with whitespace
collapsed, at its coordinate (read): items 1 to 4 in `changelog.md`, item
5 at `frame/design.md:91-92`, item 6 at `routing.md:20` and item 7 at
`frame/plan.md:100`.

What matched: the phase record's claims that new asserts went red. A
sample was re-run with `seal mutate` in a scratch clone (executed,
*Probes*). These were the draw-once sentence and the attribution to the
spike in `docs/checks/the-stamp.md`, and the old launcher sentence restored
in `README.md`. Each mutant was `red`. The other mutants that
`phase-1.md:79-92` lists were not re-run.

What matched: `gaps.md` labels the suite, the repository-wide lint and the
format check `unverified` and names the orchestrator as their answerer.
That label is honest: no party has run them. Its *Not done* reads
`nothing`. Filing the removal's issue is the orchestrator's at the pull
request (`frame/design.md:114-115`), so that is no gap.

The new asserts sit inside two existing cases and add no case, so no new
test is read against a group. Each holds a fact *Scope* item 6 or scenario
row 5 states.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The whole suite, the repository-wide lint and the format check at `cbe9a186f`. This round ran the plan's narrow modules and a format and lint check of the three changed test files only (contract rule 2) | `seal/threads/1794271937-the-readme-narrates-three-migrations/gaps.md:7` | the orchestrator, through `seal gate` |
| Whether 90 days is the right window before the compatibility paths leave | `seal/threads/1794271937-the-readme-narrates-three-migrations/frame/design.md:88-98` | the owner, at the pull request |
| The phase record's other `seal mutate` claims, for the Korean edition, the wrap entry and the `${CLAUDE_PLUGIN_DATA}/stamp.py` and citation asserts | `seal/threads/1794271937-the-readme-narrates-three-migrations/trail/phases/phase-1.md:79-92` | the sealer, if it samples them |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the seven modules of plan row 1 and `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`, in the branch worktree | 270 passed, exit 0 |
| `uvx ruff format --check` and `uvx ruff check` over the three changed test files | 3 files already formatted, all checks passed, exit 0 each |
| `bin/seal mutate tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` with the tuple emptied, then with `templates/setup/gone.md` added, `--tests` the case alone, in a scratch clone at `cbe9a186f` | 2 mutants, 2 red |
| `bin/seal mutate docs/checks/the-stamp.md` with "drawn once, since" made "drawn once either way, since", then "as the owner's spike showed" added after the measurement, `--tests` `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py` | 2 mutants, 2 red |
| `bin/seal mutate README.md` with the new launcher clause put back to "`/agentic:update` names both for you to take out by hand", same tests | red; `test_both_readmes_say_what_the_stamp_hook_writes_and_leaves` failed |

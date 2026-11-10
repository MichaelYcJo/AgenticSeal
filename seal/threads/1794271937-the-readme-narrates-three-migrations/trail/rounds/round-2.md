# Review round 2: 1794271937-the-readme-narrates-three-migrations

```seal
target: 5d834a711, fixes cd68ee96d..5d834a711
```

This is the verifying round over round 1's fixes. The code read is the diff
`cd68ee96d..5d834a711`: the frame repair `1e57f1a59`, the crafter's fix
`7a608c6ce`, the close block commit `a411017eb`, and the frame fold
`5d834a711`. Outside that bound, the work item's records were each read
whole at `5d834a711`: `routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`,
`trail/phases/phase-1.md` and `trail/rounds/round-1.md`. No `pr.<lang>.md`
stands, and `seal/config.json` names English for both language keys, so
none is owed. `seal/parity.json` is not declared, so no parity comparison
was owed.

Carried from round 1 as coordinates and not re-established here, since the
fix diff does not touch them: the confirmation of the
`READ_BY_AN_EARLIER_RELEASE` exemption, the issue's *Done when* grep, the
seven *Results* rows of the experiment record against the comment, the
removal date's agreement across the records, and the phase record's
`seal mutate` claims. Re-established here: update step 3's span at
`skills/update/SKILL.md:87-135`, the comment's text (re-fetched), each of the
three closes, the two frame statements the fold rewrote, every `pr.md`
quote, and the acceptance greps of scenario rows 1 and 2.

## Findings

None. No close of round 1 fails to hold, no unit the fix pass touched
carries a new defect, and no sentence of the work item's records is
contradicted by `5d834a711`.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the clause that `/agentic:update` tells a person what the
release they leave asks of them is gone from every statement round 1 named.
`README.md:95-98` now says only that the command takes out what an earlier
release wrote into `CLAUDE.md` and names what an earlier release left that
only the person can remove, with the link. `README.ko.md:99-102` says the
same two things in the same order. `changelog.md:3` says the same two
things. `frame/design.md:29-33` (*Scope* item 1) was repaired in
`1e57f1a59`. The close answer said the claim also stood in G3's right
column at `frame/design.md:13`. The fold `5d834a711` rewrote that cell to
"already prints, for a person coming from an earlier release, the notes of
every release after the one they leave, with what each asks of them". That
matches `skills/update/SKILL.md:120-121`, which prints the body of every
release after the old version up to the new one, and `:129-135`, which gives
what the user has to do a line of its own (read). A search for the old
wording over both READMEs, `docs/` and the work item finds it only in
round 1's own record (executed, `git grep -n -i -e 'asks of' -e 'what that
release' -e '요구하는 것'`). The rewrap leaves `README.md:99` at 83
columns, under the limit of 88, and the wrap case passed (executed,
*Probes*).

```seal
confirms: round-1#2
```
What holds: the experiment record now says whose the re-run outline is, at
both places round 1 named.
`docs/experiments/2026-11-06-what-draws-the-stamp-without-a-plugin-hook.md:41-45`
opens "The outline that follows is not the comment's" and dates it to
2026-11-10, for #1492. `:61-64` says the first paragraph of *Method* is the
comment's account and the second an outline nobody has run. The comment was
fetched again: its section *The terminal stamp* says the surfaces were
"Read and executed on Claude Code 2.1.319, 2026-11-06, in a scratch
plugin", and it holds no steps and no coloured `systemMessage` hook
(executed, `gh api`). So the outline is the transcriber's, as the record now
says. The fix pass claimed the date 2026-11-10 is the outline's commit
date. `git log -S'To re-run it'` lists `b0cb62de0`, dated 2026-11-10
(executed). The close answer said `frame/design.md` *Scope* item 5 still
called the method the comment's account. The fold `5d834a711` rewrote it at
`frame/design.md:73-75`, which now says *Method* holds the comment's
account and, after it, an outline written for #1492 that nobody has run.
That matches the record. A search for "comment's account" and "re-run
outline" finds no other present-tense statement. `phase-1.md:62-63` still
reads "Its *Method* carries a re-run outline and says it is the comment's
account". That line states the record at the phase's commit, where it was
true, so it is no finding.

```seal
confirms: round-1#3
```
What holds: `frame/plan.md:36-43` no longer cites a `routing.md` sentence
that the fold rewrote. It now lists what the diff touches in its own words,
and its last clause says `routing.md` *Why this way* holds the route that
follows from the exemption. `routing.md:20` holds that route. The list is
whole against the branch. `git diff --stat origin/release/v0.37.1...HEAD`,
outside `seal/threads/`, names seven files (executed): the two READMEs,
`docs/checks/the-stamp.md`, the experiment record,
`tests/behaviour/test_docs_line_wrap.py`,
`tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py`,
which holds both cases of *Scope* item 6 (`:139` for the policy case), and
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`.
The paragraph names each of them.

What matched: each quote of `pr.md` stands word for word, with whitespace
collapsed, at its coordinate at `5d834a711` (read). Items 1 to 4 are in
`changelog.md`. Item 5 is at `frame/design.md:91-92`, item 6 at
`routing.md:20` and item 7 at `frame/plan.md:99`. The fix to
`changelog.md:3` left the sentence `pr.md` item 2 quotes as it was.

What matched: the acceptance greps of `frame/design.md` *User scenarios &
acceptance* rows 1 and 2, re-run because both READMEs changed. Row 1's grep
printed nothing and exited 1. Row 2's grep hit `README.md:99` in *Updating*
and `README.ko.md:104` in *업데이트*, besides the command listings further
down (executed).

What matched: `gaps.md:7` labels the suite, the repository-wide lint and the
format check `unverified` and names the orchestrator as their answerer. That
label is honest at `5d834a711`, since no party has run them since the fixes.
The fix diff adds no test and changes none, so no new test is read against a
group.

This round leaves nothing open. What comes due is the orchestrator's broad
run at HEAD, and the sealer's spawn after it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The whole suite, the repository-wide lint and the format check at `5d834a711`. This round ran five narrow modules only (contract rule 2) | `seal/threads/1794271937-the-readme-narrates-three-migrations/gaps.md:7` | the orchestrator, through `seal gate` |
| Whether 90 days is the right window before the compatibility paths leave | `seal/threads/1794271937-the-readme-narrates-three-migrations/frame/design.md:88-98` | the owner, at the pull request |
| The phase record's `seal mutate` claims that round 1 did not re-run, for the Korean edition, the wrap entry and the `${CLAUDE_PLUGIN_DATA}/stamp.py` and citation asserts | `seal/threads/1794271937-the-readme-narrates-three-migrations/trail/phases/phase-1.md:79-92` | the sealer, if it samples them |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_both_editions_carry_the_same_folds.py`, `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/behaviour/test_release_hygiene.py` and `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, in the branch worktree | 158 passed, exit 0 |
| `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6675898172 --jq .body` | the comment's body; its section *The terminal stamp* names a scratch plugin and gives no steps |
| `git log -S'To re-run it' -- docs/experiments` | `7a608c6ce` and `b0cb62de0`, the second dated 2026-11-10 |
| ``git grep -n -e 'agentic:start' -e 'claude-md-block' -e '`stamp.py`' -- README.md README.ko.md`` | no output, exit 1 |
| `git grep -n 'seal mode' -- README.md README.ko.md` | `README.md:99` and `README.ko.md:104` in the update sections, and the command listings |

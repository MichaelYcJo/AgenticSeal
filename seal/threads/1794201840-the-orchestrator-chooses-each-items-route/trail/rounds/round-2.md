# Review round 2: 1794201840-the-orchestrator-chooses-each-items-route

```seal
target: 6c53e2da, fixes 91421710..6c53e2da
```

This is a verifying round. It read the range `91421710..6c53e2da` in a
`git clone --no-local` at `6c53e2da`: the round 1 record (`540c0405`), the
orchestrator's fold (`417e0839`), the fix pass's two commits (`ddf7b471`,
`55815ed9`) and its close blocks (`6c53e2da`). The code it reviewed is that
diff: `README.md`, `README.ko.md` and `templates/records/sdd-routing.md`.
Beside that bound it read `routing.md`, the three frame files, `gaps.md`,
`changelog.md` and `pr.md`, each whole at the target. No `pr.<lang>.md`
stands, and none is owed: `seal/config.md` names English for both language
rows.

Carried from round 1 and not re-established, because the fix range touches
none of their files: the old-label census over the tree, the ladder class
(G21), the four `from` texts of `frame/design.md` `## Rule changes` in their
policy files, and the test pairs `seal layout --pairs` printed. `seal rules
--check`, the check that carries the rules' `check:` targets, still exits 0
at the target (executed), so no carried rule coordinate is re-derived.

## Findings

### 1. The frame's G7 still says the routing template does not change, while the fix range changes it

```seal
severity: should
location: `seal/threads/1794201840-the-orchestrator-chooses-each-items-route/frame/design.md:15`
evidence: read `seal/threads/1794201840-the-orchestrator-chooses-each-items-route/frame/design.md:15`, `seal/threads/1794201840-the-orchestrator-chooses-each-items-route/frame/design.md:77`, `seal/threads/1794201840-the-orchestrator-chooses-each-items-route/frame/plan.md:64`, `templates/records/sdd-routing.md:16`
```

Why it matters: G7's last sentence reads "So neither the parser, the
template nor a check changes" (`frame/design.md:15`). At the target the
template changes: `55815ed9` rewrote its `## Why this way` placeholder
(`templates/records/sdd-routing.md:16`). The fold at `417e0839` rewrote the
*Out* bullet to say the placeholder is in scope (`frame/design.md:77`), and
left G7's conclusion as it was. So the frame now says two things about the
same file. The plan's judgment row (`frame/plan.md:64`) says G7's grounds
"cover the `Answered` line alone". G7's own last sentence names the whole
template, so that row describes G7 as it would read after this fix, not as
it reads now.

The Grounding section is dated to `e1067476`, and a dated section states
that commit. That covers G7's facts: the `Answered` line stood at
`templates/records/sdd-routing.md:12` and no script read it. It does not
cover G7's last sentence, which is a decision about this work's diff and not
a fact of the tree at `e1067476`. A decision folded after the frame is
rewritten in place, and the sentence that stood on the old decision goes
in the same commit (`skills/core/SKILL.md` *The rule a mechanism is kept
against*). The sealer reads the frame against the diff in its step 4, and
on this sentence it reads a frame that says the template does not change
over a diff that changes it.

This finding takes no `regression:` or `reopens:` line. Round 1 finding 2's
close holds (the confirmation below), and the sentence stands in a part of
`frame/design.md` that no commit of the fix range changed. It came from the
read of the work item's records, not from the fix diff.

The fix rewrites G7's last sentence. It keeps G7's facts, and it makes the
plan's row at `frame/plan.md:64` true as written, so that row needs no
change. No other statement in the work item says the template stays
unchanged (read: every line holding "template" in the frame files, the
phase records, `gaps.md`, `changelog.md` and `routing.md`).

```markdown
| G7 `git grep` over `*.py` outside `tests/` for `AUTOMATION_YES` and `["automation"]`, and over the tree for `Answered <date>` (executed) | No script outside `lib/routing.py` reads the `Automation` value. The `Answered` line stands in `templates/records/sdd-routing.md:12` and in the fixture `tests/e2e/teammate/test_teammate_flow.py:62`, and no script reads it. So neither the parser nor a check changes, and the template's `Answered` line keeps its shape. |
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: both opening paragraphs now name the exception before the seal
sentence (read: `README.md:17-21`, `README.ko.md:20-23`). The English reads
"Unless the session made the change itself, as under `direct`, or you asked
for the branch back, the run ends at a pull request whose records carry a
seal". The Korean says the same in one condition and one result, and ends
"머지는 하지 않습니다" as its own sentence. The fix pass claimed the second
case comes from `Destination` `stop before the pull request` under
`agentic`. `skills/implement/orchestration.md:552` holds that bullet inside
*Under agentic* (`:515`), and `:325` gives the same exit as `manual`'s
fourth box, so "you asked for the branch back" covers every answer that
can end without a pull request (read). "made the change itself, as under
`direct`" uses the words of the `direct` bullet at `README.md:132-133` and
the `agentic` bullet at `:122-126`, so it does not reach `Implementation`
`the session`, which still ends at a sealed pull request. The fix pass's
search for another sentence that promises a seal on every run was re-run
at the target (executed: `git grep -n -i "every run\|always ends\|ends at a
pull request\|ends in a seal\|에서 끝나"` over both READMEs). Its hits are
the ones the close names: `README.md:9`, `:19`, `:273`, `README.ko.md:276`.
`README.md:9` and `:273` describe the agents' chain, not every route. The
two editions still pass their fold, line-wrap and pasted-passage cases
(executed, *Probes*).

```seal
confirms: round-1#2
```
What holds: the placeholder at `templates/records/sdd-routing.md:16` now
asks for the grounds that `skills/implement/orchestration.md` *What the
answer writes* asks for (read). *What the answer writes* is the heading at
`skills/implement/orchestration.md:340`, and no heading stands between it
and `:367-370`. Those lines give both lengths: one or two sentences where
the person chose the rows, and the grounds *Under agentic* asks for where
the orchestrator chose them (read). So the length has one source, as the
close claims, and the `Answered` line at `:12` is unchanged. The close
claims no other file restates the old length for `routing.md`. Re-run at the
target, `git grep -n "one or two sentences"` outside `seal/threads` finds
only `skills/implement/orchestration.md:367`, the source, and
`templates/records/sdd-plan.md:35`, which is about a plan's judgment rows
(executed). The cases that read the template, in
`tests/behaviour/test_waiver_decided_at_start.py` and
`tests/lib/test_routing.py`, pass (executed). The close's claim that this
is no departure holds: `417e0839` folded the placeholder into *Out*
(`frame/design.md:77`) and wrote the judgment's row
(`frame/plan.md:64`). The one sentence that fold left standing is
finding 1.

What matched: the changelog's added sentence is true at the target. "The
routing template's placeholder under that heading now points at
`skills/implement/orchestration.md` *What the answer writes*, which sets
what the grounds hold, in place of "one or two sentences"" agrees with
`templates/records/sdd-routing.md:16` and the diff of `55815ed9` (read).

What matched: `pr.md`'s eight quotes stand word for word, with runs of
whitespace collapsed, at their sources. The first seven are in
`changelog.md`, quotes 1 to 4 in the first *Added* item, 5 in the second, 6
in the third, and 7 in the *Updating* line. The eighth is in `gaps.md`
*Not verified*, the first row (executed, *Probes*). The sentence the fix
pass added to the first *Added* item stands between quotes 3 and 4 and
changes neither.

What matched: `routing.md`, `frame/questions.md` and `gaps.md` are unchanged
in the range, and the target contradicts none of their sentences (read).
`routing.md` *Why this way* names the answer `automation`, the label the
owner gave on 2026-11-09 before it was renamed, so it records that answer
and does not state a present label.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate (full suite, ruff check, ruff format check) at the target. This round ran only the modules in *Probes*, so the suite is `unverified`. | `seal/config.md` `Broad gate` row | the orchestrator, by its broad run before the sealer |
| Whether an orchestrator answered `agentic` chooses as *Under agentic* guides, and whether a sealer and a settle read chosen routes as the new sentences say. Both are agents' behaviour at run time, and no case runs either. | `gaps.md` *Not verified*, rows 1 and 2 | the repository owner, as `gaps.md` names |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_waiver_decided_at_start.py tests/lib/test_routing.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/behaviour/test_docs_line_wrap.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/text/test_a_record_carries_no_comment.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/text/test_a_document_has_room_for_the_next_fold.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/text/test_a_question_says_who_can_answer_it.py tests/skills/test_pr_body.py -q`, in the clone at `6c53e2da` | exit 0, 339 passed |
| `bin/seal rules --check`, in the clone | exit 0, all 219 check lines in 68 rule files hold |
| `python3 -I test_tmp_quotes.py`, which collapses whitespace in `changelog.md`, `gaps.md` and each `pr.md` quote and looks for each quote in the file its coordinate names | all eight found |
| `git grep -n "one or two sentences"` and the fix pass's README search, in the clone | the hits named in the two confirmations |
| `chain_check.py --baseline release/v0.37.0 --root <the branch worktree> --worktree`, run with both the installed 0.36.0 copy and the tree's copy, with this record in place | exit 0. It printed finding 1 as open for having no close block, and the missing gate record and guarantee. It printed no notice at `frame/design.md` |

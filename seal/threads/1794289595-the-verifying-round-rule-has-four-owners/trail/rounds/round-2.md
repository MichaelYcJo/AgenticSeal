# Review round 2: 1794289595-the-verifying-round-rule-has-four-owners

```seal
target: 9f8996beb, fixes e889a539b..9f8996beb
```

This is a verifying round. The code it reviews is the diff of the round 1
fixes, `e889a539b..9f8996beb`: `skills/code-review/SKILL.md` *Earlier
rounds*, `RULES` row 21 of `tests/text/test_the_rules_have_one_owner.py`,
and the work item's `frame/design.md`, `frame/plan.md`, `gaps.md`,
`changelog.md` and `trail/rounds/round-1.md`. Beside that bound it read
`routing.md`, the three frame files, `gaps.md`, `changelog.md` and `pr.md`
whole at `9f8996beb`. No `pr.<lang>.md` stands, since both language keys of
`seal/config.json` read English. It read the tree's text of
`agents/proofer.md` and `skills/code-review/SKILL.md`, not the installed
0.37.1 copies the proofer was spawned with.

Carried from round 1 and not re-established: where the three relations are
read by the check (`skills/code-review/scripts/chain_check.py#channel`,
`:888-946`) and by the form (`docs/forms/the-round-record.md:64-80`), and
the base coordinates `df775c52c` `skills/code-review/orchestration.md:118-119`
and `agents/proofer.md:136-141`. Each was opened at the coordinate round 1
gave and read again, not searched for. Every verdict below is this round's.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the fix pass claimed that *Earlier rounds* drops "exactly" and
says that two lines name a finding whose close holds where its fix made a
regression's unit. `skills/code-review/SKILL.md:140-150` at `9f8996beb`
reads "named this round by one of three lines", and `:145-147` reads "Where
the close of the finding whose fix made the unit holds as well, a
`confirms:` line names that finding too, so two lines name it". The case
round 1 gave, a fix that holds for its own finding and breaks its unit, now
has its answer in the section: a `confirms:` line and a `regression:` line.
That agrees with the check, which collects every reference into one set and
refuses only a finding none names (`chain_check.py:905-946`, read), and
with the form, which allows one `regression:` or `reopens:` line per
finding block and says nothing against a confirmation beside it
(`docs/forms/the-round-record.md:14`, read). The `reopens:` sentence that
follows is unchanged, so no line's meaning moves for the other cases.

The pass departed from the paste-ready text in one phrase and gave its
grounds: "Where that fix's own finding holds" could read as "where the
finding's claim stands", which `docs/forms/the-round-record.md` *The round
record* uses for `rejected`. The pass wrote "the close of the finding whose
fix made the unit holds". That reading is the one round 1 meant, and it has
one reading. The departure holds.

`RULES` row 21 now pins the sentence without "exactly"
(`tests/text/test_the_rules_have_one_owner.py:175-181`). The pass claimed the
row was red against the unfixed section. `test_the_owner_states_the_rule`
asserts that the sentence is a substring of the flattened owner
(`:202-207`), and "by exactly one of three lines" does not hold "by one of
three lines", so the row fails if "exactly" returns. Read; this round did
not re-run the mutation (`## Not judged`).

The frame's half: `frame/design.md:29`, *Scope* item 1, now says a closed
finding is named "by one of three lines, and by a second where a second
relation holds", and that both lines stand where the fix holds for its own
finding. It says what the section says. Read.

The pass left the new two-lines sentence unpinned, and `gaps.md:37-48`
gives the grounds. This round checked the claim: no file under `tests/`
holds "two lines name", "names that finding too" or "holds as well"
(executed, `git grep`). `skills/code-review/SKILL.md` *A finding is not
closed too early* says a claim a fix writes into a document closes when a
test pins the document. This round weighs that bullet and confirms the
close. The defect round 1 named was the word "exactly", which made the
section forbid what the check and the form allow, and row 21 now goes red
on its return. The unpinned sentence states what those two already allow,
and removing it leaves no contradiction. `docs/running/what-a-script-gates.md`
*The checks* lets a case pin a fact a reader acts on and does not require
one. The orchestrator may weigh the other reading: that the bullet asks
for a third `RULES` row. That row would be one more line of a table that
already exists, and no round has needed it.

```seal
confirms: round-1#2
```
What holds: `changelog.md:4` reads as round 1's paste-ready text:
`agents/proofer.md` "keeps the bound of a verifying round, and now holds
the sentence on a new unit in the fix diff, which
`skills/code-review/orchestration.md` held". Round 1's evidence was re-run:
`git show df775c52c:agents/proofer.md | grep -n -i 'new unit'` finds
nothing, the base's `orchestration.md:118-119` holds the sentence, and at
`9f8996beb` `agents/proofer.md:139` holds it while `orchestration.md` holds
no "new unit" (executed). `pr.md:3` quotes only the item's bold lead, which
did not change.

```seal
confirms: round-1#3
```
What holds: `frame/plan.md:7-12` counts seven rule files and lists them.
`git diff --stat df775c52c..9f8996beb` outside `seal/threads` lists the same
seven, with `.claude-plugin/plugin.json` and
`tests/text/test_the_rules_have_one_owner.py` (executed). The fix is the
framer's fold at `ff6d0e908`, which touched only `frame/design.md` and
`frame/plan.md` (executed, `git show --stat`). The finding is located in
`frame/plan.md` alone. So the close is one the core's row *No fix that no
round reads* gives to the sealer, and this round reads it all the same
because it sits in the fix range.

What matched: the two rows the fold and the orchestrator added to
`frame/plan.md` *Judgments of the run*. The fold row says the base
`agents/proofer.md:136-141` said "is named this round" with no "exactly".
`git show df775c52c:agents/proofer.md` holds "is named this round:" at line
138 and no "exactly" (executed). The fix-pass row says the owner asked for
only the framer to run on Fable and every later agent on Opus. The
milestone `release: 0.37.2` holds that under *Model*: "The framer of #1476,
#1477 and #1478 runs on Fable; every other agent of every item runs on
Opus" (executed, `gh api` on the repository's milestones). Both cited
sections stand as headings: `skills/implement/orchestration.md:24` and
`skills/code-review/orchestration.md:16` (executed, `grep -n`).

What matched: every quote of `pr.md` stands at the source its coordinate
names, with runs of whitespace collapsed. Quote 7 is still the second
2026-11-10 row of *Judgments of the run* and quote 9 the first, now that the
section holds four rows of that date. Quote 8 writes its inner quotation
marks as `\"`, which round 1 judged a match, and this round compared it
with the escapes removed (executed, an inline `python3` over the nine
lines, all nine found).

What matched: the rest of the records that state the present, read whole
at `9f8996beb`. `gaps.md` `## Not verified` now names the round 1 fix pass
and the close blocks of `round-1.md` as the record of its claims. That fits
the fix range: `b2590e477` changed one rule file and the test file,
`972908a57` changed `changelog.md` (executed, `git show --stat`).
`routing.md`, `frame/questions.md`, the rest of `frame/design.md` and
`frame/plan.md`, and the other items of `changelog.md` are unchanged in the
fix range, and the fixed section contradicts none of their sentences.
The phase records state their own commits. `trail/phases/phase-1.md` quotes
the defining sentence with "exactly", as it read at `e15ed537d`, so
`9f8996beb` does not contradict it. Read.

What matched: the narrow modules over the fixed section and its cases ran
green: 162 passed, exit 0 (executed, see `## Probes`). The section's lines
are within the wrap the docs case holds, and no 15-word run of the new
sentence stands in a second rule file.

What matched: the fix reaches every statement of "exactly one line" in the
tree. `git grep -n -i -E` for "exactly one (of three )?line", "exactly one
of (the )?three" and "by exactly one" over `*.md` and `*.py` outside
`seal/threads` finds one unrelated line, `evals/scripts/rule_cases.py:277`
(executed). This is a search for wordings, so it is a sample of an open
class, as contract rule 12 names it. The other statements of the three
relations, `docs/forms/the-round-record.md:14` and `:64-80` and
`skills/code-review/orchestration.md:198-224`, were read against the fixed
section, and none forbids two lines naming one finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check. This round ran six narrow modules, and the suite stays `unverified` | `seal/config.json` `Broad gate` | the orchestrator, by its broad run after the rounds |
| The fix pass's two `seal mutate` runs on `skills/code-review/SKILL.md`: "exactly" put back ended `red`, and the two-lines sentence taken out survived. This round read the guard and searched the tests and ran neither again | `trail/rounds/round-1.md`, the close block of finding 1 | the sealer, which re-runs a sample of the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/text/test_review_axes.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_the_verifying_round_is_bounded_not_cheapest.py -q` | exit 0, 162 passed |
| round 1 finding 2's three `grep` lines, at `df775c52c` and at `9f8996beb` | the base's `agents/proofer.md` holds no "new unit"; `orchestration.md:118-119` at the base and `agents/proofer.md:139` at `9f8996beb` hold the sentence |
| `git diff --stat df775c52c..9f8996beb -- . ':!seal/threads'` and `git show --stat` of the five fix commits | seven rule files, the test file and `plugin.json`; `ff6d0e908` touched only the two frame files |
| `git grep` of the two-lines sentence's words under `tests/`, `skills/`, `docs/` and `agents/` | one line, `skills/code-review/SKILL.md:146` |
| `git grep -n -i -E` for "exactly one" wordings outside `seal/threads` | `evals/scripts/rule_cases.py:277` alone, unrelated |
| an inline `python3` comparing the nine quotes of `pr.md` with their sources, whitespace collapsed | all nine found |
| `gh api` on the repository's milestones, the description of `release: 0.37.2` | the *Model* paragraph the fix-pass judgment row cites |

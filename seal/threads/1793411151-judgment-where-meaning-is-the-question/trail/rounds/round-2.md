# Review round 2: 1793411151-judgment-where-meaning-is-the-question

target: 6ff6df90, fixes 39c3bf24..6ff6df90

This is a verifying round. It reads the fix diff `39c3bf24..6ff6df90`
alone: `24b7a5ed` (the core and writing-style), `b993444b` (the frame's
paragraph under Table B), `2d6d3d75` (round 1's answers) and `6ff6df90`
(the orchestrator's fold, which no round had read). It answers each of
round 1's six closes. The five scripts that still refuse a line spelt
otherwise are the interim state `trail/phases/phase-1.md` records, and no
finding counts them.

Facts carried from round 1 and not re-established this round: that
`templates/setup/hygiene.yml:14-20` reads only committed files and nothing
in local mode, that `docs/one-root-by-lifetime.md:128` says the pull-request
checks cannot run in local mode, and that `hooks/question-gate.py:104`
returns unless the declaration reads `yes`. Re-read this round, because
each is what a fixed row now rests on: `chain_check.py#follows`
(`:1521-1552`), the records arm (`:1740-1776`), the strictness rule in
`main` (`:2259-2261`), `broad_gate.py`'s docstring on its `--sealing` arm
(`:28-31`), and `skills/implement/SKILL.md` *1. Read the documents that
outrank the code first*.

## Findings

### 1. The frame still states the core's script sentence in the wording round 1 replaced, once as policy the settle will write

severity: should
location: `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:8`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:44`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:259-260`
evidence: read `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:8`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:44`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:48`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:252-268`, `skills/core/SKILL.md:121-126`
verdict: fixed 5db4f69f

Round 1's finding 4 found that "what it did not read it names" reads two
ways. Read whole, a script names every line of prose it did not read; read
as the frame means it, a script names only a line that looks like one of
its form's lines. `24b7a5ed` rewrote the core to the narrow reading
(`skills/core/SKILL.md:123-126`). The fold `6ff6df90` then gave its own
cause: the frame held "a copy that round 1's fixes left behind", so the two
copies said different things. It replaced Table B with a pointer and
stopped there. The same cause has three more instances in the frame. A
`git grep` over it found the first two, and reading the `## Rule changes`
item around `:252` found the third, whose phrase wraps across a line:

- `frame/design.md:44`, Scope item 1, gives the core sentence as built:
  "what it did not read it names and decides nothing about ... the
  judgment of the agent that reads the record". These are the two phrases
  finding 4 replaced. The sealer reads the design's scope against the tree
  at step 4 (`agents/sealer.md`), so it meets the two texts disagreeing,
  and the disagreement can only be settled from round 1's record.
- `frame/design.md:8`, the *Grounding* row, summarises the same sentence
  as "names what it did not read".
- `frame/design.md:259-260`, the `## Rule changes` `add` item for
  `docs/what-a-script-gates.md` *Which gate a script holds*. Its bold rule
  is "A script gates a closed form, in one spelling, and names what it did
  not read". The settle writes this text into the policy root as written.
  A section is cited by its bold sentence
  (`skills/writing-style/SKILL.md:262-263`), and a citation of this one
  carries the wide reading that finding 4 removed from the core. The body
  under it narrows the rule, which is also true of the core's original
  sentence.

`frame/design.md:48`, Scope item 5's heading, uses the same words and was
weighed: its body says exactly which line is printed, and nothing cites the
heading alone, so it is not counted. Contract rule 12 asks the fix for
every instance of a cause, and rule 19 asks the commit that changes a fact
to correct every sentence stating it. The frame is the framer's text, which
the fix pass would not edit (round 1 finding 1's answer). So, like
`6ff6df90`, this is the orchestrator's fold.

At `frame/design.md:44`, the clause from "what it did not read" to "the
agent that reads the record" becomes:

```markdown
it names as not read a line or a file that looks like one of its form's and is not one, and decides nothing on it; no script carries a list of the spellings a label is written in; whether such a line meant the label is the judgment of the agent that reads the text.
```

At `frame/design.md:8`, the second cell's second sentence becomes:

```markdown
Scope item 1 rewrites it: a script reads the plugin's own forms in one spelling each, names as not read a line or a file that looks like one of its form's and is not one, and carries no list of the spellings a label is written in.
```

At `frame/design.md:259-261`, the bold rule, from its opening `**` to the
`**` after "at a named step.", becomes the text below. The body after it,
from "A closed form is" on `:261`, is unchanged:

```markdown
    **A script gates a closed form, in one spelling, and names as not read a
    line or a file that looks like one of the form's and is not one; a
    judgment of meaning belongs to the agent that already reads the text, at
    a named step.**
```

answer: The orchestrator folded all three instances in place, as the finding asks and as the frame's new fold rule (`frame/design.md` *Scope* item 11, folded at 7b796a4a) puts it. The paste-ready text was read as the policy reader and the sealer read it. Each instance now states what the core says at `skills/core/SKILL.md:121-126`: a line or file that looks like one of the form's and is not one, and the agent that reads the text. The texts were used as written. `:48` was left as the round judged. No file outside the frame changed, so the sealer reads this fix at HEAD.

## Confirmations

confirms: round-1#1
The close holds. `skills/core/SKILL.md:99` now conditions the invariant on a
run routed `Automation` `yes`, and that is the condition under which
`hooks/question-gate.py` refuses. The protection cell names the run the
person sent end to end. On an attended run, nothing in the row now forbids
what `skills/implement/orchestration.md:179` allows (read). The fix pass
left the paragraph *Asking a person is the most expensive step*
(`skills/core/SKILL.md:80-90`) unchanged, and this round weighed that.
The paragraph is guidance, not an invariant: it claims no exemption from
judgment and no mechanism, and the one mechanism it names,
`hooks/routing-edit-gate.py`, applies "in a repository opted in by its
`seal/` root". Its sentence "Whatever needs a person is asked once,
together, before the first edit" is what its cited source says
(`skills/implement/SKILL.md`, *Collect what needs a person before the first
edit, and ask it in one batch* and *Once the batch is answered, the session
runs to the pull request*, read). So it is not finding 1's cause. The tension
between that source and the `no` box at `orchestration.md:179` predates
this work item and is outside the fix diff.
The frame's half of finding 1 (`frame/design.md:102` at round 1) is gone:
`6ff6df90` replaced the frame's copy of the row with a pointer to the core
(read).

confirms: round-1#2
The close holds. `skills/core/SKILL.md:105-109` says the check refuses only
a ready pull request where first setup or `seal pr-checks install` put its
workflow. This round re-read the code. `main` judges strictly only where the
state is not `draft` and not unseen (`chain_check.py:2259-2261`). Before a
pull request exists, `gh pr view` answers nothing and no event payload is
present, so problems print as notices and the exit is 0. `seal gate` runs
the arm with `--sealing` (`broad_gate.py:28-31`). `seal pr-checks install`
is a command (`bin/seal:15`). The sentence names `agents/sealer.md` step 1
and the orchestrator's section *Orchestrator: the pull request opens once
the sealer seals* (`skills/code-review/orchestration.md:177`). Both exist,
and that section orders the seal before the pull request (read). One
reading is left open, and it is not a defect: run by hand against a ready
pull request with no workflow installed, the check does exit 1. The
sentence is about what stops a pull request, and nothing stops one there.

confirms: round-1#3
The close holds. Row 2 (`skills/core/SKILL.md:100`) now says every record
carries one `target:` line, and HEAD descends from the last record's commit
and from every `fixed` commit. The `target:` row is `one` per record
(`docs/the-review-record.md:43`). `follows` refuses a commit it cannot
resolve or one HEAD does not descend from (`chain_check.py:1532-1537`). The
records arm applies it to the last record alone (`:1763-1776`). All read.

confirms: round-1#4
The close holds at its locations. `skills/core/SKILL.md:123-126` names as not
read "a line or a file that looks like one of its form's and is not one",
and gives the judgment to "the agent that reads the text".
`skills/writing-style/SKILL.md:265-266` reads "그 글을 읽는 에이전트".
`CONTRIBUTING.md:386-391` says "what the gate names as a line it did not
read", which is the narrow reading (read). The class has three more
instances in the frame, which finding 1 above names.

confirms: round-1#5
The close holds. The bold opener at `skills/writing-style/SKILL.md:257-258`
ends "검사가 읽는 줄은 검사가 읽는 철자 하나로 쓴다". The body at `:264-266`
carries only the naming and the reader's judgment, so the rule and its body
agree (read). `git grep` for the old opener's phrase "통과할 수 있는 모양"
finds it only in round 1's record (executed). The section's intro, "아래 세
규칙" at `:253`, still counts three rules. The `check:` line at `:268` and
its pin are unchanged.

confirms: round-1#6
The close held when it was made, and the fold has since removed the table.
`b993444b` is a pure move: its removed and added lines are the same set
(executed, `git show b993444b` with the changed lines sorted, no line
unmatched). `6ff6df90` then replaced the table and its paragraph with a
pointer, so the frame no longer renders a table whose rows a reader could
miscount (read).

confirms: none
The fold `6ff6df90`, read as a new unit, is accurate about the core. Its
pointer says that `skills/core/SKILL.md` *Judgment is not licence to skip a
party* holds the table once (`:97-103`), and it does. It says the first
row naming `chain_check.py` spells its path (`:100`), that later rows say
"the same check" (`:101-103`), and that the fourth row names the
`Broad gate` row and no tool (`:102`). All three hold (read). The frame's
other mentions of Table B, at `frame/plan.md:7`, `:29` and `:46`,
`frame/design.md:9`, `:67` and `:90`, and `frame/questions.md:12-13`, cite
the table by name and none quotes a row, so the pointer serves each of
them (read). Its words "Its five invariants are the core's list before this
work" are qualified by the same sentence's "as round 1's fix pass corrected
it". The first invariant is narrower than the old list's last item, and that
narrowing is round 1 finding 1's close.

confirms: none
The crafter's measurement of the core, 8,525 of 10,000 characters, is
consistent with this round's. `core.output(root, root)` over this round's
clone at `6ff6df90` printed 8,661 characters, a margin of 1,339 (executed).
The difference is the clone's path in the header line, which
`frame/design.md:37` says the header carries. Both are over the 1,000 the
frame set for cutting the `Held by` cells.

confirms: none
The narrow modules that read the core and writing-style pass at
`6ff6df90`: 215 cases in nine modules (executed, listed under
`## Probes`). `seal rules --check` printed "all 265 check lines in 54 rule
files hold" (executed), which matches the crafter's count. This round did not
re-run the crafter's 663, and the label for the rest stays as `gaps.md`
gives it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and `seal gate` over the branch, labelled `unverified` in `gaps.md` | the branch at `6ff6df90` | the orchestrator, by `seal gate --base release/v0.26.0 --record` after the rounds settle |
| The crafter's 663 cases over the modules that read the core or writing-style, of which this round re-ran 215 | `skills/core/SKILL.md`, `skills/writing-style/SKILL.md` | the orchestrator's broad run |
| Whether `skills/implement/SKILL.md` *Once the batch is answered, the session runs to the pull request* should say it holds on a run routed `Automation` `yes`, as the `no` box at `skills/implement/orchestration.md:179` lets an attended run ask later; this predates the work item and is outside the fix diff | `skills/implement/SKILL.md`, `skills/implement/orchestration.md:179` | the orchestrator, to file or leave |
| Phases 2 to 5 and their Scope items, outside this round by `frame/plan.md` *Phases* | `frame/design.md` *Scope* items 5 to 14 | the rounds that read those phases |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_core_check.py tests/hooks/test_core.py tests/text/test_review_axes.py tests/text/test_every_agent_reads_the_contract.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_a_language_section_of_writing_style_opens_alone.py tests/behaviour/test_docs_line_wrap.py tests/text/test_the_rules_claude_md_names_have_one_home.py tests/skills/test_payload_meter.py -q`, in a `git clone --no-local` at `6ff6df90` under the scratchpad | 215 passed, exit 0 |
| `bin/seal rules --check`, in the same clone | "all 265 check lines in 54 rule files hold", exit 0 |
| `python3 -c` calling `core.output(root, root)` from `hooks/lib/core.py`, in the same clone | 8,661 characters, 1,339 under `CAP` |
| `git show b993444b`, its removed and added lines sorted and compared | no line unmatched: a pure move |
| `git grep -n` for the old opener's phrase "통과할 수 있는 모양" and the new "검사가 읽는 철자" | the old phrase stands only in round 1's record; the new one stands at `skills/writing-style/SKILL.md:258` |
| `git grep -n -i` for "what it did not read", "names what it did not read", "agent that reads the record" and "기록을 읽는 에이전트", outside the round records | only `frame/design.md:8`, `:27`, `:44`, `:46`, `:48`, `:245`, `:252` and `:272`. `:27`, `:46`, `:245`, `:252` and `:272` say "names as unread" or "what it does with what it did not read", which is the narrow reading. `:259-260` wraps the phrase across a line and was found by reading |

# Round 1 report — 1791852610, the routing question shows the four boxes only under per axis (#911)

Target `bb9eed9b`, base `origin/release/v0.21.1` at `321e9de1`. The whole
build was reviewed, phases 1 to 3. Reading was done in the worktree.
Everything run was run in a `git clone --no-local` of it at the target, in
the session scratchpad. The clone, its virtualenv and the one probe file
were deleted before this report was handed over.

## The shape of what was found

The change does what the spec asks. Every live copy of the retired sentence
is gone or rewritten, and the press reader is byte-identical to the base.
The six divergences the smith recorded hold up on their grounds.

What is wrong is in the prose that explains the new shape, and in one reader
of the old shape that the class sweep missed:

1. The routing section now says the batch rule forbids only a late question
   and not a second click. `skills/implement/SKILL.md` §1, which it cites,
   says the opposite in its own words (🟡 1).
2. `tests/test_chain_hooks_hardening.py` still pins the retired rule in its
   message and comment. Its `in one call` assertion is now satisfied by a
   sentence that means the reverse (🟡 2).
3. The ceiling sentence the build carried into its rewritten paragraph says
   two presets beside the boxes is five. With four boxes it is six (🟡 3).
4. Three smaller items: the resume paragraph reads against the new opening
   (⬜ 4), a reflow left a two-word line in the guard spec (⬜ 5), and
   `overview.md` reports two gaps that the last commit closed (⬜ 6, a
   record correction).

## Spec compliance — stage 1

Each of the spec's six in-scope items was opened against the diff.

- **The procedure.** `skills/implement/orchestration.md` carries the new
  shape in the header paragraph, the section opening, the #88 ceiling
  paragraph, the diagram, the multi-repository subsection and the two
  headings. The act table rows equal the new headings. Read.
- **The block.** `templates/claude-md-block.md` and `CLAUDE.md` carry the
  same bullet. The orchestrator ran `claude_block.py --check` (exit 0). Read.
- **The two pointers.** `skills/implement/SKILL.md:34` and
  `agents/framer.md:275` say the new shape. Read.
- **The reader.** `git diff --quiet 321e9de1 bb9eed9b -- hooks/` exits 0, and
  `hooks/worktree_consent.py` has the blob `079cbb10` at both ends. Executed.
  Rule 3 of `docs/worktree-guard-spec.md` §*Creation consent* says the two
  shapes read the same and why, which matches the code: the loop in
  `hooks/worktree_consent.py#_routing_preset` skips any question whose
  `multiSelect` is not `False`. The new case is listed in the section's
  `Enforced by:` line. Read.
- **The pins.** `tests/test_waiver_decided_at_start.py` (three cases plus the
  smith's case) and `tests/test_review_axes.py` assert the new sentence and
  refuse the old one. Read; green in the orchestrator's run.
- **The records.** The ledger fragment has the S5 row, five `Corrected ·`
  rows and 22 `Re-read ·` rows. Each `Corrected ·` row carries every
  coordinate of the released row it replaces, at the new heading, which is
  what `docs/the-evidence-ledger.md` §*A released row is read again in the
  branch's fragment* requires of it. Read, and the coordinates were compared
  row by row against `seal/releases/0.12.0.md` rows 66 and 68,
  `seal/releases/0.15.5.md` A2, `seal/releases/0.19.0.md` P4 and
  `seal/releases/0.21.0.md` S10.

**The stale-copy sweep.** `git grep` at the target for *two questions*,
*one call*, *same call*, *in ONE*, *boxes beside*, *meaningful only under* and
the old heading, outside released records and earlier work items. What is
left is the bootstrap's own two-question call (out of scope by the spec),
the commit gate's *Both arms, one call* (out of scope), the new rule 3
sentence, and the two items in 🟡 1 and 🟡 2. Executed (the grep), and each
hit read.

**The press under the new shape's real second call.** The S5 case covers
question 1 alone, but not question 1 followed by the boxes in a call of
their own, which is what a `per axis` run now writes. A probe planted that
transcript three ways (all boxes ticked, the first box only, none) plus an
earlier `automation` press taken back by `per axis` and its boxes call. Both
probe cases passed: a boxes-only result answers no routing question, so the
`per axis` before it stands. Executed. It is a case worth planting; see
*Regression tests to plant*.

## The smith's divergences, judged

- **The 14-word sentence.** The frame's sentence is 16 words, and
  `tests/test_no_passage_is_pasted_into_a_second_file.py#test_no_pair_shares_more_than_it_was_measured_at`
  reads a 15-word run shared by two files as a pasted passage. The block
  cannot link to the skill, and `tests/test_review_axes.py` needs one
  spelling in both. Shortening the sentence rather than raising the baseline
  is the right direction. The sentence still names both halves. Accepted.
- **The heading.** The frame's heading is 99 columns and the wrap limit is
  88. The written one is 87 and keeps every fact. Accepted.
- **Five `Corrected ·` rows and 22 `Re-read ·` rows.** A renamed heading is a
  moved anchor, and the ledger rule quoted above says a re-read does not
  clear one. The five families are the ones whose coordinate is the old
  heading. Accepted.
- **The renamed S1 case.** Its old name and docstring stated the retired
  rule. No ledger row or `Enforced by:` line named it; the old name survives
  only in `.test_durations` and in an earlier work item's inventory. Accepted.
- **`agents/smith.md` on the shared STALE tuple.** This is the class sweep
  contract §12 asks for, and it is the step that should also have reached
  🟡 2. Accepted.
- **`### Why these rows` in `spec.md`.** Words unchanged, added at the
  orchestrator's request for #905. Accepted.

## Findings from reading

### 🟡 1 — the routing section says §1 permits a second wait, and §1 says each wait is a cost

`skills/implement/orchestration.md:270-273`:

> Under `per axis` the second call follows the first at once, before the
> first edit, and that is still the one batch the batch rule asks for: what
> it forbids is a question that arrives late, not a second click
> (`skills/implement/SKILL.md` §1).

`skills/implement/SKILL.md:205-206`, the rule it cites:

> Asking one at a time is the same failure spread out: three interruptions
> cost three waits.

§1 does not say a second click is free. It says each interruption is a
wait. The spec's Grounding row attributes the same reading to §1, and §1
does not carry it. The decision itself has grounds: Q1 of `questions.md`
takes the trade from the owner's own *Now / After* table in #911. Only the
citation is wrong.

Why it matters: a session loads both files. Read side by side, one tells it
that two calls are one batch, and the other tells it that two calls are two
waits. The next person who wants to split a question will cite this
paragraph as the precedent that §1 allows it.

The fix says what the trade is, and cites §1 only for what §1 says.

### 🟡 2 — `tests/test_chain_hooks_hardening.py` still pins the retired rule

`tests/test_chain_hooks_hardening.py:1275-1278`, inside
`tests/test_chain_hooks_hardening.py#test_the_questions_are_collected_before_the_work_not_during_it`:

```python
    assert "in one call" in orchestration, (
        "the orchestrator's routing section no longer says the questions go "
        "in one call, which is what makes the batch one wait"
    )
```

and the comment at `:1298-1300`: *`agents/framer.md` does, and says it with
`in one call`, which is the spelling that stays clear of this.*

Both are now false. The routing section says the questions do not go in one
call. `agents/framer.md` no longer contains `in one call` at all, because
this build rewrote its diagram line. The assertion stays green for two
reasons that have nothing to do with its message. One is the new sentence
*Question 1 goes in one call of its own*, which means the reverse. The other
is `orchestration.md:436`, *`write routing.md && git add && git commit` in
one call writes nothing*, which also satisfied it at the base.

The spec named this file and decided to keep the literal, on the grounds
that "that case is about the batch being one wait and still holds". Under
`per axis` it is two calls, so that reason no longer holds. The overview does
not mention the file.

Why it matters: this is a reader of the retired shape, the class contract §12
asks the build to enumerate. Delete the new sentence and this case fails
with a message telling the editor to put the questions back in one call,
which is the shape #911 removed.

### 🟡 3 — "two presets beside the boxes is five"; with four boxes it is six

`skills/implement/orchestration.md:273-275`:

> `AskUserQuestion` allows at most four options per question, and two
> presets beside the boxes is five

The presets are `automation` and `no work item`, and question 2 has four
boxes. Two beside four is six. The sentence has said five since #88, which
already had four boxes (`git show 865a9807:skills/implement/orchestration.md`).
This build reflowed it into the paragraph it wrote, and its own STALE tuple
exists to catch exactly this kind of count in exactly this section. The
conclusion, more than four, still holds.

### ⬜ 4 — the resume paragraph reads against the new opening

`skills/implement/orchestration.md:300-302` puts question 1 again at a resume
*in the same call as whatever else the resume has to ask*. Line 263 now
opens the section with *Question 1 goes in one call of its own*. The reader
handles both, and a resume asks no boxes because `routing.md` already holds
them, so behaviour is right. A session meeting both sentences has to work
out which one governs. Adding *at the start of a work item* to line 263, or
*(the boxes are not put again: `routing.md` holds them)* to the resume
sentence, ends the question.

### ⬜ 5 — a reflow left a two-word line

`docs/worktree-guard-spec.md:981` reads `  Nothing that` on its own, between
the renamed heading reference and *survives a machine move*. Rejoin it with
the next line.

### ⬜ 6 — `overview.md` reports two gaps the last commit closed (a record correction)

`seal/specs/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis/overview.md`
§*Not verified* row 3 says `plan.md`'s approval line still reads
`Approved <date> by <who>`, and §*Not done* says the phases' `Ran by` rows read
`unknown`. At `bb9eed9b` the approval line is filled in (`plan.md:7`) and
all three phases read `specseal:smith on Opus 5.5`. Drop the row and the
paragraph.

## Findings from execution

None of the findings above came from a failing run. What was executed
confirmed: the reader is unchanged, the new shape's second call does not
disturb the press, and four modules that read the edited files and were
outside the orchestrator's set pass.

## Regression tests to plant

Destination `tests/test_the_guard_asks_once_per_session.py`, beside
`test_question_1_alone_and_the_boxes_beside_it_read_the_same_press`. The
transcript a `per axis` run now writes, question 1 alone and then the boxes
in a call of their own, is not yet pinned. The probe below ran green at the
target. Before planting, show it red per contract §15, for instance with a
throwaway edit that makes `_routing_answer` return `True` for any
`multiSelect` result.

```python
def boxes_alone(repo, ticked, tool_id):
    """The second call of the new shape: the four boxes, alone."""
    return ask_entries(
        repo,
        answer=", ".join(ticked),
        options=BOXES,
        multi=True,
        tool_id=tool_id,
        question=BOXES_QUESTION,
    )


def test_per_axis_and_its_own_boxes_call_are_not_the_press(projects, repo):
    """#911. Under `per axis` the boxes come in a second call; that result
    answers no routing question, so the `per axis` before it stands, and an
    earlier press stays taken back."""
    q1 = ask_entries(repo, answer="per axis", tool_id="toolu_q1")
    for ticked in (BOXES, BOXES[:1], ()):
        write_transcript(projects, "me", q1 + boxes_alone(repo, ticked, "toolu_b"))
        assert wc.automation_answered(str(repo), "me") is False, ticked
        assert wc.consent(str(repo), "me") == "", ticked
    earlier = ask_entries(repo, tool_id="toolu_earlier")
    write_transcript(projects, "me", earlier + q1 + boxes_alone(repo, BOXES, "toolu_b"))
    assert wc.automation_answered(str(repo), "me") is False
```

## Facts for the evidence ledger

- `hooks/worktree_consent.py` is the blob `079cbb10` at `321e9de1` and at
  `bb9eed9b`, and `git diff --quiet 321e9de1 bb9eed9b -- hooks/` exits 0.
  Executed this round. It backs the S5 row's *The reader is unchanged*.
- A result carrying only the four `multiSelect` boxes makes
  `hooks/worktree_consent.py#_routing_answer` return None, so it neither
  gives nor takes back the press. Executed by the probe above; a row for it
  belongs with the planted case.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | The routing section says the batch rule forbids only a late question and not a second click, citing §1; §1 says each interruption is a wait | `skills/implement/orchestration.md:270` | open | `skills/implement/SKILL.md:205-206` says *three interruptions cost three waits*; the trade is the owner's from #911 (Q1), not §1's |
| 🟡 2 | A batching test still pins the retired one-call rule in its message and comment, and its `in one call` assertion is satisfied by a sentence meaning the reverse | `tests/test_chain_hooks_hardening.py:1275` | open | Message: *the questions go in one call, which is what makes the batch one wait*; comment at :1298 says `agents/framer.md` uses `in one call`, which it no longer does; contract §12 |
| 🟡 3 | The ceiling sentence the build carried into its paragraph counts two presets beside four boxes as five | `skills/implement/orchestration.md:274` | open | Two presets (`automation`, `no work item`) plus four boxes is six; wrong since #88 (`865a9807`), reflowed by this build |
| ⬜ 4 | The resume paragraph puts question 1 in the same call as other questions, while the new opening says it goes in a call of its own | `skills/implement/orchestration.md:301` | open | Behaviour right (the reader takes both, and a resume asks no boxes); the two sentences need a word saying which moment each governs |
| ⬜ 5 | A reflow left `Nothing that` on a line of its own | `docs/worktree-guard-spec.md:981` | open | Cosmetic; rejoin with the next line |
| ⬜ 6 | `overview.md` reports the approval line and the `Ran by` rows as unfilled; `bb9eed9b` filled both | `seal/specs/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis/overview.md` | open | `plan.md:7` and `phases/phase-1.md:7`, `phase-2.md:7`, `phase-3.md:7` at the target; a record correction, outside `Needs a fix` |
| 🟢 | The press reader is byte-identical to the base | `hooks/worktree_consent.py#_routing_preset` | confirmed | Executed: `git diff --quiet` on `hooks/` exit 0, blob `079cbb10` at both ends |
| 🟢 | Every live copy of the retired *two questions in ONE call* sentence is gone or rewritten | `skills/implement/orchestration.md`, `templates/claude-md-block.md`, `CLAUDE.md`, `skills/implement/SKILL.md`, `agents/framer.md` | confirmed | Executed `git grep` sweep at the target; what remains is out of scope by the spec, or is 🟡 1 and 🟡 2 |
| 🟢 | The smith's six divergences hold on their grounds: the 14-word sentence, the 87-column heading, five `Corrected ·` and 22 `Re-read ·` rows, the renamed S1 case, `agents/smith.md` on STALE, the Removes sub-heading | `seal/specs/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis/overview.md` | confirmed | Each `Corrected ·` row compared coordinate by coordinate with the released row it replaces; the refusing checks named exist at the cited names |
| ❓ | That the harness shows question 1 alone with no boxes, and that a session following the new block puts the second call only after `per axis` | `templates/claude-md-block.md:16` | ❓ out of verified scope | No session was run against the block; the orchestrator answers it at the next routing question it puts from a block carrying this change |

## Executed probes

| What was run | Result |
|---|---|
| `git diff --quiet 321e9de1 bb9eed9b -- hooks/`; `git rev-parse` of `hooks/worktree_consent.py` at both ends | exit 0; `079cbb10` at both |
| `git grep` at `bb9eed9b` for the retired phrasings and the old headings, outside released records and earlier work items | every hit read; the stale ones are 🟡 1 and 🟡 2 |
| One-file test_tmp probe in the clone's `tests/`: `per axis` then a boxes-only call (all, first, none ticked), and an earlier press taken back by `per axis` and its boxes call; run once with `bin/test … -q -p no:xdist`, then deleted | exit 0, 2 passed |
| `SPECSEAL_CASE_CEILING_S=600 bin/test tests/test_first_setup_asks_once.py tests/test_a_signer_declares_its_pact.py tests/test_one_word_one_meaning.py tests/test_a_section_marked_for_one_role_reaches_only_that_role.py -q` in the clone at `bb9eed9b` | exit 0, 2732 passed |
| Broad gate: the full suite, the repository-wide lint and the typecheck | not yet. Not run by this round; it is the sealer's, once the rounds settle |

## Paste-ready fixes

### 🟡 1 and 🟡 3 — `skills/implement/orchestration.md:270-275`

Replaces the paragraph that begins *Under `per axis` the second call follows
the first at once*. The last sentence carries 🟡 3's count.

```markdown
Under `per axis` the second call follows the first at once, before the first
edit. That is a second wait, and it is the trade #911 took: the boxes depend
on question 1's answer, so putting them beside it shows them under the two
answers they mean nothing for. Asked at once and before the first edit, the
second wait still costs a reply rather than a stopped session, which is how
`skills/implement/SKILL.md` §1 prices a question. `AskUserQuestion` allows at
most four options per question, and two presets beside the four boxes is six
— so the shape below is two questions rather than one, and that is what
makes both fit.
```

### 🟡 2 — `tests/test_chain_hooks_hardening.py:1275-1278` and `:1298-1300`

The assertion, pinned on the sentence that now carries the claim. Show it red
by deleting that sentence from the section before committing it (contract
§15).

```python
    assert "Question 1 goes in one call of its own" in " ".join(
        orchestration.split()
    ), (
        "the orchestrator's routing section no longer says question 1 is put "
        "in a call of its own before the first edit, with the boxes after it "
        "only under `per axis` (#911)"
    )
```

The comment lines 1298-1300, from *The second is true* to *stays clear of
this.*:

```python
    # The second is true and a definition may need to say it — `agents/
    # framer.md` does, in its diagram's first line (*asks question 1; boxes
    # only if per axis*), which stays clear of this. A definition that needs
    # the other wording will
```

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

Needs a fix: yes — 🟡 1 (the §1 citation in the routing section), 🟡 2 (the
batching test still pinning the retired one-call rule), 🟡 3 (five for six)

Loses a record or crashes: no

## Proof block

Opened this round: `skills/implement/orchestration.md` (lines 80-549 and the
diff), `skills/implement/SKILL.md` (lines 195-219 and the diff),
`agents/framer.md` (lines 255-290), `docs/worktree-guard-spec.md` (lines
296-340, 525-529, 974-986), `docs/commit-review-gate-spec.md` (lines
525-545), `hooks/worktree_consent.py` (lines 195-285),
`tests/test_the_guard_asks_once_per_session.py` (lines 1187-1307 and the
diff), `tests/test_waiver_decided_at_start.py` (the diff),
`tests/test_review_axes.py` (the diff), `tests/test_chain_hooks_hardening.py`
(lines 1240-1350), `templates/claude-md-block.md` and `CLAUDE.md` (the diff),
`templates/sdd-routing.md` (lines 85-110), `skills/update/SKILL.md` (grep),
`docs/the-evidence-ledger.md` (the moved-anchor paragraph),
`seal/ledger/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis.md`,
`seal/releases/0.12.0.md` rows 66 and 68, `seal/releases/0.15.5.md` A2,
`seal/releases/0.19.0.md` row 9, `seal/releases/0.21.0.md` S10, and this work
item's `spec.md`, `overview.md`, `questions.md`, `changelog.md`, `plan.md:7`
and `phases/phase-*.md:7`. The S1 case's old name was searched for and not
opened.

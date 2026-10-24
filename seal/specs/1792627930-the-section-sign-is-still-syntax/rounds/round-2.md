# Review round 2: 1792627930-the-section-sign-is-still-syntax

target: ea3141ed, fixes a9d9423c..ea3141ed

This verifying round read the fix diff a9d9423c..ea3141ed, in a
`git clone --no-local` of the branch at ea3141ed. It also sampled the phase 4
guidance moves that round 1 left in `## Not judged`; the coordinator asked
for that sample. From round 1 it carried coordinates only: the nine modules
that reach `hooks/blocks.py#fence_only`, and the line numbers of
`APPLIES_THE_SHARED_GUARD`. Every verdict below was reached again in this
round.

## Findings

### 1. Three living sentences still point at guidance that phase 4 took out of the templates

severity: should
location: `agents/framer.md:129-130`, `docs/the-review-and-parity-arms.md:78-79`, `skills/writing-style/SKILL.md:169-170`, `seal/specs/1792627930-the-section-sign-is-still-syntax/spec.md`, `seal/follow-up.md`
evidence: executed `git grep -n -E 'sdd-(spec|plan|questions|routing|overview|phase|round|guarantee)\.md' -- agents skills docs CONTRIBUTING.md README.md hooks`, `git grep -n -i -E "template's|the template (says|states|names|carries|explains|lists|holds)" -- agents skills docs templates CONTRIBUTING.md README.md`, `git show 0d62145a:templates/sdd-routing.md`, `git show 0d62145a:templates/sdd-overview.md`
verdict: fixed 7eb63541

Phase 4 built these units, so this finding takes neither a `regression:` nor
a `reopens:` line. `spec.md` scope item 11 lands each guidance sentence in
what its writer reads. Three sentences elsewhere still send their reader to
the template for guidance that is no longer there.

- `agents/framer.md:129-130` says a `questions.md` row "names who can answer
  it from the template's three values". `templates/sdd-questions.md` now
  holds only the empty `Who can answer` column. The three values moved to
  `skills/implement/SKILL.md` *3. The SDD file set*. The framer is preloaded
  with this definition and acts on it.
- `docs/the-review-and-parity-arms.md:79` says a change that no work item owns
  "takes the third answer of `templates/sdd-routing.md`". At the base, that
  template's comment named question 1's `no work item` answer. The template
  now has no such answer. The answer stands in
  `skills/implement/orchestration.md` *Question 1*, at line 288.
- `skills/writing-style/SKILL.md:169-170` gives as its good example
  "templates/sdd-overview.md 를 열어 보니 diff 가 보여 주지 못하는 것만 적는
  마무리 메모였다". That sentence came from the template's comment, which is
  gone. The template now shows only section placeholders.

The search covered every living mention of a record template, and every
sentence that says a template states something. These three were the only
pointers into removed guidance. The framer fix adds 46 bytes to the framer's
preload, which stays below the base: 25255 at 0d62145a, 25194 at ea3141ed,
25240 after the fix (executed, `evals/scripts/noninferiority.py#preload_bytes`).
The `docs/` sentence changes through `## Rule changes`. Replayed with
`rule_changes.parse` and `apply_op` against the docs at ea3141ed, the item
below parses with no error and is placed (executed).

```markdown
In agents/framer.md, lines 129-130, the sentence ends:
...and names who can answer it, one of the three values of
`skills/implement/SKILL.md` *3. The SDD file set*.

In spec.md, appended to ## Rule changes:
- change
  file: docs/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: declaration: it takes the third answer of `templates/sdd-routing.md`.
  to: declaration: it takes the third answer of question 1, `no work item`,
    in `skills/implement/orchestration.md` *Question 1*.

In skills/writing-style/SKILL.md, lines 169-170 of the example block:
좋음   `skills/implement/SKILL.md` *4. The closing memo — only what the diff cannot show*
       를 열어 보니 마무리 메모였다 → 마무리 메모
```

answer: Holds. `agents/framer.md` now names the three values in `skills/implement/SKILL.md` *3. The SDD file set*, in the record's words. The framer's preload is 25239 bytes against the base's 25255 (executed). The good example in `skills/writing-style/SKILL.md` now opens `skills/implement/SKILL.md` *4. The closing memo — only what the diff cannot show*. The `docs/the-review-and-parity-arms.md` sentence is the framer's to change, through `## Rule changes`. I closed the class with a `git grep` over every living file for "the template's", "template comment", "the template says", "in the template" and the record's two patterns (executed). The search found two more pointers into removed guidance, both in `seal/follow-up.md`. One row quoted the plan template's Status rule, which now stands in the skill. Another said the routing vocabulary is read out of a comment, and since #1005 it is read out of the placeholder. Each row now points where the guidance stands, which is why `location:` gains that path. Every other match names a template's shape, row or placeholder, which still exists. The touched modules and the meta modules pass: 1844 passed (executed).

## Confirmations

confirms: round-1#1
`tests/test_no_living_file_writes_the_section_sign.py#signs` stands in
`APPLIES_THE_SHARED_GUARD` at
`tests/test_a_shrunken_corpus_declines_to_judge.py:183-185`. Round 1's
executed line was run again, inside the run of the seven modules that
dae18434 changed: 1048 passed (executed). The comment beside the row follows
the table's own convention.

confirms: round-1#2
`test_the_fence_walks_agree_shape_by_shape` and its 19 shapes stand at
`tests/test_unverified_rows_close.py:2518-2566`, without the copy half.
Round 1's executed line was run again: the `fence_only` mutation
`return hidden, None`, over the same nine modules, is now red, exit 0
(executed).

confirms: round-1#3
`NEAR_CITATION` and `near_citations` stand at
`tests/test_the_agent_contract_holds_the_universal_rules.py:77-79` and
`368-398`. The tree-wide case and the three shapes pass. The exemption case
`test_the_one_spelling_is_no_near_miss` keeps `contract rule 21` and
`Contract rule 3` unrefused. I narrowed the pattern to
`[Cc]ontract\s+[Rr]ule\s+\d`, and the near-miss cases went red, exit 0
(executed). One spelling still passes unread: a number glued to `rule`, as
in `rule21`. Neither reader reads it, and the smith's sweep found no glued
word on an added line. I judge it no finding.

confirms: round-1#4
`skills/code-review/SKILL.md:130-132` keeps only the `reopens:` half, in the
words round 1 gave. `tests/test_chain_check.py` passes inside the module run
(executed). The `regression:` half stands in `docs/the-review-record.md`
*The run*, in `skills/code-review/orchestration.md` and in
`agents/warden.md`.

confirms: round-1#5
`seal/specs/1792627930-the-section-sign-is-still-syntax/overview.md:24-28`
keeps the `.test_durations` sentence alone, and drops its count. `spec.md`
`## Rule changes` carries the verdict spelling (read).

confirms: none
dae18434 introduced no defect in the units it added or changed. The seven
modules it touches passed, 1048 in all (executed). The restored fence case
uses `importlib`, `os` and `uc`, which the module already imports. The 18
comments now read `section 4.5` and its like. `FENCE_SHAPES` has one home
again, and no other module names it.

confirms: none
This round sampled about a dozen rows of the phase 4 table at
`seal/specs/1792627930-the-section-sign-is-still-syntax/phases/phase-4.md:33-81`,
each read against the base template and its stated home. Each row below
holds at its home (read).
The policy root outranking the spec is at `skills/implement/SKILL.md:86`.
The pact anchor and `pact-check` are at `docs/the-pact.md:79`.
The `## Removes` review is at `docs/the-reader-registry.md:10`.
The `Reframed` line is at `docs/the-review-record.md:507` and
`agents/framer.md:177`.
The mark's `<who>` and its shared shape are at
`skills/implement/SKILL.md:413-417`.
The verdict shapes and the `Answered` line are at `agents/sealer.md:79-85`.
One row per claim is at `agents/sealer.md:121-131`.
The routing rules are at `skills/implement/orchestration.md:358-383`.
The `Status` writer is at `skills/implement/SKILL.md:346-348`.
Two places fall short. The three answerer values are finding 1. One
sentence of `templates/sdd-questions.md` at the base is in no row of the
table and stands nowhere: "Sorting the rows this way also keeps the batch
short enough to answer in one sitting". It is a reason and instructs
nothing, so it is no finding. It does mean the table's claim to place every
sentence is not quite whole.

## Not judged

| What | Location | Who answers |
|---|---|---|
| CI run 39713225557 at ea3141ed, not yet read | the run's logs | the coordinator |
| The full suite, the repository-wide lint and the typecheck at ea3141ed | the whole tree | the orchestrator, through `broad-gate` after the rounds settle |
| The rows of the phase 4 table that neither round sampled, about twenty | `seal/specs/1792627930-the-section-sign-is-still-syntax/phases/phase-4.md:33-81` | the round that verifies finding 1's fix, reading each row against its home |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the seven modules dae18434 changed | 1048 passed |
| `bin/mutation-check hooks/blocks.py`, with `fence_only` returning no unclosed opener, over the nine modules that reach it | red, exit 0 |
| `bin/mutation-check` of `NEAR_CITATION`, narrowed to `[Cc]ontract\s+[Rr]ule\s+\d`, over the near-miss cases | red, exit 0 |
| `noninferiority.preload_bytes` for the framer at ea3141ed, with finding 1's framer fix added as a byte count | 25194 now, 25240 after the fix, base 25255 |
| `rule_changes.parse` and `apply_op` on finding 1's `change` item, against the docs at ea3141ed | no error, placed |

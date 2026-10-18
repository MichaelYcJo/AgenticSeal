# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — review round 7

target: 6cc463d0, fixes 9960f6e4..6cc463d0

## Findings

### 1. The stated double-stamp limit says the clone that drew the stamp draws it again after an amend, which a case on the same rule's line shows it does not

severity: should
location: `docs/the-review-record.md:289-292`, `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/changelog.md:16-21`, `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/overview.md:26`, `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/overview.md:54-59`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:1447`
verdict: fixed 9a1330e8
regression: round-6#1

The unit is the limit sentence d1af2e22 wrote into §*The stamp* and the
fragment, and copied into `overview.md`'s round-3 row and its new Not done
bullet. The frame states the limit for a second clone (`spec.md:88-94`: "the
amend of the sealing commit itself in a second clone"; `plan.md:145` and the
B1 row at `plan.md:157` the same); the fix widened it to the class round 6
asked for and dropped the clone it holds in, taking round 6's own
paste-ready text, which carried that gap, word for word, while the code
comment the same commit wrote keeps it (`seal_stamp.py:926-927`, "in a clone
that holds no values file for the work item").

Why it matters. §*The stamp* now says a `sealed` committed over a history
with no earlier `sealed` "draws the stamp again in that clone: the sealing
commit amended or rewritten there over its own parent". The fragment says "a
clone" does. In the clone that drew the first stamp neither is true:
`_queue_one` asks `already_queued` before it queues
(`skills/verify/scripts/seal_stamp.py:1110-1111`), and that clone's values
file, pending or drawn, stops the amend. The rule's own `Enforced by:` line
names `test_a_recommit_of_the_same_guarantee_queues_no_second_file`, whose
docstring and body are exactly that amend queuing nothing
(`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:667-685`). So
the policy sentence and a case it cites contradict each other, and an agent
or a person who amends the sealing commit where it was sealed is told to
expect a second stamp that never comes. The sentence is one agents read and
act on, which is `should`. Before d1af2e22 the fragment said "a second
clone", which was right on this point.

Executed: the stamp module with the line-wrap, one-word, pasted-passage,
real-identifier and words modules, 131 passed at 6cc463d0, the recommit case
among them (probe row 1). The fix below, applied in the round's clone: the
new assertion failed before the docs sentence changed (`AssertionError: the
limit names the clone it holds in`), then the stamp, line-wrap, one-word,
pasted-passage and changelog modules read 175 passed, `uvx ruff check` and
`uvx ruff format --check` of the test module exit 0, `bin/rules --check`
exit 0; the clone restored by `git checkout` (probe row 4).

Read: `git grep -n -F` under `tests/` pins `draws the stamp again in that
clone` and `the history is the only record the rule reads`; the fix keeps
both phrases. Nothing pins the fragment's or `overview.md`'s sentences.

In `docs/the-review-record.md`, lines 290-292 (from the line opening
`` `sealed`, which draws ``) become:

```markdown
`sealed` in a clone that holds no values file for the work item, which draws
the stamp again in that clone: the sealing commit amended or rewritten there
over its own parent, or a second seal on a copy of the branch that had not
fetched the first. The clone that drew the stamp keeps its values file, so an
amend there draws nothing. That is a stated limit, since across
```

In the fragment, line 16 and line 21 become:

```markdown
  It does not hold where another clone, one that never wrote this work
  item's stamp values itself, commits a `sealed` over a history that
```

```markdown
  tree counts stamps. The clone that drew the stamp keeps its values, so an
  amend there draws nothing. A squash or a cherry-pick of the guarantee onto
```

In `overview.md`, the round-3 row's "still queues in that clone" and the Not
done bullet's opening take the same qualifier:

```markdown
- A `sealed` committed over a history that carries no earlier `sealed`, in
  a clone that holds no values file for the work item, draws the stamp
  again in that clone: the sealing commit amended or
```

And the pin, in
`test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`,
after the assertion on the reason clause, seen red before the docs sentence
lands:

```python
    # #975 round 7's finding 1: the limit names the clone it holds in. The
    # clone that drew the stamp keeps its values file, and an amend there
    # queues nothing (`test_a_recommit_of_the_same_guarantee_queues_no_second_file`).
    assert "in a clone that holds no values file for the work item" in rule, (
        "the limit names the clone it holds in"
    )
```

answer: the record's fix, applied as written. §*The stamp* now states the limit for "a clone that holds no values file for the work item" and adds that the clone that drew the stamp keeps its values file, so an amend there draws nothing; the fragment says "another clone, one that never wrote this work item's stamp values itself" and carries the same added sentence; `overview.md`'s round-3 row and its Not done bullet take the qualifier. The class was enumerated by `git grep` of `had not fetched`, `rewritten there` and `no earlier .sealed` outside the round records: those four places and `seal_stamp.py`'s once comment, which already named the clone, and `questions.md` Q9, which says "a second clone" and is not this pass's. The pin is in `test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`. executed: that case red before the docs sentence changed (`AssertionError: the limit names the clone it holds in`), green after; the stamp, line-wrap, one-word, pasted-passage, real-identifier and words modules 131 passed, the changelog module 52 passed; `uvx ruff check` and `uvx ruff format --check` of the test module exit 0; `bin/rules --check` exit 0. read: `git grep -n -F` of `draws the stamp again in that clone` and `the history is the only record the rule reads` under `tests/` finds only that case, and both phrases stand.

### 2. The memo records the widened limit only as the chosen side, so the sealer reading `spec.md` against the tree meets an amend-only limit the frame calls undecided

severity: should
location: `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/overview.md:26`, `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/spec.md:88-94`, `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/plan.md:145`, `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/plan.md:157`
verdict: fixed 1efe22f3
regression: round-6#1

The unit is `overview.md`'s §*Where spec and implementation diverged*, whose
round-3 row d1af2e22 rewrote. The frame says the limit is the amend in a
second clone and that "this reframe does not decide it" (`spec.md:88-94`;
`plan.md:145`; B1 at `plan.md:157`: "round 3's stated limit, left
standing"); the fix stated a wider class under `questions.md` Q9 (a) and,
as its answer says, left the framer's documents as they read; the defect is
that the memo, the one place the implement skill sends that difference to,
does not quote the frame's side of it.

Why it matters. `skills/implement/SKILL.md:400-401` asks for each divergence
"both sides quoted, which side won, and the grounds". The round-3 row's
Chosen cell now carries the class and its Grounds cell carries Q9 (a), but
its "Spec says" cell still reads "`plan.md` B1 named nothing for a second
clone", which is what B1 said before the reframe and not what it says at
6cc463d0 (`plan.md:157` names the amend in a second clone). Nowhere does the
memo quote `spec.md:88-94` or `plan.md:145`. A sealer reading `spec.md`
§*Scope* against §*The stamp* finds the spec stating one instance and leaving
it undecided, the policy stating a class as decided, and no row saying that
this is a recorded divergence with the frame's words beside the choice. The
same gap reaches `settle`, which folds what is still true of `spec.md` into
`docs/`: the amend-only sentence is the one it would find. The smith was
right not to edit the framer's documents; the memo row is where the
difference goes.

Read: `overview.md:13-28`, `spec.md:88-94`, `plan.md:140-147` and `plan.md:157`,
`questions.md:59`, against `skills/implement/SKILL.md:385-404` and
`templates/sdd-overview.md`. Nothing executes a memo's divergence rows; the
sealer reads them.

A new row after the round-3 row:

```markdown
| The double-stamp limit's extent (round 6) | `spec.md` §*Scope*: "The amend of the sealing commit itself in a second clone, which draws the stamp again there … Q8 was not asked about it and this reframe does not decide it. It stays a stated limit"; `plan.md:145` and its B1 row: "An amend of the sealing commit itself in a second clone draws again there (round 3's stated limit, left standing)" | the class, stated in the fragment, §*The stamp* and `seal_stamp.py`'s once comment: a `sealed` committed over a history that carries no earlier `sealed`, in a clone that holds no values file for the work item, the sealing commit amended or rewritten there over its own parent or a second seal on a copy of the branch that had not fetched the first (d1af2e22) | round 6's finding 1 drew a second stamp from `rebase --force-rebase` and from an unfetched second seal beside the amend (`rounds/round-6.md`); `questions.md` Q9 (a) decided what `spec.md` left undecided: a stated limit, since across clones the history is the only record read and nothing beside the tree counts stamps. The frame's documents are left as written, and this row is where the difference is recorded |
```

answer: the row is in `overview.md` after the round-3 row, as the record wrote it with two changes: `plan.md`'s side quotes the §*Technical context* sentence and the B1 row each in its own words, by section rather than line, and the Chosen cell names 9a1330e8 beside d1af2e22, since finding 1's qualifier landed there. The round-3 row's "Spec says" cell now reads that B1 named nothing for a second clone at round 3 and, since the reframe after round 5, names the amend in a second clone as round 3's stated limit, pointing to the new row. `spec.md` and `plan.md` are left as written. executed: each quoted span checked present in `spec.md` and `plan.md` with whitespace folded (four of four); the one-word, real-identifier, words and pasted-passage modules 40 passed; `bin/unverified-check` exit 0. read: nothing executes a memo's divergence rows; the sealer reads them.

## Confirmations

confirms: round-6#1
The fix states the limit as a class with its reason in all three places the
finding named: the fragment (`changelog.md:16-21`), §*The stamp*
(`docs/the-review-record.md:288-294`, "was stamped then" now "counts as
stamped then") and the once comment (`seal_stamp.py:925-931`), and the pin
carries two assertions (`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:1440-1447`).
Executed: with the sentence through `counts stamps.` deleted in the round's
clone the policy case fails (`AssertionError: the limit says why it is
one`), restored it passes (probe row 3). The class the sentence names
matches the three shapes round 6 executed. The close holds for what round 6
asked; its paste-ready text omitted the clone the limit holds in, and this
round's finding 1 is that omission, reported as a regression of this fix.

confirms: round-6#2
The fragment's once paragraph (`changelog.md:23-30`) now says a `sealed`
that queued nothing because a person committed it outside a Claude session,
or a clone whose hooks slot is somebody else's committed it, counts as the
work item's one stamp, so no later commit of that history draws it, a
corrected row or a re-seal from a clone with the hooks among them; the
second paragraph (`changelog.md:39-42`) points back. Read against the
policy's unchecked paragraph (`docs/the-review-record.md:339-343`), which
states the class, and `_queue_one`, where `sealed_before` refuses before any
session is asked (`seal_stamp.py:1107-1108`). Round 6's probe row 1 executed
the behaviour; the sentence now says it. Local mode is left out with a true
reason: no commit there carries `guarantee.md`.

confirms: round-6#3
`test_a_sealed_item_rebased_and_cloned_fresh_queues_nothing`
(`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:811-851`) is
round 6's fenced case with its body unchanged (a `diff` of the two differs
only in trailing blank lines), and the rule's `Enforced by:` line names it
(`docs/the-review-record.md:296`). Executed: with `sealed_before` changed in
the round's clone to count a `sealed` only where `rev-parse -q --verify
<target>^{commit}` succeeds (`plan.md` B4), `-k 'rebased or recommit'` read
1 failed, 3 passed: the new case failed on the fresh clone's queued line
while `test_a_sealed_item_rebased_in_another_clone_queues_nothing` passed;
restored, 4 passed (probe row 2). So the case holds B4 off where its group
does not.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck: `unverified` by this round | — | the orchestrator's broad run, after the rounds settle |
| Whether `spec.md:88-94` and `plan.md:145`, `plan.md:157` should be rewritten to the class rather than recorded as a divergence (finding 2 takes the memo route, which leaves the framer's documents as written) | `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/spec.md:88-94` | the orchestrator, under the owner's delegation |

## Probes

| Command | Result |
|---|---|
| `bin/test` of the stamp module, `test_docs_line_wrap.py`, `test_one_word_one_meaning.py`, `test_no_passage_is_pasted_into_a_second_file.py`, `test_no_real_identifiers.py`, `test_the_record_is_written_in_words.py` with `-q`, in the round's clone at 6cc463d0 | 131 passed, exit 0 |
| `sealed_before` changed in the clone to the B4 form; `bin/test` of the stamp module `-q -k 'rebased or recommit'`; the file restored by `git checkout`; the same run again | 1 failed (`test_a_sealed_item_rebased_and_cloned_fresh_queues_nothing`, the queued line printed), 3 passed; then 4 passed |
| §*The stamp*'s sentences from `That is a stated limit` through `counts stamps.` deleted in the clone; `bin/test` of the stamp module `-q -k test_the_policy_names_what_enforces`; restored; that case and the recommit case again | 1 failed (`AssertionError: the limit says why it is one`); then 2 passed |
| finding 1's fix applied in the clone: the new assertion first, `bin/test -k test_the_policy_names_what_enforces`; then the docs and fragment lines; `bin/test` of the stamp, line-wrap, one-word, pasted-passage and changelog modules `-q`; `uvx ruff format --check` and `uvx ruff check` of the test module; `bin/rules --check`; the clone restored by `git checkout`, `git status --short` | 1 failed (`AssertionError: the limit names the clone it holds in`); 175 passed; exit 0, exit 0; exit 0; clean |
| this record: `chain_check.py --baseline f6ae6db6 --root <the branch worktree> --worktree`; staged in the clone, `bin/test` of `test_no_real_identifiers.py`, `test_the_record_is_written_in_words.py`, `test_one_word_one_meaning.py`, `test_no_passage_is_pasted_into_a_second_file.py` with `-q` | two refusals for this record, each finding's `verdict: open`, beside the absent `broad-gate.md` and `guarantee.md`; 40 passed |

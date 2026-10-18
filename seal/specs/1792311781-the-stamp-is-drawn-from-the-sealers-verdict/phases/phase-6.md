# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — phase 6

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | b2f97fb1 |


## What this phase was asked

The reframe after round 5, under `questions.md` Q8 (a): once per work item
takes the never-twice direction. The case first:
`test_a_sealed_item_rebased_in_another_clone_queues_nothing`, the body of
`rounds/round-5.md` finding 1's fenced case unchanged, placed after
`test_a_sealed_item_recommitted_in_another_clone_queues_nothing` and seen red
against `seal_stamp.py` as 96cd142b carries it. Then `sealed_before`'s loop
body back to round 3's, with the `target_of` call and its `merge-base`
removed; `sealed_before`'s and `queue_for_guarantee`'s docstrings and the
once comment saying that a `sealed` that drew nothing counts too and the
missing stamp is #976's gap; `test_a_seal_that_queued_nothing_does_not_count_as_stamped`
removed with no twin. In `docs/the-review-record.md` §*The stamp*, the
sentence back to round 3's words, the removed case's entry on the
`Enforced by:` line replaced by the new case, and one sentence added to the
unchecked paragraph, its phrase pinned in
`test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does` and
seen red first. The fragment's clause rewritten in the same commit. No
agent definition, `questions.md`, `agents/sealer.md` or the contract.

## What this phase found

**The case was red where the plan said** (executed): at 5f43a5c3's
`seal_stamp.py` the new case failed on `assert after_the_commit(other) == ""`,
the second clone printing the queued line for a second values file after
the rebase and the fresh `sealed` row. With round 3's loop body it passes,
and the stamp module reads 50 passed (51 cases before, one added, one
removed). `grep -c does_not_count_as_stamped` of the module reads 0.

**The pin was red before the sentence** (executed): the `silence` tuple's
new entry `already read \`sealed\` and that verdict drew nothing` failed
against the unchecked paragraph as it stood, and passes with the sentence.

**The mutation the plan named turned both cross-clone cases red**
(executed): `mutation-check` replacing `if sealed_before(chain, top, ...)`
in `_queue_one` with `if False:` printed `red`, failing
`test_a_sealed_item_recommitted_in_another_clone_queues_nothing` and
`test_a_sealed_item_rebased_in_another_clone_queues_nothing`, and restored
the file by its own copy.

**The frame's last check cannot print nothing as written.** `plan.md` row 6
verifies with `git grep -n -F -e 'over a commit then in its history' -e
'corrects that row in place' -- ':!seal/specs/*/rounds/' ':!seal/specs/*/overview.md'`
printing nothing. Two things keep it from holding literally: `plan.md` rows
6 and 7 and `spec.md`'s two *Reframed after round 5* rows of `## Removes`
quote both phrases as what is removed, and the `:!` pathspec with a
trailing slash does not exclude the round records, so `rounds/round-4.md`
and `rounds/round-5.md` print too. Read as meant, it holds: with
`:(exclude,glob)seal/specs/**` nothing prints, and with the rounds and the
memo excluded by glob magic only the frame's own four quoting rows print.

**A line opening with `#976` was avoided in the unchecked paragraph.** The
plan's sentence ends `the gap #976 carries.`; wrapped at the file's width
`#976` opened a line. GFM reads no heading there, since `#` needs a space
after it, but the wrap was moved so the line opens with `gap`.

**What was not changed, by enumeration** (§12, read): every other
statement of the once rule was found with `git grep` for `once per work
item`, `stamped then` and `sealed_before`. `chain_check.py#earlier_verdicts`'
docstring, `tests/test_the_sealer_guarantees.py::TestEarlierVerdicts`,
`hooks/sealer-stamp.py`, `skills/verify/SKILL.md` and the module's own
header speak of the earlier-run chain or of once per work item without the
ancestry condition, so none of them carried round 4's narrowing.

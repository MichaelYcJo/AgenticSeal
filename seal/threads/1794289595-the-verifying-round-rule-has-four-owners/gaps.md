# Closing memo: 1794289595-the-verifying-round-rule-has-four-owners

## Not verified

- nothing
  why: the two phases changed rule text in seven files, one test file and the version in `.claude-plugin/plugin.json`, and the round 1 fix pass changed one rule file, the test file and `changelog.md`; each claim they rest on was run or read, as `trail/phases/phase-1.md`, `trail/phases/phase-2.md` and the close blocks of `trail/rounds/round-1.md` record; the broad gate is the orchestrator's.

## Not done

`docs/forms/the-round-record.md` *The round record*, the paragraph **Each
round answers to the next by reference**, still states the three relations
in its own words. `frame/design.md` *Grounding* G7 keeps it as the form the
check reads, so phase 1 left it. After phase 1 its wording and the
definition in `skills/code-review/SKILL.md` *Earlier rounds* are two texts
a later edit can move apart, and no case compares them.

Phase 2 left three sentences that say a commit outside the work item's
records is read by a round. None states the condition on which the sealer
reads a change, so none is a second statement of the exception, and
`frame/design.md` *Scope* item 5 lists none of them. Each restates the
first half of the core's row in its own words, and no case compares it with
the row.

- `skills/code-review/orchestration.md` *Orchestrator: the pull request
  opens once the sealer seals*, the sentence "Where the merge resolved a
  conflict in a file outside the work item's records, the orchestrator
  spawns a verifying round on that resolution". Its grounds are its own:
  the check reads no merge commit.
- The same section, the paragraph **The stated limit**, "Its fix is a
  commit outside the work item's records, so it takes the repair path
  below". It states a fact about one kind of fix.
- `docs/running/the-review-and-parity-arms.md`, the row *through the review
  chain*, "the last record's `target:` commit at HEAD or followed only by
  the work item's own records". It says what the check reads, as the `Held
  by` cell of the core's row does.

The round 1 fix pass added one sentence to `skills/code-review/SKILL.md`
*Earlier rounds*: where the close of the finding whose fix made the unit
holds as well, a `confirms:` line names that finding too, so two lines
name it. No case holds that sentence. A `seal mutate` run that took it out
survived `tests/text/test_the_rules_have_one_owner.py` and
`tests/text/test_review_axes.py`. The fix pass left it unpinned. The
`RULES` row 21 pins the sentence before it without "exactly", so the
contradiction round 1 found cannot come back without a red case. The
sentence itself restates what `docs/forms/the-round-record.md` *The round
record* and `skills/code-review/scripts/chain_check.py#channel` already
allow. `frame/design.md` *Scope* item 7 names two rows and no third, and a
third would add a pin no round has yet needed.

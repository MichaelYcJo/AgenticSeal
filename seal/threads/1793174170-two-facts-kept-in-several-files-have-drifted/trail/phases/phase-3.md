# Phase 3: 1793174170-two-facts-kept-in-several-files-have-drifted

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 255bde09 |

## What this phase was asked

Build `frame/plan.md`'s phase 3, one home for each pasted passage. The way
back before the commit to shared is told in `skills/config/SKILL.md` only,
and both READMEs link to it (S6). `skills/implement/SKILL.md:355-359` links
to `docs/the-agent-set.md` (S7). Both `BASELINE` entries are removed.
`frame/questions.md` Q1 is built on its default: the passage is found by
its words at the branch tip, not by its line numbers.

## What this phase found

- **Q1 met its first option.** `skills/implement/SKILL.md` still held the
  sentence at `:355-359` at the branch tip, found by its words "split it
  records" and "account of what got built". #1110 had not reached this
  branch, so the sentence was replaced by the link as framed. No other
  line of that file was edited (read).
- **S7 seen red, then green.** With the two entries taken out of
  `BASELINE` and the passages unchanged, `test_no_pair_shares_more_than_it_was_measured_at`
  failed with exit 1: `README.md` and `skills/config/SKILL.md` shared 21
  runs of 15 words, the longest 35, and `docs/the-agent-set.md` and
  `skills/implement/SKILL.md` shared 20, the longest 34. After the
  rewrites the module passed, 8 cases, exit 0 (executed).
- **S6 seen red, then green.** The re-pointed
  `test_the_readme_gives_both_moves_under_first_run` failed for both
  editions, and the new `test_the_way_back_before_the_commit_to_shared_is_told_in_its_home`
  failed on "refuses a switch over a staged change", exit 1, 3 failed.
  After the edits the module passed, 51 cases, exit 0 (executed).
- **The skill section's new case.** The frame names the re-pointed README
  case as S6's proof and says the skill section takes in the README's
  reasons. Nothing pinned those reasons in the skill, so a second case in
  the same module reads the section and requires the command, the
  staged-change reason, the pathspec reason and the citation of
  `docs/one-root-by-lifetime.md` *Shared or local*.
  `tests/text/test_the_settings_have_a_front_door.py` was not edited, and
  it passed, 18 cases, exit 0 (executed).
- **The README sentence was rewritten past the passage.** Taking out the
  way back alone was not enough. The README's "taking them out of the tree
  later does not take them out of it" shared 19 words with the skill's
  sentence on the point of no return. So the README says the commit puts
  the records into the history for good, and the skill says the records
  stay in the history whatever later leaves the tree. Neither shares a
  15-word run with the other now.
- **What still states the way back, and why it stands.** `git grep` on
  `git reset -- :/seal` and "guard has never looked" outside the records
  finds the skill section, two test pins, and the text `seal mode shared`
  prints (`skills/implement/scripts/seal.py:2546-2556`, pinned by
  `tests/skills/test_seal.py:3137`). `frame/design.md` *Out of scope*
  keeps the printed text, because a person reads it at the moment of the
  switch. `agents/framer.md:24` says "becomes an account of what got
  built" about the framer writing no code. It is a different sentence,
  `BASELINE` has no framer and agent-set pair, and the check passes, so
  it stays (read).
- **Each new unit was mutated, and each went red.** `seal mutate` printed
  `red` with exit 0 for six mutants: `git reset -- :/seal` written back
  into `README.md`, the link's heading cut in `README.ko.md`, and in the
  skill section "unstages the whole index", the policy citation and
  "staged" each changed. The sixth pasted the removed sentence back into
  `skills/implement/SKILL.md` against the passage check (executed).
- **Every module that reads a file this phase changed ran green.** Found
  with `git grep -l` on the README names, `CONTRIBUTING.md`,
  `test_durations`, the two skills' paths and the two changed test
  modules, 66 modules, one per call, each exit 0 (executed). `uvx ruff
  check` and `uvx ruff format --check` passed over the two changed test
  files (exit 0, executed).

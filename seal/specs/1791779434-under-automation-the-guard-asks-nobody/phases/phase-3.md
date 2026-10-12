# 1791779434-under-automation-the-guard-asks-nobody — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | d92a6daa |
| Ran by | unknown — the spawn prompt named neither the agent nor the model, and a segment does not supply that value about itself |

## What this phase was asked

The reframe after round 3, approved at `34c26823`. The deny under the press
says only what the guard read and what the guard does: that the row blocks
while tracked changes exist, that `git commit` and `git stash`, run alone,
pass the guard, and that the model chooses and git's output reports the
result. It predicts nothing about any switch form. S12 pins one identical
text across round 3's sixteen setups. The three prescription cases are
removed (W4). The attended `ask` stays byte-identical (S2), S8 holds, and
the press sentence does not change by one byte, because #896 copies it.

## What this phase found

**W3, the text.** It opens with the row's lead, now followed by *so no other
row of this guard stops the switch*. The first frame wrote *so the switch
itself may go ahead* there, and git refuses `--orphan` over the changes, so
that clause was a prediction too. The listing and the phantom note are as
before. Then come the press sentence, byte-identical, and one sentence on
what the row does. *The ways on, none of which needs a person* follows with
the *Issue each command on its own* sentence, unchanged. Then: `git commit`
and `git stash` are on this guard's list and pass it alone, and which fits,
and what to run after, is the model's to decide, reported by git's own
output. The re-issue sentence ends it. Every command carries `git_at`'s
word, as before. The Korean half follows the same order. Its count sentence
now says *추적 파일 변경*, matching the stop's own wording.

**W4, the removals and the word list.** Removed:
`test_a_creating_switch_under_the_press_takes_the_stash_way` (NAME NOT IN TREE),
`test_an_orphan_switch_under_the_press_takes_the_commit_way` (NAME NOT IN TREE) and
`test_the_deny_does_not_say_a_discarding_switch_carries_the_changes` (NAME NOT IN TREE). Each form they ran is a row of S12,
so none is lost as a setup. S4 keeps both commands and the switch after
each, with real git, and drops every assertion about where the change ended.
S12's negative check takes every option-shaped word
(`(?<![\w-])--?[A-Za-z][\w-]*`) rather than a fixed list. A form a later
round names is then caught without editing the list, and `-C` needs no
exception, because in S12 the shell stands in the switch's tree and the
command word is plain `git`. The prediction words are `pop`, `way 2`,
`squash`, `carries`, `conflict` and `detached`. S1 checks the same words.

**How S1 and S12 were seen red.** Both were run against the guard as it
stood (unchanged since `04f450ea`, the same bytes as at `0f1663f5`): 17
failures, all on the pinned text. The word check alone was applied to
`0f1663f5`'s pinned `dirty_deny`, which that commit's S1 asserted equal to
the hook's output. It found `-c`, `--orphan` and `--show-current` in both
languages, and `pop`, `way 2`, `carries` and `detached` in English. The
equality half was shown through `mutation-check`: a per-form clause
(`({command[11:18]})`) planted in the count sentence turned all sixteen S12
rows red.

**The policy's `Enforced by:` line moved in this phase**, ahead of the
plan's phase 4. It named the three removed cases, so
`tests/test_a_folded_statement_names_what_enforces_it.py` would have failed
at this phase's close. The paragraph's prose is phase 4's.

**Records naming the removed cases carry the checker's marker.**
`tests/test_a_record_states_what_the_tree_has.py` refused 23 lines across
`spec.md`, `plan.md`, `questions.md` and six round records, each naming a
removed case. Each line now carries `NAME NOT IN TREE`, the repair the
checker prescribes. In a table row the marker sits inside the last cell, so
no parser meets a new column. The round records keep every verdict and
ground as written.

**The ledger rows describing the code moved with it.** S1, S4 and
`Corrected · S2` are restated, and S12 is a new row held by its test. S9
describes the policy text and moves in phase 4.

**`git grep` over the hook for `--orphan`, `way 2` and `stash pop`** finds
nothing anywhere in the file (exit 1), not only in the pressed block.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| The deny's per-form recipe: commit first with its `-c`, `--orphan` and detached-HEAD clauses, the stash sequence with its pop, and the *a switch that keeps them carries them* premise | nowhere, by the reframe's decision (`spec.md` §*Why the deny predicts nothing*); S12 keeps any of it from coming back as a clause |
| The three recipe cases of rounds 1–2 | S12's sixteen rows hold every form they ran; S4 holds the two commands passing the guard |
| S4's assertions about where git left the change | nowhere: the deny promises no outcome |

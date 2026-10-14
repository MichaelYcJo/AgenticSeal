# 1791940762-the-record-of-truth-is-tests-not-coordinates — phase 8

| Field | Value |
|---|---|
| Phase | 8 |
| Commit | written when the phase closes |
| Ran by | smith on Opus 5.5, as the attribution line in the spawn prompt names it |

## What this phase was asked

Q3, answered by the owner on 2026-10-15 with option 2: remove `Pact notify`
and the one-spelling machinery of #759, measured first against what that
rule ever caught. First the measurement, here, executed apart from read.
Then `hooks/config.py#pact_declaration` stops reading `Pact notify`, and
`pact_lines_not_read`, `HTML_CELL`, `UNDER_A_HEADER`, `PACT_WORD` and every
caller, case, message, constant and sentence that stood only on them go in
the same commits; `chain-check` and `pact-check` stop printing the value;
`templates/config.md`, `skills/config/SKILL.md`, `docs/the-pact.md`, the
routing step's row and this item's `changelog.md` are rewritten in place,
and any `seal/budgets.md` row the cut lowers goes down. What a `Pact notify`
row left in a user's `seal/config.md` does afterwards is decided and stated
once, in the one place the config rules live. Anything else found standing
only on the removed fact goes too; a removal whose premise proves false is
stopped and reported.

## What this phase found

**The measurement: the rule never caught a real config.**

| What | Found | How |
|---|---|---|
| the issue | #759, found in round 1's fix pass of #756: a `\| Pact notify \| always \|` written after the config table ended was read as the default, so under `always` a moved ledger row citing no clause was re-stamped with no pact change recorded | read, `gh issue view 759` |
| what it cost | a first design, #784, closed unmerged after four review rounds each found spellings it missed; the redesign, #793 (1e2b2ed5, 2026-10-05), took 31 files and 5,550 lines in, four more rounds and a post-review fix (#794) | read, `gh pr view 793`, `git show --stat 1e2b2ed5` |
| commits that changed its units since | #827 (the signer rename), #882 (#867), #925 (#871), #901 (#834's inventory), #895 (#835), and this item's 0655544e, 9c9b99fb, 6506a26f | read, `git log -S pact_lines_not_read`, `git log -S UNDER_A_HEADER` |
| issues citing it | #794 (its own three whites), #834 and #867 (cited as the pattern *read one spelling, refuse the rest*), #754 and #779 (flow measurements of its segments) | read, `gh search issues '#759'`, `'"Pact notify"'` |
| a real config it refused | none. This repository's `seal/config.md` has never held a `Pact` line on any ref, and no issue reports a refusal from an installed repository | executed, `git log -p --all -- seal/config.md` (0 lines naming `Pact`); read, the two searches above |
| what its refusals did fire on | the corpus built from #784's four rounds, 2,649 cases of `tests/test_a_signer_declares_its_pact.py` priced at 36.4 Windows seconds; and `templates/config.md` copied whole, the rule refusing the plugin's own template (round 1 of #793, a defect of itself) | executed, `bin/test --collect-only`, the `.test_durations` sum; read, PR #793's body |
| its premise | gone: the records `always` chose rows of lost their writer in phase 4 and their reader in phase 7 | read, `phases/phase-4.md`, `phases/phase-7.md` |

**#871's walker already refuses the shapes #759 was opened about.** A probe
over `hooks/config.py` at 0f4e11d1 (executed): a `Pact notify` row written
below a blank line, below prose, or under a second table is refused by
`config_table` for any item, the one-spelling machinery aside. What only
the machinery refused was a pact row under a heading, inside a fence or a
comment, or spelled another way (`**Pact notify**`). Once `Pact notify` is
gone, those shapes matter only for a `Pact` row, and a `Pact` row the walk
does not read leaves the signer with no row at the pact's repository:
`pact-check` reads it `ONE-SIDED` and exits 2
(`skills/verify/scripts/pact_check.py#check`, held by
`tests/test_pact_check.py::test_s11_a_relationship_recorded_on_one_side_is_refused`;
read). So the removal's premise holds: nothing live needs the rule.

# 1791940762-the-record-of-truth-is-tests-not-coordinates — phase 8

| Field | Value |
|---|---|
| Phase | 8 |
| Commit | a8d02ea5 |
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

**A leftover `Pact notify` row is read by nobody, and nothing names it.**
Decided here and stated once, in `templates/config.md` §*Pact*: in the
table, no command refuses, prints or names it, like any item no reader asks
for; below the table and above the next heading it is the walker's
refusal, as any row there is.
Naming it would keep a reader alive for a row that changes nothing, and a
refusal would stop `pact-check` at the pact's repository over it. This is
also how phase 5 left the `Ledger frozen from` and `Removes from` rows.
Three cases hold it, one per reader's caller, each seen red by one
mutation that refused the row again.

**One more unit stood only on the rule.** `hooks/config.py#indexed_config_rows`
had no caller in code, and its docstring gave the rule as its one reason;
it goes, with its assertion in `tests/test_the_mode_question_is_asked_once.py`,
whose `config_table` assertion beside it already holds the same rows.
`gfm_table_oracle.rows_under` stays: `tests/test_one_table_walker_reads_what_gfm_renders.py`
calls it.

**What left, by commit.**

| Commit | What |
|---|---|
| f873c26c | the measurement above |
| 535ccaf2 | `Pact notify` and the one-spelling machinery, with `indexed_config_rows`: `pact_declaration` returns `(pacts, refusals)` and `declared_pacts` the same or None; `chain-check`'s notice and `pact-check`'s `READ` line drop the value; `tests/test_a_signer_declares_its_pact.py` from 2,649 cases to 50, the two notify cases and #759's S7 in `tests/test_pact_check.py` and the notify parameters and #759's S8 in `tests/test_a_signers_ci_prints_its_pact.py` replaced by one leftover-row case each; the walker table's `pact_lines_not_read` row; `templates/config.md` (the table row, the vocabulary bullet, §*Pact*), `skills/config/SKILL.md` (nine rows), `docs/the-pact.md` (two statements out, one rewritten, one sentence), the routing step's row, `changelog.md`; `declared_pacts`, `doubled_row` and `chain_check.py#pact_notices` declare and leave `tests/undeclared_readers.txt`, and `pact_line_refusal` leaves it; `unenforced:templates/config.md` 34 → 31 |
| a8d02ea5 | a doubled `Pact` row keeps the walker's refusal last, which `mutation-check` showed no case watched once the notify arm left |

**What `git grep -n 'Pact notify'` still names, and why.**

| Where | Why |
|---|---|
| `templates/config.md` §*Pact* | the leftover-row statement, the one place it is said |
| `hooks/config.py#pact_declaration` | the docstring sentence pointing at that statement |
| the three pact test modules | the leftover-row cases and the template pin |
| `.test_durations`, 648 lines | ids of deleted cases; 2,609 entries for the three modules' deleted cases (55.5 s) stay for the refresh's `--clean-durations` |
| `changelog/0.18.0.md` to `0.19.0.md` | released entries |
| `seal/specs/*` of ten earlier work items, and this item's records | process records, retired by `settle --retire-process` |

**Verification, executed unless named.** The three pact modules, the
settings, line-end, mode-question, census and one-reader modules: 558 cases,
three red on a first spelling whose `notify` assertion matched the test's
own temp path, then green. Every test module naming a changed file, 66
modules: 4,385 passed, 9 skipped. The encoding and interpreter modules: 173
passed. `budget_check.py` exit 1 on the tree until the template's row was
lowered, then exit 0 on the tree and against `origin/release/v0.22.0`.
`uvx ruff check` and `ruff format --check` on every changed Python file,
exit 0 after one `RUF005` fix. `mutation-check`, each `red`: the reader
refusing a leftover row (five cases in three modules), `pact-check`'s `READ`
line and `chain-check`'s notice naming the value again, the template's
statement and the skill's `nine` reworded, the walker's refusal dropped
from each of `pact_declaration`'s three returns, and `declared_pacts`
returning the old `None` notify for no file.
`test_the_durations_file_prices_the_suite` is red: 617 of 9,208 collected
cases unpriced (6.7 %), the same refresh `overview.md` §*Not verified*
names. The full suite is the sealer's.

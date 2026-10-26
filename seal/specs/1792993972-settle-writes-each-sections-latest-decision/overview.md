# Overview: settle writes each section's latest decision (#1033)

## Why this work exists

`settle` refused or held every released spec whose `from` had gone stale and
every directory with an open row, so the 0.22.4 settle could move nothing; now
the script shows the specs by section and removes, the settling session writes
each section's latest decision and closes the rows, and CI reads a whole
removal of a directory that stood at the base as a settle.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| When `replay`, `apply_op` and `_cut` leave | `plan.md` phase 1: "`rule_changes.py` ... loses `replay`, `conflicts`, `_ancestor`, `apply_op` and `_cut`" / phase 1 removed `conflicts`; phase 2 removed the other three | the code | `unverified_check.py#settled` called `rules.replay` until phase 2 rewrote it; removed in phase 1, `settled` would raise `AttributeError` between the two commits for any removed directory that states a rule |
| `_ancestor` | `spec.md` *Data & interfaces*: "It loses `replay`, `conflicts`, `_ancestor`, `apply_op` and `_cut`", and "gains one function that groups ordered specs" / `_ancestor` stays, and `rule_changes.py` gains `group`, `section_lines` and `unordered` | the code | S5: "they are one group with the pair marked unordered". Marking a pair that no ancestry orders needs the ancestry read, which is `_ancestor`; `unordered` reads it |
| S8's cases | S8: "the existing cases in `tests/test_unverified_check.py` (`test_refuses_a_removal_no_settle_explains` and the fewer-rows cases), passing unchanged" / three cases were rewritten | the code | under *In* item 4's predicate a directory removed whole is a settle, so the shapes those cases held as deletions now settle: in `test_refuses_a_removal_no_settle_explains` a directory with an open row and one whose spec was dropped; in `test_refuses_a_record_that_left_whole` a renamed directory, a deleted `specs/` and a deleted work item; in `tests/test_chain_check.py::Test_retired` two of the three `nothing-absorbing-it` shapes and the second half of `test_accepts_every_declaration_leaving_with_the_root`. Each keeps or gains a shape that is still a deletion (a memo removed from a directory that stays, a `routing.md` deleted beside a `spec.md` that stays), and the whole-removal shapes became accepting cases |
| `policy_documents` and `SPEC` | `spec.md` *Removes* names `wrote_a_spec` and `here` "where nothing else calls" them / `unverified_check.py#policy_documents`, its two cases, and the `SPEC` constant went too | the code | each was read only by the replay inside `settled`; contract rule 12 asks for the class, not the instance |
| What the dry run lists as removed | *In* item 1: "the citations into what `--apply` would remove, as today" / it lists every released directory, `now` or `once its N open rows close`, with the citations into each | the code | on the real tree every one of the 41 records holds an open row (S10), so the directories `--apply` would remove now are none, and the citations the settling session needs before the removal would never print |
| `pattern`'s cases | `spec.md` *Removes*: `tests/test_rule_changes.py::Test_replay` (all eleven cases) / they went, and `Test_pattern` holds the two properties of the kept `pattern` they were the only cases of | the code | `pattern` stays (*Data & interfaces*) and the dry run's `from found` and `to found` read it; a rewrapped sentence and a word inside another had no other case |
| The procedure case's docstring | `plan.md` phase 3: "its docstring's sentences on rounds 1 and 2 give way to one on round 3" / the docstring keeps round 1's "a row that fits two kinds has one reading" and drops its half on step 6's set | the code | the case still asserts "A row that fits more than one kind takes the first that fits", so that half still describes what the case holds |
| Places beyond *In* item 7 | *In* item 7 names `skills/implement/SKILL.md` line 75 / line 340 ("the rule changes `settle` applies to the policy root"), `tests/test_the_retired_rules_await_their_settle.py`'s docstring and `unverified_check.py#live_lines`'s note on "the `settle.py` caller" were rewritten too | the code | contract rule 19: each stated the old fact; `apply_op` was that caller |

## Not verified

| Item | Who must answer |
|---|---|
| closed the new and rewritten cases of `tests/test_settle.py`, `tests/test_rule_changes.py`, `tests/test_unverified_check.py` and `tests/test_chain_check.py` on Windows | the branch's `tests` workflow run 40292155366 at `548a7a4b` passed every leg, the four Windows groups included |
| closed the full suite, the repository-wide lint and format check, and the typecheck at the branch head | `broad-gate.md` records the run at `8a32ccac` against `2974871d`; its printed report read BROAD GATE PASSED, ruff check and format clean, the suite 6,522 passed and 14 skipped, chain-check exit 0. The repository has no typecheck to run (#951 adds one) |

## Not done

Running the settle. `spec.md` *Out* leaves the 0.22.4 settle to the owner,
after this merges into `release/v0.22.4`, with the tree's script
(`plan.md` *Operational impact*); S10 ran the dry run read-only and nothing
else.

The prices of the cases `.test_durations` already held. The branch's removals
left 96 entries the suite no longer collects, which turned
`test_the_durations_file_prices_the_suite` red on run 40282308738, so the file
now takes that run's `test-durations` artifact's entry set: the 96 entries go
and the 133 cases the file lacked take the artifact's prices. The other 6,403
entries keep their committed prices, because the artifact rewrites every line
of the file and an edit made through the `Edit` tool carries the changed
entries only; the next refresh from a `tests` run replaces them.

## Fed back into the spec

Inferred during implementation, for a planner to overturn:

- The dry run's line shapes (`questions.md` Q4), recorded in
  `phases/phase-1.md` and pinned in `tests/test_settle.py`.
- What counts as a named path in an open row: a backticked span with a `/`,
  or a file name with an extension this repository uses, looked for from the
  root, from the work item's own directory, and as a tracked file's name.

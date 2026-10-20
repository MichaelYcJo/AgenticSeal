# 1792449518-settle-squashes-specs-into-docs-in-place — review round 2

target: fedc2790, fixes a8bd7772..fedc2790

This is a verifying round over the fix pass `a69a1c6e` to `e9879bbd`, its
record commit `0e93d61d`, and the orchestrator's record-only `fedc2790`.
From round 1 it carries coordinates only: the lines each finding named, and
the probe in its `## Probes` row. Every verdict below was reached again at
fedc2790. Round 1's `executed` lines were re-run. The four relayed CI cases
ran again, now green. The round-1 probe was written again from its row,
extended to a grandchild heading and to a parent heading named later, run
once and deleted. Each new case the fix pass added was also run against
round 1's code (the four scripts checked out at a8bd7772 in the clone, then
restored), and every one of them failed there.

## Findings

No finding. Each close holds, and the new units the fix pass added hold
when read as code. The two copies the orchestrator named are judged under
`## Confirmations`.

## Confirmations

confirms: round-1#1
`skills/code-review/scripts/chain_check.py:1770` binds the settle sentence
as `SETTLE_SAYS`, and its one use at line 1861 reads that name. Line 91's
`RETIRED_SAYS` is bound once again, so line 1687 prints the old-verdict
sentence. `tests/test_the_sealer_guarantees.py::test_the_old_words_are_refused_by_line`
passes at fedc2790. Executed.

confirms: round-1#2
`tests/test_settle_reads_before_it_removes.py:815` and
`tests/test_waiver_decided_at_start.py:715` each name the whole heading,
`Document layout — two roots, three lifetimes`, in one literal on one
line. The smith claimed the citation scan reads source lines, so a literal
split over two lines would fail again. The red run at a8bd7772 and the
green run here agree with that claim.
`tests/test_the_set_a_work_item_always_has.py::test_every_cited_heading_of_implement_exists`
and both pins pass. Executed.

confirms: round-1#3
The helper at `tests/test_settle_applies_rule_changes_in_place.py:400-405`
passes `encoding="utf-8"` in place of `text=True`, and the encoding module
passes. Executed.

confirms: round-1#4
`ruff.toml:49` lists `skills/settle/scripts/rule_changes.py` at `py39`, and
the interpreter-floor case passes. The answer says `fold_check.py` stays
out of that set. That holds: the fix makes `fold_check.py` load
`unverified_check.py`, which runs in the floored set, but nothing in the
floored set loads `fold_check.py`, and the case found no unfloored file.
Executed.

confirms: round-1#5
`skills/settle/scripts/rule_changes.py:166` refuses a `file` holding `\` or
`:`. The re-written probe parsed round 1's four Windows-shaped values, and
each was refused as "not a top-level docs/ file". `skills/settle/scripts/settle.py:293-303`
holds every spec whose `file` differs only in case from a document on disk
or from another spec's `file`. Both cases of `test_a_name_that_differs_only_in_case_is_held`
pass here and failed at a8bd7772, and the tree is unchanged after the held
run. The CI predicate carries no case check, and it does not need one. It
reads paths through git, which matches case exactly, so a mis-cased `file`
cannot be placed there and the removal stays refused. Executed.

confirms: round-1#6
The fix differs from round 1's proposal, and it holds on the grounds
given in its `answer:` line. Making the whole document one place would turn two
releases that add rules to different sections of one document into a
conflict. `rule_changes.overlapping` (`skills/settle/scripts/rule_changes.py:285-311`)
reads each place's ancestor headings from the document as it stood before
the replay. Two places overlap when they are in one file and one section
holds the other, or when either is the whole document. `replay` and
`conflicts` both ask it. The probe confirmed four cases:
- A held spec at `X` makes a later spec at its child `Y` wait.
- It also makes a later spec at its grandchild `Z` wait.
- A held spec at `Z` makes a later spec at the parent `X` wait.
- Sibling sections `W` and `Z` do not overlap, and neither do two files.

A section whose heading appears twice gets no ancestors. `apply_op` refuses
such a section at its own heading anyway, so nothing applies under it. The
new wait case and the `S child` conflict row failed at a8bd7772 and pass
here. Executed.

confirms: round-1#7
`NOTHING` is defined once, at `skills/verify/scripts/unverified_check.py:90`.
`rule_changes.py` and `fold_check.py` read it there, and neither keeps its
own copy. The probe's four near misses (`-`, `--`, `:` and a capital `N`)
are each refused with "writes `nothing — <why>`, with an em dash (U+2014)"
(`rule_changes.py:111`). `fold_check.py#names_targets` now reaches the
constant through `reader()`. `.github/scripts/rules.py` calls it, and
`tests/test_the_rules_command_reads_each_rule_off_its_test.py` passes (27
cases). Executed.

confirms: round-1#8
`skills/settle/scripts/settle.py:604-609` adds `; <n> with no
`## Rule changes`, left in place` to the last line. The skill's exit
sentence and the script's exit-code docstring (`settle.py:40-42`) both say
such a spec is counted and is not refused. The exit code is unchanged, as
the finding allowed. `test_an_apply_with_nothing_to_do_is_no_refusal` pins
the count. Executed.

confirms: round-1#9
`README.md:264` and `README.ko.md:254` no longer describe the freeze. Both
point to `skills/settle/scripts/fold_check.py` and `templates/config.md`
§*The fold's values*, so each cheat sheet holds one pointer and restates no
check. That follows the owner's Q1 direction rather than round 1's
paste-ready rows. The two editions say the same thing.
`test_both_cheat_sheets_point_to_the_checks_home` passes for both. Read and
executed.

confirms: round-1#10
`docs/release-checklist.md:115-118`, `templates/config.md:452-454` and
`docs/the-record-layout.md:25-28` each point to `skills/settle/SKILL.md`
§*A document past its ceiling is split, never trimmed*. None of them orders
a split in the same pull request. The checklist pin now refuses the old
sentence. Read and executed.

confirms: none
The first copy the orchestrator named does not restate a rule. The **One
read** paragraph of `skills/settle/scripts/fold_check.py` (lines 27-31)
describes the command's own output, and both cheat sheets now name that
file as the statement of what `fold-check` checks. The skill section names
what a document owes and defers to it ("as `fold-check` does"). The reason
the ceiling is a report (a guess from bytes, and one tool's per-call cap)
now stands only in this docstring, because `templates/config.md` dropped
its copy. So it is the one statement of that reason, not a second one. Its
`(the owner's answer of 2026-10-20)` names where the rule came from and
narrates no history. Read.

confirms: none
The second copy holds for its reader. `docs/release-checklist.md` §*2b*
says `--apply` writes `docs/`. The checklist is this repository's own
release procedure, and this repository's `seal/config.md` declares no
`Policy root` row, so its policy root is `docs`. The adopter-facing
statement, `skills/settle/SKILL.md:4-6`, names the row. Read.

confirms: none
The orchestrator's `fedc2790` rewrites `spec.md`'s `## Removes` row for the
freeze to "reported, never frozen or refused (Q6)". That answers round 1's
`## Not judged` row on `spec.md:204`. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Q2 is still `open`, and the settled predicate rests on its default (a) | `seal/specs/1792449518-settle-squashes-specs-into-docs-in-place/questions.md` Q2 | the owner, through the orchestrator |
| Q3 is still `open`: nothing gates a pull request that edits the policy root | `seal/specs/1792449518-settle-squashes-specs-into-docs-in-place/questions.md` Q3 | the owner, through the orchestrator |
| The Windows-shaped `file:` cases on a Windows host. Run 39348926688 at 0e93d61d is the first cross-platform run that carries them | `tests/test_settle_applies_rule_changes_in_place.py` | the orchestrator, from that run |
| Q4: whether bytes halved overestimates dense Hangul | `skills/settle/scripts/fold_check.py:316-318` | a measurement, as the frame says |
| The full suite, the repository-wide lint and the typecheck | the whole branch | the orchestrator, at `broad-gate` |

This round leaves nothing open. What comes due is the orchestrator's broad
run, then the sealer's spawn.

## Probes

| Command | Result |
|---|---|
| `python3 tests/test_tmp_round2_probe.py` | exit 0, deleted afterwards. The four near misses of `nothing — ` were each refused naming the em dash (U+2014). The four Windows-shaped `file:` values were each refused as not a top-level `docs/` file. A held spec at `X` kept later specs at `Y` and `Z` waiting. A held spec at `Z` kept a later one at `X` waiting. `overlapping` answered false for `W` beside `Z` and for two files, and true for `X` holding `Z` and for the whole document |
| `bin/test` over the four round-1 CI cases, `tests/test_settle_applies_rule_changes_in_place.py`, `tests/test_settle_reads_before_it_removes.py`, `tests/test_a_document_has_room_for_the_next_fold.py`, `tests/test_waiver_decided_at_start.py::test_the_framer_writes_rule_changes_from_the_index` and `tests/test_a_folded_statement_names_what_enforces_it.py`, `-q -p no:randomly` | exit 0: 355 passed in 4.74s |
| `bin/test tests/test_the_rules_command_reads_each_rule_off_its_test.py -q -p no:randomly` | exit 0: 27 passed |
| the four scripts checked out at a8bd7772 in the clone, then the new wait, case, conflict and refusal cases run with `bin/test`, then the scripts restored at fedc2790 | exit 1: 10 failed, 10 passed. The failures are every new row (four Windows values, two sentinel near misses, the nested wait, both case variants and the `S child` conflict). After the restore, `git status` was clean |

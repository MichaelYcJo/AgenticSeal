# 1792126889-every-agent-is-written-anew-from-its-job — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 93c1878c (the build; the phase closes after the evaluation, and `plan.md`'s Status cell stays empty until then) |
| Ran by | specseal:smith on Opus 5.5 (spawn 3a, build only) |

## What this phase was asked

Build only; a separate spawn runs the four agents' sets after this one.
Write `skills/agent-contract/SKILL.md` anew: one opening paragraph, then
`§1`…`§N`, each a short rule paragraph with its `Enforced by:` line, no
incident histories, the four rules of `spec.md` §*Rules the rewrite states in
place*, §2 saying no agent runs the broad gate and the orchestrator runs it
before the sealer, and the "each agent's numbers" sentence made true. Write
the old-to-new section map, rewrite the contract citations with one one-shot
script asserting its counts, and rewrite `docs/the-agent-set.md`'s
section-number sentence to *from this edition*. Give `agents/warden.md`'s
record step one sentence: read the record through
`skills/code-review/scripts/chain_check.py` before handing back and correct
what it refuses. Plant T3, T4 and T5, each seen red first, run every module
that reads the contract or a rewritten citation, fix or remove the failing
pins, run `bin/rules --check` and `ruff` on the changed Python, commit, and
write this record.

## What this phase found

**The contract.** 20,368 B, 369 lines, 17 sections before; 16,537 B, 281
lines, 20 sections after. Every section ends in an `Enforced by:` line (the
old file had none, so there was no target to keep). What left: the "How the
sections are numbered" heading (its rule is now one sentence of the opening
paragraph), every measured incident (#30's worktree, #36's prompts, the 28
minutes, the 128 shell edits, the milestone-49 stops, the "sat in two
definitions" histories), and §3's, §5's and §6's explanatory paragraphs.
§9's gate grammar stays whole: `tests/test_edits_go_through_the_edit_tool.py`
pins it, and it is rule rather than history.

**Rules keep their numbers where they stay, rather than a new order.** The
plan says "§1 to §N in the new order" and fixes no order. Every renumbered
citation is a site to rewrite and a site a reviewer has to check, so the
order that moves the fewest is the one chosen: old §16 (where `seal/`
resolves) joins old §11 (the record language), since it existed only because
§11 could not be followed without it, and old §17 moves up to §16. The four
new rules are §17–§20. A reader wanting a grouped order can still have one;
it costs every citation in the tree, which this phase judged not worth it.

| Old | New |
|---|---|
| §1–§10 | §1–§10 (§2 rewritten: no agent runs the broad gate) |
| §11 | §11 (now also holds old §16) |
| §12–§15 | §12–§15 |
| §16 | §11 |
| §17 | §16 |
| none | §17 clean up only what you started |
| none | §18 a check that refuses correct code is fixed or reported |
| none | §19 a change rewrites the text it amends in place |
| none | §20 do not avoid the change a problem calls for |

**Citations.** Outside the contract, 20 `§16`/`§17` sites before
(`git grep -P "§1[67](?!\d)"`, excluding `seal/specs`, `changelog` and the
contract, the same 20 the 957-phase-3-survey `sites.txt` lists). One script made
17 exact substitutions, each asserted to match once, then was deleted. After it,
10 sites: 6 are the new §16 (the commit rule), 1 is a historical
"the old §16, now part of §11" in a measurement docstring, and 3 were pins
rewritten by hand below. Three sites read "contract §11 and §16 each record
…", and the contract no longer records that history, so they now say
"§11 was written to end" (§19's rule applied to its own rewrite). T3 reads
145 citations in 264 files (121 outside the contract), and none names a
section the contract lacks.

**§2 now contradicts the sealer until phase 5.** `agents/sealer.md`
§*Rules* ("The broad gate is yours. The contract's §2 leaves each definition
to say …"), `docs/the-broad-gate.md` §*One act, one owner*, `CONTRIBUTING.md`
line 108 and `agents/smith.md`'s "the sealer takes the broad gate once" still
state the old owner. Plan row 5 rewrites each of them with the gate's new
order, so they are left for it; only the dangling `Enforced by:` target in
`docs/the-broad-gate.md` was re-pointed here.

**The batching figures.** §10 now points each kind of segment at
`docs/the-review-record.md` §*The per-segment bars* and says no definition
states a second copy. T5 was red on `agents/smith.md` (1.08–1.17) and
`agents/framer.md` (1.4, and the 0.15.1 framers' 2.3–3.1), so this phase
removed the smith's item 5 and the framer's figure paragraph and one
sentence, and pointed the framer at its row. The framer's other
measurements, which carry no "tools per turn", are phase 4's.

**The warden's sentence.** `chain_check.py` refuses any finding that reads
`open`, and the warden writes `verdict: open` by rule, so the sentence names
that one refusal as the one the warden leaves standing. The command it names
is `python3 skills/code-review/scripts/chain_check.py --baseline <base> --worktree`.

**New cases, each seen red (exit 1):**

- T3 `test_every_cited_section_exists`, red with a planted `contract §21` in
  `skills/implement/orchestration.md:32`, then restored. Its can-fail cases
  plant one number above the last heading in four trees and spellings, and
  one keeps another file's `§N` in a definition from counting.
- T4 `test_the_four_rules_stand_with_their_enforcers`, red with
  "never kill by command name" deleted from §17, then restored.
- T5 `test_no_definition_states_a_tools_per_turn_figure`, red on the tree as
  it stood (smith and framer), green after their figures went.
- `mutation-check`, one break per new unit, each `red`: the other-file guard
  in `cited_sections`, the citation extraction in `cited_sections`, and the
  second alternative of `TOOLS_PER_TURN`.

**Pins changed (Q7: re-pointed where the rule stays, removed where it was
narration):**

- `test_the_agent_contract_holds_the_universal_rules.py`: PINS 2 to "No agent
  runs any of the three"; 16 to the commit rule's pin; 17–20 added;
  `test_the_root_resolution_rule_says_why_it_is_universal` replaced by
  `…_states_both_places` (the "why" was history);
  `test_the_method_lessons_moved_in` removed (it pinned the four incident
  stories).
- `test_a_commit_names_its_repository.py`: `section(17)` to `section(16)`;
  the "is the last section" assert removed (it held while §17 was newest).
- `test_a_probe_that_commits_says_so.py`: the `#36` incident pin removed.
- `test_broad_gate_rule.py`: `test_the_prohibition_itself_has_one_home…`
  re-pointed to the new §2; `test_the_smith_carries_the_batching_rule…`
  replaced by `test_the_implementers_bar_is_not_the_reviewers_and_has_one_home`;
  `test_only_one_definition_assigns_the_broad_gate` removed (it pinned
  §2's "One definition … does hand them over", which is gone; T7 in phase 5
  replaces it); the refusal pins moved to the new §3 wording; the unused
  `DASH` constant removed.
- `test_the_handoff_before_round_one.py`: the smith's-number test now
  asserts §10's pointer; `test_the_framers_definition_carries_its_own_number`
  replaced by `…_points_at_its_bar`.
- `test_a_moved_rule_leaves_its_definition.py`: the smith's "1.08–1.17" and
  "§10's number for you" kept-application pins removed.

**Verified (executed):**

- The 69 modules `git grep -l -E "agent-contract|§[0-9]" -- tests` names, run
  together with `-n auto` after the last pin fix: 4525 passed, 15 skipped,
  1 failed (`test_docs_line_wrap.py` on one contract line this phase broke).
  After the rewrap, that module with the two contract modules: 111 passed,
  exit 0.
- The eight modules whose pins changed: 353 passed, 4 skipped, exit 0.
- `bin/rules --check`: exit 0, all 463 targets in 60 rule files resolve.
- `uvx ruff check` and `uvx ruff format --check` over the ten changed
  Python files: exit 0 both.

**Not run here:** the four agents' evaluation sets (`evals/<agent>-phase-3.md`)
are the next spawn's, and the full suite is the orchestrator's, after the
rounds settle.

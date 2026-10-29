# Review round 2: 1793240970-a-rename-runs-red-first-cases-as-new-behaviour

target: e3022ce4, fixes 37638558..e3022ce4

## Findings

None. The fix range holds three commits. `c545690b` is the fix pass.
`cb6e9d88` commits the round-1 record with its three answers. `e3022ce4`
folds the three fixes into `frame/design.md`. Each close round 1 left
`fixed c545690b` holds, and the two new units, the changelog lines and the
frame fold, hold no defect. The round stayed inside the fix range.

## Confirmations

confirms: round-1#1
Contract rule 2 now names the set the frame names. The fix pass claimed the
sentence reads "the test modules that read a path the phase changed,
whether they name it, import it or glob the directory that holds it".
`skills/agent-contract/SKILL.md:38-41` says that. It matches step 7 of
`frame/design.md:51-53`, which says "the test modules that read a path the
phase changed". The changelog says "read" at `changelog.md:4` and in its
process row at `changelog.md:10`. Rule 12's enumeration, executed: `git grep
-n -iE` over the tree for "name a path", "names a path the phase", "name a
changed path" and the phase-wide rename spellings. Outside the round
records and other work items' unrelated text, it found no copy of the old
word. The *Scope* row of `skills/verify/SKILL.md` and crafter step 7
(`agents/crafter.md:50-51`) cite rule 2 and hold no copy. The rule's
`check:` modules pass: `tests/text/test_broad_gate_rule.py` and
`tests/text/test_the_agent_contract_holds_the_universal_rules.py` ran in the
narrow command in `## Probes`. Carried from round 1, not re-established:
the frame's coordinates for the set, `frame/plan.md:15-16` and the
`## Removes` row.

confirms: round-1#2
Crafter step 5 and the sealer's `seen red` rule now apply to each unit.
The fix pass claimed step 5 reads "Where a unit is only renamed or moved,
write no case new for it". `agents/crafter.md:40-47` says that. So steps 5
and 6 (`agents/crafter.md:48-49`) both apply to a unit, as
`frame/design.md:57-62` asks. The fix pass also enumerated the class and
changed the sealer. `agents/sealer.md:135-138` now reads "A unit the phase
record says was only renamed or moved claims no `seen red`", and its HEAD
re-run covers "the existing cases the record names for it". Rule 12's
search, executed: `git grep -n -iE` for "phase that only", "phase only
renam", "only renames or moves" and "only renamed or moved" over `agents`,
`skills`, `templates`, `docs`, `README.md`, `CONTRIBUTING.md` and this work
item's frame and changelog. Every hit speaks of a unit. The verify row at
`skills/verify/SKILL.md:334`, `skills/implement/SKILL.md:231` and the
*Regression test* row at `skills/code-review/SKILL.md:75` were read. Each
speaks of a rename or a move, not of a phase.

confirms: round-1#3
The three old-name graders now refuse `shout` in any case and inside a
name. Each of `evals/behaviour/crafter/rule-crafter-rename/graders/shape-old-name-gone-code.md`,
`shape-old-name-gone-test.md` and `shape-old-name-gone-readme.md` holds
`pattern: 'shout'`, `flags: 'i'` and `match: 'not_contains'`. The
generator at `evals/scripts/rule_cases.py:505-513` writes them, and
regenerating in the round's clone changed no file. Round 1's executed
evidence line was re-run in Python and in `node`, with both patterns. On a
test body that calls `exclaim` but keeps `class ShoutTest` and
`def test_shout`, the old pattern did not match and the new one matched, so
the new grader fails that half-rename. The correct rename shape was also
run. That shape is `def exclaim` with the fixture's docstring, a test file
with `class ExclaimTest` and `def test_exclaim`, and the README line naming
`exclaim(text)`. Neither pattern matched it, so a correct run still passes
all three graders. The flag letter `i` is not new to the suite: the
measured sealer graders under `evals/behaviour/sealer/` already carry
`flags: 'mi'`.

confirms: none
The frame fold at `e3022ce4` matches the build. Read: `frame/design.md:44-48`
now says step 5 applies per unit. `frame/design.md:83-86` says the sealer's
rule applies per unit. `frame/design.md:150` names the regex `shout` with
flag `i`, as the generator writes it. One pronoun in the sealer bullet now
reads loosely. "The existing cases it names" refers to a unit, and a unit
names nothing. The binding sentence at `agents/sealer.md:136-137` says "the
cases the record names for it", so no agent acts on the looser wording.
It is no finding.

confirms: none
The changelog's new sentence at `changelog.md:3` matches the case. It says
the case "fails a run that leaves `shout` in any case or inside a name such
as `test_shout`". The graders read in the confirmation of round-1#3 do
that.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck at e3022ce4. The suite stays `unverified` in this round | the branch | the orchestrator, through `seal gate` |
| No case exercises a phase that renames one unit and adds behaviour in another. No case exercises rule 2's import or glob reach either. Executed: `git grep -n -iE` over `tests` and `evals` for the fixed sentences found only a comment at `tests/text/test_the_handoff_before_round_one.py:128` about step 6. The closes of round-1#1 and round-1#2 rest on reading the text, as the closed findings asked. The phase-wide wording had no case before the fix either | `agents/crafter.md:40-47`, `agents/sealer.md:135-138`, `skills/agent-contract/SKILL.md:38-41` | the orchestrator, if a mixed-phase crafter case is wanted |
| Whether the paid `rule-crafter-rename` runs still pass with the tightened graders. No run was made after the fix. The fix pass's account says the six measured traces hold `ExclaimTest` and `test_exclaim`. This round did not reopen the traces and carries that from round 1 | `evals/behaviour/crafter/rule-crafter-rename/graders/` | the orchestrator, at the next crafter comparison |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the worktree into `<scratchpad>/1793240970-a-rename-runs-red-first-cases-as-new-behaviour/round-2/clone`, checked out at e3022ce4 | exit 0 |
| `python3 evals/scripts/rule_cases.py` in that clone, then `git status --short` | exit 0; no file changed |
| `node -e` testing `/\bshout\b/` and `new RegExp("shout","i")` over four bodies: a test file keeping `ShoutTest` and `test_shout`, a test file with `ExclaimTest` and `test_exclaim`, the renamed `src/textutil.py`, and the renamed README line | exit 0; the kept-name test file gave old false, new true; the other three gave false for both |
| `python3 -c` running `re.search` with `\bshout\b`, and with `shout` and `re.I`, over the kept-name test file | exit 0; old False, new True |
| `bin/test` in the worktree over sixteen modules that read a changed path, `-q`: `test_rule_cases`, `test_noninferiority`, `test_evals_layout`, `test_the_agent_contract_holds_the_universal_rules`, `test_broad_gate_rule`, `test_the_suite_has_a_command_that_is_cheap_twice`, `test_the_sealer_guarantees`, `test_the_seal_is_taken_once_by_the_sealer`, `test_no_passage_is_pasted_into_a_second_file`, `test_a_moved_rule_leaves_its_definition`, `test_docs_line_wrap`, `test_the_rules_have_one_owner`, `test_every_agent_reads_the_contract`, `test_one_word_one_meaning`, `test_no_case_tells_the_agent_it_is_evaluated`, `test_the_set_a_work_item_always_has` | exit 0; 761 passed |
| `bin/seal rules --check` in the worktree | exit 0; all 267 check lines in 55 rule files hold |

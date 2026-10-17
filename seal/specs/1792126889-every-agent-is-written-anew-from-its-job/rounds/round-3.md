# 1792126889-every-agent-is-written-anew-from-its-job — review round 3

target: 7e8e194e, fixes 74c6a75a..7e8e194e

## Findings

This verifying round raises no finding. Each of round 2's two closes holds,
and the fix range's new sentence and new assertion hold as code.

## Confirmations

confirms: round-2#1
Contract §2 now ends "Where the run is yours, the same hand-over carries its
result instead of the label." (`skills/agent-contract/SKILL.md:46-47`, read).
The sentence sits after the one that tells every agent to label the suite
`unverified`, so the sealer, the one agent §2 gives the run, is no longer told
to hand its result over as `unverified`. This agrees with the sealer's step 6
(`agents/sealer.md:75-77`), which returns the gate's `SEALED` or `NOT
SEALED` lines as they came, and with
`docs/the-broad-gate.md:38-41` (read). The pin is
`test_the_prohibition_itself_has_one_home_and_it_is_the_contract`
(`tests/test_broad_gate_rule.py:205-211`), scoped to §2's body through
`contract_section(2)`, so a copy of the sentence anywhere else in the
contract cannot satisfy it (read). §2's `Enforced by:` line names that case
beside its earlier target, and `bin/rules --check` resolves it (executed).
Executed: with the sentence deleted from the clone's contract,
`bin/test` over `tests/test_broad_gate_rule.py` and
`tests/test_the_agent_contract_holds_the_universal_rules.py` exits 1 with that
one case failing and 79 passing; restored, the two modules pass. That is the
pin seen red, which the answer's claim about 74c6a75a also asserts.

The answer says no other sentence tells every agent to label the suite
`unverified`. Enumerated again here by `git grep -i` for a suite and
`unverified` within forty characters over `skills`, `agents`, `docs`,
`CONTRIBUTING.md`, `bin` and `hooks` (executed). The hits are contract §2
itself, `docs/the-broad-gate.md:39`, which already carries the exception,
`skills/verify/SKILL.md:284`, the row for the hand-off to review, which is not
the sealer's act, and a constant in `skills/verify/scripts/broad_gate.py:179`.
`agents/smith.md:232-233` and `agents/warden.md:140-141` speak of the smith's
hand-over, as the answer says (read). No site in the class still binds the
sealer to the label.

confirms: round-2#2
The fragment's first bullet now reads "a warden spawn preloaded 27,032 bytes
at its evaluation (`93c1878c`) where it preloaded 76,019 at `af9c924b`"
(`seal/specs/1792126889-every-agent-is-written-anew-from-its-job/changelog.md:6-7`,
read). Past tense with a commit on each figure, so the sentence no longer
states a fact about the plugin that a later edit moves. Executed: the sha256
of `agents/warden.md` and of the contract at 93c1878c equal the two `preload`
hashes the new side carries in `evals/warden-phase-3.json`, and the two
files sum to 27,032 there, the record's `preload_bytes`. At af9c924b the
warden's four preloaded files, the definition, the contract, `code-review`
and `writing-style`, sum to 18,031 + 20,368 + 16,620 + 21,000 = 76,019, the
record's "Baseline preload bytes". So both commits the bullet names are the
trees the evaluation read.

The prompt asked this round to recount HEAD's figure. Executed:
`noninferiority.preload_bytes` over the clone at 7e8e194e lists
`agents/warden.md` and `skills/agent-contract/SKILL.md` and returns 27,198,
and `wc -c` on each file at 8d7e6a44 and at 7e8e194e gives 10,527 plus
16,671, the same sum. The contract grew from 16,491 to 16,671, which is the
180 bytes the answer gives for round-2#1's sentence. Rule 4 still holds by
arithmetic, 27,198 < 76,019.

confirms: none
The fragment's second bullet says the contract "is about a fifth smaller".
The new sentence moved that figure, so it is re-read at this HEAD: 16,671
against 20,368 at af9c924b is 18.2% smaller (executed, `wc -c`), which still
reads as about a fifth. The table under the first bullet names its own
commits, and no tracked file outside the work item's directory states the
preload figure (`git grep -F '27,032'` and `git grep -F '27032'`, executed).

confirms: none
The narrow modules for the changed sentences pass at 7e8e194e. `git grep -n
-F` over `tests` and `evals` for each changed sentence finds only
`tests/test_broad_gate_rule.py` (executed). `bin/test` over that module,
`tests/test_the_agent_contract_holds_the_universal_rules.py`,
`tests/test_the_changelog_is_gathered_at_release.py`,
`tests/test_every_reader_ends_a_line_where_gfm_does.py`,
`tests/test_no_real_identifiers.py`,
`tests/test_a_rewritten_definition_proved_non_inferior.py` and
`tests/test_every_agent_reads_the_contract.py` exits 0 with 253 passed and 4
skipped. `bin/rules --check` exits 0, with 464 targets in 60 rule files,
which is round 2's 463 plus the new `Enforced by:` target.

## Not judged

| What | Location | Who answers |
|---|---|---|
| CI run 39044553922 at 7e8e194e, and the full suite, lint and typecheck; not waited on, and not run, per contract §2 | the branch | the orchestrator, then the sealer's broad gate after the rounds settle |
| Whether the warden's outcome and rule 5 still hold at a preload of 27,198 bytes, 166 more than the one measured; rule 4 holds by arithmetic, and no paid evaluation ran | `seal/specs/1792126889-every-agent-is-written-anew-from-its-job/evals/warden-phase-3.md` | the orchestrator, at the milestone's close against af9c924b |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the seven modules in the last confirmation; `bin/rules --check` | exit 0, 253 passed, 4 skipped; exit 0, 464 targets in 60 rule files |
| §2's new sentence deleted from the clone's contract with `Edit`, then `bin/test` over `tests/test_broad_gate_rule.py` and `tests/test_the_agent_contract_holds_the_universal_rules.py`; restored with `git checkout` | exit 1: 1 failed (`test_the_prohibition_itself_has_one_home_and_it_is_the_contract`), 79 passed; clean tree after the restore |
| `noninferiority.preload_bytes` over the clone at 7e8e194e; `git show <rev>:<file> \| wc -c` for the warden's preload at 93c1878c, 155920f5, 74c6a75a, 8d7e6a44 and 7e8e194e | 27,198; 27,032, 27,018, 27,018, 27,198, 27,198 |
| sha256 of the warden's preloaded files at af9c924b, 93c1878c and 7e8e194e, against `evals/warden-phase-3.json` | the 93c1878c hashes equal the record's `preload`; the af9c924b files sum to 76,019 |
| `git grep -i` for a suite and `unverified` within forty characters over `skills agents docs CONTRIBUTING.md bin hooks` | four hits, none binding the sealer to the label |

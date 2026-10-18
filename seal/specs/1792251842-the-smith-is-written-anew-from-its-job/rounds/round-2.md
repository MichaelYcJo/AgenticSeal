# 1792251842-the-smith-is-written-anew-from-its-job — review round 2

target: 2c7716bd, fixes 3d97e196..2c7716bd

## Findings

### 1. Phase 4 and the memo still call #969's difference "a few contract sentences" and "#969's §2 change", one sentence after naming three more files

severity: should
location: `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-4.md:38-42`, `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md:32`
verdict: fixed eb75405c
reopens: round-1#6

Read. Round 1's finding 6 was that the records describe what #969 changed in
the warden's read set as contract §2 and one warden sentence, while the
warden also read `docs/the-review-record.md` and more. 44387d56 corrected
the sentences round 1 quoted, but the same description stands in the same
two units a few lines on. `phases/phase-4.md:39-42` says re-taking the
baselines "would cost about $60 more for a difference of a few contract
sentences, so the comparison below includes #969's §2 change as well as
this item's, and says so". The Grounds cell of `overview.md:32` names the
three added files and then ends "Re-taking the baselines would have cost
about $60 for a few contract sentences, so the comparison includes #969's
§2 change as well as this item's". So each unit now says two different
things about the same difference, and the second one is the description
finding 6 found false. The changelog's matching sentence was corrected
("#969's changes"), so only these two are left.

Executed. The recount behind the corrected sentences holds (see
`## Confirmations`), so the fix is only to make the tail agree with it.

```diff
--- a/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-4.md
+++ b/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-4.md
@@
 `evals/<agent>-phase-4.json` and `.md`. The baselines stay those of phase 1
 at 2fc33333 (the orchestrator's decision, 2026-10-18): re-taking them on the
-merged tree would cost about $60 more for a difference of a few contract
-sentences, so the comparison below includes #969's §2 change as well as
-this item's, and says so.
+merged tree would cost about $60 more, so the comparison below includes
+#969's changes named above as well as this item's, and says so.
--- a/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md
+++ b/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md
@@
-| Phase 4 taken twice, the second on the merged tree (phase 4) | `plan.md` row 4 runs the three agents once at phase 3's commit, against phase 1's baselines | the first take at 7053c184 (records 668fd5f4, a3bf3832) is history; the record is the second take at af716289, this branch with `release/v0.22.1` merged in at 16e8d4c8 plus two test fixes no agent reads; the baselines stay phase 1's at 2fc33333 by the orchestrator's decision (2026-10-18) | #969 merged into `release/v0.22.1` (4a6e24f6) before the framer's re-run was taken, changing contract §2, which all three agents preload, one sentence of `agents/warden.md`, and `docs/the-review-record.md`, `skills/code-review/scripts/chain_check.py` and `agents/sealer.md`, which the warden reads in the evaluated tree; an agent whose read set changed is measured again. Re-taking the baselines would have cost about $60 for a few contract sentences, so the comparison includes #969's §2 change as well as this item's (`phases/phase-4.md`) |
+| Phase 4 taken twice, the second on the merged tree (phase 4) | `plan.md` row 4 runs the three agents once at phase 3's commit, against phase 1's baselines | the first take at 7053c184 (records 668fd5f4, a3bf3832) is history; the record is the second take at af716289, this branch with `release/v0.22.1` merged in at 16e8d4c8 plus two test fixes no agent reads; the baselines stay phase 1's at 2fc33333 by the orchestrator's decision (2026-10-18) | #969 merged into `release/v0.22.1` (4a6e24f6) before the framer's re-run was taken, changing contract §2, which all three agents preload, one sentence of `agents/warden.md`, and `docs/the-review-record.md`, `skills/code-review/scripts/chain_check.py` and `agents/sealer.md`, which the warden reads in the evaluated tree; an agent whose read set changed is measured again. Re-taking the baselines would have cost about $60, so the comparison includes #969's changes named here as well as this item's (`phases/phase-4.md`) |
```

answer: eb75405c takes the paste-ready text in both units: `phases/phase-4.md` now says the comparison includes "#969's changes named above", and `overview.md`'s Grounds cell for the phase-4 row ends "#969's changes named here", each pointing at the list of contract §2, the warden's sentence, `docs/the-review-record.md`, `skills/code-review/scripts/chain_check.py` and `agents/sealer.md` a few lines earlier. `git grep -F` for "few contract" and "§2 change" finds them outside the round records only in #969's own `questions.md`, about a different fact.

### 2. The smith's re-take after round 1 is missing from the changelog's commit coordinate and from the memo

severity: should
location: `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/changelog.md:45-46`, `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md:36`
verdict: fixed eb75405c
regression: round-1

The unit is the record of the smith's third side, at 28d6a453. `plan.md`
row 4 runs an agent's set a second time only for a `fail` caused by its own
sentence and says "no third run", and `questions.md` Q1 stops this item
before the next agent once its spend passes $150; 2c7716bd took the smith's
side again after round 1's fixes and wrote it into `phases/phase-4.md`,
`phases/phase-5.md` and the changelog's table, but not into the changelog's
commit coordinate or into `overview.md`; the defect comes from the fix
range's own record commit, which no finding of round 1 asked for.

Read. `changelog.md:45-46` ends the table's paragraph "the verdict is
`evals/<agent>-phase-4.md`, both committed at `6f3ee98b`". Executed:
`git log` over the work item's `evals/` shows `smith-phase-4.json` and
`smith-phase-4.md` last committed at 2c7716bd, and the smith row above that
sentence now reads that side (26,879, 35,691.6, 5.4509). So a plugin user
who follows the coordinate to 6f3ee98b finds 26,596 and 35,993.1, not the
row's figures.

Read. `overview.md` has a divergence row for phase 4 taken twice and one
for Q1's stop passed by the second take, whose Grounds say "the item's
total is 227.8873". It has none for the smith's third take. That take ran
outside `plan.md` row 4's two takes, and it spent 5.4509 USD with the item
already past Q1's $150 (227.8873 + 5.4509 = 233.3382). The reason is in
`phases/phase-4.md:95-98` (round 1 changed the definition after the side
was measured, and an agent whose read set changed is measured again), and
the memo is where a divergence goes. The tree records no answer to Q1's
stop for this take; the owner's answer on 2026-10-18 was asked about the
second take's $60. Whether it covers this take is a row of `## Not judged`.

```diff
--- a/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/changelog.md
+++ b/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/changelog.md
@@
   and `adbbea77`) and `evals/<agent>-phase-4.json`; the verdict is
-  `evals/<agent>-phase-4.md`, both committed at `6f3ee98b`.
+  `evals/<agent>-phase-4.md`, both committed at `6f3ee98b` for the warden
+  and the framer and at `2c7716bd` for the smith.
```

The row below goes into `overview.md`'s divergence table after the row
"Q1's spend stop passed (phase 4's second take)":

```markdown
| The smith's side taken a third time, after round 1 (phase 4) | `plan.md` row 4 runs an agent's set a second time only for a `fail` its own sentence caused, and no third run; `questions.md` Q1 stops this item before the next agent once its spend passes $150 | the side at 28d6a453 (committed at 2c7716bd) is the smith's record in `evals/smith-phase-4.json` and `.md`; the af716289 side is history | round 1's fixes changed `agents/smith.md` at a72d5b53 after that side was measured, and an agent whose read set changed is measured again (`phases/phase-4.md`); the take spent 5.4509 with the item at 227.8873, so the item's total is 233.3382 |
```

answer: eb75405c names `6f3ee98b` for the warden's and the framer's records and `2c7716bd` for the smith's in `changelog.md` (each read with `git log -1` on the six files), and adds the divergence row to `overview.md`: the third take was the orchestrator's, so that the record measures the text that ships, and the owner's "decide and go with your recommendation" of 2026-10-18 was given to the orchestrator's recommendation to re-measure on the merged tree, a delegation the orchestrator applied to this take as well. Recounting the total from the phase records showed the second take's sides, 5.3675 + 41.7424 + 16.1196, sum to 63.2295 and not the 63.2293 written (63.2296 from the three JSONs' `costUsd`), so the same commit corrects 63.2293, 123.7421, 129.1930 and 227.8873 in `phases/phase-4.md`, `phases/phase-5.md` and `overview.md` to 63.2295, 123.7423, 129.1932 and 227.8875; the item's evaluation total is 104.1452 + 129.1932 = 233.3384, not 233.3382.

### 3. No case holds the two sentences round 1's fixes put into the smith's hand-back, so a trim can take back the changelog's promise with every case green

severity: should
location: `agents/smith.md:55-57`, `agents/smith.md:73-74`, `tests/test_a_moved_rule_leaves_its_definition.py`
verdict: fixed eb75405c
regression: round-1#3

The units are step 10's new clause (a question only a person can answer,
a leftover for `seal/follow-up.md`, with who answers each) and the `## Never`
line that refuses a block at the end of the hand-back. `spec.md` §*The
shape this item gives each file* lists "put an emoji or a proof block in
anything it writes" under `## Never` and asks an `Enforced by:` only of
`## Rules`, and plan row 2 plants cases for the four rules decision 1
names; a72d5b53 wrote both sentences as round 1's paste-ready text gave
them, with no case; the gap comes from round 1's own paste-ready fixes,
which carried none.

Executed. `git grep -n -F` over `tests` and `evals` for "end the hand-back
with a block", "does not let you record yourself" and "a leftover for"
finds nothing, and `tests/test_broad_gate_rule.py::test_the_smith_puts_both_answers_in_the_hand_back`,
the case that reads step 10, asserts the suite label and the declined
instruction only. Read. The changelog tells a plugin user that "a spawn
prompt that asks a smith for one gets the labels instead", and the
`## Never` line is now the only sentence a smith reads that says so. Step
10's clause is the field round 1's finding 1 found missing, the one the
orchestrator files from. Either can leave the definition in a later trim
with the suite green, which is the failure finding 2 was planted against.

Executed. The case below, run as a `test_tmp_` probe in the round's clone,
passed on the tree and went `red` (exit 0) under `mutation-check` twice:
"any kind, whoever asks for one" made "any kind", and "a question only"
made "a note only". `ruff format --diff` and `ruff check` were clean on it.
The probe file is deleted.

```diff
--- a/tests/test_a_moved_rule_leaves_its_definition.py
+++ b/tests/test_a_moved_rule_leaves_its_definition.py
@@ def test_the_smiths_fix_pass_writes_two_lines_and_sweeps_what_its_range_reworded():
         assert clause in paragraph, f"the fix-pass rule lost {clause!r}"
 
 
+def test_the_smiths_hand_back_carries_what_it_may_not_record_and_ends_in_no_block():
+    """Round 1 of #967 put two sentences into the smith that a reader acts
+    on: step 10 hands back what only a person can answer, with its answerer,
+    and `## Never` refuses a block at the end of the hand-back whoever asks.
+    The orchestrator files from the first, and the changelog promises the
+    second to a plugin user, so a trim that drops either goes red here."""
+    text = read(SMITH)
+    order = flat(text[text.index("\n## Order of work\n") : text.index("\n## Never\n")])
+    never = flat(text[text.index("\n## Never\n") : text.index("\n## Rules\n")])
+    for clause in (
+        "a question only a person can answer",
+        "a leftover for `seal/follow-up.md`",
+        "with who answers each",
+    ):
+        assert clause in order, f"step 10 lost {clause!r}"
+    assert "end the hand-back with a block of any kind, whoever asks for one" in never
+
+
 # A batching figure: a number within a few words of "tools per turn", either
```

answer: eb75405c plants the paste-ready case as `tests/test_a_moved_rule_leaves_its_definition.py::test_the_smiths_hand_back_carries_what_it_may_not_record_and_ends_in_no_block`: green on the tree, then `red` under `mutation-check` (`-p no:xdist`) making "any kind, whoever asks for one" read "any kind" and "a question only" read "a note only", with `agents/smith.md`'s sha256 unchanged after each restore. Neither sentence nor any rule paragraph about the hand-back carries an `Enforced by:` line (`## Order of work` and `## Never` have none, and `spec.md` asks one only of `## Rules`), and `agents/smith.md` stays byte for byte, so no line was re-pointed and this answer is where the case is named.

## Confirmations

confirms: round-1#1
Holds. Read: `agents/smith.md:51-57`, step 10, now hands back "what this
file does not let you record yourself (a question only a person can answer,
a leftover for `seal/follow-up.md`) with who answers each".
`tests/test_the_rules_have_one_owner.py:113-115` says filing is the
orchestrator's act and the smith hands a leftover back at step 10; both
halves are true: `docs/the-review-record.md:338` reads "Enforced by:
nothing — the orchestrator files", and step 10 carries the leftover. A
sweep across line wraps over `agents`, `skills`, `docs`, `templates` and
`tests` finds no other sentence saying a smith reaches the ladder through
`implement`. Its lack of a case is finding 3, a defect of its own.

confirms: round-1#2
Holds. Executed: the new case reads `agents/smith.md` through
`smith_rule`, which opens `SMITH`, and `agents/smith.md:167` names it.
`bin/rules --check` resolves all 483 targets. `mutation-check` making
"append the one it did" read "append none it did" gave `red` (exit 0), the
case failing on the clause "append the one it did change after `, `", and
the file's sha256 was unchanged after the restore.

confirms: round-1#3
Holds. Read: `agents/smith.md:73-74` refuses a block at the end of the
hand-back, "whoever asks for one", which is the sentence the changelog's
promise needed. Executed: `wc -c agents/smith.md` reads 10,276, under
10,527, and T6's module is green over it. What holds that sentence is
finding 3.

confirms: round-1#4
Holds. Read: `skills/implement/orchestration.md:19-21` and
`tests/test_chain_hooks_hardening.py:303` say a smith spawn opens
`implement`. Executed: a sweep for "smith spawn preloads" and "smith
preloads" across line wraps finds only `tests/test_review_axes.py:112` and
`tests/test_waiver_decided_at_start.py`, both about `orchestration.md`,
which no smith spawn preloads, and both true.

confirms: round-1#5
Holds. Read: `skills/verify/SKILL.md:218-220` reads "any edit after the run
voids the claim". Executed: the same sweep for "your seal" and "breaks
your" finds nothing; "the smith's seal" survives once, in the skill's
past-tense account of an incident, which round 1 set aside as history.

confirms: round-1#7
Holds. Read: `phases/phase-4.md:81-88` and `overview.md:51-57` no longer
clear the item on the framer's opens. They say the framer preloads both
rewritten skills, that no sentence of this item's files is identified as
the cause, and that the fail is carried to #968. The figures they lean on
(total tokens down 0.5%, 120 to 109 calls) are `phases/phase-4.md`'s table
and were recounted in round 1.

confirms: round-1#8
Holds. Read: `overview.md:36` now says the owner answered "decide and go
with your recommendation" and that the `## Not verified` row is closed with
that answer, which the closed row at `overview.md:47` says too. The row's
total stops at the second take; that is finding 2.

confirms: none
The fix pass's recount of the warden's reads, which departed from the
orchestrator's text for finding 6, holds against the kept traces. Executed,
read only, over `SpecSeal-worktrees/967-phase-4-raw/warden/traces` and
`967-phase-4b-raw/warden/traces`, for every path
`git diff --name-only 7053c184 af716289` lists, counting a run when a tool
call names the path under the evaluated tree's root (a `VAR=<root>`
assignment resolved): `docs/the-review-record.md` in 17 and 18 runs,
`skills/code-review/scripts/chain_check.py` in 18 and 17, `agents/sealer.md`
in 2 and 1, `agents/warden.md` in 1 and 0, and no other listed path in
either take. `skills/code-review/orchestration.md` is named under the tree
in no run; its 6 runs a take name it relative to a session whose `cwd` is
the fixture's `home/cwd`, or in `git diff <fixture commit>..HEAD`. So
"every time as the reviewed fixture's own copy" is what the traces show,
and round 1's "named in 6" counted those.

confirms: none
The smith's re-taken side is what the records say. Executed:
`noninferiority.py run --agent smith --from-raw SpecSeal-worktrees/967-phase-4c-raw/smith`
into scratch, then `cmp` against the committed `evals/smith-phase-4.json`,
exit 0; `compare --phase 4` against `baseline-smith.json` re-rendered
`smith-phase-4.md` byte for byte (`cmp` exit 0); `check` on it, exit 0. Its
`rev` is 28d6a453, `suite_rev` af9c924b, 8 runs not cut short, and its
preload hashes equal `shasum -a 256` of `agents/smith.md` (ada69687…) and
the contract (642b0da6…) at 2c7716bd, 10,276 + 16,603 = 26,879 bytes. The
figures in `phases/phase-4.md:100-107` and the changelog's smith row
recount: 7,566,611 / 212 = 35,691.6 per call (-17.1%), 26,879 / 90,728
(-70.4%), 5.4509 / 6.6210 (-17.7%), 24 graders of 2 runs each passing (48
of 48), and 123.7421 + 5.4509 = 129.1930.

confirms: none
The smith opened both skills in all eight runs of the re-take, as
`phases/phase-4.md:109-111` and the changelog say. Executed over
`SpecSeal-worktrees/967-phase-4c-raw/smith/traces`, read only: all 8 runs
call `Read` on the evaluated tree's `skills/implement/SKILL.md`, and all 8
read the content of `## English prose rules` before their first write to a
phase record (five by `Read` at offset 278, two by an `awk` range, one by
`sed -n 278,320p`), not only a heading list.

confirms: none
The narrow modules over the fix range are green. Executed in the clone at
2c7716bd: `bin/rules --check` exit 0; `bin/test` over the three changed test
modules and fourteen that read the changed files, exit 0 (474 passed and 2
skipped, then 108 passed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the owner's answer to Q1's stop, given for the second take's $60, covers the smith's re-take after round 1 (5.4509 USD, the item then at 227.8873 against a $150 stop) | `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/questions.md:46`, `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-4.md:95-112` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck on this branch | the branch at 2c7716bd | the orchestrator's broad gate |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the checkout into the round's scratch directory, checked out at 2c7716bd | exit 0 |
| `noninferiority.py run --agent smith --from-raw SpecSeal-worktrees/967-phase-4c-raw/smith --out <scratch>`, then `cmp` against `evals/smith-phase-4.json` | exit 0; `cmp` exit 0 |
| `noninferiority.py compare --agent smith --phase 4 --old evals/baseline-smith.json --new <scratch json> --out <scratch md>`, then `cmp` against `evals/smith-phase-4.md`; `noninferiority.py check evals/smith-phase-4.md` | exit 0, `cmp` exit 0; exit 0 |
| `shasum -a 256` and `wc -c` on `agents/smith.md` and `skills/agent-contract/SKILL.md` | the hashes of the side's preload; 10,276 + 16,603 = 26,879 |
| a trace reader over both warden takes' traces for every path `git diff --name-only 7053c184 af716289` lists, at the tree's root and elsewhere | exit 0: the counts under `## Confirmations` |
| a reader of every warden call naming `skills/code-review/orchestration.md`, with the session's `cwd` | exit 0: none under the tree, every one in the fixture |
| a reader of every call naming `writing-style` in the smith re-take's traces, against the first phase-record write | exit 0: the section read in 8 of 8 before the record |
| `bin/rules --check --root <clone>` | exit 0: all 483 targets in 60 rule files resolve |
| `bin/test` over `test_a_moved_rule_leaves_its_definition`, `test_the_rules_have_one_owner`, `test_chain_hooks_hardening`, `test_broad_gate_rule`, `test_every_agent_reads_the_contract`, `test_the_record_is_written_in_words`, `test_one_word_one_meaning`, `test_docs_line_wrap`, `test_no_real_identifiers`, `test_a_rewritten_definition_proved_non_inferior`, `-q` | exit 0: 474 passed, 2 skipped |
| `bin/test` over `test_review_axes`, `test_waiver_decided_at_start`, `test_a_reference_root_is_read_and_never_taken`, `test_edits_go_through_the_edit_tool`, `test_a_phase_hands_the_next_one_a_record`, `test_no_passage_is_pasted_into_a_second_file`, `test_the_payload_meter_says_what_it_measured`, `-q` | exit 0: 108 passed |
| `mutation-check agents/smith.md --replace "append the one it did" "append none it did" --tests "bin/test tests/test_a_moved_rule_leaves_its_definition.py -p no:xdist -q -k test_the_smiths_fix_pass_writes_two_lines_and_sweeps_what_its_range_reworded"` | exit 0: `red`; the file's hash unchanged after |
| finding 3's case as a `test_tmp_` probe: run on the tree, then `mutation-check` making "any kind, whoever asks for one" read "any kind" and "a question only" read "a note only"; `ruff format --diff` and `ruff check` on it | 1 passed; `red` (exit 0) under each; clean, clean; the probe file deleted |
| a sweep across line wraps over `agents`, `skills`, `docs`, `templates` and `tests` for "smith spawn preloads", "your seal", "breaks your" and "reaches it through `implement`" | exit 0: the two `orchestration.md` sentences and one past-tense line, each true |

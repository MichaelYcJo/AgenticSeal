# 1792363189-rule-3-decides-on-the-agent-not-one-run — review round 2

target: 4205fd6e, fixes 978c8f23..4205fd6e

## Findings

## Confirmations

confirms: round-1#1
The close holds (read, `git diff 978c8f23..4205fd6e`). Commit 7d2bc3d1
rewrites the rule 3 clause of
`seal/specs/1792126889-every-agent-is-written-anew-from-its-job/spec.md:224-229`
in place. That file is the one finding 1's `location:` names, and the
commit touches no other file. The sentence no longer states a per-grader
comparison as `verdict`'s rule. It points to rule 3 of `evals/README.md`
§*The behaviour suite*, which is the rule's one home. It also says #957's
phases judged each grader on its own, so the paragraph's later sentence,
"This rule holds unchanged for every later phase", is still true of #957's
own phases. The rewrite left a short line, "read across every", where the
pasted text met the old line, and the sentence runs on unbroken across it.
No file under `tests`, `.github`, `hooks`, `skills` or `bin` names
#957's directory (read, `git grep -l 1792126889`), so no pin reads the
rewritten text.

confirms: none
Round 1's list of the old rule's statements was incomplete, and the fix
pass's sweep corrects it. Round 1 said it enumerated every place the
rule's words survive. Its search output was cut at 80 lines, and the cut
fell before the directories of #967 (`1792251842-…`) and #969
(`1792252400-…`). Both directories sit on the branch at 4279671d, and both
items shipped in v0.22.1 (`git tag --contains` on their merge commits
f6ae6db6 and 4a6e24f6 prints `v0.22.1`). This round ran the search again
over the whole tree at 4205fd6e, uncut. It found every statement the fix
pass names. Beyond those, it found only process records and the `model`
rule (executed, `git grep` on "at least as often", "less often than the
baseline", "as often as on the baseline", "per-grader", "per grader",
"each shape and reach", "each shape grader" and "every shape and reach
grader", with this work item's directory and `.test_durations` left out).

confirms: none
Each statement the fix pass names as standing does stand, read at
4205fd6e. Finding 1 depended on one distinction. Its sentence defined
`verdict`'s rules and said that definition held for every later phase. None
of the statements below defines `verdict`'s rules.

- `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/spec.md:215`,
  #967's S3. The cell names the check #967's acceptance passed and the record
  that holds it (`evals/smith-phase-4.md` rule 3). It does not define rule 3.
  The rule S3 protects is that the smith opens `implement` when it acts.
- `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/spec.md:203`,
  #969's S4. This is an acceptance cell too. It asks "each truth and shape
  grader" to pass at least as often, which is not the form of rule 1 or rule
  3 at any commit. So it states S4's own bar and not `verdict`'s rules. Its
  check is `evals/sealer-phase-4.md` reading `pass`.
- The same file at `:206`, #969's S7. It states the `model` subcommand's
  rule. `noninferiority.py#cheaper_model` still applies that rule unchanged,
  because `questions.md` Q1 leaves it alone. So the sentence is true.
- `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/evals/sealer-model.md:73`.
  It is a reason line in a record of a run. It stays for the same reason
  this work item's `spec.md` §*Scope*, Out, gives for #957's records.
- `seal/specs/1792126889-every-agent-is-written-anew-from-its-job/overview.md:43`
  ("#966 holds the per-grader rule's sample size") and
  `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/spec.md:79`
  ("The per-grader rule's sample size — #966"). Both point to #966, which
  is where the question went and where it was answered. Neither states the
  rule.

The other hits are process records: #957 `phases/phase-1b.md:14-15`,
`:45` and `:160`, #957 `phases/phase-2.md:409`, and #969
`phases/phase-5.md:154`. `settle --retire-process` removes them. The one
remaining hit, #969 `questions.md:41` Q2, asks about the `model` rule. One
risk remains, and it belongs to judgment, not to this branch. The session
that folds #967 has to read S3's cell as evidence of a passed check and not
as a definition of rule 3. `skills/settle/SKILL.md` makes that judgment its
own: it folds "only what is still true".

confirms: none
Finding 1's `answer:` names three of the six statements this round was
asked about: #967 `spec.md:215`, #969 `spec.md:203` and #969
`evals/sealer-model.md:73`. It does not name #969 `spec.md:206`, #957
`overview.md:43` or #969 `spec.md:79`, which came from the fix pass's
hand-back. The three left out are judged in the entry above, so nothing
goes unread. The `answer:` line is accurate for the three it names.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck: unverified | the branch at 4205fd6e | the orchestrator, by `broad-gate --base release/v0.22.2` now that this round leaves nothing open; the sealer's spawn follows that run |

## Probes

| Command | Result |
|---|---|
| `git diff --stat 978c8f23..4205fd6e` | two files: #957's `spec.md` (+5, -3) and this work item's `rounds/round-1.md` (+2, -2) |
| `git grep -n -i` over the whole tree for the eight phrases named above, with this work item's directory and `.test_durations` left out | 21 lines; every one is named in an entry above or is a #957 `evals/*.md` reason line round 1 placed out of scope |
| `git tag --contains f6ae6db6` and `git tag --contains 4a6e24f6` | `v0.22.1` for each |
| `git grep -l 1792126889 -- tests .github hooks skills bin` | no output |

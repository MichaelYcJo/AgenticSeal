# Review round 2: 1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request

```seal
target: 40d089338, fixes 7e5561f4d..40d089338
```

This is a verifying round. Its target is the diff from round 1's target 7e5561f4d to 40d089338. That diff holds the fix commit decfee662 and the orchestrator's records commits b0107c661, 4576eac1a and 40d089338. No `seal/parity.md` is declared, so the round block holds no `original:` line. `seal/config.md` has no `Record language` row and no `Pact` row, so the record is English and no pact anchor was read.

Carried from round 1 and not re-established: `RULE_FILES` reads `docs/*.md` alone (`.github/scripts/rules.py:71-79`, `.github/scripts/rules.py:211-221`), and `rule_changes.parse` accepts a `file` under any configured `Policy root`. Round 1's S7 and G9 confirmations are carried as the source the closed `gaps.md` rows cite. Every verdict below was reached this round, and both of round 1's mutants were run again.

## Findings

None. The round opened nothing that holds a defect.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `test_reads_the_to_of_an_add_as_of_a_change` stands in `Test_check_lines_in_a_to` above `test_reads_no_check_line_in_a_from` (`tests/skills/test_chain_check.py:1901-1914`), as round 1's paste-ready case gave it, word for word. The fix pass claimed the case went red under `WRITES_A_TO = ("change",)`. This round set that mutant in a scratch clone at 40d089338, and `tests/skills/test_chain_check.py` gave 1 failed and 173 passed. The one failure was the new case (executed). With the mutant removed, the module passed (executed, in the narrow run below). Read against its group: no other case of the module puts a check line in an `add`'s `to`, and the mutant shows it, since no other case went red. So the case covers an edge its group did not cover.

```seal
confirms: round-1#2
```
What holds: `CHECK_LINE_SAYS` reads "`.github/scripts/rules.py`, the reader `seal rules --check` uses, refuses this check line, which the settle writes into `{file}` as it stands: {why}" (`skills/code-review/scripts/chain_check.py:1052-1055`). The pinned copy at `tests/skills/test_chain_check.py:1786-1789` is the same text. The sentence no longer says that `seal rules --check` reads `{file}`, so it is true under any `Policy root`. The fix pass claimed that restoring the old message turned the refusal cases red. This round put the old two-line message back into the scratch clone's `chain_check.py` alone. `bin/test tests/skills/test_chain_check.py -q -k Test_check_lines_in_a_to` then gave 4 failed and 4 passed (executed). The four that failed are the four cases that assert a refusal, the new `add` case among them. The design's `to`, which round 1 named at `frame/design.md:77-86`, was folded in 40d089338 under the orchestration rule that has the orchestrator fold a frame statement the fix pass may not edit (`skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer*, read). Its words equal round 1's paste-ready text once whitespace is collapsed: 130 words on each side, equal (executed). The tree's own `chain_check.py`, run from the scratch clone over the branch's checkout with `--worktree`, printed no line for this design. So the folded `## Rule changes` still parses and its check line holds (executed, design S8).

```seal
confirms: none
```
What matched: the other statements of finding 2's claim are found and each is true, a list made by a method and not only by wording. The fix pass searched by wording, a sample, and named the `rules.py` docstring and the fragment as fixed, and `docs/the-review-record.md:197`, design G10 and `plan.md:41` as still true. This round listed the class from what produces it: the text this branch adds. Every added line of `.github/scripts/rules.py` and `skills/code-review/scripts/chain_check.py` from the base 57d6665b5 to 40d089338 was read whole (`git diff -U0`, executed). The five added lines of `skills/settle/SKILL.md` and the added docstring of `skills/settle/scripts/rule_changes.py` were read too. Each added line of the tests and of this work item's files that names `seal rules`, `rules.py`, a rule file, the policy root, the settle's write or "no pull request" was listed by `git grep` and read (executed). No added line in a script, skill or test still says that `seal rules --check` reads the file the settle writes. The `rules.py` docstring now ends "before the settle writes the line into the policy root" (`.github/scripts/rules.py:24-27`). The fragment says "In this repository, whose policy documents are `docs/`" before it names `seal rules --check`. Four statements stand in this work item's own frame: design G10, design *Out* at `frame/design.md:47`, design *Removes* at `frame/design.md:103`, and `plan.md:41`. Each is said of this repository, whose `Policy root` is the default `docs` (`seal/config.md` has no such row, read), so each is true there. All four leave the tree when the settle removes the work item. `docs/the-review-record.md:197` predates the branch and speaks of a section that does not parse, not of a check line, so it is true as it stands.

```seal
confirms: none
```
What matched: the folded `to` keeps line 83 of the design at 128 columns, where round 1's paste-ready text wrapped it. Once the settle drops the four-space indent, that line lands in `docs/the-review-record.md` at 124 columns. That file is not in `COVERED` of `tests/behaviour/test_docs_line_wrap.py`, and it already holds 44 lines over 88 columns (executed, `awk` over the file). So no check refuses the line, and a line that only reads badly is no finding.

```seal
confirms: none
```
What matched: the two `gaps.md` rows 40d089338 closes say what round 1 ran. The S7 row matches round 1's first confirmation and the G9 row matches its second, coordinates included (read, `trail/rounds/round-1.md:99-107`). Each row opens with the word `closed`, which is the spelling `skills/verify/scripts/unverified_check.py` reads as a closed row (read, its docstring at lines 47-50 and `CLOSED` at line 136). The two judgment rows b0107c661 and 40d089338 add to `frame/plan.md` *Judgments of the run* each name a date, the judgment, its grounds and the document it was judged against. The second cites the orchestration section that holds the fold rule quoted above.

```seal
confirms: none
```
What matched: the three test modules the branch touched pass at 40d089338. `bin/test tests/skills/test_chain_check.py tests/github/test_rules.py tests/skills/test_rule_changes.py -q` gave 309 passed, exit 0 (executed). This is a narrow run, not a seal of the suite.

This round leaves nothing open. What comes due is the orchestrator's broad run, and the sealer's spawn after it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite beyond the narrow runs above, the repository-wide lint and the format check: `unverified` | the whole tree at 40d089338 | the orchestrator's broad gate, `seal gate --base origin/release/v0.28.0 --record seal/threads/1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request` |
| The new `add` case on the Windows leg of `.github/workflows/test.yml` | `tests/skills/test_chain_check.py:1901-1914` | the pull request's `tests` run |
| That the release note shows this fragment under its `<!-- specs/... -->` marker once, still open in `gaps.md` | `.github/scripts/publish_release_note.py:292` | the tag's workflow at the 0.28.0 release, and the orchestrator reading the published note |

## Probes

Every probe ran in a `git clone --no-local` of the repository at 40d089338, under the round's scratch directory at `<work item>/round-2/`. Each mutant was set with the `Edit` tool and undone with `git checkout` of the one file before the next run. The clone is removed before the hand-back.

| Command | Result |
|---|---|
| `bin/test tests/skills/test_chain_check.py tests/github/test_rules.py tests/skills/test_rule_changes.py -q` | 309 passed, exit 0 |
| `WRITES_A_TO` set to `("change",)`; `bin/test tests/skills/test_chain_check.py -q -p no:xdist` | 1 failed, 173 passed; the failure is `test_reads_the_to_of_an_add_as_of_a_change` |
| `CHECK_LINE_SAYS` in `chain_check.py` set back to the message at 7e5561f4d; `bin/test tests/skills/test_chain_check.py -q -k Test_check_lines_in_a_to` | 4 failed, 4 passed; the four that failed are the cases that assert a refusal |
| `python3 -I` of the clone's `skills/code-review/scripts/chain_check.py --baseline origin/release/v0.28.0 --root` the branch checkout `--worktree` | exit 0; no line for this work item's design; notices for the verifying round, the gate record and the guarantee the chain still owes |
| `python3` comparing the words of `trail/rounds/round-1.md:79-89` with `frame/design.md:77-86` | equal, 130 words each |
| `git diff -U0 57d6665b5 40d089338` over the two scripts, and `git grep` over this work item's files for `seal rules --check` beside the settle, the policy root or `docs/` | the list read in the third confirmation |

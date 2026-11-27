# Review round 1: 1795742082-a-records-only-fix-is-keyed-on-its-finding

```seal
target: c00937a93 against origin/release/v0.39.2
```

This is the work item's first round, so no earlier round carries a coordinate or a verdict. The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md` whole at `c00937a93`. The records language and the commit language are both English, so no `pr.<lang>.md` is owed. The diff read is `68bb3d5a9..c00937a93`: `chain_check.py`, the core's row, `agents/sealer.md` step 4, the new rule of `agents/proofer.md`, `seal/follow-up.md`, and the cases in `tests/skills/test_chain_check.py` and `tests/behaviour/test_the_sealer_guarantees.py`. `seal/parity.json` is not declared, so no parity comparison is owed.

## Findings

### 1. The proofer's new rule places a merged-tree finding "in this work item's file", which reads as the work item's records as well as the file that holds the unit

```seal
severity: should
location: `agents/proofer.md:165-166`, `seal/threads/1795742082-a-records-only-fix-is-keyed-on-its-finding/frame/design.md:52`
evidence: read `agents/proofer.md:124`, `agents/proofer.md:153-169`, `skills/code-review/scripts/chain_check.py:991-996`; executed `git grep -n -e "located in this work" -e "item's file, with the merged-in" c00937a93 -- agents skills docs templates seal`
```

Why it matters: the rule tells a proofer where to locate a finding, and this work makes `location:` decide who reads a records-only fix. `chain_check.py#located_in_records` (`:991-996`) gives the fix to the sealer where the finding block names a path in the work item's records. The sentence at `agents/proofer.md:165-166` reads: "A unit of the diff or a sentence of the records that the merged tree contradicts is a finding located in this work item's file". The phrase has two readings. In one, it is the file of this work item that holds the unit or the sentence, so a code unit is located in its code file. In the other, it is a file of this work item's directory, which is how the tree's records use the phrase: the search on the evidence line prints three records outside this item that write "located in this work item's records". A proofer that takes the second reading places a code unit's contradiction on a record path alone. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* asks for one reading of text an agent acts on. The rule above it at `agents/proofer.md:124` already states the intended placement in one reading: "a finding located in the file that holds it".

The search is a sample under contract rules 12 and 19, because a statement in other words escapes it. It printed `agents/proofer.md:165-166` and the frame's own bullet at `frame/design.md:52`, which the rule copies. The snippet below covers the rule. The frame's bullet is a sentence saying what the work does, so the fix pass changes it in the same pass, or the orchestrator folds it.

```markdown
records that the merged tree contradicts is a finding located in the file
of this work item's diff or records that holds it, never in the merged-in
text, which it names on `evidence:`. No part of this read
```

## Confirmations

What matched: the key. Claimed in `phase-1.md:6`: `#located_in_records` returns `any(under(q, item) for q in f.located)`. Found at `chain_check.py:996`. `Finding.located` holds the finding block's `location:` paths alone, and `#finding_of` (`:843-850`) adds the close block's paths only to `paths`. `#records_only`, `#follows` and `#verdict_problems` are unchanged, as *Scope* item 2 says (read). So a pass that touched any path outside the records still owes the round through `#follows` (`:1007-1033`), which the unchanged S3 cases hold (executed: the module ran green).

What matched: the cases are seen red as `phase-1.md:7` claims. In the round's clone, `f.located` changed to `f.paths` turned `test_refuses_a_last_records_code_finding_its_close_places_in_the_records` red at its line assertion, `assert [] == [(..., 24)]`. The base's body, `bool(f.paths) and all(under(q, item) for q in f.paths)`, turned `test_passes_a_last_records_code_finding_fixed_in_its_records_alone` red with the extra item ending "a verifying round is owed" (executed, `## Probes`). Each new case was read against its group, the cases under `run-ends-with-verifying-round` at `tests/skills/test_chain_check.py:4566-4682`. The rewritten case is the only one whose finding names a record beside an outside path. The new case is the only one whose close block alone names the record. Neither repeats another case. The sealer's new case pins phrases that the existing `test_step_4_reads_a_records_only_fix_over_its_diff` does not.

What matched: the departure from the issue's first *Done when* line. The issue asks for a key on the fix's changed paths alone. The frame keeps the finding block's own `location:` in the key (`frame/plan.md:24`). The grounds hold on three counts. First, the frame's count says each of the 19 findings named a record in its own block (`frame/design.md` G9). Second, the owner's evidence is in owlery, which `frame/design.md` G12 says nobody opened here. This round opened it. Owlery #132 round 4 finding 1 names `frame/design.md:94-115` beside `records-place.ts:627`. Round 5 finding 1 names `frame/design.md:116-125` beside `daemon.ts:3238`. #188 round 2 finding 2 names `gaps.md:7` beside `agent-events.ts:23` (executed: `git show` of each record at its close commit in the owlery checkout). So the chosen key gives the sealer every pass the issue's evidence names, as `frame/plan.md:24` claims. Third, the guard the key keeps is real: a close block's `location:` that a fixer writes does not pick the sealer, which the new case holds (executed above).

What matched, with one route the frame does not name: the key can still be steered by an edit to the finding block itself. The proofer hands back an uncommitted record. The fix pass appends its close blocks to that file, and the orchestrator commits it once, after the pass (`skills/code-review/orchestration.md:99-112`). So no commit holds the proofer's own block, and nothing compares it with HEAD. Only the rule at `docs/forms/the-round-record.md:55`, "The finding's own block is the proofer's and is never edited", keeps a fixer from adding a record path to it (read). The base's key could be steered the same way, by replacing the code path with a record path. The new key needs only an added path, but the code path then stays on the line, and the new sentence of `agents/sealer.md` step 4 has the sealer open it at HEAD. So this change does not widen what such an edit hides. `frame/plan.md:13` names only the close-block route, and this round opens no finding on that omission.

What matched: `skills/core/SKILL.md:113`, `agents/sealer.md:105-115`, the four docstrings and the comment above `Finding` state the new condition and nothing else (read). The search of `frame/design.md` S5 prints nothing at `c00937a93`. At `68bb3d5a9` it prints the three lines G24 names (executed). No unsettled design in the tree outside this item names the paragraph opening **The last record is at HEAD**, "code half", or the sentence of `docs/forms/the-round-record.md` this item's `## Rule changes` rewrites (executed: `grep -n -F` over `seal/threads/*/frame/design.md`). The chain check's `--worktree` read prints no notice at a line of `frame/design.md` and refuses no operation of `## Rule changes` (executed).

What matched: `seal/follow-up.md:47`, the row #1615 sent, gains the class *Scope* item 8 names. It also carries G7 to G9's count as of 2026-11-27, and the clause that goes back to the weighing (read). The changelog's `### Fixed` entry and its `### Process changes` row say what the diff does, in the shape of `templates/records/process.md` (read). `pr.md:1` quotes `frame/plan.md:53` word for word (read).

What matched, on the crafter's open claim on the core's size. The claim: the cap case fails in this worktree on base as well, and the core measures 9919 at the main checkout's path. Found: the hook's output measures 10150 at the worktree's 120-character path, and the base's core gives 10125, with the root path standing three times (executed, `## Probes`). Projected to the main checkout's path, HEAD gives 9919 and the base 9894. Projected to a GitHub Actions runner's checkout path of 41 characters, HEAD gives 9913. This change adds 25 characters and leaves 81 under the cap at the main checkout. Neither sibling branch changes `skills/core/SKILL.md`: `git diff 68bb3d5a9...<branch> -- skills/core/SKILL.md` prints nothing for `fix/1624-1628-1629-a-session-is-bound-by-the-crafters-rules` at `4fc4abafa` or `fix/1633-records-name-the-base-and-version-as-values` at `d22e62cf7` (executed). So the growth is inside the headroom for the release's known work. The main checkout's path is 43 characters, not the 42 that `gaps.md:8` and `phase-1.md:12` write. The 9919 they give is the figure at 43, so the action the row names stands. The case measures a path the repository does not control, so any checkout path past about 70 characters fails it on base. That defect predates this work and is not this work's to fix.

What matched: the `gaps.md:10` row on the proofer's new rule, whose answerer is this round. The round read the rule at `agents/proofer.md:153-169` against *Scope* item 6. It holds the four facts the item lists. Its two commands are the ones `frame/design.md` G17 ran, and it agrees with `skills/code-review/orchestration.md:293-310` and with `#follows`, which lists the branch's commits with `--no-merges` and `^<base>` (read). Finding 1 is on one sentence of it. The row reads "the row *No pull request without a seal* ... guaranteed at their own pull requests". In local mode, or in a repository without the check's workflow, no pull request check ran, and the core gives that row to `agents/sealer.md` step 1 and the orchestrator in those cases. The act the sentence asks, to review none of the merged-in text, stays the same there, so this round opens no finding on it. Closing the row is the orchestrator's act.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the suite is `unverified` at `c00937a93` beyond the five modules this round ran, and the cap case at a checkout path of ordinary length is part of it | the `Broad gate` key of `seal/config.json` | the orchestrator's broad run, after finding 1 is closed |
| Whether a sealer in a real run withholds where a records-only fix left an outside path the finding asked to change (`frame/questions.md` Q1) | `seal/follow-up.md:47` | the repository owner, at the next release |
| The phase's boundary-set count, 1 failed, 1703 passed, 10 skipped (`phase-1.md:11`), which this round did not run again because the set is wider than the narrow form | `seal/threads/1795742082-a-records-only-fix-is-keyed-on-its-finding/trail/phases/phase-1.md:11` | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `PROBE_ROOT=<worktree> .venv/bin/python -m pytest -q -s <scratchpad>/1795742082-a-records-only-fix-is-keyed-on-its-finding/round-1/test_tmp_core_cap.py` | HEAD: 10150 characters at the 120-character worktree path, root path three times; the base's core: 10125. Projected to 43 characters, HEAD gives 9919. Projected to 41, HEAD gives 9913 |
| In the round's clone at `c00937a93`, `located_in_records` edited to read `f.paths`, then `pytest -q -p no:xdist tests/skills/test_chain_check.py -k code_finding` | 1 failed, 1 passed: the close-block case red at its line assertion |
| The same clone, `located_in_records` edited to the base's body, the same command | 1 failed, 1 passed: the rewritten case red with "a verifying round is owed"; the clone restored by `git checkout` |
| `bin/test -q tests/skills/test_chain_check.py` | 263 passed |
| `bin/test -q tests/behaviour/test_the_sealer_guarantees.py tests/text/test_the_rules_have_one_owner.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_a_cited_section_stands_in_its_file.py` | 121 passed |

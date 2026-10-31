# Review round 2: 1793437163-fields-stand-in-marked-blocks

```seal
target: 36cfef32 against origin/release/v0.27.0
```

This round has three jobs. It answers round 1's three closes. It reviews phase 2 as code, `6f60e85f..36cfef32` with the merge set apart: `ba347a80`, `7b6a03d6`, `63002be0`, `9f7c8f61`, `7ea1eda7`, and the records-only commits `f0b4d72d`, `aef89462` and `36cfef32`. It also judges the merge of `origin/release/v0.27.0` at `1a7d3ae3`, which brought in #1154 as `5560c742`. The work was done in a `git clone --no-local` under the session scratchpad at `36cfef32`, with the `v0.26.0` tag fetched into it.

Facts carried from round 1 without searching again: where `write_gate_file` stands (`skills/verify/scripts/broad_gate.py:2463`), where `GATE_RECORD` stands (`evals/scripts/rule_cases.py:826`), and the two commits finding 3 names (`e52833c6`, `99ca2178`). Every verdict below was reached again at `36cfef32`.

Out of scope here, and phase 3's or 4's: the agents' instructions, `skills/code-review/*.md`, writing-style, `templates/setup/config.md`, the proofer and sealer graders, the YAML splits, the version and the changelog. None of them is a finding.

## Findings

### 1. `seal gate --record` still exits 0 on a gate record the check refuses, where its last block already names the run

```seal
severity: should
location: `skills/verify/scripts/broad_gate.py:2487-2503`, `tests/skills/test_broad_gate.py:2019-2033`
evidence: executed `bin/test tests/github/test_tmp_round2.py -q -s -p no:xdist`
reopens: round-1#2
```

Why it matters: the close in `3e51b9a1` reads the file back only on the path that appends. The early return at `broad_gate.py:2487-2489` comes first. It returns the path as soon as the held file's last block names the same run, and nothing reads that file for refusals. The fix's own docstring now claims the command raises `Refused` "where the file as it would be written is one the reader refuses at a line". On the early-return path, the file as it would be written is the held file, so that claim is false. Round 1's finding named the comment line among its two cases, and the comment line still passes on this path.

The probe held a `trail/gate.md` whose last run block reads `run: aaa1111 against bbb2222`, then called `write_gate_file(item, "aaa1111", "bbb2222")`. With a comment line below the block, the call returned the path and left the file unchanged, while `fields.read` refused the file at line 7 with `COMMENT_LINE`. With a fence nobody closed below the block, the call also returned the path, and the reader refused the file at line 9 with `UNCLOSED`. In both cases `chain_check.broad_gate` refuses the record at the pull request after the command exited 0. A person reaches this path by re-running `seal gate --record` at the same tree after the record was edited. That is the moment the command could have named the line.

The proposed fix reads the file as it will stand on both paths, and writes only where it appends:

```python
    runs = fields.read(held, fields.GATE).blocks
    same = bool(runs) and runs[-1].fields[fields.RUN].value == value
    text = held if same else held.rstrip("\n") + "\n\n" + block
    # The file as it will stand is read back, the held file itself where its
    # last block already names this run: a line the reader refuses is refused
    # here, where a person can fix the file, and not at the pull request.
    # No OS precondition: this reads a string.
    after = fields.read(text, fields.GATE)
    if after.refusals:
        line, why = after.refusals[0]
        raise Refused(f"seal gate: {path} was not written: line {line}: {why}")
    if not after.blocks or after.blocks[-1].fields[fields.RUN].value != value:
        raise Refused(
            f"seal gate: {path} was not written: the reader reads no run block "
            "at its end, since a fence above the block hides it"
        )
    if same:
        return path
```

The regression case extends `Test_write_gate_file::test_refuses_a_file_whose_new_run_the_reader_would_not_read` with the two held files below. Each is refused with `match="was not written"` and left byte for byte. It should be seen red against `36cfef32`, where the call returns the path.

```python
RUN = "`" * 3 + "seal\nrun: aaa1111 against bbb2222\n" + "`" * 3 + "\n"
HELD = [
    "# x\n\n" + RUN + "\n" + "<" + "!-- a note -->\n",
    "# x\n\n" + RUN + "\na note\n\n" + "`" * 3 + "\n",
]
# ids: "a comment line below the same run", "a fence nobody closed below the same run"
```

### 2. At the 0.27.0 tag the release seal reads #1154's round records through the new reader, refuses both, and leaves the deferred row unread

```seal
severity: should
location: `.github/scripts/release_seal.py:290-371`, `seal/threads/1793438028-pre-0-23-upgrade-readings-removed/trail/rounds/round-1.md`, `seal/threads/1793438028-pre-0-23-upgrade-readings-removed/trail/rounds/round-2.md`, `seal/threads/1793437163-fields-stand-in-marked-blocks/frame/design.md:13`, `seal/threads/1793437163-fields-stand-in-marked-blocks/frame/plan.md:50-55`
evidence: executed `bin/test tests/github/test_tmp_round2.py -q -s -p no:xdist`
```

Why it matters: `frame/design.md:13` grounds *Scope* item 9 on a premise. It says a record written before the change "is read by the new reader only in a work item whose pull request is still open". That premise does not hold for `release_seal.py#chain_counts`. At a tag, it reads every round record of every work item the release's pull requests resolve to, through the tag's `chain_check.record_findings` (`release_seal.py:331-355`). The merge at `1a7d3ae3` brought in #1154's work item, whose two round records stand in labelled lines. #1154 merged into `release/v0.27.0` before this work item, so it was never in flight across the change, and nothing rewrites its records. Both records ship in 0.27.0 beside the reader that refuses them.

The probe ran `chain_counts` at `36cfef32` over the two pull requests, #1209 and this branch. It returned `(2, 3, 0, None)` and printed "the deferred row is not read: the round record's reader refused" for both of #1154's records. `record_findings` gave each of them only `NO_ROUND_BLOCK`. The 0.27.0 release seal will therefore draw its deferred row as not read. The count is knowable: #1154's findings are all closed `fixed`. The same holds for any other work item of milestone 75 that merges before this one.

The same function's docstring still states the labelled grammar's refusals (`release_seal.py:298-304`): "a finding whose `verdict:` line reads", and "no `target:` line, a finding with no `verdict:` line or a value outside the four". Since `7b6a03d6` a finding with no close block is open and is not refused. The verdict takes three values, and the refusals are the block reader's. Phase 2 left the file unchanged under *Scope* item 6, and its behaviour changed under it. Contract rule 19 puts the sentence in the commit that changed the fact.

The fix has three parts. First, the docstring, at `release_seal.py:297-304`:

```python
    `hooks/lib/routing.py#rounds`. `deferred` is the number of distinct issues
    that are the home of a finding whose close block's `verdict:` reads
    `deferred <home>`, read with `chain_check.record_findings` and `#issue_of`
    (#866): a home names an issue only where it is exactly `#N`, so a file,
    the frame, or a home with words after the issue counts none. A round
    record the check's reader refuses anything of -- one in labelled lines
    from before #1198, which holds no round block, a line of a block that does
    not parse, or a block out of its place -- leaves
```

Second, one of two choices, which is the orchestrator's to make. It can rewrite #1154's `round-1.md` and `round-2.md` into blocks with their findings, verdicts and answers unchanged, in a commit that touches only them, as `aef89462` did for this work item's round 1. Or, where it holds a merged work item's records out of this pull request's reach, it can add an *Operational impact* line to `frame/plan.md`. That line would say the 0.27.0 release seal's deferred row reads not read for each work item merged into `release/v0.27.0` before this one.

Third, `frame/design.md:13` names `release_seal.py#chain_counts` as the one reader that reads a released release's records at its tag, so the premise of *Scope* item 9 stands corrected.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the close holds (executed and read). `evals/scripts/rule_cases.py:826-841` writes `GATE_RECORD` as one run block with the hexadecimal placeholders `a0a0a0a` and `c0c0c0c`, and its comment states that shape. At `36cfef32`, `tests/behaviour/test_evals_layout.py` and `tests/evals/test_rule_cases.py` pass inside the 1054-case run in *Probes*, so the generator's output equals the committed sealer scaffolds. `f0b4d72d` folds the rule that each phase regenerates the generators of the record it reshapes into `frame/plan.md:61`. Phase 2 followed it: `SEALER_ROUND` at `rule_cases.py:796-810` writes blocks, and the five scaffolds were regenerated.

```seal
confirms: round-1#3
```
What holds: the close holds (executed and read). `gaps.md:10` closes the row with the cause, and `trail/phases/phase-1.md:7` names `unverified_check.py` from `e52833c6` and `chain_check.py` from `99ca2178`. Re-derived: `git show e52833c6:skills/verify/scripts/unverified_check.py` names `fields.py`, its parent does not, and `git log -S'hooks/lib/fields.py' -- evals/scripts/replay_targets.py` gives `99ca2178` as the first commit to list it.

```seal
confirms: none
```
What matched: *Scope* item 5's placement rules are pinned (executed). With the `OUTSIDE` refusal at `skills/code-review/scripts/chain_check.py:683-684` removed in the clone, `tests/skills/test_chain_check.py` went red on `Test_findings::test_refuses_a_block_out_of_its_place` and `test_refuses_a_record_with_no_findings_section_or_two`, and `tests/skills/test_pr_body.py` stayed green. The line was restored. This is one mutant. The crafter's 14 and 3 were not re-run, which is a row of *Not judged*.

```seal
confirms: none
```
What matched: *Scope* item 6 holds for the shipped readers (executed and read). Every attribute of `chain_check` that shipped code outside `tests/` names still exists at `36cfef32`: `BROAD_GATE_FILE`, `DEFERRED`, `FIELDS`, `issue_of`, `load`, `record_findings`, `round_of`, `round_read`, `ROUTING`, `section_end` and `SHARED_READER`. No shipped file names `label_of`, `value_of`, `GRAMMAR`, a `*_ROW` constant, `unclosed`, `comment_lines` or `CONFIRMATIONS_TABLE` of the check. `release_seal.py` and `broad_gate.py#rounds_rows` are unchanged in code, but finding 2 says where `release_seal.py` meets the change.

```seal
confirms: none
```
What matched: the first departure holds (read and executed). The crafter claimed `replay_targets.py` had to change against *Scope* item 6 because item 5 removed `label_of`, `value_of`, `finding_spans`' use of `TARGET_ROW` and `LOCATION_ROW`. `evals/scripts/replay_targets.py:86-93` and `:268-327` now read the `target:` and `location:` values with `label_value` in 0.22.0's one spelling, and end a finding at the next heading of level 3 or less, as `finding_spans` did. The round is still judged by the `round_of` of the commit that wrote it. The cases that need the `v0.26.0` tag fail with a message naming it where it is absent (`tests/evals/test_replay_targets.py:41-55`). Every pytest job of `.github/workflows/test.yml` checks out at `fetch-depth: 0` (`:118-120`, read). With the tag present, `test_replay_targets.py`, `test_seed_defects.py` and `test_noninferiority.py` pass inside the 1054-case run.

```seal
confirms: none
```
What matched: the second and fourth departures hold (read and executed). The fixtures of `tests/github/test_release_seal.py:138-169` and `tests/skills/test_broad_gate.py:1932-1951` now write blocks, and only the `answer:` replacement at `test_release_seal.py:507` changed with them. Their assertions are unchanged, and both modules pass. `evals/scripts/noninferiority.py:295-332` takes a finding's row from the `location:` line of the finding block `round_read` places in it. Its cases pass, among them `63002be0`'s case for a close block naming a location.

```seal
confirms: none
```
What matched: the third departure holds (read). `section_end` (`chain_check.py:216-225`) reads no policy document. `finding_spans` at `:598-616` and `pr_body.py` through `CHAIN.section_end` end a section with it, so it is a section helper and not part of the grammar loader. The rest of the loader the frame's *Removes* names is gone.

```seal
confirms: none
```
What matched: the crafter disclosed a slip against contract rule 9 in `tests/evals/test_replay_targets.py`, made by a script that asserted each match (read). The diff holds five call sites passing `at=LABELLED_AT` (`:138`, `:146`, `:147`, `:159`, `:164`), where the record says four substitutions. Either one substitution matched two sites, or one site went through the `Edit` tool. The text is the same either way, and each call is right.

```seal
confirms: none
```
What matched: of *Scope* item 8, the round-record writers in evals and fixtures write blocks (executed). This is a sample, found by a `git grep` on spellings of the `target:` key, so a writer that builds the line another way would not show. The one writer left in labelled lines is `tests/e2e/teammate/test_teammate_flow.py:76-82`. Its round record is not read, because the teammate's branch declares nothing, and the module passes (7 passed).

```seal
confirms: none
```
What matched: the merge holds at the pull request (executed and read). The one file changed on both sides is `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`. #1154 changed a docstring at `:1083-1088`, and phase 2 changed `:965-1000` and `:1152`, so the two sides do not overlap. The module passes. This tree's check, run with `--worktree` before this record existed, named only this work item's records. `follows` reads `--no-merges` from the base, which holds `5560c742`, so no #1154 record is judged at this pull request. `tests/test_censuses.py`, `tests/behaviour/test_release_hygiene.py`, `tests/hooks/test_dispatch.py` and `tests/hooks/test_optin.py` pass (318). #1154 removed `optin.earlier` and `EARLIER_HEADINGS`, and no phase 2 code names either. Where #1154 meets the new reader is finding 2.

```seal
confirms: none
```
What matched: no new case duplicates one in its group (executed). `bin/seal layout --pairs` over the nine test files phase 2 changed reads 9 files and names 0 pairs.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck. This round ran narrow modules only, and the suite stays `unverified` | the branch at the head the rounds settle on | the orchestrator, by `seal gate --base <base> --record <item>` once the rounds settle |
| The crafter's 84-red run against `ba347a80` and its `seal mutate` runs (14 of 14 on `chain_check.py`, 3 of 3 on `pr_body.py`). This round re-ran one mutant (the `OUTSIDE` refusal) and none of those runs | `trail/phases/phase-2.md:28-35` | the sealer, at the guarantee (contract rule 15) |
| `evals/scripts/behaviour.py#FINDINGS_SHAPE` generates the nine proofer `shape-findings.md` graders, and it requires a `verdict:` line under a finding heading. A proofer that writes an open finding by the new template has none, so every such run fails the grader until it changes | `evals/scripts/behaviour.py:76-82`, `:105-111` | phase 3's round, with the graders |
| Whether `pr_body.py#_round` should copy each confirmation block without the prose under it. Bare `confirms: none` blocks repeat in the body and say nothing to a reader of the pull request | `skills/code-review/scripts/pr_body.py:319-344` | the orchestrator, as a row of `frame/plan.md`'s *Judgments of the run* |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_chain_check.py tests/skills/test_pr_body.py tests/hooks/test_fields.py tests/github/test_release_seal.py tests/evals/test_replay_targets.py tests/evals/test_seed_defects.py tests/evals/test_noninferiority.py tests/skills/test_broad_gate.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_evals_layout.py tests/evals/test_rule_cases.py tests/text/test_the_record_is_written_in_words.py tests/text/test_a_record_carries_no_comment.py -q` at `36cfef32`, with `v0.26.0` fetched | 1054 passed, 1 skipped |
| `bin/test tests/test_censuses.py tests/behaviour/test_release_hygiene.py tests/hooks/test_dispatch.py tests/hooks/test_optin.py -q` | 318 passed |
| `bin/test tests/e2e/teammate/test_teammate_flow.py -q` | 7 passed |
| `tests/github/test_tmp_round2.py`, one file run once with `-s` and then deleted: `write_gate_file` over a held record whose last block names the run, with a comment line and then a fence nobody closed below it; `record_findings` over #1154's two round records; `release_seal.chain_counts` over #1209 and this branch | both gate calls returned the path, file unchanged, with refusals at line 7 (`COMMENT_LINE`) and line 9 (`UNCLOSED`); each #1154 record gave `NO_ROUND_BLOCK` alone; `chain_counts` returned `(2, 3, 0, None)` and printed that the deferred row is not read |
| `OUTSIDE` refusal at `chain_check.py:683-684` replaced by `continue` in the clone, then `bin/test tests/skills/test_chain_check.py tests/skills/test_pr_body.py -q`; the line restored | 2 failed (`test_refuses_a_block_out_of_its_place`, `test_refuses_a_record_with_no_findings_section_or_two`), 186 passed |
| `bin/seal layout --pairs` over the nine test files phase 2 changed | 9 files read, 0 pairs |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.27.0 --root <the branch worktree> --worktree` before this record | round 1's findings 1 and 2 owe a verifying round, the last record is behind HEAD, and the gate record and the guarantee are absent; no #1154 path named |

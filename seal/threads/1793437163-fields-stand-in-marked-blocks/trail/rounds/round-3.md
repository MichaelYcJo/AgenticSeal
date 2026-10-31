# Review round 3: 1793437163-fields-stand-in-marked-blocks

```seal
target: 609a8fc1 against origin/release/v0.27.0
```

This round has three jobs. First, it answers round 2's two closes, `fixed 1f41f9d7` and `fixed 75a4245a`, together with the two records-only rewrites that carry the second close: `977b1ac9` for #1154 and `609a8fc1` for #1126. Second, it reviews phase 3 as code and text, `977b1ac9..ab29adcf`, together with the orchestrator's `frame/questions.md` Q2 commit `369649d6`. Third, it judges the merge `dfb49c8c`, which brought in #1126 as `ea73e94f`. The work was done in a `git clone --no-local` under the session scratchpad at `609a8fc1`. The `v0.26.0` tag and `origin/release/v0.27.0` were fetched into the clone, and a `v0.26.0` worktree beside it served only to load that release's check.

Facts carried from round 2 without searching again: `write_gate_file` stands in `skills/verify/scripts/broad_gate.py` near `:2463`, `chain_counts` stands at `.github/scripts/release_seal.py:290-371`, and #1154's two records are at `seal/threads/1793438028-pre-0-23-upgrade-readings-removed/trail/rounds/`. Every verdict below was reached again at `609a8fc1`. No `seal/parity.md` exists, so the round block holds no `original:` line.

Out of scope here, and phase 4's: the YAML splits, the version and the changelog fragment. None of them is a finding.

## Findings

### 1. `skills/code-review/SKILL.md` *The record* still sends the proofer to the `evidence:` forms of a grammar row the section no longer names

```seal
severity: should
location: `skills/code-review/SKILL.md:141`
evidence: read `skills/code-review/SKILL.md:115-144`
```

Why it matters: phase 3 rewrote the paragraph that opens *The record*. Before phase 3, that paragraph said each labelled line "follows its row of the grammar table in `docs/the-review-record.md` *The round record*", and the bullet at `:141` then said "`evidence:` names what the claim rests on, in the forms its row gives". Now the paragraph says `hooks/lib/fields.py` is "the one statement of each block's lines and the shape of each value", and it names no table and no row. The bullet still says "its row". The only row a proofer can find is the docs table, which `## Rule changes` removes at the settle, and which this same section no longer calls the grammar's one statement. So the bullet points the proofer at the second source this work set out to retire. The proofer reads this sentence at step 1 of every round. Contract rule 19 asks the commit that rewrote the paragraph to correct the sentences that stood on it. The phase record calls its `git grep` sweep a sample, and its word list ("grammar table", "labelled line" and others) does not hold "its row".

The fix names the module, as the paragraph above it does:

```markdown
- `evidence:` names what the claim rests on, in the forms
  `hooks/lib/fields.py` gives its value. A claim that something is absent
  rests on a search, so its line is `executed`. The check cannot tell such a
  claim from another; the round reading the record does.
```

### 2. The script-reach module still says no document tells anybody to run a script with no subcommand, after `command_forms` was changed to let `agents/proofer.md` do it

```seal
severity: should
location: `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:33-39`, `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:307-320`
evidence: read `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:33-39`, `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:168-190`, `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:307-320`, `agents/proofer.md:56-58`
```

Why it matters: the crafter claimed that changing `command_forms`, rather than re-wrapping proofer step 7, keeps what the helper checks. On the property the module pins, the claim holds. That property is #318's: a reader told about a script can reach it. The new reader counts an invocation only where it does not carry the script's repo-relative path (`:184-190`). A located invocation is the locator the module's second rule asks of a script with a subcommand, and a wrong path still counts (`:416-425`). A scan of every shipped `.md` under `agents/`, `skills/` and `templates/` for a no-subcommand script followed by a flag found one line, `agents/proofer.md:57`, which carries the path (executed, *Probes*). So no reader loses a way to the script.

What the change does alter is the premise the exemption stood on, and two statements of that premise were left as they were. The module docstring at `:33-39` says the exemption is "for a script nobody is told to run", and says "the moment a document shows such a script being invoked, the classification stops being true and goes red". The case at `:307-320` says the script "is excused the locator rule because nobody is told to type it". Its failure message says the classification is "kept with no subcommand because no document tells anybody to run it", and offers two remedies: add the script to `TOOLS`, or take the invocation out. Since `ffbcdd78`, `agents/proofer.md` step 7 tells every proofer to run `chain_check.py`, and the case passes because the line carries the path. The crafter rewrote the helper's docstring and the `NO_SUBCOMMAND` reason in the same commit, and these three statements of the same fact stand beside them. Contract rule 19 puts each in that commit. The message matters most. An agent that meets this red case is offered two remedies and not the third, writing the script's path, which the reader now accepts.

The fix states the premise as the helper now reads it:

```python
# tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:33-39
"""
A script with no subcommand is exempt from the second rule because it has no
command to name, and requiring its path in every document that mentions it
would touch six files for a script nobody is told to run without being told
where it is. `test_a_script_with_no_subcommand_is_shown_in_no_command_form`
is what keeps that exemption from being a loophole: the moment a document
shows such a script being invoked without its repo-relative path, the
classification stops being true and goes red rather than standing as a note.
"""

# :307-320
def test_a_script_with_no_subcommand_is_shown_in_no_command_form(pair):
    """What keeps the exemption above from being a loophole. A script with no
    subcommand is excused the locator rule because nobody is told to type it
    without its repo-relative path, and this is that premise asked of the
    tree rather than assumed."""
    document, script = pair
    base = os.path.basename(script)
    shown = command_forms(read(os.path.join(ROOT, document)), script)
    assert not shown, (
        f"{document} shows {base} being invoked without its path, so the "
        f"classification in {os.path.basename(__file__)} -- kept with no "
        "subcommand because no document tells anybody to run it without "
        "saying where it is -- is no longer true:\n"
        + "\n".join(f"  {document}:{n}: {line.strip()}" for n, line in shown)
        + "\n\nEither add it to `TOOLS` in `skills/implement/scripts/seal.py`, "
        f"write the invocation with its path `{script}`, or take it out."
    )
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: the close holds (executed and read). `skills/verify/scripts/broad_gate.py:2487-2505` now reads `held` back through `fields.read` where its last run block names the same run, and it returns the path only after the refusal check and the last-block check. The docstring at `:2464-2471` says so. With `broad_gate.py` taken from `b92f3a9e`, the commit before the fix, `Test_write_gate_file` failed on its two new parameters, "a comment line below the same run" and "a fence nobody closed below the same run" (2 failed, 7 passed). Restored to `609a8fc1`, `tests/skills/test_broad_gate.py` and `tests/github/test_release_seal.py` passed (360 passed, 1 skipped). The idempotent path still holds: `test_refuses_to_record_one_run_twice` passes on a clean held file.

```seal
confirms: round-2#2
```
What holds: the close holds (executed and read). The docstring of `chain_counts` at `.github/scripts/release_seal.py:297-310` now states the block reader's refusals: a record with no round block, a block line that does not parse, a block out of its place, and a finding with no finding block, which `chain_check.py:750` refuses as `NO_FINDING_BLOCK`. It also says a finding with no close block is open and counts none, which matches `(OPEN, None)` and `issue_of` returning nothing. The frame folds the route at `b92f3a9e`: `frame/design.md:13` and *Scope* item 9, and `frame/plan.md` *Operational impact* and *Judgments of the run*.

The orchestrator claimed it compared the rewrites line by line. Re-derived here over all five files of `977b1ac9` and `609a8fc1` against each commit's parent: each file only gains lines of three backticks with `seal` and closing fences (10, 13, 11, 6 and 3 pairs). It loses no line, and its other lines keep their order once fences, blank lines and `verdict:` lines are set aside. `v0.26.0`'s `round_of` over each original and this tree's `round_of` over each rewrite returned no errors on either side. They returned the same target, the same findings with their verdicts, paths and references, and the same held numbers. The `confirms:` references differ only in the line each stands on, moved down by the added fences. `chain_counts` over the clone returned `(2, 5, 0, 0)` for #1209 and #1210, as the orchestrator reported, and `(3, 7, 0, 0)` with this branch added. `git log --first-parent 15a5ce66..origin/release/v0.27.0` lists only #1209 and #1210, so no other item merged into the base still holds labelled records.

```seal
confirms: none
```
What matched: the first departure holds (read). The crafter claimed that *Scope* item 7's sentence for `skills/writing-style/SKILL.md`, said of every record, would be false. *Scope* *Out* keeps `routing.md`'s table, `## Rule changes`, *Judgments of the run* and `gaps.md`'s `## Not verified` outside blocks, and each is read by a check. The rewritten sentence at `skills/writing-style/SKILL.md:264-267` names the round records, `guarantee.md` and `trail/gate.md`, which are Table F's three files. It drops the sentence that whether a near-miss line meant the label is the reading agent's judgment, and `skills/core/SKILL.md` *The rule a mechanism is kept against* still states that for every other form, so no rule is lost.

```seal
confirms: none
```
What matched: the second departure holds (read). Each of the five files outside item 7's list stated a fact phase 1 or 2 changed, and each now states the new one. `skills/implement/SKILL.md:485-491` and `skills/implement/acts.md:72` now say close block where they said two lines. `skills/legacy-parity/SKILL.md:112-113` says the round block, and the verdict block of each sealer run, which matches `agents/sealer.md` step 5 and the last-block reading of `originals_of`. `skills/verify/orchestration.md:432-437` says the finding block's `severity:` and `location:`, and a block per broad run with the newest last. `skills/writing-style/outside-the-review.md:63` says the body copies every `seal` block and finding heading. Two more stale sentences of the same class are findings 1 and 2, which the sweep's word list did not reach. The phase record calls the sweep a sample, which is honest.

```seal
confirms: none
```
What matched: the graders hold (executed and read). The diff changes exactly the nine proofer `shape-findings.md` and the five sealer `shape-verdict.md` graders. `FINDINGS_SHAPE` at `evals/scripts/behaviour.py:76-84` asks for a block opened by `severity:` in the same `### <n>.` section, and the sealer pattern at `evals/scripts/rule_cases.py:977-989` asks for the `Verdict:` line inside a block whose lines open no fence. The four `truth-*` graders read `^Verdict:.*` with `mi` flags. A verdict block's `Verdict:` line starts at column 0 of the file, so each still finds its outcome. The shape grader of the same case is what requires the block. `tests/evals/test_rule_cases.py` and `tests/behaviour/test_evals_layout.py` pass inside the run in *Probes*. `bin/seal layout --pairs` over phase 3's 14 changed test files names no pair. Q2's answer at `369649d6` says the same as `trail/phases/phase-3.md`.

```seal
confirms: none
```
What matched: the instructions agree with Table F and the reader (read). `agents/proofer.md:48-60` has the proofer write a round block and finding blocks and no close block. `agents/crafter.md:164-187` has the fix pass append a close block, with a `location:` line where the fix went elsewhere, and edit nothing of the proofer's. `chain_check.py#verdict_problems` at `:1091-1119` accepts a `fixed` commit touching a path either block's `location:` names. `agents/sealer.md:100-117` and `:170-176` append one verdict block per run, and `templates/records/sdd-guarantee.md` holds that block. `skills/code-review/orchestration.md:151-153`, `:199` and `:379-383` cover the orchestrator's own closes and a fence near the opener at the preflight. `templates/setup/config.md:126-133` names `hooks/lib/fields.py` and copies no key, which `test_the_exclusion_list_points_at_the_block_grammar_and_restates_none_of_it` pins.

```seal
confirms: none
```
What matched: `gaps.md` *Not done* is accurate (read). `skills/code-review/orchestration.md:437-452`, *Orchestrator: verify before posting*, holds four checks and none reads the record against the template. *Scope* item 7 names only the preflight reading. The docs sentence that names that read as what catches a finding written inside a fence stood before #1198. `CONTRIBUTING.md:386-394`, **What it reads**, states the rule for every gate, and the readers of the forms this work kept still name near misses, so the paragraph is still true. Where the *Not done* item goes after the settle is a row of *Not judged*.

```seal
confirms: none
```
What matched: the merged tree holds (executed and read). `tests/conftest.py` changed on both sides of `dfb49c8c` in separate hunks: #1126 added `directory=` to `symlink_or_skip` at `:626-647`, and this branch rewrote `guarantee_record` from `:1548`. The merge keeps both. #1126 adds `skills/settle/SKILL.md`, `skills/settle/scripts/settle.py` and its records, and no sentence of the old record grammar (executed, `git grep` over `skills/`). `settle.py` reads `gaps.md`, `frame/design.md` and `frame/plan.md` by name and reads no round record. `tests/skills/test_settle.py` and `tests/text/test_settle_reads_before_it_removes.py` pass inside the run in *Probes*. This tree's check with `--worktree` names no record of #1154 or #1126. `edited_work_items` at `chain_check.py:1074-1088` judges only a work item whose `frame/design.md` this pull request's own commits change, and the two rewrite commits touch only round records.

```seal
confirms: none
```
What matched: the crafter's boundary run is matched in kind (executed). Its 95 modules and 4140 passes are its claim. This round selected the 92 test modules under `tests/` that a `git grep` for the names of phase 3's changed paths lists, and added `tests/github/test_release_seal.py`, `tests/hooks/test_fields.py`, `tests/hooks/test_blocks.py` and `tests/skills/test_seal_stamp.py`. That run gave 4025 passed and 9 skipped, and `bin/seal rules --check` exited 0. The two selections differ, so the counts do not compare.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck. This round ran narrow module sets only, and the suite stays `unverified` | the branch at the head the rounds settle on | the orchestrator, by `seal gate --base <base> --record <item>` once the rounds settle |
| The *Not done* item on *Orchestrator: verify before posting* stands only in `gaps.md` *Not done*, which no reader tracks: the settle closes `## Not verified` rows and removes the directory. After 0.27.0 settles, nothing holds the missing template read | `seal/threads/1793437163-fields-stand-in-marked-blocks/gaps.md:20`, `skills/code-review/orchestration.md:437-452` | the orchestrator: a `seal/follow-up.md` row or an issue, or a row of *Judgments of the run* saying why none |
| *Scope* item 9 rewrites the records of items merged into `release/v0.27.0` before this pull request opens. An item merged after it opens and before it merges is checked against the base's 0.26.0 reader and lands in labelled lines, and the release seal then reads its deferred row as not read | `frame/design.md` *Scope* item 9 | the orchestrator, by reading `git log --first-parent` of the base before the merge |
| The crafter's `seal mutate` runs and its seen-red runs listed in `trail/phases/phase-3.md:27-48`. This round re-ran the round-2 fix's red case and none of the phase's | `trail/phases/phase-3.md` | the sealer, at the guarantee (contract rule 15) |
| Whether a proofer and a sealer that follow the rewritten instructions pass the changed graders | `gaps.md` *Not verified* | the next comparison of the proofer and sealer suites, run on both sides fresh |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_broad_gate.py -q -k Test_write_gate_file` with `broad_gate.py` checked out from `b92f3a9e`, then restored | 2 failed (the two same-run parameters), 7 passed |
| `bin/test tests/skills/test_broad_gate.py tests/github/test_release_seal.py -q` at `609a8fc1` | 360 passed, 1 skipped |
| A line comparison in Python over the five files of `977b1ac9` and `609a8fc1` against each parent | only fence lines added, none removed, order the same apart from fences, blank lines and `verdict:` lines |
| `tests/github/test_tmp_round3.py`, one file run once with `-s` and then deleted: `release_seal.chain_counts` over #1209 and #1210, then with this branch; `round_of` of `v0.26.0`'s check over each original against this tree's over each rewrite | `(2, 5, 0, 0)` and `(3, 7, 0, 0)`; no errors on either side; the same target, findings, verdicts, paths, references and held numbers, with only the line numbers of `confirms:` moved |
| A Python scan of every tracked `.md` under `agents/`, `skills/` and `templates/` for `rule_changes.py` or `chain_check.py` followed by a flag | one line, `agents/proofer.md:57`, carrying the path |
| `bin/test` over the 92 modules a `git grep` for phase 3's changed paths lists, with `tests/github/test_release_seal.py`, `tests/hooks/test_fields.py`, `tests/hooks/test_blocks.py` and `tests/skills/test_seal_stamp.py`, `-q` | 4025 passed, 9 skipped |
| `bin/seal rules --check` | exit 0 |
| `bin/seal layout --pairs` over phase 3's 14 changed test files | 14 files read, 0 pairs |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.27.0 --root . --worktree` in the clone, before this record | round 2's two closes owe a verifying round, the last record is behind HEAD, and the gate record and the guarantee are absent; no #1154 or #1126 path named |

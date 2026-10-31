# Review round 1: 1793437163-fields-stand-in-marked-blocks

target: 968f5ac4 against origin/release/v0.27.0

This is round 1, so no earlier record exists and no fact is carried. Every fact below was established this round at `968f5ac4`, in a `git clone --no-local` under the session scratchpad. The scope is phase 1, `b72008ec..968f5ac4`: `frame/design.md` *Scope* items 1 to 4, and item 9 for the guarantee and the gate record, with Table F as the grammar. The round records' reader, the round template, the agents' instructions, writing-style, the eval graders, the YAML splits, the version and the changelog belong to phases 2 to 4. None of them is a finding here.

## Findings

### 1. Phase 1 leaves the suite red on a case its own commit broke, and the generator's comment still states the old gate shape

severity: must
location: `evals/scripts/rule_cases.py:826-833`, `evals/scripts/rule_cases.py:913`, `evals/behaviour/sealer/rule-sealer-false-red/scaffold.sh`, `evals/behaviour/sealer/rule-sealer-sealed/scaffold.sh`, `evals/behaviour/sealer/rule-sealer-stale-gate/scaffold.sh`, `evals/behaviour/sealer/rule-sealer-untrue-body/scaffold.sh`
evidence: executed `bin/test tests/hooks/test_fields.py tests/hooks/test_blocks.py tests/skills/test_seal_stamp.py tests/skills/test_pr_body.py tests/behaviour/test_the_sealer_guarantees.py tests/behaviour/test_evals_layout.py tests/evals/test_replay_targets.py tests/hooks/test_sealer_stamp_queue.py -q`, `.venv/bin/python evals/scripts/rule_cases.py`, `.venv/bin/python -m pytest -q tests/behaviour/test_evals_layout.py tests/evals/test_rule_cases.py`
verdict: fixed e6c81213

The crafter claimed that `tests/behaviour/test_evals_layout.py::test_the_sealer_cases_are_the_generators_output` is red at the phase boundary and that phase 3 owns the repair under *Scope* item 8. The claim about the result holds. At `968f5ac4` that case fails with four differing scaffolds: `rule-sealer-false-red`, `rule-sealer-sealed`, `rule-sealer-stale-gate` and `rule-sealer-untrue-body`. Every other case of the eight modules passed (1 failed, 314 passed).

Leaving it red is not acceptable here, and the generator's gate record belongs in this phase. Commit `99ca2178` changed the shape of `trail/gate.md` and changed `pr_body._gate` to copy run blocks. `evals/scripts/rule_cases.py:826-827` still says that `GATE_RECORD` is the record "in `broad_gate.write_gate_file`'s shape", and `GATE_RECORD` still writes the `Broad gate` table. Contract rule 19 asks the commit that changes a fact to correct, in the same commit, every sentence and case that stated it. *Scope* item 8 covers the graders and the scaffolds' reading of verdicts, but this constant is a second writer of the gate record that `99ca2178` changed. Leaving it costs every later phase boundary one known red case, which hides any new red among the same modules. The repair is also not named in `frame/plan.md`'s phase 3 row; only the phase record carries it. The repair is small and has been run. With the change below, the generator rewrites exactly the four scaffolds, and both `tests/behaviour/test_evals_layout.py` (14 passed) and `tests/evals/test_rule_cases.py` (19 passed) go green. The placeholders have to be hexadecimal, as `BUILD_SHA` already is. `pr_body.compose` now reads the gate record through `hooks/lib/fields.py` before the scaffold fills it, and `RUN_SHA` does not match the `run:` shape, so the old placeholders make the generator refuse the record.

````python
# evals/scripts/rule_cases.py, replacing the GATE_RECORD block at :826-833
# The record `seal gate --record` writes, in `broad_gate.write_gate_file`'s
# shape: the work item's heading and one run block. Its commits are
# placeholders the scaffold fills, hexadecimal as `BUILD_SHA` is, because
# `pr_body.compose` reads the block through `hooks/lib/fields.py` first.
RUN_SHA = "a0a0a0a"
BASE_SHA = "c0c0c0c"
GATE_RECORD = f"""# {{item}} — broad gate

```seal
run: {RUN_SHA} against {BASE_SHA}
```
"""

# and at :913
    ran = [(RUN_SHA, "$run"), (BASE_SHA, "$(git rev-parse main)")]
````

Then run `python3 evals/scripts/rule_cases.py` and commit the four regenerated scaffolds with it. Where the orchestrator keeps the repair in phase 3 anyway, `frame/plan.md`'s phase 3 row names the case in its *Verified by* cell.

answer: Fixed as the finding proposes: `GATE_RECORD` is one run block with the hexadecimal placeholders `a0a0a0a` and `c0c0c0c`, its comment states that shape, and `rule_cases.py` regenerated exactly the four sealer scaffolds; `tests/behaviour/test_evals_layout.py` and `tests/evals/test_rule_cases.py` pass (33). The class searched by `git grep` for a `Broad gate` cell with a run, `Target SHA` and `earlier run:` outside `seal/` and `docs/`, and for every writer of `trail/gate.md` or `guarantee.md` in `evals/scripts` and shipped code: no other generator or fixture writes either record in the old shape except the tests' deliberate old-shape refusal inputs; `agents/sealer.md` and `templates/setup/config.md` stay phase 3's. The phase record's paragraph that gave this case to phase 3 is rewritten in 5d5a1813.

### 2. `seal gate --record` reports success on a gate record whose new run the reader does not read

severity: should
location: `skills/verify/scripts/broad_gate.py:2463-2498`, `tests/skills/test_broad_gate.py:1959`
evidence: executed `.venv/bin/python -m pytest -q -s tests/skills/test_tmp_round1.py`
verdict: fixed 3e51b9a1

Before this phase, `write_gate_file` wrote the whole file from scratch, so its output always read. Now it appends the assembled block to whatever text `trail/gate.md` holds. It checks the block alone (`fields.assemble`) and never reads back the file it writes. Its docstring says it raises `Refused` where "the run is not one the reader reads", but that holds only for the block in isolation. This is a new failure path that the change introduces.

The probe showed two cases. In the first, a held file ends with a fence nobody closed (`a note`, then a line of three backticks). The appended block's closing fence then closes that earlier fence. The file reads `Read(blocks=[], refusals=[], notices=[])`, and the command returns its path as written. At the pull request `chain_check.broad_gate` then refuses with `NO_RUN_BLOCK`, which tells the person to run `seal gate --base <base> --record <item>`, the command they have just run. Running it again appends a second block that does read, so the first run left a misleading record and no error. In the second case, a held file holds a line that begins with an HTML comment opener. That file is written too, and the reader refuses it at line 1.

The command should refuse here, at the moment a person can fix the file, and not at the pull request.

```python
    runs = fields.read(held, fields.GATE).blocks
    if runs and runs[-1].fields[fields.RUN].value == value:
        return path
    text = held.rstrip("\n") + "\n\n" + block
    # The file as it will be written is read back: a run below a fence nobody
    # closed, or in a file the reader refuses at a line, is refused here
    # rather than at the pull request. No OS precondition: this reads a string.
    after = fields.read(text, fields.GATE)
    newest = after.blocks[-1].fields[fields.RUN].value if after.blocks else None
    if after.refusals or newest != value:
        said = (
            f"line {after.refusals[0][0]}: {after.refusals[0][1]}"
            if after.refusals
            else "the reader reads no run block at its end"
        )
        raise Refused(f"seal gate: {path} was not written: {said}")
```

The regression case belongs in `Test_write_gate_file`. A held `trail/gate.md` of `"# x\n\na note\n\n" + "`" * 3 + "\n"` is refused with `match="was not written"`, and the file is left byte for byte as it was. The case should be seen red against `968f5ac4`, where the call returns the path.

answer: Fixed: `write_gate_file` reads the file as it would write it through `hooks/lib/fields.py` and refuses, writing nothing, where the reader refuses a line or the last block is not the new run. The new case `Test_write_gate_file::test_refuses_a_file_whose_new_run_the_reader_would_not_read`, over a held fence nobody closed and a held comment line, was red against the writer before the fix, and `seal mutate` over the two new refusals turned both red. Class: the only record writer this phase changed that appends is `write_gate_file`; `rule_cases.py` writes whole records and composes the body through `pr_body.compose`, which reads them through the reader, and the stamp and `pr_body.py` write no record.

### 3. `gaps.md` hands the orchestrator an "unexplained" failure whose cause is in this phase's first commit

severity: should
location: `seal/threads/1793437163-fields-stand-in-marked-blocks/gaps.md:8`, `seal/threads/1793437163-fields-stand-in-marked-blocks/trail/phases/phase-1.md:7`
evidence: executed `.venv/bin/python -m pytest -q tests/evals/test_seed_defects.py tests/evals/test_replay_targets.py`
verdict: fixed 5d5a1813

The row at `gaps.md:8` says `tests/evals/test_seed_defects.py` failed 7 of its 17 cases twice, that "the cause was not found", and that "no phase 1 change touches what it reads". The second statement is false, and the cause can be found. The test builds a repository from the working tree's copy of each `replay_targets.CHECK_FILES` file (`tests/evals/test_seed_defects.py:85-94`). One of those files is `skills/verify/scripts/unverified_check.py`. At `e52833c6` that module starts loading `hooks/lib/fields.py` when it is imported (`unverified_check.py:181` at `968f5ac4`). `CHECK_FILES` gained `hooks/lib/fields.py` only at `99ca2178`. So any tree between the two edits fails to load the copied check.

Run on a `git archive` of `e52833c6`, the command above fails exactly 7 cases of `test_seed_defects.py`, with `replay_targets: ... chain_check.py will not load: [Errno 2] No such file or directory: .../hooks/lib/fields.py`. It also fails the replay case the phase record names. At `968f5ac4` the same command passes all 33 cases. The crafter's two failing runs had uncommitted edits or a partial stash in the tree, and that matches a working tree holding `e52833c6`'s reader without the `CHECK_FILES` line. The phase record's departure at `phase-1.md:7` names `chain_check.py` as the module that needs `fields.py` beside it. At `e52833c6`, though, the first module to need it is `unverified_check.py`, so `e52833c6` is a commit where those 8 cases are red. As written, the row sends the orchestrator to investigate a failure at the broad gate that is already explained, and the sealer will read the false sentence as a claim.

The row should be replaced by a closed account, for example:

```markdown
| `tests/evals/test_seed_defects.py` failed 7 of 17 cases in two runs during phase 1. The test copies the working tree's `replay_targets.CHECK_FILES` into a scratch repository; from `e52833c6` `unverified_check.py` loads `hooks/lib/fields.py`, which `CHECK_FILES` lists only from `99ca2178`, so a tree between the two fails the same 7 cases (and `test_replay_targets.py`'s labelled-record case) as `e52833c6` does. All pass at `968f5ac4` | closed |
```

In `phase-1.md:7`, "`chain_check.py` now loads `hooks/lib/fields.py`" should become a sentence that names `unverified_check.py` from `e52833c6`, and `chain_check.py` from `99ca2178`.

answer: Fixed: the row is closed with its cause, and `phase-1.md` names `unverified_check.py` from `e52833c6` and `chain_check.py` from `99ca2178`. Run at `e52833c6`, `tests/evals/test_seed_defects.py` gave 7 failed, each on the copied check failing to load `skills/verify/scripts/../../../hooks/lib/fields.py`, which is the cause the finding names.

## Confirmations

confirms: none
#1122 closes as *Scope* item 4 asks (executed). `tests/skills/test_seal_stamp.py::Test_queue_for_written_guarantee::test_a_guarantee_holding_a_fence_nobody_closed_queues_nothing[as filed]` is red on a `git archive` of `15a5ce66` with this branch's test file copied in: the old stamp queued one stamp. It is green at `968f5ac4`. The crafter claimed that `[under the newest]` is red against a reader without the unclosed-fence refusal. Removing the `UNCLOSED` line at `hooks/lib/fields.py:360` turned exactly that parameter red and left the other two green, as the phase record says. The stamp now reads the guarantee through `hooks/lib/fields.py`, which is the reader `chain_check.guarantee` uses (`skills/verify/scripts/seal_stamp.py:1145-1166`, read).

confirms: none
The first departure holds (executed). `evals/scripts/replay_targets.py:193` had to gain `hooks/lib/fields.py`. Without it, `tests/evals/test_replay_targets.py::Test_module::test_a_labelled_record_is_read_by_the_grammar_of_the_commit_that_wrote_it` fails at `e52833c6`, and it passes at `968f5ac4`. *Scope* item 6's own aim, that the readers of the round records keep working, needs the line.

confirms: none
The second departure holds (read). `tests/behaviour/test_release_hygiene.py:559-587` refuses a loaded file that names a version at or above the running one. "since 0.27.0" in `chain_check.NO_RUN_BLOCK` and `NO_VERDICT_BLOCK` would therefore go red at the release and stay red. "since #1198" stays true and still points at the change. Both sentences are pinned (`tests/skills/test_chain_check.py:2663-2666`, `:2877-2880`, read).

confirms: none
The third departure, `fields.UNSURE`, is a refusal that fails closed (executed and read). Below a line that opens an HTML block, or below a fence inside a container, `blocks.walk` stops placing fences (`hooks/lib/blocks.py:300-308`, read). Without the refusal, a later verdict block would silently vanish and an earlier one would read as the newest. The probe confirmed it: `<details>` above a run block is refused at the fence line, and no block is returned. That matches *The rule a mechanism is kept against*: a script holds a gate only on what it reads exactly. Whether the settled `docs/` text should name this refusal is a row of `## Not judged`.

confirms: none
*Scope* items 2 and 3 are built as written (executed and read). `git grep` over the tree outside `seal/` and `.test_durations` finds no code reader of `verdicts_of`, `target_of`, `target_row`, `earlier_verdicts`, `unread_verdicts`, `RETIRED_VERDICTS`, `newest_run`, `kept_runs`, `EARLIER_RUN`, `TARGET_WRITTEN` or `unread_originals`. The one hit is the historical seeded eval `seeded-f1c9932d`, which patches an old commit. `chain_check.broad_gate` and `chain_check.guarantee` read the last block, refuse a record that has no block, and return the reader's refusals with their lines (`skills/code-review/scripts/chain_check.py:1848-1935`, read). `templates/records/sdd-guarantee.md` holds one verdict block and keeps the tables for people.

confirms: none
The narrow modules pass (executed). In the clone, `tests/skills/test_chain_check.py`, `tests/skills/test_broad_gate.py`, `tests/behaviour/test_one_word_one_meaning.py`, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` and `tests/skills/test_unverified_check.py` gave 1019 passed and 1 skipped. The other eight modules failed only the case in finding 1. `seal layout --pairs` over the six changed test files names 0 pairs, so no new case duplicates one in its group.

confirms: none
`frame/questions.md` Q1 holds as answered (read). `tests/behaviour/test_one_word_one_meaning.py:401-420` now accepts "`seal` block" as a name, in the same commit (`99ca2178`) as the docstring it would otherwise refuse.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck. This round ran only narrow modules, and the suite stays `unverified` | the branch at the head the rounds settle on | the orchestrator, by `seal gate --base <base> --record <item>` once the rounds settle |
| The crafter's `seal mutate` runs over `seal_stamp.py` (10 mutants, 8 red, then 2 survivors closed), `chain_check.py` (13, 12 red), `broad_gate.py`, `pr_body.py` and `blocks.py`. This round re-ran one mutant (the unclosed-fence refusal) and not those runs. The stamp cases rewritten after the code at `780d2022` rest on them, as the test-first lapse says | `trail/phases/phase-1.md:30-41` | the sealer, at the guarantee (contract rule 15) |
| Whether `## Rule changes`' `to:` text for *What the check reads at the pull request* should name the `fields.UNSURE` refusal, which a person can meet and the settled `docs/` will not mention | `frame/design.md:238`, `hooks/lib/fields.py:247-252` | the orchestrator, as a row of `frame/plan.md`'s *Judgments of the run* |
| Whether `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#_literal_strings` gains the keys of `hooks/lib/fields.py` and the info string `seal`, deferred with `templates/setup/config.md` to phase 3 | `trail/phases/phase-1.md:45` | phase 3's round |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/hooks/test_fields.py tests/hooks/test_blocks.py tests/skills/test_seal_stamp.py tests/skills/test_pr_body.py tests/behaviour/test_the_sealer_guarantees.py tests/behaviour/test_evals_layout.py tests/evals/test_replay_targets.py tests/hooks/test_sealer_stamp_queue.py -q` at `968f5ac4` | 1 failed (`test_the_sealer_cases_are_the_generators_output`, four scaffolds differ), 314 passed |
| `bin/test tests/skills/test_chain_check.py tests/skills/test_broad_gate.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/skills/test_unverified_check.py -q` at `968f5ac4` | 1019 passed, 1 skipped |
| `.venv/bin/python -m pytest -q tests/skills/test_seal_stamp.py -k nobody_closed` on a `git archive` of `15a5ce66`, with this branch's `tests/skills/test_seal_stamp.py` copied in | `[as filed]` failed, with one stamp queued; `[in blocks]` and `[under the newest]` passed |
| `UNCLOSED` refusal removed at `hooks/lib/fields.py:360`, then `.venv/bin/python -m pytest -q tests/skills/test_seal_stamp.py -k nobody_closed`; the line restored | `[under the newest]` failed and the other two passed |
| `.venv/bin/python -m pytest -q tests/evals/test_seed_defects.py tests/evals/test_replay_targets.py` on a `git archive` of `e52833c6`, then at `968f5ac4` | at `e52833c6`: 8 failed (7 of `test_seed_defects.py` and the labelled-record replay case), each because the copied check cannot load `hooks/lib/fields.py`; at `968f5ac4`: 33 passed |
| `tests/skills/test_tmp_round1.py`, one file run once with `-s` and then deleted: `write_gate_file` over a held file ending in an unclosed fence, and over one holding a comment line; `fields.read` of a gate record with `<details>` above its block | first case: the path is returned and the file reads no block and no refusal; second case: written, and refused at line 1; third case: refused at the fence line with `UNSURE` |
| `GATE_RECORD` as a run block with hexadecimal placeholders, then `.venv/bin/python evals/scripts/rule_cases.py` and `.venv/bin/python -m pytest -q tests/behaviour/test_evals_layout.py tests/evals/test_rule_cases.py`, in the clone | four sealer scaffolds rewritten, nothing else; 14 passed and 19 passed |
| `bin/seal layout --pairs` over the six changed test files | 0 pairs |

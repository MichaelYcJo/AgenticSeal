# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — review round 1

target: 73d0d409 against release/v0.22.1

## Findings

### 1. The sealer is told a records-only commit after its guarantee owes no new audit, and the check refuses exactly that commit

severity: must
location: `agents/sealer.md:124-127`, `tests/test_the_sealer_guarantees.py`
verdict: fixed 6366ee46

The rule *The guarantee covers HEAD* now reads "A commit after the one
`guarantee.md` names, other than yours and the work item's records, owes a
new audit". Before this diff it read "other than the gate's and yours", which
was right. The widening is new in this branch's rewrite of the definition.

Read: `docs/the-review-record.md:251-253` says "Only the closing records,
`broad-gate.md` and `guarantee.md`, may follow the commit it names, since
every other file on the branch is one the sealer audited".
`skills/code-review/scripts/chain_check.py#guarantee` calls `follows(..., only=CLOSING_RECORDS)`,
and `follows` (`chain_check.py:1381-1412`) returns `("after", commit, path)`
for any path that is not `<item>/broad-gate.md` or `<item>/guarantee.md`, so a
changelog or phase-record commit after the guarantee fails a ready pull
request. `skills/code-review/orchestration.md` says the same thing in its
own words: a records-only repair is committed and the sealer is spawned again.
The definition is the one reader of the three that says otherwise. The
sealer also audits the changelog fragment and the phase records as parties
(step 2 and step 4), so a records commit is exactly what a new audit has to
read. A sealer that believes the sentence keeps an earlier verdict over a
changelog it never read, and the line's own `Enforced by:`
(`TestGuarantee`) tests the check, which says the opposite.

```markdown
**The guarantee covers HEAD, and a re-run audits what came after.** A commit
after the one `guarantee.md` names, other than one touching only
`broad-gate.md` or `guarantee.md`, owes a new audit, and the check at the
pull request refuses the file until it has one. Where an earlier
`guarantee.md` stands, the new audit re-runs only the claims whose
coordinates a commit since its `Target SHA` touched, reads the parties
again, and keeps the earlier verdict on the `Target SHA` row as
`; earlier run: <sha> <verdict>`.
```

answer: Taken as proposed in 6366ee46, worded as `docs/the-review-record.md` words it: "other than one touching only the closing records, `broad-gate.md` and `guarantee.md`, owes a new audit". 2d0babf9 rewrapped the paragraph and named the new pin `TestDefinition::test_the_guarantee_rule_exempts_only_the_closing_records` on its `Enforced by:` line; the pin went red under `mutation-check` restoring the old words.

### 2. Seven sentences outside the two #967 and #968 files still give the broad run, its stamp or its log to the sealer

severity: must
location: `templates/config.md:213-214`, `templates/config.md:223-225`, `skills/verify/scripts/seal_stamp.py:864`, `docs/commit-review-gate-spec.md:44-45`, `docs/the-review-and-parity-arms.md:119`, `docs/the-agent-set.md:113`, `agents/warden.md:144-145`, `tests/test_the_seal_is_taken_once_by_the_sealer.py:8310`, `tests/test_a_reference_root_is_read_and_never_taken.py`, `tests/test_the_gate_asks_the_range_ci_will_ask.py`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/overview.md`
verdict: fixed 2d0babf9

S12 says the class grep finds nothing outside `seal/specs/`, `changelog/`,
`agents/smith.md` and `agents/framer.md`. The grep `spec.md` names looks
for *sealer runs/takes the gate*. It does not find the sealer named as
owner of the stamp, the log or the run's place in the order, and this diff
already rewrote that same shape elsewhere: `hooks/dispatch.py:28` became
"before the broad gate's stamp", `broad_gate.py:1086` "what the gate's stamp
covers", `broad_gate.py:2707` "the gate's stamp". Phase 3 says the wider
grep "now finds the following, and nothing else"; it did not cover this
shape (contract §12).

Executed: `git grep -n -i -w sealer` over `skills docs templates hooks bin`
and both READMEs, each hit opened. Then `git grep -n -i -E "sealer|broad gate|broad-gate" -- agents`.
Past-tense history was left alone: `docs/the-broad-gate.md:96-98, 122, 215`,
`skills/config/SKILL.md:81` and `hooks/config.py:273`. The present-tense
statements that are false at 73d0d409:

- `templates/config.md:213-214`: "the command runs unattended — the sealer
  asks nobody anything". The sealer no longer runs the command. This is the
  template a plugin user copies.
- `templates/config.md:223-225`: "The sealer does not pick a command either
  — … what the sealer's seal covers is exactly that". `broad_gate.py:1086`,
  the message this paragraph explains, now says "the gate's stamp".
- `skills/verify/scripts/seal_stamp.py:864`: the `seal-stamp` help text,
  "Print the sealer's seal — the letter the broad gate stamps".
- `docs/commit-review-gate-spec.md:44-45`: "before the sealer's stamp".
  Its twin `hooks/dispatch.py:28` was rewritten.
- `docs/the-review-and-parity-arms.md:119`: "that is the sealer's stamp,
  which `straight to the PR` already owes".
- `docs/the-agent-set.md:113`: "the sealer's capture carries the work item
  id". The capture is now the orchestrator's `broad-gate.log`
  (`skills/code-review/orchestration.md:185`), and its pin was re-pointed
  there (`test_the_gates_capture_file_carries_the_work_item_id`).
- `agents/warden.md:144-145`: "what comes due is the sealer's spawn". Now the
  orchestrator's broad run comes due first, and the sealer's spawn after it.
  `tests/test_the_seal_is_taken_once_by_the_sealer.py:8310` pins the old
  words. The definition's other gate sentences (137-139) say nothing about
  who runs the gate and stand as they are.

Read: `git grep -n -F` of each fragment over `tests evals` finds a pin only
for the warden's sentence.

```text
templates/config.md:213-214
  and exits 2 with nothing run. It is a refusal rather than a prompt because
  the command runs unattended — the orchestrator runs it with nothing else
  running, and asks nobody anything — and a

templates/config.md:223-225
  repository that runs `npm test`; a default of `true` seals everything.
  Nobody who runs the gate picks a command either — a row is a
  thing a person wrote, and what the gate's stamp covers is exactly that. What the

skills/verify/scripts/seal_stamp.py:864
        description="Print the broad gate's stamp — the letter a green run draws.",

docs/commit-review-gate-spec.md:44-45
  `stop` group says each pending record once as a `systemMessage`, before the
  broad gate's stamp where there is one, and nothing the report adds carries a

docs/the-review-and-parity-arms.md:119
  a base — and that is the broad run's stamp, which `straight to the PR` already

docs/the-agent-set.md:113
  with every probe of the round beside it, the orchestrator's broad-gate log carries the

agents/warden.md:144-145
  conversation. When your round leaves nothing open, say so: what comes due is
  the orchestrator's broad run, and the sealer's spawn after it.

tests/test_the_seal_is_taken_once_by_the_sealer.py:8310
    assert "what comes due is the orchestrator's broad run" in warden, (
```

answer: 2d0babf9 rewrites the seven sentences to the fact (the orchestrator runs `broad-gate --record`; the stamp is the broad gate's, drawn from that run) and re-points the warden's pin, which went red under `mutation-check` restoring the old sentence. The wider grep `git grep -n -i -E "sealer'?s? (stamp|capture|log|spawn|run|broad)|broad.{0,30}(by|from) the sealer"` outside `seal/specs/` and `changelog/` found three more present-tense sites, all test text, rewritten in the same commit: the `seal-stamp` row of `tests/test_a_reference_root_is_read_and_never_taken.py:192`, the A12 docstring of `tests/test_the_gate_asks_the_range_ci_will_ask.py:403` and the module docstring of `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:1-7`; its other hits are past-tense history (`docs/the-broad-gate.md:96, 124`, `tests/test_evals_layout.py:341`, the 1790562543 section heading at `tests/test_the_seal_is_taken_once_by_the_sealer.py:2906`) or the sealer re-running its audit (`docs/the-review-record.md:246`, `chain_check.py:1647, 1677`), which stand. Left to #967 and #968, found by `git grep -n -i -w sealer`: `agents/framer.md:24`, `agents/smith.md:219, 299, 305`, `skills/verify/SKILL.md:242, 250, 253`. `overview.md`'s Not done names the warden's moved read set for the milestone close.

### 3. The sealer's step 1 counts commits the base brought in, and the check it cites does not

severity: should
location: `agents/sealer.md:46-54`, `tests/test_the_sealer_guarantees.py`
verdict: fixed 6366ee46

Read, both directions. Step 1 runs `git -C <root> log --name-only <named>..HEAD`
and withholds on any path outside `seal/specs/<item>/`. The rule it cites is
applied by `chain_check.py#broad_gate`, through `follows`, which walks
`rev-list --reverse --no-merges HEAD ^<run> ^<base>` (`chain_check.py:1398-1400`).
Three readings of the same branch:

- Record at HEAD: `<named>..HEAD` is empty, so step 1 goes on and the check
  passes. They agree.
- Record followed only by commits under the item's directory, the common case
  after `broad-gate.md` is committed: both pass. They agree.
- Record followed by a code commit on the branch: both refuse. They agree.

They part when the base is merged into the branch after the run (the
release's practice: merge the release branch in, never rebase). The base's
own commits show up in `<named>..HEAD` with their paths, so the sealer writes
`withheld — no broad run at HEAD`. The check excludes them with `^<base>`
and passes the same record. The cost is a second broad run that the check
never asked for. The definition also says nothing about a commit git cannot
resolve, or one HEAD does not descend from, which `follows` names as
`unseen` and `off`. One rule has two readings here, and the definition
should take the check's.

```markdown
1. **Read the gate's record.** Open `broad-gate.md` in the work item's
   directory, take its newest run's commit, and run
   `git -C <root> log --no-merges --name-only <named>..HEAD ^<base>`;
   `docs/the-review-record.md` §*The broad run has one home* is the rule it
   applies, as `chain_check.py#follows` reads it.
   - **At HEAD, or followed only by paths under `seal/specs/<item>/`**: go
     on.
   - **Absent, a commit git cannot resolve or HEAD does not descend from,
     or followed by any other path**: write `guarantee.md` with
     `Verdict: withheld — no broad run at HEAD`, naming the commit and the
     path where one follows, and return. Nothing broad is run in its place.
```

answer: 6366ee46: step 1 runs `git -C <root> log --no-merges --name-only <named>..HEAD ^<base>` with `<base>` the plain branch name the prompt names, cites `chain_check.py#follows`, and withholds on a commit that does not resolve or is not an ancestor of HEAD. `test_step_1_reads_the_record_and_runs_nothing` pins both, and went red under `mutation-check` dropping `--no-merges` and dropping the ancestor clause.

### 4. The refusal of an old verdict word, and the changelog, order a full broad run where spawning the sealer again is enough

severity: should
location: `skills/code-review/scripts/chain_check.py:91-96`, `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/changelog.md:35-39`, `tests/test_the_sealer_guarantees.py:295-297`
verdict: fixed 8313e330

Read. A work item in flight at the update carries the pair the old sealer
wrote: `broad-gate.md` at the commit it audited, and `guarantee.md` reading
`sound`, committed together just after. The new sealer's step 1 reads that
`broad-gate.md`. Its run is followed only by the records commit under the
item's directory, so step 1 goes on, and so does `chain_check.py#broad_gate`.
Re-spawning the sealer at HEAD writes the verdict in the new words over the
same audited code. `RETIRED_SAYS` and the changelog paragraph tell the user
to run `broad-gate --base <base> --record <item>` first anyway. That is the
full suite, lint and typecheck (nine minutes on this repository's last
measured run) spent to rewrite one word, against "broad once". A broad run
is owed only where `broad-gate.md` does not stand at HEAD, which the
sealer's own step 1 already reports as `withheld — no broad run at HEAD`.
The pin at `tests/test_the_sealer_guarantees.py:295-297` asserts both
phrases, so it moves with the message (§14).

```python
RETIRED_SAYS = (
    "is a word the verdict no longer uses: it reads `sealed`, "
    "`withheld — <reason>` or `undecided — <question>` now: spawn the "
    "sealer again at HEAD, and where `broad-gate.md` names no run at HEAD, "
    "run `broad-gate --base <base> --record <item>` and commit it first"
)
```

```markdown
  line says the word changed. If a work item of yours is in flight with a
  `guarantee.md` reading `sound` when you update, do not edit the word:
  spawn the sealer again at HEAD, which reads the `broad-gate.md` already
  committed. Where that record names no run at HEAD, run `broad-gate --base
  <base> --record <item>` and commit `broad-gate.md` first, so the verdict
  is written in the new words over the code it audited.
```

answer: 8313e330: `RETIRED_SAYS` now says the committed `broad-gate.md` still stands, to spawn the sealer again at HEAD, which writes the new word, and to run `broad-gate --base <base> --record <item>` first only where `broad-gate.md` does not stand at HEAD; the changelog paragraph says the same, and `test_the_old_words_are_refused_by_line` pins the three phrases, seen red against the old message before it changed.

### 5. A broad-gate record followed by a code commit, the stale half of step 1, is held by no case

severity: should
location: `evals/scripts/rule_cases.py:561-579`, `evals/scripts/rule_cases.py:641-650`, `evals/behaviour/sealer/rule-sealer-stale-gate`, `agents/sealer.md`, `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/phases/phase-6.md`
verdict: fixed 71f3e739

S3 promises a withheld verdict for "no `broad-gate.md`, or one whose newest
run is followed by a commit outside the item's records". Read:
`rule-sealer-no-gate` scaffolds the first state only (`gate` False writes
no record). `test_step_1_reads_the_record_and_runs_nothing` pins the
sentence. Neither puts a sealer in front of a record that exists and is
stale. That is the branch where a sealer reads a well-formed record, sees a
SHA, and seals without running `git log`. S1's grader cannot see it either,
because such a sealer runs nothing broad. The four sides all ran without this
case, so no measurement says the definition holds on it. A new case changes
the suite tree and needs its own baseline, so this fix carries a paid run.
That cost is the reason to decide it here and not leave it to chance.

```python
    ("no-gate", True, "", "withheld", r"^Verdict:.*no broad run", False),
    ("stale-gate", True, "", "withheld", r"^Verdict:.*no broad run", "stale"),
)
```

```python
    if gate == "stale":
        lines += [
            "printf '\\n' >> src/textutil.py",
            "git add -A",
            f"{BY} 'fix: a code commit after the broad run'",
        ]
```

The truth grader's description is chosen by `if gate`, and `"stale"` is
truthy. In the `report_regex` call write
`if gate is True else "The verdict says no broad run is on record at HEAD."`.

answer: 71f3e739 adds `rule-sealer-stale-gate` to `SEALER_RUNS` (a `broad-gate.md`, then a code commit to `src/textutil.py`; verdict `withheld`, truth `^Verdict:.*no broad run`), with the truth grader's text chosen from a `SEALER_TRUTH` table by GATE; the regenerated `evals/behaviour/sealer/` is copied in (`diff -r` 0), the step-1 rule's `Enforced by:` names the case, and `phases/phase-6.md` says the reference is re-run on the five-case suite after round 1. `test_the_sealer_cases_are_the_generators_output` was red before the copy. No paid side was run here.

### 6. `noninferiority.py model` prints `sonnet` for a record that carries no truth grader

severity: should
location: `evals/scripts/noninferiority.py:912-934`, `tests/test_a_rewritten_definition_proved_non_inferior.py`
verdict: fixed 126219d3

The docstring and S7 decide the model "by every truth grader". Executed:
`cheaper_model` over numbers with `graders={}` returned `('sonnet', 'every
grader holds and Sonnet spent 1.0 USD, below 2.0')`, and with one shape
grader and no truth grader it returned the same. A record with no
`## Graders` rows parses (`parse_record` reads an empty table), and
`read_record` passes it whenever its stated verdict matches what rules 4 and
5 give. So `model` exits 0 with `sonnet` on a record that measured no
outcome. That is a decision made by cost alone, the defect S7 names. The
committed `evals/sealer-model.md` carries 27 graders and is unaffected
(`model` prints `opus` on it, executed). The gap is in the function that the
next model decision will read.

```python
    result, reasons = verdict(numbers)
    if result == "no result":
        return "opus", "; ".join(reasons)
    if not any(v[0] == "truth" for v in numbers["graders"].values()):
        return "opus", "the record carries no truth grader, so no outcome was measured"
```

A case for T7, seen red against the current function first:
`model_of(tmp_path, capsys, {("c1", "shape-commits-nothing"): ("shape", 2, 2)}, {("c1", "shape-commits-nothing"): ("shape", 2, 2)})`
asserting `(0, "opus")`.

answer: `cheaper_model` returns `opus` with "the record carries no truth grader, so no outcome was measured" where no truth grader is in the record (5f4e43cf, settled in 126219d3, cases completed in 3e5fe505). The decision's "either side" needs no branch of its own: a truth grader one side lacks counts zero runs there, so that side ran the case a different number of times and `verdict` already gives `no result`, hence `opus`; the case asserts that for each side alone. `test_a_record_with_no_truth_grader_decides_opus` (no graders, a lone shape grader, shape and reach) was red against the old function; `mutation-check` gave red for the branch removed and for the kind test widened to `!= "shape"`, the second only after 3e5fe505 added the reach case.

### 7. A committed eval record carries a machine path with the account name in it

severity: should
location: `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/evals/sealer-sonnet-phase-4.json:1163`, `evals/scripts/noninferiority.py:465`, `tests/test_a_rewritten_definition_proved_non_inferior.py`, `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/evals/sealer-model.md`
verdict: fixed b5a11876

Executed: a `git grep` for the scratchpad's path pieces over the item's
`evals/` finds one line. The Sonnet side's `specseal.rev` is the absolute
scratchpad path of the tree copy, under the machine's temporary directory,
carrying the session directory and the account name. The house rule
(`CONTRIBUTING.md` §*House rules*, `CLAUDE.md`) allows no real machine
path in a tracked file. `tests/test_no_real_identifiers.py` passes only
because its pattern looks for a path shaped like `/Users/x/`, and this path
spells its user directory with dashes (executed: the module is green). The cause is the generator:
`run_side` records `os.path.abspath(a.tree)` for every `--tree` side, so the
next model decision commits another one. `phases/phase-4.md` already writes
the path as `$P/sonnet-tree`.

```python
            "rev": a.rev or f"tree {os.path.basename(os.path.normpath(a.tree))}",
```

Then set `rev` to `tree sonnet-tree` in the kept raw side's `meta.json`
(`SpecSeal-worktrees/969-phase-4-raw/sealer-sonnet-phase-4/`), and rewrite
the record with `run --from-raw` and `compare` for `evals/sealer-model.md`.
No eval runs. The `New run` digest of `sealer-model.md` moves with the JSON.

answer: b5a11876: a `--tree` side writes `rev` as `tree` (`TREE_REV`), and `--from-raw` reads a saved absolute `rev` back as `tree`, so the kept raw side's `meta.json` was left untouched; the case in `test_a_paid_run_survives_a_later_crash_and_is_read_again_from_what_was_saved` was red first and both units went red under `mutation-check`. e7406985 re-derives `sealer-sonnet-phase-4.json` with `run --from-raw` and `sealer-model.md` with phase 4's `compare` (`New run` digest ff22d7855802 to 2ffff3f1e708); `check` exits 0 and 1, `model` prints `opus`. A grep for the account path finds nothing in the item's `evals/`; the 32 `tracePath` lines of the form `/private/tmp/e-XXXXXX/out/trace.jsonl` the eval itself writes into every side, here and in earlier items' records on the base, are left as they stand.

### 8. The Q4 answer counts 90 Sonnet assistant events, and the traces hold 79, 60 of them the sealer's

severity: should
location: `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/phases/phase-4.md:62-64`, `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/questions.md:43`
verdict: fixed e7406985

Executed over the kept traces, `SpecSeal-worktrees/969-phase-4-raw/sealer-sonnet-phase-4/traces/`:
79 events of type `assistant`, every one naming `claude-sonnet-5-5`. 60
carry a `parent_tool_use_id` (the sealer subagent) and 19 do not (the case
session). 109 lines contain the string `claude-sonnet-5-5`. No count gives
90. The answer still holds: the Opus side's 73 subagent events all name
`claude-opus-5-5`, and none on the Sonnet side does. The count as written
also mixes in the case session, which runs on Sonnet because `case.yaml`
says `claude-sonnet-5-5`, so it cannot show what Q4 asks. The 60 subagent
events can.

```markdown
- Q4: the Sonnet side's traces hold 79 assistant events, all naming
  `claude-sonnet-5-5`: 60 are the sealer's (each with a `parent_tool_use_id`)
  and 19 the case session's, which runs on Sonnet by `case.yaml`. The Opus
  side's 73 sealer events all name `claude-opus-5-5`. So `run --tree`
  honoured the copy's `model: sonnet`.
```

In `questions.md:43`, write `answered 2026-10-18 by the work: the sealer's
60 events on Sonnet, none on Opus (phases/phase-4.md)` in place of `90 Sonnet
events, no Opus`.

answer: e7406985: recounted from the kept traces (every `traces/*.jsonl` line parsed, `type` `assistant`, by `message.model` and `parent_tool_use_id`): Sonnet side 79 events, 60 the sealer's and 19 the session's, all `claude-sonnet-5-5`; Opus side 73 sealer events on `claude-opus-5-5` and 17 session events on Sonnet, 90 in all, which is where the old figure came from. `phases/phase-4.md` and `questions.md` Q4 carry the figure and the counting rule; the conclusion holds.

## Confirmations

confirms: none
Every figure of the changelog table and its prose holds. Executed:
`side_numbers` over the four committed sides gives spend 3.1901, 2.8036,
1.4076 and 2.9882, and tokens per call 35,490.9, 33,386.8, 34,719.4 and
34,849.8. Preload bytes are 24,652, 23,792, 23,794 and 23,825. Graders
passed are 39, 54, 53 and 54 of 54. Each side is 8 runs and none was cut
short. The step-A suite is c2544c8f and the reference suite b394e929. The
reference's `agents/sealer.md` hash, 8f381411, is HEAD's, and the contract's
hash 642b0da6 is HEAD's too, so the reference measured the definition this
branch ships.

confirms: none
The records reproduce from the kept raw output. Executed: `run --from-raw`
of all four raw sides into scratch gives files byte-identical to the
committed JSONs (`cmp` 0 each). `compare` of baseline against phase 4, and
of phase 4 against the Sonnet copy, gives records identical to
`sealer-phase-4.md` and `sealer-model.md` (`diff` 0). `check` gives 0 on the
first and 1 on the second. `model` gives 0 and `opus`, with the reason
`rule-sealer-sound/shape-verdict passed 1/2 on Sonnet, 2/2 on Opus`.

confirms: none
`cheaper_model` fails closed where the docstring says it does. Read and
executed: a cut-short side returns `opus` through `verdict`'s `no result`. A
missing spend returns `opus`. A grader the Sonnet side passes less often
returns `opus`, whatever its kind. `model` exits 2 only on an unreadable or
unparsable record, two suites, or a stated verdict its numbers do not give,
which is what the module docstring lists. Finding 6 is the one vacuous case.

confirms: none
The verdict rename reaches every reader. Executed:
`git grep -w -n -E "sound|undecidable"` outside `seal/specs/` and
`changelog/` finds the 8 lines phase 5 left. Four are the plain adjective
and read right: `seal/follow-up.md:45`,
`tests/test_a_document_that_names_a_script_says_how_to_reach_it.py:71, 169`
and `tests/test_a_moved_rule_leaves_its_definition.py:335`. The other four
are `RETIRED_VERDICTS` and its test. A case-insensitive sweep adds only
`unsound` in `noninferiority.py` docstrings, which is the adjective too.
`verdict_word` maps `sound`, `not sound — …` and `undecidable` to the
retired branch, which names the line (`chain_check.py:1659-1668`).

confirms: none
The orchestration's order stands as `spec.md` §*The act* orders it. Read at
`skills/code-review/orchestration.md:178-223`: preflight, then
`broad-gate --record` with nothing else running and the log at
`<scratchpad>/<work-item-id>/broad-gate.log`, then a commit of
`broad-gate.md`, then the sealer's spawn. The base is passed as a plain
branch name, the gate's three only-it-can-tell lines are quoted, and the
stamp is drawn at the orchestrator's own turn end. `skills/implement/orchestration.md:40`
carries the same order.

## Not judged

| What | Location | Who answers |
|---|---|---|
| `agents/smith.md:305`, *When the sealer reports a failure*, is a third site of the class in the smith's file. `phases/phase-3.md` hands only lines 219 and 299 to #967 | `agents/smith.md:305` | the orchestrator, when it hands #967 its list |
| `skills/verify/SKILL.md:253`, *The sealer's is the only one drawn*, left to #967 by `overview.md`, while this diff edited line 258 of the same bullet | `skills/verify/SKILL.md:253-259` | #967 |
| `agents/framer.md:24` still says the sealer runs the broad gate, left to #968 by design | `agents/framer.md:24` | #968 |
| Phase 7 ran 65 test modules, 4290 tests, before the review. Whether that was a narrow run or most of the broad one under §2 | `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/phases/phase-7.md` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck at 73d0d409: `unverified` here | the branch | the orchestrator, by `broad-gate --record` once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the branch worktree into `<scratch>/round-1/clone`, checkout 73d0d409 | 0, 0 |
| `bin/test` over `test_no_real_identifiers`, `test_the_sealer_guarantees`, `test_broad_gate_rule`, `test_a_rewritten_definition_proved_non_inferior`, `test_chain_check`, `test_evals_layout`, `test_the_seal_is_taken_once_by_the_sealer`, `test_one_word_one_meaning` `-q` in the clone | 0, 594 passed |
| `bin/rules --check --root <clone>` | 0 |
| `noninferiority.py run --from-raw` of the four kept raw sides into `<scratch>/re/`, then `cmp` against the committed JSONs | 0 each; `cmp` 0 each |
| `noninferiority.py compare` of baseline against phase 4, and phase 4 against the Sonnet copy, then `diff` against the committed records | 0, 0; `diff` 0, 0 |
| `noninferiority.py check` on `sealer-phase-4.md` and `sealer-model.md`; `model` on `sealer-model.md`, committed and rebuilt | 0, 1; 0 `opus` |
| `side_numbers` over the four committed JSONs, `python3 -I -c` | the figures of the first confirmation |
| `cheaper_model` over no graders, a shape grader alone, and a truth grader with no Sonnet runs, `python3 -I -c` | `sonnet`, `sonnet`, `opus` (no result) |
| `blocked by sandbox` over the Opus side's 8 traces | 6 of 8, as Q3 says |
| assistant events by model and `parent_tool_use_id` over both phase-4 sides' traces | Opus side 73 subagent `claude-opus-5-5` and 17 session `claude-sonnet-5-5`; Sonnet side 60 subagent and 19 session, all `claude-sonnet-5-5` |
| `git grep -n -i -w sealer`, and the class grep of `spec.md`, over the paths outside `tests/` and `seal/specs/` | the seven sites of finding 2, plus `agents/smith.md`, `agents/framer.md` and past-tense history |
| `git grep -w -n -E "sound\|undecidable"` and `-i` over the tree outside `seal/specs/` and `changelog/` | 8 lines; `unsound` three times in `noninferiority.py` |

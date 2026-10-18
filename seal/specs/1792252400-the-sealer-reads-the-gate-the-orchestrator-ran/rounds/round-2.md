# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — review round 2

target: a380dcb7, fixes 884b7044..a380dcb7

## Findings

### 1. The sealer's step 1 now fails with `bad revision` in this repository's own worktree, because `<base>` is a local branch git cannot find

severity: must
location: `agents/sealer.md:36-38`, `agents/sealer.md:46-58`, `agents/sealer.md:111`, `tests/test_the_sealer_guarantees.py:331-347`
verdict: fixed e15490c5
regression: round-1#3

The unit is step 1's command, `git -C <root> log --no-merges --name-only
<named>..HEAD ^<base>`, "with `<base>` the plain branch name the prompt
names", which 6366ee46 wrote. The frame (`spec.md` §*The act, as this item
leaves it*, lines 181-187, and `plan.md` row 3) gives step 1 as `git log
--name-only <sha>..HEAD` with no base at all; round 1's finding asked for the
check's reading, `^<base>`; the fix departed from the frame as asked and
defined `<base>` as the plain branch name, which is the spelling
`broad-gate --base` takes because the gate resolves it
(`skills/verify/scripts/broad_gate.py#resolve_base`), but `git log` resolves
nothing, so the defect came from how the fix was written, not from the frame.

Executed, in the branch worktree under review, read-only:
`git log --no-merges --name-only 884b7044..HEAD ^release/v0.22.1` exits 128
with `fatal: bad revision '^release/v0.22.1'`. The worktree has no local
`release/v0.22.1` (`rev-parse --verify --quiet` exits 1); only
`origin/release/v0.22.1` exists, and the same command with `^origin/release/v0.22.1`
exits 0.

Read: `skills/verify/SKILL.md:421` says "A plain branch name is a LOCAL ref",
and `skills/code-review/orchestration.md:202-205` tells the orchestrator to
pass the base as a plain branch name because the gate resolves it to the
base's upstream, else `origin/<base>`. `chain_check.py#follows` is handed
`--baseline origin/<base_ref>` by CI (`.github/workflows/hygiene.yml:156, 184`),
and `follows` writes `^{base}` with what it is handed. So the check reads
the remote-tracking ref and the sealer is told to read the local one.

Why it matters. In this repository's own flow (a worktree per work item, no
local release branch), every sealer spawn's first command fails. Step 1 has
no branch for an unresolvable base. A sealer that reads the error as "does
not resolve" writes `withheld — no broad run at HEAD`; the orchestrator
then runs the broad gate again, about nine minutes, and the next sealer
meets the same error. Where the local branch exists but is behind its
remote, the base's newer commits merged into the branch after the run are
not excluded, which is exactly round 1's finding 3 standing again. The eval
cases cannot see it: their base `main` is a local branch with no remote.

The same plain name stands in step 2's `git diff <base>...HEAD`
(`agents/sealer.md:59`) and in the at-base restore (`agents/sealer.md:111`),
both from before this branch. They are one class with step 1 (contract §12),
so the fix resolves `<base>` once, where the definition introduces it.

Cost the fix carries: `agents/sealer.md` changes, so the five-case reference
measured at 90fa7046 no longer measures the definition that ships (round 1
confirmed it did, by hash). Whether the reference is re-run or the record
says it measured the previous text is the orchestrator's call.

```markdown
You work in the clone the prompt names, at its HEAD, against the base it
names. The prompt names the base as a plain branch name, which is a local
ref and may be missing or behind its remote; resolve it once, the way
`broad-gate` does (`broad_gate.py#resolve_base`), to the first of
`<name>@{upstream}`, `origin/<name>` and `<name>` for which
`git -C <root> rev-parse --verify --quiet` answers. Every `<base>` below is
that commit; where none answers, write `guarantee.md` with
`Verdict: undecided — the base <name> resolves to no commit in this clone`
and return.
```

```markdown
1. **Read the gate's record.** Open `broad-gate.md` in the work item's
   directory, take its newest run's commit, and run
   `git -C <root> log --no-merges --name-only <named>..HEAD ^<base>`;
   `docs/the-review-record.md` §*The broad run has one home* is the rule it
   applies, as `chain_check.py#follows` reads it.
```

```python
        assert "log --no-merges --name-only <named>..HEAD ^<base>" in step, step
        intro = " ".join(between(SEALER, "You work in the clone", "## Order of work").split())
        assert "`broad_gate.py#resolve_base`" in intro, intro
        assert "`<name>@{upstream}`, `origin/<name>` and `<name>`" in intro, intro
        assert "the plain branch name the prompt names" not in step, step
```

answer: e15490c5 resolves the base once, in the paragraph before the steps, citing `broad_gate.py#resolve_base`: the first of `<name>@{upstream}`, `origin/<name>` and `<name>` that `git -C <root> rev-parse --verify --quiet` answers is every `<base>` below (step 1's range, step 2's diff, the at-base restore), and none answering is `undecided — the base <name> resolves to no commit here`; step 1 drops "the plain branch name the prompt names". Probed read-only in the worktree: `release/v0.22.1@{upstream}` 1, `origin/release/v0.22.1` 0, `release/v0.22.1` 1, and `git log --no-merges --name-only 884b7044..HEAD ^origin/release/v0.22.1` 0. `test_step_1_reads_the_record_and_runs_nothing` holds the sentence, its three parts and the old words' absence; `mutation-check` gave red for each of four breaks. The reference measured the earlier text; `phases/phase-6.md` says it is re-run after this fix, and `overview.md` records the departure (a94ebe23).

### 2. The old-word refusal says the committed `broad-gate.md` "still stands" before it knows, beside the check's own line saying it does not

severity: should
location: `skills/code-review/scripts/chain_check.py:91-97`, `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/changelog.md:36-41`, `tests/test_the_sealer_guarantees.py:276-303`
verdict: fixed e15490c5
regression: round-1#4

The unit is `RETIRED_SAYS` as 8313e330 rewrote it, and the changelog
paragraph beside it. The frame (`plan.md:120-127`, *Operational impact*)
orders the release note to run `broad-gate --record` first and then spawn
the sealer; round 1's finding made the run conditional, and its paste-ready
text said only the condition; the fix also wrote an unconditional
"The committed `broad-gate.md` still stands", so the defect came from how
the fix was written.

Read. `RETIRED_SAYS` is printed by `chain_check.py#guarantee`
(`chain_check.py:1667`) for any `guarantee.md` reading `sound`, whatever the
state of `broad-gate.md`. `chain_check.py#broad_gate` runs in the same pass
(`chain_check.py:1866-1867`) and, for an in-flight item with a code commit
after the old run, prints "the newest broad-gate run is behind HEAD". The
person then reads one line saying the record stands and another saying it
does not. The action the message gives is right; the assertion in front of
it is a fact the function never read. The changelog paragraph asserts the
same thing to a plugin user (contract §14: a message a person acts on is
pinned and says only what holds).

```python
RETIRED_SAYS = (
    "is a word the verdict no longer uses: it reads `sealed`, "
    "`withheld — <reason>` or `undecided — <question>` now. Spawn the "
    "sealer again at HEAD, which writes the new word over the committed "
    "`broad-gate.md`; where this check also refuses `broad-gate.md`, run "
    "`broad-gate --base <base> --record <item>` and commit it first"
)
```

```python
        assert "Spawn the sealer again at HEAD, which writes the new word" in line, line
        assert (
            "where this check also refuses `broad-gate.md`, run "
            "`broad-gate --base <base> --record <item>` and commit it first"
        ) in line, line
        assert "still stands" not in line, line
```

```markdown
  `guarantee.md` reading `sound` when you update, do not edit the word:
  spawn the sealer again at HEAD, which reads the `broad-gate.md` already
  committed and writes the verdict in the new words over the code it
  audited. Where the check also refuses `broad-gate.md` as behind HEAD, run
  `broad-gate --base <base> --record <item>` and commit `broad-gate.md`
  first.
```

The four test lines replace the assertions at
`tests/test_the_sealer_guarantees.py:298-303`, and the docstring at 278-281
moves with them.

answer: e15490c5 states the remedy as a condition and asserts nothing about the record: "Where `broad-gate.md` names a run at HEAD, or one followed only by the work item's records, spawn the sealer again at HEAD, which writes the new word; otherwise run `broad-gate --base <base> --record <item>` and commit `broad-gate.md` first", and `changelog.md` says the same. `test_the_old_words_are_refused_by_line` asserts both halves and "still stands" absent, its docstring moved with it; `mutation-check` gave red for "still stands" put back, the condition dropped and the condition widened.

### 3. Two tests still say the sealer owns the broad run, and one no longer pins the owner at all

severity: should
location: `tests/test_the_suite_has_a_command_that_is_cheap_twice.py:1222-1243`, `tests/test_broad_gate_rule.py:397-400`, `tests/test_the_seal_is_taken_once_by_the_sealer.py:3231`, `tests/test_the_seal_is_taken_once_by_the_sealer.py:3790`, `tests/test_the_gate_names_every_step_ci_runs.py:1030`
verdict: fixed 2076c4d6
reopens: round-1#2

Round 1's finding 2 named the class: present-tense sentences that give the
broad run, its stamp or its log to the sealer. 2d0babf9 rewrote the seven
it named and three more its wider grep found. Two members of the class
stand, in units the build phases made, so the close does not hold for the
class (contract §12).

Read:

- `tests/test_the_suite_has_a_command_that_is_cheap_twice.py:1222`: the test
  is named `test_the_section_says_the_full_run_is_the_sealers`, its docstring
  says "who it is for is the `sealer` now", and it asserts
  `"agent-contract" in section and "sealer" in section` over `CONTRIBUTING.md`
  §*Running the checks*. That section now reads "The full suite is the
  orchestrator's, run once after the review rounds settle and before the
  sealer is spawned". The assertion passes only through "before the sealer is
  spawned", so a revert to "The full suite is the sealer's" passes it too:
  the pin no longer holds whose the run is.
- `tests/test_broad_gate_rule.py:399-400`: the docstring of
  `test_the_acts_table_row_names_the_preflight_and_stays_a_sentence` says a
  session that skips the preflight loses time "because the sealer asks the
  same arms". The row it pins, `skills/implement/orchestration.md:639`, now
  says "the broad run asks the same arms".

Executed: `git grep -n -i -E` for the sealer beside arm, suite, stamp, lint,
typecheck, preflight, broad or the gate, outside `seal/specs/`,
`changelog/`, `evals/behaviour/` and the three files left to #967 and #968.
Every other hit is the sealer reading or re-running its audit, past-tense
history, a hook or test name for the stamp, or
`tests/test_the_seal_is_taken_once_by_the_sealer.py:8322`, which pins
`agents/smith.md` and is #967's.

```python
def test_the_section_says_the_full_run_is_the_orchestrators():
    """`bin/test` with no arguments runs the whole suite, which
    §2 forbids to every agent. The section that makes it cheap is the
    section that has to say who it is for, and name the form a segment
    types.

    Re-pointed by #30 to the `sealer`, and by #969 to the orchestrator,
    which takes the run before it spawns the sealer. The owner is read from
    its own sentence: the word `sealer` alone also matches the section's
    *before the sealer is spawned*, so it held nothing."""
    section = " ".join(running_the_checks().split())
    assert "agent-contract" in section, (
        "the section makes the full suite cheap and says nothing about the "
        "rule that forbids it to a segment"
    )
    assert "The full suite is the orchestrator's" in section, (
        "the section no longer says whose the full suite is"
    )
    assert "bin/test tests/" in section, (
        "no narrow form is shown, so the only command a segment can copy is "
        "the one it must not run"
    )
```

```python
    """S8's other half. The row for that section keeps `still a sentence` —
    a session that skips the preflight loses time and nothing else, because
    the broad run asks the same arms — and its grounds name the step."""
```

answer: 2076c4d6 renames the case `test_the_section_says_the_full_run_is_the_orchestrators` and asserts "The full suite is the orchestrator's" (`mutation-check` red with "the sealer's" put back), and fixes the `test_broad_gate_rule.py` docstring to "the broad run asks the same arms". The class grep `git grep -n -i -P "sealer'?s?\b.{0,40}(broad|gate|stamp|capture|log|arms)"` (the `-E` form matches nothing: `\b` is not ERE) gave 93 lines outside `seal/specs/` and `changelog/` before the fix and 93 after it (the rewritten lines still say "gate"), and a second with `relay`, `passes`, `suite`, `lint`, `typecheck`, `preflight` gave 8 before and 5 after. Three more present-tense sites, appended to `location:` and rewritten in the same commit: the docstring at `tests/test_the_seal_is_taken_once_by_the_sealer.py:3231` and the comment at `:3790` ("the sealer passes/relays the gate's lines"), and the docstring at `tests/test_the_gate_names_every_step_ci_runs.py:1030`; since #969 the sealer sees no output of the gate's. Every other hit is a `.test_durations` key or test name, the `sealer-stamp` hook, the sealer reading a record, past-tense history (`docs/the-agent-set.md:111`, `docs/the-broad-gate.md:122, 124`, `tests/test_evals_layout.py:123, 341`, `tests/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:6`, the fixture text of `tests/test_a_process_record_drop_passes_the_readers.py:58, 62`), or the orchestrator's run before the spawn. Left to #967 and #968: `agents/smith.md:299`, `agents/framer.md:24`, `tests/test_the_seal_is_taken_once_by_the_sealer.py:8322` (8323 after this commit's comment line), and `skills/verify/SKILL.md`, which this grep does not hit.

### 4. The closing memo records none of round 1's three departures from the frame

severity: should
location: `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/overview.md:12-23`
verdict: fixed a94ebe23
regression: round-1

The unit is `overview.md`'s table *Where spec and implementation diverged*,
which a380dcb7 edited (the reference side's row) and which no finding of
round 1 named. The frame says three things the fixed tree now does
otherwise: `spec.md:181-187` gives step 1 as `git log --name-only <sha>..HEAD`
(the tree: `--no-merges … ^<base>`, from round 1's finding 3);
`plan.md:120-127` orders the release note to run `broad-gate --record` first
(the changelog: run it only where the record does not stand, finding 4);
`spec.md:202`, S3, is verified by "the fourth sealer case
`rule-sealer-no-gate`" (a fifth case, `rule-sealer-stale-gate`, now holds
the stale half, finding 5). The fixes departed from the frame on round 1's
word, and the defect is that the memo the sealer reads in step 2 says
nothing of it, which came from how the fix pass was written up.

Why it matters. The sealer's step 4 sets the spec against the build and
names where they disagree. Each of the three is a disagreement with its
grounds only in `rounds/round-1.md`, and the table is where this item puts
every other one, the phase-6 reference row among them. `plan.md:127` itself
holds as it stands: it is the framer's approved text, and the departure
belongs in this table rather than in an edit to the frame.

```markdown
| The sealer's step 1 command (round 1) | `spec.md` §*The act, as this item leaves it*: `git log --name-only <sha>..HEAD` | `git log --no-merges --name-only <named>..HEAD ^<base>`, withholding on a commit that does not resolve or HEAD does not descend from (6366ee46) | round 1's finding 3: the plan's range counts the base's commits merged in after the run, which `chain_check.py#follows` excludes with `--no-merges` and `^<base>` (`rounds/round-1.md`) |
| The in-flight remedy for a `guarantee.md` reading `sound` (round 1) | `plan.md` *Operational impact*: run `broad-gate --record`, commit, then spawn the sealer | spawn the sealer again at HEAD, and run the broad gate first only where `broad-gate.md` does not stand at HEAD, in `RETIRED_SAYS` and `changelog.md` (8313e330) | round 1's finding 4: the record the old sealer committed is followed only by records, so a second broad run buys one word (`rounds/round-1.md`) |
| S3's case (round 1) | `spec.md` S3 is verified by the fourth case, `rule-sealer-no-gate`, which scaffolds no record | a fifth case, `rule-sealer-stale-gate`, scaffolds a record a code commit follows (71f3e739); the reference was re-run on the five cases | round 1's finding 5: no case held the stale half of step 1 (`rounds/round-1.md`, `phases/phase-6.md`) |
```

answer: a94ebe23 adds the three rows, the remedy's row worded for e15490c5's condition, and a fourth for this pass's base resolution, which departs from `spec.md` §*The act* (step 1 there names no base, and steps 2 to 5 stay as 0.22.0 left them).

## Confirmations

confirms: round-1#1
The rule *The guarantee covers HEAD* at `agents/sealer.md:127-135` now
exempts only "the closing records, `broad-gate.md` and `guarantee.md`",
which is `docs/the-review-record.md:251-253` and what
`chain_check.py#guarantee` passes to `follows` as `only=CLOSING_RECORDS`.
Executed: `TestDefinition::test_the_guarantee_rule_exempts_only_the_closing_records`
passes in the clone, and it asserts both the new words and the absence of
"work item's records". The `Enforced by:` line names it, and `bin/rules
--check` resolves every target.

confirms: round-1#5
`rule-sealer-stale-gate` is the sealed case's scaffold plus one code commit
to `src/textutil.py` after the record's commit (executed: `diff` of the two
scaffolds with the slug replaced shows those three lines and nothing else),
with its truth grader's text from `SEALER_TRUTH["stale"]`.
`test_the_sealer_cases_are_the_generators_output` passes in the clone, and
the step-1 rule's `Enforced by:` names the case. Executed over the kept
traces of the five-case reference (`969-phase-6b-raw/traces/006.jsonl` and
`007.jsonl`): both sealers ran the step-1 range and wrote `withheld — no
broad run at HEAD` naming the code commit and `src/textutil.py`. The case
has not been seen failing on a sealer that skips the range; see Not judged.

confirms: round-1#6
`cheaper_model` returns `opus` with "the record carries no truth grader, so
no outcome was measured" where no grader in the record is a truth grader
(`evals/scripts/noninferiority.py:931-932`), after `verdict`'s no result.
Executed: `test_a_record_with_no_truth_grader_decides_opus` passes (no
graders, a lone shape grader, shape and reach; and a truth grader on one side
alone, which comes back a no result naming "different number of times").
`model` on the committed `evals/sealer-model.md` still prints `opus`.

confirms: round-1#7
A `--tree` side records `rev` as `tree` (`noninferiority.py:471`), and
`annotate` reads an absolute saved `rev` back as `tree`
(`noninferiority.py:402`). Executed: `run --from-raw` of the kept
`969-phase-4-raw/sealer-sonnet-phase-4/` into scratch gives a file
byte-identical to the committed `evals/sealer-sonnet-phase-4.json`, whose
`rev` reads `tree`; `compare` of phase 4 against it gives a record identical
to `evals/sealer-model.md` (`New run` digest 2ffff3f1e708); `check` exits 1
and `model` prints `opus`. No account path is left in the item's `evals/`.

confirms: round-1#8
Executed over the kept phase-4 traces, every line parsed, `type`
`assistant`, counted by `message.model` and `parent_tool_use_id`: the
Sonnet side holds 60 sealer events and 19 session events, all
`claude-sonnet-5-5`; the Opus side 73 sealer events on `claude-opus-5-5` and
17 session events on Sonnet. `phases/phase-4.md:62-70` and `questions.md`
Q4 carry those figures.

confirms: none
The five-case reference reproduces and every figure quoted from it holds.
Executed: `run --from-raw` of `SpecSeal-worktrees/969-phase-6b-raw/` into
scratch is byte-identical to `evals/reference-sealer.json` (`cmp` 0), and so
are the other three sides from their kept raw output. `side_numbers` on it:
10 runs, none cut short, spend 3.0973 (3.0972808), 2,564,595 tokens over 73
calls, 35,131.4 per call, 423.1 seconds, preload 24,209 bytes, 68 of 68
graders (14, 14, 12, 14 and 14 by case), suite rev 90fa7046 and tree
5c3e8119. The four-case side it replaces: 2.9882, 395.1 seconds, 76 calls,
2,648,585 tokens, 23,825 bytes. The five sides sum to 13.4868. Those are the
figures of `phases/phase-6.md:48-73`, the changelog's reference row,
`overview.md`'s two edited cells and `questions.md` Q5. 90fa7046 and
a380dcb7 differ only in the item's records, so the reference measured the
`agents/sealer.md` at HEAD; finding 1 changes that.

confirms: none
The orchestrator's decision to leave the `tracePath` lines holds against
`CONTRIBUTING.md` §*House rules*. Read: the rule's classes are a real domain
and a real user path, inlined into an example, fixture or doc
(`CONTRIBUTING.md:283-288`, `tests/test_no_real_identifiers.py`). The 34
lines of the form `/private/tmp/e-XXXXXX/out/trace.jsonl` (8, 10, 8 and 8
across the four sides) are a random temporary directory the eval itself
writes, carry no account name, handle or domain, and stand in the same
shape in ten records of `1792126889-every-agent-is-written-anew-from-its-job`
on the base. `test_no_real_identifiers` passes in the clone. The `root`
and `path` fields are a different shape; see Not judged.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The four sides also carry `root` and `path` lines of the form `/private/var/folders/<hash>/T/specseal-eval-<random>/tree`, the platform's per-user temporary directory, written by the eval as the `tracePath` lines are, and the same shape stands in ten records of `1792126889-every-agent-is-written-anew-from-its-job` on the base. Whether the house rule reaches a measurement record the eval writes, rather than an example or fixture, is a decision about the rule | `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/evals/*.json:9, 17` | the owner |
| `rule-sealer-stale-gate` has not been seen failing on a sealer that skips step 1's range (contract §15); only the generator check was seen red. A side on a definition without the stale branch is a paid run | `evals/behaviour/sealer/rule-sealer-stale-gate/` | the orchestrator |
| Whether the five-case reference is re-run after finding 1 changes `agents/sealer.md`, or its record says it measured the earlier text | `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/evals/reference-sealer.json` | the orchestrator |
| `tests/test_the_seal_is_taken_once_by_the_sealer.py:8322` asserts "Then the sealer takes the broad gate once" in `agents/smith.md`, a site of finding 3's class in #967's file | `tests/test_the_seal_is_taken_once_by_the_sealer.py:8322` | #967 |
| The warden's read set moved with its one sentence at `agents/warden.md:144-145`; not re-measured here, by design | `agents/warden.md:144-145` | the milestone close |
| The full suite, the repository-wide lint and the typecheck at a380dcb7: `unverified` here | the branch | the orchestrator, by `broad-gate --record` once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the branch worktree into `<scratch>/round-2/clone`, checkout a380dcb7 | 0, 0 |
| `bin/test` over `test_the_sealer_guarantees`, `test_a_rewritten_definition_proved_non_inferior`, `test_the_seal_is_taken_once_by_the_sealer`, `test_broad_gate_rule`, `test_evals_layout`, `test_no_real_identifiers`, `test_one_word_one_meaning`, `test_a_reference_root_is_read_and_never_taken`, `test_the_gate_asks_the_range_ci_will_ask`, `test_the_stamp_reaches_the_person_it_is_drawn_for`, `test_docs_line_wrap`, `test_chain_check` `-q` in the clone | 0, 721 passed |
| `bin/rules --check --root <clone>` | 0, 467 targets in 60 rule files |
| `git log --no-merges --name-only 884b7044..HEAD ^release/v0.22.1` in the branch worktree | 128, `fatal: bad revision '^release/v0.22.1'` |
| the same with `^origin/release/v0.22.1`; `rev-parse --verify --quiet release/v0.22.1` | 0; 1 |
| `noninferiority.py run --from-raw` of the four kept raw sides into `<scratch>/round-2/re/`, `cmp` against the committed JSONs | 0 each; identical each |
| `noninferiority.py compare --agent sealer --phase 4` of phase 4 against the Sonnet side, against `sealer-model.md`; `check` and `model` on it | 0, identical; 1; 0 `opus` |
| `side_numbers` over the committed reference and the four-case reference at 884b7044 | the figures of the sixth confirmation |
| assistant events by `message.model` and `parent_tool_use_id` over both phase-4 sides' traces | Sonnet side 60 sealer and 19 session, all Sonnet; Opus side 73 sealer on Opus and 17 session on Sonnet |
| `Bash` commands and `Verdict:` lines of the two `rule-sealer-stale-gate` traces of the five-case reference | both ran the step-1 range and wrote `withheld — no broad run at HEAD` naming the code commit and `src/textutil.py` |
| `diff` of the stale-gate scaffold against the sealed and the no-gate scaffolds, slug replaced | only the stale commit's three lines; only the record and the stale commit |
| `git grep -n -i -E` for the sealer beside arm, suite, stamp, lint, typecheck, preflight, broad or the gate, outside `seal/specs/`, `changelog/`, `evals/behaviour/` and the #967 and #968 files | the two sites of finding 3, plus reading, history and #967's pin |
| `grep` of the item's four side JSONs for machine paths | 34 `tracePath` lines; `root` and `path` under the per-user temporary directory in each |

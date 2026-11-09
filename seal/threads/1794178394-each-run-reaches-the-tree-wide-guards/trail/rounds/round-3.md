# Review round 3: 1794178394-each-run-reaches-the-tree-wide-guards

```seal
target: c959aa45 against release/v0.36.0
```

This is a verifying round. Its target is the branch at `c959aa45` against `release/v0.36.0` at `c7bb14ca`, which is still the merge base (executed: `git merge-base HEAD origin/release/v0.36.0`). Since round 2's target `84331b77`, five commits landed, and each touches only the work item's records (executed: `git diff --stat 84331b77 HEAD`):

- `18f2aca6` records round 2.
- `931639f2` is the orchestrator's fold of round 2's finding 2.
- `ca0d3909` is the fix pass for finding 1, and it changes `trail/phases/phase-2.md` and `gaps.md`.
- `3bddb268` appends round 2's close blocks.
- `c959aa45` is the orchestrator's fold of the fix pass into `frame/questions.md` Q2 and `frame/plan.md`.

The round read that diff whole. No code, test or document outside `seal/threads/` changed since round 2, so this round's review is bounded by records-only commits.

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` whole at `c959aa45`, then `trail/phases/phase-2.md` and rounds 1 and 2. It carried from round 2, without re-establishing them, the clean merge at `84331b77` and the reading of `CONTRIBUTING.md` beside #1444. The shipped readers of `.claude-plugin/plugin.json` were also carried, but this round checked their walk-up at each line it cites. It carried the six `pr.md` quotes too, since `pr.md` has not changed since round 2 (executed: `git diff 84331b77 HEAD -- '*/pr.md'` is empty).

## Findings

None. Both closes hold, and no sentence of the records that state the present is contradicted at `c959aa45`.

## Confirmations

```seal
confirms: round-2#1
```
What holds: `trail/phases/phase-2.md` part 3 now lists eight readers, and the teammate flow is the eighth (`phase-2.md:140-163`). The record builds the list from the shipped code that opens the manifest, walks up from there, and runs the test files under the audit hook, and it says the list is a sample over spellings (`phase-2.md:177-228`). `gaps.md:10` hands that limit to review as not verified. The fix differs from round 2's text in three places, which the close names: it keeps round 1's 97-file run as history, it explains why the case counts differ after the merge, and it adds the probes. None of the three changes what the finding asked for.

The round checked the walk-up at each line it cites. `seal.py#plugin_version` is called from `plugin_workflow`, `left_workflow_line`, `install_workflow` and `remove_workflow`. Those are reached only from `switch`, under `seal mode`, and from `pr_checks` (executed: an `awk` over the defining function of each call in `skills/implement/scripts/seal.py`). `release_seal.py:228-236` loads `broad_gate.py`, `release_report.py:59` and `:104` load `payload_meter.py`, and `seal.py:120`, `:152` and `:169` map `gate`, `payload` and `pr-body` (read). `roll_flow_measurement_issue.py:271` defines `read_version` and `tag_release.py:121` defines `version_at` (read).

The figures hold. Summed by file over `.test_durations` at HEAD, the 98 files are 525.6 s, the eight readers are 311.8 s and the teammate flow is 11.0 s (executed, a sum by file). `git diff --stat 69f00945 931639f2 -- tests/` shows five changed files in the two directories, and the three under `tests/text/` lose 33, 159 and 18 lines, 210 in all (executed). 33.96 s against 70.14 s is about half, as `phase-2.md:255` says. The 35-file walk list and the 21 files already probed are the fix pass's own executed claims. The round checked their arithmetic against rounds 1 and 2: 21 + 12 + 2 = 35. It did not rebuild the list, and `gaps.md:10` keeps the question open.

```seal
confirms: round-2#2
```
What holds: `frame/design.md:50`, `frame/design.md:54` and `frame/plan.md:46` read round 2's three replacements word for word, and `frame/plan.md:56` records the judgment (read, `git diff 84331b77 HEAD -- '*/frame/*'`). Each replacement holds at HEAD on the facts round 2 executed, and no file those facts stand on has changed since (executed: `git diff --stat 84331b77 HEAD` lists only records).

What matched: the fold `c959aa45`. `frame/questions.md:16` Q2 states 98 files and 33.96 s at `931639f2`. The chosen row of *Alternatives considered* (`frame/plan.md:23`) states 525.6 s plus 36.3 s, about 562 s. Both match `phase-2.md:230-269`. The chosen row's old 143.1 s was false after round 1's correction, and round 2 did not name it, so `frame/plan.md:57` names that miss. The 143.1 s that still stands at `frame/design.md:22` and `phase-2.md:261` is the *Grounding* row dated to `94d04d30`, so it states that commit (read).

What matched: the fix pass's run of the `Review rounds 1..n` set over its paths, `bin/test tests/text tests/behaviour -q`, which its close names. This round ran that set at `c959aa45` with the teammate flow added: exit 0, 1,796 passed and 8 skipped in 15.35 s (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `c959aa45`; `gaps.md:7` labels them `unverified`, and the label is honest, since no party claims a broad run | the branch at `c959aa45` | the orchestrator, at the broad gate |
| Whether a test file outside the two directories reads the manifest beyond the eight, by a spelling no search tried (`gaps.md:10`); this round re-checked the walk-up at its lines and did not rebuild the 35-file list | `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/gaps.md:10` | the sealer, who reads the row as a claim, since no reading short of running the suite under the hook makes the list whole |
| Whether the two timed runs of *Scope* item 7 compare like with like, since each is one run under the load of the release's other sessions (`phase-2.md:109-117`) | `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/trail/phases/phase-2.md` | the orchestrator, where it weighs done-when 2 |
| Where the glob clause came from, which the frame labels `unverified` as history | `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/frame/design.md:28` | the owner |

This round leaves nothing open. Next come the orchestrator's broad run and then the sealer's spawn.

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text tests/behaviour tests/e2e/teammate/test_teammate_flow.py -q` at `c959aa45` | exit 0, 1,796 passed and 8 skipped in 15.35 s |
| `python3 -c` sum by file of `.test_durations` over the 98-file set, the eight readers and the teammate flow | 98 files, 525.6 s; 311.8 s; 11.0 s |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.36.0 --root <the branch worktree> --worktree`, after this record | exit 0; it refused nothing in the round records and named only the gate record and the guarantee, which the broad run and the sealer write; it printed no notice at `frame/design.md` |

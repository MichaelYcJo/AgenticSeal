# Review round 1: 1793521562-the-proofer-cases-come-from-thread-records

```seal
target: 89cab72398ef413434a4e5000a015da755239e70 against release/v0.27.2
```

The diff is `813665f0..89cab723`. No earlier round exists, so no fact is carried from one. Every claim below was re-established in a `git clone --no-local` of the branch worktree at the target, with `origin` set to the GitHub URL and tags and `+refs/pull/*/head` fetched. One fact is carried from the frame without a check of its own: the 0.27.1 records in the working tree equal those at `v0.27.1` (`frame/design.md` *Grounding*, the `--case` row). The `--case` runs below rest on the tags, so nothing here depends on that fact. No `seal/parity.md` is declared, so the round block carries no `original:` line.

## Findings

### 1. In `seeded-55b66958`, the location line round 1 wrote for its real finding also passes the seeded truth, so a run that never sees the seed is scored as finding it

```seal
severity: should
location: `evals/behaviour/proofer/seeded-55b66958/graders/truth-seeded.md`, `evals/behaviour/proofer/seeded-bf9efcba/graders/truth-seeded.md`, `evals/scripts/seed_defects.py:155-189`, `evals/scripts/seed_defects.py:259`, `tests/evals/test_seed_defects.py`
evidence: executed `python3 -I - (each truth- grader of the four seeded cases searched over the unseeded round 1 record at its tag, git show v0.27.1:seal/threads/1793504229-a-linked-memo-named-as-the-argument/trail/rounds/round-1.md and the three others)`, `python3 -I - (each seeded line from scaffold.sh set against every path:line of every round 1 finding that is a truth)`
```

Why it matters: a seeded case measures whether the proofer finds a planted defect. In `seeded-55b66958` the seed is `skills/verify/scripts/unverified_check.py:1053`, inside `repository_of`, at target `ab958884`. Round 1's finding 1 is the case's `truth-1`. Its `location:` line names `` `skills/verify/scripts/unverified_check.py:1658` `` first and `` `skills/verify/scripts/unverified_check.py:1060-1086` `` fourth. `truth-seeded` accepts `unverified_check.py:1038` to `:1068`, so it matches `:1060`. I searched each grader's pattern over the round 1 record at `v0.27.1`, which reviewed the code before any seed. That one line matched both `truth-1` and `truth-seeded`. A proofer that reports the real defect the way round 1 did is credited with the seed as well. A rewritten proofer that misses the seed and finds the real defect then loses nothing on this case.

This goes against three statements in the tree:

- `evals/scripts/seed_defects.py:27`: "The seed lands on no line the window of such a finding accepts."
- `evals/README.md:131`: "no two truths of one case may accept the same `location:` line".
- `tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py:26-29`: "so one finding is never counted as two".

That test passes on this case because it builds rows of one coordinate each, from each pattern's own lines. It never tries a line that names several coordinates, which is how round 1 wrote this finding.

The cause is in the generator, which this diff runs and does not change. `seed_defects.py#seed` (`:155-189`) skips a line only where a truth's regex accepts `path:n`. `truth_pattern` builds each truth's regex from the first coordinate of its finding only (`evals/scripts/replay_targets.py:668-702`, `LOCATION.search`). So coordinates after the first never block a seed. I listed every case this cause can produce by taking each of the four seeded cases apart: its seeded line from `scaffold.sh`, set against every `path:line` of every round 1 finding that is a truth. Two of the four have their seed inside such a coordinate:

- `seeded-55b66958`, seed at `:1053`, within 15 lines of finding 1's `unverified_check.py:1060-1086`. Round 1's own line passes `truth-seeded` (executed).
- `seeded-bf9efcba`, seed at `unverified_check.py:1605`, inside finding 1's `unverified_check.py:1587-1652`, its second coordinate. Round 1's own line does not pass `truth-seeded`, because the range opens at `1587`, which is 18 lines from the seed (executed). The seed still sits in code the real finding names, which `seed_defects.py:27` rules out. A run that cites a line in that range for the real finding is credited with the seed.

`seeded-ea73e94f` and `seeded-5fd6b88c` have no seed near any coordinate of a truth (executed).

The crafter's contract rule 15 probe (`trail/phases/phase-1.md`, *Contract rule 15 for the generated cases*) showed each `truth-seeded` matching `location: <path>:<line>` and missing `<line>` plus or minus 16. It never searched a grader over the unseeded record, so it could not find this overlap.

The fix belongs in the generator. Then `seed_defects.py --count 4` runs again, which may move the seed in these two cases or pick another commit. `frame/design.md` *Scope* puts "a change to either generator" out of this work, so the orchestrator decides whether the fix lands here or in an issue of its own. If it moves to an issue, the two cases ship as they stand, and `gaps.md` names them. The change below blocks a seed within the window of any coordinate a truth's finding names, ranges included. Every name in it is in the tree (`rt.LOCATION`, `rt.WINDOW`, `t["truths"][i]["location"]`). It assumes nothing at an OS boundary.

```python
# evals/scripts/seed_defects.py
def seed(base, target, truths=(), locations=()):
    ...
    accepts = [re.compile(p, re.M) for p in truths]
    # Every coordinate a truth's finding names, not only the first one its
    # pattern is built from: a report that names the finding as round 1
    # wrote it must not also find the seed.
    named = []
    for value in locations:
        for m in rt.LOCATION.finditer(value):
            if m["line"]:
                last = re.search(r"[-\N{EN DASH}](\d+)`$", m[0])
                named.append((m["path"], int(m["line"]), int(last[1]) if last else int(m["line"])))
    ...
            window = range(line - rt.WINDOW, line + rt.WINDOW + 1)
            if any(
                a.search(f"location: `{path}:{n}`") for a in accepts for n in window
            ):
                continue
            if any(
                p == path and first - rt.WINDOW <= line <= end + rt.WINDOW
                for p, first, end in named
            ):
                continue
            ...

# in target_of, :259
    found = seed(
        t["base"], t["target"], patterns, [truth["location"] for truth in t["truths"]]
    )
```

A case pinning it belongs in `tests/evals/test_seed_defects.py`, beside `test_refuses_a_line_no_seed_may_take` (`:197`): a truth whose finding names `a.py:1`, then `a.py:40-60`, and a seed that would land on `a.py:45`, refused.

```seal
verdict: fixed bbf155e5
answer: Fixed at 87ebbc41, and the four seeded cases were written again at bbf155e5. `seed_defects.py#seed` takes the `location:` values of the truths' findings, and a new `named` gives the lines each coordinate covers: a line, a range to its last line, a unit's lines, or the whole file for a bare path. A seed is now refused within 15 lines of any of them, as well as where a truth's regex accepts its window, and `target_at` passes the values. I did not apply the paste-ready code as given. It parsed the range end with a second regex over the match, which `truths_with` already did on its own. Instead `replay_targets.py#LOCATION` gains a `last` group, and `truths_with` reads that group too, so the range grammar is spelt once. The paste-ready code also covered line and range coordinates only, and this fix covers units and bare paths as well. Two cases hold the fix. `Test_seed::test_keeps_the_seed_off_every_coordinate_a_truths_location_names` covers a range, an en-dash range, a line, a unit and a bare path, and was red against the old `seed()`. `Test_target_of::test_keeps_the_seed_off_a_later_coordinate_of_round_1s_finding` covers the wiring through `target_at`. `seal mutate` went red on each of the five new units: the span check, the range end, the unit span, the bare path and the wiring. The range-end mutation first SURVIVED, because the range in the case opened within the window, so the range now opens at `a.py:20`. Regenerated, `seeded-bf9efcba` takes no seed and leaves the suite. `seeded-55b66958`'s seed moves from `:1053` to `:1739`. `seeded-7a8899d5` joins. `seeded-ea73e94f` and `seeded-5fd6b88c` are byte for byte as before. In every seeded case, each `location:` line of a truth's finding, as round 1 wrote it, is accepted by its own grader alone, and no coordinate of a truth stands within 15 lines of the seed. In a fresh clone with the pull refs fetched, `--case` and `--count 4` each wrote these four cases, and `diff -r` against the committed cases is empty. `changelog.md` is updated at 555306a0.
```

## Confirmations

```seal
confirms: none
```
What matched: Scenario 1 and *Scope* item 1. `evals/behaviour/proofer/` at the target holds `rule-proofer-one-finding` and the eight new cases, and none of the old eight (executed: `ls`). `git grep` for the eight old names outside `seal/threads/` finds them only as data in `tests/evals/test_replay_targets.py:1041-1042` and `tests/evals/test_seed_defects.py:499-522`, and in two `.test_durations` keys (executed). That matches the crafter's account in `trail/phases/phase-1.md`, *What still names the old cases*.

```seal
confirms: none
```
What matched: Scenario 2 and *Scope* item 3. The crafter claimed that the eight cases are what `--count 4` writes and that `--case` regenerates them byte for byte. In the clone, `replay_targets.py --case` with the four replay names and `seed_defects.py --case` with the four seeded names each exited 0. `diff -r` of each written case against its committed directory exited 0, for all eight. `--count 4` with each generator also exited 0 and wrote the same eight names, and `diff -r` of that output against the committed suite exited 0 (executed). The names, truth counts and sizes match `frame/design.md` *Grounding* and the changelog fragment.

```seal
confirms: none
```
What matched: Scenario 3. Each of the eight new `scaffold.sh` files ran in its own empty directory under this round's scratch directory and exited 0. Each tree's `seal/README.md` opens with `# What AgenticSeal maintains in seal/`, which is `hooks/lib/optin.py:70`. No tree holds `seal/specs/`, and each holds its work item's `routing.md`. No tree holds the record the prompt names. The replay trees hold the earlier rounds the phase record lists: rounds 1 to 3 for r4, rounds 1 and 2 for r3, round 1 for each r2 (executed). One old case's target, `cdd0ce13` (`replay-1791779434-r5` at the base), holds `seal/specs/`, and its `seal/README.md` opens with `# seal/ — what this plugin maintains` (executed: `git show`, `git ls-tree`). So the changelog's account of what the old cases rebuilt holds.

```seal
confirms: none
```
What matched: Scenario 4 and *Scope* item 2. `evals/scripts/recurred_truths.json` holds one entry, for `rule-proofer-one-finding`. The diff removes the ten others and changes no other line (read: `git diff 813665f0..HEAD -- evals/scripts/recurred_truths.json`). The remaining entry still names `rule-warden` in its `from` rows (executed: `grep -c`, 4), so the file's place in `tests/censuses.py#OLD_NAME_RECORDS` still stands on that entry.

```seal
confirms: none
```
What matched: Scenario 5, through the runner. `bin/test -q` over `tests/evals/test_seed_defects.py`, `tests/evals/test_replay_targets.py`, `tests/evals/test_rule_cases.py`, `tests/behaviour/test_evals_layout.py`, `tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py`, `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` and `tests/test_censuses.py` gave 263 passed, exit 0 (executed). These modules are narrower than the crafter's phase-boundary set, and this round re-ran no other module. The set's passing does not answer finding 1, because `test_no_two_truths_of_a_proofer_case_accept_one_location` tries only one-coordinate rows.

```seal
confirms: none
```
What matched: the departure in `tests/evals/test_seed_defects.py:490-537`. The crafter claimed that the old case opened the committed suite through `OUT`. `evals/scripts/replay_targets.py:724-727` checks each entry's case against `OUT`, and the old case patched `TRUTHS` alone (read). The new case builds `proofer/` under `tmp_path` and patches `OUT` in both `rt` and `sd.rt`. `seed_defects.OUT` is a copy taken at import (`evals/scripts/seed_defects.py:73`), but `recurred_truths` reads `rt.OUT`, so patching `sd.rt` is the patch that counts (read). The crafter's `seal mutate` of `replay_targets.py`, with `for e in recurred_truths().get(case, []):` made `for e in []:`, gave `red: the cases failed against the mutation (exit 1)` again, at `tests/evals/test_seed_defects.py:517` (executed). I read the case against its group. `tests/evals/test_rule_cases.py:70-96` patches `TRUTHS` alone and leans on `rule-proofer-one-finding` being committed. `rule_cases.py` writes that case every time and `--count` never re-picks it, so the reason the crafter gave for this edit does not apply to that one. `seal layout --pairs` names no pair in `tests/evals/test_seed_defects.py`, whose `TARGET` is `evals/scripts/seed_defects.py` (executed). The case adds no coverage its group lacks, because it is the same case with its suite made its own.

```seal
confirms: none
```
What matched: *Scope* item 4 and Scenario 6. `git grep -n -E 'every committed case|four committed cases|lands #986 on' -- ':!seal/threads'` prints nothing (executed by the crafter). This round read the four rewrites at `evals/README.md:87-92`, `evals/scripts/replay_targets.py:132-135`, `tests/censuses.py:1053-1057` and `tests/evals/test_replay_targets.py:1074-1077`. The crafter's decision 2 narrowed the README paragraph to one reason. It holds: `compare` refuses a pair whose suite trees differ (`evals/scripts/noninferiority.py:1196-1200`, read), and a side with no `report_text` is the paragraph above it (`evals/README.md:81-85`). A search on wordings for "0.22", "#986", "committed replay/seeded/proofer", "the four/eight committed" and "cut from" over `evals/`, `tests/`, `docs/`, `skills/`, `agents/` and the two top-level guides found no other sentence about where the committed cases come from (executed: `git grep`). That is a sample, as the phase record says of its own search. The docstring at `tests/evals/test_replay_targets.py:1048-1052` still says "the eight committed replay and seeded cases". The frame keeps it as the history of #964 (*Out*), and it names that moment, so it is no finding.

```seal
confirms: none
```
What matched: the exemptions that stand on the committed cases. `tests/censuses.py#RECORDED_CASE` still passes every replay and seeded case file. With it switched off, `old_names` finds nothing in any of the 69 files of the new cases (executed: `.venv/bin/python` over `censuses.old_names`). So no committed case needs it today. Its stated premise does not depend on the 0.22.x cases: a case's bytes are a record that is never edited by hand, and `--case` still writes a case from any release tag. So it is no exception left standing on the old fact. The `RECORD_LINES` exemption of `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` is held by 11 rule cases, at the base and at the target alike (executed: `git grep -l -F`).

```seal
confirms: none
```
What matched: the changelog fragment. The suite's replay and seeded cases hold 13 `truth-` graders, against 27 at the base (executed: `git ls-tree` counts). No recorded proofer side is committed at HEAD, `v0.27.1` or `v0.27.0` (executed: `git ls-tree -r` for `seal/threads/*/evals/*proofer*.json`), so "No recorded side is lost" holds for the tree. A side kept outside the tree is not something this round can see.

```seal
confirms: none
```
What matched: contract rule 15 for the replay graders. Each of the four replay `truth-` graders matches exactly one line of its round record at its tag, and that line is its own finding's `location:` line (executed). Each seeded window is centred on the line its scaffold mutates: 1605, 1053, 537 and 210 (read). The scaffold's own `assert` that the old text stands at that line passed in each run above. The overlap between truths in finding 1 is a separate question that this check does not answer.

```seal
confirms: none
```
What matched: the broad gate's label. `gaps.md` *Not verified* labels the full suite, the repository-wide lint and the format check unverified and names the orchestrator, by `seal gate` after the rounds settle. The label is honest: the crafter ran a named module set and `ruff` on four files only (`trail/phases/phase-1.md`, *Scenario 5 and contract rule 2*). This round ran no broad gate either.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the proofer, on the current release, reads a new case's earlier records and writes its record at the prompt's path. Only a paid run shows it, and the owner withheld paid runs for 0.27.2, so this round did not run one either | `frame/questions.md` Q1; `gaps.md` *Not verified* | the owner, at the first paid proofer run after 0.27.2 |
| Which rounds the suite measures. Q2 is still open, and its account names the two cases from #1150's work item. It does not name a second lean: `seeded-bf9efcba` and `seeded-55b66958` both seed `skills/verify/scripts/unverified_check.py`. So the four seeded cases mutate three files, and two of the eight cases review the generators' own code | `frame/questions.md` Q2; `frame/plan.md` *Technical context*, the failure scenario | the owner |
| Whether the third `tests/` edit, `tests/evals/test_seed_defects.py:490-537`, conflicts with a sibling 0.27.2 branch not yet in this tree. The milestone names `evals/` alone | `trail/phases/phase-1.md` decision 1 | the orchestrator |
| Whether a replay scaffold that keeps `origin` lets the proofer fetch the later rounds of the record it replays. The generator writes it this way, and this diff does not change it. `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/rounds/round-1.md:231` raised it, and this round carried that row and did not judge it again | `evals/behaviour/proofer/replay-*/scaffold.sh` | the owner |
| The full suite, the repository-wide lint and the format check at the target | the tree at `89cab723` | the orchestrator, by `seal gate` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `replay_targets.py --case` with the four replay names and `seed_defects.py --case` with the four seeded names, `--out` a scratch directory, then `diff -r` of each against its committed directory | each exit 0, and every `diff -r` exit 0 |
| `replay_targets.py --count 4` and `seed_defects.py --count 4`, `--out` a second scratch directory, then `diff -r` against `evals/behaviour/proofer` excluding `rule-proofer-one-finding` | each exit 0, the same eight names, `diff -r` exit 0 |
| each new `scaffold.sh` run with `sh` in its own empty scratch directory, then `head -1 seal/README.md`, `test -d seal/specs`, `test -e` of the prompt's report path | eight exit 0, eight marker lines, no `seal/specs`, no report |
| `python3 -I -` reading on stdin: each seeded case's `truth-` patterns searched over its round 1 record from `git show <tag>:` | `seeded-55b66958`: `truth-1` and `truth-seeded` both match round 1's finding 1 line; in the other three, `truth-seeded` matches nothing |
| `python3 -I -` reading on stdin: each seeded line set against every `path:line` of every round 1 finding that is a truth | `seeded-55b66958` within 15 lines of `:1060-1086`; `seeded-bf9efcba` inside `:1587-1652`; the other two clear |
| `python3 -I -` reading on stdin: each replay `truth-` pattern searched over its round record at its tag | each matches one line, its own finding's |
| `bin/seal mutate evals/scripts/replay_targets.py --replace "    for e in recurred_truths().get(case, []):" "    for e in []:" --tests "bin/test -q -p no:xdist tests/evals/test_seed_defects.py -k test_the_replay_and_seeded_generators_read_the_entries_too"` | `red: the cases failed against the mutation (exit 1)`, and `git status -s` empty afterwards |
| `bin/test -q` over the seven modules named in the fifth confirmation | 263 passed, exit 0 |
| `bin/seal layout --pairs` | exit 0; no pair in `tests/evals/test_seed_defects.py` |

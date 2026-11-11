# Review round 2: 1794383424-the-gate-ships-a-copy-of-one-workflow

```seal
target: f0e6b7be0, fixes 27bbbdd75..87698a9ff
```

This is a verifying round. The code under review is the diff of fix pass 1,
`27bbbdd75..87698a9ff`: `15d57e9bb` (the framer's fold of `frame/design.md`
and `frame/plan.md`), `d0d00e0c9` (the comment above `resolve_base` and
`trail/phases/phase-1.md`) and `87698a9ff` (the close blocks of round 1).
`f0e6b7be0` merges `origin/release/v0.37.4` at `10e721f11` (#1498). It
changes `.claude-plugin/plugin.json`, `tests/censuses.py` and the records of
work item `1794383422-the-census-reads-root-names-from-a-case-root`, and no
file this work changes (executed: `git diff --name-only 87698a9ff
f0e6b7be0`). `routing.md`, the three frame files, `gaps.md`, `changelog.md`,
`pr.md` and `trail/phases/phase-1.md` were each read whole at `f0e6b7be0`.
No `pr.<lang>.md` stands, and none is owed: `seal/config.json` names English
for both language keys. No `seal/parity.json` and no `Pact` key is
declared. The runs below were taken in a `git clone --no-local` of the
worktree at `f0e6b7be0`, under the round's scratch directory.

Carried from round 1 and not established again: the reading of *Scope* items
1 to 9 against the build diff, S4 and S5 as round 1 ran them, and the
coordinates of `5909a2776` that round 1 opened (`def gate` at `:2571`,
`def main` at `:2804`). Re-run here: the `evidence: executed` line of each
of round 1's findings.

## Findings

### 1. `frame/design.md` says no test caller of `panel` passes a fifth positional argument, and `Test_panel` passes one

```seal
severity: should
location: `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/frame/design.md:60`
evidence: executed `git grep -n -E '(gate|broad_gate)\.panel\(' -- tests` at `f0e6b7be0`, which lists `tests/skills/test_broad_gate.py:1564` passing `"tree 1.0"` as the fifth positional argument; read `skills/verify/scripts/broad_gate.py:1858-1866`, `5909a2776:tests/skills/test_broad_gate.py:2061`
```

Why it matters: *Data & interfaces* is the frame's statement of the
interface after the work, and the sealer reads it against the tree. Its
last sentence at `:60` reads "After *Scope* item 4, no test caller passes a
fifth positional argument (read: G10)." At the target,
`Test_panel#test_accepts_the_item_and_the_gate_row` calls
`gate.panel("c", base, checks(), str(item), "tree 1.0")`
(`tests/skills/test_broad_gate.py:1564`). That is five positional arguments,
and the fifth binds to `copy`, which `panel` now takes fifth
(`broad_gate.py:1858-1866`). At `5909a2776` the same case passed `WORKFLOW`
fifth and `"tree 1.0"` sixth (`:2061`). So the sentence's point holds: no
test caller passes a workflow where `copy` now stands. Its words do not
hold, and a sealer who runs the same `git grep` finds a caller it says is
absent. The sentence states what the work does, so it is read against the
target (`skills/implement/SKILL.md` *Document layout — two roots, three
lifetimes*). The fold at `15d57e9bb` rewrote the line's first clause and
left this one. Round 1 recorded the same call as a match ("five with `copy`
fifth") and did not set it against this sentence.

The sentence is the frame's only statement of the test callers' arguments
(executed: `git grep -n -i -e fifth -e positional` over the work item, which
finds it and round 1's record alone). The fold owes no other line.

```markdown
- `broad_gate.panel(tree, base, checks, item, copy=None, branch=None, run=None)`: the `workflow` parameter leaves. `gate` is its one caller in the plugin (executed: `git grep -n "panel("` over `skills`, `lib` and `.github`). After *Scope* item 4, no test caller passes a workflow: the one test caller with a fifth positional argument, `Test_panel#test_accepts_the_item_and_the_gate_row`, passes the copy, which `copy` now takes fifth (read: G10).
```

### 2. The phase record cites G5 for the four files that S4 lists

```seal
severity: should
location: `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/trail/phases/phase-1.md:5`
evidence: read `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/trail/phases/phase-1.md:5`, `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/frame/design.md:13`, `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/frame/design.md:55`; executed `git show <c>:seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/trail/phases/phase-1.md` for `f614a68e8` and `d0d00e0c9`, and the same for `frame/design.md` at `0dd6d89f3`, `4df4b087a` and `15d57e9bb`
```

Why it matters: `trail/phases/phase-1.md:5` claims "S4's `git grep` listed
the four files G5 names before the build." G5 (`frame/design.md:13`) is the
probe of what the section printed. It names `templates/setup/hygiene.yml`
and this repository's `.github/workflows/hygiene.yml`, and no list of four
files. The four files are in S4 itself (`frame/design.md:55`): "At
`5909a2776` it lists `skills/verify/orchestration.md`, ...". G5 has held the
probe in every version of the frame (`0dd6d89f3`, `4df4b087a`,
`15d57e9bb`). So the citation was wrong when the phase wrote it at
`f614a68e8`. `d0d00e0c9` rewrote this line for round 1's finding 2 and kept
the sentence. A sealer checking the crafter's account opens G5 and does not
find the files the account says it names. The defect came from the build
phase, not from the fix pass, so this finding takes no `regression:` line.

```markdown
S4's `git grep` listed the four files S4 names at `5909a2776` before the build.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the comment above `resolve_base`
(`skills/verify/scripts/broad_gate.py:2240-2243`) now names `moved_line` and
the refusal below it as the readers of `base.given`. Neither is a check. The
text is round 1's snippet, word for word. `git grep -n -e 'base\.given' --
skills lib .github bin` at `f0e6b7be0` lists `:500-529` inside `moved_line`
and `:2247`, the refusal. It also lists the comment at `:2240`, and no other
line. So two readers is the whole count, and the fix pass's claim that no
other comment in the file counts them holds. The frame half stands at
`frame/design.md:29`: `gate`'s comment "names `moved_line` and the refusal
of a base that does not resolve (`:2622-2627`) as the readers of
`base.given`". At `5909a2776`, `:2621` is `base = resolve_base(...)` and the
refusal runs from `:2622` to `:2627`. The comment change is a comment, so
nothing but the import can fail. The narrow run below, `uvx ruff check` and
`uvx ruff format --check` on the file pass, and the four rewritten lines are 75
columns at most. Executed and read.

```seal
confirms: round-1#2
```
What holds: every sentence that round 1's finding 2 located now names
`gate` for the lines that stand in `gate()`. These are `frame/design.md:12`
("inside `gate` (`:2571-2803`; `main` at `:2804` parses the arguments and
calls it)"), `:29`, `:60` and `:78`, `frame/plan.md:7` and
`trail/phases/phase-1.md:12`. `git grep -n -w main` over the work item,
with the round records left out, finds `main` at five places. Two name the
branch: the changelog's base of `main`, and *Removes*' "a base of
`main`" at `design.md:76`. One is `design.md:61`, "`broad_gate.main`'s
stderr", which round 1 kept. One is the new judgment row at `plan.md:55`,
and one is the account of the miss at `phase-1.md:5`, and both state the
miss as history. None places a line of `gate()` in `main`, so the fix pass's
claim of no other such sentence holds. `phase-1.md:5` now says the build's
reading checked each line number and not the function. That is true of what
round 1 found. The new judgment row at `plan.md:55` gives `broad_gate.py:2246`
at `27bbbdd75` for the refusal, and `git show 27bbbdd75:...` puts it at
`:2246`. Its `def gate` at `:2571-2803` of `5909a2776` matches round 1's
executed lines. Executed and read.

What matched: `pr.md`'s two quotes, after the fold. The chosen row's
verdict cell stands word for word at `frame/plan.md:17`. The title quote
stands at `frame/plan.md:56`, the row *Judgments of the run* now holds below
the new row at `:55`. `pr.md` cites both by section and row, not by line, so
the inserted row moves nothing it names. Read.

What matched: `changelog.md`, `gaps.md` and `routing.md` are unchanged since
round 1 (executed: `git diff --stat 27bbbdd75 f0e6b7be0` over the work item
lists only `frame/design.md`, `frame/plan.md`, `trail/phases/phase-1.md` and
`trail/rounds/round-1.md`). Read whole at
the target, each sentence still matches the tree. `gaps.md` labels the broad
gate `unverified` and names the orchestrator, which is honest.

What matched: the fix pass's narrow run's two failures, the `Test_census_case`
cases, pass at `f0e6b7be0` with #1498 merged, as the prompt's account of
#1498's hand-back says. Executed (see `## Probes`).

The fix diff adds no test, so no new case is read against its group.

A note with no finding: `trail/phases/phase-1.md:24` says #1498's fix is
"`10e721f11`, which this branch does not hold". Since `f0e6b7be0` the branch
holds it. The paragraph reports the phase's narrow run over the tree as it
stood then, so it states that time and is no claim about the target.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD: the full suite, `uvx ruff check .` and `uvx ruff format --check .`. The suite is `unverified` here (contract rule 2). | `seal/config.json` `Broad gate` | the orchestrator's broad run |
| S2: no `CI also` row in the gate's report at HEAD, and no stderr line opening `seal gate: .github/workflows/hygiene.yml's` | `gaps.md:8` | the orchestrator, reading its broad run's output |
| S3's case on `windows-latest`, where `os.path.join` spells the searched path with `\` | `tests/skills/test_broad_gate.py` `Test_main::test_a_workflow_with_a_release_job_leaves_the_run_as_it_was` | CI on the pull request |
| Carried from round 1, and no record answers it at the target: whether `CONTRIBUTING.md` *What a change to a gate must carry* asks this body to state a failure direction and a prompt budget for a change that leaves the gate's verdicts and exit codes as they were. If it does, which record `pr.md` quotes for them. | `CONTRIBUTING.md`, `pr.md` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_broad_gate.py tests/test_conftest.py tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py -q`, in the clone at `f0e6b7be0` | exit 0: 324 passed, 1 skipped |
| `bin/test tests/test_conftest.py -q -k Test_census_case`, in the clone at `f0e6b7be0` | 2 passed |
| `uvx ruff check` and `uvx ruff format --check` on `skills/verify/scripts/broad_gate.py` | both exit 0 |
| `git grep -n -e 'base\.given' -- skills lib .github bin` | `broad_gate.py:500-529` in `moved_line`, `:2240` the comment, `:2247` the refusal |
| `git grep -n -E '(gate\|broad_gate)\.panel\(' -- tests` | four calls in `tests/skills/test_broad_gate.py`, at `:1550`, `:1564`, `:1571` and `:1581`; `:1564` passes five positional arguments |

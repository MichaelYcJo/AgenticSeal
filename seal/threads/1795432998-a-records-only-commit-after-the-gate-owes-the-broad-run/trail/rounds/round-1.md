# Review round 1: 1795432998-a-records-only-commit-after-the-gate-owes-the-broad-run

```seal
target: eb03b235f against origin/release/v0.38.6
```

The branch was read against `origin/release/v0.38.6` at `2025561ae`, over
its nine commits, `e5bdbff55` to `eb03b235f`. This is the first round, so
no coordinate or verdict was carried from an earlier one, and every fact
below was established here. `seal/parity.json` is not declared, so no
parity comparison was owed. The work item's records were each read whole
at `eb03b235f`: `routing.md`, the three frame files, `gaps.md`,
`changelog.md`, `pr.md` and `trail/phases/phase-1.md`. `seal/config.json`
names English for both language keys, so no `pr.<lang>.md` is owed and
none stands.

The orchestrator's spawn prompt said that `broad_gate` calls `follows`
with no `only` and that `guarantee` passes `only=CLOSING_RECORDS`. That
claim holds: `skills/code-review/scripts/chain_check.py:1677` calls
`follows(root, sha, base, item)`, and `:1719` calls
`follows(root, sha, base, item, only=CLOSING_RECORDS)`, where `:303` sets
`CLOSING_RECORDS` to `trail/gate.md` and `guarantee.md` (read).
`agents/sealer.md:60-66` lets the newest run be followed only by paths
under `seal/threads/<item>/` (read). The diff changes neither file. So the
frame's premise, that the mechanisms already hold the rule and only its
statements change, is right.

The new case at `tests/skills/test_chain_check.py:3096` was read against
its group, `Test_broad_gate`, and the `Test_guarantee` and `Test_follows`
classes. It covers something none of them covers: no other case commits a
record other than `trail/gate.md` and `guarantee.md` after the run and
asks the broad gate arm, as `frame/design.md` G13 says. Its guarantee
assertion repeats in part what `Test_guarantee` already pins for a
`gaps.md` commit after the verdict, which is no gap, since the case as a
whole holds the fact *Scope* item 8 states.

## Findings

### 1. The new rule paragraph says a commit of `trail/gate.md` or `guarantee.md` owes the sealer again

```seal
severity: should
location: `skills/code-review/orchestration.md:268-271`, `seal/threads/1795432998-a-records-only-commit-after-the-gate-owes-the-broad-run/frame/design.md:40`, `seal/threads/1795432998-a-records-only-commit-after-the-gate-owes-the-broad-run/changelog.md:3`
evidence: read `skills/code-review/orchestration.md:268-279`, `skills/code-review/gate-to-pull-request.md:12-16`, `skills/code-review/gate-to-pull-request.md:88-91`, `skills/code-review/scripts/chain_check.py:303`, `skills/code-review/scripts/chain_check.py:1719`, `seal/threads/1795432998-a-records-only-commit-after-the-gate-owes-the-broad-run/frame/design.md:40`
```

Why it matters: the paragraph is now the one statement of the rule for
the orchestrator (`frame/design.md` *Scope* item 3). It says: "A commit
after the newest broad run that changes only files under
`seal/threads/<work-item-id>/` owes no broad run. It owes `seal pr-body`
on the body file again and the sealer again"
(`skills/code-review/orchestration.md:268-270`). Two commits that every
run makes fall under that subject. The orchestrator commits
`trail/gate.md` after the run (`skills/code-review/gate-to-pull-request.md:88`),
and it commits `guarantee.md` after the sealer
(`skills/code-review/gate-to-pull-request.md:12`). Read as written, the
commit of `guarantee.md` owes another sealer, whose `guarantee.md` commit
owes another, without end. The guarantee arm says the opposite: those two
files may follow the verdict's commit (`chain_check.py:1719`, with
`CLOSING_RECORDS` at `:303`). The paragraph means a repair of another
record after the sealer has written its verdict, and its words do not
say so. The same wording stands in `frame/design.md:40` (*Scope* item 3)
and in `changelog.md:3` ("a records-only commit after the run owes
`seal pr-body` and the sealer again"). The fix pass owes those two
sentences as well.

```markdown
**A commit after the newest broad run that changes only files under
`seal/threads/<work-item-id>/` owes no broad run.** Where such a commit
changes a record other than `trail/gate.md` and `guarantee.md` after the
sealer has written its verdict, it owes `seal pr-body` on the body file
again and the sealer again, and the sealer reads every record at HEAD.
Those two files may follow the verdict's commit, as the guarantee arm
reads it (`skills/code-review/scripts/chain_check.py#CLOSING_RECORDS`).
A commit that changes any other path owes the broad run
again, after the round that the row *No fix that no round reads* of
`skills/core/SKILL.md` *Judgment is not licence to skip a party* gives it.
```

The rest of the paragraph, from "`agents/sealer.md` step 1 and the pull
request check's broad gate arm", stays as it is. In `frame/design.md:40`
and `changelog.md:3`, the clause on what the commit owes takes the same
condition: a record other than `trail/gate.md` and `guarantee.md`,
changed after the sealer's verdict.

```seal
verdict: fixed 8baf1cb43
answer: The paragraph in `skills/code-review/orchestration.md` takes the paste-ready fix, with one more clause: the commits of `trail/gate.md` and `guarantee.md` owe neither another broad run nor another sealer, which `frame/design.md` *Scope* item 3 now states. The rest of the paragraph stands, rewrapped. `changelog.md:3` now says that a records-only commit owes no broad run, and owes `seal pr-body` and the sealer again where it changes a record other than those two after the sealer's verdict. `frame/design.md:40` was folded by the framer at `07a38f1ce`. The other statements in this branch's files were read at `8baf1cb43`, and none says that a commit of the two files owes the sealer: `gate-to-pull-request.md:147` is about a repair of another record, and `templates/setup/config.md`, `README.md`, `README.ko.md`, `gaps.md` and `pr.md` do not state it.
```

### 2. The core's fourth row names "the closing records", a term the core never defines and that reads as the closing memo

```seal
severity: should
location: `skills/core/SKILL.md:115`, `seal/threads/1795432998-a-records-only-commit-after-the-gate-owes-the-broad-run/frame/design.md:39`, `seal/threads/1795432998-a-records-only-commit-after-the-gate-owes-the-broad-run/changelog.md:11`
evidence: executed `grep -n "closing records" skills/core/SKILL.md` at `eb03b235f`, which prints line 115 alone, and `git show 2025561ae:skills/core/SKILL.md | grep -n "closing records"`, which prints nothing; read `skills/core/SKILL.md:114-115`, `docs/forms/the-guarantee.md:28`, `skills/implement/SKILL.md:239`, `skills/implement/SKILL.md:274`
```

Why it matters: the new cell says the guarantee arm fails a ready pull
request "without `Verdict: sealed` at HEAD or at a commit that only the
closing records follow" (`skills/core/SKILL.md:115`). The core is the text
every session reads first, in every user's repository, and this is the
only place it uses the term. The term was not there before the diff. It is
defined in `docs/forms/the-guarantee.md:28` as `trail/gate.md` and
`guarantee.md`, and in `chain_check.py:303`, and a core reader opens
neither. The plugin calls `gaps.md` "the closing memo"
(`skills/implement/SKILL.md:239`, `:274`), and a phase's close writes
`gaps.md`, the phase record and the changelog fragment together, as this
branch's commit `b566ca252` does. So "the closing records" can be read as
those records. Under that reading, the fourth row lets a `gaps.md` or
`changelog.md` repair follow the seal, which is the opposite of what
`frame/plan.md` *Alternatives considered* chose and of what the new case
pins (`tests/skills/test_chain_check.py:3106-3117`). The row just above,
row 3, exempts every record from the broad run, which makes this reading
easier to slip into. The changelog's first item already spells the two
files out. `frame/design.md:39` (*Scope* item 2) and the first
*Process changes* row of `changelog.md:11` use the bare term, and the fix
pass owes them too.

```markdown
| No pull request without a seal | nothing reaches the base that the last independent party did not guarantee | the same check's guarantee arm: a ready pull request fails without `Verdict: sealed` at HEAD or at a commit that only `trail/gate.md` and `guarantee.md` follow; and its body arm: a ready pull request fails where its body is not what `seal pr-body` composes at HEAD, the seal mark among it |
```

```seal
verdict: fixed 8baf1cb43
answer: `skills/core/SKILL.md:115` takes the paste-ready row as written, and the first *Process changes* row of `changelog.md` says that the row lets `trail/gate.md` and `guarantee.md` follow the guarantee. `frame/design.md:39` was folded by the framer at `07a38f1ce`. At `8baf1cb43`, a `git grep` for "closing records" over the files this branch changed finds the term only in `tests/skills/test_chain_check.py`. That module uses it as `chain_check.py#CLOSING_RECORDS`'s name, and one of the uses is the refusal sentence the case builds, so it stays. `templates/setup/config.md:485` already spells out the two files.
```

## Confirmations

What matched: `frame/design.md` *Scope* items 1, 2, 4, 5, 6, 7 and 8 each
stand at the target as the item states: `skills/core/SKILL.md:114-115`,
`skills/code-review/gate-to-pull-request.md:148-150`,
`skills/implement/orchestration.md:423`, `README.md:285-287`,
`README.ko.md:288-290`, `templates/setup/config.md:331-339` (inside
`## Broad gate`, before `### What is refused, and what stays allowed` at
`:341`) and `tests/skills/test_chain_check.py:3096-3126` (read). Item 3's
paragraph stands after the paragraph on a conflict with the base, at
`skills/code-review/orchestration.md:268-279`, apart from finding 1
(read). *Data & interfaces* holds: the diff leaves
`skills/code-review/scripts/` and `agents/` untouched, and seven text files
change (executed: `git diff --stat 2025561ae..eb03b235f`).

What matched: the acceptance scenario *No sentence states the strict
rule*. G15's command prints nothing at the target (executed in the clone,
exit 1 with no output).

What matched: the phase record claims the case was seen red twice, once
per guard. Both mutations were re-run in the clone through `bin/seal
mutate`. With `broad_gate` calling `follows(..., only=CLOSING_RECORDS)` the
case went red at `tests/skills/test_chain_check.py:3105`, the first
`broad_gate` assertion. With `follows` reading `if False or (` it went red
at the last assertion, `[] == [...]`, on the refusal naming `f.txt`
(executed). So each assertion pins the guard it names. The clone's
`git status` was clean after both runs.

What matched: the phase record's other claims hold. No file changed
between `e5bdbff55` and `e36796bb8` except the three frame files
(executed: `git diff --stat`). The module docstring's *broad gate* and
*guarantee* rows already state the two sets (`chain_check.py:67-74`,
read). `git diff-tree --name-only` lists `changelog.md` before `pr.md`, so
the guarantee refusal names `changelog.md`, which the narrow run confirms
(executed).

What matched: the narrow runs the plan names pass at the target
(executed: `Test_broad_gate`, `Test_guarantee` and `Test_follows` of
`tests/skills/test_chain_check.py`, 37 passed; the six text and behaviour
modules of the plan row with `tests/behaviour/test_docs_line_wrap.py`, 116
passed). `seal rules --check` holds all 175 check lines (executed).

What matched: each quote of `pr.md` stands word for word at its
coordinate: `frame/design.md:34`, the G3 row at `frame/design.md:11`, and
`frame/plan.md:47` (read).

What matched: the row of `gaps.md` that asks a round to read
`README.ko.md:288-290` beside `README.md:285-287`. The Korean clause
"pull request 가 담을 커밋에서, 또는 뒤에 작업 항목의 기록만 이어지는
커밋에서" says the commit the pull request will carry, or a commit that
only the work item's records follow. That is the rule the English sentence
states (read).

What matched: the frame's `## Rule changes` `from` text stands word for
word at `docs/releasing/branch-and-release.md:279-280` (read). The chain
check printed no notice at any line of `frame/design.md` naming a test pin
or a copy (executed).

The search for other statements of the rule was a sample, here as in the
phase record. This round ran
`git grep -n -i -E "(broad (run|gate|pass)|gate run|trail/gate\.md).{0,80}(HEAD|head commit|again)"`
outside `seal/threads/` and `tests/`. Beyond the lines the phase record
names, it printed `docs/layout/the-record-layout.md:35` and
`skills/verify/orchestration.md:75`. The first is about a merge conflict
and the second about a `new` failure, and both stay true. Row 3's
*Held by* cell names two cases in which `agents/sealer.md` step 1 withholds
and leaves out a run naming a commit that does not resolve or that HEAD
does not descend from (`agents/sealer.md:62`). The cell does not say
"only", so it contradicts nothing, and it is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check over the target: the suite is `unverified` by this round, and contract rule 2 leaves it out of this round | `gaps.md:7` | the orchestrator, at the broad run after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/seal mutate skills/code-review/scripts/chain_check.py --replace 'behind = follows(root, sha, base, item)' 'behind = follows(root, sha, base, item, only=CLOSING_RECORDS)' --tests "bin/test tests/skills/test_chain_check.py -q -k test_lets_the_records_follow_the_run -p no:xdist"` | `red`, failing at `tests/skills/test_chain_check.py:3105`; the file was restored |
| `bin/seal mutate skills/code-review/scripts/chain_check.py --replace 'if not path.startswith(f"{item}/") or (' 'if False or (' --tests "bin/test tests/skills/test_chain_check.py -q -k test_lets_the_records_follow_the_run -p no:xdist"` | `red`, failing at the last `broad_gate` assertion, `[]` against the refusal naming `f.txt`; the file was restored |

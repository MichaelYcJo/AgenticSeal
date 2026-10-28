# Review round 2: 1793226630-most-contract-rules-are-proved-by-their-own-wording

target: 208f7076, fixes 32fe2e88..208f7076

## Findings

### 1. `frame/plan.md` rows C and E still give the readers that rules 4, 5 and 15 had before the fix pass

severity: should
location: `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/frame/plan.md:72`, `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/frame/plan.md:74`
evidence: executed `git grep -n -E "rules? (2, )?4|4 and 15|4, 7|5, 12|3, 5|rules 2, 5|sealer cases" -- seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording`, `grep -n '^check:' skills/agent-contract/SKILL.md`
verdict: fixed 5a77bc37

The fold at `208f7076` rewrote the frame lines that the fix pass listed:
the rule rows of `frame/design.md`, judgments 4 and 5 of
`frame/questions.md`, and the eval targets at `frame/plan.md:45-48`. Two
rows of the plan's *Alternatives considered* table state the same fact,
and the fold did not reach them.

Row E says "the sealer cases read rules 2, 4 and 15, and the crafter cases
read rule 7". At HEAD the sealer cases are named by rules 2 and 5
(`skills/agent-contract/SKILL.md:46`, `:78`). Rules 4 and 15 read `check:
none reader: the sealer at each guarantee` (`:67`, `:182`). Row C says that
rules 3, 5, 12, 13, 14, 17, 18, 19 and 20 "describe a judgment" and that a
grader for them "would read words again". Rule 5 now names two existing
graders, and rules 4 and 15, which name no case, are not in the list.

Round 1, finding 1 rested part of its grounds on row E. Row E is the frame's
statement of which existing readers this work keeps. A sealer that compares
the frame with the contract finds the plan contradicting rules 4, 5 and 15.
This is the class contract rule 12 asks the fix to cover. The fix pass's
list of frame lines named `frame/plan.md:45-47` and stopped there.

Replace the two rows with:

```markdown
| C. Replace each removed pin with a new behaviour eval case | An eval case is a paid run (`runs: 2`, `timeout_seconds: 1200`, read in `evals/behaviour/crafter/rule-crafter-slugify/case.yaml`) taken at a preload rewrite, never in CI. Rules 3, 12, 13, 14, 17, 18, 19 and 20 describe a judgment, and `evals/scripts/rule_cases.py:7-8` says the graders "read files and tool calls, never a judge". A grader for them would read words again. Rules 4 and 15 have no existing grader that reads the sealer's own labels or its own red runs (`frame/design.md` *Why each eval case is the reader it is*), and a new case for them is the paid run this row weighs | Rejected. Existing eval cases are named where their graders read the behaviour |
```

```markdown
| E. Name `none reader:` on every rule that loses its pin, evals included | It throws away the readers the tree already has: the sealer cases read rules 2 and 5, and the crafter cases read rule 7 | Rejected |
```

answer: The frame is the orchestrator's, and its fold at `5a77bc37` rewrote rows C and E. I read both at HEAD: `frame/plan.md:72` now lists rules 3, 12, 13, 14, 17, 18, 19 and 20 as judgments and gives rules 4 and 15 their own sentence, and `:74` says the sealer cases read rules 2 and 5. Both match `skills/agent-contract/SKILL.md:46`, `:67`, `:78` and `:182`. This pass made no commit for this finding.

### 2. The phase 2 bullet and the `gaps.md` row on the 182 say that `frame/design.md` calls 182 a bound, but the fold removed that sentence

severity: should
location: `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/trail/phases/phase-2.md:146-147`, `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/gaps.md:16`
evidence: executed `git grep -n "182" -- seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording`, `git show d0b5cf4f:seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/frame/design.md | grep -n "182"`, `git diff --stat d0b5cf4f f9c33d98 -- seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/frame/`
verdict: fixed ec52e4f4
regression: round-1#3

The unit is the bullet *The issue's 182 does not bound the count* at
`phase-2.md:146-154` and the row *The bound on the count* at `gaps.md:16`.
`16e0d911` rewrote both. Phase 2's row of `frame/plan.md` has the count
taken by the method in `frame/design.md` *Data & interfaces*. At
`d0b5cf4f` that section said "The issue's rough figure of 182 for
`tests/text` bounds the count from above". The fix pass kept that
sentence as the premise of the bullet and the row. Then the orchestrator's
fold at `208f7076` replaced it with "The issue's figure of 182 is its own
grep ... so it is no bound on this count" (`frame/design.md:230-232`). Both
records now quote, in the present tense, a sentence the frame no longer
holds.

The sentence does not change between `d0b5cf4f` and `f9c33d98`. Only
`frame/plan.md`'s Status cells changed there (executed), so `d0b5cf4f` is
the frame that both phases counted against.

This matters now because the orchestrator posts phase 2 on #1111 after this
round. A reader of the issue who opens `frame/design.md` finds the opposite
of what the bullet says the frame states. The `gaps.md` row stands under
*Where spec and implementation diverged*. A sealer that compares its quote
with the frame finds no such sentence.

In `phase-2.md`, the bullet's first two lines become:

```markdown
- **The issue's 182 does not bound the count.** `frame/design.md` at
  `d0b5cf4f`, the frame this phase counted against, said the issue's rough
  figure of 182 bounds the count from above. The issue
```

In `gaps.md`, the row's *Spec says / code did* cell becomes:

```markdown
`frame/design.md` at `d0b5cf4f`: "The issue's rough figure of 182 for `tests/text` bounds the count from above." The method counts 255, and `208f7076` wrote the count's reading of 182 into the frame
```

answer: The finding holds. `208f7076` replaced the sentence that both records quoted (read, `git diff d0b5cf4f HEAD -- frame/design.md`). `ec52e4f4` applies the round's text: the bullet in `phase-2.md` and the *Spec says / code did* cell in `gaps.md` now quote `frame/design.md` at `d0b5cf4f`, the frame both phases counted against. The same diff shows the fold left *Data & interfaces*' list of excluded kinds unchanged, so the command-spelling row of `gaps.md` still reads true at HEAD. Sweep: I ran `grep` for `182`, `bound`, `false-red`, `rule 4`, `rule 15` and `11` over `trail/phases/`, `gaps.md` and `changelog.md` (executed). No other sentence there states the old bound, the old count or the old readers.

### 3. Round 1's answer to finding 2 says `git grep` finds 11 `check:` lines that name an eval case, but it lists ten and the tree holds ten

severity: should
location: `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/trail/rounds/round-1.md:104`
evidence: executed `git grep -n -E 'check:.*evals/behaviour' 16e0d911 -- ':!seal/'`, `git grep -n -E '^\s*check:.*evals/' -- ':!seal/'`
verdict: deferred trail/rounds/round-2.md
regression: round-1#2

The unit is finding 2's `answer:` line at `round-1.md:104`, which
`16e0d911` wrote. `frame/design.md` *Why each eval case is the reader it
is* says which eval case reads which contract rule. Under contract rule 12,
the fix pass swept every `check:` line in the tree that names an eval case,
and it wrote the number 11 beside a list of ten. The list is right and the
number is wrong.

The grep at `16e0d911` and at HEAD finds ten rule lines:
`agents/proofer.md:74`, `agents/sealer.md:125`, `:130`, `:136` and `:148`,
`skills/code-review/SKILL.md:38` and `:140`, and
`skills/agent-contract/SKILL.md:46`, `:78` and `:102`. A wider pattern also
finds two fixture strings at `tests/github/test_rules.py:266` and `:503`,
but neither is a rule's line. The spawn prompt of this round repeats "the 11
`check:` lines". A sealer that takes the claim and re-runs the sweep gets
ten, and the record contradicts itself.

In finding 2's `answer:` line, replace:

```markdown
`git grep` finds 11 `check:` lines in the tree that name an eval case.
```

with:

```markdown
`git grep` finds 10 `check:` lines in the tree that name an eval case.
```

answer: The finding holds. The right number is 10: `git grep -n -E '^\s*check:.*evals/' -- ':!seal/'` finds 10 lines in 4 files, the ten that round 1's answer listed (executed). Round 1's record stays as written, so the correction is this answer line, which the orchestrator commits with this record. No living record of mine states the count: `grep` for "11 `check`" over `trail/phases/`, `gaps.md` and `changelog.md` exits 1 (executed). Phase 2's "eleven" counts lead literals, not `check:` lines.

## Confirmations

confirms: round-1#1
Rule 5's line at `skills/agent-contract/SKILL.md:78` names
`rule-sealer-false-red` and `rule-sealer-untrue-body`, and both hold
`case.yaml` (executed `ls`). Each truth grader passes only where the
guarantee's verdict line names the claim the tree contradicts
(`truth-false-red.md:1-7`, `truth-untrue-body.md:1-7`, read). The
changelog sentence at `changelog.md:3` is the text round 1 wrote. The
`gaps.md:23` row names the three sealer cases. `bin/seal rules --check`
exits 0. Executed and read.

confirms: round-1#2
Rules 4 and 15 read `check: none reader: the sealer at each guarantee`
(`skills/agent-contract/SKILL.md:67`, `:182`). That uses the form of
`docs/the-review-record.md:613`, and `bin/seal rules --check` accepts it
(executed). The changelog says so. I re-read the sealer rules at
`agents/sealer.md:125-148` against the cases they name. `:130` (a verdict
names its claim) and `:136` (a `seen red` is re-run) are acts of the sealer
under test. I did not re-read the graders behind `agents/proofer.md:74`,
`skills/code-review/SKILL.md:38` and `:140`, or `agents/sealer.md:125` and
`:148`. They lie outside the fix diff, so for those lines I carry the fix
pass's reading. The sweep's count is finding 3. Executed and read.

confirms: round-1#3
I re-ran round 1's executed line: the issue's grep per file over
`tests/text` gives 182 at `0b75346f` (174 without the contract module) and
168 at `ee746f3b`. `gh issue view 1111` shows the command under the rough
count, written `-r tests/<dir>` (executed). The `## Not verified` row that
asked the owner is gone, so nothing in the records sends the question to
the owner. `frame/design.md:230-232` now states the 182 as the issue's
grep and no bound. Finding 2 covers the sentence that still quotes the old
frame. Executed.

confirms: round-1#4
`phase-2.md:124-132` carries round 1's sentence. I re-ran round 1's
executed lines. `git grep -n "still a sentence"` at `ee746f3b` finds the
word at
`tests/behaviour/test_every_orchestrator_act_names_its_delivery.py:106` and
the cell at `tests/text/test_broad_gate_rule.py:403`. I wrote the probe
again from round 1's `## Probes` row. Over `test_review_axes.py` at
`ee746f3b`, it lists 15 `in` and 3 `not in` comparisons. That is 10 counted
(`:16`, `:31` and `:138` among them), 4 left out (`:49` heading, `:110`
path, `:111` command, `:112` the `Seal-Routing` trailer) and 1 in Q2
(`:109`), which is the phase's row. Executed.

confirms: none
Where the fold touched the frame, it matches the build. `frame/design.md:122`,
`:123` and `:133` equal `skills/agent-contract/SKILL.md:67`, `:78` and
`:182`. Judgments 4 and 5 of `frame/questions.md` list the same readers, and
`frame/plan.md:45-48` names the three sealer targets. Two sentences were
read and raise no finding. At `frame/design.md:153`, "that case" follows a
sentence that names two cases, and the citation `agents/sealer.md:132-136`
and "the crafter's breach" fix it to `rule-sealer-false-red`. The grounding
row at `frame/design.md:15` names the proofer and orchestrator spellings,
claims no full list, and is not wrong for leaving out the sealer's. Read.

confirms: none
Apart from finding 2's sentence, phase 2's count is fit to post. A script
over `phase-2.md` gives 39 rows, and their module names equal the
`tests/text` modules at `ee746f3b` except the contract module (diff exit
0). The columns sum to 255, 124, 3, 75 and 81, and 255, 124 and 3 make 382.
The kinds sum to the total row. In each of the 26 modules with a left-out
number, the line list under *Where each left-out literal stands* holds as
many lines as that number. The probe's listing over the 39 modules gives
382 `in` and 75 `not in`, as the phase says. No file under `tests/` changed
between `ee746f3b` and HEAD. Executed.

confirms: none
Carried, not re-established: the coordinates round 1 named were opened
where they point instead of being searched again. These were the issue's
command, the truth graders, `agents/sealer.md:132-136`, and the probe's
method. Round 1's per-module re-decision of six modules was not repeated.
Only `test_review_axes.py`'s candidates were listed again. Every verdict
above was reached this round. `trail/phases/phase-1.md:28` says "all six
eval targets" of `9ad992b6`, which is a past state, so it stands as the fix
pass said. Read.

confirms: none
The checks the caller named, run narrow through `bin/test -q`, each exit 0:
the contract module (29), the five `HEADING` importers (5, 5, 23, 221, 17),
`tests/github/test_rules.py` (59), `tests/behaviour/test_docs_line_wrap.py`
(39) and `tests/text/test_every_agent_reads_the_contract.py` (22).
`bin/seal layout --check` exits 0. `bin/seal rules --check` exits 0, with
"all 266 check lines in 55 rule files hold". The suite stays labelled
`unverified`, and the orchestrator answers it. Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck, including `test_the_durations_file_prices_the_suite` | the branch at `208f7076` | the orchestrator, through `seal gate` |
| Whether the eval cases rules 2, 5 and 7 name pass on a run | `evals/behaviour/sealer/`, `evals/behaviour/crafter/` | the orchestrator, at the next preload rewrite that runs the behaviour evals |
| Whether the frame lines folded at `208f7076` belong under `gaps.md` *Fed back into the spec*, which reads `none` | `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/gaps.md` | the orchestrator |
| Rule 2's case reads one agent and one command spelling. Whether that partial reach is enough for rule 2 | `evals/behaviour/sealer/rule-sealer-no-gate/graders/shape-runs-no-broad-run.md` | the owner |
| `frame/questions.md` Q1 and Q2 stand on their defaults with Status `open` | `frame/questions.md` | the owner |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_pin_sample.py <worktree> ee746f3b` (the probe at `<scratchpad>/1793226630-most-contract-rules-are-proved-by-their-own-wording/round-2/`, run then deleted), first walking every comparison under an `assert` | 392 `in` and 76 `not in`: comparisons inside comprehensions are counted too, which round 1's listing did not do |
| the same probe, rewritten to read only top-level comparisons and the operands of `and` or `or`, over `test_review_axes.py` and over all 39 modules | 15 `in` and 3 `not in` at lines 16, 31, 38, 49, 50, 59, 109 to 112, 134, 138, 247, 251, 255; 382 `in` and 75 `not in` over all 39 |
| the issue's grep, per file over `tests/text`, at `0b75346f` and at `ee746f3b` | 182 (174 without the contract module); 168 |
| `python3 -I -` over `phase-2.md`, summing the table and matching each left-out number with its line list | 39 rows; 255, 124, 3, 75, 81; 382; no mismatch in 26 modules |
| `git grep -n -E 'check:.*evals/behaviour' 16e0d911 -- ':!seal/'` | 10 rule lines and 2 fixture strings in `tests/github/test_rules.py` |
| `bin/test <module> -q` over the nine modules in *Confirmations* | each exit 0 |
| `bin/seal layout --check`; `bin/seal rules --check` | exit 0; exit 0, "all 266 check lines in 55 rule files hold" |

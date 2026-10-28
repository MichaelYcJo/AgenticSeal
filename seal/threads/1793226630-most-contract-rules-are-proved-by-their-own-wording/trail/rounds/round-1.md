# Review round 1: 1793226630-most-contract-rules-are-proved-by-their-own-wording

target: 951f316b against origin/release/v0.24.0

## Findings

### 1. Rule 5 names no reader, while two sealer eval cases grade the behaviour it asks for

severity: should
location: `skills/agent-contract/SKILL.md:78`, `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/changelog.md:3`
evidence: read `skills/agent-contract/SKILL.md:69-78`, `evals/behaviour/sealer/rule-sealer-false-red/graders/truth-false-red.md:1-7`, `evals/behaviour/sealer/rule-sealer-untrue-body/graders/truth-untrue-body.md:1-7`, `evals/behaviour/sealer/rule-sealer-false-red/scaffold.sh:155-158`, `agents/sealer.md:114-117`
verdict: open

Rule 5 says a fact handed to an agent in prose is a claim, and that for a
reviewer the implementer's account is a claim and not evidence. Its
`check:` line now reads `none reader: the proofer at review`. A reader of
the contract therefore concludes that nothing in the tree reads rule 5's
behaviour.

Two eval cases do read it. In `rule-sealer-false-red`, the fixture's phase
record claims that a case was seen red, labelled `executed`
(`scaffold.sh:155-158`). The truth grader passes only where the sealer's
verdict names that claim. The sealer can name it only if it re-ran the case
instead of taking the record's word, which is rule 5 applied by a reviewer.
`rule-sealer-untrue-body` does the same with a claim in the pull request
body. `agents/sealer.md:114-117` states the sealer's form of the same rule:
"a phase record's `seen red` ... are claims".

The frame's own test applies here. `frame/questions.md` judgment 5 names an
eval case "only where its grader reads the rule's behaviour", and
`frame/plan.md` row E rejects a design that "throws away" readers the tree
already has. Rule 5 is the one rule this change re-pointed where a grader
of the agent under test reads the rule, and the line does not name it.

The fix changes rule 5's line. `bin/seal rules --check` accepts both targets
today, because both directories hold `case.yaml`.

```markdown
check: evals/behaviour/sealer/rule-sealer-false-red/ evals/behaviour/sealer/rule-sealer-untrue-body/
```

The changelog fragment's list then reads, in place of its last two
sentences:

```markdown
Rules 3 and 17 name the orchestrator at each hand-back. Rule 5 names the sealer's `rule-sealer-false-red` and `rule-sealer-untrue-body` eval cases, and rules 12, 13, 14, 18, 19 and 20 name the proofer at review.
```

answer:

### 2. Rules 4 and 15 name an eval case whose graders read the sealer catching another party's breach, not either rule's own act

severity: should
location: `skills/agent-contract/SKILL.md:67`, `skills/agent-contract/SKILL.md:182`, `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/changelog.md:3`
evidence: read `evals/behaviour/sealer/rule-sealer-false-red/graders/shape-verdict.md:1-7`, `evals/behaviour/sealer/rule-sealer-false-red/graders/truth-false-red.md:1-7`, `evals/behaviour/sealer/rule-sealer-false-red/scaffold.sh:155-158`, `agents/sealer.md:132-136`, `evals/behaviour/crafter/rule-crafter-slugify/graders/shape-phase-record.md:1-5`
verdict: open

The caller asked whether each eval case now named reads its rule. For rules
2 and 7 it does. The agent under test is the one the rule binds, and a
grader reads that agent's act: the sealer runs no `seal gate --base`, and
the crafter leaves no `test_tmp_` file.

For rules 4 and 15 it does not. The agent under test in
`rule-sealer-false-red` is the sealer. Its graders read four things: the
verdict word `withheld`, that the verdict names the fixture's claim, that no
gate ran, and that only `guarantee.md` was written. None of them reads
whether the sealer labels its own claims `executed`, `read` or `unverified`
(rule 4). The sealer plants no case, so nothing in the case can show it
seeing a new case red (rule 15). The breach of rules 4 and 15 in the case is
the fixture's, written by `scaffold.sh:155-158`. What the graders read is
the sealer's own rule *A `seen red` is re-run against the code before the
change* (`agents/sealer.md:132-136`), which already names this case. No
crafter case reads either rule: `shape-phase-record.md` asks only that the
phase record exists.

`frame/design.md` *Why each eval case is the reader it is* says the case
proves the sealer "reads" a claim recorded without its run and a case never
seen red. That describes who holds the two rules instead of the agent
bound by them, which is what `check: none reader: <who reads it>` spells.
Under judgment 5's test, the case is not their proof.

The fix names the sealer as the reader. `docs/the-review-record.md:613`
already uses the `none reader: the sealer ...` form, and `bin/seal rules
--check` reads it.

```markdown
## 4 Label what was executed apart from what was read
...
check: none reader: the sealer at each guarantee
```

```markdown
## 15 A new case is not planted until it has been seen red
...
check: none reader: the sealer at each guarantee
```

The changelog fragment's sentence "Rules 4 and 15 name
`rule-sealer-false-red`" then reads "Rules 4 and 15 name the sealer at each
guarantee". The fix pass might hold that a downstream catch counts as a
rule's proof. If so, its answer says that, and the sentence of judgment 5
that it would contradict is named there.

answer:

### 3. The count's records say that the issue does not record how it reached 182, and route that question to the owner, but the issue states its command and the command reproduces 182

severity: should
location: `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/gaps.md:16`, `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/gaps.md:23`, `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/trail/phases/phase-2.md:144-149`
evidence: executed `gh issue view 1111 --json body`, `for f in $(git ls-tree --name-only 0b75346f tests/text/ | grep "\.py$"); do git show 0b75346f:$f | grep -c -E "assert \(?\s*\"[^\"]{25,}\"\s*\)?\s+in\b"; done`, `for f in $(git ls-tree --name-only ee746f3b tests/text/ | grep "\.py$"); do git show ee746f3b:$f | grep -c -E "assert \(?\s*\"[^\"]{25,}\"\s*\)?\s+in\b"; done`
verdict: open

The orchestrator is about to post the count on #1111 with these records as
its source. `phase-2.md:148-149` says "How the issue reached 182 is not on
record here. The owner, who wrote the figure, answers that", and
`gaps.md:23` lists it under `## Not verified` with the owner as answerer.
`phase-2.md:146-147` adds "no line count gives 182 either".

The issue body states the command under *Where it stands*:
`grep -h -E 'assert \(?\s*"[^"]{25,}"\s*\)?\s+in\b' -r tests/<dir> | wc -l`
at `0b75346f`. Run per file over `tests/text` at `0b75346f` and summed, it
gives 182. That is 174 in the 39 modules, plus 8 in the contract module.
Over the 39 modules at `ee746f3b`, it gives 168. The pattern counts a line
only where an assert opens with a literal of 25 or more characters. It does
not count shorter literals such as `never`, `two` or `hand-back`, a second
literal on the same line, or a literal on the line after the `assert`. The
method counts all of these, so 182 bounds nothing. The divergence is real,
and the reason is on record. A question sent to the owner and posted on
the issue would ask the owner for something the issue already shows.

Replace `phase-2.md:144-149` with:

```markdown
- **The issue's 182 does not bound the count.** `frame/design.md` says the
  issue's rough figure of 182 bounds the count from above. The issue
  states its command: `grep -h -E 'assert \(?\s*"[^"]{25,}"\s*\)?\s+in\b'
  -r tests/text | wc -l` at `0b75346f`. Run per file there, it gives 182,
  and over the 39 modules at `ee746f3b` it gives 168. It counts one line
  per assert that opens with a literal of 25 or more characters. The method
  also counts shorter literals, a second literal on one line and a literal
  wrapped onto the next line, so under it 255 literals count, and 182
  bounds nothing.
```

In `gaps.md`, the grounds cell of the row *The bound on the count* reads:

```markdown
The method as written. The issue's own grep counts only an assert that opens with a literal of 25 or more characters: 182 at `0b75346f`, 168 over the 39 modules at `ee746f3b`. The method counts shorter literals too, so 182 is no bound on it
```

Delete the `## Not verified` row *How the issue reached its rough figure of
182*.

answer:

### 4. Phase 2 describes "field or marker" as every table-cell value, yet counts three table cells as phrase pins, so a re-derivation from that description gets a different number

severity: should
location: `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/trail/phases/phase-2.md:124-130`
evidence: executed `python3 -I test_tmp_pin_sample.py <worktree> ee746f3b test_review_axes.py`, `git grep -n "still a sentence"`
verdict: open

`phase-2.md:124-125` says "*Field or marker* holds table separators and
table-cell values". The count applies a narrower rule, and that rule is the
frame's. The cells it leaves out are ones a checker or a script reads. One
is `| still a sentence |` at `test_broad_gate_rule.py:403`, a word
`tests/behaviour/test_every_orchestrator_act_names_its_delivery.py:106`
matches. Others are the bar cells at `test_the_handoff_before_round_one.py:252`
and `:256`. The axis-table cells that `test_review_axes.py:16`, `:31` and
`:138` assert are counted, and that is right under the frame, since no
checker reads them. `test_review_axes.py` then counts 10, which this round
re-derived.

S8 of `frame/design.md` has the sealer re-derive one module's number. A
sealer that takes the description as written and picks
`test_review_axes.py` leaves out three more cells. It gets 7, and withholds
over a count that is right. The sentence is one an agent acts on.

Replace the sentence's first clause, so that `phase-2.md:124-130` reads:

```markdown
  own output. *Field or marker* holds a separator row, a table cell a
  checker or a script reads (the cells at the lines listed under that kind
  above), the verdict spellings `fixed <commit>` and `deferred <where it
  was repaired>`, the labels `executed`, `read` and `unverified`, the
  `Seal-Routing` trailer, an HTML marker, the `reopens:` field, a GitHub
  label, and the bar values that
  `tests/text/test_the_handoff_before_round_one.py` checks against
  `session_cost.py`. A table cell no checker reads, such as the axis rows
  at `test_review_axes.py:16`, `:31` and `:138`, is prose, and it counts.
```

answer:

## Confirmations

confirms: none
This is round 1. No earlier round exists, so no fact was carried. Every
fact below was established this round.

confirms: none
The issue's first *Done when* holds. `FACTS`
(`tests/text/test_the_agent_contract_holds_the_universal_rules.py:43-56`)
writes the fact beside its spellings for the two pins kept: rules 1 and 11.
`PINS`, `FOUR_RULES` and the seven phrase cases are gone, as
`frame/design.md` *The module's other phrase cases* decides. The 13
`check:` lines changed to the readers in *Each pin, decided*. The module is
named on the lines of rules 1, 8 and 11 and no other (S6, executed
`grep -n '^check:' skills/agent-contract/SKILL.md`). No name the change
removed is cited anywhere in the tree (executed `git grep` over the ten
removed names). Read.

confirms: none
The new cases read what they claim. `rules_without_one_check_line` counts
lines that open with `check: ` under the settle grammar
(`skills/settle/SKILL.md:102-103`). No other module reads whether a
contract rule carries the line: the five importers use `HEADING` only to
split sections, and `.github/scripts/rules.py` cannot read it, as
`skills/settle/SKILL.md` *What this plugin checks* says. So the new case
duplicates nothing in its group. The move case keeps `text[end:]` now.
Phase 1's claim that the case at base dropped sections 16 to 20 holds by
reading the removed lines. The docstring rewrite at
`tests/text/test_the_handoff_before_round_one.py:106-110` names the rows at
`:79-81` correctly: contract rules 1, 12 and 6. Read.

confirms: none
The survivors t4 and t6 hold for the reasons `phase-1.md` gives. Each kept
spelling occurs once in the contract (executed `grep -c`: 1 and 1), so a
reader of the whole file and a reader of the body agree under deletion. t3
kills the same break through the move case. t6 removes an entry of the
input list, and no case can watch its own inputs. Read and executed.

confirms: none
The count's candidates re-derive. Over all 39 modules at `ee746f3b`, an AST
listing of every assert comparison with a string literal or f-string on the
left gives 382 `in` and 75 `not in`, the same as phase 2. Six modules were
re-decided by reading each literal beside its source: the two largest
(`test_a_segment_feeds_the_flow_log.py` at 32, `test_broad_gate_rule.py` at
31), then `test_settle_reads_before_it_removes.py` at 25,
`test_the_handoff_before_round_one.py` at 24, `test_review_axes.py` at 10
and `test_a_question_says_who_can_answer_it.py` at 11. Each matches phase
2's number and its left-out lines by kind. In the sample, the left-out
kinds are applied as the frame states, plus the command kind. Executed and
read.

confirms: none
The command kind (24 left out, 279 if they counted as prose) is a
divergence `gaps.md` records with its grounds. The grounds are
`frame/questions.md` judgment 2, the same test that keeps rule 1's command
forms. The sampled commands are commands, such as `gh issue comment` and
`--body-file`, and a sentence that contains a command is counted as prose.
Read.

confirms: none
`gaps.md` holds the `# Overview:` heading and the sections the ladder's
overview test reads. Its claims were checked against the tree. Findings 3
and 4 cover the two that do not hold, and the rest held. Read.

confirms: none
The suite is labelled `unverified` and given to the orchestrator, which is
honest. `.test_durations` lacks prices for 6 collected ids and still holds
47 entries for ids no longer collected, against 6774 priced entries
(executed). `STALE_SHARE` is 0.05
(`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:90`),
so this branch alone is far under both shares. Whether the whole suite is
under them is the broad gate's question.

confirms: none
The checks the caller named, run narrow through `bin/test -q`, each exit 0:
the contract module (29), the five `HEADING` importers (5, 5, 23, 221, 17),
`tests/github/test_rules.py` (59), and every module `git grep -l` finds
naming a changed `tests/` path:
`tests/text/test_the_handoff_before_round_one.py` (13),
`tests/text/test_a_language_section_of_writing_style_opens_alone.py` (2)
and `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py`
(4). Two more read the contract's `check:` lines and were run too:
`tests/behaviour/test_docs_line_wrap.py` (39) and
`tests/text/test_every_agent_reads_the_contract.py` (22).
`bin/seal layout --check` exits 0. `bin/seal rules --check` exits 0, with
"all 266 check lines in 55 rule files hold". Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck, including `test_the_durations_file_prices_the_suite` | the branch at `951f316b` | the orchestrator, through `seal gate` |
| Whether the eval cases now named by rules 2 and 7 pass on a run, and those named by 4 and 15 unless finding 2 moves them | `evals/behaviour/sealer/`, `evals/behaviour/crafter/` | the orchestrator, at the next preload rewrite that runs the behaviour evals |
| Rule 2's case reads one agent and one command spelling, `seal gate --base`. A sealer that runs the full suite through `bin/test` passes it. Whether that partial reach is enough for rule 2 | `evals/behaviour/sealer/rule-sealer-no-gate/graders/shape-runs-no-broad-run.md` | the owner |
| `frame/questions.md` Q1 and Q2 stand on their defaults with Status `open` | `frame/questions.md` | the owner |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_pin_sample.py <worktree> ee746f3b` over six modules (the probe at `<scratchpad>/1793226630-most-contract-rules-are-proved-by-their-own-wording/round-1/`, run then deleted) | `in` and `not in` candidates: flow log 44 and 13, broad gate 43 and 4, settle 42 and 24, handoff 39 and 1, review axes 15 and 3, question 13 and 2. Each equals phase 2's counted, left-out and Q2 columns summed |
| the same probe over all 39 modules | 382 `in`, 75 `not in` |
| the issue's grep, per file over `tests/text`, at `0b75346f` and at `ee746f3b` | 182 (174 without the contract module) at `0b75346f`; 168 at `ee746f3b` |
| `bin/test <module> -q` over the twelve modules in *Confirmations* | each exit 0 |
| `bin/seal layout --check`; `bin/seal rules --check` | exit 0; exit 0, "all 266 check lines in 55 rule files hold" |
| `bin/test tests/text/test_the_agent_contract_holds_the_universal_rules.py --collect-only -q`, compared with `.test_durations` | 29 collected, 6 unpriced, 47 priced entries no longer collected, 6774 priced in all |

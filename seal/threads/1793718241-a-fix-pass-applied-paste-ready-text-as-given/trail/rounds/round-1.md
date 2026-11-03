# Review round 1: 1793718241-a-fix-pass-applied-paste-ready-text-as-given

```seal
target: b3c819edf against release/v0.31.0
```

No earlier round exists, so nothing is carried from one. The review read
the diff `b47104fa6..b3c819edf` whole: the seven files outside `seal/` and
the work item's records. Every verdict below is this round's own, reached
in a `git clone --no-local` at `b3c819edf`.

## Findings

### 1. The sealer's exception and the two citing skill sentences give rule 15's guard red to every case that passes before the change, where rule 15 gives it to a case that asserts an absence

```seal
severity: should
location: `agents/sealer.md:145-148`, `skills/verify/SKILL.md:43-45`, `skills/implement/SKILL.md:164-166`, `seal/threads/1793718241-a-fix-pass-applied-paste-ready-text-as-given/changelog.md:4`, `seal/threads/1793718241-a-fix-pass-applied-paste-ready-text-as-given/changelog.md:11`
evidence: read `skills/agent-contract/SKILL.md:183-190`, `agents/sealer.md:145-148`, `skills/verify/SKILL.md:43-45`, `skills/implement/SKILL.md:164-166`, `seal/threads/1793718241-a-fix-pass-applied-paste-ready-text-as-given/changelog.md:4`, `seal/threads/1793718241-a-fix-pass-applied-paste-ready-text-as-given/changelog.md:11`
```

Why it matters: contract rule 15 is the one source of the guard red, and it
gives that red to one class of case. At `skills/agent-contract/SKILL.md:183-186`
the class is "A case that asserts something is not named, counted, read or
let through". For every other case, the rule's last sentence holds
(`:188-190`): "A case that passes against the defect it was written for
pins nothing". The three sentences that cite the rule name a wider class.

- `skills/verify/SKILL.md:43-45` reads "a new test that passes there, such
  as one asserting that nothing is named, is shown red the way contract rule
  15 states". The class is every new test that passes against the
  pre-change code, and the absence case is only its example. A crafter at a
  completion claim reads that any test passing at the base has a rule-15
  red. Rule 15 gives such a test no red unless it asserts an absence.
- `skills/implement/SKILL.md:164-166` reads "A case that is already green
  against the tree as it stands, such as a case asserting that something is
  not named, takes its red from contract rule 15". The class is the same,
  and so is the example's role.
- `agents/sealer.md:145-148` reads "A case that passes there was never red,
  unless its record says it was shown red with its named guard alone
  removed (rule 15)". The exception is keyed on the record's claim alone.
  A phase record can claim a guard red for a case that asserts no absence
  and passes at the base, and the sealer then re-runs it with a line of
  HEAD's code removed. A case that goes red there still passes against the
  defect it was written for, so rule 15 says it pins nothing. The sealer
  accepts it, and that case is what its *A `seen red` is re-run against the
  code before the change* paragraph exists to refuse.

The work item's records state the same wide class. The changelog's
`### Changed` entry ends "cite rule 15 for a new case that passes before
the change" (`changelog.md:4`), and its second process row ends "cite rule
15 for a case that passes before the change" (`changelog.md:11`). The
release note is built from that text. The class also comes from the frame:
`frame/design.md` *Scope* items 3 to 5 (`:34-36`) and S5 (`:61`) draft it this
way. So the build followed the frame. The route for a defect the frame
holds is the orchestrator's, by `skills/code-review/orchestration.md`
*A regression is routed by comparing the fix with the frame*. Folding those
frame cells to the narrower class is the orchestrator's act, and the
snippet below does not reach them.

The snippet below covers the three shipped sentences and the two changelog
lines. It also orders the sealer's guard re-run before the clone is
removed. The paragraph's first sentence removes the clone after the base
run, and "re-run in the clone" otherwise names a clone that is gone. It
leaves the frame cells named above to the orchestrator. After applying it, the fix
pass runs `tests/text/test_no_passage_is_pasted_into_a_second_file.py` and
`tests/behaviour/test_docs_line_wrap.py`. The three sentences share the run
"that something is not named, counted, read or let through", ten words
long, and that module refuses fifteen.

```text
agents/sealer.md, the sentences after "never change the tree under audit.":

A case that passes there was never red,
unless it asserts that something is not named, counted, read or let
through and its record says it was shown red with its named guard alone
removed (rule 15). Such a case is re-run in the same clone, before it is
removed, with HEAD's code restored and that guard alone removed, and its
failing line is read for that guard.

skills/verify/SKILL.md, 2. Able to fail, the new-test sentence:

For a new test: it was
observed failing against the pre-change code, and a new test asserting
that nothing is named, counted, read or let through, which passes there,
is shown red the way contract rule 15 states.

skills/implement/SKILL.md, 2. Implement test-first, the sentence after the
bold cadence:

A case asserting that something is not named, counted, read or let
through is already green against the tree as it stands, and takes its
red from contract rule 15.

changelog.md:4, the last clause:

... cite rule 15 for such a case.

changelog.md:11, the last clause of the Change cell:

... cite rule 15 for such a case |
```

```seal
verdict: fixed 533801c30
answer: The finding holds. Rule 15 at `skills/agent-contract/SKILL.md:183-190` gives the guard red only to a case that asserts something is not named, counted, read or let through, and the three citing sentences gave it to every case green before the change. Before applying the paste-ready text, I read it against rule 15, the paragraph around each coordinate and the paste and line-wrap cases. The sealer's text is applied with one change: the paragraph's first sentence no longer removes the clone, and a sentence after the guard re-run says "Remove the clone once its runs are done". The snippet's "before it is removed" left the first sentence ordering the removal before the re-run, and its "it" could be read as the case. The verify and implement sentences are my own words, because the snippet's wording claims that every such case passes before the change. Rule 15 says such a case passes against old code that does none of the four acts, and a case can assert an absence that the old code still violates. So verify reads "except that a new test asserting that nothing is named, counted, read or let through, where it passes there, is shown red the way contract rule 15 states", and implement reads "A case asserting that something is not named, counted, read or let through that is already green against the tree as it stands takes its red from contract rule 15". The two changelog clauses are applied as given, and the `### Changed` entry's sealer sentence now says the re-run is in the clone with HEAD's code restored. Every citation of rule 15 under `agents skills docs templates CONTRIBUTING.md README.md` was listed with `git grep -n "rule 15"`, which prints the three fixed lines and no other. Contract rule 15 itself is the fourth statement. The 106-module boundary set passed at 533801c30: 5222 passed, 12 skipped, exit 0. `frame/design.md` *Scope* items 3 to 5, S4 and S5 and `trail/phases/phase-1.md`'s paragraph on the verify clause still state the wider class or the old wording. Those are the framer's and phase 1's records, and are left for the orchestrator to fold.
```

## Confirmations

```seal
confirms: none
```
What matched: `frame/design.md` *Scope* item 1 at `agents/crafter.md:167-177`.
The crafter's paragraph says a spawn prompt or a judgment row that tells
the fix pass to apply a paste-ready fix names the fix and does not waive
the reading. It says the reading is against `frame/design.md`, the phase's
`frame/plan.md` row and every input the code hands the unit, and it keeps
the procedure-step reading, the release sentence and the own-words
sentence. The phase record claimed two departures from the frame's draft.
"without waiving the reading below" is one: `agents/crafter.md:169` points
at the next sentence. "the `frame/plan.md` row of the phase that built it" is
the other: a fix pass has no phase of its own, so the row is the phase's
that built the unit. Each holds as read. This answers the issue's first
*Done when* item. The issue's "with every sentence it leaves standing read
too" stands at `agents/crafter.md:183-185`, as `frame/design.md` G4 says
(read).

```seal
confirms: none
```
What matched: the crafter's claim that each changed clause of the pin was
seen red with its sentence deleted. This round re-ran the four mutants with
`bin/seal mutate agents/crafter.md` over `bin/test
tests/text/test_a_moved_rule_leaves_its_definition.py -q -p no:xdist -k
test_the_crafters_fix_pass_appends_a_close_block`. The baseline passed and
4 of 4 mutants went red (executed). Which line fails is read from
`tests/text/test_a_moved_rule_leaves_its_definition.py:465-504` (read). Each
clause is its own assertion whose message names that clause, and each
mutant deletes text that only its own clause holds, so the first assertion
to fail names the deleted clause. The unchanged clauses for the release
sentence and the own-words sentence pass at HEAD (S2, executed in the
narrow run below). A mutation score licenses *tested* here, not *safe*.

```seal
confirms: none
```
What matched: contract rule 15 at `skills/agent-contract/SKILL.md:181-190`
says what `frame/design.md` *Scope* item 2 asks (read). An absence case is
shown red with only its named guard removed, and its failing line is read
for that guard. A case kept green by a second guard pins nothing of the
guard it names, and so does a case failing on a line that names something
else. The catch names both forms. This answers the issue's second *Done
when* item. The first sentence's two forms and "say in the hand-back how
it was shown" stand.

```seal
confirms: none
```
What matched: the phase record's departure on the sealer's re-run place.
It claimed "re-run in the clone at HEAD's code" in place of the frame's
"re-run at HEAD", on the grounds that the same paragraph says "never change
the tree under audit". `agents/sealer.md:145-148` holds both (read), and
the frame's wording would have the sealer remove a guard from the tree it
audits. The ordering of that re-run against the clone's removal is part of
finding 1's snippet.

```seal
confirms: none
```
What matched: `frame/plan.md` *Judgments of the run* row 1 and the frame's
S5, S6 and S7 as folded at `b3c819edf`. All three were executed at HEAD.
`git grep -n '(rule 15)' -- agents/sealer.md` printed one line,
`agents/sealer.md:147`. `git grep -n 'contract rule 15' -- skills/verify/SKILL.md
skills/implement/SKILL.md` printed one line in each. `git grep -n 'takes the
snippet as the repair' -- . ':!seal/'` printed nothing and exited 1.
`git diff --stat b47104fa6...HEAD -- ':!seal/'` printed 7 files changed.
The `(rule 15)` spelling is the one `skills/writing-style/SKILL.md:263-264`
gives a definition under `agents/` (read).

```seal
confirms: none
```
What matched: `frame/design.md` *Scope* item 6 at
`skills/code-review/SKILL.md:171-174`. The reason now reads "A fix pass that
finds the snippet holds applies it as the repair", and the rest of the
paragraph stands (read). The sentence agrees with `agents/crafter.md:167-177`.

```seal
confirms: none
```
What matched: the claim that no mechanism is added, and that the frame's
choice to build no check is grounded. The diff adds no script, hook, eval
or check line (executed, the diff stat above). *Scope* item 9 and
`frame/plan.md` *Alternatives considered* rows 2 and 3 ground the choice in
`skills/core/SKILL.md` *The rule a mechanism is kept against* (read). The
`gaps.md` row asked the proofer whether a case reads the new sentences. It
holds that none does: `git grep` over `tests evals` for six phrases of the
new sentences printed nothing and exited 1 (executed). Rule 15 carries no
`check:` line, and `skills/implement/SKILL.md:172-173` says such a rule is
read by review, which this round did, finding 1 among the results. The
sealer paragraph's `check:` target, `evals/behaviour/sealer/rule-sealer-false-red/`,
keeps its path. Its fixture's phase record claims a red "against the code
before the change", not a guard red
(`evals/behaviour/sealer/rule-sealer-false-red/scaffold.sh:143-146`, read).
So the new exception does not apply to it, and the expected `withheld`
verdict stands as read.

```seal
confirms: none
```
What matched: the crafter's rule-12 account of the other statements of the
two old facts, and its label. It called its list a sample, as rule 12
asks. This round ran a wider search of its own over `skills agents docs
templates hooks CONTRIBUTING.md README.md bin`, with the spellings listed
under `## Probes` (executed). It found no other sentence stating that a
fix pass takes a paste-ready text as the repair, or that a new case's red
comes only from the old code. `agents/crafter.md:114-118`,
`skills/verify/SKILL.md:292`, `CONTRIBUTING.md:350` and `README.md:610`
stay true (read). The spellings form an unbounded domain, so this list is
a sample too. Its open part stays with the next round and the sealer.

```seal
confirms: none
```
What matched: S8, the narrow cases that read the edited files. `bin/test -q
tests/text/test_a_moved_rule_leaves_its_definition.py
tests/text/test_no_passage_is_pasted_into_a_second_file.py
tests/behaviour/test_docs_line_wrap.py
tests/text/test_the_agent_contract_holds_the_universal_rules.py
tests/text/test_every_agent_reads_the_contract.py` gave 282 passed, exit 0
(executed). The phase record claimed the verify clause and the implement
sentence share no fifteen-word run, and the passage module's pass confirms
it. No test function is added, so no new test is read against its group.

```seal
confirms: none
```
What matched: the changelog fragment's `### Changed` entry beside the
process rows. The phase record grounds it in
`docs/layout/the-record-layout.md:111`, which makes `changelog.md` the work
item's entry in the release notes. Every other open work item's fragment
carries the same two headings (executed, a loop over
`seal/threads/*/changelog.md`). `## Process changes` is owed because the
diff changes `agents/*.md` files (`docs/layout/the-record-layout.md:52`,
read). Two clauses of the fragment carry finding 1's class.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The crafter's 106-module boundary run, 5222 passed and 12 skipped. This round ran the five modules S8 names and not the rest. The suite stays `unverified` until the broad run at HEAD | `trail/phases/phase-1.md`, *The boundary run* | the orchestrator, at its broad run |
| `evals/behaviour/sealer/rule-sealer-false-red/` was not run, since an eval is a paid run. Its fixture was read, under *Confirmations* | `agents/sealer.md:152` | the orchestrator, where the release runs the sealer's evals |

## Probes

| Command | Result |
|---|---|
| `bin/seal mutate agents/crafter.md` with four `--replace` pairs deleting each changed clause, `--tests "bin/test tests/text/test_a_moved_rule_leaves_its_definition.py -q -p no:xdist -k test_the_crafters_fix_pass_appends_a_close_block"` | baseline passed; mutants 1 to 4 red, exit 1 each; `4 mutants, 4 red, 0 SURVIVED`; the clone's `git status --short` printed nothing afterwards |
| `bin/test -q` over the five modules S8 names | 282 passed, exit 0 |
| `git grep -n -i -E` over `skills agents docs templates hooks CONTRIBUTING.md README.md bin`, with `.ko.md` files left out, for `paste-ready`, `paste ready`, `as given`, `as written`, `applied as`, `apply the (round\|proposal\|snippet)` and `the snippet` | the hits the confirmation above names, `skills/code-review/orchestration.md:205-206`, `docs/running/the-run.md:36`, `docs/forms/the-round-record.md:57` and form or code lines that state no reading of a paste-ready fix |
| `git grep -n -i -E` over the same roots for `seen red`, `shown red`, `observed failing`, `seen failing`, `pre-change`, `old code`, `before the change`, `go(es)? red`, `went red`, `red against`, `never red`, `red first`, `red-first`, `been red`, `passes at (the )?base`, `revert(ing\|ed)? the fix`, `mutant` and `guard (alone\|removed)` | the four rewritten sentences, and the coordinates the confirmation above names as staying true; no other statement of a new case's red |
| `git grep -n -e 'named guard alone' -e 'counted, read or' -e 'takes its red from' -e 'shown red the way' -e 'finds the snippet holds' -e 'never red' -- tests evals` | nothing, exit 1 |
| `python3 skills/code-review/scripts/chain_check.py --baseline b47104fa6 --root . --worktree`, in the clone before this record | exit 0; no notice at a line of `frame/design.md` |

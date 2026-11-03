# Review round 2: 1793726048-the-stop-judgment-holds-against-later-rows

```seal
target: 2fa32833a, fixes d7087a3ce..2fa32833a
```

This verifying round read the diff of the last fixes, `d7087a3ce..2fa32833a`, in a `git clone --no-local` of the main clone at `2fa32833a`, made in the round's scratch directory and removed before hand-back. The diff holds three commits: the fix pass at `89480ded9`, the orchestrator's fold of the frame at `679d00927`, and round 1's close blocks at `2fa32833a`. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` holds no `Record language` row, so the record is English. The diff adds no test, so *Each new test is read against its group* had nothing to read.

Carried from round 1, not re-established: the base ranges of the stop paragraph and the proofer rule (round 1's third confirmation), the location of #1216's round 5 record at `v0.28.0`, and that `skills/settle/rule-changes.md:79` lets a rule no case holds carry no check line. Re-derived this round: every verdict below, and each claim of the spawn prompt named under `## Confirmations`. Round 1's finding 1 is closed `deferred frame/design.md ## Rule changes, the orchestrator's fold`. It stands deferred there, and this round names whether the fold answers it in a confirmation, without writing it up again.

This round opens two findings, both `should`, and no `must`. Finding 1 is a regression in the bullet finding 4's fix rewrote. Finding 2 is in the frame records the fold changed, and its fix touches only the work item's records.

## Findings

### 1. The rewritten bullet states that every test of a moved helper holds no fact the frame states, one sentence after defining such a case by what its assertions hold

```seal
severity: should
location: `skills/code-review/SKILL.md:132-141`
evidence: read `skills/code-review/SKILL.md:132-141`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:42`
regression: round-1#4
```

The unit is the bullet of `skills/code-review/SKILL.md` *The record* that opens "A case that holds no fact the frame states", which `89480ded9` rewrote at `:132-141`. The frame's *Scope* item 3, first point (`frame/design.md:42`), defines such a case by the behaviour its assertions hold and gives a moved helper's test as an example, "such as a test of a helper the work moved or wrote beside its *Scope*"; the fix applied round 1's paste-ready sentences as given and turned that example into a rule, "A test of a helper the work moved, or wrote beside its *Scope*, is such a case"; the defect came from how round 1's paste-ready fix was written.

Why it matters: the bullet now holds two tests that disagree on one case. At `:133-136`, a case is such a case when its assertions hold no behaviour that a *Scope* item, an acceptance row or a `check:` line states. At `:136-137`, a test of a helper the work moved is such a case, with no condition. Take a moved helper whose behaviour an acceptance row states, and a test of it. By the first sentence it holds a fact the frame states, so a gap in it is weighed as any gap. By the second it is such a case, so the gap "is not a `should` by default". The closing exception does not settle it: a moved helper's behaviour is one the diff did not change, so "a behaviour the diff changed that no case then holds" does not reach it. A proofer acts on this bullet at every round to decide whether a finding opens, so the sentence is a `should`.

Claimed (round 1's close of finding 4): the sentences were applied as given after reading them against *Scope* item 3's first point and S5. The phrase "is such a case" stands in round 1's paste-ready snippet (`trail/rounds/round-1.md`, finding 4), so the claim is true. The frame's wording is "such as", which this round reads as an example under the definition.

The statements of the definition, listed by taking apart the files that state it: this bullet, *Scope* item 3's first point, the changelog fragment's second bullet and its second *Process changes* row, and `agents/proofer.md:139-141`, which cites the bullet. Only the bullet makes the example a rule, so the fix touches it alone. The fix restores the frame's "such as" and rewraps the lines it touches to the same width:

```markdown
- A case that holds no fact the frame states is weighed by what the release
  ships without the fix. Such a case is one whose assertions hold no
  behaviour that a *Scope* item, an acceptance row or a `check:` line of a
  rule the diff changes states, such as a test of a helper the work moved
  or wrote beside its *Scope*. A fact that only a *Grounding* row states
  does not count. A parameter in it that pins nothing, a guard in it of
  code the diff did not change that no case pins, or a comment or name of
  it that claims more than it pins leaves the code as the frame says. So
  such a gap is not a `should` by default, and the round opens no finding
  for it. A comment and
```

The snippet replaces `:132-141`, whose last line ends "opens no finding for it. A comment and". The line after it, `:142`, opens "a name of such a case" and stays as written. `tests/behaviour/test_docs_line_wrap.py` reads the width, and the fix pass runs it.

```seal
verdict: fixed bffc022d6
answer: The finding holds: round 1's paste-ready "is such a case" made the frame's example a rule beside the definition, and round 1's fix pass applied it as given. This pass read round 2's snippet against *Scope* item 3's first point and the bullet before it and did not apply it as given. Its "such as a test of a helper the work moved" still lists that test under the definition without its condition, so the moved helper whose behaviour an acceptance row states, the case this finding names, would read two ways again. The bullet now keeps the example and states its condition, in this pass's own words: "A test of a helper the work moved, or wrote beside its *Scope*, is such a case only where no *Scope* item, acceptance row or `check:` line states what the helper does." The next sentence opens "A parameter in such a case", because "it" would otherwise refer to the helper. The bullet's lines from there to "bullet above." are rewrapped, and `tests/behaviour/test_docs_line_wrap.py` with `tests/text/test_the_rules_have_one_owner.py` exited 0 (executed). The changelog fragment and `agents/proofer.md:139-141` state no example and needed no change.
```

### 2. The fold added entries and points to the frame and left the counts and ordinals that name them, so two *Removes* rows point at the wrong `change`

```seal
severity: should
location: `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:21`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:71`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:77`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:112-116`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/plan.md:15`
evidence: read `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:85-116`, `agents/sealer.md:80-88`
```

The units are cells and sentences of `frame/design.md` and `frame/plan.md` that `679d00927`, the orchestrator's fold, added or left beside what it added. That commit is the orchestrator's amendment of the frame, recorded as row 2 of `frame/plan.md` *Judgments of the run*, and not a fix pass's commit, so this finding carries no `regression:` line.

Why it matters: `## Rule changes` now holds three `change` entries, in this order: the homes sentence at `docs/running/the-run.md:48`, the cap sentence at `:12-14`, and the routing sentence at `:28-30`. The fold's two new *Removes* rows name them by position, and both positions are wrong:

- `frame/design.md:113`, the cap row, says "the first `change`". The cap change is the second entry (`:93-97`).
- `frame/design.md:114`, the routing row, says "the second `change`". The routing change is the third entry (`:99-103`).

`agents/sealer.md:82-84` has the sealer confirm, for every `## Removes` row, that nothing of it stands in the tree, and step 4 (`:86-88`) has it read the design's *Removes* against the build. A sealer that opens "the first `change`" for the cap row finds the homes sentence, which does not remove the cap. So the record points the last independent party at the wrong entry, and the sentence is a `should`.

The same fold left other statements of the old counts. Each is wrong, and the fix pass owes them with the two rows:

- `frame/design.md:112`, the homes row, still says "the `change`", which named one entry and now names none of three.
- `frame/design.md:116` says "it narrows the three rules above ... and the rule change narrows the fourth". The table now has six rows and the section three entries.
- `frame/design.md:71`, S1's *Verifiable how*, says "item 1's six points". *Scope* item 1 now says "seven things" (`:32`).
- `frame/design.md:21`, G13, says the work "states its one change to the policy root".
- `frame/design.md:77`, S7, says "for its `change`", and `frame/plan.md:15` says "with that `to`", each in the singular.

The method: the fold grew three counted sets, *Scope* item 1's points (six to seven), `## Rule changes` (one entry to three) and `## Removes` (four rows to six). This round read every sentence of `frame/design.md`, `frame/plan.md`, `changelog.md`, `gaps.md` and `trail/phases/phase-1.md` that counts or orders one of them, found by a search for "points", "things", "`change`", "`to`", "rule change", "rules above" and "fourth". `trail/phases/phase-1.md:43`'s "six points" is the phase's record of what it built, and it stays true. So the list is whole for these three sets and these five files.

The fix, each line in place:

```markdown
G13, at `frame/design.md:21`: "so it states its one change to the policy root in `## Rule changes` for the settle"
becomes "so it states its changes to the policy root in `## Rule changes` for the settle"

S1, at `:71`: "read by the round against item 1's six points;"
becomes "read by the round against item 1's seven points;"

S7, at `:77`: "and prints no pin notice and no copy notice for its `change`"
becomes "and prints no pin notice and no copy notice for any of its `change` entries"

*Removes*, at `:112`: "| the `change` in `## Rule changes`, written by the settle |"
becomes "| the first `change` in `## Rule changes`, written by the settle |"

*Removes*, at `:113`: "| the first `change` in `## Rule changes`, written by the settle |"
becomes "| the second `change` in `## Rule changes`, written by the settle |"

*Removes*, at `:114`: "the second `change` in `## Rule changes`, written by the settle |"
becomes "the third `change` in `## Rule changes`, written by the settle |"

`:116`: "In return it narrows the three rules above, which pulled the other way in #1216's run, and the rule change narrows the fourth."
becomes "In return it narrows the first three rules above, which pulled the other way in #1216's run, and the three `change` entries narrow the other three, the last of them together with *Scope* item 1's seventh point."

`frame/plan.md:15`: "must share no run of 15 words with that `to` (S7)."
becomes "must share no run of 15 words with any of those `to` values (S7)."
```

Where the fix stops: `## Rule changes` itself is not touched, so `rule_changes.py` reads the same three entries. The fix touches only the work item's records, so the round that reads it is the sealer, by the table of `skills/core/SKILL.md` *Judgment is not licence to skip a party*.

```seal
verdict: fixed 71078b4cb
answer: The finding holds; the miscount was the orchestrator's own fold at 679d00927, so the orchestrator answers it in the records. Each *Removes* row now names its `change` by the opening words of its `from`, which leaves no ordinal to drift as entries are added, and G13, S1, S7, the closing paragraph of *Removes* and `frame/plan.md` *Technical context* count three changes and seven points. `## Rule changes` itself is unchanged. `frame/plan.md` *Judgments of the run* row 3 records it.
```

## Confirmations

```seal
confirms: round-1#2
```
What holds: the stop paragraph and the route section's lead now agree. Read: `skills/code-review/orchestration.md:175-179` says a finding with a `regression:` line is no exception, and that from the stop row on a `must` alone is routed and every other regression takes a home, never the framer. `:233-236` says that once a row has judged the run excessive, only a `must` takes a route below. So the third route row (`:242`) no longer sends a `should` to the framer after a stop, and S1's then-clause holds. The policy root's statement at `docs/running/the-run.md:28-30` is the third `change` of `## Rule changes` (`frame/design.md:99-103`). Executed: `rule_changes.parse` read three entries with no error, and `apply_op` placed each in `docs/running/the-run.md` in memory; the result of the third reads "only a `must` takes a route, and every other regression takes a home that costs no round". Claimed: the crafter moved the sentence from where round 1 put it. It stands after the sentence naming the drain row and rung 1, so "those documents" still follows the sentence it refers to. Read: the other statements of the route, `skills/code-review/orchestration.md:214`, `docs/running/the-run.md:38` and `agents/framer.md:227`, each defer to the section or the paragraph the change narrows, so none needs a change of its own.

```seal
confirms: round-1#3
```
What holds: `skills/implement/orchestration.md:480` now reads "only a `must`, or an item whose fix is confined to the work item's records, is done now". That agrees with the home the stop paragraph names at `skills/code-review/orchestration.md:167-170` and with the first `change`'s `to` (`frame/design.md:91`). The fold carried it into *Scope* item 2 (`:40`) and S4 (`:74`), read.

```seal
confirms: round-1#4
```
What holds: the bullet at `skills/code-review/SKILL.md:132-141` now defines such a case by the behaviour its assertions hold, and says "A fact that only a *Grounding* row states does not count", so S5's case reads one way. The fold carried the definition into *Scope* item 3's first point (`frame/design.md:42`), and the changelog fragment states it, read. The sentence the same fix made of the moved helper's example is finding 1, a new defect beside this close and not a reopening of it.

```seal
confirms: none
```
What matched: round 1's finding 1, closed `deferred frame/design.md ## Rule changes, the orchestrator's fold`. The fold answers it. Executed: the second `change` (`frame/design.md:93-97`) placed in memory turns `docs/running/the-run.md:12-14` into "does not count toward the three finding rounds, which mark where the orchestrator weighs a loop that is not converging and are no cap". That agrees with `skills/code-review/orchestration.md:137-138`. The *Scope* Out bullet the finding named stale (`frame/design.md:63`) now says `:13` did not stay true and that item 5 changes it, and *Scope* item 5 (`:50`) names the three coordinates. Executed: `git grep -n -i -e '\bcap\b' -e capped -- docs skills agents templates`. Its other hits name a stopped run (`agents/proofer.md:132`, `docs/forms/the-round-record.md:105`, `docs/releasing/branch-and-release.md:91`), a size or a call limit, or a title shown as an example (`docs/releasing/issues-and-milestones.md:340`). One hit stands outside both the finding and the fold: `docs/releasing/issues-and-milestones.md:4-5` calls what `docs/running/the-run.md` owns "the round cap". It is a pointer whose target stays right after the settle, so this round opens no finding for it. It is named here for the settle, which writes `docs/`.

```seal
confirms: none
```
What matched: the orchestrator's claim (executed) that `chain_check.py --worktree` at the fold printed no rule-change refusal or notice, and the crafter's claim (executed) that the two new entries share no 15-word run. Executed in the clone at `2fa32833a`: `python3 skills/code-review/scripts/chain_check.py --baseline 5005355d8 --root . --worktree` exited 0 and printed no pin notice and no copy notice. Its lines name the verifying round round 1's `fixed` closes owe, and the gate record and guarantee not yet written. Executed: `git grep` over `tests` and `evals` of "toward the cap", "cap stops", "at any round of the run", "only a `must` is done now" and "whose assertions hold" printed nothing in a test, so no case pins a sentence the fixes rewrote or the changes will rewrite. The crafter's planted copy that went red was not repeated.

```seal
confirms: none
```
What matched: the crafter's claim (read) that `agents/proofer.md:132` stays. Read: "a round told the run is capped still reports what it finds at the severity it finds it" names a run the orchestrator stopped, as `docs/releasing/branch-and-release.md:91` does, and says nothing of the three rounds as a cap. The fold's *Scope* Out bullet (`frame/design.md:63`) states the same reason.

```seal
confirms: none
```
What matched: S9 at `2fa32833a`. Executed in the clone: `bin/test` over the five modules S9 names passed, 116 cases, among them `tests/behaviour/test_docs_line_wrap.py`, which reads the width of the rewrapped bullet. This is a narrow run, not the suite.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the full suite passes at `2fa32833a`. This round ran five modules | the repository's `Broad gate` row | the orchestrator, at the broad run |
| Who makes a fix confined to the work item's records after a stop row. The drain row has "the party that builds the work item" do it (`skills/implement/orchestration.md:480`), the stop paragraph scopes "spawn no fix pass" to rungs 2 to 4 (`skills/code-review/orchestration.md:167-170`), and the new sentence on a regression says "never a fix pass" with no scope (`:179`), as *Scope* item 1's fourth and seventh points do (`frame/design.md:36`, `:39`). Every reading costs no round, which is what the stop protects, so this round opens no finding. It is the orchestrator's own act, and the orchestrator reads which one it takes | `skills/code-review/orchestration.md:179` | the orchestrator, at the next stop row |
| Q1: whether a fix that changes no assertion owes no verifying round. The build stands on the default **No** (carried from round 1) | `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/questions.md` | the repository owner |

## Probes

| Command | Result |
|---|---|
| `python3 skills/code-review/scripts/chain_check.py --baseline 5005355d8 --root . --worktree`, in the clone at `2fa32833a` | exit 0; no rule-change refusal, pin notice or copy notice; it names the verifying round owed for round 1's three `fixed` closes, and no gate record or guarantee yet |
| `python3 -I -c` importing `skills/settle/scripts/rule_changes.py`, running `parse` over `frame/design.md` and `apply_op` for each entry over `docs/running/the-run.md` in memory | three entries, no error, each placed; nothing written to disk |
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_chain_hooks_hardening.py tests/text/test_the_verifying_round_is_bounded_not_cheapest.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py -q`, in the clone | exit 0, 116 passed |
| `git grep -n -i -e 'toward the cap' -e 'cap stops' -e 'at any round of the run' -e 'run-ends-with-verifying-round' -e 'only a `must` is done now' -e 'whose assertions hold' -e 'no \*Scope\* item' -- tests evals skills agents docs` | no test holds a rewritten sentence; the rule id is read by `tests/skills/test_chain_check.py` and `tests/text/test_the_rules_have_one_owner.py` |
| `git grep -n -i -e '\bcap\b' -e capped -- docs skills agents templates` | the hits named under the confirmation of finding 1's fold |

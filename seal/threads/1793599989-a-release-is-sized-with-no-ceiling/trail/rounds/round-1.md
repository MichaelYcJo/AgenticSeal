# Review round 1: 1793599989-a-release-is-sized-with-no-ceiling

```seal
target: 2a746982 against release/v0.28.1
```

Reviewed in a `git clone --no-local` of the branch worktree at `2a746982`, against `40e6c23e`. `release/v0.28.1` does not resolve in the worktree, so every command that names the base names `origin/release/v0.28.1` or `40e6c23e`, which `git rev-parse` gives as the same commit (executed). This is round 1, so no fact is carried from an earlier round; every verdict below was reached at this target. No `seal/parity.md` is declared, so the round block holds no `original:` line.

The implementer's account, claim by claim:

- Claimed S2: no pin notice at `design.md` at `ea581e55`. This round ran `chain_check.py` over the worktree at `2a746982`, and it printed no line at `frame/design.md` (executed, `## Probes`).
- Claimed S1: one `change`, no errors, nothing unread. `rule_changes.parse` returned one op, `errors=[]` and `unread=[]`, and `apply_op` placed it with no refusal (executed).
- Claimed S3: the mutation table in `trail/phases/phase-1.md:17-21`. Not re-run by this round (read only; see `## Not judged`).
- Claimed S5: the one statement of a count is `docs/issues-and-milestones.md:32`, and the list is a sample. This round's own searches, with other spellings, found no second statement (`## Confirmations`). The crafter named the list a sample and named where its open part stands (`gaps.md:9`), as contract rule 12 asks.
- Claimed the phase-boundary run exited 0 with 1369 passed. Not re-run; this round ran three of its modules (17 passed, executed).
- Claimed in `gaps.md:13` that dropping `read`'s `root` parameter is a refactor the work did not ask for. Finding 3 answers it.

## Findings

### 1. The new paragraph sends an overflowing issue to "the next release", which the release-branch rule contradicts for a `feat:`

```seal
severity: should
location: `seal/threads/1793599989-a-release-is-sized-with-no-ceiling/frame/design.md:91-93`, `seal/threads/1793599989-a-release-is-sized-with-no-ceiling/changelog.md:3`
evidence: read `seal/threads/1793599989-a-release-is-sized-with-no-ceiling/frame/design.md:91-93`, `docs/branch-and-release.md:330`, `docs/issues-and-milestones.md:46-50`
```

Why it matters: the `to` tells whoever places an issue that, once the description is overloaded, "An issue that does not have to be in effect before the next work item starts then moves to the next release" (`frame/design.md:91-93`). `docs/branch-and-release.md:330`, in *Work accumulates on a release branch*, says the `feat:`s that share a planned minor's goal "ship together in it". It also says a `feat:` that lands in a milestone numbered as a patch moves back to the planned minor whose goal it shares. The next release after a minor is often a patch. A session that follows the new paragraph for a `feat:` therefore moves it into a milestone the other rule moves it straight back out of, and the two documents give it two answers. The old paragraph said nothing about where an issue moves, so this conflict is new with this `to`. The changelog repeats the sentence at `changelog.md:3` ("moves to the next release").

The fix replaces lines 91-93 of the `to`, from "release carries more than a reader can follow." to the end of "next release.":

```text
    release carries more than a reader can follow. An issue that does not
    have to be in effect before the next work item starts then moves to a
    later `release:` milestone, and a `feat:` moves only where
    `docs/branch-and-release.md` *Work accumulates on a release branch*
    sends it.
```

In `changelog.md:3`, "moves to the next release." becomes "moves to a later release, and a `feat:` only where `docs/branch-and-release.md` *Work accumulates on a release branch* sends it." Once the `to` changes, rerun `chain_check.py --worktree` to confirm the check line is still read and no pin is named.

```seal
verdict: fixed c72cff98
answer: The finding holds: `docs/branch-and-release.md:329`, under *Work accumulates on a release branch* (heading at `:120`), sends a `feat:` in a patch-numbered milestone to the planned minor whose goal it shares or renames the milestones forward, and no pending design changes that paragraph. `changelog.md:3` now reads "moves to a later release, and a `feat:` only where `docs/branch-and-release.md` *Work accumulates on a release branch* sends it." A fix pass does not edit the frame, so the orchestrator folds the `to`. It replaces `frame/design.md:91-93`, from "    release carries more than a reader can follow." to "    next release. The judgment counts work items rather than ticket numbers.", with these five lines: "    release carries more than a reader can follow. An issue that does not" / "    have to be in effect before the next work item starts then moves to a" / "    later `release:` milestone, and a `feat:` moves only where" / "    `docs/branch-and-release.md` *Work accumulates on a release branch*" / "    sends it. The judgment weighs work items rather than ticket numbers." These lines also carry finding 2's fix. Those words are the proofer's, and I read them as the settle and a later reader of the section would. With the five lines applied to a scratch copy of the design, `rule_changes.parse` with root `docs` returned one op, `errors=[]` and `unread=[]`, and `apply_op` placed it with no refusal, the check line still last in the paragraph (executed). The cited section stands in `docs/branch-and-release.md` (read). The same rule is stated a second time at `frame/design.md:39`, *Scope* item 1, so the orchestrator also replaces "is the one that moves, and that the judgment counts work items, not ticket numbers." there with "is the one that moves, to a later `release:` milestone and for a `feat:` only where `docs/branch-and-release.md` *Work accumulates on a release branch* sends it, and that the judgment weighs work items, not ticket numbers." `chain_check.py --worktree` is to be re-run once the orchestrator's commit is in.
```

### 2. "The judgment counts work items" puts a count back into the paragraph that removes the number

```seal
severity: should
location: `seal/threads/1793599989-a-release-is-sized-with-no-ceiling/frame/design.md:93`, `seal/threads/1793599989-a-release-is-sized-with-no-ceiling/changelog.md:3`
evidence: read `seal/threads/1793599989-a-release-is-sized-with-no-ceiling/frame/design.md:84-97`, `docs/issues-and-milestones.md:23-24`, `seal/threads/1793599989-a-release-is-sized-with-no-ceiling/frame/design.md:67`
```

Why it matters: S6 (`frame/design.md:67`) asks that a reader of the `to` "reads no number" and leaves with the judgment. After the settle, the section says at `docs/issues-and-milestones.md:23-24` that a release is sized "and not by a count". Eight lines later the `to` says "The judgment counts work items rather than ticket numbers." That sentence survives from the old paragraph, where "The count is in work items" told the reader the unit of the ceiling. With the ceiling gone it has no count to name a unit for. A session reads "counts", and then has to choose between the criterion's "not by a count" and a judgment that counts. The sentence's job is to name the unit the judgment weighs, so a verb that implies no tally keeps that job and gives the paragraph one reading. The changelog repeats the sentence.

```text
    next release. The judgment weighs work items rather than ticket numbers.
```

The line keeps its place in the `to` (line 93; its first words follow finding 1's fix if that lands first). In `changelog.md:3`, "The judgment counts work items rather than ticket numbers" becomes "The judgment weighs work items rather than ticket numbers".

```seal
verdict: fixed c72cff98
answer: The finding holds: after the settle, `docs/issues-and-milestones.md:23-24` sizes a release "and not by a count", and "counts" in the `to` gives a reader a second reading. `changelog.md:3` now reads "The judgment weighs work items rather than ticket numbers". For the `to`, the fifth of the five replacement lines in finding 1's close block ends "sends it. The judgment weighs work items rather than ticket numbers.", so the orchestrator's one fold of `frame/design.md:91-93` applies both fixes. The *Scope* item 1 sentence at `frame/design.md:39` changes "counts" to "weighs" in the replacement given there.
```

### 3. `read` keeps a `root` parameter that only the removed sweep passed

```seal
severity: should
location: `tests/behaviour/test_a_release_is_sized_by_a_criterion.py:24-26`, `seal/threads/1793599989-a-release-is-sized-with-no-ceiling/gaps.md:11-13`
evidence: executed `git grep -n 'read(' 40e6c23e -- tests/behaviour/test_a_release_is_sized_by_a_criterion.py`
```

Why it matters: at the base, `read(rel, root=ROOT)` had one caller passing `root`, `restatements` at `:153` (`read(rel, root).splitlines()`), so the sweep's temporary-repository case could point it at a scratch tree (executed). This branch removes `restatements` and that case, and the only remaining caller, `flat` at `:35`, passes no root. Design *Scope* item 3 removes "the units only they use", and `skills/core/SKILL.md` *The rule a mechanism is kept against* removes, in the same commit, "what stood on the old fact". The parameter is such a part. `gaps.md:13` gives the opposite reason, that removing it "is a refactor this work did not ask for". Scope item 3 does ask for it, and item 4 keeps `read`, not its parameter. Left in, the parameter tells the next reader that some caller reads another tree, and none does.

```python
def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()
```

The `## Not done` section of `gaps.md` (`:11-13`) goes with it, since it holds only this row.

```seal
verdict: fixed 51bfa4ed
answer: The finding holds: at `ea581e55` no caller of `read` passes `root`, and *Scope* item 3 removes the units only the sweep used. My closing memo gave the opposite reason, and it was wrong. `read` is now `def read(rel):` and opens `os.path.join(ROOT, rel)`, as the paste-ready fix gives it. Ruff check and format exit 0, and the module passes (executed). The `## Not done` heading of `gaps.md` stays, with its row replaced by `nothing`: the template's own wording for that section is "or nothing", and `skills/implement/SKILL.md` *4. The closing memo* says a memo with nothing left reads `nothing`. The decision recorded in `trail/phases/phase-1.md` stays as the build made it, because a fix pass writes no phase record. This close block is where that decision is reversed.
```

## Confirmations

```seal
confirms: none
```
What matched: S2 holds at the target. `chain_check.py --baseline origin/release/v0.28.1 --root <worktree> --worktree` exited 0 and printed no pin notice and no line at `frame/design.md`. The only lines it printed were for the round record, `trail/gate.md` and `guarantee.md`, which are not written yet (executed). No notice was printed at a design line, so this round takes no finding from a notice.

```seal
confirms: none
```
What matched: S1 holds. `rule_changes.parse` with root `docs` returned one op, `errors=[]` and `unread=[]`, and `apply_op` placed it with no refusal. In the applied document the new paragraph stands between the criterion and **What the criterion does not change.**, with its own check line before that paragraph (executed). By `.github/scripts/rules.py`'s docstring and `skills/settle/SKILL.md` *A rule has one shape*, a second check line inside one section is in grammar (read).

```seal
confirms: none
```
What matched: *Scope* items 2, 3, 4, 5, 6 and 8 hold in the diff. `SHARED_CEILING`, the ceiling's case, the sweep's six cases and their units are gone, and `re`, `build_tracked_tree`, `git_listing` and `on_disk` are no longer imported (read, `git diff 40e6c23e..2a746982`). `test_the_rule_says_what_it_does_not_change` is unchanged. The registry row at the base's `test_a_shrunken_corpus_declines_to_judge.py:72` is gone. `seal/follow-up.md` loses only the `hits()` row. `.test_durations` parses as one JSON object of 6038 keys, and its one key for the module is the remaining case (executed). `bin/test -q -p no:xdist` over the module, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` and `tests/text/test_the_release_tail_does_not_end_at_the_tag.py` exited 0 with 17 passed (executed). No name of a removed unit stands anywhere outside `seal/threads/` (`git grep` for `STATES_A_SIZE`, `restatements(`, `test_one_document_states`, `SHARED_CEILING`, `NOUN_FORMS` and `test_the_sweep_can_fail`, no hit, executed).

```seal
confirms: none
```
What matched: the rewritten module docstring (`tests/behaviour/test_a_release_is_sized_by_a_criterion.py:1-15`) describes what the case reads at `docs/issues-and-milestones.md:39-43`. It still gives the wrap-collapsing reason that `tests/text/test_the_release_tail_does_not_end_at_the_tag.py:22-27` cites "for the reason its own docstring gives", and that sentence stays true (read). It states no count and no history.

```seal
confirms: none
```
What matched: G7's measurement, which the changelog quotes, holds when the base's `STATES_A_SIZE` is read against the seven sentences. None of the five count sentences holds `release('s) sized`, `release's size`, `size of a release` or `is the size`. "the release's size" and "A release is sized" match the fourth and first alternatives (read, `git show 40e6c23e:tests/behaviour/test_a_release_is_sized_by_a_criterion.py`).

```seal
confirms: none
```
What matched: S5, re-run with spellings the crafter's three commands do not hold. A number word or digit before `work items`, `items`, `issues`, `tickets` or `pull requests` was searched for on a line naming a release, milestone, cut, size, cap or limit, over the whole tree outside `seal/threads/`. Limit phrases (`at most`, `no more than`, `up to`, `too many`, `small release`, `release cap`, `room for another`, `overload`, `grown past`) were searched for over `docs/`, `skills/`, `agents/`, `templates/` and the root documents. Guidance on moving an issue into a release milestone was searched for as well. The ten open milestone descriptions were searched through `gh api repos/MichaelYcJo/SpecSeal/milestones` (all executed). None of the hits states a count for a release's size. They are report rows, a fixture of four work items, closing-comment examples and, in `backlog: review chain & agents`, the round cap, which belongs to #1288. This is a sample of a class whose spellings are unbounded, as contract rule 12 says, and its open part is the row of `## Not judged`.

```seal
confirms: none
```
What matched: S6 holds apart from findings 1 and 2. The `to` states no number. It names who judges and what they judge against, which is whether the description can still name the one purpose its issues share and the grounds for their order. Both are what `docs/issues-and-milestones.md:46-50` already asks a release milestone's description to state, so the paragraph points at that rule and does not restate it. The `to` leaves the criterion at `:23-30` as the test of which issue moves (read, `frame/design.md:84-97` against design G1 and G9).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck; the suite is `unverified` here, as `gaps.md:7` labels it, and that label is honest | the tree at the target | the orchestrator's `seal gate --base release/v0.28.1 --record 1793599989-a-release-is-sized-with-no-ceiling` |
| S3's mutation results, which this round read and did not re-run | `trail/phases/phase-1.md:15-23` | the sealer, which samples the crafter's claims |
| A count for a release's size written in a spelling none of the searches above or G12's matches | the tree outside `seal/threads/` | the proofer of any later diff that adds such a sentence |

## Probes

| Command | Result |
|---|---|
| `git rev-parse origin/release/v0.28.1` in the worktree; `release/v0.28.1` itself | `40e6c23e63372b1254751b04bffcfd7c8cf493d6`; `release/v0.28.1` does not resolve, and `chain_check.py --baseline release/v0.28.1` exited 2 |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.28.1 --root <worktree> --worktree`, before the record | exit 0; no line at `frame/design.md`; lines only for the missing round record, `trail/gate.md` and `guarantee.md` |
| `rule_changes.parse` and `apply_op` on `frame/design.md`, root `docs`, run with `python3 -I` in the clone | one op, `errors=[]`, `unread=[]`; `apply_op` returned no refusal |
| `bin/test -q -p no:xdist tests/behaviour/test_a_release_is_sized_by_a_criterion.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py tests/text/test_the_release_tail_does_not_end_at_the_tag.py` | exit 0, 17 passed |
| `json.load` of `.test_durations` | 6038 keys; one key for the module, `test_the_rule_says_what_it_does_not_change` |
| `git grep -n 'read(' 40e6c23e -- tests/behaviour/test_a_release_is_sized_by_a_criterion.py` | callers at `:109` (`read(rel)`), `:153` (`read(rel, root)`) and `:200` (`read(OWNER)`) |
| `git grep -n -i -P` for a number before `work items`, `items`, `issues`, `tickets` or `pull requests`, filtered to lines naming a release or milestone; `git grep -n -i -P` for limit phrases over the rule files | no statement of a count for a release's size |
| `gh api 'repos/MichaelYcJo/SpecSeal/milestones?state=open&per_page=100'`, descriptions searched for counts and limit words | 10 milestones; one hit, "the cap" in `backlog: review chain & agents`, which is the round cap |

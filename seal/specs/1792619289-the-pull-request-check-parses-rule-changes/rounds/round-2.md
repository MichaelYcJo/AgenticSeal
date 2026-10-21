# 1792619289-the-pull-request-check-parses-rule-changes — review round 2

target: 06e3232f against release/v0.22.3

This round read the diff be5a9330..06e3232f. That diff holds the reframe (4fb593a8), its approval (81f607c0), round 1's fix pass (2d234e72 and 693c9a8c), phase 2 (e077c5d5 and 2a3ea1a2), and the records commit 06e3232f. It is the first finding round on the redesign. Round 1's findings 3 and 4 closed `fixed`, and both are answered under `## Confirmations`.

Round 1's findings 1 and 2 closed `deferred the frame`, as `skills/code-review/orchestration.md:134` has a redesign close them. They stand deferred. The reframe 4fb593a8 took them in: finding 1 became *Scope* item 1's second set, and finding 2 became *Scope* item 3's limit. Phase 2 built them. This round reviewed phase 2 as new work, which is how those two findings are weighed here, and it does not write them up again.

Carried from round 1, not established again: where the readers live (`chain_check.py#rule_changes_read`, `unverified_check.py#rule_changes` and `#policy_root`, `settle.py:282-286`); that `heading_level` is the plugin's one heading rule; and the b451e503 count. Every verdict below was reached on the tree at 06e3232f. `seal/parity.md` is not declared. `spec.md` cites no reference root. The owner's direction, `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*, applies as a review criterion, and finding 1 rests on it.

## Findings

### 1. The docstring and the settle pointer say every pull request's edited specs are read, while the check reads them only where a work item is declared

severity: should
location: `skills/code-review/scripts/chain_check.py:16-22`, `skills/settle/SKILL.md:79-82`
evidence: read `skills/code-review/scripts/chain_check.py:16-22`, `skills/code-review/scripts/chain_check.py:1981-1993`, `skills/settle/SKILL.md:79-82`, `seal/specs/1792619289-the-pull-request-check-parses-rule-changes/spec.md:23-37`, `tests/test_chain_check.py:2189-2200`
verdict: open

An agent decides from these two sentences whether CI will read a spec it edits. Under `[no-review]`, for example, the check reads nothing, and these sentences say it will.

Phase 2 owed this place (`plan.md` phase 2 row; `spec.md` *Scope* item 5, "each place names both sets of item 1"). *Scope* item 1 states the second set with its qualifier: "Every `seal/specs/<id>/spec.md` the pull request's own commits add or change, on a pull request that declares at least one work item" (`spec.md:30-31`). The code agrees. `main` returns at `if not declarations` before it computes `edited` (`chain_check.py:1981-1993`), and S15 (`tests/test_chain_check.py:2189-2200`) pins that a pull request declaring nothing reads no spec.

Two of the places that restate the set drop the qualifier:

- The docstring's `rule changes` arm: "and in every work item `spec.md` the pull request's own commits add or change (`edited_work_items`)" (`chain_check.py:16-22`). Nothing else in the docstring says that a pull request with no declaration reads nothing.
- The `settle` pointer: "for every work item `spec.md` the pull request's own commits add or change" (`SKILL.md:79-82`).

The two hygiene comments do not have the defect, because "It never fails for a pull request that declared nothing" stands right before their lists. The changelog does not either: "On a pull request that declares a work item, it also parses". So two of the places that state one value now state it without its condition.

```python
  rule changes  the `## Rule changes` section parses with
                `rule_changes.parse`, the one reader `settle` applies, in
                the `spec.md` of each judged work item under either
                `Planning` answer, and, on a pull request that declares at
                least one work item, in every work item `spec.md` its own
                commits add or change (`edited_work_items`); a spec with no
                such section, and a work item with no spec, pass
```

```markdown
`chain-check` asks the same reader at the pull request, for each work item
whose `routing.md` it judges and, on a pull request that declares at least
one work item, for every work item `spec.md` its own commits add or change
(`docs/the-review-record.md` *What the check reads at the pull request*).
```

answer:

## Confirmations

confirms: round-1#3
The fix holds at `skills/settle/scripts/rule_changes.py:72-94`. Probe N2 ran the old and the new reader over boundary headings. `  ## Rule Changes`, `## Rule changes` (U+00A0 between the words), `## Rule  changes`, `## *Rule changes*` and `## Rule changes (규칙 변경)` each read as no section before the fix. Each is now refused at its line, with the heading as written. `## Rule changes ##` parses under both readers, as the closing run is stripped. `tests/test_settle_applies_rule_changes_in_place.py:170` holds round 1's six near misses alone and beside the right heading, and `:189` holds the boundary of other letters. Probe N1 parsed every spec at 06e3232f (119), at `main` (117) and at `release/v0.22.3` (118) with both readers. No spec gives a different result, so the change refuses nothing at the owner's settle that it read before. That holds for `settle.py:286` and for `unverified_check.py#settled`, the reader's other caller. The class stays narrowed and not closed, as the answer says. A setext heading, a heading in a blockquote and one four spaces in read as no section under both readers. That limit belongs to the plugin's one heading rule, whose docstring states that setext headings are not read (`skills/verify/scripts/unverified_check.py:526`). Executed.

confirms: round-1#4
The fix holds at `.github/workflows/hygiene.yml:169-181` and `templates/hygiene.yml:82-94`. In both, the not-a-draft qualifier opens the list, so every item sits under it. The dashed separator is gone. Both copies list the same items in the same words, and the spec item phase 2 rewrote is identical in both. Read.

confirms: none
The edited set takes the edges the coordinator named the way *Scope* item 1 says. Probe E1: a spec moved to another work item and changed in one commit is read at its new path, and nothing names the old path. E2: a spec the branch deletes yields nothing. E3: an exact move into the judged work item is read by the per-declaration loop. E4: an untracked spec under `--worktree` is read. A spec a release pull request carries is left to the squash that carried it (`tests/test_chain_check.py:2073`), and an exact move is left alone (`:2202`). `edited_work_items` is reached only after the declared-nothing return, and `rule_changes_of` holds the one exit-2 guard for both callers (`chain_check.py:1578-1609`, `:2027`, `:2039`). Executed.

confirms: none
*Scope* item 3's limit is pinned. S6's second half (`tests/test_chain_check.py:2016`) runs `--sealing` with no event payload, prints the refusal and exits 0. That is what round 1's probe P2 showed, and the changelog's sentence now says it. Read.

confirms: none
Each new case was read against its group. S12, S13 and S14 each take a different route to the edited set: added, changed on the base, and `straight to the PR`. S15, S16, the depth and name case and the edited exit-2 case each pin a filter that no other case reaches, as phase 2's mutation note says. None covers what another case already covers. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at 06e3232f, handed over as `unverified` | `seal/specs/1792619289-the-pull-request-check-parses-rule-changes/phases/phase-2.md` | the orchestrator, through `broad-gate`, once the rounds settle |
| CI run 39689643276 at 06e3232f (the orchestrator reports 39685286823 at be5a9330 passed every leg) | the `tests` workflow | the orchestrator |
| Whether `--sealing` should judge strictly where no pull request exists yet, carried from round 1 | `skills/code-review/scripts/chain_check.py:1969-1970` | the orchestrator, for the owner |
| Specs on the other open branches of this release, which this round did not read | the branches of the concurrent sessions | the orchestrator, at each of those pull requests, where this check now reads them |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_tmp_round2_probe.py -q -s -p no:xdist` in a scratch clone at 06e3232f, with E1 to E4 and N1 and N2 in one file | 6 passed. E1 exit 1 naming the new path only; E2 exit 0; E3 exit 1 naming the judged spec; E4 one line naming the untracked spec. N1: no spec at 06e3232f, `main` or `release/v0.22.3` parses differently under the be5a9330 reader and the new one. N2: five ATX near misses are newly refused; setext, blockquote and four-space headings read as no section under both readers |

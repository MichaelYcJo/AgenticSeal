# Review round 1: 1793240968-every-session-reads-bootstrap-and-parity-setup

target: 904078cf against origin/release/v0.24.1

## Findings

### 1. After a local answer at first setup, a yes to the parity question now runs a procedure that tells the person to commit `seal/parity.md` and that a pull-request check will refuse

severity: should
location: `skills/parity-setup/SKILL.md:49-65`, `skills/implement/bootstrap.md:186-187`
evidence: read `skills/parity-setup/SKILL.md:49-65`, `skills/implement/bootstrap.md:80-87`, `skills/implement/bootstrap.md:183-187`, `docs/the-review-and-parity-arms.md:84-85`, `docs/the-review-and-parity-arms.md:143-144`, `seal/threads/1793240968-every-session-reads-bootstrap-and-parity-setup/changelog.md:4`
verdict: open

The branch sends the bootstrap's yes into `skills/parity-setup/SKILL.md`
*Procedure*. That procedure was written for a command run in a set-up
repository, and two of its steps assume the root is committed. The bootstrap
reaches step 3 right after step 1, where the person may have just chosen
**local**. `skills/implement/bootstrap.md:80-87` says local mode "touches
nothing in the tree" and is "never a commit candidate". The procedure then
says, at `skills/parity-setup/SKILL.md:50`, to write `seal/parity.md`
"committed". At `:59-65` it tells the person that a ready pull request fails
its check until an `original:` line is recorded.
`docs/the-review-and-parity-arms.md:84-85` and `:143-144` say that in local
mode no pull-request check reads a round record. So the person is told, in
the same conversation, two things that contradict the mode they just picked.

The account claims this as a gain. The fragment says, at `changelog.md:4`,
that the procedure "says what changes once `seal/parity.md` exists, which the
removed restatement did not". That holds only where the root is committed.
The removed section at `1e82fd0a` (`skills/implement/orchestration.md:296-299`)
promised no pull-request refusal, and it gave no instruction to commit; it
said only that the checkout path stays out of "the committed file". The `/agentic:parity-setup`
command run in local mode had the same gap before this branch. The branch is
what puts it in front of every first-setup yes, so the fix belongs here
(contract rule 12: both steps are the class, and step 7 is the one a person
reads).

A fix that changes what the person is told is pinned in the same commit
(contract rule 14). The case that already reads the skill is
`tests/behaviour/test_chain_hooks_hardening.py#test_parity_declaration_is_bootstrappable_not_hand_written`.

```markdown
6. **Write two files.**
   - `seal/parity.md` from `templates/setup/parity.md`. Where the root is
     `<repo>/seal/`, commit it. In local mode the root sits under the common
     git directory and nothing under it is committed, so write it there and
     commit nothing. Coordinate-trust exceptions start empty.
   - `~/.claude/agentic/parity-paths.md`: the machine-local checkout path,
     keyed by this repository's origin remote URL so worktrees and second
     checkouts resolve to one entry. **This never goes in the committed
     file**: it is wrong for every other machine.

7. **Show the result and say what changes now.** Name the `legacy-parity`
   skill, the `tracer` agent, and that divergence from the original now needs
   grounds rather than preference. Say the consequence the user meets first,
   too. Where the root is `<repo>/seal/`: from this file onward, a ready pull
   request that changes anything outside the document roots fails its check
   until the comparison with the original is recorded as an `original:` line,
   in each round record under `through the review chain` and in the sealer's
   `guarantee.md` under `straight to the PR` (`skills/legacy-parity/SKILL.md`
   *Recording the comparison*). In local mode no pull-request check reads a
   round record or a guarantee (`docs/the-review-and-parity-arms.md` *The two
   arms*): say that the `original:` line is still written, and that no check
   refuses a record without it.
```

```python
# tests/behaviour/test_chain_hooks_hardening.py, in
# test_parity_declaration_is_bootstrappable_not_hand_written, after `setup`
procedure = " ".join(open(setup, encoding="utf-8").read().split())
assert "In local mode no pull-request check reads" in procedure, (
    "the parity-setup procedure promises a pull-request refusal local mode never gives"
)
```

answer:

## Confirmations

confirms: none
No earlier round exists, so no fact is carried. Every coordinate below was
opened or run this round, in a clone of the branch at `904078cf`.

confirms: none
The bootstrap moved byte for byte. Claimed in `trail/phases/phase-2.md` *The
S5 comparison*; the same `diff` of `3890b230:skills/implement/orchestration.md`
lines 89 to 279 against `skills/implement/bootstrap.md` from its heading to the
end exited 0 (executed). Against the base `1e82fd0a` the only difference is
step 3's yes at `skills/implement/bootstrap.md:186-187`, which is phase 1's
rewrite (executed).

confirms: none
The word counts hold: `wc -w` gives 7,835 for `skills/implement/orchestration.md`
at `1e82fd0a`, 5,839 at `904078cf`, and 1,907 for `skills/implement/bootstrap.md`
(executed). These are the figures in `trail/phases/phase-2.md` and in
`changelog.md:3`, which meets the issue's third Done-when item.

confirms: none
Both red-first claims hold (contract rule 15). With the pointer sentence
deleted from `skills/implement/orchestration.md:6-9`,
`test_the_orchestrators_half_sends_a_fresh_repository_to_the_bootstrap` failed
on its own message. With step 3's yes in `skills/implement/bootstrap.md:186-187`
reduced to "continues the work",
`test_parity_declaration_is_bootstrappable_not_hand_written` failed on "the
bootstrap's yes never reaches the parity-setup procedure" (executed, see
`## Probes`). The section-only read in that case is what lets it go red, since
the acts table's Bootstrap row at `skills/implement/orchestration.md:454` names
the same path. This bears out the first divergence in `gaps.md:11`.

confirms: none
The second divergence in `gaps.md:12` holds (read).
`tests/behaviour/test_first_setup_asks_once.py:175-181` names "the whole
Bootstrap section" and no file.
`tests/behaviour/test_every_orchestrator_act_names_its_delivery.py:286-300`
plants only the two orchestration files, and `acts` skips a path that does not
resolve at `:144-145`.

confirms: none
No citation of the moved headings is left on the old file (executed, `git grep`
for `Parity setup` and `bootstrap` outside `seal/threads/`). What remains is
`hooks/mode-gate.py:15-16` and `:50-51`, `templates/setup/claude-md-block.md:16`
and the acts table, all on the new path. One history sentence remains in a
docstring, `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py:8`.
The two `docs/` sentences that name the old file,
`docs/one-root-by-lifetime.md:108` and `docs/one-root-by-lifetime.ko.md:103`,
are rule changes in `frame/design.md:181-192`, as the policy root's rule asks.

confirms: none
Each rule change's `from:` text stands where the settle will look for it
(executed, whitespace folded). Four stand in `docs/` at `904078cf`. The fifth,
for `docs/the-record-layout.md`, stands in the `to:` text of
`seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/frame/design.md:455-457`,
which the settle applies first in merge order. The archive paragraph of
`docs/release-checklist.md:77-86` names the same path glob, and that work
item's rule changes remove it, so it needs no change here.

confirms: none
The preset block and the opening sentence agree with the issue's routing.
`templates/setup/claude-md-block.md:16` sends a fresh repository to
`skills/implement/bootstrap.md` *Orchestrator: Bootstrap*. A block installed
before the change lands on `skills/implement/orchestration.md:6-9`, which states
the same condition and sends it on (read). The issue left the parity sentence
to the framer, and `frame/questions.md:12-15` records why one sentence serves
both.

confirms: none
The nine modules the frame lists pass at `904078cf`, each run alone through
`bin/test` (executed, see `## Probes`). The `unverified` label on the full
suite, the lint and the typecheck in `gaps.md:18` names the orchestrator, and
it is honest: nothing broad was run by the crafter or by this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The crafter wrote `changelog.md` with its `### Process changes` row, which `frame/plan.md:93-98` gives to the orchestrator; the crafter's write set names `changelog.md` only where the plan's row asks for it. Its facts match the tree (see the word counts above), and whether the orchestrator adopts it as written is not a reviewer's call | `seal/threads/1793240968-every-session-reads-bootstrap-and-parity-setup/changelog.md` | the orchestrator |
| Whether step 7's refusal sentence holds under the default mode, shared with records only, where no workflow is installed and only `seal gate` runs `chain_check.py` | `skills/parity-setup/SKILL.md:57-65` | the crafter, in the fix pass of finding 1 |
| The full suite, the repository-wide lint and the typecheck over this branch | the branch at `904078cf` | the orchestrator, at `seal gate --record` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `diff <(git show 3890b230:skills/implement/orchestration.md \| sed -n '89,279p') <(sed -n '/^## Orchestrator: Bootstrap$/,$p' skills/implement/bootstrap.md)` | exit 0 |
| the same `diff` with `1e82fd0a` in place of `3890b230` | exit 1, differing only at step 3's yes, lines 178 to 179 of the range |
| `wc -w skills/implement/orchestration.md skills/implement/bootstrap.md` and `git show 1e82fd0a:skills/implement/orchestration.md \| wc -w` | 5,839, 1,907 and 7,835 |
| `bin/test <module> -q`, once per module, for `test_first_setup_asks_once.py`, `test_chain_hooks_hardening.py`, `test_every_orchestrator_act_names_its_delivery.py`, `test_a_cited_section_stands_in_its_file.py`, `test_no_passage_is_pasted_into_a_second_file.py`, `test_docs_line_wrap.py`, `test_the_rules_have_one_owner.py`, `test_the_settings_have_a_front_door.py` and `test_a_section_marked_for_one_role_reaches_only_that_role.py` | each exit 0: 51, 30, 15, 23, 8, 40, 35, 18 and 11 passed |
| In the clone, the pointer sentence removed from `skills/implement/orchestration.md` and step 3's yes cut to "continues the work" in `skills/implement/bootstrap.md`, both by `Edit`; then `bin/test tests/behaviour/test_first_setup_asks_once.py -k test_the_orchestrators_half_sends_a_fresh_repository_to_the_bootstrap -p no:xdist -q` and `bin/test tests/behaviour/test_chain_hooks_hardening.py -k test_parity_declaration_is_bootstrappable_not_hand_written -p no:xdist -q` | exit 1 and exit 1, each on its own assertion message; both edits reverted by `Edit`, and `git diff --quiet` exited 0 |
| `python3 -I` reading each rule change's `from:` text against its `docs/` file, whitespace folded | four found; `docs/the-record-layout.md` not found, its text standing in the sibling work item's `to:` |
| `git grep -n -i -e 'Parity setup' -e bootstrap` outside `seal/threads/` | no citation names the old file for either heading |

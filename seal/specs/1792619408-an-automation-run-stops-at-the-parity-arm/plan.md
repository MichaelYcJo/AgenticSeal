# Implementation Plan: an automation run stops at the parity arm

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md holds HOW, in phases. It
is the Design Gate's artifact: where the work alters observable behaviour,
approval of this plan is the gate. -->

Approved <date> by <who>, when `smith` was spawned.

<!-- The line above is the record that the gate happened. The orchestrator
writes it when it spawns the build, in the shape and on the terms
`skills/implement/orchestration.md` *The plan is approved at the spawn*
states, including the shape where `routing.md` answers `Implementation`
with `the session`. A later session, a reviewer and CI all read the tree,
and a plan with nobody's name on it cannot be told from one nobody approved.
The line shares its shape with `templates/sdd-routing.md`'s `Answered <date>
by <who>, before the first edit.`: the verb, the date, who, and the moment.
The two are pinned against each other, so neither spelling can drift into a
second convention for one kind of fact. -->

## Summary

In a repository that declares `seal/parity.md`, a branch whose `routing.md`
answers `through the review chain` stops meeting the parity arm at the
commit, and the pull-request check takes the arm's place: it refuses a ready
pull request whose round records do not each carry an `original:` line
naming the migration config's baseline. The warden writes that line in the
round where it compares. The `straight to the PR` answer and an undeclared
branch keep the arm at the commit as it is today.

## Technical context

**Why the run stops today** (`read` unless marked).

- `hooks/gate.py#arms_missing` (lines 162 to 168) adds the parity arm where
  the waiver is absent, `optin.parity_config(cwd)` holds, `touches_code`
  holds and the mark under the git directory does not name HEAD. Unlike the
  review arm three lines above it, it does not consult
  `routing.declared(cwd, top)`.
- Under the `automation` press the refusal text is `hooks/gate.py#AUTOMATION`:
  a commit that belongs to a work item is not retried and is handed back at
  the end of the run. So the smith's first code commit ends the build.
- The parity mark is written by the warden in a review round
  (`agents/warden.md` *Order of work* step 5) or by the orchestrator where it
  compared with no round (`skills/legacy-parity/SKILL.md` *Recording the
  comparison*). The smith commits at `agents/smith.md` *Order of work* step 6,
  before any round, so in a chain run the arm can meet a build commit only
  with a waiver.
- `hooks/question-gate.py` (#1002) refuses `AskUserQuestion` while
  `Automation` reads `yes`, so the attended text, which tells the model to
  ask, cannot be acted on in such a run either.

**What the build touches.**

| Coordinate | What changes |
|---|---|
| `hooks/gate.py#arms_missing` and the module docstring's *The two arms* list | the parity arm gains the conjunct *no declaration whose `review` is `routing.CHAIN`*; the declaration is read once for both arms |
| `skills/code-review/scripts/chain_check.py` | a new refusal for a chain-declared work item in a parity repository whose diff touches code: a round record with no `original:` line, or one naming another commit; a config with no readable `Baseline commit` |
| `docs/the-review-record.md` *The round record*, the grammar table | one new row, `original:`, edited in the commit that adds its reader, because `chain_check.py#grammar` loads the table from that file at run time; #1000 did the same (`ebbbd2f0`, its phase 3, `read`) |
| `hooks/config.py` | one reader of `seal/parity.md`'s `Baseline commit` cell, beside `read_table`; no reader of that row exists today (`executed`: `git grep -n 'Baseline commit' -- hooks skills .github bin` returned only `skills/implement/orchestration.md:249`) |
| `templates/sdd-round.md` | an `original:` placeholder line with one comment saying when it is owed |
| `agents/warden.md` *Order of work* step 5 | the warden writes `original: <baseline>` in the record once it compared, beside the mark it already writes |
| `skills/legacy-parity/SKILL.md` *Recording the comparison* | names the round record line as the record CI reads, and when the gate still asks |
| `skills/implement/orchestration.md` *Orchestrator: how the work is routed* | the wake/quiet table's parity cell and the sentence under it |
| `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* | the sentence *A declaration does not silence the parity arm* |
| `README.md` and `README.ko.md` *The gates* | the `commit-review-gate` row's parity sentence |
| `tests/test_routing_is_recorded.py`, `tests/test_chain_check.py`, and one inside-git case module | the cases of S1 to S11 |

**The failure scenario of the chosen approach, six months on.** A warden
copies `original: <baseline>` from an earlier round's record without
comparing the new range. The check passes, because it reads that a
comparison was recorded and not that it was good; this is the parity mark's
own limit (`docs/the-review-and-parity-arms.md` *Parity arm*, last
paragraph), moved to a place CI can see. What catches it is the next round
and the sealer reading the records, not a check. A second scenario: a
chain-declared branch with `stop before the pull request` is checked by
nothing, the cost the review arm's declaration already carries.

**This repository declares no `seal/parity.md`** (`executed`: `ls seal/`
lists `config.md`, `follow-up.md`, `README.md` and `specs`), so the smith's
own commits on this branch never meet the parity arm, and no existing round
record here owes the new line. No round record in the tree opens a line with
`original:` (`executed`: `git grep -n -E '^original:' -- seal/specs evals`
exit 1, with `^target:` over `seal/specs` as the control, exit 0).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Keep the arm as it stands | every `automation` run in a migration repository stops at the smith's first code commit and hands the build back; the issue's done-when fails by construction | rejected |
| B. A chain declaration quiets the arm at the commit, and `chain_check.py` owes an `original:` line naming the baseline in every round record | a warden copies the line without comparing, and the check cannot tell; a chain branch that never opens a pull request is checked by nothing. Both are limits the mark and the review arm's declaration already have | **chosen**: it keeps the catch (a code change nobody compared does not reach a ready pull request), moves it where CI sees it, and stops nobody; it is the review arm's own design applied to the second arm |
| C. The smith writes the parity mark from a scribe comparison | the smith cannot spawn a scribe (contract §6), so the orchestrator spawns one before each commit; the mark names one HEAD, so the second commit of a phase stops again; the builder certifies its own comparison, which the review arm's two answers exist to refuse; and CI never sees a mark under the git directory | rejected |
| D. The comparison as a phase step, recorded in `phases/phase-N.md` and read by the gate before the commit | the phase record is written when the phase closes, after its commits; a gate that reads a builder-written line as the satisfying fact turns a claim into a waiver, and the reading is of words | rejected |
| E. The parity arm moves to the pull request for every branch, and leaves the commit everywhere | an undeclared code commit in a migration repository, question 1's `no work item` answer, is read by no pull-request check, which passes a branch with no declaration with a notice; nothing then records that nobody compared | rejected; its pull-request half is B |
| F. A `Parity` row in `routing.md`, or a fifth box in question 2 | question 2 is at its four-box cap (`skills/implement/orchestration.md` *Question 2*, *The ceiling*); `seal/parity.md` already declares the migration, so the row states one value twice; a row nobody is asked about is a claim | rejected |
| G. Remove the parity arm, its mark and `[no-parity]` altogether, replacing the structure rather than adapting it | the premise that keeps it was checked: the undeclared path exists (`skills/implement/orchestration.md` *Question 1*, row 3; `skills/implement/SKILL.md` *1. Read the spec before the code*, which names `[no-parity]` beside `[no-review]`), and on that path the visible waiver in history is the only trace that nobody compared. G loses that trace and rewrites every parity case in `tests/test_chain_hooks_hardening.py` and `tests/test_the_commit_gate_decides_at_the_commit.py` for a defect that is about declared runs | rejected for this item; B removes the arm only where a pull-request check replaces it |
| H. A declaration quiets the arm for either review answer, as it does the review arm | under `straight to the PR` no round record exists to carry a comparison, so the check either owes nothing there, which drops the protection under that answer, or refuses every code pull request in a migration repository, which makes that answer unusable there | rejected as the default; `questions.md` Q1 puts the choice to the owner |

## Phases

The pull-request half lands first, so the branch never holds a state in
which the commit-time stop is gone and nothing at the pull request stands in
its place.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The pull-request half. The `original:` row in `docs/the-review-record.md`'s grammar table; the `Baseline commit` reader in `hooks/config.py`; `chain_check.py`'s refusal of S4, S6, S10 and S11, reading the doc-root rule from `hooks/gate.py#DOC_ROOTS` and `touches_code` rather than a copy; `templates/sdd-round.md`'s placeholder; `agents/warden.md` step 5; `legacy-parity` *Recording the comparison*. Cases S4 to S11 in `tests/test_chain_check.py`, the refusal cases marked `@pytest.mark.rule("parity-at-the-pull-request")` | each case seen red against the tree as it stands, then green; the narrow runs of `tests/test_chain_check.py`, `tests/test_review_axes.py` and the module pinning `templates/sdd-round.md`; `mutation-check` over each unit added | |
| 2 | The commit half. The conjunct in `hooks/gate.py#arms_missing` and its docstring; S1's cases through `arms_missing`, `pre-commit` and the PreToolUse reading, marked `@pytest.mark.rule("parity-quiet-under-the-chain")`; the two `tests/test_routing_is_recorded.py` cases rewritten to `straight to the PR` (S2); the wake/quiet table and its sentence in `skills/implement/orchestration.md`; the sentence in `skills/implement/SKILL.md`; the README rows; the work item's `changelog.md` fragment | each case seen red, then green; the narrow runs of `tests/test_routing_is_recorded.py`, `tests/test_an_automation_run_meets_no_commit_prompt.py`, `tests/test_chain_hooks_hardening.py` and `tests/test_the_commit_gate_decides_at_the_commit.py`; S12's two `git grep` searches, each beside a control that finds a known line; `mutation-check` over the conjunct | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past
one, which someone can open.

The party that builds a phase fills its cell as the phase closes, not at the
end. A phase reconstructed afterwards is reconstructed from the diff, which is
where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. The party that builds the phase
writes it to `seal/specs/<work-item-id>/phases/phase-N.md`, from
`templates/sdd-phase.md`, when the phase closes.

Where feature branches squash, these commits stop resolving at the merge, and
**a rebase during the work does the same thing earlier and more quietly**,
because the orphaned object still answers `git cat-file` in the worktree that
wrote it. **The party that rebases the branch re-reads this column after the
rebase**, or the column names commits that resolve in one clone and nowhere
else. Nothing measures from this column, which is why that is tolerable.

## Operational impact

- **A migration repository with a chain-declared work item in flight** meets
  the new refusal at its next ready pull request once it upgrades: round
  records written before this release carry no `original:` line. A round
  written after the upgrade carries it. This is the case
  `docs/the-review-record.md` *What the check reads at the pull request*
  already states for a line the table adds, and the changelog fragment names
  it.
- **A repository with no `seal/parity.md`** sees no change at the commit or
  at the pull request.
- No new dependency, environment variable or migration.

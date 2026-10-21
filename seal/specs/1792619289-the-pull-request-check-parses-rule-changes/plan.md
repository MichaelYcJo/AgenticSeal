# Implementation Plan: the pull request check parses each spec's rule changes (#1006)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md holds HOW, in phases. It
is the Design Gate's artifact: where the work alters observable behaviour,
approval of this plan is the gate. -->

Approved 2026-10-22 by the orchestrator, under the owner's `automation` answer and Q1's default, when `smith` was spawned.
Approved 2026-10-22 by the orchestrator, for the redesign after round 1, when `smith` was spawned.

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

`chain_check.py` gains one read over two sets of specs. It parses with
`rule_changes.parse`, the reader `settle` uses, the `spec.md` of every work
item whose `routing.md` it judges, and every work item `spec.md` the pull
request's own commits add or change on a pull request that declares at
least one work item. Each error becomes a refusal at the spec's path and the
parser's line. The first set is read in the per-declaration loop in `main`
beside the frame arm (phase 1). The second is read after that loop, from
the diff `main` already holds, filtered by `carried_by` and by the moved
set (phase 2, after round 1). Both take the check's draft and ready
strictness and its `--sealing` behaviour without a rule of their own. The
prose that lists what the check reads is corrected in the commit that
changes it, and the policy root's statement of the rule is `spec.md`
`## Rule changes`.

## Technical context

Coordinates are at the frame commit's parent, b571ece3 (read).

- `skills/code-review/scripts/chain_check.py`
  - `main` (1852–1967). The per-declaration loop is 1923–1960. A carried
    declaration never enters `declarations` (1893–1899). A declaration a
    settle removed, or one git does not carry, ends at `continue` (1926–1938),
    and so does one `routing.parse` cannot read (1939–1949). The frame arm is
    called at 1950–1952, and the new call goes beside it. Under `--sealing`
    only the `broad_gate` and `guarantee` entries become notices (1955–1960),
    and the new entries stay in `problems`.
  - `frame` (1509–1543) reads `spec.md` through `read_record` only where
    `Planning` reads `framer` (1511), so a work item declared `the session`
    has no spec read today.
  - `read_record` (698–709) reads HEAD, or the disk under `--worktree`.
  - `SHARED_READER` (469–475) is `skills/verify/scripts/unverified_check.py`,
    loaded at import. `retired` (1843–1849) already asks
    `unverified_check.py#settled`, which loads `rule_changes.py`.
  - The module docstring (1–47) lists five arms.
- `skills/verify/scripts/unverified_check.py`
  - `rule_changes` (1352–1362) loads `skills/settle/scripts/rule_changes.py`
    by path once and caches it.
  - `policy_root` (1083–1087) is `hooks/config.py#policy_root`'s answer, the
    value `settle.py` passes (`settle.py:282` and `settle.py:581`).
  - `annotate` (1576–1586) prints `path:line  message`, or a GitHub
    annotation in CI.
- `skills/settle/scripts/rule_changes.py#parse` (72–142) returns `Parsed(ops,
  nothing, errors)`. `ops` is None where the spec has no section. `errors`
  holds at most one `(line, reason)`, and the line counts the way `grep -n`
  does, through `gfm_lines`.
- Where the check runs: `.github/workflows/hygiene.yml` job `release`, step
  *a declared review chain has the round record it claimed* (184–188), on
  every pull request event. `skills/verify/scripts/broad_gate.py` arm 3 runs
  it with `--sealing` (docstring line 30), and `--preflight` runs the same
  arm. `templates/hygiene.yml` (82–95) runs the same script in user
  repositories, from a clone at the release the user installed.
- Importers that must stay untouched: `hooks/commitgate.py` (262–273),
  `skills/verify/scripts/seal_stamp.py` (1011–1016 and its callers),
  `skills/verify/scripts/broad_gate.py` (2517–2531) and
  `.github/scripts/release_seal.py` (288–295). Each uses readers and
  constants and never `main`.
- `tests/test_chain_check.py`: the `branch` fixture (166–222) declares
  `the session` and `through the review chain`; `ready` and `draft`
  (234–249); `check` (252–254) runs `main`; `squash` (330) builds a carried
  commit; `TestCarriedBy` (354) and `TestFrame` (1862) are the neighbours.

For phase 2, at be5a9330 (read): `main` starts at 1881, `paths, moved =
diff` is 1917, the `if not declarations` return is 1944, `fork` is computed
at 1948, the loop's `rule_changes_read` call and its exit-2 guard follow
`frame`, and the notices print from 1999. `carried_by` is 634. Round 1's
record, finding 1, holds a sketch of the edited set at the line after
`fork`.

**What breaks in six months.** A `spec.md` edited by a pull request that
declares nothing still merges unread (Alternatives A2). `settle`'s dry run
still names it after the release. A pull request that edits many specs
pays one `git log` per spec in `carried_by`: #941's would have paid 114. A
second case: a later change to
`rule_changes.parse` that reads the policy root's documents, such as whether
a `section:` exists, would reach the pull request through this call and
refuse sections whose text an earlier unsettled spec has not placed yet. The
call inherits whatever the one reader decides, which is the point of one
reader, and whoever changes the reader meets this caller in `git grep`.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Parse the `spec.md` of each work item whose `routing.md` the check judges, inside `main`'s per-declaration loop, and every work item `spec.md` the pull request's own commits add or change, on a pull request that declares at least one work item, less what `carried_by` assigns to another pull request and what the diff only moved; all through `unverified_check.py#rule_changes` | the case A2 names: a `spec.md` edited by a pull request that declares nothing merges unread. A pull request that edits many specs pays one `git log` per spec | **chosen, after round 1.** It reads every section the pull request's own commits wrote, reuses the diff, the moved set and `carried_by` the declarations already use, and keeps the promise that a pull request declaring nothing is asked nothing |
| A2. As A1, and also on a pull request that declares nothing | a pull request that declared nothing fails for a spec it carries, which the comment above the hygiene step (*It never fails for a pull request that declared NOTHING*), `CONTRIBUTING.md`'s *ask nothing of a branch that declared nothing* and the no-declaration notice's *examined nothing* all deny. Four sentences change for a pull request that belongs to no work item | rejected. Such a pull request carries no routing, no round and no frame, and `settle`'s dry run still names its spec |
| A9. Parse only the `spec.md` of each work item whose `routing.md` the check judges (phase 1's build) | a declared work item that edits another work item's spec merges that section unread. #941's squash b451e503 added `## Rule changes` to 114 other work items' specs without touching their `routing.md`, and none of those sections would have been read. Round 1's probes P1a, P1b and P1c each exited 0 on a ready pull request (executed by the warden) | rejected at round 1, finding 1. Its premise, that a work item's own spec is always beside a judged declaration, holds, and the conclusion drawn from it did not: a declared commit can write another work item's spec |
| A3. Parse every `spec.md` in the tree at HEAD, the population `settle` reads | one section merged unread, before this check or by a direct push, refuses every later pull request on the release branch, charged to authors who did not write it | rejected. Measured at the frame: the 118 specs other than this one all parse (executed, in memory), so A3 would refuse nothing today; the failure is the next one |
| A4. Replace the structure: run `settle`'s dry run at the pull request as a new hygiene step | the dry run exits 0 where the spec is also held by an open row, which is how both 0.22.3 instances passed, and exits 1 for refusals no pull request can settle, a `from:` an unmerged earlier spec places or a conflict merge order decides. A new step also owes a row in `broad_gate.py`'s partition | rejected |
| A5. The commit gate parses `spec.md` at each commit | a framer's skeleton commit holds the template's empty section and is refused mid-run, which stops an unattended run at the commit. The reading inside git covers only clones whose hooks are this plugin's, so CI has to read it anyway | rejected |
| A6. Keep the structure: nothing reads the section before `settle`, and a framer or warden runs the parser by hand | two sections in one release did not parse and were found by chance (#941, #940), and `bin/settle --released-at HEAD` exited 0 on both because each spec was also held by an open row | rejected. Its premise, that somebody runs the parser, was checked: no file under `agents/`, `skills/`, `docs/` or `templates/` tells anybody to (executed, `git grep`) |
| A7. Read the spec once in `main` and hand the text to both `frame` and the new read | `frame`'s signature changes, and so do its two direct cases in `TestFrame`, to save one `git show` per judged work item | rejected. `frame` reads the spec only under `Planning` `framer` (`chain_check.py:1511`), so a work item declared `the session` needs the new read's own `read_record` call anyway |
| A8. `chain_check.py` loads `rule_changes.py` itself with its own `load` | two module objects for one reader under two names, the copy `tests/test_a_format_has_one_reader.py` exists to keep out | rejected; the shared reader's loader already serves `chain_check.py#retired` |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `chain_check.py#rule_changes_read`, the constant `RULE_CHANGES_SAYS`, the call in `main` beside `frame`, and exit 2 with the stderr line where the loader raises, all as `spec.md` *Data & interfaces* states them. Cases S1 to S10 in `tests/test_chain_check.py`, each carrying `@pytest.mark.rule("rule-changes-read-at-the-pull-request")`. In the same commit, the sentences `spec.md` `## Removes` names, rewritten in place, and one sentence after `skills/settle/SKILL.md` *Rule changes*'s *`skills/settle/scripts/rule_changes.py` is the one reader.* saying that `chain-check` asks the same reader at the pull request, citing `docs/the-review-record.md` *What the check reads at the pull request* | `bin/test tests/test_chain_check.py -q`. Each refusal case (S1, S2, S3, S5, S6, S7, S9, S10) seen red against `chain_check.py` as it stands at the frame commit, and the smith's hand-back saying how. `rule_changes.parse` run in memory over this work item's `spec.md`, to show its own section still parses | 22bfec31 |
| 2 | The reframe after round 1. In `main`, the edited work items as `spec.md` *Data & interfaces* states them, computed after the `if not declarations` return and read after the per-declaration loop under the same exit-2 guard. Cases S12 to S16 and S6's second half in `tests/test_chain_check.py`, each carrying the same marker. In the same commit, every sentence that says the check reads only judged work items' specs, rewritten in place to name both sets of *Scope* item 1: the docstring's `rule changes` arm, both hygiene comments as round 1's fix pass leaves them, and the `skills/settle/SKILL.md` pointer sentence. `changelog.md`'s *stays a refusal in the broad gate's own run* rewritten to *Scope* item 3's limit | `bin/test tests/test_chain_check.py -q`. S12, S13 and S14 seen red against `chain_check.py` at 22bfec31, and the smith's hand-back saying how. `rule_changes.parse` run in memory over this work item's `spec.md` | |

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

- **No migration, no new environment variable, no new dependency.**
- **It blocks more.** A ready pull request that declares a work item, and
  carries a `spec.md` of either set whose `## Rule changes` does not parse,
  now fails the hygiene job. The orchestrator's `broad-gate` run and
  `--preflight` print the refusal and do not fail on it, because no pull
  request exists yet when they run (`spec.md` *Scope* item 3). A wrong
  refusal costs one edit to a spec at its own pull request; a wrong allow is
  a release whose rule changes apply nothing at the owner's settle.
- **Prompt budget: none.** The refusal is printed and read; nothing asks.
- **User repositories** meet the read at the release they install, through
  `templates/hygiene.yml`'s clone of the plugin. An open pull request there
  whose spec's section does not parse goes red at its next run after the
  upgrade, with the line and the reason.
- **This work item's own section** is read by the check from the build's
  first commit on, because the build lands the read on this branch. It
  parses at the frame (executed, in memory), and phase 1's last check is
  that it still does.

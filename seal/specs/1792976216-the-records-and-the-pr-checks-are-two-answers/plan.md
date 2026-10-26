# Implementation Plan: where the records live and whether CI checks pull requests are two answers (#952)

Approved 2026-10-26 by the orchestrator under the owner's automation answer, when `smith` was spawned for phases 1 and 2.

Approved 2026-10-26 by the orchestrator under the owner's automation answer, when `smith` was spawned for phase 3.

## Summary

Two phases. Phase 1 makes every step of `templates/hygiene.yml` pass a pull
request that declares nothing, and plants the case that keeps it so. Phase 2
splits the bootstrap's answer, gives the workflow its own command, takes the
workflow out of `seal mode`, and rewrites every text that said otherwise.
Phase 1 goes first because phase 2's new header and docs say a workflow left
in local mode examines nothing, which is true only after phase 1.

Review round 3 sent the work item back to the framer: two of its findings
were second regressions, one on the rule-change items that state the no-root
condition and one on the chain step's no-root test under `--worktree`. The
reframe puts the two rule-change corrections into `spec.md` itself (round 3,
findings 1 and 3), and adds phase 3. Phase 3 plants the one case the no-root
test lacks, shows that every answer of that test has a case, replays the
rule changes onto `docs/` and runs the documents' own cases over the result,
and closes the build with `overview.md`. The two regressions had one cause.
The frame accepted a unit on less than its applied form: the rule changes on
parsing and placing, and the test on its cases passing. S8 and S9 now ask for
the applied form.

## Technical context

- **The checks.** `templates/hygiene.yml` runs four steps after
  `actions/checkout`: the plugin's clone, `unverified_check.py --baseline
  origin/<base> seal/specs/`, `chain_check.py --baseline origin/<base>`, and
  `seal.py mode --check`. Only the second fails a pull request that declares
  nothing, in two shapes (`spec.md` *Scope*, *What the tree says today*,
  executed). The exit 2 sits at `skills/verify/scripts/unverified_check.py`
  lines 1709 to 1718, after the base comparison; the missing-path refusal at
  lines 1518 to 1521 and 1590 to 1607; `settled_root` at lines 1434 to 1456
  is the precedent the two new states sit beside.
- **The writer.** `skills/implement/scripts/seal.py` already holds the
  workflow's whole writer: `plugin_version` (1757), `plugin_workflow`
  (1775), `install_workflow` (1797) and `remove_workflow` (1869). Their only
  caller is `switch` (lines 2321 and 2294; read by `git grep
  install_workflow`). The new `pr-checks` subcommand calls them, and the
  parser at lines 2514 to 2564 gains it beside `mode`, with
  `choices=("install", "remove")`.
- **The question.** `skills/implement/orchestration.md` *Orchestrator:
  Bootstrap* step 1 states the options; `hooks/mode-gate.py#question_reason`
  states the gate's three for a root with no `Mode` row.
- **The case of item 4.** `tests/conftest.py#workflow_steps` (line 119)
  already splits a workflow into named steps; `symlink_or_skip` and
  `gh_answers` exist there too. `tests/e2e/creation/test_creation_flow.py`
  is the one flow file to copy the shape from.
- **Failure scenario of the chosen approach, six months on.** A later
  release adds a step to `templates/hygiene.yml` that reads something only a
  work item has, and a teammate's pull request goes red again. The case of
  phase 1 runs every `run:` block it finds, so that step fails the suite
  before it ships. What the case cannot catch: a step that needs the network
  and is not the clone, which the case refuses by counting the `git clone`
  steps, and a base the four shapes do not cover, such as a work item whose
  `overview.md` is unreadable. That last one is a base broken by a pull
  request merged red, and its author's to fix.
- **Second failure scenario.** A person deletes `.github/workflows/hygiene.yml`
  by hand. `seal pr-checks` then reports *not installed*, which is true, and
  nothing else disagrees, because no row claims otherwise. Under a config row
  this was a disagreement for some check to fail on.
- **The no-root test of phase 3.** `skills/code-review/scripts/chain_check.py#main`
  lines 2191 to 2197 at `2f41bbf9`: `gone` comes from `os.path.lexists`
  under `--worktree` and from `git ls-tree HEAD -- seal` otherwise, and a
  `git()` of None keeps the declarations judged. `tests/test_chain_check.py`
  `Test_retired` (lines 3359 to 3450) holds a case for four of its five
  answers; the case round 3 finding 2 drafted is the fifth, and the round ran
  it as a probe, passing at `64a13a36` and failing against `gone = False`
  (executed by the round).
- **The replay of phase 3.** `skills/settle/scripts/rule_changes.py#parse`
  (line 83) reads `## Rule changes`, and `apply_op` (line 217) writes a
  `change` item's `to` lines as they stand after the text before `from` on
  its line. That is why a `to` line's width is only known applied. Rounds 2
  and 3 each built this replay as a probe in a clone, and no command in
  `bin/` runs it.
- **Failure scenario of phase 3, six months on.** A later work item changes
  the chain step's no-root test again and its frame accepts it on its cases
  passing, as this one did before the reframe. S9's mutants are a probe, and
  nothing re-runs them. What stays is five cases, one per answer, so a later
  edit that drops an answer turns one of them red. The replay is a probe
  too. In this work item, phase 3 and the verifying round run it. In a later
  work item, a rule-change `to` text that the settle would show too wide, or
  copied, or pinned by a case, is found by a reviewer who builds the replay,
  or else at the settle (`questions.md` Q4).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **A. The workflow file is the record** of whether the checks are installed; the `Mode` row keeps `local` and `shared` | The issue's sentence *recorded where the mode row is* is not built as written; a reader of `seal/config.md` alone cannot see whether the checks are installed and has to run `seal pr-checks` | **Chosen.** One source, the file CI itself runs, and nothing to migrate: every existing repository already reads correctly. `questions.md` Q1 carries it to the owner with this as the default |
| B. A `Pull-request checks` row in `seal/config.md`, written by the bootstrap and by `seal pr-checks`, compared with the file by `seal mode --check` | A teammate's pull request that deletes or renames the workflow leaves the row disagreeing. Either `--check` fails it, which is a step gating a teammate, or it does not, and the row says something false with nothing reading it. Every existing repository has no such row, so an absent row has to be read from the file anyway, which makes the file the source and the row a copy | Refused: `CLAUDE.md` *The rule a mechanism is kept against*, a fact has one source and nothing is kept beside the tree to stay in step with it |
| C. A third `Mode` value, such as `shared-checks` | `Mode` would answer two questions at once, the coupling this issue removes. Every reader of the row (`hooks/config.py#declared_mode`, the mode gate, `seal mode --apply`) learns a value that is not a place, and `shared` in an existing repository with a workflow reads as records only, so its own `--check` disagrees after the upgrade | Refused |
| D. Keep `seal mode` carrying the workflow, and only add the records-only answer | The structure stays. Its premise is that the switch is the moment the checks should change. Checked: the premise is false for the reported case, where a person moves to shared and wants no workflow, and for a person who moves to local and wants to keep a workflow that a teammate's clone still reads until the commit lands. Every switch would then need a flag saying which half to do | Refused: the issue's item 2 and the premise both say replace |
| E. Replace the carry with `seal pr-checks install` and `seal pr-checks remove`, the existing writer moved behind its own command | The person who switches has to run a second command to change the checks. The switch prints that command where it applies (`spec.md` *In* item 4) | **Chosen**, with D's premise checked above |
| F. Name the command `seal checks` | `seal checks` sits one letter from the `--check` flag that `seal mode` and `seal export` already take, and a person typing `seal check` gets a usage error that reads like a missing flag | Refused for `seal pr-checks`, which uses the documents' own term, *the pull-request checks* |
| G. Make `unverified_check.py` exit 0 for any path holding no `overview.md` | `unverified-check docs/` and a misspelt `seal/spces/` both pass in silence, the failure `settled_root` was written to prevent | Refused: only a path whose last two parts are `seal` and `specs` takes the new states |
| H. Keep the base comparison when no `seal/` root is in the tree | The pull request that runs `seal mode local` with the workflow kept deletes every `overview.md`, and the deletion arm fails it with no way out but removing the checks in the same pull request | Refused: with no root in the tree nothing is declared, and the diff shows the whole root leaving |
| I. Add a fourth option, *Shared, with pull-request checks*, to the mode gate | The gate reaches a root that exists and skipped the bootstrap; a fourth option states the bootstrap's split a second time, in a deny reason a model relays | Refused: the gate's *Shared* option names `seal pr-checks install`, which is the same choice one command later |
| J. Leave the bootstrap writing the file by hand, as now, beside the new command | Two writers of one file: the bootstrap's one-liner and `install_workflow`. A fix to one, such as the staging check, misses the other | Refused: the bootstrap runs the command |
| K. Keep the working-tree reading of the no-root test under `--worktree`, and add the case for its one unpinned answer | A later edit to the test that changes what `os.path.lexists` is asked still meets five cases, so the failure left is a sixth shape nobody listed; the six round 3 ran are in its confirmations | **Chosen** (reframe after round 3). The premise that keeps the structure, checked: under `--worktree`, `read_record` and `changed` read the declarations from the working tree (`docs/the-review-and-parity-arms.md` lines 112 to 114, read), so the no-root test reads the tree the declarations come from. Round 3 ran six tree shapes through both readings and found them as `spec.md` *In* item 6 says (executed by the round) |
| L. Replace the working-tree reading: ask HEAD in both modes, and state the uncommitted switch as a limit in *Out* | A session that runs `chain-check --worktree` after `seal mode local` and before the commit is refused on every `routing.md` with "git does not carry this file at HEAD", which CI accepts once the switch is committed. A new untracked root goes unjudged, and the check prints a cause that is false (round 2, finding 2, executed by that round) | Refused: K's premise holds, and L brings back both of round 2's shapes |
| M. Add a check or a case at the pull request that applies every unsettled spec's `## Rule changes` and runs the documents' own cases over the result | It judges every unsettled spec, so it goes red today on the three specs the merge-order replay already refuses (round 2, `## Not judged`), and it gates a pull request on specs outside its branch. It is a new gate, which owes the argument `CONTRIBUTING.md` *What a change to a gate must carry* asks for | Refused for this work item; whether the class earns a gate is `questions.md` Q4 |
| N. Carry S8's applied half as a probe: phase 3 replays this spec's items onto `docs/` at `02ee12de` and runs the documents' cases, and the verifying round does the same | The probe leaves nothing in the tree, so the next work item meets the class with only a reviewer's replay (above) | **Chosen**, with M left to Q4 |
| O. State the no-root rule in the `add` alone, and drop the two `change` items that qualify "the deletion is judged" and "the refusal stands" | The two sentences then read as absolute beside an `add` that says otherwise, the two readings round 1's fix pass found and `64a73e7b` qualified. `CLAUDE.md` *Repo rule: text an agent or a check reads has one reading* refuses that | Refused: three items, with the `add` as the one statement and each `change` naming it or its term |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `unverified_check.py`: the two exit-0 states of `spec.md` *In* item 6, its docstring's exit codes, and cases in `tests/test_unverified_check.py` marked `nothing-declared-nothing-owed`; the flow case `tests/e2e/teammate/test_teammate_flow.py` of *In* item 7, with the same marker | the case seen red at `02ee12de` on the two failing bases and green after; `bin/test tests/test_unverified_check.py tests/e2e/teammate -q`; `bin/test-layout --check tests/e2e/teammate/test_teammate_flow.py`; `python3 skills/code-review/scripts/chain_check.py --baseline release/v0.22.4` on the branch, which reads this spec's `## Rule changes` (scenario S8) | 4d019bcc |
| 2 | `seal pr-checks` and the switch without the carry (*In* items 3 and 4), `bin/seal`'s comment, the mode gate's options (item 5), the bootstrap's three options (item 1), `templates/hygiene.yml`'s header, `templates/seal-README.md` and `seal/README.md`, `skills/config/SKILL.md`, `README.md`, `README.ko.md`, `CONTRIBUTING.md`, every test pin `spec.md` *Places* lists, and `changelog.md` from `spec.md` *Data & interfaces* | each rewritten pin seen red against phase 1's commit first; `bin/test tests/test_seal.py tests/test_mode_gate.py tests/test_first_setup_asks_once.py tests/test_the_mode_is_a_row_and_a_command.py tests/e2e/teammate -q`; `git grep -n -e 'workflows/hygiene' -e 'install_workflow' -e 'red forever'` outside `docs/`, `changelog/`, `CHANGELOG.md` and `seal/specs/` finds only the coordinates `spec.md` *Places* keeps | ce6b9afe |
| 3 | The reframe after round 3. In `tests/test_chain_check.py` `Test_retired`, the case for the no-root test's fifth answer, marked `nothing-declared-nothing-owed`: under `--worktree`, a switch to local run and not committed leaves no `seal` in the working tree, so nothing is declared (round 3 finding 2's draft, `spec.md` *In* item 6). S9: each of the five answers dropped by a mutant in turn, each mutant killed by a case, and where one survives, its case added. S8's applied half: this spec's 17 items replayed onto `docs/` at `02ee12de` in a scratch clone, and the modules whose code names a changed document, `README.md`, `README.ko.md` or `docs/` run over the result. `overview.md` from `templates/sdd-overview.md`, as the build's last phase. No source file and no changelog line change. A replay that fails is a divergence for the phase record and the hand-back, because `spec.md` is the framer's | the new case seen red against `gone = False` in the `if WORKTREE:` arm, then green; `bin/test tests/test_chain_check.py tests/e2e/teammate tests/test_unverified_check.py -q`; the five mutants of S9, each run once with `bin/test tests/test_chain_check.py -q`, the source restored after each, and the killing case named in `phases/phase-3.md`; the replay, the documents' modules green over the applied `docs/` except a case that also fails with `docs/` as committed, then `docs/` restored; `python3 skills/code-review/scripts/chain_check.py --baseline release/v0.22.4` for the parse half; `bin/test tests/test_chain_hooks_hardening.py -q` with `overview.md` in place (round 3, `## Not judged`) | |

## Operational impact

- **A consuming repository that already has the workflow keeps it**, byte
  for byte, pinned to the release that wrote it. Nothing in the plugin
  writes into a consuming repository at upgrade, and the `Mode` row the
  bootstrap wrote keeps the mode gate silent, so nobody is asked again. The
  fix of phase 1 reaches that repository's CI only when a person moves the
  pin: edit the `--branch v<old>` line, or run `seal pr-checks remove`, then
  `seal pr-checks install`, and commit.
- **A new first setup writes nothing under `.github/` by default.** A person
  who wants the checks answers the second option, or runs
  `seal pr-checks install` later.
- **`seal mode local` no longer removes the workflow.** The switch prints the
  command that does.
- No new dependency, environment variable or config row.
- Phase 3 changes nothing a consuming repository receives, so the changelog
  fragment stays as phase 2 and the fix passes left it.

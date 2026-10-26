# Implementation Plan: where the records live and whether CI checks pull requests are two answers (#952)

Approved 2026-10-26 by the orchestrator under the owner's automation answer, when `smith` was spawned for phases 1 and 2.

## Summary

Two phases. Phase 1 makes every step of `templates/hygiene.yml` pass a pull
request that declares nothing, and plants the case that keeps it so. Phase 2
splits the bootstrap's answer, gives the workflow its own command, takes the
workflow out of `seal mode`, and rewrites every text that said otherwise.
Phase 1 goes first because phase 2's new header and docs say a workflow left
in local mode examines nothing, which is true only after phase 1.

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

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `unverified_check.py`: the two exit-0 states of `spec.md` *In* item 6, its docstring's exit codes, and cases in `tests/test_unverified_check.py` marked `nothing-declared-nothing-owed`; the flow case `tests/e2e/teammate/test_teammate_flow.py` of *In* item 7, with the same marker | the case seen red at `02ee12de` on the two failing bases and green after; `bin/test tests/test_unverified_check.py tests/e2e/teammate -q`; `bin/test-layout --check tests/e2e/teammate/test_teammate_flow.py`; `python3 skills/code-review/scripts/chain_check.py --baseline release/v0.22.4` on the branch, which reads this spec's `## Rule changes` (scenario S8) | 4d019bcc |
| 2 | `seal pr-checks` and the switch without the carry (*In* items 3 and 4), `bin/seal`'s comment, the mode gate's options (item 5), the bootstrap's three options (item 1), `templates/hygiene.yml`'s header, `templates/seal-README.md` and `seal/README.md`, `skills/config/SKILL.md`, `README.md`, `README.ko.md`, `CONTRIBUTING.md`, every test pin `spec.md` *Places* lists, and `changelog.md` from `spec.md` *Data & interfaces* | each rewritten pin seen red against phase 1's commit first; `bin/test tests/test_seal.py tests/test_mode_gate.py tests/test_first_setup_asks_once.py tests/test_the_mode_is_a_row_and_a_command.py tests/e2e/teammate -q`; `git grep -n -e 'workflows/hygiene' -e 'install_workflow' -e 'red forever'` outside `docs/`, `changelog/`, `CHANGELOG.md` and `seal/specs/` finds only the coordinates `spec.md` *Places* keeps | ce6b9afe |

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

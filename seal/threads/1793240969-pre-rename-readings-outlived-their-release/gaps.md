# Closing memo: 1793240969-pre-rename-readings-outlived-their-release

## Why this work exists

Two readings of names from before the rename to AgenticSeal were promised
for removal in 0.24.0 and outlived it, because no issue scheduled them. Now
`chain-check` reads only the `Seal-Routing` trailer key, and the routing
parser reads the implementer's old name as unanswered.

## Where spec and implementation diverged

None. The frame held at this tree, and the build followed it.

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch | executed by the orchestrator's broad gate at `0c05299a` against `1e82fd0a`, passed (`trail/gate.md`), and this repository declares no typecheck (`seal/config.md` *Broad gate*; #951 would add one) |

## Not done

The other readings that a comment promised to drop in the minor release
after the rename stay, on `frame/questions.md` Q1's default (a). They read
files in a person's own install, and how long a straight upgrade from a
release before 0.23.0 is supported is a person's decision. The orchestrator
files one issue for them. Each one, with its coordinate:

- The CLAUDE.md block markers a release before the rename wrote, read by
  `install.sh` (`OLD_START`, `OLD_END`) and `uninstall.sh` (the same two),
  and described in `skills/update/SKILL.md`, the table row for a block
  between the old markers. The pin is
  `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py`,
  and the `KEPT_OLD_NAMES` items for both markers in `tests/censuses.py`
  stay with them.
- The clone line of a workflow a release before the rename wrote, read by
  `skills/implement/scripts/seal.py#OLD_PLUGIN_CLONE`, and described in
  `templates/setup/hygiene.yml` and `README.md`, the paragraph on
  `seal pr-checks install` after the rename. The pins are two cases of
  `tests/skills/test_seal.py`, and the `KEPT_OLD_NAMES` item for the clone
  line stays with them.

The sentence in `docs/the-routing-check.md` *At the pull request* that says
`chain-check` reads the old trailer key stays in this pull request. A pull
request does not edit the policy root, and the settle after this release
removes it from `frame/design.md` `## Rule changes`. Until then the
`KEPT_OLD_NAMES` item for the old key stays, because that sentence spells
it.

`.test_durations` keeps the two rewritten cases under their old ids and
has no entry under the new ones. Two cases fall far below the one in twenty
that `test_the_durations_file_prices_the_suite` allows, and `CONTRIBUTING.md`
refreshes the file from a `tests` run's artifact, which this branch has not
had.

## Fed back into the design

none

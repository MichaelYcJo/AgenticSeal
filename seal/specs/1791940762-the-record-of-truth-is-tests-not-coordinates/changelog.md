### Removed

- **The evidence ledger leaves the plugin (#944).** Over 45 releases the
  ledger re-read 1,421 prose claims and found 1,420 of them still true, and
  at most 91 false claims surfaced through drift in all that time. In
  0.21.0, 76 % of a release's ledger file was upkeep rows. The record of
  truth is now a test: a rule a policy document states ends with an
  `Enforced by:` line naming the case that holds it, and CI running the
  suite is the check. Gone with the ledger:
  1. the data: `seal/ledger.md`, the 45 `seal/releases/*.md` files and
     every `seal/ledger/<id>.md` fragment, which git keeps at `v0.21.1`
     (`git show v0.21.1:seal/releases/<X.Y.Z>.md`);
  2. the commands `evidence-check`, `correction-check` and
     `survivor-check`, with their `.cmd` twins, the fold
     (`fold_ledger.py`), the post-commit drift advisor and the pre-anchor
     ledger migration hook;
  3. the `evidence-check` and `evidence-ci` skills, `templates/ledger.md`,
     `templates/evidence-check.yml` and the demo GIF;
  4. the CI `ledger` job, the fold, correction and survivor hygiene steps,
     and the broad gate's `ledger`, `corrections` and `survivors` arms, so
     the gate runs `unverified` and `chain`;
  5. the `evidence-todo.md` and `survivors.md` file kinds, and the
     `Ledger frozen from` and `Removes from` rows of `seal/config.md`;
  6. `docs/the-evidence-ledger.md`, whose fold, settle and liveness rules
     moved whole into `docs/the-record-layout.md`.

  A repository that still runs `evidence-check` from an earlier release
  meets a wrapper that is gone; nothing reads a ledger file it keeps, and
  `seal export --check` counts a work item by its `specs/<id>/` directory
  alone. The coordinate kernel `fold-check`, `pact-check`, `chain-check` and
  the rider check import, cut from 7,270 lines to 545, moves from
  `skills/evidence-check/scripts/evidence_check.py` to
  `skills/verify/scripts/coordinates.py`, and `pact_check.py` moves beside
  it; `pact-check` is typed as before.

  | Deleted | Files | Lines | Bytes | Windows seconds |
  |---|---|---|---|---|
  | the ledger data | 47 | 5,938 | 4,389,886 | — |
  | test modules | 20 | 26,606 | 1,131,576 | 777.4 |
  | code (`fold_ledger.py`, `correction_check.py`, `survivor_check.py`, two hooks) | 5 | 5,104 | 238,269 | — |
  | the skills, templates and demo | 5 | 1,808 | 198,403 | — |
  | `docs/the-evidence-ledger.md` | 1 | 714 | 52,159 | — |
  | the three `survivors.md` records | 3 | 111 | 17,045 | — |
  | the `bin/` wrappers | 6 | 84 | 3,327 | — |
  | total | 87 | 40,365 | 6,030,665 | 777.4 |

  Measured against the merge base `f975ea66`: the branch is 4,302 lines in
  and 54,867 out, and 19.1 more Windows seconds left with cases cut from
  kept modules, so the suite's priced total fell by 796.5 seconds. Also
  gone: one ubuntu CI job per pull request, three hygiene steps and three
  gate arms. The pull request's own run measures the minutes saved; the
  frame's estimate is about 29 billed minutes a run.
  (`1791940762-the-record-of-truth-is-tests-not-coordinates`, #944)
- **`pact-check` grades the pact anchors in a signer's specs and nothing
  else (#944).** A signer's records of pact changes,
  `seal/pact-changes/<work-item-id>.md`, were written by the ledger's
  re-read, so nothing has written one since the ledger left. `pact-check`
  stops reading them and the pact's reviews in `seal/pact-reviews/`, so the
  `NOTED` line and the change counts on the `READ` line and in the summary
  are gone. The pact review procedure and `templates/pact-review.md` go
  with them, and `pact-check` no longer reads anchors in a signer's ledger
  files. The `Pact notify` row, which chose which of those records the
  pact's repository read, goes too: `pact-check`'s `READ` line and
  `chain-check`'s notice no longer print a notify value, and a row left in a
  config's table is read by nobody, refused by nothing and named by
  nothing, as `templates/config.md` §*Pact* says. With it goes the rule
  that refused every other line of `seal/config.md` naming a pact (#759),
  which never refused a real config. A row written below the table and
  above the next heading is still refused, as any row there is, and a
  `Pact` row the table does not hold reads as no row, so `pact-check`
  reports that signer as recorded on one side only.
  (`1791940762-the-record-of-truth-is-tests-not-coordinates`, #944)

### Added

- **Every `Enforced by:` target in a rule file must resolve, and the rules
  with none are counted (#944).** Two rows in `seal/budgets.md`, measured on
  every pull request: `enforced-unresolved`, a gate at 0, names each target
  that is gone, renamed, defined twice or a constant; and `unenforced:<file>`,
  one row per rule file, counts the bold-led rule paragraphs, a list item's
  indented continuation included, that carry no `Enforced by:` line or carry
  `nothing — <why>`. A new rule with no test
  raises its file's row and owes a `Budget raised:` line in the pull request
  body; a rule that gains its test lowers it. An eval case directory,
  `evals/behaviour/<agent>/<case>/` holding a `case.yaml`, is a target too.
  `bin/rules <doc>` prints a document's sections beside what each target's
  docstring says it guards, resolving the targets in the repository it is
  typed in, and writes nothing.
  (`1791940762-the-record-of-truth-is-tests-not-coordinates`, #944)

### Changed

- **The plugin's headline is the rule that names its test (#944).** The
  manifest's description and keywords, both READMEs and `SECURITY.md` no
  longer describe an evidence ledger with drift detection. The smith's proof
  block names the cases a work item added and how each was seen red, where
  it named ledger rows. Agents, skills and templates that sent a session to
  ledger rows now send it to the `Enforced by:` lines and the spec's
  Grounding. A record `round-record` refuses for an unclosed comment names
  `unverified-check` among its readers, where it named `evidence-check`.
  The warden is no longer told an evidence checker scans its committed
  report, and a bare symbol refused in a file no parser bounds no longer
  points at `--reverify`.
  (`1791940762-the-record-of-truth-is-tests-not-coordinates`, #944)

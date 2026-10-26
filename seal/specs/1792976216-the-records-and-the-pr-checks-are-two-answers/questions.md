# Questions for the planner: where the records live and whether CI checks pull requests are two answers (#952)

## Answered by the tree

The ticket left these open, and the tree answers them. Each names where the
answer was read, so a reader can overturn it by opening the same place.

1. **The empty root already passes.** A `seal/` root with an empty or absent
   `specs/` exits 0 in `unverified_check.py#settled_root` since `edd022ad`
   (#525). Executed: a teammate's pull request against a base holding only
   `seal/config.md` passes all three steps. The live failures are a root
   whose work items carry no `overview.md`, and no root at all (`spec.md`
   *Scope*, *What the tree says today*).
2. **`seal mode --check` needs no change, and `chain_check.py` needs one.**
   Executed: both exit 0 for a teammate's pull request on all three bases
   probed. The mode check judges the repository's state, which a teammate's
   change does not touch; a disagreement reaches a base only through a pull
   request merged red. Round 1 (finding 1, executed) found the chain step
   refusing the pull request that moves a root to local mode with the checks
   kept, so `spec.md` *In* item 6 reads no root at HEAD as nothing declared.
3. **The `Mode` row keeps its two values**, `local` and `shared`, read by
   `hooks/config.py#declared_mode`, the mode gate and `seal mode --apply`.
   Whether the checks are installed is not a place, so it is not a mode
   (`plan.md` *Alternatives considered*, row C). Q1 below holds the open half.
4. **The command's name is `seal pr-checks`, with the action words
   `install` and `remove`.** `pr-checks` uses the documents' own term, *the
   pull-request checks*, and is not one letter from the `--check` flag of
   `seal mode` and `seal export`. The verbs are the names of the functions
   that already do the work, `install_workflow` and `remove_workflow`, in
   `skills/implement/scripts/seal.py`. argparse's `choices` refuse any other
   word. It lives in `seal.py` beside `mode`, because that file already holds
   the whole writer and `bin/seal` already reaches it.
5. **`seal pr-checks install` refuses unless `<repo>/seal/` is a directory.**
   The checks read committed records (`templates/hygiene.yml` header), and in
   local mode nothing is committed. `remove` needs no root, because a
   workflow that outlived its root is the case it exists for.
6. **The bootstrap runs the command rather than writing the file by hand**,
   so the file has one writer (`plan.md` row J). The version one-liner leaves
   `skills/implement/orchestration.md`; `seal.py#plugin_version` reads the
   version from beside the script, and `tests/test_seal.py`
   `Test_plugin_version` pins it.
7. **The mode gate keeps three options** and names `seal pr-checks install`
   in its *Shared* option (`plan.md` row I).
8. **With no `seal/` root in the tree, `unverified-check` compares nothing
   against the base.** Otherwise the pull request that moves a root to local
   mode, with the workflow kept, fails the deletion arm (`plan.md` row H).
9. **Only a path whose last two parts are `seal` and `specs` takes the new
   exit-0 states**, as only that path is settled today (`docs/the-record-layout.md`
   *The fold, and what tells it from a deletion*). Any other path holding no
   `overview.md` stays exit 2 (`plan.md` row G).
10. **An existing shared-mode repository keeps its workflow and is not asked
    again.** Nothing the plugin runs writes `.github/workflows/hygiene.yml`
    outside `seal pr-checks install` after phase 2 (read: `git grep
    install_workflow`, whose only caller today is `seal.py#switch`), and a
    root with a `Mode` row is never asked by `hooks/mode-gate.py`. Its pin
    moves only when a person moves it (`plan.md` *Operational impact*).
11. **The case of item 4 lives at `tests/e2e/teammate/test_teammate_flow.py`
    with `TARGET = "templates/hygiene.yml"`.** `CONTRIBUTING.md` *The test
    layout* puts a flow across modules under `tests/e2e/<flow>/` and lets a
    case that reads a shipped document name it as `TARGET`.
12. **The `unverified-check` rule names a marker, `nothing-declared-nothing-owed`.**
    Its test drives a script that fails a pull-request job, and
    `skills/settle/SKILL.md` *A rule has one shape* asks a marker for such a
    rule.
13. **`templates/claude-md-block.md` is not changed.** It names no option and
    nothing installed; it sends a session with no root to the Bootstrap.
14. **This repository's own `.github/workflows/hygiene.yml` is not touched**,
    as the issue says.
15. **A changelog fragment is owed.** What a consuming repository receives
    changes: the default first setup, the command that writes the workflow,
    `seal mode`'s switch, and `unverified-check` at the next pin (`spec.md`
    *Data & interfaces*, last table).

## Open

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | The issue says the answer *is recorded where the mode row is, so `seal mode --check` and the hooks read one source*. Is a record in `seal/config.md` wanted, beside the workflow file? The tree cannot answer it because the ticket asks for it in words, and `CLAUDE.md` *The rule a mechanism is kept against* (a fact has one source; nothing is kept beside the tree to stay in step with it) asks the opposite, and a ticket ranks below policy (`skills/implement/SKILL.md` *1. Read the spec before the code*) | a person: the owner | (a) The workflow file is the record. `seal pr-checks` reads it, no row is added, and every existing repository reads correctly with nothing migrated. (b) A `Pull-request checks` row, written by the bootstrap and by `seal pr-checks`, and compared with the file by `seal mode --check`: a new disagreement that either fails a teammate's pull request that deletes the file, or is never read; an absent row in every existing repository has to be filled from the file. (c) A third `Mode` value: `Mode` answers two questions, and every existing `shared` repository with a workflow disagrees with itself after the upgrade | (a), built in phase 2 | open |
| Q2 | Does the flow case of phase 1 run on the Windows legs of `.github/workflows/test.yml`, where `bash` and a symbolic link to the tree may not be available? Reading cannot tell; a run on that leg can | a measurement: the pull request's CI run on `windows-latest` | (a) It runs there as on Linux. (b) It skips through `tests/conftest.py#symlink_or_skip` where `$RUNNER_TEMP/specseal` cannot be made to resolve to the tree, which costs nothing the template needs, since `templates/hygiene.yml` pins `ubuntu-latest` | (b) where the link cannot be made, (a) elsewhere | open |
| Q3 | Does `bin/test-layout --check` accept `tests/e2e/teammate/test_teammate_flow.py` with a document as its `TARGET`, and its classes as scenarios? The layout text allows both; only the checker's run says whether it reads them together | the work: phase 1, which records a divergence row where it moves the file | (a) As framed. (b) Another directory or file name the checker accepts, with the marker and the four bases unchanged | (a) | answered 2026-10-26 by the work: phase 1 ran `bin/test-layout --check tests/e2e/teammate/test_teammate_flow.py tests/test_unverified_check.py`, which printed `2 files read, 0 refused, 0 declare no TARGET`, so the file stays where the frame put it (`phases/phase-1.md`) |

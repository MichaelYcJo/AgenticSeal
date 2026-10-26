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
16. **The reframe after round 3 takes the round's two rule-change
    corrections into `spec.md` as written.** The `change` to
    `docs/the-review-and-parity-arms.md` wraps after "except where the tree",
    and the `add` to `docs/the-review-record.md` says a deleted declaration is
    otherwise "judged", the word of the paragraph *The check reads the diff as
    declarations*. Round 3 applied both and ran the five document modules its
    finding 1 names, 81 passed (executed by the round). The framer's own
    in-memory apply of the 17 items with `rule_changes.py#parse` and
    `apply_op` refused none and left no new line over 88 columns in
    `docs/the-review-and-parity-arms.md` (executed; no case was run).
17. **The chain step's no-root test keeps its working-tree reading under
    `--worktree`.** It reads the tree the declarations come from, and the
    one answer no case reached gets its case in phase 3 (`plan.md` rows K
    and L).
18. **A workflow pinned to a release newer than the installed one is a
    limit, not a version comparison.** The advice `seal mode local` prints
    there, followed, leaves a workflow that passes (`spec.md` *Out*). This
    closes the row rounds 2 and 3 carried under `## Not judged`.

## Open

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | The issue says the answer *is recorded where the mode row is, so `seal mode --check` and the hooks read one source*. Is a record in `seal/config.md` wanted, beside the workflow file? The tree cannot answer it because the ticket asks for it in words, and `CLAUDE.md` *The rule a mechanism is kept against* (a fact has one source; nothing is kept beside the tree to stay in step with it) asks the opposite, and a ticket ranks below policy (`skills/implement/SKILL.md` *1. Read the spec before the code*) | a person: the owner | (a) The workflow file is the record. `seal pr-checks` reads it, no row is added, and every existing repository reads correctly with nothing migrated. (b) A `Pull-request checks` row, written by the bootstrap and by `seal pr-checks`, and compared with the file by `seal mode --check`: a new disagreement that either fails a teammate's pull request that deletes the file, or is never read; an absent row in every existing repository has to be filled from the file. (c) A third `Mode` value: `Mode` answers two questions, and every existing `shared` repository with a workflow disagrees with itself after the upgrade | (a), built in phase 2 | open |
| Q2 | Does the flow case of phase 1 run on the Windows legs of `.github/workflows/test.yml`, where `bash` and a symbolic link to the tree may not be available? Reading cannot tell; a run on that leg can | a measurement: the pull request's CI run on `windows-latest` | (a) It runs there as on Linux. (b) It skips through `tests/conftest.py#symlink_or_skip` where `$RUNNER_TEMP/specseal` cannot be made to resolve to the tree, which costs nothing the template needs, since `templates/hygiene.yml` pins `ubuntu-latest` | (b) where the link cannot be made, (a) elsewhere | answered 2026-10-26 by a measurement: the `tests` workflow run 40264357704 on the branch at `895db45e` passed every leg, and on `windows-latest` (group 1) the flow cases ran rather than skipped, with `test_accepts_a_teammates_pull_request_on_every_base` taking 3.37s and `test_accepts_the_pull_request_that_moves_the_root_to_local_mode` 2.83s in the durations report, so (a) |
| Q3 | Does `bin/test-layout --check` accept `tests/e2e/teammate/test_teammate_flow.py` with a document as its `TARGET`, and its classes as scenarios? The layout text allows both; only the checker's run says whether it reads them together | the work: phase 1, which records a divergence row where it moves the file | (a) As framed. (b) Another directory or file name the checker accepts, with the marker and the four bases unchanged | (a) | answered 2026-10-26 by the work: phase 1 ran `bin/test-layout --check tests/e2e/teammate/test_teammate_flow.py tests/test_unverified_check.py`, which printed `2 files read, 0 refused, 0 declare no TARGET`, so the file stays where the frame put it (`phases/phase-1.md`) |
| Q4 | Does the class of round 1 finding 3, round 2 finding 1 and round 3 finding 1 earn a gate: a check or a case at the pull request that applies a spec's `## Rule changes` to the policy root and runs the documents' own cases over the result? Each of the three was a case green on the branch and red at the settle, and each was found by a reviewer's replay. The tree cannot answer it, because it adds a gate over every unsettled spec, and `CLAUDE.md` *The rule a mechanism is kept against* weighs a mechanism by what it catches against what it costs, which is the owner's judgment. The answer does not change what #952 builds | a person: the owner | (a) No gate. A frame's acceptance carries the replay as a probe, as S8 does here, and a reviewer builds it. (b) An issue of its own, for a check that applies each judged spec's items and runs the cases that read the changed documents. It has to decide what it does with the specs the merge-order replay already refuses for reasons outside the pull request, three today (round 2, `## Not judged`). (c) A case in `tests/` over every unsettled spec: it goes red on those three specs today, so it needs the same decision first | (a) for this work item; the orchestrator relays the row to the owner in the pull request body | open |

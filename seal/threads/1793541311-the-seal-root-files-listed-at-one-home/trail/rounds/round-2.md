# Review round 2: 1793541311-the-seal-root-files-listed-at-one-home

```seal
target: 32c50daa, fixes 2dfbc3fe..32c50daa
```

This is a verifying round over the diff of round 1's fixes, and it stays inside that diff. The diff changes four paths: `README.md`, `README.ko.md`, the work item's `changelog.md` and `trail/rounds/round-1.md` (executed: `git diff --name-only 2dfbc3fe..32c50daa`). The change to `round-1.md` is the close block of finding 1 and nothing else (executed: `git diff 2dfbc3fe..32c50daa` over that file). `seal/` declares no `parity.md`, so the round block holds no `original:` line. `seal/config.md` has no `Record language` row, so the record is English.

Carried from round 1 rather than re-established: the class probe's method and its reading of the hits outside the two README rows (round 1 *Probes*, first row), the period between merge and settle in which `docs/the-record-layout.md` *seal/* lacks the `parity.md` and `pact.md` rows (round 1's seventh confirmation), and the parse of the design's `## Rule changes`. The diff touches none of `docs/`, `frame/` or the rule changes, so no check of those facts fails. Re-derived this round: the text of both README rows, the citations they add, whether the class probe still finds a root list in either README row, the truth of the rewritten fragment, and every verdict below.

The axes walked: whether the close of round 1's finding 1 holds, in both editions; whether the rewritten rows drop a fact the old rows carried; whether the new citations are read by the check that holds them and can fail; whether the fragment's new sentences are true of the tree; and whether `trail/phases/phase-1.md:37` must change. Inputs, authorization, query scope, ordering, concurrency and security have no subject here: the diff changes prose in two READMEs and one record, and no code path.

## Findings

None.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the close `fixed f907c6ee`. `README.md:117` and `README.ko.md:112` now carry round 1's two paste-ready rows word for word, each linking `docs/the-record-layout.md` *seal/* in place of the short list, and the rest of each row is unchanged (read, `git diff 2dfbc3fe..f907c6ee`). Round 1's class probe, written again from its *Probes* row with the Korean spellings added, matches both README rows at `2dfbc3fe` and neither at `32c50daa` (executed). At `32c50daa` the lists of the root's files it finds are the four drawn trees. Every other hit stands in a file the fix diff does not touch, so round 1's reading of those units, as naming two files for another reason, carries. The Korean row's citation is read by the check: with `*seall/*` planted at `README.ko.md:112`, `test_every_cited_section_stands_in_its_file` failed and named `README.ko.md:112` (executed). This re-runs a sample of the fix pass's coverage claim; the English row was not planted this round. *seal/* stands as a section at `docs/the-record-layout.md:267` (read).

```seal
confirms: none
```
What matched: the rewritten rows lose no fact. The old English row said the config holds "the two language rows and the mode". That fact still stands in the same README, in the tree's `config.md` entry at `README.md:124`, and in the Korean edition at `README.ko.md:119` (read). The other facts the old lists named, the follow-up list and the migration config, stand in the same trees and in `docs/the-record-layout.md` *seal/* once the settle writes the design's rule changes.

```seal
confirms: none
```
What matched: the fragment's new sentences are true of the tree. `changelog.md` now counts five passages that listed some of the root's files: the lifetimes table's row, the two README rows, the export docstring and the flow log's location row. It says the first four left out `README.md` and `pact.md`, which is true of the two old README rows (read, `git show 2dfbc3fe:README.md`, line 117, and the Korean edition, line 112). Its headline now says every other place "in the skills and the README" links the home. The README's tree lists the files rather than linking them, and the fragment's last sentence names the four trees as the ones that stay and list the six entries. A reader of the entry therefore meets the exception in the same entry, so this is no finding (read).

```seal
confirms: none
```
What matched: `trail/phases/phase-1.md:37` stands, and its sentence is no finding. The sentence claims that design *Scope* leaves `README.md:117` to #1102. Round 1's finding 1 showed that claim wrong, and the close block at `trail/rounds/round-1.md:39-42` says so and names the line. `agents/crafter.md` *A fix pass appends close blocks and writes no phase record* forbids the fix pass to amend the phase record, so the line is the build's account of phase 1 at `f15fcb33`, dated by its commit, and not a statement of the tree in force. Its reader before the merge is the sealer, which reads the round records beside it and so meets the correction, and the settle after the release removes the work item's directory. No reader is left with the wrong claim alone. The design is also still true where it speaks: `frame/design.md:44` gives grounds for the README trees alone, and those trees are unchanged (read). The README rows changed through round 1's finding, which the close records, and not through a frame item.

```seal
confirms: none
```
What matched: the narrow run over the changed paths. Every module under `tests/` that names `README.md` or `README.ko.md`, 42 of them without `conftest.py` and `censuses.py`, together with `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, gave 2622 passed and 1 skipped in one `bin/test -q` at `32c50daa` (executed). The fix pass reports 44 modules and 2798 passed. Its set adds the line-wrap and census modules to the same list, so the counts differ by the set and not by a failure. This is a probe and not the seal.

```seal
confirms: none
```
What matched: the labels. `gaps.md` *Not verified* still names the orchestrator, by `seal gate`, for the full suite, the lint and the format check at the branch's head, and the fix pass ran no broad command (read). This round leaves nothing open. What comes due is the orchestrator's broad run with `seal gate`, then the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD | the branch at `32c50daa` | the orchestrator, by `seal gate`, now that the rounds settle |
| S3 and S4: the settle writes the *seal/* table with six rows, and the record layout alone for the layout file by file | `frame/design.md` *Rule changes* | the repository owner, at the settle after 0.27.3 |
| S5 at the pull request: `chain-check` reads the three `change` items and refuses nothing | the `hygiene` workflow's chain step | the pull request's CI |
| A list of the root's files worded in a way neither P1, P2 nor the class probe matches, in English or Korean | the tracked tree outside `seal/threads/` | open: no method lists the class whole (contract rule 12) |

## Probes

All probes ran in `<scratchpad>/1793541311-the-seal-root-files-listed-at-one-home/round-2/clone`, a `git clone --no-local` of the worktree checked out at `32c50daa`. The probe file was deleted, and the planted citation was restored with `git checkout --`; `git status --short` printed nothing afterwards.

| Command | Result |
|---|---|
| `python3 test_tmp_root_lists.py`: every paragraph and table row of a tracked `.md`, `.py`, `.yml`, `.txt`, `.toml` or `.json` file outside `seal/threads/` and `tests/`, kept where it names two or more of the root's entries, with the Korean spellings of the follow-up list, the repository's config and the migration config added | at `32c50daa`, 23 units, and none is `README.md:117` or `README.ko.md:112`; the lists of the root's files are the trees at `README.md:121`, `README.ko.md:116`, `seal/README.md:81` and `templates/setup/seal-README.md:81`. At `2dfbc3fe` the same probe matches `README.md:117` and `README.ko.md:112` |
| `git diff --name-only 2dfbc3fe..32c50daa` | four paths: `README.md`, `README.ko.md`, the work item's `changelog.md` and `trail/rounds/round-1.md` |
| `bin/test -q` over the 42 modules under `tests/` that name `README.md` or `README.ko.md`, without `conftest.py` and `censuses.py`, and `tests/behaviour/test_a_cited_section_stands_in_its_file.py` | 2622 passed, 1 skipped, exit 0 |
| `bin/test -q -p no:xdist tests/behaviour/test_a_cited_section_stands_in_its_file.py` with `*seall/*` planted at `README.ko.md:112` | exit 1, 1 failed and 42 passed; `README.ko.md:112` was named as citing `*seall/*` |

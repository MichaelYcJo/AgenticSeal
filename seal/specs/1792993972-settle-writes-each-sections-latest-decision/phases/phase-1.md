# Phase 1: 1792993972-settle-writes-each-sections-latest-decision

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | a8e6a2f9 |

## What this phase was asked

`settle` groups the released specs by section, shows each group's history and
the open rows, and removes directories; it no longer writes `docs/`.
`rule_changes.py` and `settle.py` change as the plan says,
`skills/settle/SKILL.md` becomes the settling session's procedure, and the
other places `spec.md` *In* item 7 lists are rewritten. Run the read-only dry
run on the real tree (S10) and record what it prints. Q3 and Q4 are answered
by this phase's work; Q1 builds on its default, one issue per distinct
measurement.

## What this phase found

**The frame holds, with two exceptions about its removal list** (`read`).

- **`replay`, `apply_op` and `_cut` cannot leave `rule_changes.py` in this
  phase.** `unverified_check.py#settled` calls `rules.replay` (lines 1316 to
  1318 at `0408fccf`), and phase 2 is the phase that rewrites `settled`.
  Removing them here would leave `settled` raising `AttributeError` for any
  removed directory that states a rule, between the two commits. So phase 1
  removes `conflicts`, and `replay`, `apply_op`, `_cut` and
  `tests/test_rule_changes.py::Test_replay` go in phase 2 with their last
  caller. The module docstring says `replay` serves `settled` until then.
- **`_ancestor` stays.** `spec.md` *Data & interfaces* says `rule_changes.py`
  loses `_ancestor`, and S5 asks that two specs whose adding commits no
  ancestry orders be marked inside their group. Marking them needs the
  ancestry read, so `_ancestor` stays and the new `unordered` reads it.
  `rule_changes.py` therefore gains three functions where the spec names one
  grouping function and a section-range finder: `group`, `section_lines` and
  `unordered`. This divergence goes to `overview.md` in phase 2.

**Q4, the dry run's shapes** (the work). The dry run prints a three-line
summary, then each group as `group N`, its places as `place: <file> section
\`<section>\`, at <file>:<first>-<last>` (or `: <why> in the working tree`),
and its operations numbered in merge order as `<kind>  <id>
seal/specs/<id>/spec.md:<line>  from found, to not found`; a whole-section
`remove` says `the whole section`. An unordered pair is one `unordered:` line.
Then the specs to read whole, the no-change block, the directories with no
`spec.md`, the open rows with their named paths, what `--apply` removes (`now`
or `once its N open rows close`), and the readers. `--apply` prints `removed
<dir>/` with each closed row and `what closed it:`, or `kept <dir>/: its
record holds N open rows; ...` with each row, then `fold-check`'s lines, then
`removed N directories; kept M, each with a row to close`. Each shape is
pinned in `tests/test_settle.py`.

**A named path is looked for in three places** (the work). A backticked span
counts as a path when it holds a `/` or is a file name with an extension this
repository uses (`.py`, `.md`, `.cmd`, `.sh`, `.ps1`, `.yml`, `.yaml`,
`.json`, `.toml`, `.txt`), so `cmd.exe` and `str.strip` are not paths. It is
in the tree when it exists from the root, from the work item's own directory
(`questions.md`), or, for a bare name, as a tracked file's name
(`broad_gate.py`). The first S10 run, before the second and third places,
reported every `questions.md` and `spec.md` as not in the tree.

**Every released directory now leaves alike.** With no open row, a spec with
no `## Rule changes` goes like any other, so the `tree` fixture's three
section-less specs are removed by `--apply`, and the kept cases that leaned on
them staying were rewritten (`Test_apply::test_accepts_every_released_directory_with_no_open_row`).

**Which retired cases were kept, and why** (`read`). Kept where the behaviour
stays: the readers and citations case (rewritten to the new heading and to
`now` and `once its 1 open row close`), the team `specs/` case, the unreadable
memo (renamed `test_refuses_...`), the unreleased directory, the moved spec
(rewritten to read the group's order, since `--apply` no longer orders
anything), the spec no commit adds (rewritten to the `unordered` mark), the
ceiling case, the local-mode and opt-out refusals, and the settled root. The
case-insensitive name case went: with no document written, two names on one
disk overwrite nothing. `tests/test_settle_reads_before_it_removes.py`'s
`test_the_documents_say_a_spec_less_directory_is_retired_by_the_rule` keeps
its `docs/` half, which stays true until the settle writes that section, and
its skill half now reads *it leaves like any other*.

**The cases were seen red against `0408fccf`** (`executed`). The new
`tests/test_settle.py`, `tests/test_rule_changes.py` and
`tests/test_settle_reads_before_it_removes.py` were copied into a scratch
clone at `0408fccf` and run there: 17 settle cases, all 10 `Test_group` and
`Test_section_lines` cases, and 9 skill and README cases failed. In the
working tree all pass. A mutation of the bare-name lookup survived the first
cases with every case green, so the open-row case names `one-root.md`;
`a8e6a2f9` holds that change, and the mutant is now red.

**S10 over the real tree** (`executed`: `python3
skills/settle/scripts/settle.py --released-at origin/main`, exit 0, with
`origin/main` at `67694cba`, read-only, no `--apply`). Its summary:

```
released at origin/main: 41 work items; 5 unreleased and untouched
    6 state rule changes, 35 hold the no-change block, 0 to read whole, 0 wrote no spec.md
    48 groups; 62 open rows in 41 records
```

- 48 groups and 90 operations from the six specs `1792533444`,
  `1792540458`, `1792619408`, `1792624592`, `1792627930` and `1792628098`.
  Nothing is refused, no pair is marked unordered, and every place's heading
  is in the working tree.
- The groups span 15 documents: `docs/worktree-guard-spec.md` (7 places),
  `docs/the-record-layout.md` and `docs/the-review-record.md` (6 each),
  `docs/the-review-and-parity-arms.md` (5), `docs/commit-review-gate-spec.md`,
  `docs/one-root-by-lifetime.md` and its `.ko.md` edition,
  `docs/release-checklist.md` and `docs/the-pact.md` (4 each),
  `docs/issues-and-milestones.md` (3), `docs/branch-and-release.md`,
  `docs/measuring-a-run.md`, `docs/the-agent-set.md` and
  `docs/the-broad-gate.md` (2 each), and `docs/README.md` (1).
- Eight groups hold more than one spec: groups 3, 4, 6, 8, 9, 13, 14 and
  15. Group 8, `docs/the-review-and-parity-arms.md`, holds seven operations
  from three specs across five places.
- Two `from` values are not found: `1792619408` at `spec.md:196` (section
  *What the check reads at the pull request*) and `1792627930` at
  `spec.md:279`. Two `to` values are already found: `1792628098` at `spec.md:338` and
  `spec.md:453`.
- **Q3**: the reader counts 62 open rows in the 41 records, every record
  holding at least one, the same 62 the framer's `awk` walk gave. 8 named
  paths are not in the working tree.
- `what settle --apply removes` lists all 41 as `once its N open rows
  close`; 60 lines list the `tests/` readers of `seal/specs`.

**S12** (`executed`): `rule_changes.py#parse` over this work item's `spec.md`
reads 8 operations and no error.

**One case of the narrow run fails and is not this phase's**
(`executed`): `tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`
names this work item, which has no `overview.md` until phase 2 writes it. It
failed the same way at `0408fccf`, where the frame's directory already stood.

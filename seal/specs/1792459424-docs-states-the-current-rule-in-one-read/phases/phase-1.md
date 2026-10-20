# 1792459424-docs-states-the-current-rule-in-one-read — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | f60117a3 |

## What this phase was asked

The `check:` line in the grammar of `spec.md` *Data & interfaces*: the
no-target form `check: none reader: <who reads it>`, every other spelling
refused at `<path>:<line>` with exit 1. The resolver moved into `rules.py`,
`fold-check`'s shape arm and the `Fold shape from` row removed, the `rule`
pytest marker registered and carried by the gate tests. Every label line
converted by a one-shot script in the scratchpad that asserts its counts, the
18 `nothing` lines by hand. The prose naming the label rewritten in the same
commit, and the cases pinning the old label updated.

The owner's direction for the build: no symbol a reader can trip on as
syntax, no value stated twice, no spelling a near miss could pass, the rule
once and no narrative. Beside the touched modules, the seven repository-wide
meta modules, `bin/rules --check`, `bin/fold-check` and ruff run at the phase
boundary, because #953's narrow runs passed while four meta cases failed in
CI.

## What this phase found

- **The base held 243 label lines, not 240.** Three in
  `docs/the-record-layout.md` stand indented under list items, and git's ERE
  reads `\s` in `git grep -E '^\s*Enforced by:'` as no match. The reader
  counted 243 at ac83bdf3. Two statements left with their subject: the shape
  rule and the `path::name` resolver rule. The other 241 were converted: 223
  by the script, 18 by hand.
- **Which rules carry a marker was measured, not guessed.** A trace plugin
  ran the 442 tests the base's lines named (1144 cases) and recorded each
  gate entry point a test drove: `main` called in process, a process started
  with the script in its argv, or git running a hook. The gate entry points
  are the PreToolUse commit gate, the two git hooks that can refuse, and the
  scripts of the `hygiene.yml` steps. 69 tests drove one, and 33 lines named
  such a test. The worktree guard's three lines were left on files: their
  tests drive `dispatch.py pre-bash` to refuse a worktree creation, not a
  commit. So were the three of `docs/the-broad-gate.md`: `broad-gate` runs
  the checks outside any commit or job. 27 lines carry a marker, and 140
  decorators sit in 22 test files. Every `::` test a marker line named
  carries its marker, so the marker names the old set exactly.

  | Marker | Rule file |
  |---|---|
  | `executed-text-is-read`, `one-heredoc-shape-is-data` | `docs/commit-review-gate-spec.md` |
  | `second-gather-appends` | `docs/release-checklist.md` |
  | `judged-inside-the-commit`, `a-persons-own-commit`, `how-a-stop-is-put`, `sealed-off-the-branch-refused`, `no-verify-met-where-the-branch-moves`, `gits-own-commits-not-judged`, `text-reading-stands-aside` | `docs/the-commit-gate-inside-git.md` |
  | `a-settle-is-no-deletion`, `an-empty-root-is-settled`, `one-merge-base` | `docs/the-record-layout.md` |
  | `review-arm-asks`, `routing-read-first`, `two-review-answers`, `a-declaration-removed` | `docs/the-review-and-parity-arms.md` |
  | `location-touched-by-fix`, `fix-pass-two-lines`, `judged-where-carried`, `round-record-read-by-label`, `last-record-at-head`, `old-table-shape-refused`, `ready-needs-sealed`, `stamp-drawn-once`, `refused-sealed-leaves-a-record`, `run-ends-with-verifying-round` | `docs/the-review-record.md` |

- **Every other line names files.** A file named twice in a line is named
  once. `S7`'s comparison holds: of the 106 paths the base named, the two no
  line names now are `skills/settle/scripts/fold_check.py` and
  `tests/test_a_folded_statement_names_what_enforces_it.py`, both `## Removes`
  rows.
- **The hand conversions.** 17 `nothing` lines became
  `check: none reader: <who>`, the reader taken from the old reason; a reason
  that said more than who reads it stayed as a prose sentence above the line.
  `docs/measuring-a-run.md`'s line named a test for half its rule, so it now
  names `tests/test_session_cost_post.py`, and the gap is a sentence. The
  reason on `docs/branch-and-release.md`'s line described a marketplace
  record, not its paragraph about closing issues; it reads `review` now, and
  phase 7 owns that document.
- **The grammar is stated in `skills/settle/SKILL.md` *A rule has one
  shape*,** where a consuming repository reads it; `rules.py`, the implement
  skill and both READMEs point there. `spec.md` *Data & interfaces* keeps the
  frame's copy until the directory goes (overview).
- **`rules.py` reads markers with `ast`,** into an `if`, a `try` or a `with`
  as pytest collects, and skips every directory whose name starts with a dot:
  a virtual environment holds `test_*.py` files that may not parse here. A
  marker on a class marks its methods, and `rules <doc>` prints the class
  docstring.
- **Readers the shape arm left without a caller.** `coordinates.py`'s
  `named_unit`, `unit_kinds` and `_parsed_kinds` resolved `path::name` and
  nothing else, and went with their case (overview). The enforcement pairing
  of `tests/test_both_editions_carry_the_same_folds.py` read
  `fold_check.numbered_statements`, so it went in this phase rather than with
  the marker arm in phase 2.
- **For phase 2:** `FOLD_MARKER` is still read by the outline arm's marker
  count in `tests/test_both_editions_carry_the_same_folds.py`, the marker
  exemption in `tests/test_docs_line_wrap.py`, and `gather_changelog.py`.
- **For phase 3:** `unverified_check.py#NOTHING` is now read by
  `rule_changes.py` alone.
- **For phases 5 and 9:** after the conversion `fold-check` estimates
  `docs/worktree-guard-spec.md` at 33,802 tokens and
  `docs/one-root-by-lifetime.ko.md` at 28,170.
- **The checks at the boundary (executed):** `bin/rules --check` exit 0, 241
  check lines in 61 rule files; `bin/fold-check` exit 0, the two documents
  above named; 51 modules (every touched test module, the nine whose strings
  hold a node id, and the seven meta modules) run, and the six cases that
  failed rerun green once their pins and this item's `overview.md` were
  written; ruff check and format over the 47 changed Python files clean. Each new or rewritten case of the rules, fold-check and wrap
  modules was run red against a copy of cbd4c91b first. Every unit added to
  `rules.py` and `tests/conftest.py` was broken once with `mutation-check`,
  and each run was red.

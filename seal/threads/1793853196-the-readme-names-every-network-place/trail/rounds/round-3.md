# Review round 3: 1793853196-the-readme-names-every-network-place

```seal
target: e6221756, fixes 50cae2cd..e6221756
```

This is a verifying round. It read the diff `50cae2cd..e6221756`. That diff
holds round 2's record (committed at b8b42b93), the orchestrator's fold
c9f27afb, the fix commit 8e605e8c, the phase record's update 0c820872 and
the close block at e6221756. The round answers round 2's finding 1, closed
`fixed 8e605e8c`. It also reads the new README text as prose a directory
reviewer reads. The record language is English, since `seal/config.md` has
no `Record language` row. No `seal/parity.md` is declared.

Facts carried from earlier rounds and not re-derived: the census of network
calls under `hooks/`, `skills/` and `bin/` (round 1 *Probes*), since this
diff changes no code; the dependency install `uv run` makes, which the
phase record probed; and that `uvx ruff` asks for no Python the project
pins (round 2 *Probes*, third row), since the `uvx` sentence is unchanged.
The fix diff adds no test, so no new test is read against its group.

The crafter's account was read as claims.

- It claimed an offline probe of a project with `[tool.ruff]` alone and
  `.python-version` set to `3.10` exited 2 with "A managed Python download
  is available for Python 3.10". This round ran that shape and the
  `[project]` shape with `requires-python = ">=3.9"`. Both exited 2 with
  that hint (executed, *Probes*).
- It claimed five narrow modules exit 0 before and after the rewrap, and
  did not name them in the account this round received. This round ran
  round 2's six modules at e6221756, the line-wrap and folds modules among
  them. They exit 0, 142 passed (executed).
- It claimed `chain_check.py --worktree` exits 0 and reads the close block
  as `fixed 8e605e8c`. This round ran the same check with this record in
  place (*Probes*).
- It called its `git grep` for "requires-python" and "python-version"
  complete for those words and a sample otherwise. That label is honest.
  The closed set of contract rule 12 is this diff and the work item's
  files that state the present. This round searched them, and the tree,
  for "requires-python", "python-version", "managed Python" and the
  download wording in both languages (executed). Every hit is in the diff,
  in `trail/phases/phase-1.md:38-42` as an account of round 1, or in a
  `.github/workflows/` `python-version:` key that is no statement of this
  fact. `frame/design.md:186` names "the Python it downloads" with no
  condition, and `frame/plan.md:74` is a dated judgment row, so both stay
  true.
- It labelled the full suite `unverified`, which is honest under contract
  rule 2.

## Findings

None.

## Confirmations

```seal
confirms: round-2#1
```
What holds: both editions now tie the Python download to a version the
project asks for and the machine lacks, not to `requires-python` in a
`[project]` alone. `README.md:311-313` reads "Where a project asks for a
Python version the machine does not have, such as through a
`.python-version` file or `requires-python`, uv first downloads that
version from GitHub" (read). "a project" no longer refers back to the
`[project]` clause before it, so the `[tool.ruff]`-only shape is covered.
`README.ko.md:314-316` says the same, with "등으로" standing for "such as"
(read). `changelog.md:3` ends with the same condition and "with or without
a `[project]` table" (read). The two probe shapes of round 2 both exit 2
with the download hint at this tree's uv, 0.9.18, and this machine has no
Python 3.10 (executed). So each shape the finding named falls inside the
new sentence.

The crafter wrote its own sentence rather than round 2's snippet. Its
grounds hold: the orchestrator's row at `frame/plan.md:75` asks for the
condition named by what the person sees, without listing every uv setting.
That row also answers round 2's `## Not judged` row on uv's own settings,
such as `python-preference` and `UV_PYTHON`, so this round does not raise
it again. The sentence states no claim those settings make false: it says
where uv downloads, and does not say uv downloads nowhere else.

What matched: the fold c9f27afb states the same condition in census row 2
at `frame/design.md:56` and in *Scope* 1 at `frame/design.md:96-102`
(read). Both now agree with the README and the changelog.

What matched: `trail/phases/phase-1.md:38-49` keeps round 1's account and
adds round 2's reopening and 8e605e8c (read). Round 1's condition stands as
what round 1 found, and the new sentences state what 8e605e8c did. HEAD
contradicts neither.

What matched: read as prose, the English sentence is one clause of
condition and one of action, and "that version" points back to it. The
Korean sentence reads the same way and keeps the subject 프로젝트 for
요구하는. Both paragraphs wrap within the line-wrap check's limit, and the
folds and paste checks pass (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD; contract rule 2 keeps them from this round, and the crafter's `unverified` label for them is honest. This round leaves nothing open, so the broad run is what comes due, and the sealer's spawn after it | `seal/config.md` `Broad gate` row | the orchestrator's broad run |
| Whether `CONTRIBUTING.md`'s hook rule widens to every shipped network call; the build took default (a) | `frame/questions.md` Q1 | the owner, through the orchestrator's report |
| Whether the plugin directory's reviewer reads a true README at the next `dist` commit | `frame/design.md` S8 | the owner |

## Probes

| Command | Result |
|---|---|
| `uv run --offline ruff --version`, uv 0.9.18, scratch `UV_CACHE_DIR` and `UV_PYTHON_INSTALL_DIR`, in a project with `[tool.ruff]` alone and `.python-version` set to `3.10` | exit 2: "No interpreter found for Python 3.10 in managed installations or search path", hint "A managed Python download is available for Python 3.10, but uv is set to offline mode" |
| The same, in a project with `[project]`, `requires-python = ">=3.9"`, `[tool.ruff]` and `.python-version` set to `3.10` | exit 2, the same error and hint |
| `uv python list --only-installed` | CPython 3.9, 3.11, 3.12, 3.13, 3.14 and 3.15; no 3.10 |
| `bin/test -q` over `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_both_editions_carry_the_same_folds.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/behaviour/test_release_hygiene.py` and `tests/hooks/test_version_check.py`, at e6221756 | exit 0, 142 passed |
| `git grep -n` for "requires-python", "python-version" and "managed Python" over the tree, and `git grep -n -i` for "download", "내려받", "python build" and "interpreter" over both READMEs, `CONTRIBUTING.md`, `docs/`, `hooks/lint-python.py`, `skills/`, `agents/` and `templates/` | the diff's own lines, `trail/phases/phase-1.md:38-42`, the frame's dated row `frame/plan.md:74`, `.github/workflows/` `python-version:` keys, and interpreter lines in `skills/verify/` and `templates/setup/config.md` that are not about lint-python |
| `python3 skills/code-review/scripts/chain_check.py --baseline 31558c76 --root` the branch worktree `--worktree` | exit 0, with the plugin's 0.32.3 copy and with the tree's copy alike. It printed that no pull request exists yet, and that `trail/gate.md` and `guarantee.md` are not yet written, which the broad run and the sealer write. It printed no notice at a line of `frame/design.md` |

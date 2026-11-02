# Review round 2: 1793591507-the-settle-reads-what-earlier-settles-judged

```seal
target: ed12660ea, fixes e59ec5995..ed12660ea
```

The target is the fix pass over round 1: `0e45a9122`, `29bbfba17`,
`8c38dcf69` and the close blocks at `ed12660ea`. It changes
`skills/settle/scripts/settle.py#earlier_judgments`, its paragraph in
`skills/settle/SKILL.md` *What the dry run shows*, three cases in
`tests/skills/test_settle.py` and one paragraph of `gaps.md` (executed: `git
diff --stat e59ec5995..ed12660ea`). The round stays inside that diff. No
`seal/parity.md` is declared, so no `original:` line is owed.

Carried from round 1, not re-established: the replay counts over this
repository's history (74 rows, 41 groups, 18 work items), the confirmations
of the section's shape and of the S2 pin, and the three edges it judged not
worth a finding. The fix diff touches none of them except the reading
itself, and the narrow run below covers that. Round 1's probe for finding 1
is replaced by a stronger check: the case the fix pass committed, run against
the code round 1 reviewed.

Claimed by the fix pass: the `-z` parse was checked against git's bytes,
each new case went red with its guard alone removed, and two readers of the
same class lie outside this work item and went to #1283. Each claim was
checked, as the confirmations below say.

## Findings

This round opens no finding, and none is a `must`.

## Confirmations

```seal
confirms: round-1#1
```
What holds: a removed plan whose work item id holds a character past ASCII
is read. `earlier_judgments` reads `git log -z` and splits on NUL
(`skills/settle/scripts/settle.py:1114-1140`, read). The parse was checked
against git's own bytes over `origin/main` (executed: the same `git log`
command, read through Python). Each commit's field ends in a NUL, and the
first path after it opens with a newline, which `lstrip("\n")` removes. The
last path of one commit is followed directly by the next commit's U+0001.
All 5 commit fields were found, and every other non-empty piece was a path
under `seal/threads`. No path can open with U+0001 or a newline, because
`REMOVED_PLAN_RE` wants it to open with `seal/threads/`. The case
`Test_main::test_a_removed_plan_of_a_non_ascii_id_is_read` was run alone
against `settle.py` as it stood at `e59ec5995`, and it failed at its last
line, `assert f"\n    {old}  " in text`: the output named only
`1700000002-new` (executed). At `ed12660ea` it passes. The class was listed
by the fix pass from every `git` call in `settle.py` and `rule_changes.py`
that prints a path. This round re-listed the calls in all four scripts under
`skills/settle/scripts/` (executed: `grep` for `--name-only`, `ls-tree`,
`ls-files`, `--name-status` and `diff`), and the list matches.
`fold_check.py` and `passages.py` call no `git` that prints a path.
`settle.py#released` and `rule_changes.py#order` are the two left. #1283's
comment names both, with the fix pass's probe (read, through the
code-hosting service's command line tool).

```seal
confirms: round-1#2
```
What holds: `--no-renames` has a case. With `--no-renames` alone removed
from `skills/settle/scripts/settle.py:1118`,
`Test_main::test_a_plan_deleted_where_another_is_added_is_still_read`
failed at `assert f"\n    {old}  " in text`, and the 8 other cases on
removed plans passed (executed). The case sets `diff.renames` in the probe
repository's own config, so a person's global setting does not change what it
tests. `gaps.md` *Not done* no longer gives the wrong grounds. Its
paragraph names `--full-history` alone, with the grounds round 1's first
edge gives (read, `gaps.md:13`). The docstring and the skill's paragraph say
what `-z` and `--no-renames` each keep, and both statements match the code
(read, `settle.py:1104-1107`, `skills/settle/SKILL.md:224-229`).

```seal
confirms: none
```
What matched: the third new case, beyond round 1's text, pins
`--no-show-signature`. With that flag alone removed,
`Test_main::test_a_signed_removal_is_read_under_any_show_signature` failed
at `assert f"\n    {old}  " in text`. It ran on this machine and did not
skip (executed). Without the flag, `log.showSignature=true` puts the
signature check ahead of the U+0001 field, so `startswith("\x01")` fails
and the commit is never set. The case copies the shape of its group's
signed-commit case, `test_a_signed_commit_is_read_under_any_show_signature`
(`tests/skills/test_settle.py:2796`, read): the same key setup, the same
skips, and the same override of `GIT_CONFIG_COUNT` through `monkeypatch`.

```seal
confirms: none
```
What matched: each new case covers something its group does not. In each
of the three mutant runs, exactly one case of the nine on removed plans
failed, and it was the case written for that flag. `bin/seal layout
--pairs` printed no pair from `tests/skills/test_settle.py` (executed).

```seal
confirms: none
```
What matched: the slice passes at `ed12660ea`. `tests/skills/test_settle.py`
passed 159 cases. The 23 modules that name `settle/SKILL.md`,
`settle/scripts/settle` or `"settle"` passed 1716 cases (both executed,
`bin/test` in the clone). `uvx ruff check` and `uvx ruff format --check`
passed on `settle.py` and `test_settle.py` (executed). This run probes the
slice; it does not seal the tree.

Edges this round judged not worth a finding, with their grounds:

- The non-ASCII case relies on git's default `core.quotePath`. A person
  with `core.quotePath=false` in their global config would see it pass
  against the code without `-z`. CI and the default config both quote, and
  the case went red there. The rename case pins its own config, and this
  one could do the same in one line. Without that line, the case still
  catches a regression in CI, so it would cost a reader little to ship.
- `trail/phases/phase-1.md` still says the `--no-renames` mutant survived.
  That was true of the phase's code and cases at `4711da2e8`, so the record
  is not wrong. The fix pass's close already says so.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `ed12660ea`, still `unverified`; this round ran only the slice above. This round leaves nothing open, so the broad run is now due | the branch at `ed12660ea` | the orchestrator, at `seal gate`, then the sealer's spawn after it |
| Whether #1283 will fix `settle.py#released` and `rule_changes.py#order`; they came before this branch and lie outside its frame | #1283 | the orchestrator, who routed them |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_settle.py -q` in a `git clone --no-local` at `ed12660ea` | exit 0, 159 passed |
| `git log -z --no-renames --full-history --no-show-signature --diff-filter=D --name-only "--format=%x01%H %h %s" origin/main -- seal/threads`, read through Python | 5 commit fields, each followed by a NUL and a newline before its first path; every other piece a path under `seal/threads` |
| `settle.py` from `e59ec5995`, then the non-ASCII case alone | exit 1, failed at `assert f"\n    {old}  " in text` |
| `--no-renames` alone removed, then the nine removed-plan cases of `Test_main` | exit 1; only the rename case failed, at the same assertion |
| `--no-show-signature` alone removed, then the same nine cases | exit 1; only the signed-removal case failed, at the same assertion; none skipped |
| `bin/seal layout --pairs` | exit 0; no pair from `tests/skills/test_settle.py` |
| `bin/test` over the 23 modules `git grep -l` lists for the settle's paths | exit 0, 1716 passed |
| `uvx ruff check` and `uvx ruff format --check` on the two touched Python files | both exit 0 |

Each mutant was reverted before the next run. The clone and the logs under
the round's scratch directory were removed before this record was handed back.

# 1791940762-the-record-of-truth-is-tests-not-coordinates — review round 1

| Field | Value |
|---|---|
| Target SHA | e05213e0b5ba587a43d98d5626a7760227081d32 |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #950 |
| Broad gate | not yet |
| Fixes checked by | round-2 |
| Fix range | `5a3ffdb46ef4143063d169b63e798a91ccfc75a4..67275a502c78b802367a21f001790890b91fed16`, 8 commits |
| Contract changes | docstring → describe, round-1-report.md, round-1.md |
| New units | DEFINITIONS (depth 1); GATED (depth 1); test_a_target_the_resolver_finds_in_a_block_prints_its_sentence (depth 1); test_with_no_root_the_targets_resolve_where_the_command_runs (depth 1); TODO_FILE (depth 1); test_the_todo_file_sits_where_settle_looks (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 to 🟡 8: the `rules` root and its crash, the uncounted indented rule paragraphs, the layout's stale resolver statement and its F2 citation, the *evidence feedback* sentences, the follow-up row on the sweep, and the case asserting `evidence-todo.md`'s layout |
| Loses a record or crashes | yes — 🟡 2: `rules` exits 1 with a `StopIteration` traceback on a target defined under an `if`; nothing found loses a record |

- [x] Pass

## What this round was asked

Round 1 of #944 against origin/release/v0.22.0: spec compliance and correctness, and specifically anything still standing on the removed ledger, change records, `Pact notify` or #759's one-spelling rule; text appended rather than rewritten in place, or a second copy of a fact; a removal whose premise is false; a check bent around instead of fixed. Narrow checks only.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | `rules` defaults `--root` to the plugin's own tree, so a user's real test reads "does not exist"; the command has no README row | `.github/scripts/rules.py:139` | **fixed** `89b000a9` | fixed at 89b000a9; executed: from a scratch repository, `bin/rules docs/x.md` printed `tests/test_user.py does not exist` for a test the repository holds, exit 0; every case passes `--root` |
| 🟡 2 | `rules` crashes with `StopIteration` on a target defined under an `if`, which the resolver accepts | `.github/scripts/rules.py:73` | **fixed** `04da85ca` | fixed at 04da85ca; executed: a scratch tree with `def` under `if sys.platform` → traceback, exit 1; the docstring promises 0 or 2 |
| 🟡 3 | `rule_paragraphs` does not open a paragraph indented 1–3 spaces, against its docstring; 46 bold-led paragraphs in six rule files are uncounted | `.github/scripts/budget_check.py:219` | **fixed** `7b8edffb` | fixed at 7b8edffb; executed over `rule_files('.')`: 46 openers, 0 counted, among them `agents/warden.md:170`; the permissive direction for a gate |
| 🟡 4 | the layout's resolver statement says any `def` or `class` is accepted; the resolver now refuses a name defined twice | `docs/the-record-layout.md:243` | **fixed** `0bda17c7` | fixed at 0bda17c7; read: c04e759f rewrote `fold_check.py` and `budget_check.py` docstrings and not the rule's home |
| 🟡 5 | "evidence feedback" and "Leave evidence rows empty" still describe the implement skill's §2 | `skills/implement/orchestration.md:56` | **fixed** `e28d7a5d` | fixed at e28d7a5d; read: also `skills/implement/orchestration.md:18` and `agents/smith.md:27`; none listed in `overview.md` §*Not done* |
| 🟡 6 | a follow-up row asks the owner about the deleted survivor sweep | `seal/follow-up.md:74` | **fixed** `0c01f8ad` | fixed at 0c01f8ad; read: `spec.md` §*What is lost, honestly* answers its second option; `overview.md` lists `:67` and not `:74` |
| 🟡 7 | the layout's index row cites `(F2, built)`, from a section phase 1 deleted | `docs/the-record-layout.md:17` | **fixed** `d978ba3d` | fixed at d978ba3d; read: no `F2` remains in any rule file |
| 🟡 8 | a case asserts `evidence-todo.md`'s layout for the deleted fold's guard, and its message names that guard | `tests/test_the_set_a_work_item_always_has.py:308` | **fixed** `67275a50` | fixed at 67275a50; read: `:372-394`; the live reader is `settle.py#PROCESS_TODOS`, `tests-todo.md` alone |
| ❓ | W2 and S11: each moved kernel case and each re-pointed pin was seen red by one mutation | `tests/test_a_unit_is_bounded_where_a_parser_decides.py` | ❓ out of verified scope | read only: `phases/phase-4.md` and `phases/phase-8.md` claim `mutation-check` red for each, and this round re-ran none; round 2's warden answers it with `mutation-check` on that module |

## Paste-ready fixes

```python
# module docstring, the two usage lines
  rules <doc>              every heading of DOC, and under each the targets
                           of its `Enforced by:` lines, each with the first
                           sentence of its docstring, resolved in the
                           repository the current directory is in
  rules <doc> --root DIR   resolve the targets in DIR instead

# main()
    parser.add_argument(
        "--root", default=None, help="the repository to resolve in (default: cwd)"
    )
    args = parser.parse_args(argv)
    ...
    root = os.path.abspath(args.root or os.getcwd())
```
```python
def test_with_no_root_the_targets_resolve_where_the_command_runs(
    tmp_path, capsys, monkeypatch
):
    """`rules <doc>` from inside a repository resolves that repository's
    targets, not the tree the script ships in."""
    root = tree(tmp_path, "## A\n\n**Held.** Why.\nEnforced by: tests/test_x.py::test_held\n")
    monkeypatch.chdir(root)
    assert rules.main(["docs/a.md"]) == 0
    out = capsys.readouterr().out
    assert "tests/test_x.py::test_held — A held rule is guarded." in out, out
```
```python
def defined(node, name):
    """The `def` or `class` NAME in NODE's scope, looked for through the
    blocks that are not a definition, as `coordinates.py#named_unit` looks,
    or None.

    Reads: owned — a parsed tree its caller hands it; unknown passed"""
    for child in ast.iter_child_nodes(node):
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if child.name == name:
                return child
        else:
            found = defined(child, name)
            if found is not None:
                return found
    return None


def docstring(root, target):
    # ... unchanged down to the parse ...
    for part in name.split("::") if name else []:
        node = defined(node, part)
        if node is None:
            return None
    return ast.get_docstring(node)
```
```python
def test_a_target_defined_under_an_if_prints_its_sentence(tmp_path, capsys):
    """A unit the resolver finds inside an `if` is described, not a crash."""
    root = tree(tmp_path, "## A\n\n**R.** Why.\nEnforced by: tests/test_x.py::test_gated\n")
    (root / "tests" / "test_x.py").write_text(
        'import sys\nif sys.platform:\n    def test_gated():\n        """Gated. More."""\n',
        "utf-8",
    )
    code, out, _err = run(root, capsys)
    assert code == 0
    assert "tests/test_x.py::test_gated — Gated." in out, out
```
```python
RULE_PARAGRAPH = re.compile(rf"(?:{LIST_MARKER}|[ ]{{0,3}})\*{{2,3}}[^*\s]")
```
```python
        ("- Item.\n\n  **A rule.** Why.\n", ["**A rule.** Why."]),
```
```markdown
**`path::name` has one resolver.** An `Enforced by:` target names a unit as
pytest spells a node id, so a method is `::Class::method`, and `fold-check`
and the `enforced-unresolved` budget read it through
`skills/settle/scripts/fold_check.py#target_problem`, which looks the name up
through `coordinates.py#named_unit`. A name is looked up where it is
defined. A `def` or `class` its file defines once is accepted, and so is a
file alone. A name defined twice names no one unit and is refused.
Enforced by: tests/test_a_folded_statement_names_what_enforces_it.py::test_a_method_resolves_in_pytests_spelling, tests/test_a_folded_statement_names_what_enforces_it.py::test_the_target_is_resolved_by_named_unit, tests/test_a_folded_statement_names_what_enforces_it.py::test_a_name_defined_twice_is_no_target
```
```markdown
`skills/implement/SKILL.md` is the other half and holds the implementation
itself — the record language, the document layout, the spec-first procedure,
the test-first cadence, the SDD file set, the closing memo and the review
incorporation.
```
```markdown
The `implement` skill (preloaded) is your procedure — document layout, judgment
precedence (policy > SDD > code), the test-first cadence, overview, review
incorporation. This file only adds what the skill does not carry.
```
```markdown
| three `seal/follow-up.md` rows change | not in the frame / the row asking whether `CONTRIBUTING.md` gains a third arm for a drifted ledger claim and the row asking whether a marker-shape checker replaces the survivor sweep's reading of phase records are removed, and the ledger and `evidence-check` clauses leave the `hits()` and `Broad gate` rows | the build | the first two questions have no subject without the ledger and the sweep, and `spec.md` §*What is lost, honestly* answers the second: the shape is review's; the other two rows' questions stand without the ledger clauses |
```
```markdown
| The changelog | `seal/specs/<work-item-id>/changelog.md` while a work item is open; `changelog/<X.Y.Z>.md`, the release's own file, once its release gathers it | each release file is under target, and is the unit | the file name, by version, and `CHANGELOG.md`, which heads each release newest first with a link to its file |
```
```python
TODO_FILES = ("tests-todo.md",)


def _at_the_work_item(root):
    """Every todo file at the level `settle.py#process_plan` reads."""
    ...


def test_the_todo_file_sits_where_settle_looks():
    """A glob is a claim about layout, and nothing checked the layout.

    `skills/settle/scripts/settle.py` keeps a released item's process record
    while its `tests-todo.md` has an open row, and it reads that file at the
    work item's own level, `seal/specs/<id>/tests-todo.md`. A file one
    directory deeper, under `rounds/`, is one it never sees — silently,
    because a guard that finds nothing and a guard that looks in the wrong
    place say the same thing (issue #96).
    """
    stray = sorted(_below_the_work_item(ROOT))
    assert not stray, (
        "a todo file sits below the work item's own directory, where "
        "`settle --retire-process` cannot see it: "
        f"{[os.path.relpath(p, ROOT) for p in stray]}. It reads "
        "`seal/specs/<id>/tests-todo.md`, one level only"
    )
```

## Executed probes

| What was run | Result |
|---|---|
| `python3 .github/scripts/budget_check.py` on the clone at e05213e0 | exit 0 |
| `python3 .github/scripts/rules.py <f>` over every rule file `budget_check.py#RULE_FILES` names | every file exit 0 |
| `bin/rules docs/x.md` run from a scratch repository whose `tests/test_user.py` defines the target | prints `does not resolve: tests/test_user.py does not exist`, exit 0 (🟡 1) |
| `rules.py docs/x.md --root <scratch>` against a `def` under `if sys.platform != "win32":` | `StopIteration` traceback, exit 1 (🟡 2) |
| `budget_check.rule_paragraphs` over `rule_files('.')`, against a regex for 1–3-space `**` openers after a blank line | 46 openers, 0 counted (🟡 3) |
| `broad_gate.PARTITION` loaded and counted against `hygiene.yml`'s step names | 11 steps, 8 with no arm, 3 arms (`unverified`, `chain`, `mode`); every step name matches the workflow |
| the spec's S9 grep over `agents skills templates docs hooks .github CLAUDE.md CONTRIBUTING.md README*.md SECURITY.md` | two lines, `skills/verify/SKILL.md:137` and `round_record.py:2092`, both the mutation sense `overview.md` names, plus `arm_check.py`'s |
| `git grep -n 'Pact notify'` outside `seal/specs`, `changelog`, `.test_durations` | `hooks/config.py:859`, `templates/config.md:429-430`, three test modules: phase 8's list |
| `bin/test tests/test_a_budget_ratchets.py tests/test_the_rules_command_reads_each_rule_off_its_test.py tests/test_a_folded_statement_names_what_enforces_it.py tests/test_the_set_a_work_item_always_has.py -q` | 217 passed, exit 0 |
| the broad gate (full suite, lint, typecheck) | not yet — the sealer's, once, after the rounds settle; it was not run here, and no number above stands for it |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

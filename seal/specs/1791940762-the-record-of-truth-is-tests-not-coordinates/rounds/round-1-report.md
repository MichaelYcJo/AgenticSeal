# Round 1 report — 1791940762, the record of truth is tests, not coordinates (#944)

| Field | Value |
|---|---|
| Round | 1 |
| Target SHA | e05213e0b5ba587a43d98d5626a7760227081d32 |
| Base | `origin/release/v0.22.0` (f975ea66) |
| Reviewed by | warden, in a `git clone --no-local` of the worktree at the target SHA |

## What was asked, and how it was read

The owner's bar for this release: the repository stops growing by accretion.
A change rewrites the text it amends in place, and in the same commit removes
what stood on the old fact. A fact has one source. Existing is not a reason to
keep something. Beyond spec compliance, the round looked for four things:
anything still standing on the removed ledger, change records, `Pact notify`
or #759's rule that is not listed as left on purpose; text appended instead
of rewritten, or a second copy; a removal whose premise is false; and a check
bent around instead of fixed.

The implementer's account (`spec.md`, `plan.md`, `questions.md`,
`overview.md`, the eight phase records) was read in full and treated as a
claim. Where a finding contradicts it, the finding says what was claimed and
what the code does. Known and not reported: the `.test_durations` refresh and
e05213e0's unsharded Windows leg, `tests/test_release_hygiene.py`'s S7 guard,
and the ~40 test fixtures and comments that say *ledger*, which are #942's.

Stage 1, spec compliance, holds on the axes it was checked on. S8 (the gate's
`PARTITION` has 11 steps, 8 excluded and 3 mirrored arms, executed), S9 (the
spec's grep names only the two mutation-sense uses of *survivor* that
`overview.md` already lists, executed), the `Pact notify` grep against phase
8's list (executed), and `budget_check.py` exit 0 on the tree (executed). The
findings below are what stage 2 and the four questions found.

## How the findings relate

- **The replacement's two new readers have defects of their own.** `rules`
  resolves against the plugin's tree rather than the user's (🟡 1), and
  crashes on a target its own resolver accepts (🟡 2). `rule_paragraphs`
  does not count a rule paragraph indented one to three spaces, which its own
  docstring says it reads (🟡 3).
- **The slice document kept text that stood on facts this branch changed.**
  Its resolver statement still says any `def` is accepted after c04e759f made
  a name defined twice a refusal (🟡 4). Its index row still cites F2, from a
  section phase 1 deleted (🟡 7).
- **Three sentences and two records still stand on the ledger or the sweep,
  and none is in `overview.md` §*Not done*.** The implement skill's
  *evidence feedback* (🟡 5), a follow-up row whose subject is the deleted
  survivor sweep (🟡 6), and a test whose assertion and message name the
  deleted fold's guard (🟡 8).

## Findings

### 🟡 1 — `rules` resolves every target against the plugin's own tree, so in a user's repository each real test reads "does not exist"

`.github/scripts/rules.py:139` defaults `--root` to `ROOT`, the directory two
levels above the script. That is this repository in a clone, and the plugin
cache for a user. `tests/test_the_release_check_watches_what_ships.py` says
the plugin loader puts `bin/` on the Bash tool's PATH, so `rules` is a bare
command for every user. The document is found from the current directory
(`rules.py:146`), but the targets are resolved under the plugin root.

Executed. A scratch repository holding `docs/x.md` with
`Enforced by: tests/test_user.py::test_users_rule`, and that test defined,
ran `bin/rules docs/x.md` from inside it. The output was
`tests/test_user.py::test_users_rule — does not resolve: tests/test_user.py does not exist`,
at exit 0.

Why it matters: a user is told a test they have does not exist. Every case in
`tests/test_the_rules_command_reads_each_rule_off_its_test.py` passes
`--root`, so the default was never exercised. `fold-check`, the checker this
command sits beside, defaults to the current directory
(`skills/settle/scripts/fold_check.py:709`). The command is also named in
neither README's command table, so a user who finds `rules` on PATH has no
row saying what it reads.

### 🟡 2 — `rules` exits 1 with a `StopIteration` traceback on a target defined under an `if`

`.github/scripts/rules.py:73-79` walks to a `path::name` target through
`node.body` only. `coordinates.py#named_unit` walks into `if`, `try` and
`with` blocks (`coordinates.py:497-515`), so `budget_check.py#target_problem`
accepts such a target. Then `docstring` calls `next()` on an empty generator,
and `describe` (`rules.py:96`) catches only `OSError`, `ValueError` and
`SyntaxError`.

Executed. A scratch tree with `if sys.platform != "win32": def
test_posix_only(): ...` and a document bound to it. `rules.py docs/x.md
--root <scratch>` ended with `StopIteration` at exit 1. The module docstring
promises exit 0 or 2 only.

Why it matters: a read-only command crashes on input its own resolver calls
valid. The class is every target nested in a non-`def` block, including a
method inside a class body's `if`.

### 🟡 3 — A rule paragraph indented one to three spaces is not counted, so 46 bold-led rules sit outside `unenforced`

`.github/scripts/budget_check.py:219` is
`RULE_PARAGRAPH = (?:LIST_MARKER)?\*{2,3}[^*\s]`. The `[ ]{0,3}` lives inside
`LIST_MARKER`, so a paragraph opening `  **A rule.**` matches only when a
list marker follows the spaces. `rule_paragraphs`' docstring
(`budget_check.py:799-801`) says each form opens "up to three spaces in".
This is the shape of a list item's continuation paragraph, which the agent
definitions use for most of their rules.

Executed, over `budget_check.py#rule_files('.')`. 46 lines open a block with
one to three spaces and `**`, and none is in `rule_paragraphs`' output:
`skills/verify/SKILL.md` 15, `agents/smith.md` 8, `agents/warden.md` 8,
`skills/implement/orchestration.md` 8, `skills/config/SKILL.md` 6,
`CONTRIBUTING.md` 1. One of them is `agents/warden.md:170`, *A round told
the run is capped still reports what it finds*, a rule with no
`Enforced by:` line.

Why it matters: `unenforced` is a gate that blocks the more it counts. Here
it under-counts, which is the permissive direction. A new rule written as an
indented paragraph raises no row, while `CONTRIBUTING.md:57` tells a
contributor that a new bold-led rule does. The fix raises six files'
ceilings, which owes `Budget raised:` lines with this finding as the reason.

### 🟡 4 — The layout's resolver statement still says any `def` or `class` is accepted, after c04e759f made a name defined twice a refusal

`docs/the-record-layout.md:243-249`, §*The fold, and what tells it from a
deletion*, reads: "A name is looked up where it is defined, and any `def` or
`class` or a file alone is accepted." c04e759f changed
`fold_check.py#target_problem` to refuse a name its file defines twice.
`fold_check.py`'s module docstring and `budget_check.py`'s docstring were
rewritten for it, and this statement was not.

Read. Why it matters: this is the rule's home, and it now disagrees with the
code and with two docstrings. That is a second copy of a fact going stale,
which the tenet rules out. The statement's enforcers do not include
`tests/test_a_folded_statement_names_what_enforces_it.py::test_a_name_defined_twice_is_no_target`,
the case that holds the new half.

### 🟡 5 — Three sentences still describe the implement skill as "evidence feedback", and one tells a bootstrap to leave evidence rows empty

- `skills/implement/orchestration.md:56-58`: "Leave evidence rows empty. They
  fill through the feedback rule in `skills/implement/SKILL.md` §2". The
  bullet stood under the bootstrap's `seal/ledger.md` item, which phase 5
  removed. Nothing has evidence rows now, and §2 is *Implement test-first,
  and let each rule name its test*.
- `skills/implement/orchestration.md:18`: "the evidence feedback".
- `agents/smith.md:27`: "evidence feedback".

Read. The implement skill's own description says *the test-first cadence*
(`skills/implement/SKILL.md:5`). Why it matters: every orchestrator reads
orchestration.md, and every smith spawn preloads `agents/smith.md`. Each one
is told about a procedure the branch removed. None of the three is in
`phases/phase-7.md`'s grep table or in `overview.md` §*Not done*. Phase 7's
grep was for `ledger`, and none of these sentences contains the word.

### 🟡 6 — `seal/follow-up.md:74` asks the owner a question whose subject is the deleted survivor sweep

The row opens "**The survivor sweep no longer reads a work item's
`phases/phase-N.md`**" and asks whether a marker-shape checker is worth
building "or whether the shape stays a reviewer's to read". This branch
deleted the sweep. `spec.md` §*What is lost, honestly* gives the sweep's
sentence-level reading to each phase's rule census and to the warden, which
answers the row's second option.

Read. Why it matters: `seal/follow-up.md` is a durable record outside the
work-item paperwork, and its rows are read as open decisions for the owner.
`overview.md` §*Not done* lists `seal/follow-up.md:67` as left on purpose
and says nothing about `:74`. Phase 6's divergence row says two follow-up
rows changed, and this was not one of them.

### 🟡 7 — The layout's index row still cites `(F2, built)`, from the section phase 1 deleted

`docs/the-record-layout.md:17`, the *The changelog* row of §*Every kind of
record, at a glance*, ends "(F2, built)". F2 was an item of §*What is decided
and not built yet*, which phase 1 removed whole (`overview.md`, the second
divergence row). No `F2` remains anywhere in the rule files, so nothing
resolves the citation.

Read. Why it matters: this is the slice document taken to zero in phase 1,
and the removal left a citation standing on what it removed. That is the
"remove what stood on the old fact" half of the tenet.

### 🟡 8 — A case asserts the layout of `evidence-todo.md` for the deleted fold's guard, and its failure message names that guard

`tests/test_the_set_a_work_item_always_has.py:308` keeps
`TODO_FILES = ("evidence-todo.md", "tests-todo.md")`. At `:372-394`,
`test_the_two_todo_files_sit_where_the_release_guard_looks` says
`.github/scripts/fold_ledger.py` refuses a release on an open
`evidence-todo.md` row. Its failure message ends "The release guard reads
`seal/specs/*/evidence-todo.md`". `_at_the_work_item` says it is "the level
`fold_ledger.py`'s glob reads". The fold and the file kind are both gone.
The surviving reader of a todo file at that level is
`settle.py#PROCESS_TODOS`, which reads `tests-todo.md` alone.

Read. Why it matters: this is a check, not a fixture. It still asserts where
a retired file kind sits, and a person meeting its failure is sent to a
guard that does not exist. It is outside `overview.md` §*Not done*'s
"fixtures and comments" sentence, because it is neither.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | `rules` defaults `--root` to the plugin's own tree, so a user's real test reads "does not exist"; the command has no README row | `.github/scripts/rules.py:139` | open | executed: from a scratch repository, `bin/rules docs/x.md` printed `tests/test_user.py does not exist` for a test the repository holds, exit 0; every case passes `--root` |
| 🟡 2 | `rules` crashes with `StopIteration` on a target defined under an `if`, which the resolver accepts | `.github/scripts/rules.py:73` | open | executed: a scratch tree with `def` under `if sys.platform` → traceback, exit 1; the docstring promises 0 or 2 |
| 🟡 3 | `rule_paragraphs` does not open a paragraph indented 1–3 spaces, against its docstring; 46 bold-led paragraphs in six rule files are uncounted | `.github/scripts/budget_check.py:219` | open | executed over `rule_files('.')`: 46 openers, 0 counted, among them `agents/warden.md:170`; the permissive direction for a gate |
| 🟡 4 | the layout's resolver statement says any `def` or `class` is accepted; the resolver now refuses a name defined twice | `docs/the-record-layout.md:243` | open | read: c04e759f rewrote `fold_check.py` and `budget_check.py` docstrings and not the rule's home |
| 🟡 5 | "evidence feedback" and "Leave evidence rows empty" still describe the implement skill's §2 | `skills/implement/orchestration.md:56` | open | read: also `skills/implement/orchestration.md:18` and `agents/smith.md:27`; none listed in `overview.md` §*Not done* |
| 🟡 6 | a follow-up row asks the owner about the deleted survivor sweep | `seal/follow-up.md:74` | open | read: `spec.md` §*What is lost, honestly* answers its second option; `overview.md` lists `:67` and not `:74` |
| 🟡 7 | the layout's index row cites `(F2, built)`, from a section phase 1 deleted | `docs/the-record-layout.md:17` | open | read: no `F2` remains in any rule file |
| 🟡 8 | a case asserts `evidence-todo.md`'s layout for the deleted fold's guard, and its message names that guard | `tests/test_the_set_a_work_item_always_has.py:308` | open | read: `:372-394`; the live reader is `settle.py#PROCESS_TODOS`, `tests-todo.md` alone |
| ❓ | W2 and S11: each moved kernel case and each re-pointed pin was seen red by one mutation | `tests/test_a_unit_is_bounded_where_a_parser_decides.py` | ❓ out of verified scope | read only: `phases/phase-4.md` and `phases/phase-8.md` claim `mutation-check` red for each, and this round re-ran none; round 2's warden answers it with `mutation-check` on that module |

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

## Regression tests to plant

- `tests/test_the_rules_command_reads_each_rule_off_its_test.py`: a case that
  runs `rules.main([doc])` with no `--root`, with the current directory a
  `tmp_path` repository holding the target, and asserts no `does not resolve`
  (🟡 1). Seen red on the tree as it stands.
- `tests/test_the_rules_command_reads_each_rule_off_its_test.py`: a target
  defined under an `if` prints its first sentence at exit 0 (🟡 2). Seen red
  as the `StopIteration` above.
- `tests/test_a_budget_ratchets.py`, in
  `test_a_rule_paragraph_opens_a_block_with_a_bold_lead`'s table: an id
  `an indented paragraph`, `("- Item.\n\n  **A rule.** Why.\n", ["**A rule.** Why."])`
  (🟡 3). Red on the tree: `rule_paragraphs` returns nothing for it.

## Paste-ready fixes

### 🟡 1

`.github/scripts/rules.py`. Resolve against the current directory, as
`fold-check` does, and say so in the docstring. Then add a `rules` row to
both READMEs' command tables in one commit (S12).

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

### 🟡 2

`.github/scripts/rules.py`. Find the unit the way `named_unit` does: through
`if`, `try` and `with` blocks, but never into another `def`.

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

### 🟡 3

`.github/scripts/budget_check.py:219`. Let the three spaces stand before a
bare `**` as well as before a list marker. Then raise the six files' rows in
`seal/budgets.md` to what `budget_check.py` measures, with one
`Budget raised: unenforced:<file> <old> -> <new>: rule paragraphs indented
inside a list item were not counted (round 1 of #944, 🟡 3)` line each in
the pull request body.

```python
RULE_PARAGRAPH = re.compile(rf"(?:{LIST_MARKER}|[ ]{{0,3}})\*{{2,3}}[^*\s]")
```

```python
        ("- Item.\n\n  **A rule.** Why.\n", ["**A rule.** Why."]),
```

with `"an indented paragraph"` added to the `ids` list in the same position.

### 🟡 4

`docs/the-record-layout.md`, the `path::name` statement. Rewritten in place,
with the case that holds the new half added to its line.

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

### 🟡 5

Three edits, one commit. Lower `preload:smith` in `seal/budgets.md` in the
same commit if the measurement leaves its band.

`skills/implement/orchestration.md:16-19`:

```markdown
`skills/implement/SKILL.md` is the other half and holds the implementation
itself — the record language, the document layout, the spec-first procedure,
the test-first cadence, the SDD file set, the closing memo and the review
incorporation.
```

`skills/implement/orchestration.md:56-58`: delete the bullet that opens
"Leave evidence rows empty. They fill through the feedback rule in".

`agents/smith.md:26-28`:

```markdown
The `implement` skill (preloaded) is your procedure — document layout, judgment
precedence (policy > SDD > code), the test-first cadence, overview, review
incorporation. This file only adds what the skill does not carry.
```

### 🟡 6

`seal/follow-up.md`. Delete line 74, the row headed **The survivor sweep no
longer reads a work item's `phases/phase-N.md`**. Its subject left with the
sweep, and `spec.md` §*What is lost, honestly* gives the shape to review,
which is the row's second option. Then name it in `overview.md`'s
divergence row about `seal/follow-up.md`:

```markdown
| three `seal/follow-up.md` rows change | not in the frame / the row asking whether `CONTRIBUTING.md` gains a third arm for a drifted ledger claim and the row asking whether a marker-shape checker replaces the survivor sweep's reading of phase records are removed, and the ledger and `evidence-check` clauses leave the `hits()` and `Broad gate` rows | the build | the first two questions have no subject without the ledger and the sweep, and `spec.md` §*What is lost, honestly* answers the second: the shape is review's; the other two rows' questions stand without the ledger clauses |
```

### 🟡 7

`docs/the-record-layout.md:17`, the last cell of *The changelog* row.

```markdown
| The changelog | `seal/specs/<work-item-id>/changelog.md` while a work item is open; `changelog/<X.Y.Z>.md`, the release's own file, once its release gathers it | each release file is under target, and is the unit | the file name, by version, and `CHANGELOG.md`, which heads each release newest first with a link to its file |
```

### 🟡 8

`tests/test_the_set_a_work_item_always_has.py`. The kind that is left, and
the reader that reads it.

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

Needs a fix: yes — 🟡 1 to 🟡 8: the `rules` root and its crash, the uncounted indented rule paragraphs, the layout's stale resolver statement and its F2 citation, the *evidence feedback* sentences, the follow-up row on the sweep, and the case asserting `evidence-todo.md`'s layout
Loses a record or crashes: yes — 🟡 2: `rules` exits 1 with a `StopIteration` traceback on a target defined under an `if`; nothing found loses a record

The broad gate has not come due: this round leaves eight findings open, so
the sealer's spawn waits for the round that closes them.

## Proof block

```
📋 code-review applied
· spec:     seal/specs/1791940762-…/spec.md, plan.md, questions.md, overview.md, phases/phase-7.md, phases/phase-8.md
· opened:   .github/scripts/budget_check.py (diff), .github/scripts/rules.py, skills/settle/scripts/fold_check.py (diff and target_problem), skills/verify/scripts/coordinates.py (header, _parsed_kinds, named_unit), skills/verify/scripts/broad_gate.py (diff), skills/verify/scripts/seal_stamp.py (diff), skills/settle/scripts/settle.py (diff and retire_process tail), skills/verify/scripts/unverified_check.py (diff), skills/verify/scripts/pact_check.py (rename diff), hooks/config.py (diff), hooks/dispatch.py, hooks/routing.py, hooks/blocks.py, hooks/review-history-guard.py, hooks/root-migrate.py (diffs), skills/code-review/scripts/chain_check.py, round_record.py, skills/implement/scripts/seal.py (diffs), .github/scripts/rider_check.py, gather_changelog.py (diffs), .github/workflows/hygiene.yml, test.yml (diffs), seal/budgets.md, seal/config.md, seal/follow-up.md (diff and :74), docs/the-record-layout.md (1-345), docs/release-checklist.md (diff), docs/the-reader-registry.md, docs/the-review-and-parity-arms.md (diffs), templates/config.md (§Pact), CLAUDE.md, .github/PULL_REQUEST_TEMPLATE.md (diffs), CONTRIBUTING.md (§What a change to a gate must carry), agents/warden.md (diff), agents/smith.md:24-30, skills/implement/SKILL.md (header, headings, proof block, 250-262), skills/implement/orchestration.md:12-64, skills/code-review/SKILL.md:246-260, tests/test_the_set_a_work_item_always_has.py:300-410, tests/test_a_budget_ratchets.py:1625-1675, tests/test_the_rules_command_reads_each_rule_off_its_test.py:1-95, tests/test_settle_retires_the_process_record.py:340-385
· verified: executed — the probes table above; read — every finding's location; unverified — the full suite, lint and typecheck (the sealer's), and W2/S11's seen-red claims (round 2)
```

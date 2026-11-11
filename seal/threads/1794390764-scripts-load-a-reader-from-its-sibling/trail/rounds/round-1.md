# Review round 1: 1794390764-scripts-load-a-reader-from-its-sibling

```seal
target: 707107377 against origin/release/v0.37.4
```

The range is `3285f1a04..707107377`, the merge base with
`origin/release/v0.37.4` to HEAD. It was read in a `git clone --no-local`
of the branch under this round's scratch directory, and every probe ran
there. No earlier round exists, so nothing is carried from one. The facts
carried from the frame and the phases, and not established again here,
are named where they are used: G10's list of the guarded commands, phase
3's run of `seal layout --moved` at exit 1, and phase 3's `cmp` of S1's
stdout against the base.

## Findings

### 1. Where a caller goes on past an absent module, the person still reads "Nothing was read."

```seal
severity: must
location: `lib/sibling.py:80-82`, `skills/verify/scripts/broad_gate.py:1836-1839`, `.github/scripts/release_seal.py:317-325`
evidence: executed `python3 <scratchpad>/1794390764-scripts-load-a-reader-from-its-sibling/round-1/test_tmp_goes_on.py <clone>`; read `lib/sibling.py:80-82`, `skills/verify/scripts/broad_gate.py:1836-1839`, `.github/scripts/release_seal.py:317-325`, `tests/github/test_release_seal.py:695-709`
```

Why it matters: `lib/sibling.py#load` writes `MISSING` to stderr before it
raises `SystemExit(2)`, whoever catches the exit. The sentence ends
"Nothing was read." Two callers catch that exit and go on, by
`frame/design.md` *Scope* item 4. So in those runs the person reads that
nothing was read, while the gate goes on to its panel or the release seal
is drawn.

The probe pointed `sibling.ROOT` at an empty directory and called
`broad_gate.rounds_rows` on one round record. It returned
`[('rounds', '1')]`, the run going on. Its stderr held the whole sentence,
"cannot read .../skills/code-review/scripts/chain_check.py, which this
command loads. ... Nothing was read." and no other line.

The frame's clause for these sites is unmet at the label site. *Scope*
item 4 says a caller that catches the loader's `SystemExit` "its line
then says what goes unread and does not restate the absent file", and it
names `broad_gate.py`'s round label site among them. `broad_gate.py:1838`
catches the exit and returns the rows with no line of its own, so nothing
says the round counts went unread. `release_seal.py#chain_counts` prints
its own line, but after the loader's sentence, and its `({problem})` reads
`(2)`. `test_release_seal.py:709` pins the loader's sentence on that
stderr.

The lazy readers of `chain_check.py` (`:1177`, `:1420`, `:1648`, `:1815`)
are not part of this finding. Each of them ends the check at exit 2, so
"Nothing was read." holds there.

The fix keeps the sentence and exit 2 wherever the exit is not caught. A
caller that goes on loads inside `sibling.going_on()`, which keeps the
sentence back. The caller then names the absent file in its own line,
from the path the exit carries:

```python
# lib/sibling.py: import contextlib beside the other imports.
class Absent(SystemExit):
    """The exit `load` raises for an absent file: code 2, its path in
    `path`."""

    def __init__(self, path):
        super().__init__(2)
        self.path = path


_going_on = 0


@contextlib.contextmanager
def going_on():
    """A load inside it that meets an absent file raises `Absent` without
    writing `MISSING`: the caller goes on without the module and says in
    its own line what goes unread, naming `Absent.path`."""
    global _going_on
    _going_on += 1
    try:
        yield
    finally:
        _going_on -= 1


# in load(), in place of the two lines at :81-82:
    if not os.path.isfile(path):
        if not _going_on:
            sys.stderr.write(MISSING.format(path=path) + "\n")
        raise Absent(path)
```

```python
# skills/verify/scripts/broad_gate.py#rounds_rows, in place of :1836-1839
    try:
        with sibling.going_on():
            chain = sibling_module("skills/code-review/scripts/chain_check.py")
    except sibling.Absent as absent:  # a label never stops a run that passed
        sys.stderr.write(
            f"seal gate: the round rows are not counted: {absent.path} is absent\n"
        )
        return rows
    except Refused:  # a label never stops a run that passed
        return rows
```

```python
# .github/scripts/release_seal.py#chain_counts, in place of :317-325
    try:
        import sibling

        with sibling.going_on():
            routing, chain, reader = readers()
    except (Exception, SystemExit) as problem:
        said = getattr(problem, "path", None) or problem
        print(
            "the chain rows are not read: the round record's readers did not "
            f"load ({said})"
        )
        return None, None, capped, None
```

The snippets do not reach every statement of the old fact, and the fix
pass owes the rest. `frame/design.md` *Scope* item 4 ("does not restate
the absent file") and *Data & interfaces*, the `load` bullet "Where the
file is absent, it writes one sentence to stderr", change with it. So do
`lib/sibling.py`'s docstring and `#load`'s, and the comment at
`release_seal.py:319-320`. `tests/github/test_release_seal.py:709` asserts
the sentence and changes with it. `tests/lib/test_sibling.py` holds no
case for `going_on`, and `test_broad_gate.py#Test_rounds_rows` holds none
for the new line.

```seal
verdict: fixed 82b1693a0
answer: The finding holds. `lib/sibling.py` gains `Absent`, a `SystemExit` with code 2 carrying `path`, and `going_on()`, inside which `load` raises `Absent` and writes nothing; outside it the sentence and exit 2 stand. `broad_gate.py#rounds_rows` and `release_seal.py#chain_counts` load inside the block and name the absent file in a line of their own; the other catches of `SystemExit` outside `tests/` end the run at exit 2 or catch no load. Mutants of the block's test, its decrement, and its use at each caller went red. The design sentences this changes (*Scope* item 4, *Data & interfaces*, S5) go to the framer.
```

### 2. The changelog says every script copied alone says one sentence, and most end in a traceback

```seal
severity: should
location: `seal/threads/1794390764-scripts-load-a-reader-from-its-sibling/changelog.md:3`
evidence: executed `python3 unverified_check.py`, `python3 tag_release.py` and `python3 settle.py`, each copied alone into `<scratchpad>/1794390764-scripts-load-a-reader-from-its-sibling/round-1/alone/`; read `frame/design.md` *Scope* item 2, `trail/phases/phase-2.md` *The scenarios this phase owes* S6
```

Why it matters: the item's bold sentence says "A script of the plugin
copied out and run on its own says one sentence about what it lacks". The
item then says "Each script now reaches every other module of the plugin
through `lib/sibling.py`", and that where a file it loads is absent "it
prints ... and exits 2". This is the text a user reads in the release
note.

Copied alone, `unverified_check.py` and `tag_release.py` each exited 1 in
`ModuleNotFoundError: No module named 'sibling'`. `settle.py` exited 2 in
the sentence. *Scope* item 2 guards the eight commands of G10 and gives
`rules.py` and `release_report.py` their own guard. It leaves every other
script unguarded on purpose (*Alternatives considered* A10). Phase 2's S6
counts twelve scripts under `.github/scripts/` and `evals/scripts/` that
end in that traceback, and phase 1's S6 adds the unguarded scripts under
`skills/`. `hooks/core-start.py` reaches `lib/core.py` by a plain import,
since *Out of scope* item 2 keeps its base form. So the item states for
every script what holds for ten commands.

```markdown
- **A command of the plugin copied out and run on its own says one sentence about what it lacks (#1482).** Each script under `skills/`, `.github/scripts/` and `evals/scripts/` now reaches the other modules of the plugin through `lib/sibling.py`. Where a file it loads is absent, it prints `cannot read <path>, which this command loads. It ships in the plugin beside this script; a copy of one script taken on its own is not a plugin. Nothing was read.` and exits 2. `<path>` is the absent file's absolute path. A copy of `seal.py`, `settle.py`, `fold_check.py`, `pact_check.py`, `payload_meter.py`, `chain_check.py`, `pr_body.py` or `broad_gate.py` taken alone prints that sentence about `lib/sibling.py` itself, and so do `rules.py` and `release_report.py` when their arguments reach a load. A copy of any other script taken alone ends in a traceback, as it did before. Before, the scripts that reported an absent file each did so in a sentence of their own, naming what the file was for. `chain_check.py`, `pr_body.py` and `broad_gate.py` print the new sentence where they printed a line of their own. In a whole plugin, no command's output or exit code changes.
```

```seal
verdict: fixed 703882aae
answer: The finding holds. The first changelog item names the commands that say the sentence when copied alone, and says a copy of any other script ends as it did before, most of them in a traceback, since `release_seal.py` exits 0 whatever fails. It also says that `seal gate` and the release seal, going on without a module, name the absent file in their own line.
```

### 3. The move wrote `INVISIBLE`'s seven characters into `lib/lines.py` as themselves, where the base spelt them by code point

```seal
severity: should
location: `lib/lines.py:70`
evidence: executed `od -c` of `lib/lines.py:70`, `uvx ruff check --select PLE2515,RUF001 lib/lines.py` (1 error), and `python3 <scratchpad>/1794390764-scripts-load-a-reader-from-its-sibling/round-1/test_tmp_units.py <clone>`; read `git show 3285f1a04:skills/verify/scripts/unverified_check.py` line 148, `tests/lib/test_gaps.py:39-42`
```

Why it matters: at the base the constant read
`"\ufe0f\ufe0e\u200b\u200c\u200d\u2060\ufeff"`. At HEAD the line holds the
seven characters themselves: two variation selectors, three zero-width
characters, the word joiner and a byte-order mark. On screen the string
reads as empty. The move commit `27d2476c1` made the change, and it is
the one source difference the unit probe found in a moved unit outside
docstrings and comments. The values are equal, so no behaviour changed.
The next person who edits the line cannot see what it holds, and an
editor that drops a byte-order mark or a zero-width character changes
the reader with no visible diff. The tree spells such characters by code
point elsewhere for this reason (`tests/lib/test_gaps.py:39`: "Spelt by
code point, so no emoji and no invisible character stands in"). Ruff's
`PLE2515`, which this repository does not select, refuses the line.

The likely cause is the tool that wrote the file. This round's `Write`
call turned the same escapes in this record into the characters, and a
script had to restore them. So the fix pass checks the line after its
edit. `grep -c 'ufe0f' lib/lines.py` should print 1, and the line below
should print `False`. The file holds other non-ASCII characters in its
comments, so the check names the seven.

```sh
python3 -c "t = open('lib/lines.py', encoding='utf-8').read(); print(any(chr(c) in t for c in (0xFE0F, 0xFE0E, 0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF)))"
```

```python
INVISIBLE = "\ufe0f\ufe0e\u200b\u200c\u200d\u2060\ufeff"
```

```seal
verdict: fixed e2d4013f0
answer: The finding holds. A script wrote `INVISIBLE`'s seven code points as `\uXXXX` escapes again, and the record's check prints `False`. A scan of every `.py` file in the range for invisible characters finds no other this work introduced.
```

### 4. No case holds the exit code the diff changed for a lone copy run with `--help`

```seal
severity: should
location: `tests/skills/test_settle.py:3695-3721`, `tests/skills/test_fold_check.py:367-393`, `tests/skills/test_pact_check.py:115-137`, `tests/skills/test_payload_meter.py:1418-1445`
evidence: executed `python3 <copy> --help` for `settle.py`, `fold_check.py`, `pact_check.py` and `payload_meter.py`, each copied alone (exit 2, one line on stderr); executed `git grep -n -- '"--help"'` over the four test modules; read the four cases at their coordinates
```

Why it matters: `frame/design.md` *Data & interfaces* and `changelog.md`
state one changed exit code. A lone copy of these four commands run with
`--help` exits 2 in the sentence, where the base printed its help at exit
0. S4 states the scenario "with no argument or with any, `--help` among
them", verified by a case per command.

Each copied-alone case runs its copy with `--root <repo>` alone. A run
with `--root` reaches a load whether the guard stands at import or inside
the first function that loads (A13). So a later edit that moves the guard
back into a function turns no case red and silently undoes the stated
exit code. The `--help` hits in these modules run the whole script.
`test_settle.py:2156` and `:3664` run settle in a whole plugin, and
`test_fold_check.py:161` and `test_payload_meter.py:1646` do the same for
theirs. This is the *Regression test* row: a behaviour the diff changed
that no case holds.

```python
    @pytest.mark.parametrize(
        "args", [["--root", "{root}"], ["--help"]], ids=["a-run", "help"]
    )
    def test_a_script_copied_alone_exits_2_and_names_what_it_misses(
        self, tmp_path, args
    ):
        """#590, and S4 of #1482. A copy of this script taken without its
        siblings exits 2, with the loader's one sentence naming the absent
        `lib/sibling.py` by its path: 2 means the input or the tree was
        unusable and nothing was read, and a sibling that is not beside the
        command is that kind. The sentence names no purpose, and `--help`
        reaches it too, since the guard stands at import (#1482, A13)."""
        script = TARGET
        # ... the rest as it stands, without the `args = [...]` line
```

This is `test_settle.py`'s case. `test_fold_check.py` and
`test_payload_meter.py` take the same parametrize, and their own `args`
line goes. `test_pact_check.py`'s case passes `["--root", str(repo)]`
inline, so it takes the parametrize and builds its argv from `args` as
the other three do. Each new row is shown red with the guard moved into
the function that first loads (contract rule 15).

```seal
verdict: fixed 4b2cabc58
answer: The finding holds. The four copied-alone cases run the copy with `--help` as well, as a second parametrize row; a mutant that lets `--help` through the guard, as moving it into the getter would, turned only the `[help]` row red in each file.
```

### 5. `pr.md` gives A14 a reason for its rejection that the plan does not give

```seal
severity: should
location: `seal/threads/1794390764-scripts-load-a-reader-from-its-sibling/pr.md:2`
evidence: read `seal/threads/1794390764-scripts-load-a-reader-from-its-sibling/pr.md:2`, `seal/threads/1794390764-scripts-load-a-reader-from-its-sibling/frame/plan.md:91-92`
```

Why it matters: the quote of A14 stands word for word at `plan.md:91`.
The words after it say "rejected for reading no path under `tests/` as a
load". Read as "because", that is false. The plan rejects A14 because it
reads too little: following a table and a helper's argument "is a data
flow the walk would have to guess", and the arm dropped
`skills/settle/scripts/fold_check.py` with the eight files. Read as "in
favour of", it names only the half of the chosen arm that A15 is about.
The pull request's reader cannot tell which reading was meant, and
neither reading gives A14's actual fault.

```markdown
- "A14. `loaded_by` reads a tracked path only where it is handed to `sibling.load`, in the call or through a module-level name" (`frame/plan.md` *Alternatives considered*, rejected: it drops `skills/settle/scripts/fold_check.py` with the eight files, so the walk reads every tracked-path string and leaves out only those under `tests/`)
```

```seal
verdict: fixed af7b9370a
answer: The finding holds. `pr.md` now gives A14 the reason the plan rejects it for: it drops `skills/settle/scripts/fold_check.py` with the eight files.
```

## Confirmations

What matched: `lib/sibling.py#load` does what `frame/design.md` *Data &
interfaces* states (read `lib/sibling.py:60-95`). It returns the module
`sys.modules` holds for the same file, compared by spelling and then by
`realpath`. It writes `MISSING` and raises `SystemExit(2)` for an absent
file, and `ImportError` naming both files for a stem another file holds.
It takes a module that raises back out of `sys.modules`.
`tests/lib/test_sibling.py` holds each of these and passed (executed).
No stem of a tracked module outside `tests/` is a standard library name
(executed: `sys.stdlib_module_names` against `git ls-files`). So `lib/`
standing first on `sys.path` shadows nothing in a script's process.

What matched: S1 holds at HEAD (executed: `test_tmp_count.py`). One
`seal settle` with no argument executes twelve files once each, three
of them `lib/gaps.py`, `lib/items.py` and `lib/lines.py`, and does not
execute `unverified_check.py`. The byte-identity of stdout with the base
is carried from phase 3's `cmp` and was not re-run.

What matched: S2 and S3 (executed). `git grep -n unverified_check --
'*.py'` outside the script and its test file prints the `seal.py#TOOLS`
row, sentences on units the script keeps, the load in
`test_a_foreign_seal_dir_keeps_the_records_shared.py`, and test history
or imports of `test_unverified_check`; no script loads it.
`spec_from_file_location` outside `tests/` stands at `lib/sibling.py:86`
alone. `def _?load(` is `lib/sibling.py:60` and `session_cost.py:927`
alone.

What matched: each unit moved out of `unverified_check.py` stands at its
new home with the same code (executed: `test_tmp_units.py` and
`test_tmp_unitdiff.py`, source and AST against `3285f1a04`). The
differences are the docstrings and comments that cite the unit's new
place, `tree_at`'s two calls through `GITCMD`, and `INVISIBLE` (finding
3). `unverified_check.py` reads every name it still defines (executed: an
AST walk of the module). That is *Scope* item 9's "keeps no name it does
not use itself".

What matched: S8, weighed as A17 leaves it to review (executed:
`test_tmp_cases.py` over the five files the move took cases from at
`a5b69cd01`, against those files and the three new ones at HEAD, with
every module-binding name read as one name). 446 cases are identical. One
differs in its docstring alone (`test_settle.py`,
`Test_main::test_accepts_a_near_heading_inside_a_comment_without_a_word`).
Two stand under the renamed class `Test_rule_changes_reader`. Six differ
in one line each, and each line is a call the move forced:

- the three `test_refuses_a_comment_line_at_its_line` cases read
  `chain.FIELDS.COMMENT_LINE`;
- `Test_rule_changes_read::test_refuses_to_run_where_its_reader_will_not_load`
  patches `chain.rule_changes_reader`;
- `Test_pins_and_copies_in::test_names_a_test_the_parser_gives_up_on_as_not_read`
  calls `chain.rule_changes_reader()`;
- `Test_module::test_an_absent_reader_is_the_loaders_sentence_alone`
  expects `lib/lines.py`.

That is phase 3's nine. None weakens an assertion. The one case gone is
the one *Removes* names. Every other test name the branch removes from
`tests/` is a case *Removes* names, or one phase 1 renamed (executed: a
count of case names at `3285f1a04` against HEAD). `CONTRIBUTING.md` *The
test layout* asks the move check, or a mutation table where it exits 1,
of "a rebuilt module". This work rebuilds no test module; it moves
classes with their units under *Scope* item 10, which the comparison
holds. So the moved cases owe no mutation table, and the missing `--moved`
exemption costs nothing here.

What matched: A13's changed exit code is real and stated (executed: the
four commands copied alone and run with `--help` each exit 2 with one
line on stderr). It is stated in `frame/design.md` *Data & interfaces*,
`frame/plan.md` *Operational impact* and `changelog.md`'s second item.
Its missing case is finding 4.

What matched, with a claim corrected: phase 3 *Decisions on names*
claims that a new getter that loaded another module "would raise
`AttributeError` in every case that parses". That holds for
`rule_changes.py#grammar` and `payload_meter.py#_line_reader`. It does
not hold for `rule_changes.py#blocks`, `#fields` or `coordinates.py#fence_rule`.
`lib/lines.py` imports `gfm_lines`, `fence_opener` and `fence_closes`
from `lib/blocks.py`, and `lib/gaps.py` imports `COMMENT_LINE` from
`lib/fields.py` (executed: `hasattr` on each). A getter swapped to the
neighbour hands back the same function objects. Those mutants are
equivalent, so no case is owed and no finding follows.

What matched: the guards of *Scope* item 2 stand where it says, at import
in the eight commands and inside `rules.py#sibling` and
`release_report.py#module` (read). Each spells the loader's sentence
about `lib/sibling.py`. The copied-alone cases of `rules.py` and
`release_report.py` pass (executed). `settle.py` copied alone exits 2 in
the sentence (executed).

What matched: `chain_check.py#main` now asks `lib/optin.py#repo_root`,
which answers `""` for a path that is not a directory. The base's
`repo_root` took the directory of a file. The usage line
(`chain_check.py:124`) names `--root DIR`, so no documented input changes.
Phase 3 records the reason.

What matched: `pr.md`'s four quotes stand word for word at `plan.md`
A13, A14 and A17 and at the third row of *Judgments of the run* (read).
`Commit and pull request language` is English, so no `pr.<lang>.md` is
owed. The merge `f55d551de` keeps #1488's comment over `"lib/lines.py"`
at `tests/behaviour/test_release_hygiene.py:1314-1317`, and
`chain_check.py:167` holds that path (read).

What matched: the five `from` lines of *Rule changes* still stand in
`docs/` at HEAD. No other sentence under `docs/`, `skills/**/*.md`,
`agents/`, `templates/`, `CONTRIBUTING.md` or `README.md` cites a moved
unit away from its new home (executed: `git grep -w` on each moved
name). The chain check run over the branch worktree printed no notice at
a line of `frame/design.md` (executed).

What matched: the suite is labelled honestly. `gaps.md` names the full
suite, lint and typecheck as not verified for each phase, with the
orchestrator answering by the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD; this round ran four modules' worth of narrow runs | the whole tree | the orchestrator, by the broad gate |
| `frame/questions.md` Q1: whether a test file meets one shared `lib/` module instance changed by another file in one `pytest` process | `frame/questions.md` Q1, `gaps.md` | the orchestrator, by the broad gate |
| `lib/sibling.py#_same` on Windows, where case and separator may differ | `lib/sibling.py:46-57` | CI's `windows-latest` job |
| The five workflows that run the scripts under `.github/scripts/` | `.github/workflows/` | CI, on the release pull request, the merge to `main` and the next tag |
| S1's stdout byte for byte against the base's; carried from phase 3, not re-run | `trail/phases/phase-3.md` *The scenarios this phase owes* | phase 3's executed `cmp`, read by the sealer |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_goes_on.py <clone>`, `broad_gate.rounds_rows` with `sibling.ROOT` at an empty directory | rows `[('rounds', '1')]`; stderr the loader's sentence about `chain_check.py`, ending "Nothing was read." |
| `python3 test_tmp_units.py <clone>` and `test_tmp_unitdiff.py`, each moved unit's source and AST against `3285f1a04` | code identical but `INVISIBLE`'s spelling and `tree_at`'s two `GITCMD.` calls; the other differences are docstrings and comments |
| `python3 test_tmp_cases.py <clone> a5b69cd01`, S8's comparison with module names read as one | same 446, differ 6, docstring only 1, renamed class 2, gone 1 |
| `python3 test_tmp_count.py <clone>`, `settle.py` as `__main__` with `exec_module` counted | exit 0; twelve files once each, no `unverified_check.py` |
| `python3 <copy>` for `unverified_check.py`, `tag_release.py` and `settle.py` copied alone | exit 1 `No module named 'sibling'`, exit 1 the same, exit 2 the sentence |
| `python3 <copy> --help` for `settle.py`, `fold_check.py`, `pact_check.py` and `payload_meter.py` copied alone | exit 2 each, one stderr line |
| `bin/test tests/lib/test_gaps.py -q -p no:xdist` | 78 passed |
| `bin/test tests/lib/test_sibling.py tests/lib/test_lines.py tests/lib/test_items.py tests/behaviour/test_every_entry_point_runs_at_the_floor.py tests/github/test_rules.py tests/github/test_release_report.py tests/github/test_release_seal.py -q` | 301 passed |
| `uvx ruff check --select PLE2515,RUF001 lib/lines.py` | 1 error, at `INVISIBLE` |
| the plugin's and the tree's `chain_check.py --baseline origin/release/v0.37.4 --root <worktree> --worktree`, before this record | exit 0, the same output from both; notices only that no round, gate or guarantee record stands yet |

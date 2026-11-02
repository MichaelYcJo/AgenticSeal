# Review round 2: 1793577579-the-pull-request-names-each-pin-a-rule-change-breaks

```seal
target: c783f18f4, fixes 5f78f553d..c783f18f4
```

This verifying round read the diff `5f78f553d..c783f18f4` in the main clone at `c783f18f4`. That diff holds round 1's record (`b98163430`), the orchestrator's plan fold (`4105fd13c`), the fix commit (`28e82bf4d`), the fix pass's close blocks (`6410302ba`) and the orchestrator's design fold (`c783f18f4`). Probes ran in a scratch clone made with `git clone --no-local`, removed before hand-back. Carried from round 1 as coordinates and not re-established: the load chain against `ruff.toml` `[per-file-target-version]` (the fix adds no load), the S7 replay counts in `trail/phases/phase-1.md`, and where the pin reading lives (`chain_check.py#_read_tree`, `#_section_text`, `#pins_and_copies_in`). Every claim of the fix pass's close blocks was read as a claim and checked against the tree below. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` holds no `Record language` row, so the record is English. No finding below is taken from a `chain-check` notice: the check printed none for this design.

## Findings

### 1. A design that rewrites a passage with a `change` and adds the passage to another document gets no copy notice, though the first document still holds most of it after the settle

```seal
severity: should
location: `skills/code-review/scripts/chain_check.py:1256-1270`, `skills/settle/scripts/rule_changes.py:361-389`, `skills/code-review/scripts/chain_check.py:97`, `skills/code-review/scripts/chain_check.py:1244-1246`, `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/changelog.md:3`, `tests/skills/test_rule_changes.py:660-676`, `tests/skills/test_chain_check.py:2137-2160`
evidence: executed `.venv/bin/python -m pytest -q -p no:cacheprovider -p no:xdist tests/skills/test_tmp_probe.py`
regression: round-1#1
```

The unit is the `gone` collection in `chain_check.py#pins_and_copies_in` and the subtraction in `rule_changes.py#copies`, both added by `28e82bf4d`. The frame (plan row 1, which delivers *Scope* item 3's `copies`; `frame/design.md:101-102`, the `add`'s `to` as folded at `c783f18f4`, and `agents/proofer.md:64`) makes a copy a finding where another file keeps the passage after the settle, while the fix takes each `from` out of its document and puts nothing in its place, so a `change` is read as a `remove`; the defect came from round 1's own paste-ready fix, which collected `op.old` the same way, and the fix pass kept that collection.

Why it matters: the settle replaces a `change`'s `from` with its `to`. It does not delete it. A design that shortens a paragraph in `docs/a.md` to a pointer and adds the full paragraph to `docs/b.md` is a common way to move a rule's home. Where the shortened `to` keeps a run of 15 words of the paragraph, `docs/a.md` still holds a copy after the settle. The probe planted exactly that. `docs/policy.md` *A section* holds `Then w0 ... w14 and on.`. A `change` rewrites it to `Then w0 ... w14 and see the other file.`, and an `add` of `docs/other.md` has the original passage as its `to`. At `c783f18f4` the check prints nothing for the design. With `5f78f553d`'s two scripts in place it prints one copy notice at the `add`'s `to`, naming `docs/policy.md` and 4 shared runs of 15 words. After the settle three of those runs still stand in `docs/policy.md`, through the `change`'s `to`. So the fix turned a true notice into silence. The paste test then meets the copy first at the settle's broad run, after the pull request that could reword it has merged, which is the late meeting #1216 exists to end.

The same narrowing stands in the sentences that describe the subtraction. The module docstring (`chain_check.py:97`, "as the design's own removals leave it"), the `pins_and_copies_in` docstring (`:1244-1246`), the `copies` docstring, and the changelog fragment ("after the text the same design takes out of that document is taken out") all describe a removal. Each is rewritten to say the document is read as the design's operations leave it.

The fix carries each `change`'s `to` with its `from`, and puts the `to` where the `from` stood. A `remove` carries None. The replacement is a function, so a backslash in a `to` is not read as a group reference.

```python
# skills/code-review/scripts/chain_check.py#pins_and_copies_in, in the first loop
        taking.append((op, taken, at))
        if taken:
            # What the settle leaves in OP's file: a `change` puts its `to`
            # where its `from` stood, and a `remove` puts nothing there.
            gone.setdefault(op.file, []).append((taken, op.new))


# skills/settle/scripts/rule_changes.py#copies
def copies(op, texts, gone=None):
    """... GONE, `{path: [(text, put)]}`, is what the same design's
    operations do to each document: each TEXT is found once by `pattern`
    across any wrapping and replaced by PUT, the `to` of a `change`, or by
    nothing for a `remove`, before the runs are counted. So a passage the
    design moves leaves no copy where it took it from, and a passage a
    `change` keeps in its `to` is still a copy there. ..."""
    ...
        text = texts[path]
        for taken, put in (gone or {}).get(path, ()):
            if taken and taken.split():
                text = pattern(taken).sub(
                    lambda _m, put=put: f"\n{put or ''}\n", text, count=1
                )
        shared = p.windows(p.words(text)).intersection(order)
```

```python
# tests/skills/test_rule_changes.py, Test_copies: the two cases at 660-676
# pass GONE as pairs, `{"docs/a.md": [(passage, None)]}`, and one case is added.
    def test_accepts_a_run_a_change_keeps_in_its_to(self):
        """A `change` that rewrites the passage in `docs/a.md` and keeps 15 of
        its words leaves a copy there after the settle."""
        passage = f"Then {run_of(WINDOW)} and on."
        kept = f"Then {run_of(WINDOW)} and see the other file."
        texts = {"docs/a.md": f"## S\n\n{passage}\n"}
        o = one_op("add", new=passage, file="docs/b.md")
        found = rules.copies(o, texts, {"docs/a.md": [(passage, kept)]})
        assert [path for path, _count, _run in found] == ["docs/a.md"]


# tests/skills/test_chain_check.py, Test_pins_and_copies_in, beside
# test_accepts_a_passage_the_design_moves_naming_no_copy
    def test_names_a_copy_a_change_keeps_in_its_to(self, branch, ready, capsys):
        """A `change` that shortens a passage of `docs/policy.md` and keeps a
        run of 15 of its words, beside an `add` of the whole passage to
        `docs/other.md`: `docs/policy.md` keeps a copy after the settle."""
        root, _code = branch
        passage = f"Then {words_of(15)} and on."
        kept = f"Then {words_of(15)} and see the other file."
        write(
            root,
            "docs/policy.md",
            f"# Policy\n\n## A section\n\n{passage}\n\n## Another\n\nOther words.\n",
        )
        planted_spec(
            root,
            spec_with(
                "- change\n  file: docs/policy.md\n  section: A section\n"
                f"  from: {passage}\n  to: {kept}\n"
                f"- add\n  file: docs/other.md\n  to: {passage}\n"
            ),
        )
        code, out = check(root, capsys)
        assert code == 0, out
        assert any(
            "repeats a passage of `docs/policy.md`" in ln for ln in spec_lines(out)
        ), out
```

The chain-check case is the probe as it ran, and it is red at `c783f18f4`. The count of runs is left out of its assert because it depends on `passages.py#words`; the unit case pins the path. The fold of *Scope* item 3 that finding 3 asks for states the replacement too.

### 2. A tracked file whose name is not UTF-8 is still skipped unnamed, so the class the close lists as whole has an instance it left silent

```seal
severity: should
location: `skills/code-review/scripts/chain_check.py:1186-1196`, `skills/code-review/scripts/chain_check.py:1206-1209`, `skills/code-review/scripts/chain_check.py:317-326`
evidence: read `skills/code-review/scripts/chain_check.py:317-326`, `skills/code-review/scripts/chain_check.py:1157-1213`
reopens: round-1#2
```

Why the close does not hold: it lists the class by taking the reading apart into each source it opens, and calls a listed file the working tree deleted "the one silent case left". The listing is a source too, and its decoding is a step the list leaves out. `_tracked` reads `git ls-files -z` through `git()`, which decodes stdout with `errors="replace"` (`chain_check.py:322-323`). With `-z`, git prints each path's bytes verbatim, so a byte that is not UTF-8 reaches `_read_tree` as U+FFFD. The file of that mangled name does not exist, `open` raises `FileNotFoundError`, and both loops (`:1194`, `:1208`) skip it as deleted. The file stands in the working tree, the settle's broad run reads it, and the check names neither a pin in it nor that it went unread. This is the defect round 1 named, a source the reading could not read skipped with no notice, in one more instance.

It was read, not probed. macOS file systems refuse a name that is not UTF-8, so it cannot be planted on this machine; it arises on Linux. Every instance the close does list holds: the narrow run passed each new case at `c783f18f4`, and each was red with `5f78f553d`'s two scripts (executed, `## Probes`). That run also answers round 1's `## Not judged` row on `MemoryError` and `RecursionError`.

The fix names the mangled path, since U+FFFD stands in a listed path only where git's bytes did not decode. Where a path does hold U+FFFD and the file exists, `open` succeeds and this branch is not reached.

```python
# skills/code-review/scripts/chain_check.py
# A tracked path whose bytes are not UTF-8, after `not read: `: `git()` reads
# git's output with `errors="replace"`, so the name no longer opens.
NAME_UNREAD = "`{path}` has a name that is not UTF-8, so no {what} in it is named"


def _not_found(path, unread, what):
    """For a listed PATH that does not open: a file the working tree deleted
    is skipped, and one whose name git printed in bytes that are not UTF-8,
    which reads here with U+FFFD in it, is named on UNREAD as not read."""
    if "�" in path:
        why = NAME_UNREAD.format(path=path, what=what)
        unread.append((path, 0, RULE_CHANGES_UNREAD.format(why=why)))

# _read_tree, the tests loop and the documents loop:
        except FileNotFoundError:
            _not_found(path, unread, "pin")  # "copy" in the documents loop
            continue
```

`_read_tree`'s docstring then says that a deleted file is skipped and a file whose name did not decode is named. A case in `Test_pins_and_copies_in` monkeypatches `chain.git` to list `tests/test_�.py` and expects the notice. That runs on every platform. Where the fix pass judges the case outside the flow this tool serves, the cheaper answer is one limit sentence in that docstring naming the case, and no guard.

### 3. The design still states `copies(op, texts)` as comparing each document as the tree holds it, which the fix changed

```seal
severity: should
location: `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/design.md:45`, `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/design.md:78`
evidence: executed `grep -n "copies(op, texts)" seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/*.md`
```

Why it matters: *Scope* item 3 (`frame/design.md:45`) says `copies(op, texts)` returns each corpus path other than `file` that shares a run with the `to`. *Data & interfaces* (`:78`) names the same signature. Since `28e82bf4d` the function takes a third argument, and a path whose shared runs stand only in what the design takes out is not returned. The sealer reads the design against the tree, and a reader of item 3 expects the moved passage that `test_accepts_a_passage_the_design_moves_naming_no_copy` asserts is not named. The fix pass named four sentences to the orchestrator as standing on the old rule (`frame/design.md:48`, `:101`, `:102`, `:120`), and the fold at `c783f18f4` took those four. A search on the function's own name over the frame finds these two, which neither list holds. Contract rule 19 asks for the sentences found at least that way.

A fix pass does not edit `frame/design.md`, so this is the orchestrator's fold. It is written for the code as finding 1's fix leaves it.

```markdown
`copies(op, texts, gone)` returns, for an `add` or `change` whose `file` `in_corpus` admits, each corpus path other than `file` whose text, as the design's operations leave it (each `from` replaced by its `change`'s `to`, each text a `remove` takes out removed), shares at least one run of `windows(words(...))` with the `to`'s, with the count and one run.
```

and at `:78`, `copies(op, texts, gone)` in place of `copies(op, texts)`.

## Confirmations

```seal
confirms: round-1#1
```
What holds: a design that moves a passage, a `remove` of its section in one document and an `add` of it to another, is no longer named as a copy. Executed: `Test_pins_and_copies_in::test_accepts_a_passage_the_design_moves_naming_no_copy` passes at `c783f18f4` and fails with `5f78f553d`'s two scripts. The two `Test_copies` cases at `tests/skills/test_rule_changes.py:660-676` hold the wrapped passage and the passage standing twice, and fail with the old `copies`. The proofer's sentence (`agents/proofer.md:63-65`) now makes a copy a finding only where another file keeps the passage after the settle, so a correct move is no finding. The close's choice of taking the text out through `pattern` over subtracting runs holds as argued: `pattern` collapses whitespace runs, and `section_lines`'s text is `gfm_lines`, which changes no character but the line ends (read, `skills/verify/scripts/coordinates.py:73-83`), so the section a `remove` takes out matches the raw document. Finding 1 above is a separate defect in the same unit: a `change` handled as a `remove`.

```seal
confirms: round-1#3
```
What holds: the removal signal in `frame/plan.md:12`, as folded at `4105fd13c`. A named fact pin the settle repoints is the intended path. The signal is the count of notices that became findings at review, against the notices printed. The count rests on a finding quoting its notice, and `agents/proofer.md:66-67` now says so; the changelog's `### Process changes` row carries it (read). The plan's `## Judgments of the run` holds a row for the fold.

```seal
confirms: none
```
What matched: the folded `to` values still parse, and the design passes its own read. Executed: `rule_changes.parse` over `frame/design.md` at `c783f18f4` returns five operations, no error and no unread line. The `add` keeps its `check:` line, and the `change` of `docs/what-a-script-gates.md` *The checks* lands in a table cell and holds no `|`. `bin/seal rules --check` exits 0. `chain_check.py --baseline origin/release/v0.28.0 --root . --worktree` exits 0 and prints no pin, copy or not-read notice for this design. Its other lines are the round-1 closes this record answers, the round behind HEAD, and the gate and guarantee records still to come. Design S8 holds.

```seal
confirms: none
```
What matched: each new case against its group. The two unit cases in `Test_copies` cover the subtraction at `copies`, and the chain-check move case covers the collection of a `remove`'s section into `gone`, which no unit case reaches. `test_names_a_section_a_remove_cannot_read_as_not_read` (both ids), `test_names_a_test_and_a_document_it_cannot_open_as_not_read`, `test_names_a_test_the_parser_gives_up_on_as_not_read` (both ids) and `test_names_a_listing_git_could_not_make_as_not_read` each pin one new branch and its message, as contract rule 14 asks. `test_names_a_rule_document_that_does_not_decode_as_not_read` changes only its expected message. No case covers nothing its group did not already cover. The open case names its error's type as the platform's, so it holds where Windows raises `PermissionError` for a directory and POSIX raises `IsADirectoryError`. The seen-red claims hold: with `5f78f553d`'s `chain_check.py` and `rule_changes.py` (which `4105fd13c` leaves unchanged) in the scratch clone, every case the fix added or changed fails (executed, `## Probes`).

```seal
confirms: none
```
What matched: the new messages and the unread notice with no path. `LISTING_UNREAD` goes out at path `""`, and `unverified_check.py#annotate` prints the message alone outside CI and an annotation with no `file=` in CI (read, `skills/verify/scripts/unverified_check.py:1616-1626`). `SECTION_UNREAD` carries `section_lines`'s own reason, and the grammar requires a `remove`'s `section` (read, `skills/settle/scripts/rule_changes.py:53-57`), so the message never names a section of `None`. A `remove`'s `file` is a top-level policy-root file by the parser (`:224-229`), so `_section_text` opens nothing outside it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `c783f18f4`. This round ran narrow modules only, so the suite is `unverified`. | the branch at `c783f18f4` | the orchestrator, at `seal gate` after the rounds settle |
| The new cases on the Windows leg, the open case's `PermissionError` among them | `tests/skills/test_chain_check.py:2137-2270` | the pull request's `.github/workflows/test.yml` run |
| A tracked path that is not UTF-8, which cannot be planted on this machine's file system (finding 2) | `skills/code-review/scripts/chain_check.py:1194`, `skills/code-review/scripts/chain_check.py:1208` | the fix pass's case, which monkeypatches the listing |
| The S7 replay counts, carried from round 1 and not re-run | `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/trail/phases/phase-1.md:38` | the sealer, in its sample of the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:xdist tests/skills/test_rule_changes.py tests/skills/test_chain_check.py::Test_pins_and_copies_in tests/skills/test_passages.py` | exit 0, 110 passed |
| `.venv/bin/python -m pytest -q -p no:cacheprovider -p no:xdist tests/skills/test_rule_changes.py::Test_copies tests/skills/test_chain_check.py::Test_pins_and_copies_in`, in the scratch clone at `c783f18f4` with `git checkout 5f78f553d -- skills/code-review/scripts/chain_check.py skills/settle/scripts/rule_changes.py` | 10 failed, 9 passed: the two new `Test_copies` cases, the changed decode case, and the seven new chain-check case ids |
| `.venv/bin/python -m pytest -q -p no:cacheprovider -p no:xdist tests/skills/test_tmp_probe.py`, one file in the scratch clone's `tests/skills/`, run at `c783f18f4` and with `5f78f553d`'s two scripts, then deleted with the clone | a `change` keeping 15 words of its `from` beside an `add` of the passage to `docs/other.md`: no line for the design at `c783f18f4`; one copy notice naming `docs/policy.md`, 4 runs, with the old scripts (finding 1) |
| `python3 -I -c` loading `skills/settle/scripts/rule_changes.py` and running `parse` over this design | 5 operations, `errors []`, `unread []` |
| `bin/seal rules --check` | exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.28.0 --root . --worktree` | exit 0; no notice for this design; the round-1 closes owed a verifying round, the round behind HEAD, and the missing gate and guarantee records |

# Review round 3: 1793577579-the-pull-request-names-each-pin-a-rule-change-breaks

```seal
target: 7f0bb99b7, fixes c783f18f4..7f0bb99b7
```

This verifying round read the diff `c783f18f4..7f0bb99b7` in the main clone at `7f0bb99b7`. That diff holds round 2's record (`c73bda8cd`), the orchestrator's judgment row (`c55de1d42`), the fix commit (`bd8c45c2a`), the fix pass's close blocks (`cea3eb3ae`) and the orchestrator's design fold (`7f0bb99b7`). Probes ran in a scratch clone made with `git clone --no-local` at `7f0bb99b7`, removed before hand-back. Carried from rounds 1 and 2 as coordinates and not re-established: the load chain against `ruff.toml` `[per-file-target-version]` (the fix adds no load), the S7 replay counts in `trail/phases/phase-1.md`, and where the pin reading lives (`chain_check.py#_read_tree`, `#_section_text`, `#pins_and_copies_in`, `rule_changes.py#copies`). Every claim of the fix pass's close blocks and of the handoff was read as a claim and checked against the tree below. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` holds no `Record language` row, so the record is English.

Finding 2 is a `must`. Its notice was printed only once finding 1's fix was applied in the scratch clone, and it is quoted in the finding.

## Findings

### 1. Two `add`s of one passage into two documents get no copy notice, since the copy reading never puts an `add`'s `to` into the document it lands in

```seal
severity: should
location: `skills/code-review/scripts/chain_check.py:1262-1278`, `skills/settle/scripts/rule_changes.py:361-389`, `skills/code-review/scripts/chain_check.py:97`, `skills/code-review/scripts/chain_check.py:1238-1253`, `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/changelog.md:3`, `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/design.md:45`, `tests/skills/test_rule_changes.py:637`, `tests/skills/test_chain_check.py:2137`
evidence: executed `.venv/bin/python -m pytest -q -p no:cacheprovider -p no:xdist tests/skills/test_tmp_probe.py`
```

Why it matters: the fix reads each document "as the design's operations leave it" (`chain_check.py:97`). The parser gives three operation kinds, `add`, `change` and `remove` (`rule_changes.py:54-56`). The fix models two of them. A `change` puts its `to` where its `from` stood, and a `remove` takes its text out. An `add` puts its `to` into its document, and `pins_and_copies_in` records nothing for it (`chain_check.py:1276-1278`: `gone` is filled only where `taken` is set). So where one design adds the same passage to `docs/a.md` and to `docs/b.md`, neither `to` is compared with the other, and the check prints nothing. After the settle both documents hold the passage, which is the copy *Scope* item 6 and the design's `add` (`frame/design.md:101-102`) make a finding. The paste test then meets it at the settle's broad run, after the merge. Finding 2 below is a real instance in this very design.

The probe planted two `add`s of `Then w0 ... w14 and on.` into two documents that do not hold it. At `7f0bb99b7` the check printed no line for the design. A control with the passage already in `docs/b.md` printed one copy notice, so the design parsed and the arm ran. With the fix below applied in the scratch clone, the two `add`s printed two notices, one at each `to`, each naming the other document with 4 runs.

This is no regression. Before round 1's fix, `copies` read each document as the tree holds it, which also leaves an `add`'s `to` out (read, `5f78f553d`). Round 2's finding 1 named one instance, a `change`, and its close holds for that instance (`## Confirmations`). The class is built here from what produces it, the three operation kinds the parser gives, and the `add` is the instance left. Contract rule 12 asks the fix for the whole class.

The sentences that state the reading enumerate two kinds and read as the whole list: the module docstring (`chain_check.py:97`), `pins_and_copies_in`'s docstring (`:1248-1252`), `copies`' docstring (`rule_changes.py:366-372`), the changelog fragment (`changelog.md:3`) and the design's *Scope* item 3 (`frame/design.md:45`). Each gains the `add`. The design's sentence is the orchestrator's fold, since a fix pass does not edit `frame/design.md`.

The fix records an `add`'s `to` with no text taken out, and `copies` puts it at the document's end. The end, not the section, is enough for a run wholly inside the `to`. A run that would span the `to` and the words around it where the settle places it is not counted, and the docstring says so. This touches no OS boundary.

```python
# skills/code-review/scripts/chain_check.py#pins_and_copies_in, the first loop
        taking.append((op, taken, at))
        if taken:
            # What the settle leaves in OP's file: a `change` puts its `to`
            # where its `from` stood, and a `remove` puts nothing there.
            gone.setdefault(op.file, []).append((taken, op.new))
        elif op.kind == "add" and op.new:
            # An `add` takes nothing out and puts its `to` into OP's file.
            gone.setdefault(op.file, []).append((None, op.new))


# skills/settle/scripts/rule_changes.py#copies; its docstring reads: GONE,
# `{path: [(text, put)]}`, is what the same design's operations do to each
# document. Where TEXT is set, it is found once by `pattern`, across any
# wrapping, and replaced by PUT, the `to` of a `change`, or by nothing for a
# `remove`. Where TEXT is None, PUT is an `add`'s `to`, put at the
# document's end, so a run it shares with the words beside it is not counted.
        for taken, put in (gone or {}).get(path, ()):
            if taken and taken.split():
                # A function, so a backslash in PUT is text, not a group.
                text = pattern(taken).sub(
                    lambda _m, put=put: f"\n{put or ''}\n", text, count=1
                )
            elif put:
                text = f"{text}\n{put}\n"
```

```python
# tests/skills/test_rule_changes.py, Test_copies
    def test_names_a_run_another_add_of_the_design_puts_in(self):
        """An `add` of the same design puts its `to` into `docs/a.md`, which
        holds the passage after the settle though the tree does not yet."""
        passage = f"Then {run_of(WINDOW)} and on."
        texts = {"docs/a.md": "## S\n\nOther words.\n"}
        o = one_op("add", new=passage, file="docs/b.md")
        found = rules.copies(o, texts, {"docs/a.md": [(None, passage)]})
        assert found == [("docs/a.md", 4, f"then {run_of(WINDOW - 1)}")]


# tests/skills/test_chain_check.py, Test_pins_and_copies_in
    def test_names_a_passage_two_adds_of_one_design_put_in_two_documents(
        self, branch, ready, capsys
    ):
        """Two `add`s of one passage into two documents that do not hold it:
        each document holds it after the settle, so each `to` names the
        other document."""
        root, _code = branch
        passage = f"Then {words_of(15)} and on."
        write(root, "docs/a.md", "# A\n\n## One\n\nOther words here.\n")
        write(root, "docs/b.md", "# B\n\n## Two\n\nStill other words.\n")
        planted_spec(
            root,
            spec_with(
                f"- add\n  file: docs/a.md\n  section: One\n  to: {passage}\n"
                f"- add\n  file: docs/b.md\n  section: Two\n  to: {passage}\n"
            ),
        )
        code, out = check(root, capsys)
        assert code == 0, out
        said = spec_lines(out)
        assert len(said) == 2, out
        assert "repeats a passage of `docs/b.md`" in said[0], out
        assert "repeats a passage of `docs/a.md`" in said[1], out
```

Both cases ran in the scratch clone: the unit case failed at `7f0bb99b7` and passed with the fix, and the chain-check case is the probe as it ran. With the fix, `tests/skills/test_rule_changes.py` and `Test_pins_and_copies_in` passed whole (93 passed).

### 2. This design's own `add` and its `change` of `docs/what-a-script-gates.md` *The checks* share two runs of 15 words, so the 0.28.0 settle writes a copy the paste test refuses

```seal
severity: must
location: `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/design.md:121`, `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/design.md:103-104`, `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/design.md:73`
evidence: executed `python3 -I -c "load rule_changes.py and passages.py; parse frame/design.md; intersect passages.windows of the add's to with each change's to"`, `python3 skills/code-review/scripts/chain_check.py --baseline 8d39d6f80 --root . --worktree`
```

Why it matters: the `add` lands in `docs/the-review-record.md` *What the check reads at the pull request* and says "A source the reading cannot read, a test file, a rule document, a section a `remove` names or a file listing, is named as not read" (`frame/design.md:103-104`). The `change` at `:121` writes into `docs/what-a-script-gates.md` *The checks* "each source it cannot read, a test file, a rule document, a section a `remove` names or a file listing". Read by `passages.py#words` and `#windows`, the two values share 2 runs of 15 words, one of them "cannot read, a test file, a rule document, a section a remove names or a" (executed). After the 0.28.0 settle both documents hold that run. The pair is not in `BASELINE` (read, `tests/text/test_no_passage_is_pasted_into_a_second_file.py:158`), and the paste test fails a pair outside `BASELINE` that shares any run (`:51`). So the settle's broad run meets this design's copy, after the merge. `frame/plan.md` *Alternatives considered* row 1 states why that is late: "The copy is answerable only before the merge, by rewording the `to`." The design's S8 (`:73`) says its operations print no copy. It holds at `7f0bb99b7` only because of finding 1.

Both sentences came in with the orchestrator's fold of round 1's rewording at `c783f18f4` (executed, `git log -S` on the shared words). Round 2 read that fold, and the check it ran printed nothing for the design, for the reason finding 1 gives.

The notice, as the check printed it in the scratch clone with finding 1's fix applied:

```text
seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/design.md:121  this `to` repeats a passage of `docs/the-review-record.md`: 2 of its runs of 15 words stand there, one of them "cannot read, a test file, a rule document, a section a remove names or a"
```

The fix keeps the list in the `add`, whose section is the home of what the check reads, and has the table cell point to it. It is the orchestrator's fold, since a fix pass does not edit `frame/design.md`. With this line and finding 1's fix in the scratch clone, `rule_changes.parse` returned five operations, no error and no unread line, and the check printed nothing for the design. The cell holds no `|`.

```markdown
  to: each line of a `to` that opens like a `check:` line and is not one, and each source it cannot read, as `docs/the-review-record.md` *What the check reads at the pull request* lists them; names each test pin a `from` takes out and each run a `to` shares with another rule document, refusing neither;
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: a `change` that keeps a run of its `from` in its `to` beside an `add` of the passage elsewhere is named again. Claimed: `gone` carries `(from, to)` pairs, `None` for a `remove`, and `copies` writes each `to` in place of its `from` through a function. Found: `chain_check.py:1276-1278` appends `(taken, op.new)`, and `op.new` is None for a `remove` by the grammar (`rule_changes.py:56`, which gives a `remove` no `to`). `rule_changes.py:383-388` replaces through a lambda with `put` bound at definition, so a backslash in a `to` is text. Executed: `Test_copies::test_accepts_a_run_a_change_keeps_in_its_to` and `Test_pins_and_copies_in::test_names_a_copy_a_change_keeps_in_its_to` pass at `7f0bb99b7`. With `c783f18f4`'s two scripts in the scratch clone, both fail, and so do the two round-1 unit cases that now pass pairs (4 failed, 17 passed). The expected 3 runs in both cases are right by count: the `to` keeps `then w0 ... w14 and`, 17 words, against the passage's 18. The backslash mutation of the close was read, not re-run: a replacement string holding `\1` against a pattern with no group raises `re.error`. The docstrings at `chain_check.py:97` and `:1248-1252`, `copies`' docstring and the changelog sentence now state the replacement. Finding 1 above is the `add`, the instance of the same class this close did not reach.

```seal
confirms: round-2#2
```
What holds: the close answers the reopen with a limit and no guard, as the orchestrator's row of `2026-11-02` in `frame/plan.md` *Judgments of the run* decides, on `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame*. Read: the sentence at `chain_check.py:1188-1192` is true of the code. `git()` decodes with `errors="replace"` (`:317-326`), `_tracked` lists with `-z` (`:1160`), and both loops of `_read_tree` skip a `FileNotFoundError` (`:1198`, `:1212`). No behaviour changed and no case was owed. Round 2's `## Not judged` row for this case named the fix pass's case as its answerer; under the limit no case exists, and the row is closed by the limit sentence.

```seal
confirms: round-2#3
```
What holds: round 2 closed this finding `deferred` to the orchestrator's fold, and `7f0bb99b7` is that fold. *Scope* item 3 (`frame/design.md:45`) holds the round's proposed text whole, and *Data & interfaces* (`:78`) reads `copies(op, texts, gone)`. Executed: `git grep -n -F 'copies(op, texts)'` finds the signature only in round 2's record, and `git grep` on "design's own removals" and "takes out of that document is taken out" finds the old wording only there. The item's parenthesis lists two operation kinds, which finding 1 extends.

```seal
confirms: none
```
What matched: each new case against its group. `Test_copies::test_accepts_a_run_a_change_keeps_in_its_to` is the only unit case where `gone` carries a `to`, and the chain-check case is the only one that reaches the pairing of `op.new` into `gone`, which no unit case reaches. The two round-1 unit cases changed only their argument's shape. No case covers nothing its group did not already cover.

```seal
confirms: none
```
What matched: the narrow modules at `7f0bb99b7`. Executed: `bin/test -q -p no:xdist tests/skills/test_rule_changes.py tests/skills/test_chain_check.py::Test_pins_and_copies_in tests/skills/test_passages.py` exits 0, 112 passed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `7f0bb99b7`. This round ran narrow modules only, so the suite is `unverified`. | the branch at `7f0bb99b7` | the orchestrator, at `seal gate` after the rounds settle |
| The new cases on the Windows leg | `tests/skills/test_chain_check.py:2137`, `tests/skills/test_rule_changes.py:679` | the pull request's `.github/workflows/test.yml` run |
| The S7 replay counts, carried from round 1 and not re-run; finding 1's fix can add pairs to the copy half of that replay | `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/trail/phases/phase-1.md:38` | the fix pass for finding 1, and the sealer in its sample of the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:xdist tests/skills/test_rule_changes.py tests/skills/test_chain_check.py::Test_pins_and_copies_in tests/skills/test_passages.py`, in the main clone | exit 0, 112 passed |
| `.venv/bin/python -m pytest -q -p no:cacheprovider -p no:xdist tests/skills/test_rule_changes.py::Test_copies tests/skills/test_chain_check.py::Test_pins_and_copies_in`, in the scratch clone with `git checkout c783f18f4 -- skills/code-review/scripts/chain_check.py skills/settle/scripts/rule_changes.py` | 4 failed, 17 passed: the three `Test_copies` cases that pass pairs, and `test_names_a_copy_a_change_keeps_in_its_to` |
| `.venv/bin/python -m pytest -q -p no:cacheprovider -p no:xdist tests/skills/test_tmp_probe.py`, one file in the scratch clone's `tests/skills/`, run at `7f0bb99b7` and with finding 1's fix, then deleted with the clone | two `add`s of one passage: no line for the design at `7f0bb99b7`, two copy notices with the fix; the control with the passage already in `docs/b.md`: one copy notice; the unit case: failed at `7f0bb99b7`, passed with the fix (finding 1) |
| `.venv/bin/python -m pytest -q -p no:cacheprovider -p no:xdist tests/skills/test_rule_changes.py tests/skills/test_chain_check.py::Test_pins_and_copies_in`, in the scratch clone with finding 1's fix | exit 0, 93 passed |
| `python3 -I -c` loading `rule_changes.py` and `passages.py` at `7f0bb99b7`, parsing this design and intersecting the windows of the `add`'s `to` with each `change`'s `to` | the `change` at line 117 shares 2 runs with the `add`; the other three share none (finding 2) |
| `python3 skills/code-review/scripts/chain_check.py --baseline 8d39d6f80 --root . --worktree`, in the scratch clone with finding 1's fix, then again with finding 2's line | exit 0 both times; first one copy notice at `frame/design.md:121` naming `docs/the-review-record.md`, then no line for the design; `rule_changes.parse` returned five operations, no error, no unread line |
| `git log -S` on the shared words over this design | `c783f18f4` alone (finding 2) |

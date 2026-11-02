# Review round 1: 1793577579-the-pull-request-names-each-pin-a-rule-change-breaks

```seal
target: 5f78f553d against origin/release/v0.28.0
```

The target is the branch at `5f78f553d` against `origin/release/v0.28.0` (`8d39d6f80`). No earlier round exists, so no fact is carried from one. Three facts are carried from the crafter's executed account and were not re-run here: the S7 replay counts over `a92c358b^` (`trail/phases/phase-1.md`), the seen-red runs and mutation scores of each new case, and the Scope item 7 census of sentences. `seal/parity.md` is not declared, so the round block holds no `original:` line.

## Findings

### 1. A design that moves a passage from one rule document to another gets a copy notice for the text it takes out, and the proofer's sentence makes that notice a finding

```seal
severity: should
location: `skills/settle/scripts/rule_changes.py:361-380`, `skills/code-review/scripts/chain_check.py:1197-1236`, `agents/proofer.md:62-65`, `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/design.md:101`
evidence: executed `python3 -I test_tmp_probe.py`
```

Why it matters: `rule_changes.py#copies` compares a `to` with each rule document as the working tree holds it, and it leaves out only the document the operation itself writes. It never subtracts what the same design's other operations take out. The design's own grammar writes a move as a `remove` (or a `change` with a `from`) in one document and an `add` in another. The probe parsed such a design: a `remove` of section `S` from `docs/a.md` and an `add` to `docs/b.md` whose `to` is the passage `S` holds. `copies` named `docs/a.md` with 6 shared runs, under Python 3.15 and 3.9 alike. After the settle, `docs/a.md` holds none of those runs, so the paste test would find no copy.

The sentence the build added to `agents/proofer.md:62-65` then turns the notice into a finding: "and so is a `to` that repeats a passage another file holds". Its fact branch defers to the settle, but its copy branch gives the proofer no question to weigh. A proofer that follows it writes a finding against a correct move, and the fix pass rewords a `to` that was right. The same categorical statement stands in the design's `add` (`frame/design.md:101`, "A pin of a rule's wording and a copy are findings"), which the settle writes into `docs/the-review-record.md`. On the record the case did not arise: the replay over the 0.27.1 designs named 5 pairs, all real copies (`trail/phases/phase-1.md`, S7, carried and not re-run). The shape is still one the rule-changes grammar accepts and one that moving a rule's home calls for.

The fix takes the noise out at the reader, so the sentence stays true. `copies` subtracts the runs of what the design takes out of each document, and `pins_and_copies_in` collects that text once per design. A case in `Test_pins_and_copies_in` plants the move and expects no copy notice. It is seen red against `5f78f553d`.

```python
# skills/settle/scripts/rule_changes.py
def copies(op, texts, gone=None):
    """... GONE, `{path: [text]}`, is what the design's operations take out
    of each document; a run that stands only in that text is no copy."""
    p = passages()
    if op.new is None or not p.in_corpus(op.file):
        return []
    said = p.words(op.new)
    order = [" ".join(said[i : i + p.WINDOW]) for i in range(len(said) - p.WINDOW + 1)]
    out = []
    for path in sorted(texts):
        if path == op.file or not p.in_corpus(path):
            continue
        shared = p.windows(p.words(texts[path])).intersection(order)
        for taken in (gone or {}).get(path, ()):
            shared -= p.windows(p.words(taken))
        if shared:
            out.append((path, len(shared), next(r for r in order if r in shared)))
    return out


# skills/code-review/scripts/chain_check.py#pins_and_copies_in, before `for op in ops:`
gone = {}
for op in ops:
    if op.old is not None:
        gone.setdefault(op.file, []).append(op.old)
    elif op.kind == "remove":
        gone.setdefault(op.file, []).append(_section_text(rules, root, op) or "")
# ... and in the loop:
#     for path, count, run in rules.copies(op, sources["documents"], gone)
```

A subtracted run is only removed where a run of the other document's text equals a run of the taken text after `passages.py#words`. A `from` that `words` normalises differently from the document's text (a wrapped section name, for one) still leaves its runs standing. That residue is a notice, which refuses nothing.

```seal
verdict: fixed 28e82bf4d
answer: Held, fixed in my own words rather than the paste-ready fix: `rule_changes.py#copies` takes a `gone` argument, `{path: [text]}`, and takes each text out of its document once through `rule_changes.py#pattern`, across any wrapping, before counting runs, where the proposal subtracted the taken text's runs; so a passage the document holds twice still counts once taken out, and no normalisation residue is left. `chain_check.py#pins_and_copies_in` collects each `from`, and each section a `remove` with no `from` takes out, per document once per design. Seen red at `4105fd13c`: `Test_copies::test_refuses_a_run_that_stands_only_in_text_the_design_takes_out` and `::test_accepts_a_run_the_document_still_holds_after_what_is_taken_out` (no `gone` argument), and `Test_pins_and_copies_in::test_accepts_a_passage_the_design_moves_naming_no_copy` (named `docs/policy.md`); `seal mutate` 4 of 4 red over the subtraction and its call. With the reader fixed, `agents/proofer.md` step 7 now makes a copy a finding where another file keeps the passage after the settle, which also covers a removal by another pending design that this design's read cannot see. `frame/design.md:101` ("a copy are findings") holds for a copy so counted, and `:48` (*Scope* item 6) states the old proofer sentence; both are named to the orchestrator to fold to "a copy another file keeps after the settle".
```

### 2. The pin reading of a `remove` with no `from` reads nothing, and says nothing, where the working tree lacks its document or section

```seal
severity: should
location: `skills/code-review/scripts/chain_check.py:1183-1194`, `skills/code-review/scripts/chain_check.py:1161-1162`, `skills/code-review/scripts/chain_check.py:1175-1176`, `skills/code-review/scripts/chain_check.py:1219-1220`
evidence: read `skills/code-review/scripts/chain_check.py:1148-1236`, `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/trail/phases/phase-1.md:9`
```

Why it matters: `_section_text` returns None in three cases: the operation's document cannot be opened, it does not decode, or `rule_changes.py#section_lines` finds no such section. In the last case it throws away the reason the section reader gave (`span, _why = ...` at `chain_check.py:1191`). `pins` then returns `[]` for the operation, and no notice says the section was not read. The reader prints nothing, which looks the same as finding no pin. A `remove` of a section that another pending design adds reaches this path, because the section is not in the tree until the settle writes it. In the same way, `_read_tree` skips any `OSError` (`:1161`, `:1175`) with no notice. Its docstring gives the reason as a file git lists and the tree has deleted, but `PermissionError` and `IsADirectoryError` take the same branch.

`skills/core/SKILL.md` *The rule a mechanism is kept against* has a reader name as not read what it could not read. The design's E3 adopts that rule. The phase-1 departure (`trail/phases/phase-1.md:9`) applied it to one instance, a rule document that does not decode, after the first build skipped it unnamed. That record does not name the class the instance belongs to: a file or section the pin and copy reading could not read, skipped with no notice. Contract rule 12 asks for the class, and this finding lists the instances left: the section not found, the document not opened or not decoded for a `remove`, and an `OSError` other than a missing file.

```python
# chain_check.py, beside DOCUMENT_UNREAD
SECTION_UNREAD = "`{file}` *{section}* could not be read in the working tree ({why}), so no pin in it is named"


def _section_text(rules, root, op):
    """(text, None) for the section OP takes out, as the working tree at ROOT
    holds it, or (None, why) where it cannot be read."""
    try:
        with open(os.path.join(root, *op.file.split("/")), encoding="utf-8") as f:
            text = f.read()
    except (OSError, UnicodeDecodeError) as exc:
        return None, type(exc).__name__
    span, why = rules.section_lines(text, op.section)
    if span is None:
        return None, why
    return "\n".join(rules.reader().gfm_lines(text)[span[0] - 1 : span[1]]), None


# in pins_and_copies_in
        elif op.kind == "remove":
            taken, why = _section_text(rules, root, op)
            at = op.line
            if taken is None:
                said = SECTION_UNREAD.format(file=op.file, section=op.section, why=why)
                out.append((rel, at, RULE_CHANGES_UNREAD.format(why=said)))

# in _read_tree, both loops: skip a deleted file only
        except FileNotFoundError:
            continue
        except (OSError, UnicodeDecodeError, ...) as exc:  # named as not read
```

`section_lines`'s second value is assumed to be a sentence saying why, as its call in `rule_changes.py` reads it. The tree was not checked for its type at every return. Each new notice is pinned by a case in `Test_pins_and_copies_in`, as contract rule 14 asks.

```seal
verdict: fixed 28e82bf4d
answer: Held. The class was listed by taking the reading apart into each source it opens: the two `git ls-files` listings (`tests/*.py`, `*.md`); each test file's open, decode and `ast.parse`, which raises `SyntaxError` or `ValueError` on a bad source and `RecursionError` or `MemoryError` past its nesting limit; each rule document's open and decode; and a `remove` with no `from`'s document open and decode and its `section_lines` lookup (no heading, or one standing twice). A `from` and a `to` are design text and open nothing. Each instance is now named as not read: `LISTING_UNREAD` (no path, line 0) for a listing git cannot make, `TEST_UNREAD` with the error's name for every test-file failure (`TEST_UNREADABLE`, which also covers the `MemoryError` row of `## Not judged`), `DOCUMENT_UNREAD`, now `could not be read (<error>)`, for a document's open or decode, and `SECTION_UNREAD` at the operation's line with `section_lines`' own reason, an absent document reading "the document is not in the tree". A `FileNotFoundError` on a listed test or document, one the working tree deleted, is still skipped, since it is no file of the tree the settle writes into; that is the one silent case left, and `_read_tree`'s docstring says so. Seen red at `4105fd13c`: `test_names_a_section_a_remove_cannot_read_as_not_read` (both ids), `test_names_a_test_and_a_document_it_cannot_open_as_not_read`, `test_names_a_test_the_parser_gives_up_on_as_not_read` (both ids) and `test_names_a_listing_git_could_not_make_as_not_read`; `seal mutate` 6 of 6 red over the branches. Other statements: `chain_check.py`'s module docstring is corrected in the same commit; `frame/design.md:102` ("A test file the check cannot parse is named as not read") and `:120` (`each test file it cannot parse`) state the narrower rule and are named to the orchestrator to fold.
```

### 3. The plan's signal for removing the reading fires on the path the design intends, so the settle cannot weigh the mechanism by it

```seal
severity: should
location: `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/plan.md:12`
evidence: read `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/plan.md:12`, `agents/proofer.md:62-65`, `docs/what-a-script-gates.md:53`, `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/design.md:18-19`, `tests/behaviour/test_waiver_decided_at_start.py:585-597`
```

Why it matters: `frame/plan.md:12` gives the signal that the notices have become noise: "a settle whose broad run fails on a pin the pull request had named". The answer it gives is to remove the reading. The proofer's sentence (`agents/proofer.md:64-65`) says a named pin of a fact is no finding, "since the settle repoints it". #1278's criterion (`docs/what-a-script-gates.md:53`) is that a case pins a fact and one that pins wording goes, so after #1278 most standing pins are facts. A fact pin that a pull request named, that the proofer correctly passed, and that the settle's broad run then failed on is the designed path. The plan's signal reads that path as the failure. The settle that weighs this mechanism by *The rule a mechanism is kept against* would remove a reading that worked, or keep one that caught nothing, because the signal cannot tell the two apart.

The design's own numbers frame the noise question that the signal should answer. At the base, 4 of 4 named pins would not fail, and each is a fact by its comment (`frame/design.md:19`, G13; `tests/behaviour/test_waiver_decided_at_start.py:594` reads `agents/framer.md`). The four pins #1278 kept and this design counts (G12, `frame/design.md:18`) are facts too, so the sentence makes each of them no finding. After #1278, the pin half catches only at the pull request: wording pins #1278 did not list. The copy half is the one that can be answered only before the merge (plan row 1). What the reading caught is therefore the count of notices that became findings at review. The plan names no record that would hold that count.

```markdown
The signal is the count the settle reads in the released work items' round records: how many pin and copy notices became findings at review, against how many were printed. A named fact pin that the settle repointed is the designed path. It counts as a notice that caught nothing, and is no failure. A settle whose broad run fails on a wording pin or a copy that a pull request named and its proofer passed is the second signal. Where the count stays at nothing over two settles, the answer is to remove the pin half, since `skills/core/SKILL.md` *The rule a mechanism is kept against* weighs it by what it caught.
```

```seal
verdict: fixed 4105fd13c
answer: Held, and folded by the orchestrator at `4105fd13c`, with a row in `## Judgments of the run`, since a fix pass does not edit `frame/plan.md`. I read the fold and find it right: a named fact pin the settle repoints is now the intended path, and the signal is the count of notices that became findings at review against the notices printed. That count rests on a finding naming the notice it came from, which nothing told the proofer to do, so `28e82bf4d` adds to `agents/proofer.md` step 7 that a finding taken from such a notice quotes it, and the changelog's process row says so.
```

## Confirmations

```seal
confirms: none
```
What matched: every notice the new reading prints refuses nothing. `pins_and_copies_in`'s result goes only to `notices` (`skills/code-review/scripts/chain_check.py:1263-1268`), and `main` prints notices without changing the exit code. Executed: each `Test_pins_and_copies_in` case asserts exit 0 and passed in the narrow run. `chain_check.py --baseline 8d39d6f80 --root . --worktree` at HEAD exited 0 under Python 3.15 and under `/usr/bin/python3` 3.9.6. Its only refusals were the round, gate and guarantee records this round precedes, and it printed no pin, copy or not-read notice, so design S8 holds and every test module parses at the floor. One exception was found by the probe. A test source that makes `ast.parse` raise `MemoryError` (100,000 unary minus signs, under 3.15) is not caught by `_read_tree` and ends the check with a traceback. It is a row of `## Not judged`, not a finding, because no shipped file has that shape.

```seal
confirms: none
```
What matched: the load chain against `ruff.toml` `[per-file-target-version]`. `chain_check.py` loads `skills/verify/scripts/unverified_check.py`, which loads `skills/settle/scripts/rule_changes.py` (`unverified_check.py:1382`). That loads `passages.py` (`rule_changes.py:47`), which loads `unverified_check.py` again (`passages.py:21`), and `chain_check.py` loads `.github/scripts/rules.py` and `hooks/lib/fields.py` besides. Each of the five script modules stands in the table at `py39` (read, `ruff.toml:47-51`), and `passages.py` is the one this diff adds. `hooks/lib/fields.py` falls under the table's `hooks/*.py` row, whose `*` crosses a `/`. Executed: `tests/hooks/test_launch.py`, which holds the table both ways against what the walk reaches, passed. `uvx ruff check` over the three changed scripts exited 0.

```seal
confirms: none
```
What matched: the move of the paste reader changes nothing the paste test asserts (design S6). Executed: `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py` and `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` passed with `BASELINE` untouched. The phase-1 departure claimed that the census `tests/censuses.py#heading_rule` refused the moved `HEADING` pattern, so `passages.py` reads a heading through `unverified_check.py#heading_level`. Read against the base's `HEADING` (`^ {0,3}#{1,6}(\s|$)`), the two readings differ only after a `#` run that a whitespace character other than space or tab follows. `tests/test_censuses.py` passed.

```seal
confirms: none
```
What matched: the claim that the proofer's sentence lets a proofer weigh a notice. It holds for a pin: the sentence sends the proofer to `docs/what-a-script-gates.md` *The checks*, whose `the cases under tests/text/` row (`:53`) holds #1278's fact-or-wording criterion. Neither branch asks the proofer to change the test, the design or the check. It does not hold for a copy, which is finding 1.

```seal
confirms: none
```
What matched: the new cases against their groups. `Test_in_corpus` and `Test_windows` cover what no case covered before. `Test_words` holds the two cases moved from the paste test unchanged in what they assert. Three chain-check cases add no branch the unit cases do not already hold: the `to` that keeps the literal, the fourteen-word half of the copy case, and the Korean edition. Each is a unit case of `Test_pins` or `Test_copies` driven through `pins_and_copies_in`. Design *Scope* item 5 and S2, S4 and S5 require each one at the chain-check level, so they are no finding. The `gaps.md` *Not done* claim also holds (read, `rule_changes.py:379`). The run a copy notice prints is the first in the `to`'s order, and in every case that run is also the first in sorted order.

```seal
confirms: none
```
What matched: the changelog fragment against the phase records (read). The not-read sentence covers both files. The replay counts and the process row's text are `trail/phases/phase-1.md`'s and `agents/proofer.md:60-65`'s. The `### Process changes` row exists because the diff changes `agents/proofer.md`. Executed: `bin/seal rules --check` and `bin/seal layout --check tests` exited 0.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `5f78f553d`. This round ran narrow modules only, so the suite is `unverified`. | the branch at `5f78f553d` | the orchestrator, at `seal gate` after the rounds settle |
| The new cases on the Windows leg, where the paths come from `git ls-files` and are split and joined for `open` | `skills/code-review/scripts/chain_check.py:1155-1194` | the pull request's `.github/workflows/test.yml` run |
| The S7 replay counts (26 pins, 5 pairs, every pin the 0.27.1 settle repointed among them). Carried from the crafter's executed run and not re-run here. | `seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/trail/phases/phase-1.md:38` | the sealer, in its sample of the crafter's claims |
| A test source that makes `ast.parse` raise `MemoryError` or `RecursionError` ends `chain-check` with a traceback, not a not-read notice | `skills/code-review/scripts/chain_check.py:1158-1166` | the orchestrator: a limit sentence, or catching the two in `_read_tree` |

## Probes

| Command | Result |
|---|---|
| `python3 skills/code-review/scripts/chain_check.py --baseline 8d39d6f80 --root . --worktree` | exit 0; refusals only for the missing round, gate and guarantee records; no pin, copy or not-read notice; 1.9 s wall |
| `/usr/bin/python3 skills/code-review/scripts/chain_check.py --baseline 8d39d6f80 --root . --worktree` (3.9.6) | exit 0; the same lines; no test module named as not read |
| `bin/test -q tests/skills/test_passages.py tests/skills/test_rule_changes.py tests/skills/test_chain_check.py::Test_pins_and_copies_in tests/hooks/test_launch.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/test_censuses.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` | exit 0, 519 passed |
| `bin/seal rules --check`; `bin/seal layout --check tests`; `uvx ruff check` over the three changed scripts | each exit 0 |
| `python3 -I test_tmp_probe.py`, run once from the round's scratch directory with the clone as its argument, under 3.15 and 3.9.6, then deleted | a `remove` of `docs/a.md` *S* plus an `add` of its passage to `docs/b.md`: `copies` names `docs/a.md`, 6 runs (finding 1). 100,000 unary minus signs: `ast.parse` raises `MemoryError` under 3.15 and parses under 3.9. `copies` costs 0.075 s (3.15) and 0.093 s (3.9) per operation over the 61 rule documents |

# Review round 1: 1793795355-the-census-reads-every-entry-point

```seal
target: 4bca71fb5 against release/v0.32.0
```

This round reviews the branch at 4bca71fb5 against `release/v0.32.0`,
which is `origin/main` at 479a79d15 (`git rev-parse`, executed). No earlier
round exists, so this round carries no fact, and every fact below was
opened this round. The repository declares no `seal/parity.md`, so no
`original:` line is owed. `seal/config.md` has no `Record language` row, so
this record is English. The runs took place in a `git clone --no-local` of
the worktree at 4bca71fb5, under the session scratchpad, and the clone has
since been removed.

Stage 1 read `routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, both phase records, `gaps.md` and `changelog.md`. It
read them against `skills/core/SKILL.md` *The rule a mechanism is kept
against*, the `hooks/lib/console.py` docstring, `CONTRIBUTING.md` *House
rules* and `docs/running/what-a-script-gates.md` *The checks*. Stage 2 read
the diff of `tests/censuses.py`, `tests/test_censuses.py`,
`tests/hooks/test_console.py`, the text pin and the 26 scripts. These are
the axes that apply to this diff:

- what the census reads and what it decides on;
- its corpus;
- the boundary of the loop form, meaning each guard of `loop_pairs`;
- the order of statements in a block;
- what each refusal tells a contributor;
- what the removed case held;
- whether every entry point gives the answer at HEAD.

Authorization, query scope, concurrency and security do not apply. The
census reads source text and runs nothing.

## Findings

### 1. Two refusals state that an entry point gives no answer, where the census only failed to read the answer in its form

```seal
severity: should
location: `tests/censuses.py:749-754`, `tests/censuses.py:769-774`, `CONTRIBUTING.md:423-426`, `tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py:24-29`, `tests/test_censuses.py:596-600`, `tests/test_censuses.py:636-642`
evidence: executed the round's probe `test_tmp_entry_point_probe.py` (see `## Probes`); read `tests/censuses.py:741-775`, `tests/test_censuses.py:645-661`, `CONTRIBUTING.md:423-427`
```

Why it matters: `skills/core/SKILL.md` *The first value* says "A script that
answers 'these differ' where the meaning is the same is the worst result the
workflow can give". The census reads exactly: `ast`, `ast.literal_eval` and
equality with `STREAMS`. Refusing a spelling it does not read is the
frame's deliberate choice (`frame/plan.md` *Technical context*, the first
failure scenario), so the refusal is grounded. The wording of the refusal
is a separate matter. Two of the three messages state a fact the census did
not read:

- The loop message at `tests/censuses.py:769` says "the loop does not give
  the answer `hooks/lib/console.py#STREAMS` holds". The case at
  `tests/test_censuses.py:648` plants `for _name, _errors in
  console.STREAMS:` with the `reconfigure` call of the form. That loop gives
  exactly that answer, and the census tells the contributor that it does
  not. The probe got the same line for a `list` literal of the same pairs
  and for a loop of the form with an `else:` clause.
- The message for a block with no answer, at `tests/censuses.py:749`, says
  "the `__main__` block gives the streams no answer". The probe planted
  `if True:` with `console.to_utf8()` inside it as the block's first
  statement and got that line. The census reads only the block's own
  statements (`tests/censuses.py:745`), so it found no answer there. It did
  not find that the block gives none.

The rule a contributor reads makes this worse. `CONTRIBUTING.md:423-426`
says the answer may stand "as the call `console.to_utf8()` or as a loop over
the same pairs". A loop over `console.STREAMS` is a loop over the same
pairs, and the census refuses it. The third message, on order, at
`tests/censuses.py:759-763`, states only what the census read, and it
stands.

The fix makes each message say what the census did not read, and makes the
rule name the one form. The second fence below is the `CONTRIBUTING.md`
encoding bullet, from line 423. A spelling outside the form then costs the
contributor the one rewrite the plan accepts, and the census no longer says
the answer is missing. The text pin currently holds the whole sentence. By
*The checks*, the row on the cases that read prose, a case "pins a fact a
reader acts on; one that pins wording goes". So the snippet below pins the
facts and not the sentence.

```python
# tests/censuses.py, answer_problems: the two messages
            guard.lineno: (
                "the census reads no answer among the `__main__` block's own "
                "statements, so an entry point that raises while printing may "
                "die with stdout empty; open the block with `console.to_utf8()`, "
                "or with a loop over the pairs `hooks/lib/console.py#STREAMS` "
                "holds, or put `# exempt from entry_point: <why>` on its own "
                "line above it"
            )
...
            problems[answer.lineno] = (
                "the census does not read this loop as the answer "
                "`hooks/lib/console.py#STREAMS` holds; it reads a `for` over the "
                f"literal pairs {streams!r} that calls "
                '`.reconfigure(encoding="utf-8", errors=<errors>)` on '
                "the stream it binds from `getattr(sys, <name>, None)`; name those "
                "pairs in that form, or make the call `console.to_utf8()`"
            )
```

```markdown
  names `encoding="utf-8"`. Every entry point, a tracked `.py` with a
  `__main__` block, also opens its first such block with the answer
  `hooks/lib/console.py#STREAMS` holds, as the call `console.to_utf8()` or
  as a loop over the literal pairs in the one form
  `tests/censuses.py#loop_pairs` reads. The `encoding` and `entry_point`
  censuses in
```

```python
# tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py
    assert "opens its first such block with the answer" in flat
    assert "the one form `tests/censuses.py#loop_pairs` reads" in flat
    assert "enforce both over every tracked `.py`" in flat
```

The snippet leaves out four statements of the same fact, and the fix pass
owes each of them:

- the two message pins, at `tests/test_censuses.py:596-600` and `:636-642`;
- the third bullet of the changelog fragment, which repeats "as the call or
  as a loop over the same pairs";
- `frame/design.md` *Scope* item 6, which states the same words. It is the
  orchestrator's to fold.

`tests/censuses.py#entry_point`'s docstring and `answer_problems`'
docstring already say "in the one shape `loop_pairs` reads" and "in the
second form", and they stand.

```seal
verdict: fixed bc6d3387a
answer: The finding holds, and the paste-ready text was not applied as given. Its no-answer message kept "a loop over the pairs `hooks/lib/console.py#STREAMS` holds", which admits the `console.STREAMS` loop that the CONTRIBUTING.md sentence was faulted for. In bc6d3387a the no-answer refusal says the census reads no answer among the block's own statements, and that an entry point that gives none dies with stdout empty when it raises while printing. It names the loop as one over `hooks/lib/console.py#STREAMS`' literal pairs in the one form `tests/censuses.py#loop_pairs` reads. The loop refusal says the census does not read this loop as the answer `STREAMS` holds. CONTRIBUTING.md's "a loop over the same pairs" now reads "a loop over its literal pairs in the one form `tests/censuses.py#loop_pairs` reads". The text pin now holds three facts: what the block opens with, the one form, and what the censuses enforce over. The two message pins in `tests/test_censuses.py` were changed first, together with the text pin, and all four cases failed against the old messages and the old bullet, each at the new wording (executed). They passed after the change. The same claim stood in `answer_problems`' docstring ("the block holds no answer"), in `entry_point`'s docstring ("no answer is refused", "a loop that is not that answer") and in the fragment's first and third bullets. fdd342bb8 corrects them. The rule's other statements are named in the hand-back. `frame/design.md` *Scope* item 6 is among them, for the orchestrator to fold.
```

### 2. No case holds the refusal of a loop whose target is not two names, which design Scope item 2 states

```seal
severity: should
location: `tests/test_censuses.py:645-661`, `tests/censuses.py:672-678`
evidence: executed `bin/seal mutate tests/censuses.py --replace "and len(target.elts) == 2" "and len(target.elts) >= 2" --tests "bin/test -q -p no:xdist tests/test_censuses.py -k Test_entry_point"`, the same with `isinstance(target, ast.Tuple)` made `hasattr(target, "elts") or True`, and the same with `and all(isinstance(e, ast.Name) for e in target.elts)` made `and True`: each printed `SURVIVED`
```

Why it matters: design *Scope* item 2 says the loop form's "target is two
names". Item 3 says a `for` statement that is not of the loop form is
refused at its `for` line. `loop_pairs` holds that refusal with three
guards at `tests/censuses.py:672-678`. Each of the three was broken alone,
and every case of `Test_entry_point` passed against each one. With the
guards in place, the probe planted a one-name target, a three-name target
and a nested target. Each was refused at its `for` line. With a guard
removed, the census raises instead of refusing (read): the name unpacking
at `:679` fails with `AttributeError` or `ValueError`, so a contributor
gets a traceback in place of the line item 3 promises. This is behaviour
the diff added and no case holds. That makes it the *Regression test* row
of `skills/code-review/SKILL.md` *Probes and regression tests*. Phase 1's
mutation table (`trail/phases/phase-1.md`, M1 to M9) has no run on these
guards, and no case for them is mentioned elsewhere in the record.

```python
    @pytest.mark.parametrize(
        "target", ["_pair", "_name, _errors, _extra", "_name, (_errors, _extra)"]
    )
    def test_refuses_a_loop_whose_target_is_not_two_names_at_its_for_line(
        self, tmp_path, target
    ):
        text = loop().replace("for _name, _errors in", f"for {target} in", 1)
        root = plant(tmp_path, "hooks/x.py", GUARD + text + "    main()\n")
        assert lines_of(censuses.entry_point("hooks/x.py", root)) == ["hooks/x.py:2"]
```

Contract rule 15 asks that each arm be shown red with only its guard
removed. The `_pair` arm goes red against the `ast.Tuple` check, the
three-name arm against the length check, and the nested arm against the
`ast.Name` check. The fix pass states how it showed each one red.

```seal
verdict: fixed 6c77082d6
answer: The finding holds. 705109345 adds `test_refuses_a_loop_whose_target_is_not_two_names_at_its_for_line` to *Test_entry_point*, beside the shape case, with one-name, three-name and nested targets. 6c77082d6 gives the arms the ids `one-name`, `three-names` and `nested`, so a run can name each one. Each arm was shown red with only its own guard removed, by one `bin/seal mutate tests/censuses.py` run each against that arm's node id (executed). `isinstance(target, ast.Tuple)` made `True` turned the `one-name` arm red, with `AttributeError` at `tests/censuses.py:675`. `len(target.elts) == 2` made `>= 2` turned `three-names` red, with `ValueError` at `:679`. The `ast.Name` check made `True` turned `nested` red, with `AttributeError` at `:679`. Each run ended `red: the cases failed against the mutation`, and the command restored the file. Each failure is the census raising where its guard would have refused, so each arm pins its own guard.
```

## Confirmations

What matched: every entry point gives the answer at HEAD, read by a probe
written apart from the census, as design *User scenarios & acceptance*'s
last row asks. The probe parsed every tracked `.py` and found 48 files with
a module-level `__main__` block. It took the first statement of each first
block that is `console.to_utf8()` or a `for` holding `reconfigure`. It ran
that statement against a stand-in `sys`, and against a stand-in `console`
wherever the file imports `console`. In 45 of the 48, the answer is the
block's first statement and puts the three streams into `STREAMS`' pairs.
The file binds `sys` at module level, and each of the seven that make the
call imports `console`. `hooks/lib/launch.py` gives none, and that is its
exemption. `broad_gate.py:3253` and `seal_stamp.py:1513` give the answer
after two statements and after one (executed). The census does not read
the imports, and this probe did. No loop at HEAD leaves out the `hasattr`
guard (executed: a count of `.reconfigure(` against `hasattr(` in each file
`hooks/lib/console.py`'s `git grep` lists).

What matched: the census reads exactly what the frame says it reads. It
reads the first module-level block (`tests/censuses.py:793`), and the
corpus is every tracked `.py`, because `_python` is called without `under`
(`:790`). `STREAMS` is parsed out of `hooks/lib/console.py` under `ROOT`
(`:724-738`), and the census keeps no copy of it. The one judgment it makes
is in the wording of two messages (finding 1). I re-ran phase 1's M1, the
corpus, and M3, the pair comparison, as one `seal mutate` batch, and both
were red (executed). That matches the phase record's table.

What matched: two of the guards phase 1 ran no mutation on hold no fact the
frame states. Each survived its mutation (executed, the same command as
finding 2's evidence). They are the `orelse` guard at
`tests/censuses.py:670` and the `getattr` argument count at
`tests/censuses.py:693`. With either removed, the census accepts a loop
with an `else:` clause, or a `getattr` given four arguments, which raises
`TypeError` at run time. The frame says nothing on either, so this round
opens no finding for them.

What matched: the exemptions of `broad_gate.py:3246` and
`seal_stamp.py:1508` state reasons that hold. `seal_stamp.py:1509` asks
`pick_shape(sys.stdout)` before the loop. `broad_gate.py:3247-3252` loads
the stamp module and asks `_stamp.is_utf8(sys.stdout)` before the loop
(read). The only output before the loop is the `Refused` path's write to
`stderr`, which Python opens with `backslashreplace`, so that write cannot
raise. `hooks/dispatch.py`'s exemption is gone. Its loop is the block's
first statement and gives `STREAMS`' pairs (executed, the probe).

What matched: the removal of
`tests/hooks/test_console.py#test_a_release_script_run_on_its_own_gives_the_answer_streams_holds`
(plan A8) holds. The census now reads the pairs and the `reconfigure` call
of the three release scripts' loops, and of every other loop. Plan A8 says
"the case catches nothing the census misses", and that is not true as
written. The run-time case would also have caught a loop that names an
unbound `sys`, and the census does not read imports. The probe above found
`sys` bound in every entry point (executed), and `tests/github/test_rules.py:757`
still runs `rules.py` as a script (read). So the release loses no instance,
and the claim is a sentence of the plan rather than a defect of the tree.

What matched: the `gaps.md` *Not done* point on
`label_merged_on_release_branch.py` and `release_completeness_check.py`
needs no change. Both loops give `STREAMS`' pairs (executed, the probe), and
the census reads the answer, not the form. Plan A10's reason for the loop
is that a script that loads nothing from `hooks/lib/` would otherwise add
a load that can fail before the answer. That reason does not cover these
two files, because their sibling has already loaded `console` at import. A
call would therefore cost them nothing, and the loop costs them nothing
either. `frame/design.md` *Scope* item 5, as folded at 4bca71fb5, names
both files under the loop. `hooks/lib/console.py`'s sentence "None of the
others says why it copies the loop" stays true of them. No behaviour
differs between the two forms.

What matched: the five calls moved out of `main()` are each the first
statement of their block, and each file imports `console` (executed, the
probe). Plan A7 says no file calls these scripts' `main()` from outside.
The tests do call it in process, for example
`tests/github/test_finding_counts.py:90` and
`tests/github/test_tag_release.py:141` (read). A7's own failure scenario
names those in-process calls, and the console docstring's reason for
keeping the call off import covers them.

What matched: the new cases each cover a guard the group did not cover
before. Phase 1's M1 to M9 each turned a different case red, and two of
them were re-run red this round. `seal layout --pairs` names no pair for
`tests/test_censuses.py`, `tests/hooks/test_console.py` or the text pin
(executed). The `evals/scripts/noninferiority.py` hunk is its `__main__`
block alone (`git diff 479a79d15..4bca71fb5`, executed). The stale
`.test_durations` keys that `gaps.md` *Not done* names are dropped by the
shards' `--clean-durations` and the union that `durations_union.py`
documents at `:4-16` (read).

What matched: the three modules of the plan's *Verified by* cells passed.
They are `tests/test_censuses.py`, `tests/hooks/test_console.py` and the
text pin, with 198 passed (executed, `bin/test -q` over the three). That
run includes the census sweep of every tracked file. No phase record
claims the suite, so the suite's label is honest.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite, the lint and the typecheck at HEAD: `unverified` by this round (contract rule 2) | the branch at 4bca71fb5 | the orchestrator, at its broad run |
| Whether the loop form should also require the `hasattr` guard. The census accepts a loop that calls `reconfigure` on the bound stream with no `hasattr` check (executed, the probe), and such a loop raises where a stream is `None`, which `hooks/lib/console.py#to_utf8`'s docstring names. No loop at HEAD lacks the guard, and design *Scope* item 2 does not name it | `tests/censuses.py:664-704` | the orchestrator, as a fold of design *Scope* item 2 or a follow-up |
| The seventeen repaired scripts under a cp949, cp932 or cp936 console on Windows, carried from `gaps.md` *Not verified* | `gaps.md` | the repository owner, on a Windows console |

## Probes

| Command | Result |
|---|---|
| `.venv/bin/python -m pytest -q -s -p no:xdist -p no:cacheprovider test_tmp_entry_point_probe.py`, a probe that parses every tracked `.py`, runs each first block's answer statement against a stand-in `sys`, checks the module-level `import sys` and `import console`, and runs `censuses.entry_point` over nine planted shapes | 48 entry points. 45 give `STREAMS`' answer first, with `sys` bound and `console` imported where called. `launch.py` gives none, `broad_gate.py` gives it at index 2 and `seal_stamp.py` at index 1. Planted shapes: `for`-`else`, one-name target, three-name target, nested target, four-argument `getattr`, `console.STREAMS` and a `list` literal are each refused at line 2 with the loop message. `if True:` around the call is refused at line 1 with the no-answer message. A loop with no `hasattr` guard is accepted. The file was deleted after the run |
| `bin/seal mutate tests/censuses.py --replace <old> <new> --tests "bin/test -q -p no:xdist tests/test_censuses.py -k Test_entry_point"`, five runs: the `orelse` guard dropped, `len(target.elts) == 2` made `>= 2`, `isinstance(target, ast.Tuple)` made true, the `ast.Name` check made true, `in (2, 3)` made `>= 2` | each `SURVIVED`, exit 1, the file restored by the command |
| the same command as one batch: `_python(rel, root)` given `("hooks/",)`, and `!= streams` made `is None` | `2 mutants, 2 red, 0 SURVIVED` |
| `bin/test -q tests/test_censuses.py tests/hooks/test_console.py tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` | 198 passed |
| `bin/seal layout --pairs` | no pair names the three modules |

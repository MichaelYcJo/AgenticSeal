# Review round 2: 1793795355-the-census-reads-every-entry-point

```seal
target: 93c257765, fixes 79d50f5ca..93c257765
```

This verifying round reads the diff `79d50f5ca..93c257765`: `bc6d3387a`,
`6c77082d6` and `705109345` (the fix pass's code and cases), `fdd342bb8`
(two docstrings and the fragment), `15e7fd5eb` (the close blocks) and
`93c257765` (the orchestrator's fold of `frame/design.md` *Scope* items 4
and 6, `frame/plan.md` *Operational impact* and a row of *Judgments of the
run*). The runs took place in a `git clone --no-local` of the worktree at
`93c257765`, under the session scratchpad, and the clone is removed before
the hand-back. `seal/config.md` has no `Record language` row, so this
record is English, and no `seal/parity.md` exists, so no comparison with an
original is owed.

Carried from round 1, not re-established: that every entry point gives the
answer at HEAD (round 1's probe over the 48 entry points), the exemptions'
reasons, the removal of the run-time case, and the corpus and pair
comparison of the census. The fix diff touches no entry point script and no
line of `tests/censuses.py` outside the two messages and two docstrings
(`git diff --stat 79d50f5ca..93c257765`, executed), so none of those checks
has a reason to fail. Re-derived this round: both closes, the wording of
the two messages against what the census reads, the new case against its
group, and every sentence the fix pass and the fold added.

The axes for this diff: what each refusal tells a contributor; whether each
new sentence of the frame, the fragment, the docstrings and `CONTRIBUTING.md`
is true of the census at HEAD; whether each arm of the new case pins its own
guard; and what the text pin holds against *The checks*. Authorization,
query scope, concurrency and security do not apply: the diff changes text
the census prints and cases that read it.

## Findings

### 1. The fold and the fragment say each refusal states what the census did not read, and the order refusal states what it read

```seal
severity: should
location: `seal/threads/1793795355-the-census-reads-every-entry-point/frame/plan.md:91-93`, `seal/threads/1793795355-the-census-reads-every-entry-point/changelog.md:3`
evidence: read `seal/threads/1793795355-the-census-reads-every-entry-point/frame/plan.md:91-93`, `seal/threads/1793795355-the-census-reads-every-entry-point/changelog.md:3`, `tests/censuses.py:762-767`, `seal/threads/1793795355-the-census-reads-every-entry-point/trail/rounds/round-1.md:72-74`; executed `git grep -n -i 'refusal says'`
regression: round-1#1
```

Why it matters: the units are the sentence `93c257765` added to
`frame/plan.md` *Operational impact*, "What it reads", and the sentence
`fdd342bb8` added to the fragment's first bullet. Design *Scope* item 3
names three refusals, and round-1#1 faulted two of them, so the fix stated
of all three what holds of two, and the defect came from widening the
finding's two messages to every refusal. The plan says "each refusal says
what the census did not read rather than that the file gives no answer".
The fragment says "A refusal says what the census did not read, not that
the script gives no answer". The order refusal at `tests/censuses.py:762-767`
says "the `__main__` block's answer, at line N, is not its first
statement". That states what the census read: an answer, and its line. It
names nothing the census did not read. Round 1 said so ("states only what
the census read, and it stands", `round-1.md:72-74`). The plan's line is
what the pull request body carries under *What it reads*, by
`CONTRIBUTING.md` *What a change to a gate must carry*, and the fragment is
the release note a person reads, so both tell a reader something about the
third refusal that its text does not do.

```markdown
  - What it reads: the first module-level `__main__` block of each tracked
    `.py`, through `ast`. A statement in neither of the two forms is not
    read as an answer. The refusal at the `if` line and the refusal at the
    `for` line each say what the census did not read rather than that the
    file gives no answer, and the refusal at the block's first statement
    names the line of the answer it read.
```

```markdown
The refusal at the `if` line and the refusal at the `for` line say what the census did not read, not that the script gives no answer: a call nested under another statement, or a loop over `console.STREAMS`, gives the answer and is refused, because the census reads neither spelling.
```

The second fence replaces the fragment's sentence that opens "A refusal
says what the census did not read" in `changelog.md:3`, and nothing else
in that bullet. No other statement of the claim stands in the work item:
`git grep -n -i 'refusal says'` over the tree lists these two lines, the
fold's row of *Judgments of the run* at `frame/plan.md:105`, which says
*Operational impact* "states what a refusal says" and claims nothing of
the third, and round 1's close at `round-1.md:137`, which describes the two
messages alone (executed).

```seal
verdict: fixed 6e22d54f7
answer: The finding holds. The order refusal at `tests/censuses.py:762-767` names the answer the census read and that answer's line, so neither sentence was true of it. The plan half is the orchestrator's fold at `a483cbb43`. In the fragment, f4ac057ae replaces the sentence that opened "A refusal says what the census did not read". The new sentence says this of the refusals at the `if` line and at the `for` line alone, and it adds that the refusal at the block's first statement names the line of the answer the census read there. Reading the bullet again, the next sentence, "Each refusal names the forms it accepts", made the same overreach: the order refusal names no form. 6e22d54f7 makes it "The refusals at the `if` line and at the `for` line name the forms the census reads, and each refused line can be exempted". Both commits touch `changelog.md` alone. `grep -n -i 'each refusal\|every refusal'` over `changelog.md` and `gaps.md` then listed nothing (executed). `tests/github/test_publish_release_note.py` and `tests/behaviour/test_chain_hooks_hardening.py` passed at 6e22d54f7, 80 cases (executed).
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the two messages now say what the census did not read. The
no-answer refusal at `tests/censuses.py:749-757` says "the census reads no
answer among the `__main__` block's own statements", and the loop refusal
at `tests/censuses.py:771-777` says "the census does not read this loop as
the answer `hooks/lib/console.py#STREAMS` holds" (read). Round 1's probe
was written again from its `## Probes` row for the shapes that drew the two
messages, and the census printed each line (executed). A loop over
`console.STREAMS`, a `list` literal of the pairs, and a loop with an
`else:` clause each drew the loop refusal at line 2. `if True:` around the
call drew the no-answer refusal at line 1. A loop of drifted pairs, and a
block of `main()` alone, drew the same two messages, and both are true of
those as well. The fix pass claimed its reason for not applying round 1's
text as given: the no-answer message round 1 proposed kept "a loop over
the pairs `hooks/lib/console.py#STREAMS` holds", which admits the
`console.STREAMS` loop. That holds: round 1's snippet at `round-1.md:91-92`
says so (read), and the message at HEAD names "the one form
`tests/censuses.py#loop_pairs` reads" in its place. `CONTRIBUTING.md:425-427`
names the same one form, and `tests/censuses.py#loop_pairs` resolves to the
function at `tests/censuses.py:664` (read). The text pin now holds "opens its
first such block with the answer" and "the one form
`tests/censuses.py#loop_pairs` reads". Each is a fact a reader acts on, the
first block and where the form is read, rather than the sentence's
wording, as *The checks* in `docs/running/what-a-script-gates.md` asks. The
pin went red with `CONTRIBUTING.md` given "the same pairs" again (executed,
`bin/seal mutate`). The two docstrings at `tests/censuses.py:742-745` and
`:788-792` and the fragment's third bullet say what the census reads
(read). `frame/design.md` *Scope* item 6 is folded to the bullet as it
stands (read). The claim that the fix makes each refusal say what the
census did not read went further than the two messages, and that is
finding 1.

```seal
confirms: round-1#2
```
What holds: `test_refuses_a_loop_whose_target_is_not_two_names_at_its_for_line`
at `tests/test_censuses.py:665-675` plants the one-name, three-name and
nested targets, with ids `one-name`, `three-names` and `nested`, and expects
the refusal at line 2 (read). Round 1's evidence was re-run as one batch
against `-k Test_entry_point`. Each of the three guard mutations, which
each printed `SURVIVED` in round 1, is now red (executed). The fix pass
claimed each arm was red with only its own guard removed. That holds: one
`bin/seal mutate` run per guard against its arm's node id alone turned
`one-name` red with `AttributeError` at `tests/censuses.py:675`,
`three-names` red with `ValueError` at `:679`, and `nested` red with
`AttributeError` at `:679` (executed). Each failure is the census raising at
the line its guard keeps it from, so each arm pins its own guard. The case
is read against its group: `test_refuses_a_loop_of_another_shape_at_its_for_line`
at `:657` covers the iterable and the `reconfigure` call, not the target,
so the new case covers what no other case did. `seal layout --pairs` names
no pair for `tests/test_censuses.py` (executed). `frame/design.md` *Scope*
item 4 now lists the case (read).

What matched: the fold's row of `frame/plan.md` *Judgments of the run* names
the folds the diff makes to *Scope* items 4 and 6 and to *Operational
impact*, and cites `skills/implement/orchestration.md` (read). *Scope* item
6 says the pin "pins three facts of the bullet". The pin holds six
assertions of that bullet, three of which the fix pass's commit wrote or
kept for the entry-point sentence. Read either way, no party acts on the
count, so it is no finding.

What matched: the three modules of the plan's *Verified by* cells passed,
`tests/test_censuses.py`, `tests/hooks/test_console.py` and the text pin,
with 201 passed, the 198 of round 1 and the three new arms (executed).
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` and
`tests/behaviour/test_docs_line_wrap.py` passed over the rewrapped bullet,
90 passed (executed). No hand-back claims the suite, so the suite's label
is honest.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite, the lint and the typecheck at HEAD: `unverified` by this round (contract rule 2) | the branch at 93c257765 | the orchestrator, at its broad run |
| Whether the loop form should also require the `hasattr` guard, carried from round 1's `## Not judged`; the fold answers it nowhere (read: `frame/plan.md` *Judgments of the run*) | `tests/censuses.py:664-704` | the orchestrator, as a fold of design *Scope* item 2 or a follow-up |
| The seventeen repaired scripts under a cp949, cp932 or cp936 console on Windows, carried from `gaps.md` *Not verified* | `gaps.md` | the repository owner, on a Windows console |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/test_censuses.py tests/hooks/test_console.py tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` | 201 passed |
| `bin/seal mutate tests/censuses.py` with the three target guards of `loop_pairs` as one batch (`== 2` made `>= 2`, `isinstance(target, ast.Tuple)` made `True`, the `ast.Name` check made `True`), `--tests "bin/test -q -p no:xdist tests/test_censuses.py -k Test_entry_point"` | `3 mutants, 3 red, 0 SURVIVED`, the file restored |
| a first attempt at the three per-arm runs, whose `--tests` lost its node id to the shell's subscript expansion and so began the suite unscoped | stopped after about 180 seconds by the round, before any result; the clone showed no change and no process from it remained (executed: `git status`, `ps`). Nothing is taken from it |
| `bin/seal mutate tests/censuses.py` once per guard, `--tests` naming the one arm's node id (`[one-name]`, `[three-names]`, `[nested]`) | each `red`: `AttributeError` at `:675`, `ValueError` at `:679`, `AttributeError` at `:679` |
| `bin/seal mutate CONTRIBUTING.md --replace` with "`tests/censuses.py#loop_pairs` reads. The" made "the same pairs. The", `--tests` the text pin | `red`, at the assertion of the one form |
| `bin/test -q -s -p no:xdist -p no:cacheprovider tests/test_tmp_round2_probe.py`, a probe that plants six shapes under `hooks/` and prints `censuses.entry_point` for each | `console.STREAMS`, a `list` literal, `for`-`else` and drifted pairs: the loop refusal at line 2; `if True:` around the call and `main()` alone: the no-answer refusal at line 1. The file was deleted after the run |
| `bin/test -q tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py` | 90 passed |
| `bin/seal layout --pairs` | no pair names `tests/test_censuses.py` |

# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — review round 3

target: 6429ce35, fixes 15b7fa76..6429ce35

## Findings

### 1. The interpreter-floor case is red since phase 2, and the two `ruff.toml` lines alone leave it red

severity: must
location: `tests/test_a_script_says_which_interpreter_it_needs.py:433`, `ruff.toml:46`, `skills/code-review/scripts/chain_check.py:893`
verdict: fixed 4d777c78

Why it matters. `test_what_runs_before_any_floor_needs_nothing_its_python3_lacks`
fails on this branch, so the pull request's test legs fail on it. The case
derives the set of files that run on whatever `python3` starts them, a hook
and every module it loads in its own process, and holds each one to
`ruff.toml`'s `per-file-target-version` and to the syntax that version has.
Phase 2's writer put two files into that set: `seal_stamp._chain_check`
loads `skills/code-review/scripts/chain_check.py` from git's `post-commit`,
and `chain_check.py:72` loads `skills/verify/scripts/unverified_check.py`.
Neither is in the table. This is a unit a build phase made, so it is new
work and takes no `regression:` line. No phase, round or fix pass ran this
module; phase 5 probed six other inventory modules and not this one.

The orchestrator's message to this round claimed the cause and a fix of two
`ruff.toml` lines. The cause holds; the fix does not, on its own.

Executed (probe rows 6 to 8):

- The case passes at the base `f6ae6db6` and at `ddb5cf1a`, phase 1's
  record. It fails at `3a8e9b0e`, phase 2's writer and the next commit, and
  at `0dd09a37` and `6429ce35`, with
  `['skills/code-review/scripts/chain_check.py',
  'skills/verify/scripts/unverified_check.py'] run before any floor is
  checked`. So the writer is the cause.
- With the two lines added to `ruff.toml`, the same case still fails, at
  its next assertion: `{'skills/code-review/scripts/chain_check.py': [(893,
  '`zip(..., strict=...)`')]} run on whatever python3 starts them, and need
  a newer one`. `zip`'s `strict=` is Python 3.10.
- With the two lines and line 893 without `strict=False`, the module and
  `tests/test_chain_check.py` pass (84), and `ruff check` and `ruff format
  --check` of both files pass under the edited table (ruff 0.17.1).
- Under Python 3.9.6, the three modules import, and
  `seal_stamp.queue_for_guarantee` over a fixture holding a `sealed`
  guarantee returns its one line. So `finding_spans`, which holds line 893,
  is not reached on the writer's path today, and the stamp is not lost at
  3.9; the case refuses the file because the file now runs there, not
  because this path raised.

The fix, in `ruff.toml` after line 46:

```toml
"skills/verify/scripts/seal_stamp.py" = "py39"
"skills/code-review/scripts/chain_check.py" = "py39"
"skills/verify/scripts/unverified_check.py" = "py39"
```

And `skills/code-review/scripts/chain_check.py:893`, which ruff no longer
asks for `strict=` once the file is linted at 3.9:

```python
    return (start, end), list(zip(heads, [*heads[1:], end])), None
```

answer: `ruff.toml`'s `per-file-target-version` gains `chain_check.py` and `unverified_check.py` at `py39`, and `chain_check.py:893`'s `zip` drops `strict=`, as the record gives them. The class beyond what ruff reads, enumerated over the post-commit path (`hooks/commitgate.py`, `seal_stamp.py`, `chain_check.py`, `unverified_check.py`): `uvx vermin --target=3.9- --violations --eval-annotations` reports a minimum of 3.8 and no target missed, and the same command over HEAD's `chain_check.py` reports 3.10 and `Target versions not met`, so it can fail; and `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` with `tests/test_chain_check.py` run under `/usr/bin/python3` 3.9.6 gave 122 passed and 4 failed, each failure a `zip(..., strict=True)` in a test file (`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:983`, `tests/test_chain_check.py:1000`, `:1132`, `:1412`), which no floor covers since tests run on the runner's interpreter, and none in the four modules. executed: `test_what_runs_before_any_floor_needs_nothing_its_python3_lacks` red at b81de037 naming the two files, green after; `bin/test tests/test_a_script_says_which_interpreter_it_needs.py tests/test_chain_check.py -q` 84 passed; `uvx ruff check` of `ruff.toml` and the three scripts, and `uvx ruff format --check` of the two, exit 0

### 2. A second clone of the same branch draws the work item's stamp again for a commit that edits a sealed guarantee or re-seals with a fresh row

severity: should
location: `skills/verify/scripts/seal_stamp.py:1071-1083`, `docs/the-review-record.md:281-291`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`
verdict: fixed 076b1ee4
reopens: round-1#3

Why the close does not hold. Round 1's finding 3 was that once per work item
rests on a row an agent writes and on one clone's files. 33a5b676 closed the
same-clone re-seal and the squash elsewhere, and left the second clone of the
same branch to the `Target SHA` row's `; earlier run: <sha> sealed`, the row
the finding named as unchecked. Round 2 left that shape as a row of
`## Not judged`; this round reached it by a probe. In a second clone the
values directory is empty, so `already_queued` answers False, and the
audited commit is an ancestor, so the `merge-base` test passes.

Why it matters. The owner's rule is one stamp per work item, drawn from the
sealer's `sealed`. A session that resumes on another machine is the second
clone; this repository's runs have done that.

Executed (probe rows 2 to 4, `test_tmp_*` files over the module's own
fixtures, each run once and deleted):

- A `sealed` guarantee is committed and queued in one clone. In a
  `git clone --no-local` of it, on `feat/x`, a commit appends a line to the
  guarantee with no new run: `post-commit` queues a second stamp.
- In the same second clone, a fix is committed and the guarantee rewritten
  `sealed` at the new commit with its row written fresh, round 1's P1 shape:
  a second stamp is queued.
- For contrast, the same re-seal with `; earlier run: <target> sealed` kept
  queues nothing, and a `withheld` then `sealed` in one clone queues one.

The history of the guarantee is in the tree and in every clone, so it holds
across clones without the row. A guarantee that read `sealed` at any earlier
commit of HEAD's history was stamped where that commit was made. With the
change below, both second-clone commits queue nothing, `withheld` then
`sealed` still queues one, and
`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`,
`tests/test_the_commit_gate_decides_at_the_commit.py` and
`tests/test_every_reader_ends_a_line_where_gfm_does.py` stay green (261
passed with the case below; the one failure was finding 1's case, untouched
by this change). `ruff check` and `ruff format --check` of the file pass.

Not closed by it, and said so: an amend of the sealing commit itself in a
second clone still queues, since that commit's parent predates the
guarantee. The fail direction stays a missing stamp: a `sealed` committed
where no stamp could be drawn (a foreign hooks slot, a person's own commit)
means no later commit draws one.

In `skills/verify/scripts/seal_stamp.py`, before `_queue_one`. It reads git
output with `split()`, so the reader inventory needs no entry; `git log`
from a root commit exits 128, `_git` returns None and the history is empty:

```python
def sealed_before(chain, top, path):
    """True where `path` read one `Verdict:` of `sealed` at a commit before
    HEAD in HEAD's history. That commit was stamped where it was made, in
    this clone or another, so what the history carries holds across clones
    and asks nothing of the row an agent writes. A root commit has no
    parent: `git log` exits 128 and the history is empty."""
    reader = chain.SHARED_READER
    for sha in (_git(top, "log", "--format=%H", "HEAD^", "--", path) or "").split():
        text = _git(top, "show", f"{sha}:{path}")
        if text is None:
            continue
        verdicts = chain.verdicts_of(reader, text)
        if len(verdicts) == 1 and chain.verdict_word(verdicts[0][1]) == chain.SEALED:
            return True
    return False
```

In `_queue_one`, after the earlier-run check at line 1071:

```python
    if any(word == chain.SEALED for _sha, word in chain.earlier_verdicts(cell)):
        return None
    if sealed_before(chain, top, f"{rel}/guarantee.md"):
        return None
```

The case, after `test_a_squash_of_a_sealed_item_in_another_clone_queues_nothing`.
It failed at 6429ce35 (the body edit queued a line) and passed with the change
above (probe rows 4 and 5):

```python
def test_a_sealed_item_recommitted_in_another_clone_queues_nothing(tmp_path):
    """#975 round 3, once per work item. The guarantee was stamped in one
    clone. In a second clone of the same branch, a commit that edits the
    sealed guarantee with no new run, and a re-seal whose row lost its
    earlier run, each find `sealed` earlier in the guarantee's history, so
    nothing is queued. Red at 6429ce35: the second clone held no values
    file, so each queued one."""
    repo, _target, base = guaranteed(tmp_path)
    assert after_the_commit(repo)
    other = tmp_path / "other"
    subprocess.run(
        ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
    )
    git(other, "switch", "-q", "feat/x")
    item = other / "seal" / "specs" / ITEM_NAME / "guarantee.md"
    item.write_text(item.read_text(encoding="utf-8") + "\na note\n", encoding="utf-8")
    commit_all(other, "a note in the guarantee, no new run")
    assert after_the_commit(other) == ""
    (other / "x.txt").write_text("a fix after the seal\n", encoding="utf-8")
    commit_all(other, "a fix")
    new = git(other, "rev-parse", "--short", "HEAD").stdout.strip()
    item.write_text(guarantee_text(new, base, "sealed"), encoding="utf-8")
    commit_all(other, "the sealer again, its row written fresh")
    assert after_the_commit(other) == ""
    assert queued(other) == []
```

The sentence in `docs/the-review-record.md` §*The stamp* that states the
rule, with the case added to its `Enforced by:` line. In the same commit,
`overview.md`'s third `## Not verified` row, which this closes, goes, and the
fragment's "already stamped in this clone" can say "in this clone or another
of the same branch":

```text
nothing. `withheld` and `undecided` queue nothing. Once per work item is held
by what the clone and the tree carry, with no count beside them: a values
file already named for the work item, pending or drawn, under any session's
directory is not written twice, whatever commit it named; a commit whose
audited commit is not in its own history, a squash or a cherry-pick of the
guarantee elsewhere, queues nothing; and a guarantee that read `sealed` at an
earlier commit of that history, or whose `Target SHA` row's `; earlier run:`
chain reads `sealed`, was stamped then, which holds across clones. The stamp
carries what the records at the
```

answer: `seal_stamp.sealed_before` and its call in `_queue_one` are added as the record gives them, `queue_for_guarantee`'s docstring names the condition, and the module's once comment now names four facts and the amend left out. `docs/the-review-record.md` §*The stamp* carries the record's sentence and the case on its `Enforced by:` line. That section states how once is held and lists no limits of it, so the amend of the sealing commit in a second clone is stated in `overview.md` §*Where spec and implementation diverged* as a limit, by the orchestrator's decision, and not in the document. `overview.md`'s third `## Not verified` row opens with `closed` rather than being removed, since `unverified-check` counts rows, and §*Fed back into the spec* gains the fact. The fragment says a stamped work item draws nothing more in another clone of the same branch too, with the amend as its one exception. executed: `test_a_sealed_item_recommitted_in_another_clone_queues_nothing` red at b81de037 (the body edit queued a line), green after; `mutation-check` of `sealed_before` five ways (the call made `if False:`, the verdict word, the path, `-n0` on the log, and `HEAD^` made `HEAD` against `test_a_reseal_after_withheld_queues_the_stamp`), each `red`; the stamp, commit-gate, reader, interpreter-floor, line-wrap, pasted-passage, changelog, record-words, one-word, release-hygiene and real-identifier modules 440 passed; `bin/rules --check` exit 0; `uvx ruff check` and `uvx ruff format --check` exit 0. Not seen red alone: the case's second commit, the fresh-row re-seal, since the body edit before it queues first at b81de037; the record's probe row 2 saw that shape queue on its own

## Confirmations

confirms: round-2#1
The ten sentences and the two messages read as the record gave them (read,
the fix diff), and the two further messages and the docstring the answer
names follow too. The class was swept again from the tree, not from the
answer (executed, probe row 9): a phrase search for the broad run named a
seal over every tracked file outside the records and changelogs found only
the pin that holds `broad seal` absent, and every remaining `seal` word in
`README.md`, `README.ko.md`, `skills/verify/SKILL.md` and
`docs/the-broad-gate.md` names a command, the root, the concept, a claim
held to the Seal Test, or the sealer's or the smith's seal. The pins pass
(probe row 1).

confirms: round-2#2
Line 431 reads `\bseal[-_.]\w[\w.-]*` and the case is added as given (read).
Against the line as it stood at 15b7fa76, four sentence-final lines were not
refused: the case's two, `the seal...` and `seal."`. With the new line each
is refused, and `seal-stamp --from`, `seal_stamp.py` and `seal-mark.txt` are
still taken out (executed, probe row 10). The module passes (probe row 1).
The limit of an enumeration stays, and is not new: a hyphenated prose
compound such as `seal-like` or `seal-free` is still taken out as a name
(executed, same row). None stands in the four swept files, since the
construction case is green.

confirms: round-2#3
`overview.md` §*Where spec and implementation diverged* carries the row
round 2 gave, citing `phases/phase-4.md` and round 2's finding 3 (read).
`spec.md` is unedited, which `skills/implement/SKILL.md:343-346` and `:400`
support: `spec.md` is the framer's and a divergence goes to the builder's
memo with both sides quoted. The overview case passes (probe row 1).

confirms: none
The changelog fragment's sealer row matches its records. `side_numbers`
over #969's `evals/reference-sealer.json` and this item's
`evals/sealer-phase-4.json` gives 24,702 and 24,700 bytes; 2,855,195 / 77
and 3,239,330 / 90 tokens per call, 37,080.5 and 35,992.6; spend 3.3898 and
3.5731; 68 of 68 grader passes on each side (34 graders, 2 runs); 10 runs
each, none cut short; suite tree `5c3e8119` on both, at `1483d8ba` and
`981b0acc` (executed, probe row 11). The sha256 of `agents/sealer.md` and
`skills/agent-contract/SKILL.md` at 6429ce35 equal the measured side's
preload, so the measurement at 981b0acc stands for HEAD's definition
(executed). `tests/test_a_rewritten_definition_proved_non_inferior.py`
passes (probe row 1). The fragment's quoted `post-commit` line is
`seal_stamp.QUEUED`, which `test_a_sealed_guarantees_commit_queues_one_stamp`
pins (read; passes, probe row 1).

confirms: none
3820f7bb's two `OUT_OF_CLASS` entries hold.
`test_every_splitlines_call_left_is_named_with_its_reason` fails at 15b7fa76
on `queue_for_guarantee` and `_queue_one`, passes at 6429ce35, and passes at
`ddb5cf1a`, before phase 2 (executed, probe row 12).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck: `unverified` by this round. The orchestrator's message reports one run of the suite at 6429ce35 with one failure, finding 1; that is its claim, not this round's run, and an edit follows it | — | the orchestrator's broad run, after the rounds settle |
| Whether an amend of the sealing commit in a second clone, which finding 2's change leaves queueing, is worth closing too | `skills/verify/scripts/seal_stamp.py:1071-1083` | the orchestrator, under the owner's delegation |

## Probes

| Command | Result |
|---|---|
| `bin/test` of `test_one_word_one_meaning.py`, `test_broad_gate_rule.py`, `test_the_gate_names_every_step_ci_runs.py`, `test_every_reader_ends_a_line_where_gfm_does.py`, `test_chain_hooks_hardening.py`, `test_docs_line_wrap.py`, `test_no_passage_is_pasted_into_a_second_file.py`, `test_release_hygiene.py`, `test_the_changelog_is_gathered_at_release.py`, `test_a_rewritten_definition_proved_non_inferior.py`, `test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `test_no_real_identifiers.py`, `test_the_record_is_written_in_words.py` with `-q`; then `bin/test tests/test_the_seal_is_taken_once_by_the_sealer.py -q -k` over the three changed messages' cases; then `bin/rules --check`, in the round's clone at 6429ce35 | 430 passed, exit 0; 5 passed, exit 0; exit 0, 494 targets in 60 files resolve |
| `tests/test_tmp_round3_second_clone.py`, four cases over the stamp module's fixtures, `-s -p no:xdist`, at 6429ce35 | a body edit in a second clone queued a line; a fresh-row re-seal in a second clone queued a line; a chained re-seal queued nothing; `withheld` then `sealed` in one clone queued one |
| the same file with `sealed_before` added to the clone's `seal_stamp.py`; then the stamp, commit-gate and reader modules | body edit and fresh-row re-seal queued nothing; the other two as before; 255 passed, exit 0 |
| `tests/test_tmp_round3_case.py`, finding 2's case, at 6429ce35 | 1 failed, exit 1, the body edit's line queued |
| the same case with `sealed_before` in place, with the stamp, commit-gate, reader and interpreter-floor modules; `uvx ruff check` and `uvx ruff format --check` of `seal_stamp.py`; then the file restored and the case deleted | 1 failed (finding 1's case), 261 passed; ruff exit 0 and 0; `git status` clean |
| `bin/test tests/test_a_script_says_which_interpreter_it_needs.py -q`, then `-k test_what_runs_before_any_floor_needs_nothing_its_python3_lacks` at `f6ae6db6`, `ddb5cf1a`, `0dd09a37` and back at 6429ce35 | 1 failed, 5 passed at 6429ce35; passed at `f6ae6db6` and `ddb5cf1a`; failed at `0dd09a37` and at 3a8e9b0e |
| the two `ruff.toml` lines added alone, the module run | 1 failed, 5 passed: `chain_check.py` line 893, `zip(..., strict=...)` |
| the two lines and line 893 without `strict=False`; `bin/test tests/test_a_script_says_which_interpreter_it_needs.py tests/test_chain_check.py -q`; `uvx ruff check` (0.17.1) of both files and `ruff.toml`, `uvx ruff format --check` of `chain_check.py`; both files restored | 84 passed, exit 0; ruff exit 0 and 0; `git status` clean |
| `uv run --no-project --python 3.9` importing `chain_check.py`, `unverified_check.py` and `seal_stamp.py`, then a `test_tmp_*` script calling `queue_for_guarantee` over a fixture with a `sealed` guarantee; the script deleted | 3.9.6; all three import; one line returned |
| `git grep -n -i -E` of `broad seal`, `seal taken before`, `seals a tree`, `sealing the whole`, `those seals`, `that seal and`, `seal that covers`, `it sealed over`, `gate sealed` and a run within twenty characters of a seal word, outside `seal/specs`, `changelog`, `CHANGELOG.md` and JSON; `grep -n -w` of the seal words in the two READMEs, `skills/verify/SKILL.md` and `docs/the-broad-gate.md` | one hit, `tests/test_broad_gate_rule.py:55`, the pin; every word read as a command, the root, the concept or a named party's seal |
| `tests/test_tmp_round3_sweep.py`, ten lines through `GATE_SEAL_NAMES` and through the same pattern with 15b7fa76's alternative, `-s -p no:xdist`; deleted after | both of the case's lines, `the seal...` and `seal."` refused now and not then; `seal-like` and `seal-free` taken out by both |
| `python3 -I` with `noninferiority.side_numbers` over `reference-sealer.json` and `sealer-phase-4.json`; `shasum -a 256 agents/sealer.md skills/agent-contract/SKILL.md`; the script deleted | the figures in the first `confirms: none` entry; both hashes equal the new side's preload |
| `bin/test tests/test_every_reader_ends_a_line_where_gfm_does.py -q -k test_every_splitlines_call_left_is_named_with_its_reason` at 15b7fa76 and at `ddb5cf1a` | failed at 15b7fa76 on the two units; passed at `ddb5cf1a` |
